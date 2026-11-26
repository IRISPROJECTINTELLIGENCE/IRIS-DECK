# CLAUDE.md — IRIS Investment Deck workspace

This repository is the self-contained development and review environment for the **IRIS Investment Summary**, the pre-seed deck for IRIS Intelligence Pty Ltd. Read this file first in every session. Nothing here depends on an earlier conversation.

## What this is

- **Company:** IRIS Intelligence Pty Ltd (ACN 700 449 618), Gold Coast, Queensland. Two founders (referred to externally as directors): James Thompson (commercial) and Gopesh Khanna (technical). Pre-revenue.
- **Product:** IRIS reads the systems a construction project already runs (Procore / Aconex, Jobpac, PayApps, ProcurePro, email and Office, share drive), by builder-authorised, read-only API connections, and reconciles them into one source-linked delivery risk position across the management domains (cost, time, scope, procurement, payment, quality, safety, compliance), with drill-down to the record and a chat that answers from the records. It writes nothing back and replaces nothing.
- **Working thesis (cover):** "A risk tool for development and construction lending." IRIS gives construction capital a source-linked view of project delivery risk, reconciling fragmented project records to identify emerging exposure and inform funding, intervention and recovery decisions. The owner restored this wording on 4 Nov 2026 after a v507 rewrite; do not change the cover line. One platform, two products (D-35): IRIS for Lenders and IRIS for Builders, separated by role-based permissions.
- **Raise:** AUD $750K pre-seed SAFE at a $4M valuation cap (owner decision D-39, 24 November 2026; previously $500K at $5M, D-21). The round is framed as the build of the enterprise product (D-40). **Do not change the terms** without project-owner approval.
- **Status:** Proof of concept (slide 7 shows it) on a populated Procore sandbox. An R&D partnership is agreed with one South East Queensland Tier 2 builder, with access to real project data (owner, 22–24 November 2026). No recovery engagement run. No lender mandate. No paying customer.

## The investment narrative (three applications of one platform)

The deck's current sequence, approved by the project owner on 29 October 2026 (see `review/review-decisions.md`, D-07):

1. **Now — builder pilot deployments** on live projects, at $3,500 a month per project, to prove the position reconciles to the builder's own cost reports. The technical and commercial proving ground.
2. **Alongside — a lender design partner** (target: a non-bank private credit fund) shaping the lender view from those pilots: what to show, how it is structured, how it bears on the facility and the lender's position.
3. **At scale — continuous lender monitoring** written into facilities as a drawdown condition, paid by the developer at 15 bps a year on the full project debt stack, senior alone or senior with mezzanine (floor $3,500, cap $10,000 a month; $48M average facility in the base case, $72,000 a year, D-49); **distressed-project assessments** offered after that, at a separate fixed fee per engagement.

The setup brief that created this workspace described recovery and assessment as the *near-term* entry. That wording predates the 29 October decision. The deck, the review files and this file follow the later decision. Do not reorder the applications without a documented decision in `review/review-decisions.md` and project-owner approval.

## Product scope (decided)

- IRIS reads the **builder's systems only**. Facility, equity, presales and sunset figures are the lender's own inputs to its view, not systems IRIS ingests.
- When a builder's internal forecast and its developer-facing forecast differ, IRIS **reports the system of record and flags the gap**; it does not adjudicate.
- IRIS **does not** replace the QS, the site inspection, an independent cost-to-complete assessment or professional judgement; it certifies nothing and values nothing. It makes **no** builder scoring, company-wide solvency assessment or payment surveillance across a builder's book.
- Competition is framed as a bounded claim (D-35): as of November 2026, no product found that reads a project's source systems and reconciles them into one position for the lender, the builder and the developer. Korrix (lender-side service), SteelCap (announced), Cintech and Vyne (builder-side) are named on slide 9. Adjacent software is either a source system IRIS reads or a tool it sits beside. IPEX is not a partner. A partnership would only be considered with a product similar enough in logic to merge with.

## Repository layout

