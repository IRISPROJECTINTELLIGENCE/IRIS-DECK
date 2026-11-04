"""Build the IRIS five-year market, revenue, cost and cash model (openpyxl, formulas only).

Run: python3 build_model.py <output.xlsx>
All inputs live on the Inputs sheet (three cases side by side: Base, Upside, Conservative).
Every other number is a formula. Month 1 is the month the pre-seed round closes.
Version of 4 November 2026 (D-37): five years, four revenue lines, lender book conversion.
"""
import sys
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter as CL

OUT = sys.argv[1]
FONT = "Arial"
BLUE, BLACK, GREEN, GREY = "0000FF", "000000", "008000", "6F6A63"


def font(color=BLACK, bold=False, italic=False, size=10):
    return Font(name=FONT, color=color, bold=bold, italic=italic, size=size)


FILL_HDR = PatternFill("solid", fgColor="F2F2F2")
FILL_SEC = PatternFill("solid", fgColor="E7E2D8")
FILL_KEY = PatternFill("solid", fgColor="FFFF00")
FILL_OUT = PatternFill("solid", fgColor="FBE9E4")
TOPLINE = Border(top=Side(style="thin", color="000000"))

F_MONEY = '$#,##0;($#,##0);"-"'
F_MONEY_M = '$#,##0.0;($#,##0.0);"-"'
F_BN = '#,##0.0;(#,##0.0);"-"'
F_PCT = '0.0%;(0.0%);"-"'
F_CNT = '#,##0;(#,##0);"-"'
F_CNT1 = '#,##0.0;(#,##0.0);"-"'
F_NUM = '#,##0.0;(#,##0.0);"-"'
F_INT = '0'

CASES = [("base", "B", "Base"), ("up", "C", "Upside"), ("cons", "D", "Conservative")]
MONTHS = 60
YEARS = 5

wb = openpyxl.Workbook()
wi = wb.active
wi.title = "Inputs"
REF = {}


def setw(ws, widths):
    for col, w in widths.items():
        ws.column_dimensions[col].width = w


setw(wi, {"A": 60, "B": 13, "C": 13, "D": 13, "E": 15, "F": 14, "G": 120})
wi["A1"] = "IRIS five-year model: inputs"
wi["A1"].font = font(bold=True, size=14)
wi["A2"] = ("Blue cells are inputs. Three cases run side by side. Yellow cells are owner decisions. A$ excluding GST. "
            "Month 1 is the month the pre-seed round closes. 999 = not in this case.")
wi["A2"].font = font(GREY, italic=True)
for i, h in enumerate(["Input", "Base", "Upside", "Conservative", "Unit", "Type", "Source or basis"], 1):
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
    for col in range(1, 8):
        wi.cell(row=row, column=col).fill = FILL_SEC
    row += 1


def inp(key, label, base, up, cons, unit, typ, source, fmt, key_decision=False):
    global row
    wi.cell(row=row, column=1, value=label).font = font()
    for col, val in ((2, base), (3, up), (4, cons)):
        c = wi.cell(row=row, column=col, value=val)
        c.font = font(BLUE)
        c.number_format = fmt
        if key_decision:
            c.fill = FILL_KEY
    wi.cell(row=row, column=5, value=unit).font = font(GREY)
    wi.cell(row=row, column=6, value=typ).font = font(GREY)
    s = wi.cell(row=row, column=7, value=source)
    s.font = font(GREY)
    s.alignment = Alignment(wrap_text=True, vertical="top")
    REF[key] = row
    row += 1


def table(key, title, rows_, header, source, fmt=F_INT):
    global row
    wi.cell(row=row, column=1, value=title).font = font(bold=True)
    s = wi.cell(row=row, column=7, value=source)
    s.font = font(GREY)
    s.alignment = Alignment(wrap_text=True, vertical="top")
    row += 1
    for i, h in enumerate(header, 1):
        c = wi.cell(row=row, column=i, value=h)
        c.font = font(bold=True)
        c.fill = FILL_HDR
    row += 1
    first = row
    for r in rows_:
        wi.cell(row=row, column=1, value=r[0]).font = font()
        for col, val in zip((2, 3, 4), r[1:4]):
            c = wi.cell(row=row, column=col, value=val)
            c.font = font(BLUE)
            c.number_format = fmt
        row += 1
    REF[key] = (first, row - 1)
    row += 1


IB19 = "IBISWorld E3019 Multi-Unit Apartment and Townhouse Construction in Australia (2026)"
IB21 = "IBISWorld E3021 Commercial and Industrial Building Construction in Australia (2026)"

section("1. Building work a year, Australia (IBISWorld)")
for key, label, val, src in [
    ("mu_med", "Multi-unit: medium-rise flats and units (4–8 storeys)", 18.9, IB19 + ", 2025-26: $18.9bn."),
    ("mu_high", "Multi-unit: high-rise and super high-rise (9+ storeys)", 14.6, IB19 + ", 2025-26: $14.6bn."),
    ("ci_tot", "Commercial and industrial building, all segments", 70.9, IB21 + ", 2026-27: $70.9bn."),
]:
    inp(key, label, val, val, val, "A$bn a year", "Reported", src, F_BN)
inp("ci_big", "Share of C&I work on jobs of $10M or more", 0.65, 0.65, 0.65, "% of value", "Estimate",
    "IBISWorld does not split by job size. Cross-check: the top 50 builders started 722 projects worth $43.9bn in 2025, about $61M each (Hubexo, April 2026).", F_PCT)
