#!/usr/bin/env python3
"""Wowhead Forever scraper: zone listviews -> quest pages (new/updated) -> NPC/object pages (coords).
Everything is cached under raw/ so re-runs are free. Polite: ~1 request/sec, retries with backoff.
"""
import re, json, os, sys, time, random, html as htmlmod
import urllib.request, urllib.error

BASE = "https://www.wowhead.com/forever/"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
RAW = "raw"; DATA = "data"
os.makedirs(RAW, exist_ok=True); os.makedirs(DATA, exist_ok=True)
LOG = open("scrape.log", "a", encoding="utf-8")
def log(*a):
    s = " ".join(str(x) for x in a); print(s); LOG.write(s + "\n"); LOG.flush()

_last = 0.0
def fetch(path, key, min_gap=1.0):
    """GET BASE+path, cache to raw/<key>.html. Returns html text or None."""
    fn = os.path.join(RAW, f"{key}.html")
    if os.path.exists(fn) and os.path.getsize(fn) > 2000:
        return open(fn, encoding="utf-8", errors="ignore").read()
    global _last
    for attempt in range(5):
        wait = max(0, _last + min_gap + random.uniform(0, 0.4) - time.time())
        if wait > 0: time.sleep(wait)
        _last = time.time()
        req = urllib.request.Request(BASE + path, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=40) as r:
                body = r.read().decode("utf-8", errors="ignore")
            if len(body) < 2000:
                log("short body", path, len(body)); time.sleep(5); continue
            open(fn, "w", encoding="utf-8").write(body)
            return body
        except urllib.error.HTTPError as e:
            log("HTTP", e.code, path)
            if e.code == 404:
                open(fn, "w").write("<!-- 404 -->" + " " * 2100); return None
            time.sleep(10 * (attempt + 1))
        except Exception as e:
            log("ERR", path, repr(e)); time.sleep(10 * (attempt + 1))
    return None

def raw_json_at(text, start):
    dec = json.JSONDecoder()
    obj, _ = dec.raw_decode(text[start:])
    return obj

def parse_listviews(h):
    """Return {listview_id: rows} from either inline Listview calls or the listPage JSON blob."""
    out = {}
    for m in re.finditer(r"new Listview\(\{template: '(\w+)', id: '([\w-]+)'", h):
        # find `data: [` after this match
        i = h.find("data: [", m.end())
        if i < 0: continue
        try:
            rows = raw_json_at(h, i + len("data: "))
        except Exception as e:
            log("listview parse fail", m.group(2), e); continue
        out[m.group(2)] = {"template": m.group(1), "rows": rows}
    m = re.search(r'<script type="application/json" id="data\.page\.listPage\.listviews">(.*?)</script>', h, re.S)
    if m:
        try:
            for lv in json.loads(m.group(1)):
                out[lv["id"]] = {"template": lv["template"], "rows": lv["data"]}
        except Exception as e:
            log("listPage parse fail", e)
    return out

def strip_tags(s):
    s = re.sub(r"<br\s*/?>", "\n", s)
    s = re.sub(r"<[^>]+>", "", s)
    return htmlmod.unescape(s).strip()

def parse_infobox(h):
    m = re.search(r'printHtml\("(\[ul\].*?)",\s*"infobox', h, re.S)
    if not m: return {}
    bb = m.group(1).replace("\\/", "/").replace('\\"', '"')
    items = re.findall(r"\[li\](.*?)\[/li\]", bb, re.S)
    info = {"raw": items}
    ents = {"start": [], "end": []}
    for it in items:
        t = re.sub(r"\[/?[^\]]+\]", "", it).strip()
        if t.startswith("Level:"): info["level"] = int(re.search(r"\d+", t).group())
        elif t.startswith("Requires level"): info["reqlevel"] = int(re.search(r"\d+", t).group())
        elif t.startswith("Type:"): info["type"] = t.split(":", 1)[1].strip()
        elif t.startswith("Side:"): info["side_text"] = t.split(":", 1)[1].strip()
        elif t.startswith("Start:") or t.startswith("End:"):
            key = "start" if t.startswith("Start:") else "end"
            found = re.findall(r"\[url=/forever/(npc|object|item)=(\d+)[^\]]*\](.*?)\[/url\]", it)
            for kind, eid, name in found:
                ents[key].append({"kind": kind, "id": int(eid), "name": name})
            if not found:
                for eid in re.findall(r"Object #(\d+)", it):
                    ents[key].append({"kind": "object", "id": int(eid), "name": f"Object #{eid} (unnamed, e.g. a poster or crate)"})
        elif t.startswith("Added in patch"): info["patch"] = t.replace("Added in patch", "").strip()
        elif t in ("Sharable", "Not sharable", "Repeatable", "Daily"): info[t.lower().replace(" ", "_")] = True
        elif t.startswith("Series") or t.startswith("Part of"): info["series_text"] = t
        elif t.startswith("Race") or t.startswith("Class") or t.startswith("Requires"): info.setdefault("reqs", []).append(t)
    info["start"] = ents["start"]; info["end"] = ents["end"]
    return info

