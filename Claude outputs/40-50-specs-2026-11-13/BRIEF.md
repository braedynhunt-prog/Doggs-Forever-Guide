# Brief: draft a chapter spec for round 2 of the 30-60 guide (levels 42-50), 13 Nov 2026

You are a subagent working for the main session on Braedyn's WoW Forever levelling guide (Dwarf Shaman, 2H Enhancement, Alliance; a Guidelime addon). Repo: `C:\Users\Braedyn\Documents\WoW Forever Atlas`. You draft the **spec** for the one chapter named in your prompt. You do NOT write the chapter Lua. A later agent writes the Lua from your spec, so the spec must carry every fact that agent needs, each one checked against the data. You are carrying out a plan Braedyn approved: do exactly what this brief and your prompt say. If something is unclear, blocked or looks wrong, do not guess and do not widen scope: write it under "Unsure" in the spec and in your report.

## Hard limits
- Read-only on the repo. The only files you may create are your spec file and throwaway scripts, both in the scratch folder named in your prompt. No git command that changes anything. Do not touch `lessons.md`, `CLAUDE.md`, the guide, the data, the docs.
- Do not run `tooling/tip.py`, `tooling/fetch_tooltips.py`, `tooling/gear_calls.py` or `tooling/dungeon_loot.py` (they write tracked files). Do not run anything under `Claude outputs/40-50-plan-2026-11-12/` (those scripts rewrite the plan).
- No browser, no wowhead.com pages. `nether.wowhead.com/forever/tooltip/item/<id>` and `/tooltip/quest/<id>` from a shell are fine, one request per second.
- Python on this PC wants Windows paths (C:/...). In a Bash heredoc a backslash escape becomes a control byte: avoid backslashes in heredoc scripts, and for anything over ~20 lines write the script with the Write tool and run it by path.

## Read first (in this order)
1. `docs/40-50-plan-2026-11-12.md` - the approved route plan. Read: "Braedyn's answers", "How the decisions were made", the XP table, **your chapter's section** (its note, its Required list and its Optional / conditional list), the chapters before and after yours, "Threads" (training rows and prices, profession gates, hearth and flight proposal, known flight points), and the in-game test list.
2. `docs/RULES.md` (the standing rules; rules 2, 3, 9, 11, 12, 13, 14 and the writing rules matter most) and the repo's `lessons.md`.
3. `tooling/README.txt` (the tools and the qdb row layout).
4. Your zone's pool file(s) in `Claude outputs/40-50-plan-2026-11-12/pool/` (named `<category>_<Zone>.txt`; the plan's chapter section tells you the zones): every candidate quest with giver, ender, prerequisites, kill targets with levels and ranks, item sources and drop rates, rewards. `pool/_decisions.tsv` holds the verdict and reason per quest (columns: category, id, name, level, required level, XP, money, verdict, reason, flags, highest mob level, best scored reward). `Claude outputs/40-50-plan-2026-11-12/overrides_r2.tsv` holds the hand rulings.
5. Format references: `guide/Guidelime_ForeverShaman/38_RivergladesI.lua` (an outdoor chapter of the 30-60 group) and `39e_Uldaman.lua` (a dungeon chapter: quest labels, one-run wording). Read the last 30 lines of the chapter before yours if it exists (chapter 42 follows `41_PowderfusePort.lua`).
6. Round 1's spec for a comparable chapter, as a model of the level of detail: `Claude outputs/30-60-specs-2026-11-11/38.md` (outdoor) or `39e.md` (dungeon).

