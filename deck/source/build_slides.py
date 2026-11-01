"""Write the 14-slide IRIS deck (D-31) into deck/source/slides. Run from anywhere."""
import os, json
OUT = "/home/claude/iris-deck/deck/source/slides"
F = "font-family:Inter, Arial, sans-serif;"
INK, BODY, MUTED, CORAL, CORAL2, RULE, PANEL, PANEL2 = "#1a1714", "#3d3934", "#6f6a63", "#e8533a", "#c2412a", "#d9d4ca", "#f1ede4", "#f8e6dd"

def label(text):
    return (f'  <p data-iris-label="1" style="position:absolute; top:62px; left:128px; width:1200px; {F} font-size:24px; '
            f'font-weight:600; line-height:1; letter-spacing:3px; text-transform:uppercase; color:{CORAL2}">{text}</p>\n')

def pageno(n):
    return (f'  <p style="position:absolute; right:128px; bottom:64px; width:200px; {F} font-size:24px; text-align:right; '
            f'color:{MUTED}">{n}</p>\n')

def h2(line1, line2=None):
    s = f'  <h2 style="{F} font-size:64px; font-weight:600; line-height:1.1; letter-spacing:-1.5px; color:{INK}">{line1}'
    if line2:
        s += f'<br><span style="color:{CORAL}">{line2}</span>'
    return s + '</h2>\n'

def p(text, size=26, color=BODY, lh=1.4, extra=""):
    return f'  <p style="{F} font-size:{size}px; line-height:{lh}; color:{color};{extra}">{text}</p>\n'

def caps(text, color=MUTED, size=24, extra=""):
    return (f'<p style="{F} font-size:{size}px; font-weight:600; line-height:1.3; letter-spacing:3px; text-transform:uppercase; '
            f'color:{color};{extra}">{text}</p>')

def section(sid, body, gap=28, aside=""):
    return (f'<section id="{sid}" data-transition="fade" style="display:flex; flex-direction:column; gap:{gap}px; '
            f'padding:112px 128px 160px; background:#faf7f0">\n{body}  <aside>{aside}</aside>\n</section>\n')

S = {}

# ---------------------------------------------------------------- 02 summary
rows = [
    ("The problem", INK, "Construction is about one in four Australian insolvencies <span style=\"color:#6f6a63\">(ASIC, FY2025–26)</span>. "
     "When a funded project gets into trouble, the first question is where it really stands. That answer sits in five systems, "
     "is assembled by hand monthly, and reaches the funders late and filtered."),
    ("The product", INK, "IRIS reads those systems by read-only API and reconciles them into one risk position, by domain, each finding "
     "linked to its record. It writes nothing back. The QS stays."),
    ("Who pays", INK, "Builders, monthly per project, now. Developers, in basis points on the facility, once a lender writes IRIS into it. "
     "That mandate is the scale route: one lender brings its book."),
    ("Why now", INK, "Rates up 100 bps in 2026; a $3.3bn developer-builder failure in August; ASIC moving on private credit valuations. "
     "Capital still flows, on harder questions <span style=\"color:#6f6a63\">(reported)</span>."),
    ("Where we are", INK, "MVP on a populated Procore sandbox, shown to a South East Queensland Tier 2 builder; live-project access being "
     "negotiated. Pre-revenue."),
    ("The round", CORAL2, "<b>$500K SAFE at a $5M cap.</b> Buys live data, reconciliation to builders’ own cost reports, a lender beside its QS, "
     "a security review and paid demand."),
]
b = label("Summary") + pageno("02") + h2("Simply put.")
b += '  <div style="display:flex; flex-direction:column">\n'
for i, (k, kc, t) in enumerate(rows):
    bt = f"2px solid {INK}" if i == 0 else f"1px solid {RULE}"
    b += (f'    <div style="display:grid; gap:24px; grid-template-columns:270px 1fr; padding:15px 0; border-top:{bt}">\n'
          f'      {caps(k, kc)}\n      <p style="{F} font-size:26px; line-height:1.4; color:{INK}">{t}</p>\n    </div>\n')
b += '  </div>\n'
S["summary"] = section("summary", b, 30, "One-page version of the deck. Each row answers the question the previous one raises: what is wrong, what IRIS does about it, who pays, why the timing, how far along, and what the money buys.")

# ---------------------------------------------------------------- 03 stakes (problem)
stats = [
    ("$3.08bn", CORAL, "Secured lender exposure", "Owed to secured lenders when Bathla entered administration in August 2026; about 40 private credit funds exposed <span style=\"color:#6f6a63\">(reported)</span>"),
    ("$736M", INK, "Still being reconciled", "Inter-company balances the administrator could not confirm a month in <span style=\"color:#6f6a63\">(reported)</span>"),
    ("20–40%", INK, "Replacement-builder premium", "Extra cost of a replacement builder on the remaining works; part of it is the price of what the newcomer cannot see. Founder experience"),
]
b = label("Problem") + pageno("03")
b += h2("Construction failures put billions of lender capital at risk.", "What a lender recovers depends on the project’s real state.")
b += p("Finish it, sell it or write it down: each option is priced off what the records show.", 32, BODY, 1.35)
b += '  <div style="display:flex; flex-direction:row; gap:56px">\n'
for n, nc, t, c in stats:
    b += (f'    <div style="display:flex; flex-direction:column; gap:14px; flex:1; padding:22px 0 0; border-top:3px solid {INK}">\n'
          f'      <p style="{F} font-size:96px; font-weight:600; line-height:1; letter-spacing:-4px; color:{nc}">{n}</p>\n'
          f'      <p style="{F} font-size:24px; font-weight:600; line-height:1.3; color:{INK}">{t}</p>\n'
          f'      <p style="{F} font-size:24px; line-height:1.4; color:{BODY}">{c}</p>\n    </div>\n')
