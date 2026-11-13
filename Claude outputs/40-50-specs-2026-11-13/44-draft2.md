# Spec: chapter 44 "Stormwind, the Temple door and Aerie Peak" (round 2, re-cut 13 Nov 2026)

Data used (all read 13 Nov): QuestieDB Forever 1.0.16 (`tooling/qdb/quest.json`, `npc.json`; via `qinfo.py`, `loc.py` and a row dump), Wowhead XP and money `data/zone_1519.json`, `zone_10.json`, `zone_4.json`, `zone_47.json`, `zone_16591.json` (12 Nov pulls), `data/wowhead_quest_links.json`, `tooling/trainer_costs.json` (12 Nov), client build 70938 `TaxiNodes.csv` / `TaxiPath.csv`, pool files `1519_Stormwind`, `10_Duskwood`, `4_BlastedLands`, `8_SwampofSorrows`, `47_Hinterlands`, `_decisions.tsv`, `overrides_r2.tsv`, the guide's `[P]` / `[S]` / `[H]` tags (chapters 00-41), nether tooltips item/6091 and quest/1448 (shell, 13 Nov). Every id below was looked up in those files. Facts reused from `45-draft.md` / `44-draft.md` were re-checked; the Badlands legs of the old 44 draft are not used.

No quest of this chapter has a kill or a drop objective; nothing in it fails rule 12 or 13.

## 1. Header
- File: `44_StormwindAeriePeak.lua`
- Title: `[N 42-43 Stormwind and Aerie Peak]`
- Next: `[NX 42-43 Stranglethorn Vale]` (chapter 45 "Booty Bay" as the plan titles its file).
- `[GA Alliance]`
- Description: `[D Forever Shaman 30-60 (Braedyn)\\Stormwind and the search for the Temple of Atal'Hakkar: Brohann Caskbelly sends you to the Pool of Tears in the Swamp of Sorrows, Andromath's supplies go by Darkshire to Nethergarde Keep on the way; then Aerie Peak for Falstad, Gryphon Master Talonaxe and Rhapsody Shindigger, whose Kalimdor Kocktail rides with you to Tanaris and Feralas.]`
- Level: plan XP table 42.2 in, 42.4 out (12,290 required XP).

## 2. Entry state
- Where: Ironforge, end of chapter 43 (Dalaran crater hand-in done, per the prompt; chapter 43 is specced in parallel).
- Hearth: Farholde Keep. Last bind `[S Farholde Keep]` 38_RivergladesI.lua:39; every later hearth tag is Farholde Keep (38:117, 39e:65, 40:50, 41:79). Assumed unchanged by chapters 42-43 (the prompt says so).
- Flight points known (the `[P]` tags): Stormwind (00b:67, 05:14), Darkshire (14:21), Nethergarde Keep (37:50), Aerie Peak (29:67); Ironforge is the Dwarf's home city and the chapters fly from it. All five this chapter uses are known: no flight point is discovered here.
- Quests carried in that this chapter touches (conditional, only if chapter 42 gave them): 94894 The Twilight Threat (holds Kilgar's Head 265837, quest row [10]); 94893 Delivering Closure (holds Marshal Ryan's Crest 266428, row [10]; 40:52 tells him to leave it "for the 40-50 guide's first Stormwind visit", which is this chapter).
- Carried through untouched (from chapters 42-43, assumed, for the main session to reconcile): Friz's errands 95295 I Know a Guy (chapter 45), 95219 From Port to Port (chapter 47), 95296 Shipping and Handling if taken (chapter 46).
- Training: the level 42 row is bought in Ironforge at the start of chapter 43 (plan Threads). Here only a repeat `[O]` at Farseer Maret Firetend in Aerie Peak if that stop was skipped. The level 44 row is chapter 48's.
- Professions: Artisan Leatherworking at Drakk Stonehand, Aerie Peak (plan Threads: chapter 44 or 48), `[O]` at skill 200. Artisan Skinning (Balthus, Ironforge) is not on this chapter's path (39d:21 and chapter 43's Ironforge stop carry it).

## 3. Travel and hearth
Flight masters (npc.json): Dungar Longdrink 352, Stormwind 71.3,72.2; Felicia Maline 2409, Duskwood 77.5,44.3; Alexandra Constantine 8609, Blasted Lands 65.5,24.3; Gryth Thurden 1573, Ironforge 55.5,47.7; Guthrum Thunderfist 8018, Hinterlands 11.1,46.1 (round 1 writes 11.1,46.2 at 29:67).

