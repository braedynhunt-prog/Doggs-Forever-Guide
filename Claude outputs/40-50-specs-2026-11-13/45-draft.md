# Spec: chapter 45 "Stormwind, the Temple door and Booty Bay" (round 2, drafted 13 Nov 2026)

Data used: QuestieDB Forever 1.0.16 (`tooling/qdb`, 12 Nov), Wowhead XP `data/zone_1519.json`, `zone_10.json`, `zone_33.json`, `zone_16591.json` (12 Nov), `data/wowhead_quest_links.json` (11/12 Nov), `data/drop_rates.json`, client tables build 70938 (`TaxiNodes.csv`, `TaxiPath.csv`), quest and item tooltips read today from nether.wowhead.com/forever (1395, 1448, 196, 95295, 95322, 95325, 95326, 95327, 95384, 97332, 1477; items 213127, 277256, 277974, 6091). Every id below was looked up in those files.

**Read Deviation 1 first: as the plan orders the chapters, 1449 To The Hinterlands (chapter 44) cannot be taken. The spec gives the route both ways.**

## 1. Header
- File: `45_StormwindBootyBay.lua`
- Title: `[N 42-44 Stranglethorn Vale]` (the plan's). Next: `[NX 43-44 Tanaris]`
- `[GA Alliance]`
- Description: `[D Forever Shaman 30-60 (Braedyn)\\Stormwind hand-ins from the Riverglades, Brohann's search for the Temple of Atal'Hakkar at the Pool of Tears, the Darkshire supply run to Nethergarde Keep, then Booty Bay: Friz's caravan chain with Caravaneer Ruzzgot, the Venture Co. ledger at Lake Nezferiti and Nesingwary's last raptor hunt. Ends on the boat to Ratchet.]`
- Level: plan predicts 42.8 in, 43.2 out (`route_xp.py`: 24,315 required XP). In order A (Deviation 1) he enters the Stormwind leg at about 42.6 and the Booty Bay leg at about 43.0.
- Level-check line (rule 14): "This chapter wants level 43": the plan's figure, the quest level of In Search of the Temple (1448, L43) and the dragonkin round the Pool of Tears (41-45 in the DB). Highest required level among the pickups is 40 (1477, 1395: quest row [3] = 40); kill targets are Jungle Stalkers 40-41 and, near the ledger, Venture Co. Agents 39. Under 40: Vital Supplies and Supplies for Nethergarde are not offered; play chapter 46's Gadgetzan quests first. (Cannot happen on the route: he enters at 42.6+.)

## 2. Entry state
- Where: plan order: end of chapter 44, Aerie Peak or Ironforge. Order A: end of chapter 43 in Ironforge for the Stormwind leg, end of chapter 44 for the Booty Bay leg.
- Hearth: Farholde Keep (last bind `[S Farholde Keep]` 38_RivergladesI.lua:39; `[H Farholde Keep]` in 39e, 40, 41). Chapters 42-44 are not written; the plan keeps Farholde through 45. Check this against 42-44 when they exist.
- Carried in (from chapter 42): 94894 The Twilight Threat (Kilgar's Head, item 265837 = quest row [10]); 94893 Delivering Closure (Marshal Ryan's Crest, item 266428; only if the Field Marshal's Log chain was done); 95295 I Know a Guy. In order A part 2 he also arrives with chapter 44's quests done and 1452 in the log (see Deviation 1).
- Profession / training: none falls here. No shaman trainer in Stormwind, Darkshire, Nethergarde or Booty Bay (Threads: stops are Ironforge 43/49/57 and Aerie Peak 44/49). No profession gate on this road in the plan's Threads.

## 3. Travel and hearth
Flight links (TaxiPath build 70938): Stormwind (node 2) - Darkshire (12), Stormwind - Nethergarde Keep (45), Darkshire - Nethergarde Keep, Stormwind - Booty Bay (19), Darkshire - Booty Bay, Ironforge (6) - Stormwind, Ironforge - Aerie Peak (43). All known flight points (plan Threads; [P] tags in round 1: Darkshire, Nethergarde 37:50, Booty Bay 30, Stormwind). No Alliance flight point in north Stranglethorn (the only other STV nodes are Horde Grom'gol 20 and the Horde Booty Bay node 18).

Flight masters: Dungar Longdrink 352 Stormwind 71.3,72.2; Felicia Maline 2409 Duskwood 77.5,44.3; Alexandra Constantine 8609 Blasted Lands 65.5,24.3; Gyll 2859 Stranglethorn 27.5,77.8; Gryth Thurden 1573 Ironforge 55.5,47.7; Guthrum Thunderfist 8018 Hinterlands 11.1,46.2. Deeprun Tram: Ironforge 76,51 / Stormwind 73.1,49.2 (as 39d:11/14 write them; not in the data).

The one loop: Stormwind (hand-ins, pickups) -> fly Darkshire (1477 in, 1395 out) -> fly Nethergarde (1395 in) -> ride north into the Swamp past the Fallen Hero, east past Stonard to the Pool of Tears (1448) -> ride back to Nethergarde -> fly Stormwind (1448 in). **He returns to Stormwind once (two visits in all).** Riding back to Nethergarde (about 37 units in the Swamp plus the Blasted Lands' north end) beats Deadwind Pass to Darkshire (the Swamp's west edge alone is ~60 units from the Pool) and keeps the hearth for later. The crate of 1395 lasts 1 hour (item 6091 tooltip: "Duration: 1 hour"), the Darkshire - Nethergarde flight is direct: no hurry.

Booty Bay leg: fly Booty Bay (Stormwind - Booty Bay direct in order B; Aerie Peak - Ironforge - Stormwind - Booty Bay in order A). **Hearth proposal (deviation 4): bind at Innkeeper Skindle 6807, Stranglethorn 27.0,77.3, on arrival**, so the hearth brings him back from Nesingwary's camp instead of a ~66-unit ride. Chapter 46 binds Gadgetzan anyway, so the Farholde bind buys nothing after this chapter. If the hearth is on cooldown, Astral Recall goes to the same place (round 1's wording, 31:62); otherwise ride south on the road (as 30 did).

Out: the Booty Bay - Ratchet boat (TaxiNodes 34 "Transport, Booty Bay - Ratchet"). The pier is not in the data: Classic puts it beside Wharfmaster Lozgil (26.35,73.56), so `[G26.0,73.2 Stranglethorn Vale]` is |cffffcc00unverified|r.

Roads (not in the data, write briefly as unverified): Blasted Lands north to the Swamp past the Fallen Hero of the Horde (round 1 rode it the other way, 37:48-49, Swamp 34.3,66.1); Swamp east past Stonard (Horde, 44-47,51-57 per 37:15) to the Pool; Booty Bay north on the road to Nesingwary (round 1, 30:90).

## 4. Route

### Order B (plan order: chapter 44 already played)

**Leg 1 - Stormwind** (arrive by tram 73.1,49.2 or flight 71.3,72.2)
1. `[OC]` level-check line (section 1) and carried-in line.
2. Turn in **94894 The Twilight Threat** at Highlord Bolvar Fordragon 1748, Stormwind 80.2,38.4 (Stormwind Keep). 4,850 XP, 0 money. Plain (carried). Quest row [2] [[1748]]. No reward choice.
3. Turn in **94893 Delivering Closure** at Abigail Lawson 278088, Stormwind 50.2,51.8 (Cathedral Square). 4,200 XP + 70s. Conditional on chapter 42 (only if he has Marshal Ryan's Crest, 266428); counted as required in the plan. Write it as "if you have it".
4. Accept **1448 In Search of The Temple** at Brohann Caskbelly 5384, Stormwind 69.45,40.4 (Dwarven District, Explorers' League). 3,600 XP at the hand-in. Objective (row [8] trigger, zone 8): "Search for the Temple of Atal'Hakkar", an exploration ring in the Swamp of Sorrows of 8 points: 70.2,45.2 / 66.6,48.1 / 73.6,48.1 / 64.9,53.3 / 75.4,53.3 / 66.6,58.4 / 73.6,58.4 / 70.2,60.5 (centre ~70.2,52.8, the Pool of Tears). No prerequisite ([11]/[12] None). Unlocks 1449 ([21] = 1449). Wowhead types it "Group" (pool flag GROUP, Wowhead type 1); the plan ruled it plain: nothing elite stands inside the ring in the DB (see the danger note in Leg 3). Brohann stands 4 units from the tram: if arriving by tram, do him first.
5. Accept and turn in **1363 Mazen's Behest** at Mazen Mac'Nadir 338, Stormwind 51.8,74.2 -> Acolyte Dellis 5386, Stormwind 51.4,73.8 (half a unit apart). 330 XP, 0 money. "Speak with Acolyte Dellis." No prerequisite. Its follow-up 1364 is out (silent): do not take it from Dellis.
6. Accept **1477 Vital Supplies** at High Sorcerer Andromath 5694, Stormwind 48.7,87.6. 970 XP at Darkshire. "Speak with Watchmaster Sorigal." Row [26] = 1395: it is the breadcrumb for 1395 (1395 row [27] = [1477]); so hand 1477 in **before** accepting 1395.
7. Fly Darkshire at Dungar Longdrink 352, Stormwind 71.3,72.2.

**Leg 2 - Darkshire and Nethergarde**
8. Turn in **1477 Vital Supplies** at Watchmaster Sorigal 5464, Duskwood 75.8,46.2. 970 XP.
9. Accept **1395 Supplies for Nethergarde** at Watchmaster Sorigal 5464, Duskwood 75.8,46.2. 2,900 XP + 50s at the hand-in. Gives the Crate of Power Stones (item 6091, row [10]; "Duration: 1 hour"). The quest itself carries no timer in its tooltip; "before the powerstones expire" means the crate's hour.
10. Fly Nethergarde Keep at Felicia Maline 2409, Duskwood 77.5,44.3 (direct link).
11. Turn in **1395** at Quartermaster Lungertz 5393, Blasted Lands 66.5,21.4. 2,900 XP + 50s. No reward choice.

**Leg 3 - the Pool of Tears**
12. `[OC]` the way: north out of the Blasted Lands past the Fallen Hero of the Horde into the Swamp (Swamp 34.3,66.1), then east, keeping south of Stonard (Horde, 44-47,51-57). Unverified road.
13. `[OC]` |cFFFF0000Danger:|r Mukomonji (npc 262306, level 62, rank 1 = elite in the DB) has one spawn at Swamp 62.4,52.9, 2.5 units west of the ring's west point. Come in from the south. Round the Pool the DB has Wyrmkin Dreamwalkers (42-43), Green Scalebanes (42-43), Green Wyrmkin (41-42), Scalebane Captains (43-44), an Elder Dragonkin (45), Deathstrike Tarantulas (40-41), and Sawfin Frenzies (38-40) in the water. None ranked elite.
14. Explore the Temple of Atal'Hakkar for **1448** `[QC1448]` - goto the ring's south point `[G70.2,60.5 Swamp of Sorrows]` and ride north into the ring until it completes. (Wowhead's tooltip also lists "Razor Hill" as a requirement: an area-name artifact of the page, not a second objective; unverified but the DB has one objective.)
15. Ride back south-west to Nethergarde (`[G65.5,24.3 Blasted Lands]`), fly Stormwind at Alexandra Constantine 8609.

**Leg 4 - Stormwind again**
16. Turn in **1448 In Search of The Temple** at Brohann Caskbelly 5384, Stormwind 69.45,40.4. 3,600 XP, 0 money. In order B 1449 cannot be part of chapter 44 any more (Deviation 1, option B-ii): either take 1449 here and do the Aerie Peak round trip now (B-ii) or leave it for chapter 49 (B-i).
17. Fly Booty Bay at Dungar Longdrink 352.

**Leg 5 - Booty Bay**
18. Bind at Innkeeper Skindle 6807, `[S Booty Bay]`, Stranglethorn 27.0,77.3 (deviation 4).
19. Turn in **95295 I Know a Guy** at Caravaneer Ruzzgot 3945, Stranglethorn 27.4,74.1. 315 XP, 0 money (giver Friz 255897, chapter 42).
20. Accept **95322 Get the Goods** at Ruzzgot 3945. 2,350 XP. Objective (tooltip): "Bloodsail Trunk examined" - "Find the Bloodsail Trunk outside of Booty Bay". QuestieDB has the quest but no objective, no required level and no trunk object (no object named "Bloodsail Trunk" in object.json, case-insensitive); Wowhead series 95295 > 95322 > 95325 (wowhead_quest_links.json). **The trunk's position is a Needs pull.** Hint only: a Forever-only camp of 7 Venture Co. Mercenaries (260425, level 36-37, not elite) stands at 29.7-30.5,70.4-72.7, just outside Booty Bay to the north-east; whether the trunk is there is unverified. Hold the step with `[QC95322]`.
21. Turn in **95322** at Ruzzgot. 2,350 XP. Accept **95325 We've Been Robbed!** (2,350 XP): "Find the Venture Co. Ledger in the Venture Co. Camp near Lake Nezferiti". It **ends at the object** Venture Co. Ledger 630887, Stranglethorn 42.76,18.53 (quest row [2] = [None, [630887]]), so the XP comes at the ledger.
22. Accept the pickup for chapter 49 **97332 Twice Misplaced Trust** at Wharfmaster Lozgil 4631, Stranglethorn 26.35,73.56 (row [1] [[4631]], req 36, L41, 3,300 XP at Wharfmaster Whizzbuzz 259961, Riverglades 79.45,52.71). Gives the Twice Reordered Package (277974, row [10]). DB: no prerequisite ([11]/[12] None). Wowhead's series box lists 97329 > 97328 > 97331 > 97332; round 1 did only 97328 Anything of Value (30:64, 93); 97329 Where's the Key? and 97331 Zimmix's Great Escape (both at Zimmix Sputterspark 268992, 23.46,12.79) were never in the guide. **Unverified that Lozgil offers it**: write "if Lozgil offers it; if not, chapter 49 drops its hand-in". Its own Wowhead page is not in wowhead_quest_links.json (Needs pull).
23. Conditional **95384 Partial Mystical Notes** at Dudd Fizzlescroll 260873, Stranglethorn 28.27,76.35 (Wowhead end n260873; no starter in the DB or on Wowhead). Starts from the item Partial Mystical Notes 213127 (tooltip: "This Item Begins a Quest", requires level 35, BoP, unique), dropped only by Skullsplitter Mystic 780 (item row [1] = [780]; level 39-40, 67 spawns at 42-49,30-42, not on this route), 8.38% (drop_rates.json, single dropper). 3,150 XP + 50s; reward Dudd's Second-Favorite Wand 277256 (a wand: shamans cannot use it; sell 1g 20s 13c). Write it as `[O]` "only if you have the notes in your bags: use them to start the quest and hand in". No kill line (rule 12: under 30%).
24. Ride north on the road to Nesingwary's camp (~66 units, Ghost Wolf/ram).

**Leg 6 - north Stranglethorn**
25. Accept **196 Raptor Mastery** at Hemet Nesingwary 715, Stranglethorn 35.66,10.81. 2,450 XP, 0 money. Objective (row [9]): kill 10 Jungle Stalker 687. Prerequisite 195 ([12] = [195]): done in chapter 30 (30:71 QA195, 30:80 QT195; 194 at 30:28/71). Follow-up 197 (Tethis, 43 elite) is out: silent.
26. East to the Venture Co. camp at Lake Nezferiti: click the Venture Co. Ledger 630887 `[QT95325]` (2,350 XP) at 42.76,18.53. Venture Co. Agents 260429 (level 39, not elite in the DB; Normal on Wowhead per the brief) stand on it: 19 spawns at 42.0-44.8,18.2-23.1; also a Workboss 1095 (36), Lumberjack 921 (34-35), Mechanics 1097 (34-35) and two Shredders 4260 (37) round 43-46,19-23. The ledger also **offers 95326 The Big Payback** (starts at o630887): **out** (rule 12, Ruzzgot's Shipment 29.29% from the Agents) - but see Deviation 3: All's Well That Ends Well may need it.
27. Kill 10 **Jungle Stalker** 687 (level 40-41, not elite, 43 spawns) `[QC196]`. Two groups: 28-35,36-46 (nearest to the camp: 32.6-34.7,36.5-40.2) and 23-28,48-52 on the west. Goto `[G33.0,39.5 Stranglethorn Vale]`. Young Jungle Stalkers 854 (36-37) do not count. Skin them.
28. Turn in **196** at Hemet Nesingwary 715, 35.66,10.81. 2,450 XP. No reward.
29. Hearth to `[H Booty Bay]` (or Astral Recall; or ride south).

**Leg 7 - Booty Bay and the boat**
30. At Caravaneer Ruzzgot 3945: accept **95327 All's Well That Ends Well** for chapter 49 (3,150 XP at Friz Frazzlespark 255897, Riverglades 77.1,52.9; Wowhead start n3945, end n255897; DB row has no prerequisite; its Wowhead series is empty). Whether Ruzzgot offers it without 95326 handed in is **unverified** (Deviation 3). Write: "if Ruzzgot offers All's Well That Ends Well, take it; if not, chapter 49 drops its hand-in".
31. `[OC]` Check line (section 7).
32. Take the boat to Ratchet at the pier beside Lozgil `[G26.0,73.2 Stranglethorn Vale]` (unverified pier).

### Order A (recommended in Deviation 1): Stormwind leg before chapter 44
- **Part 1 (played after chapter 43, which ends in Ironforge):** Deeprun Tram to Stormwind (Ironforge 76,51) - Legs 1-4 exactly as above, except step 16 adds **accept 1449 To The Hinterlands** at Brohann (1,800 XP at Falstad Wildhammer 5635, Hinterlands 11.81,46.76; [12] = [1448]) and step 17 becomes "Deeprun Tram back to Ironforge (Stormwind 73.1,49.2)". Chapter 44 then runs as planned (Thelsamar, Badlands, Aerie Peak with 1449 > 1450 > 1451 > 1452).
- **Part 2 (after chapter 44, from Aerie Peak):** fly Booty Bay at Guthrum Thunderfist 8018 (Hinterlands 11.1,46.2; Aerie Peak - Ironforge - Stormwind - Booty Bay; the game routes it, unverified that it does it in one hop), then Legs 5-7.
- How the main session cuts the file is its call: either part 1 becomes its own chapter between 43 and 44 (a renumber; there is room, e.g. `43b`, as 39-39e was cut), with 45 keeping the Booty Bay legs, or chapter 44 is moved after a Stormwind-only chapter. The step content does not change.

### Order B with 1449 kept (B-ii), for completeness
After step 16: accept 1449 at Brohann, fly Stormwind - Ironforge - Aerie Peak, 1449 at Falstad, 1450 at Gryphon Master Talonaxe 5636 (Hinterlands 9.75,44.47), 1451 and accept 1452 at Rhapsody Shindigger 5634 (26.94,48.59), then Aerie Peak - Ironforge - Stormwind - Booty Bay. That is a second Aerie Peak visit and two long flights, which is what Order A avoids. B-i (leave 1449-1452 to chapter 49) breaks answer 3: 1452's gizzards and livers are collected in chapters 46-47 and need the quest in the log.

## 5. Gear calls
- No kept quest of this chapter has a reward choice or a wearable reward (zone JSON itemchoices / itemrewards empty for 196, 95295, 95322, 95325, 94893, 1363, 1448, 94894, 1395, 1477).
- 95384 (conditional): Dudd's Second-Favorite Wand 277256 (Ranged Wand, 35.67 dps, +5 Int, Requires level 40; tooltip read 13 Nov from nether, not in `weights/tooltips/2026-11-12.json`): shamans cannot use wands - vendor (1g 20s 13c).
- 97332's rings (Refunded / Renegotiated / Apology Ring) are chosen at the chapter-49 hand-in, not here.

## 6. Out (silent; reasons from `_decisions.tsv`)
- 1364 Mazen's Behest (follow-up from Dellis): drop under 30%, Khadgar's Essays 5.0%.
- 543 The Perenolde Tiara: elite outside a dungeon (Grel'borg the Miser, 39 elite); not on the route.
- 212 A Meal Served Cold: drop under 30%, Chilled Basilisk Haunch 3.06%.
- 95326 The Big Payback (offered by the ledger): drop under 30%, Ruzzgot's Shipment 29.29% (see Deviation 3).
- 197 Raptor Mastery: elite outside a dungeon (Tethis, 43 elite).
- 193 Panther Mastery: elite (Bhag'thera 40 elite). 208 Big Game Hunter: elite (King Bangalash 43 elite).
- 189 Bloodscalp Ears 16.7%; 205 Troll Witchery 17.7% and 206 Mai'Zoth behind it; 209 Skullsplitter Tusks 18.3%; 587 Up to Snuff 25.4%; 576 Keep An Eye Out 1.9%; 600 Venture Company Mining 29.6%; 606 Scaring Shaky 25.76% and 607, 609, 613 behind it: drop under 30%.
- 338 The Green Hills of Stranglethorn and 339-342 Chapters I-IV: pages are low zone-wide drops.
- 605 Singing Blue Shards: below the bracket. 621 Zanzil's Secret (30.6%) and 617/623 Akiris by the Bundle (31.3%): XP-only optional (rule 11).
- 97405 Noise Complaints, 8551 The Captain's Chest, 8552/8553/8554 (Mok'rash / Negolash), 630 Message in a Bottle (King Mukla), 619 Enticing Negolash: elite outside a dungeon (rule 13).
- 614, 615, 618, 620: old copies. 1127 Fool's Stout: chain behind out quests. 7810/7908 Arena Master: event / arena. 9272 Dressing the Part, 1423 The Lost Supplies (Swamp): no XP.
- Not out but later: 608, 348, 580, 594, 624-626, 95385 (chapter 51); 3721 (round 3); 3787, 3789, 5066, 5048 (round 3); 95264 Shaw Needs To Know (Stormwind hand-in, its chapter per the plan).

## 7. End check
`[OC]` Check: handed in here: The Twilight Threat (94894), Delivering Closure (94893, if you had it), Mazen's Behest (1363), Vital Supplies (1477), Supplies for Nethergarde (1395), In Search of The Temple (1448), I Know a Guy (95295), Get the Goods (95322), We've Been Robbed! (95325), Raptor Mastery (196), Partial Mystical Notes (95384, if the notes were in your bags). Carried out: All's Well That Ends Well (95327, Friz, chapter 49) and Twice Misplaced Trust (97332, Whizzbuzz, chapter 49), each if it was offered; in order A also To The Hinterlands (1449, chapter 44) from part 1. Plus Friz's other two errands from chapter 42 (Shipping and Handling 95296 for Steamwheedle Port, chapter 46; From Port to Port 95219 for Feathermoon, chapter 47). Hearth: Booty Bay (deviation 4; chapter 46 binds Gadgetzan). You stand on the boat to Ratchet.

## 8. Totals
- Required: 10 quests, **24,315 XP**, **1g 20s** (94893 70s + 1395 50s): 196 2,450; 95295 315; 95322 2,350; 95325 2,350; 94893 4,200; 1363 330; 1448 3,600; 94894 4,850; 1395 2,900; 1477 970. Equals the plan's XP-table row 45.
- Optional / conditional: 95384 3,150 XP + 50s (equals the plan's 3,150).
- Pickups for chapter 49 made here (0 XP here): 95327 3,150; 97332 3,300. In order A, 1449 (1,800, counted in chapter 44).

## 9. Unverified / in-game test list, Needs pull, Unsure
Unverified / test list:
- Bloodsail Trunk position for Get the Goods (95322): not in QuestieDB.
- Whether Ruzzgot offers All's Well That Ends Well (95327) without The Big Payback (95326).
- Whether Lozgil offers Twice Misplaced Trust (97332) after only Anything of Value (97328), without 97329 / 97331.
- Mukomonji (262306, level 62 elite) at Swamp 62.4,52.9 by the Pool of Tears: what it is, whether it is hostile or patrols.
- Where the 1448 exploration completes inside the ring; the road Blasted Lands - Swamp - Pool of Tears; Booty Bay - Ratchet pier position.
- Whether the Aerie Peak - Booty Bay flight is one booking (order A part 2).

Needs pull (Wowhead quest pages, browser; not done here per the brief):
- quest=95322 (the trunk's map pin), quest=97332 (series / prerequisite / starter), quest=95327 (prerequisite: does it follow 95326?), quest=95326 (its map and the Agent's real rank).

Unsure:
- Deviation 1's choice (order A vs B-ii) is the main session's and Braedyn's.
- Deviation 3: whether The Big Payback comes back in if 95327 needs it.
- Delivering Closure is counted required by the plan though it depends on chapter 42's conditional chain; I kept it required with an "if you have it" wording.

## 10. Deviations from the route plan
1. **1449 To The Hinterlands cannot be in chapter 44 as ordered.** Quest row 1449 [12] preQuestSingle = [1448]; [11] = None. 1448 [11] = None, [12] = None, [21] next = 1449. And 1449's giver is Brohann Caskbelly 5384 in **Stormwind** (row [1] [[5384]]), not at Aerie Peak; chapter 44 (Ironforge - Thelsamar - Badlands - Aerie Peak) never passes Stormwind. 1450 [12] = [1449], 1451 [12] = [1450], 1452 [12] = [1451], so the whole Rhapsody chain (and 1452 for chapters 46-47, answer 3) hangs on 1448. Options: **A (recommended)** play this chapter's Stormwind and Swamp legs (1-4) right after chapter 43 in Ironforge, take 1449 at Brohann on the return, then chapter 44, then this chapter's Booty Bay legs (5-7) from Aerie Peak; no extra flights. **B-ii** keep the order and add an Aerie Peak round trip after leg 4 (1449-1452 move from 44 to 45). B-i (push 1449-1452 to chapter 49) breaks answer 3. Chapter 44 is not rewritten here.
2. **Two pickups for chapter 49 are made in this chapter** and are not on the route line: 95327 All's Well That Ends Well (giver Ruzzgot 3945) and 97332 Twice Misplaced Trust (giver Lozgil 4631, Booty Bay). The plan lists both as required in chapter 49 without saying where they are picked up.
3. **All's Well That Ends Well (95327) probably follows The Big Payback (95326), which the plan has out.** The chain in the data: 95325 ends at the ledger object 630887; 95326 starts at that ledger and ends at Ruzzgot; 95327 starts at Ruzzgot. The DB gives 95327 no prerequisite and Wowhead's series box stops at 95325, so the link is not proven. 95326: one Ruzzgot's Shipment at 29.29% from Venture Co. Agent (single dropper; 19 Agents stand around the ledger the route already visits), budget about 4 kills, 3,000 XP. Rule 12 puts it out (under 30%). If Braedyn wants to protect 95327's 3,150 XP: take 95326 at the ledger as `[O]` "drop quest, ~4 kills", hand in at Ruzzgot in leg 7. Not written into the route above; the route as written takes 95327 "if offered".
4. **Hearth**: bind Booty Bay on arrival (the plan's proposal keeps Farholde through 45). Saves a ~66-unit ride back from Nesingwary; chapter 46 binds Gadgetzan, so nothing later uses the Farholde bind before then.
5. Level check: the plan says "wants 43"; the highest required level here is 40 and the mobs are 39-41 (45 at the Pool's edge). Kept the plan's 43 with that explanation.
