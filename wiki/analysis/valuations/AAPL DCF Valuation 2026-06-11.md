---
type: analysis
analysis_type: dcf-valuation
ticker: AAPL
company: Apple Inc.
date: 2026-06-11
currency: USD
source_files:
  - wiki/entities/AAPL.md
  - raw/financials/AAPL_fundamentals.md
  - raw/imports/AAPL_latest_results_source.md
  - raw/imports/AAPL_market_quote_2026-06-11.md
tags:
  - analysis/dcf
  - ticker/AAPL
---

# AAPL DCF Valuation - 2026-06-11

## Bottom Line

This DCF can be run because current price, market cap, shares, cash, debt, and FCF were freshly verified. Forward guidance was not verified from official Apple sources, so the valuation uses source-backed historical FCF plus explicit scenario assumptions rather than management guidance.

Using TTM Q2 FY2026 FCF of USD 129.174B, total cash and marketable securities of USD 146.595B, total debt of USD 84.711B, diluted shares of 14.768B, base WACC of 9.0%, terminal growth of 2.5%, and a mature-compounder FCF path, base-case fair value is approximately USD 153 per diluted share.

Against the fresh market-data price of USD 292.15 on 2026-06-10 at 1:01 PM EDT, the base case implies about 48% downside. Even the bull scenario reaches only about USD 229 per share. The practical valuation read is **AVOID new capital / HOLD only if already owned for quality and tax/sizing reasons**.

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| Entity page | `wiki/entities/AAPL.md` | Business model, thesis, risks, source map. |
| Normalized facts | `raw/financials/AAPL_fundamentals.md` | Q2 FY2026 financials, balance sheet, FCF, revenue mix, ratios. |
| Latest source note | `raw/imports/AAPL_latest_results_source.md` | Official-source extraction and ingest provenance. |
| Market quote note | `raw/imports/AAPL_market_quote_2026-06-11.md` | Fresh price, market cap, shares, and market-data provenance. |
| SEC Q2 FY2026 Form 10-Q | https://www.sec.gov/Archives/edgar/data/320193/000032019326000013/aapl-20260328.htm | Official quarterly facts, cash/debt, shares, and MD&A risk context. |
| SEC FY2025 Form 10-K | https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm | Annual baseline and annual cash-flow history. |
| StockAnalysis statistics | https://stockanalysis.com/stocks/aapl/statistics/ | Fresh market price, market cap, P/FCF, EV/FCF, and market-data cross-check. |

## Input Table

Company financial statement amounts are USD billions unless noted.

| Input | Value | Source / Calculation |
|---|---:|---|
| Fresh market price used | USD 292.15 | StockAnalysis statistics page, Jun 10, 2026 1:01 PM EDT. |
| Fresh market capitalization | USD 4.29T | StockAnalysis statistics page, checked 2026-06-10. |
| Shares outstanding | 14.69B | StockAnalysis statistics page; SEC cover page gives 14.687356B as of 2026-04-17. |
| Diluted shares used for DCF | 14.768B | SEC Q2 FY2026 Form 10-Q, 1H FY2026 weighted-average diluted shares. |
| Cash and cash equivalents | 45.572 | SEC Q2 FY2026 Form 10-Q. |
| Current marketable securities | 22.935 | SEC Q2 FY2026 Form 10-Q. |
| Non-current marketable securities | 78.088 | SEC Q2 FY2026 Form 10-Q. |
| Total cash and marketable securities | 146.595 | 45.572 + 22.935 + 78.088. |
| Total debt | 84.711 | Commercial paper 1.997 + current term debt 8.310 + non-current term debt 74.404. |
| Net cash used | 61.884 | 146.595 - 84.711. |
| 1H FY2026 operating cash flow | 82.627 | SEC Q2 FY2026 Form 10-Q. |
| 1H FY2026 capex spend | 4.344 | SEC Q2 FY2026 Form 10-Q, cash outflow converted to positive spend. |
| 1H FY2026 free cash flow | 78.283 | 82.627 - 4.344. |
| FY2025 operating cash flow | 111.482 | SEC FY2025 Form 10-K / StockAnalysis cross-check. |
| FY2025 capex spend | 12.715 | SEC FY2025 Form 10-K / StockAnalysis cross-check. |
| TTM operating cash flow | 140.222 | FY2025 111.482 - 1H FY2025 53.887 + 1H FY2026 82.627. |
| TTM capex spend | 11.048 | FY2025 12.715 - 1H FY2025 6.011 + 1H FY2026 4.344. |
| TTM free cash flow | 129.174 | 140.222 - 11.048. |
| Official forward guidance | not disclosed | No verified official forward revenue / EPS / FCF guidance in source set. |

## Base Case Assumptions

| Assumption | Bear | Base | Bull |
|---|---:|---:|---:|
| Starting reference | TTM FCF USD 129.174B | TTM FCF USD 129.174B | TTM FCF USD 129.174B |
| Year 1 FCF | 115.0 | 132.0 | 140.0 |
| Year 2 FCF | 118.0 | 139.0 | 152.0 |
| Year 3 FCF | 121.0 | 146.0 | 165.0 |
| Year 4 FCF | 124.0 | 153.0 | 178.0 |
| Year 5 FCF | 127.0 | 160.0 | 190.0 |
| WACC | 10.0% | 9.0% | 8.0% |
| Terminal growth | 2.0% | 2.5% | 3.0% |
| Interpretation | Product cycle normalizes and margins face component/tariff pressure. | Services and buybacks support steady FCF growth from a very large base. | iPhone cycle, Services, AI/device refresh, and margin resilience sustain stronger FCF growth. |