b += '  </div>\n  <div style="flex:1"></div>\n'
b += '  <div style="display:flex; flex-direction:column; gap:14px">\n    ' + caps("Large recent builder and developer failures · reported") + '\n'
b += ('    <svg xmlns="http://www.w3.org/2000/svg" aria-label="Timeline of eight large builder and developer failures from 2020 to 2026" viewBox="0 0 1664 24" style="width:1664px; height:24px">'
      '<path d="M100 12H1564" stroke="#CFC8BB" stroke-width="2" fill="none"/>' +
      ''.join(f'<circle cx="{x}" cy="12" r="7" fill="#1A1714"/>' for x in (100, 309, 518, 727, 937, 1146, 1355)) +
      '<circle cx="1564" cy="12" r="10" fill="#E8533A"/></svg>\n')
b += '    <div style="display:flex; flex-direction:row; justify-content:space-between">\n'
for name, yr, last in (("Grocon", 2020, 0), ("Probuild", 2022, 0), ("Condev", 2022, 0), ("PBS", 2023, 0), ("Porter Davis", 2023, 0), ("St Hilliers", 2024, 0), ("Roberts Co", 2025, 0), ("Bathla", 2026, 1)):
    st = f"font-weight:600; color:{CORAL2}" if last else f"color:{MUTED}"
    b += f'      <p style="width:200px; {F} font-size:24px; line-height:1.25; text-align:center; {st}">{name}<br>{yr}</p>\n'
b += '    </div>\n  </div>\n'
b += p("Sources: The Urban Developer, 25 September 2026; ABC News, 17 October 2026; ASIC; founder observations. Detail in the appendix (A6).", 24, MUTED)
S["stakes"] = section("stakes", b, 26, "Bathla figures from the administrator's updates as reported by The Urban Developer on 25 September 2026: about $3.08bn owed to secured lenders within about $3.4bn of total creditor debt; about $736m of inter-company receivables and payables that may be overstated and were still being reconciled a month after appointment. All 13 remaining active sites were closed on 23 September after emergency lender funding ran out. One lender's senior loan on a near-complete project was later sold and a receiver appointed to settle presales (ABC News, 17 October 2026). The replacement-builder premium of 20 to 40 per cent is founder experience, not a measured figure; part of it prices what the incoming builder cannot see in the records. Scope: IRIS reads a project's builder systems, so on a Bathla project it would show that project's trades owed against what was claimed and certified, and its cost position against forecast; the group's inter-company position is the administrator's reconciliation. Construction's share of insolvencies, 24.5 per cent in FY2025-26, is on slide 2 (ASIC).")

# ---------------------------------------------------------------- 04 mechanism
cards = [
    ("1 · The project’s systems", "Procore or Aconex, Jobpac, PayApps, ProcurePro and the inbox. Variations, delays, trades let and money owed each live somewhere different."),
    ("2 · The builder’s monthly report", "Assembled by hand from those systems, by the party it reports on."),
    ("3 · The lender’s QS certificate", "Work in place checked against the claim, from a site visit and the builder’s submissions. Not independently verified; no allowance for defects."),
    ("4 · The facility decision", "The drawdown is funded on the certificate, weeks after the records moved. Finish, sell or write down is decided on the same summary."),
]
b = label("Problem · the mechanism") + pageno("04")
b += h2("The position sits in five systems and travels up by hand.", "Each hand-off filters it. The lender sees it last.")
b += '  <div style="display:flex; flex-direction:row; gap:16px; align-items:stretch">\n'
for i, (t, c) in enumerate(cards):
    bg = PANEL2 if i == 3 else PANEL
    bl = f"border-left:3px solid {CORAL}" if i == 3 else f"border-left:3px solid {INK}"
    b += (f'    <div style="display:flex; flex-direction:column; gap:12px; flex:1; padding:22px 24px 24px; background:{bg}; {bl}">\n'
          f'      <p style="{F} font-size:24px; font-weight:600; line-height:1.25; letter-spacing:1px; color:{INK}">{t}</p>\n'
          f'      <p style="{F} font-size:24px; line-height:1.38; color:{BODY}">{c}</p>\n    </div>\n')
    if i < 3:
        b += ('    <svg xmlns="http://www.w3.org/2000/svg" aria-label="arrow" viewBox="0 0 24 16" style="width:24px; height:16px; align-self:center; flex:none">'
              '<path d="M0 8H18" stroke="#1A1714" stroke-width="2" fill="none"/><path d="M12 2L20 8L12 14" stroke="#1A1714" stroke-width="2" fill="none"/></svg>\n')
b += '  </div>\n'
b += p("<b>What the certificate does not carry:</b> notices against time bars, cost moving before it is notified, contingency already spent, market exposure in the trades, defects, and trades owed more than the builder has claimed. The last is usually the first sign.", 26, INK)
b += p("<b>Since 2021</b>, fixed prices, thinner builders and in-house delivery have moved more of the risk inside the project. The lender’s view has not moved.", 26, INK)
b += '  <div style="flex:1"></div>\n'
b += p("Founder observation, from work inside builders across three delivery models. Detail: appendix A2, A3.", 24, MUTED)
S["mechanism"] = section("mechanism", b, 24, "The chain: five systems hold the records; the builder's team assembles the monthly report from them (internal cost report and the PCG report to the client); the lender's quantity surveyor values work in place from a site inspection and checks the claim against the contract sum, working from the claim, the variation and EOT registers as submitted, the statutory declaration that trades are paid and the builder's programme, and reports that the information was not independently verified and that no allowance is made for defects; the lender funds the drawdown on that certificate. What sits beneath it, by cause: entitlement at the time bar (notices, variations, latent conditions near or past the deadline that decides who pays); forecast movement not yet notified and the prelims it extends; how much of forecast final cost is still contingency and provisional sums; market exposure in the trades (rates locked while prices move, scope unlet, trades let against allowances); completion risk (labour on site against programme, open defects and non-conformances against PC); and cash strain in the trades, what subcontractors are owed against what the builder has claimed and been paid, which is usually the first sign of a builder in trouble and the one the lender sees last. Appendix A2 carries the row-by-row table with the QS item each sits beneath and the source system; A3 the four market shifts since 2021 with sources (Stamford Capital 2026 survey; builder failures 2022–25; non-bank share of commercial property debt).")

