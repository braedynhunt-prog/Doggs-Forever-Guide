# Forever game-data plan - review, wider data pool and the scope to build (29 Oct 2026)

Status: **reviewed, not started.** Braedyn approved the direction on 29 Oct and parked it for later. The original proposal is `C:\Users\Braedyn\Downloads\forever-db-plan.md`; this doc replaces it. Every claim below was checked against the repo (`tooling/README.txt`, `guidelib.py`, `check_guide.py`, `verify.py`, `qdb/*.json`, `data/zone_*.json`, `tooling/lw/*`, `probe/`, the 27 and 28 Oct audits) or against a live fetch on 29 Oct 2026. Launch is 4 Nov.

## Verdict
Worth doing in part, not as written, and the data pool can be widened cheaply. The original plan was drafted from the claude.ai notes and does not know what the 28 Oct session built; its central mechanism (scripted Wowhead drop-rate fetching) does not work. But the client tables for the Forever build are downloadable as CSV from wago.tools, a community SQLite build of the plan's phase 1 is published daily, and the XP-per-level table is settled. Build: a QuestieDB refresh, a client-table fetcher, a quest-XP simulator with sourced constants, and a rates file with a `verify.py` module. Drop: our own SQLite, the MCP server, VMaNGOS, the daily fetcher.

## Problems with the original plan

1. **Phase 2 (`fetch_rates.py`) cannot run as a script.** `nether.wowhead.com/forever/tooltip/item/723` (Goretusk Liver) and `/3685` (Raptor Egg) return no "Dropped by" or "Drop Chance" text; the endpoint carries a rate only for single-dropper items (the 27 Oct audit noted this). `www.wowhead.com/forever/npc=454` returns HTTP 403 from a shell. NPC drop listviews are reachable only through the browser-console workflow (`wh_zone_listview.js`, the `tooling/lw/` pulls), which CloudFront throttles after ~14 pages. "Daily for the first week" is a manual browser job. Phases 3 and 4's rule-3 arithmetic therefore has no scripted rate source.

2. **It does not know about the 28 Oct verification layer.** `verify.py` already does most of phase 4: `questnpc` checks every `[QA]`/`[QT]` TAR against the DB starter/finisher, `tar` checks every `[G]` against DB spawns at 3 map units, `gates` checks skill prerequisites; `check_guide.py` checks required level, prerequisites and flow; `guidelib.py` is the shared data layer. "Fold `tarcheck.py` into `check_guide.py`" is done. New checks belong in `verify.py` as modules with baselines.

3. **DoggsProbe exists and already logs what phase 7 wants to add.** `probe/DoggsProbe/Items.lua` handles `LOOT_OPENED` with `GetLootSourceInfo` (lines 356-372) and `QUEST_TURNED_IN` XP (line 297), plus vendor stock and reward choices; `probe2json.py` converts the SavedVariables. The plan calls it "not built yet" and cites `claude/forever-probe-addon-spec.md` and `claude/wow-forever.md`, neither of which exists on the PC. Phase 7 reduces to an importer plus a day-one install. Never run on Forever: test-list item.

4. **A home-built SQLite duplicates data every tool already reads**, and someone else already publishes the same thing (Sources, item 4). The provenance idea (`source` per row) is right; the container is wrong.

5. **The simulator is the strongest phase; its constants are now mostly sourced** (Sources, items 1-2), but kill counts cannot come from kill lines: 173 kill lines carry a `[TAR]`, only 77 a parseable count. Counts come from quest objectives in `qdb/quest.json` (row [9]) plus kills-needed from the rate. Quest XP is ready: 535 `[QT]` quests on the Dwarf chain, 530 have Wowhead Forever XP (missing 2951, 87760, 97894, 98190, 98313). `docs/20-30-build.md` already did a coarse hand version ("30 at the end of chapter 18 on quest XP alone"); the simulator's value is per-step placement in 1-20, the missing-XP fallback, and a ranked XP list for 30-40.

