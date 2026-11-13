#!/usr/bin/env python3
r"""Route XP table: quest XP, quest money and predicted level per chapter, from a plain list of quest ids.

    python tooling\route_xp.py <route file> [--share 0.65] [--start 42.0]
    python tooling\route_xp.py --table            print the XP-per-level table and the bracket sums

RULES.md rule 14: the XP budget of a plan is computed from the same list the plan text prints. The route
file is that list. Layout (plain text, '#' starts a comment):

    start 42.0                      level on entry to the first chapter (or --start)
    share 0.65                      quest XP as a share of all XP earned (or --share)
    == 42 Riverglades III | wants 42
    94881 95064, 96015              required quests, counted
    opt: 94925 95121                optional quests: listed and summed apart, never counted
    == 43 Krol'dok Stronghold | wants 43
    ...

Quest XP is scaled for quests 6 or more levels under the chapter's entry level (80 / 60 / 40 / 20 / 10%).
Per chapter it prints the counted quests, their XP and money (data\zone_*.json, the Wowhead Forever pull),
the level on entry and on exit (all XP = quest XP / share), the highest required level among the chapter's
quests, and a flag when that level is above the predicted level on entry. It also flags: an id with no XP
row, an id listed twice in the file, an id that chapters already written hand in ([QT<id>] in the addon folder).

XP_TO_LEVEL is the pre-2.3 table of https://warcraft.wiki.gg/wiki/Experience_to_level ("This table shows the
experience needed to advance, by level, before Patch 2.3.0"), read in a browser on 12 Nov 2026 (the page
blocks shell fetches). XP_TO_LEVEL[n] = XP needed to go from level n to n + 1. Bracket sums: 30-40 655,400;
40-50 1,151,700; 50-60 1,778,600; 1-60 4,084,700. wowforeverleveling.com (from the game files) agreed on
11 Nov 2026. The shorter table in tugs_diff.py is the later (2.3) one and is not used here.
"""
import sys, os, re, json, glob, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import guidelib as gl

_ROWS = """1:400 2:900 3:1400 4:2100 5:2800 6:3600 7:4500 8:5400 9:6500 10:7600 11:8800 12:10100 13:11400 14:12900
15:14400 16:16000 17:17700 18:19400 19:21300 20:23200 21:25200 22:27300 23:29400 24:31700 25:34000 26:36400 27:38900
28:41400 29:44300 30:47400 31:50800 32:54500 33:58600 34:62800 35:67100 36:71600 37:76100 38:80800 39:85700 40:90700
41:95800 42:101000 43:106300 44:111800 45:117500 46:123200 47:129100 48:135100 49:141200 50:147500 51:153900
52:160400 53:167100 54:173900 55:180800 56:187900 57:195000 58:202300 59:209800"""
XP_TO_LEVEL = {int(a): int(b) for a, b in (p.split(':') for p in _ROWS.split())}


def bracket(a, b):
    """XP needed to go from level a to level b (whole levels)."""
    return sum(XP_TO_LEVEL[l] for l in range(a, b))


def add_xp(level, xp):
    """Level (with a fraction) after earning xp from a fractional level."""
    while level < 60:
        l = int(level); need = XP_TO_LEVEL[l]
        left = (1 - (level - l)) * need
        if xp < left: return level + xp / need
        xp -= left; level = float(l + 1)
    return 60.0


def scale(player, quest):
    """Share of a quest's XP paid at a player level: full to 5 levels over the quest, then 80 / 60 / 40 / 20 / 10%
    (the same steps verify.py's xp check accepts). The table uses the chapter's entry level for every quest in it."""
    d = player - quest
    return 1.0 if d <= 5 or not quest else {6: 0.8, 7: 0.6, 8: 0.4, 9: 0.2}.get(d, 0.1)


def load_quests():
    """{id: row} from data/zone_*.json; a browser-refreshed row wins over an older one."""
    rows = {}
    for fn in sorted(glob.glob(os.path.join(gl.BASE, 'data', 'zone_*.json'))):
        for q in json.load(open(fn, encoding='utf-8')).get('quests', []):
            old = rows.get(q['id'])
            if old is None or (q.get('_browser') or '') > (old.get('_browser') or ''): rows[q['id']] = q
    return rows


def handed_in():
    """{quest id: chapter file} for every [QT<id>] already in the addon folder."""
    out = {}
    for fn in sorted(glob.glob(os.path.join(gl.ADDON, '*.lua'))):
        for m in re.finditer(r'\[QT(\d+)', open(fn, encoding='utf-8').read()):
            out.setdefault(int(m.group(1)), os.path.basename(fn))
    return out


