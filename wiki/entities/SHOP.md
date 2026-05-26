---
type: entity
ticker: SHOP
company: Shopify Inc.
market: Nasdaq / TSX
currency: USD
period_type: quarterly + annual
reporting_scope: Q1 2026 quarter ended 2026-03-31 plus FY2025 annual baseline
latest_period: Q1 2026
latest_period_end: 2026-03-31
latest_total_revenue_usd_m: 3170
latest_net_income_usd_m: -581
source_gap_count: 9
source_gaps:
  - Full FY2026 actual results are not disclosed.
  - FY2026 full-year revenue / FCF guidance is not disclosed.
  - Official company-hosted full call transcript / Q&A was not verified.
  - Segment-level operating income or FCF is not disclosed.
  - Product-level profitability for Payments, Shop Pay, Shop Campaigns, Capital, POS, and AI tools is not disclosed.
  - Merchant cohort retention, take rate by merchant size, and GMV by geography are partially disclosed / not disclosed.
  - Loan / merchant cash advance credit losses through a recessionary cycle are not disclosed.
  - Equity and other investment future fair-value impact is not predictable.
  - Investor-specific cost basis, position size, tax status, and required return were not provided.
source_notes:
  - raw/imports/SHOP_latest_results_source.md
normalized_markdown: raw/financials/SHOP_fundamentals.md
normalized_json: raw/financials/SHOP_fundamentals.json
tags:
  - entity/company
  - ticker/SHOP
---

# SHOP - Shopify Inc.

## Snapshot

| Item | Value |
|---|---|
| Ticker | SHOP |
| Company | Shopify Inc. |
| Market | Nasdaq / TSX |
| Currency | USD |
| Latest period | Q1 2026, quarter ended 2026-03-31 |
| Reporting scope | Q1 2026 quarter ended 2026-03-31 plus FY2025 annual baseline |
| Normalized file | `raw/financials/SHOP_fundamentals.md` |
| Latest price check | USD 103.00 regular close on 2026-05-22; market cap USD 133.66B |
| Current action read | WAIT / WATCHLIST; avoid new capital until valuation gives more margin of safety |

## Source Map

| Priority | Source | Status | Notes |
|---:|---|---|---|
| 1 | SEC / official filings | Available | Q1 2026 Form 10-Q and FY2025 Form 10-K reviewed. |
| 1 | Official company results | Available | Q1 2026 press release used for GMV, MRR, FCF reconciliation, and Q2 2026 outlook. |
| 2 | Earnings transcript / call material | Partial | Secondary transcript found, but company-hosted full transcript / Q&A was not verified; not used for durable numbers. |
| 3 | Financial statements / metrics | Available | Stooq and StockAnalysis used only for fresh market-data check. |
| 4 | News / web context | Limited | Not needed for core financial facts in this pass. |

## Business Model

Shopify เป็น commerce infrastructure platform สำหรับ merchants ที่ต้องการขายผ่าน online storefronts, physical retail, AI platforms, social media, marketplaces, and other channels. Core product คือ integrated back-end system สำหรับ storefront, inventory, payments, checkout, shipping, marketing, analytics, financing, and merchant operations.

Revenue แบ่งหลักเป็น `Subscription solutions` และ `Merchant solutions`. Subscription solutions เป็น platform access / software subscription layer ที่ gross margin สูงมาก ส่วน Merchant solutions โตไปกับ GMV ผ่าน payments, transaction services, Shop Pay, shipping, apps/themes economics, advertising, lending, and other merchant services. Quality ของ business อยู่ที่ scale, ecosystem, merchant tooling, checkout/payment penetration, and multi-channel commerce adoption.

## Segments / Revenue Mix

| Category | Q1 2026 Revenue | Q1 2026 Mix | Q1 2026 YoY | Q1 2026 Gross Margin | Source |
|---|---:|---:|---:|---:|---|
| Subscription solutions | USD 750M | 23.7% | 21.0% | 80.3% | Shopify Q1 2026 Form 10-Q / press release. |
| Merchant solutions | USD 2.420B | 76.3% | 39.1% | 39.0% | Shopify Q1 2026 Form 10-Q / press release. |
| Total | USD 3.170B | 100.0% | 34.3% | 48.8% | Shopify Q1 2026 Form 10-Q / press release. |