6. **Phase 3 (VMaNGOS) is redundant.** The 27 Oct audit applied classicdb.ch rates to all 148 collection quests on the route; the community `forever.db` carries the same cmangos chances with a `classicdb` label.

7. **MCP server: no.** Claude Code runs `python tooling/qinfo.py 22` as cheaply as an MCP call. The gaps ("nearest vendor for item X", "rate for item X") are two CLI functions.

8. **Minor.** Row-index notes mix 1-indexed (RULES) and 0-indexed (README) conventions; use `guidelib.py` accessors. `forever_change` already exists as `envChange.status` on every Wowhead row.

## Sources found on 29 Oct (the wider pool)

1. **XP per level: Classic's table, confirmed.** Wowhead's September "XP requirements reduced" datamine was retracted after Blizzard explained the file read is not the one the game uses; Warcraft Tavern's Forever experience guide lists the Classic values (L1 400 ... L20 23,200 ... L30 47,400 ... L40 90,700; 4,084,700 to 60). This constant moves from "unverified" to "sourced".
   https://www.warcrafttavern.com/forever/guides/experience/ , https://www.wowhead.com/forever/news/experience-requirements-significantly-reduced-in-wow-forever-383038

2. **Kill XP and quest XP rules.** Open-world kill XP: Classic formula (45 + 5 x mob level, level-difference brackets, grey = 0), with Forever paying **4-20% less for lower-level mobs** (community measurement by a Reddit user; a Blizzard senior designer confirmed it is intentional; no official formula). Dungeon mob XP was cut hard before beta, then raised ~20% on 8 Oct; dungeon quest bonus XP halved on 1 Oct; party XP now uses each player's own level (8 Oct). Our zone XP pulls are dated 17-18 Oct, after both dungeon changes. Low-level quest reduction: 100% to quest level + 5, then 80/60/40/20/10% (Classic rule, used by Polestar for Forever).
   https://www.icy-veins.com/wow-forever/news/nerfed-experience-gains-from-low-level-mobs-in-wow-forever/ , https://us.forums.blizzard.com/en/wow/t/wow-forever-beta-development-notes/2360696/5 , https://www.bluetracker.gg/wow/topic/eu-en/631316-wow-forever-beta-development-notes-updated-26-october/

3. **Forever client tables on wago.tools, fetchable from a shell.** Product `wowf`, latest build 1.60.1.70685 (28 Oct). `https://wago.tools/db2/<Table>/csv?build=1.60.1.70685` returned CSV on 29 Oct for `QuestXP` (quest XP by quest level x difficulty tier, 100 rows), `SkillLineAbility` (7,853 rows: per-recipe yellow/grey thresholds in `TrivialSkillLineRankLow/High`), `ItemSparse`, `Creature` (names, classification; mob levels are server-side). Use: `QuestXP` as the fallback for the 5 quests without Wowhead XP and for 30-40 planning; `SkillLineAbility` for the recipe colours the audits list as unverified. Caveat: the client values look like post-vanilla tuning, not Classic (Curiously Tasty Omelet yellow 165 / grey 205 vs Classic 150/190; Longjaw Mud Snapper 45/85 vs Classic 50/90; Heavy Linen and Wool bandages match Classic). Record them as "client table, build N" and keep the in-game colour checks on the test list.
   https://wago.tools/api/builds (product list), https://wago.tools/db2/QuestXP/csv?build=1.60.1.70685

4. **`salty-max/wow-data` publishes `forever.db` daily (MIT).** Downloaded and inspected 29 Oct (release `db-dd3d5b7b2d43`, built 29 Oct 20:44, 325 MB SQLite, 91 MB gz). Pins: `wowf` 1.60.1.70685, QuestieDB commit of 29 Oct, cmangos classic-db. Tables: creature (levels, rank, loot ids), spawn, item, loot (with `chance` from `classicdb` for Classic items, e.g. Goretusk Liver 32-38% from the four goretusks; Forever items like Pristine Leather 249427 have `questie` rows with no chance), vendor, trainer_spell, recipe_source, quest/objective/prereq/reward, plus client tables (`client_SkillLineAbility`, `client_QuestV2`, `client_QuestInfo`, `client_TaxiNodes`; no `QuestXP`). Every row carries `source`. This is the original plan's phase 1, done. **No quest XP.** Use it as a read-only sidecar for Classic loot chances and vendors instead of building our own; treat it as untrusted third-party data and keep `qdb/` as the checked source.
   https://github.com/salty-max/wow-data , https://github.com/salty-max/wow-data/releases

