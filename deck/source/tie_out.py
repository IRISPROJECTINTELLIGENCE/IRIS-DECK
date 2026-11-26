"""Tie every model-derived figure on slides 2, 11 and 13, and on A5, A6, A15 and A16, to the workbook.
Usage: python3 -I tie_out.py <workbook.xlsx> <slides dir>"""
import sys, re, html, openpyxl
from decimal import Decimal, ROUND_HALF_UP
wbp, sd = sys.argv[1], sys.argv[2]
wb = openpyxl.load_workbook(wbp, data_only=True)
S, M, I = wb["Summary"], wb["Market"], wb["Inputs"]
def rnd(x, nd=0):
    return Decimal(repr(float(x))).quantize(Decimal(1).scaleb(-nd), rounding=ROUND_HALF_UP)
def srow(label, sheet=S, col=1):
    for r in range(1, sheet.max_row + 1):
        v = sheet.cell(row=r, column=col).value
        if isinstance(v, str) and v.startswith(label): return r
    raise KeyError(label)
def sv(label, case=0):  # five years of a Summary line; case 0 base, 1 upside, 2 conservative
    r = srow(label); c0 = 2 + 6 * case
    return [S.cell(row=r, column=c0 + i).value for i in range(5)]
def mv(label): return M.cell(row=srow(label, M), column=2).value
def iv(label, col=2): return I.cell(row=srow(label, I), column=col).value
def ue(label): return S.cell(row=srow(label), column=2).value
def text(name):
    s = open(f"{sd}/{name}.html").read(); body, _, aside = s.partition("<aside>")
    f = lambda t: re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", t)))
    return f(body), f(aside)
def k(x): return f"{int(rnd(x/1000)):,}"
def sgn(x): return ("+" if x > 0 else "−") + f"{abs(int(rnd(x/1000))):,}"
def m1(x): return f"${rnd(x/1e6,1)}M"
def m2(x):
    v = rnd(x/1e6, 2 if abs(x) < 1e6 else 1); return ("−" if x < 0 else "") + f"${abs(v)}M"
checks = []; figs = 0
def chk(where, label, shown, hay):
    global figs
    ok = shown in hay; checks.append((ok, where, label, shown)); figs += len(re.findall(r"\d[\d,.]*", shown))
ec, ecn = text("economics"); ra, ran = text("raise"); a5, a5n = text("apx-sizing"); a6, a6n = text("apx-model")
rev_f, rev_b, rev_a, rev = sv("IRIS for Lenders"), sv("IRIS for Builders"), sv("Distressed-project assessments"), sv("Total revenue")
ppl, plat, go, cont, cost, op = sv("People"), sv("Platform build"), sv("Sales, commissions"), sv("Contingency"), sv("Total costs"), sv("Operating result")
len_, fac, bld, jobs, team = sv("Lenders with the condition"), sv("Facilities under the condition"), sv("Paying builders"), sv("Paid builder jobs"), sv("Team")
# slide 11 table
chk("11", "lenders row", " ".join(k(x) for x in rev_f), ec)
chk("11", "builders row", " ".join(k(x) for x in rev_b), ec)
chk("11", "assessments row", "– – " + " ".join(k(x) for x in rev_a[2:]), ec)
chk("11", "revenue row", "Revenue " + " ".join(k(x) for x in rev), ec)
chk("11", "people row", "People " + " ".join(k(x) for x in ppl), ec)
chk("11", "platform row", " ".join(k(x) for x in plat), ec)
chk("11", "sales row", " ".join(k(x) for x in go), ec)
chk("11", "total costs row", "with contingency " + " ".join(k(x) for x in cost), ec)
chk("11", "EBITDA row", " ".join(sgn(x) for x in op), ec)
for y in range(5):
    assert abs(ppl[y] + plat[y] + go[y] + cont[y] - cost[y]) < 1, "cost rows do not sum"
    assert abs(rev_f[y] + rev_b[y] + rev_a[y] - rev[y]) < 1 and abs(rev[y] - cost[y] - op[y]) < 1
