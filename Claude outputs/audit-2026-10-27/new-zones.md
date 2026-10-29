# New Forever zones vs the 1-30 Alliance guide (audit, 27 Oct 2026)

**Short answer:** yes, apart from one zone. The guide visits every new Forever zone, dungeon and hub that an Alliance character can actually play between 1 and 30: Hall of Thanes, Ruins of Lordaeron, Excavation Site: Wetlands, Whelgar's dig site, the Redridge merchant camp, the camping hubs, Alba Fairmoon, Father Gavin, Steelgrill, Howin Kindfeather, and the rest. The one new outdoor zone in the 1-30 range that it skips is **Zephras Isle**. That is the Skyborne starting zone (levels 1-12). Sources disagree on whether a non-Skyborne character can get there at all, and for this route it would be grey content anyway. The **City of Dalaran** dungeon (28-33) is deliberately left for the 30-40 guide. On the route the guide passes, there are a few cheap new quests it doesn't take (section 4).

Method: QuestieDB Forever 1.0.6 (`tooling/qdb`) was cross-checked against the Wowhead zone listviews (`data/zone_*.json`, XP) and the Sep scrape (`data/quests.json`). A quest counts as "new" if its id is 86000 or higher, or Wowhead flags it `new`. A quest is "available" if a Human or Dwarf can take it (race mask 0 or `& 5`), it has no class restriction or is Shaman/Hunter, and it requires level 30 or lower. A quest is "in the guide" if the guide has a `[QA/QT/QC/QS<id>]` tag for it. Each quest is filed under the zone where its giver stands; instance quests are filed under their instance. All numbers were computed with Python (`python3 -I`). The scripts are in the scratchpad (`newzones/newq.py`, `table.py`).

## 1. Content new to Forever, Alliance 1-30

