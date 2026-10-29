-- DoggsProbe / Regen.lua
-- Mana/health regen probe: a 1 s sampler out of combat. Every sample is tagged with a state
-- (idle / drink / food, plus "+fsr" when within 5 s of the last mana-costing cast) and
-- aggregated into buckets keyed "level|spirit|int|state". A capped raw sample list is kept too.
--
-- Rules that keep the buckets honest:
--   * a sample counts for mana only if mana was below max before AND after the second
--     (a full pool hides regen; a tick that fills the pool is truncated), and mana did not drop
--   * same for health
--   * samples are dropped while in combat, during the second after leaving combat,
--     and when the gap between samples is not roughly one second (loading screens, lag)

local ADDON, NS = ...
local API = NS.API

local Regen = {}
NS.Regen = Regen

local RAW_CAP = 2500
Regen.RAW_FIELDS = "t,dt,state,dMana,dHp,mana,manaMax,hp,hpMax,lvl,spi,int,manaValid,hpValid"

local last = nil
local lastInCombat = false
local lastManaCast = -100
local lastAnyCast = -100
local lastCastSpell = nil
local manaCostCache = {}

local function spellCostsMana(spellID)
	if not spellID then return false end
	local c = manaCostCache[spellID]
	if c == nil then
		local mana = API.SpellCost(spellID)
		c = (mana or 0) > 0
		manaCostCache[spellID] = c
	end
	return c
end

function Regen.OnCastSucceeded(unit, castGUID, spellID)
	if unit ~= "player" then return end
	local now = GetTime()
	lastAnyCast = now
	spellID = NS.SafeNumber(spellID)
	if spellCostsMana(spellID) then
		lastManaCast = now
		lastCastSpell = spellID
	end
end

local function db()
	local r = NS.char.regen
	r.buckets = r.buckets or {}
	r.raw = r.raw or {}
	r.rawFields = Regen.RAW_FIELDS
	r.samples = r.samples or 0
	r.dropped = r.dropped or 0
	return r
end

-- state string for this second
function Regen.State(now)
	local drink, food = false, false
	API.ForEachPlayerBuff(function(name)
		local n = string.lower(name)
		if n:find("drink", 1, true) or n:find("refreshment", 1, true) then drink = true end
		if n:find("food", 1, true) or n:find("well fed", 1, true) then food = true end
		return drink and food
	end)
	local s
	if drink and food then s = "drink+food" elseif drink then s = "drink" elseif food then s = "food" else s = "idle" end
	if now - lastManaCast < 5 then s = s .. "+fsr" end
	return s
end

function Regen.Tick()
	local now = GetTime()
	local mana = NS.SafeNumber(UnitPower("player", 0))
	local manaMax = NS.SafeNumber(UnitPowerMax("player", 0))
	local hp = NS.SafeNumber(UnitHealth("player"))
	local hpMax = NS.SafeNumber(UnitHealthMax("player"))
	local inCombat = NS.SafeBool(UnitAffectingCombat("player"))
	local dead = NS.SafeBool(UnitIsDeadOrGhost("player"))
	if not mana or not manaMax or not hp or not hpMax then return end

	local r = db()
	if last and not inCombat and not lastInCombat and not dead then
		local dt = now - last.t
		if dt > 0.5 and dt < 3 then
			local _, _, spi = pcall(UnitStat, "player", 5)
			local _, _, int = pcall(UnitStat, "player", 4)
			spi = NS.SafeNumber(spi) or 0
			int = NS.SafeNumber(int) or 0
			local lvl = NS.SafeNumber(UnitLevel("player")) or 0
			local state = Regen.State(now)
			local key = string.format("%d|%d|%d|%s", lvl, spi, int, state)
			local dMana = mana - last.mana
			local dHp = hp - last.hp
			local manaValid = (last.mana < manaMax) and (mana < manaMax) and (dMana >= 0)
			local hpValid = (last.hp < hpMax) and (hp < hpMax) and (dHp >= 0)
			local b = r.buckets[key]
			if not b then
				b = { lvl = lvl, spi = spi, int = int, state = state, n = 0, manaSec = 0, mana = 0, hpSec = 0, hp = 0, manaMax = manaMax, hpMax = hpMax }
				r.buckets[key] = b
			end
			b.n = b.n + 1
			b.manaMax = manaMax
			b.hpMax = hpMax
			if manaValid then
				b.manaSec = b.manaSec + dt
				b.mana = b.mana + dMana
			end
			if hpValid then
				b.hpSec = b.hpSec + dt
				b.hp = b.hp + dHp
			end
			r.samples = r.samples + 1
			if manaValid or hpValid then
				local raw = r.raw
				raw[#raw + 1] = { time(), math.floor(dt * 100 + 0.5) / 100, state, dMana, dHp, mana, manaMax, hp, hpMax, lvl, spi, int, manaValid and 1 or 0, hpValid and 1 or 0 }
				while #raw > RAW_CAP do table.remove(raw, 1) end
			end
		else
			r.dropped = r.dropped + 1
		end
	end
	last = { t = now, mana = mana, hp = hp }
	lastInCombat = inCombat and true or false
end

NS.EveryTick("regen", Regen.Tick)
NS.On("UNIT_SPELLCAST_SUCCEEDED", Regen.OnCastSucceeded, "player")

-- sorted bucket report lines
function Regen.Report()
	local r = db()
	local keys = {}
	for k in pairs(r.buckets) do keys[#keys + 1] = k end
	table.sort(keys)
	local lines = {}
	for _, k in ipairs(keys) do
		local b = r.buckets[k]
		local mps = b.manaSec > 0 and (b.mana / b.manaSec) or 0
		local hps = b.hpSec > 0 and (b.hp / b.hpSec) or 0
		local per5 = mps * 5
		lines[#lines + 1] = string.format("L%d spi %d int %d %-12s  mana: %5.0f s -> %6.0f mana = %6.2f/s (%5.1f per 5 s)   hp: %5.0f s = %5.2f/s   [%d samples]",
			b.lvl, b.spi, b.int, b.state, b.manaSec, b.mana, mps, per5, b.hpSec, hps, b.n)
	end
	return lines, r
end

function Regen.Status()
	local r = db()
	local n = 0
	for _ in pairs(r.buckets) do n = n + 1 end
	return string.format("regen: %d buckets, %d samples (%d raw kept, %d dropped), last mana cast %.0f s ago (spell %s)",
		n, r.samples or 0, #r.raw, r.dropped or 0, GetTime() - lastManaCast, tostring(lastCastSpell))
end

local prevReset = NS.OnReset
NS.OnReset = function() if prevReset then prevReset() end; last = nil end
