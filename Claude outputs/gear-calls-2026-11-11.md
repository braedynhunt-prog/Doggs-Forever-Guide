# Gear-call check - 2026-11-11

Report only (tooling/gear_calls.py). Dwarf chain of the guide (Hunter and Human lines skipped). Quoted stats on gear lines compared with today's Forever tooltips; quest-reward picks scored with weights/score_items.py (AP-equivalent; band nearest the chapter's starting level; no mace term).

- Tooltips (newest file wins per item): weights/tooltips/2026-11-11.json dated 2026-11-11 - 1144 items taken; weights/tooltips/2026-11-08.json dated 2026-11-08 - 0 items taken; weights/tooltips/2026-11-05.json dated 2026-11-05 - 0 items taken; weights/tooltips/2026-11-02.json dated 2026-11-02 - 0 items taken; weights/tooltips/2026-11-01.json dated 2026-11-01 - 0 items taken; weights/tooltips/2026-10-29.json dated 2026-10-29 - 0 items taken; weights/item_tooltips.json dated 2026-09-24 (sources.json fallback_date) - 0 items taken
- Weights: level-20 central wdps=14 str=2 ap=1 int=1.65 agi=0.8 spi=2.5 sta=0 sp=2 exp=3; conservative Spi 1.5 SP 1.0 Exp 1.0; no mace term (spec removed 17 Oct 2026); other bands take Int/Agi from enh_weights: L10 int=0.58 agi=0.47; L15 int=1.63 agi=0.58; L25 int=1.67 agi=0.8; L30 int=1.65 agi=0.95; L40 int=1.69 agi=1.12
- Reward choices: data/zone_*.json "itemchoices" (Wowhead Forever atlas, as qinfo.py); item names: tooling/qdb/item.json; gear classes: tooling/client/1.60.1.70888/Item.csv
- Counts: gear lines scanned 282; item names matched 482; stat mismatches 6; quests checked (2+ choices) 107; quests flagged 37

## Part 1 - quoted stats that differ from the tooltip

| chapter | line | item | quoted | tooltip | differs | quoted text |
|---|---|---|---|---|---|---|
| 03_HallOfThanes | 40 | Catacomb Cloak | +2 Sta +3 AP | +2 Sta +7 AP | AP (tooltip AP includes conditional "Attack Power against X", which parse() adds in) | +2 Sta +3 AP, +4 more against humanoids |
| 05_Westfall | 103 | Spiritwraith Drape | +2 Str +2 SP | +3 Agi +4 Spi | Str, SP | cloth +2 Str +2 spell damage |
| 07_Deadmines | 89 | Miner's Cape | +5 Sta +4 AP | +5 Sta +10 AP | AP (tooltip AP includes conditional "Attack Power against X", which parse() adds in) | +5 Sta +4 AP |
| 18_Wetlands1 | 66 | Raptorbane Armor | +3 Sta +16 AP | +3 Sta +31 AP | AP (tooltip AP includes conditional "Attack Power against X", which parse() adds in) | leather chest, 92 armor, +3 Sta, +16 Attack Power, +15 more against beasts - AP feeds Enhancement |
| 22_ExcavationSite | 48 | Raptorbane Armor | +16 AP | +3 Sta +31 AP | AP (tooltip AP includes conditional "Attack Power against X", which parse() adds in) | +16 attack power, +15 more against beasts |
| 26_RazorfenKraul | 59 | Hand Axe | 22.9 dps +5 Str +5 Spi | 1.5 dps | Str, Spi, wdps | 22.9 dps +5 Str +5 Spi, unique |

Parentheses with stat-like text that did not parse:

- 01a_ColdridgeValley:9 Strong Fishing Pole (+5 Fishing)
- 04_LochModan2:47 Hunting Satchel (10 slot bag; hunters: the Hunting Ammo Sack is also +10% ranged speed, the same as the Small Shot Pouch you already own, so the bag is worth more)

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
- Thelsamar Axe (3154) - Main Hand Axe 9.1 dps +2 Agi; central 127.9 / conservative 127.9; usable - 1H (shield set only)
- Dwarven Flamestick (5241) - Ranged Wand 13.6 dps +2 Spi; central 5.0 / conservative 3.0; not usable - wand (shaman can't use)
- Guide pick: none (line 24)
- Suggested pick: Thelsamar Axe
- Why flagged: guide names no pick (none) but Thelsamar Axe scores 127.9

### 04_LochModan2 line 50 - QT217 In Defense of the King's Lands (band L15)

- Lucky Trousers (1832) - Legs Cloth +2 Agi +2 Sta +3 Spi; central 8.7 / conservative 5.7; usable
- Frontier Britches (1436) - Legs Leather +3 Str +3 Agi; central 7.7 / conservative 7.7; usable
- Dwarven Defender (6187) - Off Hand Shield +3 Sta; central 0.0 / conservative 0.0; not usable - off-hand/ranged (2H build)
- Guide pick: Frontier Britches (line 51)
- Suggested pick: Lucky Trousers
- Why flagged: conservative best Frontier Britches differs from central best Lucky Trousers

### 05_Westfall line 51 - QT9 The Killing Fields (band L15)

- Harvester's Robe (1561) - Chest Cloth +2 Spi +2 SP; central 9.0 / conservative 5.0; usable
- Harvester's Pants (3578) - Legs Leather +2 Agi +3 Spi; central 8.7 / conservative 5.7; usable
- Harvester's Pestslayer (276695) - Ranged Bow 6.0 dps +1 Agi +1 Sta; central 0.6 / conservative 0.6; not usable - bow (shaman can't use)
- Guide pick: Harvester's Pants (line 52)
- Suggested pick: Harvester's Robe
- Why flagged: conservative best Harvester's Pants differs from central best Harvester's Robe

### 05_Westfall line 102 - QT153 Red Leather Bandanas (band L15)

- Leggings of the People's Militia (12295) - Legs Cloth +2 Str +2 SP; central 8.0 / conservative 6.0; usable
- Cloak of the People's Militia (3511) - Back  +2 Agi; central 1.2 / conservative 1.2; usable
- Greaves of the People's Militia (5944) - Feet Mail +3 Sta; central 0.0 / conservative 0.0; not usable - mail (40+)
- Guide pick: Cloak of the People's Militia (line 103)
- Suggested pick: Leggings of the People's Militia
- Why flagged: central best Leggings of the People's Militia beats the pick by 6.8

### 07_Deadmines line 127 - QT166 The Defias Brotherhood (band L20)

- Staff of Westfall (2042) - Two-Hand Staff 15.2 dps +5 Int +6 Spi +16 SP; central 267.6 / conservative 245.6; usable
- Chausses of Westfall (6087) - Legs Mail +11 Str +5 Sta; central 22.0 / conservative 22.0; not usable - mail (40+)
- Tunic of Westfall (2041) - Chest Leather +11 Agi +5 Sta; central 8.8 / conservative 8.8; usable
- Guide pick: none (line 128)
- Suggested pick: Staff of Westfall
- Why flagged: guide names no pick (none) but Staff of Westfall scores 267.6

### 07_Deadmines line 132 - QT214 Red Silk Bandanas (band L20)