Merchant solutions คือ growth engine และ revenue majority แล้ว แต่ mix นี้ทำให้ consolidated gross margin ต่ำกว่า pure subscription software เพราะ payments / merchant services มี cost structure ต่างกัน.

## Financial Facts

| Metric | Latest value | Source |
|---|---:|---|
| Q1 2026 GMV | USD 100.743B | Shopify Q1 2026 press release. |
| Q1 2026 MRR | USD 212M | Shopify Q1 2026 press release. |
| Q1 2026 revenue | USD 3.170B | Shopify Q1 2026 Form 10-Q / press release. |
| Q1 2026 gross profit / margin | USD 1.546B / 48.8% | Shopify Q1 2026 Form 10-Q / calculation. |
| Q1 2026 operating income / margin | USD 382M / 12.1% | Shopify Q1 2026 Form 10-Q / calculation. |
| Q1 2026 net loss | USD (581)M | Shopify Q1 2026 Form 10-Q; affected by equity investment losses. |
| Q1 2026 net income excluding impact of equity investments | USD 360M | Shopify Q1 2026 press release; non-GAAP. |
| Q1 2026 FCF / FCF margin | USD 476M / 15.0% | Shopify Q1 2026 press release; non-GAAP. |
| FY2025 FCF | USD 2.007B | Calculation from FY2025 Form 10-K OCF minus capex. |
| TTM FCF | USD 2.120B | FY2025 FCF - Q1 2025 FCF + Q1 2026 FCF. |
| Cash, cash equivalents, and marketable securities | USD 5.743B | Shopify Q1 2026 Form 10-Q MD&A. |
| Operating lease liabilities | USD 179M | Shopify Q1 2026 Form 10-Q. |
| Net cash using cash/marketable securities less lease liabilities | USD 5.564B | 5.743 - 0.179. |
| Q2 2026 revenue outlook | High-twenties percentage YoY growth | Shopify Q1 2026 press release. |
| Q2 2026 FCF margin outlook | Mid-teens | Shopify Q1 2026 press release; non-GAAP. |

## Charts

See `raw/financials/SHOP_fundamentals.md` for source-backed quarterly YoY, quarterly trend, annual, revenue mix, cash-flow/capex, and balance-sheet chart blocks.

## Transcript / Management Commentary

Official full call transcript / Q&A was not verified. From official press release and 10-Q only, management framing is that Q1 growth was broad-based across geographies, merchant sizes, and channels, with GMV above USD 100B in the quarter. The 10-Q business overview also highlights Shopify's role across online storefronts, physical retail spaces, AI platforms, and social media.

Q2 outlook still implies strong growth but not a full-year guide: revenue growth high-twenties, gross profit dollars up mid-twenties, operating expenses at 35%-36% of revenue, SBC at USD 145M, and FCF margin in the mid-teens.

## Thesis

### Bull Case

SHOP เป็น high-quality commerce compounder ที่ยังโตเร็วใน scale ใหญ่มาก. Q1 revenue grew 34.3%, Merchant solutions grew 39.1%, GMV passed USD 100B in a single quarter, operating income nearly doubled YoY, and FCF margin stayed around 15%. Balance sheet มี net cash สูง และ no obvious interest-bearing debt burden after convertible notes matured.

Long-term bull case คือ Shopify keeps expanding take rate and merchant wallet share through payments, Shop Pay, POS, B2B/enterprise, international, apps/ecosystem, lending, advertising, and AI-enabled commerce workflows. If operating leverage continues while growth remains high-twenties or better, FCF can compound faster than revenue.

### Bear Case

Valuation is the main objection. At USD 103.00, market cap is about USD 133.66B, TTM FCF yield is only 1.59%, and market EV / TTM FCF is about 60.4x. Base DCF fair value is about USD 51.45 per share, and even a bull case with very strong FCF growth reaches about USD 85.33. That means the market is already underwriting a long runway of high FCF growth.

Merchant solutions mix also carries lower gross margin than subscriptions, transaction and loan losses grew 54.7% YoY in Q1, and loans / MCAs continue to expand. GAAP net income remains noisy because equity and other investments can swing results sharply.

