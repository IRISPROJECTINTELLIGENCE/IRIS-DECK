"""Build the IRIS market and revenue model workbook (openpyxl, formulas only).

Run: python3 build_model.py <output.xlsx>
All inputs live on the Inputs sheet. Every other number is a formula.
"""
import sys
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter as CL
from openpyxl.comments import Comment

OUT = sys.argv[1]
FONT = "Arial"
BLUE, BLACK, GREEN, GREY, RED = "0000FF", "000000", "008000", "6F6A63", "C00000"


def font(color=BLACK, bold=False, italic=False, size=10):
    return Font(name=FONT, color=color, bold=bold, italic=italic, size=size)


FILL_HDR = PatternFill("solid", fgColor="F2F2F2")
FILL_SEC = PatternFill("solid", fgColor="E7E2D8")
FILL_KEY = PatternFill("solid", fgColor="FFFF00")
FILL_OUT = PatternFill("solid", fgColor="FBE9E4")
THIN = Side(style="thin", color="BFBFBF")
TOPLINE = Border(top=Side(style="thin", color="000000"))

F_MONEY = '$#,##0;($#,##0);"-"'
F_MONEY_M = '$#,##0.0;($#,##0.0);"-"'
F_BN = '#,##0.0;(#,##0.0);"-"'
F_PCT = '0.0%;(0.0%);"-"'
F_CNT = '#,##0;(#,##0);"-"'
F_CNT1 = '#,##0.0;(#,##0.0);"-"'
F_NUM = '#,##0.0;(#,##0.0);"-"'
F_INT = '0'

wb = openpyxl.Workbook()

# ---------------------------------------------------------------- Inputs
wi = wb.active
wi.title = "Inputs"
REF = {}  # key -> row on Inputs


def setw(ws, widths):
    for col, w in widths.items():
        ws.column_dimensions[col].width = w


setw(wi, {"A": 58, "B": 14, "C": 14, "D": 16, "E": 13, "F": 110})
wi["A1"] = "IRIS market and revenue model: inputs"
wi["A1"].font = font(bold=True, size=14)
wi["A2"] = ("Blue cells are inputs; change them here and the other sheets recalculate. "
            "Yellow cells are open decisions. A$, excluding GST. Month 1 is the month the round closes.")
wi["A2"].font = font(GREY, italic=True)
hdr = ["Input", "Base", "Conservative", "Unit", "Type", "Source or basis"]
for i, h in enumerate(hdr, 1):
    c = wi.cell(row=4, column=i, value=h)
    c.font = font(bold=True)
    c.fill = FILL_HDR
wi.freeze_panes = "A5"
row = 5


def section(title):
    global row
    row += 1
    c = wi.cell(row=row, column=1, value=title)
    c.font = font(bold=True)
    for col in range(1, 7):
        wi.cell(row=row, column=col).fill = FILL_SEC
    row += 1


def inp(key, label, base, cons, unit, typ, source, fmt, key_decision=False):
    """cons=None means the input is shared by both cases (column C left blank)."""
    global row
    wi.cell(row=row, column=1, value=label).font = font()
    b = wi.cell(row=row, column=2, value=base)
    b.font = font(BLUE)
    b.number_format = fmt
    if cons is not None:
        c = wi.cell(row=row, column=3, value=cons)
        c.font = font(BLUE)
        c.number_format = fmt
    else:
        c = wi.cell(row=row, column=3, value="same")
        c.font = font(GREY, italic=True)
        c.alignment = Alignment(horizontal="right")
    wi.cell(row=row, column=4, value=unit).font = font(GREY)
    wi.cell(row=row, column=5, value=typ).font = font(GREY)
    s = wi.cell(row=row, column=6, value=source)
    s.font = font(GREY)
    s.alignment = Alignment(wrap_text=True, vertical="top")
    if key_decision:
        b.fill = FILL_KEY
        if cons is not None:
            c.fill = FILL_KEY
    REF[key] = row
    row += 1


def note(text):
    global row
    c = wi.cell(row=row, column=1, value=text)
    c.font = font(GREY, italic=True)
    row += 1


V = __import__("json").load(open(sys.argv[2])) if len(sys.argv) > 2 else {}


def v(key, default):
    return V.get(key, default)


IB19 = "IBISWorld E3019 Multi-Unit Apartment and Townhouse Construction in Australia (2026)"
IB21 = "IBISWorld E3021 Commercial and Industrial Building Construction in Australia (2026)"

section("1. Building work a year, Australia (straight from IBISWorld)")
inp("mu_med", "Multi-unit: medium-rise flats and units (4–8 storeys)", 18.9, None, "A$bn a year", "Reported",
    IB19 + ", products and services segmentation, 2025-26: $18.9bn (30.7%).", F_BN)
inp("mu_high", "Multi-unit: high-rise and super high-rise apartments (9+ storeys)", 14.6, None, "A$bn a year", "Reported",
    IB19 + ", 2025-26: $14.6bn (23.7%).", F_BN)
inp("mu_low", "Multi-unit: low-rise apartments (1–3 storeys)", 4.2, None, "A$bn a year", "Reported",
    IB19 + ", 2025-26: $4.2bn (6.9%). Out of scope: mostly jobs under $10M.", F_BN)
inp("mu_town", "Multi-unit: townhouses, other dwellings and conversions", 23.8, None, "A$bn a year", "Reported",
    IB19 + ", 2025-26: $23.8bn (38.7%). Out of scope: mostly small jobs by house builders.", F_BN)
inp("ci_ind", "C&I: factory and industrial buildings", 19.4, None, "A$bn a year", "Reported",
    IB21 + ", products and services segmentation, 2026-27: $19.4bn (27.4%).", F_BN)
inp("ci_off", "C&I: offices", 16.2, None, "A$bn a year", "Reported", IB21 + ", 2026-27: $16.2bn (22.8%).", F_BN)
inp("ci_ret", "C&I: retail buildings", 11.8, None, "A$bn a year", "Reported", IB21 + ", 2026-27: $11.8bn (16.7%).", F_BN)
inp("ci_ent", "C&I: entertainment and recreational buildings", 6.0, None, "A$bn a year", "Reported",
    IB21 + ", 2026-27: $6.0bn (8.4%).", F_BN)