```
deck/source/            deck.json (main deck, 13 slides, D-35) and appendix.json (appendix deck, A1–A10) + slides/*.html — the editable source (Slides artifact format). Two Slides artifacts: the main deck and "IRIS Investment Summary · Appendix"; the appendix is not in the main deck (D-26). Main order: cover, summary, stakes, mechanism, evidence, product, mvp, why-now, competition, go-to-market, economics, team, raise. Appendix (rebuilt 26 Nov 2026, generated by deck/source/build_appendix.py with notes in appendix_notes.json): apx-pack (A1, backs slide 6), apx-mechanism (A2, slide 4), apx-since-2021 (A3, slide 4), apx-reach (A4, slide 10), apx-sizing (A5, slide 11), apx-model (A6, slide 11), apx-sources (A7, slides 2, 3, 8), apx-landscape (A8, slide 9), apx-recovery (A9, assessments), apx-risks (A10, slide 13). Each page: a one-line heading, one line naming the slide it backs, one short table of single-line rows, detail in the notes. Keep it that lean.
deck/source/format-reference/   the Slides format reference (SKILL.md and reference/*.md); read before editing a slide
deck/source/measure.py  line-fit measurement script (see "Editing slides")
deck/assets/            iris-mvp-horizon-tower.png (slide 6, uploaded to the main artifact as /_blob/03ce40e84c34ae3aba2336b0250a6ca4); Inter is loaded from Google Fonts
deck/exports/           PDF exports of approved versions (none committed at baseline; see "Exports")
financial-model/        build_model.py (generates the five-year workbook) and IRIS_model_5y.xlsx (the controlled source); the 36-month model is kept as *_legacy
research/source-register.md   every public source the deck cites, with URL and date
research/market-evidence.md   the dated market facts behind slides 2, 8, A3
research/competitive-landscape.md   the October 2026 review of about sixty products and firms, with the 4 November addendum (Korrix, SteelCap, Cintech, Vyne) and the 26 November re-read, behind slides 9 and A8
research/IRIS-Competitive-Landscape.xlsx   the one-sheet competitor table sent with the deck, generated by research/build_competitor_table.py
review/investment-thesis.md   the thesis, the three applications, the sequence
review/investment-critique.md ChatGPT's independent review findings (append-only log)
review/claims-register.md     every material claim classed by evidence type
review/change-log.md          slide-by-slide record of substantive changes
review/review-decisions.md    numbered decisions and approvals by the project owner
```

## Editing slides

