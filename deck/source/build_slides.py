"""IRIS deck v4 (D-38): the 30 October deck, consolidated to 13 slides, with the five-year model,
the two products, the ecosystem map and the competitive map. Composed from the v440 / v500 sources."""
import os, re, json
V440 = "/home/claude/v440"          # 30 Oct PDF sources (de574de)
V500 = "/home/claude/base/slides"   # the owner's later comment fixes (2c4fe81)
OUT = "/home/claude/iris-deck/deck/source/slides"
F = "font-family:Inter, Arial, sans-serif;"
INK, BODY, MUTED, CORAL, CORAL2, RULE, PANEL, PANEL2 = "#1a1714", "#3d3934", "#6f6a63", "#e8533a", "#c2412a", "#d9d4ca", "#f1ede4", "#f8e6dd"
G = '<span style="color:#6f6a63">'

def rd(folder, name):
    return open(os.path.join(folder, name + ".html"), encoding="utf-8").read()

def label(text):
    return (f'  <p data-iris-label="1" style="position:absolute; top:62px; left:128px; width:1200px; {F} font-size:24px; '
            f'font-weight:600; line-height:1; letter-spacing:3px; text-transform:uppercase; color:{CORAL2}">{text}</p>\n')

def pageno(n):
    return f'  <p style="position:absolute; right:128px; bottom:64px; width:200px; {F} font-size:24px; text-align:right; color:{MUTED}">{n}</p>\n'

def h2(a, b=None):
    s = f'  <h2 style="{F} font-size:64px; font-weight:600; line-height:1.1; letter-spacing:-1.5px; color:{INK}">{a}'
    if b:
        s += f'<br><span style="color:{CORAL}">{b}</span>'
    return s + '</h2>\n'

def p(text, size=26, color=BODY, lh=1.4, extra=""):
    return f'  <p style="{F} font-size:{size}px; line-height:{lh}; color:{color};{extra}">{text}</p>\n'

def caps(text, color=MUTED, size=24):
    return f'<p style="{F} font-size:{size}px; font-weight:600; line-height:1.3; letter-spacing:3px; text-transform:uppercase; color:{color}">{text}</p>'

def section(sid, body, gap=28, aside=""):
    return (f'<section id="{sid}" data-transition="fade" style="display:flex; flex-direction:column; gap:{gap}px; '
            f'padding:112px 128px 160px; background:#faf7f0">\n{body}  <aside>{aside}</aside>\n</section>\n')

def set_page(html, n):
    return re.sub(r'(right:\s*128px;\s*bottom:\s*64px;\s*width:\s*200px;[^>]*>)[^<]*(</p>)', r'\g<1>' + n + r'\2', html, count=1)

def must(html, old, new):
    assert html.count(old) == 1, old[:70]
    return html.replace(old, new)

S = {}

# 01 cover --------------------------------------------------------------------
c = rd(V440, "cover")
c = must(c, "October 2026", "November 2026")
S["cover"] = c

# 02 summary (the owner's version, v500) ----------------------------------------
s = rd(V500, "summary")
s = must(s, "Three uses, one platform", "Two products, one platform")
s = must(s, "<b>Now:</b> builder pilot deployments on live projects, a monthly fee per project, to prove the position and value added.&nbsp;<br><b>Alongside:</b> a lender design partner shaping the lender view from those pilots.&nbsp;<br><b>At scale:</b> monitoring written into the facility, paid in basis points; distressed-project assessments at a separate fee.",
         "<b>IRIS for Builders, now:</b> pilot deployments on live projects at a monthly fee per live job, to prove the position and protect the builder’s margin.<br><b>IRIS for Lenders, alongside:</b> a design-partner lender shapes the view; at scale it is written into the facility and paid by the developer in basis points. Distressed-project assessments at a separate fee.")
s = must(s, "POC built on a populated Procore sandbox, shown to a South East Queensland Tier 2 builder; live-project access is being negotiated, not yet granted. Pre-revenue.&nbsp;",
         "MVP built on a populated Procore sandbox, shown to a South East Queensland Tier 2 builder; live-project access being negotiated. One non-bank private credit fund has told us the lender view would be useful to it. Pre-revenue.")
s = must(s, "Buys measurable validation: a deployment ready enterprise product, live data access, reconciliation against builders’ own cost reports, a lender live beside its QS, security review, and evidence of paid demand.",
         "It buys the evidence: a deployment-ready enterprise product, live data, reconciliation against builders’ own cost reports, a lender live beside its QS, a security review, and paid demand.")
s = s.replace("that is reconciled by hand, monthly", "reconciled by hand, monthly").replace("by read only API connection", "by read-only API connection")
S["summary"] = s