inp("ci_hot", "C&I: hotels", 4.8, None, "A$bn a year", "Reported", IB21 + ", 2026-27: $4.8bn (6.8%).", F_BN)
inp("ci_oth", "C&I: other business premises", 12.7, None, "A$bn a year", "Reported", IB21 + ", 2026-27: $12.7bn (17.9%).", F_BN)

section("2. Scope, who funds it, and Queensland")
inp("ci_big", "Share of C&I building work on jobs of $10M or more", 0.65, None, "% of value", "Estimate",
    "Estimate; IBISWorld does not split by job size. Cross-check: the top 50 builders alone started 722 projects worth $43.9bn in 2025, "
    "averaging about $61M (Hubexo Construction League, April 2026).", F_PCT)
inp("mu_dev", "Multi-unit work funded by developers", 0.880, None, "% of value", "Reported",
    IB19 + ", major markets, 2025-26: large developers and REITs 48.8% plus owners and small developers 39.2%.", F_PCT)
inp("ci_dev", "C&I work funded by developers", 0.731, None, "% of value", "Reported",
    IB21 + ", major markets, 2026-27: commercial property developers 59.8% plus industrial property developers 13.3%. "
    "End users (23.3%) mostly fund from their own balance sheets.", F_PCT)
inp("q_mu", "Queensland share of multi-unit building work", 0.196, None, "% of value", "Reported",
    IB19 + ", geographic breakdown: Queensland 19.6% of the value of apartment and townhouse work done, 2024-25.", F_PCT)
inp("q_ci", "Queensland share of C&I building work", 0.182, None, "% of value", "Reported (proxy)",
    IB21 + ", geographic breakdown: Queensland has 18.2% of establishments, and its share of work done is below its one-fifth population share. "
    "Used as the proxy until ABS state tables are pulled.", F_PCT)

section("3. From building work to live projects and facilities")
inp("build_mu", "Average build period, apartments", 29, None, "months", "Measured",
    "ABS average completion time for apartments, FY2025-26: 9.54 quarters, about 29 months (10.03 quarters in Queensland), "
    "via The Good Builder citing the ABS data cube, October 2026.", F_INT)
inp("build_ci", "Average build period, C&I jobs of $10M or more", 24, None, "months", "Estimate",
    "Estimate. Cross-check: ABS non-residential work yet to be done was $76.4bn at March 2026 against about $70bn of work a year (ABS).", F_INT)
inp("proj_val", "Average contract value, jobs of $10M or more", 40, None, "A$M", "Estimate",
    "Estimate. Cross-checks: Brisbane and Gold Coast apartment projects on hold average about $48M (PRD via The Good Builder, September 2026); "
    "Qualitas senior construction loans average about $39M (June 2026); the top 50 builders' 2025 starts averaged about $61M (Hubexo).", F_NUM)
inp("fac_ratio", "Construction facility as a share of the build contract", 1.0, None, "x", "Estimate",
    "Estimate. Lenders fund about 60–80% of total development cost (banks 60–70%, non-banks 75–80%: Feasly and Vertex Capital, 2026), "
    "and the build is roughly two-thirds of that cost, so the facility is about the size of the build contract.", '0.00"x"')
inp("sec_pct", "Contract security held on a live job", 0.05, None, "% of contract", "Estimate",
    "Estimate: 5% security is common under AS 4000-style head contracts. Used for the insurer and surety memo line, which is not counted.", F_PCT)
inp("surety_fee", "Surety and bank guarantee fee", 0.01, None, "% a year", "Reported",
    "Brokers quote 0.5–1.5% a year for surety and 0.5–2% for bank guarantees (BCS Broking, 2026). Memo line, not counted.", F_PCT)
inp("qs_dev", "Developers' spend on quantity surveying services", 711, None, "A$M a year", "Reported",
    "IBISWorld OD5428 Quantity Surveying Services in Australia (2026), major markets, 2025-26: property developers $711.0m (26.7%). Context, not counted.", F_CNT)

section("4. Pricing")
inp("price_b", "Builder subscription, per project", v("price_b", 3500), v("price_b_c", 3500), "A$ a month", "Company",
    "Company pricing for builder deployments (slide 10).", F_MONEY)
inp("bps", "Facility fee", 15, 12.5, "bps a year", "Company",
    "Charged on the facility limit, paid by the developer as a condition of the facility. Range tested: 10–20 bps.", '0.0')
inp("fee_floor", "Facility fee floor", 3500, 3500, "A$ a month", "Company",
    "Floor so a small facility pays no less than a builder subscription.", F_MONEY)
inp("fee_cap", "Facility fee cap", 10000, 10000, "A$ a month", "Company",
    "Cap so the fee stays proportionate on large facilities (Textura caps its fee for the same reason).", F_MONEY)
inp("fac_avg", "Average facility, first lenders", 35, 30, "A$M", "Estimate",
    "Estimate for South East Queensland facilities. Qualitas senior construction loans average about $39M (June 2026); "
    "Brisbane apartment projects on hold average about $35M (PRD, September 2026).", F_NUM)

section("5. Builder deployments")
inp("rd_start", "R&D deployments go live", 3, 3, "month", "Company", "Slide 17: two builder deployments live by month 3.", F_INT)
inp("rd_n", "R&D deployments", 2, 2, "projects", "Company", "Slide 17.", F_INT)
inp("paid_start", "Builder deployments start paying", 6, 7, "month", "Company",
    "After the position reconciles to the builder's own cost reports.", F_INT)
inp("add_y1", "New paid builder projects a month, Year 1", 1.0, 0.5, "projects a month", "Company", "Founder-led sales, after the first paid month.", "0.00")
inp("add_y2", "New paid builder projects a month, Year 2", 1.25, 0.75, "projects a month", "Company", "With a commercial lead once the seed round closes.", "0.00")
inp("add_y3", "New paid builder projects a month, Year 3", 1.5, 1.0, "projects a month", "Company", "", "0.00")
inp("churn", "Paid builder projects lost a month", 0.01, 0.02, "% a month", "Estimate",
    "Projects end, but builders usually move the subscription to their next job.", F_PCT)