inp("mu_dev", "Multi-unit work funded by developers", 0.88, 0.88, 0.88, "% of value", "Reported", IB19 + ", major markets: developers and REITs 48.8% plus owners and small developers 39.2%.", F_PCT)
inp("ci_dev", "C&I work funded by developers", 0.731, 0.731, 0.731, "% of value", "Reported", IB21 + ", major markets: commercial 59.8% plus industrial 13.3% property developers.", F_PCT)
inp("q_mu", "Queensland share of multi-unit work", 0.196, 0.196, 0.196, "% of value", "Reported", IB19 + ", geographic breakdown, 2024-25.", F_PCT)
inp("q_ci", "Queensland share of C&I work", 0.182, 0.182, 0.182, "% of value", "Reported (proxy)", IB21 + ", share of establishments; used as the proxy for work done.", F_PCT)
inp("build_mu", "Average build period, apartments", 29, 29, 29, "months", "Measured", "ABS average completion time, FY2025-26: 9.54 quarters (10.03 in Queensland).", F_INT)
inp("build_ci", "Average build period, C&I jobs of $10M or more", 24, 24, 24, "months", "Estimate", "Cross-check: ABS non-residential work yet to be done $76.4bn at March 2026 against about $70bn of work a year.", F_INT)
inp("proj_val", "Average contract value, jobs of $10M or more", 40, 40, 40, "A$M", "Estimate", "Cross-checks: SEQ apartment jobs on hold average about $48M (PRD, Sep 2026); Qualitas senior construction loans about $39M (Jun 2026); top-50 builders' 2025 starts about $61M (Hubexo).", F_NUM)
inp("fac_ratio", "Project debt stack as a share of the build contract", 1.2, 1.2, 1.2, "x", "Estimate",
    "Lenders fund 60–80% of total development cost (banks 60–70%, non-banks 75–80%: Feasly, Vertex Capital 2026); the build is about two-thirds of that cost, so the full stack (senior plus mezzanine) is about 1.1–1.2 times the build contract (D-33).", '0.00"x"')
inp("distress", "Share of live funded projects that stall or default in a year", 0.04, 0.05, 0.03, "% a year", "Estimate",
    "Construction was 24.5% of FY2025-26 insolvencies (3,472 of 14,153, ASIC) and 37% in July–August 2026 with Bathla. No public series for funded $10M-plus projects; 4% is an estimate and the weakest input in the assessment line.", F_PCT)

section("2. Pricing (company decisions)")
inp("price_b", "IRIS for Builders: subscription per live job", 3500, 3500, 3500, "A$ a month", "Company", "Follows the builder across its jobs (D-33).", F_MONEY)
inp("bps", "IRIS for Lenders: facility fee", 15, 15, 12.5, "bps a year", "Company", "On the full project debt stack, paid by the developer as a condition of the facility, as it pays the QS. Cross-check: QS progress monitoring on a job of this size is in the same range (Pekaj Group 2026; Feasly 2026).", '0.0')
inp("fee_floor", "Facility fee floor", 3500, 3500, 3500, "A$ a month", "Company", "No facility pays less than a builder subscription.", F_MONEY)
inp("fee_cap", "Facility fee cap", 10000, 12500, 10000, "A$ a month", "Company", "Keeps the fee proportionate on large facilities. At $80M and 15 bps the cap binds.", F_MONEY)
inp("fac_avg", "Average facility, full debt stack", 80, 80, 60, "A$M", "Owner decision D-33", "IRIS is written into the whole stack; $80M average (owner, 1 Nov 2026). Qualitas senior loans average $39M; with mezzanine and larger jobs the stack is about double.", F_NUM, key_decision=True)
inp("price_d", "IRIS for Developers: project with no lender condition", 2500, 2500, 2500, "A$ a month", "Company", "Developer-direct PCG view, from Year 3. Priced below the builder subscription because the developer brings no systems of its own.", F_MONEY)
inp("assess_fee", "Distressed-project assessment, per engagement", 35000, 45000, 25000, "A$", "Estimate (benchmarked)",
    "Benchmark: a QS initial financier's report on a commercial job is $8,000–20,000, non-bank lenders at the upper end; a final account review $2,000–5,000 (Pekaj Group, 2026); full QS cost management runs 0.5–2% of build value (Feasly, 2026). An assessment on a stalled $40M job sits between an initial report and a cost-management engagement. No engagement has set the fee (D-37).", F_MONEY)

section("3. IRIS for Lenders: adoption and book conversion")
inp("per_lender", "New facilities per lender a month after adoption", 0.8, 1.0, 0.5, "facilities a month", "Estimate",
    "About ten facilities a year of $80M, roughly $770M of originations: a $1.5bn construction book turning over on 24-month terms. Larger lenders write more; the average across twenty includes smaller funds.", "0.00")
inp("book_fac", "Existing facilities per lender that come under the condition at re-papering", 10, 14, 6, "facilities", "Estimate",
    "A lender's live book re-papers at extensions and refinances; about half of a 20-facility book is assumed to come under the condition in the 18 months after adoption. The rest completes before it re-papers.", F_INT)
inp("book_m", "Months over which the existing book converts", 18, 15, 24, "months", "Estimate", "Extensions and refinances fall across the book's remaining terms.", F_INT)
inp("fac_term", "Facility term", 24, 24, 24, "months", "Estimate", "Facilities leave the count at completion.", F_INT)
table("lenders", "Lender adoption: month each lender's first facility comes under the condition",
      [(f"Lender {i}", b, u, c) for i, (b, u, c) in enumerate([
          (12, 12, 12), (18, 17, 21), (22, 20, 27), (26, 23, 33), (29, 26, 40), (32, 28, 48), (34, 30, 56), (36, 32, 999),
          (39, 34, 999), (41, 36, 999), (43, 38, 999), (45, 40, 999), (47, 42, 999), (48, 44, 999), (50, 46, 999), (52, 48, 999),
          (54, 50, 999), (56, 52, 999), (58, 54, 999), (60, 56, 999)], 1)],
      ["Lender", "Base", "Upside", "Conservative"],
      "Owner target (4 Nov 2026): 1 / 3 / 8 / 14 / 20 lenders by the end of Years 1–5. The design partner is lender 1 (month 12). Lenders 2 onwards follow a live result at lender 1. "
      "This cadence is a company target, not a sourced figure; the design-partner letter and the first written condition are the evidence that would ground it.")

section("4. IRIS for Builders: the wedge")
inp("rd_start", "R&D deployments go live", 3, 3, 3, "month", "Company", "Two builder deployments live by month 3 (slide 13).", F_INT)
inp("rd_n", "R&D deployments", 2, 2, 2, "projects", "Company", "", F_INT)
inp("paid_start", "Builders start paying", 6, 6, 7, "month", "Company", "After the position reconciles to the builder's own cost reports.", F_INT)
inp("jobs_start", "Paid jobs per builder at signing", 2, 2, 2, "projects", "Company", "", F_INT)
inp("jobs_ramp", "Further jobs added per builder a month", 0.5, 0.5, 0.33, "projects a month", "Estimate", "About one new job every two months.", "0.00")
inp("jobs_cap", "Live jobs per builder at maturity", 6, 7, 5, "projects", "Estimate", "A SEQ Tier 2 builder runs about three to eight jobs of $10M or more at a time (founder observation; the pilot builder's own count is the first evidence).", F_INT)
table("builders", "Builder adoption: month each builder starts paying",
      [(f"Builder {i}", b, u, c) for i, (b, u, c) in enumerate([
          (6, 6, 7), (6, 6, 7), (12, 11, 15), (20, 17, 24), (28, 22, 33), (33, 26, 42), (37, 30, 51), (40, 33, 60), (43, 36, 999), (46, 39, 999),
          (48, 42, 999), (50, 44, 999), (52, 46, 999), (54, 48, 999), (56, 50, 999), (58, 52, 999), (60, 54, 999), (999, 56, 999), (999, 58, 999), (999, 60, 999)], 1)],
      ["Builder", "Base", "Upside", "Conservative"],
      "Owner input (1 Nov 2026): five builders at about six jobs each by month 36. From Year 4 builders under a lender condition bring their other jobs and the count rises with lender adoption.")

