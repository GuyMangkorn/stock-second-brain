---
type: entity
ticker: GE
company: GE Aerospace
market: NYSE
currency: USD
period_type: quarterly + annual
reporting_scope: Q1 2026 quarter ended 2026-03-31 plus FY2025 annual baseline
latest_period: Q1 2026
latest_period_end: 2026-03-31
latest_total_revenue_usd_m: 12392
latest_net_income_usd_m: 1904
source_gap_count: 8
source_gaps:
  - Full FY2026 actual results are not disclosed.
  - GAAP reconciliation for FY2026 non-GAAP guidance is not disclosed.
  - Segment-level FCF is not disclosed.
  - Program-level profitability is not disclosed.
  - Customer concentration and airline credit-risk exposure are not disclosed.
  - Excess cash versus insurance/investment securities normalization requires judgment.
  - Market data after the 2026-05-20 close was not verified.
  - Investor-specific cost basis, position size, tax status, and required return were not provided.
source_notes:
  - raw/imports/GE_latest_results_source.md
normalized_markdown: raw/financials/GE_fundamentals.md
normalized_json: raw/financials/GE_fundamentals.json
tags:
  - entity/company
  - ticker/GE
---

# GE - GE Aerospace

## Snapshot

| Item | Value |
|---|---|
| Ticker | GE |
| Company | GE Aerospace |
| Market | NYSE |
| Currency | USD |
| Latest period | Q1 2026, quarter ended 2026-03-31 |
| Reporting scope | Q1 2026 quarter ended 2026-03-31 plus FY2025 annual baseline |
| Normalized file | `raw/financials/GE_fundamentals.md` |
| Latest price check | USD 300.17 close on 2026-05-20; checked 2026-05-21 Asia/Bangkok |
| Current action read | AVOID-new-capital / WAIT; HOLD only if already owned and position size is intentional |

## Source Map

| Priority | Source | Status | Notes |
|---:|---|---|---|
| 1 | SEC / official filings | Available | Q1 2026 Form 10-Q and FY2025 Form 10-K reviewed. |
| 1 | Official company results | Available | Q1 2026 earnings release used for results, segment data, FCF reconciliation, and guidance. |
| 2 | Earnings transcript / call material | Available | GE-hosted LSEG Q1 2026 transcript reviewed for commentary; no unsupported numbers normalized from it. |
| 3 | Financial statements / metrics | Available | Stooq used only for fresh market-data check; official SEC share count takes priority. |
| 4 | News / web context | Limited | Not needed for core financial facts in this pass. |

## Business Model

GE Aerospace เป็น pure-play aerospace propulsion, services, and systems company หลัง GE Vernova separation. ธุรกิจหลักอยู่ใน engine installed base, spare parts, long-term service agreements, MRO, commercial engine deliveries, defense engines, propulsion, and additive technologies.

Quality ของ business อยู่ที่ installed base และ aftermarket economics: GE ระบุ installed base ประมาณ 50,000 commercial engines และ 30,000 military aircraft engines, ขณะที่ FY2025 Form 10-K ระบุว่า company operates through two reportable segments: Commercial Engines & Services และ Defense & Propulsion Technologies. Narrative สำคัญคือ service revenue โตเร็วกว่า equipment, backlog/RPO ใหญ่, และ supply chain execution ผ่าน FLIGHT DECK เป็นตัวปลดล็อก output.

## Segments / Revenue Mix

| Segment / category | Q1 2026 Revenue | Q1 2026 Mix of adjusted revenue | Q1 2026 YoY | Q1 2026 Profit | Q1 2026 Profit Margin | Source |
|---|---:|---:|---:|---:|---:|---|
| Commercial Engines & Services | USD 8.920B | 76.8% | 34% | USD 2.356B | 26.4% | GE Q1 2026 release / Form 10-Q. |
| Defense & Propulsion Technologies | USD 3.214B | 27.7% | 19% | USD 0.379B | 11.8% | GE Q1 2026 release / Form 10-Q. |
| Corporate Cost & Eliminations | USD (0.519B) | not meaningful | not meaningful | USD (0.206B) | not meaningful | GE Q1 2026 release; non-GAAP. |

