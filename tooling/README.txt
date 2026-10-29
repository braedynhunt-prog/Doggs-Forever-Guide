Forever route tooling (moved out of the Claude project on 24 Sep 2026 so it isn't loaded into every chat)

These are the scripts a Claude session used to build the 1-20 Dwarf Shaman guide from the atlas.
Since 25 Sep 2026 the scripts find everything relative to this "WoW Forever Atlas" folder (set the FOREVER_ATLAS
environment variable to point elsewhere):
  ..\data\                     = atlas quests.json, entities.json, zone_*.json (from run.bat)
  tooling\qdb\*.json           = Questie's Classic DB converted with luatab.py (quest/npc/object/item.json; from Questie
                                 v11.38.0's Database\Classic\classic*DB.lua - rerun luatab.py on a newer Questie to refresh)
  ..\guide\Guidelime_ForeverAlliance      = the addon folder check_guide.py reads (shared Shaman + Hunter guide since 25 Sep)
  tooling\extra_quests.json     = optional hand-added atlas rows for quests the scrape missed ({"<questId>": {...atlas row...}})
Run from anywhere, e.g.  python tooling\check_guide.py   (pool.py still expects to be run from inside tooling\ for qdb\).

luatab.py        Questie Lua table file -> JSON            python3 luatab.py classicQuestDB.lua quest.json
pool.py          per-zone merged quest pool (atlas + Questie), Alliance/Dwarf filtered   python3 pool.py 1 38 1537
qdetail.py       full detail for atlas quests (objectives, entity coords, item stats)   python3 qdetail.py 96390 96393
loc.py           Questie spawn centroids for NPCs/objects   python3 loc.py "Crag Boar" 1125 obj:"Shimmerweed Basket"
check_guide.py   static flow check of the guide .lua files (tags, zones, QA->QT/QS, prerequisites, level bands,
                 [NX] chapter links). Known/accepted findings as of 25 Sep: 5 'optional quest step without [G]' Ongoing
                 lines and Call of Earth 94373 vs its level-10 twin 96243 (unverified in game).

scrape.py / build_report.py / report.js / report.css / zones.json / the TSV and the atlas HTML are the Wowhead
scraper and atlas page and were already in this folder (they run on the PC: see run.bat).
The stat-weight model and item scorer live in ..\weights\ (see its README).

17 Oct 2026 additions
  qdb\                 = QuestieDB Forever 1.0.6 decoded to JSON (quest/npc/object/item.json + META.json) - same row layout as before,
                         so every script reads it unchanged. 5,226 quests (982 new to Forever), NPC/object spawns in FOREVER map space.
                         No XP field. requiredRaces carries a high bit (Alliance = 4294967373; mask with & 77).
  qdb_classic\         = the old Questie v11.38.0 Classic DB (kept for comparisons)
  questiedb_baked.py   decode QuestieDB's baked TOC store:  python3 tooling\questiedb_baked.py <QuestieDB_Forever.toc> tooling\qdb
                       (the TOC is inside the official Questie release zip, QuestieDB\QuestieDB_Forever.toc; re-run on each release)
  tugs_diff.py         diff a TUGs Guidelime folder against our guide:  python3 tooling\tugs_diff.py compare\TUGs-1.12-2026-10-14\GuideLime_TUGs_Forever compare
  wh_quests.py         fetch Wowhead quest pages into extra_quests.json - Wowhead blocks page fetches since Oct 2026, so only the
                       nether tooltip endpoint works (name + objectives); kept for when/if the block lifts
  extra_quests.json    hand/tooltip-added atlas rows for quests the Sep 23 atlas lacks (check_guide / tugs_diff read it)
  coord_transform_forever.json  Classic -> Forever map transforms: Stormwind x' = 0.77367x + 19.68, y' = 0.77383y + 24.43;
                       Redridge x' = x - 5.09. Other 1-30 zones are identical. Questie Classic spawns and old Wowhead-Classic numbers
                       need it; the Forever DB spawns and the Forever atlas do not.
  check_guide.py       now runs the flow check once per race chain (Human 00a/00b+shared, Dwarf 01a/01b+shared; Shaman lines = Dwarf)

17 Oct 2026 - quest XP via the browser
  Wowhead Forever zone pages carry every quest's XP (the quest Listview), but block scripts.  Workflow that works:
    1. open https://www.wowhead.com/forever/zone=<id> in a real browser (Claude's built-in browser pane works)
    2. run tooling\wh_zone_listview.js in the console -> a TSV block
    3. python3 tooling\ingest_zone_tsv.py < block.tsv   (several blocks per file are fine; raw copies land in data\browser\)
  Pulled 17 Oct: 11 Wetlands, 10 Duskwood, 44 Redridge, 267 Hillsbrad, 1519 Stormwind, 1537 Ironforge,
    16732 Excavation Site, 16611 Ruins of Lordaeron, 717 Stockade, 1581 Deadmines, 16919 Hall of Thanes,
    36 Alterac, 130 Silverpine, 331 Ashenvale  (batch2.tsv / batch3.tsv in data\browser\ are the raw pulls).
    then 1 Dun Morogh, 12 Elwynn, 38 Loch Modan, 40 Westfall (batch4.tsv), 148 Darkshore, 45 Arathi, 33 STV (batch5.tsv).
  Not pulled: 406 Stonetalon (not on the route).  About 14 pages in a row trips a CloudFront 403; wait a few minutes.
  Quests Wowhead itself lists with blank XP: 98190 A Friend of the Family, 97894 Business in Auberdine, 87760 Holy Diver, 91736 Applejack Still.
  compare\forever_20-30_candidates.tsv = every Alliance class-free quest req 18-30 in the 20-30 zones ranked by XP (built 17 Oct).
