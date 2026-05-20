---
type: entity
ticker: CSCO
company: Cisco Systems, Inc.
market: Nasdaq
currency: USD
period_type: quarterly + annual
reporting_scope: Q3 FY2026 and nine months ended 2026-04-25 plus FY2025 annual baseline
latest_period: Q3 FY2026
latest_period_end: 2026-04-25
latest_total_revenue_usd_m: 15841
latest_net_income_usd_m: 3373
source_gap_count: 8
source_gaps:
  - Q3 FY2026 Form 10-Q not found during source discovery.
  - Official full prepared remarks / Q&A transcript not normalized.
  - FY2026 full-year actual results not disclosed.
  - FY2026 FCF guidance not verified.
  - Product-category operating profit not disclosed.
  - Hyperscaler AI customer concentration not disclosed.
  - Market quote after 2026-05-18 close not verified.
  - Investor-specific position size, tax basis, and required return not provided.
source_notes:
  - raw/imports/CSCO_latest_results_source.md
normalized_markdown: raw/financials/CSCO_fundamentals.md
normalized_json: raw/financials/CSCO_fundamentals.json
tags:
  - entity/company
  - ticker/CSCO
---

# CSCO - Cisco Systems, Inc.

## Snapshot

| Item | Value |
|---|---|
| Ticker | CSCO |
| Company | Cisco Systems, Inc. |
| Market | Nasdaq |
| Currency | USD |
| Latest period | Q3 FY2026, quarter ended 2026-04-25 |
| Reporting scope | Q3 FY2026 and nine months ended 2026-04-25 plus FY2025 annual baseline |
| Normalized file | `raw/financials/CSCO_fundamentals.md` |
| Latest price check | USD 118.88 close on 2026-05-18; checked 2026-05-20 |
| Current action read | AVOID / WAIT for new capital; REVIEW or TRIM only if already overweight |

## Source Map

| Priority | Source | Status | Notes |
|---:|---|---|---|
| 1 | SEC / official filings | Available | Q3 FY2026 Form 8-K and FY2025 Form 10-K reviewed. Q3 FY2026 10-Q was not found. |
| 1 | Official company results | Available | Q3 FY2026 earnings release reviewed and used for financial tables. |
| 2 | Earnings transcript / call material | Partially available | Official event page found; official full transcript text was not normalized. |
| 3 | Financial statements / metrics | Available | Yahoo Finance and FinanceCharts used only for fresh market data, lower priority than official filings/results. |
| 4 | News / web context | Limited | Not required for core financial facts; secondary transcript context used only as lower-priority commentary. |

## Business Model

Cisco เป็น enterprise networking, security, collaboration, and observability platform company. Core business ยังผูกกับ switching, routing, wireless, data center, and servers ใน Networking ขณะที่ Security, Observability และ subscription/service revenue ช่วยเพิ่ม recurring profile หลัง Splunk integration.

FY2025 Form 10-K ระบุ product categories หลักคือ Networking, Security, Collaboration และ Observability พร้อม services/support offerings. Subscription revenue ใน FY2025 อยู่ที่ USD 31.526B จาก total revenue USD 56.654B, ทำให้ Cisco ไม่ใช่ pure hardware cycle เท่านั้น แต่ยังมี upfront hardware/software revenue และ ratable subscription/service revenue ผสมกัน.

## Segments / Revenue Mix

| Segment / category | Q3 FY2026 Revenue | Q3 FY2026 Mix | Q3 FY2026 YoY | 9M FY2026 Revenue | 9M FY2026 YoY | Source |
|---|---:|---:|---:|---:|---:|---|
| Americas | USD 9.569B | 60.4% | 14% | USD 27.403B | 10% | Cisco Q3 FY2026 release. |
| EMEA | USD 4.054B | 25.6% | 9% | USD 12.262B | 10% | Cisco Q3 FY2026 release. |
| APJC | USD 2.218B | 14.0% | 9% | USD 6.409B | 7% | Cisco Q3 FY2026 release. |
| Networking | USD 8.815B | 55.6% | 25% | USD 24.877B | 20% | Cisco Q3 FY2026 release. |
| Security | USD 2.008B | 12.7% | 0% | USD 6.006B | -2% | Cisco Q3 FY2026 release. |
| Collaboration | USD 1.024B | 6.5% | -1% | USD 3.133B | 1% | Cisco Q3 FY2026 release. |
| Observability | USD 0.269B | 1.7% | 3% | USD 0.820B | 3% | Cisco Q3 FY2026 release. |
| Services | USD 3.724B | 23.5% | -1% | USD 11.237B | 0% | Cisco Q3 FY2026 release. |

