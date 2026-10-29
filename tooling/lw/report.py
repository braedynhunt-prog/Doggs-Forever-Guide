"""Builds lw_mats_report.md and lw_mats_totals.json from lw_calc.json + source data."""
import json, os, math, re
from collections import defaultdict, OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
C = json.load(open(os.path.join(HERE, 'lw_calc.json'), encoding='utf-8'))
R = json.load(open(os.path.join(HERE, '..', 'lw', 'lw_recipes_forever.json'), encoding='utf-8'))
SP = json.load(open(os.path.join(HERE, '..', 'lw', 'skill_page_items.json'), encoding='utf-8'))
QDB = json.load(open("/mnt/user-data/uploads/WoW Forever Atlas/tooling/qdb/item.json", encoding='utf-8'))
TIPS = json.load(open(os.path.join(HERE, 'item_tips_new.json'), encoding='utf-8'))
UPTIPS = json.load(open("/mnt/user-data/uploads/WoW Forever Atlas/tooling/item_tips.json", encoding='utf-8'))

NPC = {k.split(':')[1]: v['tip'].split(' Level')[0] for k, v in TIPS.items() if k.startswith('npc:')}
NPC.update({'4421': 'Charlga Razorflank', '4424': 'Aggem Thorncurse', '3670': 'Lord Pythas', '1717': 'Hamhock', '3974': 'Houndmaster Loksey', '4422': 'Agathelos the Raging', '4428': 'Death Speaker Jargba',
            '6168': 'Roogug', '6489': 'Ironspine'})   # Classic ids not fetched (Brawler's Helm only)


def iname(i):
    v = QDB.get(str(i))
    return v[0] if v and v[0] else f'item {i}'


def tip(i):
    i = str(i)
    t = TIPS.get(i) or UPTIPS.get(i)
    return t['tip'] if t else ''


def stats(i):
    t = tip(i)
    parts = re.findall(r'\+\d+ (?:Strength|Agility|Stamina|Intellect|Spirit|Armor|Nature Resistance|Fire Resistance|Frost Resistance|Shadow Resistance|Arcane Resistance)\b', t)
    m = re.search(r'Increases damage and healing done by magical spells and effects by up to (\d+)', t)
    if m:
        parts.append(f'+{m.group(1)} spell power')
    m = re.search(r'Increases healing done by up to (\d+) and damage done by up to (\d+)', t)
    if m:
        parts.append(f'+{m.group(1)} healing/+{m.group(2)} spell dmg')
    return ', '.join(parts)


SRCN = {1: 'crafted', 2: 'drop', 4: 'quest', 5: 'vendor', 6: 'trainer', 16: 'fishing', 21: 'pickpocket'}
SPELLSRC = {2: 'drop', 4: 'quest', 5: 'pattern item', 6: 'trainer'}


def srcs(lst, m=SRCN):
    return '/'.join(m.get(x, str(x)) for x in (lst or [])) or 'none listed'


def reag(lst):
    return ', '.join(f'{n} {nm}' for it, n, nm in lst)


def fl(x):
    return math.floor(x + 1e-9)


out = []
w = out.append

w('# Leatherworking materials plan: Dwarf Enhancement Shaman, WoW Forever (levels 1-30, skill 1-150)\n')
w('Built 27 Oct 2026 from the Wowhead Forever leatherworking recipe table (601 spells), the skill-page item lists, the Forever '
  'leather source tables, Questie\'s Forever item DB and ~120 fresh Wowhead Forever tooltips. Script: `lwcalc.py` + `report.py` '
  'in this folder; numbers are reproducible from `lw_calc.json`.\n')

# ---------------- headline ----------------
t125 = C['to125']['by_category']; t150 = C['to150']['by_category']; tml = C['to150_mlonly']['by_category']
w('## Headline\n')
w(f"- **Pristine Leather: 25** for the six pattern-sold Totemic pieces (Belt 2, Gloves 2, Boots 3, Hood 4, Tunic 6, Leggings 8). "
  "Armor, Pants and Helm need none. This is the bottleneck. The data has no Forever samples; player comments report roughly 1 per 600 skins and a 5g-each vendor in Riverglade. Expect about 2 from the route, so you are about 23 short.")
w(f"- **Sulfuric Acid: 27** for the eight pieces to skill 125, **30** with the Helm, so **54 / 60 Pyrite** plus 27 / 30 Empty Vials (Alchemy 40 craft: 2 Pyrite + 1 Empty Vial).")
w(f"- Skill path 1-125 with all eight Totemic crafts uses about {C['to125']['n_crafts']} crafts. Light Leather {t125['skinned'].get('Light Leather (2318)')}, Medium Leather {t125['skinned'].get('Medium Leather (2319)')}, "
  f"Light Hide 15, Medium Hide 9.")
