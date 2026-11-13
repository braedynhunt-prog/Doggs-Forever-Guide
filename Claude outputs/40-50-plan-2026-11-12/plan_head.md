# 40-50 route plan (round 2 of the 30-60 guide, levels 42-50) - 12 Nov 2026, revised 13 Nov

It fixes the chapter list and the per-quest decisions for round 2, the dungeon placement, the profession, training and gear threads, and what the specs still have to settle. It replaces the seven-line zone outline for round 2 in `docs/30-60-plan-2026-11-11.md`. Session plan: `~/.claude/plans/scalable-sauteeing-falcon.md` (approved 12 Nov). Data record: `docs/audit-2026-11-12.md`, section (4).

**In short:** 16 chapters, files `42_...lua` to `57_...lua`, in the group "Forever Shaman 30-60". 161 required quests, 562,175 quest XP, 37g 43s of quest money. At the 65% quest share that takes him from 42.0 to **49.3** on required quest XP alone; 42 -> 50 needs 627,380. Another 178,195 XP is listed as optional or conditional, and three dungeon runs add kill XP the estimate does not count. Braedyn accepted that on 13 Nov: the round ends in Ironforge wherever he is, round 3 starts from there. Order: Riverglades pickups and Krol'dok; Stormwind, the Temple door, Aerie Peak and Booty Bay; Kalimdor (Tanaris, Feralas); back east (the Hinterlands, Searing Gorge, Nethergarde and the Cape); Kalimdor again (Feralas, Maraudon, Tanaris, Zul'Farrak, Azshara, Un'Goro); a closing Ironforge and Nethergarde stop.

## Revision of 13 Nov 2026 - what the first version got wrong
The version Braedyn approved on 13 Nov read 184 required quests, 631,220 XP, level 50.0. The first four chapter specs (drafts in `Claude outputs/40-50-specs-2026-11-13/`) showed that was too high, and why:
- **QuestieDB has no objectives or prerequisites for many Forever-only quests** (72 of the route's quests are Forever-only; 47 have no objectives in the DB). The rule script could not see a 7% drop (What We Lost) or that a quest follows an out or optional quest. All 72 were re-read from Wowhead's quest tooltips on 13 Nov, and Wowhead's series (30 more quest pages pulled) is now used as an offer gate: a quest that the series puts right after an out, optional or conditional quest is written "only if it is offered" and not counted. That moved 17 Riverglades and Krol'dok quests, two in Azshara and one from Booty Bay out of the required list. On drops the other Forever-only quests held up: their items come from ground objects or single named mobs.
- **Three quests sat before their prerequisites**: To The Hinterlands needs In Search of The Temple (the Stormwind leg now comes first); Nekrum's Medallion needs the Hinterlands chain to Thadius Grimshade (Zul'Farrak now comes after it); Forbidden Knowledge needs an elite quest that is out (it is out). `tooling/route_xp.py` now lists such cases.
- **The Badlands leg** was 3,600 required XP once Forbidden Knowledge was out and The Black Box turned out to have no item source. Dropped.
Lessons are logged in `lessons.md` (13 Nov).

**Where the solid quest XP sits** (round-2 zones, by quest level, after the correction; "needed" is all XP for those levels x 0.65):

| quest level | solid | conditional / optional | out by a rule | needed |
|---|---|---|---|---|
| 45 and below | 138,410 | 62,995 | 192,395 | 207,415 (levels 42-45) |
| 46-48 | 181,790 | 17,900 | 82,690 | 240,370 (levels 45-48) |
| 49-52 | 177,430 | 11,800 | 166,860 | 179,595 (levels 48-50) |
| 53-55 | 92,330 | 81,300 | 90,380 | used at 48-50 |

The shortfall is in the first half: chapters 42-45 hold about 34,000 solid XP, so he reaches Tanaris at about 42.5 and enters the Hinterlands and the Searing Gorge a level or more under their level checks on quest XP alone. Each of those chapters orders its quests by mob level and says what to do when under.

