# 40-50 route plan (round 2 of the 30-60 guide, levels 42-50) - 12 Nov 2026

Braedyn approves this before any chapter spec is written. It fixes the chapter list and the per-quest decisions for round 2, the dungeon placement, the profession, training and gear threads, and what the specs still have to settle. It replaces the seven-line zone outline for round 2 in `docs/30-60-plan-2026-11-11.md`. Session plan: `~/.claude/plans/scalable-sauteeing-falcon.md` (approved 12 Nov). Data record: `docs/audit-2026-11-12.md`, section (4).

**In short:** 16 chapters, files `42_...lua` to `57_...lua`, in the group "Forever Shaman 30-60". 177 required quests, 610,790 quest XP, 40g 43s of quest money. At the 65% quest share that takes him from 42.0 to **49.8** on required quest XP alone; 42 -> 50 needs 627,380. Another 156,030 XP is listed as optional or conditional, and three dungeon runs add kill XP the estimate does not count. Order: Riverglades and Krol'dok, a first Eastern Kingdoms loop, Kalimdor (Tanaris, Feralas, Zul'Farrak), back east (the Hinterlands, Searing Gorge, Booty Bay), Kalimdor again (Feralas, Maraudon, Tanaris, Azshara, Un'Goro), and a closing Ironforge stop at 50.

## Questions for you
Each has my recommendation; the plan below is written as if you say yes to all of them.

1. **Where round 2 ends.** The Temple of Atal'Hakkar's mobs are level 46-55 in the DB (most are 50-52) and its quests are level 50-55. Alcaz Prison's Alliance quests are all level 53 and need level 46-48. Recommendation: both open round 3; round 2 ends in Ironforge at 50 with three dungeons (Krol'dok Stronghold, Zul'Farrak, Maraudon).
2. **Noxious Lair Investigation (82), Tanaris.** Five Centipaar Insect Parts at 50.7%, about ten kills. By rules 11 and 12 it is an XP-only optional and goes out, and four quests go with it (The Scrimshank Redemption, both Insect Part Analysis, Rise of the Silithid: 10,980 XP) plus the silithid chain into Un'Goro. Recommendation: keep it as a plain step with the budget on the line. That alone lifts the round to 50.0.
3. **Rhapsody's Kalimdor Kocktail (1452), the Hinterlands.** Three Roc Gizzards at 5.9% (about 50 roc kills in Tanaris), three Ironfur Livers at 24% and three Groddoc Livers at 27% (Feralas). Out by rule 12. But it is the only way to Rhapsody's Tale and Into The Temple of Atal'Hakkar (7,100 XP), the Temple's main quest. Recommendation: keep it optional with the three budgets on the kill lines, because you run every dungeon with all its quests; say so and I drop it and the Temple quest with it.
4. **Boss items in dungeons.** Nine dungeon quests of this round hang on an item only one boss carries. Wowhead reads those at 12-43% because its sample counts every kill, including players without the quest. Recommendation: label them normal with a "one kill" note and count them (this plan does; they are 44,700 XP of the required total). Trash collections under 30% stay grind / luck.
5. **Leatherworking.** Scored on the level-40 weights, the crafted mail open at 42-50 is modest (Turtle Scale 20-39 a piece, Tough Scorpid 18-39; the leather Big Voodoo set 42-47). Dragonscale pays at 52-56 (Blue Dragonscale chest 63.3, legs 71.8, helm 80.4). Recommendation: take Dragonscale Leatherworking (5141, Peter Galen, Azshara) in chapter 55 as an optional gate at skill 225, and leave the six Wild Leather quests (the way to Tribal) out.
6. **Left out on judgment, not by a rule** (say if you want any back): Sweet Amber in Westfall (five fetch steps across zones, one of them Truesilver; 23,300 XP), the Desolace, Arathi and Faldir's Cove leftovers at level 39-42 (about 17,000 XP, all off the route), and Coolant Heads Prevail (wants Frost Oil).
7. **Round-1 fixes found by the data refresh** (listed at the end). Recommendation: one small fix round now with its own release, before the round-2 specs, because the trainer prices and the ram quests are in chapters you reach first.
8. **`check_sources.py` reads today's pulls as stale** because it compares the local pull date (12 Nov) with the build's UTC stamp (13 Nov 01:36). Recommendation: let me change the comparison to local time; it is a three-line tooling fix.

## Data (all pulled or checked 12 Nov 2026; manifest `tooling/sources.json`)
| source | version / pull | note |
|---|---|---|
| QuestieDB Forever (`tooling/qdb`) | 1.0.16, 12 Nov | replaced on Braedyn's OK; diff in the audit doc |
| Client tables (`tooling/client/1.60.1.70938/`) | build 70938, 12 Nov | flight graph and XP table inputs unchanged from 70888 |
| Wowhead quest XP (`data/zone_*.json`) | 35 zones re-pulled 12 Nov, after the build | no change on any quest chapters 00-41 use |
| Drop rates (`data/drop_rates.json`) | 309 items; 117 item pages and 94 tooltip rows dated 12 Nov | rows still dated 11 Nov are round-1 items |
| Quest pages (`data/wowhead_quest_links.json`) | 194 quests; 55 added 12 Nov | most Forever pages in Azshara state no side |
| Item tooltips (`weights/tooltips/2026-11-12.json`) | 1,527 items, all fetched 12 Nov | against 11 Nov: no stat or price change |
| Trainer costs (`tooling/trainer_costs.json`) | 26 trainers, 12 Nov | the build repriced the Forever-only shaman spells |
| Spell tooltips (`data/spell_tooltips.json`) | re-read 12 Nov | 28 of 28 identical: the level-40 weights stand |
| XP per level (`tooling/route_xp.py`) | warcraft.wiki.gg, pre-2.3 table, read 12 Nov | 40-50 = 1,151,700; 42-50 = 965,200 |

`python tooling/check_sources.py` on 12 Nov after the pulls: QuestieDB and client OK; the Wowhead-derived rows still print STALE for the reason in question 8.

## How the decisions were made
The pool is every quest on Wowhead Forever of quest level 39-55 that is not Horde-side, is class-free or shaman, is open to a Dwarf, needs level 50 or less, and has no `[QA]` / `[QT]` tag in chapters 00-41, plus the prerequisite chain of each: 702 quests. The rules were applied by script (`Claude outputs/40-50-plan-2026-11-12/`: `pool_r2.py`, `decide_r2.py`, `overrides_r2.tsv`, `plan_r2.py`), then every borderline case was ruled by hand in `overrides_r2.tsv` with its reason. Per quest:
- **Elite targets outside dungeons (rule 13)**: rank from QuestieDB npc row [5] for kill targets and for every dropper of a required item, and from the Wowhead item and NPC pages; the Forever and Classic databases agree on rank for every target checked, and the ten named targets QuestieDB leaves unranked were read off their Wowhead pages. Out, except Tremors of the Earth's second part (optional, for the Prismscale Hauberk).
- **Drops (rule 12)**: the Wowhead Forever rate over all droppers. 60% or better plain; 30-60% optional only for an upgrade or when the route's kill quests cover it (one case: Water Pouch Bounty); under 30% out with the chain behind it. A named mob's item at 30-60% is one kill only (one case: Andre Firebeard).
- **Dungeons (rule 2)**: required chapters. Quests are normal, normal on a boss item (question 4), or grind / luck.
- **No giver or no side**: a quest with no giver in the DB and none on its Wowhead page, or a Forever quest whose page states no side and whose giver has no faction in the DB, is conditional: listed, not counted.
- **Prerequisites**: quest rows [11] and [12]; a quest behind an out quest is out, a quest behind an undecided one waits with it.
- **Level**: `tooling/route_xp.py` on `docs/40-50-route-2026-11-12.txt`, the same list this document prints (rule 14). Quests six or more levels under the chapter's entry level are scaled.

