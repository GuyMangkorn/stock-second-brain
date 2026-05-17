---
type: entity
ticker: MSFT
company: Microsoft Corporation
market: Nasdaq
currency: USD
period_type: quarterly
reporting_scope: FY26 Q3 and nine months ended 2026-03-31
latest_period: FY26 Q3
latest_period_end: 2026-03-31
latest_total_revenue_usd_m: 82886
latest_net_income_usd_m: 31778
source_gap_count: 4
source_gaps:
  - Current market price and valuation multiples require fresh market-data check.
  - Product-level dollar revenue not normalized where only growth rates were disclosed.
  - Full annual FY2026 data is not yet available.
  - Longer historical segment comparisons were not normalized in this ingest.
source_notes:
  - raw/imports/MSFT_latest_results_source.md
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
| Latest period | FY26 Q3, quarter ended 2026-03-31 |
| Reporting scope | FY26 Q3 and nine months ended 2026-03-31 |
| Latest total revenue | USD 82,886 million |
| Latest net income | USD 31,778 million |
| Normalized file | [[MSFT_fundamentals]] |

Microsoft is a technology company that creates platforms and tools powered by AI, with durable revenue exposure across cloud infrastructure, productivity software, business applications, search, gaming, and devices. This snapshot is sourced from the FY26 Q3 Form 10-Q and official Microsoft Investor Relations materials.

## Source Map

| Priority | Source | Status | Notes |
|---:|---|---|---|
| 1 | SEC / official filings | Found | Form 10-Q filed 2026-04-29, accession `0001193125-26-191507`, period of report 2026-03-31. |
| 2 | Earnings transcript | Found | Microsoft FY26 Q3 earnings call transcript dated 2026-04-29. |
| 3 | Financial statements / metrics | Found | Microsoft FY26 Q3 IR income statements, balance sheets, cash flows, and segment results. |
| 4 | News / web context | Found but not used for durable numbers | Reuters context found; official sources were sufficient for financial facts. |

## Business Model

- Productivity and Business Processes: Microsoft 365 commercial and consumer products and cloud services, LinkedIn, and Dynamics.
- Intelligent Cloud: Azure and other cloud services, server products, cloud infrastructure, and related enterprise services.
- More Personal Computing: Windows, Devices, Search and news advertising, and Gaming.
- Management commentary emphasizes Microsoft Cloud, Azure, Microsoft 365 Copilot, GitHub Copilot, Security Copilot, and broader AI infrastructure as key growth drivers.

## Segments / Revenue Mix

| Segment | FY26 Q3 Revenue | Share of FY26 Q3 Revenue | FY26 Q3 Operating Income | Source |
|---|---:|---:|---:|---|
| Productivity and Business Processes | 35,013 | 42.24% | 20,973 | Microsoft FY26 Q3 segment results |
| Intelligent Cloud | 34,681 | 41.84% | 13,753 | Microsoft FY26 Q3 segment results |
| More Personal Computing | 13,192 | 15.92% | 3,672 | Microsoft FY26 Q3 segment results |
| Total | 82,886 | 100.00% | 38,398 | Microsoft FY26 Q3 segment results |

## Financial Facts

| Metric | FY26 Q3 | FY25 Q3 | 9M FY26 | 9M FY25 | Source |
|---|---:|---:|---:|---:|---|
| Total revenue | 82,886 | 70,066 | 241,832 | 205,283 | Microsoft FY26 Q3 income statements |
| Gross margin | 56,058 | 48,147 | 164,983 | 141,466 | Microsoft FY26 Q3 income statements |
| Operating income | 38,398 | 32,000 | 114,634 | 94,205 | Microsoft FY26 Q3 income statements |
| Net income | 31,778 | 25,824 | 97,983 | 74,599 | Microsoft FY26 Q3 income statements |
| Diluted EPS | 4.27 | 3.46 | 13.14 | 9.99 | Microsoft FY26 Q3 income statements |
| Net cash from operations | 46,679 | 37,044 | 127,494 | 93,515 | Microsoft FY26 Q3 cash flows |
| Additions to property and equipment | (30,876) | (16,745) | (80,146) | (47,472) | Microsoft FY26 Q3 cash flows |
| Free cash flow | 15,803 | 20,299 | 47,348 | 46,043 | Calculated: net cash from operations plus additions to property and equipment. |

### Key Ratios

