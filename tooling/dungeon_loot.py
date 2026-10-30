#!/usr/bin/env python3
"""Dungeon loot report for the Dwarf 2H Enhancement shaman route (REPORT ONLY - writes nothing but its report file).

For each dungeon chapter of the guide: every creature QuestieDB places in the dungeon, every item those creatures
drop, filtered to gear a Dwarf 2H Enhancement shaman can wear at 1-30 (by the client Item table), scored with the
weights/score_items.py parser and weights, and checked against what the guide already mentions.

    python tooling\\dungeon_loot.py                 -> Claude outputs\\dungeon-loot-<today>.md
    python tooling\\dungeon_loot.py --stdout        -> print the report instead
    python tooling\\dungeon_loot.py --chapter 07    -> one dungeon chapter only

Inputs (read only):
  tooling/qdb/npc.json, item.json, META.json     via guidelib.db()  (npc [0] name, [6] spawns {zoneId: ...};
                                                 item [0] name, [1] npcDrops, [9] required level)
  tooling/client/<highest build>/Item.csv        ClassID / SubclassID / InventoryType per item id (wago.tools, wowf)
  weights/tooltips/<newest YYYY-MM-DD>.json      Wowhead Forever tooltips {name: {"id", "tooltip"}}; falls back to
  or weights/item_tooltips.json                  the 24 Sep 2026 scrape when no dated cache exists
  guide/Guidelime_ForeverAlliance/*.lua          chapter text (mentions, baseline gear)

Scoring: score_items.parse() + score_items.score(). The level-20 central / conservative sets are copied from
score_items.main() (they are locals there and can't be imported). Levels 10 and 15 take the same sets with Int, Agi
and the mace term replaced by enh_weights.weights() for that band (Spirit / SP / Expertise are held at the
recommended values in every band, as docs/forever-enh-stat-weights.md does). Each chapter uses the band nearest
its starting level.
"""
import argparse, csv, datetime, glob, json, os, re, sys, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import guidelib as gl

WEIGHTS_DIR = os.path.join(gl.BASE, 'weights')
sys.path.insert(0, WEIGHTS_DIR)
# score_items.py has no import-time side effects (main() is behind __name__ == "__main__"); it imports enh_weights,
# which is also guarded. Both are only read here.
from score_items import parse, score, usable  # noqa: E402
from enh_weights import band_scenarios, weights as model_weights  # noqa: E402

# ---------------------------------------------------------------- dungeon chapters
# chapter file prefix -> QuestieDB zone id of the dungeon
DUNGEONS = {
    '03': 16919,   # Hall of Thanes
    '07': 1581,    # The Deadmines
    '08': 16611,   # Ruins of Lordaeron
    '13': 719,     # Blackfathom Deeps
    '15': 717,     # The Stockade
    '22': 16732,   # Excavation Site
    '24': 721,     # Gnomeregan
    '26': 491,     # Razorfen Kraul
}

# ---------------------------------------------------------------- what a Dwarf 2H Enhancement shaman can use (1-30)
# Item.csv ClassID / SubclassID -> label. A tuple value restricts the row to those InventoryTypes
# (2 neck, 11 finger, 12 trinket, 16 cloak). Anything not listed (mail 3, plate 4, shields 6, swords, polearms,
# bows, guns, wands, librams/totems, off-hand held items, non-gear) is dropped.
USABLE = {
    (2, 0):  ('1H axe', None),
    (2, 1):  ('2H axe', None),
    (2, 4):  ('1H mace', None),
    (2, 5):  ('2H mace', None),
    (2, 10): ('staff', None),
    (2, 13): ('fist weapon', None),
    (2, 15): ('dagger', None),
    (4, 2):  ('leather', None),
    (4, 1):  ('cloth', (16,)),            # cloth only as a cloak
    (4, 0):  ('misc', (2, 11, 12)),       # neck, ring, trinket
}
INVTYPE = {1: 'head', 2: 'neck', 3: 'shoulder', 5: 'chest', 20: 'chest', 6: 'waist', 7: 'legs', 8: 'feet', 9: 'wrist',
           10: 'hands', 11: 'finger', 12: 'trinket', 13: '1H', 16: 'back', 17: '2H', 21: 'main hand', 22: 'off hand'}

