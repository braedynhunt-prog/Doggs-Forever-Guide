"""Ingest one combined zone TSV (several ZONE blocks) one block per run of tooling/ingest_zone_tsv.py,
and print per zone: rows before / after, new quests, and every change in xp / level / reqlevel / side / money.
Usage: python ingest_batch.py <repo root> <batch.tsv> [--dry]"""
import sys, os, re, json, subprocess
ROOT, PATH = sys.argv[1], sys.argv[2]
DRY = '--dry' in sys.argv
text = open(PATH, encoding='utf-8', newline='').read()
blocks = [b for b in re.split(r'(?m)^(?=ZONE\t)', text) if b.startswith('ZONE\t')]
print(f'{os.path.basename(PATH)}: {len(blocks)} blocks')
FIELDS = ('xp', 'level', 'reqlevel', 'side', 'money')
allchg = []
for b in blocks:
    if not b.endswith('\n'): b += '\n'
    head = b.split('\n', 1)[0]
    zid = int(re.search(r'zone=(\d+)', head).group(1))
    fn = os.path.join(ROOT, 'data', f'zone_{zid}.json')
    old = {q['id']: dict(q) for q in json.load(open(fn, encoding='utf-8'))['quests']} if os.path.exists(fn) else {}
    rows = [l.split('\t') for l in b.split('\n')[1:] if l.strip()]
    if not DRY:
        r = subprocess.run([sys.executable, os.path.join(ROOT, 'tooling', 'ingest_zone_tsv.py')], input=b.encode('utf-8'), capture_output=True)
        if r.returncode: print('INGEST FAILED', zid, r.stderr.decode()[-400:]); sys.exit(1)
        new = {q['id']: q for q in json.load(open(fn, encoding='utf-8'))['quests']}
    else:
        num = lambda s: None if s == '' else int(float(s)) if float(s) == int(float(s)) else float(s)
        new = {int(f[0]): {'xp': num(f[3]), 'level': num(f[1]), 'reqlevel': num(f[2]), 'side': num(f[4]), 'money': num(f[11]) or 0, 'name': f[14]} for f in rows}
    pulled = {int(f[0]) for f in rows}
    added = [i for i in pulled if i not in old]
    gone = [i for i in old if i not in pulled]
    chg = []
    for i in pulled:
        if i in old:
            for k in FIELDS:
                a, c = old[i].get(k), new[i].get(k)
                if (a or 0) != (c or 0): chg.append((i, new[i].get('name'), k, a, c))
    print(f'zone {zid} {head.split("/")[-1]}: pulled {len(pulled)} rows, file had {len(old)}, new {len(added)}, no longer listed {len(gone)}, changed fields {len(chg)}')
    for i in added[:12]: print(f'   NEW {i} {new[i].get("name")} L{new[i].get("level")} req{new[i].get("reqlevel")} xp {new[i].get("xp")} side {new[i].get("side")}')
    if len(added) > 12: print(f'   ... {len(added) - 12} more new')
    for c in chg[:25]: print('   CHG', *c)
    if len(chg) > 25: print(f'   ... {len(chg) - 25} more changes')
    if gone: print('   not listed now:', gone[:15])
    allchg += [(zid,) + c for c in chg]
print('total changed fields', len(allchg))