# 03 problem (v440 with the owner's later heading) --------------------------------
s = rd(V440, "stakes")
s = must(s, "Recoveries depend on what remains beneath the contract.", "What a lender recovers depends on the project’s real state.")
s = must(s, "<b>The consequence:</b> delivery uncertainty can result in further funding requirements, enforcement costs and credit losses. <b>What IRIS reads</b> is each funded project’s builder records: trades owed against claimed and certified, cost against forecast. The group ledger is the administrator’s.",
         "<b>The consequence:</b> delivery uncertainty becomes further funding, enforcement cost and credit loss. <b>What IRIS reads</b> is each funded project’s builder records: trades owed against claimed and certified, and cost against forecast.")
s = must(s, "Detail on appendix A6.", "Detail in appendix A7.")
S["stakes"] = s

# 04 the mechanism (systems strip + three causes) ---------------------------------
sysrow = re.search(r'(<div style="display:flex; flex-direction:row; gap:20px">.*?)\n    </div>\n  </div>', rd(V440, "systems"), flags=re.S)
strip = sysrow.group(1) + "\n    </div>"
strip = strip.replace("padding:22px 18px 24px", "padding:14px 16px 16px").replace("font-size:30px", "font-size:28px").replace("gap:10px", "gap:6px")
for a_, b_ in [("project management: drawings and documents, RFIs, correspondence, site records, defects, variations", "drawings, RFIs, site records, defects, variations"),
               ("ERP: costing, budgets, forecasts, payroll, contracts", "costing, budgets, forecasts, contracts"),
               ("trade payments: claims, certification, payment", "trade claims, certification, payment"),
               ("procurement: tenders, trades let, subcontracts", "tenders, trades let, subcontracts"),
               ("correspondence across all parties and the unstructured data around it", "correspondence across all parties"),
               ("the project’s folders: contracts, registers, reports, minutes", "contracts, registers, reports, minutes")]:
    assert strip.count(a_) == 1, a_[:30]
    strip = strip.replace(a_, b_)
rows3 = [
    ("Programme and EOTs as submitted", "Notices against the time bar.", "Notices, variations and latent conditions near or past the deadline that decides who pays.", "Aconex, Procore, email"),
    ("Cost to complete on the contract sum", "Cost moving before it is notified.", "Delays, changes and allowance movements the records show coming, and the preliminaries they extend.", "Programme, Jobpac forecast, email"),
    ("Builder’s statutory declaration", "Cash strain in the trades.", "What subcontractors are owed against what the builder has already claimed and been paid for their work. Usually the first sign.", "PayApps, Jobpac"),
]
b = label("Problem · the mechanism") + pageno("04")
b += h2("The lender’s monthly check reports a filtered position.", "The real one sits in the builder’s systems, assembled by hand.")
b += '  <div style="display:flex; flex-direction:column; gap:14px">\n    ' + strip.replace("\n", "\n  ") + '\n  </div>\n'
b += '  <div style="display:flex; flex-direction:column">\n'
b += (f'    <div style="display:grid; grid-template-columns:440px 1fr 340px">\n'
      f'      <p style="padding:12px 20px 10px; {F} font-size:24px; font-weight:600; line-height:1.2; letter-spacing:3px; text-transform:uppercase; color:#cfc8bb; background:{INK}">The lender’s QS reports</p>\n'
      f'      <p style="padding:12px 20px 10px; {F} font-size:24px; font-weight:600; line-height:1.2; letter-spacing:3px; text-transform:uppercase; color:{CORAL2}; background:{PANEL2}; border-left:3px solid {CORAL}">What sits beneath it, by cause</p>\n'
      f'      <p style="padding:12px 20px 10px; {F} font-size:24px; font-weight:600; line-height:1.2; letter-spacing:3px; text-transform:uppercase; color:#5f5a53; background:{PANEL2}">Where it lives</p>\n    </div>\n')
for qs, head, body, src in rows3:
    b += (f'    <div style="display:grid; grid-template-columns:440px 1fr 340px">\n'
          f'      <p style="padding:8px 20px; {F} font-size:24px; line-height:1.4; color:#efe9dc; background:{INK}; border-top:1px solid #3a3530">{qs}</p>\n'
          f'      <p style="padding:8px 20px; {F} font-size:24px; line-height:1.4; color:{INK}; background:{PANEL2}; border-left:3px solid {CORAL}"><b>{head}</b> {body}</p>\n'
          f'      <p style="padding:8px 20px; {F} font-size:24px; line-height:1.4; color:#5f5a53; background:{PANEL2}; border-top:1px solid #ecc9bb">{src}</p>\n    </div>\n')
