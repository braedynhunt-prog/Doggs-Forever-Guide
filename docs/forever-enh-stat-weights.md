# Forever 2H Enhancement Dwarf Shaman — stat weights (levels 1-20)

Built 24 Sep 2026 for the "our own Pawn" project. Braedyn's brief: tune for **kill speed** (mobs per hour while grinding/questing), **1-20 in bands**, **2H Enhancement only**. Tooling at `weights\`: `enh_weights.py` (the model), `score_items.py` (scores the scraped Forever tooltips + the LW sets and compares with the guide's picks), `sensitivity.py` (flexes every uncertain input), `item_tooltips.json` (the ~200 Forever tooltips from Wowhead, 24 Sep), `scores_2026-09-24.txt` (last run), `README.txt`. Next step agreed 24 Sep, late: a data-logging addon ("DoggsProbe") that records all of this while he plays — spec in the claude.ai Project doc `claude/forever-probe-addon-spec.md`. Nothing has been checked in game yet — the "verify at the Server Slam" list at the bottom is the price of that.

## The weights (attack power = 1)

| stat | level 10 | level 15 | level 20 | notes |
|---|---|---|---|---|
| weapon DPS (2H) | 14 | 14 | 14 | exact: 14 AP = 1 DPS, and Rockbiter is AP so weapon speed does not matter before Windfury (30) |
| Strength | 2.0 | 2.0 | 2.0 | 2 AP per point for shaman |
| Attack Power | 1.0 | 1.0 | 1.0 | |
| Intellect | 0.4 | 1.05 | 1.05 | = Mental Dexterity (1 AP per Int at 3/3, from ~level 12) + a little spell crit. **The mana pool itself is worth nothing for kill speed** (see below) |
| Agility | 0.5 | 0.6 | 0.85 | crit only: 1% crit per ~6 Agi at 10, ~7 at 15, ~8 at 20 (vs 20 at 60) |
| Spirit | **1.0** (model 1.25) | **1.0** (model 0.8) | **1.0** (model 1.6) | the big surprise, and the least certain number — range 0.5-2.3 depending on Forever's regen rules and how much you drink; use 1.0 until the character sheet settles it |
| Stamina | 0 | 0 | 0 | never limits a steady grind; only deaths, multi-pulls and dungeon tanking give it value. Suggest a 0.25 floor in the addon so +Sta items aren't shown as literally worthless |
| Spell damage | **1.5** (model 2.4) | **1.5** (model 1.6) | **1.5** (model 2.7) | Earth Shock + Lightning Shield scaling; Forever's coefficients are unknown (vanilla used) — range 0.3-3.9 |
| Expertise (per point on the tooltip) | n/a | **3** (model 5.6) | **3** (model 5.2) | Forever item expertise is a *rating* (10 rating = 1% at 60). Model assumes the TBC below-60 curve (6 rating ≈ 2.6% at 20 → about 5% more swings landing from the front). If Forever doesn't scale ratings by level it's 0.8-1.2 instead |
| +1% hit or +1% crit | 2.7 | 3.8 | 6.0 | |
| mace (Dwarf Mace Specialization, +1% crit) | +3.4 | +4.3 | +7.5 | flat bonus per mace ≈ +0.25 / +0.3 / +0.5 weapon DPS. **17 Oct: the Oct 15 beta build removed weapon specializations (Dwarf Mace Spec is now Earth Fury, 2% crit damage) — this term is obsolete** |

Recommended "central" set for the addon (15-20): `wdps 14, Str 2, AP 1, Int 1.05, Agi 0.85 (0.6 at 15), Spi 1.0, Sta 0 (or 0.25 floor), SP 1.5, Exp 3, Hit% 6, Crit% 6` (mace term dropped, see above). Every reward call below was also re-run with a conservative set (Spi 0.5, SP 0.5, Exp 1) and only one call flips (Chok'sul's reward, see Disagreements).

## How the model works (so it can be argued with)

Steady-state grind loop: fight → walk/loot (9 s) → fight …, drink whenever the pool is empty. Kill speed = 3600 / (fight time + walk + drink time per fight). Weights are numeric derivatives of that per point of each stat, normalised to AP.