section("6. Lender mandates")
inp("l1", "Lender 1 (design partner): first facility under the condition", 12, 18, "month", "Company", "Slide 17: first facility at month 12.", F_INT)
inp("l2", "Lender 2 starts", 21, 27, "month", "Company", "Lenders 2 onwards follow a live result at lender 1. 999 means not in this case.", F_INT)
inp("l3", "Lender 3 starts", 27, 33, "month", "Company", "", F_INT)
inp("l4", "Lender 4 starts", 33, 999, "month", "Company", "", F_INT)
inp("l5", "Lender 5 starts", 999, 999, "month", "Company", "", F_INT)
inp("per_lender", "New facilities under the condition, per lender a month", 0.75, 0.5, "facilities a month", "Estimate",
    "New facilities, extensions and refinances; the condition goes on when a loan is papered.", "0.00")
inp("fac_term", "Facility term", 24, 24, "months", "Estimate", "Facilities leave the count at completion.", F_INT)

section("7. Team")
inp("n_found", "Founders, full-time from month 1", 2, 2, "people", "Company", "", F_INT)
inp("sal_found", "Founder salary, each", v("sal_found", 100000), v("sal_found_c", 100000), "A$ a year", "Open decision",
    "Pending the founders' decision on the round and salaries.", F_MONEY, key_decision=True)
inp("oncost", "On-costs on salaries", 0.12, 0.12, "% of salary", "Reported",
    "Superannuation guarantee, 12% from 1 July 2025. Payroll tax stays below the Queensland threshold in these years.", F_PCT)
note("Hires: salary and the month each role starts (999 = not hired in that case). Edit in the table below.")
row += 1
hires_hdr_row = row
for i, h in enumerate(["Role", "Salary (A$)", "Base start", "Cons. start", "", "Why"], 1):
    c = wi.cell(row=row, column=i, value=h)
    c.font = font(bold=True)
    c.fill = FILL_HDR
row += 1
HIRES = [
    ("Commercial lead (lenders and builders)", 160000, 16, 19, "Runs lender onboarding and builder sales. Hired once the seed round closes."),
    ("Engineer 1 (integrations)", 170000, 16, 19, "Connectors and platform reliability as live projects grow."),
    ("Deployment analyst 1", 110000, 16, 22, "Onboards projects; checks each position against source records."),
    ("Engineer 2", 160000, 22, 28, ""),
    ("Deployment analyst 2", 110000, 25, 31, ""),
    ("Engineer 3", 160000, 28, 999, ""),
    ("Deployment analyst 3", 110000, 31, 999, ""),
]
hire_first = row
for role, sal, sb, sc, why in HIRES:
    wi.cell(row=row, column=1, value=role).font = font()
    for col, val, fmt in ((2, sal, F_MONEY), (3, sb, F_INT), (4, sc, F_INT)):
        c = wi.cell(row=row, column=col, value=val)
        c.font = font(BLUE)
        c.number_format = fmt
    wi.cell(row=row, column=6, value=why).font = font(GREY)
    row += 1
hire_last = row - 1
REF["hire_sal"] = (hire_first, hire_last)

section("8. Other costs")
inp("build_y1", "Platform build and R&D, Year 1 (contract engineering)", v("build_y1", 170000), v("build_y1_c", 170000), "A$ a year", "Open decision",
    "From the use of funds on slide 17; moves with the round.", F_MONEY, key_decision=True)
inp("ext_y2", "Contract engineering, Year 2", 60000, 40000, "A$ a year", "Estimate", "", F_MONEY)
inp("ext_y3", "Contract engineering, Year 3", 60000, 40000, "A$ a year", "Estimate", "", F_MONEY)
inp("cloud_fix", "Cloud, models and tools, fixed", v("cloud_fix", 800), v("cloud_fix_c", 800), "A$ a month", "Estimate", "Hosting, monitoring, development tools.", F_MONEY)
inp("cloud_var", "Cloud and model use, per live project or facility", 150, 200, "A$ a month", "Estimate",
    "Model inference, storage and connectors per live job.", F_MONEY)
inp("sec_y1", "Security certification, Year 1", v("sec_y1", 30000), v("sec_y1_c", 30000), "A$", "Estimate", "ISO 27001 or SOC 2, needed for lender onboarding by month 6.", F_MONEY)
inp("sec_on", "Security audits, from Year 2", 20000, 20000, "A$ a year", "Estimate", "Surveillance audits and penetration testing.", F_MONEY)
inp("ins_y1", "Insurance, Year 1", v("ins_y1", 10000), v("ins_y1_c", 10000), "A$ a year", "Estimate", "Professional indemnity and cyber; inside the contingency line of the use of funds.", F_MONEY)
inp("ins_y2", "Insurance, Year 2", 30000, 30000, "A$ a year", "Estimate", "Lender reliance raises professional indemnity cover.", F_MONEY)
inp("ins_y3", "Insurance, Year 3", 45000, 45000, "A$ a year", "Estimate", "", F_MONEY)
inp("sm_y1", "Sales and customer success, Year 1", v("sm_y1", 20000), v("sm_y1_c", 20000), "A$ a year", "Estimate", "From the use of funds on slide 17.", F_MONEY)
inp("sm_y2", "Sales and customer success, Year 2", 80000, 60000, "A$ a year", "Estimate", "", F_MONEY)
inp("sm_y3", "Sales and customer success, Year 3", 150000, 100000, "A$ a year", "Estimate", "", F_MONEY)
inp("lg_y1", "Legal, accounting and IP, Year 1", v("lg_y1", 20000), v("lg_y1_c", 20000), "A$ a year", "Estimate", "From the use of funds on slide 17.", F_MONEY)
inp("lg_y2", "Legal, accounting and IP, Year 2", 40000, 40000, "A$ a year", "Estimate", "", F_MONEY)
inp("lg_y3", "Legal, accounting and IP, Year 3", 60000, 60000, "A$ a year", "Estimate", "", F_MONEY)
inp("cont_y1", "Contingency, Year 1", v("cont_y1", 10000), v("cont_y1_c", 10000), "A$", "Open decision", "Use of funds contingency line, less the Year 1 insurance shown above.", F_MONEY, key_decision=True)
inp("cont_pct", "Contingency, Years 2–3", 0.05, 0.05, "% of costs", "Estimate", "", F_PCT)

section("9. Funding")
inp("safe", "This round (SAFE), received month 1", v("safe", 500000), v("safe_c", 500000), "A$", "Owner decision D-21 (30 Oct 2026)",
    "Pending the founders' decision on round size and cap.", F_MONEY, key_decision=True)
