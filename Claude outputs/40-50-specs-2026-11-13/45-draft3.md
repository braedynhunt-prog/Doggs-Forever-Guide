# Spec: chapter 45 "Booty Bay" (round 2, second revision of 13 Nov 2026)

Re-cut of `Claude outputs/40-50-specs-2026-11-13/45-draft2.md` to the plan's second revision. Data used (all read 13 Nov 2026): QuestieDB Forever 1.0.16 (`tooling/qdb/{quest,npc,object,item}.json`); Wowhead XP, money, reqlevel and rewards `data/zone_33.json`, `zone_16591.json`, `zone_440.json`, `zone_1176.json`; `data/wowhead_quest_links.json`; `data/browser/r2_pages_2026-11-12.tsv` (NPC 260429); `data/drop_rates.json`; client build 70938 (`TaxiNodes.csv`, `TaxiPath.csv`, `SkillRaceClassInfo.csv`); tooltips `weights/tooltips/2026-11-12.json`; nether.wowhead.com/forever tooltips read 13 Nov from a shell: item 2799, item 3919, quest 348, 349, 95322. Pool: `pool/33_Stranglethorn.txt`, `16591_Riverglades.txt`, `440_Tanaris.txt`, `1176_ZulFarrak.txt`; verdicts `pool/_decisions.tsv`, `overrides_r2.tsv`. Every id below was looked up in those files in the same step. Facts reused from draft2 were re-checked (positions, flight links, trunk search, ledger, Hemet, Stalker spawns, recipe vendor, wand skill row); what changed is listed under Deviations.

## 1. Header
- File: `45_BootyBay.lua`
- Title: `[N 42-43 Stranglethorn Vale]`. Next: `[NX 42-44 Tanaris]` (chapter 46, plan title `[N 42-44 Tanaris]`).
- `[GA Alliance]`
- Description: `[D Forever Shaman 30-60 (Braedyn)\\Booty Bay: Friz's caravan errands for Caravaneer Ruzzgot (the Bloodsail Trunk, the Venture Co. ledger and the stolen shipment), Shaky Phillipe's giblets from the Mistvale gorillas, and Nesingwary's Jungle Stalkers. Pickups for Tanaris, the Hinterlands and the Cape. Ends on the boat to Ratchet.]`
- Level: plan predicts 42.4 in, 42.7 out (`route_xp.py` 13 Nov: 7 required, 16,215 XP).
- Level-check line (rule 14): "This chapter wants level 41: the Elder Mistvale Gorillas and Jungle Stalkers are 40-41 (npc 1557 and 687 rows [3]/[4]); Stoley's Debt and Tran'rek need level 40 to accept. Under 41: take the gorillas from the west edge one at a time and leave the Stalkers to last. Under 40: Stoley's Debt (2872) and Tran'rek (2864) cannot be taken; take them when you hit 40 before the boat (chapter 46 needs both)." Highest required level among the counted quests is 36 (95295 row [3] = 36; 95322/95325/95326/95327 row [3] null, Wowhead 36; 606/607 row [3] = 30; 196 = 28). The plan's "wants 42" is its round floor: Deviation 3.