Q3 story ชัดเจนว่า Networking เป็น engine หลัก: revenue โต 25% YoY และ official release ระบุว่า networking product orders accelerated to more than 50% YoY. Security ยังไม่พิสูจน์ growth ใน reported revenue แม้ Splunk/AI-security narrative จะช่วย optionality.

## Financial Facts

| Metric | Latest value | Source |
|---|---:|---|
| Q3 FY2026 revenue | USD 15.841B | Cisco Q3 FY2026 release. |
| Q3 FY2026 GAAP operating income / margin | USD 3.960B / 25.0% | Cisco Q3 FY2026 release / calculation. |
| Q3 FY2026 net income | USD 3.373B | Cisco Q3 FY2026 release. |
| Q3 FY2026 diluted EPS / non-GAAP EPS | USD 0.85 / USD 1.06 | Cisco Q3 FY2026 release. |
| Q3 FY2026 free cash flow | USD 3.343B | Calculation: OCF USD 3.757B - capex USD 0.414B. |
| 9M FY2026 free cash flow | USD 7.771B | Calculation: OCF USD 8.791B - capex USD 1.020B. |
| TTM free cash flow | USD 11.788B | FY2025 FCF - 9M FY2025 FCF + 9M FY2026 FCF. |
| Cash plus investments | USD 16.640B | Cisco Q3 FY2026 release. |
| Total debt | USD 31.303B | Cisco Q3 FY2026 release calculation. |
| Net debt using cash plus investments | USD 14.663B | Cisco Q3 FY2026 release calculation. |
| RPO | USD 43.462B | Cisco Q3 FY2026 release. |
| FY2026 revenue guidance | USD 62.8B to USD 63.0B | Cisco Q3 FY2026 release. |
| FY2026 GAAP / non-GAAP EPS guidance | USD 3.16-3.21 / USD 4.27-4.29 | Cisco Q3 FY2026 release. |
| FY2026 hyperscaler AI infrastructure orders outlook | about USD 9B | Cisco Q3 FY2026 release. |

## Charts

See `raw/financials/CSCO_fundamentals.md` for source-backed quarterly YoY, YTD, annual FCF, segment revenue, cash-flow/capex, and balance-sheet chart blocks.

## Transcript / Management Commentary

Official release framed Q3 FY2026 as a record revenue quarter with double-digit top and bottom-line growth. Demand signal สำคัญคือ total product orders +35% YoY และ +19% excluding hyperscalers, พร้อม hyperscaler AI infrastructure orders USD 5.3B year to date.

Management raised FY2026 hyperscaler AI infrastructure order expectation to about USD 9B and AI infrastructure revenue expectation to about USD 4B. This materially improves growth narrative, but the valuation question is whether market price already capitalizes too much of that upside.

## Thesis

### Bull Case

CSCO มี quality cash engine, large installed base, meaningful subscription/service revenue, และกำลังได้ narrative ใหม่จาก AI networking infrastructure. Q3 FY2026 revenue โต 12%, Networking revenue โต 25%, product orders โต 35%, และ AI infrastructure order outlook ถูกยกขึ้นเป็น about USD 9B. Balance sheet ยังรับ debt ได้ และ TTM FCF USD 11.788B ยังรองรับ dividend, buyback, and reinvestment.

ถ้า AI networking demand เป็น multi-year refresh cycle ไม่ใช่ one-time hyperscaler spike, Cisco อาจ re-rate จาก legacy networking multiple ไปใกล้ broader AI infrastructure multiple ได้มากขึ้น.

### Bear Case

ราคา equity วิ่งนำ fundamentals ไปมาก. Latest accessible price USD 118.88 ทำให้ market cap ประมาณ USD 469.6B และ TTM FCF yield เหลือเพียง 2.51%. DCF base case ที่ใช้ TTM FCF source-backed ให้ fair value เพียงประมาณ USD 47.02 ต่อ diluted share, ต่ำกว่าราคาตลาดประมาณ 60%.

