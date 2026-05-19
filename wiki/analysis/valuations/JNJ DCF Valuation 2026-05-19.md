---
type: analysis
analysis_type: dcf-valuation
ticker: JNJ
company: Johnson & Johnson
date: 2026-05-19
currency: USD
source_files:
  - wiki/entities/JNJ.md
  - raw/financials/JNJ_fundamentals.md
  - raw/imports/JNJ_latest_results_source.md
tags:
  - analysis/dcf
  - ticker/JNJ
---

# JNJ DCF Valuation - 2026-05-19

## Bottom Line

This DCF can be run because the required inputs were freshly checked: current price, market cap, shares, cash, debt, free cash flow, and guidance. The result is a valuation warning.

Using FY2026 FCF outlook of approximately USD 21B, Q1 2026 cash plus marketable securities of USD 22.051B, total debt of USD 54.987B, diluted average shares of 2.4452B, a base WACC of 8.5%, terminal growth of 2.5%, and a five-year FCF growth fade from 6.0% to 4.0%, base-case fair value is approximately USD 150 per diluted share.

Against the fresh price check of USD 228.92 on 2026-05-18, the base case implies roughly 34% downside. Even the upper end of the sensitivity table, using 7.5% WACC and 3.0% terminal growth, is about USD 202 per share, below the current price.

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| Entity page | `wiki/entities/JNJ.md` | Business model, source map, thesis, risks. |
| Normalized facts | `raw/financials/JNJ_fundamentals.md` | Q1 2026 financials, balance sheet, FCF, shares, segment facts. |
| Latest source note | `raw/imports/JNJ_latest_results_source.md` | Local source extraction and ingest provenance. |
| SEC Q1 2026 Form 10-Q | https://www.sec.gov/Archives/edgar/data/200406/000020040626000087/jnj-20260329.htm | Official quarterly facts, shares, cash, debt, OCF, capex. |
| FY2025 Annual Report | https://www.jnj.com/download/johnson-johnson-2025-annual-report | FY2025 annual FCF baseline. |
| Q1 2026 earnings call transcript | https://s203.q4cdn.com/636242992/files/doc_financials/2026/q1/JNJ-USQ_Transcript_2026-04-14.pdf | FY2026 FCF outlook and management commentary. |
| Q1 2026 earnings presentation | https://s203.q4cdn.com/636242992/files/doc_financials/2026/q1/JNJ-Earnings-Presentation-Q1-2026-Final.pdf | Capital allocation and guidance. |
| FinanceCharts JNJ price history | https://www.financecharts.com/stocks/JNJ/summary/price | Fresh price check, checked 2026-05-19 Bangkok time. |

## Input Table

All company financial statement amounts are USD billions unless noted.

| Input | Value | Source / Calculation |
|---|---:|---|
| Fresh market price used | USD 228.92 | FinanceCharts price page, closing share price for 2026-05-18; checked 2026-05-19 Bangkok time. |
| Common shares outstanding | 2.407216971B | SEC Form 10-Q, shares outstanding as of 2026-04-17. |
| Fresh market cap | USD 551.1B | Calculated: 228.92 * 2.407216971B. |
| FinanceCharts market cap cross-check | USD 552.324B | FinanceCharts price page; provider market cap uses provider share basis. |
| Diluted shares used for DCF | 2.4452B | SEC Form 10-Q, Q1 2026 diluted average shares. |
| Cash and cash equivalents | 21.688 | SEC Form 10-Q. |
| Marketable securities | 0.363 | SEC Form 10-Q. |
| Cash + marketable securities | 22.051 | 21.688 + 0.363. |
| Loans and notes payable | 17.460 | SEC Form 10-Q. |
| Long-term debt | 37.527 | SEC Form 10-Q. |
| Total debt | 54.987 | 17.460 + 37.527. |
| Net debt | 32.936 | 54.987 - 22.051. |
| Q1 2026 operating cash flow | 2.514 | SEC Form 10-Q. |
| Q1 2026 capex spend | 1.049 | SEC Form 10-Q, cash outflow converted to positive spend. |
| Q1 2026 free cash flow | 1.465 | 2.514 - 1.049. |
| FY2025 operating cash flow | 24.530 | FY2025 Annual Report. |
| FY2025 capex spend | 4.832 | FY2025 Annual Report. |
| FY2025 free cash flow | 19.698 | 24.530 - 4.832. |
| FY2026 FCF outlook | approximately 21.000 | Q1 2026 earnings call transcript. |
| FY2026 reported sales guidance midpoint | 100.8 | Q1 2026 press release / presentation. |
| FY2026 adjusted EPS guidance midpoint | USD 11.55 | Q1 2026 press release / presentation; non-GAAP. |

## Base Case Assumptions

