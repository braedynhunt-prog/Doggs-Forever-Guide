#!/usr/bin/env python3
r"""Data checks for the Forever Guidelime files (the flow check is check_guide.py; both read guidelib.py).

Modules (python tooling\verify.py [--all] [--module questnpc,tar,gates,xp,money] [--update-baseline] [--chain Dwarf]):
  questnpc  every [QA]/[QT] line's [TAR] is the quest's starter / finisher in tooling/qdb/quest.json
  tar       every [TAR] exists in npc.json with the written name, and the line's [G x,y Zone] is within 3 units of a DB spawn
            (first [TAR] on the line; later ones only need to be within 15, they are "next to" the first)
  gates     skill-gated steps (recipes, trainer ranks, Camping 101) come after the steps that provide the skill
            (tooling/skill_gates.json: providers = learn / cook-to-N / fish-to-N / Journeyman; gates = min skill, mode)
  xp        every "N XP" on a [QA]/[QT] line is that quest's XP, a level-scaled share (80/60/40/20/10%) or the line's sum (data/zone_*.json)
  money     every money quote: [QT] rewards (zone data money), vendor prices (4 x tooltip sell price), trainer prices
            (tooling/trainer_costs.json) and the Gold check lines (running quest money, quoted purchases, 15%)
Lines on the Dwarf Shaman route only (the Human / Hunter lines are unmaintained since 27 Oct 2026).

Findings are "module  file:line  message". tooling/verify_baseline.txt holds the accepted ones (another addon folder named by
FOREVER_GUIDE uses tooling/verify_baseline_<folder>.txt, 1 Nov 2026): the default run prints
only findings that are not in it and exits 1 when there are any; --all prints everything grouped by module;
--update-baseline rewrites the baseline from the current run.
"""
import os, sys, re, json, math, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import guidelib as gl

HERE = os.path.dirname(os.path.abspath(__file__))
BASELINE = gl.baseline_path('verify')   # verify_baseline.txt for the Alliance folder, verify_baseline_<folder>.txt otherwise (1 Nov 2026)
GATES = os.path.join(HERE, 'skill_gates.json')
NEAR, NEAR_SECOND = 3.0, 15.0

def route_lines(chain=gl.DEFAULT_CHAIN):
    """(file, ln, line, band) for every step on the chain, skipping other races' and Hunter-only lines."""
    for f in gl.chain_files(chain):
        txt = gl.read(f); ga = gl.chapter_ga(txt); band = gl.chapter_band(txt)
        for ln, line in gl.steps(txt):
            if not gl.on_chain(line, ga, chain): continue
            m = gl.A_TAG.search(line)
            if m and 'Hunter' in m.group(1) and 'Shaman' not in m.group(1): continue
            yield f, ln, line, band

def fmt_ids(ids, name):
    return ', '.join(f'{i} {name(i) or "?"}' for i in ids)

# ---------------------------------------------------------------- questnpc
def check_questnpc(lines):
    out = []
    for f, ln, line, band in lines:
        tars = gl.tars(line)
        for code, qid, title in gl.quest_tags(line):
            if code not in ('QA', 'QT'): continue
            ends = gl.qends(qid) if code == 'QT' else gl.qstarts(qid)
            what = 'finisher' if code == 'QT' else 'starter'
            if ends is None:
                out.append((f, ln, f'[{code}{qid}] {gl.qname(qid)}: quest not in the Forever DB (not checkable)')); continue
            npcs = ends['npc']; objs = ends['object']; items = ends.get('item', [])
            also = (f'; or object {fmt_ids(objs, gl.object_name)}' if objs else '') + (f'; or item {", ".join(map(str, items))}' if items else '')
            if tars:
                if any(t in npcs for t, _ in tars): continue
                if not npcs and (objs or items):
                    kind = 'object ' + fmt_ids(objs, gl.object_name) if objs else 'item ' + ', '.join(map(str, items))
                    out.append((f, ln, f'[{code}{qid}] {gl.qname(qid)}: {what} in the DB is {kind}; line has [TAR{tars[0][0]} {tars[0][1]}] (fine if the TAR is just the nearby NPC)'))
                elif not npcs:
                    out.append((f, ln, f'[{code}{qid}] {gl.qname(qid)}: DB lists no {what} at all; line has [TAR{tars[0][0]} {tars[0][1]}]'))
                else:
                    out.append((f, ln, f'[{code}{qid}] {gl.qname(qid)}: line has {", ".join(f"[TAR{t} {n}]" for t, n in tars)}; DB {what}: {fmt_ids(npcs, gl.npc_name)}{also}'))
            else:
                if npcs:
                    out.append((f, ln, f'[{code}{qid}] {gl.qname(qid)}: no [TAR] on the line; DB {what}: {fmt_ids(npcs, gl.npc_name)}{also}'))
    return out

