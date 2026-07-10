---
type: entity
ticker: KO
company: The Coca-Cola Company
market: NYSE
currency: USD
period_type: quarterly + annual
reporting_scope: Q1 2026 and FY2025 annual baseline
latest_period: Q1 2026
latest_period_end: 2026-04-03
latest_total_revenue_usd_m: 12472
latest_net_income_usd_m: 3966
source_gap_count: 6
source_gaps:
  - Official Q1 2026 earnings call transcript text was not accessible in this session.
  - Product/category-level profitability is not disclosed.
  - Sequential quarterly line-item trend was not normalized.
  - Detailed bridge from FY2025 FCF to FY2026 FCF guidance is not disclosed.
  - Real-time quote after the 2026-06-26 close is not available because 2026-06-28 is a Sunday.
  - Investor-specific position size, cost basis, tax status, and required return were not provided.
source_notes:
  - raw/imports/KO_latest_results_source.md
  - raw/imports/KO_market_quote_2026-06-28.md
normalized_markdown: raw/financials/KO_fundamentals.md
normalized_json: raw/financials/KO_fundamentals.json
tags:
  - entity/company
  - ticker/KO
---

# KO - The Coca-Cola Company

## Snapshot

| Item | Value |
|---|---|
| Ticker | KO |
| Company | The Coca-Cola Company |
| Market | NYSE |
| Currency | USD |
| Latest period | Q1 2026, quarter ended 2026-04-03 |
| Reporting scope | Q1 2026 and FY2025 annual baseline |
| Latest regular-session close | USD 82.63 on 2026-06-26 |
| Market cap | USD 355.54B from MarketWatch; USD 355.51B calculated from filing shares |
| Normalized file | `raw/financials/KO_fundamentals.md` |

## Source Map

| Priority | Source | Status | Notes |
|---:|---|---|---|
| 1 | SEC / official filings | Complete for Q1 2026 and FY2025 baseline | Q1 2026 Form 10-Q and FY2025 Form 10-K used for statements, shares, cash, debt, annual trend, and segments. |
| 2 | Earnings transcript | Partial / blocked | Official transcript PDF link was discovered, but text access was blocked in this session; not used as evidence. |
| 3 | Financial statements / metrics | Complete for normalized scope | Company filing values and official FY2026 guidance used; MarketWatch used only for current market data. |
| 4 | News / web context | Not needed | Decision did not require news beyond official results and fresh market quote. |

## Business Model

The Coca-Cola Company เป็น global beverage company ที่มี economics หลักจาก brands, concentrate / syrup system, finished products, bottling partners, และ global distribution reach. Quality ของธุรกิจมาจาก scale, brand portfolio, pricing power, repeat consumption, และ asset-light concentrate economics บางส่วน แต่ balance sheet ใช้ debt สูงพอสมควรเมื่อเทียบกับ FY2026 guided FCF.

FY2025 Form 10-K เป็น annual baseline สำหรับ business model; Q1 2026 Form 10-Q และ earnings release เป็น latest operating evidence.

## Segments / Revenue Mix

| Segment | Q1 2026 Revenue | Mix | YoY Change | Read |
|---|---:|---:|---:|---|
| Europe, Middle East & Africa | 2,807 | 22.51% | 26.96% | Strong reported growth; check currency / structural impacts before extrapolating. |
| Latin America | 1,678 | 13.45% | 9.10% | Healthy reported growth. |
| North America | 4,891 | 39.21% | 10.98% | Largest revenue region; important for valuation durability. |
| Asia Pacific | 1,426 | 11.43% | 3.78% | Positive but slower reported growth. |
| Bottling Investments | 1,638 | 13.13% | 4.40% | Lower-margin / structurally different economics than concentrate-heavy operations. |
| Corporate | 32 | 0.26% | 6.67% | Small residual line. |

## Financial Facts

| Metric | Latest Value | Source / Calculation |
|---|---:|---|
| Q1 2026 net operating revenues | USD 12.472B | Q1 2026 Form 10-Q. |
| Q1 2026 operating income | USD 4.359B | Q1 2026 Form 10-Q. |
| Q1 2026 net income | USD 3.966B | Q1 2026 Form 10-Q. |
| Q1 2026 diluted EPS | USD 0.91 | Q1 2026 Form 10-Q. |
| Q1 2026 simple FCF | USD 1.755B | Operating cash flow 2.021B - capex 0.266B. |
| FY2025 simple FCF | USD 5.296B | Operating cash flow 7.408B - capex 2.112B. |
| FY2026 FCF guidance | approximately USD 12.2B | Q1 2026 earnings release. |
| Cash and short-term investments | USD 11.083B | Q1 2026 Form 10-Q. |
| Total debt used for valuation | USD 43.890B | Loans and notes payable + current maturities + long-term debt. |
| Net debt used for valuation | USD 32.807B | 43.890B - 11.083B. |
| Diluted shares used for DCF | 4.314B | Q1 2026 Form 10-Q. |

## Charts

