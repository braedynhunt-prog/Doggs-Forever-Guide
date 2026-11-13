"""Score the scraped Forever item tooltips with the Enhancement weights and compare with the guide's picks."""
import json, re, sys, copy, os, glob
from enh_weights import band_scenarios, weights, kills_per_hour

TOOLTIPS = "item_tooltips.json"   # 24 Sep 2026 scrape, superseded; kept because hunter_score.py imports the name
HERE = os.path.dirname(os.path.abspath(__file__))

def default_tooltips():
    """Newest weights/tooltips/<date>.json (highest-sorting name); item_tooltips.json only if that folder has none."""
    found = sorted(glob.glob(os.path.join(HERE, "tooltips", "*.json")))
    return found[-1] if found else os.path.join(HERE, TOOLTIPS)

# 2 Nov 2026: "Relic" counts as a slot only when "Idol" follows it (druid idols: "RelicIdol" on the Forever tooltip);
# totems and librams keep parsing with no slot, as before.
SLOT_RE = re.compile(r"(Head|Neck|Shoulder|Back|Chest|Wrist|Hands|Waist|Legs|Feet|Finger|Trinket|Main Hand|One-Hand|Two-Hand|Off Hand|Held In Off-hand|Ranged|Shirt|Tabard|Relic(?=Idol))"
                     r"(Cloth|Leather|Mail|Plate|Shield|Axe|Mace|Sword|Dagger|Staff|Polearm|Bow|Gun|Wand|Fist Weapon|Crossbow|Idol)?")
# the lookahead keeps form-only attack power ("+N Attack Power in Cat, Bear, ...") out of "ap"; it goes to feral_ap
STAT_RE = re.compile(r"\+(\d+) (Strength|Agility|Stamina|Intellect|Spirit|Attack Power)(?! in (?:Cat|Bear|Dire Bear|Moonkin))")
# 2 Nov 2026: feral attack power for the feral profile (weights/feral_weights.py), in its own key "feral_ap" so the enh
# and prot scorers never see it. The 1 Nov 2026 Forever tooltip cache has no such item, so both Classic wordings are
# matched: "+N Attack Power in Cat, Bear, and Dire Bear forms only." and "Increases attack power by N in Cat, Bear,
# Dire Bear, and Moonkin forms only." (unverified on Forever).
FERAL_AP_RE = re.compile(r"(?:\+(\d+) Attack Power|Increases attack power by (\d+)) in (?:Cat|Bear|Dire Bear|Moonkin)\b", re.I)
SP_RE = re.compile(r"Increases damage and healing done by magical spells and effects by up to (\d+)")
SP2_RE = re.compile(r"Increases healing done by up to (\d+) and damage done by up to (\d+)")
SPDMG_RE = re.compile(r"Increases damage done by magical spells and effects by up to (\d+)")
EXP_RE = re.compile(r"Increases your expertise by (\d+)")
DPS_RE = re.compile(r"\(([\d.]+) damage per second\)")
REQ_RE = re.compile(r"Requires Level (\d+)")
ILVL_RE = re.compile(r"Item Level (\d+)")
# 1 Nov 2026: tank stats for the prot profile (weights/prot_weights.py). Strings as the Forever tooltips write them
# (weights/tooltips/2026-11-01.json): "184 Armor" base + "+30 Armor" bonus, "Equip: Increased Defense +4.", "13 Block"
# (shield), "+6 Block Value", "Increases your chance to Block attacks with a shield by 1.0%.", "... to Dodge an attack
# by 0.4%.", "Improves your chance to hit by 0.4%." The enh score() and fmt_stats() ignore these keys.
ARMOR_RE = re.compile(r"(?<![+\d.])(\d+) Armor\b")
ARMOR_BONUS_RE = re.compile(r"\+(\d+) Armor\b")
DEF_RE = re.compile(r"(?:Increased Defense|Defense) \+(\d+)|\+(\d+) Defense\b")
BLOCK_RE = re.compile(r"(?<![+\d.])(\d+) Block\b(?! Value)")
BLOCK_BONUS_RE = re.compile(r"\+(\d+) Block Value|block value of your shield by (\d+)", re.I)
BLOCKPCT_RE = re.compile(r"chance to block attacks with a shield by ([\d.]+)%", re.I)
DODGE_RE = re.compile(r"chance to dodge an attack by ([\d.]+)%", re.I)
PARRY_RE = re.compile(r"chance to parry an attack by ([\d.]+)%", re.I)
HIT_RE = re.compile(r"Improves your chance to hit by ([\d.]+)%")
CRIT_RE = re.compile(r"Improves your chance to get a critical strike by ([\d.]+)%")