- Each slide is a `<section>` of 1920×1080 with inline styles; padding 112px top, 128px sides, 160px bottom (content width 1664px). Text is never below 24px. Speaker notes live in `<aside>`. Read `deck/source/format-reference/format.md`, `layout.md` and `styles.md` before changing structure.
- **Never render to check fit.** Measure lines instead: write a JSON spec `[{"label","text","size","width","wght","ls"}]` and run `python3 -I deck/source/measure.py <inter-variable.woff2> spec.json`. The font file is `@fontsource-variable/inter` (`inter-latin-opsz-normal.woff2`); install with `npm i @fontsource-variable/inter` into a scratch folder. Keep every slide's content inside the 808px vertical budget.
- **Design language:** cream background #FAF7F0, ink #1A1714, body #3D3934, muted #6F6A63, coral #E8533A / #C2412A, rules #D9D4CA, panels #F1EDE4 / #F8E6DD. Inter. One central conclusion per slide. No new slides unless something is consolidated.
- **Banned words on the deck** (the project owner's rule): nobody, every, only, never, always, guarantees, prevents, real time. Run a grep before every commit.
- **Confidentiality:** no employers, prospects, customer funds, lenders or project names on the deck. The three project examples on slide 4 are real record sets with names, values, delivery models and lags altered; keep them unidentifiable. The private research notes behind them are **not** in this repository and must not be added without the project owner's written authorisation.
- Page numbers are hand-set in each slide file (`02`–`13`; `A1`–`A10` in the appendix deck); renumber when the order changes. Every slide but the cover carries a section label (`<p data-iris-label="1" …>` at top 62px, coral caps): Summary, Problem, Problem · the mechanism, Evidence, Solution, Solution · proof of concept, Why now, Competition, Go to market, Market and model, Team, The round, Appendix An · Backs slide N · name (the owner's in-page edits drop the `data-iris-label` attribute; the label text and position are what matter). `deck.json` carries order and section descriptions. `deck/source/build_slides.py` generated the 13 main slides in the 4 November rebuild (D-35); the HTML in `deck/source/slides/` is the source of record and is edited directly from here on.
- **Copy standard (D-34, D-35):** short declarative sentences in plain English; no stacked fragments in threes; no insider shorthand ("the position", "source-linked") without saying what it is; a concrete number or example wherever one exists; coral second heading lines used sparingly. "Real time" is banned: write "continuous" or "as it happens".

## Claims discipline

Every material claim is one of: **verified fact** (dated public source in `research/source-register.md`), **founder observation** (labelled on the slide), **illustrative example** (slide 7), **modelled assumption** (workbook), **demonstrated MVP capability**, **planned capability**, or **unvalidated commercial hypothesis**. The deck must not claim: paying customers; completed recovery work; independent certification of cost to complete; universal API coverage; proven accuracy or security certification; a guaranteed mandate; guaranteed recovery outcomes; countercyclical revenue. Keep `review/claims-register.md` current.

## The financial model is a controlled source

`financial-model/IRIS_model_5y.xlsx` is generated by `build_model.py` (`python3 build_model.py out.xlsx`, then recalc). Five years, three cases, three revenue lines: IRIS for Lenders, IRIS for Builders and assessments (D-37, 4 Nov 2026; the developer-direct line was removed on 26 Nov 2026 by owner decision D-48, and there is no developer product: the developer pays the facility fee and reads the mandated view). The average facility is one figure for the market and the lender line, the average build contract times the debt multiple, flexed by case (owner direction D-49, 26 Nov 2026): $48M base ($40M × 1.2), $73M upside ($61M × 1.2), $40M conservative ($40M × 1.0, senior debt alone). The deck's figures come from its base case: revenue $0.18M / $1.7M / $6.1M / $14.5M / $25.8M; EBITDA −$0.48M / −$0.82M / −$0.50M / $1.3M / $4.2M; run rate $31.3M at month 60; lenders 1 / 3 / 8 / 14 / 20 with 1 / 30 / 109 / 229 / 373 facilities of $48M at 15 bps ($72K a year each); builders 3 / 4 / 6 / 11 / 17 carrying 12 / 22 / 34 / 58 / 92 jobs; team 2 / 18 / 36 / 69 / 102; cash positive throughout with the $3M seed at month 15; market $291M Australia / $55M Queensland. The workbook and the competitor table are formatted as plain Excel at the owner's direction (D-48: Calibri 11, black text, bold headings, thin rules, no fills or coloured fonts); keep that look. Builders are the wedge; each lender brings its book, which is what bends the curve. Assessments are priced at $35K, benchmarked to QS report fees. The lender cadence is a company target and is labelled so. Do not change an assumption without a decision in `review/review-decisions.md`; when one changes, regenerate the workbook, re-run its checks, and update slide 11 and appendix A5–A6 together.

## Roles and process

- **Claude** edits source, implements approved revisions, keeps design consistency, renders exports, records changes in `review/change-log.md`.
- **ChatGPT** is the independent investment-committee reviewer; its findings go in `review/investment-critique.md` or GitHub issues / PR comments. It does not edit slides.
- **Project owner (James Thompson)** approves every material change to proposition, valuation, raise, business model, financial assumptions or the baseline. Neither model merges its own work into `main`.

Workflow for each substantive refinement: open an issue → name the slides and the intended investment improvement → implement on `refinement/institutional-v2` → render a PDF into `deck/exports/` → record in `change-log.md` → submit for ChatGPT review → address accepted findings → owner approval → merge to `main`. `main` is the approved baseline and is never pushed to directly.

## Exports

The deck renders inside the Claude Slides artifact page; the PDF/PPTX export is produced from that page's Download menu by the project owner, or by Claude where a rendering route exists, and committed to `deck/exports/` named `IRIS-Investment-Summary-v<N>.pdf`. A source change is not complete until the export matching it is committed.

## Baseline

Branch `main`, tag `baseline-v307`: the deck as published on 29 October 2026 (artifact version 1793270675-17c7, deck v307 plus the owner's in-page edits to that point). The inventory with hashes is in `README.md`.
