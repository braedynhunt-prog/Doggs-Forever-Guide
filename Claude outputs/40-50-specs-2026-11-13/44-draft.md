# Spec: chapter 44 Badlands (and the Aerie Peak leg that has to move) - drafted 13 Nov 2026

Data used: QuestieDB Forever 1.0.16 (`tooling/qdb`, pulled 12 Nov), `data/zone_3.json` (Wowhead XP and money, browser 12 Nov), `data/drop_rates.json` (rows dated 12 Nov), `data/wowhead_quest_links.json`, `weights/tooltips/2026-11-12.json`, `python weights/score_items.py --band 40`, `tooling/trainer_costs.json` (12 Nov), `tooling/client/1.60.1.70938/TaxiPath.csv`. Shell tooltips read today: nether.wowhead.com/forever/tooltip/quest/78823, /78830, /737 and item/211269, 211301, 4613; nether classic tooltip item/4613; classicdb.ch item 4613.

**Headline: the plan's chapter cannot be played as written.** Three findings change it (all under Deviations, section 10):
1. **1449 To The Hinterlands is accepted from Brohann Caskbelly in Stormwind and needs 1448 first** (quest row [1] = [[5384]], row [12] preQuestSingle = [1448]; 1450 row [12] = [1449], 1451 row [12] = [1450], 1452 row [12] = [1451]). 1448 is chapter 45's. So the whole Aerie Peak leg (1449, 1450, 1451, the 1452 pickup, Drakk and Maret) must come after chapter 45's Stormwind / Temple leg and before chapter 46 (Tanaris, where the Roc Gizzards are; quest items drop only with the quest in the log). This spec writes chapter 44 as the Badlands only and gives the moved leg in full (section 4, "Leg moved to chapter 45").
2. **737 Forbidden Knowledge cannot be had**: row [12] = [735, 736]; 736 is the Horde twin, 735 The Star, the Hand and the Heart is OUT in `_decisions.tsv` (rule 13: Grel'borg the Miser 39, Dagun the Ravenous 43, Mogh the Undying 44, npc row [5] = 1 for all three). Out, silently, with 735.
3. **708 The Black Box has no known source**: it starts from the Corroded Black Box (4613), and item row [1] npcDrops, [2] objectDrops and [3] itemDrops are all null in qdb 1.0.16 and in qdb_classic; drop_rates.json has no row; the Forever and Classic nether tooltips carry no "Dropped by"; classicdb.ch item 4613 has no dropped-by / contained-in tab. It cannot be a plain required step until a Wowhead Forever item page says where the box comes from (Needs pull). Written as conditional, both ways.

---

## 1. Header
- File: `44_Badlands.lua`
- Title: `[N 42-43 Badlands]` (the plan's title, unchanged)
- Next: `[NX 42-44 Stranglethorn Vale]` (chapter 45 as the plan titles it; if chapter 45 is re-titled because it gains the Aerie Peak leg, use its new title)
- `[GA Alliance]`
- Description: `[D Forever Shaman 30-60 (Braedyn)\\The Badlands at 42: Garek's Tremors of the Earth against Boss Tho'grun, the optional group fight at the Seal of the Earth for the Prismscale Hauberk, and the Corroded Black Box if one drops; then Ironforge and the flight to Stormwind for chapter 45.]`
- Level on entry 42.6 (plan's XP table); exit about 42.7 on the required 3,600 XP (42.8 with the Black Box, more with 717).

## 2. Entry state
- Stands at Farholde Keep (Riverglades) after the Krol'dok run of chapter 43. Hearth = Farholde Keep (`[S Farholde Keep]` at 38_RivergladesI.lua:39; every later `[H]` is Farholde Keep: 39e:65, 40:50, 41:79; chapter 43's spec should confirm it ends with that hearth).
- Quests carried in that this chapter touches: none. Round 1 did 718 Mirages (35_Badlands.lua:21-25), so 732 is open; round 1 never took 732 (requires level 40). Round 1 handed in 727 To Ironforge for Yagyin's Digest (39e:57), which opens 735 at Gerrig Bonegrip - out (above), so nothing at Gerrig.
- Carried through untouched: whatever chapters 42-43 hand on (Friz's errands 95295 / 95296 / 95383 / 95219, 94894 The Twilight Threat, 94893 Delivering Closure if taken; the chapter 42/43 specs list them).
- Training: none due. The level 42 row was bought in Ironforge at the start of chapter 43 (plan); the 44 row is chapter 49's. One optional reminder at Eldrun on the way through Ironforge (section 4, leg 4).
- Professions: nothing gated in the Badlands. Artisan Skinning was a chapter 39d line (39d:21); a repeat `[O]` reminder at Balthus is offered in leg 4. Artisan Leatherworking (Drakk Stonehand, Aerie Peak) moves with the Aerie Peak leg.

## 3. Travel and hearth
- **In:** at flight master [TAR257087 Gretchen Mayberry] (Riverglades zone 16591, DB centre 61.1,80.8; the guide uses 60.9,80.9 at 38:38 and 39:11), fly Thelsamar. TaxiPath build 70938 has a direct link Farholde Keep (node 3276) - Thelsamar (node 8), cost field 630 (6s 30c, unverified in game). Both flight points are known (`[P Farholde Keep]` 38:38; Thelsamar since round 1).
- Thelsamar flight master [TAR1572 Thorgrum Borrelson] Loch Modan 33.9,51.0.
- **Badlands:** the road south out of Loch Modan, as in chapter 35 (35:17 calls the pass unverified; no NPC or object in the data). No Alliance flight point in the Badlands (TaxiNodes has only Kargath, node 21, Horde).
- **Out:** ride back north to Thelsamar and fly [TAR1572 Thorgrum Borrelson] -> Ironforge (link 8 -> 6, cost 110). Do not hearth: the hearth is Farholde Keep and stays there for chapter 45 (plan's hearth proposal: Farholde Keep through 45). Astral Recall is the same hearth.
- Ironforge flight master [TAR1573 Gryth Thurden] Ironforge 55.5,47.7; Ironforge - Stormwind link 6 -> 2 (cost 50). The Deeprun Tram is not in the data (round 1 uses it, 39d "by tram"; unverified on Forever beyond that). Chapter 45 starts in Stormwind.
- No bind in this chapter.

## 4. Route

### Level check (first line)
`[OC]Level check - this chapter wants level 42`: the quest needs 40 (732 row [3] = 40), but Boss Tho'grun's camp is Dustbelcher Wyrmhunters 40-41 (7 spawns), Maulers 41-42 (11), Shamans 42-43 (7), Boss Tho'grun 41-42 (npc rows [3]/[4]), and the Malevolent Mirages, level 42 ELITE in the DB (npc 269756, row [5] = 1, 106 positions x5-71 y34-79, 16 within 4 units of Tho'grun), roam the whole south and west. Still 40-41? Pull the camp one at a time from its east edge and keep clear of the Mirages; round 2 has no later Badlands pass, so the choice is careful pulls or skipping 732 (3,600 XP) and 717. Predicted entry 42.6.

### Leg 1: Farholde Keep - Thelsamar - Garek
1. `[OC]` heading: Badlands; carried in: nothing for this chapter.
2. Fly: at [TAR257087 Gretchen Mayberry], fly to [F Thelsamar] `[G60.9,80.9 Riverglades]`.
3. Travel line: ride south out of Thelsamar on the road into the Badlands (pass unverified, as in 35). Goto-only step to Garek's spot is fine as a travel line.
4. **Accept 732 Tremors of the Earth** at [TAR2888 Garek] (L50, not elite) `[G61.9,54.3 Badlands]`. XP 3,600, money 0 (zone_3.json). Quest L43, requires 40. Prerequisite 718 Mirages (row [12] = [718]; done in 35:25). Objective: "Retrieve the Sign of the Earth for Garek" - 1 Sign of the Earth (4640). Label: plain. Mobs near Garek: Feral Crag Coyotes 37-38, Dark Riders 41 (npc 218931, 17 spawns x56-59 y52-57, not elite) - normal.
   - Garek also stands next to [TAR7867 Thorkaf Dragoneye] (DB, level 50) - not used.

### Leg 2: west to Boss Tho'grun
5. **Objective 732**: Kill [TAR2944 Boss Tho'grun] (level 41-42; DB rank blank, Wowhead Normal per the plan; one spawn) for the Sign of the Earth [QC732] `[G12.6,75.5 Badlands]`. Drop: Sign of the Earth 93.55% (drop_rates.json 12 Nov, nether tooltip single dropper) - rule 12: a single named mob at 60%+, plain, no budget. His camp: Dustbelcher Wyrmhunter 2716 (40-41), Mauler 2717 (41-42), Shaman 2718 (42-43), all not elite. Dustbelcher Ogre Mages 2720 (43-44) are further south (x7-10 y86-92): stay north of y85.
6. `[OC]` caution note on the Malevolent Mirages (42 elite in DB, wide roam) - unverified whether they patrol or stand; the DB has 106 positions.
7. **Conditional 78823 Terror of the Desert Skies** (`[O]`, not counted): if a Primitive Drawing (211269) drops from the Dustbelchers, right-click it, `[QA78823 Terror of the Desert Skies]` - the item begins the quest (nether tooltip item/211269: "This Item Begins a Quest"; quest row [1] is null, Wowhead quest page start = none, `wowhead_quest_links.json` 78823: start [], end ["n715"], side Both). XP 1,550, money 25s (zone_3.json money 2500). Hand-in [TAR715 Hemet Nesingwary] Stranglethorn 35.7,10.8 - chapter 45 visits Hemet for 196 Raptor Mastery (196 starts and ends at Hemet), so it rides to chapter 45. Rates (drop_rates.json 12 Nov, per mob): Wyrmhunter 49/349 = 14.0%, Mauler 17/292 = 5.8%, Shaman 13/153 = 8.5% (Ogre 15.3%, Brute 11.1%, Warrior 18.2%, Mystic 14.3%; overall 12.8%). Do not kill for it (rule 3); take it if it drops. No item reward (zone_3 itemchoices / itemrewards empty), so rule 11 keeps it only as the plan's conditional line: no extra kills, just the pickup.
8. **Conditional 708 The Black Box** (`[O]`, see Deviations): if a Corroded Black Box (4613) is in your bags, right-click it, `[QA708 The Black Box]` (2,350 XP + 50s; requires 30, L40). The data names no source; place the line here, after the kills, as "if one dropped anywhere in the Badlands". Hand-in in leg 4.

### Leg 3: back to Garek, and the optional Seal of the Earth
9. **Turn in 732** at [TAR2888 Garek] `[G61.9,54.3 Badlands]` (3,600 XP).
10. `[OC][A Shaman]` gear note for 717 (section 5) before the accept, so he knows whether it is worth a group.
11. **Optional 717 Tremors of the Earth** - `[O]` `|cFFFF0000GROUP 5+|r`, kept for the Prismscale Hauberk (rule 13; only if it is an upgrade, see section 5). Accept at [TAR2888 Garek] `[G61.9,54.3 Badlands]`. XP 5,900, money 0 (zone_3.json). L50, requires 40, row [12] = [732]. Source item: the Sign of the Earth (row [10] = 4640) - it stays in the bags from 732. Objective text (row [7]): use the Sign at the Pillars of Amethyst, Opal and Diamond for the three runestones, place them in the Seal of the Earth to free Blacklash and Hematus, kill both and bring Blacklash's Bindings, the Chains of Hematus and the Sign back.
12. Runestones, solo (no elites at the pillars; the DB has Scalding Whelps 41-43, not elite, at Opal and Diamond; a "Shadowy Figure" 218241 level 63 with 2 / 1 positions near Opal / Diamond - unverified what it is, give it room). Use `[CI]` per runestone (one of several items of one quest - lesson 11 Nov round B):
    - Pillar of Opal (object 2848) `[G72.3,66.9 Badlands]` -> Opal Runestone [CI4844,1]
    - Pillar of Amethyst (object 2858) `[G81.3,64.3 Badlands]` -> Amethyst Runestone [CI4843,1]
    - Pillar of Diamond (object 2842) `[G83.5,32.8 Badlands]` -> Diamond Runestone [CI4845,1]
    (Order Garek - Opal - Amethyst - Diamond - Seal keeps the ride one loop; runestone ids from qdb item rows 4843-4845, row [2] objectDrops = the pillar.) Whether the Sign is "used" on each pillar (an item use) or the pillar is just clicked is unverified; Guidelime `[UI4640]` is unverified on Forever (RULES writing rules) - write it as "click the pillar (use the Sign of the Earth if it asks)".
13. GROUP step: at the Seal of the Earth (object 2933) `[G81.5,49.9 Badlands]`, place the runestones and kill [TAR2757 Blacklash] (level 50 ELITE, npc row [5] = 1; DB spawn 81.9,49.5) and [TAR2759 Hematus] (level 50 ELITE; 82.0,49.9) [QC717]. Drops: Blacklash's Bindings (4615) 77.78% and Chains of Hematus (4645) 87.5% (drop_rates.json 12 Nov, nether single-dropper tooltips) - single named mobs at 60%+, plain within the optional quest; one kill each, if an item fails to drop do not wait for a respawn: `[QS717]`. Around the Seal: Scorched Guardians (2726) level 43-45 ELITE, 12 positions x77-85 y45-58. Group wording: two level-50 elites released together, 7-8 levels over you, plus 43-45 elite guards: `|cFFFF0000GROUP 5+|r` (or one level-55+ helper). No group within the 2-minute rule? `[QS717 Tremors of the Earth]` and move on.
14. **Turn in 717** at [TAR2888 Garek] `[G61.9,54.3 Badlands]` (5,900 XP) - gear choice, section 5. 717 lists 779 Seal of the Earth as a child quest (row [13] = [779]; 779 is no-XP and out) - nothing to do.
15. If 717 was not done: abandon nothing (717 never taken). The Sign of the Earth then stays in the bags - note it can be sold or destroyed (unverified that it vanishes on 732's turn-in; it is 717's source item, row [10]).

### Leg 4: out by Thelsamar to Ironforge
16. Travel: ride north to Thelsamar (same pass).
17. Fly: at [TAR1572 Thorgrum Borrelson], fly to [F Ironforge] `[G33.9,51.0 Loch Modan]`.
18. **Conditional turn in 708** (only if the Corroded Black Box dropped): at [TAR2092 Pilot Longbeard] in the Hall of Arms, `[QT708]` (2,350 XP + 50s) `[G72.7,94.0 Ironforge]`. If the pull (Needs pull) shows a high-rate source on mobs this route kills, the accept becomes a plain kill-and-accept step in leg 2 and this a plain turn-in.
19. `[O][A Shaman]` at [TAR258098 Eldrun Stormbreaker] `[G47.1,13.8 Ironforge]` `[T]`: the level 42 row only if chapter 43's stop was skipped - Grace of Air Totem 1, Fire Resistance Totem 2, Windfury Totem 2 at 1g 60s each, Fire Nova 4 at 1g 89s 47c (trainer_costs.json 258098, 12 Nov; 6g 69s 47c in all). Must/buy marks from the leveling sheet as chapter 43 sets them.
20. `[O]` at [TAR6291 Balthus Stoneflayer] in the Great Forge `[G39.9,32.5 Ironforge]` `[T]` Artisan Skinning (5g) once Skinning is 200, only if not bought in 39d (Threads).
21. Fly: at [TAR1573 Gryth Thurden], fly to [F Stormwind] `[G55.5,47.7 Ironforge]` (or the tram, unverified).
22. `[OC]` Check line (section 7).

### Leg moved to chapter 45 (the Aerie Peak leg) - every fact, for the chapter 45 spec
Placement: in chapter 45 **after** 1448 In Search of The Temple is handed in to Brohann Caskbelly and **before** the Booty Bay legs (1452's items drop only with the quest in the log, and 46 starts the Roc kills).
- At [TAR5384 Brohann Caskbelly] Stormwind 69.5,40.4: `[QT1448]` (chapter 45) and **accept 1449 To The Hinterlands** (1,800 XP, money 0; L43 req 38; row [12] = [1448]; objective: speak with Falstad).
- Stormwind [TAR352 Dungar Longdrink] 71.3,72.2 -> Ironforge (link 2 -> 6) -> Aerie Peak (link 6 -> 43, cost 730). Aerie Peak flight point is known (`[P Aerie Peak]` 29:67). A plain "fly to Aerie Peak" from Stormwind is a two-hop route (no direct Stormwind - Aerie Peak link in TaxiPath).
- Aerie Peak flight master [TAR8018 Guthrum Thunderfist] Hinterlands 11.1,46.1 (guide 29:67 uses 11.1,46.2).
- **Turn in 1449 / accept 1450 Gryphon Master Talonaxe** at [TAR5635 Falstad Wildhammer] (L50) Hinterlands 11.8,46.8. 1450: 890 XP, money 0, L43 req 38, row [12] = [1449]; speak with Talonaxe in the Aviary.
- **Turn in 1450 / accept 1451 Rhapsody Shindigger** at [TAR5636 Gryphon Master Talonaxe] (L44) Hinterlands 9.8,44.5. 1451: 1,800 XP, money 0, L43 req 38, row [12] = [1450].
- `[A Shaman]` at [TAR270263 Farseer Maret Firetend] 14.4,42.6 `[T]`: level 42 row if not bought (same four ranks and prices as Eldrun, trainer_costs.json 270263: 1g 60s x3 + 1g 89s 47c); no Ghost Wolf on her list (29:68).
- `[O]` at [TAR11097 Drakk Stonehand] 13.4,43.5 `[T]` Artisan Leatherworking (spell 10662, skill 200, 5g = 50000c, trainer_costs.json 11097, 12 Nov) - only at Leatherworking 200; character-level gate unverified (Classic 35).
- Walk east out of Aerie Peak to [TAR5634 Rhapsody Shindigger] (L44) **Hinterlands 26.9,48.6** - not in Aerie Peak: about 15 map units east. On the way (DB, zone 47, x15-30 y40-55): Trained Razorbeaks 40-42 (friendly per 29:66), Mangy Silvermanes 41-42, Vicious Owlbeasts 42-43, Silvermane Wolves 43-44, Highvale Outrunners 43-44 / Marksmen 45-46 / Rangers 46-47 (a few positions), Vengeful Spirits 45 (221828, 6 positions). None elite in the DB.
- **Turn in 1451 / accept 1452 Rhapsody's Kalimdor Kocktail** at Rhapsody (26.9,48.6). 1452: 3,600 XP (counted in chapter 49), L43 req 38, row [12] = [1451]. Objectives (row [7]): 3 Roc Gizzards (6257), 3 Groddoc Livers (6259), 3 Ironfur Livers (6258); row [9] counts are 0 in the DB, the count is from the text. Collected in 46 (Rocs) and 47 (bears, apes); hand-in at Rhapsody in 49. Per-mob rates (drop_rates.json 12 Nov): Roc 21/171 = 12.3%, Fire Roc 46/960 = 4.8%, Searing Roc 1/31; Ironfur Bear 25/117 = 21.4%, Grizzled 12/45 = 26.7%, Patriarch 8/29; Groddoc Ape 39/148 = 26.4%, Thunderer 9/32.
- Back to [TAR8018 Guthrum Thunderfist] and fly on (Aerie Peak - Ironforge - Stormwind - Booty Bay is the game's route; Aerie Peak - Southshore exists too). Hearth is Farholde Keep, so there is no shortcut back.
- XP moved into chapter 45: 1449 1,800 + 1450 890 + 1451 1,800 = 4,490.

Alternative order (if chapter 45 is to stay one Stormwind-to-Booty-Bay run): play chapter 45's Stormwind and Temple-door legs (Stormwind hand-ins, 1448 with the Pool of Tears, Darkshire / Nethergarde) **before** this chapter, take 1449 at Brohann, then this Badlands chapter, then Ironforge - Aerie Peak (the leg above), then fly to Booty Bay for chapter 45's remainder. That saves one Ironforge - Stormwind hop but splits chapter 45 in two. Main session's choice; either way 1448 precedes 1449.

## 5. Gear calls
- **717 Tremors of the Earth** (choice; tooltips 2026-11-12.json, `score_items.py --band 40` central [conservative]):
  - Prismscale Hauberk (11194) mail chest +3 Sta +4 Int +23 Spi: **64.3 [41.3]**
  - Mindburst Medallion (11196) neck +6 Int +5 Spi +6 spell damage: 34.6 [23.6]
  - Blazewind Breastplate (11193) leather chest +3 Str +23 Agi +5 Sta: 31.8 [31.8] (hand-computed with the band weights Str 2.0, Agi 1.12)
  - Warforged Chestplate (11195): plate, unusable.
  - What he likely wears: Doomsayer's Robe (4746, cloth chest -11 Sta +18 Spi +6 SP, 57.0 [33.0]) - the 709 choice of 39e:43, a quest reward, so most likely; or Intrepid Explorer's Chainmail (95799 reward, 53.4 [37.4], 31:80); or **Deathchill Armor** (10764, mail chest, 66.7 [44.7], Amnennar 25.80% per its tooltip, 39b:35) only if it dropped.
  - Call: **Prismscale Hauberk** replaces Doomsayer's Robe (+7.3 central, +8.3 conservative) or the Intrepid chainmail (+10.9). **With Deathchill Armor, 717 is no upgrade**: the Hauberk is 2.4 below it, and the Mindburst Medallion (34.6) loses to the Curio-Adorned Necklace (42.7) from 94998 in chapter 42 (a required quest). So the 717 line reads "only if you are not wearing Deathchill Armor" (rule 11: kept only for a scored upgrade).
- 732, 708, 78823: no item rewards (zone_3.json itemchoices / itemrewards empty for all three).
- 1449-1452 (moved leg): no item rewards.
- (Out, for the record: 737's fixed reward is the Skull of Impending Doom, an off-hand, not for a two-hander.)

## 6. Out (zone 3 Badlands quests not in this chapter; reasons from `_decisions.tsv`)
- 737 Forbidden Knowledge - **new**: chain behind 735 (see Deviations).
- 735 The Star, the Hand and the Heart - elite outside a dungeon (rule 13): Grel'borg the Miser (39 elite), Dagun the Ravenous (43 elite), Mogh the Undying (44 elite).
- 692 The Lost Fragments - drop under 30%: Torn Scroll Fragment 3.61%; 656 Summoning the Princess (category 45) - chain behind 692.
- 710 Study of the Elements: Rock - below the bracket and nothing kept behind it.
- 711 Study of the Elements: Rock - drop under 30%: Large Stone Slab 18.84%.
- 712 Study of the Elements: Rock - drop under 30%: Bracers of Rock Binding 24.16%; 734 / 777 / 778 This Is Going to Be Hard - chain behind 712.
- 713 Coolant Heads Prevail - below the bracket and nothing kept behind it; 714 Gyro... What? - chain behind 713.
- 733 Scrounging - drop under 30%: Scrap Metal 15.2% (9 droppers, best Dustbelcher Ogre Mage 31% of 35).
- 97617 Safety Checks - drop under 30%: Unstudied Artifact 7.7% (4 droppers, best Shadowforge Darkweaver 29% of 319).
- 716 Stone Is Better than Cloth - chain behind 712.
- 706 Fiery Blaze Enchantments - elite outside a dungeon (rule 13): Scorched Guardian (45 elite).
- 762 An Ambassador of Evil - elite outside a dungeon: Ambassador Infernus (42 elite).
- 779 Seal of the Earth - no XP, nothing kept behind it.
- 2500 Badlands Reagent Run (category 38) - drop under 30%: Rock Elemental Shard 11.4%; 17 Uldaman Reagent Run - chain behind 2500.
- 78830 Terror of the Desert Skies - **moved out of this chapter** (see Deviations): it is accepted at Hemet Nesingwary in Stranglethorn, which comes after the Badlands.

## 7. End check
`[OC]Check:` handed in here: Tremors of the Earth (732); if done, Tremors of the Earth (717); if the box dropped, The Black Box (708). Carried out: Terror of the Desert Skies (78823) only if the Primitive Drawing dropped - to Hemet Nesingwary in chapter 45. Nothing else from this chapter stays in the log. Still carried from chapters 42-43: their list (Friz's errands, The Twilight Threat, Delivering Closure if taken). Hearth = Farholde Keep. You stand in Stormwind for chapter 45, where In Search of The Temple and then the Aerie Peak leg (To The Hinterlands, Gryphon Master Talonaxe, Rhapsody Shindigger, the Kocktail pickup) follow.

## 8. Totals
| | plan row 44 | this spec |
|---|---|---|
| required quests | 6 | 1 (732), or 2 if 708 is confirmed plain after the pull |
| required XP | 12,790 | 3,600 (5,950 with 708) |
| required money | 50s | 0 (50s with 708) |
| optional / conditional XP | 11,350 | 717 5,900 + 78823 1,550 = 7,450 (+ 708 2,350 while it is conditional) |

Reconciliation: 12,790 - 737 2,350 (out) - 1449/1450/1451 4,490 (to chapter 45) - 708 2,350 (conditional pending pull) = 3,600. Optional 11,350 - 78830 3,900 (out of this chapter) = 7,450. Route-wide required XP drops by 2,350 (737) for sure and by another 2,350 if 708 stays conditional; the 4,490 only moves. Predicted exit: about 42.7 (the plan's 12,790 XP moved him 0.2 levels; 3,600 is about 0.06) (route_xp.py not re-run: it reads the plan's route file, which this spec does not change).

## 9. Unverified / in-game test list; Needs pull; Unsure
**Unverified / test list**
- The Loch Modan - Badlands pass (as in chapter 35).
- Malevolent Mirage (269756): 42 ELITE in the DB with 106 positions over the south and west Badlands - stand or roam? Was it there in round 1 (chapter 35 does not mention it)?
- Boss Tho'grun not elite (DB rank blank; Wowhead Normal per the plan).
- The pillars: click or use the Sign of the Earth; whether the Sign of the Earth disappears at 732's turn-in.
- Blacklash and Hematus spawn together at the Seal; Scorched Guardians elite.
- Primitive Drawing drops for a shaman (Season-of-Discovery item, ilvl 1, req 26) and 78823 can be handed in by a shaman.
- Farholde Keep - Thelsamar flight price (TaxiPath cost 630).
- Artisan Leatherworking character-level gate at Drakk (moved leg).
- "Shadowy Figure" (218241, level 63) near the Opal and Diamond pillars.

**Needs pull**
- `wowhead.com/forever/item=4613` (Corroded Black Box): dropped-by / contained-in tabs and rates. This settles whether 708 is plain (rule 12: 60%+ or an object), optional with a budget, or out.
- `wowhead.com/forever/quest=78830`: does a Dwarf Shaman get it (Wowhead reqclass 68 = Hunter + Shaman; QuestieDB row [6] = 4 = Hunter only)?
- `wowhead.com/forever/npc=269756` (Malevolent Mirage): rank and behaviour.

**Unsure**
- With 737 out and 708 unsourced, the Badlands detour carries 3,600 required XP (plus 717 for a group, plus 708 if the pull is good) for about two flights and a long ride (Garek 61.9,54.3 - Tho'grun 12.6,75.5 - Garek). Whether the Badlands leg stays at all is the main session's / Braedyn's call; I kept it as the plan has it.
- Which reorder to use for the Aerie Peak leg (written: moved into chapter 45 after 1448; alternative: chapter 45's Stormwind/Temple legs before this chapter).
- 78823 at chapter 45's Hemet visit assumes the chapter 45 spec keeps 196 Raptor Mastery at Hemet (35.7,10.8).

## 10. Deviations from the route plan
1. **1449, 1450, 1451 and the 1452 pickup move to chapter 45**, after 1448. Fields: 1449 row [1] = [[5384]] (Brohann Caskbelly, Stormwind 69.5,40.4), row [12] = [1448]; 1450 row [12] = [1449]; 1451 row [12] = [1450]; 1452 row [12] = [1451]; 1448 has no prerequisite (rows [11]/[12] null) and is in the plan's chapter 45 list. 4,490 XP moves with them. Drakk Stonehand (Artisan Leatherworking) and Farseer Maret Firetend move with the leg. The plan's prose ("Ironforge - Aerie Peak for Falstad's hand-in") missed that 1449 is accepted in Stormwind.
2. **737 Forbidden Knowledge is out**: row [12] = [735, 736]; 735 is OUT in `_decisions.tsv` (rule 13, three elites, npc row [5] = 1 each); 736 is Horde (race mask 8589934770, Undercity giver Keeper Bel'dugur). -2,350 required XP.
3. **708 The Black Box is conditional until pulled**: item 4613 rows [1]/[2]/[3] null in qdb 1.0.16 and qdb_classic; no drop_rates.json row; nether tooltips (Forever, Classic) show no dropper; classicdb.ch shows none. -2,350 required XP and -50s required money until a pull shows a source.
4. **78830 Terror of the Desert Skies leaves this chapter**: the plan says "shaman-flagged row with no giver", but qdb row [1] = [[715]] (Hemet Nesingwary, Stranglethorn 35.7,10.8; source item 211272 Empty Bait Cage, row [10]) and row [6] = 4 (Hunter); Wowhead zone_3.json reqclass = 68 (Hunter + Shaman); its fixed reward is the Rune of Expose Weakness, "Classes: Hunter" (nether item/211301). It cannot be accepted before the Badlands leg in either order (Hemet comes in chapter 45), and its target Gharrik (213795, level 40, 23.0,67.2 Badlands, Crimson Trophy Quill 92.86%) is in the Badlands, which round 2 does not revisit. -3,900 optional XP here; the Ponderous Loop (11.8) is lost.
5. **78823 is a drop-start**, not a "no giver" quest: nether item/211269 "This Item Begins a Quest". Conditional as planned; its hand-in rides to chapter 45 (Hemet).
6. **717 gets a precondition** the plan did not state: only if he is not wearing Deathchill Armor (66.7 > Prismscale 64.3), since the other choice (Mindburst Medallion 34.6) loses to the chapter-42 Curio-Adorned Necklace (42.7).
7. The plan's chapter text starts "From Ironforge"; chapter 43 ends at Farholde Keep, and Farholde Keep - Thelsamar is a direct link (TaxiPath 3276 <-> 8), so the chapter starts with that flight.