- **Character**: Dwarf Shaman base stats interpolated from the Classic level-1 line and wowsims/sod's level 25/40/60 tables (Dwarf offsets +2/−4/+3/−1/−1), plus the guide's own gear at each band (Coldridge Hammer at 10; Mountaineer's Greataxe + Bingles' gloves + Robe of the Keeper at 15; Smite's Hammer + the Hall of Thanes/Deadmines set at 20). Talents: Mental Dexterity 1/3 at 10, 3/3 + Thundering Strikes 3/5 at 15, + TS 5/5 + Shamanistic Focus at 20. Rockbiter R2/R3 at +63/+76/+103 AP (foreverdiff floor → Wowhead max, growing inside the rank). Result: 133 / 193 / 312 AP, 5.9 / 8.1 / 13.6% crit, 16 / 23 / 41 white DPS.
- **Melee**: AP = 2×level + 2×Str − 20 (+ Rockbiter + Int×MD); DPS = weapon DPS + AP/14; same-level mob from the front: 5% miss, 5% dodge, 5% parry, 10% glancing at 95%, crits ×2. Crit per Agi from vmangos (4.6 Agi/1% at L1), XPOff's level-19 measurement (7.7), wowsims/sod (10.3 @25, 13.95 @40, 19.7 @60).
- **Spells**: Earth Shock with Forever's cut base damage (R2 33, R3 49 — Classic was 32-34 / 60-64), 6 s cooldown, vanilla SP coefficient (0.21 / 0.30); Lightning Shield 3 orbs per fight (Forever cut ~10%); Shamanistic Focus −45% mana at 20. Spell crit ×1.5, 3% spell miss.
- **Mana/health economy**: every point of mana spent is eventually drunk back at (drink rate + Spirit regen) mana/s — Spring Water 8/s at 10, Ice Cold Milk 20/s at 15-20; Spirit regen (15-17 + Spi/5 per 2 s tick, i.e. 0.1 mana/s per Spirit, vanilla and wowsims formula) applies outside the 5-second rule: 4 s of the walk plus the whole drink. HP lost per fight (0.7×level DPS after armour, minus walking regen) is healed with Healing Wave at ~1.8 HP per mana. Because both loops are steady-state, **pool size and max HP cancel out**: a bigger pool means fewer, longer drinks, not less drinking. That's why Int is "just" Mental Dexterity and Sta is 0.
- **Policy**: the model picks the shock count per fight that maximises kills/hour. At 10-15 that is *one Earth Shock on the pull* (each extra 85-mana shock costs more drinking than the ~1.2 s of melee it saves); at 20 with Shamanistic Focus shocking every 6 s is roughly break-even, so it doesn't matter. Lightning Shield is always worth keeping up.

### Sensitivity (level 20)
Robust: weapon DPS, Str, Int, Agi (0.73-1.08 across a ±20% crit table), hit/crit. Moves a lot: **Spirit** (0.5 if Forever has no Spirit regen; 1.2 with 5 s walks; 2.3 with 15 s walks; 1.0 if the regen formula is half of vanilla), **spell damage** (1.3-3.9 with the Earth Shock coefficient 0-2×), **expertise** (1.2 flat / 3.0 TBC-points / 5.2 TBC-rating). Attacking from behind (grouped with a tank) halves expertise (2.5) since parry stops mattering. Mob level +2 raises Agi/crit/hit ~10%.

## Findings worth acting on

1. **Talent order: Mental Dexterity first, not Thundering Strikes.** At 10-12 one rank of MD is ~9 AP (a third of ~27 Int) versus ~2.3 AP-equivalent for 1% crit; even at 20 it's 43 AP vs ~6. Icy Veins' order (TS 10-14, MD 15-17) costs real damage for five levels. Recommended: MD 10-12, TS 13-17, Improved Ghost Wolf 18-19, Shamanistic Focus 20 (11 points).
2. **Spirit is a real stat for a levelling shaman.** Under vanilla regen rules a point of Spirit is worth about as much as a point of Int, because drinking is 15-25% of grind time and Spirit is the only stat that shortens it. Icy Veins ranks Spirit second to last because they think in DPS, not kills per hour. Held at 1.0 rather than the model's 1.6 until Forever's regen is confirmed (Forever runs on a modern client; nothing published says whether Spirit still regens the vanilla way).
3. **Shocks are barely worth casting while grinding at 10-19** (85 mana for 49 damage when a drink gives 20 mana/s): shock on the pull, then melee. With Shamanistic Focus at 20 it stops mattering.
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
1. **Mana regen while not casting** at a known Spirit (settles the Spirit weight: vanilla says 0.1 mana/s per Spirit + ~8/s base).
2. **Expertise %** on the character sheet with the Dwarven Tree Chopper equipped, or any +expertise item (settles rating vs points and the below-60 scaling).
3. **Rockbiter's AP** on the character sheet at 10, 16 and 20 (does it grow inside a rank?).
4. **Earth Shock tooltip with a spell-damage item on** (R3 with the +18 Fang of Magmatus: vanilla predicts ~+5; Forever moved base damage into scaling, so it may be more).
5. Crit % naked at 15 or 20 (checks the Agi table: predicted 1.7 + Agi/7.0 + talents at 15).
6. Whether Spirit regen continues while drinking (assumed yes).

## Sources
foreverdiff.com (client diff: Earth Shock, imbues, talents, totems, removed talents), Wowhead Forever spell 8017/8018/8019/10399 (Rockbiter AP) and item 2907 (Tree Chopper), wowforevertalents.com (talent text), Icy Veins Forever Enhancement guide and Dwarf race guide, Mobalytics shaman overview, warcrafttavern.com/forever/guides/stats (2 AP/Str, 20 Agi/1% crit, 15 mana/Int, 5% miss), github wowsims/forever issue #34 + base_stats_auto_gen.go (expertise 10 rating/1% at 60, crit per Agi 0.0508, base crit 1.675/2.201), wowsims/sod core/stats.go + mana.go (shaman base stats 25/40/50/60, crit per Agi/Int by level, Dwarf offsets, 15+Spi/5 regen), xpoff.com level-19 stat guide (0.13% crit and dodge per Agi, 0.055% spell crit per Int), vmangos StatSystem.cpp (AP formula, 4.6 Agi/1% at L1), magey/classic-warrior attack table (miss/dodge/parry/glancing), vanilla WoWWiki (Spirit regen table, spell coefficients, recalled — Fandom pages return 402 now).