section("5. IRIS for Developers (developer-direct, no lender condition)")
inp("dev_start", "Developer-direct projects start", 30, 27, 36, "month", "Company", "After the lender view exists; sold to developers whose facility carries no condition.", F_INT)
inp("dev_add", "New developer-direct projects a month", 0.5, 0.75, 0.25, "projects a month", "Estimate", "A small line; the developer's main route is through its lender's condition.", "0.00")

section("6. Distressed-project assessments")
inp("assess_start", "Assessments offered from", 30, 27, 36, "month", "Company", "After the platform is proven on live jobs (D-07).", F_INT)
inp("assess_off", "Off-platform assessments won a year, by Year 5", 8, 12, 3, "engagements a year", "Estimate",
    "Lenders, receivers and administrators on projects not under the condition. Ramps linearly from the start month. About 140 funded $10M-plus projects a year stall nationally at a 4% rate; 8 is about 6% of them.", F_INT)
inp("assess_on", "Share of on-platform distressed facilities that buy an assessment", 0.6, 0.75, 0.4, "%", "Estimate", "A lender already on IRIS usually needs the assessment when a facility stalls.", F_PCT)

section("7. Team")
inp("n_found", "Founders, full-time from month 1", 2, 2, 2, "people", "Company", "", F_INT)
inp("sal_found", "Founder salary, each", 100000, 100000, 100000, "A$ a year", "Owner decision D-21", "", F_MONEY, key_decision=True)
inp("oncost", "On-costs on salaries", 0.12, 0.12, 0.12, "% of salary", "Reported", "Superannuation guarantee 12% from 1 July 2025.", F_PCT)
inp("sal_raise", "Salary growth a year, from Year 3", 0.03, 0.03, 0.03, "% a year", "Estimate", "", F_PCT)
inp("sal_found2", "Founder salary, each, from Year 3", 180000, 180000, 150000, "A$ a year", "Company", "Market rate once the seed is in and lenders are live.", F_MONEY)
inp("an_ratio", "Live facilities and jobs per deployment analyst", 8, 10, 10, "per analyst", "Estimate", "An analyst keeps each position checked against its source records monthly; about eight live jobs each. Analysts are hired as the count grows (formula, not a fixed list).", F_INT)
inp("an_sal", "Deployment analyst salary", 110000, 110000, 110000, "A$ a year", "Estimate", "", F_MONEY)
inp("ls_ratio", "Lenders per lender success manager", 2, 3, 3, "per manager", "Estimate", "Onboards each lender's book, runs credit-committee reviews, holds the relationship.", F_INT)
inp("ls_sal", "Lender success manager salary", 140000, 140000, 140000, "A$ a year", "Estimate", "", F_MONEY)
inp("eng_base", "Engineers from month 16, before lender scaling", 2, 2, 1, "people", "Company", "Connectors, platform, reliability.", F_INT)
inp("eng_ratio", "Lenders per additional engineer", 1.5, 2, 3, "per engineer", "Estimate", "Each lender brings its own facility structures, reporting formats and security review.", "0.0")
inp("eng_sal", "Engineer salary", 170000, 170000, 170000, "A$ a year", "Estimate", "", F_MONEY)
inp("onb_cost", "One-off cost to connect each new facility", 4000, 4000, 5000, "A$", "Estimate", "Connector setup, record mapping and the first reconciliation, mostly contractor and analyst time.", F_MONEY)
inp("comm", "Sales commission on new lender revenue", 0.08, 0.08, 0.08, "% of first-year fees", "Estimate", "Paid on each new facility's first-year fee.", F_PCT)
HIRES = [
    ("Commercial lead (lenders and builders)", 160000, 16, 14, 19),
    ("Lender onboarding lead", 150000, 18, 16, 999),
    ("Head of product and risk", 180000, 22, 19, 999),
    ("Security and platform engineer", 170000, 34, 29, 999),
    ("Sales, lenders 1", 160000, 37, 31, 999),
    ("Finance and operations", 130000, 38, 33, 999),
    ("Product manager", 150000, 40, 35, 999),
    ("Sales, lenders 2", 160000, 43, 37, 999),
    ("Head of sales", 200000, 44, 38, 999),
    ("Data and ML engineer 1", 180000, 45, 39, 999),
    ("Support 1", 100000, 48, 42, 999),
    ("Marketing and content", 120000, 48, 42, 999),
    ("Data and ML engineer 2", 180000, 53, 47, 999),
    ("Support 2", 100000, 56, 50, 999),
    ("Legal and compliance", 160000, 50, 44, 999),
]
table("hires", "Hires: the month each role starts",
      [(r[0], r[2], r[3], r[4]) for r in HIRES], ["Role", "Base start", "Upside start", "Cons. start"],
      "Fixed roles only. Deployment analysts, lender success managers and engineers are hired by formula as facilities and lenders grow (inputs above). Salaries in the next table.")
table("sal", "Hire salaries (A$ a year, Year 1 terms; grow with the salary-growth input from Year 3)",
      [(r[0], r[1], r[1], r[1]) for r in HIRES], ["Role", "Base", "Upside", "Conservative"], "Market rates for Brisbane and Gold Coast, 2026 (estimate).", F_MONEY)