# ---------------------------------------------------------------- 05 evidence
ev = [
    ("Project A · $45M mixed-use", "Open-book builder-developer; private credit facility arrived mid-build", "$4.4M", CORAL,
     "More cost in the ledger than in the lender’s pack, at a third complete, plus a $1.5M delay claim not yet submitted. <b>The lender saw it</b> about nine months later. <b>It decided</b> whether the facility was in balance."),
    ("Project B · $300M residential tower", "Major builder; refinance at two-thirds complete", "$0", INK,
     "Delay buffer left: the incentive pool was spent to the dollar against the forecast delay, on a $110M contract carrying $35M of change. <b>The lender was</b> a monthly pack behind, more than 30 times. <b>It decided</b> the refinance terms."),
    ("Project C · $15M commercial", "Investor syndicate; private financier; QS-gated drawdowns", "12 days", INK,
     "From claim to cash. Delay contingency fully used at three-quarters of the programme; the position typed by hand each month. <b>It decided</b> whether to extend the facility."),
]
b = label("Evidence") + pageno("05")
b += h2("On three real jobs, the position sat in the records", "weeks before it reached the people funding them.")
b += p("Real case studies with indicative data. Names, values and delivery models altered.", 28, BODY)
b += '  <div style="display:flex; flex-direction:row; gap:56px">\n'
for t, sub, n, nc, c in ev:
    b += (f'    <div style="display:flex; flex-direction:column; gap:10px; flex:1; padding:18px 0 0; border-top:3px solid {INK}">\n'
          f'      {caps(t)}\n'
          f'      <p style="{F} font-size:26px; font-weight:600; line-height:1.3; color:{INK}">{sub}</p>\n'
          f'      <p style="{F} font-size:72px; font-weight:600; line-height:1; letter-spacing:-2.5px; color:{nc}">{n}</p>\n'
          f'      <p style="{F} font-size:24px; line-height:1.4; color:{BODY}">{c}</p>\n    </div>\n')
b += '  </div>\n  <div style="flex:1"></div>\n'
b += p("Evidence of the problem, not of IRIS. This round rebuilds the position on these files.", 24, MUTED)
S["evidence"] = section("evidence", b, 24, "Three private record sets, held by the founders and read in full: a builder's share drive (cost-system exports, registers, claims, programmes, cashflows, PCG reports, the lender's QS initial report and the bank's term sheet); a developer's PCG pack and its capital partner's feasibility; a lender's QS drawdown report, payment certificates, PCG to the financier and trust investor report. Figures, contract sizes, delivery-model labels and lags on the slide are altered so the projects cannot be identified; the structure of each issue is as found. Project A: the builder's internal forecast ran ahead of the figure in the developer's PCG pack for about a year, with a large unsubmitted delay claim, unlet finishes trades forecast flat at budget, and a programme sliding month on month. Project B: a major-builder tower under a well-run monthly PCG whose delay-incentive pool had been consumed to the dollar by approved wet-weather days, with the bank refinancing in at about three-quarters complete. Project C: a small commercial job under a private financier with QS-gated drawdowns across two contracts, where the delay contingency was fully used with a fifth of the programme to run, and the monthly dashboard was typed by hand from the builder's PDF, with formula errors in the working files. In each case the number that decided whether the lender's money was safe existed in a record before it existed in a report. These are illustrative examples of the problem; they are not outcomes IRIS has delivered.")

# ---------------------------------------------------------------- 06 product (solution + value ladder)
ladder = [
    ("Builder", "Sees its exposure first: notices near time bars, unlet scope, trades owed, defects. Protects its margin.", "$3,500 a month per project · now", INK),
    ("Developer", "The same position beside its PCG report, without re-typing it. Knows what its lender will see, first.", "In basis points, once its lender requires it", INK),
    ("Lender", "The position beneath the certificate, each figure linked to its record, before the drawdown decision.", "Writes IRIS into the facility · the scale route", CORAL2),
    ("In distress", "A lender, receiver or administrator gets a source-linked position in days, with a trail a committee or court can check.", "Fixed fee per engagement · after live proof", INK),
]
b = label("Solution") + pageno("06")
b += h2("IRIS reads those systems and reconciles them into", "one source-linked position for each party funding the job.")
b += p("Read-only API. Nothing written back, installed or replaced. The QS, the site visit and judgement stay.", 30, BODY, 1.35)
b += '  <div style="display:flex; flex-direction:column">\n'
b += (f'    <div style="display:grid; grid-template-columns:240px 1fr 520px; gap:24px; padding:0 0 10px; border-bottom:2px solid {INK}">\n'
      f'      {caps("Who")}\n      {caps("What it gets from the same position")}\n      {caps("Who pays, and when")}\n    </div>\n')
