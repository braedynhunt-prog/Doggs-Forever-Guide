# Spec 48 - The Hinterlands 43-45 (drafted 13 Nov 2026, round 2, third wave)

Data used (all read 13 Nov 2026): tooling/qdb = QuestieDB Forever 1.0.16 (quest/npc/object/item.json); data/zone_47.json and zone_1537.json (Wowhead XP, money, side, itemchoices); data/wowhead_quest_links.json; data/drop_rates.json (no row for 8704 or 279225); data/browser/r2_pages3_2026-11-13.tsv (QUEST 86616) and r2_pages_2026-11-12.tsv (NPC 270263); nether.wowhead.com/forever/tooltip item/279225, item/8704, quest/86616, item/9645, 9646, 270101, object/669105 (shell, 13 Nov); classicdb.ch item 8704, npc 7996 / 8636 (Classic only, marked so); tooling/trainer_costs.json (12 Nov); tooling/client/1.60.1.70938/TaxiNodes.csv + TaxiPath.csv; weights/tooltips/2026-11-12.json; `python weights/score_items.py --band 40` (central weights str 2.00 int 1.69 agi 1.12 spi 2.50 sta 0 sp 2.00). Pool files 47_Hinterlands.txt, 1537_Ironforge.txt, 440_Tanaris.txt, 16591_Riverglades.txt; _decisions.tsv.

## 1. Header
- File: `48_Hinterlands.lua`
- `[N 43-45 The Hinterlands]`
- `[NX 44-45 Searing Gorge]` (plan title of chapter 49; match it to the chapter-49 spec)
- `[GA Alliance]`; class lines `[A Shaman]`. Group "Forever Shaman 30-60".
- `[D ...]`: "Back east by Theramore and the Menethil boat to Aerie Peak: Rhapsody's Kocktail handed in, the Witherbark cages and the Altar of Zul for Talonaxe (the chain that leads to Zul'Farrak), Skulk Rock's oozes, the OOX-09/HL escort, Maret Firetend's totems at 45; then Ironforge for the level-44 training, the Explorers' League (Uldum, Tymor) at 45 and the bind for the Searing Gorge."
- Level on entry 43.5 (plan XP table), exit 44.0 on required quest XP (the plan counts 836 here; see Deviations 1).
- **Level-check line (first `[OC]`):** "This chapter wants level 45: Repurposed Totems (Aerie Peak) and the four Explorers' League pickups in Ironforge (Portents of Uldum, Passing the Burden, An Easy Pickup, Signal for Pickup) need 45 to accept. Mobs: the Witherbark cages 40-44, the Altar of Zul 45-47, Skulk Rock 46-48, the escort's ambushers 46-47. Under 45 (expected: about 43.5 in, 44 out): do the cages first, then the Altar, Skulk Rock and the escort; leave Repurposed Totems untaken and do the Ironforge pickups only once you are 45 (see the Ironforge leg)."

## 2. Entry state
- Stands at Feathermoon Stronghold's flight master [TAR8019 Fyldren Moonfeather] 30.2,43.2 Feralas (chapter 47 end). Hearth = Feathermoon (chapter 47 `[S]`, assumed from the prompt). Known flight points needed: Feathermoon, Thalanaar (chapter 47), Theramore (`[P Theramore]` 32:28), Menethil Harbor (`[P Menethil Harbor]` 09:61), Aerie Peak (`[P Aerie Peak]` 29:67), Ironforge, Thelsamar, Farholde Keep (`[P Farholde Keep]` 38).
- Carried in, handed in here: **1452 Rhapsody's Kalimdor Kocktail** (accepted chapter 44; 3 Roc Gizzard 6257 from chapter 46, 3 Ironfur Liver 6258 and 3 Groddoc Liver 6259 from chapter 47).
- Carried in, conditional ("only if you carry it"): **95327** All's Well That Ends Well (from Caravaneer Ruzzgot 3945, Booty Bay, chapter 45, if offered), **97332** Twice Misplaced Trust (Wharfmaster Lozgil 4631, Booty Bay, chapter 45, if offered; source item 277974 Twice Reordered Package), **95472** Consolation Prize (Tazzik 260857, Steamwheedle Port 67.3,24.0 Tanaris, chapter 46, if offered).
- Possibly carried in (only if an earlier Ironforge stop took them; the chapter 43/44 specs decide): 6625 Alliance Trauma, 6609 I Got Nothin' Left!.
- Training and professions that fall here: shaman level-44 row (Firetend at Aerie Peak or Eldrun in Ironforge); Artisan Leatherworking at Drakk Stonehand if not taken in chapter 44; Artisan First Aid and Artisan Fishing gates on the Theramore pass and in Ironforge.

