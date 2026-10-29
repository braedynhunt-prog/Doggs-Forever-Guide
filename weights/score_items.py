"""Score the scraped Forever item tooltips with the Enhancement weights and compare with the guide's picks."""
import json, re, sys, copy
from enh_weights import band_scenarios, weights, kills_per_hour

TOOLTIPS = "item_tooltips.json"

SLOT_RE = re.compile(r"(Head|Neck|Shoulder|Back|Chest|Wrist|Hands|Waist|Legs|Feet|Finger|Trinket|Main Hand|One-Hand|Two-Hand|Off Hand|Held In Off-hand|Ranged|Shirt|Tabard)"
                     r"(Cloth|Leather|Mail|Plate|Shield|Axe|Mace|Sword|Dagger|Staff|Polearm|Bow|Gun|Wand|Fist Weapon|Crossbow)?")
STAT_RE = re.compile(r"\+(\d+) (Strength|Agility|Stamina|Intellect|Spirit|Attack Power)")
SP_RE = re.compile(r"Increases damage and healing done by magical spells and effects by up to (\d+)")
SP2_RE = re.compile(r"Increases healing done by up to (\d+) and damage done by up to (\d+)")
SPDMG_RE = re.compile(r"Increases damage done by magical spells and effects by up to (\d+)")
EXP_RE = re.compile(r"Increases your expertise by (\d+)")
DPS_RE = re.compile(r"\(([\d.]+) damage per second\)")
REQ_RE = re.compile(r"Requires Level (\d+)")
ILVL_RE = re.compile(r"Item Level (\d+)")

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
    return it

def usable(it):
    """Returns (usable_now, note) for a 2H Enhancement shaman below 40."""
    slot, cls = it["slot"], it["cls"]
    if slot is None:
        return False, "not equipment"
    if slot in ("Shirt", "Tabard", "Trinket"):
        return False, "cosmetic"
    if cls == "Mail":
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
    if it["slot"] in ("Two-Hand",):
        s += w["wdps"] * it["wdps"]
        if it["cls"] == "Mace":
            s += w["mace_bonus"]
    elif it["slot"] in ("Main Hand", "One-Hand"):
        s += w["wdps"] * it["wdps"]
        if it["cls"] == "Mace":
            s += w["mace_bonus"]
    return s

def fmt_stats(it):
    parts = []
    if it["wdps"]: parts.append(f"{it['wdps']:.1f} dps")
    for k, lab in (("str", "Str"), ("agi", "Agi"), ("sta", "Sta"), ("int", "Int"), ("spi", "Spi"), ("ap", "AP"), ("sp", "SP"), ("exp", "Exp")):
        if it[k]: parts.append(f"+{it[k]} {lab}")
    return " ".join(parts) or "no stats"

def main():
    data = json.load(open(TOOLTIPS))
    items = [parse(n, r) for n, r in data.items()]
    for n, d in CRAFTED.items():
        it = dict(name=n, id=None, quest=None, str=0, agi=0, sta=0, int=0, spi=0, ap=0, sp=0, exp=0, wdps=0.0, slot=d["slot"], cls=d["cls"], req=d["req"], ilvl=0)
        it.update({k: v for k, v in d.items() if k in it})
        items.append(it)

    # Central weights (level-20 band) and a conservative set with Spirit/SP/Expertise at the low end of their ranges.
    w_eff = dict(wdps=14.0, str=2.0, ap=1.0, int=1.05, agi=0.85, spi=1.0, sta=0.0, sp=1.5, exp=3.0, mace_bonus=7.0)
    w_spam = dict(wdps=14.0, str=2.0, ap=1.0, int=1.05, agi=0.85, spi=0.5, sta=0.0, sp=0.5, exp=1.0, mace_bonus=7.0)
    wsets = {"central": w_eff, "conservative": w_spam}

    print("WEIGHTS (level 20, AP = 1):")
    for nm, w in wsets.items():
        print(f"  {nm:12s} " + "  ".join(f"{k}={w[k]:.2f}" for k in ["wdps", "str", "ap", "int", "agi", "spi", "sta", "sp", "exp", "mace_bonus"]))

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

    print("\nPER-QUEST REWARD RANKING (score = AP-equivalent; level-20 weights, central | conservative)")
    for q in sorted(byq):
        rows = byq[q]
        if not any(usable(r)[0] for r in rows):
            continue
        print(f"\nquest {q}  (guide: {guide.get(q, '?')})")
        ranked = sorted(rows, key=lambda r: -score(r, w_eff))
        for r in ranked:
            u, note = usable(r)
            se, ss = score(r, w_eff), score(r, w_spam)
            flag = "" if u else f"  [{note}]"
            print(f"   {se:6.1f} | {ss:6.1f}   {r['name']:34s} {str(r['slot']):12s} {str(r['cls'] or ''):8s} {fmt_stats(r)}{flag}")

    # ---- slot-by-slot best usable at level <= 20 from the whole pool
    print("\nSLOT BY SLOT, everything usable with req <= 20 (central weights; conservative in brackets)")
    slots = ["Two-Hand", "Head", "Neck", "Shoulder", "Back", "Chest", "Wrist", "Hands", "Waist", "Legs", "Feet", "Finger"]
    for sl in slots:
        rows = [r for r in items if r["slot"] == sl and usable(r)[0] and r["req"] <= 20 and score(r, w_eff) > 0]
        rows.sort(key=lambda r: -score(r, w_eff))
        print(f"\n{sl}:")
        for r in rows[:8]:
            src = f"q{r['quest']}" if r["quest"] else ("craft/RoL" if r["id"] is None else "drop")
            print(f"   {score(r, w_eff):6.1f} [{score(r, w_spam):6.1f}]  {r['name']:38s} {str(r['cls'] or ''):8s} {fmt_stats(r):40s} {src}  req{r['req']}")

if __name__ == "__main__":
    main()
