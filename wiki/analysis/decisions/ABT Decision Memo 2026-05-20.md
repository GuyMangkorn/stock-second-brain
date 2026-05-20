---
type: analysis
analysis_type: decision-memo
ticker: ABT
company: Abbott Laboratories
date: 2026-05-20
currency: USD
decision: WAIT / WATCHLIST for new capital; HOLD only if already owned and comfortable with Exact Sciences integration risk
source_files:
  - index.md
  - wiki/entities/ABT.md
  - raw/financials/ABT_fundamentals.md
  - raw/imports/ABT_latest_results_source.md
  - wiki/analysis/valuations/ABT DCF Valuation 2026-05-20.md
tags:
  - analysis/decision-memo
  - ticker/ABT
---

# ABT Decision Memo - 2026-05-20

## Action Read

**Action: WAIT / WATCHLIST for new capital. HOLD only if already owned and comfortable with Exact Sciences integration risk and a long-term health care compounder thesis.**

ABT เป็น quality franchise แต่ยังไม่ใช่ obvious add ณ ราคาปัจจุบัน. Q1 2026 มี revenue growth ดี, Medical Devices แข็ง, Established Pharmaceuticals โตต่อ, และ guidance ยังดู healthy. แต่ debt เพิ่มแรงหลัง Exact Sciences, GAAP earnings อ่อนลง YoY, และ DCF ที่ใช้ TTM FCF source-backed ยังต่ำกว่าราคาตลาดมาก.

Base DCF fair value อยู่ประมาณ USD 63.17 ต่อ diluted share เทียบกับ fresh close price USD 88.82. Bull case ถึง USD 95.22 ได้ แต่ต้องอาศัย lower WACC, stronger FCF growth, และ execution ที่ดีหลัง acquisition. สำหรับ new capital จึงควรรอราคาที่มี margin of safety หรือหลักฐานว่า FCF/deleveraging trajectory ดีกว่าที่ TTM FCF แสดงอยู่.

## Current Price / Market Data Check

| Item | Value | Source |
|---|---:|---|
| Fresh price | USD 88.82 close on 2026-05-19 | StockAnalysis, checked 2026-05-20. |
| MarketBeat quote cross-check | USD 88.81 close / USD 88.66 extended | MarketBeat, checked 2026-05-20. |
| Market cap | USD 154.71B | StockAnalysis. |
| Enterprise value | USD 181.55B | StockAnalysis. |
| Shares outstanding | 1.74B | StockAnalysis / MarketBeat. |
| SEC common shares outstanding | 1,741,812,429 | SEC Form 10-Q, as of 2026-03-31. |
| Diluted weighted-average shares | 1.747073B | SEC Form 10-Q, Q1 2026. |
| TTM FCF yield on market cap | 4.77% | TTM FCF USD 7.378B / market cap USD 154.71B. |

## Evidence From Vault

| Fact | Value | Source |
|---|---:|---|
| Latest verified period | Q1 2026 ended 2026-03-31 | `raw/financials/ABT_fundamentals.md`. |
| Q1 2026 net sales | USD 11.164B | SEC Form 10-Q. |
| Q1 2026 reported / comparable sales growth | 7.8% / 3.7% | SEC Form 10-Q calculation / Abbott Q1 release. |
| Q1 2026 operating earnings | USD 1.345B | SEC Form 10-Q. |
| Q1 2026 net earnings | USD 1.077B | SEC Form 10-Q. |
| Q1 2026 diluted EPS | USD 0.61 | SEC Form 10-Q. |
| Q1 2026 adjusted diluted EPS | USD 1.15 | Abbott Q1 release; non-GAAP. |
| Q1 2026 FCF | USD 0.916B | SEC Form 10-Q calculation. |
| TTM FCF | USD 7.378B | FY2025 FCF - Q1 2025 FCF + Q1 2026 FCF. |
| Cash plus short-term investments | USD 7.295B | SEC Form 10-Q. |
| Total debt | USD 34.047B | SEC Form 10-Q calculation. |
| FY2026 comparable sales growth guidance | 6.5% to 7.5% | Abbott Q1 release. |
| FY2026 adjusted diluted EPS guidance | USD 5.38 to USD 5.58 | Abbott Q1 release. |

## Valuation Read

| Valuation item | Result | Read |
|---|---:|---|
| DCF base fair value | USD 63.17 per diluted share | ต่ำกว่า current price ประมาณ 29% |
| DCF bull fair value | USD 95.22 per diluted share | upside จำกัด และต้องใช้ favorable assumptions |
| TTM FCF yield on market cap | 4.77% | ไม่ถูกพอให้ ignore leverage/integration risk |
| Market EV / TTM FCF | 24.61x | premium multiple สำหรับช่วงที่ GAAP earnings กดดัน |
| Net debt / TTM FCF | 3.63x | manageable แต่สูงขึ้นอย่างมีนัยสำคัญหลัง Exact Sciences |
| Forward adjusted P/E | about 16.2x | ดู reasonable บน non-GAAP EPS, แต่ key debate คือ FCF conversion |

valuation ไม่ได้บอกว่า ABT เป็นธุรกิจแย่. มันบอกว่าราคา ณ ตอนนี้ยังต้องการ FCF growth/deleveraging ที่ดีเพื่อ justify upside. เมื่อ official FCF guidance ยังไม่เปิดเผยและ acquisition integration ยังใหม่เกินไป, action read จึงเป็น wait.