w("- By the end of chapter 26 the guide route alone gives roughly 255 Light Leather, 155 Medium Leather, 5 Light Hide and 12 Medium Hide (central estimate). "
  "Light Leather roughly breaks even, but most of it arrives after you need it. You are short about 95 Medium Leather, 10 Light Hide and 23 Pristine Leather. Section F has the numbers.\n")

# ---------------- A ----------------
w('## A. Leatherworking skill path 1 → 150\n')
w('Model: one craft at a time, expected values. Orange = 1.0 skill-up. From yellow to grey the chance is (grey − skill)/(grey − yellow). '
  'Green uses the same formula; grey = 0. Crafts are whole numbers, so each segment is rounded up. Totemic pieces are crafted at the first skill where you can learn them. '
  'Cured Light Hide (15, for Belt/Gloves/Armor/Boots/Pants) is crafted at 30-45 while it is orange. Cured Medium Hide (9 for Hood/Tunic/Leggings, +2 for the Helm) is crafted from 75 while it is orange. '
  'Filler recipes come only from the trainer or the starting recipes: Light Armor Kit and the Handstitched pieces. At each craft the script picks the cheapest one by '
  'expected material cost per skill point. Costs are in Light Leather equivalents: LL 1, Medium Leather 2.5, Light Hide 15, Medium Hide 40 (the two hides are scarce, so fillers avoid them), Heavy Leather 3 from 125 '
  '(once you skin level 30+ beasts), thread/salt/dye at vendor price.\n')
w('Training: Apprentice to 75, Journeyman at 50 (character level 10), Expert at 125 (character level 20). The Totemic patterns are bought at 60/75/85/100/110/125 skill from Daniel Stitchsong, 30 Merchant\'s Favor each.\n')
w('| Skill | Crafts | Recipe (colours O/Y/G/Gr) | Source | Reagents per craft | Reagents total |')
w('|---|---:|---|---|---|---|')
for sg in C['to150']['segments']:
    col = '/'.join(str(x) for x in sg['colors'])
    tag = {'totemic': ' **(Totemic)**', 'quota': ' (for Totemic)', 'filler': ''}[sg['forced']]
    tot = ', '.join(f'{v} {k}' for k, v in sg['total_reagents'].items())
    src = srcs(sg['source'], SPELLSRC) if sg['source'] else ('starter' if sg['colors'][0] == 0 and 'Totemic' not in sg['name'] else 'no pattern found')
    w(f"| {fl(sg['start'])}-{fl(sg['end'])} | {sg['crafts']} | {sg['name']}{tag} ({col}) | {src} | {reag(sg['reagents'])} | {tot} |")
w('')
w(f"Result: 1 → {C['to150']['final_skill']:.1f} in {C['to150']['n_crafts']} crafts.\n")
w("Notes on the path:\n")
w("- **Totemic Armor (80), Pants (105) and Helm (130) give no skill-up.** Their colours are [0, N, N, N] (grey as soon as learned), and no Pattern item for them exists in the data. They are counted as crafts with 0 gain.")
w("- The Fine Leather Belts from 88-98 are left over (13-15 belts). Vendor them or use them for Dark Leather Belts later.")
w("- Path to 125 only (no Helm): the same as above, except the two extra Cured Medium Hides at 86-88 are not made, so it takes 15 Fine Leather Belts at 86-98 instead of 13. "
  f"It ends at {C['to125']['final_skill']:.1f} after the Leggings, in {C['to125']['n_crafts']} crafts.")
alt = [sg for sg in C['to150_mlonly']['segments'] if sg['start'] >= 125.9]
w("- **125-150 without Heavy Leather** (if you stay on route materials only): " + '; '.join(
    f"{fl(sg['start'])}-{fl(sg['end'])} {sg['crafts']}x {sg['name']}" for sg in alt) +
  f". That costs {tml['skinned'].get('Medium Leather (2319)')} Medium Leather in total, which is far worse. Heavy Armor Kits from skinned Heavy Leather (level 30-40 beasts) are the realistic 125-150 path, "
  "and Forceful/Mystic Heavy Armor Kits need Heavy Armor Kits as a reagent anyway.")
w("- Optional ways to save leather: the trainer's Medium Leather conversion (4 Light Leather → 1 Medium Leather, 75/75/80/85) gives points at 75-85 and turns surplus Light Leather into Medium. "
  "Heavy Leather (5 Medium → 1 Heavy, 125/125/130/135) works the same way at 125-130.\n")

# ---------------- B ----------------
w('## B. Totemic Leather set (and Brawler\'s for the hunter)\n')
w('Stats are from the Forever tooltips. "Pattern" gives the Pattern item, its `recipeItems.source` (5 = vendor, 2 = drop) and the vendors and drop NPCs in Questie\'s Forever DB. '
  'Vendors 256734 = **Daniel Stitchsong** (Azeroth Commerce Authority merchant camp, Redridge border) and 248201 = **Pawani** (Durotar Supply and Logistics, Horde side). '
  'The 30 Merchant\'s Favor price comes from the guide note, not from the data.\n')
