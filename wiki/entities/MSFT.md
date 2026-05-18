---
type: entity
ticker: MSFT
company: Microsoft Corporation
market: Nasdaq
currency: USD
period_type: quarterly + annual
reporting_scope: FY2025 annual baseline plus FY26 Q3 and nine months ended 2026-03-31
latest_period: FY26 Q3
latest_period_end: 2026-03-31
latest_total_revenue_usd_m: 82886
latest_net_income_usd_m: 31778
source_gap_count: 5
source_gaps:
  - Current market price, valuation multiples, market capitalization, and analyst targets require a fresh market-data check before valuation use.
  - Product-level FY26 Q3 dollar revenue where Microsoft disclosed only growth rates: ไม่พบข้อมูลที่ยืนยันได้.
  - Exact revenue contribution and margin profile of individual AI products such as Microsoft 365 Copilot, GitHub Copilot, and Security Copilot: not disclosed.
  - OpenAI-specific Azure capacity, contract concentration, and economics are not disclosed with enough granularity for normalized valuation work.
  - Full annual FY2026 results are not yet available.
source_notes:
  - raw/imports/MSFT_latest_results_source.md
  - raw/imports/MSFT_company_deep_dive_2026-05-17.md
normalized_markdown: raw/financials/MSFT_fundamentals.md
normalized_json: raw/financials/MSFT_fundamentals.json
tags:
  - entity/company
  - ticker/MSFT
---

# MSFT - Microsoft Corporation

## Snapshot

| Item | Value |
|---|---|
| Ticker | MSFT |
| Company | Microsoft Corporation |
| Market | Nasdaq |
| Currency | USD |
| Latest verified period | FY26 Q3, quarter ended 2026-03-31 |
| Annual baseline | FY2025, year ended 2025-06-30 |
| Latest quarterly revenue | USD 82,886 million |
| Latest quarterly net income | USD 31,778 million |
| FY2025 revenue | USD 281,724 million |
| FY2025 net income | USD 101,832 million |
| Normalized file | [[MSFT_fundamentals]] |
| Deep dive source note | [[MSFT_company_deep_dive_2026-05-17]] |

Microsoft is a global software, cloud, AI, gaming, productivity, developer, and advertising platform company. The durable investment question is no longer whether the core franchise has scale; official FY2025 and FY26 Q3 sources show it does. The debate is whether very large AI infrastructure investment can keep compounding Azure, Microsoft 365, GitHub, Security, Dynamics, and consumer AI monetization without permanently compressing free cash flow and cloud margins.

## Source Map

| Priority | Source | Status | Notes |
|---:|---|---|---|
| 1 | SEC / official filings | Found | FY2025 Form 10-K / Annual Report: https://www.sec.gov/Archives/edgar/data/789019/000095017025100235/msft-20250630.htm and https://www.microsoft.com/investor/reports/ar25/index.html. FY26 Q3 Form 10-Q filing detail: https://www.sec.gov/Archives/edgar/data/789019/0001193125-26-191507-index.html. |
| 2 | Earnings transcript | Found | FY26 Q3 earnings call transcript: https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q3. |
| 3 | Financial statements / metrics | Found | FY26 Q3 Microsoft IR financial tables and FY2025 Annual Report Note 18 segment and product/service revenue tables. |
| 4 | News / web context | Not used for durable financial facts | Official filings, IR tables, and the official transcript were sufficient for this deep dive. |

## Business Model

Microsoft monetizes a broad installed base through subscription software, cloud consumption, enterprise licensing, advertising, gaming content, hardware, and services.