5. **Our QuestieDB is three releases behind.** `tooling/qdb` is Forever 1.0.6 (bundle of 12 Oct). Questie published 1.0.7 (23 Oct), 1.0.8 and 1.0.9 (26 Oct); the `Questie/QuestieDB` repo had commits on 29 Oct ("Quest fixes"). The pandaquest import of 1.0.8 counts 5,232 quests vs our 5,226. Refresh = `questiedb_baked.py` on the 1.0.9 bundle TOC, then rerun both checkers and diff the baselines.
   https://github.com/Questie/Questie/releases (bundle/v12.3.1+v1.0.9, 26 Oct 2026)

6. **Crowdsourced Forever drop observations exist but are too thin to use today.** `wowdb.wiki` (World Recorder addon 1.7.7): item pages list dropped-by NPCs but no counts or rates, no export. `warcraftforever.games/npcs`: 2,104 NPCs from 350 sessions; Young Goretusk "seen once, no drops". `zugzugdb.com` (build 70532, 22 Oct): NPC pages exist, CSV export 404, rate-limited (HTTP 429). Verdict: Wowhead Forever listviews via the browser stay the only sampled Forever rates. Re-check wowdb.wiki one week after launch.
   https://wowdb.wiki/ , https://github.com/azeroth-db/world-recorder , https://warcraftforever.games/npcs , https://zugzugdb.com/

7. **Polestar (fitzforge, GPL-3) is a full Forever route simulator; use its calibrated priors, not its code.** Its model doc states: Classic XP table; quest XP from `QuestXP` at quest level x tier (breadcrumb low / normal middle / chain-end, escort, group high), recorded XP overrides; kill XP 45 + 5 x level with ~5% per level of difference; unknown drop rate counted at 30%, quest-only items 60%; incidental kill XP prior 4.3% +/- 3.8% (fitted 12 Oct); run speed 7 yd/s; quest log 40; NPC ranks corrected from Wowhead Forever (QuestieDB gives Forever NPCs rank 0; 22 Era NPCs reclassified, e.g. Bruuz elite). The last point matters for our group/elite labels.
   https://github.com/fitzforge/polestar (docs/SIMULATION.md)

8. **Forever addon environment (for DoggsProbe).** `charles-hood/forever-addon-kit` (24 Sep, build 69893): SavedVariables are written on exit but never read back (Blizzard bug), combat log restricted, player/target health secret in combat, Retail codebase (`WOW_PROJECT_MAINLINE`, interface 16001). DoggsProbe's README already expects the reset; exports still work. Add to the probe instructions: `/reload` before quitting, expect defaults every launch.
   https://github.com/charles-hood/forever-addon-kit

9. **Blizzard beta dev notes (bluetracker, to 27 Oct)** carry loot facts worth grepping during audits: multi-drop fixes (1 and 16 Oct), Storm, Earth and Fire totems now drop more often and from more mobs (8 Oct; the 20-30 build left this quest out as "Horde per Wowhead"), Mother Fang nerfed, Eye of the Tempest multi-drop.

## Scope to build, in order

### A0. Refresh `tooling/qdb` to QuestieDB Forever 1.0.9 (one hour)
Download bundle `Questie-v12.3.1+v1.0.9.zip`, run `python tooling/questiedb_baked.py <QuestieDB_Forever.toc> tooling/qdb`, update `META.json`, rerun `check_guide.py` and `verify.py --all`, diff against the baselines, report new findings for approval. Keep 1.0.6 in `archive/` for comparison.

