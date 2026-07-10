---
type: analysis
analysis_type: dcf-valuation
ticker: CSCO
company: Cisco Systems, Inc.
date: 2026-05-20
currency: USD
source_files:
  - wiki/entities/CSCO.md
  - raw/financials/CSCO_fundamentals.md
  - raw/imports/CSCO_latest_results_source.md
tags:
  - analysis/dcf
  - ticker/CSCO
---

# CSCO DCF Valuation - 2026-05-20
Entity: [[CSCO]]

## Bottom Line

DCF can be run because the required inputs were freshly checked or source-backed: current accessible price, market cap, shares, cash/investments, debt, FCF, and guidance. The main caveat is that the latest accessible market price was the 2026-05-18 close from a market-data source; Yahoo cross-check was delayed to 2026-05-15. Future action calls should refresh the quote again.

Using TTM FCF of USD 11.788B, cash plus investments of USD 16.640B, total debt of USD 31.303B, diluted shares of 3.987B, base WACC of 9.0%, terminal growth of 2.5%, and a five-year FCF growth path fading from 5.0% to 3.5%, base-case fair value is approximately USD 47.02 per diluted share.

Against the latest accessible price of USD 118.88, the base case implies about 60% downside. CSCO เป็น quality cash-generative franchise และ AI networking momentum จริง แต่ current price ต้องการ sustained AI-led FCF acceleration หรือ valuation multiple ที่สูงมากต่อเนื่อง จึงยังไม่มี margin of safety สำหรับ new capital.

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| Entity page | `wiki/entities/CSCO.md` | Business model, source map, thesis, risks. |
| Normalized facts | `raw/financials/CSCO_fundamentals.md` | Q3 FY2026 financials, balance sheet, FCF, shares, segment data, and guidance. |
| Latest source note | `raw/imports/CSCO_latest_results_source.md` | Local source extraction and ingest provenance. |
| SEC Form 8-K | https://www.sec.gov/Archives/edgar/data/858877/000085887726000075/csco-20260513.htm | Official Q3 FY2026 result filing reference. |
| Cisco Q3 FY2026 earnings release | https://investor.cisco.com/news/news-details/2026/CISCO-REPORTS-THIRD-QUARTER-EARNINGS/default.aspx | Official Q3 FY2026 tables, cash/debt, cash flow, segment data, and guidance. |
| Cisco FY2025 Form 10-K | https://www.sec.gov/Archives/edgar/data/858877/000085887725000111/csco-20250726.htm | FY2025/FY2024/FY2023 FCF baseline. |
| FinanceCharts CSCO market cap history | https://www.financecharts.com/stocks/CSCO/summary/market-cap | Latest accessible price and market cap; checked 2026-05-20. |
| Yahoo Finance CSCO quote | https://finance.yahoo.com/quote/CSCO/ | Cross-check for delayed quote and market cap; checked 2026-05-20. |

## Input Table

All company financial statement amounts are USD billions unless noted.

| Input | Value | Source / Calculation |
|---|---:|---|
| Latest accessible market price used | USD 118.88 | FinanceCharts market-cap history, 2026-05-18 close; checked 2026-05-20. |
| Market cap | USD 469.603B | FinanceCharts market-cap history. |
| Yahoo quote cross-check | USD 118.21 close / USD 117.83 after hours | Yahoo Finance, 2026-05-15 delayed quote; checked 2026-05-20. |
| Yahoo market cap cross-check | USD 466.917B | Yahoo Finance. |
| Diluted shares used for DCF | 3.987B | Cisco Q3 FY2026 release, 9M FY2026 diluted shares. |
| Market-data shares outstanding | 3.95B | FinanceCharts market-cap history. |
| Cash and cash equivalents | 7.083 | Cisco Q3 FY2026 release. |
| Investments | 9.557 | Cisco Q3 FY2026 release. |
| Cash plus investments | 16.640 | 7.083 + 9.557. |
| Short-term debt | 11.932 | Cisco Q3 FY2026 release. |
| Long-term debt | 19.371 | Cisco Q3 FY2026 release. |
| Total debt | 31.303 | 11.932 + 19.371. |
| Net debt using cash plus investments | 14.663 | 31.303 - 16.640. |
| Q3 FY2026 operating cash flow | 3.757 | Cisco Q3 FY2026 release. |
| Q3 FY2026 capex spend | 0.414 | Cisco Q3 FY2026 release; PP&E acquisition converted to positive spend. |
| Q3 FY2026 FCF | 3.343 | 3.757 - 0.414. |
| 9M FY2026 FCF | 7.771 | 8.791 - 1.020. |
| FY2025 FCF | 13.288 | Cisco FY2025 Form 10-K. |
| 9M FY2025 FCF | 9.271 | Cisco Q3 FY2026 release calculation. |
| TTM FCF | 11.788 | 13.288 - 9.271 + 7.771. |
| FY2026 revenue guidance | 62.8 to 63.0 | Cisco Q3 FY2026 release. |
| FY2026 GAAP EPS guidance | 3.16 to 3.21 | Cisco Q3 FY2026 release. |
| FY2026 non-GAAP EPS guidance | 4.27 to 4.29 | Cisco Q3 FY2026 release. |
| FY2026 AI infrastructure orders outlook | about 9.0 | Cisco Q3 FY2026 release. |