# score_items.py slot names -> comparison group for the baseline (1H weapon slots compare with each other)
SLOT_GROUP = {'Main Hand': '1H weapon', 'One-Hand': '1H weapon'}

# ---------------------------------------------------------------- weights
# Copied verbatim from score_items.main() (level-20 band).
W20_CENTRAL = dict(wdps=14.0, str=2.0, ap=1.0, int=1.05, agi=0.85, spi=1.0, sta=0.0, sp=1.5, exp=3.0, mace_bonus=7.0)
W20_CONSERVATIVE = dict(wdps=14.0, str=2.0, ap=1.0, int=1.05, agi=0.85, spi=0.5, sta=0.0, sp=0.5, exp=1.0, mace_bonus=7.0)
BANDS = (10, 15, 20)


def band_weights():
    """{band: (central, conservative)}. 20 = score_items' sets; 10/15 = those with model Int/Agi/mace for the band."""
    out = {20: (W20_CENTRAL, W20_CONSERVATIVE)}
    scen = band_scenarios()
    for b in (10, 15):
        m, _ = model_weights(scen[b])
        over = {k: round(m[k], 2) for k in ('int', 'agi', 'mace_bonus')}
        out[b] = (dict(W20_CENTRAL, **over), dict(W20_CONSERVATIVE, **over))
    return out


def nearest_band(level):
    return min(BANDS, key=lambda b: (abs(b - level), -b))


# ---------------------------------------------------------------- inputs
def to_ascii(s):
    return unicodedata.normalize('NFKD', str(s)).encode('ascii', 'ignore').decode('ascii')


def ascii(s):
    """ASCII for a table cell (a '|' would break the Markdown table)."""
    return to_ascii(s).replace('|', '/')


def client_item_table():
    root = os.path.join(HERE, 'client')
    builds = [d for d in os.listdir(root) if os.path.exists(os.path.join(root, d, 'Item.csv'))]
    if not builds:
        sys.exit('no tooling/client/<build>/Item.csv found')
    build = max(builds, key=lambda d: tuple(int(x) if x.isdigit() else 0 for x in d.split('.')))
    rows = {}
    with open(os.path.join(root, build, 'Item.csv'), encoding='utf-8', newline='') as f:
        for r in csv.DictReader(f):
            rows[int(r['ID'])] = (int(r['ClassID']), int(r['SubclassID']), int(r['InventoryType']))
    return build, rows


def tooltip_sources():
    """[(path, date string)] newest first: every weights/tooltips/<YYYY-MM-DD>.json, then weights/item_tooltips.json.
    An item takes its tooltip from the newest file that has it, so a partial new cache does not hide the old scrape."""
    dated = sorted((p for p in glob.glob(os.path.join(WEIGHTS_DIR, 'tooltips', '*.json'))
                    if re.fullmatch(r'\d{4}-\d{2}-\d{2}', os.path.splitext(os.path.basename(p))[0])), reverse=True)
    out = [(p, os.path.splitext(os.path.basename(p))[0]) for p in dated]
    p = os.path.join(WEIGHTS_DIR, 'item_tooltips.json')
    if os.path.exists(p):
        out.append((p, datetime.date.fromtimestamp(os.path.getmtime(p)).isoformat() + ' (file date)'))
    return out