section("8. Other costs")
for key, label, vals, unit, typ, src in [
    ("build_y", "Platform build and contract engineering, by year", [170000, 90000, 90000, 60000, 60000], "A$ a year", "Company", "Year 1 from the use of funds (slide 13)."),
    ("cloud_fix", "Cloud, models and tools, fixed, by year", [9600, 24000, 60000, 120000, 180000], "A$ a year", "Estimate", "Hosting, monitoring, development tools; grows with the team."),
    ("sec_y", "Security certification and audits, by year", [30000, 35000, 60000, 80000, 100000], "A$ a year", "Estimate", "ISO 27001 or SOC 2 in Year 1 for lender onboarding; surveillance audits and penetration testing after."),
    ("ins_y", "Insurance (PI and cyber), by year", [10000, 45000, 150000, 300000, 500000], "A$ a year", "Estimate", "Lender reliance raises professional indemnity cover as facilities under the condition grow."),
    ("sm_y", "Sales and marketing (non-salary), by year", [20000, 120000, 400000, 1000000, 1600000], "A$ a year", "Estimate", "Events, travel, content, lender and broker channel."),
    ("lg_y", "Legal, accounting and IP, by year", [20000, 40000, 120000, 220000, 320000], "A$ a year", "Estimate", "Reliance terms, side-deed templates, mandate opinion, trademarks."),
    ("off_y", "Office and overheads, by year", [0, 12000, 90000, 300000, 480000], "A$ a year", "Estimate", "Remote in Years 1–2; Brisbane or Gold Coast office from Year 3."),
]:
    for yi, v in enumerate(vals, 1):
        vc = v if (yi <= 2 or key in ("build_y", "sec_y")) else round(v * 0.5, -3)
        inp(f"{key}{yi}", f"{label}: Year {yi}", v, v, vc, unit, typ, (src + " Conservative runs non-salary overheads at half from Year 3.") if yi == 1 else "", F_MONEY)
inp("cloud_var", "Cloud and model use per live job or facility", 250, 250, 300, "A$ a month", "Estimate", "Model inference, storage and connectors per live job.", F_MONEY)
inp("cont_y1", "Contingency, Year 1", 10000, 10000, 10000, "A$", "Company", "Use of funds contingency line.", F_MONEY)
inp("cont_pct", "Contingency, Years 2–5", 0.05, 0.05, 0.05, "% of costs", "Estimate", "", F_PCT)

section("9. Funding")
inp("safe", "Pre-seed SAFE, received month 1", 500000, 500000, 500000, "A$", "Owner decision D-21", "$500K at a $5M cap.", F_MONEY, key_decision=True)
inp("seed", "Seed round", 3000000, 3000000, 3000000, "A$", "Company", "Slide 13: seed in months 15–18 on the evidence of Year 1.", F_MONEY)
inp("seed_m", "Seed round received", 15, 15, 15, "month", "Company", "", F_INT)
inp("ser_a", "Series A (shown separately)", 8000000, 8000000, 0, "A$", "Company", "Optional: funds a faster lender rollout and national sales from Year 4. Cash is shown with and without it.", F_MONEY)
inp("ser_a_m", "Series A received", 36, 33, 999, "month", "Company", "", F_INT)

# ---------------------------------------------------------------- monthly sheets
C0 = 3
CLAST = C0 + MONTHS - 1
YCOL = {y: CLAST + 1 + y for y in range(1, YEARS + 1)}


def mcol(m):
    return CL(C0 + m - 1)


def I(key, col):
    return f"Inputs!${col}${REF[key]}"


