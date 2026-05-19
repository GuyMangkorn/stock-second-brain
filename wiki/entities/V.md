---
type: entity
ticker: V
company: Visa Inc.
market: NYSE
currency: USD
period_type: quarterly + annual
reporting_scope: Fiscal Q2 2026 quarter and six months ended 2026-03-31 plus FY2025 annual baseline
latest_period: Q2 FY2026
latest_period_end: 2026-03-31
latest_total_revenue_usd_m: 11230
latest_net_income_usd_m: 6021
source_gap_count: 5
source_gaps:
  - Segment profit by growth engine is not disclosed.
  - Product-level economics for agentic commerce, stablecoin settlement, and Visa Direct are not disclosed.
  - Forward free cash flow guidance is not disclosed.
  - Post-exchange-offer fully diluted share count is not directly disclosed in checked sources.
  - FY2026 full-year actual results are not yet available.
source_notes:
  - raw/imports/V_latest_results_source.md
normalized_markdown: raw/financials/V_fundamentals.md
normalized_json: raw/financials/V_fundamentals.json
tags:
  - entity/company
  - ticker/V
---

# V - Visa Inc.

## Snapshot

| Item | Value |
|---|---|
| Ticker | V |
| Company | Visa Inc. |
| Market | NYSE |
| Currency | USD |
| Latest verified period | Q2 FY2026, quarter ended 2026-03-31 |
| Latest quarterly net revenue | USD 11,230 million |
| Latest quarterly net income | USD 6,021 million |
| FY2025 free cash flow | USD 21,577 million |
| Current price check | USD 332.64 close on 2026-05-18, checked 2026-05-19 Bangkok time |
| Market cap check | USD 624.481 billion from FinanceCharts |
| Normalized file | [[V_fundamentals]] |
| Latest source note | [[V_latest_results_source]] |
| Latest valuation memo | [[V DCF Valuation 2026-05-19]] |
| Latest decision memo | [[V Decision Memo 2026-05-19]] |

Visa เป็น global payment network และ payment technology platform ที่มี economics ดีมาก: asset-light, margin สูง, FCF conversion แข็งแรง และ network effects ชัดเจน. ประเด็นลงทุนหลักไม่ใช่คุณภาพธุรกิจ แต่คือ current valuation เทียบกับ growth runway, regulatory/litigation risk, และความไม่ชัดของ post-exchange-offer diluted share count.

## Source Map

| Priority | Source | Status | Notes |
|---:|---|---|---|
| 1 | SEC / official filings | Found | Q2 FY2026 Form 10-Q: https://www.sec.gov/Archives/edgar/data/1403161/000140316126000079/v-20260331.htm. FY2025 Form 10-K: https://www.sec.gov/Archives/edgar/data/1403161/000140316125000089/v-20250930.htm. |
| 1 | SEC 8-K exchange offer filings | Found | May 2026 Class B exchange offer results and settlement: https://www.sec.gov/Archives/edgar/data/1403161/000119312526215875/d59695d8k.htm and https://www.sec.gov/Archives/edgar/data/1403161/000119312526219432/d64238d8k.htm. |
| 2 | Earnings transcript / call materials | Found | Q2 FY2026 IR-hosted transcript, presentation, and operational performance data from Visa IR / Q4 CDN. |
| 3 | Financial statements / metrics | Found | Official SEC tables, Visa earnings release, and FinanceCharts market-data check for current price. |
| 4 | News / web context | Not used for durable company facts | Official sources were sufficient for this workflow. |

## Business Model

Visa operates a global payments technology network. The company facilitates transactions among consumers, sellers, financial institutions, fintechs, businesses, and governments, but it does not issue cards, extend credit, or set account-holder rates. This matters because Visa earns toll-like revenue from authorization, clearing, settlement, data processing, cross-border activity, and value-added services without taking traditional lending credit risk.

Key business engines:

| Engine | Revenue mechanism | Durable drivers | Current pressure points |
|---|---|---|---|
| Consumer payments | Card and credential usage across face-to-face and digital commerce | Global acceptance, credentials, digital payment penetration, e-commerce, affluent card mix | Regulation of fees, macro consumer spending, alternative payment rails. |
| Commercial and money movement solutions | B2B, commercial cards, Visa Direct, cross-border payouts and money movement | New endpoints, commercial cross-border, fintech/platform integrations | Competition, pricing scrutiny, adoption pace outside cards. |
| Value-added services | Risk, fraud, advisory, marketing, authorization, tokenization, issuer/acquirer services | Transaction-linked distribution, data scale, AI-enabled services, client demand | Disclosure is limited; product-level margins are not disclosed. |

## Segments / Revenue Mix

Visa reports one operating segment. Revenue category data and growth-engine commentary are still useful, but they are not full segment disclosures.

| Revenue category / engine | Q2 FY2026 fact | Source |
|---|---:|---|
| Service revenue | USD 4,981M, up 13% YoY | Q2 earnings release. |
| Data processing revenue | USD 5,543M, up 18% YoY | Q2 earnings release. |
| International transaction revenue | USD 3,631M, up 10% YoY | Q2 earnings release. |
| Other revenue | USD 1,320M, up 41% YoY | Q2 earnings release. |
| Client incentives | USD (4,245)M, up 14% YoY | Q2 earnings release. |
| Value-added services revenue | USD 3.3B, up 27% constant dollar | Q2 transcript. |
| Commercial and money movement solutions revenue | up 24% constant dollar | Q2 transcript. |

## Financial Facts

| Fact | Value | Source |
|---|---:|---|
| Q2 FY2026 net revenue | USD 11,230M | `raw/financials/V_fundamentals.md`. |
| Q2 FY2026 net revenue growth | 17.05% YoY | SEC 10-Q / earnings release. |
| Q2 FY2026 operating income | USD 7,234M | SEC 10-Q. |
| Q2 FY2026 net income | USD 6,021M | SEC 10-Q / earnings release. |
| Q2 FY2026 diluted EPS | USD 3.14 | SEC 10-Q. |
| Q2 FY2026 non-GAAP EPS | USD 3.31 | Earnings release; non-GAAP. |
| 6M FY2026 operating cash flow | USD 9,788M | SEC 10-Q. |
| 6M FY2026 capex spend | USD 761M | SEC 10-Q. |
| 6M FY2026 free cash flow | USD 9,027M | Calculated: OCF - capex spend. |
| Cash + investment securities | USD 14,221M | SEC 10-Q. |
| Total debt | USD 23,976M | SEC 10-Q debt note. |
| Net debt | USD 9,755M | Calculated from SEC 10-Q. |
| FY2025 free cash flow | USD 21,577M | FY2025 Form 10-K calculation. |
| FY2026 adjusted net revenue guidance | low-double-digit to low-teens growth | Q2 FY2026 transcript. |
| FY2026 adjusted EPS guidance | low-teens growth | Q2 FY2026 transcript. |

## Charts

Charts are maintained in `raw/financials/V_fundamentals.md` and use only verified values from official filings, official IR materials, or shown calculations.

## Transcript / Management Commentary

- Management said Q2 FY2026 net revenue grew 17% and non-GAAP EPS grew 20%, with the strongest net revenue growth since 2022.
- Visa Direct had 3.7B transactions, up 23% YoY.
- Value-added services revenue grew 27% constant dollar to USD 3.3B, and management said VAS represents about 30% of net revenue.
- Commercial and money movement solutions revenue grew 24% constant dollar.
- Management highlighted agentic commerce, stablecoins, blockchain settlement, and Visa as a Service as long-run growth areas.
- CFO Christopher Suh said Q2 outperformance came from higher-than-expected volatility, stronger value-added services revenue, and lower-than-expected incentives.
- Management raised full-year adjusted net revenue and EPS guide, now expecting adjusted net revenue growth in the low-double-digit to low-teens range and adjusted EPS growth in the low-teens.
- Middle East conflict is a near-term uncertainty for CEMEA cross-border travel; CEMEA is about 6% of total payments volume per management commentary.

## Thesis

### Bull Case

