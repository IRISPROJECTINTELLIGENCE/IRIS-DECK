# IRIS competitive landscape, current to 30 October 2026

Purpose: test the deck's bounded claim — "as of October 2026 we found no product that reconciles a project's systems into one position for builder, developer and lender, or that a lender writes into its facility" — against every product or firm an investor could name. Written 30 Oct 2026 from fresh web searches plus the four files in `/home/claude/research_notes/IRIS competitive landscape/` (dated 24 Oct 2026, cited below as "prior notes").

**Labels**
- **[F]** fact from a primary source (company release, filing, regulator) or reputable trade press, dated.
- **[V]** vendor claim: marketing, sponsored content, founder statements. Not independently checked.
- **[I]** my inference.
- **[U]** not verified in this session; background knowledge or a prior-notes item I did not re-fetch.

**Position labels** (one per entry): "source system IRIS reads", "sits beside IRIS", "adjacent AI tool (builder-side)", "adjacent AI tool (lender-side)", "lender draw tool (US)", "service incumbent / channel", "credit data", "closest to a competitor".

**Threat flags** per entry: **(a)** reconciles across multiple source systems; **(b)** serves the lender with a project-level position; **(c)** is written into facility documents. "No" means no evidence found; it is not proof of absence.

**Research limits.** Primary sites blocked by the fetch allowlist this session: ipex.com.au, pitchbook.com, dealroom.co (news). IPEX facts therefore come from sponsored articles, a podcast page and a PDF of its own material. Pages not re-fetched today are marked [U] with the prior-notes reference. No private sources (lender facility agreements, QS engagement letters) were available; (c) is tested only on public statements.

---

## 1. Builder project-management platforms

### 1.1 Procore (NYSE: PCOR), including Datagrid, Helix, owner suite
- **What it does.** Construction management platform (project management, financials, quality/safety, field) sold mainly to general contractors; owner and specialty-contractor editions.
- **Who pays / serves.** The builder (fixed annual fee on construction volume) [F, prior notes, FY2025 10-K]; owners buy separately.
- **Records layer.** Its own system. Datagrid adds cross-system agents: "third-party data sources, including ERPs and cloud storage tools"; connectors named for Autodesk Construction Cloud, Trimble, Hilti, Fieldwire, Sage [F, Pulse 2.0, 22 Jan 2026; Verdantix, 3 Feb 2026]. Q2 2026 release: "a connected Common Data Environment launched to unify and verify project data" [F, Business Wire, 29 Jul 2026].
- **Lender / facility.** None found. The owner suite (17 Jun 2026) has "Funding Source Management" that "tracks where project money comes from and how it's spent" and "Portfolio Monitoring" where "Procore AI can surface emerging financial, schedule, and operational risks across portfolios"; it does not mention lenders or financiers; Capital Planning and Funding Source Management GA "late 2026" [F, Business Wire, 17 Jun 2026]. Procore Pay (US) is a payment rail between GC and subs, not a lender product [U, support pages exist].
- **Australia.** Regional office in Australia; 15% of 2025 revenue outside the US [F, prior notes, 10-K].
- **Funding / 2025–26 moves.** Datagrid acquired, closed 16 Jan 2026 per Procore 10-Q ($168.0M cash) [F, prior notes]; Verdantix gives 20 Jan [F]. Datagrid agents embedded in Procore May 2026; "Digital Coworker" tiers Starter/Pro/Enterprise Jul 2026 [F, Construction Owners, Oct 2026]. DroneDeploy agreement ~ $845M, 29 Jul 2026 [F, prior notes]. Q2 2026 revenue $375M (+16%), RPO $1.67B; FY2026 guide $1,510–1,514M [F, Business Wire, 29 Jul 2026]. Groundbreak 2026 (20–22 Oct 2026, Orlando): agents that "flag contract risk"; the owner-side question raised publicly was "Can agents act on data in non-Procore systems?" [F, Construction Owners, Oct 2026]. October 2026 releases: NVIDIA digital-twin collaboration, Procore AI Go, IBM Maximo collaboration for owners [F, listed on the Q2 page].
- **Position:** source system IRIS reads.
- **Flags:** (a) **yes, partly** — Datagrid agents read across ERP and document stores for the builder; (b) no; (c) no.
- **Scepticism.** Procore now owns a cross-system agent layer and sells it to non-Procore customers. It has not shown a lender view, and its paying customer is the builder. The owner suite's "risk across portfolios" is owner-side, within Procore data. [I]
- Sources: https://pulse2.com/procore-acquires-datagrid-to-expand-agentic-ai-and-connect-construction-data-across-platforms (22 Jan 2026); https://research.verdantix.com/insights/blog/construction-software-consolidation-heats-up-in-2026--procore-acquires-datagrid-as-hexagon-launches-multivista (3 Feb 2026); https://www.businesswire.com/news/home/20260617320347/en/ (17 Jun 2026); https://www.businesswire.com/news/home/20260729106137/en/ (29 Jul 2026); https://www.businesswire.com/news/home/20251015796723/en/ (15 Oct 2025); https://www.constructionowners.com/news/whats-new-at-groundbreak-2026-ai-agents-the-bash-and-an-awards-preview (Oct 2026).

### 1.2 Oracle Aconex (and Oracle Construction & Engineering)
- **What it does.** Document control, correspondence and workflow CDE; widely the developer-controlled correspondence system on Australian jobs [U, market practice].
- **Who pays.** The party that sets up the project (often developer or head contractor); per-project licensing.
- **Records layer.** Its own system. Oracle C&E Intelligence ingests Aconex, Unifier and P6 for cost and schedule analytics (vendor material marked "not a commitment to deliver") [V, prior notes].
- **Lender / facility.** None found.
- **Australia.** Melbourne-founded; Oracle bought Aconex for about US$1.2B (closed 2018) [F, Converge Digest headline; U for close date].
- **2025–26 moves.** 13 Apr 2026 release: enhanced document processes and structured ITP test plans; no AI named [F, Quantisnow summary of Oracle release]. Oracle AI safety advisor tool (2025–26) [U, headline only].
- **Position:** source system IRIS reads.
- **Flags:** (a) no (own data; Oracle analytics stays inside the Oracle family); (b) no; (c) no.
- Sources: https://quantisnow.com/insight/new-oracle-aconex-capabilities-improve-project-transparency-and-control-6497178 (13 Apr 2026); https://convergedigest.com/oracle-acquires-aconex-for-12b-cloud/ [U].