## 3. Travel and hearth
- **In, flight:** Feathermoon - Thalanaar - Theramore: TaxiPath 325/326 (41<->31) and 56/57 (31<->32). One `Fly to [F Theramore]` at Fyldren Moonfeather 8019 (30.2,43.2 Feralas). Theramore flight master [TAR4321 Baldruc] 67.5,51.3 Dustwallow Marsh.
- **Boat:** Theramore east dock (71.5,55.5 per 32:27) to Menethil Harbor; Menethil pier 5.6,63.2 Wetlands (32:25). Boats are not in the data: unverified (32:25 already flags boat-or-portal).
- **Menethil to Aerie Peak:** [TAR1571 Shellei Brondir] 9.5,59.7 Wetlands, `Fly to [F Aerie Peak]`: two-hop either way, Menethil - Refuge Pointe - Aerie Peak (TaxiPath 269 7->16, 275 16->43) or Menethil - Ironforge - Aerie Peak (17 7->6, 263 6->43). Aerie Peak flight master [TAR8018 Guthrum Thunderfist] 11.1,46.1 (guide 29:67 uses 11.1,46.2).
- **Hearth does not help on the way in** (bound at Feathermoon, where he starts).
- **Bind 1: Aerie Peak**, on arrival, at [TAR7744 Innkeeper Thulfram] 14.2,41.6 Hinterlands: `bind your Hearthstone to [S Aerie Peak]`. Reason: the escort ends on the east coast at 79.1,61.4, the far side of the zone from every hand-in; `Hearth to [H Aerie Peak]` (Astral Recall does the same) brings him back to Talonaxe, Fraggar and Firetend.
- **Bind 2: Ironforge**, at the end of the Ironforge leg, [TAR5111 Innkeeper Firebrew] 18.1,51.5 Ironforge: `bind your Hearthstone to [S Ironforge]`. Reason: chapter 49 is a first trip on foot to Thorium Point and chapter 50 starts in Ironforge (tram to Stormwind); a hearth at the end of chapter 49 then lands where chapter 50 starts. If the chapter-49 spec wants another bind, the main session reconciles.
- **Out:** Aerie Peak - Ironforge flight (TaxiPath 264 43->6, cost field 730). Ironforge flight master [TAR1573 Gryth Thurden] 55.5,47.7.
- **Conditional Powderfuse ride (only if he carries 95327, 95472 or 97332):** from Aerie Peak `Fly to [F Farholde Keep]` (Aerie Peak - Ironforge - Thelsamar - Farholde Keep: TaxiPath 264, 16 (6->8), 11589 (8->3276)); flight master [TAR257087 Gretchen Mayberry] 61.1,80.8 Riverglades; ride north-east to Powderfuse Port (Friz 77.1,52.9; Whizzbuzz 79.5,52.7), ride back, `Fly to [F Ironforge]` (3276->8->6). Placed before the Ironforge leg so its XP counts toward 45 before the level-45 pickups.

## 4. Route (play order)

