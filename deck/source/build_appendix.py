#!/usr/bin/env python3
"""Generate the sixteen appendix pages (A1-A16) of the IRIS Investment Summary.

Usage: python3 -I build_appendix.py <out_dir> [inter-variable.woff2]

Each page backs one named slide of the main deck: a one-line heading, one line that
names the slide's claim or gap, one short table, and the detail in the speaker notes.
With the font file the script also measures every text block and prints each page's
minimum height against the 808px frame (rows stretch to fill what is left).

This script produced the 26 November 2026 rebuild. The HTML in deck/source/slides/ is
the source of record once the owner has edited a page in the artifact.
"""
import html, io, json, os, re, sys

F = "font-family:Inter, Arial, sans-serif"
INK, BODY, MUTED, CORAL, RULE, RULE2 = "#0a0a0a", "#2a2a2a", "#6b6b6b", "#d03b39", "#d6d6d6", "#e6e6e6"
W, H, GAP, COLGAP = 1664, 808, 24, 28

# ---------------------------------------------------------------- content
# Cell markup: **bold lead**. A cell is a string, or (string, style) where style is
# "key" (semibold ink), "num" (right-aligned figures), "status" (semibold coral), "muted".

NOTES = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "appendix_notes.json")))

PAGES = [
 dict(id="apx-pack", num="A1", label="Appendix A1 · Backs slide 6 · The lender view",
  h2="The lender view is built around five decisions.",
  stand="**Slide 6** leaves the lender view to this round’s build. These are the decisions it serves.",
  cols=["460px", "520px", "1fr"], head=["Lender decision", "Made today on", "What IRIS adds"],
  rows=[
   [("Release a drawdown", "key"), "The QS report and the builder’s claim", "The cost and time records behind the claim"],
   [("Confirm the job can finish", "key"), "The contract price left to pay", "The builder’s own cost to finish"],
   [("Judge the completion date", "key"), "The programme, as submitted", "Delays, notices and labour on site"],
   [("Refinance or extend", "key"), "The borrower’s information", "Each risk traced to its record"],
   [("Step in when a builder fails", "key"), "Records rebuilt by hand", "Where the job stood on day one"],
  ],
  foot="Planned: live on a facility beside the lender’s QS at month 9."),

 dict(id="apx-mechanism", num="A2", label="Appendix A2 · Backs slide 4 · Beneath the QS report",
  h2="Six causes sit beneath the lender’s QS report.",
  stand="**Slide 4** shows three lines of the report. Beneath them sit six causes of cost and delay.",
  cols=["470px", "1fr", "330px"], head=["The QS reports", "What sits beneath it", "Where it lives"],
  groups=[
   ("Programme and EOTs as submitted", [
     ["**Time bars.** Notices near the deadline that decides who pays.", ("Aconex, Procore, email", "muted")],
     ["**Completion.** Labour on site and open defects.", ("Procore, Aconex", "muted")]]),
   ("Cost to complete on the contract", [
     ["**Cost not yet notified.** Delays and changes before a notice.", ("Programme, Jobpac", "muted")],
     ["**Soft forecast.** Contingency and allowances still unspent.", ("Jobpac, cost plan", "muted")],
     ["**Trades still to let.** Scope unlet while prices move.", ("ProcurePro, Jobpac", "muted")]]),
   ("Builder’s statutory declaration", [
     ["**Trades paid.** What each trade is owed, and how late.", ("PayApps, Jobpac", "muted")]]),
  ],
  foot="Basis: AIQS guidance note (2019) and founder observation."),

 dict(id="apx-since-2021", num="A3", label="Appendix A3 · Backs slide 4 · Since 2021",
  h2="Four changes since 2021 moved risk inside the project.",
  stand="**Slide 4** says more of the risk now sits inside the project. This is the evidence.",
  cols=["320px", "1fr", "560px"], head=["Change", "Effect", "Evidence"],
  rows=[
   [("Fixed prices", "key"), "The 2021–23 cost shock broke builders on fixed prices.", ("Six large builders failed, 2022–25", "muted")],
   [("Thinner builders", "key"), "Less balance sheet to absorb an overrun.", ("About a quarter of insolvencies (ASIC)", "muted")],
   [("In-house delivery", "key"), "One pool of capital takes the loss.", ("Founder observation; Bathla", "muted")],
   [("Fewer presales", "key"), "Less of the exit sold before drawdown.", ("No presales: 18% to 37% of lenders", "muted")],
  ],
  foot=None),





 dict(id="apx-landscape", num="A8", label="Appendix A8 · Backs slide 9 · The landscape",
  h2="No product found reconciles a builder’s systems for the lender.",
  stand="**Slide 9** names nine. About sixty were reviewed, October–November 2026, in six groups.",
  cols=["420px", "560px", "1fr"], head=["Group", "Examples", "Where it stops"],
  rows=[
   [("Lender-side services", "key"), "Lender’s QS, Korrix, IPEX, iCIRT", "Submissions, site walks, payments"],
   [("US lender draw tools", "key"), "Built, Rabbet, Land Gorilla", "US draws; not found in Australia"],
   [("The builder’s systems", "key"), "Procore, Aconex, Jobpac, PayApps", "What IRIS reads"],
   [("Builder-side AI", "key"), "Cintech, Vyne, Slate, Datagrid", "Serve the builder; no lender view"],
   [("Owner controls", "key"), "Mastt, Kahua, Northspyre, Octant", "The owner’s ledgers and summaries"],
   [("Restructuring advisers", "key"), "KordaMentha, McGrathNicol, FTI", "Rebuild the position by hand"],
  ],
  foot="The full table is sent with the deck."),

 dict(id="apx-recovery", num="A9", label="Appendix A9 · Backs slides 3, 6 and 11 · Assessments",
  h2="An assessment reads a troubled project’s records for a fixed fee.",
  stand="Proposed service, offered once the platform is proven. No engagement has been run.",
  cols=["300px", "1fr"], head=None,
  rows=[
   [("When", "key"), "A funded project is in distress, or its builder has failed."],
   [("Who pays", "key"), "The lender or its receiver. $35,000 in the model, benchmarked to QS fees."],
   [("What it gives", "key"), "Where the job stood, each finding traced to its record, gaps listed."],
   [("Access", "key"), "Simplest where IRIS is already on the job; else the administrator agrees."],
   [("Scale", "key"), "About 14 in Year 5, about 2% of revenue."],
  ],
  foot=None),

]
# ---------------------------------------------------------------- 26 November 2026, institutional pass
# A4-A7 and A10 rewritten; A11-A16 added. Sources are linked where the address names no lender or fund.
TGB = "https://thegoodbuilder.com.au/540-companies-in-one-day-why-the-insolvency-numbers-will-look-worse-next-year/"
ACI = "https://alternativecreditinvestor.com/2026/10/01/bathla-collapse-set-to-sharpen-investor-scrutiny-of-australian-private-credit/"
UTD_SEP = "https://www.theurbandeveloper.com/articles/bathla-update-construction-shut-down"
UTD_AUG = "https://www.theurbandeveloper.com/articles/bathla-group-administration-sydney-developer-collapse-debts-teneo-appointed"
RBA = "https://www.rba.gov.au/media-releases/2026/mr-26-30.html"
ABS = "https://www.abs.gov.au/media-centre/media-releases/cpi-rose-49-year-october-2026"
COT = "https://www.cotality.com/au/insights/articles/housing-downturn-broadens-as-brisbane-and-perth-lead-the-decline"
CU = "https://www.claytonutz.com/insights/2026/october/private-credits-stress-test-from-developer-distress-to-fund-freezes-asics-enforcement-moment-arrives"
STAM = "https://www.theurbandeveloper.com/articles/stamford-capital-lender-sentiment-construction-lending-2026"
FSC = "https://fsc.org.au/news/media-release/media-release-fsc-releases-industry-standard-for-private-markets"
ASICV = "https://asic.gov.au/about-asic/news-centre/news-items/asic-puts-private-credit-on-notice-ahead-of-30-june-valuations-and-reporting"