## What is already decided (do not reopen)
- **The quest list of your chapter is the plan's.** Required quests are required, optional / conditional ones are listed with their label and reason, everything else of the zone is out and gets no tag (rule 4). If the data forces a change (a prerequisite the plan missed, a giver that is not where the plan thinks, a quest that cannot be done at this point of the route), do not silently change the list: put it under "Deviations" with the field values that force it, and write the route both ways if the choice is not obvious.
- Dungeon chapters are required chapters, one run, never a re-run. Labels: normal; normal on a boss item ("one kill only; Wowhead reads N% over all kills"); grind / luck (optional, abandon with `[QS]` if it does not drop).
- Elite targets outside dungeons are out, except where the plan lists a quest as GROUP, optional.
- Weights: the level-40 band for the whole round (`python weights/score_items.py --band 40`, tooltips `weights/tooltips/2026-11-12.json`). Mail counts from 40. Rage of the Storm and Bonebiter are the two-handers he may hold on entry to chapter 42 (see `docs/forever-enh-stat-weights.md`, 11 Nov section, and round 1's gear lines).
- No gold-farming steps. Skipped quests are silent.

## What you settle
- **Order of play** inside the chapter, grouped into legs, so that travel is short and every pickup precedes its objective and hand-in. Quests that are picked up in your chapter but handed in in a later one (or the reverse) are named in the plan's chapter notes; list every carried quest in and out.
- **Every fact of every step**, from the data in the same step, never from memory or from the plan's prose: quest id and exact title (`tooling/qdb/quest.json` row [0]), XP and money (`python tooling/qinfo.py <ids>`; it reads `data/zone_*.json`), giver and ender NPC or object with id, name and `x,y Zone` (`python tooling/loc.py`, `qinfo.py`, `qdetail.py`; where QuestieDB has no giver use `data/wowhead_quest_links.json` and say so), objectives with counts (quest row [7] text and row [9]), kill targets with id, level range and rank (npc rows [3], [4], [5]), item sources and the drop rate with the kill budget (budget = count / rate; rates in `data/drop_rates.json`: use the per-mob rows when the route kills only the good droppers), prerequisites (rows [11], [12]) and every quest that names yours as a prerequisite.
- **Level check**: "this chapter wants level N" (the highest required level among its pickups, or the level its mobs need: say which) and what to do when under it. The plan's predicted entry level is in its XP table.
- **Travel, hearth and flights**: how he gets in and out, with the flight master and innkeeper ids and coordinates from the DB. A flight point must be discovered on foot before it can be flown to: the plan's Threads section lists the known ones. Flight links are in `tooling/client/1.60.1.70938/TaxiNodes.csv` and `TaxiPath.csv`. Roads, boats, passes and dungeon entrances are not in the data: write what is known and mark the rest unverified, briefly. State binds from the `[S]` / `[H]` tags of the earlier chapters, not from memory.
- **Gear calls** for every reward choice of a kept quest: the pick, its score, the runner-up, what it replaces. Read each item's slot, armour type and stats from the tooltip file, never from its name.
- **Trainer, vendor and profession stops** that fall in your chapter (the plan's Threads section says which): prices from `tooling/trainer_costs.json` (12 Nov) and, for vendor items, 4 x the tooltip sell price. Profession gates are optional lines that fire only at the stated skill.
- **Dungeon chapters also**: mob level range inside (npc rows with a spawn in the dungeon's zone id; say when the DB has none), the bosses each quest needs, where each quest is picked up outside, what is shareable, whether the levels call for a wing split (as Scarlet Monastery was split in round 1: `34_ScarletMonastery.lua` and `39c_Alterac.lua`).

## Rules to quote when they decide something
- Rule 12 (drops): plain at 60%+, or with an object source, or a single named mob at 60%+; 30-60% optional with "drop quest, ~N kills" unless the route's kill quests on the same mobs cover the budget; under 30% out with the chain behind it; a named mob's item at 30-60% is "one kill only, then abandon".
- Rule 11 (optional test): an `[O]` step stays only for a scored upgrade, a bag, a food-thread recipe, or a gate (class quest, trainer, profession rank, mount, needed reputation).
- Rule 13: elites outside dungeons are `GROUP n+` and optional, kept only for a scored upgrade.
- Rule 9: every quest picked up is turned in or explicitly abandoned, in this chapter or a named later one.
- Lessons: every id typed is looked up in the same step; search names case-insensitively before calling something absent; when one DB field is empty check the other tables; a step that collects one of several items of a quest is held with `[CI item,count]`, not `[QC id,index]`; a blank Wowhead side is unknown, not excluded.

## Useful commands (run from the repo root)
- `python tooling/qinfo.py <ids>` (add `-s` for one line each), `python tooling/qdetail.py <ids>`, `python tooling/loc.py "<npc name>" <npc id> obj:"<object name>"`
- `python tooling/route_xp.py docs/40-50-route-2026-11-12.txt` - the plan's XP table (read-only)
- `python weights/score_items.py --help`; `python tooling/gold.py` (quest money per chapter through 41)

## The spec file
Write `<your scratch folder>\<chapter number>.md` (for example `46.md`), plain ASCII Markdown, with these sections:
1. **Header**: file name to create, `[N <lo>-<hi> <Title>]`, the next chapter's `[NX ...]` title as the plan has it, `[GA Alliance]`, the one-sentence description, level on entry and expected level on exit.
2. **Entry state**: where he stands, hearth, quests carried in (ids), profession and training items that fall here.
3. **Travel and hearth**: in and out, flights, boats, roads, binds.
4. **Route**: the steps in play order, grouped into legs. For every quest step: action (accept / objective / turn in), quest id and exact title, XP and money, NPC or object id + name + `x,y Zone`, objective with counts and mob / object ids + location + mob levels, drop rate and kill budget where rule 12 needs one, prerequisite, label (plain / `[O]` + reason / GROUP n / conditional / dungeon label). For non-quest steps: trainer (`[T]`) with the row and prices, vendor (`[V]`) with price, profession gate, class step (`[A Shaman]`), note (`[OC]`).
5. **Gear calls**.
6. **Out**: the zone's quests that are out, one line each with the rule (copy the reason from `_decisions.tsv`; do not re-litigate).
7. **End check**: what the log should hold at the chapter's end; carried out.
8. **Totals**: required quest count, required XP, optional XP, quest money. They must equal the plan's XP table row for your chapter, or the difference is explained under Deviations.
9. **Unverified / in-game test list**, **Needs pull** (what only a Wowhead page could settle) and **Unsure**.
10. **Deviations from the route plan**: every place the spec differs from `docs/40-50-plan-2026-11-12.md`, with the data that forced it.

If the Write tool refuses the spec file, write it with a short Python script instead and say so.

## Report back (text, this exact shape, at most 50 lines; do not paste the spec)
```
CHAPTER <n> <title> | levels a-b | file <spec path>
HUB/HEARTH/TRAVEL: ...
REQUIRED (n, XP total, money): id Title XP; ...
OPTIONAL / CONDITIONAL: id Title XP - label, reason / budget; ...
GEAR: quest id -> pick (score) over runner-up (score), replaces X; ...
TRAINERS/VENDORS/PROFESSIONS: ...
CARRIED IN: ... | CARRIED OUT: ...
DEVIATIONS FROM THE ROUTE PLAN: ...
UNVERIFIED / TEST LIST: ...
NEEDS PULL: ...
UNSURE: ...
VERIFIED: what you checked against which file
```

## Added 13 Nov after the first wave (this section wins where it differs from the text above)
The first four drafts (chapters 42-45 of the old cut) showed the 12 Nov plan overstated its quest XP, and the plan was revised the same day. `docs/40-50-plan-2026-11-12.md` is now the revised plan: read its "Revision of 13 Nov" section and answers 9-11 as well. Chapter numbers, titles and quest lists changed; an older draft or note that disagrees with the plan document is out of date.

- **QuestieDB is thin on Forever-only quests** (ids above about 78000): row [9] (objectives), rows [11] / [12] (prerequisites) and the giver are often empty although the quest has them. For every such quest in your chapter: read the objective from the quest text (row [7]) and from `python tooling/qdetail.py`; find the item's droppers in `tooling/qdb/item.json` rows [1] / [2] / [3], then its rate in `data/drop_rates.json` or, when absent, on `nether.wowhead.com/forever/tooltip/item/<id>` ("Dropped by", "Drop Chance"); read giver, ender and series in `data/wowhead_quest_links.json` (start / end: n = npc, o = object, i = item). If a required quest then fails rule 12 or 13, it goes under Deviations with the numbers; you do not drop it yourself.
- **Wowhead's series is an offer gate in the plan.** A quest that follows an out, optional or conditional quest in its series is conditional: written as an `[O]` line "if <giver> offers it", never counted. Keep that label; do not promote such a quest to plain because QuestieDB shows no prerequisite.
- **Raw page pulls you may read** (tab-separated: kind, id, JSON): `data/browser/r2_pages_2026-11-12.tsv`, `r2_pages2_2026-11-12.tsv`, `r2_pages3_2026-11-13.tsv` (QUEST, ITEM, NPC, ZNPC rows: quick facts, series, drop tables, NPC classification and maps). Many Forever NPC pages carry a classification but no level: say "level not in the data", do not estimate one as fact.
- **Prerequisite order across chapters** is checked by `python tooling/route_xp.py docs/40-50-route-2026-11-12.txt` (it must print no "prerequisite not met" line). Inside your chapter you check it by hand: every pickup after its prerequisite's hand-in, and the giver really stands where your leg is (To The Hinterlands is given in Stormwind, not at Aerie Peak).
- **The route runs under its level checks.** On required quest XP the plan enters several chapters a level or more below the level they want (the XP table's entry column). The chapter still opens with its level-check line; order the legs by mob level, lowest first, and name the quests to leave for last or to skip when under. Do not add quests to close the gap.
- **Drafts of the first wave**: `Claude outputs/40-50-specs-2026-11-13/42-draft.md` to `45-draft.md`. They were written against the old chapter cut. Your prompt says whether one applies to you; facts in a draft are re-checked against the data before they are reused, like any other prose.
- **Things found in the first wave**: Sergeant Riftan (258023) stands at the Twilight's Shroud, Riverglades 30.7,49.1, not at Farholde Keep. What We Lost 94829 and All That's Left 94858 are out (Farmers' Mementos 7.26%). The Big Payback 95326 is out (29.29%) and All's Well That Ends Well 95327 is conditional behind it. Forbidden Knowledge 737 is out and the Badlands trip is dropped. The Black Box 708 has no item source. Zul'Farrak sits behind the Hinterlands chain (2988 > 2989 > 2990 > 2991) because Nekrum's Medallion needs it.
- **Carries between chapters**: the neighbouring specs are written at the same time as yours and cannot be read. State every quest, item and bind you assume on entry and leave on exit, with ids, so the main session can reconcile them.
- The working tree is clean except for two untracked files of Braedyn's under `docs/`; leave them alone. If `git status` shows anything else changed, say so in your report and carry on reading.

## Added 13 Nov, evening: second revision of the plan (this section wins over everything above)
The plan was revised a second time on 13 Nov and Braedyn approved the result, including a **new chapter order**. `docs/40-50-plan-2026-11-12.md` is current: read its "Second revision of 13 Nov" section and answers 12-15 before anything else. Chapter numbers 49-57 changed; any older text (this brief's earlier sections, a draft) that uses another number or another quest list is out of date.

- **Chapter list now**: 42 Riverglades pickups, 43 Krol'dok Stronghold, 44 Stormwind / the Temple door / Aerie Peak, 45 Booty Bay, 46 Tanaris I, 47 Feralas I, 48 The Hinterlands, 49 Nethergarde and the Cape of Stranglethorn, 50 Feralas II, 51 Zul'Farrak, 52 the eastern trip (Tabetha, Nethergarde, the Dalaran crater, the Searing Gorge, the Explorers' League pickups), 53 Tanaris II and Uldum, 54 Maraudon, 55 Darnassus and Azshara, 56 Un'Goro Crater, 57 the closing Ironforge stop.
- **A quest is listed in the chapter that hands it in.** A chapter's Required list can therefore hold a quest whose pickup or objective lies in an earlier chapter, and your chapter can hold pickups and objectives of quests counted later. The plan's chapter note names the main carries; you find the rest: for every quest of the neighbouring chapters' lists, check whether its giver, an objective or its ender stands on your route (quest rows [1], [2], [9]; `python tooling/route_xp.py docs/40-50-route-2026-11-12.txt` prints no place fault for the plan as it stands). State every carry in and out with ids.
- **Required levels are hard gates.** The route file's table shows the predicted level on entry; `route_xp.py` ends with the level "with required levels enforced". A quest cannot be accepted under its required level (quest row [3], Wowhead reqlevel in `data/zone_*.json`): order the chapter so a quest's pickup comes when the level is reached, lowest required level first, and say in the level-check line what he does when he is under (the conditional quests of the chapter first; otherwise which quests wait). Never plan a pickup under its required level.
- **Fill quests** (answer 12) are required steps with a kill budget on the kill line; their reasons in `overrides_r2.tsv` start with "fill".
- **Conditional lines**: the OOX robot quests (beacons at 0.34-0.58% per kill), Ship Schedules, Voodoo Dues, Message in a Bottle, the Wowhead-series cases. Written as `[O]` "if ..." lines, never counted, with the `[QS]` abandon where a pickup may be left hanging (rule 9).
- **Carried to round 3** (picked up where that costs nothing, never handed in this round; the end Check names them): Cortello's Riddle (scroll on the Bloodsail ship, chapter 49), Seed of Life (Maraudon), It's a Secret to Everybody's last part (Un'Goro), Into The Temple of Atal'Hakkar, Return to the Hinterlands. Not picked up at all in round 2: Whiskey Slim's Lost Grog, The Sunken Temple, The Stone Circle, Repurposed Totems, Beneath Nordrassil, the Sprite Darter chain after Doling Justice's Darnassus hand-in.
- **Drafts**: `42-draft2.md` to `48-draft2.md` in `Claude outputs/40-50-specs-2026-11-13/` are the second wave's specs, written against the first revision. Your prompt says whether one applies to you. Their facts are re-checked before reuse.
- Drop rates added 13 Nov are in `data/drop_rates.json` (items 8705, 8704, 8623, 9276, 9250).
