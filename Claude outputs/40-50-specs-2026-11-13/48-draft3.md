# Spec 48 - The Hinterlands (round 2, second revision; re-cut of 48-draft2.md, 13 Nov 2026)

Data used (all read 13 Nov 2026): tooling/qdb = QuestieDB Forever 1.0.16 (quest/npc/object.json; npc row [6] = spawns, [3]/[4] levels, [5] rank); data/zone_47.json, zone_16591.json, zone_33.json (Wowhead XP, money, reqlevel, side, rewards); data/drop_rates.json (item 9259 per-mob rows, dated 12 Nov; item 8704 pooled, 13 Nov); tooling/trainer_costs.json (12 Nov); tooling/client/1.60.1.70938/TaxiNodes.csv + TaxiPath.csv; weights/tooltips/2026-11-12.json; `python weights/score_items.py --band 40`; `python tooling/qinfo.py`, `loc.py`; `python tooling/route_xp.py docs/40-50-route-2026-11-12.txt` (chapter 48 row: 6 quests, 23,350, 1g 15s, 43.4 -> 43.8, optional 15,500; no prerequisite or place fault). Pool files 47_Hinterlands.txt, 16591_Riverglades.txt; _decisions.tsv; overrides_r2.tsv. Guide lines quoted: 29:64-67, 32:25-27, 38:38, 39d:21, 41:6-22.

## 1. Header
- File: `48_Hinterlands.lua`
- `[N 43-44 The Hinterlands]`
- `[NX 43-45 Stranglethorn Vale]` (plan title of chapter 49; match it to the chapter-49 spec)
- `[GA Alliance]`; class lines `[A Shaman]`. Group "Forever Shaman 30-60".
- `[D ...]`: "Back east by Theramore and the Menethil boat: Friz Frazzlespark's last delivery at Powderfuse Port, then Aerie Peak: Rhapsody's Kocktail handed in, the Witherbark cages, the Altar of Zul and its troll necklaces, Skulk Rock's oozes, and Talonaxe's feather for Nethergarde (the chain to Zul'Farrak). Ends in Ironforge."
- Level on entry 43.4, exit 43.8 (plan XP table; route_xp.py agrees).
- **Level-check line (first `[OC]`):** "This chapter wants level 45 for its mobs: no pickup needs more than 40 (the OOX quests 43), but the Altar of Zul trolls are 45-47 and Skulk Rock's oozes 46-48. You arrive at about 43.4. Under 45: Powderfuse Port first (no fighting), then the Witherbark cages (trolls 40-45), then at the Altar pull the Axe Throwers (45-46) at its north and west edge before going up; at Skulk Rock the Green Sludges (46-47) before the Jade Oozes (47-48); the OOX escort, if the beacon dropped, last. Nothing in this chapter waits for a level."

