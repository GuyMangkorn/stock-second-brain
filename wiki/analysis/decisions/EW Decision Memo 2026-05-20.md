---
type: decision-memo
ticker: EW
company: Edwards Lifesciences Corporation
date: 2026-05-20
action_read: WAIT / AVOID new capital at current price
current_price: 82.16
currency: USD
tags:
  - analysis/decision
  - ticker/EW
---

# EW Decision Memo - 2026-05-20
Entity: [[EW]]

## Action Read

`WAIT / AVOID new capital at current price`.

EW เป็น high-quality structural heart medtech business แต่ current price ที่ USD 82.16 ยังไม่ให้ margin of safety จาก source-backed DCF. สำหรับ portfolio ที่ถืออยู่แล้ว อาจจัดเป็น `HOLD / monitor` ได้ถ้า thesis คือ quality compounder และ tax basis ดี แต่สำหรับ new capital วันนี้ valuation ยังตึงเกินไป.

## Current Price / Market Data Check

| Item | Value | Source |
|---|---:|---|
| Current price | USD 82.16 | FinancialContent official close, 2026-05-19 4:10 PM EDT |
| Shares outstanding | 575.8M | Form 10-Q cover, as of 2026-04-30 |
| Calculated market cap | USD 47,307.7M | `82.16 * 575.8` |
| Cash plus short-term investments | USD 3,671.5M | Form 10-Q |
| Long-term debt | USD 598.5M | Form 10-Q |
| Net cash before lease liabilities | USD 3,073.0M | Calculation |
| TTM FCF | USD 1,089.5M | FY2025/Q1 source-backed calculation |
| Price / TTM FCF | 43.4x | `47,307.7 / 1,089.5` |

## Evidence From Vault

- Q1 2026 net sales grew 16.7% YoY to USD 1,648.6M, with all product groups growing.
- TAVR remains the core engine: USD 1,197.3M Q1 sales, 72.6% of Q1 revenue, and 14.4% YoY growth.
- TMTT is the fastest-growing reported product group: USD 175.1M Q1 sales, 51.9% YoY growth, but only 10.6% of Q1 sales.
- Balance sheet is strong: USD 3.67B cash plus short-term investments versus USD 0.60B long-term debt.
- FCF conversion is the weak current datapoint: Q1 2026 FCF was USD -21.1M versus USD 224.4M in Q1 2025, though FY2025 FCF was USD 1,335.0M.

## Valuation Read

P11 DCF base case gives fair value about USD 40/share using:

- TTM FCF base: USD 1,089.5M.
- FCF growth fade: 8%, 7%, 6%, 5%, 4%.
- WACC: 9.0%.
- Terminal growth: 2.5%.
- Net cash before lease liabilities: USD 3,073.0M.
- Shares: 575.8M.

เมื่อเทียบกับ USD 82.16 current price, base DCF downside ประมาณ 51%. Even if FY2025 FCF of USD 1,335.0M is used as the starting point, scenario fair value is about USD 48/share, still meaningfully below the current price. ดังนั้น decision ไม่ควร rely on "quality" อย่างเดียวโดยไม่ให้ price discipline.

## Bull Case

- Structural heart focus is attractive: TAVR is scaled, clinically important, and still grew double digit in Q1 2026.
- TMTT offers a credible growth option if repair/replacement adoption continues and centers scale procedures.
- Net cash balance sheet gives flexibility for R&D, acquisitions, and buybacks.
- FY2026 guidance was raised after Q1: company guided 9% to 11% constant-currency sales growth and adjusted EPS of USD 2.95 to USD 3.05.

## Bear Case

- Current multiple is demanding versus source-backed FCF.
- Q1 FCF was negative despite strong sales and earnings, so cash conversion must be watched closely.
- Product concentration in TAVR is high; evidence, guidelines, reimbursement, or competitive shifts can matter a lot.
- TMTT optionality is real but early; if the market is already capitalizing that future, execution risk is expensive.

## Key Assumptions

- Q1 working-capital pressure is not assumed to persist forever, but base valuation uses TTM FCF rather than smoothing it away.
- WACC of 9.0% is reasonable for a high-quality but innovation/regulatory-exposed Health Care equipment company.
- Terminal growth of 2.5% is appropriate for a mature developed-market compounder.
- No investor-specific tax basis, existing position size, or required return was provided, so action read is for new capital.

## What Would Change The Decision

- Price falls toward a valuation range with margin of safety, especially below or near conservative DCF fair value.
- Q2/Q3 2026 confirms FCF rebound and raises source-backed normalized FCF.
- Edwards discloses stronger FCF guidance or product economics that justify a materially higher FCF growth path.
- TMTT becomes large enough and profitable enough to change the long-term FCF slope, not only revenue growth.

## Missing / Unverified Data

- GAAP reconciliation for forward non-GAAP guidance is not provided.
- FY2026 full-year actual results are not yet available.
- Product-level profitability by TAVR, TMTT, and Surgical is not disclosed.
- Forward FCF guidance is not disclosed.
- Normalized recurring FCF after Q1 working-capital movements, divestiture effects, legal accrual timing, transition service arrangements, and ASR timing is not fully isolated.
- Exact share count after 2026-04-30 is not disclosed.
- Market quote is provider-sourced and should be refreshed before future action calls.
- Investor-specific position size, tax basis, required return, and portfolio constraints were not provided.

## Source Map

| Source | URL / Path | Role |
|---|---|---|
| [[EW_latest_results_source]] | `raw/imports/EW_latest_results_source.md` | P1 source note and handoff. |
| [[EW_fundamentals]] | `raw/financials/EW_fundamentals.md` | P4 normalized facts. |
| [[EW DCF Valuation 2026-05-20]] | `wiki/analysis/valuations/EW DCF Valuation 2026-05-20.md` | P11 valuation. |
| EW Q1 2026 Form 10-Q | https://www.sec.gov/Archives/edgar/data/1099800/000109980026000026/ew-20260331.htm | Latest filing data. |
| EW FY2025 Form 10-K | https://www.sec.gov/Archives/edgar/data/1099800/000109980026000009/ew-20251231.htm | Annual baseline. |
| EW Q1 2026 earnings release | https://ir.edwards.com/news/news-details/2026/Edwards-Lifesciences-Reports-First-Quarter-Results/default.aspx | Guidance. |
| FinancialContent quote | https://markets.financialcontent.com/stocks.ksnt/quote/detailedquote?Symbol=NY%3AEW | Current price check. |
