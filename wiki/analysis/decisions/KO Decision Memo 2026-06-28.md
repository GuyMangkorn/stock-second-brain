---
type: analysis
analysis_type: decision-memo
ticker: KO
company: The Coca-Cola Company
date: 2026-06-28
currency: USD
decision: WAIT / AVOID-new-capital; HOLD only for existing defensive-quality allocation
source_files:
  - index.md
  - wiki/entities/KO.md
  - raw/financials/KO_fundamentals.md
  - raw/imports/KO_latest_results_source.md
  - raw/imports/KO_market_quote_2026-06-28.md
  - wiki/analysis/valuations/KO DCF Valuation 2026-06-28.md
tags:
  - analysis/decision-memo
  - ticker/KO
---

# KO Decision Memo - 2026-06-28
Entity: [[KO]]

## Action Read

**Action: WAIT / AVOID-new-capital at current price. HOLD only if this is already an existing defensive-quality allocation with acceptable sizing.**

KO เป็น excellent-quality consumer staples franchise แต่ current valuation ไม่เปิด margin of safety. Fresh price คือ USD 82.63 จาก 2026-06-26 close, market cap ประมาณ USD 355.5B, FY2026 guided FCF yield แค่ 3.43%, และ forward EV / guided FCF ประมาณ 31.8x. Base DCF จาก FY2026 FCF guidance ให้ fair value ประมาณ USD 51.53 ต่อ diluted share, หรือ downside ราว 37.6%.

ธุรกิจดีจริง แต่ราคาเรียกร้องให้ FCF guidance convert ได้ดีมากและให้ terminal assumptions ที่ใจดี. สำหรับ new capital ควรรอราคาที่ดีกว่านี้หรือหลักฐาน Q2/FY2026 ว่า FCF normalization แข็งแรงกว่าที่ model base case รับรู้.

## Current Price / Market Data Check

| Metric | Value | Source / Calculation |
|---|---:|---|
| Latest regular-session close checked | USD 82.63 on 2026-06-26 | MarketWatch KO quote page, checked 2026-06-28 Asia/Bangkok. |
| Market cap displayed by source | USD 355.54B | MarketWatch KO quote page. |
| Shares outstanding | 4,302.482M | KO Q1 2026 Form 10-Q shares outstanding at 2026-04-17. |
| Market cap calculated from filing shares | USD 355.51B | 82.63 * 4,302.482M. |
| Diluted shares used in DCF | 4,314M | KO Q1 2026 Form 10-Q. |
| Cash and short-term investments | USD 11.083B | KO Q1 2026 Form 10-Q. |
| Total debt used for valuation | USD 43.890B | 0.332B loans and notes + 4.493B current maturities + 39.065B long-term debt. |
| Net debt | USD 32.807B | 43.890 - 11.083. |
| FY2026 FCF guidance | approximately USD 12.2B | KO Q1 2026 earnings release. |
| Forward FCF yield | 3.43% | 12.2 / 355.51. |
| Forward EV / guided FCF | 31.83x | (355.51 + 43.89 - 11.083) / 12.2. |

## Evidence From Vault

| Evidence | Read | Source |
|---|---|---|
| Q1 2026 net operating revenues grew 12.07% YoY | Top-line momentum is strong. | `raw/financials/KO_fundamentals.md` |
| Q1 2026 operating income grew 71.48% YoY | Profit rebound is strong, but Q1 2025 base was weaker. | `raw/financials/KO_fundamentals.md` |
| Q1 2026 diluted EPS was USD 0.91 vs USD 0.55 | Earnings power improved materially. | KO Q1 2026 Form 10-Q. |
| Q1 2026 simple FCF was USD 1.755B | Positive cash start, but not enough alone to validate full-year guidance. | KO Q1 2026 Form 10-Q and calculation. |
| FY2026 FCF guidance is approximately USD 12.2B | Management expects major FCF normalization versus FY2025. | KO Q1 2026 earnings release. |
| FY2025 simple FCF was USD 5.296B | Highlights working-capital / normalization risk in the DCF anchor. | KO FY2025 Form 10-K. |
| Net debt / FY2026 guided FCF is about 2.69x | Balance sheet is manageable but material for equity valuation. | `raw/financials/KO_fundamentals.md` |

## Valuation Read

| Scenario | Fair Value / Share | Upside / Downside vs USD 82.63 | Read |
|---|---:|---:|---|
| Bear | USD 29.42 | -64.4% | If FCF misses guidance and WACC / terminal assumptions reset, downside is severe. |
| Base | USD 51.53 | -37.6% | Quality does not offset current valuation. |
| Bull | USD 80.57 | -2.5% | Requires low WACC, strong FCF growth, and 3.0% terminal growth; still not clearly above price. |

