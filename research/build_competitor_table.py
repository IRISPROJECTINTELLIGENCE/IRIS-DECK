"""Build the IRIS competitor table (one sheet, openpyxl, no formulas).

Run: python3 build_competitor_table.py <output.xlsx>
Source: research/competitive-landscape.md (about sixty products and firms, October to November 2026) and slide 9.
Plain Excel formatting, as the model workbook (D-48): Calibri 11, black text, bold headings, a thin grid on the
table, no fills. Rows auto-fit to their wrapped text.
"""
import sys
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from openpyxl.worksheet.properties import PageSetupProperties

OUT = sys.argv[1]
FONT = "Calibri"
WIDTHS = {"A": 34, "B": 72, "C": 15, "D": 12, "E": 66}
AS_AT = "26 November 2026"
THIN = Side(style="thin")
GRID = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)


def font(bold=False, size=11):
    return Font(name=FONT, bold=bold, size=size, family=2, scheme="minor")


IRIS = ("IRIS (Gold Coast)",
        "Reads the builder's systems by read-only API and reconciles them to show where a project stands on time, cost and quality, "
        "and what is putting each at risk. Each finding traces to its record. One platform for the lender and the builder.",
        "Yes", "Yes",
        "Sits beside the QS. Certifies nothing and values nothing. Proof of concept today, with an R&D partnership agreed with a Tier 2 builder.")

GROUPS = [
    ("Serves the lender, from outside the builder's systems", [
        ("Lender's QS",
         "The control lenders use today. Certifies work in place each month against the builder's claim, after a site inspection. Its report is a condition of each drawdown.",
         "No", "Yes",
         "Works from the claim and the documents the builder submits. IRIS sits beside it."),
        ("Korrix (Sydney)",
         "A monitoring service for lenders: a builder health check from public registers, then monthly meetings, site walks and a risk brief, "
         "written into the facility as a condition. Insurance cover for builder failure is in development.",
         "No", "Yes",
         "A monthly brief prepared by hand. No connection to the builder's systems. No customers named."),
        ("IPEX (Melbourne)",
         "Software on a project payment account. Sets QS-certified progress against the payments made to each trade and reports the gap. "
         "Says several lenders require its data as a condition of funding.",
         "No", "Yes",
         "Sees the payments that pass through its account. No view of cost, forecast, variations or programme."),
        ("CreditorWatch",
         "Credit bureau. Credit checks, payment defaults and alerts on the builder company.",
         "No", "Yes",
         "Rates the company. Holds no project data."),
        ("Equifax iCIRT",
         "Star ratings of builders and developers, drawn from company, licence and financial data.",
         "No", "Yes",
         "Rates the company at a point in time. Holds no project data."),
        ("SteelCap",
         "Announced as construction risk intelligence for lenders. A landing page with an early-access sign-up.",
         "Not stated", "Yes",
         f"No product, team or integrations shown as of {AS_AT}."),
    ]),
    ("Serves the lender, United States", [
        ("Built Technologies (Nashville)",
         "Construction loan administration for lenders: draws, inspections, lien waivers and budget variances, with a sync to Procore. "
         "More than 300 lenders, by its own count.",
         "Part", "Yes",
         "Reviews the draw as the borrower submits it. No Australian presence found."),
        ("Rabbet (Austin)",
         "Draw management for construction lenders, with covenant checks and budget monitoring.",
         "No", "Yes",
         "Works at the level of the loan budget. No Australian presence found."),
        ("Land Gorilla (California)",
         "Construction loan management with AI draw agents and a due-diligence review of the builder and the budget.",
         "No", "Yes",
         "Works at the level of the draw, residential loans first. No Australian presence found."),
    ]),
    ("Reads the builder's systems, for the builder", [
        ("Cintech (Australia)",
         "One record per project from the builder's systems (Aconex, Procore, Jobpac, PayApps and others), AI answers that cite their source, "
         "time-bar tracking and notice drafting.",
         "Yes", "No",
         "The builder is the customer. No lender view or cost forecast described. The closest Australian product on the builder side."),
        ("Vyne",
         "Decision intelligence for builders. Answers with sources across tenders, projects and offices, so lessons carry from one job to the next.",
         "Part", "No",
         "Aimed at tendering and retained knowledge. Early stage: no construction-system connectors or customers named."),
        ("Procore with Datagrid (United States)",
         "AI agents that read across the builder's ERP and documents, inside the platform many builders already run.",
         "Yes", "No",
         "The builder pays for it. No lender view shown. Procore is a system IRIS reads."),
        ("Trimble: Jobpac and Document Crunch (United States)",
         "Contract-obligation AI being brought into its builder ERP family, which includes Jobpac in Australia.",
         "Part", "No",
         "Stays inside Trimble's own products, for the builder. Jobpac is a system IRIS reads."),
        ("Slate Technologies (California)",
         "A decision assistant that reads the major construction platforms and links to the schedule, for Tier 1 builders.",
         "Yes", "No",
         "No product for a lender on a live project. No Australian customers found."),
        ("Octant AI (Brisbane)",
         "Machine-learning forecasts of final cost and margin from cost reports and schedules.",
         "No", "No",
         "Forecasts from summary reports. No link back to the record."),
    ]),
    ("Serves the owner or developer", [
        ("Mastt (Sydney)",
         "Project and portfolio controls for owners and their project managers: budgets, commitments, claims, risk and reporting.",
         "No", "No",
         "Runs on the owner's own ledgers. No connection to the builder's systems and no lender features."),
    ]),
    ("Beside IRIS: sources and channels", [
        ("Procore, Aconex, Jobpac, PayApps, ProcurePro",
         "The systems a builder already runs a project on.",
         "–", "No",
         "Sources IRIS reads. Each holds its own part of the project."),
        ("Lendbase",
         "A marketplace that matches commercial borrowers with lenders.",
         "No", "Yes",
         "Works before the facility is written. A possible channel to lenders."),
    ]),
    ("Also reviewed", [
        ("Builder platforms and ERPs",
         "Autodesk Construction Cloud, Cheops, CMiC, Workbench, Premier, Fieldwire, Aphex, Buildertrend, Databuild, EstimateOne, Buildxact, Simpro.",
         "–", "No",
         "The builder's own systems. Sources IRIS reads or could read."),
        ("Claims and payment tools",
         "Earlytrade, Lentune, Oracle Textura, GCPay.",
         "–", "No",
         "Claims and early payment between the builder and its trades. No lender product."),
        ("Lender software, overseas",
         "Abrigo, nCino, Brdg.",
         "No", "Yes",
         "Loan administration and draw tools. No Australian construction product found."),
        ("Services to lenders",
         "Builder due-diligence advisers; restructuring advisers (KordaMentha, McGrathNicol, FTI); trackers lenders have built in-house.",
         "No", "Yes",
         "Work done by hand: before the contract, or once a project is in distress."),
        ("Research",
         "BuildGuard AI (a university project in a CSIRO programme).",
         "No", "No",
         "Research-stage prediction of builder insolvency. No product."),
        ("Owner and developer controls",
         "Kahua, Northspyre, INGENIOUS.BUILD, InEight, Oracle Primavera, Asite.",
         "No", "No",
         "Controls on the owner's own data. No lender product."),
        ("Builder-side AI",
         "Trunk Tools, Alloovium, Briq, Enlaye, nPlan, Plexa, Deep Space, ALICE, Parspec, Pype, Kojo, Anility, Versatile.",
         "Part", "No",
         "AI for the builder's teams on documents, schedules and procurement. No lender view."),
        ("Site progress and quality",
         "Buildots, Doxel, OpenSpace, BuildPass, Visibuild, Scopey Onsite.",
         "No", "No",
         "Measure progress or quality on site, which is the QS's ground. No cost or commercial records."),
        ("Credit data",
         "Experian (illion), Dun & Bradstreet, Rapid Ratings.",
         "No", "Yes",
         "Company-level credit scores. Nothing on the project."),
    ]),
]

