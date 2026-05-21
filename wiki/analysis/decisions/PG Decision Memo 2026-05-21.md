---
type: analysis
analysis_type: decision-memo
ticker: PG
company: The Procter & Gamble Company
date: 2026-05-21
currency: USD
decision: WAIT / HOLD-existing-quality; avoid new capital without margin of safety
source_files:
  - index.md
  - wiki/entities/PG.md
  - raw/financials/PG_fundamentals.md
  - raw/imports/PG_latest_results_source.md
  - wiki/analysis/valuations/PG DCF Valuation 2026-05-21.md
tags:
  - analysis/decision-memo
  - ticker/PG
---

# PG Decision Memo - 2026-05-21

## Action Read

**Action: WAIT for new capital / HOLD existing quality position. Avoid adding unless price gives clearer margin of safety or FY2026/FY2027 evidence improves.**

P&G เป็น high-quality defensive compounder ที่เหมาะกับ watchlist ระยะยาว: Q3 FY2026 reported sales +7%, organic sales +3%, YTD simple FCF โต 9.8%, balance sheet ไม่ตึง, และ cash return plan ยังแข็งแรง. แต่ valuation ตอนนี้ไม่ใจดี. ที่ USD 142.44, stock ให้ TTM FCF yield แค่ 4.53% และ base-case DCF ได้ fair value ประมาณ USD 133.34 ต่อ diluted share, ต่ำกว่าราคาปัจจุบันราว 6.4%.

สำหรับ existing position: **HOLD** ได้ถ้าเป้าคือ defensive quality, dividend compounding, และ portfolio stability. สำหรับ new money: **WAIT / AVOID-new-capital** จนกว่าจะมี valuation cushion หรือ evidence ว่า margin recovery และ organic growth ดีกว่า base case.

## Current Price / Market Data Check

| Metric | Value | Source / Calculation |
|---|---:|---|
| Latest regular-session close checked | USD 142.44 on 2026-05-20 | Stooq PG quote CSV, fetched 2026-05-21 Asia/Bangkok. |
| Shares outstanding | 2,328.599M | P&G Q3 FY2026 Form 10-Q shareholders' equity table. |
| Market cap | USD 331.69B | 142.44 * 2,328.599M. |
| Diluted shares used in DCF | 2,416.5M | P&G Q3 FY2026 diluted weighted-average shares. |
| Cash and equivalents | USD 12.306B | P&G Q3 FY2026 Form 10-Q. |
| Total debt | USD 37.026B | Debt due within one year 13.174B + long-term debt 23.852B. |
| Net debt | USD 24.720B | 37.026 - 12.306. |
| TTM simple FCF | USD 15.028B | FY2025 FCF 14.044B - 9M FY2025 FCF 10.055B + 9M FY2026 FCF 11.039B. |
| FCF yield | 4.53% | 15.028 / 331.69. |
| Market EV / TTM FCF | 23.72x | (331.69 + 37.026 - 12.306) / 15.028. |

## Evidence From Vault

| Evidence | Read | Source |
|---|---|---|
| Q3 FY2026 net sales grew 7.38% reported | Top-line momentum is solid. | `raw/financials/PG_fundamentals.md` |
| Q3 FY2026 organic sales grew 3% | Core growth is positive but still low-single-digit. | P&G Q3 FY2026 earnings release. |
| Gross margin fell 150 bps reported; core gross margin fell 100 bps | Margin pressure remains central to the debate. | P&G Q3 FY2026 earnings release. |
| FY2026 YTD simple FCF grew 9.79% YoY | Cash conversion supports quality thesis. | P&G Form 10-Q and normalized facts. |
| Net debt / TTM FCF is about 1.64x | Balance sheet is manageable. | `raw/financials/PG_fundamentals.md` |
| FY2026 core EPS guide is USD 6.83 to USD 7.09 | Management maintained range but expects lower-end result. | P&G Q3 FY2026 earnings release. |
| Planned FY2026 cash returns are about USD 10B dividends and USD 5B buybacks | Capital return remains a durable part of the thesis. | P&G Q3 FY2026 earnings release. |

## Valuation Read

| Scenario | Fair Value / Share | Upside / Downside vs USD 142.44 | Read |
|---|---:|---:|---|
| Bear | USD 85.00 | -40.3% | If margin pressure persists and terminal assumptions reset lower, downside is material. |
| Base | USD 133.34 | -6.4% | Quality is not enough to create margin of safety at current price. |
| Bull | USD 179.70 | +26.2% | Requires premium WACC, 3% terminal growth, and stronger FCF compounding. |

