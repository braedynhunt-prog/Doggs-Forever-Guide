# Gear-call check - 2026-11-01

Report only (tooling/gear_calls.py). Dwarf chain of the guide (Hunter and Human lines skipped). Quoted stats on gear lines compared with today's Forever tooltips; quest-reward picks scored with weights/score_items.py (AP-equivalent; band nearest the chapter's starting level; no mace term).

- Tooltips (newest file wins per item): weights/tooltips/2026-11-01.json dated 2026-11-01 - 503 items taken; weights/tooltips/2026-10-29.json dated 2026-10-29 - 0 items taken; weights/item_tooltips.json dated 2026-09-24 (sources.json fallback_date) - 0 items taken
- Weights: level-20 central wdps=14 str=2 ap=1 int=1.05 agi=0.85 spi=1 sta=0 sp=1.5 exp=3; conservative Spi 0.5 SP 0.5 Exp 1.0; no mace term (spec removed 17 Oct 2026); other bands take Int/Agi from enh_weights: L10 int=0.38 agi=0.52; L15 int=1.03 agi=0.62; L25 int=1.1 agi=0.75; L30 int=1.09 agi=0.84
- Reward choices: data/zone_*.json "itemchoices" (Wowhead Forever atlas, as qinfo.py); item names: tooling/qdb/item.json; gear classes: tooling/client/1.60.1.70707/Item.csv
- Counts: gear lines scanned 277; item names matched 424; stat mismatches 16; quests checked (2+ choices) 105; quests flagged 33

## Part 1 - quoted stats that differ from the tooltip

| chapter | line | item | quoted | tooltip | differs | quoted text |
|---|---|---|---|---|---|---|
| 03_HallOfThanes | 38 | Spiritwraith Drape | +4 Agi +3 Spi | +3 Agi +4 Spi | Agi, Spi | back +4 Agi +3 Spi |
| 03_HallOfThanes | 38 | Ephemeral Choker | +4 Sta +2 Spi | +5 Spi | Sta, Spi | neck +4 Sta +2 Spi |
| 03_HallOfThanes | 40 | Deepgrave Trousers | +7 Str +3 Agi +3 Spi | +3 Agi +3 Spi | Str | leather legs +7 Str +3 Agi +3 Spi |
| 03_HallOfThanes | 47 | Flamefist Grips | +2 Str +4 Agi +4 Spi | +5 Agi +5 Spi | Str, Agi, Spi | leather hands +2 Str +4 Agi +4 Spi |
| 03_HallOfThanes | 57 | Durgen's Crescent Axe | 12.3 dps +2 Str | 12.3 dps +4 Str | Str | 1H axe 12.3 dps +2 Str |
| 03_HallOfThanes | 64 | Tomb Robber's Gloves | +3 Sta +6 Int | +1 Sta +2 Int | Sta, Int | +3 Sta +6 Int |
| 03_HallOfThanes | 67 | Dusty Belt | +5 Agi +4 Spi | +2 Agi +2 Spi | Agi, Spi | leather waist +5 Agi +4 Spi |
| 03_HallOfThanes | 69 | Ironforge Greathammer | 16 dps +4 Str +7 Sta | 16.0 dps | Str, Sta | 2H mace 16.0 dps +4 Str +7 Sta, no level requirement |
| 05_Westfall | 94 | Spiritwraith Drape | +2 Str +2 Spi | +3 Agi +4 Spi | Str, Spi | cloth +2 Str +2 Spi |
| 07_Deadmines | 84 | Rockslicer | 19.7 dps +10 Str | 19.7 dps +7 Str | Str | 2H axe 19.7 dps +10 Str, req 18 |
| 07_Deadmines | 88 | Miner's Cape | +5 Sta +4 AP | +5 Sta +10 AP | AP (tooltip AP includes conditional "Attack Power against X", which parse() adds in) | +5 Sta +4 AP |
| 07_Deadmines | 113 | Cookie's Tenderizer | 13.9 dps +4 Str | 13.9 dps +4 Spi | Str | 1H mace 13.9 dps +4 Str |
| 07_Deadmines | 139 | Bravo's Armbands | +2 Str +4 Agi +4 Spi | +3 Str +3 Agi | Str, Agi, Spi | leather wrist +2 Str +4 Agi +4 Spi |
| 18_Wetlands1 | 66 | Raptorbane Armor | +3 Sta +16 AP | +3 Sta +31 AP | AP (tooltip AP includes conditional "Attack Power against X", which parse() adds in) | leather chest, 92 armor, +3 Sta, +16 Attack Power, +15 more against beasts - AP feeds Enhancement |
| 22_ExcavationSite | 48 | Raptorbane Armor | +16 AP | +3 Sta +31 AP | AP (tooltip AP includes conditional "Attack Power against X", which parse() adds in) | +16 attack power |
| 26_RazorfenKraul | 58 | Hand Axe | 22.9 dps +5 Str +5 Spi | 1.5 dps | Str, Spi, wdps | 22.9 dps +5 Str +5 Spi, unique |