| Content | What it is | Faction | Levels | How you get there | Guide | Confidence / source |
|---|---|---|---|---|---|---|
| **Zephras Isle** (16593) | Skyborne starting zone: a flying island in Skywall. Hubs: Thendal Grove, Shen'dar Village, Falaath, Windfield/Gustberry Lowlands, Valanaar, Shadowgale Forest. 86 class-free story quests a Human/Dwarf could take (68 open to anyone, 18 High Order/Alliance-tagged), 21 Horde-only (Windshaper), 15 Skyborne-only. | Neutral sanctuary. Separate Alliance (High Order) and Horde (Windshaper) quest lines | 1-12 (quest levels 1-13) | Skyborne start there. Everyone else would need the skycutter from the Violet Citadel balcony in Dalaran (the chain's last quest, 94946, sends you to Denaaris Stargale at Alterac 12.3,56.3). **Whether a non-Skyborne can board is disputed**: allthings.how says "any character who can reach the dock can board"; gamer-guides and wowforevergame.wiki say it is part of the Skyborne Heroic Pack and other characters can't reach it; the Icy Veins headline says players "can experience Zephras Isle without playing Skyborne" (the page wouldn't fetch). | **Not covered** (0/88) | DB: high. Access: low, unresolved. [warcraft.wiki.gg](https://warcraft.wiki.gg/wiki/Zephras_Isle), [Blizzard](https://news.blizzard.com/en-us/article/24302071/wow), [allthings.how](https://allthings.how/world-of-warcraft-how-to-get-to-zephras-isle-via-the-dalaran-skycutter/), [gamer-guides](https://gamer-guides.com/warcraft-forever/zephras-isle-to-stormwind-orgrimmar/), [Icy Veins](https://www.icy-veins.com/wow-forever/news/wow-forever-players-can-experience-zephras-isle-without-playing-skyborne/) |
| **City of Dalaran**, the city itself (Alterac ~10-23, 52-72) | A new neutral city hub. The DB lists innkeepers, battlemasters (including Darkspear Islands), vendors, trainers, Kirin Tor Guards, a Skyborne Portal to Stormwind (12.0,56.2) and the skycutter dock. Quest givers: Belanaa Windveil, the High Order cloth quartermaster (A Donation of Wool, req 12; A Donation of Silk, req 26), Magus Olvek (Past Due, L38) | Alliance-friendly per the DB; neutral per the guides | Any level; city NPCs are 25-30 | Walk in from Hillsbrad (ch08 does this) or from Silverpine | **Passed through** in ch08 (`[G18,72 Alterac]`). No city quests are taken. Note: ch08 still describes the crater as "22-24 Kirin Tor mages, avoidable" (Classic wording); check this on live | DB: high. [warcraft.wiki.gg/Forever](https://warcraft.wiki.gg/wiki/Forever) |
| **City of Dalaran dungeon** (16544/16560) | New 5-man | Both. Alliance attunement starts with Emissary Jacques in Southshore | 28-33 (quests L33, req 24) | Image of Archmage Modera on the Silverpine shore, 68.6,45.2 | **Deferred on purpose.** Lead-ins 92456 and 92489 (ch15) and 92432 (ch23) are carried. 92457, 92458 and 92459 are not taken. The dungeon was closed all through the beta | [Warcraft Tavern](https://www.warcrafttavern.com/news/nine-new-dungeons-coming-to-world-of-warcraft-forever/), [finalboss](https://finalboss.io/world-of-warcraft-forever-dalaran-attunement-skyborne-1-12-guide), [kami-labs](https://kami-labs.fr/wow-forever/leveling-donjons-wow-forever/) |
| **Hall of Thanes** (16919) | New 5-man under Ironforge | Alliance-favoured | 13-18 (finder level 13) | Old Ironforge passage beside Magni's throne | **Fully covered**, ch03 (4/4 plus 98423 Treaty) | Warcraft Tavern; DB |
| **Ruins of Lordaeron** (16611) | New 5-man above Undercity | Horde-favoured; Alliance has its own 4 quests | 15-22 | Southshore, Dalaran, swim to Tirisfal | **Fully covered**, ch08 (4/4 Alliance) | Warcraft Tavern; DB |
| **Excavation Site: Wetlands** (16732) | New 5-man above Whelgar's dig | Both (separate quest sets) | 24-31 | Wetlands, past Whelgar | **Fully covered**, ch22 (9/9 Alliance; pickups in ch16/18/19/20) | DB; kami-labs |
| **Whelgar's Excavation Site** (16876) | New subzone or zone id for the revamped dig site (no separate DB spawns) | Alliance | 22-32 (Goaz Warders are 32 elites) | Wetlands 38.8,52.4 | **Covered**, ch18 and ch22 (299, 98216, 98310, 98313, 98824, 95810, 943) | DB |
| **Manor Mistmantle** (17191) | Listed as a 5-man instance in the client, but it has no bosses or level, and there's no portal at the manor | n/a | n/a | n/a | Not applicable. The outdoor manor is used in ch17 (Stalvan, 98) | [kami-labs](https://kami-labs.fr/en/manoir-mantebrume-wow-forever/), [Icy Veins](https://www.icy-veins.com/wow-forever/news/wow-forever-is-hiding-instance-portals-nobody-can-enter-yet/) |
| **Half-Pint Tavern** (16632) | Instance id in the client only. Wowhead lists no quests or NPCs, the DB has no spawns, and no web coverage was found | n/a | n/a | n/a | Not applicable | data only, low |
| **"Hillsbrad Foothills" instance** (16562) | 5-man id with no quests, NPCs or objects in the DB and an empty Wowhead listview; not among the 9 announced dungeons | n/a | n/a | n/a | Not applicable (not playable) | data; Warcraft Tavern list |
| Redridge **merchant camp** (Azeroth Commerce Authority, 10,72) | Caravan: Tamelyn Aldridge (Waylaid Supplies to Merchant's Favor), Daniel Stitchsong (patterns), Marcy Baker, Elaine Compton | Alliance (Marcy's crates also run to Dokimi in the Barrens) | Any | Redridge west entrance | **Partially covered**: used as a turn-in and vendor stop in ch06/10/16. Not taken: Sign Me Up! (95816, you buy the Advertising License Application from Tamelyn), Shipping Label (98247, item-started), 4x A Sealed Crate (trade-route deliveries, no XP) | DB |
| Camping hubs: Eric Brighthammer (DM 46.7,53.9), Sam Sarsaparilla (Elwynn 44.9,63.4), Lyreena Duskblade (Teldrassil 57.6,56.6) | The Great Outdoors / The Adventurer / Camping 101 | Alliance | 4-6 | Starting zones | Eric and Sam are **covered** for the route's professions (ch01b, ch00a/00b). Other-profession Camping 101s skipped on purpose. Lyreena (Night Elf start): **not visited** | DB |
| Westfall: Alba Fairmoon (52.5,52.9 and 38.7,83.7), Ozwin Ironsprocket (Saldean's) | New quest hubs | Alliance | 13-18 | Westfall | **Covered**, ch05/07 (Alba 7/7, Ozwin 2/2). Harvesting the Harvesters part 2 (92910, item-started, 800 XP) is mentioned in ch05 as a "keep if it drops" note | DB |
| Dun Morogh: Father Gavin, Beldin Steelgrill (Steelgrill's Depot), Earthseer Farsen, Mountaineer Gretchen, Bruegs Kindleborn, Teo Hammerstorm | New or reworked hubs | Alliance | 1-12 | Dun Morogh | **Covered**, ch01a/01b/00b (25/26; the only one missing is the repeatable Earth Sapta 94472) | DB |
| Elwynn new NPCs (Kelsey Fargo, Tordrin Sternblade, Josephine Carson, Blixie Fitzwink, Hamish Bergwort, Ormin Pelford, Hagar Lowe) plus Ridgepoint Tower (Merell Ross, 84.8,79.3) | New hubs | Alliance | 1-12 | Elwynn | **Covered** except Ridgepoint and the two rare-drop heads (Croaky's Head 91740, Elmpaw's Head 91746) and the Enchanting quest 91753 | DB |
| Loch Modan / Wetlands / Hillsbrad / Darkshore / Ashenvale / Stormwind new NPCs (Mountaineer Ylva, Braldir, Norric, Howin Kindfeather, Sylessa, Essene Villard, Hervdana, Captive Fire Elemental, Captain McManus, Emissary Jacques, Arbal, Maseara Autumnmoon, Gilbert Gray, Philmor, Roy Lewells) | New quest givers | Alliance | 11-30 | On route | **Covered** (each giver's new quests are 100% in the guide except the Shaman Sapta repeatables) | DB |
| Stonetalon: Night Elf Courier (48.7,39.9) | New quest, Stonetalon Supply Run (86574) | Alliance | req 20, L24 | ch20's optional Stonetalon dip runs past it | **Not covered** | DB |
| Teldrassil new quests (Dolanaar, Ban'ethil, Oracle Glade) | 12 story quests plus 14 camping/profession quests | Alliance (any race) | 3-12 | Rut'theran / Darnassus | **Not covered.** The route reaches Teldrassil at 23+ (ch11) and 29 (ch20), when all of them are grey | DB |
| Out of range or not open | Riverglades (16591, 36-44 by zones.json; Wowhead NPCs 36-57), Shen'dralas (16651, quests L38-43), Darkspear Islands battleground (16606, 30-60; quests req 30, L39), Mount Hyjal (55-60), Gilneas / Ruins of Gilneas / Shark-Infested Waters (guarded by level 63 elites), Battle for Gilneas, the BRS/BRD revamps, Burning Steppes 16508, map variants 16510/16509/16144, test maps | | | | Not applicable for 1-30 | zones.json, DB, Icy Veins |

## 2. New-quest coverage by zone

"Available" = new, Human/Dwarf-usable, class-free or Shaman/Hunter, req ≤ 30, not a profession quest, and quest level under 35 (the "L60" placeholder quests are counted). XP is Wowhead's value at the quest's own level.

| Zone | Available | In guide | Not in guide | XP not taken (known) | Profession quests (in guide) | Other-class / Skyborne-only |
|---|---|---|---|---|---|---|
| Dun Morogh | 26 | 25 | 1 | 0 | 12 (7) | 0 |
| Loch Modan | 12 | 10 | 2 | 0 | 0 | 0 |
| Ironforge | 7 | 4 | 3 | 1,125 | 2 (0) | 0 |
| Elwynn Forest | 31 | 27 | 4 | 2,195 | 14 (6) | 1 |
| Stormwind City | 14 | 13 | 1 | 125 | 0 | 5 |
| Westfall | 13 | 11 | 2 | 905 | 0 | 0 |
| Redridge Mountains | 10 | 4 | 6 | 1,320* | 0 | 0 |
| Duskwood | 3 | 2 | 1 | 0 | 0 | 0 |
| Wetlands | 30 | 30 | 0 | 0 | 0 | 0 |
| Darkshore | 7 | 5 | 2 | 1,275 | 0 | 0 |
| Ashenvale | 4 | 4 | 0 | 0 | 0 | 0 |
| Hillsbrad Foothills | 5 | 3 | 2 | 430 | 0 | 0 |
| Silverpine (Modera) | 2 | 1 | 1 | 265 | 0 | 0 |
| Arathi Highlands | 1 | 1 | 0 | 0 | 0 | 0 |
| Darnassus | 3 | 0 | 3 | 840 | 0 | 1 |
| Teldrassil | 12 | 0 | 12 | 4,650 | 14 (0) | 0 |
| Hall of Thanes | 3 | 3 | 0 | 0 | 0 | 0 |
| Ruins of Lordaeron | 4 | 4 | 0 | 0 | 0 | 0 |
| Excavation Site | 9 | 9 | 0 | 0 | 0 | 0 |
| City of Dalaran (dungeon) | 4 | 2 | 2 | 7,900 | 0 | 0 |
| Alterac / Dalaran city | 3 | 1 | 2 | 2,310* | 0 | 5 |
| **Zephras Isle** | **88** | **0** | **88** | **40,300** | 14 (0) | 15 |
| Deadmines / Stockade | 1 / 0 | 1 / 0 | 0 | 0 | 0 | 0 |
| The Barrens | 3 | 0 | 3 | ? | 0 | 0 |
| Stonetalon | 1 | 0 | 1 | 1,950 | 0 | 0 |
| **Total** | **296** | **160** | **136** | **65,590** | 56 (13) | 27 |

\* These include quests that Wowhead lists at level 60 (the commerce and cloth-donation quests). Their real XP at your level is unknown and probably much lower. Also outside the table: 146 Craftsman's Writ quests in the new "Crafting" category (16941). They are profession-gated and none are in the guide.

The Hall of Thanes row shows 3 because 96393 is filed under its Dun Morogh giver. All 4 of its quests are in the guide.

## 3. New quests not in the guide (excluding Zephras Isle)

| Zone | Quest (id) | Req / L | Giver | XP | Probable reason it isn't in the guide |
|---|---|---|---|---|---|
| Stonetalon | Stonetalon Supply Run (86574) | 20 / 24 | Night Elf Courier 48.7,39.9 → Innkeeper Faralia, Stonetalon Peak 35.8,5.7 | 1,950 | Missed. It sits on ch20's optional dip: 6 bundles from the Pridewings the dip runs past (drop rate not in the DB), and the hand-in is next to Keeper Albagorm (37.1,8.1), where the dip already ends. Full XP at 29. Reward: Courier's Wristguards |
| Elwynn | Croaky's Head (91740) | 7 / 10 | Drops from Croaky (L11, SE Elwynn 76.7,85.7), hand in to Merell Ross at Ridgepoint Tower 84.8,79.3 | 840 | Rare-mob drop, off-path corner; Human route only |
| Elwynn | Elmpaw's Head (91746) | 7 / 10 | Drops from Elmpaw (L12, 76.3,47.1), hand in to Helene Peltskinner 46.2,62.2 (the guide visits her) | 840 | Rare-mob drop; Human route only |
| Elwynn | An Enchanting Lesson (91753) | 5 / 7 | Kitta Firewind, Tower of Azora | 475 | Profession-gated (you have to disenchant Crude Wax Effigies) |
| Elwynn | A Scribbled Letter (92479) | 1 / 1 | Marshal McBride | 40 | Hunter letter, Human only; trivial (the guide's Hunter goes to the trainer anyway) |
| Redridge | Sign Me Up! (95816) | 1 / "60" | Item bought from Tamelyn Aldridge, hand in to Elaine Compton (merchant camp) | 660 at L60 | Commerce or shop system. XP is the level-60 figure. The guide already stops there 3 times |
| Redridge | Shipping Label (98247) | 10 / "60" | Item-started (source not in the DB), hand in to Marcy Baker | 660 at L60 | Unknown item source |
| Redridge | A Sealed Crate (91899/91900/91904/91905) | 0-1 / "60" | Marcy Baker ↔ Dokimi (Barrens) | none | Trade-route delivery, no XP |
| Ironforge | Rotgath Stonebeard (95817) | 1 / "60" | No giver in the DB | 660 at L60 | Commerce or shop chain; no start point known |
| Ironforge | Your Package Has Arrived (97263) | 1 / 2 | Misplaced Packages object 72.3,48.6, hand in to Eldrun | 45 | Trivial |
| Ironforge / Dun Morogh / Loch Modan | Call of Earth 96243 (level-10 twin, noted in 01a); Earth/Fire/Water Sapta 94472/94473/94616 | | | | Shaman twins or repeatables; deliberate |
| Darkshore | WANTED: Jai'vhanel (98025) | 10 / 13 | WANTED board, Auberdine 37.2,44.2 | 1,150 | Grey at 23-24 (about 115 XP). Reward: Swordfeather Cloak |
| Darkshore / Stormwind | Expanding Horizons (97914) / Making Do (97926) | 13 / 17 | Thundris ↔ Baros Alexston | 125 each | Breadcrumb pair, grey at 23 |
| Darnassus | Eyes of the Sentinels (98067); Crown of the Earth 98046/98065 | 1 / 11 | Sentinel Dalia Sunblade, Fandral, Lariia | 660 / 90 / 90 | Grey at 29; the Crown chain is Night Elf story |
| Teldrassil | Nature's Call 97977, Fang of Githyiss 97236, Soft Saber Pelts 87288, The Lost Runner 99046, Not Dead Yet 99047, Escaping Ban'ethil 99053, The Great Tree Provides 99050, Easing Suffering 99073, Twisted Hatred 98403, The Sisterhood of Elune 98391, Darkness in the Glade 98392, The Oracle Tree 98398 | 1-6 / 3-12 | Dolanaar, Oracle Glade | 4,650 total | Night Elf start zone; grey by the time the route arrives |
| Westfall | Harvesting the Harvesters (92910) | 8 / 15 | Item (Precessive Autocognition Assembly) from harvest golems | 800 | Mentioned in ch05 as "keep if it drops" (no tag) |
| Westfall | Of Mice and Milk (93928) | 15 / 15 | Mouse, hand in to Hemet Nesingwary (STV) | 105 | Joke quest; ends in STV |
| Hillsbrad | A Lack of Virtue (98459), Talk of the Town (98463) | 18 / 21, 28 / 33 | Tom Half-fish, Barkeep Kelly | 165 / 265 | Skipped on purpose (ch23 note: breadcrumbs to Menethil / Booty Bay) |
| Silverpine / Dalaran dungeon | Starving Arcane (92457), Heart of Disruption (92458), Friend of the Kirin Tor (92459) | 24 / 33 | Image of Archmage Modera 68.6,45.2 | 3,950 / 3,950 / 265 | Deferred to the 30-40 guide (dungeon closed in beta) |
| Dalaran city | A Donation of Wool (99191), A Donation of Silk (99192) | 12 / "60", 26 / "60" | Belanaa Windveil (High Order cloth QM) 11.7,57.8 | 660 / 1,650 at L60 | Not considered; cloth turn-in; XP is the level-60 figure |
| Duskwood | An Unfortunate End (99267) | 1 / "60" | Night Watch Guard | none | Torch reward only |
| Barrens | Chol'aruk the Ravener (97005) | 15 / 21 | Bainham, Ratchet 61.9,39.4 (Chol'aruk at 57.7,27.2) | ? | Off route until ch26, by which point it's 9 levels grey |
| Barrens | Legacy Reward x2 (96339, 96383) | 0 / "60" | Innkeeper Wiley | none | Account reward, not questing |

Not counted above, because they're out of range or not Shaman/Hunter quests: Past Due (96800, L38), Darkspear Islands Clash (98895/6, req 30 L39), the Shaman quests 96016/96135 (L40, already noted in ch25), the rogue Syndicate chain, priest/druid/mage class quests. Wowhead also lists 5 new quests that aren't in QuestieDB 1.0.6, so they may have been removed or renumbered. Two of them are already handled as notes in the guide: A Taste of Darkness 95771 (ch00b) and The Valor Family 98447 (ch14/17). The other three are A Quick Craft 95818 (Ironforge shop quest, "L60"), An Acquaintance in Southshore 95786 (STV, req 30) and A Sealed Crate 91906.

**Zephras Isle, by area** (class-free quests usable by Human/Dwarf; 2 have no XP listed): Thendal Grove, quest levels 1-5: 14 quests, 3,090 XP. Shen'dar Village and Falaath, 6-9: 30 quests, 13,420 XP. Valanaar and Gustberry, 10-11: 23 quests, 13,640 XP. Shadowgale and the finale, 12-13: 19 quests, 9,225 XP. **Total: 86 quests, 39,375 XP.** That is roughly all the XP from 1 to about 11.5, so it's a complete starting zone. With the Classic grey-quest XP cut, the static value is about 37,200 XP for a level-12 visitor, but only about 8,600 XP for a level-20 visitor. Level 20 is when the route first reaches Dalaran (ch08).

## 4. Bottom line

1. **Already done:** every new dungeon and hub that is playable for Alliance at 1-30 is in the guide. That covers Hall of Thanes, Ruins of Lordaeron, Excavation Site, Whelgar, the merchant camp, the camping and Alba/Gavin/Steelgrill/Kindfeather hubs, and the new Hillsbrad NPCs. Wetlands, Ashenvale, Duskwood and the three new instances are at 100% of available new quests.
2. **Zephras Isle (not covered):** the only new 1-30 questing zone. It is a full 1-12 Skyborne start (86 quests, about 39k XP). Two things stand in the way:
   - It's uncertain a Dwarf or Human can get there at all. Sources conflict, and you'd have to reach the Dalaran dock first.
   - Even if you can, the route first reaches Dalaran at level 20, when the island is worth only about 8.6k XP for many hours of play.

   Recommendation: skip it on the Dwarf/Human route. If you roll a High Order Skyborne (Hunter is available to them; Shaman is Horde-only), it would need its own 1-12 chapter set that replaces Coldridge, Dun Morogh, Northshire and Elwynn, then join at Loch Modan or Darkshore around level 12. If you just want to see the island, test the skycutter on launch day before planning anything.
3. **City of Dalaran dungeon (28-33):** deferred on purpose. If it opens on 4 Nov, the chain is worth about 16.7k XP at 30: 92456 + 92489 + 92457 + 92458 at 3,950 each, 92432 at 660, 92459 at 265. That is the biggest new block just past 30. Dungeon quests lost half their bonus XP on 1 Oct.
4. **Cheap new pickups on the existing route:**
   - **Stonetalon Supply Run (1,950 XP)**, in ch20's Stonetalon dip. Nearly free: courier on the road, mobs you already pass, hand-in next to Albagorm.
   - **Croaky's Head and Elmpaw's Head (840 XP each)** on the Human Elwynn route at level 10-11. Each needs a named rare: Croaky in the SE corner, Elmpaw east of Goldshire. Croaky's hand-in is at Ridgepoint Tower, which the guide never visits.
   - **Sign Me Up!** at the merchant camp the guide already stops at, and the Dalaran cloth donations when ch08 walks through the city. Real XP is unknown because Wowhead lists them at level 60.
   - Everything else missing is grey at the route's level (Jai'vhanel, Darnassus, Teldrassil), off route, or not real questing.
5. **Side findings (not about new zones, worth checking):**
   - (a) ch08 still treats the Dalaran crater as a place with hostile Kirin Tor mages. The Forever DB has a friendly city there with inns, battlemasters, vendors, and a Skyborne Portal to Stormwind at 12.0,56.2. If the capitals have portals to Dalaran (allthings.how mentions a "Skydome Portal" in Stormwind's Wizard's Sanctum), the 15-20 minute Southshore trek to Ruins of Lordaeron could be much shorter. Unverified.
   - (b) Both QuestieDB and Wowhead give Old Ironforge Incursion (96393) and The Restless Dead (96394) the race mask 4294967372, which is Dwarf, Night Elf and Gnome only, with no Human. Yet 00b (Human) offers 96393 and shared ch02 offers 96394 with no Human caveat. Elsewhere the guide does flag Human exclusions (ch16, ch18).