## 2. Entry state
- Where: Aerie Peak, the Hinterlands, at Guthrum Thunderfist's flight master (end of chapter 44, per the prompt).
- Hearth: Stormwind (chapter 44 binds it; the plan's Threads "Stormwind in 44"; chapter 44 is specced in parallel, the main session confirms the `[S]`).
- Carried in:
  - 95295 I Know a Guy (from Friz Frazzlespark 255897, chapter 42). Required here.
  - Passing through, not touched here: 1452 Rhapsody's Kalimdor Kocktail (chapter 44 -> chapter 48); 95219 From Port to Port (chapter 42 -> chapter 47); 95296 Shipping and Handling only if chapter 41's optional smuggling block was done (-> chapter 46). Any OOX rescue cannot be in the log yet (beacons come in 46-48).
- Training / professions: no shaman trainer in Booty Bay (Threads: Ironforge 43, 48, 49, 52, 57; Aerie Peak 44, 48). No profession gate here in the Threads. Two optional lines (recipe vendor, fishing) kept from draft2: Deviation 4.

## 3. Travel and hearth
- In: TaxiPath build 70938: Aerie Peak (node 43) links to 6 Ironforge, 14, 16, 66, 67; Booty Bay (node 19) links to 2 Stormwind, 4, 12. Route: Aerie Peak - Ironforge - Stormwind - Booty Bay, all known flight points (Booty Bay `[P]` in chapter 30). Step: at Guthrum Thunderfist 8018, Hinterlands 11.07,46.15, `[F Booty Bay]` "(the game routes it through Ironforge and Stormwind)" `[G11.1,46.2 The Hinterlands]`. Arrive at Gyll 2859, Stranglethorn 27.53,77.79. Shorter if the hearthstone is ready: hearth to Stormwind and fly from Dungar Longdrink 352 (`[G71.3,72.2 Stormwind City]`, the round-1 line 39:13) - Unsure 4, written as an `[OC]` note only.
- Bind: Innkeeper Skindle 6807, Stranglethorn 27.04,77.31: `[S Booty Bay]` on arrival (plan Threads "Booty Bay for 45"; Stormwind's bind from chapter 44 ends here; chapter 46 binds Gadgetzan).
- In the zone: Booty Bay to the gorillas is about 11 units north-east (Ruzzgot 27.4,74.1 to the gorilla centre 32.9,64.6); gorillas to Nesingwary's camp about 54 units north on the road (passes Grom'gol, Horde: do not stop). Roads not in the data.
- Back: `[H Booty Bay]` from Nesingwary's camp (Astral Recall the same if the hearth is on cooldown; otherwise the road south).
- Out: the Booty Bay - Ratchet boat (TaxiNodes 34 "Transport, Booty Bay - Ratchet"). Pier not in the data: Grizzlowe 9559 "Shipmaster" at Stranglethorn 26.08,73.35; Grimble 9558 "Shipmaster" at The Barrens 63.54,38.61 (Ratchet). `[G26.1,73.4 Stranglethorn Vale]`, pier and times |cffffcc00unverified|r.

## 4. Route

### Leg 1 - Booty Bay: arrival and pickups
1. `[OC]` level-check line (section 1).
2. `[OC]` Carried in: I Know a Guy (95295) from Friz, chapter 42. No shaman trainer here (next: Ironforge, chapter 48). If your hearth is ready, hearth to Stormwind and fly from Dungar Longdrink instead (one hop shorter) - Unsure 4.
3. At Guthrum Thunderfist 8018, `[F Booty Bay]` (the game routes it) `[G11.1,46.2 The Hinterlands]`.
4. At Innkeeper Skindle 6807, bind `[S Booty Bay]` (Stormwind's bind from chapter 44 ends here; chapter 46 binds Gadgetzan) `[G27.0,77.3 Stranglethorn Vale]`.
5. Accept **606 Scaring Shaky** at "Sea Wolf" MacKinley 2501, Stranglethorn 27.78,77.07 `[G27.8,77.1 Stranglethorn Vale]`. 3,300 XP, 0 money at the hand-in (zone_33). Row [3] req 30, L41; no prerequisite (rows [11]/[12] null). Objective (row [7], [9]): 5 Mistvale Giblets 3919 for "Shaky" Phillipe. Plain (fill). MacKinley's starts (npc row [9]): 606, 609, 613, 2872.
6. Turn in **95295 I Know a Guy** at Caravaneer Ruzzgot 3945, Stranglethorn 27.37,74.08 `[G27.4,74.1 Stranglethorn Vale]`. 315 XP, 0 money (zone_16591 / zone_33). Row [1] Friz 255897, [2] Ruzzgot 3945; req 36, L40. Plain. No reward. Wowhead series 95295 > 95322 > 95325.
7. Accept **95322 Get the Goods** at Ruzzgot 3945 (same spot). 2,350 XP, 0 money at the hand-in. Objective (row [7]; nether tooltip 13 Nov): "Find the Bloodsail Trunk outside of Booty Bay", requirement "Bloodsail Trunk examined". Row [3]/[9]/[11]/[12] null; Wowhead req 36. Ruzzgot's npc row [9] starts [1041, 95322, 95325, 95327], row [10] ends [1040, 95295, 95322, 95326]. Plain.
8. Find the Bloodsail Trunk `[QC95322]`. **Position not in the data** (re-checked 13 Nov: no object named "trunk" or "bloodsail trunk" in object.json case-insensitive; no 95322 row in quest links or page pulls; only Ruzzgot's npc row names the quest). Hints, both |cffffcc00unverified|r: the Bloodsail Correspondence object 2083 at 27.28,69.52 (4.6 units north of Ruzzgot along the coast) and a Forever camp of seven Venture Co. Mercenaries 260425 (36-37, rank none) at 29.7-30.5,70.4-72.7 just north-east of town. Write `[G27.3,69.5 Stranglethorn Vale]` with "the trunk's spot is not in the data: look along the coast north of town (unverified)".
9. Turn in **95322 Get the Goods** at Ruzzgot 3945 `[G27.4,74.1 Stranglethorn Vale]`. 2,350 XP, 0 money. No reward.
10. Accept **95325 We've Been Robbed!** at Ruzzgot 3945. 2,350 XP, 0 money at the hand-in. Objective: "Find the Venture Co. Ledger in the Venture Co. Camp near Lake Nezferiti". Ends at the object Venture Co. Ledger 630887 (row [2] = [null, [630887]]; Wowhead end o630887), 42.76,18.53. Plain.
11. `[O]` Cooking: at Kelsey Yance 2664, `[V]` Recipe: Cooked Glossy Mightfish 13940 (1g 60s = 4 x the 40s sell price, tooltip 2026-11-12; Requires Cooking 225; food +30 AP well fed, eaten from 35) - only if you did not buy it in chapter 31 (31:14, "if gold allows"). Item row [13] vendors = [2664], the only vendor. Kelsey Yance npc row: 28.23,74.34 `[G28.2,74.3 Stranglethorn Vale]`. Deviation 4.

### Leg 2 - the Mistvale gorillas (north-east of Booty Bay)
12. Leave town north and turn east into the valley (about 11 units; roads not in the data).
13. Kill **Elder Mistvale Gorilla** 1557 for 5 **Mistvale Giblets** 3919 `[QC606]` `[TAR1557 Elder Mistvale Gorilla]` `[G33.0,65.5 Stranglethorn Vale]`. Level 40-41, rank none (npc row [3]/[4]/[5]), 28 spawns, centre 32.9,64.6, range x 30.85-34.99, y 57.97-68.43: a west strip at 30.9-32.5,58.0-60.7 and the main group at 31.2-35.0,62.2-68.4 (densest 32-34.5,64.5-67.6). Rate: 25.76% (`drop_rates.json`, nether tooltip, single dropper, 12 Nov; the tooltip reads 26.32% on 13 Nov). Kill line: "Kill [TAR1557 Elder Mistvale Gorilla] for 5 Mistvale Giblets [QC606] (~26% - budget ~19 kills)". Rule 12 would put 26% out; it is in as a fill quest (answer 12, `overrides_r2.tsv`: "fill ... budget about 19 kills"). Keep east of x 35: Silverback Patriarchs 1558 (42-43, nine spawns at 35.2-37.9,60.0-63.9) and the Unbagwa site (Witch Doctor Unbagwa 1449 at 35.27,60.41; Mokk the Savage 1514 lvl 44, Enraged Silverback Gorilla 1511 lvl 41-42 and Konda 1516 lvl 43 listed at the same spot) stand there.
14. `[OC]` **Keep every Gorilla Fang** (item 2799): do not vendor them. Stranglethorn Fever (349, Witch Doctor Unbagwa, under 348 from Fin Fizracket; chapter 49) needs 10 (nether tooltip quest 349: "Gorilla Fang x 10"). The Elder Mistvale Gorillas drop them at about 42.6% (463 of 1,086 kills, `drop_rates.json` per-mob row, 11 Nov); the fang is not a quest item (nether tooltip 2799: no "Quest Item" line, sells for 67c, stacks to 20), so it drops without the quest. The ~19 giblet kills should leave about 8 fangs; the rest come in chapter 49. (Whether to kill on to 10 here: Unsure 1.)

### Leg 3 - north Stranglethorn
15. Ride north on the road to Nesingwary's camp (about 54 units from the gorillas; Ghost Wolf `[A Shaman]`). You pass the Jungle Stalkers on the way: they do not count until Hemet gives the quest.
16. Accept **196 Raptor Mastery** at Hemet Nesingwary 715, Stranglethorn 35.66,10.81 `[G35.7,10.8 Stranglethorn Vale]`. 2,450 XP, 0 money at the hand-in. Objective (row [9]): kill 10 Jungle Stalker 687. Req 28, L41. Prerequisite row [12] = [195], handed in at 30:80. Next in chain 197 (Tethis, elite): out, silent. Plain.
17. East to Lake Nezferiti: click the **Venture Co. Ledger** 630887 and turn in **95325 We've Been Robbed!** `[QT95325]` `[G42.8,18.5 Stranglethorn Vale]` (10.5 units from Hemet). 2,350 XP, 0 money. No reward.
18. Accept **95326 The Big Payback** from the same ledger `[QA95326]` `[G42.8,18.5 Stranglethorn Vale]`. 3,000 XP, 0 money at the hand-in (zone_16591). Row [1] = [null, [630887]] (object start), row [2] Ruzzgot 3945; row [3] null, Wowhead req 36, L39; Wowhead series empty. Objective (row [7]): "Kill the Venture Co. Agent and take back Ruzzgot's Shipment"; item 268810 Ruzzgot's Shipment x1 (row [9]).
19. Kill **Venture Co. Agent** 260429 for **Ruzzgot's Shipment** 268810 `[QC95326]` `[TAR260429 Venture Co. Agent]` `[G43.5,20.1 Stranglethorn Vale]`. Level 39, rank none (npc row; Wowhead page: Level 39, no Elite line, hostile to both factions), 19 spawns in the DB, centre 43.5,20.1, range x 42.03-44.84, y 18.20-23.12 (Wowhead's map shows four, 43.3-43.6,20.2-21.6). Rate 29.29% (`drop_rates.json`, single dropper, 12 Nov). Kill line: "Kill [TAR260429 Venture Co. Agent] for Ruzzgot's Shipment [QC95326] (~29% - budget ~4 kills)". Fill (answer 12; `overrides_r2.tsv`). Also in the camp: Venture Co. Workboss 1095 (36) 43.11,19.01, Lumberjack 921 (34-35), Mechanics 1097 (34-35), Shredders 4260 (37) at 46.43,19.87 and 43.9,23.17.
20. South-west to the Jungle Stalkers: kill 10 **Jungle Stalker** 687 `[QC196]` `[TAR687 Jungle Stalker]` `[G31.0,42.5 Stranglethorn Vale]`. Level 40-41, rank none, 43 spawns: an eastern band 27.3-34.7,36.5-47.2 (nearest the camp 32.6-34.7,36.5-40.2, about 21 units from the Agents) and a western group 23.0-27.8,48.1-51.5. Young Jungle Stalkers 854 (36-37, four spawns 30.7-32.1,42.5-44.7) do not count. `[OC]` Skin them.
21. Turn in **196 Raptor Mastery** at Hemet Nesingwary 715 `[G35.7,10.8 Stranglethorn Vale]` (32 units north). 2,450 XP, 0 money. No reward.
    Order note: Hemet - ledger/Agents - Stalkers - Hemet is about 64 units of riding; Hemet - Stalkers - Hemet - ledger about 75; Hemet - Stalkers - ledger - Hemet about 69.
22. Hearth to `[H Booty Bay]` (Astral Recall the same; otherwise the road south).

### Leg 4 - Booty Bay: hand-ins, pickups for later, the boat
23. Turn in **606 Scaring Shaky** at "Shaky" Phillipe 2502, Stranglethorn 26.90,73.59 `[G26.9,73.6 Stranglethorn Vale]` (3.7 units from the inn). 3,300 XP, 0 money. No reward.
24. Accept **607 Return to MacKinley** at Shaky 2502. Row [12] = [606]; req 30, L41; gives Shaky's Payment 3922 (row [10]). Plain.
25. Turn in **607 Return to MacKinley** at "Sea Wolf" MacKinley 2501 `[G27.8,77.1 Stranglethorn Vale]`. 2,450 XP + **40s** (zone_33 money 4000). No item reward.
26. Accept **2872 Stoley's Debt** at MacKinley 2501. Req 40 (row [3]; Wowhead 40), L45; no prerequisite. Ends at Stoley 7881, Tanaris 67.1,24.0 (Steamwheedle Port), chapter 46 (390 XP there). Predicted level here 42.6, above 40. Plain pickup.
27. `[O]` Conditional: accept **609 Voodoo Dues** at MacKinley 2501 if you mean to try the three ogres in chapter 49. Row [12] = [607]; req 30, L44; 3,750 XP + 65s, counted nowhere (plan: conditional, "taken in chapter 45, tried in chapter 49, abandoned if a piece is missing"). Items: Maury's Clubbed Foot 3924 (Maury "Club Foot" Wilkins 2535, 43-44, 35.3,51.3) 70.4%, Jon-Jon's Golden Spyglass 3925 (Jon-Jon the Crow 2536, 34.9,51.8) 58.9%, Chucky's Huge Ring 3926 (Chucky "Ten Thumbs" 2537, 40.0,58.2) 59.4%. Chapter 49 holds the `[QS]` if a piece is missing (rule 9). Its follow-up 613 (elite, Maury's Key 4.2%) is out.
28. Accept **2864 Tran'rek** at Krazek 773, Stranglethorn 26.95,77.21 `[G26.9,77.2 Stranglethorn Vale]` (beside the inn). Req 40, L45; no prerequisite; ends at Tran'rek 7876, Tanaris 51.6,26.8 (Gadgetzan), chapter 46 (390 XP there). Krazek's npc row [9] includes 2864. Plain pickup. Follow-up 2865 Scarab Shells is chapter 51's.
29. `[O]` Conditional: **95384 Partial Mystical Notes** - only if item 213127 is in your bags: use it `[UI213127]`, turn in at Dudd Fizzlescroll 260873, Stranglethorn 28.27,76.35 `[QT95384]` `[G28.3,76.4 Stranglethorn Vale]`. 3,150 XP + 50s (zone_33). Row [1] null, [2] [[260873]], req 32, L40. Item drops only from Skullsplitter Mystic 780 (39-40, 42-49,30-42, not on this route) at 8.38%. Counted as this chapter's optional 3,150. Reward: Dudd's Second-Favorite Wand (section 5).
30. Turn in **95326 The Big Payback** at Caravaneer Ruzzgot 3945 `[G27.4,74.1 Stranglethorn Vale]`. 3,000 XP, 0 money. No reward.
31. Accept **95327 All's Well That Ends Well** at Ruzzgot 3945 (required pickup; counted in chapter 48). Row [1] [[3945]], [2] [[255897]] Friz Frazzlespark, Riverglades 77.1,52.9; row [3] null, Wowhead req 36, L40; 3,150 XP at the chapter-48 hand-in. No prerequisite in the DB, Wowhead series empty: the offer after The Big Payback is |cffffcc00unverified|r (test list). Write it plain, with an `[OC]` "if Ruzzgot does not offer it, note it: chapter 48 counts it".
32. `[O]` Conditional: accept **97332 Twice Misplaced Trust** at Wharfmaster Lozgil 4631, Stranglethorn 26.35,73.56, "if Lozgil offers it" `[G26.4,73.6 Stranglethorn Vale]`. Req 36, L41; ends at Wharfmaster Whizzbuzz 259961, Riverglades 79.5,52.7 (chapter 48, optional 3,300 XP there); gives the Twice Reordered Package 277974. Wowhead series 97329 > 97328 > 97331 > 97332; 97331 is out. Not counted here.
33. `[O]` Fishing: fish the harbour toward 225 while you wait for the boat `[SK Fishing 225]` `[G26.1,73.4 Stranglethorn Vale]` (Artisan Fishing gate, Threads: Theramore passes). Deviation 4.
34. `[OC]` Check line (section 7).
35. Take the boat to Ratchet from the pier by Grizzlowe 9559 `[G26.1,73.4 Stranglethorn Vale]` (pier and times |cffffcc00unverified|r). It lands by Grimble 9558, The Barrens 63.54,38.61, where chapter 46 starts.

Leg distances inside town: inn 27.0,77.3 -> Shaky 3.7 -> MacKinley 3.6 -> Krazek 0.9 -> Dudd 1.4 -> Ruzzgot 2.3 -> Lozgil 1.1 -> pier 0.3.

## 5. Gear calls
- Required quests: no reward choice and no item reward (zone_33 / zone_16591 itemchoices and itemrewards empty for 196, 606, 607, 95295, 95322, 95325, 95326; also 95327, 2872, 2864, 609).
- 95384 (conditional): Dudd's Second-Favorite Wand 277256 (Wand, 35.67 dps, +5 Int, +1 mp5, req 40, sell 1g 20s 13c; tooltip 2026-11-12). Shamans cannot use wands: SkillRaceClassInfo row 144 (skill 228) ClassMask 400, no shaman bit 64. Vendor it.
- 97332 (conditional, chosen at the chapter-48 hand-in): Apology Ring 278019 (+6 Sta, +4 spell damage; tooltip 2026-11-12) 8.0 central / 4.0 conservative over Renegotiated Ring 278018 (+3 Str +6 Sta) 6.0 / 6.0; Refunded Ring 278017 (+8 Sta) 0. Hand computation with the `score_items.py --band 40` header (str 2.00, sp 2.00 / 1.00, sta 0); the chapter-48 spec makes the call.
- Note for chapter 49: Medicine Blanket 4113 (348; +4 Sta +9 Spi back, tooltip) is the plan's 22.5 back score.

## 6. Out (silent; reasons from `_decisions.tsv`)
- 197 Raptor Mastery (Tethis, elite), 193 Panther Mastery (Bhag'thera, elite), 208 Big Game Hunter: elite outside a dungeon (rule 13).
- 613 Cracking Maury's Foot: elite, Maury's Key 4.2% (plan, 13 Nov).
- 78823 / 78830 Terror of the Desert Skies: Badlands, dropped (answer 11).
- 189 Bloodscalp Ears, 205 Troll Witchery (206 behind), 209 Skullsplitter Tusks, 587 Up to Snuff, 576 Keep An Eye Out: drop under 30% (rule 12).
- 600 Venture Company Mining, 621 Zanzil's Secret, 617 Akiris by the Bundle (623 behind): budget is a farm (plan, fill test: 34 / 39 / 32 kills).
- 338-342 Green Hills pages; 97405, 8551-8554, 630, 619: elite outside a dungeon; 614, 615, 618, 620 old copies; 1127; 7810 / 7908; 9272; 605.
- Not picked up here: 580 Whiskey Slim's Lost Grog (round 3, plan), 624 Cortello's Riddle (picked up on the Bloodsail ship in chapter 49), 3721 (round 3), 608 (chapter 49, Fleet Master Seahorn 2487 at 27.17,77.01, behind 604), 348 (chapter 49; Unsure 2).

## 7. End check
`[OC]` Check: handed in here: I Know a Guy (95295), Get the Goods (95322), We've Been Robbed! (95325, at the ledger), The Big Payback (95326), Raptor Mastery (196), Scaring Shaky (606), Return to MacKinley (607); Partial Mystical Notes (95384) only if the notes dropped. In the log for later: All's Well That Ends Well (95327, Friz, chapter 48), Stoley's Debt (2872, Stoley, chapter 46), Tran'rek (2864, Gadgetzan, chapter 46), Voodoo Dues (609, chapter 49) if taken, Twice Misplaced Trust (97332, chapter 48) if offered; still carried: Rhapsody's Kalimdor Kocktail (1452), From Port to Port (95219), Shipping and Handling (95296) if you have it. Bags: every Gorilla Fang (about 8; chapter 49 needs 10). Hearth: Booty Bay.

Carried out: 95327, 2872, 2864 (plain); 609, 97332 (conditional); 1452, 95219, 95296 (through); item 2799 x ~8. Bind: Booty Bay.

## 8. Totals
- Required: **7 quests, 16,215 XP, 40s**: 196 2,450; 606 3,300; 607 2,450 (+40s); 95326 3,000; 95295 315; 95322 2,350; 95325 2,350. Equals the plan's XP-table row 45 (7 / 16,215 / 40s).
- Optional / conditional counted here: 95384 3,150 XP + 50s. Equals the plan's 3,150.
- Picked up here, counted later (0 XP here): 95327 3,150 (ch 48, required); 2872 390 and 2864 390 (ch 46, required); 609 3,750 + 65s (ch 49, conditional); 97332 3,300 (ch 48, conditional).

## 9. Unverified / in-game test list, Needs pull, Unsure
Unverified / test list:
- The Bloodsail Trunk's position (95322) and whether `[QC95322]` completes on "Bloodsail Trunk examined".
- Whether Ruzzgot offers All's Well That Ends Well (95327) after The Big Payback (plan test list).
- Whether Lozgil offers Twice Misplaced Trust (97332).
- Venture Co. Agent count: 19 spawns in QuestieDB, four on Wowhead's map; if only four stand, a 4-kill budget may wait on respawns.
- The Booty Bay pier and boat times; the road from Booty Bay into the gorilla valley.
- Whether Mokk, Konda and the Enraged Silverback stand at Unbagwa's spot (the DB lists a spawn for each) or are summoned.

Needs pull:
- quest=95322 Get the Goods: the Bloodsail Trunk's map pin and object id.
- Optional: quest=95327 page for a prerequisite on The Big Payback.

Unsure:
1. Fangs: 19 giblet kills leave about 8 of 10 fangs (19 x 42.6% = 8.1; 10 fangs need about 23-24 kills). Killing four or five more gorillas here would finish them; I wrote "keep them", not extra kills, because the plan budgets 19. Chapter 49 passes Unbagwa (Voodoo Dues ogres at 35-40,51-58) either way.
2. Accepting 348 Stranglethorn Fever here: Fin Fizracket 2486 stands in Booty Bay at 27.61,76.74 (row [1] [[2486]]), req 40 (row [3]; predicted 42.4 on entry), no prerequisite. Accepting it on arrival costs one log slot and no travel. Useful only if he also does the summon here: Unbagwa (349, child quest, row [25] = 348) stands at 35.27,60.41, 4.8 units from the gorilla centre, and Mokk is level 44 (plus Konda 43 and the Enraged Silverback 41-42 at the spot) against 42.5 - that would move 5,850 XP and the Medicine Blanket from chapter 49 into 45 and needs 10 fangs. Not added; the main session and the chapter-49 spec decide.
3. Level check 41 (data) against the plan's 42: Deviation 3.
4. Entry: hearth to Stormwind and fly from there is shorter than Aerie Peak - Ironforge - Stormwind - Booty Bay, if chapter 44 leaves the hearth ready; chapter 44 is specced in parallel. Written as an `[OC]` note only, the `[F]` from Aerie Peak is the step.
5. Seen in passing (not this chapter): `route_xp.py` today prints "with required levels enforced: ends at 47.1; 27 quests (117,370 XP)" while the plan text says 48.0 with eleven Un'Goro quests closed.

## 10. Deviations from the route plan
1. **"South of Booty Bay" is north-east.** The plan and `overrides_r2.tsv` put the Elder Mistvale Gorillas south of Booty Bay; their 28 spawns are at 30.9-35.0,58.0-68.4 (npc 1557 row [6]), north-east of Booty Bay (y 74-78). Wording only.
2. **The Bloodsail Trunk has no position**; the step carries a hint `[G]` marked unverified.
3. **Level check 41 instead of 42** (mobs 40-41; pickups req 40). Entry is predicted at 42.4, so either works; the main session may keep 42.
4. **Two optional lines the plan does not list** (no XP effect), kept from draft2: the Recipe: Cooked Glossy Mightfish vendor line (food thread, only if not bought in chapter 31) and a "fish toward 225" line by the pier. Drop either if preferred.
5. **Order against "lowest mobs first"**: the gorillas (40-41) come before the Venture Co. Agents (39) because they lie on the way north and Hemet's quest must be taken before the Stalkers; at 42.4 he is above all three groups.
6. **Venture Co. Agent centre**: the prompt gives 42.0,21.5 (the DB's first spawn); the 19-spawn centre is 43.5,20.1.
