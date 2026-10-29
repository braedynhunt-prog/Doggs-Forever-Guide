-- DoggsProbe / Commands.lua
-- /probe slash commands. Everything prints to chat; the data itself is in SavedVariables.

local ADDON, NS = ...

local function printLines(lines, max)
	max = max or 40
	for i, l in ipairs(lines) do
		if i > max then NS.Printf("... %d more line(s) (see SavedVariables)", #lines - max); break end
		print("  " .. l)
	end
	if #lines == 0 then print("  (nothing recorded yet)") end
end

local function count(t)
	local n = 0
	for _ in pairs(t or {}) do n = n + 1 end
	return n
end

local function help()
	NS.Print("commands:")
	print("  /probe            take + print a character snapshot now")
	print("  /probe status     what is running, which API paths were taken, counts")
	print("  /probe regen      mana/health regen per level|spirit|int|state bucket")
	print("  /probe spells     latest reading of every watched spell (rank, cost, description)")
	print("  /probe scan       re-walk the spellbook and take spell readings now")
	print("  /probe items      item count and the last 5 items seen")
	print("  /probe bags       scan every equipped and bag item into the item DB")
	print("  /probe combat     swing/spell sampling by target level; 'combat on' retries after a block")
	print("  /probe rockbiter  the recorded imbue AP deltas")
	print("  /probe quests     quests seen (with reward choices)")
	print("  /probe errors     errors caught by the addon")
	print("  /probe debug      toggle verbose chat output")
	print("  /probe export     where the data file is and how to read it")
	print("  /probe reset confirm      wipe this character's data (items kept)")
	print("  /probe reset all confirm  wipe everything incl. the item DB")
	print("  Remember: SavedVariables only write on /reload or logout - /reload before you quit.")
end

local function status()
	local c = NS.char
	local b = NS.build or {}
	NS.Printf("v%s on %s build %s (toc %s, project %s) | %s | session %d",
		NS.version, tostring(b.version), tostring(b.build), tostring(NS.toc), tostring(b.project), NS.charKey, c.meta.sessions or 0)
	NS.Printf("ticker %s | tooltip hook: %s | issecretvalue: %s",
		NS.tickerRunning and "running" or "NOT running", tostring(NS.Items.hookMode), tostring(_G.issecretvalue ~= nil))
	local keys = {}
	for k in pairs(NS.apiReport) do keys[#keys + 1] = k end
	table.sort(keys)
	local parts = {}
	for _, k in ipairs(keys) do parts[#parts + 1] = k .. "=" .. tostring(NS.apiReport[k]) end
	NS.Print("api paths: " .. (#parts > 0 and table.concat(parts, ", ") or "(none used yet)"))
	NS.Printf("snapshots %d | rockbiter deltas %d | spells %d (book %d via %s) | items %d (%d new this session) | quests %d | vendors %d | loot sources %d",
		#c.snapshots, #c.rockbiter, count(c.spells), c.spellbookCount or 0, tostring(c.spellbookApi), NS.Items.Count(),
		NS.Items.newThisSession or 0, count(c.quests), count(c.vendors), count(c.loot))
	NS.Print(NS.Regen.Status())
	local cb = c.combat or {}
	NS.Printf("combat: mode %s, %s, %d events, %d errors%s", tostring(cb.mode or "full"), cb.enabled and "on" or "off",
		cb.events or 0, cb.errors or 0, cb.blocked and (", blocked: " .. tostring(cb.blocked)) or "")
	NS.Printf("errors logged: %d | talents api: %s", #(DoggsProbeDB.errors or {}), tostring(c.snapshots[#c.snapshots] and c.snapshots[#c.snapshots].talents and c.snapshots[#c.snapshots].talents.api))
	NS.Print("data only reaches disk on /reload or logout.")
end

local function items()
	NS.Printf("%d item(s) in the DB for this client (hook: %s). Last seen:", NS.Items.Count(), tostring(NS.Items.hookMode))
	for _, rec in ipairs(NS.Items.Recent(5)) do
		local srcs = {}
		for s in pairs(rec.src or {}) do srcs[#srcs + 1] = s end
		table.sort(srcs)
		print(string.format("  [%d] %s  ilvl %s req %s %s/%s %s | %d line(s), stats %s | seen x%d via %s",
			rec.id, tostring(rec.link or rec.name or "?"), tostring(rec.ilvl or "?"), tostring(rec.reqLevel or "?"),
			tostring(rec.type or "?"), tostring(rec.subType or "?"), tostring(rec.equipLoc or ""),
			rec.lines and #rec.lines or 0, rec.stats and tostring(count(rec.stats)) or "none", rec.n or 0, table.concat(srcs, "; ")))
	end
end

local function rockbiter()
	local list = NS.char.rockbiter
	NS.Printf("%d imbue change(s) recorded:", #list)
	for i, r in ipairs(list) do
		print(string.format("  #%d L%s: mh %s(id %s) -> %s(id %s) | AP %s -> %s (delta %s) | Str %s->%s Int %s->%s | dmg %s-%s -> %s-%s | %s",
			i, tostring(r.lvl), tostring(r.before.mh), tostring(r.before.mhID), tostring(r.after.mh), tostring(r.after.mhID),
			tostring(r.before.ap), tostring(r.after.ap), tostring(r.delta), tostring(r.before.str), tostring(r.after.str),
			tostring(r.before.int), tostring(r.after.int), tostring(r.before.dmin), tostring(r.before.dmax),
			tostring(r.after.dmin), tostring(r.after.dmax), date("%H:%M:%S", r.t)))
	end
end

local function quests()
	local ids = {}
	for id in pairs(NS.char.quests) do ids[#ids + 1] = id end
	table.sort(ids, function(a, b) return (NS.char.quests[a].last or 0) > (NS.char.quests[b].last or 0) end)
	NS.Printf("%d quest(s) seen; most recent first:", #ids)
	for i = 1, math.min(15, #ids) do
		local q = NS.char.quests[ids[i]]
		print(string.format("  [%d] %s | npc %s | xp %s | choices %d rewards %d | objectives %d",
			ids[i], tostring(q.title or "?"), tostring(q.npc or "?"), tostring(q.xp or q.xpGained or "?"),
			q.choices and #q.choices or 0, q.rewards and #q.rewards or 0, q.objectives and #q.objectives or 0))
	end
end

local function errors()
	local list = DoggsProbeDB.errors or {}
	NS.Printf("%d error(s) logged (newest last):", #list)
	for i = math.max(1, #list - 14), #list do
		local e = list[i]
		print(string.format("  %s [%s] %s", date("%m-%d %H:%M:%S", e.t or 0), tostring(e.where), tostring(e.msg)))
	end
end

local function export()
	NS.Print("the data lives in DoggsProbeDB, written to WTF\\Account\\<account>\\SavedVariables\\DoggsProbe.lua on /reload or logout.")
	NS.Print("do a /reload now, then copy that file; probe2json.py in WoW Forever Atlas\\probe\\ turns it into JSON.")
	NS.Printf("current size estimate: %d snapshots, %d items, %d regen samples, %d spells.",
		#NS.char.snapshots, NS.Items.Count(), NS.char.regen.samples or 0, count(NS.char.spells))
end

SLASH_DOGGSPROBE1 = "/probe"
SLASH_DOGGSPROBE2 = "/doggsprobe"
SlashCmdList["DOGGSPROBE"] = function(msg)
	msg = (msg or ""):gsub("^%s+", ""):gsub("%s+$", "")
	local cmd, rest = msg:match("^(%S+)%s*(.*)$")
	cmd = cmd and string.lower(cmd) or ""
	rest = rest and string.lower(rest) or ""
	local ok, err = pcall(function()
		if cmd == "" or cmd == "snap" or cmd == "snapshot" then
			NS.Snapshot.Take("manual")
		elseif cmd == "status" then
			status()
		elseif cmd == "regen" then
			local lines = NS.Regen.Report()
			NS.Print("regen buckets (mana/s excludes seconds at full mana and seconds where mana dropped):")
			printLines(lines, 60)
		elseif cmd == "spells" then
			NS.Print("watched spells, latest reading:")
			printLines(NS.Spells.Report(), 40)
		elseif cmd == "scan" then
			NS.Spells.Scan("manual")
			NS.Print("spell scan done; /probe spells to list")
		elseif cmd == "items" then
			items()
		elseif cmd == "bags" then
			local a = NS.Items.ScanEquipped(true)
			local b = NS.Items.ScanBags(true)
			NS.Printf("scanned %d equipped + %d bag item(s); %d item(s) in the DB", a, b, NS.Items.Count())
		elseif cmd == "combat" then
			if rest == "on" or rest == "retry" then
				NS.Combat.Retry()
			elseif rest == "off" then
				NS.Combat.Disable()
				NS.Print("combat sampling off until /probe combat on")
			end
			printLines(NS.Combat.Report(), 40)
		elseif cmd == "rockbiter" or cmd == "imbue" then
			rockbiter()
		elseif cmd == "quests" then
			quests()
		elseif cmd == "errors" then
			errors()
		elseif cmd == "debug" then
			NS.debug = not NS.debug
			NS.Print("debug output " .. (NS.debug and "on" or "off"))
		elseif cmd == "export" then
			export()
		elseif cmd == "reset" then
			if rest == "confirm" then
				NS.ResetChar(false)
				NS.Print("this character's data wiped (item DB kept). /reload to write it out.")
			elseif rest == "all confirm" then
				NS.ResetChar(true)
				NS.Print("everything wiped. /reload to write it out.")
			else
				NS.Print("type '/probe reset confirm' (this character) or '/probe reset all confirm' (everything)")
			end
		else
			help()
		end
	end)
	if not ok then NS.LogError("command:" .. cmd, err) end
end
