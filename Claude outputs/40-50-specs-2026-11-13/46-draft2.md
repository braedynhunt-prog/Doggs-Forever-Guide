# Spec 46 - Tanaris I (drafted 13 Nov 2026, round 2 of the 30-60 guide)

Data used (all read 13 Nov 2026): `tooling/qdb` = QuestieDB Forever 1.0.16 (quest/npc/object/item.json; `python tooling/qinfo.py`, `loc.py`); `data/zone_*.json` via qinfo (XP, money); `data/drop_rates.json` (rows dated 12 Nov); `data/wowhead_quest_links.json` (series, start/end); `data/browser/r2_pages*_2026-11-1*.tsv` (QUEST 97536, ITEM 6257); `nether.wowhead.com/forever/tooltip/` pulled 13 Nov for quests 97536, 1690, 1691, 1707, 8366, 2873, 2876, 992, 3520, 6610, 95321, 95383, 95312, 95472 and items 278194, 9276, 9250 (objective counts below come from these: qdb row [9] carries no counts); `weights/tooltips/2026-11-12.json` + `python weights/score_items.py --band 40`; `tooling/client/1.60.1.70938/TaxiNodes.csv` / `TaxiPath.csv`; plan `docs/40-50-plan-2026-11-12.md` (revised 13 Nov) and `docs/40-50-route-2026-11-12.txt`; pool `Claude outputs/40-50-plan-2026-11-12/pool/440_Tanaris.txt`, `16591_Riverglades.txt`, `400_ThousandNeedles.txt` rows of `_decisions.tsv`.