### 1.3 Autodesk Construction Cloud / Forma (incl. Autodesk Assistant)
- **What it does.** Build, Cost Management, Docs, BIM; Payapps now inside it (see 3.1). Prior notes record a 2026 rename of ACC to Autodesk Forma [U, prior notes].
- **Who pays.** Builders, designers, owners.
- **Records layer.** Own system. At AU 2026 (week of 29 Sep 2026) Autodesk previewed a next-generation agentic Assistant across Forma/Fusion/Flow, with "Assistant Builder" for customers' own agents; GA, pricing and regions "to be announced in 2027"; no ACC or ERP integration named; no owner or lender angle [F, iTWire, 29 Sep 2026].
- **Lender / facility.** None found.
- **Australia.** Yes (Payapps is Melbourne-based).
- **Position:** source system IRIS reads.
- **Flags:** (a) within Autodesk only; (b) no; (c) no.
- Source: https://itwire.com/business-it-news/data/autodesks-real-bet-at-au-2026-isnt-a-product-its-an-assistant-that-knows-the-project (29 Sep 2026).

### 1.4 Trimble Viewpoint (Vista, Spectrum, Jobpac, ProjectSight, Trimble Construction One)
- **What it does.** Construction ERP and project management; Jobpac is the ANZ builder ERP (see 2.1).
- **2025–26 moves.** Trimble Agent Studio announced at Dimensions, 10 Nov 2025 (pilot); "Viewpoint Finance Assistant" expected in Labs early 2026; CEO on "breaking down data silos" [F, Investing.com, 10 Nov 2025]. Trimble bought **Document Crunch**, closed 4 Apr 2026, $246.4M, with the contract "rule set" to become the "intelligent DNA" of TC1 and push obligations into ERP [F, prior notes citing Trimble 10-Q and Construction Dive, 6 Apr 2026]. Briq's Otto AI (16 Dec 2025) runs "continuous reconciliation between field activity and financials" across Viewpoint/Spectrum/Tekla [V, Access Newswire].
- **Lender / facility.** None found.
- **Australia.** Jobpac is used by Australian Tier 1 and 2 builders [U, prior notes].
- **Position:** source system IRIS reads.
- **Flags:** (a) **emerging** — Document Crunch obligations plus Jobpac cost inside one vendor would be a builder-side commercial-risk product; (b) no; (c) no.
- Sources: https://ng.investing.com/news/company-news/trimble-unveils-agentic-ai-platform-at-annual-user-conference-93CH-2199436 (10 Nov 2025); https://www.accessnewswire.com/newsroom/en/computers-technology-and-internet/briqs-otto-ai-extends-autonomous-workflows-across-the-trimble-eco-1117862 (16 Dec 2025).

### 1.5 CMiC
- Construction ERP (Toronto); launched "NEXUS", an AI-enabled ERP, 2025–26 [F, headline only, ForConstructionPros]. Builder-side own system. Small Australian footprint [U]. **Position:** sits beside IRIS (an ERP IRIS could read if a builder used it). Flags: none.
- Source: https://www.forconstructionpros.com/construction-technology/product/22953722/cmic-cmic-launches-nexus-an-aipowered-erp-platform-for-the-construction-industry [headline].

### 1.6 Buildertrend
- US residential builder and remodeler software; no commercial-lender product; limited Australian relevance [U]. **Position:** sits beside IRIS. Flags: none.

### 1.7 Fieldwire (Hilti)
- Field task and plan management; a Datagrid connector exists [F, Verdantix]. Builder-side own data. **Position:** source system IRIS reads (field layer). Flags: none.

---

## 2. Builder ERP and cost systems in Australia

### 2.1 Jobpac Connect (Trimble, via Viewpoint)
- Job cost, forecasting, cash flow, variations, procurement, AP/AR, payroll; ANZ builder ERP; listed "from A$249" on a comparison site [3P, prior notes]. Viewpoint bought Jobpac Apr 2015; Trimble bought Viewpoint Jul 2018 [F, prior notes]. No Jobpac-specific AI found; Viewpoint Finance Assistant for Vista in Labs 2026 [F, see 1.4]. Earlytrade and Lentune both integrate with Jobpac [F, 3.4, 3.5]. **Position:** source system IRIS reads. Flags: none.

### 2.2 Cheops (CSSP, JDM Technology Group)
- Australian construction ERP for mid-to-large builders; ProcurePro and Plexa list Cheops finance links [F, 5.x; V]. **Position:** source system IRIS reads. Flags: none. [U for 2025–26 product moves.]

### 2.3 Workbench (NZ)
- Job-costing ERP for ANZ contractors; listed on Preqin as Workbench International Ltd [U]. **Position:** sits beside IRIS / possible source. Flags: none.

### 2.4 Premier Construction Software (Constellation Software subsidiary)
- Construction ERP with a QBCC-certified trust-accounting add-on: "first software awarded QBCC certification", listed on the QBCC public registry, 15 May 2025. Queensland rule cited: government projects over $1M and private over $10M must use compliant software [F, AAP/PR Newswire, 15 May 2025]. ANZ office; CEO ANZ Michael Jantke. **Position:** sits beside IRIS (trust-account compliance is a builder-side control; also a potential source). Flags: none.
- Source: https://aap.com.au/aapreleases/cision20250514ae88115 (15 May 2025).

### 2.5 Xero / MYOB add-ons: Buildxact, Simpro, Lentune
- **Buildxact** (Melbourne): estimating and job management for residential builders; Series A A$18.5M [F, Business News Australia, undated in result]. Below IRIS's $20M+ commercial target. **Position:** sits beside IRIS.
- **Simpro** (Brisbane): trade-services job management; Lentune syncs with it [F]. **Position:** sits beside IRIS.
- **Lentune** (Christchurch/Melbourne): "sits between your email inbox and your accounting system"; invoice automation, POs, progress claims, cost-to-complete reporting; integrations Xero, MYOB (CSV), Procore, Jobpac Connect, CostCon, Simpro; targets $5M–$100M builders; ISO 27001; vendor metrics 7.8M invoices, $14B costs, 8,500+ users [V, lentune.com/en-au]. **Position:** sits beside IRIS (builder-side cost control; a possible source). Flags: (a) partial — it pulls invoices into a cost view for the builder; (b) no; (c) no.
- Source: https://www.lentune.com/en-au/ (fetched 30 Oct 2026).

