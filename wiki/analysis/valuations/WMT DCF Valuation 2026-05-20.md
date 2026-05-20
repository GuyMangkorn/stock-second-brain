---
type: analysis
analysis_type: dcf-valuation
ticker: WMT
company: Walmart Inc.
date: 2026-05-20
currency: USD
source_files:
  - wiki/entities/WMT.md
  - raw/financials/WMT_fundamentals.md
  - raw/imports/WMT_latest_results_source.md
tags:
  - analysis/dcf
  - ticker/WMT
---

# WMT DCF Valuation - 2026-05-20

## Bottom Line

DCF can be run because the core inputs were source-backed or freshly checked: current price, market cap, shares, cash, debt, FCF, and guidance. The main limitation is that Walmart has not disclosed FY2027 FCF guidance, so this model starts from FY2026 reported FCF and treats FY2027 guidance as directional context rather than an FCF forecast.

Using FY2026 FCF of USD 14.923B, cash of USD 10.727B, total debt and finance lease obligations of USD 51.523B, FY2026 diluted weighted-average shares of 8.022B, base WACC of 7.5%, terminal growth of 2.5%, and a five-year FCF growth path fading from 6.0% to 3.5%, base-case fair value is approximately USD 37.41 per diluted share.

Against the fresh WMT quote of USD 132.57 on 2026-05-20, the base case implies about 72% downside. This is a valuation warning, not a business-quality downgrade: Walmart is a defensive scale leader, but the current share price requires far stronger FCF per share expansion than the latest source-backed FCF base alone supports.

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| Entity page | `wiki/entities/WMT.md` | Business model, thesis, risks, catalysts. |
| Normalized facts | `raw/financials/WMT_fundamentals.md` | FY2026 financials, balance sheet, FCF, shares, guidance, and market data. |
| Latest source note | `raw/imports/WMT_latest_results_source.md` | P1 official-source extraction and ingest provenance. |
| FY2026 Form 10-K | https://stock.walmart.com/sec-filings/all-sec-filings/content/0000104169-26-000055/0000104169-26-000055.pdf | Official annual financials, segment data, FCF, shares. |
| Q4 FY26 earnings release | https://corporate.walmart.com/content/dam/corporate/documents/newsroom/2026/02/19/walmart-releases-q4-fy26-earnings/q4-fy26-earnings-release.pdf | FY2027 guidance, balance sheet, cash flow, EPS, diluted shares. |
| Q4 FY26 earnings transcript | https://corporate.walmart.com/content/dam/corporate/documents/newsroom/2026/02/19/walmart-releases-q4-fy26-earnings/q4-fy26-earnings-call-transcript.pdf | Management commentary on growth drivers. |
| Stooq quote CSV | https://stooq.com/q/l/?s=wmt.us&f=sd2t2ohlcv&h&e=csv | Fresh quote, checked 2026-05-20. |

## Input Table

Amounts are USD billions unless noted.

| Input | Value | Source / Calculation |
|---|---:|---|
| Fresh market price used | USD 132.57 | Stooq CSV, WMT.US, 2026-05-20 17:29:38. |
| Common shares outstanding | 7.972402501B | FY2026 Form 10-K, as of 2026-03-11. |
| Implied market cap | USD 1,056.901B | 132.57 * 7.972402501B. |
| Diluted shares used for DCF | 8.022B | Q4 FY26 earnings release, FY2026 diluted weighted-average shares. |
| Cash and cash equivalents | 10.727 | Q4 FY26 earnings release. |
| Short-term borrowings | 6.596 | Q4 FY26 earnings release. |
| Current long-term debt | 3.542 | Q4 FY26 earnings release. |
| Long-term debt | 34.624 | Q4 FY26 earnings release. |
| Current finance lease obligations | 0.856 | Q4 FY26 earnings release. |
| Long-term finance lease obligations | 5.905 | Q4 FY26 earnings release. |
| Total debt and finance lease obligations | 51.523 | 6.596 + 3.542 + 34.624 + 0.856 + 5.905. |
| Net debt and finance lease obligations | 40.796 | 51.523 - 10.727. |
| FY2026 operating cash flow | 41.565 | FY2026 Form 10-K. |
| FY2026 capex spend | 26.642 | FY2026 Form 10-K. |
| FY2026 free cash flow | 14.923 | FY2026 Form 10-K reconciliation. |
| FY2027 net sales guidance | +3.5% to +4.5% constant currency | Q4 FY26 earnings release. |
| FY2027 adjusted operating income guidance | +6.0% to +8.0% constant currency | Q4 FY26 earnings release; non-GAAP. |
| FY2027 adjusted EPS guidance | USD 2.75 to USD 2.85 | Q4 FY26 earnings release; non-GAAP. |
| FY2027 capex guidance | approximately 3.5% of net sales | Q4 FY26 earnings release. |

## Base Case Assumptions