## Braedyn's answers (13 Nov 2026) - the plan below is written to them
1. **Round end: yes.** The Temple of Atal'Hakkar (mobs level 46-55 in the DB, most 50-52; quests level 50-55) and Alcaz Prison (Alliance quests all level 53, required level 46-48) open round 3. Round 2 ends in Ironforge with three dungeons: Krol'dok Stronghold, Maraudon, Zul'Farrak.
2. **Noxious Lair Investigation (82): in**, as a plain step with the budget (five Centipaar Insect Parts at 50.7%, about ten kills). The four Tanaris quests behind it (10,980 XP) are plain with it.
3. **Rhapsody's Kalimdor Kocktail (1452): in and required**, not optional ("if we lose out on a lot by not doing the grind then don't make it optional"). Skipping it loses 13,400 XP and the Temple's main quest. Budgets from the per-mob rows: three Roc Gizzards at 12% from plain Rocs, about 25 kills in Tanaris (5.9% over all three roc types); three Ironfur Livers at 24%, about 12 bears, and three Groddoc Livers at 27%, about 11 apes, in Feralas. It is picked up at Aerie Peak in chapter 44 and handed in there in chapter 48; Rhapsody's Tale goes to Stormwind in chapter 50, where Into The Temple of Atal'Hakkar is taken for round 3.
4. **Boss items in dungeons: counted as normal.** Nine dungeon quests of this round (44,700 XP) hang on an item only one boss carries; Wowhead reads those at 12-43% because its sample counts every kill, quest or not. They are labelled normal with a "one kill" note. Trash collections under 30% stay grind / luck.
5. **Leatherworking: Dragonscale, and the Wild Leather chain stays out** ("1", after the explanation). Dragonscale Leatherworking (5141, Peter Galen, Azshara 37.6,65.4: 2 Tough Scorpid Breastplates, 2 Tough Scorpid Gloves, 10 Worn Dragonscales) is an optional gate step in chapter 55 at skill 225. The Wild Leather chain at Pratt McGrubben (seven quests, 20,350 XP, 16 crafted pieces, 6 Thick Armor Kits and 7 Wildvine for the patterns of a leather set with random enchantments, and the entry to Tribal) is out of round 2: its Turtle Scales and Wildvine come from mobs of level 48 and up in the DB. Whether it comes back in round 3 as an optional hand-in thread that stops before the Tribal quest is decided when round 3 is planned.
6. **Left out on judgment: they stay out** (explained 13 Nov; none asked back): Sweet Amber in Westfall (23,300 XP; five fetch steps across zones, one of them Truesilver), six Desolace leftovers at level 39-42 (9,230 XP) and three Arathi and Faldir's Cove leftovers at level 40 (7,850 XP).
7. **Round-1 fix round: done 13 Nov** (TOC 2026.11.13, released; record in `docs/audit-2026-11-13.md`).
8. **`check_sources.py`: fixed 13 Nov.** It compared the local pull date with the build's UTC stamp; it now converts the stamp to local time.
9. **The gap to 50: accepted as it is** ("A"). No rule is relaxed and nothing left out on judgment comes back; the dungeon runs' kill XP and the conditional quests are expected to make up most of it. Dungeon quests are in the count: 79,350 XP of normal and boss-item quests in the three dungeons. Not in the count: the grind / luck dungeon quests and everything behind them (Twilight Mementos and its two follow-ups, Troll Temper, Gahz'rilla, the Shadowshard Fragments, Twisted Evils) and the kill XP of the runs.
10. **Zul'Farrak: moved to the second Kalimdor trip** ("A"), chapter 54 at about 47, after the Hinterlands chain and the Nethergarde stop that give Nekrum's Medallion.
11. **The Badlands trip: dropped.** Tremors of the Earth and the optional group quest for the Prismscale Hauberk go with it.