| Business line | Revenue mechanism | Durable driver | Primary official source |
|---|---|---|---|
| Microsoft 365 Commercial | Recurring subscriptions, cloud services, E5/security/compliance, Microsoft 365 Copilot, Office/Windows Commercial components | Seat growth, ARPU expansion, Copilot attach, migration from on-premises Office to cloud | FY2025 Annual Report; FY26 Q3 transcript. |
| Azure and server products | Consumption-based cloud and AI services, GitHub cloud services, SQL Server, Windows Server, Visual Studio, CALs, hybrid infrastructure | Workload migration, AI app demand, capacity availability, developer adoption | FY2025 Annual Report; FY26 Q3 transcript. |
| Dynamics and Power Platform | Cloud and on-premises ERP/CRM, low-code, usage-based credits, agentic business apps | Business process digitization, seat plus consumption model, cross-sell into Microsoft 365/Azure | FY2025 Annual Report; FY26 Q3 transcript. |
| LinkedIn | Talent, Marketing, Premium, Sales Solutions, subscriptions and advertising | Member engagement, recruiter demand, B2B ads, AI-enabled sales/hiring workflow | FY2025 Annual Report; FY26 Q3 transcript. |
| Windows and Devices | OEM licenses, commercial Windows components, Surface and accessories | PC cycle, Windows install base, enterprise compatibility, edge AI opportunities | FY2025 Annual Report; FY26 Q3 transcript. |
| Gaming | Xbox content, Game Pass, first-party and third-party content, cloud gaming, hardware, advertising | Content slate, subscription pricing, active users, Activision Blizzard integration | FY2025 Annual Report; FY26 Q3 transcript. |
| Search and news advertising | Bing, Edge, Copilot search, Microsoft News, affiliate traffic | Search volume, revenue per search, Edge/Bing share gains, AI search engagement | FY2025 Annual Report; FY26 Q3 transcript. |

### What Makes The Model Work

- Enterprise annuity base: commercial subscriptions, enterprise agreements, RPO, and mission-critical identity/security/admin surfaces support retention and upsell.
- Cloud consumption loop: Azure demand pulls through data, AI, developer, security, and management workloads.
- AI distribution: Copilot can be distributed through Microsoft 365, GitHub, Dynamics, Security, Windows, Edge, Bing, and Xbox rather than through a single product surface.
- Capital intensity: Microsoft is increasingly a software plus infrastructure compounder; capex, finance leases, depreciation, energy, and GPU/CPU cost now matter more to free cash flow than in a pure software model.

## Segments / Revenue Mix

### FY26 Q3 Segment Mix

| Segment | FY26 Q3 Revenue | Share of FY26 Q3 Revenue | FY26 Q3 Operating Income | Source |
|---|---:|---:|---:|---|
| Productivity and Business Processes | 35,013 | 42.24% | 20,973 | Microsoft FY26 Q3 segment results. |
| Intelligent Cloud | 34,681 | 41.84% | 13,753 | Microsoft FY26 Q3 segment results. |
| More Personal Computing | 13,192 | 15.92% | 3,672 | Microsoft FY26 Q3 segment results. |
| Total | 82,886 | 100.00% | 38,398 | Microsoft FY26 Q3 segment results. |

### FY2025 Annual Segment Mix

| Segment | FY2025 Revenue | Share of FY2025 Revenue | FY2025 Operating Income | Source |
|---|---:|---:|---:|---|
| Productivity and Business Processes | 120,810 | 42.88% | 69,773 | Microsoft FY2025 Annual Report, Note 18. |
| Intelligent Cloud | 106,265 | 37.72% | 44,589 | Microsoft FY2025 Annual Report, Note 18. |
| More Personal Computing | 54,649 | 19.40% | 14,166 | Microsoft FY2025 Annual Report, Note 18. |
| Total | 281,724 | 100.00% | 128,528 | Microsoft FY2025 Annual Report, Note 18. |

### FY2025 Product / Service Revenue Mix

| Product / service offering | FY2025 Revenue | Share of FY2025 Revenue | Source |
|---|---:|---:|---|
| Server products and cloud services | 98,435 | 34.94% | Microsoft FY2025 Annual Report, Note 18. |
| Microsoft 365 Commercial products and cloud services | 87,767 | 31.15% | Microsoft FY2025 Annual Report, Note 18. |
| Gaming | 23,455 | 8.33% | Microsoft FY2025 Annual Report, Note 18. |
| LinkedIn | 17,812 | 6.32% | Microsoft FY2025 Annual Report, Note 18. |
| Windows and Devices | 17,314 | 6.15% | Microsoft FY2025 Annual Report, Note 18. |
| Search and news advertising | 13,878 | 4.93% | Microsoft FY2025 Annual Report, Note 18. |
| Dynamics products and cloud services | 7,827 | 2.78% | Microsoft FY2025 Annual Report, Note 18. |
| Enterprise and partner services | 7,760 | 2.75% | Microsoft FY2025 Annual Report, Note 18. |
| Microsoft 365 Consumer products and cloud services | 7,404 | 2.63% | Microsoft FY2025 Annual Report, Note 18. |
| Other | 72 | 0.03% | Microsoft FY2025 Annual Report, Note 18. |
| Total | 281,724 | 100.00% | Microsoft FY2025 Annual Report, Note 18. |