Links (TaxiPath build 70938, node ids from TaxiNodes: Stormwind 2, Ironforge 6, Darkshire 12, Aerie Peak 43, Nethergarde Keep 45; cost field in copper, the price shown in game unverified): 2->12 330 (3s 30c); 12->45 830 (8s 30c); 45->2 830; 2->6 50; 6->43 730. No direct Stormwind - Aerie Peak link: the game routes Stormwind - Ironforge - Aerie Peak.

Deeprun Tram: Ironforge 76,51 (02:73, 04:66) to Stormwind 73.1,49.2 (00b:152, 05:6); not in the data, as round 1 writes it.

Loop (the plan's order, checked): Ironforge -tram- Stormwind (pickups, conditional hand-ins) -fly- Darkshire (1477 in, 1395 out) -fly- Nethergarde Keep (1395 in) -ride- Swamp of Sorrows, the Pool of Tears (1448) - back to Stormwind (1448 in, 1449 out) -fly- Aerie Peak (1449-1451, 1452 out). Ends at Guthrum Thunderfist for chapter 45's flight to Booty Bay.

**Hearth: bind in Stormwind (recommended, Deviation 1).** The Farholde bind does nothing for chapters 44-45 (the plan rebinds at Booty Bay on arrival in 45). Bound at Innkeeper Allison 6740, Stormwind 60.4,75.3 (between Mazen and the flight master on leg 1), he hearths (or casts Astral Recall, which goes to the same place) from the Pool of Tears straight to Stormwind. That replaces the ride back from the Pool to Nethergarde (about 37 units west across the Swamp to the Fallen Hero at 34.3,66.1, then the pass and the Blasted Lands' north end) and the 8s 30c Nethergarde - Stormwind flight. Chapter 43 used the hearth for the Krol'dok run: if the hearth is on cooldown, Astral Recall; if both are, take the plan's way (ride back to Nethergarde, fly Stormwind). Both ways are written in leg 3.

Roads (not in the data; marked unverified in the Lua): Nethergarde Keep north through the pass to the Swamp past the Fallen Hero of the Horde (round 1 rode it the other way, 37:48-49, "Classic knowledge, unverified"); Swamp east, south of Stonard, to the Pool; Aerie Peak east to Rhapsody on foot (about 15 units).

## 4. Route

### Level check (first line)
`[OC]Level check - this chapter wants level 42`: the highest required level of its pickups is 40 (Vital Supplies 1477 and Supplies for Nethergarde 1395, quest row [3] = 40); the 42 is the ground: dragonkin round the Pool of Tears 41-45 and the Hinterlands mobs on the walk to Rhapsody 41-44 (section below). Nothing in this chapter has to be killed. Under 42: ride round the packs, come into the Pool's ring from the south, and on the Hinterlands walk keep to the road. Under 40 (cannot happen on the route, entry 42.2): Andromath and Sorigal do not offer 1477 / 1395; leave them for chapter 50's Stormwind - Nethergarde trip.

### Leg 1 - Stormwind (from the tram)
1. `[OC]` heading + carried-in line (section 2) + hearth note (bind here, section 3).
2. Accept **1448 In Search of The Temple** at Brohann Caskbelly 5384 (L40), Stormwind 69.5,40.4 (Dwarven District, 4 units from the tram exit). 3,600 XP, 0 money at the hand-in (zone_1519). Quest L43, req 38. Prerequisite none (rows [11], [12] empty). Row [21] next = 1449. Objective (row [8]): "Search for the Temple of Atal'Hakkar", an exploration area in the Swamp of Sorrows (zone 8) given as 8 points 70.2,45.2 / 66.6,48.1 / 73.6,48.1 / 64.9,53.3 / 75.4,53.3 / 66.6,58.4 / 73.6,58.4 / 70.2,60.5 (centre about 70.2,52.8, the Pool of Tears). Wowhead type 1 (Group) in zone_1519; pool flag GROUP; `_decisions.tsv` PLAIN (nothing elite inside the ring in the DB; Mukomonji stands outside it, leg 3). Label: plain.
3. Conditional: at Highlord Bolvar Fordragon 1748, Stormwind 80.2,38.4 (Stormwind Keep), `[QT94894 The Twilight Threat]` - 4,850 XP, 0 money. `[O]` "only if you carry The Twilight Threat" (it holds Kilgar's Head). Ender from quest row [2] [[1748]] and Wowhead end n1748. No reward.
4. Conditional: at Abigail Lawson 278088, Stormwind 50.2,51.8 (Cathedral Square), `[QT94893 Delivering Closure]` - 4,200 XP + 70s (zone_1519 money 7000). `[O]` "only if you carry Delivering Closure" (Marshal Ryan's Crest; Demar Brant offered it after Dying Wish 94892, chapter 40:52 or chapter 42). Ender row [2] [[278088]], Wowhead end n278088; series 94885 > 94887 > 94892 > 94893. No reward.
5. Accept **1363 Mazen's Behest** at Mazen Mac'Nadir 338 (L44), Stormwind 51.8,74.2, and turn it in at Acolyte Dellis 5386 (L15), Stormwind 51.4,73.8 (half a unit away). 330 XP, 0 money. L41, req 37. Prerequisite none. Objective: "Speak with Acolyte Dellis in Stormwind." Its follow-up 1364 (Dellis) is out (Khadgar's Essays 5.0%): no tag, silent. Can be one line: `[QA1363 Mazen's Behest]` at Mazen then `[QT1363]` at Dellis as two steps (two NPCs).
6. Bind: at Innkeeper Allison 6740, Stormwind 60.4,75.3, `[S Stormwind]` (Deviation 1). If Braedyn rejects the rebind, drop this line and use leg 3's "without the bind" lines.
7. Accept **1477 Vital Supplies** at High Sorcerer Andromath 5694 (L62), Stormwind 48.7,87.6 (Mage Quarter; round 1 used him at 15:78 and 30:13). 970 XP, 0 money at Darkshire. L45, req 40. Prerequisite none. Objective: "Speak with Watchmaster Sorigal." Row [26] = 1395 and 1395's row [27] = [1477]: 1477 is the breadcrumb of 1395, so 1477 is handed in **before** 1395 is accepted (a breadcrumb is closed once its target is taken).
   Order on the ground: tram 73.1,49.2 -> Brohann 69.5,40.4 -> Bolvar 80.2,38.4 (if held) -> Cathedral Square 50.2,51.8 (if held) -> Mage Quarter 48.7,87.6 -> Mazen / Dellis 51.8,74.2 -> Allison 60.4,75.3 -> Dungar 71.3,72.2. (Andromath before Mazen keeps it one sweep south and back east; the writer may swap 5 and 7.)
8. Fly: at Dungar Longdrink 352, Stormwind 71.3,72.2, fly `[F Darkshire]`.

### Leg 2 - Darkshire and Nethergarde Keep
9. At Watchmaster Sorigal 5464 (L29), Duskwood 75.8,46.2: `[QT1477]` (970 XP), then `[QA1395 Supplies for Nethergarde]`. 1395: 2,900 XP + 50s at the hand-in (zone_10 / zone_4 money 5000). L45, req 40. Prerequisite: none in rows [11]/[12] (1477 is its breadcrumb, row [27]). Objective (row [7]): "Bring the Crate of Powerstones to Quartermaster Lungertz, before the powerstones expire." Source item Crate of Power Stones 6091 (row [10]); its tooltip (nether item/6091, 13 Nov): Quest Item, Unique, "Duration: 1 hour". Flight is direct, so no hurry; say "the crate lasts an hour: fly straight on".
10. Fly: at Felicia Maline 2409, Duskwood 77.5,44.3, fly `[F Nethergarde Keep]` (direct link 12->45).
11. At Quartermaster Lungertz 5393 (L54), Blasted Lands 66.5,21.4: `[QT1395]` - 2,900 XP + 50s. No reward choice.

### Leg 3 - the Pool of Tears
12. `[OC]` the way, unverified (round 1 rode it the other way, 37:48-49): out of Nethergarde north through the pass into the Swamp of Sorrows past the Fallen Hero of the Horde (Swamp 34.3,66.1), then east keeping south of Stonard. Stonard (Horde) sits at about 41-50,55-62 (DB: Stonard Grunts 866 L56 at 41-48,56-58; Enraged Stonard Grunts 275088 L55 at 47-50,60; Stonard Orc 864 L48); keep south of y 64 between x 40 and 52. Blasted Lands on the way: the Dreadmaul ogres (45-47) stand at 41-44,11-15 and the Scorpok Stingers (50-51) at 44-50,15-26 (DB): keep to the road. Deathstrike Tarantulas 769 (40-41, not elite, 17 spawns at 55-62,60-69) are the only hostiles on the last stretch.
13. Travel: ride to the ring's south point `[G70.2,60.5 Swamp of Sorrows]`.
14. `[OC]` |cFFFF0000Danger:|r Mukomonji 262306, level 62, rank 1 (elite) in npc.json, one spawn at Swamp 62.4,52.9: 2.5 units west of the ring's west point (64.9,53.3). Come in from the south and do not cross the west edge. Round the Pool (DB, x60-80 y42-64, none elite): Wyrmkin Dreamwalker 743 (42-43, 4), Green Scalebane 744 (42-43, 3), Scalebane Captain 745 (43-44, 2), Green Wyrmkin 742 (41-42, 1), Elder Dragonkin 746 (45, 1, at 78,55), Deathstrike Tarantula 769 (40-41), Shadow Panther 768 (39-40), Sawfin Frenzy 14356 (38-40, 8, in the water).
15. Objective **1448**: ride north from the south point into the ring until "Search for the Temple of Atal'Hakkar" completes `[QC1448]` `[G70.2,56.0 Swamp of Sorrows]` (a point inside the ring, 4.5 units north of the south point; where exactly it fires is unverified). The nether quest tooltip also lists "Razor Hill" as a requirement: an area-name artifact of Wowhead's page (the DB has one objective); do not write it.
16. Back to Stormwind, with the bind: `|cFFfff8a3Hearth to [H Stormwind]|r` (Astral Recall does the same if the hearth is on cooldown).
    Without the bind (if Deviation 1 is rejected, or hearth and Astral Recall are both on cooldown): ride back the same way to Nethergarde Keep `[G65.5,24.3 Blasted Lands]` and at Alexandra Constantine 8609 fly `[F Stormwind]` (direct link 45->2, cost 830).

### Leg 4 - Stormwind again
17. At Brohann Caskbelly 5384, Stormwind 69.5,40.4: `[QT1448]` (3,600 XP, 0 money) and `[QA1449 To The Hinterlands]`. 1449: 1,800 XP, 0 money (zone_1519 / zone_47) at Falstad. L43, req 38. Prerequisite 1448 (row [12] = [1448]). Giver row [1] [[5384]] (Stormwind, not Aerie Peak). Objective: "Speak with High Thane Falstad Wildhammer at Aerie Peak in the Hinterlands."
18. Fly: at Dungar Longdrink 352, Stormwind 71.3,72.2, fly `[F Aerie Peak]` (the game routes it through Ironforge: links 2->6 50, 6->43 730). Brohann is 4 units from the tram: taking the tram to Ironforge and flying from Gryth Thurden 1573 (55.5,47.7) is the same trip; the writer picks one (round 1 flies).

### Leg 5 - Aerie Peak and Rhapsody
19. At Falstad Wildhammer 5635 (L50), Hinterlands 11.8,46.8: `[QT1449]` (1,800 XP) `[QA1450 Gryphon Master Talonaxe]`. 1450: 890 XP, 0 money (zone_47). L43, req 38. Prerequisite 1449 (row [12]). Objective: "Speak with Gryphon Master Talonaxe inside the Aerie Peak Aviary."
20. At Gryphon Master Talonaxe 5636 (L44), Hinterlands 9.8,44.5 (the Aviary): `[QT1450]` (890 XP) `[QA1451 Rhapsody Shindigger]`. 1451: 1,800 XP, 0 money. L43, req 38. Prerequisite 1450. Objective: "Seek out Rhapsody Shindigger in The Hinterlands."
21. `[A Shaman]` `[O]` at Farseer Maret Firetend 270263 (L45), Hinterlands 14.4,42.6, `[T]`: the level 42 row only if it was not bought in Ironforge in chapter 43 (trainer_costs.json 270263, 12 Nov, raw Wowhead values): Grace of Air Totem 1 1g 60s, Fire Resistance Totem 2 1g 60s, Windfury Totem 2 1g 60s, Fire Nova 4 1g 89s 47c (6g 69s 47c in all). Must / later marks as chapter 43 writes them (the leveling sheet's level-42 row reads "Grace of Air Totem 1, Fire Nova 4; later: Windfury Totem 2"). Her list matches Eldrun's for these four (same rows in trainer_costs.json). She has no Ghost Wolf (29:68).
22. `[O]` at Drakk Stonehand 11097 (L55), Hinterlands 13.4,43.5, `[T]` train Artisan Leatherworking (5g; trainer_costs.json 11097: "Artisan Leatherworking", skill 200, 50000c) - only if Leatherworking is 200. Character-level gate unverified (round 1's wording, 29:69). Gate line, rule 11 (profession rank).
23. `[OC]` the walk to Rhapsody: east out of Aerie Peak along the road, about 15 units (unverified road). Trained Razorbeaks 2657 (40-42) and Wildhammer Sentries are friendly (29:66). Hostile on the way (DB, x14-30 y42-54, none elite): Mangy Silvermane 2923 (41-42, 14 at 17-24,48-53), Vicious Owlbeast 2927 (42-43, 3 at 24-27,49-53), Silvermane Wolf 2924 (43-44, 2 at 25-28,51-53). Just east of Rhapsody the Highvale elves: Marksman 2693 (45-46) at 28-30,46-50, Ranger 2694 (46-47) at 28-30,43-46, Outrunner 2691 (43-44), Scout 2692 (44-45), and Vengeful Spirits 221828 (45) at 29-30,47-50: do not go east of x 28.
24. At Rhapsody Shindigger 5634 (L44), Hinterlands 26.9,48.6: `[QT1451]` (1,800 XP) `[QA1452 Rhapsody's Kalimdor Kocktail]`. 1452: 3,600 XP, 0 money, counted in chapter 48 where it is handed in to Rhapsody. L43, req 38. Prerequisite 1451 (row [12]). Objective (row [7]): 3 Roc Gizzards (6257), 3 Groddoc Livers (6259), 3 Ironfur Livers (6258); row [9] lists the three items with count 0, the 3 comes from the text. Droppers (qinfo): Roc 5428 (41-43, Tanaris), Fire Roc 5429 (43-45), Searing Roc 5430 (47-49); Ironfur Bear 5268 (41-42, Feralas), Grizzled Ironfur Bear 5272 (44), Ironfur Patriarch 5274 (48-49); Groddoc Ape 5260 (42-43, Feralas), Groddoc Thunderer 5262 (49-50). Budgets are the plan's (answer 3) and belong to chapters 46-47: about 25 Rocs, 12 bears, 11 apes. Row [21] next = 1469 Rhapsody's Tale (chapter 50). Label: required (Braedyn, answer 3). Write the accept with its carry note: "(3,600 XP at Rhapsody in chapter 48: the gizzards in Tanaris, the livers in Feralas)".
25. Walk back west to Guthrum Thunderfist 8018 `[G11.1,46.2 The Hinterlands]` (travel line; chapter 45 starts with his flight).
26. `[OC]` Check line (section 7).
27. `[NX 42-43 Stranglethorn Vale]`

## 5. Gear calls
None. No kept or conditional quest of this chapter has a reward choice or a fixed item reward: `itemchoices` and `itemrewards` are empty in the zone JSON for 1363, 1448, 1449, 1450, 1451, 1452, 1395, 1477, 94893, 94894 (zone_1519, zone_10, zone_4, zone_47, zone_16591). `score_items.py` was not needed.

## 6. Out (silent; reasons from `_decisions.tsv`)
- 1364 Mazen's Behest: drop under 30%, Khadgar's Essays on Dimensional Convergence 5.0% (5 droppers, best Molt Thorn 8% of 12).
- 543 The Perenolde Tiara: elite outside a dungeon (rule 13), Grel'borg the Miser (39 elite); not on the route.
- 212 A Meal Served Cold: drop under 30%, Chilled Basilisk Haunch 3.06%.
- 1423 The Lost Supplies (Swamp): no XP, nothing kept behind it.
- Blasted Lands 2581 / 2583 / 2585 / 2601 / 2603 (and 2582 / 2584 / 2586 / 2602 / 2604 behind them): three-item collections at 30-36% for a one-hour buff item (rule 11). 3501 Everything Counts In Large Amounts: drop under 30% (1.5%); 3502 behind it.
- Not out, later (no tag here): 3787, 3789, 5066, 5048 (round 3); 95264 Shaw Needs To Know (L53 req 48, kept by the rules, not used in round 2); Blasted Lands 96797 / 96798 / 96799 / 96811 / 93684 / 93685 (req 45, L54-55: "in the pool, not used in round 2"), 2521 / 2522 (elite, GROUP?), 93572 (no side), 87295 (round 3); Swamp 93679, 3374, 3512 (L55); Hinterlands quests at Aerie Peak (2988, 2877 and the rest) are chapter 48's: do not take them here.

## 7. End check
`[OC]|cffffcc00Check:|r handed in here: Mazen's Behest (1363), Vital Supplies (1477), Supplies for Nethergarde (1395), In Search of The Temple (1448), To The Hinterlands (1449), Gryphon Master Talonaxe (1450), Rhapsody Shindigger (1451); and if you carried them, The Twilight Threat (94894) and Delivering Closure (94893). In the log: Rhapsody's Kalimdor Kocktail (1452: gizzards in Tanaris, chapter 46; livers in Feralas, chapter 47; hand-in at Rhapsody, chapter 48). Still carried from chapters 42-43: Friz's errands (I Know a Guy 95295 for chapter 45, From Port to Port 95219 for chapter 47, Shipping and Handling 95296 if taken). Hearth = Stormwind (Farholde Keep if the bind was skipped); chapter 45 binds Booty Bay. You stand at Guthrum Thunderfist in Aerie Peak.`

Carried out: 1452 (to chapters 46-48); 95295, 95219, 95296 untouched. Bind: Stormwind (Deviation 1).

## 8. Totals
- Required: 7 quests, **12,290 XP**, **50s**: 1363 330; 1448 3,600; 1449 1,800; 1450 890; 1451 1,800; 1395 2,900 (+50s); 1477 970. Equals the plan's XP-table row 44 (route_xp.py: 7, 12,290, 50s, 42.2 -> 42.4, highest required level 40).
- Optional / conditional: 94893 4,200 (+70s) + 94894 4,850 = **9,050 XP**, 70s. Equals the plan's 9,050.
- Picked up here, counted later: 1452 3,600 (chapter 48).
- Spending (optional lines): level 42 row 6g 69s 47c if not bought in chapter 43; Artisan Leatherworking 5g at skill 200; flights about 3s 30c + 8s 30c + 7s 80c (TaxiPath cost fields; 8s 30c more without the bind).

## 9. Unverified / in-game test list, Needs pull, Unsure
Unverified / test list:
- Where inside the Pool of Tears ring "Search for the Temple of Atal'Hakkar" completes (DB gives the ring only).
- Mukomonji (262306, level 62 elite, Swamp 62.4,52.9): what it is, hostile or not, stands or patrols. Also an unknown Forever NPC Shen'dorei Windwell (271929, level 1-2) at the Pool's centre (70,56) and Fel Tear / Fel Interloper spawns (222697 / 223543, 35-38) at 61,43-44: not used.
- Enraged Stonard Grunts (275088, L55) at Swamp 47-50,60: hostile to the Alliance on the ride past Stonard?
- The Nethergarde - Swamp pass and the ride south of Stonard; the Aerie Peak - Rhapsody road; the Highvale elves' reach toward Rhapsody.
- Flight prices against the TaxiPath cost fields.
- Drakk Stonehand's character-level gate for Artisan Leatherworking.
- 1452's per-item count of 3 (row [9] counts are 0).

Needs pull: none for this chapter's required steps. (Mukomonji's Wowhead NPC page would settle what it is; not needed to route round it.)

Unsure:
- Whether chapter 42 gives 94893 / 94894 (their hand-ins here are written "only if you carry it", so the chapter works either way).
- Whether chapter 43 buys the level 42 row (Maret's line is `[O]` "only if not bought in chapter 43").
- Whether the hearth is off cooldown at the Pool (chapter 43 hearths for the Krol'dok run); Astral Recall and the ride back are written as fallbacks.

## 10. Deviations from the route plan
1. **Bind in Stormwind** (Innkeeper Allison 6740, 60.4,75.3) on leg 1, and hearth (or Astral Recall) from the Pool of Tears to Stormwind. The plan's hearth proposal keeps Farholde Keep through chapter 44 and its loop returns Pool - Nethergarde - Stormwind. Reason: nothing in chapters 44-45 uses the Farholde bind (45 binds Booty Bay on arrival, plan Threads), and the bind saves the ride back across the Swamp and the pass (about 37 units in the Swamp alone, Pool 70,60 to the Fallen Hero 34.3,66.1) plus the 8s 30c flight (TaxiPath 45->2). The plan's way is written as the fallback in step 16. Braedyn's call.
2. Quest list, XP and money: no change. 1448 > 1449 > 1450 > 1451 > 1452 checked in rows [12]; 1449's giver is Brohann in Stormwind (row [1] [[5384]]), so 1449 is taken on the second Stormwind visit, after the Pool, as the plan's loop has it.
3. Small additions the plan does not state: 1477 must be handed in before 1395 is accepted (1477 row [26] = 1395, 1395 row [27] = [1477]: breadcrumb); both conditional hand-ins (94894 Bolvar, 94893 Abigail Lawson) fall on the first Stormwind visit.