def load_tooltips(paths):
    """-> (by_id {id: (name, rec)}, by_name {lower name: (name, rec)}, {path: items taken from it}); paths newest first."""
    by_id, by_name, used = {}, {}, {}
    for path in paths:
        i, n = _load_one(path)
        used[path] = 0
        for k, v in i.items():
            if k not in by_id:
                by_id[k] = v
                used[path] += 1
        for k, v in n.items():
            if k not in by_name:
                by_name[k] = v
                if v[1].get('id') is None:
                    used[path] += 1
    return by_id, by_name, used


def _load_one(path):
    """One cache file: {name: {id, tooltip}}, {id: {name, tooltip}} or [{id, name, tooltip}, ...]."""
    raw = json.load(open(path, encoding='utf-8'))
    recs = []
    if isinstance(raw, dict):
        for k, v in raw.items():
            if not isinstance(v, dict) or 'tooltip' not in v:
                continue
            if k.isdigit() and 'name' in v:
                recs.append((v['name'], dict(v, id=v.get('id', int(k)))))
            else:
                recs.append((v.get('name', k), v))
    else:
        recs = [(v.get('name', ''), v) for v in raw if isinstance(v, dict) and 'tooltip' in v]
    by_id, by_name = {}, {}
    for name, rec in recs:
        if rec.get('id') is not None:
            by_id[int(rec['id'])] = (name, rec)
        by_name.setdefault(name.lower(), (name, rec))
    return by_id, by_name


def chapters():
    """[(prefix, file, text, start level, end level, title, ga)] in file-name order."""
    out = []
    for path in gl.chapter_files():
        fn = os.path.basename(path)
        txt = gl.read(path)
        lo, hi = gl.chapter_band(txt)
        out.append((fn.split('_')[0], fn, txt, lo, hi, gl.chapter_title(txt), gl.chapter_ga(txt)))
    return out


# ---------------------------------------------------------------- report
DROP_RE = re.compile(r'Drop Chance:?\s*([\d.]+\s*%)', re.I)


