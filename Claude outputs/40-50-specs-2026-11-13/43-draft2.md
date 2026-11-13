# Spec 43 - Krol'dok Stronghold (dungeon) (13 Nov 2026, revised plan; re-cut of `Claude outputs/40-50-specs-2026-11-13/43-draft.md`)

Plan: `docs/40-50-plan-2026-11-12.md` (revised 13 Nov), "### 43 Krol'dok Stronghold (dungeon)"; route line `== 43` in `docs/40-50-route-2026-11-12.txt`: required 96771 94984 94982; opt 94980 94981 94983 94997 94998 94969.

Data used (all read 13 Nov 2026): tooling/qdb (QuestieDB Forever 1.0.16: quest rows [0]-[3] [7] [9] [11] [12] and source item [11], npc rows [0] [3]-[6] [13], item rows [0] [1] [4] [5] [13]); data/zone_16842.json (Wowhead Forever, browser 2026-11-12: level, req, XP, money, side, itemchoices / itemrewards); data/wowhead_quest_links.json (start / end / series, pulled 2026-11-13 for all but 94969, 2026-11-12); data/browser/r2_pages3_2026-11-13.tsv (ZNPC 16842; QUEST 94980 94981 94982 94983 94984 94997 94998 96771; NPC 258042 258100 258102 258104 258972 259253; ITEM 279851 279929); data/browser/r2_pages_2026-11-12.tsv (NPC 258964 258968 268423 259256); data/drop_rates.json (267234 per-mob rows, 267104 and 267086 single-dropper rows, 2026-11-12); nether.wowhead.com/forever/tooltip from a shell, 13 Nov (item 267138, item 267089, item 279851 "Entity not found", quest 94969); weights/tooltips/2026-11-12.json; `python weights/score_items.py --band 40` (scratch copy of the output); tooling/trainer_costs.json (258098 and 6291, pulled 2026-11-12); docs/forever-shaman-leveling-sheet.html (level 42 row); tooling/client/1.60.1.70938/TaxiNodes.csv + TaxiPath.csv; the [S] / [H] tags of chapters 38-41.

