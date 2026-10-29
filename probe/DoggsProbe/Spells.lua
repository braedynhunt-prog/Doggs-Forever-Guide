-- DoggsProbe / Spells.lua
-- Spell probe: on login / level-up / gear change (and /probe scan) walk the spellbook, find the
-- highest known rank of each watched spell and store id, rank, description (the tooltip numbers),
-- mana cost and the spell power / crit the character had at that moment. Readings are deduped,
-- so a gear swap that changes spell damage produces exactly one new reading per spell.

local ADDON, NS = ...
local API = NS.API

local Spells = {}
NS.Spells = Spells

-- names are matched case-insensitively; unknown names cost nothing
Spells.watch = {
	"Earth Shock", "Flame Shock", "Frost Shock",
	"Lightning Shield", "Lightning Bolt", "Chain Lightning",
	"Healing Wave", "Lesser Healing Wave",
	"Rockbiter Weapon", "Flametongue Weapon", "Frostbrand Weapon", "Windfury Weapon",
	"Stormstrike", "Water Shield", "Healing Stream Totem", "Mana Spring Totem",
	"Searing Totem", "Stoneskin Totem", "Strength of Earth Totem",
}
Spells.imbues = { "Rockbiter Weapon", "Flametongue Weapon", "Frostbrand Weapon", "Windfury Weapon" }

local READINGS_CAP = 24
local watchSet = {}
for _, n in ipairs(Spells.watch) do watchSet[string.lower(n)] = n end
local imbueSet = {}
for _, n in ipairs(Spells.imbues) do imbueSet[string.lower(n)] = n end

local function rankNumber(sub)
	if type(sub) ~= "string" then return nil end
	local r = sub:match("(%d+)")
	return r and tonumber(r) or nil
end

-- returns { [lowerName] = { id, name, rank, rankText } } for the highest rank of every spell,
-- and the api path string. Also refreshes NS.char.spellbook (id -> "Name (Rank N)").
function Spells.WalkBook()
	local best = {}
	local book = {}
	local count = 0
	local path = API.ForEachSpellBookSpell(function(id, name, sub)
		id = NS.SafeNumber(id)
		name = NS.SafeString(name)
		if not id or not name then return end
		sub = NS.SafeString(sub)
		if not sub or sub == "" then sub = API.SpellSubtext(id) end
		local rank = rankNumber(sub)
		count = count + 1
		book[id] = name .. ((sub and sub ~= "") and (" (" .. sub .. ")") or "")
		local key = string.lower(name)
		local cur = best[key]
		if not cur or (rank or 0) >= (cur.rank or 0) then
			best[key] = { id = id, name = name, rank = rank, rankText = sub }
		end
	end)
	NS.char.spellbook = book
	NS.char.spellbookCount = count
	NS.char.spellbookApi = path
	return best, path
end

local function currentPower()
	local sp = {}
	for i, school in ipairs(NS.SCHOOL_NAMES) do
		local ok, v = pcall(GetSpellBonusDamage, i)
		if ok then sp[school] = NS.SafeNumber(v) end
	end
	local okH, heal = pcall(GetSpellBonusHealing)
	local crit = {}
	for i, school in ipairs(NS.SCHOOL_NAMES) do
		local ok, v = pcall(GetSpellCritChance, i)
		v = ok and NS.SafeNumber(v) or nil
		if v then crit[school] = math.floor(v * 100 + 0.5) / 100 end
	end
	local okAP, base, pos, neg = pcall(UnitAttackPower, "player")
	local ap = (okAP and NS.SafeNumber(base)) and ((base or 0) + (pos or 0) + (neg or 0)) or nil
	local _, _, int = pcall(UnitStat, "player", 4)
	return sp, okH and NS.SafeNumber(heal) or nil, crit, ap, NS.SafeNumber(int)
end

local function reading(entry)
	local desc = API.SpellDescription(entry.id)
	local mana, costs = API.SpellCost(entry.id)
	local sp, heal, crit, ap, int = currentPower()
	local lvl = NS.SafeNumber(UnitLevel("player"))
	local r = {
		id = entry.id, name = entry.name, rank = entry.rank, rankText = entry.rankText,
		desc = desc, mana = mana, costs = costs,
		spNature = sp.nature, spFire = sp.fire, spFrost = sp.frost, heal = heal,
		critNature = crit.nature, critFire = crit.fire, critFrost = crit.frost,
		ap = ap, int = int, lvl = lvl, t = time(),
	}
	local info = API.SpellInfo(entry.id)
	if info then r.castTime = info.castTime end
	r.key = table.concat({ tostring(r.id), tostring(r.desc), tostring(r.mana), tostring(r.spNature), tostring(r.spFire),
		tostring(r.spFrost), tostring(r.heal), tostring(r.lvl), imbueSet[string.lower(entry.name)] and tostring(r.ap) or "" }, "|")
	return r
