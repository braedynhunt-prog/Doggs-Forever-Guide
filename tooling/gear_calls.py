#!/usr/bin/env python3
"""Gear-call check for the Dwarf 2H Enhancement shaman route (REPORT ONLY - writes nothing but its report file).

Checks every gear call in the Dwarf chain of the guide against today's Forever item tooltips and stat weights:
  Part 1  quoted stats - "Name (leather chest +4 Str +3 Agi ...)" / "Name (2H mace 19.7 dps +11 Str, req 18)" compared
          with score_items.parse() of the item's tooltip
  Part 2  quest-reward picks - every [QT] on a Shaman/Dwarf line whose quest offers 2+ reward choices, each usable
          choice scored with the chapter's band weights (central and conservative), compared with the guide's pick
  Part 3  reward-choice ids and gear-line items with no tooltip in the cache (input for fetch_tooltips.py --from-file)

    python tooling\\gear_calls.py            -> Claude outputs\\gear-calls-<today>.md
    python tooling\\gear_calls.py --stdout   -> print the report instead

Inputs (read only):
  guide/Guidelime_ForeverAlliance/*.lua     gl.chain_files('Dwarf'); lines with [A ...Hunter...] or [GA Human] skipped
  weights/tooltips/<newest>.json (+ older)  dungeon_loot.tooltip_sources() / load_tooltips()
  data/zone_*.json                          Wowhead Forever quest rows: "itemchoices" [[itemId, count], ...] - the same
                                            source and field qinfo.py prints as "rewards: choice [...]"
  tooling/qdb/item.json                     item names ([0])
  tooling/client/<build>/Item.csv           ClassID 2/4 (weapon/armor) to decide which item.json names count as gear
                                            when they appear on a gear line (dungeon_loot.client_item_table())

Gear line: a |cffffcc00...|r heading whose text contains "Gear" or "Loot", or a green |cff66ff66Name|r item.
Weights: dungeon_loot.band_weights(), band = nearest_band(chapter start level).
Guide pick (Part 2): from the gear lines on the [QT] line and the next 3 steps (Hunter / Human lines skipped):
the green item that is one of the quest's choices, else the first choice name on the line, else "none" when the
heading text starts with nothing/none or the line says vendor/pass/nothing, else "unstated".
"Best" in Part 2 is the best usable non-1H choice by central score; 1H weapons (usable() note "1H (shield set only)")
only count as best when no other usable choice exists - the build is 2H and a 1H is the shield set, as in
dungeon_loot.py.
"""
import argparse, datetime, glob, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import guidelib as gl

WEIGHTS_DIR = os.path.join(gl.BASE, 'weights')
sys.path.insert(0, WEIGHTS_DIR)
from score_items import parse, score, usable  # noqa: E402
from dungeon_loot import (band_weights, nearest_band, tooltip_sources, load_tooltips, client_item_table,  # noqa: E402
                          to_ascii, ascii, BANDS, W20_CENTRAL, W20_CONSERVATIVE)

COLOR = re.compile(r'\|c[0-9a-fA-F]{8}|\|r')
HEADING = re.compile(r'\|cffffcc00(.*?)\|r', re.I)
GREEN = re.compile(r'\|cff66ff66([^|]+)\|r', re.I)
QT_TAG = re.compile(r'\[QT(\d+)')
SUFFIX = re.compile(r'\s*\[\d+\]$')
LABELS = {'normal', 'grind', 'luck', 'grind/luck'}

STAT_NAMES = [('attack power', 'ap'), ('spell damage', 'sp'), ('spell dmg', 'sp'), ('expertise', 'exp'),
              ('strength', 'str'), ('agility', 'agi'), ('stamina', 'sta'), ('intellect', 'int'), ('spirit', 'spi'),
              ('str', 'str'), ('agi', 'agi'), ('sta', 'sta'), ('int', 'int'), ('spi', 'spi'), ('ap', 'ap'),
              ('sp', 'sp'), ('exp', 'exp')]
QSTAT = re.compile(r'\+(\d+)\s*(' + '|'.join(re.escape(s) for s, _ in STAT_NAMES) + r')\b', re.I)
QDPS = re.compile(r'(\d+(?:\.\d+)?)\s*dps\b', re.I)
STAT_KEY = {s: k for s, k in STAT_NAMES}
LAB = {'str': 'Str', 'agi': 'Agi', 'sta': 'Sta', 'int': 'Int', 'spi': 'Spi', 'ap': 'AP', 'sp': 'SP', 'exp': 'Exp'}
NONE_WORDS = re.compile(r'\b(nothing|vendor|pass|none)\b', re.I)


