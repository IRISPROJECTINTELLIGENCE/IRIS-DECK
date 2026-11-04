"""IRIS deck v3 (D-35): lender-first, one platform two products. Writes deck/source/slides and deck.json."""
import os, json
OUT = "/home/claude/iris-deck/deck/source/slides"
F = "font-family:Inter, Arial, sans-serif;"
INK, BODY, MUTED, CORAL, CORAL2, RULE, PANEL, PANEL2 = "#1a1714", "#3d3934", "#6f6a63", "#e8533a", "#c2412a", "#d9d4ca", "#f1ede4", "#f8e6dd"
G = '<span style="color:#6f6a63">'

def label(text):
    return (f'  <p data-iris-label="1" style="position:absolute; top:62px; left:128px; width:1200px; {F} font-size:24px; '
            f'font-weight:600; line-height:1; letter-spacing:3px; text-transform:uppercase; color:{CORAL2}">{text}</p>\n')

def pageno(n):
    return (f'  <p style="position:absolute; right:128px; bottom:64px; width:200px; {F} font-size:24px; text-align:right; '
            f'color:{MUTED}">{n}</p>\n')

def h2(text, size=64, coral=None):
    s = f'  <h2 style="{F} font-size:{size}px; font-weight:600; line-height:1.1; letter-spacing:-1.5px; color:{INK}">{text}'
    if coral:
        s += f'<br><span style="color:{CORAL}">{coral}</span>'
    return s + '</h2>\n'

def p(text, size=26, color=BODY, lh=1.4, extra=""):
    return f'  <p style="{F} font-size:{size}px; line-height:{lh}; color:{color};{extra}">{text}</p>\n'

def caps(text, color=MUTED, size=24, extra=""):
    return (f'<p style="{F} font-size:{size}px; font-weight:600; line-height:1.3; letter-spacing:3px; text-transform:uppercase; '
            f'color:{color};{extra}">{text}</p>')

def section(sid, body, gap=32, aside=""):
    return (f'<section id="{sid}" data-transition="fade" style="display:flex; flex-direction:column; gap:{gap}px; '
            f'padding:112px 128px 160px; background:#faf7f0">\n{body}  <aside>{aside}</aside>\n</section>\n')

def rows(items, first_col, pad=18, size=26):
    b = '  <div style="display:flex; flex-direction:column">\n'
    for i, (k, t) in enumerate(items):
        bt = f"2px solid {INK}" if i == 0 else f"1px solid {RULE}"
        b += (f'    <div style="display:grid; gap:24px; grid-template-columns:{first_col}px 1fr; padding:{pad}px 0; border-top:{bt}">\n'
              f'      {caps(k, INK)}\n      <p style="{F} font-size:{size}px; line-height:1.4; color:{INK}">{t}</p>\n    </div>\n')
    return b + '  </div>\n'

def stats(cards, num=96, gap=56):
    b = f'  <div style="display:flex; flex-direction:row; gap:{gap}px">\n'
    for n, nc, t, c in cards:
        b += (f'    <div style="display:flex; flex-direction:column; gap:14px; flex:1; padding:22px 0 0; border-top:3px solid {INK}">\n'
              f'      <p style="{F} font-size:{num}px; font-weight:600; line-height:1; letter-spacing:-4px; color:{nc}">{n}</p>\n'
              f'      <p style="{F} font-size:24px; font-weight:600; line-height:1.3; color:{INK}">{t}</p>\n'
              f'      <p style="{F} font-size:24px; line-height:1.4; color:{BODY}">{c}</p>\n    </div>\n')
    return b + '  </div>\n'

S = {}

# 01 cover ------------------------------------------------------------------
c = open(os.path.join(OUT, "cover.html"), encoding="utf-8").read()
# cover line is the owner's; left as published
# thesis sentence is the owner's; left as published
              "IRIS reads the systems a construction project already runs and shows the people funding it where the project stands, as it happens.")
assert "A risk tool" in c
S["cover"] = c

