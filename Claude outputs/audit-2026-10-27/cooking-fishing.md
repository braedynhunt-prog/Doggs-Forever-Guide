# Cooking, Fishing and First Aid audit: Forever Alliance 1-30 (Dwarf Shaman route)

Read-only audit, 27 Oct 2026. Nothing under `guide/` was changed.

**Sources.** Vendor, drop, quest and NPC data come from QuestieDB Forever 1.0.6 (`tooling/qdb`). Coordinates are spawn centroids in Forever map space. Recipe skill, food stats and level requirements come from Wowhead Forever tooltips (`nether.wowhead.com/forever/tooltip/...`), fetched this session and cached in the scratchpad, not in `item_tips.json`. Anything taken only from Classic knowledge is marked **(Classic, unverified)**.

## Short answer

The guide has **no cooking levelling plan**: no skill targets by chapter or level. What it does have:

- profession and camping notes;
- the four cooking-trainer touch points (learn Cooking, and Journeyman mentioned in text);
- recipe-reward quests, picked up for their XP and almost never labelled as recipe sources.

What it is missing:

- **Recipe vendors.** It never sends you to one: Drac Roughcut, Khara's Longjaw recipe, Kendor Kabonka, Shandrina's Expert Cookbook, Ulthaan.
- **Reagents.** No spice, Simple Wood or Flint and Tinder purchases, although its camp steps assume a campfire.
- **Journeyman training steps.** No line with a [G]/[TAR] for it, even though one recipe-reward hand-in (Crocolisk Steak, 80) lands above the Apprentice cap of 75.
- **Fishing.** Only "learn Fishing if you want it" at Paxton Ganter.
- **One cooking quest.** Seasoned Wolf Kabobs (90) is missing: 2,000 XP on chapters the route already runs.

One wording fix is needed. The guide says "every cooked food gives a stat buff and an XP trickle". The Forever tooltips say something different:

- Eating for 10 seconds gives **Well Fed for 15 min: the stat buff plus +5% XP from kills**.
- Some cooked foods give **no** Well Fed: Charred Wolf Meat, Boiled Clams, Clam Chowder, Dig Rat Stew and Savory Deviate Delight.
- The Forever smoothies give Spirit with no XP line.

The XP bonus is the same for every buff food, so "best food" comes down to the stat. Eat while you drink and the buff costs nothing.

## 1. What the guide already has

Dwarf path plus shared chapters. Human 00a/00b lines are only noted.

| Where | What | Comment |
|---|---|---|
| 01a:8 | Profession note: Cooking passive "stat buff and an XP trickle"; First Aid now makes healing potions | Wording fix above. The potions part is correct (Blizzard Watch) |
| 01a:9 | Hunter pet-food note | – |
| 01a:10 | Camping note: Basic Campfire (3 slots), objects incl. Fish Bowl +8% all stats, 1 h cooldown, Camping 101 at Eric | Missing: Fish Bowl needs Fishing 20 and is Kings-exclusive. Each object is a crafted consumable |
| 01b:9 | Keep extra Chunk of Boar Meat / Crag Boar Rib "for Cooking" | Only cooking-mats instruction in the guide |
| 01b:13-16 | The Great Outdoors → [QA96629 Camping 101: Cooking]; optional Skinning/Mining/First Aid/LW | Fishing (96050) excluded "unless you take it" |
| 01b:18 / 01b:81 | [QA384] / [QT384] Beer Basted Boar Ribs | Recipe reward (Cooking 25) not mentioned. Only 1 Rhapsody Malt bought (01b:20) |
| 01b:21 | Gremlock Pilsnor: learn Cooking, [QT96629] | – |
| 01b:25 / 01b:85 | Thamner Pol: learn First Aid; [QT96047] at First Aid 20 | – |
| 01b:59 | [O] Paxton Ganter: learn Fishing if you want | No pole/vendor step, no Fish Bowl link |
| 01b:129 | Waylaid Supplies note | Crates include Spiced Wolf Meat, Herb Baked Eggs, Smoked Bear Meat, Brilliant Smallfish, Heavy Linen/Wool/Silk Bandages, Minor/regular Healing Potions, Soothing Turtle Bisque (DB). Not mentioned |
| 02:36 / 02:114 | [QA418] / [QT418] Thelsamar Blood Sausages | Recipe: Blood Sausage (60) not mentioned |
| 02:69 | [O] Khara Deepwater [V] "fishing supplies" | No mention that she sells Longjaw Mud Snapper (best AP food) |
| 02:97 / 04:33, 02:104 | Crocolisk Hunting 385; "keep Crocolisk Meat" | Recipe: Crocolisk Steak (80) not mentioned. **Arrives above the Apprentice cap** |
| 03:14, 04:60 | Text notes: Nissa Firestone / Daryl Riknussun teach Journeyman at 50 | Text only, no [G]/[TAR] step |
| 03:25, 07:71 | "Camp before you zone in" | No Simple Wood / Flint and Tinder ever bought |
| 05:33/37/55/58 | Goretusk Liver Pie (22), Westfall Stew (36/38) | Recipes (50 / 75) not called out |
| 06:9 | Merchant camp mentions "Cooking vendors" | Kalsey Sanden (10.6,72.3): smoothies + Smoked Sagefish |
| 06:24/69 | Selling Fish 127 | Recipe: Murloc Fin Soup (90) not mentioned |
| 06:29/70, 06:30 | Redridge Goulash 92; Crystal Boughman teaches Journeyman | Only in-guide Journeyman pointer outside Ironforge |
| 07:11-13 | Catherine Leland bait for Fishin' Time 95065 (910 XP) | Arnold Leland (trainer) stands beside her |
| 07:104-105 | Cookie | Missing: Cookie's Stirring Rod (+25% cooking speed) and Blueprint: Cookie's Feast (web sources; not in the DB drop table) |
| 09:74/100, 18:45 | Apprentice's Duties 471 | Recipe: Crocolisk Gumbo (120) not mentioned |
| 10:17 | Michelle Belle: Journeyman First Aid | Only Journeyman First Aid step with [G] |
| 11:41/94 | Fruit of the Sea 1138 | The Family and the Fishing Pole (1141, 980 XP) absent |
| 14:70 | Dusky Crab Cakes 93 "(Gooey Spider Cake needs Cooking 110)" | The only recipe-skill flag in the guide |
| 18:50-62 | Ormer's Revenge 294/296 | Recipe: Curiously Tasty Omelet (130) not mentioned |
| 23:13-14/39/41 | Soothing Turtle Bisque 555, Soothing Spices from Micha Yance | Recipe needs 175 (Expert) |
| Many (07:52, 08:19, 11:14, 12:65, 13:7, 16:7, 20:58, 22:16, 24:8, 25:74, 26:8) | "stock food and water" | Vendor food only |
| 00a:7-8, 00a:62-64, 00b:12-13, 00b:127-128 | Human: Sam Sarsaparilla Camping 101, Tomas (Cooking), Michelle Belle (First Aid) | Human path only |