def plain(line):
    return COLOR.sub('', line)


def skip_line(line):
    """Hunter / Human lines (including [A Dwarf,Hunter] and [A Human,Hunter])."""
    if '[GA Human]' in line:
        return True
    for m in gl.A_TAG.finditer(line):
        if 'Hunter' in m.group(1) or ('Human' in m.group(1) and 'Dwarf' not in m.group(1)):
            return True
    return False


def is_gear_line(line):
    return any(re.search(r'gear|loot', h, re.I) for h in HEADING.findall(line)) or bool(GREEN.search(line))


def wh_rows():
    """Wowhead Forever quest rows by id from data/zone_*.json (first file wins), as qinfo.py builds WH."""
    wh = {}
    for f in glob.glob(os.path.join(gl.BASE, 'data', 'zone_*.json')):
        for q in json.load(open(f, encoding='utf-8')).get('quests', []):
            wh.setdefault(q['id'], q)
    return wh


class Names:
    """Item-name matcher: tooltip-cache names (suffix ' [id]' stripped) + item.json weapon/armor names."""

    def __init__(self, tt_name, item, client):
        self.by = {}   # lower plain name -> {'tt': [(name, rec)], 'ids': set(item ids)}
        for lname, (name, rec) in tt_name.items():
            p = SUFFIX.sub('', name).strip()
            self.by.setdefault(p.lower(), {'tt': [], 'ids': set(), 'name': p})['tt'].append((name, rec))
        for iid, r in item.items():
            nm = r[0]
            c = client.get(int(iid))
            if not nm or not c or c[0] not in (2, 4):
                continue
            e = self.by.setdefault(nm.lower(), {'tt': [], 'ids': set(), 'name': nm})
            e['ids'].add(int(iid))
        for k in list(self.by):
            # item.json-only one-word names ("Mace", "Maul", "Swiftwind" the NPC) are mostly prose, not item calls
            if len(k) < 4 or k in LABELS or k.startswith('recipe:') or (not self.by[k]['tt'] and ' ' not in k):
                del self.by[k]
        self.all_ids = {}
        for iid, r in item.items():
            if r[0]:
                self.all_ids.setdefault(r[0].lower(), set()).add(int(iid))
        self.order = sorted(self.by, key=len, reverse=True)
        self.pats = {}

    def find(self, text):
        """[(start, end, lower name)] non-overlapping, longest first, case-insensitive, word-bounded."""
        low = text.lower()
        taken = [False] * len(low)
        out = []
        for k in self.order:
            if k not in low:
                continue
            p = self.pats.get(k)
            if p is None:
                p = self.pats[k] = re.compile(r'(?<![A-Za-z0-9])' + re.escape(k) + r'(?![A-Za-z0-9])')
            for m in p.finditer(low):
                if any(taken[m.start():m.end()]):
                    continue
                for i in range(m.start(), m.end()):
                    taken[i] = True
                out.append((m.start(), m.end(), k))
        return sorted(out)


def quoted_stats(par):
    q = {}
    for v, s in QSTAT.findall(par):
        k = STAT_KEY[s.lower()]
        q[k] = q.get(k, 0) + int(v)
    m = QDPS.search(par)
    if m:
        q['wdps'] = float(m.group(1))
    return q


def fmt_item(it):
    parts = []
    if it['wdps']:
        parts.append('%.1f dps' % it['wdps'])
    for k in ('str', 'agi', 'sta', 'int', 'spi', 'ap', 'sp', 'exp'):
        if it[k]:
            parts.append('+%d %s' % (it[k], LAB[k]))
    return ' '.join(parts) or 'no stats'


def fmt_q(q):
    parts = []
    if 'wdps' in q:
        parts.append('%g dps' % q['wdps'])
    for k in ('str', 'agi', 'sta', 'int', 'spi', 'ap', 'sp', 'exp'):
        if k in q:
            parts.append('+%d %s' % (q[k], LAB[k]))
    return ' '.join(parts)


def diff(q, it):
    """List of differing keys between quoted stats and a parsed tooltip item."""
    bad = []
    for k, v in q.items():
        if k == 'wdps':
            if abs(v - it['wdps']) > 0.06:
                bad.append(k)
        elif v != it[k]:
            bad.append(k)
    return bad


