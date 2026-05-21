---
type: entity
ticker: IBM
company: International Business Machines Corporation
market: NYSE
currency: USD
period_type: quarterly + annual
reporting_scope: Q1 2026 quarter ended 2026-03-31 plus FY2025 annual baseline
latest_period: Q1 2026
latest_period_end: 2026-03-31
latest_total_revenue_usd_m: 15917
latest_net_income_usd_m: 1216
source_gap_count: 7
source_gaps:
  - Full FY2026 actual results are not disclosed.
  - Product-level AI revenue and AI margins are not disclosed.
  - Exact Q1 2026 generative AI book of business value was not verified.
  - Segment-level FCF is not disclosed.
  - Full detailed balance sheet was not normalized in this pass.
  - Financing debt treatment requires explicit valuation judgment.
  - Investor-specific cost basis, position size, tax status, and required return were not provided.
source_notes:
  - raw/imports/IBM_latest_results_source.md
normalized_markdown: raw/financials/IBM_fundamentals.md
normalized_json: raw/financials/IBM_fundamentals.json
tags:
  - entity/company
  - ticker/IBM
---

# IBM - International Business Machines Corporation

## Snapshot

| Item | Value |
|---|---|
| Ticker | IBM |
| Company | International Business Machines Corporation |
| Market | NYSE |
| Currency | USD |
| Latest period | Q1 2026, quarter ended 2026-03-31 |
| Reporting scope | Q1 2026 plus FY2025 annual baseline |
| Normalized file | `raw/financials/IBM_fundamentals.md` |
| Latest price check | USD 224.88 close on 2026-05-20; checked 2026-05-21 Asia/Bangkok |
| Current action read | HOLD / WATCHLIST; ADD only with margin of safety or clearer FCF/debt proof |

IBM เป็น Software-led Hybrid Cloud and AI platform company ที่ยังมี Consulting, Infrastructure, Financing และ mainframe cycle exposure ผสมอยู่ใน business model. Q1 2026 official sources แสดง revenue growth, margin expansion, FCF growth และ guidance ที่ยังมั่นใจ แต่ balance sheet มี leverage สูงหลัง Confluent และ acquisition-led strategy จึงต้อง underwrite debt และ FCF durability อย่างระวัง.

## Source Map

| Priority | Source | Status | Notes |
|---:|---|---|---|
| 1 | SEC / official filings | Found | Q1 2026 Form 10-Q, accession `0000051143-26-000038`, filed 2026-04-23; FY2025 10-K / annual report extract reviewed. |
| 1 | Official company results | Found | IBM Q1 2026 earnings release used for segment revenue, cash/debt summary, guidance, and dividend. |
| 2 | Earnings transcript / call material | Found | IBM official 1Q26 prepared remarks used for management commentary and guidance detail. |
| 3 | Financial statements / metrics | Found | Stooq used only for fresh market price; market cap calculated from official IBM shares outstanding. |
| 4 | News / web context | Not used for durable financial facts | Official sources were sufficient for core flow. |

## Business Model

IBM monetizes enterprise technology through software subscriptions/license and support, consulting engagements, infrastructure sales/support, and financing. The strategic center is hybrid cloud and AI: Red Hat, automation, data, transaction processing, watsonx, consulting transformation work, and IBM Z / distributed infrastructure.

| Business line | Revenue mechanism | Durable driver | Primary source |
|---|---|---|---|
| Software | Hybrid cloud and AI platforms, Red Hat, automation, data, transaction processing, subscriptions and licenses | Enterprise hybrid cloud standardization, AI orchestration/governance, Red Hat platform adoption, recurring software support | IBM Q1 2026 Form 10-Q and prepared remarks. |
| Consulting | Strategy and technology, intelligent operations, implementation and transformation services | Enterprise modernization, AI/data transformation, backlog conversion, asset-led delivery productivity | IBM Q1 2026 prepared remarks. |
| Infrastructure | IBM Z, Power, Storage, infrastructure support | Mainframe refresh cycle, resilient mission-critical workloads, on-platform AI inference, storage/Power demand | IBM Q1 2026 Form 10-Q and prepared remarks. |
| Financing | Client financing and commercial financing | Enables large enterprise transactions and hardware/software adoption, but adds debt and receivables complexity | IBM Q1 2026 Form 10-Q. |

## Segments / Revenue Mix