for who, what, pays, pc in ladder:
    b += (f'    <div style="display:grid; grid-template-columns:240px 1fr 520px; gap:24px; padding:14px 0; border-top:1px solid {RULE}">\n'
          f'      <p style="{F} font-size:26px; font-weight:600; line-height:1.35; color:{pc}">{who}</p>\n'
          f'      <p style="{F} font-size:24px; line-height:1.38; color:{INK}">{what}</p>\n'
          f'      <p style="{F} font-size:24px; line-height:1.38; color:{BODY}">{pays}</p>\n    </div>\n')
b += '  </div>\n  <div style="flex:1"></div>\n'
b += p("<b>Built:</b> MVP on a Procore sandbox. <b>This round:</b> enterprise V1, an adapter per system, three views, proven on live records. <b>Next:</b> portfolio view across a lender’s book; assessments.", 24, BODY)
S["product"] = section("product", b, 26, "What IRIS produces from the reconciled records: the position (where the project stands on cost, time, scope, procurement, payment, quality, safety and compliance, against the baseline); the exposure (unpriced variations, delays without notice, trades let against allowances, open defects, approval and insurance gaps, each valued and dated); and gaps and conflicts (what should exist and doesn't, and where two records disagree). Each party gets its own view of the same position; commercially sensitive items stay with the builder. IRIS values nothing and certifies nothing; it reports the system of record and flags the gap where the builder's internal and client-facing forecasts differ. Distressed-project assessment is proposed functionality at a separate fee, offered after the platform is proven on live jobs; no engagement has been run. Before an appointment, access runs through the facility's information rights and the builder's side deed; after, through the receiver's or administrator's agreement. The six-step assessment workflow and the lender decisions the position serves are in the appendix (A1, A4).")

# ---------------------------------------------------------------- 07 mvp
mvp = [
    ("One position", "Value at risk $5.9M of a $148.4M forecast; eight weeks of time at risk; $12.9M incurred and not recovered. Each figure drills to its record."),
    ("Six domains", "Contract, programme, cost and cash flow, letting and procurement, design and documentation, quality; each with its status and the item driving it."),
    ("What to do next", "Nineteen actions ranked by severity, time-bar proximity and age; each tied to the variation, RFI or notice behind it."),
    ("Ask the project", "A chat that answers from the records and cites the evidence it drew on."),
]
b = label("Solution · the MVP") + pageno("07")
b += h2("The MVP today: one project, one position, six domains.")
b += '  <div style="display:flex; flex-direction:row; gap:40px; align-items:start">\n'
b += ('    <img src="/_blob/03ce40e84c34ae3aba2336b0250a6ca4" alt="IRIS MVP screen: a project position of value at risk, time at risk and cash lag; six domain cards; a ranked action list; and the project analyst chat" '
      f'style="width:850px; height:650px; background:#ffffff; border:1px solid {RULE}">\n')
b += '    <div style="display:flex; flex-direction:column; gap:16px; flex:1">\n'
for t, c in mvp:
    b += (f'      <div style="display:flex; flex-direction:column; gap:6px; padding:12px 0 0; border-top:3px solid {INK}">\n'
          f'        {caps(t, INK)}\n        <p style="{F} font-size:24px; line-height:1.38; color:{BODY}">{c}</p>\n      </div>\n')
b += '    </div>\n  </div>\n  <div style="flex:1"></div>\n'
b += p("Demonstration build on a populated Procore sandbox; the project and its figures are fictional. Live-project access is being negotiated.", 24, MUTED)
S["mvp"] = section("mvp", b, 24, "The screen is the MVP as it runs today on a populated Procore sandbox: a fictional project with a $142.5M head contract and a forecast of $148.4M, reporting period May 2026. Top row: the project position, with value at risk, time at risk and cash lag, plus the reconciliation coverage figure (88% of records reconciled). Middle: six domain cards, each with a status, the figure that drives it and a drill-down to the records. Bottom: the action stack, nineteen items ranked by severity, time-bar proximity and age, thirteen critical, each with its value and the source records it rests on. Right: the project analyst, a chat that answers from the records and cites them. Not claimed: a live connection, an accuracy figure, or a lender using it.")

# ---------------------------------------------------------------- 08 why-now
wn = [
    ("Rates and feasibility", "The cash rate rose 100 bps in 2026 to 4.60%; CPI 4.3% to September; dwelling values 5.2% below their March peak <span style=\"color:#6f6a63\">(RBA; ABS; Cotality)</span>."),
    ("A $3.3bn failure", "Bathla: 540 entities into administration on 25 August, about $3.3bn owed to about 40 funds; sites closed and receivers appointed by late September <span style=\"color:#6f6a63\">(reported)</span>."),
    ("Regulators on valuation", "ASIC reviewed 52 private credit funds holding $76bn, warned on 22 September to prepare for enforcement, and named residential construction on 30 September <span style=\"color:#6f6a63\">(reported)</span>."),
    ("The enabler", "Models now read contracts, correspondence and cost records together and cite the source of each figure, at a cost that works per project per month."),
]
b = label("Why now") + pageno("08")
b += h2("The market moved to where the position matters most.", "Capital is still being deployed. It is asking harder questions.")
b += '  <div style="display:flex; flex-direction:column">\n'
for i, (t, c) in enumerate(wn):
    bt = f"2px solid {INK}" if i == 0 else f"1px solid {RULE}"
    b += (f'    <div style="display:grid; gap:24px; grid-template-columns:340px 1fr; padding:18px 0; border-top:{bt}">\n'
          f'      {caps(t, INK)}\n      <p style="{F} font-size:26px; line-height:1.4; color:{INK}">{c}</p>\n    </div>\n')