def build_month_sheet(ws, col, title):
    setw(ws, {"A": 50, "B": 12})
    for m in range(1, MONTHS + 1):
        ws.column_dimensions[mcol(m)].width = 10.5
    ws.column_dimensions[CL(CLAST + 1)].width = 3
    for y in range(1, YEARS + 1):
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

    label(3, "Month", True)
    label(4, "Year", True)
    for m in range(1, MONTHS + 1):
        c = ws.cell(row=3, column=C0 + m - 1, value=(1 if m == 1 else f"={mcol(m-1)}3+1"))
        c.font = font(bold=True)
        c.fill = FILL_HDR
        c.alignment = Alignment(horizontal="right")
        y = ws.cell(row=4, column=C0 + m - 1, value=f"=ROUNDUP({mcol(m)}3/12,0)")
        y.font = font(GREY)
        y.alignment = Alignment(horizontal="right")
    for yy in range(1, YEARS + 1):
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
            rows.append(("_sec", r, title, "", None, None, "section", True, False))
        r += 1

    lf, ll = REF["lenders"]
    lst = f"Inputs!${col}${lf}:${col}${ll}"
    bf, bl = REF["builders"]
    bst = f"Inputs!${col}${bf}:${col}${bl}"
    hf, hl = REF["hires"]
    hst = f"Inputs!${col}${hf}:${col}${hl}"
    sf, sl = REF["sal"]
    sal = f"Inputs!${col}${sf}:${col}${sl}"

    def yv(key, m):
        return "CHOOSE(" + f"{m}$4," + ",".join(I(f"{key}{yi}", col) for yi in range(1, YEARS + 1)) + ")"

    blank("IRIS for Lenders")
    row_def("lenders", "Lenders with the condition", "lenders", lambda m, p: f"=COUNTIF({lst},\"<=\"&{m}$3)", F_CNT, "stock")
    row_def("newf", "New facilities under the condition", "facilities", lambda m, p: f"={m}{R['lenders']}*{I('per_lender',col)}", F_CNT1)
    row_def("rollf", "Existing book re-papered under the condition", "facilities",
            lambda m, p: f"=SUMPRODUCT(({lst}<{m}$3)*({lst}+{I('book_m',col)}>={m}$3))*{I('book_fac',col)}/{I('book_m',col)}", F_CNT1)
    row_def("endf", "Facilities completing", "facilities",
            lambda m, p: f"=IF({m}$3>{I('fac_term',col)},INDEX(${mcol(1)}${R['newf']}:${mcol(MONTHS)}${R['newf']},1,{m}$3-{I('fac_term',col)})+INDEX(${mcol(1)}${R['rollf']}:${mcol(MONTHS)}${R['rollf']},1,{m}$3-{I('fac_term',col)}),0)", F_CNT1)
    row_def("livef", "Facilities under the condition, end of month", "facilities",
            lambda m, p: f"={(p + str(R['livef']) + '+') if p else ''}{m}{R['newf']}+{m}{R['rollf']}-{m}{R['endf']}", F_CNT1, "stock")
    row_def("fee_f", "Fee per facility", "A$ a month",
            lambda m, p: f"=MIN(MAX({I('fac_avg',col)}*1000000*{I('bps',col)}/10000/12,{I('fee_floor',col)}),{I('fee_cap',col)})", F_MONEY, "stock")
    row_def("rev_f", "IRIS for Lenders revenue (paid by developers)", "A$", lambda m, p: f"={m}{R['livef']}*{m}{R['fee_f']}", F_MONEY)
    blank()
    blank("IRIS for Builders")
    row_def("rd", "R&D deployments live (unpaid)", "projects",
            lambda m, p: f"=IF(AND({m}$3>={I('rd_start',col)},{m}$3<{I('paid_start',col)}),{I('rd_n',col)},0)", F_CNT1, "stock")
    row_def("builders", "Paying builders", "builders", lambda m, p: f"=COUNTIF({bst},\"<=\"&{m}$3)", F_CNT, "stock")
    row_def("paid", "Paid builder jobs, end of month", "projects",
            lambda m, p: (f"=SUMPRODUCT(({bst}<={m}$3)*((({I('jobs_start',col)}+{I('jobs_ramp',col)}*({m}$3-{bst}))>{I('jobs_cap',col)})*{I('jobs_cap',col)}"
                          f"+(({I('jobs_start',col)}+{I('jobs_ramp',col)}*({m}$3-{bst}))<={I('jobs_cap',col)})*({I('jobs_start',col)}+{I('jobs_ramp',col)}*({m}$3-{bst}))))"), F_CNT1, "stock")
    row_def("rev_b", "IRIS for Builders revenue", "A$", lambda m, p: f"={m}{R['paid']}*{I('price_b',col)}", F_MONEY)
    blank()
    blank("IRIS for Developers (developer-direct)")
    row_def("newd", "New developer-direct projects", "projects", lambda m, p: f"=IF({m}$3>={I('dev_start',col)},{I('dev_add',col)},0)", F_CNT1)
    row_def("endd", "Developer-direct projects completing", "projects",
            lambda m, p: f"=IF({m}$3>{I('fac_term',col)},INDEX(${mcol(1)}${R['newd']}:${mcol(MONTHS)}${R['newd']},1,{m}$3-{I('fac_term',col)}),0)", F_CNT1)
    row_def("lived", "Developer-direct projects, end of month", "projects",
            lambda m, p: f"={(p + str(R['lived']) + '+') if p else ''}{m}{R['newd']}-{m}{R['endd']}", F_CNT1, "stock")
    row_def("rev_d", "IRIS for Developers revenue", "A$", lambda m, p: f"={m}{R['lived']}*{I('price_d',col)}", F_MONEY)
    blank()
    blank("Distressed-project assessments")
    row_def("ass_on", "On-platform assessments", "engagements",
            lambda m, p: f"=IF({m}$3>={I('assess_start',col)},{m}{R['livef']}*{I('distress',col)}/12*{I('assess_on',col)},0)", F_CNT1)
    row_def("ass_off", "Off-platform assessments", "engagements",
            lambda m, p: f"=IF({m}$3>={I('assess_start',col)},{I('assess_off',col)}/12*MIN(1,({m}$3-{I('assess_start',col)}+1)/({MONTHS}-{I('assess_start',col)}+1)),0)", F_CNT1)
    row_def("rev_a", "Assessment revenue", "A$", lambda m, p: f"=({m}{R['ass_on']}+{m}{R['ass_off']})*{I('assess_fee',col)}", F_MONEY)
    blank()
    row_def("rev", "Total revenue", "A$", lambda m, p: f"={m}{R['rev_f']}+{m}{R['rev_b']}+{m}{R['rev_d']}+{m}{R['rev_a']}", F_MONEY, bold=True, topline=True)
    row_def("arr", "Annualised revenue (month × 12)", "A$", lambda m, p: f"={m}{R['rev']}*12", F_MONEY, "stock")
    blank()
    blank("Team and costs")
    row_def("n_an", "Deployment analysts", "people", lambda m, p: f"=IF({m}$3<16,0,ROUNDUP(({m}{R['livef']}+{m}{R['paid']}+{m}{R['lived']})/{I('an_ratio',col)},0))", F_CNT, "stock")
    row_def("n_ls", "Lender success managers", "people", lambda m, p: f"=IF({m}$3<16,0,ROUNDUP({m}{R['lenders']}/{I('ls_ratio',col)},0))", F_CNT, "stock")
    row_def("n_eng", "Engineers", "people", lambda m, p: f"=IF({m}$3<16,0,{I('eng_base',col)}+ROUNDUP({m}{R['lenders']}/{I('eng_ratio',col)},0))", F_CNT, "stock")
    row_def("c_found", "Founders", "A$", lambda m, p: f"={I('n_found',col)}*IF({m}$4<=2,{I('sal_found',col)},{I('sal_found2',col)})/12*(1+{I('oncost',col)})*(1+{I('sal_raise',col)})^MAX(0,{m}$4-3)", F_MONEY)
    row_def("c_hire", "Fixed roles", "A$", lambda m, p: f"=SUMPRODUCT(({hst}<={m}$3)*{sal})/12*(1+{I('oncost',col)})*(1+{I('sal_raise',col)})^MAX(0,{m}$4-2)", F_MONEY)
    row_def("c_an", "Deployment analysts", "A$", lambda m, p: f"={m}{R['n_an']}*{I('an_sal',col)}/12*(1+{I('oncost',col)})*(1+{I('sal_raise',col)})^MAX(0,{m}$4-2)", F_MONEY)
    row_def("c_ls", "Lender success", "A$", lambda m, p: f"={m}{R['n_ls']}*{I('ls_sal',col)}/12*(1+{I('oncost',col)})*(1+{I('sal_raise',col)})^MAX(0,{m}$4-2)", F_MONEY)
    row_def("c_eng", "Engineers", "A$", lambda m, p: f"={m}{R['n_eng']}*{I('eng_sal',col)}/12*(1+{I('oncost',col)})*(1+{I('sal_raise',col)})^MAX(0,{m}$4-2)", F_MONEY)
    row_def("c_comm", "Sales commissions", "A$", lambda m, p: f"=({m}{R['newf']}+{m}{R['rollf']})*{m}{R['fee_f']}*12*{I('comm',col)}", F_MONEY)
    row_def("c_onb", "Facility onboarding", "A$", lambda m, p: f"=({m}{R['newf']}+{m}{R['rollf']}+{m}{R['newd']})*{I('onb_cost',col)}", F_MONEY)
    row_def("c_build", "Platform build and contract engineering", "A$", lambda m, p: f"={yv('build_y', m)}/12", F_MONEY)
    row_def("c_cloud", "Cloud, models and tools", "A$", lambda m, p: f"={yv('cloud_fix', m)}/12+({m}{R['rd']}+{m}{R['paid']}+{m}{R['livef']}+{m}{R['lived']})*{I('cloud_var',col)}", F_MONEY)
    row_def("c_sec", "Security certification and audits", "A$", lambda m, p: f"={yv('sec_y', m)}/12", F_MONEY)
    row_def("c_ins", "Insurance", "A$", lambda m, p: f"={yv('ins_y', m)}/12", F_MONEY)
    row_def("c_sm", "Sales and marketing", "A$", lambda m, p: f"={yv('sm_y', m)}/12", F_MONEY)
    row_def("c_lg", "Legal, accounting and IP", "A$", lambda m, p: f"={yv('lg_y', m)}/12", F_MONEY)
    row_def("c_off", "Office and overheads", "A$", lambda m, p: f"={yv('off_y', m)}/12", F_MONEY)
    row_def("c_cont", "Contingency", "A$", lambda m, p: f"=IF({m}$4=1,{I('cont_y1',col)}/12,{I('cont_pct',col)}*SUM({m}{R['c_found']}:{m}{R['c_off']}))", F_MONEY)
    row_def("cost", "Total costs", "A$", lambda m, p: f"=SUM({m}{R['c_found']}:{m}{R['c_cont']})", F_MONEY, bold=True, topline=True)
    row_def("head", "Team, end of month", "people", lambda m, p: f"={I('n_found',col)}+COUNTIF({hst},\"<=\"&{m}$3)+{m}{R['n_an']}+{m}{R['n_ls']}+{m}{R['n_eng']}", F_CNT, "stock")
    blank()
    row_def("op", "Operating result (EBITDA)", "A$", lambda m, p: f"={m}{R['rev']}-{m}{R['cost']}", F_MONEY, bold=True)
    blank()
    blank("Cash")
    row_def("in_safe", "Pre-seed", "A$", lambda m, p: f"=IF({m}$3=1,{I('safe',col)},0)", F_MONEY)
    row_def("in_seed", "Seed", "A$", lambda m, p: f"=IF({m}$3={I('seed_m',col)},{I('seed',col)},0)", F_MONEY)
    row_def("in_a", "Series A", "A$", lambda m, p: f"=IF({m}$3={I('ser_a_m',col)},{I('ser_a',col)},0)", F_MONEY)
    row_def("cash0", "Cash with pre-seed only, end of month", "A$", lambda m, p: f"={(p + str(R['cash0']) + '+') if p else ''}{m}{R['op']}+{m}{R['in_safe']}", F_MONEY, "stock")
    row_def("cash1", "Cash with seed, end of month", "A$", lambda m, p: f"={(p + str(R['cash1']) + '+') if p else ''}{m}{R['op']}+{m}{R['in_safe']}+{m}{R['in_seed']}", F_MONEY, "stock", bold=True)
    row_def("cash2", "Cash with seed and Series A, end of month", "A$", lambda m, p: f"={(p + str(R['cash2']) + '+') if p else ''}{m}{R['op']}+{m}{R['in_safe']}+{m}{R['in_seed']}+{m}{R['in_a']}", F_MONEY, "stock")
    row_def("neg1", "Helper: month if cash with seed is negative", "month", lambda m, p: f"=IF({m}{R['cash1']}<0,{m}$3,99)", F_INT, "helper")

    for key, rr, text, unit, fn, fmt, kind, bold, topline in rows:
        if kind == "section":
            c = ws.cell(row=rr, column=1, value=text)
            c.font = font(bold=True)
            for cc in range(1, YCOL[YEARS] + 1):
                ws.cell(row=rr, column=cc).fill = FILL_SEC
            continue
        label(rr, text, bold, unit)
        if kind == "helper":
            ws.cell(row=rr, column=1).font = font(GREY, italic=True)
        for m in range(1, MONTHS + 1):
            c = ws.cell(row=rr, column=C0 + m - 1, value=fn(mcol(m), mcol(m - 1) if m > 1 else None))
            c.number_format = fmt
            c.font = font(bold=bold, color=(GREY if kind == "helper" else BLACK))
            if topline:
                c.border = TOPLINE
        for yy in range(1, YEARS + 1):
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