inp("seed", "Seed round", v("seed", 3000000), v("seed_c", 3000000), "A$", "Company", "Slide 17: seed raise in months 15–18 on the mandate result.", F_MONEY)
inp("seed_m", "Seed round received", 15, 18, "month", "Company", "Slide 17: months 15–18, after the first facility under the condition.", F_INT)
inp("tax_r", "R&D tax incentive refund (not counted)", 0, 0, "A$", "Company",
    "Left at zero: the refundable R&D offset would add cash in the year after spend, but is not counted here.", F_MONEY)

INPUT_LAST = row

# ---------------------------------------------------------------- monthly sheets
MONTHS = 36
C0 = 3  # column C = month 1
CLAST = C0 + MONTHS - 1  # column AL
YCOL = {1: CLAST + 2, 2: CLAST + 3, 3: CLAST + 4}  # AN, AO, AP


def mcol(m):
    return CL(C0 + m - 1)


def I(key, scen):
    col = "B" if scen == "base" else "C"
    return f"Inputs!${col}${REF[key]}"


def build_month_sheet(ws, scen, title):
    setw(ws, {"A": 46, "B": 12})
    for m in range(1, MONTHS + 1):
        ws.column_dimensions[mcol(m)].width = 10.5
    ws.column_dimensions[CL(CLAST + 1)].width = 3
    for y in (1, 2, 3):
        ws.column_dimensions[CL(YCOL[y])].width = 13
    ws["A1"] = title
    ws["A1"].font = font(bold=True, size=14)
    ws["A2"] = "Monthly drivers, revenue, costs and cash. All formulas; inputs are on the Inputs sheet. A$."
    ws["A2"].font = font(GREY, italic=True)
    ws.freeze_panes = "C5"
    R = {}

    def label(r, text, bold=False, unit=""):
        ws.cell(row=r, column=1, value=text).font = font(bold=bold)
        if unit:
            ws.cell(row=r, column=2, value=unit).font = font(GREY)

    # header rows
    label(3, "Month", True)
    label(4, "Year", True)
    for m in range(1, MONTHS + 1):
        c = ws.cell(row=3, column=C0 + m - 1)
        c.value = 1 if m == 1 else f"={mcol(m-1)}3+1"
        c.font = font(bold=True)
        c.fill = FILL_HDR
        c.alignment = Alignment(horizontal="right")
        y = ws.cell(row=4, column=C0 + m - 1, value=f"=ROUNDUP({mcol(m)}3/12,0)")
        y.font = font(GREY)
        y.alignment = Alignment(horizontal="right")
    for yy in (1, 2, 3):
        c = ws.cell(row=3, column=YCOL[yy], value=f"Year {yy}")
        c.font = font(bold=True)
        c.fill = FILL_HDR
        c.alignment = Alignment(horizontal="right")
        ws.cell(row=4, column=YCOL[yy], value="total or year end").font = font(GREY, italic=True)

    r = 6
    rows = []

    def row_def(key, text, unit, fn, fmt, kind="flow", bold=False, topline=False):
        nonlocal r
        R[key] = r
        rows.append((key, r, text, unit, fn, fmt, kind, bold, topline))
        r += 1

    def blank(title=None):
        nonlocal r
        if title:
            R["_" + title] = r
            rows.append(("_sec", r, title, "", None, None, "section", True, False))
        r += 1

    blank("Builder deployments")
    row_def("rd", "R&D deployments live (unpaid)", "projects",
            lambda m, p: f"=IF(AND({m}$3>={I('rd_start',scen)},{m}$3<{I('paid_start',scen)}),{I('rd_n',scen)},0)", F_CNT1, "stock")
    row_def("adds", "New paid builder projects", "projects",
            lambda m, p: f"=IF({m}$3<={I('paid_start',scen)},0,CHOOSE({m}$4,{I('add_y1',scen)},{I('add_y2',scen)},{I('add_y3',scen)}))", F_CNT1)
    row_def("paid", "Paid builder projects, end of month", "projects",
            lambda m, p: (f"=IF({m}$3<{I('paid_start',scen)},0,IF({m}$3={I('paid_start',scen)},{I('rd_n',scen)},"
                          f"{(p + str(R['paid'])) if p else '0'}*(1-{I('churn',scen)})+{m}{R['adds']}))"), F_CNT1, "stock")
    row_def("rev_b", "Builder subscription revenue", "A$",
            lambda m, p: f"={m}{R['paid']}*{I('price_b',scen)}", F_MONEY)
    blank()
    blank("Lender mandates")
    row_def("lenders", "Lenders with the condition", "lenders",
            lambda m, p: f"=COUNTIF(Inputs!${'B' if scen=='base' else 'C'}${REF['l1']}:${'B' if scen=='base' else 'C'}${REF['l5']},\"<=\"&{m}$3)", F_CNT, "stock")
    row_def("newf", "New facilities under the condition", "facilities",
            lambda m, p: f"={m}{R['lenders']}*{I('per_lender',scen)}", F_CNT1)
    row_def("endf", "Facilities completing", "facilities",
            lambda m, p: f"=IF({m}$3>{I('fac_term',scen)},INDEX(${mcol(1)}${R['newf']}:${mcol(MONTHS)}${R['newf']},1,{m}$3-{I('fac_term',scen)}),0)", F_CNT1)
    row_def("livef", "Facilities under the condition, end of month", "facilities",
            lambda m, p: f"={(p + str(R['livef']) + '+') if p else ''}{m}{R['newf']}-{m}{R['endf']}", F_CNT1, "stock")
    row_def("fee_f", "Fee per facility", "A$ a month",
            lambda m, p: (f"=MIN(MAX({I('fac_avg',scen)}*1000000*{I('bps',scen)}/10000/12,{I('fee_floor',scen)}),{I('fee_cap',scen)})"), F_MONEY, "stock")
    row_def("rev_f", "Facility fee revenue", "A$",
            lambda m, p: f"={m}{R['livef']}*{m}{R['fee_f']}", F_MONEY)
    blank()
    row_def("rev", "Total revenue", "A$", lambda m, p: f"={m}{R['rev_b']}+{m}{R['rev_f']}", F_MONEY, bold=True, topline=True)
    row_def("arr", "Annualised revenue (month × 12)", "A$", lambda m, p: f"={m}{R['rev']}*12", F_MONEY, "stock")
    blank()
    blank("Team and costs")
    hs = "C" if scen == "base" else "D"
    hr = f"Inputs!${hs}${hire_first}:${hs}${hire_last}"
    hsal = f"Inputs!$B${hire_first}:$B${hire_last}"
    row_def("head", "Team, end of month", "people",
            lambda m, p: f"={I('n_found',scen)}+COUNTIF({hr},\"<=\"&{m}$3)", F_CNT, "stock")
    row_def("c_found", "Founders", "A$", lambda m, p: f"={I('n_found',scen)}*{I('sal_found',scen)}/12*(1+{I('oncost',scen)})", F_MONEY)
    row_def("c_hire", "Hires", "A$", lambda m, p: f"=SUMPRODUCT(({hr}<={m}$3)*{hsal})/12*(1+{I('oncost',scen)})", F_MONEY)
    row_def("c_build", "Platform build and contract engineering", "A$",
            lambda m, p: f"=CHOOSE({m}$4,{I('build_y1',scen)},{I('ext_y2',scen)},{I('ext_y3',scen)})/12", F_MONEY)
    row_def("c_cloud", "Cloud, models and tools", "A$",
            lambda m, p: f"={I('cloud_fix',scen)}+({m}{R['rd']}+{m}{R['paid']}+{m}{R['livef']})*{I('cloud_var',scen)}", F_MONEY)
    row_def("c_sec", "Security certification and audits", "A$",
            lambda m, p: f"=CHOOSE({m}$4,{I('sec_y1',scen)},{I('sec_on',scen)},{I('sec_on',scen)})/12", F_MONEY)
    row_def("c_ins", "Insurance", "A$", lambda m, p: f"=CHOOSE({m}$4,{I('ins_y1',scen)},{I('ins_y2',scen)},{I('ins_y3',scen)})/12", F_MONEY)
    row_def("c_sm", "Sales and customer success", "A$", lambda m, p: f"=CHOOSE({m}$4,{I('sm_y1',scen)},{I('sm_y2',scen)},{I('sm_y3',scen)})/12", F_MONEY)
    row_def("c_lg", "Legal, accounting and IP", "A$", lambda m, p: f"=CHOOSE({m}$4,{I('lg_y1',scen)},{I('lg_y2',scen)},{I('lg_y3',scen)})/12", F_MONEY)
    row_def("c_cont", "Contingency", "A$",
            lambda m, p: f"=IF({m}$4=1,{I('cont_y1',scen)}/12,{I('cont_pct',scen)}*SUM({m}{R['c_found']}:{m}{R['c_lg']}))", F_MONEY)
    row_def("cost", "Total costs", "A$", lambda m, p: f"=SUM({m}{R['c_found']}:{m}{R['c_cont']})", F_MONEY, bold=True, topline=True)
    blank()
    row_def("op", "Operating result", "A$", lambda m, p: f"={m}{R['rev']}-{m}{R['cost']}", F_MONEY, bold=True)
    blank()
    blank("Cash")
    row_def("in_safe", "This round", "A$", lambda m, p: f"=IF({m}$3=1,{I('safe',scen)},0)", F_MONEY)
    row_def("cash0", "Cash before the seed round, end of month", "A$",
            lambda m, p: f"={(p + str(R['cash0']) + '+') if p else ''}{m}{R['op']}+{m}{R['in_safe']}", F_MONEY, "stock", bold=True)
    row_def("in_seed", "Seed round", "A$", lambda m, p: f"=IF({m}$3={I('seed_m',scen)},{I('seed',scen)},0)", F_MONEY)
    row_def("cash1", "Cash after the seed round, end of month", "A$",
            lambda m, p: f"={(p + str(R['cash1']) + '+') if p else ''}{m}{R['op']}+{m}{R['in_safe']}+{m}{R['in_seed']}", F_MONEY, "stock")
    row_def("negflag", "Helper: month if cash before seed is negative", "month",
            lambda m, p: f"=IF({m}{R['cash0']}<0,{m}$3,99)", F_INT, "helper")

    for key, rr, text, unit, fn, fmt, kind, bold, topline in rows:
        if kind == "section":
            c = ws.cell(row=rr, column=1, value=text)
            c.font = font(bold=True)
            for col in range(1, YCOL[3] + 1):
                ws.cell(row=rr, column=col).fill = FILL_SEC
            continue
        label(rr, text, bold, unit)
        if kind == "helper":
            ws.cell(row=rr, column=1).font = font(GREY, italic=True)
        for m in range(1, MONTHS + 1):
            col = mcol(m)
            prev = mcol(m - 1) if m > 1 else None
            c = ws.cell(row=rr, column=C0 + m - 1, value=fn(col, prev))
            c.number_format = fmt
            c.font = font(bold=bold, color=(GREY if kind == "helper" else BLACK))
            if topline:
                c.border = TOPLINE
        for yy in (1, 2, 3):
            if kind == "helper":
                continue
            if kind == "stock":
                f = f"=INDEX(${mcol(1)}{rr}:${mcol(MONTHS)}{rr},1,{12*yy})"
            else:
                f = f"=SUMIF(${mcol(1)}$4:${mcol(MONTHS)}$4,{yy},${mcol(1)}{rr}:${mcol(MONTHS)}{rr})"
            c = ws.cell(row=rr, column=YCOL[yy], value=f)
            c.number_format = fmt
            c.font = font(bold=bold)
            c.fill = FILL_OUT
            if topline:
                c.border = TOPLINE
    return R


