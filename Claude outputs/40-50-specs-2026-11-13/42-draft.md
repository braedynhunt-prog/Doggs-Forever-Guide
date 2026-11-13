# Spec 42 - Riverglades: the Farholde loose ends (drafted 13 Nov 2026)

Data used (read 13 Nov 2026 unless noted): `tooling/qdb` = QuestieDB Forever 1.0.16 (META.json); `data/zone_16591.json` and `data/zone_16842.json` (Wowhead zone pages, browser pull 12 Nov: XP, money, side, rewards); `data/wowhead_quest_links.json` (Wowhead quest pages: start, end, Series box; 11-12 Nov); `data/drop_rates.json`; `weights/tooltips/2026-11-12.json`; `python weights/score_items.py --band 40 --tooltips tooltips/2026-11-12.json` (output only, nothing written); nether.wowhead.com/forever/tooltip fetched 13 Nov for items 266148, 267138, 3575, 4304, 268035, 268036 and quests 94829, 94997, 94981, 94963, 95295, 95296, 95219, 94891, 94894; `tooling/client/1.60.1.70938/TaxiNodes.csv` + `TaxiPath.csv`; round-1 records `Claude outputs/30-60-specs-2026-11-11/38.md`, `40.md`, `41.md`, `riverglades_sheet.txt`, `riverglades_pull_results.txt`; chapters `38_RivergladesI.lua`, `40_RivergladesII.lua`, `41_PowderfusePort.lua`.

**Prerequisites:** quest rows [11] and [12] are empty for every quest of this chapter and for all the pickups (94829 94858 94961 94963 95975 94981 94980 94997 94998 94890 94891 94893 94894 94983 94984 94982 95295 95296 95219). Every chain order below comes from Wowhead's Series box or from the quest's source item, and is **unverified** in game.

**The main finding:** five of the plan's eight required quests are doubtful on the data. Two are out by rule 12 (94829 at 7.26%, and 94858 behind it); three sit in Wowhead's series behind quests that are out (94963 behind 94961, 95975 behind 95988 > 95957, 94891 behind the elite 94890) and are written here as "if offered" `[O]` lines. Lingering Essence / Curios of Curiosity have no series on file but carry a satchel item that reads like the follow-up of the dungeon's Twilight Mementos. See section 10.

