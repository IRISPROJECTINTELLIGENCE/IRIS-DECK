"""Plain-English basis for each input on the Inputs sheet.

Each entry is (type, basis). Types:
  Reported         taken from a published source, named in the basis
  Measured         a published statistic
  Estimate         the company's estimate; the basis says how it was worked out and what would test it
  Company target   a plan the company has to achieve; not evidence
  Company decision a price, salary or funding term the company sets

The basis answers three questions in order: what the number is, where it comes from, and how it is worked
out. Where there is no outside source, it says so.
"""

IB19 = "IBISWorld report E3019, Multi-Unit Apartment and Townhouse Construction in Australia (2026)"
IB21 = "IBISWorld report E3021, Commercial and Industrial Building Construction in Australia (2026)"

BASIS = {
    # 1. Market
    "mu_med": ("Reported", f"Value of medium-rise apartment building work done in Australia in 2025-26, from {IB19}."),
    "mu_high": ("Reported", f"Value of high-rise apartment building work done in Australia in 2025-26, from {IB19}."),
    "ci_tot": ("Reported", f"Value of all commercial and industrial building work in Australia in 2026-27, from {IB21}. Only the share on jobs of $10M or more is counted (next row)."),
    "ci_big": ("Estimate", "The share of commercial and industrial work done on jobs worth $10M or more. No outside source: IBISWorld does not split work by job size. 65% is the company's estimate, on the basis that large jobs carry most of the value even though small jobs are most of the count. Test it with a job-size breakdown from a building-approvals dataset."),
    "mu_dev": ("Reported", f"The share of apartment work paid for by developers, who borrow against it, rather than by owners building for themselves. From {IB19}, major markets: developers and REITs 48.8% plus owners and small developers 39.2%."),
    "ci_dev": ("Reported", f"The share of commercial and industrial work paid for by property developers. From {IB21}, major markets: commercial developers 59.8% plus industrial developers 13.3%."),
    "q_mu": ("Reported", f"Queensland's share of apartment work done, from {IB19}, state breakdown, 2024-25."),
    "q_ci": ("Reported", f"Queensland's share of commercial and industrial businesses, from {IB21}. Used as a stand-in for its share of work done, which IBISWorld does not publish by state."),
    "build_mu": ("Measured", "How long an apartment building takes from start to finish: 9.54 quarters, about 29 months, the ABS average completion time for 2025-26 (Queensland 10.03 quarters). Work a year × build time = the value under construction at any one time."),
    "build_ci": ("Estimate", "How long a commercial job of $10M or more takes. The ABS shows $76.4bn of non-residential work still to be done in March 2026 against about $70bn done a year: about one year of work in hand, which fits jobs that take about two years from start to finish."),
    "mkt_job": ("Estimate", "The average build contract across all live jobs of $10M or more. Used only to count how many jobs are in the market: value under construction ÷ $40M. Three published figures sit around it: a listed lender's senior construction loans average about $39M (June 2026); Brisbane and Gold Coast apartment jobs on hold average about $48M (PRD, September 2026); the top 50 builders' 2025 starts averaged about $61M (Hubexo, April 2026)."),
    "fac_ratio": ("Estimate", "How big the loan is next to the build contract. Lenders fund up to about 80% of total development cost with senior and mezzanine debt (banks 60–70%, non-bank lenders 75–80%: Feasly; Vertex Capital, 2026). The build is about two-thirds of total cost. 80% ÷ two-thirds = 1.2 times the build contract. Used to turn the market's $40M average job into a $48M average facility."),
    "distress": ("Estimate", "The share of funded jobs of $10M or more that stall or default in a year. No public series exists. 4% is the company's estimate, set against construction's share of company insolvencies: 24.5% in 2025-26 (ASIC) and 37% in July–August 2026 with the Bathla group. It drives the number of assessments only."),
    # 2. Pricing
    "price_b": ("Company decision", "What a builder pays for IRIS for Builders on each live job. Set by the company. The subscription stays with the builder as it moves from one job to the next."),
    "bps": ("Company decision", "What the developer pays for IRIS for Lenders, as a share of the facility each year. 15 basis points is 0.15%: $120,000 a year on an $80M facility. Set by the company. The developer pays it as a condition of the loan, the way it pays for the lender's QS report today. For scale: non-bank senior construction facilities were priced in the high single digits to low double digits a year in 2026, with establishment and line fees of one to a few per cent of the limit (Feasly, July 2026). At 10% interest, 15 bps is about 1.5% of a year's interest on the facility. Untested with a lender: the design partner is asked what it would pay, and what comes off the rate for a facility it can see into."),
    "fee_floor": ("Company decision", "The least any facility pays: $3,500 a month, the same as a builder subscription. It applies to facilities under about $28M. There is no cap on large facilities (D-51)."),
    "fac_avg": ("Company decision", "The average size of the facilities IRIS is written into, senior debt alone or with mezzanine. Set by the owner on 26 November 2026: the lenders that adopt first write the larger mid- and high-rise jobs. This drives the lender revenue line. It is larger than the market average facility ($48M) because IRIS targets the larger end of the market. Test it against the first design-partner lender's book."),
    "mkt_fac": ("Derived", "The average facility across the whole market: the $40M market average job × 1.2. At 15 bps it pays $72,000 a year. Used only on the Market sheet."),
    "assess_fee": ("Estimate", "The fixed fee for one assessment of a troubled project's records. Benchmarked to what lenders already pay a QS: an initial financier's report on a commercial job costs $8,000–20,000 (non-bank lenders at the upper end) and full QS cost management runs 0.5–2% of build value, which is $200,000 or more on a $40M job (Pekaj Group; Feasly, 2026). $35,000 sits between the two."),
    # 3. Lenders
    "per_lender": ("Estimate", "How many new facilities each lender puts under IRIS a month once it has adopted it. 0.8 a month is about ten a year. At $80M each that is about $770M of new construction loans a year, which implies a construction book of about $1.5bn turning over on two-year terms. Large non-bank lenders write more than this; smaller funds write less. Real estate private credit in Australia is about $80bn, 31% of residential development debt, and the five largest providers hold 52% of it (CBRE, November 2026), so the first lenders to adopt are likely to be the larger ones. Test it against the design-partner lender's actual origination."),
    "book_fac": ("Estimate", "How many of a lender's existing loans come under IRIS when they are extended or refinanced. Loans already signed owe nothing new, so only loans that are re-signed are counted. Ten is about half of a 20-loan book; the rest finish before they are re-signed."),
    "book_m": ("Estimate", "The months over which those existing loans are re-signed, spread across their remaining terms."),
    "fac_term": ("Estimate", "How long a facility stays under IRIS: the life of the build. Facilities leave the count when the job finishes."),
    "lend_life": ("Estimate", "Retention: how long a lender keeps writing IRIS into new facilities once it has adopted it. 60 months means no lender stops within the five years. A facility already under the condition keeps it until the job finishes; a lender that stops adds no new ones. No lender has adopted yet, so there is no retention evidence; the Sensitivities sheet shows each lender stopping after three years. Each mature lender is about $2.2M a year of fees."),
    # 4. Builders
    "rd_start": ("Company target", "The month the R&D partner builder's first live jobs are connected."),
    "rd_n": ("Company target", "Live jobs connected through the R&D partnership. Unpaid."),
    "paid_start": ("Company target", "The month the first builders start paying: once IRIS reconciles to the builder's own cost reports."),
    "jobs_start": ("Estimate", "Live jobs a builder puts on IRIS when it signs."),
    "jobs_ramp": ("Estimate", "How fast a builder adds its other jobs: about one every two months."),
    "jobs_cap": ("Estimate", "The most jobs a builder has on IRIS at once. A South East Queensland Tier 2 builder runs about three to eight jobs of $10M or more at a time (founder observation)."),
    # 5. Assessments
    "assess_start": ("Company target", "The month assessments are first offered: once the platform is proven on live jobs."),
    "assess_off": ("Estimate", "Assessments sold on jobs that are not on IRIS, to lenders, receivers and administrators. At a 4% stall rate, about 140 funded jobs of $10M or more stall a year nationally; eight is about 6% of them. Ramps up from the start month."),
    "assess_on": ("Estimate", "The share of stalled facilities already on IRIS whose lender buys an assessment."),
    # 6. Team
    "n_found": ("Company decision", "The two directors, full-time from month 1."),
    "sal_found": ("Company decision", "Each director's salary until Year 3. Two at $100,000 plus 12% super is the $224,000 in the use of funds."),
    "oncost": ("Reported", "Superannuation guarantee: 12% of salary from 1 July 2025 (ATO)."),
    "sal_raise": ("Estimate", "Annual pay rises from Year 3."),
    "sal_found2": ("Company decision", "Each director's salary from Year 3, once the seed is in and lenders are live."),
    "an_ratio": ("Estimate", "Live jobs and facilities one deployment analyst looks after. The analyst checks each job's figures against its source records monthly. The model hires analysts automatically as the count grows. This is the largest cost driver in the model."),
    "an_sal": ("Estimate", "Deployment analyst salary, Brisbane and Gold Coast market rate, 2026."),
    "ls_ratio": ("Estimate", "Lenders one lender success manager looks after: onboarding the lender's book, credit-committee reviews, the relationship."),
    "ls_sal": ("Estimate", "Lender success manager salary, market rate, 2026."),
    "eng_base": ("Company decision", "Engineers hired from month 16, after the seed, before lenders scale."),
    "eng_ratio": ("Estimate", "One more engineer for each 1.5 lenders: each lender brings its own loan structures, reporting formats and security review."),
    "eng_sal": ("Estimate", "Engineer salary, market rate, 2026."),
    "onb_cost": ("Estimate", "One-off cost to connect a new facility: connector setup, record mapping and the first reconciliation."),
    "comm": ("Estimate", "Sales commission: 8% of each new facility's first-year fee."),
    # 7. Other costs
    "cloud_var": ("Estimate", "Cloud hosting and AI model use for each live job or facility, a month."),
    "cont_y1": ("Company decision", "The contingency line in the use of funds."),
    "cont_pct": ("Estimate", "Contingency on all costs from Year 2."),
    # 8. Funding
    "safe": ("Company decision", "This round: a $750K SAFE at a $4M valuation cap, received in month 1."),
    "seed": ("Company decision", "The next round, assumed in all three cases. Raised on a product in paid use, with or without a lender's mandate."),
    "seed_m": ("Company target", "The month the seed is received."),
    "ser_a": ("Company decision", "An optional later round to roll out lenders faster. Not needed to stay cash positive: cash is shown with and without it."),
    "ser_a_m": ("Company target", "The month the Series A would be received."),
}

