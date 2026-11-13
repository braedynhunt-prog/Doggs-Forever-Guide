# Spec 42 - Riverglades: pickups and loose ends (13 Nov 2026, third wave)

Started from `Claude outputs/40-50-specs-2026-11-13/42-draft.md`, re-cut to the revised plan (`docs/40-50-plan-2026-11-12.md`, section "### 42", XP table row 42: 0 required, 10,500 optional/conditional). Every fact below re-checked 13 Nov against: `tooling/qdb` (QuestieDB Forever 1.0.16) via `python tooling/qinfo.py` and `python tooling/loc.py`; `data/zone_16591.json` and `data/zone_16842.json` (XP, money, side); `data/wowhead_quest_links.json` (start, end, series; Krol'dok rows pulled 13 Nov); `data/browser/r2_pages3_2026-11-13.tsv` (QUEST rows 94980 94981 94982 94983 94984 94997 94998 96771); `Claude outputs/40-50-plan-2026-11-12/pool/_decisions.tsv`; `docs/40-50-route-2026-11-12.txt` + `python tooling/route_xp.py` (row 42: 0 / 0 / 00s / 10,500); nether.wowhead.com/forever tooltips fetched 13 Nov for quests 94891, 94963, 95296, 95975 and item 275042; guide chapters 38, 40, 41.

**Prerequisites:** quest rows [11]/[12] are empty for every quest named here (Forever-only, thin DB). All chain order comes from Wowhead's series (an offer gate, not proof) or from source items.

## 1. Header
- File: `42_RivergladesIII.lua`, footer group "Forever Shaman 30-60".
- `[N 42-43 Riverglades]`; next `[NX 42-43 Krol'dok Stronghold]` (plan chapter 43 title).
- `[GA Alliance]`; any gear line `[A Shaman]`.
- `[D ...]` (suggested): "Back through the Riverglades at 42: the Krol'dok Stronghold quests from Demar Brant, Ashe Amberhall and Sergeant Riftan, Friz Frazzlespark's errands for Booty Bay and Feathermoon, and whatever Gray Dawnbright, Fuzzle and Riftan still offer. Hearth stays Farholde Keep."
- Level on entry **42.0**, exit **42.0** on required XP (plan XP table; 0 required). If all three conditional quests are offered: +10,500 XP.
- **Level-check line (first `[OC]`):** "This chapter wants level 42 (the plan's call; the highest required level among its pickups is 40: From Port to Port 95219 and Eye of Mugg 94982). The only fights are Fuzzle's escort through Sunnyglade (cultists 37-40) and the edge of the Twilight's Shroud at Sergeant Riftan (cultists 42-44). Under 42: nothing here needs a kill - skip Fuzzle's escort if offered and walk to Riftan from the east without entering the Shroud."
  - Data (loc.py): Twilight Neophyte 256798 L37-38 (centre 48.3,48.8), Twilight Shadowmancer 254560 L39-40 (47.8,48.3), Twilight Raider 256952 L39-40 (49.0,49.7); Twilight Fanatic 256795 L42-43, Twilight Corrupter 256797 L42-43, Twilight Champion 256799 L43-44 (Shroud, x25-42 y32-55).
- Legs run lowest mob level first: Keep (none) -> Powderfuse Port (none) -> Sunnyglade (37-40) -> Riftan (42-44 nearby) -> back to the Keep.

## 2. Entry state
- Stands in **Farholde Keep**: chapter 41 ends `Hearth to [H Farholde Keep]` (41_PowderfusePort.lua:79). Hearth bound `[S Farholde Keep]` at 38:39; every later `[H]` goes there (39e:65, 40:50, 41:79). **Hearth on cooldown at the start.**
- Quests carried in (all conditional, none required):
  - 94892 Dying Wish was handed in at Demar Brant in chapter 40 only if the 1.6% Field Marshal's Log dropped in 38 (40:44, 40:52); 40:52 told him to leave Delivering Closure (94893) for round 2. So 94893 is normally NOT in the log yet: it is picked up here (Leg A) if Demar offers it.
  - 94907 A Small Favor was handed in at 40:51 (plain step) - the series predecessor of Tome of Twilight (series [94907, 94984]).
  - Chapter 41's optional Friz block (94928 > 95288 > 95293 > 95294; 41:56-58, 41:77) decides whether Friz offers 95296.
- Professions / training: none falls here (plan Threads: the level-42 shaman row is chapter 43's Ironforge stop; Artisan Leatherworking is chapter 44).

## 3. Travel and hearth
- In: already at Farholde Keep.
- Flight master [TAR257087 Gretchen Mayberry] (L55 elite flag in qdb), loc.py centre 61.1,80.8 (14 points x58-63 y78-83); round 1 wrote 60.9,80.9 (38:38) - keep that. Innkeeper [TAR257595 Barracks Master Harlan] centre 64.2,82.9. **No rebind**: hearth stays Farholde Keep (plan Threads: Farholde through chapter 44).
- Roads (not in the data, unverified): Keep -> Powderfuse Port "past the north side of Farholde Keep and up the coast road north-east" (41:17 wording). Port -> Sunnyglade: west across the plains. Sunnyglade -> Fuzzle's Treasure (41.6,47.7) -> Riftan (30.7,49.1) west. Riftan -> Keep: ride east past Sunnyglade and Wheeler's Grange (40:50 wording).
- **Hearth decision: no hearth in this chapter.** The hearth is on cooldown at the start (41:79) and chapter 43 needs it (plan: 43 flies to Ironforge, then Southshore and the Dalaran crater, and "hearths back for the run"). The chapter rides back from Riftan instead, so the hearth is off cooldown and unused when chapter 43 needs it. Last step: ride back to the Keep.
- Out: chapter ends in Farholde Keep beside Gretchen Mayberry; chapter 43 opens with the flight to Ironforge (known: `[P Farholde Keep]` 38:38, `[P Thelsamar]` 02:43).

## 4. Route (play order)
Coordinates: qdb (loc.py / qinfo.py) unless marked.

### Leg A - Farholde Keep: the Stronghold quests (all within 1 unit of 66.7,81.0)
1. `[OC]` level check (section 1).
2. `[OC]` carried-in note: "Hearth on cooldown; it stays unused this chapter (you ride back from Riftan) so it is ready for chapter 43. Nothing required is carried in."
3. At [TAR257591 Ashe Amberhall], **66.8,81.1 Riverglades** (round 1 wrote 66.7,81.1): `[QA94984 Tome of Twilight]` - 4,650 XP, 0 money, req 39, L44; "Kill Nar'gurk within Krol'dok Stronghold and recover any valuable information" (Tome of Twilight 267104 from Nar'gurk 258964, instance, no spawn in qdb). Ender Ashe Amberhall. Label in chapter 43: **normal (boss item, one kill; Wowhead reads 37.84% over all kills)**. Series [94907, 94984]: 94907 done in 40. Giver: Wowhead start = Ashe only (r2_pages3); qdb row [1] lists Demar Brant and Ashe. Counted in chapter 43.
4. At [TAR257558 Demar Brant] <Knight Commander>, **66.7,81.0 Riverglades**: `[QA94982 Eye of Mugg]` - 4,850 XP + 1g 30s, req 40, L45; "Infiltrate Krol'dok Stronghold and return to Commander Brant with proof of their leader's demise" (Eye of Mugg 267086 from Overlord Mugg 258968, instance). Ender Demar Brant. Label in chapter 43: **normal (boss item, one kill; Wowhead 41.67%)**. Wowhead start = Demar only, series empty; qdb lists Demar and Ashe. Counted in chapter 43.
5. Same NPC, `[O]` line: `[QA94893 Delivering Closure]` - 4,200 XP + 70s, req 36, L47; source item Marshal Ryan's Crest 266428; "Deliver Marshal Ryan's Crest to Abigail Lawson in the Cathedral Square of Stormwind City" -> [TAR278088 Abigail Lawson], **Stormwind City 50.2,51.8**, hand-in **chapter 44**. Line text: "Only if you handed in Dying Wish in chapter 40". Series [94885, 94887, 94892, 94893]. Label: conditional (plan, counted in 44's optional list).
6. (No Alphonse Dumas step.) Key Ingredients 94981 is NOT offered yet: series [94980, 94981] (r2_pages3, 13 Nov) puts it after Krol'dok Moulding 94980, which starts from Tunk's dungeon drop (chapter 43). Silent here.

### Leg B - Powderfuse Port: Friz Frazzlespark and Gray Dawnbright
7. `[OC]` "To the port - ride past the north side of Farholde Keep and up the coast road north-east (road unverified)".
8. At [TAR255897 Friz Frazzlespark] <Specialty Goods>, **77.1,52.9 Riverglades** (qdb, 1 point; round 1 wrote 77.2,52.9 - keep 77.2,52.9 for consistency, within 0.1):
   - `[QA95295 I Know a Guy]` - 315 XP, 0 money, req 36, L40, side Both; "Speak to Friz's contact in Booty Bay" -> [TAR3945 Caravaneer Ruzzgot], **Stranglethorn Vale 27.4,74.1**, hand-in **chapter 45**. Series [95295, 95322, 95325] (first). **Plain pickup** (plan; counted in 45).
   - `[QA95219 From Port to Port]` - 330 XP, 0 money, **req 40**, L41, side Alliance; source item Cask of Powderfuse Port 276068 (qdb item row: no source, given by the quest); "Deliver the Cask of Powderfuse Port to Mardrack Greenwell at Feathermoon Stronghold in Feralas" -> [TAR7941 Mardrack Greenwell], **Feralas 31.0,43.1**, hand-in **chapter 47**. No series. **Plain pickup** (plan; counted in 47).
9. Same NPC, `[O]` line: `[QA95296 Shipping and Handling]` - 315 XP, 0 money; qdb req none, Wowhead req 36, L40, side Both; "Speak with Wharfmaster Steamfizzle at Steamwheedle Port in Tanaris" -> [TAR260405 Wharfmaster Steamfizzle], **Tanaris 67.6,23.1**, hand-in **chapter 46**. Tooltip (13 Nov): "Requirements: Money: 10s" (paid at the hand-in, unverified). Series [95294, 95296, 95383, 95312, 95321, 95472]: follows 95294 Smuggler's Bargain (chapter 41, optional). Line text: "Only if you did Friz's smuggling quests in chapter 41 and he offers it". Label: conditional (counted in 46's optional list).
10. At [TAR263120 Gray Dawnbright], **78.8,54.2 Riverglades**, `[O]` line: `[QA95975 Her World]` - **3,300 XP**, 0 money, req 36, L41, side Alliance; "Gather 20 Wildflowers and deliver them to Tessa Dawnbright in Farholde Keep" (tooltip: Wildflower x 20). Item Wildflower 271823: qdb item row [2] = object 648994 (no row in object.json, no spawn); drop_rates.json: 683/683 = 100% from object 648994. Ender [TAR263089 Tessa Dawnbright] 63.9,82.2 Riverglades (Leg E). Series [95988, 95957, 95975]: follows 95957 Drink Up!, out. Line text: "Only if Gray offers it (it follows quests the guide skips)". Label: **conditional, counted here**.
11. `[O]` Gather 20 Wildflowers `[CI271823,20]` or `[QC95975]` - **position Needs pull** (object 648994's map). The writer must not invent a `[G]`; see Unsure 1.

### Leg C - Sunnyglade: Fuzzle
12. `[OC]` "West to Sunnyglade (~30 units). Cultists here are 37-40. |cFFFF0000Danger:|r Ghostmaw, a level-42 elite crocolisk, patrols the water (qdb: 475 points, x40-66 y32-79, centre 52.6,56.0)". (Note: 40:35 gives 47-54,42-57; the 1.0.16 DB range is wider. npc 263380 L42 rank 1.)
13. At [TAR259158 Fuzzle], **47.3,51.4 Riverglades**, `[O]` line: `[QA94963 Biting the Hand]` - **3,150 XP + 50s**, req 36, L40, side Both; text "<Fuzzle snarls.>"; tooltip "Help Fuzzle escape Sunnyglade". Ender: object [Fuzzle's Treasure] 625582, **41.6,47.7 Riverglades** (no `[TAR]` on an object step, as 41:18). Series [94961, 94963]: 94961 is out (Twilight Finger Bone 16.2%, rule 12). Line text: "Only if Fuzzle offers the escort (it follows a quest the guide skips)". Label: **conditional, counted here**.
14. `[O]` Escort Fuzzle out of Sunnyglade to his treasure `[QC94963]` `[G41.6,47.7 Riverglades]` (escort path not in the data; cultists 37-40 on the way).
15. `[O]` At the Fuzzle's Treasure, `[QT94963]` (3,150 XP + 50s) `[G41.6,47.7 Riverglades]`.

### Leg D - The Twilight's Shroud: Sergeant Riftan
16. `[OC]` "West to Sergeant Riftan at the east edge of the Twilight's Shroud. |cFFFF0000Danger:|r Overlord Kilgar, a level-46 elite, walks the Shroud north-west of Riftan (qdb 17 points x26-31 y40-47, centre 27.4,43.5): approach from the east and do not go north. Cultists in the Shroud are 42-44."
17. At [TAR258023 Sergeant Riftan], **30.7,49.1 Riverglades** (qdb 1 point; round 1 wrote 30.4,49.0 - within 0.3, either is fine; brief: Riftan stands here, not at the Keep):
   - `[QA94983 Twilight Mementos]` - 4,300 XP, 0 money, req 38, L42; "Collect 8 Cultist Bangles from the Twilight's Hammer in Krol'dok Stronghold" (Twilight Bangle 267234; qdb droppers 258042 Twilight Grunt, 258100 Twilight Warlock, 258102 Twilight Outrider, 258104 Twilight Lieutenant, instance; 11.4% over 6 mob types, _decisions.tsv). Ender Riftan. Label: **grind / luck (chapter 43)** - picked up on the way because it costs nothing (rule 2); in chapter 43 abandoned with `[QS94983]` if 8 bangles do not drop on the one run. Line note: "grind / luck: Krol'dok Stronghold, chapter 43 - one run, no re-run". Counted nowhere (plan answer 9).
   - Lingering Essence 94997 and Curios of Curiosity 94998 are NOT offered here: series [94983, 94997, 94998] (r2_pages3, 13 Nov) puts them after Twilight Mementos. Silent; chapter 43 handles them.
18. Same NPC, `[O]` line: `[QA94891 News to Farholde]` - **4,050 XP**, 0 money, req 38, L46, side Alliance; source item Kilgar's Head 265837 (qdb item row [1] = Overlord Kilgar 256881 only; the quest hands it over); tooltip "Return to Ashe Amberhall in Farholde Keep". Ender [TAR257591 Ashe Amberhall] (Leg E). Fixed reward Farholde Keep Tabard 275042. Series [94890, 94891]: 94890 Bring Me His Head is out (Overlord Kilgar, 46 elite, rule 13). Line text: "Only if Riftan offers it without Bring Me His Head (unverified)". Label: **conditional, counted here**. Do NOT take 94890 (silent).
19. `[OC]` "Back to Farholde Keep - ride east past Sunnyglade and Wheeler's Grange (road unverified). Keep your hearth for chapter 43."
20. Travel step to the Keep: `Ride back to Farholde Keep [G66.7,81.0 Riverglades]` (goto-only travel step; allowed by the 4 Nov lesson).

### Leg E - Farholde Keep: conditional hand-ins
21. `[O]` At [TAR257591 Ashe Amberhall], **66.8,81.1**: `[QT94891]` (4,050 XP) - only if you carry it.
22. `[O]` At [TAR257558 Demar Brant], **66.7,81.0**: `[QA94894 The Twilight Threat]` - 4,850 XP, 0 money, req 38, L45, side Alliance; source item Kilgar's Head 265837; "Deliver Kilgar's Head to Bolvar Fordragon within Stormwind Keep in Stormwind City" -> [TAR1748 Highlord Bolvar Fordragon], **Stormwind City 80.2,38.4**, hand-in **chapter 44**. Wowhead start Demar Brant; series empty (quest-links row; 94894 is not in r2_pages3). Line text: "Only if Demar offers it (it delivers Kilgar's Head; most likely only after News to Farholde)". Placed after step 21 so a News to Farholde hand-in comes first. Label: conditional (counted in 44's optional list).
23. `[O]` At [TAR263089 Tessa Dawnbright], **63.9,82.2** (round 1 wrote 63.8,82.2): `[QT95975]` (3,300 XP) - only if you carry it with 20 Wildflowers.
24. Last step: `[OC]` Check (section 7), no `[G]`. He stands in Farholde Keep near Gretchen Mayberry, hearth off cooldown or nearly so.

### Not taken (silent, rule 4)
94829, 94858, 94961, 94890, 95957, 95988 and the rest of section 6. Not in this chapter at all: 94980/94981/94997/94998/94969/96771 (chapter 43).

## 5. Gear calls
- No reward choice is handed in in this chapter.
- 94891 News to Farholde (if offered) -> Farholde Keep Tabard 275042 (fixed; tabard, ilvl 20, BoP, no stats, sells 1g 25s; nether tooltip 13 Nov - not in weights/tooltips/2026-11-12.json): cosmetic, keep or vendor. Line: "`[OC][A Shaman]` Gear (94891): the Farholde Keep Tabard has no stats - wear it or vendor it (1g 25s)".
- 94963 gives 50s only; 95975 no reward in qdb.
- The rewards of 94984 (Twilight Initiate's Belt / Torn Cultist Cloak) and 94982 (Rock on Stick / Stick No Rock / Bigger Rock on Bigger Stick) are chapter 43's gear calls (hand-ins there).

## 6. Out (Riverglades quests not in this chapter; silent; reasons from _decisions.tsv)
- 94829 What We Lost - Farmers' Mementos 7.26% from Twilight Raiders only, five needed, ~69 kills (rule 12)
- 94858 All That's Left - series after 94829, which is out
- 94961 Biting the Hand - Twilight Finger Bone 16.2% (rule 12)
- 94890 Bring Me His Head - Overlord Kilgar, 46 elite (rule 13)
- 94679 Snargl's Snout - Snargl 40 elite (rule 13)
- 95562 Cut Off the Heads - Chogg'Zac 41 elite (rule 13)
- 95986 King of the Wild Plains - Ombassa 41 elite (rule 13)
- 95120 WANTED: Old Rot-Chum - 42 elite (rule 13)
- 95912 WANTED: Blademaster Kaijo - 42 elite (rule 13)
- 94926 Drop the Hammer - Komuk 45 elite (rule 13); no giver in the DB
- 95935 Hail the Dragonslayer - Braedyn's 11 Nov ruling
- 95261 It Takes Guts - Beast Entrails 13.2% (rule 12)
- 95326 The Big Payback - Ruzzgot's Shipment 29.29% (rule 12)
- 95984 Song of the Strider - Intact Tallstrider Beak 15.56% (rule 12)
- 95957 Drink Up! / 95988 Goes Down Smooth - quest level 38, below the round-2 pool (39-55), not in _decisions.tsv and in no chapter 00-41; round 1 left 95988 out (Crawler Spittle 12.21%, 38.md per the draft)

## 7. End check
`[OC]` Check text (adjust to what was offered):
- Handed in here, if offered: Biting the Hand (94963), News to Farholde (94891), Her World (95975). Nothing required.
- **Carried out** (into later chapters):
  - 94984 Tome of Twilight (Ashe Amberhall 66.8,81.1) and 94982 Eye of Mugg (Demar Brant 66.7,81.0) -> **chapter 43**, Krol'dok Stronghold; hand-ins back at the Keep.
  - 94983 Twilight Mementos (Sergeant Riftan 30.7,49.1, grind / luck) -> **chapter 43**; hand-in at Riftan; if handed in, Riftan offers 94997 then Ashe offers 94998 (chapter 43).
  - 95295 I Know a Guy -> Caravaneer Ruzzgot, Booty Bay 27.4,74.1, **chapter 45**.
  - 95219 From Port to Port (Cask of Powderfuse Port 276068) -> Mardrack Greenwell, Feathermoon 31.0,43.1, **chapter 47**.
  - If offered: 95296 Shipping and Handling (10s at the hand-in) -> Wharfmaster Steamfizzle, Tanaris 67.6,23.1, **chapter 46**.
  - If offered: 94893 Delivering Closure -> Abigail Lawson, Stormwind 50.2,51.8, **chapter 44**.
  - If offered: 94894 The Twilight Threat -> Bolvar Fordragon, Stormwind 80.2,38.4, **chapter 44**.
- Hearth bound Farholde Keep, **not used in this chapter** (used at 41:79). Next: fly Farholde Keep -> Ironforge (chapter 43).
- Log: 5 sure quests, at most 8.

## 8. Totals
| | quests | XP | money |
|---|---|---|---|
| Plan XP table row 42 | 0 required | 0 required / 10,500 optional | 00s |
| This spec, required | 0 | 0 | 00s |
| This spec, conditional counted here | 3: 94963 3,150; 95975 3,300; 94891 4,050 | **10,500** | 50s (94963) |
Matches the plan. Money: the plan's "money" column covers required quests only (00s); the 50s is conditional.
Pickups counted in other chapters (no XP here): 94984 4,650 and 94982 4,850 (+1g 30s) in 43 required; 94983 4,300 in 43 grind/luck; 95295 315 in 45; 95219 330 in 47; conditional 95296 315 (46), 94893 4,200 (+70s) and 94894 4,850 (44). None is six or more levels below 42, so nothing is scaled.

## 9. Unverified / in-game test list, Needs pull, Unsure
**In-game test list:**
- Fuzzle offers Biting the Hand (94963) without 94961; the escort path.
- Gray Dawnbright offers Her World (95975) without 95988 / 95957; where the Wildflowers grow.
- Riftan offers News to Farholde (94891) without Bring Me His Head (already on the plan's list); Demar then offers The Twilight Threat (94894).
- Demar offers Delivering Closure (94893) only after Dying Wish (94892).
- Friz offers I Know a Guy (95295) and From Port to Port (95219) without the chapter-41 smuggling block; Shipping and Handling (95296) only with it; whether its 10s is taken at the hand-in.
- Ashe gives Tome of Twilight and Demar gives Eye of Mugg (Wowhead), or both give both (qdb row [1]).
- Roads: Keep -> port, port -> Sunnyglade, Riftan -> Keep.

**Needs pull:**
- Object 648994 Wildflower: its map (decides the `[G]` and the leg of step 11).
- 94894 The Twilight Threat: the prompt said r2_pages3 holds its series box; it does not (r2_pages3 has no QUEST 94894 row; the quest-links row from 11 Nov shows series []). Its quest page would settle whether it follows 94891 / 94890.

**Settled by r2_pages3 (13 Nov):** Lingering Essence and Curios of Curiosity follow Twilight Mementos (series [94983, 94997, 94998]); Key Ingredients follows Krol'dok Moulding (series [94980, 94981]); Tome of Twilight follows A Small Favor (series [94907, 94984], done in 40); Eye of Mugg has no series. The draft's plain 94997/94998/94981 lines are therefore gone from this chapter.

**Unsure:**
1. Her World's gather step has no position. Options: (a) keep the `[O]` pickup and the hand-in, and write the gather step with Gray's `[G78.8,54.2]` plus "Wildflowers: position not in the data, look around Gray and the port road" (unverified); (b) drop the gather line until the object map is pulled. Main session decides.
2. 95059 Frazzlespark's Crate (280 XP, L36, req 36, Alliance; Friz -> Demar Brant; zone_16591) is not in the round-2 pool and is not added. Main session decides.
3. Hearth: this spec rides back from Riftan instead of hearthing so the hearth is free for chapter 43's return from the Dalaran crater. If chapter 43's spec assumes a hearth used at the end of 42, reconcile.
4. Leg D (Riftan) carries no counted XP: only Twilight Mementos (grind / luck, uncounted) and the conditional News to Farholde. The plan names Riftan in the loop, so it stays; it costs the ride west and back (~45 units).

## 10. Deviations from the route plan
- None in the quest list: 0 required, conditional 94963 / 95975 / 94891 = 10,500 XP as in the plan.
- Giver detail: the plan says "Demar Brant and Ashe Amberhall at the Keep for Eye of Mugg and Tome of Twilight"; Wowhead (r2_pages3) has Ashe start Tome of Twilight and Demar start Eye of Mugg; qdb lists both NPCs for both. Written per Wowhead.
- Dungeon pickups made here for chapter 43: 94984 (Ashe), 94982 (Demar), 94983 (Riftan). 94980 / 94981 / 94997 / 94998 / 94969 / 96771 cannot be picked up here (drop start, series, no giver, Alterac).
- No hearth used (section 3), consistent with the plan's "Farholde through chapter 44".
