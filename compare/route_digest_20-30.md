# Route digest: Forever Alliance levels 20-30 (Dwarf Shaman, Dwarf/Human Hunter)

Sources: tooling/qdb/{quest,npc,object,item}.json, Wowhead zone json (data/zone_*.json), data/quests.json, tooling/extra_quests.json, data/entities.json, compare/TUGs-1.12-2026-10-14 raw Lua and tugs_20-35.tsv, guide/Guidelime_ForeverAlliance 00-08 (incl. 08_RuinsOfLordaeron, 08_LooseEnds), QuestieDB Forever Zones/dungeons.lua (entrances). compare/pool_20-30.txt covers only 3 zones, so the pool was rebuilt from Questie + Wowhead. Facts only: every qid, req, XP, giver, ender, prerequisite is from those files; blank XP = `?`; unresolved items are flagged. No route is proposed.

Scope: Alliance (Questie race mask &77 / Wowhead side 1,3), class-free + Shaman + Hunter class quests. Excluded: Horde-only, other classes, PvP/BG, seasonal (category2 9), professions (unless class-free and on route), Craftsman's Writ, NYI rows 636, 79090, 95817, 95818, 79945, and 34 event/legacy/turn-in rows with quest level >=55 but req <40 (cloth Donation quests, Darkmoon Faire, Sealed Crate, Shipping Label, Legacy Reward...). Coordinates are Forever map space as in the DB and guide. Zone codes in brackets after a location: SW Stormwind, IF Ironforge, WL Wetlands, DW Duskwood, RR Redridge, WF Westfall, EL Elwynn, DS Darkshore, AV Ashenvale, LM Loch Modan, DM Dun Morogh, AR Arathi, HB Hillsbrad, SP Silverpine, DN Darnassus, AL Alterac, DU Dustwallow, ST Stonetalon, TN Thousand Needles, BA Barrens, FE Feralas, BL Badlands, STV Stranglethorn.

### State at the end of chapter 08 (08_RuinsOfLordaeron.lua)

- Level 20, in Stormwind (Cathedral Square / Stockade gate / Keep hand-ins), hearth = Sentinel Hill (Westfall), Southshore flight path taken, Sentinel Hill and Stormwind flights known (ch08 uses them). ch08 boat route: Stormwind harbour > Auberdine > Menethil > Southshore.
- Turned in by ch08: 389, 3765, 92415, 95195, 95250 and optional 95189. Accepted by ch08 and still open: 971 Knowledge in the Deeps (Shaman; Hunter optional), 1275, 94494 (Shaman), 95161, 98461 (optional breadcrumb to Menethil). ch08 log check also lists 121, 118, 115, 19, 353 (open from 1-20).
- 08_LooseEnds optional list: 95041 Data Hoarders (abandon unless 7 punch cards), Loch Modan elites (271, 531, 217, 255, 256), A Dark Threat Looms 250-283, Redridge 20-25 (122, 124, 126, 143/144, 150, 91, 219), Call of Water 94495/94497 (stops before 94499), Stockade pickups. Column `D`: D = turned in during 1-20 (252 quests), 8 = ch08, L = 08_LooseEnds.

Hubs (Sections 2-4) are coordinate boxes around the named town/camp, e.g. Menethil x5-15 y48-66, Dun Modr x44-56 y8-24, Whelgar x33-43 y46-56, Darkshire x66-86 y40-52, Lakeshire x15-30 y40-64, SW Cathedral x48-61 y42-57, SW Keep x68-83 y26-48, IF Cavern x44-55 y2-16, Astranaar x30-40 y44-54, Auberdine x30-44 y36-50, Southshore x42-56 y44-70, Refuge x40-52 y42-52; a giver outside every box is `Field NPCs` (zone name in Section 3).

### Data gaps and conflicts