## 2. Entry state
- Stands at Thalanaar, Feralas, after Thalanaar Delivery (chapter 47's end, per the prompt and 47-draft2 Deviation 4); flight master [TAR4319 Thyssiana] 89.5,45.9 Feralas.
- Hearth: Feathermoon (chapter 47 `[S Feathermoon]`, per the prompt; 47 is specced in parallel). Not used in this chapter before the Aerie Peak rebind.
- Flight points known and used: Thalanaar (47), Theramore (`[P]` chapter 32), Menethil Harbor (09:61), Thelsamar, Farholde Keep (38:38), Ironforge, Aerie Peak (29:67).
- **Carried in, handed in here:**
  - 1452 Rhapsody's Kalimdor Kocktail (accepted chapter 44; 3 Roc Gizzard 6257 from chapter 46, 3 Ironfur Liver 6258 and 3 Groddoc Liver 6259 from chapter 47).
  - 95327 All's Well That Ends Well (accepted from Caravaneer Ruzzgot 3945, Booty Bay 27.4,74.1, chapter 45, after The Big Payback 95326).
  - Conditional, only if held: 95472 Consolation Prize (Tazzik 260857, Steamwheedle Port 67.3,24.0 Tanaris, chapter 46, if offered); 97332 Twice Misplaced Trust (Wharfmaster Lozgil 4631, Booty Bay, chapter 45, if offered).
  - Possibly, if an earlier Ironforge stop took them: 6625 Alliance Trauma, 6609 I Got Nothin' Left! (gates; chapters 43/44 decide).
- Training / professions that fall here: shaman level-44 row (Firetend, Aerie Peak, or Eldrun, Ironforge: wherever he first is 44); Artisan Leatherworking at Drakk Stonehand if not bought in chapter 44; Artisan Skinning at Balthus if not bought at 40; the Artisan First Aid / Fishing gates at Theramore and Ironforge.

## 3. Travel and hearth
**Order chosen: (b) Farholde first.** Thalanaar - Theramore - boat - Menethil - Farholde Keep - Powderfuse Port - Farholde Keep - Aerie Peak - Hinterlands quests - Aerie Peak - Ironforge.
- Why (b) over (a) Menethil - Aerie Peak - quests - Farholde - Ironforge: both take three flights from Menethil (seven hops either way), and (b) is a little cheaper by the TaxiPath cost fields (740 + 1,470 + 730 = 2,940c against 1,060 + 1,470 + 740 = 3,270c); and (b) hands in All's Well That Ends Well (3,150 XP, up to 8,800 with the two conditional hand-ins) before he meets the 45-48 mobs, which the level check wants. In (a) the Hinterlands come first at 43.4.
- **In, flight:** at Thyssiana 4319, Thalanaar 89.5,45.9 Feralas, `Fly to [F Theramore]`: TaxiPath 57 (31 -> 32, cost 730). Theramore flight master [TAR4321 Baldruc] 67.5,51.3 Dustwallow Marsh.
- **Boat:** Theramore east dock (71.5,55.5 Dustwallow, 32:27) to Menethil Harbor's south-west pier (5.6,63.2 Wetlands, 32:25). Boats are not in the data; 32:25 already flags this dock as boat-or-portal: unverified, and the plan's test list has "the Menethil - Theramore boat".
- **Menethil - Farholde Keep:** at [TAR1571 Shellei Brondir] 9.5,59.7 Wetlands, `Fly to [F Farholde Keep]` (the game routes it through Thelsamar): TaxiPath 266 (7 -> 8, 110) + 11589 (8 -> 3276, 630). Farholde Keep flight master [TAR257087 Gretchen Mayberry]: the DB has 14 points (x58-63 y78-83, centre 61.1,80.8); the guide uses 60.9,80.9 (38:38).
- **Farholde Keep - Powderfuse Port, both ways on foot:** Friz Frazzlespark 77.1,52.9, Whizzbuzz 79.5,52.7 Riverglades; about 32 units north-east. 41:20 gives the way ("ride back east past the north side of Farholde Keep and up the coast road north-east", road unverified). The port has no flight path (41:6).
- **Farholde Keep - Aerie Peak:** at Gretchen Mayberry, `Fly to [F Aerie Peak]` (the game routes it through Thelsamar and Ironforge): TaxiPath 11588 (3276 -> 8, 630) + 15 (8 -> 6, 110) + 263 (6 -> 43, 730). (Through Refuge Pointe, 8 -> 16 -> 43, costs 1,890.) Aerie Peak flight master [TAR8018 Guthrum Thunderfist] 11.1,46.1 (guide 29:67 uses 11.1,46.2).
- **Bind: Aerie Peak**, on arrival, at [TAR7744 Innkeeper Thulfram] 14.2,41.6 Hinterlands, `[S Aerie Peak]`. Used once: `[H Aerie Peak]` from Skulk Rock (or the escort's end at 79.1,61.4) back to Fraggar and Talonaxe; Astral Recall does the same if the hearth is on cooldown.
- **Out:** at Guthrum Thunderfist, `Fly to [F Ironforge]`: TaxiPath 264 (43 -> 6, 730). Ironforge flight master [TAR1573 Gryth Thurden] 55.5,47.7. The chapter ends in Ironforge; chapter 49 starts there.
- **No Ironforge bind** (Deviation 2): chapter 49 goes Ironforge - Stormwind - Nethergarde - Booty Bay and binds Booty Bay (plan Threads), so an Ironforge bind is never hearthed to. Hearth on exit = Aerie Peak. If the chapter-49 spec wants a hearth to Ironforge, the line is: at [TAR5111 Innkeeper Firebrew] 18.1,51.5 Ironforge, `[S Ironforge]`.
- Flight spending: 730 + 740 + 1,470 + 730 = 3,670c = 36s 70c (TaxiPath cost fields; any reputation discount not applied).

## 4. Route (play order)

### Leg A - Theramore pass and the boat (optional gates only; no counted quest)
1. `[OC]` heading: Theramore, then the boat.
2. `[O]` Only if you carry Alliance Trauma (6625) and First Aid is 225: at [TAR12939 Doctor Gustaf VanHowzen] 67.8,49.0 Dustwallow Marsh, `[QT6625 Alliance Trauma]` (970 XP) and `[QA6624 Triage]` (3,900 XP; req 35, L45; skill row [17] = [129, 225]); do the triage there and `[QT6624]`. Gate: Artisan First Aid (rule 11). Not counted. (qdb row [12] of 6624 is empty; the Classic order Trauma -> Triage is kept, unverified.)
3. `[O]` Only if you carry I Got Nothin' Left! (6609) and Fishing is 225: at [TAR12919 Nat Pagle] 58.6,60.1 Dustwallow Marsh (outside Theramore, about 15 units south-west of the flight master), `[QT6609 I Got Nothin' Left!]` (970 XP) and `[QA6607 Nat Pagle, Angler Extreme]` (3,900 XP at the hand-in; req 35; skill [356, 225]; the four fish are carried out). Gate: Artisan Fishing. Not counted.
4. Take the boat to Menethil Harbor from the Theramore east dock `[G71.5,55.5 Dustwallow Marsh]` (unverified, see section 3).

### Leg B - Powderfuse Port (no fighting)
5. At Shellei Brondir 1571, `Fly to [F Farholde Keep]` `[G9.5,59.7 Wetlands]`.
6. Ride north-east from Gretchen Mayberry (60.9,80.9) to Powderfuse Port (road unverified, 41:20).
7. Turn in **95327 All's Well That Ends Well** (3,150 XP, 0 money; L40, Wowhead reqlevel 36, qdb req empty; side 3) at [TAR255897 Friz Frazzlespark] (L41) `[G77.1,52.9 Riverglades]`. Giver Caravaneer Ruzzgot 3945 (chapter 45). No reward. Plain (required). If Ruzzgot did not offer it in chapter 45 (on the plan's test list), this step and the ride only fire for steps 8-9.
8. `[O]` Only if you carry it: turn in **95472 Consolation Prize** (2,350 XP, 0 money; L40 req 36; fixed reward Sweat-Stained Shirt 270334) at Friz Frazzlespark, same spot. Conditional (Wowhead series after 95321 Tazzik's Dues, conditional).
9. `[O]` Only if you carry it: turn in **97332 Twice Misplaced Trust** (3,300 XP, 0 money; L41 req 36; fixed Jug of Badlands Bourbon 2595, choice of three rings, see Gear) at [TAR259961 Wharfmaster Whizzbuzz] (L45) `[G79.5,52.7 Riverglades]`. Conditional (series after 97331 Zimmix's Great Escape, out).
10. Ride back to Gretchen Mayberry `[G60.9,80.9 Riverglades]`; `Fly to [F Aerie Peak]`.
   - The leg's whole reason is step 7 (required); without 95327 in the log and none of 8-9, skip Leg B and fly Menethil - Aerie Peak instead (Menethil - Ironforge - Aerie Peak, TaxiPath 17 + 263, 1,060c).

### Leg C - Aerie Peak: bind and pickups
11. Bind at [TAR7744 Innkeeper Thulfram] `[S Aerie Peak]` `[G14.2,41.6 The Hinterlands]`.
12. Accept **2988 Witherbark Cages** (3,900 XP, 0 money; L45 req 40; rows [11]/[12] empty) at [TAR5636 Gryphon Master Talonaxe] (L44) `[G9.8,44.5 The Hinterlands]`. Objective (row [9]): check three cages - First Witherbark Cage obj 144066 at 23.3,58.8; Second 144067 at 23.1,58.8; Third 144068 at 32.0,57.3. Plain.
13. Accept **2877 Skulk Rock Clean-up** (4,400 XP, 50s; L48 req 40; no prerequisite) and **2880 Troll Necklace Bounty** (3,900 XP, 65s; L45 req 40; no prerequisite) at [TAR7884 Fraggar Thundermantle] (L60) `[G14.8,44.6 The Hinterlands]`. 2877: kill 10 Green Sludge 2655 and 10 Jade Ooze 2656 (counts from row [7] text; row [9] counts are 0). 2880: bring 5 Troll Tribal Necklaces 9259 (row [7] text; row [9] = item 9259). Both plain. 2880 is a fill quest (overrides_r2.tsv, Braedyn 13 Nov). Take it now so the Witherbark trolls killed at the cages count toward it. 2881 Troll Necklace Bounty (the no-XP repeat Fraggar offers next) is not taken (out: no XP).
14. `[O]` `[A Shaman]` At 44 only: [TAR270263 Farseer Maret Firetend] (L45) `[G14.4,42.6 The Hinterlands]` `[T]` level-44 row (Trainers below). Expected: not 44 yet here; repeated at step 30 and in Ironforge.
15. `[O]` At Leatherworking 200, if not bought in chapter 44: [TAR11097 Drakk Stonehand] `[G13.4,43.5 The Hinterlands]` `[T]` Artisan Leatherworking (spell 10662, 50,000c = 5g, skill 200). Character-level gate unverified. Gate (rule 11).

### Leg D - the Witherbark cages and Rhapsody (mobs 40-45)
16. West village: cages 1 and 2 `[QC2988]` `[G23.2,58.8 The Hinterlands]` (hold with `[QC2988]`; if the writer wants one step per cage, the objective order in row [9] is First, Second, Third). Mobs (qdb): Witherbark Scalper 2649 L40-41 (13 spawns, x22-25 y55-60), Witherbark Zealot 2650 L41-42 (9, same area); Witch Doctor Ti'ik 270772 L49 (not elite in qdb, one spawn within 5 units of the cages): avoid him. Kills here count for 2880: Scalper 28.5% (94/330), Zealot 25.2% (56/222).
17. East village: cage 3 `[QC2988]` `[G32.0,57.3 The Hinterlands]`. Mobs: Witherbark Hideskinner 2651 L42-43 (18, x28-33 y57-61) 30.5% (61/200), Witherbark Venomblood 2652 L43 (8, x30-33 y57-62) 42.5% (34/80) for 2880.
18. North to Rhapsody: turn in **1452 Rhapsody's Kalimdor Kocktail** (3,600 XP, 0 money; L43 req 38; row [12] = [1451], done chapter 44) at [TAR5634 Rhapsody Shindigger] (L44) `[G26.9,48.6 The Hinterlands]` (not in Aerie Peak: about 15 units east). Objective: 3 Roc Gizzard 6257, 3 Groddoc Liver 6259, 3 Ironfur Liver 6258 (row [9]). Plain (required, Braedyn 13 Nov). Accept **1469 Rhapsody's Tale** (2,700 XP at the hand-in; L43 req 38; row [12] = [1452]; ends Brohann Caskbelly 5384, Stormwind 69.5,40.4 - chapter 49, counted there). Mobs near him: Vengeful Spirit 221828 L45 (8 spawns within 5 units; not elite in qdb), Highvale Scout 2692 L44-45 / Marksman 2693 L45-46 / Ranger 2694 L46-47 (x28-33 y43-50, east of him): come from the west.
19. Back to Aerie Peak: turn in **2988** at Talonaxe `[G9.8,44.5 The Hinterlands]`; accept **2989 The Altar of Zul** (4,400 XP, 0 money; L48 req 40; row [12] = [2988]). Objective: "Search the Altar of Zul" (row [8] trigger 48.98,68.66 Hinterlands).

### Leg E - the Altar of Zul, Skulk Rock, the beacon (mobs 45-48)
20. `[OC]` Approach note for the Altar (write it in full): "The Altar of Zul is a troll ziggurat. Come in from the north-west, kill the Vilebranch Axe Throwers on the lower slopes for the necklaces first, then climb, clear the Soothsayers on the stairs and touch the top. The DB puts two level 50 elites, Qiaga the Keeper and Morta'gya the Keeper, on the top beside the trigger: if they are there, do not pull them; step onto the trigger from the side away from them and leave. If they stand on the trigger itself, leave the step for now, finish the necklaces and Skulk Rock, and note it - the Altar is then a group step."
21. Kill for **2880**: `Kill [TAR2639 Vilebranch Axe Thrower] for 5 Troll Tribal Necklaces [QC2880] (~30% - budget ~17 kills, fewer for every necklace from the cages)` `[G46.2,65.5 The Hinterlands]`. Rates from data/drop_rates.json item 9259 per-mob rows (Wowhead Forever item page, 12 Nov):
    - Vilebranch Axe Thrower 2639, L45-46, not elite: 31.9% (23/72); 9 spawns, all at the Altar (x43-50 y62-70), 2.7-6.6 units from the Keepers.
    - Vilebranch Witch Doctor 2640, L46-47, not elite: 51.4% (18/35), but only **one** of its 9 spawns is at the Altar (47.6,69.5, 1.7 units from the Keepers, the closest of the necklace mobs). The other 8 stand at x63-69 y60-70, at the foot of Jintha'Alor among elite Vilebranch Warriors 4465 (L45-46, 19 spawns), Headhunters, Berserkers and Shadowcasters: not used (rule 13).
    - Vilebranch Scalper 4466, L46-47, not elite: 29.9% (206/690); 8 spawns at the Altar (2.9-6.4 units from the Keepers), 4 more beside Skulk Rock (x52-54 y38-40).
    - Vilebranch Soothsayer 4467, L46-47, not elite: 27.0% (184/682); 15 spawns at the Altar, five of them within 1.5 units of the Keepers (on the stairs and top): kill those only if the Keepers are not there. 2 more beside Skulk Rock.
    - Budget: Axe Throwers alone 5 / 0.319 = 16 kills; mixed with Scalpers and Soothsayers about 30%, 17 kills; the cages' Witherbark kills (25-43%) take one or two necklaces off before he gets here. The plan's "13-17" assumed several Witch Doctors at the Altar; there is one (Deviation 3). Still inside the fill test (about 25 or less).
    - Retherokk the Berserker 8216 (L48, rank 4 = rare) stands at 50.5,64.1, next to an Axe Thrower spawn (50.5,64.4): avoid.
    - Elite droppers (Headhunter 2641, Shadowcaster 2642, Berserker 2643 and the rest, Qiaga 7996, Morta'gya 8636) are not targets.
22. The Altar top `[QC2989]` `[G49.0,68.7 The Hinterlands]`. Plain, with the step-20 note. Keepers (qdb npc row [5] = 1, elite, L50): Qiaga the Keeper 7996 at 48.64,68.24 and Morta'gya the Keeper 8636 at 48.77,68.36, 0.3-0.5 units from the trigger (about 11-17 yards at the Classic map scale, unverified), inside a level-50 elite's aggro range at his level. In-game test item; Unsure 1.
23. North to Skulk Rock (about 25 units): **2877** `Kill 10 [TAR2655 Green Sludge] and 10 [TAR2656 Jade Ooze] [QC2877]` `[G51.7,44.5 The Hinterlands]` and `[G54.8,43.2 The Hinterlands]`. Green Sludge 2655 L46-47, 46 spawns x44-60 y39-55; Jade Ooze 2656 L47-48, 45 spawns x45-60 y38-53; not elite. Sludges first (lower). qdb also has a Green Sludge 222978 (L50, 8 spawns near 46,37-40, around the robot): a different id, it does not count. **qdb also places level 50-51 Forever-only creatures across Skulk Rock** (within 5 units of the ooze centres: Fallen Moonkin 221330 L51, about 30 points; Dreadfeather Hippogryph 221312 L51, about 15-20 of its 284 points over x44-74 y22-57; Wyrmkin Starhunter 221325 L51; Wrath Whelp 221326 L51; Doomkin 221333 with level 9999; Dreamwarden Valori 221351 L50; none ranked elite). Whether they are in the open world on Forever is unverified (Unsure 2). Write an `[OC]`: "if level 50-51 dream creatures roam Skulk Rock, work the oozes on the west and south edge (x44-50 y45-55) and leave the rest".
24. `[OC]` The OOX-09/HL Distress Beacon (item 8704) drops at 0.58% per kill over 49 Hinterlands mob types (drop_rates.json, 509 of 87,752 kills, 13 Nov): every mob of this chapter can drop it. Conditional (rule 12, plan); never farmed.
25. `[O]` If the beacon dropped: use it `[UI8704]` and accept **485 Find OOX-09/HL!** (4,400 XP; L48 req 43; quest row [1] = [null, null, [8704]]); turn it in at [TAR7806 Homing Robot OOX-09/HL] (L42) `[G49.4,37.7 The Hinterlands]` and accept **836 Rescue OOX-09/HL!** (5,450 XP at the hand-in; L48 req 43; row [12] = [485]). Escort OOX-09/HL "to the shoreline beyond Overlook Cliff" `[QC836]` (row [8] trigger 79.14,61.36). Ambushers in qdb: Marauding Owlbeast 7808 L46, Vilebranch Ambusher 7809 L47 (not elite; count and timing unverified). The robot's spot has 18 Wyrmkin Starhunters 221325 and 21 Wrath Whelps 221326 (L51) within 5 units in qdb (Unsure 2). 836 is handed in to Oglethorpe Obnoticus 7406, Booty Bay 28.4,76.3, in chapter 49. Written `[UI]` as in round 1 (unverified on Forever, RULES writing rules). Conditional, not counted.
26. `|cFFfff8a3Hearth to [H Aerie Peak]|r` from Skulk Rock or the escort's end (Astral Recall does the same).

### Leg F - Aerie Peak hand-ins
27. Turn in **2877 Skulk Rock Clean-up** (4,400 XP, 50s) and **2880 Troll Necklace Bounty** (3,900 XP, 65s) at Fraggar Thundermantle `[G14.8,44.6 The Hinterlands]`. No item rewards (zone_47 itemchoices / itemrewards empty).
28. Turn in **2989 The Altar of Zul** (4,400 XP) at Talonaxe `[G9.8,44.5 The Hinterlands]`. Accept **2990 Thadius Grimshade** (2,100 XP at the hand-in; L47 req 40; row [12] = [2989]; carries Sharpbeak's Feather 9468 to Thadius Grimshade 8022, Blasted Lands 66.9,19.5 - Nethergarde, chapter 49, counted there). Chain: 2988 > 2989 > 2990 > 2991 Nekrum's Medallion (Zul'Farrak, chapter 51; handed in chapter 52).
   - If the Altar step could not be done (Keepers on the trigger): 2989 stays in the log, 2990 is not offered; say so in the step and leave it to the main session (Unsure 1).
29. `[O]` `[A Shaman]` At 44, if not bought at step 14: Firetend `[T]` level-44 row `[G14.4,42.6 The Hinterlands]`.
30. At Guthrum Thunderfist `Fly to [F Ironforge]` `[G11.1,46.2 The Hinterlands]`.

### Leg G - Ironforge (end)
31. `[O]` `[A Shaman]` At 44, if not bought at Firetend: [TAR258098 Eldrun Stormbreaker] `[G47.1,13.8 Ironforge]` `[T]` level-44 row. Expected exit level 43.8: most likely the row waits for chapter 49's Ironforge start or a later stop (plan Threads: Ironforge 48 and 49).
32. `[O]` At Skinning 200, if not bought at 40 (39d:21): [TAR6291 Balthus Stoneflayer] `[G39.9,32.5 Ironforge]` `[T]` Artisan Skinning (spell 10768, 50,000c = 5g). Gate.
33. `[O]` At First Aid 225, if not carried: [TAR5150 Nissa Firestone] `[G55.1,58.3 Ironforge]` `[QA6625 Alliance Trauma]` (req 35; ends VanHowzen, Theramore: chapter 50's Theramore pass). At Fishing 225, if not carried: [TAR5161 Grimnur Stonebrand] `[G48.1,6.9 Ironforge]` `[QA6609 I Got Nothin' Left!]` (req 35; ends Nat Pagle, Dustwallow: chapter 50). Gates, not counted.
34. End Check (section 7). No bind (section 3).

## Trainers / vendors (prices: tooling/trainer_costs.json, pulled 12 Nov, Wowhead raw values)
- Level-44 row, identical at Firetend 270263 and Eldrun 258098: Lightning Bolt R8 (10392) 1g 80s; Stoneskin Totem R5 (10407) 1g 80s; Lesser Healing Wave R4 (10466) 1g 80s; Nature Resistance Totem R2 (10600) 1g 80s; Rockbiter Weapon R6 (16315) 1g 80s. Total 9g. (Raw or 5% off: round-wide test item.)
- Artisan Leatherworking (10662) at Drakk Stonehand 11097: 5g, skill 200. Artisan Skinning (10768) at Balthus Stoneflayer 6291: 5g, skill 200.
- No vendor purchase. Money in: 1g 15s (2877 50s, 2880 65s). Money out: flights 36s 70c; training 9g if 44; Artisan ranks 5g each if bought. tooling/gold.py covers chapters through 41 only: no gold line computed here.

## 5. Gear calls (band 40, central [conservative]; tooltips weights/tooltips/2026-11-12.json)
- 836 Rescue OOX-09/HL! (conditional; choice at the hand-in in Booty Bay, chapter 49 - listed here for the chapter-49 writer): Gnomish Inventor Boots 9645 (cloth feet +7 Sta +2 Int +11 Spi) 30.9 [19.9] over Gnomish Floatation Device 270101 (leather feet +10 Str +10 Sta) 20.0 [20.0]; Gnomish Water Sinking Device 9646 is plate (-5 Agi +16 Sta), unusable. Southsea Mojo Boots 20641 (cloth feet +11 Int, +8 spell damage; 8366 Southsea Shakedown, required in chapter 46) score 34.6 [26.6]: with them on, none of the three is an upgrade; take the Water Sinking Device for its sell price (67s 91c, against 67s 68c and 64s 34c).
- 97332 Twice Misplaced Trust (conditional): Apology Ring 278019 (+6 Sta, +4 spell damage) 8.0 [4.0] over Renegotiated Ring 278018 (+3 Str +6 Sta) 6.0 [6.0] and Refunded Ring 278017 (+8 Sta) 0.0. Central pick Apology Ring; it is an upgrade only over an empty or weaker ring slot (write "if a ring slot is empty or weaker"). Fixed: Jug of Badlands Bourbon 2595 (drink).
- 95472 Consolation Prize: Sweat-Stained Shirt 270334, shirt, no stats, sells 55s (fixed).
- No reward on 95327, 1452, 1469, 2988, 2989, 2990, 2877, 2880, 485 (zone_47 / zone_16591 itemchoices and itemrewards empty; 2877 and 2880 pay money only).

## 6. Out / not here (silent in the Lua; reasons from _decisions.tsv)
- 2881 Troll Necklace Bounty - OUT: no XP, nothing kept behind it.
- 2994 Saving Sharpbeak - OUT: elite outside a dungeon (rule 13): Vile Priestess Hexx (51 elite) at the top of Jintha'Alor.
- 4787 The Ancient Egg - OUT: the Ancient Egg (Hinterlands 57.6,86.8) is guarded by Hitah'ya the Keeper and Vilebranch Aman'zasi Guards (51 elite) - rule 13; it also needs The Prophecy of Mosh'aru.
- 86616 Repurposed Totems - LATER: needs level 45 at Aerie Peak; round 3's return to Aerie Peak. Not written, not even as an "if 45" line (prompt).
- 2963 Portents of Uldum, 3448 Passing the Burden, 3450 An Easy Pickup, 3451 Signal for Pickup - need level 45; chapter 52. Not written here (prompt).
- 2993 Return to the Hinterlands - LATER (round 3). 2992 The Divination - chapter 52. 1450 / 1451 were chapter 44.
- Not taken here though their givers stand on the route: 2861 Tabetha's Task (Bink, Ironforge: chapter 49 starts in Ironforge, plan note), 2769 The Brassbolts Brothers (Klockmort, Ironforge; conditional in chapter 51), 98233 Sword in the Slime (Guard Jameson, Theramore: chapter 50's Theramore pass).

## 7. End check
`[OC]Check:` handed in here: All's Well That Ends Well (95327), Rhapsody's Kalimdor Kocktail (1452), Witherbark Cages (2988), Troll Necklace Bounty (2880), Skulk Rock Clean-up (2877), The Altar of Zul (2989); if carried: Consolation Prize (95472), Twice Misplaced Trust (97332); if the beacon dropped: Find OOX-09/HL! (485); gates 6625/6624 and 6609 if carried. In the log, carried out: Rhapsody's Tale 1469 (Brohann, Stormwind, chapter 49); Thadius Grimshade 2990 (Nethergarde, chapter 49); Rescue OOX-09/HL! 836 with the escort done, if the beacon dropped (Oglethorpe, Booty Bay, chapter 49); 6607 Nat Pagle (fish) if taken; 6625 / 6609 if picked up in Ironforge (chapter 50's Theramore pass). Still in the log from earlier chapters and not touched here: whatever chapters 45-47 carry for later (Deliver to MacKinley 2874, Voodoo Dues 609 if taken, the OOX-22/FE rescue 2767 if its beacon dropped). Hearth = Aerie Peak. You stand at Gryth Thurden in Ironforge; chapter 49 starts here.