wsb = wb.create_sheet("Base")
RB = build_month_sheet(wsb, "base", "Base case: monthly")
wsc = wb.create_sheet("Conservative")
RC = build_month_sheet(wsc, "cons", "Conservative case: monthly")

# ---------------------------------------------------------------- Market
wm = wb.create_sheet("Market", 1)
setw(wm, {"A": 62, "B": 16, "C": 14, "D": 110})
wm["A1"] = "Market: total, serviceable and obtainable"
wm["A1"].font = font(bold=True, size=14)
wm["A2"] = ("Built from IBISWorld's figures for the two industries IRIS serves. Green cells link to Inputs; black cells are formulas. "
            "Change inputs on the Inputs sheet.")
wm["A2"].font = font(GREY, italic=True)
for i, h in enumerate(["Line", "Value", "Unit", "How it is worked out"], 1):
    c = wm.cell(row=4, column=i, value=h)
    c.font = font(bold=True)
    c.fill = FILL_HDR
wm.freeze_panes = "A5"
mr = 5
M = {}


def msec(title):
    global mr
    mr += 1
    c = wm.cell(row=mr, column=1, value=title)
    c.font = font(bold=True)
    for col in range(1, 5):
        wm.cell(row=mr, column=col).fill = FILL_SEC
    mr += 1


