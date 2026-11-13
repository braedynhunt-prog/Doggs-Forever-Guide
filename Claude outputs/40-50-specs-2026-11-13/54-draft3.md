# Spec 54 - Maraudon (required dungeon chapter; drafted 13 Nov 2026 against the plan's second revision)

Data used (13 Nov 2026): tooling/qdb (QuestieDB Forever 1.0.16: quest rows incl. [20] requiredSourceItems, [21] nextQuestInChain, [22] questFlags; npc rows [3]-[6]; object and item rows); data/zone_2100.json, zone_405.json, zone_15.json (Wowhead Forever XP / money / reqlevel / side, 12 Nov); data/drop_rates.json (17702, 17703, 17756, 17684, pulled 12 Nov); tooling/client/1.60.1.70938/TaxiNodes.csv, TaxiPath.csv; weights/tooltips/2026-11-12.json scored with score_items.parse/score/usable and profiles.enh_band_weights()[40] (central wdps 14, Str 2, AP 1, Int 1.69, Agi 1.12, Spi 2.5, SP 2; conservative Spi 1.5, SP 1); nether.wowhead.com/forever tooltips read 13 Nov from a shell into the scratch file tips54.json (quests 7067 7066 7070 7065 7041 7044 7046 7028; items 17758 17757 17761-17765 17781 17703 17702 17191 and the boss loot listed in section 5). guide/Guidelime_ForeverShaman/33_Desolace.lua for what round 1 did in Desolace. Wing membership, room order and portals are Classic knowledge, marked unverified: the DB places every Maraudon NPC at the instance marker (zone 2100, [-1,-1]).

