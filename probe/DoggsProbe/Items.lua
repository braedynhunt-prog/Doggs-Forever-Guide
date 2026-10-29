-- DoggsProbe / Items.lua
-- Item logger: every item tooltip shown (bags, loot, vendors, AH, chat links, quest rewards) plus
-- direct scans of equipped items, bag contents, quest reward choices, vendor stock and loot windows.
-- Items are stored account-wide per client (DoggsProbeDB.items[toc][itemID]); quests, vendors and
-- loot sources are stored per character.

local ADDON, NS = ...
local API = NS.API

local Items = {}
NS.Items = Items

local SRC_CAP = 8
local lastSeen = {}       -- itemID -> GetTime() of the last count
local context = nil       -- "quest:123:Title" / "vendor:Name" / "loot:Name" / "ah" / "mail" / nil

function Items.Context() return context or "other" end

local function now() return time() end

-------------------------------------------------------------------------------
-- Record
-------------------------------------------------------------------------------
function Items.FillInfo(rec)
	if not rec.name then
		local info = API.ItemInfo(rec.link or rec.id)
		if info then
			for k, v in pairs(info) do
				if k ~= "link" then rec[k] = v end
			end
			if info.link and (not rec.link or #info.link > #rec.link) then rec.link = info.link end
		end
	end
	if not rec.stats and rec.link then
		rec.stats = API.ItemStats(rec.link)
	end
end

-- id: item id; link: item link or nil; lines: tooltip lines or nil; src: context string
function Items.Record(id, link, lines, src)
	id = NS.SafeNumber(id)
	if not id then return nil end
	local db = NS.items
	local rec = db[id]
	local isNew = not rec
	if not rec then
		rec = { id = id, first = now(), n = 0, src = {} }
		db[id] = rec
	end
	local t = GetTime()
	if not lastSeen[id] or t - lastSeen[id] > 1 then
		rec.n = rec.n + 1
		rec.last = now()
		lastSeen[id] = t
	end
	link = NS.SafeString(link)
	if link and (not rec.link or #link > #rec.link) then rec.link = link end
	if lines and #lines > 0 and (not rec.lines or #lines >= #rec.lines) then rec.lines = lines end
	if src then
		src = tostring(src)
		if not rec.src[src] then
			local n = 0
			for _ in pairs(rec.src) do n = n + 1 end
			if n < SRC_CAP then rec.src[src] = now() end
		end
		rec.firstSrc = rec.firstSrc or src
	end
	rec.lvlSeen = rec.lvlSeen or NS.SafeNumber(UnitLevel("player"))
	Items.FillInfo(rec)
	if isNew then
		Items.newThisSession = (Items.newThisSession or 0) + 1
		NS.Debug("new item", id, rec.name or "?", src or "")
	end
	return rec
end

-- record an item by link, scanning its tooltip for the raw lines
function Items.RecordLink(link, src, lines)
	local id = NS.ItemIDFromLink(link)
	if not id then return nil end
	if not lines then
		local rec = NS.items[id]
		if not rec or not rec.lines then lines = API.TooltipLinesForLink(link) end
	end
	return Items.Record(id, link, lines, src)
end

function Items.Count()
	local n = 0
	for _ in pairs(NS.items) do n = n + 1 end
	return n
end

function Items.Recent(k)
	local list = {}
	for _, rec in pairs(NS.items) do list[#list + 1] = rec end
	table.sort(list, function(a, b) return (a.last or a.first or 0) > (b.last or b.first or 0) end)
	local out = {}
	for i = 1, math.min(k or 5, #list) do out[i] = list[i] end
	return out
end

-------------------------------------------------------------------------------
-- Tooltip hooks
-------------------------------------------------------------------------------
local function handleTooltipData(tooltip, data)
	if tooltip and tooltip.IsForbidden and tooltip:IsForbidden() then return end
	local lines, id = NS.LinesFromData(data)
	local link
	if tooltip and tooltip.GetItem then
		local ok, _, l = pcall(tooltip.GetItem, tooltip)
		if ok then link = l end
	end
	if not link and TooltipUtil and TooltipUtil.GetDisplayedItem then
		local ok, _, l = pcall(TooltipUtil.GetDisplayedItem, tooltip)
		if ok then link = l end
	end
	if not link and data and data.hyperlink then link = data.hyperlink end
	id = id or NS.ItemIDFromLink(link)
	if not id then return end
	Items.Record(id, link, lines, Items.Context())
end

local function handleTooltipFrame(tip)
	if tip and tip.IsForbidden and tip:IsForbidden() then return end
	local ok, _, link = pcall(tip.GetItem, tip)
	if not ok then return end
	local id = NS.ItemIDFromLink(link)
	if not id then return end
	local lines = NS.LinesFromFrame(tip)
	Items.Record(id, link, lines, Items.Context())
end

function Items.InstallHooks()
	if Items.hookMode then return end
	if TooltipDataProcessor and type(TooltipDataProcessor.AddTooltipPostCall) == "function"
		and Enum and Enum.TooltipDataType and Enum.TooltipDataType.Item then
		TooltipDataProcessor.AddTooltipPostCall(Enum.TooltipDataType.Item, function(tooltip, data)
			NS.SafeCall("tooltip:data", handleTooltipData, tooltip, data)
		end)
		Items.hookMode = "TooltipDataProcessor"
	else
		local n = 0
		for _, name in ipairs({ "GameTooltip", "ItemRefTooltip", "ShoppingTooltip1", "ShoppingTooltip2", "ItemRefShoppingTooltip1", "ItemRefShoppingTooltip2" }) do
			local tip = _G[name]
			if tip and tip.HookScript and tip.GetItem then
				local ok = pcall(tip.HookScript, tip, "OnTooltipSetItem", function(self)
					NS.SafeCall("tooltip:" .. name, handleTooltipFrame, self)
				end)
				if ok then n = n + 1 end
			end
		end
		Items.hookMode = "OnTooltipSetItem x" .. n
	end
	NS.apiReport.tooltipHook = Items.hookMode
end

-------------------------------------------------------------------------------
-- Scans: equipped items, bags
-------------------------------------------------------------------------------
function Items.ScanEquipped(force)
	local n = 0
	for slot = 1, 19 do
		local ok, link = pcall(GetInventoryItemLink, "player", slot)
		link = ok and NS.SafeString(link) or nil
		local id = NS.ItemIDFromLink(link)
		if id then
			local rec = NS.items[id]
			if force or not rec or not rec.lines then
				local lines = API.TooltipLinesForInventory(slot)
				Items.Record(id, link, lines, "equipped")
				n = n + 1
			end
		end
	end
	return n
end

function Items.ScanBags(force)
	local n = 0
	local maxBag = (_G.NUM_BAG_SLOTS or 4)
	if _G.NUM_TOTAL_EQUIPPED_BAG_SLOTS and _G.NUM_TOTAL_EQUIPPED_BAG_SLOTS > maxBag then maxBag = _G.NUM_TOTAL_EQUIPPED_BAG_SLOTS end
	for bag = 0, maxBag do
		local slots = API.BagSlots(bag)
		for slot = 1, slots do
			local link = API.BagLink(bag, slot)
			local id = NS.ItemIDFromLink(link)
			if id then
				local rec = NS.items[id]
				if force or not rec or not rec.lines then
					local lines = API.TooltipLinesForBag(bag, slot)
					Items.Record(id, link, lines, "bag")
					n = n + 1
				end
			end
		end
	end
	return n
end

-------------------------------------------------------------------------------
-- Quests
-------------------------------------------------------------------------------
local function questRecord(qid)
	local q = NS.char.quests[qid]
	if not q then
		q = { first = now() }
		NS.char.quests[qid] = q
	end
	q.last = now()
	return q
end

local function questFrameEvent(event)
	local okQ, qid = pcall(GetQuestID)
	qid = okQ and NS.SafeNumber(qid) or nil
	if not qid or qid == 0 then return end
	local okT, title = pcall(GetTitleText)
	title = okT and NS.SafeString(title) or nil
	local q = questRecord(qid)
	q.title = title or q.title
	q.lvlSeen = q.lvlSeen or NS.SafeNumber(UnitLevel("player"))
	local okN, npc = pcall(UnitName, "questnpc")
	if not okN or not npc then okN, npc = pcall(UnitName, "npc") end
	if okN and NS.SafeString(npc) then q.npc = npc end
	context = "quest:" .. qid .. ":" .. tostring(q.title or "?")
	q.events = q.events or {}
	q.events[event] = (q.events[event] or 0) + 1

	if event == "QUEST_DETAIL" then
		local okO, obj = pcall(GetObjectiveText); if okO then q.objectiveText = NS.SafeString(obj) end
		local okX, xp = pcall(GetRewardXP); if okX then q.xp = NS.SafeNumber(xp) end
		local okM, money = pcall(GetRewardMoney); if okM then q.money = NS.SafeNumber(money) end
		local okD, text = pcall(GetQuestText)
		if okD and NS.SafeString(text) then q.text = text:sub(1, 400) end
	end
	if event == "QUEST_DETAIL" or event == "QUEST_COMPLETE" then
		local okC, nChoices = pcall(GetNumQuestChoices)
		nChoices = okC and NS.SafeNumber(nChoices) or 0
		if nChoices > 0 then
			q.choices = {}
			for i = 1, nChoices do
				local okL, link = pcall(GetQuestItemLink, "choice", i)
				link = okL and NS.SafeString(link) or nil
				if link then
					q.choices[i] = link
					local lines = API.TooltipLinesForQuestItem("choice", i) or API.TooltipLinesForLink(link)
					Items.RecordLink(link, context, lines)
				end
			end
		end
		local okR, nRewards = pcall(GetNumQuestRewards)
		nRewards = okR and NS.SafeNumber(nRewards) or 0
		if nRewards > 0 then
			q.rewards = {}
			for i = 1, nRewards do
				local okL, link = pcall(GetQuestItemLink, "reward", i)
				link = okL and NS.SafeString(link) or nil
				if link then
					q.rewards[i] = link
					local lines = API.TooltipLinesForQuestItem("reward", i) or API.TooltipLinesForLink(link)
					Items.RecordLink(link, context, lines)
				end
			end
		end
		if event == "QUEST_COMPLETE" then
			local okX, xp = pcall(GetRewardXP); if okX and NS.SafeNumber(xp) then q.xpAtTurnIn = xp end
			q.turnedIn = q.turnedIn or now()
		end
	end
	NS.Debug(event, qid, q.title)
end

NS.On("QUEST_DETAIL", function() questFrameEvent("QUEST_DETAIL") end)
NS.On("QUEST_PROGRESS", function() questFrameEvent("QUEST_PROGRESS") end)
NS.On("QUEST_COMPLETE", function() questFrameEvent("QUEST_COMPLETE") end)
NS.On("QUEST_FINISHED", function() if context and context:sub(1, 6) == "quest:" then context = nil end end)

NS.On("QUEST_ACCEPTED", function(a, b)
	local qid = NS.SafeNumber(b) or NS.SafeNumber(a)
	if not qid or qid == 0 then return end
	local q = questRecord(qid)
	q.accepted = q.accepted or now()
	q.lvlAccepted = q.lvlAccepted or NS.SafeNumber(UnitLevel("player"))
	C_Timer.After(1.5, function()
		NS.SafeCall("quest:objectives", function()
			local obj = API.QuestObjectives(qid)
			if obj and #obj > 0 then q.objectives = obj end
			if not q.title and C_QuestLog and type(C_QuestLog.GetTitleForQuestID) == "function" then
				local ok, title = pcall(C_QuestLog.GetTitleForQuestID, qid)
				if ok and NS.SafeString(title) then q.title = title end
			end
		end)
	end)
end)

NS.On("QUEST_TURNED_IN", function(qid, xp, money)
	qid = NS.SafeNumber(qid)
	if not qid then return end
	local q = questRecord(qid)
	q.turnedIn = now()
	q.xpGained = NS.SafeNumber(xp)
	q.moneyGained = NS.SafeNumber(money)
	q.lvlTurnedIn = NS.SafeNumber(UnitLevel("player"))
end)

-------------------------------------------------------------------------------
-- Vendors
-------------------------------------------------------------------------------
NS.On("MERCHANT_SHOW", function()
	local okN, name = pcall(UnitName, "npc")
	name = okN and NS.SafeString(name) or nil
	local okG, guid = pcall(UnitGUID, "npc")
	guid = okG and NS.SafeString(guid) or nil
	local key = name or guid or "unknown vendor"
	context = "vendor:" .. key
	local v = NS.char.vendors[key]
	if not v then
		v = { name = name, first = now(), items = {} }
		NS.char.vendors[key] = v
	end
	v.last = now()
	v.visits = (v.visits or 0) + 1
	if guid then v.npcID = NS.NpcIDFromGUID(guid) end
	local okZ, zone = pcall(GetZoneText); if okZ then v.zone = NS.SafeString(zone) end
	local okSZ, sub = pcall(GetSubZoneText); if okSZ then v.subzone = NS.SafeString(sub) end
	local okC, n = pcall(GetMerchantNumItems)
	n = okC and NS.SafeNumber(n) or 0
	local items = {}
	for i = 1, n do
		local okL, link = pcall(GetMerchantItemLink, i)
		link = okL and NS.SafeString(link) or nil
		local id = NS.ItemIDFromLink(link)
		if id then
			local info = API.MerchantItem(i) or {}
			items[#items + 1] = { id, info.price, info.stack, info.avail, info.ext and 1 or nil }
			local rec = NS.items[id]
			local lines = nil
			if not rec or not rec.lines then lines = API.TooltipLinesForMerchant(i) or API.TooltipLinesForLink(link) end
			Items.Record(id, link, lines, context)
		end
	end
	if #items > 0 then
		v.items = items
		v.itemFields = "id,price(copper),stack,avail(-1=unlimited),extendedCost"
	end
	NS.Debug("vendor", key, n, "items")
end)
NS.On("MERCHANT_CLOSED", function() if context and context:sub(1, 7) == "vendor:" then context = nil end end)

-------------------------------------------------------------------------------
-- Loot
-------------------------------------------------------------------------------
local function lootSourceName(slot)
	local guid
	if type(GetLootSourceInfo) == "function" then
		local ok, g = pcall(GetLootSourceInfo, slot)
		if ok and NS.SafeString(g) then guid = g end
	end
	local okT, tguid = pcall(UnitGUID, "target")
	if not guid and okT and NS.SafeString(tguid) then guid = tguid end
	if guid then
		local u = NS.units[guid]
		if u and u.name then return u.name, guid end
		local npcID, kind = NS.NpcIDFromGUID(guid)
		if npcID then return (kind or "npc") .. "#" .. npcID, guid end
		return kind or "?", guid
	end
	return "?", nil
end

NS.On("LOOT_OPENED", function()
	local okN, n = pcall(GetNumLootItems)
	n = okN and NS.SafeNumber(n) or 0
	local srcName
	for slot = 1, n do
		local okL, link = pcall(GetLootSlotLink, slot)
		link = okL and NS.SafeString(link) or nil
		local id = NS.ItemIDFromLink(link)
		if id then
			if not srcName then srcName = lootSourceName(slot) end
			context = "loot:" .. srcName
			local rec = NS.items[id]
			local lines = nil
			if not rec or not rec.lines then lines = API.TooltipLinesForLoot(slot) or API.TooltipLinesForLink(link) end
			Items.Record(id, link, lines, context)
			local src = NS.char.loot[srcName]
			if not src then
				src = {}
				NS.char.loot[srcName] = src
			end
			src[id] = (src[id] or 0) + 1
		end
	end
	if not srcName then context = "loot:?" end
end)
NS.On("LOOT_CLOSED", function() if context and context:sub(1, 5) == "loot:" then context = nil end end)

-------------------------------------------------------------------------------
-- Other windows (context only)
-------------------------------------------------------------------------------
NS.On("AUCTION_HOUSE_SHOW", function() context = "ah" end)
NS.On("AUCTION_HOUSE_CLOSED", function() if context == "ah" then context = nil end end)
NS.On("MAIL_SHOW", function() context = "mail" end)
NS.On("MAIL_CLOSED", function() if context == "mail" then context = nil end end)
NS.On("TRADE_SKILL_SHOW", function() context = "tradeskill" end)
NS.On("TRADE_SKILL_CLOSE", function() if context == "tradeskill" then context = nil end end)
NS.On("BANKFRAME_OPENED", function() context = "bank" end)
NS.On("BANKFRAME_CLOSED", function() if context == "bank" then context = nil end end)

-------------------------------------------------------------------------------
-- Triggers
-------------------------------------------------------------------------------
local prevLoaded = NS.OnLoaded
NS.OnLoaded = function(...)
	if prevLoaded then prevLoaded(...) end
	Items.InstallHooks()
end

local prevEnter = NS.OnEnterWorld
NS.OnEnterWorld = function(...)
	if prevEnter then prevEnter(...) end
	C_Timer.After(7, function()
		NS.SafeCall("items:login", function()
			local a = Items.ScanEquipped()
			local b = Items.ScanBags()
			NS.Printf("item logger: %d equipped + %d bag item(s) scanned, %d item(s) in the DB (%s)", a, b, Items.Count(), Items.hookMode or "no hook")
		end)
	end)
end

NS.On("BAG_UPDATE_DELAYED", function() NS.Debounce("items:bags", 3, function() Items.ScanBags() end) end)
NS.On("PLAYER_EQUIPMENT_CHANGED", function() NS.Debounce("items:equip", 2, function() Items.ScanEquipped() end) end)