def build(only=None):
    npc, item = gl.db('npc'), gl.db('item')
    meta = json.load(open(os.path.join(gl.QDB, 'META.json'), encoding='utf-8'))
    cbuild, client = client_item_table()
    tt_srcs = tooltip_sources()
    if not tt_srcs:
        sys.exit('no tooltip cache found under weights/')
    tt_id, tt_name, tt_used = load_tooltips([p for p, _ in tt_srcs])
    bw = band_weights()
    chs = chapters()

    # reverse index: npc id -> items it drops
    drops_of = {}
    for iid, r in item.items():
        for n in (r[1] or []):
            if n is not None:
                drops_of.setdefault(int(n), []).append(int(iid))

    def tooltip_for(iid, name):
        if iid in tt_id:
            return tt_id[iid]
        hit = tt_name.get(name.lower())
        if hit and (hit[1].get('id') in (None, iid)):
            return hit
        return None

    # baseline candidates: tooltip items named on Gear:/Loot: lines (Dwarf shaman lines only), per chapter
    gear_lines = {}
    for pre, fn, txt, lo, hi, title, ga in chs:
        if ga == 'Human':
            gear_lines[pre] = []
            continue
        ls = [l for _, l in gl.steps(txt) if ('Gear:' in l or 'Loot:' in l) and '[A Hunter]' not in l and '[GA Human]' not in l]
        gear_lines[pre] = [l.lower() for l in ls]

    lines = ['# Dungeon loot check - %s' % datetime.date.today().isoformat(), '',
             'Report only (tooling/dungeon_loot.py). Gear a Dwarf 2H Enhancement shaman can use at 1-30 that QuestieDB lists as '
             'dropping from creatures inside each dungeon, scored with weights/score_items.py (AP-equivalent; central and '
             'conservative weight sets, band nearest the chapter\'s starting level). "Beats guide gear" compares the central '
             'score with the best item in the same slot named on a Gear:/Loot: line (Shaman/Dwarf lines) in this chapter or '
             'any earlier one. Mail, plate, shields, swords, polearms, ranged and cloth other than cloaks are left out.', '']
    no_tt_lines = []
    order = [c for c in chs if c[0] in DUNGEONS and (only is None or c[0] == only)]
    if only is not None and not order:
        sys.exit('chapter %s is not a dungeon chapter (%s)' % (only, ', '.join(sorted(DUNGEONS))))

    for pre, fn, txt, lo, hi, title, ga in order:
        zid = str(DUNGEONS[pre])
        band = nearest_band(lo)
        wc, wk = bw[band]
        low_txt = txt.lower()
        npcs = {int(k): r for k, r in npc.items() if isinstance(r[6], dict) and zid in r[6]}

        # drops kept by the usability filter
        kept = {}
        for nid in npcs:
            for iid in drops_of.get(nid, []):
                c = client.get(iid)
                if not c:
                    continue
                u = USABLE.get((c[0], c[1]))
                if not u or (u[1] is not None and c[2] not in u[1]):
                    continue
                k = kept.setdefault(iid, dict(id=iid, name=item[str(iid)][0] or '?', droppers=set(), cls=c, typ=u[0]))
                k['droppers'].add(npcs[nid][0] or str(nid))

        # baseline per slot group
        base = {}
        for p2, *_ in [c for c in chs if c[0] <= pre]:
            for lname, (name, rec) in tt_name.items():
                if any(lname in l for l in gear_lines.get(p2, [])):
                    it = parse(name, rec)
                    if not usable(it)[0]:
                        continue
                    base.setdefault(SLOT_GROUP.get(it['slot'], it['slot']), {})[name] = score(it, wc)

        rows = []
        for k in kept.values():
            c = k['cls']
            req = item[str(k['id'])][9] if len(item[str(k['id'])]) > 9 else None
            slot = INVTYPE.get(c[2], 'inv%d' % c[2])
            k['slottype'] = slot if k['typ'] in ('misc',) else ('%s %s' % (slot, k['typ']) if k['typ'] in ('leather', 'cloth') else k['typ'])
            t = tooltip_for(k['id'], k['name'])
            k['tt'] = t is not None
            k['mentioned'] = k['name'].lower() in low_txt
            k['elsewhere'] = [p for p, _, t2, *_ in chs if p != pre and k['name'].lower() in t2.lower()]
            if t:
                it = parse(t[0], t[1])
                k['req'] = it['req'] or req
                k['sc'], k['sk'] = score(it, wc), score(it, wk)
                g = SLOT_GROUP.get(it['slot'], it['slot'])
                cands = [(s, n) for n, s in base.get(g, {}).items() if n.lower() != t[0].lower()]  # never itself
                if cands:
                    bs, bn = max(cands)
                    k['beats'] = '%s (vs %s %.1f)' % ('yes' if k['sc'] > bs else 'no', bn, bs)
                else:
                    k['beats'] = 'no baseline'
                m = DROP_RE.search(t[1]['tooltip'])
                k['drop'] = m.group(1).replace(' ', '') if m else 'unknown'
            else:
                k['req'] = req
                k['sc'] = k['sk'] = None
                k['beats'] = 'no tooltip'
                k['drop'] = 'unknown'
            rows.append(k)

        lines += ['## %s - %s (levels %d-%d)' % (fn[:-4], ascii(title), lo, hi), '',
                  '- Dungeon zone id %s; creatures in QuestieDB: %d; usable gear drops: %d (%d not mentioned in the chapter); '
                  'weights: level-%d band' % (zid, len(npcs), len(rows), sum(1 for r in rows if not r['mentioned']), band), '']
        if not npcs:
            lines += ['QuestieDB has no creatures for this dungeon - browser pull needed', '']
            no_tt_lines.append('%s: (no creatures in QuestieDB)' % fn[:-4])
            continue

        def drs(r):
            d = sorted(r['droppers'])
            return ascii(', '.join(d[:4]) + (' +%d more' % (len(d) - 4) if len(d) > 4 else ''))

        def key(r):
            return (r['sc'] is None, -(r['sc'] or 0), r['name'])

        nm = sorted([r for r in rows if not r['mentioned']], key=key)
        lines += ['### Not mentioned in this chapter', '']
        if nm:
            lines += ['| item | id | slot/type | req | dropper(s) | central | conservative | beats guide gear | drop chance |',
                      '|---|---|---|---|---|---|---|---|---|']
            for r in nm:
                el = (' (named in %s)' % ', '.join(r['elsewhere'])) if r['elsewhere'] else ''
                lines.append('| %s%s | %d | %s | %s | %s | %s | %s | %s | %s |' % (
                    ascii(r['name']), el, r['id'], r['slottype'], r['req'] if r['req'] else '?', drs(r),
                    '%.1f' % r['sc'] if r['sc'] is not None else 'no tooltip',
                    '%.1f' % r['sk'] if r['sk'] is not None else 'no tooltip', ascii(r['beats']), r['drop']))
        else:
            lines.append('(none)')
        lines += ['', '### Mentioned in this chapter', '']
        men = sorted([r for r in rows if r['mentioned']], key=key)
        for r in men:
            sc = ('%.1f / %.1f' % (r['sc'], r['sk'])) if r['sc'] is not None else 'no tooltip'
            lines.append('- %s (%d, %s, req %s, %s) - %s; beats guide gear: %s; drop chance: %s' % (
                ascii(r['name']), r['id'], r['slottype'], r['req'] or '?', drs(r), sc, ascii(r['beats']), r['drop']))
        if not men:
            lines.append('(none)')
        lines.append('')
        ids = sorted(r['id'] for r in rows if not r['tt'])
        no_tt_lines.append('%s: %s' % (fn[:-4], ' '.join(map(str, ids)) if ids else '(none)'))

    lines += ['## Item ids with no tooltip', '', '```'] + no_tt_lines + ['```', '',
              '## Data provenance', '',
              '- QuestieDB: %s %s (contract %s, built %s) - tooling/qdb/' % (meta.get('flavor'), meta.get('version'), meta.get('contract'), meta.get('build_time')),
              '- Client Item table: build %s - tooling/client/%s/Item.csv' % (cbuild, cbuild),
              '- Tooltips (newest file wins per item): ' + '; '.join('%s dated %s - %d items taken' % (
                  os.path.relpath(p, gl.BASE).replace('\\', '/'), d, tt_used[p]) for p, d in tt_srcs),
              '- Weights: level-20 central %s; conservative Spi %.1f SP %.1f Exp %.1f; bands 10/15 Int/Agi/mace from enh_weights: %s' % (
                  ' '.join('%s=%g' % kv for kv in W20_CENTRAL.items()), W20_CONSERVATIVE['spi'], W20_CONSERVATIVE['sp'], W20_CONSERVATIVE['exp'],
                  '; '.join('L%d int=%g agi=%g mace=%g' % (b, bw[b][0]['int'], bw[b][0]['agi'], bw[b][0]['mace_bonus']) for b in (10, 15))),
              '- Drop chances come only from tooltip text ("Drop Chance"); Wowhead shows them only for single-dropper items.', '']
    return '\n'.join(to_ascii(l) for l in lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--stdout', action='store_true', help='print the report instead of writing it')
    ap.add_argument('--chapter', help='limit to one dungeon chapter, e.g. 07')
    a = ap.parse_args()
    rep = build(a.chapter.zfill(2) if a.chapter else None)
    if a.stdout:
        sys.stdout.write(rep)
        return
    out_dir = os.path.normpath(os.path.join(gl.BASE, 'Claude outputs'))
    os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, 'dungeon-loot-%s.md' % datetime.date.today().isoformat())
    with open(out, 'w', encoding='ascii', newline='\n') as f:
        f.write(rep)
    print(out)


if __name__ == '__main__':
    main()