CRAFTED = {  # Forever Leatherworking sets from the README (level, slot, stats)
    "Totemic Leather Belt (LW, 12)":   dict(slot="Waist", cls="Leather", req=12, str=4, sta=3, sp=4),
    "Totemic Leather Gloves (LW, 15)": dict(slot="Hands", cls="Leather", req=15, str=4, sta=3, sp=5),
    "Totemic Leather Armor (LW, 15)":  dict(slot="Chest", cls="Leather", req=15, str=7, sta=3, int=3, sp=5),
    "Totemic Leather Boots (LW, 17)":  dict(slot="Feet",  cls="Leather", req=17, str=5, sta=4, sp=5),
    "Totemic Leather Pants (LW, 20)":  dict(slot="Legs",  cls="Leather", req=20, str=9, sta=4, int=4, sp=7),
    "Totemic Leather Hood (LW, 20)":   dict(slot="Head",  cls="Leather", req=20, sta=10, sp=8),
    "Brawler's Leather Belt (LW, 12)": dict(slot="Waist", cls="Leather", req=12, str=4, agi=4, sta=3),
    "Brawler's Leather Gloves (LW, 15)": dict(slot="Hands", cls="Leather", req=15, str=4, agi=4, sta=3),
    "Brawler's Leather Armor (LW, 15)": dict(slot="Chest", cls="Leather", req=15, str=5, agi=7, sta=3, spi=3),
    "Brawler's Leather Boots (LW, 17)": dict(slot="Feet", cls="Leather", req=17, str=5, agi=5, sta=4),
    "Brawler's Leather Pants (LW, 20)": dict(slot="Legs", cls="Leather", req=20, str=6, agi=9, sta=4, spi=4),
    "Brawler's Leather Hood (LW, 20)":  dict(slot="Head", cls="Leather", req=20, agi=8, sta=10),
    "Duty Bound Leggings (Ruins of Lordaeron)": dict(slot="Legs", cls="Leather", req=15, agi=6, sta=9, ap=12),
    "Grave Shroud (Ruins of Lordaeron)": dict(slot="Back", cls=None, req=15, str=3, agi=2, sta=5),
}

def parse(name, rec):
    tt = rec["tooltip"]
    # drop set-bonus text ("Defias Leather (0/5) ... (3) Set : +15 Attack Power against Humanoids")
    for marker in (" (0/5)", "(2) Set"):
        if marker in tt:
            tt = tt[:tt.index(marker)]
    it = dict(name=name, id=rec.get("id"), quest=rec.get("quest"), str=0, agi=0, sta=0, int=0, spi=0, ap=0, sp=0, exp=0, wdps=0.0,
              slot=None, cls=None, req=0, ilvl=0)
    m = SLOT_RE.search(tt.split("|")[2] if tt.count("|") >= 2 else tt)
    if not m:
        m = SLOT_RE.search(tt)
    if m:
        it["slot"], it["cls"] = m.group(1), m.group(2)
    for v, s in STAT_RE.findall(tt):
        key = {"Strength": "str", "Agility": "agi", "Stamina": "sta", "Intellect": "int", "Spirit": "spi", "Attack Power": "ap"}[s]
        it[key] += int(v)
    m = SP_RE.search(tt);    it["sp"] = int(m.group(1)) if m else it["sp"]
    m = SP2_RE.search(tt);   it["sp"] = int(m.group(2)) if m else it["sp"]
    m = SPDMG_RE.search(tt); it["sp"] = int(m.group(1)) if m else it["sp"]
    m = EXP_RE.search(tt);   it["exp"] = int(m.group(1)) if m else 0
    m = DPS_RE.search(tt);   it["wdps"] = float(m.group(1)) if m else 0.0
    m = REQ_RE.search(tt);   it["req"] = int(m.group(1)) if m else 0
    m = ILVL_RE.search(tt);  it["ilvl"] = int(m.group(1)) if m else 0
    # tank stats (1 Nov 2026) - extra keys only, so the enh output is unchanged
    it["armor"] = sum(int(v) for v in ARMOR_RE.findall(tt)) + sum(int(v) for v in ARMOR_BONUS_RE.findall(tt))
    it["defense"] = sum(int(a or b) for a, b in DEF_RE.findall(tt))
    it["block"] = sum(int(v) for v in BLOCK_RE.findall(tt)) + sum(int(a or b) for a, b in BLOCK_BONUS_RE.findall(tt))
    it["blockpct"] = sum(float(v) for v in BLOCKPCT_RE.findall(tt))
    it["dodge"] = sum(float(v) for v in DODGE_RE.findall(tt))
    it["parry"] = sum(float(v) for v in PARRY_RE.findall(tt))
    it["hit"] = sum(float(v) for v in HIT_RE.findall(tt))
    it["crit"] = sum(float(v) for v in CRIT_RE.findall(tt))
    it["feral_ap"] = sum(int(a or b) for a, b in FERAL_AP_RE.findall(tt))
    head = tt.split("|")[2] if tt.count("|") >= 2 else tt
    it["thrown"] = it["slot"] is None and "Thrown" in head
    return it