checks.append((True, "11", "cost rows + contingency = total; revenue lines = revenue; revenue − costs = EBITDA (5 years)", "arithmetic")); figs += 0
# slide 11 tiles and footer (D-54: SAM is the jobs with a construction facility; tiers nest)
tam, sam, som = mv("Total market (TAM)"), mv("Serviceable market (SAM)"), mv("Obtainable (SOM): annualised revenue at month 60, Base")
qm, live_n, live_dev, live_oth = mv("First market: Queensland"), mv("Live projects in scope, Australia"), mv("of which developer-funded"), mv("of which other")
chk("11", "TAM tile", f"${int(rnd(tam))}M Total market (TAM)", ec)
chk("11", "SAM tile", f"${int(rnd(sam))}M Serviceable (SAM)", ec)
chk("11", "SOM tile", f"${rnd(som,1)}M Obtainable (SOM)", ec)
chk("11", "SOM share of SAM", f"{int(rnd(som/sam*100))}% of SAM", ec); assert sam < tam and som < sam
chk("11", "live jobs Australia (about 4,330)", f"About {int(round(live_n,-1)):,} live jobs", ec)
chk("11", "jobs with a facility", f"The {int(round(live_dev)):,} jobs with a facility", ec)
chk("11", "Queensland first market", f"Queensland: ${int(rnd(qm))}M", ec)
chk("11", "about 370 facilities; 92 jobs", "about 370 facilities; seventeen builders on 92 jobs", ec); assert round(fac[4], -1) == 370 and round(jobs[4]) == 92 and round(bld[4]) == 17 and round(len_[4]) == 20
chk("11", "lenders at year end", " / ".join(str(int(rnd(x))) for x in len_) + " lenders", ec)
chk("11", "facilities at year end", " / ".join(str(int(rnd(x))) for x in fac) + " facilities", ec)
chk("11", "team", "team " + " / ".join(str(int(rnd(x))) for x in team), ec)
fa = [iv("Average facility under IRIS, full debt stack", c) for c in (2, 3, 4)]
chk("11", "average facility, base", f"facilities averaging ${int(rnd(fa[0]))}M", ec)
chk("11", "upside and conservative", f"Upside ${int(rnd(sv('Total revenue',1)[4]/1e6))}M, conservative ${rnd(sv('Total revenue',2)[4]/1e6,1)}M", ec)
assert min(S.cell(row=srow("Cash at year end, with seed"), column=c).value for c in list(range(2,7))+list(range(8,13))+list(range(14,19))) > 0
assert ue("First month cash with seed goes negative, base") == 99 and ue("First month cash goes negative, conservative") == 99
checks.append((True, "11", "cash positive with the seed in all three cases (year ends; base and conservative month by month)", "check"))
# slide 11 notes
arr49, arr60 = ue("Run rate at month 49"), ue("Run rate at month 60")
chk("11 notes", "Year 1 costs", f"Year 1 costs (${k(cost[0])}K)", ecn)
chk("11 notes", "facility basis", f"average ${int(rnd(fa[0]))}M across the whole debt stack (senior alone or senior with mezzanine), entered directly by case", ecn)
chk("11 notes", "fee per facility", f"${int(ue('Annualised fee per facility')):,} a year at 15 bps", ecn)
chk("11 notes", "tiers", f"TAM ${rnd(tam,1)}M: {int(round(live_dev)):,} jobs", ecn); chk("11 notes", "SAM", f"SAM ${rnd(sam,1)}M", ecn)
chk("11 notes", "SOM shares", f"{int(rnd(som/sam*100))}% of SAM and {int(rnd(som/tam*100))}% of TAM", ecn)
chk("11 notes", "facility value", f"${rnd(mv('Facility value under IRIS'),1)}bn, {int(rnd(mv('Facility value under IRIS')/mv('Construction facility value')*100))}% of the ${int(rnd(mv('Construction facility value')))}bn", ecn)
chk("11 notes", "Queensland", f"first market at ${rnd(qm,1)}M", ecn)
chk("11 notes", "run rate bridge", f"run rate is {m1(arr49)} at month 49 and {m1(arr60)} at month 60", ecn)
chk("11 notes", "margins", f"Contribution per facility is {int(rnd(ue('Contribution margin per facility')*100))}% and Year 5 EBITDA {int(rnd(ue('Year 5 EBITDA margin')*100))}%", ecn)
# slide 13 notes and runway
chk("13 notes", "Year 1 costs and revenue", f"${k(cost[0])}K against $650K of spend lines here; Year 1 revenue of ${k(rev[0])}K", ran)
uof = [("Enterprise product build", "$320K"), ("Founder salaries", "$224K"), ("Security audit, cloud and models", "$46K"), ("Sales, marketing and customer success", "$20K"), ("Legal, accounting and IP", "$20K"), ("Contingency and insurance", "$20K"), ("Runway reserve to the seed", "$100K")]
for lab, shown in uof:
    r = srow(lab, S, 8); v = S.cell(row=r, column=12).value
    chk("13", f"use of funds: {lab}", f"{lab if lab!='Founder salaries' else 'Founder salaries, full-time, with super'} {shown}", ra); assert f"${int(v/1000)}K" == shown
