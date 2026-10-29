-- Minimal WoW API stub for exercising DoggsProbe offline under Lua 5.1.
-- Profiles: "era" (old globals, no C_TooltipInfo), "forever" (C_ namespaces, table returns,
-- issecretvalue, secret combat-log amounts), "blocked" (forever + secret subevents).
local STUB = {}
local profile = arg and arg[1] or "era"
STUB.profile = profile
local FOREVER = (profile ~= "era")
local BLOCKED = (profile == "blocked")

-------------------------------------------------------------------------------
-- clock
-------------------------------------------------------------------------------
local clock = 1000.0
local EPOCH = 1790300000
function GetTime() return clock end
function time() return EPOCH + math.floor(clock) end
function date(fmt, t) return os.date(fmt, t or time()) end
function GetServerTime() return time() end

local timers = {}
C_Timer = {}
function C_Timer.After(delay, fn) timers[#timers + 1] = { at = clock + delay, fn = fn } end
function C_Timer.NewTicker(period, fn)
	local t = { at = clock + period, fn = fn, period = period }
	timers[#timers + 1] = t
	return { Cancel = function() t.cancelled = true end }
end
function STUB.advance(seconds, step)
	step = step or 0.5
	local target = clock + seconds
	while clock < target - 1e-9 do
		clock = math.min(target, clock + step)
		table.sort(timers, function(a, b) return a.at < b.at end)
		local i = 1
		while i <= #timers do
			local t = timers[i]
			if t.cancelled then table.remove(timers, i)
			elseif t.at <= clock + 1e-9 then
				if t.period then
					t.at = t.at + t.period
					t.fn()
					i = i + 1
				else
					table.remove(timers, i)
					t.fn()
				end
			else
				i = i + 1
			end
		end
		STUB.world.tick(step)
	end
end

-------------------------------------------------------------------------------
-- secret values
-------------------------------------------------------------------------------
local SECRET = {}
SECRET.__index = SECRET
local function boom() error("attempt to use a secret value") end
SECRET.__lt, SECRET.__le, SECRET.__add, SECRET.__sub, SECRET.__mul, SECRET.__concat = boom, boom, boom, boom, boom, boom
SECRET.__tostring = function() return "<SECRET>" end
function STUB.secret(v) return setmetatable({ v = v }, SECRET) end
if FOREVER then
	function issecretvalue(v) return type(v) == "table" and getmetatable(v) == SECRET end
end

-------------------------------------------------------------------------------
-- output capture
-------------------------------------------------------------------------------
STUB.output = {}
local rawprint = print
function print(...)
	local parts = {}
	for i = 1, select("#", ...) do parts[i] = tostring((select(i, ...))) end
	local line = table.concat(parts, " ")
	STUB.output[#STUB.output + 1] = line
	if STUB.echo then rawprint(line) end
end

-------------------------------------------------------------------------------
-- world state
-------------------------------------------------------------------------------
local W = {
	level = 10, str = 30, agi = 20, sta = 28, int = 27, spi = 29,
	apBase = 60, apPos = 0, apNeg = 0,
	mana = 300, manaMax = 500, hp = 400, hpMax = 500, combat = false, dead = false,
	buffs = {}, imbueMH = false, imbueID = 0, imbueOH = false,
	spNature = 0, spFire = 0, spFrost = 0, heal = 0,
	regenBase = 8.0, regenCast = 2.0, xp = 1200, xpMax = 5000, zone = "Dun Morogh",
	targetGUID = nil, target = nil, equip = {}, bags = { [0] = {}, {}, {}, {}, {} },
	questID = 0, questTitle = nil, questChoices = {}, questRewards = {}, merchant = {}, loot = {},
}
STUB.world = W
function W.tick(dt)
	if not W.combat and not W.dead then
		-- 2-second regen ticks like the real client
		W.acc = (W.acc or 0) + dt
		if W.acc >= 2 then
			W.acc = W.acc - 2
			local drinking = false
			for _, b in ipairs(W.buffs) do if b.name == "Drink" then drinking = true end end
			local perTick = 15 + W.spi / 5
			if drinking then perTick = perTick + 20 * 2 end
			if W.lastManaCast and clock - W.lastManaCast < 5 then perTick = 0 + (drinking and 40 or 0) end
			W.mana = math.min(W.manaMax, W.mana + perTick)
			W.hp = math.min(W.hpMax, W.hp + 5)
		end
	end
end

-------------------------------------------------------------------------------
-- frames / events
-------------------------------------------------------------------------------
local frames = {}
local Frame = {}
Frame.__index = Frame
function Frame:RegisterEvent(e) self.events[e] = true end
function Frame:RegisterUnitEvent(e, u) self.events[e] = u or true end
function Frame:UnregisterEvent(e) self.events[e] = nil end
function Frame:SetScript(k, fn) self.scripts[k] = fn end
function Frame:HookScript(k, fn) self.hooks[k] = self.hooks[k] or {}; table.insert(self.hooks[k], fn) end
function Frame:GetName() return self.name end
function Frame:IsForbidden() return false end
function Frame:SetOwner() end
function Frame:ClearLines() self.lines = {} end
function Frame:NumLines() return #(self.lines or {}) end
function Frame:GetItem() return self.itemName, self.itemLink end
local function setTipLines(self, lines, name, link)
	self.lines = lines or {}
	self.itemName, self.itemLink = name, link
	for i, l in ipairs(self.lines) do
		_G[self.name .. "TextLeft" .. i] = { GetText = function() return l[1] end, IsShown = function() return true end }
		_G[self.name .. "TextRight" .. i] = { GetText = function() return l[2] end, IsShown = function() return l[2] ~= nil end }
	end
end
STUB.setTipLines = setTipLines
function Frame:SetHyperlink(link) local it = STUB.itemByLink(link); if it then setTipLines(self, it.lines, it.name, it.link) end end
function Frame:SetInventoryItem(unit, slot) local link = W.equip[slot]; if link then self:SetHyperlink(link) end end
function Frame:SetBagItem(bag, slot) local link = W.bags[bag][slot]; if link then self:SetHyperlink(link) end end
function Frame:SetQuestItem(kind, i) local link = (kind == "choice" and W.questChoices or W.questRewards)[i]; if link then self:SetHyperlink(link) end end
function Frame:SetMerchantItem(i) local m = W.merchant[i]; if m then self:SetHyperlink(m.link) end end
function Frame:SetLootItem(i) local l = W.loot[i]; if l then self:SetHyperlink(l.link) end end

function CreateFrame(kind, name, parent, template)
	local f = setmetatable({ kind = kind, name = name, events = {}, scripts = {}, hooks = {} }, Frame)
	frames[#frames + 1] = f
	if name then _G[name] = f end
	return f
end
UIParent = CreateFrame("Frame", "UIParent")
GameTooltip = CreateFrame("GameTooltip", "GameTooltip")
ItemRefTooltip = CreateFrame("GameTooltip", "ItemRefTooltip")
ShoppingTooltip1 = CreateFrame("GameTooltip", "ShoppingTooltip1")
ShoppingTooltip2 = CreateFrame("GameTooltip", "ShoppingTooltip2")

function STUB.fire(event, ...)
	for _, f in ipairs(frames) do
		if f.events[event] and f.scripts.OnEvent then f.scripts.OnEvent(f, event, ...) end
	end
end

-------------------------------------------------------------------------------
-- build / unit info
-------------------------------------------------------------------------------
function GetBuildInfo()
	if FOREVER then return "1.60.1", "69977", "Sep 22 2026", 16001 end
	return "1.15.9", "69547", "Jul 15 2026", 11509
end
WOW_PROJECT_ID = FOREVER and 99 or 2
function UnitName(unit)
	if unit == "player" then return "Doggs" end
	if unit == "target" or unit == "mouseover" then return W.target and W.target.name end
	if unit == "npc" or unit == "questnpc" then return W.npcName end
	return nil
end
function GetRealmName() return FOREVER and "Forever" or "Mankrik" end
function UnitClass() return "Shaman", "SHAMAN" end
function UnitRace() return "Dwarf", "Dwarf" end
function UnitFactionGroup() return "Alliance", "Alliance" end
function UnitLevel(unit)
	if unit == "player" then return W.level end
	if (unit == "target" or unit == "mouseover") and W.target then return W.target.level end
	return 0
end
function UnitGUID(unit)
	if unit == "player" then return "Player-1-000000AA" end
	if (unit == "target" or unit == "mouseover") and W.target then return W.target.guid end
	if unit == "npc" then return W.npcGUID end
	return nil
end
function UnitClassification(unit) return W.target and W.target.class or "normal" end
function UnitCreatureType(unit) return "Beast" end
function UnitStat(unit, i)
	local v = ({ W.str, W.agi, W.sta, W.int, W.spi })[i]
	return v - 2, v, 2, 0
end
function UnitAttackPower() return W.apBase, W.apPos, W.apNeg end
function UnitPower(unit, t) return W.mana end
function UnitPowerMax(unit, t) return W.manaMax end
function UnitHealth() return W.hp end
function UnitHealthMax() return W.hpMax end
function UnitAffectingCombat() return W.combat end
function UnitIsDeadOrGhost() return W.dead end
function UnitArmor() return 100, 120, 100, 20, 0 end
function UnitDamage() return 20.5, 31.5, 0, 0, 0, 0, 1 end
function UnitAttackSpeed() return 2.6, nil end
if not FOREVER then function UnitAttackBothHands() return 50, 0, 50, 0 end end
function UnitXP() return W.xp end
function UnitXPMax() return W.xpMax end
function GetZoneText() return W.zone end
function GetSubZoneText() return "Kharanos" end
function GetCritChance() return 5.9 + (W.level - 10) * 0.2 end
function GetSpellCritChance(school) return 2.2 end
function GetDodgeChance() return 4.1 end
function GetParryChance() return 0 end
function GetBlockChance() return 0 end
function GetSpellBonusDamage(school) return ({ 0, 0, W.spFire, W.spNature, W.spFrost, 0, 0 })[school] end
function GetSpellBonusHealing() return W.heal end
function GetExpertise() return FOREVER and 2 or 0, 0 end
function GetHitModifier() return 0 end
function GetSpellHitModifier() return 0 end
CR_HIT_MELEE, CR_HIT_SPELL, CR_CRIT_MELEE, CR_CRIT_SPELL, CR_EXPERTISE, CR_DODGE, CR_PARRY = 6, 8, 9, 11, 24, 3, 4
function GetCombatRating(id) if id == 24 and FOREVER then return 6 end return 0 end
function GetCombatRatingBonus(id) if id == 24 and FOREVER then return 2.6 end return 0 end
function GetManaRegen() return W.regenBase, W.regenCast end
if FOREVER then function GetPowerRegenForPowerType(t) return W.regenBase, W.regenCast end end
function GetWeaponEnchantInfo() return W.imbueMH, W.imbueMH and 1800000 or nil, nil, W.imbueMH and W.imbueID or nil, W.imbueOH, nil, nil, nil end
function GetInventoryItemLink(unit, slot) return W.equip[slot] end
if FOREVER then function GetMeleeHaste() return 0 end else function GetHaste() return 0 end end
function UnitAura(unit, i, filter)
	if FOREVER then error("UnitAura was removed") end
	local b = W.buffs[i]
	if not b then return nil end
	return b.name, 136000, 0, nil, 0, 0, "player", false, false, b.id
end
if FOREVER then
	C_UnitAuras = { GetAuraDataByIndex = function(unit, i, filter)
		local b = W.buffs[i]
		if not b then return nil end
		return { name = b.name, spellId = b.id, icon = 136000 }
	end }
end

-- talents: classic API on era, nothing on forever
if not FOREVER then
	function GetNumTalentTabs() return 3 end
	function GetTalentTabInfo(tab) return ({ "Elemental", "Enhancement", "Restoration" })[tab], "tex", 0, "file" end
	function GetNumTalents(tab) return 2 end
	function GetTalentInfo(tab, i)
		if tab == 2 and i == 1 then return "Ancestral Knowledge", "tex", 1, 1, 3, 5, false, true end
		if tab == 2 and i == 2 then return "Thundering Strikes", "tex", 1, 2, 1, 5, false, true end
		return "Unused", "tex", 1, 3, 0, 5, false, true
	end
end

-------------------------------------------------------------------------------
-- spells
-------------------------------------------------------------------------------
local SPELLS = {
	{ id = 8042, name = "Earth Shock", rank = "Rank 1", cost = 30, desc = "Instantly shocks the target with concussive force, causing %d to %d Nature damage." },
	{ id = 8044, name = "Earth Shock", rank = "Rank 2", cost = 50, desc = "Instantly shocks the target with concussive force, causing %d to %d Nature damage." },
	{ id = 8050, name = "Flame Shock", rank = "Rank 1", cost = 55, desc = "Instantly sears the target with fire, causing %d Fire damage immediately and %d Fire damage over 12 sec." },
	{ id = 324, name = "Lightning Shield", rank = "Rank 1", cost = 45, desc = "The caster is surrounded by 3 balls of lightning. When a spell, melee or ranged attack hits the caster, the attacker will be struck for %d Nature damage." },
	{ id = 403, name = "Lightning Bolt", rank = "Rank 1", cost = 15, desc = "Casts a bolt of lightning at the target for %d to %d Nature damage." },
	{ id = 331, name = "Healing Wave", rank = "Rank 1", cost = 25, desc = "Heals a friendly target for %d to %d." },
	{ id = 8017, name = "Rockbiter Weapon", rank = "Rank 1", cost = 5, desc = "Imbue the Shaman's weapon with the fury of the earth, increasing attack power by %d. Lasts 30 minutes." },
	{ id = 8018, name = "Rockbiter Weapon", rank = "Rank 2", cost = 10, desc = "Imbue the Shaman's weapon with the fury of the earth, increasing attack power by %d. Lasts 30 minutes." },
	{ id = 2484, name = "Earthbind Totem", rank = "", cost = 10, desc = "Summons an Earthbind Totem." },
	{ id = 6603, name = "Attack", rank = "", cost = 0, desc = "Auto attack." },
}
local function spellById(id) for _, s in ipairs(SPELLS) do if s.id == id then return s end end end
local function spellDesc(s)
	if s.name == "Earth Shock" then
		local base = s.id == 8044 and 33 or 19
		local c = math.floor(W.spNature * 0.21 + 0.5)
		return string.format(s.desc, base + c, base + 3 + c)
	elseif s.name == "Rockbiter Weapon" then
		return string.format(s.desc, s.id == 8018 and 63 or 24)
	elseif s.name == "Lightning Shield" then
		return string.format(s.desc, 13 + math.floor(W.spNature * 0.1))
	elseif s.name == "Healing Wave" then
		return string.format(s.desc, 36 + math.floor(W.heal * 0.3), 47 + math.floor(W.heal * 0.3))
	elseif s.name == "Flame Shock" then
		return string.format(s.desc, 25, 28)
	elseif s.name == "Lightning Bolt" then
		return string.format(s.desc, 15, 17)
	end
	return s.desc
end

C_Spell = C_Spell or {}
function C_Spell.RequestLoadSpellData(id) end
if FOREVER then
	function C_Spell.GetSpellInfo(id) local s = spellById(id); if s then return { name = s.name, iconID = 1, castTime = 0, minRange = 0, maxRange = 20, spellID = id } end end
	function C_Spell.GetSpellDescription(id) local s = spellById(id); return s and spellDesc(s) or "" end
	function C_Spell.GetSpellSubtext(id) local s = spellById(id); return s and s.rank or nil end
	function C_Spell.GetSpellPowerCost(id) local s = spellById(id); if s and s.cost > 0 then return { { name = "MANA", type = 0, cost = s.cost, minCost = s.cost } } end return {} end
	Enum = Enum or {}
	Enum.PowerType = { Mana = 0 }
	Enum.SpellBookSpellBank = { Player = 0, Pet = 1 }
	Enum.SpellBookItemType = { None = 0, Spell = 1, FutureSpell = 2, PetAction = 3, Flyout = 4 }
	Enum.TooltipDataType = { Item = 0, Spell = 1 }
	C_SpellBook = {
		GetNumSpellBookSkillLines = function() return 2 end,
		GetSpellBookSkillLineInfo = function(i)
			if i == 1 then return { name = "General", itemIndexOffset = 0, numSpellBookItems = 1 } end
			return { name = "Shaman", itemIndexOffset = 1, numSpellBookItems = #SPELLS - 1 }
		end,
		GetSpellBookItemInfo = function(index, bank)
			local s = SPELLS[index == 1 and #SPELLS or index - 1]
			if not s then return nil end
			return { spellID = s.id, name = s.name, subName = s.rank, itemType = 1, isPassive = false, isOffSpec = false }
		end,
		GetSpellBookItemName = function(index, bank) local s = SPELLS[index == 1 and #SPELLS or index - 1]; return s and s.name, s and s.rank end,
	}
else
	function GetSpellInfo(id) local s = spellById(id); if s then return s.name, s.rank, 1, 0, 0, 20, id end end
	function GetSpellDescription(id) local s = spellById(id); return s and spellDesc(s) or "" end
	function GetSpellSubtext(id) local s = spellById(id); return s and s.rank or nil end
	function GetSpellPowerCost(id) local s = spellById(id); if s and s.cost > 0 then return { { name = "MANA", type = 0, cost = s.cost, minCost = s.cost } } end return {} end
	BOOKTYPE_SPELL = "spell"
	function GetNumSpellTabs() return 2 end
	function GetSpellTabInfo(i) if i == 1 then return "General", "tex", 0, 1 end return "Shaman", "tex", 1, #SPELLS - 1 end
	function GetSpellBookItemInfo(index, book) local s = SPELLS[index == 1 and #SPELLS or index - 1]; if s then return "SPELL", s.id end end
	function GetSpellBookItemName(index, book) local s = SPELLS[index == 1 and #SPELLS or index - 1]; if s then return s.name, s.rank end end
end

-------------------------------------------------------------------------------
-- items
-------------------------------------------------------------------------------
local ITEMS = {}
local function addItem(id, name, quality, ilvl, req, itype, sub, loc, stats, lines)
	local link = string.format("|cff1eff00|Hitem:%d::::::::10:::::::|h[%s]|h|r", id, name)
	ITEMS[id] = { id = id, name = name, link = link, quality = quality, ilvl = ilvl, req = req, type = itype, sub = sub, loc = loc, stats = stats, lines = lines }
	return link
end
addItem(2907, "Dwarven Tree Chopper", 2, 20, 15, "Weapon", "Two-Handed Axes", "INVTYPE_2HWEAPON",
	{ ITEM_MOD_STRENGTH_SHORT = 4, ITEM_MOD_EXPERTISE_RATING_SHORT = 6 },
	{ { "Dwarven Tree Chopper" }, { "Binds when picked up" }, { "Two-Hand", "Axe" }, { "25 - 39 Damage", "Speed 2.90" }, { "(11.0 damage per second)" }, { "+4 Strength" }, { "Equip: Increases your expertise by 6." }, { "Requires Level 15" } })
addItem(2205, "Duskbringer", 2, 20, 15, "Weapon", "Two-Handed Maces", "INVTYPE_2HWEAPON",
	{ ITEM_MOD_STAMINA_SHORT = 7, ITEM_MOD_STRENGTH_SHORT = 4 },
	{ { "Ironforge Greathammer" }, { "Binds when picked up" }, { "Two-Hand", "Mace" }, { "30 - 46 Damage", "Speed 2.70" }, { "(14.1 damage per second)" }, { "+4 Strength" }, { "+7 Stamina" }, { "Requires Level 16" } })
addItem(1200, "Minor Channeling Ring", 2, 22, 17, "Armor", "Miscellaneous", "INVTYPE_FINGER",
	{ ITEM_MOD_SPELL_POWER_SHORT = 5 },
	{ { "Minor Channeling Ring" }, { "Binds when picked up" }, { "Finger" }, { "Equip: Increases damage and healing done by magical spells and effects by up to 5." }, { "Requires Level 17" } })
addItem(159, "Refreshing Spring Water", 1, 5, 1, "Consumable", "Food & Drink", "",
	{},
	{ { "Refreshing Spring Water" }, { "Use: Restores 151.2 mana over 18 sec. Must remain seated while drinking." }, { "Requires Level 1" } })
addItem(2589, "Linen Cloth", 1, 5, 1, "Trade Goods", "Trade Goods", "", {}, { { "Linen Cloth" }, { "Max Stack: 20" } })
addItem(4540, "Tough Hunk of Bread", 1, 5, 1, "Consumable", "Food & Drink", "", {}, { { "Tough Hunk of Bread" }, { "Use: Restores 61 health over 18 sec." } })
addItem(5411, "Spiritwraith Drape", 2, 25, 20, "Armor", "Cloth", "INVTYPE_CLOAK",
	{ ITEM_MOD_SPIRIT_SHORT = 3, ITEM_MOD_STAMINA_SHORT = 3 },
	{ { "Spiritwraith Drape" }, { "Back" }, { "16 Armor" }, { "+3 Stamina" }, { "+3 Spirit" }, { "Requires Level 20" } })

function STUB.itemByLink(link)
	local id = link and tonumber(link:match("item:(%d+)"))
	return id and ITEMS[id]
end
function STUB.link(id) return ITEMS[id].link end
local function itemInfo(idOrLink)
	local it = type(idOrLink) == "number" and ITEMS[idOrLink] or STUB.itemByLink(idOrLink)
	if not it then return nil end
	return it.name, it.link, it.quality, it.ilvl, it.req, it.type, it.sub, 1, it.loc, 135000, 100, 2, 1, 1
end
local function itemStats(link) local it = STUB.itemByLink(link); if not it then return nil end local t = {}; for k, v in pairs(it.stats) do t[k] = v end return t end
if FOREVER then
	C_Item = { GetItemInfo = itemInfo, GetItemStats = itemStats, RequestLoadItemDataByID = function() end }
else
	GetItemInfo = itemInfo
	GetItemStats = itemStats
	C_Item = { RequestLoadItemDataByID = function() end }
end
NUM_BAG_SLOTS = 4
C_Container = {
	GetContainerNumSlots = function(bag) return bag == 0 and 16 or 6 end,
	GetContainerItemLink = function(bag, slot) return W.bags[bag][slot] end,
}

-- tooltip data (forever)
local function tooltipData(it)
	local lines = {}
	for i, l in ipairs(it.lines) do lines[i] = { type = 0, leftText = l[1], rightText = l[2] } end
	if BLOCKED and it.id == 5411 then lines[2].leftText = STUB.secret("x") end
	return { type = 0, id = it.id, hyperlink = it.link, lines = lines }
end
if FOREVER then
	C_TooltipInfo = {
		GetHyperlink = function(link) local it = STUB.itemByLink(link); return it and tooltipData(it) end,
		GetInventoryItem = function(unit, slot) local it = STUB.itemByLink(W.equip[slot]); return it and tooltipData(it) end,
		GetBagItem = function(bag, slot) local it = STUB.itemByLink(W.bags[bag][slot]); return it and tooltipData(it) end,
		GetQuestItem = function(kind, i) local it = STUB.itemByLink((kind == "choice" and W.questChoices or W.questRewards)[i]); return it and tooltipData(it) end,
		GetMerchantItem = function(i) local m = W.merchant[i]; local it = m and STUB.itemByLink(m.link); return it and tooltipData(it) end,
		GetLootItem = function(i) local l = W.loot[i]; local it = l and STUB.itemByLink(l.link); return it and tooltipData(it) end,
	}
	local postCalls = {}
	TooltipDataProcessor = { AddTooltipPostCall = function(t, fn) postCalls[#postCalls + 1] = { t = t, fn = fn } end }
	TooltipUtil = { GetDisplayedItem = function(tip) return tip.itemName, tip.itemLink end }
	function STUB.hover(link)
		local it = STUB.itemByLink(link)
		setTipLines(GameTooltip, it.lines, it.name, it.link)
		for _, p in ipairs(postCalls) do if p.t == 0 then p.fn(GameTooltip, tooltipData(it)) end end
	end
else
	function STUB.hover(link)
		local it = STUB.itemByLink(link)
		setTipLines(GameTooltip, it.lines, it.name, it.link)
		for _, fn in ipairs(GameTooltip.hooks.OnTooltipSetItem or {}) do fn(GameTooltip) end
	end
end

-------------------------------------------------------------------------------
-- quests / merchant / loot
-------------------------------------------------------------------------------
function GetQuestID() return W.questID end
function GetTitleText() return W.questTitle end
function GetObjectiveText() return "Bring 8 Boar Ribs to Grelin Whitebeard." end
function GetQuestText() return "The boars have been a menace..." end
function GetRewardXP() return 450 end
function GetRewardMoney() return 250 end
function GetNumQuestChoices() return #W.questChoices end
function GetNumQuestRewards() return #W.questRewards end
function GetQuestItemLink(kind, i) return (kind == "choice" and W.questChoices or W.questRewards)[i] end
C_QuestLog = {
	GetQuestObjectives = function(qid) return { { text = "Boar Rib: 0/8", type = "item", finished = false, numFulfilled = 0, numRequired = 8 } } end,
	GetTitleForQuestID = function(qid) return "A Refugee's Quandary" end,
}
function GetMerchantNumItems() return #W.merchant end
function GetMerchantItemLink(i) return W.merchant[i] and W.merchant[i].link end
if FOREVER then
	C_MerchantFrame = { GetItemInfo = function(i) local m = W.merchant[i]; return { name = m.name, price = m.price, stackCount = 1, numAvailable = -1, hasExtendedCost = false } end }
else
	function GetMerchantItemInfo(i) local m = W.merchant[i]; return m.name, 135000, m.price, 1, -1, true, true, false end
end
function GetNumLootItems() return #W.loot end
function GetLootSlotLink(i) return W.loot[i] and W.loot[i].link end
function GetLootSourceInfo(i) return W.lootGUID, 1 end

-------------------------------------------------------------------------------
-- combat log
-------------------------------------------------------------------------------
local cleu = {}
function CombatLogGetCurrentEventInfo() return unpack(cleu, 1, cleu.n) end
function STUB.cleu(sub, dstGUID, dstName, ...)
	local n = select("#", ...)
	cleu = { clock, sub, false, "Player-1-000000AA", "Doggs", 0x511, 0, dstGUID, dstName, 0x10a48, 0, ... }
	cleu.n = 11 + n
	if BLOCKED then cleu[2] = STUB.secret(sub) end
	STUB.fire("COMBAT_LOG_EVENT_UNFILTERED")
end

SlashCmdList = {}
function STUB.slash(msg) SlashCmdList["DOGGSPROBE"](msg) end

-------------------------------------------------------------------------------
-- SavedVariables writer in Blizzard's format
-------------------------------------------------------------------------------
local function q(s) return '"' .. s:gsub("\\", "\\\\"):gsub('"', '\\"'):gsub("\n", "\\n"):gsub("\r", "\\r") .. '"' end
local function ser(v, indent, out, path)
	local t = type(v)
	if t == "number" then
		if v ~= v or v == math.huge or v == -math.huge then error("bad number at " .. path) end
		if math.floor(v) == v and math.abs(v) < 2^52 then out[#out + 1] = string.format("%d", v) else out[#out + 1] = string.format("%.14g", v) end
	elseif t == "string" then out[#out + 1] = q(v)
	elseif t == "boolean" then out[#out + 1] = tostring(v)
	elseif t == "table" then
		if getmetatable(v) == SECRET then error("secret value stored at " .. path) end
		out[#out + 1] = "{\n"
		for k, val in pairs(v) do
			local kt = type(k)
			if kt ~= "number" and kt ~= "string" then error("bad key type " .. kt .. " at " .. path) end
			out[#out + 1] = indent .. "\t[" .. (kt == "number" and string.format("%d", k) or q(k)) .. "] = "
			ser(val, indent .. "\t", out, path .. "." .. tostring(k))
			out[#out + 1] = ",\n"
		end
		out[#out + 1] = indent .. "}"
	else
		error("unserialisable " .. t .. " at " .. path)
	end
end
function STUB.writeSavedVariables(path)
	local out = { "\nDoggsProbeDB = " }
	ser(DoggsProbeDB, "", out, "DoggsProbeDB")
	out[#out + 1] = "\n"
	local f = assert(io.open(path, "w"))
	f:write(table.concat(out))
	f:close()
end

-------------------------------------------------------------------------------
-- addon loader
-------------------------------------------------------------------------------
function STUB.loadAddon(dir, toc)
	local NS = {}
	local f = assert(io.open(dir .. "/" .. toc))
	for line in f:lines() do
		line = line:gsub("\r", "")
		if line ~= "" and not line:match("^#") then
			local chunk = assert(loadfile(dir .. "/" .. line))
			chunk("DoggsProbe", NS)
		end
	end
	f:close()
	return NS
end

return STUB