# Rows of the by-year cost tables share one basis, given on the Year 1 row.
YEAR_BASIS = {
    "build_y": ("Company decision", "Year 1 is the $320,000 enterprise product build in the use of funds; later years are upkeep by contract engineers."),
    "cloud_fix": ("Estimate", "Fixed hosting, monitoring and development tools; grows with the team. The conservative case runs these overheads at half from Year 3."),
    "sec_y": ("Estimate", "An independent security audit and penetration test in Year 1, with the access review and the security questionnaire pack lenders ask for; certification to a recognised standard (ISO 27001 or SOC 2) when a lender's procurement requires it, then surveillance audits and annual penetration tests."),
    "ins_y": ("Estimate", "Professional indemnity and cyber insurance. Cover rises as lenders rely on IRIS across more facilities. Half in the conservative case from Year 3."),
    "sm_y": ("Estimate", "Events, travel, content and the lender and broker channel. Half in the conservative case from Year 3."),
    "lg_y": ("Estimate", "Reliance terms, side-deed templates, the legal opinion on the lender condition, trademarks. Half in the conservative case from Year 3."),
    "off_y": ("Estimate", "Remote in Years 1–2; a Brisbane or Gold Coast office from Year 3. Half in the conservative case from Year 3."),
}

TABLE_BASIS = {
    "lenders": "Company target. The month each lender puts its first facility under IRIS. Lender 1 is the design partner at month 12; the rest follow a live result there: 1 / 3 / 8 / 14 / 20 lenders by the end of Years 1–5. This cadence is the plan, not evidence. The lending market is concentrated (the five largest real estate private credit providers hold 52% of that market: CBRE, November 2026), so a handful of adoptions carries most of the volume. Move a month to test a slower rollout; the Sensitivities sheet shows lenders a year late and no lender at all.",
    "builders": "Company target. The month each builder starts paying. Five builders at about six jobs each by month 36; from Year 4, builders working under a lender's condition bring their other jobs, so the count rises with lenders.",
    "hires": "Company decision. Fixed roles and the month each starts. Analysts, lender success managers and engineers are not in this table: they are hired by formula as jobs and lenders grow (section 6).",
    "sal": "Estimate. Market salaries for Brisbane and the Gold Coast, 2026, in Year 1 terms; they rise with the salary-growth input from Year 3.",
}

# Use-of-funds rows (section 9) do not drive the model.
UOF_TYPE = "Company decision"