## 8. Totals
| | count | XP | money |
|---|---|---|---|
| Required (95327 3,150; 1452 3,600; 2880 3,900; 2988 3,900; 2877 4,400; 2989 4,400) | 6 | 23,350 | 1g 15s (2877 50s + 2880 65s) |
| Optional / conditional (95472 2,350; 97332 3,300; 485 4,400; 836 5,450) | 4 | 15,500 | 0 |
Equals the plan's XP table row for chapter 48 (6, 23,350, 1g 15s; optional 15,500). Note: 836's 5,450 XP is earned at its hand-in in Booty Bay (chapter 49) although the plan lists it here, as an optional. 1469 (2,700) and 2990 (2,100) are picked up here and counted in chapter 49. Gates (6625/6624 4,870, 6609 970, 6607 3,900) not counted.

## 9. Unverified / in-game test list
- The Altar of Zul: are Qiaga the Keeper 7996 and Morta'gya the Keeper 8636 (L50 elite) on the top, and can a level 43-44 touch the trigger without pulling them (plan test list).
- Skulk Rock and the OOX robot: are the level 50-51 Forever-only creatures of qdb (Fallen Moonkin 221330, Dreadfeather Hippogryph 221312, Wyrmkin Starhunter 221325, Wrath Whelp 221326, Doomkin 221333, Dreamwarden Valori 221351) in the open world.
- Only one Vilebranch Witch Doctor at the Altar (qdb): necklace pace from the Axe Throwers.
- Theramore - Menethil boat (plan test list); the Farholde Keep - Powderfuse Port road (41:20).
- Whether Ruzzgot offers 95327 after The Big Payback (plan test list).
- Witch Doctor Ti'ik 270772 (L49) at the west cages: hostile or not.
- Drakk Stonehand's character-level gate for Artisan Leatherworking.
- Trainer price raw or 5% off (round-wide).
- OOX-09/HL escort: ambush count and mobs (Classic knowledge).
- `[UI8704]` on the Forever build (RULES: in use, unverified).