- XP = Wowhead XP at quest level, no decay (Section 5.2). `?` = blank in data. Questie vs Wowhead disagreements carry `WHreq`/`WHL`: 631/632/633 Thandol Span Q28 vs WH26, 1144 Willix Q23 vs WH22, 2904 A Fine Mess Q24 vs WH20, 472 WHL30.
- QDB lacks pre/next/givers for many new Forever (9xxxx) quests; fallbacks: atlas info.start/end, extra_quests, entities.json, Wowhead, quest text. No link data for the Dragonmaw arc (98208-98310), the Wetlands Lost chain (87491-88758) or the Excavation set; their order is inferred (`..`, `~>` in Section 3).
- NPC level bands (npc.json) are missing for Ruins of Lordaeron (2 rows, no levels), Excavation Site (0 rows) and Dalaran (0 rows); only quest levels and ch08 text (RoL finder L15, bosses L18-22) exist. No spawn data: 265701 Captain Truman (95250), 262681 Ardin Grassman (95647 ender), Daewyn (95772 ender); givers of 95795, 95809, 78924, 78916 not in files.
- Dungeon sort ids: Gnomeregan 133 (721), Razorfen Kraul 1717 (491), Ruins of Lordaeron 16611 (+16591 for 95161). BFD has Wowhead type-62 duplicates (78921, 78923-78926, req 25) excluded from sums (78916 The Heart of the Void is a separate r25 row, giver not in files); SoD Gnomeregan 79xxx/80xxx (req 40) ignored. Brief ids: 1198 = In Search of Thaelrid, 1199 = Twilight Falls, 1200 = Blackfathom Villainy.
- Shadowfang Keep: all 3 quests are Horde-only (no Alliance quests). RoL Horde-only quests excluded. Deadmines fully done in 1-20.
- Call of Water: no pre/next in QDB; 94503 text says Westfall but npc 5895 spawns only in Silverpine (38.7,44.6), ch08 agrees with Silverpine and calls 94503 "a return to Norric" while QDB ends 94502 and starts 94503 at Forgotten Shrine (Westfall 45.6,59.9). 94616 Water Sapta (r20, Norric, XP blank) is outside the brief chain, looks like an alternate Westfall step.
- Class quests req 15-35: Hunter only 78830 (STV, req 26 L40, quill from Gharrik in Badlands) and 78114 (no giver/ender, req 1, L25, tooltip 404). Shaman req 30: 94789, 79358, 96016, 96135, 96264 (Arathi, Veyric Thunderhame). Wowhead lists Call of Earth/Fire (94373 94374 94375 94449 94465 94468) as Dwarf-only; no other Shaman race data used.
- Race: Questie says all Alliance on every pool row; Wowhead reqrace 76 (no Human bit) on 35 digest rows, shown `noHu?` (98208, 98209, 98197, 98072, 98190, 98282, 98221, 98245, 98246, 98386, 98387, 96393, 98461, 98815 ...); unresolved, matters only for a Human Hunter.
- Duskwood Missions 81730-81747 (Field Captain Palandar, 46.0,49.4) are group dailies, req 23 L27, one row, excluded from sums. Other dailies/repeatables flagged (Talismans of Merit 8289/7921/7887, Sparklematic tier 3).
- TUGs: 28-29 Blackfathom Depths and 32-33 Excavation Site are placeholders ("This will be added later", #N/A); 33-34 Gnomeregan partly #N/A; no `[S ...]` hearth sets and no `Set your [H]` in chapters 20-32; Missing Diplomat is only started in 30-31 (1274, 1241, 1242, accepts 1243; 1244 is in 32-33); 95737 accepted in 27-28, turned in in 29-30 with 95647 picked up.
- Dun Modr (Dark Iron elites L27-31), the Dragonmaw arc and the Excavation set are `new` in Forever.

## 1. Dungeon quests

Dungeon membership = Questie sort/WH category in the dungeon (Gnomeregan also sort 133, Razorfen Kraul sort 1717), or giver/ender/objective NPC living only inside it. Alliance + class-free + Shaman/Hunter only; Horde-only, PvP, seasonal excluded. `D` col: D=turned in during 1-20, a=accepted in 1-20 still open, 8=accepted/turned in by ch08, L=in 08_LooseEnds.

### Ruins of Lordaeron (16611)
- entrance: Undercity (zone 1497) 72.48,11.33 per QuestieDB dungeons.lua; ch08 text puts the portal in the ruins courtyard, Tirisfal Glades ~61,67 (swim from Dalaran shore)
- band: no NPC level data in npc.json (2 NPC rows); ch08: finder L15, bosses L18-22, group of 5, ~45 min; quest levels 21-22 req 15-16
|id|name|req/L|xp|giver|ender|pre (*=in digest, D=done 1-20, !=not in digest)|next|st|T|D|notes|
|---|---|---|---|---|---|---|---|---|---|---|---|
|92415|Remember That I Love You|15/22|2600|item:Blood-Stained Parchment / item:Last Scrawlings of Edward Heartweaver|Orphan Matron Nightingale 56.3,54.0 [SW]|||N|T20|8|item start (source ?); ch08: Blood-Stained Parchment lies beside Rath'mael (last boss); click to start|
|95161|Remember That I Love You|15/22|175|Orphan Matron Nightingale 56.3,54.0 [SW]|Avette Fellwood 73.0,44.4 [DW]|||N|T20|8|noHu?|
|95250|Abominable Creatures|16/21|1650|?|?|||N|T20|8|no giver; no ender; txt: Collect the Head of the Baron in the Ruins of Lordaeron and bring it back to Captain Trum.; ch08+objective text: giver/ender = Captain Truman (npc 265701, no spawn data) just inside the entrance|
|95195|Bloodied Insignia|16/22|2600|item:Bloodied Insignia|General Marcus Jonathan 69.2,82.7 [SW]|||N|T20|8|item start (drop: Ragged Ghoul, Mangled Cadaver); ch08: first undead looted drops the Bloodied Insignia that starts it; 10 total|
|95189|Crest of Lordaeron|16/22|2600|item:Crest of Lordaeron|Lady Dena Kennedy 65.6,13.8 [SW]|||N|T20|8|item start (source ?); ch08: Crest lies on the ground along the route; hand-in Lady Dena Kennedy, ch08 coords 62.6,5.8 (entities.json 65.6,13.8)|

### The Stockade (717)
- entrance: Stormwind 52.41,70.01 (Warden Thelwater 51.5,69.4 is at the gate)
- band: hostile NPCs L23-29 (n=11); elites L23-29 (n=11)
|id|name|req/L|xp|giver|ender|pre (*=in digest, D=done 1-20, !=not in digest)|next|st|T|D|notes|
|---|---|---|---|---|---|---|---|---|---|---|---|
|391|The Stockade Riots|16/29|2350|Warden Thelwater 51.5,69.4 [SW]|=|389*|392*|-|T25|||
|377|Crime and Punishment|22/26|2100|Councilman Millstipe 71.9,47.8 [DW]|=|||U|T24,T25|||
|387|Quell The Uprising|22/26|2650|Warden Thelwater 51.5,69.4 [SW]|=|||U|T25|||
|388|The Color of Blood|22/26|2650|Nikova Raskol 76.4,63.7 [SW]|=|||-|T25|||
|378|The Fury Runs Deep|22/27|2750|Motley Garmason 49.7,18.2 [WL]|=|303*||U||||
|386|What Comes Around...|22/25|2000|Guard Berton 21.2,46.6 [RR]|=|||U|T25|||

### Shadowfang Keep (209)
- entrance: Silverpine Forest 44.8,67.8
- band: hostile NPCs L18-26 (n=27); elites L18-26 (n=25); all 3 QDB/WH quests are Horde-only: NO Alliance quests
- no Alliance quests found for this dungeon.

### Blackfathom Deeps (719)
- entrance: Ashenvale 14.5,14.2
- band: hostile NPCs L22-28 (n=29); elites L22-28 (n=28)
|id|name|req/L|xp|giver|ender|pre (*=in digest, D=done 1-20, !=not in digest)|next|st|T|D|notes|
|---|---|---|---|---|---|---|---|---|---|---|---|
|971|Knowledge in the Deeps|10/23|2750|Gerrig Bonegrip 50.8,5.6 [IF]|=|||-||8||
|1200|Blackfathom Villainy|18/27|3300|Argent Guard Thaelrid (inside BFD)|Dawnwatcher Selgorm 56.2,24.4 [DN]|||U||||
|1198|In Search of Thaelrid|18/24|2400|Dawnwatcher Shaedlass 55.4,25.0 [DN]|Argent Guard Thaelrid (inside BFD)||1200*|-||||
|1275|Researching the Corruption|18/24|2400|Gershala Nightwhisper 38.3,43.0 [DS]|=|||U||8||
|1199|Twilight Falls|20/25|2550|Argent Guard Manados 55.2,24.0 [DN]|=|||U||||
|78921|Blackfathom Villainy|25/27|3300|Argent Guard Thaelrid (inside BFD)|Dawnwatcher Selgorm 56.2,24.4 [DN]|||U|||type62(raid)|
|78924|In Search of Thaelrid|25/27|2750|?|?|||U|||type62(raid); no giver; no ender|
|78923|Knowledge in the Deeps|25/27|3300|Gerrig Bonegrip 50.8,5.6 [IF]|=|||U|||type62(raid)|
|78926|Researching the Corruption|25/27|2750|Gershala Nightwhisper 38.3,43.0 [DS]|=|||U|||type62(raid)|
|78916|The Heart of the Void|25/25|?|?|Dawnwatcher Selgorm 56.2,24.4 [DN]|||U|||no giver; txt: The Heart of the Void / Bring the Blackfathom Pearl to Dawnwatcher Selgorm in Darnassus.|
|78925|Twilight Falls|25/27|2750|Argent Guard Manados 55.2,24.0 [DN]|=|||U|||type62(raid)|

### Excavation Site: Wetlands (16732)
- entrance: Wetlands 47.79,56.16
- band: no NPC level data in npc.json (0 NPC rows); quests req 24, L28-31
|id|name|req/L|xp|giver|ender|pre (*=in digest, D=done 1-20, !=not in digest)|next|st|T|D|notes|
|---|---|---|---|---|---|---|---|---|---|---|---|
|95795|Fallen in the Fen|24/31|3150|?|Dorin Songblade 25.8,46.4 [RR]|||N|||no giver; txt: Return to Dorin Songblade.|
|95809|Heartwoven|24/31|3150|?|Caitlin Grassman 11.9,58.8 [WL]|||N|||no giver; txt: Return to Caitlin Grassman in Menethil Harbor.|
|98815|Highland Hides|24/28|1150|James Halloran 8.6,55.7 [WL]|=|||N|||noHu?|
|95646|Horrors in the Highland|24/31|3150|Rethiel the Greenwarden 56.4,40.4 [WL]|=|||N|||noHu?|
|95810|Lost Relic Carry|24/31|630|item:Titan Relic|Prospector Whelgar 38.8,52.4 [WL]|||N|||item start (drop: Relic Guardian)|
|95647|Lost in the Thicket Things|24/31|2500|Caitlin Grassman 11.9,58.8 [WL]|?|||N|T29||noHu?; no ender; txt: Find Ardin Grassman in the Excavation Sites.; ender = Ardin Grassman inside the Excavation Site (npc 262681, no spawn data)|
|98824|Prehistoric Prism|24/31|3150|Prospector Whelgar 38.8,52.4 [WL]|High Explorer Magellas 69.9,18.6 [IF]|||N||||
|95737|Seeking Caitlin|24/31|630|Llana 35.0,48.5 [AV]|Caitlin Grassman 11.9,58.8 [WL]|||N|T27|||
|95772|Songblade Search|24/31|3150|Dorin Songblade 25.8,46.4 [RR]|?|||N|||noHu?; no ender; txt: Look for Dorin Songblade's brother, Daewyn, in Whelgar's Excavation Site.; ender = Daewyn inside Excavation Site (text); not in files|

### Gnomeregan (721; Questie sort 133)
- entrance: Dun Morogh 24.3,39.8
- band: hostile NPCs L20-34 (n=28); elites L25-34 (n=22)
|id|name|req/L|xp|giver|ender|pre (*=in digest, D=done 1-20, !=not in digest)|next|st|T|D|notes|
|---|---|---|---|---|---|---|---|---|---|---|---|
|2926|Gnogaine|20/27|2200|Ozzie Togglevolt 45.9,49.4 [DM]|=||2962*|-|T33o|||
|2928|Gyrodrillmatic Excavationators|20/30|2450|Shoni the Shilent 62.6,34.1 [SW]|=|||U|T30|||
|2922|Save Techbot's Brain!|20/26|2650|Tinkmaster Overspark 69.5,50.3 [IF]|=|||-|T31,T33o|||
|2927|The Day After|20/27|220|Gnoarn 69.2,50.5 [IF]|Ozzie Togglevolt 45.9,49.4 [DM]||2926*|-|T33o|||
|2962|The Only Cure is More Green G.|20/30|2450|Ozzie Togglevolt 45.9,49.4 [DM]|=|2926*||-||||
|2923|Tinkmaster Overspark|20/26|210|Brother Sarno 51.0,48.4 [SW]|Tinkmaster Overspark 69.5,50.3 [IF]||2922*|-|T30|||
|2904|A Fine Mess|24/30|2450|Kernobee (inside Gnomeregan)|Scooty 27.6,77.5 [STV]|||U|||ESC?; WHreq20|
|2924|Essential Artificials|24/30|3050|Klockmort Spannerspan 67.9,46.1 [IF]|=|||-|T31,T33o|||
|2925|Klockmort's Essentials|24/30|245|Mathiel 59.5,45.4 [DN]|Klockmort Spannerspan 67.9,46.1 [IF]||2924*|-|T34|||
|2931|Castpipe's Task|25/28|230|Gaxim Rustfizzle 59.5,67.2 [ST]|Master Mechanic Castpipe 69.8,48.1 [IF]||2930*|-|T27|||
|2930|Data Rescue|25/30|3650|Master Mechanic Castpipe 69.8,48.1 [IF]|=|||-|T31,T33o|||
|2953|More Sparklematic Action|25/30|?|obj:The Sparklematic 5200 (inside Gnomeregan)|=|2952*, 4605*, 4606*||-|||REPT; excl:4603,4604|
|4603|More Sparklematic Action|25/30|?|obj:The Sparklematic 5200 (inside Gnomeregan)|=|2952*, 4605*, 4606*||-|||REPT; excl:2953,4604|
|4604|More Sparklematic Action|25/30|?|obj:The Sparklematic 5200 (inside Gnomeregan)|=|2955! ?, 4605*, 4606*||-|||REPT; excl:2953,4603|
|2929|The Grand Betrayal|25/35|2750|High Tinker Mekkatorque 68.8,49.0 [IF]|=|||-|T31,T33o|||
|2951|The Sparklematic 5200!|25/30|?|obj:The Sparklematic 5200 (inside Gnomeregan)|=|||-|||excl:4601,4602|
|2952|The Sparklematic 5200!|25/30|2450|obj:The Sparklematic 5200 (inside Gnomeregan)|=|2951*, 4601*, 4602*||-|||excl:4605,4606|
|4601|The Sparklematic 5200!|25/30|?|obj:The Sparklematic 5200 (inside Gnomeregan)|=|||-|||excl:2951,4602|
|4602|The Sparklematic 5200!|25/30|?|obj:The Sparklematic 5200 (inside Gnomeregan)|=|||-|||excl:2951,4601|
|4605|The Sparklematic 5200!|25/30|2450|obj:The Sparklematic 5200 (inside Gnomeregan)|=|2951*, 4601*, 4602*||-|||excl:2952,4606|
|4606|The Sparklematic 5200!|25/30|2450|obj:The Sparklematic 5200 (inside Gnomeregan)|=|2951*, 4601*, 4602*||-|||excl:2952,4605|
|2945|Grime-Encrusted Ring|28/34|2700|item:Grime-Encrusted Ring|obj:The Sparklematic 5200 (inside Gnomeregan)|||-|||item start (drop: Dark Iron Agent)|
|2947|Return of the Ring|28/34|2700|obj:The Sparklematic 5200 (inside Gnomeregan)|Talvash del Kissel 36.4,3.6 [IF]|2945*|2948*|-||||

### Razorfen Kraul (491; Questie sort 1717)
- entrance: The Barrens 42.9,90.2
- band: hostile NPCs L15-33 (n=39); elites L24-33 (n=37)
|id|name|req/L|xp|giver|ender|pre (*=in digest, D=done 1-20, !=not in digest)|next|st|T|D|notes|
|---|---|---|---|---|---|---|---|---|---|---|---|
|1221|Blueleaf Tubers|20/26|2100|Mebok Mizzyrix 62.4,37.6 [BA]|=|||-||||
|1144|Willix the Importer|23/30|3050|Willix the Importer (inside RFK)|=|||U|||ESC?; WHreq22|
|1142|Mortality Wanes|25/30|3050|Heralath Fallowbrook (inside RFK)|Treshala Fallowbrook 69.5,67.8 [DN]|||U||||
|1101|The Crone of the Kraul|29/34|3350|Falfindel Waywarder 89.6,46.6 [FE]|=|1100*||-||||
|96264|Elemental Aid|30/33|2650|Veyric Thunderhame 59.8,27.6 [AR]|=|||N|||[Sha]|

### Scarlet Monastery (796)
- entrance: Tirisfal Glades 82.6,33.8
- band: hostile NPCs L8-42 (n=36); elites L30-42 (n=33)
|id|name|req/L|xp|giver|ender|pre (*=in digest, D=done 1-20, !=not in digest)|next|st|T|D|notes|
|---|---|---|---|---|---|---|---|---|---|---|---|
|1050|Mythology of the Titans|28/38|3550|Librarian Mae Paledust 75.0,12.5 [IF]|=|||-|T31|||
|96800|Past Due|30/38|2850|Magus Olvek 10.7,64.1 [AL]|=|||N||||
|1053|In the Name of the Light|34/40|4700|Raleigh the Devout 51.5,58.4 [HB]|=|1052! Down the Scarlet Path||-||||

### Deadmines (1581) leftovers
- entrance: Westfall 42.5,71.7
- band: hostile NPCs L14-21 (n=24); elites L17-21 (n=21)
- all Alliance Deadmines quests (92753, 166, 167, 168, 214, 2040, plus 373 The Unsent Letter) were turned in during 1-20 (D). Nothing left. (7938 is the Darkmoon quest, seasonal, excluded.)

### City of Dalaran (16544) - not requested, present in data
- entrance: Alterac Mountains 8.46,59.21
- band: no NPC level data in npc.json (0 NPC rows); quests req 24, L33
|id|name|req/L|xp|giver|ender|pre (*=in digest, D=done 1-20, !=not in digest)|next|st|T|D|notes|
|---|---|---|---|---|---|---|---|---|---|---|---|
|92456|A Green Sample|24/33|3950|Shylamiir 31.5,62.6 [SW]|=|||N||||
|92458|Heart of Disruption|24/33|3950|Image of Archmage Modera 68.6,45.1 [SP]|=|||N||||
|92489|Power Overwhelming|24/33|3950|High Sorcerer Andromath 48.7,87.6 [SW]|=|||N||||
|92457|Starving Arcane|24/33|3950|Image of Archmage Modera 68.6,45.1 [SP]|=|||N||||


## 2. Zone quest tables (grouped by giver hub; a quest is filed under the zone of its giver, so a Stormwind-sorted quest handed out in Darkshire sits under Duskwood)

Columns: req/L = Questie required level / quest level. xp = Wowhead XP at quest level (? = blank in data). Rows are sorted by giver then req within each hub; `"` in the giver or name column = same as the row above. giver/ender: name x,y (coordinates rounded to integers here; exact values in tooling/qdb), `[XX]` zone code when outside the table zone, `=` ender same as giver, `obj:`/`item:` object/item starters, `(inside X)` NPC spawns only inside a dungeon, `no giver`/`no ender` not in the files. pre: ids that unlock the row (`ALL:` = all needed, else any); `!` = prerequisite not in this digest (name given), `D` = done in 1-20. next: Questie next id (`!` = not in digest). st = Forever status (N new, U updated, - unchanged, ? unknown). T = TUGs chapter (T23 = chapter 23-24, `o` optional). D = Atlas guide (D turned in during 1-20, a accepted only, 8 handled by ch08, L in 08_LooseEnds). Notes: GRP group quest (Wowhead type 1), ESC? party-accept/escort flag, DAILY/REPT repeatable, type62(raid) Wowhead raid-type duplicate, WHreq/WHL Wowhead req/level disagrees with Questie, noHu? Wowhead reqrace 76 = no Human bit while Questie says all Alliance (unresolved; matters only to a Human Hunter), item start (drop: X). Sums exclude dailies, repeatables, type-62. Rows with req<5 and 1-20-done rows with req<18 and L<21 are omitted.

### 2.0 Class quests (Shaman and Hunter, req 15-35 anywhere in Questie+Wowhead data), tagged in notes
Scan result: Shaman = Call of Water (9), 94616, Call of Air 94789 and the req-30 Arathi set (79358, 96016, 96135, 96264); Hunter = only 78830 and 78114.
|id|name|req/L|xp|giver|ender|pre|next|st|T|D|notes|
|---|---|---|---|---|---|---|---|---|---|---|---|
|94494|Call of Water|20/20|780|Eldrun Stormbreaker 47,14|Norric Lochthane 42,19|||N||8L|[Sha]; Water Totem chain start (level-20 totem quest); ch08 takes it at Eldrun|
|94495|Call of Water|20/22|435|Norric Lochthane 42,19|Hervdana Saegrund 66,76|||N||L|[Sha]|
|94497|Call of Water|20/22|870|Hervdana Saegrund 66,76|=|||N||L|[Sha]|
|94499|Call of Water|20/22|1300|Hervdana Saegrund 66,76|=|||N|||[Sha]|
|94500|Call of Water|20/23|1400|Hervdana Saegrund 66,76|=|||N|||[Sha]|
|94501|Call of Water|20/23|460|Hervdana Saegrund 66,76|Norric Lochthane 42,19|||N|||[Sha]|
|94502|Call of Water|20/23|1400|Norric Lochthane 42,19|obj:Forgotten Shrine 46,60|||N|||[Sha]|
|94503|Call of Water|20/23|185|obj:Forgotten Shrine 46,60|Minor Manifestation of Water 39,45|||N|||[Sha]; ender per QDB = Westfall south coast; ch08 text says Silverpine 38.4,44.4 is the next step (94505); see sec 3 note|
|94505|Call of Water|20/23|2750|Minor Manifestation of Water 39,45|Norric Lochthane 42,19|||N|||[Sha]|
|94616|Water Sapta|20/20|?|Norric Lochthane 42,19|=|||N|||[Sha]; not in brief chain; text: take the water sapta to tainted pond water in Westfall (looks like an alternate/obsolete Westfall step; XP blank)|
|94789|Call of Air|30/30|2450|Eldrun Stormbreaker 47,14|Veyric Thunderhame 60,28|||N|||[Sha]; req 30; Eldrun (IF) -> Veyric Thunderhame (Arathi NE); start of Call of Air|
|79358|Storm, Earth, and F.|30/38|3150|Veyric Thunderhame 60,28|Rau Cliffrunner 46,52 / Veyric Thunderhame 60,28|||U|||[Sha]; WHL40; req 30 L38; ender Rau Cliffrunner (Thousand Needles) or Veyric|
|96016|The Tempest's Weapo.|30/40|3150|Veyric Thunderhame 60,28|Bath'rah the Windwatcher 80,67|||N|||[Sha]|
|96135|Heed My Call|30/40|3150|Veyric Thunderhame 60,28|=|||N|||[Sha]; GRP|
|96264|Elemental Aid|30/33|2650|Veyric Thunderhame 60,28|=|||N|||[Sha]|
|78830|Terror of the Deser.|26/40|3900|Hemet Nesingwary 36,11|=|||U|||[Hun]; Hunter; Stranglethorn (Hemet Nesingwary 35.7,10.8); objective item from Gharrik in Badlands; req 26 L40 (outside route zones)|
|78114|Wild Wyvern Wrangli.|1/25|2000|?|?|||-|||[Hun]; no giver; no ender; Hunter class sort -261; req 1 in data; no giver/ender in files; Wowhead tooltip 404 (no text); not placeable|

### Wetlands
|id|name|req/L|xp|giver|ender|pre|next|st|T|D|notes|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Menethil**: 35 rows, open class-free XP 48,155 (+1 unk)|||||||||||dungeon starts (sec 1): 98815>Excavation, 95647>Excavation|
|943|The Absent Minded P.|15/24|2400|Archaeol. Flagongut 11,60|=|942||U|T29|||
|98282|Alchemical Hazards|20/22|1750|Caitlin Grassman 12,59|=|||N|T29||noHu?|
|98190|A Friend of the Fam.|20/25|?|Captain Stoutfist 10,57|Highlord Bolvar Fordragon 80,38 [SW]|||N|T29||noHu?|
|98230|This Land Was Their.|22/29|1200|"|Howin Kindfeather 49,42|||N||||
|98221|From the Ashes|23/28|2300|"|=|||N|T29||noHu?|
|465|Nek'rosh's Gambit|23/31|1900|"|obj:Dragonmaw Catapult 47,47 / obj:Dragonmaw Catapult 47,47|464|474|U|T29|||
|464|War Banners|23/28|2300|"|=||465|-|T29|||
|463|The Greenwarden|20/21|830|First Mate Fitzsimmons 11,60|Rethiel the Greenwarden 56,40||276|-|T29|||
|290|Lifting the Curse|22/30|1200|"|obj:Intrepid's Locked Strongbox 14,24|289|292|-|T29|||
|289|The Cursed Crew|22/29|1750|"|=|288|290|-|T29|||
|288|The Third Fleet|22/27|220|"|=||289|-|T29|||
|322|Blessed Arm|20/29|1200|Glorin Steelbrow 11,61|Grimand Elmore 60,34 [SW]|324|325|-|T31|||
|526|Lightforge Ingots|20/29|1750|"|=|324|322|-|||excl:322,324|
|321|Lightforge Iron|20/29|590|"|obj:Waterlogged Chest 12,64|270|324|-|T31|||
|293|Cleansing the Eye|22/30|2450|"|Archbishop Benedictus 50,45 [SW]|292||-|T31|||
|472|Fall of Dun Modr|25/25|1200|Harlo Barnaby 11,56|Longbraid the Grim 50,18|||U|T29||WHL30|
|471|Apprentice's Duties|18/26|2100|James Halloran 9,56|=|484||-|T29|||
|484|Young Crocolisk Ski.|18/22|1750|"|=||471|U|T29|||
|98240|Crimson Crate Deliv.|19/29|1200|"|Howin Kindfeather 49,42|||N||||
|98072|Crocs of the Sky|19/27|2200|"|=|||N|T29||noHu?|
|279|Claws from the Deep|20/22|1750|Karl Boran 8,59|=||281|-|T29|||
|281|Reclaiming Goods|20/25|510|"|obj:Damaged Crate 14,41|279|284|-|T29|||
|98189|Return the Statuette|20/25|200|"|Captain Stoutfist 10,57|||N|T29||noHu?|
|1249|The Missing Diplomat|28/33|1300|Mikhail 11,61|=|1248|1250|-|||ESC?|
|1264|"|28/33|1300|"|Cmdr Samaul 68,49 [DU]|1250|1265|-||||
|1132|Fiora Longears|30/30|1200|Red Jack Flint 10,58|Fiora Longears 66,45 [DU]||1133|U||||
|470|Digging Through the.|19/24|2400|Sida 12,58|=|||-|T29|||
|98208|Bloom of the Heavens|22/29|2350|Sylessa Duskwhisper 8,56|=|||N|T29||noHu?|
|98209|"|22/29|1200|"|Thundris Windweaver 37,40 [DS]|||N|||noHu?|
|1250|The Missing Diplomat|28/33|265|Tapoke "Slim" Jahn 11,60|Mikhail 11,61|1249|1264|U||||
|305|In Search of The Ex.|21/24|970|Tarrel Rockweaver 12,52|Merrin Rockweaver 39,52||306|U|T29|||
|98197|Spoils of War|18/22|1750|Valstag Ironjaw 10,57|=|||N|T29||noHu?|
|473|Report to Captain S.|23/28|230|"|Captain Stoutfist 10,57|455|464|-||||
|1302|James Hyal|30/35|690|Vincent Hyal 11,60|Clerk Lendry 68,48 [DU]|||-||||
|324|The Lost Ingots|20/29|1750|obj:Waterlogged Chest 12,64|Glorin Steelbrow 11,61|321|322|-|T31|||
|**Dun Modr**: 11 rows, open class-free XP 25,440|||||||||||dungeon starts (sec 1): 378>Stockade|
|274|A Dark Threat Looms|16/18|340|Ashlan Stonesmirk 50,18|Chief Engineer Hinderweir VII 46,14 [LM]|161|278|-||L||
|88756|Bring Back a Bang|27/32|2550|"|=|||N|||GRP; noHu?|
|87491|Spark of Freedom|27/32|2550|Captive Fire Elemental 46,17|Roggo Harlbarrow 50,18|||N|||GRP|
|87318|Hearts of the Lost|28/33|2650|Comar Villard 50,13|Essene Villard 52,9|||N|||GRP|
|88757|Accessories of the .|28/33|2650|Essene Villard 52,9|=|||N|||GRP|
|88758|Sentiments of the L.|28/33|2650|"|Comar Villard 50,13|||N|||GRP|
|304|A Grim Task|26/34|3350|Longbraid the Grim 50,18|=|||U|T31o||GRP|
|303|The Dark Iron War|25/30|2450|Motley Garmason 50,18|=||378|-|T31o||GRP; ELITE:Dark Iron Dwarf L27; Dark Iron Tunneler L29|
|634|Plea To The Alliance|28/31|1250|Rhag Garmason 50,18|Captain Nials 46,48 [AR]|633||U|T29|||
|631|The Thandol Span|28/31|2500|"|obj:Ebenezer Rustlocke's Corpse 51,8||632|U|T29||GRP; WHreq26|
|633|"|28/31|2500|"|=|632|634|U|T29||WHreq26|
|**Whelgar**: 8 rows, open class-free XP 16,135 (+1 unk)|||||||||||dungeon starts (sec 1): 98824>Excavation|
|306|In Search of The Ex.|21/24|485|Merrin Rockweaver 39,52|Tarrel Rockweaver 12,52|305||U|T29|||
|294|Ormer's Revenge|22/24|1950|Ormer Ironbraid 38,51|=||295|-|T29|||
|295|"|22/27|2200|"|=|294|296|U|T29|||
|296|"|22/29|2950|"|=|295||U|T29|||
|299|Uncovering the Past|22/27|2200|Prospector Whelgar 39,52|=|||U|T29|||
|98216|Understanding Our P.|23/31|3150|"|=|||N|||GRP|
|98313|For Further Study|24/32|?|"|Historian Karnik 78,12 [IF]|||N||||
|98310|Gleaning Our Future|24/32|3200|"|=|||N|||GRP|
|**Dun Algaz road**: 6 rows, open class-free XP 13,980||||||||||||
|469|Daily Delivery|18/21|830|Einar Stonegrip 50,39|James Halloran 9,56|||-||||
|98245|Razormaw Needling|21/29|2350|Howin Kindfeather 49,42|=|||N|T29||noHu?|
|98246|Trying Times|21/29|2350|"|=|||N|T29||noHu?|
|98291|Death to the Dragon.|22/30|3050|"|=|||N|||GRP|
|98297|Stopping the Cycle|24/34|2700|"|=|||N|||GRP|
|98300|Word to Ironforge|24/34|2700|"|King Magni Bronzebeard 39,56 [IF]|||N||||
|**Greenwarden**: 4 rows, open class-free XP 8,800|||||||||||dungeon starts (sec 1): 95646>Excavation|
|275|Blisters on The Land|20/26|2650|Rethiel the Greenwarden 56,40|=|277||U||||
|277|Fire Taboo|20/23|1850|"|=|276|275|-|T29|||
|276|Tramping Paws|20/21|1250|"|=||277|-|T29|||
|98283|Carnage|22/30|3050|"|=|||N|||GRP|
|**Hervdana**: 4 rows, open class-free XP 0||||||||||||
|**Field NPCs**: 8 rows, open class-free XP 13,560||||||||||||
|284|The Search Continues|20/25|510|obj:Damaged Crate 14,41|obj:Sealed Barrel 14,38|281|285|-|T29|||
|98293|Forced Disarmament|22/30|3050|obj:Dragonmaw Armaments 59,45|Captain Stoutfist 10,57|||N|||GRP|
|474|Defeat Nek'rosh|23/32|2550|obj:Dragonmaw Catapult 47,47 / obj:Dragonmaw Catapult 47,47|Captain Stoutfist 10,57|465||U|T31o||GRP|
|632|The Thandol Span|28/31|2500|obj:Ebenezer Rustlocke's Corpse 51,8|Rhag Garmason 50,18|631|633|U|T29||WHreq26|
|286|Return the Statuette|20/25|1500|obj:Half-buried Barrel 14,35|Karl Boran 8,59|285||-|T29|||
|292|The Eye of Paleth|22/30|1200|obj:Intrepid's Locked Strongbox 14,24|Glorin Steelbrow 11,61|290|293|-|T31|||
|285|Search More Hovels|20/25|1000|obj:Sealed Barrel 14,38|obj:Half-buried Barrel 14,35|284|286|-|T29|||
|98223|Old Habits|23/31|1250|obj:Tattered Spellbook 54,55|Captain Stoutfist 10,57|||N||||

### Duskwood
|id|name|req/L|xp|giver|ender|pre|next|st|T|D|notes|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Darkshire**: 45 rows, open class-free XP 58,305|||||||||||dungeon starts (sec 1): 377>Stockade|
|173|Worgen in the Woods|23/28|1150|Calor 76,48|=||221|-|T30|||
|221|"|23/29|1750|"|=|173|222|-|T30|||
|222|"|23/31|1900|"|=|221|223|-||||
|223|"|23/31|3150|"|Jonathan Carevin 75,49|222||-|T32|||
|93|Dusky Crab Cakes|17/20|780|Chef Grual 74,43|=|5|240|-|T24|||
|240|Return to Jitters|17/20|780|"|Jitters 18,56|93||-|T26|||
|266|Inquire at the Inn|20/25|200|Clerk Daltry 73,47|Tavernkeep Smitts 74,44|265|453|-|T30|||
|67|The Legend of Stalv.|22/28|1150|"|obj:Old Footlocker 42,67 [WF]|66|68|-|T24|||
|69|"|22/28|570|"|Innkeeper Farley 44,66 [EL]|68|70|-|T24|||
|97|"|22/28|230|"|Cmdr Althea Ebonlocke 74,47|80|98|-|T26|||
|1042|The Carevin Family|25/30|245|"|Jonathan Carevin 75,49|1041|1043|-||||
|56|The Night Watch|18/24|1450|Cmdr Althea Ebonlocke 74,47|=||57|-|T24|||
|57|"|18/26|2100|"|=|56|58|-|T30|||
|58|"|18/30|2450|"|=|57||-|T30|||
|80|The Legend of Stalv.|22/28|230|"|Clerk Daltry 73,47|79|97|-|T26|||
|98|"|22/35|4100|"|Madame Eva 76,45|97||U||||
|228|Mor'Ladim|28/35|2050|"|=|227|229|-|||GRP|
|229|The Daughter Who Li.|28/35|275|"|Watcher Ladimore 74,48|228|231|-||||
|164|Deliveries to Sven|17/23|920|Elaine Carevin 75,49|Sven Yorgen 8,34||95|-|T24|||
|163|Raven Hill|17/20|390|"|Jitters 18,56||5|-|T24|||
|165|The Hermit|17/25|1000|"|Abercrombie 28,31||148|-|T24|||
|1044|Answered Questions|25/30|3050|Jonathan Carevin 75,49|Thyn'tel Bladeweaver 62,39 [DN]|1043||-||||
|1043|The Scythe of Elune|25/30|2450|"|=|1042|1044|-||||
|146|Messenger to Darksh.|18/18|340|Lord Ello Ebonlocke 72,46|Magistrate Solomon 25,44 [RR]|145||-||||
|253|Bride of the Embalm.|20/30|3650|"|=|252||U|||GRP|
|251|Translate Abercromb.|20/30|245|"|Sirra Von'Indi 73,48|160|401|-||||
|101|The Totem of Inflic.|18/25|2550|Madame Eva 76,45|=|||-|T24|||
|157|Deliver the Thread|20/24|1450|"|Abercrombie 28,31|154|158|-|T24|||
|149|Ghost Hair Thread|20/24|485|"|Blind Mary 82,59|148|154|-|T24|||
|265|The Shadowy Search .|20/25|200|"|Clerk Daltry 73,47|262|266|-|T30|||
|66|The Legend of Stalv.|22/28|230|"|Clerk Daltry 73,47||67|-|T24|||
|96139|The Valor Family|18/22|1750|Sirra Von'Indi 73,48|=|||N|T24||noHu?|
|252|Translation to Ello|20/30|245|"|Lord Ello Ebonlocke 72,46|401|253|-||||
|401|Wait for Sirra to F.|20/30|1850|"|=|251|252|-||||
|227|Morgan Ladimore|28/35|275|"|Cmdr Althea Ebonlocke 74,47|225|228|-|T30|||
|453|Finding the Shadowy.|20/25|1000|Tavernkeep Smitts 74,44|Jitters 18,56|266|268|-|T30|||
|156|Gather Rot Blossoms|20/24|970|"|=|158|159|-|T30|||
|159|Juice Delivery|20/24|970|"|Abercrombie 28,31|156|133|-|T30|||
|79|The Legend of Stalv.|22/28|230|"|Cmdr Althea Ebonlocke 74,47|78|80|-|T26|||
|174|Look To The Stars|20/25|2000|Viktori Prism'Antras 80,48|=||175|U|T24|||
|175|"|20/25|1000|"|Blind Mary 82,59|174|177|U|T24|||
|181|"|20/30|2450|"|=|177||U|T24|||
|1244|The Missing Diplomat|28/30|2450|Watcher Backus 75,44|=|1243|1245|-|T32|||
|1245|"|28/30|245|"|Elling Trias 66,74 [SW]|1244|1246|-||||
|231|A Daughter's Love|28/35|1350|Watcher Ladimore 74,48|obj:A Weathered Grave 18,29|229||U||||
|**Raven Hill**: 2 rows, open class-free XP 900||||||||||||
|5|Jitters' Growling G.|17/20|390|Jitters 18,56|Chef Grual 74,43||93|-|T24|||
|268|Return to Sven|20/25|510|"|Sven Yorgen 8,34|453|323|-|T30|||
|**Sven**: 6 rows, open class-free XP 9,500||||||||||||
|226|Wolves at Our Heels|19/21|1250|Lars 8,33|=|||-|T24|||
|55|Morbent Fel|20/32|3850|Sven Yorgen 8,34|=|325||-|T32o||GRP; ELITE:Morbent Fel L32|
|323|Proving Your Worth|20/28|2300|"|=|268|269|-|T30|||
|269|Seeking Wisdom|20/29|590|"|Bishop Farthing 50,46 [SW]|323|270|-|T30|||
|95|Sven's Revenge|20/25|1000|"|obj:Mound of loose dirt 50,78||230|-|T24|||
|262|The Shadowy Figure|20/25|510|"|Madame Eva 76,45|230|265|-|T30|||
|**Abercrombie**: 6 rows, open class-free XP 4,430||||||||||||
|133|Ghoulish Effigy|20/27|1650|Abercrombie 28,31|=|159|134|-|T30|||
|160|Note to the Mayor|20/30|610|"|Lord Ello Ebonlocke 72,46|134|251|-||||
|134|Ogre Thieves|20/30|1200|"|=|133|160|-|T30|||
|148|Supplies from Darks.|20/24|485|"|Madame Eva 76,45||149|-|T24|||
|158|Zombie Juice|20/24|485|"|Tavernkeep Smitts 74,44|157|156|-|T30|||
|254|Digging Through the.|20/35|?|obj:Eliza's Grave Dirt 29,31|=|||-|||REPT|
|**Nightmare camp**: 18 rows, open class-free XP 0||||||||||||
|81730-81747|Duskwood Missions I-XVIII (18 quests in one row)|23/27|XP by mission: 2200: I,II,III,X,XI,XII,XIII,XIV,XV; 1650: IV,V,VI,VII,VIII,IX,XVI,XVII,XVIII|Field Captain Palandar 46,49|=|||-|||DAILY; GRP; each ends at the giver|
|**Twilight Grove**: 1 rows, open class-free XP 1,250||||||||||||
|245|Eight-Legged Menaces|17/21|1250|Watcher Dodds 45,67|=|||-|T24|||
|**Brightwood**: 2 rows, open class-free XP 1,695||||||||||||
|177|Look To The Stars|20/25|1500|Blind Mary 82,59|Viktori Prism'Antras 80,48|175|181|U|T24|||
|154|Return the Comb|20/24|195|"|Madame Eva 76,45|149|157|-|T24|||
|**Field NPCs**: 2 rows, open class-free XP 1,690||||||||||||
|225|The Weathered Grave|28/35|690|obj:A Weathered Grave 18,29|Sirra Von'Indi 73,48||227|-|T30|||
|230|Sven's Camp|20/25|1000|obj:Mound of loose dirt 50,78|Sven Yorgen 8,34|95|262|-|T30|||
|**Item/drop starts**: 2 rows, open class-free XP 3,800||||||||||||
|337|An Old History Book|20/25|1500|item:An Old History Book|Milton Sheaf 77,30 [SW]||538|-|||item start (drop: Flesh Eater, Skeletal Warrior)|
|96138|Merrick's Bow|18/28|2300|item:Merrick's Bow|Sirra Von'Indi 73,48|||N|||item start (drop: Lost Watcher)|
|**Giver not in files**: 1 rows, open class-free XP 2,200||||||||||||
|98447|The Valor Family|18/27|2200|?|?|||N|||no giver; no ender; txt: The Valor Family / Find the cause of the Valor family ghosts in Raven Hill for Sirra Von'.|

### Redridge (20-27 leftovers: not turned in during 1-20, req<=27)
|id|name|req/L|xp|giver|ender|pre|next|st|T|D|notes|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Lakeshire**: 16 rows, open class-free XP 27,700|||||||||||dungeon starts (sec 1): 386>Stockade, 95772>Excavation|
|91|Solomon's Law|17/23|1850|Bailiff Conacher 25,44|=|||-|T22|L||
|150|Murloc Poachers|20/20|1550|Dockmaster Baren 23,47|=|||-|T22|L||
|347|Rethban Ore|20/24|970|Foreman Oslow 27,49|Brother Paxton 50,40 [EL]|345|346|-||||
|128|Blackrock Bounty|20/25|2000|Guard Howe 26,58|=|||-|T26|||
|143|Messenger to Westfa.|14/14|490|Magistrate Solomon 25,44|Gryan Stoutmantle 56,48 [WF]|121|144|-|T22|L||
|145|Messenger to Darksh.|18/18|1000|"|Lord Ello Ebonlocke 72,46 [DW]|144|146|-|T26|||
|115|Shadow Magic|18/23|2300|Marshal Marris 28,49|=|20D||-|T22|aL|GRP|
|19|Tharil'zun|18/25|2550|"|=|20D||-|T22|aL|GRP|
|34|An Unwelcome Guest|18/24|1950|Martie Jainrose 17,46|=|||-|T26|||
|118|The Price of Shoes|14/18|340|Verner Osgood 26,47|Smith Argus 42,66 [EL]||119|-|T20|aL||
|122|Underbelly Scales|14/18|1700|"|=|119||-||L||
|124|A Baying of Gnolls|15/20|1150|"|=|119|126|-|T22|L||
|126|Howling in the Hills|15/25|2000|"|=|124||-|T26|L||
|169|Wanted: Gath'Ilzogg|15/26|2650|obj:Wanted: Gath'Ilzogg 25,46|Magistrate Solomon 25,44|||U|T26||GRP|
|95999|WANTED: Incinerator.|16/25|2550|obj:Wanted: Incinerator Gar'im 24,46|Magistrate Solomon 25,44|||N|T26o||GRP; noHu?|
|180|Wanted: Lieutenant .|15/26|2650|obj:Wanted: Lieutenant Fangore 22,46|Magistrate Solomon 25,44|||U|T26|||
|**Keeshan**: 1 rows, open class-free XP 2,550||||||||||||
|219|Missing In Action|19/25|2550|Corporal Keeshan 23,13|Marshal Marris 28,49|||-||L|ESC?|
|**Field NPCs**: 1 rows, open class-free XP 1,300||||||||||||
|248|Looking Further|20/22|1300|obj:Old Lion Statue 79,47|obj:An Empty Jar 58,50|94|249|-|T26o||GRP|
|**Item/drop starts**: 1 rows, open class-free XP 1,400||||||||||||
|178|Theocritus' Retriev.|15/23|1400|item:Glowing Shadowhide Pendant|Theocritus 65,70 [EL]|||-|||item start (drop: Shadowhide Darkweaver, Shadowhide Slayer)|

### Hillsbrad Foothills
|id|name|req/L|xp|giver|ender|pre|next|st|T|D|notes|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Southshore**: 25 rows, open class-free XP 54,750|||||||||||dungeon starts (sec 1): 1053>SM|
|98463|Talk of the Town|28/33|265|Barkeep Kelly 52,59|Nixxrax Fillamug 27,77 [STV]|||N|T31|||
|565|Bartolo's Yeti Fur .|29/34|2700|Bartolo Ginsetti 49,56|=|||-||||
|98071|Brewer's Trade|23/27|2200|Brewmeister Bilger 52,59|=|||N|T31|||
|98059|Hillsbrad's Hoard|23/27|2200|Captain McManus 46,50|=|||N||||
|555|Soothing Turtle Bis.|28/31|2500|Chef Jessen 52,59|=|||-||||
|564|Costly Menace|30/34|2700|Darren Malvew 52,56|=|||-|T34|||
|92432|An Alarming Request|30/33|660|Emissary Jacques 48,60|Image of Archmage Modera 69,45 [SP]|||N||||
|536|Down the Coast|25/30|1850|Lieutenant Farren Orinelle 51,58|=||559|-|T31|||
|559|Farren's Proof|25/32|2550|"|=|536|560|-|T31|||
|560|"|25/32|255|"|Marshal Redpath 49,59|559|561|-|T31|||
|563|Reassignment|25/32|3200|"|Major Samuelson 76,37 [SW]|562||-|T31|||
|562|Stormwind Ho!|25/32|1950|"|=|561|563|-|T31|||
|540|Preserving Knowledge|20/38|3550|Loremaster Dibbs 51,57|=|538|542|-|||GRP|
|542|Return to Milton|20/38|3550|"|Milton Sheaf 77,30 [SW]|540||-||||
|554|Stormpike's Deciphe.|28/40|1550|"|Prospector Stormpike 75,12 [IF]|551||-||||
|514|Letter to Stormpike|30/34|1350|"|Prospector Stormpike 75,12 [IF]|511|525|-|T34|||
|512|Noble Deaths|26/36|2800|Magistrate Henry Maleb 48,59|=|510||-||||
|505|Syndicate Assassins|26/33|1950|"|=|||-|T34|||
|523|Baron's Demise|30/40|3900|"|=|522||-||||
|537|Dark Council|30/40|3150|"|=|525||-||||
|561|Farren's Proof|25/32|255|Marshal Redpath 49,59|Lieutenant Farren Orinelle 51,58|560|562|-|T31|||
|500|Crushridge Bounty|30/36|3500|"|=||504|-||||
|504|Crushridge Warmonge.|30/40|4700|"|=|500||U|||GRP; ELITE:Crushridge Warmonger L39|
|659|Hints of a New Plag.|30/33|1300|Phin Odelic 50,59|Quae 60,54 [AR]||658|-|T31|||
|98459|A Lack of Virtue|18/21|165|Tom "Half-fish" Wilson 51,66|Bart Tidewater 9,59 [WL]|||N||||

### Alterac Mountains
|id|name|req/L|xp|giver|ender|pre|next|st|T|D|notes|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Field NPCs**: 5 rows, open class-free XP 4,650|||||||||||dungeon starts (sec 1): 96800>SM|
|8404|Fight for Warsong G.|20/29|1200|Alliance Brigadier General 39,82|=|8372!, 8399!||U|||REPT|
|8405|"|30/39|1500|"|=|8372!, 8399!, 8400!||U|||REPT|
|96137|Ira's Dagger|18/24|1950|Bath'rah the Windwatcher 80,67 / item:Ira's Dagger|Sirra Von'Indi 73,48 [DW]|||N||||
|510|Foreboding Plans|26/34|1350|obj:Syndicate Documents (no pos) / obj:Syndicate Documents (no pos) +1|Magistrate Henry Maleb 48,59 [HB]||512|-|T34|||
|511|Encrypted Letter|30/34|1350|"|Loremaster Dibbs 51,57 [HB]||514|-|T34|||
|**Item/drop starts**: 2 rows, open class-free XP 1,490||||||||||||
|522|Assassin's Contract|30/38|710|item:Assassin's Contract|Magistrate Henry Maleb 48,59 [HB]||523|-|||item start (drop: Shadowy Assassin)|
|551|The Ensorcelled Par.|30/40|780|item:Ensorcelled Parchment|Loremaster Dibbs 51,57 [HB]||554|-|||item start (source ?)|
|**Giver not in files**: 1 rows, open class-free XP 265||||||||||||
|93689|Friend of the Kirin.|24/33|265|?|?|||?|||no giver; no ender; txt: Friend of the Kirin Tor / Speak with Archmage Celindra in the City of Dalaran.|

### Ashenvale
|id|name|req/L|xp|giver|ender|pre|next|st|T|D|notes|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Astranaar**: 14 rows, open class-free XP 23,180|||||||||||dungeon starts (sec 1): 95737>Excavation|
|1056|Journey to Stonetal.|18/18|680|Faldreas Goeth'Shael 36,49|Keeper Albagorm 37,8 [ST]||1057|-|T27|||
|1033|Elune's Tear|20/22|1750|Pelturas Whitemoon 37,52|=|1020|1034|-|T23|||
|1035|Fallen Sky Lake|20/30|3050|"|=|1034||-|T34|||
|1034|The Ruins of Stardu.|20/23|1850|"|=|1033|1035|-|T27|||
|1025|An Aggressive Defen.|18/24|1950|Raene Wolfrunner 37,50|=|1023||-|T27|||
|1054|Culling the Threat|18/25|2000|"|=|||-|T27|||
|991|Raene's Cleansing|18/19|1450|"|Teronis' Corpse 20,42||1023|-|T23|||
|1024|"|18/21|830|"|Shael'dryn 54,46|1023|1026|-|T27|||
|1030|"|18/28|1700|"|Krolg 51,75|1029|1045|-||||
|1070|On Guard in Stoneta.|17/21|830|Sent. Thenysil 35,50|Kaela Shadowspear 60,67 [ST]||1085|-|T23|||
|1081|Reception from Tyra.|17/28|3400|"|Tyrande Whisperwind 39,82 [DN]|1082||-||||
|1008|The Zoram Strand|14/19|1450|Shindrell Swiftfire 35,49|=||1134|-|T23|||
|1134|Pridewings of Stone.|18/21|1650|"|=|1008||-|T23|||
|4581|Kayneth Stillwind|24/29|590|"|Kayneth Stillwind 85,45|||-|T27,T34|||
|**Forest Song**: 8 rows, open class-free XP 13,350||||||||||||
|970|The Tower of Althal.|13/21|1650|Delgren the Purifier 26,39|=|967|973|-|T23|||
|973|"|13/24|1950|"|=|970|1140|-|T23|||
|1140|"|13/28|2300|"|=|973|1167|-||||
|1167|"|13/28|570|"|Balthule Shadowstrike 55,25 [DS]|1140|1143|-||||
|976|Supplies to Auberdi.|19/24|2900|Feero Ironhand 26,39|Delgren the Purifier 26,39|973||-|||ESC?|
|1010|Bathran's Hair|20/20|780|Orendil Broadleaf 26,39|=||1020|-|T23|||
|1020|Orendil's Cure|20/20|1950|"|Pelturas Whitemoon 37,52|1010|1033|-|T23|||
|1023|Raene's Cleansing|18/21|1250|Teronis' Corpse 20,42|Raene Wolfrunner 37,50|991|1024|-|T23|||
|**Talen**: 2 rows, open class-free XP 3,700||||||||||||
|1007|The Ancient Statuet.|19/20|1150|Talen 15,31|=||1009|-|T23|||
|1009|Ruuzel|20/25|2550|"|=|1007||-|T23|||
|**Illiyana**: 4 rows, open class-free XP 8,160||||||||||||
|1032|Satyr Slaying!|26/32|2550|Illiyana 22,53|=|1031||-||||
|1021|Vile Satyr! Dryads .|26/32|2550|"|Anilia 78,45||1031|-|T34|||
|1022|The Howling Vale|25/30|2450|Sent. Melyria Frostshadow 22,53|=||1037|-|T34|||
|1037|Velinde Starsong|25/30|610|"|Thyn'tel Bladeweaver 62,39 [DN]|1022|1038|-|T34|||
|**Shael'dryn**: 5 rows, open class-free XP 6,660||||||||||||
|1026|Raene's Cleansing|18/27|2200|Shael'dryn 54,46|=|1024|1027|-|T27|||
|1027|"|18/28|2300|"|=|1026|1028|-|T34|||
|1028|"|18/28|1700|"|obj:Hidden Shrine 56,49|1027|1055|-|T34|||
|1029|"|18/28|230|"|Raene Wolfrunner 37,50|1055|1030|-||||
|1055|"|18/28|230|obj:Hidden Shrine 56,49|Shael'dryn 54,46|1028|1029|-||||
|**Ash south**: 8 rows, open class-free XP 20,200||||||||||||
|78132|Dragonslayer's Helm|15/25|2550|Alonso 43,70|=|||U||||
|78134|Dragonslayer's Lance|15/25|2550|"|=|||U||||
|78133|Dragonslayer's Shie.|15/25|2550|"|=|||U||||
|1045|Raene's Cleansing|18/30|2450|Krolg 51,75|=|1030|1046|U||||
|1046|"|18/30|3050|"|Raene Wolfrunner 37,50|1045||U||||
|1016|Elemental Bracers|20/24|1950|Sent. Velene Starstrike 50,67|=||1017|-||||
|1017|Mage Summoner|20/25|2550|"|=|1016||-||||
|86757|Slowing the Orc Adv.|27/32|2550|Shandrina 49,67|=|||N||||
|**Ash SE**: 5 rows, open class-free XP 2,620||||||||||||
|7863|Sentinel Basic Care.|25/34|270|Illiyana Moonblaze 61,84|=|||-|||excl:7864,7865|
|8289|Talismans of Merit|10/15|?|Sent. Farsong 62,84|=|||?|||REPT|
|7921|"|20/25|?|"|=|||?|||REPT|
|7887|"|30/35|?|"|=|||?|||REPT|
|98027|Gleaming Crescent N.|25/29|2350|obj:Gleaming Crescent Pendant 63,72|Maliynn 37,50|||N||||
|**Ash east**: 5 rows, open class-free XP 13,000||||||||||||
|1031|The Branch of Cenar.|26/32|2550|Anilia 78,45|Illiyana 22,53|1021|1032|-|T34|||
|1011|Forsaken Diseases|24/29|2350|Kayneth Stillwind 85,45|=||1012|-||||
|1012|Insane Druids|24/32|3200|"|=|1011||U||||
|98418|Shared Fury|23/30|2450|Maseara Autumnmoon 86,46|=|||N||||
|98417|Vengeful Trail|23/30|2450|"|=|||N||||
|**Giver not in files**: 1 rows, open class-free XP 2,750||||||||||||
|908|Amongst the Ruins|25/27|2750|?|?|||-|||GRP; no giver; no ender; txt: Amongst the Ruins Level 27 / Bring the Fathom Core to Je'neu Sancrea at Zoram'gar Outpost.|

### Darkshore (leftovers: not turned in during 1-20)
|id|name|req/L|xp|giver|ender|pre|next|st|T|D|notes|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Auberdine**: 9 rows, open class-free XP 5,840 (+1 unk)|||||||||||dungeon starts (sec 1): 1275>BFD, 78926>BFD|
|729|The Absent Minded P.|15/20|1150|Archaeol. Hollee 37,42|Prospector Remtravel 36,84||731|-||||
|741|"|15/20|1150|"|Chief Archaeol. Greywhisker 31,85 [DN]|731|942|-||||
|98461|Unrequited Love|18/21|165|"|Tarrel Rockweaver 12,52 [WL]|||N||8|noHu?|
|79099|Baron Aquanis|25/27|2750|Davius Voidstar 37,44|=|||U|||type62(raid)|
|87760|Holy Diver|15/20|?|Gwennyth Bly'Leggonde 37,46|=|||N||||
|965|The Tower of Althal.|13/18|680|Sent. Elissa Starbreeze 39,44|Balthule Shadowstrike 55,25||966|-||||
|990|Trek to Ashenvale|15/19|365|Sent. Selarin 39,43|Raene Wolfrunner 37,50 [AV]|994, 995||-||||
|986|A Lost Master|10/20|1550|Terenthis 39,43|=|985!(How Big a Threat?)|993|-||||
|993|"|10/20|780|"|Volcor 45,85|986||-||||
|**Darkshore south**: 6 rows, open class-free XP 9,530||||||||||||
|98013|Swelling Forces|12/20|1550|Arbal 44,76|=|||N|||noHu?|
|5321|The Sleeper Has Awa.|17/20|1550|Kerlonian Evershade 44,76|Liladris Moonriver 27,36 [AV]|||U|||ESC?|
|951|Mathystra Relics|12/20|1950|Onu 44,76|=|950!(Return to Onu)||-||||
|731|The Absent Minded P.|15/20|1950|Prospector Remtravel 36,84|Archaeol. Hollee 37,42|729|741|-|||ESC?|
|994|Escape Through Force|10/22|1750|Volcor 45,85|Terenthis 39,43|993|990|-|T23||ESC?; excl:995|
|995|Escape Through Stea.|10/20|780|"|Terenthis 39,43|993|990|-|||ESC?; excl:994|
|**Darkshore north**: 6 rows, open class-free XP 10,050||||||||||||
|966|The Tower of Althal.|13/18|1350|Balthule Shadowstrike 55,25|=|965|967|-||||
|967|"|13/18|1000|"|Delgren the Purifier 26,39 [AV]|966|970|-||||
|981|"|13/31|2500|"|Delgren the Purifier 26,39 [AV]|1143||-||||
|1143|"|13/31|2500|"|=|1167|981|-||||
|2098|Gyromast's Retrieval|14/20|1550|Gelkak Gyromast 57,13|=||2078|-||||
|2078|Gyromast's Revenge|14/20|1150|"|=|2098||U|||GRP; ELITE:The Threshwackonator 4100 L20|
|**Item/drop starts**: 2 rows, open class-free XP 3,600||||||||||||
|968|The Powers Below|10/20|1950|item:Book: The Powers Below|Gerrig Bonegrip 51,6 [IF]|||-|||item start (drop: Twilight Disciple, Twilight Thug)|
|98028|Baron Marinous|17/21|1650|item:Clouded Water Globe|Onu 44,76|||N|||item start (drop: Baron Marinous)|

### Stormwind
|id|name|req/L|xp|giver|ender|pre|next|st|T|D|notes|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**SW Cathedral**: 9 rows, open class-free XP 7,820|||||||||||dungeon starts (sec 1): 95161>RoL, 2923>Gnomer|
|399|Humble Beginnings|10/15|1050|Baros Alexston 58,48|=|||-||||
|97926|Making Do|13/17|125|"|Thundris Windweaver 37,40 [DS]|||N||||
|396|An Audience with th.|16/31|3750|"|Lady Katrana Prestor 80,38|395||-|T30o|||
|389|Bazil Thredd|16/22|435|"|Warden Thelwater 51,69|373D|391|-|T20|a8L||
|393|Shadow of the Past|16/29|590|"|Master Mathias Shaw 78,71|392|350|-|T25|||
|270|The Doomed Fleet|20/29|1200|Bishop Farthing 50,46|Glorin Steelbrow 11,61 [WL]|269|321|-|T30|||
|343|Speaking of Fortitu.|20/24|195|Brother Kristoff 55,54|Milton Sheaf 77,30||344|-||||
|98219|The Shamed Lieutena.|20/30|245|Lord Grayson Shadowbreaker 48,50|Lieutenant Farren Orinelle 51,58 [HB]|||N|||noHu?|
|1274|The Missing Diplomat|28/28|230|Thomas 50,44|Bishop DeLavey 80,44||1241|-|T30|||
|**SW Keep**: 7 rows, open class-free XP 8,855||||||||||||
|1241|The Missing Diplomat|28/28|230|Bishop DeLavey 80,44|Jorgen 76,85|1274|1242|-|T30|||
|543|The Perenolde Tiara|30/40|4700|Count Remington Ridgewell 77,48|=|||-|||GRP|
|98191|A Friend of the Fam.|20/25|200|Highlord Bolvar Fordragon 80,38|Lord Grayson Shadowbreaker 48,50|||N|T30|||
|344|Brother Paxton|20/24|485|Milton Sheaf 77,30|Brother Paxton 50,40 [EL]|343|345|-||||
|538|Southshore|20/38|710|"|Loremaster Dibbs 51,57 [HB]|337|540|-||||
|2746|Items of Some Conse.|16/31|630|Tyrion 73,36|=|2745|434|-|T25|||
|434|The Attack!|16/31|1900|"|Elling Trias 66,74|2746|394|-|T30o||ESC?|
|**SW Dwarven**: 3 rows, open class-free XP 1,640 (+1 unk)|||||||||||dungeon starts (sec 1): 2928>Gnomer|
|97894|Business in Auberdi.|13/17|?|Borgus Steelhand 59,34|Gorbold Steelhand 38,41 [DS]||982!|N|||noHu?|
|353|Stormpike's Delivery|9/15|1050|Grimand Elmore 60,34|Mtn Stormpike 25,18 [LM]|||U||aL||
|325|Armed and Ready|20/29|590|"|Sven Yorgen 8,34 [DW]|322|55|-|T32|||
|**SW Old Town**: 5 rows, open class-free XP 2,380 (+1 unk)|||||||||||dungeon starts (sec 1): 388>Stockade|
|1247|The Missing Diplomat|28/31|250|Dashel Stonefist 74,59|Elling Trias 66,74|1447|1248|-||||
|1447|"|28/31|1250|"|=|1246|1247|-|||ESC?|
|395|Brotherhood's End|16/31|630|Master Mathias Shaw 78,71|Baros Alexston 58,48|394|396|-|T30o|||
|350|Look to an Old Frie.|16/31|250|"|Elling Trias 66,74|393|2745|-|T25|||
|78297|You've Got Yourself.|20/25|?|Master Wood 81,61|Grizzby 62,39 [BA]|||U||||
|**SW Trade**: 6 rows, open class-free XP 2,230|||||||||||dungeon starts (sec 1): 391>Stockade, 387>Stockade|
|2745|Infiltrating the Ca.|16/31|250|Elling Trias 66,74|Tyrion 73,36|350|2746|-|T25|||
|394|The Head of the Bea.|16/31|250|"|Master Mathias Shaw 78,71|434|395|-|T30o|||
|1243|The Missing Diplomat|28/28|230|"|Watcher Backus 75,44 [DW]|1242|1244|-|T30|||
|1246|"|28/31|250|"|Dashel Stonefist 74,59|1245|1447|-||||
|1248|"|28/33|660|"|Mikhail 11,61 [WL]|1247|1249|-||||
|392|The Curious Visitor|16/29|590|Warden Thelwater 51,69|Baros Alexston 58,48|391|393|-|T25|||
|**SW Mage**: 6 rows, open class-free XP 11,430|||||||||||dungeon starts (sec 1): 92489>Dalaran|
|690|Malin's Request|30/32|1950|Archmage Malin 50,87|Skuerto 47,47 [AR]||691|-||||
|1076|Devils in Westfall|17/21|1650|Collin Mauren 53,87|=|1075|1077|-||||
|1078|Retrieval for Mauren|17/26|2100|"|=|||-||||
|1077|Special Delivery fo.|17/21|830|"|Gaxim Rustfizzle 60,67 [ST]|1076||-||||
|335|A Noble Brew|25/30|2450|Zardeth of the Black Claw 40,85|=||336|-|T30|||
|336|"|25/30|2450|"|Lord Baurles K. Wishock 78,49|335|397|-|T32|||
|**SW Park**: 1 rows, open class-free XP 1,450|||||||||||dungeon starts (sec 1): 92456>Dalaran|
|3765|The Corruption Abro.|18/24|1450|Argos Nightwhisper 36,68|Gershala Nightwhisper 38,43 [DS]||1275|-||8||
|**SW Harbor**: 2 rows, open class-free XP 690 (+1 unk)||||||||||||
|1271|Feast at the Blue R.|30/37|?|Angus Stern 52,94|=|1222||-||||
|1301|James Hyal|30/35|690|Connor Rivers 51,96|Vincent Hyal 11,60 [WL]||1302|-||||
|**Field NPCs**: 4 rows, open class-free XP 1,855||||||||||||
|72|The Legend of Stalv.|22/28|230|Caretaker Folsom 43,72|obj:Sealed Crate 42,72|70|74|-|T24|||
|121|Messenger to Stormw.|14/14|245|General Marcus Jonathan 69,83|Magistrate Solomon 25,44 [RR]|120D|143|-|T20|aL||
|1242|The Missing Diplomat|28/28|230|Jorgen 76,85|Elling Trias 66,74|1241|1243|-|T30|||
|74|The Legend of Stalv.|22/28|1150|obj:Sealed Crate 42,72|Marshal Haggard 85,69 [EL]|72|75|-|T24|||
|**Item/drop starts**: 1 rows, open class-free XP 0||||||||||||
|373|The Unsent Letter|16/22|870|item:An Unsent Letter|Baros Alexston 58,48||389|-|T20|D|item start (drop: Edwin VanCleef)|

### Ironforge
|id|name|req/L|xp|giver|ender|pre|next|st|T|D|notes|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**IF Cavern**: 5 rows, open class-free XP 9,500|||||||||||dungeon starts (sec 1): 971>BFD, 78923>BFD|
|735|The Star, the Hand .|30/44|5600|Gerrig Bonegrip 51,6|=|727|737|-|||GRP|
|737|Forbidden Knowledge|30/40|2350|Gerrig Bonegrip 51,6 / Keeper Bel'dugur 54,54 [UC]|Theldurin the Lost 51,77 [BL]|735, 736!(The Star, the Han.)||-||||
|687|Theldurin the Lost|30/40|1550|Gerrig Bonegrip 51,6 / Zaruk 75,36 [AR]|Theldurin the Lost 51,77 [BL]|653, 688!(Myzrael's Allies)|692|-||||
|**IF Explorers**: 2 rows, open class-free XP 2,060|||||||||||dungeon starts (sec 1): 1050>SM|
|525|Further Mysteries|30/34|1350|Prospector Stormpike 75,12|Magistrate Henry Maleb 48,59 [HB]|514|537|-|T34|||
|707|Ironband Wants You!|30/37|710|"|Prospector Ironband 66,66 [LM]||738|-||||
|**IF Tinkertown**: 2 rows, open class-free XP 2,480|||||||||||dungeon starts (sec 1): 2922>Gnomer, 2927>Gnomer, 2924>Gnomer, 2930>Gnomer, 2929>Gnomer|
|1073|Ineptitude + Chemic.|17/21|1650|Lomac Gearstrip 72,52|=|1072|1074|-||||
|1074|"|17/21|830|"|Gaxim Rustfizzle 60,67 [ST]|1073||-||||
|**IF Military**: 1 rows, open class-free XP 2,450||||||||||||
|1179|The Brassbolts Brot.|28/30|2450|Pilot Longbeard 73,94|Wizzle Brassbolts 78,77 [TN]|||-|T31,T33|||
|**IF Mystic**: 1 rows, open class-free XP 1,200||||||||||||
|686|A King's Tribute|25/30|1200|King Magni Bronzebeard 39,56|Grand Mason Marblesten 39,88|683|689|-|T31,T33|||
|**Field NPCs**: 5 rows, open class-free XP 10,250||||||||||||
|689|A King's Tribute|25/31|2500|Grand Mason Marblesten 39,88|=|686|700|-|T31,T33|||
|700|"|25/31|2500|"|King Magni Bronzebeard 39,56|689||-|T33|||
|1453|Reclaimers' Busines.|30/33|1300|Roetten Stonehammer 70,21|Kreldig Ungor 66,10 [Desolace]|||-|T34|||
|683|Sara Balloo's Plea|25/30|1200|Sara Balloo 64,67|King Magni Bronzebeard 39,56|637|686|-|T31,T33|||
|2948|Gnome Improvement|28/35|2750|Talvash del Kissel 36,4|=|2947||-||||
|**Item/drop starts**: 1 rows, open class-free XP 2,450||||||||||||
|637|Sully Balloo's Lett.|25/30|2450|item:Waterlogged Envelope|Sara Balloo 64,67||683|-|T29||item start (source ?)|

### Loch Modan (leftovers)
|id|name|req/L|xp|giver|ender|pre|next|st|T|D|notes|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Thelsamar**: 4 rows, open class-free XP 4,825||||||||||||
|86776|Ingredients for the.|15/30|2450|Morhan Coppertongue 34,47|=|||N||||
|468|Report to Mountaine.|19/21|165|Mtn Kadrell 33,50|Mtn Rockgar 25,10||455|-||||
|467|Stonegear's Search|20/23|460|Mtn Kadrell 33,50 / Pilot Longbeard 73,94 [IF]|Pilot Stonegear 50,49 [DM]||466|-||||
|256|WANTED: Chok'sul|17/22|1750|obj:WANTED 37,47|Magistrate Bluntnose 35,44|||U||L|GRP|
|**LM Dam**: 8 rows, open class-free XP 6,610||||||||||||
|161|A Dark Threat Looms|16/18|1350|Chief Engineer Hinderweir VII 46,14|Ashlan Stonesmirk 50,18 [WL]|199|274|-||L||
|250|"|16/18|680|"|obj:Suspicious Barrel 56,13||199|-||L||
|278|"|16/18|1350|"|=|274|280|-||L|GRP|
|280|"|16/18|680|"|obj:Explosive Charge 51,14|278|283|-||L||
|79975|Eagle's Fist|14/32|2550|obj:Carved Figurine 49,13|obj:Messenger Bag 22,24 [AR]|||U||||
|**Stormpike post**: 1 rows, open class-free XP 1,250||||||||||||
|455|The Algaz Gauntlet|19/21|1250|Mtn Rockgar 25,10|Valstag Ironjaw 10,57 [WL]||473|-||||
|**Ironband**: 2 rows, open class-free XP 4,300||||||||||||
|704|Agmond's Fate|30/38|2850|Prospector Ironband 66,66|=|739||U||||
|738|Find Agmond|30/38|1450|"|obj:Battered Dwarven Skeleton 51,62 [BL]||739|-||||
|**Field NPCs**: 2 rows, open class-free XP 3,300||||||||||||
|283|A Dark Threat Looms|16/20|1950|obj:Explosive Charge 51,14|Chief Engineer Hinderweir VII 46,14|280||-||L||
|199|"|16/18|1350|obj:Suspicious Barrel 56,13|Chief Engineer Hinderweir VII 46,14|250|161|-||L||

### Westfall (leftovers)
|id|name|req/L|xp|giver|ender|pre|next|st|T|D|notes|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Sentinel**: 1 rows, open class-free XP 245||||||||||||
|144|Messenger to Westfa.|14/14|245|Gryan Stoutmantle 56,48|Magistrate Solomon 25,44 [RR]|143|145|-|T24|L||
|**WF south**: 2 rows, open class-free XP 1,700||||||||||||
|68|The Legend of Stalv.|22/28|1700|obj:Old Footlocker 42,67|Clerk Daltry 73,47 [DW]|67|69|-|T24|||
|**Field NPCs**: 1 rows, open class-free XP 1,750||||||||||||
|79008|... and that note y.|14/22|1750|obj:Burned-Out Remains 37,51|obj:Burned-Out Remains 46,74 [BA] / obj:Nailed Plank 46,74 [BA]|||U||||

### Elwynn Forest (leftovers)
|id|name|req/L|xp|giver|ender|pre|next|st|T|D|notes|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Goldshire**: 2 rows, open class-free XP 2,380||||||||||||
|70|The Legend of Stalv.|22/28|1700|Innkeeper Farley 44,66|Caretaker Folsom 43,72 [SW]|69|72|-|T24|||
|119|Return to Verner|13/18|680|Smith Argus 42,66|Verner Osgood 26,47 [RR]|118||-|T20|L||
|**Northshire**: 2 rows, open class-free XP 2,435||||||||||||
|345|Ink Supplies|20/24|485|Brother Paxton 50,40|Foreman Oslow 27,49 [RR]|344|347|-||||
|346|Return to Kristoff|20/24|1950|"|Brother Kristoff 55,54 [SW]|347||-||||
|**Elwynn east**: 4 rows, open class-free XP 5,720||||||||||||
|75|The Legend of Stalv.|22/28|1150|Marshal Haggard 85,69|=|74|78|-|T26|||
|78|"|22/28|570|"|Tavernkeep Smitts 74,44 [DW]|75|79|-|T26|||
|94|A Watchful Eye|20/21|1250|Theocritus 65,70|obj:Old Lion Statue 79,47 [RR]||248|-|T20|||
|249|Morganth|20/27|2750|Theocritus 65,70 / obj:Old Lion Statue 79,47 [RR]|Theocritus 65,70|248||U|||GRP|

### Arathi Highlands (req<=30)
|id|name|req/L|xp|giver|ender|pre|next|st|T|D|notes|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Refuge**: 11 rows, open class-free XP 30,520||||||||||||
|695|An Apprentice's Enc.|30/39|300|Apprentice Kryten 46,48|Skuerto 47,47|694|696|-|||GRP|
|691|Worth Its Weight in.|30/36|3500|"|=||693|-||||
|681|Northfold Manor|30/31|2500|Captain Nials 46,48|=||682|-||||
|682|Stromgarde Badges|30/37|3550|"|=|681||U|||GRP|
|8260|Arathor Basic Care .|25/34|270|Samuel Hawke 46,45|=|||-|||excl:8261,8262|
|696|Attack on the Tower|30/39|3000|Skuerto 47,47|=|695|697|-|||GRP|
|697|Malin's Request|30/39|3750|"|Archmage Malin 50,87 [SW]|696||-|||GRP|
|694|Trelane's Defenses|30/39|3000|"|Apprentice Kryten 46,48|693|695|-|||GRP|
|693|Wand over Fist|30/39|3000|"|=|691|694|-||||
|684|Wanted!  Marez Cowl|30/39|3750|obj:Wanted Board 46,48|Captain Nials 46,48|||U|||GRP|
|685|Wanted!  Otto and F.|30/40|3900|"|Captain Nials 46,48|||U|||GRP|
|**Arathi NE**: 4 rows, open class-free XP 2,850|||||||||||dungeon starts (sec 1): 96264>RFK|
|642|The Princess Trapped|30/37|2850|obj:Shards of Myzrael 62,34|obj:Iridescent Shards 84,31||651|U||||
|**Arathi E**: 4 rows, open class-free XP 9,200 (+1 unk)||||||||||||
|660|Hints of a New Plag.|30/37|2850|Kinelory 60,54|Quae 60,54|657|661|-|||ESC?|
|657|"|30/36|?|Quae 60,54|Kinelory 60,54|658|660|-||||
|658|"|30/36|2800|"|=|659|657|-||||
|661|"|30/37|3550|"|Phin Odelic 50,59 [HB]|660||-||||
|**Arathi W**: 2 rows, open class-free XP 5,800||||||||||||
|653|Myzrael's Allies|30/40|2350|obj:Keystone 36,58|Gerrig Bonegrip 51,6 [IF]|652|687|-||||
|652|Breaking the Keysto.|30/42|3450|obj:Stone of Inner Binding 36,57|obj:Keystone 36,58|651|653|-|||GRP|
|**Field NPCs**: 3 rows, open class-free XP 7,850||||||||||||
|647|MacKreel's Moonshine|28/30|3050|Foggy MacKreel 43,93|Brewmeister Bilger 52,59 [HB]|||-|||ESC?|
|651|Stones of Binding|30/38|2850|obj:Iridescent Shards 84,31|obj:Stone of Inner Binding 36,57|642|652|U||||
|79976|This Must Be The Pl.|14/32|1950|obj:Messenger Bag 22,24|obj:Hastily Rolled-Up Satchel 22,24|||U||||
|**Item/drop starts**: 1 rows, open class-free XP 1,350||||||||||||
|635|Crystal in the Moun.|30/35|1350|item:Pendant of Myzrael|obj:Shards of Myzrael 62,34|||U|||item start (drop: Bloodscalp Warrior, Bloodscalp Scout)|

### Silverpine Forest (Alliance-available)
|id|name|req/L|xp|giver|ender|pre|next|st|T|D|notes|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Field NPCs**: 2 rows, open class-free XP 265|||||||||||dungeon starts (sec 1): 92458>Dalaran, 92457>Dalaran|
|92459|Friend of the Kirin.|24/33|265|Image of Archmage Modera 69,45|Archmage Celindra 14,60 [AL]|||N||||

### Dun Morogh (leftovers)
|id|name|req/L|xp|giver|ender|pre|next|st|T|D|notes|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Field NPCs**: 1 rows, open class-free XP 1,750|||||||||||dungeon starts (sec 1): 2926>Gnomer, 2962>Gnomer|
|466|Search for Incendic.|20/22|1750|Pilot Stonegear 50,49|=|||-||||

### Other zones: quests outside the zones above that a TUGs 20-32 chapter uses (other chain neighbours appear only in Section 3)
|id|name|req/L|xp|giver|ender|pre|next|st|T|D|notes|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Stonetalon**: 1 rows||||||||||||
|1085|On Guard in Stoneta.|17/21|165|Kaela Shadowspear 60,67|Gaxim Rustfizzle 60,67||1071|-|T27|||

## 3. Chains (cross-zone bounces)

Node = `id[class] name rREQ/Llevel XPxp giverhub>enderhub [flags]`; flags: D done in 1-20, 8 handled by chapter 08, T## = TUGs chapter (T29 = 29-30, `o` optional). Link symbols: `->` QDB prereq/next link; `~>` link implied by same-name + ender=giver or by the brief (no QDB link); `..` no link in the data (order inferred, flagged). Hub names are the Section 2 hubs; `in-X` = NPC/object only inside dungeon X; `?` = no position in files. XP = raw Wowhead XP at quest level.

### 3.A Chains named in the brief

**Call of Water (Shaman, Water Totem)** - 9 quests, 9,580 XP
- 94494 Call of Water r20/L20 780xp IF Cavern>LM Dam [8] ~> 94495 r20/L22 435xp LM Dam>Hervdana ~> 94497 r20/L22 870xp Hervdana ~> 94499 r20/L22 1300xp Hervdana ~> 94500 r20/L23 1400xp Hervdana ~> 94501 r20/L23 460xp Hervdana>LM Dam ~> 94502 r20/L23 1400xp LM Dam>WF south ~> 94503 r20/L23 185xp WF south>Silverpine ~> 94505 r20/L23 2750xp Silverpine>LM Dam
- note: Route: Ironforge Eldrun > Loch Modan dam Norric > Wetlands SE cave Hervdana (x4 parts) > Norric > Westfall Forgotten Shrine (obj) > Silverpine Minor Manifestation of Water (npc 5895, only spawns in zone 130 at 38.7,44.6) > Norric. No pre/next in QDB; links are the brief order, each giver = previous ender. Conflicts: 94503 objective text says Westfall but npc 5895 is Silverpine only (ch08 agrees: Silverpine 38.4,44.4); ch08 calls 94503 "a return to Norric" while QDB ends 94502 and starts 94503 at the shrine. 94499 Red Waterskin is at Stonewatch Falls (Redridge) and 94500 Blue Waterskin comes from Astranaar per ch08. 94616 Water Sapta is a separate row (2.0).

**The Missing Diplomat (all r28)** - 17 quests, 16,315 XP
- 1274 The Missing Diplomat r28/L28 230xp SW Cathedral>SW Keep [T30] -> 1241 r28/L28 230xp SW Keep>Stormwind [T30] -> 1242 r28/L28 230xp Stormwind>SW Trade [T30] -> 1243 r28/L28 230xp SW Trade>Darkshire [T30] -> 1244 r28/L30 2450xp Darkshire [T32] -> 1245 r28/L30 245xp Darkshire>SW Trade -> 1246 r28/L31 250xp SW Trade>SW Old Town -> 1447 r28/L31 1250xp SW Old Town -> 1247 r28/L31 250xp SW Old Town>SW Trade -> 1248 r28/L33 660xp SW Trade>Menethil -> 1249 r28/L33 1300xp Menethil -> 1250 r28/L33 265xp Menethil -> 1264 r28/L33 1300xp Menethil>Dustwallow -> 1265 r28/L35 275xp Dustwallow -> 1266 r28/L36 700xp Dustwallow -> 1324 r28/L38 2150xp Dustwallow -> 1267 r28/L38 4300xp Dustwallow
- note: Stormwind (Cathedral > Keep > Stormwind > Trade/Stockade) > Darkshire > Stormwind Old Town/Trade > Menethil > Dustwallow (boat). TUGs 30-31 does 1274 > 1241 > 1242 and accepts 1243 (to Darkshire); 1244 appears only in the 32-33 chapter (T32, outside 20-32); the Menethil leg (1248-1250, 1264) is in no TUGs chapter; Dustwallow leg is L35-38. 1267 is U, 1324 has the party flag, 1250 U.

**The Legend of Stalvan (all r22)** - 13 quests, 13,240 XP
- 66 The Legend of Stalv. r22/L28 230xp Darkshire [T24] -> 67 r22/L28 1150xp Darkshire>WF south [T24] -> 68 r22/L28 1700xp WF south>Darkshire [T24] -> 69 r22/L28 570xp Darkshire>Goldshire [T24] -> 70 r22/L28 1700xp Goldshire>Stormwind [T24] -> 72 r22/L28 230xp Stormwind [T24] -> 74 r22/L28 1150xp Stormwind>Elwynn east [T24] -> 75 r22/L28 1150xp Elwynn east [T26] -> 78 r22/L28 570xp Elwynn east>Darkshire [T26] -> 79 r22/L28 230xp Darkshire [T26] -> 80 r22/L28 230xp Darkshire [T26] -> 97 r22/L28 230xp Darkshire [T26] -> 98 r22/L35 4100xp Darkshire
- note: Darkshire > Westfall south coast (Mistmantle) > Darkshire > Goldshire > Stormwind > Elwynn east > Darkshire. TUGs: 66-74 in 24-25, 75-97 in 26-27; 98 (L35, 4100 XP) not in TUGs. 253 Bride of the Embalmer (r20, GRP) belongs to the separate chain 252 > 253.

**Raene's Cleansing (all r18)** - 12 quests, 19,340 XP
- 991 Raene's Cleansing r18/L19 1450xp Astranaar>Forest Song [T23] -> 1023 r18/L21 1250xp Forest Song>Astranaar [T23] -> 1024 r18/L21 830xp Astranaar>Shael'dryn [T27] -> 1026 r18/L27 2200xp Shael'dryn [T27] -> 1027 r18/L28 2300xp Shael'dryn [T34] -> 1028 r18/L28 1700xp Shael'dryn [T34] -> 1055 r18/L28 230xp Shael'dryn -> 1029 r18/L28 230xp Shael'dryn>Astranaar -> 1030 r18/L28 1700xp Astranaar>Ash south -> 1045 r18/L30 2450xp Ash south -> 1046 r18/L30 3050xp Ash south>Astranaar
- 1023 Raene's Cleansing r18/L21 1250xp Forest Song>Astranaar [T23] -> 1025 An Aggressive Defen. r18/L24 1950xp Astranaar [T27]
- note: Astranaar (Raene) > Forest Song (Teronis corpse) > Astranaar > Shael'dryn camp (53,46) and Hidden Shrine > Raene > Krolg (Ash south, 50.8,75.1) > Raene. 1025 is a side branch ending in Astranaar. 990 Trek to Ashenvale (r15, Auberdine breadcrumb to Raene) leads in; QDB shows no prereq on 991. TUGs: 991 and 1023 in 23-24, 1024 and 1026 in 27-28, 1027/1028 only in 34-35 (outside 20-32).

**Dragonmaw arc (Wetlands, new in Forever, mostly GRP)** - 10 quests, 24,200 XP
- 98208 Bloom of the Heavens r22/L29 2350xp Menethil [T29] ~> 98209 r22/L29 1200xp Menethil>Auberdine
- 98230 This Land Was Their. r22/L29 1200xp Menethil>Dun Algaz road ~> 98291 Death to the Dragon. r22/L30 3050xp Dun Algaz road ~> 98297 Stopping the Cycle r24/L34 2700xp Dun Algaz road
- 98283 Carnage r22/L30 3050xp Greenwarden
- 98293 Forced Disarmament r22/L30 3050xp Wetlands>Menethil
- 98223 Old Habits r23/L31 1250xp Wetlands>Menethil
- 98216 Understanding Our P. r23/L31 3150xp Whelgar .. 98310 Gleaning Our Future r24/L32 3200xp Whelgar
- note: NO pre/next in QDB or Wowhead for any of these; grouping is by giver/ender adjacency and req (22 > 23 > 24) only (`..` = no data). 98208/98209: Sylessa (Menethil) > Thundris Windweaver (Auberdine, boat); 98230 Stoutfist > Howin 49.4,42.1 then Howin self-turn-ins 98291, 98297 (L34); 98283 kill at Rethiel 56.4,40.4; 98293 click Dragonmaw Armaments 58.9,45.1 > Stoutfist; 98223 click Tattered Spellbook 53.5,54.5 > Stoutfist; 98216/98310 at Whelgar 38.8,52.4. Same NPCs also give 98245 and 98246 (Howin, r21, T29), 98300 (Howin, r24, > King Magni, Ironforge) and 98313 (Whelgar, r24, > Historian Karnik, Ironforge). Wowhead reqrace 76 (no Human) on 98208/98209.

**Wetlands "Lost" chain (Dun Modr, r27-28, all GRP, all new)** - 5 quests, 13,050 XP
- 87491 Spark of Freedom r27/L32 2550xp Dun Modr .. 88756 Bring Back a Bang r27/L32 2550xp Dun Modr
- 87318 Hearts of the Lost r28/L33 2650xp Dun Modr ~> 88757 Accessories of the . r28/L33 2650xp Dun Modr ~> 88758 Sentiments of the L. r28/L33 2650xp Dun Modr
- note: All at Dun Modr (45-52, 9-18), no QDB links. 87318 Comar > Essene, 88757 Essene, 88758 Essene > Comar (giver=ender adjacency). 87491 (Captive Fire Elemental > Roggo Harlbarrow) and 88756 (Ashlan Stonesmirk) are r27, link between them unconfirmed. Dun Modr holds L27-31 elites.

**Excavation lead-in** - 2 quests, 3,130 XP
- 95737 Seeking Caitlin r24/L31 630xp Astranaar>Menethil [T27] ~> 95647 Lost in the Thicket. r24/L31 2500xp Menethil>? [T29]
- note: 95737 (Llana, Astranaar 35.0,48.5) > Caitlin Grassman (Menethil 11.9,58.8) who gives 95647 (ender Ardin Grassman inside the Excavation Site, npc 262681 has no spawn). TUGs: 95737 picked up in 27-28, turned in with 95647 picked up in 29-30. Other Excavation quests: Section 1.

**Knowledge in the Deeps (BFD)** - 1 quests, 2,750 XP
- 971 Knowledge in the De. r10/L23 2750xp IF Cavern [8]
- note: Single quest (Gerrig Bonegrip, Forlorn Cavern IF 50.8,5.6; item from a chest in BFD). 78923 is the type-62 duplicate (r25 L27).

**The Corruption Abroad > Researching the Corruption (BFD)** - 2 quests, 3,850 XP
- 3765 The Corruption Abro. r18/L24 1450xp SW Park>Auberdine [8] -> 1275 Researching the Cor. r18/L24 2400xp Auberdine [8]
- note: 3765 Argos Nightwhisper (Stormwind Park 36.2,67.6) > Gershala Nightwhisper (Auberdine dock 38.3,43.0) who gives 1275 (8 Corrupted Brain Stems, Fallenroot satyrs in and around BFD) and takes it back. 78926 is the type-62 duplicate.

**In Search of Thaelrid > Blackfathom Villainy; Twilight Falls (BFD, Darnassus)** - 3 quests, 8,250 XP
- 1198 In Search of Thaelr. r18/L24 2400xp Darnassus>in-BFD -> 1200 Blackfathom Villainy r18/L27 3300xp in-BFD>Darnassus
- 1199 Twilight Falls r20/L25 2550xp Darnassus
- note: 1198 Shaedlass (Darnassus 55.4,25.0) > Argent Guard Thaelrid inside BFD; 1200 Thaelrid > Selgorm (Darnassus 56.2,24.4); 1199 Manados (Darnassus 55.2,24.0) self-turn-in. Type-62 duplicates 78921, 78924, 78925 (r25) are in Section 1, as is 78916 The Heart of the Void (r25, giver not in files, not type 62).

### 3.B Other chains with a not-done member at req>=18 or quest L>=20, a dungeon member or a TUGs 20-32 member
Compact form `id name(rREQ;giverhub>enderhub)`, `||` separates branches; names are in the Section 2 rows by id; chains labelled by their first quest. Sparklematic: Sparklematic 5200 (Gnomeregan, obj in dungeon): three pick-one tiers (excl lists in QDB). Tier 1: 2951 | 4601 | 4602 (r25 L30, XP blank) -> Tier 2: 2952 | 4605 | 4606 (2450 XP each) -> Tier 3 (REPEATABLE, XP blank): 2953 | 4603 | 4604. Grime-Encrusted Ring: 2945 (item from Dark Iron Agent, r28 L34, 2700xp) -> 2947 (Sparklematic > Talvash del Kissel, Ironforge 36.4,3.6) -> 2948 Gnome Improvement (r28 L35, 2750xp, Talvash). Gnomeregan feed-in chains are in Part B (Save Techbot's Brain, Gnogaine, Data Rescue, Essential Artificials).

- **How Big a Threat?** (10): 984(r10;Auberdine) -> 985(r10;Auberdine) -> 986(r10;Auberdine) -> 993(r10;Auberdine>Darkshore south) -> 994(r10;Darkshore south>Auberdine) -> 990(r15;Auberdine>Astranaar) || 984(r10;Auberdine) -> 4761(r11;Auberdine) -> 4762(r11;Auberdine) -> 4763(r15;Auberdine) || 993(r10;Auberdine>Darkshore south) -> 995(r10;Darkshore south>Auberdine) -> 990(r15;Auberdine>Astranaar)
- **The Price of Shoes** (5): 118(r14;Lakeshire>Goldshire) -> 119(r13;Goldshire>Lakeshire) -> 122(r14;Lakeshire) || 119(r13;Goldshire>Lakeshire) -> 124(r15;Lakeshire) -> 126(r15;Lakeshire)
- **The Tower of Althalaxx** (10): 965(r13;Auberdine>Darkshore north) -> 966(r13;Darkshore north) -> 967(r13;Darkshore north>Forest Song) -> 970(r13;Forest Song) -> 973(r13;Forest Song) -> 1140(r13;Forest Song) -> 1167(r13;Forest Song>Darkshore north) -> 1143(r13;Darkshore north) -> 981(r13;Darkshore north>Forest Song) || 973(r13;Forest Song) -> 976(r19;Forest Song)
- **Messenger to Stormwind** (6): 120(r14;Lakeshire>Stormwind)D -> 121(r14;Stormwind>Lakeshire) -> 143(r14;Lakeshire>Sentinel) -> 144(r14;Sentinel>Lakeshire) -> 145(r18;Lakeshire>Darkshire) -> 146(r18;Darkshire>Lakeshire)
- **Trouble In Darkshore?** (6): 730(r14;Darnassus>Auberdine) -> 729(r15;Auberdine>Darkshore south) -> 731(r15;Darkshore south>Auberdine) -> 741(r15;Auberdine>Darnassus) -> 942(r15;Darnassus>Menethil) -> 943(r15;Menethil)
- **The Zoram Strand** (2): 1008(r14;Astranaar) -> 1134(r18;Astranaar)
- **Remember That I Love You** (2, all r15): 92415(item>SW Cathedral) ~> 95161(SW Cathedral>Darkshire)
- **A Dark Threat Looms** (7, all r16): 250(LM Dam>Loch Modan) -> 199(Loch Modan>LM Dam) -> 161(LM Dam>Dun Modr) -> 274(Dun Modr>LM Dam) -> 278(LM Dam) -> 280(LM Dam>Loch Modan) -> 283(Loch Modan>LM Dam)
- **The Unsent Letter** (12, all r16): 373(item>SW Cathedral)D -> 389(SW Cathedral>SW Trade) -> 391(SW Trade) -> 392(SW Trade>SW Cathedral) -> 393(SW Cathedral>SW Old Town) -> 350(SW Old Town>SW Trade) -> 2745(SW Trade>SW Keep) -> 2746(SW Keep) -> 434(SW Keep>SW Trade) -> 394(SW Trade>SW Old Town) -> 395(SW Old Town>SW Cathedral) -> 396(SW Cathedral>SW Keep)
- **Raven Hill** (4, all r17): 163(Darkshire>Raven Hill) -> 5(Raven Hill>Darkshire) -> 93(Darkshire) -> 240(Darkshire>Raven Hill)
- **Deliveries to Sven** (17): 164(r17;Darkshire>Sven) -> 95(r20;Sven>Duskwood) -> 230(r20;Duskwood>Sven) -> 262(r20;Sven>Darkshire) -> 265(r20;Darkshire) -> 266(r20;Darkshire) -> 453(r20;Darkshire>Raven Hill) -> 268(r20;Raven Hill>Sven) -> 323(r20;Sven) -> 269(r20;Sven>SW Cathedral) -> 270(r20;SW Cathedral>Menethil) -> 321(r20;Menethil) -> 324(r20;Menethil) -> 322(r20;Menethil>SW Dwarven) -> 325(r20;SW Dwarven>Sven) -> 55(r20;Sven) || 324(r20;Menethil) -> 526(r20;Menethil) -> 322(r20;Menethil>SW Dwarven)
- **The Hermit** (15): 165(r17;Darkshire>Abercrombie) -> 148(r20;Abercrombie>Darkshire) -> 149(r20;Darkshire>Brightwood) -> 154(r20;Brightwood>Darkshire) -> 157(r20;Darkshire>Abercrombie) -> 158(r20;Abercrombie>Darkshire) -> 156(r20;Darkshire) -> 159(r20;Darkshire>Abercrombie) -> 133(r20;Abercrombie) -> 134(r20;Abercrombie) -> 160(r20;Abercrombie>Darkshire) -> 251(r20;Darkshire) -> 401(r20;Darkshire) -> 252(r20;Darkshire) -> 253(r20;Darkshire)
- **On Guard in Stonetalon** (16): 1070(r17;Astranaar>Stonetalon) -> 1085(r17;Stonetalon) -> 1071(r17;Stonetalon) -> 1072(r17;Stonetalon>IF Tinkertown) -> 1073(r17;IF Tinkertown) -> 1074(r17;IF Tinkertown>Stonetalon) -> 1079(r17;Stonetalon) -> 1091(r17;Stonetalon) -> 1083(r20;Stonetalon) -> 1082(r17;Stonetalon>Astranaar) -> 1081(r17;Astranaar>Darnassus) || 1071(r17;Stonetalon) -> 1075(r17;Stonetalon>SW Mage) -> 1076(r17;SW Mage) -> 1077(r17;SW Mage>Stonetalon) -> 1079(r17;Stonetalon) || 1074(r17;IF Tinkertown>Stonetalon) -> 1080(r17;Stonetalon) -> 1091(r17;Stonetalon) -> 1084(r22;Stonetalon) -> 1082(r17;Stonetalon>Astranaar) || 1077(r17;SW Mage>Stonetalon) -> 1080(r17;Stonetalon)
- **Blackrock Menace** (3, all r18): 20(Lakeshire)D -> 19(Lakeshire) || 20(Lakeshire)D -> 115(Lakeshire)
- **The Night Watch** (3, all r18): 56(Darkshire) -> 57(Darkshire) -> 58(Darkshire)
- **Young Crocolisk Skins** (2, all r18): 484(Menethil) -> 471(Menethil)
- **Journey to Stonetalon Peak** (3): 1056(r18;Astranaar>Stonetalon) -> 1057(r20;Stonetalon) -> 1059(r20;Stonetalon>Feralas)
- **Fiora Longears** (2): 1132(r30;Menethil>Dustwallow) -> 1133(r18;Dustwallow>Astranaar)
- **Report to Mountaineer Rockgar** (6): 468(r19;Thelsamar>Stormpike post) -> 455(r19;Stormpike post>Menethil) -> 473(r23;Menethil) -> 464(r23;Menethil) -> 465(r23;Menethil>Wetlands) -> 474(r23;Wetlands>Menethil)
- **The Ancient Statuette** (2): 1007(r19;Talen) -> 1009(r20;Talen)
- **A Watchful Eye** (3, all r20): 94(Elwynn east>Redridge) -> 248(Redridge) -> 249(Elwynn east/Redridge>Elwynn east)
- **Look To The Stars** (4, all r20): 174(Darkshire) -> 175(Darkshire>Brightwood) -> 177(Brightwood>Darkshire) -> 181(Darkshire)
- **The Greenwarden** (4, all r20): 463(Menethil>Greenwarden) -> 276(Greenwarden) -> 277(Greenwarden) -> 275(Greenwarden)
- **Claws from the Deep** (9, all r20): 279(Menethil) -> 281(Menethil>Wetlands) -> 284(Wetlands) -> 285(Wetlands) -> 286(Wetlands>Menethil) ~> 98189(Menethil) ~> 98190(Menethil>SW Keep) ~> 98191(SW Keep>SW Cathedral) ~> 98219(SW Cathedral>Southshore)
- **An Old History Book** (4, all r20): 337(item>SW Keep) -> 538(SW Keep>Southshore) -> 540(Southshore) -> 542(Southshore>SW Keep)
- **Speaking of Fortitude** (5, all r20): 343(SW Cathedral>SW Keep) -> 344(SW Keep>Northshire) -> 345(Northshire>Lakeshire) -> 347(Lakeshire>Northshire) -> 346(Northshire>SW Cathedral)
- **Stonegear's Search** (2, all r20): 467(Thelsamar/IF Military>Dun Morogh) -> 466(Dun Morogh)
- **Bathran's Hair** (5, all r20): 1010(Forest Song) -> 1020(Forest Song>Astranaar) -> 1033(Astranaar) -> 1034(Astranaar) -> 1035(Astranaar)
- **Elemental Bracers** (2, all r20): 1016(Ash south) -> 1017(Ash south)
- **Tinkmaster Overspark** (2, all r20): 2923(SW Cathedral>IF Tinkertown) -> 2922(IF Tinkertown)
- **The Day After** (3, all r20): 2927(IF Tinkertown>Dun Morogh) -> 2926(Dun Morogh) -> 2962(Dun Morogh)
- **In Search of The Excavation Team** (2, all r21): 305(Menethil>Whelgar) -> 306(Whelgar>Menethil)
- **The Third Fleet** (5, all r22): 288(Menethil) -> 289(Menethil) -> 290(Menethil>Wetlands) -> 292(Wetlands>Menethil) -> 293(Menethil>SW Cathedral)
- **Ormer's Revenge** (3, all r22): 294(Whelgar) -> 295(Whelgar) -> 296(Whelgar)
- **The Dark Iron War** (2): 303(r25;Dun Modr) -> 378(r22;Dun Modr)
- **Worgen in the Woods** (4, all r23): 173(Darkshire) -> 221(Darkshire) -> 222(Darkshire) -> 223(Darkshire)
- **Forsaken Diseases** (2, all r24): 1011(Ash east) -> 1012(Ash east)
- **Klockmort's Essentials** (2, all r24): 2925(Darnassus>IF Tinkertown) -> 2924(IF Tinkertown)
- **A Noble Brew** (2, all r25): 335(SW Mage) -> 336(SW Mage>Stormwind)
- **Down the Coast** (6, all r25): 536(Southshore) -> 559(Southshore) -> 560(Southshore) -> 561(Southshore) -> 562(Southshore) -> 563(Southshore>SW Keep)
- **Sully Balloo's Letter** (5, all r25): 637(item>Ironforge) -> 683(Ironforge>IF Mystic) -> 686(IF Mystic>Ironforge) -> 689(Ironforge) -> 700(Ironforge>IF Mystic)
- **The Howling Vale** (9, all r25): 1022(Illiyana) -> 1037(Illiyana>Darnassus) -> 1038(Darnassus) -> 1039(Darnassus>Barrens) -> 1040(Barrens>STV) -> 1041(STV>Darkshire) -> 1042(Darkshire) -> 1043(Darkshire) -> 1044(Darkshire>Darnassus)
- **Castpipe's Task** (2, all r25): 2931(Stonetalon>IF Tinkertown) -> 2930(IF Tinkertown)
- **Foreboding Plans** (2, all r26): 510(?>Southshore) -> 512(Southshore)
- **Vile Satyr! Dryads in Danger!** (3, all r26): 1021(Illiyana>Ash east) -> 1031(Ash east>Illiyana) -> 1032(Illiyana)
- **The Weathered Grave** (5, all r28): 225(Duskwood>Darkshire) -> 227(Darkshire) -> 228(Darkshire) -> 229(Darkshire) -> 231(Darkshire>Duskwood)
- **The Ensorcelled Parchment** (2): 551(r30;item>Southshore) -> 554(r28;Southshore>IF Explorers)
- **The Thandol Span** (4, all r28): 631(Dun Modr>Wetlands) -> 632(Wetlands>Dun Modr) -> 633(Dun Modr) -> 634(Dun Modr>Refuge)
- **Grime-Encrusted Ring** (3, all r28): 2945(item>in-Gnomeregan) -> 2947(in-Gnomeregan>Ironforge) -> 2948(Ironforge)
- **Lonebrow's Journal** (2, all r29): 1100(item>Feralas) -> 1101(Feralas)
- **Crushridge Bounty** (2, all r30): 500(Southshore) -> 504(Southshore)
- **Encrypted Letter** (4, all r30): 511(?>Southshore) -> 514(Southshore>IF Explorers) -> 525(IF Explorers>Southshore) -> 537(Southshore)
- **Assassin's Contract** (2, all r30): 522(item>Southshore) -> 523(Southshore)
- **The Princess Trapped** (7, all r30): 642(Arathi NE>Arathi) -> 651(Arathi>Arathi W) -> 652(Arathi W) -> 653(Arathi W>IF Cavern) -> 687(IF Cavern/Arathi>Badlands) -> 692(Badlands) -> 656(Badlands>Arathi NE)
- **Hints of a New Plague?** (5, all r30): 659(Southshore>Arathi E) -> 658(Arathi E) -> 657(Arathi E) -> 660(Arathi E) -> 661(Arathi E>Southshore)
- **Northfold Manor** (2, all r30): 681(Refuge) -> 682(Refuge)
- **Malin's Request** (7, all r30): 690(SW Mage>Refuge) -> 691(Refuge) -> 693(Refuge) -> 694(Refuge) -> 695(Refuge) -> 696(Refuge) -> 697(Refuge>SW Mage)

(3.B lists 57 chains.)

## 4. TUGs 20-30 travel skeleton (compare/TUGs-1.12-2026-10-14, Alliance)

One row per chapter file 20-22 .. 31-32. `[Hub: +accept -turnin ...]` in order, hub = location of that quest giver (accept) or ender (turn-in) using the Section 2 hubs; `<F X>` = `Fly to [F X]`, `<P x,y Zone>` = flight path pickup, `<H>` = `Use your [H] Hearthstone.`, `<BOAT ..>` boat/tram text, `<run ..>` run/jump steps. Race tags: `{Hu}` Human-only line, `{noHu}` line tagged Nightelf/Dwarf/Gnome (not Human), `{Hunter}`/`{Shaman}` class lines; other class-only lines (Mage, Paladin, Warrior...) are dropped. There are NO `[S ...]` hearth-set tags anywhere in TUGs and 20-32 never contains `Set your [H]` (later chapters do, e.g. Ironforge, Hinterlands, STV); every `<H>` is followed by Stormwind hand-ins or a Stormwind-departing boat/flight, so TUGs implies hearth = Stormwind, whereas the Atlas ch08 ends with hearth = Sentinel Hill. Expected level = second number of the chapter name; need = XP from level start to end per the Section 5 table; T-in XP = sum of raw Wowhead XP of the chapter turn-ins (each id once, quest XP only, no mob XP, no decay, `?` quests counted as unk). The raw TUGs flights quoted: only `[F Redridge Mountains]`, `[F Sentinel Hill]`, `[F Stormwind]`, `[F Stormwind City]`, `[F Duskwood]`, `[F Darkshire]`, `[F Westfall]`, `[F Ashenvale]`, `[F Wetlands]`.

|chapter|end L|need XP|T-in XP (n turn-ins)|skeleton|
|---|---|---|---|---|
|20-22 Ruins of Lordaeron & Deadmines|22|43,200|22,425 (18)|[in-dungeon/?: +95250] [item: +95195 +95189 +92415] [in-dungeon/?: -95250] <H hearth> [SW Cathedral: -92415 +95161] [Stormwind: -95189 -95195] [Elwynn east: +94{noHu}] [Three Corners: +244{noHu}] <F Redridge Mountains{Hu}> [Three Corners: +244{Hu}] [Lakeshire: +129 -65 +132 +127 +120 +118 -244 +246 +98407] <P 30.6,59.4 Redridge Mountains{noHu}> <F Sentinel Hill> [Sentinel: -132 +135] <F Stormwind> [Stormwind: -120 +121] [Goldshire: -118 +119] [SW Old Town: -135 +141] <F Sentinel Hill> [Sentinel: -141 +142 -142 +155 -155 +166 +214] <note Look for a group for deadmines..> [item: +373] <H hearth> [SW Keep: -167 -168] [SW Dwarven: -2040] [SW Cathedral: -373 +389] [SW Trade: -389]|
|22-23 Redridge Mountains|23|24,000|14,935 (15)|<F Redridge Mountains> [Lakeshire: +98387 +20 +125 -119 +124 +3741] [Three Corners: -129 +130] [Lakeshire: -98387 -20 +19 +115 -125 +89 -121 +143 +91 +150 -150 -127 -130 +131 -131 -124 -89 -3741 -246 -98407] <H hearth> <BOAT Take the boat route to Auberdine.>|
|23-24 Ashenvale|24|25,500|22,960 (+1 unk) (17)|[Auberdine: -4763 -2139 -87760] [Darkshore south: -951 -98013] <note ESCORT QUEST INCOMING,make sure all group memb..> [Darkshore south: -993 +994] [Forest Song: -5713 -967 +970 +1010 -1010 +1020 -970 +973] [Illiyana: -945] <P 34.59,48.01 Ashenvale> [Astranaar: +1008 +1070 +991 -1020 +1033] [Forest Song: -991 +1023] [Talen: +1007 -1007 +1009] <note As a Group do Ruuzel, if youre solo skip it. (..> [Talen: -1009] [Astranaar: -1008 +1134 -1023] <H hearth>|
|24-25 Duskwood|25|27,200|18,885 (20)|<F Redridge Mountains> [Darkshire: +66 +101 -66 +67 +96139 +377 +56 +163 +164 +165] <P 77.12,44.17 Duskwood> [Darkshire: +174 -174 +175] [Brightwood: -175 +177] [Twilight Grove: +245] [Raven Hill: -163 +5] [Sven: -164 +95 +226] [Abercrombie: -165 +148] [Sven: -226] [Sentinel: -143 +144] [WF south: -67 +68] <F Duskwood> [Darkshire: -148 +149 -5 +93 -56 -68 +69 -96139] [Brightwood: -149 +154] [Darkshire: -177 +181 -154 +157] <F Stormwind City> [Goldshire: -69 +70] [Stormwind: -70 +72 -72 +74]|
|25-26 Stockades|26|28,900|9,330 (7)|[SW Trade: +387 +391] [SW Old Town: +388] <F Duskwood> [Darkshire: +377] <F Redridge Mountains> [Lakeshire: +386] [SW Trade: -387 -391 +392] [SW Cathedral: -392 +393] [SW Old Town: -388 -393 +350] [SW Trade: -350 +2745] [SW Keep: -2745 +2746]|
|26-27 Redridge Mountains|27|30,500|34,435 (23)|<F Redridge Mountains> [Lakeshire: +98386 +126 +169 +95999 -144 +145 +180 -386 +92 -92 +34] [Elwynn east: -74 +75 -75 +78 +94{Hu}] [Lakeshire: +128] [Redridge: -94 +248] [Lakeshire: -34 -91 -95999 -180 -169 -126 -98386 -19 -115 -128] <F Darkshire> [Darkshire: -78 +79 -93 +240 -79 +80 -80 +97 -377 -145 -97] <H hearth>|
|27-28 Ashenvale|28|32,200|11,805 (9)|<BOAT Take the boat to Auberdine.> [Auberdine: -994] <F Ashenvale> [Astranaar: +95737 +1056 +1024 +1025 +1054] <run 43.6,50 Ashenvale> <run 46.8,49.2 Ashenvale> <run 47,51.7 Ashenvale> [Shael'dryn: -1024 +1026] [Astranaar: -1033 +1034 -1054] <run 42.3,71.0 Ashenvale> [Stonetalon: +2931 -1070 +1085 -1085 -1056] <P 36.45,7.07 Stonetalon Mountains> <F Ashenvale> <note Start looking for a BFD dungeon group...> [Astranaar: +4581 -1025 -1034] <note Continue questing: Fly to Auberdine and take the boat to Wetlands(Menethil Harbo>|
|28-29 Blackfathom Depths|29|33,900|0 (0)|<H hearth>|
|29-30 Wetlands|30|35,600|48,870 (32)|[Menethil: +98208 +484 +279] <P 9.5,59.7 Wetlands> [Menethil: +463 +288 -942 +943 -288 +289 -95737 +95647 +98282 +470 +472 +98197 +464 +98221 -98461 +305] <run 34.1,40.8 Wetlands> [Whelgar: +294 -305 +306 +299 -294 +295 -295 +296 -299] <run 31.99,48.68 Wetlands> <run 31.15,49.05 Wetlands> <run 32.41,50.92 Wetlands> [Whelgar: -296] [Dun Algaz road: +98245 +98246] [Greenwarden: -463 +276 -276 +277 -277] [Dun Modr: -472 +631] [Wetlands: -631 +632] [Dun Modr: -632 +633] <run jump off Thandol bridge to Arathi 44.3,92.9> [item: +637] [Dun Modr: -633 +634] [Refuge: -634] <P 45.7,46.1 Arathi Highlands> <F Wetlands> [Menethil: -279 +281 -484 +471 -98197 -464 +465 -470 -98282 -943 -306] [Wetlands: -281 +284 -284 +285 -285 +286] [Menethil: -471 +98072 -286 +98189 -289 +290 -98189 +98190] <H hearth>|
|30-31 Duskwood|31|37,300|29,340 (+1 unk) (31)|[SW Mage: -7791 +335] [SW Cathedral: +2923] [SW Dwarven: +2928] <F Duskwood> [Darkshire: +57 +173] <run 65.0,46.3 Duskwood> [Darkshire: -173 +221] [Duskwood: -95 +230] [Twilight Grove: -245] [Raven Hill: -240] [Abercrombie: -157 +158] [Duskwood: +225] [Sven: -230 +262] <run 56.4,52.6 Westfall> <F Duskwood> [Darkshire: -262 +265 -57 +58 -265 +266 -225 +227 -227 -266 +453 -158 +156 -221 -156 +159] <F Westfall> [Raven Hill: -453 +268] [Abercrombie: -159 +133 -133 +134] [Sven: -268 +323 -323 +269] <H hearth> [SW Cathedral: +1274 -269 +270] [SW Keep: -98190 +98191 -1274 +1241 -2746 +434] [Stormwind: -1241 +1242] [SW Trade: -1242 +1243 -434 +394] [SW Old Town: -394 +395] [SW Cathedral: -395 +396] [SW Keep: -396]|
|31-32 Wetlands|32|n/a (31->32 not given)|37,660 (24)|<BOAT Take the tram to Ironforge.> [Dun Morogh: -2927] [IF Tinkertown: -2923 +2922 +2929 -2931 +2930 +2924] [Ironforge: -637 +683] [IF Mystic: -683 +686] [IF Explorers: +1050] [IF Military: +1179] [Ironforge: -686 +689] <F Wetlands> [Menethil: -270 +321 -321 +324 -324 +322] [Wetlands: -290 +292 -465] <note If you're in a group, do the follow up ELITE q..> [Wetlands: +474] <note If you're in a group, accept the follow up ELI..> [Dun Modr: +304 +303 -304 -303] [Dun Algaz road: -98246 -98245] [Menethil: -474 -98072 -292 +293] <BOAT Take the boat to Southshore.> [Southshore: +659 +536 +98463 +98071 -536 +559 -559 +560 -560 +561 -561 +562 -562 +563 -98071] <P 49.4,52.4 Hillsbrad Foothills> <H hearth>|

Cumulative chapter turn-in XP, 20-22 through 31-32 (race/class-filtered, raw): 250,645; XP needed 20 -> 31 = 318,300 (28-29 BFD chapter is empty, its quest XP is missing).
- 20-22: Dwarf accepts 94 and 244 then walks to Lakeshire and takes the Redridge [P] 30.6,59.4; Human uses `Fly to [F Redridge Mountains]` (line tagged [A Human]); Deadmines group trip; first [H] follows RoL (TUGs assumes it returns to Stormwind)
- 23-24: 994 is an escort (party); 1009 Ruuzel is a group quest; [P] Astranaar 34.59,48.01
- 24-25: [P] Darkshire 77.12,44.17; chapter text points to "23-24 Redridge Mountains" / stockades next
- 26-27: QC95999, QC248, QC169, QC19, QC115 are marked Elite/Hard optional
- 27-28: no [H] at the end; text: `Continue questing: Fly to Auberdine and take the boat to Wetlands(Menethil Harbor)`; [P] Stonetalon 36.45,7.07; BFD only a hint
- 28-29: PLACEHOLDER ("This will be added later", #N/A lines) with one [H]; no quests
- 29-30: [P] Menethil 9.5,59.7 and Refuge Pointe 45.7,46.1; bridge jump to Arathi to reach the item start 637
- 30-31: two [F Duskwood] and one [F Westfall]; [H] is mid-chapter; Mage/Paladin/Priest/Druid/Warlock/Warrior-only lines dropped
- 31-32: tram to Ironforge, `[F Wetlands]` from Ironforge, boat Menethil > Southshore, Southshore [P] 49.4,52.4; TODO line "Wetlands dungeon guide" (Excavation not written)

## 5. Level table, XP decay, totals

### 5.1 XP per level (given) and cumulative from the start of level 20

|level|XP to next|cumulative from 20.0 to reach next|
|---|---|---|
|20 -> 21|20,800|20,800|
|21 -> 22|22,400|43,200|
|22 -> 23|24,000|67,200|
|23 -> 24|25,500|92,700|
|24 -> 25|27,200|119,900|
|25 -> 26|28,900|148,800|
|26 -> 27|30,500|179,300|
|27 -> 28|32,200|211,500|
|28 -> 29|33,900|245,400|
|29 -> 30|35,600|281,000|
|30 -> 31|37,300|318,300|

### 5.2 Quest XP decay (given rule): d = char level - quest level; d<=5: 100%, d=6: 80%, 7: 60%, 8: 40%, 9: 20%, d>=10: 10%

|char level|quest L for 100%|80% (L=)|60%|40%|20%|10% (L<=)|
|---|---|---|---|---|---|---|
|20|>=15|14|13|12|11|<=10|
|21|>=16|15|14|13|12|<=11|
|22|>=17|16|15|14|13|<=12|
|23|>=18|17|16|15|14|<=13|
|24|>=19|18|17|16|15|<=14|
|25|>=20|19|18|17|16|<=15|
|26|>=21|20|19|18|17|<=16|
|27|>=22|21|20|19|18|<=17|
|28|>=23|22|21|20|19|<=18|
|29|>=24|23|22|21|20|<=19|
|30|>=25|24|23|22|21|<=20|

### 5.3 Class-free Alliance quest XP, req 18-30, by zone table (Wowhead XP at quest level; excludes dailies, repeatables, type-62 and class quests; none of these rows was turned in during 1-20, so open = total)

|zone|quests|XP|quests with unknown XP|
|---|---|---|---|
|Wetlands|70|123,330|2|
|Duskwood|59|78,260|0|
|Redridge|9|16,170|0|
|Hillsbrad Foothills|25|54,750|0|
|Alterac Mountains|6|6,405|0|
|Ashenvale|39|73,820|0|
|Darkshore|1|165|0|
|Stormwind|25|22,025|2|
|Ironforge|13|27,910|0|
|Loch Modan|5|6,175|0|
|Westfall|1|1,700|0|
|Elwynn Forest|7|9,855|0|
|Arathi Highlands|21|55,620|1|
|Silverpine Forest|1|265|0|
|Dun Morogh|1|1,750|0|
|**total zone tables**|283|478,200||

### 5.4 Dungeon quest XP totals (class-free, Section 1 tables; excludes dailies, repeatables, type-62; Dalaran is a bonus set not in the brief)

|dungeon|quests (all listed, req<=35)|XP|unk XP|req 18-30 only: quests|XP|
|---|---|---|---|---|---|
|Ruins of Lordaeron|5|9,625|0|0|0|
|The Stockade|6|14,500|0|5|12,150|
|Blackfathom Deeps|6|13,400|1|5|10,650|
|Excavation Site: Wetlands|9|20,660|0|9|20,660|
|Gnomeregan|20|35,305|3|20|35,305|
|Razorfen Kraul|4|11,550|0|4|11,550|
|Scarlet Monastery|3|11,100|0|2|6,400|
|City of Dalaran|4|15,800|0|4|15,800|
|**total req 18-30**|||||112,515 (49 quests)|

Sanity: XP needed 20 -> 30 = 281,000; 20 -> 31 = 318,300. Zone-table req 18-30 raw quest XP (478,200) plus dungeon req 18-30 (112,515) is 590,715 before decay, i.e. about 2.1x the XP of levels 20-30. Call of Water (Shaman) adds 9,580 XP (Atlas guide quotes ~10,000-10,500).