w('| Piece | Req lvl | ilvl | LW (O/Y/G/Gr) | Stats | Reagents | Pattern (source) |')
w('|---|---:|---:|---|---|---|---|')
for t in C['totemic_table']:
    col = '/'.join(str(x) for x in t['colors'])
    if t['pattern']:
        p = t['pattern']
        drops = ', '.join(NPC.get(str(n), str(n)) for n in (p['qdb_npcDrops'] or []))
        pat = f"{p['id']} ({srcs(p['source'])}{'; also drops from ' + drops if drops else ''})"
    else:
        dr = t['item_qdb_npcDrops']
        pat = 'no Pattern item in the data' + (f"; the item itself is a BoP drop from {len(dr)} dungeon bosses" if dr else '; no source found')
    w(f"| {t['name'].replace('Totemic Leather ', '')} | {t['reqlevel']} | {t['ilvl']} | {t['learnedat']} ({col}) | {stats(t['item'])} | {reag(t['reagents'])} | {pat} |")
helm = [t for t in C['totemic_table'] if t['name'].endswith('Helm')][0]
w('')
w("- **No Totemic bracers, shoulders or cloak exist** in the recipe table. The set is Belt, Gloves, Armor/Tunic (chest), Boots, Pants/Leggings (legs) and Hood/Helm (head), "
  "so you wear either Armor or Tunic, Pants or Leggings, Hood or Helm.")
w("- **Armor, Pants, Helm:** these recipes have no source, no Pattern item, and grey colours. Questie lists no drops or vendors for the Armor or Pants items. Their tooltips also lack durability, which suggests the data is unfinished. "
  "The guide's chapter-06 note says Stitchsong sells Armor 15 and Pants 20. Treat that as unverified until you see it in game. "
  f"The **Helm** is a BoP boss drop: {', '.join(NPC.get(str(n), str(n)) for n in helm['item_qdb_npcDrops'])} "
  "(Stockade, BFD, RFK, SM). The guide's BFD/RFK notes already rank the Defender's Helm (+12 Str +13 Sta) above the Totemic Helm. The crafted totals below still include all three, as you asked. "
  "Section C lists the Armor/Pants/Helm share separately so you can subtract it.")
w('')
w('**Brawler\'s Leather (Str/Agi/Sta).** Same skill levels, colours and reagents as Totemic, except **Shadowgem** replaces Sulfuric Acid, in the same counts.\n')
w('| Piece | Req | LW | Stats | Unique reagent | Pattern (source / drops) |')
w('|---|---:|---:|---|---|---|')
for t in C['brawler_table']:
    sg = [f'{n} {nm}' for it, n, nm in t['reagents'] if it == 1210]
    if t['pattern']:
        p = t['pattern']
        drops = ', '.join(NPC.get(str(n), str(n)) for n in (p['qdb_npcDrops'] or []))
        pat = f"{p['id']} ({srcs(p['source'])}{'; ' + drops if drops else ''})"
    else:
        pat = 'none' + (' (item drops from dungeon bosses, BoP)' if t['item_qdb_npcDrops'] else '')
    w(f"| {t['name'].replace(chr(66)+'rawler' + chr(39) + 's Leather ', '')} | {t['reqlevel']} | {t['learnedat']} | {stats(t['item'])} | {', '.join(sg)} | {pat} |")
w('')
w("Brawler's totals for all nine pieces: 25 Pristine Leather and 30 Shadowgem (no Sulfuric Acid). The leather and hides are the same as Totemic. "
  "For a hunter, **Trapper's Leather** (Belt: +4 Agi +4 Sta +3 Int, made with Deviate Scale) is the Agility/Intellect variant. It is worth a look before the hunter commits to Brawler's.\n")

# ---------------- C ----------------
w('## C. Grand total of raw materials\n')
w('These totals cover every craft in section A, including the Cured Light/Medium Hide crafts and the Totemic pieces. Cured hides are broken down into hide + Salt.\n')
cols = [('(1) Path to 125 + 8 Totemic pieces', C['to125']['raw_totals']),
        ('(2) Path to 150 + Helm (Heavy Armor Kits 126-150)', C['to150']['raw_totals']),
        ('(2b) to 150, Medium Leather only', C['to150_mlonly']['raw_totals'])]
ids_sk = [2318, 783, 2319, 4232, 4234]; ids_v = [2320, 2321, 4289, 4340]; ids_n = [249427, 249410]
w('| Material | ' + ' | '.join(c[0] for c in cols) + ' |')
w('|---|' + '---:|' * len(cols))
for title, ids in (('**Skinned**', ids_sk), ('**Vendor**', ids_v), ('**New Forever reagents**', ids_n)):
    w(f'| {title} |' + ' |' * len(cols))
    for i in ids:
        w(f'| {iname(i)} ({i}) | ' + ' | '.join(str(c[1].get(str(i), 0)) for c in cols) + ' |')
