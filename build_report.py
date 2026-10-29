#!/usr/bin/env python3
"""Build the 'Forever Alliance Quest Atlas' page from data/*.json (static HTML fragment for the Artifact tool)."""
import json, os, re, html, datetime
from collections import defaultdict, Counter

DATA = "data"
Q = {int(k): v for k, v in json.load(open(f"{DATA}/quests.json", encoding="utf-8")).items()}
E = json.load(open(f"{DATA}/entities.json", encoding="utf-8")) if os.path.exists(f"{DATA}/entities.json") else {}
ZONEROWS = {int(r["id"]): r for r in json.load(open("zones.json", encoding="utf-8"))}
ASSIGNED = set()
OWNER = {}

# Alliance route order (dwarf-first since he leans Dwarf Shaman), then shared, then dungeons
ORDER = [
    ("Starting zones (1-12)", [1, 12, 141, 16593]),
    ("Capitals", [1537, 1519, 1657]),
    ("10-20", [38, 40, 148, 44]),
    ("20-30", [10, 11, 331, 406, 267]),
    ("28-35 spill-over", [36, 45, 400, 33]),
    ("Dungeons", [16919, 16611, 1581, 717, 721, 718, 719, 209, 491, 796]),
]
ZONE_NOTE = {
    1: "Dwarf/Gnome start. Anvilmar → Kharanos → Amberstill/Gol'Bolar → Hall of Thanes chain at ~13-16.",
    12: "Human start. Northshire → Goldshire → Eastvale.",
    141: "Night Elf start. Shadowglen → Dolanaar.",
    16593: "Skyborne start (new race). Everything here is new; only the High Order (Alliance) Skyborne can start here.",
    16919: "New dungeon under Old Ironforge, finder level 13 (13-18). Chain starts in Dun Morogh (Earthseer Farsen).",
    16611: "New dungeon in the Lordaeron ruins above Undercity, finder level 15 (15-20). Alliance quests come from the Sepulcher side / Silverpine.",
}
CLASSES = {1: "Warrior", 2: "Paladin", 4: "Hunter", 8: "Rogue", 16: "Priest", 64: "Shaman", 128: "Mage", 256: "Warlock", 1024: "Druid"}
SLOT = {1: "Head", 2: "Neck", 3: "Shoulder", 4: "Shirt", 5: "Chest", 6: "Waist", 7: "Legs", 8: "Feet", 9: "Wrist", 10: "Hands", 11: "Ring", 12: "Trinket",
        13: "1H", 14: "Shield", 15: "Ranged", 16: "Back", 17: "2H", 18: "Bag", 19: "Tabard", 20: "Chest", 21: "Main hand", 22: "Off hand", 23: "Held", 24: "Ammo", 25: "Thrown", 26: "Ranged", 28: "Relic"}
QUAL = {0: "poor", 1: "common", 2: "uncommon", 3: "rare", 4: "epic"}

def esc(s): return html.escape(str(s) if s is not None else "")

def side_of(q):
    s = q["list"].get("side")
    if s is None: s = (q.get("g") or {}).get("side")
    return s  # 1 A, 2 H, 3 both, None unknown

def classes_of(q):
    m = q["list"].get("reqclass") or q["list"].get("classs") or (q.get("g") or {}).get("reqclass") or 0
    return [n for b, n in CLASSES.items() if m & b]

def coords_for(kind, eid, zone_id):
    e = E.get(f"{kind}:{eid}") or {}
    mp = e.get("mapper") or {}
    if isinstance(mp, list): mp = {}
    best = None
    for z, arr in mp.items():
        for a in arr:
            if not a.get("coords"): continue
            c = a["coords"][0]
            item = (a.get("uiMapName") or ZONEROWS.get(int(z), {}).get("name") or z, c[0], c[1], int(z) if str(z).lstrip("-").isdigit() else 0)
            if int(z) == zone_id and best is None: best = item
            elif best is None or (int(z) == zone_id): best = item if best is None or int(z) == zone_id else best
    return best  # (zone name, x, y, zone id)