# ---------------------------------------------------------------- tar
def check_tar(lines):
    out = []
    for f, ln, line, band in lines:
        tars = gl.tars(line)
        if not tars: continue
        gs = gl.gotos(line)
        for i, (nid, nm) in enumerate(tars):
            dbname = gl.npc_name(nid)
            if dbname is None:
                out.append((f, ln, f'[TAR{nid} {nm}] not in the Forever DB')); continue
            if dbname != nm:
                out.append((f, ln, f'[TAR{nid}] is "{dbname}" in the DB, line says "{nm}"'))
            if not gs: continue
            gx, gy, gz = gs[0]
            if gz not in gl.ZID:
                out.append((f, ln, f'[G{gx},{gy} {gz}]: zone has no map id in guidelib.ZID')); continue
            pts = gl.npc_spawns(nid, gl.ZID[gz])
            if not pts:
                zones = gl.npc_zones(nid)
                where = f'spawns in zones {zones}' if zones else 'no spawn data in the DB at all'
                out.append((f, ln, f'{nm} ({nid}) has no spawn in {gz} ({where})')); continue
            best = min(pts, key=lambda p: math.hypot(p[0] - gx, p[1] - gy))
            d = math.hypot(best[0] - gx, best[1] - gy)
            lim = NEAR if i == 0 else NEAR_SECOND
            if d > lim:
                tag = '' if i == 0 else ' (secondary TAR, 15-unit limit)'
                out.append((f, ln, f'{nm} [G{gx},{gy}] is {d:.1f} from the nearest spawn {best[0]:.1f},{best[1]:.1f}{tag}'))
    return out

# ---------------------------------------------------------------- gates
def check_gates(lines):
    cfg = json.load(open(GATES, encoding='utf-8'))
    state = {s: {'learned': False, 'cap': 0, 'target': 0, 'where': None} for s in cfg['skills']}
    out = []
    for f, ln, line, band in lines:
        # a step is one unit: what it provides (learn, fish-to-N, a rank) counts for the gates on the same line
        for p in cfg['providers']:
            if p['match'] not in line: continue
            st = state[p['skill']]
            if p.get('learn'):
                st['learned'] = True; st['cap'] = max(st['cap'], 75); st['target'] = max(st['target'], 1)
            if p.get('target'):
                st['target'] = max(st['target'], p['target']); st['where'] = f'{os.path.basename(f)}:{ln}'
            if p.get('rank'):
                st['cap'] = max(st['cap'], p['rank'])
        # gates apply to actionable steps only: [OC] lines are notes (plans, gear calls, labels) and may name a recipe
        # or trainer long before the route reaches it. Providers on [OC] lines still count (the targets live in notes).
        for g in (cfg['gates'] if not line.startswith('[OC]') else ()):
            if g['match'] not in line: continue
            st = state[g['skill']]; skill = g['skill']; need = g['min']; mode = g['mode']
            cond = bool(re.search(r'\bif (you|Cooking|Fishing|First Aid|Skinning|Mining)\b', line)) or 'if you' in line
            soft = ' [conditional step]' if cond else ''
            src = '' if 'Classic' not in g['source'] and 'unverified' not in g['source'] else ' [gate value unverified on Forever]'
            if not st['learned']:
                out.append((f, ln, f'{g["match"]} needs {skill} {need} but the route has not learned {skill} yet{soft}{src}')); continue
            if mode in ('rank', 'target') and st['cap'] < need:
                out.append((f, ln, f'{g["match"]} needs {skill} {need}; the last rank on the route caps {skill} at {st["cap"]}{soft}{src}'))
            if mode == 'target' and st['target'] < need:
                w = f' (last target: {skill} {st["target"]} at {st["where"]})' if st['where'] else f' (no {skill} target stated yet)'
                out.append((f, ln, f'{g["match"]} needs {skill} {need}; the route has only asked for {skill} {st["target"]} so far{w}{soft}{src}'))
            if g.get('level') and band[1] < g['level']:
                out.append((f, ln, f'{g["match"]} needs level {g["level"]}; the chapter tops out at {band[1]}{soft}{src}'))
    return out

# ---------------------------------------------------------------- xp
# Quest XP from the Wowhead zone files (data/zone_*.json); data/quests.json (gl.atlas) is the September atlas and is not
# refreshed, so it is not used here. A row from a browser-refreshed zone (file-level "_browser_refresh") wins.
_XP = None
XP_NUM = r'(?:\d{1,2},\d{3}|\d{2,5})'
XP_SUM = re.compile(r'(?<![\d,])(' + XP_NUM + r'(?:\s*\+\s*' + XP_NUM + r')+)\s*XP')
XP_ONE = re.compile(r'(?<![\d,])(' + XP_NUM + r')\s*XP')
XP_SKIP = ('chain', 'in all', 'pair', 'total', 'more', 'about')
XP_SCALE = (0.8, 0.6, 0.4, 0.2, 0.1)

