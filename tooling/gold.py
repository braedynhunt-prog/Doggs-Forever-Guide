"""Quest money per guide chapter, from the Wowhead Forever zone files (data/zone_*.json, field "money").

Usage:
  python tooling/gold.py                     per-chapter required / optional turn-in money and the running total
  python tooling/gold.py 02_LochModan.lua:48 the running total up to (not including) that line of that chapter
Required = [QT] on a step that is not [O]; optional = [QT] on an [O] step. Hidden Human/Hunter lines are skipped.
Vendor sales are not counted. Guide folder: guide/Guidelime_ForeverShaman (override with GUIDE_DIR).
"""
import glob, json, os, re, sys

ROOT = os.environ.get("FOREVER_ATLAS", os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GUIDE = os.environ.get("GUIDE_DIR", os.path.join(ROOT, "guide", "Guidelime_ForeverShaman"))


def quest_money():
    money = {}
    for f in glob.glob(os.path.join(ROOT, "data", "zone_*.json")):
        with open(f, encoding="utf-8") as fh:
            for q in json.load(fh).get("quests", []):
                money[q["id"]] = q.get("money") or 0
    return money


def fmt(c):
    return f"{c // 10000}g {(c % 10000) // 100:02d}s" if c >= 10000 else f"{c // 100}s {c % 100:02d}c"


def main():
    money = quest_money()
    stop = sys.argv[1] if len(sys.argv) > 1 else None
    stop_file, stop_line = (stop.split(":")[0], int(stop.split(":")[1])) if stop else (None, None)
    cum = 0
    for f in sorted(glob.glob(os.path.join(GUIDE, "*.lua"))):
        name = os.path.basename(f)
        if name in ("11s_DarkshoreShort.lua", "11t_SleepingBag.lua"):   # alternate chapters (guidelib.ALTERNATES): their turn-ins repeat chapter 11's and 26's
            continue
        req = opt = 0
        unknown = []
        with open(f, encoding="utf-8") as fh:
            for n, line in enumerate(fh, 1):
                if name == stop_file and n >= stop_line:
                    break
                if "[A Hunter]" in line or "[GA Human]" in line:
                    continue
                for qid in re.findall(r"\[QT(\d+)", line):
                    qid = int(qid)
                    if qid not in money:
                        unknown.append(qid)
                        continue
                    if line.startswith("[O]"):
                        opt += money[qid]
                    else:
                        req += money[qid]
        cum += req
        extra = f"  no money data: {unknown}" if unknown else ""
        print(f"{name:30} required {fmt(req):>9}  optional {fmt(opt):>9}  running total {fmt(cum):>9}{extra}")
        if name == stop_file:
            print(f"-> required quest money before {stop}: {fmt(cum)}")
            break


if __name__ == "__main__":
    main()