| Assumption | Bear | Base | Bull |
|---|---:|---:|---:|
| FCF anchor | 14.923 | 14.923 | 14.923 |
| Year 1 FCF growth | 2.5% | 6.0% | 8.0% |
| Year 2 FCF growth | 3.0% | 6.0% | 7.5% |
| Year 3 FCF growth | 3.0% | 5.0% | 7.0% |
| Year 4 FCF growth | 2.5% | 4.0% | 6.0% |
| Year 5 FCF growth | 2.5% | 3.5% | 5.0% |
| WACC | 8.5% | 7.5% | 6.5% |
| Terminal growth | 2.0% | 2.5% | 3.0% |

WACC basis: Consumer Staples range in `wiki/reference/valuation-assumptions.md` is 7%-8%. Base WACC of 7.5% reflects Walmart's defensive scale, recurring traffic, and investment-grade-like access to capital, while still recognizing tariff, labor, capex, and low-margin retail risk. Bull WACC of 6.5% is below the normal range and should be treated as an optimistic quality premium case.

Terminal growth basis: 2.5% is inside the mature developed-market / GDP-like defensive range. Long-run growth above 3.0% would require durable proof that higher-margin digital businesses can compound FCF faster than core retail without excessive capex.

## FCF Projection

Base case amounts are USD billions.

| Year | FCF | Growth |
|---:|---:|---:|
| Year 1 | 15.818 | 6.0% |
| Year 2 | 16.767 | 6.0% |
| Year 3 | 17.606 | 5.0% |
| Year 4 | 18.310 | 4.0% |
| Year 5 | 18.951 | 3.5% |

Base rationale: FY2027 guidance implies adjusted operating income can grow faster than sales, but FY2027 capex remains heavy at approximately 3.5% of net sales and management did not disclose FCF guidance. The projection therefore assumes FCF improves but does not force an aggressive step-change.

## Valuation Summary

Amounts are USD billions except per-share data.

| Scenario | WACC | Terminal Growth | Enterprise Value | Cash | Debt + Finance Leases | Equity Value | Fair Value / Diluted Share | Upside / Downside vs USD 132.57 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Bear | 8.5% | 2.0% | 241.5 | 10.7 | (51.5) | 200.7 | 25.01 | -81.1% |
| Base | 7.5% | 2.5% | 340.9 | 10.7 | (51.5) | 300.1 | 37.41 | -71.8% |
| Bull | 6.5% | 3.0% | 519.3 | 10.7 | (51.5) | 478.5 | 59.65 | -55.0% |

## Sensitivity Matrix

Base projection fair value per diluted share, USD.

| WACC / Terminal Growth | 2.0% | 2.5% | 3.0% |
|---:|---:|---:|---:|
| 6.5% | 43.01 | 48.11 | 54.67 |
| 7.5% | 34.20 | 37.41 | 41.34 |
| 8.5% | 28.10 | 30.28 | 32.87 |

## Sanity Checks

| Check | Result | Read |
|---|---:|---|
| FY2026 FCF yield on implied market cap | 1.41% | Very low; market is pricing durable quality and growth far beyond current FCF yield. |
| Forward adjusted P/E on FY2027 guide midpoint | 47.35x | Premium multiple even using non-GAAP EPS. |
| Net debt and finance leases / FY2026 FCF | 2.73x | Manageable for Walmart, but not irrelevant at a low FCF yield. |
| Base terminal value share of EV | 79.4% | High but below the 85%-90% warning zone. |
| FY2027 capex guide | about 3.5% of net sales | Capex intensity remains a key FCF constraint. |

## What Would Change The Valuation

- FY2027 Q1 and YTD results show FCF conversion much stronger than FY2026.
- Walmart discloses FCF guidance or cash-flow commentary that supports a higher FCF anchor.
- Advertising, membership, marketplace, VIZIO, and data services disclose enough profitability to justify a materially higher FCF growth path.
- Capex intensity falls while omnichannel growth remains strong.
- Current price corrects sharply while guidance remains intact.

## Missing / Unverified Data

| Data item | Status | Valuation impact |
|---|---|---|
| FY2027 Q1 actual results | not yet available | Q1 event was scheduled for 2026-05-21; valuation should be refreshed after release. |
| FY2027 full-year FCF guidance | ไม่พบข้อมูลที่ยืนยันได้ | Model uses FY2026 FCF anchor and assumptions rather than invented FCF guidance. |
| Forward GAAP EPS / net income guidance | not provided | Limits GAAP earnings cross-check. |
| Product-level profitability for higher-margin businesses | not disclosed | Limits confidence in long-term FCF growth assumptions. |
| Segment-level FCF | not disclosed | Limits granular valuation by segment. |
| Investor-specific required return | not provided | Could alter personal action threshold but not the source-backed fair value math. |

## Entity Update

Updated `wiki/entities/WMT.md` with valuation watch items and an AVOID-new-capital / WAIT action read. The valuation gap is large enough that the decision memo should emphasize waiting for either a price reset or post-Q1 FY2027 source update.