def ent_html(ents, zone_id):
    parts = []
    for e in ents:
        c = coords_for(e["kind"], e["id"], zone_id)
        name = esc(e["name"])
        url = f"https://www.wowhead.com/forever/{e['kind']}={e['id']}"
        if c:
            same = c[3] == zone_id
            loc = f'<span class="coord">{c[1]:g},{c[2]:g}</span>' + ("" if same else f' <span class="zone-tag">{esc(c[0])}</span>')
        else:
            loc = '<span class="coord unknown">no coords yet</span>'
        kind = "" if e["kind"] == "npc" else f' <span class="kind">{e["kind"]}</span>'
        parts.append(f'<a href="{url}" target="_blank" rel="noopener">{name}</a>{kind} {loc}')
    return "<br>".join(parts) if parts else '<span class="muted">item / unknown</span>'

def rewards_html(q):
    g = q.get("g") or {}
    items = q.get("items") or {}
    ids = [i[0] for i in g.get("itemchoices", [])] + [i[0] for i in g.get("itemrewards", [])]
    choice = set(i[0] for i in g.get("itemchoices", []))
    out = []
    for iid in ids:
        it = items.get(str(iid)) or items.get(iid) or {}
        if not it: continue
        eq = it.get("equip") or {}
        bits = []
        slot = SLOT.get(eq.get("slotbak"))
        if slot: bits.append(slot)
        if eq.get("dps"): bits.append(f"{eq['dps']:.1f} dps" + (f" · {eq.get('speed'):.2f}" if eq.get("speed") else ""))
        if eq.get("armor"): bits.append(f"{eq['armor']} armor")
        stats = [f"+{eq[k]} {k}" for k in ("agi", "str", "sta", "int", "spi") if eq.get(k)]
        bits += stats
        for k, lab in (("mleatk", "AP"), ("splpwr", "SP"), ("mlecritstrkrtng", "crit"), ("hitrtng", "hit")):
            if eq.get(k): bits.append(f"+{eq[k]} {lab}")
        q_ = QUAL.get(it.get("quality"), "")
        tag = "choice" if iid in choice else "reward"
        bits_html = (' <span class="muted">(' + esc(", ".join(bits)) + ')</span>') if bits else ""
        out.append(f'<div class="rew q-{q_}"><a href="https://www.wowhead.com/forever/item={iid}" target="_blank" rel="noopener">{esc(it.get("name"))}</a>'
                   f'{bits_html}<span class="rtag">{tag}</span></div>')
    coins = q.get("coin_levels") or {}
    money = None
    if coins:
        v = list(coins.values())[0]
        if v: money = v
    if money:
        g_, s_, c_ = money // 10000, (money // 100) % 100, money % 100
        out.append(f'<div class="rew money">{(str(g_)+"g ") if g_ else ""}{(str(s_)+"s ") if s_ else ""}{(str(c_)+"c") if c_ and not g_ else ""}</div>')
    rep = g.get("reprewards") or q["list"].get("reprewards") or []
    if rep:
        vals = sorted(set(r[1] for r in rep))
        out.append('<div class="rew muted">' + ", ".join(f"+{v} rep" for v in vals) + (f" ({len(rep)} factions)" if len(rep) > 1 else "") + "</div>")
    return "".join(out) or '<span class="muted">—</span>'

def series_html(q):
    s = q.get("series") or []
    if not s: return ""
    n = next((x["n"] for x in s if x.get("current") or x["id"] == q["id"]), None)
    names = " → ".join(("<b>" if x["id"] == q["id"] else "") + esc(x["name"]) + ("</b>" if x["id"] == q["id"] else "") for x in s)
    return f'<span class="chain" title="{names}">chain {n}/{len(s)}</span>'

def notes_html(q):
    bits = []
    ot = (q.get("objective_text") or "").strip()
    if ot: bits.append(f'<div class="obj">{esc(ot)}</div>')
    objs = [o for o in q.get("objectives") or [] if o.get("text")]
    if objs:
        bits.append('<div class="objs">' + " · ".join(f'{esc(o["text"])}' + (f' ×{o["qty"]}' if o["qty"] > 1 else "") for o in objs) + "</div>")
    ch = (q.get("g") or {}).get("envChange") or {}
    if ch.get("lines"):
        bits.append('<div class="chg">' + "<br>".join(esc(l) for l in ch["lines"][:4]) + "</div>")
    cm = q.get("comments") or []
    if cm:
        c = cm[0]
        if len(c) > 220: c = c[:217] + "…"
        bits.append(f'<div class="cmt">“{esc(c)}”</div>')
    return "".join(bits)

