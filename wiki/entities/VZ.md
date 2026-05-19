---
type: entity
ticker: VZ
company: Verizon Communications Inc.
market: NYSE / Nasdaq
currency: USD
period_type: quarterly + annual
reporting_scope: Q1 2026 quarter ended 2026-03-31 plus FY2025 annual baseline
latest_period: Q1 2026
latest_period_end: 2026-03-31
latest_total_revenue_usd_m: 34440
latest_net_income_usd_m: 5146
source_gap_count: 5
source_gaps:
  - Product-level profitability by wireless, FWA, fiber, IoT, security, and enterprise services is not disclosed.
  - Frontier standalone post-close financial contribution in Q1 2026 is not fully isolated.
  - Exact normalized recurring FCF after Frontier integration and debt paydown is unverified.
  - Investor-specific tax basis, dividend income need, and position size were not provided.
  - Intrayear market price after regular market open on 2026-05-19 was not verified.
source_notes:
  - raw/imports/VZ_latest_results_source.md
normalized_markdown: raw/financials/VZ_fundamentals.md
normalized_json: raw/financials/VZ_fundamentals.json
tags:
  - entity/company
  - ticker/VZ
---

# VZ - Verizon Communications Inc.

## Snapshot

| Item | Value |
|---|---|
| Ticker | VZ |
| Company | Verizon Communications Inc. |
| Market | NYSE / Nasdaq |
| Currency | USD |
| Latest verified period | Q1 2026, quarter ended 2026-03-31 |
| Latest quarterly operating revenue | USD 34,440 million |
| Latest quarterly net income | USD 5,146 million |
| FY2026 FCF guidance | USD 21.5B or more |
| Current price check | USD 46.88 close on 2026-05-18; checked 2026-05-19 Bangkok time |
| Market cap check | USD 195.74B from MarketBeat |
| Normalized file | [[VZ_fundamentals]] |
| Latest source note | [[VZ_latest_results_source]] |
| Latest valuation memo | [[VZ DCF Valuation 2026-05-19]] |
| Latest decision memo | [[VZ Decision Memo 2026-05-19]] |

Verizon เป็น telecom cash-flow story ที่ dividend yield สูงและ FCF guide ชัดขึ้น แต่ leverage หลัง Frontier ยังเป็นแกน risk หลัก. Q1 2026 ดีขึ้นในเชิง subscriber, churn, adjusted EPS และ FCF, แต่ DCF ที่ subtract total debt ยังต้องการราคาต่ำกว่านี้เพื่อให้ margin of safety ชัด.

## Source Map

| Priority | Source | Status | Notes |
|---:|---|---|---|
| 1 | SEC / official filings | Found | Q1 2026 Form 10-Q: https://www.sec.gov/Archives/edgar/data/732712/000073271226000023/vz-20260331.htm. FY2025 Form 10-K: https://www.verizon.com/about/sites/default/files/2025-Annual-Report-on-Form-10k.pdf. |
| 1 | Verizon Q1 2026 earnings release | Found | Official release with Q1 results and FY2026 guidance: https://www.verizon.com/about/news/feed/verizons-transformation-actions-deliver-growth-profitability-1q26-company-raises-adjusted-eps. |
| 2 | Earnings transcript / call materials | Found | Q1 2026 IR-hosted transcript and quarterly earnings page. |
| 3 | Financial statements / metrics | Found | Official SEC tables plus MarketBeat market-data check for current price. |
| 4 | News / web context | Not used for durable company facts | Official sources were sufficient for this workflow. |

## Business Model

Verizon provides communications, technology, information, and streaming products and services to consumers, businesses, and government entities. The core economic engine is recurring connectivity: mobility, broadband, fiber, FWA, enterprise networking, managed/security services, and related equipment/device activity.

The investment profile is not asset-light. Verizon needs heavy network capex, spectrum/license investment, and a large debt stack. The offset is recurring demand, high customer stickiness when churn improves, and management's ability to convert operating cash flow into dividends, debt reduction, buybacks, and network investment.

## Segments / Revenue Mix

| Segment / revenue category | Q1 2026 | Q1 2025 | Source |
|---|---:|---:|---|
| Consumer total operating revenues | USD 26,453M | USD 25,618M | SEC 10-Q. |
| Business total operating revenues | USD 7,419M | USD 7,286M | SEC 10-Q. |
| Consumer mobility and broadband service | USD 19,108M | USD 18,728M | SEC 10-Q. |
| Business mobility and broadband service | USD 3,681M | USD 3,710M | SEC 10-Q. |
| Consumer operating income | USD 7,714M | USD 7,424M | SEC 10-Q. |
| Business operating income | USD 884M | USD 664M | SEC 10-Q. |

## Financial Facts

| Fact | Value | Source |
|---|---:|---|
| Q1 2026 total operating revenues | USD 34,440M | `raw/financials/VZ_fundamentals.md`. |
| Q1 2026 revenue growth | 2.85% YoY | SEC 10-Q. |
| Q1 2026 operating income | USD 8,242M | SEC 10-Q. |
| Q1 2026 net income | USD 5,146M | SEC 10-Q. |
| Q1 2026 diluted EPS | USD 1.20 | SEC 10-Q. |
| Q1 2026 free cash flow | USD 3,783M | SEC 10-Q reconciliation. |
| Cash and cash equivalents | USD 8,366M | SEC 10-Q. |
| Total debt | USD 172,460M | SEC 10-Q balance sheet calculation. |
| Net debt | USD 164,094M | Calculated from SEC 10-Q. |
| FY2025 free cash flow | USD 20,126M | FY2025 Form 10-K reconciliation. |
| FY2026 free cash flow guidance | USD 21.5B or more | Verizon Q1 2026 earnings release. |
| FY2026 adjusted EPS guidance | USD 4.95 to USD 4.99 | Verizon Q1 2026 earnings release. |

