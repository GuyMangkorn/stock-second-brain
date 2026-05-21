---
type: entity
ticker: DELL
company: Dell Technologies Inc.
market: NYSE
currency: USD
period_type: annual
reporting_scope: "FY2026 fiscal year ended 2026-01-30; FY2027 guidance; market-data check 2026-05-21"
latest_period: FY2026
latest_period_end: 2026-01-30
latest_total_revenue_usd_m: 113538
latest_net_income_usd_m: 5936
source_gap_count: 7
source_gaps:
  - FY2027 Q1 actual results are not available as of the 2026-05-21 source check.
  - FY2027 free cash flow guidance is not disclosed.
  - Product-level and customer-level AI server profitability is not disclosed.
  - Segment-level FCF is not disclosed.
  - AI server order/backlog split by customer type is not disclosed.
  - DFS debt valuation treatment requires explicit judgment.
  - Investor-specific cost basis, position size, tax status, and required return were not provided.
source_notes:
  - raw/imports/DELL_latest_results_source.md
normalized_markdown: raw/financials/DELL_fundamentals.md
normalized_json: raw/financials/DELL_fundamentals.json
tags:
  - entity/company
  - ticker/DELL
---

# DELL - Dell Technologies Inc.

## Snapshot

| Item | Value |
|---|---|
| Ticker | DELL |
| Company | Dell Technologies Inc. |
| Market | NYSE |
| Currency | USD |
| Latest period | FY2026 fiscal year ended 2026-01-30 |
| Latest official result | Q4 / FY2026 results released 2026-02-26; FY2026 Form 10-K filed 2026-03-16 |
| Current price check | USD 242.93 close on 2026-05-20; USD 242.39 pre-market on 2026-05-21 6:52 AM EDT |
| Market cap / shares out | USD 157.80B / 649.57M provider values |
| Normalized file | `raw/financials/DELL_fundamentals.md` |
| Decision read | WAIT / AVOID-new-capital at current price; revisit after FY2027 Q1 results |

## Source Map

| Priority | Source | Status | Notes |
|---:|---|---|---|
| 1 | FY2026 Form 10-K | Verified | Annual financial statements, segment revenue, debt split, diluted shares. |
| 1 | FY2026 Q4 / full-year release | Verified | Latest official results, FCF, balance sheet, and FY2027 guidance. |
| 2 | Q4 FY2026 IR-hosted earnings transcript | Verified | Management commentary on AI backlog, supply, pricing, margin protection, and cash-flow caveat. |
| 3 | StockAnalysis market quote | Verified as provider source | Fresh current market data checked 2026-05-21. |
| 3 | Dell IR upcoming events | Verified | FY2027 Q1 results scheduled 2026-05-28. |

## Business Model

Dell เป็น technology hardware และ infrastructure vendor ที่ขาย servers, storage, networking, PCs, services, support และ financing ผ่าน Dell Financial Services. Thesis ตอนนี้ไม่ได้เป็น PC-only story แล้ว แต่ pivot สำคัญคือ AI infrastructure ผ่าน `Infrastructure Solutions Group` โดยเฉพาะ AI-optimized servers ที่โตจาก USD 9.3B ใน FY2025 เป็น USD 24.7B ใน FY2026.

ธุรกิจยังมี cyclicality สูงกว่าซอฟต์แวร์ เพราะ gross margin ถูกกดจาก hardware mix, component cost, memory/GPU supply, และ pricing cycle. จุดแข็งคือ scale, supply chain, customer relationships, deployment/service attach และ financing capability.

## Segments / Revenue Mix

| Segment / Category | FY2026 Revenue | FY2026 Read |
|---|---:|---|
| ISG - AI-optimized servers | 24,683 | ตัวขับ growth หลัก; demand, backlog, และ FY2027 guidance ชี้ว่ายังแรงมาก |
| ISG - Traditional servers and networking | 19,512 | ได้ประโยชน์จาก modernization และ compute refresh |
| ISG - Storage | 16,631 | Stable growth; potential attach กับ enterprise AI deployments |
| CSG - Commercial | 44,062 | PC commercial recovery / share opportunity |
| CSG - Consumer | 6,922 | ยังอ่อนกว่า commercial และลดลง YoY ใน FY2026 |

## Financial Facts

- FY2026 revenue: USD 113.538B, +19% YoY.
- FY2026 operating income: USD 8.149B; operating margin 7.2%.
- FY2026 net income attributable: USD 5.936B; diluted EPS USD 8.68.
- FY2026 FCF: USD 8.555B from OCF USD 11.185B minus capex / capitalized software spend USD 2.630B.
- Cash and equivalents at 2026-01-30: USD 11.528B.
- Debt principal at 2026-01-30: core debt USD 17.018B, DFS related debt USD 14.646B, total debt USD 31.763B.
- FY2027 guidance: revenue midpoint USD 140B, AI-optimized server revenue roughly USD 50B, GAAP EPS midpoint USD 11.52, non-GAAP EPS midpoint USD 12.90.