Visa เป็นหนึ่งใน quality compounders ที่ strongest ใน market: net revenue โตเร็ว, operating margin มากกว่า 60%, FCF margin สูง, share repurchase capacity ใหญ่ และ growth engines ใหม่อย่าง VAS, Visa Direct, commercial payments, agentic commerce และ stablecoin settlement เพิ่ม runway. ถ้า low-double-digit revenue growth และ low-teens EPS growth ถูก sustain ได้หลายปี หุ้นอาจ deserve premium multiple ต่อไป.

### Bear Case

Valuation ยังเข้ม. ที่ USD 332.64 และ market cap USD 624.481B, FY2025 FCF yield อยู่ประมาณ 3.45%. DCF base case ที่ใช้ FY2025 FCF เป็น anchor และ growth assumptions ที่ค่อนข้างดี ยังให้ fair value ต่ำกว่า current price. Regulatory scrutiny, interchange litigation, client incentives, cross-border volatility, alternative payment rails และ share-structure complexity ทำให้ margin of safety ต้องชัดกว่านี้ก่อน add new capital.

### Key Debate

คำถามไม่ใช่ Visa ดีไหม. Official sources ชี้ว่าธุรกิจยังดีมาก. คำถามคือราคาปัจจุบันให้ผลตอบแทน risk-adjusted พอหรือไม่ ถ้าต้อง underwrite growth หลายปี และยอมรับ regulatory/litigation/share-count uncertainty.

## Risks

- Global regulation of payments, interchange, network fees, privacy, cybersecurity, and AI.
- U.S. covered litigation and unresolved interchange reimbursement fee claims.
- Dependence on financial institutions, acquirers, processors, sellers, fintechs, and platforms.
- Competition from Mastercard, domestic networks, real-time payment rails, wallets, fintechs, and alternative payment methods.
- Cross-border travel volatility and regional macro shocks.
- Client incentives and pricing dynamics could pressure net revenue conversion.
- Share-structure complexity after Class B exchange offer may make market cap/share-count comparisons less clean.

## Catalysts

- Sustained low-double-digit to low-teens revenue growth through FY2026 and beyond.
- VAS growth remains above core network growth with attractive profitability.
- Visa Direct and commercial/money movement keep compounding at above-company growth rates.
- FIFA and marketing services revenue convert into durable client engagement.
- Agentic commerce and stablecoin settlement become measurable revenue pools without margin dilution.
- Buyback capacity continues to reduce diluted shares at attractive prices.

## Valuation Watch Items

- Latest DCF memo: [[V DCF Valuation 2026-05-19]].
- Base-case fair value from the memo is approximately USD 233 per diluted share versus the fresh price check of USD 332.64.
- Bull case reaches approximately USD 337 per diluted share, close to current price, but requires stronger growth and lower WACC.
- Watch FY2026 FCF conversion, post-exchange-offer diluted share disclosure, VAS/CMS growth durability, and regulatory/litigation updates.

## Reports / Source Notes

- [[V_latest_results_source]]
- [[V_fundamentals]]
- [[V DCF Valuation 2026-05-19]]
- [[V Decision Memo 2026-05-19]]

## Follow-Up

- Refresh after Q3 FY2026 results with attention to FCF, diluted shares after exchange-offer settlement, incentives, cross-border travel, VAS, Visa Direct, and guidance changes.
- Add a share-structure note if Visa discloses a cleaner post-exchange fully diluted share count.
- Track U.S. covered litigation updates and fee/regulatory developments.
- Revisit valuation if price falls materially or if FCF conversion clearly accelerates above FY2025 levels.

## Missing / Unverified Data

| Item | Status | Why it matters |
|---|---|---|
| Segment profit by growth engine | not disclosed | Limits ability to value VAS/CMS separately. |
| Product-level economics for agentic commerce, stablecoin settlement, and Visa Direct | not disclosed | Limits underwriting of new growth engines. |
| Forward free cash flow guidance | not disclosed | DCF years 1-5 must use scenario assumptions, not company FCF guidance. |
| Post-exchange-offer fully diluted share count | ไม่พบข้อมูลที่ยืนยันได้ | Share-count complexity affects precise market cap and per-share valuation. |
| FY2026 full-year actual results | ไม่พบข้อมูลที่ยืนยันได้ | Q2/6M actuals and FY2026 guidance are the freshest facts. |
