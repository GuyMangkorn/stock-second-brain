---
type: analysis
analysis_type: dcf-valuation
ticker: GOOGL
company: Alphabet Inc.
date: 2026-05-18
currency: USD
source_files:
  - wiki/entities/GOOGL.md
  - raw/financials/GOOGL_fundamentals.md
  - raw/imports/GOOGL_latest_results_source.md
tags:
  - analysis/dcf
  - ticker/GOOGL
---

# GOOGL DCF Valuation - 2026-05-18

## Bottom Line

This DCF can be run because the required inputs were freshly verified: current price, market cap, shares, cash, debt, free cash flow, and guidance. The result is a severe valuation warning.

Using Alphabet's company-reconciled TTM free cash flow of USD 64.429 billion, cash and marketable securities of USD 126.840 billion, total debt of USD 80.3 billion, diluted shares of 12.238 billion, a base WACC of 9.0%, terminal growth of 2.5%, and a five-year recovery path after the 2026-2027 capex step-up, base-case fair value is approximately USD 113 per diluted share.

Against the freshly checked GOOGL price of USD 404.15 on 2026-05-18 at 11:16 AM EDT, the base case implies about 72% downside. Even a bull case with Year 5 FCF reaching USD 190 billion produces fair value around USD 259 per share. The current price requires either much higher post-2027 FCF, a far lower discount rate, or terminal economics that exceed the mature-company framework used by this vault.

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| Entity page | `wiki/entities/GOOGL.md` | Business model, thesis, risks, source map. |
| Normalized facts | `raw/financials/GOOGL_fundamentals.md` | Q1 2026 financials, balance sheet, FCF, segments, ratios. |
| Latest source note | `raw/imports/GOOGL_latest_results_source.md` | Local extraction and ingest provenance. |
| SEC Q1 2026 Form 10-Q | https://www.sec.gov/Archives/edgar/data/1652044/000165204426000048/goog-20260331.htm | Official Q1 2026 financial statements, debt, backlog, MD&A. |
| Alphabet Q1 2026 earnings release | https://s206.q4cdn.com/479360582/files/doc_financials/2026/q1/2026q1-alphabet-earnings-release.pdf | Q1 2026 financial tables, FCF reconciliation, segment results. |
| Alphabet Q1 2026 transcript | https://s206.q4cdn.com/479360582/files/doc_events/2026/Apr/29/2026_Q1_Earnings_Transcript.pdf | Capex guidance and management commentary. |
| SEC FY2025 Form 10-K | https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/goog-20251231.htm | FY2025 annual baseline, segment history, OCF/capex context. |
| StockAnalysis GOOGL overview | https://stockanalysis.com/stocks/googl/ | Fresh price, market cap, shares, and valuation context checked 2026-05-18. |
| StockAnalysis GOOG statistics | https://stockanalysis.com/stocks/goog/statistics/ | Cross-check for total shares outstanding, enterprise value, and valuation ratios. |

## Input Table

All company financial statement amounts are USD billions unless noted.