def quest_xp():
    """{quest id: (xp, name)} from data/zone_*.json; browser-refreshed zones win over zones that were not refreshed."""
    global _XP
    if _XP is None:
        import glob
        _XP, fresh = {}, {}
        for p in sorted(glob.glob(os.path.join(gl.BASE, 'data', 'zone_*.json'))):
            d = json.load(open(p, encoding='utf-8')); fr = bool(d.get('_browser_refresh'))
            for q in d.get('quests', []):
                if q.get('xp') is None: continue
                if q['id'] in _XP and fresh[q['id']] and not fr: continue
                _XP[q['id']] = (q['xp'], q.get('name')); fresh[q['id']] = fr
    return _XP

def _xp_clause(line, start, end):
    """The text between the parentheses enclosing [start, end), or the ~60 chars around it."""
    o = line.rfind('(', 0, start); c = line.find(')', end)
    if o != -1 and ')' not in line[o:start] and c != -1 and '(' not in line[end:c]:
        return line[o + 1:c]
    return line[max(0, start - 60):end + 60]

def check_xp(lines):
    xp = quest_xp(); out = []
    for f, ln, line, band in lines:
        ids = []
        for code, qid, title in gl.quest_tags(line):
            if code in ('QA', 'QT') and qid not in ids: ids.append(qid)
        if not ids: continue
        toks = []   # (text, value)
        taken = []
        for m in XP_SUM.finditer(line):
            taken.append(m.span())
            clause = _xp_clause(line, m.start(), m.end())
            if any(w in clause for w in XP_SKIP): continue
            for n in re.findall(XP_NUM, m.group(1)): toks.append((n, int(n.replace(',', ''))))
        for m in XP_ONE.finditer(line):
            if any(a <= m.start() < b for a, b in taken): continue
            clause = _xp_clause(line, m.start(), m.end())
            if any(w in clause for w in XP_SKIP) or '+' in clause: continue
            toks.append((m.group(1), int(m.group(1).replace(',', ''))))
        if not toks: continue
        known = [i for i in ids if i in xp]; missing = [i for i in ids if i not in xp]
        def ok(v):
            for i in known:
                x = xp[i][0]
                if v == x or any(abs(v - round(x * k)) <= 5 for k in XP_SCALE): return True
            return bool(known) and v == sum(xp[i][0] for i in known)
        for text, v in toks:
            if ok(v): continue
            if missing:
                if 'not listed' in line or 'not in the DB' in line: continue
                for i in missing:
                    out.append((f, ln, f'"{text} XP" quoted but {i} {gl.qname(i) or "?"} has no XP in data/zone_*.json'))
                continue
            listing = ', '.join(f'{i} {xp[i][1]} = {xp[i][0]:,}' for i in known)
            out.append((f, ln, f'"{text} XP" matches no quest on the line ({listing})'))
    return out

# ---------------------------------------------------------------- money
# Money quotes (5 Nov 2026). Four sub-checks, each finding prefixed with its name:
#   quest      a reward quote on a [QT] line is one quest's money (data/zone_*.json "money", copper) or the line's sum
#   vendor     "<Item> (<price>[ each][, <total>])" on [V] / "buy" lines: buy price = 4 x the newest weights/tooltips
#              sell price, +0..+3 copper; a quoted total = units x unit price
#   trainer    prices on [T] lines against tooling/trainer_costs.json (pulled per NPC; absent = one finding per line)
#   goldcheck  "Gold check" / "quest money so far" lines: running [QT] money on the route, and the quoted purchases
#              (vendor and trainer prices as the guide quotes them, from chapter 02 on) within MONEY_TOL
TRAINER_COSTS = os.path.join(HERE, 'trainer_costs.json')
TOOLTIPS_DIR = os.path.join(gl.BASE, 'weights', 'tooltips')
MONEY_TOL = 0.15
MONEY_UNIT = {'g': 10000, 's': 100, 'c': 1, 'gold': 10000, 'silver': 100, 'copper': 1}
_MPART = r'\d+(?:[gsc](?![A-Za-z])|\s+(?:gold|silver|copper)\b)'
MONEY_TOKEN = re.compile(r'(?<![\w.,\-])(?:(\d+)-)?(' + _MPART + r'(?:\s+' + _MPART + r')*)')
MONEY_LIST = re.compile(r'(?<![\w.,])(\d+)((?:\s*(?:,|\band\b|\bor\b)\s*\d+)+)\s+(gold|silver|copper)\b')
COLOUR = re.compile(r'\|c[0-9a-fA-F]{8}|\|r')
QUEST_MONEY_SKIP = re.compile(r'\bbuy\b|\[V\]|\[T\]|\beach\b|\bcosts\b|\bsheet\b|Gold check|\bper\b|\bfor the\b|\bsell\b|\bvendor\b', re.I)
NAME_WORD = re.compile(r"[A-Z][\w'\-]*:?$")
NAME_JOIN = ('and', 'of', 'the', '-')
SPELL_FILLER = re.compile(r'\b(?:are musts|is a must|musts|a buy|buys|are|then|from \d+)\b')
LEARN_RANK = re.compile(r'\blearn (?:Apprentice|Journeyman|Expert|Artisan) [A-Z]\w*(?: [A-Z]\w*)? \(')
LINE_TOTAL = re.compile(r'\b(?:whole page|for the lot|in all|all in)\b')
OPTIONAL_SEG = 'when gold is easy'
_QMONEY = None