### Revenue Mix Read

The core company is now mainly commercial cloud and productivity. Productivity and Business Processes plus Intelligent Cloud represented 80.60% of FY2025 revenue and 84.08% of FY26 Q3 revenue, based on official segment tables. More Personal Computing still matters for distribution and cash generation, but it is no longer the center of the financial mix.

## Financial Facts

### Latest Quarterly And YTD Facts

| Metric | FY26 Q3 | FY25 Q3 | 9M FY26 | 9M FY25 | Source |
|---|---:|---:|---:|---:|---|
| Total revenue | 82,886 | 70,066 | 241,832 | 205,283 | Microsoft FY26 Q3 income statements. |
| Gross margin | 56,058 | 48,147 | 164,983 | 141,466 | Microsoft FY26 Q3 income statements. |
| Operating income | 38,398 | 32,000 | 114,634 | 94,205 | Microsoft FY26 Q3 income statements. |
| Net income | 31,778 | 25,824 | 97,983 | 74,599 | Microsoft FY26 Q3 income statements. |
| Diluted EPS | 4.27 | 3.46 | 13.14 | 9.99 | Microsoft FY26 Q3 income statements. |
| Net cash from operations | 46,679 | 37,044 | 127,494 | 93,515 | Microsoft FY26 Q3 cash flows. |
| Additions to property and equipment | (30,876) | (16,745) | (80,146) | (47,472) | Microsoft FY26 Q3 cash flows. |
| Free cash flow | 15,803 | 20,299 | 47,348 | 46,043 | Calculated: net cash from operations plus additions to property and equipment. |

### FY2025 Annual Baseline

| Metric | FY2025 | FY2024 | YoY Change | Source |
|---|---:|---:|---:|---|
| Revenue | 281,724 | 245,122 | 15% | Microsoft FY2025 Annual Report, Summary Results of Operations. |
| Gross margin | 193,893 | 171,008 | 13% | Microsoft FY2025 Annual Report, Summary Results of Operations. |
| Operating income | 128,528 | 109,433 | 17% | Microsoft FY2025 Annual Report, Summary Results of Operations. |
| Net income | 101,832 | 88,136 | 16% | Microsoft FY2025 Annual Report, Summary Results of Operations. |
| Diluted EPS | 13.64 | 11.80 | 16% | Microsoft FY2025 Annual Report, Summary Results of Operations. |
| Microsoft Cloud revenue | 168,900 | 137,700 | 23% | Microsoft FY2025 Annual Report, Note 18 / MD&A. |

### Key Ratios

| Ratio | Period / date | Value | Formula |
|---|---|---:|---|
| Gross profit margin | FY26 Q3 | 67.63% | 56,058 / 82,886 |
| Operating margin | FY26 Q3 | 46.33% | 38,398 / 82,886 |
| Net profit margin | FY26 Q3 | 38.34% | 31,778 / 82,886 |
| Gross profit margin | FY2025 | 68.82% | 193,893 / 281,724 |
| Operating margin | FY2025 | 45.62% | 128,528 / 281,724 |
| Net profit margin | FY2025 | 36.15% | 101,832 / 281,724 |
| Current ratio | 2026-03-31 | 1.28x | 175,329 / 136,661 |
| Quick ratio | 2026-03-31 | 1.01x | (32,105 + 46,167 + 60,041) / 136,661 |
| Liabilities / equity | 2026-03-31 | 0.68x | 279,861 / 414,367 |

## Charts

The chart blocks below use only verified values from `raw/financials/MSFT_fundamentals.md` and `raw/imports/MSFT_company_deep_dive_2026-05-17.md`.

### Quarterly YoY Comparison

```chart
type: bar
labels: ["FY25 Q3", "FY26 Q3"]
series:
  - title: Revenue
    backgroundColor: rgba(16, 185, 129, 0.72)
    borderColor: rgba(52, 211, 153, 1)
    data: [70066, 82886]
  - title: Operating Income
    backgroundColor: rgba(56, 189, 248, 0.68)
    borderColor: rgba(125, 211, 252, 1)
    data: [32000, 38398]
  - title: Net Income
    backgroundColor: rgba(251, 191, 36, 0.72)
    borderColor: rgba(252, 211, 77, 1)
    data: [25824, 31778]
```

### YTD Comparison