PAGES_NEW = {
 "apx-reach": dict(id="apx-reach", num="A4", label="Appendix A4 · Backs slide 10 · How the condition holds",
  h2="Each party has a reason to sign and a document that binds it.",
  stand="**Slide 10** assumes a lender writes IRIS into a facility. Why each party agrees, and where their interests pull apart.",
  cols=["520px", "1fr", "290px"], head=["Question", "Answer", "Status"],
  rows=[
   [("Why does the lender want it?", "key"), "Cost to finish and completion, from the records.", ("Design partner tests", "status")],
   [("Why does the developer pay?", "key"), "A condition of its debt, as the QS fee is today.", ("QS precedent", "status")],
   [("Why does the builder agree?", "key"), "A tender condition for all bidders; it sees findings first.", ("Untested", "status")],
   [("What binds each party?", "key"), "Developer: the facility. Builder: tender, contract, side deed.", ("Standard documents", "status")],
   [("A builder already under contract?", "key"), "Owes nothing new. New facilities come first.", ("By design", "status")],
   [("The lender wants the builder’s detail?", "key"), "Totals and records; rates stay with the builder.", ("Proposed rule", "status")],
   [("The developer pays, the lender relies?", "key"), "A fixed fee. IRIS reports what the records show.", ("By design", "status")],
   [("Will the drafting hold?", "key"), "Lawyers confirm the documents.", ("Month 9 opinion", "status")],
  ],
  foot=None),

 "apx-sizing": dict(id="apx-sizing", num="A5", label="Appendix A5 · Backs slide 11 · Market sizing",
  h2="The market counts each live job once, at one price.",
  stand="**Slide 11** gives $291M, $254M and $49.2M. Each step is a formula on the workbook’s Market sheet.",
  cols=["470px", "170px", "1fr"], head=["Step", ("Value", "num"), "How it is worked out"],
  rows=[
   [("Building work a year", "key"), ("$79.6bn", "num"), "Apartments $33.5bn; commercial $70.9bn × 65% on $10M+ jobs"],
   [("Value under construction", "key"), ("$173bn", "num"), "Work a year × build time: 29 and 24 months"],
   [("With a construction facility", "key"), ("$139bn", "num"), "Developer-funded: 88% and 73% (IBISWorld)"],
   [("Live jobs, at $40M average", "key"), ("4,328", "num"), "3,465 with a facility; 863 without"],
   [("Total market (TAM)", "total"), ("$291M", "numb"), "3,465 × $72K + 863 × $42K + $4.9M of assessments"],
   [("Serviceable (SAM)", "total"), ("$254M", "numb"), "The jobs with a facility: where a lender sets the condition"],
   [("Obtainable (SOM)", "total"), ("$49.2M", "numb"), "Month 60: 373 × $120K + 92 × $42K + assessments"],
  ],
  foot="$40M is the market’s average job, $48M its average facility (1.2 times), $80M the facilities IRIS targets."),

 "apx-model": dict(id="apx-model", num="A6", label="Appendix A6 · Backs slide 11 · Model assumptions",
  h2="The lender drivers set the curve; the margin follows from cost per job.",
  stand="**Slide 11** shows the base case. Each driver, the number behind it, and the reason for it.",
  cols=["430px", "210px", "1fr"], head=["Driver", ("Base case", "num"), "Why this number"],
  rows=[
   [("Lenders adopting", "key"), ("1 · 8 · 20", "num"), "Target. Five lenders hold 52% of property private credit"],
   [("New facilities per lender", "key"), ("0.8 a month", "num"), "About $770M a year: a $1.5bn construction book"],
   [("Existing loans re-signed", "key"), ("10", "num"), "Half a 20-loan book, at extension or refinance"],
   [("Fee per facility", "key"), ("$120K", "num"), "15 bps on $80M: about 1.5% of a year’s interest"],
   [("Lenders lost", "key"), ("None", "num"), "Live facilities keep the condition; one is $2.2M a year"],
   [("Contribution per facility", "key"), ("78%", "num"), "Fee less analyst, cloud, commission, onboarding"],
   [("EBITDA margin, Year 5", "key"), ("45%", "num"), "Job costs $10.7M; lender staff $4.3M; fixed $7.4M"],
   [("Revenue, Year 5", "total"), ("$40.5M", "numb"), "Months 49 to 60. Month 60 × 12 is the $49.2M run rate"],
  ],
  foot="Lenders a year late, no lender, or a late seed: A15. Each $10M of facility is about $4.6M of Year 5 revenue."),

 "apx-sources": dict(id="apx-sources", num="A7", label="Appendix A7 · Backs slides 2, 3 and 8 · Sources",
  h2="Where the deck’s public figures come from.",
  stand="Dated and linked. A sum owed to lenders is **exposure**; a write-down is a **loss** recognised so far.",
  cols=["1fr", "100px", "700px"], head=["Figure", "Slide", "Source"],
  rows=[
   [("Construction, 24.5% of insolvencies", "key"), "2, 8", f"[ASIC series 1 via The Good Builder, 22 Sep 2026]({TGB})"],
   [("Bathla: about $3.3bn owed, 40 funds", "key"), "2, 8", f"AFR; Bloomberg; [ACI, 1 Oct 2026]({ACI})"],
   [("$3.08bn owed to secured lenders", "key"), "3", f"Exposure. [The Urban Developer, 25 Sep 2026]({UTD_SEP})"],
   [("Lender of a decade out by January", "key"), "3", f"[The Urban Developer, 25 Aug 2026]({UTD_AUG})"],
   [("About $168M written down, three funds", "key"), "3", "Loss. The Urban Developer, 30 Sep 2026"],
   [("Cash rate, CPI, dwelling values", "key"), "2, 8", f"[RBA, 3 Nov]({RBA}); [ABS, 25 Nov]({ABS}); [Cotality, 2 Nov]({COT})"],
   [("ASIC review and enforcement warning", "key"), "8", f"[Clayton Utz, 1 Oct 2026]({CU}); The Nightly, 30 Sep"],
   [("Presales and lending terms", "key"), "8", f"[Stamford survey, 2026]({STAM}); Gravity Capital, 25 Oct"],
   [("Valuation standard from July 2027", "key"), "8", f"[FSC Standard 30, 26 Aug 2026]({FSC}); [ASIC, 18 Jun]({ASICV})"],
   [("Replacement builder prices 20–40%", "key"), "3", ("Founder experience, unmeasured", "muted")],
  ],
  foot=None),

 "apx-risks": dict(id="apx-risks", num="A10", label="Appendix A10 · Backs slide 13 · Risks the round retires",
  h2="The round answers seven questions, each by a set month.",
  stand="**Slide 13**’s milestones, read as the risks they retire. The first four are what the build is for.",
  cols=["620px", "1fr", "170px"], head=["Question", "Answered by", ("Month", "num")],
  rows=[
   [("Does it reconcile on live data?", "key"), "The pass marks on A14, on our partner’s jobs", ("6", "num")],
   [("Will builders pay for it?", "key"), "The first paying builders", ("6", "num")],
   [("Will a lender’s security review pass?", "key"), "An independent audit and penetration test", ("6", "num")],
   [("Will a lender use it beside its QS?", "key"), "A scoped lender view on one live facility", ("9", "num")],
   [("Will the documents hold?", "key"), "A legal opinion on the condition and side deed", ("9", "num")],
   [("Will a lender write it in?", "key"), "The first drawdown condition. A target", ("12", "num")],
   [("Is the next round fundable?", "key"), "A seed on paid use, with or without a lender", ("15–18", "num")],
  ],
  foot="Month 9 needs a scoped lender view brought forward in the build plan (A12). Costs of delay: A15."),

 "apx-status": dict(id="apx-status", num="A11", label="Appendix A11 · Backs slide 2 · Where we are",
  h2="What is built, what is agreed, and what is still a target.",
  stand="**Slide 2** gives the status in one line. Each item here is classed by the evidence behind it.",
  cols=["430px", "1fr", "330px"], head=["Item", "Detail", "Status"],
  rows=[
   [("Proof of concept", "key"), "A fictional project on a Procore sandbox (slide 7)", ("Built", "status")],
   [("R&D partner builder", "key"), "SEQ Tier 2; real project data; unpaid", ("Agreed", "status")],
   [("Engineering partner", "key"), "Builds the enterprise product", ("In negotiation", "status")],
   [("Builder feedback", "key"), "A Tier 1 senior contracts manager, in writing", ("Received, May 2026", "status")],
   [("Lender interest", "key"), "A non-bank fund called the lender view useful", ("Discussion; no letter", "status")],
   [("Paying builders", "key"), "None yet. Two from month 6", ("Target", "status")],
   [("Lender on a live facility", "key"), "None yet. The design partner, month 9", ("Target", "status")],
   [("First drawdown condition", "key"), "None yet. Month 12", ("Target", "status")],
  ],
  foot="Pre-revenue. Not claimed: paying customers, a mandate, an accuracy figure or a security certificate."),

 "apx-architecture": dict(id="apx-architecture", num="A12", label="Appendix A12 · Backs slides 6 and 7 · Architecture",
  h2="Rules produce each finding; models read and explain the records.",
  stand="**Slides 6 and 7** show the product. How it is built and what exists today; R1 to R7 are its releases, in order.",
  cols=["470px", "1fr", "330px"], head=["Layer", "What it does", "Status"],
  rows=[
   [("Connectors", "key"), "Read-only API access; nothing written back", ("Procore, proof of concept", "status")],
   [("Canonical project model", "key"), "One model of the job, whatever the vendor", ("In build, R1", "status")],
   [("Verification checks", "key"), "Rules held as data; each finding keeps one ID", ("In build, R1", "status")],
   [("Evidence links", "key"), "Each finding opens the records behind it", ("Proof of concept", "status")],
   [("Isolation, roles, audit log", "key"), "Each customer walled off; each read logged", ("R1 and R2", "status")],
   [("Correspondence and email", "key"), "Notices and claims read into the model", ("Planned, R3", "status")],
   [("Chat over the records", "key"), "Answers cite records; says when it cannot tell", ("Demo; R4", "status")],
   [("Aconex, ProcurePro, PayApps", "key"), "More systems on the same framework", ("Planned, R5", "status")],
   [("Lender and developer views", "key"), "Scoped views behind an audited boundary", ("Planned, R7", "status")],
  ],
  foot="The moat: the project model and its library of checks, which a follower must rebuild, and the condition in lenders’ documents."),

 "apx-security": dict(id="apx-security", num="A13", label="Appendix A13 · Backs slides 6 and 10 · Security and reliance",
  h2="The builder grants access, and each read of its data is logged.",
  stand="What a lender’s security and credit teams will ask, and how IRIS answers.",
  cols=["430px", "1fr", "300px"], head=["Requirement", "How IRIS meets it", "Status"],
  rows=[
   [("Hosting", "key"), "Azure, Australia; encrypted in transit and at rest", ("R1", "status")],
   [("Access", "key"), "The builder authorises each connection, read-only", ("By design", "status")],
   [("Who sees what", "key"), "Lender: its job, as totals and records; rates stay", ("Proposed rule", "status")],
   [("Isolation", "key"), "Each customer’s data walled off and tested", ("R2", "status")],
   [("Audit trail", "key"), "Each data access logged; findings keep history", ("R1", "status")],
   [("Data handling", "key"), "Builder controls, IRIS processes; deleted on exit", ("Before live use", "status")],
   [("Assurance", "key"), "Security audit and penetration test", ("After the raise", "status")],
   [("Reliance", "key"), "The builder’s records, reconciled and dated", ("Terms of use", "status")],
   [("Insurance", "key"), "Professional indemnity and cyber cover", ("Before paid use", "status")],
  ],
  foot="IRIS values and certifies nothing. The QS, the valuer and the lender’s credit judgement stay."),

 "apx-pilot": dict(id="apx-pilot", num="A14", label="Appendix A14 · Backs slides 7 and 13 · Pilot pass marks",
  h2="The pilot passes or fails on measures set before it starts.",
  stand="Proposed for the R&D pilot, to be agreed with the builder. **None has been measured yet.**",
  cols=["390px", "1fr", "360px"], head=["Measure", "Pass mark", "Measured against"],
  rows=[
   [("Agreement to source", "key"), "Totals agree, three months running", ("The builder’s cost report", "muted")],
   [("Traceability", "key"), "Each figure opens its source record", ("A sample audit", "muted")],
   [("Precision", "key"), "8 in 10 findings confirmed real", ("The builder’s commercial team", "muted")],
   [("Recall", "key"), "9 in 10 items in the risk register found", ("The builder’s risk register", "muted")],
   [("Lead time", "key"), "Median 30 days before the cost report", ("Live jobs; historic records", "muted")],
   [("Time bars", "key"), "Each delay event flagged before its deadline", ("The contract’s notice periods", "muted")],
   [("Commercial value", "key"), "Exposure the team did not hold, 10 times the fee", ("The builder’s sign-off", "muted")],
   [("Conversion", "key"), "The builder pays from month 6", ("An invoice", "muted")],
  ],
  foot="The time-bar and commercial-value marks are the two uses a Tier 1 senior contracts manager named (A11)."),

 "apx-downside": dict(id="apx-downside", num="A15", label="Appendix A15 · Backs slides 11 and 13 · Downside cases",
  h2="If lenders come a year late, Year 5 is $24M and cash holds.",
  stand="Each case re-runs the base model. Costs follow the plan as written; in practice hiring waits for lenders.",
  cols=["1fr", "190px", "190px", "460px"], head=["Case", ("Revenue Y5", "num"), ("EBITDA Y5", "num"), "Cash"],
  rows=[
   [("Base case", "key"), ("$40.5M", "num"), ("$18.1M", "num"), "Lowest $261K, before the seed"],
   [("Lenders twelve months later", "key"), ("$24.1M", "num"), ("$7.1M", "num"), "Lowest $260K"],
   [("No lender in five years", "key"), ("$3.4M", "num"), ("−$5.3M", "num"), "Hiring for lenders stops by month 38"],
   [("Each lender stops after three years", "key"), ("$39.5M", "num"), ("$17.5M", "num"), "Lowest $261K"],
   [("Seed at month 21", "key"), ("$40.5M", "num"), ("$18.1M", "num"), "Below zero from month 20"],
   [("Seed of $1.5M", "key"), ("$40.5M", "num"), ("$18.1M", "num"), "Lowest $261K"],
   [("No seed", "key"), ("$40.5M", "num"), ("$18.1M", "num"), "Below zero, months 20 to 27"],
   [("Lenders late and a $1.5M seed at month 21", "key"), ("$24.1M", "num"), ("$7.1M", "num"), "Below zero from month 19"],
  ],
  foot="The seed’s timing matters more than its size: it needs to land by month 19, or hiring after month 16 waits."),

 "apx-round": dict(id="apx-round", num="A16", label="Appendix A16 · Backs slide 13 · Terms and runway",
  h2="The round covers 13 months of costs before any revenue.",
  stand="**Slide 13** gives the use of funds. The terms, the runway and what the seed depends on.",
  cols=["430px", "1fr", "320px"], head=["Term", "Detail", "Status"],
  rows=[
   [("Instrument", "key"), "A SAFE for A$750K", ("Set", "status")],
   [("Valuation cap", "key"), "A$4M", ("Set", "status")],
   [("Cap basis, discount, pro rata", "key"), "Pre- or post-money; any discount; MFN", ("To confirm", "status")],
   [("Enterprise build", "key"), "$320K with an engineering partner", ("Quote pending", "status")],
   [("Directors", "key"), "Full-time from close, $100K each plus super", ("Set", "status")],
   [("Runway", "key"), "13 months of the plan’s costs, no revenue", ("Model", "status")],
   [("Seed", "key"), "$3M at month 15; needed by month 19", ("Plan", "status")],
  ],
  foot="With the plan’s revenue, cash stays above $261K before the seed. Cases with a late or smaller seed: A15."),
}
NEW_ORDER = ["apx-status", "apx-architecture", "apx-security", "apx-pilot", "apx-downside", "apx-round"]

