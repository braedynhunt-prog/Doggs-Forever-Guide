# Spec 56 - Un'Goro Crater (13 Nov 2026, round 2 of the 30-60 guide)

Written against `docs/40-50-plan-2026-11-12.md` (second revision), section "### 56 Un'Goro Crater", and BRIEF.md (its last section wins). Facts checked 13 Nov against `tooling/qdb` 1.0.16 (quest rows [1] [2] [3] [7] [9] [10] [11] [12]; npc rows [3] [4] [5] [6] [9] [10] [11] [12]; object spawns; item rows [1] [2] [3]), `python tooling/qinfo.py` / `loc.py`, `data/zone_490.json` and `zone_357.json` (XP, money, reqlevel, side, itemchoices), `data/drop_rates.json`, `data/wowhead_quest_links.json`, `data/browser/r2_pages*_2026-11-1*.tsv`, nether.wowhead.com/forever tooltips (quests 4284 3882 4291 4501 87492 87494 3883 3845; items 11116 11114 280459 11107; read 13 Nov), `tooling/client/1.60.1.70938/TaxiNodes.csv` + `TaxiPath.csv`, `weights/score_items.py` functions at `--band 40` on `weights/tooltips/2026-11-12.json`, `python tooling/route_xp.py docs/40-50-route-2026-11-12.txt`. The neighbouring drafts `55-draft3.md` (exit: hearth Talrendis Point, 2941 carried) and `57-draft3.md` (entry: stands at Marshal's Refuge) were read for the carries only.

## 1. Header
- File: `56_UnGoro.lua` (group "Forever Shaman 30-60").
- `[N 47-49 Un'Goro Crater]`; next `[NX 48-49 Ironforge]` (plan's chapter 57 title); `[GA Alliance]`; class lines `[A Shaman]`.
- Description (suggested): `[D Forever Shaman 30-60 (Braedyn)\\The Borrower to Gadgetzan, then Un'Goro Crater from the Tanaris side: Marshal's Refuge (flight point), the raft and Linken's pack, J.D. Collie's crystals and pylons; then, as your level opens them, the Marshal's Refuge, Torwa Pathfinder and Spraggle Frock quests. The round ends here: what your level has not opened is where round 3 starts.]`
- Level: entry 47.5 (route_xp: 47.55); exit 48.4 on all four tiers at the 65% share. Per tier (route_xp `add_xp`, share 0.65, from 47.55): after A 47.84, after B 48.16, after C 48.28, after D 48.44. With required levels enforced (route_xp's walk) the chapter stops after Tier A at 47.8: Tier B needs 48 (about 20,000 XP short = 0.16 x 129,100), C 49, D 50.

### Level-check line (first `[OC]`)
"|cffffffffLevel 47-50|r - this chapter is built on required levels. Tier A (The Borrower, the raft and Linken's pack, J.D. Collie's crystals and pylons) needs 47 and its mobs are 48-50 in the east, up to 55 at the Western Pylon. Tier B (the Marshal's Refuge pickups, A-Me 01, Torwa Pathfinder's carcass and pheromones) needs 48; Tier C (Roll the Bones, Beware of Pterrordax) needs 49; Tier D (Ringo, Uncanny Crystal) needs 50. Do each tier when your level opens it; when it does not, the chapter stops there and round 3 starts from that tier (the Check at the end lists what is left). Under 47 nothing in the crater opens: hand in The Borrower and take the conditional Microcrystal Contamination if its scale has dropped (it needs 45). Tier A ends at about 47.8 on quest XP: the rest of 48 is kill XP on the east side's level 48-50 mobs (ravasaurs, threshers, fledgling pterrordax) or the conditional quest."

## 2. Entry state
- Stands at Talrendis Point, Azshara (end of chapter 55, `55-draft3.md` step 39). Hearth: Talrendis Point per that draft (`[S Talrendis Point]` at Berdun Cliffbrew 240482). The prompt allows Gadgetzan too: the route is written for both (section 3).
- Carried in: **2941 The Borrower** (from Daryn Lightwind, chapter 55; source item A Short Note 9329; ends Curgle Cranklehop 7763). Possibly a **A Mangled Journal** (item 11116) if one dropped earlier: it only drops in Un'Goro (item row [1], 48 Un'Goro npc ids), so no.
- Flight points known that matter: Talrendis Point (55), Theramore (round 1), Gadgetzan (`[P Gadgetzan]` in chapter 46's spec). New here: Marshal's Refuge.
- Training: none. No shaman trainer in Tanaris or Un'Goro (plan Threads: chapters 53-56 pass none; the 46 / 48 rows wait for chapter 57). Professions: no gate falls in this chapter (plan Threads). Vendors at the Refuge for restock only (no purchase planned, no price quoted): Nergal [12959] General Goods 43.3,7.7; Gibbert [3000] Weapon Merchant 44.1,7.2.

## 3. Travel and hearth
- **In, case 1 (hearth = Talrendis Point, as 55-draft3 leaves it):** at Jarrodenus [12577] Talrendis Point 11.9,77.6 Azshara (55-draft3) fly to Gadgetzan. TaxiPath 70938 has no Talrendis - Gadgetzan path: Talrendis (node 64) - Theramore (32) path 446 cost 630, Theramore - Gadgetzan (39) path 222 cost 730 (= 6s 30c + 7s 30c = 13s 60c if the cost field is copper, as 57-draft3 reads it; unverified). The game routes the two hops as one flight (unverified). Then bind at Gadgetzan (below).
- **In, case 2 (hearth = Gadgetzan):** hearth from Talrendis Point; no flight.
- **Gadgetzan:** flight master Bera Stonehammer [7823] L55 elite 51.0,29.3 Tanaris; Innkeeper Fizzgrimble [7733] 52.5,27.9 Tanaris; Curgle Cranklehop [7763] 52.4,26.9 Tanaris.
- **Bind: `[S Gadgetzan]` at Fizzgrimble** (case 1; in case 2 it is already Gadgetzan). Reason: the DB has no innkeeper in Un'Goro (no npc with a spawn in zone 490 carries subName Innkeeper: the only subNames are Weapon Merchant, General Goods Vendor, Flight Master, Simone's Pet), and chapter 57 starts with Marshal's Refuge - Gadgetzan - Theramore: a Gadgetzan hearth replaces its first flight. Talrendis Point is of no further use in round 2.
- **Gadgetzan to the crater (unverified, no road data):** ride west-south-west across Tanaris to the crater rim and down the ramp into south-east Un'Goro. The only data hint: 4291's text puts Torwa Pathfinder [9619] (71.6,76.0 Un'Goro) "near the entrance to Un'Goro Crater". Use `[G71.6,76.0 Un'Goro Crater]` as the arrival point. Ghost Wolf / ram for the ride.
- **Marshal's Refuge:** flight master Gryfe [10583] L55 elite 45.2,5.8 Un'Goro: `[P Marshal's Refuge]` on arrival (TaxiNodes 79, "Marshal's Refuge, Un'Goro Crater"; links Gadgetzan 39 by paths 452/458, Cenarion Hold 73, node 72).
- **Out:** every tier ends at Marshal's Refuge; chapter 57 flies Marshal's Refuge - Gadgetzan - Theramore (or hearths to Gadgetzan). Hearth on exit: Gadgetzan.

### Danger lines (DB rank in npc row [5]: 1 elite, 2 rare elite, 4 rare; faction template row [11]: 14 = aggressive "Monster", 7 = "Creature", meaning unverified)
- **Devilsaurs (elite, 54-56, faction 14):** Devilsaur [6498] at 34.6,22.4 / 57.3,23.7 / 31.2,36.4; Tyrant Devilsaur [6500] at 74.2,33.0 / 50.1,60.7; Ironhide Devilsaur [6499] at 57.3,61.8. They patrol in Classic (the DB has only these points; patrol paths not in the data). Every leg crosses at least one: name them on the leg's travel line.
- **Stegodons (elite, 52-55, faction 14):** Stegodon [6501] 13 points, Plated [6502] 7, Spiked [6503] 3, Thunderstomp [6504] 2, all at x26-41 y58-81 (south-west): the Dinosaur Bones (3882), the Research Equipment (3881) and the Western Pylon (4288) lie among them.
- **Stone Guardians (elite, 60-61, faction 7):** [6560] at 53.9,36.8 / 52.9,37.5 / 43.5,31.5 / 70.6,38.9 (3.1 from the Crate of Foodstuffs) / 76.0,54.1 (4.3 from the Eastern Pylon) / 72.2,70.5 and 70.7,77.7 (by Torwa). Whether they attack on sight is unverified.
- **Fire Plume Ridge (Ringo):** Blazerunner [9376] L56 elite at 49.4,49.3 (2.5 from Ringo), Baron Charr [14461] L58 elite at 43.8,48.1; Living Blaze 54-55, Scorching Elemental 53-54 round 45-55,42-57.
- **Rares / named:** King Mosh [6584] L60 rare elite 35.3,36.0 (in the Frenzied Pterrordax area); Gruff [6583] L57 rare elite 38.0,75.5; Clutchmother Zavas [6582] L54 rare on the Gorishi Hive Hatchery itself (48.7,85.3); Gorishi Hive Queen [10041] L56 and Hive Guard [10040] L54 at 43.9,81.4; Uhk'loc [6585] L53 rare 68.5,12.7 and U'cha [9622] L55 68.1,12.6 (4 units north of A-Me 01); Ravasaur Matriarch [6581] L50 rare 62.4,66.0 (2.7 from the raft); Lar'korwi [9684] L56 (not elite) 79.7,49.8 (2.5 from the Eastern Pylon).
- **Unknown:** 21 points of a Forever npc "Venomhide Ravasaur" [269206], level 60-60, no rank, no faction id, friendlyToFaction "H" (row [12]), all at x68-72 y68-80 - on top of Torwa Pathfinder (0.4 units) and 2.2 units from the Damaged Blue Crystal (87492). Not the Classic Venomhide Ravasaur [6508] (50-51). What they are is unverified (Unsure U3); the chapter cannot avoid Torwa.

## 4. Route

Mob levels below are npc rows [3]-[4]; spawn centres and ranges from row [6] (zone 490). XP and money from `data/zone_*.json`.

### Leg A0 - Gadgetzan (Tier A, needs nothing new)
1. `[OC]` level-check line (section 1).
2. Case 1: at [TAR12577 Jarrodenus] fly to `[F Gadgetzan]` (two hops through Theramore) `[G11.9,77.6 Azshara]`. Case 2: hearth to Gadgetzan `[H Gadgetzan]`. (Lua writer: the chapter can carry only one of these as a held step; 55-draft3 leaves the hearth at Talrendis, so case 1 is the step and case 2 an `[OC]` note.)
3. At [TAR7763 Curgle Cranklehop] `[QT2941 The Borrower]` (1,100 XP, no money; req 42, L48; pre 2940 done in chapter 55) `[G52.4,26.9 Tanaris]`. Curgle then offers 2944 The Super Snapper FX: out, silent.
4. At [TAR7733 Innkeeper Fizzgrimble] bind `[S Gadgetzan]` `[G52.5,27.9 Tanaris]` (case 1 only).
5. `[OC]` ride note: west-south-west across Tanaris to the crater rim and down into Un'Goro (road unverified).

### Leg A1 - the raft (Tier A; mobs 48-50 in the south-east)
6. Ride into the crater to Torwa Pathfinder's camp `[G71.6,76.0 Un'Goro Crater]`. `[OC]` Torwa's quests need 48 and 50: nothing to take at 47. Danger: the unknown level-60 Venomhide Ravasaurs [269206] stand round him (U3); Stone Guardians (elite 60) at 72.2,70.5 and 70.7,77.7.
7. At the Wrecked Raft (object 161505, found object, not an NPC) `[QA3844 It's a Secret to Everybody]` (1,250 XP; req 47, L52; no prerequisite) `[G63.0,68.6 Un'Goro Crater]`. Ravasaurs [6505] 48-49 (38 points, x57-68 y60-83) and Ravasaur Runners [6506] 49-50 round the pond; Ravasaur Matriarch (rare 50) 2.7 units north-west.
8. At A Small Pack (object 161504) beside it `[QT3844]` (1,250 XP) `[QA3845 It's a Secret to Everybody]` (5,100 XP at the hand-in; req 47; pre 3844, row [12]) `[G63.1,69.1 Un'Goro Crater]`. You get A Small Pack (item 11107, "Right Click to Open", source item, row [10]): open it for the Large Compass [11104], Curled Map Parchment [11105] and Lion-headed Key [11106] (item row [3] = 11107; the three objectives, quest tooltip) `[UI11107]` (unverified tag).

### Leg A2 - to Marshal's Refuge (Tier A)
9. Ride north to Marshal's Refuge `[G45.2,5.8 Un'Goro Crater]`: keep to the east side (x62-72, mobs 48-51) to about y35, then north-west past the tar pits (Tar Beasts 50-51, Tar Creepers 51-52, Lurkers 52-54, Lords 53-54 at x41-65 y15-36) - path unverified. Danger: Tyrant Devilsaur at 74.2,33.0, Devilsaur at 57.3,23.7, Stone Guardians at 70.6,38.9 and 53.9,36.8; the gorilla caves (50-53, x60-69 y13-19) east of the way.
10. At [TAR10583 Gryfe] `[P Marshal's Refuge]` `[G45.2,5.8 Un'Goro Crater]`.
11. At [TAR8737 Linken] `[QT3845]` (5,100 XP) `[G44.7,8.1 Un'Goro Crater]`; `[QA3908 It's a Secret to Everybody]` if he offers it (5,100 XP counted in round 3; req 47; pre 3845; you get Linken's Training Sword [11133], source item; ends Donova Snowden [9298], Winterspring 31.3,45.2): carried to round 3, never handed in this round (plan, "LATER" in `_decisions.tsv`). Label: carried, not counted.
12. At [TAR9117 J.D. Collie] (in the cave at the Refuge; 3941's text) `[QA4284 Crystals of Power]` (5,250 XP + 80s at the hand-in; req 47, L53; no prerequisite) `[G41.9,2.7 Un'Goro Crater]`.

### Leg A3 - Power Crystals, east side (Tier A; mobs 48-51)
13. Collect 7 Red, 7 Yellow, 7 Green and 7 Blue Power Crystals (quest tooltip counts; items 11186 / 11188 / 11185 / 11184) from the crystal clusters `[QC4284]` `[G66.0,50.0 Un'Goro Crater]`. Data: each colour has two object ids (164660/164780 red, 164661/164781 yellow, 164659/164779 green, 164658/164778 blue) sharing the same 148 points over the whole crater; the east side x56-79 y20-79 holds 63 of them (by 10x10 square: 70-79,60-69 10; 70-79,50-59 7; 60-69,60-69 6; 60-69,70-79 8; 60-69,20-29 6; 60-69,40-49 5; 70-79,40-49 5; 70-79,30-39 4) and that is the crater's lowest band: Ravasaurs 48-51, Bloodpetal Lashers 48-49 and Threshers 49-50, Muculent Ooze 48-50, Fledgling Pterrordax 48-50, Young Diemetradon 49-50. Plain (objects; rule 12 does not apply). Which colour a point gives is not in the data; crystals that are not quest items before 4284 is accepted (unverified). Loop: Refuge - east side south to about y75 - back north the same way. Danger as on step 9; Stone Guardian at 76.0,54.1; Ironhide Devilsaur 57.3,61.8; Tyrant Devilsaur 50.1,60.7 (keep east of x60 south of y55).
14. `[OC]` A Mangled Journal (11116) and the Crystal Infused Scale (280459) can drop on this loop: keep them (Tier B and the conditional 87494).

### Leg A4 - the pylons (Tier A)
15. At [TAR9117 J.D. Collie] `[QT4284]` (5,250 XP + 80s) `[QA4285 The Northern Pylon]` `[QA4287 The Eastern Pylon]` `[QA4288 The Western Pylon]` (3,950 XP each at the hand-in; req 47, L53; each pre 4284 completed, row [12]) `[G41.9,2.7 Un'Goro Crater]`.
16. Discover the Northern Crystal Pylon (object 164955) `[QC4285]` `[G56.5,12.5 Un'Goro Crater]`. Pterrordax 50-52 round it (24 of their 63 points at x50-59 y0-19); Devilsaur 11.2 units south (57.3,23.7); Uhk'loc 12 units east.
17. Discover the Eastern Crystal Pylon (object 164957) `[QC4287]` `[G77.2,50.0 Un'Goro Crater]`. Way down the east side (48-51 band). Danger: Stone Guardian 4.3 units south (76.0,54.1); Lar'korwi (L56) 2.5 units east; Tyrant Devilsaur 74.2,33.0 on the way.
18. Discover the Western Crystal Pylon (object 164956) `[QC4288]` `[G23.9,59.2 Un'Goro Crater]`. The hardest stop of the tier: Frenzied Pterrordax 51-54, Bloodpetal Trappers 52-53, Glutinous Ooze 52-54, Elder Diemetradon 53-55 round it; Plated Stegodon (elite) 4.6 units east, Stegodons 6.6 / 6.9. Ride across south of Fire Plume Ridge (Tyrant Devilsaur 50.1,60.7, Ironhide 57.3,61.8 - path unverified) or back north round the crater's west side (Devilsaurs 31.2,36.4 and 34.6,22.4, King Mosh 35.3,36.0).
    Order note: the three pylons are ride-to stops, not kill legs; they are ordered for travel (Northern is 13 units from the Refuge) with the Western, the highest band, last.
19. Back at [TAR9117 J.D. Collie] `[QT4285]` `[QT4287]` `[QT4288]` (3,950 XP each) `[QA4321 Making Sense of It]` (530 XP; req 47; pre all three pylons, row [11]; "Speak with J.D. Collie in a moment") then `[QT4321]` (530 XP; fixed reward Crystal Pylon User's Manual [11482], not gear) `[G41.9,2.7 Un'Goro Crater]`. Collie then offers the six Crystal quests (4381-4386, no XP): out, silent. Whether 4321 completes at once or after a short wait is unverified.
20. `[OC]` Tier A done: about 47.8 on quest XP. Tier B needs 48.

### Leg B0 - gate (Tier B, needs 48)
21. `[OC]` "|cffffffffTier B - level 48|r: the Marshal's Refuge pickups, A-Me 01, the two crates, Torwa Pathfinder and the Gorishi hive. Under 48: this is where the chapter ends for now; round 3 starts here (see the Check at the end). The level-48 quests: Williden's Journal, Alien Ecology, Expedition Salvation, Chasing A-Me 01, The Fare of Lar'korwi, The Scent of Lar'korwi."

### Leg B1 - Refuge pickups (Tier B)
22. At [TAR9270 Williden Marshal] `[QA3881 Expedition Salvation]` (5,250 XP + 40s at the hand-in; req 48, L53; no prerequisite) `[G44.0,7.1 Un'Goro Crater]`.
23. At [TAR9271 Hol'anyee Marshal] beside him `[QA3883 Alien Ecology]` (5,100 XP + 40s; req 48, L52; you get the Unused Scraping Vial [11132], row [10]) `[G43.9,7.2 Un'Goro Crater]`.
24. If you carry A Mangled Journal (11116; "Requires Level 48", "This Item Begins a Quest", "Property of Williden Marshal", tooltip 13 Nov): use it `[QA3884 Williden's Journal]` (3,550 XP; req 48, L50; starts from the item, quest row [1] = item 11116) and at [TAR9270 Williden Marshal] `[QT3884]` (3,550 XP) `[G44.0,7.1 Un'Goro Crater]`. Label: see Deviation D1 (plan: plain; data: a drop-start of unknown rate). If it has not dropped yet, the hand-in comes at step 36.
25. At [TAR9618 Karna Remtravel] `[QA4243 Chasing A-Me 01]` (2,650 XP; req 48, L53; no prerequisite) `[G46.4,13.4 Un'Goro Crater]`.

### Leg B2 - east and south-east (Tier B; mobs 48-53)
26. Ride east to A-Me 01 `[QT4243]` at [TAR9623 A-Me 01] (2,650 XP; she is the ender, row [2]) `[G67.7,16.8 Un'Goro Crater]`. She stands in the gorilla ground (Un'Goro Gorilla 50-51, Stomper 51-52, Thunderer 52-53, 26 points each at x60-69 y13-19); Uhk'loc (rare 53) and U'cha (55) 4 units north. Do not take 4244 (Mithril Casing, out; silent). Danger on the way: Devilsaur 57.3,23.7.
27. South to the Crate of Foodstuffs (object 161526, one point) `[QC3881]` (item 11113) `[G68.5,36.5 Un'Goro Crater]`. Stone Guardian (elite 60) 3.1 units south-east (70.6,38.9), Tyrant Devilsaur 6.7 units (74.2,33.0). Young Diemetradon 49-50, Bloodpetal Threshers 49-50 round it.
28. South to [TAR9619 Torwa Pathfinder] `[QA4290 The Fare of Lar'korwi]` (5,250 XP; req 48, L53; no prerequisite) `[G71.6,76.0 Un'Goro Crater]`. If you carry a Crystal Infused Scale: step 34 first.
29. North to the Fresh Threshadon Carcass (object 166863, one point) for a Piece of Threshadon Carcass (11504) `[QC4290]` `[G68.7,56.7 Un'Goro Crater]`. Ravasaur Hunters 49-50 and Venomhide Ravasaurs [6508] 50-51 (x62-73 y45-61); Stone Guardian 7.7 units east (76.0,54.1).
30. At [TAR9619 Torwa Pathfinder] `[QT4290]` (5,250 XP) `[QA4291 The Scent of Lar'korwi]` (5,250 XP; req 48; pre 4290, row [12]) `[G71.6,76.0 Un'Goro Crater]`.
31. Kill [TAR9683 Lar'korwi Mate] (49-50, not elite; 12 points at x58-71 y59-80, most at 60-69,60-69) for 2 Ravasaur Pheromone Glands (11509) `[QC4291]` "(74.6% - budget ~3 kills)" `[G64.9,68.2 Un'Goro Crater]`. Rule 12: single named dropper at 60%+, plain (`drop_rates.json`: nether tooltip, single dropper, 12 Nov).
32. At [TAR9619 Torwa Pathfinder] `[QT4291]` (5,250 XP) `[G71.6,76.0 Un'Goro Crater]`. He then offers 4292 The Bait for Lar'korwi (L56, req 48, Lar'korwi L56): not in round 2's pool (quest level above 55), no tag.
33. (kill-leg order: these Torwa kills, 49-50, are the tier's lowest; the hive and the Research Equipment follow.)
34. `[O]` conditional: if a Crystal Infused Scale (280459) has dropped, use it `[QA87494 Microcrystal Contamination]` and at [TAR9619 Torwa Pathfinder] `[QT87494]` (5,650 XP + 85s; req 45 on Wowhead, blank in qdb; Wowhead side Both, no start, end Torwa) `[G71.6,76.0 Un'Goro Crater]`. Not counted. Gear: section 5.

### Leg B3 - the hive and the Research Equipment (Tier B; mobs 51-55)
35a. South-west to the Gorishi hive: use the Unused Scraping Vial at a Gorishi Hive Hatchery (object 174793, one DB point) for a Hive Wall Sample (11131) `[QC3883]` `[UI11132]` (unverified tag; whether the vial is used on the object or the object clicked is unverified) `[G48.7,85.3 Un'Goro Crater]`. Gorishi Wasps / Workers 51-52, Reavers 51-53, Stingers / Tunnelers 52-53 (x42-56 y72-88). Clutchmother Zavas (rare 54) stands on the DB point itself; Hive Queen (56) and Hive Guard (54) at 43.9,81.4, 6 units west. The quest text says "chambers with the hanging larval spawns": other hatcheries are not in the DB.
35b. North-west to the Research Equipment (object 161521, one point) `[QC3881]` (item 11112) `[G38.5,66.1 Un'Goro Crater]`. Danger: Plated Stegodon (elite 52-54) 1.5 units away (37.5,67.2), Stegodons 2.2 and 3.7 units; Gruff (rare elite 57) 9.5 units south. Elder Diemetradon 53-55 and Glutinous Ooze 52-54 round it. See Deviation D2.
36. Back north to Marshal's Refuge (path round the west side: Devilsaurs 31.2,36.4 and 34.6,22.4, King Mosh 35.3,36.0; unverified) and at [TAR9270 Williden Marshal] `[QT3881]` (5,250 XP + 40s) and, if the journal has dropped by now, `[QA3884]` / `[QT3884]` (3,550 XP) `[G44.0,7.1 Un'Goro Crater]`; at [TAR9271 Hol'anyee Marshal] `[QT3883]` (5,100 XP + 40s) `[G43.9,7.2 Un'Goro Crater]`. Hol'anyee also starts 92020 (not in the pool; no tag; U5).

### Leg C0 - gate (Tier C, needs 49)
37. `[OC]` "|cffffffffTier C - level 49|r: Roll the Bones and Beware of Pterrordax. Under 49: the chapter ends here for now (Check)."

### Leg C1 - pickups (Tier C)
38. At [TAR9272 Spark Nilminer] `[QA3882 Roll the Bones]` (4,900 XP; req 49, L51; no prerequisite) `[G43.5,7.4 Un'Goro Crater]`.
39. At the Beware of Pterrordax sign (object 174682, found object) `[QA4501 Beware of Pterrordax]` (5,650 XP; req 49, L55; no prerequisite) `[G43.5,8.4 Un'Goro Crater]`.

### Leg C2 - kills, lowest first (Tier C; mobs 50-55)
40. Kill 10 [TAR9166 Pterrordax] (50-52, not elite; 63 points, 24 of them at x50-59 y0-19 right east of the Refuge; others x40-59 y78-99) `[QC4501]` `[G55.0,10.0 Un'Goro Crater]`. Devilsaur 57.3,23.7 south of them.
41. Kill 15 [TAR9167 Frenzied Pterrordax] (51-54, not elite; 202 points at x20-43 y19-79, densest 20-39,20-49) `[QC4501]` `[G28.0,38.0 Un'Goro Crater]`. Danger: Devilsaurs at 31.2,36.4 and 34.6,22.4 in this ground, King Mosh (rare elite 60) 35.3,36.0.
42. South to the bone field: 8 Dinosaur Bones (11114) from the Dinosaur Bone piles (object 161527, 20 points at x29-39 y62-78: 31.0,72.2 / 32.7,73.5 / 30.9,78.0 / 31.0,77.4 / 31.9,76.3 / 31.2,77.3 / 32.9,62.7 / 31.1,77.7 / 31.1,78.0 / 39.2,75.3 / 37.2,72.7 / 34.7,72.4 / 34.5,72.0 / 38.6,77.5 / 36.3,65.2 / 34.8,67.5 / 31.5,68.9 / 30.3,70.8 / 29.2,72.6 / 35.6,75.8) `[QC3882]` `[G31.5,74.0 Un'Goro Crater]`. Plain by rule 12 (object source). The bones also drop from the non-elite Young Diemetradon / Diemetradon / Elder Diemetradon (9162-9164, 49-55; item row [1]; rate not in the data). **Every pile lies 0.4-3.0 units from an elite stegodon** (Stegodon 52-53, Plated 52-54, Spiked 53-54, Thunderstomp 54-55; faction 14): pull nothing, loot from the edge, or kill the Diemetradons of steps 41-42 for the drop. See Deviation D2.
43. Back to Marshal's Refuge: at [TAR9272 Spark Nilminer] `[QT3882]` (4,900 XP; gear section 5) `[G43.5,7.4 Un'Goro Crater]`; at [TAR9997 Spraggle Frock] `[QT4501]` (5,650 XP; gear section 5) `[G43.6,8.5 Un'Goro Crater]`.

### Leg D0 - gate (Tier D, needs 50)
44. `[OC]` "|cffffffffTier D - level 50|r: Lost!, A Little Help From My Friends, Uncanny Crystal. Under 50: the chapter ends here for now (Check)."

### Leg D1 - Torwa, then Ringo (Tier D; mobs 48-51, then 53-58)
45. At [TAR9997 Spraggle Frock] `[QA4492 Lost!]` (2,800 XP; req 50, L55; no prerequisite; you get Spraggle's Canteen [15722], row [10]) `[G43.6,8.5 Un'Goro Crater]`.
46. Ride to [TAR9619 Torwa Pathfinder] `[QA87492 Uncanny Crystal]` (5,650 XP + 85s; req 50, L55; Wowhead: Alliance, start and end Torwa, "Sharable", no series; qdb row [9] item 280417) `[G71.6,76.0 Un'Goro Crater]`. Path as step 9 in reverse.
47. The Damaged Blue Crystal (object 672518, one point) `[QC87492]` `[G66.3,75.2 Un'Goro Crater]`. 2.2 units from the level-60 Venomhide Ravasaur [269206] cluster (U3).
48. At [TAR9619 Torwa Pathfinder] `[QT87492]` (5,650 XP + 85s; no reward item in zone_490.json) `[G71.6,76.0 Un'Goro Crater]`. Forever-only check (BRIEF): qdb rows [11]/[12] empty, Wowhead series empty: no prerequisite.
49. North-west to Fire Plume Ridge: at [TAR9999 Ringo] (L54, not elite, friendly) `[QT4492]` (2,800 XP) `[QA4491 A Little Help From My Friends]` (5,650 XP; req 50; pre 4492, row [12]; you get Spraggle's Canteen [11804], row [10]) `[G51.9,49.9 Un'Goro Crater]`. Danger: Blazerunner (elite 56) 2.5 units west, Baron Charr (elite 58) 8.3 units west, Tyrant Devilsaur 11 units south (50.1,60.7); Living Blaze 54-55, Scorching Elementals 53-54 round the ridge.
50. Lead Ringo to Spraggle Frock at Marshal's Refuge; "If Ringo faints, use Spraggle's Canteen to revive him" (quest text) `[QC4491]` `[UI11804]` (unverified tag) `[G43.6,8.5 Un'Goro Crater]`. Path not in the data: straight north passes the tar pits (Lurkers 52-54, Lords 53-54 at x41-54 y15-28) between the Devilsaurs at 34.6,22.4 and 57.3,23.7. If the escort fails, take it again from Ringo (whether he respawns at once is unverified).
51. At [TAR9997 Spraggle Frock] `[QT4491]` (5,650 XP; gear section 5) `[G43.6,8.5 Un'Goro Crater]`.

### End
52. `[OC]` Check (section 7).

Lua writer note on the gates: steps 21, 37 and 44 are `[OC]` notes; the `[QA]` steps after them hold the cursor until he skips them. How a player leaves a Guidelime chapter in the middle (skip the remaining steps, or go on to chapter 57) is for the main session to settle (U1).

## 5. Gear calls (level-40 band, central weights; `weights/score_items.py` functions on `weights/tooltips/2026-11-12.json`; worn items from round 1's gear lines and the plan's best-reward table)
- **3882 Roll the Bones** (choice): Excavator's Utility Belt [11909] (leather waist +4 Sta +16 Int) 27.0; Archaeologist's Quarry Boots [11908] (cloth feet +9 Agi +10 Sta +9 Int) 25.3. Neither is an upgrade: waist on entry is the Twilight Initiate's Belt (29.8, chapter 43 boss item) or the Vinehedge Cinch / Nightscale Girdle (28.0, chapters 50 / 55); feet are the Southsea Mojo Boots (34.6, chapter 46). Take the Quarry Boots to vendor (98s 86c vs 82s 67c). Exception: if your belt scores under 27.0, take the Utility Belt.
- **4501 Beware of Pterrordax** (choice): Grotslab Gloves [11918] (mail hands +12 Agi +12 Int) 33.7; Cragplate Greaves [11919] plate, unusable. Below the Witherseed Gloves (48.5, chapter 53) and the Prisoner Handwraps (cloth hands +12 Spi +15 SP, chapter 40; 60.0 by the same weights, computed by hand: 2.5 x 12 + 2.0 x 15): vendor. Sell prices: Cragplate Greaves 95s 72c, Grotslab Gloves 95s 37c: take the Greaves.
- **4491 A Little Help From My Friends** (choice): Treetop Leggings [11911] (cloth legs +8 Sta +8 Int +18 Spi) 58.5; Clayridge Helm [11913] (mail head +16 Agi +15 Spi) 55.4; Yesterday's Pants [270122] (leather legs +14 Str +12 Sta +9 Spi) 50.5; Bejeweled Legguards [11910] plate, unusable. Legs: Apprentice Sorcerer's Slacks (73.7, chapter 31) stay. Head: the Engineer's Guild Headpiece (75.0, chapter 51 boss item) stays; **if you have no Headpiece** (it is one boss kill in Zul'Farrak), take the Clayridge Helm over the Saltseer's Helm (about 48.8 at band 40 by hand: 1.69 x 12 + 2.5 x 5 + 2.0 x 8; chapter 31). Otherwise vendor: Yesterday's Pants sell best (1g 67s 17c; Clayridge 1g 40s 44c, Treetop 1g 23s 92c).
- **87494 Microcrystal Contamination** (conditional; choice): Crystal-flecked Waistguard [281262] (mail waist +6 Str +15 Int) 37.3 - wear it, it beats the Twilight Initiate's Belt (29.8) and the Vinehedge Cinch / Nightscale Girdle (28.0); Crystal-flecked Cord [281261] (leather waist +9 Sta +14 Int) 23.7.
- **4321 Making Sense of It**: Crystal Pylon User's Manual [11482], fixed, not gear.
- No other kept quest has a reward item (`zone_490.json` itemchoices / itemrewards empty for 3844 3845 4284 4285 4287 4288 3884 3883 3881 4243 4290 4291 4492 87492; 2941 empty in `zone_357.json`).
- Required level of the reward items: the 12 Nov tooltips carry no "Requires Level" line for any of them.

## 6. Out (silent in the guide; reasons copied from `_decisions.tsv`)
- 3909 The Videre Elixir - chain behind Muigin and Larion
- 3912 Meet at the Grave - chain behind 3909 The Videre Elixir
- 3913 A Grave Situation - chain behind 3912
- 3914 Linken's Sword - chain behind 3913
- 3941 A Gnome's Assistance - chain behind 3914
- 3942 Linken's Memory - chain behind 3941
- 4084 Silver Heart - drop under 30%: Silvery Claws 6.9%
- 4005 Aquementas - chain behind 4084
- 3961 Linken's Adventure - chain behind 4005
- 4141 Muigin and Larion - Bloodpetal 35.3% - XP-only optional (rule 11); A Visit to Gregan, Haze of Evil and The Videre Elixir go with it
- 4142 A Visit to Gregan - chain behind 4141
- 4143 Haze of Evil - chain behind 4142
- 4144 Bloodpetal Sprouts - chain behind 4143
- 4244 Chasing A-Me 01 - drop under 30%: Mithril Casing 2.2%
- 4245 Chasing A-Me 01 - chain behind 4244
- 4289 The Apes of Un'Goro - drop under 30%: Un'Goro Thunderer Pelt 23.08%
- 4301 The Mighty U'cha - chain behind 4289
- 4502 Volcanic Activity - drop under 30%: Un'Goro Ash 9.5%
- 4503 Shizzle's Flyer - Webbed scales 33% - XP-only optional (Shizzle's Muzzle is a leather shoulder at level 50)
- 4381 Crystal Restore, 4382 Crystal Force, 4383 Crystal Ward, 4384 Crystal Yield, 4385 Crystal Charge, 4386 Crystal Spire, 5150 Dadanga is Hungry! - no XP, nothing kept behind it
- 2944 The Super Snapper FX (Curgle, Tanaris) - elite outside a dungeon (rule 13): Gammerita (48 elite)
- Round 3, not picked up: the Morrowgrain chain (3763 and on), 4513 A Little Slime Goes a Long Way (plan, "Left for round 3"). Not in the pool: 4292 The Bait for Lar'korwi (L56), 92020 (U5).

## 7. End check
`[OC]` Check, by where he stops:
- **Whatever tier he stops at, the log holds:** 3908 It's a Secret to Everybody (Linken's Training Sword, to Donova Snowden, Winterspring - round 3), plus the other round-3 carries from earlier chapters (1475, 624, 7066 and Return to the Hinterlands, as 57-draft3 lists them). Handed in here: 2941 and every quest of the tiers he played. Hearth: Gadgetzan. Flight point new: Marshal's Refuge. He stands at Marshal's Refuge; chapter 57 flies out from there.
- **Stops after Tier A (under 48)** - left for round 3 (11 quests, 51,700 XP): Tier B 3884, 3883, 3881, 4243, 4290, 4291; Tier C 3882, 4501; Tier D 4491, 4492, 87492. Keep A Mangled Journal (11116) if it has dropped.
- **Stops after Tier B (under 49)** - left (5 quests, 24,650 XP): 3882, 4501, 4491, 4492, 87492 (and 3884 if the journal never dropped).
- **Stops after Tier C (under 50)** - left (3 quests, 14,100 XP): 4491, 4492, 87492.
- **All four tiers** - nothing of the chapter left.
- No quest of this chapter may be left accepted and unfinished: 4492 and 4491 are taken only in Tier D and finished in it; 87494 (conditional) is handed in at Torwa on the next Torwa stop, or carried into round 3 if the scale drops after the last one (it ends at Torwa, where round 3 starts), or `[QS87494]`.

## 8. Totals
| tier | quests | XP | money | level after (share 0.65, from 47.55) |
|---|---|---|---|---|
| A (req 42/47) | 8: 2941 3844 3845 4284 4285 4287 4288 4321 | 25,080 | 80s | 47.84 |
| B (req 48) | 6: 3884 3883 3881 4243 4290 4291 | 27,050 | 80s | 48.16 |
| C (req 49) | 2: 3882 4501 | 10,550 | 0 | 48.28 |
| D (req 50) | 3: 4491 4492 87492 | 14,100 | 85s | 48.44 |
| **total** | **19** | **76,780** | **2g 45s** | |
- Equals the plan's XP table row (19 required, 76,780 XP, 2g 45s). Optional / conditional: 87494, 5,650 XP + 85s (plan: 5,650). Carried, not counted: 3908 (5,100, round 3).
- If D1 is accepted (3884 conditional): 18 required, 73,230 XP, Tier B 23,500.

## 9. Unverified / in-game test list; Needs pull; Unsure
**Unverified / test list**
- The ride Gadgetzan - crater rim - the ramp into south-east Un'Goro; whether the ramp arrives by Torwa (71.6,76.0).
- The Talrendis Point - Gadgetzan flight routed through Theramore as one flight; its price (cost fields 630 + 730).
- Whether quest-start objects (the Wrecked Raft, the Pterrordax sign) and the A Mangled Journal item offer their quest below its required level (the journal says "Requires Level 48" on its tooltip); whether the journal can be looted under 48 and kept.
- Whether the Power Crystal objects can be looted before 4284 is accepted; which colour each point gives.
- Whether the pylon quests are offered only after Crystals of Power is handed in (qdb row [12] = 4284) or with it.
- Making Sense of It: done at once or after Collie's talk.
- Alien Ecology: how the Scraping Vial is used; where the other hatcheries are.
- The Dinosaur Bone piles among the elite stegodons: can they be looted without a pull; the Diemetradon bone drop rate.
- Stone Guardians (faction 7): hostile on sight or not.
- The 21 level-60 "Venomhide Ravasaur" [269206] round Torwa (U3).
- Ringo's escort: path, faint mechanic, respawn after a failure.
- Devilsaur patrol paths (the DB has single points).
**Needs pull**
- Wowhead Forever item page 11116 A Mangled Journal (dropped-by listview) for its rate: settles D1.
- Wowhead Forever NPC page 269206 (classification, level, reaction): settles U3.
- Wowhead Forever item page 11114 Dinosaur Bone (Diemetradon rows) if D2 goes the drop way.
**Unsure**
- U1 Tier gates: the brief wants each tier as its own block that he can stop after. Guidelime has an `[XP]` goal tag (used once, 02_LochModan.lua:161) but it would hold the cursor; the gates are written as `[OC]` notes. How he leaves the chapter in the middle is the main session's call.
- U2 Order inside tiers: kill legs are ordered by mob level (B: mates 49-50, then the hive 51-54 and the stegodon ground; C: Pterrordax 50-52, Frenzied 51-54, the bones); ride-to stops (A-Me 01, the crates, the pylons) are placed for travel. Strict mob-level order would add about two crater crossings.
- U3 Venomhide Ravasaur [269206]: level 60, friendlyToFaction "H", 21 points round Torwa. If hostile to Alliance at 60, Torwa's three quests (4290, 4291, 87492) and the conditional 87494 cannot be reached; they are 16,150 required XP, plus 5,650 conditional.
- U4 Classic memory says devilsaurs patrol and the stegodons are aggressive; the data says only rank elite and faction template 14. Danger lines are written from the data.
- U5 92020 Hol'anyee's Big Book of Big Lizards (L55, reqlevel blank, ends at npc 40833 "at the summit of Mount Hyjal") starts at Hol'anyee and is not in the pool; no tag.
- U6 Chapter 57's entry: 57-draft3 says "Hearth: Gadgetzan or Marshal's Refuge"; Marshal's Refuge has no innkeeper in the DB, so the hearth is Gadgetzan.

## 10. Deviations from the route plan
- **D1 3884 Williden's Journal is a drop-start quest of unknown rate.** Quest row [1] = item 11116 A Mangled Journal; item row [1] = 48 Un'Goro npc ids (6498-6519, 6527, 6551-6560, 6581-6585, 9162-9167, 9477, 9621, 9683, 9684, 10040, 10041), rows [2]/[3] empty (no object or container); no row in `data/drop_rates.json`; the nether tooltip carries no drop chance (multi-dropper). The plan's own method rates a quest that starts from a dropped item on that item ("How the decisions were made": the OOX beacons, the Ship Schedule: conditional) and `_decisions.tsv` has it PLAIN with no reason. Written here as "if the journal has dropped" at the two Williden stops and still counted, as the plan has it; if it goes conditional the chapter is 18 required, 73,230 XP (Tier B 23,500). Main session's call.
- **D2 Objectives inside elite ground.** 3882's Dinosaur Bone piles (object 161527, 20 points) each lie 0.4-3.0 units from an elite stegodon (npc row [5] = 1, 52-55, faction 14), and 3881's Research Equipment (161521) is 1.5 units from a Plated Stegodon. The plan's rule-13 check covered kill targets and droppers only (as in 46-draft2's D4, Gadgetzan Water Survey). Kept plain with danger lines; the bones also drop from non-elite Diemetradons at an unknown rate.
- **D3 Hearth.** The plan's Threads propose Gadgetzan for 56; 55-draft3 binds Talrendis Point, so chapter 56 flies Talrendis - Theramore - Gadgetzan and rebinds at Gadgetzan (no innkeeper in Un'Goro). Same end state as the plan.
- No change to the quest list; no prerequisite or place fault found inside the chapter (3845 after 3844; the pylons after 4284; 4321 after the three pylons; 4291 after 4290; 4491 after 4492; 3908 after 3845).
