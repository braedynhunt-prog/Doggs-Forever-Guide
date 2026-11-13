# Spec 47 - Feralas I 43-44 (drafted 13 Nov 2026, wave 3)

Data used (all read 13 Nov 2026): tooling/qdb = QuestieDB Forever 1.0.16 (quest/npc/object/item.json); data/zone_357.json, zone_440.json, zone_47.json, zone_16591.json, zone_33.json (Wowhead XP, money, side, reward choices; via tooling/qinfo.py); data/drop_rates.json (per-mob rows for 6258 and 6259, item pages 12 Nov); data/wowhead_quest_links.json and data/browser/r2_pages_2026-11-12.tsv (95599 page: Side None, not sharable); tooling/client/1.60.1.70938/TaxiNodes.csv + TaxiPath.csv; weights/tooltips/2026-11-12.json + `python weights/score_items.py --band 40`; nether.wowhead.com/forever/tooltip/item/8705, /221497, /287992 and /tooltip/quest/95599, /3520 (fetched 13 Nov from the shell); pool files 357_Feralas.txt, 400_ThousandNeedles.txt, 440_Tanaris.txt and pool/_decisions.tsv; docs/40-50-plan-2026-11-12.md (revised 13 Nov) and docs/40-50-route-2026-11-12.txt.

Coordinates are qdb spawns (Forever map space) unless marked otherwise. "Derived" = computed by me from TaxiNodes world positions (see section 3), not a DB spawn.