w('| *Sulfuric Acid → Pyrite (249391)* | ' + ' | '.join(str(2 * c[1].get('249410', 0)) for c in cols) + ' |')
w('| *Sulfuric Acid → Empty Vial (3371)* | ' + ' | '.join(str(c[1].get('249410', 0)) for c in cols) + ' |')
w('')
ex = {'Armor': [[2318, 16], [4231, 2], [249410, 1]], 'Pants': [[2319, 8], [4231, 4], [249410, 2]], 'Helm': [[2319, 12], [4233, 2], [249410, 3]]}
w("Share of the totals for the three unverified pieces (subtract it if they turn out not to be craftable): Armor = 16 Light Leather, 2 Light Hide, 2 Salt, 1 Acid. "
  "Pants = 8 Medium Leather, 4 Light Hide, 4 Salt, 2 Acid. Helm = 12 Medium Leather, 2 Medium Hide, 2 Salt, 3 Acid. "
  "Skipping Armor and Pants also cuts the Cured Light Hide quota from 15 to 9. The 6 missing skill points then come from about 6 more Light Armor Kits/Embossed Gloves, roughly 15 Light Leather.")
tp = C['totemic_pieces_raw_150']
w(f"\nThe Totemic pieces alone (all nine, hides as hide + Salt): " + ', '.join(f'{v} {k}' for k, v in sorted(tp.items(), key=lambda x: -x[1])) + '.\n')

# ---------------- D ----------------
w('## D. Sulfuric Acid\n')
a = C['acid_recipe']
w(f"Sulfuric Acid (249410) is a new Forever reagent. The only source is the Alchemy recipe {a['spell']}, learned at Alchemy {a['learnedat']} (colours {'/'.join(map(str, a['colors']))}): "
  f"**{reag(a['reagents'])}** per Acid. Pyrite (249391) is a new Forever 'Scarce' reagent that comes only from mining nodes (Questie lists {len(a['pyrite_objectDrops'])} objects: Copper, Tin, Silver and Iron vein ids). "
  f"Empty Vial is a vendor item ({a['vial_vendor_count']} vendors).\n")
w('| Piece | Belt | Gloves | Armor | Boots | Hood | Pants | Tunic | Leggings | Helm |')
w('|---|' + '---:|' * 9)
w('| Acid | ' + ' | '.join(str(C['acid_per_piece'][p]) for p in ['Belt', 'Gloves', 'Armor', 'Boots', 'Hood', 'Pants', 'Tunic', 'Leggings', 'Helm']) + ' |')
w('')
w("- **To 125 (8 pieces): 27 Sulfuric Acid = 54 Pyrite + 27 Empty Vials.**")
w("- **With the Helm: 30 Acid = 60 Pyrite + 30 Vials.**")
w("- Only the six pieces whose patterns are sold (no Armor/Pants/Helm): 24 Acid = 48 Pyrite.")
w("- You have neither Mining nor Alchemy, so buy the Acid (or Pyrite plus an alchemist's time) on the Auction House. The merchant-camp AH is right next to Stitchsong.\n")

# ---------------- E ----------------
w('## E. Pristine Leather (249427), the bottleneck\n')
p = C['pristine']
w(f"**Needed: 25** (Belt 2, Gloves 2, Boots 3, Hood 4, Tunic 6, Leggings 8; Armor, Pants and Helm use none). Brawler's needs the same 25.\n")
w('What the data says:\n')
w('- **Skinned-from** has only 5 rows, all named or rare beasts, with tiny all-time samples and **no Forever samples** (fcount 0): ' + '; '.join(
    f"{r['name']} (lvl {r['min']}) {r['count']}/{r['outof']} = {100*r['count']/r['outof']:.1f}%" + (f", stacks {r['pctstack']}" if r['pctstack'] else '') for r in p['skinned_from']) +
  '. **Daggerfang is on your route** (Loch Modan, chapter 02, with a second try in chapter 16-17): about a 1% chance of 2-3.')
w(f"- **Dropped-by** has {p['dropped_by_n']} beasts with {p['dropped_by_sum_count']} drops in {p['dropped_by_sum_outof']:,} kills ({100*p['dropped_by_sum_count']/p['dropped_by_sum_outof']:.3f}%, about 1 in {p['dropped_by_sum_outof']//p['dropped_by_sum_count']:,}). Forever-only drops: {p['dropped_by_sum_fcount']}. "
  "Those kill counts include pre-Forever kills of the same mobs, so this rate is meaningless. Questie lists " + str(p['qdb_npcDrops_count']) + " beasts as sources. Top rows: " +
  '; '.join(f"{r['name']} {r['count']}/{r['outof']:,}" for r in p['dropped_by_top'][:5]) + '. Stacks are 2-3 (about 2.4 on average).')
