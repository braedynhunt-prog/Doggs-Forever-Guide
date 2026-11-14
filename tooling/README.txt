Forever route tooling (moved out of the Claude project on 24 Sep 2026 so it isn't loaded into every chat)

These are the scripts a Claude session used to build the 1-20 Dwarf Shaman guide from the atlas.
Since 25 Sep 2026 the scripts find everything relative to this "WoW Forever Atlas" folder (set the FOREVER_ATLAS
environment variable to point elsewhere):
  ..\data\                     = atlas quests.json, entities.json, zone_*.json (from run.bat)
  tooling\qdb\*.json           = Questie's Classic DB converted with luatab.py (quest/npc/object/item.json; from Questie
                                 v11.38.0's Database\Classic\classic*DB.lua - rerun luatab.py on a newer Questie to refresh)
  ..\guide\Guidelime_ForeverShaman      = the addon folder check_guide.py reads (shared Shaman + Hunter guide since 25 Sep)
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

28 Oct 2026 - verification layer (first Claude Code session; the repo is a git repository from this day)
  guidelib.py          shared parsing + data access for the checkers: paths (FOREVER_ATLAS, FOREVER_GUIDE = addon folder override),
                       zone tables (ZONES for [G] names, ZID name -> Forever map id), tag regexes, quest/npc/object lookups
                       (qstarts/qends/npc_spawns/npc_zones), per-line helpers (steps, race_of, tags, quest_tags, gotos, tars) and the
                       race chains (Human = 00a/00b + shared, Dwarf = 01a/01b + shared). check_guide.py and verify.py import it.
                       Line numbers are the file's own (check_guide.py reported one too high before this day).
                       qdb row layout, 0-indexed as Python reads it: quest [0] name [1] startedBy [npcs, objects, items] [2] finishedBy
                       [npcs, objects] [3] reqLevel [9] objectives [11] preQuestGroup [12] preQuestSingle; npc [0] name [6] spawns
                       {zoneId: [[x, y], ...]}; object [0] name [3] spawns; item [0] name [1] npcDrops [5] questRewards [13] vendors
                       (RULES.md quotes the same columns 1-indexed: "item row 14 = vendors, row 2 = npc drops").
  verify.py            data checks on the Dwarf Shaman route (Human / Hunter lines skipped):
                         questnpc  the [TAR] on every [QA]/[QT] line is the quest's starter/finisher in qdb/quest.json
                         tar       every [TAR] exists with the written name; the line's [G] is within 3 units of a DB spawn
                                   (first [TAR]; later ones on the line within 15); supersedes tarcheck.py, which still works
                         gates     recipes / trainer ranks / Camping 101 / fishing gear come after the steps that learn the
                                   profession, raise its cap or state a cook-to-N / fish-to-N target (skill_gates.json)
                         xp        (1 Nov 2026) every "N XP" on a [QA]/[QT] line equals a quest on the line, an 80/60/40/20/10%
                                   level-scaled share of one (+-5), or the line's sum; "A + B XP" is checked number by number.
                                   Reads data\zone_*.json (a browser-refreshed zone's row wins; data\quests.json is not used).
                                   Chain / pair totals are skipped: a number whose clause (its parentheses, else ~60 chars
                                   around it) says chain, in all, pair, total, more or about, or contains a lone '+'
                         money     (5 Nov 2026) every money quote, four sub-checks prefixed in the message:
                                   quest: a reward on a [QT] line is one quest's data\zone_*.json "money" or the line's sum;
                                   vendor: "<Item> (<price>[ each][, total])" on [V]/"buy" lines = 4 x the tooltip sell price
                                   (+0..3c; newest weights\tooltips\*.json); trainer: [T] prices against trainer_costs.json;
                                   goldcheck: "Gold check" / "quest money so far|by now" lines against the running [QT] money
                                   and the quoted [V]/[T] purchases from chapter 02, within 15%.
  trainer_costs.json   (5 Nov 2026) Forever trainer prices per NPC from the Wowhead Forever NPC pages (browser pull;
                       steps in sources.json). fetch_tooltips.py now keeps money units ("Sell Price: 1s 80c").
                       python tooling\verify.py            -> only findings missing from verify_baseline.txt, exit 1 if any
                       python tooling\verify.py --all      -> everything, grouped by module, NEW marks lines not in the baseline
                       python tooling\verify.py --update-baseline   after Braedyn accepts a finding
  skill_gates.json     every recipe, trainer and cook-to-N / fish-to-N string in the guide with its skill value and source.
                       Recipe and fishing-item values are Forever tooltips (nether.wowhead.com/forever/tooltip/item/<id>, 28 Oct);
                       trainer ranks (Journeyman 50 / level 10) and Camping 101 thresholds are Classic values, marked unverified.
                       Add a row whenever a new recipe/trainer line goes into the guide.
  check_guide_baseline.txt / verify_baseline.txt   the accepted findings (13 Nov 2026: 26 check_guide lines, 91 verify lines; the round-2 additions are named in docs\40-50-build-2026-11-13.md).
  hook_check_guide.py  Claude Code PostToolUse hook (.claude\settings.json, matcher Edit|Write|MultiEdit): after a .lua under guide\
                       is edited it runs check_guide.py and verify.py and returns only what is missing from the baselines on stderr
                       with exit 2, so the finding lands back in the session. Hook settings load when Claude Code starts.
                       By hand: python tooling\hook_check_guide.py --file guide\Guidelime_ForeverShaman\02_LochModan.lua
  Python: none was installed on the PC before 28 Oct 2026 (the Microsoft Store stub only); Python 3.12.10 is now at
                       %LOCALAPPDATA%\Programs\Python\Python312\ and first on the user PATH.

29 Oct 2026 - data-pool review (nothing built yet; plan and sources in docs\forever-db-plan-2026-10-29.md)
  client\<build>\        Forever client DB2 tables as CSV from wago.tools (product "wowf"), pinned per build; see client\README.txt.
                         QuestXP, SkillLineAbility (recipe yellow/grey), QuestInfo, TaxiNodes for 1.60.1.70685 (28 Oct 2026).
  Facts checked 29 Oct:  nether tooltip endpoint carries "Drop Chance" only for single-dropper items; www.wowhead.com NPC pages
                         return 403 from a shell (browser console only); QuestieDB Forever 1.0.9 (26 Oct) is three releases past
                         our qdb\ 1.0.6; salty-max/wow-data publishes a daily forever.db (SQLite, same client build + QuestieDB +
                         cmangos loot chances, no quest XP); XP-per-level is Classic's table (Wowhead's September datamine retracted).

29 Oct 2026 - data freshness check
  sources.json         manifest of every game-data source the guide uses: path, upstream, how its version is checked, pull steps.
                       It stores no versions or dates; the checker reads those live (qdb\META.json, client\<build>\ folder names,
                       each data\zone_*.json "_browser_refresh"). Add a row when a new data source comes into use.
  check_sources.py     read-only: polls GitHub (Questie, salty-max) and wago.tools for the latest versions and prints OK / STALE /
                       INFO / ERROR per source with the pull steps.  Exit 0 fine, 1 stale, 2 a source unreachable (stop, don't use
                       old data).  --quiet prints only non-OK rows.  Run it at the start of any plan that relies on game data.
                       Wowhead XP has no upstream version (403 from a shell): a zone counts as stale once a wowf client build is
                       newer than its browser pull, which is a proxy, since not every build changes quest XP.
                       Python's ssl can't verify api.github.com on this PC; get_json() retries the same request with curl.

29 Oct 2026 - dungeon loot check and item tooltips
  qdb\                 refreshed to QuestieDB Forever 1.0.9 (bundle v12.3.1+v1.0.9, 26 Oct) with questiedb_baked.py; 1.0.6 is in git
                       2 Nov 2026: refreshed to 1.0.10 (bundle v12.4.0+v1.0.10, 2 Nov): same ids, 52 quest rows (reputation rounding,
                       273 objective) and 99 npc rows (rank field now filled: 1 elite, 4 rare) changed; no check changed. 1.0.9 is in git.
                       history. Spawn points 119,499 -> 77,962: Questie thinned dense clusters, almost all on Zephras Isle (16593);
                       route mobs checked unchanged. 3,825 NPCs have no spawns at all, including Hall of Thanes bosses Magmatus
                       (261316) and Faldrim Anvilmar (261306).
  client\<build>\Item.csv   ClassID / SubclassID / InventoryType for every item (complete; ItemSparse is not, so it is not pinned).
  fetch_tooltips.py    python tooling\fetch_tooltips.py <ids> | --from-file ids.txt  -> weights\tooltips\<today>.json (same shape as
                       weights\item_tooltips.json; never writes that file). nether.wowhead.com tooltip endpoint, one request per
                       second, plain UA; stops on any HTTP error other than 404. Keeps "Dropped by" / "Drop Chance" text.
                       Forever item stats changed between the 24 Sep scrape and 29 Oct for most items spot-checked.
  dungeon_loot.py      report only -> Claude outputs\dungeon-loot-<date>.md: per dungeon chapter (03 07 08 13 15 22 24 26), the gear
                       a 2H Enhancement shaman can use that QuestieDB lists as dropping from creatures spawning in the dungeon,
                       scored with weights\score_items.py, split into mentioned / not mentioned by the chapter, with a same-slot
                       comparison against items named on Gear:/Loot: lines. Tooltips: newest dated cache wins per item, then
                       item_tooltips.json. Ends with the ids that have no tooltip (feed them to fetch_tooltips.py).
                       Blind spots: creatures with no spawns (bosses above), and Ruins of Lordaeron / Excavation Site, which have
                       no creatures in QuestieDB.
  check_sources.py     new rows: item_tooltips (stale until a cache newer than the client build covers every item of the
                       24 Sep scrape) and pandaquest_forever (PandaQuest's Forever Wowhead overrides; empty on 29 Oct).

1 Nov 2026 - generator-built variants (warrior plan Phase 0; plan in docs\warrior-build-plan-2026-11-01.md)
  build_variant.py     builds a class/race variant addon from the Alliance chapters (never written):
                         python tooling\build_variant.py tooling\variants\skyborne_warrior\variant.json            -> guide\<folder>\ + <folder>.zip
                         python tooling\build_variant.py <variant.json> --out <dir> [--report <file>]             -> anywhere else
                         python tooling\build_variant.py <variant.json> --passthrough --out <dir>                 -> regression test: the
                                              source chapters must come out byte-identical (TOCs are the variant's)
                       Per source chapter: overlay\<key>.txt (anchors QA<id> QT<id> QC<id> TAR<id> G<x>,<y> "N <title>" "T <text>", #n for the
                       nth match; @replace @after @before @delete @header @gear-dungeon; an unknown or ambiguous anchor aborts),
                       then lines whose [A ...] tags exclude the variant are dropped and untagged [OC] Gear/Loot lines stripped,
                       then the generated gear lines go after their [QT] lines, then the [D ...] prefix and the footer group
                       are rewritten. Hand-written chapters (variants\<v>\chapters\) are copied verbatim; a missing one is a
                       warning. Writes both TOCs, the zip and a build report (drops, strips, overlay ops, gear placement,
                       inline gear text and "needs overlay" lines with a flag word). Full syntax: the script's docstring.
  variants\<v>\        variant.json (schema: variants\skyborne_warrior\README.txt), profile.json, chapters\, overlay\,
                       generated_gear.json, missing_tooltips.txt, build_report.txt
  gear_calls.py        --profile enh|prot|feral (default enh: the report is unchanged), --variant <variant.json> (score the variant's
                       chapters), --emit <file> (generated gear JSON for the builder; schema in the docstring; also writes the
                       variant's missing_tooltips.txt for fetch_tooltips.py --from-file). "unstated" = a choice has no tooltip.
  dungeon_loot.py      --profile / --variant as gear_calls.py; the default report is unchanged
  ..\weights\profiles.py   PROFILES {'enh', 'prot', 'feral'}: weights per band, usable(), score(), secondary slot, client Item.csv
                       filter, gear-line wording. enh = the shaman behaviour exactly; prot = ..\weights\prot_weights.py
                       (reasoning-only, docs\forever-prot-stat-weights.md). score_items.parse() now also reads armor, defense,
                       block value, block / dodge / parry chance, hit and crit (extra keys; enh scores unchanged).
                       2 Nov 2026: feral = ..\weights\feral_weights.py (bear sets for bands 10/15, cat sets for 20/25/30;
                       reasoning-only, docs\forever-feral-stat-weights.md); parse() also reads feral_ap and idols (Relic/Idol).
  variants\skyborne_druid\   Skyborne Feral Druid variant (2 Nov 2026): profile feral, folder Guidelime_ForeverDruid; hand-written
                       chapters 00s/00t/00u (Phase 2), overlay 02-26 (Phase 3, spec docs\druid-overlay-spec-2026-11-02.md), generated_gear.json
                       (feral emit, 97 picks; gear_skip_quests lists seven weapon/off-hand picks worded by hand in the overlay), built 2 Nov
                       (28 chapters, 305 overlay ops, 78 generated gear lines); record docs\druid-build-2026-11-02.md
  check_guide.py       2 Nov 2026: hearth-bind check - on each chain every [H X] must match the latest [S X] (the first [H] before any
                       [S] counts as the starting inn); found the Lakeshire bind (06) followed by "Hearth to Sentinel Hill" (07-10)
  guidelib.py          FOREVER_GUIDE naming a variant's output folder (its basename is variant.json "folder", or the folder holds
                       <folder>.toc) switches FOOTER, CHAINS (one chain, variant.json "chain"), DEFAULT_CHAIN, RACES and
                       RACE_WORDS to the variant; Warrior, Skyborne and Druid (2 Nov) are race/class words everywhere; Zephras Isle (16593,
                       Guidelime map 2521) is a known zone (also in tarcheck.py). baseline_path(): Alliance keeps
                       check_guide_baseline.txt / verify_baseline.txt, any other folder uses *_baseline_<folder>.txt.
                       12 Nov 2026: alternate chapters - ALTERNATES maps an alternate file to the chapter it replaces
                       (11s_DarkshoreShort.lua -> 11_Darkshore.lua; 11t_SleepingBag.lua -> None, an optional extra chapter that
                       replaces nothing, chain Dwarf+11t). The Human and Dwarf chains leave alternates out; each alternate
                       gets its own chain (Dwarf+11s = the Dwarf route with 11 swapped for 11s), which check_guide.py runs for
                       flow and hearth and verify.py takes as --chain Dwarf+11s. gold.py skips the alternate; tarcheck.py,
                       dungeon_loot.py and tugs_diff.py read every file. Variants list their chapters in variant.json, so an
                       alternate is not carried into them unless it is added there.
  verify.py            baseline and default --chain follow the folder (FOREVER_GUIDE=guide\Guidelime_ForeverWarrior -> Skyborne)
  tarcheck.py, pool30.py   read guidelib.ADDON (FOREVER_GUIDE) instead of the hard-coded Alliance folder
  hook_check_guide.py  checks the edited file's own addon folder with that folder's baselines; flags edits inside a generated
                       folder; an edit under tooling\variants\<v>\ rebuilds that variant and checks it, but only once
                       guide\<folder>\ exists (the first real build is run by hand)
  ..\weights\hunter_score.py   pinned to guide\Guidelime_ForeverShaman (was the first Guidelime_Forever* match)

12 Nov 2026 - round 2 (40-50) data refresh
  qdb\                 refreshed to QuestieDB Forever 1.0.16 (bundle v12.8.0+v1.0.16, 12 Nov): nothing removed, +211 quests (5,893),
                       576 quest rows changed (starter / finisher links), 1,769 npc rows (levels, ranks, spawns), 805 item rows (drop
                       sources). verify.py went from 202 to 65 findings; verify_baseline.txt was pruned of the 139 lines no longer
                       produced. 1.0.14 is in git history. Record: docs\audit-2026-11-12.md.
  client\1.60.1.70938\ the twelve tables for the 13 Nov build; diff in client\README.txt.
  route_xp.py          python tooling\route_xp.py <route file> [--share 0.65] [--start 42.0]  /  --table
                       13 Nov 2026: a chapter line may carry '| zones <map ids>' (the zones the chapter visits); every required quest is then
                       walked through the chapters (giver, objectives, ender) and a hand-in the route does not reach is a problem. The last
                       lines give the level with required levels enforced and the quests closed when their chapter is played.
                       Quest XP, quest money and predicted level per chapter from a plain list of quest ids per chapter
                       ("== title | wants N" lines, ids below, "opt:" lines listed but not counted). Flags a chapter whose highest
                       required level is above its predicted entry level, ids without an XP row, ids listed twice and ids the
                       written chapters already hand in. Holds the pre-2.3 XP-per-level table 1-60 from warcraft.wiki.gg
                       (30-40 655,400; 40-50 1,151,700; 50-60 1,778,600). RULES.md rule 14: a plan's XP table is this tool's
                       output on the list the plan prints. The table in tugs_diff.py is the later 2.3 one; do not reuse it.

13 Nov 2026 - QuestieDB 1.1.1
  qdb\                 refreshed to QuestieDB Forever 1.1.1 (bundle v12.9.0+v1.1.1, published 14 Nov 00:31 UTC): nothing removed,
                       +21 quests (5,914), 753 quest rows changed (398 gained an any-of prerequisite [12], 32 an all-of one [11];
                       also next-in-chain [21], exclusive-to [15], starters / finishers), 1,372 npc rows (spawns), 89 object rows,
                       270 item rows. check_guide.py went from 26 to 73 problems on the shaman guide: 47 "needs X turned in first"
                       lines, left open for a fix round. verify.py 92 -> 88 findings; verify_baseline.txt was pruned by hand of the
                       12 lines no longer produced and took five reworded Azshara lines. 1.0.16 is in git history.
                       Record: docs\audit-2026-11-13.md, last section.
  QuestXP              the bundle also ships QuestieDB\support\Forever\QuestXP\xpDB-traces.lua (QuestXP.db[id] = {level, xp},
                       3,559 rows built from QuestieTrace player traces). questiedb_baked.py does not read it. Compared once with
                       data\zone_*.json: of the shaman guide's 1,075 quests 955 are in both and 953 agree. It is not a source in
                       sources.json.
