# Chapter 52 spec - Tabetha, Nethergarde, the crater and the Searing Gorge (draft, 13 Nov 2026)

Data used (all read 13 Nov 2026): tooling/qdb (QuestieDB Forever 1.0.16) quest rows [0]-[3] [7] [9] [11] [12] [24] [27], npc rows [0] [3]-[6] [13], item rows [0]-[2] [5]; `python tooling/qinfo.py` / `loc.py`; data/zone_{51,1537,15,4,36,1176}.json (Wowhead Forever XP, money, reqlevel, side, itemchoices / itemrewards); data/drop_rates.json; data/wowhead_quest_links.json (only 96770 is in it); tooling/client/1.60.1.70938/TaxiNodes.csv + TaxiPath.csv; tooling/trainer_costs.json (12 Nov); weights/tooltips/2026-11-12.json scored with the level-40 band (score_items.py functions, band 40); nether.wowhead.com/forever/tooltip/item/11818, /item/5396, /quest/3367 (13 Nov); classicdb.ch item 11818 (Classic rate, 13 Nov); docs/forever-shaman-leveling-sheet.html (training buys); round-1 chapters 27, 32, 35, 39d, 39e for roads, boats and binds. Re-checked facts from 43-draft2 (crater, Ironforge rows), 44-draft2 (Stormwind - Nethergarde), 48-draft2 (Explorers' League rows).

## 1. Header
- File: `52_SearingGorge.lua`
- Title: `[N 44-46 Searing Gorge]`; next: `[NX 45-47 Tanaris]` (plan: chapter 53 `[N 45-47 Tanaris]`); `[GA Alliance]` (chapter is Dwarf Shaman route; class steps `[A Shaman]`).
- Description: `[D Forever Shaman 30-60 (Braedyn)\\The eastern trip at 45: Tiara of the Deep to Tabetha, the Menethil boat, The Witch Doctor's Head at the Dalaran crater, Nekrum's Medallion and the Divination at Nethergarde Keep, then the Searing Gorge by the Badlands road (Dorius, the outhouse, the Thorium Brotherhood board and Hansel's three hunts) and the Explorers' League in Ironforge.]`
- Level on entry 44.7 (plan XP table), exit 45.6. Wants 45.

## 2. Entry state
- Stands at Gadgetzan (chapter 51 ends there after the Zul'Farrak hand-ins). Hearth = Gadgetzan (chapter 51's bind; plan Threads). Astral Recall goes to the same bind.
- Carried in (assumed from chapter 51 / earlier): 2846 Tiara of the Deep complete (Tiara 9234; taken from Tabetha in chapter 50), 2991 Nekrum's Medallion complete (Medallion 9471; taken from Thadius in chapter 49), 96770 The Witch Doctor's Head complete (Zum'rah's Head 277112; taken from Archmage Lan'dalock in chapter 43). If any boss item did not drop, that quest was abandoned in chapter 51 and its step here does not fire.
- Possibly carried (gates, only if an earlier Ironforge stop took them): 6625 Alliance Trauma, 6609 I Got Nothin' Left! / 6607 Nat Pagle, Angler Extreme.
- Also needed: 2439 The Platinum Discs handed in (39e:60, "level 40 only"); without it Magellas does not offer 2963 (row [12] = [2439]).
- Bring: 15 Silk Cloth (4306) for Caught! (row [7]); not a drop of this chapter's mobs in the data.
- Training that falls here: shaman level-44 row if still open (chapters 48/49 offer it at 44), level-46 row "if 46" at the end. Profession gates: Artisan First Aid / Artisan Fishing at Theramore (if carried) and their pickups in Ironforge (if not carried, for chapter 53's Theramore pass); Artisan Skinning at Balthus Stoneflayer if not learned.

## 3. Travel and hearth
Flight links (TaxiPath build 70938; node ids from TaxiNodes: Gadgetzan 39, Theramore 32, Menethil 7, Southshore 14, Ironforge 6, Stormwind 2, Nethergarde Keep 45, Thelsamar 8, Thorium Point 74 (Alliance node; 75 is the Horde one)). Costs are the raw Cost field in copper; price shown in game unverified.

| hop | link | cost |
|---|---|---|
| Gadgetzan - Theramore | 39->32 | 630 |
| Theramore - Menethil | boat (not in the data) | - |
| Menethil - Southshore | 7->14 direct | 330 |
| Southshore - Ironforge | 14->6 direct | 330 |
| Ironforge - Stormwind | Deeprun Tram (free; not in the data) or 6->2 50 | 0 |
| Stormwind - Nethergarde Keep | 2->45 direct | 830 |
| Nethergarde - Ironforge | hearth / Astral Recall (bind Ironforge) | 0 |
| Ironforge - Thelsamar | 6->8 | 110 |
| Thelsamar - Badlands - Searing Gorge | on foot (unverified) | 0 |
| Thorium Point - Ironforge | 74->6 direct, once discovered (or hearth / Recall) | 830 |
| Ironforge - Menethil | 6->7 direct | 330 |

**Order proposed (cheaper than the starting proposal):** Gadgetzan - Theramore (Tabetha) - boat to Menethil - **fly Menethil - Southshore direct** (the crater first) - Southshore - Ironforge (bind, train, buy silk) - tram - Stormwind - Nethergarde - **hearth to Ironforge** - Thelsamar - Badlands - Searing Gorge on foot - Thorium Point flight point - fly Ironforge (or hearth) - Explorers' League - fly Menethil. Seven flights, 3,390 c raw (2,560 c if the Gorge exit uses the hearth). The starting proposal (Menethil - Ironforge - Stormwind - Nethergarde - Stormwind - Ironforge - Southshore - Ironforge - Thelsamar ... ) needs nine to eleven hops: it flies Ironforge - Southshore - Ironforge for the crater and Nethergarde - Stormwind back. The level-45 parts stay last either way.

Flight masters (npc row [6]): Bera Stonehammer 7823 Tanaris 51.0,29.3; Baldruc 4321 Dustwallow 67.5,51.3; Shellei Brondir 1571 Wetlands 9.5,59.7; Darla Harris 2432 Hillsbrad Foothills 49.3,52.3; Gryth Thurden 1573 Ironforge 55.5,47.7; Dungar Longdrink 352 Stormwind 71.3,72.2; Alexandra Constantine 8609 Blasted Lands 65.5,24.3; Thorgrum Borrelson 1572 Loch Modan 33.9,51.0; **Lanie Reed 2941 Searing Gorge 37.9,30.9 (Gryphon Master; `[P Thorium Point]` is new: no `[P]` for it in chapters 00-41, plan Threads list it as "new in this round, reached on foot").**

**Hearth.** Gadgetzan (chapter 51) until the first Ironforge pass; bind at Innkeeper Firebrew 5111, Ironforge 18.1,51.5 `[S Ironforge]`. Used: Nethergarde -> Ironforge (hearth), and optionally Searing Gorge -> Ironforge at the end (hearth or Astral Recall, whichever is ready). Chapter 53 rebinds at Gadgetzan (plan Threads). Cooldowns on Forever not in the data (Classic 60 min hearth, 15 min Recall; unverified).

**Boat.** Theramore - Menethil: round 1 landed from Menethil on Theramore's east dock (32:27, 71.5,55.5) and left Menethil from the far south-west pier (32:25, 5.6,63.2 Wetlands; "boat or portal unverified"). The return sailing is on the plan's test list.

**Southshore - crater:** on foot, "walk west through the north-west pass into the Dalaran crater" (27:27, `[G18,72 Alterac Mountains]`); not in the data.

**Into the Searing Gorge (settled from the data as far as it goes):**
- Thorium Point's flight point is not known (no `[P Thorium Point]` in 00-41; plan Threads). TaxiPath links Thorium Point only to Ironforge (6) and Morgan's Vigil (71); Morgan's Vigil is not known either. So the way in is on foot.
- The Loch Modan side: the only key in the data is Key to Searing Gorge (item 5396; item row [5] questRewards = [3201] At Last!; tooltip "Binds when picked up, Unique", no use text). 3201 is OUT (chain behind 3181 The Horn of the Beast: Margol the Rager 48 elite, rule 13; `_decisions.tsv`). No gate object for the Stonewrought side is in object.json. Classic knowledge (unverified): the Loch Modan gate opens only with that key, so this way is closed.
- The Badlands side: round 1 rode Thelsamar south into the Badlands (35:18, "the road itself is unverified"). Classic knowledge (unverified): the road into the Gorge leaves the Badlands' west near Kargath and enters the Gorge's east side. Kargath is Horde (npc rows: Kargath Grunt 8155 L55 x5 at Badlands ~3.8,47.4; Warlord Goretooth 60; Gorrik 2861 wind rider master 4.0,44.8): keep clear of it. Badlands mobs on the way 37-45 (round 1 data).
- First steps inside the Gorge are on its east side (Dorius 63.9,61.0, the outhouse 65.6,62.2), then west to Thorium Point: this fits the Badlands entry.

## 4. Route

Level check (first line, rule 14): `[OC]` "|cffffffffLevel check|r  -  this chapter wants level 45: the Thorium Brotherhood board and Hansel's quests (7729, 7723, 7724, 7727, 7722) and the four Explorers' League pickups (2963, 3448, 3450, 3451) cannot be accepted below 45 (quest row [3]); their mobs are 45-49. You arrive at about 44.7. The hand-ins on the way (Tabetha, the crater, Nethergarde) and the Gorge quests that need 40-43 (Dorius, Caught!, Kalaran, Zamael) come first; they should carry you to 45 before Thorium Point. Still 44 at Thorium Point: kill Dark Iron Slavers (45-46) round the Cauldron's north rim until 45 (the Outhouse Key can drop from them), then take the board. Never accept a pickup under its level."

Level path (model: quest XP / 0.65 share, level 44 = 111,800 XP): 44.7 at Gadgetzan; +17,400 quest XP of hand-ins before the Gorge -> about 44.94; +9,210 of the Gorge's level-40-43 quests -> about 45.06; the rest -> 45.6.

`[OC]` intro: "|cffffffffThe eastern trip|r  -  you start at Gadgetzan, hearth = Gadgetzan; it moves to Ironforge here. 19 quests, 61,010 XP, 9g quest money. Bring 15 Silk Cloth (bank or auction house) for the outhouse."

### Leg 1 - Theramore and Tabetha
1. At Bera Stonehammer 7823, fly `[F Theramore]` `[G51.0,29.3 Tanaris]`.
2. `[O]` Gate (rule 11, not counted): only if carrying 6625 Alliance Trauma and First Aid 225: at Doctor Gustaf VanHowzen 12939 `[G67.8,49.0 Dustwallow Marsh]` `[QT6625]` (970 XP) `[QA6624 Triage]` (3,900 XP, req 35; 15 patients with Triage Bandage 16991), do it there, `[QT6624]`.
3. `[O]` Gate: only if carrying 6609 I Got Nothin' Left! and Fishing 225: at Nat Pagle 12919 `[G58.6,60.1 Dustwallow Marsh]` (on the way to Tabetha) `[QT6609]` (970 XP) `[QA6607 Nat Pagle, Angler Extreme]` (3,900 XP at the hand-in: four fish from fishing spots in Feralas 62.8,51.6, Swamp of Sorrows 87.1,61.4, Desolace 28.8,62.1, Stranglethorn 28.5,34.6 - none on this trip). If 6607 is already carried with all four fish: `[QT6607]`.
4. Ride to Tabetha (road not in the data; chapter 50 rode it). At Tabetha 6546 `[QT2846 Tiara of the Deep]` - 6,050 XP + 65s (zone_15 money 6500). Quest L46 req 40; started in chapter 50 (prev Tabetha's Task 2861, row [27]). Reward choice Gemshale Pauldrons 9531 / Dank Shoulderpads 270098, fixed Spellshifter Rod 9527 (gear call below). `[G46.1,57.1 Dustwallow Marsh]`.
5. Ride back to Theramore; take the boat to Menethil from the east dock `[G71.5,55.5 Dustwallow Marsh]` (round 1's landing dock; departure dock and the sailing unverified - plan test list).

### Leg 2 - the Dalaran crater
6. Land at Menethil (south-west pier, 5.6,63.2). At Shellei Brondir 1571 fly `[F Southshore]` `[G9.5,59.7 Wetlands]` (direct link 7->14).
7. `[OC]` "|cffffffffThe Dalaran crater|r  -  on foot from Southshore through the north-west pass, as in chapters 27 and 43 (no flight point)".
8. At Archmage Lan'dalock 20735 (L35, rank 1 in the DB, friendly Kirin Tor) `[QT96770 The Witch Doctor's Head]` - 5,050 XP + 1g 30s (zone_36 money 13000). Quest L46 req 39, Alliance (zone_36 side 1; wowhead_quest_links side Alliance, start = end n20735). No reward items. `[G15.3,73.9 Alterac Mountains]`.
9. Ride back to Southshore; at Darla Harris 2432 fly `[F Ironforge]` `[G49.3,52.3 Hillsbrad Foothills]`.

### Leg 3 - Ironforge (first pass)
10. At Innkeeper Firebrew 5111 bind `[S Ironforge]` `[G18.1,51.5 Ironforge]`.
11. `[A Shaman]` `[O]` At 44, if the level-44 row is still open: Eldrun Stormbreaker 258098 `[T]` `[G47.1,13.8 Ironforge]`. trainer_costs.json (12 Nov, Wowhead raw): Lightning Bolt 8 (10392), Stoneskin Totem 5 (10407), Lesser Healing Wave 4 (10466), Nature Resistance Totem 2 (10600), Rockbiter Weapon 6 (16315), 1g 80s each, 9g the row. Sheet buys: Lesser Healing Wave 4, Lightning Bolt 8 (3g 60s); the rest when gold is easy. The 5% question stays on the test list.
12. `[O]` Gate: Artisan Skinning at Balthus Stoneflayer 6291 (spell 10768, 50,000 c = 5g, Skinning 200), only if not learned (39d:21, 43) `[G39.9,32.5 Ironforge]`.
13. `[O]` Gates for chapter 53's Theramore pass, only if not carried: at First Aid 225, Nissa Firestone 5150 `[QA6625 Alliance Trauma]` (req 35) `[G55.1,58.3 Ironforge]`; at Fishing 225, Grimnur Stonebrand 5161 `[QA6609 I Got Nothin' Left!]` (req 35) `[G48.1,6.9 Ironforge]`.
14. `[OC]` "Silk Cloth: 15 for Caught! - from the bank or the auction house now; the Gorge mobs are not a known source." (AH position not in the data.)
15. Deeprun Tram to Stormwind (Ironforge 76,51 to Stormwind 73.1,49.2, as round 1; not in the data) `[G76,51 Ironforge]`.

### Leg 4 - Nethergarde Keep
16. At Dungar Longdrink 352 fly `[F Nethergarde Keep]` `[G71.3,72.2 Stormwind City]` (direct 2->45, 830).
16b. `[OC]` "Only if the Medallion dropped in Zul'Farrak: if Nekrum's Medallion (2991) was abandoned there, skip steps 17-18 (The Divination 2992 needs it, row [12] = [2991]) and the Nethergarde trip with them - go from Ironforge straight to step 20." (Writer: the whole leg 4 is an "if" on 2991; without it the tram/flight to Nethergarde is not made. Same pattern for 2846 at step 4 and 96770 at step 8: each hand-in fires only if its item dropped.)
17. At Thadius Grimshade 8022 (L50; top of the keep) `[QT2991 Nekrum's Medallion]` - 5,250 XP + 70s (zone_4 money 7000); row [11] pre(any) [2990] (chapter 49) `[QA2992 The Divination]` - 1,050 XP, req 40, pre [2991]; objective "Wait until Grimshade performs the ritual of divination" (row [9] = npc 8022 x3: a scripted event, held with `[QC2992]`) `[G66.9,19.5 Blasted Lands]`.
18. Wait for the ritual; `[QT2992]` (1,050 XP, no money). 2993 Return to the Hinterlands is offered next and is not taken (round 3; see Unsure 1).
19. `|cFFfff8a3Hearth to [H Ironforge]|r` (or Astral Recall) `[G66.9,19.5 Blasted Lands]`. Fallback if neither is ready: Alexandra Constantine 8609 fly `[F Ironforge]` (45->2->6) `[G65.5,24.3 Blasted Lands]`.

### Leg 5 - to the Searing Gorge
20. At Gryth Thurden 1573 fly `[F Thelsamar]` `[G55.5,47.7 Ironforge]`.
21. `[OC]` "|cffffffffThe Badlands road|r  -  south out of Loch Modan into the Badlands (as in chapter 35), then west; the road into the Gorge climbs out of the Badlands' west, north of Kargath (Horde town: stay clear of its level-55 guards). The roads and the pass are not in the data (|cffffcc00unverified|r). The Loch Modan gate needs the Key to Searing Gorge, which this guide does not get."
22. Travel step into the Gorge's east side `[G63.9,61.0 Searing Gorge]` (writer: goto-only).

### Leg 6 - Searing Gorge east (requires 40-43; mobs 43-45)
Mobs here (npc rows): Dark Iron Geologist 5839 L43-44 (8 spawns, x62-69 y32-62); Dark Iron Watchman 8637 L44-45 (5, ~62.7,59.9); Tempered War Golem 5853 L45-47; Glassweb Spider 5856 L43-45 (20, x58-73 y16-75); Dark Iron Kidnapper 15692 L42-45 (10, x67-70 y32-36); Famished Blackworg 269254 L45-47 (217, x42-61 y25-86) and Enraged Stormcrow 222699 L45 (48) are Forever additions. Iodax the Obliterator 222546 L50 (9 spawns at ~66.1,45.4, no rank) stands among the Geologists: avoid. None of the quest mobs is elite.
23. At Dorius Stonetender 8284 (L45) `[QA3367 Suntara Stones]` - 4,400 XP, no money (zone_51), L48 req 40, no prerequisite; objective "Help Dorius get back to Ironforge" (tooltip: "Dorius Escort"); ends at the Singed Letter object 175704 `[G63.9,61.0 Searing Gorge]`. Writer: accept but do not start the walk until Caught! is done (if the escort starts on accept, do Caught! after the letter instead - unverified).
24. Click the Wooden Outhouse 173265 `[QA4449 Caught!]` - 3,900 XP, no money, L45 req 43, no prerequisite; "Kill 8 Dark Iron Geologists and bring 15 pieces of Silk Cloth" (row [7]; row [9] npc 5839 + item 4306) `[G65.6,62.2 Searing Gorge]`.
25. Kill 8 Dark Iron Geologist 5839 (43-44) `[QC4449]` `[G65.5,50.4 Searing Gorge]` (8 spawns only; respawn wait possible).
26. Outhouse: `[QT4449]` (3,900 XP) `[G65.6,62.2 Searing Gorge]`. 4450 Ledger from Tanaris is offered next and is not taken (out, rule 12: Solid Crystal Leg Shaft 19.44%).
27. Escort Dorius north to the Singed Letter `[QC3367]` (escort route, ambush and mob levels not in the data; Classic: he is ambushed and dies, the letter is left - unverified). Dark Iron Kidnappers 42-45 stand on the way at 67-70,32-36 (droppers of the Outhouse Key, see step 37).
28. Click the Singed Letter 175704 `[QT3367]` (4,400 XP) `[QA3368 Suntara Stones]` - 4,400 XP + 1g 40s at Curator Thorius in Ironforge (zone_51 / zone_1537 money 14000), pre [3367]; source item Singed Letter 10443; carried to leg 9 `[G74.5,19.3 Searing Gorge]`.

### Leg 7 - Thorium Point and the two tales (requires 40)
29. Ride west to Thorium Point. At Lanie Reed 2941 get the `[P Thorium Point]` flight point `[G37.9,30.9 Searing Gorge]`.
30. At Zamael Lunthistle 8436 (L50, not elite) `[QA3377 Prayer to Elune]` - 470 XP, no money, L50 req 40; "Hear Zamael tell his tale" (row [9] = npc 8436 x5: a talk event, `[QC3377]`), `[QT3377]` at once `[G29.6,26.3 Searing Gorge]`. **Danger:** he stands inside the Twilight camp - Twilight Fire Guard 5861 (48-49 elite) 0.4, Twilight Idolater 8419 (49-51 elite) 0.4, Twilight Geomancer 5862 (49-50 elite) 0.6, Highlord Mastrogonde 8282 (51, rank 2) 0.2 units from his DB point. Line: "only if you can reach him without a pull; otherwise leave it (470 XP)" - see Deviation 2. 3378 Prayer to Elune is offered next and is not taken (out, rule 13).
31. At Kalaran Windblade 8479 (L55, rank 1, friendly giver) `[QA3441 Divine Retribution]` - 440 XP, no money, L48 req 40; "Listen as Kalaran Windblade tells his story" (row [9] = npc 8479 x5: talk event, `[QC3441]`), `[QT3441]` `[G39.1,39.0 Searing Gorge]`. On the Cauldron's west lip: Slave Workers 45-47 0.6, Dark Iron Slavers 1.1, Taskmasters 1.7, Dark Iron Sentry 8504 (48 elite) 3.4 units. **The Kalaran chain stops here**: the next quest 3442 The Flawless Flame is out (rule 12: Golem Oil 16.5%; drop_rates.json 12 Nov) and everything behind it goes with it (3443, 3452 elite drops, 3453, 3454, 3462, 3463, 3481). Last quest taken: 3441.
   Expected level after steps 23-31: about 45.06.

### Leg 8 - Thorium Point at 45 (requires 45; mobs 45-49)
32. Level gate line: "45 now? If not, kill Dark Iron Slavers 5844 (45-46) on the Cauldron's north rim until you are (`[G42.8,42.8 Searing Gorge]`)".
33. At the Wanted/Missing/Lost & Found board 179827 `[QA7729 JOB OPPORTUNITY: Culling the Competition]` - 4,400 XP + 2g 10s (zone_51 money 21000), L48 req 45, no prerequisite; ends Taskmaster Scrange 14626 `[G37.6,26.5 Searing Gorge]`. (7728 and 7701 on the same board are out: 12.42% drop / elite.)
34. At Hansel Heavyhands 14627 (L53) `[QA7723 Curse These Fat Fingers]` (4,550 XP + 70s, req 45: 20 Heavy War Golems), `[QA7724 Fiery Menace!]` (4,550 XP + 70s, req 45: 20 Greater Lava Spiders), `[QA7727 Incendosaurs? Whateverosaur is More Like It]` (4,550 XP + 70s, req 45: 20 Incendosaurs) `[G38.6,27.8 Searing Gorge]`. Counts from row [7]; no prerequisites.
35. At Master Smith Burninate 14624 (L52) `[QA7722 What the Flux?]` - 4,700 XP + 75s, L50 req 45; "find the Secret Plans: Fiery Flux" (item 18922 from object 179826 only) `[G38.8,28.5 Searing Gorge]`.

### Leg 9 - the Cauldron (kill order lowest first)
36. Kill 15 Dark Iron Slaver 5844 (45-46; 30 spawns x35-58 y24-58) and 15 Dark Iron Taskmaster 5846 (47-48; 31 spawns x34-57 y23-54) round the Cauldron `[QC7729]` `[G42.5,39.8 Searing Gorge]`. Not elite. Dark Iron Sentry 8504 (48 elite, 6 spawns x34-49 y35-62) walks among them: avoid.
37. **The Key to Freedom** (plan: required; see Deviation 1): the Grimesilt Outhouse Key 11818 drops from Dark Iron Steamsmith 5840, Slaver 5844, Taskmaster 5846, Lookout 8566, Kidnapper 15692, Sentry 8504 (item row [1]). No Forever rate in the data (multi-dropper; the nether tooltip carries none); classicdb lists 3% from each (Classic, unverified on Forever): budget ~33 kills; step 36's 30 kills give about a 60% chance. When it drops: right-click it `[QA4451 The Key to Freedom]` (5,250 XP, no money, L47 req 43; start item 11818, row [1]) - hand-in at the Wooden Outhouse, step 42. Writer: `[O]` line "if the key drops"; no abandon needed when it does not (the quest is never in the log).
38. Kill 20 Heavy War Golem 5854 (47-49; 23 spawns x32-51 y38-63, "the areas surrounding the Cauldron") `[QC7723]` `[G40.8,49.2 Searing Gorge]`.
39. Kill 20 Greater Lava Spider 5858 (47-49; 26 spawns x22-43 y33-77, west and south-west plateaus) `[QC7724]` `[G29.5,59.2 Searing Gorge]`.
40. Into the Slag Pit: kill 20 Incendosaur 9318 (47-49; only 13 spawns x43-51 y20-39: expect to wait on respawns) `[QC7727]` `[G48.4,28.0 Searing Gorge]`; loot the Secret Plans: Fiery Flux from object 179826 `[QC7722]` `[G40.5,35.7 Searing Gorge]`. **Danger:** Overseer Maltorius 14621 (50 elite) and a Dark Iron Sentry (48 elite) stand 0.3 units from the plans' DB point; Slave Master Blackheart 8283 (50, rare) 1.9 - see Unsure 3.
41. Thorium Point hand-ins: Taskmaster Scrange 14626 `[QT7729]` (4,400 XP + 2g 10s) `[G39.0,27.5 Searing Gorge]`; Hansel Heavyhands 14627 `[QT7723]` `[QT7724]` `[QT7727]` (3 x 4,550 XP + 70s each; fixed rewards, gear below) `[G38.6,27.8 Searing Gorge]`; Master Smith Burninate 14624 `[QT7722]` (4,700 XP + 75s) `[G38.8,28.5 Searing Gorge]`. Burninate then offers 7736/7737/8241/8242 (level 60): not taken.
42. `[O]` Only with 4451 in the log: ride east to the Wooden Outhouse `[QT4451]` (5,250 XP) `[G65.6,62.2 Searing Gorge]`, then back to Thorium Point (or hearth from there, step 43).
43. At Lanie Reed 2941 fly `[F Ironforge]` `[G37.9,30.9 Searing Gorge]` (74->6, 830) - or hearth / Astral Recall to Ironforge if ready.

### Leg 10 - Ironforge: the Hall of Explorers (requires 45)
44. At Curator Thorius 8256 `[QT3368 Suntara Stones]` (4,400 XP + 1g 40s) `[G71.5,15.7 Ironforge]`. He then offers 3371 Dwarven Justice (L55, round 3): not taken.
45. At High Explorer Magellas 5387 `[QA2963 Portents of Uldum]` - 470 XP, L50 req 45, pre [2439] (39e) `[G69.9,18.6 Ironforge]`. If he does not offer it, 2439 was not done: 2963 and 2946 are gone (chapter 53 loses 2946/2954, chapter 57 2977/2964).
46. At Historian Karnik 2916 `[QT2963]` (470 XP) `[QA2946 Seeing What Happens]` (4,700 XP, req 45, pre [2963]; ends Uldum Pedestal 142343 Tanaris 37.6,81.4 - **counted in chapter 53**) `[QA3448 Passing the Burden]` (510 XP, L52 req 45, no prerequisite) `[G77.5,11.8 Ironforge]`.
47. At Tymor 8507 `[QT3448]` (510 XP) `[QA3449 Arcane Runes]` (2,550 XP, req 45, pre [3448]; four rune rubbings in Azshara, ends Pilot Xiggs Fuselighter 8392 Azshara 77.8,91.4 - **counted in chapter 55**) then `[QA3450 An Easy Pickup]` (510 XP, req 45; row [24] parentQuest = 3449, so take Arcane Runes first) `[G31.0,4.8 Ironforge]`.
48. `[A Shaman]` `[O]` At 46 only: Eldrun Stormbreaker 258098 `[T]` level-46 row `[G47.1,13.8 Ironforge]`: Frost Shock 3 (10472), Mana Spring Totem 3 (10496), Magma Totem 3 (10586), Chain Heal 2 (10622), Windwall Totem 2 (15111), Flametongue Weapon 5, 2g each, 12g the row (trainer_costs.json 12 Nov). Sheet: buy Mana Spring 3 (2g); later Frost Shock 3, Magma 3. Expected: 45.6 here, so this mostly waits for chapter 57 (plan Threads). Also the 44 row here if step 11 did not fire.
49. At Xiggs Fuselighter 8517 `[QT3450]` (510 XP) `[QA3451 Signal for Pickup]` and `[QT3451]` (510 XP; fixed reward Standard Issue Flare Gun 10444, "To be used at the makeshift helipad in Azshara", 2 charges - keep it for chapter 55) `[G70.9,94.6 Ironforge]`. 3483 Signal for Pickup (no XP; a replacement gun) is not taken.
50. `[OC]` Check (section 7).
51. At Gryth Thurden 1573 fly `[F Menethil Harbor]` `[G55.5,47.7 Ironforge]` (6->7, 330). Chapter 53 starts with the Menethil - Theramore boat.

## 5. Gear calls (level-40 band, weights/tooltips/2026-11-12.json, central | conservative)
- **2846 Tiara of the Deep, choice:** Gemshale Pauldrons 9531 (plate shoulder +5 Str +10 Sta +8 Int; 23.5, plate: shaman cannot wear; sells 1g 6s 95c) / Dank Shoulderpads 270098 (leather shoulder +4 Agi +13 Sta; 4.5 | 4.5; sells 77s 75c). Call: **take Gemshale Pauldrons to vendor** (the better sale); Dank Shoulderpads only if the shoulder slot is empty. It is below every shoulder of round 1 (Palm Frond Mantle 26.8, Batwing Mantle 34.0, Inquisitor's Shawl 36.0, Mantle of Doan 44.1) and chapter 47's Failed Flying Experiment (31.2).
- **2846 fixed: Spellshifter Rod 9527** (staff 27.59 dps, +6 Sta +17 Int, +40 spell damage; 495.0 | 455.0; sells 2g 55s 14c). Below Rage of the Storm 280604 (529.8), Bonebiter 6830 (583.5) and Bigger Rock on Bigger Stick 279480 (604.5): vendor.
- **7723 fixed: Slagplate Gauntlets 19126** (plate hands +12 Str +7 Sta; plate): vendor, 44s 51c.
- **7724 fixed: Seared Mail Girdle 19125** (mail waist +12 Agi +7 Sta; 13.4 | 13.4): below Violet Sash 27.2, Twilight Initiate's Belt 29.8 (chapter 43), Deathmage Sash 39.3; vendor 66s 52c (wear only over an empty waist).
- **7727 fixed: Luffa 19141** (trinket, no stats; "Use: Removes 1 Bleed effect. While in or on Water, removes all Bleed, Disease, and Poison effects. (5 Min Cooldown)"): score 0; keep if a trinket slot is empty (utility), else vendor 93s 47c.
- **3451 fixed: Standard Issue Flare Gun 10444**: quest tool for chapter 55.
- No reward on 96770, 2991, 2992, 3367, 3368, 3441, 3377, 4449, 4451, 7729, 7722, 2963, 3448, 3450 (zone itemchoices / itemrewards empty).

## 6. Out (silent; reasons from `_decisions.tsv`)
- 3181 The Horn of the Beast - starts from Margol's Horn, which drops from Margol the Rager (48 elite) - rule 13; Proof of Deed (3182) and At Last! (3201) go with it.
- 3442 The Flawless Flame - drop under 30%: Golem Oil 16.5%.
- 3443 Forging the Shaft - drop under 30%: Thorium Plated Dagger 6.8%.
- 3452, 3453, 3454, 3462, 3463, 3481 - chain behind 3443.
- 3378 Prayer to Elune (second part) - elite outside a dungeon (rule 13): the Twilight drops.
- 4450 Ledger from Tanaris - drop under 30%: Solid Crystal Leg Shaft 19.44%.
- 7728 STOLEN: Smithing Tuyere and Lookout's Spyglass - drop under 30%: Smithing Tuyere 12.42%.
- 7701 WANTED: Overseer Maltorius - elite outside a dungeon (rule 13).
- 7704 Look at the Size of It! - pillow object only in Blackrock Depths: round 3.
- 3372 Release Them, 3566 Rise, Obsidion! - behind Dwarven Justice (level 55) / elite targets (rule 13).
- 93162 Head of the Obliterator, 93163 Heart of the Obliterator - no giver, no side.
- Ironforge: 3371 Dwarven Justice (level 55, round 3), 3483 Signal for Pickup (no XP), 4512/4513 (round 3), 3790, 5090, 3701/3702 (req 47-50, not this round's list).
- 2993 Return to the Hinterlands (Thadius) - round 3 (Unsure 1).

## 7. End check
`[OC]` "|cffffcc00Check:|r handed in here: Tiara of the Deep (2846), The Witch Doctor's Head (96770), Nekrum's Medallion (2991), The Divination (2992), Suntara Stones (3367, 3368), Caught! (4449), Divine Retribution (3441), Prayer to Elune (3377), the board and Hansel (7729, 7723, 7724, 7727), What the Flux? (7722), The Key to Freedom (4451) if the key dropped, Portents of Uldum (2963), Passing the Burden (3448), An Easy Pickup (3450), Signal for Pickup (3451). In the log for later: Seeing What Happens (2946, Uldum, chapter 53), Arcane Runes (3449, Azshara, chapter 55); gates 6625 / 6609 / 6607 if carried; and the Flare Gun in the bags."
- Carried out: 2946 (to 53), 3449 (to 55), optional 6625 / 6609 / 6607 (to 53's Theramore pass). Stands in Menethil (or on the boat); hearth = Ironforge (chapter 53 rebinds Gadgetzan).
- Nothing from chapters 50-51 left open by this chapter.

## 8. Totals
- Required: 19 quests, **61,010 XP**, **9g 00s** (sum of zone_*.json rows: 96770 5,050/1g 30s; 2846 6,050/65s; 2991 5,250/70s; 2992 1,050; 3367 4,400; 3368 4,400/1g 40s; 3441 440; 3377 470; 4449 3,900; 4451 5,250; 7729 4,400/2g 10s; 7723, 7724, 7727 4,550/70s each; 2963 470; 7722 4,700/75s; 3448, 3450, 3451 510 each). Equals the plan row.
- Optional XP counted: 0. Gates (not counted): 6625 970 + 6624 3,900; 6609 970 + 6607 3,900.
- If Deviation 1 is accepted: 18 required, 55,760 XP, 9g 00s (4451 has no money). If Deviation 2 is accepted as well: 17, 55,290.
- Earned on this trip vs picked up: all 19 are handed in here; 2946 and 3449 are picked up here and counted in 53 / 55.
- Spent: flights about 34s (raw, 3,390 c); training 3g 60s (44 buys) or 9g (44 row), plus 2g-12g (46 row if 46); Artisan Skinning 5g if taken; Silk Cloth on the AH (price unknown).

## 9. Unverified / in-game test list
- Theramore - Menethil boat (departure dock); Southshore - crater path; Deeprun Tram (as round 1).
- The Badlands road into the Searing Gorge and where it enters the Gorge; whether the Loch Modan gate is closed without the Key to Searing Gorge.
- Dorius's escort: start trigger, path, ambush, mob levels; whether the Singed Letter appears when he dies.
- Grimesilt Outhouse Key drop rate on Forever (Classic 3%).
- Whether Zamael can be reached without pulling the Twilight elites; whether the Fiery Flux plans can be looted without Overseer Maltorius.
- **Level 54-62 Forever-only NPCs in the Gorge** (no rank in the DB, ids 228718-228970): Firelands Invader 54-55 (67 spawns, centre 40.9,40.3 - on Kalaran and the Cauldron), Infernus Siege Giant 60 (326, x25-62 y32-83), Lieutenant Skarresh 58-60 (67, x39-50 y24-47 - the Slag Pit and Incendosaurs), Duke Searbrand 59-60 (43,28), Firelands Drudge 56-57 (44,27), Flamebringer Stalker 55-56 (33, x33-39 y25-32 - Thorium Point; one point 0.2 units from Hansel), Flamebringer Defender / Elementalist 55-56 (the Twilight camp), Obsidian Reaver 56-60 and Surger 55-57 (south), Lord Gazzran 62 (81, x29-45 y58-75 - the lava spiders' ground), Galenges 62, Duke Tectonis 59-60. If these are live (not an event layer), every level-45 quest area is overrun. Check in game before the chapter is played.
- Iodax the Obliterator (50, 9 spawns among the Geologists); Famished Blackworgs (45-47, 217 spawns) on the east side.
- Trainer price: raw or 5% less.
- Whether Tymor offers An Easy Pickup only with Arcane Runes in the log (row [24]).

## Needs pull
- Wowhead Forever item page 11818 (Grimesilt Outhouse Key: dropped-by count/outof) - settles Deviation 1.
- Wowhead Forever NPC pages for 228718 Firelands Invader, 228722 Infernus Siege Giant, 228747 Flamebringer Stalker, 228721 Lieutenant Skarresh (classification, whether they are an event).
- Wowhead Forever quest page 3367 (escort details, series) and 4451 (start).

## Unsure
1. **2993 Return to the Hinterlands.** The prompt says it is not taken (round 3); the brief's last section lists Return to the Hinterlands under "carried to round 3 (picked up where that costs nothing, never handed in this round; the end Check names them)". The spec follows the prompt; if the main session follows the brief, add `[QA2993 Return to the Hinterlands]` (2,100 XP at Talonaxe, Hinterlands 9.8,44.5, round 3) after step 18 and name it in the Check.
2. **Firelands NPCs** (test list): if live, the Gorge order and the level check do not hold; nothing in the data says whether they are an event.
3. **What the Flux? (7722)**: the plans lie 0.3 units from Overseer Maltorius (50 elite) and a Dark Iron Sentry (48 elite). Rule 13 speaks of kill targets, so the quest stays plain as the plan has it; the line warns. Classic players loot it while Maltorius is pulled away or not looking (unverified).
4. **Silk Cloth**: 15 needed; no source on the route in the data. If he has none and the AH is dear, Caught! (3,900 XP) costs gold.
5. Whether the escort (3367) starts on accept; the order of steps 23-27 assumes it does not.
6. Whether 2439 was done in 39e (level-40-only line); 2963 depends on it.

## 10. Deviations from the route plan
1. **4451 The Key to Freedom fails rule 12 on the Classic number.** It starts from a dropped item (Grimesilt Outhouse Key 11818, item row [1] = six Dark Iron types); a drop-start quest is rated on its item (plan, "How the decisions were made"). Forever rate: not in the data (no drop_rates.json row; nether tooltip has none). classicdb: 3% from each dropper. At 3% the budget is ~33 kills; rule 12 puts an item under 30% out. The route's 30 kills for 7729 give about a 60% chance, so it behaves like the OOX beacons: proposal - write it as a conditional `[O]` "if the key drops" line and take it out of the count (19 -> 18 quests, 61,010 -> 55,760 XP, money unchanged). The spec writes it as an `[O]` "if it drops" step either way (step 37/42), since the quest cannot be in the log without the key. The decision file marked it PLAIN because the script rated only objective items, not start items.
2. **3377 Prayer to Elune (470 XP)**: Zamael stands inside the Twilight camp, 0.2-0.6 units from four elite or rare-elite types (48-51). Not a rule-13 target, so it stays required; proposal: make it `[O]` "only if you can reach him without a pull" and uncounted (-470 XP).
3. **Order**: Menethil - Southshore direct for the crater before Ironforge, and the hearth (bound in Ironforge) from Nethergarde, instead of the plan's Menethil - Ironforge - Stormwind - Nethergarde - ... - Southshore order: about four fewer flights. Same quests, same level gates.
4. **Badlands crossing**: the plan dropped the Badlands trip (answer 11); this chapter rides through the Badlands to reach the Gorge (no quests there). That is travel only.
