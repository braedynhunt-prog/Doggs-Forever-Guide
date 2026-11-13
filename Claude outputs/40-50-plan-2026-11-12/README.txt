Working papers of the 40-50 route plan (docs/40-50-plan-2026-11-12.md), 12 Nov 2026.

pool/                 output of pool_r2.py for quest levels 39-55: one text file per Wowhead category (zone) with every
                      candidate quest, its giver, ender, prerequisites, kill targets, item sources and rates, rewards;
                      _pool.json (the same, structured); _decisions.tsv (one verdict per quest: category, id, name, level,
                      required level, XP, money, verdict, reason, flags, highest mob level, best scored reward);
                      _review.txt; _need_*.tsv (what had no rate, tooltip or page when the pool was last built)
overrides_r2.tsv      the hand rulings (quest id, verdict, reason) applied on top of the automatic verdicts
chapters_r2.json      chapter numbers, titles, file names, level checks and the hand-written chapter notes
plan_head.md / plan_tail.md   the hand-written parts of the plan document
pool_r2.py            builds pool/ from data/zone_*.json, tooling/qdb, data/drop_rates.json, data/wowhead_quest_links.json,
                      weights/tooltips and the chapter files
decide_r2.py          applies RULES.md rules 2, 3, 11, 12, 13 and overrides_r2.tsv; writes pool/_decisions.tsv
plan_r2.py            assigns kept quests to chapters; writes the route file and the generated sections
assemble_r2.py        joins head + generated + tail into docs/40-50-plan-2026-11-12.md
compile_r2.py         compiled the two browser pulls (data/browser/r2_pages*_2026-11-12.tsv) into data/drop_rates.json,
                      data/wowhead_quest_links.json and tooling/trainer_costs.json (already run; kept for the method)
ingest_batch.py       ingested the combined zone pulls one block per run (already run)

To rebuild the plan after a ruling changes (from the repo root; R = this folder):
  python "R/pool_r2.py" . "R/pool" 39 55
  python "R/decide_r2.py" . "R/pool" data/browser/r2_pages_2026-11-12.tsv data/browser/r2_pages2_2026-11-12.tsv
  python "R/plan_r2.py" . "R/pool" docs/40-50-route-2026-11-12.txt "R/plan_generated.md"
  python "R/assemble_r2.py" .
  python tooling/route_xp.py docs/40-50-route-2026-11-12.txt

Verdicts: PLAIN, DUN-normal, DUN-boss (one boss holds the item) are required and counted. DUN-grind, GROUP-OPT, COND
(conditional), ASK (Braedyn's call), GATE (profession gate) are listed as optional and not counted. LATER = round 3.
OUT and JUDGE-OUT are silent in the guide.

13 Nov 2026, second revision: chapters_r2.json carries "visits" per chapter (the map ids of the zones the chapter goes to);
plan_r2.py writes them into the route file as '| zones ...' and tooling/route_xp.py checks every hand-in against them. A quest is
selected into the chapter that hands it in (the DARN, EAST and MOVED sets in plan_r2.py). The chapters are ordered by required
level: after a ruling changes, read the last lines of route_xp.py (required levels enforced) before trusting the table.
