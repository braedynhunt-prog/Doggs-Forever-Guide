Forever client tables (DB2 -> CSV) from wago.tools, pinned per build. Fetched with
  curl -A "Mozilla/5.0" "https://wago.tools/db2/<Table>/csv?build=<build>"
(works from a shell; https://wago.tools/api/builds lists the builds under product "wowf").

1.60.1.70707/  (build of 30 Oct 2026, fetched 1 Nov 2026) - same five tables. Diff from 70685: Item.csv +106 ids, 1 changed
               row; SkillLineAbility only enchanting rows at skill 360 and three removed rows; QuestXP, QuestInfo, TaxiNodes identical.
1.60.1.70685/  (build of 28 Oct 2026, fetched 29 Oct 2026)
  QuestXP.csv            quest XP by quest level (ID) x difficulty tier (Difficulty_1..7); fallback for quests with no Wowhead XP
  SkillLineAbility.csv   per recipe spell: SkillLine (185 Cooking, 129 First Aid, 356 Fishing), TrivialSkillLineRankLow = yellow,
                         TrivialSkillLineRankHigh = grey. Values look post-vanilla for some recipes (Curiously Tasty Omelet 165/205 vs
                         Classic 150/190; Longjaw Mud Snapper 45/85 vs Classic 50/90; the bandages match Classic) - whether the server
                         uses them is unverified; keep the colour checks on the in-game test list.
  QuestInfo.csv          quest type ids (1 Elite, 41 PvP, 62 Raid, 81 Dungeon)
  TaxiNodes.csv          flight masters (names, world positions)
  Item.csv               every item id with ClassID / SubclassID / InventoryType (fetched 29 Oct 2026); dungeon_loot.py uses it to
                         keep only gear a 2H Enhancement shaman can wear. ItemSparse is NOT pinned: it lacks many Classic items.

Plan and sources: docs\forever-db-plan-2026-10-29.md. Nothing reads these yet (fetch_client.py / simulate_xp.py are planned, not built).

2 Nov 2026 - TaxiPath.csv pulled into 1.60.1.70707/ for the druid guide (flight connections: FromTaxiNode, ToTaxiNode, Cost; join
  on TaxiNodes.csv ID). Moonglade: node 62 "Nighthaven, Moonglade" -> 27 Rut'theran Village at cost 0 (the druid-only flight, Silva
  Fil'naveth); node 49 "Moonglade" <-> 26 Auberdine (830c), 52 Everlook, 65 Talonbranch Glade (the general flight master, Sindrayl).
  TaxiPathNode (11k rows) was not pinned.