```chart
type: bar
labels: ["9M FY25", "9M FY26"]
series:
  - title: Revenue
    backgroundColor: rgba(16, 185, 129, 0.72)
    borderColor: rgba(52, 211, 153, 1)
    data: [205283, 241832]
  - title: Operating Income
    backgroundColor: rgba(56, 189, 248, 0.68)
    borderColor: rgba(125, 211, 252, 1)
    data: [94205, 114634]
  - title: Net Income
    backgroundColor: rgba(251, 191, 36, 0.72)
    borderColor: rgba(252, 211, 77, 1)
    data: [74599, 97983]
  - title: Free Cash Flow
    backgroundColor: rgba(139, 92, 246, 0.68)
    borderColor: rgba(167, 139, 250, 1)
    data: [46043, 47348]
```

### FY2025 Segment Revenue

```chart
type: bar
labels: ["Productivity and Business Processes", "Intelligent Cloud", "More Personal Computing"]
series:
  - title: FY2025 Revenue
    backgroundColor: rgba(16, 185, 129, 0.72)
    borderColor: rgba(52, 211, 153, 1)
    data: [120810, 106265, 54649]
  - title: FY2025 Operating Income
    backgroundColor: rgba(56, 189, 248, 0.68)
    borderColor: rgba(125, 211, 252, 1)
    data: [69773, 44589, 14166]
```

### FY26 Q3 Segment Revenue

```chart
type: bar
labels: ["Productivity and Business Processes", "Intelligent Cloud", "More Personal Computing"]
series:
  - title: FY26 Q3 Revenue
    backgroundColor: rgba(16, 185, 129, 0.72)
    borderColor: rgba(52, 211, 153, 1)
    data: [35013, 34681, 13192]
  - title: FY25 Q3 Revenue
    backgroundColor: rgba(56, 189, 248, 0.68)
    borderColor: rgba(125, 211, 252, 1)
    data: [29944, 26751, 13371]
```

### Quarterly Cash Flow And Capex

Capex is plotted as positive spend. Microsoft reports additions to property and equipment as cash outflows.

```chart
type: bar
labels: ["FY25 Q3", "FY26 Q3"]
series:
  - title: Operating Cash Flow
    backgroundColor: rgba(16, 185, 129, 0.72)
    borderColor: rgba(52, 211, 153, 1)
    data: [37044, 46679]
  - title: Capex Spend
    backgroundColor: rgba(244, 63, 94, 0.64)
    borderColor: rgba(251, 113, 133, 1)
    data: [16745, 30876]
  - title: Free Cash Flow
    backgroundColor: rgba(251, 191, 36, 0.72)
    borderColor: rgba(252, 211, 77, 1)
    data: [20299, 15803]
```

### Balance Sheet Snapshot

```chart
type: bar
labels: ["2025-06-30", "2026-03-31"]
series:
  - title: Assets
    backgroundColor: rgba(16, 185, 129, 0.72)
    borderColor: rgba(52, 211, 153, 1)
    data: [619003, 694228]
  - title: Liabilities
    backgroundColor: rgba(244, 63, 94, 0.64)
    borderColor: rgba(251, 113, 133, 1)
    data: [275524, 279861]
  - title: Equity
    backgroundColor: rgba(56, 189, 248, 0.68)
    borderColor: rgba(125, 211, 252, 1)
    data: [343479, 414367]
```

## Moat

| Moat vector | Evidence | Watch item | Source |
|---|---|---|---|
| Enterprise distribution and switching costs | Microsoft 365, Teams, Office, Windows Commercial, identity, security, compliance, SharePoint, Power BI, and Copilot are bundled across enterprise workflows. | Whether Copilot ARPU and E5/security attach keep expanding without customer pushback. | FY2025 Annual Report; FY26 Q3 transcript. |
| Cloud scale and capacity | Azure and other cloud services grew 40% YoY in FY26 Q3; management said demand continues to exceed available capacity. | Whether capex and finance leases convert to revenue fast enough to protect FCF. | FY26 Q3 press release and transcript. |
| Data and workflow context | Microsoft cited Work IQ context across organizational documents, communications, meetings, and SharePoint sites; this is hard for standalone AI apps to replicate inside enterprises. | Whether customers view this as differentiated enough to pay for Copilot at scale. | FY26 Q3 transcript. |
| Developer ecosystem | Nearly 140,000 organizations used GitHub Copilot, and enterprise subscribers nearly tripled YoY. | Usage-based pricing must align revenue with inference cost and customer value. | FY26 Q3 transcript. |
| Security/compliance surface | Microsoft can bundle Defender, Purview, identity, endpoint, cloud security, and Security Copilot. | Security incidents or regulatory failures could erode trust. | FY2025 Annual Report; FY26 Q3 transcript. |
| Consumer distribution | Monthly active Windows devices surpassed 1.6 billion; Bing monthly active users reached 1 billion; Microsoft 365 Consumer had nearly 95 million subscribers. | Consumer AI monetization remains less proven than commercial AI monetization. | FY26 Q3 transcript. |
| Financial capacity | FY2025 net income was USD 101,832 million and FY26 Q3 operating income was USD 38,398 million. | The same capacity can become a risk if AI capex return thresholds fall. | FY2025 Annual Report; FY26 Q3 financial tables. |