## 1. Header
- File: `54_Maraudon.lua`
- `[N 46-47 Maraudon]` (required dungeon chapter, no `[O]`; chapter 53's `[NX]` must use this string)
- `[NX 46-48 Azshara]` (chapter 55's title as the plan has it)
- `[GA Alliance]`; shaman lines `[A Shaman]`. Footer group "Forever Shaman 30-60".
- Description: `[D Forever Shaman 30-60 (Braedyn)\\Maraudon in one run from Desolace: Nijel's Point pickups, the Centaur Pariah, the outer cave (Cavindra, the orange pool, the Khan spirits), the purple and orange wings, then the inner falls for Celebras and Princess Theradras; back by the Pariah to Nijel's Point, where chapter 55 flies on.]`
- Level on entry ~46.1 (plan XP table), exit ~46.5 on quest XP (plus the run's kill XP, not counted).
- **First line (level check)** `[OC]`: "This chapter wants level 48: the inner falls' bosses are elite level 49-51 (Celebras the Cursed 49, Landslide and Rotgrip 50, Princess Theradras 51). The pickups need at most 45 (Corruption of Earth and Seed 7065). The outer cave (40-43) and the two wings (42-48) suit a group at 46. Under 48: play the order below as it is (outer cave, purple, orange, inner falls last) and look for a group with members at 48+ for the inner falls; if the group cannot take the Princess, abandon Corruption of Earth and Seed and do not re-run (rule 2). Under 45 at Nijel's Point (not expected): Keeper Marandis will not give 7065; run the rest."

## 2. Entry state
- Where: Gadgetzan (chapter 53 ends there), **hearth Gadgetzan** (chapter 53's bind, per the prompt; the plan's hearth proposal is Gadgetzan for 53, 54 and 56). Not used in this chapter.
- Quests carried in, untouched here: 162 Rise of the Silithid and 3022 Handle With Care (to Darnassus, chapter 55), 3449 Arcane Runes (Azshara, 55). None of chapter 55's or 56's quests has a giver, objective or ender in Desolace or Maraudon (55's Nijel's Point start is only the flight).
- 7070 Shadowshard Fragments: if chapter 53 took it at Tervosh on its Theramore pass, skip leg 1's pickup.
- Gear on entry (from round 1 and the plan's table; chapters 49-53 are specced in parallel, so a better piece may already be worn): two-hander Bonebiter 583.5 or Bigger Rock on Bigger Stick 604.5 (94982, ch43 boss item); rings Purified Ring 30.3 + Coldwater Ring 27.6 (39d / 39c); neck Triune Amulet or Giantstone Medallion (25.0, round 1); chest Doomsayer's Robe 57.0 (39e) or the round-1 mail boss chest 66.7; waist Vinehedge Cinch 28.0 (ch50) or Twilight Initiate's Belt 29.8 (ch43); head Engineer's Guild Headpiece 75.0 (ch51 boss item) if it dropped.
- Training / professions: none here. No shaman trainer in Desolace (plan Threads: chapters 53-56 pass none); no profession gate falls in this chapter.

## 3. Travel and hearth
- **In:** at [TAR7823 Bera Stonehammer] 51.0,29.3 Tanaris fly to Theramore (TaxiPath 201, node 39 -> 32, cost 630c in the table); at [TAR4321 Baldruc] 67.5,51.3 Dustwallow Marsh fly to Nijel's Point (TaxiPath 163, 32 -> 37, 530c). There is no direct Gadgetzan - Nijel's Point path in build 70938; the game would route Gadgetzan - Nijel's Point through Theramore anyway, so the stop for Tervosh costs only the landing. All three points are known (`[P]` Nijel's Point in 33:16; Theramore from round 1; Gadgetzan from chapter 46).
- **Desolace roads are not in the data.** Round 1 (33_Desolace.lua) used a south road from Nijel's Point past Kormek's Hut (62.3,39.0) to the Kodo Graveyard and the caravan stops. Path in: Nijel's Point -> south past Kormek's Hut (Willow, 62.2,39.6) -> the Centaur Pariah (50.4,86.7; he patrols x44-51 y86-88) -> north-west to the Maraudon entrance. Keep east of Shadowprey Village (Horde): Shadowprey Guardians, level 55, stand at x24-26 y68-71.
- **Entrance:** the DB has object 178400 "Maraudon Portal" at 29.2,61.2 Desolace and puts the outer cave's mobs, Cavindra (31.9,63.8), the Orange Crystal Pool (object 178907, 33.2,65.7) and the Khan spirits in the Desolace zone, i.e. outside the instance. The Maraudine centaur camp (38-40, not elite; ch33) surrounds the approach; Khan Hratha (42 elite) and his guards stand at 29.6,52.0, north of the cave - stay clear. Which opening is the purple and which the orange wing is Classic knowledge (unverified); the plan's prompt calls the area the Valley of Spears, while chapter 33 uses that name for x58-65 y82-92: name unverified, coordinates from the DB.
- **Out:** walk out of the instance, ride to the Pariah (hand-in), then north on the road past Willow (optional hand-in) to Nijel's Point for the last two hand-ins. Chapter 55 starts at [TAR6706 Baritanas Skyriver] 64.7,10.5 Desolace.
- **Bind:** no change; Gadgetzan stays (Unsure: the Nijel's Point alternative).
- **Scepter of Celebras** (17191, 7046's fixed reward), tooltip: "Use: Creates a portal, teleporting group members that use it to Earth Song Falls in inner Maraudon. (30 Sec Cooldown)". It is the shortcut for a later visit; this chapter's single run does not need it. Where it can be used is unverified.

## 4. Route

### Leg 1 - Theramore stop (only for the optional 7070)
1. `[O]` At [TAR4967 Archmage Tervosh] 66.4,49.3 Dustwallow Marsh: `[QA7070 Shadowshard Fragments]` (3,450 XP, req 39, quest L42; Stormwind rep 150; shareable, questFlags 8). Label **grind / luck**. Objective (Wowhead tooltip): 10 Shadowshard Fragments (17756) from Maraudon. Skip if chapter 53 took it.
2. At [TAR4321 Baldruc] 67.5,51.3 Dustwallow Marsh: fly Nijel's Point.

### Leg 2 - Nijel's Point pickups (every giver within 6 units of the flight master)
3. At [TAR11715 Talendria] 68.5,8.9 Desolace: `[QA7041 Vyletongue Corruption]` (5,250 XP, req 41, L47; Wowhead side 1). She gives the Coated Cerulean Vial (17693, quest row [10]). Objective: fill it at the orange crystal pool, use the Filled Cerulean Vial (17696) on the Vylestem Vines to make a Noxxious Scion (13696, L45-46, not elite, instance) emerge, kill it: "Heal 8 plants" (quest text; QuestieDB count field 0). Label **normal**. Not shareable in the data (questFlags empty). Note: the DB also puts a Vylestem Vine (object 178908) at 68.45,8.78 beside Talendria and one at 23.1,70.3; the vines the quest needs are inside (Classic: purple wing, unverified).
4. At [TAR13698 Keeper Marandis] 63.8,10.7 Desolace: `[QA7065 Corruption of Earth and Seed]` (6,100 XP, **req 45**, L51; Cenarion Circle 150; shareable). Objective: kill Princess Theradras (12201, L51 elite). Label **normal**.

### Leg 3 - the road south
5. `[O]` At [TAR13656 Willow] 62.2,39.6 Desolace (beside Kormek's Hut): `[QA7028 Twisted Evils]` (5,250 XP, req 41, L47; shareable). Label **grind / luck**: Theradric Crystal Carvings (17684), **25 on Wowhead Forever's tooltip** (QuestieDB's text says 15), 26.6% over all droppers in drop_rates.json; best per-mob rows Vile Larva 52% (296/568), Constrictor Vine 44%, Sister of Celebrian 41%, Barbed Lasher 40%, Putridus Satyr 34%, Celebrian Dryad 34%. Budget ~94 kills at the overall rate: never farmed; whatever the run's trash gives.
6. At [TAR13717 Centaur Pariah] 50.4,86.7 Desolace (patrols x44-51 y86-88; L42, not elite): `[QA7067 The Pariah's Instructions]` (5,450 XP + 1g 40s at hand-in, req 39, L48; not shareable in the data). He gives The Pariah's Instructions (17781, "Right Click to Read"). Objective (Wowhead tooltip): Amulet of Union (17758) **and** Amulet of Spirits (17757). Quest row [20] requiredSourceItems = 17757, 17761, 17762, 17763, 17764, 17765: the Amulet of Spirits plus the five Khans' gems; each gem's Use: "Places all five of the Khans' gems in the Amulet of Spirits" (this makes the Amulet of Union; Classic mechanic, the in-game result unverified). Label **normal**.
7. Ride north-west to the Maraudon entrance, east of Shadowprey Village [G29.2,61.2 Desolace].

### Leg 4 - the outer cave (Desolace zone, elite, not instanced: form the group here)
- `[OC]` labels block (chapter-26 / 39e style), one line per quest: 7067 normal; 7041 normal; 7044 normal (boss items, one kill each); 7046 normal; 7065 normal; 7070 grind / luck; 7028 grind / luck; Seed of Life 7066 picked up after the Princess and carried to round 3.
- `[OC]` mobs (DB, all elite, rank row [5] = 1): north / purple side (x27-30 y53-58) Shadowshard Rumbler 40-41 (8 spawns), Shadowshard Smasher 41-42 (7), Rock Borer 40-41 (10), Rock Worm 41-42 (10); south / orange side (x30-37 y59-68) Ambereye Basilisk 40-41 (14), Ambereye Reaver 41-42 (8), Ambershard Crusher 40-41 (2), Ambershard Destroyer 42-43 (2); Cursed Centaur 43 rare elite (30.4,60.2); Maraudine Priest 40-42 and Ghostly Raider / Marauder 40-42 near 28,63 (not elite). Side names are Classic (unverified).
8. At [TAR13697 Cavindra] 31.9,63.8 Desolace (L45 elite, friendly): `[QA7044 Legends of Maraudon]` (3,400 XP, req 41, L49; shareable; nextQuestInChain 7046). Objective: Celebrian Rod (17702) and Celebrian Diamond (17703), then speak with Celebras. Ends at Celebras the Redeemed (13716) inside.
9. Fill the Coated Cerulean Vial at the Maraudon Orange Crystal Pool (object 178907) [CI17696,1 Filled Cerulean Vial] [G33.2,65.7 Desolace]. (Held with [CI]: 7041's objectives are the Scion kills, not the vial.)
10. Kill [TAR13718 The Nameless Prophet] (L41 elite; DB spawns 28.2,62.4 / 27.2,63.1 / 28.8,62.4 / 28.2,64.2) for the Amulet of Spirits [CI17757,1] [G28.2,62.4 Desolace]. Tooltip: "Dropped by: The Nameless Prophet, Drop Chance: 60.87%" - a single named mob at 60%+, plain (rule 12). If it does not drop: one more pull after his respawn is not budgeted; abandon 7067 `[QS7067]` (the gems need the amulet).
11. Kill [TAR12240 Spirit of Kolk] (L43 elite, 29.7,60.5) for the Gem of the First Khan [CI17761,1]; [TAR12239 Spirit of Gelk] (L42 elite, 29.4,56.9) for the Gem of the Second Khan [CI17762,1]; [TAR12241 Spirit of Magra] (L43 elite, 35.8,60.4) for the Gem of the Third Khan [CI17763,1]. Three separate lines, each with its own [G]. Each gem has one dropper (item row [1]); no rate in the data (Wowhead tooltip shows none): normal, one kill each. The Amulet of Spirits' Use ("Forces the spirits of the first centaur Kahns to manifest in the physical world") suggests it must be used to make the spirits appear (Classic; unverified); the DB also holds living Kolk 13742, Gelk 13741 and Magra 13740 (L42-43 elite) at the same spots - the gems drop from the Spirit ids.
12. `[O]` Kill [TAR11777 Shadowshard Rumbler] and [TAR11778 Shadowshard Smasher] for 10 Shadowshard Fragments `[QC7070]` [G27.8,55.6 Desolace] (drop quest, 45.9% over both: Rumbler 85/185, Smasher 82/179 - budget ~22 kills on 15 spawns; only the ones on the way to Gelk, no farm). Under 10 at the portal: `[QS7070]` there.

### Leg 5 - the instance, one run (rule 2). No [G] inside; dungeon lines keep the outdoor pin [G29.2,61.2 Desolace] if the writer needs one.
Wing order: purple (bosses 47-48) then orange (48), inner falls last (49-51). Wings and their bosses are Classic knowledge; the levels are the DB's.
13. Purple wing: kill the Vylestem Vines' Noxxious Scions: use the [UI17696 Filled Cerulean Vial] on 8 Vylestem Vines and kill each [TAR13696 Noxxious Scion] `[QC7041]`.
14. Kill [TAR12243 Spirit of Veng] (L47 elite) for the Gem of the Fifth Khan [CI17765,1].
15. Kill [TAR12236 Lord Vyletongue] (L47 elite) for the Celebrian Diamond [CI17703,1]. **normal, boss item: one kill only; Wowhead reads 37.9% over all kills (tooltip 41.76%)**; no diamond: 7044 and 7046 are lost, `[QS7044]` at the end of the run.
16. `[OC]` Meshlok the Harvester (L48, rank 2 = rare elite) may stand in the wing: not a quest target; Bloomsprout Headpiece (section 5).
17. Orange wing: kill [TAR12242 Spirit of Maraudos] (L46 elite) for the Gem of the Fourth Khan [CI17764,1].
18. Kill [TAR13282 Noxxion] (L48 elite) for the Celebrian Rod [CI17702,1]. **normal, boss item: one kill only; Wowhead 42.6% (Noxxion 60/141; tooltip 45.45%)**; no rod: as step 15.
19. `[OC]` Razorlash (L48 elite) is not a quest target (Classic: on the orange path; drops in section 5).
20. Use a Khan's gem to make the Amulet of Union `[QC7067]` (any gem's Use; once all five gems and the Amulet of Spirits are in the bags).
21. Inner falls: kill [TAR12225 Celebras the Cursed] (L49 elite). [TAR13716 Celebras the Redeemed] (L49) then stands there (Classic; DB instance marker): `[QT7044]` `[QA7046 The Scepter of Celebras]` (5,700 XP, req 41; preQuestSingle [7044]; questFlags 2, not shareable). Objective: "Create the Scepter of Celebras" - assist him during the ritual (object 178965 Incantation of Celebras), speak with him when it is done `[QC7046]`; `[QT7046]` - Scepter of Celebras (fixed).
22. `[OC]` On the way: Landslide (L50 elite; Classic: on the path to the Princess), Tinkerer Gizlock (L50 elite, Classic placement disputed, not needed), **Rotgrip (L50 elite): kill him if the group agrees - Gatorbite Axe (section 5)**.
23. Kill [TAR12201 Princess Theradras] (L51 elite) `[QC7065]`. If the group cannot kill her: `[QS7065]`, skip step 24; no re-run.
24. [TAR12238 Zaetar's Spirit] (L60 elite, friendly; appears after the Princess in Classic): `[QA7066 Seed of Life]` (6,100 XP + 1g 50s at Keeper Remulos in Moonglade; required level 45 in QuestieDB, 39 on Wowhead; source item Seed of Life 17760). **Carried to round 3**, never handed in this round. Not counted.
25. `[O]` If 7028 is not at 25 carvings: `[QS7028]` here (or keep it to hand in at Willow on the way out only if it is complete).

### Leg 6 - out and home
26. Out of the instance; ride to [TAR13717 Centaur Pariah] [G50.4,86.7 Desolace]: `[QT7067]` (1g 40s) - Mark of the Chosen (fixed, trinket).
27. North on the road; `[O]` at [TAR13656 Willow] [G62.2,39.6 Desolace]: `[QT7028]` if 25 carvings (gear, section 5).
28. At [TAR11715 Talendria] [G68.5,8.9 Desolace]: `[QT7041]` (gear, section 5).
29. At [TAR13698 Keeper Marandis] [G63.8,10.7 Desolace]: `[QT7065]` (gear, section 5).
30. `[OC]` Check line (section 7). Chapter 55 starts at Baritanas Skyriver (fly Auberdine).

## 5. Gear calls (band 40, mail wearable; central | conservative)
- **7041 Vyletongue Corruption** (choice): **Woodseed Hoop** (ring +10 Int +6 SP) 28.9 | 22.9 over Sagebrush Girdle (leather waist +11 Agi +9 Int) 27.5 | 27.5; Branchclaw Gauntlets are plate (unusable). The Hoop replaces the Coldwater Ring 27.6 | 18.6 (39c), +1.3. Take the Girdle instead only if his belt scores under 27.5 (not with Vinehedge Cinch 28.0 or Twilight Initiate's Belt 29.8).
- **7065 Corruption of Earth and Seed** (choice): Resurgence Rod (2H staff 34.1 dps +37 SP) 551.1 | 514.1 - below Bonebiter 583.5 and Bigger Rock on Bigger Stick 604.5, above Rage of the Storm 529.8. Thrash Blade (sword) and Verdant Keeper's Aim (bow) are unusable. Take the Rod: wield it only if Rage of the Storm is still the weapon, else vendor (4g 21s 42c, the best sell; Thrash Blade 3g 37s 14c).
- 7067: Mark of the Chosen (trinket, proc only) - fixed; not scored (trinkets score 0 in the model).
- 7046: Scepter of Celebras - fixed, the portal key.
- `[O]` 7070: Prodigious Shadowshard Pendant (+9 SP) 18.0 | 9.0 over Zealous Shadowshard Pendant (+14 AP) 14.0 | 14.0; both below his neck (Triune / Giantstone 25.0): **no upgrade**; take the Zealous for the conservative tie-break or vendor either (60s 1c each).
- `[O]` 7028: Acumen Robes (cloth chest +15 Int +14 SP) 53.3 | 39.3 over Relentless Chain (mail chest +11 Sta +11 Int +20 AP) 38.6; Sprightring Helm 12.3; Hulkstone Pauldrons plate. Below Doomsayer's Robe 57.0 (39e): **no upgrade**; vendor value Relentless Chain 1g 31s 4c (best sell).
- Boss loot, roll calls (`[OC]`, live tooltip drop chances, 13 Nov; none is in weights/tooltips/2026-11-12.json):
  - **Gatorbite Axe** (Rotgrip; 2H axe 45.8 dps, bleed proc not scored, **req 48**, 28.89%) **640.9** - beats Bonebiter 583.5 by 57 and Bigger Rock 604.5 by 36: ROLL, carry it, wear it at 48.
  - **Soothsayer's Headdress** (Celebras the Cursed; leather head +7 Sta +15 Int +8 Spi +23 SP, req 47, 32.2%) 91.3 | 60.3 - beats Engineer's Guild Headpiece 75.0: roll, wear at 47.
  - Infernal Trickster Leggings (Vyletongue; mail legs +20 Agi +8 Int +10 Spi, req 45, 28.2%) 60.9 | 50.9 - roll only if his legs score under ~60 (the plan's Treetop Leggings 58.5 come later, ch56).
  - Brusslehide Leggings (Razorlash; leather legs +12 Sta +7 Int +23 SP, req 46, 22.7%) 57.8 | 34.8; Vinerot Sandals (Razorlash; cloth feet +9 Int +10 Spi +6 SP, req 46, 24.9%) 52.2 | 36.2 - beats Southsea Mojo Boots 34.6: roll.
  - Rotgrip Mantle (cloth shoulder +18 Int +13 SP, req 48, 30.0%) 56.4 | 43.4 - beats Failed Flying Experiment 31.2: roll, wear at 48.
  - Eye of Theradras (Princess; cloth head +10 Sta +19 Int +10 Spi, crit not scored, req 49, 22.1%) 57.1 - below the Headdress; Bracers of the Stone Princess (mail wrist +6 Sta +5 Int +28 AP, req 49, 48.8%) 36.5 - beats Reloading Assist Armbands 23.7 / Chelonian Cuffs 16.9: roll, wear at 49; Rockgrip Gauntlets (Landslide; mail hands +10 Sta +11 Int +28 AP, req 48, 23.7%) 46.6 - below Witherseed Gloves 48.5 (ch53).
  - Satyrmane Sash (Vyletongue; cloth waist +7 Sta +10 Int +14 SP, req 45, 19.4%) 44.9 | 30.9 - beats his belt (28-30): roll. Bloomsprout Headpiece (Meshlok; mail head +15 Sta +36 AP, 32.3%) 36.0 - below the head he has.
  - Nothing else scores for him (plate, wands, swords, guns, off-hands; Blackstone Ring 20.0 and Gemshard Heart 25.2 are at or below his ring / neck).

## 6. Out
- 93404 Rot and Regret (5,700) - giver Woodwyrd (254674) stands in Shen'dralas, which is out (11 Nov ruling). (`_decisions` / plan "Out" list.)
- Desolace (plan "Out, by zone"): 1380 / 1381 / 96222 Khan Hratha (rule 13, 42 elite); 93196 Khan Jehn (judgment, leftover at 42); 1459 > 1466 > 1467 Reagents for Reclaimers Inc. (chain); 92743 A Conqueror's Crown (judgment); 1456 / 1457 The Karnitol Shipwreck (Karnitol's Satchel 6.8%); 93224 Carved Centaur Totems (25.0%); 93678 Abridged Notes on Draenethyst (judgment, cross-continent delivery); 93226 / 93227 Buying Friendship (judgment, 390 XP rep hand-ins); 6141 Brother Anton (judgment, 300 XP). All silent (rule 4).
- 7066 Seed of Life: picked up, carried to round 3 (Moonglade, zone 493).

## 7. End check
- Handed in here: 7067, 7041, 7044, 7046, 7065 (7065 abandoned only if the Princess could not be killed); optional 7028 handed in or abandoned in the run; 7070 carried to chapter 57 with 10 fragments, or abandoned at the portal.
- Carried out: 7066 Seed of Life (round 3, Moonglade); `[O]` 7070 Shadowshard Fragments to Theramore (chapter 57: Archmage Tervosh 66.4,49.3 Dustwallow Marsh, on the walk to the Menethil boat); 162, 3022 (Darnassus, ch55), 3449 (Azshara, ch55) untouched.
- Where: Nijel's Point; hearth Gadgetzan.

## 8. Totals
- Required (5): 7067 5,450 + 1g 40s; 7041 5,250; 7044 3,400; 7046 5,700; 7065 6,100 = **25,900 XP, 1g 40s** - equals the plan's row.
- Optional (grind / luck, not counted): 7070 3,450; 7028 5,250 = **8,700 XP** - equals the plan's row.
- Not counted: 7066 Seed of Life 6,100 + 1g 50s (round 3).

## 9. Unverified / in-game test list; Needs pull; Unsure
Test list:
- Wing membership and order (purple: Vyletongue, Meshlok, Veng; orange: Noxxion, Razorlash, Maraudos; inner: Celebras, Landslide, Gizlock, Rotgrip, Princess) and where the wing portals are; the DB gives only object 178400 at 29.2,61.2.
- Where the Vylestem Vines are; whether the Khan spirits need the Amulet of Spirits used to appear; how the gems combine into the Amulet of Union.
- Whether the Khan gems drop 100% with the quest (no rate in the data).
- Celebras the Redeemed appearing after Celebras the Cursed; where the Scepter portal can be used.
- Zaetar's Spirit after the Princess; Seed of Life's required level (QuestieDB 45, Wowhead 39).
- Twisted Evils count: 25 (Wowhead Forever) or 15 (QuestieDB text).
- Desolace road Kormek's Hut - the Pariah - the Maraudon entrance; Shadowprey guards' reach.
- Shareability: questFlags 8 on 7044, 7065, 7070, 7028; none on 7067, 7041, 7046.
Needs pull: none required. Optional: drop rates of Gems 17761-17765 (Wowhead item pages), the Wowhead Forever quest page of 7066 for its required level.
Unsure:
- **Wing decision.** Recommended (a), one full run here. Quests per part: outer cave + purple + orange complete 7067 and 7041 (10,700 XP) and the 7044 items; the inner falls hold 7044's hand-in, 7046 and 7065 (15,200 XP) and Seed of Life. Option (b) outer wings here, inner falls at the start of chapter 55 (the last Nijel's Point pass): the only XP gained in between is 7067 + 7041 (10,700, under 0.1 level at 46), and the second visit re-enters without the Scepter (it is 7046's reward, in the inner part), so a wing is walked twice plus the ride Nijel's Point - entrance - back (~10 min, estimate). Option (c) the whole dungeon at the start of 55: same level as (a), and the chapter 55 / 54 boundary moves with nothing gained. The only option that buys levels would be leaving the inner falls for round 3, which drops 15,200 required XP from round 2 - not offered by the plan, not proposed.
- Hearth: alternative is to bind at [TAR11103 Innkeeper Lyshaerya] 66.3,6.5 on arrival and hearth from the Pariah to Nijel's Point (saves the ~80-unit ride north, a few minutes, estimate) at the cost of the Willow hand-in and leaving the hearth at Nijel's Point for chapter 55; chapter 55's spec decides its own bind.
- Both optional quests fail rule 11's test (no scored upgrade: pendants 18.0 / 14.0 vs neck 25.0, Acumen Robes 53.3 vs Doomsayer's Robe 57.0); they are kept as the plan's dungeon grind / luck lines. The main session may cut them.
- 7070's pickup and hand-in are in Theramore: picked up in leg 1 (or chapter 53), handed in in chapter 57 only if 57's spec adds `[QT7070]`.
- Gear on entry for chapters 49-53 is assumed from the plan's table; the parallel specs may change the comparisons.

## 10. Deviations from the route plan
- No quest list change. Gear-table differences: Acumen Robes (7028) is not an upgrade against Doomsayer's Robe 57.0; Resurgence Rod (7065) is not an upgrade against Bonebiter / Bigger Rock.
- 7028 Twisted Evils needs **25** carvings on Wowhead Forever's quest tooltip (plan used QuestieDB's 15): budget ~94 kills at 26.6%. Still grind / luck, not counted.
- 7070 Shadowshard Fragments: the plan places it in chapter 54; its giver and ender are Archmage Tervosh in Theramore. The route reaches the ender in chapter 57 (Marshal's Refuge - Gadgetzan - Theramore - Menethil boat), so it is carried there; the fragments drop only from Shadowshard Rumbler / Smasher in the outer cave (Desolace zone, elite 40-42), not inside the instance.
- 7067 needs the Amulet of Spirits (Nameless Prophet, 60.87%) and five gems (three outer-cave spirits, Maraudos and Veng inside); the plan's pool line said "Amulet of Union <- no source in qdb". Plain by rule 12 (single named mob at 60%+).
- Celebrian Diamond / Rod: tooltip rates 41.76% / 45.45% next to the plan's 37.9% / 42.6% (drop_rates.json kept as the label number).
- 7066 Seed of Life: QuestieDB required level 45 (plan pool said 39, Wowhead's figure); carried as planned.
- Route: Gadgetzan - Theramore - Nijel's Point with a landing in Theramore (only for 7070).