b += '  </div>\n  <div style="flex:1"></div>\n'
b += p("The gap beneath the certificate exists in good markets too; a downturn raises the cost of it. Facility monitoring is paid on what is lent, so it grows with lending. From July 2027 the private credit industry standard requires quarterly independent valuation <span style=\"color:#6f6a63\">(reported)</span>.", 24, BODY)
S["why-now"] = section("why-now", b, 28, "Dated facts, October 2026. Cash rate: RBA, 4.60% after 100 bps of increases in 2026. CPI: ABS headline (monthly series) 4.3% annual to September 2026, trimmed mean 3.6%. Dwelling values: Cotality, 5.2% below the March 2026 peak. Bathla: 540 entities into administration on 25 August; about $3.3bn owed (AFR total; $3.08bn to secured lenders per The Urban Developer, 25 September); 13 remaining sites closed on 23 September; receivers appointed on individual projects. ASIC: review of 52 private credit funds holding $76bn (REP 820); 22 September warning to prepare for enforcement; 30 September naming residential construction; June guidance to reassess loan values before formal default; industry standard from July 2027 requiring quarterly independent valuation. Redemptions: a $2.3bn credit fund suspended redemptions on 22 October 2026. Construction was 37% of insolvencies in July–August with Bathla, 23.5% without (ASIC). All sources dated in research/source-register.md and appendix A6.")

# ---------------------------------------------------------------- 09 go-to-market
gtm = [
    ("Now · Builder pilots", INK, "Prove it on live jobs: two R&D deployments, then a monthly fee per project. Gate: the position reconciles to the builder’s own cost reports.", "Builder · $3,500 a month per project"),
    ("Alongside · Lender design partner", INK, "A non-bank lender shapes the lender view from the pilots and uses it on a live facility beside its QS. Gate: security, PI and reliance terms in place.", "No fee · the partner’s time"),
    ("Scale · The mandate", CORAL2, "A credit committee accepts a live result and writes IRIS into one facility as a drawdown condition; then its book; then the next lender.", "Developer · 15 bps a year on the facility, as it pays the QS"),
]
b = label("Go to market") + pageno("09")
b += h2("Builders prove it. A lender shapes it. The mandate scales it.")
b += '  <div style="display:flex; flex-direction:row; gap:28px">\n'
for t, tc, c, pays in gtm:
    bg = PANEL2 if tc == CORAL2 else PANEL
    b += (f'    <div style="display:flex; flex-direction:column; gap:14px; flex:1; padding:26px 30px 28px; background:{bg}">\n'
          f'      {caps(t, tc)}\n      <p style="{F} font-size:26px; line-height:1.4; color:{INK}">{c}</p>\n'
          f'      <p style="{F} font-size:24px; font-weight:600; line-height:1.4; color:{BODY}">{pays}</p>\n    </div>\n')
b += '  </div>\n'
b += '  <div style="display:flex; flex-direction:column">\n'
for i, (t, c) in enumerate([
    ("How the mandate holds", "The facility binds the developer; the head contract and side deed bind the builder, from the next facility, extension or refinance. A builder under contract today owes nothing new."),
    ("Who opens the systems", "The builder, read-only. It sees each finding first; builder, developer and lender each get their own view."),
]):
    bt = f"2px solid {INK}" if i == 0 else f"1px solid {RULE}"
    b += (f'    <div style="display:grid; gap:24px; grid-template-columns:340px 1fr; padding:12px 0; border-top:{bt}">\n'
          f'      {caps(t)}\n      <p style="{F} font-size:24px; line-height:1.4; color:{INK}">{c}</p>\n    </div>\n')
b += '  </div>\n  <div style="flex:1"></div>\n'
b += p("Nothing assumed automatic: no access, no pilot; no reconciled result, no lender test; no live result, no condition. The legal pathway is confirmed in this round (slide 14).", 24, MUTED)
S["go-to-market"] = section("go-to-market", b, 30, "Three workstreams on one platform, in sequence (D-07): builder pilots are the technical and commercial proving ground and a revenue line of their own; the lender design partner (target: a non-bank private credit fund) shapes the lender view from those pilots with the pilot builder's consent; at scale the lender requires IRIS as a drawdown condition, the developer pays in basis points as it pays the QS, and the builder opens its systems under the head contract and side deed. Distressed-project assessments are part of the scale stage, priced per engagement. Mandate mechanics: lender to developer by the facility agreement; developer to all bidders by a tender or award condition; developer to builder by a head-contract clause; all three parties by the side deed at financial close. A builder that carves it out gets IRIS's view of its own job; we expect a carve-out to read as a signal to the lender, which is untested until a lender adopts. Each figure links to its record, so a disputed finding is checked against data the builder does not write. Appendix A4 carries the mandate table.")

# ---------------------------------------------------------------- 10 competition
comp = [
    ("Source systems IRIS reads", "Procore and Aconex (the job); Jobpac (the cost ledger and forecast); PayApps and ProcurePro (trade claims and letting); email, Office and the share drive.", "IRIS reads them. It replaces none."),
    ("The lender’s controls today", "The lender’s QS (work in place, monthly, from the claim); IPEX (payment-account control); project trust accounts; CreditorWatch and iCIRT (a company rating).", "Money movement and a company rating. No project position."),
    ("Builder-side AI", "Procore and Datagrid agents over the ERP and documents; Document Crunch on contract risk; Octant and Alloovium (AU) on outturn; Slate and Trunk Tools (US).", "For the builder, on the builder’s data. Not shared upward."),
    ("Lender draw tools, US", "Built (draws for 300+ US lenders; reads Procore financials), Rabbet and Land Gorilla check the submitted draw package. No Australian equivalent found.", "Checks the package. Does not read beneath it."),
]
b = label("Competition") + pageno("10")
b += h2("We found no system that does this.", "Lenders’ controls stop at the certificate and the bank.")
b += '  <div style="display:flex; flex-direction:column">\n'
b += (f'    <div style="display:grid; grid-template-columns:300px 1fr 420px; gap:24px; padding:0 0 10px; border-bottom:2px solid {INK}">\n'
      f'      {caps("Layer")}\n      {caps("Who is in it")}\n      {caps("Where it stops")}\n    </div>\n')
