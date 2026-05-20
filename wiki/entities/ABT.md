---
type: entity
ticker: ABT
company: Abbott Laboratories
market: NYSE
currency: USD
period_type: quarterly + annual
reporting_scope: Q1 2026 quarter ended 2026-03-31 plus FY2025 annual baseline
latest_period: Q1 2026
latest_period_end: 2026-03-31
latest_total_revenue_usd_m: 11164
latest_net_income_usd_m: 1077
source_gap_count: 7
source_gaps:
  - FY2026 full-year actual results not disclosed.
  - FY2026 full-year FCF guidance not verified.
  - Forward GAAP EPS / net income guidance not provided.
  - Official full Q&A transcript not normalized.
  - Product-level profitability not disclosed.
  - Exact Sciences full run-rate contribution and integration cost detail only partially disclosed.
  - Investor-specific position size, tax basis, and required return not provided.
source_notes:
  - raw/imports/ABT_latest_results_source.md
normalized_markdown: raw/financials/ABT_fundamentals.md
normalized_json: raw/financials/ABT_fundamentals.json
tags:
  - entity/company
  - ticker/ABT
---

# ABT - Abbott Laboratories

## Snapshot

| Item | Value |
|---|---|
| Ticker | ABT |
| Company | Abbott Laboratories |
| Market | NYSE |
| Currency | USD |
| Latest period | Q1 2026, quarter ended 2026-03-31 |
| Reporting scope | Q1 2026 quarter ended 2026-03-31 plus FY2025 annual baseline |
| Normalized file | `raw/financials/ABT_fundamentals.md` |
| Latest price check | USD 88.82 close on 2026-05-19; checked 2026-05-20 |
| Current action read | WAIT / WATCHLIST for new capital |

## Source Map

| Priority | Source | Status | Notes |
|---:|---|---|---|
| 1 | SEC / official filings | Available | Q1 2026 Form 10-Q and FY2025 Form 10-K reviewed. |
| 1 | Official company results | Available | Q1 2026 earnings release reviewed. |
| 2 | Earnings transcript / call material | Partially available | Official webcast referenced, but official full Q&A transcript was not normalized. |
| 3 | Financial statements / metrics | Available | StockAnalysis and MarketBeat used only for fresh market data, lower priority than filings. |
| 4 | News / web context | Limited | Not required for core financial facts; no secondary news was used for durable company facts. |

## Business Model

Abbott เป็น diversified health care company ที่ขาย medical devices, diagnostics, nutritionals, และ branded generic medicines ทั่วโลก. รายได้กระจายระหว่าง businesses ที่มี demand driver ต่างกัน: procedure volume และ product cycle ใน Medical Devices, diagnostic test volumes และ installed platforms ใน Diagnostics, emerging-market branded generics ใน Established Pharmaceuticals, และ consumer/clinical nutrition ใน Nutrition.

หลังปิดดีล Exact Sciences วันที่ 2026-03-23 บริษัทเพิ่ม Cancer Diagnostics เข้า portfolio. จุดนี้เพิ่ม growth optionality แต่ก็ดัน leverage ขึ้นมากใน Q1 2026 เพราะ Abbott ออก debt ใหม่เพื่อ finance acquisition.

## Segments / Revenue Mix

| Segment / category | Q1 2026 Sales | Q1 2026 Mix | Reported Growth | Comparable / FX-neutral Growth | Source |
|---|---:|---:|---:|---:|---|
| Nutrition | USD 2.017B | 18.1% | -6.0% | -7.7% comparable | Abbott Q1 release. |
| Diagnostics | USD 2.180B | 19.5% | 6.1% | 1.8% comparable | Abbott Q1 release. |
| Established Pharmaceuticals | USD 1.426B | 12.8% | 13.2% | 9.0% comparable | Abbott Q1 release. |
| Medical Devices | USD 5.539B | 49.6% | 13.2% | 8.5% comparable | Abbott Q1 release. |

