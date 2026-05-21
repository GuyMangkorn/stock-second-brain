---
type: entity
ticker: AMAT
company: Applied Materials, Inc.
market: Nasdaq Global Select Market
currency: USD
period_type: quarterly + annual
reporting_scope: Q2 FY2026 and six months ended 2026-04-26 plus FY2025 annual baseline
latest_period: Q2 FY2026
latest_period_end: 2026-04-26
latest_total_revenue_usd_m: 7910
latest_net_income_usd_m: 2806
source_gap_count: 8
source_gaps:
  - Q2 FY2026 Form 10-Q was not found as of the 2026-05-21 source search.
  - Official full Q2 FY2026 call transcript / Q&A was not verified.
  - FY2026 full-year FCF guidance is not disclosed.
  - Exact Q2 period-end shares outstanding was not verified.
  - Segment-level FCF is not disclosed.
  - Customer-specific AI/HBM/advanced-packaging revenue and margins are not disclosed.
  - Market-data provider variance requires refresh before action changes.
  - Investor-specific cost basis, position size, tax status, and required return were not provided.
source_notes:
  - raw/imports/AMAT_latest_results_source.md
normalized_markdown: raw/financials/AMAT_fundamentals.md
normalized_json: raw/financials/AMAT_fundamentals.json
tags:
  - entity/company
  - ticker/AMAT
---

# AMAT - Applied Materials, Inc.

## Snapshot

| Item | Value |
|---|---|
| Ticker | AMAT |
| Company | Applied Materials, Inc. |
| Market | Nasdaq Global Select Market |
| Currency | USD |
| Latest period | Q2 FY2026, quarter ended 2026-04-26 |
| Reporting scope | Q2 FY2026 and 6M FY2026 plus FY2025 annual baseline |
| Normalized file | `raw/financials/AMAT_fundamentals.md` |
| Latest price check | USD 426.85 on 2026-05-20 at 4:00 PM EDT; checked 2026-05-21 |
| Current action read | AVOID-new-capital / WAIT-for-better-entry |

AMAT เป็น semiconductor equipment leader ที่อยู่ตรงกลาง AI infrastructure cycle: leading-edge logic, DRAM/HBM, advanced packaging และ installed-base services. Q2 FY2026 แข็งมากใน revenue, margin, EPS และ management raised tone ต่อ calendar 2026 semi equipment growth แต่ stock price สะท้อน growth ไปไกลมากเมื่อเทียบกับ source-backed TTM FCF yield ประมาณ 1.6% และ DCF ที่ไม่ใช้ FCF เดาเอง.

## Source Map

| Priority | Source | Status | Notes |
|---:|---|---|---|
| 1 | SEC / official filings | Found | Q2 FY2026 Form 8-K / Exhibit 99.1, accession `0001628280-26-035071`; FY2025 Form 10-K reviewed. |
| 1 | Official company results | Found | Applied Materials Q2 FY2026 earnings release used for financials, cash flow, balance sheet, segments, and Q3 outlook. |
| 2 | Earnings transcript / call material | Partial | Official webcast referenced by company; full written company-hosted Q&A transcript not verified. |
| 3 | Financial statements / metrics | Found | FinancialContent used only for fresh market price; market cap calculated from price and source-backed weighted-average basic shares. |
| 4 | News / web context | Not used for durable financial facts | Official sources were sufficient for core financial workflow. |

## Business Model

Applied Materials sells equipment, services, and software used to manufacture semiconductors and advanced displays. The core business is wafer fabrication equipment and materials engineering systems; the services business monetizes the installed base through spares, service agreements, upgrades, and productivity tools.

| Business line | Revenue mechanism | Durable driver | Primary source |
|---|---|---|---|
| Semiconductor Systems | Process equipment for deposition, etch, process control, thermal, CMP, implant and related materials engineering steps | Leading-edge logic transitions, DRAM/HBM intensity, advanced packaging, AI data-center semiconductor demand | FY2025 Form 10-K and Q2 FY2026 Exhibit 99.1. |
| Applied Global Services | Spares, service agreements, upgrades, equipment and productivity services for installed base | Growing installed base, fab utilization, chamber count, long-term service agreements | FY2025 Form 10-K and Q2 FY2026 Exhibit 99.1. |
| Other / Display and adjacent markets | Display and adjacent equipment categories not reportable as separate segments | Display cycle and adjacent process opportunities | FY2025 Form 10-K and Q2 FY2026 Exhibit 99.1. |

