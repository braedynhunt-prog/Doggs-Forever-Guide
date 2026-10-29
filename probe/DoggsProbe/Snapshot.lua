-- DoggsProbe / Snapshot.lua
-- Character-sheet snapshots (login, level-up, gear change, imbue change, /probe) and the
-- Rockbiter AP watcher (AP just before vs just after the weapon imbue appears).

local ADDON, NS = ...
local API = NS.API

local Snap = {}
NS.Snapshot = Snap

local STAT_NAMES   = { "str", "agi", "sta", "int", "spi" }
local SCHOOL_NAMES = { "phys", "holy", "fire", "nature", "frost", "shadow", "arcane" }
NS.SCHOOL_NAMES = SCHOOL_NAMES

-- combat rating ids we care about (constants exist on both clients, fallbacks are the retail values)
local RATINGS = {
	{ "hitMelee",  "CR_HIT_MELEE",  6 },
	{ "hitSpell",  "CR_HIT_SPELL",  8 },
	{ "critMelee", "CR_CRIT_MELEE", 9 },
	{ "critSpell", "CR_CRIT_SPELL", 11 },
	{ "hasteMelee", "CR_HASTE_MELEE", 18 },
	{ "hasteSpell", "CR_HASTE_SPELL", 20 },
	{ "expertise", "CR_EXPERTISE",  24 },
	{ "dodge",     "CR_DODGE",      3 },
	{ "parry",     "CR_PARRY",      4 },
	{ "defense",   "CR_DEFENSE_SKILL", 2 },
	{ "weaponSkill", "CR_WEAPON_SKILL", 1 },
}

local function num(v) return NS.SafeNumber(v) end
local function round(v, d)
	if type(v) ~= "number" then return nil end
	local m = 10 ^ (d or 2)
	return math.floor(v * m + 0.5) / m
end

