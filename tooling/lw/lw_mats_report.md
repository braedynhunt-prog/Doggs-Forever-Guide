# Leatherworking materials plan: Dwarf Enhancement Shaman, WoW Forever (levels 1-30, skill 1-150)

Built 27 Oct 2026 from the Wowhead Forever leatherworking recipe table (601 spells), the skill-page item lists, the Forever leather source tables, Questie's Forever item DB and ~120 fresh Wowhead Forever tooltips. Script: `lwcalc.py` + `report.py` in this folder; numbers are reproducible from `lw_calc.json`.

## Headline

- **Pristine Leather: 25** for the six pattern-sold Totemic pieces (Belt 2, Gloves 2, Boots 3, Hood 4, Tunic 6, Leggings 8). Armor, Pants and Helm need none. This is the bottleneck. The data has no Forever samples; player comments report roughly 1 per 600 skins and a 5g-each vendor in Riverglade. Expect about 2 from the route, so you are about 23 short.
- **Sulfuric Acid: 27** for the eight pieces to skill 125, **30** with the Helm, so **54 / 60 Pyrite** plus 27 / 30 Empty Vials (Alchemy 40 craft: 2 Pyrite + 1 Empty Vial).
- Skill path 1-125 with all eight Totemic crafts uses about 149 crafts. Light Leather 258, Medium Leather 250, Light Hide 15, Medium Hide 9.
- By the end of chapter 26 the guide route alone gives roughly 255 Light Leather, 155 Medium Leather, 5 Light Hide and 12 Medium Hide (central estimate). Light Leather roughly breaks even, but most of it arrives after you need it. You are short about 95 Medium Leather, 10 Light Hide and 23 Pristine Leather. Section F has the numbers.

## A. Leatherworking skill path 1 → 150

Model: one craft at a time, expected values. Orange = 1.0 skill-up. From yellow to grey the chance is (grey − skill)/(grey − yellow). Green uses the same formula; grey = 0. Crafts are whole numbers, so each segment is rounded up. Totemic pieces are crafted at the first skill where you can learn them. Cured Light Hide (15, for Belt/Gloves/Armor/Boots/Pants) is crafted at 30-45 while it is orange. Cured Medium Hide (9 for Hood/Tunic/Leggings, +2 for the Helm) is crafted from 75 while it is orange. Filler recipes come only from the trainer or the starting recipes: Light Armor Kit and the Handstitched pieces. At each craft the script picks the cheapest one by expected material cost per skill point. Costs are in Light Leather equivalents: LL 1, Medium Leather 2.5, Light Hide 15, Medium Hide 40 (the two hides are scarce, so fillers avoid them), Heavy Leather 3 from 125 (once you skin level 30+ beasts), thread/salt/dye at vendor price.

Training: Apprentice to 75, Journeyman at 50 (character level 10), Expert at 125 (character level 20). The Totemic patterns are bought at 60/75/85/100/110/125 skill from Daniel Stitchsong, 30 Merchant's Favor each.