## 2. Forever food facts

From the tooltips. All foods are 15 min Well Fed and +5% kill XP unless marked.

The **Value** column is attack-power equivalent for 2H Enhancement, using the project's own weights in `weights/forever-enh-stat-weights.md`: Str 2.0, AP 1.0, Int 1.05, Agi 0.85, Sta 0.

| Food | Learn skill | Eat lvl | Buff | Value | Mats / where on route | Recipe source (DB) |
|---|---|---|---|---|---|---|
| Roasted Boar Meat | 1 (trainer) | – | +1 Str | 2 | Chunk of Boar Meat: Crag Boars (01b), Mountain Boars (02) | Trainer (Classic, unverified) |
| Spiced Wolf Meat | 10 (trainer) | – | +1 Agi | 0.85 | Stringy Wolf Meat + Mild Spices | Trainer (Classic, unverified). **Charred Wolf Meat = no buff** |
| Herb Baked Egg | 1 (trainer) | – | +1 Sta | 0 | Small Egg (Mountain Buzzard 02, Fleshrippers 05, Dire Condor 06) | Trainer (Classic, unverified) |
| Beer Basted Boar Ribs | 25 | – | +1 Str | 2 | Crag Boar Rib + Rhapsody Malt (Innkeeper Belm) | Quest 384 (in guide) |
| Brilliant Smallfish | 1 | – | +2 AP | 2 | Raw Brilliant Smallfish (Dun Morogh/Loch Modan water, Classic) | Gretta Ganter, Khara Deepwater, Catherine Leland, Tharynn Bouden |
| Smoked Bear Meat | 40 | – | +1 Str | 2 | Bear Meat: Elder/Grizzled Black Bears (02), Thistle Bears (11) | **Drac Roughcut, Thelsamar 35.6,49.1** (not in guide) |
| Goretusk Liver Pie | 50 | 5 | +3 Str | 6 | Goretusk Liver: Young/Great Goretusk (05, 06) + Mild Spices | Quest 22 (in guide); Kendor |
| **Longjaw Mud Snapper** | 50 | 5 | **+10 AP** | **10** | Raw Longjaw Mud Snapper (inland water 10-25 zones, Classic) | **Khara Deepwater 40.3,39.3** (02:69), Tansy Puddlefizz (IF 48.2,6.5), Tharynn Bouden |
| Blood Sausage | 60 | 5 | +3 Str | 6 | Bear Meat + Boar Intestines + Spider Ichor (02 north loop) | Quest 418 (in guide) |
| Westfall Stew | 75 | 5 | +15% speed (Westfall only) | – | Vulture Meat, Murloc Eye, Goretusk Snout | Quest 38 (in guide) |
| Breakfast Omelette (new) | 75 | 5 | +3 Sta | 0 | Small Egg + 4 Mild Spices | Drop: Dire Condor (06:56, rate unknown) |
| Dry Pork Ribs | 80 (trainer) | 5 | +3 Str | 6 | Boar Ribs: Mountain/Elder Mountain Boar (02/04), Goretusks (05/06) + Mild Spices | Journeyman trainer (Classic, unverified) |
| Crocolisk Steak | 80 | 5 | +3 Agi | 2.55 | Crocolisk Meat: Loch Crocolisk (02), Wetlands crocs (09/18) | Quest 385 (in guide) |
| Murloc Fin Soup | 90 | – | +1 Sta | 0 | 2 Murloc Fin + Hot Spices (06/10/09) | Quest 127 (in guide) |
| Redridge Goulash | 100 | 5 | +3 Int | 3.15 | Crisp Spider Meat + Tough Condor Meat (06) | Quest 92 (in guide) |
| Seasoned Wolf Kabob | 100 | 15 | +5 Agi | 4.25 | 2 Lean Wolf Flank + Mild Spices (Duskwood dire wolves) | **Quest 90 (missing)**; Kendor |
| **Succulent Pork Ribs** | 110 | 15 | **+5 Str** | **10** | 2 Boar Ribs + Hot Spices | **Kendor Kabonka, SW Old Town 77.5,52.7** (not in guide); drops |
| **Lean Venison** | 110 | 15 | **+5 Str** | **10** | Stag Meat + 4 Mild Spices (Wild Buck/Shadowhorn Stag, Ashenvale) | **Ulthaan, Silverwind Refuge 50.0,66.6** (not in guide) |
| Big Bear Steak | 110 | 5 | +3 Str | 6 | Big Bear Meat + Hot Spices | Ulthaan; quest 498 (Horde) |
| Gooey Spider Cake | 110 | 15 | +5 Sta | 0 | 2 Gooey Spider Leg + Hot Spices | Quest 93 (in guide) |
| Crocolisk Gumbo | 120 | 15 | +5 Agi | 4.25 | Tender Crocolisk Meat (Wetlands crocs) + Hot Spices | Quest 471 (in guide) |
| Curiously Tasty Omelet | 130 | 15 | +5 Sta | 0 | Raptor Egg (Mottled raptors, 18) + Hot Spices | Quest 296 (in guide); Kendor |
| Tasty Lion Steak | 150 | 25 | +10 Agi | 8.5 | 2 Lion Meat + Soothing Spices | Quest 564 Costly Menace (req 30, not on route) |
| **Bear Brisket** (new) | 175 | 25 | **+10 Str** | **20** | 2 Big Bear Meat + 3 Hot Spices | Drop: Ashenvale Bear (21-22, Ashenvale 46.4,58.9), rate unknown |
| **Mithril Head Trout** | 175 | 25 | **+20 AP** | **20** | Raw Mithril Head Trout (Classic: Wetlands/Hillsbrad inland, higher Fishing) | Stuart Fleming (Menethil 8.0,58.4), Lindea Rabonne (Southshore 50.6,61.0), Heldan Galesong (Auberdine 37.0,56.4), Tansy (IF) |
| Soothing Turtle Bisque | 175 | 15 | +5 Sta | 0 | Turtle Meat (Snapjaw, 23) + Soothing Spices | Quest 555 (in guide) |

