# Brief: write one chapter of the 30-60 guide from its spec (round B, 11 Nov 2026)

You are a subagent working for the main session on Braedyn's WoW Forever levelling guide (Dwarf Shaman, 2H Enhancement, Alliance; a Guidelime addon). Repo: `C:\Users\Braedyn\Documents\WoW Forever Atlas`. Braedyn approved the plan and the chapter specs; you write **one chapter file** exactly as its spec lays it out. If anything is unclear, blocked or looks wrong, do not guess and do not widen scope: write what is certain, and report the rest.

## Hard limits
- The only file you create or edit is your chapter: `guide\Guidelime_ForeverShaman\<file>.lua` (name in your prompt and in TITLES.md). No other guide file, no TOC, no data file, no `lessons.md`, no `CLAUDE.md`, no docs, no git command that changes anything (no add, commit, stash, checkout, restore).
- No browser, no wowhead.com pages. `nether.wowhead.com/forever/tooltip/item/<id>` or `/quest/<id>` from a shell is fine, one request per second.
- Python on this PC wants Windows paths (C:/...). In a Bash heredoc a backslash escape becomes a control byte: write the Lua with the Write tool, never through a heredoc, and make later changes with the Edit tool.
- Keep your scratch files, if any, in a folder of your own under the scratchpad path given in your prompt.

## Read first
1. `docs/RULES.md` - the standing rules; "Writing rules - how the Lua is written" is the part you apply line by line.
2. `lessons.md` (repo root) - the 4 Nov entries on hold tags and ids, and the XP-attribution entry, matter most.
3. `Claude outputs/30-60-specs-2026-11-11/TITLES.md` - **authoritative** for your file name, `[N]`, `[NX]`, start and end points, hearth, carried quests and training stops. It overrides your spec's header.
4. `Claude outputs/30-60-specs-2026-11-11/DECISIONS.md` - Braedyn's rulings (both addenda).
5. Your spec: `Claude outputs/30-60-specs-2026-11-11/<n>.md`. Section 4 is the route in play order; sections 5-9 feed the gear lines, the Check note and your report.
6. Format references: `guide/Guidelime_ForeverShaman/23_Hillsbrad.lua` (an outdoor chapter) and `24_Gnomeregan.lua` or `26_RazorfenKraul.lua` (a dungeon chapter: quest labels, GROUP tags, one-run wording). Copy their header shape, colour codes, label wording and tag vocabulary. **Do not invent a Guidelime tag**: use only tags that already appear in chapters 00-26.
7. `tooling/README.txt` for the checkers.