| Ratio | FY26 Q3 / 2026-03-31 | Formula |
|---|---:|---|
| Gross profit margin | 67.63% | 56,058 / 82,886 |
| Operating margin | 46.33% | 38,398 / 82,886 |
| Net profit margin | 38.34% | 31,778 / 82,886 |
| Current ratio | 1.28x | 175,329 / 136,661 |
| Quick ratio | 1.01x | (32,105 + 46,167 + 60,041) / 136,661 |
| Liabilities / equity | 0.68x | 279,861 / 414,367 |

## Charts

The chart blocks below use only verified values from `raw/financials/MSFT_fundamentals.md`.

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

### Segment Revenue

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

Capex is plotted as positive spend. Microsoft reports additions to property and
equipment as cash outflows.

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

## Transcript / Management Commentary

- Microsoft Cloud revenue was disclosed at USD 54.5 billion in FY26 Q3, up 29% year over year.
- Management said the AI business surpassed a USD 37 billion annual revenue run rate, up 123% year over year.
- Azure and other cloud services revenue grew 40% year over year, or 39% in constant currency.
- Commercial remaining performance obligation was USD 627 billion, up 99% year over year.
- Q3 capital expenditures were USD 31.9 billion; management said roughly two thirds of Q3 capex was for short-lived assets, primarily GPUs and CPUs.
- Q4 FY26 revenue outlook was USD 86.7 billion to USD 87.8 billion; management expected calendar 2026 capex of roughly USD 190 billion.

## Thesis

### Bull Case

- Microsoft is converting cloud and AI demand into reported growth: FY26 Q3 revenue rose 18%, operating income rose 20%, and Azure and other cloud services grew 40%.
- The company has a broad monetization surface across Azure, Microsoft 365, Dynamics, GitHub, Security, LinkedIn, and consumer endpoints.
- Commercial remaining performance obligation of USD 627 billion provides a large contracted revenue base, though recognition timing and OpenAI-related exposure need monitoring.

### Bear Case

- AI infrastructure spend is rising rapidly: Q3 capex was USD 31.9 billion and management guided calendar 2026 capex to roughly USD 190 billion.
- Microsoft Cloud gross margin pressure is tied to AI infrastructure investment and growing AI product usage.
- More Personal Computing revenue declined 1% in FY26 Q3, with weakness in Windows OEM and Devices and Xbox content and services.

### Key Debate

The central debate is whether Microsoft can translate very high AI and cloud infrastructure spending into durable revenue growth and margins that offset higher depreciation, finance leases, component costs, and capacity constraints.

## Risks

- AI infrastructure capacity, component cost, and finance lease intensity may pressure free cash flow and margins.
- Cloud and AI competition may reduce pricing power or increase required investment.
- More Personal Computing remains exposed to PC, device, gaming, and advertising cycles.
- OpenAI partnership economics and customer concentration inside AI workloads should be monitored through filings and transcripts.
- Current valuation risk is not assessed here because market price and multiples were not freshly checked.

## Catalysts

- Azure growth acceleration or improved capacity availability.
- Microsoft 365 Copilot paid seat growth and ARPU expansion.
- GitHub Copilot and Security Copilot monetization under usage-based models.
- Better-than-expected AI infrastructure efficiency or capex-to-revenue conversion.
- FY26 Q4 results and full-year FY2026 Form 10-K.

## Valuation Watch Items

- Fresh market price, market capitalization, enterprise value, P/E, EV/revenue, EV/operating income, free cash flow yield, dividend yield.
- Trailing twelve-month EPS and free cash flow after FY26 Q4 / FY2026 10-K.
- Depreciation and finance lease impacts from AI datacenter buildout.
- Microsoft Cloud gross margin trend.

## Reports / Source Notes

- [[MSFT_latest_results_source]]
- [[MSFT_fundamentals]]
- `raw/financials/MSFT_fundamentals.json`
- SEC 10-Q filing detail: https://www.sec.gov/Archives/edgar/data/789019/0001193125-26-191507-index.html
- Microsoft FY26 Q3 transcript: https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q3

## Follow-Up

- Freshly check market price and valuation multiples before making valuation claims.
- Add FY2025 annual baseline from Form 10-K for longer annual trend context.
- After FY26 Q4 / FY2026 10-K, update full-year revenue, operating income, net income, free cash flow, and segment trends.
- Track capex, finance leases, depreciation, and Microsoft Cloud gross margin in the next update.

## Missing / Unverified Data

- Current market price and valuation multiples: not ingested.
- Product-level dollar revenue where only growth rates were disclosed: not disclosed.
- Full annual FY2026 results: not available in the latest official source.
- Long historical segment data: not ingested in this pass.