SHEETS = {}
for case, col, name in CASES:
    ws_ = wb.create_sheet(name)
    SHEETS[case] = (name, build_month_sheet(ws_, col, f"{name} case: monthly"))

# ---------------------------------------------------------------- Market
wm = wb.create_sheet("Market", 1)
setw(wm, {"A": 62, "B": 16, "C": 14, "D": 110})
wm["A1"] = "Market: total, serviceable and obtainable"
wm["A1"].font = font(bold=True, size=14)
wm["A2"] = "Built from IBISWorld's figures for the two industries IRIS serves. Green cells link to Inputs; black cells are formulas."
wm["A2"].font = font(GREY, italic=True)
for i, h in enumerate(["Line", "Value", "Unit", "How it is worked out"], 1):
    c = wm.cell(row=4, column=i, value=h)
    c.font = font(bold=True)
    c.fill = FILL_HDR
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


def IB(key):
    return f"Inputs!$B${REF[key]}"


def mref(key):
    return f"$B${M[key]}"


msec("A. Building work a year in scope")
mline("mu_in", "Multi-unit work in scope (medium- and high-rise)", f"={IB('mu_med')}+{IB('mu_high')}", "A$bn", "IBISWorld E3019, 2025-26.", F_BN, link=True)
mline("ci_in", "C&I work in scope (jobs of $10M or more)", f"={IB('ci_tot')}*{IB('ci_big')}", "A$bn", "IBISWorld E3021 × share on $10M+ jobs.", F_BN, link=True)
msec("B. Value under construction and live projects")
mline("mu_live", "Multi-unit value under construction", f"={mref('mu_in')}*{IB('build_mu')}/12", "A$bn", "Work a year × build period.", F_BN)
mline("ci_live", "C&I value under construction", f"={mref('ci_in')}*{IB('build_ci')}/12", "A$bn", "", F_BN)
mline("live_val", "Value under construction in scope, Australia", f"={mref('mu_live')}+{mref('ci_live')}", "A$bn", "", F_BN, bold=True)
mline("dev_live", "Developer-funded value under construction", f"={mref('mu_live')}*{IB('mu_dev')}+{mref('ci_live')}*{IB('ci_dev')}", "A$bn", "Where a lender can make IRIS a condition of the facility.", F_BN)
mline("live_n", "Live projects in scope, Australia", f"={mref('live_val')}*1000/{IB('proj_val')}", "projects", "÷ average contract value.", F_CNT, bold=True)
mline("live_dev", "of which developer-funded (facility fee)", f"={mref('dev_live')}*1000/{IB('proj_val')}", "projects", "", F_CNT)
mline("live_oth", "of which other (builder subscription)", f"={mref('live_n')}-{mref('live_dev')}", "projects", "", F_CNT)
msec("C. Price per job")
mline("fee_fac", "Facility fee per facility a year", f"=MIN(MAX({IB('proj_val')}*{IB('fac_ratio')}*1000000*{IB('bps')}/10000,{IB('fee_floor')}*12),{IB('fee_cap')}*12)", "A$ a year", "Average debt stack × bps, within floor and cap.", F_MONEY)
mline("fee_b", "Builder subscription per job a year", f"={IB('price_b')}*12", "A$ a year", "", F_MONEY)
mline("fee_a", "Assessments a year, Australia", f"={mref('live_dev')}*{IB('distress')}*{IB('assess_fee')}/1000000", "A$M a year", "Distressed funded projects a year × fee.", F_MONEY_M)
msec("D. Market, A$ millions a year")
mline("tam_f", "Facility fees on all developer-funded projects", f"={mref('live_dev')}*{mref('fee_fac')}/1000000", "A$M a year", "", F_MONEY_M)
mline("tam_b", "Builder subscriptions on all other projects", f"={mref('live_oth')}*{mref('fee_b')}/1000000", "A$M a year", "", F_MONEY_M)
mline("tam", "Total market (TAM), Australia", f"={mref('tam_f')}+{mref('tam_b')}+{mref('fee_a')}", "A$M a year", "Monitoring and subscriptions on all live jobs of $10M or more, plus assessments.", F_MONEY_M, bold=True, out=True)
mline("q_dev", "Queensland developer-funded value under construction", f"={mref('mu_live')}*{IB('q_mu')}*{IB('mu_dev')}+{mref('ci_live')}*{IB('q_ci')}*{IB('ci_dev')}", "A$bn", "", F_BN)
mline("q_oth", "Queensland other value under construction", f"={mref('mu_live')}*{IB('q_mu')}*(1-{IB('mu_dev')})+{mref('ci_live')}*{IB('q_ci')}*(1-{IB('ci_dev')})", "A$bn", "", F_BN)
mline("q_live", "Live projects in scope, Queensland", f"=({mref('q_dev')}+{mref('q_oth')})*1000/{IB('proj_val')}", "projects", "", F_CNT)
mline("sam", "Serviceable market (SAM), Queensland", f"=({mref('q_dev')}*1000/{IB('proj_val')}*{mref('fee_fac')}+{mref('q_oth')}*1000/{IB('proj_val')}*{mref('fee_b')})/1000000+{mref('q_dev')}*1000/{IB('proj_val')}*{IB('distress')}*{IB('assess_fee')}/1000000", "A$M a year", "South East Queensland is about 79% of the state's pipeline (CSQ).", F_MONEY_M, bold=True, out=True)
for case, col, name in CASES:
    nm, R = SHEETS[case]
    mline(f"som_{case}", f"Obtainable (SOM): annualised revenue at month 60, {name}", f"={nm}!${mcol(MONTHS)}${R['arr']}/1000000", "A$M a year", "", F_MONEY_M, link=True, bold=(case == "base"), out=(case == "base"))
    mline(f"som36_{case}", f"Annualised revenue at month 36, {name}", f"={nm}!${mcol(36)}${R['arr']}/1000000", "A$M a year", "", F_MONEY_M, link=True)
