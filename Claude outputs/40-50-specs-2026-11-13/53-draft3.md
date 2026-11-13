# Spec 53 - Tanaris II and Uldum (drafted 13 Nov 2026, round 2 of the 30-60 guide, second revision)

Data used (all read 13 Nov 2026): `tooling/qdb` = QuestieDB Forever 1.0.16 (quest/npc/object/item.json; `python tooling/qinfo.py`, own spawn scripts on npc row [6] / object row [3]); `data/zone_440.json` (Wowhead XP, money, reward choices); `data/drop_rates.json` (8587 dated 12 Nov, 8623 dated 13 Nov); `data/wowhead_quest_links.json` (97540 only; the other quests of the chapter are not in it); `data/browser/r2_pages*_2026-11-1*.tsv` (QUEST 97540, ITEM 8587, NPC 12046); `nether.wowhead.com/forever/tooltip/` pulled 13 Nov for quests 97540, 1560, 2954, 2946, 3161, 2741 and items 9978, 6064, 8594, 9507; `weights/tooltips/2026-11-12.json` scored with `weights/score_items.py` functions at `--band 40`; `tooling/client/1.60.1.70938/TaxiNodes.csv` / `TaxiPath.csv`; `tooling/trainer_costs.json` (12 Nov); plan `docs/40-50-plan-2026-11-12.md` (second revision) and `docs/40-50-route-2026-11-12.txt` (`route_xp.py` re-run 13 Nov: row 53 = 12 quests, 45,130 XP, 1g 95s, optional 9,850); pool `Claude outputs/40-50-plan-2026-11-12/pool/440_Tanaris.txt` and `_decisions.tsv`; format models `32_Dustwallow.lua` (boat and Theramore markers), `46-draft2.md` (Gadgetzan facts, re-checked here).

