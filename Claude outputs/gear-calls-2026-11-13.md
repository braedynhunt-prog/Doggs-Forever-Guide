# Gear-call check - 2026-11-13

Report only (tooling/gear_calls.py). Dwarf chain of the guide (Hunter and Human lines skipped). Quoted stats on gear lines compared with today's Forever tooltips; quest-reward picks scored with weights/score_items.py (AP-equivalent; band nearest the chapter's starting level; no mace term).

- Tooltips (newest file wins per item): weights/tooltips/2026-11-12.json dated 2026-11-12 - 1527 items taken; weights/tooltips/2026-11-11.json dated 2026-11-11 - 0 items taken; weights/tooltips/2026-11-08.json dated 2026-11-08 - 0 items taken; weights/tooltips/2026-11-05.json dated 2026-11-05 - 0 items taken; weights/tooltips/2026-11-02.json dated 2026-11-02 - 0 items taken; weights/tooltips/2026-11-01.json dated 2026-11-01 - 0 items taken; weights/tooltips/2026-10-29.json dated 2026-10-29 - 0 items taken; weights/item_tooltips.json dated 2026-09-24 (sources.json fallback_date) - 0 items taken
- Weights: level-20 central wdps=14 str=2 ap=1 int=1.15 agi=0.8 spi=2.5 sta=0 sp=2 exp=3; conservative Spi 1.5 SP 1.0 Exp 1.0; no mace term (spec removed 17 Oct 2026); other bands take Int/Agi from enh_weights: L10 int=0.41 agi=0.46; L15 int=1.13 agi=0.55; L25 int=1.17 agi=0.78; L30 int=1.14 agi=0.96; L40 int=1.19 agi=1.13
- Reward choices: data/zone_*.json "itemchoices" (Wowhead Forever atlas, as qinfo.py); item names: tooling/qdb/item.json; gear classes: tooling/client/1.60.1.70938/Item.csv
- Counts: gear lines scanned 452; item names matched 972; stat mismatches 8; quests checked (2+ choices) 180; quests flagged 73

## Part 1 - quoted stats that differ from the tooltip

| chapter | line | item | quoted | tooltip | differs | quoted text |
|---|---|---|---|---|---|---|
| 03_HallOfThanes | 40 | Catacomb Cloak | +2 Sta +3 AP | +2 Sta +7 AP | AP (tooltip AP includes conditional "Attack Power against X", which parse() adds in) | +2 Sta +3 AP, +4 more against humanoids |
| 05_Westfall | 103 | Spiritwraith Drape | +2 Str +2 SP | +3 Agi +4 Spi | Str, SP | cloth +2 Str +2 spell damage |
| 07_Deadmines | 89 | Miner's Cape | +5 Sta +4 AP | +5 Sta +10 AP | AP (tooltip AP includes conditional "Attack Power against X", which parse() adds in) | +5 Sta +4 AP |
| 18_Wetlands1 | 66 | Raptorbane Armor | +3 Sta +16 AP | +3 Sta +31 AP | AP (tooltip AP includes conditional "Attack Power against X", which parse() adds in) | leather chest, 92 armor, +3 Sta, +16 Attack Power, +15 more against beasts - AP feeds Enhancement |
| 22_ExcavationSite | 48 | Raptorbane Armor | +16 AP | +3 Sta +31 AP | AP (tooltip AP includes conditional "Attack Power against X", which parse() adds in) | +16 attack power, +15 more against beasts |
| 26_RazorfenKraul | 59 | Hand Axe | 22.9 dps +5 Str +5 Spi | 1.5 dps | Str, Spi, wdps | 22.9 dps +5 Str +5 Spi, unique |
| 34_ScarletMonastery | 34 | Dog Training Gloves | +24 AP | +45 AP | AP (tooltip AP includes conditional "Attack Power against X", which parse() adds in) | leather hands +24 attack power, +21 more against beasts, req 31, ~30% |
| 51_ZulFarrak | 46 | Apprentice Sorcerer's Slacks | +10 Int +5 Spi +11 SP | +9 Int +17 Spi +8 SP | Int, Spi, SP | Ruuzlu, the Sandfury Executioner, Zerillis; ring +10 Int +5 Spi +11 spell damage -10 Sta |

Parentheses with stat-like text that did not parse:

- 01a_ColdridgeValley:9 Strong Fishing Pole (+5 Fishing)
- 04_LochModan2:47 Hunting Satchel (10 slot bag; hunters: the Hunting Ammo Sack is also +10% ranged speed, the same as the Small Shot Pouch you already own, so the bag is worth more)
- 41_PowderfusePort:65 Riverglades Marsh Gas (50% slow and +15 Fire damage taken in 5 yards, 15 sec cooldown)

## Part 2 - flagged quest-reward picks

Best = best usable choice by central score, 1H weapons excluded unless nothing else is usable. Flagged when the best beats the guide pick by more than 1.0, when the conservative set picks a different item, or when the guide names no pick although a choice scores above 2.0. Weapon scores include 14 x dps, so a weapon choice outscoring armor only says the item is strong for its slot, not that it beats the weapon already worn.

### 01a_ColdridgeValley line 61 - QT218 The Stolen Journal (band L10)

- Smooth Walking Staff (5581) - Two-Hand Staff 2.7 dps; central 38.2 / conservative 38.2; usable
- Dwarven Kite Shield (6176) - Off Hand Shield no stats; central 0.0 / conservative 0.0; not usable - off-hand/ranged (2H build)
- Guide pick: Dwarven Kite Shield (line 62)
- Suggested pick: Smooth Walking Staff
- Why flagged: central best Smooth Walking Staff beats the pick by 38.2

### 01b_DunMorogh line 190 - QT417 A Pilot's Revenge (band L10)

- Compact Hammer (1009) - Main Hand Mace 7.0 dps +1 Sta; central 97.4 / conservative 97.4; usable - 1H (shield set only)
- Craftsman's Dagger (2218) - One-Hand Dagger 6.8 dps +1 Agi; central 95.1 / conservative 95.1; usable - 1H (shield set only)
- Guide pick: none (line 191)
- Suggested pick: Compact Hammer
- Why flagged: guide names no pick (none) but Compact Hammer scores 97.4

### 03_HallOfThanes line 39 - QT96395 An Ancient Grudge (band L15)

- Deepgrave Trousers (279900) - Legs Leather +3 Agi +3 Spi; central 9.2 / conservative 6.2; usable
- Catacomb Cloak (279899) - Back  +2 Sta +7 AP; central 7.0 / conservative 7.0; usable
- Guide pick: Deepgrave Trousers (line 40)
- Suggested pick: Deepgrave Trousers
- Why flagged: conservative best Catacomb Cloak differs from central best Deepgrave Trousers

### 04_LochModan2 line 23 - QT297 Gathering Idols (band L15)