# 02 problem ----------------------------------------------------------------
b = label("The problem") + pageno("02")
b += h2("Between financial close and practical completion,", coral="the lender is the last to know.")
b += p("A lender funds most of a project and watches it through a monthly certificate prepared from the builder’s own submissions. When the project gets into trouble, the lender finds out after the builder, after the developer, and often after the money has gone.", 30, BODY, 1.4)
b += stats([
    ("$3.08bn", CORAL, "Owed to secured lenders", f"When one builder-developer entered administration in August 2026; about 40 private credit funds exposed {G}(reported)</span>"),
    ("1 in 4", INK, "Australian insolvencies are construction", f"3,472 of 14,153 in FY2025–26 {G}(ASIC)</span>"),
    ("20–40%", INK, "Replacement-builder premium", "The extra cost of finishing a failed project with a new builder. Part of it is the price of what the newcomer cannot see. Founder experience"),
])
b += '  <div style="flex:1"></div>\n'
b += p("Grocon 2020 · Probuild 2022 · Condev 2022 · PBS 2023 · Porter Davis 2023 · St Hilliers 2024 · Roberts Co 2025 · Bathla 2026. Sources in the appendix.", 24, MUTED)
S["stakes"] = section("stakes", b, 32, "Bathla figures from the administrator's updates as reported by The Urban Developer on 25 September 2026: about $3.08bn owed to secured lenders within about $3.4bn of total creditor debt; about $736m of inter-company balances still being reconciled a month in; about 40 private credit funds exposed. Construction's share of insolvencies: ASIC series 1, FY2025–26, 24.5 per cent. The replacement-builder premium of 20 to 40 per cent is founder experience, not a measured figure. Scope: IRIS reads a project's builder systems; on a failed group's project it would show that project's trades owed against what was claimed and certified, and its cost position against forecast. The group's inter-company position is the administrator's reconciliation.")

# 03 why --------------------------------------------------------------------
chain = [
    ("The builder’s systems", "hold the records: variations, notices, trades let, claims, payments, forecast."),
    ("The builder’s monthly report", "is written from those records, by the builder."),
    ("The lender’s QS", "certifies the claim from a site visit and the builder’s submissions. Not independently verified."),
    ("The lender", "funds the drawdown on the certificate, weeks after the records moved."),
]
b = label("The problem · why") + pageno("03")
b += h2("The information exists. It travels by hand, through the party it reports on.")
b += '  <div style="display:flex; flex-direction:row; gap:16px; align-items:stretch">\n'
for i, (t, c2) in enumerate(chain):
    bg = PANEL2 if i == 3 else PANEL
    bl = f"border-left:3px solid {CORAL}" if i == 3 else f"border-left:3px solid {INK}"
    b += (f'    <div style="display:flex; flex-direction:column; gap:10px; flex:1; padding:24px 24px 28px; background:{bg}; {bl}">\n'
          f'      <p style="{F} font-size:26px; font-weight:600; line-height:1.3; color:{INK}">{t}</p>\n'
          f'      <p style="{F} font-size:24px; line-height:1.4; color:{BODY}">{c2}</p>\n    </div>\n')
    if i < 3:
        b += ('    <svg xmlns="http://www.w3.org/2000/svg" aria-label="arrow" viewBox="0 0 24 16" style="width:24px; height:16px; align-self:center; flex:none">'
              '<path d="M0 8H18" stroke="#1A1714" stroke-width="2" fill="none"/><path d="M12 2L20 8L12 14" stroke="#1A1714" stroke-width="2" fill="none"/></svg>\n')