def money_fmt(c):
    """Copper -> '1g 2s 30c', zero units dropped."""
    if not c: return '0c'
    g, r = divmod(c, 10000); s, cc = divmod(r, 100)
    return ' '.join(f'{v}{u}' for v, u in ((g, 'g'), (s, 's'), (cc, 'c')) if v)

def money_parts(text):
    """'1g 80s' / '10 silver' -> copper (the unit parts of one token)."""
    return sum(int(n) * MONEY_UNIT[u] for n, u in re.findall(r'(\d+)\s*(gold|silver|copper|[gsc])', text))

def money_tokens(line):
    """[(start, end, text, lo, hi, listed)] for every money amount on a line, positions in the line. A range '65-85s'
    gives lo < hi; 'N and M silver' gives one token per number, listed = the numbers of that list in order."""
    s = COLOUR.sub(lambda m: ' ' * len(m.group()), line)
    out = []; taken = []
    for m in MONEY_LIST.finditer(s):
        nums = [m.group(1)] + re.findall(r'\d+', m.group(2)); u = MONEY_UNIT[m.group(3)]
        vals = [int(n) * u for n in nums]
        for v in vals: out.append((m.start(), m.end(), s[m.start():m.end()], v, v, vals))
        taken.append(m.span())
    for m in MONEY_TOKEN.finditer(s):
        if any(a <= m.start() < b for a, b in taken): continue
        hi = money_parts(m.group(2))
        if m.group(1):
            first = re.match(r'\d+\s*(gold|silver|copper|[gsc])', m.group(2)).group(1)
            lo = int(m.group(1)) * MONEY_UNIT[first]
        else:
            lo = hi
        out.append((m.start(), m.end(), s[m.start():m.end()], lo, hi, None))
    return sorted(out, key=lambda t: t[0]), s

def quest_money():
    """{quest id: (copper, name)} for quests with money > 0 in data/zone_*.json; browser-refreshed zones win."""
    global _QMONEY
    if _QMONEY is None:
        import glob
        allq, fresh = {}, {}
        for p in sorted(glob.glob(os.path.join(gl.BASE, 'data', 'zone_*.json'))):
            d = json.load(open(p, encoding='utf-8')); fr = bool(d.get('_browser_refresh'))
            for q in d.get('quests', []):
                if q['id'] in allq and fresh[q['id']] and not fr: continue
                allq[q['id']] = (q.get('money') or 0, q.get('name')); fresh[q['id']] = fr
        _QMONEY = {k: v for k, v in allq.items() if v[0] > 0}
    return _QMONEY

def _qt_ids(line):
    ids = []
    for code, qid, title in gl.quest_tags(line):
        if code == 'QT' and qid not in ids: ids.append(qid)
    return ids

def check_money_quest(lines):
    qm = quest_money(); out = []
    for f, ln, line, band in lines:
        ids = _qt_ids(line)
        if not ids: continue
        toks, s = money_tokens(line)
        known = [i for i in ids if i in qm]; missing = [i for i in ids if i not in qm]
        done_lists = []
        for a, b, text, lo, hi, listed in toks:
            clause = _xp_clause(s, a, b)
            if QUEST_MONEY_SKIP.search(clause) or 'quest money' in clause: continue
            if listed is not None:
                if (a, b) in done_lists: continue
                done_lists.append((a, b))
                if len(listed) == len(ids):
                    # "391 and 387 pay 25 and 40 silver": the amounts pair with the [QT] ids in order
                    for i, v in zip(ids, listed):
                        if i not in qm:
                            out.append((f, ln, f'quest: "{money_fmt(v)}" quoted but {i} {gl.qname(i) or "?"} has no money in data/zone_*.json'))
                        elif qm[i][0] != v:
                            out.append((f, ln, f'quest: "{money_fmt(v)}" paired with {i} {qm[i][1]}, which pays {money_fmt(qm[i][0])}'))
                    continue
                vals = listed
            else:
                vals = [lo]
            for v in vals:
                if any(qm[i][0] == v for i in known) or (known and v == sum(qm[i][0] for i in known)): continue
                shown = money_fmt(v) if listed is not None else text
                if missing:
                    for i in missing:
                        out.append((f, ln, f'quest: "{shown}" quoted but {i} {gl.qname(i) or "?"} has no money in data/zone_*.json'))
                    continue
                listing = ', '.join(f'{i} {qm[i][1]} = {money_fmt(qm[i][0])}' for i in known)
                out.append((f, ln, f'quest: "{shown}" matches no quest on the line ({listing})'))
    return out

