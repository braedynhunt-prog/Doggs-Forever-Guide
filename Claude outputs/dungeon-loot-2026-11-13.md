# Dungeon loot check - 2026-11-13

Report only (tooling/dungeon_loot.py). Gear a Dwarf 2H Enhancement shaman can use at 1-30 that QuestieDB lists as dropping from creatures inside each dungeon (zone spawns, the chapter's [TAR] ids and a hand list of spawnless bosses), scored with weights/score_items.py (AP-equivalent; central and conservative weight sets, band nearest the chapter's starting level; no mace term). "Beats guide gear" compares the central score with the best item in the same slot that the guide calls out in green on a Shaman/Dwarf line in this chapter or any earlier one. 1H weapons are the shield set (secondary) and compare only with each other. Drops more than 5 levels above the chapter's top level are left out. "Mentioned" = the full name, or the first word followed by "(" (the helm lines' short form), appears in the chapter. Mail, plate, shields, swords, polearms, ranged and cloth other than cloaks are left out.

## 03_HallOfThanes - 15-16 Hall of Thanes (levels 15-16)

- Dungeon zone id 16919; creatures: 19 (5 spawned in the zone, 14 from the chapter's [TAR] ids and the hand list); usable gear drops: 7 (0 not mentioned in the chapter; 0 more hidden as req > 21); weights: level-15 band

### Not mentioned in this chapter

(none)

### Mentioned in this chapter

- Golemheart Stave (270228, staff, req 13, Plunder) - 202.3 / 184.3; beats guide gear: no (vs Ironforge Greathammer 223.6); drop chance: 34.76%
- Durgen's Crescent Axe (270256, 1H axe (shield set), req 13, Durgen Dirgehammer) - 180.1 / 180.1; beats guide gear: no baseline; drop chance: 28.77%
- Fang of Magmatus (271095, dagger (shield set), req 13, Magmatus) - 151.7 / 133.7; beats guide gear: no baseline; drop chance: 35.76%
- Flamefist Grips (270231, hands leather, req 13, Magmatus) - 15.2 / 10.2; beats guide gear: no baseline; drop chance: 32.74%
- Ephemeral Choker (270227, neck, req 13, Faldrim Anvilmar) - 12.5 / 7.5; beats guide gear: no baseline; drop chance: 33.35%
- Spiritwraith Drape (271097, back cloth, req 13, Faldrim Anvilmar) - 11.7 / 7.7; beats guide gear: no baseline; drop chance: 34.01%
- Direhammer Leggings (270260, legs leather, req 13, Durgen Dirgehammer) - 2.2 / 2.2; beats guide gear: no baseline; drop chance: 26.83%

## 07_Deadmines - 19-20 Deadmines (levels 19-20)

- Dungeon zone id 1581; creatures: 63 (27 spawned in the zone, 36 from the chapter's [TAR] ids and the hand list); usable gear drops: 28 (12 not mentioned in the chapter; 0 more hidden as req > 25); weights: level-20 band

### Not mentioned in this chapter

| item | id | slot/type | req | dropper(s) | central | conservative | beats guide gear | drop chance |
|---|---|---|---|---|---|---|---|---|
| Goblin Hammer | 273297 | 1H mace (shield set) | 18 | Gilnid | 213.5 | 213.5 | no baseline | 30.77% |
| Goblin Screwdriver | 1936 | dagger (shield set) | 13 | Goblin Engineer | 173.2 | 173.2 | no baseline | 2.61% |
| Blackened Defias Gloves | 10401 | hands leather | 14 | Defias Overseer, Defias Taskmaster | 12.0 | 12.0 | no baseline | unknown |
| Woodworking Gloves | 1945 | hands leather | 13 | Goblin Woodcarver | 8.4 | 6.4 | no baseline | 9.18% |
| First Mate Band | 284715 | finger | 17 | Mr. Smite | 8.0 | 8.0 | no baseline | 23.36% |
| Metalworking Gloves | 1944 | hands leather | 13 | Goblin Craftsman | 6.0 | 6.0 | no baseline | 8.30% |
| Blackened Defias Boots | 10402 | feet leather | 15 | Defias Strip Miner | 4.8 | 4.8 | no baseline | 4.19% |
| Lookie's Spyglass | 273298 | trinket | 18 | Cookie | 2.5 | 1.5 | no baseline | 29.39% |
| Red Defias Mask | 7997 | head leather | ? | Defias Blackguard, Defias Evoker, Defias Highwayman, Defias Knuckleduster +10 more | 0.0 | 0.0 | no baseline | unknown |
| Scouting Belt | 6581 | waist leather | 16 | Miner Johnson | 0.0 | 0.0 | no (vs Blackened Defias Belt 18.0) | unknown |
| Stonemason Cloak | 1930 | back cloth | 13 | Defias Miner | 0.0 | 0.0 | no baseline | 3.37% |
| Viridian Band | 11982 | finger | 18 | Cookie | 0.0 | 0.0 | no baseline | unknown |

### Mentioned in this chapter

- Smite's Mighty Hammer (7230, 2H mace, req 18, Mr. Smite) - 301.1 / 301.1; beats guide gear: yes (vs Rockslicer 289.8); drop chance: 24.15%
- Rockslicer (872, 2H axe, req 18, Rhahk'Zor) - 289.8 / 289.8; beats guide gear: no (vs Smite's Mighty Hammer 301.1); drop chance: 32.57%
- Rhahk'Zor's Hammer (5187, 2H mace, req 16, Rhahk'Zor) - 274.2 / 266.2; beats guide gear: no (vs Smite's Mighty Hammer 301.1); drop chance: 31.89%
- Taskmaster Axe (5194, 2H axe, req 18, Sneed) - 254.8 / 231.8; beats guide gear: no (vs Smite's Mighty Hammer 301.1); drop chance: 30.57%
- Emberstone Staff (5201, staff, req 17, Captain Greenskin) - 246.4 / 222.4; beats guide gear: no (vs Smite's Mighty Hammer 301.1); drop chance: 30.59%
- Smite's Reaver (5196, 1H axe (shield set), req 17, Mr. Smite) - 208.8 / 205.8; beats guide gear: no baseline; drop chance: 23.85%
- Cookie's Tenderizer (5197, 1H mace (shield set), req 16, Cookie) - 205.0 / 201.0; beats guide gear: no baseline; drop chance: 31.19%
- Buzzer Blade (2169, dagger (shield set), req 16, Sneed's Shredder) - 170.0 / 148.0; beats guide gear: no baseline; drop chance: 29.83%
- Stonemason Trousers (1934, legs leather, req 15, Defias Blackguard) - 23.1 / 16.1; beats guide gear: yes (vs Smith's Trousers 11.2); drop chance: 2.47%
- Blackened Defias Belt (10403, waist leather, req 17, Captain Greenskin) - 18.0 / 18.0; beats guide gear: no baseline; drop chance: 31.27%
- Blackened Defias Leggings (10400, legs leather, req 14, Defias Overseer, Defias Taskmaster) - 16.8 / 16.8; beats guide gear: yes (vs Smith's Trousers 11.2); drop chance: unknown
- Smelting Pants (5199, legs leather, req 16, Gilnid) - 12.5 / 7.5; beats guide gear: yes (vs Smith's Trousers 11.2); drop chance: 33.33%
- Blackened Defias Armor (10399, chest leather, req 17, Edwin VanCleef) - 10.4 / 10.4; beats guide gear: no baseline; drop chance: 20.71%
- Miner's Cape (5444, back cloth, req 17, Miner Johnson) - 10.0 / 10.0; beats guide gear: no baseline; drop chance: 52.76%
- Lavishly Jeweled Ring (1156, finger, req 17, Gilnid) - 8.5 / 8.5; beats guide gear: no baseline; drop chance: 31.70%
- Cape of the Brotherhood (5193, back cloth, req 19, Edwin VanCleef) - 4.0 / 4.0; beats guide gear: no baseline; drop chance: 18.90%

## 08_RuinsOfLordaeron - 20-21 Ruins of Lordaeron (levels 20-21)

- Dungeon zone id 16611; creatures: 33 (14 spawned in the zone, 19 from the chapter's [TAR] ids and the hand list); usable gear drops: 7 (2 not mentioned in the chapter; 0 more hidden as req > 26); weights: level-20 band

### Not mentioned in this chapter

| item | id | slot/type | req | dropper(s) | central | conservative | beats guide gear | drop chance |
|---|---|---|---|---|---|---|---|---|
| Coldspire Staff | 271215 | staff | 19 | Rath'mael | 212.0 | 212.0 | no (vs Smite's Mighty Hammer 301.1) | 32.90% |
| Scepter of the Abandoned | 271216 | 1H mace (shield set) | 17 | The Abandoned | 182.7 | 158.7 | no baseline | 34.61% |

### Mentioned in this chapter

- Segmented Spider Leg (271203, staff, req 15, Witherfang) - 264.7 / 259.7; beats guide gear: no (vs Smite's Mighty Hammer 301.1); drop chance: 31.87%
- Corpse Chopper (271217, 2H axe, req 16, Bjork) - 254.7 / 254.7; beats guide gear: no (vs Smite's Mighty Hammer 301.1); drop chance: 35.69%
- Meathook Slicer (271204, dagger (shield set), req 15, The Baron) - 190.5 / 190.5; beats guide gear: no baseline; drop chance: 31.20%
- Bloodied Chestwraps (271212, chest leather, req 17, Viktor the Vile) - 28.1 / 19.1; beats guide gear: yes (vs Blackened Defias Armor 10.4); drop chance: 33.05%
- Witherbite Bracers (271202, wrist leather, req 15, Witherfang) - 13.2 / 8.2; beats guide gear: yes (vs Bravo's Armbands 8.4); drop chance: 32.15%

## 13_Blackfathom - 25-26 Blackfathom Deeps (levels 25-26)

- Dungeon zone id 719; creatures: 31 (31 spawned in the zone, 0 from the chapter's [TAR] ids and the hand list); usable gear drops: 26 (9 not mentioned in the chapter; 0 more hidden as req > 31); weights: level-25 band

### Not mentioned in this chapter

| item | id | slot/type | req | dropper(s) | central | conservative | beats guide gear | drop chance |
|---|---|---|---|---|---|---|---|---|
| Axe of the Enforcer | 1454 | 1H axe (shield set) | 24 | Aku'mai Snapjaw, Barbed Crustacean, Baron Aquanis, Blackfathom Sea Witch +12 more | 265.8 | 265.8 | no baseline | unknown |
| Doomspike | 3413 | dagger (shield set) | 22 | Aku'mai Fisher, Aku'mai Snapjaw, Barbed Crustacean, Blackfathom Myrmidon +17 more | 248.6 | 248.6 | no baseline | unknown |
| Grimclaw | 1481 | 1H axe (shield set) | 22 | Aku'mai Snapjaw, Barbed Crustacean, Baron Aquanis, Blackfathom Myrmidon +15 more | 241.5 | 241.5 | no baseline | unknown |
| Crested Scepter | 3414 | 1H mace (shield set) | 24 | Aku'mai Snapjaw, Barbed Crustacean, Baron Aquanis, Blackfathom Sea Witch +11 more | 236.0 | 204.0 | no baseline | unknown |
| Evocator's Blade | 2567 | dagger (shield set) | 20 | Aku'mai Fisher, Aku'mai Snapjaw, Barbed Crustacean, Blackfathom Myrmidon +16 more | 224.0 | 191.0 | no baseline | unknown |
| Threshadon Fang | 5516 | dagger (shield set) | 11 | Deep Pool Threshfin, Old Serra'kis | 70.0 | 70.0 | no baseline | unknown |
| Wisdom's Leather Helm | 252515 | head leather | 25 | Twilight Lord Kelris | 14.0 | 7.0 | no (vs Defender's Leather Helm 24.0) | unknown |
| Cuirboulli Boots | 2143 | feet leather | 22 | Barbed Crustacean, Blackfathom Myrmidon, Blackfathom Sea Witch, Blindlight Murloc +2 more | 0.0 | 0.0 | no (vs Kimbra Boots 12.2) | unknown |
| Tough Leather Pants | 1808 | legs leather | 25 | Twilight Shadowmage | 0.0 | 0.0 | no (vs Smith's Trousers 11.1) | unknown |

### Mentioned in this chapter

- Reef Axe (6905, 2H axe, req 22, Gelihast) - 345.9 / 337.9; beats guide gear: yes (vs Twilight Maul 344.3); drop chance: 32.40%
- Twilight Maul (273841, 2H mace, req 23, Lorgus Jett) - 344.3 / 332.3; beats guide gear: no (vs Reef Axe 345.9); drop chance: 33.75%
- Rod of the Sleepwalker (1155, staff, req 24, Twilight Lord Kelris) - 339.0 / 296.0; beats guide gear: no (vs Reef Axe 345.9); drop chance: 11.94%
- Staff of the Blessed Seer (2271, staff, req 20, Aku'mai Fisher, Aku'mai Snapjaw, Barbed Crustacean, Baron Aquanis +17 more) - 300.4 / 262.4; beats guide gear: no (vs Reef Axe 345.9); drop chance: unknown
- Staff of the Friar (3415, staff, req 21, Aku'mai Fisher, Aku'mai Snapjaw, Barbed Crustacean, Blackfathom Myrmidon +17 more) - 290.9 / 261.9; beats guide gear: no (vs Reef Axe 345.9); drop chance: unknown
- Bite of Serra'kis (6904, dagger (shield set), req 23, Old Serra'kis) - 247.7 / 247.7; beats guide gear: no baseline; drop chance: 31.71%
- Glowing Thresher Cape (6901, back cloth, req 24, Old Serra'kis) - 26.0 / 15.0; beats guide gear: yes (vs Grave Shroud 6.0); drop chance: 30.81%
- Stormrider's Leather Helm (252514, head leather, req 25, Aku'mai) - 25.0 / 15.0; beats guide gear: yes (vs Defender's Leather Helm 24.0); drop chance: unknown
- Defender's Leather Helm (252455, head leather, req 25, Aku'mai, Gelihast, Lorgus Jett, Old Serra'kis +1 more) - 24.0 / 24.0; beats guide gear: yes (vs Recipe: Mithril Head Trout 0.0); drop chance: unknown
- Moss Cinch (6911, waist leather, req 25, Aku'mai) - 24.0 / 12.0; beats guide gear: yes (vs Blackened Defias Belt 18.0); drop chance: 28.92%
- Totemic Leather Helm (252456, head leather, req 25, Aku'mai, Baron Aquanis, Gelihast, Lorgus Jett +2 more) - 24.0 / 12.0; beats guide gear: no (vs Defender's Leather Helm 24.0); drop chance: unknown
- Naga Battle Gloves (888, hands leather, req 22, Lady Sarevess) - 18.0 / 13.0; beats guide gear: no baseline; drop chance: 34.24%
- Ring of Precision (1491, finger, req 22, Aku'mai Fisher, Aku'mai Snapjaw, Barbed Crustacean, Baron Aquanis +16 more) - 12.2 / 9.2; beats guide gear: no baseline; drop chance: unknown
- Bands of Serra'kis (6902, wrist leather, req 22, Old Serra'kis) - 12.0 / 12.0; beats guide gear: yes (vs Bravo's Armbands 8.3); drop chance: 32.40%
- Brawler's Leather Helm (252512, head leather, req 25, Aku'mai, Gelihast, Lorgus Jett, Twilight Lord Kelris) - 7.8 / 7.8; beats guide gear: no (vs Defender's Leather Helm 24.0); drop chance: unknown
- Cursed Murloc Eye (273840, trinket, req 24, Gelihast) - 0.0 / 0.0; beats guide gear: no baseline; drop chance: 32.14%
- Spiked Shell Band (273839, finger, req 22, Ghamoo-ra) - 0.0 / 0.0; beats guide gear: no (vs Ring of Precision 12.2); drop chance: 32.06%

## 15_Stockade - 26-27 The Stockade (levels 26-27)

- Dungeon zone id 717; creatures: 38 (11 spawned in the zone, 27 from the chapter's [TAR] ids and the hand list); usable gear drops: 20 (5 not mentioned in the chapter; 0 more hidden as req > 32); weights: level-25 band

### Not mentioned in this chapter

| item | id | slot/type | req | dropper(s) | central | conservative | beats guide gear | drop chance |
|---|---|---|---|---|---|---|---|---|
| Stormrider's Leather Helm (named in 24, 26) | 252514 | head leather | 25 | Bazil Thredd | 25.0 | 15.0 | yes (vs Defender's Leather Helm 24.0) | unknown |
| Totemic Leather Helm | 252456 | head leather | 25 | Bazil Thredd, Dextren Ward, Kam Deepfury | 24.0 | 12.0 | no (vs Defender's Leather Helm 24.0) | unknown |
| Red Wool Cloak | 273825 | back cloth | 26 | Bazil Thredd | 6.0 | 3.0 | no (vs Glowing Thresher Cape 26.0) | 21.24% |
| Nightskulker Ring | 273820 | finger | 23 | Dextren Ward | 0.0 | 0.0 | no (vs Ring of Precision 12.2) | 27.88% |
| Red Defias Mask | 7997 | head leather | ? | Marzon the Silent Blade | 0.0 | 0.0 | no (vs Defender's Leather Helm 24.0) | unknown |

### Mentioned in this chapter

- Graverobber's Shovel (273817, 2H mace, req 23, Dextren Ward) - 333.6 / 333.6; beats guide gear: no (vs Reef Axe 345.9); drop chance: 31.93%
- Kam's Walking Stick (2280, staff, req 24, Kam Deepfury) - 322.8 / 290.8; beats guide gear: no (vs Reef Axe 345.9); drop chance: 32.20%
- Hamhock's Cleaver (273809, 1H axe (shield set), req 25, Hamhock) - 289.0 / 289.0; beats guide gear: no baseline; drop chance: 35.35%
- Prison Shank (2941, dagger (shield set), req 23, Bruegal Ironknuckle) - 253.6 / 253.6; beats guide gear: no baseline; drop chance: 30.71%
- Iron Knuckles (2942, fist weapon (shield set), req 23, Bruegal Ironknuckle) - 247.1 / 247.1; beats guide gear: no baseline; drop chance: 29.92%
- Demolition Girdle (273807, waist leather, req 24, Kam Deepfury) - 34.0 / 25.0; beats guide gear: yes (vs Moss Cinch 24.0); drop chance: 31.22%
- Executioner Mantle (273804, shoulder leather, req 21, Targorr the Dread) - 32.5 / 23.5; beats guide gear: no baseline; drop chance: 29.43%
- Defender's Leather Helm (252455, head leather, req 25, Bazil Thredd, Dextren Ward, Hamhock, Kam Deepfury) - 24.0 / 24.0; beats guide gear: yes (vs Recipe: Mithril Head Trout 0.0); drop chance: unknown
- Blackrock Harness (273805, chest leather, req 21, Targorr the Dread) - 14.0 / 14.0; beats guide gear: yes (vs Blackened Defias Armor 10.3); drop chance: 29.28%
- Dark Horde Band (273806, finger, req 21, Targorr the Dread) - 12.0 / 6.0; beats guide gear: no (vs Ring of Precision 12.2); drop chance: 30.20%
- Brawler's Leather Helm (252512, head leather, req 25, Bazil Thredd, Dextren Ward, Hamhock, Kam Deepfury) - 7.8 / 7.8; beats guide gear: no (vs Defender's Leather Helm 24.0); drop chance: unknown
- Combat Cloak (4716, back cloth, req 27, Bazil Thredd) - 5.0 / 3.0; beats guide gear: no (vs Glowing Thresher Cape 26.0); drop chance: unknown
- Defias Jailbreakers (273824, hands leather, req 26, Bazil Thredd) - 4.7 / 4.7; beats guide gear: no (vs Zodiac Gloves 22.2); drop chance: 21.13%
- Defias Renegade Ring (1076, finger, req 21, Defias Captive, Defias Convict, Defias Inmate, Defias Insurgent +1 more) - 3.1 / 3.1; beats guide gear: no (vs Ring of Precision 12.2); drop chance: unknown
- Superior Boots (9802, feet leather, req 21, Bruegal Ironknuckle, Kam Deepfury, Targorr the Dread) - 0.0 / 0.0; beats guide gear: no (vs Kimbra Boots 12.2); drop chance: unknown

## 22_ExcavationSite - 29-30 Excavation Site: Wetlands (levels 29-30)

- Dungeon zone id 16732; creatures: 27 (0 spawned in the zone, 27 from the chapter's [TAR] ids and the hand list); usable gear drops: 5 (2 not mentioned in the chapter; 0 more hidden as req > 35); weights: level-30 band

### Not mentioned in this chapter

| item | id | slot/type | req | dropper(s) | central | conservative | beats guide gear | drop chance |
|---|---|---|---|---|---|---|---|---|
| Superior Boots (named in 15) | 9802 | feet leather | 21 | Mottled Razormaw, Mottled Scytheclaw | 0.0 | 0.0 | no (vs Ambassador's Boots 12.9) | unknown |
| Thicket Bindings | 286985 | wrist leather | 26 | Highland Horror | no tooltip | no tooltip | no tooltip | unknown |

### Mentioned in this chapter

- Garb of Florid Feathers (273026, chest leather, req 26, Shadetooth) - 25.7 / 25.7; beats guide gear: no (vs Raptorbane Armor 31.0); drop chance: 30.87%
- Ring of Power Regulation (273030, finger, req 28, Relic Guardian) - 12.0 / 6.0; beats guide gear: no (vs Fury Ring 17.0); drop chance: 29.00%
- Supple Bellyskin Leggings (273022, legs leather, req 26, Saltspine) - 12.0 / 12.0; beats guide gear: yes (vs Smith's Trousers 11.8); drop chance: 35.71%

## 24_Gnomeregan - 30-31 Gnomeregan (levels 30-31)

- Dungeon zone id 721; creatures: 61 (43 spawned in the zone, 18 from the chapter's [TAR] ids and the hand list); usable gear drops: 25 (10 not mentioned in the chapter; 3 more hidden as req > 36); weights: level-30 band

### Not mentioned in this chapter

| item | id | slot/type | req | dropper(s) | central | conservative | beats guide gear | drop chance |
|---|---|---|---|---|---|---|---|---|
| Vibroblade | 9485 | 1H axe (shield set) | 25 | Arcane Nullifier X-21, Caverndeep Ambusher, Caverndeep Burrower, Caverndeep Reaver +11 more | 266.8 | 266.8 | no baseline | unknown |
| Oscillating Power Hammer | 9488 | 1H mace (shield set) | 23 | Arcane Nullifier X-21, Caverndeep Ambusher, Caverndeep Burrower, Caverndeep Reaver +13 more | 255.0 | 255.0 | no baseline | unknown |
| Emblazoned Chestpiece | 6396 | chest leather | 27 | Crowd Pummeler 9-60 | 21.7 | 15.7 | no (vs Raptorbane Armor 31.0) | unknown |
| Wisdom's Leather Helm | 252515 | head leather | 25 | Grubbis | 14.0 | 7.0 | no (vs Defender's Leather Helm 24.0) | unknown |
| Combat Cloak (named in 15) | 4716 | back cloth | 27 | Arcane Nullifier X-21, Chomper, Crowd Pummeler 9-60, Dark Iron Agent +9 more | 5.0 | 3.0 | no (vs Glowing Thresher Cape 26.0) | unknown |
| Charged Gear | 9461 | finger | 31 | Mekgineer Thermaplugg | 0.0 | 0.0 | no (vs Fury Ring 17.0) | 25.35% |
| Gnomeregan Amulet | 10299 | neck | 26 | Caverndeep Ambusher, Caverndeep Burrower, Caverndeep Reaver, Dark Iron Agent +5 more | 0.0 | 0.0 | no (vs Thermaplugg Medal of Honor 25.0) | unknown |
| Gnomeregan Band | 10298 | finger | 25 | Caverndeep Ambusher, Caverndeep Burrower, Caverndeep Reaver, Holdout Medic +3 more | 0.0 | 0.0 | no (vs Fury Ring 17.0) | unknown |
| Superior Boots (named in 15) | 9802 | feet leather | 21 | Caverndeep Burrower, Caverndeep Reaver, Irradiated Slime, Techbot | 0.0 | 0.0 | no (vs Acidic Walkers 29.1) | unknown |
| Tough Leather Pants | 1808 | legs leather | 25 | Holdout Warrior, Leprous Defender | 0.0 | 0.0 | no (vs Triprunner Dungarees 23.3) | unknown |

### Mentioned in this chapter

- Thermaplugg's Left Arm (9459, 2H axe, req 31, Mekgineer Thermaplugg) - 476.8 / 476.8; beats guide gear: yes (vs Manual Crowd Pummeler 442.8); drop chance: 23.87%
- Manual Crowd Pummeler (9449, 2H mace, req 29, Crowd Pummeler 9-60) - 442.8 / 442.8; beats guide gear: no (vs Thermaplugg's Left Arm 476.8); drop chance: 31.60%
- Hydrocane (9452, staff, req 27, Viscous Fallout) - 349.5 / 313.5; beats guide gear: no (vs Thermaplugg's Left Arm 476.8); drop chance: 30.86%
- Supercharger Battle Axe (9486, 2H axe, req 23, Arcane Nullifier X-21, Caverndeep Ambusher, Caverndeep Burrower, Caverndeep Reaver +14 more) - 322.6 / 322.6; beats guide gear: no (vs Thermaplugg's Left Arm 476.8); drop chance: unknown
- Toxic Revenger (9453, dagger (shield set), req 27, Viscous Fallout) - 287.4 / 287.4; beats guide gear: no baseline; drop chance: 33.90%
- Royal Diplomatic Scepter (9457, 1H mace (shield set), req 30, Dark Iron Ambassador) - 280.6 / 248.6; beats guide gear: no baseline; drop chance: 21.10%
- Skullduggery Belt (274042, waist leather, req 29, Grubbis) - 33.5 / 26.5; beats guide gear: yes (vs Moss Cinch 24.0); drop chance: 32.28%
- Stormrider's Leather Helm (252514, head leather, req 25, Grubbis) - 25.0 / 15.0; beats guide gear: yes (vs Defender's Leather Helm 24.0); drop chance: unknown
- Thermaplugg Medal of Honor (274068, neck, req 29, Crowd Pummeler 9-60) - 25.0 / 19.0; beats guide gear: no (vs Giantstone Medallion 25.0); drop chance: 35.72%
- Electrocutioner Lagnut (9447, finger, req 29, Electrocutioner 6000) - 23.5 / 13.5; beats guide gear: yes (vs Fury Ring 17.0); drop chance: 30.71%
- Band of Thorns (5007, finger, req 26, Crowd Pummeler 9-60) - 15.0 / 9.0; beats guide gear: no (vs Fury Ring 17.0); drop chance: unknown
- Petrolspill Leggings (9509, legs leather, req 25, Arcane Nullifier X-21, Caverndeep Ambusher, Caverndeep Burrower, Caverndeep Reaver +9 more) - 13.4 / 13.4; beats guide gear: no (vs Triprunner Dungarees 23.3); drop chance: unknown
- Gnomebot Operating Boots (9450, feet leather, req 29, Crowd Pummeler 9-60) - 8.0 / 4.0; beats guide gear: no (vs Acidic Walkers 29.1); drop chance: 29.79%
- Emissary Cuffs (9455, wrist leather, req 30, Dark Iron Ambassador) - 0.0 / 0.0; beats guide gear: no (vs Bands of Serra'kis 12.0); drop chance: 36.13%
- Tundra Necklace (12039, neck, req 28, Grubbis) - 0.0 / 0.0; beats guide gear: no (vs Thermaplugg Medal of Honor 25.0); drop chance: unknown

## 26_RazorfenKraul - 30-31 Razorfen Kraul (levels 30-31)

- Dungeon zone id 491; creatures: 48 (41 spawned in the zone, 7 from the chapter's [TAR] ids and the hand list); usable gear drops: 26 (6 not mentioned in the chapter; 0 more hidden as req > 36); weights: level-30 band

### Not mentioned in this chapter

| item | id | slot/type | req | dropper(s) | central | conservative | beats guide gear | drop chance |
|---|---|---|---|---|---|---|---|---|
| Death Prophet Spine | 274158 | staff | 26 | Aggem Thorncurse | 333.0 | 299.0 | no (vs Thermaplugg's Left Arm 476.8) | 31.02% |
| Vendetta | 776 | dagger (shield set) | 26 | Death's Head Acolyte, Death's Head Adept, Death's Head Sage, Death's Head Seer +12 more | 275.9 | 275.9 | no baseline | unknown |
| Death Speaker Scepter | 2816 | 1H mace (shield set) | 28 | Death Speaker Jargba | 200.1 | 200.1 | no baseline | 33.45% |
| Thornweaver Drape | 274149 | back cloth | 25 | Roogug | 29.0 | 16.0 | yes (vs Glowing Thresher Cape 26.0) | 28.04% |
| Roogug's Severed Head | 274152 | trinket | 25 | Roogug | 15.0 | 9.0 | no (vs Whisperwind Headdress 41.5) | 36.30% |
| Tough Leather Pants | 1808 | legs leather | 25 | Quilguard Champion | 0.0 | 0.0 | no (vs Ferine Leggings 39.7) | unknown |

### Mentioned in this chapter

- Corpsemaker (6687, 2H axe, req 29, Overlord Ramtusk) - 435.3 / 435.3; beats guide gear: no (vs Thermaplugg's Left Arm 476.8); drop chance: 34.43%
- Wind Spirit Staff (6689, staff, req 29, Earthcaller Halmgar) - 385.0 / 346.0; beats guide gear: no (vs Thermaplugg's Left Arm 476.8); drop chance: 46.77%
- Slaghammer (1976, 2H mace, req 24, Death's Head Adept, Death's Head Priest, Death's Head Sage, Death's Head Seer +16 more) - 354.5 / 354.5; beats guide gear: no (vs Thermaplugg's Left Arm 476.8); drop chance: unknown
- Pronged Reaver (6692, 1H axe (shield set), req 30, Charlga Razorflank) - 343.4 / 338.4; beats guide gear: no baseline; drop chance: 29.90%
- Swinetusk Shank (6691, dagger (shield set), req 30, Agathelos the Raging) - 304.6 / 260.6; beats guide gear: no baseline; drop chance: 39.40%
- Thornspike (6681, dagger (shield set), req 27, Aggem Thorncurse) - 288.3 / 288.3; beats guide gear: no baseline; drop chance: 33.40%
- Staff of the Shade (2549, staff, req 22, Agam'ar, Death's Head Acolyte, Death's Head Adept, Death's Head Priest +22 more) - 231.6 / 231.6; beats guide gear: no (vs Thermaplugg's Left Arm 476.8); drop chance: unknown
- Geomancer Headdress (274155, head leather, req 25, Roogug) - 43.0 / 25.0; beats guide gear: yes (vs Whisperwind Headdress 41.5); drop chance: 30.90%
- Whisperwind Headdress (6688, head leather, req 29, Earthcaller Halmgar) - 41.5 / 23.5; beats guide gear: yes (vs Defender's Leather Helm 24.0); drop chance: 49.25%
- Ferine Leggings (6690, legs leather, req 29, Agathelos the Raging) - 39.7 / 39.7; beats guide gear: yes (vs Triprunner Dungarees 23.3); drop chance: 28.66%
- Stormrider's Leather Helm (252514, head leather, req 25, Death Speaker Jargba) - 25.0 / 15.0; beats guide gear: no (vs Whisperwind Headdress 41.5); drop chance: unknown
- Defender's Leather Helm (252455, head leather, req 25, Agathelos the Raging, Aggem Thorncurse, Charlga Razorflank, Death Speaker Jargba +2 more) - 24.0 / 24.0; beats guide gear: no (vs Whisperwind Headdress 41.5); drop chance: unknown
- Totemic Leather Helm (252456, head leather, req 25, Aggem Thorncurse, Charlga Razorflank) - 24.0 / 12.0; beats guide gear: no (vs Whisperwind Headdress 41.5); drop chance: unknown
- Thorncursed Grips (274159, hands leather, req 27, Aggem Thorncurse) - 18.0 / 18.0; beats guide gear: no (vs Zodiac Gloves 22.1); drop chance: 34.25%
- Mantle of Thieves (2264, shoulder leather, req 25, Death's Head Acolyte, Death's Head Adept, Death's Head Sage, Death's Head Seer +15 more) - 17.1 / 14.1; beats guide gear: no (vs Executioner Mantle 32.5); drop chance: unknown
- Wolfclaw Gloves (1978, hands leather, req 22, Agam'ar, Death's Head Acolyte, Death's Head Adept, Death's Head Priest +21 more) - 15.8 / 15.8; beats guide gear: no (vs Zodiac Gloves 22.1); drop chance: unknown
- Agamaggan's Clutch (6693, finger, req 30, Charlga Razorflank) - 15.0 / 9.0; beats guide gear: no (vs Tiger Band 22.5); drop chance: 31.87%
- Stygian Bone Amulet (6695, neck, req 29, Blind Hunter) - 10.0 / 5.0; beats guide gear: no (vs Thermaplugg Medal of Honor 25.0); drop chance: 33.33%
- Brawler's Leather Helm (252512, head leather, req 25, Agathelos the Raging, Aggem Thorncurse, Blind Hunter, Charlga Razorflank +2 more) - 9.6 / 9.6; beats guide gear: no (vs Whisperwind Headdress 41.5); drop chance: unknown
- Plains Ring (2039, finger, req 24, Death's Head Acolyte, Death's Head Adept, Death's Head Sage, Death's Head Seer +19 more) - 3.4 / 3.4; beats guide gear: no (vs Tiger Band 22.5); drop chance: unknown

## Item ids with no tooltip

```
03_HallOfThanes: (none)
07_Deadmines: (none)
08_RuinsOfLordaeron: (none)
13_Blackfathom: (none)
15_Stockade: (none)
22_ExcavationSite: 286985
24_Gnomeregan: (none)
26_RazorfenKraul: (none)
```

## Data provenance

- QuestieDB: Forever 1.0.16 (contract 4, built 2023-11-14T22:13:20Z) - tooling/qdb/
- Client Item table: build 1.60.1.70938 - tooling/client/1.60.1.70938/Item.csv
- Tooltips (newest file wins per item): weights/tooltips/2026-11-12.json dated 2026-11-12 - 1527 items taken; weights/tooltips/2026-11-11.json dated 2026-11-11 - 0 items taken; weights/tooltips/2026-11-08.json dated 2026-11-08 - 0 items taken; weights/tooltips/2026-11-05.json dated 2026-11-05 - 0 items taken; weights/tooltips/2026-11-02.json dated 2026-11-02 - 0 items taken; weights/tooltips/2026-11-01.json dated 2026-11-01 - 0 items taken; weights/tooltips/2026-10-29.json dated 2026-10-29 - 0 items taken; weights/item_tooltips.json dated 2026-09-24 (sources.json fallback_date) - 0 items taken
- Weights: level-20 central wdps=14 str=2 ap=1 int=1.15 agi=0.8 spi=2.5 sta=0 sp=2 exp=3; conservative Spi 1.5 SP 1.0 Exp 1.0; no mace term (spec removed 17 Oct 2026); other bands take Int/Agi from enh_weights: L10 int=0.41 agi=0.46; L15 int=1.13 agi=0.55; L25 int=1.17 agi=0.78; L30 int=1.14 agi=0.96; L40 int=1.19 agi=1.13
- Creatures: QuestieDB zone spawns + the chapter's [TAR] ids + the DUNGEONS hand list of spawnless bosses. Trash in Ruins of Lordaeron and Excavation Site has no zone spawn in QuestieDB and is not listed.
- Drop chances come only from tooltip text ("Drop Chance"); Wowhead shows them only for single-dropper items.