Parentheses with stat-like text that did not parse:

- 01a_ColdridgeValley:9 Strong Fishing Pole (+45 Fishing in Forever)
- 02_LochModan:74 Strong Fishing Pole (+45 Fishing in Forever, needs Fishing 10, level 5 - equip it when you fish)
- 04_LochModan2:46 Hunting Satchel (10 slot bag; hunters: the Hunting Ammo Sack is also +10% ranged speed, the same as the Small Shot Pouch you already own, so the bag is worth more)

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
- Craftsman's Dagger (2218) - One-Hand Dagger 6.8 dps +1 Agi; central 95.2 / conservative 95.2; usable - 1H (shield set only)
- Guide pick: none (line 191)
- Suggested pick: Compact Hammer
- Why flagged: guide names no pick (none) but Compact Hammer scores 97.4

### 03_HallOfThanes line 39 - QT96395 An Ancient Grudge (band L15)

- Catacomb Cloak (279899) - Back  +2 Sta +7 AP; central 7.0 / conservative 7.0; usable
- Deepgrave Trousers (279900) - Legs Leather +3 Agi +3 Spi; central 4.9 / conservative 3.4; usable
- Guide pick: Deepgrave Trousers (line 40)
- Suggested pick: Catacomb Cloak
- Why flagged: central best Catacomb Cloak beats the pick by 2.1

### 04_LochModan2 line 22 - QT297 Gathering Idols (band L15)

- Trogg Slicer (6186) - Two-Hand Sword 11.9 dps +5 Spi; central 171.7 / conservative 169.2; not usable - sword (shaman can't use)
- Thelsamar Axe (3154) - Main Hand Axe 9.1 dps +2 Agi; central 127.9 / conservative 127.9; usable - 1H (shield set only)
- Dwarven Flamestick (5241) - Ranged Wand 13.6 dps +2 Spi; central 2.0 / conservative 1.0; not usable - wand (shaman can't use)
- Guide pick: none (line 23)
- Suggested pick: Thelsamar Axe
- Why flagged: guide names no pick (none) but Thelsamar Axe scores 127.9

### 05_Westfall line 51 - QT9 The Killing Fields (band L15)

- Harvester's Robe (1561) - Chest Cloth +2 Spi +2 SP; central 5.0 / conservative 2.0; usable
- Harvester's Pants (3578) - Legs Leather +2 Agi +3 Spi; central 4.2 / conservative 2.7; usable
- Harvester's Pestslayer (276695) - Ranged Bow 6.0 dps +1 Agi +1 Sta; central 0.6 / conservative 0.6; not usable - bow (shaman can't use)
- Guide pick: Harvester's Pants (line 52)
- Suggested pick: Harvester's Robe
- Why flagged: conservative best Harvester's Pants differs from central best Harvester's Robe

### 05_Westfall line 93 - QT153 Red Leather Bandanas (band L15)

- Leggings of the People's Militia (12295) - Legs Cloth +2 Str +2 SP; central 7.0 / conservative 5.0; usable
- Cloak of the People's Militia (3511) - Back  +2 Agi; central 1.2 / conservative 1.2; usable
- Greaves of the People's Militia (5944) - Feet Mail +3 Sta; central 0.0 / conservative 0.0; not usable - mail (40+)
- Guide pick: Cloak of the People's Militia (line 94)
- Suggested pick: Leggings of the People's Militia
- Why flagged: central best Leggings of the People's Militia beats the pick by 5.8

### 07_Deadmines line 125 - QT14 The People's Militia (band L20)

- Edge of the People's Militia (1566) - Two-Hand Sword 11.2 dps +5 Sta; central 156.9 / conservative 156.9; not usable - sword (shaman can't use)
- Fist of the People's Militia (1480) - Main Hand Mace 8.4 dps +2 Str; central 122.2 / conservative 122.2; usable - 1H (shield set only)
- Boots of the People's Militia (270006) - Feet Leather +4 SP; central 6.0 / conservative 2.0; usable
- Spark of the People's Militia (12296) - Ranged Wand 12.8 dps +1 SP; central 1.5 / conservative 0.5; not usable - wand (shaman can't use)
- Guide pick: none (line 126)
- Suggested pick: Boots of the People's Militia
- Why flagged: guide names no pick (none) but Boots of the People's Militia scores 6.0