def parse_quest(h, qid):
    q = {"id": qid}
    m = re.search(r"\$\.extend\(g_quests\[%d\], " % qid, h)
    if m:
        try: q["g"] = raw_json_at(h, m.end())
        except Exception as e: log("g_quests parse fail", qid, e)
    q["info"] = parse_infobox(h)
    # objective text + objective rows
    m = re.search(r'<h1 class="heading-size-1">(.*?)</h1>(.*?)(?=<script|<h2)', h, re.S)
    if m:
        q["name"] = strip_tags(m.group(1))
        body = m.group(2)
        obj_text = re.split(r'<table class="icon-list">', body)[0]
        q["objective_text"] = strip_tags(obj_text)
        rows = re.findall(r'<tr data-icon-list-quantity="(\d+)">(.*?)</tr>', body, re.S)
        q["objectives"] = []
        for qty, row in rows:
            link = re.search(r'/forever/(npc|object|item)=(\d+)', row)
            q["objectives"].append({"qty": int(qty), "text": strip_tags(re.sub(r'<span class="icon-list-quantity-wrapper.*', "", row, flags=re.S)),
                                    "kind": link.group(1) if link else None, "eid": int(link.group(2)) if link else None})
    m = re.search(r'<h2 class="heading-size-3">Description</h2>(.*?)<h2', h, re.S)
    if m: q["description"] = strip_tags(m.group(1))[:1200]
    m = re.search(r'<table class="series">(.*?)</table>', h, re.S)
    if m:
        ser = []
        for n, cell in re.findall(r'<th>(\d+)\.</th><td>(.*?)</td>', m.group(1), re.S):
            link = re.search(r'quest=(\d+)[^"]*">(.*?)</a>', cell)
            if link: ser.append({"n": int(n), "id": int(link.group(1)), "name": strip_tags(link.group(2))})
            else: ser.append({"n": int(n), "id": qid, "name": strip_tags(cell), "current": True})
        q["series"] = ser
    m = re.search(r"setupScalingRewards\((\{.*?\})\);", h)
    if m:
        try:
            sr = json.loads(m.group(1)); q["xp_levels"] = sr.get("xp", {}).get("levels"); q["coin_levels"] = sr.get("coin", {}).get("levels")
        except Exception: pass
    # item data (rewards etc.)
    items = {}
    for m in re.finditer(r"WH\.Gatherer\.addData\(3, 16, ", h):
        try:
            d = raw_json_at(h, m.end())
            for k, v in d.items():
                items[int(k)] = {"name": v.get("name_enus"), "quality": v.get("quality"), "equip": v.get("jsonequip", {})}
        except Exception as e: log("item gatherer fail", qid, e)
    q["items"] = items
    m = re.search(r"g_mapperData\s*=\s*", h)
    if m:
        try: q["mapper"] = raw_json_at(h, m.end())
        except Exception: pass
    # comments (noscript) — first few, for location hints
    m = re.search(r'<noscript><div id="user-comments">(.*?)</noscript>', h, re.S)
    if m:
        cs = re.findall(r'<div class="user-post-">.*?</h3>(.*?)</div>', m.group(1), re.S)
        q["comments"] = [strip_tags(c)[:400] for c in cs[:4]]
    return q

def parse_entity(h, kind, eid):
    e = {"kind": kind, "id": eid}
    m = re.search(r"<title>(.*?) - ", h); e["name"] = htmlmod.unescape(m.group(1)) if m else None
    m = re.search(r"g_mapperData\s*=\s*", h)
    if m:
        try: e["mapper"] = raw_json_at(h, m.end())
        except Exception as ex: log("mapper fail", kind, eid, ex)
    var = {"npc": "g_npcs", "object": "g_objects", "item": "g_items"}[kind]
    m = re.search(r"\$\.extend\(%s\[%d\], " % (var, eid), h)
    if m:
        try: e["g"] = raw_json_at(h, m.end())
        except Exception as ex: log("g_ent fail", kind, eid, ex)
    m = re.search(r'printHtml\("(\[ul\].*?)",\s*"infobox', h, re.S)
    if m:
        bb = m.group(1).replace("\\/", "/")
        e["infobox"] = [re.sub(r"\[/?[^\]]+\]", "", it).strip() for it in re.findall(r"\[li\](.*?)\[/li\]", bb, re.S)]
    m = re.search(r'<noscript><div id="user-comments">(.*?)</noscript>', h, re.S)
    if m:
        cs = re.findall(r'<div class="user-post-">.*?</h3>(.*?)</div>', m.group(1), re.S)
        e["comments"] = [strip_tags(c)[:300] for c in cs[:3]]
    return e