RW = int(ue("Months the round alone covers"))
low = ue("Lowest cash with seed (base)")
SN = wb["Sensitivities"]
def sens(change):
    r = srow(change, SN, 2)
    neg = SN.cell(row=r, column=8).value
    return dict(rev5=SN.cell(row=r, column=3).value, e5=SN.cell(row=r, column=5).value, low=SN.cell(row=r, column=7).value, neg=neg)
s21 = sens("At month 21")
need_by = int(s21["neg"].split()[1]) - 1
chk("13", "runway line", f"covers {RW} months of costs before any revenue; the seed is needed by month {need_by}", ra)
chk("13 notes", "runway notes", f"covers {RW} months of the plan’s costs; with the plan’s revenue cash stays above ${int(rnd(low/1000))}K", ran)
su, sun = text("summary")
chk("2", "round row runway", f"It covers {RW} months of costs before any revenue", su)
# A5
a5r = lambda key: mv(key)
chk("A5", "building work", f"${rnd(mv('Multi-unit work in scope')+mv('C&I work in scope'),1)}bn", a5)
chk("A5", "value under construction", f"${int(rnd(mv('Value under construction in scope, Australia')))}bn", a5)
chk("A5", "with a facility", f"${int(rnd(mv('Developer-funded value under construction')))}bn", a5)
chk("A5", "live jobs", f"{int(round(live_n)):,} {int(round(live_dev)):,} with a facility; {int(round(live_oth))} without", a5)
chk("A5", "TAM formula", f"{int(round(live_dev)):,} × ${int(mv('Facility fee per facility a year')/1000)}K + {int(round(live_oth))} × ${int(mv('Builder subscription per job a year')/1000)}K + ${rnd(mv('Assessments a year, Australia'),1)}M", a5)
chk("A5", "tiers", f"${int(rnd(tam))}M", a5); chk("A5", "SAM", f"${int(rnd(sam))}M", a5); chk("A5", "SOM", f"${rnd(som,1)}M", a5)
chk("A5", "SOM build", f"{int(rnd(fac[4]))} × ${int(ue('Annualised fee per facility')/1000)}K + {int(rnd(jobs[4]))} × $42K", a5)
chk("A5", "three sizes", f"$40M is the market’s average job, ${int(rnd(iv('Average facility across the market')))}M its average facility (1.2 times), ${int(rnd(fa[0]))}M", a5)
chk("A5 notes", "TAM", f"TAM = {int(round(live_dev)):,} × $72,000 + {int(round(live_oth))} × $42,000 + $4.9M = ${rnd(tam,1)}M", a5n)
chk("A5 notes", "SAM", f"= ${rnd(sam,1)}M (D-54)", a5n)
chk("A5 notes", "Queensland", f"{int(round(mv('Live projects in scope, Queensland')))} live jobs and ${rnd(qm,1)}M", a5n)
chk("A5 notes", "SOM shares", f"${rnd(som,1)}M, {int(rnd(som/sam*100))}% of SAM and {int(rnd(som/tam*100))}% of TAM", a5n)
chk("A5 notes", "checks", f"the {int(round(mv('Jobs under IRIS')))} jobs under IRIS at month 60 are {int(rnd(mv('as a share of live jobs')*100))}% of live jobs", a5n)
# A6
chk("A6", "lenders Y1/Y3/Y5", " · ".join(str(int(rnd(len_[i]))) for i in (0, 2, 4)), a6)
chk("A6", "fee", f"${int(ue('Annualised fee per facility')/1000)}K 15 bps on ${int(rnd(fa[0]))}M", a6)
chk("A6", "contribution", f"{int(rnd(ue('Contribution margin per facility')*100))}% Fee less analyst", a6)
cj, cl, cf = ue("Year 5 costs that grow with jobs"), ue("Year 5 costs that grow with lenders"), ue("Year 5 fixed costs")
chk("A6", "EBITDA margin", f"{int(rnd(ue('Year 5 EBITDA margin')*100))}% Job costs {m1(cj)}; lender staff {m1(cl)}; fixed {m1(cf)}", a6)
chk("A6", "revenue and run rate", f"{m2(rev[4])} Months 49 to 60. Month 60 × 12 is the {m1(arr60)} run rate", a6)
chk("A6", "each $10M of facility", f"Each $10M of facility is about ${rnd(rev_f[4]/fa[0]*10/1e6,1)}M of Year 5 revenue", a6)
chk("A6 notes", "fees per mature lender", f"ach mature lender is about ${rnd(ue('Annualised facility fees per lender at month 60')/1e6,1)}M a year of fees (about {int(rnd(ue('Facilities per lender at month 60')))} facilities)", a6n)
chk("A6 notes", "unit economics", f"costs about ${int(rnd(-ue('less deployment analyst')/100))*100:,} a job", a6n)
chk("A6 notes", "contribution", f"contribution ${int(rnd(ue('Contribution per facility a year')/100))*100:,}, {int(rnd(ue('Contribution margin per facility')*100))}%", a6n)
chk("A6 notes", "run rate", f"from {m1(rev[4]*0+ue('Run rate at month 49')/12)} in month 49 to {m1(arr60/12)} in month 60", a6n)
chk("A6 notes", "run rates", f"{m1(arr49)} at month 49 and {m1(arr60)} at month 60", a6n)
chk("A6 notes", "revenue list", "revenue " + " / ".join(m2(x) for x in rev), a6n)
chk("A6 notes", "EBITDA list", "EBITDA " + " / ".join(m2(x) for x in op), a6n)
chk("A6 notes", "upside and conservative", f"upside ${int(rnd(sv('Total revenue',1)[4]/1e6))}M and conservative ${rnd(sv('Total revenue',2)[4]/1e6,1)}M in Year 5", a6n)
an6 = sens("6")
chk("A6 notes", "analyst lever", f"six jobs each takes Year 5 EBITDA to {m1(an6['e5'])}", a6n)
ret = sens("Each lender stops adding facilities after three years")
chk("A6 notes", "retention", f"Year 5 revenue would fall by {m1(rev[4]-ret['rev5'])}", a6n)
# A15 downside cases (Sensitivities sheet)
a15, a15n = text("apx-downside")
late, none_, nos, s15, comb = sens("Every lender twelve months later"), sens("No lender in five years"), sens("No seed"), sens("$1.5M"), sens("Lenders twelve months later and a $1.5M seed")
def m1s(x): return ("−" if x < 0 else "") + f"${abs(rnd(x/1e6,1))}M"
chk("A15", "base", f"Base case {m1(rev[4])} {m1(op[4])} Lowest ${int(rnd(low/1000))}K", a15)
chk("A15", "lenders late", f"Lenders twelve months later {m1s(late['rev5'])} {m1s(late['e5'])} Lowest ${int(rnd(late['low']/1000))}K", a15)
chk("A15", "no lender", f"No lender in five years {m1s(none_['rev5'])} {m1s(none_['e5'])} Hiring for lenders stops by {none_['neg']}", a15)
chk("A15", "retention", f"Each lender stops after three years {m1s(ret['rev5'])} {m1s(ret['e5'])} Lowest ${int(rnd(ret['low']/1000))}K", a15)
chk("A15", "seed at 21", f"Seed at month 21 {m1(rev[4])} {m1(op[4])} Below zero from {s21['neg']}", a15)
chk("A15", "seed 1.5", f"Seed of $1.5M {m1(rev[4])} {m1(op[4])} Lowest ${int(rnd(s15['low']/1000))}K", a15)
chk("A15", "no seed", f"No seed {m1(rev[4])} {m1(op[4])} Below zero, months {nos['neg'].split()[1]} to", a15)
chk("A15", "combined", f"{m1s(comb['rev5'])} {m1s(comb['e5'])} Below zero from {comb['neg']}", a15)
chk("A15", "seed needed by", f"it needs to land by month {need_by}", a15)
# A16, A10
a16, a16n = text("apx-round")
chk("A16", "runway", f"covers {RW} months of costs before any revenue", a16); chk("A16", "seed by", f"needed by month {need_by}", a16); chk("A16", "lowest cash", f"cash stays above ${int(rnd(low/1000))}K", a16)
bad = [c for c in checks if not c[0]]
for ok, where, label, shown in checks:
    print(("ok  " if ok else "FAIL"), f"{where:9s}", label, "|", shown[:110])
print(f"\n{len(checks)} checks, {figs} figures, {len(bad)} failed")
sys.exit(1 if bad else 0)
