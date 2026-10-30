# Loot check and data refresh: follow-ups (29 Oct 2026)

Status: **parked, not started.** Braedyn asked on 29 Oct to save this and run it later. Each step below needs his approval before it runs; guide edits are proposed first, as the working agreements require.

## Where things stand (end of 29 Oct)
- `tooling/qdb/` is QuestieDB Forever 1.0.9 (commit 6641516). `weights/tooltips/2026-10-29.json` holds 276 fresh Forever tooltips. `python tooling/check_sources.py` reports everything current except the Wowhead quest XP (21 zones pulled 17-18 Oct, older than client build 1.60.1.70685 of 28 Oct).
- `python tooling/dungeon_loot.py` writes the report-only loot check; the first run is `Claude outputs/dungeon-loot-2026-10-29.md`.
- Forever item stats changed between the 24 Sep scrape and 29 Oct for many items (Rockslicer +10 to +7 Str; Durgen's Crescent Axe +2 Str +1 Agi +1 Spi to +4 Str; Golemguard Chest, Golemheart Stave and Ironforge Greathammer lost stats). The guide's gear calls were scored on the old numbers.
- **Run `python tooling/check_sources.py` first.** If anything reads STALE by the time this is picked up, refresh it before acting (global fresh-data rule).

## Drops the 29 Oct report found that the guide doesn't mention
Rates are Wowhead "Drop Chance" figures where the tooltip carries one; otherwise unknown.
- Totemic Leather Helm (req 25): bosses in Blackfathom, the Stockade and Razorfen Kraul. The guide names no head item.
- Deadmines: Goblin Hammer (1H mace, Gilnid, ~1.3%); Blackened Defias Leggings and Stonemason Trousers (~5.7%), both above the legs the guide names.
- Razorfen Kraul: Thornweaver Drape (Roogug, ~2.7%).
- Gnomeregan: Electrocutioner Lagnut (ring, ~31.8%).
- Blackfathom 1H weapons (Axe of the Enforcer, Doomspike, Grimclaw, Crested Scepter) are trash drops and one-handers; they won't replace the 2H.

## Steps

### 1. Fill the loot blind spots (browser)
- QuestieDB 1.0.9 has no spawns for 3,825 creatures, including Hall of Thanes bosses Magmatus (261316) and Faldrim Anvilmar (261306), so their drops are invisible to the report. Ruins of Lordaeron (16611) and Excavation Site (16732) have no creatures at all.
- Pull these dungeons' loot from Wowhead's dungeon/NPC pages in the browser (the `tooling/lw/` and `wh_zone_listview.js` workflow; ~14 pages before CloudFront throttles). No shell scraping of wowhead.com.
- Feed the result to `dungeon_loot.py` as an extra NPC/drop input, so the report covers all eight dungeon chapters.

### 2. Drop the obsolete mace term from scoring
- `docs/forever-enh-stat-weights.md` marks the Dwarf mace term obsolete since 17 Oct (weapon specializations removed; Mace Spec became Earth Fury). `weights/score_items.py` and `tooling/dungeon_loot.py` still add `mace_bonus` 7.
- Set it to 0 in both, rerun `score_items.py` and `dungeon_loot.py`, note the date in the weights README.
- Chapter 07 line 95 still says "a mace for the Dwarf crit"; that text goes into step 5's proposals.

### 3. Tighten the report
- Hide drops whose required level is more than 5 above the chapter's top level (Gnomeregan lists Falcon's Hook req 39 and Ranger Shoulders req 37).
- Compare weapons against the 2H the guide has him using at that point, not against 1H items.
- Baseline only from items the guide actually recommends, not ones it names to pass on (today Corsair's Overshirt, a cloth chest marked "pass", is the chest baseline).
- Date the 24 Sep fallback tooltips as 2026-09-24 in the provenance line, not the file's modified time.

### 4. Audit the QuestieDB 1.0.9 checker findings (chapters 05, 06, 11)
`check_guide.py` went from 0 to 17 flow problems; `verify.py` has one new finding. For each, decide whether the guide or Questie is wrong, then propose lines.
- 05 Westfall line 22: The State of the Mines (92745) now needs Testing the Wells (92742) and Murloc Gills (92744) turned in first; Moonbrook Espionage (92747) and Explosive Consultation (92748) follow from it.
- 05 Westfall line 59: Harvesting the Harvesters (92911) needs 92910, a quest with the same name.
- 05 Westfall line 80: Odd Child `[G41.2,79.0]` is 6.4 units from the nearest 1.0.9 spawn at 42.8,72.8.
- 06 Redridge line 19: Alther's Mill (98386) needs The Everstill Bridge (89).
- 06 Redridge line 66: Shadow Magic (115) and Tharil'zun (19) need Blackrock Blockade (98387).
- 11 Darkshore line 36: Holy Diver (87760) needs nine beached-turtle/creature quests (4722-4733) all turned in. This looks like a Questie modelling error ("all of" instead of "one of"); check in game, put it on the test list.
- Findings Braedyn accepts go into the baseline with `verify.py --update-baseline`; the rest become guide edits.

### 5. Rescore every gear call on fresh stats, then propose guide edits
- Pull tooltips for every item named on a `Gear:` or `Loot:` line that isn't in today's cache (`fetch_tooltips.py`), rescore with the step-2 weights, and list each call whose verdict flips or whose quoted stats are wrong (e.g. chapter 07's Rockslicer "+10 Str").
- Add the step-1/3 dungeon finds where they beat the expected gear.
- Show Braedyn the proposed lines; after approval, an Opus subagent edits, then `check_guide.py`, `verify.py`, zip rebuild and TOC bump, as the working agreements say.

## Verification
- `check_sources.py`: no STALE rows besides any accepted ones.
- `dungeon_loot.py`: every dungeon chapter has creatures; Hall of Thanes shows Magmatus's and Faldrim's drops; no item above the level cap.
- `check_guide.py` back to 0 flow problems plus the 7 cosmetic; `verify.py` clean against the updated baseline.
- In-game test list (current audit doc) gains: Holy Diver prerequisites, Odd Child's position, and any drop or stat taken only from Wowhead.