## Base Case Assumptions

| Assumption | Bear | Base | Bull |
|---|---:|---:|---:|
| Year 1 FCF anchor | 11.788 | 11.788 | 11.788 |
| Year 1 FCF growth | 0.0% | 5.0% | 8.0% |
| Year 2 FCF growth | 1.0% | 5.0% | 7.5% |
| Year 3 FCF growth | 1.0% | 4.5% | 7.0% |
| Year 4 FCF growth | 1.5% | 4.0% | 6.0% |
| Year 5 FCF growth | 1.5% | 3.5% | 5.0% |
| WACC | 10.5% | 9.0% | 8.0% |
| Terminal growth | 2.0% | 2.5% | 3.0% |

WACC basis: Information Technology range in `wiki/reference/valuation-assumptions.md` is 8%-12%. Base WACC is 9.0% because Cisco is a large, cash-generative market leader with recurring services/subscription revenue, but AI hardware cyclicality, competitive pressure, Security/Splunk execution, and current valuation risk argue against using the low end.

Terminal growth basis: 2.5% is inside the mature developed-market compounder range. Bull case 3.0% requires AI infrastructure demand to become durable FCF growth rather than only order/revenue growth.

## FCF Projection

Base case amounts are USD billions.

| Year | FCF | Growth |
|---:|---:|---:|
| Year 1 | 12.377 | 5.0% |
| Year 2 | 12.996 | 5.0% |
| Year 3 | 13.581 | 4.5% |
| Year 4 | 14.124 | 4.0% |
| Year 5 | 14.619 | 3.5% |

Base rationale: use source-backed TTM FCF, then fade from mid-single-digit FCF growth. This gives Cisco credit for AI infrastructure and networking momentum, but does not assume revenue guidance converts one-for-one into FCF because capex, component costs, mix, and working capital can pressure cash flow.

## Valuation Summary

Amounts are USD billions except per-share data.

| Scenario | WACC | Terminal Growth | Enterprise Value | Cash + Investments | Total Debt | Equity Value | Fair Value / Diluted Share | Upside / Downside vs USD 118.88 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Bear | 10.5% | 2.0% | 135.3 | 16.6 | (31.3) | 120.6 | 30.25 | -74.6% |
| Base | 9.0% | 2.5% | 202.1 | 16.6 | (31.3) | 187.5 | 47.02 | -60.4% |
| Bull | 8.0% | 3.0% | 286.2 | 16.6 | (31.3) | 271.5 | 68.09 | -42.7% |

## Sensitivity Matrix

Base projection fair value per diluted share, USD.

| WACC / Terminal Growth | 2.0% | 2.5% | 3.0% |
|---:|---:|---:|---:|
| 8.0% | 52.22 | 56.30 | 61.20 |
| 9.0% | 44.16 | 47.02 | 50.35 |
| 10.0% | 38.12 | 40.21 | 42.59 |

## Sanity Checks

| Check | Result | Read |
|---|---:|---|
| TTM FCF yield on market cap | 2.51% | Expensive for a mature cash-flow company unless AI-led FCF growth accelerates materially. |
| Market EV / TTM FCF | 41.08x | Very high versus a DCF anchored on actual trailing FCF. |
| Net debt / TTM FCF | 1.24x | Balance sheet is manageable; valuation, not solvency, is the key issue. |
| Base terminal value share of EV | 74.1% | High but below the 85%-90% warning zone. |
| Forward GAAP P/E | about 37.3x | Market is capitalizing a strong growth narrative. |
| Forward non-GAAP P/E | about 27.8x | More reasonable than GAAP P/E, but still not cheap for a mature hardware/software mix. |

## What Would Change The Valuation

- FY2026 and FY2027 FCF materially exceed the TTM FCF anchor.
- AI infrastructure orders convert into high-margin revenue and repeatable FCF.
- Networking order growth remains broad-based excluding hyperscalers.
- Security/Splunk returns to durable growth without heavy margin dilution.
- Current price falls substantially while guidance and FCF quality remain intact.
- Cisco discloses enough AI customer concentration and margin data to reduce order-quality uncertainty.

## Missing / Unverified Data

| Data item | Status | Valuation impact |
|---|---|---|
| Q3 FY2026 Form 10-Q | ไม่พบข้อมูลที่ยืนยันได้ | Official release is sufficient for core P11 inputs, but full filing would improve risk and balance-sheet detail. |
| FY2026 FCF guidance | ไม่พบข้อมูลที่ยืนยันได้ | DCF uses TTM FCF instead of an invented FY2026 FCF forecast. |
| Market quote after 2026-05-18 close | ไม่พบข้อมูลที่ยืนยันได้ | Current action read should be refreshed before future trade decisions. |
| Product-category operating profit | not disclosed | Limits segment-specific valuation. |
| Hyperscaler AI customer concentration / margin | not disclosed | Key uncertainty for AI order quality. |
| Official full Q&A transcript | not normalized | Could refine management-confidence and analyst-pushback reads. |
| Investor-specific required return | not provided | Could change whether an existing position should be held or trimmed. |

## Entity Update

Updated `wiki/entities/CSCO.md` with this valuation memo link and valuation watch items. The valuation pushes the action read toward AVOID / WAIT for new capital at current price and REVIEW / TRIM only if an existing position is overweight.