### Key Debate

คำถามหลักไม่ใช่ "Shopify เป็น business ดีไหม" แต่คือ "ราคา ณ USD 103 จ่ายแพงเกินไปสำหรับ FCF durability ที่ source-backed แล้วหรือยัง". Business momentum ยังดีมาก แต่ margin of safety ยังบาง เพราะ current valuation ต้องการ growth + FCF conversion ที่ต่อเนื่องหลายปี.

## Risks

- Valuation risk: TTM FCF yield 1.59% and EV / TTM FCF about 60.4x.
- Merchant solutions mix risk: faster Merchant solutions growth can pressure consolidated gross margin mix.
- Credit / loss risk from Shopify Capital, loans, merchant cash advances, transaction losses, and payments exposure.
- GAAP earnings volatility from equity and other investments.
- Competition from Amazon, payments providers, enterprise commerce platforms, social commerce, and AI-native commerce interfaces.
- Macro / merchant health risk if consumer spending, SMB formation, or merchant GMV slows.
- Regulatory / payments / data privacy risk across jurisdictions.
- Source gap risk because product-level profitability, segment FCF, cohort retention, and full-year FY2026 guidance are not disclosed.

## Catalysts

- Q2 2026 results confirming high-twenties revenue growth and mid-teens FCF margin.
- Continued Merchant solutions growth without major gross margin deterioration.
- Evidence that transaction and loan losses stabilize as a percentage of revenue.
- More disclosure on AI tools, Shop Pay, Payments, Capital, enterprise, and international profitability.
- A price pullback that lifts FCF yield toward a more attractive entry.
- Full-year FY2026 guidance or management commentary that makes FCF runway more source-backed.

## Valuation Watch Items

- Current DCF memo: [[SHOP DCF Valuation 2026-05-26]].
- Base-case fair value from P11 is approximately USD 51.45 per diluted share versus USD 103.00 fresh price check.
- Bull case reaches about USD 85.33, still below current price.
- Watch whether TTM FCF can compound above 20% for several years while FCF margin stays in the mid-teens or better.
- Re-run valuation after Q2 2026 results and any updated FY2026 outlook.

## Reports / Source Notes

| Note | Type |
|---|---|
| [[SHOP_latest_results_source]] | Latest results source note |
| [[SHOP_fundamentals]] | Normalized financial facts |
| [[SHOP DCF Valuation 2026-05-26]] | DCF valuation |
| [[SHOP Decision Memo 2026-05-26]] | Decision memo |

## Follow-Up

- Refresh after Q2 2026 results with revenue, GMV, MRR, gross margin, operating income, OCF, capex, FCF, cash, marketable securities, operating lease liabilities, shares, and any FY2026 outlook.
- Track Merchant solutions gross margin, transaction and loan losses, and loan/MCA balances.
- Look for official company-hosted transcript or more complete Q&A before using call commentary as durable evidence.
- Recheck current price before any action change.
- If disclosure improves, split Merchant solutions by payments, Capital, Shop Pay, advertising, POS, B2B/enterprise, and AI tooling economics.

## Missing / Unverified Data

| Item | Status | Notes |
|---|---|---|
| Full FY2026 actual results | not disclosed | Q1 2026 is the latest official period found. |
| FY2026 full-year revenue / FCF guidance | not disclosed | Official outlook found only for Q2 2026. |
| Official company-hosted full call transcript / Q&A | not verified | Secondary transcripts exist, but durable financial facts use press release and filings. |
| Segment-level operating income or FCF | not disclosed | Revenue/cost of revenue is disclosed by solutions category only. |
| Product-level profitability for Payments, Shop Pay, Shop Campaigns, Capital, POS, and AI tools | not disclosed | Limits precision on Merchant solutions quality. |
| Merchant cohort retention, take rate by merchant size, and GMV by geography | partially disclosed / not disclosed | Needed to underwrite durability of growth. |
| Loan / merchant cash advance credit losses through a recessionary cycle | not disclosed | Important because loans and MCAs are growing. |
| Equity and other investment future fair-value impact | not predictable | GAAP net income can remain volatile. |
| Investor-specific cost basis, position size, tax status, and required return | not provided | Needed for personalized sizing. |