## Needs pull
- Wowhead Forever NPC pages 7996 and 8636 (map: where the Keepers stand on Forever).
- Wowhead Forever NPC pages 221330 / 221312 / 221325 (zone, phase, whether they are an event).
- Wowhead Forever NPC 2640 (map: Witch Doctor spawns at the Altar).

## Unsure
1. The Altar of Zul trigger sits 0.3-0.5 units from two level-50 elites in qdb (draft2's Unsure 1, kept as an in-game test per the prompt). If they stand on the top in game, 2989 is in practice a GROUP step (rule 13), and with it 2990 (chapter 49), Nekrum's Medallion and The Divination (chapters 51-52): the main session's call; the spec writes the approach note and a "leave it and note it" branch, nothing more. The necklace mobs (Axe Throwers, Scalpers) stand clear of them (2.7-6.6 units); the one Witch Doctor at 1.7 units and five Soothsayers within 1.5 units do not.
2. Level 50-51 Forever-only creatures (221xxx ids) cover Skulk Rock and the robot's spot in qdb. If they are there and hostile, the required 2877 (and the conditional escort) at level 43-44 are dangerous. Not changed here.
3. If 1452's nine items are not all in the bags (budgets in chapters 46-47), 1452 and 1469 cannot be handed in / taken here; the next Kalimdor passes are chapter 50 (Feralas livers) and 53 (Tanaris gizzards), and the next Aerie Peak visit is round 3. Not settled by this spec.
4. Which earlier Ironforge stop took 6609 / 6625 (decides whether steps 2-3 fire at all).

## 10. Deviations from the route plan
1. **Leg order (b)**, Farholde Keep and Powderfuse Port before Aerie Peak, where the plan note reads Aerie Peak first ("Then Farholde Keep and the ride to Powderfuse Port"). Reason: equal flights, 330c cheaper (TaxiPath cost fields), and 3,150-8,800 XP of hand-ins before the 45-48 mobs. The prompt left the choice to the spec.
2. **No Ironforge bind.** The plan's Threads propose "Aerie Peak, then Ironforge, in 48"; chapter 49 binds Booty Bay and never hearths to Ironforge on the plan's route, so the second bind buys nothing. Hearth on exit = Aerie Peak. The one-line Ironforge bind is given in section 3 if the chapter-49 spec needs it.
3. **Troll Necklace Bounty budget 16-17 kills, not 13-17**: drop_rates.json has the Witch Doctor at 51% but qdb has only one of its nine spawns at the Altar (47.56,69.49); the others stand among Jintha'Alor's elites. The budget rests on the Axe Throwers (31.9%, 9 spawns), Scalpers (29.9%) and Soothsayers (27.0%) at the Altar, helped by the cages' Witherbark trolls (25-43%). Still a fill under the plan's test (about 25 or less). No list change.
4. **836 Rescue OOX-09/HL! XP falls in chapter 49** (its ender Oglethorpe 7406 is in Booty Bay, quest row [2]); the plan lists it as an optional of 48. Optional, so no effect on the required totals.