# vendor prices: the newest weights/tooltips/*.json, first "Sell Price:" in the tooltip (a recipe's tooltip also
# carries the taught item's sell price after it). A unit-less sell price ("Sell Price: 25", older pulls) is unknown.
_TT = None; _ITEMS = None
def tooltips():
    global _TT
    if _TT is None:
        import glob
        ps = sorted(glob.glob(os.path.join(TOOLTIPS_DIR, '*.json')))
        raw = json.load(open(ps[-1], encoding='utf-8')) if ps else {}
        _TT = {k.lower(): v for k, v in raw.items()}
    return _TT

def item_by_name():
    """{lower-case name: [(id, vendors)]} from tooling/qdb/item.json (row 0 name, row 13 vendors)."""
    global _ITEMS
    if _ITEMS is None:
        _ITEMS = {}
        for k, v in gl.db('item').items():
            if v and v[0]: _ITEMS.setdefault(v[0].lower(), []).append((k, v[13] if len(v) > 13 else None))
    return _ITEMS

def sell_price(name):
    """('ok', copper) / ('nocache', None) / ('nounit', text) / ('none', None) for an item's tooltip sell price."""
    t = tooltips().get(name.lower())
    if t is None: return 'nocache', None
    m = re.search(r'Sell Price:\s*([^|]*)', t.get('tooltip', ''))
    if not m: return 'none', None
    txt = m.group(1).strip()
    pm = re.match(r'((?:\d+[gsc]\s*)+)(?![\w])', txt)
    if not pm: return 'nounit', txt
    return 'ok', money_parts(pm.group(1))

def _name_before(s, p):
    """The item name (run of capitalised words, 'and'/'of'/'the'/'-' inside) ending at s[:p], and a leading count."""
    words = s[:p].replace('(', ' ( ').split()
    run = []
    while words:
        w = words[-1]
        if NAME_WORD.match(w) or (run and w in NAME_JOIN): run.insert(0, words.pop())
        else: break
    while run and run[0] in NAME_JOIN: words.append(run.pop(0))
    while run and run[-1] in NAME_JOIN: run.pop()
    n, counted = 1, False
    if run and words and re.fullmatch(r'\d+', words[-1]): n, counted = int(words[-1]), True
    return ' '.join(run), n, counted

def vendor_items(line):
    """[(name, units, unit price, total or None, token text, form)] for the priced items on a [V] / 'buy' line.
    form 'paren' = '<Item> (<price>...)', 'bare' = '<Item> <price>' (kept only when the name is a DB item)."""
    toks, s = money_tokens(line)
    out = []; used = set()
    for i, (a, b, text, lo, hi, listed) in enumerate(toks):
        if i in used or listed is not None or lo != hi: continue
        before = s[:a]
        pm = re.search(r'\(\s*$', before)
        if pm:
            name, n, counted = _name_before(s, pm.start()); form = 'paren'
        else:
            name, n, counted = _name_before(s, a); form = 'bare'
            if not name or name.lower() not in item_by_name(): continue
        if not name: continue
        rest = s[b:]
        each = bool(re.match(r'\s+each\b', rest))
        total = None
        tm = re.match(r'(\s+each)?\s*,\s*$', s[b:toks[i + 1][0]]) if i + 1 < len(toks) else None
        if tm and form == 'paren':
            nb = toks[i + 1]
            after = s[nb[1]:]
            if re.match(r'(\s+total)?\s*[\);]', after):
                total = nb[3]; used.add(i + 1)
        unit = lo if (each or n == 1) else None
        out.append((name, n, unit, total if total is not None else (None if each or n == 1 else lo), text, form))
    return out