## Bull Case

- Q1 2026 sales โต 7.8% reported และ 3.7% comparable.
- Medical Devices โต 13.2% reported และ 8.5% comparable โดย Rhythm Management, Electrophysiology, Heart Failure และ Diabetes Care เป็น driver.
- Established Pharmaceuticals โต 9.0% comparable จาก emerging markets.
- Exact Sciences เพิ่ม new Cancer Diagnostics vertical; Q1 มี sales USD 96M ตั้งแต่ acquisition date.
- FY2026 adjusted EPS guide USD 5.38-5.58 ทำให้ current price อยู่ราว 16x adjusted EPS midpoint.
- TTM FCF USD 7.378B ยังเป็น cash engine ที่ช่วย dividend และ debt paydown ได้ถ้า integration ไม่สะดุด.

## Bear Case

- Q1 2026 operating earnings ลด 20.6% YoY และ net earnings ลด 18.7% YoY แม้ revenue โต.
- SG&A เพิ่มมากจาก acquisition/integration และ stock-based compensation related to Exact Sciences.
- Total debt เพิ่มเป็น USD 34.047B และ net debt using cash plus STI เป็น USD 26.752B.
- FY2026 full-year FCF guidance ไม่พบข้อมูลที่ยืนยันได้.
- DCF base case ต่ำกว่าราคาตลาดมาก และ market EV / TTM FCF ประมาณ 24.6x.
- Exact Sciences integration, product/regulatory risk, Nutrition volume recovery, and litigation overhang ยังเป็นตัวแปรสำคัญ.

## Key Assumptions

| Assumption | Working choice |
|---|---|
| Investor profile | Long-term quality/compounder investor ที่ยังต้องการ margin of safety |
| Position status | Unknown; action จึงเน้น new capital เป็น WAIT |
| FCF anchor | Source-backed TTM FCF of USD 7.378B |
| Valuation framework | Health Care DCF, 8.5% base WACC, 2.5% terminal growth |
| Balance sheet treatment | Use cash plus short-term investments minus total debt for equity value |

## What Would Change The Decision

- Upgrade toward add ถ้าราคาลงใกล้หรือต่ำกว่า base fair value โดย guidance ยัง intact.
- Upgrade ถ้า FY2026 actual FCF สูงกว่า TTM FCF anchor อย่างมีนัยสำคัญ.
- Upgrade ถ้า Abbott แสดง deleveraging path หลัง Exact Sciences ชัดเจนกว่าปัจจุบัน.
- Upgrade ถ้า Cancer Diagnostics growth และ synergy evidence offset acquisition dilution.
- Downgrade toward avoid ถ้า guidance ถูกลด, FCF conversion อ่อน, หรือ debt/integration cost สูงกว่าที่ source ปัจจุบันบอกไว้.

## Missing / Unverified Data

| Item | Status | Why it matters |
|---|---|---|
| FY2026 full-year actual results | not disclosed | Q1 2026 is the latest official period found. |
| FY2026 full-year FCF guidance | ไม่พบข้อมูลที่ยืนยันได้ | DCF uses TTM FCF rather than an invented FY2026 FCF guide. |
| Forward GAAP EPS / net income guidance | not provided | Limits GAAP P/E and normalized earnings cross-check. |
| Exact Sciences full run-rate contribution and integration cost detail | partially disclosed | Important for acquisition accretion/dilution and synergy analysis. |
| Product-level profitability | not disclosed | Limits segment-specific valuation. |
| Official full Q&A transcript | ไม่พบข้อมูลที่ยืนยันได้ | Could refine management-confidence and analyst-pushback reads. |
| Investor-specific tax basis, position size, and required return | not provided | Needed for individualized hold/trim/add sizing. |

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| `raw/imports/ABT_latest_results_source.md` | Local source note | P1 official-source discovery and extraction. |
| `raw/financials/ABT_fundamentals.md` | Local normalized facts | P4 verified financial facts, charts, ratios. |
| `wiki/entities/ABT.md` | Local entity page | P6 business model, thesis, risks, catalysts. |
| `wiki/analysis/valuations/ABT DCF Valuation 2026-05-20.md` | Local valuation memo | P11 DCF and sensitivity. |
| SEC Q1 2026 Form 10-Q | https://www.sec.gov/Archives/edgar/data/1800/000162828026028357/abt-20260331.htm | Official quarterly facts. |
| Abbott Q1 2026 earnings release | https://abbott.mediaroom.com/2026-04-16-Abbott-Reports-First-Quarter-2026-Results-Updates-Guidance-to-Reflect-Acquisition-of-Exact-Sciences?asPDF=1 | Guidance and segment/category commentary. |
| Abbott FY2025 Form 10-K | https://www.sec.gov/Archives/edgar/data/1800/000162828026010185/abt-20251231.htm | Annual FCF baseline and legal-risk context. |
| StockAnalysis ABT statistics page | https://stockanalysis.com/stocks/abt/statistics/ | Fresh market-data check. |
| MarketBeat ABT quote page | https://www.marketbeat.com/stocks/NYSE/ABT/ | Market-data cross-check. |