| Skill | Crafts | Recipe (colours O/Y/G/Gr) | Source | Reagents per craft | Reagents total |
|---|---:|---|---|---|---|
| 1-30 | 29 | Light Armor Kit (0/30/45/60) | starter | 1 Light Leather | 29 Light Leather |
| 30-45 | 15 | Cured Light Hide (for Totemic) (30/50/60/70) | trainer | 1 Light Hide, 1 Salt | 15 Light Hide, 15 Salt |
| 45-51 | 15 | Light Armor Kit (0/30/45/60) | starter | 1 Light Leather | 15 Light Leather |
| 51-60 | 9 | Embossed Leather Gloves (40/70/85/100) | trainer | 3 Light Leather, 2 Coarse Thread | 27 Light Leather, 18 Coarse Thread |
| 60-61 | 1 | Totemic Leather Belt **(Totemic)** (60/90/105/120) | pattern item | 10 Light Leather, 2 Cured Light Hide, 2 Pristine Leather, 1 Coarse Thread, 1 Sulfuric Acid | 10 Light Leather, 2 Cured Light Hide, 2 Pristine Leather, 1 Coarse Thread, 1 Sulfuric Acid |
| 61-75 | 15 | Embossed Leather Gloves (40/70/85/100) | trainer | 3 Light Leather, 2 Coarse Thread | 45 Light Leather, 30 Coarse Thread |
| 75-76 | 1 | Totemic Leather Gloves **(Totemic)** (75/100/112/125) | drop/pattern item | 12 Light Leather, 3 Cured Light Hide, 2 Pristine Leather, 1 Fine Thread, 2 Sulfuric Acid | 12 Light Leather, 3 Cured Light Hide, 2 Pristine Leather, 1 Fine Thread, 2 Sulfuric Acid |
| 76-80 | 4 | Cured Medium Hide (for Totemic) (75/90/97/105) | trainer | 1 Medium Hide, 1 Salt | 4 Medium Hide, 4 Salt |
| 80-80 | 1 | Totemic Leather Armor **(Totemic)** (0/80/80/80) | no pattern found | 16 Light Leather, 2 Cured Light Hide, 1 Sulfuric Acid | 16 Light Leather, 2 Cured Light Hide, 1 Sulfuric Acid |
| 80-85 | 5 | Cured Medium Hide (for Totemic) (75/90/97/105) | trainer | 1 Medium Hide, 1 Salt | 5 Medium Hide, 5 Salt |
| 85-86 | 1 | Totemic Leather Boots **(Totemic)** (85/110/122/135) | pattern item | 14 Light Leather, 4 Cured Light Hide, 3 Pristine Leather, 1 Fine Thread, 3 Sulfuric Acid | 14 Light Leather, 4 Cured Light Hide, 3 Pristine Leather, 1 Fine Thread, 3 Sulfuric Acid |
| 86-88 | 2 | Cured Medium Hide (for Totemic) (75/90/97/105) | trainer | 1 Medium Hide, 1 Salt | 2 Medium Hide, 2 Salt |
| 88-98 | 13 | Fine Leather Belt (55/85/100/115) | trainer | 6 Light Leather, 2 Coarse Thread | 78 Light Leather, 26 Coarse Thread |
| 98-100 | 2 | Gray Leather Boots (75/100/112/125) | trainer | 4 Medium Leather, 2 Fine Thread, 1 Gray Dye | 8 Medium Leather, 4 Fine Thread, 2 Gray Dye |
| 100-101 | 1 | Totemic Leather Hood **(Totemic)** (100/125/137/150) | drop/pattern item | 8 Medium Leather, 2 Cured Medium Hide, 4 Pristine Leather, 2 Fine Thread, 4 Sulfuric Acid | 8 Medium Leather, 2 Cured Medium Hide, 4 Pristine Leather, 2 Fine Thread, 4 Sulfuric Acid |
| 101-105 | 5 | Gray Leather Boots (75/100/112/125) | trainer | 4 Medium Leather, 2 Fine Thread, 1 Gray Dye | 20 Medium Leather, 10 Fine Thread, 5 Gray Dye |
| 105-105 | 1 | Totemic Leather Pants **(Totemic)** (0/105/105/105) | no pattern found | 8 Medium Leather, 4 Cured Light Hide, 2 Sulfuric Acid | 8 Medium Leather, 4 Cured Light Hide, 2 Sulfuric Acid |
| 105-110 | 6 | Gray Leather Boots (75/100/112/125) | trainer | 4 Medium Leather, 2 Fine Thread, 1 Gray Dye | 24 Medium Leather, 12 Fine Thread, 6 Gray Dye |
| 110-111 | 1 | Totemic Leather Tunic **(Totemic)** (110/135/147/160) | pattern item | 10 Medium Leather, 3 Cured Medium Hide, 6 Pristine Leather, 3 Fine Thread, 6 Sulfuric Acid | 10 Medium Leather, 3 Cured Medium Hide, 6 Pristine Leather, 3 Fine Thread, 6 Sulfuric Acid |
| 111-115 | 8 | Gray Leather Boots (75/100/112/125) | trainer | 4 Medium Leather, 2 Fine Thread, 1 Gray Dye | 32 Medium Leather, 16 Fine Thread, 8 Gray Dye |
| 115-121 | 9 | Dark Leather Cloak (85/110/122/135) | trainer | 8 Medium Leather, 1 Fine Thread, 1 Gray Dye | 72 Medium Leather, 9 Fine Thread, 9 Gray Dye |
| 121-125 | 4 | Hillman's Leather Gloves (120/145/157/170) | trainer | 14 Medium Leather, 4 Fine Thread | 56 Medium Leather, 16 Fine Thread |
| 125-126 | 1 | Totemic Leather Leggings **(Totemic)** (125/150/160/170) | drop/pattern item | 12 Medium Leather, 4 Cured Medium Hide, 8 Pristine Leather, 3 Fine Thread, 8 Sulfuric Acid | 12 Medium Leather, 4 Cured Medium Hide, 8 Pristine Leather, 3 Fine Thread, 8 Sulfuric Acid |
| 126-130 | 4 | Heavy Armor Kit (125/145/155/165) | trainer | 5 Heavy Leather, 1 Fine Thread | 20 Heavy Leather, 4 Fine Thread |
| 130-130 | 1 | Totemic Leather Helm **(Totemic)** (0/130/130/130) | no pattern found | 12 Medium Leather, 2 Cured Medium Hide, 3 Sulfuric Acid | 12 Medium Leather, 2 Cured Medium Hide, 3 Sulfuric Acid |
| 130-150 | 21 | Heavy Armor Kit (125/145/155/165) | trainer | 5 Heavy Leather, 1 Fine Thread | 105 Heavy Leather, 21 Fine Thread |

Result: 1 → 150.6 in 175 crafts.

Notes on the path:

- **Totemic Armor (80), Pants (105) and Helm (130) give no skill-up.** Their colours are [0, N, N, N] (grey as soon as learned), and no Pattern item for them exists in the data. They are counted as crafts with 0 gain.
- The Fine Leather Belts from 88-98 are left over (13-15 belts). Vendor them or use them for Dark Leather Belts later.
- Path to 125 only (no Helm): the same as above, except the two extra Cured Medium Hides at 86-88 are not made, so it takes 15 Fine Leather Belts at 86-98 instead of 13. It ends at 126.3 after the Leggings, in 149 crafts.
- **125-150 without Heavy Leather** (if you stay on route materials only): 126-130 4x Hillman's Leather Gloves; 130-130 1x Totemic Leather Helm; 130-150 21x Hillman's Leather Gloves. That costs 612 Medium Leather in total, which is far worse. Heavy Armor Kits from skinned Heavy Leather (level 30-40 beasts) are the realistic 125-150 path, and Forceful/Mystic Heavy Armor Kits need Heavy Armor Kits as a reagent anyway.
- Optional ways to save leather: the trainer's Medium Leather conversion (4 Light Leather → 1 Medium Leather, 75/75/80/85) gives points at 75-85 and turns surplus Light Leather into Medium. Heavy Leather (5 Medium → 1 Heavy, 125/125/130/135) works the same way at 125-130.

## B. Totemic Leather set (and Brawler's for the hunter)

Stats are from the Forever tooltips. "Pattern" gives the Pattern item, its `recipeItems.source` (5 = vendor, 2 = drop) and the vendors and drop NPCs in Questie's Forever DB. Vendors 256734 = **Daniel Stitchsong** (Azeroth Commerce Authority merchant camp, Redridge border) and 248201 = **Pawani** (Durotar Supply and Logistics, Horde side). The 30 Merchant's Favor price comes from the guide note, not from the data.