CES คือ value driver หลัก: Q1 2026 revenue โต 34%, services revenue โต 39%, internal shop visit revenue โต 35%, spare parts revenue โตมากกว่า 25%, และ equipment revenue โต 20%. DPT โตดีเช่นกัน แต่ margin ต่ำกว่าและ mix/defense investment pressure ยังต้องติดตาม.

## Financial Facts

| Metric | Latest value | Source |
|---|---:|---|
| Q1 2026 total revenue | USD 12.392B | GE Q1 2026 Form 10-Q. |
| Q1 2026 adjusted revenue | USD 11.614B | GE Q1 2026 release; non-GAAP. |
| Q1 2026 operating profit / margin | USD 2.528B / 21.8% | GE Q1 2026 release; non-GAAP. |
| Q1 2026 net income attributable to common shareholders | USD 1.904B | GE Q1 2026 Form 10-Q. |
| Q1 2026 continuing diluted EPS / adjusted EPS | USD 1.83 / USD 1.86 | GE Q1 2026 Form 10-Q / release. |
| Q1 2026 FCF | USD 1.658B | GE Q1 2026 release; non-GAAP. |
| FY2025 FCF | USD 7.694B | GE FY2025 Form 10-K; non-GAAP. |
| TTM FCF | USD 7.901B | FY2025 FCF - Q1 2025 FCF + Q1 2026 FCF. |
| Cash, cash equivalents and restricted cash | USD 10.981B | GE Q1 2026 Form 10-Q. |
| Total borrowings | USD 20.277B | GE Q1 2026 Form 10-Q calculation. |
| Net debt using cash only | USD 9.296B | Total borrowings - cash. |
| FY2026 FCF guidance | USD 8.0B to USD 8.4B | GE Q1 2026 release; non-GAAP. |
| FY2026 adjusted EPS guidance | USD 7.10 to USD 7.40 | GE Q1 2026 release; non-GAAP. |

## Charts

See `raw/financials/GE_fundamentals.md` for source-backed quarterly YoY, annual FCF, segment revenue, cash-flow/capex, and balance-sheet chart blocks.

## Transcript / Management Commentary

Management tone was constructive but careful. Q1 had strong demand and the company said it was trending toward the high end of full-year guidance, but GE kept the range unchanged because assumptions include elevated crude through 3Q, fuel availability pressure, lower global GDP estimates, and flat to low-single-digit departures growth.

Key thesis signals:

- Commercial services are the center of gravity: shop visits, workscopes, and spare parts are driving revenue.
- Backlog/RPO supports visibility, but supply chain delinquency and material flow remain operational constraints.
- Management did not see evidence of aftermarket pre-buying in Q1, which helps reduce the risk that orders were only pull-forward.
- GE9X commentary did not indicate a change to schedule or losses, but program-level economics remain undisclosed.

## Thesis

### Bull Case

GE Aerospace มี rare industrial quality: installed base ใหญ่, aftermarket demand durable, commercial services economics attractive, defense exposure growing, และ management culture หลัง separation ดู focused กว่า legacy GE มาก. Q1 2026 orders +87%, adjusted revenue +29%, operating profit +18%, และ FCF +14% บ่งชี้ว่า demand ไม่ได้อ่อน แม้ macro assumptions เริ่ม conservative.

ถ้า supply chain execution ดีขึ้นต่อเนื่อง, shop visits/spare parts convert เป็น revenue ได้เร็วขึ้น, และ FY2026 FCF ไปแตะ high end ของ USD 8.0B-8.4B guidance, GE อาจรักษา premium multiple ได้ในฐานะ high-quality aerospace compounder.

### Bear Case

ราคา current market สะท้อน quality เกือบเต็มมากแล้ว. ที่ USD 300.17, market cap อยู่ราว USD 313.18B, TTM FCF yield เพียง 2.52%, forward FCF yield จาก FY2026 midpoint เพียง 2.62%, และ forward adjusted P/E ประมาณ 41.4x. Base DCF ที่ใช้ FY2026 FCF guidance midpoint ให้ fair value เพียงประมาณ USD 146.40 ต่อ diluted share, ต่ำกว่าราคาตลาดมาก.

