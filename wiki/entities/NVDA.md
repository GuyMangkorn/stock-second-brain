---
type: entity
ticker: NVDA
company: NVIDIA Corporation
market: Nasdaq Global Select Market
currency: USD
period_type: mixed
reporting_scope: Q1 FY2027 quarter ended 2026-04-26 and FY2026 annual baseline
latest_period: Q1 FY2027
latest_period_end: 2026-04-26
latest_total_revenue_usd_m: 81615
latest_net_income_usd_m: 58321
source_gap_count: 7
source_gaps:
  - Full earnings transcript / Q&A not ingested.
  - Named hyperscaler demand and backlog not disclosed.
  - Reporting taxonomy is changing to Data Center / Edge Computing.
  - Market data must be refreshed before trading.
  - Marketable equity securities excluded from conservative net cash valuation input.
  - China export-control sensitivity remains material.
  - Customer concentration exists but named customers are not disclosed.
source_notes:
  - raw/imports/NVDA_latest_results_source.md
  - raw/imports/NVDA_market_quote_2026-06-25.md
normalized_markdown: raw/financials/NVDA_fundamentals.md
normalized_json: raw/financials/NVDA_fundamentals.json
tags:
  - entity/company
  - ticker/NVDA
---

# NVDA - NVIDIA Corporation

## Snapshot

| Item | Value |
|---|---|
| Ticker | NVDA |
| Company | NVIDIA Corporation |
| Market | Nasdaq Global Select Market |
| Currency | USD |
| Latest period | Q1 FY2027, three months ended 2026-04-26 |
| Reporting scope | Q1 FY2027 and FY2026 annual baseline |
| Current price check | USD 195.03 at 2026-06-25 12:43 PM EDT, StockAnalysis |
| Market cap check | USD 4.72T at 2026-06-25 12:43 PM EDT, StockAnalysis |
| Normalized file | `raw/financials/NVDA_fundamentals.md` |

## Source Map

| Priority | Source | Status | Notes |
|---:|---|---|---|
| 1 | SEC / official filings | Complete for latest Q1 FY2027 and FY2026 baseline | Q1 FY2027 Form 10-Q and FY2026 Form 10-K captured. |
| 2 | Earnings transcript / call materials | Partial | Official press release and CFO commentary captured; full Q&A transcript not ingested. |
| 3 | Financial statements / metrics | Complete for core DCF inputs | Cash, debt, FCF, shares, guidance, current price captured. |
| 4 | News / web context | Minimal | No durable news context added beyond market quote. |

## Business Model

NVIDIA เป็น AI infrastructure platform company ที่รายได้หลักมาจาก accelerated computing, GPUs, networking, software ecosystem และ systems สำหรับ data centers. รายได้ FY2026 ถูกครอบงำโดย Data Center ที่ USD 193.737B จาก total revenue USD 215.938B ตาม FY2026 Form 10-K.

ใน Q1 FY2027 บริษัทเริ่มสื่อสาร reporting framework ใหม่เป็น `Data Center` และ `Edge Computing`; Data Center จะแยกเป็น `Hyperscale` และ `ACIE` ในอนาคต. จุดนี้ทำให้ thesis ต้องดูทั้ง demand จาก hyperscalers, AI clouds, sovereign / enterprise AI และ edge/robotics/automotive แต่ไม่ควรเทียบ segment เก่ากับ segment ใหม่แบบตรง ๆ โดยไม่ติด caveat.

## Segments / Revenue Mix

| End Market | FY2026 Revenue | FY2025 Revenue | FY2024 Revenue |
|---|---:|---:|---:|
| Data Center | 193,737 | 115,186 | 47,525 |
| Gaming | 16,042 | 11,350 | 10,447 |
| Professional Visualization | 3,191 | 1,878 | 1,553 |
| Automotive | 2,349 | 1,694 | 1,091 |
| OEM and Other | 619 | 389 | 306 |

Q1 FY2027 official release ระบุ Data Center revenue USD 75.2B และ Edge Computing revenue USD 6.4B. Under prior sub-market labels, Data Center compute revenue was USD 60.4B and Data Center networking revenue was USD 14.8B.

## Financial Facts

| Metric | Latest Verified Value | Period | Source |
|---|---:|---|---|
| Revenue | 81,615 | Q1 FY2027 | Q1 FY2027 press release |
| Net income | 58,321 | Q1 FY2027 | Q1 FY2027 press release |
| Operating cash flow | 50,344 | Q1 FY2027 | Q1 FY2027 press release |
| Free cash flow | 48,554 | Q1 FY2027 | Q1 FY2027 press release company reconciliation |
| Cash and equivalents | 13,237 | 2026-04-26 | Q1 FY2027 press release |
| Marketable debt securities | 37,098 | 2026-04-26 | Q1 FY2027 press release |
| Marketable equity securities | 30,237 | 2026-04-26 | Q1 FY2027 press release |
| Short-term debt | 1,000 | 2026-04-26 | Q1 FY2027 press release |
| Long-term debt | 7,470 | 2026-04-26 | Q1 FY2027 press release |
| Weighted diluted shares | 24,391 | Q1 FY2027 | Q1 FY2027 press release |
| Shares outstanding | 24.22B | 2026-06-25 12:43 PM EDT | StockAnalysis |
| FY2026 calculated FCF | 96,575 | FY2026 | FY2026 Form 10-K calculation |
| TTM calculated FCF | 118,994 | TTM through Q1 FY2027 | FY2026 FCF - Q1 FY2026 FCF + Q1 FY2027 FCF |