## Charts

See `raw/financials/DELL_fundamentals.md` for annual trend, segment revenue, cash flow/capex, and balance sheet chart blocks.

## Transcript / Management Commentary

Management emphasized AI demand as the key driver: FY2026 AI orders were USD 64.1B, shipments were about USD 25B, and exiting AI backlog was USD 43B. The forward debate is not just demand, but whether Dell can protect margin while supply is tight and input costs reset higher.

Important P6 read: management said the company uses shorter quote validity, dynamic pricing, list price changes, discount control, and reduced promotions to protect margins. นี่เป็น operational lever ที่สำคัญ เพราะ AI server revenue โตเร็วแต่ margin mix ยังต่ำกว่า classic enterprise hardware/software-like economics.

On cash flow, management did not give formal FY2027 FCF guidance. เพราะฉะนั้น P11 valuation ใช้ FY2026 verified FCF เป็น base ไม่ใช่การเดา FY2027 FCF guidance.

## Thesis

### Bull Case

DELL อาจเป็น AI infrastructure scale beneficiary ที่ยังมี execution runway ใหญ่: backlog USD 43B, FY2027 AI server revenue guidance roughly USD 50B, และ FY2027 revenue midpoint USD 140B. ถ้า pricing actions ชดเชย component inflation ได้ และ storage/services attach เพิ่มตาม enterprise AI deployments, FCF could grow faster than old hardware-cycle expectations.

### Bear Case

Current price already discounts a lot of the AI upside. At USD 242.93 close, market cap is about USD 157.8B and market cap / FY2026 FCF is about 18.4x. ถ้า AI server margins stay mid-single-digit, component costs keep moving up, หรือ backlog conversion has timing / supply issues, valuation support can compress fast.

### Key Debate

คำถามหลักคือ AI revenue growth จะ translate เป็น durable FCF growth ได้แค่ไหน. Revenue guidance ใหญ่และชัด แต่ FCF guidance ไม่ disclosed, segment-level FCF ไม่ disclosed, และ DFS debt treatment ทำให้ valuation ต้องระวังเป็นพิเศษ.

## Risks

- AI server gross / operating margin dilution if mix shifts toward lower-margin hardware faster than attach and pricing can compensate.
- Component supply tightness and memory/GPU cost inflation.
- Customer concentration risk in large AI infrastructure orders is not fully disclosed.
- CSG remains cyclical and exposed to PC demand, pricing, and refresh timing.
- Balance sheet optics are complicated by DFS; total liabilities exceed assets and total debt is high, even though DFS debt has financing-asset backing.
- Current valuation embeds strong FY2027 execution before FY2027 Q1 actual results are available.

## Catalysts

- FY2027 Q1 results on 2026-05-28.
- AI server backlog conversion and new order trends.
- Evidence that storage, networking, services, and deployment attach improve AI economics.
- Any disclosed FY2027 cash-flow or working-capital update.
- Gross margin stabilization despite component cost pressure.
- Continued buybacks and dividend growth if FCF remains strong.

## Valuation Watch Items

- Base-case DCF in `wiki/analysis/valuations/DELL DCF Valuation 2026-05-21.md` estimates fair value around USD 209/share using FY2026 FCF, 10.0% WACC, 2.5% terminal growth, FY2026 diluted shares, and core debt treatment.
- At USD 242.93 close, base case implies roughly 14% downside, so margin of safety is not present for new capital.
- A stricter total-debt treatment lowers the implied value; a current-share-count treatment raises per-share value. This is why DFS treatment must stay explicit.

## Reports / Source Notes

- [[DELL_latest_results_source]]
- [[DELL_fundamentals]]
- [[DELL DCF Valuation 2026-05-21]]
- [[DELL Decision Memo 2026-05-21]]

## Follow-Up

- Refresh immediately after FY2027 Q1 results on 2026-05-28.
- Check Q1 revenue, EPS, OCF/FCF if disclosed, cash, debt, share count, AI server shipments/orders/backlog, and gross margin.
- Watch whether FY2027 guidance changes after Q1.
- Re-run valuation if management gives FY2027 FCF or working-capital guidance.

## Missing / Unverified Data

- FY2027 Q1 actual results are not available as of the 2026-05-21 source check.
- FY2027 free cash flow guidance is not disclosed.
- Product-level and customer-level AI server profitability is not disclosed.
- Segment-level FCF is not disclosed.
- AI server order/backlog split by enterprise, neocloud, and sovereign customers is not disclosed.
- DFS debt valuation treatment requires explicit judgment.
- Investor-specific cost basis, position size, tax status, and required return were not provided.
