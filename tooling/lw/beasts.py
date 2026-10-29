import re, glob, os, json, sys
G = "/mnt/user-data/uploads/WoW Forever Atlas/guide/Guidelime_ForeverAlliance"
BEAST = re.compile(r"wolf|boar|bear|leopard|crocolisk|raptor|razormaw|scytheclaw|screecher|plainstrider|kodo|worg|hyena|whelp|buzzard|condor|fleshripper|goretusk|wendigo|yeti|snapjaw|mangeclaw|vagash|frosthowl|daggerfang|den mother|sarltooth|bellygrub|nightbane|carnage|prowler|panther|tiger|gorilla|stag|lion|stalker|threshadon|lurker|turtle|dragonkin|drake", re.I)
NOT = re.compile(r"cave stalker|leech stalker|ursa|foulweald|tarantula|stalvan|pathstalker|redridge thrasher", re.I)
files = sorted(f for f in glob.glob(G + "/*.lua") if not os.path.basename(f).startswith("00"))
out = []
for f in files:
    ch = os.path.basename(f)[:-4]
    for i, ln in enumerate(open(f, encoding="utf-8"), 1):
        if ln.startswith("[OC]") or not re.search(r"\bkill|\[CI", ln, re.I):
            continue
        tars = [(m.start(), m.group(1), m.group(2)) for m in re.finditer(r"\[TAR(\d+) ([^\]]+)\]", ln)]
        beasts = [t for t in tars if BEAST.search(t[2]) and not NOT.search(t[2])]
        if not beasts:
            continue
        txt = re.sub(r"\|c[0-9a-fA-F]{8}|\|r", "", ln.strip())
        txt = re.sub(r"\[G[^\]]*\]", "", txt)
        out.append({"ch": ch, "line": i, "beasts": [b[2] for b in beasts], "text": txt[:300]})
json.dump(out, open(sys.argv[1], "w"), indent=1)
for o in out:
    print(o["ch"], o["line"], o["beasts"], "|", o["text"][:260])
