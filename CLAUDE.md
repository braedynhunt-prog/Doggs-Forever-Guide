# WoW Forever Atlas

Braedyn's levelling guide for his Dwarf Shaman (2H Enhancement) on WoW Forever, Alliance, built as a Guidelime addon, plus the data and tooling that produce it. The guide covers 1-42 since 11 Nov 2026: chapters `00a`-`26` (group "Forever Shaman 1-30") and `27`-`41` (group "Forever Shaman 30-60", round 1; record `docs/30-40-build-2026-11-11.md`). 40-50 and 50-60 are the next rounds.

Owner: Braedyn. He plays the guide and reports what breaks; you keep the files correct.

## Layout
- `guide/Guidelime_ForeverShaman/` — the addon: one `.lua` per chapter (`00a`…`41`), TOCs. `Guidelime_ForeverShaman.zip` beside it is the installable copy; rebuild it after any guide edit.
- `tooling/` — Python scripts and the data they read. `tooling/qdb/{quest,npc,object,item}.json` is the decoded QuestieDB **Forever** database (`qdb_classic/` is the old Classic one). `check_guide.py` is the static flow check; `tarcheck.py` checks `[TAR]` positions against DB spawns. Read `tooling/README` before using any of them.
- `data/` — Wowhead quest-atlas scrape (`quests.json`, `entities.json`, `zone_*.json`). Source of quest XP. Wowhead now blocks the scraper; treat this as a frozen snapshot.
- `weights/` — stat-weight model for a 2H Enhancement shaman (`enh_weights.py`, `score_items.py`).
- `archive/` — superseded guide versions. Never edit.
- `Claude outputs/` — long audit reports.
- `docs/` — the project notes brought over from claude.ai: `RULES.md` (the standing rules, read it before touching the guide), `README.md` (build history and route rationale), `20-30-build.md`, `audit-2026-10-27.md` (latest state and open in-game test list), `forever-enh-stat-weights.md`.

## The rules
@docs/RULES.md

## Working agreements for this repo
- The guide is never edited casually. Audit or propose first, show Braedyn the proposed lines, edit after he approves. Large edits go to a subagent; the main session reviews them.
- After every edit to a `.lua` under `guide/`: run `python tooling/check_guide.py` (expected: 0 flow problems, 7 known cosmetic "optional step without [G]" findings) and, if any `[G]` changed, `python tooling/tarcheck.py`. Then rebuild the zip and bump the TOC version/notes.
- Verify every quest ID, NPC, vendor, coordinate and skill gate against `tooling/qdb/*.json` and `data/*.json`, never from memory or prose. Anything taken from Classic knowledge rather than Forever data is marked unverified.
- Data freshness: `tooling/sources.json` is the data manifest. Run `python tooling/check_sources.py` at the start of any plan that relies on game data, and state its result in the plan.
- Lua files: ASCII only, LF line endings. Don't invent Guidelime tags.
- Commit after each coherent change with a message saying which chapters changed and why. Don't rewrite history.
- A guide-edit round is not done until it is released (3 Nov). After the commits are pushed: `gh release create v<TOC version>` on main, title `Forever Shaman + Warrior + Druid 1-30 - <version>`, all three zips attached, body = the previous release's install section plus a changelog since the previous tag (per guide, from the TOC notes and commit log). One release per TOC version; a later edit on the same day goes into a new version. Check `gh release list` against the TOC versions at the start of any guide session.
- Don't touch the WoW `Interface\AddOns` folder unless asked. Installing = copying `guide/Guidelime_ForeverShaman/` there, nothing else.
- When something can't be verified from the data, say so and put it on the in-game test list in the current audit doc rather than guessing.

## Lessons
@lessons.md
