---
type: valuation
ticker: DELL
company: Dell Technologies Inc.
date: 2026-05-21
valuation_type: DCF
action_dependency: P13
price_checked: "2026-05-21"
tags:
  - analysis/valuation
  - ticker/DELL
---

# DELL DCF Valuation - 2026-05-21

## Bottom Line

Base-case DCF fair value is about **USD 209/share**, versus the fresh checked close price of **USD 242.93**. That implies roughly **14% downside** under the base case, so DELL does not show a source-backed margin of safety for new capital today.

Valuation nuance สำคัญมาก: Dell has DFS financing debt. Base case uses `core debt` for equity bridge because DFS debt funds customer financing assets and is not the same economic exposure as ordinary operating debt. A stricter total-debt bridge gives about **USD 188/share**, so the decision should stay conservative until FY2027 Q1 confirms cash conversion.

## Source Map

| Source | URL / Path | Used For |
|---|---|---|
| FY2026 Form 10-K | https://investors.delltechnologies.com/node/19326/html | Diluted shares, debt split, annual financials, segment context |
| FY2026 Q4 / full-year results release | https://investors.delltechnologies.com/news-releases/news-release-details/dell-technologies-delivers-fourth-quarter-and-full-year-fiscal-3 | FCF, cash, FY2027 guidance |
| Q4 FY2026 IR transcript | https://investors.delltechnologies.com/static-files/9e5d4126-0f17-4ceb-b26c-a2563b8bcbc9 | Management commentary on supply, pricing, margins, and no FCF guide |
| StockAnalysis DELL quote | https://stockanalysis.com/stocks/dell/ | Current price, market cap, shares out checked 2026-05-21 |
| Local fundamentals | `raw/financials/DELL_fundamentals.md` | Normalized source-backed facts |

## Input Table

| Input | Value | Source / Basis |
|---|---:|---|
| Current close price | 242.93 | StockAnalysis, at close 2026-05-20 4:00 PM EDT; checked 2026-05-21 |
| Pre-market price | 242.39 | StockAnalysis, 2026-05-21 6:52 AM EDT |
| Market cap | 157.80B | StockAnalysis provider value |
| Current shares out | 649.57M | StockAnalysis provider value |
| DCF share count | 684M | FY2026 weighted-average diluted shares from Form 10-K |
| FY2026 FCF | 8.555B | OCF 11.185B - capex / capitalized software 2.630B |
| Cash and equivalents | 11.528B | 2026-01-30 balance sheet |
| Core debt, principal | 17.018B | 2026-01-30 Form 10-K debt table |
| DFS related debt, principal | 14.646B | 2026-01-30 Form 10-K debt table |
| Total debt, principal | 31.763B | 2026-01-30 Form 10-K debt table |
| FY2027 revenue guidance midpoint | 140.0B | FY2026 results release |
| FY2027 AI server revenue guidance | Roughly 50.0B | FY2026 results release |
| FY2027 GAAP diluted EPS guidance midpoint | 11.52 | FY2026 results release |
| FY2027 non-GAAP diluted EPS guidance midpoint | 12.90 | FY2026 results release |

## Base Case Assumptions

| Assumption | Base Case | Rationale |
|---|---:|---|
| Year 1 FCF growth | 12.0% | Below FY2027 revenue guidance growth because AI server mix and working capital can dilute FCF conversion. |
| Year 2 FCF growth | 10.0% | Assumes backlog conversion continues but growth begins to fade. |
| Year 3 FCF growth | 8.0% | Fade toward mature hardware/infrastructure economics. |
| Year 4 FCF growth | 6.0% | Conservative fade. |
| Year 5 FCF growth | 4.0% | Approaches terminal profile. |
| WACC | 10.0% | Information Technology range with cyclical hardware, leverage, and AI component-cost risk. |
| Terminal growth | 2.5% | Mature developed-market terminal growth assumption. |
| Equity bridge | EV + cash - core debt | Uses core debt because DFS related debt is linked to customer financing assets; total-debt sensitivity is shown separately. |

