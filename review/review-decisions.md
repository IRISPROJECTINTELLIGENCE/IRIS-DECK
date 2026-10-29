# Review decisions

Numbered, dated, with who decided. A decision here is the only way the thesis, terms, model assumptions or baseline change. "Owner" is the project owner, James Thompson.

| # | Date | Decision | By | Status |
|---|---|---|---|---|
| D-01 | 24 Oct 2026 | Round terms: AUD $750K pre-seed SAFE at a $7.5M valuation cap. | Owner | Approved |
| D-02 | 24 Oct 2026 | The deck pitches API connection only (an adapter per system API, a systems register per project); export, document and email fallbacks live in the build scope, not the deck. | Owner | Approved |
| D-03 | 24 Oct 2026 | The lender sees the project's delivery risk position and the builder's position on that project only; IRIS takes no view on the builder as a company. No reliance-letter mechanism; IRIS is not replacing the QS. | Owner | Approved |
| D-04 | 24 Oct 2026 | Project examples on slide 7 carry altered figures so the jobs cannot be identified; structure of each issue kept. | Owner | Approved |
| D-05 | 26 Oct 2026 | Investment-committee pass: three applications of one platform; built / in build / intended distinguished; market and model labelled as modelled; milestones framed as evidence created; claims register maintained. | Owner (brief) | Implemented v166 |
| D-06 | 29 Oct 2026 | First lender type for the design partner: a non-bank private credit fund. POC dataset: the fullest private record set (Project A on the deck), with the owner's written permission as the first gate. | Owner | Approved |
| D-07 | 29 Oct 2026 | Sequence: builder pilot deployments first to prove the position; a lender design partner alongside; monitoring at scale as a facility condition; distressed-project assessments after that at a separate fee. Supersedes the "recovery as near-term entry" wording in the 26 Oct brief and the workspace setup brief. | Owner (artifact comment) | Implemented v223 |
| D-08 | 29 Oct 2026 | Product scope: builder systems only. The lender view structures the risk those systems carry from the lender's perspective; facility, equity, presales and sunset figures are lender inputs, not ingested systems. | Owner | Approved |
| D-09 | 29 Oct 2026 | Two forecasts on one job: IRIS reports the system of record and flags the gap; it does not adjudicate. | Owner | Approved |
| D-10 | 29 Oct 2026 | Facility fee basis: 15 bps on the facility limit, floor $3,500 and cap $10,000 a month, as modelled. | Owner | Approved |
| D-11 | 29 Oct 2026 | Competition framing: no system found that replicates IRIS as of October 2026; adjacent software shown as source systems or tools IRIS sits beside; IPEX is not a partner; a partnership only with a product similar enough in logic to merge with. | Owner | Implemented v204 |
| D-12 | 29 Oct 2026 | Slide 3 stats: $3.08bn secured-lender debt and $736M of unreconciled inter-company balances (administrator's figures, reported) replace the earlier set; replacement-builder premium stated as 20–40%, founder experience. | Owner (draft) / Claude (substitution) | Implemented v195 |
| D-13 | 29 Oct 2026 | Slide 5 funding row uses the Stamford Capital 2026 survey (zero-presale lenders 18% → 37%; 60–100% bracket 45% → 8%). | Owner | Implemented v294 |
| D-14 | 29 Oct 2026 | Workspace: this repository is the active development environment; `main` is the immutable baseline (tag `baseline-v307`); all work on `refinement/institutional-v2`; ChatGPT reviews, Claude edits, owner approves merges. | Owner (brief) | Pending owner approval of setup |

## Open decisions (owner's call)

| # | Question | Options on the table | Why it matters |
|---|---|---|---|
| O-01 | Builder-project ramp in the base case: 8 / 21 / 36 paid projects at year end. | Keep (per the 26 Oct brief) or move to 4 / 12 / 24 (Year 3 revenue ≈ $2.15M, run rate ≈ $3.0M, Year 2 ≈ −$390K). | The owner flagged 36 as out of reach; the brief said retain the base case. Changing it means regenerating the workbook and slides 14, 15, A4, A5. |
| O-02 | Written permission from each record-set owner to use altered figures from their files on the deck. | Obtain before circulation, or remove the example. | Slide 7 rests on three private record sets; one owner is a pilot prospect. |
| O-03 | Security certification standard named on slide 17 (month 6). | ISO 27001, SOC 2 Type 1, Essential Eight. | Investors will ask which; the $40K line must match. |
| O-04 | Founder salaries and the round/salary thread raised on the deck comments. | — | Open since 24 Oct. |