## Segments / Revenue Mix

| Segment | Q2 FY2026 Revenue | Q2 FY2026 Mix | YoY Change | Operating Margin | Source |
|---|---:|---:|---:|---:|---|
| Semiconductor Systems | USD 5.965B | 75.41% | 10.44% | 35.1% | Q2 FY2026 Exhibit 99.1. |
| Applied Global Services | USD 1.665B | 21.05% | 17.25% | 29.2% | Q2 FY2026 Exhibit 99.1. |
| Other | USD 0.280B | 3.54% | 0.36% | -20.0% | Q2 FY2026 Exhibit 99.1. |

Semiconductor Systems is the center of gravity. Within that segment, Q2 FY2026 mix was 67% Foundry/logic/other, 29% DRAM, and 4% Flash memory. DRAM exposure matters because HBM and memory architecture shifts can raise materials intensity, but customer-specific HBM revenue and margins are not disclosed.

## Financial Facts

| Metric | Latest value | Source |
|---|---:|---|
| Q2 FY2026 revenue | USD 7.910B | Q2 FY2026 Exhibit 99.1. |
| Q2 FY2026 GAAP operating margin | 31.9% | Q2 FY2026 Exhibit 99.1. |
| Q2 FY2026 GAAP net income | USD 2.806B | Q2 FY2026 Exhibit 99.1. |
| Q2 FY2026 diluted EPS / non-GAAP EPS | USD 3.51 / USD 2.86 | Q2 FY2026 Exhibit 99.1. |
| Q2 FY2026 non-GAAP FCF | USD 0.210B | Q2 FY2026 Exhibit 99.1. |
| 6M FY2026 calculated FCF | USD 1.250B | OCF 2.531B - capex 1.281B. |
| FY2025 calculated FCF | USD 5.698B | FY2025 Form 10-K OCF 7.958B - capex 2.260B. |
| TTM calculated FCF | USD 5.343B | FY2025 FCF + 6M FY2026 FCF - 6M FY2025 FCF. |
| Cash + short-term investments | USD 8.241B | Q2 FY2026 Exhibit 99.1. |
| Total debt | USD 6.455B | Q2 FY2026 Exhibit 99.1; short-term debt + long-term debt. |
| Net cash | USD 1.786B | Cash + short-term investments - total debt. |
| Q3 FY2026 revenue guidance | USD 8.950B +/- USD 0.500B | Q2 FY2026 Exhibit 99.1. |
| Q3 FY2026 non-GAAP EPS guidance | USD 3.36 +/- USD 0.20 | Q2 FY2026 Exhibit 99.1. |

## Charts

See `raw/financials/AMAT_fundamentals.md` for source-backed quarterly YoY, YTD, annual, segment mix, cash-flow/capex, and balance-sheet chart blocks.

## Transcript / Management Commentary

Management commentary in the official Q2 release is bullish: Applied said Q2 delivered record revenue and earnings, and management now expects the semiconductor equipment business to grow more than 30% in calendar 2026. The stated drivers are AI infrastructure build-out, leadership in leading-edge logic, DRAM and advanced packaging, and operational readiness to support customer growth.

สิ่งที่ต้องระวังคือ management tone นี้ยังไม่เท่ากับ source-backed FCF guidance. Q2 FCF was only USD 210M and 6M FY2026 FCF was below 6M FY2025 because capex and working-capital/inventory build increased. This may be deliberate capacity preparation, but DCF should not convert it into normalized FCF without further evidence.

## Thesis

### Bull Case

AMAT อยู่ในตำแหน่งดีมากสำหรับ AI capex cycle เพราะลูกค้าต้องการ more advanced logic, more DRAM/HBM, และ advanced packaging. Semiconductor Systems delivered USD 5.965B revenue in Q2 FY2026, AGS grew faster than company average, and Q3 guide implies another step-up in revenue and non-GAAP EPS. Net cash balance sheet gives flexibility for dividends, buybacks, R&D, and acquisitions like NEXX.

ถ้า calendar 2026 equipment growth >30% แปลเป็น sustained FCF growth หลัง inventory/capex build, AMAT could deserve a premium multiple. The business quality and strategic position are real.

### Bear Case