### 2.6 Deep Space (Brisbane), Plexa (Australia), Databuild, EstimateOne
- **Deep Space**: all-in-one builder platform for mid-sized ANZ builders, KAI assistant; seed from VentureOn Partners Mar 2024; Pro plan A$2,495/month [aggregator, prior notes]. **Position:** sits beside IRIS.
- **Plexa** (Plexa Pro Pty Ltd, AWS Sydney, ISO 27001/SOC 2 badges): "AI construction operating system" with document, procurement, HSEQ and finance modules, an AI agent and a live MCP connector; serves builders, developers and clients; lenders not mentioned; its tools page names no integrations, though its own blog claims Jobpac and Cheops finance links [V, plexapro.com/tools fetched 30 Oct 2026; prior notes]. **Position:** adjacent AI tool (builder-side). Flags: (a) within its own data model; (b) no; (c) no.
- **Databuild** (ITW) and **EstimateOne**: builder-side; covered in prior notes; no change. **Position:** sits beside IRIS.

---

## 3. Trade payment, claims and compliance

### 3.1 Payapps (Autodesk), formerly Progressclaim.com; GCPay (North America)
- **What it does.** Progress-claim submission, assessment and approval between head contractors and subcontractors, with variations, retentions and compliance documents; "Early Payment" lets subs request earlier payment on approved claims [F, PR Newswire via AAP, 31 Aug 2026].
- **Who pays.** Head contractors (subs often free) [U].
- **Records layer.** Own claims data; "integrates with construction ERP, project management, and financial management systems" [V].
- **Scale.** 57,000+ users; AUD $35B+ claims a year; 34 of Australia's top 50 builders [V, 31 Aug 2026]. Autodesk agreed to buy Payapps 24 Jan 2024; Payapps (ANZ/UK/Ireland) and GCPay (North America) had processed close to $50B by 2023 [F/V, Autodesk blog, updated 10 Jun 2025].
- **Lender / facility.** None found. No "builder risk" product for developers or lenders found [U: searched, not found].
- **Position:** source system IRIS reads.
- **Flags:** (a) no; (b) no; (c) no.
- Sources: https://www.aap.com.au/aapreleases/cision20260831ae36713/ (31 Aug 2026); https://www.autodesk.com/blogs/construction/transforming-construction-payments-autodesks-strategic-move-with-payapps-acquisition/ (1 Feb 2024, upd. 10 Jun 2025).

### 3.2 IPEX (Industry Payment Exchange), Melbourne
- **What it does.** Software on a project bank account. Each certified progress payment lands in the builder's IPEX account; the builder draws prelims, margin and direct costs; the balance can only go to KYC/AML-checked subcontractors, suppliers and consultants linked to that project; bank details are matched to the builder's payment file. Developers and lenders see who was paid, when and how much (as % of subcontract value by default), before approving the next claim [V, IPEX summary PDF via Charter Keck Cramer, Nov 2025; Property Council sponsored, 9 Oct 2024]. "IPEX Monitor" (14 Mar 2025) removes builder withdrawal limits but keeps payment transparency [V, TUD sponsored]. "Payment verification": "certified progress is reconciled against live payment data" at each drawdown as a "simple monthly control"; "if the payment position falls outside tolerance, the lender can stop or condition further funding"; IPEX can be engaged mid-project on a distressed job [V, TUD sponsored, 20 Oct 2026]. "Cash to Complete" vs "Cost to Complete" framing [V, TUD sponsored, 24 Mar 2026, prior notes].
- **Who pays.** Not disclosed in any source found [U].
- **Records layer.** Bank-account transactions, builder payment files, QS certified amounts, payee KYC. **Not** the builder's project or cost systems (Procore, Jobpac etc.). Builders "submit a payment file" [V, Property Council, 9 Oct 2024].
- **Lender / facility.** IPEX CEO Paul Reid: "we are now starting to see lenders actually mandate the controls as a condition of lending into certain jobs"; also used as a tender requirement [V, Charter Keck Cramer podcast page, 10 Nov 2025]. Earlier: "developers and lenders can require IPEX use as a condition of winning the contract" [V, TUD, 3 Feb 2023]; controls "typically written into the head contract" [V, TUD, 5 Aug 2024]. The 20 Oct 2026 article contains no facility-condition wording and names no lender. **I found no lender or borrower source confirming a facility condition.**
- **Clients named (by IPEX).** Goodman Group, WINIM, Fortis, Trilogy Funds, MaxCap, INGWE Capital, Kervale [V, Nov 2025; Aug 2026]. Trilogy Funds and MaxCap are non-bank lenders. "80 commercial builders operating IPEX projects"; contract values $5M–$250M [V, TUD sponsored, 7 Aug 2026].
- **Scale.** >$600M under management (Sep 2023); >$1B committed (Mar 2025); >$1.5B deployed (Nov 2025) [V].
- **Australia.** Yes; Melbourne; national.
- **Funding / ownership.** Founders Chris Strode and Jake Porteous [F, Building Connection, 18 Sep 2023]; CEO Paul Reid (ex-BCI Media) [F]. No funding round, valuation or acquirer found [U]. No AI claims found.
- **Position:** **closest to a competitor** (for lender attention and the mandate idea).
- **Flags:** (a) **no** — it reconciles two things (QS certified progress vs its own payment ledger), not the builder's systems; (b) **yes** — a project-level payment position for the lender at each drawdown; (c) **claimed by the vendor** (CEO statement, Nov 2025), unverified from any lender.
- **Scepticism.** All IPEX material is sponsored or self-published. The lender-mandate claim is a CEO podcast remark. Its control is money movement, not record reconciliation; it does not see internal cost, trade commitments against allowances, unsubmitted variations, notices or time bars. It is also the product most likely to be named by an Australian non-bank lender as "what we already use." [I]
- Sources: https://charterkc.com.au/?p=17846 (10 Nov 2025); https://charterkc.com.au/wp-content/uploads/2025/11/2511_IPEX-Summary.pdf (Nov 2025); https://www.theurbandeveloper.com/articles/ipex-construction-lending-governance-payment-verification-bathla (20 Oct 2026); https://www.theurbandeveloper.com/articles/builders-are-not-scared-of-payment-verification-ipex (7 Aug 2026); https://www.theurbandeveloper.com/articles/ipex-launches-builder-friendly-version-of-payment-platform (14 Mar 2025); https://www.theurbandeveloper.com/articles/reducing-lender-risk-on-developer-builder-projects (18 Sep 2024); https://www.theurbandeveloper.com/articles/builder-due-diligence-ends-just-as-delivery-risk-begins (5 Aug 2024); https://www.propertycouncil.com.au/?p=408733 (9 Oct 2024); https://theurbandeveloper.com/articles/you-can-t-insure-against-builder-insolvency-but-there-is-another-way-to-protect-your-project (3 Feb 2023); https://buildingconnection.com.au/2023/09/18/ipex-set-sights-on-safeguarding-construction-against-insolvency/ (18 Sep 2023).