## 1. Header
- File: `46_TanarisI.lua`
- `[N 42-44 Tanaris]`
- `[NX 43-44 Feralas]` (chapter 47's title in the plan)
- `[GA Alliance]`; class lines `[A Shaman]`; footer group "Forever Shaman 30-60".
- `[D ...]`: "From Ratchet by the Barrens road, the Great Lift and the Shimmering Flats to Gadgetzan (flight point, inn): the water survey at Sandsorrow Watch, the Wastewander bandits, Steamwheedle Port and the Southsea pirates of Lost Rigger Cove, the two WANTED posters, Rhapsody's roc gizzards and the Screecher Spirits pickup for Feralas."
- Level on entry **42.5** (XP table), exit **43.2** on the plan's count, about **43.15** with Deliver to MacKinley handed in at chapter 50 (Deviation D1).
- **Level-check line (first `[OC]`):** "This chapter wants level 43. Every quest here needs 38-40, but the Southsea pirates and Andre Firebeard at Lost Rigger Cove are 44-45, the Wastewander Assassins 44-45 and Caliph Scorpidsting 46. Under 43: do the Rocs, Sandsorrow and the bandit camp first (mobs 40-43), then Waterspring Field, then the Cove; Caliph comes last, at 44 if you can."

## 2. Entry state
- Stands on the **Ratchet dock**, off the Booty Bay - Ratchet boat that ends chapter 45. Hearth: **Booty Bay** (chapter 45's bind, per the prompt; not used here).
- Flight points known that matter: Ratchet (`[P Ratchet]` 26_RazorfenKraul.lua:30), Theramore (32_Dustwallow.lua:28). Gadgetzan is NOT known: no `[P Gadgetzan]` in chapters 00-41 (grep 13 Nov).
- Quests carried in, assumed (main session to reconcile):
  - **2872 Stoley's Debt** - starts at "Sea Wolf" MacKinley [2501], Booty Bay **27.8,77.1 Stranglethorn Vale**; must be picked up in chapter 45 (not on chapter 45's plan list: Deviation D2).
  - **1452 Rhapsody's Kalimdor Kocktail** - picked up at Rhapsody Shindigger [5634] Aerie Peak (Hinterlands 26.9,48.6) in chapter 44; prerequisite 1451 (quest row [12]).
  - **95296 Shipping and Handling** - only if Friz Frazzlespark [255897] offered it in chapter 42 (Riverglades 77.1,52.9).
  - Possibly 2769 The Brassbolts Brothers and 2864 Tran'rek if earlier specs took them (see Unsure U8).
- Training: none here. No shaman trainer in Tanaris; the 42 row was chapter 43, the 44 row is Aerie Peak in chapter 48 (plan Threads).
- Professions: the Artisan Cooking gate (6610 Clamlette Surprise, Cooking 225) is offered here as an optional line.

## 3. Travel and hearth
- **In (road, unverified):** Ratchet - Barrens road south - the Great Lift - Thousand Needles - Shimmering Flats - Tanaris. No flight link reaches Gadgetzan from a known point: TaxiPath 70938 links Gadgetzan (node 39, Alliance mount 541) only to Theramore 32 (paths 201/222), Thalanaar 31 (323/324), node 73 (394/424) and Marshal's Refuge 79 (452/458); Ratchet (node 80) links to Theramore, 25 and 64 only. Theramore - Gadgetzan is flyable only once Gadgetzan is discovered on foot.
  - Markers (round 1's, 39_StormHeedTempest.lua:45-48): Ratchet flight master Bragok [16227] 63.1,37.2 The Barrens (the dock east of him is unverified, 39c:13); Camp Taurajo road `[G44.5,59.2 The Barrens]`; bottom of the Barrens `[G46.4,73.9 The Barrens]`; Great Lift `[G29.2,34.2 Thousand Needles]` (DB has two Great Lift objects, 29.2,34.2 and 43.3,46.9; unverified which is the lift). Then east through Thousand Needles past **Freewind Post** (Horde; flight master Nyse [4317] L55 elite at 45.1,49.1 Thousand Needles - stay clear) to the Mirage Raceway in the Shimmering Flats (Wizzle Brassbolts [4453] 78.1,77.1 Thousand Needles as the marker), then south into Tanaris to Gadgetzan. Ghost Wolf / ram for the ride. Horde towns on the way (Crossroads, Camp Taurajo, Freewind Post): stay on the road.
  - Thousand Needles pickups on the way: none. Every Needles quest in the pool is out (`_decisions.tsv` category 400: Shimmering Flats chains grey at 42, Indurium 21.8%, Dream Dust chain XP-only).
- **Gadgetzan:** flight master **Bera Stonehammer [7823]** L55 elite **51.0,29.3 Tanaris** `[P Gadgetzan]`. Innkeeper **Innkeeper Fizzgrimble [7733]** **52.5,27.9 Tanaris**: `bind your Hearthstone to [S Gadgetzan]` (plan Threads: Gadgetzan for 46).
- **Steamwheedle Port** (67,23) has no flight point in TaxiNodes; it is ridden to (~16 units from Gadgetzan).
- **Out:** the chapter ends in Gadgetzan, bound there. Chapter 47 goes by road Gadgetzan - Thousand Needles - Thalanaar. Note for the main session: TaxiPath 323/324 links Gadgetzan and Thalanaar directly, so once chapter 47 takes `[P Thalanaar]` the later Tanaris/Feralas trips can fly that link.

## 4. Route (play order)

### Leg A - arrival in Gadgetzan (pickups, flight point, bind)
1. `[OC]` level-check line (section 1).
2. `[OC]` road note (section 3), then travel steps: Ratchet `[G63.1,37.2 The Barrens]` -> `[G44.5,59.2 The Barrens]` -> `[G46.4,73.9 The Barrens]` -> Great Lift `[G29.2,34.2 Thousand Needles]` -> Mirage Raceway `[G78.1,77.1 Thousand Needles]` -> Gadgetzan `[G51.0,29.3 Tanaris]`. All road markers unverified (DB has no road data).
3. At [TAR7823 Bera Stonehammer] `[P Gadgetzan]` `[G51.0,29.3 Tanaris]`.
4. At [TAR7733 Innkeeper Fizzgrimble] bind `[S Gadgetzan]` `[G52.5,27.9 Tanaris]`.
5. At [TAR7724 Senior Surveyor Fizzledowser] `[QA992 Gadgetzan Water Survey]` (3,050 XP + 35s at the hand-in; req 38, L46; you get the Untapped Dowsing Widget [8584], quest row [10]) `[G50.2,27.5 Tanaris]`. Plain.
6. At the Wanted Poster (object 150075) in Gadgetzan `[QA2781 WANTED: Caliph Scorpidsting]` (5,050 XP + 1g 30s; req 39, L46; ends at Chief Engineer Bilgewhizzle) and `[QA2875 WANTED: Andre Firebeard]` (3,900 XP + 1g 30s; req 40, L45; ends at Security Chief Bilgewhizzle, Steamwheedle Port) `[G51.8,27.0 Tanaris]`. Both plain (2875 carries the one-kill label at its kill line).
7. At [TAR14743 Jhordy Lapforge] `[QA97536 Gnomish Garbage]` (2,900 XP; req 40, L45; Wowhead: Alliance, start and end Jhordy [14743], series none, "Not sharable"; you get the Crate of Radioactive Refuse [278194], 5 charges, 30 sec cooldown, "Discard hazardous materials a safe distance away from Gadgetzan and other garbage"; objective "Experimental Refuse discarded x 5", nether tooltip 13 Nov) `[G52.3,26.9 Tanaris]`. Plain. Forever-only check done: qdb row [9]/[11]/[12] empty; objective from the tooltip; no prerequisite in the series.
8. At [TAR7407 Chief Engineer Bilgewhizzle] `[QA1690 Wastewander Justice]` (3,600 XP + 60s; req 40, L43) `[G52.5,28.5 Tanaris]`. Plain.
9. At [TAR7408 Spigot Operator Luglunket] beside him `[QA1707 Water Pouch Bounty]` (2,800 XP; req 40, L44; 5 Wastewander Water Pouches; reward Gadgetzan Water Co. Care Package [8484]) `[G52.5,28.4 Tanaris]`. Plain with the budget (step 17).
10. `[O]` Cooking 225 only: at [TAR8125 Dirge Quikcleave] `[QA6610 Clamlette Surprise]` (3,900 XP at the hand-in; req 35, L45, requires Cooking 225 - quest row [17] = [185, 225]; 12 Giant Eggs, 10 Zesty Clam Meat, 20 Alterac Swiss) `[G52.6,28.1 Tanaris]`. Gate line (rule 11: profession rank). Giant Eggs drop from the Rocs of this chapter (qdb item 12207 row [1]: 5428, 5429, 5430 among others; no rate in the data) and from the Hinterlands owlbeasts (chapter 48); Zesty Clam Meat comes from an item (7973, clams); Alterac Swiss from innkeeper/food vendors (25 vendors in item row [13], e.g. Truk Wildbeard [4782] Hinterlands, Craig Nollward [4894] Dustwallow; price not in the dated tooltips). Hand-in: chapter 53 (Gadgetzan) - not counted (see Unsure U9).
11. `[OC]` Gadgetzan does not give the chapter-53 quests now (Noxious Lair, Andi Lynn, Tran'rek, the Egg-O-Matic, Curgle): see Unsure U6.

### Leg B - west: Rocs and the Sandsorrow water hole (mobs 41-43; elite camp 42-44 at the pool)
12. Kill [TAR5428 Roc] (level 41-43, not elite; 19 spawns, x35-59 y25-37) for 3 Roc Gizzards for 1452 Rhapsody's Kalimdor Kocktail `[CI6257,3]` - "(~12% - budget ~25 kills)". Per-mob rows of `data/drop_rates.json` (12 Nov): Roc 5428 21/171 = 12.3%; Fire Roc 5429 46/960 = 4.8% (43-45, 41 spawns x37-59 y35-54); Searing Roc 5430 1/31 (47-49). Budget 3 / 0.123 = 24.4, about 25 Roc kills. Spawns: 9 at x49-50 y35-37 (south of town), 3 at 48.7-49.9,28.2-31.2 (west gate), 45.9,29.0, 40.7,33.1, 40.9,24.9, 35.3,29.0 (on the way to Sandsorrow), 3 at 56.1,25.4 / 57.4,31.9 / 59.2,31.1 (Leg C). `[G49.5,35.8 Tanaris]`. Held with `[CI6257,3]`, not `[QC1452,1]` (lesson: one of several items). Kill line text: "the gizzard comes from plain Rocs only (Fire Rocs 5%)". If fewer than three after ~25 Rocs, keep killing Rocs here and in Leg C (the quest is required, Braedyn 13 Nov; this is the only gizzard stop before the chapter-48 hand-in).
13. `[OC]` |cFFFF0000Danger:|r the Sandsorrow Watch water hole (39.0,29.0) stands inside the Sandfury troll camp: Sandfury Firecaller [5647] 43-44, Axe Thrower [5646] 43-44 and Hideskinner [5645] 42-43 are all **elite** (qdb npc row [5] = 1, Classic DB the same); the nearest spawns are 0.7 (Firecaller 39.65,29.21), 0.9 (Axe Thrower 39.62,28.40) and 1.5 units away, all to the east and north-east (x39.6-41.0, y27.6-30.1). The west side is open (next troll 3 units away at 37.3-37.6,26.2-26.3). Come in from the south-west, use the widget at the pool's west edge and leave west. See Deviation D4.
14. Use the Untapped Dowsing Widget at the Sandsorrow Watch Water Hole (object 144052; Tapped Dowsing Widget [8585] from the object) `[QC992]` `[UI8584]` `[G38.6,29.2 Tanaris]` (marker 0.4 west of the object at 39.0,29.0, on the open side; unverified how close the widget must be).
15. Use the Crate of Radioactive Refuse 5 times in the open desert between Sandsorrow and Gadgetzan (30 sec cooldown; "a safe distance away from Gadgetzan and other garbage": where that is, is unverified - try around 44,30) `[QC97536]` `[UI278194]` `[G44.0,30.0 Tanaris]`.
16. Back in Gadgetzan: at [TAR7724 Senior Surveyor Fizzledowser] `[QT992]` (3,050 XP + 35s) `[G50.2,27.5 Tanaris]`; at [TAR14743 Jhordy Lapforge] `[QT97536]` (2,900 XP) `[G52.3,26.9 Tanaris]`. Do NOT take 82 Noxious Lair Investigation (chapter 53; silent - just no tag; see U6).

### Leg C - east: the bandit camp (mobs 40-42)
17. East of Gadgetzan (x59-66 y23-34): kill [TAR5618 Wastewander Bandit] (41-42; 13 spawns, centre 62.8,29.2) and [TAR5616 Wastewander Thief] (40-41; 25 spawns, centre 62.7,29.3), 10 of each `[QC1690]` `[G62.7,29.3 Tanaris]`. Same kills: 5 Wastewander Water Pouches `[QC1707]` "(~33% - budget ~15 kills; the two Wastewander Justice quests kill 44 of these mobs)". Per-mob rows (12 Nov): Thief 472/1344 = 35.1%, Bandit 445/1321 = 33.7%, Rogue 298/949 = 31.4%, Shadow Mage 206/671 = 30.7%, Assassin 182/558 = 32.6%, Scofflaw 10/46, Andre Firebeard also drops it (item row [1]). Expected from this leg's 20 kills: ~6.9 pouches; Leg D adds 24 kills (~7.5). Rule 12 clause: 30-60% plain with the budget because the route's kill quests on the same mobs cover it. Rocs at 56-59,25-32 for step 12 on the way.
18. Back to Gadgetzan (~10 units): at [TAR7407 Chief Engineer Bilgewhizzle] `[QT1690]` (3,600 XP + 60s) `[QA1691 More Wastewander Justice]` (3,750 XP + 65s; req 40, L44; prerequisite 1690, quest row [12]) `[G52.5,28.5 Tanaris]`. At [TAR7408 Spigot Operator Luglunket] `[QT1707]` if you have 5 pouches (2,800 XP; Care Package) `[G52.5,28.4 Tanaris]`; otherwise after Leg D.

### Leg D - south-east: Waterspring Field (mobs 41-45)
19. At Waterspring Field (x58-66 y32-41): kill [TAR5617 Wastewander Shadow Mage] (41-43; 24 spawns, centre 61.8,37.1) x10, [TAR5615 Wastewander Rogue] (43-44; 22, centre 62.2,37.4) x8, [TAR5623 Wastewander Assassin] (44-45; 13, centre 61.8,37.9) x6 `[QC1691]` `[G61.9,37.4 Tanaris]`; finish the pouches here `[QC1707]`.
20. `[OC]` Caliph Scorpidsting [7847] (level 46, not elite; one spawn 61.8,38.2, among the Rogues and Assassins): at 44 kill him now (step 26); under 44 leave him - the route comes back for him after the Cove.
21. Ride north-east to Steamwheedle Port (~15 units).

### Leg E - Steamwheedle Port (pickups)
22. At [TAR7881 Stoley] `[QT2872 Stoley's Debt]` (390 XP; carried from chapter 45) `[QA2873 Stoley's Shipment]` (3,900 XP + 50s; req 40, L45; Stoley's Shipment [9244] from the Stolen Cargo, object 142181) `[G67.1,24.0 Tanaris]`. Plain.
23. At [TAR7882 Security Chief Bilgewhizzle] `[QA8366 Southsea Shakedown]` (3,900 XP + 65s; req 40, L45; 10 each of four Southsea types) `[G67.1,23.9 Tanaris]`. Plain.
24. At [TAR8579 Yeh'kinya] `[QA3520 Screecher Spirits]` (3,750 XP at the hand-in, chapter 53; req 40, L44; you get Yeh'kinya's Bramble [10699]; "Capture the spirits of 3 screechers in Feralas", objective "Screecher Spirits collected x 3"; kill target in qdb Screecher Spirit [8612] L1, Feralas x42-61 y36-62) `[G67.0,22.4 Tanaris]`. Counted in chapter 53 (route file, `_decisions.tsv` 3520 PLAIN, "mobs to 1"); done in Feralas, chapter 47. Do not take its follow-up 3527 now (needs 3520 handed in; chapter 54).
25. `[O]` Friz block only (if you carry 95296): at [TAR260405 Wharfmaster Steamfizzle] `[QT95296 Shipping and Handling]` (315 XP) `[QA95383 Shipping and Handling]` (315 XP: Friz's Secret Stash to Tazzik) `[G67.6,23.1 Tanaris]`; at [TAR260857 Tazzik] `[QT95383]` (315 XP) `[QA95312 Coming to Collect]` (315 XP: speak with Fizbuz Mithril in Gadgetzan) `[G67.3,24.0 Tanaris]`. Conditional: Wowhead series 95294 > 95296 > 95383 > 95312 > 95321 > 95472, each "only if offered" (qdb rows [11]/[12] empty; req level blank in qdb, 36 on Wowhead).

### Leg F - Lost Rigger Cove (mobs 44-45)
26. (If not done in Leg D and you are 44+, Caliph can wait; he is on the way home in Leg H.)
27. `[OC]` Lost Rigger Cove (x71-76 y42-49), south of the Port (~23 units). |cFFFF0000Danger:|r Kregg Keelhaul [8203], level 47, qdb rank 4 (rare, not elite), one spawn 73.2,48.7, 1.6 from Andre. Southsea Kidnappers (45, 5 spawns) also stand here (no quest).
28. Kill [TAR7855 Southsea Pirate] (44-45; 26 spawns, centre 72.4,46.0), [TAR7856 Southsea Freebooter] (44-45; 27, 73.3,45.8), [TAR7857 Southsea Dock Worker] (44-45; 30, 74.1,47.7), [TAR7858 Southsea Swashbuckler] (44-45; 31, 74.7,46.0), 10 of each `[QC8366]` `[G73.3,46.3 Tanaris]`.
29. Loot Stoley's Shipment from the Stolen Cargo (object 142181, five spawn points all at 72.1-72.2,46.7-46.8) `[QC2873]` `[G72.2,46.8 Tanaris]`.
30. Kill [TAR7883 Andre Firebeard] (level 45, not elite; one spawn 73.4,47.1) for Firebeard's Head `[QC2875]` "(~59% - one kill only, then abandon)" `[G73.4,47.1 Tanaris]`. Rule 12: a single named mob's item at 30-60% (`drop_rates.json` 9246, 58.89%, nether tooltip 12 Nov) is one kill only.
31. If the head did not drop: abandon `[QS2875 WANTED: Andre Firebeard]` (rule 9). Write it as a conditional `[OC]`/step pair the way round 1 writes "abandon if it does not drop" lines.
32. Ship Schedules: the four Southsea types drop a **Pirate's Footlocker** [9276] (qdb item row [1] = 7855, 7856, 7857, 7858; "Right Click to Open"), which holds the **Ship Schedule** [9250] (qdb item 9250 row [3] = [9276]; "This Item Begins a Quest", requires level 40). Open every footlocker; when the Ship Schedule turns up, `[QA2876 Ship Schedules]` (4,850 XP + 1g 30s at the hand-in; req 40, L45) - the line carries `[G73.3,46.3 Tanaris]`. No rate for either item is in the data (see D3 / Needs pull). Never picked up unless it drops, so rule 9 holds either way.

### Leg G - Steamwheedle Port hand-ins
33. At [TAR7881 Stoley] `[QT2873]` (3,900 XP + 50s) `[QA2874 Deliver to MacKinley]` (3,900 XP + 50s at the hand-in; req 40, L45; prerequisite 2873, row [12]; you get Stoley's Bottle [9245]; ends at "Sea Wolf" MacKinley [2501], Booty Bay 27.8,77.1) `[G67.1,24.0 Tanaris]`. Carried out to chapter 50 (Booty Bay bind, plan Threads): D1.
34. At [TAR7882 Security Chief Bilgewhizzle] `[QT8366]` (3,900 XP + 65s; gear call G1) `[QT2875]` (3,900 XP + 1g 30s, if you have the head) `[QT2876]` (4,850 XP + 1g 30s, if the Ship Schedule dropped) `[G67.1,23.9 Tanaris]`.

### Leg H - Caliph and back to Gadgetzan
35. Ride south-west to Waterspring Field: kill [TAR7847 Caliph Scorpidsting] (level 46, not elite; one spawn 61.8,38.2) for Caliph Scorpidsting's Head `[QC2781]` (82.69%, single dropper, `drop_rates.json` 8723; plain under rule 12) `[G61.8,38.2 Tanaris]`. Detour from the Port: Port - Caliph 15.8 units, Caliph - Gadgetzan 14 (against 15.8 straight).
36. At [TAR7407 Chief Engineer Bilgewhizzle] `[QT1691]` (3,750 XP + 65s) `[QT2781]` (5,050 XP + 1g 30s) `[G52.5,28.5 Tanaris]`; at [TAR7408 Spigot Operator Luglunket] `[QT1707]` (2,800 XP) if not done in Leg C `[G52.5,28.4 Tanaris]`. Do NOT take 2768 Divino-matic Rod from Bilgewhizzle (chapter 54; U6).
37. `[O]` Friz block only: at [TAR220984 Fizbuz Mithril] `[QT95312]` (315 XP) `[QA95321 Tazzik's Dues]` (3,150 XP at the hand-in; "Confront Tazzik", objective "Tazzik confronted"; Tazzik [260857] level 40, qdb rank blank) `[G51.7,27.8 Tanaris]`.
38. `[O]` Friz block only: ride back to Steamwheedle Port (~16 units) and confront [TAR260857 Tazzik] `[QC95321]` `[G67.3,24.0 Tanaris]`, then `[QT95321]` (3,150 XP) `[QA95472 Consolation Prize]` (Tazzik's Sweaty Shirt to Friz Frazzlespark, Powderfuse Port; 2,350 XP counted in chapter 48) `[G67.3,24.0 Tanaris]`. Ride back to Gadgetzan for chapter 47. Whether Tazzik is fought or talked to is unverified.
39. `[OC]` Check (section 7).

## 5. Gear calls (level-40 band, `score_items.py --band 40`, tooltips 2026-11-12.json; central [conservative])
- **G1 - 8366 Southsea Shakedown:** take **Southsea Mojo Boots** [20641] (cloth feet, +11 Int, +8 spell damage; 34.6 [26.6]). Runner-up Southsea Head Bucket [20640] is **plate** head (+6 Str +15 Sta, Defense +4): unusable. Replaces **Verger Greaves** (mail feet +7 Str +8 SP from chapter 38: 7x2.00 + 8x2.00 = 30.0 [22.0]) - an upgrade by 4.6 [4.6]; also beats Kodo Rustler Boots (26.0). Sell: Mojo 48s 29c, Bucket 48s 12c, Verger 44s 28c. Unless chapters 42-45 gave him feet over 34.6 (none in the plan's reward table).
- **2874 Deliver to MacKinley (handed in chapter 50, not here):** Swashbuckler Sash [9636] cloth waist +10 Str +9 Sta = 20.0 [20.0] loses to Twilight Initiate's Belt (29.8 [22.8], chapter 43 boss item) and to Violet Sash (+9 Int +6 SP, 27.2 [21.2], chapter 30); Shinkicker Boots [9637] is plate (+10 Str +9 Agi), unusable. Take the Shinkicker Boots to sell (47s 49c against 31s 54c). For the chapter-50 spec.
- 1707 Water Pouch Bounty: fixed reward Gadgetzan Water Co. Care Package [8484] (open it; contents not in the data).
- 95472 Consolation Prize (chapter 48 hand-in): Sweat-Stained Shirt [270334], shirt, no stats.
- No other kept quest here has a reward.

## 6. Out (silent: no tag)
Tanaris (`_decisions.tsv`):
- 1878 Water Pouch Bounty - repeatable follow-up of Water Pouch Bounty, 375 XP.
- 8365 Pirate Hats Ahoy! - drop under 30%: Southsea Pirate Hat 22.4% (7 droppers, best Southsea Dock Worker 30% of 1242).
- 97530 Dunemaul Dues - drop under 30%: Brilliantly Polished Bangle 4.3%.
- 2605 The Thirsty Goblin - drop under 30%: Laden Dew Gland 10.81%; 2606, 2641, 2661, 2662 - chain behind it.
- 8893 The Super Egg-O-Matic - no XP, nothing kept behind it.
- 4504 Super Sticky - Super Sticky Tar 32.9%, XP-only optional (rule 11).
- 4496 Bungle in the Jungle - Gorishi Scent Gland 5.0%; 4507, 4508 - chain behind it.
- 4450 Ledger from Tanaris (category 51) - Solid Crystal Leg Shaft 19.44%.
Not out but later (chapter 53, plan): 82, 10, 110, 113, 162, 1560, 97540, 2741, 3022, 351, 648, 3161, 5863, 2946, 2954, 3362, 3444 - no tag in this chapter. Thousand Needles (category 400): all out (Shimmering Flats chains grey at 42; Indurium 21.8%; Dream Dust 30.4% XP-only).

## 7. End check (`[OC]` text for the writer)
- Handed in here: 2872, 2873, 992, 97536, 1690, 1691, 1707, 2781, 8366, 2875 (or abandoned), 2876 (if it dropped); Friz block: 95296, 95383, 95312, 95321.
- In the log, carried out: **2874 Deliver to MacKinley** (Stoley's Bottle; MacKinley, Booty Bay, chapter 50); **1452 Rhapsody's Kalimdor Kocktail** with 3 Roc Gizzards (livers in Feralas, chapter 47; hand-in Aerie Peak, chapter 48); **3520 Screecher Spirits** (Feralas, chapter 47; hand-in Yeh'kinya, chapter 53); Friz block: **95472 Consolation Prize** (Friz, chapter 48); Cooking 225 only: **6610 Clamlette Surprise** (Dirge, chapter 53).
- Hearth = Gadgetzan. Flight point Gadgetzan taken. Next: Feralas by road.

## 8. Totals
| | quests | XP | money |
|---|---|---|---|
| Plan row 46 (required) | 12 | 41,990 | 7g 15s |
| Required handed in this chapter (spec) | 11 | 38,090 | 6g 65s |
| Required picked up here, handed in chapter 50 (2874) | 1 | 3,900 | 50s |
| Optional / conditional (Friz 95296 315 + 95383 315 + 95312 315 + 95321 3,150) | 4 | 4,095 | 00s |
Required list and sum equal the plan (12 quests, 41,990 XP, 7g 15s = 71,500c: 3,500 + 13,000 + 6,000 + 6,500 + 0 + 0 + 5,000 + 5,000 + 13,000 + 13,000 + 6,500 + 0); the difference is only where 2874's 3,900 XP and 50s land (D1). Optional equals the plan's 4,095. Not counted here: 1452 (chapter 48), 3520 (53), 95472 (48), 6610 (gate, 53). 2875 (3,900 + 1g 30s) is at 59%; 2876 (4,850 + 1g 30s) hangs on an unrated footlocker (D3).

## 9. Unverified / in-game test list
- The road Ratchet - Great Lift - Thousand Needles - Shimmering Flats - Gadgetzan, and which Great Lift object is the lift.
- Sandsorrow water hole: how close the widget must be, and whether the pool's west edge is clear of the elite trolls.
- Gnomish Garbage: where "a safe distance away from Gadgetzan and other garbage" is; whether a charge fails near town.
- Pirate's Footlocker drop rate and how often it holds the Ship Schedule.
- Whether Stoley offers 2873 without 2872 (qdb: no prerequisite).
- Tazzik's Dues: fight or talk; whether Fizbuz offers 95321 at all.
- Giant Egg drop on Rocs (Clamlette Surprise).
- Gadgetzan - Thalanaar flight (TaxiPath 323/324) once Thalanaar is known.

## 10. Needs pull
- Item 9276 Pirate's Footlocker and 9250 Ship Schedule: drop chance (Wowhead Forever item pages; the nether tooltips carry none). Settles D3.
- Item 12207 Giant Egg per-mob rates on Rocs (only if the Clamlette line is kept as more than a pickup).

## 11. Unsure
- U1 2872 Stoley's Debt starts in Booty Bay (MacKinley 27.8,77.1) and is not on chapter 45's list; this spec assumes chapter 45 picks it up (D2).
- U2 2874 Deliver to MacKinley ends in Booty Bay; this spec carries it to chapter 50 (D1).
- U3 2876 Ship Schedules: count it as required (plan) or make it conditional "if the Ship Schedule drops" (D3).
- U4 992's water hole sits 0.7-1.5 units from elite Sandfury trolls (42-44): keep plain with the approach note (as written), or label it (D4).
- U5 Gizzards: 25 kills on 19 Roc spawns is at rule 3's edge (more than ~25 kills on fewer than ~20 spawns); Braedyn's answer 3 makes 1452 required, so the spec says "keep killing Rocs until three". Confirm.
- U6 Chapter-53/54 quests given in Gadgetzan whose pickup costs nothing and has no timer field in the data (not added): 82 Noxious Lair Investigation (Fizzledowser, after 992; req 39), 2741 The Super Egg-O-Matic (Egg-O-Matic object 52.4,27.0; req 42; the Hippogryph Egg objects are in Feralas 57.1,76.3, so a pickup now lets chapter 47 or 51 take the egg), 3022 Handle With Care (Curgle Cranklehop 52.4,26.9; req 42; ends at Rut'theran), 2768 Divino-matic Rod (Chief Engineer Bilgewhizzle; Zul'Farrak, chapter 54). Not candidates: 5863 (req 44), 3362 (req 45), 3161 (Marvon 52.7,45.9, off the route; req 43), 1560 (escort).
- U7 Friz block: Fizbuz stands in Gadgetzan and Tazzik in the Port, so 95321 costs one extra Port round trip (~32 units) at the end; written that way.
- U8 If 2769 The Brassbolts Brothers (starts in Ironforge) or 2864 Tran'rek (starts at Krazek, Booty Bay) were picked up in earlier chapters, the road passes Wizzle Brassbolts (Thousand Needles 78.1,77.1) and Tran'rek stands in Gadgetzan (51.6,26.8): both counted in chapter 54. Not added.
- U9 6610 Clamlette Surprise: pickup here at Cooking 225, hand-in chapter 53; whether he will have Cooking 225 at 42 is not known (rule 5 targets stop at 175 by ~30).

## 12. Deviations from the route plan
- **D1** 2874 Deliver to MacKinley ends at "Sea Wolf" MacKinley [2501], Stranglethorn Vale 27.8,77.1 (quest row [2] = [[2501]]): it cannot be handed in in Tanaris. Picked up here, handed in at Booty Bay in chapter 50 (bind Booty Bay in the Threads). Chapter 46 earns 11 quests, 38,090 XP, 6g 65s; chapter 50 gains 3,900 XP and 50s. Exit level about 43.15 instead of 43.2.
- **D2** 2872 Stoley's Debt starts at MacKinley in Booty Bay (quest row [1] = [[2501]]): its pickup belongs to chapter 45, which the plan does not list.
- **D3** 2876 Ship Schedules starts from the Ship Schedule [9250], which comes out of a Pirate's Footlocker [9276] dropped by the four Southsea types (item rows [3] and [1]); the plan lists it plain with no drop flag, and no rate for either item is in the data. Kept as the plan has it, written as "when the Ship Schedule turns up"; whether it is counted is the main session's call.
- **D4** 992 Gadgetzan Water Survey's object is inside an elite camp (Sandfury, npc row [5] = 1, 42-44). The plan's elite check covered kill targets and droppers only. Kept plain with the approach note.
