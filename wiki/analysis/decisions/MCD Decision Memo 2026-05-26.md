---
type: analysis
analysis_type: decision-memo
ticker: MCD
company: McDonald's Corporation
date: 2026-05-26
currency: USD
decision: AVOID-new-capital / WATCHLIST; HOLD only for existing quality position with valuation tolerance
source_files:
  - index.md
  - wiki/entities/MCD.md
  - raw/financials/MCD_fundamentals.md
  - raw/imports/MCD_latest_results_source.md
  - wiki/analysis/valuations/MCD DCF Valuation 2026-05-26.md
tags:
  - analysis/decision-memo
  - ticker/MCD
---

# MCD Decision Memo - 2026-05-26

## Action Read

**Action: AVOID new capital / WATCHLIST. HOLD existing quality position only if the investor already owns it and accepts premium valuation risk.**

MCD เป็น business คุณภาพสูงมาก: global brand, 95% franchised restaurant base, recurring rent/royalty economics, digital and drive-thru advantages, and strong operating margin. Q1 2026 execution was solid with global comparable sales +3.8%, revenue +9.4%, and operating income +11.5%.

แต่ valuation ไม่ให้ช่องว่างพอ. ที่ USD 282.27 close on 2026-05-22, market cap is USD 200.55B and EV is USD 254.28B. TTM simple FCF is only USD 7.039B, so FCF yield is 3.51% and EV / TTM FCF is 36.1x. Base-case DCF gives about USD 125.32 per diluted share, far below current price.

## Current Price / Market Data Check

| Metric | Value | Source / Calculation |
|---|---:|---|
| Latest regular-session close checked | USD 282.27 on 2026-05-22 | StockAnalysis MCD quote page, checked 2026-05-26 Asia/Bangkok. |
| Latest after-hours quote noted | USD 282.24 on 2026-05-22 | StockAnalysis MCD quote page. |
| Shares outstanding | 710.51M | StockAnalysis statistics page. |
| Market cap | USD 200.55B | StockAnalysis market cap page. |
| Enterprise value | USD 254.28B | StockAnalysis statistics / market cap page. |
| Diluted shares used in DCF | 713.5M | Q1 2026 earnings release / Form 10-Q. |
| Cash and equivalents | USD 1.170B | Q1 2026 Form 10-Q. |
| Long-term debt | USD 40.105B | Q1 2026 Form 10-Q. |
| Long-term lease liability | USD 14.069B | Q1 2026 Form 10-Q. |
| TTM simple FCF | USD 7.039B | FY2025 FCF 7.186B - Q1 2025 FCF 1.877B + Q1 2026 FCF 1.730B. |
| FCF yield | 3.51% | 7.039 / 200.55. |
| Market EV / TTM FCF | 36.13x | 254.28 / 7.039. |

## Evidence From Vault

| Evidence | Read | Source |
|---|---|---|
| Q1 2026 global comparable sales grew 3.8% | Demand improved versus Q1 2025 decline. | `raw/financials/MCD_fundamentals.md` |
| Q1 2026 revenue grew 9.42% YoY | Top-line recovery is source-backed. | Q1 2026 Form 10-Q. |
| Q1 2026 operating margin was 45.31% | Franchise model remains highly profitable. | Calculation from Q1 2026 Form 10-Q. |
| Q1 2026 simple FCF fell 7.83% YoY | Higher capex is a real cash-flow drag. | Q1 2026 Form 10-Q and normalized facts. |
| 2026 capex guidance is USD 3.7B-3.9B | Restaurant development requires elevated reinvestment. | Q1 2026 Form 10-Q outlook. |
| 2026 FCF conversion guidance is low-to-mid 80% | Management still expects strong cash conversion, but no FCF dollar guide. | Q1 2026 Form 10-Q outlook. |
| Long-term debt plus lease liability is large relative to FCF | Balance sheet / lease burden constrains equity value. | Q1 2026 Form 10-Q. |

## Valuation Read

| Scenario | Fair Value / Share | Upside / Downside vs USD 282.27 | Read |
|---|---:|---:|---|
| Bear | USD 73.97 | -73.8% | If FCF grows slowly and WACC stays high, downside is severe. |
| Base | USD 125.32 | -55.6% | Base case does not support new capital. |
| Bull | USD 203.22 | -28.0% | Even optimistic assumptions remain below market price. |

