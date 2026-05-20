---
type: entity
ticker: ATLX
company: Atlas Lithium Corporation
market: Nasdaq Capital Market
currency: USD
period_type: quarterly + annual
reporting_scope: Q1 2026 quarter ended 2026-03-31 plus FY2025 annual baseline
latest_period: Q1 2026
latest_period_end: 2026-03-31
latest_total_revenue_usd_m: 0.074386
latest_net_income_usd_m: -16.540056
source_gap_count: 8
source_gaps:
  - Commercial lithium revenue from Neves not disclosed or not yet generated.
  - Revenue guidance not verified.
  - Free cash flow guidance not verified.
  - Normalized positive FCF base for DCF not verified.
  - Final Neves financing package not verified.
  - Fully diluted share count not fully normalized.
  - Segment economics for future lithium concentrate production not verified.
  - Investor-specific position size, tax basis, and required return not provided.
source_notes:
  - raw/imports/ATLX_latest_results_source.md
normalized_markdown: raw/financials/ATLX_fundamentals.md
normalized_json: raw/financials/ATLX_fundamentals.json
tags:
  - entity/company
  - ticker/ATLX
---

# ATLX - Atlas Lithium Corporation

## Snapshot

| Item | Value |
|---|---|
| Ticker | ATLX |
| Company | Atlas Lithium Corporation |
| Market | Nasdaq Capital Market |
| Currency | USD |
| Latest period | Q1 2026, quarter ended 2026-03-31 |
| Reporting scope | Q1 2026 plus FY2025 annual baseline |
| Normalized file | `raw/financials/ATLX_fundamentals.md` |
| Latest price check | USD 4.275 intraday on 2026-05-19 2:55 PM EDT; market cap USD 126.07M |
| Current action read | AVOID new capital / WATCHLIST only |

## Source Map

| Priority | Source | Status | Notes |
|---:|---|---|---|
| 1 | SEC / official filings | Available | Q1 2026 Form 10-Q and FY2025 Form 10-K reviewed. |
| 1 | Official company news / IR | Available | Apr. 2026 project and critical-minerals updates reviewed; forward-looking. |
| 2 | Earnings transcript / call material | Not found | No official earnings-call transcript normalized in this workflow. |
| 3 | Financial statements / market data | Available | StockAnalysis used only for fresh price / market cap / EV. |
| 4 | News / web context | Limited | Not needed beyond official company news for durable facts. |

## Business Model

ATLX เป็น exploration/development-stage critical minerals company ที่ focus หลักคือการผลักดัน `Neves Project` ใน Minas Gerais, Brazil ไปสู่ lithium concentrate production. ณ Q1 2026 financials บริษัทมีรายได้เล็กมากจาก Iron ore project ไม่ใช่ commercial lithium concentrate revenue.

Investment case จึงไม่ใช่ operating cash-flow compounder ในปัจจุบัน แต่เป็น project-development / financing / execution story. คุณภาพ thesis ขึ้นกับการเปลี่ยน DFS economics ให้เป็น actual production, securing financing, commissioning plant, controlling capex, และขาย lithium concentrate ตาม offtake / market demand.

## Segments / Revenue Mix

| Item | Q1 2026 Fact | Source |
|---|---|---|
| Reportable segment | Mining | SEC Form 10-Q. |
| Q1 2026 revenue source | Exclusively Iron ore project | SEC Form 10-Q. |
| Customer concentration | One customer accounted for 100% of Q1 2026 revenue | SEC Form 10-Q. |
| Other projects | Exploration phase | SEC Form 10-Q. |
| Main development focus | Neves Project near Aracuai, Minas Gerais, Brazil | SEC Form 10-Q. |

ยังไม่มี source-backed lithium revenue mix เพราะ Neves ยังไม่ถูกพิสูจน์ใน actual operating results.

## Financial Facts

| Metric | Latest value | Source |
|---|---:|---|
| Q1 2026 net revenue | USD 0.074M | SEC Form 10-Q. |
| Q1 2026 operating loss | USD (16.792M) | SEC Form 10-Q. |
| Q1 2026 net loss | USD (16.540M) | SEC Form 10-Q. |
| Q1 2026 net loss attributable to ATLX stockholders | USD (13.557M) | SEC Form 10-Q. |
| Q1 2026 basic/diluted loss per share | USD (0.50) | SEC Form 10-Q. |
| Q1 2026 operating cash flow | USD (10.630M) | SEC Form 10-Q. |
| Q1 2026 FCF before capitalized exploration | USD (11.843M) | SEC Form 10-Q calculation. |
| Cash and cash equivalents | USD 34.359M | SEC Form 10-Q, 2026-03-31. |
| Convertible Debt | USD 10.180M | SEC Form 10-Q, 2026-03-31. |
| Deferred consideration from royalties sold | USD 20.000M | SEC Form 10-Q, 2026-03-31. |
| Cover-page shares outstanding | 29,490,887 | SEC Form 10-Q, 2026-05-04. |
| FY2025 FCF before capitalized exploration | USD (28.258M) | SEC Form 10-K calculation. |

## Charts

See `raw/financials/ATLX_fundamentals.md` for source-backed quarterly YoY, annual cash-burn, cash-flow/capex, and balance-sheet chart blocks.

## Transcript / Management Commentary

ไม่พบ official earnings-call transcript ที่ normalize ได้ใน workflow นี้. Management commentary ที่ durable ได้มาจาก Form 10-Q และ official press releases:

- บริษัทมี historical net operating losses และยังไม่ได้ generate material revenues.
- Liquidity หลักมาจาก equity financing และ equity financing ของ subsidiary.
- Management เชื่อว่า cash/equivalents เพียงพอสำหรับ working capital และ capex needs อย่างน้อย 12 เดือนจาก financial-statement date.
- หาก current resources ไม่พอ บริษัทอาจต้องหา equity หรือ debt financing เพิ่ม.
- Q1 2026 update ชี้ว่า company focus คือ Neves implementation และมี written indications of interest จากหลายฝ่ายสำหรับ future lithium concentrate supply, แต่ยังไม่ใช่ binding revenue guidance ใน source note นี้.

## Thesis

### Bull Case

Bull case อยู่ที่ project optionality: ถ้า Neves เปลี่ยนจาก DFS เป็น producing asset ได้จริง ATLX อาจมี upside สูงเมื่อเทียบกับ market cap ประมาณ USD 126M. Official releases disclose expected production around 146,000 tonnes/year, estimated operating cost USD 489/tonne at mine gate, DFS NPV USD 539M, IRR 145%, และ payback 11 เดือน. Mitsui offtake / strategic investment และ Japan-U.S. critical-minerals attention ช่วยเพิ่ม strategic relevance.

### Bear Case

Bear case หนักกว่าใน data ปัจจุบัน: company ยังไม่มี commercial lithium revenue, Q1 2026 net revenue แค่ USD 74k, net loss USD 16.5M, Q1 FCF burn ก่อน capitalized exploration ประมาณ USD 11.8M, และ liquidity ยังพึ่ง financing. DFS economics เป็น forward-looking project model ไม่ใช่ realized cash flow. Dilution risk สูงเพราะ company ใช้ equity/ subsidiary equity financing เป็น funding source หลัก.

### Key Debate

คำถามหลักคือ Neves จะถูก finance, build, commission, และ ramp ได้ตาม DFS economics หรือไม่. จนกว่าจะมี binding financing / construction milestones / commercial shipment / realized unit economics, ATLX ยังเป็น speculative project-development equity มากกว่าธุรกิจที่ DCF ได้จาก recurring FCF.

## Risks

- Pre-production risk: no verified commercial lithium revenue from Neves.
- Financing risk: future capital needs may require equity or debt financing.
- Dilution risk: Q1/FY2025 financing relied heavily on share issuance and subsidiary equity raise.
- Commodity risk: lithium concentrate price and demand can move sharply.
- Construction / commissioning risk: plant installation, partner execution, capex, schedule, and ramp may differ from DFS.
- Brazil/regulatory/community risk: mining permits, environmental obligations, local stakeholders, and FX/operating conditions matter.
- Customer concentration: Q1 2026 revenue was from one Iron ore customer.
- Related-party / subsidiary complexity: Atlas Critical Minerals is consolidated as VIE and involves related-party transactions.

## Catalysts

- Binding Neves financing package or confirmed government/strategic support.
- Detailed construction milestones and 100% partner readiness for remaining scopes.
- Plant commissioning and first commercial lithium concentrate shipment.
- Mitsui/offtake fulfillment milestones.
- Evidence that realized capex, operating cost, grade/recovery, and product price are close to DFS assumptions.
- Quarterly updates showing lower cash burn or non-dilutive funding.

## Valuation Watch Items

- Current valuation memo: [[ATLX DCF Valuation 2026-05-20]].
- P11 stopped before fair value because normalized positive FCF, revenue guidance, FCF guidance, and realized lithium economics are not verified.
- Watch cash burn vs USD 34.359M cash, convertible debt USD 10.180M, royalty liability USD 20.000M, and share count after ATM / compensation / conversion.
- For any future DCF, require commercial revenue, operating cost evidence, capex-to-completion, funding structure, fully diluted shares, and lithium price assumptions.

## Reports / Source Notes

| Note | Type |
|---|---|
| [[ATLX_latest_results_source]] | Latest results source note |
| [[ATLX_fundamentals]] | Normalized financial facts |
| [[ATLX DCF Valuation 2026-05-20]] | DCF stop / valuation gap memo |
| [[ATLX Decision Memo 2026-05-20]] | Decision memo |

## Follow-Up

- Re-check after next 10-Q or any Neves financing / commissioning 8-K.
- Normalize fully diluted share count from options, warrants, RSUs, and convertible instruments before any valuation upgrade.
- Track cash burn, ATM use, subsidiary financings, and convertible debt.
- Verify whether project contracts remain at/below DFS budget after full scope awards.
- Require commercial shipment and realized unit economics before running a production-based DCF.

## Missing / Unverified Data

| Item | Status | Notes |
|---|---|---|
| Commercial lithium revenue from Neves | not disclosed / not yet generated | Q1 2026 revenue came from Iron ore project. |
| Revenue guidance | ไม่พบข้อมูลที่ยืนยันได้ | Project production/cost targets are not revenue guidance. |
| FCF guidance | ไม่พบข้อมูลที่ยืนยันได้ | No official FCF guide found. |
| Normalized positive FCF base for DCF | ไม่พบข้อมูลที่ยืนยันได้ | Q1 and FY2025 FCF are negative. |
| Final Neves financing package | ไม่พบข้อมูลที่ยืนยันได้ | Potential U.S./Japan support is not committed financing in extracted sources. |
| Fully diluted share count | not fully normalized | Cover/basic shares are verified; full dilution needs separate securities schedule normalization. |
| Realized lithium concentrate unit economics | ไม่พบข้อมูลที่ยืนยันได้ | DFS numbers are forward-looking until production starts. |
| Investor-specific position size, tax basis, required return | not provided | Needed for personalized action sizing. |