def mline(key, text, formula, unit, how, fmt, link=False, bold=False, out=False):
    global mr
    wm.cell(row=mr, column=1, value=text).font = font(bold=bold)
    c = wm.cell(row=mr, column=2, value=formula)
    c.number_format = fmt
    c.font = font(GREEN if link else BLACK, bold=bold)
    if out:
        c.fill = FILL_OUT
    wm.cell(row=mr, column=3, value=unit).font = font(GREY)
    h = wm.cell(row=mr, column=4, value=how)
    h.font = font(GREY)
    h.alignment = Alignment(wrap_text=True, vertical="top")
    M[key] = mr
    mr += 1


def ib(key):
    return f"=Inputs!$B${REF[key]}"


def mref(key):
    return f"$B${M[key]}"


msec("A. Building work a year in IRIS's scope (IBISWorld)")
mline("mu_med", "Medium-rise flats and units", ib("mu_med"), "A$bn", "IBISWorld E3019, 2025-26. In scope.", F_BN, link=True)
mline("mu_high", "High-rise and super high-rise apartments", ib("mu_high"), "A$bn", "IBISWorld E3019, 2025-26. In scope.", F_BN, link=True)
mline("mu_low", "Low-rise apartments", ib("mu_low"), "A$bn", "IBISWorld E3019. Out of scope: mostly under $10M a job.", F_BN, link=True)
mline("mu_town", "Townhouses, other dwellings and conversions", ib("mu_town"), "A$bn", "IBISWorld E3019. Out of scope.", F_BN, link=True)
mline("mu_tot", "Multi-unit residential, all segments", f"=SUM(B{M['mu_med']}:B{M['mu_low']})+B{M['mu_town']}", "A$bn",
      "IBISWorld reports $61.4bn; segments sum to $61.5bn through rounding.", F_BN)
mline("ci_tot", "Commercial and industrial building, all segments",
      f"=SUM(Inputs!$B${REF['ci_ind']}:$B${REF['ci_oth']})", "A$bn", "IBISWorld E3021, 2026-27: $70.9bn.", F_BN)
mline("ci_big", "Share of C&I work on jobs of $10M or more", ib("ci_big"), "%", "See Inputs.", F_PCT, link=True)
mline("mu_in", "Multi-unit work in scope", f"={mref('mu_med')}+{mref('mu_high')}", "A$bn", "Medium-rise plus high-rise.", F_BN)
mline("ci_in", "C&I work in scope", f"={mref('ci_tot')}*{mref('ci_big')}", "A$bn", "All C&I segments, jobs of $10M or more.", F_BN)
mline("in_tot", "Building work in scope, Australia", f"={mref('mu_in')}+{mref('ci_in')}", "A$bn a year", "", F_BN, bold=True)

msec("B. From work a year to value under construction")
mline("build_mu", "Average build period, apartments", ib("build_mu"), "months", "ABS, FY2025-26.", F_INT, link=True)
mline("build_ci", "Average build period, C&I", ib("build_ci"), "months", "See Inputs.", F_INT, link=True)
mline("mu_live", "Multi-unit value under construction", f"={mref('mu_in')}*{mref('build_mu')}/12", "A$bn",
      "Work a year × build period: each job is live for its build period.", F_BN)
mline("ci_live", "C&I value under construction", f"={mref('ci_in')}*{mref('build_ci')}/12", "A$bn", "", F_BN)
mline("live_val", "Value under construction in scope, Australia", f"={mref('mu_live')}+{mref('ci_live')}", "A$bn", "", F_BN, bold=True)

msec("C. Who funds it (IBISWorld major markets)")
mline("mu_dev", "Multi-unit work funded by developers", ib("mu_dev"), "%", "IBISWorld E3019.", F_PCT, link=True)
mline("ci_dev", "C&I work funded by developers", ib("ci_dev"), "%", "IBISWorld E3021.", F_PCT, link=True)
mline("dev_live", "Developer-funded value under construction", f"={mref('mu_live')}*{mref('mu_dev')}+{mref('ci_live')}*{mref('ci_dev')}", "A$bn",
      "Where a construction lender can make IRIS a condition of the facility.", F_BN)
mline("oth_live", "Other value under construction", f"={mref('live_val')}-{mref('dev_live')}", "A$bn",
      "End users, government and other owners: no construction facility to condition, so builders pay.", F_BN)

msec("D. Live projects and price per project")
mline("proj_val", "Average contract value, jobs of $10M or more", ib("proj_val"), "A$M", "See Inputs.", F_NUM, link=True)
mline("live_n", "Live projects in scope, Australia", f"=IF({mref('proj_val')}=0,0,{mref('live_val')}*1000/{mref('proj_val')})", "projects",
      "Value under construction ÷ average contract value.", F_CNT, bold=True)
mline("live_dev", "of which developer-funded (facility fee)", f"=IF({mref('proj_val')}=0,0,{mref('dev_live')}*1000/{mref('proj_val')})", "projects", "", F_CNT)
mline("live_oth", "of which other (builder subscription)", f"={mref('live_n')}-{mref('live_dev')}", "projects", "", F_CNT)
mline("fac_ratio", "Facility as a share of the build contract", ib("fac_ratio"), "x", "See Inputs.", '0.00"x"', link=True)
mline("bps", "Facility fee", ib("bps"), "bps a year", "Base case.", '0.0', link=True)
mline("fee_fac", "Facility fee per facility",
      f"=MIN(MAX({mref('proj_val')}*{mref('fac_ratio')}*1000000*{mref('bps')}/10000,Inputs!$B${REF['fee_floor']}*12),Inputs!$B${REF['fee_cap']}*12)",
      "A$ a year", "Average facility × fee, within the floor and cap.", F_MONEY)
mline("fee_b", "Builder subscription per project", f"=Inputs!$B${REF['price_b']}*12", "A$ a year", "", F_MONEY)