| Segment | Q1 2026 Revenue | Q1 2026 Mix | Reported YoY | Constant-Currency YoY | Source |
|---|---:|---:|---:|---:|---|
| Software | USD 7.052B | 44.30% | 11% | 8% | IBM Q1 2026 earnings release / Form 10-Q. |
| Consulting | USD 5.272B | 33.12% | 4% | 1% | IBM Q1 2026 earnings release / Form 10-Q. |
| Infrastructure | USD 3.326B | 20.90% | 15% | 12% | IBM Q1 2026 earnings release / Form 10-Q. |
| Financing | USD 0.220B | 1.38% | 15% | 10% | IBM Q1 2026 earnings release / Form 10-Q. |
| Other | USD 0.048B | 0.30% | -21.31% | not emphasized | IBM Q1 2026 earnings release / Form 10-Q. |

Q1 mix shows IBM is now clearly Software-led by revenue, but Consulting and Infrastructure still matter. Infrastructure growth was boosted by z17 / IBM Z strength, while Consulting remained slower despite better signings and high GenAI backlog penetration.

## Financial Facts

| Metric | Latest value | Source |
|---|---:|---|
| Q1 2026 revenue | USD 15.917B | IBM Q1 2026 Form 10-Q. |
| Q1 2026 GAAP gross margin | 56.23% | Calculation: 8.950 / 15.917. |
| Q1 2026 GAAP net income | USD 1.216B | IBM Q1 2026 Form 10-Q. |
| Q1 2026 diluted EPS / operating EPS | USD 1.28 / USD 1.91 | IBM Q1 2026 Form 10-Q; operating EPS is non-GAAP. |
| Q1 2026 IBM-defined FCF | USD 2.220B | IBM Q1 2026 Form 10-Q reconciliation. |
| TTM IBM-defined FCF | USD 14.992B | FY2025 FCF - Q1 2025 FCF + Q1 2026 FCF. |
| Cash + restricted cash + marketable securities | USD 11.828B | IBM Q1 2026 Form 10-Q. |
| Total debt | USD 66.4B | IBM Q1 2026 earnings release. |
| IBM Financing debt included in total debt | USD 12.8B | IBM Q1 2026 earnings release and prepared remarks. |
| FY2026 revenue guidance | More than 5% constant-currency growth | IBM Q1 2026 earnings release and prepared remarks. |
| FY2026 FCF guidance | About USD 1B YoY increase | IBM Q1 2026 earnings release and prepared remarks. |

## Charts

See `raw/financials/IBM_fundamentals.md` for source-backed quarterly YoY, annual, segment mix, cash-flow/capex, and balance-sheet chart blocks.

## Transcript / Management Commentary

Management described Q1 2026 as a strong start, with 6% constant-currency revenue growth and 13% free cash flow growth. The strategic message is that enterprises want AI across hybrid environments where they can control data, governance, security, and infrastructure choice.

Key commentary:

- Software constant-currency revenue grew 8%; Red Hat grew 10%; OpenShift was described as a USD 2B ARR business.
- Consulting revenue grew 1% constant currency, signings returned to 6% growth, and generative AI represented about 30% of Consulting backlog.
- Infrastructure grew 12% constant currency; IBM Z grew 48% constant currency as z17 continued to outperform prior programs.
- Management maintained FY2026 guidance for more than 5% constant-currency revenue growth and about USD 1B FCF growth.
- Confluent adds strategic Data/AI value but creates dilution and acquisition/debt integration risk.

## Thesis

### Bull Case

IBM มี setup ที่น่าสนใจสำหรับ investor ที่ต้องการ enterprise AI exposure แบบ valuation ไม่สุดโต่งเท่า mega-cap AI infrastructure names. Q1 2026 official sources support revenue growth, margin expansion, FCF growth และ FY2026 FCF guidance ที่ประมาณ USD 15.7B. Software is the center of gravity, Red Hat/OpenShift มี recurring platform value, และ IBM Z cycle ยังช่วย Infrastructure ในระยะสั้น.

ถ้า IBM ทำให้ Software โต 10%+ ได้จริง, Consulting กลับมา low-to-mid-single-digit growth, และ FCF โตตาม guidance พร้อมลด leverage หลัง Confluent, stock อาจสมควรได้ multiple สูงกว่า legacy IT services perception.