- Piercing Axe (6094) - Two-Hand Axe 12.6 dps +6 Agi; central 180.9 / conservative 180.9; usable
- Scrimshaw Dagger (2089) - One-Hand Dagger 9.7 dps +2 Sta; central 136.1 / conservative 136.1; usable - 1H (shield set only)
- Solid Shortblade (2074) - One-Hand Sword 9.4 dps +1 Str +1 Sta; central 133.6 / conservative 133.6; not usable - sword (shaman can't use)
- Monastic Hammer (270005) - Main Hand Mace 6.4 dps +2 Int +12 SP; central 117.3 / conservative 105.3; usable - 1H (shield set only)
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

- Dreamer's Leggings (270016) - Legs Leather +6 Int +2 SP; central 13.9 / conservative 11.9; usable
- Polar Gauntlets (7606) - Hands Mail +4 Str +2 Spi; central 13.0 / conservative 11.0; not usable - mail (40+)
- Bravo's Armbands (270015) - Wrist Leather +3 Str +3 Agi; central 8.4 / conservative 8.4; usable
- Sable Wand (7607) - Ranged Wand 16.9 dps +2 Spi; central 5.0 / conservative 3.0; not usable - wand (shaman can't use)
- Guide pick: Bravo's Armbands (line 141)
- Suggested pick: Dreamer's Leggings
- Why flagged: central best Dreamer's Leggings beats the pick by 5.5

### 09_LochModanMenethil line 20 - QT217 In Defense of the King's Lands (band L20)

- Lucky Trousers (1832) - Legs Cloth +2 Agi +2 Sta +3 Spi; central 9.1 / conservative 6.1; usable
- Frontier Britches (1436) - Legs Leather +3 Str +3 Agi; central 8.4 / conservative 8.4; usable
- Dwarven Defender (6187) - Off Hand Shield +3 Sta; central 0.0 / conservative 0.0; not usable - off-hand/ranged (2H build)
- Guide pick: Frontier Britches (line 20)
- Suggested pick: Lucky Trousers
- Why flagged: conservative best Frontier Britches differs from central best Lucky Trousers

### 09_LochModanMenethil line 84 - QT286 Return the Statuette (band L20)

- Icicle Rod (2950) - Two-Hand Staff 12.5 dps +4 Int +18 SP; central 217.6 / conservative 199.6; usable
- Mariner Boots (2949) - Feet Leather +1 Agi +6 Sta; central 0.8 / conservative 0.8; usable
- Guide pick: Mariner Boots (line 84)
- Suggested pick: Icicle Rod
- Why flagged: central best Icicle Rod beats the pick by 216.8

### 11_Darkshore line 40 - QT4681 Washed Ashore (band L25)

- Dryweed Belt (15399) - Waist Leather +2 Int; central 3.3 / conservative 3.3; usable
- Sandcomber Boots (15398) - Feet Cloth no stats; central 0.0 / conservative 0.0; usable
- Clamshell Bracers (15400) - Wrist Mail no stats; central 0.0 / conservative 0.0; not usable - mail (40+)
- Guide pick: unstated
- Suggested pick: Dryweed Belt
- Why flagged: guide names no pick (unstated) but Dryweed Belt scores 3.3

### 11_Darkshore line 94 - QT1138 Fruit of the Sea (band L25)

- Shucking Gloves (15405) - Hands Leather +2 Sta +2 Int; central 3.3 / conservative 3.3; usable
- Crustacean Boots (15406) - Feet Mail +3 Sta; central 0.0 / conservative 0.0; not usable - mail (40+)
- Guide pick: unstated
- Suggested pick: Shucking Gloves
- Why flagged: guide names no pick (unstated) but Shucking Gloves scores 3.3

### 11_Darkshore line 113 - QT2139 Tharnariun's Hope (band L25)

- Evergreen Gloves (7738) - Hands Cloth +3 Int +2 Spi; central 10.0 / conservative 8.0; usable
- Timberland Cape (7739) - Back  +3 Spi; central 7.5 / conservative 4.5; usable
- Guide pick: Timberland Cape (line 114)
- Suggested pick: Evergreen Gloves
- Why flagged: central best Evergreen Gloves beats the pick by 2.5

### 11_Darkshore line 115 - QT982 Deep Ocean, Vast Sea (band L25)

- Noosegrip Gauntlets (15402) - Hands Mail +2 Str; central 4.0 / conservative 4.0; not usable - mail (40+)
- Welldrip Gloves (15401) - Hands Cloth +2 Int; central 3.3 / conservative 3.3; usable
- Murloc-hide Gloves (270004) - Hands Leather +2 Agi; central 1.6 / conservative 1.6; usable
- Guide pick: unstated
- Suggested pick: Welldrip Gloves
- Why flagged: guide names no pick (unstated) but Welldrip Gloves scores 3.3

### 12_Ashenvale line 72 - QT973 The Tower of Althalaxx (band L25)

- Staff of the Purifier (5613) - Two-Hand Staff 11.2 dps +8 Spi +16 SP; central 209.1 / conservative 185.1; usable
- Clergy Ring (5622) - Finger  +1 Sta +3 Spi; central 7.5 / conservative 4.5; usable
- Guide pick: Clergy Ring (line 73)
- Suggested pick: Staff of the Purifier
- Why flagged: central best Staff of the Purifier beats the pick by 201.6

### 14_Duskwood line 70 - QT181 Look to the Stars (band L25)

- Zodiac Gloves (7106) - Hands Cloth +4 Int +7 Spi; central 24.2 / conservative 17.2; usable
- Belt of the Stars (7107) - Waist Mail +6 Str +6 Sta; central 12.0 / conservative 12.0; not usable - mail (40+)
- Guide pick: unstated
- Suggested pick: Zodiac Gloves
- Why flagged: guide names no pick (unstated) but Zodiac Gloves scores 24.2

### 15_Stockade line 31 - QT98191 A Friend of the Family (band L25)

- Knight's Lance (281296) - Two-Hand Polearm 16.8 dps +7 Agi +5 Sta; central 241.1 / conservative 241.1; not usable - polearm (shaman can't use)
- Royal Dagger (281297) - Main Hand Dagger 8.5 dps +4 Int +18 SP; central 162.1 / conservative 144.1; usable - 1H (shield set only)
- Guide pick: Knight's Lance (line 31)
- Suggested pick: Royal Dagger
- Why flagged: central best Royal Dagger beats the pick by 162.1

### 16_RedridgeEastvale line 53 - QT19 Tharil'zun (band L25)

- Orc Crusher (6093) - Two-Hand Mace 18.2 dps +8 Str +4 Sta; central 270.7 / conservative 270.7; usable
- Fire Hardened Buckler (1276) - Off Hand Shield +5 Spi; central 12.5 / conservative 7.5; not usable - off-hand/ranged (2H build)
- Guide pick: unstated
- Suggested pick: Orc Crusher
- Why flagged: guide names no pick (unstated) but Orc Crusher scores 270.7

### 16_RedridgeEastvale line 56 - QT95999 WANTED: Incinerator Gar'im (band L25)

- Disjointed Shoes (277226) - Feet Leather +12 AP +5 SP; central 22.0 / conservative 17.0; usable
- Alacritous Treads (277234) - Feet Mail +5 Str +5 Agi; central 14.0 / conservative 14.0; not usable - mail (40+)
- Incinerator's Boots (277218) - Feet Cloth +3 Sta +6 Int; central 10.0 / conservative 10.0; usable
- Guide pick: unstated
- Suggested pick: Disjointed Shoes
- Why flagged: guide names no pick (unstated) but Disjointed Shoes scores 22.0

### 17_Duskwood2 line 22 - QT98 The Legend of Stalvan (band L25)

- Crescent of Forlorn Spirits (2044) - Main Hand Axe 18.1 dps +6 Spi; central 268.8 / conservative 262.8; usable - 1H (shield set only)
- Ring of Forlorn Spirits (2043) - Finger  +2 Sta +8 SP; central 16.0 / conservative 8.0; usable
- Ring of Ruin (270053) - Finger  +4 Str +6 Agi; central 12.8 / conservative 12.8; usable
- Guide pick: Ring of Forlorn Spirits (line 23)
- Suggested pick: Ring of Forlorn Spirits
- Why flagged: conservative best Ring of Ruin differs from central best Ring of Forlorn Spirits

### 19_Wetlands2 line 80 - QT304 A Grim Task (band L30)

- Tranquil Ring (2917) - Finger  +1 Int +7 Spi; central 19.1 / conservative 12.2; usable
- Fury Ring (270050) - Finger  +6 Str +2 Spi; central 17.0 / conservative 15.0; usable
- Gold Lion Shield (2916) - Off Hand Shield +2 Str +5 Sta +3 Spi; central 11.5 / conservative 8.5; not usable - off-hand/ranged (2H build)
- Guide pick: Fury Ring (line 81)
- Suggested pick: Tranquil Ring
- Why flagged: central best Tranquil Ring beats the pick by 2.1; conservative best Fury Ring differs from central best Tranquil Ring

### 19_Wetlands2 line 90 - QT633 The Thandol Span (band L30)

- Swampland Trousers (4505) - Legs Cloth +11 Sta +4 Int; central 6.6 / conservative 6.6; usable
- Dwarven Guard Cloak (4504) - Back  +1 Agi +6 Sta; central 0.9 / conservative 0.9; usable
- Guide pick: Dwarven Guard Cloak (line 91)
- Suggested pick: Swampland Trousers
- Why flagged: central best Swampland Trousers beats the pick by 5.6

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
- Staghide Armguards (270021) - Wrist Leather +3 Agi +3 Sta; central 2.8 / conservative 2.8; usable
- Guide pick: Staghide Armguards (line 10)
- Suggested pick: Prelacy Cape
- Why flagged: central best Prelacy Cape beats the pick by 8.7

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

- Relic Hunter Belt (11936) - Waist Cloth +2 Str +4 Int +2 Spi; central 15.6 / conservative 13.6; usable
- Windfelt Gloves (5630) - Hands Leather +3 Int +4 SP; central 12.9 / conservative 8.9; usable
- Hammerfist Gloves (5629) - Hands Leather +3 Str +3 Agi; central 8.8 / conservative 8.8; usable
- Guide pick: Windfelt Gloves (line 25)
- Suggested pick: Relic Hunter Belt
- Why flagged: central best Relic Hunter Belt beats the pick by 2.7

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
- Explorer's League Dustcover (271716) - Back  +5 Agi +5 Int +5 Spi; central 25.5 / conservative 20.5; usable
- Guide pick: unstated
- Suggested pick: Heavehammer
- Why flagged: guide names no pick (unstated) but Heavehammer scores 420.2

### 24_Gnomeregan line 101 - QT2929 The Grand Betrayal (band L30)

- Civinad Robes (9623) - Chest Cloth +7 Sta +12 Spi +9 SP; central 48.0 / conservative 27.0; usable
- Dual Reinforced Leggings (9625) - Legs Mail +12 Str; central 24.0 / conservative 24.0; not usable - mail (40+)
- Triprunner Dungarees (9624) - Legs Leather +3 Str +18 Agi +6 Sta; central 23.1 / conservative 23.1; usable
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
- Night Watch Pantaloons (2954) - Legs Cloth +9 Sta +8 Int; central 13.2 / conservative 13.2; usable
- Watch Master's Cloak (2953) - Back  +7 Sta; central 0.0 / conservative 0.0; usable
- Guide pick: Watch Master's Cloak (line 35)
- Suggested pick: Night Watch Pantaloons
- Why flagged: central best Night Watch Pantaloons beats the pick by 13.2

### 26_RazorfenKraul line 87 - QT1142 Mortality Wanes (band L30)

- Sentinel's Boots (270047) - Feet Mail +4 Str +4 Sta +6 Spi; central 23.0 / conservative 17.0; not usable - mail (40+)
- Lancer Boots (6752) - Feet Leather +5 Agi +6 Sta +4 Spi; central 14.8 / conservative 10.8; usable
- Mourning Shawl (6751) - Back  +8 Sta; central 0.0 / conservative 0.0; usable
- Guide pick: unstated
- Suggested pick: Lancer Boots
- Why flagged: guide names no pick (unstated) but Lancer Boots scores 14.8

## Part 3 - items with no tooltip

Reward-choice item ids (all [QT] quests with 2+ choices) and weapon/armor names on gear lines that the cache lacks. Fetch with: python tooling\fetch_tooltips.py --from-file <file with these ids>

```
4239 4566 249410 249427 252435 252446
```

Gear-line names without a tooltip (name - item.json ids - first line):

- Embossed Leather Gloves - 4239 - 02_LochModan:59
- Pristine Leather - 249427 - 07_Deadmines:8
- Sturdy Quarterstaff - 4566 - 01b_DunMorogh:153
- Sulfuric Acid - 249410 - 07_Deadmines:8
- Totemic Leather Armor - 252435 - 02_LochModan:59
- Totemic Leather Pants - 252446 - 19_Wetlands2:48