Valuation is the decisive issue. MCD can remain a high-quality company and still be a poor new-money entry if the market is paying too much for durability.

## Bull Case

- Brand scale and franchised economics are unusually durable.
- Q1 2026 comparable sales improved across U.S., International Operated Markets, and International Developmental Licensed Markets.
- Operating margin remains in the mid-40% range.
- Digital, loyalty, delivery, drive-thru, and restaurant development can compound Systemwide sales.
- Management targets meaningful unit growth toward 50,000 restaurants by end-2027.
- Existing holders may benefit from compounding and dividend growth even if near-term upside is limited.

## Bear Case

- FCF yield is only 3.51%, which gives little margin of safety.
- Market EV / TTM FCF is about 36.1x, high for a mature restaurant operator.
- Debt and lease obligations are large relative to TTM FCF.
- Q1 FCF declined YoY because capex rose.
- Franchisee-level profitability is not disclosed, so system health cannot be fully underwritten from public facts.
- If consumer pressure hits traffic or value perception, premium valuation can compress quickly.

## Key Assumptions

| Assumption | Working choice | Why it matters |
|---|---|---|
| FCF basis | Simple `OCF - capex` | Company defines FCF this way and the inputs are source-backed. |
| Starting FCF | TTM FCF USD 7.039B | Avoids annualizing a single quarter. |
| WACC | 8.5% base | Consumer Discretionary reference range is 8%-10%; quality lowers the hurdle but leverage/leases keep it above defensive-staple levels. |
| Terminal growth | 2.5% base | Mature compounder assumption. |
| New-money hurdle | Require visible margin of safety | Current price does not clear base or bull DCF. |

## What Would Change The Decision

- Upgrade toward WATCHLIST / possible ADD if the share price falls enough to lift FCF yield and create margin of safety.
- Upgrade if FY2026 FCF dollars come in materially above TTM FCF while comparable sales and operating margin remain strong.
- Keep HOLD for existing positions if the investor values MCD as a defensive quality compounder and has a low cost basis.
- Downgrade toward TRIM if FCF conversion misses guidance, comparable sales weaken, or valuation remains high while debt/lease burden rises.
- Re-run DCF after Q2 2026 or if official full transcript / new guidance adds material context.

## Missing / Unverified Data

| Item | Status | Why it matters |
|---|---|---|
| Full FY2026 actual results | not disclosed | Need full-year FCF and margin outcome. |
| Official text transcript / full Q&A | ไม่พบข้อมูลที่ยืนยันได้ | Limits official Q&A context. |
| Forward FCF dollar guidance | not disclosed | DCF uses TTM FCF rather than a company FCF dollar guide. |
| Product-level profitability by menu category | not disclosed | Cannot underwrite menu category economics directly. |
| Franchisee-level profitability and leverage | not disclosed | Franchisee health is central to rent/royalty durability. |
| Exact current intraday price on 2026-05-26 | ไม่พบข้อมูลที่ยืนยันได้ | Latest available source price is 2026-05-22 close. |
| Investor-specific cost basis, position size, tax status, and required return | not provided | Prevents personalized sizing. |

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| Entity page | `wiki/entities/MCD.md` | Business model, thesis, risks, catalysts, source gaps. |
| Normalized financial facts | `raw/financials/MCD_fundamentals.md` | Q1 2026 financial facts, FY2025 baseline, market data, cash, debt, FCF, guidance. |
| Latest results source note | `raw/imports/MCD_latest_results_source.md` | Source map and extracted facts. |
| DCF valuation memo | `wiki/analysis/valuations/MCD DCF Valuation 2026-05-26.md` | Source-backed DCF scenarios and sensitivity. |
| McDonald's Q1 2026 Form 10-Q | https://www.sec.gov/Archives/edgar/data/63908/000006390826000051/mcd-20260331.htm | Primary Q1 filing source. |
| McDonald's Q1 2026 earnings release PDF | https://corporate.mcdonalds.com/content/dam/sites/corp/nfl/pdf/Q1%202026%20Exhibit%2099.1%20-%203.31.26.pdf | Official results release. |
| McDonald's FY2025 Form 10-K | https://www.sec.gov/Archives/edgar/data/63908/000006390826000035/mcd-20251231.htm | Annual baseline and historical FCF. |
| StockAnalysis MCD quote / market cap | https://stockanalysis.com/stocks/mcd/ | Fresh market data checked 2026-05-26. |