BY_ID = {p['id']: p for p in PAGES}
BY_ID.update(PAGES_NEW)
PAGES = [BY_ID[i] for i in ["apx-pack", "apx-mechanism", "apx-since-2021", "apx-reach", "apx-sizing", "apx-model", "apx-sources", "apx-landscape", "apx-recovery", "apx-risks"] + NEW_ORDER]
for _pg in PAGES: _pg["notes"] = NOTES[_pg["id"]]

ORDER = [p["id"] for p in PAGES]

# ---------------------------------------------------------------- html
LINK = re.compile(r"\[([^\]]+)\]\((https://[^)\s]+)\)")
def esc(s): return html.escape(s, quote=False)
def plain(s): return LINK.sub(r"\1", s)
def runs(s):
    out = []
    for i, part in enumerate(re.split(r"\*\*(.+?)\*\*", plain(s))):
        if part: out.append((part, 600 if i % 2 else 400))
    return out
def links(part):
    out, pos = [], 0
    for m in LINK.finditer(part):
        out.append(esc(part[pos:m.start()])); out.append(f'<a href="{html.escape(m.group(2), quote=True)}">{esc(m.group(1))}</a>'); pos = m.end()
    return "".join(out) + esc(part[pos:])
def inline(s):
    out = []
    for i, part in enumerate(re.split(r"\*\*(.+?)\*\*", s)):
        if part: out.append(f"<b>{links(part)}</b>" if i % 2 else links(part))
    return "".join(out)
