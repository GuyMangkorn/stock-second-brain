---
type: entity
ticker: MDT
company: Medtronic plc
market: NYSE
currency: USD
period_type: quarterly + annual
reporting_scope: FY26 Q3 and nine months ended 2026-01-23 plus FY2025 annual baseline
latest_period: FY26 Q3
latest_period_end: 2026-01-23
latest_total_revenue_usd_m: 9017
latest_net_income_usd_m: 1150
source_gap_count: 6
source_gaps:
  - FY26 full-year results not disclosed.
  - FY26 full-year FCF guidance not verified.
  - Product/division-level profitability not disclosed.
  - Diabetes standalone post-separation financials not verified.
  - Post-CathWorks / Anteris financial contribution not fully disclosed.
  - Investor-specific position size, tax basis, and required return not provided.
source_notes:
  - raw/imports/MDT_latest_results_source.md
normalized_markdown: raw/financials/MDT_fundamentals.md
normalized_json: raw/financials/MDT_fundamentals.json
tags:
  - entity/company
  - ticker/MDT
---

# MDT - Medtronic plc

## Snapshot

| Item | Value |
|---|---|
| Ticker | MDT |
| Company | Medtronic plc |
| Market | NYSE |
| Currency | USD |
| Latest period | FY26 Q3, quarter ended 2026-01-23 |
| Reporting scope | FY26 Q3 and nine months ended 2026-01-23 plus FY2025 annual baseline |
| Normalized file | `raw/financials/MDT_fundamentals.md` |
| Latest price check | USD 77.32 close on 2026-05-18; USD 77.36 premarket on 2026-05-19 |
| Current action read | WAIT / WATCHLIST for new capital |

## Source Map

| Priority | Source | Status | Notes |
|---:|---|---|---|
| 1 | SEC / official filings | Available | Q3 FY26 Form 10-Q and FY2025 Form 10-K reviewed. |
| 1 | Official company results | Available | Q3 FY26 earnings release and FY2025 Q4/full-year release reviewed. |
| 2 | Earnings transcript / call material | Partially available | Prepared remarks / webcast page exists, but this workflow used official release commentary rather than a full Q&A transcript. |
| 3 | Financial statements / metrics | Available | StockAnalysis used only for fresh market data, lower priority than filings. |
| 4 | News / web context | Limited | Not required for core financial facts; current official IR page used for Q4 FY26 reporting date. |

## Business Model

Medtronic เป็น large-cap medical technology company ที่ขาย device-based therapies และ related services ทั่วโลก. ธุรกิจหลักกระจายอยู่ใน Cardiovascular, Neuroscience, Medical Surgical, และ Diabetes โดย demand อิง installed base, clinical adoption, hospital procedure volumes, reimbursement, regulatory approvals, และ physician/patient outcomes.

โมเดลธุรกิจมี recurring/consumable-like elements บางส่วน แต่ไม่ใช่ pure subscription. Growth ต้องพึ่ง product cycle และ innovation cadence เช่น pulsed field ablation, TAVR, cardiac rhythm management, spine, neuromodulation, robotic-assisted surgery, และ diabetes technology.

## Segments / Revenue Mix

| Segment | Q3 FY26 Revenue | Q3 FY26 Mix | YoY Growth | 9M FY26 Revenue | Source |
|---|---:|---:|---:|---:|---|
| Cardiovascular | 3,457 | 38.3% | 13.8% | 10,179 | Medtronic Q3 FY26 release. |
| Neuroscience | 2,558 | 28.4% | 4.1% | 7,536 | Medtronic Q3 FY26 release. |
| Medical Surgical | 2,173 | 24.1% | 4.9% | 6,428 | Medtronic Q3 FY26 release. |
| Diabetes | 796 | 8.8% | 14.8% | 2,274 | Medtronic Q3 FY26 release. |
| Other operating segment | 32 | 0.4% | 3.0% | 101 | Medtronic Q3 FY26 release / SEC Form 10-Q. |
| Other adjustments | 0 | 0.0% | n/a | 39 | SEC Form 10-Q; Italian payback adjustment noted in MD&A. |
| Total | 9,017 | 100.0% | 8.7% | 26,557 | Medtronic Q3 FY26 release / SEC 10-Q. |

Cardiovascular คือ growth engine หลักใน Q3 FY26 โดย management ชี้ไปที่ Cardiac Ablation Solutions และ pulsed field ablation. Diabetes ก็โต double digit แต่มี strategic uncertainty จากแผน separation.

## Financial Facts

| Metric | Latest value | Source |
|---|---:|---|
| Q3 FY26 net sales | USD 9.017B | SEC Form 10-Q. |
| Q3 FY26 reported growth | 8.7% YoY | Medtronic Q3 FY26 release. |
| Q3 FY26 organic growth | 6.0% YoY | Medtronic Q3 FY26 release. |
| Q3 FY26 operating profit | USD 1.464B | SEC Form 10-Q. |
| Q3 FY26 net income | USD 1.150B | SEC Form 10-Q. |
| Q3 FY26 diluted EPS | USD 0.89 | SEC Form 10-Q. |
| Q3 FY26 non-GAAP diluted EPS | USD 1.36 | Medtronic Q3 FY26 release. |
| 9M FY26 free cash flow | USD 3.341B | Medtronic Q3 FY26 release. |
| Cash plus investments | USD 8.383B | SEC Form 10-Q, 2026-01-23. |
| Total debt | USD 28.071B | SEC Form 10-Q calculation. |
| Net debt using cash plus investments | USD 19.688B | SEC Form 10-Q calculation. |
| FY26 organic revenue growth guidance | approximately 5.5% | Medtronic Q3 FY26 release. |
| FY26 diluted non-GAAP EPS guidance | USD 5.62 to USD 5.66 | Medtronic Q3 FY26 release. |