b += '  </div>\n  <div style="flex:1"></div>\n'
b += p("Since 2021, fixed prices, thinner builders and in-house delivery have moved more of the risk inside the project. The lender’s view is still a certificate on the head contract. Six causes and the market shifts: appendix A2, A3.", 24, MUTED)
S["mechanism"] = section("mechanism", b, 22, rd(V500, "mechanism").split("<aside>")[1].split("</aside>")[0] + " The systems: " + rd(V440, "systems").split("<aside>")[1].split("</aside>")[0])

# 05 evidence (v440) -------------------------------------------------------------
s = set_page(rd(V440, "evidence"), "05")
s = must(s, "weeks before it reached the people funding them.", "months before it reached the people funding them.")
s = must(s, "Investor syndicate; private financier; QS-gated drawdowns", "Investor syndicate with a private financier and QS-gated drawdowns")
S["evidence"] = s

# 06 solution: v440 top + two products ------------------------------------------
s = rd(V440, "product")
s = set_page(s, "06")
top = s.split('<div id="pc698a2a917fcr3-cbb80cd7"')[0]
aside = s.split("<aside>")[1].split("</aside>")[0]
panels = [
    ("IRIS for Builders", INK, "The same position, first: notices near time bars, unlet scope, trades owed, defects. The builder keeps its margin. <b>$3,500 a month per live job.</b>", "Builder pays · $3,500 a month per live job"),
    ("IRIS for Lenders", CORAL2, "Each facility’s position beneath the certificate, continuously, with drill-down to the record. <b>In the facility; the developer pays 15 bps a year.</b>", "Developer pays · 15 bps a year on the facility"),
    ("Permissions and distress", MUTED, "The builder authorises and sees each finding first; lender and developer see the reconciled position. <b>In distress, the position in days.</b>", "Role-based, one platform"),
]
b = top.rstrip() + '\n  <div style="position:absolute; top:772px; left:128px; width:1664px; display:flex; flex-direction:row; gap:40px">\n'
for t, tc, body, pays in panels:
    bt = CORAL if tc == CORAL2 else (RULE if tc == MUTED else INK)
    b += (f'    <div style="display:flex; flex-direction:column; gap:6px; flex:1; padding:14px 0 0; border-top:3px solid {bt}">\n'
          f'      {caps(t, tc)}\n      <p style="{F} font-size:24px; line-height:1.35; color:{BODY}">{body}</p>\n    </div>\n')
b += '  </div>\n  <aside>' + aside + " One platform, two products (D-35): the builder's product and the lender's product read the same reconciled position; what differs is the view, the entitlement and the buyer. The developer's fee is paid out of the facility; the hypothesis that a monitored facility prices inside an unmonitored one is tested with the design partner at month 9.</aside>\n</section>\n"
S["product"] = b

# 07 mvp (v440) -------------------------------------------------------------------
S["mvp"] = set_page(rd(V440, "mvp"), "07")

# 08 why now (v440, right column replaced) ----------------------------------------
s = rd(V440, "why-now")
s = set_page(s, "08")
s = must(s, "Across the cycle", "The market’s answer so far")
old_cycle = re.search(r'The layer beneath the certificate goes unreported in good markets too;.*?</p>', s, flags=re.S).group(0)
s = s.replace(old_cycle, "Lender-side monitoring is being sold as a loan condition, done by site walks and register checks. Builder-side AI is being sold to builders, on builders’ data. Reading the builder’s systems for the lender is open ground; the names are on the next slide.</p>")
s = must(s, "<b>Not confined to one group.</b> A $2.3bn real-estate credit fund suspended redemptions on 22 October. Construction was 37% of insolvencies in July–August with Bathla, 23.5% without",
         "<b>Not confined to one group.</b> A $2.3bn credit fund suspended redemptions on 22 October. Construction was 37% of insolvencies in July–August with Bathla, 23.5% without")