w('- **The 12 player comments (Sep-Oct 2026):**')
for c in p['comments']:
    body = re.sub(r'\s+', ' ', c['body'].replace('[b]', '').replace('[/b]', '')).strip()
    if len(body) > 230:
        body = body[:227].rsplit(' ', 1)[0] + ' …'
    w(f"  - {c['date']}: \"{body}\"")
w('')
w("- **The vendor/price comment (11 Oct):** \"Y'all need to keep in mind these items are 5g from the vendor in Riverglade near the BMAH. 5g each.\" "
  "At that price the 25 cost **about 125 g**. That comment is unconfirmed.")
w("- **Rate comments:** the drop works from low skill (\"2 from skinning a boar in Westfall @lvl 13 with 75 skinning\", \"croc at skill 108\"). "
  "The best measured rate is \"roughly 1 in 601 or 0.164%\" (600 Pridewings at Skinning 225). Others report \"getting 2 in 20+ hours of skinning\", \"leveled from 1-200 without a single pristine leather drop\", "
  "and \"5-8 a day just questing until i hit level 25. After 25 I have not seen this drop\". So it may be level-gated or bugged above 25.")
w(f"- **What the route gives:** about 475 beast skins (central estimate, section F) × 0.16% × ~2.4 per drop ≈ **2 Pristine Leather by level 30**. You need 25. "
  "Even at the most optimistic reported rate (5-8 per day while questing below 25), you would be about 2-3 days short. **Plan to buy it (vendor or AH) or farm it deliberately**. "
  "Craft the pieces with the best value per Pristine Leather first: Belt (2), Gloves (2) and Boots (3), all with real slot upgrades. Tunic (6) and Leggings (8) are the expensive ones.\n")

# ---------------- F ----------------
w('## F. Skinning yield along the guide route\n')
w('Method: I grepped the 27 dwarf-route chapter files (01a-26; 00a/00b are the human start) for kill and collect steps on skinnable beasts '
  '(wolves, boars, bears, cats, crocolisks, raptors, buzzards/condors/vultures, wendigos/yetis, turtles, dragonkin whelps, Nightbane worgen). '
  'Explicit "Kill N" counts are used as written. For "collect X" steps, kills = items ÷ an assumed quest-drop rate (~0.6, or ~0.4 for "low drop rate"). '
  'Ormer\'s Revenge (294/295) uses the Classic counts of 10+10. Added on top: 8 BFD and 15 RFK beast trash. '
  'Low = written steps only; **central = +50% for beasts killed in passing** (adds, travel, packs); high = +100%.\n')
w('Per-skin yields by mob level, from the skinned-from tables (all-time samples; Forever-only samples match, e.g. Great Goretusk 72.6% vs 73.1%):\n')
w('| Mob level | Light Leather /skin | Light Hide /skin | Medium Leather /skin | Medium Hide /skin |')
w('|---|---:|---:|---:|---:|')
for b in ['<=10', '11-15', '16-20', '21-25', '26-30', '31+']:
    r = C['skin_rates'][b]
    g = lambda k: (f"{r[k]['per_skin']:.2f}" + (' (assumed)' if r[k].get('assumed') else '') + (f" ({100*r[k]['p']:.0f}% × {r[k]['avgstack']:.2f})" if r[k].get('p') else '')) if k in r else '-'
    w(f"| {b} | {g('2318')} | {g('783')} | {g('2319')} | {g('4232')} |")
w('\n(≤10 is not in the data. 0.85 Light Leather equivalent assumes Ruined Leather Scraps converted 3 → 1 via the Light Leather recipe.)\n')
w('Written beast kills per chapter (before the +50%): ' + ', '.join(f'{ch} {k}' for ch, k in C['route_kills_per_chapter_explicit'] if k) + '. All other chapters have 0.\n')
w('| By end of | Beast skins (low / central / high) | Light Leather | Light Hide | Medium Leather | Medium Hide |')
w('|---|---|---|---|---|---|')
RY = C['route_yields']
for ch, lbl in (('07', 'ch 07 Deadmines (lvl 20)'), ('14', 'ch 14 Duskwood (~26)'), ('26', 'ch 26 RFK (~30)')):
    rows = [RY[f'ch{ch}_inc{i}'] for i in (0, 50, 100)]
    def trip(key):
        return ' / '.join(str(round(r['raw'].get(key, 0))) for r in rows)
    w(f"| {lbl} | {' / '.join(str(r['beast_kills']) for r in rows)} | {trip('2318')} | {trip('783')} | {trip('2319')} | {trip('4232')} |")
