---
type: source-note
ticker: WMT
company: Walmart Inc.
source_kind: latest-results
search_date: 2026-05-20
reporting_scope: FY2026 fiscal year ended 2026-01-31 plus upcoming FY2027 Q1 event
currency: USD
normalized_output: raw/financials/WMT_fundamentals.md
entity: "[[WMT]]"
tags:
  - source/latest-results
  - ticker/WMT
---

# WMT - Latest Results Source

## Source Map

| Priority | Source | URL / Path | Publication Date | Notes |
|---:|---|---|---|---|
| 1 | FY2026 Form 10-K | https://stock.walmart.com/sec-filings/all-sec-filings/content/0000104169-26-000055/0000104169-26-000055.pdf | 2026-03-13 | Annual report for fiscal year ended 2026-01-31; used for financial statements, segment data, FCF, shares, cash, debt, and risk context. |
| 1 | Walmart IR latest financial results page | https://stock.walmart.com/ | checked 2026-05-20 | Confirms latest financial results available on the IR page are FY2026 fiscal year ended 2026-01-31; FY2027 Q1 event is scheduled 2026-05-21. |
| 1 | Q4 FY26 earnings release | https://corporate.walmart.com/content/dam/corporate/documents/newsroom/2026/02/19/walmart-releases-q4-fy26-earnings/q4-fy26-earnings-release.pdf | 2026-02-19 | Used for FY2026 / Q4 FY26 highlights, FY2027 guidance, balance sheet, cash flow, shares, and Q1 FY27 / FY27 outlook. |
| 2 | Q4 FY26 earnings call transcript | https://corporate.walmart.com/content/dam/corporate/documents/newsroom/2026/02/19/walmart-releases-q4-fy26-earnings/q4-fy26-earnings-call-transcript.pdf | 2026-02-19 | Used for management commentary on eCommerce, advertising, membership, automation, Sparky, delivery speed, and business mix. |
| 1 | FY2027 Q1 earnings event page | https://corporate.walmart.com/news/events/fy2027-q1-earnings-release | checked 2026-05-20 | Confirms Q1 FY2027 materials were scheduled to become available on 2026-05-21 at approximately 6 a.m. CT, after this source check. |
| 3 | Stooq quote CSV | https://stooq.com/q/l/?s=wmt.us&f=sd2t2ohlcv&h&e=csv | checked 2026-05-20 | Fresh market quote: WMT.US last/close USD 132.57 at 2026-05-20 17:29:38, volume 4,517,090. |

## Reporting Scope

- Company: Walmart Inc.
- Ticker: WMT.
- Exchange / market: Nasdaq Global Select Market. The FY2026 Form 10-K states Walmart common stock trades under `WMT` on Nasdaq.
- Latest official results available as of the 2026-05-20 Asia/Bangkok source check: FY2026 fiscal year ended 2026-01-31 and Q4 FY26 materials released 2026-02-19.
- FY2027 Q1 earnings were scheduled for 2026-05-21 at 7:00 a.m. US/Central, with materials expected around 6:00 a.m. CT. They were not yet available during this workflow.
- Fiscal year end: January 31.
- Basis: US GAAP for financial statements. Constant-currency and adjusted operating income / adjusted EPS guidance are non-GAAP and labeled as such.

## Currency / Units

- Currency: USD.
- Financial statement units: USD millions unless otherwise stated.
- Market data: USD per share, shares in billions, market cap in USD billions/trillions.
- FCF definition: Walmart-defined free cash flow equals net cash provided by operating activities minus payments for property and equipment.

## Extracted Facts

### Company / Market Identity

| Fact | Extracted value | Source |
|---|---:|---|
| Company name | Walmart Inc. | FY2026 Form 10-K. |
| Ticker | WMT | FY2026 Form 10-K. |
| Primary listing | Nasdaq Global Select Market | FY2026 Form 10-K. |
| Common shares outstanding | 7,972,402,501 as of 2026-03-11 | FY2026 Form 10-K cover page. |
| Holders of record | 185,190 as of 2026-03-11 | FY2026 Form 10-K. |
| Retail units at FY2026 period end | 10,955 | FY2026 Form 10-K. |
| Retail square feet at FY2026 period end | 1,057 million | FY2026 Form 10-K. |

