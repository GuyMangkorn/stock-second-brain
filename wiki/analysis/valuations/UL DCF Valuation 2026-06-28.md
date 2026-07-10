---
type: analysis
analysis_type: dcf-valuation
ticker: UL
company: Unilever PLC
date: 2026-06-28
currency: EUR
source_files:
  - wiki/entities/UL.md
  - raw/financials/UL_fundamentals.md
  - raw/imports/UL_latest_results_source.md
tags:
  - analysis/dcf
  - ticker/UL
---

# UL DCF Valuation - 2026-06-28
Entity: [[UL]]

## Bottom Line

This DCF uses source-backed FY2025 free cash flow of EUR 5.921B, cash and cash equivalents of EUR 3.941B, total financial liabilities of EUR 28.278B, diluted average shares of 2,195.3M, fresh UL ADR close of USD 60.55 on 2026-06-26, StockAnalysis market cap of USD 131.45B, and EUR/USD 1.13904.

Base-case fair value is approximately **EUR 46.78 per share**, or **USD 53.28 per ADR-equivalent share**, about **12.0% downside** versus USD 60.55. Action implication: **WATCHLIST / WAIT**. Business quality is real, but current price does not offer enough margin of safety under a source-backed base case.

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| Entity page | `wiki/entities/UL.md` | Business model, thesis, risks, catalysts and source gaps. |
| Normalized facts | `raw/financials/UL_fundamentals.md` | Q1 2026 trading update, FY2025 annual baseline, FCF, cash, debt, shares, guidance and market data. |
| Latest results source note | `raw/imports/UL_latest_results_source.md` | Source map and extracted source facts. |
| Unilever Annual Report and Accounts 2025 / Form 20-F | https://www.unilever.com/files/unilever-annual-report-and-accounts-2025.pdf | FY2025 FCF, cash, debt, shares, segment data, capital allocation and value creation plan. |
| Unilever Q1 2026 Overview | https://www.unilever.com/investors/results-events/results-events-webcasts/overview-q1-2026/ | Latest trading update and FY2026 guidance. |
| StockAnalysis UL quote | https://stockanalysis.com/stocks/ul/ | Fresh ADR price, market cap and shares out checked 2026-06-28 Asia/Bangkok. |
| XE EUR/USD converter | https://www.xe.com/currencyconverter/convert/?Amount=1&From=EUR&To=USD | FX conversion checked 2026-06-28 07:58 UTC. |

## Input Table

Financial statement amounts are EUR billions unless noted.

| Input | Value | Source / Calculation |
|---|---:|---|
| Fresh UL ADR close used | USD 60.55 | StockAnalysis close on 2026-06-26; checked 2026-06-28 Asia/Bangkok. |
| Market capitalization | USD 131.45B | StockAnalysis UL quote. |
| EUR/USD | 1.13904 | XE, checked 2026-06-28 07:58 UTC. |
| Market cap converted to EUR | EUR 115.40B | 131.45 / 1.13904. |
| StockAnalysis shares out | 2.18B | StockAnalysis UL quote. |
| Diluted shares used in DCF | 2,195.3M | Unilever Annual Report 2025. |
| Estimated post-cancellation ordinary shares | 2,181.005M | Annual Report share table calculation. |
| Cash and cash equivalents | 3.941 | Unilever Annual Report 2025. |
| Current financial liabilities | 2.582 | Unilever Annual Report 2025. |
| Non-current financial liabilities | 25.696 | Unilever Annual Report 2025. |
| Total financial liabilities used as debt | 28.278 | 2.582 + 25.696. |
| Net debt reported by company | 23.076 | Unilever Annual Report 2025; includes other current financial assets in net debt bridge. |
| FY2025 FCF | 5.921 | Unilever Annual Report 2025. |
| FY2026 USG guidance | bottom end of 4%-6% guidance range | Unilever Q1 2026 Overview FAQ. |
| FY2026 volume growth guidance | at least 2% | Unilever Q1 2026 Overview FAQ. |
| FY2026 margin guidance | modest margin improvement versus 2025 | Unilever Q1 2026 Overview FAQ. |

## Base Case Assumptions

| Assumption | Bear | Base | Bull |
|---|---:|---:|---:|
| Starting FCF anchor | FY2025 FCF EUR 5.921B | FY2025 FCF EUR 5.921B | FY2025 FCF EUR 5.921B |
| Year 1 FCF growth | 0.0% | 4.0% | 6.0% |
| Year 2 FCF growth | 0.0% | 4.0% | 5.5% |
| Year 3 FCF growth | 1.0% | 3.5% | 5.0% |
| Year 4 FCF growth | 1.0% | 3.0% | 4.0% |
| Year 5 FCF growth | 1.0% | 3.0% | 3.5% |
| WACC | 8.5% | 7.5% | 7.0% |
| Terminal growth | 1.5% | 2.5% | 3.0% |

