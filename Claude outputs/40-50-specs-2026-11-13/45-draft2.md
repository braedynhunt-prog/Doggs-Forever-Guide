# Spec: chapter 45 "Booty Bay" (round 2, re-cut 13 Nov 2026)

Data used (all read 13 Nov 2026): QuestieDB Forever 1.0.16 (`tooling/qdb/{quest,npc,object,item}.json`, 12 Nov); Wowhead XP and rewards `data/zone_33.json`, `data/zone_16591.json` (12 Nov); `data/wowhead_quest_links.json` (pulled 11-13 Nov); `data/browser/r2_pages_2026-11-12.tsv`, `r2_pages2_2026-11-12.tsv`, `r2_pages3_2026-11-13.tsv`; `data/drop_rates.json`; client tables build 70938 (`TaxiNodes.csv`, `TaxiPath.csv`, `SkillRaceClassInfo.csv`); tooltips `weights/tooltips/2026-11-12.json`; quest tooltips 95322, 95325, 95327 read 13 Nov from nether.wowhead.com/forever. Pool: `Claude outputs/40-50-plan-2026-11-12/pool/33_Stranglethorn.txt`, `16591_Riverglades.txt`, `3_Badlands.txt`; verdicts `pool/_decisions.tsv`. Every id below was looked up in those files. The first-wave draft `45-draft.md` was re-checked line by line; its Stormwind, Darkshire, Nethergarde and Pool of Tears legs belong to chapter 44 and are not here.

## 1. Header
- File: `45_BootyBay.lua`
- Title: `[N 42-43 Stranglethorn Vale]`. Next: `[NX 42-44 Tanaris]` (chapter 46 as the plan titles it).
- `[GA Alliance]`
- Description: `[D Forever Shaman 30-60 (Braedyn)\\Booty Bay for Friz's caravan errands with Caravaneer Ruzzgot (the Bloodsail Trunk outside town, then the Venture Co. ledger at Lake Nezferiti) and Nesingwary's third raptor hunt, the Jungle Stalkers. Ends on the boat to Ratchet.]`
- Level: plan predicts 42.4 in, 42.5 out (`route_xp.py`: 7,465 required XP).
- Level-check line (rule 14): "This chapter wants level 41": set by the mobs, the Jungle Stalkers (687, level 40-41). Highest required level among the pickups is 36 (95295 quest row [3] = 36; 95322 / 95325 have no row [3], Wowhead reads 36 for both; 196 row [3] = 28). The Venture Co. Agents at the ledger are 39. Under 41: kill the Stalkers on the eastern edge of their range (32-35, 36-41) one at a time; no quest here is held back for level. (The plan's table says "wants 42"; see Deviation 3.)

## 2. Entry state
- Where: Aerie Peak, the Hinterlands, at the end of chapter 44 (plan: chapter 44 ends at Aerie Peak with Rhapsody Shindigger).
- Hearth: Farholde Keep. Last bind is `[S Farholde Keep]` at 38_RivergladesI.lua:39; `[H Farholde Keep]` at 39e:65, 40:50, 41:79. The plan keeps Farholde through chapter 44; chapter 44 is specced in parallel, so the main session confirms it did not rebind.
- Carried in:
  - 95295 I Know a Guy (picked up from Friz Frazzlespark 255897 in chapter 42; plain pickup there per the plan). Required here.
  - Passing through, not touched here: 1452 Rhapsody's Kalimdor Kocktail (from chapter 44, for Tanaris / Feralas, handed in chapter 48); 95219 From Port to Port (chapter 42 -> Feathermoon, chapter 47); 95296 Shipping and Handling only if chapter 41's optional smuggling block was done (-> chapter 46).
- Training / professions: no shaman trainer in Booty Bay (Threads: stops are Ironforge in 43, 48, 50, 57 and Aerie Peak in 44, 48). Expert Fishing was bought here in chapter 31 (31:13); Artisan Fishing is Nat Pagle (chapter 48 / 51 Theramore passes). The plan's Threads put no profession gate at Booty Bay. One optional food-thread vendor line (Deviation 4) and one optional fishing line, see the route.

## 3. Travel and hearth
- In: at Guthrum Thunderfist 8018 (Gryphon Master), Hinterlands 11.07,46.15 -> `[F Booty Bay]` "(the game routes it)", round 1's wording (31:30, 31:69, 39c:15). TaxiPath build 70938: Aerie Peak (node 43) - Ironforge (6) - Stormwind (2) - Booty Bay (19); Aerie Peak has no other path toward Booty Bay. All three hops are known flight points (Booty Bay `[P]` at 30:92; Stormwind and Ironforge flown from in round 1). Arrive at Gyll 2859, Stranglethorn 27.53,77.79.
- Bind: Innkeeper Skindle 6807, Stranglethorn 27.04,77.31, `[S Booty Bay]` on arrival (plan: "bind at Booty Bay for this chapter"; chapter 46 binds Gadgetzan). Round 1 bound the same innkeeper at 31:11.
- In the zone: Booty Bay to Nesingwary's camp is the road north, about 67 map units (round 1 rode it at 30:91 the other way: "Ghost Wolf and do not stop"; it passes Grom'gol, Horde). Road not in the data.
- Back: `[H Booty Bay]` from Nesingwary's camp. On cooldown: Astral Recall does the same (round 1 wording, 31:62); otherwise ride south on the road.
- Out: the Booty Bay - Ratchet boat. The client has the route (TaxiNodes 34 "Transport, Booty Bay - Ratchet"). The pier is not in the data; the DB puts Grizzlowe 9559 ("Shipmaster") at Stranglethorn 26.08,73.35, on the harbour's north side beside Wharfmaster Lozgil, and Grimble 9558 ("Shipmaster") at The Barrens 63.54,38.61 (Ratchet), which is where 39c:13 boarded the reverse trip (`[G63.1,37.2 The Barrens]`). Use `[G26.1,73.4 Stranglethorn Vale]` for the pier; |cffffcc00unverified|r that the boat docks there and its times.

