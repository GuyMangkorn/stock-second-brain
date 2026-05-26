---
type: entity
ticker: CRWD
company: CrowdStrike Holdings, Inc.
market: Nasdaq Global Select Market
currency: USD
period_type: mixed
reporting_scope: "Q4 FY2026 and fiscal year ended 2026-01-31; FY2027 guidance; market-data check 2026-05-26"
latest_period: FY2026
latest_period_end: 2026-01-31
latest_total_revenue_usd_m: 4812.005
latest_company_defined_fcf_usd_m: 1235.274
source_gap_count: 9
source_gaps:
  - FY2027 Q1 actual results are not available as of the 2026-05-26 source check.
  - FY2027 free cash flow guidance is not disclosed.
  - Company-hosted full written Q4 FY2026 earnings call transcript / Q&A was not verified.
  - Product-level revenue and profitability by module or platform category are not fully disclosed.
  - Segment-level operating income and segment-level FCF are not disclosed.
  - Customer-level economics, renewal pricing, and contract duration distribution are not disclosed.
  - Ultimate July 19 Incident legal / remediation cost is not fully known.
  - Current market price, market cap, and EV are provider-sourced, not company-filed facts.
  - Investor-specific cost basis, position size, tax status, and required return were not provided.
source_notes:
  - raw/imports/CRWD_latest_results_source.md
normalized_markdown: raw/financials/CRWD_fundamentals.md
normalized_json: raw/financials/CRWD_fundamentals.json
tags:
  - entity/company
  - ticker/CRWD
---

# CRWD - CrowdStrike Holdings, Inc.

## Snapshot

| Item | Value |
|---|---|
| Ticker | CRWD |
| Company | CrowdStrike Holdings, Inc. |
| Market | Nasdaq Global Select Market |
| Currency | USD |
| Latest period | FY2026 fiscal year ended 2026-01-31 |
| Latest official result | Q4/FY2026 results released 2026-03-03; FY2026 Form 10-K filed 2026-03-05 |
| Next result event | Q1 FY2027 results scheduled 2026-06-03 after U.S. market close |
| Current price check | USD 663.46 last close on 2026-05-22; USD 657.01 pre-market on 2026-05-26 8:31 AM EDT |
| Market cap / shares out | USD 168.87B / 254.54M provider values |
| Enterprise value | USD 164.46B provider value |
| Normalized file | `raw/financials/CRWD_fundamentals.md` |
| Decision read | WAIT / AVOID-new-capital at current valuation |

## Source Map

| Priority | Source | Status | Notes |
|---:|---|---|---|
| 1 | FY2026 Form 10-K | Verified | Annual financial statements, cash, debt, shares, business model, and risks. |
| 2 | Q4/FY2026 earnings release | Verified | Latest official results, ARR, company-defined FCF, module adoption, and FY2027 guidance. |
| 2 | Q4 FY2026 earnings call transcript | Partially verified as secondary | Company-hosted full written transcript not found; secondary transcript used only for commentary context. |
| 3 | StockAnalysis quote/statistics | Verified as provider source | Fresh market price, market cap, EV, shares, cash/debt cross-check, and valuation ratios checked 2026-05-26. |
| 4 | Q1 FY2027 results date announcement | Verified | Confirms next actual result is scheduled for 2026-06-03 and is not available yet. |

## Business Model

CrowdStrike เป็น cybersecurity software company ที่ขาย Falcon platform แบบ cloud-native subscription. Core model คือ land-and-expand: ลูกค้าเริ่มจาก module บางส่วน แล้วเพิ่ม endpoint, workload, identity, cloud, SIEM, exposure management, data protection, and AI security modules เข้าไปใน platform เดียวกัน

ความน่าสนใจของ business model คือ recurring revenue, high gross margin, high ARR visibility, and strong platform consolidation narrative. FY2026 ending ARR แตะ USD 5.25B และ module adoption สูงขึ้น: 50% ของ subscription customers ใช้ 6+ modules, 34% ใช้ 7+ modules, และ 24% ใช้ 8+ modules.

ข้อควรระวังคือ GAAP profitability ยังถูกกดด้วย stock-based compensation, acquisition costs, and July 19 Incident-related costs. บริษัทสร้าง FCF ได้สูง แต่ market valuation ตอนนี้ให้ multiple สูงมาก จึงต้องแยก business quality ออกจาก price discipline.

## Segments / Revenue Mix

CrowdStrike reports revenue as subscription and professional services. Segment-level operating income / FCF by module was not verified.

| Revenue Stream | FY2026 Revenue | Share of FY2026 Revenue | Read |
|---|---:|---:|---|
| Subscription | USD 4.565B | 94.9% | Core recurring SaaS/platform revenue. |
| Professional services | USD 0.247B | 5.1% | Smaller services component, linked to threat environment and implementation work. |
| Total | USD 4.812B | 100.0% | Revenue grew 21.7% YoY in FY2026. |

## Financial Facts

- FY2026 revenue: USD 4.812B, up 21.7% from FY2025.
- FY2026 subscription revenue: USD 4.565B, about 94.9% of total revenue.
- FY2026 gross profit: USD 3.593B; gross margin 74.7%.
- FY2026 GAAP operating loss: USD 293.3M.
- FY2026 GAAP net loss attributable to CrowdStrike: USD 162.5M.
- FY2026 non-GAAP operating income: USD 1.046B; non-GAAP operating margin 21.8%.
- FY2026 operating cash flow: USD 1.612B.
- FY2026 company-defined FCF: USD 1.235B; FCF margin 25.7%.
- Cash and cash equivalents at 2026-01-31: USD 5.230B.
- Long-term debt at 2026-01-31: USD 745.5M.
- Class A shares outstanding at 2026-01-31: 253.363M.
- FY2027 guidance: revenue USD 5.868B to USD 5.928B, ARR USD 6.466B to USD 6.516B, non-GAAP operating income USD 1.422B to USD 1.462B, non-GAAP EPS USD 4.78 to USD 4.90 using 260M diluted shares.

