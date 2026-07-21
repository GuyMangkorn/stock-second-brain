---
type: analysis
analysis_type: dcf-valuation
ticker: V
company: Visa Inc.
date: 2026-05-19
currency: USD
source_files:
  - wiki/entities/V.md
  - raw/financials/V_fundamentals.md
  - raw/imports/V_latest_results_source.md
tags:
  - analysis/dcf
  - ticker/V
---

# V DCF Valuation - 2026-05-19
Entity: [[V]]

## Bottom Line

This DCF can be run because the required inputs were freshly checked: current price, market cap, shares, cash, debt, FCF, and guidance. The key caveat is that Visa did not provide forward FCF guidance, so the five-year forecast is a scenario anchored to verified FY2025 FCF, 6M FY2026 FCF, and management's FY2026 revenue/EPS guidance.

Using FY2025 FCF of USD 21.577B as the starting FCF anchor, Q2 FY2026 cash plus investment securities of USD 14.221B, total debt of USD 23.976B, diluted weighted-average Class A shares of 1.916B, a base WACC of 8.5%, terminal growth of 2.5%, and a five-year FCF growth fade from 9.0% to 5.5%, base-case fair value is approximately USD 233 per diluted share.

Against the fresh price check of USD 332.64 on 2026-05-18, the base case implies about 30% downside. The bull case reaches approximately USD 337 per share, slightly above current price, but that case requires 12% first-year FCF growth, an extended high-growth fade, 7.5% WACC, and 3.0% terminal growth. That is possible for a high-quality compounder, but it is not a margin-of-safety setup.

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| Entity page | `wiki/entities/V.md` | Business model, source map, thesis, risks. |
| Normalized facts | `raw/financials/V_fundamentals.md` | Q2 FY2026 financials, balance sheet, FCF, shares, operating drivers. |
| Latest source note | `raw/imports/V_latest_results_source.md` | Local source extraction and ingest provenance. |
| SEC Q2 FY2026 Form 10-Q | https://www.sec.gov/Archives/edgar/data/1403161/000140316126000079/v-20260331.htm | Official quarterly facts, shares, cash, debt, OCF, capex. |
| FY2025 Form 10-K | https://www.sec.gov/Archives/edgar/data/1403161/000140316125000089/v-20250930.htm | FY2025 annual FCF baseline. |
| Q2 FY2026 earnings transcript | https://s1.q4cdn.com/050606653/files/doc_financials/2026/q2/CORRECTED-TRANSCRIPT_-Visa-Inc-V-US-Q2-2026-Earnings-Call-28-April-2026-5_00-PM-ET-4.pdf | Management commentary and guidance. |
| SEC May 2026 exchange-offer 8-Ks | https://www.sec.gov/Archives/edgar/data/1403161/000119312526215875/d59695d8k.htm and https://www.sec.gov/Archives/edgar/data/1403161/000119312526219432/d64238d8k.htm | Share-structure and litigation context. |
| FinanceCharts V price page | https://www.financecharts.com/stocks/V/summary/price | Fresh price and market cap check, checked 2026-05-19 Bangkok time. |

## Input Table

All company financial statement amounts are USD billions unless noted.

| Input | Value | Source / Calculation |
|---|---:|---|
| Fresh market price used | USD 332.64 | FinanceCharts price page, close for 2026-05-18; checked 2026-05-19 Bangkok time. |
| Market cap | USD 624.481B | FinanceCharts price page current metrics. |
| Diluted shares used for DCF | 1.916B | SEC 10-Q / earnings release, Q2 FY2026 diluted weighted-average Class A shares. |
| Cash and cash equivalents | 12.404 | SEC 10-Q. |
| Investment securities | 1.817 | SEC 10-Q; current and non-current combined. |
| Cash + investment securities | 14.221 | 12.404 + 1.817. |
| Current maturities of debt | 1.559 | SEC 10-Q. |
| Long-term debt | 22.417 | SEC 10-Q. |
| Total carrying value of debt | 23.976 | SEC 10-Q debt note. |
| Net debt | 9.755 | 23.976 - 14.221. |
| 6M FY2026 operating cash flow | 9.788 | SEC 10-Q. |
| 6M FY2026 capex spend | 0.761 | SEC 10-Q, cash outflow converted to positive spend. |
| 6M FY2026 free cash flow | 9.027 | 9.788 - 0.761. |
| FY2025 operating cash flow | 23.059 | FY2025 Form 10-K. |
| FY2025 capex spend | 1.482 | FY2025 Form 10-K. |
| FY2025 free cash flow | 21.577 | 23.059 - 1.482. |
| FY2026 adjusted net revenue guidance | low-double-digit to low-teens growth | Q2 FY2026 transcript. |
| FY2026 adjusted EPS guidance | low-teens growth | Q2 FY2026 transcript. |

## Base Case Assumptions

