---
type: analysis
analysis_type: dcf-valuation
ticker: META
company: Meta Platforms, Inc.
date: 2026-06-10
currency: USD
source_files:
  - wiki/entities/META.md
  - raw/financials/META_fundamentals.md
  - raw/imports/META_latest_results_source.md
  - raw/imports/META_market_quote_2026-06-10.md
tags:
  - analysis/dcf
  - ticker/META
---

# META DCF Valuation - 2026-06-10

## Bottom Line

This DCF can be run because the required inputs were freshly verified: current price, market cap, shares, cash, debt, FCF, and guidance. The result is not a clean buy signal, but it is also not an obvious avoid-at-any-price result.

Using TTM Q1 2026 company-method FCF of USD 45.637B, cash and marketable securities of USD 81.180B, long-term debt of USD 58.748B, diluted shares of 2.564B, a base WACC of 9.0%, terminal growth of 2.5%, and a five-year FCF recovery path after the 2026 capex step-up, base-case fair value is approximately USD 529 per diluted share.

Against the freshly checked Nasdaq price of USD 577.61 on 2026-06-10 at 12:52 PM ET, the base case implies about 8% downside. The bull case reaches about USD 1,033 per share, but it depends on FCF rising to USD 160B by Year 5 while terminal value carries 85% of EV. The practical read is **WAIT for new capital / HOLD existing quality position if sizing is normal**.

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| Entity page | `wiki/entities/META.md` | Business model, thesis, risks, source map. |
| Normalized facts | `raw/financials/META_fundamentals.md` | Q1 2026 financials, balance sheet, FCF, segments, ratios. |
| Latest source note | `raw/imports/META_latest_results_source.md` | Official-source extraction and ingest provenance. |
| Market quote note | `raw/imports/META_market_quote_2026-06-10.md` | Fresh price, market cap, shares, and market-data provenance. |
| SEC Q1 2026 Form 10-Q | https://www.sec.gov/Archives/edgar/data/1326801/000162828026028526/meta-20260331.htm | Official quarterly filing and share-count facts. |
| SEC Q1 2026 8-K Exhibit 99.1 | https://www.sec.gov/Archives/edgar/data/1326801/000162828026028364/meta-03312026xexhibit991.htm | Financial tables, FCF reconciliation, segment results, guidance. |
| SEC FY2025 Form 10-K | https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm | FY2025 annual baseline and risk context. |
| Nasdaq quote / summary APIs | https://api.nasdaq.com/api/quote/META/info?assetclass=stocks; https://api.nasdaq.com/api/quote/META/summary?assetclass=stocks | Fresh price and market cap checked 2026-06-10. |

## Input Table

All company financial statement amounts are USD billions unless noted.

| Input | Value | Source / Calculation |
|---|---:|---|
| Fresh market price used | USD 577.61 | Nasdaq quote API, Jun 10, 2026 12:52 PM ET. |
| Fresh market capitalization | USD 1.466T | Nasdaq summary API, checked 2026-06-10. |
| Shares outstanding | 2.538B | SEC Q1 2026 Form 10-Q cover facts: Class A 2.196B + Class B 0.342B as of 2026-04-24. |
| Diluted shares used for DCF | 2.564B | Q1 2026 weighted-average diluted shares from SEC 8-K Exhibit 99.1. |
| Cash and cash equivalents | 23.426 | SEC 8-K Exhibit 99.1. |
| Marketable securities | 57.754 | SEC 8-K Exhibit 99.1. |
| Cash + marketable securities | 81.180 | 23.426 + 57.754. |
| Long-term debt | 58.748 | SEC 8-K Exhibit 99.1. |
| Net cash used | 22.432 | 81.180 - 58.748. |
| Q1 2026 operating cash flow | 32.226 | SEC 8-K Exhibit 99.1. |
| Q1 2026 capex spend | 18.997 | Purchases of property and equipment, converted from cash outflow to positive spend. |
| Q1 2026 finance lease principal | 0.843 | SEC 8-K Exhibit 99.1. |
| Q1 2026 free cash flow | 12.386 | SEC 8-K Exhibit 99.1 company non-GAAP reconciliation. |
| TTM operating cash flow | 124.000 | FY2025 OCF 115.800 - Q1 2025 OCF 24.026 + Q1 2026 OCF 32.226. |
| TTM capex spend | 75.747 | FY2025 capex 69.691 - Q1 2025 capex 12.941 + Q1 2026 capex 18.997. |
| TTM finance lease principal | 2.616 | FY2025 2.524 - Q1 2025 0.751 + Q1 2026 0.843. |
| TTM free cash flow | 45.637 | 124.000 - 75.747 - 2.616. |
| FY2026 capex guidance | USD 125B-145B | SEC 8-K Exhibit 99.1, including principal payments on finance leases. |
| Q2 2026 revenue guidance | USD 58B-61B | SEC 8-K Exhibit 99.1. |
| FY2026 total expense guidance | USD 162B-169B | SEC 8-K Exhibit 99.1. |

## Base Case Assumptions