### 3.3 Earlytrade (Sydney)
- Working-capital fintech: early-payment and progress-claim platforms funded by the head contractor's own capital; integrates with Trimble Jobpac and Vista and other ERPs; AU, NZ, US, UK. BuildingPoint (Trimble's ANZ distributor) made Earlytrade its preferred progress-claims and early-payment partner from Jan 2026 (announced 24 Feb 2026). CEO Guy Saxelby. No developer or lender product [F/V, FNArena/PR Newswire, 24 Feb 2026]. A US$14.2M raise appears in search headlines [U, PropTechBuzz headline]. **Position:** sits beside IRIS. Flags: none.
- Source: https://fnarena.com/index.php/2026/02/24/earlytrade-and-buildingpoint-announce-strategic-anz-partnership (24 Feb 2026).

### 3.4 Lentune — see 2.5.

### 3.5 Oracle Textura Payment Management
- Subcontractor payment and lien-waiver management (US-centred); Australasia help docs exist, so an ANZ configuration is offered [F, Oracle docs]. Oracle acquired Textura 2016 [U]. **Position:** sits beside IRIS. Flags: none.

### 3.6 GCPay — see 3.1 (Autodesk, North America).

### 3.7 Queensland project trust accounts (BIF Act)
- A statutory control: builders must hold project funds in a project trust account on in-scope contracts, with retention trust accounts; compliant software is required above thresholds (Premier is first certified, 15 May 2025) [F, 2.4]. TUD/IPEX notes a QBCC limit on developer control of a project trust account [V, 5 Aug 2024]. **Position:** sits beside IRIS (a regulatory data layer, not a product). Flags: none. [U for 2026 amendments.]

---

## 4. Lender-side construction loan, draw management and project monitoring

### 4.1 Built Technologies (Nashville)
- **What it does.** Construction loan administration: draws, inspections, lien waivers, disbursement, covenant alerts, budget variances, portfolio reporting; borrower and builder portals; "Draw Agent" (4 Nov 2025) in Audit/Assist/Automate modes [F, Business Wire, 4 Nov 2025; getbuilt.com lender page].
- **Who pays.** The lender (volume-based); owners/GCs free to send payments, paid tier for lien waivers [F/V, prior notes].
- **Records layer.** Submitted draw packages plus integrations: "Sage, Yardi, and Procore"; nCino, Salesforce, core banking [V, lender page]. Built–Procore app: syncs projects, vendors, commitments, prime contracts, requisitions/pay apps, direct costs, lien waivers, invoice/payment/compliance data; owners "use Built's draw management tools to submit draw requests to lenders" [V, Built blog, 4 Jun 2026]. Tracks GC financial health via Experian BusinessIQ [V]. "The financial execution layer between Procore and the ERP" [V].
- **Lender / facility.** Lenders "adopted Built ... to power their draw process" and builders submit draws through it (WaFd Bank builder guide) [F, bank document]; US Bank uses Built for consumer construction mortgages [F, Business Wire, 31 Mar 2026, headline]. No loan-agreement wording found; it is operationally required by the lender rather than a facility covenant [I].
- **Scale.** "Over 300 lenders and more than $317B on the platform"; "17 of the top 25 lenders" [V, lender page]; prior notes: 355 lenders, $392B+ (site, Oct 2026) [V]; $1.5B valuation Feb 2022 [F].
- **Australia.** None found [U: searched, nothing].
- **Position:** lender draw tool (US).
- **Flags:** (a) **partly** — syncs Procore and Sage/Yardi financials, but the lender review is of the submitted draw; (b) **yes** — a lender's project-level draw and variance position; (c) operationally required by lenders; no facility wording found.
- **Scepticism.** Structurally the closest US analogue to IRIS's lender application: a lender-paid platform that reads Procore financials. It stops at the head-contract draw and lien-waiver layer and has no ANZ presence. If Built entered Australia it would be the most credible incumbent threat on the lender side. [I]
- Sources: https://www.businesswire.com/news/home/20251104739836/en (4 Nov 2025); https://getbuilt.com/solutions-for-lenders/ (fetched 30 Oct 2026); https://getbuilt.com/blog/procore-app-marketplace/ (4 Jun 2026); https://www.wafdbank.com/documents/wafd-bank-builder-welcome-guide.pdf (undated bank guide).

### 4.2 Rabbet (Austin)
- Two separate products that do not share data: Rabbet Construction Lending (draw management with "automated covenant checks", inspection workflows, budget monitoring, core-bank API; per-draw pricing) and Rabbet Development (owner budgets, anticipated final cost, draw packages; Yardi, QuickBooks, AvidXchange, Bill.com, Nexus, MRI; from $15,000/yr). "$160B in assets under management"; CEO Will Mitchell; Procore not mentioned; no AI features listed; US customers only; page updated Aug 2026 [V, rabbet.com]. Central Inbox launched Dec 2025 [F, headline]. **Position:** lender draw tool (US). Flags: (a) no; (b) yes (loan budget level); (c) no evidence. No Australian presence [U].
- Source: https://rabbet.com/what-is-rabbet-software (fetched 30 Oct 2026).

