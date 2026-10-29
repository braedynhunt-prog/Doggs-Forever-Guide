-- DoggsProbe / Core.lua
-- Namespace, chat output, error capture, the C_-first compat layer, SavedVariables init,
-- the event dispatcher and the 1-second ticker every module hangs off.
-- Lua 5.1, no libraries. Written against the modern C_ API with fallbacks to the old
-- globals so it loads on Classic Era 1.15.9 (11509) and WoW Forever (16001).

local ADDON, NS = ...
_G.DoggsProbe = NS            -- exposed for /run poking; not required by anything
NS.name = ADDON
NS.version = "2026.09.24"

local PREFIX = "|cff33ff99DoggsProbe|r: "
local SNAPSHOT_CAP  = 300     -- character snapshots kept per character
local ERROR_CAP     = 60      -- errors kept in the DB

NS.debug = false

-------------------------------------------------------------------------------
-- Output
-------------------------------------------------------------------------------
function NS.Print(...)
	local n = select("#", ...)
	local parts = {}
	for i = 1, n do parts[i] = tostring((select(i, ...))) end
	print(PREFIX .. table.concat(parts, " "))
end

function NS.Printf(fmt, ...)
	local ok, msg = pcall(string.format, fmt, ...)
	if not ok then msg = tostring(fmt) .. " (format error: " .. tostring(msg) .. ")" end
	print(PREFIX .. msg)
end

function NS.Debug(...)
	if NS.debug then NS.Print("|cff888888[debug]|r", ...) end
end