def norm(c): return c if isinstance(c, tuple) else (c, "body")

CELL = {
 "body":   f"{F}; font-size:24px; line-height:1.35; color:{BODY}",
 "muted":  f"{F}; font-size:24px; line-height:1.35; color:{MUTED}",
 "key":    f"{F}; font-size:24px; font-weight:600; line-height:1.35; color:{INK}",
 "total":  f"{F}; font-size:24px; font-weight:600; line-height:1.35; color:{CORAL}",
 "status": f"{F}; font-size:24px; font-weight:600; line-height:1.35; color:{CORAL}",
 "num":    f"{F}; font-size:24px; line-height:1.35; text-align:right; font-variant-numeric:tabular-nums; color:{INK}",
 "numb":   f"{F}; font-size:24px; font-weight:600; line-height:1.35; text-align:right; font-variant-numeric:tabular-nums; color:{INK}",
}
HEAD = f"{F}; font-size:24px; font-weight:600; line-height:1.2; letter-spacing:3px; text-transform:uppercase; color:{MUTED}"
ROWPAD = 8

def p(text, style): return f'<p style="{style}">{inline(text)}</p>'
def grid(cols): return f"display:grid; grid-template-columns:{' '.join(cols)}; gap:{COLGAP}px"

def head_row(pg):
    cells = []
    for c in pg["head"]:
        t, st = norm(c)
        cells.append(f'<p style="{HEAD}{"; text-align:right" if st == "num" else ""}">{esc(t)}</p>')
    return f'    <div style="{grid(pg["cols"])}; padding:0 0 12px; border-bottom:2px solid {INK}">\n      ' + "\n      ".join(cells) + "\n    </div>"

