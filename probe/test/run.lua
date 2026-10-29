-- Scenario runner: lua5.1 run.lua <era|forever|blocked> <addon dir> <out.lua>
package.path = "./?.lua;" .. package.path
local STUB = dofile("wowstub.lua")
local dir, out = arg[2], arg[3]
local W = STUB.world
local fails = 0
local function say(l) io.write(l, "\n") end
local function check(cond, msg) if cond then say("  ok   " .. msg) else fails = fails + 1; say("  FAIL " .. msg) end end
local function section(s) say("\n== " .. s .. " (" .. STUB.profile .. ")") end
STUB.echo = false

-- world setup
W.equip[16] = STUB.link(2205)
W.equip[15] = STUB.link(5411)
W.bags[0][1] = STUB.link(159)
W.bags[0][2] = STUB.link(2589)
W.bags[1][1] = STUB.link(4540)

section("load")
local NS = STUB.loadAddon(dir, STUB.profile == "era" and "DoggsProbe_Vanilla.toc" or "DoggsProbe.toc")
STUB.fire("ADDON_LOADED", "SomethingElse")
STUB.fire("ADDON_LOADED", "DoggsProbe")
check(type(DoggsProbeDB) == "table", "DoggsProbeDB created")
check(NS.char and NS.char.meta.class == "SHAMAN", "char record " .. tostring(NS.charKey))
STUB.fire("PLAYER_ENTERING_WORLD", true, false)
STUB.advance(10)
check(#NS.char.snapshots == 1 and NS.char.snapshots[1].reason == "login", "login snapshot taken")
local s = NS.char.snapshots[1]
check(s.stats.spi[1] == 29 and s.ap[1] == 60, "snapshot stats/AP read correctly")
check(s.equip[16] ~= nil and s.mhTip and #s.mhTip > 0, "snapshot has main-hand link + tooltip lines")
check(s.talents.api ~= nil, "talents api recorded: " .. tostring(s.talents.api))
local nWatched = 0
for _ in pairs(NS.char.spells) do nWatched = nWatched + 1 end
check(nWatched == 6, "spell probe found 6 watched spells (" .. nWatched .. ")")
check(NS.char.spells["Earth Shock"] and NS.char.spells["Earth Shock"].rank == 2, "Earth Shock highest rank = 2")
check(NS.char.spells["Earth Shock"].latest.mana == 50, "Earth Shock mana cost read")
check(NS.char.spells["Rockbiter Weapon"].latest.desc:find("63"), "Rockbiter description carries the AP number")
check(NS.Items.Count() == 5, "login item scan: 5 items (" .. NS.Items.Count() .. ")")
check(NS.items[2205] and NS.items[2205].lines and #NS.items[2205].lines == 8, "equipped weapon tooltip lines captured")
check(NS.items[2205].stats and NS.items[2205].stats.ITEM_MOD_STRENGTH_SHORT == 4, "GetItemStats captured")

section("regen probe")
W.mana = 200
STUB.advance(30, 0.5)
STUB.fire("UNIT_SPELLCAST_SUCCEEDED", "player", "cast-1", 8044)   -- Earth Shock: mana cost -> fsr
W.mana = W.mana - 50
STUB.advance(10, 0.5)
table.insert(W.buffs, { name = "Drink", id = 430 })
STUB.advance(20, 0.5)
W.buffs = {}
W.combat = true
STUB.advance(6, 0.5)
W.combat = false
STUB.advance(2, 0.5)
local buckets = NS.char.regen.buckets
local keys = {}
for k in pairs(buckets) do keys[#keys + 1] = k end
table.sort(keys)
say("  buckets: " .. table.concat(keys, ", "))
check(buckets["10|29|27|idle"] and buckets["10|29|27|idle"].manaSec > 20, "idle bucket accumulated")
check(buckets["10|29|27|idle+fsr"] ~= nil, "fsr bucket exists after a mana cast")
check(buckets["10|29|27|drink"] ~= nil, "drink bucket exists")
local idle = buckets["10|29|27|idle"]
local rate = idle.mana / idle.manaSec
check(rate > 9 and rate < 12, string.format("idle regen rate %.2f/s ~ 10.4 expected", rate))
check(#NS.char.regen.raw > 20, "raw samples kept: " .. #NS.char.regen.raw)

section("imbue watcher")
W.imbueMH = true; W.imbueID = 1; W.apPos = 63
STUB.advance(2)
check(#NS.char.rockbiter == 1 and NS.char.rockbiter[1].delta == 63, "Rockbiter AP delta = 63")
check(NS.char.rockbiter[1].spells and NS.char.rockbiter[1].spells["Rockbiter Weapon"], "imbue spell text stored with the delta")
check(NS.char.snapshots[#NS.char.snapshots].reason == "imbue", "imbue snapshot taken")

section("level up + gear change")
W.level = 11; W.xp = 100; W.xpMax = 6000
STUB.fire("PLAYER_LEVEL_UP", 11)
STUB.advance(5)
check(NS.char.snapshots[#NS.char.snapshots].reason == "levelup 11", "levelup snapshot")
local before = #NS.char.spells["Earth Shock"].readings
W.spNature = 18
W.equip[11] = STUB.link(1200)
STUB.fire("PLAYER_EQUIPMENT_CHANGED", 11, true)
STUB.fire("PLAYER_EQUIPMENT_CHANGED", 11, true)
STUB.advance(5)
check(#NS.char.spells["Earth Shock"].readings == before + 1, "one new Earth Shock reading after +18 spell damage")
check(NS.char.spells["Earth Shock"].latest.spNature == 18 and NS.char.spells["Earth Shock"].latest.desc:find("37"), "reading carries SP 18 and the new numbers")
check(NS.items[1200] ~= nil, "new ring logged on equip")
STUB.fire("PLAYER_EQUIPMENT_CHANGED", 11, true)
STUB.advance(5)
check(#NS.char.spells["Earth Shock"].readings == before + 1, "identical re-scan deduped")

section("quests")
W.questID = 313; W.questTitle = "A Refugee's Quandary"; W.npcName = "Grelin Whitebeard"
W.questChoices = { STUB.link(2907), STUB.link(5411) }
W.questRewards = {}
STUB.fire("QUEST_DETAIL")
check(NS.char.quests[313] and #NS.char.quests[313].choices == 2, "quest detail logged with 2 choices")
check(NS.items[2907] and NS.items[2907].src["quest:313:A Refugee's Quandary"], "Tree Chopper logged from the quest context")
check(NS.items[2907].lines[7]:find("expertise"), "expertise line kept in raw lines")
STUB.fire("QUEST_ACCEPTED", 313)
STUB.fire("QUEST_FINISHED")
STUB.advance(3)
check(NS.char.quests[313].objectives and NS.char.quests[313].objectives[1]:find("Boar Rib"), "objectives captured after accept")
STUB.fire("QUEST_COMPLETE")
STUB.fire("QUEST_TURNED_IN", 313, 450, 250)
STUB.fire("QUEST_FINISHED")
check(NS.char.quests[313].xpGained == 450, "turn-in XP recorded")

section("vendor + loot")
W.npcName = "Tharek Blackstone"; W.npcGUID = "Creature-0-1-2-3-1247-0000000001"
W.merchant = { { link = STUB.link(159), name = "Refreshing Spring Water", price = 25 }, { link = STUB.link(4540), name = "Tough Hunk of Bread", price = 25 } }
STUB.fire("MERCHANT_SHOW")
STUB.fire("MERCHANT_CLOSED")
check(NS.char.vendors["Tharek Blackstone"] and #NS.char.vendors["Tharek Blackstone"].items == 2, "vendor stock logged")
check(NS.char.vendors["Tharek Blackstone"].npcID == 1247, "vendor npc id from GUID")
W.target = { guid = "Creature-0-1-2-3-1125-0000000099", name = "Crag Boar", level = 12, class = "normal" }
STUB.fire("PLAYER_TARGET_CHANGED")
W.lootGUID = W.target.guid
W.loot = { { link = STUB.link(2589) } }
STUB.fire("LOOT_OPENED")
STUB.fire("LOOT_CLOSED")
check(NS.char.loot["Crag Boar"] and NS.char.loot["Crag Boar"][2589] == 1, "loot source table")

section("tooltip hook")
STUB.hover(STUB.link(5411))
STUB.hover(STUB.link(5411))
check(NS.items[5411].n >= 1 and NS.items[5411].lines and #NS.items[5411].lines == 6, "hover recorded via " .. tostring(NS.Items.hookMode))

section("combat log")
local G = W.target.guid
local function dmg(amount) return STUB.profile == "era" and amount or STUB.secret(amount) end
-- SWING_DAMAGE payload: amount, overkill, school, resisted, blocked, absorbed, critical, glancing, crushing
STUB.cleu("SWING_DAMAGE", G, "Crag Boar", dmg(31), 0, 1, 0, 0, 0, false, false, false)
STUB.cleu("SWING_DAMAGE", G, "Crag Boar", dmg(62), 0, 1, 0, 0, 0, true, false, false)
STUB.cleu("SWING_DAMAGE", G, "Crag Boar", dmg(24), 0, 1, 0, 0, 0, false, true, false)
STUB.cleu("SWING_MISSED", G, "Crag Boar", "DODGE", false, 0)
STUB.cleu("SWING_MISSED", G, "Crag Boar", "MISS", false, 0)
-- SPELL_DAMAGE payload: spellId, spellName, school, amount, overkill, school, resisted, blocked, absorbed, critical
STUB.cleu("SPELL_DAMAGE", G, "Crag Boar", 8044, "Earth Shock", 8, dmg(38), 0, 8, 0, 0, 0, false)
STUB.cleu("SPELL_DAMAGE", G, "Crag Boar", 324, "Lightning Shield", 8, dmg(13), 0, 8, 0, 0, 0, true)
STUB.cleu("SPELL_MISSED", G, "Crag Boar", 8044, "Earth Shock", 8, "RESIST")
STUB.cleu("SPELL_CAST_SUCCESS", G, "Crag Boar", 8044, "Earth Shock", 8)
if STUB.profile == "blocked" then for i = 1, 95 do STUB.cleu("SWING_DAMAGE", G, "Crag Boar", 1, 0, 1, 0, 0, 0, false, false, false) end end
-- an event from someone else must be ignored
local c = NS.char.combat
local bk = string.format("%+d", 12 - W.level)
if STUB.profile == "era" then
	check(c.mode == "full" and c.swing[bk] and c.swing[bk].swings == 5 and c.swing[bk].dmg == 117, "era: full damage sums by level bucket " .. bk)
	check(c.swing[bk].miss.DODGE == 1 and c.swing[bk].miss.MISS == 1 and c.swing[bk].crits == 1 and c.swing[bk].glances == 1, "era: miss/crit/glance counts")
	check(c.spell["Earth Shock"].hits == 1 and c.spell["Earth Shock"].casts == 1 and c.spell["Earth Shock"].miss.RESIST == 1 and c.spell["Lightning Shield"].crits == 1, "era: spell buckets")
elseif STUB.profile == "forever" then
	check(c.mode == "counts" and c.swing[bk].swings == 5 and c.swing[bk].dmg == 0, "forever: switched to counts mode, no amounts stored")
	check(c.swing[bk].miss.DODGE == 1 and c.swing[bk].crits == 1, "forever: counts still kept")
	check(c.blocked == nil and c.enabled, "forever: sampling still enabled")
else
	check(c.blocked ~= nil and not c.enabled, "blocked: combat sampling disabled and flagged: " .. tostring(c.blocked))
end

section("slash commands")
local n0 = #STUB.output
for _, cmd in ipairs({ "", "status", "regen", "spells", "scan", "items", "bags", "combat", "rockbiter", "quests", "errors", "export", "help", "debug", "debug", "reset", "combat on" }) do
	STUB.slash(cmd)
end
check(#STUB.output > n0 + 40, "commands printed " .. (#STUB.output - n0) .. " lines")
local errs = DoggsProbeDB.errors or {}
check(#errs == 0, "no errors logged (" .. #errs .. ")")
for _, e in ipairs(errs) do say("    error: " .. tostring(e.where) .. ": " .. tostring(e.msg)) end

section("SavedVariables (full)")
local okF, errF = pcall(STUB.writeSavedVariables, out)
check(okF, "full DB serialised" .. (okF and "" or (": " .. tostring(errF))))

section("reset + reload path")
STUB.slash("reset confirm")
check(#NS.char.snapshots == 0 and NS.Items.Count() >= 5, "reset wiped the character but kept items")
STUB.slash("")
check(#NS.char.snapshots == 1, "snapshot works after reset")
STUB.advance(3)

section("SavedVariables")
local ok, err = pcall(STUB.writeSavedVariables, out .. ".after-reset.lua")
check(ok, "serialised after reset without secret/unserialisable values" .. (ok and "" or (": " .. tostring(err))))
say(string.format("\n%s: %d check(s) failed", STUB.profile, fails))
-- dump a few chat lines so the wording can be eyeballed
say("\n-- sample chat output --")
local shown = 0
for i = 1, #STUB.output do
	local l = STUB.output[i]
	if l:find("DoggsProbe") and shown < 14 then say("  " .. l); shown = shown + 1 end
end
os.exit(fails == 0 and 0 or 1)