| Piece | Req lvl | ilvl | LW (O/Y/G/Gr) | Stats | Reagents | Pattern (source) |
|---|---:|---:|---|---|---|---|
| Belt | 12 | 17 | 60 (60/90/105/120) | +4 Strength, +3 Stamina, +4 spell power | 10 Light Leather, 2 Cured Light Hide, 2 Pristine Leather, 1 Coarse Thread, 1 Sulfuric Acid | 252768 (vendor) |
| Gloves | 15 | 20 | 75 (75/100/112/125) | +4 Strength, +3 Stamina, +5 spell power | 12 Light Leather, 3 Cured Light Hide, 2 Pristine Leather, 1 Fine Thread, 2 Sulfuric Acid | 252780 (drop/vendor; also drops from Bazzalan) |
| Armor | 15 | 20 | 80 (0/80/80/80) | +7 Strength, +3 Stamina, +3 Intellect, +6 spell power | 16 Light Leather, 2 Cured Light Hide, 1 Sulfuric Acid | no Pattern item in the data; no source found |
| Boots | 17 | 22 | 85 (85/110/122/135) | +5 Strength, +4 Stamina, +6 spell power | 14 Light Leather, 4 Cured Light Hide, 3 Pristine Leather, 1 Fine Thread, 3 Sulfuric Acid | 252789 (vendor) |
| Hood | 20 | 25 | 100 (100/125/137/150) | +10 Stamina, +9 spell power | 8 Medium Leather, 2 Cured Medium Hide, 4 Pristine Leather, 2 Fine Thread, 4 Sulfuric Acid | 252801 (drop/vendor; also drops from Lord Pythas, Deathsworn Captain, Wolf Master Nandos, Verdan the Everliving) |
| Pants | 20 | 25 | 105 (0/105/105/105) | +9 Strength, +4 Stamina, +4 Intellect, +7 spell power | 8 Medium Leather, 4 Cured Light Hide, 2 Sulfuric Acid | no Pattern item in the data; no source found |
| Tunic | 22 | 27 | 110 (110/135/147/160) | +8 Strength, +6 Stamina, +5 Intellect, +7 spell power | 10 Medium Leather, 3 Cured Medium Hide, 6 Pristine Leather, 3 Fine Thread, 6 Sulfuric Acid | 252808 (vendor) |
| Leggings | 25 | 30 | 125 (125/150/160/170) | +9 Strength, +7 Stamina, +6 Intellect, +8 spell power | 12 Medium Leather, 4 Cured Medium Hide, 8 Pristine Leather, 3 Fine Thread, 8 Sulfuric Acid | 252823 (drop/vendor; also drops from Aku'mai, Gelihast) |
| Helm | 25 | 30 | 130 (0/130/130/130) | +13 Stamina, +12 spell power | 12 Medium Leather, 2 Cured Medium Hide, 3 Sulfuric Acid | no Pattern item in the data; the item itself is a BoP drop from 14 dungeon bosses |

- **No Totemic bracers, shoulders or cloak exist** in the recipe table. The set is Belt, Gloves, Armor/Tunic (chest), Boots, Pants/Leggings (legs) and Hood/Helm (head), so you wear either Armor or Tunic, Pants or Leggings, Hood or Helm.
- **Armor, Pants, Helm:** these recipes have no source, no Pattern item, and grey colours. Questie lists no drops or vendors for the Armor or Pants items. Their tooltips also lack durability, which suggests the data is unfinished. The guide's chapter-06 note says Stitchsong sells Armor 15 and Pants 20. Treat that as unverified until you see it in game. The **Helm** is a BoP boss drop: Dextren Ward, Kam Deepfury, Bazil Thredd, Interrogator Vishas, Charlga Razorflank, Aggem Thorncurse, Aku'mai, Old Serra'kis, Twilight Lord Kelris, Gelihast, Fallen Champion, Azshir the Sleepless, Baron Aquanis, Lorgus Jett (Stockade, BFD, RFK, SM). The guide's BFD/RFK notes already rank the Defender's Helm (+12 Str +13 Sta) above the Totemic Helm. The crafted totals below still include all three, as you asked. Section C lists the Armor/Pants/Helm share separately so you can subtract it.

**Brawler's Leather (Str/Agi/Sta).** Same skill levels, colours and reagents as Totemic, except **Shadowgem** replaces Sulfuric Acid, in the same counts.

| Piece | Req | LW | Stats | Unique reagent | Pattern (source / drops) |
|---|---:|---:|---|---|---|
| Belt | 12 | 60 | +4 Strength, +4 Agility, +3 Stamina | 1 Shadowgem | 252765 (vendor) |
| Gloves | 15 | 75 | +4 Strength, +4 Agility, +3 Stamina | 2 Shadowgem | 252777 (drop/vendor; Captain Greenskin) |
| Armor | 15 | 80 | +5 Strength, +7 Agility, +3 Stamina, +3 Spirit | 1 Shadowgem | none |
| Boots | 17 | 85 | +5 Strength, +5 Agility, +4 Stamina | 3 Shadowgem | 252786 (vendor) |
| Hood | 20 | 100 | +8 Agility, +10 Stamina | 4 Shadowgem | 252798 (drop/vendor; Lord Pythas, Skum) |
| Pants | 20 | 105 | +6 Strength, +9 Agility, +4 Stamina, +4 Spirit | 2 Shadowgem | none |
| Tunic | 22 | 110 | +6 Strength, +8 Agility, +6 Stamina, +5 Spirit | 6 Shadowgem | 252805 (vendor) |
| Legguards | 25 | 125 | +7 Strength, +9 Agility, +7 Stamina, +6 Spirit | 8 Shadowgem | 252820 (drop/vendor; Bazil Thredd, Twilight Lord Kelris, Gelihast) |
| Helm | 25 | 130 | +10 Agility, +13 Stamina | 3 Shadowgem | none (item drops from dungeon bosses, BoP) |

Brawler's totals for all nine pieces: 25 Pristine Leather and 30 Shadowgem (no Sulfuric Acid). The leather and hides are the same as Totemic. For a hunter, **Trapper's Leather** (Belt: +4 Agi +4 Sta +3 Int, made with Deviate Scale) is the Agility/Intellect variant. It is worth a look before the hunter commits to Brawler's.

## C. Grand total of raw materials

These totals cover every craft in section A, including the Cured Light/Medium Hide crafts and the Totemic pieces. Cured hides are broken down into hide + Salt.

| Material | (1) Path to 125 + 8 Totemic pieces | (2) Path to 150 + Helm (Heavy Armor Kits 126-150) | (2b) to 150, Medium Leather only |
|---|---:|---:|---:|
| **Skinned** | | | |
| Light Leather (2318) | 258 | 246 | 246 |
| Light Hide (783) | 15 | 15 | 15 |
| Medium Leather (2319) | 250 | 262 | 612 |
| Medium Hide (4232) | 9 | 11 | 11 |
| Heavy Leather (4234) | 0 | 125 | 0 |
| **Vendor** | | | |
| Coarse Thread (2320) | 79 | 75 | 75 |
| Fine Thread (2321) | 77 | 102 | 177 |
| Salt (4289) | 24 | 26 | 26 |
| Gray Dye (4340) | 30 | 30 | 30 |
| **New Forever reagents** | | | |
| Pristine Leather (249427) | 25 | 25 | 25 |
| Sulfuric Acid (249410) | 27 | 30 | 30 |
| *Sulfuric Acid → Pyrite (249391)* | 54 | 60 | 60 |
| *Sulfuric Acid → Empty Vial (3371)* | 27 | 30 | 30 |

Share of the totals for the three unverified pieces (subtract it if they turn out not to be craftable): Armor = 16 Light Leather, 2 Light Hide, 2 Salt, 1 Acid. Pants = 8 Medium Leather, 4 Light Hide, 4 Salt, 2 Acid. Helm = 12 Medium Leather, 2 Medium Hide, 2 Salt, 3 Acid. Skipping Armor and Pants also cuts the Cured Light Hide quota from 15 to 9. The 6 missing skill points then come from about 6 more Light Armor Kits/Embossed Gloves, roughly 15 Light Leather.

The Totemic pieces alone (all nine, hides as hide + Salt): 52 Light Leather (2318), 50 Medium Leather (2319), 30 Sulfuric Acid (249410), 26 Salt (4289), 25 Pristine Leather (249427), 15 Light Hide (783), 11 Medium Hide (4232), 10 Fine Thread (2321), 1 Coarse Thread (2320).

## D. Sulfuric Acid

Sulfuric Acid (249410) is a new Forever reagent. The only source is the Alchemy recipe 1249633, learned at Alchemy 40 (colours 40/50/70/90): **2 Pyrite, 1 Empty Vial** per Acid. Pyrite (249391) is a new Forever 'Scarce' reagent that comes only from mining nodes (Questie lists 11 objects: Copper, Tin, Silver and Iron vein ids). Empty Vial is a vendor item (115 vendors).

| Piece | Belt | Gloves | Armor | Boots | Hood | Pants | Tunic | Leggings | Helm |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Acid | 1 | 2 | 1 | 3 | 4 | 2 | 6 | 8 | 3 |

- **To 125 (8 pieces): 27 Sulfuric Acid = 54 Pyrite + 27 Empty Vials.**
- **With the Helm: 30 Acid = 60 Pyrite + 30 Vials.**
- Only the six pieces whose patterns are sold (no Armor/Pants/Helm): 24 Acid = 48 Pyrite.
- You have neither Mining nor Alchemy, so buy the Acid (or Pyrite plus an alchemist's time) on the Auction House. The merchant-camp AH is right next to Stitchsong.

## E. Pristine Leather (249427), the bottleneck

**Needed: 25** (Belt 2, Gloves 2, Boots 3, Hood 4, Tunic 6, Leggings 8; Armor, Pants and Helm use none). Brawler's needs the same 25.

What the data says:

- **Skinned-from** has only 5 rows, all named or rare beasts, with tiny all-time samples and **no Forever samples** (fcount 0): Daggerfang (lvl 15) 3/294 = 1.0%, stacks {2: 66.6667,3: 33.3333}; Echeyakee (lvl 16) 3/632 = 0.5%; Lakota'mani (lvl 22) 2/354 = 0.6%; Snarlflare (lvl 18) 1/96 = 1.0%; Thunderstomp (lvl 24) 1/158 = 0.6%. **Daggerfang is on your route** (Loch Modan, chapter 02, with a second try in chapter 16-17): about a 1% chance of 2-3.
- **Dropped-by** has 80 beasts with 663 drops in 4,389,751 kills (0.015%, about 1 in 6,621). Forever-only drops: 0. Those kill counts include pre-Forever kills of the same mobs, so this rate is meaningless. Questie lists 105 beasts as sources. Top rows: Sunscale Scytheclaw 45/168,822; Great Goretusk 28/173,117; Rabid Dire Wolf 28/85,524; Zhevra Runner 27/116,578; Greater Plainstrider 22/213,383. Stacks are 2-3 (about 2.4 on average).
- **The 12 player comments (Sep-Oct 2026):**
  - 2026-09-18: "Got 2 off The named kodo in mulgore"
  - 2026-09-20: "This started dropping from level 18 mobs as soon as i hit skinning 150."
  - 2026-09-20: "I got 2 from skinning a boar in westfall @lvl 13 with 75 skinning"
  - 2026-09-21: "Just skinned 2 from a worgen in Silverpine. I was doing Arugal's Folly, so it was either a Moonrage Glutton or a Moonrage Darksoul."
  - 2026-09-22: "Skinned one off of a lvl 14 or 15 crocodile at skill 108"
  - 2026-10-04: "It looks like the drop rate is abysmal. I've been farming these for hours off the wyverns in Stonetalon. I only got one drop of 2x, thats it. The last hour about, I had 2/5 Boutiful harvest, but I didn't get any additional …"
  - 2026-10-05: "Got 10 of it from Wailing Caverns, was skinning raptors, crocolisks and some serpents with snakes but i dont remember what was my skinning skill, but around 150 for sure"
  - 2026-10-09: "the drop rate needs to be fixed this is worse then hunting for artic fur back in wath im 225 skinning duskwood for 5 hours lvl 25 to 29 mobs got 0 of them wetlands for 6 hours got 1 of a lvl 28 crock loch modan 3 hours got 0 …"
  - 2026-10-11: "Why is this considered "dropped by" rather than "skinned from"? Something also seem to be wrong with the drop rate. The past few days I have been farming mobs for several hours, in several spots AND dungeons and haven't gotten …"
  - 2026-10-11: "Y'all need to keep in mind these items are 5g from the vendor in Riverglade near the BMAH. 5g each. That is what they will be worth come live because of their rarity."
  - 2026-10-14: "This skinning rate is tough, at 225 skinning I farmed about 600 Pridemwings in Stonetalon are Mirkfallen Lake and got 1 (off the rare spawn). Then randomly got one from skinning a level 22 ashenvale bear; roughly 1 in 601 or …"
  - 2026-10-18: "This appears to be bugged as I was getting 5-8 a day just questing until i hit level 25. After 25 I have not seen this drop from any skinned mobs, grey mobs or otherwise at all. There is no way this is the meant functionality …"

- **The vendor/price comment (11 Oct):** "Y'all need to keep in mind these items are 5g from the vendor in Riverglade near the BMAH. 5g each." At that price the 25 cost **about 125 g**. That comment is unconfirmed.
- **Rate comments:** the drop works from low skill ("2 from skinning a boar in Westfall @lvl 13 with 75 skinning", "croc at skill 108"). The best measured rate is "roughly 1 in 601 or 0.164%" (600 Pridewings at Skinning 225). Others report "getting 2 in 20+ hours of skinning", "leveled from 1-200 without a single pristine leather drop", and "5-8 a day just questing until i hit level 25. After 25 I have not seen this drop". So it may be level-gated or bugged above 25.
- **What the route gives:** about 475 beast skins (central estimate, section F) × 0.16% × ~2.4 per drop ≈ **2 Pristine Leather by level 30**. You need 25. Even at the most optimistic reported rate (5-8 per day while questing below 25), you would be about 2-3 days short. **Plan to buy it (vendor or AH) or farm it deliberately**. Craft the pieces with the best value per Pristine Leather first: Belt (2), Gloves (2) and Boots (3), all with real slot upgrades. Tunic (6) and Leggings (8) are the expensive ones.

## F. Skinning yield along the guide route

Method: I grepped the 27 dwarf-route chapter files (01a-26; 00a/00b are the human start) for kill and collect steps on skinnable beasts (wolves, boars, bears, cats, crocolisks, raptors, buzzards/condors/vultures, wendigos/yetis, turtles, dragonkin whelps, Nightbane worgen). Explicit "Kill N" counts are used as written. For "collect X" steps, kills = items ÷ an assumed quest-drop rate (~0.6, or ~0.4 for "low drop rate"). Ormer's Revenge (294/295) uses the Classic counts of 10+10. Added on top: 8 BFD and 15 RFK beast trash. Low = written steps only; **central = +50% for beasts killed in passing** (adds, travel, packs); high = +100%.

Per-skin yields by mob level, from the skinned-from tables (all-time samples; Forever-only samples match, e.g. Great Goretusk 72.6% vs 73.1%):

| Mob level | Light Leather /skin | Light Hide /skin | Medium Leather /skin | Medium Hide /skin |
|---|---:|---:|---:|---:|
| <=10 | 0.85 (assumed) | 0.00 (assumed) | - | - |
| 11-15 | 0.75 (60% × 1.25) | 0.05 (5% × 1.00) | - | - |
| 16-20 | 1.03 (69% × 1.50) | 0.05 (5% × 1.00) | - | - |
| 21-25 | 0.63 (42% × 1.50) | - | 0.52 (50% × 1.04) | 0.05 (5% × 1.00) |
| 26-30 | - | - | 0.70 (70% × 1.01) | 0.05 (5% × 1.00) |
| 31+ | - | - | 0.43 (43% × 1.00) | 0.04 (4% × 1.00) |

(≤10 is not in the data. 0.85 Light Leather equivalent assumes Ruined Leather Scraps converted 3 → 1 via the Light Leather recipe.)

Written beast kills per chapter (before the +50%): 01a 26, 01b 67, 02 17, 04 5, 05 19, 06 16, 09 7, 11 1, 13 8, 16 1, 17 10, 18 56, 19 32, 22 6, 23 30, 26 15. All other chapters have 0.

| By end of | Beast skins (low / central / high) | Light Leather | Light Hide | Medium Leather | Medium Hide |
|---|---|---|---|---|---|
| ch 07 Deadmines (lvl 20) | 150 / 225 / 300 | 127 / 191 / 255 | 3 / 5 / 6 | 0 / 0 / 0 | 0 / 0 / 0 |
| ch 14 Duskwood (~26) | 166 / 249 / 332 | 138 / 207 / 276 | 3 / 5 / 6 | 8 / 12 / 16 | 1 / 1 / 2 |
| ch 26 RFK (~30) | 316 / 474 / 632 | 171 / 256 / 342 | 3 / 5 / 6 | 104 / 155 / 207 | 8 / 12 / 16 |

**Route vs need (central estimate at the end of chapter 26):**

| Material | Route (central) | Need, path to 125 | Gap | Need, path to 150 | Gap |
|---|---:|---:|---:|---:|---:|
| Light Leather | 256 | 258 | -2 | 246 | +10 |
| Light Hide | 5 | 15 | -10 | 15 | -10 |
| Medium Leather | 155 | 250 | -95 | 262 | -107 |
| Medium Hide | 12 | 9 | +3 | 11 | +1 |
| Heavy Leather | 0 | 0 | +0 | 125 | -125 |

- **Light Leather:** the path uses all ~258 by skill ~98, which you reach around levels 20-22. The route gives ~190 by level 20 and ~205 by chapter 14, so you are short ~50-70 at the time you need it. It breaks even by level 30.
- **Medium Leather:** short ~95 for the path to 125 (most of it goes on Gray Leather Boots at 98-115 and Dark Leather Cloaks at 115-121). Medium Leather only starts dropping in chapters 17-23, at levels 26-30.
- **Light Hide:** you need 15 (for Cured Light Hide) and the route gives ~5. Short ~10. At 5% per skin of level 11-20 beasts, that is ~200 extra skins, or buy them on the AH.
- **Medium Hide:** you need 9-11 and the route gives ~12, but nearly all of it comes at levels 26-30. The Hood (req 20) and Tunic (req 22) will wait unless you buy hides. Those Cured Medium Hides will also be grey by then, so you lose about 9 cheap skill points.
- **Heavy Leather (125-150):** the route gives none. Expect it from level 30-40 beasts after the guide ends.
- **Verdict:** the route alone does not cover the leather. It roughly covers Light Leather (late) and Medium Hide (late). It is short ~95 Medium Leather, ~10 Light Hide and ~23 Pristine Leather for the path to 125. Reaching 150 needs ~125 Heavy Leather on top.

## G. Later Forever Leatherworking sets

| Set | Armour | Pieces (LW skill) | LW range | Req level |
|---|---|---|---|---|
| Cloudy Gustwoven | Leather | Bracers 50, Belt 50, Gloves 55, Boots 55, Harness 60, Trousers 60, Hood 175, Spaulders 175 | 50-175 | 5-30 |
| Cloudy Windraveled | Leather | Armguards 50, Strap 50, Mitts 55, Footwraps 55, Jerkin 60, Pants 60, Cover 175, Drapes 175 | 50-175 | 5-30 |
| Azure Gustwoven | Leather | Bracers 50, Belt 50, Gloves 55, Boots 55, Harness 60, Trousers 60, Hood 175, Spaulders 175 | 50-175 | 5-30 |
| Azure Windraveled | Leather | Armguards 50, Strap 50, Mitts 55, Footwraps 55, Jerkin 60, Pants 60, Cover 175, Drapes 175 | 50-175 | 5-30 |
| Wisdom's | Leather | Belt 60, Gloves 75, Armor 80, Boots 85, Hood 100, Pants 105, Tunic 110, Leggings 125, Helm 130 | 60-130 | 12-25 |
| Stormrider's | Leather | Belt 60, Gloves 75, Armor 80, Boots 85, Hood 100, Pants 105, Tunic 110, Kilt 125, Helm 130 | 60-130 | 12-25 |
| Defender's | Leather | Belt 60, Gloves 75, Armor 80, Boots 85, Hood 100, Pants 105, Tunic 110, Kilt 125, Helm 130 | 60-130 | 12-25 |
| Trapper's | Leather | Belt 60, Gloves 75, Armor 80, Boots 85, Hood 100, Pants 105, Tunic 110, Legguards 125, Helm 130 | 60-130 | 12-25 |
| Brawler's | Leather | Belt 60, Gloves 75, Armor 80, Boots 85, Hood 100, Pants 105, Tunic 110, Legguards 125, Helm 130 | 60-130 | 12-25 |
| Hillman's | Leather | Boots 110 | 110-110 | 22-22 |
| Mender's (Leather) | Leather | Belt 150, Gloves 175, Shoes 200, Shoulders 210, Bracers 225, Boots 235, Waistguard 250, Gauntlets 250 | 150-250 | 30-50 |
| Skycaller's (Leather) | Leather | Belt 150, Gloves 175, Shoes 200, Shoulders 210, Bracers 225, Boots 235, Waistguard 250, Gauntlets 250 | 150-250 | 30-50 |
| Skirmisher's (Leather) | Leather | Belt 150, Gloves 175 | 150-175 | 30-35 |
| Warden's | Leather | Belt 150, Gloves 175, Shoes 200, Shoulders 210, Bracers 225, Boots 235, Waistguard 250, Gauntlets 250 | 150-250 | 30-50 |
| Stalker's (Leather) | Leather | Belt 150, Gloves 175 | 150-175 | 30-35 |
| Skulker's | Leather | Belt 150, Gloves 175, Shoes 200, Shoulders 210, Bracers 225, Boots 235, Waistguard 250, Gauntlets 250 | 150-250 | 30-50 |
| Prowler's | Leather | Belt 150, Gloves 175, Shoes 200, Shoulders 210, Bracers 225, Boots 235, Waistguard 250, Gauntlets 250 | 150-250 | 30-50 |
| Mender's (Mail) | Mail | Boots 200, Shoulders 210, Bracers 225, Sabatons 235, Belt 250, Gauntlets 250 | 200-250 | 40-50 |
| Skycaller's (Mail) | Mail | Boots 200, Shoulders 210, Bracers 225, Sabatons 235, Belt 250, Gauntlets 250 | 200-250 | 40-50 |
| Skirmisher's (Mail) | Mail | Boots 200, Shoulders 210, Bracers 225, Sabatons 235, Belt 250, Gauntlets 250 | 200-250 | 40-50 |
| Stalker's (Mail) | Mail | Boots 200, Shoulders 210, Bracers 225, Sabatons 235, Belt 250, Gauntlets 250 | 200-250 | 40-50 |
| Charged Scorpid | Mail | Belt 230, Helm 240, Shoulders 250, Gauntlets 255, Bracers 255, Vest 260, Leggings 270, Boots 280 | 230-280 | 46-56 |
| Supple Scorpid | Mail | Boots 230, Leggings 240, Bracers 250, Belt 255, Shoulders 255, Helm 260, Vest 270, Sabatons 280 | 230-280 | 46-56 |
| Blue Suede | Leather | Shoes 235, Gloves 240, Pants 255, Shoulders 260, Armor 265, Belt 270, Bracers 275, Hat 280 | 235-280 | 47-56 |
| Tooled Leather | Leather | Belt 235, Boots 240, Armor 255, Gauntlets 260, Crown 265, Bracers 270, Epaulets 275, Pants 280 | 235-280 | 47-56 |
| Heavy Scorpid | Mail | Boots 255 | 255-255 | 51-51 |
| Wicked Leather | Leather | Boots 260, Shoulders 270 | 260-270 | 52-54 |
| Bileblister | Leather | Claws 285, Girdle 290, Boots 295 | 285-295 | 53-53 |
| Hivethrasher's | Leather | Claws 285, Girdle 290, Boots 295 | 285-295 | 53-53 |
| Scalegut | Mail | Clenchers 285, Belt 290, Treaders 295 | 285-295 | 53-53 |
| Broodwatcher's | Mail | Clenchers 285, Belt 290, Treaders 295 | 285-295 | 53-53 |
| Grovekeeper | Leather | Trousers 300, Grips 300, Shoulderpads 300, Stompers 300, Kilt 300, Mitts 300, Mantle 300, Sandals 300, Legguards 300, Handguards 300, Pauldrons 300, Boots 300, Leggings 300, Gauntlets 300, Spaulders 300, Treads 300 | 300-300 | 60-60 |
| Wildstalker's | Mail | Legguards 300, Gauntlets 300, Spaulders 300, Greaves 300 | 300-300 | 60-60 |
| Grimstitch | Leather | Pants 300, Gloves 300, Spaulders 300, Boots 300 | 300-300 | 60-60 |
| Spiritcaller | Mail | Leggings 300, Grips 300, Spaulders 300, Treads 300, Pants 300, Gauntlets 300, Epaulets 300, Greaves 300, Kilt 300, Gloves 300, Mantle 300, Boots 300 | 300-300 | 60-60 |
| Elderwild | Leather | Waistcord 300, Pants 300 | 300-300 | 60-60 |

Other new Forever items in the table: the boots-only patterns (Black Whelp Slippers, Dark Leather Boots, Murloc Scale Shoes, Moonglow Boots, LW 35, req 10), Hillman's Leather Boots (110, req 22), Light Leather Reagent Bag, Camp Tent and Tanning Rack (camp objects), the level-60 epics (Living Crown, Dawn Armor, Timbermaw Tunic, Warbear Helm, Ironfeather Leggings, Red/Blue/Black Dragonscale, Pristine Scorpid Leggings), Outlaw's Collar, Eternity Pauldrons, Tranquil Wristguards, Mourning Handguards and Wild Leather Armor Kit (all 300). The level-1 "Adaptive" patterns at 285 have no recipe row.

**One representative piece of each 150+ set (Forever tooltip):**

| Set | Piece | Req | Stats |
|---|---|---:|---|
| Skirmisher's (Leather) | Skirmisher's Leather Belt | 30 | +9 Strength, +6 Stamina, +4 Intellect, +7 spell power |
| Skirmisher's (Leather) | Skirmisher's Leather Gloves | 35 | +10 Strength, +7 Stamina, +10 spell power |
| Prowler's (Leather) | Prowler's Leather Belt | 30 | +9 Strength, +6 Agility, +6 Stamina, +4 Intellect |
| Prowler's (Leather) | Prowler's Leather Shoes | 40 | +11 Strength, +7 Agility, +7 Stamina, +5 Intellect |
| Warden's (Leather) | Warden's Leather Belt | 30 | +6 Strength, +6 Agility, +9 Stamina, +38 Armor |
| Skulker's (Leather) | Skulker's Leather Belt | 30 | +6 Strength, +9 Agility, +6 Stamina, +4 Spirit |
| Stalker's (Leather) | Stalker's Leather Belt | 30 | +9 Agility, +6 Stamina, +6 Intellect, +4 Spirit |
| Skycaller's (Leather) | Skycaller's Leather Belt | 30 | +6 Stamina, +6 Intellect, +4 Spirit, +10 spell power |
| Mender's (Leather) | Mender's Leather Belt | 30 | +4 Stamina, +6 Intellect, +6 Spirit, +19 healing/+6 spell dmg |
| Skirmisher's (Mail) | Skirmisher's Mail Boots | 40 | +11 Strength, +7 Stamina, +5 Intellect, +9 spell power |
| Skirmisher's (Mail) | Skirmisher's Mail Belt | 50 | +14 Strength, +10 Stamina, +15 spell power |
| Stalker's (Mail) | Stalker's Mail Belt | 50 | +14 Agility, +12 Stamina, +10 Intellect |
| Skycaller's (Mail) | Skycaller's Mail Belt | 50 | +10 Stamina, +12 Intellect, +16 spell power |
| Mender's (Mail) | Mender's Mail Belt | 50 | +10 Stamina, +12 Intellect, +30 healing/+10 spell dmg |
| Supple Scorpid | Supple Scorpid Vest | 54 | +15 Strength, +16 Stamina, +12 spell power |
| Charged Scorpid | Charged Scorpid Vest | 52 | +15 Intellect, +14 Spirit, +12 spell power |
| Heavy Scorpid | Heavy Scorpid Boots | 51 | +10 Agility, +9 Stamina |
| Blue Suede | Blue Suede Armor | 53 | +16 Strength, +8 Agility, +12 Stamina |
| Tooled Leather | Tooled Leather Armor | 51 | +16 Intellect, +11 Spirit, +12 spell power |
| Wicked Leather | Wicked Leather Boots | 52 | +12 Agility, +12 Stamina |
| Bileblister | Bileblister Girdle | 53 | +17 Stamina, +14 Intellect, +6 Nature Resistance |
| Hivethrasher's | Hivethrasher's Girdle | 53 | +7 Agility, +21 Stamina, +4 Nature Resistance |
| Scalegut | Scalegut Belt | 53 | +14 Agility, +17 Stamina, +6 Nature Resistance |
| Broodwatcher's | Broodwatcher's Belt | 53 | +21 Stamina, +4 Nature Resistance, +16 healing/+5 spell dmg |
| Elderwild | Elderwild Waistcord | 60 | +21 Stamina, +18 Spirit, +30 healing/+10 spell dmg |
| Cloudy/Azure Gustwoven | Cloudy Gustwoven Harness | 7 | +2 Strength |
| Cloudy/Azure Windraveled | Cloudy Windraveled Jerkin | 7 | +2 Intellect |
| Spiritcaller (Mail, Shaman only) | Spiritcaller Leggings / Pants / Kilt | 60 | Artisan's Tier (LW 300): 'The Spiritcaller's **Rage**' (Leggings, Grips, Spaulders, Treads) has 2pc +1% attack/cast speed, 4pc +36 AP vs Elementals and 5pc −0.5 s Stormstrike cooldown. 'Storm' is the Elemental set (+1% hit, Lava Burst); plain 'Spiritcaller' is Restoration. |

**Recommendation (Enhancement):**

For 30-40 in leather, aim for **Skirmisher's Leather**: Belt at LW 150 / req 30 (+9 Str +6 Sta +4 Int +7 spell power) and Gloves at LW 175 / req 35 (+10 Str +7 Sta +10 spell power). It is Totemic's Str/Sta/Int/spell-power profile one tier up. Every 150+ leather set has only a belt (req 30) and gloves (req 35) below req 40. Keep the Totemic pieces in the other slots until 40. From 40, switch to **Skirmisher's Mail** (Boots 40, Shoulders 42, Bracers 45, Sabatons 47, Gauntlets and Belt 50; e.g. Belt +14 Str +10 Sta +15 spell power). Then **Supple Scorpid** (Vest req 54: +15 Str +16 Sta +12 spell power) at 51-56, and **The Spiritcaller's Rage** at 60, the Shaman-only Artisan's Tier set with a Stormstrike cooldown bonus. Prowler's (Str/Agi/Sta/Int) is the fallback if a Skirmisher's pattern is hard to get. Stalker's, Skycaller's and Mender's are hunter, caster and healer sets.

**Forceful / Mystic armor kits** (all pattern items, vendor; for chest, legs, hands or feet):

| Kit | LW (O/Y/G/Gr) | Req | Reagents | Effect (tooltip) |
|---|---|---:|---|---|
| Forceful Medium Armor Kit | 80/95/102/110 | 15 | 1 Medium Armor Kit, 2 Strange Dust, 2 Elixir of Lion's Strength | Attack Power value by 4 and the armor value by 16 |
| Mystic Medium Armor Kit | 80/95/102/110 | 15 | 1 Medium Armor Kit, 2 Strange Dust, 2 Minor Mana Potion | Spell Power value by 2 and the armor value by 16 |
| Forceful Heavy Armor Kit | 135/155/165/175 | 30 | 1 Heavy Armor Kit, 2 Soul Dust, 2 Elixir of Giant Growth | Attack Power value by 0 and armor value by 0 |
| Mystic Heavy Armor Kit | 135/155/165/175 | 30 | 1 Heavy Armor Kit, 2 Soul Dust, 2 Lesser Mana Potion | Spell Power value by 75 and armor value by 0 |
| Forceful Thick Armor Kit | 185/205/215/225 | 40 | 1 Thick Armor Kit, 2 Vision Dust, 2 Elixir of Ogre's Strength | Attack Power value by 0 and armor value by 0 |
| Mystic Thick Armor Kit | 185/205/215/225 | 40 | 1 Thick Armor Kit, 2 Vision Dust, 2 Mana Potion | Spell Power value by 75 and armor value by 0 |
| Forceful Rugged Armor Kit | 235/235/245/255 | 50 | 1 Rugged Armor Kit, 2 Dream Dust, 2 Elixir of Giants, 1 Pristine Scale, 1 Fel Hide | Attack Power value by 0 and armor value by 0 |
| Mystic Rugged Armor Kit | 235/235/245/255 | 50 | 1 Rugged Armor Kit, 2 Dream Dust, 2 Major Mana Potion, 1 Pristine Scale, 1 Fel Hide | Spell Power value by 75 and armor value by 0 |

The Medium kits are readable: **Forceful = +4 Attack Power** (+16 armour), **Mystic = +2 spell power**. For Enhancement, Forceful is the one to use. The Heavy, Thick and Rugged tooltips still show unfilled template values ("Attack Power by 0", "Spell Power by 75"), so their real bonuses cannot be read from the data yet. Assume they scale the same way (Forceful = AP) and check in game.

## Assumptions and uncertainty

- **Skill-up model:** expected values with the Classic formula (grey − skill)/(grey − yellow) from yellow upward, using the integer skill. Real crafting is random; budget about ±10% on filler crafts. Recipes coloured [0, N, N, N] (Totemic Armor/Pants/Helm) are counted as giving 0 points.
- **Filler choice** depends on my cost weights (Light Leather 1, Medium Leather 2.5, Light Hide 15, Medium Hide 40, Heavy Leather 3 after 125). If Medium Leather turns out easier to get than Light Leather, Gray Leather Boots and Dark Leather Cloak take over earlier. The totals move by tens, not hundreds.
- **Timing:** the path assumes the Cured Medium Hides are made at 75-88 while they are orange. On the route, Medium Hide arrives at levels 26-30, so unless you buy hides, those 9-11 crafts will be grey. You then need ~9 more filler crafts (~36 Medium Leather) to cover the lost points.
- **Unverified pieces:** no Pattern item for Totemic Armor/Pants/Helm exists in the data, and the Helm is a BoP dungeon drop. The totals include them because you asked. Section C shows how to subtract them.
- **Forever drop rates:** most skinned-from rows are all-time samples, but the Forever-only samples that exist agree within ~1 percentage point. Light Leather from level 21-25 beasts rests on only two mobs. Medium Leather stack size is taken as 1 where the data gives none. Beasts at level ≤10 are not in the data (0.85 Light Leather equivalent per skin is assumed). Pristine Leather has **zero** Forever samples in the data; its rate comes only from player comments, which suggest it may be bugged or level-gated.
- **Route kill counts** are hand estimates: collect steps ÷ ~0.6, Classic counts for Ormer's Revenge, +50% incidental kills for the central case, and dungeon trash added. They exclude Skinning skill gating (assumes Skinning is kept level with the character) and Waylaid Supplies use.
- **Not resolved:** the Merchant's Favor price (30, from the guide, not the data); whether the Riverglade 5g Pristine Leather vendor exists; Pyrite node rates; the real Heavy/Thick/Rugged kit values.