Other foods and drinks, not worth targeting:

- **Crab Cake, Cooked Crab Claw, Pincer Bites:** Int foods.
- **Peace Tea:** dropped by Frostmane Seers (01b:65). A drink: mana plus Healing Power, needs Peacebloom.
- **Smoothies:** Spirit; sold by Kalsey Sanden at the Redridge camp.
- **Smoked Sagefish:** spell damage.
- **Fillet of Frenzy, Loch Frenzy Delight, Bristle Whisker Catfish, Rockscale Cod:** these four only buff Fishing skill.
- **Savory Whimsyfin Delight:** new transform food; drops from Redridge mobs.

**Best food by level for this character:**

| Level | Best food | Value |
|---|---|---|
| 1-5 | Roasted Boar Meat / Beer Basted Boar Ribs / Brilliant Smallfish | 2 |
| 5-15 | Longjaw Mud Snapper if you fish | 10 |
| 5-15, no fishing | +3 Str: Blood Sausage, Dry Pork Ribs, Goretusk Liver Pie | 6 |
| 15-25 | Succulent Pork Ribs or Lean Venison (tie Longjaw) | 10 |
| 25+ | Bear Brisket / Mithril Head Trout (both need Cooking 175, i.e. Expert) | 20 |

Agility, Intellect and Stamina foods are filler for skill-ups. Stamina food only matters in dungeons.

**Buying vs learning.** No cooking recipe in the Forever DB has a character-level requirement, so you can always buy one early and learn it later (Classic vendor behaviour). Recipe reward items stay in your bags the same way. The real gates are:

- **Journeyman:** skill 50 and level 10 (Classic, unverified). Apprentice caps at 75.
- **Expert Cookbook:** needs Cooking 125 to read. Journeyman caps at 150.
- **Recipe learn skill:** each recipe's "Requires Cooking (N)" on the tooltip.
- **Food level:** eat level 5 / 15 / 25 on the bigger foods.