def usable(it, level=None):
    """Returns (usable_now, note) for a 2H Enhancement shaman. Mail counts from level 40 (11 Nov 2026: level = the
    chapter's weights band; None = below 40, as every caller before the 40 band)."""
    slot, cls = it["slot"], it["cls"]
    if slot is None or slot == "Relic":   # Relic (druid idol, 2 Nov 2026) parsed as no slot before
        return False, "not equipment"
    if slot in ("Shirt", "Tabard", "Trinket"):
        return False, "cosmetic"
    if cls == "Plate":                     # 11 Nov 2026: Pauldron of Order was scored as wearable (no plate rule before)
        return False, "plate (shaman can't wear)"
    if cls == "Mail" and (level is None or level < 40):
        return False, "mail (40+)"
    if cls in ("Sword", "Polearm", "Bow", "Gun", "Crossbow", "Wand"):
        return False, f"{cls.lower()} (shaman can't use)"
    if slot in ("Off Hand", "Held In Off-hand", "Ranged"):
        return False, "off-hand/ranged (2H build)"
    if slot in ("Main Hand", "One-Hand"):
        return True, "1H (shield set only)"
    return True, ""

def score(it, w):
    s = (w["str"] * it["str"] + w["agi"] * it["agi"] + w["sta"] * it["sta"] + w["int"] * it["int"] + w["spi"] * it["spi"]
         + w["ap"] * it["ap"] + w["sp"] * it["sp"] + w["exp"] * it["exp"])
    if it["slot"] in ("Two-Hand", "Main Hand", "One-Hand"):
        s += w["wdps"] * it["wdps"]
    # no mace term since 1 Nov 2026: Dwarf Mace Specialization was removed from Forever on 17 Oct (Earth Fury)
    return s

def fmt_stats(it):
    parts = []
    if it["wdps"]: parts.append(f"{it['wdps']:.1f} dps")
    for k, lab in (("str", "Str"), ("agi", "Agi"), ("sta", "Sta"), ("int", "Int"), ("spi", "Spi"), ("ap", "AP"), ("sp", "SP"), ("exp", "Exp")):
        if it[k]: parts.append(f"+{it[k]} {lab}")
    return " ".join(parts) or "no stats"