## Transcript / Management Commentary

- AI business surpassed a USD 37 billion annual revenue run rate in FY26 Q3, up 123% YoY.
- Microsoft Cloud revenue was USD 54.5 billion in FY26 Q3, up 29% YoY, and Microsoft Cloud gross margin was 66%.
- Commercial RPO was USD 627 billion, up 99% YoY including OpenAI, with a weighted average duration of about two and a half years; roughly 25% is expected to be recognized within 12 months.
- Microsoft 365 Copilot paid seats were over 20 million; management said net paid seat additions accelerated and ARPU growth was led by E5 and Microsoft 365 Copilot.
- Azure and other cloud services grew 40% YoY; management said strong customer demand across workloads, segments, and regions continues to exceed available capacity.
- Q3 capital expenditures were USD 31.9 billion, roughly two thirds for short-lived assets such as GPUs and CPUs; cash paid for property and equipment was USD 30.9 billion.
- FY26 Q4 revenue guidance was USD 86.7 billion to USD 87.8 billion; calendar 2026 capex expectation was roughly USD 190 billion, including about USD 25 billion from higher component pricing.
- Management expected FY27 double-digit revenue and operating income growth, but this is forward-looking guidance rather than a verified result.

## Thesis

### Bull Case

- Microsoft has multiple compounding engines rather than one product cycle: Azure, Microsoft 365, GitHub, Security, Dynamics, LinkedIn, Windows, Search, and Gaming.
- The latest official quarter shows strong commercial momentum: FY26 Q3 revenue grew 18%, operating income grew 20%, Azure and other cloud services grew 40%, and Microsoft Cloud revenue grew 29%.
- AI monetization has real reported scale: management disclosed a USD 37 billion AI business annual revenue run rate and over 20 million Microsoft 365 Copilot paid seats.
- The enterprise moat is strengthened by workflow context, identity, security, compliance, admin, and data surfaces that sit inside existing customer operations.
- RPO of USD 627 billion provides visibility, though OpenAI-related concentration and recognition timing need monitoring.

### Bear Case

- AI infrastructure turns Microsoft into a more capital-intensive business: Q3 capex was USD 31.9 billion and calendar 2026 capex is expected at roughly USD 190 billion.
- Microsoft Cloud gross margin and Intelligent Cloud gross margin are under pressure from AI infrastructure, GitHub Copilot usage, and accelerated capacity buildout.
- More Personal Computing remains cyclical; FY26 Q3 revenue declined 1%, with Windows OEM/Devices and Xbox content/services both declining.
- OpenAI-related bookings, capacity demand, investment accounting, and economics are not disclosed with enough granularity to fully underwrite concentration risk.
- Valuation could be fragile if investors capitalize AI growth while free cash flow lags due to capex, finance leases, depreciation, or component inflation.

### Key Debate

The key debate is whether Microsoft's AI infrastructure buildout produces enough incremental high-margin revenue across Azure, Microsoft 365, GitHub, Security, Dynamics, and consumer surfaces to offset higher capex, finance leases, depreciation, energy needs, GPU/CPU costs, and gross margin pressure.

### Current Action Read

2026-05-18 decision memo: `[[MSFT Decision Memo 2026-05-18]]` reads MSFT as **WAIT for new capital / HOLD for an existing normal-sized core position**. The business-quality read remains strong, but fresh market valuation and the DCF memo argue against adding until either price improves or free-cash-flow conversion catches up with AI capex.

## Risks