## 1. Header
- File: `53_TanarisII.lua`
- `[N 45-47 Tanaris]`
- `[NX 46-47 Maraudon]` (chapter 54's title in the plan)
- `[GA Alliance]`; footer group "Forever Shaman 30-60".
- `[D ...]`: "Menethil to Theramore by boat, Theramore to Gadgetzan by air. The Explorers' League at the Uldum pedestal, the Dunemaul compound and Marvon's Gahz'ridian ornaments, the Noxious Lair and the silithid chain, Thistleshrub Valley and Tooga's walk home to Torta. Handle With Care and Rise of the Silithid go on to Darnassus."
- Level on entry **45.6**, exit **46.1** (plan XP table).
- **Level-check line (first `[OC]`):** "This chapter wants level 47 for its mobs: Dunemaul ogres 46-48 and Gor'marok 49, the Centipaar of the Noxious Lair and the Hazzali of the Gaping Chasm 47-50, Thistleshrub Valley 48-50. Every quest here can be taken at 45 (The Stone Watcher, Seeing What Happens and Thistleshrub Valley need 45, the rest 39-44). The legs run lowest first: the Dunemaul compound and the ornaments, then the Uldum pedestal (talk only, but level 48-49 elite Dune Smashers stand beside it), then the Noxious Lair, Thistleshrub Valley with Tooga, and the Gaping Chasm last. Under 46: kill Gor'marok last in the compound and pull the Thistleshrub Rootshapers (49-50) one at a time."
  - Highest required level among the pickups: 45 (2946 carried in, 2954, 3362). Highest mob level: 50 (Centipaar Swarmer/Sandreaver, Hazzali Swarmer/Stinger, Thistleshrub Rootshaper). The plan's "wants 47" is mob-driven.
  - No quest is under-level at 45.6 (required levels enforced: all twelve open on entry), so nothing waits.

## 2. Entry state (assumed; main session to reconcile)
- Stands at **Menethil Harbor**, end of chapter 52. Hearth: **Ironforge** (chapter 52's bind, per the prompt).
- Flight points needed: Theramore (`[P Theramore]` 32_Dustwallow.lua:28) and **Gadgetzan** (taken on foot in chapter 46: `[P Gadgetzan]` at Bera Stonehammer, assumed from the 46 draft).
- Quests carried in:
  - **2946 Seeing What Happens** (from Historian Karnik [2916], Ironforge 77.5,11.8, chapter 52, after 2963 Portents of Uldum; carries the Miniature Platinum Discs [6064], quest row [10]).
  - **3449 Arcane Runes** (Tymor, chapter 52; for Azshara, chapter 55) - untouched here.
  - **2741 The Super Egg-O-Matic with the Hippogryph Egg [8564]** - only if chapter 46 took it at the Egg-O-Matic and chapter 47 or 50 looted the egg in Feralas (see Deviation D1). If not carried, see D1.
  - Optional gates, only if chapter 52 took them in Ironforge at skill 225: **6625 Alliance Trauma** (Nissa Firestone [5150], Ironforge 55.1,58.3), **6609 I Got Nothin' Left!** (Grimnur Stonebrand [5161], Ironforge 48.1,6.9). **6610 Clamlette Surprise** only if chapter 46 took it at Cooking 225 (chapter 46's spec: optional Cooking 225 pickup at Dirge Quikcleave).
  - Chapter 51 (Zul'Farrak, before this chapter) handed in Screecher Spirits and ran the dungeon. 3161 Gahz'ridian gates nothing there: no quest names 3161 in rows [11]/[12], and 2770 Gahz'rilla (Wizzle Brassbolts) has no prerequisite. No re-run.
  - 82 Noxious Lair Investigation: this spec picks it up here (the 46 draft left it for chapter 53). If chapter 46's final spec took it, the pickup line falls away.
- Training: none. No shaman trainer in Dustwallow or Tanaris (plan Threads: chapters 53-56 pass no shaman trainer; the 46/48 rows wait for chapter 57).

## 3. Travel and hearth
- **In:** Menethil Harbor - boat to Theramore. Pier and landing copied from round 1: "Take the boat to Theramore from the far south-west pier" `[G5.6,63.2 Wetlands]` (32_Dustwallow.lua:25; boat or portal still marked unverified there); land on the Theramore east dock (71.5,55.5).
- **Theramore:** flight master **Baldruc [4321]** `[G67.5,51.3 Dustwallow Marsh]` (npc row [6]: 67.48,51.30). Fly **Theramore - Gadgetzan**: TaxiPath 222 (node 32 -> 39), Cost field 730 (7s 30c; whether the game charges this raw value is unverified). Return path 201 (39 -> 32) cost 630.
- **Gadgetzan:** flight master Bera Stonehammer [7823] L55 elite (guard-type), 51.0,29.3 Tanaris. Innkeeper **Fizzgrimble [7733]** 52.5,27.9 Tanaris: bind `[S Gadgetzan]` (plan Threads: Gadgetzan for 53, 54 and 56).
- **Hearth used once**, in Leg D from the Gaping Chasm back to Gadgetzan `[H Gadgetzan]` (saves a ~45-unit ride; if on cooldown, ride north). Cooldown length on Forever unverified.
- **Out:** the chapter ends in Gadgetzan, bound there. Chapter 54 flies Gadgetzan - Theramore - Nijel's Point (plan).
- Roads in Tanaris are not in the data; all leg distances below are straight-line map units.

## 4. Route (play order)

### Leg A - boat, Theramore gates, Gadgetzan (pickups, bind)
1. `[OC]` level-check line (section 1).
2. Take the boat to Theramore `[G5.6,63.2 Wetlands]` (travel; unverified as in round 1).
3. `[O]` First Aid 225 only, if you carry 6625: at [TAR12939 Doctor Gustaf VanHowzen] `[QT6625 Alliance Trauma]` (970 XP) `[QA6624 Triage]` (3,900 XP; req 35, quest row [17] = First Aid (129) 225; you get Triage Bandages [16991]; "save 15 patients before 6 of them die", trigger "15 Patients Saved!" at 67.79,49.06) then `[QC6624]` and `[QT6624]` on the spot `[G67.8,49.0 Dustwallow Marsh]`. Gate line (rule 11: profession rank). Not counted.
4. `[O]` Fishing 225 only, if you carry 6609: swim to Nat Pagle's island south of Theramore: at [TAR12919 Nat Pagle] `[QT6609 I Got Nothin' Left!]` (970 XP) `[G58.6,60.1 Dustwallow Marsh]`. Whether to also accept 6607 Nat Pagle, Angler Extreme (3,900 XP; req 35, Fishing 225, row [17] = [356, 225]; four fish from four fishing-location objects: Feralas Ahi Feralas 62.8,51.6; Misty Reed Mahi Mahi Swamp of Sorrows 87.1,61.4; Sar'theris Striker Desolace 28.8,62.1; Savage Coast Blue Sailfin Stranglethorn 28.5,34.6) depends on which strands the later chapters pass: see Unsure U5. Not counted. ~12 units each way from the flight master; Nat Pagle's trainer list on Wowhead is empty (trainer_costs.json 12 Nov), so no price.
5. At flightmaster [TAR4321 Baldruc], fly to Gadgetzan `[G67.5,51.3 Dustwallow Marsh]` (7s 30c).
6. At [TAR7733 Innkeeper Fizzgrimble], bind `[S Gadgetzan]` `[G52.5,27.9 Tanaris]`.
7. If you carry the Hippogryph Egg: at the Egg-O-Matic (object 142071) `[QT2741 The Super Egg-O-Matic]` (4,200 XP; req 42, L47; objective Hippogryph Egg [8564] x1, nether tooltip; fixed reward Egg Crate [8647], no stats) `[G52.4,27.0 Tanaris]`. Plain in the plan; see D1. The egg follow-ups (8893, 2747-2750) get no tag.
8. At [TAR7724 Senior Surveyor Fizzledowser] `[QA82 Noxious Lair Investigation]` (3,150 XP + 50s at the hand-in; req 39, L47; prerequisite 992 Gadgetzan Water Survey, quest row [12] = [992], handed in chapter 46; "Bring five Centipaar insect parts from the Noxious Lair to Alchemist Pestlezugg") `[G50.2,27.5 Tanaris]`. Plain with the budget (Braedyn, 13 Nov).
9. At [TAR11758 Andi Lynn] `[QA5863 The Dunemaul Compound]` (4,550 XP; req 44, L49; kill 10 Dunemaul Brutes, 10 Dunemaul Enforcers and Gor'marok the Ravager - counts from the quest text, row [7]; qdb row [9] carries no counts) `[G52.8,27.4 Tanaris]`. Plain.
10. At [TAR7876 Tran'rek] `[QA3362 Thistleshrub Valley]` (4,700 XP + 75s; req 45, L50; kill 8 Gnarled Thistleshrubs and 8 Thistleshrub Rootshapers, quest text) `[G51.6,26.8 Tanaris]`. Plain.
11. At [TAR7763 Curgle Cranklehop] `[QA3022 Handle With Care]` (2,100 XP + 50s at the hand-in, chapter 55; req 42, L47; you get A Carefully-packed Crate [9507], quest row [10]; ends at Erelas Ambersky [7916], Teldrassil 55.5,92.0 = Rut'theran) `[G52.4,26.9 Tanaris]`. Counted in chapter 55; carried out.
12. `[O]` Cooking 225 only: at [TAR8125 Dirge Quikcleave] hand in `[QT6610 Clamlette Surprise]` if you carry it with its items, or take it `[QA6610]` and do it, only at Cooking 225 (chapter 46 left it as an optional Cooking 225 pickup) (3,900 XP; req 35, row [17] = Cooking (185) 225; 12 Giant Eggs, 10 Zesty Clam Meat, 20 Alterac Swiss; fixed reward Clamlette Surprise [16971]) `[G52.6,28.1 Tanaris]`. Gate line (rule 11). Giant Eggs [12207] also drop from the Tanaris Rocs (item row [1] includes 5428, 5429, 5430; no rate in the data). Not counted.

### Leg B - south: Marvon, the ornaments, the Dunemaul compound, Uldum (mobs 43-49; elites at the pedestal)
13. Ride south ~18 units: at [TAR7771 Marvon Rivetseeker] `[QA3161 Gahz'ridian]` (4,400 XP at the hand-in; req 43, L48; collect 30 Gahz'ridian Ornaments [8443]; you get the Gahz'ridian Detector [9978], quest row [10]) `[G52.7,45.9 Tanaris]`. Plain.
14. `[OC]` Equip the Gahz'ridian Detector in the head slot (nether tooltip 9978: Head, "Equip: Nearby Gahz'ridian appears on the minimap"); swap your helm back when the 30 are in. The Gahz'ridian (object 140971) are ground objects: 105 spawn points (about 90 distinct spots) over the central desert x36-58 y24-78. On this leg: 6 around Marvon (x50-56 y43-49), 16 east of the compound (x44-49 y59-68), 5 in the north camp (x36-44 y50-60), 16 around the south camp (x38-44 y68-79); 18 more lie in the desert round Gadgetzan (x36-58 y24-40) for the later legs. How many ornaments one mound gives is not in the data.
15. Collect Gahz'ridian Ornaments on the way south-west `[CI8443,30]` `[G46.5,64.0 Tanaris]` (held by the item count; it completes the moment you have 30, wherever that is).
16. Dunemaul Compound, north camp (x37-43 y50-60): kill [TAR5474 Dunemaul Brute] (46-48, not elite; 30 spawns, 24 of them here) and [TAR5472 Dunemaul Enforcer] (46-47; 25 spawns, 18 here), 10 of each `[QC5863]` `[G40.5,55.5 Tanaris]`. Dunemaul Warlocks (47-48), Ogre Mages (46-47) and Ogres (45-46) stand among them (not on the quest). Rares in the camp: Cyclok the Mad [8202] 48 (41.3,54.7), Omgorn the Lost [8201] 50 (38.7,55.6), both rank 4 (rare, not elite).
17. Kill [TAR12046 Gor'marok the Ravager] (level 49; qdb rank blank, Wowhead page facts list no elite tag - the plan reads Normal; one spawn 41.5,57.8, Wowhead map 41.0-41.6,57.4-57.8) `[QC5863]` `[G41.5,57.8 Tanaris]`. Under 46: do him last.
18. South camp (x38-42 y70-75): more ornaments; 4 Brutes and 4 Enforcers here if the north camp ran short.
19. `[OC]` |cFFFF0000Danger:|r the Uldum pedestal (37.6,81.4) stands among six **Dune Smashers [5469], level 48-49, elite** (npc row [5] = 1): spawns 37.17,81.3 (0.5 from the pedestal), 37.64,80.61 (0.8), 36.67,80.62, 37.15,79.92, 37.12,79.64, 36.69,79.16 - all to the north and west of the pedestal. Come in from the south-east, do the three steps below and leave the same way. See Deviation D2.
20. At the Uldum Pedestal (object 142343) `[QT2946 Seeing What Happens]` (4,700 XP; req 45, L50; prerequisite 2963 in row [12]) `[G37.8,81.6 Tanaris]`.
21. Talk to the [TAR7918 Stone Watcher of Norgannon] (level 60, faction 35, gossip flags "AH": a friendly NPC, not fought) and `[QA2954 The Stone Watcher]` (4,700 XP; req 45, L50; prerequisite 2946, row [12] = [2946, 2966]; objective "Learn the purpose of the Stone Watcher of Norgannon", nether tooltip; QuestieDB stores it as a creature objective on 7918, which is where the pool's "mobs to 60" flag comes from), go through his dialogue `[QC2954]` `[G37.6,81.4 Tanaris]`. The quest is given by the Watcher or the pedestal (row [1] = 7918 / object 142343).
22. At the Uldum Pedestal `[QT2954]` (4,700 XP) `[QA2977 Return to Ironforge]` (470 XP at the hand-in, chapter 57; req 45; prerequisite 2954; ends at Historian Karnik, Ironforge 77.5,11.8) `[G37.8,81.6 Tanaris]`. Carried out to chapter 57. (2967 Return to Thunder Bluff is the Horde twin: no tag.)

### Leg C - west: the Noxious Lair, Thistleshrub Valley, Tooga home to Torta (mobs 47-50)
23. Ride north ~37 units to the Noxious Lair (x30-37 y38-51). Kill Centipaar for 5 Centipaar Insect Parts [8587] `[QC82]` `[G33.6,44.5 Tanaris]` - "(drop quest, ~51% - budget ~10 kills; Wasps, Stingers and Swarmers drop best)". Targets: [TAR5455 Centipaar Wasp] 47-48 (26 spawns; 122/210 = 58.1%), [TAR5456 Centipaar Stinger] 48-49 (36; 116/212 = 54.7%), [TAR5457 Centipaar Swarmer] 49-50 (22; 48/82 = 58.5%); poorer droppers Centipaar Worker 48-49 (20; 36.4%), Sandreaver 49-50 (8; 31.3%), Tunneler 47-48 (13; 14.5%) (`drop_rates.json` per-mob rows, 12 Nov; overall 312/615 = 50.7%; budget 5 / 0.507 = 9.9). Rare: Soriid the Devourer [8204] 50, rank 4, 34.1,44.7. Rule 12: 30-60% would be `[O]`; Braedyn kept it plain with the budget (answer 2, 13 Nov), because the chain behind it is required.
24. Ride south ~21 units to Thistleshrub Valley (x27-31 y60-70): kill [TAR5490 Gnarled Thistleshrub] (48-49; only 8 spawns) x8 and [TAR5485 Thistleshrub Rootshaper] (49-50; 11 spawns) x8 `[QC3362]` `[G29.3,65.5 Tanaris]`. Eight of eight Gnarled spawns means waiting for respawns. Thistleshrub Dew Collectors (47-48, 14 spawns) and Glasshide Petrifiers (48-49) are in the valley too (not on the quest).
25. At [TAR5955 Tooga] (level 45; 4 spawn points 29.5,60.5 / 30,65 / 30,70 / 31.8,74.2 - he wanders the valley) `[QA97540 Oasis]` (3,550 XP; Wowhead: requires level 40, side Both, start and end Tooga, "Not sharable", series none, added 1.60.1.70862; qdb row [3] blank, rows [9]/[11]/[12] empty; text "Show the newly quenched Tooga the way back to his wife, Torta.") and `[QA1560 Tooga's Quest]` (5,900 XP; req 40, L50; "Lead Tooga to Torta", nether tooltip; no prerequisite) `[G30.0,65.0 Tanaris]`. Both plain in the plan. What Oasis asks for beyond its text is not in any data we hold: see Unsure U1 and Needs pull.
26. `[OC]` Escort: lead Tooga north-east to Torta near Steamwheedle Port (~53 units, the line passes about 51,42 east of Marvon). Stay close; ambushes, his speed and any timer are unverified (no timer field in the data). Kill-free otherwise; the desert on the way is 40-48.
27. At [TAR6015 Torta] `[QT1560 Tooga's Quest]` (5,900 XP; gear call G1) `[G66.6,25.7 Tanaris]`. Then `[QT97540 Oasis]` at [TAR5955 Tooga] if he stands beside her (3,550 XP) `[G66.6,25.7 Tanaris]` - unverified where Oasis is handed in (U1).
28. Ride west ~15 units to Gadgetzan, through the desert ornaments if the count is short.
29. At [TAR5594 Alchemist Pestlezugg] `[QT82]` (3,150 XP + 50s) `[G50.9,27.0 Tanaris]`.
30. At [TAR7724 Senior Surveyor Fizzledowser] `[QA10 The Scrimshank Redemption]` (4,400 XP; req 39, L48; prerequisite 82, row [12]; Scrimshank's Surveying Gear [8593] from object 144053) `[G50.2,27.5 Tanaris]`. Plain.
31. At [TAR11758 Andi Lynn] `[QT5863]` (4,550 XP; gear call G2) `[G52.8,27.4 Tanaris]`; at [TAR7876 Tran'rek] `[QT3362]` (4,700 XP + 75s) `[G51.6,26.8 Tanaris]`.

### Leg D - south-east: Marvon, the Gaping Chasm (mobs 47-50), the silithid chain
32. Ride south ~18 units: at [TAR7771 Marvon Rivetseeker] `[QT3161 Gahz'ridian]` (4,400 XP; gear call G3) `[G52.7,45.9 Tanaris]`. Take the Detector off and the helm back on.
33. Ride south-east ~25 units into the Gaping Chasm (Hazzali hive, x53-57 y68-74): loot Scrimshank's Surveying Gear (object 144053, one spawn 55.96,71.17) `[QC10]` `[G56.0,71.2 Tanaris]`. In the way: Hazzali Tunneler 48-49 (18 spawns, 55.1,71.4), Worker 47-48 (22), Wasp 47-48 (28), Swarmer 49-50 (24), Sandreaver 48 (18), Stinger 49-50 (10); rare Haarka the Ravenous [8205] 50, rank 4, 53.3,73.8. No quest kills here.
34. `[O]` Conditional: **if an OOX-17/TN Distress Beacon [8623] has dropped** (any of 82 Tanaris mob types, every mob of this chapter included; 0.41% per kill, 1,085 of 263,968, Wowhead item page 13 Nov): right-click it `[QA351 Find OOX-17/TN!]` (req 43), ride to [TAR7784 Homing Robot OOX-17/TN] (one spawn 60.2,64.7, ~8 units north-east of the chasm) `[QT351]` (4,400 XP) `[QA648 Rescue OOX-17/TN!]` (5,450 XP at the hand-in; req 43; prerequisite 351) `[G60.2,64.7 Tanaris]`, then escort the robot to Steamwheedle Port (escort route and ambushes unverified). 648 is handed in to Oglethorpe Obnoticus [7406] in Booty Bay (Stranglethorn 28.4,76.3): **no Booty Bay visit is left in round 2, so the rescue is carried to round 3** (rule 9: it stays in the log, named in the end Check). If the escort is skipped, take 648 and keep it (the robot waits) - or leave the beacon unopened; both satisfy rule 9. A beacon that drops after this leg stays in the bags for round 3. Not counted (plan: conditional).
35. Hearth to Gadgetzan `[H Gadgetzan]` (ride ~45 units if it is on cooldown).
36. At [TAR7724 Senior Surveyor Fizzledowser] `[QT10]` (4,400 XP) `[QA110 Insect Part Analysis]` (440 XP; req 39; prerequisite 10) `[G50.2,27.5 Tanaris]`.
37. At [TAR5594 Alchemist Pestlezugg] `[QT110]` (440 XP) `[QA113 Insect Part Analysis]` (440 XP + 70s at the hand-in; prerequisite 110; you get the Insect Analysis Report [8594]) `[G50.9,27.0 Tanaris]`.
38. At [TAR7724 Senior Surveyor Fizzledowser] `[QT113]` (440 XP + 70s) `[QA162 Rise of the Silithid]` (5,700 XP at the hand-in, chapter 55; req 39; prerequisite 113; carries the Insect Analysis Report [8594]; ends at Gracina Spiritmight [7740], Darnassus 41.8,85.6) `[G50.2,27.5 Tanaris]`. Counted in chapter 55; carried out. Its follow-up 4493 March of the Silithid (req 50) is not taken in round 2.
39. `[OC]` Check (section 7).

## 5. Gear calls (level-40 band, tooltips 2026-11-12.json, `score_items.py` functions; central [conservative])
- **G1 - 1560 Tooga's Quest:** neither is an upgrade. Chelonian Cuffs [9638] (mail wrist +4 Sta +10 Int; 16.9 [16.9]) lose to the Arathi Armbands he has worn since chapter 29 (leather wrist +7 Str +5 Agi; 19.6 [19.6]); Band of the Great Tortoise [9642] is a ring with +120 armour only (0.0). Take the Cuffs to sell (68s 75c against 20s 92c).
- **G2 - 5863 The Dunemaul Compound:** take **Rugwood Mantle** [16739] (leather shoulder +11 Int +4 Spi +7 SP; 42.6 [31.6]). It replaces Inquisitor's Shawl (36.0 [29.0]), Failed Flying Experiment (31.2 [31.2], chapter 47 if the OOX-22 beacon dropped) or Palm Frond Mantle (26.8 [20.8]); against Mantle of Doan (44.1 [29.1]) it is a side-grade (lower central, higher conservative): keep Doan. Runner-up Witherseed Gloves [16738] (cloth hands +13 Spi +8 SP; 48.5 [27.5]) lose to the Prisoner Handwraps of chapter 40 (60.0 [33.0]); they beat the Traveled Gloves (40.0 [29.0]) on central only. Sell: Mantle 73s, Gloves 38s 93c.
- **G3 - 3161 Gahz'ridian:** take **Surveyor's Tunic** [10827] (leather chest +11 Str +15 Spi; 59.5 [44.5]). It beats Doomsayer's Robe (57.0 [33.0], chapter 39e), Intrepid Explorer's Chainmail (53.4 [37.4]) and Blackwater Tunic (51.5 [36.5], chapter 49). Runner-up Staff of Lore [10826] (two-hand staff 27.58 dps, +5 Int +18 Spi +40 SP; 519.6 [461.6]) loses to every two-hander he can hold: Bigger Rock on Bigger Stick (604.5, chapter 43), Bonebiter (583.5), Rage of the Storm (529.8). The Staff sells for more (2g 55s 1c against 1g 2s 38c), but the Tunic is the upgrade.
- **648 Rescue OOX-17/TN! (conditional, hand-in round 3):** Reloading Assist Armbands [270103] (mail wrist +10 Agi +5 Spi; 23.7 [18.7]) over Projectile Redirectors [270102] (leather wrist +5 Str +10 Agi; 21.2 [21.2]); both beat the Arathi Armbands (19.6) on central. Optomatic Deflector (shield) and Thermotastic Egg Timer (off-hand) are not for a 2H build. For the round-3 spec.
- 2741: fixed Egg Crate [8647], no stats. 82, 10, 110, 113, 97540, 2946, 2954, 3362: no item reward (zone_440 itemchoices / itemrewards empty).

## 6. Out (silent: no tag)
Tanaris (`_decisions.tsv`):
- 8893 The Super Egg-O-Matic - no XP, nothing kept behind it (2747-2750, the egg grades, are not in the pool: no tag).
- 2605 The Thirsty Goblin - drop under 30%: Laden Dew Gland 10.81% (the Thistleshrub Dew Collectors of Leg C); 2606, 2641, 2661, 2662 - chain behind it.
- 97530 Dunemaul Dues - drop under 30%: Brilliantly Polished Bangle 4.3%.
- 4504 Super Sticky - Super Sticky Tar 32.9%, XP-only optional (rule 11).
- 4496 Bungle in the Jungle - Gorishi Scent Gland 5.0%; 4507, 4508 - chain behind it.
- 8365 Pirate Hats Ahoy!, 1878 Water Pouch Bounty - out (chapter 46 area).
- Later, not in round 2: 3444 The Stone Circle (follows 3445 The Sunken Temple, level 46 at Feathermoon: round 3); 4493 March of the Silithid (req 50, Darnassus); 3721 An OOX of Your Own (needs all three OOX rescues).

## 7. End check (`[OC]` text for the writer)
- Handed in here: 2741 (if the egg came), 2946, 2954, 5863, 82, 1560, 97540, 3362, 3161, 10, 110, 113; conditional: 351 (if the beacon dropped); gates: 6625/6624, 6609, 6610 at skill 225.
- In the log, carried out: **162 Rise of the Silithid** (Insect Analysis Report; Gracina Spiritmight, Darnassus, chapter 55); **3022 Handle With Care** (A Carefully-packed Crate; Erelas Ambersky, Rut'theran, chapter 55); **2977 Return to Ironforge** (Miniature Platinum Discs; Historian Karnik, chapter 57); **3449 Arcane Runes** (Azshara, chapter 55, untouched); conditional **648 Rescue OOX-17/TN!** (Oglethorpe, Booty Bay, **round 3**); gate 6607 if taken (U5).
- Hearth = Gadgetzan. Next: Gadgetzan - Theramore - Nijel's Point by air for Maraudon.

## 8. Totals
| | quests | XP | money |
|---|---|---|---|
| Plan row 53 (required) | 12 | 45,130 | 1g 95s |
| Spec, required handed in here | 12 | 45,130 | 1g 95s (82 50s + 113 70s + 3362 75s) |
| Optional / conditional (351 4,400 + 648 5,450) | 2 | 9,850 | 00s |
Sum: 3,150 + 4,400 + 440 + 440 + 5,900 + 3,550 + 4,200 + 4,400 + 4,550 + 4,700 + 4,700 + 4,700 = 45,130. Equal to the plan, on two conditions: 2741's egg is carried in (D1), and 1560 and 97540 are two separate hand-ins (U1). 648's 5,450 is earned in round 3. Not counted here: 162 and 3022 (chapter 55), 2977 (chapter 57), the gate quests (6624 3,900, 6625 970, 6609 970, 6610 3,900).

## 9. Unverified / in-game test list
- The Menethil - Theramore boat (round 1's line), and the Theramore - Gadgetzan fare (TaxiPath 730 = 7s 30c).
- Oasis 97540: what it asks, where it is handed in, and whether Tooga gives both Oasis and Tooga's Quest.
- Tooga's escort: speed, ambushes, timer, and whether he can be led while mounted.
- Gahz'ridian: ornaments per mound; whether the mounds show without the Detector.
- Uldum pedestal: whether the Dune Smashers aggro from the pedestal's south-east side.
- Gor'marok's rank (DB blank, Wowhead facts no elite tag).
- OOX-17/TN escort route and ambushes (only if the beacon drops).
- Whether Nat Pagle's island is reached by swimming from Theramore; Triage event at skill 225.
- Hearth cooldown on Forever (one hearth in Leg D).

## 10. Needs pull
- Wowhead Forever quest page 97540 Oasis (description, progress and completion text, comments) and NPC page 5955 Tooga (quests started/ended, map): settles U1.
- Item 8443 Gahz'ridian Ornament page (objects, count per mound) only if the in-game test disagrees with 30 mounds.

## 11. Unsure
- U1 **Oasis 97540 and Tooga's Quest 1560** share giver and text ("Show [the newly quenched] Tooga the way back to his wife, Torta"); 1560 ends at Torta, 97540 at Tooga; 97540 has no objective in QuestieDB or the nether tooltip and Wowhead's series is empty. They may be one escort in two versions (then only one is earned: -3,550 or -5,900 XP) or a pair (Oasis first, then the escort). Written as both, accepted together, Oasis handed in at Tooga beside Torta; main session to decide whether to count both.
- U2 2741 depends on the egg from Feralas (D1).
- U3 Leg order: Dunemaul first follows "lowest first" at a cost of about 23 units over doing the Noxious Lair first on the way out of Gadgetzan; swap if the main session prefers travel over the level order.
- U4 Whether chapter 46's final spec already gave 82 (then step 8 falls away) and whether chapter 52 took 6609 / 6625 in Ironforge.
- U5 6607 Nat Pagle, Angler Extreme needs fish from Feralas, Swamp of Sorrows, Desolace and Stranglethorn; after this chapter the route passes only Desolace (54). Accepting it here leaves it open into round 3 unless the other three were fished earlier; the plan Threads list it as a gate without settling this.

## 12. Deviations from the route plan
- **D1 2741 The Super Egg-O-Matic cannot be finished inside Tanaris.** Its objective is a Hippogryph Egg [8564] (quest row [9] = item 8564; nether tooltip "Requirements: Hippogryph Egg"), whose only source is the Hippogryph Egg object 141931 (item row [2] = [141931]): 9 spawns, all in **Feralas** x53.7-58.6 y74.4-78.2 (object row [3]), among Frayfeather hippogryphs 44-47 (Antilus the Soarer, rare 48, at 55.6,74.2). No Feralas visit follows chapter 53. To keep it counted here: chapter 46 accepts 2741 at the Egg-O-Matic (Gadgetzan 52.4,27.0; req 42, he is 42.7 there) and chapter 47 or 50 loots the egg; chapter 53 hands it in. If neither did, 2741 (4,200 XP) drops out of round 2 and chapter 53 earns 11 quests, 40,930 XP. (`route_xp.py` reports no place fault because it does not walk object-only objectives in another zone, apparently.)
- **D2 2946 / 2954 / 2977 at the Uldum pedestal:** not a kill quest, but the pedestal stands 0.5-0.8 units from level 48-49 elite Dune Smashers (npc 5469, row [5] = 1, six spawns). Wowhead types 2954 as Group. The plan's override keeps 2954 plain ("no kill target"); kept plain here with the approach note (step 19), the same treatment as the Sandsorrow water hole in the 46 draft.
- **D3 Gate lines:** the Triage and Nat Pagle steps assume chapter 52 took 6625 / 6609 at skill 225; the plan places the gates on "the Theramore passes" without naming where the Ironforge pickups happen.
- No other change: the 12 required quests, the 2 conditional ones and their labels are the plan's.