Risks ไม่ใช่เรื่อง business แย่ แต่เป็น valuation + execution: supply chain delinquency, higher install engine mix, growth investment, geopolitical/fuel pressure on airline behavior, undisclosed program profitability, และ run-off insurance/investment securities ที่ทำให้ balance-sheet normalization ซับซ้อน.

### Key Debate

คำถามหลักคือ GE Aerospace ควรซื้อที่ premium multiple แค่ไหน. Business quality ดีจริงและ visibility สูงขึ้น แต่ current price ต้องการ sustained high FCF growth, long-duration aftermarket strength, และ flawless execution แทบพร้อมกัน. ถ้า FCF โตไม่ทัน multiple, downside จาก valuation compression สูง.

## Risks

- Valuation risk: TTM FCF yield 2.52% และ forward adjusted P/E ประมาณ 41.4x.
- Supply chain / delinquency risk: demand ยัง outstrips supply ในบางพื้นที่.
- Commercial aerospace cycle risk from departures, fuel costs, airline credit quality, aircraft production schedules, and shop-visit timing.
- Program risk: GE9X, LEAP ramp, long-term service agreement margin estimates, and defense program execution.
- Margin pressure from equipment mix, investments, inflation, tariffs, and higher install engine growth.
- Run-off insurance / investment securities balance sheet complexity can distort simple net cash or EV calculations.
- Customer concentration and contract-level profitability are not fully disclosed.

## Catalysts

- Q2 2026 results and whether GE keeps trending toward the high end of FY2026 guidance.
- Evidence that spare parts and shop-visit demand converts without margin erosion.
- Better material flow and lower delinquency / improved on-time delivery metrics.
- FY2026 FCF tracking above USD 8.2B midpoint.
- New engine wins and CFM / widebody order momentum.
- Any disclosure that clarifies insurance runoff, investment securities, program profitability, or customer credit exposure.

## Valuation Watch Items

- Current DCF memo: [[GE DCF Valuation 2026-05-21]].
- Base-case fair value from P11 is approximately USD 146.40 per diluted share versus latest checked USD 300.17 close.
- Even the bull DCF scenario reaches only about USD 227.49 because current market price implies a very high FCF multiple.
- Watch FY2026 FCF, CES margin, shop-visit conversion, buybacks, and whether price falls closer to a reasonable FCF yield before upgrading action read.

## Reports / Source Notes

| Note | Type |
|---|---|
| [[GE_latest_results_source]] | Latest results source note |
| [[GE_fundamentals]] | Normalized financial facts |
| [[GE DCF Valuation 2026-05-21]] | DCF valuation |
| [[GE Decision Memo 2026-05-21]] | Decision memo |

## Follow-Up

- Refresh after Q2 2026 results with adjusted revenue, operating profit, FCF, cash, borrowings, shares, buybacks, CES/DPT revenue and margins, RPO, and updated guidance.
- Track whether FY2026 FCF is pacing above the USD 8.2B midpoint.
- Recheck current price before any action change.
- If GE discloses more detail, normalize investment securities, insurance liabilities, and excess cash treatment before relying on a balance-sheet-adjusted DCF.
- Track supply chain delinquency, shop visits, spare parts availability, LEAP/GE9X execution, and defense margin.

## Missing / Unverified Data

| Item | Status | Notes |
|---|---|---|
| Full FY2026 actual results | not disclosed | Q1 2026 is the latest official period found. |
| GAAP reconciliation for FY2026 non-GAAP guidance | not disclosed | GE states reconciliation cannot be provided without unreasonable effort. |
| Segment-level FCF | not disclosed | FCF is disclosed at company level. |
| Program-level profitability | not disclosed | LEAP, GE9X, defense systems, and aftermarket economics are not separated. |
| Customer concentration / airline credit exposure | not disclosed | Management commentary is qualitative. |
| Excess cash vs insurance/investment securities normalization | judgment required | Base DCF uses cash and borrowings, but does not treat all investment securities as excess cash. |
| Market data after 2026-05-20 close | ไม่พบข้อมูลที่ยืนยันได้ | Stooq latest available close was 2026-05-20. |
| Investor-specific tax basis, position size, and required return | not provided | Needed for personalized action sizing. |