for t, c, stop in comp:
    b += (f'    <div style="display:grid; grid-template-columns:300px 1fr 420px; gap:24px; padding:13px 0; border-top:1px solid {RULE}">\n'
          f'      <p style="{F} font-size:24px; font-weight:600; line-height:1.35; color:{INK}">{t}</p>\n'
          f'      <p style="{F} font-size:24px; line-height:1.38; color:{INK}">{c}</p>\n'
          f'      <p style="{F} font-size:24px; line-height:1.38; color:{CORAL2}">{stop}</p>\n    </div>\n')
b += '  </div>\n  <div style="flex:1"></div>\n'
b += p("In October 2026 we found no software that reconciles a project’s systems into one position for builder, developer and lender. About sixty products reviewed: appendix A7.", 24, BODY)
S["competition"] = section("competition", b, 26, "The bounded claim: as of October 2026, no system found that reconciles a construction project's source systems into one source-linked position shared by builder, developer and lender. Adjacent software is either a source system IRIS reads or a tool it sits beside. IPEX is the closest Australian control: payment-account control with vendor-claimed lender mandates; it moves money and does not read the position. Built is the closest overseas analogue: draw management for 300+ US lenders, reading Procore financials, checking the submitted package rather than reconciling beneath it. Builder-side AI (Procore and Datagrid agents, Document Crunch, Octant, Alloovium, Slate, Trunk Tools) works for the builder on the builder's data and shares nothing upward. The full review of about sixty products and firms is in research/competitive-landscape.md and appendix A7. IPEX is not a partner; a partnership would be considered only with a product similar enough in logic to merge with.")

# ---------------------------------------------------------------- 11 market
mk = [
    ("$244M", CORAL, "Total market, Australia · modelled", "About 4,300 live jobs of $10M and over: 3,500 developer-funded at 15 bps on a $40M facility, 860 others at $3,500 a month."),
    ("$46M", INK, "Serviceable, Queensland · modelled", "About 820 live jobs in scope. South East Queensland, where the founders and the first builders and lenders are, holds about 80% of the state’s building pipeline."),
    ("$8.9M", INK, "Obtainable, month 36 · base case", "Month-36 run rate: eight lenders with the condition on about 130 facilities, and 50 paid builder projects. Under 4% of Australia."),
]
b = label("Market size") + pageno("11")
b += h2("$244M a year in Australia at our prices.", "$46M of it in Queensland.")
b += p("Developers pay in basis points once a lender requires IRIS; builders pay monthly until then. Lenders operate nationally, so the obtainable figure is measured against Australia.", 28, BODY)
b += '  <div style="display:flex; flex-direction:row; gap:56px">\n'
for n, nc, t, c in mk:
    b += (f'    <div style="display:flex; flex-direction:column; gap:14px; flex:1; padding:22px 0 0; border-top:3px solid {INK}">\n'
          f'      <p style="{F} font-size:96px; font-weight:600; line-height:1; letter-spacing:-4px; color:{nc}">{n}</p>\n'
          f'      <p style="{F} font-size:24px; font-weight:600; line-height:1.3; color:{INK}">{t}</p>\n'
          f'      <p style="{F} font-size:24px; line-height:1.4; color:{BODY}">{c}</p>\n    </div>\n')
b += '  </div>\n  <div style="flex:1"></div>\n'
b += p("Not counted: assessment fees (no engagement has set the fee or volume); insurers and surety providers, holding about $8.7bn of security on these jobs. Built from IBISWorld, ABS and lender data; derivation in appendix A5.", 24, MUTED)
S["market"] = section("market", b, 26, "Market sheet of financial-model/IRIS_model_36m.xlsx. Building work in scope (IBISWorld E3019 medium- and high-rise apartments, $33.5bn; E3021 commercial and industrial on jobs of $10M or more, about 65% of $70.9bn) is converted to value under construction by build period (29 months apartments, ABS; 24 months C&I, estimate), divided by an average contract of $40M (cross-checked against Qualitas, PRD and Hubexo figures) to give about 4,330 live projects, of which about 3,470 are developer-funded (IBISWorld major-market shares). Facility fee: 15 bps a year on a facility about the size of the build contract, within a $3,500 floor and $10,000 cap a month. Queensland shares: 19.6% of multi-unit work, 18.2% of C&I (IBISWorld). The obtainable figure is the month-36 annualised revenue of the base case (D-32): 8 lenders, 129 facilities, 50 paid builder projects. The previous base ($3.6M) is kept as the conservative case.")

# ---------------------------------------------------------------- 12 economics
def trow(cells, bold=False, top=False, color=INK, note=None):
    st = f"border-top:{'2px solid ' + INK if top else '1px solid ' + RULE};"
    w = "600" if bold else "400"
    s = f'    <div style="display:grid; grid-template-columns:1fr 120px 120px 120px; gap:16px; padding:9px 0; {st}">\n'
    s += f'      <p style="{F} font-size:24px; font-weight:{w}; line-height:1.3; color:{color}">{cells[0]}'
    if note:
        s += f' <span style="font-weight:400; color:{MUTED}">{note}</span>'
    s += '</p>\n'
    for v in cells[1:]:
        s += f'      <p style="{F} font-size:24px; font-weight:{w}; line-height:1.3; text-align:right; color:{color}">{v}</p>\n'
    return s + '    </div>\n'