w('')
need125 = C['to125']['raw_totals']; need150 = C['to150']['raw_totals']
cen = RY['ch26_inc50']['raw']
w('**Route vs need (central estimate at the end of chapter 26):**\n')
w('| Material | Route (central) | Need, path to 125 | Gap | Need, path to 150 | Gap |')
w('|---|---:|---:|---:|---:|---:|')
for i in ('2318', '783', '2319', '4232', '4234'):
    have = round(cen.get(i, 0)); n1 = need125.get(i, 0); n2 = need150.get(i, 0)
    w(f"| {iname(int(i))} | {have} | {n1} | {have - n1:+d} | {n2} | {have - n2:+d} |")
w('')
w("- **Light Leather:** the path uses all ~258 by skill ~98, which you reach around levels 20-22. The route gives ~190 by level 20 and ~205 by chapter 14, so you are short ~50-70 at the time you need it. It breaks even by level 30.")
w("- **Medium Leather:** short ~95 for the path to 125 (most of it goes on Gray Leather Boots at 98-115 and Dark Leather Cloaks at 115-121). Medium Leather only starts dropping in chapters 17-23, at levels 26-30.")
w("- **Light Hide:** you need 15 (for Cured Light Hide) and the route gives ~5. Short ~10. At 5% per skin of level 11-20 beasts, that is ~200 extra skins, or buy them on the AH.")
w("- **Medium Hide:** you need 9-11 and the route gives ~12, but nearly all of it comes at levels 26-30. The Hood (req 20) and Tunic (req 22) will wait unless you buy hides. Those Cured Medium Hides will also be grey by then, so you lose about 9 cheap skill points.")
w("- **Heavy Leather (125-150):** the route gives none. Expect it from level 30-40 beasts after the guide ends.")
w("- **Verdict:** the route alone does not cover the leather. It roughly covers Light Leather (late) and Medium Hide (late). It is short ~95 Medium Leather, ~10 Light Hide and ~23 Pristine Leather for the path to 125. "
  "Reaching 150 needs ~125 Heavy Leather on top.\n")

# ---------------- G ----------------
w('## G. Later Forever Leatherworking sets\n')
crafted = {c['spell']: c for c in SP['crafted']}
groups = OrderedDict()
PREF = r"^(Cloudy Gustwoven|Cloudy Windraveled|Azure Gustwoven|Azure Windraveled|Charged Scorpid|Supple Scorpid|Heavy Scorpid|Blue Suede|Tooled Leather|Wicked Leather|Grovekeeper|Wildstalker's|Grimstitch|Spiritcaller|Bileblister|Hivethrasher's|Scalegut|Broodwatcher's|Elderwild|[A-Z][a-z]+'s (?=(Leather|Mail)))"
for s in sorted(R['spells'], key=lambda s: s['learnedat']):
    if s['status'] != 'new' or not s.get('creates'):
        continue
    m = re.match(PREF, s['name'])
    if not m:
        continue
    key = m.group(1).strip()
    c = crafted.get(s['id'], {})
    arm = {2: 'Leather', 3: 'Mail'}.get(c.get('subclass'), '?')
    groups.setdefault(key, []).append((s, c, arm))
g2 = OrderedDict()
for k, v in groups.items():
    arms = set(a for s, c, a in v)
    if len(arms) > 1:
        for arm in sorted(arms):
            g2[f'{k} ({arm})'] = [x for x in v if x[2] == arm]
    else:
        g2[k] = v
groups = OrderedDict(sorted(g2.items(), key=lambda kv: min(x[0]['learnedat'] for x in kv[1])))
w('| Set | Armour | Pieces (LW skill) | LW range | Req level |')
w('|---|---|---|---|---|')
for k, v in groups.items():
    pcs = ', '.join(f"{s['name'].replace(k.split(' (')[0] + ' ', '').replace('Leather ', '').replace('Mail ', '')} {s['learnedat']}" for s, c, a in v)
    sk = [s['learnedat'] for s, c, a in v]; rl = [c.get('reqlevel') for s, c, a in v if c.get('reqlevel')]
    arms = '/'.join(sorted(set(a for s, c, a in v)))
    w(f"| {k} | {arms} | {pcs} | {min(sk)}-{max(sk)} | {min(rl) if rl else '?'}-{max(rl) if rl else '?'} |")
w('')
w('Other new Forever items in the table: the boots-only patterns (Black Whelp Slippers, Dark Leather Boots, Murloc Scale Shoes, Moonglow Boots, LW 35, req 10), Hillman\'s Leather Boots (110, req 22), '
  'Light Leather Reagent Bag, Camp Tent and Tanning Rack (camp objects), the level-60 epics (Living Crown, Dawn Armor, Timbermaw Tunic, Warbear Helm, Ironfeather Leggings, Red/Blue/Black Dragonscale, Pristine Scorpid Leggings), '
  'Outlaw\'s Collar, Eternity Pauldrons, Tranquil Wristguards, Mourning Handguards and Wild Leather Armor Kit (all 300). The level-1 "Adaptive" patterns at 285 have no recipe row.\n')