## 1. Header
- File: `47_FeralasI.lua`
- `[N 43-44 Feralas]`
- `[NX 43-45 The Hinterlands]` (chapter 48's title as the plan has it: `48_Hinterlands.lua`, `[N 43-45 The Hinterlands]`).
- `[GA Alliance]`; footer group "Forever Shaman 30-60".
- `[D ...]`: "Feralas from the east: the road from Gadgetzan through Thousand Needles to Thalanaar, the boat to Feathermoon Stronghold, the Ruins of Solarsal, the Gordunni ogres of the High Wilderness, the Missing Courier chain to the Woodpaw gnoll camps, OOX-22/FE if its beacon drops, Yeh'kinya's screecher spirits and Rhapsody's bear and ape livers. Ends at Thalanaar for the flight to Theramore."
- Level on entry **43.2**, exit **43.5** on required quest XP (plan XP table; route_xp.py re-run 13 Nov prints the same row: 14 / 27,475 / 1g 75s / 43.2 -> 43.5).
- **Level-check line (first `[OC]` of the chapter):** "This chapter wants level 43. Every pickup needs 39-40, but the Gordunni ogres run 42-45 (Brutes 42-43, Warlocks 43-44, Shaman 44-45) and the Rogue Vale Screechers 44-46. Under 43: in Leg D kill the Brutes and Warlocks first, take the Shaman last, and use the low Vale Screechers (41-43) for the spirits."

## 2. Entry state
- Stands in **Gadgetzan** (chapter 46 ends there). Hearth: **Gadgetzan** (chapter 46 binds it - assumed from the prompt, not read: 46 is specced in parallel). Gadgetzan flight point known (taken in 46, assumed).
- Quests carried in (ids; reconcile with 44, 46 and 42):
  - **1452 Rhapsody's Kalimdor Kocktail** (picked up at Aerie Peak in 44); holds 3 Roc Gizzards (6257) from 46 (assumed). Livers collected here; handed in at Rhapsody in 48.
  - **3520 Screecher Spirits** (picked up from Yeh'kinya 8579, Tanaris 67.0,22.4, in 46); carries Yeh'kinya's Bramble (10699, the quest's source item per qinfo). Objective done here; handed in at Steamwheedle Port in 53 (plan chapter 53 list; `_decisions.tsv` verdict PLAIN, counted in 53).
  - **95219 From Port to Port** (Friz Frazzlespark, Riverglades, chapter 42); carries the Cask of Powderfuse Port (276068). Handed in here.
- Profession / training items: none fall here (plan Threads: no shaman trainer in 47; the level-44 row is Ironforge / Aerie Peak in 48; Artisan Cooking is a 46 or 53 gate). No vendor stop is needed.

## 3. Travel and hearth
- **Flight points.** Thalanaar and Feathermoon are new; neither has a `[P]` tag in chapters 00-41 (grep 13 Nov). TaxiNodes 70938: Thalanaar node 31, Feathermoon node 41, Gadgetzan node 39 (Alliance), Theramore 32. TaxiPath 70938 links: **Gadgetzan - Thalanaar (paths 323/324)**, Thalanaar - Feathermoon (325/326), Thalanaar - Theramore (56/57), Feathermoon - Nijel's Point (373/374), Feathermoon - Auberdine (225/226), Feathermoon - Cenarion Hold (471). Both points are discovered on foot first.
- **In (first trip by road, unverified):** from Gadgetzan north to the Shimmering Flats and west through Thousand Needles to the Feralas border at Thalanaar. The road is not in the data. Travel step ends `[G89.5,45.9 Feralas]`.
- **Thalanaar flight master:** Thyssiana 4319 <Hippogryph Master> L55 elite, **89.5,45.9 Feralas** -> `[P Thalanaar]`.
- **Feathermoon flight master:** Fyldren Moonfeather 8019 <Hippogryph Master> L55 elite, **30.2,43.2 Feralas** -> `[P Feathermoon]`.
- **Boat (Feathermoon ferry):** TaxiNodes 54 "Transport, Feathermoon - Feralas" exists, so the ferry is in the client. Mainland dock: **45.6,43.4 Feralas** (quest 2767's objective point "the dock along the Forgotten Coast", quest row [8]). Island dock: **about 31.0,39.6 Feralas, derived** from node 54's world position on a linear fit of the Thyssiana and Fyldren spawns (Feralas x scale 0.0144 per yard = a 6,943-yard-wide map; y scale taken as 1/46.33) - unverified, test list.
- **Inn / bind:** Innkeeper Shyria 7736 <Innkeeper>, **31.0,43.5 Feralas** -> `[S Feathermoon]` on the first visit (plan's hearth proposal: Feathermoon for 47). The hearth is used once: after Leg D if the beacon never dropped (see step D10).
- **Out:** the chapter ends at **Thalanaar** after the 4281 hand-in: `[F Theramore]` from Thyssiana (path 57, Thalanaar - Theramore) is chapter 48's first line. This differs from the prompt's "exit at Feathermoon's flight master" (see Deviations 4). Hearth stays bound at Feathermoon (chapter 48 rebinds; the plan proposes Aerie Peak or Ironforge for 48-49 and Feathermoon again for 51-52).
- **Horde town warning:** Camp Mojache (Horde) stands at about 75.4,43.8 (Camp Mojache Brave 8147, L55, 19 spawns; Innkeeper Greul 7737 74.8,45.2). The Thalanaar - west road and the Old Key crate pass it (crate 3.3 units south of the nearest Brave). Lines in Legs A and F carry an `[OC]` "keep south of Camp Mojache".

## 4. Route (play order)

### Leg A - Gadgetzan to Thalanaar to the Forgotten Coast dock (Ironfur Bears 41-42)
A1. `[OC]` level-check line (section 1).
A2. Travel: Gadgetzan -> Thousand Needles -> Thalanaar by road (unverified) `[G89.5,45.9 Feralas]`.
A3. At [TAR4319 Thyssiana] get the `[P Thalanaar]` flight point `[G89.5,45.9 Feralas]`.
A4. Ride west along the road toward the Forgotten Coast. On the way kill every **Ironfur Bear** [TAR5268] L41-42 (spawns x68-90 y35-47 along the road, centre of the eastern group about 80,41) for **Ironfur Liver** 6258 `[CI6258,3]` (1452). Per-mob rate 21.4% (25/117, drop_rates.json 12 Nov) -> about 14 kills for three; whatever is missing is finished in Leg D (Grizzled bears) or Leg F. Plain line, label "~21% - budget ~14 bears in all" (rule 3/12 budget; plan's 24% is the overall figure). `[OC]` keep south of Camp Mojache (75,44).
A5. Travel to the mainland dock `[G45.6,43.4 Feralas]` and take the boat to Sardor Isle (unverified ferry; see 3). `[OC]`: the coast round the dock has Sea Elementals 48-49 and the elite Wave / Shore / Deep Striders 47-49 (rank 1; centres 41-43,46-50): do not wander south along the shore.

### Leg B - Feathermoon Stronghold: flight point, bind, pickups (no mobs)
B1. At [TAR8019 Fyldren Moonfeather] `[P Feathermoon]` `[G30.2,43.2 Feralas]`.
B2. At [TAR7736 Innkeeper Shyria] bind `[S Feathermoon]` `[G31.0,43.5 Feralas]`.
B3. At [TAR7941 Mardrack Greenwell] <Food & Drink> `[QT95219 From Port to Port]` (330 XP, 0 money; req 40 L41; carried from 42, giver Friz Frazzlespark 255897 per qdb and wowhead_quest_links) `[G31.0,43.1 Feralas]`. Plain.
B4. At [TAR7900 Angelas Moonbreeze] `[QA2982 The High Wilderness]` (3,750 XP + 65s; req 39 L44; kill 8 Gordunni Warlocks, 8 Gordunni Shaman, 8 Gordunni Brutes - counts from row [7] text; row [9] carries the three ids with no counts) `[G31.8,45.6 Feralas]`. Plain. No prerequisite (rows [11]/[12] empty).
B5. At [TAR3936 Shandris Feathermoon] `[QA2866 The Ruins of Solarsal]` (2,700 XP, 0; req 40 L43; explore the ruins = reach the Solarsal Gazebo object) `[G30.3,46.2 Feralas]`. Plain. No prerequisite.
B6. At [TAR7877 Latronicus Moonspear] `[QA4124 The Missing Courier]` (360 XP, 0; req 40 L43; speak with Ginro) `[G30.4,46.2 Feralas]`. Plain. No prerequisite.
B7. At [TAR7880 Ginro Hearthkindle] `[QT4124]` (360 XP) `[QA4125 The Missing Courier]` (2,700 XP, 0; req 40 L43; prerequisite 4124 in row [12]; find the courier's boat on the Feralas coast = the Wrecked Row Boat object 164909) `[G31.9,45.1 Feralas]`. Plain.

### Leg C - Ruins of Solarsal (Hatecrest naga 41-43)
C1. South-west across the island to the **Solarsal Gazebo** (object 142179; 2866 ends at the object, so the step is the turn-in there): `[QT2866]` (2,700 XP) `[QA2867 Return to Feathermoon Stronghold]` (1,800 XP + 45s; req 40 L43; prerequisite 2866 row [12]) `[G26.3,52.3 Feralas]`. Mobs round it (qdb within 4 units): Hatecrest Screamer [5335] 41-42, Wave Rider [5332] 41-42, Warrior [5331] 42-43, Siren [5337] 42-43 (centres 28-30,53-56), Coast Crawl Deepseer 43-44. No kill objective (2869 Against the Hatecrest, the naga-scale quest, is out). Whether the ruins are reached on foot from the stronghold (same island) is unverified.
C2. Back in the stronghold at [TAR3936 Shandris Feathermoon] `[QT2867]` (1,800 XP + 45s) `[QA3130 Against the Hatecrest]` (360 XP, 0; req 40 L43; prerequisite 2867 row [12]; report to Latronicus) `[G30.3,46.2 Feralas]`. Plain.
C3. At [TAR7877 Latronicus Moonspear] `[QT3130]` (360 XP) `[G30.4,46.2 Feralas]`. He then offers 2869 Against the Hatecrest: silent (rule 4; it is out).

### Leg D - the south: the boat wreck, the High Wilderness ogres, apes, screechers, OOX-22/FE (mobs 41-46)
D1. Boat to the mainland `[G45.6,43.4 Feralas]`, then south along the inland side (not the beach) to the **Wrecked Row Boat** (object 164909) `[G45.4,65.0 Feralas]`: `[QT4125]` (2,700 XP) and `[QA4127 Boat Wreckage]` (375 XP, 0; req 40 L44; prerequisite 4125 row [12]; starts from either Wrecked Row Boat, 164909 at 45.4,65.0 or 186419 at 45.8,65.7; source item Discarded Knife 11462). Plain. `[OC]` warning: a Sea Elemental (48-49) spawns 0.7 units and an elite Deep Strider (47-49, rank 1) 1.5 units from the wreck - pull nothing, loot and leave east.
D2. East to the High Wilderness ogre camp (x58-64 y54-73). Lowest first: in the north half of the camp kill 8 [TAR5232 Gordunni Brute] L42-43 (15 spawns 59-62,54-65; the other 18 are in the north-east camp at 75-80,25-35, not on the route) `[QC2982]` `[G60.5,57.5 Feralas]`. Gordunni Maulers 43-44 share the camp (not targets).
D3. Same camp: kill 8 [TAR5240 Gordunni Warlock] L43-44 (15 spawns 58-62,55-73, centre 59.8,64.7) `[QC2982]` `[G59.8,64.7 Feralas]`.
D4. Same camp, south end: kill 8 [TAR5236 Gordunni Shaman] L44-45 (15 spawns 58-64,63-73, centre 60.8,67.8) `[QC2982]` `[G60.8,67.8 Feralas]`. Under 43: this line last in the leg (after D5-D6).
D5. Between the camp and the cave (x56-62 y54-64): kill [TAR5260 Groddoc Ape] L42-43 (26 spawns, 23 of them at 56-62,54-64, centre 58.5,58.5) for **Groddoc Liver** 6259 `[CI6259,3]` (1452). Per-mob rate 26.4% (39/148, drop_rates.json 12 Nov) -> budget ~11 apes; the Thunderers (49-50, 28.1%) are in the north and are not on the route. Plain, label "~26% - budget ~11 apes". Finish the bear livers here if Leg A left any: Ironfur Bear [5268] 41-42 (11 spawns 55-61,53-62) and Grizzled Ironfur Bear [TAR5272] L44 (26.7%, 12/45; 50-61,46-51 and 68-73,58-64). Old Grizzlegut (5352, rare L43, 59.5,59.4) dropped a liver in its only sampled kill - if it is up, kill it.
D6. Same area: **screecher spirits** `[QC3520]` (3 Screecher Spirits, npc 8612; count from the quest text and the 13 Nov tooltip "Screecher Spirits collected x 3"). Kill [TAR5307 Vale Screecher] L41-43 (only 4 spawns: 57.5,55, 58,58.5, 58.5,58, 60,62) or [TAR5308 Rogue Vale Screecher] L44-46 (20 spawns x42-61 y36-59, several on the way back to the dock at 46-49,36-50) and use Yeh'kinya's Bramble on the corpse to raise the spirit (the mechanic is Classic knowledge, unverified; the DB places the spirit npc 8612 at x42-61 y36-62, the screechers' range) `[G58.3,58.5 Feralas]`. Plain (counted in chapter 53).
D7. **If the OOX-22/FE Distress Beacon (8705) dropped** anywhere so far (it drops from 82 Feralas npc types per qdb item row [1], every mob of this route among them: ogres, bears, apes, screechers, Woodpaw, Hatecrest): right-click it -> `[QA2766 Find OOX-22/FE!]` (3,900 XP, 0; req 40 L45; sharable unknown) and go to the cave near Feral Scar Vale: at [TAR7807 Homing Robot OOX-22/FE] L42 `[QT2766]` (3,900 XP) `[QA2767 Rescue OOX-22/FE!]` (4,850 XP, 0; req 40 L45; prerequisite 2766 row [12]) `[G53.4,55.7 Feralas]`. Feral Scar yetis 43-46 (Feral Scar Yeti 43-44, Enraged 44-45, Hulking 45-46, Lurking 46) stand round the cave. Plan label: required. See Deviations 1 for the drop rate.
D8. `|cFFFF0000ESCORT|r` escort OOX-22/FE north-west to the Forgotten Coast dock `[QC2767]` `[G45.6,43.4 Feralas]` (objective point from quest row [8]: 45.63,43.39). The path passes Rogue Vale Screechers 44-46, Grizzled Ironfur Bears 44, Longtooth Howlers 43-44 and, near the coast, Sea Elementals / Sea Spray 47-49 (centres 43,48) - keep the robot inland. Ambushes on the walk are Classic knowledge (unverified). 2767 is handed in to **Oglethorpe Obnoticus** 7406, Booty Bay, Stranglethorn **28.4,76.3**, in chapter 50 (carried out).
D9. The escort ends at the dock: boat to Feathermoon.
D10. **If the beacon did not drop**: hearth to Feathermoon from the ogre camp `[H Feathermoon]` instead of walking back to the dock (bind from B2). The OOX lines (D7-D8) then do not fire; see Deviations 1 for how to write them.

### Leg E - Feathermoon: the knife (no mobs)
E1. At [TAR7900 Angelas Moonbreeze] `[QT2982 The High Wilderness]` (3,750 XP + 65s) `[G31.8,45.6 Feralas]`. She then offers 3445 The Sunken Temple (req 46): not here (chapter 51; silent).
E2. At [TAR7880 Ginro Hearthkindle] `[QT4127]` (375 XP) `[QA4129 The Knife Revealed]` (375 XP, 0; req 40 L44; prerequisite 4127) `[G31.9,45.1 Feralas]`.
E3. At [TAR7879 Quintis Jonespyre] `[QT4129]` (375 XP) `[QA4130 Psychometric Reading]` (375 XP, 0; req 40 L44; prerequisite 4129) `[G32.5,43.8 Feralas]`.
E4. At [TAR7880 Ginro Hearthkindle] `[QT4130]` (375 XP) `[QA4131 The Woodpaw Gnolls]` (2,800 XP, 0; req 40 L44; prerequisite 4130; search the Woodpaw camps) `[G31.9,45.1 Feralas]`.

### Leg F - east: the Woodpaw camps, the Old Key, Thalanaar (Woodpaw 40-44, Ironfur Bears 41-42)
F1. Boat to the mainland `[G45.6,43.4 Feralas]` and ride east to the southern Woodpaw camps (Woodpaw Mystic 42-43, Reaver 42-43, Alpha 43-44 at x65-78 y51-57; Mongrel 40-41, Trapper 41-42, Brute 41-42 further north at x69-77 y36-55). Kill any Ironfur Bear still needed on the way (`[CI6258,3]`).
F2. At the **Large Leather Backpacks** (object 164953) `[QT4131 The Woodpaw Gnolls]` (2,800 XP; the quest ends at the object) `[G73.3,56.3 Feralas]`. Loot the **Undelivered Parcel** (11463; qdb item row [2] = object 164953) and right-click it: `[QA4281 Thalanaar Delivery]` (2,800 XP + 65s; req 40 L44; prerequisite 4131 row [12]). Plain. The backpacks also start **4135 The Writhing Deep** (chapter 51): not taken here (see Unsure 1).
F3. `[O]` conditional (plan label): **The Old Key** - at the **Old Crate** (object 442688) `[G76.6,48.0 Feralas]` loot the Old Key (item 221497, "This Item Begins a Quest" = 95599 per its 13 Nov tooltip; qdb item row [2] = object 442688) and accept `[QA95599 The Old Key]` (3,450 XP + 55s; L42, req 35); open the **Old Chest** (object 642451) `[QT95599]` `[G79.2,49.4 Feralas]`. `[OC]` the crate stands 3.3 units south of the nearest Camp Mojache Brave (L55 Horde guard): approach from the south. Not counted (plan). See Deviations 2.
F4. Ride east to Thalanaar. At [TAR4048 Falfindel Waywarder] `[QT4281 Thalanaar Delivery]` (2,800 XP + 65s) `[G89.6,46.6 Feralas]`.
F5. `[OC]` Check line (section 7). Then chapter 48 starts at [TAR4319 Thyssiana] with the flight to Theramore.

## 5. Gear calls
- **2767 Rescue OOX-22/FE!** (reward chosen at the Booty Bay hand-in in chapter 50, reward choice from data/zone_357.json itemchoices [9647, 9648]; stats from weights/tooltips/2026-11-12.json, scores `score_items.py --band 40` central):
  - **Failed Flying Experiment** 9647: leather shoulders, +10 Str +10 Agi, req 40 (item level 48), sell 79s 62c. Score **31.2** (20.0 + 11.2).
  - **Chainlink Towel** 9648: back, +3 Int +10 Spi, sell 63s 92c. Score **30.1**.
  - Call: take the **Failed Flying Experiment** over Palm Frond Mantle (cloth +7 Int +6 Spi, 26.8 at band 40; chapter 30's shoulder pick), a gain of 4.4. If he wears Mantle of Doan (44.1) or Inquisitor's Shawl (36.0) from the round-1 dungeon loot, take the Chainlink Towel instead when his cloak scores under 30.1 (chapter 22-31 cloaks: Glowing Thresher Cape 26.0, South Seas Shroud, Watch Master's Cloak +7 Sta, Vine Pruner's Cloak), else sell the higher-priced one (the shoulders, 79s 62c). The line goes on 2767's [QT] in chapter 50.
- No other quest of this chapter has a reward item (zone_357.json itemchoices / itemrewards empty for 2982, 2866, 2867, 3130, 4124-4131, 4281, 2766, 95599; 95219 in zone_16591.json empty).

## 6. Out (silent in the guide; reasons copied from `_decisions.tsv` / the plan's Out list)
Feralas, not in 47 or 51:
- 2869 Against the Hatecrest - drop under 30%: Hatecrest Naga Scale 13.3% (9 droppers, best Lady Szallah 200% of 1)
- 2870 Against Lord Shalzaru - chain behind 2869; 2871 Delivering the Relic - chain behind 2870
- 92858 WANTED: Ohk'zi - elite outside a dungeon (rule 13): Ohk'zi (43 elite); the staff scores 501.5
- 2944 The Super Snapper FX - elite (Gammerita 48 elite); 2943 Return to Troyas, 2879 The Stave of Equinex, 2942 The Morrow Stone - chain behind it
- 7003 Zapped Giants - elite giants (Land Walker 49, Cliff Giant 50, Shore/Deep Strider 49); 7725 Again With the Zapped Giants - chain behind it; 7726 Refuel for the Zapping - repeatable follow-up, 560 XP
- 7733 Improved Quality - Rage Scar Yeti Hide 24.4%; 2821 The Mark of Quality - Thick Yeti Hide 25.5%; 7735 Pristine Yeti Hide - chain behind 2821
- 4297 Food for Baby - Silvermane Stalker Flank 0.22%; 4298 Becoming a Parent - chain behind 4297
- 3909 The Videre Elixir - chain behind Muigin and Larion; 4041 The Videre Elixir - no XP, nothing kept behind it
- 3721 An OOX of Your Own - LATER (needs the three OOX rescues; round 3, Booty Bay)
Feralas, kept but in chapter 51 (not here): 2969, 2970, 2972, 3841, 3842, 3843, 4135, 4265, 4266, 4267, 2939, 2940, 2941, 2844, 2845, 3445; optional/conditional there: 95555 Corrupted Nature, 7721 Fuel for the Zapping.
Thousand Needles (passed through, every quest OUT): 1104, 1105 (Shimmering Flats, level 30: grey at 42); 1106 (chain behind 1104); 1108 Indurium (Indurium Flake 21.8%) and its chain 1137, 1190, 1194, 1192; 1176 and the racer chain 1178, 1180, 1181, 1182, 1183, 1186, 1187, 1188, 1189 (Shimmering Flats racer chain: nine grey level 30-37 quests in front of 4,900 XP); 1116 Dream Dust in the Swamp (30.4%, XP-only optional) and its chain 1111, 1112, 1114, 1115, 1117, 1118; 1119-1122 (chain behind 621 Zanzil's Secret); 1191 (no XP); 2769 The Brassbolts Brothers is a Zul'Farrak quest (chapter 54).

## 7. End check
`[OC] Check:` handed in here: From Port to Port (95219), The High Wilderness (2982), The Ruins of Solarsal (2866), Return to Feathermoon Stronghold (2867), Against the Hatecrest (3130), The Missing Courier (4124, 4125), Boat Wreckage (4127), The Knife Revealed (4129), Psychometric Reading (4130), The Woodpaw Gnolls (4131), Thalanaar Delivery (4281), Find OOX-22/FE! (2766, if the beacon dropped), The Old Key (95599, if taken).
Still in the log, carried out:
- **1452 Rhapsody's Kalimdor Kocktail** - complete: 3 Roc Gizzards, 3 Ironfur Livers, 3 Groddoc Livers -> Rhapsody Shindigger, Aerie Peak (Hinterlands 26.9,48.6), chapter 48.
- **3520 Screecher Spirits** - complete (3 spirits) -> Yeh'kinya, Steamwheedle Port (Tanaris 67.0,22.4), chapter 53. It gates 3527 The Prophecy of Mosh'aru (chapter 54).
- **2767 Rescue OOX-22/FE!** (if the beacon dropped) - complete -> Oglethorpe Obnoticus, Booty Bay (Stranglethorn 28.4,76.3), chapter 50.
Hearth = Feathermoon. Flight points new: Thalanaar, Feathermoon. Stands at Thalanaar. Next: The Hinterlands (Thalanaar - Theramore by flight).

## 8. Totals
| | count | XP | money |
|---|---|---|---|
| required (plan list) | 14 | 27,475 | 1g 75s |
| optional / conditional | 1 (95599) | 3,450 | 55s |

Required: 2982 3,750 + 65s; 95219 330; 2866 2,700; 2867 1,800 + 45s; 3130 360; 4124 360; 4125 2,700; 4127 375; 4129 375; 4130 375; 4131 2,800; 4281 2,800 + 65s; 2766 3,900; 2767 4,850. Sum 27,475 XP and 1g 75s = the plan's XP-table row for 47 (14, 27,475, 1g 75s; optional 3,450). 1452 (3,600, counted in 48) and 3520 (3,750, counted in 53) are not in these totals.
If Deviation 1 is accepted: 12 required, 18,725 XP, 1g 75s; conditional 12,200 XP (2766 + 2767 + 95599).

## 9. Unverified / in-game test list; Needs pull; Unsure
**Unverified / test list**
- The road Gadgetzan - Thousand Needles - Thalanaar (not in the data).
- The Feathermoon ferry, its island dock (derived about 31.0,39.6) and the mainland dock (45.6,43.4 from 2767's objective point).
- Whether the Ruins of Solarsal are reached on foot from the stronghold.
- Screecher Spirits: the bramble is used on a screecher's corpse (Classic mechanic); Vale Screecher vs Rogue Vale Screecher both work.
- OOX-22/FE Distress Beacon drop rate on Forever; whether the escort has ambushes; whether the robot paths along the elite-strider coast.
- The Old Key: the Old Crate (76.6,48.0) gives the key to an Alliance player (Wowhead side None); distance to the Camp Mojache guards.
- Woodpaw backpacks: the parcel is looted (qdb object drop), not a 4131 reward.

**Needs pull**
- Wowhead Forever item page 8705 (OOX-22/FE Distress Beacon): dropped-by listview count/outof per mob - the tooltip has no Drop Chance (82 droppers).
- Wowhead Forever quest page 95599 already pulled (Side None); the object page 442688 (Old Crate) would confirm the start.

**Unsure**
1. **4135 The Writhing Deep** (chapter 51, 3,050 XP) starts from the same Large Leather Backpacks where 4131 ends (F2). Taking it here costs nothing and saves chapter 51 a walk to 73.3,56.3; the plan places it in 51. Left out of this spec (not added); the main session decides.
2. **Exit point** (Deviation 4): Thalanaar vs the prompt's Feathermoon flight master.
3. Chapter 46's exact entry state (hearth Gadgetzan, the Gadgetzan flight point, the Roc Gizzards, 3520 held) is assumed from the prompt.
4. The plan's chapter 51 says "Ratchet - Theramore - Thalanaar - Feathermoon"; TaxiPath also has Gadgetzan - Thalanaar (323/324) and Feathermoon - Nijel's Point / Auberdine / Cenarion Hold - for the 51 and 53 specs, not acted on here.
5. Find OOX-09/HL! (485, chapter 48) and Find OOX-17/TN! (351, chapter 53) are the same drop-start pattern as 2766; Deviation 1 applies to them as well if it is accepted (not checked against their data here).

## 10. Deviations from the route plan
1. **2766 Find OOX-22/FE! and 2767 Rescue OOX-22/FE! (8,750 XP) are plain in the plan but start from a drop with no rate in the data.** Item 8705 OOX-22/FE Distress Beacon: qdb item row [1] lists 82 Feralas npc droppers, no object source; data/drop_rates.json has no row; the 13 Nov nether tooltip has no Drop Chance (multi-dropper). The plan writes the other drop-start quests (95384, 95385, 95599) as conditional "taken only if it drops", and its method says such quests are not counted. Recommendation: label 2766 and 2767 conditional "if the beacon drops" and take them out of the count (-2 quests, -8,750 XP). This spec keeps them required as the plan says, written so the steps fire only when he holds the beacon (D7 with the item check; D8 after it); the writer needs the main session's ruling before choosing plain vs `[O]`.
2. **95599 The Old Key** is conditional in the plan as "probably starts from a dropped key". The data now shows a ground-object start: item 221497 Old Key, qdb item row [2] = object 442688 Old Crate at 76.6,48.0 Feralas, and its tooltip says "This Item Begins a Quest" (95599). The end is the Old Chest 642451 at 79.2,49.4, both on Leg F's road. Its Wowhead side is None (r2_pages_2026-11-12.tsv), which under the plan's method keeps it conditional. Written as `[O]` conditional, not counted, as in the plan; the main session may promote it to plain (+1 quest, +3,450 XP, +55s).
3. **Liver budgets use the per-mob rows** (drop_rates.json 12 Nov): Ironfur Bear 21.4% (25/117) -> about 14 bears, not the plan's 24% / 12; Grizzled Ironfur Bear 26.7% (12/45) -> about 11; Groddoc Ape 26.4% (39/148) -> about 11 (plan 27% / 11). The route kills only Ironfur Bears (41-42), Grizzled bears (44) and Groddoc Apes (42-43); Patriarchs (48-49) and Thunderers (49-50) are not on it.
4. **Exit at Thalanaar, not Feathermoon.** The chain ends at Thalanaar (4281, Falfindel Waywarder 89.6,46.6) and nothing after it needs Feathermoon, so the chapter ends at Thyssiana and chapter 48 flies Thalanaar - Theramore (path 57), the same leg as the plan's Feathermoon - Thalanaar - Theramore minus its first hop. If the main session wants the Feathermoon exit, the cost is a Thalanaar - Feathermoon flight (path 325) after F4.
5. **Plan's first-trip wording** ("through Feralas to the Forgotten Coast boat") holds; the spec adds that Gadgetzan - Thalanaar is a flight link in TaxiPath 70938 (usable on later trips once Thalanaar is known).