| Risk | Why it matters | Source / monitor |
|---|---|---|
| AI capex return risk | Calendar 2026 capex expectation of roughly USD 190 billion raises the hurdle for future revenue and margin conversion. | FY26 Q3 transcript; future cash flow statements. |
| Cloud margin compression | Microsoft Cloud gross margin was 66% in FY26 Q3 and guided to roughly 64% for Q4 due to AI investment and GitHub Copilot usage. | FY26 Q3 transcript. |
| Capacity, energy, GPU/CPU, land, and datacenter supply chain | Datacenters depend on buildable land, energy, networking, servers, GPUs, and other components; shortages can limit growth or increase costs. | FY2025 Annual Report risk/operations sections; FY26 Q3 transcript. |
| Competition | Microsoft competes across cloud, productivity, security, AI apps, search, gaming, devices, and business applications; competitors may pressure pricing or accelerate investment needs. | FY2025 Annual Report competition sections. |
| Cybersecurity and trust | Security incidents can harm Microsoft directly and can also affect customers that rely on Microsoft infrastructure and software. | FY2025 Form 10-K risk factors. |
| Regulation and antitrust | AI, cloud, platform bundling, privacy, security, data localization, app stores, and EU digital rules can constrain product design or economics. | FY2025 Annual Report regulatory discussion and risk factors. |
| Consumer and PC cyclicality | Windows OEM, Devices, Xbox hardware/content, and advertising are exposed to PC demand, game release cycles, pricing, inventory, and consumer behavior. | FY2025 Annual Report; FY26 Q3 transcript. |
| Accounting and concentration opacity around OpenAI | Official sources discuss OpenAI effects on bookings/RPO and investment impacts, but not enough to isolate Azure concentration, economics, or margin. | FY26 Q3 transcript and SEC filings. |

## Catalysts

| Catalyst | Evidence to watch | Source / future check |
|---|---|---|
| Azure growth and capacity delivery | Azure growth staying near management's Q4 FY26 39%-40% constant-currency outlook or accelerating in 2H calendar 2026. | Future earnings transcripts and segment results. |
| Copilot monetization | Microsoft 365 Copilot paid seat growth, ARPU uplift, E5 attach, usage intensity, retention, and large enterprise deployments. | Future Microsoft transcript metrics. |
| GitHub Copilot pricing transition | Usage-based pricing should better align revenue with usage and compute cost if customer adoption remains strong. | FY26 Q4 and FY27 transcript commentary. |
| AI infrastructure efficiency | Higher fleet utilization, lower unit inference/training cost, improved Azure efficiency, and stable or recovering Microsoft Cloud gross margin. | Cash flow statements, capex commentary, cloud gross margin. |
| Dynamics and agentic business apps | Seat plus consumption model and usage-based credits may create a second monetization curve beyond traditional SaaS seats. | Future Dynamics 365 growth and bookings commentary. |
| Consumer AI recovery | Bing/Edge share gains, Windows AI features, Microsoft 365 Consumer subscriber and ARPU growth, and Xbox engagement. | Future More Personal Computing metrics. |
| FY2026 10-K | Full-year FY2026 will clarify annual revenue mix, capex intensity, depreciation, finance leases, and segment profitability. | SEC 10-K after FY2026 year end. |

## Valuation Watch Items

- 2026-05-18 decision memo: `[[MSFT Decision Memo 2026-05-18]]` sets the current action read at WAIT for new money and HOLD for a normal-sized existing position; trim only if portfolio concentration is already too high.
- 2026-05-18 DCF memo: `[[MSFT DCF Valuation 2026-05-18]]` estimates base-case fair value at about USD 206 per diluted share versus the latest available market close of USD 421.92 on 2026-05-15. The key valuation watch item is whether AI capex converts into enough FCF growth to justify the current market-implied growth path.
- Fresh market price, market capitalization, enterprise value, diluted share count, dividend yield, buyback pace, P/E, EV/revenue, EV/operating income, and FCF yield.
- TTM free cash flow after FY26 Q4 / FY2026 10-K, especially whether operating cash flow growth offsets AI capex growth.
- Microsoft Cloud gross margin path: FY26 Q3 was 66%; Q4 guide was roughly 64%.
- Calendar 2026 capex vs revenue conversion: management expected roughly USD 190 billion of capex, including about USD 25 billion from higher component pricing.
- Depreciation, finance lease interest, and operating lease payments from datacenter buildout.
- Azure growth against capacity constraints and customer demand signals.
- RPO quality: recognition timing, OpenAI-related exposure, duration, and renewal quality.
- AI product monetization: Microsoft 365 Copilot seats/ARPU, GitHub Copilot usage-based revenue, Security Copilot adoption, Dynamics usage credits.

