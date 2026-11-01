#!/usr/bin/env python3
"""Claude Code PostToolUse hook: after an Edit/Write to a .lua under guide/, run check_guide.py and verify.py and
report anything that is not in their baselines (tooling/check_guide_baseline.txt, tooling/verify_baseline.txt).

1 Nov 2026 - several addon folders:
  - the edited file's addon folder (guide/<folder>/) is checked, with FOREVER_GUIDE set to it; the Alliance folder keeps
    the baseline names above, any other folder uses tooling/check_guide_baseline_<folder>.txt and
    tooling/verify_baseline_<folder>.txt (guidelib.baseline_path)
  - a .lua in a generator-built folder (a tooling/variants/<v>/variant.json names it) is reported as a finding: the
    next build overwrites it, edit the variant instead
  - an edit to any file under tooling/variants/<v>/ rebuilds that variant with tooling/build_variant.py and checks the
    output folder - only when the folder already exists under guide/ (the first real build is a deliberate step)

Reads the hook JSON on stdin (tool_input.file_path). Exit 0 = nothing new (or not a guide/variant file); exit 2 = new
findings, printed to stderr so Claude Code feeds them back into the session. Never blocks the edit itself (PostToolUse).
Run by hand for the same report:  python tooling/hook_check_guide.py --file guide/Guidelime_ForeverAlliance/02_LochModan.lua
"""
import sys, os, json, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..'))
GUIDE = os.path.normpath(os.path.join(ROOT, 'guide'))
VARIANTS = os.path.normpath(os.path.join(HERE, 'variants'))
sys.path.insert(0, HERE)
import guidelib as gl  # noqa: E402


def target_path():
    if len(sys.argv) > 2 and sys.argv[1] == '--file': return sys.argv[2]
    try:
        data = json.load(sys.stdin)
    except Exception as e:
        sys.stderr.write('hook_check_guide: could not parse the hook JSON on stdin (%s)\n' % e)
        sys.exit(1)
    ti = data.get('tool_input') or {}
    return ti.get('file_path') or ti.get('path')


def under(p, root):
    try:
        return os.path.commonpath([p, root]) == root
    except ValueError:
        return False


def guide_folder(p):
    """guide/<folder> for a .lua under guide/<folder>/, else None."""
    if not p or not p.lower().endswith('.lua'): return None
    ap = os.path.normpath(os.path.abspath(p))
    if not under(ap, GUIDE): return None
    rel = os.path.relpath(ap, GUIDE).split(os.sep)
    return os.path.join(GUIDE, rel[0]) if len(rel) > 1 else None


def variant_of(p):
    """tooling/variants/<v>/variant.json for a file under tooling/variants/<v>/, else None."""
    if not p: return None
    ap = os.path.normpath(os.path.abspath(p))
    if not under(ap, VARIANTS): return None
    rel = os.path.relpath(ap, VARIANTS).split(os.sep)
    vj = os.path.join(VARIANTS, rel[0], 'variant.json')
    return vj if len(rel) > 1 and os.path.exists(vj) else None


def run(script, *args, addon=None):
    env = dict(os.environ)
    if addon: env['FOREVER_GUIDE'] = addon
    r = subprocess.run([sys.executable, os.path.join(HERE, script), *args], cwd=ROOT, capture_output=True, text=True,
                       encoding='utf-8', errors='replace', env=env)
    return r.returncode, (r.stdout or '') + (r.stderr or '')


def check(addon, new):
    """check_guide.py + verify.py on one addon folder against its baselines; appends findings to new."""
    cg_base = gl.baseline_path('check_guide', addon)
    # check_guide.py: compare the full output with the accepted baseline (order-free)
    rc, out = run('check_guide.py', addon=addon)
    lines = [l for l in out.splitlines() if l.strip()]
    base = set(open(cg_base, encoding='utf-8').read().splitlines()) if os.path.exists(cg_base) else set()
    summary = [l for l in lines if ' quest events across ' in l]
    for l in lines:
        if l in base or l in summary: continue
        new.append('check_guide: ' + l)
    if rc != 0 and not new: new.append('check_guide: exited %d\n%s' % (rc, out[-2000:]))
    # verify.py: its default mode already prints only the lines missing from its baseline
    rc, vout = run('verify.py', addon=addon)
    for l in vout.splitlines():
        if l.startswith('NEW '): new.append('verify: ' + l[4:])
    if rc not in (0, 1): new.append('verify: exited %d\n%s' % (rc, vout[-2000:]))
    return (summary[0] if summary else 'check_guide ran'), (vout.strip().splitlines()[-1] if vout.strip() else 'verify ran'), cg_base


def main():
    p = target_path()
    new = []
    vj = variant_of(p)
    if vj:
        v = json.load(open(vj, encoding='utf-8'))
        addon = os.path.join(GUIDE, v['folder'])
        if not os.path.isdir(addon):
            print('variant %s changed; guide/%s not built yet - run python tooling/build_variant.py %s'
                  % (v.get('name'), v['folder'], os.path.relpath(vj, ROOT)))
            return 0
        rc, out = run('build_variant.py', vj)
        if rc != 0:
            new.append('build_variant: exited %d\n%s' % (rc, out[-2000:]))
            sys.stderr.write('Rebuild of variant %s after editing %s failed:\n' % (v.get('name'), os.path.basename(p)))
            for l in new: sys.stderr.write('  ' + l + '\n')
            return 2
        what = 'rebuilt guide/%s' % v['folder']
    else:
        addon = guide_folder(p)
        if not addon: return 0
        what = os.path.basename(p)
        gv = gl.find_variant(addon)
        if gv:
            new.append('edited %s inside a generated folder - the next build_variant.py run overwrites it; edit %s instead'
                       % (os.path.basename(p), os.path.relpath(os.path.dirname(gv[0]), ROOT)))
    s1, s2, cg_base = check(addon, new)
    if not new:
        print('guide check (%s): no new findings (%s; %s)' % (os.path.basename(addon), s1, s2))
        return 0
    sys.stderr.write('Guide check after %s (%s) - %d new finding(s) not in the baselines:\n' % (
        'editing ' + what if not vj else what, os.path.basename(addon), len(new)))
    for l in new: sys.stderr.write('  ' + l + '\n')
    sys.stderr.write('If a finding is accepted, add it to %s or run: FOREVER_GUIDE=%s python tooling/verify.py --update-baseline\n'
                     % (os.path.relpath(cg_base, ROOT), os.path.relpath(addon, ROOT)))
    return 2


if __name__ == '__main__':
    sys.exit(main())
