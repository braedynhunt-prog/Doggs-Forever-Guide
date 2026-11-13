# Brief: write one chapter of round 2 (levels 42-50) from its spec - 13 Nov 2026

You are a subagent working for the main session on Braedyn's WoW Forever levelling guide (Dwarf Shaman, 2H Enhancement, Alliance; a Guidelime addon). Repo: `C:\Users\Braedyn\Documents\WoW Forever Atlas`. Braedyn approved the route plan and the spec list on 13 Nov; you write **one chapter file** exactly as its spec and its amendment lay it out. If anything is unclear, blocked or looks wrong, do not guess and do not widen scope: write what is certain, and report the rest.

## Hard limits
- The only file you create or edit is your chapter: `guide\Guidelime_ForeverShaman\<file>.lua` (name in your prompt). No other guide file, no TOC, no data file, no `lessons.md`, no `CLAUDE.md`, no docs, no spec, no git command that changes anything (no add, commit, stash, checkout, restore). Other agents are writing the neighbouring chapters at the same time: never open their files for writing.
- Do not run `tooling/tip.py`, `tooling/fetch_tooltips.py`, `tooling/gear_calls.py`, `tooling/dungeon_loot.py` (they write tracked files), nor anything under `Claude outputs/40-50-plan-2026-11-12/`. For an item's stats read `weights/tooltips/2026-11-12.json` (keyed by item name; each entry has "id" and "tooltip") or fetch the nether tooltip yourself into your scratch folder.
- No browser, no wowhead.com pages. `nether.wowhead.com/forever/tooltip/item/<id>` or `/quest/<id>` from a shell is fine, one request per second.
- Python on this PC wants Windows paths (C:/...). In a Bash heredoc a backslash escape becomes a control byte: write the Lua with the Write tool, never through a heredoc, and make later changes with the Edit tool.
- Scratch files, if any, go in the folder named in your prompt.

## Read first
1. `docs/RULES.md` - the standing rules; "Writing rules - how the Lua is written" is the part you apply line by line.
2. `lessons.md` (repo root) - the 4 Nov entries on hold tags and ids, the XP-attribution entry, and the 11 Nov entry on `[CI item,count]` against `[QC id,index]` matter most.
3. `Claude outputs/40-50-specs-2026-11-13/00-spec-list.md` - **authoritative** for your file name, `[N]` title, start and end points, hearth, and for the **amendment** to your chapter ("Amendments the main session applies when the chapters are written": apply the item with your chapter's number; it overrides the spec). Its "Calls for Braedyn" all stand at their defaults (he approved them).
4. Your spec (file named in your prompt). Section 4 is the route in play order; sections 5-9 feed the gear lines, the Check note and your report. Where the spec was written before the plan's second revision, your prompt lists what changed; `docs/40-50-plan-2026-11-12.md` (your chapter's section: Required and Optional / conditional lists) is the final word on which quests are required, conditional or out.
5. Format references: `guide/Guidelime_ForeverShaman/38_RivergladesI.lua` (an outdoor chapter of this group), `39e_Uldaman.lua` (a dungeon chapter: quest labels, one-run wording) and `41_PowderfusePort.lua`. Copy their header shape, colour codes, label wording and tag vocabulary. **Do not invent a Guidelime tag**: use only tags that already appear in chapters 00-41.
6. `tooling/README.txt` for the checkers.

