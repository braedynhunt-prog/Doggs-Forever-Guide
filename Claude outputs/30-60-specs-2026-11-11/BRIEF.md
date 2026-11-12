# Brief: draft a chapter spec for round 1 of the 30-60 guide (11 Nov 2026)

You are a subagent working for the main session on Braedyn's WoW Forever levelling guide (Dwarf Shaman, 2H Enhancement, Alliance). Repo: `C:\Users\Braedyn\Documents\WoW Forever Atlas`. You draft the **spec** for the chapter(s) named in your prompt. You do NOT write the chapter Lua. A later agent writes the Lua from your spec, so the spec must carry every fact that agent needs, each one checked against the data.

## Hard limits
- Read-only on the repo. The only files you may create are your spec file(s) in the specs folder named in your prompt (and throwaway scripts beside them). No git commands that change anything. Do not touch `lessons.md`, `CLAUDE.md`, the guide, the data.
- Do not use a browser or fetch wowhead.com pages (the main session is using the rate limit). `nether.wowhead.com/forever/tooltip/item/<id>` and `/tooltip/quest/<id>` from a shell are fine, one request per second.
- If something is unclear, blocked or looks wrong, do not guess: write it under "Unsure" in the spec and in your report.
- Python on this PC: give Python Windows-style paths (C:/...). In a Bash heredoc, backslash escapes become control bytes, so avoid backslashes in heredoc scripts; for anything over ~20 lines write the script with the Write tool and run it by path.

## Read first (in this order)
1. `docs/30-60-build-plan-2026-11-11.md` - "Structure of the new chapters" and "Step 1 - chapter specs" define what a spec holds.
2. `docs/30-60-plan-2026-11-11.md` - the approved route. Read: "Rules added for 30-60", your chapter's section under "Round 1", "Professions thread", "Gold plan", "Carried into round 1", "Hearth / bind sequence", the "Addendum" and "Braedyn's answers" (the answers amend the sections above them).
3. `docs/RULES.md` (standing rules) and the repo's `lessons.md` (mistakes not to repeat).
4. `tooling/README.txt` (the tools and the qdb row layout).
5. `guide/Guidelime_ForeverShaman/23_Hillsbrad.lua` (the format the chapter will be written in), and the tail of `26_RazorfenKraul.lua` (where 1-30 ends). Read any other 1-30 chapter your zone touches.