| Assumption | Bear | Base | Bull |
|---|---:|---:|---:|
| Starting reference | TTM FCF USD 45.637B | TTM FCF USD 45.637B | TTM FCF USD 45.637B |
| Year 1 FCF | 35.0 | 42.0 | 50.0 |
| Year 2 FCF | 40.0 | 52.0 | 70.0 |
| Year 3 FCF | 48.0 | 65.0 | 95.0 |
| Year 4 FCF | 58.0 | 82.0 | 125.0 |
| Year 5 FCF | 70.0 | 105.0 | 160.0 |
| WACC | 10.0% | 9.0% | 8.0% |
| Terminal growth | 2.0% | 2.5% | 3.0% |
| Interpretation | AI capex suppresses FCF and Reality Labs remains a heavy drag. | FCF troughs during the capex step-up, then recovers as FoA monetization and AI ad tools scale. | AI infrastructure creates high-return ad/product gains and FCF materially exceeds pre-step-up levels. |

WACC basis: Meta is primarily a Communication Services / internet advertising platform with a net-cash balance sheet and strong competitive position, but it also has regulatory risk, platform risk, Reality Labs losses, and an unusually large AI capex cycle. The vault reference range for Communication Services is 8%-10%; base WACC is 9.0%.

Terminal growth basis: 2.0%-3.0% matches the mature developed-market compounder range in `wiki/reference/valuation-assumptions.md`.

## FCF Projection

Amounts are USD billions.

| Year | Bear FCF | Base FCF | Bull FCF |
|---:|---:|---:|---:|
| TTM anchor | 45.637 | 45.637 | 45.637 |
| Year 1 | 35.000 | 42.000 | 50.000 |
| Year 2 | 40.000 | 52.000 | 70.000 |
| Year 3 | 48.000 | 65.000 | 95.000 |
| Year 4 | 58.000 | 82.000 | 125.000 |
| Year 5 | 70.000 | 105.000 | 160.000 |

Base case rationale: Q1 2026 revenue and operating income were strong, but management raised FY2026 capex guidance to USD 125-145B. The base case assumes FCF recovers from the capex step-up rather than extrapolating FY2025 FCF directly.

## Valuation Summary

Amounts are USD billions except per-share data.

| Scenario | WACC | Terminal Growth | PV of Explicit FCF | PV of Terminal Value | Enterprise Value | Net Cash | Equity Value | Fair Value / Diluted Share | Upside / Downside vs USD 577.61 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Bear | 10.0% | 2.0% | 184.018 | 554.172 | 738.191 | 22.432 | 760.623 | 296.65 | -48.6% |
| Base | 9.0% | 2.5% | 258.825 | 1,076.136 | 1,334.961 | 22.432 | 1,357.393 | 529.40 | -8.3% |
| Bull | 8.0% | 3.0% | 382.496 | 2,243.202 | 2,625.698 | 22.432 | 2,648.130 | 1,032.81 | 78.8% |

## Sensitivity Matrix

Base projection fair value per diluted share, USD.

| WACC / Terminal Growth | 2.0% | 2.5% | 3.0% |
|---:|---:|---:|---:|
| 8.0% | 586.61 | 632.22 | 686.95 |
| 9.0% | 497.52 | 529.40 | 566.60 |
| 10.0% | 430.92 | 454.23 | 480.87 |

## Sanity Checks

| Check | Result | Read |
|---|---:|---|
| Market cap / TTM FCF | 32.1x | USD 1.466T / USD 45.637B. Demanding, but not as extreme as some AI infrastructure peers. |
| TTM FCF yield on market cap | 3.11% | Requires strong FCF recovery to be attractive for new capital. |
| Approximate market EV / TTM FCF | 31.6x | Market cap minus net cash divided by TTM FCF. |
| Base DCF terminal value share of EV | 80.6% | High but below the 85%-90% warning zone. |
| Bull DCF terminal value share of EV | 85.4% | In the warning zone; bull case is terminal-value-sensitive. |
| Reverse DCF, base WACC/terminal growth | About 19.8% 5-year FCF CAGR required | Starting from TTM FCF of USD 45.637B, matching USD 577.61 requires strong but not impossible FCF growth. |
| Net income quality | Mixed | Q1 2026 includes USD 8.03B tax benefit; FCF is cleaner for valuation. |
| Guidance cross-check | Cautious | FY2026 capex guidance rose to USD 125-145B, directly pressuring near-term FCF. |

## What Would Change The Valuation

- Evidence that FY2026 capex is peaking rather than continuing to rise.
- TTM FCF moving toward or above the base path despite high capex.
- Official disclosure that AI ad tools and business messaging are producing high incremental ROI.
- Reality Labs losses narrowing without sacrificing long-term optionality.
- A share price below base-case value with a margin of safety.
- A capex guidance increase without offsetting revenue/FCF evidence would pressure the valuation.

## Missing / Unverified Data

| Data item | Status | Valuation impact |
|---|---|---|
| Product-level AI revenue, AI ad-tool revenue, Meta AI revenue, and AI infrastructure ROI | Not disclosed | Cannot directly underwrite AI payback. |
| Reality Labs unit economics and product-level margins | Not disclosed | Cannot know whether optionality deserves a high value or should be treated as a drag. |
| Segment-level FCF | Not disclosed | FoA cash generation and Reality Labs cash burn are not separable. |
| Full FY2026 cash flow | ไม่พบข้อมูลที่ยืนยันได้ | Q1 2026 and TTM are the freshest verified cash-flow facts. |
| Exact remaining-quarter 2026 capex cadence | Not disclosed | Important for near-term FCF trough timing. |
| Investor-specific tax basis and position sizing | Not provided | Affects hold/trim decision for existing positions. |

## Entity Update

Updated `wiki/entities/META.md` with valuation watch items and report link to `[[META DCF Valuation 2026-06-10]]`. The valuation supports a wait-for-margin-of-safety action for new capital while keeping Meta on the quality watchlist.