| Assumption | Bear | Base | Bull |
|---|---:|---:|---:|
| Starting FCF reference | FY2026 outlook USD 21.0B | FY2026 outlook USD 21.0B | FY2026 outlook USD 21.0B |
| Year 1 FCF growth | 3.0% | 6.0% | 8.0% |
| Year 2 FCF growth | 3.0% | 5.5% | 7.0% |
| Year 3 FCF growth | 2.5% | 5.0% | 6.0% |
| Year 4 FCF growth | 2.5% | 4.5% | 5.0% |
| Year 5 FCF growth | 2.0% | 4.0% | 4.0% |
| WACC | 9.5% | 8.5% | 7.5% |
| Terminal growth | 2.0% | 2.5% | 3.0% |

WACC basis: JNJ is a large health care company. The vault reference range for Health Care is 8%-10%. Base WACC is 8.5% because the company has scale, diversification, and resilient cash generation, partly offset by regulatory, litigation, patent-cycle, and product-pipeline risk.

Terminal growth basis: 2.0%-3.0% is the mature developed-market compounder range in `wiki/reference/valuation-assumptions.md`.

## FCF Projection

Base case amounts are USD billions.

| Year | FCF | Growth |
|---:|---:|---:|
| Starting FY2026 outlook | 21.000 | n/a |
| Year 1 | 22.260 | 6.0% |
| Year 2 | 23.484 | 5.5% |
| Year 3 | 24.659 | 5.0% |
| Year 4 | 25.768 | 4.5% |
| Year 5 | 26.799 | 4.0% |

Base rationale: the model starts from the CFO's approximately USD 21B FY2026 FCF outlook rather than annualizing Q1 2026 FCF, because management said Q1 was depressed by payment timing changes and increased U.S. capex. The growth path fades because JNJ is a mature, diversified health care compounder rather than an early-stage growth business.

## Valuation Summary

Amounts are USD billions except per-share data.

| Scenario | WACC | Terminal Growth | PV of Explicit FCF | PV of Terminal Value | Enterprise Value | Net Debt | Equity Value | Fair Value / Diluted Share | Upside / Downside vs USD 228.92 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Bear | 9.5% | 2.0% | 87.938 | 253.877 | 341.815 | (32.936) | 308.879 | 126.32 | -44.8% |
| Base | 8.5% | 2.5% | 96.186 | 304.467 | 400.654 | (32.936) | 367.718 | 150.38 | -34.3% |
| Bull | 7.5% | 3.0% | 101.622 | 414.569 | 516.191 | (32.936) | 483.255 | 197.63 | -13.7% |

## Sensitivity Matrix

Base projection fair value per diluted share, USD.

| WACC / Terminal Growth | 2.0% | 2.5% | 3.0% |
|---:|---:|---:|---:|
| 7.5% | 168.5 | 183.5 | 201.7 |
| 8.5% | 140.2 | 150.4 | 162.4 |
| 9.5% | 119.5 | 126.8 | 135.1 |

## Sanity Checks

| Check | Result | Read |
|---|---:|---|
| Market cap / FY2026 FCF outlook | 26.2x | USD 551.1B / USD 21.0B. Rich for a mature health care compounder. |
| FY2026 FCF yield on market cap | 3.81% | USD 21.0B / USD 551.1B. |
| Market EV / FY2026 FCF outlook | 27.8x | Market cap + net debt divided by FY2026 FCF outlook. |
| Base terminal value share of EV | 76.0% | High but below the 85%-90% warning zone. |
| Dividend yield | 2.34% | USD 5.36 annual dividend / USD 228.92 price. Good income support, but not enough to offset valuation alone. |
| FCF vs dividends | covered on FY2025 and FY2026 outlook | FY2025 FCF USD 19.698B covered FY2025 dividends of USD 12.381B; FY2026 FCF outlook about USD 21B supports dividend capacity. |

## What Would Change The Valuation

- FY2026 FCF outlook is raised materially above approximately USD 21B.
- Net debt declines faster than modeled.
- Innovative Medicine launches offset STELARA erosion with better-than-expected cash conversion.
- MedTech margin pressure from tariffs and separation costs fades faster than expected.
- Legal/talc risk becomes materially less costly or less uncertain.
- The share price falls toward a level where FCF yield and DCF sensitivity offer a real margin of safety.

## Missing / Unverified Data

| Data item | Status | Valuation impact |
|---|---|---|
| Product-level revenue for ICOTYDE and IMAAVY | not disclosed | Cannot underwrite launch ramp precisely. |
| Product-level profitability by brand | not disclosed | Cannot isolate brand-level margin contribution. |
| GAAP forward guidance | not provided | DCF uses FCF and non-GAAP guidance context instead. |
| FY2026 full-year actual results | ไม่พบข้อมูลที่ยืนยันได้ | Current DCF relies on Q1 2026 actuals and FY2026 outlook. |
| Long-term post-2026 FCF guidance | ไม่พบข้อมูลที่ยืนยันได้ | Years 1-5 are scenario assumptions, not company guidance. |

## Entity Update

Updated `wiki/entities/JNJ.md` with this valuation memo link and valuation watch items. The valuation changes the decision read toward wait/avoid new capital at current price.
