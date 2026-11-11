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

2 Nov 2026 - six more tables pulled into 1.60.1.70707/ for the shaman levelling sheet (docs/forever-shaman-leveling-sheet.pdf + .html):
  SpellName.csv, SpellLevels.csv, SkillLine.csv, SkillRaceClassInfo.csv, Talent.csv, TalentTab.csv
  Talent.csv/TalentTab.csv are the OLD Classic trees (Two-Handed Axes and Maces, Weapon Mastery...), not Forever's: the Forever
  talents are server-side (SpellName.csv does carry their spells: Mental Dexterity 415140, Shamanistic Focus 1223030, Earth Fury 1259719).
  wowforevertalents.com reads the live tree + hotfix cache and is the source the sheet used. SkillRaceClassInfo/SkillLineAbility say
  shaman Two-Handed Maces is baseline (acq 1) and Two-Handed Axes trainer-taught (Buliwyf Stonehand, Ironforge) - unverified in game.

2 Nov 2026 - TaxiPath.csv pulled into 1.60.1.70707/ for the druid guide (flight connections: FromTaxiNode, ToTaxiNode, Cost; join
  on TaxiNodes.csv ID). Moonglade: node 62 "Nighthaven, Moonglade" -> 27 Rut'theran Village at cost 0 (the druid-only flight, Silva
  Fil'naveth); node 49 "Moonglade" <-> 26 Auberdine (830c), 52 Everlook, 65 Talonbranch Glade (the general flight master, Sindrayl).
  TaxiPathNode (11k rows) was not pinned.

1.60.1.70753/  (build of 2 Nov 2026, fetched 2 Nov 2026) - all twelve tables (the five standard ones + TaxiPath + the six of the
               shaman sheet). Diff from 70707: QuestXP, QuestInfo, TaxiNodes, SkillLine, SkillRaceClassInfo, Talent, TalentTab
               identical; Item.csv +3 ids (289439, 289559, 289560), 277277 flag change; TaxiPath -2 paths (3275<->3276, Alterac?);
               SkillLineAbility 20 lines (druid: Ferocious Bite 1328618 at 24 and Lacerate 1328617 at 25 / 1328616 at 34 trainer rows,
               Primal Bite rows re-chained; new Command ranks for hunters, Enchant Boots - Speed); SpellLevels 47 lines (Primal Bite
               407995 25 -> 40, 1238069/70 50/60; new Echo of Light/Wisdom, Turn Evil, Holy Shield rows); SpellName 72 lines (new
               paladin/priest/druid spell names, Camping 1327906). Wowhead XP re-pulled for all 25 route zones after this build:
               no XP, level or reward change in any zone.

3 Nov 2026 - build 1.60.1.70755 pulled into 1.60.1.70755/ (wago.tools build of 3 Nov 2026 18:16 UTC)
Tables: QuestXP SkillLineAbility QuestInfo TaxiNodes Item TaxiPath SkillLine SkillRaceClassInfo SpellLevels SpellName Talent TalentTab.
Diffed against 1.60.1.70753 by ID: 0 added, 0 removed, 0 changed rows in all 12 tables; row counts identical
(e.g. SpellName 32070, SkillLineAbility 7858, Item 31985), and all 12 files are byte-identical.
Looks like a technical build with identical game data for these tables.

4 Nov 2026 - build 1.60.1.70790 pulled into 1.60.1.70790/ (wago.tools build of 4 Nov 2026 18:08 UTC, the launch-day client).
Tables: the same twelve. Diffed against 1.60.1.70755: QuestXP, QuestInfo, TaxiNodes, TaxiPath, SkillRaceClassInfo, Talent,
TalentTab byte-identical. SpellName 59 lines, mostly rogue/warrior: rogue talents renamed (13732 Improved Sinister Strike ->
Efficient Strikes, 14162 Improved Eviscerate -> Coup de Grace), Mutilate ranks 1310705-7 replaced by Venom 1329328 and Shank
1329283/1329549, new rogue spells (Composure, Flash of Steel, Boot Knife, Quick Getaway, Ghostly Strike); warrior 1310315
Raging Blows -> Improved Whirlwind, new Fury spell Reckless Swings 1329555; shaman 16166 Elemental Mastery -> Lightning Mastery
(Elemental tree) and 437009 Totemic Projection -> Totemic Call (already in the sheet since 3 Nov). SpellLevels 14 lines and
SkillLineAbility 28 lines carry those same rogue/warrior swaps (Shank at 24, Venom at 30). SkillLine: Flags 1040 -> 66576 on the
Arms, Combat, Subtlety, Feral Combat, Assassination, Fury, Protection lines. Item: 281350 Keystone Fragment, 281352 Ancient
Runestone, 281359 Dormant Runestone reclassified Miscellaneous (15) -> Key (13); 289555 added (quest item, no Wowhead name yet).
None of the changed spells or items is referenced by the shaman, warrior or druid guide or by any QuestieDB quest.

9 Nov 2026 - build 1.60.1.70862 pulled into 1.60.1.70862/ (wago.tools build of 7 Nov 2026). Tables: the same twelve. Diffed against
1.60.1.70790: QuestXP, QuestInfo, TaxiNodes, TaxiPath, SkillLine, SkillRaceClassInfo, Talent, TalentTab byte-identical. SpellName +400 rows,
all NPC/encounter or item spells (Shen'dorei quest spells, Manastorm, Mugg's Fury, "Elixir of Endless ..." consumables, Portal to
Auberdine/Southshore/Theramore/Menethil/Grom'gol, Ultra/Giga/Cosmic Hogger) - no player shaman, warrior or druid spell added, renamed or
removed. SpellLevels 95 rows, all test/old spells (Word of Recall (OLD), Zone Recall (OLD), Blizzard, Mana Drain, War Stomp) and NPC spells.
SkillLineAbility: one row (skill 778, spell 1313392 Summon Shen'dorei Wisp). Item: 267079 and 273845 reclassified to Key (13), 278989 icon
change, 21 new ids 287960/289081-289334 (quest items, BS chain plans 251340-251354 and Pattern: Trapper's Leather Armor 252772 appear in
QuestieDB 1.0.12 the same day). Nothing referenced by the guides changed.

11 Nov 2026 - build 1.60.1.70888 pulled into 1.60.1.70888/ (wago.tools build of 10 Nov 2026). Tables: the same twelve. Diffed against 1.60.1.70862: eleven tables byte-identical; Item: 271629 reclassified Quest (12) -> Miscellaneous (15, subclass 4) and one new id 290333 (class 2 subclass 3, a ranged weapon). Nothing referenced by the guides changed.
