-- DoggsProbe / Combat.lua
-- Best-effort combat sampling from COMBAT_LOG_EVENT_UNFILTERED for the player's own swings and
-- spells, bucketed by (target level - player level). Forever inherited Midnight's addon
-- restrictions, so every read is pcall'd and checked with issecretvalue:
--   mode "full"   - amounts readable: damage sums, min/max, crit/glancing splits + miss counts
--   mode "counts" - amounts are secret: hit/crit/glance/miss counts only
--   blocked       - even the subevent/GUIDs are unreadable: unregistered, reason stored in the DB

local ADDON, NS = ...

local Combat = {}
NS.Combat = Combat

local frame = CreateFrame("Frame", "DoggsProbeCombatFrame")
local playerGUID
local registered = false

local function db()
	local c = NS.char.combat
	c.mode = c.mode or "full"
	c.swing = c.swing or {}
	c.spell = c.spell or {}
	c.events = c.events or 0
	c.errors = c.errors or 0
	return c
end

local function bucketFor(destGUID)
	if not destGUID or NS.IsSecret(destGUID) then return "?" end
	local u = NS.units[destGUID]
	local plvl = NS.SafeNumber(UnitLevel("player"))
	if u and u.level and u.level > 0 and plvl then
		return string.format("%+d", u.level - plvl)
	end
	return "?"
end

local function swingBucket(c, key)
	local b = c.swing[key]
	if not b then
		b = { swings = 0, hits = 0, crits = 0, glances = 0, miss = {}, dmg = 0, dmgN = 0, critDmg = 0, critN = 0, glanceDmg = 0, glanceN = 0, min = nil, max = nil }
		c.swing[key] = b
	end
	return b
end

local function spellBucket(c, name)
	local b = c.spell[name]
	if not b then
		b = { casts = 0, hits = 0, crits = 0, ticks = 0, miss = {}, dmg = 0, dmgN = 0, critDmg = 0, critN = 0, min = nil, max = nil }
		c.spell[name] = b
	end
	return b
end

local function addDamage(c, b, amount, critical, glancing)
	if c.mode ~= "full" then return end
	amount = NS.SafeNumber(amount)
	if not amount then
		-- amounts are secret on this client: fall back to counts for the rest of the session
		c.mode = "counts"
		c.modeReason = "damage amount unreadable (secret value)"
		NS.Print("combat log damage amounts are hidden on this client; keeping hit/miss counts only")
		return
	end
	b.dmg = b.dmg + amount
	b.dmgN = b.dmgN + 1
	if not b.min or amount < b.min then b.min = amount end
	if not b.max or amount > b.max then b.max = amount end
	if critical then b.critDmg = b.critDmg + amount; b.critN = b.critN + 1 end
	if glancing then b.glanceDmg = b.glanceDmg + amount; b.glanceN = b.glanceN + 1 end
end

local function process()
	local c = db()
	-- 11 fixed prefix values, then the subevent payload (a1..a10)
	local _, sub, _, srcGUID, _, _, _, dstGUID, _, _, _, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10 = CombatLogGetCurrentEventInfo()
	if NS.IsSecret(sub) or NS.IsSecret(srcGUID) then
		-- unreadable event: skip it; give up only if nothing readable ever arrives
		c.secret = (c.secret or 0) + 1
		if c.secret >= 100 and c.events == 0 then
			Combat.Disable("combat log subevent/source GUID are secret values (100 events, none readable)")
		end
		return
	end
	if srcGUID ~= playerGUID then return end
	c.events = c.events + 1

	if sub == "SWING_DAMAGE" then
		-- amount, overkill, school, resisted, blocked, absorbed, critical, glancing, crushing
		local b = swingBucket(c, bucketFor(dstGUID))
		local critical = NS.SafeBool(a7)
		local glancing = NS.SafeBool(a8)
		b.swings = b.swings + 1
		b.hits = b.hits + 1
		if critical then b.crits = b.crits + 1 end
		if glancing then b.glances = b.glances + 1 end
		addDamage(c, b, a1, critical, glancing)
	elseif sub == "SWING_MISSED" then
		-- missType, isOffHand, amountMissed
		local b = swingBucket(c, bucketFor(dstGUID))
		local missType = NS.SafeString(a1) or "?"
		b.swings = b.swings + 1
		b.miss[missType] = (b.miss[missType] or 0) + 1
	elseif sub == "SPELL_DAMAGE" or sub == "SPELL_PERIODIC_DAMAGE" then
		-- spellId, spellName, spellSchool, amount, overkill, school, resisted, blocked, absorbed, critical
		local name = NS.SafeString(a2) or ("spell" .. tostring(NS.SafeNumber(a1) or "?"))
		local b = spellBucket(c, name)
		local critical = NS.SafeBool(a10)
		if sub == "SPELL_PERIODIC_DAMAGE" then b.ticks = b.ticks + 1 else b.hits = b.hits + 1 end
		if critical then b.crits = b.crits + 1 end
		b.id = b.id or NS.SafeNumber(a1)
		addDamage(c, b, a4, critical, false)
	elseif sub == "SPELL_MISSED" then
		-- spellId, spellName, spellSchool, missType
		local name = NS.SafeString(a2) or ("spell" .. tostring(NS.SafeNumber(a1) or "?"))
		local b = spellBucket(c, name)
		local missType = NS.SafeString(a4) or "?"
		b.miss[missType] = (b.miss[missType] or 0) + 1
	elseif sub == "SPELL_CAST_SUCCESS" then
		local name = NS.SafeString(a2)
		if name then
			local b = spellBucket(c, name)
			b.casts = b.casts + 1
			b.id = b.id or NS.SafeNumber(a1)
		end
	end