def parse(path):
    start, share, chapters = None, None, []
    for raw in open(path, encoding='utf-8').read().splitlines():
        line = raw.split('#', 1)[0].strip()
        if not line: continue
        m = re.fullmatch(r'start\s+([\d.]+)', line)
        if m: start = float(m.group(1)); continue
        m = re.fullmatch(r'share\s+([\d.]+)', line)
        if m: share = float(m.group(1)); continue
        if line.startswith('=='):
            title, _, rest = line[2:].partition('|')
            w = re.search(r'wants\s+(\d+)', rest)
            chapters.append({'title': title.strip(), 'wants': int(w.group(1)) if w else None, 'req': [], 'opt': []})
            continue
        if not chapters: raise SystemExit(f'{path}: quest ids before the first "== chapter" line: {raw}')
        key = 'req'
        if line.lower().startswith('opt:'): key, line = 'opt', line[4:]
        chapters[-1][key] += [int(x) for x in re.findall(r'\d+', line)]
    return start, share, chapters


def money(c):
    g, rest = divmod(c, 10000); s, cc = divmod(rest, 100)
    return (f'{g}g ' if g else '') + f'{s:02d}s' + (f' {cc:02d}c' if cc else '')


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('route', nargs='?')
    ap.add_argument('--share', type=float)
    ap.add_argument('--start', type=float)
    ap.add_argument('--table', action='store_true')
    a = ap.parse_args()
    if a.table or not a.route:
        for l in sorted(XP_TO_LEVEL): print(f'{l:2d} -> {l + 1:2d}  {XP_TO_LEVEL[l]:>9,}')
        for x, y in ((1, 30), (30, 40), (40, 50), (50, 60), (1, 60)): print(f'{x}-{y}: {bracket(x, y):,}')
        return 0
    start, share, chapters = parse(a.route)
    start = a.start or start; share = a.share or share or 0.65
    if start is None: raise SystemExit('no start level: give "start N" in the route file or --start N')
    Q = load_quests(); done = handed_in()
    seen, problems = {}, []
    level, cum, cum_money, cum_opt = start, 0, 0, 0
    print(f'quest share {share:.2f}; start level {start:.1f}')
    print(f"{'chapter':46} {'n':>3} {'quest XP':>9} {'money':>9} {'cum XP':>9} {'in':>5} {'out':>5} {'max req':>7} {'opt XP':>8}")
    for ch in chapters:
        for qid in ch['req'] + ch['opt']:
            if qid in seen: problems.append(f"{qid} is listed in '{seen[qid]}' and again in '{ch['title']}'")
            seen.setdefault(qid, ch['title'])
            if qid not in Q: problems.append(f"{qid} ({ch['title']}): no row in data/zone_*.json")
            elif not Q[qid].get('xp'): problems.append(f"{qid} {Q[qid].get('name')} ({ch['title']}): no XP on Wowhead")
            if qid in done: problems.append(f"{qid} ({ch['title']}): already handed in in {done[qid]}")
        raw = sum((Q.get(q, {}).get('xp') or 0) for q in ch['req'])
        xp = sum(round((Q.get(q, {}).get('xp') or 0) * scale(int(level), Q.get(q, {}).get('level') or 0)) for q in ch['req'])
        low = [q for q in ch['req'] if scale(int(level), Q.get(q, {}).get('level') or 0) < 1]
        mon = sum((Q.get(q, {}).get('money') or 0) for q in ch['req'])
        oxp = sum((Q.get(q, {}).get('xp') or 0) for q in ch['opt'])
        reqs = [(Q.get(q, {}).get('reqlevel') or 0) for q in ch['req']]
        maxreq = max(reqs) if reqs else 0
        entry = level
        level = add_xp(level, xp / share); cum += xp; cum_money += mon; cum_opt += oxp
        wants = ch['wants'] if ch['wants'] is not None else maxreq
        flag = ''
        if maxreq and int(entry) < maxreq:
            late = [q for q in ch['req'] if (Q.get(q, {}).get('reqlevel') or 0) > int(entry)]
            flag = f'  UNDER: needs {maxreq}, enters at {entry:.1f} ({len(late)} quests: {late[:8]})'
        elif wants and int(entry) < wants: flag = f'  UNDER: wants {wants}, enters at {entry:.1f}'
        if low: flag += f'  SCALED: {len(low)} quests 6+ levels under the entry level pay {raw - xp:,} less ({low[:8]})'
        print(f"{ch['title'][:46]:46} {len(ch['req']):3d} {xp:9,} {money(mon):>9} {cum:9,} {entry:5.1f} {level:5.1f} {maxreq:7d} {oxp:8,}{flag}")
    lo, hi = int(start), int(level) + 1
    print(f'\nrequired quest XP {cum:,}; quest money {money(cum_money)}; optional XP listed {cum_opt:,}; ends at {level:.1f}')
    if hi <= 60: print(f'{lo} -> {hi} needs {bracket(lo, hi):,} XP in all ({round(bracket(lo, hi) * share):,} from quests at this share)')
    if problems:
        print(f'\n{len(problems)} problems:')
        for p in problems: print('  ' + p)
    return 1 if problems else 0


if __name__ == '__main__':
    sys.exit(main())
