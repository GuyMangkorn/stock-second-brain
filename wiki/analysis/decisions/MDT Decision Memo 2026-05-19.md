---
type: analysis
analysis_type: decision-memo
ticker: MDT
company: Medtronic plc
date: 2026-05-19
currency: USD
decision: WAIT / WATCHLIST for new capital; HOLD only if already owned and thesis horizon is long
source_files:
  - index.md
  - wiki/entities/MDT.md
  - raw/financials/MDT_fundamentals.md
  - raw/imports/MDT_latest_results_source.md
  - wiki/analysis/valuations/MDT DCF Valuation 2026-05-19.md
tags:
  - analysis/decision-memo
  - ticker/MDT
---

# MDT Decision Memo - 2026-05-19

## Action Read

**Action: WAIT / WATCHLIST for new capital. HOLD only if already owned and thesis horizon is long enough to tolerate Diabetes separation and FCF conversion uncertainty.**

MDT เป็น quality medtech franchise ที่กำลังเห็น organic growth ดีขึ้น โดย Q3 FY26 revenue โต 8.7% reported และ 6.0% organic. แต่ราคาปัจจุบันยังไม่ให้ margin of safety ชัดเมื่อดูจาก DCF ที่ใช้ TTM FCF source-backed.

Base DCF fair value อยู่ประมาณ USD 59.41 ต่อ diluted share เทียบกับ fresh close price USD 77.32. Bull case ถึง USD 89.84 ได้ แต่ต้องอาศัย lower WACC, stronger FCF growth, และ execution ที่ดีใน PFA/Hugo/Diabetes separation. สำหรับ new capital จึงควรรอ Q4 FY26 results หรือราคาที่ชดเชย risk มากกว่านี้.

## Current Price / Market Data Check

| Item | Value | Source |
|---|---:|---|
| Fresh price | USD 77.32 close on 2026-05-18 | StockAnalysis, checked 2026-05-19. |
| Premarket quote | USD 77.36 as of 2026-05-19 08:01 AM EDT | StockAnalysis. |
| Market cap | USD 99.27B | StockAnalysis. |
| Enterprise value | USD 118.81B | StockAnalysis. |
| Shares outstanding | 1.28B | StockAnalysis. |
| SEC shares outstanding | 1,283,884,964 | SEC Form 10-Q, as of 2026-02-18. |
| Diluted weighted-average shares | 1.2895B | SEC Form 10-Q, Q3 FY26. |
| TTM FCF yield on market cap | 5.45% | TTM FCF USD 5.410B / market cap USD 99.27B. |

## Evidence From Vault

| Fact | Value | Source |
|---|---:|---|
| Latest verified period | FY26 Q3 ended 2026-01-23 | `raw/financials/MDT_fundamentals.md`. |
| Q3 FY26 net sales | USD 9.017B | SEC Form 10-Q. |
| Q3 FY26 reported / organic growth | 8.7% / 6.0% | Medtronic Q3 FY26 release. |
| Q3 FY26 operating profit | USD 1.464B | SEC Form 10-Q. |
| Q3 FY26 net income | USD 1.150B | SEC Form 10-Q. |
| Q3 FY26 diluted EPS | USD 0.89 | SEC Form 10-Q. |
| 9M FY26 FCF | USD 3.341B | Medtronic Q3 FY26 release. |
| TTM FCF | USD 5.410B | FY2025 FCF - 9M FY25 FCF + 9M FY26 FCF. |
| Cash plus investments | USD 8.383B | SEC Form 10-Q. |
| Total debt | USD 28.071B | SEC Form 10-Q calculation. |
| FY26 organic revenue growth guidance | approximately 5.5% | Medtronic Q3 FY26 release. |
| FY26 non-GAAP diluted EPS guidance | USD 5.62 to USD 5.66 | Medtronic Q3 FY26 release. |

## Valuation Read

| Valuation item | Result | Read |
|---|---:|---|
| DCF base fair value | USD 59.41 per diluted share | ต่ำกว่า current price ประมาณ 23% |
| DCF bull fair value | USD 89.84 per diluted share | upside ได้ แต่ต้องใช้ optimistic assumptions |
| TTM FCF yield on market cap | 5.45% | ไม่ถูกพอให้ ignore execution risk |
| Market EV / TTM FCF | 21.96x | ไม่ใช่ deep-value multiple |
| Net debt / TTM FCF | 3.64x | manageable แต่ยังมีผลต่อ equity value |

valuation ไม่ได้บอกว่า MDT เป็นธุรกิจแย่. มันบอกว่าราคา ณ ตอนนี้ยังสะท้อนคุณภาพไปพอสมควรแล้ว และความไม่ชัดของ FY26 full-year FCF กับ Diabetes separation ยังทำให้ wait ดีกว่า add.

## Bull Case