def body_row(pg, row, first):
    total = norm(row[0])[1] == "total"
    border = f"border-top:2px solid {INK}" if total else ("" if first else f"border-top:1px solid {RULE}")
    cells = [p(*[norm(c)[0], CELL[norm(c)[1]]]) for c in row]
    st = f'{grid(pg["cols"])}; align-items:center; flex:1; padding:{ROWPAD}px 0' + (f"; {border}" if border else "")
    return f'    <div style="{st}">\n      ' + "\n      ".join(cells) + "\n    </div>"

def group_block(pg, label, rows, first):
    c0, c1, c2 = pg["cols"]
    border = "" if first else f"; border-top:1px solid {RULE}"
    inner = []
    for i, row in enumerate(rows):
        b = "" if i == 0 else f"; border-top:1px solid {RULE2}"
        cells = [p(norm(c)[0], CELL[norm(c)[1]]) for c in row]
        inner.append(f'        <div style="{grid([c1, c2])}; align-items:center; flex:1; padding:{ROWPAD}px 0{b}">\n          ' + "\n          ".join(cells) + "\n        </div>")
    return (f'    <div style="{grid([c0, "1fr"])}; flex:{len(rows)}{border}">\n'
            f'      <div style="display:flex; flex-direction:column; justify-content:center">\n        {p(label, CELL["key"])}\n      </div>\n'
            f'      <div style="display:flex; flex-direction:column">\n' + "\n".join(inner) + "\n      </div>\n    </div>")