s = s.replace("appendix A6", "appendix A7")
for a_, b_ in [
    ("<b>Rates and feasibility.</b> The cash rate rose 100 bps in 2026, to 4.60% on 30 September; annual CPI 4.3% to September, trimmed mean 3.6%. Dwelling values 5.2% below their March peak; sales 19% below a year earlier ",
     "<b>Rates and feasibility.</b> The cash rate rose 100 bps in 2026 to 4.60%; CPI 4.3% to September. Dwelling values 5.2% below their March peak "),
    ("<b>Bathla.</b> 540 entities into administration on 25 August; about $3.3bn owed to about 40 funds. Redemptions paused from 14 August; sites closed, receivers appointed from late September ",
     "<b>Bathla.</b> 540 entities into administration on 25 August; about $3.3bn owed to about 40 funds; sites closed and receivers appointed by late September "),
    ("<b>Valuation scrutiny.</b> ASIC reviewed 52 funds holding $76bn before 30 June, warned on 22 September to prepare for enforcement and on 30 September named residential construction. Three listed credit funds suspended 28 September after a $168M write-down ",
     "<b>Valuation scrutiny.</b> ASIC reviewed 52 funds holding $76bn, warned on 22 September to prepare for enforcement, and on 30 September named residential construction "),
    ("Models that read contracts, correspondence and cost records together and cite the source for each figure, at a cost that works per project per month. The tooling makes IRIS possible; the market makes it wanted.",
     "Models now read contracts, correspondence and cost records together and cite the source of each figure, at a cost that works per project per month."),
    ("In June 2026 ASIC told private credit funds to reassess loan values before formal default; the industry standard from July 2027 requires quarterly independent valuation. Forecasts of further distress are not treated as fact.",
     "From July 2027 the private credit industry standard requires quarterly independent valuation of loans; ASIC asked funds in June 2026 to reassess values before default."),
]:
    assert s.count(a_) == 1, a_[:40]
    s = s.replace(a_, b_)
S["why-now"] = s

# 09 go to market (v440 table + the mandate chain) --------------------------------
s = rd(V440, "go-to-market")
s = set_page(s, "09")
s = must(s, "Scale · Monitoring and assessments", "Scale · IRIS for Lenders")
s = must(s, "Builders prove it, a lender shapes it, monitoring scales it.", "Builders prove it on live jobs. A lender then writes IRIS into its facilities.")
s = must(s, "<b>Nothing assumed automatic:</b> no access, no pilot; no reconciled result, no lender test; no live result, no condition (milestones, slide 18).", "<b>Each step is gated on the one before it.</b> No access, no pilot. No reconciled result, no lender test. No live result, no condition.")
if "bottom:64px" not in s.split("<h2")[0]:
    s = s.replace("<h2", pageno("10") + "  <h2", 1)
for a_, b_ in [
    ("<b>Prove it on live jobs.</b> R&amp;D deployments on live projects, then a monthly fee per project. The proving ground, and a revenue line of its own.", "<b>Prove it on live jobs.</b> Two pilots, then a monthly fee per live job that follows the builder."),
    ("The position reconciles to the builder’s own cost reports and finds exposures that protect the builder’s margin.", "The position reconciles to the builder’s own cost reports and protects its margin."),
    ("<b>Shape the lender view</b> from the pilots: what to show, how it is structured, and how it bears on the facility and the lender’s position.", "<b>Shape the lender view</b> from the pilots: what to show, how it bears on the facility."),
    ("The design partner uses it on a live facility beside its QS; security, professional indemnity and reliance terms in place.", "The partner runs it on a live facility beside its QS; security, PI and reliance terms in place."),
    ("<b>A drawdown condition</b> on new facilities, extensions and refinances; then other lenders. Distressed-project assessments at a separate fee.", "<b>A drawdown condition</b> on one facility, then the lender’s book, then the next lender."),
    ("A live result the lender’s credit committee accepts, written into one facility; then the next lender after a live result.", "A live result the lender’s credit committee accepts, written into one facility."),
    ("Developer, in bps; lender or receiver per assessment", "Developer, 15 bps on the facility; lender or receiver per assessment"),
]:
    assert s.count(a_) == 1, a_[:40]
    s = s.replace(a_, b_)
head = s.split('  <div style="display:flex; flex-direction:row; gap:48px">')[0]
assert "Who requires it" not in head
aside = s.split("<aside>")[1].split("</aside>")[0]
chain = re.search(r'(<div style="display:flex;flex-direction:row;align-items:stretch">.*?</div>\n</div>)', rd(V440, "reach"), flags=re.S)
chain_html = chain.group(1)
assert "Drawdown condition" in chain_html and "Side deed" in chain_html
chain_html = chain_html.replace("padding:20px 24px", "padding:12px 20px")
b = head.rstrip() + "\n"
b += '  <div style="display:flex; flex-direction:column; gap:14px">\n    ' + caps("How the condition holds · the facility binds the developer, the tender binds the builder") + "\n"
b += "    " + chain_html.replace("\n", "\n    ") + "\n"
b += (f'    <p style="{F} font-size:24px; line-height:1.4; color:{BODY}">A builder under contract today owes nothing new; the first conditions go on new facilities, extensions and refinances. Mechanics and the carve-out question: appendix A4.</p>\n  </div>\n')
b += '  <aside>' + aside + " The lender signal (D-36) is a founder-reported conversation with one non-bank private credit fund, unnamed; no letter yet.</aside>\n</section>\n"
S["go-to-market"] = b

