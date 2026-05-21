---
type: entity
ticker: CRWV
company: CoreWeave, Inc.
market: Nasdaq Global Select Market
currency: USD
period_type: mixed
reporting_scope: "Q1 2026 quarter ended 2026-03-31; FY2025 annual baseline; FY2026 guidance; market-data check 2026-05-21"
latest_period: Q1 2026
latest_period_end: 2026-03-31
latest_total_revenue_usd_m: 2078
latest_net_income_usd_m: -740
source_gap_count: 9
source_gaps:
  - FY2026 full-year actual results are not available as of the 2026-05-21 source check.
  - FY2026 free cash flow guidance is not disclosed.
  - A source-backed positive normalized FCF base is not available.
  - Revenue by product line, customer type, or individual major customer is not fully disclosed.
  - Segment-level operating income and segment-level FCF are not disclosed.
  - Post-quarter DDTL 5.0 draw amounts and exact pro forma debt outstanding are not verified in a filing-level balance sheet.
  - GAAP net income or EPS guidance for FY2026 was not verified.
  - Current market quote is provider-sourced and pre-market on 2026-05-21.
  - Investor-specific cost basis, position size, tax status, and required return were not provided.
source_notes:
  - raw/imports/CRWV_latest_results_source.md
normalized_markdown: raw/financials/CRWV_fundamentals.md
normalized_json: raw/financials/CRWV_fundamentals.json
tags:
  - entity/company
  - ticker/CRWV
---

# CRWV - CoreWeave, Inc.

## Snapshot

| Item | Value |
|---|---|
| Ticker | CRWV |
| Company | CoreWeave, Inc. |
| Market | Nasdaq Global Select Market |
| Currency | USD |
| Latest period | Q1 2026 quarter ended 2026-03-31 |
| Latest official result | Q1 2026 results released 2026-05-07; Q1 2026 Form 10-Q filed 2026-05-15 |
| Current price check | USD 101.28 close on 2026-05-20; USD 105.95 pre-market on 2026-05-21 8:15 AM EDT |
| Market cap / shares out | USD 55.26B / 545.57M provider values |
| Enterprise value | USD 88.14B provider value |
| Normalized file | `raw/financials/CRWV_fundamentals.md` |
| Decision read | AVOID-new-capital / WATCHLIST until positive FCF path is source-backed |

## Source Map

| Priority | Source | Status | Notes |
|---:|---|---|---|
| 1 | Q1 2026 Form 10-Q | Verified | Latest quarterly financials, cash, debt, lease obligations, cash flow, and share count. |
| 1 | FY2025 Form 10-K | Verified | Annual baseline and business/risk context. |
| 2 | Q1 2026 earnings release | Verified | Official Q1 results, backlog, adjusted EBITDA, capex, and summary metrics. |
| 2 | Q1 2026 outlook presentation | Verified | Q2 and FY2026 guidance. |
| 2 | Q1 2026 earnings call transcript | Verified | Management commentary on demand, capex, leverage, and guidance context. |
| 3 | StockAnalysis market quote / statistics | Verified as provider source | Fresh current market data checked 2026-05-21. |
| 4 | DDTL 5.0 facility announcement | Context only | Post-quarter financing context; not used as reported quarter-end debt. |

## Business Model

CoreWeave เป็น specialized cloud infrastructure company สำหรับ accelerated computing workloads โดยเน้น GPU cloud, AI training/inference, managed software, and adjacent application software. Business model คือ capacity-first: บริษัทลงทุนล่วงหน้าใน data centers, GPUs, networking, power, and long-lived customer contracts แล้วรับ revenue จาก compute capacity และ related services.

จุดแข็งของโมเดลคือ demand visibility สูงมากจาก backlog/RPO และการอยู่ใน AI infrastructure bottleneck. จุดอ่อนคือ capital intensity หนักมาก: revenue โตเร็ว แต่ต้องใช้ debt, leases, supplier financing, and capex ขนาดใหญ่ก่อนที่ FCF จะเห็นผล. นี่ทำให้ CRWV เป็น growth infrastructure story มากกว่า high-margin software story ในตอนนี้.

## Segments / Revenue Mix

ไม่พบข้อมูลที่ยืนยันได้ for reportable segment revenue mix. Source-backed operating view currently uses company-level revenue, backlog, RPO, adjusted EBITDA, capex, and cash-flow data.

| Operating Indicator | Q1 2026 / Latest Value | Read |
|---|---:|---|
| Revenue | USD 2.078B | 111.7% YoY growth, but still paired with heavy capex. |
| Revenue backlog | USD 99.355B | Very large demand visibility versus TTM revenue. |
| Remaining performance obligations | USD 98.767B | Long-dated contracted revenue profile. |
| Adjusted EBITDA backlog | USD 62.983B | Management-defined profitability indicator, not cash flow. |
| FY2026 revenue guidance | USD 12B to USD 13B | Implies large step-up from FY2025 revenue of USD 5.131B. |
| FY2026 capex guidance | USD 31B to USD 35B | Central risk for FCF and balance sheet. |

## Financial Facts