b += '  </div>\n'
b += p("The certificate is not wrong. It is late and narrow. It does not carry notices approaching their time bar, cost moving before it is notified, contingency already spent, or trades owed more than the builder has claimed.", 28, INK)
b += p("That last one is usually the first sign of a builder in trouble, and the lender sees it last.", 28, CORAL2)
b += '  <div style="flex:1"></div>\n'
b += p("Founder observation from work inside builders across arm’s-length, joint-venture and in-house delivery. Row-by-row detail in the appendix.", 24, MUTED)
S["mechanism"] = section("mechanism", b, 32, "The chain: five systems hold the records (Procore or Aconex, Jobpac, PayApps, ProcurePro, email and the share drive); the builder's team writes the monthly report from them (the internal cost report and the PCG report to the client); the lender's quantity surveyor values work in place from a site inspection and checks the claim against the contract sum, working from the claim, the variation and EOT registers as submitted, the statutory declaration that trades are paid and the builder's programme, and reports that the information was not independently verified and that no allowance is made for defects; the lender funds the drawdown on that certificate. What sits beneath it, by cause: entitlement at the time bar; forecast movement not yet notified and the prelims it extends; how much of forecast final cost is still contingency and provisional sums; market exposure in the trades; completion risk; and cash strain in the trades, what subcontractors are owed against what the builder has claimed and been paid, usually the first sign of a builder in trouble. Since 2021, fixed prices, thinner builders and in-house delivery have moved more of the risk inside the project while the lender's view stayed a certificate on the head contract (appendix A3). Appendix A2 carries the row-by-row table.")

# 04 evidence ---------------------------------------------------------------
b = label("Evidence") + pageno("04")
b += h2("On three real jobs, the lender was months behind the records.")
b += p("Real case studies with indicative data. Names, values and delivery models altered.", 26, MUTED)
ev = [
    ("Project A · $45M mixed-use", "$4.4M", CORAL, "More cost in the builder’s ledger than in the lender’s pack, at a third complete. The lender saw it about nine months later, while deciding whether the facility was in balance."),
    ("Project B · $300M residential tower", "$0", INK, "Delay buffer left on a $110M contract carrying $35M of change. The lender was a monthly pack behind, more than thirty times, when it set the refinance terms."),
    ("Project C · $15M commercial", "12 days", INK, "From claim to cash, with the delay contingency gone at three-quarters of the programme. The lender’s position was typed by hand from the builder’s PDF each month."),
]
b += '  <div style="display:flex; flex-direction:row; gap:56px">\n'
for t, n, nc, c2 in ev:
    b += (f'    <div style="display:flex; flex-direction:column; gap:14px; flex:1; padding:20px 0 0; border-top:3px solid {INK}">\n'
          f'      {caps(t)}\n'
          f'      <p style="{F} font-size:80px; font-weight:600; line-height:1; letter-spacing:-3px; color:{nc}">{n}</p>\n'
          f'      <p style="{F} font-size:24px; line-height:1.4; color:{BODY}">{c2}</p>\n    </div>\n')
b += '  </div>\n  <div style="flex:1"></div>\n'
b += p("Evidence of the problem, not of IRIS. This round rebuilds the position on these files.", 24, MUTED)
S["evidence"] = section("evidence", b, 32, "Three private record sets, held by the founders and read in full: a builder's share drive (cost-system exports, registers, claims, programmes, cashflows, PCG reports, the lender's QS initial report and the bank's term sheet); a developer's PCG pack and its capital partner's feasibility; a lender's QS drawdown report, payment certificates, PCG to the financier and trust investor report. Figures, contract sizes, delivery-model labels and lags are altered so the projects cannot be identified; the structure of each issue is as found. Project A: the builder's internal forecast ran ahead of the figure in the developer's PCG pack for about a year, with a $1.5M delay claim not yet submitted and $5.8M of finishes trades unlet. Project B: a delay-incentive pool consumed to the dollar by approved wet-weather days, with the bank refinancing in at about three-quarters complete. Project C: a small commercial job under a private financier with QS-gated drawdowns, delay contingency fully used with a fifth of the programme to run, the monthly dashboard typed by hand with formula errors in the working files. These are illustrative examples of the problem; they are not outcomes IRIS has delivered.")

# 05 product ----------------------------------------------------------------
b = label("The product") + pageno("05")
b += h2("IRIS reads the builder’s systems and shows the lender", coral="the position beneath the certificate.")
b += '  <div style="display:flex; flex-direction:row; gap:64px">\n'
b += (f'    <div style="display:flex; flex-direction:column; gap:16px; width:620px; flex:none; padding:26px 30px 30px; background:{PANEL}">\n'
      f'      {caps("How it connects")}\n'
      f'      <p style="{F} font-size:26px; line-height:1.4; color:{INK}">Read-only connections, authorised by the builder, to Procore or Aconex, Jobpac, PayApps, ProcurePro and the inbox.</p>\n'
      f'      <p style="{F} font-size:26px; line-height:1.4; color:{INK}">Nothing is installed. Nothing is written back. The QS and the site visit stay.</p>\n    </div>\n')