# 10 competition: map + table ------------------------------------------------------
def dot(x, y, name, fill=INK, dashed=False, w=600):
    st = f'stroke="{fill}" stroke-width="2" stroke-dasharray="6 5" fill="none"' if dashed else f'fill="{fill}"'
    return (f'<circle cx="{x}" cy="{y}" r="9" {st}/><text x="{x+16}" y="{y+8}" font-family="Inter, Arial, sans-serif" font-size="22" font-weight="{w}" fill="{INK}">{name}</text>')
svg = ('<svg xmlns="http://www.w3.org/2000/svg" aria-label="Map of products by whether they read the builder\'s systems and whether they serve the lender" viewBox="0 0 760 560" style="width:600px; height:442px">'
       '<rect x="70" y="20" width="670" height="480" fill="#f1ede4"/>'
       '<rect x="405" y="20" width="335" height="240" fill="#f8e6dd"/>'
       '<path d="M405 20V500" stroke="#CFC8BB" stroke-width="2" stroke-dasharray="6 5"/><path d="M70 260H740" stroke="#CFC8BB" stroke-width="2" stroke-dasharray="6 5"/>'
       '<text x="76" y="546" font-family="Inter, Arial, sans-serif" font-size="20" font-weight="600" letter-spacing="2" fill="#6f6a63">DOES NOT READ THE BUILDER’S SYSTEMS</text>'
       '<text x="500" y="546" font-family="Inter, Arial, sans-serif" font-size="20" font-weight="600" letter-spacing="2" fill="#6f6a63">READS THE BUILDER’S SYSTEMS</text>'
       '<text transform="translate(40 250) rotate(-90)" font-family="Inter, Arial, sans-serif" font-size="20" font-weight="600" letter-spacing="2" fill="#6f6a63">SERVES THE LENDER</text>'
       '<text transform="translate(40 490) rotate(-90)" font-family="Inter, Arial, sans-serif" font-size="20" font-weight="600" letter-spacing="2" fill="#6f6a63">SERVES THE BUILDER</text>'
       + dot(120, 70, "Lender’s QS") + dot(120, 130, "Korrix") + dot(120, 190, "IPEX") + dot(250, 70, "SteelCap (announced)", MUTED, True)
       + dot(300, 190, "Built (US)") + dot(120, 330, "Lendbase (origination)", MUTED) + dot(450, 330, "Procore + Datagrid") + dot(450, 390, "Cintech") + dot(450, 450, "Vyne (preview)", MUTED, True)
       + f'<circle cx="600" cy="130" r="14" fill="{CORAL}"/><text x="622" y="139" font-family="Inter, Arial, sans-serif" font-size="26" font-weight="600" fill="{CORAL2}">IRIS</text>'
       '</svg>')
comp = [
    ("Lender’s QS", "The claim, builder submissions", "Lender", "Certifies work in place monthly. Not independently verified."),
    ("Korrix (AU)", "Registers, site walks, builder reports", "Lender", "A monthly brief by hand; proposes a loan condition. Reads no systems."),
    ("IPEX (AU)", "A payment account", "Lender", "Controls money movement. No project position."),
    ("Built (US)", "Procore financials, draw package", "Lender", "Checks the submitted draw. No Australian presence."),
    ("Cintech · Vyne", "The builder’s systems", "Builder", "Cited answers and actions for the builder. Shares nothing upward."),
    ("SteelCap (AU)", "Unknown", "Lender", "A landing page and an early-access form."),
    ("IRIS", "The builder’s systems, read-only", "All three", "One reconciled position, each figure linked to its record, in the facility."),
]
b = label("Competition") + pageno("09")
b += h2("Others watch the project from outside, or serve the builder.", "IRIS reads the builder’s systems for the lender.")
b += '  <div style="display:flex; flex-direction:row; gap:40px; align-items:start">\n    ' + svg + '\n    <div style="display:flex; flex-direction:column; flex:1">\n'
b += (f'      <div style="display:grid; grid-template-columns:180px 240px 110px 1fr; gap:14px; padding:0 0 8px; border-bottom:2px solid {INK}">\n'
      f'        {caps("Who")}\n        {caps("Reads")}\n        {caps("Serves")}\n        {caps("Where it stops")}\n      </div>\n')