## 1. Header
- File: `42_RivergladesIII.lua`, footer group "Forever Shaman 30-60".
- `[N 42-43 Riverglades]` (plan). Next: `[NX 42-43 Krol'dok Stronghold]` (plan's chapter 43 title).
- `[GA Alliance]`; the gear line is `[A Shaman]`.
- `[D ...]`: "Back to the Riverglades at 42: Friz Frazzlespark's errands at Powderfuse Port, Fuzzle's escape from Sunnyglade, Sergeant Riftan at the Twilight's Shroud, and the Farholde Keep hand-ins and Krol'dok Stronghold pickups before the trip to Ironforge."
- Level on entry **42.0** (plan XP table). Exit: the plan's 25,400 XP gives 42.4; this spec's plain quests give 10,200 XP (about 42.15 by the plan's own ratio) and 20,700 if all three offer-gated quests are offered (about 42.3). Ratio = 0.4 level per 25,400 XP, from the plan's row; nothing typed from the XP table.
- **Level-check line (first `[OC]`):** "This chapter wants level 42. Its pickups need at most level 40 (From Port to Port, Eye of Mugg); the limit is Sergeant Riftan's post at the edge of the Twilight's Shroud, where Twilight Fanatics and Corrupters are 42-43 and Champions 43-44. Fuzzle's escort runs through Sunnyglade's cultists (37-40). Under 42: do the port and Fuzzle first (they are first anyway) and reach Riftan from the east without pulling the Shroud."
  - Data: 256795 Twilight Fanatic L42-43, 256797 Twilight Corrupter L42-43, 256799 Twilight Champion L43-44 (spawns x25-42 y32-55); 256798 Neophyte L37-38, 254560 Shadowmancer L39-40, 256952 Raider L39-40 (Sunnyglade). Highest required level: 95219 req 40, 94982 req 40, 94984 req 39, the rest 36-38.

## 2. Entry state
- Stands in **Farholde Keep** (chapter 41's last step is `Hearth to [H Farholde Keep]`, 41_PowderfusePort.lua:79). **Hearth = Farholde Keep** (bound `[S Farholde Keep]` 38:39; every later hearth goes there: 39e:65, 40:50, 41:79). The hearth is **on cooldown** at the start (just used).
- Carried in: nothing required. Conditional: if he handed in **94892 Dying Wish** in chapter 40 (40:52, only if the 1.6% Field Marshal's Log dropped in 38) and left Delivering Closure as 40:52 told him, Demar Brant now offers 94893 (Leg E).
- Chapter 41's optional Friz block (94928 > 95288 > 95293 > 95294) decides whether Friz offers 95296 (Leg B).
- Professions: no trainer, recipe or skill gate falls here (plan Threads: none for 42). Key Ingredients wants **4 Thick Leather** (he skins; Leatherworking since 6 Nov) and **12 Iron Bars** (see Leg A).
- Training: none here. The level-42 shaman row is chapter 43's Ironforge stop.

## 3. Travel and hearth
- In: already at Farholde Keep.
- Flight master: [TAR257087 Gretchen Mayberry] <Gryphon Master>, Farholde Keep, **60.9,80.9 Riverglades** (as 38:38; qdb has 14 points x58-63 y78-83). Farholde Keep links (TaxiPath 70938): Lakeshire, Morgan's Vigil, Thelsamar. Powderfuse Port has an Alliance node (3275) with **no TaxiPath link**: no flight there.
- Innkeeper: [TAR257595 Barracks Master Harlan] 64.6,84.2 (qdb 3 points 62.9-65.2, 82.1-84.1). No rebind: hearth stays Farholde Keep (plan Threads: Farholde through chapter 45).
- Roads (not in the data, unverified): Keep -> Powderfuse Port as chapter 41 rode it ("past the north side of Farholde Keep and up the coast road north-east", 41:17, Painted Hide at 72.3,61.8 on the way). Port -> Sunnyglade: back south-west to the Painted Hide, then west past Terral's Watch (Watcher Cornelius 59.5,64.0) and north-west into Sunnyglade. **Keep south of Rog'mar** (Horde: Rog'mar Grunt 255996 L55, 71 points x53-62 y38-55; Grakna 255993 L55 elite wind rider master 59.4,45.7).
- Back: `Hearth to [H Farholde Keep]` at Riftan (Leg D); if still on cooldown, ride east past Sunnyglade and Wheeler's Grange (40:50 wording).
- Out: the chapter ends at Farholde Keep. Chapter 43 opens at Gretchen Mayberry with `Fly to [F Ironforge]` (Farholde Keep - Thelsamar - Ironforge: TaxiPath 11588 Farholde->Thelsamar exists, and Thelsamar->Ironforge; both nodes known: `[P Farholde Keep]` 38:38, `[P Thelsamar]` 02:43).
- Rule-1 zone note: no new hub; Farholde Keep, Powderfuse Port, Sunnyglade and the Shroud were all visited in 38/40/41.

## 4. Route (play order)

Coordinates: qdb spawn centres unless marked "(Wowhead map, not in qdb)".

### Leg A - Farholde Keep: Alphonse Dumas
1. `[OC]` level check (section 1).
2. `[OC]` Carried in / overview: "Hearth = Farholde Keep (on cooldown). Nothing required is carried in. Delivering Closure is yours only if you handed in Dying Wish in chapter 40. Friz Frazzlespark's Tanaris errand depends on chapter 41's optional smuggling block."
3. At [TAR259250 Alphonse Dumas] <Journeyman Blacksmith>, **64.5,82.0 Riverglades**: `[QA94981 Key Ingredients]` - 3,300 XP + 55s; req 38, L41; "Bring 4 Thick Leather and 12 Iron Bars to Alphonse Dumas" (tooltip 13 Nov: Thick Leather x4, Iron Bar x12). Reward: Krol'dok Compound Key 267089 (item class 13 key; what it opens is not in the data). **Plain** (Dumas's npc row starts [94981]; no series on file). Story note, unverified: Dumas is also the ender of 94980 Krol'dok Moulding (a dungeon drop), so in game he may offer Key Ingredients only after the moulding; if he does not offer it, skip both Key Ingredients lines and leave it to chapter 43.
   - Materials: Thick Leather 4304 (sells 3s; not sold by any Riverglades NPC: item row [13] vendor = 14846 only). Iron Bar 3575 (sells 2s; **no vendor and no drop in qdb**, item rows [1]/[13] empty). He has no Mining since the 6 Nov switch (docs/audit-2026-11-06.md:3), and the DB has **no auctioneer in the Riverglades** (scan of zone 16591 npc subnames). So:
4. `[OC]` + conditional hand-in, written both ways: "If you already carry 12 Iron Bars and 4 Thick Leather, hand it in now. Otherwise keep it: buy the Iron Bars at the Ironforge Auction House in chapter 43 and hand it in when you are back at Farholde Keep for the Stronghold." Lua: `[O]If you have the bars and leather: at [TAR259250 Alphonse Dumas], [QT94981] (3,300 XP + 55s) [G64.5,82.0 Riverglades]`. Chapter 43's spec must carry the AH purchase and the `[QT94981]` (see section 7).

### Leg B - Powderfuse Port: Friz Frazzlespark and Gray Dawnbright
5. Travel: ride to Powderfuse Port (road as 41:17, unverified) `[G77.2,52.9 Riverglades]`.
6. At [TAR255897 Friz Frazzlespark] <Specialty Goods>, **77.1,52.9 Riverglades** (41 wrote 77.2,52.9; qdb 77.1,52.9, one point; both within 3):
   - `[QA95295 I Know a Guy]` - 315 XP, 0 money; req 36, L40, side Both; "Speak to Friz's contact in Booty Bay" -> **Caravaneer Ruzzgot 3945, Stranglethorn Vale 27.4,74.1, chapter 45**. Wowhead series `95295 > 95322 > 95325` (first in its series). **Plain.**
   - `[QA95219 From Port to Port]` - 330 XP, 0 money; req **40**, L41, side Alliance; source item Cask of Powderfuse Port 276068; "Deliver the Cask of Powderfuse Port to Mardrack Greenwell at Feathermoon Stronghold" -> **Mardrack Greenwell 7941, Feralas 31.0,43.1, chapter 47**. No series on Wowhead. **Plain.**
   - Neither row names the smuggling block (rows [11]/[12] empty, 95295 heads its own series, 95219 has none), so both are written as plain; that Friz offers them without A Few Furs for Friz is unverified (41.md F5 expected "possibly 95295" after 95294).
7. Same NPC, `[O]` line: `[QA95296 Shipping and Handling]` - 315 XP, 0 money; req none in qdb (Wowhead page req 36), L40, side Both; "Speak with Wharfmaster Steamfizzle at Steamwheedle Port in Tanaris" -> **Wharfmaster Steamfizzle 260405, Tanaris 67.6,23.1, chapter 46**. Tooltip: "Requirements: Money: 10" in silver markup (10s, taken at the hand-in, unverified). Wowhead series **`95294 > 95296 > 95383 > 95312 > 95321 > 95472`**: it follows **95294 Smuggler's Bargain**, the last step of chapter 41's optional Friz block. Line text: "If you did Friz's smuggling quests in chapter 41 he offers it; if he does not offer it, skip this line (his Tanaris chain in chapters 46 and 49 goes with it)". Label: conditional (offer-gated). See section 10, item 6.
8. At [TAR263120 Gray Dawnbright], **78.8,54.2 Riverglades**, `[O]` line: `[QA95975 Her World]` - 3,300 XP, 0 money; req 36, L41, side Alliance; "Gather 20 Wildflowers and deliver them to Tessa Dawnbright in Farholde Keep" (Wildflower 271823 x20, from the **Wildflower** object 648994: 683/683 = 100% on Wowhead's item page, riverglades_pull_results.txt:37; **the object has no spawn in qdb and its map was never pulled**). Ender Tessa Dawnbright 263089, Farholde Keep 63.9,82.2. Wowhead series **`95988 > 95957 > 95975`**: 95988 Goes Down Smooth (Crawler Spittle 12.21%, out in round 1, 38.md:124) and 95957 Drink Up! come first. Line text: "If Gray offers it (Wowhead puts it after Goes Down Smooth and Drink Up!, which the guide skips); otherwise skip this line and the Wildflower line". Label: conditional (offer-gated).
9. `[O]` Gather 20 Wildflowers `[QC95975]` - position **Needs pull** (object 648994 map). If the pull shows them round Farholde Keep, the step moves to Leg E before Tessa; if along the port road or Sunnyglade, it goes in Leg C. The writer must not invent a `[G]`.

### Leg C - Sunnyglade: Fuzzle
10. Travel: from the port south-west past the Painted Hide (72.3,61.8) and Terral's Watch (59.5,64.0), then north-west to Sunnyglade; keep south of Rog'mar (section 3). `[G47.3,51.4 Riverglades]`.
11. `[OC]` danger: "Ghostmaw, a level-42 elite crocolisk, roams the Sunnyglade water (47-54,42-57) - Fuzzle stands at its west edge" (40:35 wording; npc 263380). Cultists here: Neophytes 37-38, Shadowmancers and Raiders 39-40.
12. At [TAR259158 Fuzzle], **47.3,51.4 Riverglades**, `[O]` line: `[QA94963 Biting the Hand]` - 3,150 XP + **50s**; req 36, L40, side Both; text "<Fuzzle snarls.>"; objective (tooltip 13 Nov) "Help Fuzzle escape Sunnyglade". Ender: the **Fuzzle's Treasure** object 625582, **41.6,47.7 Riverglades** (qdb, one point; Wowhead map 41.7,47.7). Wowhead series **`94961 > 94963`**: 94961 Biting the Hand (20 Twilight Finger Bones, 16.2%) is out by rule 12. Line text: "If Fuzzle offers the escort (Wowhead puts it after the finger-bone quest, which the guide skips); otherwise skip the Fuzzle lines". Label: conditional (offer-gated). Do NOT take 94961 (silent).
13. `[O]` Escort Fuzzle out of Sunnyglade to his treasure `[QC94963]` `[G41.6,47.7 Riverglades]` (escort path not in the data; cultists 37-40 on the way).
14. `[O]` At the Fuzzle's Treasure object: `[QT94963]` (3,150 XP + 50s) `[G41.6,47.7 Riverglades]`. Tag: an object ender; no `[TAR]` (round 1 writes object steps without one, e.g. 41:18 the Painted Hide).

### Leg D - The Twilight's Shroud: Sergeant Riftan
15. Travel: west from the treasure (~11 units) to Riftan `[G30.4,49.0 Riverglades]`.
16. `[OC]` danger: "Overlord Kilgar, level 46 elite, walks the Shroud north of Riftan (qdb 17 points x26-31 y40-47, the nearest at 30.9,46.9, two units north of Riftan): approach from the east and do not go north". (npc 256881, L46, rank 1.)
17. At [TAR258023 Sergeant Riftan], **30.7,49.1 Riverglades** (40 wrote 30.4,49.0; within 3 of the one qdb point):
   - `[QA94983 Twilight Mementos]` - 4,300 XP, 0 money; req 38, L42; "Collect 8 Cultist Bangles from the Twilight's Hammer in Krol'dok Stronghold" (Twilight Bangle 267234, 11.4% over six elite droppers, drop_rates.json 12 Nov). **Dungeon grind / luck (chapter 43)**: picked up because it costs nothing on the way in (rule 2); abandoned with `[QS]` in 43 if the bangles do not drop on the one run. Line note: "grind / luck: Krol'dok Stronghold, chapter 43".
   - `[QA94997 Lingering Essence]` - 3,450 XP + 55s; req 38, L42; source item Satchel of Cursed Mementos 268035 (Quest Item, Unique); "Bring the Satchel of Cursed Mementos to Ashe Amberhall in Farholde Keep" -> Ashe Amberhall, Leg E. **Plain** (Riftan's npc row starts [94888, 94889, 94890, 94891, 94983, 94997, 96015]; no series on file). Fallback `[OC]` right after: "If Riftan does not offer Lingering Essence yet, it probably follows Twilight Mementos: skip it and Curios of Curiosity here; chapter 43 takes them up if the bangles drop." (unverified; section 9).
18. Same NPC, `[O]` line: `[QA94891 News to Farholde]` - 4,050 XP, 0 money; req 38, **L46**; source item **Kilgar's Head 265837** (the head of the elite Overlord Kilgar, 100% from him, drop_rates.json 12 Nov); "Return to Ashe Amberhall in Farholde Keep"; reward Farholde Keep Tabard 275042 (fixed). Wowhead series **`94890 > 94891`**: 94890 Bring Me His Head (kill Overlord Kilgar, L46 elite) is out by rule 13. What the data shows: qdb rows [11]/[12] empty, Riftan's npc row lists 94891 among his starts, and the quest hands you the head itself (row [10] = 265837), so nothing in the data needs the kill; Wowhead's series says it follows 94890. Line text: "If Riftan offers News to Farholde without Bring Me His Head (unverified); otherwise skip this line". Label: conditional (offer-gated). Do NOT take 94890 (silent).
19. `Hearth to [H Farholde Keep]` (on cooldown? ride back east past Sunnyglade and Wheeler's Grange) `[G30.4,49.0 Riverglades]`.

### Leg E - Farholde Keep: hand-ins and the Stronghold pickups
All within 3 units of 65,82.
20. At [TAR257591 Ashe Amberhall], **66.8,81.1 Riverglades** (38/40 wrote 66.7,81.1): `[QT94997]` (3,450 XP + 55s) `[QA94998 Curios of Curiosity]` - 3,450 XP + 55s; req 38, L42; source item Satchel of Mementos 268036; "Bring the Satchel of Mementos to Melanie Sable" -> Melanie Sable 259287. **Plain** (Ashe's npc row starts 94998). Reward choice: Curio-Adorned Necklace 279850 (only choice; gear call 1).
21. Same NPC, `[O]` line: `[QT94891]` (4,050 XP) - only if you carry it.
22. At [TAR259287 Melanie Sable] <Expert Enchanter>, **66.2,83.4 Riverglades**: `[QT94998]` (3,450 XP + 55s). Gear `[OC][A Shaman]` (section 5).
23. `[O]` At [TAR263089 Tessa Dawnbright], **63.9,82.2 Riverglades** (38 wrote 63.8,82.2): `[QT95975]` (3,300 XP) - only if you carry it with 20 Wildflowers.
24. At [TAR257558 Demar Brant] <Knight Commander>, **66.7,81.0 Riverglades**: `[QA94984 Tome of Twilight]` (4,650 XP, 0 money; req 39, L44; kill Nar'gurk 258964 in Krol'dok Stronghold for the Tome of Twilight 267104; ender Ashe Amberhall; **normal (boss item, one kill)**, chapter 43; Wowhead series 94907 > 94984, and 94907 A Small Favor was handed in at 40:51) and `[QA94982 Eye of Mugg]` (4,850 XP + 1g 30s; req 40, L45; "proof of their leader's demise", Eye of Mugg 267086 from Overlord Mugg 258968; ender Demar Brant; **normal (boss item, one kill)**, chapter 43). Both quests are also offered by Ashe (quest row [1] = [257558, 257591]); the writer may put them on the Ashe line of step 20 instead to save a click.
25. Same NPC, `[O]` line: `[QA94894 The Twilight Threat]` - 4,850 XP, 0 money; req 38, L45; source item **Kilgar's Head 265837**; "Deliver Kilgar's Head to Bolvar Fordragon within Stormwind Keep" -> **Highlord Bolvar Fordragon 1748, Stormwind City 80.2,38.4, chapter 45**. No series on Wowhead, rows [11]/[12] empty; it hands over Kilgar's Head like 94891, so it most likely needs the same Kilgar kill or News to Farholde first. Line text: "If Demar offers it (most likely only after News to Farholde); otherwise skip this line". Label: conditional (offer-gated). Order: after step 21, so a News to Farholde hand-in comes first.
26. Same NPC, `[O]` line: `[QA94893 Delivering Closure]` - 4,200 XP + 70s; req 36, L47; source item Marshal Ryan's Crest 266428; "Deliver Marshal Ryan's Crest to Abigail Lawson in the Cathedral Square of Stormwind City" -> **Abigail Lawson 278088, Stormwind City 50.2,51.8, chapter 45**. Condition: **only if you handed in Dying Wish (94892) in chapter 40**. Data: Wowhead series `94885 > 94887 > 94892 > 94893` (the Field Marshal's Log chain, which starts from a 1.6% drop in chapter 38, 38:110); the crest is the source item of both 94892 and 94893 (item 266428 row [14] = [94892, 94893]); qdb rows [11]/[12] empty; 40:52 told him Demar "then offers Delivering Closure ... leave it for the 40-50 guide". Line text: "Only if you handed in Dying Wish in chapter 40".
27. `[OC]` If he holds the bars now and skipped step 4: "At Alphonse Dumas (64.5,82.0) hand in Key Ingredients if you bought the bars on the way; otherwise it rides on to chapter 43." (Optional; the writer may drop this if step 4 suffices.)
28. **Last step** - `[OC]` Check (section 7), at the flight master: `[G60.9,80.9 Riverglades]` is not allowed on a text line (writing rule: coordinates on quest lines only), so the Check is an `[OC]` with no `[G]`. He stands in **Farholde Keep** with hearth on cooldown (used in Leg D), hearth bound to Farholde Keep, next to Gretchen Mayberry; chapter 43's first step is the flight to Ironforge.

### What is not taken (silent in the Lua, rule 4)
94829, 94858 (section 10, item 1), 94961, 94890 and every other out quest in section 6. Do not mention them in the Lua.

## 5. Gear calls
1. **94998 Curios of Curiosity** -> **Curio-Adorned Necklace** 279850 (neck, BoP, ilvl 44: +9 Int +7 Spi, Equip +5 spell damage/healing; sells 69s 86c; tooltip 2026-11-12) = **42.7 [30.7]** on the level-40 band. Only choice, so no runner-up among the rewards. It beats every neck the guide has offered him: Amberglow Talisman (39d:13, +1 Agi +7 Sta +10 Spi) 26.1 [16.1], Giantstone Medallion (22:61, +10 Spi) 25.0, Thermaplugg Medal of Honor (+6 Sta +6 Spi +10 AP) 25.0, Explorers' League Commendation (34:53, +9 Sta +9 Spi) 22.5, Kodobone Necklace (33:89, +7 Sta +4 Spi) 10.0 (central weights spi 2.5, int 1.69, sp 2.0, ap 1.0, sta 0, agi 1.12; the three last numbers computed by hand from those weights, the first two read from the scorer). Line: "|cff66ff66Curio-Adorned Necklace|r (neck +9 Int +7 Spi +5 spell power; 42.7 on the weights): wear it - it beats any neck so far (Amberglow Talisman 26.1, Giantstone Medallion 25.0)".
2. **94891 News to Farholde** (if done) -> Farholde Keep Tabard 275042 (tabard, no stats; sells 1g 25s): cosmetic, keep or vendor.
3. **94981 Key Ingredients** -> Krol'dok Compound Key 267089 (Unique, BoP, item class 13): keep it for the Stronghold (what it opens is not in the data).
4. 94963 gives 50s, 94997 / 94998 55s each: no items.

## 6. Out (the zone's quests not in this chapter; silent)
Riverglades (from `_decisions.tsv`):
- 94679 Snargl's Snout - elite outside a dungeon (rule 13): Snargl (40 elite); the reward is cloth
- 94961 Biting the Hand - drop under 30%: Twilight Finger Bone 16.2% (4 droppers, best Twilight Neophyte 18% of 4379)
- 95562 Cut Off the Heads - elite outside a dungeon (rule 13): Chogg'Zac (41 elite)
- 95986 King of the Wild Plains - elite outside a dungeon (rule 13): Ombassa (41 elite)
- 95120 WANTED: Old Rot-Chum - elite outside a dungeon (rule 13): Old Rot-Chum (42 elite)
- 95935 Hail the Dragonslayer - Braedyn's 11 Nov ruling
- 95261 It Takes Guts - drop under 30%: Beast Entrails 13.2% (19 droppers, best Juvenile Paletusk 46% of 83)
- 95912 WANTED: Blademaster Kaijo - elite outside a dungeon (rule 13): Blademaster Kaijo (42 elite)
- 94926 Drop the Hammer - elite outside a dungeon (rule 13): Komuk (45 elite); no giver in the DB either
- 94890 Bring Me His Head - elite outside a dungeon (rule 13): Overlord Kilgar (46 elite)
- 95326 The Big Payback - drop under 30%: Ruzzgot's Shipment 29.29%
- 95984 Song of the Strider - drop under 30%: Intact Tallstrider Beak 15.56%
- **New here (section 10, item 1):** 94829 What We Lost - drop under 30%: Farmers' Mementos 266148 7.26% (nether tooltip 13 Nov; single dropper Twilight Raider 256952); and 94858 All That's Left - chain behind 94829 (Wowhead series 94829 > 94858). Both were out in round 1 for the same reason (38.md:125, then 6.61%).
- Not in the round-2 pool at all (L36): 95059 Frazzlespark's Crate - see Unsure.
In other chapters of round 2: 95322 95325 (45), 95312 95321 95383 (46), 95327 95472 (49) - Friz's chains; 96771 94980 94983(kill) 94984(kill) 94982(kill) 94969 (43).

## 7. End check
`[OC]` Check text for the writer (adjust to what was offered):
- Handed in here: Lingering Essence (94997), Curios of Curiosity (94998); if offered: Biting the Hand (94963), News to Farholde (94891), Her World (95975); Key Ingredients (94981) if you had the bars.
- In the log, carried out:
  - **94983 Twilight Mementos** (grind / luck), **94984 Tome of Twilight**, **94982 Eye of Mugg** -> chapter 43, Krol'dok Stronghold (hand-ins Riftan 30.7,49.1 / Ashe 66.8,81.1 / Demar 66.7,81.0).
  - **94981 Key Ingredients** if not handed in -> chapter 43 (buy 12 Iron Bars at the Ironforge AH, hand in at Alphonse Dumas 64.5,82.0 when back at the Keep). **Chapter 43's spec must carry this.**
  - **95295 I Know a Guy** -> Caravaneer Ruzzgot, Booty Bay 27.4,74.1, chapter 45.
  - **94894 The Twilight Threat** (if offered) -> Bolvar Fordragon, Stormwind 80.2,38.4, chapter 45.
  - **94893 Delivering Closure** (if Dying Wish was done) -> Abigail Lawson, Stormwind 50.2,51.8, chapter 45.
  - **95296 Shipping and Handling** (if offered; 10s at the hand-in) -> Wharfmaster Steamfizzle, Steamwheedle Port 67.6,23.1, chapter 46.
  - **95219 From Port to Port** (Cask of Powderfuse Port) -> Mardrack Greenwell, Feathermoon 31.0,43.1, chapter 47.
- Hearth = Farholde Keep (on cooldown). Next: fly Farholde Keep - Thelsamar - Ironforge (chapter 43).
- Log size: at most 10 quests carried out.

## 8. Totals
| | quests | XP | money |
|---|---|---|---|
| Plan (XP table row 42) | 8 | 25,400 | 2g 15s |
| This spec, plain | 3 (94981, 94997, 94998) | 10,200 | 1g 65s |
| This spec, conditional (offer-gated `[O]`) | 3 (94963, 95975, 94891) | 10,500 | 50s |
| Out by rule 12 (new) | 2 (94829, 94858) | 4,700 | 0 |
10,200 + 10,500 + 4,700 = 25,400; 1g 65s + 50s = 2g 15s. XP per quest from `qinfo.py` / zone JSON: 94829 2,350; 94858 2,350; 94963 3,150 (+50s); 95975 3,300; 94981 3,300 (+55s); 94997 3,450 (+55s); 94998 3,450 (+55s); 94891 4,050. No quest is six or more levels below 42, so none is scaled.
Pickups for later chapters carry no XP here: 95295 315, 95296 315, 95219 330, 94894 4,850, 94893 4,200, 94983 4,300, 94984 4,650, 94982 4,850 (counted in chapters 45-47 and 43).
Optional XP (plan): 0. Of the hand-in at 94981, 3,300 XP may move to chapter 43.

## 9. Unverified / in-game test list, Needs pull, Unsure
**In-game test list:**
- Fuzzle offers Biting the Hand (94963) without 94961.
- Gray Dawnbright offers Her World (95975) without 95988 / 95957; where the Wildflowers grow.
- Sergeant Riftan offers News to Farholde (94891) without Bring Me His Head (plan test list already); Demar offers The Twilight Threat (94894) without it.
- Riftan offers Lingering Essence (94997) before Twilight Mementos (94983) is done.
- Alphonse Dumas offers Key Ingredients (94981) before Krol'dok Moulding (94980); what the Krol'dok Compound Key opens.
- Friz offers I Know a Guy (95295), From Port to Port (95219) and Shipping and Handling (95296) without the chapter-41 smuggling block; whether 95296's 10s is taken at the hand-in.
- Road port -> Terral's Watch -> Sunnyglade south of Rog'mar; Fuzzle's escort path.

**Needs pull (Wowhead pages, browser):**
- Object 648994 Wildflower: its map (decides where step 9 goes and its `[G]`).
- Quest pages 94997, 94998, 94983 and 94981 / 94980: their Series boxes (is Lingering Essence after Twilight Mementos? is Key Ingredients after Krol'dok Moulding?). These decide whether 6,900-10,200 XP of this chapter can be done before the dungeon.
- Quest page 94894: whether anything lists it in a series with 94890 / 94891.

**Unsure:**
- 95059 Frazzlespark's Crate (280 XP, L36, req 36, Alliance; Friz 77.1,52.9 -> Demar Brant 66.7,81.0) is not in the round-2 pool (below quest level 39) and round 1 left it open (41.md Unsure). It fits this route exactly (pickup in Leg B, hand-in in Leg E). Main session decides; not in the spec's lines.
- Whether 94997 / 94998 should be written plain (as here: no series evidence) or as "if offered" like the others. If the Needs-pull shows them after Twilight Mementos, they move to chapter 43 as conditional on the bangles (grind / luck, 11.4%), i.e. they would become conditional quests, not required.
- The working tree holds uncommitted edits to `Claude outputs/40-50-plan-2026-11-12/decide_r2.py` and `pool/_decisions.tsv` that I did not make (rows 8406, 737, 687; none in categories 16591 / 16842). I read the file as it stood.

## 10. Deviations from the route plan
1. **94829 What We Lost and 94858 All That's Left are out (rule 12)**, -4,700 XP. Farmers' Mementos 266148: item row [1] = [256952] Twilight Raider only; nether tooltip 13 Nov "Dropped by: Twilight Raider, Drop Chance: 7.26%"; 5 needed = ~69 kills. The plan's decision script read no drop because quest row [9] (objectives) is null for 94829 - the item is named only in the text ("Collect 5 Farmers' Mementos from Twilight Raiders") and the tooltip ("Farmers' Mementos x 5, Mementos buried x 5"). 94858 is behind it in Wowhead's series (`[[94829, 94858]]`, wowhead_quest_links.json), so it goes with it (rule 12: "out, silently, with every quest behind it in its chain"). Round 1 ruled both out the same way (38.md:125). If Braedyn keeps them anyway, the lines are: Farmer Elbrim 258697 at 52.8,42.4 (both quests); Twilight Raiders L39-40 around the farm (271 points x34-65 y30-61) for 5 Farmers' Mementos (~7% - budget ~69 kills) and 5 graves west of the farm (not in the data); then 94858: Discarded Doll from the Discarded Doll object 622001 "in the nearby barn" (100%, no position in qdb) and the Damaged Locket from Converted Farmer 259258 L41 at 53.5,43.9 (8 points; 75.0% single dropper, tooltip 12 Nov - 1 kill, budget 2).
2. **94963, 95975, 94891 become offer-gated `[O]` lines** ("if offered"), 10,500 XP conditional. Each is in a Wowhead series behind an out quest: 94963 behind 94961 (16.2%, rule 12); 95975 behind 95988 (12.21%, rule 12) and 95957; 94891 behind 94890 (elite, rule 13). qdb shows no prerequisite for any of them, so they may be offered; the plan already marked 94891 unverified. Written the other way (plain), each would hold the cursor if not offered. Round 1 used the same "if offered" `[O]` form (38:61 Stepped Out, 41 Argo's line).
3. **94997 / 94998 kept plain but may belong after the dungeon.** Lingering Essence is given by Twilight Mementos's giver and ender (Riftan) and hands over a "Satchel of Cursed Mementos"; Twilight Mementos collects bangles "from the Twilight's Hammer in Krol'dok Stronghold". No series data exists for either, so the spec keeps the plan's placement with a skip-if-not-offered fallback (step 17). Needs pull settles it.
4. **94981's hand-in may move to chapter 43** (3,300 XP + 55s): 12 Iron Bars have no vendor or drop in qdb, he has no Mining, and the Riverglades has no auctioneer; the nearest AH on the route is Ironforge at chapter 43's start.
5. **For chapter 45 (not this chapter's totals):** 94893 Delivering Closure (4,200 XP, listed required in 45) exists only after 94892 Dying Wish, the end of the 1.6% Field Marshal's Log chain (38:110, 40:52): it is conditional, not required. 94894 The Twilight Threat (4,850, required in 45) hands over Kilgar's Head like 94891 and is offer-gated the same way. Up to 9,050 XP of chapter 45's required total is doubtful.
6. **For chapters 46 and 49:** 95296 Shipping and Handling heads a chain the plan counts as required (95296 315, 95383 315, 95312 315, 95321 3,150 in 46; 95472 2,350 in 49 = 6,445 XP), and Wowhead's series puts 95294 Smuggler's Bargain - the end of chapter 41's **optional** Friz block (94925 A Fur Trade, 48% hides) - in front of it. Without that block the whole chain may not be offered. The plan did not see this because 95296 has no qdb prerequisite. Written both ways here (step 7).
7. Friz's errands otherwise: 95295 and 95219 have no gate in the data (95295 heads its own series; 95219 has none) - plain, as the plan has them.