## Corrections found on 11 Nov after the route plan was written (they override it)
- 659 Hints of a New Plague? and 555 Soothing Turtle Bisque are already done in the 1-30 guide (chapters 23/25). Before listing any quest, grep the 1-30 chapters for `[QA<id>` / `[QT<id>` to see whether it is already taken or done.
- 1050 Mythology of the Titans is NOT carried (no `[QA1050` in 00-26): chapter 27's Ironforge loop must pick it up.
- The Drowned City quests 95787, 95788 and 95798 start at Loremaster Dibbs (npc 2277, Southshore, Hillsbrad 50.6,57.1); 95798 ends at Abra Cadabra (npc 252019, Dalaran area, Alterac 12.1,70.3). 97130 starts and ends at Archmage Timear (npc 31439). They are picked up in chapter 27 and done in a new optional chapter **31b The Drowned City**.
- A new optional chapter **34b Razorfen Downs**: 96773 The Coldbringer's Eye (Archmage Lan'dalock 20735, start and end), 6626 A Host of Evil (Myriam Moonsinger 12866, The Barrens 49.0,94.9), 3636 Bring the Light (Archbishop Benedictus 1284, Stormwind; req 39).
- 79365 With Wind Beneath Your Wings is Horde-side on Wowhead: out.
- 95219 From Port to Port is a delivery to Feathermoon (Feralas): round 2, not a flight hop. Powderfuse Port has no flight paths.
- Draenethyst chain: 93464 starts at Magtoor (Swamp), ends at Azore Aldamort (Desolace 38.9,27.2); 93465 Azore to Azore; 93678 Azore to Magtoor. The route does Desolace before the Swamp, so the chain is out of round 1.
- 92867 Ground to Keep: Wowhead start and end = npc 219 (Groundskeeper Lomar), who is not in `tooling/qdb/npc.json`; all four kill targets are elites. It is `[O]` GROUP only if Old Leather Jacket (280505) or Stromgarde Hood (278567) scores as an upgrade, else out.
- 93429 Blood of My Blood: start and end npc 254775 Karana (no spawn in qdb). 93585 This Light of Mine ends at Magtoor 1776. 97284 Vahlarriel's Vengeance: start and end Vahlarriel Demonslayer 5642. 98233 Sword in the Slime: start and end Guard Jameson 271167. 79624 Anyone Can Cook: drop-start, ends at Skonk 217300. 2500 Badlands Reagent Run and 17 Uldaman Reagent Run: Ghak Healtouch 1470 (Thelsamar). 96135 Heed My Call: Veyric to Veyric; 96016 The Tempest's Weapons: Veyric to Bath'rah 6176; 79358 Storm, Earth and Fire starts at Veyric. Chain order on Wowhead: 94789 > 96264 > 79358 > 96135 > 96016.
- 97328 Anything of Value: starts at the object 661516, ends at Wharfmaster Lozgil 4631; Wowhead lists it in a series 97329 > 97328 > 97331 > 97332 although qdb shows no prerequisite. Mark "prerequisite unverified".
- Live drop rates 11 Nov (single-dropper tooltips): Sealed Folder 4482 78.0% (Forsaken Courier) so 658 is plain; Jameson's Training Sword 280203 35.2% so 98233 is an XP-only optional = out; Jumbo Crawfish Shell 43.5%; Coyote Pelt 16.6%, Intact Tallstrider Beak 16.0%, Crawler Spittle 12.2% (their quests are out). Multi-dropper items still being pulled by the main session: 267266, 266425, 266427, 266888, 8009, 8052, 7846, 7847, 7848, 213422. If your chapter depends on one of them, write both outcomes ("plain if >= 60%, [O] if 30-60%, out below") and list it under "Needs pull".
- Flight graph (client TaxiPath 70888, Alliance): Stormwind - Sentinel Hill, Lakeshire, Ironforge, Darkshire, Booty Bay, Nethergarde Keep, Morgan's Vigil. Ironforge - Stormwind, Menethil, Thelsamar, Southshore, Refuge Pointe, Aerie Peak. Southshore - Ironforge, Menethil, Refuge Pointe, Aerie Peak. Refuge Pointe - Ironforge, Menethil, Thelsamar, Southshore, Aerie Peak. Booty Bay - Stormwind, Sentinel Hill, Darkshire. Darkshire - Stormwind, Sentinel Hill, Lakeshire, Booty Bay, Nethergarde Keep. Nethergarde Keep - Stormwind, Darkshire, Morgan's Vigil. Thelsamar - Ironforge, Menethil, Refuge Pointe, Farholde Keep. Lakeshire - Stormwind, Sentinel Hill, Darkshire, Morgan's Vigil, Farholde Keep. Farholde Keep - Lakeshire, Thelsamar, Morgan's Vigil. Theramore - Auberdine, Thalanaar, Nijel's Point, Gadgetzan, Talrendis Point, Ratchet. Nijel's Point - Auberdine, Theramore, Stonetalon Peak, Feathermoon. Auberdine - Rut'theran, Astranaar, Theramore, Stonetalon Peak, Nijel's Point, Feathermoon. A flight point must be discovered on foot before it can be flown to: check the 1-30 chapters (`[F ...]`, `[P ...]` tags and their text) for which ones he has; say "undiscovered, first trip by road" where he has not been.
- Wowhead start/end data for more quests: `C:\Users\Braedyn\AppData\Local\Temp\claude\d2bbe0dc1f9a43ed\2646e58a-e308-4b8e-b9ed-860a59359d3c\scratchpad\wh_quest_links_partial.txt`.
- Chapter numbering for round 1: 27, 28, 29, 30, 31, 31b, 32, 33, 34, 34b, 35, 36, 37, 38, 39, 40, 41 (41 = Powderfuse Port, new). `[NX]` chains in that order.