for i, (who, reads, serves, stop) in enumerate(comp):
    last = i == len(comp) - 1
    bg = f" background:{PANEL2}; border-top:2px solid {CORAL};" if last else f" border-top:1px solid {RULE};"
    wc = CORAL2 if last else INK
    b += (f'      <div style="display:grid; grid-template-columns:180px 240px 110px 1fr; gap:14px; padding:6px 0;{bg}">\n'
          f'        <p style="{F} font-size:24px; font-weight:600; line-height:1.3; color:{wc}">{who}</p>\n'
          f'        <p style="{F} font-size:24px; line-height:1.3; color:{INK}">{reads}</p>\n'
          f'        <p style="{F} font-size:24px; line-height:1.3; color:{INK}">{serves}</p>\n'
          f'        <p style="{F} font-size:24px; line-height:1.3; color:{BODY}">{stop}</p>\n      </div>\n')
b += '    </div>\n  </div>\n  <div style="flex:1"></div>\n'
b += p("About sixty products and firms reviewed, November 2026; sources and detail in appendix A8.", 24, MUTED)
S["competition"] = section("competition", b, 28, "Korrix Intelligence Partners (Sydney): Assess (builder financial health check from nine registers and reports), Monitor (monthly: progress meetings, site walks, covenant register, risk brief; proposed as a loan condition at a fixed monthly fee), Protect (insurance layer in development); reports only to the lender; no software integrations. SteelCap: a landing page, coming soon. IPEX: payment-account control with vendor-claimed lender mandates; moves money, does not read the position. Built: draw management for 300+ US lenders, reads Procore financials, checks the submitted package; no ANZ presence. Cintech: one record per project from thirteen named connectors (Aconex, Procore, ProcurePro, PayApps, Jobpac and others), cited answers, AI workers, time bars; founders ex-CIO and ex-infrastructure lead at Tier 2 builders; no customers named. Vyne: decision intelligence and organisational memory for builders; illustrative preview, no live systems. Procore with Datagrid: agents over the builder's ERP and documents, for the builder. Lendbase: a commercial-lending origination marketplace, upstream of the facility; a channel rather than a competitor. The lender's existing controls are the QS certificate, IPEX, project trust accounts and CreditorWatch or iCIRT ratings. IPEX is not a partner. Full review: research/competitive-landscape.md.")

# 11 market and model ---------------------------------------------------------------
def trow(cells, bold=False, top=False, color=INK, size=24):
    st = f"border-top:{'2px solid ' + INK if top else '1px solid ' + RULE};"
    w = "600" if bold else "400"
    s_ = f'      <div style="display:grid; grid-template-columns:1fr 100px 100px 100px 100px 100px; gap:10px; padding:6px 0; {st}">\n'
    s_ += f'        <p style="{F} font-size:{size}px; font-weight:{w}; line-height:1.3; color:{color}">{cells[0]}</p>\n'
    for v in cells[1:]:
        s_ += f'        <p style="{F} font-size:{size}px; font-weight:{w}; line-height:1.3; text-align:right; color:{color}">{v}</p>\n'
    return s_ + '      </div>\n'

b = label("Market and model") + pageno("11")
b += h2("A $291M market a year in Australia at our prices.", "Each lender brings its book, so the curve bends in Year 3.")
b += '  <div style="display:flex; flex-direction:row; gap:48px; align-items:start">\n    <div style="display:flex; flex-direction:column; width:560px; flex:none">\n'
for n, nc, t, c2 in [("$291M", CORAL, "Total market, Australia · modelled", "About 4,300 live jobs of $10M and over at our prices: facilities, subscriptions, assessments."),
                     ("$55M", INK, "Serviceable, Queensland · modelled", "About 820 live jobs; South East Queensland holds about 80% of the state’s pipeline."),
                     ("$49.5M", INK, "Obtainable · month-60 run rate, base case", "Twenty lenders on about 370 facilities; seventeen builders on 92 jobs. About 17% of Australia.")]:
    b += (f'      <div style="display:flex; flex-direction:column; gap:6px; padding:12px 0 14px; border-top:3px solid {INK}">\n'
          f'        <p style="{F} font-size:48px; font-weight:600; line-height:1; letter-spacing:-2px; color:{nc}">{n}</p>\n'
          f'        <p style="{F} font-size:24px; font-weight:600; line-height:1.3; color:{INK}">{t}</p>\n'
          f'        <p style="{F} font-size:24px; line-height:1.35; color:{BODY}">{c2}</p>\n      </div>\n')
b += '    </div>\n    <div style="display:flex; flex-direction:column; flex:1">\n'
b += (f'      <div style="display:grid; grid-template-columns:1fr 100px 100px 100px 100px 100px; gap:10px; padding:0 0 6px">\n        {caps("Base case · A$K")}\n'
      + ''.join(f'        <p style="{F} font-size:24px; font-weight:600; line-height:1.3; text-align:right; color:{MUTED}">Y{y}</p>\n' for y in range(1, 6)) + '      </div>\n')