## 4. Route

### Leg 1 - Booty Bay (arrival)
1. `[OC]` level-check line (section 1).
2. `[OC]` Carried in: I Know a Guy (95295) from Friz in chapter 42. Training: no shaman trainer here (next: Ironforge, chapter 48). 
3. At Guthrum Thunderfist 8018, Aerie Peak, `[F Booty Bay]` (the game routes it) `[G11.1,46.2 The Hinterlands]`.
4. At Innkeeper Skindle 6807, bind `[S Booty Bay]` (Farholde's bind ends here; chapter 46 binds Gadgetzan) `[G27.0,77.3 Stranglethorn Vale]`.
5. Turn in **95295 I Know a Guy** at Caravaneer Ruzzgot 3945, Stranglethorn 27.37,74.08 `[G27.4,74.1 Stranglethorn Vale]`. 315 XP, 0 money (zone_16591 / zone_33). Quest row [1] Friz 255897, [2] Ruzzgot 3945; req 36, L40. Plain. No reward. Wowhead series 95295 > 95322 > 95325.
6. Accept **95322 Get the Goods** at Ruzzgot 3945 (same spot). 2,350 XP at the hand-in, 0 money. Objective (quest row [7] and the nether tooltip, 13 Nov): "Find the Bloodsail Trunk outside of Booty Bay in Stranglethorn Vale." Requirement: "Bloodsail Trunk examined". QuestieDB row has no objectives ([9] null), no required level ([3] null; Wowhead 36), no prerequisites ([11]/[12] null). Plain.
7. Conditional: at Wharfmaster Lozgil 4631, Stranglethorn 26.35,73.56, `[O]` accept **97332 Twice Misplaced Trust** "if Lozgil offers it" `[G26.4,73.6 Stranglethorn Vale]`. 3,300 XP at Wharfmaster Whizzbuzz 259961, Riverglades 79.45,52.71 (chapter 48; counted there as optional). Quest row [1] [[4631]], [2] [[259961]], req 36, L41, [10] = 277974 (Twice Reordered Package, given on accept), no prerequisite in the DB. Wowhead series 97329 > 97328 > 97331 > 97332 (quest page pulled 13 Nov, r2_pages3 row 24); 97331 Zimmix's Great Escape is out (verdict COND, `_decisions.tsv`), and round 1 did only 97328 (30:64, 30:93). Label: conditional, "if offered" - do not promote. Not shareable (Wowhead page).
8. Find the Bloodsail Trunk for **95322** `[QC95322]`. **The trunk's position is not in the data**: no object named "Bloodsail Trunk" in object.json (case-insensitive search for "trunk" and "bloodsail"), no Wowhead page for 95322 in `wowhead_quest_links.json` or the three r2 page pulls, no npc of that name. Hints only, both |cffffcc00unverified|r: the Bloodsail Correspondence object 2083 (the Classic Bloodsail camp, quest 595/597) at Stranglethorn 27.28,69.52, four units north of Ruzzgot along the coast; and a Forever-only camp of seven Venture Co. Mercenaries 260425 (level 36-37, rank none) at 29.7-30.5,70.4-72.7, just north-east of town. Write the step with `[G27.3,69.5 Stranglethorn Vale]` and the text "the trunk's spot is not in the data: look along the coast north of town (unverified)", unless the Needs-pull item settles it first.
9. Turn in **95322 Get the Goods** at Ruzzgot 3945 `[G27.4,74.1 Stranglethorn Vale]`. 2,350 XP, 0 money. No reward.
10. Accept **95325 We've Been Robbed!** at Ruzzgot 3945. 2,350 XP at the hand-in, 0 money. Objective: "Find the Venture Co. Ledger in the Venture Co. Camp near Lake Nezferiti in Stranglethorn." It **ends at the object** Venture Co. Ledger 630887 (quest row [2] = [null, [630887]]; Wowhead end o630887), Stranglethorn 42.76,18.53 (object row [3]). Plain.
11. `[O]` Cooking (Deviation 4): at Kelsey Yance 2664, Stranglethorn 28.23,74.34, `[V]` Recipe: Cooked Glossy Mightfish 13940 (1g 60s = 4 x the 40s sell price, tooltip 2026-11-12; Requires Cooking 225; food: +30 attack power for 15 min and +5% kill XP, eaten from level 35) - only if you did not buy it in chapter 31 (31:14 offered it "if gold allows"). Learn it at Cooking 225 (Artisan Cooking is chapter 46's Clamlette Surprise gate). Item row [13] vendors = [2664] (the only vendor in the DB). `[G28.2,74.3 Stranglethorn Vale]`.
12. Ride north on the road to Nesingwary's camp (about 67 units; Ghost Wolf `[A Shaman]`, outdoors only). Grom'gol (Horde) stands on the west coast beside the road: do not stop.

### Leg 2 - north Stranglethorn
13. Accept **196 Raptor Mastery** at Hemet Nesingwary 715, Stranglethorn 35.66,10.81 `[G35.7,10.8 Stranglethorn Vale]`. 2,450 XP at the hand-in, 0 money (zone_33). Objective (row [9]): kill 10 Jungle Stalker 687. Req 28, L41. Prerequisite row [12] = [195] Raptor Mastery, handed in plain at 30:80 (`[QT195]`; 194 at 30:71). This is the third part of Hemet's raptor chain (194 Stranglethorn Raptors > 195 Lashtail Raptors > 196 Jungle Stalkers > 197 Tethis). Its follow-up 197 (Tethis, 43 elite) is out: silent.
14. East to the Venture Co. camp at Lake Nezferiti: click the **Venture Co. Ledger** 630887, turn in **95325 We've Been Robbed!** `[QT95325]` `[G42.8,18.5 Stranglethorn Vale]`. 2,350 XP, 0 money. Mobs on it (DB): Venture Co. Agent 260429, level 39, rank none (Wowhead NPC page in r2_pages: Level 39, no Elite line, hostile to both factions), 19 spawns at 42.0-44.8,18.2-23.1; Venture Co. Workboss 1095 (36) at 43.11,19.01, Lumberjack 921 (34-35), Mechanics 1097 (34-35), Shredders 4260 (37) at 46.43,19.87 and 43.9,23.17. The ledger also starts 95326 The Big Payback (out, rule 12: Ruzzgot's Shipment 268810 29.29%, drop_rates.json 12 Nov, single dropper Venture Co. Agent): silent, no line.
15. South-west to the Jungle Stalkers: kill 10 **Jungle Stalker** 687 (level 40-41, rank none, 43 spawns) `[QC196]` `[G31.0,42.5 Stranglethorn Vale]`. Their range in the DB: an eastern band 28-35,36-46 (densest 28.8-32.5,41.7-44.6; nearest to the camp 32.6-34.7,36.5-40.2) and a western group 23-28,48-52. About 23 units from the ledger to the band's north end. Young Jungle Stalkers 854 (36-37, four spawns at 31-32,42-45) stand among them and do not count. `[OC]` Skin them.
16. Turn in **196 Raptor Mastery** at Hemet Nesingwary 715 `[G35.7,10.8 Stranglethorn Vale]`. 2,450 XP, 0 money. No reward (zone_33 itemchoices / itemrewards empty).
   Order note: ledger first, then the Stalkers, then Hemet is about 65 units of riding after the pickup; Stalkers first and the ledger last is about 73.
17. Hearth to `[H Booty Bay]` (cooldown: Astral Recall, or the road south).

### Leg 3 - Booty Bay and the boat
18. Conditional: at Caravaneer Ruzzgot 3945, `[O]` accept **95327 All's Well That Ends Well** "if Ruzzgot offers it" `[G27.4,74.1 Stranglethorn Vale]`. 3,150 XP at Friz Frazzlespark 255897, Riverglades 77.1,52.9 (chapter 48; counted there as optional). Quest row [1] [[3945]], [2] [[255897]]; no prerequisite in the DB, Wowhead series empty. Verdict COND (`_decisions.tsv`): Ruzzgot is where The Big Payback (95326, out) ends, so the link is suspected, not proven. No reward.
19. Conditional: **95384 Partial Mystical Notes** - `[O]` only if the Partial Mystical Notes (item 213127) are in your bags: use them to start the quest `[UI213127]`, then turn in at Dudd Fizzlescroll 260873, Stranglethorn 28.27,76.35 `[QT95384]` `[G28.3,76.4 Stranglethorn Vale]`. 3,150 XP + 50s (zone_33). Quest row [1] null (no starter), [2] [[260873]], req 32, L40, objective item 213127. Item: BoP, unique, "This Item Begins a Quest", requires level 35; dropped only by Skullsplitter Mystic 780 (level 39-40, 67 spawns round 42-49,30-42, not on this route), 8.38% (drop_rates.json 12 Nov). Rule 12: under 30%, so no kill line; the plan counts it as conditional ("taken only if the item drops"). Reward: Dudd's Second-Favorite Wand 277256 - not usable (section 5).
20. `[O]` Fishing: fish the Booty Bay harbour toward 225 while you wait for the boat `[SK Fishing 225]` `[G26.1,73.4 Stranglethorn Vale]` (the Artisan Fishing quest at Nat Pagle, chapter 48 / 51, needs 225; Threads). Optional, profession-rank gate (rule 11).
21. `[OC]` Check line (section 7).
22. Take the boat to Ratchet from the pier by Grizzlowe, Shipmaster 9559 `[G26.1,73.4 Stranglethorn Vale]` (pier and times |cffffcc00unverified|r). It lands at Ratchet by Grimble 9558, The Barrens 63.54,38.61, where chapter 46 starts.

## 5. Gear calls
- Required quests: none has a reward choice or a wearable reward (zone_33 / zone_16591: 196, 95295, 95322, 95325 itemchoices and itemrewards empty).
- 95384 (conditional): Dudd's Second-Favorite Wand 277256 (Ranged Wand, 35.67 dps, +5 Int, +1 mp5, Requires level 40, sell 1g 20s 13c; tooltip 2026-11-12). Shamans cannot use wands: SkillRaceClassInfo row 144 (skill 228 Wands) has ClassMask 400 (priest, mage, warlock; no shaman bit 64). Vendor it.
- 97332 (conditional, picked up here, chosen at the chapter-48 hand-in): Apology Ring 278019 (+6 Sta, +4 spell damage) 8.0 central / 4.0 conservative over Renegotiated Ring 278018 (+3 Str +6 Sta) 6.0 / 6.0; Refunded Ring 278017 (+8 Sta) 0.0. Level-40 band weights (score_items.py --band 40 header: str 2.00, sp 2.00 / 1.00, sta 0). Replaces whichever ring scores lower at that point; the chapter-48 spec makes the call. Also rewards a Jug of Badlands Bourbon 2595.
- 95327: no reward.

## 6. Out (silent; reasons from `_decisions.tsv`)
- 197 Raptor Mastery: elite outside a dungeon (rule 13): Tethis (43 elite). 193 Panther Mastery: Bhag'thera (40 elite). 208 Big Game Hunter: King Bangalash (43 elite).
- 95326 The Big Payback (starts at the ledger): drop under 30%: Ruzzgot's Shipment 29.29%.
- 78823 Terror of the Desert Skies (drop-start, hand-in Hemet): drop-start from Tho'grun's Dustbelchers (about 6-14%); the Badlands trip is dropped (Braedyn, 13 Nov). 78830 Terror of the Desert Skies (Hemet): given for a Hunter rune; its item comes from the Badlands.
- 189 Bloodscalp Ears 16.7%; 205 Troll Witchery 17.7% (206 Mai'Zoth behind it); 209 Skullsplitter Tusks 18.3%; 587 Up to Snuff 25.4%; 576 Keep An Eye Out 1.9%; 600 Venture Company Mining 29.6%; 606 Scaring Shaky 25.76% (607, 609, 613 behind it): drop under 30% (rule 12).
- 338 The Green Hills of Stranglethorn and 339-342 Chapters I-IV: pages are low zone-wide drops.
- 621 Zanzil's Secret (30.6%), 617 Akiris by the Bundle (31.3%; 623 behind it): XP-only optional (rule 11).
- 97405 Noise Complaints, 8551 The Captain's Chest, 8552 / 8553 / 8554 (Mok'rash, Negolash), 630 Message in a Bottle (King Mukla), 619 Enticing Negolash: elite outside a dungeon (rule 13).
- 614, 615, 618, 620: old copies. 1127 Fool's Stout: chain behind out quests. 7810 / 7908 Arena Master: event / arena. 9272 Dressing the Part: no XP. 605 Singing Blue Shards: below the bracket.
- Not out, placed later: 608, 348, 580, 594, 624, 625, 626, 95385 (chapter 50); 3721 An OOX of Your Own (LATER, round 3).

## 7. End check
`[OC]` Check: handed in here: I Know a Guy (95295), Get the Goods (95322), We've Been Robbed! (95325, at the ledger), Raptor Mastery (196); Partial Mystical Notes (95384) only if the notes were in your bags. In the log for later chapters: Twice Misplaced Trust (97332, Whizzbuzz, chapter 48) and All's Well That Ends Well (95327, Friz, chapter 48), each only if it was offered; Rhapsody's Kalimdor Kocktail (1452, chapters 46-48); From Port to Port (95219, chapter 47); Shipping and Handling (95296, chapter 46) if you have it. Hearth: Booty Bay (chapter 46 binds Gadgetzan). You stand on the boat to Ratchet.

## 8. Totals
- Required: 4 quests, **7,465 XP**, **0 money**: 196 2,450; 95295 315; 95322 2,350; 95325 2,350. Equals the plan's XP-table row 45 (4 / 7,465 / 00s).
- Optional / conditional counted here: 95384 3,150 XP + 50s. Equals the plan's 3,150.
- Picked up here, counted in chapter 48 (0 XP here): 95327 3,150; 97332 3,300 (both conditional).

## 9. Unverified / in-game test list, Needs pull, Unsure
Unverified / test list:
- The Bloodsail Trunk's position (95322): not in any data file; the hint points (27.3,69.5 Bloodsail Correspondence; 29.7-30.5,70.4-72.7 Mercenary camp) are guesses.
- Whether Lozgil offers Twice Misplaced Trust (97332) without 97329 / 97331.
- Whether Ruzzgot offers All's Well That Ends Well (95327) without The Big Payback (95326).
- The Booty Bay pier for the Ratchet boat (Grizzlowe 9559 at 26.08,73.35 is the DB's only marker) and the boat's times.
- Whether `[QC95322]` completes on "Bloodsail Trunk examined" (a click objective QuestieDB does not list).

Needs pull (Wowhead page, browser):
- quest=95322 Get the Goods: the map pin of the Bloodsail Trunk (and the object id). This is the one fact the chapter lacks.
- Optional: quest=95327, to see whether its page names 95326 as a prerequisite (the 13 Nov links row shows an empty series and no prerequisite field is pulled).

Unsure:
- **Whiskey Slim's Lost Grog (580, chapter 50) would save a trip if picked up here.** Its giver Whiskey Slim 2491 stands in Booty Bay (27.14,77.45; req 40, no prerequisite in the DB), but its item, Pupellyverbos Port 3900, comes only from the object 2068, whose spawns are all in **the Hinterlands** (zone 47, about 48 points at 73-82,46-95). Chapter 48 is the Hinterlands; chapter 50 comes after it. Picked up in chapter 50, the port needs another Hinterlands trip; picked up here, chapter 48 can collect it and chapter 50 hands it in. Not taken here because the plan lists 580 in chapter 50; the main session and the chapter 48 / 50 specs decide.
- **Cortello's Riddle (624-626, chapter 50)** for the chapter-50 spec: 624 starts from the scroll object 2554 south of Booty Bay (29-34,88-90) and ends at A Soggy Scroll 2553 in the **Swamp of Sorrows** (22.87,48.19); 625 ends at Musty Scroll 2555 in **Dustwallow Marsh** (31.11,66.14); 626 ends at Cortello's Treasure 2556 in **the Hinterlands** (80.79,46.82). A pickup of 624 here saves nothing (its next stop is the Swamp, which chapters 46-48 do not visit), but chapter 50 cannot finish 625 / 626 at the Cape as the plan's chapter text implies.
- The level check: 41 by the mobs vs the plan's 42 (Deviation 3).
- Whether chapter 44 leaves the hearth at Farholde (assumed) - it does not change this chapter, which binds Booty Bay anyway.

## 10. Deviations from the route plan
1. **Pickups for chapter 48 named here.** The plan counts 95327 All's Well That Ends Well and 97332 Twice Misplaced Trust in chapter 48 without saying where they are picked up; their givers are Ruzzgot 3945 and Lozgil 4631 in Booty Bay (quest rows [1]). Both are written here as conditional "if offered" pickups (0 XP here). No change to the counts.
2. **The Bloodsail Trunk has no position**; the step carries a hint `[G]` marked unverified (section 4, step 8) until quest=95322 is pulled.
3. **Level check 41 instead of 42.** Rule 14 sets it from the highest required level (36) or the mobs (Jungle Stalkers 40-41, npc 687 rows [3]/[4]). The plan's "wants 42" is the round's floor, not a figure from this chapter's data. Either works: entry is predicted at 42.4. The main session may keep 42.
4. **Two optional lines the plan does not list** (no XP effect): the Recipe: Cooked Glossy Mightfish vendor line at Kelsey Yance (food thread past Mithril Head Trout, rule 5 / rule 11; only if not bought in chapter 31; Threads leave recipe vendors to the specs) and a "fish toward 225" line while waiting for the boat (gate for Artisan Fishing in chapter 48 / 51). Drop either if the main session prefers.
5. Route order inside the north leg: the ledger (95325) comes before the Stalkers and the hand-in at Hemet, because 196 must be accepted at Hemet first (row [1] [[715]]) and the Stalkers stand south of the camp; this is the shortest order found (about 65 units vs 73).