### 07_Deadmines line 125 - QT166 The Defias Brotherhood (band L20)

- Staff of Westfall (2042) - Two-Hand Staff 15.2 dps +5 Int +6 Spi +16 SP; central 247.6 / conservative 228.6; usable
- Chausses of Westfall (6087) - Legs Mail +11 Str +5 Sta; central 22.0 / conservative 22.0; not usable - mail (40+)
- Tunic of Westfall (2041) - Chest Leather +11 Agi +5 Sta; central 9.3 / conservative 9.3; usable
- Guide pick: none (line 126)
- Suggested pick: Staff of Westfall
- Why flagged: guide names no pick (none) but Staff of Westfall scores 247.6

### 07_Deadmines line 130 - QT214 Red Silk Bandanas (band L20)

- Piercing Axe (6094) - Two-Hand Axe 12.6 dps +6 Agi; central 181.2 / conservative 181.2; usable
- Scrimshaw Dagger (2089) - One-Hand Dagger 9.7 dps +2 Sta; central 136.1 / conservative 136.1; usable - 1H (shield set only)
- Solid Shortblade (2074) - One-Hand Sword 9.4 dps +1 Str +1 Sta; central 133.6 / conservative 133.6; not usable - sword (shaman can't use)
- Monastic Hammer (270005) - Main Hand Mace 6.4 dps +2 Int +12 SP; central 110.1 / conservative 98.1; usable - 1H (shield set only)
- Guide pick: none (line 131)
- Suggested pick: Piercing Axe
- Why flagged: guide names no pick (none) but Piercing Axe scores 181.2

### 07_Deadmines line 136 - QT167 Oh Brother... (band L20)

- Miner's Revenge (1893) - Two-Hand Axe 13.0 dps +6 Spi; central 188.0 / conservative 185.0; usable
- Miner's Workboots (270013) - Feet Leather +5 Spi; central 5.0 / conservative 2.5; usable
- Miner's Workgloves (270012) - Hands Cloth +5 Sta; central 0.0 / conservative 0.0; usable
- Guide pick: Miner's Workboots (line 137)
- Suggested pick: Miner's Revenge
- Why flagged: central best Miner's Revenge beats the pick by 183.0

### 07_Deadmines line 138 - QT2040 Underground Assault (band L20)

- Polar Gauntlets (7606) - Hands Mail +4 Str +2 Spi; central 10.0 / conservative 9.0; not usable - mail (40+)
- Dreamer's Leggings (270016) - Legs Leather +6 Int +2 SP; central 9.3 / conservative 7.3; usable
- Bravo's Armbands (270015) - Wrist Leather +3 Str +3 Agi; central 8.6 / conservative 8.6; usable
- Sable Wand (7607) - Ranged Wand 16.9 dps +2 Spi; central 2.0 / conservative 1.0; not usable - wand (shaman can't use)
- Guide pick: Bravo's Armbands (line 139)
- Suggested pick: Dreamer's Leggings
- Why flagged: conservative best Bravo's Armbands differs from central best Dreamer's Leggings

### 09_LochModanMenethil line 83 - QT286 Return the Statuette (band L20)

- Icicle Rod (2950) - Two-Hand Staff 12.5 dps +4 Int +18 SP; central 206.2 / conservative 188.2; usable
- Mariner Boots (2949) - Feet Leather +1 Agi +6 Sta; central 0.8 / conservative 0.8; usable
- Guide pick: Mariner Boots (line 83)
- Suggested pick: Icicle Rod
- Why flagged: central best Icicle Rod beats the pick by 205.3

### 11_Darkshore line 40 - QT4681 Washed Ashore (band L25)

- Dryweed Belt (15399) - Waist Leather +2 Int; central 2.2 / conservative 2.2; usable
- Sandcomber Boots (15398) - Feet Cloth no stats; central 0.0 / conservative 0.0; usable
- Clamshell Bracers (15400) - Wrist Mail no stats; central 0.0 / conservative 0.0; not usable - mail (40+)
- Guide pick: unstated
- Suggested pick: Dryweed Belt
- Why flagged: guide names no pick (unstated) but Dryweed Belt scores 2.2

### 11_Darkshore line 94 - QT1138 Fruit of the Sea (band L25)

- Shucking Gloves (15405) - Hands Leather +2 Sta +2 Int; central 2.2 / conservative 2.2; usable
- Crustacean Boots (15406) - Feet Mail +3 Sta; central 0.0 / conservative 0.0; not usable - mail (40+)
- Guide pick: unstated
- Suggested pick: Shucking Gloves
- Why flagged: guide names no pick (unstated) but Shucking Gloves scores 2.2

### 11_Darkshore line 112 - QT2139 Tharnariun's Hope (band L25)

- Evergreen Gloves (7738) - Hands Cloth +3 Int +2 Spi; central 5.3 / conservative 4.3; usable
- Timberland Cape (7739) - Back  +3 Spi; central 3.0 / conservative 1.5; usable
- Guide pick: Timberland Cape (line 113)
- Suggested pick: Evergreen Gloves
- Why flagged: central best Evergreen Gloves beats the pick by 2.3

### 11_Darkshore line 114 - QT982 Deep Ocean, Vast Sea (band L25)

- Noosegrip Gauntlets (15402) - Hands Mail +2 Str; central 4.0 / conservative 4.0; not usable - mail (40+)
- Welldrip Gloves (15401) - Hands Cloth +2 Int; central 2.2 / conservative 2.2; usable
- Murloc-hide Gloves (270004) - Hands Leather +2 Agi; central 1.5 / conservative 1.5; usable
- Guide pick: unstated
- Suggested pick: Welldrip Gloves
- Why flagged: guide names no pick (unstated) but Welldrip Gloves scores 2.2

### 12_Ashenvale line 72 - QT973 The Tower of Althalaxx (band L25)

- Staff of the Purifier (5613) - Two-Hand Staff 11.2 dps +8 Spi +16 SP; central 189.1 / conservative 169.1; usable
- Clergy Ring (5622) - Finger  +1 Sta +3 Spi; central 3.0 / conservative 1.5; usable
- Guide pick: Clergy Ring (line 73)
- Suggested pick: Staff of the Purifier
- Why flagged: central best Staff of the Purifier beats the pick by 186.1

### 14_Duskwood line 68 - QT181 Look to the Stars (band L25)

- Belt of the Stars (7107) - Waist Mail +6 Str +6 Sta; central 12.0 / conservative 12.0; not usable - mail (40+)
- Zodiac Gloves (7106) - Hands Cloth +4 Int +7 Spi; central 11.4 / conservative 7.9; usable
- Guide pick: unstated
- Suggested pick: Zodiac Gloves
- Why flagged: guide names no pick (unstated) but Zodiac Gloves scores 11.4

### 15_Stockade line 31 - QT98191 A Friend of the Family (band L25)

- Knight's Lance (281296) - Two-Hand Polearm 16.8 dps +7 Agi +5 Sta; central 240.7 / conservative 240.7; not usable - polearm (shaman can't use)
- Royal Dagger (281297) - Main Hand Dagger 8.5 dps +4 Int +18 SP; central 150.8 / conservative 132.8; usable - 1H (shield set only)
- Guide pick: Knight's Lance (line 31)
- Suggested pick: Royal Dagger
- Why flagged: central best Royal Dagger beats the pick by 150.8

### 16_RedridgeEastvale line 52 - QT19 Tharil'zun (band L25)

- Orc Crusher (6093) - Two-Hand Mace 18.2 dps +8 Str +4 Sta; central 270.7 / conservative 270.7; usable
- Fire Hardened Buckler (1276) - Off Hand Shield +5 Spi; central 5.0 / conservative 2.5; not usable - off-hand/ranged (2H build)
- Guide pick: unstated
- Suggested pick: Orc Crusher
- Why flagged: guide names no pick (unstated) but Orc Crusher scores 270.7

### 16_RedridgeEastvale line 55 - QT95999 WANTED: Incinerator Gar'im (band L25)

- Disjointed Shoes (277226) - Feet Leather +12 AP +5 SP; central 19.5 / conservative 14.5; usable
- Alacritous Treads (277234) - Feet Mail +5 Str +5 Agi; central 13.8 / conservative 13.8; not usable - mail (40+)
- Incinerator's Boots (277218) - Feet Cloth +3 Sta +6 Int; central 6.6 / conservative 6.6; usable
- Guide pick: unstated
- Suggested pick: Disjointed Shoes
- Why flagged: guide names no pick (unstated) but Disjointed Shoes scores 19.5

### 16_RedridgeEastvale line 67 - QT249 Morganth (band L25)

- Rose Mantle (5274) - Shoulder Cloth +5 Int +5 SP; central 13.0 / conservative 8.0; usable
- Shadow Gauntlets (270034) - Hands Mail +5 Str +4 Sta; central 10.0 / conservative 10.0; not usable - mail (40+)
- Demonhide Bracers (270033) - Wrist Leather +3 Str +4 Agi; central 9.0 / conservative 9.0; usable
- Guide pick: Rose Mantle (line 68)
- Suggested pick: Rose Mantle
- Why flagged: conservative best Demonhide Bracers differs from central best Rose Mantle

### 17_Duskwood2 line 16 - QT377 Crime and Punishment (band L25)

- Darkshire Mail Leggings (2906) - Legs Mail +7 Str +7 Spi; central 21.0 / conservative 17.5; not usable - mail (40+)
- Town Clerk's Mittens (270029) - Hands Cloth +7 Int +3 SP; central 12.2 / conservative 9.2; usable
- Ambassador's Boots (2033) - Feet Leather +3 Agi +5 Sta +4 Spi; central 6.2 / conservative 4.2; usable
- Guide pick: Ambassador's Boots (line 18)
- Suggested pick: Town Clerk's Mittens
- Why flagged: central best Town Clerk's Mittens beats the pick by 6.0

### 19_Wetlands2 line 90 - QT633 The Thandol Span (band L30)

- Swampland Trousers (4505) - Legs Cloth +11 Sta +4 Int; central 4.4 / conservative 4.4; usable
- Dwarven Guard Cloak (4504) - Back  +1 Agi +6 Sta; central 0.8 / conservative 0.8; usable
- Guide pick: Dwarven Guard Cloak (line 91)
- Suggested pick: Swampland Trousers
- Why flagged: central best Swampland Trousers beats the pick by 3.5

### 19_Wetlands2 line 110 - QT474 Defeat Nek'rosh (band L30)

- Ancient War Sword (3209) - Two-Hand Sword 21.7 dps +9 Str +6 Sta; central 321.4 / conservative 321.4; not usable - sword (shaman can't use)
- Barreling Reaper (6194) - Main Hand Axe 16.6 dps +5 Sta; central 232.1 / conservative 232.1; usable - 1H (shield set only)
- Guide pick: Ancient War Sword (line 112)
- Suggested pick: Barreling Reaper
- Why flagged: central best Barreling Reaper beats the pick by 232.1

### 20_Darnassus line 9 - QT1275 Researching the Corruption (band L30)

- Beetle Clasps (7003) - Wrist Mail +3 Sta +6 AP; central 6.0 / conservative 6.0; not usable - mail (40+)
- Prelacy Cape (7004) - Back  +3 Spi +2 SP; central 6.0 / conservative 2.5; usable
- Staghide Armguards (270021) - Wrist Leather +3 Agi +3 Sta; central 2.5 / conservative 2.5; usable
- Guide pick: Staghide Armguards (line 10)
- Suggested pick: Prelacy Cape
- Why flagged: central best Prelacy Cape beats the pick by 3.5; conservative best Staghide Armguards differs from central best Prelacy Cape

### 20_Darnassus line 24 - QT741 The Absent Minded Prospector (band L30)

- Relic Hunter Belt (11936) - Waist Cloth +2 Str +4 Int +2 Spi; central 10.4 / conservative 9.4; usable
- Windfelt Gloves (5630) - Hands Leather +3 Int +4 SP; central 9.3 / conservative 5.3; usable
- Hammerfist Gloves (5629) - Hands Leather +3 Str +3 Agi; central 8.5 / conservative 8.5; usable
- Guide pick: Hammerfist Gloves (line 25)
- Suggested pick: Relic Hunter Belt
- Why flagged: central best Relic Hunter Belt beats the pick by 1.8

### 21_AshenvaleEast line 86 - QT981 The Tower of Althalaxx (band L30)

- Seraph's Strike (5614) - Two-Hand Sword 21.1 dps +3 Str +10 Spi; central 311.3 / conservative 306.3; not usable - sword (shaman can't use)
- Pious Legwraps (10043) - Legs Cloth +8 Sta +7 Spi; central 7.0 / conservative 3.5; usable
- Guide pick: unstated
- Suggested pick: Pious Legwraps
- Why flagged: guide names no pick (unstated) but Pious Legwraps scores 7.0

### 22_ExcavationSite line 65 - QT943 The Absent Minded Prospector (band L30)

- Skullchipper (5626) - Two-Hand Axe 13.0 dps +6 Str +1 Sta; central 194.0 / conservative 194.0; usable
- Relic Blade (5627) - One-Hand Dagger 10.0 dps +3 Sta; central 140.0 / conservative 140.0; usable - 1H (shield set only)
- Archaeologist's Gown (270022) - Chest Cloth +5 Spi +2 SP; central 8.0 / conservative 3.5; usable
- Guide pick: unstated
- Suggested pick: Skullchipper
- Why flagged: guide names no pick (unstated) but Skullchipper scores 194.0

### 24_Gnomeregan line 23 - QT98824 Prehistoric Prism (band L30)

- Heavehammer (271766) - Two-Hand Mace 27.7 dps +32 AP; central 420.2 / conservative 420.2; usable
- Healer's Staff (271767) - Two-Hand Staff 20.8 dps +12 Sta +22 SP; central 323.8 / conservative 301.8; usable
- Explorer's League Dustcover (271716) - Back  +5 Agi +5 Int +5 Spi; central 14.7 / conservative 12.2; usable
- Guide pick: unstated
- Suggested pick: Heavehammer
- Why flagged: guide names no pick (unstated) but Heavehammer scores 420.2

### 24_Gnomeregan line 99 - QT2929 The Grand Betrayal (band L30)

- Civinad Robes (9623) - Chest Cloth +7 Sta +12 Spi +9 SP; central 25.5 / conservative 10.5; usable
- Dual Reinforced Leggings (9625) - Legs Mail +12 Str; central 24.0 / conservative 24.0; not usable - mail (40+)
- Triprunner Dungarees (9624) - Legs Leather +3 Str +18 Agi +6 Sta; central 21.1 / conservative 21.1; usable
- Guide pick: unstated
- Suggested pick: Civinad Robes
- Why flagged: guide names no pick (unstated) but Civinad Robes scores 25.5; conservative best Triprunner Dungarees differs from central best Civinad Robes

### 25_LooseEnds30 line 33 - QT55 Morbent Fel (band L30)

- Sparkmetal Coif (1282) - Head Mail +9 Str +8 Spi; central 26.0 / conservative 22.0; not usable - mail (40+)
- Night Watch Pantaloons (2954) - Legs Cloth +9 Sta +8 Int; central 8.7 / conservative 8.7; usable
- Watch Master's Cloak (2953) - Back  +7 Sta; central 0.0 / conservative 0.0; usable
- Guide pick: Watch Master's Cloak (line 34)
- Suggested pick: Night Watch Pantaloons
- Why flagged: central best Night Watch Pantaloons beats the pick by 8.7

### 26_RazorfenKraul line 86 - QT1142 Mortality Wanes (band L30)

- Lancer Boots (6752) - Feet Leather +5 Agi +6 Sta +4 Spi; central 8.2 / conservative 6.2; usable
- Mourning Shawl (6751) - Back  +8 Sta; central 0.0 / conservative 0.0; usable
- Guide pick: unstated
- Suggested pick: Lancer Boots
- Why flagged: guide names no pick (unstated) but Lancer Boots scores 8.2

## Part 3 - items with no tooltip

Reward-choice item ids (all [QT] quests with 2+ choices) and weapon/armor names on gear lines that the cache lacks. Fetch with: python tooling\fetch_tooltips.py --from-file <file with these ids>

```
(none)
```