def quest_row(q, zone_id):
    info = q.get("info") or {}
    l = q["list"]; g = q.get("g") or {}
    lvl = l.get("level") or g.get("level"); req = l.get("reqlevel") or g.get("reqlevel")
    xp = l.get("xp") if l.get("xp") is not None else g.get("xp")
    side = side_of(q); cls = classes_of(q)
    st = l.get("envChange", {}).get("status")
    typ = info.get("type") or ""
    badges = []
    if st == "new": badges.append('<span class="b new">new</span>')
    elif st == "updated": badges.append('<span class="b upd">updated</span>')
    if typ: badges.append(f'<span class="b typ">{esc(typ)}</span>')
    if cls: badges.append(f'<span class="b cls">{esc("/".join(cls))}</span>')
    if side == 2: badges.append('<span class="b horde">Horde</span>')
    elif side == 3: badges.append('<span class="b both">both</span>')
    ser = series_html(q)
    data_cls = ",".join(cls) if cls else "none"
    return (f'<tr class="qrow" data-status="{st}" data-side="{side or 0}" data-class="{esc(data_cls)}" data-name="{esc((q.get("name") or l.get("name") or "").lower())}">'
            f'<td class="num"><span class="lvl">{lvl if lvl is not None else "?"}</span><span class="req">req {req if req is not None else "?"}</span></td>'
            f'<td class="qname"><a href="https://www.wowhead.com/forever/quest={q["id"]}" target="_blank" rel="noopener">{esc(q.get("name") or l.get("name"))}</a> {ser}<div class="badges">{"".join(badges)}</div></td>'
            f'<td class="num xp">{xp if xp else "—"}</td>'
            f'<td class="ent">{ent_html(info.get("start", []), zone_id)}</td>'
            f'<td class="ent">{ent_html(info.get("end", []), zone_id)}</td>'
            f'<td class="rews">{rewards_html(q)}</td>'
            f'<td class="notes">{notes_html(q)}</td></tr>')

def hubs_for(zone_id, quests):
    """Cluster new-quest givers by proximity inside this zone."""
    pts = []
    for q in quests:
        if q["list"].get("envChange", {}).get("status") != "new": continue
        for e in (q.get("info") or {}).get("start", []):
            c = coords_for(e["kind"], e["id"], zone_id)
            if c and c[3] == zone_id: pts.append((c[1], c[2], e["name"], q))
    clusters = []
    for x, y, name, q in pts:
        for cl in clusters:
            if abs(cl["x"] - x) <= 3 and abs(cl["y"] - y) <= 3:
                cl["names"].add(name); cl["quests"].add(q["id"]); cl["xp"] += (q["list"].get("xp") or 0); break
        else:
            clusters.append({"x": x, "y": y, "names": {name}, "quests": {q["id"]}, "xp": q["list"].get("xp") or 0})
    clusters.sort(key=lambda c: -len(c["quests"]))
    return clusters