end

local function onEvent()
	local ok, err = pcall(process)
	if not ok then
		local c = db()
		c.errors = c.errors + 1
		c.lastError = tostring(err)
		if c.errors == 1 then NS.LogError("combat", err) end
		if c.errors >= 5 then
			Combat.Disable("too many errors reading the combat log: " .. tostring(err))
		end
	end
end

function Combat.Enable()
	if registered then return end
	if type(CombatLogGetCurrentEventInfo) ~= "function" then
		Combat.Disable("CombatLogGetCurrentEventInfo missing")
		return
	end
	local c = db()
	if c.blocked then
		NS.Print("combat sampling stays off (blocked earlier: " .. tostring(c.blocked) .. "); /probe combat on to retry")
		return
	end
	local ok, g = pcall(UnitGUID, "player")
	playerGUID = ok and g or nil
	if not playerGUID or NS.IsSecret(playerGUID) then
		Combat.Disable("player GUID unreadable")
		return
	end
	frame:SetScript("OnEvent", onEvent)
	frame:RegisterEvent("COMBAT_LOG_EVENT_UNFILTERED")
	registered = true
	c.enabled = true
end

function Combat.Disable(reason)
	local c = db()
	if registered then
		frame:UnregisterEvent("COMBAT_LOG_EVENT_UNFILTERED")
		registered = false
	end
	c.enabled = false
	if reason then
		c.blocked = reason
		c.blockedAt = time()
		NS.Print("combat sampling disabled: " .. tostring(reason))
	end
end

function Combat.Retry()
	local c = db()
	c.blocked = nil
	c.errors = 0
	c.mode = "full"
	c.modeReason = nil
	Combat.Enable()
end

function Combat.Report()
	local c = db()
	local lines = {}
	lines[#lines + 1] = string.format("mode %s%s, %d player events, %d unreadable, %d errors%s", c.mode, c.enabled and "" or " (OFF)", c.events,
		c.secret or 0, c.errors, c.blocked and (", blocked: " .. c.blocked) or "")
	local keys = {}
	for k in pairs(c.swing) do keys[#keys + 1] = k end
	table.sort(keys)
	for _, k in ipairs(keys) do
		local b = c.swing[k]
		local misses = {}
		for mt, n in pairs(b.miss) do misses[#misses + 1] = mt .. " " .. n end
		table.sort(misses)
		local avg = b.dmgN > 0 and (b.dmg / b.dmgN) or 0
		local cavg = b.critN > 0 and (b.critDmg / b.critN) or 0
		local gavg = b.glanceN > 0 and (b.glanceDmg / b.glanceN) or 0
		lines[#lines + 1] = string.format("swings vs level %s: %d swings, %d hit (%d crit, %d glance), miss: %s | avg %.1f (crit %.1f, glance %.1f) min %s max %s",
			k, b.swings, b.hits, b.crits, b.glances, #misses > 0 and table.concat(misses, ", ") or "none", avg, cavg, gavg, tostring(b.min), tostring(b.max))
	end
	local names = {}
	for k in pairs(c.spell) do names[#names + 1] = k end
	table.sort(names)
	for _, name in ipairs(names) do
		local b = c.spell[name]
		local misses = {}
		for mt, n in pairs(b.miss) do misses[#misses + 1] = mt .. " " .. n end
		table.sort(misses)
		local avg = b.dmgN > 0 and (b.dmg / b.dmgN) or 0
		lines[#lines + 1] = string.format("%s: %d casts, %d hits, %d ticks, %d crits, miss: %s | avg %.1f min %s max %s",
			name, b.casts, b.hits, b.ticks, b.crits, #misses > 0 and table.concat(misses, ", ") or "none", avg, tostring(b.min), tostring(b.max))
	end
	return lines
end

local prevEnter = NS.OnEnterWorld
NS.OnEnterWorld = function(...)
	if prevEnter then prevEnter(...) end
	Combat.Enable()
end

local prevReset = NS.OnReset
NS.OnReset = function() if prevReset then prevReset() end; Combat.Disable(); Combat.Retry() end