### A1. `tooling/fetch_client.py` + `tooling/client/<build>/` (half a day)
Fetch `QuestXP`, `SkillLineAbility`, `QuestV2`, `QuestInfo`, `TaxiNodes` CSVs from wago.tools for a pinned build (argument, default 1.60.1.70685); cache under `tooling/client/<build>/`; README section. Add a `colours` check to `skill_gates.json` / `verify.py gates`: each recipe row gains `yellow`/`grey` from `SkillLineAbility` with `source: client <build>`; a cook-to-N / bandage-to-N target above a recipe's grey value is a finding. Mark every value where client differs from Classic for the in-game test list.

### A2. `tooling/simulate_xp.py` (one day)
- Walk the Dwarf chain with `guidelib.chain_files('Dwarf')`, `steps()`, `quest_tags()`, `on_chain()`; XP merge as in `qinfo.py` lines 21-25 plus `guidelib.atlas()`.
- Quest XP at `[QT]` (skip `[O]` unless `--optional`; `[QS]` = 0), reduced by the 100/80/60/40/20/10 rule from the predicted level; quests with no Wowhead XP fall back to `QuestXP[level][tier]` with Polestar's tier rule, flagged.
- Kill XP from `[QC]` kill objectives (count x mob level from `npc.json` row [3]/[4], Classic formula) times a `lowlevel_factor` parameter (default 0.9, range 0.8-0.96, "community measurement"); item objectives use kills = count / rate from `rates.json` (unknown = 30%, quest-only = 60%, flagged); `[XP n]` grind steps raise the level to n; an `incidental` parameter (default 0.043) for untracked kills.
- Output: per-step level and XP; per-chapter XP; `[QA]` whose `reqlevel` exceeds the predicted level; a ranked quest list. Constants in one dict with a `source` string each.
- Check: 20-30 totals reconcile with `docs/20-30-build.md` (quest XP only, optional included).

### B. `tooling/rates.json` + `verify.py` module `rates` (one day)
Seed from the 27 Oct audit tables (`Claude outputs/audit-2026-10-27/drop-rates.md`) and the community `forever.db` `loot.chance` where `source = classicdb`; shape as `tooling/lw/leather_sources_forever.json` (npc, count/outof, source, date). Refresh path is the browser: `wh_npc_listview.js` + `ingest_npc_tsv.py` modelled on the zone pair. The module computes kills = count / rate per `[QC]` item objective, compares with spawn count in the `[G]` zone and rule 3 thresholds, checks any "budget ~N" on the line, warns on Classic-only or missing rates. Baseline for approval.

### C. `tooling/q.py` (CLI only, two hours)
`vendor <itemId>` (item.json vendors, nearest spawn to a `[G]`), `rate <itemId>`, `sidecar <sql>` against the downloaded `forever.db` when present.

### D. After launch
Probe importer (`probe/import_rates.py`: loot counts and `xpGained` per quest into `rates.json` / an XP check); re-check wowdb.wiki for sampled rates; grep the dev notes on each audit.

### Dropped from the original plan
Own SQLite `forever.db` / `build_db.py`; three-tier confidence schema (a `source` string per rates row instead); VMaNGOS; MCP server; fold-tarcheck item (done); `forever_change` table.

## Open decisions for Braedyn
- A0-A2 and B before launch, C and D after? (Recommended.)
- Keep the community `forever.db` as a sidecar (325 MB, untrusted, daily-moving) or only lift its `classicdb` loot chances into `rates.json` once? (Recommended: lift once, cite the release tag.)
- Spend browser time now on the ~20 NPC pages behind the route's collection quests for Forever-beta samples?

## Verification when built
- After A0: `check_guide.py` 0 flow problems + 7 cosmetic; `verify.py` new findings listed and approved before the baseline is updated.
- After A1: every `skill_gates.json` recipe row has client colours; the differences-from-Classic list goes to the current audit doc's test list.
- After A2: totals reconcile with `docs/20-30-build.md`; three chapters spot-checked by hand; the constants and their sources listed in the README section "29 Oct 2026".
- After B: `verify.py --all` shows the `rates` module; findings approved into the baseline.
