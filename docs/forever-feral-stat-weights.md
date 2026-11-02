# Forever Feral Druid (bear 10-20, cat from 20) - stat weights (levels 1-30)

Written 2 Nov 2026 for the Skyborne Druid variant of the guide (Phase 0: tooling and variant skeleton); weapon dps added the same day from Blizzard's Forever class deep dive. **These weights are reasoning only.** No kill-speed model sits behind them (unlike the shaman's, `docs/forever-enh-stat-weights.md`): they are starting numbers so the gear generator can make consistent calls. Tooling: `weights/feral_weights.py` (the numbers and the usable rule), `weights/profiles.py` (profile `feral`), `tooling/gear_calls.py --profile feral`, `tooling/dungeon_loot.py --profile feral`. Nothing has been checked in game.

The route levels in Bear Form from 10 to 20 and in Cat Form from 20. Bands 10 and 15 use the bear set, bands 20, 25 and 30 the cat set (each chapter takes the band nearest its starting level, as for the other profiles).

## The weights (attack power = 1)

Reasoning:
- **Verified** (Blizzard, World of Warcraft Forever class deep dives: Hunter and Druid, https://news.blizzard.com/en-us/article/24301515/world-of-warcraft-forever-class-deep-dives-hunter-and-druid): form auto-attack dps **equals the equipped weapon's dps** (each form has a fixed attack speed), Rake and Swipe scale with attack power, and Cat Form gives "+12 AP plus Agility". So weapon dps is a first-order stat in every band, weighted at the Classic conversion **1 dps = 14 AP** (10 in the conservative set). Staves and 2H maces get no bias over 1H maces, daggers and fist weapons beyond their dps and stats.
- **Assumed (Classic, unverified on Forever):** 2 AP per Strength in forms; 1 AP per Agility plus crit (and armor and dodge in Bear Form); Bear Form takes 180% of item armor.
- Feral attack power on gear ("+N Attack Power in Cat, Bear, and Dire Bear forms") counts as plain AP (parser key `feral_ap`; the shaman and warrior scorers never read it).

### Bear (bands 10, 15)

| stat | central | conservative | notes |
|---|---|---|---|
| weapon dps (main hand / 2H) | 14 | **10** | form auto-attack = weapon dps (deep dive) |
| Strength | 2 | 2 | 2 AP per point in forms (Classic, unverified) |
| Attack Power (incl. feral AP) | 1 | 1 | Swipe scales with AP (deep dive) |
| Stamina | 1.5 | **1.2** | survival while pulling two or three mobs solo in Bear Form |
| Agility | 1.2 | **1.0** | 1 AP + crit + armor + dodge |
| Armor (per point, base + bonus) | 0.05 | **0.03** | Bear Form takes 180% armor from items; leather beats cloth of the same stats |
| +1% crit | 6 | **4** | |
| +1% hit | 8 | 8 | |
| Intellect | 0.3 | 0.3 | shifting costs mana; a little mana for heals between pulls |
| Spirit | 0.2 | 0.2 | regen between pulls |
| ranged dps, Defense, block, dodge %, parry %, expertise, spell power | 0 | 0 | |

### Cat (bands 20, 25, 30)

| stat | central | conservative | notes |
|---|---|---|---|
| weapon dps (main hand / 2H) | 14 | **10** | form auto-attack = weapon dps (deep dive) |
| Strength | 2 | 2 | 2 AP per point in forms (Classic, unverified) |
| Agility | 1.6 | **1.3** | Cat Form: "+12 AP plus Agility" (deep dive) + crit |
| Attack Power (incl. feral AP) | 1 | 1 | Rake scales with AP (deep dive) |
| Stamina | 0.6 | 0.6 | less needed than in Bear Form |
| +1% crit | 8 | **5** | |
| +1% hit | 10 | 10 | |
| Intellect | 0.2 | 0.2 | |
| Spirit | 0.2 | 0.2 | |
| Armor, ranged dps, Defense, block, dodge %, parry %, expertise, spell power | 0 | 0 | |

A gear call is flagged when the central and conservative sets pick different items.

## What a feral druid can use (1-30) - `feral_weights.usable()`
- Armor: **cloth and leather in every slot**; no mail, no plate. Neck, rings, trinkets and cloaks count.
- Weapons: staves, 1H and 2H maces, daggers, fist weapons. No axes, swords, polearms, wands, off-hand weapons (no dual wield).
- Held-in-off-hand items (orbs, tomes) and **idols** (relic slot). Totems and librams parse with no slot and stay "not equipment".
- No shields and no ranged slot (bows, guns, crossbows, wands, thrown). A druid has no pull slot, so the profile has no secondary slot (`SECONDARY = None`).
- Client-table filter for dungeon loot (`profiles.FERAL_USABLE`): Item.csv weapon subclasses 4 / 5 (1H / 2H mace), 10 (staff), 13 (fist), 15 (dagger); armor 1 cloth and 2 leather in every slot, 0 misc as neck / ring / trinket / held in off-hand (InventoryType 2, 11, 12, 23), 8 idol (InventoryType 28).

## Examples on the 1 Nov 2026 tooltips (central / conservative)
From `gear_calls.py --profile feral --variant tooling/variants/skyborne_druid/variant.json --emit` (scratch run, 2 Nov 2026, weapon dps 14 / 10):
- Bear, band 10 weapon: **Novice's Quarterstaff** (staff 2.7 dps, quest 92470 Foul Matriarch) 37.52 / 26.8, over Scout Ranger's Dagger 28.0 and Peacekeeper's Pickhammer 27.44; **Stained Ritual Dagger** (dagger 4.4 dps, quest 92528 Among the Faithful) 61.74 / 44.1.
- Bear, band 15 weapon: **Ironforge Greathammer** (2H mace 16.0 dps, quest 96393 Old Ironforge Incursion) 223.58 / 159.7.
- Bear, band 15 armor: **Catacomb Cloak** (cloak +2 Sta +7 AP, quest 96395 An Ancient Grudge) 10.75 / 9.85; **Frontier Britches** (leather legs +3 Str +3 Agi, quest 217 In Defense of the King's Lands) 12.8 / 10.92.
- Cat, band 20 weapon over armor: **Staff of Westfall** (staff 15.2 dps +5 Int +6 Spi, quest 166 The Defias Brotherhood) 214.58 / 153.9, over Tunic of Westfall (leather chest +11 Agi +5 Sta) 20.6 / 17.3. Like the shaman's, a weapon's score includes 14 x dps: it says the weapon is strong for its slot, not that it beats the weapon already worn.
- Cat, band 20 armor: **Smith's Trousers** (leather legs +4 Str +4 Agi, quest 89 The Everstill Bridge) 14.4 / 13.2.
- Cat, band 30: **Heavehammer** (2H mace 27.7 dps +32 AP, quest 98824 Prehistoric Prism) 420.22 / 309.3, over Healer's Staff (20.8 dps +12 Sta) 297.98; **Triprunner Dungarees** (leather legs +3 Str +18 Agi +6 Sta, quest 2929 The Grand Betrayal) 38.4 / 33.0; **Raptorbane Armor** (leather chest +3 Sta +31 AP, quest 296 Ormer's Revenge) 32.8 / 32.8.

Emitter counts on that run: 115 quests with reward choices - 95 picks, 4 coin flips, 4 nothing, 10 not gear, 2 unstated (missing tooltips); 54 dungeon loot groups; 21 item ids without a tooltip (`tooling/variants/skyborne_druid/missing_tooltips.txt`). Against the first run (weapon dps 0) 10 of 115 calls changed, all toward weapons.

## How the generator words the picks
`tooling/gear_calls.py --profile feral --variant tooling/variants/skyborne_druid/variant.json --emit <file>` writes one line per quest with reward choices, in the guide's style: `[OC][A Druid] |cffffcc00Gear:|r take |cff66ff66Smith's Trousers|r (leather legs +4 Str +4 Agi)`; "X or Y, coin flip" when the runner-up is within 10%; "nothing for a druid - vendor" when nothing usable scores; no line for bag/potion/food-only rewards or when a tooltip is missing. Only stats with a non-zero weight in the chapter's band are quoted (armor is never quoted outside shields, so an armor-only piece reads "leather chest"); feral attack power is quoted as "+N AP in forms". Idols are worded "idol", held items "held in off-hand". The report headers print the bear (10/15) and cat (20/25/30) sets on two lines.

## Verified
- Form auto-attack dps = the equipped weapon's dps, fixed attack speed per form; Rake and Swipe scale with AP; Cat Form gives "+12 AP plus Agility" (Blizzard class deep dive, URL above).

## Open until checked in game
**Unverified on Forever:**
1. **Strength to AP in forms** (2 per point assumed, Classic).
2. **Feral attack power wording.** The 1 Nov 2026 tooltip cache has no item with form-only attack power, so the parser matches both Classic wordings ("+N Attack Power in Cat, Bear, and Dire Bear forms only." and "Increases attack power by N in Cat, Bear, Dire Bear, and Moonkin forms only."). The real Forever wording has not been seen.
3. **Form attack speeds 1.0 (cat) / 2.5 (bear)**: seen only in a search snippet, not on the page itself. They do not change the dps weight (dps is what the form uses), but they matter for any later kill-speed model.
4. **Feral Charge and Primal Bite are talents on Forever** (Blizzard's class deep dive; Wowhead tooltips list 20 / 40), not trained spells; whether a Cat-Form Feral Charge build changes the Str/Agi balance (or the bear-to-cat switch at 20) is not known.
5. The Str / Agi / crit exchange rates at levels 10-30 and the 180% Bear Form armor on Forever.
6. Whether the Skyborne racials change anything worth weighting (not modelled).
7. A kill-speed model like `enh_weights.py` for bear and cat, if the gear calls look wrong in play.