### 4.3 Land Gorilla (California)
- Construction loan management "since 2010": draws, inspections (incl. remote video), lien waivers, servicing; eight AI "Draw Agents", an Assistant, document processing, risk scoring, lien monitoring; **X-RAY** (16 Jun 2026): AI due diligence on "project feasibility, budget accuracy, contractual risk, and builder reliability", with replacement-contractor analysis; residential 1–4 unit now, commercial/multifamily "coming months" [F/V, landgorilla.com; WRE News, 16 Jun 2026]. US only (50-state compliance library). **Position:** lender draw tool (US). Flags: (a) no; (b) yes (draw level, with builder reliability scoring); (c) no evidence.
- Sources: https://landgorilla.com/ (fetched 30 Oct 2026); https://wrenews.com/?p=91521 (16 Jun 2026).

### 4.4 nCino, Abrigo, Bluebeam
- **nCino**: bank operating system; Built integration since 2020; nCino rolled its mortgage system into Australia [F, National Mortgage News, 29 Oct 2020]. Not a construction monitoring tool. **Position:** sits beside IRIS.
- **Abrigo** (ex-Sageworks): US bank software with a construction-lending module [F, URL only]. **Position:** lender draw tool (US).
- **Bluebeam** (Nemetschek): PDF markup; Nemetschek invested in Document Crunch (Nov 2024) [F, prior notes]. **Position:** sits beside IRIS.

### 4.5 Northspyre (Atlanta)
- Owner/developer "end-to-end real estate development management platform"; Complex Capital Management add-on splits funding across lenders and equity partners per line item (fall 2025); Portfolio Analytics Plus; imports journals from Yardi, MRI, Sage Intacct, Sage 300, RealPage, Acumatica, QuickBooks; bi-directional Acumatica and JD Edwards; "$200B+ supported projects"; Series B $25M (Feb 2022) [F, Business Wire, 8 Jan 2026]. No lender portal or draw product named. US. **Position:** sits beside IRIS (owner-side). Flags: (a) across the owner's accounting systems only; (b) no; (c) no.
- Source: https://www.businesswire.com/news/home/20260108193626/en (8 Jan 2026).

### 4.6 Brdg (Canada)
- Draw-readiness agents for developers, lenders and cost consultants; C$850K pre-seed Aug 2026 [F, prior notes]. **Position:** adjacent AI tool (lender-side). Flags: (b) partial; (a) no; (c) no.

### 4.7 Australian lenders' own tools
- **Australian First Mortgage** built an in-house construction-tracking website (24 Oct 2016): loan settlement, builder details, stage photos, invoices and payments, logins for builders, brokers, borrowers [F, The Adviser]. Historic; shows lenders build internal trackers rather than buy [I].
- **Assetline Capital** (sponsored, 12 Feb 2026): in-house construction team plus QS to assess claims, review contracts and measure builder cash flow; no software named [V, TUD].
- **Not found:** any Australian bank or non-bank publicly using Built, Rabbet or Land Gorilla, or any Australian-built lender draw platform other than IPEX's payment layer. Searches: "construction loan drawdown management software Australia", "MaxCap OR Qualitas OR Wingate OR Pallas ... monitoring technology platform" (returned only US vendors). [U: absence of evidence.]
- Sources: https://www.theadviser.com.au/lender/35278-non-bank-lender-launches-site-to-track-construction-projects (24 Oct 2016); https://www.theurbandeveloper.com/articles/assetline-capital-construction-expertise-non-bank-development-finance (12 Feb 2026).

---

## 5. Owner / developer project controls

### 5.1 Mastt (Sydney)
- Capital project and portfolio controls for owners and their PM consultants: budget ledgers, commitments, pay apps, change orders, schedule, risk, documents; "Mastt Agent" marketed in Oct 2026 as a "Digital Project Manager" (RFIs, EOT notice example, monthly report); first project free; Professional "averages $165 per project per month" [V, prior notes, mastt.com]. Seed $2.2M Dec 2020; Series A $9.5M led by OIF Ventures with Gravel Road Ventures (Aconex founders), Feb 2022; customers Jacobs, Aurecon, AECOM, WSP, Australian governments [F, Mastt blog, 11 Feb 2022]. No later round found [U]. No integration with builder systems claimed; no lender features [V/U]. **Position:** sits beside IRIS (the nearest Australian owner-side analogue). Flags: (a) no; (b) no; (c) no.
- Source: https://www.mastt.com/blogs/mastt-raises-9-5-million-in-series-a-funding (11 Feb 2022, upd. Dec 2024).

### 5.2 Kahua (Atlanta)
- "AI enterprise construction platform for complex capital programs" for public and institutional owners; 2,500+ customers, $400B+ program value; Bain Capital Tech Opportunities investment reported at $250M (Bloomberg) at >$1B valuation, ~$100M ARR, 1 Oct 2026; AI capabilities are funded plans; no lender mention [F/V, MarketScale, 1 Oct 2026]. Kahua AI assistant launched May 2026 [F, headline]. **Position:** sits beside IRIS. Flags: none.
- Source: https://www.marketscale.com/industries/engineering-and-construction/bain-capitals-reported-250m-minority-investment-values-construction-platform-kahua-above-1b (1 Oct 2026).

### 5.3 InEight (Kiewit-owned), Oracle Primavera, Asite
- InEight: owner/contractor project controls, some Australian infrastructure use [U, prior notes]. Primavera P6: scheduling (Oracle). Asite: UK CDE. None serves lenders. **Position:** sits beside IRIS. Flags: none.

### 5.4 Aphex (London)
- Daily site execution (lookaheads, weekly work plans); contractors incl. Balfour Beatty, Skanska, Mace; used in Australia/NZ (Acciona LXRP); Expedition Growth Capital investment; Toronto office 28 Jul 2026; no risk or finance features [F, GlobeNewswire, 28 Jul 2026]. **Position:** sits beside IRIS. Flags: none.
- Source: https://www.globenewswire.com/news-release/2026/07/28/3334415/0/en/daily-site-execution-platform-aphex-launches-in-north-america.html.