def page_html(pg):
    out = [f'<section id="{pg["id"]}" data-transition="fade" style="display:flex; flex-direction:column; gap:{GAP}px; padding:112px 128px 160px; background:#ffffff">']
    out.append(f'  <p data-iris-label="1" style="position:absolute; top:62px; left:128px; width:1500px; {F}; font-size:24px; font-weight:600; line-height:1; letter-spacing:3px; text-transform:uppercase; color:{INK}">{esc(pg["label"])}</p>')
    out.append(f'  <h2 style="{F}; font-size:52px; font-weight:600; line-height:1.1; letter-spacing:-1px; color:{INK}">{esc(pg["h2"])}</h2>')
    out.append(f'  <p style="{F}; font-size:26px; line-height:1.4; color:{BODY}">{inline(pg["stand"])}</p>')
    out.append('  <div style="display:flex; flex-direction:column; flex:1">')
    if pg.get("head"): out.append(head_row(pg))
    if "groups" in pg:
        for i, (label, rows) in enumerate(pg["groups"]): out.append(group_block(pg, label, rows, i == 0))
    else:
        for i, row in enumerate(pg["rows"]): out.append(body_row(pg, row, i == 0 and bool(pg.get("head"))))
    out.append("  </div>")
    if pg.get("foot"): out.append(f'  <p style="{F}; font-size:24px; line-height:1.42; color:{MUTED}">{inline(pg["foot"])}</p>')
    out.append(f'  <p style="position:absolute; right:128px; bottom:64px; width:200px; {F}; font-size:24px; text-align:right; color:{MUTED}">{pg["num"]}</p>')
    out.append(f'  <aside>{esc(pg["notes"])}</aside>')
    out.append("</section>\n")
    return "\n".join(out)

