---
type: analysis
analysis_type: decision-memo
ticker: SHOP
company: Shopify Inc.
date: 2026-05-26
currency: USD
decision: WAIT / WATCHLIST; avoid new capital until valuation gives more margin of safety
source_files:
  - index.md
  - wiki/entities/SHOP.md
  - raw/financials/SHOP_fundamentals.md
  - raw/imports/SHOP_latest_results_source.md
  - wiki/analysis/valuations/SHOP DCF Valuation 2026-05-26.md
tags:
  - analysis/decision-memo
  - ticker/SHOP
---

# SHOP Decision Memo - 2026-05-26
Entity: [[SHOP]]

## Action Read

**Action: WAIT / WATCHLIST. Avoid new capital until valuation gives more margin of safety.**

SHOP เป็น business คุณภาพสูงที่ยังโตแรง: Q1 2026 revenue +34.3% YoY, Merchant solutions +39.1%, GMV above USD 100B, operating income +88.2%, and FCF margin around 15%. Balance sheet also supports the thesis with USD 5.743B cash / marketable securities and only USD 0.179B operating lease liabilities treated as debt-like obligations in this memo.

แต่ที่ USD 103.00, market cap ประมาณ USD 133.66B, TTM FCF yield แค่ 1.59%, and market EV / TTM FCF about 60.4x. Base DCF fair value is about USD 51.45, and even bull case is about USD 85.33. สำหรับ new capital จึงควร WAIT. ถ้าถืออยู่แล้วและ cost basis ต่ำ อาจ HOLD ได้ แต่ต้องรู้ว่า return ต่อจากนี้พึ่งพา FCF compounding หลายปีและ multiple ที่ยัง premium มาก.

## Current Price / Market Data Check

| Metric | Value | Source / Calculation |
|---|---:|---|
| Fresh market price checked | USD 103.00 close on 2026-05-22 | Stooq SHOP.US quote CSV checked 2026-05-26. |
| Latest after-hours cross-check | USD 103.25 after-hours on 2026-05-22 | StockAnalysis quote page checked 2026-05-26; not used for base market cap. |
| Market cap | USD 133.66B | USD 103.00 * 1.297654610B shares outstanding. |
| Shares outstanding | 1.297654610B | Shopify Q1 2026 Form 10-Q cover page as of 2026-05-01. |
| Diluted shares used in DCF | 1.303357874B | Shopify Q1 2026 weighted-average diluted shares. |
| Cash, cash equivalents, and marketable securities | USD 5.743B | Shopify Q1 2026 Form 10-Q MD&A. |
| Operating lease liabilities | USD 0.179B | Shopify Q1 2026 Form 10-Q; debt-like obligation. |
| Net cash | USD 5.564B | 5.743 - 0.179. |
| TTM FCF | USD 2.120B | FY2025 FCF 2.007B - Q1 2025 FCF 0.363B + Q1 2026 FCF 0.476B. |
| TTM FCF yield | 1.59% | 2.120 / 133.658. |
| Market EV / TTM FCF | 60.42x | (133.658 + 0.179 - 5.743) / 2.120. |

## Evidence From Vault

| Evidence | Read | Source |
|---|---|---|
| Q1 2026 GMV was USD 100.743B | Platform scale remains exceptional. | `raw/imports/SHOP_latest_results_source.md` |
| Q1 2026 revenue was USD 3.170B, +34.3% YoY | Growth is still strong at scale. | `raw/financials/SHOP_fundamentals.md` |
| Merchant solutions revenue was USD 2.420B, +39.1% YoY | Monetization of merchant activity is the growth engine. | Shopify Q1 2026 Form 10-Q / press release. |
| Subscription solutions gross margin was 80.3% | Software layer remains high-quality. | `raw/financials/SHOP_fundamentals.md` |
| Merchant solutions gross margin was 39.0% | Mix shift is lower-margin than subscriptions. | `raw/financials/SHOP_fundamentals.md` |
| Transaction and loan losses rose 54.7% YoY | Credit / payments risk is worth tracking. | Shopify Q1 2026 Form 10-Q / press release. |
| Q1 2026 FCF was USD 476M | Cash generation is real and source-backed. | Shopify Q1 2026 press release. |
| FY2026 full-year FCF guidance was not found | DCF uses TTM FCF rather than invented guidance. | `raw/imports/SHOP_latest_results_source.md` |

## Valuation Read

| Scenario | Fair Value / Share | Upside / Downside vs USD 103.00 | Read |
|---|---:|---:|---|
| Bear | USD 30.16 | -70.7% | If growth normalizes or losses/credit pressure rise, downside is large. |
| Base | USD 51.45 | -50.0% | Strong business, but current price is too demanding for new capital. |
| Bull | USD 85.33 | -17.2% | Even strong FCF compounding does not create enough margin of safety at current price. |