## Charts

See `raw/financials/MDT_fundamentals.md` for source-backed quarterly YoY, YTD, segment revenue, cash-flow/capex, and balance-sheet chart blocks.

## Transcript / Management Commentary

Management framed Q3 FY26 as a stronger growth quarter, with 6% organic revenue growth ahead of guidance. The strongest named driver was Cardiovascular, especially Cardiac Ablation Solutions and pulsed field ablation. Management also highlighted U.S. FDA clearance for Hugo robotic-assisted surgery and M&A activity around CathWorks and Anteris.

Guidance was reiterated rather than raised: FY26 organic revenue growth approximately 5.5% and diluted non-GAAP EPS of USD 5.62 to USD 5.66. This guide includes an estimated USD 185M tariff impact.

## Thesis

### Bull Case

MDT มี setup ที่น่าสนใจกว่าเดิมถ้าเชื่อว่า organic growth 5%+ sustainable: Cardiovascular acceleration ช่วย offset slower franchises, Diabetes ยังโตดี, และ FCF generation remains meaningful. Balance sheet ไม่ได้ตึงแบบ highly levered telecom/utility case; net debt using cash plus investments อยู่ประมาณ USD 19.7B เทียบ TTM FCF ประมาณ USD 5.41B.

ถ้า product cycle ใน PFA, TAVR, Hugo, neuromodulation, spine, และ diabetes execution เดินต่อพร้อม margin improvement, stock ที่ trading ราว 18x TTM FCF อาจกลับมา rerate ได้.

### Bear Case

รายได้โต แต่ GAAP operating profit และ Q3 net income ลดลง YoY เพราะ cost, amortization, litigation/restructuring, tariff, and portfolio-transition pressure ยังมีน้ำหนัก. DCF base case ใช้ TTM FCF และ WACC 8.5% ให้ fair value ต่ำกว่าราคาตลาด ทำให้ margin of safety ยังไม่พอสำหรับ new capital.

Diabetes separation, tariff policy, regulatory risk, clinical adoption risk, product recalls/litigation, and acquisition integration เป็นตัวแปรที่อาจทำให้ valuation multiple ถูกกดต่อ.

### Key Debate

คำถามหลักคือ MDT กำลังกลับเข้าสู่ durable mid-single-digit organic growth พร้อม FCF compounding หรือแค่ rebound จาก product-cycle pockets ที่ยังไม่พอชนะ margin, tariff, and portfolio-separation drag.

## Risks

- Product/regulatory risk: medical devices require approvals, clinical evidence, and post-market safety.
- Tariff and trade-policy risk: FY26 guidance includes approximately USD 185M potential tariff impact.
- Portfolio complexity: Diabetes separation could unlock focus but adds execution and stranded-cost uncertainty.
- Margin risk: Q3 FY26 GAAP operating profit fell YoY despite strong revenue growth.
- Litigation/restructuring/amortization: recurring adjustments complicate GAAP vs non-GAAP quality of earnings.
- Competitive risk: PFA, TAVR, surgical robotics, spine, and diabetes markets are innovation-heavy and competitive.

## Catalysts

- Q4 FY26 / FY2026 results on 2026-06-03.
- Evidence that Q3 organic acceleration carries into FY2026 full-year results.
- Continued adoption of pulsed field ablation portfolio.
- Further progress on Hugo robotic-assisted surgery commercialization.
- Diabetes separation milestones and standalone financial disclosure.
- Debt/cash-flow trajectory and FCF conversion improvement after FY2026 close.

## Valuation Watch Items

- Current DCF memo: [[MDT DCF Valuation 2026-05-19]].
- Base-case fair value from P11 is approximately USD 59.41 per diluted share versus USD 77.32 latest close.
- Bull case reaches approximately USD 89.84 only if WACC is lower and FCF growth is stronger.
- Watch TTM FCF, FY26 actual FCF, non-GAAP to GAAP conversion, and Diabetes separation economics before upgrading the action read.

## Reports / Source Notes

| Note | Type |
|---|---|
| [[MDT_latest_results_source]] | Latest results source note |
| [[MDT_fundamentals]] | Normalized financial facts |
| [[MDT DCF Valuation 2026-05-19]] | DCF valuation |
| [[MDT Decision Memo 2026-05-19]] | Decision memo |

## Follow-Up

- Refresh after Q4 FY26 / FY2026 results on 2026-06-03.
- Normalize FY2026 full-year revenue, operating profit, net income, OCF, capex, FCF, cash, debt, shares, and guidance.
- Track Diabetes separation disclosures, standalone margins, capital structure, and stranded costs.
- Verify whether FY2026 actual FCF supports the TTM FCF anchor used in the current DCF.
- Re-check current price before any action change.

## Missing / Unverified Data

| Item | Status | Notes |
|---|---|---|
| FY26 full-year results | not disclosed | Q4 FY26 results scheduled for 2026-06-03. |
| FY26 full-year FCF guidance | ไม่พบข้อมูลที่ยืนยันได้ | Q3 FY26 official sources disclose 9M FCF only. |
| Product/division-level profitability | not disclosed | Segment revenue is disclosed; product-level profit is not. |
| Diabetes standalone post-separation financials | ไม่พบข้อมูลที่ยืนยันได้ | No standalone public-company financials in extracted sources. |
| Detailed post-CathWorks / Anteris financial contribution | not fully disclosed | Transaction details do not provide complete run-rate P&L contribution. |
| Investor-specific position size, tax basis, required return | not provided | Needed for portfolio-specific add/hold/trim sizing. |
