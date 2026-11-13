"""Apply the fix-round proposals to a guide folder (a scratch mirror by default) and print the old / new lines.
Usage: python fix_apply.py <guide folder> <spec.json> [<proposed.tsv> ...] [--quiet]
spec rows: file, line, subs [[old, new], ...], optional after [lines]; tsv rows: file <TAB> line <TAB> full new line.
Line numbers are the ORIGINAL file's; insertions are applied bottom-up so they do not shift earlier rows."""
import sys, os, json, re, collections
G = sys.argv[1]; QUIET = '--quiet' in sys.argv
args = [a for a in sys.argv[2:] if a != '--quiet']
edits = collections.defaultdict(dict)       # file -> line -> (new line, [after lines], why)
for a in args:
    if a.endswith('.json'):
        for r in json.load(open(a, encoding='utf-8')):
            lines = open(os.path.join(G, r['file']), encoding='utf-8', newline='').read().split('\n')
            cur = edits[r['file']].get(r['line'], (lines[r['line'] - 1], [], ''))[0]
            for old, new in r['subs']:
                if cur.count(old) != 1: sys.exit(f"{r['file']}:{r['line']}: expected exactly one match of: {old[:70]}")
                cur = cur.replace(old, new)
            edits[r['file']][r['line']] = (cur, r.get('after', []), r.get('why', ''))
    else:
        for row in open(a, encoding='utf-8', newline='').read().split('\n'):
            if not row.strip(): continue
            f, n, new = row.rstrip('\r').split('\t', 2); n = int(n)
            if n in edits[f]: sys.exit(f'{f}:{n} is proposed twice')
            edits[f][n] = (new, [], 'stale "not in the data" remark')
tag = lambda s: sorted(re.findall(r'\[[^\]]*\]', s))
n_edit = n_add = 0
for f in sorted(edits):
    path = os.path.join(G, f)
    lines = open(path, encoding='utf-8', newline='').read().split('\n')
    for n in sorted(edits[f], reverse=True):
        new, after, why = edits[f][n]; old = lines[n - 1]
        bad = [c for c in new + ''.join(after) if ord(c) > 126 or c == '\t']
        if not QUIET:
            print(f'--- {f}:{n}  ({why})' + ('' if tag(old) == tag(new) else '   [tags differ]') + ('   NON-ASCII' if bad else ''))
            print('OLD ' + old); print('NEW ' + new)
            for x in after: print('ADD ' + x)
        lines[n - 1:n] = [new] + after; n_edit += 1; n_add += len(after)
    open(path, 'w', encoding='utf-8', newline='').write('\n'.join(lines))
print(f'{n_edit} lines changed, {n_add} lines added, in {len(edits)} files')
