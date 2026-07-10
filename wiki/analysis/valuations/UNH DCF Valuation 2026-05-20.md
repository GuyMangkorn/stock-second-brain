---
type: analysis
analysis_type: dcf-valuation
ticker: UNH
company: UnitedHealth Group Incorporated
date: 2026-05-20
currency: USD
base_fair_value_per_share: 258.41
current_price: 385.99
source_files:
  - raw/imports/UNH_latest_results_source.md
  - raw/financials/UNH_fundamentals.md
  - raw/financials/UNH_fundamentals.json
  - wiki/entities/UNH.md
tags:
  - analysis/valuation
  - ticker/UNH
---

# UNH DCF Valuation - 2026-05-20
Entity: [[UNH]]

## Bottom Line

Base case DCF fair value อยู่ประมาณ **USD 258.41 per diluted share** เทียบกับ fresh intraday price **USD 385.99** จาก StockAnalysis วันที่ 2026-05-20 11:50 AM EDT. อ่านแบบตรงไปตรงมาคือ current price ยังสูงกว่า base fair value ราว 33%.

Bull case ไปถึงประมาณ **USD 458.83** ได้ แต่ต้องใช้ TTM FCF ที่ได้แรงหนุนจาก Q1 2026 cash flow, lower WACC, และ recovery assumptions ที่ค่อนข้างดี. Bear case อยู่ประมาณ **USD 176.44** หาก FY2025 FCF เป็นฐานที่สะท้อน pressure ใหม่มากกว่า temporary trough.

เพราะ UNH เป็น managed care / health services hybrid ที่มี insurance-like capital, medical-cost reserve, regulatory, and investment-portfolio dynamics, DCF นี้ควรใช้เป็น scenario framework ไม่ใช่ precision price target.

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| `raw/imports/UNH_latest_results_source.md` | Local source note | P1 extracted source facts and fresh market-data checks. |
| `raw/financials/UNH_fundamentals.md` | Local normalized facts | P4 financial table, cash/debt/share/FCF facts. |
| `wiki/entities/UNH.md` | Local entity page | Business model, risks, and thesis context. |
| SEC Form 10-Q, Q1 2026 | https://www.sec.gov/Archives/edgar/data/731766/000073176626000127/unh-20260331.htm | Cash, debt, shares, cash flow, and Q1 operating facts. |
| SEC Form 10-K, FY2025 | https://www.sec.gov/Archives/edgar/data/731766/000073176626000062/unh-20251231.htm | FY2025/FY2024/FY2023 cash flow baseline. |
| UnitedHealth Q1 2026 release | https://www.unitedhealthgroup.com/content/dam/UHG/PDF/investors/2026/unh-reports-first-quarter-2026-results.pdf | Guidance, non-GAAP reconciliation, segment and operating metrics. |
| StockAnalysis UNH statistics | https://stockanalysis.com/stocks/unh/statistics/ | Fresh price, market cap, EV, shares, and market ratios. |
| MarketBeat UNH quote | https://www.marketbeat.com/stocks/NYSE/UNH/ | Fresh price and market cap cross-check. |

## Input Table

| Input | Value | Source / Calculation |
|---|---:|---|
| Current price | USD 385.99 | StockAnalysis, 2026-05-20 11:50 AM EDT. |
| Market cap | USD 350.53B | StockAnalysis, checked 2026-05-20. |
| Enterprise value | USD 401.37B | StockAnalysis, checked 2026-05-20. |
| Shares outstanding | 908.14M | StockAnalysis; SEC exact count 908,144,404 as of 2026-04-30. |
| Diluted shares used for DCF | 910M | SEC Q1 2026 diluted weighted-average shares. |
| Cash plus short-term investments | USD 31.229B | SEC Form 10-Q calculation. |
| Total debt | USD 77.917B | SEC Form 10-Q calculation. |
| Net debt | USD 46.688B | Total debt - cash plus short-term investments. |
| FY2025 FCF | USD 16.075B | FY2025 OCF 19.697B - capex 3.622B. |
| TTM FCF | USD 19.666B | FY2025 FCF 16.075B - Q1 2025 FCF 4.558B + Q1 2026 FCF 8.149B. |
| FY2026 FCF guidance | ไม่พบข้อมูลที่ยืนยันได้ | Not disclosed in extracted official sources. |
| FY2026 GAAP EPS guidance | Greater than USD 17.35 | UnitedHealth Q1 2026 release. |
| FY2026 adjusted EPS guidance | Greater than USD 18.25 | UnitedHealth Q1 2026 release; non-GAAP. |

## Base Case Assumptions