- Q3 FY26 organic revenue growth 6.0% สูงกว่า Q3 guidance 50 bps.
- Cardiovascular โต 13.8% reported โดย Cardiac Ablation Solutions/PFA เป็น driver สำคัญ.
- Diabetes revenue โต 14.8% reported แม้กำลังเข้าสู่ separation path.
- Balance sheet มี cash plus investments USD 8.383B และ net debt using cash plus investments ประมาณ USD 19.688B.
- FY26 non-GAAP EPS guidance USD 5.62-5.66 ทำให้ stock ดูไม่แพงมากบน non-GAAP EPS.
- หาก Hugo, PFA, TAVR, neuromodulation, และ Diabetes separation execute ได้ดี bull DCF ยังมี upside.

## Bear Case

- Q3 FY26 operating profit ลดลง YoY แม้ revenue โตแรง.
- Q3 FY26 GAAP EPS ลดลงจาก USD 1.01 เป็น USD 0.89.
- Market EV / TTM FCF ประมาณ 22x ยังไม่ถูกสำหรับบริษัทที่มี tariff, regulatory, and portfolio-transition risk.
- FY26 full-year FCF guidance ไม่พบข้อมูลที่ยืนยันได้ใน official Q3 sources.
- Diabetes separation อาจสร้าง stranded cost หรือ dis-synergy ที่ยังประเมินไม่ได้.
- DCF base case ต่ำกว่าราคาตลาดชัดเจน.

## Key Assumptions

| Assumption | Working choice |
|---|---|
| Investor profile | Long-term quality/compounder investor ที่ยังต้องการ margin of safety |
| Position status | Unknown; action จึงเน้น new capital เป็น WAIT |
| FCF anchor | Source-backed TTM FCF of USD 5.410B |
| Valuation framework | Health Care DCF, 8.5% base WACC, 2.5% terminal growth |
| Balance sheet treatment | Use cash plus investments minus total debt for equity value |

## What Would Change The Decision

- Upgrade toward add ถ้าราคาลงใกล้หรือต่ำกว่า base fair value โดย guidance ยัง intact.
- Upgrade ถ้า FY2026 actual FCF สูงกว่า TTM FCF anchor อย่างมีนัยสำคัญ.
- Upgrade ถ้า Diabetes separation disclosures ชี้ว่า value unlock มากกว่า stranded-cost risk.
- Upgrade ถ้า Q4 FY26 results ยืนยันว่า GAAP operating profit เริ่มตาม organic revenue acceleration.
- Downgrade toward avoid ถ้า FY26 guide ถูกลด, FCF conversion อ่อน, หรือ Diabetes separation สร้าง drag มากกว่าคาด.

## Missing / Unverified Data

| Item | Status | Why it matters |
|---|---|---|
| FY26 full-year results | not disclosed | Q4 FY26 / FY2026 actuals are scheduled for 2026-06-03. |
| FY26 full-year FCF guidance | ไม่พบข้อมูลที่ยืนยันได้ | DCF uses TTM FCF rather than an invented FY26 FCF guide. |
| Product/division-level profitability | not disclosed | Limits segment-specific valuation. |
| Diabetes standalone post-separation financials | ไม่พบข้อมูลที่ยืนยันได้ | Important for sum-of-the-parts and stranded-cost analysis. |
| Full Q&A transcript signal | not normalized | Could refine management-confidence and analyst-pushback reads. |
| Investor-specific tax basis, position size, and required return | not provided | Needed for individualized hold/trim/add sizing. |

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| `raw/imports/MDT_latest_results_source.md` | Local source note | P1 official-source discovery and extraction. |
| `raw/financials/MDT_fundamentals.md` | Local normalized facts | P4 verified financial facts, charts, ratios. |
| `wiki/entities/MDT.md` | Local entity page | P6 business model, thesis, risks, catalysts. |
| `wiki/analysis/valuations/MDT DCF Valuation 2026-05-19.md` | Local valuation memo | P11 DCF and sensitivity. |
| SEC Q3 FY26 Form 10-Q | https://www.sec.gov/Archives/edgar/data/1613103/000162828026011107/mdt-20260123.htm | Official quarterly facts. |
| Medtronic Q3 FY26 earnings release | https://news.medtronic.com/2026-02-17-Medtronic-reports-strong-third-quarter-fiscal-2026-results-with-highest-enterprise-revenue-growth-in-10-quarters | Guidance, segment revenue, and FCF. |
| Medtronic FY2025 Q4/full-year release | https://news.medtronic.com/2025-05-21-Medtronic-reports-strong-finish-to-its-fiscal-year-with-its-fourth-quarter-financial-results-announces-dividend-increase | FY2025/FY2024/FY2023 FCF baseline. |
| Medtronic IR overview | https://investorrelations.medtronic.com/ | Q4 FY26 reporting date. |
| StockAnalysis MDT statistics page | https://stockanalysis.com/stocks/mdt/statistics/ | Fresh market-data check. |
