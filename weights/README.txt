Forever 2H Enhancement Dwarf Shaman - stat weights (built 24 Sep 2026)

forever-enh-stat-weights.md   the write-up: weights per level band, how the model works, sensitivity,
                              check of every gear call in the 1-20 guide, and the list of things to
                              read off the character sheet at the Server Slam
enh_weights.py                the kill-speed model (python3, no dependencies). Run it to print the
                              weights for levels 10/15/20 under both shock policies.
sensitivity.py                flexes every uncertain input (Spirit regen, expertise scaling, mob
                              level, Rockbiter growth, ...) and prints the weights for each case
score_items.py                scores every item in the newest tooltips/<date>.json (+ the LW sets) with the
                              central and conservative weight sets, per quest and per slot;
                              --tooltips <file> overrides
item_tooltips.json            the ~200 Forever item tooltips scraped from Wowhead on 24 Sep (superseded; kept for history)
scores_2026-09-24.txt         the last score_items.py output

Recommended weights for the addon (levels 15-20, attack power = 1):
  weapon dps 14 | Str 2 | AP 1 | Int 1.15 | Agi 0.8 (0.6 at 15) | Spirit 2.5 | Sta 0 (or 0.25 floor)
  spell dmg 2.0 | expertise 3 per rating point (= 7 per 1% in Pawn, see below) | +1% hit 6 | +1% crit 6
  (13 Nov 2026: Int 1.65 -> 1.15. The class tuning that went live 12 Nov cut Mental Dexterity back to 33/66/100% of Int and
   Stormstrike to 100% weapon damage on an 8 s cooldown; enh_weights.py carries both (MENTAL_DEXTERITY, SS_WEAPON_MULT,
   SS_COOLDOWN) and an optional Windfury Totem term. Model Int 1.13-1.19 at 15-40; nothing else moves by more than 0.05.
   Run: weights_2026-11-13.txt. Record: docs/audit-2026-11-13.md.)
  (8 Nov 2026: Spirit 1.0 -> 2.5, spell dmg 1.5 -> 2.0, Int 1.55 -> 1.65, Agi 0.85 -> 0.8. Braedyn's level-21 character sheet:
   mana regen 51 per 5 s at 41 Spirit, unchanged when Int went 45 -> 42 = 1.25 x Spirit per 5 s, no base, no Int term (the model
   had vanilla's 17 + Spi/5 per tick); melee crit 9.6% = 0.46 base + 39 Agi / 9.4 + 5% Thundering Strikes and spell crit 9.55% =
   2.3 + 45 Int / 20.0 + 5%, which confirms foreverdb.net's per-level client crit tables (build 1.60.1.70862) now in enh_weights.py;
   Earth Shock R3 71-76 (build 70755 of 3 Nov raised every rank to about Classic; WCLBox), Lightning Shield R2 24 / R3 40 per orb.
   Model output with these: Spirit 4.1-4.8 and SP 3.0-3.5 at 15-20 when shocking on cooldown, 2.5 / 1.8 with one shock per fight,
   1.9 / 1.2 with Lightning Shield only; the central set takes the one-shock case, the conservative set the LS-only case.
   Run: weights_2026-11-08.txt.)
  (4 Nov 2026: Forever tooltips show expertise as a percent ("Reduces chance to be Dodged or Parried by 0.6%", Dwarven Tree
   Chopper) and Pawn 2.14.1 parses it as ExpertiseRating in percent, so the Pawn scale in docs/forever-addons.md uses 7 per 1%
   (the model valued 6 points = 2.6% at 18). Whether that percent scales with level is still the in-game check below.)
  (3 Nov 2026: Int 1.05 -> 1.55 (Mental Dexterity 50/100/150% of Int, was 33/67/100%; source: Blizzard dev notes 3 Nov); enh_weights.py md term now 0.5 AP per Int per rank)
  (1 Nov 2026: the "mace +7 flat" term is gone - Dwarf Mace Specialization was removed from Forever on 17 Oct;
   score_items.py, sensitivity.py and tooling/dungeon_loot.py no longer add it. enh_weights.py gained 25 and 30
   bands for the 23-31 chapters; tooltips now live in tooltips/<date>.json, item_tooltips.json is the 24 Sep scrape.)
  (3 Nov 2026, later: score_items.py now reads the newest tooltips/<date>.json and prints which; scores_2026-11-03.txt re-run from 2026-11-02.json, which corrects Rockslicer (+7 Str, was +10) and the Ironforge Greathammer (no stats, was +4 Str +7 Sta). The tooltips/<date>.json caches carry no quest field, so score_items.py takes the quest links by item name from item_tooltips.json and says how many in its first line.)

Open until checked in game: whether the Spirit regen has a level term (re-read at the same Spirit a few
levels on), expertise rating-to-% below 60 (decides expertise 1..5), Rockbiter AP growth inside a rank,
Earth Shock's spell-power coefficient below top rank (0.386 at R7 on Wowhead). Settled 8 Nov 2026: regen
formula, crit per Agi / Int, base crit, Earth Shock and Lightning Shield ranks. See the .md.

11 Nov 2026: level-40 band and the Windfury / Stormstrike / Flurry terms
  enh_weights.py        now has an imbue switch (Rockbiter or Windfury), Stormstrike, Improved Stormstrike, Flurry, Anticipation,
                        Tidal Focus, Mindfulness, Improved Lightning Shield and Mental Quickness, bands 10/15/20/25/30/40, and prints
                        imbue and level-40 weapon tables after the bands. Bands 10/15/20 reproduce weights_2026-11-08.txt.
  talent_check.py       the levelling sheet's talent order against five alternatives at 25/30/40 (python weights/talent_check.py)
  score_items.py        --band N scores with that band's weights and rules (Mail from 40); no flag = level 20 as before
  weights_2026-11-11.txt the run: model, talent check, sensitivity. Write-up: docs/forever-enh-stat-weights.md, 11 Nov section.
  Spell data behind it: data/spell_tooltips.json (manifest row spell_tooltips).