def check_money_vendor(lines):
    out = []
    for f, ln, line, band in lines:
        if '[T]' in line or 'Gold check' in line: continue
        if '[V]' not in line and not re.search(r'\bbuy\b', line): continue
        for name, n, unit, total, text, form in vendor_items(line):
            ent = item_by_name().get(name.lower())
            sold = [e for e in (ent or []) if e[1]]
            if not sold:
                why = '' if not ent else f' (item {ent[0][0]} has no vendors in the DB)'
                out.append((f, ln, f'vendor: no vendor item named "{name}" in tooling/qdb/item.json{why}')); continue
            st, sp = sell_price(name)
            if st == 'nocache':
                out.append((f, ln, f'vendor: no tooltip cached for {name}')); continue
            if st == 'nounit':
                out.append((f, ln, f'vendor: tooltip sell price for {name} has no units ("Sell Price: {sp}"), "{text}" unchecked')); continue
            if st == 'none':
                out.append((f, ln, f'vendor: tooltip for {name} has no sell price, "{text}" unchecked')); continue
            lo, hi = 4 * sp, 4 * sp + 3
            if unit is not None:
                if not lo <= unit <= hi:
                    out.append((f, ln, f'vendor: "{text}" for {name}: tooltip sell price {money_fmt(sp)} gives {money_fmt(lo)} - {money_fmt(hi)}'))
                if total is not None and total != unit * n:
                    out.append((f, ln, f'vendor: total for {n} {name} is quoted {money_fmt(total)} but {n} x {money_fmt(unit)} = {money_fmt(unit * n)}'))
            elif total is not None and not n * lo <= total <= n * hi:
                out.append((f, ln, f'vendor: "{text}" for {n} {name}: tooltip sell price {money_fmt(sp)} gives {money_fmt(n * lo)} - {money_fmt(n * hi)} for {n}'))
    return out

# trainer prices
_TC = None
def trainer_costs():
    global _TC
    if _TC is None:
        _TC = json.load(open(TRAINER_COSTS, encoding='utf-8')) if os.path.exists(TRAINER_COSTS) else False
    return _TC

def _paren_groups(s):
    """[(start, end)] of the top-level parenthesised groups of s (inside the parentheses)."""
    out = []; depth = 0; st = None
    for i, ch in enumerate(s):
        if ch == '(':
            if depth == 0: st = i + 1
            depth += 1
        elif ch == ')' and depth:
            depth -= 1
            if depth == 0: out.append((st, i))
    return out

def _spell_run(text):
    """'Fire Nova, Purge, Healing Wave 3 - ' -> [('Fire Nova', None, 'Fire Nova'), ..., ('Healing Wave', 3, 'Healing Wave 3')]."""
    t = SPELL_FILLER.sub(' ', text).replace(':', ': ').rstrip(' ,-')
    words = t.split(); run = []
    while words:
        w = words[-1]; core = w.rstrip(',')
        if NAME_WORD.match(core) and not core.endswith(':') or re.fullmatch(r'\d+', core) or core in ('and', 'or', 'of', 'the') or w == ',':
            run.insert(0, words.pop())
        else: break
    while run and run[0].rstrip(',') in ('and', 'or', 'of', 'the') or (run and re.fullmatch(r'\d+,?', run[0])): run.pop(0)
    out = []
    for part in re.split(r',|\band\b|\bor\b', ' '.join(run)):
        part = part.strip()
        if not part: continue
        m = re.match(r'(.*?)\s+(\d+)$', part)
        out.append((m.group(1), int(m.group(2)), part) if m else (part, None, part))
    return out