## Rules to apply (from RULES.md and the route plan; quote the rule when it removes a quest)
- Drop-quest rule: a mob-drop collection is plain at a Wowhead Forever rate of 60%+ (or with an object source, or a single named mob at 60%+); `[O]` at 30-60% with "drop quest, ~N kills" (N = count / rate), unless the route's kill quests on the same mobs already cover the budget (then plain with the budget label); under 30% it is out, with every quest behind it in the chain. Rates: `data/drop_rates.json` and tooltip "Drop Chance" in `weights/tooltips/2026-11-11.json`. Class-quest items (Twisted Totems) ignore the rate.
- Optional-step test: an `[O]` quest stays only for a scored gear upgrade, a bag, a food-thread recipe, or a gate (class quest, trainer, profession rank, mount, needed reputation). XP-only optionals are out. Elite and group quests get the same test and a `GROUP n+` label.
- Rule 2: dungeon chapters are optional chapters; each quest labelled normal / grind; one run only, never a re-run.
- Rule 9: every quest picked up is turned in or explicitly abandoned, in this chapter or a named later one. List what is carried in and out.
- Before a quest goes in: read its prerequisites (quest row [11] preQuestGroup, [12] preQuestSingle in `tooling/qdb/quest.json`) and its start NPC's spawn; before a quest goes out or optional: list every quest that names it as a prerequisite.
- Faction: Wowhead `side` first (1 Alliance, 2 Horde, 3 or "Both"), then the race mask.
- Every id, coordinate, price, XP value and stat line comes from the data files in the same step, never from memory. Search NPC and object names case-insensitively before calling one absent. When one qdb field is empty, check the other tables keyed on the same id.
- Gear: scores from `weights/score_items.py` on `weights/tooltips/2026-11-11.json` (read `weights/README*` and `python weights/score_items.py --help`; `python tooling/gear_calls.py --help`). Band 30 for chapters 27-34b, band 40 (`--band 40`) for chapters 35-41. Leather or cloth by score until 40; mail only from level 40. Stat order and weights come from `docs/forever-enh-stat-weights.md`, not from memory. Compare each reward against what he is likely wearing from earlier chapters' picks (say which).
- Prices: trainers from `tooling/trainer_costs.json`; vendor items = tooltip sell price x 4.
- XP and quest money: `data/zone_*.json` (`python tooling/qinfo.py <ids>` prints XP; it reads those files).
- Coordinates are Forever map space straight from `tooling/qdb` spawns (`python tooling/loc.py`, `qinfo.py`). Zone names for `[G]` must be ones `tooling/guidelib.py` ZONES knows.

## Useful commands (run from the repo root)
- `python tooling/qinfo.py <ids>` (add `-s` for one line each), `python tooling/qinfo.py zone:<zoneOrSort>`, `python tooling/qdetail.py <ids>`, `python tooling/loc.py "<npc name>" <npc id> obj:"<object name>"`
- `python tooling/pool30.py L28-41 <zone ids>` - the zone's pool; reconcile it with the route plan so no plain kill/object quest is missed, and say which pool quests you left out and why (one line each).
- `python tooling/gold.py` - quest money per chapter (1-30 running total is 17g 05s at the end of 26).

## The spec file
Write `<specs folder>\<chapter>.md` (for example `27.md`, `31b.md`), plain ASCII Markdown, with these sections:
1. **Header**: file name to create (`NN_Name.lua`), `[N <levels> <Title>]`, `[NX ...]` next chapter title, `[GA ...]`, description line, level on entry and expected level on exit.
2. **Entry state**: where he stands, hearth, quests carried in (ids), professions targets that fall in this chapter.
3. **Travel and hearth**: how he gets in and out (flight names, boats, roads, with coordinates of flight masters / innkeepers from qdb), bind changes.
4. **Route**: the steps in play order, grouped into legs. For every quest step: action (accept / objective / turn in), quest id and exact title, XP and money, NPC or object id + name + `x,y Zone`, objective with counts and mob/object ids + location, drop rate and kill budget where the rule needs one, prerequisite, label (plain / `[O]` + reason / GROUP n). For non-quest steps: trainer (`[T]`), vendor (`[V]`) with price, profession stop, class step (`[A Shaman]`), note (`[OC]`).
5. **Gear calls**: per reward choice: the pick, its score, the runner-up, and what it replaces.
6. **Out**: quests of the zone left out, one line each with the rule.
7. **End check**: what the log should hold at the chapter's end; carried out.
8. **Totals**: plain quest count, plain XP, `[O]` XP, quest money.
9. **Unverified / in-game test list** and **Needs pull** (what only a Wowhead page can settle) and **Unsure**.
10. **Deviations from the route plan**: every place the spec differs from `docs/30-60-plan-2026-11-11.md`, with the data that forced it.

If the Write tool refuses the spec file, write it with a short Python script instead and say so.

## Report back (as text, this exact shape, at most 60 lines per chapter)
```
CHAPTER <n> <title> | levels a-b | file <spec path>
HUB/HEARTH/TRAVEL: ...
PLAIN (n, XP total, money): id Title XP; ...
OPTIONAL: id Title XP - reason / budget; ...
OUT: id Title - rule; ...
GEAR: quest id -> pick (score) over runner-up (score), replaces X; ...
TRAINERS/VENDORS/PROFESSIONS: ...
CARRIED IN: ... | CARRIED OUT: ...
DEVIATIONS FROM ROUTE PLAN: ...
UNVERIFIED / TEST LIST: ...
NEEDS PULL: ...
UNSURE: ...
VERIFIED: what you checked against which file
```