Valuation lens is DCF-led because FCF, cash, debt, shares, price, and guidance were freshly verified. Multiple read supports the same caution: forward EV / guided FCF of about 31.8x is demanding for a mature staples compounder.

## Bull Case

- KO has one of the strongest global beverage brand portfolios and distribution systems.
- Q1 2026 revenue, operating income, EPS, and FCF all improved materially versus Q1 2025.
- Management raised FY2026 organic revenue and comparable currency-neutral EPS guidance.
- FY2026 FCF guidance of about USD 12.2B, if achieved, would show strong normalization after weak FY2025 cash flow.
- Consumer staples defensiveness can justify a premium multiple in uncertain macro periods.

## Bear Case

- Fresh price implies only a 3.43% forward FCF yield on FY2026 guidance.
- Forward EV / guided FCF of about 31.8x leaves little room for guidance disappointment.
- FY2025 simple FCF was only USD 5.296B, so FY2026 FCF normalization remains a key proof point.
- Net debt of about USD 32.807B after cash/ST investments reduces equity value in DCF.
- Official earnings call transcript text was not accessible, limiting Q&A-level confidence.
- Currency and structural impacts can still pressure reported comparable EPS.

## Key Assumptions

| Assumption | Working choice | Why it matters |
|---|---|---|
| FCF basis | FY2026 FCF guidance of USD 12.2B | Best source-backed forward cash-flow anchor, but still guidance. |
| WACC | 7.5% base | Consumer Staples range is 7%-8%; KO quality supports the range, net debt and valuation sensitivity argue against going too low. |
| Terminal growth | 2.5% base | Mature developed-market compounder assumption. |
| New-money hurdle | Require margin of safety versus base DCF | Current price does not clear it. |
| Investor profile | Long-term investor, normal-sized position | Without cost basis/position size, memo avoids personalized trim/add sizing. |

## What Would Change The Decision

- Upgrade toward ADD if price falls materially below the base DCF value while business quality remains intact.
- Upgrade toward WATCHLIST / staged entry if FY2026 Q2 confirms FCF and organic growth are tracking above base assumptions and price also improves.
- Keep HOLD for existing allocation if KO continues compounding and position size is already appropriate.
- Downgrade toward TRIM if price rises further without FCF guidance improving, or if FY2026 FCF conversion weakens.
- Re-run P11 after Q2 2026 or full-year FY2026 results.

## Missing / Unverified Data

| Item | Status | Why it matters |
|---|---|---|
| Official Q1 2026 earnings call transcript text | ไม่พบข้อมูลที่ยืนยันได้ | Limits management Q&A detail. |
| Full FY2026 actual FCF | not disclosed | Current valuation depends on guidance conversion. |
| Detailed bridge from FY2025 FCF to FY2026 guided FCF | not disclosed | FY2026 guided FCF is much higher than FY2025 actual simple FCF. |
| Product/category-level profitability | not disclosed | Cannot underwrite detailed margin drivers. |
| Real-time quote after 2026-06-26 close | ไม่พบข้อมูลที่ยืนยันได้ | 2026-06-28 is Sunday; refresh price before future action changes. |
| Investor-specific cost basis, position size, tax status, and required return | not provided | Prevents personalized sizing. |

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| Entity page | `wiki/entities/KO.md` | Business model, thesis, risks, catalysts, source gaps. |
| Normalized financial facts | `raw/financials/KO_fundamentals.md` | Q1 2026 financial facts, FY2025 baseline, market data, cash, debt, FCF, guidance. |
| Latest results source note | `raw/imports/KO_latest_results_source.md` | P1 source discovery and extracted facts. |
| Market quote note | `raw/imports/KO_market_quote_2026-06-28.md` | Fresh price and market cap check. |
| DCF valuation memo | `wiki/analysis/valuations/KO DCF Valuation 2026-06-28.md` | Source-backed DCF scenarios and sensitivity. |
| KO Q1 2026 Form 10-Q | https://investors.coca-colacompany.com/filings-reports/all-sec-filings/content/0001628280-26-028802/ko-20260403.htm | Primary filing source. |
| KO Q1 2026 earnings release | https://investors.coca-colacompany.com/news-events/press-releases/detail/1158/coca-cola-reports-first-quarter-2026-results-and-updates-full-year-guidance | Official results and guidance. |
| KO FY2025 Form 10-K | https://investors.coca-colacompany.com/filings-reports/all-sec-filings/content/0001628280-26-010047/ko-20251231.htm | Annual baseline and historical FCF. |
| MarketWatch KO quote page | https://www.marketwatch.com/investing/stock/ko | Fresh market price and market cap. |