def trainer_groups(line):
    """Parse the prices on a trainer line. Returns (groups, line_totals, unparsed, ntokens):
    group = {'spells': [(name, rank, raw)], 'each': copper|None, 'price': copper|None (one spell), 'total': copper|None,
    'text': token text, 'optional': bool}; line_totals = [(copper, text)]; unparsed = [clause]."""
    toks, s = money_tokens(line)
    toks = [t for t in toks if not re.match(r'\s+of quest money', s[t[1]:])]
    groups, line_totals, unparsed = [], [], []
    pg = _paren_groups(s)
    seen = set()
    for ga, gb in pg:
        inner = [t for t in toks if ga <= t[0] < gb]
        if not inner: continue
        seen.update(t[0] for t in inner)
        clause = s[ga:gb]
        # top-level ';' segments of the clause (inner parentheses are blanked)
        flat = ''.join(' ' if ch in '()' else ch for ch in clause)
        depth = 0; flat2 = list(flat)
        for i, ch in enumerate(clause):
            if ch == '(': depth += 1
            elif ch == ')': depth -= 1
            elif ch == ';' and depth > 0: flat2[i] = ','
        flat = ''.join(flat2)
        pos = 0; first_seg = True
        for seg in flat.split(';'):
            sa = ga + pos; pos += len(seg) + 1
            st = [t for t in inner if sa <= t[0] < sa + len(seg)]
            if not st: first_seg = False; continue
            optional = OPTIONAL_SEG in seg
            prev_end = sa; last_group = None
            for a, b, text, lo, hi, listed in st:
                if lo != hi or listed is not None:
                    unparsed.append(clause); break
                after = s[b:sa + len(seg)]
                before_txt = s[prev_end:a]
                before_txt = ''.join(' ' if ch in '()' else ch for ch in before_txt)
                each = bool(re.match(r'\s+each\b', after))
                if LINE_TOTAL.search(before_txt) or LINE_TOTAL.search(after[:20]):
                    line_totals.append((lo, text)); prev_end = b; continue
                spells = _spell_run(before_txt)
                if not spells and first_seg and prev_end == sa:
                    # "(70 silver each)" / "(10 silver)": the spells stand before the parenthesis on the line
                    lead = s[:ga - 1]; cut = max(lead.rfind(')'), lead.rfind(']'), lead.rfind(':'))
                    spells = _spell_run(lead[cut + 1:])
                if not spells:
                    if last_group is not None and last_group['each'] is not None and last_group['total'] is None and not each:
                        last_group['total'] = lo; prev_end = b; continue
                    unparsed.append(clause); break
                g = {'spells': spells, 'each': lo if each else None, 'price': None if each else lo, 'total': None,
                     'text': text + (' each' if each else ''), 'optional': optional}
                if not each and len(spells) > 1:
                    unparsed.append(clause); break
                groups.append(g); last_group = g; prev_end = b
            first_seg = False
    for t in toks:
        if t[0] not in seen:
            unparsed.append(s[max(0, t[0] - 60):t[1] + 60].strip())
    return groups, line_totals, list(dict.fromkeys(unparsed)), len(toks)

def _trainer_lines(lines):
    for f, ln, line, band in lines:
        if 'Gold check' in line: continue
        if '[T]' in line or LEARN_RANK.search(line): yield f, ln, line, band

def _find_spell(entry, name, rank):
    sp = entry.get('spells', []); nl = name.lower()
    names = {x['name'] for x in sp if x['name'].lower() == nl}
    if not names:
        names = {x['name'] for x in sp if x['name'].lower().startswith(nl + ' ')}
    if len(names) != 1: return None
    nm = names.pop()
    for x in sp:
        if x['name'] == nm and (x.get('rank') == rank or (rank is None and x.get('rank') in (1, None))): return x
    return None

def check_money_trainer(lines):
    out = []; tc = trainer_costs()
    for f, ln, line, band in _trainer_lines(lines):
        groups, totals, unparsed, ntok = trainer_groups(line)
        if not ntok: continue
        if tc is False:
            out.append((f, ln, f'trainer: no tooling/trainer_costs.json yet ({ntok} prices on the line unchecked)')); continue
        for u in unparsed:
            out.append((f, ln, f'trainer: could not parse the trainer prices on this line: {u.strip()}'))
        tars = gl.tars(line)
        if not tars:
            out.append((f, ln, 'trainer: priced trainer line has no [TAR]')); continue
        nid, nm = tars[0]; entry = tc.get(str(nid))
        if entry is None:
            out.append((f, ln, f'trainer: {nm} ({nid}) is not in tooling/trainer_costs.json')); continue
        tname = entry.get('name') or nm
        line_sum = 0; line_ok = True
        for g in groups:
            costs = []
            for name, rank, raw in g['spells']:
                x = _find_spell(entry, name, rank)
                if x is None or x.get('cost') is None:
                    out.append((f, ln, f'trainer: spell "{raw}" not taught by {tname}')); costs.append(None); continue
                costs.append(x['cost'])
                if g['each'] is not None and x['cost'] != g['each']:
                    out.append((f, ln, f'trainer: "{g["text"]}" but {raw} costs {money_fmt(x["cost"])}'))
                if g['price'] is not None and x['cost'] != g['price']:
                    out.append((f, ln, f'trainer: "{g["text"]}" but {raw} costs {money_fmt(x["cost"])}'))
            if None in costs: line_ok = False; continue
            if g['total'] is not None and g['total'] != sum(costs):
                out.append((f, ln, f'trainer: "{money_fmt(g["total"])}" total but {", ".join(r for _, _, r in g["spells"])} sum to {money_fmt(sum(costs))}'))
            if not g['optional']: line_sum += sum(costs)
        for v, text in totals:
            if line_ok and v != line_sum:
                names = ', '.join(r for g in groups if not g['optional'] for _, _, r in g['spells'])
                out.append((f, ln, f'trainer: "{text}" total but {names} sum to {money_fmt(line_sum)}'))
    return out

