"""Tie every model-derived figure on slide 11, slide 13 (notes), A5 and A6 to the workbook.
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
# slide 11 tiles and footer
tam, sam, som = mv("Total market (TAM)"), mv("Serviceable market (SAM)"), mv("Obtainable (SOM): annualised revenue at month 60, Base")
chk("11", "TAM tile", f"${int(rnd(tam))}M Total market", ec)
chk("11", "SAM tile", f"${int(rnd(sam))}M Serviceable", ec)
chk("11", "SOM tile", f"${rnd(som,1)}M Obtainable", ec)
chk("11", "SOM share", f"About {int(rnd(som/tam*100))}% of Australia", ec)
chk("11", "live jobs Australia (about 4,300)", "About 4,300 live jobs", ec); assert round(mv("Live projects in scope, Australia"), -2) == 4300
chk("11", "live jobs Queensland (about 820)", "About 820 live jobs", ec); assert round(mv("Live projects in scope, Queensland"), -1) == 820
chk("11", "about 370 facilities; 92 jobs", "about 370 facilities; seventeen builders on 92 jobs", ec); assert round(fac[4], -1) == 370 and round(jobs[4]) == 92 and round(bld[4]) == 17 and round(len_[4]) == 20
chk("11", "lenders at year end", " / ".join(str(int(rnd(x))) for x in len_) + " lenders", ec)
chk("11", "facilities at year end", " / ".join(str(int(rnd(x))) for x in fac) + " facilities", ec)
chk("11", "team", "team " + " / ".join(str(int(rnd(x))) for x in team), ec)
fa = [iv("Average facility under IRIS, full debt stack", c) for c in (2, 3, 4)]
chk("11", "average facility, base", f"facilities averaging ${int(rnd(fa[0]))}M", ec)
chk("11", "upside and conservative", f"Year 5 upside ${int(rnd(sv('Total revenue',1)[4]/1e6))}M on ${int(rnd(fa[1]))}M facilities, conservative ${rnd(sv('Total revenue',2)[4]/1e6,1)}M on ${int(rnd(fa[2]))}M", ec)
assert min(S.cell(row=srow("Cash at year end, with seed"), column=c).value for c in list(range(2,7))+list(range(8,13))+list(range(14,19))) > 0
assert ue("First month cash with seed goes negative, base") == 99 and ue("First month cash goes negative, conservative") == 99
checks.append((True, "11", "cash positive with the seed in all three cases (year ends; base and conservative month by month)", "check"))
# slide 11 notes
chk("11 notes", "Year 1 costs", f"Year 1 costs (${k(cost[0])}K)", ecn)
chk("11 notes", "facility basis", f"average ${int(rnd(fa[0]))}M across the whole debt stack (senior alone or senior with mezzanine), entered directly by case", ecn)
chk("11 notes", "fee per facility", f"${int(ue('Annualised fee per facility')):,} a year at 15 bps", ecn)
# slide 13 notes
chk("13 notes", "Year 1 costs and revenue", f"${k(cost[0])}K against $650K of spend lines here; Year 1 revenue of ${k(rev[0])}K", ran)
uof = [("Enterprise product build", "$320K"), ("Founder salaries", "$224K"), ("Security audit, cloud and models", "$46K"), ("Sales, marketing and customer success", "$20K"), ("Legal, accounting and IP", "$20K"), ("Contingency and insurance", "$20K"), ("Runway reserve to the seed", "$100K")]
for lab, shown in uof:
    r = srow(lab, S, 8); v = S.cell(row=r, column=12).value
    chk("13", f"use of funds: {lab}", f"{lab if lab!='Founder salaries' else 'Founder salaries, full-time, with super'} {shown}", ra); assert f"${int(v/1000)}K" == shown
# A5
chk("A5", "market facility", f"15 bps on ${int(rnd(iv('Average facility across the market')))}M", a5)
chk("A5", "price per job", f"${int(mv('Facility fee per facility a year')/1000)}K · ${int(mv('Builder subscription per job a year')/1000)}K", a5)
chk("A5", "revenue potential", f"${int(rnd(tam))}M ${int(rnd(sam))}M", a5)
chk("A5", "heading and standfirst", f"${int(rnd(tam))}M market", a5); chk("A5", "Queensland", f"${int(rnd(sam))}M in Queensland", a5)
chk("A5", "live jobs", f"{int(round(mv('Live projects in scope, Australia'),-1)):,} {int(round(mv('Live projects in scope, Queensland'),-1))}", a5)
chk("A5", "value under construction", f"${int(rnd(mv('Value under construction in scope, Australia')))}bn", a5)
chk("A5", "developer-funded", f"${int(rnd(mv('Developer-funded value under construction')))}bn", a5)
chk("A5 notes", "facilities and builder jobs", f"{int(round(mv('of which developer-funded'),-1)):,} developer-funded jobs at ${int(mv('Facility fee per facility a year')):,}", a5n)
# A6
r3 = lambda xs: " ".join(str(int(rnd(xs[i]))) for i in (0, 2, 4))
chk("A6", "lenders Y1/Y3/Y5", "A company target. " + r3(len_), a6)
chk("A6", "facilities Y1/Y3/Y5", "plus its book " + r3(fac), a6)
chk("A6", "fee", f"15 bps on ${int(rnd(fa[0]))}M. Bull ${int(rnd(fa[1]))}M, bear ${int(rnd(fa[2]))}M ${int(ue('Annualised fee per facility')/1000)}K", a6)
chk("A6", "builder jobs Y1/Y3/Y5", "$3,500 a month each " + r3(jobs), a6)
chk("A6", "assessments Y3/Y5", f"– {int(rnd(sv('Assessments in the year')[2]))} {int(rnd(sv('Assessments in the year')[4]))}", a6)
chk("A6", "team Y1/Y3/Y5", "month 15 " + r3(team), a6)
chk("A6", "revenue Y1/Y3/Y5", " ".join(m2(rev[i]) for i in (0, 2, 4)), a6)
chk("A6", "each $10M of facility", f"each $10M of average facility is about ${rnd(rev_f[4]/fa[0]*10/1e6,1)}M of Year 5 revenue", a6)
chk("A6 notes", "fees per mature lender", f"ach mature lender is about ${rnd(ue('Annualised facility fees per lender at month 60')/1e6,1)}M a year of fees (about {int(rnd(ue('Facilities per lender at month 60')))} facilities)", a6n)
chk("A6 notes", "each basis point", f"each basis point of fee is about ${rnd(ue('Year 5 lender revenue for each basis point of fee')/1e6,1)}M in Year 5", a6n)
chk("A6 notes", "revenue list", "revenue " + " / ".join(m2(x) for x in rev), a6n)
chk("A6 notes", "EBITDA list", "EBITDA " + " / ".join(m2(x) for x in op), a6n)
chk("A6 notes", "upside and conservative", f"Upside ${int(rnd(sv('Total revenue',1)[4]/1e6))}M and conservative ${rnd(sv('Total revenue',2)[4]/1e6,1)}M in Year 5", a6n)
chk("A6 notes", "facility by case", f"average ${int(rnd(fa[0]))}M in the base case, ${int(rnd(fa[1]))}M in the upside and ${int(rnd(fa[2]))}M in the conservative case", a6n)
chk("A6 notes", "Years 2 and 4", f"{int(rnd(len_[1]))} and {int(rnd(len_[3]))} lenders on {int(rnd(fac[1]))} and {int(rnd(fac[3]))} facilities; {int(rnd(jobs[1]))} and {int(rnd(jobs[3]))} paid builder jobs; {int(rnd(team[1]))} and {int(rnd(team[3]))} people", a6n)
assert fa == [80, 102, 48] and iv("Project debt stack as a multiple", 4) == 1.2
bad = [c for c in checks if not c[0]]
for ok, where, label, shown in checks:
    print(("ok  " if ok else "FAIL"), f"{where:9s}", label, "|", shown[:110])
print(f"\n{len(checks)} checks, {figs} figures, {len(bad)} failed")
sys.exit(1 if bad else 0)
