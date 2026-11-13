# Forever 2H Enhancement Dwarf Shaman — stat weights (levels 1-20)

Built 24 Sep 2026 for the "our own Pawn" project. Braedyn's brief: tune for **kill speed** (mobs per hour while grinding/questing), **1-20 in bands**, **2H Enhancement only**. Tooling at `weights\`: `enh_weights.py` (the model), `score_items.py` (scores the scraped Forever tooltips + the LW sets and compares with the guide's picks), `sensitivity.py` (flexes every uncertain input), `item_tooltips.json` (the ~200 Forever tooltips from Wowhead, 24 Sep), `scores_2026-09-24.txt` (last run), `README.txt`. Next step agreed 24 Sep, late: a data-logging addon ("DoggsProbe") that records all of this while he plays — spec in the claude.ai Project doc `claude/forever-probe-addon-spec.md`. Nothing has been checked in game yet — the "verify at the Server Slam" list at the bottom is the price of that.

## The weights (attack power = 1)

| stat | level 10 | level 15 | level 20 | notes |
|---|---|---|---|---|
| weapon DPS (2H) | 14 | 14 | 14 | exact: 14 AP = 1 DPS, and Rockbiter is AP so weapon speed does not matter before Windfury (30) |
| Strength | 2.0 | 2.0 | 2.0 | 2 AP per point for shaman |
| Attack Power | 1.0 | 1.0 | 1.0 | |
| Intellect | 0.66 | 1.63 | 1.67 | 8 Nov 2026: model values with Ancestral Knowledge 2/5 from 20 (central 1.65; was 0.58 / 1.55 / 1.58). = Mental Dexterity (1.5 AP per Int at 3/3, from ~level 12) + a little spell crit. 3 Nov 2026: was 0.4 / 1.05 / 1.05 at 1 AP per Int; Mental Dexterity now 50/100/150% of Int, up from 33/67/100% (source: Blizzard dev notes 3 Nov). **The mana pool itself is worth nothing for kill speed** (see below) |
| Agility | 0.4 | 0.6 | 0.8 | crit only. 8 Nov 2026: 1% crit per 7.3 Agi at 10, 8.2 at 15, 9.4 at 20, 11.5 at 30, 19.7 at 60 (Forever client PlayerExpectedStat table via foreverdb.net, confirmed on the character sheet at 21); was ~6 / ~7 / ~8, so Agi was 0.5 / 0.6 / 0.85 |
| Spirit | **2.5** (model 7.6) | **2.5** (model 4.8) | **2.5** (model 4.1) | 8 Nov 2026: the character sheet settled the regen: 51 mana per 5 s at 41 Spirit, unchanged when Int went 45 to 42 = **1.25 x Spirit per 5 s, no base term, no Int term** (vanilla's 17 + Spi/5 per tick would read 63). 0.25 mana/s per point is 2.5x the slope the model had. The model's number depends on how much mana you burn: 1.9 keeping only Lightning Shield up, 2.5 with one shock per fight, 4.1 shocking on cooldown, 5.8 with 15 s walks (level 20). Central set holds the one-shock value. Was 1.0; the old note read: the big surprise, and the least certain number — range 0.5-2.3 depending on Forever's regen rules and how much you drink; use 1.0 until the character sheet settles it |
| Stamina | 0 | 0 | 0 | never limits a steady grind; only deaths, multi-pulls and dungeon tanking give it value. Suggest a 0.25 floor in the addon so +Sta items aren't shown as literally worthless |
| Spell damage | **2.0** (model 4.2) | **2.0** (model 3.5) | **2.0** (model 3.0) | Earth Shock + Lightning Shield scaling with the vanilla per-rank coefficients (Wowhead Forever gives 0.386 at top rank, the vanilla value). 8 Nov 2026: Earth Shock ranks were raised to about Classic on 3 Nov (R3 69-74, read 71-76 in game at 21), so shocks are worth casting from 14 and spell damage scores with them: 1.2 Lightning Shield only, 1.8 one shock per fight, 3.0 on cooldown. Was 1.5; old note: Forever's coefficients are unknown (vanilla used) — range 0.3-3.9 |
| Expertise (per point on the tooltip) | n/a | **3** (model 5.6) | **3** (model 5.2) | Forever item expertise is a *rating* (10 rating = 1% at 60). Model assumes the TBC below-60 curve (6 rating ≈ 2.6% at 20 → about 5% more swings landing from the front). If Forever doesn't scale ratings by level it's 0.8-1.2 instead |
| +1% hit or +1% crit | 2.7 | 3.8 | 6.0 | |
| mace (Dwarf Mace Specialization, +1% crit) | +3.4 | +4.3 | +7.5 | flat bonus per mace ≈ +0.25 / +0.3 / +0.5 weapon DPS. **17 Oct: the Oct 15 beta build removed weapon specializations (Dwarf Mace Spec is now Earth Fury, 2% crit damage) — this term is obsolete; 1 Nov: the 30 Oct hotfix cache replaces Earth Fury with Artisan's Precision (1% hit with spells and attacks; datamined, unverified in game)** |

**13 Nov 2026: Int is 1.15, not 1.65** (Mental Dexterity back to 100% of Int with the 12 Nov tuning; see the 13 Nov update at the end; everything else in this set stands). Recommended "central" set for the addon (15-20), **8 Nov 2026**: `wdps 14, Str 2, AP 1, Int 1.65, Agi 0.8 (0.6 at 15), Spi 2.5, Sta 0 (or 0.25 floor), SP 2.0, Exp 3, Hit% 6, Crit% 6` (mace term dropped, see above); conservative set `Spi 1.5, SP 1.0, Exp 1` (the Lightning-Shield-only case). Until 8 Nov the central set was `Int 1.55, Agi 0.85, Spi 1.0, SP 1.5` and the conservative `Spi 0.5, SP 0.5, Exp 1`; every gear call below was made with those, and `tooling/gear_calls.py` re-scores them (docs/audit-2026-11-08.md).

3 Nov 2026: central Int 1.05 → 1.55 (Mental Dexterity 50/100/150% of Int, was 33/67/100%; source: Blizzard dev notes 3 Nov). Model Int per band now L10 0.60/0.55, L15 1.58/1.53, L20 1.58, L25 1.60, L30 1.59 (shock-every-6 s / kill-speed-optimum policy). The gear-pick sections below still use the old weights.

## How the model works (so it can be argued with)

Steady-state grind loop: fight → walk/loot (9 s) → fight …, drink whenever the pool is empty. Kill speed = 3600 / (fight time + walk + drink time per fight). Weights are numeric derivatives of that per point of each stat, normalised to AP.

- **Character**: Dwarf Shaman base stats interpolated from the Classic level-1 line and wowsims/sod's level 25/40/60 tables (Dwarf offsets +2/−4/+3/−1/−1), plus the guide's own gear at each band (Coldridge Hammer at 10; Mountaineer's Greataxe + Bingles' gloves + Robe of the Keeper at 15; Smite's Hammer + the Hall of Thanes/Deadmines set at 20). Talents: Mental Dexterity 1/3 at 10, 3/3 + Thundering Strikes 3/5 at 15, + TS 5/5 + Shamanistic Focus at 20. Rockbiter R2/R3 at +63/+76/+103 AP (foreverdiff floor → Wowhead max, growing inside the rank). Result: 133 / 193 / 312 AP, 5.9 / 8.1 / 13.6% crit, 16 / 23 / 41 white DPS.
- **Melee**: AP = 2×level + 2×Str − 20 (+ Rockbiter + Int×MD); DPS = weapon DPS + AP/14; same-level mob from the front: 5% miss, 5% dodge, 5% parry, 10% glancing at 95%, crits ×2. Crit per Agi (8 Nov 2026) from the Forever client's PlayerExpectedStat table (foreverdb.net/stats/shaman, build 1.60.1.70862: 7.3 @10, 8.2 @15, 9.4 @20, 10.3 @25, 11.5 @30, 19.7 @60), base melee crit 0.46 and base spell crit 2.3 from the character sheet at 21 (melee 9.6% = 0.46 + 39/9.4 + 5% Thundering Strikes; spell 9.55% = 2.3 + 45/20.0 + 5%). Before 8 Nov: vmangos / XPOff / wowsims anchors (4.6 @1, 7.7 @19, 10.3 @25) and base crit 1.7.
- **Spells**: 8 Nov 2026: Earth Shock at the 3 Nov build's values (R1 21-24, R2 38-41, R3 69-74, R4 131-140; WCLBox; the beta had 18 / 33 / 49 / 81 and the model used those until 8 Nov) and Lightning Shield at 13 / 24 / 40 / 64 per orb (Forever; Classic 13 / 29 / 51 / 80). The original text: Earth Shock with Forever's cut base damage (R2 33, R3 49 — Classic was 32-34 / 60-64), 6 s cooldown, vanilla SP coefficient (0.21 / 0.30); Lightning Shield 3 orbs per fight (Forever cut ~10%); Shamanistic Focus −45% mana at 20. Spell crit ×1.5, 3% spell miss.
- **Mana/health economy**: every point of mana spent is eventually drunk back at (drink rate + Spirit regen) mana/s — Spring Water 8/s at 10, Ice Cold Milk 20/s at 15-20; Spirit regen (8 Nov 2026: 1.25 x Spirit per 5 s = 0.25 mana/s per Spirit, nothing else, as read on the character sheet; until then vanilla's 15-17 + Spi/5 per tick, 0.1 mana/s per Spirit) applies outside the 5-second rule: 4 s of the walk plus the whole drink. HP lost per fight (0.7×level DPS after armour, minus walking regen) is healed with Healing Wave at ~1.8 HP per mana. Because both loops are steady-state, **pool size and max HP cancel out**: a bigger pool means fewer, longer drinks, not less drinking. That's why Int is "just" Mental Dexterity and Sta is 0.
- **Policy**: the model picks the shock count per fight that maximises kills/hour. At 10-15 that is *one Earth Shock on the pull* (each extra 85-mana shock costs more drinking than the ~1.2 s of melee it saves); at 20 with Shamanistic Focus shocking every 6 s is roughly break-even, so it doesn't matter. Lightning Shield is always worth keeping up.

### Sensitivity (level 20)
8 Nov 2026 run (`weights/weights_2026-11-08.txt`): robust: weapon DPS, Str, Int, Agi, hit/crit. Moves a lot: **Spirit** (4.1 baseline; 3.0 with 5 s walks, 5.8 with 15 s; 3.5 / 5.6 with mob HP +30 / -30%; 2.5 with one shock per fight, 1.9 Lightning Shield only), **spell damage** (3.0; 1.7-4.3 with the shock coefficient 0-2x; 1.8 one shock, 1.2 LS only), **expertise** (5.5 TBC-rating; 2.6 from behind). The pre-8-Nov run read: robust: weapon DPS, Str, Int, Agi (0.73-1.08 across a ±20% crit table), hit/crit. Moves a lot: **Spirit** (0.5 if Forever has no Spirit regen; 1.2 with 5 s walks; 2.3 with 15 s walks; 1.0 if the regen formula is half of vanilla), **spell damage** (1.3-3.9 with the Earth Shock coefficient 0-2×), **expertise** (1.2 flat / 3.0 TBC-points / 5.2 TBC-rating). Attacking from behind (grouped with a tank) halves expertise (2.5) since parry stops mattering. Mob level +2 raises Agi/crit/hit ~10%.

## Findings worth acting on

1. **Talent order: Mental Dexterity first, not Thundering Strikes.** At 10-12 one rank of MD is ~9 AP (a third of ~27 Int) versus ~2.3 AP-equivalent for 1% crit; even at 20 it's 43 AP vs ~6. Icy Veins' order (TS 10-14, MD 15-17) costs real damage for five levels. Recommended: MD 10-12, TS 13-17, Improved Ghost Wolf 18-19, Shamanistic Focus 20 (11 points).
2. **Spirit is a real stat for a levelling shaman.** 8 Nov 2026: confirmed and then some. Forever's regen is 0.25 mana/s per Spirit point with no base (character sheet), 2.5x vanilla's slope, so on the model a point of Spirit is worth more than a point of Str whenever you shock at all (2.5 with one shock per fight, 4.1 on cooldown; 1.9 even with Lightning Shield alone). Central set 2.5. The original reasoning: under vanilla regen rules a point of Spirit is worth about as much as a point of Int, because drinking is 15-25% of grind time and Spirit is the only stat that shortens it. Icy Veins ranks Spirit second to last because they think in DPS, not kills per hour. Held at 1.0 rather than the model's 1.6 until Forever's regen is confirmed (Forever runs on a modern client; nothing published says whether Spirit still regens the vanilla way).
3. **Shocks are worth casting from 14** (8 Nov 2026; the 3 Nov build raised Earth Shock R3 from 49 to 69-74 for the same 85 mana): the model's kill-speed optimum is now shock on cooldown plus Lightning Shield at every band from 15, and the Spirit and spell-damage weights assume at least one shock per fight. The pre-3-Nov finding was: shocks are barely worth casting while grinding at 10-19 (85 mana for 49 damage when a drink gives 20 mana/s): shock on the pull, then melee.
4. **The mana pool doesn't buy kill speed**, so +Int items are Mental Dexterity items (1 AP each) — fine, still better than Agi — and "+mana" is not a reason to prefer them.
5. **Stamina is 0 for kill speed.** If that feels wrong in dungeons, that's the dungeon case, not the grind case; the addon can carry a small floor.

## Check of the guide's gear picks (level-20 central weights; conservative in brackets)

Weapons, in order: Smite's Mighty Hammer 308 > Rockslicer 296 > Orc Crusher 278 ≈ Rhahk'Zor's Hammer 276 [269] > Staff of Westfall 248 [229] > Emberstone Staff 239 [213] ≈ **Ironforge Greathammer 239** ≈ Taskmaster Axe 235 [216] > Mountaineer's Greataxe > Coldridge Hammer > Gnarled Short Staff > Smooth Walking Staff 38 vs Anvilmar Sledge 43. Every weapon call in the guide holds. Two refinements: Rhahk'Zor's Hammer is a clear upgrade over the Greathammer (+37), not just a consolation roll; and **Staff of Westfall (Oh Brother, guaranteed) ties or beats the Greathammer**, so if Deadmines gives neither Smite's nor Rockslicer it is the Oh Brother pick, ahead of the Tunic. Orc Crusher (25) is a −30 downgrade from Smite's, not a side-grade.

Armour: Deepgrave Trousers 19.6 > Dreamer's Leggings 17.6 [13.6] > Smith's 11.4 > Frontier 8.6 > Direhammer 3.0 ✓. Gold-flecked Gloves 14.0 > Flamefist Grips 11.4 [9.4] > Dusty Mining Gloves 7.7 > Tomb Robber's 6.3 > Bingles' 3.6 ✓. Blackened Defias Belt 18.0 > Dusty Belt 8.2 ✓. Blackened Defias Armor 10.6 > Tunic of Westfall 9.3 ✓ (closer than the guide implies; both far behind the crafted chests). Bravo's Armbands 11.4 — only wrist with stats ✓. Spiritwraith Drape 6.4 ≈ Catacomb Cloak 6.0 > Cape of the Brotherhood 4.2 ≈ Miner's Cape 4.0 ✓ (Deepgrave over Catacomb for An Ancient Grudge is right by a mile). Lavishly Jeweled Ring 8.0 ✓. Ephemeral Choker 2.0 — worthless by the numbers but still the only neck ✓.

Crafted sets (README numbers): **Totemic Leather beats Brawler's in every slot** for a 2H Enhancement shaman (Str 2.0 ≫ Agi 0.85, and the spell damage counts): Armor 24.6 [19.6] vs 18.9, Pants 32.7 vs 23.6, Boots 17.5 [12.5] vs 14.2, Gloves 15.5 [10.5] vs 11.4 (and vs Gold-flecked 14.0 — a toss-up that the SP weight decides), Belt 14.0 vs 11.4 but the **Defias Belt (18.0) beats both**. Hood: Totemic 12.0 [4.0] vs Brawler's 6.8 — the only head items in the bracket. So the README's "LW sets beat the quest/dungeon pieces slot for slot" holds, with the belt as the exception.

### Disagreements / additions
- **Chok'sul (quest 256, 20+): a coin flip, not Loch Walkers.** Minor Channeling Ring 8.1 [4.1] vs Kimbra Boots 7.2 [5.7] vs Loch Walkers 6.4 [4.9]. The ring goes into an empty second ring slot and survives the Totemic Boots; take the ring unless spell damage turns out to be weak on Forever, then Kimbra.
- **Oh Brother (167)**: Staff of Westfall if no Deadmines 2H dropped (see above); otherwise Tunic only if no Defias/Totemic chest.
- **The People's Militia (14)**: Boots of the People's Militia (+3 spell damage, 4.5) are a small upgrade over the statless Frosthowl's until the Totemic Boots at 17 — not "nothing".
- **Dwarven Tree Chopper (A Dark Threat Looms, 20+)**: 213 even with the generous expertise weight — well below the Greathammer; the guide's silence is right.
- Slot-by-slot best at 20 from everything in the data: Smite's; Totemic Hood; Ephemeral Choker; Grave Shroud (Ruins of Lordaeron, 7.7) > Spiritwraith; Totemic Armor; Bravo's; Totemic Gloves ≈ Gold-flecked; Blackened Defias Belt; Totemic Pants; Totemic Boots; Lavishly Jeweled Ring + Minor Channeling Ring.

## Verify in game (first things to look at on the character sheet)
1. SETTLED 8 Nov 2026 (level 21): **mana regen** 51 per 5 s at 41 Spirit, 51 again after Int 45 to 42 = 1.25 x Spirit per 5 s, no base, no Int term. Still open: a level term (re-read at the same Spirit at 25 or 30).
2. **Expertise %** on the character sheet with the Dwarven Tree Chopper equipped, or any +expertise item (settles rating vs points and the below-60 scaling).
3. **Rockbiter's AP** on the character sheet at 10, 16 and 20 (does it grow inside a rank?).
4. PARTLY SETTLED 8 Nov: **Earth Shock R3 reads 71-76 at 21** with no spell-damage gear (WCLBox base 69-74 plus within-rank level scaling). Still open: the tooltip with a +spell-damage item on (R3 with the +18 Fang of Magmatus: vanilla predicts ~+5).
5. SETTLED 8 Nov: **crit at 21** melee 9.6% (0.46 base + 39 Agi / 9.4 + 5% Thundering Strikes) and spell 9.55% (2.3 + 45 Int / 20.0 + 5%): foreverdb's client tables hold and base melee crit is 0.46, not 1.7. The Agility tooltip's own "6.69%" is wrong (a Blizzard forum bug report says the Forever Agility tooltip misreports crit); read the Crit Chance line, not the Agility hover.
6. Whether Spirit regen continues while drinking (assumed yes).
7. SETTLED 8 Nov: Lightning Shield R2 reads 25 at level 21 (WCLBox base 24 plus within-rank scaling); the model's 24 / 40 hold.

## Sources
8 Nov 2026: Braedyn's level-21 character sheet (regen, crit, Earth Shock tooltip); foreverdb.net/stats/shaman (Forever client PlayerExpectedStat and ChrClasses tables, build 1.60.1.70862, extracted 2026-11-08: crit per Agi / Int per level, 2 AP per Str, 15 mana per Int; says base crit, dodge per Agi and regen per Spirit are server-side and not in the client); wowforever.wclbox.com (Earth Shock, Lightning Shield, Healing Wave ranks, build 1.60.1.70862, with the 3 Nov build 70755 shock change); wowhead.com/forever/spell=1220751 (Earth Shock SP mod 0.386). Earlier: foreverdiff.com (client diff: Earth Shock, imbues, talents, totems, removed talents), Wowhead Forever spell 8017/8018/8019/10399 (Rockbiter AP) and item 2907 (Tree Chopper), wowforevertalents.com (talent text), Icy Veins Forever Enhancement guide and Dwarf race guide, Mobalytics shaman overview, warcrafttavern.com/forever/guides/stats (2 AP/Str, 20 Agi/1% crit, 15 mana/Int, 5% miss), github wowsims/forever issue #34 + base_stats_auto_gen.go (expertise 10 rating/1% at 60, crit per Agi 0.0508, base crit 1.675/2.201), wowsims/sod core/stats.go + mana.go (shaman base stats 25/40/50/60, crit per Agi/Int by level, Dwarf offsets, 15+Spi/5 regen), xpoff.com level-19 stat guide (0.13% crit and dodge per Agi, 0.055% spell crit per Int), vmangos StatSystem.cpp (AP formula, 4.6 Agi/1% at L1), magey/classic-warrior attack table (miss/dodge/parry/glancing), vanilla WoWWiki (Spirit regen table, spell coefficients, recalled — Fandom pages return 402 now).

## 1 Nov 2026 update - mace term removed from the code, bands 25 and 30 added
- The mace term (obsolete since the 17 Oct build, see the table) is now gone from `score_items.py`, `tooling/dungeon_loot.py` and the model's default scenarios (`mace=False`); `sensitivity.py` keeps one case, "mace spec restored", that shows what it was worth.
- `enh_weights.band_scenarios()` gained **25** (Smite's Hammer + the end-of-20s set, 11 talent points, Flurry not modelled) and **30** (Twilight Maul, Defender's Leather Helm, Naga Battle Gloves, Bands of Serra'kis, Glowing Thresher Cape + the rest; Elemental Weapons 3/3). Gear sums from `weights/tooltips/2026-11-01.json`. Model output (shock every 6 s + Lightning Shield): L25 `int 1.10, agi 0.75, spi 1.08, sp 2.75, exp 4.10, hit/crit% 6.7`; L30 `int 1.09, agi 0.84, spi 1.10, sp 2.42, exp 3.90, hit/crit% 8.2`. As for 10/15, the loot report takes only Int and Agi from these bands and holds Spirit 1.0, SP 1.5, Exp 3.0 at the recommended values.
- Tooltip cache: `weights/tooltips/<date>.json` (newest wins); `item_tooltips.json` stays the 24 Sep scrape. Stats did not change between the 29 Oct and 1 Nov pulls.
- **The "Check of the guide's gear picks" section above predates the October stat changes.** On the 1 Nov tooltips: Deepgrave Trousers 19.6 -> 5.5 (lost +7 Str), Ironforge Greathammer 239 -> 224 (lost +4 Str +7 Sta), Flamefist Grips 11.4 -> 9.3, Dusty Belt 8.2 -> 3.7, Bravo's Armbands 11.4 -> 8.6, Rockslicer 296 -> 290 (+7 Str), Spiritwraith Drape 6.4 -> 6.6, Smite's Mighty Hammer 308 -> 301 (no mace term). Consequences, applied to the guide on 1 Nov (`docs/audit-2026-11-01.md`, step 5): Frontier Britches (8.6) and Smith's Trousers (11.4) now beat Deepgrave; Staff of Westfall (248) beats the Greathammer when no Deadmines 2H dropped; Catacomb Cloak is 3.0 (parse() counts its "+4 against Humanoids", the guide does not). `tooling/gear_calls.py` re-runs this check.

## 8 Nov 2026 update - character-sheet readings replace four guesses
- Braedyn at level 21 (Int 45, Agi 39, Spi 41; Thundering Strikes 5/5, Mental Dexterity 3/3, Ancestral Knowledge 2/5): mana regen 51 per 5 s while not casting, 51 again with Int 42 and no Spirit gear to vary; melee crit 9.6%, spell crit 9.55%; Earth Shock R3 71-76 with no spell-damage gear.
- Model changes in `enh_weights.py`: Spirit regen `0.25 x Spirit` mana/s (was `8.5 + Spi/10`); Agi-to-crit and Int-to-spell-crit per-level tables from the Forever client (foreverdb.net); base melee crit 0.46 (was 1.7); Earth Shock ranks 22.5 / 39.5 / 71.5 / 135.5 (3 Nov build; were 18 / 33 / 49 / 81); Lightning Shield 13 / 24 / 40 / 64 per orb (were 13 / 29 / 51 x 0.9); Healing Wave 1.75 HP per mana; Ancestral Knowledge 2/5 in the 20-30 bands. Run and sensitivity: `weights/weights_2026-11-08.txt`.
- Model output (AP = 1, kill-speed optimum = shock on cooldown + Lightning Shield at every band from 15): L15 `int 1.63 agi 0.58 spi 4.77 sp 3.51`; L20 `int 1.67 agi 0.82 spi 4.12 sp 3.00 exp 5.55 hit/crit 6.40`; L25 `int 1.72 agi 0.81 spi 3.13 sp 3.24`; L30 `int 1.69 agi 0.90 spi 2.93 sp 2.74`. One shock per fight at 20: `spi 2.46 sp 1.76`; Lightning Shield only: `spi 1.85 sp 1.18`.
- Central set now `Int 1.65, Agi 0.8 (0.6 at 15), Spi 2.5, SP 2.0` (the one-shock case, since the model's on-cooldown optimum assumes you drink every pool dry and never wait); conservative `Spi 1.5, SP 1.0, Exp 1`. Applied to `weights/profiles.py`, `weights/score_items.py`, `weights/README.txt`, the Pawn string in `docs/forever-addons.md` and the LOF Enhancement row (`Str 1.0, Agi 0.4, Sta 0.125, Int 0.825, Spi 1.25, AP 0.5, SP 1.0, Dmg 1.0, Hit 3, Crit 3, Armor 0.01, DPS 7`).
- Consequence for the guide: Spirit pieces score 2.5x and spell-damage pieces 1.33x what they did; `tooling/gear_calls.py` lists the calls that flip (docs/audit-2026-11-08.md). Stat order for rule 6 per point: weapon dps > Spirit ~ Str > spell damage > Int > Agi.

## 11 Nov 2026 update - Windfury, Stormstrike, Flurry and a level-40 band; imbue, weapon and talent verdicts
Plan: `docs/weights-40-plan-2026-11-11.md`. Run: `weights/weights_2026-11-11.txt`. Data: `data/spell_tooltips.json` (manifest row `spell_tooltips`), WCLBox talent page and foreverdb.net at build 1.60.1.70888, live item tooltips.

**What the brief had wrong (checked 11 Nov, logged in `lessons.md`).** Rage of the Storm is 102-154, speed 3.60, 35.56 dps, +16 Str +15 Sta, +10% Stormstrike damage (the "+15 Sta +12 Int, 3.20 speed" line was a 28 Oct reading). Elemental Weapons 3/3 adds 40% to Windfury's attack power as well as 20% to Rockbiter's. Improved Stormstrike is 50% / 100% per rank (Wowhead spell page: base value 20, rank curve 50 / 100). Flurry is 6% per rank. Tidal Focus gives +1% hit per rank and Mindfulness 17 / 33 / 50% mana regeneration while casting, so the Restoration points are not model-neutral. Stormstrike is tier 4 (15 points) on WCLBox and in the wowsims tree; its tooltip still says "Requires level 40".

**Imbue attack power grows with level.** The cast tooltips are rendered for a level-60 viewer. The passive auras on the Wowhead spell pages give the value at the rank's level: Rockbiter 88 (16) / 129 (24) / 211 (34) against tooltips of 118 / 194 / 355, Windfury 46 (30) / 119 (40) against 104 / 221. That confirms the floor and max columns the model has used since September; how fast the value climbs between them is still the linear convention, and every imbue row is printed at floor, model and max.

**Model changes (`weights/enh_weights.py`).** `Scenario.imbue` (Rockbiter or Windfury), talents `ss`, `iss`, `flurry`, `ant`, `tf`, `mind`, `ils`, `mq`, and `weapon_speed` is now used. Windfury: 20% per landed hit of 2 extra white swings carrying the rank's AP; no Rockbiter AP. Stormstrike: 150% of normalized weapon damage (weapon damage + AP x 3.3 / 14, as wowsims/forever reads the spell), a yellow strike, one in the first cooldown window and one per 6 s after, 8% of base mana, +20% on every Earth Shock after the pull shock; Rage of the Storm multiplies the strike by 1.1. Improved Stormstrike and Mindfulness give regeneration while casting (the fight plus the 5-second tail); in the central case they do not stack. Flurry: 6% per rank on the swings that follow a crit within 3 swings. Tidal Focus: melee hit and cheaper heals. Tables: Earth Shock R5/R6, Lightning Shield R5/R6, Healing Wave efficiency from 32, Rockbiter's level-34 rank 211-355 (was 211-260), crit rows for 35 and 40, client base mana per level, Sweet Nectar / Moonberry Juice / Morning Glory Dew. Bands 25 and 30 now use the sheet's talents; band 40 is new (route-plan gear: Str 7, Agi 5, Int 35, Spi 85, SP 53 before the weapon).

**Regression.** Bands 10 / 15 / 20: kills/hour and every weight identical to `weights_2026-11-08.txt`; only the printed pool and fights-per-drink move with the client base mana (L10 309 -> 304, L15 500 -> 487, L20 767 -> 757). `sensitivity.py` output is byte-identical.

**Weights (AP = 1, shock on cooldown + Lightning Shield, the optimum at every band).**

| band | wdps | Int | Agi | Spi | SP | Exp | +1% hit | +1% crit |
|---|---|---|---|---|---|---|---|---|
| 25 | 14.45 | 1.67 | 0.80 | 3.48 | 2.46 | 4.56 | 7.43 | 7.43 |
| 30 | 13.97 | 1.65 | 0.95 | 4.63 | 2.03 | 4.10 | 8.63 | 9.69 |
| 40 | 14.71 | 1.69 | 1.12 | 5.40 | 1.98 | 4.15 | 0.00 | 14.19 |

At 40 hit is worth nothing once Tidal Focus 5/5 has removed the 5% miss, and crit is worth more because it also drives Stormstrike and Flurry. The profiles still take only Int and Agi from the model (`weights/profiles.py`, `BANDS` now ends at 40) and hold Str 2, Spi 2.5, SP 2.0, Exp 3, wdps 14. The 8 Nov numbers for 25 and 30 (Int 1.72 / 1.69, Agi 0.81 / 0.90) are superseded; the 1-30 gear reports keep every pick and flag.

**Imbue verdict: no kill-speed case for Windfury at 30 or 40.** Kills/hour, model growth (floor - max):

| band | Rockbiter | Windfury |
|---|---|---|
| 30 | 198.0 (192.8 - 201.4) | 196.6 (196.6 - 199.1) |
| 40, Rage of the Storm | 222.4 (214.5 - 227.5) | 218.2 (218.2 - 221.3) |

Windfury gives up 200-360 AP on every swing and every Stormstrike for extra attacks that carry +64 AP at 30 and +167 at 40 (rank value x 1.4). The two are within 2% of each other, inside what the model can resolve, and Rockbiter is the steadier one. Chapters 22 and 24 of the 1-30 guide say "Windfury on the 2H from 30"; the model does not support that line and does not refute it. Not edited here (no guide edit in this plan). **Braedyn's decision (11 Nov 2026, confirmed the same evening for the 30-60 guide): the guide says Windfury on the two-hander from 30** - the online guides all say so and Rockbiter adds threat in groups; with a 2% gap the model is no reason to differ. Chapter 39 of the 30-60 guide trains Windfury Weapon rank 2 at 40 as a must.

**Weapon verdict at 40: Rage of the Storm, by a hair.** Rage 222.4 against Bonebiter 220.1 with Rockbiter, 218.2 against 217.8 with Windfury; without Stormstrike Bonebiter leads 170.3 to 167.5. The linear score (`python weights/score_items.py --band 40`: Bonebiter 583.5, Rage of the Storm 529.8) cannot see the Stormstrike bonus or the 3.6 speed that normalized Stormstrike rewards. A 1% gap means either is fine; Bonebiter is worth carrying if it arrives first, not worth a dungeon run on its own.

**Talent check (`weights/talent_check.py`), kills/hour.**

| build | 25 | 30 | 40 | vs sheet at 30 / 40 |
|---|---|---|---|---|
| A sheet as written | 216.1 | 198.0 | 222.4 | |
| B Flurry 5/5 first (26-30), Ancestral Knowledge 3 for Anticipation | 216.1 | 187.2 | 224.0 | -5.5% / +0.7% |
| C Enhancement only to 40 (Flurry 5, Mental Quickness 2, Improved Lightning Shield 3) | 216.1 | 198.0 | 228.2 | 0 / +2.6% |
| D Tidal Focus straight after Stormstrike | 216.1 | 189.0 | 224.0 | -4.5% / +0.7% |
| E Flurry in place of Improved Ghost Wolf | 216.1 | 199.2 | 224.0 | +0.6% / +0.7% |
| F sheet to 37, Flurry 5/5 in place of Mindfulness | 216.1 | 198.0 | 224.0 | 0 / +0.7% |

- The sheet's order to 32 is sound. Stormstrike (55 kills/hour at 40) and Shamanistic Focus (32) carry the build; Improved Stormstrike at 30-31 is the regeneration engine, and the builds that delay it lose 5% at 30.
- **Mindfulness 3/3 at 38-40 duplicates Improved Stormstrike 2/2** unless the two stack: removing either one costs nothing in the central case, removing both costs 6%. If they stack the sheet gains 11% (247.4) and is the best build here. One point at 38 and a look at the regeneration while casting settles it; until then the three points are a coin flip against Flurry.
- Flurry is weak at these crit rates (0.5 kills/hour per point at 40); Tidal Focus is worth about 1 per point, all of it from the hit.
- Improved Ghost Wolf, Spirit Weapons and Toughness have no term in the model. Builds B, D and E look better than they play because they skip Improved Ghost Wolf.
- Every difference in the table except the two -5% rows is under 3%, which is inside the model's resolution. Recommendation: keep the sheet; decide 38-40 from the stacking test.

**Limits of the model at these levels.** With Stormstrike the fights last 4.5-6.5 s. The model's continuous counts (a shock every 6 s plus the pull shock, three Lightning Shield orbs per fight) overstate damage in fights that short, so the absolute kills/hour at 25-40 are high; the comparisons share the bias. Windfury's variance, Flurry procs from Windfury and Stormstrike crits, and the dodge/parry reset of Improved Stormstrike are not modelled.

**In-game test list.**
1. Stormstrike offered in tier 4 at 25 (two client-derived sources say yes; the tooltip says level 40).
2. Rockbiter's AP on the character sheet now and one level later (how fast it grows inside a rank); the same for Windfury at 30. This decides the imbue rows.
3. Improved Stormstrike rank 1 in the talent pane: 50%.
4. At 38: does Mindfulness add to Improved Stormstrike's regeneration while casting?
5. Tidal Focus: does the hit show on the character sheet for melee, spells or both?
6. Windfury's extra attacks: do they carry the +AP on both attacks (tooltip wording says so)?

## 13 Nov 2026 update - the 12 Nov class tuning: Stormstrike 100% / 8 s, Mental Dexterity 100% of Int, imbues stack with weapon totems
Run: `weights/weights_2026-11-13.txt`. Record: `docs/audit-2026-11-13.md` (second part). Sources, all read 13 Nov: Blizzard hotfix notes dated 10 Nov, live 12 Nov 10:45 PST (US forum topic 2403040, posts 6 and 9; announced 6 Nov in topic 2404092); the live Wowhead tooltips (`data/spell_tooltips.json`, re-pulled: Stormstrike 17364 "100% weapon damage", "8 sec cooldown"; the Windfury Weapon tooltips no longer say they disable the Windfury Totem benefit); the WCLBox talent page at build 1.60.1.70938 (Mental Dexterity 33 / 66 / 100%).

**What Blizzard changed.** Stormstrike 100% weapon damage (was 150%) on an 8 s cooldown (was 6 s). Mental Dexterity 33 / 66 / 100% of Intellect as attack power (was 50 / 100 / 150% since the 3 Nov notes). Maelstrom Weapon: 20% cast time and mana per application at every rank (was 4 / 8 / 12 / 16 / 20%), and 6 / 7 / 8 / 9 / 10 activations per minute by rank (was 20 per minute at every rank). Weapon imbues and weapon totems work at the same time. The developers' note says the aim is that Enhancement prefers Strength and attack power and stays a Windfury spec, and the 6 Nov post says balance changes may follow "on future Tuesdays if necessary"; nothing further is announced.

**Model changes (`weights/enh_weights.py`).** `MENTAL_DEXTERITY` (0.33 / 0.66 / 1.0 per rank), `SS_WEAPON_MULT` 1.0, `SS_COOLDOWN` 8.0; Improved Stormstrike's buff now sees 15 / 8 = about 1.9 Stormstrikes; the +20% shock bonus is capped at one shock per Stormstrike (no effect at a 6 s cooldown); optional `Scenario.wf_totem_ap` for a Windfury Totem standing next to the fight (20% per landed white swing of one extra white swing; procs from Stormstrike and from Windfury Weapon's extra attacks left out). Maelstrom Weapon and Rage of the Farseer still have no term.

**Weights (AP = 1, kill-speed optimum = shock on cooldown + Lightning Shield).**

| band | wdps | Int | Agi | Spi | SP | Exp | +1% hit | +1% crit | kills/h (11 Nov) |
|---|---|---|---|---|---|---|---|---|---|
| 10 | 13.85 | 0.41 | 0.46 | 3.87 | 2.57 | 13.48 | 2.83 | 2.83 | 170.8 (172.2) |
| 15 | 13.94 | 1.13 | 0.55 | 4.54 | 3.43 | 5.68 | 3.84 | 3.84 | 146.5 (149.0) |
| 20 | 13.96 | 1.15 | 0.79 | 3.94 | 2.94 | 5.35 | 6.17 | 6.17 | 162.5 (165.2) |
| 25 | 14.31 | 1.17 | 0.78 | 3.18 | 2.75 | 4.38 | 7.14 | 7.14 | 191.8 (216.1) |
| 30 | 13.98 | 1.14 | 0.96 | 4.21 | 2.28 | 3.96 | 8.34 | 9.74 | 172.9 (198.0) |
| 40 | 14.50 | 1.19 | 1.13 | 5.10 | 2.24 | 3.96 | 0.00 | 14.17 | 195.7 (222.4) |

Only Intellect moves: **central Int 1.65 -> 1.15** (one attack power per point plus a little spell crit). Agi, Spirit and spell damage stay within 0.1 of the 11 Nov run, so the central set is now `wdps 14, Str 2, AP 1, Int 1.15, Agi 0.8 (0.6 at 15), Spi 2.5, Sta 0 (0.25 floor), SP 2.0, Exp 3, Hit% 6, Crit% 6` and the conservative set keeps `Spi 1.5, SP 1.0, Exp 1`. Order per point: weapon dps > Spirit > Str = spell damage > Int > Agi; at 40 Int and Agi are level. Applied to `weights/profiles.py`, `weights/score_items.py`, `weights/README.txt`, the Pawn string in `docs/forever-addons.md` (Intellect=1.15) and the LOF Enhancement row (Int 0.575; LOF 1.6.7 had overwritten the 8 Nov row that morning). Kill speed falls 11-13% at 25-40 and 1-2% below 25.

**Gear.** 180 quest-reward choices re-scored: three picks move, each by under 2 points and each between different slots (Bring the Light 3636: Amberglow Talisman 26.1 against Purified Ring 24.3; Roll the Bones 3882: Quarry Boots 20.9 against Utility Belt 19.0, both below what is worn; A Little Help From My Friends 4491: Clayridge Helm 55.6 against Treetop Leggings 54.5, both below what is worn). The quoted scores of Int items in chapters 19-56 were re-quoted the same day.

**Imbue and weapon at 30 / 40 (kills/hour).** Rockbiter and Windfury are level: 172.9 against 174.7 at 30, 195.7 against 195.6 at 40 (they were 198.0 / 196.6 and 222.4 / 218.2). The guide's Windfury-from-30 line stands and the model no longer leans against it. At 40 the four two-handers sit within 2%: with Windfury, Bigger Rock on Bigger Stick 198.7, The Minotaur 198.0, Bonebiter 196.9, Rage of the Storm 195.6; with Rockbiter 196.8 / 196.5 / 195.5 / 195.7. Rage of the Storm's lead over Bonebiter is gone (its +10% Stormstrike damage and 3.6 speed are worth less at 100% and 8 s); chapter 39c now says to wear Bonebiter with Windfury and bank Rage of the Storm.

**Windfury Totem with the imbue.** New since 12 Nov. On the model a Windfury Totem (level 32) next to the fight adds 4-5% kills/hour with Rockbiter and 3-4% with Windfury Weapon at 30 and 40 (totem attack power 0 to the tooltip's 95), which is more than any talent choice in the table below. It assumes the totem is carried from pull to pull (Totemic Call) so that its 115 mana is not paid every fight. Grace of Air (42, +49 Agility on the level-60 tooltip) is worth about half of that by the crit weight (an estimate, not a model run). Unverified in game.

**Talent check (`weights/talent_check.py`), kills/hour.**

| build | 25 | 30 | 40 | vs sheet at 30 / 40 |
|---|---|---|---|---|
| A sheet as written | 191.8 | 172.9 | 195.7 | |
| B Flurry 5/5 first | 191.8 | 164.8 | 197.6 | -4.7% / +0.9% |
| C Enhancement only to 40 | 191.8 | 172.9 | 202.3 | 0 / +3.3% |
| D Tidal Focus straight after Stormstrike | 191.8 | 165.7 | 197.6 | -4.2% / +1.0% |
| E Flurry in place of Improved Ghost Wolf | 191.8 | 174.3 | 197.6 | +0.8% / +1.0% |
| F sheet to 37, Flurry 5/5 in place of Mindfulness | 191.8 | 172.9 | 197.6 | 0 / +1.0% |

- **The order to 40 does not change.** Every row has the sign and about the size it had on 11 Nov. Stormstrike with its improvement is still worth 30.9 kills/hour at 40 (it was 55) and is still the best point at 25; Shamanistic Focus 30.9; the builds that delay Improved Stormstrike still lose 4-5% at 30.
- Mental Dexterity 3/3 is worth 6.8 kills/hour at 40 (2.3 per point) against Thundering Strikes' 6.7 for five points (1.3 per point): still the better talent per point.
- The Mindfulness / Improved Stormstrike stacking question is unchanged (218.7 if they stack).
- **49-54, by reasoning, not modelled.** The first point of Maelstrom Weapon now gives 6 of the 10 activations per minute at full strength, where before each point gave a fifth of the effect. Rage of the Farseer needs 30 Enhancement points and Mental Quickness 2/2 and has no Maelstrom Weapon prerequisite (WCLBox, build 70938); the sheet has 28 Enhancement points at 48. So: Maelstrom Weapon 2/5 at 49-50, Rage of the Farseer at 51 (was 54), Maelstrom Weapon 3-5 at 52-54. Applied to the sheet on 13 Nov.

**In-game test list (additions).**
1. Windfury Totem with Windfury Weapon on: do both proc (the combat log shows two different Windfury attacks)? Does the totem's attack carry its attack power?
2. Totemic Call on a Windfury Totem between pulls: range and cooldown as the sheet says (30 s)?
3. Stormstrike in the talent pane: 100% weapon damage, 8 sec cooldown.
4. Mental Dexterity 3/3: attack power on the character sheet rises by 1 per point of Intellect.
5. Maelstrom Weapon rank 1 tooltip: the chance shown for a 3.4-3.6 speed two-hander (6 per minute should read about 34-36%).