def zone_section(zone_id):
    zr = ZONEROWS.get(zone_id, {"name": f"zone {zone_id}"})
    zf = f"{DATA}/zone_{zone_id}.json"
    if not os.path.exists(zf): return ""
    z = json.load(open(zf, encoding="utf-8"))
    rows = [r for r in z["quests"] if r.get("envChange", {}).get("status") in ("new", "updated")]
    quests = [Q[r["id"]] for r in rows if r["id"] in Q]
    uniq = []
    for q in quests:
        if OWNER.get(q["id"]) != zone_id or q["id"] in ASSIGNED: continue
        ASSIGNED.add(q["id"]); uniq.append(q)
    def sort_key(q):
        ser = q.get("series") or []
        first = ser[0]["id"] if ser else q["id"]
        n = next((x["n"] for x in ser if x["id"] == q["id"]), 0)
        lvl = min([(q["list"].get("level") or 0)] + [Q[x["id"]]["list"].get("level") or 0 for x in ser if x["id"] in Q]) if ser else (q["list"].get("level") or 0)
        return (lvl, first, n, q["id"])
    quests = sorted(uniq, key=sort_key)
    def alliance_ok(q): return side_of(q) in (1, 3, None)
    new_a = [q for q in quests if q["list"]["envChange"]["status"] == "new" and alliance_ok(q)]
    upd_a = [q for q in quests if q["list"]["envChange"]["status"] == "updated" and alliance_ok(q)]
    new_h = [q for q in quests if q["list"]["envChange"]["status"] == "new" and not alliance_ok(q)]
    xp_new = sum((q["list"].get("xp") or 0) for q in new_a if not classes_of(q))
    xp_cls = sum((q["list"].get("xp") or 0) for q in new_a if classes_of(q))
    total_q = len(z["quests"])
    new_npcs = sum(1 for n in z["npcs"] if n.get("envChange", {}).get("status") == "new")
    lv = f'{zr.get("minlevel")}-{zr.get("maxlevel")}' if zr.get("maxlevel") else ""
    hubs = hubs_for(zone_id, new_a)
    hub_html = ""
    if hubs:
        items = []
        for c in hubs[:6]:
            items.append(f'<li><span class="coord">{c["x"]:g},{c["y"]:g}</span> {len(c["quests"])} quest{"s" if len(c["quests"])!=1 else ""}, {c["xp"]:,} XP · {esc(", ".join(sorted(c["names"])[:4]))}{"…" if len(c["names"])>4 else ""}</li>')
        hub_html = f'<div class="hubs"><span class="hubs-label">New quest givers cluster at</span><ul>{"".join(items)}</ul></div>'
    note = ZONE_NOTE.get(zone_id, "")
    note_html = f'<p class="znote">{esc(note)}</p>' if note else ""
    stat = (f'<div class="zstats"><span><b>{len(new_a)}</b> new Alliance-usable quests</span><span><b>{xp_new:,}</b> XP from them'
            f'{f" (+{xp_cls:,} class-only)" if xp_cls else ""}</span><span><b>{len(upd_a)}</b> updated</span>'
            f'<span><b>{new_npcs}</b> new NPCs</span><span class="muted">{total_q} quests listed in total</span></div>')
    body = ""
    if new_a or new_h or upd_a:
        body = ('<div class="tablewrap"><table><thead><tr><th>Lvl</th><th>Quest</th><th>XP</th><th>Start</th><th>End</th><th>Rewards</th><th>Objectives / notes</th></tr></thead><tbody>'
                + "".join(quest_row(q, zone_id) for q in new_a + upd_a + new_h) + "</tbody></table></div>")
    else:
        body = '<p class="muted empty">Nothing new or changed recorded here yet. Either Forever left it alone or nobody with the Wowhead client has been through it (the beta cap is 20).</p>'
    return (f'<section class="zone" id="z{zone_id}"><div class="zhead"><h2>{esc(zr["name"])}</h2><span class="zlvl">{lv}</span>'
            f'<span class="b zstatus {esc(zr.get("envChange",{}).get("status",""))}">{esc(zr.get("envChange",{}).get("status",""))}</span></div>'
            f'{note_html}{stat}{hub_html}{body}</section>')

