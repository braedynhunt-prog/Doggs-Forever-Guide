# Braedyn's decisions on the spec list (11 Nov 2026, late) and facts pulled after the specs were drafted

Every spec is revised to these. Where a decision removes or moves a quest, also fix the spec's Totals, End check, Carried in/out, Gear calls and Deviations so the file is consistent. Keep the ten-section layout. Edit your own spec file(s) in this scratchpad specs folder; the repo stays read-only for you.

## Decisions
1. **Dungeons are required chapters, not optional** (RULES.md rule 2 was changed on 11 Nov: "Dungeons are not optional. Only the grind/luck quests inside a dungeon are optional"). Chapter titles of dungeon chapters carry no `[O]`; their normal-labelled quests count in the plain totals; a grind/luck quest inside stays `[O]` (picked up, done once, abandoned if the item does not drop, never a re-run).
2. **Elites outside dungeons: always GROUP, optional.** An elite-target quest outside an instance is `[O]` `GROUP n+` and stays only when its reward is a scored gear upgrade (or a bag, food-thread recipe or gate); otherwise it is out, with every quest that needs it. Rank comes from qdb npc row [5] AND from the Wowhead classification in `wowhead_maps_20261111.txt` (qdb leaves many Forever ranks blank).
3. **Field Marshal's Log**: in, as one conditional line and block ("if the Log drops while you do Saving Sunnyglade"); no XP counted. **A Fur Trade**: in, `[O]` with the ~17-kill budget, and Friz's chain in chapter 41 as a block that depends on it. **Hail the Dragonslayer (95935): out.**
4. **Uldaman is run at level 40**, from chapter 39's Ironforge stop, not after the Badlands. **Razorfen Downs is run at level 40** on chapter 39's Barrens / Thousand Needles leg. See "Level-40 block" below for the new chapter numbers.
5. **Chapter 37 gets a Booty Bay hop** (Darkshire flight): the Bloodsail chain 595 > 597 > 599 > 604 (required level 37) as plain quests, 608 as `[O]` GROUP for the Blackwater Cap if it scores as an upgrade, Tokal's 79235 hand-in, 79236 (Cherry Grog) and the 79242 pickup.
6. **The level-40 Alterac targets move to the level-40 block**: 537 Dark Council, 522 Assassin's Contract / 523 Baron's Demise, 551 The Ensorcelled Parchment / 554 Stormpike's Deciphering leave chapter 27 and are done on the Alterac leg at 40 (the leg that visits Bath'rah). 511 > 514 > 525 stay in 27 (525's follow-up 537 is then picked up at 40).
7. **Faldir's Cove waits for level 35**: chapter 31 does 663-669 only if he is 35 on arrival; otherwise the whole cove is done on the level-40 block's Arathi stop, where 670 and 667 already are. Write both chapters so either case works.
8. **Hearth**: the route plan's sequence stands (Braedyn did not approve dropping the Booty Bay bind): Southshore (27), Booty Bay (31), Theramore (32), Nijel's Point (33), Thelsamar (35, new, proposed by the 35 spec), Farholde Keep (38). Nethergarde has no inn.
9. **Imbue at 40: Windfury** (train Windfury Weapon rank 2 as a must; the two-hander carries Windfury).
10. The 1-30 chapters are not touched by any of this.

## Level-40 block (replaces the old 36, 34b and 39)
- `39_Level40.lua` **39 Level 40: Ironforge** - the trigger (he dings 40 in the Riverglades and leaves from Farholde Keep), Eldrun's ranks, Mail, riding and the ram at Amberstill, Artisan Skinning if 200, the Ironforge pickups for Uldaman (2398 at Stormpike, 762 at Karnik after 726, 2439 if it starts there), 3636 Bring the Light at Archbishop Benedictus if the Stormwind hop is cheaper here than later (say which), ends at the Thelsamar flight.
- `39b_Uldaman.lua` **39b Uldaman** - the dungeon chapter (old spec 36), entered at 40 so 2278 / 2279 The Platinum Discs are in; hand-ins in Ironforge.
- `39c_StormHeedTempest.lua` **39c Storm, Heed, Tempest** - Arathi (Veyric: 79358 hand-in, 96135; Faldir's Cove 670 / 667 and, if not done in 31, 663-669; 95315 The Riverglades Report pickup at Captain Nials 2700; Illari's cache for 79242), then Menethil - Theramore - Ratchet and the Barrens road south to Myriam Moonsinger (6626 pickup), the Great Lift and the Heed My Call ritual.
- `39d_RazorfenDowns.lua` **39d Razorfen Downs** - the dungeon chapter (old spec 34b), placed where the road passes it (before or after the ritual: decide from the map and say why).
- `39e_Alterac.lua` **39e The Tempest's Weapons** - back to Veyric, then Southshore and Alterac: 96016 at Bath'rah (Rage of the Storm), the moved Syndicate block (537, 522 / 523, 551 / 554), the Dalaran crater hand-ins that are still open (96773 at Lan'dalock), hearth to Farholde Keep for chapter 40.
The exact split is the spec agent's to adjust if the travel says otherwise; say so under Deviations. `[NX]` order for the round: 27, 28, 29, 30, 31, 31b, 32, 33, 34, 35, 37, 38, 39, 39b, 39c, 39d, 39e, 40, 41. There is no chapter 36 or 34b any more.

## Facts pulled after the specs were drafted (files in this folder)
- `pull_extras.txt`: 95786 An Acquaintance in Southshore starts at Brother Nimetz 739 (Rebel Camp) and ends at Loremaster Dibbs (3,150 XP + 50s): pickup in chapter 30. 95789 / 95791 are side Both, Krazek to Krazek. 95799 Dibbs to Historian Karnik. 92459 is the follow-up of 92458. 94929 starts at Watcher Biggs (Swamp), ends at Demar Brant. 95315 starts at Captain Nials (Refuge Pointe), ends at Demar Brant. I'lalai Fetish 9-17% per mob (grind/luck); Saltseer artifact about 40% per mob. Noboru's Cudgel 34 of 38 kills: 1392 is plain in chapter 37. Veron Amberstill's rams: 20g and 40g rows. Groundskeeper Lomar at Arathi 27,57. Karana at Swamp 26.0,31.4.
- `riverglades_pull_results.txt` and `wowhead_maps_20261111.txt`: drop sources, ground-object and mob positions, levels and ranks for the Riverglades. Elites there: Snargl 40, Chogg'Zac 41, Overlord Kilgar 46, Komuk 45, Old Rot-Chum 42, Scaldaron 43 rare elite. Not elite: Trapclaw 42, Monstrous Threshadon 42.
- Stolen Shipment (97328) is looted from Stolen Shipment objects (661518, Stranglethorn x22.8-25.9 y8.1-13.0, 19 points): 97328 is plain in chapter 30; its prerequisite is still unverified.
- Farseer Maret Firetend (Aerie Peak) lists 163 shaman spells at Eldrun's prices (no Ghost Wolf): she is a real `[T]` stop.
- The Drowned City entrance: several community guides (Warcraft Tavern, fextralife, wowforeverleveling) give an underwater cave at about 21.4,27.9 Stranglethorn Vale, reached by swimming past the Vile Reef to the Sunken Hollow by the isle of water elementals; a large stone tablet stands beside the cave. Community-sourced, not verified in game: use it, marked unverified.
- Pauldron of Order (94926) is plate; Rot-Covered Harpoon (95120) is a polearm the shaman cannot use; Servomechanic Sledgehammer needs Engineering 100.
- Every Forever food gives +5% kill XP (known since 27 Oct, docs/audit-2026-10-27.md): it is not a reason to change the food thread. Mithril Head Trout stays the thread; Plain Ol' Paletusk (+10 Str) is an equal, Cooked Glossy Mightfish (+30 AP, Cooking 225) the next step up.
- When chapter 34 (Scarlet Monastery) is run, it ends in Ironforge and chapter 35 starts there.

## Level on entry (plain quests + dungeon quests, 65% quest share; recomputed by the main session after this pass)
27: 31.0 | 28: 31.5 | 29: 31.9 | 30: 32.3 | 31: 33.3 | 31b: 33.8 | 32: 34.2 | 33: 35.0 | 34: 36.1 | 35: 36.4 | 37: 37.2 | 38: 37.7 | 39 block: 40 by definition | 40 and 41: 40-42. Dungeon runs add kill XP this estimate does not count, and he ran three levels ahead of the 1-30 guide. Each chapter opens with a level-check line: "this chapter wants level N" (N = the highest required level among its plain quests, or the level its mobs need), and what to do if he is under it (the previous dungeon chapter, or carry the named quests forward).

## Report back
A short list only: what changed in each spec file (quests moved in/out with ids, new totals: plain count, plain XP, optional XP, money), anything a decision made impossible, anything still unsure. No full chapter report.

## Addendum 2 (Braedyn, 11 Nov, after the reconciled list): the level-40 block is reordered and renamed
On quest XP he leaves Riverglades I (chapter 38) at about 38.2, not 40, so the block no longer starts with the level-40 Ironforge stop. The block now starts when chapter 38 is finished, whatever his level. The main session renamed the spec files to the play order:

| play order | new file | chapter | was |
|---|---|---|---|
| 1 | 39.md (`39_StormHeedTempest.lua`) | Storm, Heed, Tempest: Arathi, Faldir's Cove, the Barrens road, the Heed My Call ritual | 39c.md |
| 2 | 39b.md (`39b_RazorfenDowns.lua`) | Razorfen Downs | 39d.md |
| 3 | 39c.md (`39c_Alterac.lua`) | The Tempest's Weapons: Veyric, Faldir's Cove's last legs, Alterac, Rage of the Storm; ends in Ironforge | 39e.md |
| 4 | 39d.md (`39d_Level40.lua`) | Level 40: Ironforge (and the Stormwind tram): training, Mail, riding and the ram, the Uldaman pickups | 39.md |
| 5 | 39e.md (`39e_Uldaman.lua`) | Uldaman; ends with the Ironforge hand-ins and the hearth to Farholde Keep | 39b.md |

`[NX]` order for the round: 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 39b, 39c, 39d, 39e, 40, 41. Every reference to the old labels inside a spec must be changed to the new ones.

Consequences to write in:
- **Start of the block**: from Farholde Keep fly Lakeshire - Stormwind (stop: 3636 Bring the Light at Archbishop Benedictus **only if he is level 39**, its required level; if he is 38 it is skipped and Razorfen Downs runs without it; 94893's hand-in if the Field Marshal's Log chain is in the log), then on to Refuge Pointe (through Ironforge). No training stop here.
- **Faldir's Cove is always done in the block** (single path; chapter 31 no longer touches it): 663-668 and the 669 pickup on the first Arathi visit (new 39); 669 handed in and 670 taken at Seahorn in Booty Bay on the way back from Kalimdor (the Ratchet - Booty Bay boat); 670 and 667 at the cove on the second Arathi visit (new 39c). Drop every "Case 1".
- **3636 and 96773** are handed in after Razorfen Downs: 96773 at Lan'dalock on the Alterac leg (new 39c), 3636 at Benedictus on new 39d's Stormwind tram trip (3636 only if it was picked up).
- **New 39c ends in Ironforge** (554 hand-in) and **new 39d starts there**: level-check "this chapter wants level 40": Windfury Weapon rank 2 and the other level-40 ranks, Mail (SkillRaceClassInfo row 145), Apprentice Riding and the ram; if he is still 39 he trains what he can, runs Uldaman (the Platinum Discs 2278 / 2279 need 40 at pickup: say what to do at 39) and returns to train. Uldaman pickups in new 39d: 2398 The Lost Dwarves (Prospector Stormpike) and 1360 Reclaimed Treasures (Krom Stoutarm). 762 and 1139 stay out and the amulet chain 722-726 stays the one-kill optional (Braedyn was asked; unless he says otherwise this stands).
- **New 39e (Uldaman) starts at Thelsamar** after new 39d, ends with the Ironforge hand-ins, then the hearth to Farholde Keep; chapter 40 starts there.
- Rage of the Storm is taken in new 39c at about 39.4 on quest XP: check its required level in the tooltip (weights/tooltips/2026-11-11.json, id 280604) and say what he swings until he can equip it.
- Facts from the last pull (pull_extras.txt, third section): The Lost Magic of the Runemasters and The Coldbringer's Eye are ground objects (96800 and 96773 are normal quests); Blademaster Kaijo is a level 42 elite (95912 out); Gronok the Butcher (44) and Admiral Lamora (45) are not elite; Farholde Scouts stand from 44.2,63.6.
- Chapter 40 stays thin on purpose (Braedyn: "if we have enough XP then leave it out").