WACC basis: Apple is an Information Technology / consumer electronics platform with massive scale, net cash, and durable ecosystem advantages, but it also faces product-cycle, regulatory, AI, tariff, and component-cost risks. The vault reference range for Information Technology is 8%-12%; base WACC is 9.0%.

Terminal growth basis: 2.0%-3.0% matches the mature developed-market compounder range in `wiki/reference/valuation-assumptions.md`.

## FCF Projection

Amounts are USD billions.

| Year | Bear FCF | Base FCF | Bull FCF |
|---:|---:|---:|---:|
| TTM anchor | 129.174 | 129.174 | 129.174 |
| Year 1 | 115.000 | 132.000 | 140.000 |
| Year 2 | 118.000 | 139.000 | 152.000 |
| Year 3 | 121.000 | 146.000 | 165.000 |
| Year 4 | 124.000 | 153.000 | 178.000 |
| Year 5 | 127.000 | 160.000 | 190.000 |

Base case rationale: Apple already produces enormous FCF, so the key discipline is not extrapolating Q2 strength into unrealistic long-term growth. Services and buybacks can support per-share compounding, but official guidance was not verified and Apple flagged component/tariff/margin risks.

## Valuation Summary

Amounts are USD billions except per-share data.

| Scenario | WACC | Terminal Growth | PV of Explicit FCF | PV of Terminal Value | Enterprise Value | Net Cash | Equity Value | Fair Value / Diluted Share | Upside / Downside vs USD 292.15 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Bear | 10.0% | 2.0% | 456.526 | 1,005.427 | 1,461.953 | 61.884 | 1,523.837 | 103.18 | -64.7% |
| Base | 9.0% | 2.5% | 563.211 | 1,639.827 | 2,203.038 | 61.884 | 2,264.922 | 153.37 | -47.5% |
| Bull | 8.0% | 3.0% | 651.074 | 2,663.803 | 3,314.876 | 61.884 | 3,376.760 | 228.65 | -21.7% |

## Sensitivity Matrix

Base projection fair value per diluted share, USD.

| WACC / Terminal Growth | 2.0% | 2.5% | 3.0% |
|---:|---:|---:|---:|
| 8.0% | 168.72 | 180.79 | 195.27 |
| 9.0% | 144.93 | 153.37 | 163.21 |
| 10.0% | 127.10 | 133.26 | 140.31 |

## Sanity Checks

| Check | Result | Read |
|---|---:|---|
| Market cap / TTM FCF | 33.0x | USD 4.29T / USD 129.174B. This requires unusually strong long-term FCF growth for Apple's scale. |
| TTM FCF yield | 3.03% | Thin yield for a hardware-led company unless FCF per share compounds quickly. |
| EV/FCF | 32.6x | StockAnalysis market-data cross-check. |
| Base DCF terminal value share of EV | 74.4% | High but within mature DCF tolerance. |
| Bull DCF terminal value share of EV | 80.4% | Still assumption-sensitive. |
| Reverse DCF, base WACC/terminal growth | About 20.5% 5-year FCF CAGR required | Very demanding from a USD 129B FCF base. |
| Analyst target cross-check | USD 311.55 average target | Secondary market context is above current price, but it is not source-backed intrinsic value. |
| Guidance cross-check | not disclosed | No official forward guidance was verified; this lowers conviction in aggressive growth assumptions. |

## What Would Change The Valuation

- Fresh price declines below the base DCF range with a real margin of safety.
- Verified official guidance or results support sustained FCF growth well above the base path.
- Services growth and gross margin expand without regulatory or component-cost pressure.
- Apple discloses AI/device-refresh monetization that plausibly lifts FCF per share.
- Tariff/component risks ease without offsetting demand pressure.
- Buybacks remain large but occur at valuations closer to intrinsic value.

## Missing / Unverified Data

| Data item | Status | Valuation impact |
|---|---|---|
| Official Apple investor-relations Q2 FY2026 press release page | ไม่พบข้อมูลที่ยืนยันได้ | SEC 10-Q is sufficient for facts, but release/call tone is missing. |
| Official earnings-call transcript | ไม่พบข้อมูลที่ยืนยันได้ | Management tone and Q&A cannot be used as durable evidence. |
| Forward revenue, EPS, gross margin, capex, or FCF guidance | Not disclosed in verified source set | DCF uses explicit assumptions instead of management guidance. |
| AI-specific revenue or Apple Intelligence monetization | Not disclosed | AI optionality cannot be independently underwritten. |
| Product unit volumes and product-level margins below Products / Services | Not disclosed | Limits unit-economics analysis. |
| Q2 standalone operating cash flow and capex | Not disclosed in extracted official table | Valuation uses 1H and TTM FCF. |
| Investor-specific tax basis and position sizing | Not provided | Affects hold/trim choice for existing positions. |

## Entity Update

Updated `wiki/entities/AAPL.md` with valuation watch items and report link to `[[AAPL DCF Valuation 2026-06-11]]`. The valuation supports avoiding new capital at the fresh price unless the investor has a separate portfolio/tax reason to hold an existing quality position.