## How the chapter is written
- Header: `Guidelime.registerGuide([[`, the `[N ...]` line from your prompt, a `[D Forever Shaman 30-60 (Braedyn)\\<one sentence>]` line as chapters 38-41 write it, `[GA Alliance]`, then the opening `[OC]` notes: first the **level-check** line (rule 14: "this chapter wants level N" and what to do when under it; the spec gives it), then carried-in / training notes as chapters 38-41 do. Class steps carry `[A Shaman]`. Then the `[NX ...]` line from your prompt, placed where chapters 38-41 put theirs. Footer exactly: `]], "Forever Shaman 30-60")`.
- One step per line. Every step has an explicit `[G x,y Zone]`; NPC and mob steps carry `[TAR<id> Name]`; coordinates sit on quest / action lines, not on standalone text. Zone names must be ones `tooling/guidelib.py` ZONES knows.
- `[QA<id> Exact Title]` on pickups (the title exactly as `tooling/qdb/quest.json` has it; for a quest the DB lacks, the Wowhead zone JSON's); `[QT<id>]` and `[QC<id>]` as chapters 38-41 write them. Every quest picked up is turned in in this chapter, or the Check note names the later chapter that does, or it is abandoned with `[QS<id>]` where the spec says so (rule 9).
- **Hold tags** (check_guide enforces): a step that expects an action at an NPC or object carries the tag that holds it - `[T]` train, `[V]` vendor, `[QC...]` objective, `[CI item,count]` collect, `[SK]`, `[P]` flight point, `[S]` bind, `[H]` hearth, `[F]` fly. Only pure travel steps are goto-only. A step that collects one of several items of a quest is held with `[CI item,count]`, not `[QC id,index]`.
- `[O]` = optional step; `[OC]` = a note that completes with the next step. Notes, gear calls, labels, level checks, tier gates and the Check go in `[OC]`.
- **Conditional quests** (the plan's "conditional": "if he offers it", "if the beacon drops", "only if you are 45", "only at skill 225") are `[O]` lines whose text states the condition first. They are never counted and never block: if a conditional pickup may be left hanging, the chapter (or the Check) says to abandon it with `[QS<id>]`.
- **Fill quests and collections**: kill lines read "Kill [TAR...] for N <item> [QC...] (~rate - budget ~N kills)" with the rate and budget from the spec.
- **Dungeon chapters are required**: normal quests are plain steps labelled normal; a boss-item quest says "one kill only; Wowhead reads N% over all kills" and what to do if it does not drop (abandon with `[QS]`, never a re-run); grind / luck quests are `[O]` with the "one run, abandon if short" wording of 39e.
- **Skipped quests are silent** (rule 4): a quest the spec lists under Out gets no tag and no "don't take X" line. A danger warning about a mob (an elite beside an objective, a patrol) is fine and wanted.
- **Required levels**: never place a pickup before the level its quest needs. Where the spec says a leg waits for a level, write the gate as an `[OC]` line in front of that leg's first pickup.
- Quoted numbers must check: every "N XP" on a `[QA]` / `[QT]` line is that quest's XP in `data/zone_*.json` (`python tooling/qinfo.py <id>`), attributed to the right quest when a line has several; quest money as the zone JSON has it; trainer prices from `tooling/trainer_costs.json` on `[T]` lines; vendor lines as "<Item> (<price> each)" = 4 x the tooltip sell price.
- Gear lines: `[OC][A Shaman]` lines with the pick as the spec's section 5 gives it, in the style of chapters 38-41, conditional wording where the spec is conditional.
- Every id you type (quest, NPC, object, item) is looked up in `tooling/qdb/*.json` in the same step, never typed from the spec on trust: if the spec and the data disagree, the data wins and you report it. Coordinates come from the qdb spawn (`python tooling/loc.py`, `qinfo.py`), except where the spec marks a position as not in the data: write what the spec says about it (a hint marked unverified, or no `[G]` where the amendment says so) and list the line in your report.
- Unverified facts the spec flags (a road, a boat, an entrance, an escort path) are written the way 38-41 write them: say what is known and that the rest is unverified, briefly. No invented detail.
- ASCII only, LF line endings, no tab characters. Length comparable to chapters 38-41 for the same amount of content; do not pad.

## Checks before you report
Run from the repo root and read only the lines that name your file (the neighbouring chapters are being written at the same time and will show unfinished state):
- `python tooling/check_guide.py` - expect no finding for your file except cross-chapter ones that cannot resolve until the other new chapters exist (an `[NX]` whose target is not written yet; a carried quest whose `[QA]` or `[QT]` lives in another new chapter). List those separately.
- `python tooling/verify.py --all` - read every line naming your file; fix what is yours (wrong starter / ender, a `[G]` more than 3 units from the spawn, an XP or money number) and list what remains with the reason.
- `python -c "d=open(r'<your file>','rb').read(); print(max(d), d.count(b'\r'), d.count(b'\t'))"` - must print a first number under 127 and two zeros.

## Report back (text, this shape, at most 40 lines)
```
CHAPTER <n> | file <path> | <line count> lines, <step count> steps
WRITTEN: one line per leg (what it covers)
QUESTS: accepted [ids] | turned in [ids] | optional / conditional [ids] | abandoned-if [ids] | carried out [ids -> chapter]
AMENDMENT APPLIED: what you changed against the spec for the spec list's amendment and the prompt's list
DEVIATIONS FROM THE SPEC: each with the data that forced it (or "none")
DATA DISAGREEMENTS: spec said X, <file> says Y (or "none")
CHECKS: check_guide lines for this file | verify lines for this file | byte check
CROSS-CHAPTER (resolve when the others exist): ...
POSITIONS NOT FROM QDB: line -> id -> x,y
NEW TRAINER / RECIPE / VENDOR LINES (for tooling/skill_gates.json): ...
UNSURE: ...
```
