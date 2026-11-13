# Spec 43 - Krol'dok Stronghold (dungeon) (drafted 13 Nov 2026)

Plan: `docs/40-50-plan-2026-11-12.md`, "### 43 Krol'dok Stronghold (dungeon)"; route line `== 43` in `docs/40-50-route-2026-11-12.txt` (required 96771 94984 94982; opt 94980 94983 94969).

Data used (all read 13 Nov 2026): tooling/qdb (QuestieDB Forever 1.0.16: quest rows [0] [1] [2] [3] [4] [7] [9] [11] [12], npc rows [0] [3]-[6] [13], item rows [0] [1]); data/zone_16842.json (Wowhead Forever, browser 2026-11-12: level, req, XP, money, side, itemchoices); data/drop_rates.json (items 267234 row 2026-11-12 per-mob, 267104 and 267086 single-dropper tooltip rows 2026-11-12); data/browser/r2_pages_2026-11-12.tsv and r2_pages2_2026-11-12.tsv (NPC lines 258964, 258968, 268423, 259256; ITEM line 267234); weights/tooltips/2026-11-12.json; nether.wowhead.com/forever/tooltip (shell, 13 Nov: quest 94969, quest 96771, item 267138, item 267089, items 279851 / 279929 return nothing); tooling/trainer_costs.json (Eldrun 258098 and Balthus 6291, pulled 2026-11-12); docs/forever-shaman-leveling-sheet.html (level 42 row); tooling/client/1.60.1.70938/TaxiNodes.csv + TaxiPath.csv; `python weights/score_items.py --band 40`; a scratch run of weights/enh_weights.py (read-only import, a third and fourth weapon added in memory to WEAPONS_40; nothing written to the repo).

## 1. Header
- File: `43_KroldokStronghold.lua`
- `[N 42-43 Krol'dok Stronghold]` (plan title; required dungeon chapter, no `[O]` on the title)
- `[NX 42-43 Badlands]` (chapter 44's title as the plan has it; copy exactly if 44's spec changes it)
- `[GA Alliance]`; class lines `[A Shaman]`. Footer group "Forever Shaman 30-60".
- Description: `[D Forever Shaman 30-60 (Braedyn)\\Krol'dok Stronghold at 42: the level 42 training in Ironforge, Ranath Nightstride's quest from the Dalaran crater, one run through the Stronghold (Nar'gurk, Zalfan Moonshadow, Overlord Mugg), the Farholde Keep hand-ins, then back to the crater and on to Ironforge.]`
- **First line (level check)** `[OC]`: "|cffffffffLevel check|r  -  this chapter wants level 42: Eye of Mugg and Krol'dok No More! need 40, Tome of Twilight 39, Vengeance of the Highborne 37; the quests are level 41-45 and every Stronghold mob Wowhead lists is elite, but the mob levels inside are not in the data (in-game check). You arrive at about 42.4. Under 42: the Ironforge and Dalaran legs come first anyway; for the run, find a group at 43-45 and keep to its pace. There is no later slot: never a re-run"
- Level on entry 42.4 (plan's XP table); exit about 42.6 on quest XP alone (plus the dungeon's kill XP, not counted).

## 2. Entry state
- Where: Farholde Keep, Riverglades, where chapter 42 ends (plan, chapter 42 note). **Hearth = Farholde Keep**: bound at [TAR257595 Barracks Master Harlan] in chapter 38 (`38_RivergladesI.lua:39`, `[S Farholde Keep]`); chapters 39e, 40 and 41 end with `[H Farholde Keep]` and no later `[S]` exists in 00-41. Chapter 42 (not yet written) is planned to keep it. Whether the hearth is on cooldown at the start depends on chapter 42's last step (see Unsure).
- Quests carried in (all picked up in chapter 42 per the plan; none has a prerequisite in qdb rows [11]/[12]):
  - 94984 Tome of Twilight - from [TAR257558 Demar Brant] or [TAR257591 Ashe Amberhall] (qdb row [1] lists both), Farholde Keep.
  - 94982 Eye of Mugg - same two givers.
  - 94983 Twilight Mementos [O, grind / luck] - from [TAR258023 Sergeant Riftan], who stands at the **Twilight's Shroud, Riverglades 30.7,49.1** (single spawn, npc row [6]), not at Farholde Keep.
  - Krol'dok Compound Key (item 267089, reward of 94981 Key Ingredients in chapter 42; tooltip: "Binds when picked up, Unique", no use text). What it opens is not in the data; keep it in the bags (unverified).