mline("som_sh", "SOM (base, month 60) as a share of TAM", f"={mref('som_base')}/{mref('tam')}", "%", "", F_PCT)

# ---------------------------------------------------------------- Summary
ws = wb.create_sheet("Summary", 1)
setw(ws, {"A": 48})
for i in range(2, 2 + 3 * (YEARS + 1)):
    ws.column_dimensions[CL(i)].width = 12
ws["A1"] = "IRIS: five-year summary"
ws["A1"].font = font(bold=True, size=14)
ws["A2"] = "A$ unless stated. Year 1 starts the month the pre-seed closes. Linked from the monthly sheets."
ws["A2"].font = font(GREY, italic=True)
colstart = {}
cc = 2
for case, col, name in CASES:
    colstart[case] = cc
    c = ws.cell(row=4, column=cc, value=name)
    c.font = font(bold=True)
    for yy in range(1, YEARS + 1):
        h = ws.cell(row=5, column=cc + yy - 1, value=f"Year {yy}")
        h.font = font(bold=True)
        h.fill = FILL_HDR
        h.alignment = Alignment(horizontal="right")
    cc += YEARS + 1
sr = 6
S = {}


def ssec(title):
    global sr
    sr += 1
    c = ws.cell(row=sr, column=1, value=title)
    c.font = font(bold=True)
    for col in range(1, cc):
        ws.cell(row=sr, column=col).fill = FILL_SEC
    sr += 1


def sline(key, text, src_key, fmt, bold=False, topline=False, combine=None):
    global sr
    ws.cell(row=sr, column=1, value=text).font = font(bold=bold)
    for case, col, name in CASES:
        nm, R = SHEETS[case]
        for yy in range(1, YEARS + 1):
            ycol = CL(YCOL[yy])
            f = ("=" + "+".join(f"{nm}!${ycol}${R[k]}" for k in combine)) if combine else f"={nm}!${ycol}${R[src_key]}"
            c = ws.cell(row=sr, column=colstart[case] + yy - 1, value=f)
            c.number_format = fmt
            c.font = font(GREEN, bold=bold)
            if topline:
                c.border = TOPLINE
    S[key] = sr
    sr += 1


