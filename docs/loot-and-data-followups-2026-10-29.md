# Loot check and data refresh: follow-ups (29 Oct 2026, revised 1 Nov 2026)

Status: **parked, not started.** Braedyn asked on 29 Oct to save this and run it later. Reviewed 1 Nov 2026 against the repo and the checkers; the review changed the order, shrank the browser step, corrected two factual errors (noted inline) and added a step 0. Each step needs his approval before it runs; guide edits are proposed first, as the working agreements require.

## Where things stand (1 Nov)
- `tooling/qdb/` is QuestieDB Forever 1.0.9 (commit 6641516). `weights/tooltips/2026-10-29.json` holds 276 Forever tooltips.
- `python tooling/check_sources.py` on 1 Nov: questiedb OK (1.0.9); **client STALE** (1.60.1.70685 -> 1.60.1.70707 of 30 Oct); **item_tooltips STALE** (29 Oct cache, newer build); wowhead_xp STALE (21 zones pulled 17-18 Oct). Re-run it when this is picked up and refresh anything STALE first (global fresh-data rule; see step 0).
- `python tooling/dungeon_loot.py` writes the report-only loot check; the first run is `Claude outputs/dungeon-loot-2026-10-29.md`.
- Forever item stats changed between the 24 Sep scrape and 29 Oct for many items (Rockslicer +10 to +7 Str; Durgen's Crescent Axe +2 Str +1 Agi +1 Spi to +4 Str; Golemguard Chest, Golemheart Stave and Ironforge Greathammer lost stats). The guide's gear calls were scored on the old numbers.
- `check_guide.py` is at 24 problems (17 flow + the 7 cosmetic) since the 1.0.9 refresh, so the "0 flow problems" gate fails for every guide edit until step 1 is done.

## Drops the 29 Oct report found that the guide doesn't mention
Rates are Wowhead "Drop Chance" figures where the tooltip carries one; otherwise unknown. Rule 3 applies: none of these becomes a target; see step 5 for how they may be mentioned.
- Deadmines: Blackened Defias Leggings (Overseer/Taskmaster trash, rate unknown) and Stonemason Trousers (~5.7%), both above the legs the guide names. Goblin Hammer (1H mace, Gilnid, ~1.3%) is shield-set only and too rare for a line.
- Razorfen Kraul: Thornweaver Drape (Roogug, ~2.7%): too rare for a line.
- Gnomeregan: Electrocutioner Lagnut (ring, ~31.8%).
- Blackfathom 1H weapons (Axe of the Enforcer, Doomspike, Grimclaw, Crested Scepter) are trash drops and one-handers; shield set at most, never the 2H.
- *Correction (1 Nov):* the 29 Oct version said the guide names no head item and listed Totemic Leather Helm as a gap. Chapters 13 (line 38) and 26 (line 59) already call Defender's Leather Helm first and Totemic second. The report showed "no baseline" only because its matcher looks for `Gear:`/`Loot:` and those lines are headed "Leather helms (req 25 ...)"; fixed in step 3.

## Steps, in order

### 0. Refresh stale data
- Client tables: pull build 1.60.1.70707 (`Item.csv` is read by `dungeon_loot.py`) per the `sources.json` pull steps (5 tables, scripted curl), update `tooling/client/README.txt`, commit.
- Tooltips: re-pull **all** cached ids with `fetch_tooltips.py`, not just missing ones (stats move between builds; 276 ids at one per second is five minutes). Writes `weights/tooltips/<today>.json`.
- Wowhead XP: re-pull in the browser only the zones step 1 edits touch (40 Westfall, 44 Redridge, 148 Darkshore), not all 21.

### 1. Audit the QuestieDB 1.0.9 checker findings (chapters 05, 06, 11) - was step 4
This is the gate for every later guide edit, so it goes first. `verify.py` has one new finding (Odd Child). For each, decide whether the guide or Questie is wrong, then propose lines. What the data already says (1 Nov):
- 05 Westfall line 22: `[QA92745]` The State of the Mines (and 92747 Moonbrook Espionage, 92748 Explosive Consultation) are picked up on line 22, but the prerequisites 92742 Testing the Wells and 92744 Murloc Gills are turned in on line 69. Pure reorder: move the three pickups after line 69.
- 05 Westfall line 59: `[QA92911]`/`[QT92911]` Harvesting the Harvesters share one line; 92910 (same name, same giver 253395, its prerequisite) is nowhere in the guide. Wowhead Forever lists 92910 in Westfall with 800 XP (`data/zone_40.json`). A missing 800 XP quest, not an ordering issue: add `[QA92910]` ... `[QT92910]` before 92911.
- 06 Redridge line 19: `[QA98386]` Alther's Mill is picked up before `[QT89]` The Everstill Bridge (line 62). Reorder to after line 62.
- 06 Redridge lines 66/67: `[QA115]` Shadow Magic and `[QA19]` Tharil'zun on line 66, `[QT98387]` Blackrock Blockade on 67. Swap the two lines.
- 11 Darkshore line 36: Holy Diver (87760) needs all nine beached quests 4722-4733 per Questie (preQuestGroup). The guide only does 4731-4733 (lines 81/90), so a reorder alone does not fix it, and Holy Diver has no Wowhead XP (`zone_148` shows None). Check the Wowhead Forever quest page in the browser (series/requires) before any in-game test; if "all nine" holds, either add the six missing beached quests with their XP or drop Holy Diver (no quest without known XP).
- 05 Westfall line 80: Odd Child `[G41.2,79.0]` is 6.4 units from the nearest 1.0.9 spawn at 42.8,72.8. In-game tarcheck.
- Findings Braedyn accepts go into the baseline with `verify.py --update-baseline` and a regenerated `check_guide_baseline.txt`; the rest become guide edits (Opus subagent, then `check_guide.py`, `verify.py`, zip rebuild, TOC bump).

### 2. Drop the obsolete mace term from scoring
- `docs/forever-enh-stat-weights.md` marks the Dwarf mace term obsolete since 17 Oct (weapon specializations removed; Mace Spec became Earth Fury). The term lives in three places, not two:
  - `weights/score_items.py`: `mace_bonus` 7.0 in both weight dicts (lines 106-107) -> 0, or remove the term from `score()`.
  - `tooling/dungeon_loot.py`: `W20_CENTRAL`/`W20_CONSERVATIVE` -> 0, **and** delete `mace_bonus` from the override tuple in `band_weights()` (line 87), otherwise bands 10/15 re-import the model's value.
  - `weights/enh_weights.py`: `band_scenarios()` has `mace=True` at 10 and 20, which adds +1% crit to the baseline character; set all three to False and make `weights()` emit `mace_bonus` 0 (the formula on line 269 still returns a positive number with the flag off).
- Also `weights/sensitivity.py` ("no mace (axe) baseline" case) and `weights/README.txt` ("mace +7 flat"), with a dated note in the README.
- Chapter 07 line 95 still says "a mace for the Dwarf crit"; that text goes into step 5's proposals.

### 3. Tighten the report
- Baseline from green-highlighted items (`|cff66ff66Name|r`) on Shaman/Dwarf lines, not from `Gear:`/`Loot:` substrings. The guide already uses green for "the call" and leaves "pass" items plain, so this gives "items the guide recommends" in one rule and fixes the Corsair's Overshirt case (a cloth chest marked "pass" is today's chest baseline) and the helm case above.
- Keep the 1H comparison group but label it "shield set, secondary". The guide tracks a shield-set 1H (Cookie's Tenderizer, Smite's Reaver), so 1H rows are valid but low priority; never compare a 1H against the 2H.
- "Mentioned" check: also match the chapter's short form (the helm lines say "Totemic (+13 Sta ...)"), or accept that helm drops show as not mentioned.
- Hide drops whose required level is more than 5 above the chapter's top level (Gnomeregan lists Falcon's Hook req 39 and Ranger Shoulders req 37).
- Read the fallback tooltip date from `sources.json` (`fallback_date`) instead of the file's modified time.
- Weights beyond 20: chapters 13-26 (levels 25-31) are scored with the level-20 band because `enh_weights.py` stops at 20. Add 25 and 30 scenarios (wowsims has the 25/40 base-stat rows the weights doc cites; gear from the chapter-18 set) before step 5, since step 5 proposes edits to those chapters. Record the new bands in the weights doc.