## 3. Route-aligned cooking plan, with skill checkpoints

Skill-up colours are Classic orange/yellow/green/gray thresholds **(Classic, unverified)**.

| Chapter (lvl) | Stop / NPC (Forever coords) | Do | Target skill |
|---|---|---|---|
| 01b (6) Kharanos | Gremlock Pilsnor 47.7,52.3 (in guide). Kreg Bilmn 47.2,52.4: Simple Wood + Flint and Tinder. Golorn Frostbeard 46.7,53.5: Mild Spices, Fishing Pole. Innkeeper Belm 47.4,52.5: Rhapsody Malt | Learn Cooking. Cook every Chunk of Boar Meat (Roasted Boar Meat 1/45/65/85) and every spare Crag Boar Rib after 384 (Beer Basted 25/60/80/100) | **40-50 by level 11** |
| 01b (10) Kharanos | Gremlock again (01b:130 trainer stop) | Try Journeyman if 50 (whether Gremlock offers it is unverified) | – |
| 02 (11-12) Thelsamar | **Drac Roughcut 35.6,49.1** (next to Yanni, 02:38) | Buy Recipe: Smoked Bear Meat (40; 40/80/100/120). Cook the north-loop Bear Meat. Roast Mountain Boar meat to 45 first if you are under 40 | 50+ |
| 02 (12) Ironforge trip | **Daryl Riknussun 60.1,36.4** (Great Forge; 10-12 units off the route's nearest step). Emrul Riknussun 59.9,37.4: spices | Journeyman Cooking if 50. Dry Pork Ribs (80) from the trainer **(Classic, unverified)** | – |
| 02 (12) the loch | **Khara Deepwater 40.3,39.3** (02:69) | Buy Recipe: Longjaw Mud Snapper (50) even if you are under 50 | – |
| 02 (13-14) | Vidra Hearthstove (02:114) | Learn Blood Sausage (60). Its mats come from the 02:68 north loop | 60-75 |
| **03 (15) Ironforge** | Daryl Riknussun 60.1,36.4 | **Last Ironforge visit before 04:33.** Must be Journeyman here, or the Crocolisk Steak reward (80) cannot be learned and you are stuck at 75 | 75 → Journeyman |
| 04 (16-17) | Marek Ironheart (04:33) | Learn Crocolisk Steak (80). Elder Mountain Boars (04:28) → Boar Ribs (Dry Pork Ribs) | 85-90 |
| 05 (17-18) Westfall | Salma Saldean (05:55) | Learn Goretusk Liver Pie (50) and Westfall Stew (75, yellow to 115) | 90-100 |
| 06 (18-19) Lakeshire | Chef Breanna, Crystal Boughman 17.7,43.5 (Journeyman fallback). **Gloria Femmel 21.6,43.5**: Hot Spices | Learn Murloc Fin Soup (90) and Redridge Goulash (100); you may be just under 100, so keep it in your bags | ~100 |
| 08 (20) Stormwind tram | **Kendor Kabonka 77.5,52.7** (5 units from the tram step at 73.8,49.2). Stephen Ryback 78.2,53.1 is the trainer | Buy Recipe: Succulent Pork Ribs (110; orange to 130). Bank Boar Ribs from 04/05/06 for it | – |
| 09 (21-22) Menethil | James Halloran (09:100) | Learn Crocolisk Gumbo (120). Cook Tender Croc Meat | 110-120 |
| 12 (24-25) Silverwind Refuge | **Shandrina 49.5,67.1** (0.3 from the 12:50 step; Alliance faction). **Ulthaan 50.0,66.6** | Buy the Expert Cookbook (read it at 125) and Lean Venison (110, +5 Str). Kill Ashenvale Bears you pass for Big Bear Meat and a Bear Brisket chance | 125 → Expert |
| 14 / 15 / 17 (25-28) Duskwood | Chef Grual 73.8,43.5. Felicia Gump (SW 69.3,71.3) | Gooey Spider Cake (110). **Add quest 90 Seasoned Wolf Kabobs** (2,000 XP, see insertions) | 130-145 |
| 18 (28-29) Wetlands | Ormer Ironbraid (18:62) | Learn Curiously Tasty Omelet (130; yellow to 170) with Mottled raptor eggs | ~150 |
| 23 (30) Southshore | Chef Jessen. **Lindea Rabonne 50.6,61.0** (Mithril Head Trout). Micha Yance 48.9,55.0: Soothing Spices | Soothing Turtle Bisque needs 175, which you are probably not at yet; keep the recipe | 150-165 |

**Arrive-below-requirement flags:**

1. **04:33, Crocolisk Steak (80): the real gap.** Apprentice caps at 75, and the guide's next Ironforge stop (04:57) comes *after* the turn-in. Fix: a Journeyman step in ch02 or ch03.
2. **02:69, Longjaw (50), around level 12:** you are probably 40-50 here. Buying is fine; learn it at 50.
3. **06:70, Redridge Goulash (100), level 18-19:** likely just under. Carry it.
4. **12:50, Expert Cookbook (125), level 24-25:** borderline. Buy it and read it later. ch21:69 passes Shandrina again at 29-30 as a second chance.
5. **23:41, Soothing Turtle Bisque (175), level 30:** below. Expert plus 175 is a post-30 goal. Mithril Head Trout and Bear Brisket have the same gate.

The Forever **Journeyman Campfire** (5 slots) needs Cooking 90 to learn and 140 to place. Its blueprint drops from Lord Serpentis in Wailing Caverns, which is not on the route. Warcraft Tavern also says it drops in the Deadmines; the DB does not.

## 4. Fishing

**Trainers on route:**

- Paxton Ganter, Dun Morogh 35.5,40.2 (01b:59). Camping 101: Fishing (96050, 270 XP) hands in here.
- Grimnur Stonebrand, IF Forlorn Cavern 48.1,6.9, about 6 units from the shaman-trainer step at 46.2,13.2 (02, 03, 04, 08, 15).
- Arnold Leland, SW canal 55.0,69.7, beside 07:11.
- Matthew Hooper, Lakeshire 21.9,51.1.
- Harold Riggs, Menethil 8.1,58.6.

Journeyman Fishing is skill 50 / level 10 **(Classic, unverified)**. The Expert Fishing book (req level 20, Fishing 125, Forever tooltip) is sold by Old Man Heming in Booty Bay, which is off the route.

**Poles, bait and fish recipes on route:**

| Vendor | Coords | Sells |
|---|---|---|
| Golorn Frostbeard (Kharanos) | 46.7,53.5 | Fishing Pole, Shiny Bauble |
| Gretta Ganter (Brewnall; 01b:57 quest NPC) | 31.5,44.6 | Strong Fishing Pole (+45 Fishing, req Fishing 10), Brilliant Smallfish |
| Khara Deepwater (Loch Modan) | 40.3,39.3 | Poles, Nightcrawlers, Brilliant Smallfish, Longjaw Mud Snapper, Loch Frenzy Delight |
| Tansy Puddlefizz (IF) | 48.2,6.5 | Longjaw Mud Snapper, Slitherskin Mackerel, Rockscale Cod, Mithril Head Trout |
| Catherine Leland (SW) | 55.1,69.8 | Brilliant Smallfish, Rainbow Fin Albacore, Bristle Whisker Catfish |
| Stuart Fleming (Menethil) | 8.0,58.4 | Rainbow Fin Albacore, Rockscale Cod, Mithril Head Trout |
| Heldan Galesong (Auberdine) | 37.0,56.4 | Rainbow Fin Albacore, Rockscale Cod, Mithril Head Trout, Clam Chowder |
| Laird (Auberdine) | 36.8,44.3 | Fillet of Frenzy |
| Lindea Rabonne (Southshore; route passes at 20 and 30) | 50.6,61.0 | Bristle Whisker Catfish, Rockscale Cod, Mithril Head Trout |

**Where to fish on route (catch tables are Classic, unverified):**

- Iceflow Lake (01b:59-63): Brilliant Smallfish.
- The loch at Khara's dock (02, 04, 09): Longjaw Mud Snapper, Loch Frenzy, Smallfish.
- Lake Everstill at the Lakeshire docks (06, 10, 16): Longjaw, later Bristle Whisker.
- Westfall coast (05/07) and Darkshore/Wetlands coasts (09, 11, 18): Rainbow Fin Albacore.
- Wetlands and Hillsbrad inland (18-23): Bristle Whisker, then Mithril Head Trout at higher skill.

**Fish Bowl:**

- **How to get it:** Fishing 20. Learned from Camping 101: Fishing (Paxton Ganter) or a fishing trainer.
- **Cost:** 1 Raw Brilliant Smallfish + 1 Empty Vial each (wow-professions; craft spell not found in the tooltip scan).
- **Effect:** +8% all stats, mutually exclusive with Blessing of Kings (Forever tooltip, item 279967).
- **The catch: each player places ONE camp object per hour** (shared 1 h cooldown). Solo, Braedyn's single object is the choice between Lodestone (Might-like melee AP; value level-scaled and unresolved in the tooltip), Camp Chair (+2% crit) and Fish Bowl.
- **My read:** for a 2H Enhancement shaman, Lodestone is probably the better solo pick (Might is mostly AP; Kings at ~20 is a few Str). Fish Bowl is worth having as the duo's second object, or when Lodestone turns out small in game. **Verify in game.**

**Verdict on fishing.** Worth a small, bounded investment, not a levelling sideline:

- **Must-do (about 15 min):** learn at Paxton and fish Iceflow Lake to 20 for the Fish Bowl option. Bank 10-20 Raw Brilliant Smallfish for bowls.
- **Good value:** fish Longjaw at Khara's dock in ch02 and ch04 when you hearth to Thelsamar anyway. At 10 AP it is the best Enhancement food from 5 to 25, and 40 fish ≈ 10 hours of buff.
- **Skip:** Bristle Whisker and Rockscale. Their buffs are fishing skill only.
- **Optional:** The Family and the Fishing Pole (1141, 980 XP, 6 Darkshore Grouper, ch11). Its pole tooltip says +27 Fishing; Warcraft Tavern says +3.

## 5. First Aid

**Already in the guide:**

- learn First Aid at Thamner Pol (01b:25);
- First Aid Kit via Camping 101 at First Aid 20 (01b:85);
- Journeyman as ch03/04 text only;
- Michelle Belle Journeyman (10:17).

**Not in the guide:**

- a Journeyman step with [G] in Ironforge;
- Wool / Silk bandage switches;
- potions.

| Skill | Recipe (learn skill, Classic, unverified) | Cloth on route |
|---|---|---|
| 1-40 | Linen Bandage (1) | Linen: troggs/Frostmane in 01a/01b, Stonesplinter troggs in 02 (mobs 1-19) |
| 40-80 | Heavy Linen Bandage (40) | Same |
| **50** | **Journeyman First Aid, level 10** at Nissa Firestone IF 55.1,58.3 (ch02/03/04). Also Shaina Fuller SW 53.0,44.7, Fremal Doohickey Menethil 10.8,61.4, Michelle Belle Goldshire | – |
| 80-115 | Wool Bandage (80) | Wool: Defias (05, 07 Deadmines), Redridge gnolls/Blackrock (06, 10), Wetlands gnolls/Dark Iron (09) |
| 115-150 | Heavy Wool Bandage (115) | Same |
| 150 | Silk Bandage (150) = Journeyman cap | Silk: Stockade (15), Duskwood/Hillsbrad humanoids, Gnomeregan (24) |
| >150 | Needs Expert First Aid - Under Wraps (First Aid 125 to read), Deneb Walker in Stromgarde, Arathi 27.0,58.8 | Off route. The ch19/25 Refuge Pointe visits are ~20 units away, inside a level 30-40 area |

The bandage tooltips list the skill needed to *use* each one (Heavy Linen 20, Wool 50, Heavy Wool 75, Silk 100, Heavy Silk 125). Those are Classic values too, not a Forever change.

**Forever First Aid extras (Blizzard Watch, beta):**

- **Healing potions:** Minor (skill 1: Peacebloom + Mild Spices), Lesser (55: Briarthorn + 2 Mild Spices), Healing Potion (110: Bruiseweed + Hot Spices; restores 280-360, usable in combat).
- **Curatives:** Simple Poultice (90, disease), Woolen Tourniquet (120, bleed).

He has no Herbalism, so the herbs come from the AH. Healing Potions are worth carrying for dungeons from about ch10.

**Manual drops on route:**

- Manual: Strong Anti-Venom: Duskwood undead (Flesh Eater, Skeletal Warrior/Horror/Mage), which ch17 kills.
- Manual: Clever Poultice: Defias Enchanter, Duskwood, level 26.

**First Aid Kit:** 3 Linen Bandage + 1 Refreshing Spring Water. Stamina buff, Fortitude-exclusive (spell 1230117). Stamina weight for grinding is 0, so this is a dungeon object.

## 6. Prioritized insertion points

Each proposed line is Guidelime syntax ready to paste. Coordinates are Forever DB centroids.

### P1: fixes a real gap or adds XP

1. **01b, after line 21** ("At [TAR1699 Gremlock Pilsnor], learn Cooking ..."):
   - `[OC]|cffffcc00Cooking (Forever):|r eat a cooked food for 10 sec = Well Fed for 15 min: a stat buff plus 5% more XP from kills - eat it while you drink. Charred Wolf Meat and Boiled Clams give no buff; Roasted Boar Meat and Beer Basted Boar Ribs give +1 Str. Cook every Chunk of Boar Meat you loot - aim for Cooking 50 by level 12-15 (Journeyman needs 50 and level 10)`
   - `At [TAR1691 Kreg Bilmn], [V] buy 1 Flint and Tinder and 10 Simple Wood (each Basic Campfire Kit uses 1 Simple Wood) [G47.2,52.4 Dun Morogh]`
   - `[O]At [TAR1692 Golorn Frostbeard], [V] buy 10 Mild Spices (Spiced Wolf Meat, Herb Baked Egg, later pies) and a Fishing Pole if you will fish [G46.7,53.5 Dun Morogh]`
2. **01b, line 20:** change "buy 1 [CI2894,1 Rhapsody Malt]" to buy 1 plus ~10 spares. Then **after line 81** ("[QT384]"):
   - `Learn the Recipe: Beer Basted Boar Ribs (Cooking 25) and cook every spare Crag Boar Rib (1 Rhapsody Malt each, Innkeeper Belm) [G46.8,52.4 Dun Morogh]`
3. **02, after line 38** (Yanni Stoutheart [V]):
   - `At [TAR1465 Drac Roughcut] beside Yanni, [V] buy Recipe: Smoked Bear Meat (Cooking 40, +1 Str) and 10 Mild Spices; cook the Bear Meat from the north loop (roast Mountain Boar meat to 40 first if you are short) [G35.6,49.1 Loch Modan]`
4. **02, after line 57** (Balthus Stoneflayer, Ironforge trip):
   - `[O]At [TAR5159 Daryl Riknussun] on the east side of the Great Forge, learn Journeyman Cooking if you are Cooking 50 (Apprentice stops at 75, and the Crocolisk Steak recipe at the lodge needs 80) [G60.1,36.4 Ironforge]`
   - `[O]At [TAR5150 Nissa Firestone], learn Journeyman First Aid at First Aid 50 [G55.1,58.3 Ironforge]`
5. **03, after line 13** ("In the Commons, [R][V] and stock 20+ water"), because this is the last Ironforge visit before 04:33:
   - `At [TAR5159 Daryl Riknussun], learn Journeyman Cooking now if you skipped it - you must have it before Marek's Crocolisk Steak recipe in 16-17 Loch Modan [G60.1,36.4 Ironforge]`
   - `[O]At [TAR5150 Nissa Firestone], Journeyman First Aid if you have not [G55.1,58.3 Ironforge]`
6. **14, after line 70** (Chef Grual, Dusky Crab Cakes):
   - `[O]At [TAR272 Chef Grual], [QA90 Seasoned Wolf Kabobs] (2,000 XP, requires 18: 10 Lean Wolf Flank from the Rabid Dire Wolves around Abercrombie's shack in chapter 17 plus Stormwind Seasoning Herbs from Felicia Gump in chapter 15; the reward Recipe: Seasoned Wolf Kabob needs Cooking 100) [G73.8,43.5 Duskwood]`
   - **15, after line 68** (Elling Trias, Trade District): `[O]At [TAR1303 Felicia Gump] (herbs, by the Trade District gate), buy [CI2665,1 Stormwind Seasoning Herbs] for Seasoned Wolf Kabobs [G69.3,71.3 Stormwind City]`
   - **17, after line 26** (Abercrombie, first visit): `[O]Kill [TAR565 Rabid Dire Wolf] around the shack for 10 Lean Wolf Flank [QC90] [G27.7,31.1 Duskwood]` (Starving Dire Wolves at 36.2,24.4 drop them too)
   - **17, after line 45** (Tavernkeep Smitts): `[O]At [TAR272 Chef Grual], [QT90] [G73.8,43.5 Duskwood]`

### P2: best-food recipe stops

7. **02, line 69** (Khara Deepwater), extend it or add after it:
   - `[O]At [TAR1684 Khara Deepwater], buy Recipe: Longjaw Mud Snapper (Cooking 50: +10 attack power for 15 min, the best food you can make until 25) if you fish; the loch at her dock gives Raw Longjaw Mud Snapper [G40.3,39.3 Loch Modan]`
8. **02, after line 114** ([QT418]):
   - `Learn the Recipe: Blood Sausage (Cooking 60, +3 Str); Bear Meat, Boar Intestines and Spider Ichor keep dropping from the north-loop bears, boars and Forest Lurkers [G34.8,49.3 Loch Modan]`
9. **04, after line 33** ([QT385]):
   - `Learn the Recipe: Crocolisk Steak (Cooking 80, needs Journeyman) and cook your Crocolisk Meat; bank the Boar Ribs from the Elder Mountain Boars for Succulent Pork Ribs later [G81.8,61.7 Loch Modan]`
10. **06, after line 70** ([QT92]):
    - `Learn Recipe: Redridge Goulash (Cooking 100) and Murloc Fin Soup (90, from Selling Fish) - keep them if you are not there yet [G17.6,43.8 Redridge Mountains]`
    - `[O]At [TAR3085 Gloria Femmel], [V] buy 20 Hot Spices (Succulent Pork Ribs, Gumbo, Gooey Spider Cake, Murloc Fin Soup) [G21.6,43.5 Redridge Mountains]`
11. **08, after line 14** (tram, Stormwind at 20). Not class-filtered; it is 5 units from the tram:
    - `[O]In Old Town at [TAR340 Kendor Kabonka], buy Recipe: Succulent Pork Ribs (Cooking 110: 2 Boar Ribs + Hot Spices, +5 Str - your best meat food from 15 to 25) [G77.5,52.7 Stormwind City]`
12. **12, after line 50** (Silverwind Refuge):
    - `At [TAR3955 Shandrina], buy the Expert Cookbook (read it at Cooking 125 - Journeyman stops at 150) and 10 Hot Spices [G49.5,67.1 Ashenvale]`
    - `[O]At [TAR3960 Ulthaan], buy Recipe: Lean Venison (Cooking 110, +5 Str; Stag Meat from Wild Bucks and Shadowhorn Stags + 4 Mild Spices) [G50.0,66.6 Ashenvale]`
    - `[OC]Kill the Ashenvale Bears you pass: Big Bear Meat, and a chance at Recipe: Bear Brisket (Cooking 175, +10 Str at level 25 - your best food after 25)`
13. **09, after line 100** and **18, after line 45** ([QT471]):
    - `Learn the Recipe: Crocolisk Gumbo (Cooking 120) and cook your Tender Crocolisk Meat [G8.6,55.7 Wetlands]`
14. **18, after line 62** ([QT296]):
    - `Learn the Recipe: Curiously Tasty Omelet (Cooking 130; yellow to 170 - your 150-170 skill-up) with the Raptor Eggs from the Mottled raptors [G38.2,50.9 Wetlands]`

### P3: fishing and First Aid (optional)

15. **01b, line 16** (Eric's Camping 101 line): add `[QA96050 Camping 101: Fishing]` to the optional set.

    **01b, line 59** (Paxton): `[O]At [TAR1700 Paxton Ganter], learn Fishing, fish Iceflow Lake to 20 (about 15 min), then [QT96050] - Fish Bowl (+8% all stats, not with Blessing of Kings; 1 Raw Brilliant Smallfish + 1 Empty Vial each). Bank 10-20 smallfish. You place ONE camp object per hour, so compare it with your Lodestone [G35.4,40.2 Dun Morogh]`
16. **01b, after line 25** (Thamner Pol): `[OC]Bandage every Linen Cloth (troggs and Frostmane drop it); at First Aid 20 craft First Aid Kits (3 Linen Bandage + 1 Refreshing Spring Water) and hand in Camping 101: First Aid`
17. **07, after line 11** (Catherine Leland): `[O]Next to her, [TAR5493 Arnold Leland] trains Fishing (Journeyman at 50) [G55.0,69.7 Stormwind City]`
18. **05 or 07** (Westfall Defias): `[OC]First Aid: switch to Wool Bandages at 80 - Defias drop Wool; Heavy Wool at 115; Healing Potion (First Aid 110, Bruiseweed + Hot Spices from the AH) is worth carrying into the Deadmines`
19. **23, after line 41** ([QT555]): `[O]At [TAR2383 Lindea Rabonne], buy Recipe: Mithril Head Trout (Cooking 175, +20 attack power) if you fish [G50.6,61.0 Hillsbrad Foothills]`
20. **Wording fixes:** 01a:8, 01b:9 and 06:30 say "XP trickle". Change to "+5% XP from kills while Well Fed (15 min)". Add "Fishing 20, Kings-exclusive" to the Fish Bowl mention at 01a:10.

## Unverified / open

- **Journeyman requirements:** skill 50 / level 10, Expert 125, Artisan level 35 — Classic values and kami-labs.
- **Which trainers teach Journeyman:** Gremlock? Cook Ghilm at Gol'Bolar 68.4,54.5?
- **Trainer recipe lists:** Spiced Wolf Meat, Herb Baked Egg, Dry Pork Ribs, Crab Cake, Coyote Steak are Classic values.
- **Skill-up colours and drop rates** for all recipes.
- **Catch tables per zone.**
- **Lodestone and First Aid Kit values:** the tooltips show unresolved level tables.
- **Fish Bowl reagents:** web source only.
- **Cookie's Feast blueprint and Journeyman Campfire drops in the Deadmines:** web claims; the DB has no source.

**Web sources used:**

- [Warcraft Tavern – Cooking Overview](https://www.warcrafttavern.com/forever/guides/cooking/)
- [Warcraft Tavern – Camping Objects & Buffs](https://www.warcrafttavern.com/forever/guides/camping-objects-buffs/)
- [Warcraft Tavern – Cooked Food Provides an XP Buff](https://www.warcrafttavern.com/forever/news/cooked-food-provides-an-xp-buff-in-world-of-warcraft-forever)
- [Warcraft Tavern – New Cooking Recipes](https://www.warcrafttavern.com/forever/news/new-cooking-recipes-for-world-of-warcraft-forever/)
- [Warcraft Tavern – Fishing Overview](https://www.warcrafttavern.com/forever/guides/fishing/)
- [Warcraft Tavern – First Aid Overview](https://www.warcrafttavern.com/forever/guides/first-aid/)
- [Warcraft Tavern – First Aid Profession Preview](https://www.warcrafttavern.com/forever/news/first-aid-profession-preview-for-world-of-warcraft-forever/)
- [Blizzard Watch – First Aid overhaul](https://blizzardwatch.com/2026/10/16/first-aid-getting-new-recipes-updates-world-warcraft-forever/)
- [wow-professions – Forever Camping Guide](https://www.wow-professions.com/forever/camping-guide)
- [kami-labs – Forever cooking guide](https://kami-labs.fr/en/guide-cuisine-wow-forever/)

Icy Veins and Mobalytics refused fetches. The gfinity cooking guide was read but not relied on: its camp objects contradict the datamined tooltips.