See `raw/financials/KO_fundamentals.md` for source-backed chart blocks:

- Quarterly YoY Comparison
- Annual Trend
- Segment Revenue Chart
- Cash Flow And Capex Chart
- Balance Sheet Snapshot Chart

## Transcript / Management Commentary

- Official Q1 2026 release says management raised full-year 2026 organic revenue and comparable currency-neutral EPS guidance after Q1 performance.
- FY2026 guidance: organic revenue growth 5% to 6%; comparable currency-neutral EPS growth 8% to 10%; operating cash flow approximately USD 14.4B; capex approximately USD 2.2B; free cash flow approximately USD 12.2B.
- Official transcript text remains a gap; no Q&A claims are used.

## Thesis

### Bull Case

KO เป็น high-quality consumer staples compounder: brand moat ใหญ่, global distribution แข็งแรง, Q1 2026 revenue +12.1% YoY, operating income +71.5% YoY, และ management raised FY2026 organic revenue / comparable currency-neutral EPS guidance. ถ้า FY2026 FCF guidance USD 12.2B convert ได้จริง และ organic growth อยู่ในกรอบ 5%-6%, business quality ยังรองรับ premium multiple ได้.

### Bear Case

Valuation คือปัญหาหลัก. ที่ USD 82.63 และ market cap ประมาณ USD 355.5B, FY2026 guided FCF yield มีเพียง 3.43% และ forward EV / guided FCF ประมาณ 31.8x. DCF base case จาก source-backed guidance ยังให้ fair value ต่ำกว่าราคาตลาดมาก. FY2025 FCF ต่ำเพราะ working-capital drag ทำให้ฐาน cash-flow มีความผันผวน และ net debt / guided FCF ประมาณ 2.69x.

### Key Debate

Debate หลักไม่ใช่ว่า KO เป็นธุรกิจดีหรือไม่ แต่คือราคาปัจจุบันจ่าย premium มากเกินไปหรือยัง. Investor ต้องเห็น either ราคาอ่อนลง, FCF conversion ชัดขึ้น, หรือ FY2027 growth/margin evidence ดีกว่า base case ก่อนเพิ่ม new capital.

## Risks

- Valuation risk จาก FCF yield ต่ำและ EV / guided FCF สูง.
- Currency and structural headwinds can offset comparable currency-neutral growth.
- FY2026 FCF guidance depends on working-capital normalization after weak FY2025 OCF.
- High net debt relative to guided FCF reduces financial flexibility versus net-cash compounders.
- Bottling Investments economics may dilute company-level margins versus pure concentrate economics.
- Transcript Q&A was unavailable, limiting management-color confidence.

## Catalysts

- FY2026 Q2 results confirming organic revenue growth and EPS resilience.
- Full-year FY2026 FCF conversion near or above USD 12.2B guidance.
- Evidence that currency / structural headwinds are fading.
- Faster debt reduction or shareholder returns supported by durable FCF.
- Share price pullback that lifts FCF yield and creates margin of safety.

## Valuation Watch Items

- Base DCF fair value from `[[KO DCF Valuation 2026-06-28]]`: approximately USD 51.53 per diluted share.
- Fresh price used: USD 82.63 on 2026-06-26.
- Base DCF downside: approximately 37.6%.
- Bull scenario fair value: approximately USD 80.57, still slightly below current price and dependent on low WACC / high terminal growth.
- Re-run valuation after FY2026 Q2 or full-year results, especially if FCF conversion diverges from USD 12.2B guidance.

## Reports / Source Notes

- [[KO_latest_results_source]]
- [[KO_market_quote_2026-06-28]]
- [[KO_fundamentals]]
- [[KO DCF Valuation 2026-06-28]]
- [[KO Decision Memo 2026-06-28]]

## Follow-Up

- Retrieve official Q1 2026 transcript text if accessible later.
- Refresh current price before any future action call.
- Compare KO valuation to PEP, MNST, KDP, and consumer staples peers if considering relative-value entry.
- Update after Q2 2026 results and verify whether FY2026 FCF guidance remains intact.
- Track net debt and capital allocation through FY2026.

## Missing / Unverified Data

| Item | Status | Notes |
|---|---|---|
| Official Q1 2026 earnings call transcript text | ไม่พบข้อมูลที่ยืนยันได้ | Official PDF link was discovered but blocked. |
| Product/category-level profitability | not disclosed | Segment revenue is available, but detailed profit pool data is not normalized. |
| Sequential quarterly trend | ไม่พบข้อมูลที่ยืนยันได้ | Only Q1 2026 / Q1 2025 and annual trend were normalized in this pass. |
| Detailed bridge from FY2025 FCF to FY2026 FCF guidance | not disclosed | FY2026 FCF guidance is source-backed, but the working-capital bridge remains incomplete. |
| Real-time quote after 2026-06-26 close | ไม่พบข้อมูลที่ยืนยันได้ | 2026-06-28 is a Sunday; latest close used. |
| Investor-specific constraints | not provided | No personalized sizing or tax/cost-basis action call. |