def build():
    now = datetime.date.today().strftime("%d %b %Y")
    # totals
    all_zone_ids = [z for _, zs in ORDER for z in zs]
    tot_new = tot_upd = tot_xp = 0; seen = set()
    for zid in all_zone_ids:
        zf = f"{DATA}/zone_{zid}.json"
        if not os.path.exists(zf): continue
        for r in json.load(open(zf, encoding="utf-8"))["quests"]:
            if r["id"] in seen or r["id"] not in Q: continue
            seen.add(r["id"]); q = Q[r["id"]]
            if side_of(q) not in (1, 3, None): continue
            st = r.get("envChange", {}).get("status")
            if st == "new": tot_new += 1; tot_xp += (r.get("xp") or 0) if not classes_of(q) else 0
            elif st == "updated": tot_upd += 1
    nav = "".join(f'<a href="#z{z}">{esc(ZONEROWS.get(z,{}).get("name",z))}</a>' for _, zs in ORDER for z in zs if os.path.exists(f"{DATA}/zone_{z}.json"))
    # assignment pass: dungeons claim their quests first so a dungeon section lists all of its quests
    ASSIGNED.clear(); OWNER.clear()
    assign_order = [z for band, zs in ORDER if band == "Dungeons" for z in zs] + [z for band, zs in ORDER if band != "Dungeons" for z in zs]
    for zid in assign_order:
        zf = f"{DATA}/zone_{zid}.json"
        if not os.path.exists(zf): continue
        for r in json.load(open(zf, encoding="utf-8"))["quests"]:
            if r.get("envChange", {}).get("status") in ("new", "updated") and r["id"] in Q and r["id"] not in OWNER:
                OWNER[r["id"]] = zid
    sections = ""
    for band, zs in ORDER:
        sections += f'<h3 class="band">{esc(band)}</h3>' + "".join(zone_section(z) for z in zs)
    css = open("report.css", encoding="utf-8").read()
    js = open("report.js", encoding="utf-8").read()
    page = f"""<title>Forever Alliance Quest Atlas</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600;700&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>{css}</style>
<div class="wrap">
<header class="top">
  <div class="title"><span class="eyebrow">World of Warcraft: Forever · beta 1.60.1 · Alliance 1-30</span><h1>Forever Alliance Quest Atlas</h1>
  <p class="lede">Every quest Wowhead's Forever database marks as <b>new</b> or <b>updated</b> in the Alliance levelling zones, with givers, coordinates, XP, chains and rewards, pulled on {now}. The beta cap is 20, so 1-20 zones are well covered and 20-30 zones fill in as the cap rises; nothing past 30 exists yet. Coordinates come from Wowhead client sightings and can be a few units off.</p></div>
  <div class="tiles"><div class="tile"><b>{tot_new}</b><span>new quests<br>Alliance-usable</span></div><div class="tile"><b>{tot_xp:,}</b><span>XP from new<br>non-class quests</span></div><div class="tile"><b>{tot_upd}</b><span>updated<br>quests</span></div><div class="tile"><b>{len([z for z in all_zone_ids if os.path.exists(f'{DATA}/zone_{z}.json')])}</b><span>zones &amp;<br>dungeons scanned</span></div></div>
</header>
<div class="controls" id="controls">
  <label class="chk"><input type="checkbox" id="f-updated"> show updated quests</label>
  <label class="chk"><input type="checkbox" id="f-horde"> show Horde-only</label>
  <label class="sel">class <select id="f-class"><option value="all">all</option><option value="none">none (hide class quests)</option>{"".join(f'<option value="{n}">{n}</option>' for n in CLASSES.values())}</select></label>
  <label class="search"><input type="search" id="f-search" placeholder="filter by quest name"></label>
  <span class="count" id="f-count"></span>
</div>
<nav class="znav">{nav}</nav>
<main>{sections}</main>
<footer class="foot"><p>Source: wowhead.com/forever zone, quest and NPC pages (crowdsourced via the Wowhead client), read {now}. "New" and "updated" are Wowhead's own change flags against Classic Era; the change notes on updated quests are Wowhead's diff lines. Quest rows link to the Wowhead page. Class quests are tagged and can be hidden with the class filter.</p></footer>
</div>
<script>{js}</script>
"""
    open("forever-alliance-quest-atlas.html", "w", encoding="utf-8").write(page)
    # standalone copy for opening straight from disk (the Artifact tool adds this skeleton itself)
    local = ('<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
             '<style>:root{color-scheme:light}body{margin:0;font:14px system-ui}img{max-width:100%}[hidden]{display:none!important}</style></head><body>'
             + page + '</body></html>')
    open("forever-alliance-quest-atlas.local.html", "w", encoding="utf-8").write(local)
    print("wrote", len(page), "bytes;", tot_new, "new /", tot_upd, "updated /", tot_xp, "xp")

if __name__ == "__main__":
    build()