-------------------------------------------------------------------------------
-- Secret values (Forever inherited Midnight's addon restrictions) and safe calls
-------------------------------------------------------------------------------
local issecretvalue = _G.issecretvalue

-- true when v is a value addons are not allowed to read (comparing/adding it would error)
function NS.IsSecret(v)
	if issecretvalue then
		local ok, r = pcall(issecretvalue, v)
		if ok and r then return true end
	end
	return false
end

-- a number we are allowed to store, or nil
function NS.SafeNumber(v)
	if v == nil or NS.IsSecret(v) then return nil end
	if type(v) ~= "number" then return nil end
	return v
end

function NS.SafeString(v)
	if v == nil or NS.IsSecret(v) then return nil end
	if type(v) == "string" then return v end
	if type(v) == "number" or type(v) == "boolean" then return tostring(v) end
	return nil
end

function NS.SafeBool(v)
	if v == nil or NS.IsSecret(v) then return nil end
	return v and true or false
end

-- pcall a function and return its results; on error, log it and return nil
local errorsPrinted = 0
function NS.LogError(where, msg)
	local db = DoggsProbeDB
	if db then
		db.errors = db.errors or {}
		local list = db.errors
		list[#list + 1] = { t = time(), where = tostring(where), msg = tostring(msg), toc = NS.toc }
		while #list > ERROR_CAP do table.remove(list, 1) end
	end
	if errorsPrinted < 5 then
		errorsPrinted = errorsPrinted + 1
		NS.Print("|cffff5555error|r in " .. tostring(where) .. ": " .. tostring(msg))
		if errorsPrinted == 5 then NS.Print("(further errors go to DoggsProbeDB.errors only; /probe errors to list)") end
	end
end

function NS.SafeCall(where, fn, ...)
	local res = { pcall(fn, ...) }
	if not res[1] then
		NS.LogError(where, res[2])
		return nil
	end
	return unpack(res, 2)
end

-- call a global or C_ function by trying candidates in order; returns the packed results
-- of the first candidate that exists and does not error. cands = { fn1, fn2, ... }
function NS.TryCall(cands, ...)
	for i = 1, #cands do
		local fn = cands[i]
		if type(fn) == "function" then
			local res = { pcall(fn, ...) }
			if res[1] then return res end
		end
	end
	return nil
end

-------------------------------------------------------------------------------
-- Compat layer: modern C_ API first, old globals second. Every entry records
-- which path it took in NS.apiReport so /probe status can show it.
-------------------------------------------------------------------------------
local API = {}
NS.API = API
NS.apiReport = {}

local function report(key, value)
	if NS.apiReport[key] == nil then NS.apiReport[key] = value end
end

local function fn(ns, name)
	local t = _G[ns]
	if type(t) == "table" and type(t[name]) == "function" then return t[name] end
	return nil
end

-- Build info -----------------------------------------------------------------
function API.Build()
	local version, build, date, toc = GetBuildInfo()
	return { version = version, build = build, date = date, toc = toc, project = _G.WOW_PROJECT_ID }
end

-- Spells ---------------------------------------------------------------------
-- returns a normalised table { name, rank, icon, castTime, minRange, maxRange, spellID } or nil
function API.SpellInfo(id)
	local f = fn("C_Spell", "GetSpellInfo")
	if f then
		local res = { pcall(f, id) }
		if res[1] and type(res[2]) == "table" then
			report("spellInfo", "C_Spell.GetSpellInfo (table)")
			local t = res[2]
			return { name = t.name, icon = t.iconID, castTime = t.castTime, minRange = t.minRange,
				maxRange = t.maxRange, spellID = t.spellID or id }
		elseif res[1] and type(res[2]) == "string" then
			report("spellInfo", "C_Spell.GetSpellInfo (multi-return)")
			return { name = res[2], rank = res[3], icon = res[4], castTime = res[5], minRange = res[6],
				maxRange = res[7], spellID = res[8] or id }
		end
	end
	if type(GetSpellInfo) == "function" then
		local ok, name, rank, icon, castTime, minRange, maxRange, spellID = pcall(GetSpellInfo, id)
		if ok and name then
			report("spellInfo", "GetSpellInfo")
			return { name = name, rank = rank, icon = icon, castTime = castTime, minRange = minRange,
				maxRange = maxRange, spellID = spellID or id }
		end
	end
	return nil
end

function API.SpellDescription(id)
	local res = NS.TryCall({ fn("C_Spell", "GetSpellDescription"), _G.GetSpellDescription }, id)
	if res then
		report("spellDescription", fn("C_Spell", "GetSpellDescription") and "C_Spell" or "global")
		return NS.SafeString(res[2])
	end
	return nil
end

function API.SpellSubtext(id)
	local res = NS.TryCall({ fn("C_Spell", "GetSpellSubtext"), _G.GetSpellSubtext }, id)
	if res then return NS.SafeString(res[2]) end
	return nil
end

-- returns manaCost (number or nil) and a "type=cost,..." summary string
function API.SpellCost(id)
	local res = NS.TryCall({ fn("C_Spell", "GetSpellPowerCost"), _G.GetSpellPowerCost }, id)
	if not res or type(res[2]) ~= "table" then return nil, nil end
	report("spellCost", fn("C_Spell", "GetSpellPowerCost") and "C_Spell" or "global")
	local mana, parts = nil, {}
	local manaType = (Enum and Enum.PowerType and Enum.PowerType.Mana) or 0
	for _, c in ipairs(res[2]) do
		if type(c) == "table" then
			local cost = NS.SafeNumber(c.cost)
			local ptype = NS.SafeNumber(c.type)
			local pname = NS.SafeString(c.name)
			if cost then
				parts[#parts + 1] = (pname or tostring(ptype)) .. "=" .. cost
				if ptype == manaType or pname == "MANA" then mana = cost end
			end
		end
	end
	return mana, table.concat(parts, ",")
end

function API.RequestSpellData(id)
	local f = fn("C_Spell", "RequestLoadSpellData")
	if f then pcall(f, id) end
end

-- iterate the player's spellbook: cb(spellID, name, subName). Returns the api path used.
function API.ForEachSpellBookSpell(cb)
	local C = _G.C_SpellBook
	if C and type(C.GetNumSpellBookSkillLines) == "function" and type(C.GetSpellBookItemInfo) == "function" then
		report("spellbook", "C_SpellBook")
		local bank = (Enum and Enum.SpellBookSpellBank and Enum.SpellBookSpellBank.Player) or 0
		local spellType = (Enum and Enum.SpellBookItemType and Enum.SpellBookItemType.Spell) or 1
		local okN, numLines = pcall(C.GetNumSpellBookSkillLines)
		if not okN or type(numLines) ~= "number" then return "C_SpellBook (no skill lines)" end
		for line = 1, numLines do
			local okL, info = pcall(C.GetSpellBookSkillLineInfo, line)
			if okL and type(info) == "table" then
				local offset = info.itemIndexOffset or 0
				local count = info.numSpellBookItems or 0
				for i = offset + 1, offset + count do
					local okI, item = pcall(C.GetSpellBookItemInfo, i, bank)
					if okI and type(item) == "table" and item.spellID and (item.itemType == spellType or item.itemType == nil) then
						local name, sub = item.name, item.subName
						if (not name or name == "") and type(C.GetSpellBookItemName) == "function" then
							local okName, n2, s2 = pcall(C.GetSpellBookItemName, i, bank)
							if okName then name, sub = n2, s2 end
						end
						if name and not item.isOffSpec then cb(item.spellID, name, sub) end
					end
				end
			end
		end
		return "C_SpellBook"
	end
	if type(GetNumSpellTabs) == "function" and type(GetSpellBookItemInfo) == "function" then
		report("spellbook", "GetSpellTabInfo")
		local book = _G.BOOKTYPE_SPELL or "spell"
		for tab = 1, GetNumSpellTabs() do
			local _, _, offset, count = GetSpellTabInfo(tab)
			offset = offset or 0
			for i = offset + 1, offset + (count or 0) do
				local okI, stype, id = pcall(GetSpellBookItemInfo, i, book)
				if okI and stype == "SPELL" and id then
					local okN, name, sub = pcall(GetSpellBookItemName, i, book)
					if okN and name then cb(id, name, sub) end
				end
			end
		end
		return "GetSpellTabInfo"
	end
	report("spellbook", "none")
	return "none"
end

-- Items ----------------------------------------------------------------------
-- normalised item info table or nil (nil = not cached yet; a load request is sent)
function API.ItemInfo(idOrLink)
	local f = fn("C_Item", "GetItemInfo") or _G.GetItemInfo
	if not f then return nil end
	report("itemInfo", fn("C_Item", "GetItemInfo") and "C_Item.GetItemInfo" or "GetItemInfo")
	local ok, name, link, quality, ilvl, minLevel, itype, subtype, stack, equipLoc, icon, sellPrice,
		classID, subclassID, bindType = pcall(f, idOrLink)
	if not ok or not name then
		local req = fn("C_Item", "RequestLoadItemDataByID")
		local id = type(idOrLink) == "number" and idOrLink or NS.ItemIDFromLink(idOrLink)
		if req and id then pcall(req, id) end
		return nil
	end
	return {
		name = NS.SafeString(name), link = NS.SafeString(link), quality = NS.SafeNumber(quality),
		ilvl = NS.SafeNumber(ilvl), reqLevel = NS.SafeNumber(minLevel), type = NS.SafeString(itype),
		subType = NS.SafeString(subtype), equipLoc = NS.SafeString(equipLoc), sellPrice = NS.SafeNumber(sellPrice),
		classID = NS.SafeNumber(classID), subclassID = NS.SafeNumber(subclassID), bindType = NS.SafeNumber(bindType),
	}
end

function API.ItemStats(link)
	local res = NS.TryCall({ fn("C_Item", "GetItemStats"), _G.GetItemStats }, link)
	if not res or type(res[2]) ~= "table" then return nil end
	report("itemStats", fn("C_Item", "GetItemStats") and "C_Item.GetItemStats" or "GetItemStats")
	local out, any = {}, false
	for k, v in pairs(res[2]) do
		local kk, vv = NS.SafeString(k), NS.SafeNumber(v)
		if kk and vv then out[kk] = vv; any = true end
	end
	return any and out or nil
end

function NS.ItemIDFromLink(link)
	if type(link) ~= "string" then return nil end
	local id = link:match("item:(%d+)")
	return id and tonumber(id) or nil
end

-- Containers -----------------------------------------------------------------
function API.BagSlots(bag)
	local res = NS.TryCall({ fn("C_Container", "GetContainerNumSlots"), _G.GetContainerNumSlots }, bag)
	if res then
		report("container", fn("C_Container", "GetContainerNumSlots") and "C_Container" or "global")
		return NS.SafeNumber(res[2]) or 0
	end
	return 0
end

function API.BagLink(bag, slot)
	local res = NS.TryCall({ fn("C_Container", "GetContainerItemLink"), _G.GetContainerItemLink }, bag, slot)
	if res then return NS.SafeString(res[2]) end
	return nil
end

-- Auras ----------------------------------------------------------------------
-- cb(name, spellId) for every helpful aura on the player; return true from cb to stop
function API.ForEachPlayerBuff(cb)
	local g = fn("C_UnitAuras", "GetAuraDataByIndex")
	if g then
		report("auras", "C_UnitAuras.GetAuraDataByIndex")
		for i = 1, 80 do
			local ok, a = pcall(g, "player", i, "HELPFUL")
			if not ok or type(a) ~= "table" then break end
			local name = NS.SafeString(a.name)
			if name and cb(name, NS.SafeNumber(a.spellId)) then return end
		end
		return
	end
	if type(UnitAura) == "function" then
		report("auras", "UnitAura")
		for i = 1, 80 do
			local ok, name, _, _, _, _, _, _, _, _, spellId = pcall(UnitAura, "player", i, "HELPFUL")
			if not ok or not name then break end
			if cb(name, spellId) then return end
		end
		return
	end
	report("auras", "none")
end

-- Tooltips -------------------------------------------------------------------
-- Turn a C_TooltipInfo data table into a flat list of "left | right" strings, plus the item id.
function NS.LinesFromData(data)
	if type(data) ~= "table" then return nil end
	local lines = data.lines
	if type(lines) ~= "table" then return nil, NS.SafeNumber(data.id) end
	-- 10.0.2-style data keeps fields in .args until surfaced
	if TooltipUtil and type(TooltipUtil.SurfaceArgs) == "function" then
		if data.type == nil and data.args then pcall(TooltipUtil.SurfaceArgs, data) end
		for _, line in ipairs(lines) do
			if type(line) == "table" and line.leftText == nil and line.args then pcall(TooltipUtil.SurfaceArgs, line) end
		end
	end
	local out = {}
	for _, line in ipairs(lines) do
		if type(line) == "table" then
			local l = line.leftText
			local r = line.rightText
			if NS.IsSecret(l) then l = "<secret>" end
			if r ~= nil and NS.IsSecret(r) then r = nil end
			l = NS.SafeString(l)
			r = NS.SafeString(r)
			if l and l ~= "" then
				if r and r ~= "" then out[#out + 1] = l .. " | " .. r else out[#out + 1] = l end
			end
		end
	end
	return out, NS.SafeNumber(data.id)
end

-- Same for a tooltip frame (Era path): read GameTooltipTextLeftN / RightN
function NS.LinesFromFrame(tip)
	if not tip or not tip.GetName then return nil end
	local name = tip:GetName()
	if not name then return nil end
	local out = {}
	local n = tip.NumLines and tip:NumLines() or 0
	for i = 1, n do
		local L = _G[name .. "TextLeft" .. i]
		local R = _G[name .. "TextRight" .. i]
		local l = L and L.GetText and L:GetText()
		local r = R and R.GetText and R:IsShown() and R:GetText()
		if NS.IsSecret(l) then l = "<secret>" end
		if r ~= nil and NS.IsSecret(r) then r = nil end
		l = NS.SafeString(l)
		r = NS.SafeString(r)
		if l and l ~= "" then
			if r and r ~= "" then out[#out + 1] = l .. " | " .. r else out[#out + 1] = l end
		end
	end
	return out
end

local scanTip
function NS.ScanTip()
	if not scanTip then
		scanTip = CreateFrame("GameTooltip", "DoggsProbeScanTooltip", UIParent, "GameTooltipTemplate")
		scanTip:SetOwner(UIParent, "ANCHOR_NONE")
	end
	scanTip:ClearLines()
	scanTip:SetOwner(UIParent, "ANCHOR_NONE")
	return scanTip
end

-- generic tooltip fetch: infoName = C_TooltipInfo function name, setName = tooltip method name
local function tooltipLines(infoName, setName, ...)
	local g = fn("C_TooltipInfo", infoName)
	if g then
		report("tooltipScan", "C_TooltipInfo")
		local ok, data = pcall(g, ...)
		if ok and data then return NS.LinesFromData(data) end
		return nil
	end
	report("tooltipScan", "scan frame")
	local tip = NS.ScanTip()
	local setter = tip[setName]
	if type(setter) ~= "function" then return nil end
	local ok = pcall(setter, tip, ...)
	if not ok then return nil end
	return NS.LinesFromFrame(tip)
end

function API.TooltipLinesForLink(link)      return tooltipLines("GetHyperlink", "SetHyperlink", link) end
function API.TooltipLinesForInventory(slot) return tooltipLines("GetInventoryItem", "SetInventoryItem", "player", slot) end
function API.TooltipLinesForBag(bag, slot)  return tooltipLines("GetBagItem", "SetBagItem", bag, slot) end
function API.TooltipLinesForQuestItem(kind, i) return tooltipLines("GetQuestItem", "SetQuestItem", kind, i) end
function API.TooltipLinesForMerchant(i)     return tooltipLines("GetMerchantItem", "SetMerchantItem", i) end
function API.TooltipLinesForLoot(i)         return tooltipLines("GetLootItem", "SetLootItem", i) end

-- Merchant -------------------------------------------------------------------
function API.MerchantItem(i)
	local C = _G.C_MerchantFrame
	if C and type(C.GetItemInfo) == "function" then
		local ok, t = pcall(C.GetItemInfo, i)
		if ok and type(t) == "table" then
			report("merchant", "C_MerchantFrame.GetItemInfo")
			return { name = NS.SafeString(t.name), price = NS.SafeNumber(t.price), stack = NS.SafeNumber(t.stackCount),
				avail = NS.SafeNumber(t.numAvailable), ext = NS.SafeBool(t.hasExtendedCost) }
		end
	end
	if type(GetMerchantItemInfo) == "function" then
		local ok, name, _, price, stack, avail, _, _, ext = pcall(GetMerchantItemInfo, i)
		if ok then
			report("merchant", "GetMerchantItemInfo")
			return { name = NS.SafeString(name), price = NS.SafeNumber(price), stack = NS.SafeNumber(stack),
				avail = NS.SafeNumber(avail), ext = NS.SafeBool(ext) }
		end
	end
	return nil
end

-- Quest objectives for a quest in the log (after QUEST_ACCEPTED) ----------------
function API.QuestObjectives(questID)
	local g = fn("C_QuestLog", "GetQuestObjectives")
	if not g then return nil end
	local ok, list = pcall(g, questID)
	if not ok or type(list) ~= "table" then return nil end
	local out = {}
	for i, o in ipairs(list) do
		if type(o) == "table" then
			local text = NS.SafeString(o.text) or "?"
			local otype = NS.SafeString(o.type)
			local need = NS.SafeNumber(o.numRequired)
			out[i] = text .. (otype and (" [" .. otype .. "]") or "") .. (need and (" x" .. need) or "")
		end
	end
	return out
end

-------------------------------------------------------------------------------
-- Unit cache (levels/names by GUID, for loot sources and combat buckets)
-------------------------------------------------------------------------------
NS.units = {}
local unitOrder = {}
function NS.NoteUnit(unit)
	local ok, guid = pcall(UnitGUID, unit)
	if not ok or not guid or NS.IsSecret(guid) then return end
	local _, name = pcall(UnitName, unit)
	local _, level = pcall(UnitLevel, unit)
	local _, class = pcall(UnitClassification, unit)
	local _, ctype = pcall(UnitCreatureType, unit)
	local rec = NS.units[guid]
	if not rec then
		rec = {}
		NS.units[guid] = rec
		unitOrder[#unitOrder + 1] = guid
		if #unitOrder > 300 then
			local old = table.remove(unitOrder, 1)
			NS.units[old] = nil
		end
	end
	rec.name = NS.SafeString(name) or rec.name
	rec.level = NS.SafeNumber(level) or rec.level
	rec.class = NS.SafeString(class) or rec.class
	rec.ctype = NS.SafeString(ctype) or rec.ctype
end

function NS.NpcIDFromGUID(guid)
	if type(guid) ~= "string" then return nil end
	local kind, id = guid:match("^(%a+)%-%d+%-%d+%-%d+%-%d+%-(%d+)%-")
	if kind == "Creature" or kind == "Vehicle" or kind == "GameObject" then return tonumber(id), kind end
	return nil, kind
end

-------------------------------------------------------------------------------
-- SavedVariables
-------------------------------------------------------------------------------
NS.DB_VERSION = 1

function NS.CharKey()
	local name = UnitName("player") or "Unknown"
	local realm = GetRealmName() or "Realm"
	return name .. "-" .. realm
end

function NS.InitDB()
	DoggsProbeDB = DoggsProbeDB or {}
	local db = DoggsProbeDB
	db.version = NS.DB_VERSION
	db.items = db.items or {}
	db.chars = db.chars or {}
	db.errors = db.errors or {}
	db.created = db.created or time()

	local build = API.Build()
	NS.toc = build.toc or 0
	NS.build = build
	db.items[NS.toc] = db.items[NS.toc] or {}
	NS.items = db.items[NS.toc]

	local key = NS.CharKey()
	local c = db.chars[key]
	if not c then
		c = {}
		db.chars[key] = c
	end
	NS.charKey = key
	NS.char = c

	local _, class = UnitClass("player")
	local _, race = UnitRace("player")
	c.meta = c.meta or {}
	c.meta.name = UnitName("player")
	c.meta.realm = GetRealmName()
	c.meta.class = class
	c.meta.race = race
	c.meta.faction = UnitFactionGroup("player")
	c.meta.client = build
	c.meta.addonVersion = NS.version
	c.meta.created = c.meta.created or time()
	c.meta.lastLogin = time()
	c.meta.sessions = (c.meta.sessions or 0) + 1
	c.meta.hasIsSecretValue = (issecretvalue ~= nil)

	c.snapshots = c.snapshots or {}
	c.rockbiter = c.rockbiter or {}
	c.regen = c.regen or {}
	c.spells = c.spells or {}
	c.spellbook = c.spellbook or {}
	c.combat = c.combat or {}
	c.quests = c.quests or {}
	c.vendors = c.vendors or {}
	c.loot = c.loot or {}
	return c
end

function NS.PushSnapshot(s)
	local list = NS.char.snapshots
	list[#list + 1] = s
	while #list > SNAPSHOT_CAP do table.remove(list, 1) end
	return #list
end

function NS.ResetChar(all)
	local db = DoggsProbeDB
	db.chars[NS.charKey] = nil
	if all then
		db.items = {}
		db.errors = {}
	end
	NS.InitDB()
	if NS.OnReset then NS.OnReset() end
end

-------------------------------------------------------------------------------
-- Event dispatcher
-------------------------------------------------------------------------------
local handlers = {}
local frame = CreateFrame("Frame", "DoggsProbeEventFrame")
NS.frame = frame

function NS.On(event, handler, unit)
	if not handlers[event] then
		handlers[event] = {}
		if unit and frame.RegisterUnitEvent then
			frame:RegisterUnitEvent(event, unit)
		else
			frame:RegisterEvent(event)
		end
	end
	local list = handlers[event]
	list[#list + 1] = handler
end

frame:SetScript("OnEvent", function(self, event, ...)
	local list = handlers[event]
	if not list then return end
	for i = 1, #list do
		local ok, err = pcall(list[i], ...)
		if not ok then NS.LogError(event, err) end
	end
end)

-- debounce helper: NS.Debounce("key", seconds, fn) runs fn once, `seconds` after the last call
local pending = {}
function NS.Debounce(key, seconds, f)
	local stamp = (pending[key] or 0) + 1
	pending[key] = stamp
	C_Timer.After(seconds, function()
		if pending[key] == stamp then
			pending[key] = nil
			local ok, err = pcall(f)
			if not ok then NS.LogError("debounce:" .. key, err) end
		end
	end)
end

-------------------------------------------------------------------------------
-- 1-second ticker shared by the regen probe and the imbue watcher
-------------------------------------------------------------------------------
local tickers = {}
function NS.EveryTick(name, f) tickers[#tickers + 1] = { name = name, f = f } end

local ticker
function NS.StartTicker()
	if ticker then return end
	ticker = C_Timer.NewTicker(1, function()
		for i = 1, #tickers do
			local ok, err = pcall(tickers[i].f)
			if not ok then NS.LogError("tick:" .. tickers[i].name, err) end
		end
	end)
	NS.tickerRunning = true
end

-------------------------------------------------------------------------------
-- Lifecycle
-------------------------------------------------------------------------------
local loaded, enteredWorld = false, false
NS.On("ADDON_LOADED", function(name)
	if name ~= ADDON or loaded then return end
	loaded = true
	NS.InitDB()
	NS.Printf("v%s loaded on %s (build %s, toc %s) for %s. /probe for commands.",
		NS.version, tostring(NS.build.version), tostring(NS.build.build), tostring(NS.toc), NS.charKey)
	if NS.OnLoaded then NS.OnLoaded() end
end)

NS.On("PLAYER_ENTERING_WORLD", function(isLogin, isReload)
	if not loaded then return end
	if enteredWorld then return end
	enteredWorld = true
	NS.StartTicker()
	if NS.OnEnterWorld then NS.OnEnterWorld(isLogin, isReload) end
end)

NS.On("PLAYER_TARGET_CHANGED", function() NS.NoteUnit("target") end)
NS.On("UPDATE_MOUSEOVER_UNIT", function() NS.NoteUnit("mouseover") end)
