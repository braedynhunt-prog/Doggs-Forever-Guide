"""Sensitivity of the level-20 (and 15) weights to the uncertain inputs."""
import copy
from enh_weights import band_scenarios, weights, kills_per_hour

KEYS = ["wdps", "str", "int", "agi", "spi", "sta", "sp", "exp", "hitpct", "critpct", "mace_bonus"]

def run(label, sc, optimise=True):
    w, kph = weights(sc, optimise_policy=optimise)
    pol = w["_policy"]
    print(f"{label:44s} pol={str(pol[0]):>3s}/{'LS' if pol[1] else '--'}  " + " ".join(f"{k}={w[k]:5.2f}" for k in KEYS))

for lvl in (15, 20):
    base = band_scenarios()[lvl]
    print(f"\n##### level {lvl} #####")
    run("baseline (efficient policy)", base)
    run("baseline (shock every 6 s)", base, optimise=False)
    for label, mod in [
        ("Rockbiter at rank-floor value", dict(rockbiter_frac=0.0)),
        ("Rockbiter at tooltip max", dict(rockbiter_frac=1.0)),
        ("mobs +1 level", dict(mob_level_delta=1)),
        ("mobs +2 levels", dict(mob_level_delta=2)),
        ("attacking from behind (group)", dict(from_behind=True)),
        ("Spirit regen half of vanilla", dict(spirit_regen_scale=0.5)),
        ("Spirit regen zero (Forever removed it)", dict(spirit_regen_scale=0.0)),
        ("mob HP -30%", dict(mob_hp_per_level=(0.77, 6.3))),
        ("mob HP +30%", dict(mob_hp_per_level=(1.43, 11.7))),
        ("walk 5 s between mobs", dict(walk_seconds=5.0)),
        ("walk 15 s between mobs", dict(walk_seconds=15.0)),
        ("mob damage x2 (heals needed)", dict(mob_dps_per_level=1.4)),
        ("mob damage x3", dict(mob_dps_per_level=2.1)),
        ("shock SP coefficient x2", dict(shock_coef_scale=2.0)),
        ("shock SP coefficient x0", dict(shock_coef_scale=0.0)),
        ("expertise: flat 0.1%/rating (no level scaling)", dict(expertise_model="flat60")),
        ("expertise: 0.25%/point (TBC points)", dict(expertise_model="point")),
        ("no mace (axe) baseline", dict(mace=False)),
    ]:
        sc = copy.deepcopy(base)
        for k, v in mod.items(): setattr(sc, k, v)
        run(label, sc)
    # agi-per-crit +-20 %
    import enh_weights as ew
    orig = ew._AGI_PER_CRIT
    for f, lab in ((0.8, "agi/crit table x0.8 (agi better)"), (1.2, "agi/crit table x1.2 (agi worse)")):
        ew._AGI_PER_CRIT = [(l, v * f) for l, v in orig]
        run(lab, copy.deepcopy(base))
    ew._AGI_PER_CRIT = orig
    # talent order alternative at 15: TS 5 / MD 1
    if lvl == 15:
        sc = copy.deepcopy(base); sc.talents = dict(ts=5, md=1)
        run("talents: Thundering Strikes first (IV order)", sc)