| Assumption | Bear | Base | Bull |
|---|---:|---:|---:|
| Starting FCF anchor | FY2025 FCF USD 21.577B | FY2025 FCF USD 21.577B | FY2025 FCF USD 21.577B |
| Year 1 FCF growth | 5.0% | 9.0% | 12.0% |
| Year 2 FCF growth | 5.0% | 8.5% | 11.0% |
| Year 3 FCF growth | 4.5% | 7.5% | 9.5% |
| Year 4 FCF growth | 4.0% | 6.5% | 8.0% |
| Year 5 FCF growth | 3.5% | 5.5% | 6.5% |
| WACC | 9.5% | 8.5% | 7.5% |
| Terminal growth | 2.0% | 2.5% | 3.0% |

WACC basis: Visa is classified economically as a high-quality payments technology / financial infrastructure compounder. The vault reference range for Financials is 8%-10%, and Information Technology is 8%-12%. Base WACC is 8.5% because the business has exceptional margins, network effects, and moderate net debt, offset by regulatory, litigation, fee-pricing, cross-border, and share-structure risks.

Terminal growth basis: 2.0%-3.0% is the mature developed-market compounder range in `wiki/reference/valuation-assumptions.md`.

## FCF Projection

Base case amounts are USD billions.

| Year | FCF | Growth |
|---:|---:|---:|
| Starting FY2025 FCF | 21.577 | n/a |
| Year 1 | 23.519 | 9.0% |
| Year 2 | 25.518 | 8.5% |
| Year 3 | 27.432 | 7.5% |
| Year 4 | 29.215 | 6.5% |
| Year 5 | 30.822 | 5.5% |

Base rationale: the model starts from verified FY2025 FCF instead of forcing a forward FCF guide that Visa did not disclose. The growth path reflects management's low-double-digit to low-teens FY2026 adjusted net revenue growth and low-teens adjusted EPS growth outlook, then fades because Visa is already a large, mature global network.

## Valuation Summary

Amounts are USD billions except per-share data.

| Scenario | WACC | Terminal Growth | PV of Explicit FCF | PV of Terminal Value | Enterprise Value | Net Debt | Equity Value | Fair Value / Diluted Share | Upside / Downside vs USD 332.64 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Bear | 9.5% | 2.0% | 94.445 | 231.168 | 325.613 | (9.755) | 315.858 | 164.85 | -50.4% |
| Base | 8.5% | 2.5% | 106.408 | 350.172 | 456.580 | (9.755) | 446.825 | 233.21 | -29.9% |
| Bull | 7.5% | 3.0% | 116.623 | 538.644 | 655.267 | (9.755) | 645.512 | 336.91 | 1.3% |

## Sensitivity Matrix

Base projection fair value per diluted share, USD.

| WACC / Terminal Growth | 2.0% | 2.5% | 3.0% |
|---:|---:|---:|---:|
| 7.5% | 259.8 | 281.7 | 308.5 |
| 8.5% | 218.3 | 233.2 | 250.8 |
| 9.5% | 187.9 | 198.6 | 210.9 |

## Sanity Checks

| Check | Result | Read |
|---|---:|---|
| Market cap / FY2025 FCF | 28.9x | USD 624.481B / USD 21.577B. Premium multiple. |
| FY2025 FCF yield on market cap | 3.45% | Strong quality, but not obviously cheap. |
| Market EV / FY2025 FCF | 29.4x | Market cap + net debt divided by FY2025 FCF. |
| Base terminal value share of EV | 76.7% | High but below the 85%-90% warning zone. |
| Q2 FY2026 operating margin | 64.4% | Confirms exceptional economics. |
| 6M FY2026 FCF vs 6M FY2025 | -4.2% | FCF was lower YoY despite stronger earnings, so cash conversion should be watched. |

## What Would Change The Valuation

- Visa discloses or delivers FY2026 FCF materially above the FY2025 baseline.
- Post-exchange-offer diluted share count becomes clearer and lower than the current DCF share basis.
- VAS and commercial/money movement sustain above-company growth without margin dilution.
- Regulatory and litigation risks fade or become less costly than modeled.
- The share price falls enough to lift FCF yield and create a genuine margin of safety.

## Missing / Unverified Data

| Data item | Status | Valuation impact |
|---|---|---|
| Forward free cash flow guidance | not disclosed | DCF uses scenario assumptions anchored to historical FCF and revenue/EPS guidance. |
| Post-exchange-offer fully diluted share count | ไม่พบข้อมูลที่ยืนยันได้ | Per-share valuation may need refresh after clearer share disclosure. |
| Segment profit by growth engine | not disclosed | Cannot value VAS/CMS separately. |
| Product-level economics for agentic commerce, stablecoin settlement, and Visa Direct | not disclosed | Long-run growth opportunities remain judgment-heavy. |
| FY2026 full-year actual results | ไม่พบข้อมูลที่ยืนยันได้ | Current model relies on Q2/6M actuals and management outlook. |

## Entity Update

Updated `wiki/entities/V.md` with this valuation memo link and valuation watch items. The valuation changes the decision read toward wait for new capital at current price despite strong business quality.