Valuation is the main reason to wait. PG can be a durable holding, but new-money returns depend heavily on terminal assumptions because base DCF terminal value is already about 80.8% of EV.

## Bull Case

- P&G has one of the strongest global daily-use brand portfolios in consumer staples.
- Q3 FY2026 sales growth was broad across segments, and organic sales remained positive.
- YTD FCF growth and manageable leverage support dividends and buybacks.
- Productivity savings can gradually offset tariffs, commodities, mix, and reinvestment.
- If FY2027 guidance improves, PG could deserve a persistent premium multiple.
- Defensive quality has portfolio value during macro uncertainty.

## Bear Case

- Current FCF yield is only 4.53%, leaving limited valuation cushion.
- Q3 gross margin and operating margin were pressured despite sales growth.
- Management expects FY2026 EPS toward the lower end of guidance.
- Forward adjusted FCF dollar amount is not disclosed, so DCF must rely on TTM FCF and assumptions.
- Product/category-level profitability is not disclosed, limiting ability to isolate the best and weakest profit pools.
- If rates stay higher or staples multiples compress, fair value could move closer to bear/base cases.

## Key Assumptions

| Assumption | Working choice | Why it matters |
|---|---|---|
| FCF basis | Simple `OCF - capex` | Source-backed and comparable across annual/YTD periods. |
| WACC | 7.0% base | Consumer Staples reference range is 7%-8%; PG quality supports lower end, but valuation sensitivity remains high. |
| Terminal growth | 2.5% base | Mature developed-market compounder assumption; not heroic but still important to value. |
| New-money hurdle | Require visible margin of safety | Current base DCF does not clear it. |
| Investor profile | Long-term investor, normal-sized position | Without cost basis/position size, memo avoids personalized trim/add sizing. |

## What Would Change The Decision

- Upgrade toward ADD if price falls meaningfully below base fair value while company facts stay intact.
- Upgrade toward ADD if FY2026 full-year or FY2027 guidance shows stronger organic growth, margin recovery, and FCF above current TTM anchor.
- Keep HOLD if business quality remains intact but valuation stays premium.
- Downgrade toward TRIM / AVOID if margin pressure persists, EPS/FCF guidance weakens, or FCF yield compresses further without growth acceleration.
- Re-run DCF after FY2026 Q4 / full-year results.

## Missing / Unverified Data

| Item | Status | Why it matters |
|---|---|---|
| Full FY2026 actual results | not disclosed | Need full-year FCF and margin outcome. |
| Official company-hosted full earnings call transcript | ไม่พบข้อมูลที่ยืนยันได้ | Limits official Q&A context. |
| Product/category-level profitability below reportable segments | not disclosed | Cannot underwrite brand/category economics directly. |
| Forward adjusted FCF dollar amount | not disclosed | DCF uses TTM FCF rather than a company FCF dollar guide. |
| Exact realized tariff / commodity impact after Q3 | not disclosed | Important for margin recovery. |
| Market data after 2026-05-20 close | ไม่พบข้อมูลที่ยืนยันได้ | Refresh price before future action changes. |
| Investor-specific cost basis, position size, tax status, and required return | not provided | Prevents personalized sizing. |

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| Entity page | `wiki/entities/PG.md` | Business model, thesis, risks, catalysts, source gaps. |
| Normalized financial facts | `raw/financials/PG_fundamentals.md` | Q3 FY2026 financial facts, FY2025 baseline, market data, cash, debt, FCF, guidance. |
| Latest results source note | `raw/imports/PG_latest_results_source.md` | Source map and extracted facts. |
| DCF valuation memo | `wiki/analysis/valuations/PG DCF Valuation 2026-05-21.md` | Source-backed DCF scenarios and sensitivity. |
| P&G Q3 FY2026 Form 10-Q | https://www.sec.gov/Archives/edgar/data/80424/000008042426000060/pg-20260331.htm | Primary filing source. |
| P&G Q3 FY2026 earnings release | https://www.pginvestor.com/news/news-details/2026/PG-Announces-Fiscal-Year-2026-Third-Quarter-Results/default.aspx | Official results and guidance. |
| P&G FY2025 Annual Report / Form 10-K PDF | https://www.sec.gov/Archives/edgar/data/0000080424/000119312525191752/d879413dars.pdf | Annual baseline and historical FCF. |
| Stooq PG quote CSV | https://stooq.com/q/l/?s=pg.us&f=sd2t2ohlcv&h&e=csv | Fresh market price. |
