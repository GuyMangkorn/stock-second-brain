---
type: valuation
ticker: CVS
valuation_date: 2026-07-11
method: consolidated FCF DCF scenario with earnings cross-check
stage_gate: calculation-ready-high-sensitivity
currency: USD
market_price: 102.83
market_price_date: 2026-07-09
entity: "[[CVS]]"
source_files:
  - raw/financials/CVS_fundamentals.md
  - raw/imports/CVS_latest_results_source.md
  - raw/imports/CVS_market_quote_2026-07-11.md
tags: [valuation/dcf, ticker/CVS]
---

# CVS DCF Valuation - 2026-07-11

## Bottom Line

P11 ผ่าน stage gate แบบ `calculation-ready-high-sensitivity`. CVS มี verified FCF history, cash, debt และ shares เพียงพอสำหรับ scenario DCF แต่ consolidated business รวม regulated insurer จึงไม่ควรอ่านผลเป็น precise target. Base fair value ประมาณ **USD 76.47/share** เทียบ latest verified close **USD 102.83**, หรือ downside ราว **25.6%**. Bull case อยู่ USD 142.85 แต่ต้องได้ Aetna recovery ที่ยั่งยืนพร้อม FCF growth 12% ต่อปี, WACC 8.0% และ terminal growth 3.0%. ราคาปัจจุบันจึงไม่มี base-case margin of safety ก่อนเห็น Q2.

## Market Data Check

| Item | Value | Source / calculation |
|---|---:|---|
| Latest verified close | USD 102.83 on 2026-07-09 | [[CVS_market_quote_2026-07-11]] |
| Common shares outstanding | 1.273bn | Q1 2026 10-Q |
| Calculated market cap | USD 130.90bn | 102.83 × 1.273bn |
| Market-data limitation | 2026-07-10 close not verified | Refresh before execution |

## Inputs And Treatment

| Input | Value | Provenance / treatment |
|---|---:|---|
| FY2025 FCF | USD 7.807bn | OCF 10.639 less capex 2.832 |
| FY2024 / FY2023 FCF | USD 6.326bn / 10.395bn | FY2025 10-K; shown calculation |
| Q1 2026 FCF | USD 3.400bn | OCF 4.249 less capex 0.849; not annualized |
| Base starting FCF | USD 7.000bn | Analyst assumption below FY2025; reflects FY2026 OCF guide at least 9.5bn and unknown capex |
| Cash | USD 9.542bn | Q1 2026 10-Q |
| Debt | USD 63.111bn | Current 2.580 + long-term 60.531 |
| Net debt | USD 53.569bn | Debt less cash; insurance investments excluded |
| Diluted shares | 1.279bn | Q1 2026 diluted weighted-average shares |

## Assumptions

| Scenario | Starting FCF | Annual growth, Years 1-5 | WACC | Terminal growth | Interpretation |
|---|---:|---:|---:|---:|---|
| Bear | 6.100 | 3% | 9.5% | 1.5% | OCF guide floor less annualized Q1 capex; medical/reimbursement pressure persists |
| Base | 7.000 | 8% | 8.5% | 2.5% | Aetna recovery and moderate enterprise FCF normalization |
| Bull | 7.800 | 12% | 8.0% | 3.0% | Strong, durable insurance recovery plus PBM/retail stabilization |

All forecast inputs are analyst assumptions. WACC begins within the Health Care 8%-10% reference range. Base 8.5% reflects scale and recurring health demand but retains leverage, regulatory, reserve, and execution risk. Starting FCF is deliberately below FY2025 because FY2026 OCF guidance is at least USD 9.5bn and full-year capex is not guided.

## Base Projection

| Year | Projected FCF | PV at 8.5% |
|---:|---:|---:|
| 1 | 7.560 | 6.968 |
| 2 | 8.165 | 6.936 |
| 3 | 8.818 | 6.906 |
| 4 | 9.523 | 6.874 |
| 5 | 10.285 | 6.843 |
| Explicit forecast PV | — | 34.527 |
| Terminal value | 175.700 | 116.843 PV |

`FCF = OCF - capex`; `EV = PV(explicit FCF) + PV(terminal value)`; `Equity value = EV + cash - debt`; `Fair value/share = Equity value / diluted shares`.

## Valuation Summary

| Scenario | Enterprise value | Equity value | Fair value/share | Upside / (downside) vs 102.83 | Terminal value / EV |
|---|---:|---:|---:|---:|---:|
| Bear | 82.47 | 28.90 | 22.60 | (78.0%) | 69.1% |
| Base | 151.37 | 97.80 | 76.47 | (25.6%) | 77.2% |
| Bull | 236.28 | 182.71 | 142.85 | 38.9% | 81.6% |

USD billions except per-share data. Terminal value remains below 85% of EV but dominates every scenario, making the result highly assumption-sensitive.

## Sensitivity: Base Fair Value / Share

Base starting FCF USD 7.0bn and 8% growth are held constant.

| Terminal growth \ WACC | 8.0% | 8.5% | 9.0% |
|---:|---:|---:|---:|
| 2.0% | 78.52 | 69.03 | 60.90 |
| 2.5% | 87.48 | 76.47 | 67.16 |
| 3.0% | 98.23 | 85.26 | 74.46 |

## Sanity Checks

- Latest price / FY2026 adjusted EPS guidance midpoint is approximately **13.9x**; price / GAAP EPS midpoint is approximately **16.2x**.
- FY2025 FCF yield on calculated market cap is approximately **6.0%**. This looks less demanding than DCF because DCF explicitly subtracts USD 53.6bn net debt.
- The latest price sits above every base sensitivity cell and only becomes attractive under the bull growth/cost-of-capital combination.
- Q1 FCF was USD 3.4bn, but seasonality and working-capital timing make annualization unsafe.

## Valuation-Specific Limitations

- CVS includes an insurer: investments support policy liabilities and cannot simply be added as excess cash; corporate debt and regulatory capital are not allocated by segment.
- FY2026 capex/FCF guidance is absent, making the starting FCF an explicit assumption.
- A decision-grade SOTP needs normalized segment earnings, insurance capital, and sourced peer multiples.
- Latest verified close is one session stale and cannot authorize execution.

## Change Triggers

- Re-run after Q2 with OCF, capex, MBR, prior-year development, membership, and guidance.
- Upgrade if base value approaches market price through durable FCF rather than lower WACC alone.
- Downgrade if medical trend worsens, PBM/retail profit erosion continues, or leverage rises.

## Sources

- [[CVS_latest_results_source]]
- [[CVS_fundamentals]]
- [[CVS_market_quote_2026-07-11]]
- [SEC Q1 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/64803/000006480326000052/cvs-20260331.htm)
- [Official Q1 2026 release](https://investors.cvshealth.com/news/news-details/2026/CVS-HEALTH-CORPORATION-REPORTS-STRONG-FIRST-QUARTER-2026-RESULTS-AND-RAISES-FULL-YEAR-2026-GUIDANCE/default.aspx)
