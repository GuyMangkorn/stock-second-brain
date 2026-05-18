---
type: entity
ticker: JNJ
company: Johnson & Johnson
market: NYSE
currency: USD
period_type: quarterly + annual
reporting_scope: Q1 2026 fiscal first quarter ended 2026-03-29 plus FY2025 annual baseline
latest_period: Q1 2026
latest_period_end: 2026-03-29
latest_total_revenue_usd_m: 24062
latest_net_income_usd_m: 5235
source_gap_count: 5
source_gaps:
  - Product-level revenue for ICOTYDE and IMAAVY is not disclosed.
  - Product-level profitability by brand is not disclosed.
  - GAAP forward guidance is not provided.
  - FY2026 full-year actual results are not yet available.
  - Sequential quarterly trend across recent quarters has not been normalized in this source note.
source_notes:
  - raw/imports/JNJ_latest_results_source.md
normalized_markdown: raw/financials/JNJ_fundamentals.md
normalized_json: raw/financials/JNJ_fundamentals.json
tags:
  - entity/company
  - ticker/JNJ
---

# JNJ - Johnson & Johnson

## Snapshot

| Item | Value |
|---|---|
| Ticker | JNJ |
| Company | Johnson & Johnson |
| Market | NYSE |
| Currency | USD |
| Latest verified period | Q1 2026, fiscal first quarter ended 2026-03-29 |
| Latest quarterly sales | USD 24,062 million |
| Latest quarterly net earnings | USD 5,235 million |
| FY2025 free cash flow | USD 19,698 million |
| FY2026 FCF outlook | approximately USD 21 billion |
| Current price check | USD 227.54 on 2026-05-18, checked 2026-05-19 Bangkok time |
| Market cap check | USD 547.7 billion, calculated from current price and SEC common shares outstanding |
| Normalized file | [[JNJ_fundamentals]] |
| Latest source note | [[JNJ_latest_results_source]] |
| Latest valuation memo | [[JNJ DCF Valuation 2026-05-19]] |
| Latest decision memo | [[JNJ Decision Memo 2026-05-19]] |

Johnson & Johnson is a diversified health care company now centered on Innovative Medicine and MedTech after the Kenvue separation. The core investment debate is whether strong pharma/medtech innovation and a durable dividend profile can offset STELARA erosion, legal/talc overhang, MedTech margin pressure, debt from M&A, and a valuation that already prices in a lot of stability.

## Source Map

| Priority | Source | Status | Notes |
|---:|---|---|---|
| 1 | SEC / official filings | Found | Q1 2026 Form 10-Q: https://www.sec.gov/Archives/edgar/data/200406/000020040626000087/jnj-20260329.htm. FY2025 Annual Report: https://www.jnj.com/download/johnson-johnson-2025-annual-report. |
| 2 | Earnings transcript / call materials | Found | Q1 2026 IR-hosted transcript and earnings presentation from J&J investor relations / Q4 CDN. |
| 3 | Financial statements / metrics | Found | Official SEC tables, J&J press release, J&J presentation, and FinanceCharts market-data check for current price. |
| 4 | News / web context | Not used for durable company facts | Official sources were sufficient for this workflow. |

## Business Model

JNJ operates through two reportable segments:

| Segment | Revenue mechanism | Durable drivers | Current pressure points |
|---|---|---|---|
| Innovative Medicine | Prescription medicines across oncology, immunology, neuroscience, pulmonary hypertension, infectious disease, cardiovascular/metabolism and related focus areas | Pipeline launches, specialty drug scale, oncology/immunology franchises, global commercial reach | STELARA erosion, product-cycle concentration, patent/regulatory risk, launch investment. |
| MedTech | Medical devices and technologies across cardiovascular, surgery, orthopaedics, vision and related platforms | Procedure volume, installed physician relationships, cardiovascular/electrophysiology growth, Abiomed/Shockwave platforms | Tariffs, orthopaedics separation costs, China VBP, procedure cyclicality, integration execution. |

Management frames long-term growth around six focus areas: Oncology, Immunology, Neuroscience, Cardiovascular, Surgery, and Vision. The business model remains cash-generative but more innovation-cycle and litigation-sensitive than a pure defensive consumer-health model.

## Segments / Revenue Mix

### Q1 2026 Segment Mix

| Segment | Q1 2026 sales | Share of Q1 2026 sales | Q1 2026 segment income before tax | Source |
|---|---:|---:|---:|---|
| Innovative Medicine | 15,426 | 64.11% | 5,317 | SEC Form 10-Q. |
| MedTech | 8,636 | 35.89% | 1,239 | SEC Form 10-Q. |
| Total | 24,062 | 100.00% | 6,556 | SEC Form 10-Q. |

### Geographic Mix

| Geography | Q1 2026 sales | Share of Q1 2026 sales | Source |
|---|---:|---:|---|
| United States | 13,330 | 55.40% | SEC Form 10-Q. |
| Europe | 5,848 | 24.30% | SEC Form 10-Q. |
| Western Hemisphere, excluding U.S. | 1,293 | 5.37% | SEC Form 10-Q. |
| Asia-Pacific, Africa | 3,591 | 14.92% | SEC Form 10-Q. |

## Financial Facts