- Not carried in: 96771 Vengeance of the Highborne (picked up in this chapter, leg 3), 94980 (drop-start), 94969 (no giver).
- Gear on entry (two-hander): Rage of the Storm (96016, chapter 39c) or Bonebiter (weights doc 11 Nov section).
- Training in this chapter: the level 42 row at Eldrun Stormbreaker (leg 2). Profession gate: Artisan Skinning at Balthus Stoneflayer, optional (plan Threads: "if not bought at 40").
- Pickups chapter 42 must contain (for the reconciler): `[QA94984 Tome of Twilight]` and `[QA94982 Eye of Mugg]` at Demar Brant 66.7,81.0 / Ashe Amberhall 66.8,81.1; `[QA94983 Twilight Mementos]` at Sergeant Riftan 30.7,49.1 (Twilight's Shroud) as `[O]` grind / luck; `[QT94981]` Key Ingredients (the Compound Key).

## 3. Travel and hearth
Flight graph (TaxiPath build 70938, edges touching the nodes used): Farholde Keep (3276) - Thelsamar (8) / Lakeshire (5) / Morgan's Vigil (71); Thelsamar - Ironforge (6); Ironforge - Southshore (14) / Aerie Peak (43) / Thorium Point (74) / Stormwind (2) / Menethil / Refuge Pointe; Southshore - Aerie Peak / Menethil / Refuge Pointe / Chillwind Camp. Dalaran has no flight point (chapter 28 line 10: "on foot from Southshore"). Morgan's Vigil and Thorium Point are not known yet (plan Threads), so Farholde - Thelsamar - Ironforge is the only way to Ironforge.

Flight masters (qdb / guide lines): [TAR257087 Gretchen Mayberry] Farholde Keep 60.9,80.9 Riverglades (as chapter 38:38 writes it; qdb centroid 61.1,80.8, 14 points); [TAR1572 Thorgrum Borrelson] Thelsamar 33.9,51.0 Loch Modan; [TAR1573 Gryth Thurden] Ironforge 55.5,47.7; [TAR2432 Darla Harris] Southshore 49.3,52.3 Hillsbrad Foothills. Innkeeper (bind): [TAR257595 Barracks Master Harlan] 64.6,84.2 Riverglades (chapter 38 pin; qdb 3 points, centroid 64.2,82.9) - no bind change in this chapter.

**Order of legs and why.** 96771 must be accepted at Ranath before Zalfan Moonshadow dies, so the crater comes before the run; its hand-in is at the same NPC, so the crater is visited twice whatever the order. Ironforge lies on the only flight road from Farholde Keep to Southshore, so the level 42 training costs no detour on the way out. The hearth (Farholde Keep) carries him back from the crater to the dungeon's zone in one step, saving the three-hop flight Southshore - Ironforge - Thelsamar - Farholde. After the run the Farholde hand-ins come first (they are beside the flight master), then the Farholde - Ironforge - Southshore flights and the ride to Ranath, and the chapter ends with the Southshore - Ironforge flight, which is where chapter 44 starts ("From Ironforge: fly Thelsamar", plan chapter 44). Carrying 96771 into chapter 44 instead (Aerie Peak - Southshore is one hop) would save at most one short flight hop and push 4,850 XP and a cross-chapter carry into a spec drafted without it: done here (see Unsure for the alternative).

- In: Farholde Keep - fly Ironforge (the game routes through Thelsamar) - train - fly Southshore - ride to the Dalaran crater - hearth (or Astral Recall) to Farholde Keep - ride to the Stronghold (entrance not in the data, see leg 4).
- Out: Stronghold - (only with 8 bangles: Riftan at the Shroud, then hearth or Astral Recall to Farholde Keep) - Farholde Keep hand-ins - fly Ironforge (via Thelsamar) - fly Southshore - ride to the crater - ride back - fly Ironforge. Ends at Gryth Thurden, Ironforge.
- Ride Southshore - Dalaran crater: on foot, as chapters 27/28 do; the path is not in the data (unverified). Chapter 39c line 45 warns that Crushridge Maulers (36-37) and Mages (37-38) west of x38 between y38 and y51 Alterac are elite - those are level 36-38 against a 42 now, but the warning may be repeated briefly.

## 4. Route

### Leg 1 - Farholde Keep to Ironforge
1. `[OC]` "|cffffffffFarholde Keep|r  -  you start where chapter 42 ended; hearth = Farholde Keep and it stays there. Required chapter: one run of Krol'dok Stronghold, |cFFFF0000GROUP 5|r, never a re-run, plus two visits to Ranath Nightstride in the Dalaran crater. Three normal quests, 14,350 XP and 1g 95s; three more are luck"
2. `[OC]` "|cffffcc00Carried in:|r Tome of Twilight (94984) and Eye of Mugg (94982) from Farholde Keep and, if you took it, Twilight Mementos (94983) from Sergeant Riftan - all from chapter 42. Keep the Krol'dok Compound Key from Key Ingredients (94981): the data does not say what it opens (|cffffcc00unverified|r)"
3. At [TAR257087 Gretchen Mayberry], fly to [F Ironforge] (the game routes it through Thelsamar) `[G60.9,80.9 Riverglades]`. Travel step.

### Leg 2 - Ironforge: level 42 training
4. `[A Shaman]` In the Forlorn Cavern at [TAR258098 Eldrun Stormbreaker], `[T]` the level 42 row `[G47.1,13.8 Ironforge]`. Prices `tooling/trainer_costs.json` (pulled 2026-11-12, Wowhead raw values; the 5% question stays on the test list). Every rank of the row:
   - Grace of Air Totem rank 1 (8835) - 1g 60s - sheet: **buy** ("Grace of Air = your solo air totem")
   - Fire Nova rank 4 (408344) - 1g 89s 47c - sheet: **buy**
   - Windfury Totem rank 2 (10613) - 1g 60s - sheet: **later** ("when gold is easy")
   - Fire Resistance Totem rank 2 (10537) - 1g 60s - sheet: **not listed = don't buy** (legend: "resistance totems")
   - No must in the row (the sheet's level 42 cell has no green entry). Buys 3g 49s 47c; with Windfury Totem 2 5g 9s 47c; the whole row 6g 69s 47c.
   - Suggested line text, in the round-1 format (39d:17): "train every rank your level allows that the sheet marks must or buy (level 42 row: buys Grace of Air Totem 1 - 1g 60s, Fire Nova 4 - 1g 89s 47c; when gold is easy: Windfury Totem 2 - 1g 60s; 3g 49s 47c for the buys)". Talent note the writer may add as `[OC]`: the sheet's talent column at 42 is Improved Healing Wave 2/5 (41-42, Resto); at 43 Water Shield (Resto, green).
5. `[O]` At [TAR6291 Balthus Stoneflayer] in the Great Forge, `[T]` learn Artisan Skinning (5g; trainer_costs.json spell 10768 "level 200" = skill 200) once Skinning is 200 and if not bought in chapter 39d `[G39.9,32.5 Ironforge]`. Gate (rule 11).
6. `[OC]` gold check - see Unsure (the plan says the Ironforge stops get one from `tooling/gold.py` once the chapters exist; quest money through chapter 41 is 36g 91s by `gold.py`, chapter 42 adds 2g 15s per the plan).
7. At [TAR1573 Gryth Thurden], fly to [F Southshore] `[G55.5,47.7 Ironforge]`.

### Leg 3 - the Dalaran crater: Ranath Nightstride
8. `[OC]` "|cffffffffThe Dalaran crater|r  -  on foot from Southshore, the way chapters 27 and 28 went (Dalaran has no flight point). Ranath Nightstride is a level 45 Highborne, friendly (DB faction AH), in the crater"
9. At [TAR268425 Ranath Nightstride], `[QA96771 Vengeance of the Highborne]` (4,850 XP + 65s, requires level 37: slay Zalfan Moonshadow in Krol'dok Stronghold) `[G17.8,66.0 Alterac Mountains]`. Label **normal**. qdb: start = end = 268425, spawn Alterac (zone 36) 17.8,65.95, L45, rank 1 (elite flag on a friendly quest NPC). Objective row [9]: kill 268423 Zalfan Moonshadow x1 (count from the quest text "slay Zalfan Moonshadow"). No prerequisite; nothing names 96771 as a prerequisite. No reward items (zone_16842 itemchoices []).
10. `|cFFfff8a3Hearth to [H Farholde Keep]|r` (on cooldown? Astral Recall does the same; otherwise ride back to Southshore and fly Farholde Keep - three hops through Ironforge and Thelsamar) `[G17.8,66.0 Alterac Mountains]`.

### Leg 4 - Krol'dok Stronghold, one run
11. `[OC]` "|cffffffffKrol'dok Stronghold|r  -  the way in is not in the data. Chapter 40 placed Bolder'ok, the ogre camp, north of Terral's Watch (x64-77 y13-34; ogres 41, with Rog'mar's level 55 Horde guards on the way and the elites Chub'chob 45, Clugfist 50, Komuk 45 and Scoutmaster Vargas 42 at its edges); that the Stronghold opens from there is a guess (|cffffcc00unverified|r). Ask the group or the Farholde guards"
    - Data for the writer (do not put coordinates on the line): the Wowhead NPC pages (12 Nov) put the Stronghold's NPCs on the **Eastern Kingdoms continent map (uiMap 1415)**, not on a zone map - these are continent coordinates, not Riverglades ones, and are not converted here: Nar'gurk 56.8,62.9 / 56.9,62.9; Zalfan Moonshadow 57.1,62.5 / 57.3,62.2; Tunk 58.4,62.5; Overlord Mugg 58.4,60.9 / 58.5,60.9.
12. `[OC]` "|cffffffffThe Stronghold|r  -  |cFFFF0000GROUP 5|r. Every mob Wowhead lists here is elite: the Twilight's Hammer (Grunts, Warlocks, Outriders, Lieutenants, Twilight Commander Zarmok), Nar'gurk the Corruptor, Zalfan Moonshadow, Tunk the Blacksmith and Overlord Mugg. Mob levels and the room order are not in the data. One run, never a re-run. Your quests, with the honest label:"
13. `[OC]` "|cffffcc00?|r Eye of Mugg (94982) - Overlord Mugg - |cff66ff66normal|r, one kill: his eye drops for the quest holder; Wowhead reads 41.67% because it counts every kill, quest or not. 4,850 XP + 1g 30s at Demar Brant"
14. `[OC]` "|cffffcc00?|r Tome of Twilight (94984) - Nar'gurk - |cff66ff66normal|r, one kill (Wowhead 37.84% over all kills). 4,650 XP at Ashe Amberhall"
15. `[OC]` "|cffffcc00?|r Vengeance of the Highborne (96771) - Zalfan Moonshadow - |cff66ff66normal|r: kill quest. 4,850 XP + 65s at Ranath in the crater"
16. `[OC]` "|cffffcc00?|r Twilight Mementos (94983) - 8 Cultist Bangles from the Twilight's Hammer - |cffffcc00grind/luck|r: about 11% a kill (Grunts 12.7%, Outriders 12.4%, Lieutenants 11.2%, Warlocks 9.6%, Zalfan 20.6%, Zarmok 1.8%), about 70 kills for 8. Loot what the run gives; abandon it after the run if you do not have 8"
17. `[OC]` "|cffffcc00?|r Krol'dok Moulding (94980) - |cffffcc00luck|r: Tunk drops the Krol'dok Moulding, which starts a quest for Alphonse Dumas in Farholde Keep (Wowhead 48.44%). One kill only"
18. `[OC]` "|cffffcc00?|r Krol'dok No More! (94969) - escort Marcus Tilwell to safety - |cffffcc00luck|r: neither the DB nor Wowhead names who gives it or where it ends. Take it if someone offers it at the door or inside"
19. `|cFFFF0000GROUP 5|r` Meet the group and enter Krol'dok Stronghold (entrance not in the data, |cffffcc00unverified|r). Writer: this line needs a `[G]` only if check_guide insists; 39e's dungeon lines carry no pin (see Unsure).
20. Kill [TAR258964 Nar'gurk] for the Tome of Twilight `[QC94984]` (one kill; Wowhead 37.84%). Item 267104, single dropper 258964 (item row [1]); tooltip "Dropped by: Nar'gurk, Drop Chance: 37.84%". Elite (Wowhead NPC page). No pin.
21. Kill [TAR268423 Zalfan Moonshadow] `[QC96771]`. Elite (Wowhead NPC page). No pin.
22. `[O]` Luck: if [TAR259256 Tunk] drops the Krol'dok Moulding, right-click it, `[QA94980 Krol'dok Moulding]` (3,300 XP + 55s, requires level 38: to Alphonse Dumas in Farholde Keep). Item 267138: dropper 259256 only (item row [1]), quest start (item row [4] = 94980), tooltip 13 Nov "This Item Begins a Quest, Dropped by: Tunk, Drop Chance: 48.44%". Tunk is Elite (Wowhead). Rule 12: a named mob's drop at 30-60% - one kill only; it is a drop-start, so nothing to abandon if it does not fall.
23. `[O]` Luck: if Krol'dok No More! is offered (by [TAR259253 Marcus Tilwell] or anyone at the door; qdb has the NPC 259253 with no level, spawn or quest link), `[QA94969 Krol'dok No More!]` (3,450 XP, requires level 40) and escort Marcus Tilwell `[QC94969]`. Turn-in NPC unknown: `[QT94969]` wherever the escort ends (writer: an `[O]` line "hand it in where the escort ends; if no one takes it, abandon [QS94969]"). Its two reward choices (items 279851, 279929) have no tooltip anywhere (nether returns nothing): no gear call possible.
24. Kill [TAR258968 Overlord Mugg] for the Eye of Mugg `[QC94982]` (one kill; Wowhead 41.67%). Item 267086, single dropper 258968; tooltip "Dropped by: Overlord Mugg, Drop Chance: 41.67%". Elite. The quest text calls him "their leader"; that he is the last boss is a guess (unverified). No pin.
25. `[O]` Loot the Twilight's Hammer for 8 Cultist Bangles `[QC94983]` (Twilight Bangle 267234, all six droppers elite; per-mob count/outof from drop_rates.json 2026-11-12: [TAR258042 Twilight Grunt] 312/2453 = 12.7%, [TAR258102 Twilight Outrider] 73/588 = 12.4%, [TAR258104 Twilight Lieutenant] 79/707 = 11.2%, [TAR258100 Twilight Warlock] 34/354 = 9.6%, Zalfan Moonshadow 7/34 = 20.6%, Twilight Commander Zarmok 6/333 = 1.8%; overall 11.4%; budget 8 / 0.114 = ~70 kills) - grind/luck: what the run gives, never farm. Single-item quest, so `[QC94983]` is right (no `[CI]` needed). Count 8 from the quest text (row [9] carries no count); the text says "Cultist Bangles", the item row says "Twilight Bangle".
26. `[O]` Fewer than 8 bangles after the run: abandon Twilight Mementos `[QS94983]`.
27. `[OC]` Boss loot calls: none in this chapter (the DB has no loot table for the Stronghold's NPCs: they have no rows [1]-[9]; `dungeon_loot.py` was not run, by the brief).

### Leg 5 - out of the Stronghold: Riftan (only with 8 bangles) and Farholde Keep
28. `[O]` Only with 8 bangles: ride west to [TAR258023 Sergeant Riftan] at the Twilight's Shroud, `[QT94983]` (4,300 XP, no money) `[G30.7,49.1 Riverglades]`. Chapter 40 rode it as "west past Sunnyglade"; the Shroud's cultists are 42-44 (chapter 40 line 34).
29. `[O]` From Riftan: `|cFFfff8a3Hearth to [H Farholde Keep]|r` (or Astral Recall; on cooldown: ride back east past Sunnyglade and Wheeler's Grange, as 40:50 says) `[G30.7,49.1 Riverglades]`. Writer: if Guidelime cannot hold an optional hearth cleanly, fold it into step 28's text.
30. `[OC]` "|cffffffffFarholde Keep|r  -  the hand-ins are beside the flight master"
31. At [TAR257591 Ashe Amberhall], `[QT94984]` (4,650 XP, no money) `[G66.8,81.1 Riverglades]`. Ender = 257591 only (quest row [2]); spawn 66.75,81.1. Gear call 1 goes on this line's `[OC]`.
32. At [TAR257558 Demar Brant], `[QT94982]` (4,850 XP + 1g 30s) `[G66.7,81.0 Riverglades]`. Ender = 257558 only (quest row [2]; "Commander Brant" in the text, subname Knight Commander); spawn 66.67,81.01. Gear call 2 goes on this line's `[OC]`.
33. `[O]` Only with the Moulding: at [TAR259250 Alphonse Dumas], `[QT94980]` (3,300 XP + 55s) `[G64.5,82.0 Riverglades]`. Ender = 259250 (quest row [2]; also listed in npc row [10]); spawn 64.46,82.03; Journeyman Blacksmith. No reward items.
34. At [TAR257087 Gretchen Mayberry], fly to [F Ironforge] (through Thelsamar) `[G60.9,80.9 Riverglades]`.

### Leg 6 - back to the crater, then Ironforge
35. At [TAR1573 Gryth Thurden], fly to [F Southshore] `[G55.5,47.7 Ironforge]`. (Writer may add: anything skipped at Eldrun or Balthus in leg 2 can be done now, `[O]`.)
36. Ride to the Dalaran crater. At [TAR268425 Ranath Nightstride], `[QT96771]` (4,850 XP + 65s) `[G17.8,66.0 Alterac Mountains]`.
37. Ride back to Southshore; at [TAR2432 Darla Harris], fly to [F Ironforge] `[G49.3,52.3 Hillsbrad Foothills]`. Chapter 44 starts at Ironforge.
38. `[OC]` Check line (section 7).
39. `[NX 42-43 Badlands]`

## 5. Gear calls
Weights: level-40 band (`python weights/score_items.py --band 40`, tooltips `weights/tooltips/2026-11-12.json`: central wdps 14, Str 2, Int 1.69, Agi 1.12, Spi 2.5, SP 2.0; conservative Spi 1.5, SP 1.0). Mail counts from 40.

**1. Tome of Twilight (94984), choice of two** (tooltips 2026-11-12):
- Twilight Initiate's Belt (279854): leather waist, 70 armor, +11 Agi +7 Spi, sells 43s 43c - **29.8** (22.8 conservative).
- Torn Cultist Cloak (279855): back, 30 armor, +7 Int, +3 mana per 5 s, sells 51s 89c - 11.8 (7 x 1.69; the scorer has no mp5 term).
- Call: **take the belt only if your belt scores under 29.8** - that is the Violet Sash from chapter 30 (cloth, +9 Int +6 spell damage: 27.2 / 21.2 by hand at band 40) or the Grappler's Belt from chapter 33 (+7 Str +5 Sta: 14.0). It loses to the Blightleaf Rope (30.9, City of Dalaran loot), the Demolition Girdle (34.0) and the Deathmage Sash (39.3, Razorfen Downs loot). The cloak loses to the Chainlink Towel (30.1, in the band-40 kit) and the Drape of Shifting Energy (29.5). Otherwise take the **Torn Cultist Cloak for the vendor** (51s 89c against 43s 43c).
- Suggested line: "|cffffcc00Gear (94984, choice):|r the |cff66ff66Twilight Initiate's Belt|r (leather waist +11 Agi +7 Spi, 29.8 on the weights) only over the Violet Sash or Grappler's Belt; it loses to the Blightleaf Rope, Demolition Girdle and Deathmage Sash. Otherwise take the Torn Cultist Cloak (+7 Int, mana regen) for the vendor (51s 89c)"

**2. Eye of Mugg (94982), choice of three** (tooltips 2026-11-12):
- Bigger Rock on Bigger Stick (279480): two-hand mace, 112-168, speed 3.40, 41.18 dps, +14 Str, chance on hit: "Bash the target in the face, causing 14 Physical damage every 2 sec for 20 sec" (140 damage per proc over 20 s; proc rate not on the tooltip), item level 47, no "Requires Level" line, BoP, sells 2g 84s 48c.
- Stick No Rock (279853): two-hand staff, 80-121, speed 3.30, 30.45 dps, +10 Str +18 Spi, +22 health per 5 s, +101 healing / +33 spell damage, sells 2g 78s 15c.
- Rock on Stick (279852): ONE-hand mace, 31.54 dps, +4 Str - no use to the 2H build; sells 2g 21s 68c.
- Linear band-40 scores (score_items, Two-Hand list): Bigger Rock on Bigger Stick **604.5**, Bonebiter 583.5, Stick No Rock 557.3 (506.3 conservative), Rage of the Storm 529.8 (weights doc 11 Nov; 35.56 x 14 + 16 x 2).
- The weights doc (11 Nov) compared Rage of the Storm and Bonebiter in the kill-speed model, not the linear score, because the linear score cannot see Rage's +10% Stormstrike or the normalised-Stormstrike value of a slow weapon. The same model, run 13 Nov with Bigger Rock on Bigger Stick added (weights/enh_weights.py `scenario_40`, sheet talents, kill-speed optimum; dps 41.18, speed 3.4, +14 Str, no Stormstrike bonus; the bleed proc NOT modelled), kills/hour:

  | weapon | Rockbiter | Windfury | no Stormstrike (RB / WF) |
  |---|---|---|---|
  | Rage of the Storm | 222.4 | 218.2 | 167.5 / 168.4 |
  | Bigger Rock on Bigger Stick | 221.6 | 219.8 | 171.4 / 173.7 |
  | Bonebiter | 220.1 | 217.8 | 170.3 / 172.2 |
  | Stick No Rock | 221.1 | 215.0 | 172.7 / 171.9 |

  (Rage and Bonebiter rows reproduce the doc's 222.4 / 220.1 / 218.2 / 217.8 exactly, so the run is the doc's model.)
- Call: **take Bigger Rock on Bigger Stick and put it on.** With Windfury, which the guide uses on the two-hander from 30 (Braedyn's decision, weights doc 11 Nov), it leads Rage of the Storm by 0.7% and Bonebiter by 0.9%; with Rockbiter it trails Rage by 0.4% and still beats Bonebiter. Every gap is inside the model's ~1-3% resolution, so the tie-breaks decide: it beats Bonebiter on every row and the linear score, it beats Rage without Stormstrike, and its bleed proc adds damage the model does not count. Runner-up: Stick No Rock (557.3; 221.1 / 215.0) - no. It replaces Rage of the Storm or Bonebiter, whichever he swings; the old one sells (Rage 1g 62s 35c, Bonebiter 2g 25s 4c).
- Suggested line: "|cffffcc00Gear (94982, choice):|r take |cff66ff66Bigger Rock on Bigger Stick|r (2H mace 41.18 dps, speed 3.40, +14 Str, a bleed on hit) and put it on: with Windfury it edges Rage of the Storm and Bonebiter (under 1% in the kill-speed model, plus the bleed, which the model does not count). Stick No Rock is a caster staff and Rock on Stick one-handed: pass"

**3. Vengeance of the Highborne (96771), Krol'dok Moulding (94980), Twilight Mementos (94983):** no item rewards (zone_16842 itemchoices / itemrewards empty).
**4. Krol'dok No More! (94969):** choices 279851 and 279929 - no tooltip in the 12 Nov file and none from nether on 13 Nov. No call; Needs pull.

## 6. Out
Nothing of category 16842 that is open to the Alliance is out: `_decisions.tsv` has nine 16842 rows; 94981, 94997 and 94998 are chapter 42 (PLAIN), the six here are kept as required / optional / conditional. The Horde twins on zone_16842 (94968 Eye of Mugg, 94972 Tome of Twilight, 94973 Krol'dok Moulding, 94974 Key Ingredients, 94975 A Token of Vengeance, 95056 Krol'dok No More!; side 2) are not in the pool. Silent in the guide (rule 4).

## 7. End check
Suggested `[OC]` "|cffffcc00Check:|r handed in here: Tome of Twilight (94984), Eye of Mugg (94982), Vengeance of the Highborne (96771); Twilight Mementos (94983) handed in at Riftan or abandoned; Krol'dok Moulding (94980) and Krol'dok No More! (94969) only if they came up. Nothing from this chapter stays in the log."
- Carried out: **none.** (96771 is handed in in leg 6. If the main session prefers the chapter-44 alternative in Unsure, 96771 becomes the one carried-out quest, to Ranath via Aerie Peak - Southshore.)
- Rule 9: 94983 has its `[QS]`; 94980 is accepted only when it can be handed in the same chapter; 94969 has a `[QS]` fallback.

## 8. Totals
- Required: 3 quests, **14,350 XP**, **1g 95s** (96771 4,850 + 65s; 94984 4,650 + 0; 94982 4,850 + 1g 30s; zone_16842.json, browser 2026-11-12). Equals the plan's XP table row (3, 14,350, 1g 95s).
- Optional / conditional: 94980 3,300 + 55s; 94983 4,300 + 0; 94969 3,450 + 0 = **11,050 XP**, 55s. Equals the plan's 11,050.
- Training spent here: 3g 49s 47c for the sheet's buys (6g 69s 47c for the whole row); Artisan Skinning 5g if taken.
- Highest required level among pickups: 40 (94982, 94969); plan column says 40.

## 9. Unverified / in-game test list, Needs pull, Unsure
**Unverified / in-game test list**
- Where the Stronghold's door is and how to reach it from Farholde Keep (plan test list item).
- Mob levels inside; the room order of Nar'gurk, Zalfan, Tunk and Mugg; whether Mugg is last.
- Whether Krol'dok No More! is offered at the door or inside, by whom, and where it ends (plan test list item).
- Whether Tunk's Krol'dok Moulding drops for everyone (plan test list item).
- What the Krol'dok Compound Key (from 94981) opens.
- Zalfan Moonshadow shows only 34 sampled kills on the Twilight Bangle page against 333-2,453 for the other droppers: he may be an optional or hidden boss (or 96771 is newer than the rest). Check that he is on the run's path.
- Bigger Rock on Bigger Stick's bleed proc rate.
- The trainer's price: Wowhead raw or 5% less (Fire Nova 4: 1g 89s 47c or ~1g 80s) - already on the plan's test list.
- The Southshore - crater ride path; the Astral Recall fallback when the hearth is on cooldown (Classic behaviour).
- Whether "8 Cultist Bangles" are the item the DB calls Twilight Bangle (one item on the quest, so very likely).

**Needs pull (only a Wowhead page settles it)**
- Wowhead Forever NPC pages of the Twilight trash (258042, 258100, 258102, 258104, 258972) and the four bosses carry no level field in the 12 Nov pull (the four pulled lines hold classification and map only): the level check stays an estimate until a page or the game gives levels. The zone page 16842 lists no NPCs (data/zone_16842.json "npcs": []).
- Marcus Tilwell (259253) NPC page and quest page 94969 (giver / ender; data/wowhead_quest_links.json has start [] end []).
- Item pages 279851 and 279929 (Krol'dok No More! rewards).
- The Krol'dok Stronghold map (entrance position in Riverglades coordinates).

**Unsure**
- **Level check 42 vs the plan's 43.** Evidence: highest required level 40; quest levels 41-45; all listed mobs elite; no mob levels anywhere in the data. In round 1 the dungeons' top mob level ran about at the top quest level (Razorfen Downs quests ~39-42 with Amnennar 41; Uldaman quests up to 47 with Archaedas 47), which suggests 44-46 bosses here. I wrote "wants 42, group at 43-45" because he arrives at 42.4 and nothing in the chapter raises his level before the run; confidence low. The main session may keep 43 instead.
- **96771 hand-in now or in chapter 44.** Done here: the chapter-44 alternative (Aerie Peak - Southshore - ride - Southshore - Ironforge/Stormwind) saves at most one flight hop and moves a carry into a spec drafted without it. If chapter 44's spec ends up passing Southshore anyway, moving the hand-in there is cheap.
- **Hearth at the start.** If chapter 42 ends with a hearth, the leg-3 hearth may still be on cooldown (60 minutes in Classic) after the Ironforge stop and the crater ride; Astral Recall is the fallback, then the three-hop flight. The writer should copy chapter 42's last line when it exists.
- **The entrance line's `[G]`.** 39e put its dungeon lines without a pin and check_guide passes; the entrance line here has no known coordinate. If check_guide flags it, the main session decides between no pin and a Farholde Keep pin with "from here".
- **Gold check line.** The plan wants one at each Ironforge stop from `tooling/gold.py` once the chapters exist; I have not written one (chapter 42's money is not in a file yet). Quest money through 41: 36g 91s (gold.py, 13 Nov); plan's chapter 42: 2g 15s.
- **The Riverglades leg to the Stronghold** may pass Bolder'ok's elites (chapter 40 lists them); with the entrance unknown I wrote no route.

## 10. Deviations from the route plan
1. **Wants level 42, not 43** (plan: "43 is a placeholder the spec settles from Wowhead's zone page"). The zone page (data/zone_16842.json) has no NPCs and the 12 Nov NPC lines carry no levels, so it cannot settle it; 42 = he arrives at 42.4, highest required level 40. Low confidence (Unsure).
2. **Twilight Mementos is handed in at the Twilight's Shroud, not Farholde Keep.** Sergeant Riftan 258023: one spawn, Riverglades 30.71,49.06 (npc row [6]); quest row [2] = 258023. The hand-in is an optional ride west plus a hearth (steps 28-29). Not a list change.
3. **96771 is handed in within the chapter** (second crater visit, leg 6), and the chapter ends at Ironforge for chapter 44. The plan names only the pickup trip.
4. **Krol'dok Moulding now has a rate**: 48.44% from Tunk (nether tooltip of item 267138, 13 Nov); the plan had none. It stays conditional; rule 12's "one kill only" is written on it.
5. **Artisan Skinning added** as an optional gate at the Ironforge stop (plan Threads: "Artisan Skinning: Balthus Stoneflayer, Ironforge, skill 200, 5g, if not bought at 40"; trainer_costs.json 6291 spell 10768, 50,000 c).
6. Quest list, labels and totals unchanged.