def build():
    tt_srcs = tooltip_sources()
    if not tt_srcs:
        sys.exit('no tooltip cache found under weights/')
    tt_id, tt_name, tt_used = load_tooltips([p for p, _ in tt_srcs])
    item = gl.db('item')
    cbuild, client = client_item_table()
    names = Names(tt_name, item, client)
    bw = band_weights()
    wh = wh_rows()

    def tooltip_for(iid, name):
        if iid in tt_id:
            return tt_id[iid]
        hit = tt_name.get(name.lower())
        if hit and (hit[1].get('id') in (None, iid)):
            return hit
        return None

    n_gear = n_matched = 0
    mismatches, ambiguous, unparsed = [], [], []
    missing_names = {}          # lower name -> (display, ids, first place)
    missing_choice_ids = set()
    quests_checked = 0
    flagged, no_data, single = [], [], 0

    for path in gl.chain_files('Dwarf'):
        fn = os.path.basename(path)[:-4]
        txt = gl.read(path)
        ga = gl.chapter_ga(txt)
        if ga == 'Human':
            continue
        lo, hi = gl.chapter_band(txt)
        band = nearest_band(lo)
        wc, wk = bw[band]
        st = [(ln, l) for ln, l in gl.steps(txt)]

        # ---------------- Part 1: gear lines and quoted stats
        for ln, line in st:
            if skip_line(line) or not gl.on_chain(line, ga, 'Dwarf') or not is_gear_line(line):
                continue
            n_gear += 1
            text = plain(line)
            hits = names.find(text)
            for g in GREEN.findall(line):
                gk = g.strip().lower()
                ent = names.by.get(gk)
                if (ent is None or not ent['tt']) and gk in names.all_ids and not gk.startswith('recipe:'):
                    missing_names.setdefault(gk, (g.strip(), sorted(names.all_ids[gk]), '%s:%d' % (fn, ln)))
            for i, (s, e, k) in enumerate(hits):
                ent = names.by[k]
                n_matched += 1
                if not ent['tt']:
                    missing_names.setdefault(k, (ent['name'], sorted(ent['ids']), '%s:%d' % (fn, ln)))
                nxt = hits[i + 1][0] if i + 1 < len(hits) else len(text)
                p = text.find('(', e, min(e + 60, len(text)))
                if p < 0 or p > nxt:
                    continue
                close = text.find(')', p)
                par = text[p + 1:close if close > 0 else len(text)]
                q = quoted_stats(par)
                if not q:
                    if re.search(r'\+\d+|\bdps\b', par, re.I):
                        unparsed.append('%s:%d %s (%s)' % (fn, ln, ent['name'], par))
                    continue
                if not ent['tt']:
                    continue
                parsed = [parse(n, r) for n, r in ent['tt']]
                bads = [diff(q, it) for it in parsed]
                if any(not b for b in bads):
                    continue
                it = parsed[0]
                note = ''
                if 'ap' in bads[0] and re.search(r'Attack Power against', ent['tt'][0][1]['tooltip'], re.I):
                    note = ' (tooltip AP includes conditional "Attack Power against X", which parse() adds in)'
                mismatches.append((fn, ln, ent['name'], fmt_q(q), fmt_item(it),
                                   ', '.join(LAB.get(b, b) for b in bads[0]) + note, par))
                if len(parsed) > 1:
                    ambiguous.append('%s:%d %s - %d tooltips share the name' % (fn, ln, ent['name'], len(parsed)))

        # ---------------- Part 2: reward picks
        for idx, (ln, line) in enumerate(st):
            if skip_line(line) or not gl.on_chain(line, ga, 'Dwarf'):
                continue
            for qm in QT_TAG.finditer(line):
                qid = int(qm.group(1))
                w = wh.get(qid)
                ch = [c[0] for c in (w.get('itemchoices') or [])] if w else []
                if not w:
                    no_data.append('%s:%d QT%d' % (fn, ln, qid))
                if len(ch) < 2:
                    single += 1
                    continue
                quests_checked += 1
                rows = []
                for iid in ch:
                    nm = (item.get(str(iid)) or ['?'])[0] or '?'
                    t = tooltip_for(iid, nm)
                    r = dict(id=iid, name=nm, tt=t is not None)
                    if t:
                        it = parse(t[0], t[1])
                        u, note = usable(it)
                        r.update(it=it, u=u, note=note, sc=score(it, wc), sk=score(it, wk))
                    else:
                        missing_choice_ids.add(iid)
                        r.update(u=None, note='no tooltip', sc=None, sk=None)
                    rows.append(r)

                # guide's pick
                pick, pick_line = 'unstated', None
                cnames = {r['name'].lower(): r for r in rows}
                window = [st[j] for j in range(idx, min(idx + 4, len(st)))]
                for wln, wl in window:
                    if wln != ln and (skip_line(wl) or not gl.on_chain(wl, ga, 'Dwarf')):
                        continue
                    if wln != ln and QT_TAG.search(wl) and not any(n in wl.lower() for n in cnames):
                        break   # the next quest's turn-in: its gear line is not about this quest
                    if not is_gear_line(wl):
                        continue
                    g = [x.strip().lower() for x in GREEN.findall(wl)]
                    gc = [x for x in g if x in cnames]
                    text = plain(wl).lower()
                    first = None
                    pos = [(text.find(n), n) for n in cnames if re.search(r'(?<![a-z0-9])' + re.escape(n) + r'(?![a-z0-9])', text)]
                    if pos:
                        first = min(pos)[1]
                    hm = HEADING.search(wl)
                    after = plain(wl[hm.end():]).strip().lower() if hm else ''
                    if gc:
                        pick, pick_line = cnames[gc[0]]['name'], wln
                    elif re.match(r'(nothing|none)\b', after):
                        pick, pick_line = 'none', wln
                    elif first:
                        pick, pick_line = cnames[first]['name'], wln
                    elif NONE_WORDS.search(text):
                        pick, pick_line = 'none', wln
                    else:
                        continue
                    break

                scored = [r for r in rows if r['u']]
                main_ = [r for r in scored if r['note'] != '1H (shield set only)'] or scored
                reasons = []
                best = max(main_, key=lambda r: r['sc']) if main_ else None
                bestk = max(main_, key=lambda r: r['sk']) if main_ else None
                pr = cnames.get(pick.lower()) if pick not in ('none', 'unstated') else None
                if best:
                    if pr is not None:
                        if pr['sc'] is None:
                            reasons.append('guide pick has no tooltip - not scored')
                        elif pr['name'] != best['name'] and best['sc'] - (pr['sc'] if pr['u'] else 0.0) > 1.0:
                            reasons.append('central best %s beats the pick by %.1f' % (
                                best['name'], best['sc'] - (pr['sc'] if pr['u'] else 0.0)))
                    elif best['sc'] > 2.0:
                        reasons.append('guide names no pick (%s) but %s scores %.1f' % (pick, best['name'], best['sc']))
                    if bestk['name'] != best['name'] and bestk['sk'] > best['sk'] + 1e-9:
                        reasons.append('conservative best %s differs from central best %s' % (bestk['name'], best['name']))
                if reasons and not (len(reasons) == 1 and reasons[0].startswith('guide pick has no tooltip')):
                    flagged.append(dict(fn=fn, ln=ln, qid=qid, qname=w.get('name') or gl.qname(qid), band=band,
                                        rows=rows, pick=pick, pick_line=pick_line,
                                        suggest=best['name'] if best else '-', reasons=reasons))

    # ---------------- report
    today = datetime.date.today().isoformat()
    L = ['# Gear-call check - %s' % today, '',
         'Report only (tooling/gear_calls.py). Dwarf chain of the guide (Hunter and Human lines skipped). Quoted stats on '
         'gear lines compared with today\'s Forever tooltips; quest-reward picks scored with weights/score_items.py '
         '(AP-equivalent; band nearest the chapter\'s starting level; no mace term).', '',
         '- Tooltips (newest file wins per item): ' + '; '.join('%s dated %s - %d items taken' % (
             os.path.relpath(p, gl.BASE).replace('\\', '/'), d, tt_used[p]) for p, d in tt_srcs),
         '- Weights: level-20 central %s; conservative Spi %.1f SP %.1f Exp %.1f; no mace term (spec removed 17 Oct 2026); '
         'other bands take Int/Agi from enh_weights: %s' % (
             ' '.join('%s=%g' % kv for kv in W20_CENTRAL.items()), W20_CONSERVATIVE['spi'], W20_CONSERVATIVE['sp'],
             W20_CONSERVATIVE['exp'], '; '.join('L%d int=%g agi=%g' % (b, bw[b][0]['int'], bw[b][0]['agi']) for b in BANDS if b != 20)),
         '- Reward choices: data/zone_*.json "itemchoices" (Wowhead Forever atlas, as qinfo.py); item names: tooling/qdb/item.json; '
         'gear classes: tooling/client/%s/Item.csv' % cbuild,
         '- Counts: gear lines scanned %d; item names matched %d; stat mismatches %d; quests checked (2+ choices) %d; '
         'quests flagged %d' % (n_gear, n_matched, len(mismatches), quests_checked, len(flagged)), '']

    L += ['## Part 1 - quoted stats that differ from the tooltip', '']
    if mismatches:
        L += ['| chapter | line | item | quoted | tooltip | differs | quoted text |', '|---|---|---|---|---|---|---|']
        for fn, ln, nm, q, t, d, par in mismatches:
            L.append('| %s | %d | %s | %s | %s | %s | %s |' % (fn, ln, ascii(nm), q, t, d, ascii(par)))
    else:
        L.append('(none)')
    if ambiguous:
        L += ['', 'Names shared by several tooltips (compared with every variant; the first is shown):', ''] + ['- ' + a for a in ambiguous]
    if unparsed:
        L += ['', 'Parentheses with stat-like text that did not parse:', ''] + ['- ' + ascii(u) for u in unparsed]
    L.append('')

    L += ['## Part 2 - flagged quest-reward picks', '',
          'Best = best usable choice by central score, 1H weapons excluded unless nothing else is usable. Flagged when the '
          'best beats the guide pick by more than 1.0, when the conservative set picks a different item, or when the guide '
          'names no pick although a choice scores above 2.0. Weapon scores include 14 x dps, so a weapon choice outscoring '
          'armor only says the item is strong for its slot, not that it beats the weapon already worn.', '']
    for f in flagged:
        L += ['### %s line %d - QT%d %s (band L%d)' % (f['fn'], f['ln'], f['qid'], ascii(f['qname']), f['band']), '']
        for r in sorted(f['rows'], key=lambda r: -(r['sc'] if r['sc'] is not None else -1e9)):
            if r['sc'] is None:
                L.append('- %s (%d) - no tooltip' % (ascii(r['name']), r['id']))
            else:
                it = r['it']
                L.append('- %s (%d) - %s %s %s; central %.1f / conservative %.1f; %s' % (
                    ascii(r['name']), r['id'], it['slot'], it['cls'] or '', fmt_item(it), r['sc'], r['sk'],
                    ('usable' + (' - ' + r['note'] if r['note'] else '')) if r['u'] else 'not usable - ' + r['note']))
        L += ['- Guide pick: %s%s' % (ascii(f['pick']), (' (line %d)' % f['pick_line']) if f['pick_line'] else ''),
              '- Suggested pick: %s' % ascii(f['suggest']),
              '- Why flagged: %s' % '; '.join(ascii(x) for x in f['reasons']), '']
    if not flagged:
        L += ['(none)', '']
    if no_data:
        L += ['[QT] quests with no Wowhead atlas row (reward choices unknown): ' + ', '.join(no_data), '']

    L += ['## Part 3 - items with no tooltip', '',
          'Reward-choice item ids (all [QT] quests with 2+ choices) and weapon/armor names on gear lines that the cache '
          'lacks. Fetch with: python tooling\\fetch_tooltips.py --from-file <file with these ids>', '', '```']
    gear_ids = sorted({i for _, ids, _ in missing_names.values() for i in ids})
    allids = sorted(missing_choice_ids | set(gear_ids))
    L += [' '.join(map(str, allids)) if allids else '(none)', '```', '']
    if missing_names:
        L += ['Gear-line names without a tooltip (name - item.json ids - first line):', '']
        for k in sorted(missing_names):
            nm, ids, where = missing_names[k]
            L.append('- %s - %s - %s' % (ascii(nm), ' '.join(map(str, ids)), where))
        L.append('')
    counts = dict(gear_lines=n_gear, items_matched=n_matched, mismatches=len(mismatches), quests_checked=quests_checked,
                  quests_flagged=len(flagged), no_tooltip_ids=len(allids), qt_single_or_no_choice=single)
    return '\n'.join(to_ascii(l) for l in L) + '\n', counts


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--stdout', action='store_true', help='print the report instead of writing it')
    a = ap.parse_args()
    rep, counts = build()
    if a.stdout:
        sys.stdout.write(rep)
    else:
        out = os.path.normpath(os.path.join(gl.BASE, 'Claude outputs', 'gear-calls-%s.md' % datetime.date.today().isoformat()))
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, 'w', encoding='ascii', newline='\n') as f:
            f.write(rep)
        print(out)
    print(' '.join('%s=%d' % kv for kv in counts.items()))


if __name__ == '__main__':
    main()