## How the chapter is written
- Header: `Guidelime.registerGuide([[`, the `[N ...]` line, a `[D Forever Shaman 30-60 (Braedyn)\\<one sentence>]` line, `[GA Alliance]`, then the opening `[OC]` notes: first the **level-check** line from the spec ("this chapter wants level N" and what to do if under it), then carried-in / training notes as chapter 23 does. Class steps carry `[A Shaman]` as in 23-26. Then the `[NX ...]` line where chapters 23-26 put theirs. Footer exactly: `]], "Forever Shaman 30-60")`.
- One step per line. Every step has an explicit `[G x,y Zone]`; NPC and mob steps carry `[TAR<id> Name]`; coordinates sit on quest / action lines, not on standalone text. Zone names must be ones `tooling/guidelib.py` ZONES knows.
- `[QA<id> Exact Title]` on pickups (the title exactly as `tooling/qdb/quest.json` or the Wowhead zone JSON has it); `[QT<id>]` and `[QC<id>]` as chapters 23-26 write them. Every quest picked up is turned in in this chapter, or the Check note names the later chapter that does (TITLES.md "Carried quests"), or it is abandoned with `[QS<id>]` where the spec says so.
- **Hold tags** (4 Nov lesson; check_guide enforces): a step that expects an action at an NPC or object carries the tag that holds it - `[T]` train, `[V]` vendor, `[QC...]` objective, `[CI item,count]` collect, `[SK]`, `[P]` flight point, `[S]` bind, `[H]` hearth, `[F]` fly. Only pure travel steps are goto-only.
- `[O]` = optional step; `[OC]` = a note that completes with the next step. Notes, gear calls, labels, level checks and the Check go in `[OC]`.
- Optional elite quests outside dungeons: `[O]` with `|cFFFF0000GROUP n+|r` and the reason they stay (the item). Dungeon chapters are **required**: their normal quests are plain steps labelled normal, the grind/luck ones `[O]` with the "one run, abandon if it does not drop" wording of 24 / 26.
- Kill lines for collections: "Kill [TAR...] for N <item> [QC...] (~rate - budget ~N kills)" with the rate and budget from the spec.
- **Skipped quests are silent** (rule 4): a quest the spec lists under Out gets no tag and no "don't take X" line. A danger warning about a mob (an elite standing next to an objective) is fine.
- Quoted numbers must check: every "N XP" on a `[QA]` / `[QT]` line is that quest's XP in `data/zone_*.json` (`python tooling/qinfo.py <id>`), attributed to the right quest when a line has several; chain totals say "in all" / "total"; quest money as the zone JSON has it; trainer prices from `tooling/trainer_costs.json` on `[T]` lines; vendor lines as "<Item> (<price> each)" = 4 x the tooltip sell price in `weights/tooltips/2026-11-11.json`.
- Gear lines: `[OC][A Shaman]` lines with the pick, as the spec's section 5 gives them (scores are not printed in 1-30 gear lines unless the reference chapters do; copy their style), conditional wording where the spec is conditional.
- Every id you type (quest, NPC, object, item) is looked up in `tooling/qdb/*.json` in the same step, never typed from the spec on trust: if the spec and the data disagree, the data wins and you report it. Coordinates come from the qdb spawn (`python tooling/loc.py`, `qinfo.py`), except where the spec marks a position "Wowhead map, not in qdb": use the spec's number and list the line in your report (verify's tar check will flag it).
- Unverified facts the spec flags (an entrance, a road, an escort path) are written the way 1-30 writes them: say what is known and that the rest is unverified, briefly. No invented detail.
- ASCII only (no arrows, dashes or quotes outside ASCII), LF line endings, no tab characters.
- Length: comparable to the reference chapters for the same amount of content; do not pad.

## Checks before you report
Run from the repo root and read the lines that name your file:
- `python tooling/check_guide.py` - expect no new finding for your file except cross-chapter ones that cannot resolve until the other new chapters exist (an `[NX]` whose target is not written yet; a carried quest whose `[QT]` or `[QA]` lives in a chapter not written yet). List those separately.
- `python tooling/verify.py --all` - read every line naming your file; fix what is yours (wrong starter / ender, a `[G]` more than 3 units from the spawn, an XP or money number), and list what remains with the reason (for example "Wowhead map position, NPC has no qdb spawn").
- `python -c "d=open(r'<your file>','rb').read(); print(max(d), d.count(b'\r'), d.count(b'\t'))"` - must print a first number under 127 and two zeros.
A hook also runs the checkers after each edit of a `.lua` and prints new findings; treat them the same way.

## Report back (text, this shape)
```
CHAPTER <n> | file <path> | <line count> lines, <step count> steps
WRITTEN: one line per leg (what it covers)
QUESTS: accepted [ids] | turned in [ids] | optional [ids] | abandoned-if [ids] | carried out [ids -> chapter]
DEVIATIONS FROM THE SPEC: each with the data that forced it (or "none")
DATA DISAGREEMENTS: spec said X, <file> says Y (or "none")
CHECKS: check_guide lines for this file | verify lines for this file | byte check
CROSS-CHAPTER (resolve when the others exist): ...
WOWHEAD-MAP POSITIONS USED: line -> id -> x,y
NEW TRAINER / RECIPE / VENDOR LINES (for tooling/skill_gates.json): ...
UNSURE: ...
```