Valuation is the binding issue. At the fresh quote of USD 426.85, approximate market cap is about USD 339B and TTM FCF yield is only about 1.6%. Market EV / TTM FCF is above 60x. That requires either much higher normalized FCF or many years of strong growth. Semiconductor equipment is also cyclical, customer-concentrated, export-control sensitive, and exposed to overbuild risk if AI infrastructure capex slows.

Source-backed DCF using latest verified FCF does not support the current price. Without official FY2026 FCF guidance or a clear normalized FCF bridge, new capital needs a larger margin of safety.

### Key Debate

คำถามหลักคือ Q2/H1 FCF weakness เป็น temporary working-capital/capacity build ahead of a major upcycle หรือเป็นสัญญาณว่า market price is capitalizing revenue/EPS momentum while cash conversion has not caught up. Until the FCF bridge is verified, decision read should stay valuation-disciplined.

## Risks

- Semiconductor equipment demand is cyclical and can reverse when customer capex slows.
- AI infrastructure demand may be strong but still vulnerable to overbuild or hyperscaler spending cuts.
- Customer concentration is material; FY2025 10-K disclosed two customers at about 19% and 15% of revenue.
- Export controls, China exposure, tariffs, and geopolitical restrictions can affect shipment timing and demand.
- Q2 FY2026 net income includes investment gains; GAAP net margin should not be treated as recurring operating economics.
- Capex and inventory build are pressuring near-term FCF conversion.
- Product/customer-level AI, HBM, and advanced packaging economics are not disclosed.

## Catalysts

- Q3 FY2026 revenue near or above the USD 8.95B midpoint and non-GAAP EPS near or above USD 3.36.
- FCF recovery in 2H FY2026 after capex and inventory build.
- Further evidence of DRAM/HBM and advanced packaging orders converting into revenue.
- AGS growth and margin durability as installed base expands.
- More disclosure on customer visibility, backlog, HBM/advanced packaging revenue, or normalized FCF.
- Any change in China/export-control exposure, tariffs, or customer capex plans.

## Valuation Watch Items

- Current DCF memo: [[AMAT DCF Valuation 2026-05-21]].
- Base-case fair value is about USD 120.50 per diluted share versus USD 426.85 latest quote, implying about 71.8% downside.
- Bear case is about USD 76.97 and bull case about USD 181.22; even the bull case remains below the market quote because source-backed TTM FCF is low relative to market cap.
- This is not a claim that the business is weak; it is a valuation discipline flag until FCF conversion catches up with revenue/EPS momentum.

## Reports / Source Notes

| Note | Type |
|---|---|
| [[AMAT_latest_results_source]] | Latest results source note |
| [[AMAT_fundamentals]] | Normalized financial facts |
| [[AMAT DCF Valuation 2026-05-21]] | DCF valuation |
| [[AMAT Decision Memo 2026-05-21]] | Decision memo |

## Follow-Up

- Refresh after Q3 FY2026 results with revenue, non-GAAP EPS, OCF, capex, FCF, cash, short-term investments, debt, shares, and updated guidance.
- Verify whether FCF conversion improves after inventory/capacity build.
- Look for official Q2 FY2026 Form 10-Q if filed after this workflow.
- Track exact period-end shares outstanding from the next 10-Q cover page.
- Track China/export-control exposure and customer concentration.
- Refresh price before changing the AVOID-new-capital / WAIT-for-better-entry action read.

## Missing / Unverified Data

| Item | Status | Notes |
|---|---|---|
| Q2 FY2026 Form 10-Q | not found | Latest official detailed source found was 8-K / Exhibit 99.1. |
| Official full Q2 FY2026 call transcript / Q&A | ไม่พบข้อมูลที่ยืนยันได้ | Not used for durable financial facts. |
| FY2026 full-year FCF guidance | not disclosed | DCF uses verified TTM FCF and explicit scenarios. |
| Exact Q2 period-end shares outstanding | not verified | Uses weighted-average shares from Q2 release. |
| Segment-level FCF | not disclosed | Consolidated FCF only. |
| Customer-specific AI/HBM/advanced-packaging revenue and margins | not disclosed | Cannot directly underwrite AI economics. |
| Market-data provider variance | provider-sourced | Refresh before action changes. |
| Investor-specific cost basis, position size, tax status, and required return | not provided | Needed for sizing. |