b += '    <div style="display:flex; flex-direction:column; flex:1">\n      ' + caps("What the lender sees, continuously") + '\n'
for i, t in enumerate([
    "Claimed, certified, paid and owed to the trades, side by side.",
    "Forecast final cost against the ledger, and how much of it is still contingency.",
    "Notices, variations and delays, dated against their time bars.",
    "Each figure linked to the record it came from.",
]):
    bt = f"2px solid {INK}" if i == 0 else f"1px solid {RULE}"
    b += f'      <p style="{F} font-size:28px; line-height:1.4; color:{INK}; padding:14px 0; border-top:{bt}; margin-top:{10 if i == 0 else 0}px">{t}</p>\n'
b += '    </div>\n  </div>\n  <div style="flex:1"></div>\n'
b += p("The monthly certificate reports a summary. IRIS reports the records. It values nothing and certifies nothing; it shows the lender what the records say, and where two records disagree.", 26, BODY)
S["product"] = section("product", b, 36, "What IRIS produces from the reconciled records: the position (where the project stands on cost, time, scope, procurement, payment, quality, safety and compliance, against the baseline); the exposure (unpriced variations, delays without notice, trades let against allowances, open defects, approval and insurance gaps, each valued and dated); and gaps and conflicts (what should exist and doesn't, and where two records disagree). IRIS reports the system of record and flags the gap where the builder's internal and client-facing forecasts differ; it does not adjudicate. It does not replace the QS, the site inspection, an independent cost-to-complete assessment or professional judgement, and makes no builder scoring, company-wide solvency assessment or payment surveillance across a builder's book. Built: MVP on a populated Procore sandbox. This round: enterprise V1, an adapter per source system, lender, builder and developer views, proven on live records.")

# 06 mvp --------------------------------------------------------------------
b = label("The product · today") + pageno("06")
b += h2("What it looks like today.")
b += '  <div style="display:flex; flex-direction:row; gap:48px; align-items:start">\n'
b += ('    <img src="/_blob/03ce40e84c34ae3aba2336b0250a6ca4" alt="IRIS MVP screen: a project position of value at risk, time at risk and cash lag; six domain cards; a ranked action list; and the project analyst chat" '
      f'style="width:850px; height:650px; background:#ffffff; border:1px solid {RULE}">\n')
b += '    <div style="display:flex; flex-direction:column; gap:22px; flex:1">\n'
for t, c2 in [("One position", "Value at risk, time at risk and cash lag for the project, each figure drilling to its record."),
              ("Six domains", "Contract, programme, cost and cash, letting, design, quality. Each with its status and the item driving it."),
              ("What to do next", "Actions ranked by severity and time-bar proximity, tied to the records behind them."),
              ("Ask the project", "A chat that answers from the records and cites them.")]:
    b += (f'      <div style="display:flex; flex-direction:column; gap:8px; padding:14px 0 0; border-top:3px solid {INK}">\n'
          f'        {caps(t, INK)}\n        <p style="{F} font-size:24px; line-height:1.4; color:{BODY}">{c2}</p>\n      </div>\n')
b += '    </div>\n  </div>\n  <div style="flex:1"></div>\n'
b += p("Demonstration build on a populated Procore sandbox; the project and its figures are fictional. Live-project access is being negotiated.", 24, MUTED)
S["mvp"] = section("mvp", b, 24, "The screen is the MVP as it runs today on a populated Procore sandbox: a fictional project with a $142.5M head contract and a forecast of $148.4M, reporting period May 2026. Top row: the project position, with value at risk ($5.9M), time at risk (eight weeks) and cash lag ($12.9M of cost incurred and not yet recovered), plus the reconciliation coverage figure (88% of records reconciled). Middle: six domain cards. Bottom: the action stack, nineteen items ranked by severity, time-bar proximity and age, thirteen critical. Right: the project analyst chat. Not claimed: a live connection, an accuracy figure, or a lender using it.")