## Charts

See `raw/financials/CRWD_fundamentals.md` for Q4 YoY, annual trend, revenue mix, cash-flow/capex, and balance-sheet chart blocks.

## Transcript / Management Commentary

Management frames FY2026 as a record year across ARR, operating cash flow, and free cash flow, and presents CrowdStrike as mission-critical infrastructure for AI-era security. The durable read is positive on demand quality: ending ARR reached USD 5.25B, Q4 net new ARR was USD 330.7M, and FY2027 ARR guidance midpoint implies roughly 23.6% growth.

แต่ decision-grade caveat สำคัญคือ official release does not disclose FY2027 FCF guidance. P11 can use a source-backed FY2026 FCF base, but FY2027 FCF must be modeled as an assumption, not a sourced management target.

## Thesis

### Bull Case

CRWD เป็น quality compounder ใน cybersecurity: platform consolidation, high subscription mix, strong ARR growth, net cash balance sheet, and durable FCF generation. ถ้า Falcon platform กลายเป็น control plane สำหรับ AI security และลูกค้าเพิ่ม modules ต่อเนื่อง, revenue growth และ FCF margin อาจ sustain สูงกว่าซอฟต์แวร์ทั่วไปได้.

### Bear Case

ราคาตลาดปัจจุบันสะท้อน perfection สูงมาก. Fresh market data implies roughly 133x EV / company-defined FY2026 FCF and about 28x EV / FY2027 revenue guidance midpoint. ถ้า growth decelerates, July 19 Incident costs linger, AI/security competition intensifies, or SBC dilution remains high, valuation compression can overwhelm business progress.

### Key Debate

คำถามหลักไม่ใช่แค่ว่า CRWD เป็นบริษัทดีหรือไม่. คำถามคือ price already discounts how much excellence. Source-backed DCF base case is far below the market quote, so current action read should emphasize entry discipline.

## Risks

- Valuation risk is high: market price embeds many years of strong growth and FCF conversion.
- FY2027 FCF guidance is not disclosed, so forward cash-flow conversion requires assumptions.
- GAAP losses remain affected by stock-based compensation, acquisition items, and incident-related costs.
- July 19 Incident legal, remediation, reputational, and customer-credit impacts may not be fully settled.
- Cybersecurity competition is intense across endpoint, cloud, identity, SIEM, exposure management, and AI security.
- Product-level revenue and profitability are not disclosed, limiting precision on which modules drive incremental economics.
- Customer-level renewal pricing, duration, and large-account concentration economics are not fully disclosed.

## Catalysts

- Q1 FY2027 results on 2026-06-03 showing ARR / revenue / non-GAAP operating income ahead of guidance without FCF deterioration.
- More explicit FY2027 FCF guidance or cash-flow commentary.
- Continued module adoption and Falcon Flex expansion with stable retention.
- Evidence that July 19 Incident costs decline materially.
- Pullback in stock price that lifts FCF yield and creates margin of safety.

## Valuation Watch Items

- Fresh market data checked 2026-05-26: USD 663.46 last regular-session close, USD 657.01 pre-market quote, USD 168.87B market cap, USD 164.46B EV, 254.54M provider shares out.
- P11 base-case DCF fair value is approximately USD 134 per diluted share using FY2026 company-defined FCF as the starting anchor, 10.0% WACC, 2.5% terminal growth, net cash from filing inputs, and 260M diluted shares.
- Base-case DCF implies about 80% downside versus the USD 663.46 last close; even bull case is far below market price under conservative FCF assumptions.
- Current EV / FY2026 company-defined FCF is about 133x; EV / FY2027 revenue guidance midpoint is about 27.9x.

## Reports / Source Notes

- [[CRWD_latest_results_source]]
- [[CRWD_fundamentals]]
- [[CRWD DCF Valuation 2026-05-26]]
- [[CRWD Decision Memo 2026-05-26]]

## Follow-Up

- Refresh immediately after Q1 FY2027 results on 2026-06-03 with revenue, ARR, net new ARR, non-GAAP operating income, OCF, FCF, cash, debt, shares, and any revised FY2027 guidance.
- Look for official company-hosted transcript or prepared remarks if available after Q1 FY2027.
- Track whether FY2027 FCF margin is closer to FY2026 company-defined FCF margin or affected by working capital / incident payments.
- Re-run P11 if price materially changes or official FY2027 FCF guidance appears.

## Missing / Unverified Data

- FY2027 Q1 actual results are not available as of the 2026-05-26 source check; official release is scheduled for 2026-06-03 after market close.
- FY2027 free cash flow guidance is not disclosed.
- Company-hosted full written Q4 FY2026 earnings call transcript / Q&A was not verified.
- Product-level revenue and profitability by module or platform category are not fully disclosed.
- Segment-level operating income and segment-level FCF are not disclosed.
- Customer-level economics, renewal pricing, and contract duration distribution are not disclosed.
- Ultimate July 19 Incident legal / remediation cost is not fully known.
- Current market price, market cap, and EV are provider-sourced, not company-filed facts.
- Investor-specific cost basis, position size, tax status, and required return were not provided.