## 1. Header
- File: `43_KroldokStronghold.lua`
- `[N 42-43 Krol'dok Stronghold]` (required dungeon chapter, no `[O]` on the title)
- `[NX 42-43 Stormwind and Aerie Peak]` (chapter 44's title as the plan prints it; copy exactly if 44's spec changes it)
- `[GA Alliance]`; class lines `[A Shaman]`. Footer group "Forever Shaman 30-60".
- Description: `[D Forever Shaman 30-60 (Braedyn)\\Krol'dok Stronghold at 42: the level 42 training in Ironforge, Ranath Nightstride's quest at the Dalaran crater, one run through the Stronghold (Nar'gurk, Zalfan Moonshadow, Overlord Mugg), the Farholde Keep hand-ins, then back to the crater and on to Ironforge.]`
- Level on entry **42.0**, exit **42.2** (plan XP table, required quest XP only; the run's kill XP and the conditional quests are not counted).
- **First line (level check, rule 14)** `[OC]`: "|cffffffffLevel check|r  -  this chapter wants level 42. The highest required level of its pickups is 40 (Eye of Mugg, Krol'dok No More!); Tome of Twilight needs 39, Vengeance of the Highborne 37. The quests are level 41-45 and every Stronghold mob Wowhead lists is elite, but no mob level is in the data (in-game check). Under 42: the Ironforge and crater legs come first anyway; for the run, join a group of 43-45 and keep to its pace. One run, never a re-run"
  - Source of "42": the plan's `wants 42` (route file), itself a low-confidence call (see Unsure). Evidence: ZNPC 16842 (r2_pages3) lists only Twilight Grunt and Twilight Lieutenant, `classification 1` (elite), no level; the NPC pages of the trash (258042, 258100, 258102, 258104, 258972) and bosses (258964, 258968, 268423, 259256) carry "Classification: Elite" and no "Level" fact; qdb npc rows [3]/[4] are null for all of them.

## 2. Entry state
- Where: **Farholde Keep, Riverglades**, where chapter 42 ends (plan, chapter 42 note).
- **Hearth = Farholde Keep.** `[S Farholde Keep]` at 38_RivergladesI.lua:39 (Barracks Master Harlan 257595); `[H Farholde Keep]` at 38:117, 39e:65, 40:50, 41:79; no later `[S]` in 00-41. Chapter 42 is planned to keep it (plan Threads: "Farholde Keep through chapter 44"). Whether the hearth is on cooldown at the start depends on chapter 42's last step (Unsure).
- **Quests carried in from chapter 42** (assumed; reconcile with 42's spec):
  - 94984 Tome of Twilight - giver per Wowhead (quest links, 13 Nov; QUEST page r2_pages3): **Ashe Amberhall 257591 only** (qdb row [1] lists both 257558 and 257591). Wowhead series [94907, 94984]: 94907 A Small Favor is done plain in chapter 40 (40_RivergladesII.lua:13 [QA], :51 [QT]), so no offer gate.
  - 94982 Eye of Mugg - giver per Wowhead: **Demar Brant 257558 only** (qdb row [1] lists both). No series.
  - 94983 Twilight Mementos `[O]` grind / luck - from Sergeant Riftan 258023, **Twilight's Shroud, Riverglades 30.7,49.1** (npc row [6]: one spawn 30.71,49.06; quest row [1]/[2] = 258023; Wowhead start/end n258023).
- **Not carried in:** 96771 (picked up here, leg 3); 94980 (drop-start inside); 94981, 94997, 94998 (offered after their series predecessors, here); 94969 (no giver). The Krol'dok Compound Key is no longer an entry item: Key Ingredients (94981) is in this chapter now, after the Moulding (Wowhead series [94980, 94981]).
- Gear on entry, two-hander: Rage of the Storm (chapter 39c) or Bonebiter (weights doc, 11 Nov section).
- Training here: the level 42 row at Eldrun Stormbreaker (plan Threads: "Ironforge in chapters 43 (42 row)"). Profession gate: Artisan Skinning at Balthus Stoneflayer, optional, "if not bought at 40" (it is an `[O]` line in 39d:21).

## 3. Travel and hearth
Flight graph (TaxiPath build 70938): Farholde Keep (node 3276) links only to Lakeshire (5), Morgan's Vigil (71) and Thelsamar (8) (paths 11584-11589); Thelsamar - Ironforge (6) (paths 15/16); Ironforge - Southshore (14) (paths 26/27). Morgan's Vigil is not known yet (plan Threads), so Farholde - Thelsamar - Ironforge is the way to Ironforge; `[F Ironforge]` from Farholde routes through Thelsamar. Dalaran has no flight point (Southshore, then on foot, as chapters 27/28 and 39c did).

Flight masters (qdb npc row [6]): [TAR257087 Gretchen Mayberry] Farholde Keep `60.9,80.9 Riverglades` (chapter 38's pin; qdb has 14 points, 58.5-62.0 x 79.0-83.2); [TAR1573 Gryth Thurden] Ironforge 55.5,47.7; [TAR2432 Darla Harris] Southshore 49.3,52.3 Hillsbrad Foothills. Innkeeper (bind): [TAR257595 Barracks Master Harlan] Riverglades 64.6,84.1 (one of three qdb points; chapter 38's pin). **No bind change in this chapter.**

Teleports: the hearth and Astral Recall (a level-30 must at 22:69 / 24:20 / 27:45; same bind). Cooldowns on Forever are not in the data (Classic: 60 min hearth, 15 min Astral Recall; unverified).

**Order of legs and why.** 96771 must be in the log before Zalfan Moonshadow dies, and it is picked up and handed in at the same NPC, so the crater is visited twice. Ironforge lies on the only known flight road from Farholde to Southshore, so the level 42 training costs nothing extra on the way out. The hearth carries him from the crater back to Farholde for the run. After the run: Riftan (only with 8 bangles), then the Farholde hand-ins (beside the flight master), then Farholde - Ironforge (auction house, for Key Ingredients only) - Southshore - the crater, and the chapter ends at Ironforge for chapter 44.

- In: Farholde Keep - fly Ironforge - train - fly Southshore - ride to the crater (accept 96771) - hearth (or Astral Recall) to Farholde Keep - to the Stronghold (entrance not in the data).
- Out: Stronghold - [only with 8 bangles: Riftan at the Shroud, then Astral Recall or hearth to Farholde Keep] - Farholde hand-ins - fly Ironforge - fly Southshore - ride to the crater (hand in 96771) - then either (a) with Key Ingredients complete in the bags: hearth / Astral Recall to Farholde, hand in, fly Ironforge, or (b) otherwise: ride to Southshore, fly Ironforge. **Ends at Gryth Thurden, Ironforge, hearth still Farholde Keep.**
- Southshore - crater ride: on foot, path not in the data (unverified). Chapter 39c line 45 warns of elite Crushridge (36-38) west of x38 between y38 and y51 Alterac; at 42 a short reminder is enough.

## 4. Route

### Leg 1 - Farholde Keep to Ironforge
1. `[OC]` "|cffffffffFarholde Keep|r  -  you start where chapter 42 ended; hearth = Farholde Keep and it stays there. Required chapter: one run of Krol'dok Stronghold, |cFFFF0000GROUP 5|r, never a re-run, plus two visits to Ranath Nightstride at the Dalaran crater. Three normal quests, 14,350 XP and 1g 95s; the rest come only if they drop or are offered"
2. `[OC]` "|cffffcc00Carried in:|r Tome of Twilight (94984, Ashe Amberhall) and Eye of Mugg (94982, Demar Brant) from Farholde Keep and, if you took it, Twilight Mementos (94983) from Sergeant Riftan - all from chapter 42"
3. At [TAR257087 Gretchen Mayberry], fly to [F Ironforge] (the game routes it through Thelsamar) `[G60.9,80.9 Riverglades]`. Travel step.

### Leg 2 - Ironforge: level 42 training
4. `[A Shaman]` In the Forlorn Cavern at [TAR258098 Eldrun Stormbreaker] (npc 258098, Ironforge 47.1,13.79, "Shaman Trainer"), `[T]` the level 42 row `[G47.1,13.8 Ironforge]`. trainer_costs.json (2026-11-12, Wowhead raw values; the 5% question stays on the test list):
   - Grace of Air Totem rank 1 (8835) - 1g 60s - sheet: buy ("Grace of Air = your solo air totem")
   - Fire Nova rank 4 (408344) - 1g 89s 47c - sheet: buy
   - Windfury Totem rank 2 (10613) - 1g 60s - sheet: "later"
   - Fire Resistance Totem rank 2 (10537) - 1g 60s - not on the sheet (don't buy)
   - Sheet's buys 3g 49s 47c; with Windfury Totem 2 5g 9s 47c; whole row 6g 69s 47c (plan Threads: 6g 69s 47c).
   - Line text, round-1 format (39d:17): "train every rank your level allows that the sheet marks must or buy (level 42 row: buys Grace of Air Totem 1 - 1g 60s, Fire Nova 4 - 1g 89s 47c; when gold is easy: Windfury Totem 2 - 1g 60s; 3g 49s 47c for the buys)". Optional talent `[OC]`: sheet's talent at 42 is Improved Healing Wave 2/5 (41-42, Resto).
5. `[O]` At [TAR6291 Balthus Stoneflayer] in the Great Forge (npc 6291, Ironforge 39.86,32.5), `[T]` learn Artisan Skinning (spell 10768, 50,000 c = 5g, "level 200" = Skinning 200) once Skinning is 200 and if not learned in chapter 39d `[G39.9,32.5 Ironforge]`. Gate (rule 11).
6. At [TAR1573 Gryth Thurden], fly to [F Southshore] `[G55.5,47.7 Ironforge]`.

### Leg 3 - the Dalaran crater: Ranath Nightstride
7. `[OC]` "|cffffffffThe Dalaran crater|r  -  on foot from Southshore, as in chapters 27 and 28 (Dalaran has no flight point). Ranath Nightstride is a friendly level 45 Highborne"
8. At [TAR268425 Ranath Nightstride], `[QA96771 Vengeance of the Highborne]` (4,850 XP + 65s, requires level 37) `[G17.8,66.0 Alterac Mountains]`. **normal** (plan). qdb: start = end = 268425; npc 268425 L45, rank 1, subname Highborne, one spawn Alterac (36) 17.8,65.95. Objective (row [7] / row [9]): "Travel to Krol'dok Stronghold and slay Zalfan Moonshadow" - kill 268423 x1. Prerequisites: rows [11]/[12] null; Wowhead series []. Nothing names 96771 as a prerequisite. No reward items (zone_16842).
9. `|cFFfff8a3Hearth to [H Farholde Keep]|r` (on cooldown? Astral Recall does the same) `[G17.8,66.0 Alterac Mountains]`.

### Leg 4 - Krol'dok Stronghold, one run
10. `[OC]` "|cffffffffKrol'dok Stronghold|r  -  the way in is not in the data (|cffffcc00unverified|r): ask the group or the Farholde guards". No coordinate on the line.
    - For the writer, do not put on the line: Wowhead puts the Stronghold's NPCs on the **Eastern Kingdoms continent map (uiMap 1415)**, not on a zone map; these are continent coordinates, not Riverglades ones. Trash 55.9-58.2 x 62.0-63.8; Nar'gurk 56.8,62.9; Zalfan Moonshadow 57.1,62.5 / 57.3,62.2; Twilight Commander Zarmok 56.8-57.0,63.4-63.6; Tunk 58.4,62.5; Overlord Mugg 58.4,60.9. West to east this reads Nar'gurk - Zalfan - Tunk - Mugg, with Mugg furthest from the trash; a hint of the room order only (unverified; floors are flattened).
11. `[OC]` "|cffffffffThe Stronghold|r  -  |cFFFF0000GROUP 5|r. Every mob Wowhead lists here is elite: Twilight Grunts, Warlocks, Outriders and Lieutenants, Twilight Commander Zarmok, Nar'gurk the Corruptor, Zalfan Moonshadow, Tunk the Blacksmith and Overlord Mugg. Mob levels and the room order are not in the data. One run, never a re-run. Your quests, with the honest label:"
12. `[OC]` "Eye of Mugg (94982) - Overlord Mugg - |cff66ff66normal|r, one kill: Wowhead reads 41.67% because it counts every kill, quest or not. 4,850 XP + 1g 30s at Demar Brant"
13. `[OC]` "Tome of Twilight (94984) - Nar'gurk - |cff66ff66normal|r, one kill (Wowhead 37.84% over all kills). 4,650 XP at Ashe Amberhall"
14. `[OC]` "Vengeance of the Highborne (96771) - Zalfan Moonshadow - |cff66ff66normal|r, kill quest. 4,850 XP + 65s at Ranath"
15. `[OC]` "Twilight Mementos (94983) - 8 Cultist Bangles from the Twilight's Hammer - |cffffcc00grind/luck|r: about 11% a kill, about 70 kills for 8. Loot what the run gives; abandon it after the run if you do not have 8"
16. `[OC]` "Krol'dok Moulding (94980) - |cffffcc00luck|r: Tunk drops the Moulding (Wowhead 48%), which starts a quest for Alphonse Dumas in Farholde Keep. One kill only"
17. `[OC]` "Krol'dok No More! (94969) - escort Marcus Tilwell to safety - |cffffcc00luck|r: neither the DB nor Wowhead says who gives it or where it ends. Take it if it is offered at the door or inside"
18. `|cFFFF0000GROUP 5|r` Meet the group and enter Krol'dok Stronghold (entrance not in the data, |cffffcc00unverified|r). No pin (39e's dungeon lines have none; see Unsure).
19. Kill [TAR258964 Nar'gurk] for the Tome of Twilight `[QC94984]` (one kill; Wowhead 37.84%). Item 267104: qdb item row [1] = [258964] only; drop_rates.json "Tome of Twilight" single dropper Nar'gurk 37.84% (nether tooltip, 2026-11-12). Elite (NPC page). Subname "The Corruptor" (npc row [13]). Quest row [9]: item 267104, count not in the row; quest text "Kill Nar'gurk ... recover any valuable information" - one item. No pin.
20. Kill [TAR268423 Zalfan Moonshadow] `[QC96771]`. Elite (NPC page). No pin.
21. `[O]` Luck: if [TAR259256 Tunk] drops the Krol'dok Moulding, right-click it, `[QA94980 Krol'dok Moulding]` (3,300 XP + 55s, requires level 38; to Alphonse Dumas in Farholde Keep). Item 267138: qdb item row [1] = [259256] only, row [4] = 94980 (starts it); nether tooltip 13 Nov: "Binds when picked up, Unique, This Item Begins a Quest, Dropped by: Tunk, Drop Chance: 48.44%". Tunk: Elite (NPC page), subname Blacksmith. Rule 12, a named mob's drop at 30-60%: one kill only; being a drop-start, there is nothing to abandon if it does not fall. Wowhead QUEST page: "Not sharable". Label **conditional** (plan).
22. `[O]` Luck: if Krol'dok No More! is offered (qdb has Marcus Tilwell 259253 with no level, spawn or quest link; his Wowhead page, r2_pages3, shows no map and no quests), `[QA94969 Krol'dok No More!]` (3,450 XP, no money, requires level 40) and escort Marcus Tilwell to safety `[QC94969]`. Nether quest tooltip 13 Nov: "Requirements: Escort Marcus Tilwell to safety". Ender unknown: writer adds an `[O]` line "hand it in where the escort ends; if no one takes it, abandon [QS94969]". Label **conditional** (plan). Reward choices 279851 / 279929: ITEM rows "missing" (r2_pages3), nether 279851 "Entity not found": no gear call.
23. Kill [TAR258968 Overlord Mugg] for the Eye of Mugg `[QC94982]` (one kill; Wowhead 41.67%). Item 267086: qdb item row [1] = [258968] only; drop_rates.json single dropper 41.67%. Elite (NPC page). The quest text calls him "their leader"; that he is the last boss is unverified. No pin.
24. `[O]` Loot the Twilight's Hammer for 8 Cultist Bangles `[QC94983]` - |cffffcc00grind/luck|r, never farm. Item 267234 Twilight Bangle (qdb item row [1]: 258042, 258100, 258102, 258104, 258972, 268423; all elite on drop_rates.json and the NPC pages). Per-mob count/outof, drop_rates.json 2026-11-12: [TAR258042 Twilight Grunt] 312/2453 = 12.7%, [TAR258102 Twilight Outrider] 73/588 = 12.4%, [TAR258104 Twilight Lieutenant] 79/707 = 11.2%, [TAR258100 Twilight Warlock] 34/354 = 9.6%, Zalfan Moonshadow 7/34 = 20.6%, Twilight Commander Zarmok 6/333 = 1.8%; overall 11.4%; budget 8 / 0.114 = ~70 kills. Count 8 from row [7] ("Collect 8 Cultist Bangles"); row [9] has the item with no count. One item on the quest, so `[QC94983]` (no `[CI]` needed). Label **grind / luck** (plan; rule 2 / 3: picked up, done once, abandoned if short).
25. `[O]` Fewer than 8 bangles after the run: abandon Twilight Mementos `[QS94983]`. (Then 94997 and 94998 are not offered.)
26. `[OC]` Boss loot: none listed (qdb has no drop rows for the Stronghold's NPCs; `dungeon_loot.py` not run, by the brief).

### Leg 5 - out of the Stronghold: Riftan (only with 8 bangles)
27. `[O]` Only with 8 bangles: ride west to [TAR258023 Sergeant Riftan] at the Twilight's Shroud, `[QT94983]` (4,300 XP, no money) `[G30.7,49.1 Riverglades]`. Chapter 40 rode it "west past Sunnyglade".
28. `[O]` If he offers it: `[QA94997 Lingering Essence]` (3,450 XP + 55s, requires level 38; bring the Satchel of Cursed Mementos to Ashe Amberhall in Farholde Keep) `[G30.7,49.1 Riverglades]`. qdb: start 258023, end 257591, source item 268035 (row [11]); no objective row [9]. Wowhead series [94983, 94997, 94998], "Not sharable". Label **conditional - only if he offers it** (plan: follows 94983, a grind / luck quest).
29. `[O]` From Riftan: `|cFFfff8a3Astral Recall or hearth to [H Farholde Keep]|r` (whichever is ready: the hearth was used at the crater in leg 3) `[G30.7,49.1 Riverglades]`. If neither is ready, ride back east past Sunnyglade (as 40:50 did). Writer: if Guidelime cannot hold an optional hearth cleanly, fold it into step 27's text.

### Leg 6 - Farholde Keep hand-ins
30. `[OC]` "|cffffffffFarholde Keep|r  -  the hand-ins are beside the flight master"
31. At [TAR257591 Ashe Amberhall], `[QT94984]` (4,650 XP, no money) `[G66.8,81.1 Riverglades]`. Ender = 257591 (quest row [2]; Wowhead end n257591); npc row [6] 66.75,81.1. Gear call 1 on this line's `[OC]`.
32. `[O]` Only with Lingering Essence: at [TAR257591 Ashe Amberhall], `[QT94997]` (3,450 XP + 55s) `[G66.8,81.1 Riverglades]`.
33. `[O]` If she offers it: `[QA94998 Curios of Curiosity]` (3,450 XP + 55s, requires level 38; bring the Satchel of Mementos to Melanie Sable) `[G66.8,81.1 Riverglades]`. qdb: start 257591, end 259287, source item 268036. Wowhead series [94983, 94997, 94998], "Not sharable". Label **conditional - only if offered** (plan).
34. `[O]` At [TAR259287 Melanie Sable] (npc 259287, L41, "Expert Enchanter", 66.21,83.36), `[QT94998]` (3,450 XP + 55s) `[G66.2,83.4 Riverglades]`. Gear call 3 on this line's `[OC]`.
35. At [TAR257558 Demar Brant] (subname Knight Commander; "Commander Brant" in the text), `[QT94982]` (4,850 XP + 1g 30s) `[G66.7,81.0 Riverglades]`. Ender = 257558 (quest row [2]; Wowhead end n257558); npc row [6] 66.67,81.01. Gear call 2 on this line's `[OC]`.
36. `[O]` Only with the Moulding: at [TAR259250 Alphonse Dumas] (npc 259250, L25, "Journeyman Blacksmith", 64.46,82.03), `[QT94980]` (3,300 XP + 55s) `[G64.5,82.0 Riverglades]`. No reward items.
37. `[O]` If he offers it: `[QA94981 Key Ingredients]` (3,300 XP + 55s, requires level 38: bring 4 Thick Leather and 12 Iron Bars) `[G64.5,82.0 Riverglades]`. qdb: start = end = 259250, row [7] "Bring 4 Thick Leather and 12 Iron Bars to Alphonse Dumas.", row [9] items 4304 and 3575 (counts from row [7]). Wowhead series [94980, 94981], "Sharable". Reward Krol'dok Compound Key 267089 (zone_16842 itemrewards; nether tooltip: "Binds when picked up, Unique", no use text - what it opens is not in the data). Label **conditional - only if offered** (plan). Sources: Iron Bar 3575 has no drop, vendor or quest source in qdb (rows [1] [4] [5] [13] null) - he has no Mining, so the bars come from the **auction house at the Ironforge stop in leg 7** (|cffffcc00unverified|r: price and supply unknown). Thick Leather 4304: his own Skinning (he is Skinning / Leatherworking) or the same auction house; the only qdb vendor is Lhara (14846, Darkmoon Faire), not on the route.
38. `[O]` Only if you already carry 4 Thick Leather and 12 Iron Bars: `[QT94981]` at once (3,300 XP + 55s) `[G64.5,82.0 Riverglades]`.
39. At [TAR257087 Gretchen Mayberry], fly to [F Ironforge] (through Thelsamar) `[G60.9,80.9 Riverglades]`.

### Leg 7 - Ironforge, back to the crater, then Ironforge
40. `[O]` Only with Key Ingredients in the log and short of items: buy 12 Iron Bars (and Thick Leather if short) at the Ironforge auction house (|cffffcc00unverified|r). Writer: the auctioneers are not in this spec; look up an Ironforge auctioneer id and coordinate in qdb (case-insensitive name search) or write the line as a `[OC]` note without a `[TAR]`/`[G]`. Do not put a gold-farming step in.
41. `[O]` Anything skipped at Eldrun or Balthus in leg 2 can be done now.
42. At [TAR1573 Gryth Thurden], fly to [F Southshore] `[G55.5,47.7 Ironforge]`.
43. Ride to the Dalaran crater. At [TAR268425 Ranath Nightstride], `[QT96771]` (4,850 XP + 65s) `[G17.8,66.0 Alterac Mountains]`.
44. `[O]` Only with Key Ingredients complete: `|cFFfff8a3Hearth (or Astral Recall) to [H Farholde Keep]|r`, then at [TAR259250 Alphonse Dumas] `[QT94981]` (3,300 XP + 55s) `[G64.5,82.0 Riverglades]`, then at [TAR257087 Gretchen Mayberry] fly to [F Ironforge] `[G60.9,80.9 Riverglades]`. If neither teleport is ready, or the items could not be bought: abandon Key Ingredients `[QS94981]` (rule 9) and take step 45.
45. Otherwise: ride back to Southshore; at [TAR2432 Darla Harris], fly to [F Ironforge] `[G49.3,52.3 Hillsbrad Foothills]`. Chapter 44 starts in Ironforge.
46. `[OC]` Check line (section 7).
47. `[NX 42-43 Stormwind and Aerie Peak]`

## 5. Gear calls
Weights: level-40 band (`python weights/score_items.py --band 40`, tooltips `weights/tooltips/2026-11-12.json`: wdps 14, Str 2, Int 1.69, Agi 1.12, Spi 2.5 (cons. 1.5), SP 2.0 (cons. 1.0), Sta 0). Mail counts from 40. Slots, armour and stats below are from the tooltip file, not the names.

**1. Tome of Twilight (94984), choice of two:**
- Twilight Initiate's Belt (279854): Waist, Leather, 70 armor, +11 Agi +7 Spi, sells 43s 43c - **29.8** (22.8 conservative).
- Torn Cultist Cloak (279855): Back, 30 armor, +7 Int, +3 mana per 5 s, sells 51s 89c - 11.8 (7 x 1.69; the scorer has no mp5 term).
- Call: take the **belt only if your belt scores under 29.8**: the Violet Sash from chapter 30 (cloth waist +9 Int, +6 spell damage: 27.2 at band 40 by hand, 9 x 1.69 + 6 x 2) or the Grappler's Belt from chapter 33 (leather waist +7 Str +5 Sta: 14.0). It loses to the Deathmage Sash (39.3, Razorfen Downs loot). Otherwise take the **Torn Cultist Cloak for the vendor** (51s 89c against 43s 43c).
- Line: "|cffffcc00Gear (94984, choice):|r the |cff66ff66Twilight Initiate's Belt|r (leather waist +11 Agi +7 Spi, 29.8 on the weights) over the Violet Sash or Grappler's Belt; not over the Deathmage Sash. Otherwise take the Torn Cultist Cloak (+7 Int, mana regen) for the vendor (51s 89c)"

**2. Eye of Mugg (94982), choice of three:**
- Bigger Rock on Bigger Stick (279480): Two-Hand Mace, 112-168, speed 3.40, 41.18 dps, +14 Str, chance on hit "Bash the target in the face, causing 14 Physical damage every 2 sec for 20 sec" (proc rate not on the tooltip), item level 47, no level requirement, BoP, sells 2g 84s 48c - **604.5**.
- Stick No Rock (279853): Two-Hand Staff, 30.45 dps, +10 Str +18 Spi, +22 health per 5 s, +101 healing / +33 spell damage, sells 2g 78s 15c - 557.3 (506.3 conservative).
- Rock on Stick (279852): one-hand mace - no use to the 2H build.
- Against what he holds: Bonebiter 583.5 (score_items), Rage of the Storm 529.8 linear (weights doc 11 Nov). The first-wave draft ran the weights doc's kill-speed model (weights/enh_weights.py, sheet talents; Rage and Bonebiter rows reproduce the doc's 222.4 / 220.1 / 218.2 / 217.8) with Bigger Rock added: Rockbiter 221.6 (Rage 222.4, Bonebiter 220.1), Windfury 219.8 (Rage 218.2, Bonebiter 217.8); the bleed proc is not modelled. Not re-run here (the plan quotes the result: "ties ... within 1%").
- Call: **take Bigger Rock on Bigger Stick and put it on.** With Windfury (the guide's imbue on the two-hander from 30) it leads Rage by 0.7% and Bonebiter by 0.9%; with Rockbiter it trails Rage by 0.4%; all inside the model's resolution, and its bleed adds damage the model does not count. Runner-up Stick No Rock (557.3) - no. It replaces Rage of the Storm or Bonebiter; the old one sells (Rage 1g 62s 35c, Bonebiter 2g 25s 4c).
- Line: "|cffffcc00Gear (94982, choice):|r take |cff66ff66Bigger Rock on Bigger Stick|r (2H mace 41.18 dps, speed 3.40, +14 Str, a bleed on hit) and put it on: with Windfury it edges Rage of the Storm and Bonebiter (under 1% in the kill-speed model, plus the bleed). Stick No Rock is a caster staff and Rock on Stick one-handed: pass"

**3. Curios of Curiosity (94998, conditional), one choice:**
- Curio-Adorned Necklace (279850): Neck, +9 Int +7 Spi, +5 spell damage and healing, item level 44, BoP, sells 69s 86c - **42.7** (30.7 conservative). Best neck of the round (plan's reward table).
- Against the round-1 necks (score_items band 40): Triune Amulet 33.5 (39c loot), Glowing Eye of Mordresh 27.5 (39b loot), Amberglow Talisman 26.1 (39d), Giantstone Medallion 25.0 (+10 Spi), Thermaplugg Medal of Honor 25.0 (+10 AP +6 Spi; Sta counts 0).
- Call: **take it and wear it**; it beats every neck round 1 offered. Line: "|cffffcc00Gear (94998):|r |cff66ff66Curio-Adorned Necklace|r (neck +9 Int +7 Spi +5 spell damage, 42.7 on the weights) - wear it: it beats the Triune Amulet (33.5) and every other neck so far"

**4. No item rewards:** 96771, 94980, 94983, 94997 (zone_16842 itemchoices / itemrewards empty). 94981 gives the Krol'dok Compound Key (no stats).
**5. Krol'dok No More! (94969):** choices 279851 and 279929 - "missing" on Wowhead (r2_pages3) and "Entity not found" on nether (13 Nov). No call possible.

## 6. Out
Nothing of category 16842 that is open to the Alliance is out: `_decisions.tsv` has nine 16842 rows (96771 DUN-normal; 94984, 94982 DUN-boss; 94983 DUN-grind; 94980, 94981, 94997, 94998, 94969 COND), all in this chapter. The Horde twins on zone_16842 (94968 Eye of Mugg, 94972 Tome of Twilight, 94973 Krol'dok Moulding, 94974 Key Ingredients, 94975 A Token of Vengeance, 95056 Krol'dok No More!; side 2) are not in the pool. Silent in the guide (rule 4).

## 7. End check
`[OC]` "|cffffcc00Check:|r handed in here: Vengeance of the Highborne (96771), Tome of Twilight (94984), Eye of Mugg (94982); Twilight Mementos (94983) handed in at Riftan or abandoned; Lingering Essence (94997), Curios of Curiosity (94998), Krol'dok Moulding (94980), Key Ingredients (94981) and Krol'dok No More! (94969) only if they came up, each handed in or abandoned. Nothing from this chapter stays in the log. Hearth = Farholde Keep"
- **Carried out: none.** Ends at Gryth Thurden, Ironforge; hearth Farholde Keep (no `[S]` in this chapter).
- Rule 9: 94983 has `[QS]`; 94997 / 94998 are accepted only with their hand-ins in this chapter; 94980 is a drop-start handed in the same chapter; 94981 has a `[QS]` fallback (step 44); 94969 has a `[QS]` fallback.

## 8. Totals
- Required: 3 quests, **14,350 XP**, **1g 95s** (96771 4,850 + 65s; 94984 4,650 + 0; 94982 4,850 + 1g 30s; zone_16842.json). Equals the plan's XP table row (3, 14,350, 1g 95s).
- Optional / conditional: 94980 3,300 + 55s; 94981 3,300 + 55s; 94983 4,300 + 0; 94997 3,450 + 55s; 94998 3,450 + 55s; 94969 3,450 + 0 = **21,250 XP**, 2g 20s. Equals the plan's 21,250.
- Spent here: training 3g 49s 47c (sheet's buys; 6g 69s 47c the whole row); Artisan Skinning 5g if taken; Iron Bars on the AH if Key Ingredients is taken (price unknown).
- Highest required level among pickups: 40 (94982, 94969); plan column says 40.

## 9. Unverified / in-game test list, Needs pull, Unsure
**Unverified / in-game test list**
- Where the Stronghold's door is and how to reach it from Farholde Keep (plan test list).
- Mob levels inside; room order of Nar'gurk, Zalfan, Tunk and Mugg; whether Mugg is last.
- Whether Krol'dok No More! is offered at the door or inside, by whom, and where it ends (plan test list).
- Whether Tunk's Krol'dok Moulding drops for everyone (plan test list).
- Whether Alphonse Dumas offers Key Ingredients after the Moulding, and whether Iron Bars are on the Ironforge auction house at a sane price; what the Krol'dok Compound Key opens.
- Whether Riftan offers Lingering Essence after Twilight Mementos, and Ashe Curios of Curiosity after it.
- Zalfan Moonshadow shows 34 sampled kills on the Twilight Bangle page against 333-2,453 for the other droppers: check that he is on the run's path (96771 is required).
- Bigger Rock on Bigger Stick's bleed proc rate.
- Trainer price: Wowhead raw or 5% less (Fire Nova 4: 1g 89s 47c or about 1g 80s) - on the plan's test list.
- Hearth and Astral Recall cooldowns on Forever; the Southshore - crater path.
- "8 Cultist Bangles" = the item the DB calls Twilight Bangle (one item on the quest, so very likely).

**Needs pull (only a Wowhead page settles it)**
- Settled by the third pull (r2_pages3, 13 Nov) against the draft's list: the zone NPC list (ZNPC 16842: Grunt and Lieutenant only, elite, no levels); the trash NPC pages 258042, 258100, 258102, 258104, 258972 (elite, continent map, **no level**); Marcus Tilwell 259253 (page exists: Humanoid, no map, no quests); items 279851 / 279929 (missing on Wowhead). The givers of 94984 (Ashe only) and 94982 (Demar only) and the series of 94980 / 94981 / 94983 / 94997 / 94998 / 94984 are now settled from the QUEST rows.
- Still open: mob levels (no Wowhead page carries them; in-game only); the Stronghold map with the entrance in Riverglades coordinates (no UiMap transform in tooling/client); quest page 94969 with a giver / ender (the 12 Nov links row has start [] end []); the reward items 279851 / 279929 (not on Wowhead at all, so in-game only); an Ironforge auctioneer id if the writer wants a `[TAR]` on step 40 (qdb lookup, not a pull).

**Unsure**
- **Level check 42.** The plan says 42 from the draft's low-confidence call; nothing new in the data raises or lowers it (no levels anywhere). Kept at 42 with "join a group of 43-45".
- **Hearth at the start.** If chapter 42 ends with a hearth, the leg-3 hearth may be on cooldown; Astral Recall is the fallback (step 9). Then the Riftan return (step 29) and the Key Ingredients return (step 44) each need the other teleport. The writer should copy chapter 42's last line when it exists.
- **Key Ingredients routing.** I placed the hand-in after the crater (hearth to Farholde, then fly Ironforge), which costs a Farholde - Thelsamar - Ironforge flight instead of the Southshore - Ironforge one, but needs no speculative bar purchase on the first Ironforge pass. The alternative (buy 12 bars in leg 2 on the 48% chance, hand in at once at step 38) is written as step 38 for anyone who already has them. Main session's choice.
- **Chapter 44's level 42 row.** The plan's chapter 44 note says "Farseer Maret Firetend's level 42 row fall here", but Threads put the 42 row in chapter 43 (Ironforge) and Aerie Peak's in 44 and 48. This spec trains the 42 row at Eldrun; chapter 44 should not train it again.
- **The entrance line's `[G]`.** No coordinate is known; 39e's dungeon lines have no pin. If check_guide flags it, the main session decides.
- **Gold-check line** at the Ironforge stops: not written (the plan wants one from `tooling/gold.py` once the chapters exist; chapter 42's money is not in a file yet).

## 10. Deviations from the route plan
1. **Givers per Wowhead differ from qdb:** Tome of Twilight is given by Ashe Amberhall only, Eye of Mugg by Demar Brant only (wowhead_quest_links.json 13 Nov; qdb row [1] lists both NPCs for each). Affects chapter 42's pickup lines, not this chapter's list.
2. **Twilight Mementos and Lingering Essence start at the Twilight's Shroud (Riftan 30.7,49.1), not Farholde Keep**: the hand-in of 94983 and the pickup of 94997 are an optional ride west plus a teleport (steps 27-29). Not a list change.
3. **96771 is handed in within the chapter** (second crater visit, leg 7); the chapter ends at Ironforge for chapter 44, as the plan's chapter note says.
4. **Key Ingredients' hand-in path** (step 44) adds an optional hearth / flight after the crater; conditional, not counted.
5. **Artisan Skinning** added as an optional gate at the Ironforge stop (plan Threads: "if not bought at 40"; trainer_costs.json 6291 spell 10768, 50,000 c).
6. Quest list, labels and totals unchanged (3 / 14,350 / 1g 95s; optional 21,250).