## FCF Projection

| Year | Growth | Projected FCF | PV @ 10.0% |
|---:|---:|---:|---:|
| 1 | 12.0% | 9.58 | 8.71 |
| 2 | 10.0% | 10.54 | 8.71 |
| 3 | 8.0% | 11.38 | 8.55 |
| 4 | 6.0% | 12.07 | 8.24 |
| 5 | 4.0% | 12.55 | 7.79 |

All figures are USD billions except percentages.

## Valuation Summary

| Scenario | WACC | Terminal Growth | EV | Equity Value Using Core Debt | Fair Value / Share | Upside / Downside vs USD 242.93 |
|---|---:|---:|---:|---:|---:|---:|
| Bear | 11.0% | 2.0% | 103.6 | 98.1 | 143.43 | -41.0% |
| Base | 10.0% | 2.5% | 148.5 | 143.0 | 209.07 | -13.9% |
| Bull | 9.0% | 3.0% | 216.5 | 211.0 | 308.48 | 27.0% |

Equity bridge:

```text
Base EV = PV projected FCF 42.0 + PV terminal value 106.5 = 148.5
Base equity value = EV 148.5 + cash 11.528 - core debt 17.018 = 143.0
Base fair value / share = 143.0B / 684M = 209.07
```

Debt-treatment sensitivity:

| Equity Bridge | Fair Value / Share | Upside / Downside vs USD 242.93 | Note |
|---|---:|---:|---|
| Core debt | 209.07 | -13.9% | Base case; treats DFS debt separately because it funds financing receivables. |
| Total debt principal | 187.52 | -22.8% | Stricter view; may understate value if DFS assets are not separately credited. |

## Sensitivity Matrix

Fair value per share, USD, using base FCF growth path and core debt bridge.

| Terminal Growth / WACC | 9.0% | 10.0% | 11.0% |
|---|---:|---:|---:|
| 2.0% | 228.81 | 198.63 | 175.17 |
| 2.5% | 243.09 | 209.07 | 183.06 |
| 3.0% | 259.75 | 221.00 | 191.95 |

## Sanity Checks

- Base-case terminal value is a large part of EV, so the DCF is assumption-sensitive.
- Market cap / FY2026 FCF is about 18.4x, while the base DCF implies roughly 17.4x FY2026 FCF enterprise value. ราคาใกล้ bullish assumptions มากกว่า base assumptions.
- FY2027 guidance is very strong, but guidance is revenue/EPS-heavy; FY2027 FCF is not disclosed.
- Negative book equity and high reported total debt make balance sheet interpretation noisy; DFS financing assets and obligations should not be ignored.
- If FY2027 Q1 shows stronger FCF conversion and margin protection, base FCF growth may be too low. If AI server margins stay pressured, it may still be too high.

## What Would Change The Valuation

- Positive: FY2027 Q1 shows OCF/FCF conversion close to FY2026 run-rate despite AI revenue ramp.
- Positive: management discloses or implies higher AI server attach in storage, networking, services, or support.
- Positive: gross margin stabilizes despite memory / component inflation.
- Negative: backlog converts into revenue but not FCF.
- Negative: working capital absorbs cash as AI shipments scale.
- Negative: FY2027 guidance is narrowed down or margins miss.

## Missing / Unverified Data

- FY2027 free cash flow guidance is not disclosed.
- FY2027 Q1 actual results are not yet available as of 2026-05-21.
- Segment-level FCF is not disclosed.
- Product-level AI server margin and customer concentration are not disclosed.
- Exact post-quarter diluted share count is not disclosed in the same way as FY2026 weighted-average diluted shares; market provider current shares out differs from FY2026 weighted-average diluted shares.
- DFS debt requires judgment in equity bridge.

## Entity Update

Updated `wiki/entities/DELL.md` with valuation watch items and a WAIT / AVOID-new-capital read at current price.
