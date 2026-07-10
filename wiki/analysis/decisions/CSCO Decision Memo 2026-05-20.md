---
type: analysis
analysis_type: decision-memo
ticker: CSCO
company: Cisco Systems, Inc.
date: 2026-05-20
currency: USD
decision: AVOID / WAIT for new capital; REVIEW or TRIM only if already overweight
source_files:
  - index.md
  - wiki/entities/CSCO.md
  - raw/financials/CSCO_fundamentals.md
  - raw/imports/CSCO_latest_results_source.md
  - wiki/analysis/valuations/CSCO DCF Valuation 2026-05-20.md
tags:
  - analysis/decision-memo
  - ticker/CSCO
---

# CSCO Decision Memo - 2026-05-20
Entity: [[CSCO]]

## Action Read

**Action: AVOID / WAIT for new capital. REVIEW or TRIM only if already overweight after the post-earnings re-rating.**

CSCO มี official-source quarter ที่แข็งมาก: Q3 FY2026 revenue ทำ record, Networking revenue โต 25%, product orders โต 35%, และ management ยก FY2026 hyperscaler AI infrastructure order outlook เป็น about USD 9B. Thesis ฝั่ง bull ดีขึ้นจริง เพราะ Cisco กลับมาเกี่ยวข้องกับ AI infrastructure cycle มากกว่าที่ market มองในอดีต.

แต่ราคา ณ latest accessible close USD 118.88 สะท้อนความคาดหวังสูงมาก. TTM FCF yield เหลือ 2.51%, market EV / TTM FCF ประมาณ 41.1x, และ base DCF fair value อยู่เพียง USD 47.02 ต่อ diluted share. สำหรับ new capital จึงไม่มี margin of safety. ถ้ามี position เดิมและน้ำหนักสูง ควร review/trim discipline มากกว่า chase หลัง rerating.

## Current Price / Market Data Check

| Item | Value | Source |
|---|---:|---|
| Latest accessible price used | USD 118.88 close on 2026-05-18 | FinanceCharts market-cap history, checked 2026-05-20. |
| Market cap | USD 469.603B | FinanceCharts market-cap history. |
| Market-data shares outstanding | 3.95B | FinanceCharts market-cap history. |
| Yahoo quote cross-check | USD 118.21 close / USD 117.83 after hours on 2026-05-15 | Yahoo Finance, checked 2026-05-20. |
| Yahoo market cap cross-check | USD 466.917B | Yahoo Finance. |
| Diluted shares used in DCF | 3.987B | Cisco Q3 FY2026 release, 9M FY2026 diluted shares. |
| TTM FCF yield on market cap | 2.51% | TTM FCF USD 11.788B / market cap USD 469.603B. |

## Evidence From Vault

| Fact | Value | Source |
|---|---:|---|
| Latest verified period | Q3 FY2026 ended 2026-04-25 | `raw/financials/CSCO_fundamentals.md`. |
| Q3 FY2026 revenue | USD 15.841B | Cisco Q3 FY2026 release. |
| Q3 FY2026 revenue growth | 12.0% YoY | Cisco Q3 FY2026 release / calculation. |
| Q3 FY2026 operating income / margin | USD 3.960B / 25.0% | Cisco Q3 FY2026 release / calculation. |
| Q3 FY2026 net income | USD 3.373B | Cisco Q3 FY2026 release. |
| Q3 FY2026 diluted EPS / non-GAAP EPS | USD 0.85 / USD 1.06 | Cisco Q3 FY2026 release. |
| Q3 FY2026 Networking revenue growth | 25% YoY | Cisco Q3 FY2026 release. |
| Product orders | +35% YoY; +19% excluding hyperscalers | Cisco Q3 FY2026 release. |
| FY2026 hyperscaler AI infrastructure orders outlook | about USD 9B | Cisco Q3 FY2026 release. |
| Q3 FY2026 FCF | USD 3.343B | OCF USD 3.757B - capex USD 0.414B. |
| TTM FCF | USD 11.788B | FY2025 FCF - 9M FY2025 FCF + 9M FY2026 FCF. |
| Cash plus investments | USD 16.640B | Cisco Q3 FY2026 release. |
| Total debt | USD 31.303B | Cisco Q3 FY2026 release calculation. |
| FY2026 revenue guidance | USD 62.8B to USD 63.0B | Cisco Q3 FY2026 release. |
| FY2026 GAAP / non-GAAP EPS guidance | USD 3.16-3.21 / USD 4.27-4.29 | Cisco Q3 FY2026 release. |

## Valuation Read

| Valuation item | Result | Read |
|---|---:|---|
| DCF base fair value | USD 47.02 per diluted share | ต่ำกว่า latest accessible price ประมาณ 60% |
| DCF bull fair value | USD 68.09 per diluted share | ยังต่ำกว่าราคาตลาดมาก |
| TTM FCF yield on market cap | 2.51% | แพงสำหรับ mature cash-flow profile เว้นแต่ AI-driven FCF โตแรง |
| Market EV / TTM FCF | 41.08x | multiple สูงมากเมื่อเทียบกับ trailing FCF |
| Net debt / TTM FCF | 1.24x | Balance sheet ไม่ใช่ปัญหาหลัก |
| Forward GAAP / non-GAAP P/E | about 37.3x / 27.8x | Market capitalizes AI narrative already |

