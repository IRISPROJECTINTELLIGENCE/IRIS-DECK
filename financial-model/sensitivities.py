"""Re-run the model with one input changed at a time and record the base-case results.

Run: python3 sensitivities.py <recalc.py>   (writes sensitivities.json beside this file)
build_model.py then prints the table on the Sensitivities sheet. Each variant changes the base case only.
"""
import json, os, subprocess, sys, tempfile
import openpyxl

HERE = os.path.dirname(os.path.abspath(__file__))
RECALC = sys.argv[1]
B = lambda b: None  # placeholder

# (group, label of the change, override); base values are taken from the model as built.
VARIANTS = [
    ("Average facility under IRIS (base $80M)", "$60M", {"fac_avg": [60, 102, 48]}),
    ("Average facility under IRIS (base $80M)", "$100M", {"fac_avg": [100, 102, 48]}),
    ("Facility fee (base 15 bps)", "10 bps", {"bps": [10, 15, 12.5]}),
    ("Facility fee (base 15 bps)", "20 bps", {"bps": [20, 15, 12.5]}),
    ("New facilities per lender a month (base 0.8)", "0.5", {"per_lender": [0.5, 1.0, 0.5]}),
    ("New facilities per lender a month (base 0.8)", "1.0", {"per_lender": [1.0, 1.0, 0.5]}),
    ("Lender rollout (base: first lender at month 12)", "Six months later", {"table:lenders_shift": 6}),
    ("Existing loans each lender re-signs (base 10)", "5", {"book_fac": [5, 14, 6]}),
    ("Existing loans each lender re-signs (base 10)", "15", {"book_fac": [15, 14, 6]}),
    ("Facility term (base 24 months)", "18 months", {"fac_term": [18, 24, 24]}),
    ("Facility term (base 24 months)", "36 months", {"fac_term": [36, 24, 24]}),
    ("Builder subscription (base $3,500 a month)", "$2,500", {"price_b": [2500, 3500, 3500]}),
    ("Builder subscription (base $3,500 a month)", "$5,000", {"price_b": [5000, 3500, 3500]}),
    ("Jobs per deployment analyst by month 60 (base 15)", "10", {"an_ratio_end": [10, 15, 15]}),
    ("Jobs per deployment analyst by month 60 (base 15)", "20", {"an_ratio_end": [20, 15, 15]}),
    ("Director salary to Year 3 (base $100,000)", "$140,000", {"sal_found": [140000, 100000, 100000]}),
    ("Projects that stall a year (base 4%)", "2%", {"distress": [0.02, 0.05, 0.03]}),
    ("Projects that stall a year (base 4%)", "6%", {"distress": [0.06, 0.05, 0.03]}),
    ("Seed round (base month 15)", "Month 18", {"seed_m": [18, 15, 15]}),
    # Downside cases (kind "down"): lender adoption, retention and the seed.
    ("Lender adoption", "Every lender twelve months later", {"table:lenders_shift": 12}, "down"),
    ("Lender adoption", "No lender in five years: builders and assessments alone", {"table:lenders_shift": 60}, "down"),
    ("Lender retention", "Each lender stops adding facilities after three years", {"lend_life": [36, 60, 60]}, "down"),
    ("Seed round ($3M at month 15)", "At month 21", {"seed_m": [21, 15, 15]}, "down"),
    ("Seed round ($3M at month 15)", "$1.5M", {"seed": [1500000, 3000000, 3000000]}, "down"),
    ("Seed round ($3M at month 15)", "No seed", {"seed": [0, 3000000, 3000000]}, "down"),
    ("Combined", "Lenders twelve months later and a $1.5M seed at month 21", {"table:lenders_shift": 12, "seed": [1500000, 3000000, 3000000], "seed_m": [21, 15, 15]}, "down"),
]

def run(override):
    with tempfile.TemporaryDirectory() as d:
        out = os.path.join(d, "m.xlsx")
        env = dict(os.environ, IRIS_OVERRIDE=json.dumps(override), IRIS_NO_SENS="1")
        subprocess.run([sys.executable, os.path.join(HERE, "build_model.py"), out], check=True, env=env, capture_output=True)
        r = subprocess.run([sys.executable, RECALC, out, "120"], capture_output=True, text=True)
        assert '"errors_found"' not in r.stdout and '"success"' in r.stdout, r.stdout
        S = openpyxl.load_workbook(out, data_only=True)["Summary"]
        def row(l):
            for i in range(1, S.max_row + 1):
                v = S.cell(row=i, column=1).value
                if isinstance(v, str) and v.startswith(l): return i
        g = lambda l, c=6: S.cell(row=row(l), column=c).value
        return {"rev5": g("Total revenue"), "ebitda5": g("Operating result"), "arr60": g("Annualised revenue at year end"),
                "low_cash": g("Lowest cash with seed (base)", 2), "ebitda3": g("Operating result", 4),
                "neg_month": g("First month cash with seed goes negative, base", 2)}

results = {"base": run({}), "variants": []}
for v in VARIANTS:
    grp, lab, ov = v[:3]
    kind = v[3] if len(v) > 3 else "one"
    results["variants"].append({"group": grp, "change": lab, "kind": kind, **run(ov)})
    print(grp, lab, results["variants"][-1])
json.dump(results, open(os.path.join(HERE, "sensitivities.json"), "w"), indent=1)