ssec("Revenue")
sline("rev_f", "IRIS for Lenders (paid by developers)", "rev_f", F_MONEY)
sline("rev_b", "IRIS for Builders", "rev_b", F_MONEY)
sline("rev_d", "IRIS for Developers (direct)", "rev_d", F_MONEY)
sline("rev_a", "Distressed-project assessments", "rev_a", F_MONEY)
sline("rev", "Total revenue", "rev", F_MONEY, bold=True, topline=True)
ssec("Costs")
sline("c_people", "People", None, F_MONEY, combine=["c_found", "c_hire", "c_an", "c_ls", "c_eng"])
sline("c_plat", "Platform build, cloud and security", None, F_MONEY, combine=["c_build", "c_cloud", "c_sec"])
sline("c_go", "Sales, commissions, onboarding, legal, insurance, office", None, F_MONEY, combine=["c_sm", "c_comm", "c_onb", "c_lg", "c_ins", "c_off"])
sline("c_cont", "Contingency", "c_cont", F_MONEY)
sline("cost", "Total costs", "cost", F_MONEY, bold=True, topline=True)
ssec("Result and cash")
sline("op", "Operating result (EBITDA)", "op", F_MONEY, bold=True)
sline("cash1", "Cash at year end, with seed", "cash1", F_MONEY)
sline("cash2", "Cash at year end, with seed and Series A", "cash2", F_MONEY)
ssec("Drivers at year end")
sline("lenders", "Lenders with the condition", "lenders", F_CNT)
sline("livef", "Facilities under the condition", "livef", F_CNT)
sline("builders", "Paying builders", "builders", F_CNT)
sline("paid", "Paid builder jobs", "paid", F_CNT)
sline("lived", "Developer-direct projects", "lived", F_CNT)
sline("ass", "Assessments in the year", None, F_CNT1, combine=["ass_on", "ass_off"])
sline("head", "Team", "head", F_CNT)
sline("arr", "Annualised revenue at year end", "arr", F_MONEY, bold=True)

sr += 1
ssec("Unit economics and checks (base case)")
nm, R = SHEETS["base"]
nmc, Rc = SHEETS["cons"]
for text, fn, fmt in (
    ("Annualised facility fees per lender at month 60", f"=IF({nm}!${mcol(60)}${R['lenders']}=0,0,{nm}!${mcol(60)}${R['rev_f']}*12/{nm}!${mcol(60)}${R['lenders']})", F_MONEY),
    ("Facilities per lender at month 60", f"=IF({nm}!${mcol(60)}${R['lenders']}=0,0,{nm}!${mcol(60)}${R['livef']}/{nm}!${mcol(60)}${R['lenders']})", F_CNT1),
    ("Annualised fee per facility", f"={nm}!${mcol(60)}${R['fee_f']}*12", F_MONEY),
    ("Annualised revenue per paid builder job", f"=Inputs!$B${REF['price_b']}*12", F_MONEY),
    ("Year 5 lender revenue for each basis point of fee", f"={nm}!${CL(YCOL[5])}${R['rev_f']}/Inputs!$B${REF['bps']}", F_MONEY),
    ("Revenue per employee, Year 5", f"=IF({nm}!${CL(YCOL[5])}${R['head']}=0,0,{nm}!${CL(YCOL[5])}${R['rev']}/{nm}!${CL(YCOL[5])}${R['head']})", F_MONEY),
    ("Lowest cash with seed (base)", f"=MIN({nm}!${mcol(1)}${R['cash1']}:${mcol(MONTHS)}${R['cash1']})", F_MONEY),
    ("First month cash with seed goes negative, base (99 = none)", f"=MIN({nm}!${mcol(1)}${R['neg1']}:${mcol(MONTHS)}${R['neg1']})", F_INT),
    ("Lowest cash with seed (conservative)", f"=MIN({nmc}!${mcol(1)}${Rc['cash1']}:${mcol(MONTHS)}${Rc['cash1']})", F_MONEY),
    ("First month cash goes negative, conservative (99 = none)", f"=MIN({nmc}!${mcol(1)}${Rc['neg1']}:${mcol(MONTHS)}${Rc['neg1']})", F_INT),
):
    ws.cell(row=sr, column=1, value=text).font = font()
    c = ws.cell(row=sr, column=2, value=fn)
    c.number_format = fmt
    c.font = font(GREEN)
    sr += 1
sr += 1
ssec("Market (from the Market sheet)")
for text, key, fmt in (("Total market (TAM), Australia, A$M a year", "tam", F_MONEY_M), ("Serviceable (SAM), Queensland, A$M a year", "sam", F_MONEY_M),
                       ("Obtainable (SOM), month-60 run rate, base, A$M", "som_base", F_MONEY_M), ("Month-36 run rate, base, A$M", "som36_base", F_MONEY_M),
                       ("SOM as a share of TAM", "som_sh", F_PCT), ("Live projects in scope, Australia", "live_n", F_CNT), ("Live projects in scope, Queensland", "q_live", F_CNT)):
    ws.cell(row=sr, column=1, value=text).font = font()
    c = ws.cell(row=sr, column=2, value=f"=Market!$B${M[key]}")
    c.number_format = fmt
    c.font = font(GREEN)
    sr += 1

# ---------------------------------------------------------------- Read me
wr = wb.create_sheet("Read me", 0)
setw(wr, {"A": 120})
lines = [
    ("IRIS five-year model", font(bold=True, size=14)),
    ("Version of 4 November 2026 (D-37). The source for the IRIS investor deck's market and model slides and appendix A5–A6.", font(GREY, italic=True)),
    ("", None),
    ("How to use it", font(bold=True)),
    ("Change inputs on the Inputs sheet. Blue = input. Black = formula. Green = link. Yellow = owner decision. Three cases (Base, Upside, Conservative) run side by side.", font()),
    ("", None),
    ("What the model assumes", font(bold=True)),
    ("Four revenue lines. IRIS for Lenders: a lender writes IRIS into facilities as a drawdown condition; the developer pays 15 bps a year on the full project debt stack, within a floor and a cap; each lender adds new facilities each month and its existing book comes under the condition as loans re-paper. IRIS for Builders: a subscription per live job that follows the builder. IRIS for Developers: a developer-direct view for projects with no lender condition, from Year 3. Assessments: a per-engagement fee, benchmarked to QS reports, on distressed facilities on the platform and a small number won off it.", font()),
    ("The lender adoption cadence (20 by Year 5) and the per-lender facility rate are company targets, not sourced figures. The distress rate (4% a year) is an estimate. Everything else carries its source on the Inputs sheet.", font()),
    ("No R&D tax refund, no insurer or surety revenue, no interest income. Costs are paid in the month incurred. A$ excluding GST.", font()),
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