def thead(title):
    s = f'    <div style="display:grid; grid-template-columns:1fr 120px 120px 120px; gap:16px; padding:0 0 8px">\n      {caps(title)}\n'
    for y in ("Y1", "Y2", "Y3"):
        s += f'      <p style="{F} font-size:24px; font-weight:600; line-height:1.3; text-align:right; color:{MUTED}">{y}</p>\n'
    return s + '    </div>\n'

b = label("The model") + pageno("12")
b += h2("Builders pay first. Lender mandates drive the curve.")
b += '  <div style="display:flex; flex-direction:row; gap:56px">\n'
b += '    <div style="display:flex; flex-direction:column; flex:1">\n' + thead("Revenue · A$K")
b += trow(["Builder subscriptions", "120", "699", "1,599"], top=True)
b += trow(["Facility fees, paid by the developer", "7", "814", "4,154"])
b += trow(["Total revenue", "126", "1,513", "5,753"], bold=True)
b += trow(["Run rate at year end", "404", "2,815", "8,855"], bold=True, color=CORAL2)
b += '    </div>\n    <div style="display:flex; flex-direction:column; flex:1">\n' + thead("Costs and result · A$K")
b += trow(["People", "224", "820", "2,188"], top=True)
b += trow(["Platform, cloud, security", "216", "192", "346"])
b += trow(["Sales, legal, insurance, contingency", "60", "266", "631"])
b += trow(["Total costs", "500", "1,279", "3,164"], bold=True)
b += trow(["Operating result", "−373", "+234", "+2,589"], bold=True, color=CORAL2)
b += '    </div>\n  </div>\n'
b += p("<b>At year end:</b> 8 / 24 / 50 paid builder projects; 2 / 34 / 129 facilities under 1 / 3 / 8 lenders; 2 / 9 / 17 people.", 24, MUTED)
b += p("<b>What drives the curve.</b> One lender adopting brings its book: each lender adds about 1.5 facilities a month at 15 bps on a $35M facility ($52.5K a year), and builders under the condition bring their other jobs. Year 3 recognises $5.8M; the month-36 run rate is $8.9M.", 26, INK)
b += '  <div style="flex:1"></div>\n'
b += p("<b>Cash.</b> This round carries the base to a $3M seed in months 15–18 (low cash $117K, month 18). The seed funds the lender rollout. Assessment fees not modelled. The previous base ($3.6M run rate) is kept as the conservative case (A5).", 24, BODY)
S["economics"] = section("economics", b, 26, "All figures from financial-model/IRIS_model_36m.xlsx, base case (D-32, proposed 1 November 2026). Revenue: builder subscriptions at $3,500 a month per project, 1.0 / 1.5 / 2.5 new paid projects a month in Years 1–3 after the first paid month (month 6), 1% monthly churn; facility fees at 15 bps a year on an average $35M facility, within a $3,500 floor and $10,000 cap a month, lenders adopting at months 12, 18, 22, 26, 29, 32, 34 and 36, each adding 1.5 facilities a month on a 24-month term. Costs: founders at $100K each plus 12% super; hires from month 16 (commercial lead, engineer, deployment analyst), a lender onboarding lead at month 18, head of product and risk and customer success at 22, further engineers and analysts to 17 people at month 36; platform build $170K in Year 1 then contract engineering $90K a year; cloud $800 a month fixed plus $150 per live job; security certification $30K then $35K a year; insurance $10K / $45K / $90K; sales $20K / $120K / $300K; legal $20K / $40K / $90K; contingency $10K then 5% of costs. Year 1 costs equal the $500K use of funds. Cash before the seed stays positive throughout, with a low of $117K at month 18; the $3M seed at month 15 funds the hires that precede the lender revenue. Conservative case (the previous base, D-07): four lenders at 0.75 facilities a month, 1.0 / 1.25 / 1.5 builder adds, nine people; revenue $95K / $859K / $2,304K; run rate $3.2M.")

# ---------------------------------------------------------------- 13 team
b = label("Team") + pageno("13")
b += h2("One founder works inside builders’ systems.", "The other builds analytics and AI in banking.")
b += '  <div style="display:flex; flex-direction:column; gap:14px">\n    ' + caps("Founders") + '\n    <div style="display:flex; flex-direction:row; gap:48px">\n'
for n, t, c in (("James Thompson", "Co-founder · Director", "Contracts administration on $60M–$400M projects with Tier 1 and Tier 2 builders, across arm’s-length, joint-venture and in-house delivery models. Works daily in the systems IRIS reads."),
                ("Gopesh Khanna", "Co-founder · Director", "Data scientist in banking: production analytics, predictive models and generative AI in a regulated environment. Builds with the governance and traceability a lender’s risk team will ask for.")):
    b += (f'      <div style="display:flex; flex-direction:column; gap:8px; flex:1">\n'
          f'        <h3 style="{F} font-size:40px; font-weight:600; line-height:1.15; color:{INK}">{n}</h3>\n        {caps(t, CORAL2)}\n'
          f'        <p style="{F} font-size:26px; line-height:1.42; color:{BODY}">{c}</p>\n      </div>\n')
