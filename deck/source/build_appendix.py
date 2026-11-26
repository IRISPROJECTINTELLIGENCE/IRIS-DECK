#!/usr/bin/env python3
"""Generate the ten appendix pages (A1-A10) of the IRIS Investment Summary.

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
INK, BODY, MUTED, CORAL, RULE, RULE2 = "#1a1714", "#3d3934", "#6f6a63", "#c2412a", "#d9d4ca", "#ece7dc"
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

 dict(id="apx-reach", num="A4", label="Appendix A4 · Backs slide 10 · How the condition holds",
  h2="The condition rests on documents lenders already use.",
  stand="**Slide 10** assumes a lender writes IRIS into a facility. Part of that is established; part is untested.",
  cols=["520px", "1fr", "300px"], head=["Question", "Answer", "Status"],
  rows=[
   [("Can a lender require a report?", "key"), "It does today: the QS report, paid by the borrower.", ("Established", "status")],
   [("What binds the builder?", "key"), "The tender, the head contract and the side deed.", ("Standard documents", "status")],
   [("A builder already under contract?", "key"), "Owes nothing new. New facilities come first.", ("By design", "status")],
   [("What if a builder refuses?", "key"), "It sees each finding first and keeps its rates.", ("Untested", "status")],
   [("Will the drafting hold?", "key"), "Lawyers confirm the documents.", ("Month 9 opinion", "status")],
  ],
  foot=None),

 dict(id="apx-sizing", num="A5", label="Appendix A5 · Backs slide 11 · Market sizing",
  h2="The $291M market is built up from live jobs.",
  stand="**Slide 11** puts the market at $291M in Australia and $55M in Queensland. Seven steps get there.",
  cols=["560px", "170px", "130px", "1fr"], head=["Step", ("Australia", "num"), ("Qld", "num"), "Basis"],
  rows=[
   [("Apartment work a year", "key"), ("$33.5bn", "num"), ("$6.6bn", "num"), "IBISWorld, 2025–26"],
   [("Commercial work, jobs of $10M+", "key"), ("$46.1bn", "num"), ("$8.4bn", "num"), "IBISWorld; 65% share estimated"],
   [("Value under construction", "key"), ("$173bn", "num"), ("$32.6bn", "num"), "Work a year × build period"],
   [("With a construction facility", "key"), ("$139bn", "num"), ("$26.2bn", "num"), "Developer-funded share (IBISWorld)"],
   [("Live jobs, at $40M average", "key"), ("4,330", "num"), ("820", "num"), "Estimate; cross-checks in notes"],
   [("Price per job a year", "key"), ("$72K · $42K", "num"), ("same", "num"), "15 bps on $48M · $3,500 a month"],
   [("Revenue potential a year", "total"), ("$291M", "numb"), ("$55M", "numb"), "Facilities, subscriptions, assessments"],
  ],
  foot="The $40M average job and the 65% share move it most. Both are estimates."),

 dict(id="apx-model", num="A6", label="Appendix A6 · Backs slide 11 · Model assumptions",
  h2="Six assumptions drive the five-year model.",
  stand="**Slide 11** shows the base case. These inputs produce it.",
  cols=["460px", "1fr", "120px", "120px", "120px"], head=["Driver", "Assumption", ("Year 1", "num"), ("Year 3", "num"), ("Year 5", "num")],
  rows=[
   [("Lenders with the condition", "key"), "First at month 12. A company target.", ("1", "num"), ("8", "num"), ("20", "num")],
   [("Facilities", "key"), "0.8 a month per lender, plus its book", ("1", "num"), ("109", "num"), ("373", "num")],
   [("Fee per facility a year", "key"), "15 bps on $80M. Bull $102M, bear $48M", ("$120K", "num"), ("$120K", "num"), ("$120K", "num")],
   [("Paid builder jobs", "key"), "$3,500 a month each", ("12", "num"), ("34", "num"), ("92", "num")],
   [("Assessments", "key"), "$35,000 each, from month 30", ("–", "num"), ("2", "num"), ("14", "num")],
   [("Team", "key"), "Hires after the $3M seed at month 15", ("2", "num"), ("36", "num"), ("102", "num")],
   [("Revenue, base case", "total"), "", ("$0.19M", "numb"), ("$9.3M", "numb"), ("$40.5M", "numb")],
  ],
  foot="Biggest lever: each $10M of average facility is about $4.6M of Year 5 revenue."),

 dict(id="apx-sources", num="A7", label="Appendix A7 · Backs slides 2, 3 and 8 · Sources",
  h2="Where the deck’s public figures come from.",
  stand="Dated sources for **slides 2, 3 and 8**. Market and model inputs are on A5 and A6.",
  cols=["1fr", "110px", "720px"], head=["Figure", "Slide", "Source"],
  rows=[
   [("Construction, about one in four insolvencies", "key"), "2, 8", "ASIC, series 1, 14 September 2026"],
   [("Bathla: 540 entities, $3.3bn, about 40 funds", "key"), "2, 8", "ASIC data; AFR; Bloomberg"],
   [("$3.08bn owed to secured lenders", "key"), "3", "The Urban Developer, 25 September 2026"],
   [("A project rated low to medium risk", "key"), "3", "Rampart, 6 September 2026; being confirmed"],
   [("Replacement builder prices 20–40%", "key"), "3", "Founder observation"],
   [("Cash rate, CPI, dwelling values", "key"), "8", "RBA, ABS, Cotality, November 2026"],
   [("ASIC review and enforcement warning", "key"), "8", "ASIC, September 2026"],
   [("Presales and lending terms", "key"), "8", "Stamford Capital; Gravity Capital, 2026"],
   [("Quarterly valuation from July 2027", "key"), "8", "ASIC, June 2026; industry standard"],
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

 dict(id="apx-risks", num="A10", label="Appendix A10 · Backs slide 13 · Risks",
  h2="Six risks, each with a date by which we will know.",
  stand="**Slide 13**’s milestones answer these. The first two are what this round is for.",
  cols=["460px", "1fr", "220px"], head=["Risk", "What we are doing", "Know by"],
  rows=[
   [("No lender adds the condition", "key"), "A design partner runs IRIS on a live facility first.", ("Months 9–12", "status")],
   [("Builders refuse access", "key"), "The builder sees findings first; our R&D partner agreed.", ("Months 1–3", "status")],
   [("Connections take longer", "key"), "Procore first, then one system at a time.", ("Month 6", "status")],
   [("A lender cannot rely on it", "key"), "Reconciled to builders’ cost reports; PI and reliance terms.", ("Months 6–9", "status")],
   [("A platform or QS firm builds it", "key"), "Platforms serve their own customer; QS firms can be channels.", ("Ongoing", "status")],
   [("Sales cycles run long", "key"), "The seed is raised on paid use, with or without a mandate.", ("Months 15–18", "status")],
  ],
  foot=None),
]
for _pg in PAGES: _pg["notes"] = NOTES[_pg["id"]]

ORDER = [p["id"] for p in PAGES]

# ---------------------------------------------------------------- html
def esc(s): return html.escape(s, quote=False)
def runs(s):
    out = []
    for i, part in enumerate(re.split(r"\*\*(.+?)\*\*", s)):
        if part: out.append((part, 600 if i % 2 else 400))
    return out
def inline(s): return "".join(f"<b>{esc(t)}</b>" if w == 600 else esc(t) for t, w in runs(s))
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
    out = [f'<section id="{pg["id"]}" data-transition="fade" style="display:flex; flex-direction:column; gap:{GAP}px; padding:112px 128px 160px; background:#faf7f0">']
    out.append(f'  <p data-iris-label="1" style="position:absolute; top:62px; left:128px; width:1500px; {F}; font-size:24px; font-weight:600; line-height:1; letter-spacing:3px; text-transform:uppercase; color:{CORAL}">{esc(pg["label"])}</p>')
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
        rs = runs(t) if st in ("body", "muted") else [(t, wght(st))]
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
        face = " ".join([pg["label"], pg["h2"], pg["stand"], pg.get("foot") or ""] + [norm(c)[0] for c in (pg.get("head") or [])]
                        + [norm(c)[0] for r in pg.get("rows", []) for c in r] + [g for g, _ in pg.get("groups", [])]
                        + [norm(c)[0] for _, rs in pg.get("groups", []) for r in rs for c in r])
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
