# Dungeon loot check - 2026-11-03

Report only (tooling/dungeon_loot.py). Gear a Dwarf 2H Enhancement shaman can use at 1-30 that QuestieDB lists as dropping from creatures inside each dungeon (zone spawns, the chapter's [TAR] ids and a hand list of spawnless bosses), scored with weights/score_items.py (AP-equivalent; central and conservative weight sets, band nearest the chapter's starting level; no mace term). "Beats guide gear" compares the central score with the best item in the same slot that the guide calls out in green on a Shaman/Dwarf line in this chapter or any earlier one. 1H weapons are the shield set (secondary) and compare only with each other. Drops more than 5 levels above the chapter's top level are left out. "Mentioned" = the full name, or the first word followed by "(" (the helm lines' short form), appears in the chapter. Mail, plate, shields, swords, polearms, ranged and cloth other than cloaks are left out.

## 03_HallOfThanes - 15-16 Hall of Thanes (levels 15-16)

- Dungeon zone id 16919; creatures: 19 (3 spawned in the zone, 16 from the chapter's [TAR] ids and the hand list); usable gear drops: 7 (0 not mentioned in the chapter; 0 more hidden as req > 21); weights: level-15 band

### Not mentioned in this chapter

(none)

### Mentioned in this chapter

- Golemheart Stave (270228, staff, req 13, Plunder) - 193.3 / 175.3; beats guide gear: no (vs Ironforge Greathammer 223.6); drop chance: 33.97%
- Durgen's Crescent Axe (270256, 1H axe (shield set), req 13, Durgen Dirgehammer) - 180.1 / 180.1; beats guide gear: no baseline; drop chance: 28.17%
- Fang of Magmatus (271095, dagger (shield set), req 13, Magmatus) - 144.3 / 126.3; beats guide gear: no baseline; drop chance: 34.81%
- Flamefist Grips (270231, hands leather, req 13, Magmatus) - 8.2 / 5.8; beats guide gear: no baseline; drop chance: 29.01%
- Spiritwraith Drape (271097, back cloth, req 13, Faldrim Anvilmar) - 6.0 / 4.0; beats guide gear: no baseline; drop chance: 33.76%
- Ephemeral Choker (270227, neck, req 13, Faldrim Anvilmar) - 5.0 / 2.5; beats guide gear: no baseline; drop chance: 32.85%
- Direhammer Leggings (270260, legs leather, req 13, Durgen Dirgehammer) - 2.6 / 2.6; beats guide gear: no baseline; drop chance: 23.23%

## 07_Deadmines - 19-20 Deadmines (levels 19-20)

- Dungeon zone id 1581; creatures: 64 (27 spawned in the zone, 37 from the chapter's [TAR] ids and the hand list); usable gear drops: 28 (12 not mentioned in the chapter; 0 more hidden as req > 25); weights: level-20 band

### Not mentioned in this chapter

| item | id | slot/type | req | dropper(s) | central | conservative | beats guide gear | drop chance |
|---|---|---|---|---|---|---|---|---|
| Goblin Hammer | 273297 | 1H mace (shield set) | 18 | Gilnid | 213.5 | 213.5 | no baseline | 1.30% |
| Goblin Screwdriver | 1936 | dagger (shield set) | 13 | Goblin Engineer | 173.4 | 173.4 | no baseline | 5.74% |
| Blackened Defias Gloves | 10401 | hands leather | 14 | Defias Overseer, Defias Taskmaster | 12.0 | 12.0 | no baseline | unknown |
| First Mate Band | 284715 | finger | 17 | Mr. Smite | 8.0 | 8.0 | no baseline | 1.01% |
| Woodworking Gloves | 1945 | hands leather | 13 | Goblin Woodcarver | 6.7 | 5.7 | no baseline | 6.86% |
| Metalworking Gloves | 1944 | hands leather | 13 | Goblin Craftsman | 6.0 | 6.0 | no baseline | 5.41% |
| Blackened Defias Boots | 10402 | feet leather | 15 | Defias Strip Miner | 5.1 | 5.1 | no baseline | 2.92% |
| Lookie's Spyglass | 273298 | trinket | 18 | Cookie | 1.0 | 0.5 | no baseline | 1.04% |
| Red Defias Mask | 7997 | head leather | ? | Defias Blackguard, Defias Evoker, Defias Highwayman, Defias Knuckleduster +10 more | 0.0 | 0.0 | no baseline | unknown |
| Scouting Belt | 6581 | waist leather | 16 | Miner Johnson | 0.0 | 0.0 | no (vs Blackened Defias Belt 18.0) | unknown |
| Stonemason Cloak | 1930 | back cloth | 13 | Defias Miner | 0.0 | 0.0 | no baseline | 2.68% |
| Viridian Band | 11982 | finger | 18 | Cookie | 0.0 | 0.0 | no baseline | unknown |

### Mentioned in this chapter

- Smite's Mighty Hammer (7230, 2H mace, req 18, Mr. Smite) - 301.3 / 301.3; beats guide gear: yes (vs Rockslicer 289.8); drop chance: 18.74%
- Rockslicer (872, 2H axe, req 18, Rhahk'Zor) - 289.8 / 289.8; beats guide gear: no (vs Smite's Mighty Hammer 301.3); drop chance: 5.45%
- Rhahk'Zor's Hammer (5187, 2H mace, req 16, Rhahk'Zor) - 270.2 / 262.2; beats guide gear: no (vs Smite's Mighty Hammer 301.3); drop chance: 70.21%
- Taskmaster Axe (5194, 2H axe, req 18, Sneed) - 235.3 / 216.3; beats guide gear: no (vs Smite's Mighty Hammer 301.3); drop chance: 27.49%
- Emberstone Staff (5201, staff, req 17, Captain Greenskin) - 234.4 / 210.4; beats guide gear: no (vs Smite's Mighty Hammer 301.3); drop chance: 37.82%
- Smite's Reaver (5196, 1H axe (shield set), req 17, Mr. Smite) - 204.3 / 202.8; beats guide gear: no baseline; drop chance: 36.88%
- Cookie's Tenderizer (5197, 1H mace (shield set), req 16, Cookie) - 199.0 / 197.0; beats guide gear: no baseline; drop chance: 54.07%
- Buzzer Blade (2169, dagger (shield set), req 16, Sneed's Shredder) - 159.0 / 137.0; beats guide gear: no baseline; drop chance: 49.98%
- Blackened Defias Belt (10403, waist leather, req 17, Captain Greenskin) - 18.0 / 18.0; beats guide gear: no baseline; drop chance: 26.62%
- Blackened Defias Leggings (10400, legs leather, req 14, Defias Overseer, Defias Taskmaster) - 17.1 / 17.1; beats guide gear: yes (vs Smith's Trousers 11.4); drop chance: unknown
- Stonemason Trousers (1934, legs leather, req 15, Defias Blackguard) - 12.9 / 9.4; beats guide gear: yes (vs Smith's Trousers 11.4); drop chance: 5.74%
- Lavishly Jeweled Ring (1156, finger, req 17, Gilnid) - 11.0 / 11.0; beats guide gear: no baseline; drop chance: 37.47%
- Blackened Defias Armor (10399, chest leather, req 17, Edwin VanCleef) - 10.6 / 10.6; beats guide gear: no baseline; drop chance: 15.43%
- Miner's Cape (5444, back cloth, req 17, Miner Johnson) - 10.0 / 10.0; beats guide gear: no baseline; drop chance: 55.04%
- Smelting Pants (5199, legs leather, req 16, Gilnid) - 5.0 / 2.5; beats guide gear: no (vs Smith's Trousers 11.4); drop chance: 55.26%
- Cape of the Brotherhood (5193, back cloth, req 19, Edwin VanCleef) - 4.2 / 4.2; beats guide gear: no baseline; drop chance: 22.91%

## 08_RuinsOfLordaeron - 20-21 Ruins of Lordaeron (levels 20-21)

- Dungeon zone id 16611; creatures: 22 (0 spawned in the zone, 22 from the chapter's [TAR] ids and the hand list); usable gear drops: 7 (2 not mentioned in the chapter; 0 more hidden as req > 26); weights: level-20 band

### Not mentioned in this chapter

| item | id | slot/type | req | dropper(s) | central | conservative | beats guide gear | drop chance |
|---|---|---|---|---|---|---|---|---|
| Coldspire Staff | 271215 | staff | 19 | Rath'mael | 212.0 | 212.0 | no (vs Smite's Mighty Hammer 301.3) | 32.72% |
| Scepter of the Abandoned | 271216 | 1H mace (shield set) | 17 | The Abandoned | 170.7 | 146.7 | no baseline | 33.65% |

### Mentioned in this chapter

- Segmented Spider Leg (271203, staff, req 15, Witherfang) - 257.6 / 255.2; beats guide gear: no (vs Smite's Mighty Hammer 301.3); drop chance: 31.42%
- Corpse Chopper (271217, 2H axe, req 16, Bjork) - 254.7 / 254.7; beats guide gear: no (vs Smite's Mighty Hammer 301.3); drop chance: 33.28%
- Meathook Slicer (271204, dagger (shield set), req 15, The Baron) - 190.5 / 190.5; beats guide gear: no baseline; drop chance: 30.41%
- Bloodied Chestwraps (271212, chest leather, req 17, Viktor the Vile) - 14.9 / 10.4; beats guide gear: yes (vs Blackened Defias Armor 10.6); drop chance: 33.01%
- Witherbite Bracers (271202, wrist leather, req 15, Witherfang) - 10.9 / 5.9; beats guide gear: yes (vs Bravo's Armbands 8.6); drop chance: 28.87%

## 13_Blackfathom - 25-26 Blackfathom Deeps (levels 25-26)

- Dungeon zone id 719; creatures: 30 (30 spawned in the zone, 0 from the chapter's [TAR] ids and the hand list); usable gear drops: 26 (10 not mentioned in the chapter; 0 more hidden as req > 31); weights: level-25 band

### Not mentioned in this chapter

| item | id | slot/type | req | dropper(s) | central | conservative | beats guide gear | drop chance |
|---|---|---|---|---|---|---|---|---|
| Axe of the Enforcer | 1454 | 1H axe (shield set) | 24 | Aku'mai Snapjaw, Barbed Crustacean, Baron Aquanis, Blackfathom Sea Witch +12 more | 265.8 | 265.8 | no baseline | unknown |
| Doomspike | 3413 | dagger (shield set) | 22 | Aku'mai Fisher, Aku'mai Snapjaw, Barbed Crustacean, Blackfathom Myrmidon +17 more | 248.6 | 248.6 | no baseline | unknown |
| Grimclaw | 1481 | 1H axe (shield set) | 22 | Aku'mai Snapjaw, Barbed Crustacean, Baron Aquanis, Blackfathom Myrmidon +15 more | 241.5 | 241.5 | no baseline | unknown |
| Crested Scepter | 3414 | 1H mace (shield set) | 24 | Aku'mai Snapjaw, Barbed Crustacean, Baron Aquanis, Blackfathom Sea Witch +11 more | 220.9 | 188.9 | no baseline | unknown |
| Evocator's Blade | 2567 | dagger (shield set) | 20 | Aku'mai Fisher, Aku'mai Snapjaw, Barbed Crustacean, Blackfathom Myrmidon +16 more | 203.4 | 172.9 | no baseline | unknown |
| Threshadon Fang | 5516 | dagger (shield set) | 11 | Deep Pool Threshfin, Old Serra'kis | 70.0 | 70.0 | no baseline | unknown |
| Wisdom's Leather Helm | 252515 | head leather | 25 | Twilight Lord Kelris | 10.5 | 3.5 | no (vs Defender's Leather Helm 24.0) | unknown |
| Stormrider's Leather Helm (named in 24, 26) | 252514 | head leather | 25 | Aku'mai | 10.0 | 5.0 | no (vs Defender's Leather Helm 24.0) | unknown |
| Cuirboulli Boots | 2143 | feet leather | 22 | Barbed Crustacean, Blackfathom Myrmidon, Blackfathom Sea Witch, Blindlight Murloc +2 more | 0.0 | 0.0 | no (vs Kimbra Boots 9.4) | unknown |
| Tough Leather Pants | 1808 | legs leather | 25 | Twilight Shadowmage | 0.0 | 0.0 | no (vs Smith's Trousers 11.1) | unknown |

### Mentioned in this chapter

- Reef Axe (6905, 2H axe, req 22, Gelihast) - 341.9 / 333.9; beats guide gear: yes (vs Twilight Maul 338.3); drop chance: 45.52%
- Twilight Maul (273841, 2H mace, req 23, Lorgus Jett) - 338.3 / 326.3; beats guide gear: no (vs Reef Axe 341.9); drop chance: 14.00%
- Rod of the Sleepwalker (1155, staff, req 24, Twilight Lord Kelris) - 306.5 / 269.0; beats guide gear: no (vs Reef Axe 341.9); drop chance: 47.99%
- Staff of the Blessed Seer (2271, staff, req 20, Aku'mai Fisher, Aku'mai Snapjaw, Barbed Crustacean, Baron Aquanis +17 more) - 271.4 / 238.4; beats guide gear: no (vs Reef Axe 341.9); drop chance: unknown
- Staff of the Friar (3415, staff, req 21, Aku'mai Fisher, Aku'mai Snapjaw, Barbed Crustacean, Blackfathom Myrmidon +17 more) - 265.7 / 242.7; beats guide gear: no (vs Reef Axe 341.9); drop chance: unknown
- Bite of Serra'kis (6904, dagger (shield set), req 23, Old Serra'kis) - 247.7 / 247.7; beats guide gear: no baseline; drop chance: 22.66%
- Defender's Leather Helm (252455, head leather, req 25, Aku'mai, Gelihast, Lorgus Jett, Old Serra'kis +1 more) - 24.0 / 24.0; beats guide gear: no baseline; drop chance: unknown
- Moss Cinch (6911, waist leather, req 25, Aku'mai) - 18.0 / 6.0; beats guide gear: no (vs Blackened Defias Belt 18.0); drop chance: 35.80%
- Totemic Leather Helm (252456, head leather, req 25, Aku'mai, Baron Aquanis, Gelihast, Lorgus Jett +2 more) - 18.0 / 6.0; beats guide gear: no (vs Defender's Leather Helm 24.0); drop chance: unknown
- Naga Battle Gloves (888, hands leather, req 22, Lady Sarevess) - 15.5 / 10.5; beats guide gear: no baseline; drop chance: 36.62%
- Glowing Thresher Cape (6901, back cloth, req 24, Old Serra'kis) - 12.5 / 5.5; beats guide gear: yes (vs Grave Shroud 6.0); drop chance: 37.86%
- Bands of Serra'kis (6902, wrist leather, req 22, Old Serra'kis) - 12.0 / 12.0; beats guide gear: yes (vs Bravo's Armbands 8.3); drop chance: 33.41%
- Brawler's Leather Helm (252512, head leather, req 25, Aku'mai, Gelihast, Lorgus Jett, Twilight Lord Kelris) - 7.8 / 7.8; beats guide gear: no (vs Defender's Leather Helm 24.0); drop chance: unknown
- Ring of Precision (1491, finger, req 22, Aku'mai Fisher, Aku'mai Snapjaw, Barbed Crustacean, Baron Aquanis +16 more) - 7.7 / 6.2; beats guide gear: no baseline; drop chance: unknown
- Cursed Murloc Eye (273840, trinket, req 24, Gelihast) - 0.0 / 0.0; beats guide gear: no baseline; drop chance: 4.33%
- Spiked Shell Band (273839, finger, req 22, Ghamoo-ra) - 0.0 / 0.0; beats guide gear: no (vs Ring of Precision 7.7); drop chance: 4.19%

## 15_Stockade - 26-27 The Stockade (levels 26-27)

- Dungeon zone id 717; creatures: 38 (11 spawned in the zone, 27 from the chapter's [TAR] ids and the hand list); usable gear drops: 20 (5 not mentioned in the chapter; 0 more hidden as req > 32); weights: level-25 band

### Not mentioned in this chapter

| item | id | slot/type | req | dropper(s) | central | conservative | beats guide gear | drop chance |
|---|---|---|---|---|---|---|---|---|
| Totemic Leather Helm | 252456 | head leather | 25 | Bazil Thredd, Dextren Ward, Kam Deepfury | 18.0 | 6.0 | no (vs Defender's Leather Helm 24.0) | unknown |
| Stormrider's Leather Helm (named in 24, 26) | 252514 | head leather | 25 | Bazil Thredd | 10.0 | 5.0 | no (vs Defender's Leather Helm 24.0) | unknown |
| Red Wool Cloak | 273825 | back cloth | 26 | Bazil Thredd | 4.5 | 1.5 | no (vs Glowing Thresher Cape 12.5) | 0.92% |
| Nightskulker Ring | 273820 | finger | 23 | Dextren Ward | 0.0 | 0.0 | no (vs Ring of Precision 7.7) | 1.36% |
| Red Defias Mask | 7997 | head leather | ? | Marzon the Silent Blade | 0.0 | 0.0 | no (vs Defender's Leather Helm 24.0) | unknown |

### Mentioned in this chapter

- Graverobber's Shovel (273817, 2H mace, req 23, Dextren Ward) - 333.6 / 333.6; beats guide gear: no (vs Reef Axe 341.9); drop chance: 2.00%
- Kam's Walking Stick (2280, staff, req 24, Kam Deepfury) - 308.1 / 276.1; beats guide gear: no (vs Reef Axe 341.9); drop chance: 2.93%
- Hamhock's Cleaver (273809, 1H axe (shield set), req 25, Hamhock) - 289.0 / 289.0; beats guide gear: no baseline; drop chance: 1.75%
- Prison Shank (2941, dagger (shield set), req 23, Bruegal Ironknuckle) - 253.6 / 253.6; beats guide gear: no baseline; drop chance: 19.82%
- Iron Knuckles (2942, fist weapon (shield set), req 23, Bruegal Ironknuckle) - 247.1 / 247.1; beats guide gear: no baseline; drop chance: 18.50%
- Demolition Girdle (273807, waist leather, req 24, Kam Deepfury) - 29.5 / 20.5; beats guide gear: yes (vs Moss Cinch 18.0); drop chance: 2.19%
- Defender's Leather Helm (252455, head leather, req 25, Bazil Thredd, Dextren Ward, Kam Deepfury) - 24.0 / 24.0; beats guide gear: no baseline; drop chance: unknown
- Executioner Mantle (273804, shoulder leather, req 21, Targorr the Dread) - 19.0 / 14.5; beats guide gear: no baseline; drop chance: 1.50%
- Blackrock Harness (273805, chest leather, req 21, Targorr the Dread) - 14.0 / 14.0; beats guide gear: yes (vs Blackened Defias Armor 10.3); drop chance: 1.70%
- Dark Horde Band (273806, finger, req 21, Targorr the Dread) - 9.0 / 3.0; beats guide gear: yes (vs Ring of Precision 7.7); drop chance: 1.68%
- Brawler's Leather Helm (252512, head leather, req 25, Bazil Thredd, Dextren Ward, Hamhock, Kam Deepfury) - 7.8 / 7.8; beats guide gear: no (vs Defender's Leather Helm 24.0); drop chance: unknown
- Defias Jailbreakers (273824, hands leather, req 26, Bazil Thredd) - 4.7 / 4.7; beats guide gear: no (vs Naga Battle Gloves 15.5); drop chance: 0.98%
- Defias Renegade Ring (1076, finger, req 21, Defias Captive, Defias Convict, Defias Inmate, Defias Insurgent +1 more) - 3.1 / 3.1; beats guide gear: no (vs Ring of Precision 7.7); drop chance: unknown
- Combat Cloak (4716, back cloth, req 27, Bazil Thredd) - 2.0 / 1.0; beats guide gear: no (vs Glowing Thresher Cape 12.5); drop chance: unknown
- Superior Boots (9802, feet leather, req 21, Bruegal Ironknuckle, Kam Deepfury, Targorr the Dread) - 0.0 / 0.0; beats guide gear: no (vs Kimbra Boots 9.4); drop chance: unknown

## 22_ExcavationSite - 29-30 Excavation Site: Wetlands (levels 29-30)

- Dungeon zone id 16732; creatures: 27 (0 spawned in the zone, 27 from the chapter's [TAR] ids and the hand list); usable gear drops: 4 (1 not mentioned in the chapter; 0 more hidden as req > 35); weights: level-30 band

### Not mentioned in this chapter

| item | id | slot/type | req | dropper(s) | central | conservative | beats guide gear | drop chance |
|---|---|---|---|---|---|---|---|---|
| Superior Boots (named in 15) | 9802 | feet leather | 21 | Mottled Razormaw, Mottled Scytheclaw | 0.0 | 0.0 | no (vs Kimbra Boots 9.4) | unknown |

### Mentioned in this chapter

- Garb of Florid Feathers (273026, chest leather, req 26, Shadetooth) - 31.7 / 31.7; beats guide gear: yes (vs Raptorbane Armor 31.0); drop chance: 32.06%
- Supple Bellyskin Leggings (273022, legs leather, req 26, Saltspine) - 12.0 / 12.0; beats guide gear: no (vs Carnage Trousers 12.7); drop chance: 34.53%
- Ring of Power Regulation (273030, finger, req 28, Relic Guardian) - 9.0 / 3.0; beats guide gear: no (vs Fury Ring 14.0); drop chance: 29.67%

## 24_Gnomeregan - 30-31 Gnomeregan (levels 30-31)

- Dungeon zone id 721; creatures: 52 (35 spawned in the zone, 17 from the chapter's [TAR] ids and the hand list); usable gear drops: 25 (10 not mentioned in the chapter; 3 more hidden as req > 36); weights: level-30 band

### Not mentioned in this chapter

| item | id | slot/type | req | dropper(s) | central | conservative | beats guide gear | drop chance |
|---|---|---|---|---|---|---|---|---|
| Vibroblade | 9485 | 1H axe (shield set) | 25 | Arcane Nullifier X-21, Caverndeep Ambusher, Caverndeep Burrower, Caverndeep Reaver +11 more | 266.8 | 266.8 | no baseline | unknown |
| Oscillating Power Hammer | 9488 | 1H mace (shield set) | 23 | Arcane Nullifier X-21, Caverndeep Ambusher, Caverndeep Burrower, Caverndeep Reaver +13 more | 255.0 | 255.0 | no baseline | unknown |
| Emblazoned Chestpiece | 6396 | chest leather | 27 | Crowd Pummeler 9-60 | 12.1 | 9.1 | no (vs Garb of Florid Feathers 31.7) | unknown |
| Wisdom's Leather Helm | 252515 | head leather | 25 | Grubbis | 10.5 | 3.5 | no (vs Defender's Leather Helm 24.0) | unknown |
| Combat Cloak (named in 15) | 4716 | back cloth | 27 | Arcane Nullifier X-21, Chomper, Crowd Pummeler 9-60, Dark Iron Agent +9 more | 2.0 | 1.0 | no (vs Repairman's Cape 12.8) | unknown |
| Charged Gear | 9461 | finger | 31 | Mekgineer Thermaplugg | 0.0 | 0.0 | no (vs Fury Ring 14.0) | 32.60% |
| Gnomeregan Amulet | 10299 | neck | 26 | Caverndeep Ambusher, Caverndeep Burrower, Caverndeep Reaver, Dark Iron Agent +5 more | 0.0 | 0.0 | no (vs Thermaplugg Medal of Honor 16.0) | unknown |
| Gnomeregan Band | 10298 | finger | 25 | Caverndeep Ambusher, Caverndeep Burrower, Caverndeep Reaver, Holdout Medic +3 more | 0.0 | 0.0 | no (vs Fury Ring 14.0) | unknown |
| Superior Boots (named in 15) | 9802 | feet leather | 21 | Caverndeep Burrower, Caverndeep Reaver, Irradiated Slime, Techbot | 0.0 | 0.0 | no (vs Acidic Walkers 24.2) | unknown |
| Tough Leather Pants | 1808 | legs leather | 25 | Holdout Warrior, Leprous Defender | 0.0 | 0.0 | no (vs Triprunner Dungarees 21.7) | unknown |

### Mentioned in this chapter

- Thermaplugg's Left Arm (9459, 2H axe, req 31, Mekgineer Thermaplugg) - 478.6 / 478.6; beats guide gear: yes (vs Manual Crowd Pummeler 442.4); drop chance: 18.63%
- Manual Crowd Pummeler (9449, 2H mace, req 29, Crowd Pummeler 9-60) - 442.4 / 442.4; beats guide gear: no (vs Thermaplugg's Left Arm 478.6); drop chance: 33.03%
- Hydrocane (9452, staff, req 27, Viscous Fallout) - 331.5 / 295.5; beats guide gear: no (vs Thermaplugg's Left Arm 478.6); drop chance: 20.03%
- Supercharger Battle Axe (9486, 2H axe, req 23, Arcane Nullifier X-21, Caverndeep Ambusher, Caverndeep Burrower, Caverndeep Reaver +14 more) - 322.6 / 322.6; beats guide gear: no (vs Thermaplugg's Left Arm 478.6); drop chance: unknown
- Toxic Revenger (9453, dagger (shield set), req 27, Viscous Fallout) - 287.4 / 287.4; beats guide gear: no baseline; drop chance: 18.25%
- Royal Diplomatic Scepter (9457, 1H mace (shield set), req 30, Dark Iron Ambassador) - 257.6 / 229.1; beats guide gear: no baseline; drop chance: 21.62%
- Skullduggery Belt (274042, waist leather, req 29, Grubbis) - 23.0 / 19.5; beats guide gear: yes (vs Moss Cinch 18.0); drop chance: 1.98%
- Thermaplugg Medal of Honor (274068, neck, req 29, Crowd Pummeler 9-60) - 16.0 / 13.0; beats guide gear: yes (vs Replica Crescent Necklace 5.6); drop chance: 0.97%
- Petrolspill Leggings (9509, legs leather, req 25, Arcane Nullifier X-21, Caverndeep Ambusher, Caverndeep Burrower, Caverndeep Reaver +9 more) - 12.2 / 12.2; beats guide gear: no (vs Triprunner Dungarees 21.7); drop chance: unknown
- Electrocutioner Lagnut (9447, finger, req 29, Electrocutioner 6000) - 11.5 / 5.0; beats guide gear: no (vs Fury Ring 14.0); drop chance: 31.77%
- Stormrider's Leather Helm (252514, head leather, req 25, Grubbis) - 10.0 / 5.0; beats guide gear: no (vs Defender's Leather Helm 24.0); drop chance: unknown
- Band of Thorns (5007, finger, req 26, Crowd Pummeler 9-60) - 6.0 / 3.0; beats guide gear: no (vs Fury Ring 14.0); drop chance: unknown
- Gnomebot Operating Boots (9450, feet leather, req 29, Crowd Pummeler 9-60) - 6.0 / 2.0; beats guide gear: no (vs Acidic Walkers 24.2); drop chance: 64.10%
- Emissary Cuffs (9455, wrist leather, req 30, Dark Iron Ambassador) - 0.0 / 0.0; beats guide gear: no (vs Bands of Serra'kis 12.0); drop chance: 42.04%
- Tundra Necklace (12039, neck, req 28, Grubbis) - 0.0 / 0.0; beats guide gear: no (vs Thermaplugg Medal of Honor 16.0); drop chance: unknown

## 26_RazorfenKraul - 30-31 Razorfen Kraul (levels 30-31)

- Dungeon zone id 491; creatures: 48 (41 spawned in the zone, 7 from the chapter's [TAR] ids and the hand list); usable gear drops: 26 (6 not mentioned in the chapter; 0 more hidden as req > 36); weights: level-30 band

### Not mentioned in this chapter

| item | id | slot/type | req | dropper(s) | central | conservative | beats guide gear | drop chance |
|---|---|---|---|---|---|---|---|---|
| Death Prophet Spine | 274158 | staff | 26 | Aggem Thorncurse | 316.0 | 282.0 | no (vs Thermaplugg's Left Arm 478.6) | 4.14% |
| Vendetta | 776 | dagger (shield set) | 26 | Death's Head Acolyte, Death's Head Adept, Death's Head Sage, Death's Head Seer +12 more | 275.3 | 275.3 | no baseline | unknown |
| Death Speaker Scepter | 2816 | 1H mace (shield set) | 28 | Death Speaker Jargba | 200.1 | 200.1 | no baseline | 11.68% |
| Thornweaver Drape | 274149 | back cloth | 25 | Roogug | 16.5 | 6.5 | yes (vs Repairman's Cape 12.8) | 2.73% |
| Roogug's Severed Head | 274152 | trinket | 25 | Roogug | 6.0 | 3.0 | no (vs Defender's Leather Helm 24.0) | 2.95% |
| Tough Leather Pants | 1808 | legs leather | 25 | Quilguard Champion | 0.0 | 0.0 | no (vs Ferine Leggings 45.1) | unknown |

### Mentioned in this chapter

- Corpsemaker (6687, 2H axe, req 29, Overlord Ramtusk) - 435.3 / 435.3; beats guide gear: no (vs Thermaplugg's Left Arm 478.6); drop chance: 33.95%
- Slaghammer (1976, 2H mace, req 24, Death's Head Adept, Death's Head Priest, Death's Head Sage, Death's Head Seer +16 more) - 354.5 / 354.5; beats guide gear: no (vs Thermaplugg's Left Arm 478.6); drop chance: unknown
- Wind Spirit Staff (6689, staff, req 29, Earthcaller Halmgar) - 349.5 / 318.5; beats guide gear: no (vs Thermaplugg's Left Arm 478.6); drop chance: 48.00%
- Pronged Reaver (6692, 1H axe (shield set), req 30, Charlga Razorflank) - 335.9 / 333.4; beats guide gear: no baseline; drop chance: 18.55%
- Thornspike (6681, dagger (shield set), req 27, Aggem Thorncurse) - 288.3 / 288.3; beats guide gear: no baseline; drop chance: 44.79%
- Swinetusk Shank (6691, dagger (shield set), req 30, Agathelos the Raging) - 278.6 / 236.6; beats guide gear: no baseline; drop chance: 33.57%
- Staff of the Shade (2549, staff, req 22, Agam'ar, Death's Head Acolyte, Death's Head Adept, Death's Head Priest +22 more) - 231.6 / 231.6; beats guide gear: no (vs Thermaplugg's Left Arm 478.6); drop chance: unknown
- Ferine Leggings (6690, legs leather, req 29, Agathelos the Raging) - 45.1 / 45.1; beats guide gear: yes (vs Triprunner Dungarees 21.7); drop chance: 59.52%
- Defender's Leather Helm (252455, head leather, req 25, Agathelos the Raging, Aggem Thorncurse, Charlga Razorflank, Earthcaller Halmgar) - 24.0 / 24.0; beats guide gear: no baseline; drop chance: unknown
- Whisperwind Headdress (6688, head leather, req 29, Earthcaller Halmgar) - 21.5 / 9.0; beats guide gear: no (vs Defender's Leather Helm 24.0); drop chance: 46.84%
- Geomancer Headdress (274155, head leather, req 25, Roogug) - 20.0 / 9.0; beats guide gear: no (vs Defender's Leather Helm 24.0); drop chance: 3.26%
- Thorncursed Grips (274159, hands leather, req 27, Aggem Thorncurse) - 18.0 / 18.0; beats guide gear: yes (vs Operator's Gloves 16.0); drop chance: 4.51%
- Totemic Leather Helm (252456, head leather, req 25, Aggem Thorncurse, Charlga Razorflank) - 18.0 / 6.0; beats guide gear: no (vs Defender's Leather Helm 24.0); drop chance: unknown
- Wolfclaw Gloves (1978, hands leather, req 22, Agam'ar, Death's Head Acolyte, Death's Head Adept, Death's Head Priest +21 more) - 15.2 / 15.2; beats guide gear: no (vs Thorncursed Grips 18.0); drop chance: unknown
- Mantle of Thieves (2264, shoulder leather, req 25, Death's Head Acolyte, Death's Head Adept, Death's Head Sage, Death's Head Seer +15 more) - 11.7 / 10.2; beats guide gear: no (vs Batwing Mantle 29.1); drop chance: unknown
- Stormrider's Leather Helm (252514, head leather, req 25, Death Speaker Jargba) - 10.0 / 5.0; beats guide gear: no (vs Defender's Leather Helm 24.0); drop chance: unknown
- Brawler's Leather Helm (252512, head leather, req 25, Agathelos the Raging, Aggem Thorncurse, Charlga Razorflank, Death Speaker Jargba +1 more) - 8.7 / 8.7; beats guide gear: no (vs Defender's Leather Helm 24.0); drop chance: unknown
- Stygian Bone Amulet (6695, neck, req 29, Blind Hunter) - 7.5 / 2.5; beats guide gear: no (vs Thermaplugg Medal of Honor 16.0); drop chance: 26.00%
- Agamaggan's Clutch (6693, finger, req 30, Charlga Razorflank) - 6.0 / 3.0; beats guide gear: no (vs Ladimore Heirloom Ring 17.0); drop chance: 34.89%
- Plains Ring (2039, finger, req 24, Death's Head Acolyte, Death's Head Adept, Death's Head Sage, Death's Head Seer +19 more) - 4.8 / 4.8; beats guide gear: no (vs Ladimore Heirloom Ring 17.0); drop chance: unknown

## Item ids with no tooltip

```
03_HallOfThanes: (none)
07_Deadmines: (none)
08_RuinsOfLordaeron: (none)
13_Blackfathom: (none)
15_Stockade: (none)
22_ExcavationSite: (none)
24_Gnomeregan: (none)
26_RazorfenKraul: (none)
```

## Data provenance

- QuestieDB: Forever 1.0.10 (contract 4, built 2023-11-14T22:13:20Z) - tooling/qdb/
- Client Item table: build 1.60.1.70755 - tooling/client/1.60.1.70755/Item.csv
- Tooltips (newest file wins per item): weights/tooltips/2026-11-02.json dated 2026-11-02 - 681 items taken; weights/tooltips/2026-11-01.json dated 2026-11-01 - 0 items taken; weights/tooltips/2026-10-29.json dated 2026-10-29 - 0 items taken; weights/item_tooltips.json dated 2026-09-24 (sources.json fallback_date) - 0 items taken
- Weights: level-20 central wdps=14 str=2 ap=1 int=1.55 agi=0.85 spi=1 sta=0 sp=1.5 exp=3; conservative Spi 0.5 SP 0.5 Exp 1.0; no mace term (spec removed 17 Oct 2026); other bands take Int/Agi from enh_weights: L10 int=0.55 agi=0.53; L15 int=1.53 agi=0.65; L25 int=1.6 agi=0.78; L30 int=1.59 agi=0.87
- Creatures: QuestieDB zone spawns + the chapter's [TAR] ids + the DUNGEONS hand list of spawnless bosses. Trash in Ruins of Lordaeron and Excavation Site has no zone spawn in QuestieDB and is not listed.
- Drop chances come only from tooltip text ("Drop Chance"); Wowhead shows them only for single-dropper items.