## Charts

See `raw/financials/NVDA_fundamentals.md` for source-backed quarterly YoY, annual, segment, cash-flow, and balance-sheet chart blocks.

## Transcript / Management Commentary

Management described AI factory buildout and agentic AI demand as accelerating. CFO commentary defines FCF as GAAP operating cash flow less purchases related to property/equipment/intangible assets and principal payments on property/equipment/intangible assets.

Guidance for Q2 FY2027 is revenue of USD 91.0B +/- 2%, GAAP gross margin of 74.9% +/- 50 bps, non-GAAP gross margin of 75.0% +/- 50 bps, GAAP operating expenses of about USD 8.5B, non-GAAP operating expenses of about USD 8.3B, and FY2027 tax rates of 16.0%-18.0% excluding discrete items. Outlook does not assume Data Center compute revenue from China.

## Thesis

### Bull Case

NVDA ยังเป็น scarce AI infrastructure leader: Q1 FY2027 revenue โต 85% YoY, Data Center revenue โต 92% YoY, FCF conversion สูงมาก และ balance sheet เป็น net cash แบบ conservative หากนับ cash + marketable debt securities หัก total debt. ถ้า AI factory capex cycle ยาวกว่าที่ตลาดกลัว และ networking/software/system-level attach rate เพิ่มขึ้น, FCF base อาจโตเร็วพอให้ valuation ปัจจุบันดูสมเหตุสมผลขึ้น.

### Bear Case

ราคา USD 195.03 กับ market cap USD 4.72T ต้องการให้ FCF โตต่อจาก TTM base ที่สูงมากโดยไม่ compress margin หรือ multiple. ความเสี่ยงหลักคือ export controls/China, customer concentration, supply chain dependence, hyperscaler capex digestion, competition/custom silicon, และ segment taxonomy ใหม่ที่ทำให้ trend readability ลดลง.

### Key Debate

คำถามสำคัญไม่ใช่แค่ "AI demand แข็งไหม" แต่คือ market price ได้ discount demand ไปมากแค่ไหนแล้ว. Base DCF ที่ใช้ TTM FCF USD 118.994B และ growth fade 28% -> 6% ยังได้ fair value ต่ำกว่าราคาอย่างมาก แปลว่าตลาดกำลังให้ credit กับ growth runway ที่ยาวและ/หรือ margin durability สูงกว่า conservative base case.

## Risks

- AI capex cycle อาจชะลอหลัง hyperscalers build capacity ล่วงหน้า.
- Export controls และ China revenue restrictions อาจกด addressable demand.
- Customer concentration: FY2026 Form 10-K ระบุ direct customers รายใหญ่คิดเป็น 22% และ 14% ของ revenue.
- Custom silicon จาก hyperscalers หรือคู่แข่งอาจกด pricing / share.
- Marketable equity securities มี fair-value volatility และไม่ควรนับเป็น cash เต็ม ๆ โดยไม่ติด caveat.
- Valuation sensitivity สูงเพราะ terminal value เป็นสัดส่วนใหญ่ของ DCF.

## Catalysts

- Q2 FY2027 results เทียบกับ revenue guidance USD 91.0B +/- 2%.
- Evidence ว่า Data Center demand ไม่ได้พึ่ง China compute revenue.
- Adoption ของ Vera Rubin, networking, NVLink Fusion, and AI factory systems.
- Gross margin durability around 75%.
- Buyback execution under the expanded USD 80.0B authorization.

## Valuation Watch Items

- Fresh price and market cap before any action call.
- TTM FCF conversion vs Q2 FY2027 revenue/gross margin guide.
- Whether marketable equity securities should be included in excess cash for a specific valuation lens.
- Reverse DCF: what FCF growth the current USD 195.03 price requires.
- Terminal value share of DCF remains high, so margin of safety should be explicit.

## Reports / Source Notes

- `raw/imports/NVDA_latest_results_source.md`
- `raw/imports/NVDA_market_quote_2026-06-25.md`
- `raw/financials/NVDA_fundamentals.md`
- `wiki/analysis/valuations/NVDA DCF Valuation 2026-06-26.md`
- `wiki/analysis/decisions/NVDA Decision Memo 2026-06-26.md`

## Follow-Up

- Ingest full Q1 FY2027 earnings call transcript / Q&A.
- Refresh market quote before any trade.
- Re-run valuation after Q2 FY2027 results.
- Track Data Center / Edge Computing taxonomy transition in future financial notes.

## Missing / Unverified Data

- Full earnings transcript / Q&A: ไม่พบข้อมูลที่ยืนยันได้ใน ingest นี้.
- Named hyperscaler demand / backlog: not disclosed.
- Current market data is intraday from StockAnalysis and should be refreshed before trading.
- Peer multiple set was not built; decision relies mainly on DCF, FCF yield, and official-source quality checks.