Medical Devices คือ growth engine หลักของ Q1 โดย strength มาจาก Rhythm Management, Electrophysiology, Heart Failure และ Diabetes Care. Established Pharmaceuticals ยังโตดีใน emerging markets. Diagnostics มี Core Laboratory และ Cancer Diagnostics ช่วย offset Rapid/Molecular weakness จาก respiratory season ที่อ่อนกว่าเดิม. Nutrition ยังเป็นจุดอ่อนจาก lower volume และ pricing actions.

## Financial Facts

| Metric | Latest value | Source |
|---|---:|---|
| Q1 2026 net sales | USD 11.164B | SEC Form 10-Q. |
| Q1 2026 reported / comparable sales growth | 7.8% / 3.7% | SEC Form 10-Q calculation / Abbott Q1 release. |
| Q1 2026 operating earnings | USD 1.345B | SEC Form 10-Q. |
| Q1 2026 net earnings | USD 1.077B | SEC Form 10-Q. |
| Q1 2026 diluted EPS | USD 0.61 | SEC Form 10-Q. |
| Q1 2026 adjusted diluted EPS | USD 1.15 | Abbott Q1 release; non-GAAP. |
| Q1 2026 free cash flow | USD 0.916B | SEC Form 10-Q calculation: OCF - capex. |
| TTM free cash flow | USD 7.378B | FY2025 FCF - Q1 2025 FCF + Q1 2026 FCF. |
| Cash plus short-term investments | USD 7.295B | SEC Form 10-Q, 2026-03-31. |
| Total debt | USD 34.047B | SEC Form 10-Q calculation. |
| Net debt using cash plus short-term investments | USD 26.752B | SEC Form 10-Q calculation. |
| FY2026 comparable sales growth guidance | 6.5% to 7.5% | Abbott Q1 release. |
| FY2026 adjusted diluted EPS guidance | USD 5.38 to USD 5.58 | Abbott Q1 release. |

## Charts

See `raw/financials/ABT_fundamentals.md` for source-backed quarterly YoY, annual FCF, segment revenue, cash-flow/capex, and balance-sheet chart blocks.

## Transcript / Management Commentary

Management framed Q1 2026 as aligned with expectations, with adjusted diluted EPS of USD 1.15 and sales of USD 11.2B. Abbott updated FY2026 guidance to comparable sales growth of 6.5% to 7.5% and adjusted diluted EPS of USD 5.38 to USD 5.58, including USD 0.20 dilution related to Exact Sciences.

The key operational read is mixed: Medical Devices and Established Pharmaceuticals are working, Diagnostics is now helped by Exact Sciences/Cancer Diagnostics but Rapid/Molecular remains soft, and Nutrition is still digesting lower volume plus pricing actions. The financial read is also mixed: revenue grew, but GAAP operating earnings and net earnings declined YoY as SG&A and acquisition-related expense rose.

## Thesis

### Bull Case

ABT เป็น high-quality diversified health care compounder ที่มี multiple engines. Medical Devices โต 13.2% reported และ 8.5% comparable ใน Q1, Established Pharmaceuticals โต 9.0% comparable, และ Exact Sciences เพิ่ม exposure ไปที่ oncology diagnostics ซึ่งเป็น category ที่อาจโตเร็วกว่าธุรกิจเดิม.

Balance sheet ยังมี investment-grade rating ตาม 10-Q, และ TTM FCF USD 7.378B ช่วยรองรับ dividend และ deleveraging หลังดีล Exact Sciences. ถ้า acquisition integration สำเร็จ, Nutrition volume กลับมา, และ Medical Devices รักษา momentum ได้ ราคาปัจจุบันที่ประมาณ 16x midpoint FY2026 adjusted EPS guide อาจไม่แพงบน non-GAAP EPS.

### Bear Case

Q1 2026 แสดง quality/business strength แต่ไม่ใช่ margin expansion story: revenue โต 7.8% reported แต่ operating earnings ลด 20.6% YoY และ net earnings ลด 18.7% YoY. Net debt กระโดดขึ้นเป็นประมาณ USD 26.8B หลัง Exact Sciences ทำให้ equity value sensitivity ต่อ FCF และ WACC สูงขึ้น.

