---
type: valuation
ticker: EW
company: Edwards Lifesciences Corporation
date: 2026-05-20
valuation_type: DCF
action_context: full new-ticker decision-grade flow P11
currency: USD
tags:
  - analysis/valuation
  - ticker/EW
---

# EW DCF Valuation - 2026-05-20

## Bottom Line

Base DCF ให้ fair value ประมาณ USD 40/share เทียบกับ current price USD 82.16. ดังนั้น P11 อ่านว่า valuation ไม่ให้ margin of safety สำหรับ new capital แม้ business quality และ growth profile ของ EW จะดี.

ตัวเลขนี้ไม่ใช่ company-disclosed fact. เป็น scenario valuation ที่ใช้ source-backed TTM FCF, net cash, share count, และ guidance ที่ verify แล้ว. จุดเปราะคือ Q1 2026 FCF ติดลบจาก working-capital movement จึงทำให้ TTM FCF ต่ำกว่า FY2025 FCF; ถ้าใช้ FY2025 FCF เป็น starting base แทน fair value scenario จะขึ้นเป็นประมาณ USD 48/share แต่ยังต่ำกว่าราคาปัจจุบันมาก.

## Source Map

| Source | URL / Path | Used For |
|---|---|---|
| EW Q1 2026 Form 10-Q | https://www.sec.gov/Archives/edgar/data/1099800/000109980026000026/ew-20260331.htm | Cash, short-term investments, debt, shares, Q1 FCF, product sales. |
| EW FY2025 Form 10-K | https://www.sec.gov/Archives/edgar/data/1099800/000109980026000009/ew-20251231.htm | FY2025 annual FCF and annual financial baseline. |
| EW Q1 2026 earnings release | https://ir.edwards.com/news/news-details/2026/Edwards-Lifesciences-Reports-First-Quarter-Results/default.aspx | FY2026 sales / EPS / product guidance. |
| FinancialContent quote | https://markets.financialcontent.com/stocks.ksnt/quote/detailedquote?Symbol=NY%3AEW | Fresh current price check: USD 82.16 close on 2026-05-19. |
| Vault normalized facts | [[EW_fundamentals]] | Normalized source-backed financial facts. |

## Input Table

| Input | Value | Source / Calculation |
|---|---:|---|
| Current price | USD 82.16 | FinancialContent quote search result, official close 2026-05-19 |
| Shares outstanding | 575.8M | Form 10-Q cover, as of 2026-04-30 |
| Calculated market cap | USD 47,307.7M | `82.16 * 575.8` |
| Cash and short-term investments | USD 3,671.5M | `2,445.5 cash + 1,226.0 short-term investments` |
| Long-term debt | USD 598.5M | Form 10-Q |
| Net cash before lease liabilities | USD 3,073.0M | `3,671.5 - 598.5` |
| FY2025 FCF | USD 1,335.0M | `1,595.2 OCF - 260.2 capex spend` |
| Q1 2025 FCF | USD 224.4M | `280.4 OCF - 56.0 capex spend` |
| Q1 2026 FCF | USD -21.1M | `43.8 OCF - 64.9 capex spend` |
| TTM FCF base | USD 1,089.5M | `1,335.0 - 224.4 - 21.1` |
| FY2026 sales guidance | USD 6.5B to USD 6.9B | Earnings release |
| FY2026 adjusted EPS guidance | USD 2.95 to USD 3.05 | Earnings release |

## Base Case Assumptions

| Assumption | Base Case | Rationale |
|---|---:|---|
| Starting FCF | USD 1,089.5M | TTM FCF from verified FY2025 and Q1 2026/Q1 2025 periods. |
| Year 1 FCF growth | 8.0% | Below FY2026 constant-currency sales growth guidance of 9% to 11% because Q1 FCF conversion was weak. |
| Year 2 FCF growth | 7.0% | Growth fades as TAVR base gets larger and TMTT remains early. |
| Year 3 FCF growth | 6.0% | Conservative fade toward mature medtech growth. |
| Year 4 FCF growth | 5.0% | Continued fade. |
| Year 5 FCF growth | 4.0% | Near terminal transition. |
| WACC | 9.0% | Health Care range is 8% to 10%; use 9% for medtech/regulatory/pipeline risk despite net cash. |
| Terminal growth | 2.5% | Mature developed-market compounder range from vault valuation reference. |

## FCF Projection

| Year | FCF | Growth |
|---|---:|---:|
| Base TTM | 1,089.5 | n/a |
| Year 1 | 1,176.7 | 8.0% |
| Year 2 | 1,259.0 | 7.0% |
| Year 3 | 1,334.6 | 6.0% |
| Year 4 | 1,401.3 | 5.0% |
| Year 5 | 1,457.3 | 4.0% |

## Valuation Summary

| Component | Value |
|---|---:|
| PV of explicit FCF | 5,109.6 |
| PV of terminal value | 14,936.2 |
| Enterprise value | 20,045.9 |
| Cash and short-term investments | 3,671.5 |
| Less long-term debt | (598.5) |
| Equity value | 23,118.9 |
| Shares outstanding | 575.8 |
| Fair value / share | USD 40.15 |
| Current price | USD 82.16 |
| Implied upside/downside | -51.1% |

## Sensitivity Matrix

Fair value per share, USD. Base case is WACC 9.0% and terminal growth 2.5%.

| WACC \ Terminal Growth | 2.0% | 2.5% | 3.0% |
|---:|---:|---:|---:|
| 8.0% | 43.7 | 46.6 | 49.9 |
| 9.0% | 38.2 | 40.2 | 42.4 |
| 10.0% | 34.0 | 35.5 | 37.1 |

## Sanity Checks

- Terminal value is about 74.5% of EV, within but still meaningfully assumption-sensitive.
- Current market cap of USD 47.3B is about 43.4x TTM FCF of USD 1.09B.
- FY2025 FCF base scenario gives fair value about USD 48/share using the same growth/WACC/terminal assumptions, still below the current quote.
- Net cash is material at about USD 3.1B, but it is not enough to bridge the gap between DCF value and market price.
- The valuation is conservative because it does not give extra credit for TMTT optionality beyond the explicit FCF growth fade. That optionality needs stronger source-backed FCF conversion before I would capitalize it aggressively.

## What Would Change The Valuation

- Q2/Q3 2026 FCF rebound that confirms Q1 working-capital pressure was temporary.
- TMTT growth and margin contribution large enough to justify higher FCF growth than the 8% to 4% fade used here.
- Evidence that normalized annual FCF is sustainably closer to, or above, FY2025 FCF despite divestiture and working-capital noise.
- Lower price, higher cash balance, lower share count, or new guidance that directly supports higher FCF.

## Missing / Unverified Data

- Forward FCF guidance is not disclosed.
- GAAP reconciliation for forward non-GAAP guidance is not provided.
- Product-level profitability and product-level capex are not disclosed.
- Exact share count after 2026-04-30 is not disclosed.
- Normalized recurring FCF after Q1 working-capital, legal accrual, transition service, divestiture, and ASR timing effects is not fully isolated.
- Investor-specific required return was not provided; WACC uses vault reference ranges.

## Entity Update

Updated `[[EW]]` with valuation watch items and linked this memo. Thesis impact: valuation is the main blocker. Action read should be `WAIT / AVOID new capital at current price` unless the investor has a non-valuation strategic reason or a much lower required return.