## Charts

Charts are maintained in `raw/financials/VZ_fundamentals.md` and use only verified values from official filings, official IR materials, or shown calculations.

## Transcript / Management Commentary

- Management framed Q1 2026 as evidence that the turnaround is gaining momentum.
- Verizon reported positive Q1 postpaid phone net additions for the first time since 2013.
- Management said Q1 Mobility and Broadband service revenue was pressured by 80 bps from the January network outage and should be the low point of 2026.
- The company emphasized a shift toward durable recurring service revenue and away from low-margin promotional activity.
- Consumer postpaid phone churn improved during the quarter, and March was below 85 bps per management commentary.
- Frontier integration is on track, with a target of more than USD 1B run-rate operating cost synergies by 2028.
- Management raised adjusted EPS guidance and postpaid phone net-add expectations while reaffirming FCF guidance of USD 21.5B or more.

## Thesis

### Bull Case

Verizon มี setup แบบ income + deleveraging: FCF guidance มากกว่า USD 21.5B, dividend payout จาก FCF ยังดูครอบคลุม, subscriber trends ดีขึ้น, churn ดีขึ้น, Frontier เพิ่ม fiber footprint, และ management เริ่มเปลี่ยนจาก promotion-heavy growth ไปสู่ customer economics ที่สุขภาพดีกว่า. ถ้า FCF guide ทำได้จริงและ debt ถูกลดลงตามแผน equity value จะได้ประโยชน์จากทั้ง cash yield และ leverage rerating.

### Bear Case

Balance sheet ยังหนักมาก. Q1 2026 total debt อยู่ราว USD 172.5B และ net debt จาก total debt minus cash อยู่ราว USD 164.1B. การทำ DCF แบบ enterprise value แล้ว subtract debt ให้ base fair value ต่ำกว่า market price ชัดเจน. Telecom growth ต่ำ, capex recurring, competition สูง, spectrum/network investment ต้องต่อเนื่อง และ Frontier integration ยังต้องพิสูจน์ synergy/debt paydown.

### Key Debate

คำถามหลักคือ VZ เป็น dividend/deleveraging value ที่พอชดเชย leverage risk หรือไม่. Official sources บอกว่า FCF guide และ operating momentum ดีขึ้น แต่ราคาปัจจุบันยังไม่ได้ให้ margin of safety มากพอถ้าใช้ total debt เข้มงวดใน DCF.

## Risks

- High leverage and refinancing/interest-rate sensitivity.
- Frontier integration execution and synergy timing.
- Competitive intensity in wireless, fiber, broadband, cable MVNO, and fixed wireless.
- Capex and spectrum needs could crowd out faster debt reduction.
- Network outage/customer-experience risk can pressure churn and service revenue.
- Regulatory obligations, cybersecurity, privacy, network reliability, and consumer protection scrutiny.
- Dividend investor base may react strongly if FCF conversion or leverage path weakens.

## Catalysts

- FY2026 FCF of USD 21.5B or more is delivered or exceeded.
- Debt paydown and net unsecured debt/adjusted EBITDA ratio improve toward target.
- Frontier integration creates measurable cost synergies and fiber growth.
- Sustained postpaid phone net additions without heavy promotional spend.
- Churn remains lower and customer acquisition/retention costs stay down.
- Buyback activity remains disciplined after dividend and deleveraging needs.

## Valuation Watch Items

- Latest DCF memo: [[VZ DCF Valuation 2026-05-19]].
- Base-case fair value from the memo is approximately USD 34.96 per diluted share versus the fresh close-price check of USD 46.88.
- Bull case around USD 47.29 requires lower WACC / lower risk view and still offers little margin of safety.
- Watch total debt, cash balance, FCF conversion, Frontier debt paydown, and net unsecured debt / adjusted EBITDA.

## Reports / Source Notes

- [[VZ_latest_results_source]]
- [[VZ_fundamentals]]
- [[VZ DCF Valuation 2026-05-19]]
- [[VZ Decision Memo 2026-05-19]]

## Follow-Up

- Refresh after Q2 2026 results with focus on FCF, total debt, Frontier integration, churn, postpaid phone adds, broadband net adds, capex, and guidance.
- Track whether Verizon repays substantially all Frontier debt by year-end as stated.
- Revisit valuation if price falls closer to DCF base case or debt paydown improves equity value materially.
- Watch dividend coverage against actual FCF, not only guidance.

## Missing / Unverified Data

| Item | Status | Why it matters |
|---|---|---|
| Product-level profitability by wireless, FWA, fiber, IoT, security, and enterprise services | not disclosed | Limits ability to value growth engines separately. |
| Frontier standalone post-close financial contribution in Q1 2026 | not fully isolated | Limits clean pro forma trend analysis. |
| Exact normalized recurring FCF after Frontier integration and debt paydown | ไม่พบข้อมูลที่ยืนยันได้ | FY2026 FCF guide is useful, but post-integration run-rate remains uncertain. |
| Investor-specific tax basis, dividend income need, and position size | not provided | Affects hold/add/trim decision for a real portfolio. |
| Intrayear market price after regular market open on 2026-05-19 | ไม่พบข้อมูลที่ยืนยันได้ | Fresh check used 2026-05-18 close plus 2026-05-19 extended-hours quote. |