DCF base case ที่ใช้ TTM FCF source-backed ให้ fair value ประมาณ USD 63.17 ต่อ diluted share ต่ำกว่าราคาปิด USD 88.82 ชัดเจน. Bull case ถึงจะเข้าใกล้/สูงกว่าราคาตลาดได้ แต่ต้องอาศัย lower WACC, stronger FCF growth, และ integration execution ที่ยังต้องพิสูจน์.

### Key Debate

คำถามหลักคือ Abbott กำลังได้ growth engine ใหม่ที่คุ้มกับ leverage และ acquisition dilution หรือ market ยังควร discount ดีล Exact Sciences จนเห็น FCF conversion และ debt trajectory ชัดกว่านี้.

## Risks

- Integration risk จาก Exact Sciences acquisition และ debt-funded balance sheet expansion.
- Nutrition volume and pricing risk ถ้า pricing actions ยังทำให้ volume recovery ช้า.
- Medical-device regulatory, clinical, recall, and competition risk.
- Diagnostics demand cyclicality โดยเฉพาะ respiratory testing และ China Core Lab pressure.
- GAAP/non-GAAP quality risk เพราะ adjusted EPS exclude specified items จำนวนมาก.
- Litigation risk รวมถึง specialty infant formula lawsuits ตาม FY2025 Form 10-K.
- Interest-rate and refinancing risk จาก total debt ที่สูงขึ้นหลังดีล.

## Catalysts

- Q2 2026 results and whether adjusted EPS reaches USD 1.25 to USD 1.31 guidance.
- Evidence of Nutrition volume improvement after pricing actions.
- Medical Devices growth sustainability in Rhythm Management, Electrophysiology, Heart Failure, and Diabetes Care.
- Exact Sciences integration progress, Cancer Diagnostics revenue contribution, and synergy/deleveraging disclosures.
- Updated cash flow, capex, and debt trajectory after Q2/Q3 2026 filings.
- Any update to FY2026 comparable sales or adjusted EPS guidance.

## Valuation Watch Items

- Current DCF memo: [[ABT DCF Valuation 2026-05-20]].
- Base-case fair value from P11 is approximately USD 63.17 per diluted share versus USD 88.82 latest close.
- Bull case reaches approximately USD 95.22 only with stronger FCF growth and lower WACC.
- Watch TTM FCF, FY2026 actual FCF, net debt paydown, and Exact Sciences integration before upgrading the action read.

## Reports / Source Notes

| Note | Type |
|---|---|
| [[ABT_latest_results_source]] | Latest results source note |
| [[ABT_fundamentals]] | Normalized financial facts |
| [[ABT DCF Valuation 2026-05-20]] | DCF valuation |
| [[ABT Decision Memo 2026-05-20]] | Decision memo |

## Follow-Up

- Refresh after Q2 2026 results with updated revenue, GAAP EPS, adjusted EPS, OCF, capex, FCF, cash, debt, shares, and guidance.
- Track Exact Sciences integration costs, Cancer Diagnostics growth, and any synergy/deleveraging targets.
- Verify whether FY2026 actual FCF supports or exceeds the current TTM FCF anchor.
- Re-check current price before any action change.
- Normalize an official full Q&A transcript if Abbott publishes one.

## Missing / Unverified Data

| Item | Status | Notes |
|---|---|---|
| FY2026 full-year actual results | not disclosed | Q1 2026 was the latest official period found. |
| FY2026 full-year FCF guidance | ไม่พบข้อมูลที่ยืนยันได้ | Abbott provided comparable sales and adjusted EPS guidance, not FCF guidance. |
| Forward GAAP EPS / net income guidance | not provided | Abbott says forward non-GAAP guidance cannot be reconciled with reasonable certainty. |
| Official full Q&A transcript | ไม่พบข้อมูลที่ยืนยันได้ | Webcast reference exists; official transcript was not normalized. |
| Product-level profitability | not disclosed | Segment/category revenue was disclosed; product profit was not. |
| Exact Sciences full run-rate contribution and integration cost detail | partially disclosed | Q1 includes USD 96M of sales since acquisition date, but full run-rate profitability was not disclosed. |
| Investor-specific tax basis, position size, and required return | not provided | Needed for individualized add/hold/trim sizing. |
