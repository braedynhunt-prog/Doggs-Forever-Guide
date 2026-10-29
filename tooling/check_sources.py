#!/usr/bin/env python3
"""Freshness check for the game data the guide is built from (manifest: tooling/sources.json).

READ-ONLY: only makes GET requests for version metadata. It never downloads datasets and never writes or
modifies any file; it prints the pull steps for anything stale.

Usage (repo root):  python tooling/check_sources.py [--quiet]
Exit: 0 all OK/INFO, 1 anything STALE, 2 any source unreachable (ERROR; wins over STALE).
"""
import argparse, glob, json, os, re, shutil, ssl, subprocess, urllib.request, urllib.error

BASE = os.path.abspath(os.environ.get('FOREVER_ATLAS', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')))
UA = 'Mozilla/5.0'


def get_json(url):
    """GET url -> parsed JSON; raises on failure. Python's ssl cannot verify api.github.com on this Windows box
    (intermediate certificate missing), so on a certificate failure the same GET is retried with curl, which
    verifies through the OS store. Any other failure is raised as is."""
    try:
        req = urllib.request.Request(url, headers={'User-Agent': UA})
        with urllib.request.urlopen(req, timeout=20) as r:
            return json.loads(r.read().decode('utf-8-sig'))
    except urllib.error.URLError as e:
        if not isinstance(e.reason, ssl.SSLError) or not shutil.which('curl'):
            raise
    out = subprocess.run(['curl', '-s', '-f', '--max-time', '20', '-A', UA, url], capture_output=True, timeout=30)
    if out.returncode != 0:
        raise RuntimeError('curl exit %d (after a python SSL verify failure)' % out.returncode)
    return json.loads(out.stdout.decode('utf-8-sig'))


def vtuple(s):
    return tuple(int(p) for p in s.split('.'))


def rel(*p):
    return os.path.join(BASE, *p)


def check_questiedb(src):
    with open(rel('tooling', 'qdb', 'META.json'), encoding='utf-8') as f:
        local = json.load(f)['version']
    best = None
    for r in get_json(src['upstream']['url']):
        m = re.match(r'bundle/.*\+v(\d+(?:\.\d+)*)$', r['tag_name'])
        if m and (best is None or vtuple(m.group(1)) > vtuple(best[0])):
            best = (m.group(1), r['published_at'][:10], [a['name'] for a in r['assets'] if a['name'].endswith('.zip')])
    if not best:
        raise RuntimeError('no bundle/ release in the upstream list')
    up, date, zips = best
    if vtuple(up) > vtuple(local):
        steps = [s.format(version=up, zip=zips[0] if zips else 'the zip asset') for s in src['pull']]
        return 'STALE', 'local %s -> upstream %s (%s)' % (local, up, date), [], steps
    return 'OK', 'local %s, upstream %s (%s)' % (local, up, date), [], []


def wago_latest(src):
    b = max(get_json(src['upstream']['url'])['wowf'], key=lambda x: x['created_at'])
    return b['version'], b['created_at']


def check_client(src, latest):
    root = rel('tooling', 'client')
    dirs = [d for d in os.listdir(root) if os.path.isdir(os.path.join(root, d)) and re.fullmatch(r'\d+(\.\d+)+', d)]
    local = max(dirs, key=vtuple) if dirs else None
    up, created = latest
    if local != up:
        steps = [s.format(build=up, tables=' '.join(src['tables'])) for s in src['pull']]
        return 'STALE', 'local %s -> upstream %s (%s)' % (local, up, created[:10]), [], steps
    return 'OK', 'local %s, upstream %s (%s)' % (local, up, created[:10]), [], []


def check_wowhead(src, latest):
    build_date = latest[1][:10]
    done, never = {}, []
    for f in sorted(glob.glob(rel('data', 'zone_*.json')), key=lambda p: int(re.search(r'zone_(\d+)', p).group(1))):
        zid = re.search(r'zone_(\d+)', f).group(1)
        with open(f, encoding='utf-8') as fh:
            d = json.load(fh).get('_browser_refresh')  # absent counts as null
        if d:
            done[zid] = d
        else:
            never.append(zid)
    stale = [z for z, d in done.items() if d < build_date]
    dates = sorted(done.values())
    head = 'zones refreshed %d, oldest %s, newest %s, stale %d (client build %s of %s)' % (
        len(done), dates[0] if dates else '-', dates[-1] if dates else '-', len(stale), latest[0], build_date)
    extra = (['stale zones: ' + ' '.join(stale)] if stale else []) + (['never browser-pulled: ' + ' '.join(never)] if never else [])
    return ('STALE' if stale else 'OK'), head, extra, (src['pull'] if stale else [])


def check_forever_db(src):
    r = max(get_json(src['upstream']['url']), key=lambda x: x['published_at'])
    return 'INFO', 'unused, third-party; newest release %s (%s). %s' % (r['tag_name'], r['published_at'][:10], src['notes']), [], []


def check_probe(src):
    ok = os.path.isfile(rel('probe', 'probe2json.py'))
    return 'INFO', 'no upstream; %s %s. %s' % (src['converter'], 'exists' if ok else 'MISSING', src['notes']), [], []


def main():
    ap = argparse.ArgumentParser(description='Read-only freshness check of the guide data sources.')
    ap.add_argument('--quiet', action='store_true', help='print only non-OK rows')
    args = ap.parse_args()
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sources.json'), encoding='utf-8') as f:
        srcs = {s['id']: s for s in json.load(f)['sources']}
    latest, latest_err = None, None
    try:
        latest = wago_latest(srcs['client'])
    except Exception as e:
        latest_err = 'wago.tools unreachable: %s: %s' % (type(e).__name__, e)

    def with_wago(fn):
        def run(src):
            if latest is None:
                raise RuntimeError(latest_err)
            return fn(src, latest)
        return run

    checks = [('questiedb', check_questiedb), ('client', with_wago(check_client)), ('wowhead_xp', with_wago(check_wowhead)),
              ('forever_db', check_forever_db), ('probe', check_probe)]
    code = 0
    for sid, fn in checks:
        try:
            status, line, extra, steps = fn(srcs[sid])
        except Exception as e:
            status, line, extra, steps = 'ERROR', '%s: %s' % (type(e).__name__, e), [], []
        if status == 'ERROR':
            code = 2
        elif status == 'STALE' and code == 0:
            code = 1
        if args.quiet and status == 'OK':
            continue
        print('%-6s %-11s %s' % (status, sid, line))
        for e in extra:
            print('       ' + ' ' * 12 + e)
        for s in steps:
            print('       ' + ' ' * 12 + 'pull: ' + s)
    raise SystemExit(code)


if __name__ == '__main__':
    main()