### Annual Consolidated Results

| Metric | FY2026 | FY2025 | FY2024 | Source |
|---|---:|---:|---:|---|
| Net sales | 706,413 | 674,538 | 642,637 | FY2026 Form 10-K. |
| Membership and other income | 6,750 | 6,447 | 5,488 | FY2026 Form 10-K. |
| Total revenues | 713,163 | 680,985 | 648,125 | FY2026 Form 10-K. |
| Gross profit | 171,018 | 162,785 | 152,495 | FY2026 Form 10-K. |
| Operating expenses | 147,943 | 139,884 | 130,971 | FY2026 Form 10-K. |
| Operating income | 29,825 | 29,348 | 27,012 | FY2026 Form 10-K. |
| Consolidated net income | 22,270 | 20,157 | 16,270 | FY2026 Form 10-K. |
| Diluted EPS attributable to Walmart | 2.73 | 2.41 | not normalized | Q4 FY26 earnings release. |
| Diluted weighted-average shares | 8,022 | 8,081 | not normalized | Q4 FY26 earnings release; shares in millions. |

### Cash Flow

| Metric | FY2026 | FY2025 | FY2024 | Source |
|---|---:|---:|---:|---|
| Net cash provided by operating activities | 41,565 | 36,443 | 35,726 | FY2026 Form 10-K. |
| Payments for property and equipment | (26,642) | (23,783) | (20,606) | FY2026 Form 10-K. |
| Free cash flow | 14,923 | 12,660 | 15,120 | FY2026 Form 10-K reconciliation. |
| Net cash used in investing activities | (26,350) | (21,379) | (21,287) | FY2026 Form 10-K. |
| Net cash used in financing activities | (13,553) | (14,822) | (13,414) | FY2026 Form 10-K. |

### Balance Sheet Snapshot

| Metric | 2026-01-31 | 2025-01-31 | Source |
|---|---:|---:|---|
| Cash and cash equivalents | 10,727 | 9,037 | Q4 FY26 earnings release. |
| Total current assets | 84,874 | 79,458 | Q4 FY26 earnings release. |
| Property and equipment, net | 136,083 | 119,993 | Q4 FY26 earnings release. |
| Total assets | 284,668 | 260,823 | Q4 FY26 earnings release. |
| Short-term borrowings | 6,596 | 3,068 | Q4 FY26 earnings release. |
| Long-term debt due within one year | 3,542 | 2,598 | Q4 FY26 earnings release. |
| Long-term debt | 34,624 | 33,401 | Q4 FY26 earnings release. |
| Finance lease obligations due within one year | 856 | 800 | Q4 FY26 earnings release. |
| Long-term finance lease obligations | 5,905 | 5,923 | Q4 FY26 earnings release. |
| Total current liabilities | 107,469 | 96,584 | Q4 FY26 earnings release. |
| Total Walmart shareholders' equity | 99,617 | 91,013 | Q4 FY26 earnings release. |

### Segment Results

| Segment | FY2026 Net Sales | FY2026 Total Revenues | FY2026 Operating Income | Source |
|---|---:|---:|---:|---|
| Walmart U.S. | 482,975 | 485,599 | 25,158 | FY2026 Form 10-K. |
| Walmart International | 130,423 | 131,988 | 5,103 | FY2026 Form 10-K. |
| Sam's Club U.S. | 93,015 | 95,540 | 2,442 | FY2026 Form 10-K. |
| Corporate and support | not applicable | 36 membership/other income | (2,878) | FY2026 Form 10-K. |
| Consolidated | 706,413 | 713,163 | 29,825 | FY2026 Form 10-K. |

### Guidance

