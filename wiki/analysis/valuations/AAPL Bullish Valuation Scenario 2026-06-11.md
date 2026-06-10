---
type: analysis
analysis_type: valuation-scenario
ticker: AAPL
company: Apple Inc.
date: 2026-06-11
currency: USD
source_files:
  - wiki/entities/AAPL.md
  - raw/financials/AAPL_fundamentals.md
  - raw/imports/AAPL_latest_results_source.md
  - raw/imports/AAPL_market_quote_2026-06-11.md
  - wiki/analysis/valuations/AAPL DCF Valuation 2026-06-11.md
tags:
  - analysis/valuation-scenario
  - analysis/dcf
  - ticker/AAPL
---

# AAPL Bullish Valuation Scenario - 2026-06-11

## Bottom Line

This memo answers: what happens if we intentionally use more bullish assumptions for Apple: lower WACC, higher terminal value, faster FCF growth, and explicit share-count reduction?

The answer is nuanced. A **Quality Bull** case with FCF reaching USD 220B in Year 5, WACC 7.5%, and terminal growth 3.0% gets to about **USD 290/share**, almost exactly the fresh market price of USD 292.38. To get clear upside, the model needs an **Aggressive Bull** case: FCF reaching USD 260B in Year 5, WACC 7.0%, terminal growth 3.5%, and/or a high exit multiple. That case produces about **USD 430/share**, or roughly **47% upside**, but terminal value is 87% of EV, so it is highly assumption-sensitive.

Practical read: bullish assumptions can justify AAPL, but they do not create a margin of safety unless one is comfortable underwriting very strong FCF growth and a premium terminal valuation from an already huge USD 129B TTM FCF base.

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| Base AAPL DCF | `wiki/analysis/valuations/AAPL DCF Valuation 2026-06-11.md` | Conservative/base DCF comparison. |
| Normalized facts | `raw/financials/AAPL_fundamentals.md` | TTM FCF, cash, debt, shares, and operating facts. |
| Entity page | `wiki/entities/AAPL.md` | Thesis, risks, business model, source gaps. |
| Market quote note | `raw/imports/AAPL_market_quote_2026-06-11.md` | Prior market quote and SEC-source balance sheet inputs. |
| StockAnalysis overview | https://stockanalysis.com/stocks/aapl/ | Fresh price check: USD 292.38 on 2026-06-10 1:08 PM EDT; market cap USD 4.29T; shares outstanding 14.69B. |
| StockAnalysis statistics | https://stockanalysis.com/stocks/aapl/statistics/ | Cross-check: market cap USD 4.29T, P/FCF 33.04x, EV/FCF 32.56x, TTM FCF USD 129.17B, WACC 10.02%. |
| SEC Q2 FY2026 Form 10-Q | https://www.sec.gov/Archives/edgar/data/320193/000032019326000013/aapl-20260328.htm | Official cash, debt, shares, and Q2 FY2026 operating facts. |

## Input Table

Amounts are USD billions unless noted.

| Input | Value | Source / Calculation |
|---|---:|---|
| Fresh market price | USD 292.38 | StockAnalysis overview, 2026-06-10 1:08 PM EDT. |
| Market capitalization | USD 4.29T | StockAnalysis overview/statistics. |
| TTM FCF anchor | 129.174 | Official-source calculation in `[[AAPL_fundamentals]]`. |
| Cash and marketable securities | 146.595 | SEC Q2 FY2026 Form 10-Q. |
| Total debt | 84.711 | SEC Q2 FY2026 Form 10-Q, calculated. |
| Net cash | 61.884 | 146.595 - 84.711. |
| Diluted shares used for DCF | 14.768B | SEC Q2 FY2026 Form 10-Q, 1H FY2026 weighted-average diluted shares. |
| Shares outstanding | 14.69B | StockAnalysis overview/statistics. |
| Shares change YoY | -2.39% | StockAnalysis statistics page. |
| Current P/FCF | 33.04x | StockAnalysis statistics page. |
| Current EV/FCF | 32.56x | StockAnalysis statistics page. |

## Bullish Assumption Set

| Lever | Base DCF | Quality Bull | Aggressive Bull | Dream Case |
|---|---:|---:|---:|---:|
| Year 5 FCF | 160 | 220 | 260 | 320 |
| FCF CAGR from TTM anchor | 4.4% | 11.2% | 15.0% | 19.9% |
| WACC | 9.0% | 7.5% | 7.0% | 6.5% |
| Terminal growth | 2.5% | 3.0% | 3.5% | 4.0% |
| Core story | Mature compounder | Strong Services + AI/device upgrade + buybacks | Sustained AI/device cycle, Services mix, and margin resilience | Near-perfect execution plus premium terminal assumptions |

These are assumptions, not Apple-disclosed guidance. The verified official source set still does not disclose forward FCF guidance, AI-specific monetization, or Apple Intelligence economics.

## FCF Projection

Amounts are USD billions.

| Year | Quality Bull FCF | Aggressive Bull FCF | Dream Case FCF |
|---:|---:|---:|---:|
| TTM anchor | 129.174 | 129.174 | 129.174 |
| Year 1 | 145 | 150 | 155 |
| Year 2 | 160 | 170 | 185 |
| Year 3 | 178 | 195 | 225 |
| Year 4 | 198 | 225 | 270 |
| Year 5 | 220 | 260 | 320 |

## Gordon DCF Re-Underwrite