## Reports / Source Notes

- [[MSFT Decision Memo 2026-05-18]]
- [[MSFT DCF Valuation 2026-05-18]]
- [[MSFT_latest_results_source]]
- [[MSFT_company_deep_dive_2026-05-17]]
- [[MSFT_fundamentals]]
- `raw/financials/MSFT_fundamentals.json`
- SEC FY2025 Form 10-K: https://www.sec.gov/Archives/edgar/data/789019/000095017025100235/msft-20250630.htm
- Microsoft FY2025 Annual Report: https://www.microsoft.com/investor/reports/ar25/index.html
- SEC FY26 Q3 Form 10-Q filing detail: https://www.sec.gov/Archives/edgar/data/789019/0001193125-26-191507-index.html
- Microsoft FY26 Q3 transcript: https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q3
- Microsoft FY26 Q3 press release and financial tables: https://www.microsoft.com/en-us/investor/earnings/fy-2026-q3/press-release-webcast

## Unanswered Questions

| Question | Why it matters | Current status |
|---|---|---|
| What is the true gross margin of AI workloads after GPUs, CPUs, depreciation, leases, energy, networking, and support costs? | Determines whether AI revenue is accretive or dilutive to long-run Microsoft economics. | Not disclosed in official sources reviewed. |
| How much of Azure growth and RPO is OpenAI-related versus diversified enterprise demand? | Concentration affects durability and bargaining power. | Partially discussed in transcript, but not disclosed with enough granularity. |
| How quickly can Microsoft convert capex into available capacity and revenue? | Demand exceeds available capacity; timing affects near-term growth and FCF. | Track quarterly capex, finance leases, Azure growth, and management capacity commentary. |
| Can Microsoft 365 Copilot become a broad paid habit rather than a premium-seat niche? | Copilot is central to ARPU expansion in the productivity franchise. | Over 20 million paid seats disclosed, but retention, utilization, and revenue are not separately disclosed. |
| Will usage-based GitHub Copilot pricing improve margins without slowing adoption? | Developer AI usage can be compute-intensive. | Transition announced; financial impact not yet reported. |
| Does More Personal Computing stabilize or remain a drag? | Windows, Xbox, devices, and search still influence distribution and cash flow. | FY26 Q3 revenue declined 1%; Q4 guidance called out PC and Xbox pressure. |
| What valuation compensates for both quality and AI capex risk? | The business can be excellent while the stock is expensive. | Requires fresh market-data and valuation work. |

## Follow-Up

- Run a valuation pass only after freshly checking price, market cap, share count, net cash/debt, FCF, and current multiples.
- Add FY2026 full-year figures when the FY2026 Form 10-K is filed.
- Track Microsoft Cloud gross margin, Azure growth, capex, finance leases, depreciation, and operating lease payments every quarter.
- Track Copilot paid seats, GitHub Copilot organizations/subscribers, Security Copilot customers, Dynamics usage credits, and any disclosed AI revenue details.
- Reconcile OpenAI impact on bookings/RPO and investment accounting in future filings.

## Missing / Unverified Data

| Data item | Status | Notes / Follow-up |
|---|---|---|
| Current stock price, market cap, P/E, EV/revenue, EV/operating income, FCF yield, dividend yield, and analyst targets | ไม่พบข้อมูลที่ยืนยันได้ในไฟล์ input | Requires fresh market-data check before valuation use. |
| Product-level FY26 Q3 revenue dollars where Microsoft disclosed only growth rates | ไม่พบข้อมูลที่ยืนยันได้ | Do not backfill without an official table. |
| Exact revenue and margin contribution of Microsoft 365 Copilot, GitHub Copilot, Security Copilot, and individual AI products | Not disclosed | Track transcript and segment commentary. |
| OpenAI-specific Azure revenue, backlog, capacity, margin, and contract exposure | Partially disclosed but insufficient | Transcript separates some booking/RPO commentary but not enough for a normalized table. |
| Full annual FY2026 results | ไม่พบข้อมูลที่ยืนยันได้ | FY2026 is incomplete as of FY26 Q3. |