FCF ยังลดลง YoY ใน Q3 และ 9M FY2026 แม้ revenue/EPS ดีขึ้น. Security revenue ยัง flat to down, product-category profitability ไม่ disclosed, และ hyperscaler AI customer concentration ไม่ disclosed. ถ้า AI orders ไม่แปลงเป็น high-quality margin/FCF หรือถ้า market multiple normalize, downside risk สูง.

### Key Debate

คำถามหลักคือ Cisco กำลังเปลี่ยนจาก mature networking cash cow เป็น AI infrastructure growth compounder จริงหรือไม่. ถ้าใช่ multiple ที่สูงขึ้นอาจอยู่ได้นาน แต่ถ้า AI order surge เป็น cyclical/hyperscaler-heavy, current valuation มี margin of safety ต่ำมาก.

## Risks

- Valuation risk หลัง stock re-rate; TTM FCF yield เพียง 2.51%.
- AI infrastructure orders may be concentrated, lumpy, or lower-margin than investors expect.
- Security/Splunk growth integration risk; Security revenue was flat in Q3 and down 2% YTD.
- Product gross margin pressure from component/memory costs, tariffs, mix, and AI infrastructure hardware intensity.
- Supply chain and inventory purchase commitment risk as Cisco scales Silicon One and webscale demand.
- Competition from Arista, hyperscaler internal networking, white-box solutions, Palo Alto/Fortinet/security competitors, and cloud-native observability/security stacks.
- Debt and capital allocation risk after Splunk-related balance-sheet change.

## Catalysts

- Q4 FY2026 results and whether revenue reaches USD 16.7B to USD 16.9B guidance.
- Conversion of FY2026 AI infrastructure order target to revenue and FCF.
- Evidence that Networking order growth remains broad-based excluding hyperscalers.
- Security revenue recovery and Splunk cloud/subscription migration progress.
- Updated FY2026 10-K cash flow, capex, shares, and debt after fiscal year-end.
- Any disclosure around AI customer concentration, gross margin, or backlog conversion.

## Valuation Watch Items

- Current DCF memo: [[CSCO DCF Valuation 2026-05-20]].
- Base-case fair value from P11 is approximately USD 47.02 per diluted share versus latest accessible USD 118.88 close.
- Even the bull DCF scenario reaches only about USD 68.09 because current market price implies a very high FCF multiple.
- Watch TTM FCF, AI infrastructure revenue conversion, product gross margin, and market multiple before upgrading action read.

## Reports / Source Notes

| Note | Type |
|---|---|
| [[CSCO_latest_results_source]] | Latest results source note |
| [[CSCO_fundamentals]] | Normalized financial facts |
| [[CSCO DCF Valuation 2026-05-20]] | DCF valuation |
| [[CSCO Decision Memo 2026-05-20]] | Decision memo |

## Follow-Up

- Refresh after Q4 FY2026 / FY2026 results with updated revenue, GAAP EPS, non-GAAP EPS, OCF, capex, FCF, cash, investments, debt, shares, RPO, deferred revenue, and guidance.
- Verify whether FY2026 AI infrastructure revenue/order guidance converts into FCF rather than only revenue growth.
- Normalize official prepared remarks / Q&A transcript if available from Cisco IR.
- Re-check current price before any action change, especially because available quote sources were delayed.
- Track Security revenue recovery and Splunk integration economics.

## Missing / Unverified Data

| Item | Status | Notes |
|---|---|---|
| Q3 FY2026 Form 10-Q | ไม่พบข้อมูลที่ยืนยันได้ | Form 8-K/release is official, but full Q3 10-Q was not found in this workflow. |
| Official full prepared remarks / Q&A transcript | not normalized | Official event page was found; transcript text was not normalized from official source. |
| FY2026 full-year actual results | not disclosed | Q3 FY2026 is the latest official period found. |
| FY2026 FCF guidance | ไม่พบข้อมูลที่ยืนยันได้ | Cisco gave revenue, EPS, margins, AI order/revenue outlook, not FCF guidance. |
| Product-category operating profit | not disclosed | Revenue by category is disclosed; operating profit by category is not. |
| Hyperscaler AI customer concentration | not disclosed | AI infrastructure order target is disclosed, customer mix is not verified. |
| Market quote after 2026-05-18 close | ไม่พบข้อมูลที่ยืนยันได้ | Latest accessible close found was 2026-05-18; refresh before future action calls. |
| Investor-specific tax basis, position size, and required return | not provided | Needed for individualized add/hold/trim sizing. |