# 07 two products -----------------------------------------------------------
b = label("The products") + pageno("07")
b += h2("One platform. Two products.", coral="Each party sees what it is entitled to see.")
b += '  <div style="display:flex; flex-direction:row; gap:32px">\n'
for t, tc, bg, lines, pays in [
    ("IRIS for Lenders", CORAL2, PANEL2,
     ["The position beneath the certificate, continuous, for each facility on the book.",
      "Written into the facility as a drawdown condition, as the QS is.",
      "In distress, the same position in days, for the lender, its receiver or administrator."],
     "Paid by the developer · 15 bps a year on the facility"),
    ("IRIS for Builders", INK, PANEL,
     ["The same position, first. Notices near their time bar, unlet scope, trades owed, defects against completion.",
      "The builder keeps its margin and is seen fairly by the people funding it.",
      "Its lender gets a reconciled position rather than a month of questions."],
     "Paid by the builder · $3,500 a month per live job"),
]:
    b += f'    <div style="display:flex; flex-direction:column; gap:16px; flex:1; padding:30px 36px 32px; background:{bg}">\n      {caps(t, tc, 26)}\n'
    for ln in lines:
        b += f'      <p style="{F} font-size:26px; line-height:1.4; color:{INK}">{ln}</p>\n'
    b += f'      <p style="{F} font-size:24px; font-weight:600; line-height:1.4; color:{BODY}; margin-top:6px">{pays}</p>\n    </div>\n'
b += '  </div>\n  <div style="flex:1"></div>\n'
b += p("<b>Role-based permissions.</b> The builder authorises the connection and sees each finding first. The lender sees the reconciled position, with drill-down to the record, and does not see the builder’s raw systems. The developer sees what its lender sees.", 26, INK)
S["go-to-market"] = None  # placeholder to keep order explicit below
S["products"] = section("products", b, 32, "One platform with role-based permissions (D-35). The builder's product and the lender's product read the same reconciled position; what differs is the view, the entitlement and the buyer. The builder authorises the read-only connection, sees every finding first and can annotate it; commercially sensitive items stay with the builder. The lender sees the reconciled position and the record behind each figure, not the builder's systems. The developer sees the lender view for its own facility. Distressed-project assessment is proposed functionality at a separate fee, offered after the platform is proven on live jobs; no engagement has been run (appendix A12). Hypothesis, labelled: a monitored facility can price inside an unmonitored one, so the developer's fee is paid out of a financing-cost saving; the design partner is asked at month 9.")
del S["go-to-market"]

# 08 why now ----------------------------------------------------------------
b = label("Why now") + pageno("08")
b += h2("A lender-side category is forming.", coral="None of it reads the builder’s systems.")
b += rows([
    ("Failure", f"Bathla: 540 entities into administration in August 2026, about $3.3bn owed to about 40 funds; sites closed and receivers appointed within a month {G}(reported)</span>."),
    ("Regulators", f"ASIC reviewed 52 private credit funds holding $76bn, warned of enforcement on 22 September, and named residential construction on 30 September {G}(reported)</span>."),
    ("Rates", f"The cash rate rose 100 bps in 2026 to 4.60%; CPI 4.3% to September; dwelling values 5.2% below their March peak {G}(RBA; ABS; Cotality)</span>."),
    ("The market’s answer", "Lender-side monitoring is being sold as a loan condition, done with site walks and register checks. Builder-side AI is being sold to builders, on builders’ data. The builder’s own records, read for the lender, are open ground."),
], 320, pad=20)
S["why-now"] = section("why-now", b, 36, "Dated facts, October–November 2026. Bathla: 540 entities into administration on 25 August; about $3.3bn owed (AFR total; $3.08bn to secured lenders per The Urban Developer, 25 September); 13 remaining sites closed on 23 September; receivers appointed on individual projects (ABC, 17 October). ASIC: review of 52 private credit funds holding $76bn (REP 820); 22 September warning to prepare for enforcement; 30 September naming residential construction. Cash rate: RBA, 4.60%. CPI: ABS headline (monthly series) 4.3% annual to September 2026. Dwelling values: Cotality. The market's answer: Korrix Intelligence Partners (Sydney) sells independent lender-side assessment and monthly monitoring, proposing it be written into the loan as a condition, and is building an insurance layer; SteelCap has announced 'construction risk intelligence for lenders' with early access only; Cintech and Vyne sell AI over the builder's records to the builder. None reads the builder's systems for the lender. Research in research/competitive-landscape.md and appendix A8.")

