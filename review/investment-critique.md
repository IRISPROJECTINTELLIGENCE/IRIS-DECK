# Investment critique

Independent investment-committee review of the IRIS Investment Summary. **This file is written by the reviewer (ChatGPT), not by Claude.** Append a dated entry per review round; do not edit earlier entries. Findings may also be raised as GitHub issues or pull-request comments; record the issue number here when they are.

## How to review

Review the deck source in `deck/source/` (one `<section>` per slide, in the order given by `deck/source/deck.json`; speaker notes are in `<aside>`), the thesis in `investment-thesis.md`, the evidence classes in `claims-register.md`, the sources in `../research/`, and the model in `../financial-model/`. Judge against the standard in `CLAUDE.md` §"Institutional quality": executive clarity, economic relevance, commercial credibility, factual defensibility, investor conviction, disciplined metrics, clear differentiation, credible milestones.

For each finding give: the slide, the claim or weakness, why an investment committee would object, the evidence that would resolve it, and a severity (blocks circulation / should fix / consider). Mark each finding **Accepted**, **Rejected (reason)** or **Deferred** once the project owner has ruled; Claude implements accepted findings on `refinement/institutional-v2`.

## Questions the deck must answer (from the 26 October brief)

1. What economically significant problem exists?
2. Why does the problem persist despite existing construction software, QS services and lender controls?
3. What evidence demonstrates the problem?
4. What exactly does IRIS do that existing processes do not?
5. Why is the product valuable before distress and during a recovery?
6. Why is the current market an attractive point of entry?
7. Who has authority and budget to buy it?
8. How does the business acquire customers and generate repeatable revenue?
9. Why can IRIS defend this position against incumbents?
10. What has been built and validated already?
11. What must the founders prove with this investment?
12. Why could the resulting business justify its valuation and future funding?

## Known weak points carried into the baseline (for the reviewer's attention)

- Builder access to a live project is "being negotiated", not granted (slide 2); the whole proving-ground workstream rests on it.
- No accuracy figure exists; the accuracy test on three historic record sets is a month-4 milestone.
- No lender has agreed to anything; the design partner is a target type (non-bank private credit fund), not a named counterparty.
- The "no system found that does this" claim (slide 13) is bounded to the founders' October 2026 search.
- The base-case ramp (8 / 21 / 36 paid builder projects) is under review by the owner (decision O-01).
- The three project examples (slide 7) are real but altered; permission from each record-set owner is outstanding (O-02).
- Security certification standard and PI premium are not yet specified (O-03).

## Review log

### Round 1 · 29 October 2026 · GitHub issue #1

Claude's self-assessment (O1 three-party adoption; O2 nothing demonstrated on live data; O3 execution capacity against incumbents; edits E1–E10) and ChatGPT's point-by-point response are on issue #1. The reviewer agreed with O1–O3, accepted E1–E10 with modifications, and added F1–F5. Dispositions below are Claude's; the owner rules on the items marked owner decision.

| Finding | Slide(s) | Severity (reviewer) | Disposition | Where |
|---|---|---|---|---|
| E1 three-party mechanics; separate payer, decision-maker, data controller; qualify slide 12's carve-out and network-effect claims; do not present the side-deed route as established | 11, 12, 19 | Blocks conviction | Accepted; implemented v320/v343. The side-deed route stays "to be confirmed with lawyers". | PR #2 |
| E2 artefact per milestone; dates as targets | 17 | Should fix | Accepted; implemented v321. | PR #2 |
| E3 diligence route for slide 7 | 7 | Blocks circulation beyond outreach | Deferred: owner decisions O-02 and O-10. | — |
| E4 accuracy protocol; test findings and coverage, not numeric matching alone | 8, A3 | Should fix | Accepted with the reviewer's stronger design: parity and completeness on the slide, earlier-detection evidence as the list of findings the cost report did not yet carry (notes). Tolerance and sign-off: O-05. | PR #2 |
| E5 meet Procore's owner tools; avoid absolute "none reconciles" | 13, 19, A3 | Should fix | Accepted; implemented v343. | PR #2 |
| E6 engineering capacity, certification standard | 17, A5 | Should fix | Owner decision O-03 / O-08. | — |
| E7 bound the Bathla example; exposure not loss; causal overstatement on slide 3; premium as founder observation | 3, 10 | Fix before circulation | Accepted; implemented v319/v324. The owner removed the bound from slide 10 in-page; slide 3 carries it. | PR #2 |
| E8 TAM as price-based potential under assumed adoption | 14, A4 | Should fix | Accepted; implemented v343. Penetration and overlap assumptions are on A4 and the workbook; no new slide. | PR #2 |
| E9 valuation logic | 15/17 | Gap | Owner decision O-07; the reviewer's framing (proof points that de-risk the next round, no multiple) adopted as the recommendation. | — |
| E10 "filtered to look good" | 6 | Consider | Owner decision O-06; the phrase is the owner's. | — |
| F1 run-rate arithmetic with rounded counts | 15 | Consistency | Accepted; implemented v343 ("counts rounded"; workbook figures in notes). | PR #2 |
| F2 stale CPI reference | 10 | Fix before circulation | Accepted; implemented v319 with the ABS 28 Oct release. | PR #2 |
| F3 trust and governance of conflicting records (annotation, versioning, stale feeds, what lender assurance means if inputs are permissioned away) | 8, 12, 19 | Product design | Pushback in part: D-09 already fixes the rule for two forecasts (report the system of record, flag the gap), and the lender sees whether the job is forecast to lose money, not the builder's rates. The mechanism for annotations, versioning and stale feeds is a product-design question for the owner and CTO, not deck copy; proposed as a one-row addition to A3 once decided. | Owner |
| F4 slide 3 conflates risks | 3 | Fix before circulation | Accepted; implemented v324 (exposure; decisions rest on the position; bound). | PR #2 |
| F5 facility-fee line is a scenario, not a probability-weighted forecast | 15, A5 | Label | Accepted in the notes (v343); the slide already states the dependencies. No assumption changed (O-01 open). | PR #2 |
| Strategic: builder line is a potential revenue stream, not an established business | 11, 15, 19 | — | Agreed; the deck says "a revenue line of its own" and "the conservative case", not "established". | — |
| Strategic: a single end-to-end product proof on slide 8 (records → reconciliation → finding → decision → check) | 8 | — | Agreed in principle; slide 8's chain is systems → IRIS → position/exposure/gaps with the protocol stated. A worked example would need a record set the owner can show (O-02). | Owner |