WACC basis: the vault reference range for Consumer Staples is 7%-8%. Base uses 7.5% because Unilever is a scaled staples company but has meaningful emerging-market exposure, leverage and portfolio-transition complexity. Bear uses 8.5%; bull uses 7.0% only if volume-led growth, Power Brands momentum and margin expansion prove durable.

Terminal growth basis: mature developed-market compounder range is 2.0%-3.0%; bear case uses 1.5% because of portfolio and FCF uncertainty, base uses 2.5%, and bull uses 3.0%.

## FCF Projection

Amounts are EUR billions.

| Year | Bear FCF | Base FCF | Bull FCF |
|---:|---:|---:|---:|
| FY2025 anchor | 5.921 | 5.921 | 5.921 |
| Year 1 | 5.921 | 6.158 | 6.276 |
| Year 2 | 5.921 | 6.404 | 6.622 |
| Year 3 | 5.980 | 6.628 | 6.953 |
| Year 4 | 6.040 | 6.827 | 7.231 |
| Year 5 | 6.101 | 7.032 | 7.484 |

Base case loosely tracks FY2026 guidance: low-to-mid single-digit USG, at least 2% volume growth and modest margin improvement. It does not assume a step-change in FCF because FY2025 FCF declined from FY2024 and Q1 2026 captured source did not include full cash flow.

## Valuation Summary

Amounts are EUR billions except per-share and USD conversion.

| Scenario | WACC | Terminal Growth | PV of Explicit FCF | PV of Terminal Value | Enterprise Value | Cash | Debt | Equity Value | Fair Value / Share | Fair Value / ADR-Equivalent USD | Upside / Downside vs USD 60.55 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Bear | 8.5% | 1.5% | 23.843 | 58.507 | 82.350 | 3.941 | 28.278 | 58.013 | 26.45 | 30.13 | -50.2% |
| Base | 7.5% | 2.5% | 26.616 | 100.091 | 126.707 | 3.941 | 28.278 | 102.370 | 46.78 | 53.28 | -12.0% |
| Bull | 7.0% | 3.0% | 28.472 | 134.040 | 162.512 | 3.941 | 28.278 | 138.175 | 64.34 | 73.28 | 21.0% |

## Sensitivity Matrix

Base projection fair value per ADR-equivalent share in USD.

| WACC / Terminal Growth | 2.0% | 2.5% | 3.0% |
|---:|---:|---:|---:|
| 6.5% | 61.93 | 69.81 | 79.93 |
| 7.5% | 48.31 | 53.28 | 59.35 |
| 8.5% | 38.89 | 42.27 | 46.26 |

## Sanity Checks

| Check | Result | Read |
|---|---:|---|
| Market FCF yield | 5.13% | Better than many defensive staples, but not enough alone when leverage and transition risk are included. |
| Market EV / FY2025 FCF | 23.60x | Premium multiple requires sustained volume growth and margin expansion. |
| Total financial liabilities / FY2025 FCF | 4.78x | Leverage burden is material for equity valuation. |
| Net debt / FY2025 FCF | 3.90x | Balance sheet is not distressed, but not a clean net-cash compounder. |
| Base DCF terminal value share of EV | 79.0% | Sensitive to WACC / terminal growth but below the 85%-90% warning zone. |
| Bull DCF terminal value share of EV | 82.5% | Bull case relies heavily on terminal assumptions. |

## What Would Change The Valuation

- FY2026 FCF above FY2025 with evidence that volume-led growth is converting to cash.
- Full Q1/H1 2026 statements confirming lower net debt or stronger working-capital conversion.
- Clearer pro forma portfolio economics after Ice Cream demerger and Foods transaction detail.
- A lower ADR price that lifts market FCF yield and creates a margin of safety.
- Verified ADR ratio/depositary detail if a precise ADR-to-ordinary-share bridge is needed.
- WACC changes from rates, FX, emerging-market risk, leverage or consumer staples risk premium.

## Missing / Unverified Data

| Data item | Status | Valuation impact |
|---|---|---|
| Q1 2026 full income statement, balance sheet and cash flow | not disclosed in captured source | P11 uses FY2025 FCF, cash, debt and shares. |
| Latest balance sheet after 2025-12-31 | not disclosed | Debt and cash may have changed after buybacks / portfolio actions. |
| Legal ADR-to-ordinary share ratio source | ไม่พบข้อมูลที่ยืนยันได้ | DCF output is labeled ADR-equivalent and cross-checked against market shares. |
| Capex-only annual line | ไม่พบข้อมูลที่ยืนยันได้ in extracted table | Uses company-reported FCF instead of deriving FCF. |
| Official Q1 2026 transcript / Q&A | ไม่พบข้อมูลที่ยืนยันได้ | Limits confidence on management detail behind guidance. |
| Investor-specific required return and position constraints | not provided | Prevents personalized sizing. |

## Entity Update

Updated `wiki/entities/UL.md` with the valuation watch item and current action read. Core action read is `WATCHLIST / WAIT`, because source-backed base valuation is below current market price and the latest Q1 source is not a full financial statement.
