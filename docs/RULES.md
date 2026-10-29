# Forever Alliance guide — standing rules (read before editing `Guidelime_ForeverAlliance`)

These are Braedyn's rules for the guide, collected 27 Oct 2026 from the README, the build notes, the audits and the conversations that set them. Dates mark when a rule was set. If a rule here conflicts with an older note elsewhere, this file wins. Braedyn: correct anything that is wrong or missing.

## What the guide is
- A Guidelime addon (`C:\Users\Braedyn\Documents\WoW Forever Atlas\guide\Guidelime_ForeverAlliance\`, zip beside it) for **Braedyn's Dwarf Shaman (2H Enhancement) on WoW Forever, Alliance**, levels 1-30 today, 30-40 later (built after launch from live data, not the datamined DB).
- **Efficient, not a speedrun** (27 Oct). A 10-minute detour that pays back over the next levels (a lasting food buff, a profession gate) is worth it. XP per hour still matters: no quest goes in without knowing its XP ("how do we know what quests are worth it otherwise?", 17 Oct).
- **Human and Hunter lines are no longer maintained** (27 Oct, brother not playing). They stay in the files, hidden by `[GA Human]` / `[A Hunter]`; don't spend effort on them, don't delete them without asking.
- Project docs hold notes only; code, data and the addon live on his PC under `WoW Forever Atlas\` (24 Sep).

## Content rules — what goes in
1. **Every new-to-Forever Alliance zone, dungeon and hub reachable at the route's level** is quested through (27 Oct). Known exceptions, decided: Zephras Isle (Skyborne start; skip), City of Dalaran dungeon (30-40 guide).
2. **Every Alliance dungeon in the bracket, with its quests**, as run-it-now chapters/steps marked optional and labelled **normal / grind** per quest up front (18 Oct; the label rule dates from Deviate Hides in the Era project). Group quests marked `|cFFFF0000GROUP n+|r`, optional. **Rule 3 overrides this one**: a dungeon quest whose item is a low or unknown drop is still picked up (it costs nothing on the way in) but is labelled **grind/luck**, done once, and **the dungeon is never re-run for it** — if the item doesn't drop on the run, the step says to abandon the quest. No "farm the first room for X" steps. (Precedents: Mortality Wanes in RFK at ~10%, the Baron's head, Charlga's note.)
3. **No rare-drop farms** (27 Oct). A required item drop is dropped from the guide (or made `[O]`) when it needs more than ~2× the kills the route already does there, or more than ~25 kills on fewer than ~20 spawns. Classic collections in the 20-30-kill range stay but carry a kill budget on the kill line ("~36% drop - budget ~15"). Forever items with no known rate get a budget too. Boss drops that look low on Wowhead get a "one kill only, then abandon" note. Inside dungeons this means one run, never a re-run (see rule 2).
4. **Skipped quests are silent** (27 Oct). No "don't take X" text; a quest that isn't in the guide simply has no tags. Reasons live in the audit docs, not the Lua.
5. **Cooking + Fishing are part of the route** (27 Oct). The food thread is Roasted Boar Meat → **Longjaw Mud Snapper (+10 AP, 5+)** → **Mithril Head Trout (+20 AP, 25+)**; every other recipe is skill-up filler, taken when free. Recipe vendors, trainers (Journeyman/Expert) and "cook to N" / "fish to N" stops are placed so he has the skill and level **before** he reaches the recipe. Skill targets: Cooking 50 by 12, 80 by 16, 125 by 24, 175 by ~30; Fishing 25 by 12, 50 by 15, 100 by 22, 130+ by 28. Fishing stops are `[O]`, recipe/trainer gates are plain steps. Carry this thread into every later bracket (both will be levelled for endgame anyway).
6. **Full gear guidance** for 2H Enhancement at every reward choice and dungeon (24 Sep): weapon dps > Str > Int ≈ Spirit > Agi > spell damage; leather until mail at 40. Stat weights: `docs/forever-enh-stat-weights.md`. Shaman gear lines are `[A Shaman]`.
7. **Professions:** Skinning + Mining, plus the secondaries First Aid + Cooking + Fishing; Leatherworking decision at 25 by Pristine Leather count (27 Oct). Camping 101 quests for all five. Journeyman/Expert steps for all of them at the Ironforge passes (Expert Fishing is Booty Bay — 30-40 guide).
8. **Shaman class quests** (Call of Earth / Fire / Water / Air) are threaded through the chapters at the right levels; trainer stops at every band (shaman trainers exist only in Dun Morogh and Ironforge).
9. **Every quest picked up is turned in or explicitly `[QS]`-abandoned**, or not picked up at all (10 Sep, Era project). `check_guide.py` enforces it.
10. **Launch-crowd layer** (25 Oct): at camped named mobs/objects, invite the people there; 2-minute rule then move on; catch-up lines say where the route returns.

## Writing rules — how the Lua is written
- Chapter titles are level ranges (`[N 11-15 Loch Modan]`), chained with `[NX]`; `[GA Dwarf]`/`[GA Alliance]` on chapters, `[A Shaman]` on class steps.
- **Every quest tag carries its title** (`[QA96390 Nip 'Em in the Bud]`) so new Forever quests display by name. **Every step has an explicit `[G x,y Zone]`**; NPC and mob steps carry `[TAR<id> Name]`.
- **Coordinates are Forever map space.** Stormwind and Redridge differ from Classic (`tooling\coord_transform_forever.json`: SW x' = 0.77367x + 19.68, y' = 0.77383y + 24.43; Redridge x' = x − 5.09). Forever DB spawns are already correct; Classic Wowhead numbers are not.
- `[O]` = optional step; `[OC]` = note that completes with the next step and never holds the cursor. Notes, gear calls and labels go in `[OC]`; coordinates go on quest lines, not on standalone text lines.
- **Chapter step counts matter**: Guidelime stores manual ticks by step index per chapter and wipes them when the count changes (25 Sep). Mid-chapter edits should add/remove a line deliberately so the reset is clean. (Moot until he starts playing; after launch, edit chapters he has finished or not started.)
- ASCII only in the Lua (WoW fonts drop arrows and the like); LF line endings; TOC version = date of the last edit, with a one-line changelog in `## Notes`.
- Kill lines for collections: "Kill [TAR...] for N <item> [QC...] (~rate - budget ~N kills)".
- Don't invent Guidelime tags. `[CI itemId,count]` and `[UI itemId]` are in use but unverified on the Forever build (18 Oct).

## Process rules — how to edit
- **Stage the current files from the PC first**; another session may have edited them (27 Oct had two sessions editing at once). Commit with mtime guards; rebuild the zip after.
- **Verify every NPC, vendor, coordinate and skill requirement against the data**, never from a subagent's prose: `tooling\qdb\{quest,npc,object,item}.json` (QuestieDB Forever; item row 14 = vendors, row 2 = npc drops, row 10 = req level; npc row 7 = spawns by zone; no XP field), `data\zone_*.json` (Wowhead XP), `nether.wowhead.com/forever/tooltip/item/<id>` (works from a shell; carries recipe skill, food buff, drop chance), classicdb.ch for Classic drop rates (decimals are sampled; 80/100/66/50 are emulator defaults).
- **Run `python tooling\check_guide.py` after every edit** (expected: 0 flow problems, the 7 cosmetic "optional step without [G]" findings). Run `tarcheck.py` after coordinate changes.
- Large edits go to an Opus subagent ("don't write it yourself", 25 Oct); audits are read-and-report first, then Braedyn approves, then edit. Record what changed in a dated `docs/audit-<date>.md` or build doc, and bump the TOC notes.
- Mark anything taken from Classic knowledge rather than Forever data as unverified, and keep an in-game test list in the build/audit doc.

## Where things are
- README with build history and route rationale: `docs/README.md`. 20-30 build: `docs/20-30-build.md`. Audits: `docs/audit-2026-10-27.md` (plus `audit-2026-10-25.md`, `tugs-diff.md`, `leatherworking-plan.md`, `forever-addons.md` still in the claude.ai Project). Stat weights: `docs/forever-enh-stat-weights.md`.
- Tooling and its README: `tooling\`. Detailed audit reports: `Claude outputs\audit-2026-10-27\`.