| Guidance item | Management outlook | Source |
|---|---|---|
| Q1 FY2027 net sales, constant currency | Increase 3.5% to 4.5% | Q4 FY26 earnings release. |
| Q1 FY2027 operating income, constant currency | Increase 4.0% to 6.0% | Q4 FY26 earnings release. |
| Q1 FY2027 adjusted EPS | USD 0.63 to USD 0.65 | Q4 FY26 earnings release; non-GAAP. |
| FY2027 net sales, constant currency | Increase 3.5% to 4.5% | Q4 FY26 earnings release. |
| FY2027 adjusted operating income, constant currency | Increase 6.0% to 8.0% | Q4 FY26 earnings release; non-GAAP. |
| FY2027 interest, net | Increase approximately USD 200M to USD 300M | Q4 FY26 earnings release. |
| FY2027 effective tax rate | Approximately 23.5% to 24.5% | Q4 FY26 earnings release. |
| FY2027 adjusted EPS | USD 2.75 to USD 2.85 | Q4 FY26 earnings release; non-GAAP. |
| FY2027 capital expenditures | Approximately 3.5% of net sales | Q4 FY26 earnings release. |
| FY2027 FCF guidance | ไม่พบข้อมูลที่ยืนยันได้ | No official FCF guidance was found in extracted sources. |

### Current Market Data Check

| Metric | Value | Source / Calculation |
|---|---:|---|
| Fresh quote | USD 132.57 | Stooq CSV, WMT.US, 2026-05-20 17:29:38. |
| Intraday open / high / low | USD 132.905 / 133.65 / 130.885 | Stooq CSV, checked 2026-05-20. |
| Volume at quote check | 4,517,090 | Stooq CSV. |
| Official shares outstanding | 7.972402501B | FY2026 Form 10-K, as of 2026-03-11. |
| Implied market cap | USD 1.057T | Calculation: 132.57 * 7.972402501B. |
| Diluted weighted-average shares | 8.022B | Q4 FY26 earnings release, FY2026. |

## Transcript / Commentary

- Management said FY2026 revenue exceeded USD 700B and adjusted operating income grew faster than sales on a constant-currency basis, despite higher claims expense and tariff-related uncertainty.
- The Q4 call emphasized business mix: eCommerce, advertising, membership fees, marketplace, VIZIO, and data services are intended to raise higher-margin contribution over time.
- Management said global eCommerce grew 24% in Q4 FY26; Walmart U.S. eCommerce grew 27%.
- The call framed store, club, distribution center, fulfillment center, and last-mile networks as assets that improve speed and lower marginal cost as digital volume scales.
- Sparky / agentic commerce was described as early but encouraging; management said roughly half of app users had engaged with Sparky and that engagement was associated with higher order values.
- Management noted advertising businesses globally increased 37% in Q4 FY26, including Walmart Connect U.S. up 41%, while membership income increased more than 15%.

## Financial Tables

The extracted financial tables above are sufficient for P4 normalization, P11 DCF inputs, and P13 decision memo. Missing items are listed below rather than inferred.

## Missing / Unverified Data

| Item | Status | Notes |
|---|---|---|
| FY2027 Q1 actual results | not yet available | Official event page says materials become available 2026-05-21, after this 2026-05-20 source check. |
| FY2027 full-year FCF guidance | ไม่พบข้อมูลที่ยืนยันได้ | Official guidance discloses net sales, adjusted operating income, adjusted EPS, interest, tax rate, and capex, not FCF. |
| Forward GAAP EPS / net income guidance | not provided | Guidance is non-GAAP where noted because certain GAAP items cannot be predicted. |
| Product-level profitability by eCommerce, ads, marketplace, membership, VIZIO, and data services | not disclosed | Management commentary gives growth and strategic direction, not full profit pools. |
| Segment-level free cash flow | not disclosed | Cash flow is consolidated. |
| Exact live market quote after regular U.S. close on 2026-05-20 | partially verified | Stooq quote checked intraday; refresh before future action changes. |
| Investor-specific cost basis, position size, tax status, and required return | not provided | Needed for individualized add/hold/trim sizing. |

## Handoff For Ingest

- Normalize FY2026/FY2025/FY2024 annual consolidated results from the Form 10-K.
- Normalize FY2026 segment net sales, total revenues, and operating income.
- Normalize FY2026 cash, debt, finance lease obligations, shares, FCF, and FY2027 guidance from official sources.
- Use Stooq quote only for fresh market-data check; do not treat market data as durable company fact.
- Mark FY2027 Q1 actuals and FY2027 FCF guidance as missing/unverified. Do not infer them.
