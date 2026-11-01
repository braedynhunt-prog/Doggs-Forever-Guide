# Forever Protection Warrior (1H + shield) - stat weights (levels 1-30)

Written 1 Nov 2026 for the Skyborne Protection Warrior variant of the guide (`docs/warrior-build-plan-2026-11-01.md`, Phase 0). **These weights are reasoning only.** Unlike the shaman's (`docs/forever-enh-stat-weights.md`), no kill-speed model sits behind them yet: they are the plan's starting numbers, set from the Classic warrior formulas and the levelling priority quoted by the Forever guides (weapon dps > Str/AP > Sta > Agi > Armor; Defense low while levelling), and they exist so the gear generator can make consistent calls. Tooling: `weights/prot_weights.py` (the numbers and the usable rule), `weights/profiles.py` (profile `prot`), `tooling/gear_calls.py --profile prot`, `tooling/dungeon_loot.py --profile prot`. Nothing has been checked in game.

## The weights (attack power = 1, every band 10-30)

| stat | central | conservative | notes |
|---|---|---|---|
| 1H weapon DPS | 6 | 6 | 14 AP = 1 DPS is the white-damage exchange rate, but a tank's damage is mostly abilities with flat bonuses (Revenge, Heroic Strike, Shield Slam at 30) and rage, not white swings, so weapon dps is discounted to about 40% of the enh value. Shield builds swing a slow-ish 1H; speed is ignored |
| ranged weapon DPS | 1 | 1 | the ranged slot pulls, it barely fights. Counted as a secondary slot: a ranged weapon is "best" only when no other reward is usable |
| Strength | 2 | 2 | 2 AP per point for warriors (Classic), plus block value from Str in Classic (1 per 20 Str, ignored) |
| Attack Power | 1 | 1 | |
| Stamina | 1.5 | **1.0** | survival while pulling two or three mobs solo and in dungeons; rage from damage taken is pre-mitigation in Forever, so Sta does not cost rage. The conservative set halves the premium over AP |
| Agility | 0.9 | 0.9 | crit (Classic ~20 Agi per 1% at 60, much less at low level) + 2 armor per point + a little dodge |
| Armor (per point, base + bonus) | 0.03 | **0.02** | ~100 armor = 3 AP. Makes mail beat leather of the same stats by a few points per slot, which is the intent (mail at any level for a warrior) |
| Defense (per point) | 1.5 | **1.0** | 0.04% each to miss/dodge/parry/block and crit reduction; low value while levelling, real in dungeons. The Guard's mail set carries +3..+7 |
| Block value (per point) | 0.5 | 0.5 | the "N Block" on shields and "+N Block Value" |
| Block chance (per 1%) | 3 | 3 | more Shield Specialization rage procs (Forever: rage on block) |
| Dodge / Parry (per 1%) | 4 | 4 | avoidance + Master of Defense rage (Forever talent) |
| +1% hit | 6 | 6 | |
| +1% crit | 4 | 4 | |
| Expertise (per point on the tooltip) | 2 | 2 | rating; the scaling below 60 is unknown (same open question as the shaman's) |
| Intellect / Spirit / spell power | 0 | 0 | |

Conservative set = central with Sta 1.0, Defense 1.0, Armor 0.02 (less credit for survival stats while solo levelling). A gear call is flagged when the two sets pick different items.

## What a prot warrior can use (1-30) - `prot_weights.usable()`
- Armor: **mail at any level**, leather, cloth only as a cloak; no plate (40). Neck, rings and trinkets count.
- Weapons: 1H axe, mace, sword, dagger, fist weapon; **never a 2H**; no staves, polearms, wands, held-in-off-hand items or off-hand weapons (the off hand is the shield).
- Shields (any).
- Ranged: bow, gun, crossbow, thrown - the pull slot, secondary.
- Client-table filter for dungeon loot (`profiles.PROT_USABLE`): Item.csv weapon subclasses 0/4/7/13/15 (1H), 2/3/18/16 (ranged), armor 3 mail, 2 leather, 6 shield, 1 cloth cloaks only, 0 misc neck/ring/trinket.

## Examples on the 1 Nov 2026 tooltips (central / conservative)
- Guard's mail set (Blacksmithing, BoP; scored as a reference only - the route's professions are Skinning + Mining, decided 1 Nov 2026, so none of these is crafted on the route): Belt +4 Str +4 Sta Def +3 21.4 / 17.0; Gloves +5 Str +5 Sta Def +3 25.4 / 20.3; Chain Shirt +4 Str +7 Sta Def +5 31.5 / 23.7; Boots +5 Str +5 Sta Def +4 27.4 / 21.6; Chain Leggings +5 Str +9 Sta Def +7 39.3 / 29.5; Silvered Chain Helm +10 Agi +9 Sta 27.4 / 21.3.
- Fire Hardened Hauberk (Furen's Armor) +5 Str +14 Sta 37.5 / 28.4.
- Shields: Stormforged Protector (94003, 311 armor 5 block +1 Str +1 Sta) 15.3 / 11.7; Ironplate Buckler 12.3 / 9.1; Dwarven Defender 18.3 / 13.2; Gold-plated Buckler (Deadmines) 29.6 / 22.0.
- Weapons: Smite's Reaver (1H axe 13.9 dps +3 Str) 89.7; Cookie's Tenderizer (1H mace 13.9 dps) 83.6. As with the shaman, a weapon's score is large because it includes 6 x dps: it says the weapon is good for its slot, not that it beats armor.
- Smith's Trousers (leather +4 Str +4 Agi) 13.6 / 13.0.

## How the generator words the picks
`tooling/gear_calls.py --profile prot --variant tooling/variants/skyborne_warrior/variant.json --emit <file>` writes one line per quest with reward choices, in the guide's style: `[OC][A Warrior] |cffffcc00Gear:|r take |cff66ff66Guard's Gloves|r (mail hands +5 Str +5 Sta, Def +3)`; "X or Y, coin flip" when the runner-up is within 10%; "nothing for a warrior - vendor" when nothing usable scores; no line for bag/potion/food-only rewards or when a tooltip is missing (listed for `fetch_tooltips.py --from-file`). Only stats with a non-zero weight are quoted.

## Open until checked in game
1. Rage per hit taken and per block / dodge / parry with the Forever talents (decides Sta, block and avoidance against Str).
2. Defense's real value at 20-30 (character sheet: miss/dodge/parry/block % before and after a Guard's piece).
3. Expertise rating to % below 60.
4. Whether the Skyborne racials (+2% haste, +5% vs Elementals) change anything worth weighting (not modelled).
5. A kill-speed model like `enh_weights.py` for the prot rotation, if the gear calls look wrong in play.