def _quoted_purchases(f, line):
    """What the guide says a [V] / [T] line costs, from its own quoted prices (optional segments left out)."""
    tot = 0
    if '[T]' in line or LEARN_RANK.search(line):
        groups, totals, unparsed, ntok = trainer_groups(line)
        for g in groups:
            if g['optional']: continue
            tot += g['total'] if g['total'] is not None else (g['each'] * len(g['spells']) if g['each'] is not None else g['price'])
    elif '[V]' in line or re.search(r'\bbuy\b', line):
        for name, n, unit, total, text, form in vendor_items(line):
            tot += total if total is not None else unit * n
    return tot

def _in_tol(v, quoted):
    return abs(v - quoted) <= MONEY_TOL * quoted

def check_money_goldcheck(lines):
    qm = quest_money(); out = []
    done = set(); running = 0; bought = 0; started = False
    for f, ln, line, band in lines:
        if os.path.basename(f).startswith('02_'): started = True
        if 'Gold check' in line or 'quest money so far' in line or 'quest money by now' in line:
            toks, s = money_tokens(line)
            qtok = ptok = None
            for t in toks:
                if re.search(r'quest money\b[^.;,()]{0,20}$', s[:t[0]]) and qtok is None: qtok = t
                elif re.match(r'\s+of quest money', s[t[1]:]) and qtok is None: qtok = t
                elif re.search(r'\b(?:took|costs?)\s+(?:about\s+)?$', s[:t[0]]) and ptok is None: ptok = t
            if qtok:
                a, b, text, lo, hi, _ = qtok
                ok = lo <= running <= hi if lo != hi else _in_tol(running, lo)
                if not ok:
                    out.append((f, ln, f'goldcheck: Gold check: quest money through here is {money_fmt(running)}, line says "{text}"'))
            if ptok:
                a, b, text, lo, hi, _ = ptok
                if re.search(r'list below', s[:a][-40:]):
                    # "The list below costs about 85s": the line itemises the list itself
                    e1 = s.find('.', b); e2 = s.find('. ', e1 + 1) if e1 != -1 else -1
                    e2 = len(s) if e2 == -1 else e2
                    spend = sum(t[3] for t in toks if e1 < t[0] < e2 and t is not qtok)
                    where = 'the prices listed on the line sum to'
                else:
                    spend = bought; where = 'quoted [V]/[T] purchases from chapter 02 to here are'
                if not _in_tol(spend, lo):
                    out.append((f, ln, f'goldcheck: Gold check: {where} {money_fmt(spend)}, line says "{text}"'))
        if started:
            bought += _quoted_purchases(f, line)
        for qid in _qt_ids(line):
            if qid in done: continue
            done.add(qid); running += qm.get(qid, (0,))[0]
    return out

def check_money(lines):
    return check_money_quest(lines) + check_money_vendor(lines) + check_money_trainer(lines) + check_money_goldcheck(lines)

MODULES = {'questnpc': check_questnpc, 'tar': check_tar, 'gates': check_gates, 'xp': check_xp, 'money': check_money}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--all', action='store_true', help='print every finding grouped by module, not just the new ones')
    ap.add_argument('--module', default=','.join(MODULES), help='comma list of modules to run')
    ap.add_argument('--update-baseline', action='store_true', help='write the current findings as the accepted baseline')
    ap.add_argument('--chain', default=gl.DEFAULT_CHAIN, help='race chain (default Dwarf; a variant folder: its chain)')
    a = ap.parse_args()
    lines = list(route_lines(a.chain))
    findings = []   # (module, file, ln, msg)
    for mod in a.module.split(','):
        for f, ln, msg in MODULES[mod](lines):
            findings.append((mod, os.path.basename(f), ln, msg))
    keys = [f'{m}  {f}:{ln}  {msg}' for m, f, ln, msg in findings]
    if a.update_baseline:
        open(BASELINE, 'w', encoding='utf-8', newline='\n').write('\n'.join(keys) + ('\n' if keys else ''))
        print(f'baseline written: {len(keys)} findings -> {os.path.relpath(BASELINE)}'); return 0
    base = set(open(BASELINE, encoding='utf-8').read().splitlines()) if os.path.exists(BASELINE) else set()
    if a.all:
        for mod in a.module.split(','):
            rows = [k for k, (m, *_rest) in zip(keys, findings) if m == mod]
            print(f'== {mod}: {len(rows)} ==')
            for k in rows: print(('    ' if k in base else 'NEW ') + k)
        print(f'\n{len(lines)} route lines; {len(keys)} findings, {sum(k not in base for k in keys)} not in the baseline')
        return 0
    new = [k for k in keys if k not in base]
    gone = [k for k in base if k not in set(keys)]
    for k in new: print('NEW ' + k)
    print(f'{len(keys)} findings ({len(new)} new, {len(gone)} baseline lines no longer produced)')
    return 1 if new else 0

if __name__ == '__main__':
    sys.exit(main())