# 09 competition ------------------------------------------------------------
comp = [
    ("Korrix", "Independent lender-side assessment and monthly monitoring: site walks, register checks, a risk brief. Proposes it as a loan condition.", "Outside-in, by hand, monthly. Does not read the builder’s systems."),
    ("SteelCap", "Announced “construction risk intelligence for lenders”. An early-access programme and an email address.", "Nothing shipped."),
    ("Cintech · Vyne", "AI over a builder’s project records, for the builder. Cintech lists thirteen connectors.", "Serves the builder. Shares nothing upward."),
    ("QS · IPEX · iCIRT", "The monthly certificate; payment-account control; a company rating.", "A summary, money movement, and a rating. No project position."),
]
b = label("Competition") + pageno("09")
b += h2("Others watch the project from outside or serve the builder.", coral="IRIS reads the builder’s systems for the lender.")
b += '  <div style="display:flex; flex-direction:column">\n'
for i, (t, c2, stop) in enumerate(comp):
    bt = f"2px solid {INK}" if i == 0 else f"1px solid {RULE}"
    b += (f'    <div style="display:grid; grid-template-columns:260px 1fr 520px; gap:24px; padding:18px 0; border-top:{bt}">\n'
          f'      <p style="{F} font-size:26px; font-weight:600; line-height:1.35; color:{INK}">{t}</p>\n'
          f'      <p style="{F} font-size:24px; line-height:1.4; color:{INK}">{c2}</p>\n'
          f'      <p style="{F} font-size:24px; line-height:1.4; color:{CORAL2}">{stop}</p>\n    </div>\n')
b += '  </div>\n  <div style="flex:1"></div>\n'
b += p("As of November 2026 we found no product that reads a project’s systems and reconciles them into one position for the lender, the builder and the developer. About sixty products reviewed: appendix A8.", 24, MUTED)
S["competition"] = section("competition", b, 32, "Korrix Intelligence Partners Pty Ltd, Sydney: three layers, Assess (builder financial health check from nine registers and reports, trade contractor assessment, pre-close scorecard), Monitor (monthly, attendance at progress meetings, site walks, covenant register, risk brief; proposed as a loan condition at a fixed monthly fee), Protect (insurance layer in development). Reports only to the lender; no relationship with the builder; no software integrations. SteelCap: a landing page, 'coming soon', early access programme. Cintech Construction Intelligence Platform: one record per project synced from thirteen named systems, cited answers, AI workers, time bars; founders ex-CIO and ex-infrastructure lead at Tier 2 builders; no customers named. Vyne: decision intelligence and organisational memory for builders; illustrative preview, no live systems. The lender's existing controls: the QS certificate, IPEX payment-account control (vendor-claimed lender mandates), project trust accounts, CreditorWatch and iCIRT ratings. IPEX is not a partner. The bounded claim: as of November 2026, no system found that reads a project's source systems and reconciles them into one position shared by lender, builder and developer. Full review in research/competitive-landscape.md.")

