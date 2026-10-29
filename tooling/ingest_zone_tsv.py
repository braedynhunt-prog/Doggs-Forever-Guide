#!/usr/bin/env python3
r"""Merge quest rows read off Wowhead Forever zone pages in the built-in browser into data\zone_<id>.json.

stdin = one or more blocks, each starting with a line  ZONE<TAB>/forever/zone=<id>/<slug>  followed by rows
  id level reqlevel xp side category category2 type reqclass reqrace status money itemchoices itemrewards name  (tab-separated).
Existing rows keep their other fields; level/reqlevel/xp/side/category/status/money/rewards/name are refreshed; new quests are added.
A raw copy of every block goes to data\browser\zone_<id>_<date>.tsv.
"""
import sys, os, json, re, datetime
BASE = os.environ.get('FOREVER_ATLAS', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
DATA = os.path.join(BASE, 'data'); RAWD = os.path.join(DATA, 'browser'); os.makedirs(RAWD, exist_ok=True)
today = datetime.date.today().isoformat()
blocks = re.split(r'(?m)^ZONE\t', sys.stdin.read())
def num(s):
    if s in ('', None): return None
    try: return int(s)
    except ValueError: return float(s)
for b in blocks:
    if not b.strip(): continue
    head, _, body = b.partition('\n')
    m = re.search(r'zone=(\d+)/?([\w-]*)', head); zid = int(m.group(1)); slug = m.group(2) or str(zid)
    open(os.path.join(RAWD, f'zone_{zid}_{today}.tsv'), 'w', encoding='utf-8').write('ZONE\t' + b)
    fn = os.path.join(DATA, f'zone_{zid}.json')
    z = json.load(open(fn, encoding='utf-8')) if os.path.exists(fn) else {'id': zid, 'slug': slug, 'quests': [], 'npcs': [], 'objects': [], 'items_start': [], 'items_rewards': []}
    old = {q['id']: q for q in z.get('quests', [])}
    n_new = n_upd = n_xp = 0
    for line in body.split('\n'):
        if not line.strip(): continue
        f = line.split('\t')
        if len(f) < 15: f += [''] * (15 - len(f))
        qid = int(f[0])
        row = old.get(qid)
        if row is None:
            row = {'id': qid, '_type': 6}; z['quests'].append(row); old[qid] = row; n_new += 1
        else: n_upd += 1
        if row.get('xp') in (None, '') and f[3] != '': n_xp += 1
        row.update({'level': num(f[1]), 'reqlevel': num(f[2]), 'xp': num(f[3]), 'side': num(f[4]), 'category': num(f[5]), 'category2': num(f[6]),
                    'type': num(f[7]), 'reqclass': num(f[8]) or 0, 'reqrace': num(f[9]) or 0, 'money': num(f[11]) or 0, 'name': f[14],
                    'itemchoices': [[int(x), 1] for x in f[12].split(',') if x], 'itemrewards': [[int(x), 1] for x in f[13].split(',') if x]})
        ec = row.setdefault('envChange', {'status': '', 'labels': [], 'lines': []}); ec['status'] = f[10]
        row['_browser'] = today
    z['_browser_refresh'] = today
    json.dump(z, open(fn, 'w', encoding='utf-8'), ensure_ascii=False)
    from collections import Counter
    st = Counter(q.get('envChange', {}).get('status') for q in z['quests'])
    print(f'zone {zid} {slug}: {n_new} new rows, {n_upd} refreshed ({n_xp} gained xp); now {len(z["quests"])} quests {dict(st)}')