end

local needRetry = false

-- take readings for every watched spell that is in the book. Returns number of new readings.
function Spells.Scan(reason)
	local best = Spells.WalkBook()
	local spells = NS.char.spells
	local new, empty = 0, 0
	for key, entry in pairs(best) do
		if watchSet[key] then
			local r = reading(entry)
			r.reason = reason
			if not r.desc or r.desc == "" then
				empty = empty + 1
				API.RequestSpellData(entry.id)
			end
			local rec = spells[entry.name]
			if not rec then
				rec = { readings = {} }
				spells[entry.name] = rec
			end
			rec.id = entry.id
			rec.rank = entry.rank
			rec.latest = r
			local dup = false
			for _, old in ipairs(rec.readings) do
				if old.key == r.key then dup = true; break end
			end
			if not dup and r.desc and r.desc ~= "" then
				rec.readings[#rec.readings + 1] = r
				while #rec.readings > READINGS_CAP do table.remove(rec.readings, 1) end
				new = new + 1
			end
		end
	end
	if empty > 0 and not needRetry then
		needRetry = true
		C_Timer.After(3, function()
			needRetry = false
			NS.SafeCall("spells:retry", Spells.Scan, (reason or "scan") .. "-retry")
		end)
	end
	NS.char.spellsLastScan = time()
	if new > 0 or NS.debug then
		NS.Printf("spell probe (%s): %d new reading(s), %d spell(s) watched, %d in book%s",
			tostring(reason), new, Spells.WatchedCount(), NS.char.spellbookCount or 0,
			empty > 0 and (", " .. empty .. " description(s) not loaded yet, retrying") or "")
	end
	return new
end

function Spells.WatchedCount()
	local n = 0
	for _ in pairs(NS.char.spells) do n = n + 1 end
	return n
end

-- current tooltip text of the imbue spells (stored next to each Rockbiter AP delta)
function Spells.ImbueReadings()
	local out = {}
	for name, rec in pairs(NS.char.spells) do
		if imbueSet[string.lower(name)] and rec.id then
			out[name] = { id = rec.id, rank = rec.rank, desc = API.SpellDescription(rec.id) }
		end
	end
	return out
end

function Spells.Report()
	local lines = {}
	local names = {}
	for name in pairs(NS.char.spells) do names[#names + 1] = name end
	table.sort(names)
	for _, name in ipairs(names) do
		local rec = NS.char.spells[name]
		local r = rec.latest
		if r then
			local desc = r.desc or "(no description)"
			if #desc > 160 then desc = desc:sub(1, 157) .. "..." end
			lines[#lines + 1] = string.format("%s R%s (id %d): mana %s | SP nat/fire/frost %s/%s/%s heal %s | %d reading(s) | %s",
				name, tostring(r.rank or "?"), r.id, tostring(r.mana or "?"), tostring(r.spNature or "?"), tostring(r.spFire or "?"),
				tostring(r.spFrost or "?"), tostring(r.heal or "?"), #rec.readings, desc)
		end
	end
	return lines
end

-------------------------------------------------------------------------------
-- Triggers
-------------------------------------------------------------------------------
local prevEnter = NS.OnEnterWorld
NS.OnEnterWorld = function(...)
	if prevEnter then prevEnter(...) end
	C_Timer.After(5, function() NS.SafeCall("spells:login", Spells.Scan, "login") end)
end

NS.On("PLAYER_LEVEL_UP", function() NS.Debounce("spells:levelup", 3, function() Spells.Scan("levelup") end) end)
NS.On("PLAYER_EQUIPMENT_CHANGED", function() NS.Debounce("spells:equip", 3, function() Spells.Scan("equip") end) end)
NS.On("LEARNED_SPELL_IN_TAB", function() NS.Debounce("spells:learned", 3, function() Spells.Scan("learned") end) end)
NS.On("SPELLS_CHANGED", function() NS.Debounce("spells:changed", 6, function() Spells.Scan("spells_changed") end) end)
NS.On("CHARACTER_POINTS_CHANGED", function() NS.Debounce("spells:talent", 4, function() Spells.Scan("talent") end) end)