-- talents: classic tab/index API, pcall'd; returns { api = "...", list = { "Tab/Name rank" } }
function Snap.Talents()
	local out = { api = "none" }
	if type(GetNumTalentTabs) == "function" and type(GetTalentInfo) == "function" then
		local okT, numTabs = pcall(GetNumTalentTabs)
		if okT and type(numTabs) == "number" and numTabs > 0 then
			out.api = "GetTalentInfo(tab,index)"
			out.list = {}
			out.points = {}
			for tab = 1, numTabs do
				local tabName = "tab" .. tab
				if type(GetTalentTabInfo) == "function" then
					local okTab, a, b = pcall(GetTalentTabInfo, tab)
					if okTab then
						if type(a) == "table" then tabName = NS.SafeString(a.name) or tabName
						elseif type(a) == "string" then tabName = a
						elseif type(b) == "string" then tabName = b end
					end
				end
				local okN, numTalents = pcall(GetNumTalents, tab)
				local spent = 0
				if okN and type(numTalents) == "number" then
					for i = 1, numTalents do
						local okI, name, _, tier, column, rank, maxRank = pcall(GetTalentInfo, tab, i)
						if okI and type(name) == "string" and type(rank) == "number" and rank > 0 then
							out.list[#out.list + 1] = string.format("%s/%s %d/%s", tabName, name, rank, tostring(maxRank or "?"))
							spent = spent + rank
						end
					end
				end
				out.points[tab] = spent
			end
			return out
		end
	end
	return out
end

local function equippedLinks()
	local eq = {}
	for slot = 1, 19 do
		local ok, link = pcall(GetInventoryItemLink, "player", slot)
		if ok and link and not NS.IsSecret(link) then eq[slot] = link end
	end
	return eq
end

local function buffNames()
	local names = {}
	API.ForEachPlayerBuff(function(name)
		names[#names + 1] = name
		if #names >= 40 then return true end
	end)
	return names
end

-- Build a snapshot table (does not store it)
function Snap.Build(reason)
	local s = { t = time(), reason = reason, lvl = num(UnitLevel("player")) }

	s.stats = {}
	for i = 1, 5 do
		local ok, base, eff, pos, neg = pcall(UnitStat, "player", i)
		if ok then s.stats[STAT_NAMES[i]] = { num(eff), num(base), num(pos), num(neg) } end
	end

	local okAP, base, pos, neg = pcall(UnitAttackPower, "player")
	if okAP and num(base) then
		s.ap = { (base or 0) + (pos or 0) + (neg or 0), num(base), num(pos), num(neg) }
	end

	local okC, crit = pcall(GetCritChance); if okC then s.crit = round(num(crit), 3) end
	local okD, dodge = pcall(GetDodgeChance); if okD then s.dodge = round(num(dodge), 3) end
	local okP, parry = pcall(GetParryChance); if okP then s.parry = round(num(parry), 3) end
	local okB, block = pcall(GetBlockChance); if okB then s.block = round(num(block), 3) end

	s.spellCrit, s.sp = {}, {}
	for i = 1, 7 do
		local okS, sc = pcall(GetSpellCritChance, i); if okS then s.spellCrit[SCHOOL_NAMES[i]] = round(num(sc), 3) end
		local okD2, sd = pcall(GetSpellBonusDamage, i); if okD2 then s.sp[SCHOOL_NAMES[i]] = num(sd) end
	end
	local okH, heal = pcall(GetSpellBonusHealing); if okH then s.heal = num(heal) end

	local okE, exp, expOff = pcall(GetExpertise); if okE then s.expertise = { num(exp), num(expOff) } end
	local okHM, hm = pcall(GetHitModifier); if okHM then s.hitMelee = num(hm) end
	local okSH, sh = pcall(GetSpellHitModifier); if okSH then s.hitSpell = num(sh) end

	s.ratings = {}
	if type(GetCombatRating) == "function" then
		for _, r in ipairs(RATINGS) do
			local id = _G[r[2]] or r[3]
			local okR, rating = pcall(GetCombatRating, id)
			local okBn, bonus = pcall(GetCombatRatingBonus, id)
			rating = okR and num(rating) or nil
			bonus = okBn and num(bonus) or nil
			if (rating and rating ~= 0) or (bonus and bonus ~= 0) then
				s.ratings[r[1]] = { rating, round(bonus, 3), id }
			end
		end
	end

	local okR, rbase, rcast = pcall(GetManaRegen)
	if okR then s.regen = { round(num(rbase), 3), round(num(rcast), 3) } end
	if type(GetPowerRegenForPowerType) == "function" then
		local okPR, a, b = pcall(GetPowerRegenForPowerType, 0)
		if okPR then s.regenPT = { round(num(a), 3), round(num(b), 3) } end
	end

	s.hp = num(UnitHealthMax("player"))
	s.mana = num(UnitPowerMax("player", 0))
	s.hpNow = num(UnitHealth("player"))
	s.manaNow = num(UnitPower("player", 0))

	local okA, abase, aeff, aarmor, apos, aneg = pcall(UnitArmor, "player")
	if okA then s.armor = { num(aeff), num(abase), num(apos), num(aneg) } end

	local okDm, dmin, dmax, omin, omax, dpos, dneg, dpct = pcall(UnitDamage, "player")
	if okDm then s.dmg = { round(num(dmin), 2), round(num(dmax), 2), round(num(omin), 2), round(num(omax), 2), num(dpos), num(dneg), round(num(dpct), 4) } end
	local okSp, mspeed, ospeed = pcall(UnitAttackSpeed, "player")
	if okSp then s.speed = { round(num(mspeed), 3), round(num(ospeed), 3) } end
	if type(UnitAttackBothHands) == "function" then
		local okW, mb, mm, ob, om = pcall(UnitAttackBothHands, "player")
		if okW then s.wskill = { num(mb), num(mm), num(ob), num(om) } end
	end
	if type(GetMeleeHaste) == "function" then
		local okMH, mh = pcall(GetMeleeHaste); if okMH then s.hasteMelee = round(num(mh), 3) end
	elseif type(GetHaste) == "function" then
		local okMH, mh = pcall(GetHaste); if okMH then s.haste = round(num(mh), 3) end
	end

	local okI, hasMH, mhExp, mhCharges, mhID, hasOH, ohExp, ohCharges, ohID = pcall(GetWeaponEnchantInfo)
	if okI then
		s.imbue = { mh = NS.SafeBool(hasMH) or false, mhID = num(mhID), mhExp = num(mhExp), mhCharges = num(mhCharges),
			oh = NS.SafeBool(hasOH) or false, ohID = num(ohID), ohExp = num(ohExp) }
	end
	s.mhTip = API.TooltipLinesForInventory(16)

	s.equip = equippedLinks()
	s.talents = Snap.Talents()
	s.buffs = buffNames()
	s.xp = { num(UnitXP("player")), num(UnitXPMax("player")) }
	local okZ, zone = pcall(GetZoneText); if okZ then s.zone = NS.SafeString(zone) end
	s.combat = NS.SafeBool(UnitAffectingCombat("player"))
	return s
end

local function stat(s, k) return s.stats[k] and s.stats[k][1] or "?" end

function Snap.Summary(s)
	local imbue = s.imbue and (s.imbue.mh and ("imbue " .. tostring(s.imbue.mhID)) or "no imbue") or "imbue ?"
	local exp = s.expertise and s.expertise[1] or 0
	local expRating = s.ratings and s.ratings.expertise and s.ratings.expertise[1] or 0
	return string.format("L%s %s | Str %s Agi %s Sta %s Int %s Spi %s | AP %s | crit %.2f%% | regen %s/%s | SP nat %s heal %s | exp %s (rating %s) | %s",
		tostring(s.lvl), tostring(s.reason), stat(s, "str"), stat(s, "agi"), stat(s, "sta"), stat(s, "int"), stat(s, "spi"),
		tostring(s.ap and s.ap[1] or "?"), tonumber(s.crit) or 0,
		tostring(s.regen and s.regen[1] or "?"), tostring(s.regen and s.regen[2] or "?"),
		tostring(s.sp and s.sp.nature or "?"), tostring(s.heal or "?"), tostring(exp), tostring(expRating), imbue)
end

function Snap.Take(reason, quiet)
	local s = Snap.Build(reason or "manual")
	local n = NS.PushSnapshot(s)
	if not quiet then NS.Printf("snapshot #%d: %s", n, Snap.Summary(s)) end
	return s
end

-------------------------------------------------------------------------------
-- Rockbiter / imbue watcher: sample AP + imbue state every second, record the AP
-- delta across the tick where the main-hand imbue appears, changes or drops.
-------------------------------------------------------------------------------
local prev = nil
local ROCKBITER_CAP = 60

local function miniState()
	local okI, hasMH, _, _, mhID, hasOH, _, _, ohID = pcall(GetWeaponEnchantInfo)
	if not okI then return nil end
	local okAP, base, pos, neg = pcall(UnitAttackPower, "player")
	local ap = (okAP and num(base)) and ((base or 0) + (pos or 0) + (neg or 0)) or nil
	local _, _, str = pcall(UnitStat, "player", 1)
	local _, _, int = pcall(UnitStat, "player", 4)
	local okDm, dmin, dmax = pcall(UnitDamage, "player")
	return {
		hasMH = NS.SafeBool(hasMH) or false, mhID = num(mhID) or 0,
		hasOH = NS.SafeBool(hasOH) or false, ohID = num(ohID) or 0,
		ap = ap, str = num(str), int = num(int), lvl = num(UnitLevel("player")),
		dmin = okDm and round(num(dmin), 1) or nil, dmax = okDm and round(num(dmax), 1) or nil,
		t = GetTime(),
	}
end

function Snap.ImbueTick()
	local cur = miniState()
	if not cur then return end
	if prev and (prev.hasMH ~= cur.hasMH or prev.mhID ~= cur.mhID or prev.hasOH ~= cur.hasOH or prev.ohID ~= cur.ohID) then
		local rec = {
			t = time(), lvl = cur.lvl,
			before = { ap = prev.ap, str = prev.str, int = prev.int, lvl = prev.lvl, mh = prev.hasMH, mhID = prev.mhID, oh = prev.hasOH, ohID = prev.ohID, dmin = prev.dmin, dmax = prev.dmax },
			after  = { ap = cur.ap,  str = cur.str,  int = cur.int,  lvl = cur.lvl,  mh = cur.hasMH,  mhID = cur.mhID,  oh = cur.hasOH,  ohID = cur.ohID,  dmin = cur.dmin,  dmax = cur.dmax },
			gap = round(cur.t - prev.t, 2),
		}
		if prev.ap and cur.ap then rec.delta = cur.ap - prev.ap end
		local okL, link = pcall(GetInventoryItemLink, "player", 16)
		if okL then rec.mhLink = NS.SafeString(link) end
		rec.mhTip = API.TooltipLinesForInventory(16)
		-- what the imbue spell says right now (Rockbiter tooltip carries the AP number on Forever)
		if NS.Spells and NS.Spells.ImbueReadings then rec.spells = NS.Spells.ImbueReadings() end
		local list = NS.char.rockbiter
		list[#list + 1] = rec
		while #list > ROCKBITER_CAP do table.remove(list, 1) end
		NS.Printf("imbue changed (mh %s id %s -> %s id %s): AP %s -> %s (delta %s), Str %s->%s, Int %s->%s, L%s",
			tostring(prev.hasMH), tostring(prev.mhID), tostring(cur.hasMH), tostring(cur.mhID),
			tostring(prev.ap), tostring(cur.ap), tostring(rec.delta), tostring(prev.str), tostring(cur.str),
			tostring(prev.int), tostring(cur.int), tostring(cur.lvl))
		Snap.Take("imbue")
	end
	prev = cur
end

NS.EveryTick("imbue", Snap.ImbueTick)

-------------------------------------------------------------------------------
-- Triggers
-------------------------------------------------------------------------------
local function afterEnterWorld(isLogin, isReload)
	C_Timer.After(3, function() NS.SafeCall("snapshot:login", Snap.Take, isReload and "reload" or "login") end)
end
local prevEnter = NS.OnEnterWorld
NS.OnEnterWorld = function(...) if prevEnter then prevEnter(...) end; afterEnterWorld(...) end

NS.On("PLAYER_LEVEL_UP", function(level)
	NS.Debounce("snap:levelup", 1.5, function() Snap.Take("levelup " .. tostring(level)) end)
end)

NS.On("PLAYER_EQUIPMENT_CHANGED", function(slot, hasItem)
	NS.Debounce("snap:equip", 1.5, function() Snap.Take("equip") end)
end)

NS.On("CHARACTER_POINTS_CHANGED", function()
	NS.Debounce("snap:talent", 2, function() Snap.Take("talent") end)
end)

local prevReset = NS.OnReset
NS.OnReset = function() if prevReset then prevReset() end; prev = nil end
