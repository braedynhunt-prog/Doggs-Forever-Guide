#!/usr/bin/env python3
r"""Fetch Wowhead Forever quest pages for quest ids the atlas lacks and add them to tooling\extra_quests.json
(atlas row shape, so check_guide.py / tugs_diff.py / qdetail.py pick them up).
Usage (run from the Atlas folder so scrape.py's raw\ cache is used):  python3 tooling\wh_quests.py 87760 91736 ...
   or:  python3 tooling\wh_quests.py @compare\unknown_quests.txt
"""
import sys, os, json
BASE = os.environ.get('FOREVER_ATLAS', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
os.chdir(BASE); sys.path.insert(0, BASE)
import scrape
ids = []
for a in sys.argv[1:]:
    if a.startswith('@'): ids += [int(x) for x in open(a[1:]).read().split() if x.strip().isdigit()]
    else: ids.append(int(a))
fn = os.path.join(BASE, 'tooling', 'extra_quests.json')
extra = json.load(open(fn, encoding='utf-8')) if os.path.exists(fn) else {}
for qid in ids:
    if str(qid) in extra and extra[str(qid)].get('g'): print(qid, 'already in extra_quests.json'); continue
    h = scrape.fetch(f'quest={qid}', f'quest_{qid}')
    if not h: print(qid, 'FETCH FAILED'); continue
    q = scrape.parse_quest(h, qid)
    g = q.get('g') or {}
    print(qid, q.get('name'), '| L', g.get('level'), 'req', g.get('reqlevel'), 'xp', g.get('xp'), 'side', g.get('side'), 'cat', g.get('category'),
          '|', (g.get('envChange') or {}).get('status'), '| start', [e.get('name') for e in q.get('info', {}).get('start', [])])
    extra[str(qid)] = q
json.dump(extra, open(fn, 'w', encoding='utf-8'), indent=1)
print('wrote', fn, len(extra), 'rows')