## Data (all pulled or checked 12 Nov 2026; manifest `tooling/sources.json`)
| source | version / pull | note |
|---|---|---|
| QuestieDB Forever (`tooling/qdb`) | 1.0.16, 12 Nov | replaced on Braedyn's OK; diff in the audit doc |
| Client tables (`tooling/client/1.60.1.70938/`) | build 70938, 12 Nov | flight graph and XP table inputs unchanged from 70888 |
| Wowhead quest XP (`data/zone_*.json`) | 35 zones re-pulled 12 Nov, after the build | no change on any quest chapters 00-41 use |
| Drop rates (`data/drop_rates.json`) | 311 items; 119 item pages and 94 tooltip rows dated 12-13 Nov | rows still dated 11 Nov are round-1 items |
| Quest pages (`data/wowhead_quest_links.json`) | 224 quests; 85 added 12-13 Nov | start, end, side and series; the series is the offer gate |
| Item tooltips (`weights/tooltips/2026-11-12.json`) | 1,527 items, all fetched 12 Nov | against 11 Nov: no stat or price change |
| Trainer costs (`tooling/trainer_costs.json`) | 26 trainers, 12 Nov | the build repriced the Forever-only shaman spells |
| Spell tooltips (`data/spell_tooltips.json`) | re-read 12 Nov | 28 of 28 identical: the level-40 weights stand |
| XP per level (`tooling/route_xp.py`) | warcraft.wiki.gg, pre-2.3 table, read 12 Nov | 40-50 = 1,151,700; 42-50 = 965,200 |

`python tooling/check_sources.py` on 12 Nov after the pulls: QuestieDB and client OK; the Wowhead-derived rows still print STALE because of six off-route zones and the round-1 rows of drop rates and quest links, which are dated 11 Nov (the date comparison itself was fixed on 13 Nov, answer 8).

## How the decisions were made
The pool is every quest on Wowhead Forever of quest level 39-55 that is not Horde-side, is class-free or shaman, is open to a Dwarf, needs level 50 or less, and has no `[QA]` / `[QT]` tag in chapters 00-41, plus the prerequisite chain of each: 702 quests. The rules were applied by script (`Claude outputs/40-50-plan-2026-11-12/`: `pool_r2.py`, `decide_r2.py`, `overrides_r2.tsv`, `plan_r2.py`), then every borderline case was ruled by hand in `overrides_r2.tsv` with its reason. Per quest:
- **Elite targets outside dungeons (rule 13)**: rank from QuestieDB npc row [5] for kill targets and for every dropper of a required item, and from the Wowhead item and NPC pages; the Forever and Classic databases agree on rank for every target checked, and the named targets QuestieDB leaves unranked were read off their Wowhead pages. All out.
- **Drops (rule 12)**: the Wowhead Forever rate over all droppers. 60% or better plain; 30-60% optional only for an upgrade or when the route's kill quests cover it (one case: Water Pouch Bounty); under 30% out with the chain behind it. A named mob's item at 30-60% is one kill only (one case: Andre Firebeard).
- **Dungeons (rule 2)**: required chapters. Quests are normal, normal on a boss item (answer 4), or grind / luck.
- **No giver or no side**: a quest with no giver in the DB and none on its Wowhead page, or a Forever quest whose page states no side and whose giver has no faction in the DB, is conditional: listed, not counted.
- **Prerequisites**: quest rows [11] and [12]; a quest behind an out quest is out; a prerequisite that is neither in the pool nor done (a Horde twin) cannot be met. **Wowhead's series** (`data/wowhead_quest_links.json`) is an offer gate on top: a quest right after an out, optional or conditional quest in a series is conditional. A series is not proof of a prerequisite, which is why such a quest is kept as a conditional line at all.
- **Level**: `tooling/route_xp.py` on `docs/40-50-route-2026-11-12.txt`, the same list this document prints (rule 14). Quests six or more levels under the chapter's entry level are scaled, and the tool lists any required quest whose prerequisite is not done or required in the same or an earlier chapter (none on this route).

