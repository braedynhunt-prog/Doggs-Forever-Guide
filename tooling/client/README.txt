Forever client tables (DB2 -> CSV) from wago.tools, pinned per build. Fetched with
  curl -A "Mozilla/5.0" "https://wago.tools/db2/<Table>/csv?build=<build>"
(works from a shell; https://wago.tools/api/builds lists the builds under product "wowf").

1.60.1.70685/  (build of 28 Oct 2026, fetched 29 Oct 2026)
  QuestXP.csv            quest XP by quest level (ID) x difficulty tier (Difficulty_1..7); fallback for quests with no Wowhead XP
  SkillLineAbility.csv   per recipe spell: SkillLine (185 Cooking, 129 First Aid, 356 Fishing), TrivialSkillLineRankLow = yellow,
                         TrivialSkillLineRankHigh = grey. Values look post-vanilla for some recipes (Curiously Tasty Omelet 165/205 vs
                         Classic 150/190; Longjaw Mud Snapper 45/85 vs Classic 50/90; the bandages match Classic) - whether the server
                         uses them is unverified; keep the colour checks on the in-game test list.
  QuestInfo.csv          quest type ids (1 Elite, 41 PvP, 62 Raid, 81 Dungeon)
  TaxiNodes.csv          flight masters (names, world positions)

Plan and sources: docs\forever-db-plan-2026-10-29.md. Nothing reads these yet (fetch_client.py / simulate_xp.py are planned, not built).