b += '    </div>\n  </div>\n'
b += f'  <div style="height:2px; border-top:1px solid {RULE}"></div>\n'
b += '  <div style="display:flex; flex-direction:column; gap:14px">\n    ' + caps("Advisors") + '\n    <div style="display:flex; flex-direction:row; gap:40px">\n'
for n, t, c in (("Aaron Thompson", "Thompson Project Solutions", "James’s father. 35 years in commercial construction and development; former Gold Coast builder-developer, now consulting to private capital. Weathered two prior major downturns including the GFC."),
                ("Mark Forrest", "Co-founding advisor · finance and governance", "C-suite finance executive, board director and investor. Advises on governance, strategic positioning, capital and growth. Experienced property developer in Australian and international markets.")):
    b += (f'      <div style="display:flex; flex-direction:column; gap:6px; flex:1">\n'
          f'        <h3 style="{F} font-size:32px; font-weight:600; line-height:1.15; color:{INK}">{n}</h3>\n        {caps(t, MUTED, 24, "letter-spacing:2px")}\n'
          f'        <p style="{F} font-size:24px; line-height:1.42; color:{BODY}">{c}</p>\n      </div>\n')
b += '    </div>\n  </div>\n'
S["team"] = section("team", b, 32, "Founders are referred to externally as directors. Advisors are unpaid at this stage.")

# ---------------------------------------------------------------- 14 raise + close
uof = [("Founder salaries, both full-time, with super", "$224K"), ("Platform build and R&D", "$170K"), ("Enterprise security and cyber audit", "$30K"),
       ("Cloud and LLM infrastructure", "$16K"), ("Sales, marketing and customer success", "$20K"), ("Legal, accounting and IP", "$20K"), ("Contingency and insurance", "$20K")]
ms = [("Month 3", "Two builder pilots live by API; a design-partner lender engaged."),
      ("Month 6", "The position reconciles to builders’ own cost reports; security certified."),
      ("Month 9", "The design partner using the lender view on a live facility beside its QS; PI cover, reliance terms, legal opinion on the mandate."),
      ("Month 12", "Paid builder projects; a drafted condition with one lender; assessment scope and fee set."),
      ("Months 15–18", "Seed raise on that evidence, with or without a lender mandate.")]
b = label("The round") + pageno("14")
b += h2("$500K, SAFE at a $5M cap, to prove IRIS on live data", "and open the paid route to the lender.")
b += '  <div style="display:flex; flex-direction:row; gap:64px">\n    <div style="display:flex; flex-direction:column; width:640px; flex:none">\n      ' + caps("Use of funds") + '\n'
for i, (t, v) in enumerate(uof):
    bt = f"2px solid {INK}" if i == 0 else f"1px solid {RULE}"
    b += (f'      <div style="display:grid; grid-template-columns:1fr 110px; gap:16px; padding:8px 0; border-top:{bt}; margin-top:{10 if i == 0 else 0}px">\n'
          f'        <p style="{F} font-size:24px; line-height:1.3; color:{INK}">{t}</p>\n'
          f'        <p style="{F} font-size:24px; line-height:1.3; text-align:right; color:{INK}">{v}</p>\n      </div>\n')
b += (f'      <div style="display:grid; grid-template-columns:1fr 110px; gap:16px; padding:8px 0; border-top:2px solid {INK}">\n'
      f'        <p style="{F} font-size:24px; font-weight:600; line-height:1.3; color:{INK}">Total</p>\n'
      f'        <p style="{F} font-size:24px; font-weight:600; line-height:1.3; text-align:right; color:{INK}">$500K</p>\n      </div>\n    </div>\n')
b += '    <div style="display:flex; flex-direction:column; flex:1">\n      ' + caps("What the money proves") + '\n'
for i, (t, c) in enumerate(ms):
    bt = f"2px solid {INK}" if i == 0 else f"1px solid {RULE}"
    b += (f'      <div style="display:grid; grid-template-columns:190px 1fr; gap:16px; padding:9px 0; border-top:{bt}; margin-top:{10 if i == 0 else 0}px">\n'
          f'        <p style="{F} font-size:24px; font-weight:600; line-height:1.35; color:{CORAL2}">{t}</p>\n'
          f'        <p style="{F} font-size:24px; line-height:1.35; color:{INK}">{c}</p>\n      </div>\n')
b += '    </div>\n  </div>\n  <div style="flex:1"></div>\n'
b += (f'  <div style="display:flex; flex-direction:row; gap:56px; padding:20px 0 0; border-top:2px solid {INK}">\n'
      f'    <div style="display:flex; flex-direction:column; gap:6px; flex:1">\n      {caps("Introductions wanted")}\n'
      f'      <p style="{F} font-size:24px; line-height:1.4; color:{INK}">A builder with live $10M-plus jobs in South East Queensland; a non-bank construction lender to shape the lender view.</p>\n    </div>\n'
      f'    <div style="display:flex; flex-direction:column; gap:6px; flex:1">\n      {caps("Next step")}\n'
      f'      <p style="{F} font-size:24px; line-height:1.4; color:{INK}">Walk through the product and the round with the founders.</p>\n    </div>\n  </div>\n')
b += p("James Thompson +61 409 383 030 · Gopesh Khanna +61 436 112 249 · founders@irisintelligence.com.au · Gold Coast", 24, MUTED)
S["raise"] = section("raise", b, 24, "Use of funds equals Year 1 costs in the model: founders at $100K each plus 12% super ($224K), platform build $170K, security certification $30K, cloud $16K, sales $20K, legal $20K, contingency and insurance $20K. Milestones are framed as evidence created, not outcomes promised: signed pilot agreements and the partner's letter at month 3; the scored comparison against the three historic record sets at month 4; the comparison with live cost reports signed by each builder and the security certificate at month 6; the partner's written review beside its QS report at months 6–9; the PI policy, reliance terms and legal opinion at month 9; paid invoices, a drafted condition with one lender and an assessment scope and fee at month 12; the seed raise at months 15–18 on that evidence. Terms: AUD $500K pre-seed SAFE at a $5M valuation cap (D-21).")

for k, v in S.items():
    open(os.path.join(OUT, k + ".html"), "w", encoding="utf-8").write(v)
print("wrote", list(S))