ZONES = {
    1: "dun-morogh", 12: "elwynn-forest", 141: "teldrassil", 40: "westfall", 38: "loch-modan", 44: "redridge-mountains",
    148: "darkshore", 10: "duskwood", 11: "wetlands", 331: "ashenvale", 406: "stonetalon-mountains", 267: "hillsbrad-foothills",
    36: "alterac-mountains", 45: "arathi-highlands", 400: "thousand-needles", 33: "stranglethorn-vale",
    1519: "stormwind-city", 1537: "ironforge", 1657: "darnassus", 16593: "zephras-isle",
    1581: "the-deadmines", 717: "the-stockade", 721: "gnomeregan", 718: "wailing-caverns", 719: "blackfathom-deeps",
    209: "shadowfang-keep", 491: "razorfen-kraul", 796: "scarlet-monastery", 16919: "the-hall-of-thanes", 16611: "ruins-of-lordaeron",
    16632: "half-pint-tavern", 16732: "excavation-site-wetlands", 17191: "manor-mistmantle", 16562: "hillsbrad-foothills",
    16544: "city-of-dalaran", 16560: "city-of-dalaran",
}

def main(only=None):
    zones = {}
    for zid, slug in ZONES.items():
        if only and zid not in only: continue
        h = fetch(f"zone={zid}/{slug}", f"zone_{zid}")
        if not h: log("zone fetch failed", zid); continue
        lvs = parse_listviews(h)
        z = {"id": zid, "slug": slug, "quests": lvs.get("quests", {}).get("rows", []), "npcs": lvs.get("npcs", {}).get("rows", []),
             "objects": lvs.get("objects", {}).get("rows", []), "items_start": lvs.get("starts-quest", {}).get("rows", []),
             "items_rewards": lvs.get("quest-rewards", {}).get("rows", [])}
        zones[zid] = z
        json.dump(z, open(f"{DATA}/zone_{zid}.json", "w"))
        from collections import Counter
        log(f"zone {zid} {slug}: quests {len(z['quests'])} {dict(Counter(r.get('envChange',{}).get('status') for r in z['quests']))} npcs {len(z['npcs'])} objects {len(z['objects'])}")
    # quests to fetch: new or updated, any side (Alliance filter happens in the report)
    want = {}
    for z in zones.values():
        for r in z["quests"]:
            st = r.get("envChange", {}).get("status")
            if st in ("new", "updated"):
                want[r["id"]] = r
    log("quest pages to fetch:", len(want))
    quests = {}
    qf = f"{DATA}/quests.json"
    if os.path.exists(qf): quests = {int(k): v for k, v in json.load(open(qf, encoding="utf-8")).items()}
    n = 0
    for qid, r in sorted(want.items()):
        if qid in quests: continue
        h = fetch(f"quest={qid}", f"quest_{qid}")
        if not h: continue
        q = parse_quest(h, qid); q["list"] = r
        quests[qid] = q; n += 1
        if n % 25 == 0:
            json.dump(quests, open(qf, "w")); log("quests fetched", n, "/", len(want))
    json.dump(quests, open(qf, "w")); log("quests done", len(quests))
    # entities: start/end of fetched quests + objective entities
    ents = {}
    ef = f"{DATA}/entities.json"
    if os.path.exists(ef): ents = json.load(open(ef, encoding="utf-8"))
    need = set()
    for q in quests.values():
        for k in ("start", "end"):
            for e in q.get("info", {}).get(k, []): need.add((e["kind"], e["id"]))
        for o in q.get("objectives", []):
            if o.get("kind") in ("npc", "object") and o.get("eid"): need.add((o["kind"], o["eid"]))
    log("entities to fetch:", len(need))
    n = 0
    for kind, eid in sorted(need):
        key = f"{kind}:{eid}"
        if key in ents: continue
        h = fetch(f"{kind}={eid}", f"{kind}_{eid}")
        if not h: continue
        ents[key] = parse_entity(h, kind, eid); n += 1
        if n % 25 == 0:
            json.dump(ents, open(ef, "w")); log("entities fetched", n, "/", len(need))
    json.dump(ents, open(ef, "w")); log("entities done", len(ents))

def reparse():
    quests = {int(k): v for k, v in json.load(open(f"{DATA}/quests.json", encoding="utf-8")).items()}
    for qid, q in quests.items():
        fn = f"{RAW}/quest_{qid}.html"
        if os.path.exists(fn):
            nq = parse_quest(open(fn, encoding="utf-8", errors="ignore").read(), qid); nq["list"] = q["list"]; quests[qid] = nq
    json.dump(quests, open(f"{DATA}/quests.json", "w")); log("reparsed", len(quests))
    ents = json.load(open(f"{DATA}/entities.json", encoding="utf-8"))
    for key in list(ents):
        kind, eid = key.split(":"); fn = f"{RAW}/{kind}_{eid}.html"
        if os.path.exists(fn): ents[key] = parse_entity(open(fn, encoding="utf-8", errors="ignore").read(), kind, int(eid))
    json.dump(ents, open(f"{DATA}/entities.json", "w")); log("reparsed entities", len(ents))

if __name__ == "__main__":
    if sys.argv[1:] == ["reparse"]: reparse(); sys.exit()
    only = [int(x) for x in sys.argv[1:]] or None
    main(only)
