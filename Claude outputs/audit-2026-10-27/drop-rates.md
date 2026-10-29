# Drop-rate audit: Forever Alliance guide, levels 1-30 (27 Oct 2026)

**Short answer:** yes, there are rare-drop farms on the route, but only a handful.
- **Genuine low-drop farms:** three. One is required: 98407 Show of Force (about 59 kills). Two are optional: 86757 Slowing the Orc Advance (about 250 kills for the daggers) and 95217 The Quarry's Smith (about 163 kills). A fourth, 92909 Harvesting the Harvesters, is already [O] and labelled.
- **Wrong drop source:** two required quests send you to a mob that (per the Forever DB and Wowhead) doesn't drop the item, so as written they never finish. These are 95212 Never Saddle on Quality and 91777 Rare Books.
- **Suspect numbers:** two required dungeon-boss quests show low Wowhead Forever figures that are probably sampling artifacts. Check them on the first kill.
- **Classic quests:** every Classic-era collection is an ordinary 30-50% drop. The worst takes about 25 kills (41 for Redridge Goulash, split over three mobs).

## Summary

| | Count |
|---|---|
| Quests whose objective is a mob-dropped item | **148** (174 item rows) |
| Of those: single drops from a named mob or boss | 74 |
| Of those: multi-item collections | 74 |
| Required by the route | **117** (113 required, plus 4 picked up on the route with an [O] hand-in) |
| Optional [O] | 31 |
| **Flagged** | **18**: 15 required, 1 required with an optional hand-in, 2 optional |
| Required quests with no drop rate anywhere (new Forever items) | 15, listed in section C |

A quest is flagged when the rate is under about 25%, when it needs about 20 or more kills with no overlapping kill quest, or when the guide names the wrong drop source. Expected kills = count / rate.

**Top 10 worst:**

| # | Quest | Ch | Req | Problem | Expected kills | XP |
|---|---|---|---|---|---|---|
| 1 | 98407 Show of Force | 06 | **R** | 5 Spiked Collars at **8.44%**, Redridge Thrasher, 12 spawns | **~59** (79 for 80% confidence) | 950 |
| 2 | 95212 Never Saddle on Quality | 01b | **R** | **Wrong mob**: the guide targets Snow Leopard (1201). Only Elder Snow Leopard (260157) drops the pelt, at 41.7%. | never as written (~14 on the right mob) | 630 |
| 3 | 91777 Rare Books (Human route) | 00b | **R** | **Wrong source**: the Arcane Explainer drops only from Mother Fang (a rare with one spawn point), at 26.4%. The guide says Defias Rogue Wizards drop it. | ~4 kills of a rare spawn | 790 |
| 4 | 86757 Slowing the Orc Advance | 21 | O | 4 daggers at **1.6%**; 6 swords at 12.05% | **~250** / ~50 | 2550 |
| 5 | 95217 The Quarry's Smith | 01b | O | 4 Toughened Boar Hides at **2.45%**, Scarred Crag Boar only | **~163** | 630 |
| 6 | 95250 Abominable Creatures | 08 | **R** | Head of the Baron at 15.1% (dungeon boss) | ~7 runs if the figure is real | 1650 |
| 7 | 96264 Elemental Aid (Shaman) | 25/26 | **R** | Tattered Note at 0.7% (Charlga Razorflank) | probably an artifact; true rate unknown | 2650 |
| 8 | 92 Redridge Goulash | 06 | **R** | 5+5+5 items at 35-38% on three mob types | ~41 total | 1350 |
| 9 | 150 Murloc Poachers | 10 | **R** | 8 Murloc Fins at ~31% | ~26 | 1550 |
| 10 | 22 Goretusk Liver Pie | 05 | **R** | 8 livers at 32.4% | ~25 | 910 |

## Sources and reliability

- **classicdb.ch** item pages (`https://classicdb.ch/?item=<id>`, "Dropped by" tab), fetched 27 Oct.
  - Decimal values are sampled rates (marked `cdb`).
  - Round values (80, 100, 66, 50, 45, 40, 33, 10%) are emulator defaults and only approximate (marked `cdb*`).
- **Wowhead Forever tooltips** (`https://nether.wowhead.com/forever/tooltip/item/<id>`) carry a measured "Drop Chance" for some single-dropper Forever items (marked `WH-F`).
  - Wowhead divides by every looted kill, including players without the quest, so for quest-only items these are lower bounds.
  - The distortion is worst for bosses and class quests (the 0.7% and 15.1% figures).