msec("E. Market, A$ millions a year")
mline("tam_f", "Facility fees on all developer-funded projects", f"={mref('live_dev')}*{mref('fee_fac')}/1000000", "A$M a year", "", F_MONEY_M)
mline("tam_b", "Builder subscriptions on all other projects", f"={mref('live_oth')}*{mref('fee_b')}/1000000", "A$M a year", "", F_MONEY_M)
mline("tam", "Total market (TAM): Australia, all projects in scope", f"={mref('tam_f')}+{mref('tam_b')}", "A$M a year",
      "All live jobs of $10M or more on IRIS.", F_MONEY_M, bold=True, out=True)
mline("q_mu", "Queensland share of multi-unit work", ib("q_mu"), "%", "IBISWorld E3019.", F_PCT, link=True)
mline("q_ci", "Queensland share of C&I work", ib("q_ci"), "%", "See Inputs.", F_PCT, link=True)
mline("q_dev", "Queensland developer-funded value under construction",
      f"={mref('mu_live')}*{mref('q_mu')}*{mref('mu_dev')}+{mref('ci_live')}*{mref('q_ci')}*{mref('ci_dev')}", "A$bn", "", F_BN)
mline("q_oth", "Queensland other value under construction",
      f"={mref('mu_live')}*{mref('q_mu')}*(1-{mref('mu_dev')})+{mref('ci_live')}*{mref('q_ci')}*(1-{mref('ci_dev')})", "A$bn", "", F_BN)
mline("q_live", "Live projects in scope, Queensland", f"=IF({mref('proj_val')}=0,0,({mref('q_dev')}+{mref('q_oth')})*1000/{mref('proj_val')})", "projects", "", F_CNT)
mline("sam", "Serviceable market (SAM): Queensland, starting in South East Queensland",
      f"=IF({mref('proj_val')}=0,0,({mref('q_dev')}*1000/{mref('proj_val')}*{mref('fee_fac')}+{mref('q_oth')}*1000/{mref('proj_val')}*{mref('fee_b')})/1000000)",
      "A$M a year", "Where the founders work and the first builders and lenders are. South East Queensland is about 79% of the state's building pipeline (CSQ).",
      F_MONEY_M, bold=True, out=True)
mline("som", "Obtainable (SOM): annualised revenue at month 36, base case", f"=Base!${mcol(MONTHS)}${RB['arr']}/1000000", "A$M a year",
      "From the Base sheet: builders and lenders signed by the end of Year 3.", F_MONEY_M, link=True, bold=True, out=True)
mline("som_sh", "SOM as a share of SAM", f"=IF({mref('sam')}=0,0,{mref('som')}/{mref('sam')})", "%", "", F_PCT)
mline("som_c", "Obtainable, conservative case", f"=Conservative!${mcol(MONTHS)}${RC['arr']}/1000000", "A$M a year", "", F_MONEY_M, link=True)

msec("F. Context and what is not counted")
mline("qs_dev", "Developers' spend on quantity surveying services", ib("qs_dev"), "A$M a year", "IBISWorld OD5428, 2025-26.", F_CNT, link=True)
mline("tam_qs", "IRIS total market against that spend", f"=IF({mref('qs_dev')}=0,0,{mref('tam')}/{mref('qs_dev')})", "%", "", F_PCT)
mline("sec_held", "Contract security on live jobs in scope (not counted)", f"={mref('live_val')}*Inputs!$B${REF['sec_pct']}", "A$bn",
      "Value under construction × security share. Insurers and surety providers carry it; IRIS earns nothing from them in this model.", F_BN)
mline("sec_prem", "Fees paid on that security a year (not counted)", f"={mref('sec_held')}*Inputs!$B${REF['surety_fee']}*1000", "A$M a year", "", F_MONEY_M)

# ---------------------------------------------------------------- Summary
ws = wb.create_sheet("Summary", 1)
setw(ws, {"A": 50, "B": 13, "C": 13, "D": 13, "E": 3, "F": 13, "G": 13, "H": 13})
ws["A1"] = "IRIS: three-year summary"
ws["A1"].font = font(bold=True, size=14)
ws["A2"] = "A$ unless stated. Year 1 starts the month the round closes. Linked from the Base and Conservative sheets."
ws["A2"].font = font(GREY, italic=True)
for col, text in ((2, "Base"), (6, "Conservative")):
    c = ws.cell(row=4, column=col, value=text)
    c.font = font(bold=True)
for i, col in enumerate((2, 3, 4, 6, 7, 8)):
    c = ws.cell(row=5, column=col, value=f"Year {i % 3 + 1}")
    c.font = font(bold=True)
    c.fill = FILL_HDR
    c.alignment = Alignment(horizontal="right")
ws.cell(row=5, column=1, value="").fill = FILL_HDR
sr = 6
S = {}


def sline(key, text, src_key, fmt, bold=False, topline=False, combine=None):
    """combine: list of monthly-row keys to add together."""
    global sr
    ws.cell(row=sr, column=1, value=text).font = font(bold=bold)
    for base_col, sheet, RR in ((2, "Base", RB), (6, "Conservative", RC)):
        for yy in (1, 2, 3):
            ycol = CL(YCOL[yy])
            if combine:
                f = "=" + "+".join(f"{sheet}!${ycol}${RR[k]}" for k in combine)
            else:
                f = f"={sheet}!${ycol}${RR[src_key]}"
            c = ws.cell(row=sr, column=base_col + yy - 1, value=f)
            c.number_format = fmt
            c.font = font(GREEN, bold=bold)
            if topline:
                c.border = TOPLINE
    S[key] = sr
    sr += 1


def ssec(title):
    global sr
    sr += 1
    c = ws.cell(row=sr, column=1, value=title)
    c.font = font(bold=True)
    for col in range(1, 9):
        ws.cell(row=sr, column=col).fill = FILL_SEC
    sr += 1