| Input | Value | Source / Calculation |
|---|---:|---|
| Fresh market price used | USD 404.15 | StockAnalysis GOOGL overview, May 18, 2026, 11:16 AM EDT; checked 2026-05-18. |
| Fresh market capitalization | USD 4.90 trillion | StockAnalysis GOOGL overview, checked 2026-05-18. |
| Shares outstanding | 12.12 billion | StockAnalysis GOOGL overview/statistics; official 10-Q shows 12.116 billion Class A/B/C shares issued and outstanding at 2026-03-31. |
| Diluted shares used for DCF | 12.238 billion | Alphabet Q1 2026 diluted shares used in EPS calculation. |
| Cash and cash equivalents | 38.063 | Alphabet Q1 2026 earnings release and Form 10-Q. |
| Marketable securities | 88.777 | Alphabet Q1 2026 earnings release and Form 10-Q. |
| Cash + marketable securities | 126.840 | 38.063 + 88.777. |
| Long-term debt on balance sheet | 77.501 | Alphabet Q1 2026 earnings release and Form 10-Q. |
| Total debt used | 80.300 | Form 10-Q financing note: USD 79.1B senior notes + USD 1.2B credit facilities outstanding; no commercial paper. |
| Net cash used | 46.540 | 126.840 - 80.300. |
| Q1 2026 operating cash flow | 45.790 | Alphabet Q1 2026 earnings release and Form 10-Q. |
| Q1 2026 capex spend | 35.674 | Purchases of property and equipment, converted from cash outflow to positive spend. |
| Q1 2026 free cash flow | 10.116 | 45.790 - 35.674. |
| TTM operating cash flow | 174.353 | Alphabet Q1 2026 earnings release FCF reconciliation. |
| TTM capex spend | 109.924 | Alphabet Q1 2026 earnings release FCF reconciliation. |
| TTM free cash flow | 64.429 | 174.353 - 109.924. |
| FY2025 operating cash flow | 164.700 | Alphabet FY2025 Form 10-K MD&A rounded disclosure. |
| FY2025 capex | 91.400 | Alphabet FY2025 Form 10-K MD&A rounded disclosure. |
| FY2025 free cash flow | 73.300 | 164.700 - 91.400; rounded. |
| 2026 capex guidance | USD 180B to USD 190B | Alphabet Q1 2026 transcript. |
| 2027 capex guidance | Significantly higher than 2026 | Alphabet Q1 2026 transcript; no amount disclosed. |
| Revenue backlog | 467.6 | Alphabet Q1 2026 Form 10-Q. |
| Google Cloud backlog | 462.3 | Alphabet Q1 2026 Form 10-Q. |

## Base Case Assumptions

| Assumption | Bear | Base | Bull |
|---|---:|---:|---:|
| Starting reference | TTM FCF USD 64.429B | TTM FCF USD 64.429B | TTM FCF USD 64.429B |
| Year 1 FCF | 30.0 | 42.0 | 60.0 |
| Year 2 FCF | 35.0 | 50.0 | 85.0 |
| Year 3 FCF | 45.0 | 65.0 | 115.0 |
| Year 4 FCF | 58.0 | 85.0 | 150.0 |
| Year 5 FCF | 72.0 | 105.0 | 190.0 |
| WACC | 10.0% | 9.0% | 8.0% |
| Terminal growth | 2.0% | 2.5% | 3.0% |
| Interpretation | Capex keeps suppressing FCF and AI/cloud economics do not scale fast enough. | 2026-2027 are FCF trough/transition years, followed by recovery as cloud backlog and AI demand monetize. | AI infrastructure earns strong returns, cloud backlog converts, and FCF rises far above the pre-capex-cycle base. |

WACC basis: Alphabet is economically a Communication Services / internet platform with major cloud and AI infrastructure exposure. The vault reference range for Communication Services is 8%-10%. Base WACC is 9.0% because the company has a strong balance sheet and market leadership, but also faces high capex intensity, regulatory risk, AI search disruption risk, and uncertain AI unit economics.

Terminal growth basis: 2.0%-3.0% matches the mature developed-market compounder range in `wiki/reference/valuation-assumptions.md`. This model does not use a terminal growth rate above 3.0% in the main cases.

## FCF Projection

Amounts are USD billions.

| Year | Bear FCF | Base FCF | Bull FCF |
|---:|---:|---:|---:|
| TTM anchor | 64.429 | 64.429 | 64.429 |
| Year 1 | 30.000 | 42.000 | 60.000 |
| Year 2 | 35.000 | 50.000 | 85.000 |
| Year 3 | 45.000 | 65.000 | 115.000 |
| Year 4 | 58.000 | 85.000 | 150.000 |
| Year 5 | 72.000 | 105.000 | 190.000 |

Base case rationale: Q1 2026 FCF was only USD 10.116 billion and management guided 2026 capex to USD 180 billion to USD 190 billion, with 2027 expected to increase significantly. The base case therefore does not extrapolate FY2025 FCF directly. It assumes a trough and recovery, not a collapse.