b += trow(["IRIS for Lenders, paid by developers", "8", "1,559", "8,114", "20,527", "36,846"], top=True)
b += trow(["IRIS for Builders", "178", "756", "1,162", "1,911", "3,157"])
b += trow(["IRIS for Developers, direct, from Year 3", "–", "–", "35", "202", "348"])
b += trow(["Distressed-project assessments", "–", "–", "62", "266", "488"])
b += trow(["Revenue", "186", "2,315", "9,373", "22,906", "40,839"], bold=True)
b += trow(["People", "224", "1,655", "4,256", "8,472", "14,110"], top=True)
b += trow(["Platform, cloud, security", "224", "242", "499", "930", "1,521"])
b += trow(["Sales, legal, insurance, office", "61", "607", "1,871", "3,860", "5,975"])
b += trow(["Total costs, with 5% contingency", "519", "2,629", "6,958", "13,926", "22,687"], bold=True)
b += trow(["Operating result (EBITDA)", "−332", "−315", "+2,416", "+8,980", "+18,152"], bold=True, color=CORAL2)
b += '    </div>\n  </div>\n  <div style="flex:1"></div>\n'
b += p("At year end: 1 / 3 / 8 / 14 / 20 lenders on 1 / 30 / 109 / 229 / 373 facilities; team 2 / 18 / 37 / 70 / 103. Upside $63M and conservative $7.6M in Year 5; cash positive with the $3M seed. The lender cadence is a company target; inputs and sources in appendix A5, A6.", 24, MUTED)
S["economics"] = section("economics", b, 24, "All figures from financial-model/IRIS_model_5y.xlsx, base case (D-37, 4 November 2026). Market: IBISWorld building work in scope converted to value under construction by build period, divided by a $40M average contract; facility fee 15 bps on the project debt stack at 1.2 times the build contract, within a $3,500 floor and $10,000 cap a month; assessments at 4% of funded projects a year × a $35,000 fee benchmarked to QS reports. Lender line: lenders adopting at months 12, 18, 22, 26, 29, 32, 34, 36 and then about every two months to 20 at month 60; each adds 0.8 new facilities a month and ten facilities from its existing book over 18 months as loans re-paper; 24-month term; $80M average facility, so the cap binds at $120,000 a year. Builder line: two pilots paid from month 6, then builders at months 12, 20, 28, 33, 37, 40, 43, 46, 48, 50, 52, 54, 56, 58, 60; each starts with two jobs and grows to six; $3,500 a month per job. Developer-direct: 0.5 projects a month from month 30 at $2,500. Assessments from month 30: 60% of on-platform distressed facilities, plus off-platform wins ramping to eight a year. Costs: founders at $100K then $180K from Year 3; fixed roles by start month; deployment analysts one per eight live jobs; a lender success manager per two lenders; two engineers plus one per 1.5 lenders; commissions 8% of first-year fees on new facilities; $4,000 to connect each facility; cloud $250 a month per live job; PI insurance to $500K; sales and marketing to $1.6M; 5% contingency. Year 1 costs about equal the $500K use of funds. Upside: lenders faster, 1.0 facilities a month, 14 from the book; conservative: seven lenders at 0.5 a month, $60M facilities at 12.5 bps, overheads at half. Seed $3M at month 15 in all cases; Series A optional and shown separately.")

# 12 team (v440) --------------------------------------------------------------------
S["team"] = set_page(rd(V440, "team"), "12").replace("co-founding Advisor", "Co-founding advisor")

# 13 the round + close (flex rebuild of the v440 slide) ---------------------------
aside = rd(V440, "raise").split("<aside>")[1].split("</aside>")[0]
uof = [("Founder salaries, both full-time, with super", "$224K"), ("Platform build and R&D", "$170K"), ("Enterprise security and cyber audit", "$30K"),
       ("Cloud and LLM infrastructure", "$16K"), ("Sales, marketing and customer success", "$20K"), ("Legal, accounting and IP", "$20K"), ("Contingency and insurance", "$20K")]
ms = [("Months 1–3", "Two builder pilots live by API; a design-partner lender engaged. <span style=\"color:#6f6a63\">Evidence: signed pilot agreements; the partner’s letter.</span>"),
      ("Month 6", "Reconciles to builders’ cost reports; first paying builder; security certified. <span style=\"color:#6f6a63\">Evidence: the signed comparison; the security certificate.</span>"),
      ("Month 9", "The lender view live on a facility beside its QS; PI cover, reliance terms, legal opinion. <span style=\"color:#6f6a63\">Evidence: the partner’s written review; the opinion.</span>"),
      ("Month 12", "Builders paying across their jobs; a drafted condition with one lender; assessments scoped. <span style=\"color:#6f6a63\">Evidence: paid invoices and the drafted condition.</span>"),
      ("Months 15–18", "Seed raise on that evidence, with or without a lender mandate.")]