# ---------------------------------------------------------------- measurement
def colpx(cols, total=W):
    fixed = sum(int(c[:-2]) for c in cols if c.endswith("px")); fr = sum(float(c[:-2]) for c in cols if c.endswith("fr"))
    rest = total - fixed - COLGAP * (len(cols) - 1)
    return [int(c[:-2]) if c.endswith("px") else rest * float(c[:-2]) / fr for c in cols]

def make_measurer(font_path):
    from fontTools.ttLib import TTFont
    import uharfbuzz as hb
    tt = TTFont(font_path); buf = io.BytesIO(); tt.flavor = None; tt.save(buf)
    face = hb.Face(hb.Blob(buf.getvalue())); upem = face.upem
    def width(text, size, wght, ls=0.0):
        if not text: return 0.0
        f = hb.Font(face); f.set_variations({"wght": wght, "opsz": max(14, min(32, size))})
        b = hb.Buffer(); b.add_str(text); b.guess_segment_properties(); hb.shape(f, b, {"kern": True, "liga": True})
        return sum(g.x_advance for g in b.glyph_positions) / upem * size + ls * len(text)
    def linew(line, size, ls):
        segs = []
        for t, w in line:
            if segs and segs[-1][1] == w: segs[-1][0] += t
            else: segs.append([t, w])
        segs[-1][0] = segs[-1][0].rstrip(" ")
        return sum(width(t, size, w, ls) for t, w in segs)
    def lines(rs, size, maxw, ls=0.0):
        toks = []
        for text, w in rs:
            cur = ""
            for ch in text:
                cur += ch
                if ch in " -": toks.append((cur, w)); cur = ""
            if cur: toks.append((cur, w))
        out, cur = [], []
        for tok in toks:
            if cur and linew(cur + [tok], size, ls) > maxw: out.append(cur); cur = [tok]
            else: cur = cur + [tok]
        if cur: out.append(cur)
        return len(out), [round(linew(l, size, ls)) for l in out]
    return lines