### Leg A - Theramore pass and the boat (optional gates only)
1. `[O]` Only if you carry Alliance Trauma (6625) and First Aid is 225: at [TAR12939 Doctor Gustaf VanHowzen] 67.8,49.0 Dustwallow Marsh, `[QT6625 Alliance Trauma]` (970 XP) `[QA6624 Triage]` (3,900 XP, req 35, L45; source item 16991 Triage Bandage); do the triage there and `[QT6624]`. Gate: Artisan First Aid (rule 11). Not counted.
2. `[O]` Only if you carry I Got Nothin' Left! (6609) and Fishing is 225: at [TAR12919 Nat Pagle] 58.6,60.1 Dustwallow Marsh (outside Theramore, about 15 units south-west of the flight master), `[QT6609 I Got Nothin' Left!]` (970 XP) `[QA6607 Nat Pagle, Angler Extreme]` (3,900 XP at the hand-in; four fish from fishing spots in Feralas 62.8,51.6, Swamp of Sorrows 87.1,61.4, Desolace 28.8,62.1 and Stranglethorn 28.5,34.6 - carried out). Gate: Artisan Fishing. Not counted.
3. Boat to Menethil (unverified, see section 3); `Fly to [F Aerie Peak]` at Shellei Brondir.

### Leg B - Aerie Peak (first visit) and the Witherbark cages (mobs 40-44)
4. Bind Aerie Peak at Innkeeper Thulfram 7744, 14.2,41.6.
5. Accept **2988 Witherbark Cages** (3,900 XP, 0 money; L45 req 40; no prerequisite: rows [11]/[12] null) at [TAR5636 Gryphon Master Talonaxe] (L44) 9.8,44.5 Hinterlands. Objective: check three cages - First Witherbark Cage obj 144066 23.3,58.8; Second 144067 23.1,58.8; Third 144068 32.0,57.3. Plain.
6. Accept **2877 Skulk Rock Clean-up** (4,400 XP, 50s; L48 req 40; no prerequisite) at [TAR7884 Fraggar Thundermantle] (L60) 14.8,44.6. Objective: kill 10 Green Sludge (2655, L46-47) and 10 Jade Ooze (2656, L47-48), counts from row [7] text (row [9] count fields are 0); Skulk Rock x44-60 y38-55. Plain (kill quest; done in Leg C).
7. `[O]` `[A Shaman]` At 45 only: accept **86616 Repurposed Totems** at [TAR270263 Farseer Maret Firetend] (L45) 14.4,42.6 (see Leg D step 20 for the facts). Expected: not yet 45 here.
8. `[O]` `[A Shaman]` At 44 only: Firetend `[T]` level-44 row (section "Trainers"). Expected: not yet 44 here.
9. `[O]` At Leatherworking 200, if not bought in chapter 44: [TAR11097 Drakk Stonehand] 13.4,43.5 `[T]` Artisan Leatherworking (spell 10662, 5g). Character-level gate unverified.
10. Witherbark village west: cages at 23.3,58.8 and 23.1,58.8 `[QC2988]`. Mobs there (qdb within 6 units): Witherbark Scalper 2649 L40-41, Zealot 2650 L41-42, Hideskinner 2651 L42-43, Trained Razorbeak 2657 L40-42 (friendly per 29:66), Vicious Owlbeast 2927 L42-43, Mangy Silvermane 2923 L41-42; Witch Doctor Ti'ik 270772 L49 (one spawn near; not elite in qdb) - avoid.
11. East cage 32.0,57.3 `[QC2988]`. Mobs: Witherbark Hideskinner 42-43, Venomblood 2652 L43, Silvermane Wolf 2924 L43-44, Vicious/Primitive Owlbeast 42-45; Zul'arek Hatefowler 8219 L43 (rank 4 = rare).
12. `[OC]` The OOX-09/HL Distress Beacon (item 8704, "This Item Begins a Quest", Requires Level 43; tooltip 13 Nov) drops from 53 Hinterlands mob types in qdb item row [1], every mob of this chapter among them (Witherbark, oozes, Vilebranch, owlbeasts, wolves). No Forever rate in the data: when it drops, right-click it: **accept 485 Find OOX-09/HL!** (4,400 XP; L48 req 43; starts from item 8704, quest row [1] = [null,null,[8704]]; ends at Homing Robot OOX-09/HL 7806, 49.4,37.7). Write it as `[UI8704]` + `[QA485 Find OOX-09/HL!]` (RULES: `[UI]` is in use but unverified on Forever), as an `[O]`-free plain step that fires only when the beacon is in the bags.
13. Turn in **1452 Rhapsody's Kalimdor Kocktail** (3,600 XP, 0 money; prerequisite 1451, chapter 44) at [TAR5634 Rhapsody Shindigger] (L44) 26.9,48.6 Hinterlands (not in Aerie Peak: about 15 units east of it). Accept **1469 Rhapsody's Tale** (2,700 XP at Brohann Caskbelly 5384, Stormwind 69.5,40.4 in chapter 50; row [12] = [1452]; source item 6287 Atal'ai Tablet Fragment). Mobs around Rhapsody: Highvale Marksman 2693 L45-46, Ranger 2694 L46-47, Scout 2692 L44-45, Vengeful Spirit 221828 L45; Jalinde Summerdrake 8214 L49 rank 4 (rare).
14. Back to Aerie Peak: turn in **2988** at Talonaxe 9.8,44.5; accept **2989 The Altar of Zul** (4,400 XP, 0 money; L48 req 40; row [12] = [2988]). Objective: "Check the top of the Altar of Zul" (trigger row [8]: 48.98,68.66 Hinterlands).
15. `[O]` At 45 only: Repurposed Totems at Firetend (if step 7 did not fire). At 44: the level-44 row at Firetend (if step 8 did not fire).

### Leg C - the Altar of Zul, Skulk Rock and the escort (mobs 45-48)
16. The Altar of Zul top, 49.0,68.7 `[QC2989]`. Mobs within 6 units (qdb): Vilebranch Soothsayer 4467 L46-47, Vilebranch Scalper 4466 L46-47, Vilebranch Axe Thrower 2639 L45-46, Vilebranch Wolf Pup 2680 L46-47, Vilebranch Witch Doctor 2640 L46-47; Retherokk the Berserker 8216 L48 rank 4 (rare, 4.8 units away). **qdb puts two level-50 elites 0.4-0.5 units from the trigger: Morta'gya the Keeper 8636 (48.77,68.36) and Qiaga the Keeper 7996 (48.64,68.24)** (npc row [5] = 1; classicdb: Elite, hostile to both factions; Classic comments speak of clearing the stairs and path to them). Write it as a plain step with a warning `[OC]`: "touch the top and leave; the two Keepers (50 elite) stand on it" - and see Unsure 1.
17. If 86616 was taken: Vilebranch Totem 279225 x12 - ground objects "Vilebranch Totem" 669105 (Wowhead tooltip map: 12 points at 46.1-48.8, 64.3-68.5, right around the Altar; not in qdb object.json) and Vilebranch Soothsayer 4467 (L46-47, 22 qdb spawns x45-71 y39-69, 14 of them within 6 units of the Altar) at 11.38% (nether tooltip 13 Nov). Hold with `[CI279225,12]` or `[QC86616]` (single objective). Rule 12: plain, because the item also comes from a ground object. Kill budget from the drop alone would be ~105 kills; say "loot the totems on the ground around the Altar; Soothsayers drop them too (11%)".
18. Skulk Rock: **2877** objectives - 10 Green Sludge 2655 (L46-47, 46 spawns, x44-60 y39-55, centre 51.7,44.5) and 10 Jade Ooze 2656 (L47-48, 45 spawns, x45-60 y38-53, centre 54.8,43.2) `[QC2877]`. Not elite. Note: qdb also has a Green Sludge 222978 L50 (8 spawns around 46.4,37-40) - a different id; only 2655 counts.
19. If the beacon dropped: turn in **485** at [TAR7806 Homing Robot OOX-09/HL] (L42) 49.4,37.7 and accept **836 Rescue OOX-09/HL!** (5,450 XP; L48 req 43; row [12] = [485]; ends at Oglethorpe Obnoticus 7406, Booty Bay 28.4,76.3 Stranglethorn - chapter 50; see Deviations 1). Escort OOX-09/HL to "the shoreline beyond Overlook Cliff" (row [8] trigger 79.14,61.36 Hinterlands) `[QC836]`. Ambushers in qdb: Marauding Owlbeast 7808 L46, Vilebranch Ambusher 7809 L47 (not elite; their count and timing are Classic knowledge, unverified). **Warning: qdb has Wrath Whelp 221326 (L51) 0.3 units from the robot and Wyrmkin Starhunter 221325 (L51) 1.7 units away, plus other L50-51 Forever-only npcs (221324, 221312, 221330) within 5 units** - see Unsure 2.
20. `Hearth to [H Aerie Peak]` (Astral Recall does the same) from the escort's end, 79.1,61.4.

### Leg D - Aerie Peak (second visit)
21. Turn in **2877** at Fraggar 14.8,44.6 (4,400 XP, 50s).
22. Turn in **2989** at Talonaxe 9.8,44.5 (4,400 XP). Accept **2990 Thadius Grimshade** (2,100 XP at the hand-in; L47 req 40; row [12] = [2989]; source item 9468 Sharpbeak's Feather; ends Thadius Grimshade 8022, Blasted Lands 66.9,19.5 - Nethergarde Keep, chapter 50). Chain from the rows: 2988 > 2989 (row [12] [2988]) > 2990 (row [12] [2989]) > 2991 Nekrum's Medallion (row [12] contains 2990; given by Thadius, Zul'Farrak chapter 54).
23. **86616 Repurposed Totems** (4,400 XP, 70s; L48 req 45; Alliance, start and end Farseer Maret Firetend 270263 at 14.4,42.6 - Wowhead quest page 13 Nov and qdb agree; series none; objective "Bring 12 Vilebranch Totems", row [9] = item 279225, count 12 from the text and the tooltip). If taken at step 7 or 15: turn in here. If he is 45 only now: `[O]` accept it, ride back to the Altar (step 17), return - about 35 units each way. If he is still under 45: leave it; Aerie Peak's next visit is round 3 (2993 Return to the Hinterlands, plan "Left for round 3"). Counted as required by the plan; see Deviations 4.
24. `[A Shaman]` At 44: Firetend `[T]` level-44 row if not bought (prices below). Otherwise in Ironforge.

### Leg E - conditional: Powderfuse Port (only if you carry one of the three)
25. `[O]` Aerie Peak `Fly to [F Farholde Keep]` (section 3); ride to Powderfuse Port.
26. `[O]` If you carry it: turn in **95327 All's Well That Ends Well** (3,150 XP, 0 money) and **95472 Consolation Prize** (2,350 XP, 0 money; fixed reward 270334 Sweat-Stained Shirt, a statless shirt) at [TAR255897 Friz Frazzlespark] (L41) 77.1,52.9 Riverglades.
27. `[O]` If you carry it: turn in **97332 Twice Misplaced Trust** (3,300 XP, 0 money; fixed 2595 Jug of Bourbon, choice of three rings) at [TAR259961 Wharfmaster Whizzbuzz] (L45) 79.5,52.7 Riverglades.
28. `[O]` Ride back to Gretchen Mayberry 61.1,80.8, `Fly to [F Ironforge]`.
(Without any of the three: from Aerie Peak `Fly to [F Ironforge]` at Guthrum Thunderfist 11.1,46.1.)

### Leg F - Ironforge (last: the level-45 pickups)
29. `[A Shaman]` [TAR258098 Eldrun Stormbreaker] 47.1,13.8 Ironforge `[T]` level-44 row if not bought at Firetend (needs 44).
30. At 45 only, the Explorers' League (Hall of Explorers):
    - [TAR5387 High Explorer Magellas] 69.9,18.6: accept **2963 Portents of Uldum** (470 XP; L50 req 45; row [12] = [2439] The Platinum Discs - a "level 40 only" line in 39e: if 2439 was not done, Magellas will not offer it and the Uldum chain is gone).
    - [TAR2916 Historian Karnik] 77.5,11.8: turn in **2963**; accept **2946 Seeing What Happens** (4,700 XP, req 45; Uldum Pedestal 142343, Tanaris 37.6,81.4 - chapter 53; counted there; the pool flags it GROUP: chapter 53's matter). Accept **3448 Passing the Burden** (510 XP; L52 req 45; no prerequisite).
    - [TAR8507 Tymor] 31.0,4.8: turn in **3448**; accept **3449 Arcane Runes** (2,550 XP, req 45; row [12] = [3448]; four rune rubbings in Azshara, ends Pilot Xiggs Fuselighter 8392 Azshara 77.8,91.4 - chapter 55; counted there) and **3450 An Easy Pickup** (510 XP; L52 req 45; no prerequisite in rows [11]/[12]; qdb row [24] parentQuest = 3449, so Tymor may only offer it once Arcane Runes is in the log - accept 3449 first).
    - [TAR8517 Xiggs Fuselighter] 70.9,94.6: turn in **3450**; accept and turn in **3451 Signal for Pickup** (510 XP; row [12] = [3450]; fixed reward 10444 Standard Issue Flare Gun - keep it for Azshara). 3483 Signal for Pickup (no XP, the replacement gun) is not taken.
    - Under 45: skip all of step 30; see Deviations 3 for when it can be done.
31. `[O]` At First Aid 225, if not carried: [TAR5150 Nissa Firestone] 55.1,58.3 `[QA6625 Alliance Trauma]` (req 35; ends VanHowzen, Theramore - chapter 51's Theramore pass). At Fishing 225, if not carried: [TAR5161 Grimnur Stonebrand] 48.1,6.9 `[QA6609 I Got Nothin' Left!]` (req 35; ends Nat Pagle - chapter 51). Gates, not counted.
32. Bind Ironforge at Innkeeper Firebrew 5111, 18.1,51.5.

## Trainers / vendors (prices: tooling/trainer_costs.json, pulled 12 Nov, Wowhead raw values)
- Level-44 row, identical at Eldrun 258098 and Firetend 270263: Lightning Bolt R8 (10392) 1g 80s; Stoneskin Totem R5 (10407) 1g 80s; Lesser Healing Wave R4 (10466) 1g 80s; Nature Resistance Totem R2 (10600) 1g 80s; Rockbiter Weapon R6 (16315) 1g 80s. Total 9g (whether trainers charge 5% less is on the test list).
- Artisan Leatherworking (10662) at Drakk Stonehand 11097: 5g, skill 200.
- No vendor purchase in this chapter. Gold check: quest money before Ironforge here is 50s (+70s with 86616); tooling/gold.py covers chapters through 41 only.

## 5. Gear calls (band 40, central [conservative]; tooltips 2026-11-12.json)
- 836 Rescue OOX-09/HL! (choice; hand-in at Booty Bay, chapter 50): Gnomish Inventor Boots 9645 (cloth feet +7 Sta +2 Int +11 Spi) 30.9 [19.9] over Gnomish Floatation Device 270101 (leather feet +10 Str +10 Sta) 20.0 [20.0]; Gnomish Water Sinking Device 9646 is plate (-5 Agi +16 Sta), unusable. Replaces: if he wears Southsea Mojo Boots (34.6, 8366 Southsea Shakedown, chapter 46) no upgrade - then take the Water Sinking Device for its sell price (67s 91c, against 67s 68c / 64s 34c). Otherwise the Inventor Boots.
- 97332 Twice Misplaced Trust (conditional): Apology Ring 278019 (+6 Sta +4 SP) 8.0 over Renegotiated Ring 278018 (+3 Str +6 Sta) 6.0, Refunded Ring 278017 (+8 Sta) 0.0. Only an upgrade over an empty or weaker ring slot.
- 95472 Consolation Prize: Sweat-Stained Shirt 270334, shirt, no stats (fixed).
- 3451: Standard Issue Flare Gun 10444, fixed quest tool.
- No rewards on 1452, 1469, 2988, 2989, 2990, 2877, 485, 86616, 2963, 3448, 3450 (zone_47 / zone_1537 itemchoices and itemrewards empty).

## 6. Out (silent in the Lua; reasons from _decisions.tsv)
- 2880 Troll Necklace Bounty - drop under 30%: Troll Tribal Necklace 28.9% (28 droppers, best Vilebranch Witch Doctor 51% of 35).
- 2881 Troll Necklace Bounty - chain behind 2880.
- 2994 Saving Sharpbeak - elite outside a dungeon (rule 13): Vile Priestess Hexx (51 elite) at the top of Jintha'Alor.
- 4787 The Ancient Egg - guarded by Hitah'ya the Keeper and Vilebranch Aman'zasi Guards (51 elite), rule 13; also needs The Prophecy of Mosh'aru.
- Later, not out: 2992 The Divination (chapter 57), 2993 Return to the Hinterlands (round 3). 1450 / 1451 were chapter 44.

## 7. End check
`[OC]Check:` handed in here: Rhapsody's Kalimdor Kocktail (1452), Witherbark Cages (2988), The Altar of Zul (2989), Skulk Rock Clean-up (2877); Find OOX-09/HL! (485) if the beacon dropped; Repurposed Totems (86616) at 45; at 45 in Ironforge Portents of Uldum (2963), Passing the Burden (3448), An Easy Pickup (3450), Signal for Pickup (3451); conditional: 95327, 95472, 97332 if carried; gates 6625/6624 and 6609 if carried. Carried out: Rhapsody's Tale 1469 (Brohann, Stormwind, chapter 50); Thadius Grimshade 2990 (Nethergarde, chapter 50); Rescue OOX-09/HL! 836, escort complete (Oglethorpe, Booty Bay, chapter 50); at 45: Seeing What Happens 2946 (chapter 53), Arcane Runes 3449 (chapter 55) and the Standard Issue Flare Gun; 6607 Nat Pagle (fish, chapter 51) if taken; 6625 / 6609 if picked up in step 31 (chapter 51). Hearth = Ironforge. Next: chapter 49, the Searing Gorge on foot.

## 8. Totals
| | count | XP | money |
|---|---|---|---|
| Required, as the plan counts them | 11 | 32,550 | 1g 20s (2877 50s + 86616 70s) |
| of which earned in this chapter at the predicted level (no 836 hand-in, no level-45 quests) | 5 (1452, 2988, 2989, 2877, 485; 836's escort done, hand-in chapter 50) | 20,700 | 50s |
| Optional / conditional (95327 3,150 + 95472 2,350 + 97332 3,300) | 3 | 8,800 | 00s |
Sum check: 3,600 + 3,900 + 4,400 x4 (2877, 2989, 485, 86616) + 5,450 + 470 + 510 x3 = 32,550 = plan row. Earned-here figure: 32,550 - 5,450 (836, Booty Bay) - 4,400 (86616) - 2,000 (2963, 3448, 3450, 3451) = 20,700. Gates (6625/6624 4,870, 6609 970) not counted.

## 9. Unverified / in-game test list
- Theramore - Menethil boat (or portal) and both docks.
- OOX-09/HL Distress Beacon: does it drop, from what, how often (no Forever rate in the data).
- The Altar of Zul: are Morta'gya and Qiaga the Keeper (50 elite) on the top, and can a level-44 touch the trigger and leave.
- The OOX-09/HL robot's spot (49.4,37.7): are Wrath Whelps / Wyrmkin Starhunters (L51) there in the open world.
- Vilebranch Totem ground objects 669105: one totem each, how many up at a time, respawn.
- Tymor offers An Easy Pickup only with Arcane Runes in the log (qdb parentQuest).
- Artisan Leatherworking character-level gate at Drakk.
- Bind at Innkeeper Thulfram (Aerie Peak).
- Trainer price raw or 5% off (round-wide item).
- Escort ambush count and mobs (Classic knowledge).
## Needs pull
- Wowhead Forever item 8704 (OOX-09/HL Distress Beacon): dropped-by list with counts.
- Wowhead Forever object 669105 (Vilebranch Totem): loot count per object.
- Wowhead Forever NPC 7996 / 8636 maps (where the Keepers stand) and NPC 221326 / 221325 (zone, phase).
## Unsure
1. The Altar of Zul trigger sits between two level-50 elites in qdb. If they stand on the top in game, 2989 is in practice a GROUP quest (rule 13), and with it 2990 (chapter 50) and Nekrum's Medallion (Zul'Farrak, chapter 54) - the main session's call, not changed here.
2. Level-51 Forever-only npcs (221xxx; names match an Emerald-Dream style event) stand on the OOX robot in qdb. If they are there and hostile, 485/836 at level 44 are dangerous; not changed here.
3. The beacon has no rate: if it fails rule 12 once pulled, 485 + 836 (9,850 XP) go under the main session's ruling (rule 3: no farming for it).
4. Which chapter-43/44 Ironforge stops took 6609 / 6625 (decides whether Leg A fires at all).
5. The level-45 pickups if he is still under 45 at chapter 50's Ironforge start (Deviations 3).

## 10. Deviations from the route plan
1. **836 Rescue OOX-09/HL! is handed in at Booty Bay**, not here: row [2] = [[7406]] Oglethorpe Obnoticus, Stranglethorn 28.4,76.3. Its 5,450 XP and the boot choice fall on chapter 50's Booty Bay leg; the plan's chapter-48 row counts it here. The escort is done here.
2. **Ironforge is last, not first.** At the predicted 43.5 neither the level-44 row nor the level-45 pickups are available on the way in; Menethil flies straight to Aerie Peak (TaxiPath 7->16->43 or 7->6->43). The training is offered at Firetend (Aerie Peak, at 44) or Eldrun (Ironforge, last leg). The conditional Powderfuse ride also comes before Ironforge so its XP counts toward 45.
3. **Level 45 is out of reach at the predicted 44.0**, so 2963, 3448, 3450, 3451 (2,000 XP) and the uncounted pickups 2946 and 3449 that chapters 53 and 55 need are probably not taken here. Next Ironforge pass: chapter 50's start (predicted 44.6, likely still under), then chapter 57 - after chapters 53 and 55. Option for the main session: an Ironforge stop at the end of chapter 50 (predicted 45.1; Booty Bay - Ironforge flight, then the Menethil boat to Theramore for chapter 51 instead of the Ratchet boat). Not decided here.
4. **86616 Repurposed Totems (4,400 XP, 70s) needs 45 at Aerie Peak**; at the predicted level it waits for round 3's return to Aerie Peak (2993). Counted here by the plan.
5. **The plan note "the Witherbark and Skulk Rock quests come last"**: the Witherbark cages' mobs are 40-44, the lowest of the chapter, and 2989 needs 2988 (row [12]), so the cages come first; Skulk Rock (46-48) and the escort come last outdoors.
6. **Two binds** (Aerie Peak, then Ironforge) instead of the plan's one; reasons in section 3.
7. **2963 is conditional on 2439** (row [12] = [2439]), which 39e marks "level 40 only".