valuation ไม่ได้บอกว่า Cisco เป็นธุรกิจแย่. มันบอกว่าหุ้นหลัง rerating ต้องการ execution ที่ดีมากและ FCF acceleration ชัดเจนเพื่อ justify current price. ถ้า investor ยังไม่มี position, better decision คือ wait.

## Bull Case

- Q3 FY2026 revenue ทำ record ที่ USD 15.841B, โต 12% YoY.
- Networking revenue โต 25% YoY และ networking product orders accelerated to more than 50% YoY.
- Total product orders โต 35% YoY และยังโต 19% ถ้า exclude hyperscalers.
- Hyperscaler AI infrastructure orders reached USD 5.3B year to date, และ FY2026 order outlook ถูกยกเป็น about USD 9B.
- RPO USD 43.462B และ deferred revenue USD 28.599B ช่วย visibility ของ future revenue.
- TTM FCF USD 11.788B ยังเป็น cash engine ที่รองรับ dividend, buyback, and reinvestment.

## Bear Case

- Stock re-rated hard; latest accessible price USD 118.88 เทียบกับ DCF base fair value USD 47.02.
- 9M FY2026 FCF ลดลง 16.2% YoY แม้ revenue/EPS โต.
- TTM FCF yield only 2.51%; market EV / TTM FCF about 41.1x.
- Security revenue flat in Q3 and down 2% YTD, so Splunk/security growth thesis still needs proof in reported revenue.
- AI order concentration, margin, and repeatability are not disclosed.
- Q3 FY2026 full 10-Q and official full Q&A transcript were not normalized, limiting risk-detail confidence.

## Key Assumptions

| Assumption | Working choice |
|---|---|
| Investor profile | Long-term quality/compounder investor seeking margin of safety |
| Position status | Unknown; action emphasizes new capital as AVOID / WAIT |
| FCF anchor | Source-backed TTM FCF of USD 11.788B |
| Valuation framework | Information Technology DCF, 9.0% base WACC, 2.5% terminal growth |
| Balance sheet treatment | Use cash plus investments minus total debt for equity value |
| Quote caveat | Latest accessible close found was 2026-05-18; refresh before future action changes |

## What Would Change The Decision

- Upgrade toward watchlist/add only if price falls substantially while FY2026 guidance remains intact.
- Upgrade if FY2026 actual FCF materially exceeds TTM FCF and validates AI order conversion.
- Upgrade if Cisco discloses durable AI revenue, margin, and customer diversification evidence.
- Upgrade if Security/Splunk revenue reaccelerates without margin dilution.
- Downgrade toward avoid/trim if AI orders slow, FCF conversion weakens, or current multiple persists without cash-flow support.

## Missing / Unverified Data

| Item | Status | Why it matters |
|---|---|---|
| Q3 FY2026 Form 10-Q | ไม่พบข้อมูลที่ยืนยันได้ | Full filing would improve risk, footnote, and balance-sheet detail. |
| Official full prepared remarks / Q&A transcript | not normalized | Could refine management tone, analyst pushback, and AI order-quality read. |
| FY2026 full-year actual results | not disclosed | Q3 FY2026 is the latest official period found. |
| FY2026 FCF guidance | ไม่พบข้อมูลที่ยืนยันได้ | DCF uses TTM FCF rather than invented management FCF guidance. |
| Product-category operating profit | not disclosed | Limits segment-specific valuation. |
| Hyperscaler AI customer concentration and margin | not disclosed | Central to deciding whether AI orders deserve a premium multiple. |
| Market quote after 2026-05-18 close | ไม่พบข้อมูลที่ยืนยันได้ | Refresh before future action calls or trade-sensitive decisions. |
| Investor-specific position size, tax basis, and required return | not provided | Needed for individualized hold/trim/add sizing. |

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| `raw/imports/CSCO_latest_results_source.md` | Local source note | P1 official-source discovery and extraction. |
| `raw/financials/CSCO_fundamentals.md` | Local normalized facts | P4 verified financial facts, charts, ratios. |
| `wiki/entities/CSCO.md` | Local entity page | P6 business model, thesis, risks, catalysts. |
| `wiki/analysis/valuations/CSCO DCF Valuation 2026-05-20.md` | Local valuation memo | P11 DCF and sensitivity. |
| SEC Form 8-K | https://www.sec.gov/Archives/edgar/data/858877/000085887726000075/csco-20260513.htm | Official Q3 FY2026 result filing reference. |
| Cisco Q3 FY2026 earnings release | https://investor.cisco.com/news/news-details/2026/CISCO-REPORTS-THIRD-QUARTER-EARNINGS/default.aspx | Official Q3 FY2026 results, cash/debt, FCF inputs, and guidance. |
| Cisco FY2025 Form 10-K | https://www.sec.gov/Archives/edgar/data/858877/000085887725000111/csco-20250726.htm | Annual FCF baseline and business model context. |
| FinanceCharts CSCO market cap history | https://www.financecharts.com/stocks/CSCO/summary/market-cap | Fresh market-data check. |
| Yahoo Finance CSCO quote | https://finance.yahoo.com/quote/CSCO/ | Market-data cross-check. |