- Trogg Slicer (6186) - Two-Hand Sword 11.9 dps +5 Spi; central 179.2 / conservative 174.2; not usable - sword (shaman can't use)
- Thelsamar Axe (3154) - Main Hand Axe 9.1 dps +2 Agi; central 127.8 / conservative 127.8; usable - 1H (shield set only)
- Dwarven Flamestick (5241) - Ranged Wand 13.6 dps +2 Spi; central 5.0 / conservative 3.0; not usable - wand (shaman can't use)
- Guide pick: none (line 24)
- Suggested pick: Thelsamar Axe
- Why flagged: guide names no pick (none) but Thelsamar Axe scores 127.8

### 04_LochModan2 line 50 - QT217 In Defense of the King's Lands (band L15)

- Lucky Trousers (1832) - Legs Cloth +2 Agi +2 Sta +3 Spi; central 8.6 / conservative 5.6; usable
- Frontier Britches (1436) - Legs Leather +3 Str +3 Agi; central 7.7 / conservative 7.7; usable
- Dwarven Defender (6187) - Off Hand Shield +3 Sta; central 0.0 / conservative 0.0; not usable - off-hand/ranged (2H build)
- Guide pick: Frontier Britches (line 51)
- Suggested pick: Lucky Trousers
- Why flagged: conservative best Frontier Britches differs from central best Lucky Trousers

### 05_Westfall line 51 - QT9 The Killing Fields (band L15)

- Harvester's Robe (1561) - Chest Cloth +2 Spi +2 SP; central 9.0 / conservative 5.0; usable
- Harvester's Pants (3578) - Legs Leather +2 Agi +3 Spi; central 8.6 / conservative 5.6; usable
- Harvester's Pestslayer (276695) - Ranged Bow 6.0 dps +1 Agi +1 Sta; central 0.6 / conservative 0.6; not usable - bow (shaman can't use)
- Guide pick: Harvester's Pants (line 52)
- Suggested pick: Harvester's Robe
- Why flagged: conservative best Harvester's Pants differs from central best Harvester's Robe

### 05_Westfall line 102 - QT153 Red Leather Bandanas (band L15)

- Leggings of the People's Militia (12295) - Legs Cloth +2 Str +2 SP; central 8.0 / conservative 6.0; usable
- Cloak of the People's Militia (3511) - Back  +2 Agi; central 1.1 / conservative 1.1; usable
- Greaves of the People's Militia (5944) - Feet Mail +3 Sta; central 0.0 / conservative 0.0; not usable - mail (40+)
- Guide pick: Cloak of the People's Militia (line 103)
- Suggested pick: Leggings of the People's Militia
- Why flagged: central best Leggings of the People's Militia beats the pick by 6.9

### 07_Deadmines line 127 - QT166 The Defias Brotherhood (band L20)

- Staff of Westfall (2042) - Two-Hand Staff 15.2 dps +5 Int +6 Spi +16 SP; central 265.1 / conservative 243.1; usable
- Chausses of Westfall (6087) - Legs Mail +11 Str +5 Sta; central 22.0 / conservative 22.0; not usable - mail (40+)
- Tunic of Westfall (2041) - Chest Leather +11 Agi +5 Sta; central 8.8 / conservative 8.8; usable
- Guide pick: none (line 128)
- Suggested pick: Staff of Westfall
- Why flagged: guide names no pick (none) but Staff of Westfall scores 265.1

### 07_Deadmines line 132 - QT214 Red Silk Bandanas (band L20)

- Piercing Axe (6094) - Two-Hand Axe 12.6 dps +6 Agi; central 180.9 / conservative 180.9; usable
- Scrimshaw Dagger (2089) - One-Hand Dagger 9.7 dps +2 Sta; central 136.1 / conservative 136.1; usable - 1H (shield set only)
- Solid Shortblade (2074) - One-Hand Sword 9.4 dps +1 Str +1 Sta; central 133.6 / conservative 133.6; not usable - sword (shaman can't use)
- Monastic Hammer (270005) - Main Hand Mace 6.4 dps +2 Int +12 SP; central 116.3 / conservative 104.3; usable - 1H (shield set only)
- Guide pick: none (line 133)
- Suggested pick: Piercing Axe
- Why flagged: guide names no pick (none) but Piercing Axe scores 180.9

### 07_Deadmines line 138 - QT167 Oh Brother... (band L20)

- Miner's Revenge (1893) - Two-Hand Axe 13.0 dps +6 Spi; central 197.0 / conservative 191.0; usable
- Miner's Workboots (270013) - Feet Leather +5 Spi; central 12.5 / conservative 7.5; usable
- Miner's Workgloves (270012) - Hands Cloth +5 Sta; central 0.0 / conservative 0.0; usable
- Guide pick: Miner's Workboots (line 139)
- Suggested pick: Miner's Revenge
- Why flagged: central best Miner's Revenge beats the pick by 184.5

### 07_Deadmines line 140 - QT2040 Underground Assault (band L20)

- Polar Gauntlets (7606) - Hands Mail +4 Str +2 Spi; central 13.0 / conservative 11.0; not usable - mail (40+)
- Dreamer's Leggings (270016) - Legs Leather +6 Int +2 SP; central 10.9 / conservative 8.9; usable
- Bravo's Armbands (270015) - Wrist Leather +3 Str +3 Agi; central 8.4 / conservative 8.4; usable
- Sable Wand (7607) - Ranged Wand 16.9 dps +2 Spi; central 5.0 / conservative 3.0; not usable - wand (shaman can't use)
- Guide pick: Bravo's Armbands (line 141)
- Suggested pick: Dreamer's Leggings
- Why flagged: central best Dreamer's Leggings beats the pick by 2.5

### 09_LochModanMenethil line 20 - QT217 In Defense of the King's Lands (band L20)

- Lucky Trousers (1832) - Legs Cloth +2 Agi +2 Sta +3 Spi; central 9.1 / conservative 6.1; usable
- Frontier Britches (1436) - Legs Leather +3 Str +3 Agi; central 8.4 / conservative 8.4; usable
- Dwarven Defender (6187) - Off Hand Shield +3 Sta; central 0.0 / conservative 0.0; not usable - off-hand/ranged (2H build)
- Guide pick: Frontier Britches (line 20)
- Suggested pick: Lucky Trousers
- Why flagged: conservative best Frontier Britches differs from central best Lucky Trousers

### 09_LochModanMenethil line 84 - QT286 Return the Statuette (band L20)

- Icicle Rod (2950) - Two-Hand Staff 12.5 dps +4 Int +18 SP; central 215.6 / conservative 197.6; usable
- Mariner Boots (2949) - Feet Leather +1 Agi +6 Sta; central 0.8 / conservative 0.8; usable
- Guide pick: Mariner Boots (line 84)
- Suggested pick: Icicle Rod
- Why flagged: central best Icicle Rod beats the pick by 214.8

### 11_Darkshore line 40 - QT4681 Washed Ashore (band L25)

- Dryweed Belt (15399) - Waist Leather +2 Int; central 2.3 / conservative 2.3; usable
- Sandcomber Boots (15398) - Feet Cloth no stats; central 0.0 / conservative 0.0; usable
- Clamshell Bracers (15400) - Wrist Mail no stats; central 0.0 / conservative 0.0; not usable - mail (40+)
- Guide pick: unstated
- Suggested pick: Dryweed Belt
- Why flagged: guide names no pick (unstated) but Dryweed Belt scores 2.3

### 11_Darkshore line 94 - QT1138 Fruit of the Sea (band L25)

- Shucking Gloves (15405) - Hands Leather +2 Sta +2 Int; central 2.3 / conservative 2.3; usable
- Crustacean Boots (15406) - Feet Mail +3 Sta; central 0.0 / conservative 0.0; not usable - mail (40+)
- Guide pick: unstated
- Suggested pick: Shucking Gloves
- Why flagged: guide names no pick (unstated) but Shucking Gloves scores 2.3

### 11_Darkshore line 113 - QT2139 Tharnariun's Hope (band L25)

- Evergreen Gloves (7738) - Hands Cloth +3 Int +2 Spi; central 8.5 / conservative 6.5; usable
- Timberland Cape (7739) - Back  +3 Spi; central 7.5 / conservative 4.5; usable
- Guide pick: Timberland Cape (line 114)
- Suggested pick: Evergreen Gloves
- Why flagged: central best Evergreen Gloves beats the pick by 1.0

### 11_Darkshore line 115 - QT982 Deep Ocean, Vast Sea (band L25)

- Noosegrip Gauntlets (15402) - Hands Mail +2 Str; central 4.0 / conservative 4.0; not usable - mail (40+)
- Welldrip Gloves (15401) - Hands Cloth +2 Int; central 2.3 / conservative 2.3; usable
- Murloc-hide Gloves (270004) - Hands Leather +2 Agi; central 1.6 / conservative 1.6; usable
- Guide pick: unstated
- Suggested pick: Welldrip Gloves
- Why flagged: guide names no pick (unstated) but Welldrip Gloves scores 2.3

### 12_Ashenvale line 72 - QT973 The Tower of Althalaxx (band L25)

- Staff of the Purifier (5613) - Two-Hand Staff 11.2 dps +8 Spi +16 SP; central 209.1 / conservative 185.1; usable
- Clergy Ring (5622) - Finger  +1 Sta +3 Spi; central 7.5 / conservative 4.5; usable
- Guide pick: Clergy Ring (line 73)
- Suggested pick: Staff of the Purifier
- Why flagged: central best Staff of the Purifier beats the pick by 201.6

### 14_Duskwood line 70 - QT181 Look to the Stars (band L25)

- Zodiac Gloves (7106) - Hands Cloth +4 Int +7 Spi; central 22.2 / conservative 15.2; usable
- Belt of the Stars (7107) - Waist Mail +6 Str +6 Sta; central 12.0 / conservative 12.0; not usable - mail (40+)
- Guide pick: unstated
- Suggested pick: Zodiac Gloves
- Why flagged: guide names no pick (unstated) but Zodiac Gloves scores 22.2

### 15_Stockade line 31 - QT98191 A Friend of the Family (band L25)

- Knight's Lance (281296) - Two-Hand Polearm 16.8 dps +7 Agi +5 Sta; central 240.9 / conservative 240.9; not usable - polearm (shaman can't use)
- Royal Dagger (281297) - Main Hand Dagger 8.5 dps +4 Int +18 SP; central 160.1 / conservative 142.1; usable - 1H (shield set only)
- Guide pick: Knight's Lance (line 31)
- Suggested pick: Royal Dagger
- Why flagged: central best Royal Dagger beats the pick by 160.1

### 16_RedridgeEastvale line 53 - QT19 Tharil'zun (band L25)

- Orc Crusher (6093) - Two-Hand Mace 18.2 dps +8 Str +4 Sta; central 270.7 / conservative 270.7; usable
- Fire Hardened Buckler (1276) - Off Hand Shield +5 Spi; central 12.5 / conservative 7.5; not usable - off-hand/ranged (2H build)
- Guide pick: unstated
- Suggested pick: Orc Crusher
- Why flagged: guide names no pick (unstated) but Orc Crusher scores 270.7

### 16_RedridgeEastvale line 56 - QT95999 WANTED: Incinerator Gar'im (band L25)

- Disjointed Shoes (277226) - Feet Leather +12 AP +5 SP; central 22.0 / conservative 17.0; usable
- Alacritous Treads (277234) - Feet Mail +5 Str +5 Agi; central 13.9 / conservative 13.9; not usable - mail (40+)
- Incinerator's Boots (277218) - Feet Cloth +3 Sta +6 Int; central 7.0 / conservative 7.0; usable
- Guide pick: unstated
- Suggested pick: Disjointed Shoes
- Why flagged: guide names no pick (unstated) but Disjointed Shoes scores 22.0

### 17_Duskwood2 line 22 - QT98 The Legend of Stalvan (band L25)

- Crescent of Forlorn Spirits (2044) - Main Hand Axe 18.1 dps +6 Spi; central 268.8 / conservative 262.8; usable - 1H (shield set only)
- Ring of Forlorn Spirits (2043) - Finger  +2 Sta +8 SP; central 16.0 / conservative 8.0; usable
- Ring of Ruin (270053) - Finger  +4 Str +6 Agi; central 12.7 / conservative 12.7; usable
- Guide pick: Ring of Forlorn Spirits (line 23)
- Suggested pick: Ring of Forlorn Spirits
- Why flagged: conservative best Ring of Ruin differs from central best Ring of Forlorn Spirits

### 19_Wetlands2 line 80 - QT304 A Grim Task (band L30)

- Tranquil Ring (2917) - Finger  +1 Int +7 Spi; central 18.6 / conservative 11.6; usable
- Fury Ring (270050) - Finger  +6 Str +2 Spi; central 17.0 / conservative 15.0; usable
- Gold Lion Shield (2916) - Off Hand Shield +2 Str +5 Sta +3 Spi; central 11.5 / conservative 8.5; not usable - off-hand/ranged (2H build)
- Guide pick: Fury Ring (line 81)
- Suggested pick: Tranquil Ring
- Why flagged: central best Tranquil Ring beats the pick by 1.6; conservative best Fury Ring differs from central best Tranquil Ring

### 19_Wetlands2 line 90 - QT633 The Thandol Span (band L30)

- Swampland Trousers (4505) - Legs Cloth +11 Sta +4 Int; central 4.6 / conservative 4.6; usable
- Dwarven Guard Cloak (4504) - Back  +1 Agi +6 Sta; central 1.0 / conservative 1.0; usable
- Guide pick: Dwarven Guard Cloak (line 91)
- Suggested pick: Swampland Trousers
- Why flagged: central best Swampland Trousers beats the pick by 3.6

### 19_Wetlands2 line 110 - QT474 Defeat Nek'rosh (band L30)

- Ancient War Sword (3209) - Two-Hand Sword 21.7 dps +9 Str +6 Sta; central 321.4 / conservative 321.4; not usable - sword (shaman can't use)
- Barreling Reaper (6194) - Main Hand Axe 16.6 dps +5 Sta; central 232.1 / conservative 232.1; usable - 1H (shield set only)
- Dragonmaw Skinflayer (287067) - None  14.7 dps +3 Str +3 Spi; central 13.5 / conservative 10.5; not usable - not equipment
- Guide pick: Ancient War Sword (line 112)
- Suggested pick: Barreling Reaper
- Why flagged: central best Barreling Reaper beats the pick by 232.1

### 20_Darnassus line 9 - QT1275 Researching the Corruption (band L30)

- Prelacy Cape (7004) - Back  +3 Spi +2 SP; central 11.5 / conservative 6.5; usable
- Beetle Clasps (7003) - Wrist Mail +3 Sta +6 AP; central 6.0 / conservative 6.0; not usable - mail (40+)
- Staghide Armguards (270021) - Wrist Leather +3 Agi +3 Sta; central 2.9 / conservative 2.9; usable
- Guide pick: Staghide Armguards (line 10)
- Suggested pick: Prelacy Cape
- Why flagged: central best Prelacy Cape beats the pick by 8.6

### 20_Darnassus line 16 - QT1200 Blackfathom Villainy (band L30)

- Dark Ritual Leggings (270031) - Legs Leather +9 Sta +14 SP; central 28.0 / conservative 14.0; usable
- Cultist's Armguards (270032) - Wrist Leather +7 Sta +10 AP; central 10.0 / conservative 10.0; usable
- Gravestone Scepter (7001) - Ranged Wand 29.0 dps +3 Spi; central 7.5 / conservative 4.5; not usable - wand (shaman can't use)
- Arctic Buckler (7002) - Off Hand Shield +8 Sta +3 Spi; central 7.5 / conservative 4.5; not usable - off-hand/ranged (2H build)
- Guide pick: Gravestone Scepter (line 17)
- Suggested pick: Dark Ritual Leggings
- Why flagged: central best Dark Ritual Leggings beats the pick by 28.0

### 20_Darnassus line 18 - QT1199 Twilight Falls (band L30)

- Heartwood Girdle (7000) - Waist Leather +5 Sta +6 SP; central 12.0 / conservative 6.0; usable
- Nimbus Boots (6998) - Feet Cloth +5 Agi +3 SP; central 10.8 / conservative 7.8; usable
- Silvered Gauntlets (270025) - Hands Mail +5 Sta +3 SP; central 6.0 / conservative 3.0; not usable - mail (40+)
- Guide pick: Heartwood Girdle (line 19)
- Suggested pick: Heartwood Girdle
- Why flagged: conservative best Nimbus Boots differs from central best Heartwood Girdle

### 20_Darnassus line 24 - QT741 The Absent Minded Prospector (band L30)

- Relic Hunter Belt (11936) - Waist Cloth +2 Str +4 Int +2 Spi; central 13.6 / conservative 11.6; usable
- Windfelt Gloves (5630) - Hands Leather +3 Int +4 SP; central 11.4 / conservative 7.4; usable
- Hammerfist Gloves (5629) - Hands Leather +3 Str +3 Agi; central 8.9 / conservative 8.9; usable
- Guide pick: Windfelt Gloves (line 25)
- Suggested pick: Relic Hunter Belt
- Why flagged: central best Relic Hunter Belt beats the pick by 2.1

### 21_AshenvaleEast line 87 - QT981 The Tower of Althalaxx (band L30)

- Seraph's Strike (5614) - Two-Hand Sword 21.1 dps +3 Str +10 Spi; central 326.3 / conservative 316.3; not usable - sword (shaman can't use)
- Pious Legwraps (10043) - Legs Cloth +8 Sta +7 Spi; central 17.5 / conservative 10.5; usable
- Guide pick: unstated
- Suggested pick: Pious Legwraps
- Why flagged: guide names no pick (unstated) but Pious Legwraps scores 17.5

### 22_ExcavationSite line 65 - QT943 The Absent Minded Prospector (band L30)

- Skullchipper (5626) - Two-Hand Axe 13.0 dps +6 Str +1 Sta; central 194.0 / conservative 194.0; usable
- Relic Blade (5627) - One-Hand Dagger 10.0 dps +3 Sta; central 140.0 / conservative 140.0; usable - 1H (shield set only)
- Archaeologist's Gown (270022) - Chest Cloth +5 Spi +2 SP; central 16.5 / conservative 9.5; usable
- Guide pick: unstated
- Suggested pick: Skullchipper
- Why flagged: guide names no pick (unstated) but Skullchipper scores 194.0

### 24_Gnomeregan line 24 - QT98824 Prehistoric Prism (band L30)

- Heavehammer (271766) - Two-Hand Mace 27.7 dps +32 AP; central 420.2 / conservative 420.2; usable
- Healer's Staff (271767) - Two-Hand Staff 20.8 dps +12 Sta +22 SP; central 334.8 / conservative 312.8; usable
- Explorer's League Dustcover (271716) - Back  +5 Agi +5 Int +5 Spi; central 23.0 / conservative 18.0; usable
- Guide pick: unstated
- Suggested pick: Heavehammer
- Why flagged: guide names no pick (unstated) but Heavehammer scores 420.2

### 24_Gnomeregan line 101 - QT2929 The Grand Betrayal (band L30)

- Civinad Robes (9623) - Chest Cloth +7 Sta +12 Spi +9 SP; central 48.0 / conservative 27.0; usable
- Dual Reinforced Leggings (9625) - Legs Mail +12 Str; central 24.0 / conservative 24.0; not usable - mail (40+)
- Triprunner Dungarees (9624) - Legs Leather +3 Str +18 Agi +6 Sta; central 23.3 / conservative 23.3; usable
- Guide pick: unstated
- Suggested pick: Civinad Robes
- Why flagged: guide names no pick (unstated) but Civinad Robes scores 48.0

### 25_LooseEnds30 line 13 - QT2928 Gyrodrillmatic Excavationators (band L30)

- Shilly Mitts (9609) - Hands Cloth +6 Spi +5 SP; central 25.0 / conservative 14.0; usable
- Operator's Gloves (270045) - Hands Leather +6 Str +4 Sta +4 Spi; central 22.0 / conservative 18.0; usable
- Shoni's Disarming Tool (9608) - Off Hand Axe 16.6 dps +4 Spi; central 10.0 / conservative 6.0; not usable - off-hand/ranged (2H build)
- Guide pick: Operator's Gloves (line 14)
- Suggested pick: Shilly Mitts
- Why flagged: central best Shilly Mitts beats the pick by 3.0; conservative best Operator's Gloves differs from central best Shilly Mitts

### 25_LooseEnds30 line 34 - QT55 Morbent Fel (band L30)

- Sparkmetal Coif (1282) - Head Mail +9 Str +8 Spi; central 38.0 / conservative 30.0; not usable - mail (40+)
- Night Watch Pantaloons (2954) - Legs Cloth +9 Sta +8 Int; central 9.1 / conservative 9.1; usable
- Watch Master's Cloak (2953) - Back  +7 Sta; central 0.0 / conservative 0.0; usable
- Guide pick: Watch Master's Cloak (line 35)
- Suggested pick: Night Watch Pantaloons
- Why flagged: central best Night Watch Pantaloons beats the pick by 9.1

### 26_RazorfenKraul line 87 - QT1142 Mortality Wanes (band L30)

- Sentinel's Boots (270047) - Feet Mail +4 Str +4 Sta +6 Spi; central 23.0 / conservative 17.0; not usable - mail (40+)
- Lancer Boots (6752) - Feet Leather +5 Agi +6 Sta +4 Spi; central 14.8 / conservative 10.8; usable
- Mourning Shawl (6751) - Back  +8 Sta; central 0.0 / conservative 0.0; usable
- Guide pick: unstated
- Suggested pick: Lancer Boots
- Why flagged: guide names no pick (unstated) but Lancer Boots scores 14.8

### 30_StranglethornNorth line 13 - QT92489 Power Overwhelming (band L30)

- Violet Sash (251962) - Waist Cloth +9 Int +6 SP; central 22.3 / conservative 16.3; usable
- Runebound Gloves (279849) - Hands Leather +7 Sta +4 Spi +12 AP; central 22.0 / conservative 18.0; usable
- Guide pick: none (line 14)
- Suggested pick: Violet Sash
- Why flagged: guide names no pick (none) but Violet Sash scores 22.3; conservative best Runebound Gloves differs from central best Violet Sash

### 30_StranglethornNorth line 15 - QT92456 A Green Sample (band L30)

- Thorn Protecting Girdle (279836) - Waist Mail +8 Sta +21 AP; central 21.0 / conservative 21.0; not usable - mail (40+)
- Vine Pruner's Cloak (279835) - Back  +6 Sta +5 SP; central 10.0 / conservative 5.0; usable
- Guide pick: unstated
- Suggested pick: Vine Pruner's Cloak
- Why flagged: guide names no pick (unstated) but Vine Pruner's Cloak scores 10.0

### 30_StranglethornNorth line 44 - QT204 Bad Medicine (band L30)

- Guerrilla Cleaver (4126) - Main Hand Axe 17.7 dps +3 Agi +4 Sta; central 250.4 / conservative 250.4; usable - 1H (shield set only)
- Palm Frond Mantle (4140) - Shoulder Cloth +7 Int +6 Spi; central 23.0 / conservative 17.0; usable
- Guide pick: unstated
- Suggested pick: Palm Frond Mantle
- Why flagged: guide names no pick (unstated) but Palm Frond Mantle scores 23.0

### 30_StranglethornNorth line 53 - QT331 Report to Doren (band L30)

- Junglewalker Sandals (4139) - Feet Cloth +8 Sta +5 Int +2 Spi; central 10.7 / conservative 8.7; usable
- Frost Metal Pauldrons (4123) - Shoulder Mail +11 Sta; central 0.0 / conservative 0.0; not usable - mail (40+)
- Guide pick: unstated
- Suggested pick: Junglewalker Sandals
- Why flagged: guide names no pick (unstated) but Junglewalker Sandals scores 10.7

### 30_StranglethornNorth line 60 - QT202 Colonel Kurzen (band L30)

- Dark Hearted Hammer (270071) - Two-Hand Mace 28.9 dps +12 Str +8 Sta; central 429.3 / conservative 429.3; usable
- Madman's Blade (270070) - Main Hand Dagger 14.7 dps +7 Spi +32 SP; central 287.9 / conservative 248.9; usable - 1H (shield set only)
- Shrapnel Blaster (4127) - Ranged Gun 17.4 dps +4 Agi +3 Int; central 7.3 / conservative 7.3; not usable - gun (shaman can't use)
- Guide pick: none (line 64)
- Suggested pick: Dark Hearted Hammer
- Why flagged: guide names no pick (none) but Dark Hearted Hammer scores 429.3

### 33_Desolace line 48 - QT6027 Book of the Ancients (band L40)

- Silkstream Cuffs (16791) - Wrist Cloth +4 Sta +5 Int +4 Spi; central 15.9 / conservative 11.9; usable
- Arcmetal Shoulders (16793) - Shoulder Mail +9 Agi +5 Sta; central 10.2 / conservative 10.2; usable
- Guide pick: none (line 52)
- Suggested pick: Silkstream Cuffs
- Why flagged: guide names no pick (none) but Silkstream Cuffs scores 15.9

### 33_Desolace line 53 - QT1440 Return to Vahlarriel (band L40)

- Grappler's Belt (9687) - Waist Leather +7 Str +5 Sta; central 14.0 / conservative 14.0; usable
- Gloves of Insight (9698) - Hands Leather +7 Sta +7 SP; central 14.0 / conservative 7.0; usable
- Moonlit Amice (11884) - Shoulder Cloth +7 Sta +7 SP; central 14.0 / conservative 7.0; usable
- Garrison Cloak (9699) - Back  +3 Agi +6 Sta; central 3.4 / conservative 3.4; usable
- Guide pick: unstated
- Suggested pick: Grappler's Belt
- Why flagged: guide names no pick (unstated) but Grappler's Belt scores 14.0

### 33_Desolace line 74 - QT5561 Kodo Roundup (band L40)

- Kodo Rustler Boots (15697) - Feet Cloth +3 Sta +8 Int +5 Spi; central 22.0 / conservative 17.0; usable
- Wrangling Spaulders (15698) - Shoulder Mail +8 Str +2 Agi +6 Sta; central 18.3 / conservative 18.3; usable
- Guide pick: unstated
- Suggested pick: Kodo Rustler Boots
- Why flagged: guide names no pick (unstated) but Kodo Rustler Boots scores 22.0; conservative best Wrangling Spaulders differs from central best Kodo Rustler Boots

### 33_Desolace line 87 - QT6134 Ghost-o-plasm Round Up (band L40)

- Anchorhold Buckler (15865) - Off Hand Shield +6 Int +5 SP; central 17.1 / conservative 12.1; not usable - off-hand/ranged (2H build)
- Condor Bracers (15864) - Wrist Cloth +6 Sta +7 SP; central 14.0 / conservative 7.0; usable
- Guide pick: none (line 89)
- Suggested pick: Condor Bracers
- Why flagged: guide names no pick (none) but Condor Bracers scores 14.0

### 35_Badlands line 40 - QT704 Agmond's Fate (band L40)

- Excavator Gauntlets (270060) - Hands Mail +8 Str +8 Spi; central 36.0 / conservative 28.0; usable
- Restorer's Fine Gloves (270059) - Hands Cloth +6 Sta +8 Spi +4 SP; central 28.0 / conservative 16.0; usable
- Prospector Gloves (4980) - Hands Leather +8 Int +9 SP; central 27.5 / conservative 18.5; usable
- Guide pick: unstated
- Suggested pick: Excavator Gauntlets
- Why flagged: guide names no pick (unstated) but Excavator Gauntlets scores 36.0

### 38_RivergladesI line 26 - QT94861 Helping Hands (band L40)

- Hurley's Felling Axe (274929) - Two-Hand Axe 27.7 dps +7 Str; central 402.2 / conservative 402.2; usable
- Curly's Chopper (274928) - One-Hand Axe 21.5 dps +6 Sta; central 301.0 / conservative 301.0; usable - 1H (shield set only)
- Guide pick: unstated
- Suggested pick: Hurley's Felling Axe
- Why flagged: guide names no pick (unstated) but Hurley's Felling Axe scores 402.2

### 38_RivergladesI line 63 - QT95615 In Memoriam (band L40)

- Verger Greaves (274916) - Feet Mail +7 Str +8 SP; central 30.0 / conservative 22.0; usable
- Sacristan Band (274915) - Finger  +7 Sta +2 SP; central 4.0 / conservative 2.0; usable
- Guide pick: unstated
- Suggested pick: Verger Greaves
- Why flagged: guide names no pick (unstated) but Verger Greaves scores 30.0

### 38_RivergladesI line 99 - QT95064 Preventative Measures (band L40)

- Farholde Horns (274959) - Head Mail +13 Sta +12 AP; central 12.0 / conservative 12.0; usable
- Brute Slayer Band (274961) - Finger  +6 Int; central 7.1 / conservative 7.1; usable
- Guide pick: unstated
- Suggested pick: Farholde Horns
- Why flagged: guide names no pick (unstated) but Farholde Horns scores 12.0

### 39c_Alterac line 65 - QT1053 In the Name of the Light (band L40)

- Bonebiter (6830) - Two-Hand Axe 38.8 dps +20 Str +10 Sta; central 583.5 / conservative 583.5; usable
- Sword of Serenity (6829) - One-Hand Sword 30.0 dps +9 Sta +4 Spi; central 430.0 / conservative 426.0; not usable - sword (shaman can't use)
- Black Menace (6831) - One-Hand Dagger 29.7 dps; central 415.4 / conservative 415.4; usable - 1H (shield set only)
- Orb of Lorica (11262) - Held In Off-hand  +10 Int +6 SP; central 23.9 / conservative 17.9; not usable - off-hand/ranged (2H build)
- Guide pick: unstated
- Suggested pick: Bonebiter
- Why flagged: guide names no pick (unstated) but Bonebiter scores 583.5

### 39d_Level40 line 12 - QT3636 Bring the Light (band L40)

- Amberglow Talisman (10824) - Neck  +1 Agi +7 Sta +10 Spi; central 26.1 / conservative 16.1; usable
- Purified Ring (270081) - Finger  +12 Int +5 SP; central 24.3 / conservative 19.3; usable
- Guide pick: Amberglow Talisman (line 13)
- Suggested pick: Amberglow Talisman
- Why flagged: conservative best Purified Ring differs from central best Amberglow Talisman

### 39e_Uldaman line 44 - QT709 Solution to Doom (band L40)

- Doomsayer's Robe (4746) - Chest Cloth +18 Spi +6 SP; central 57.0 / conservative 33.0; usable
- Doomcaller's Pants (270074) - Legs Leather +13 Str +9 Int; central 36.7 / conservative 36.7; usable
- Fists of Impending Doom (270075) - Hands Mail +7 Int +20 AP; central 28.3 / conservative 28.3; usable
- Guide pick: unstated
- Suggested pick: Doomsayer's Robe
- Why flagged: guide names no pick (unstated) but Doomsayer's Robe scores 57.0; conservative best Doomcaller's Pants differs from central best Doomsayer's Robe

### 39e_Uldaman line 46 - QT704 Agmond's Fate (band L40)

- Excavator Gauntlets (270060) - Hands Mail +8 Str +8 Spi; central 36.0 / conservative 28.0; usable
- Restorer's Fine Gloves (270059) - Hands Cloth +6 Sta +8 Spi +4 SP; central 28.0 / conservative 16.0; usable
- Prospector Gloves (4980) - Hands Leather +8 Int +9 SP; central 27.5 / conservative 18.5; usable
- Guide pick: unstated
- Suggested pick: Excavator Gauntlets
- Why flagged: guide names no pick (unstated) but Excavator Gauntlets scores 36.0

### 39e_Uldaman line 54 - QT2240 The Hidden Chamber (band L40)

- Dwarven Charge (9626) - Two-Hand Axe 31.2 dps +12 Str +11 Sta; central 460.9 / conservative 460.9; usable
- Guardian Staff (270078) - Two-Hand Staff 31.2 dps +11 Agi +11 Sta; central 449.9 / conservative 449.9; usable
- Explorer's League Lodestar (9627) - Held In Off-hand  +7 Sta +5 SP; central 10.0 / conservative 5.0; not usable - off-hand/ranged (2H build)
- Guide pick: unstated
- Suggested pick: Dwarven Charge
- Why flagged: guide names no pick (unstated) but Dwarven Charge scores 460.9

### 40_RivergladesII line 29 - QT94927 Dunston Checks Out (band L40)

- Dunston's Ogre Duster (275025) - One-Hand Mace 29.8 dps +10 Str +4 Sta; central 437.3 / conservative 437.3; usable - 1H (shield set only)
- Prisoner Handwraps (275021) - Hands Cloth +12 Spi +15 SP; central 60.0 / conservative 33.0; usable
- Bolder'ok Loincloth (275023) - Legs Cloth +13 Spi +9 SP; central 50.5 / conservative 28.5; usable
- Guide pick: unstated
- Suggested pick: Prisoner Handwraps
- Why flagged: guide names no pick (unstated) but Prisoner Handwraps scores 60.0

### 43_KroldokStronghold line 52 - QT94984 Tome of Twilight (band L40)

- Twilight Initiate's Belt (279854) - Waist Leather +11 Agi +7 Spi; central 29.9 / conservative 22.9; usable
- Torn Cultist Cloak (279855) - Back  +7 Int; central 8.3 / conservative 8.3; usable
- Guide pick: unstated
- Suggested pick: Twilight Initiate's Belt
- Why flagged: guide names no pick (unstated) but Twilight Initiate's Belt scores 29.9

### 43_KroldokStronghold line 58 - QT94982 Eye of Mugg (band L40)

- Bigger Rock on Bigger Stick (279480) - Two-Hand Mace 41.2 dps +14 Str; central 604.5 / conservative 604.5; usable
- Stick No Rock (279853) - Two-Hand Staff 30.4 dps +10 Str +18 Spi +33 SP; central 557.3 / conservative 506.3; usable
- Rock on Stick (279852) - One-Hand Mace 31.5 dps +4 Str; central 449.6 / conservative 449.6; usable - 1H (shield set only)
- Guide pick: unstated
- Suggested pick: Bigger Rock on Bigger Stick
- Why flagged: guide names no pick (unstated) but Bigger Rock on Bigger Stick scores 604.5

### 46_TanarisI line 64 - QT8366 Southsea Shakedown (band L40)

- Southsea Mojo Boots (20641) - Feet Cloth +11 Int +8 SP; central 29.1 / conservative 21.1; usable
- Southsea Head Bucket (20640) - Head Plate +6 Str +15 Sta; central 12.0 / conservative 12.0; not usable - plate (shaman can't wear)
- Guide pick: unstated
- Suggested pick: Southsea Mojo Boots
- Why flagged: guide names no pick (unstated) but Southsea Mojo Boots scores 29.1

### 48_Hinterlands line 20 - QT97332 Twice Misplaced Trust (band L40)

- Apology Ring (278019) - Finger  +6 Sta +4 SP; central 8.0 / conservative 4.0; usable
- Renegotiated Ring (278018) - Finger  +3 Str +6 Sta; central 6.0 / conservative 6.0; usable
- Refunded Ring (278017) - Finger  +8 Sta; central 0.0 / conservative 0.0; usable
- Guide pick: Apology Ring (line 21)
- Suggested pick: Apology Ring
- Why flagged: conservative best Renegotiated Ring differs from central best Apology Ring

### 49_StranglethornCape line 28 - QT836 Rescue OOX-09/HL! (band L40)

- Gnomish Inventor Boots (9645) - Feet Cloth +7 Sta +2 Int +11 Spi; central 29.9 / conservative 18.9; usable
- Gnomish Floatation Device (270101) - Feet Leather +10 Str +10 Sta; central 20.0 / conservative 20.0; usable
- Gnomish Water Sinking Device (9646) - Feet Plate +16 Sta; central 0.0 / conservative 0.0; not usable - plate (shaman can't wear)
- Guide pick: Gnomish Water Sinking Device (line 30)
- Suggested pick: Gnomish Inventor Boots
- Why flagged: central best Gnomish Inventor Boots beats the pick by 29.9; conservative best Gnomish Floatation Device differs from central best Gnomish Inventor Boots

### 51_ZulFarrak line 59 - QT2768 Divino-matic Rod (band L40)

- Engineer's Guild Headpiece (9534) - Head Leather +22 Spi +10 SP; central 75.0 / conservative 43.0; usable
- Magister Cowl (270099) - Head Cloth +18 SP; central 36.0 / conservative 18.0; usable
- Masons Fraternity Ring (9533) - Finger  +14 Agi +5 Sta; central 15.8 / conservative 15.8; usable
- Guide pick: unstated
- Suggested pick: Engineer's Guild Headpiece
- Why flagged: guide names no pick (unstated) but Engineer's Guild Headpiece scores 75.0

### 52_SearingGorge line 19 - QT2846 Tiara of the Deep (band L40)

- Gemshale Pauldrons (9531) - Shoulder Plate +5 Str +10 Sta +8 Int; central 19.5 / conservative 19.5; not usable - plate (shaman can't wear)
- Dank Shoulderpads (270098) - Shoulder Leather +4 Agi +13 Sta; central 4.5 / conservative 4.5; usable
- Guide pick: Gemshale Pauldrons (line 20)
- Suggested pick: Dank Shoulderpads
- Why flagged: central best Dank Shoulderpads beats the pick by 4.5

### 53_TanarisII line 45 - QT1560 Tooga's Quest (band L40)

- Chelonian Cuffs (9638) - Wrist Mail +4 Sta +10 Int; central 11.9 / conservative 11.9; usable
- Band of the Great Tortoise (9642) - Finger  no stats; central 0.0 / conservative 0.0; usable
- Guide pick: none (line 46)
- Suggested pick: Chelonian Cuffs
- Why flagged: guide names no pick (none) but Chelonian Cuffs scores 11.9

### 53_TanarisII line 53 - QT5863 The Dunemaul Compound (band L40)

- Witherseed Gloves (16738) - Hands Cloth +13 Spi +8 SP; central 48.5 / conservative 27.5; usable
- Rugwood Mantle (16739) - Shoulder Leather +11 Int +4 Spi +7 SP; central 37.1 / conservative 26.1; usable
- Guide pick: Rugwood Mantle (line 54)
- Suggested pick: Witherseed Gloves
- Why flagged: central best Witherseed Gloves beats the pick by 11.4

### 53_TanarisII line 58 - QT3161 Gahz'ridian (band L40)

- Staff of Lore (10826) - Two-Hand Staff 27.6 dps +5 Int +18 Spi +40 SP; central 517.1 / conservative 459.1; usable
- Surveyor's Tunic (10827) - Chest Leather +11 Str +15 Spi; central 59.5 / conservative 44.5; usable
- Guide pick: Surveyor's Tunic (line 59)
- Suggested pick: Staff of Lore
- Why flagged: central best Staff of Lore beats the pick by 457.6

### 54_Maraudon line 73 - QT7028 Twisted Evils (band L40)

- Acumen Robes (17775) - Chest Cloth +15 Int +14 SP; central 45.8 / conservative 31.8; usable
- Relentless Chain (17777) - Chest Mail +11 Sta +11 Int +20 AP; central 33.1 / conservative 33.1; usable
- Sprightring Helm (17776) - Head Leather +11 Agi +16 Sta; central 12.4 / conservative 12.4; usable
- Hulkstone Pauldrons (17779) - Shoulder Plate +13 Sta; central 0.0 / conservative 0.0; not usable - plate (shaman can't wear)
- Guide pick: unstated
- Suggested pick: Acumen Robes
- Why flagged: guide names no pick (unstated) but Acumen Robes scores 45.8; conservative best Relentless Chain differs from central best Acumen Robes

### 54_Maraudon line 75 - QT7041 Vyletongue Corruption (band L40)

- Woodseed Hoop (17768) - Finger  +10 Int +6 SP; central 23.9 / conservative 17.9; usable
- Sagebrush Girdle (17778) - Waist Leather +11 Agi +9 Int; central 23.1 / conservative 23.1; usable
- Branchclaw Gauntlets (17770) - Hands Plate +9 Str +5 Sta; central 18.0 / conservative 18.0; not usable - plate (shaman can't wear)
- Guide pick: none (line 76)
- Suggested pick: Woodseed Hoop
- Why flagged: guide names no pick (none) but Woodseed Hoop scores 23.9; conservative best Sagebrush Girdle differs from central best Woodseed Hoop

### 54_Maraudon line 77 - QT7065 Corruption of Earth and Seed (band L40)

- Resurgence Rod (17743) - Two-Hand Staff 34.1 dps +37 SP; central 551.1 / conservative 514.1; usable
- Thrash Blade (17705) - One-Hand Sword 35.2 dps; central 492.7 / conservative 492.7; not usable - sword (shaman can't use)
- Verdant Keeper's Aim (17753) - Ranged Bow 27.3 dps; central 0.0 / conservative 0.0; not usable - bow (shaman can't use)
- Guide pick: unstated
- Suggested pick: Resurgence Rod
- Why flagged: guide names no pick (unstated) but Resurgence Rod scores 551.1

### 56_UnGoro line 76 - QT3882 Roll the Bones (band L40)

- Archaeologist's Quarry Boots (11908) - Feet Cloth +9 Agi +10 Sta +9 Int; central 20.9 / conservative 20.9; usable
- Excavator's Utility Belt (11909) - Waist Leather +4 Sta +16 Int; central 19.0 / conservative 19.0; usable
- Guide pick: Excavator's Utility Belt (line 77)
- Suggested pick: Archaeologist's Quarry Boots
- Why flagged: central best Archaeologist's Quarry Boots beats the pick by 1.8

### 56_UnGoro line 87 - QT87494 Microcrystal Contamination (band L40)

- Crystal-flecked Waistguard (281262) - Waist Mail +6 Str +15 Int; central 29.8 / conservative 29.8; usable
- Crystal-flecked Cord (281261) - Waist Leather +9 Sta +14 Int; central 16.7 / conservative 16.7; usable
- Guide pick: unstated
- Suggested pick: Crystal-flecked Waistguard
- Why flagged: guide names no pick (unstated) but Crystal-flecked Waistguard scores 29.8

### 56_UnGoro line 90 - QT4491 A Little Help From My Friends (band L40)

- Clayridge Helm (11913) - Head Mail +16 Agi +15 Spi; central 55.6 / conservative 40.6; usable
- Treetop Leggings (11911) - Legs Cloth +8 Sta +8 Int +18 Spi; central 54.5 / conservative 36.5; usable
- Yesterday's Pants (270122) - Legs Leather +14 Str +12 Sta +9 Spi; central 50.5 / conservative 41.5; usable
- Bejeweled Legguards (11910) - Legs Plate +15 Sta +8 Spi; central 20.0 / conservative 12.0; not usable - plate (shaman can't wear)
- Guide pick: Treetop Leggings (line 91)
- Suggested pick: Clayridge Helm
- Why flagged: central best Clayridge Helm beats the pick by 1.1; conservative best Yesterday's Pants differs from central best Clayridge Helm

### 57_Ironforge line 11 - QT7070 Shadowshard Fragments (band L40)

- Prodigious Shadowshard Pendant (17773) - Neck  +9 SP; central 18.0 / conservative 9.0; usable
- Zealous Shadowshard Pendant (17772) - Neck  +14 AP; central 14.0 / conservative 14.0; usable
- Guide pick: none (line 13)
- Suggested pick: Prodigious Shadowshard Pendant
- Why flagged: guide names no pick (none) but Prodigious Shadowshard Pendant scores 18.0; conservative best Zealous Shadowshard Pendant differs from central best Prodigious Shadowshard Pendant

## Part 3 - items with no tooltip

Reward-choice item ids (all [QT] quests with 2+ choices) and weapon/armor names on gear lines that the cache lacks. Fetch with: python tooling\fetch_tooltips.py --from-file <file with these ids>

```
4239 4566 9469 9474 9477 9479 9481 10761 10766 10767 10768 10775 17714 17715 17730 17732 17736 17740 17748 17751 17754 17755 23177 249410 249427 252435 252446 270042 279851 279882 279883 279884 279929 279930
```

Gear-line names without a tooltip (name - item.json ids - first line):

- Boar Champion's Belt - 10768 - 39b_RazorfenDowns:31
- Bracers of the Stone Princess - 17714 - 54_Maraudon:65
- Brusslehide Leggings - 17751 - 54_Maraudon:52
- Carapace of Tuten'kash - 10775 - 39b_RazorfenDowns:32
- Coldrage Dagger - 10761 - 39b_RazorfenDowns:32
- Embossed Leather Gloves - 4239 - 02_LochModan:59
- Embrace of the Lycan - 9479 - 51_ZulFarrak:46
- Eye of Theradras - 17715 - 54_Maraudon:65
- Gahz'rilla Scale Armor - 9469 - 51_ZulFarrak:46
- Gatorbite Axe - 17730 - 54_Maraudon:61
- Infernal Trickster Leggings - 17754 - 54_Maraudon:48
- Jinxed Hoodoo Kilt - 9474 - 51_ZulFarrak:46
- Lady Falther'ess' Finger - 23177 - 39b_RazorfenDowns:32
- Mutinous Cuffs - 279883 - 31_BootyBayDrownedCity:64
- Plaguerot Sprig - 10766 - 39b_RazorfenDowns:32
- Pristine Leather - 249427 - 07_Deadmines:8
- Rockgrip Gauntlets - 17736 - 54_Maraudon:62
- Rotgrip Mantle - 17732 - 54_Maraudon:61
- Rusted Troll War Belt - 279882 - 31_BootyBayDrownedCity:66
- Saltseer's Helm - 279930 - 31_BootyBayDrownedCity:66
- Satyrmane Sash - 17755 - 54_Maraudon:48
- Savage Boar's Guard - 10767 - 39b_RazorfenDowns:32
- Soothsayer's Headdress - 17740 - 54_Maraudon:60
- South Seas Shroud - 279884 - 31_BootyBayDrownedCity:64
- Sturdy Quarterstaff - 4566 - 01b_DunMorogh:153
- Sulfuric Acid - 249410 - 07_Deadmines:8
- Technician's Bracers - 270042 - 31_BootyBayDrownedCity:16
- The Chief's Enforcer - 9477 - 51_ZulFarrak:45
- The Minotaur - 9481 - 51_ZulFarrak:45
- Totemic Leather Armor - 252435 - 02_LochModan:59
- Totemic Leather Pants - 252446 - 19_Wetlands2:48
- Vinerot Sandals - 17748 - 54_Maraudon:52