| Assumption | Bear | Base | Bull |
|---|---:|---:|---:|
| FCF anchor | USD 16.075B | USD 16.075B | USD 19.666B |
| Year 1 FCF growth | 0.0% | 4.0% | 6.0% |
| Year 2 FCF growth | 2.0% | 5.0% | 6.5% |
| Year 3 FCF growth | 3.0% | 5.5% | 6.5% |
| Year 4 FCF growth | 3.5% | 5.5% | 6.0% |
| Year 5 FCF growth | 3.5% | 5.0% | 5.5% |
| WACC | 10.0% | 9.0% | 8.0% |
| Terminal growth | 2.0% | 2.5% | 3.0% |

Base WACC ใช้ Health Care range 8%-10% จาก vault reference และเลือก 9.0% เพราะ UNH มี scale / investment-grade-like access to capital แต่มี regulatory, medical cost, managed-care reserve, PBM, and public-trust risk สูงกว่าบริษัท healthcare product ที่ simple กว่า.

## FCF Projection

Base case uses FY2025 FCF as conservative anchor, because Q1 2026 TTM FCF benefits from strong Q1 working-capital dynamics and FY2026 official FCF guidance is not disclosed.

| Year | FCF | PV at 9.0% |
|---:|---:|---:|
| 1 | 16,718 | 15,338 |
| 2 | 17,554 | 14,775 |
| 3 | 18,519 | 14,300 |
| 4 | 19,538 | 13,841 |
| 5 | 20,515 | 13,333 |

## Valuation Summary

| Scenario | EV | Equity Value | Fair Value / Share | Upside / Downside vs USD 385.99 | Read |
|---|---:|---:|---:|---:|---|
| Bear | 207,249 | 160,561 | 176.44 | -54.3% | Medical cost / regulatory pressure persists; FY2025 FCF is not a trough. |
| Base | 281,842 | 235,154 | 258.41 | -33.1% | Execution improves, but market already prices a large recovery. |
| Bull | 464,227 | 417,539 | 458.83 | +18.9% | TTM FCF is durable and WACC / growth assumptions improve. |

All values are USD millions except per-share values and percentages.

## Sensitivity Matrix

Base FCF path sensitivity, fair value per diluted share.

| WACC / Terminal Growth | 2.0% | 2.5% | 3.0% |
|---|---:|---:|---:|
| 8.0% | 290.35 | 315.46 | 345.59 |
| 9.0% | 240.86 | 258.41 | 278.89 |
| 10.0% | 203.76 | 216.59 | 231.26 |

## Sanity Checks

| Check | Result | Read |
|---|---:|---|
| Base terminal value share of EV | 74.6% | Within normal DCF-heavy range but still assumption-sensitive. |
| Bull terminal value share of EV | 79.9% | Bull case relies meaningfully on terminal assumptions. |
| Market EV / TTM FCF | 20.41x | Market price already assumes earnings / FCF repair. |
| TTM FCF yield on market cap | 5.61% | Reasonable, but not a deep value signal given legal/regulatory and medical cost risk. |
| Total debt / TTM FCF | 3.96x | Manageable for scale, but debt and regulated capital matter. |
| Net debt / TTM FCF | 2.37x | Better after cash/STI, but cash availability has regulatory and operating constraints. |

## What Would Change The Valuation

- Raise fair value if FY2026 actual FCF confirms TTM FCF is durable rather than Q1 working-capital aided.
- Raise fair value if MCR and operating cost ratio improve without sacrificing membership quality or future growth.
- Raise fair value if Optum Health margins recover and Optum Insight AI products show measurable revenue / margin traction.
- Lower fair value if H2 2026 earnings moderation is worse than management framed.
- Lower fair value if regulatory / legal actions impair PBM economics, Medicare Advantage economics, or capital return capacity.

## Missing / Unverified Data

| Item | Status | Why it matters |
|---|---|---|
| FY2026 full-year FCF guidance | ไม่พบข้อมูลที่ยืนยันได้ | DCF uses FY2025 FCF and TTM FCF scenarios rather than invented management FCF guidance. |
| Official full Q&A transcript | ไม่พบข้อมูลที่ยืนยันได้ | Could refine analyst pushback on MCR, Optum Health, and H2 cadence. |
| Segment-level FCF | not disclosed | Limits valuation of UnitedHealthcare vs Optum. |
| Regulatory / legal exposure quantification | partially disclosed | Material downside risk is hard to convert into a clean cash-flow adjustment. |
| Normalized insurance-capital treatment | not fully modeled | Simple FCF DCF may overstate usable cash because capital and reserves are business-critical. |
| End-of-day 2026-05-20 market data | not available during workflow | Intraday check should be refreshed before a trade decision. |

## Entity Update

Updated `wiki/entities/UNH.md` with valuation watch items, DCF range, fresh market data, and follow-up items.