def measure(pg, lines):
    rep = []; wght = lambda st: 600 if st in ("key", "total", "status", "numb") else 400
    def cell_lines(c, w):
        t, st = norm(c)
        if not t: return 1, [0]
        rs = runs(t) if st in ("body", "muted") else [(plain(t), wght(st))]
        return lines(rs, 24, w)
    n, ws = lines([(pg["h2"], 600)], 52, W, -1.0); h = n * 52 * 1.1; rep.append(f"h2 {n} line(s) {ws}")
    n, ws = lines(runs(pg["stand"]), 26, W); h += GAP + n * 26 * 1.4; rep.append(f"standfirst {n} line(s) {ws}")
    n, ws = lines([(pg["label"].upper(), 600)], 24, 1500, 3.0); rep.append(f"label {n} line(s) {ws}")
    table = 0.0; px = colpx(pg["cols"])
    if pg.get("head"):
        m = 1
        for c, w in zip(pg["head"], px):
            n, ws = lines([(norm(c)[0].upper(), 600)], 24, w, 3.0); m = max(m, n)
            if n > 1: rep.append(f"  HEADER WRAPS: {norm(c)[0]} {ws} / {round(w)}")
        table += m * 24 * 1.2 + 12 + 2
    def row_h(row, widths, tag):
        m = 1
        for c, w in zip(row, widths):
            n, ws = cell_lines(c, w); m = max(m, n)
            if n > 1: rep.append(f"  {n} lines: {tag} | {norm(c)[0][:60]} {ws} / {round(w)}")
            elif ws[0] > w - 12 and norm(c)[0]: rep.append(f"  tight: {tag} | {norm(c)[0][:60]} {ws} / {round(w)}")
        return m * 24 * 1.35 + 2 * ROWPAD + 1
    if "groups" in pg:
        inner = colpx([pg["cols"][1], pg["cols"][2]], W - px[0] - COLGAP)
        for label, rows in pg["groups"]:
            n, ws = lines([(label, 600)], 24, px[0])
            if n > 1: rep.append(f"  {n} lines: group label | {label} {ws} / {round(px[0])}")
            table += max(sum(row_h(r, inner, label[:14]) for r in rows), n * 24 * 1.35 + 2 * ROWPAD)
        nrows = sum(len(r) for _, r in pg["groups"])
    else:
        for r in pg["rows"]: table += row_h(r, px, norm(r[0])[0][:22])
        nrows = len(pg["rows"])
    h += GAP + table
    if pg.get("foot"):
        n, ws = lines(runs(pg["foot"]), 24, W); h += GAP + n * 24 * 1.42; rep.append(f"footer {n} line(s) {ws}")
    spare = H - h
    rep.insert(0, f"{pg['num']:4s} {pg['id']:16s} min height {h:6.1f} / {H}  spare {spare:6.1f}  (+{spare / nrows:4.1f}px a row over {nrows} rows)" + ("   OVER" if spare < 0 else ""))
    return rep

BANNED = re.compile(r"\b(nobody|every|never|always|guarantees|prevents|real time|real-time)\b|(?<!read-)\bonly\b", re.I)

def main():
    out_dir = sys.argv[1]; os.makedirs(out_dir, exist_ok=True)
    lines = make_measurer(sys.argv[2]) if len(sys.argv) > 2 else None
    problems = 0
    for pg in PAGES:
        s = page_html(pg)
        open(os.path.join(out_dir, pg["id"] + ".html"), "w").write(s)
        face = plain(" ".join([pg["label"], pg["h2"], pg["stand"], pg.get("foot") or ""] + [norm(c)[0] for c in (pg.get("head") or [])]
                        + [norm(c)[0] for r in pg.get("rows", []) for c in r] + [g for g, _ in pg.get("groups", [])]
                        + [norm(c)[0] for _, rs in pg.get("groups", []) for r in rs for c in r]))
        words = len(re.findall(r"[\w$%’'.,–-]+", face.replace("**", "")))
        for where, text in (("face", face), ("notes", pg["notes"])):
            for m in BANNED.finditer(text): print(f"BANNED in {pg['num']} {where}: {m.group(0)!r} …{text[max(0, m.start() - 30):m.end() + 20]}…"); problems += 1
        if len(pg["notes"]) > 4000: print(f"NOTES TOO LONG {pg['num']}: {len(pg['notes'])}"); problems += 1
        if re.search(r"font-size:(?:[0-9]|1[0-9]|2[0-3])px", s): print(f"TEXT BELOW 24px in {pg['num']}"); problems += 1
        print(f"{pg['num']:4s} {words:4d} words on the page, notes {len(pg['notes'])} chars")
        if lines:
            rep = measure(pg, lines); print("\n".join("   " + r for r in rep))
            problems += sum("OVER" in r or "WRAPS" in r for r in rep)
    print(f"\n{len(PAGES)} pages written to {out_dir}; {problems} problem(s)")
    return 1 if problems else 0

if __name__ == "__main__":
    sys.exit(main())