ssec("Revenue")
sline("rev_b", "Builder subscriptions", "rev_b", F_MONEY)
sline("rev_f", "Facility fees (developer-paid, lender condition)", "rev_f", F_MONEY)
sline("rev", "Total revenue", "rev", F_MONEY, bold=True, topline=True)
ssec("Costs")
sline("c_people", "People", None, F_MONEY, combine=["c_found", "c_hire"])
sline("c_plat", "Platform build, cloud and security", None, F_MONEY, combine=["c_build", "c_cloud", "c_sec"])
sline("c_go", "Sales, legal and insurance", None, F_MONEY, combine=["c_sm", "c_lg", "c_ins"])
sline("c_cont", "Contingency", "c_cont", F_MONEY)
sline("cost", "Total costs", "cost", F_MONEY, bold=True, topline=True)
ssec("Result and cash")
sline("op", "Operating result", "op", F_MONEY, bold=True)
sline("cash0", "Cash at year end, before the seed round", "cash0", F_MONEY)
sline("cash1", "Cash at year end, after the seed round", "cash1", F_MONEY)
ssec("Drivers at year end")
sline("paid", "Paid builder projects", "paid", F_CNT)
sline("livef", "Facilities under the condition", "livef", F_CNT)
sline("lenders", "Lenders with the condition", "lenders", F_CNT)
sline("head", "Team", "head", F_CNT)
sline("arr", "Annualised revenue at year end", "arr", F_MONEY, bold=True)

sr += 1
ssec("Funding check")
for text, fn_base, fn_cons, fmt in (
    ("Lowest cash before the seed round", f"=MIN(Base!${mcol(1)}${RB['cash0']}:${mcol(MONTHS)}${RB['cash0']})",
     f"=MIN(Conservative!${mcol(1)}${RC['cash0']}:${mcol(MONTHS)}${RC['cash0']})", F_MONEY),
    ("First month cash runs out without the seed (99 = not within 36 months)", f"=MIN(Base!${mcol(1)}${RB['negflag']}:${mcol(MONTHS)}${RB['negflag']})",
     f"=MIN(Conservative!${mcol(1)}${RC['negflag']}:${mcol(MONTHS)}${RC['negflag']})", F_INT),
    ("Lowest cash after the seed round", f"=MIN(Base!${mcol(1)}${RB['cash1']}:${mcol(MONTHS)}${RB['cash1']})",
     f"=MIN(Conservative!${mcol(1)}${RC['cash1']}:${mcol(MONTHS)}${RC['cash1']})", F_MONEY),
):
    ws.cell(row=sr, column=1, value=text).font = font()
    for col, fn in ((2, fn_base), (6, fn_cons)):
        c = ws.cell(row=sr, column=col, value=fn)
        c.number_format = fmt
        c.font = font(GREEN)
    sr += 1

sr += 1
ssec("Market (from the Market sheet)")
for text, key, fmt in (("Total market (TAM), Australia, A$M a year", "tam", F_MONEY_M),
                       ("Serviceable market (SAM), Queensland, A$M a year", "sam", F_MONEY_M),
                       ("Obtainable (SOM), month-36 annualised revenue, A$M", "som", F_MONEY_M),
                       ("Live projects in scope, Australia", "live_n", F_CNT),
                       ("Live projects in scope, Queensland", "q_live", F_CNT)):
    ws.cell(row=sr, column=1, value=text).font = font()
    c = ws.cell(row=sr, column=2, value=f"=Market!$B${M[key]}")
    c.number_format = fmt
    c.font = font(GREEN)
    sr += 1

sr += 1
ssec("What moves the result (base case)")
for text, fn, fmt in (
    ("Year 3 facility fees for each basis point of fee", f"=Base!${CL(YCOL[3])}${RB['rev_f']}/Inputs!$B${REF['bps']}", F_MONEY),
    ("Annualised facility fees per lender at month 36", f"=IF(Base!${mcol(MONTHS)}${RB['lenders']}=0,0,Base!${mcol(MONTHS)}${RB['rev_f']}*12/Base!${mcol(MONTHS)}${RB['lenders']})", F_MONEY),
    ("Annualised revenue per paid builder project", f"=Inputs!$B${REF['price_b']}*12", F_MONEY),
    ("Annualised fee per facility at month 36", f"=Base!${mcol(MONTHS)}${RB['fee_f']}*12", F_MONEY),
):
    ws.cell(row=sr, column=1, value=text).font = font()
    c = ws.cell(row=sr, column=2, value=fn)
    c.number_format = fmt
    c.font = font(GREEN)
    sr += 1

# ---------------------------------------------------------------- Read me
wr = wb.create_sheet("Read me", 0)
setw(wr, {"A": 120})
lines = [
    ("IRIS market and revenue model", font(bold=True, size=14)),
    ("Version of 24 October 2026. The source for the IRIS investor deck, slides 14, 15, A4 and A5.", font(GREY, italic=True)),
    ("", None),
    ("How to use it", font(bold=True)),
    ("Change inputs on the Inputs sheet. Blue text = an input. Black = a formula. Green = a link from another sheet.", font()),
    ("Yellow cells are open decisions (round size, founder salaries, use of funds) and should be confirmed.", font()),
    ("Base and Conservative run side by side: each has its own column on Inputs and its own monthly sheet.", font()),
    ("", None),
    ("Sheets", font(bold=True)),
    ("Summary: three years for both cases: revenue, costs, operating result, cash, drivers and the market.", font()),
    ("Market: total, serviceable and obtainable market, built from IBISWorld's figures.", font()),
    ("Inputs: each assumption, with its type (measured, reported, estimate, company decision) and source.", font()),
    ("Base and Conservative: 36 months of drivers, revenue, costs and cash.", font()),
    ("", None),
    ("What the model assumes", font(bold=True)),
    ("Two revenue lines. Builders pay a monthly subscription per project. Once a lender makes IRIS a condition of a facility, "
     "the developer pays a fee in basis points on the facility, and builder, developer and lender each use their own view.", font()),
    ("No assessment or services revenue. No revenue from insurers or surety providers. No R&D tax refund.", font()),
    ("Conventions: A$, excluding GST. Months count from the close of this round. Costs are paid in the month incurred.", font()),
    ("Formatting follows standard financial-model conventions; it can be restyled to match another template.", font(GREY, italic=True)),
]
for i, (text, fnt) in enumerate(lines, 1):
    c = wr.cell(row=i, column=1, value=text)
    if fnt:
        c.font = fnt
    c.alignment = Alignment(wrap_text=True, vertical="top")

from openpyxl.worksheet.properties import PageSetupProperties
for sheet in wb.worksheets:
    sheet.page_setup.orientation = "landscape"
    sheet.page_setup.paperSize = sheet.PAPERSIZE_A4
    sheet.sheet_properties.pageSetUpPr = PageSetupProperties(fitToPage=True)
    sheet.page_setup.fitToWidth = 1
    sheet.page_setup.fitToHeight = 0
wb.active = 0
wb.save(OUT)
print("saved", OUT)
