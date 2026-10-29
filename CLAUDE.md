# CLAUDE.md — IRIS Investment Deck workspace

This repository is the self-contained development and review environment for the **IRIS Investment Summary**, the pre-seed deck for IRIS Intelligence Pty Ltd. Read this file first in every session. Nothing here depends on an earlier conversation.

## What this is

- **Company:** IRIS Intelligence Pty Ltd (ACN 700 449 618), Gold Coast, Queensland. Two founders (referred to externally as directors): James Thompson (commercial) and Gopesh Khanna (technical). Pre-revenue.
- **Product:** IRIS reads the systems a construction project already runs (Procore / Aconex, Jobpac, PayApps, ProcurePro, email and Office, share drive), by builder-authorised, read-only API connections, and reconciles them into one source-linked delivery risk position across the management domains (cost, time, scope, procurement, payment, quality, safety, compliance), with drill-down to the record and a chat that answers from the records. It writes nothing back and replaces nothing.
- **Working thesis (cover):** IRIS gives construction capital a source-linked view of project delivery risk, reconciling fragmented project records to identify emerging exposure and inform funding, intervention and recovery decisions.
- **Raise:** AUD $500K pre-seed SAFE at a $5M valuation cap (owner decision D-21, 30 October 2026; previously $750K at $7.5M). **Do not change the terms** without project-owner approval.
- **Status:** MVP (the deck says "POC") on a populated Procore sandbox, shown to one South East Queensland Tier 2 builder; live-project access being negotiated, not granted. No recovery engagement run. No lender mandate. No paying customer.

## The investment narrative (three applications of one platform)

The deck's current sequence, approved by the project owner on 29 October 2026 (see `review/review-decisions.md`, D-07):

1. **Now — builder pilot deployments** on live projects, at $3,500 a month per project, to prove the position reconciles to the builder's own cost reports. The technical and commercial proving ground.
2. **Alongside — a lender design partner** (target: a non-bank private credit fund) shaping the lender view from those pilots: what to show, how it is structured, how it bears on the facility and the lender's position.
3. **At scale — continuous lender monitoring** written into facilities as a drawdown condition, paid by the developer at 15 bps a year on the facility limit (floor $3,500, cap $10,000 a month); **distressed-project assessments** offered after that, at a separate fixed fee per engagement.

The setup brief that created this workspace described recovery and assessment as the *near-term* entry. That wording predates the 29 October decision. The deck, the review files and this file follow the later decision. Do not reorder the applications without a documented decision in `review/review-decisions.md` and project-owner approval.

## Product scope (decided)

- IRIS reads the **builder's systems only**. Facility, equity, presales and sunset figures are the lender's own inputs to its view, not systems IRIS ingests.
- When a builder's internal forecast and its developer-facing forecast differ, IRIS **reports the system of record and flags the gap**; it does not adjudicate.
- IRIS **does not** replace the QS, the site inspection, an independent cost-to-complete assessment or professional judgement; it certifies nothing and values nothing. It makes **no** builder scoring, company-wide solvency assessment or payment surveillance across a builder's book.
- Competition is framed as a bounded "no system found that does this, as of October 2026"; adjacent software is either a source system IRIS reads or a tool it sits beside. IPEX is not a partner. A partnership would only be considered with a product similar enough in logic to merge with.

## Repository layout

```
deck/source/            deck.json + slides/*.html — the editable source (Slides artifact format)
deck/source/format-reference/   the Slides format reference (SKILL.md and reference/*.md); read before editing a slide
deck/source/measure.py  line-fit measurement script (see "Editing slides")
deck/assets/            fonts/images if any are added (none at baseline; Inter is loaded from Google Fonts)
deck/exports/           PDF exports of approved versions (none committed at baseline; see "Exports")
financial-model/        build_model.py (generates the workbook) and IRIS_model_36m.xlsx (the controlled source)
research/source-register.md   every public source the deck cites, with URL and date
research/market-evidence.md   the dated market facts behind slides 3, 5 and 10
research/competitive-landscape.md   the October 2026 review of about sixty products and firms behind slides 13 and A7
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
- **Confidentiality:** no employers, prospects, customer funds, lenders or project names on the deck. The three project examples on slide 7 are real record sets with names, values, delivery models and lags altered; keep them unidentifiable. The private research notes behind them are **not** in this repository and must not be added without the project owner's written authorisation.
- Page numbers are hand-set in each slide file (`02`–`19`, `A1`–`A7`); renumber when the order changes. Every slide but the cover carries a section label (`<p data-iris-label="1" …>` at top 62px, coral caps): Problem, Evidence, Solution, Why now, Go to market, Competition, Market size, Revenue, costs and profitability, Team, The round, Close, Questions investors ask, Appendix An · name. `deck.json` carries order and section descriptions.

## Claims discipline

Every material claim is one of: **verified fact** (dated public source in `research/source-register.md`), **founder observation** (labelled on the slide), **illustrative example** (slide 7), **modelled assumption** (workbook), **demonstrated MVP capability**, **planned capability**, or **unvalidated commercial hypothesis**. The deck must not claim: paying customers; completed recovery work; independent certification of cost to complete; universal API coverage; proven accuracy or security certification; a guaranteed mandate; guaranteed recovery outcomes; countercyclical revenue. Keep `review/claims-register.md` current.

## The financial model is a controlled source

`financial-model/IRIS_model_36m.xlsx` is generated by `build_model.py` (`python3 build_model.py out.xlsx`). The deck's figures come from it: revenue $123K / $962K / $2,615K (Y1–Y3 base), costs $500K / $962K / $1,743K, month-36 run rate $3.63M, conservative $66K / $395K / $1.07M, market $244M Australia / $46M Queensland. Year 1 costs equal the $500K use of funds (founders at $100K each plus super). Do not change an assumption without a decision in `review/review-decisions.md`; when one changes, regenerate the workbook, re-run its checks, and update slides 14, 15, A4 and A5 together.

## Roles and process

- **Claude** edits source, implements approved revisions, keeps design consistency, renders exports, records changes in `review/change-log.md`.
- **ChatGPT** is the independent investment-committee reviewer; its findings go in `review/investment-critique.md` or GitHub issues / PR comments. It does not edit slides.
- **Project owner (James Thompson)** approves every material change to proposition, valuation, raise, business model, financial assumptions or the baseline. Neither model merges its own work into `main`.

Workflow for each substantive refinement: open an issue → name the slides and the intended investment improvement → implement on `refinement/institutional-v2` → render a PDF into `deck/exports/` → record in `change-log.md` → submit for ChatGPT review → address accepted findings → owner approval → merge to `main`. `main` is the approved baseline and is never pushed to directly.

## Exports

The deck renders inside the Claude Slides artifact page; the PDF/PPTX export is produced from that page's Download menu by the project owner, or by Claude where a rendering route exists, and committed to `deck/exports/` named `IRIS-Investment-Summary-v<N>.pdf`. A source change is not complete until the export matching it is committed.

## Baseline

Branch `main`, tag `baseline-v307`: the deck as published on 29 October 2026 (artifact version 1793270675-17c7, deck v307 plus the owner's in-page edits to that point). The inventory with hashes is in `README.md`.