b = label("The round") + pageno("13")
b += h2("$500K, SAFE at a $5M cap, to prove IRIS on live data<br>and open the paid routes to the lender.")
b += '  <div style="display:flex; flex-direction:row; gap:56px">\n    <div style="display:flex; flex-direction:column; width:560px; flex:none">\n      ' + caps("Use of funds") + '\n'
for i_, (t, v) in enumerate(uof):
    bt = f"2px solid {INK}" if i_ == 0 else f"1px solid {RULE}"
    b += (f'      <div style="display:grid; grid-template-columns:1fr 100px; gap:16px; padding:8px 0; border-top:{bt}; margin-top:{10 if i_ == 0 else 0}px">\n'
          f'        <p style="{F} font-size:24px; line-height:1.3; color:{INK}">{t}</p>\n        <p style="{F} font-size:24px; line-height:1.3; text-align:right; color:{INK}">{v}</p>\n      </div>\n')
b += (f'      <div style="display:grid; grid-template-columns:1fr 100px; gap:16px; padding:8px 0; border-top:2px solid {INK}">\n'
      f'        <p style="{F} font-size:24px; font-weight:600; line-height:1.3; color:{INK}">Total</p>\n        <p style="{F} font-size:24px; font-weight:600; line-height:1.3; text-align:right; color:{INK}">$500K</p>\n      </div>\n    </div>\n')
b += '    <div style="display:flex; flex-direction:column; flex:1">\n      ' + caps("What the money proves · and the evidence each step leaves") + '\n'
for i_, (t, c2) in enumerate(ms):
    bt = f"2px solid {INK}" if i_ == 0 else f"1px solid {RULE}"
    tc = CORAL2 if t == "Month 12" else INK
    b += (f'      <div style="display:grid; grid-template-columns:170px 1fr; gap:16px; padding:9px 0; border-top:{bt}; margin-top:{10 if i_ == 0 else 0}px">\n'
          f'        <p style="{F} font-size:24px; font-weight:600; line-height:1.35; color:{tc}">{t}</p>\n        <p style="{F} font-size:24px; line-height:1.35; color:{INK}">{c2}</p>\n      </div>\n')
b += '    </div>\n  </div>\n  <div style="flex:1"></div>\n'
b += (f'  <div style="display:flex; flex-direction:row; gap:48px; padding:18px 0 0; border-top:2px solid {INK}">\n'
      f'    <div style="display:flex; flex-direction:column; gap:4px; flex:1">\n      {caps("Introductions wanted")}\n'
      f'      <p style="{F} font-size:24px; line-height:1.35; color:{INK}">A SEQ builder with live $10M-plus jobs; a construction lender to run the lender view beside its QS.</p>\n    </div>\n'
      f'    <div style="display:flex; flex-direction:column; gap:4px; width:560px; flex:none">\n      {caps("Next step · founders@irisintelligence.com.au")}\n'
      f'      <p style="{F} font-size:24px; line-height:1.35; color:{INK}">Walk through the product and the round with the founders.</p>\n    </div>\n  </div>\n')
S["raise"] = section("raise", b, 24, aside + " Contacts: James Thompson +61 409 383 030, Gopesh Khanna +61 436 112 249.")

order = ["cover", "summary", "stakes", "mechanism", "evidence", "product", "mvp", "why-now", "competition", "go-to-market", "economics", "team", "raise"]
for k in order:
    html = S[k]
    html = html.replace("Investment summary · Pre-seed", "Investment summary · Pre-seed")
    open(os.path.join(OUT, k + ".html"), "w", encoding="utf-8").write(html)
d = json.load(open("/home/claude/iris-deck/deck/source/deck.json"))
d["order"] = order
d["sections"] = {"s1": {"description": "What IRIS is and the round, in one page", "start": "cover"},
                 "s2": {"description": "The problem: funded projects fail; the real position sits in the builder's systems; three real jobs", "start": "stakes"},
                 "s3": {"description": "The solution: one reconciled position, two products; the MVP", "start": "product"},
                 "s4": {"description": "Why now, the route to market, competition", "start": "why-now"},
                 "s5": {"description": "Market and model, team, the round", "start": "economics"}}
json.dump(d, open("/home/claude/iris-deck/deck/source/deck.json", "w"), ensure_ascii=False)
print("wrote", order)