### 4. Fill the loot blind spots - was step 1, shrunk
- *Correction (1 Nov):* the 29 Oct version said the spawnless Hall of Thanes bosses' drops are invisible and that Ruins of Lordaeron (16611) and Excavation Site (16732) have no creatures. Only the zone spawn is missing. Checked in `npc.json`/`item.json`: Magmatus 261316 (Fang of Magmatus, Flamefist Grips, Kindlegem Girdle), Faldrim Anvilmar 261306 (3), Plunder 261311 (3); Ruins of Lordaeron bosses Bjork 256097, Rath'mael 250657, The Abandoned 250631, The Baron 250660, Viktor the Vile 256035, Witherfang 250483 (3-6 drops each); Excavation Site bosses Relic Guardian 260326, Saltspine 260322, Shadetooth 260325 (3-6 each), Highland Horror 260808 (1). 459 of the 3,825 spawnless creatures drop items.
- Fix: give `DUNGEONS` in `dungeon_loot.py` a per-dungeon list of extra creature ids beside the zone id (the chapter's `[TAR]` ids cover Hall of Thanes; chapters 08 and 22 name bosses in `|cffffcc00Boss|r` headings without a TAR, so the list is the ids above, verified against `npc.json`). The report then covers all eight dungeons from data already on disk and under the manifest. No browser needed for bosses.
- Trash in Ruins of Lordaeron and Excavation Site stays unlisted unless wanted: one Wowhead dungeon NPC-listview page per dungeon (2 pages) gives the ids, which resolve through `item.json`. That needs a `wh_npc_listview.js` (only `wh_zone_listview.js` exists), a dated file under `tooling/lw/` and a `sources.json` entry; share the script with the rates plan (`docs/forever-db-plan-2026-10-29.md`, B). No shell scraping of wowhead.com.

### 5. Rescore every gear call on fresh stats, then propose guide edits
- With step 0's tooltips and step 2's weights, rescore every item named on a Shaman/Dwarf gear line; list each call whose verdict flips or whose quoted stats are wrong (e.g. chapter 07's Rockslicer "+10 Str"). Pull any id still missing a tooltip first.
- Dungeon finds from steps 3/4 go in only as "if it drops, roll" lines (rule 3: never a target, never a re-run). A single-dropper item under ~5% (Goblin Hammer 1.3%, Thornweaver Drape 2.7%) gets no line. An unknown-rate trash drop (Blackened Defias Leggings) gets a line only if it beats the green call. 1H items are shield-set notes, not gear calls.
- Show Braedyn the proposed lines; after approval, an Opus subagent edits, then `check_guide.py`, `verify.py`, zip rebuild and TOC bump, as the working agreements say.

## Verification
- `check_sources.py`: no STALE rows besides any accepted ones (wowhead_xp zones not touched by step 1 may stay stale; say so).
- After step 1: `check_guide.py` back to 0 flow problems plus the 7 cosmetic; `verify.py` clean against the updated baseline.
- After step 2: `dungeon_loot.py` provenance line shows mace 0 in every band; `score_items.py` output has no mace term.
- After step 4: every dungeon chapter has creatures; Hall of Thanes shows Magmatus's and Faldrim's drops; Ruins of Lordaeron and Excavation Site show their bosses; no item above the level cap.
- In-game test list (current audit doc) gains: Holy Diver prerequisites (if the Wowhead page does not settle it), Odd Child's position, and any drop or stat taken only from Wowhead.