### Bear Case

Debt and business mix are the main friction. Total debt USD 66.4B เทียบกับ TTM FCF USD 14.992B ทำให้ total debt / FCF ประมาณ 4.43x. แม้ IBM Financing debt มี receivables backing บางส่วน แต่ equity valuation ต้องไม่ ignore balance sheet complexity. Consulting growth ยังต่ำ, AI economics ไม่ได้ disclosed ใน product-level revenue/margin, และ Infrastructure growth มี mainframe cycle component ที่อาจไม่ recurring เท่า Software.

DCF base case gives only modest upside versus current price. นี่ไม่ใช่ obvious bargain ถ้าต้องการ large margin of safety.

### Key Debate

คำถามหลักคือ IBM กำลัง transition เป็น durable Software-led AI/hybrid-cloud FCF compounder ได้จริงหรือยัง หรือ market กำลังให้เครดิตเร็วเกินไปกับ AI narrative, z17 cycle, และ acquisition-led growth. Evidence หลัง Q1 2026 ดีขึ้น แต่ยังต้องพิสูจน์ leverage reduction และ recurring Software/Consulting acceleration ต่อเนื่อง.

## Risks

- Total debt increased after Confluent; deleveraging depends on durable FCF.
- IBM Financing debt and receivables complicate simple EV / FCF interpretation.
- Product-level AI revenue and margins are not disclosed, so AI monetization cannot be directly underwritten.
- Consulting growth remains slow despite AI backlog penetration.
- Infrastructure strength includes z17 / mainframe cycle benefit that may normalize.
- Acquisition integration risk from Confluent, DataStax, HashiCorp and other software deals.
- FX can affect reported growth, while management often frames growth at constant currency.

## Catalysts

- Q2 2026 revenue growth and operating pre-tax margin expansion versus guidance.
- FY2026 FCF tracking toward about USD 15.7B.
- Evidence that Software grows 10%+ and Red Hat/OpenShift keep accelerating.
- Consulting signings and GenAI backlog converting into revenue growth.
- Debt reduction after Confluent and lower IBM Financing debt.
- More explicit disclosure on AI book of business, product-level AI revenue, margins, or backlog conversion.

## Valuation Watch Items

- Current DCF memo: [[IBM DCF Valuation 2026-05-21]].
- Base-case fair value is about USD 240.27 per diluted share versus USD 224.88 latest close, implying roughly 6.8% upside.
- Bear case is about USD 152.63 and bull case about USD 367.87; wide range reflects FCF durability, debt treatment, and terminal multiple sensitivity.
- Current price does not provide a large margin of safety, but IBM is not obviously overvalued on a source-backed FCF DCF if management's FY2026 FCF guidance holds.

## Reports / Source Notes

| Note | Type |
|---|---|
| [[IBM_latest_results_source]] | Latest results source note |
| [[IBM_fundamentals]] | Normalized financial facts |
| [[IBM DCF Valuation 2026-05-21]] | DCF valuation |
| [[IBM Decision Memo 2026-05-21]] | Decision memo |

## Follow-Up

- Refresh after Q2 2026 results with revenue, Software/Consulting/Infrastructure growth, FCF, cash, debt, shares, guidance, and any updated AI book-of-business disclosure.
- Track whether FY2026 FCF is progressing toward about USD 15.7B.
- Track post-Confluent debt reduction and interest expense.
- Watch Consulting signings/backlog conversion and whether GenAI backlog becomes durable revenue.
- Refresh price before changing the HOLD / WATCHLIST action read.

## Missing / Unverified Data

| Item | Status | Notes |
|---|---|---|
| Full FY2026 actual results | not disclosed | Q1 2026 is the latest official period found. |
| Product-level AI revenue and AI margins | not disclosed | Cannot directly model AI unit economics. |
| Exact Q1 2026 generative AI book of business value | ไม่พบข้อมูลที่ยืนยันได้ | Not verified in the source set. |
| Segment-level FCF | not disclosed | Consolidated FCF only. |
| Full detailed balance sheet normalization | not completed | P11/P13 required cash, debt, shares, and FCF; other lines can be normalized later. |
| Financing debt treatment | judgment required | DCF uses total debt conservatively and separately shows IBM Financing debt caveat. |
| Investor-specific tax basis, position size, tax status, and required return | not provided | Needed for final sizing. |