w('**One representative piece of each 150+ set (Forever tooltip):**\n')
w('| Set | Piece | Req | Stats |')
w('|---|---|---:|---|')
REP = [("Skirmisher's (Leather)", 252461), ("Skirmisher's (Leather)", 252528), ("Prowler's (Leather)", 252459), ("Prowler's (Leather)", 252465), ("Warden's (Leather)", 252460),
       ("Skulker's (Leather)", 252520), ("Stalker's (Leather)", 252521), ("Skycaller's (Leather)", 252522), ("Mender's (Leather)", 252523),
       ("Skirmisher's (Mail)", 252564), ("Skirmisher's (Mail)", 252590), ("Stalker's (Mail)", 252588), ("Skycaller's (Mail)", 252589), ("Mender's (Mail)", 252591),
       ('Supple Scorpid', 252599), ('Charged Scorpid', 252598), ('Heavy Scorpid', 252594), ('Blue Suede', 252480), ('Tooled Leather', 252552), ('Wicked Leather', 252479),
       ('Bileblister', 275611), ("Hivethrasher's", 275614), ('Scalegut', 275617), ("Broodwatcher's", 275620), ('Elderwild', 279252),
       ('Cloudy/Azure Gustwoven', 276998), ('Cloudy/Azure Windraveled', 277004)]
for k, i in REP:
    t = TIPS.get(str(i), {})
    rq = re.search(r'Requires Level (\d+)', t.get('tip', ''))
    w(f"| {k} | {t.get('name')} | {rq.group(1) if rq else ''} | {stats(i)} |")
w("| Spiritcaller (Mail, Shaman only) | Spiritcaller Leggings / Pants / Kilt | 60 | Artisan's Tier (LW 300): 'The Spiritcaller's **Rage**' (Leggings, Grips, Spaulders, Treads) has 2pc +1% attack/cast speed, 4pc +36 AP vs Elementals and 5pc −0.5 s Stormstrike cooldown. 'Storm' is the Elemental set (+1% hit, Lava Burst); plain 'Spiritcaller' is Restoration. |")
w('')
w('**Recommendation (Enhancement):**\n')
REC = ("For 30-40 in leather, aim for **Skirmisher's Leather**: Belt at LW 150 / req 30 (+9 Str +6 Sta +4 Int +7 spell power) and Gloves at LW 175 / req 35 (+10 Str +7 Sta +10 spell power). "
       "It is Totemic's Str/Sta/Int/spell-power profile one tier up. Every 150+ leather set has only a belt (req 30) and gloves (req 35) below req 40. Keep the Totemic pieces in the other slots until 40. "
       "From 40, switch to **Skirmisher's Mail** (Boots 40, Shoulders 42, Bracers 45, Sabatons 47, Gauntlets and Belt 50; e.g. Belt +14 Str +10 Sta +15 spell power). Then **Supple Scorpid** (Vest req 54: +15 Str +16 Sta +12 spell power) at 51-56, "
       "and **The Spiritcaller's Rage** at 60, the Shaman-only Artisan's Tier set with a Stormstrike cooldown bonus. Prowler's (Str/Agi/Sta/Int) is the fallback if a Skirmisher's pattern is hard to get. Stalker's, Skycaller's and Mender's are hunter, caster and healer sets.")
w(REC + '\n')
w('**Forceful / Mystic armor kits** (all pattern items, vendor; for chest, legs, hands or feet):\n')
w('| Kit | LW (O/Y/G/Gr) | Req | Reagents | Effect (tooltip) |')
w('|---|---|---:|---|---|')
for nm in ['Forceful Medium Armor Kit', 'Mystic Medium Armor Kit', 'Forceful Heavy Armor Kit', 'Mystic Heavy Armor Kit', 'Forceful Thick Armor Kit', 'Mystic Thick Armor Kit', 'Forceful Rugged Armor Kit', 'Mystic Rugged Armor Kit']:
    s = [x for x in R['spells'] if x['name'] == nm][0]
    c = crafted.get(s['id'], {})
    t = tip(s['creates'][0])
    m = re.search(r'Use: (.*?)(\| Max|$)', t)
    eff = m.group(1).strip() if m else ''
    eff = eff.replace('Permanently increase the ', '').replace(' of an item worn on the chest, legs, hands, or feet.', '').replace(' Only usable on items level 0 and above.', '')
    w(f"| {nm} | {'/'.join(map(str, s['colors']))} | {c.get('reqlevel')} | {', '.join(f'{n} {iname(i)}' for i, n in s['reagents'])} | {eff} |")
w('')
w("The Medium kits are readable: **Forceful = +4 Attack Power** (+16 armour), **Mystic = +2 spell power**. For Enhancement, Forceful is the one to use. "
  "The Heavy, Thick and Rugged tooltips still show unfilled template values (\"Attack Power by 0\", \"Spell Power by 75\"), so their real bonuses cannot be read from the data yet. "
  "Assume they scale the same way (Forceful = AP) and check in game.\n")

