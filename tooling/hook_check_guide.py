#!/usr/bin/env python3
"""Claude Code PostToolUse hook: after an Edit/Write to a .lua under guide/, run check_guide.py and verify.py and
report anything that is not in their baselines (tooling/check_guide_baseline.txt, tooling/verify_baseline.txt).

Reads the hook JSON on stdin (tool_input.file_path). Exit 0 = nothing new (or not a guide file); exit 2 = new findings,
printed to stderr so Claude Code feeds them back into the session. Never blocks the edit itself (PostToolUse).
Run by hand for the same report:  python tooling/hook_check_guide.py --file guide/Guidelime_ForeverAlliance/02_LochModan.lua
"""
import sys, os, json, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..'))
GUIDE = os.path.normpath(os.path.join(ROOT, 'guide'))
CG_BASELINE = os.path.join(HERE, 'check_guide_baseline.txt')

def target_path():
    if len(sys.argv) > 2 and sys.argv[1] == '--file': return sys.argv[2]
    try:
        data = json.load(sys.stdin)
    except Exception as e:
        sys.stderr.write('hook_check_guide: could not parse the hook JSON on stdin (%s)\n' % e)
        sys.exit(1)
    ti = data.get('tool_input') or {}
    return ti.get('file_path') or ti.get('path')

def is_guide_lua(p):
    if not p or not p.lower().endswith('.lua'): return False
    ap = os.path.normpath(os.path.abspath(p))
    try:
        return os.path.commonpath([ap, GUIDE]) == GUIDE
    except ValueError:
        return False

def run(script, *args):
    r = subprocess.run([sys.executable, os.path.join(HERE, script), *args], cwd=ROOT, capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.returncode, (r.stdout or '') + (r.stderr or '')

def main():
    p = target_path()
    if not is_guide_lua(p): return 0
    new = []
    # check_guide.py: compare the full output with the accepted baseline (order-free)
    rc, out = run('check_guide.py')
    lines = [l for l in out.splitlines() if l.strip()]
    base = set(open(CG_BASELINE, encoding='utf-8').read().splitlines()) if os.path.exists(CG_BASELINE) else set()
    summary = [l for l in lines if ' quest events across ' in l]
    for l in lines:
        if l in base or l in summary: continue
        new.append('check_guide: ' + l)
    if rc != 0 and not new: new.append('check_guide: exited %d\n%s' % (rc, out[-2000:]))
    # verify.py: its default mode already prints only the lines missing from verify_baseline.txt
    rc, out = run('verify.py')
    for l in out.splitlines():
        if l.startswith('NEW '): new.append('verify: ' + l[4:])
    if rc not in (0, 1): new.append('verify: exited %d\n%s' % (rc, out[-2000:]))
    if not new:
        print('guide check: no new findings (%s; %s)' % (summary[0] if summary else 'check_guide ran', out.strip().splitlines()[-1] if out.strip() else 'verify ran'))
        return 0
    sys.stderr.write('Guide check after editing %s - %d new finding(s) not in the baselines:\n' % (os.path.basename(p), len(new)))
    for l in new: sys.stderr.write('  ' + l + '\n')
    sys.stderr.write('If a finding is accepted, add it to tooling/check_guide_baseline.txt or run: python tooling/verify.py --update-baseline\n')
    return 2

if __name__ == '__main__':
    sys.exit(main())
