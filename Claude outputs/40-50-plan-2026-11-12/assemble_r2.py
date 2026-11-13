"""Join the hand-written head and tail with the generated sections into docs/40-50-plan-2026-11-12.md.
Usage: python assemble_r2.py <repo root>   (run plan_r2.py first)"""
import sys, os
ROOT = sys.argv[1]
S = os.path.dirname(os.path.abspath(__file__))
rd = lambda n: open(os.path.join(S, n), encoding='utf-8').read()
gen = rd('plan_generated.md').split('\n', 2)[2]
doc = rd('plan_head.md').rstrip('\n') + '\n\n' + gen.rstrip('\n') + '\n' + rd('plan_tail.md')
open(os.path.join(ROOT, 'docs', '40-50-plan-2026-11-12.md'), 'w', encoding='utf-8', newline='\n').write(doc)
print('lines', doc.count('\n'), 'bytes', len(doc.encode('utf-8')), 'non-ASCII', sorted({c for c in doc if ord(c) > 126})[:8])