# ---------------- Assumptions ----------------
w('## Assumptions and uncertainty\n')
w("- **Skill-up model:** expected values with the Classic formula (grey − skill)/(grey − yellow) from yellow upward, using the integer skill. Real crafting is random; budget about ±10% on filler crafts. "
  "Recipes coloured [0, N, N, N] (Totemic Armor/Pants/Helm) are counted as giving 0 points.")
w("- **Filler choice** depends on my cost weights (Light Leather 1, Medium Leather 2.5, Light Hide 15, Medium Hide 40, Heavy Leather 3 after 125). If Medium Leather turns out easier to get than Light Leather, Gray Leather Boots and Dark Leather Cloak take over earlier. The totals move by tens, not hundreds.")
w("- **Timing:** the path assumes the Cured Medium Hides are made at 75-88 while they are orange. On the route, Medium Hide arrives at levels 26-30, so unless you buy hides, those 9-11 crafts will be grey. You then need ~9 more filler crafts (~36 Medium Leather) to cover the lost points.")
w("- **Unverified pieces:** no Pattern item for Totemic Armor/Pants/Helm exists in the data, and the Helm is a BoP dungeon drop. The totals include them because you asked. Section C shows how to subtract them.")
w("- **Forever drop rates:** most skinned-from rows are all-time samples, but the Forever-only samples that exist agree within ~1 percentage point. Light Leather from level 21-25 beasts rests on only two mobs. Medium Leather stack size is taken as 1 where the data gives none. "
  "Beasts at level ≤10 are not in the data (0.85 Light Leather equivalent per skin is assumed). Pristine Leather has **zero** Forever samples in the data; its rate comes only from player comments, which suggest it may be bugged or level-gated.")
w("- **Route kill counts** are hand estimates: collect steps ÷ ~0.6, Classic counts for Ormer's Revenge, +50% incidental kills for the central case, and dungeon trash added. They exclude Skinning skill gating (assumes Skinning is kept level with the character) and Waylaid Supplies use.")
w("- **Not resolved:** the Merchant's Favor price (30, from the guide, not the data); whether the Riverglade 5g Pristine Leather vendor exists; Pyrite node rates; the real Heavy/Thick/Rugged kit values.")

open(os.path.join(HERE, 'lw_mats_report.md'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')

# ---------------- totals json ----------------
tot = OrderedDict()
for lab in ('to125', 'to150', 'to150_mlonly'):
    rt = C[lab]['raw_totals']
    tot[lab] = OrderedDict(
        description={'to125': 'Skill 1-125 path incl. Totemic Belt/Gloves/Armor/Boots/Hood/Pants/Tunic/Leggings',
                     'to150': 'Skill 1-150 path incl. all 9 Totemic pieces (Helm at 130), Heavy Armor Kits 126-150',
                     'to150_mlonly': 'Same as to150 but 126-150 via Hillman\'s Leather Gloves (Medium Leather only)'}[lab],
        final_skill=round(C[lab]['final_skill'], 2), crafts=C[lab]['n_crafts'],
        skinned={f'{iname(i)} ({i})': rt.get(str(i), 0) for i in ids_sk if rt.get(str(i), 0)},
        vendor={f'{iname(i)} ({i})': rt.get(str(i), 0) for i in ids_v if rt.get(str(i), 0)},
        new_forever={f'{iname(i)} ({i})': rt.get(str(i), 0) for i in ids_n},
        derived={'Pyrite (249391) for the Acid': 2 * rt.get('249410', 0), 'Empty Vial (3371) for the Acid': rt.get('249410', 0)},
        segments=[{'skill': f"{fl(s['start'])}-{fl(s['end'])}", 'crafts': s['crafts'], 'recipe': s['name'], 'role': s['forced'],
                   'colors': s['colors'], 'reagents_per_craft': {nm: n for i, n, nm in s['reagents']}, 'reagents_total': s['total_reagents']}
                  for s in C[lab]['segments']])
out_json = OrderedDict(
    totals=tot,
    pristine_leather={'needed_8_pieces_to125': 25, 'needed_with_helm': 25, 'per_piece': C['pristine_per_piece'],
                      'route_expected_by_lvl30': '~2 (475 skins x 0.164% x ~2.4)'},
    sulfuric_acid={'per_piece': C['acid_per_piece'], 'needed_to125': 27, 'needed_to150_with_helm': 30, 'needed_six_sold_patterns': 24,
                   'recipe': 'Alchemy 40: 2 Pyrite (249391) + 1 Empty Vial (3371)', 'pyrite_to125': 54, 'pyrite_to150': 60},
    route_yields=C['route_yields'], skin_rates=C['skin_rates'],
    totemic_pieces_only_raw_all9=C['totemic_pieces_raw_150'])
json.dump(out_json, open(os.path.join(HERE, 'lw_mats_totals.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
print('ok')