Amounts are USD billions except per-share data.

| Scenario | WACC | Terminal Growth | PV of Explicit FCF | PV of Terminal Value | Enterprise Value | Net Cash | Equity Value | Fair Value / Diluted Share | Upside / Downside vs USD 292.38 | Terminal Value / EV |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Quality Bull | 7.5% | 3.0% | 718.125 | 3,507.560 | 4,225.685 | 61.884 | 4,287.569 | 290.33 | -0.7% | 83.0% |
| Aggressive Bull | 7.0% | 3.5% | 804.877 | 5,481.845 | 6,286.723 | 61.884 | 6,348.607 | 429.89 | 47.0% | 87.2% |
| Dream Case | 6.5% | 4.0% | 938.352 | 9,716.174 | 10,654.526 | 61.884 | 10,716.410 | 725.65 | 148.2% | 91.2% |

The Quality Bull case is the useful discipline check: even with lower WACC and stronger FCF growth, AAPL only looks roughly fairly valued. The Aggressive Bull case creates upside, but the terminal value concentration crosses the 85% warning zone. The Dream Case is useful only as an upper-bound imagination exercise, not as a decision anchor.

## Terminal Multiple Lens

This lens uses Year 5 FCF and a terminal EV/FCF multiple instead of Gordon terminal growth. WACC is 7.5% for discounting.

| Year 5 FCF / Exit EV-FCF | 24x | 28x | 32x | 36x |
|---:|---:|---:|---:|---:|
| 220 | 301.86 | 343.36 | 384.87 | 426.37 |
| 260 | 352.22 | 401.27 | 450.32 | 499.38 |
| 320 | 428.08 | 488.45 | 548.82 | 609.20 |

This is the cleanest way to make a bullish AAPL case: if Apple can reach USD 220B-260B FCF and still deserve 28x-32x EV/FCF in Year 5, current price can be reasonable to attractive. The caveat is that a 28x-32x terminal EV/FCF multiple for a mega-cap hardware-led ecosystem is a premium assumption.

## Buyback / Share-Count Reduction Lens

This section separates per-share compounding from enterprise value. A firm DCF should not double-count buybacks by both keeping all FCF in enterprise value and also dividing by a much lower future share count. Still, share reduction is useful for understanding how Apple could grow FCF per share.

| Annual Share Count Decline | Year 5 Shares | 5-Year Reduction | Year 5 FCF/share at USD 220B FCF | Year 5 FCF/share at USD 260B FCF | Year 5 FCF/share at USD 320B FCF |
|---:|---:|---:|---:|---:|---:|
| 2.0% | 13.349B | 9.6% | 16.48 | 19.48 | 23.97 |
| 2.4% | 13.079B | 11.4% | 16.82 | 19.88 | 24.47 |
| 3.0% | 12.682B | 14.1% | 17.35 | 20.50 | 25.23 |
| 3.5% | 12.358B | 16.3% | 17.80 | 21.04 | 25.89 |

At the fresh price of USD 292.38, if Apple reaches USD 260B FCF and share count falls 2.4% annually, Year 5 FCF/share would be about USD 19.88. The current price would equal about 14.7x that Year 5 FCF/share before discounting. That can be reasonable, but it assumes the FCF target and share retirement both happen.

## Sanity Checks

| Check | Result | Read |
|---|---:|---|
| Current P/FCF | 33.04x | Current valuation already prices quality and growth. |
| Quality Bull fair value | USD 290.33/share | Roughly equal to fresh price; this validates current price only if the bullish FCF path works. |
| Aggressive Bull fair value | USD 429.89/share | Upside appears, but terminal value is 87.2% of EV. |
| Dream Case fair value | USD 725.65/share | Terminal value is 91.2% of EV; not decision-grade without stronger evidence. |
| StockAnalysis WACC cross-check | 10.02% | Market-data provider WACC is above the 7.0%-7.5% bullish WACC used here. |
| Official guidance | Not verified | No official forward FCF or AI monetization guidance supports the aggressive path yet. |

## What Would Make The Bullish Case Decision-Grade

- Official results showing FCF tracking toward USD 180B-220B without margin deterioration.
- Services growth staying double digit with Services gross margin near or above current levels.
- iPhone / Mac / AI-device refresh cycle proving durable beyond one strong quarter.
- Apple disclosing AI or Apple Intelligence monetization that plausibly raises Services or hardware replacement economics.
- Buybacks continuing near a 2%-3% annual share-count reduction rate without requiring value-destructive repurchase prices.
- Tariff/component-cost pressure easing or being offset by pricing, mix, and supply-chain execution.

## Missing / Unverified Data

| Data item | Status | Handling |
|---|---|---|
| Official forward FCF guidance | Not disclosed | Bullish FCF path is an explicit investor assumption. |
| AI-specific revenue / Apple Intelligence monetization | Not disclosed | Cannot make the AI uplift source-backed yet. |
| Long-term buyback pace | Not committed | Apple authorized buybacks, but future price/pace are discretionary. |
| Terminal EV/FCF multiple in Year 5 | Assumption | Use as scenario lens, not company fact. |
| WACC below 8% | Assumption | Lower than StockAnalysis WACC cross-check and below the prior base case. |

## Entity Update

Updated `wiki/entities/AAPL.md` with a link to this bullish scenario. The action read does not automatically change to ADD; the bullish case says AAPL can be justified only with aggressive assumptions, not that the margin of safety is already clear.