# 10 route ------------------------------------------------------------------
b = label("Route to market") + pageno("10")
b += h2("Builders prove it on live jobs. A lender writes it into a facility.")
steps = [
    ("1 · Builders", "Two pilots on live jobs. The position must reconcile to the builder’s own cost reports before anyone pays. Then a monthly fee per live job that follows the builder across its jobs."),
    ("2 · A design-partner lender", "A non-bank private credit fund shapes the lender view from the pilots and runs it beside its QS on a live facility. One such fund has told us the lender view would be useful to it."),
    ("3 · The condition", "A credit committee accepts a live result and writes IRIS into one facility as a drawdown condition. Then its book. Then the next lender."),
]
b += '  <div style="display:flex; flex-direction:row; gap:28px">\n'
for t, c2 in steps:
    b += (f'    <div style="display:flex; flex-direction:column; gap:14px; flex:1; padding:28px 32px 30px; background:{PANEL}">\n'
          f'      {caps(t, INK)}\n      <p style="{F} font-size:26px; line-height:1.4; color:{INK}">{c2}</p>\n    </div>\n')
b += '  </div>\n'
b += p("<b>How the condition holds.</b> The facility binds the developer. The head contract and side deed bind the builder, from the next facility, extension or refinance. A builder under contract today owes nothing new.", 26, INK)
b += '  <div style="flex:1"></div>\n'
b += p("Nothing is assumed automatic: no access, no pilot; no reconciled result, no lender test; no live result, no condition. Mandate mechanics in the appendix.", 24, MUTED)
S["go-to-market"] = section("go-to-market", b, 32, "Sequence (D-07): builder pilots are the technical and commercial proving ground; the lender design partner (target: a non-bank private credit fund) shapes the lender view from those pilots with the pilot builder's consent; at scale the lender requires IRIS as a drawdown condition on the whole project debt stack, the developer pays in basis points as it pays the QS, and the builder opens its systems under the head contract and side deed. The lender signal on the slide is a founder-reported conversation with one non-bank private credit fund, unnamed; the first ask is a design-partner letter and one facility to run beside its QS. Mandate mechanics: lender to developer by the facility agreement; developer to bidders by a tender or award condition; developer to builder by a head-contract clause; all three by the side deed at financial close (appendix A4). A builder that carves it out gets IRIS's view of its own job; we expect a carve-out to read as a signal to the lender, untested until a lender adopts.")

# 11 market and model -------------------------------------------------------
def trow(cells, bold=False, top=False, color=INK):
    st = f"border-top:{'2px solid ' + INK if top else '1px solid ' + RULE};"
    w = "600" if bold else "400"
    s = f'      <div style="display:grid; grid-template-columns:1fr 110px 110px 110px; gap:16px; padding:9px 0; {st}">\n'
    s += f'        <p style="{F} font-size:24px; font-weight:{w}; line-height:1.3; color:{color}">{cells[0]}</p>\n'
    for v in cells[1:]:
        s += f'        <p style="{F} font-size:24px; font-weight:{w}; line-height:1.3; text-align:right; color:{color}">{v}</p>\n'
    return s + '      </div>\n'

b = label("Market and model") + pageno("11")
b += h2("$286M a year in Australia at our prices. $9.5M of it by month 36.")
b += '  <div style="display:flex; flex-direction:row; gap:64px">\n'
b += '    <div style="display:flex; flex-direction:column; gap:28px; width:700px; flex:none">\n'
for n, nc, t, c2 in [("$286M", CORAL, "Australia, modelled", "About 4,300 live jobs of $10M and over: 3,500 with a construction facility at 15 bps on the debt stack, 860 others at $3,500 a month."),
                     ("$54M", INK, "Queensland, modelled", "About 820 live jobs. South East Queensland is where the founders, the first builders and the first lenders are.")]:
    b += (f'      <div style="display:flex; flex-direction:column; gap:10px; padding:18px 0 0; border-top:3px solid {INK}">\n'
          f'        <p style="{F} font-size:72px; font-weight:600; line-height:1; letter-spacing:-3px; color:{nc}">{n} <span style="font-size:24px; font-weight:600; letter-spacing:0; color:{MUTED}">{t}</span></p>\n'
          f'        <p style="{F} font-size:24px; line-height:1.4; color:{BODY}">{c2}</p>\n      </div>\n')