| Fact | Value | Source |
|---|---:|---|
| Q1 2026 sales | USD 24,062M | `raw/financials/JNJ_fundamentals.md`. |
| Q1 2026 reported sales growth | 9.9% YoY | SEC Form 10-Q / press release. |
| Q1 2026 operational sales growth | 6.4% | J&J press release; non-GAAP. |
| Q1 2026 net earnings | USD 5,235M | SEC Form 10-Q. |
| Q1 2026 diluted EPS | USD 2.14 | SEC Form 10-Q. |
| Q1 2026 adjusted diluted EPS | USD 2.70 | J&J press release; non-GAAP. |
| Q1 2026 operating cash flow | USD 2,514M | SEC Form 10-Q. |
| Q1 2026 capex spend | USD 1,049M | SEC Form 10-Q. |
| Q1 2026 free cash flow | USD 1,465M | Calculated: OCF - capex spend. |
| Cash + marketable securities | USD 22,051M | SEC Form 10-Q. |
| Total debt | USD 54,987M | Calculated from SEC Form 10-Q. |
| Net debt | USD 32,936M | Calculated from SEC Form 10-Q. |
| FY2025 free cash flow | USD 19,698M | FY2025 Annual Report reconciliation. |
| FY2026 FCF outlook | approximately USD 21B | Q1 2026 earnings call transcript. |

## Charts

Charts are maintained in `raw/financials/JNJ_fundamentals.md` and use only verified values from official filings, official IR materials, or shown calculations.

## Transcript / Management Commentary

- CEO Joaquin Duato described Q1 2026 as a strong start to a year of accelerated growth and impact.
- Management cited six focus areas: Oncology, Immunology, Neuroscience, Cardiovascular, Surgery, and Vision.
- Operational sales growth was 6.4% in Q1 2026. Management said STELARA was an approximate 540 bps headwind and that the company grew double digits excluding STELARA.
- Innovative Medicine operational growth was 7.4%, driven by DARZALEX, CARVYKTI, ERLEADA, RYBREVANT/LAZCLUZE, TREMFYA, and SPRAVATO, offset partly by STELARA and IMBRUVICA.
- MedTech operational growth was 4.6%, driven by electrophysiology, Abiomed, Shockwave, and trauma.
- CFO Joseph Wolk stated Q1 cash and marketable securities were about USD 22B, debt about USD 55B, net debt about USD 33B, Q1 FCF about USD 1.5B, and full-year FCF outlook about USD 21B.
- The board authorized a 3.1% dividend increase to an annual rate of USD 5.36 per share, which management described as the 64th consecutive year of dividend growth.

## Thesis

### Bull Case

JNJ still has rare scale in global health care, a broad Innovative Medicine and MedTech portfolio, durable cash generation, and a dividend-growth record that signals balance-sheet and cash-flow resilience. Q1 2026 sales growth was solid despite STELARA pressure, and management raised FY2026 sales/EPS guidance while maintaining a full-year FCF outlook of approximately USD 21B.

### Bear Case

The stock price already discounts stability. At USD 227.54, the market cap is about USD 547.7B, while FY2026 FCF outlook is about USD 21B, implying a low FCF yield. STELARA erosion, MedTech tariffs, launch investment, orthopaedics separation, litigation/talc matters, higher debt, and product-cycle risk all matter more when the valuation leaves limited margin of safety.

### Key Debate

The key debate is not whether JNJ is high quality; official sources support the quality. The question is whether current price fairly compensates for low-to-mid single digit FCF growth, patent/launch risk, MedTech margin pressure, and legal overhang. The P11 DCF says no margin of safety at the current price.

## Risks

- STELARA headwind and broader patent/lifecycle risk in Innovative Medicine.
- Brand-level product concentration and launch execution risk.
- MedTech tariff pressure and orthopaedics separation execution risk.
- Talc and other litigation matters.
- Higher net debt after M&A and capital allocation.
- Regulatory, reimbursement, pricing, and China VBP pressure.
- FX translation and global supply chain exposure.

## Catalysts

- Continued raised guidance or evidence that FY2026 FCF exceeds the approximately USD 21B outlook.
- Strong launch traction for ICOTYDE, INLEXZO, CAPLYTA, VARIPULSE, TECNIS PureSee, and other pipeline/platform assets.
- MedTech margin recovery after tariff and separation-cost pressure.
- Clearer orthopaedics separation path and economics.
- Material debt reduction or value-accretive capital allocation.
- Legal/talc risk de-escalation.

## Valuation Watch Items

- Latest DCF memo: [[JNJ DCF Valuation 2026-05-19]].
- Base-case fair value from the memo is approximately USD 150 per diluted share versus the fresh price check of USD 227.54.
- The sensitivity matrix still sits below current price across the main WACC / terminal growth range used in the vault.
- Watch FY2026 FCF conversion, net debt reduction, and whether guidance upgrades are supported by cash flow rather than only adjusted EPS.

## Reports / Source Notes

- [[JNJ_latest_results_source]]
- [[JNJ_fundamentals]]
- [[JNJ DCF Valuation 2026-05-19]]
- [[JNJ Decision Memo 2026-05-19]]

## Follow-Up

- Refresh after Q2 2026 results with focus on FCF, cash/debt, STELARA headwind, MedTech tariff impact, and FY2026 guidance.
- Add a multi-quarter trend ingest if decision quality requires Q2-Q4 2025 sequential comparisons.
- Track product-level disclosure for ICOTYDE, IMAAVY, INLEXZO, CAPLYTA, and MedTech cardiovascular platforms.
- Revisit valuation if price falls materially or FY2026 FCF outlook increases materially.

## Missing / Unverified Data

| Item | Status | Why it matters |
|---|---|---|
| Product-level revenue for ICOTYDE and IMAAVY | not disclosed | Limits launch-level underwriting. |
| Product-level profitability by brand | not disclosed | Segment-level income does not reveal brand-level economics. |
| GAAP forward guidance | not provided | Limits direct GAAP valuation bridge. |
| FY2026 full-year actual results | ไม่พบข้อมูลที่ยืนยันได้ | Q1 actuals and FY2026 guidance are the freshest facts. |
| Sequential quarterly trend across recent quarters | ไม่พบข้อมูลที่ยืนยันได้ | This P1/P4 ingest did not normalize every recent quarter. |