### 5.5 INGENIOUS.BUILD (Nashville)
- Owner-side system of record; AI claims to read "the live contract, the current master budget, the approved change order log, the pending change order queue, and committed cost records" via MCP; says owners can report "cost exposure to lenders or equity partners", but no lender feature described; $37M Series A Nov 2023 [V/F, prior notes]. **Position:** sits beside IRIS. Flags: (b) claimed intent only.

### 5.6 Procore for Owners — see 1.1.

---

## 6. AI on construction records

### 6.1 Datagrid (now Procore) — see 1.1. **Position:** adjacent AI tool (builder-side). Flags: (a) yes; (b) no; (c) no.

### 6.2 Document Crunch (now Trimble)
- Contract and document risk AI: "critical risk provisions, payment disputes, specification non-compliance, and notification failures"; "Project Assist" cross-document agent (Jun 2026); GCs/subs plus owners and insurers; Series B $21.5M led by Titanium Ventures with Nemetschek (14 Oct 2024); Trimble acquisition closed 4 Apr 2026, $246.4M; North America only [F, CO/AI 14 Oct 2024; prior notes citing Trimble 10-Q]. **Position:** adjacent AI tool (builder-side). Flags: (a) across documents, not cost systems; (b) no; (c) no.
- Source: https://getcoai.com/news/ai-startup-document-crunch-raises-21-5m-for-contract-analysis (14 Oct 2024).

### 6.3 Trunk Tools (New York)
- Source-backed Q&A over project documents plus Schedule, Submittal and Risk agents (coordination/compliance risk, not financial); reads Procore, Autodesk Build, SharePoint, Egnyte, Box; GCs and trades; $40M Series B led by Insight Partners, 24 Jul 2025 ($70M total); US/Canada [F, Unite.AI]. **Position:** adjacent AI tool (builder-side). Flags: (a) across document stores; (b) no; (c) no.
- Source: https://www.unite.ai/trunk-tools-raises-40m-series-b-to-bring-contuctions-ai-agents-to-the-frontlines/ (24 Jul 2025).

### 6.4 Alloovium (Brisbane)
- Cited answers over project files, template population, user-built workflows; SharePoint named; founders Zander Schweitzer (ex-site engineer) and Cielo Nicolosi; Startmate Summer26, full-time since Dec 2025; first pilot onboarded; targets $1M ARR and 75 partner companies in 12 months [F/V, Startmate, 10 Apr 2026]. Prior notes add YC Summer 2026 and Procore/Aconex/Asite connectors [V]. F4 Fund: "general contractors ... disconnected systems" [V]. No developer/lender angle. **Position:** adjacent AI tool (builder-side). Flags: (a) across documents/correspondence; (b) no; (c) no.
- Sources: https://startmate.com/writing/construction-runs-on-paperwork-alloovium-wants-to-change-that (10 Apr 2026); https://f4.fund/startups/alloovium.

### 6.5 Octant AI (Brisbane / Austin)
- Top-down ML outturn forecaster (cost, revenue, margin, cash flow) from "schedules, cost reports, and financial cash flow data" plus public data; names "financiers" among decision-makers who use its insights [V, Software Advice AU]; BMD paid ~A$1M for 10% (Aug 2021); 2019 alliance with Mott MacDonald and WT Partnership; 2025 push to US contractors [F, prior notes]. **Position:** adjacent AI tool (builder-side). Flags: (a) no (summary data); (b) no product; (c) no.
- Sources: https://www.softwareadvice.com.au/software/252121/octant-ai; https://www.startupdaily.net/2021/08/queensland-contruction-empire-bmd-bets-1-million-on-ai-based-project-management-startup-octant/ (17 Aug 2021).

### 6.6 Slate Technologies (California)
- "Decision assistant" that ingests "all the major construction software platforms" (Procore named in an example) and links to the schedule; modules for progress reporting and real-estate intelligence (targets banks, REITs as land buyers); Tier 1 GC customers; revenue doubling quarterly (CEO claim); ~$20M raised (aggregators conflict) [V, Pulse 2.0, 10 Jan 2025; prior notes]. **Position:** adjacent AI tool (builder-side). Flags: (a) yes, for the builder; (b) no; (c) no.
- Source: https://pulse2.com/slate-profile-trevor-schick-interview/ (10 Jan 2025).

### 6.7 nPlan (London)
- Schedule-risk AI trained on 750,000+ schedules; "Barry" assistant and Schedule Studio; $16M Series B led by CapHorn, Chevron Technology Ventures, Suffolk Technologies, 17 Oct 2025; owners and contractors (HS2, Network Rail, Chevron, NEOM); no lender/insurer product named; APAC expansion planned, Australia not named [F, nplan.io]. **Position:** adjacent AI tool (builder-side). Flags: none.
- Source: https://www.nplan.io/press-releases/nplan-raises-16m-series-b-to-scale-its-ai-led-transformation-of-capital-project-delivery (17 Oct 2025).

