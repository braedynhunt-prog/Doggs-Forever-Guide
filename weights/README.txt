Forever 2H Enhancement Dwarf Shaman - stat weights (built 24 Sep 2026)

forever-enh-stat-weights.md   the write-up: weights per level band, how the model works, sensitivity,
                              check of every gear call in the 1-20 guide, and the list of things to
                              read off the character sheet at the Server Slam
enh_weights.py                the kill-speed model (python3, no dependencies). Run it to print the
                              weights for levels 10/15/20 under both shock policies.
sensitivity.py                flexes every uncertain input (Spirit regen, expertise scaling, mob
                              level, Rockbiter growth, ...) and prints the weights for each case
score_items.py                scores every item in item_tooltips.json (+ the LW sets) with the
                              central and conservative weight sets, per quest and per slot
item_tooltips.json            the ~200 Forever item tooltips scraped from Wowhead on 24 Sep
scores_2026-09-24.txt         the last score_items.py output

Recommended weights for the addon (levels 15-20, attack power = 1):
  weapon dps 14 | Str 2 | AP 1 | Int 1.05 | Agi 0.85 (0.6 at 15) | Spirit 1.0 | Sta 0 (or 0.25 floor)
  spell dmg 1.5 | expertise 3 per point | +1% hit 6 | +1% crit 6
  (1 Nov 2026: the "mace +7 flat" term is gone - Dwarf Mace Specialization was removed from Forever on 17 Oct;
   score_items.py, sensitivity.py and tooling/dungeon_loot.py no longer add it. enh_weights.py gained 25 and 30
   bands for the 23-31 chapters; tooltips now live in tooltips/<date>.json, item_tooltips.json is the 24 Sep scrape.)

Open until checked in game: Forever's Spirit regen formula (decides Spirit 0.5..1.6), expertise
rating-to-% below 60 (decides expertise 1..5), Rockbiter AP growth inside a rank, Earth Shock's
spell-power coefficient. See the last section of the .md.