NOTES = [
    "Yes = connects to the builder's project systems. Part = reads some of them, or documents as submitted. No = works from outside those systems.",
    f"Basis: vendor websites and public sources, reviewed in October and November 2026; lender-side and Australian builder-side sites re-read on {AS_AT}.",
    "What each product does is the vendor's own description. Tools that builders or lenders have built in-house cannot be seen from outside.",
]

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Competitors"
for col, w in WIDTHS.items():
    ws.column_dimensions[col].width = w

ws["A1"] = "IRIS: competitive landscape"
ws["A1"].font = font(bold=True, size=14)
ws["A1"].alignment = Alignment(wrap_text=False)
ws["A2"] = f"Who else gives a lender or a builder a view of project delivery risk, what each reads, and where it stops. Head office in brackets where stated. As of {AS_AT}."
ws["A3"] = "We found no other product that reads a project's source systems and reconciles them into one position for the lender, the builder and the developer."
for ref in ("A2", "A3"):
    ws[ref].font = font()
HEAD_ROW = 5

HEAD = ["Competitor", "What it is", "Reads the builder's systems", "Serves the lender", "Where it stops"]
for i, h in enumerate(HEAD, 1):
    c = ws.cell(row=HEAD_ROW, column=i, value=h)
    c.font = font(bold=True)
    c.border = GRID
    c.alignment = Alignment(wrap_text=True, vertical="top", horizontal=("center" if i in (3, 4) else None))
ws.freeze_panes = f"A{HEAD_ROW + 1}"

row = HEAD_ROW + 1


def put(r, vals, bold_name=True):
    for i, v in enumerate(vals, 1):
        c = ws.cell(row=r, column=i, value=v)
        c.font = font(bold=(i == 1 and bold_name))
        c.border = GRID
        c.alignment = Alignment(wrap_text=True, vertical="top", horizontal=("center" if i in (3, 4) else None))


put(row, IRIS)
row += 1
for title, rows_ in GROUPS:
    for col in range(1, 6):
        c = ws.cell(row=row, column=col, value=(title if col == 1 else None))
        c.font = font(bold=True)
        # one box around the heading row, so the heading runs across the columns
        c.border = Border(top=THIN, bottom=THIN, left=(THIN if col == 1 else None), right=(THIN if col == 5 else None))
    row += 1
    for vals in rows_:
        put(row, vals, bold_name=(title != "Also reviewed"))
        row += 1

row += 1
for note in NOTES:
    ws.cell(row=row, column=1, value=note).font = font()
    row += 1

ws.page_setup.orientation = "landscape"
ws.page_setup.paperSize = ws.PAPERSIZE_A4
ws.sheet_properties.pageSetUpPr = PageSetupProperties(fitToPage=True)
ws.page_setup.fitToWidth = 1
ws.page_setup.fitToHeight = 0
ws.print_title_rows = f"{HEAD_ROW}:{HEAD_ROW}"
wb.properties.title = "IRIS: competitive landscape"
wb.properties.subject = f"Competitors and their positioning, as of {AS_AT}"
wb.properties.creator = "IRIS Intelligence Pty Ltd"
wb.properties.lastModifiedBy = "IRIS Intelligence Pty Ltd"
wb.save(OUT)
print("saved", OUT, "rows", row - 1)