def main():
    path = default_tooltips()
    if "--tooltips" in sys.argv:
        i = sys.argv.index("--tooltips")
        if i + 1 >= len(sys.argv):
            sys.exit("--tooltips needs a file path")
        path = sys.argv[i + 1]
    data = json.load(open(path, encoding="utf-8"))
    # 3 Nov 2026: the tooltips/<date>.json caches carry no "quest" field; take the quest links by item name from the
    # 24 Sep scrape so the per-quest ranking survives (an entry in the newer cache keeps its own quest field if it has one).
    merged = 0
    old_path = os.path.join(HERE, TOOLTIPS)
    if os.path.abspath(path) != os.path.abspath(old_path) and os.path.exists(old_path):
        for n, rec in json.load(open(old_path, encoding="utf-8")).items():
            if rec.get("quest") and n in data and not data[n].get("quest"):
                data[n]["quest"] = rec["quest"]
                merged += 1
    shown = os.path.relpath(path, HERE).replace(os.sep, "/")
    print(f"TOOLTIPS: {shown} ({len(data)} items; quest links for {merged} items taken from {TOOLTIPS})")
    items = [parse(n, r) for n, r in data.items()]
    for n, d in CRAFTED.items():
        it = dict(name=n, id=None, quest=None, str=0, agi=0, sta=0, int=0, spi=0, ap=0, sp=0, exp=0, wdps=0.0, slot=d["slot"], cls=d["cls"], req=d["req"], ilvl=0)
        it.update({k: v for k, v in d.items() if k in it})
        items.append(it)

    # Central weights (level-20 band) and a conservative set with Spirit/SP/Expertise at the low end of their ranges.
    # 3 Nov 2026: Int 1.05 -> 1.55 (Mental Dexterity 50/100/150% of Int, was 33/67/100%; source: Blizzard dev notes 3 Nov)
    # 8 Nov 2026: Spi 1.0 -> 2.5, SP 1.5 -> 2.0, Int 1.55 -> 1.65, Agi 0.85 -> 0.8 (sheet readings; see profiles.py / docs/audit-2026-11-08.md)
    # 13 Nov 2026: Int 1.65 -> 1.15 (Mental Dexterity 33/66/100% again, 12 Nov hotfix; docs/audit-2026-11-13.md)
    w_eff = dict(wdps=14.0, str=2.0, ap=1.0, int=1.15, agi=0.8, spi=2.5, sta=0.0, sp=2.0, exp=3.0)
    w_spam = dict(wdps=14.0, str=2.0, ap=1.0, int=1.15, agi=0.8, spi=1.5, sta=0.0, sp=1.0, exp=1.0)
    # 11 Nov 2026: --band N scores with that band's sets from profiles.enh_band_weights() (Int/Agi from the model) and
    # that level's rules (Mail from 40, req <= N in the slot table). No flag = the level-20 output as before.
    band = 20
    if "--band" in sys.argv:
        i = sys.argv.index("--band")
        if i + 1 >= len(sys.argv):
            sys.exit("--band needs a level band (10/15/20/25/30/40)")
        band = int(sys.argv[i + 1])
    if band != 20:
        from profiles import enh_band_weights
        bw = enh_band_weights()
        if band not in bw:
            sys.exit("unknown band %d (known: %s)" % (band, ", ".join(map(str, sorted(bw)))))
        w_eff, w_spam = bw[band]
    wsets = {"central": w_eff, "conservative": w_spam}

    print(f"WEIGHTS (level {band}, AP = 1; mace term dropped 1 Nov 2026):")
    for nm, w in wsets.items():
        print(f"  {nm:12s} " + "  ".join(f"{k}={w[k]:.2f}" for k in ["wdps", "str", "ap", "int", "agi", "spi", "sta", "sp", "exp"]))

    # ---- per-quest comparison
    guide = {  # quest id -> guide's pick (None = nothing usable / vendor)
        179: "Wolf Handler Gloves", 170: "Bear Shawl", 183: "Dwarven Leather Pants", 182: "Anvilmar Sledge",
        218: "Dwarven Kite Shield", 312: "Wooly Mittens", 315: "Goat Fur Cloak", 287: "Stone Buckler", 412: "Driving Gloves",
        320: "Gnarled Short Staff", 314: "Coldridge Hammer", 417: None, 416: "Burnt Hide Bracers", 307: "Robe of the Keeper",
        2038: "Bingles' Flying Gloves", 257: None, 258: "Fine Cloth Shirt", 385: None, 309: None, 297: None, 217: None,
        89: "Smith's Trousers (only if no Deepgrave)", 9: "Harvester's Pants (only if still in Dwarven Leather Pants)",
        153: "Cloak of the People's Militia (only if no Spiritwraith)", 102: None, 104: None, 14: None, 167: "Tunic of Westfall (if no Defias Armor)",
        168: "Dusty Mining Gloves (if no Flamefist/Gold-flecked)", 214: None, 2040: "Bravo's Armbands", 256: "Loch Walkers",
        126: "Ring of Iron Will", 219: "Bone-studded Leather", 19: "Orc Crusher (side-grade)", 283: None, 122: None, 466: None,
        176: None, 46: None, 982: None, 95999: None, 116: None, 151: "Old Blanchy's Feed Pouch", 531: "Hunting Satchel",
    }
    byq = {}
    for it in items:
        if it["quest"]: byq.setdefault(it["quest"], []).append(it)

    print(f"\nPER-QUEST REWARD RANKING (score = AP-equivalent; level-{band} weights, central | conservative)")
    for q in sorted(byq):
        rows = byq[q]
        if not any(usable(r, band)[0] for r in rows):
            continue
        print(f"\nquest {q}  (guide: {guide.get(q, '?')})")
        ranked = sorted(rows, key=lambda r: -score(r, w_eff))
        for r in ranked:
            u, note = usable(r, band)
            se, ss = score(r, w_eff), score(r, w_spam)
            flag = "" if u else f"  [{note}]"
            print(f"   {se:6.1f} | {ss:6.1f}   {r['name']:34s} {str(r['slot']):12s} {str(r['cls'] or ''):8s} {fmt_stats(r)}{flag}")

    # ---- slot-by-slot best usable at level <= 20 from the whole pool
    print(f"\nSLOT BY SLOT, everything usable with req <= {band} (central weights; conservative in brackets)")
    slots = ["Two-Hand", "Head", "Neck", "Shoulder", "Back", "Chest", "Wrist", "Hands", "Waist", "Legs", "Feet", "Finger"]
    for sl in slots:
        rows = [r for r in items if r["slot"] == sl and usable(r, band)[0] and r["req"] <= band and score(r, w_eff) > 0]
        rows.sort(key=lambda r: -score(r, w_eff))
        print(f"\n{sl}:")
        for r in rows[:8]:
            src = f"q{r['quest']}" if r["quest"] else ("craft/RoL" if r["id"] is None else "drop")
            print(f"   {score(r, w_eff):6.1f} [{score(r, w_spam):6.1f}]  {r['name']:38s} {str(r['cls'] or ''):8s} {fmt_stats(r):40s} {src}  req{r['req']}")

if __name__ == "__main__":
    main()