### 6.8 Buildots, Doxel, OpenSpace (site-progress AI)
- **Buildots**: $130M round led by O.G. Venture Partners, 14 Sep 2026 ($297M total); "control layer for large construction programs"; owners (Digital Realty, Intel) and GCs (Bouygues, HOCHTIEF); no lender use; no Australia mention [F, Pulse 2.0]. **Doxel**: owner reporting and pay-app validation (US) [prior notes]. **OpenSpace**: bought Disperse Oct 2025; some AU use [prior notes]. **Position:** sits beside IRIS (they verify physical progress, the QS's domain). Flags: (b) partial for Doxel (owner-side pay-app validation); no lender product.
- Source: https://pulse2.com/buildots-raises-130-million/amp/ (14 Sep 2026).

### 6.9 ALICE, Versatile, Parspec, Pype, Briq, Kojo, Enlaye, INGENIOUS.BUILD
- ALICE (schedule optimisation), Versatile (crane-hook sensors), Parspec ($20M raise; submittal/spec for distributors), Pype (Autodesk; submittal logs): builder-side, no finance or lender layer [U, headlines/prior knowledge]. Briq Otto AI (Dec 2025): "continuous reconciliation between field activity and financials" across Trimble ERPs [V, 1.4]. Kojo: trade procurement [prior notes]. Enlaye: $5M seed Jun 2026, "risk intelligence" from documents for contractors, developers, owners, insurers [F, prior notes]. **Position:** adjacent AI tool (builder-side) for all. Flags: (a) Briq and Enlaye partial; (b) none; (c) none.

### 6.10 Australian AI construction start-ups, 2025–26 (raises found)
- **ProcurePro** (Brisbane/London/Dubai): procurement platform; $15M (US$11M) Series B led by QIC Ventures with Airtree, Glitch and Bouygues/ISAI, 5 May 2026; valuation >$100M; integrations Procore, Aconex, Jobpac, Cheops, Office, DocuSign; AI BidLevel, AI Pulse, AI Pricing Library; 6,000+ projects, $130B+ value; no lender features [F/V, procurepro.co]. **Position:** source system IRIS reads. Flags: (a) no; (b) no; (c) no.
- **BuildPass** (Melbourne): site safety/QA/induction SaaS with AI defect and photo recognition; $7.5M seed led by Carthona, 27 Oct 2024; 400+ customers [F, iTWire]. Sits beside IRIS.
- **Visibuild** (Melbourne): on-site quality checking; $6.6M seed led by Skip Capital (Dec 2024); customers BESIX Watpac, Kapitol, Icon [F, Business News Australia]. Sits beside IRIS.
- **Scopey Onsite**: WhatsApp/voice site records; €523K pre-seed led by SFC Capital (Mar 2026) [F, Medianet]. Sits beside IRIS.
- **Deep Space**, **Plexa**, **Alloovium**, **Octant** — above. **Anility** (Sydney): subcontractor default-risk monitoring for builders [V, prior notes]. **BuildGuard AI** (CSIRO ON Prime, Victoria University, 9 Oct 2025): research-stage "financial, project, and compliance signals" for builder-insolvency prediction aimed at builders, insurers, financiers, regulators [F, CSIRO page]. **Position:** adjacent AI tool (lender-side) in intent; research stage. Flags: (a) in intent; (b) in intent; (c) no.
- **Not found:** any Australian start-up selling a lender-facing project-risk position built from builder systems. [U]
- Sources: https://procurepro.co/news/capital-raise-2026 (5 May 2026); https://itwire.com/it-industry-news/deals/ai-construction-software-creator-buildpass-lands-%247-5m-in-seed-capital (27 Oct 2024); https://www.businessnewsaustralia.com/amp-html/articles/construction-tech-visibuild-raises--6-6m-in-debut-capital-raise-backed-by-skip-capital.html; https://newshub.medianet.com.au/2026/03/building-big-australian-entrepreneurs-raise-e523k-irish-funding-for-agentic-construction-platform/143493 (Mar 2026); https://research.csiro.au/onalumni/buildguard-ai (9 Oct 2025).

---

## 7. Credit and counterparty data

### 7.1 CreditorWatch
- B2B credit bureau; construction offering for subcontractors and suppliers: builder credit checks by ABN from ASIC, ABR, ATO, court and payment-default data, alerts "when risk increases"; no project-level or lender product on the page [F, creditorwatch.com.au]. 2026 construction risk report: trade payment defaults 2.5% residential / 1.9% commercial; 60+ day arrears 10.3% commercial [F, prior notes, Aug 2026]. **Position:** credit data. Flags: none.
- Source: https://creditorwatch.com.au/construction-subcontractors-and-suppliers.

### 7.2 Equifax (iCIRT), illion (now Experian), Dun & Bradstreet, Rapid Ratings
- **Equifax iCIRT**: one-to-five star ratings of construction professionals from "character, capability, and capital" data; register lists 3+ gold stars; pitched to developers, consumers, financiers and insurers for pricing risk [F, Equifax newsroom, 1 Jun 2023]. Company-level, not project-level. **Experian** completed its A$820M purchase of **illion**, 30 Sep 2024 [F, Experian release]. **D&B** and **Rapid Ratings** (private-company financial health scores): company-level [U]. Built uses Experian BusinessIQ for GC health inside its lender product [V, 4.1]. **Position:** credit data. Flags: none; but a lender tool can embed them (Built does).
- Sources: https://equifax.com/newsroom/all-news/-/story/how-equifax-s-icirt-builds-trust-for-developers-consumers-in-australia (1 Jun 2023); https://www.experianplc.com/newsroom/press-releases/2024/experian-completes-820m-acquisition-of-illion (30 Sep 2024).

### 7.3 "Builder financial health" services
- **Newpoint Advisory**: pre-contract builder due diligence (historic and forecast financials, retention-trust compliance, ATO lodgements, disputes), updated "at least annually"; serves developers and lenders [V, TUD sponsored, 4 Oct 2022]. **Position:** service incumbent / channel. Flags: none.
- Source: https://www.theurbandeveloper.com/articles/protect-your-project-with-builder-due-diligence (4 Oct 2022).

---

## 8. Service incumbents

### 8.1 The lender's QS (RLB, WT, Slattery, Napier & Blakeley, MBM, Mitchell Brandtman, Turner & Townsend, Altus, Acumentis and others)
- **What they do.** Initial cost report before financial close (contract, budget, contingency, programme, builder capacity, drawdown forecast) and monthly progress certificates (work done, materials, variations, retention, programme, cost to complete). "A quantity surveyor report gates your drawdowns": the lender appoints, the report is addressed to the lender, the developer usually pays; facility sized so undrawn funds plus equity cover completion, with equity top-up if cost to complete exceeds remaining funds [F/3P, Feasly guide]. AIQS guidance (2019) sets the financier's report content [F, prior notes; AIQS CFR 2019 PDF]. Acumentis: progress-claim reports "typically commissioned by the financier"; monthly or milestone inspections; no software named [V, acumentis.com.au]. RLB (Americas page): technical due diligence then construction-phase monitoring (site visits, cost/schedule analysis, disbursement review) for "facility agreements, forward funding, and joint ventures"; no technology named [V, rlb.com].
- **Records layer.** The builder's claim, site inspection, documents from developer and builder, statutory declarations. They do not read builder systems [F/I].
- **Lender / facility.** **Yes — the QS certificate is the existing drawdown condition.** This is the service IRIS must sit beside, not replace.
- **Technology.** No AI or platform product from these firms found in this session or in prior notes [U].
- **Position:** service incumbent / channel.
- **Flags:** (a) no; (b) **yes** (the incumbent project-level position for the lender); (c) **yes**, as a service.
- Sources: https://www.feasly.com.au/guides/quantity-surveyor-reports-australia; https://acumentis.com.au/expertise/financier-reporting-progress-claims/; https://www.rlb.com/americas/services/specialist-solutions/lender-services/; https://www.aiqs.com.au/sites/default/files/uploaded-content/website-content/cfr2019.pdf [U, not re-fetched].

### 8.2 Restructuring and forensic advisers (McGrathNicol, KordaMentha, FTI, Deloitte, KPMG) and project-monitoring consultancies
- KordaMentha Real Estate: advises financiers on "deteriorating credits, including partially complete construction projects"; development management with programme monitoring, cost-to-complete assessments, PCG meetings; "special situations" for distressed assets; "$26B+ assets managed or advised since 2007"; no technology platform named [V, KordaMentha brochure]. McGrathNicol, FTI, Deloitte, KPMG: independent business reviews, receiverships and completions of stalled projects [U, general knowledge; Roberts Co and Grocon administrations in search results]. **Position:** service incumbent / channel (the "distressed-project assessment" buyer and competitor). Flags: (b) yes, as a service at engagement; (c) no.
- Source: https://kmbrochures.blob.core.windows.net/kmbrochuresuat/Brochures/REA_Service-line-brochure_A4_02_DIGITAL.pdf.

---

## 9. Threat table: anything that touches (a), (b) or (c)

| Product | (a) reconciles across source systems | (b) lender project-level position | (c) written into facility | Verified? |
|---|---|---|---|---|
| IPEX (AU) | No: QS certified vs its own payment ledger | Yes: monthly payment position at drawdown | Vendor CEO says some lenders "mandate the controls as a condition of lending" (Nov 2025) | (b) from sponsored content; (c) unverified by any lender |
| Lender's QS (AU) | No | Yes: certified value, cost to complete | Yes, as a service condition precedent to drawdown | Market practice; Feasly/Acumentis/AIQS |
| Built (US) | Partly: Procore + Sage/Yardi sync | Yes: draw, budget variance, covenant alerts, GC credit | Operationally required by lenders; no covenant wording found | Vendor pages and a bank's builder guide |
| Land Gorilla (US) | No | Yes: draw level plus X-RAY builder reliability | No evidence | Vendor |
| Rabbet (US) | No | Yes: loan budget, covenant checks | No evidence | Vendor |
| Procore + Datagrid | Yes, for the builder (ERP, docs) | No | No | Press releases |
| Slate, Trunk Tools, Alloovium, Briq | Yes, for the builder | No | No | Vendor / press |
| Trimble (Document Crunch + Jobpac) | Emerging, builder-side | No | No | 10-Q; roadmap statements |
| Doxel / Buildots | No | Owner-side progress validation only | No | Vendor / press |
| BuildGuard AI (AU, research) | In intent | In intent | No | CSIRO programme page |

---

## 10. One-page summary

**Names an investor is most likely to raise (12).** IPEX; Procore (with Datagrid and the owner suite); Built Technologies; Rabbet; Land Gorilla; the lender's QS (RLB, WT, Napier & Blakeley, Slattery, MBM, Mitchell Brandtman); Mastt; Payapps/Autodesk; Trimble (Jobpac plus Document Crunch); ProcurePro; Octant AI; Alloovium. Second tier: CreditorWatch/Equifax iCIRT, Kahua, Northspyre, Buildots, KordaMentha/McGrathNicol.

**The three that come closest.**
1. **IPEX** — the only Australian product that gives a lender a project-level monthly position (payments vs certified progress) and whose vendor says lenders are starting to mandate it. It reads a bank account and payment files, not the builder's systems; it sees no internal cost, commitments, unsubmitted variations, notices or time bars. Two of its named financiers (Trilogy Funds, MaxCap) are IRIS's target lender type. Expect every Australian non-bank lender to name it.
2. **Built Technologies** — the scale proof that lenders will pay for a platform that reads Procore financials and administers draws (300+ US lenders, ~$317B+). It stops at the head-contract draw layer and has no ANZ presence. It defines what "lender-side" means to a US-literate investor.
3. **Procore with Datagrid** (and, one step behind, Trimble with Document Crunch and Jobpac) — the incumbents now own cross-system agents that read a builder's ERP and documents. They have not built a lender or developer view, and their paying customer is the builder, which gives them no commercial reason to expose the builder's position outward. This is the strongest "why can't Procore do this" question.

**Does the bounded claim survive?** **Yes, as worded, with one edit and two caveats.**
- *No product found that reconciles a project's systems into one position for builder, developer and lender:* holds. Cross-system reconciliation exists only builder-side (Datagrid, Slate, Trunk Tools, Alloovium, Briq) or lender-side on submitted packages (Built, Rabbet, Land Gorilla). None combines both and reports outward.
- *Or that a lender writes into its facility:* **at risk as written.** IPEX's CEO says lenders now mandate IPEX "as a condition of lending into certain jobs" (Nov 2025), and the lender's QS certificate is already a drawdown condition on every facility. Recommended wording: "no *software* product that reconciles a project's systems into one position for builder, developer and lender; the controls lenders write into facilities today are the QS certificate and, on some projects, a payment-account control (IPEX)." That keeps the claim true, pre-empts the IPEX question, and positions IRIS beside both rather than against them.
- Caveats: (i) all IPEX evidence is sponsored or self-published and no lender has confirmed a mandate publicly; (ii) "no product found" rests on public sources, and private in-house tools at Tier 1 builders or lenders cannot be seen; (iii) the search allowlist blocked ipex.com.au, so IPEX's own product pages were not read.

**Weakest point in IRIS's position.** Lenders already have two controls at the drawdown (QS certificate, and for some, IPEX on money movement) that expose less builder data than IRIS needs. IRIS has to show that the exposure sitting in the builder's records *before* it reaches a claim or a payment is worth a third control, and that a builder will grant read access to get the job. No public evidence yet that any lender has mandated analytics of a builder's records.