- **Not reachable:** Wowhead item and quest pages, warcraft.wiki.gg and metaforge returned 202/403 to scripted fetches, so there was no cross-check against Wowhead Classic's drop tab.
- **Forever rate changes:** none found.
  - Wowhead lists the 108 Classic quests here as unchanged (81) or updated (27), and none of the updates touch objectives or counts.
  - Warcraft Tavern (26 Sep 2026, https://www.warcrafttavern.com/forever/news/quest-drops-distribute-more-evenly-in-wow-forever/) quotes Aggrend: quest items are now handed out round-robin inside a group (still being tuned), and "quest drop mechanics are otherwise unchanged". In a duo, plan on roughly the solo kill count each.
- **Beta comments** in `data/quests.json`:
  - Only two mention rates. 92909: "might be the worst quest off all time. never seen a lower drop rate anywhere". 95212: "the worst out of any Dun Morogh quest I did in the beta, but it was still quite trivial".
  - On 98326 Frosthowl, one comment says not every party member got the Sack of Fish on the first kill.
- The guide's "kami-labs 5.5%" for Shadetooth (98815) is unverified.

## A. Flagged quests, worst first (recommendations only)

**Tier 1: real low-drop farms and wrong sources**

1. **98407 Show of Force** (06_Redridge, lines 13/44/50, **required**, 950 XP)
   - 5 collars at 8.44% (WH-F) from Redridge Thrasher (L14-15, 12 spawns): about 59 kills. 30 kills finish it only 10% of the time.
   - No other quest on the route kills Thrashers.
   - Line 11 has you kill Thrashers before line 13 accepts the quest, and collars can't drop before the quest is accepted.
   - **Recommendation:** make it [O] with "stop at ~15 Thrashers", or drop it. Move the line-11 kills to after the accept.
2. **95212 Never Saddle on Quality** (01b, lines 142/169, **required**, 630 XP)
   - Line 169 targets TAR1201 Snow Leopard at 62,58.
   - The Forever DB's only dropper is 260157 Elder Snow Leopard (L9-10, x65-82 y52-62). The Wowhead tooltip agrees: "Dropped by: Elder Snow Leopard, 41.68%".
   - On the right mob that is about 14 kills (18 for 80% confidence).
   - **Recommendation:** retarget the line to TAR260157 around 75,57. There is no rate problem once that's fixed.
3. **91777 Rare Books** (00b, lines 58/91/94, Human route, **required**, 790 XP)
   - Line 94 says Defias Rogue Wizards drop the Arcane Explainer. The DB's only dropper is 471 Mother Fang: rank 4 (rare), one spawn point at Jasperlode 62.1,48.0. Wowhead agrees at 26.41%.
   - Geomancy for Curious Young Wizards also comes from one named mob, 248474 Geosculptor Yip (61.4,48.9), at 47.4%. Line 91 targets Kobold Geomancers in general.
   - **Recommendation:** point line 91 at Yip and line 94 at Mother Fang. Make the Explainer half [O] with "only if Mother Fang is up".
4. **86757 Slowing the Orc Advance** (21, lines 16/17/34, optional, 2,550 XP)
   - Swords: 6 at 12.05% from Horde Grunts (13 spawns), about 50 kills.
   - Daggers: 4 at 1.6% from Horde Scouts, about 250 kills.
   - The guide's ~30-kill budget finishes it about 0% of the time.
   - **Recommendation:** drop it from the route.
5. **95217 The Quarry's Smith** (01b, lines 157/165, optional, 630 XP)
   - 4 hides at 2.45% (WH-F) from Scarred Crag Boar only (32 spawns): about 163 kills.
   - The line just says "(boars)".
   - **Recommendation:** drop it, or "hand in only if the hides drop by chance".
6. **95250 Abominable Creatures** (08, lines 39/43/51, **required**, 1,650 XP)
   - Head of the Baron at 15.14% (WH-F). This is probably sample bias, since boss quest items are normally 100%. The guide labels it "normal".
   - **Recommendation:** keep it, and add "if no head, don't re-run" until it's confirmed in game.
7. **96264 Elemental Aid** (Shaman; 25 line 67, 26 lines 16/57/84, **required**, 2,650 XP)
   - Tattered Note at 0.70% (WH-F). Nearly all Wowhead loots of Charlga come from non-Shamans, so the true rate is **unknown**.
   - **Recommendation:** keep it, and add "one kill; no note, then abandon".

**Tier 2: Classic collections needing about 20+ kills with no overlapping kill quest**

All of these are normal Classic drops. Recommendation for every row: **keep**, and add a kill budget to the line.

| Quest | Ch | Req | XP | Items | Rate | Exp. kills | Note |
|---|---|---|---|---|---|---|---|
| 92 Redridge Goulash | 06 | R | 1350 | 5 snouts, 5 condor meat, 5 spider meat | 36.4 / 35.1 / 38.4% cdb | 14+14+13 = **~41** | known Classic slog; budget "~15 of each" |
| 150 Murloc Poachers | 10 | R | 1550 | 8 fins | 31.0% cdb | **~26** (80%: 32) | labelled "normal" |
| 22 Goretusk Liver Pie | 05 | R | 910 | 8 livers | 32.4% cdb | **~25** (80%: 30) | the Westfall Stew snouts come from the same boars |
| 127 Selling Fish | 06 | R | 1250 | 10 Spotted Sunfish | 45% cdb* | ~22 | |
| 11 Riverpaw Gnoll Bounty | 00b | R | 840 | 8 armbands | 40% cdb* | ~20 | Human route |
| 47 Gold Dust Exchange | 00b | R | 630 | 10 Gold Dust | 50% cdb* | ~20 | about 20 Fargodeep kobolds also covers Candles (~12) and Lost Books |
| 2928 Gyrodrillmatic Excavationators | 18/24 | R | 2450 | 24 Robo-mechanical Guts | 80% cdb* | ~30 | 16+ Gnomeregan mob types; already says "grind warning" |

**Tier 3: single named or boss drops under 70%** (expect a second kill or a respawn wait)

- 86758 Twisting the Knife (02, R, 1150 XP): 42.6% WH-F from Daggerfang, a roaming named mob. About 2.3 kills; the chapter 04 retry already covers it. Keep.
- 96393 Old Ironforge Incursion (Hall of Thanes, R, 1450 XP): 58.1% WH-F. Keep, with "check you looted it".
- 95646 Horrors in the Highland (Excavation Site, R, 3150 XP): 64.3% WH-F. Keep.
- 1142 Mortality Wanes (RFK, required pickup, optional hand-in, 3050 XP): 10% cdb*. Already says "luck, do not farm". Keep.

Not flagged: Shinyfinder Narf 65.5%, Nimsy 62.3% and Frosthowl 66.8% are named open-world drops, and those figures are probably biased low.

## B. Quests from the owner's list

- **Thelsamar Blood Sausages (418):** 3 of each item. Boar Intestines 31.6%, Bear Meat 41.9%, Spider Ichor 35.6% (all cdb). About 9 + 7 + 8 = ~25 kills. OK.
- **Red Leather Bandanas (153):** 15 at 80% (cdb*), about 19 kills. The People's Militia quests already kill 30 Defias, so it's fully covered.
- **Red Silk Bandanas (214):** Deadmines trash at 80%. OK.
- **Killing Fields harvester parts:** these are 92909/92911, optional, rate unknown, with the beta "worst drop rate" comment. Already [O] and labelled. Okra (33%) and Flask of Oil (34.8%, ~14 kills) fit inside the 20 Watchers Killing Fields already kills.
- **Gold Dust Exchange, Goretusk Liver Pie, Redridge Goulash:** see tier 2.
- **Tharil'zun (19), WANTED: Chok'sul (256):** elite heads at 100%. These are group gates, not drop problems.
- **Rime's Wrath (99161):** Avala's Core from a single named mob. Forever item, rate unknown.
- **Stolen Blasting Powder (95213/95214):** Forever items, rate unknown.
  - The Empty Powder Keg that starts the chain and 16 Blasting Powder both come from Rockjaw Ambushers and Backbreakers (24 spawns).
  - This is the largest unknown-rate count on the route. Suggest a "stop at ~40 kills" note.
- **Gnogaine (2926) and Green Glow (2962):** you fill a phial by using it on the mob; nothing drops. Not a drop risk.
- **Essential Artificials, Bathran's Hair and the Loch Modan Excavation chain** (436, 298, 273, 305, 306, 86613): object or delivery quests. No mob drops.
- **Night Watch, Wolves at Our Heels, A Hunter's Boast:** kill counts only.
- **The Reports, Stormpike's Delivery, Daily Delivery:** deliveries.
- **Stockade, The Color of Blood (388):** 10 bandanas at 80%. OK.
- **Not in the guide at all:** Chen's Empty Keg, Ice Claw Bear, Ironband's Compound, Ironband Wants You!, Bailor's Ore, the Buzzbox quests, Bashal'Aran.

## C. Required quests with no rate available (watch in game)

- 91743 Rascally Rodents: 8 Stolen Books. Overlaps 32 required kobold kills.
- 91775 Book Return: 6 Lost Books.
- 99130 An Enticing Offer: 6 Vials of Animal Blood.
- 95214 Stolen Blasting Powder: 16.
- 99161 Rime's Wrath: 1 core.
- 94373 Call of Earth (Shaman): 2 pendants. Overlaps 14 Troll Cave kills.
- 94466 Call of Fire (Shaman): Fire Tar and Reagent Pouch, one each.
- 92744 Murloc Gills: 7.
- 98072 Crocs of the Sky: 8 scales, about 70 spawns.
- 98245 Razormaw Needling: 10 incisors, about 59 spawns.
- 98282 Alchemical Hazards: 1 gland. Already labelled.
- 98815 Highland Hides: 4 hides. Already labelled, with an abandon line.
- Drops that start required chains:
  - the Nibbled-On Book (starts 91741)
  - the Empty Powder Keg (starts 95213)
  - the Dark Iron Map (starts 96391, which leads to 96393; the line says "keep killing until it drops" on 12 Dark Iron Spies)

## D. Lines that already warn about drops

- **01b_DunMorogh:169** — 95212: "low drop rate, don't camp it".
- **05_Westfall:28 and :34** — 92909: "worst drop rate in the zone", "very low drop".
- **10_Redridge2:57** — 115 Shadow Magic: "Label - slow".
- **10_Redridge2:61** — 91 Solomon's Law: "Label - slow".
- **11_Darkshore:36, :41, :52, :62, :77, :78, :106** — 87760, 1138, 986, 2098, 98042, 968, 98028: "no stated rate, do not farm".
- **12_Ashenvale:32** — 1023: rate not in the DB.
- **12_Ashenvale:51** — 1016 Elemental Bracers: "about 20 kills" (cdb* gives 80%, so about 6 kills).
- **13_Blackfathom:11 and :14** — 1275 and 1199: rate not in the DB.
- **14_Duskwood:7 and :20** — 101: rate not in the DB.
- **15_Stockade:28** — 968: skip it without the book.
- **15_Stockade:40** — 388: rate not in the DB.
- **16_RedridgeEastvale:29** — 347 Rethban Ore: "unknown drop rate, optional".
- **16_RedridgeEastvale:47** — 178 Glowing Shadowhide Pendant: "never farm".
- **17_Duskwood2:37, :47, :59, :65** — Ira's Dagger, Rot Blossoms, Merrick's Bow, Ghoul Ribs.
- **18_Wetlands1:13 and 24_Gnomeregan:50** — 2928: "grind warning".
- **18_Wetlands1:26 and :70** — 470 Sida's Bag: "~10 minutes".
- **18_Wetlands1:37** — 324 Lightforge Ingots.
- **18_Wetlands1:44** — 471 Giant Crocolisk Skins: "budget ~15 kills".
- **19_Wetlands2:19, :23, :30** — 98245, 464, 98072: rate not in the DB.
- **21_AshenvaleEast:16** — 86757: "Grind risk, ~30 Horde kills". That budget is too low; see A4.
- **22_ExcavationSite:6 and :30** — 98815: kami-labs 5.5%, with an abandon line.
- **23_Hillsbrad:5, :13, :26, :38, :40** — 555 and 559: budgets and an abandon line.
- **23_Hillsbrad:54** — 540: no drop rate.
- **24_Gnomeregan:7 and :86** — 2945 Grime-Encrusted Ring: "never farm".
- **26_RazorfenKraul:15** — 1142: "luck, about 0.7%".

**Not labelled yet:**
- No warning at all: 98407, 95250, 96264, 95217, 95214.
- Labelled, but the line points at the wrong mob: 95212 and 91777 need their drop source fixed.
- Kill budget worth adding: 92, 150, 22, 127.

**Suggested standing rule:** a required item drop becomes [O] with a "stop at N" note when it needs more than about 2x the kills the route already does there, or more than ~25 kills on fewer than ~20 spawns.

## Appendix: every mob-drop collection quest in the guide

Column key: **Ch** chapter where accepted. **Req:** R required, R(QS) required with an abandon line, R/O picked up on the route with an [O] hand-in, O optional. **Src:** cdb sampled, cdb* emulator default, WH-F Wowhead Forever tooltip.

Excluded because nothing drops from a mob: vendor items (Nightcrawlers/Bauble, Rhapsody Malt, Soothing Spices, Empty Vial); herbs (Peacebloom, Silverleaf); gathered (91736 apples); skinned (91751 pelts); crafted (565 cloth/cloak/thread; Copper Modulator, Crude Scope); objects (Flagongut's Fossil, Worn Leather Book, Duskweed Petals); phial fills (2926, 2962).

| Quest | Ch | Req | XP | Item x N | Route mobs (lvl) | Rate | Src | Exp. kills | Kill quests on same mobs |
|---|---|---|---|---|---|---|---|---|---|
| 6 Bounty on Garrick Padfoot | 00a | R | 335 | Garrick's Head x1 | Garrick Padfoot 5 | 100% | cdb* | 1 | |
| 18 Brotherhood of Thieves | 00a | R | 355 | Red Burlap Bandana x12 | Defias Thug 3-4 | 80% | cdb* | 15 | |
| 33 Wolves Across the Border | 00a | R | 170 | Tough Wolf Meat x8 | Timber Wolf 2 | 80% | cdb* | 10 | |
| 91743 Rascally Rodents | 00a | R | 170 | Stolen Book x8 | Kobold Vermin/Laborer/Worker 1-4 | | unknown | | 15 x10, 21 x12, 7 x10 |
| 91752 The Big Picture | 00a | R | 315 | Sack of "Picture" Books x1 | Shinyfinder Narf 3 | 65.5% | WH-F | 1.5 | |
| 11 Riverpaw Gnoll Bounty | 00b | R | 840 | Painted Gnoll Armband x8 | Riverpaw Outrunner 9-10 | 40% | cdb* | 20 | |
| 47 Gold Dust Exchange | 00b | R | 630 | Gold Dust x10 | Kobold Miner/Tunneler 5-7 | 50% | cdb* | 20 | |
| 60 Kobold Candles | 00b | R | 475 | Large Candle x8 | Kobold Miner/Tunneler | 66% | cdb* | 12.1 | |
| 83 Red Linen Goods | 00b | R | 780 | Red Linen Bandana x6 | Defias Bandit, Rogue Wizard 8-10 | 66% | cdb* | 9.1 | 91724 x6 |
| 86 Pie for Billy | 00b | R | 405 | Chunk of Boar Meat x4 | Stonetusk/Rockhide Boar | 61.0% | cdb | 6.6 | |
| 87 Goldtooth | 00b | R | 880 | Bernice's Necklace x1 | Goldtooth 8 | 100% | cdb* | 1 | |
| 88 Princess Must Die! | 00b | R | 780 | Brass Collar x1 | Princess 9 | 100% | cdb* | 1 | |
| 112 Collecting Kelp | 00b | R | 315 | Crystal Kelp Frond x4 | Murloc, Streamrunner 6-7 | 33% | cdb* | 12.1 | 99128 |
| 176 Wanted: "Hogger" | 00b | R/O | 880 | Huge Gnoll Claw x1 | Hogger 11 elite | 100% | cdb* | 1 | |
| 91775 Book Return | 00b | R | 680 | Fun with Elementals x1 | Nimsy 6 | 62.3% | WH-F | 1.6 | |
| 91775 Book Return | 00b | R | 680 | Lost Book x6 | Kobold Miner/Tunneler | | unknown | | |
| 91777 Rare Books | 00b | R | 790 | Geomancy... x1 | Geosculptor Yip 7 | 47.4% | WH-F | 2.1 | |
| 91777 Rare Books | 00b | R | 790 | Arcane Explainer x1 | Mother Fang 7-10 (rare) | 26.4% | WH-F | 3.8 | |
| 96393 Old Ironforge Incursion | 00b/01b | R | 1450 | Durgen Dirgehammer's Head x1 | Durgen (dungeon) | 58.1% | WH-F | 1.7 | |
| 99130 An Enticing Offer | 00b | R | 630 | Vial of Animal Blood x6 | Stonetusk Boar, Young Forest Bear | | unknown | | 52 x8 |
| 179 Dwarven Outfitters | 01a | R | 80 | Tough Wolf Meat x8 | Ragged Young Wolf 1 | 80% | cdb* | 10 | |
| 218 The Stolen Journal | 01a | R | 560 | Grelin's Journal x1 | Grik'nir 5 | 100% | cdb* | 1 | |
| 94373 Call of Earth (Sha) | 01a | R | 270 | Iceclaw Bear Pendant x2 | Frostmane Troll Whelp 3-4 | | unknown | | 182 x14 |
| 313 The Grizzled Den | 01b | R | 630 | Wendigo Mane x8 | (Young) Wendigo 5-7 | 80% | cdb* | 10 | |
| 314 Protecting the Herd | 01b | R | 910 | Fang of Vagash x1 | Vagash 11 elite | 100% | cdb* | 1 | |
| 315 The Perfect Stout | 01b | R | 780 | Shimmerweed x6 (also baskets) | Frostmane Seer 8-9 | 80% | cdb* | 7.5 | |
| 317 Stocking Jetsteam | 01b | R | 680 | Chunk of Boar Meat x4 | Crag Boars 5-8 | 45.0% | cdb | 8.9 | |
| 317 Stocking Jetsteam | 01b | R | 680 | Thick Bear Fur x2 | Young Black Bear 5-6 | 80% | cdb* | 2.5 | |
| 384 Beer Basted Boar Ribs | 01b | R | 630 | Crag Boar Rib x6 | Crag Boars 5-8 | 52.0% | cdb | 11.5 | |
| 412 Operation Recombobulation | 01b | R | 840 | Restab. Cog x8 + Gyromech. Gear x8 | Leper Gnome 8-10 | 80% | cdb* | 10 | |
| 417 A Pilot's Revenge | 01b | R | 660 | Mangy Claw x1 | Mangeclaw 11 | 100% | cdb* | 1 | |
| 95212 Never Saddle on Quality | 01b | R | 630 | Pristine Leopard Pelt x6 | Elder Snow Leopard 9-10 (guide targets the wrong mob) | 41.7% | WH-F | 14.4 | |
| 95213 Stolen Blasting Powder | 01b | R | 85 | Empty Powder Keg x1 | Rockjaw Ambusher/Backbreaker | | unknown | | |
| 95214 Stolen Blasting Powder | 01b | R | 840 | Stolen Blasting Powder x16 | Rockjaw Ambusher/Backbreaker | | unknown | | |
| 95217 The Quarry's Smith | 01b | O | 630 | Toughened Boar Hide x4 | Scarred Crag Boar 9-10 | 2.45% | WH-F | 163 | |
| 98326 Frosthowl | 01b | R | 780 | Sack of Fish x1 | Frosthowl 9 | 66.8% | WH-F | 1.5 | |
| 99161 Rime's Wrath | 01b | R | 700 | Avala's Core x1 | Avala 8 | | unknown | | |
| 267 The Trogg Threat | 02 | R | 910 | Trogg Stone Tooth x8 | Stonesplinter troggs 11-14 | 80% | cdb* | 10 | 224/237/263 x10 each |
| 385 Crocolisk Hunting | 02 | R | 1050 | Croc Meat x5 + Croc Skin x6 | Loch Crocolisk 14-15 | 43.6% / 80% | cdb / cdb* | 11.5 | |
| 416 Rat Catching | 02 | R | 880 | Tunnel Rat Ear x12 | Tunnel Rat Geomancer etc. | 80% | cdb* | 15 | |
| 418 Thelsamar Blood Sausages | 02 | R | 880 | Intestines/Bear Meat/Ichor x3 each | Mountain Boar, Elder Black Bear, Forest Lurker | 31.6 / 41.9 / 35.6% | cdb | 9.5 + 7.2 + 8.4 | |
| 86758 Twisting the Knife | 02 | R | 1150 | Marek's Knife x1 | Daggerfang 15 (roams) | 42.6% | WH-F | 2.3 | |
| 94466 Call of Fire (Sha) | 02 | R | 980 | Reagent Pouch x1, Fire Tar x1 | Stonesplinter Seer, Tunnel Rat Geomancer | | unknown | | 237 x10 |
| 94467 Call of Fire (Sha) | 02 | R | 1250 | Glowing Ember x1 | Minor Manifestation of Fire | 100% | cdb* | 1 | |
| 271 Vyrin's Revenge | 04 | R/O | 780 | Ol' Sooty's Head x1 | Ol' Sooty 20 elite | 100% | cdb* | 1 | |
| 297 Gathering Idols | 04 | R | 1350 | Carved Stone Idol x8 | Geomancer, Digger 17-19 | 80% | cdb* | 10 | |
| 22 Goretusk Liver Pie | 05 | R | 910 | Goretusk Liver x8 | Young Goretusk 12-13 | 32.4% | cdb | 24.7 | |
| 38 Westfall Stew | 05 | R | 910 | Vulture Meat/Murloc Eye/Snout/Okra x3 each | Young Fleshripper, murlocs, Young Goretusk, Harvest Watcher | 30.5 / 34.9 / 37.0 / 33.2% | cdb | ~9 each | 9 x20 (Okra), 152 x7 (eyes) |
| 102 Patrolling Westfall | 05 | R | 980 | Gnoll Paw x8 | Riverpaw Gnoll 11-12 | 80% | cdb* | 10 | |
| 103 Keeper of the Flame | 05 | R | 1150 | Flask of Oil x5 | Harvest Watcher 14-15 | 34.8% | cdb | 14.4 | 9 x20 |
| 104 The Coastal Menace | 05 | R | 1550 | Scale of Old Murk-Eye x1 | Old Murk-Eye 20 | 100% | cdb* | 1 | |
| 153 Red Leather Bandanas | 05 | R | 1050 | Red Leather Bandana x15 | Westfall Defias 11-15 | 80% | cdb* | 18.8 | 12 x15, 13 x15 |
| 167 Oh Brother... | 05 | R | 1550 | Thistlenettle's Badge x1 | Foreman Thistlenettle 20 elite | 100% | cdb* | 1 | |
| 168 Collecting Memories | 05 | R | 1350 | Miners' Union Card x4 | DM tunnel undead 17-18 elite | 100% | cdb* | 4 | |
| 2040 Underground Assault | 05 | R | 1550 | Gnoam Sprecklesprocket x1 | Sneed's Shredder (boss) | | unknown (boss) | | |
| 92110 My First Real Potion | 05 | O | 420 | Murloc Eye x3 | murlocs | 34.9% | cdb | 8.6 | 152 x7 |
| 92744 Murloc Gills | 05 | R | 455 | Longshore Murloc Gill x7 | Murloc Coastrunner 12-13 | | unknown | | 152 x7 |
| 92909 / 92911 Harvesting the Harvesters | 05 | O | 800 + 800 | Isospring x14, Gyrostabilizer x5; Isospring x8 | Harvest golems/watchers | | unknown ("worst") | | 9 x20 |
| 19 Tharil'zun | 06 | R | 2550 | Tharil'zun's Head x1 | Tharil'zun 24 elite | 100% | cdb* | 1 | |
| 20 Blackrock Menace | 06 | R | 1650 | Battleworn Axe x10 | Blackrock Grunt/Outrunner 19-21 | 80% | cdb* | 12.5 | |
| 89 The Everstill Bridge | 06 | R | 1550 | Iron Pike x5 + Iron Rivet x5 | Redridge Brute/Mystic 17-19 | 80% | cdb* | 6.2 | |
| 92 Redridge Goulash | 06 | R | 1350 | Snout/Condor/Spider x5 each | Great Goretusk, Dire Condor, Tarantula | 36.4 / 35.1 / 38.4% | cdb | 13.7 + 14.2 + 13.0 | |
| 115 Shadow Magic | 06 | R | 2300 | Midnight Orb x3 | Blackrock Shadowcaster 22-23 elite | 80% | cdb* | 3.8 | |
| 127 Selling Fish | 06 | R | 1250 | Spotted Sunfish x10 | Murloc Flesheater 18-19 | 45% | cdb* | 22.2 | |
| 98407 Show of Force | 06 | R | 950 | Spiked Collar x5 | Redridge Thrasher 14-15 | 8.44% | WH-F | 59.2 | |
| 142 The Defias Brotherhood | 07 | R | 1350 | A Mysterious Message x1 | Defias Messenger | 100% | cdb* | 1 | |
| 166 The Defias Brotherhood | 07 | R | 2600 | Head of VanCleef x1 | VanCleef (boss) | | unknown (boss) | | |
| 214 Red Silk Bandanas | 07 | R | 1250 | Red Silk Bandana x10 | Deadmines Defias (16 types) | 80% | cdb* | 12.5 | |
| 1275 Researching the Corruption | 08 | R | 2400 | Corrupted Brain Stem x8 | BFD satyrs/naga (10 types) | 80% | cdb* | 10 | |
| 95195 Bloodied Insignia | 08 | O | 2600 | Bloodied Insignia x10 | RoL undead (7 types) | | unknown | | |
| 95250 Abominable Creatures | 08 | R | 1650 | Head of the Baron x1 | The Baron (boss) | 15.1% | WH-F | 6.6 | |
| 256 WANTED: Chok'sul | 09 | O | 1750 | Chok'sul's Head x1 | Chok'sul 22 elite | 100% | cdb* | 1 | |
| 277 Fire Taboo | 09 | R | 1850 | Crude Flint x9 | Mosshide gnolls 22-23 | 80% | cdb* | 11.2 | |
| 278 A Dark Threat Looms | 09 | O | 1350 | Venom, Crystal, Tear x1 each | Lurkers / Mo'grosh / crocs | 100 / 23.7 / 100% | cdb* / cdb / cdb* | 1 / 4.2 / 1 | |
| 279 Claws from the Deep | 09 | R | 1750 | Gobbler's Head x1 | Gobbler 22 | 100% | cdb* | 1 | |
| 289 The Cursed Crew | 09 | O | 1750 | Snellig's Snuffbox x1 | First Mate Snellig 29 | 100% | cdb* | 1 | |
| 290 Lifting the Curse | 09 | O | 1200 | Intrepid Strongbox Key x1 | Captain Halyndor 30 | 100% | cdb* | 1 | |
| 471 Apprentice's Duties | 09 | R/O | 2100 | Giant Crocolisk Skin x6 | Giant Wetlands Crocolisk 25-26 | 80% | cdb* | 7.5 | |
| 484 Young Crocolisk Skins | 09 | R | 1750 | Young Crocolisk Skin x4 | Young Wetlands Crocolisk 21-22 | 80% | cdb* | 5 | |
| 98282 Alchemical Hazards | 09 | R | 1750 | Unruptured Stalker Gland x1 | Leech/Cave Stalker 21-22 | | unknown | | |
| 91 Solomon's Law | 10 | R | 1850 | Shadowhide Pendant x10 | Shadowhide gnolls 22-26 | 80% | cdb* | 12.5 | |
| 122 Underbelly Scales | 10 | R | 1700 | Underbelly Whelp Scale x6 | Black Dragon Whelp 17-18 | 80% | cdb* | 7.5 | |
| 126 Howling in the Hills | 10 | R | 2000 | Yowler's Paw x1 | Yowler 25 | 100% | cdb* | 1 | |
| 150 Murloc Poachers | 10 | R | 1550 | Murloc Fin x8 | Flesheater, Minor Tidecaller 17-19 | 30.8% | cdb | 26.0 | |
| 249 Morganth | 10 | R | 2750 | Pendant of Shadow x1 | Morganth 26 | 100% | cdb* | 1 | |
| 386 What Comes Around... | 10 | R | 2000 | Head of Targorr x1 | Targorr (Stockade) | 100% | cdb* | 1 | |
| 966 / 970 / 973 Tower of Althalaxx | 11 | R | 1350 / 1650 / 1950 | Worn Parchment x4 / Soul Gem x1 / Tome x1 | Dark Strand 16-19 / Ilkrud 24 | 80 / 100 / 100% | cdb* | 5 / 1 / 1 | |
| 986 A Lost Master | 11 | O | 1550 | Fine Moonstalker Pelt x5 | Moonstalker Matriarch/Sire | 80% | cdb* | 6.2 | |
| 1138 Fruit of the Sea | 11 | O | 1250 | Fine Crab Chunks x6 | Tide/Reef Crawlers | 80% | cdb* | 7.5 | |
| 1199 Twilight Falls | 11 | R | 2550 | Twilight Pendant x10 | BFD Twilight cultists | 80% | cdb* | 12.5 | |
| 2098 Gyromast's Retrieval | 11 | R | 1550 | Top/Middle/Bottom of Gelkak's Key, 1 each | Foreststrider / Greymist / Crawlers | 100% | cdb* | 1 each | |
| 87760 Holy Diver | 11 | O | ? | Rod of Deep Dominion x1 | Stormscale Beastmistress 19 | 70.6% | WH-F | 1.4 | |
| 98042 It's All Fun and Games Until... | 11 | O | 1250 | Peerless Eye x1 | Twilight Disciple/Thug | | unknown | | |
| 1009 Ruuzel | 12 | R | 2550 | Ring of Zoram x1 | Ruuzel 22 | 100% | cdb* | 1 | |
| 1016 Elemental Bracers | 12 | R | 1950 | Intact Elemental Bracer x5 | Befouled Water Elemental 23-25 | 80% | cdb* | 6.2 | |
| 1017 Mage Summoner | 12 | O | 2550 | Sarilus Foulborne's Head x1 | Sarilus 25 | 100% | cdb* | 1 | |
| 1023 Raene's Cleansing | 12 | R | 1250 | Glowing Gem x1 | Saltspittle murlocs | 100% | cdb* | 1 | |
| 1054 Culling the Threat | 12 | R | 2000 | Dal Bloodclaw's Skull x1 | Dal Bloodclaw 25 | 100% | cdb* | 1 | |
| 1200 Blackfathom Villainy | 13 | R | 3300 | Head of Kelris x1 | Kelris (boss) | 100% | cdb* | 1 | |
| 93 Dusky Crab Cakes | 14 | R | 780 | Gooey Spider Leg x6 | Duskwood spiders 18-22 | 36.5% | cdb | 16.4 | |
| 101 The Totem of Infliction | 14 | R | 2550 | Ghoul Fang x10, Spider Venom x5, Skeleton Finger x10 | ghouls / spiders / skeletons | 80% | cdb* | 12.5 / 6.2 / 12.5 | |
| 177 / 181 Look To The Stars | 14 | R | 1500 / 2450 | Looking Glass x1 / Monocle x1 | Insane Ghoul / Zzarc' Vul | 100% | cdb* | 1 | |
| 377 Crime and Punishment | 14 | R | 2100 | Hand of Dextren Ward x1 | Dextren Ward (Stockade) | 100% | cdb* | 1 | |
| 388 The Color of Blood | 15 | R | 2650 | Red Wool Bandana x10 | Stockade inmates (8 types) | 40-80% | cdb* | ~12.5-17 | |
| 391 The Stockade Riots | 15 | R | 2350 | Head of Bazil Thredd x1 | Bazil (boss) | 100% | cdb* | 1 | |
| 34 An Unwelcome Guest | 16 | R | 1950 | Bellygrub's Tusk x1 | Bellygrub 24 | 100% | cdb* | 1 | |
| 169 Wanted: Gath'Ilzogg | 16 | O | 2650 | Head of Gath'Ilzogg x1 | Gath'Ilzogg 26 elite | | unknown (named) | | |
| 180 Wanted: Lieutenant Fangore | 16 | R | 2650 | Fangore's Paw x1 | Fangore 26 | 100% | cdb* | 1 | |
| 347 Rethban Ore | 16 | O | 970 | Rethban Ore x5 (also veins) | Redridge Drudger 20-21 | 33.8% | cdb | 14.8 | |
| 95999 WANTED: Incinerator Gar'im | 16 | R | 2550 | Broken Staff x1 | Gar'im 23 elite | 85.9% | WH-F | 1.2 | |
| 98 The Legend of Stalvan | 17 | R | 4100 | Mistmantle Family Ring x1 | Stalvan 32 | 100% | cdb* | 1 | |
| 133 Ghoulish Effigy | 17 | R | 1650 | Ghoul Rib x7 | Plague Spreader + ghouls | 80% | cdb* | 8.8 | 58 x20 |
| 156 Gather Rot Blossoms | 17 | R | 970 | Rot Blossom x8 | Skeletal Horror/Fiend | 80% | cdb* | 10 | |
| 253 Bride of the Embalmer | 17 | R | 3650 | Embalmer's Heart x1 | Eliza 31 | | unknown (named) | | |
| 296 Ormer's Revenge | 18 | R | 2950 | Sarltooth's Talon x1 | Sarltooth 29 | 100% | cdb* | 1 | |
| 324 The Lost Ingots | 18 | R | 1750 | Lightforge Ingot x5 | Bluegill Raider 28-29 | 80% | cdb* | 6.2 | |
| 464 War Banners | 18 | R | 2300 | Dragonmaw War Banner x8 | Dragonmaw Raider etc. | 80% | cdb* | 10 | |
| 470 Digging Through the Ooze | 18 | O | 2400 | Sida's Bag x1 | Black/Crimson/Monstrous Ooze | 100% | cdb* | 1 | |
| 2928 Gyrodrillmatic Excavationators | 18 | R | 2450 | Robo-mechanical Guts x24 | 16+ Gnomeregan types | 80% | cdb* | ~30 | |
| 98072 Crocs of the Sky | 18 | R | 2200 | Pristine Crimson Scale x8 | 4 whelp types 23-27 | | unknown | | |
| 98216 Understanding Our Present | 18 | O | 3150 | Titanic Keystone x1 | Goaz Warder 32 elite | 88.3% | WH-F | 1.1 | |
| 98310 Gleaning Our Future | 18 | O | 3200 | 4 hearts x1 | Ados/Modr/Golm/Neru 32 elite | 81-88% | WH-F | 1.2 each | |
| 98815 Highland Hides | 18 | R(QS) | 1150 | Thicket Raptor Hide x4 | Shadetooth + Thicket raptors (dungeon) | | unknown (kami 5.5% Shadetooth) | | |
| 304 A Grim Task | 19 | O | 3350 | Ear of Balgaras x1 | Balgaras 34 elite | 100% | cdb* | 1 | |
| 378 The Fury Runs Deep | 19 | O | 2750 | Head of Deepfury x1 | Kam Deepfury (Stockade) | 100% | cdb* | 1 | |
| 474 Defeat Nek'rosh | 19 | O | 2550 | Nek'rosh's Head x1 | Nek'rosh 32 | 100% | cdb* | 1 | |
| 95646 Horrors in the Highland | 19 | R | 3150 | Horrible Rootcore x1 | Highland Horror (dungeon) | 64.3% | WH-F | 1.6 | |
| 98245 Razormaw Needling | 19 | R | 2350 | Razormaw Incisor x10 | Highland/Elder Razormaw 27-29 | | unknown | | |
| 98283 Carnage | 19 | O | 3050 | Rotclaw Flesh x1, Carnage's Head x1 | Maddened Rotclaw / Carnage | 26.3 / 92.4% | WH-F | 3.8 / 1.1 | |
| 1035 Fallen Sky Lake | 20 | R | 3050 | Fallen Moonstone x1 | Shadethicket Oracle 30 | 100% | cdb* | 1 | |
| 1031 The Branch of Cenarius | 21 | R | 2550 | Branch of Cenarius x1 | Geltharis 32 | 100% | cdb* | 1 | |
| 1046 Raene's Cleansing | 21 | R | 3050 | Ran Bloodtooth's Skull x1 | Ran Bloodtooth 30 | 100% | cdb* | 1 | 1045 x4 |
| 1143 The Tower of Althalaxx | 21 | O | 2500 | Athrikus Narassin's Head x1 | Athrikus 31 | | unknown (named) | | |
| 86757 Slowing the Orc Advance | 21 | O | 2550 | Jagged Orcish Sword x6, Curved Orcish Dagger x4 | Horde Grunt 29-30 / Scout 26-28 | 12.05 / 1.6% | WH-F | 50 / 250 | |
| 943 The Absent Minded Prospector | 22 | R | 2400 | Stone of Relu x1 (+ fossil object) | Mottled raptors | 100% | cdb* | 1 | |
| 94502 Call of Water (Sha) | 22 | R | 1400 | Corrupt Manifestation's Bracers x1 | Corrupt Minor Manifestation 22 | 100% | cdb* | 1 | |
| 95810 / 98824 Lost Relic Carry / Prehistoric Prism | 22 | O | 630 / 3150 | Titan Relic x1 | Relic Guardian (boss) | 26.8% | WH-F | 3.7 | |
| 540 Preserving Knowledge | 23 | O | 3550 | Recovered Tome x5 | Crushridge ogres 34-38 | 80-100% | cdb* | 6 | |
| 555 Soothing Turtle Bisque | 23 | R(QS) | 2500 | Turtle Meat x10 | Snapjaw 30-31 | 100% | cdb* | 10 | |
| 559 Farren's Proof | 23 | R | 2550 | Murloc Head x10 | Torn Fin murlocs 31-32 | 80% | cdb* | 12.5 | 536 x10 |
| 565 Bartolo's Yeti Fur Cloak | 23 | O | 2700 | Yeti Fur x10 | Cave/Ferocious Yeti 30-32 | 80% | cdb* | 12.5 | |
| 2922 Save Techbot's Brain! | 24 | R | 2650 | Techbot's Memory Core x1 | Techbot 26 elite | 100% | cdb* | 1 | |
| 2951 The Sparklematic 5200! | 24 | O | ? | Grime-Encrusted Object x1 | Gnomeregan trash | 80% | cdb* | 1.2 | |
| 228 Mor'Ladim | 25 | O | 2050 | Mor'Ladim's Skull x1 | Mor'Ladim 35 elite | 100% | cdb* | 1 | |
| 96264 Elemental Aid (Sha) | 25/26 | R | 2650 | Tattered Note x1 | Charlga Razorflank (boss) | 0.7% (artifact?) | WH-F | ? | |
| 1142 Mortality Wanes | 26 | R/O | 3050 | Treshala's Pendant x1 | all 27 RFK quilboar types | 10% | cdb* | 10 | |

## Data notes
- Wowhead Forever's `nether.wowhead.com/forever/tooltip/item/<id>` endpoint returns a "Drop Chance %" for many single-dropper Forever quest items; classicdb.ch serves Classic drop percentages to scripts (Wowhead pages do not).
- The Forever DB's npcDrops lists are what Questie has recorded, so "only X drops it" means "no other dropper is recorded", not proof. Both wrong-mob findings were also confirmed by the Wowhead Forever tooltip's "Dropped by" line.