## Valuation Summary

Amounts are USD billions except per-share data.

| Scenario | WACC | Terminal Growth | PV of Explicit FCF | PV of Terminal Value | Enterprise Value | Net Cash | Equity Value | Fair Value / Diluted Share | Upside / Downside vs USD 404.15 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Bear | 10.0% | 2.0% | 174.329 | 570.006 | 744.334 | 46.540 | 790.874 | 64.62 | -84.0% |
| Base | 9.0% | 2.5% | 259.267 | 1,076.136 | 1,335.403 | 46.540 | 1,381.943 | 112.92 | -72.1% |
| Bull | 8.0% | 3.0% | 459.285 | 2,663.803 | 3,123.088 | 46.540 | 3,169.628 | 259.00 | -35.9% |

## Sensitivity Matrix

Base projection fair value per diluted share, USD.

| WACC / Terminal Growth | 2.0% | 2.5% | 3.0% |
|---:|---:|---:|---:|
| 8.0% | 125.32 | 134.31 | 145.79 |
| 9.0% | 105.95 | 112.92 | 121.43 |
| 10.0% | 91.73 | 97.25 | 103.79 |

## Sanity Checks

| Check | Result | Read |
|---|---:|---|
| Market cap / TTM FCF | 76.1x | USD 4.90T / USD 64.429B. This is extremely demanding for a period of heavy capex. |
| TTM FCF yield on market cap | 1.32% | USD 64.429B / USD 4.90T. |
| Approximate market EV / TTM FCF | 75.4x | Market cap minus net cash divided by TTM FCF. |
| Base DCF terminal value share of EV | 80.6% | High, but below the 85%-90% warning zone. |
| Bull DCF terminal value share of EV | 85.3% | In the warning zone; the bull case is highly terminal-value-sensitive. |
| Reverse DCF, base WACC/terminal growth | About 44.1% 5-year FCF CAGR required | Starting from TTM FCF of USD 64.429B, matching USD 404.15 requires an unusually steep FCF ramp. |
| Net income quality | Mixed | Q1 2026 net income includes USD 28.7B of after-tax equity-security gains, so headline EPS overstates recurring operating earnings. |
| Guidance cross-check | Negative for near-term FCF | 2026 capex guide of USD 180B-190B and 2027 capex expected to rise significantly pressure FCF assumptions. |

## What Would Change The Valuation

- A sharp improvement in FCF conversion while capex remains high.
- Official evidence that Google Cloud backlog converts into high-margin recurring revenue.
- AI Search and Gemini monetization that increases revenue without structurally lowering ad margins.
- Quantified 2027 capex guidance that is lower than the current qualitative warning implies.
- Disclosure of TPU hardware economics showing strong ROIC and attractive margins.
- A materially lower share price, because the current price leaves little room for ordinary execution risk.

## Missing / Unverified Data

| Data item | Status | Valuation impact |
|---|---|---|
| Product-level AI revenue and margins for AI Overviews, Gemini, Vertex AI, TPU sales, and AI infrastructure | Not disclosed | Cannot directly underwrite AI unit economics. |
| Exact TPU hardware sales economics and customer concentration | Not disclosed | Cannot know whether TPU sales are high-ROIC, margin-accretive, or mostly strategic capacity scale. |
| Quantified 2027 capex | Not disclosed | Major uncertainty because management said 2027 capex will significantly increase versus 2026. |
| FY2026 full-year cash flow | ไม่พบข้อมูลที่ยืนยันได้ | Q1 2026 and TTM are the freshest verified cash-flow facts. |
| Investor-specific tax basis and position sizing | Not provided | Affects trim/hold decision but not intrinsic value. |

## Entity Update

Updated `wiki/entities/GOOGL.md` with a valuation watch item and report link to `[[GOOGL DCF Valuation 2026-05-18]]`. The valuation changes the action read, not the fact that Alphabet remains a high-quality business.