Valuation read คือ SHOP เป็น excellent business ที่ยังไม่ใช่ excellent entry. To justify current price, FCF has to compound very fast for a long time and market multiple has to stay rich.

## Bull Case

- Shopify remains essential commerce infrastructure for merchants across online, physical retail, social, AI, and other channels.
- Q1 2026 GMV above USD 100B proves platform scale and merchant activity.
- Merchant solutions keeps compounding through payments, Shop Pay, Capital, shipping, POS, B2B, enterprise, advertising, and ecosystem services.
- Subscription solutions remains high gross margin and supports operating leverage.
- Net cash balance sheet gives flexibility for investment and repurchases.
- AI workflows could expand merchant productivity and increase the value of Shopify's commerce data and checkout layer.

## Bear Case

- Valuation is stretched: TTM FCF yield is only 1.59%.
- Merchant solutions mix can dilute consolidated gross margin despite high revenue growth.
- Transaction and loan losses are rising faster than revenue in Q1 2026.
- Loans and merchant cash advances add credit-cycle sensitivity.
- GAAP net income is noisy due to equity and other investment fair-value changes.
- Full-year FY2026 FCF guidance was not verified, so long-term DCF needs a wide uncertainty band.

## Key Assumptions

| Assumption | Working choice | Why it matters |
|---|---|---|
| FCF basis | OCF minus purchases of property and equipment | Matches Shopify's Q1 press release reconciliation and filing inputs. |
| Starting FCF for base DCF | TTM FCF of USD 2.120B | Full-year FY2026 FCF guidance was not verified. |
| Debt treatment | Operating lease liabilities as debt-like obligations | No convertible senior notes are shown on the Q1 2026 balance sheet line. |
| Required margin of safety | High for new capital at premium multiple | Current valuation already embeds high growth. |
| Investor profile | Long-term investor, normal-sized position | No position size, tax basis, or required return was provided. |

## What Would Change The Decision

- Upgrade toward ADD only if price falls enough to lift FCF yield materially or if official results prove a much higher FCF run-rate.
- Upgrade if Q2/Q3 2026 results show revenue growth stays high while FCF margin expands above mid-teens.
- Keep WAIT if price remains near USD 103 and FCF remains near the current TTM base.
- Downgrade toward TRIM for oversized positions if price rises while transaction / loan losses and Merchant solutions margin pressure worsen.
- Re-run DCF after Q2 2026 results, with special attention to GMV, Merchant solutions gross margin, losses, OCF, capex, and any full-year guide.

## Missing / Unverified Data

| Item | Status | Why it matters |
|---|---|---|
| Full FY2026 actual results | not disclosed | Need full-year growth and FCF confirmation. |
| FY2026 full-year revenue / FCF guidance | not disclosed | Prevents a management-guided DCF anchor. |
| Official company-hosted full call transcript / Q&A | not verified | Limits management-commentary depth. |
| Segment-level operating income or FCF | not disclosed | Cannot prove cash conversion by solution category. |
| Product-level profitability for Payments, Shop Pay, Shop Campaigns, Capital, POS, and AI tools | not disclosed | Key to underwriting Merchant solutions quality. |
| Merchant cohort retention, take rate by merchant size, and GMV by geography | partially disclosed / not disclosed | Needed to judge growth durability. |
| Loan / merchant cash advance credit losses through a recessionary cycle | not disclosed | Important credit-risk gap. |
| Equity and other investment future fair-value impact | not predictable | GAAP earnings can remain volatile. |
| Investor-specific cost basis, position size, tax status, and required return | not provided | Prevents personalized sizing. |

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| Entity page | `wiki/entities/SHOP.md` | Business model, thesis, risks, catalysts, source gaps. |
| Normalized financial facts | `raw/financials/SHOP_fundamentals.md` | Q1 2026 financial facts, FY2025 baseline, market data, cash, debt-like obligations, FCF, guidance. |
| Latest results source note | `raw/imports/SHOP_latest_results_source.md` | Source map and extracted facts. |
| DCF valuation memo | `wiki/analysis/valuations/SHOP DCF Valuation 2026-05-26.md` | Source-backed DCF scenarios and sensitivity. |
| Shopify Q1 2026 Form 10-Q | https://www.sec.gov/Archives/edgar/data/1594805/000159480526000019/shop-20260331.htm | Primary filing source. |
| Shopify Q1 2026 results press release | https://www.shopify.com/investors/press-releases/shopify-delivers-again-as-merchants-clear-100-billion-in-q1-gmv | Official results and guidance. |
| Shopify FY2025 Form 10-K | https://www.sec.gov/Archives/edgar/data/1594805/000159480526000007/shop-20251231.htm | FY2025 annual baseline. |
| Stooq SHOP.US quote CSV | https://stooq.com/q/l/?s=shop.us&f=sd2t2ohlcv&h&e=csv | Fresh market price. |