b += '    </div>\n    <div style="display:flex; flex-direction:column; flex:1">\n'
b += (f'      <div style="display:grid; grid-template-columns:1fr 110px 110px 110px; gap:16px; padding:0 0 8px">\n        {caps("Base case · A$K")}\n'
      + ''.join(f'        <p style="{F} font-size:24px; font-weight:600; line-height:1.3; text-align:right; color:{MUTED}">{y}</p>\n' for y in ("Y1", "Y2", "Y3")) + '      </div>\n')
b += trow(["IRIS for Builders", "179", "756", "1,124"], top=True)
b += trow(["IRIS for Lenders, paid by developers", "8", "992", "5,064"])
b += trow(["Revenue", "187", "1,748", "6,188"], bold=True)
b += trow(["Costs", "502", "1,268", "2,976"])
b += trow(["Operating result", "−316", "+480", "+3,212"], bold=True)
b += trow(["Run rate at year end", "600", "3,132", "9,516"], bold=True, color=CORAL2)
b += '    </div>\n  </div>\n  <div style="flex:1"></div>\n'
b += p("Five builders carrying 30 live jobs, and eight lenders with the condition on 69 facilities of $80M, by month 36. This round carries the base to a $3M seed in months 15–18. Assessment fees are not modelled. Inputs and sources in the workbook and appendix.", 24, BODY)
S["economics"] = section("economics", b, 32, "All figures from financial-model/IRIS_model_36m.xlsx, base case (D-33). Market: IBISWorld building work in scope converted to value under construction by build period, divided by a $40M average contract; facility fee 15 bps on the project debt stack at 1.2 times the build contract, within a $3,500 floor and $10,000 cap a month. Builder line: two pilot builders paid from month 6, builders 3–5 from months 12, 20 and 28; each starts with two live jobs at $3,500 a month and adds about one every two months to a cap of six. Lender line: lenders adopting at months 12, 18, 22, 26, 29, 32, 34 and 36, each adding 0.8 new facilities a month on a 24-month term; $80M average facility across the debt stack, so the cap binds at $120,000 a year. Costs: founders at $100K plus super; hires from month 16 to 15 people at month 36; platform, cloud, security, insurance, sales and legal as listed on the Inputs sheet. Year 1 costs equal the $500K use of funds. Low cash $177K at month 11 before the seed. The lender adoption cadence is a company target, not a sourced figure. The previous base case is kept as the conservative case: four lenders, $3.0M run rate.")

# 12 team -------------------------------------------------------------------
t = open(os.path.join(OUT, "team.html"), encoding="utf-8").read()
t = t.replace(">13</p>", ">12</p>")
S["team"] = t

# 13 round ------------------------------------------------------------------
r = open(os.path.join(OUT, "raise.html"), encoding="utf-8").read()
r = r.replace(">14</p>", ">13</p>")
r = r.replace("$500K, SAFE at a $5M cap, to prove IRIS on live data", "$500K, SAFE at a $5M cap, to prove IRIS on live jobs")
r = r.replace("A builder with live $10M-plus jobs in South East Queensland; a non-bank construction lender to shape the lender view.", "A builder with live $10M-plus jobs in South East Queensland. A construction lender willing to run the lender view beside its QS.")
S["raise"] = r

order = ["cover", "stakes", "mechanism", "evidence", "product", "mvp", "products", "why-now", "competition", "go-to-market", "economics", "team", "raise"]
for k in order:
    open(os.path.join(OUT, k + ".html"), "w", encoding="utf-8").write(S[k])
d = json.load(open("/home/claude/iris-deck/deck/source/deck.json"))
d["order"] = order
d["sections"] = {"s1": {"description": "What IRIS is and the round", "start": "cover"},
                 "s2": {"description": "The problem: the lender is the last to know, and why; three real jobs", "start": "stakes"},
                 "s3": {"description": "The product: the position beneath the certificate; the MVP; one platform, two products", "start": "product"},
                 "s4": {"description": "Why now, competition, route to market", "start": "why-now"},
                 "s5": {"description": "Market and model, team, the round", "start": "economics"}}
json.dump(d, open("/home/claude/iris-deck/deck/source/deck.json", "w"), ensure_ascii=False)
print("wrote", order)