- Q1 2026 revenue: USD 2.078B, up from USD 982M in Q1 2025.
- Q1 2026 net loss: USD 740M.
- Q1 2026 adjusted EBITDA: USD 1.157B.
- Q1 2026 FCF: USD -4.711B from OCF USD 2.984B minus cash capex USD 7.695B.
- TTM FCF ended 2026-03-31: USD -10.616B by SEC-based calculation.
- Cash and marketable securities at 2026-03-31: USD 2.266B.
- Cash, restricted cash, and marketable securities at 2026-03-31: USD 3.342B.
- Total debt excluding leases at 2026-03-31: USD 24.859B.
- Debt-like obligations including leases at 2026-03-31: USD 35.147B.
- Total shares outstanding at 2026-04-30: 545.570M.
- FY2026 guidance: revenue USD 12B to USD 13B, adjusted operating income USD 900M to USD 1.1B, capex USD 31B to USD 35B, exit ARR USD 18B to USD 19B.

## Charts

See `raw/financials/CRWV_fundamentals.md` for quarterly YoY, annual trend, cash-flow/capex, and balance-sheet chart blocks.

## Transcript / Management Commentary

Management commentary is clearly bullish on demand and capacity utilization. The key P6 read is that CoreWeave has unusually strong backlog and ARR guidance, but the official materials also show this growth requires very large capex and interest expense. Q2 2026 guidance alone includes USD 7B to USD 9B of capex and USD 650M to USD 730M of interest expense.

สำหรับ thesis, demand is not the only question. The harder question is whether revenue backlog converts into durable equity value after capex, financing cost, lease obligations, and dilution. Official sources do not yet provide FY2026 FCF guidance or a source-backed path to positive normalized FCF.

## Thesis

### Bull Case

CRWV could be one of the clearest pure-play beneficiaries of AI compute scarcity. Revenue backlog of about USD 99.4B and FY2026 revenue guidance of USD 12B to USD 13B give unusually strong top-line visibility. If utilization stays high, financing remains available, and capex converts into long-lived contracted revenue, equity upside could be meaningful even from a high headline valuation.

### Bear Case

The company is not yet source-backed FCF positive. TTM FCF is about USD -10.6B, FY2026 capex guidance is USD 31B to USD 35B, and debt-like obligations including leases were about USD 35.1B at 2026-03-31 before considering post-quarter financing context. ถ้า funding cost rises, customer demand shifts, capacity ramps late, or contract economics disappoint, equity value can be very sensitive.

### Key Debate

คำถามหลักคือ backlog quality and unit economics. Revenue growth is verified; positive free cash flow durability is not. Until the vault has a source-backed positive FCF base or clear FCF guidance, CRWV should be treated as high-growth infrastructure speculation, not a DCF-supported compounder.

## Risks

- FCF is materially negative because capex is far above operating cash flow.
- Balance sheet risk is high due debt, leases, interest expense, and continuous funding needs.
- Revenue backlog may be long-dated and depends on capacity delivery and customer execution.
- Customer concentration is a material risk but detailed customer-level economics are not disclosed.
- GPU supply, power availability, data-center delivery, and vendor financing terms can change economics quickly.
- Public-market trading history is short, so market multiple history is thin.
- Valuation can compress if AI infrastructure sentiment cools or financing costs rise.

## Catalysts

- FY2026 quarters showing revenue guidance conversion without further negative FCF acceleration.
- More granular disclosure on FCF trajectory, customer concentration, contract duration, and unit economics.
- Lower financing cost, longer maturity funding, or improved lease/debt structure.
- Evidence that incremental capacity produces operating leverage beyond adjusted EBITDA.
- Any path to positive normalized FCF after the 2026 capex build.

## Valuation Watch Items

- P11 stopped before a precise DCF fair value because a source-backed positive normalized FCF base is not available.
- Fresh market data checked 2026-05-21: close price USD 101.28, market cap USD 55.26B, enterprise value USD 88.14B, shares out 545.57M.
- EV / TTM revenue is about 14.15x; EV / FY2026 revenue guidance midpoint is about 7.05x.
- TTM FCF is USD -10.616B and FY2026 FCF guidance is not disclosed, so FCF yield and EV/FCF are not meaningful as positive valuation supports.

## Reports / Source Notes

- [[CRWV_latest_results_source]]
- [[CRWV_fundamentals]]
- [[CRWV DCF Valuation 2026-05-21]]
- [[CRWV Decision Memo 2026-05-21]]

## Follow-Up

- Refresh after Q2 2026 results with attention to revenue, adjusted operating income, adjusted EBITDA, OCF, cash capex, FCF, cash, restricted cash, debt, leases, shares, RPO, backlog, and interest expense.
- Track whether FY2026 capex guidance stays within USD 31B to USD 35B.
- Look for any official disclosure of FY2026 FCF guidance or a positive FCF inflection timeline.
- Re-run P11 only when a positive normalized FCF base or explicit FCF bridge becomes source-backed.

## Missing / Unverified Data

- FY2026 full-year actual results are not available as of the 2026-05-21 source check.
- FY2026 free cash flow guidance is not disclosed.
- A source-backed positive normalized FCF base is not available; FY2025, Q1 2026, and TTM FCF are all negative by `OCF - cash capex`.
- Revenue by product line, customer type, or individual major customer is not fully disclosed.
- Segment-level operating income and segment-level FCF are not disclosed.
- Post-quarter DDTL 5.0 draw amounts and exact pro forma debt outstanding are not verified in a filing-level balance sheet.
- GAAP net income or EPS guidance for FY2026 was not verified.
- Current market quote is provider-sourced and pre-market on 2026-05-21, not a company filing and not a post-2026-05-21 close.
- Investor-specific cost basis, position size, tax status, and required return were not provided.
