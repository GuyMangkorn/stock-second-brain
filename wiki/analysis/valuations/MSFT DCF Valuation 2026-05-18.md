---
type: analysis
analysis_type: dcf-valuation
ticker: MSFT
company: Microsoft Corporation
date: 2026-05-18
currency: USD
source_files:
  - wiki/entities/MSFT.md
  - raw/financials/MSFT_fundamentals.md
tags:
  - analysis/dcf
  - ticker/MSFT
---

# MSFT DCF Valuation - 2026-05-18
Entity: [[MSFT]]

## Bottom Line

This DCF is source-backed but intentionally conservative about terminal economics because Microsoft's current AI buildout has made free cash flow more capital-intensive. Using TTM free cash flow of USD 72.916 billion, a base WACC of 8.5%, terminal growth of 2.5%, and a five-year FCF recovery path, the base-case fair value is approximately USD 206 per diluted share.

Against the freshly checked latest available market close of USD 421.92 on 2026-05-15, the base case implies about 51% downside. The bull case reaches roughly USD 309 per share, still below market, which means the current price requires either materially faster sustained FCF growth, a lower discount rate, a higher terminal growth assumption, or confidence that AI capex will convert into much larger post-forecast cash flows.

This is not a thesis downgrade by itself. It is a valuation warning: Microsoft remains an unusually high-quality compounder, but the stock price embeds an aggressive free-cash-flow conversion story.

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| Existing entity page | `wiki/entities/MSFT.md` | Business model, thesis, risks, FY26 Q3 context, existing source map. |
| Existing normalized facts | `raw/financials/MSFT_fundamentals.md` | FY2025 annual baseline, FY26 Q3 / 9M FY26 financial facts, cash flow, balance sheet, shares. |
| Microsoft FY26 Q3 income statements | https://www.microsoft.com/en-us/Investor/earnings/FY-2026-Q3/income-statements | Revenue, operating income, net income, diluted EPS, weighted average diluted shares. |
| Microsoft FY26 Q3 cash flows | https://www.microsoft.com/en-us/investor/earnings/fy-2026-q3/cash-flows | Operating cash flow, capex spend, Q3 and 9M FCF calculation inputs. |
| Microsoft FY26 Q3 balance sheets | https://www.microsoft.com/en-us/investor/earnings/fy-2026-q3/balance-sheets | Cash, short-term investments, current debt, long-term debt, outstanding shares. |
| Microsoft FY26 Q3 earnings transcript | https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q3 | Q4 guidance, capex guidance, Azure/Microsoft Cloud commentary, FY27 outlook. |
| Microsoft FY2025 annual cash flow tables | https://www.microsoft.com/en-us/Investor/earnings/FY-2025-Q4/cash-flows | FY2025 operating cash flow and additions to property and equipment. |
| StockAnalysis MSFT overview/statistics | https://stockanalysis.com/stocks/msft/ and https://stockanalysis.com/stocks/msft/statistics/ | Fresh market price cross-check, market cap, shares out, current valuation ratios. |
| Yahoo Finance MSFT quote | https://finance.yahoo.com/quote/MSFT/ | Fresh market price and market cap cross-check. |

## Input Table

All company financial statement amounts are USD millions unless noted.

| Input | Value | Source / Calculation |
|---|---:|---|
| Fresh market price used | USD 421.92 | StockAnalysis and Yahoo Finance, latest available close, 2026-05-15 4:00 PM EDT; checked 2026-05-18 Asia/Bangkok. |
| Fresh market capitalization | USD 3.134 trillion | Yahoo Finance quote and StockAnalysis market data, checked 2026-05-18. |
| Current share class / shares outstanding | 7.43 billion | StockAnalysis statistics; Microsoft balance sheet also shows 7.429 billion outstanding at 2026-03-31. |
| Diluted shares used for DCF | 7.445 billion | Microsoft FY26 Q3 weighted average diluted shares. Conservative per-share denominator. |
| Cash and cash equivalents | 32,105 | Microsoft FY26 Q3 balance sheets, 2026-03-31. |
| Short-term investments | 46,167 | Microsoft FY26 Q3 balance sheets, 2026-03-31. |
| Cash + short-term investments | 78,272 | 32,105 + 46,167. |
| Current portion of long-term debt | 8,839 | Microsoft FY26 Q3 balance sheets, 2026-03-31. |
| Long-term debt | 31,423 | Microsoft FY26 Q3 balance sheets, 2026-03-31. |
| Total debt used | 40,262 | 8,839 + 31,423. Operating lease liabilities are not included in base debt but are noted in caveats. |
| Net cash used | 38,010 | 78,272 - 40,262. |
| FY2025 operating cash flow | 136,162 | Microsoft FY2025 cash flow table. |
| FY2025 capex spend | 64,551 | Microsoft FY2025 additions to property and equipment, converted from cash outflow to positive spend. |
| FY2025 free cash flow | 71,611 | 136,162 - 64,551. |
| 9M FY25 free cash flow | 46,043 | Microsoft FY26 Q3 cash flow table: 93,515 - 47,472. |
| 9M FY26 free cash flow | 47,348 | Microsoft FY26 Q3 cash flow table: 127,494 - 80,146. |
| TTM free cash flow | 72,916 | FY2025 FCF 71,611 - 9M FY25 FCF 46,043 + 9M FY26 FCF 47,348. |
| Q4 FY26 revenue guidance | USD 86.7B to USD 87.8B | Microsoft FY26 Q3 transcript. |
| Q4 FY26 capex guidance | More than USD 40B | Microsoft FY26 Q3 transcript; includes higher component pricing and finance lease variability. |
| Calendar 2026 capex expectation | Roughly USD 190B | Microsoft FY26 Q3 transcript; includes about USD 25B from higher component pricing. |
| FY27 growth guidance | Double-digit revenue and operating income growth | Microsoft FY26 Q3 transcript; forward-looking guidance, not a reported result. |

## Base / Bull / Bear Assumptions

| Assumption | Bear | Base | Bull |
|---|---:|---:|---:|
| Starting FCF anchor | TTM FCF of USD 72.916B | TTM FCF of USD 72.916B | TTM FCF of USD 72.916B |
| Year 1 FCF growth | -8% | +3% | +8% |
| Year 2 FCF growth | +3% | +8% | +12% |
| Year 3 FCF growth | +5% | +9% | +12% |
| Year 4 FCF growth | +5% | +8% | +10% |
| Year 5 FCF growth | +4% | +6% | +8% |
| WACC | 9.5% | 8.5% | 7.5% |
| Terminal growth | 2.0% | 2.5% | 3.0% |
| Business interpretation | AI capex remains heavy, Microsoft Cloud margin compression persists, FCF conversion lags revenue growth. | AI capex stays elevated near term, but Azure/Copilot/GitHub/Dynamics monetization gradually restores FCF growth. | Capacity converts well, AI usage-based pricing scales, unit economics improve, and FCF growth compounds above revenue for several years. |

WACC basis: Microsoft is classified economically as a large-cap Information Technology / cloud software platform. The vault's reference range for Information Technology is 8%-12%. The base WACC is set at 8.5% after subtracting for market leadership, recurring revenue, investment-grade balance sheet, and net cash, while adding back risk for unusually high AI capex intensity, finance lease exposure, and the uncertainty of long-run AI workload economics.

Terminal growth basis: 2.0%-3.0% matches the mature developed-market compounder range in `wiki/reference/valuation-assumptions.md`. This model does not use a terminal growth rate above 3.0% in the main cases because Microsoft is already a very large business and the terminal period should not assume indefinite hypergrowth.

## FCF Projection

Amounts are USD millions.

| Year | Bear FCF | Base FCF | Bull FCF |
|---:|---:|---:|---:|
| TTM anchor | 72,916 | 72,916 | 72,916 |
| Year 1 | 67,083 | 75,104 | 78,749 |
| Year 2 | 69,095 | 81,112 | 88,199 |
| Year 3 | 72,550 | 88,412 | 98,783 |
| Year 4 | 76,178 | 95,485 | 108,661 |
| Year 5 | 79,225 | 101,214 | 117,354 |

Base case rationale: FY26 Q4 and calendar 2026 capex guidance argue against simply capitalizing operating income growth into near-term FCF. At the same time, management's Q4 revenue guide, Azure growth guide, and FY27 double-digit revenue and operating income outlook support positive FCF growth once the model moves beyond the most acute buildout period.

## Valuation Summary

Amounts are USD millions except per-share data.

| Scenario | WACC | Terminal Growth | PV of Explicit FCF | PV of Terminal Value | Enterprise Value | Net Cash | Equity Value | Fair Value / Diluted Share | Upside / Downside vs USD 421.92 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Bear | 9.5% | 2.0% | 275,807 | 686,082 | 961,889 | 38,010 | 999,899 | 134.30 | -68.2% |
| Base | 8.5% | 2.5% | 343,031 | 1,150,431 | 1,493,462 | 38,010 | 1,531,472 | 205.70 | -51.2% |
| Bull | 7.5% | 3.0% | 390,474 | 1,872,762 | 2,263,236 | 38,010 | 2,301,246 | 309.10 | -26.7% |

## Sensitivity Matrix

Base projection fair value per diluted share, USD.

| WACC / Terminal Growth | 2.0% | 2.5% | 3.0% |
|---:|---:|---:|---:|
| 7.5% | 228.17 | 246.68 | 269.30 |
| 8.5% | 193.13 | 205.70 | 220.57 |
| 9.5% | 167.45 | 176.46 | 186.85 |

## Sanity Checks

| Check | Result | Read |
|---|---:|---|
| TTM FCF yield on market cap | 2.3% | USD 72.916B / USD 3.134T. The market is paying a low current FCF yield because it expects growth and/or future FCF conversion. |
| Approximate market EV / TTM FCF | 42.5x | Uses market equity value from USD 421.92 close and net cash of USD 38.010B. This is demanding for a capex-heavy phase. |
| Base DCF terminal value share of EV | 77.0% | High but below the 85%-90% warning threshold. The model still depends heavily on terminal assumptions. |
| Bull DCF terminal value share of EV | 82.7% | Still below 85%, but near the upper end of the normal comfort zone. |
| Reverse DCF, base WACC/terminal growth | About 25.1% 5-year FCF CAGR required | At 8.5% WACC and 2.5% terminal growth, matching USD 421.92 requires Year 5 FCF of roughly USD 223B, far above the base Year 5 FCF of USD 101B. |
| Implied terminal growth if base FCF projection is used | About 5.9% | Holding the base FCF projection and 8.5% WACC, the current price implies terminal growth well above the mature-company range. |
| Management guidance cross-check | Mixed | FY27 double-digit revenue and operating income growth supports the bull story, but calendar 2026 capex near USD 190B and Q4 capex over USD 40B directly pressure FCF. |

## What Would Change The Valuation

- Higher near-term FCF conversion: if operating cash flow growth outruns capex faster than modeled, Year 1-Year 3 FCF can move materially higher.
- Clearer AI unit economics: disclosure that Copilot, GitHub Copilot, Security Copilot, Dynamics agents, and Azure AI workloads are strongly FCF-accretive would support higher growth and a lower risk premium.
- Lower capex intensity: a credible path from calendar 2026 capex toward a more normal maintenance-plus-growth level would raise fair value.
- Lower discount rate: a sustained lower-rate environment or lower perceived AI execution risk would move the sensitivity matrix upward.
- Faster share count reduction: stronger buybacks at attractive prices would raise per-share value, though buybacks at high multiples are less accretive.
- Durable Azure acceleration: management expects Azure growth to accelerate modestly in the second half of calendar 2026; sustained acceleration with stable margins would support the bull case.

## Missing / Unverified Data

| Data item | Status | Valuation impact |
|---|---|---|
| Product-level revenue and margins for Microsoft 365 Copilot, GitHub Copilot, Security Copilot, and other AI products | Not disclosed | Cannot directly model AI product unit economics. |
| OpenAI-specific Azure revenue, margin, capacity allocation, and contract economics | Not disclosed with enough granularity | Concentration and margin risk cannot be separately underwritten. |
| FY2026 full-year cash flow | ไม่พบข้อมูลที่ยืนยันได้ | FY2026 is still incomplete as of FY26 Q3; TTM FCF uses FY2025 and 9M FY26 official data. |
| Exact Q4 FY26 cash paid for property and equipment | Not yet reported | Q4 capex guidance includes finance lease variability and may not equal cash capex one-for-one. |
| Operating lease treatment in enterprise value | Simplified | Base DCF excludes operating lease liabilities from debt; including them would reduce equity value. |
| Current intraday 2026-05-18 US trading price | ไม่พบข้อมูลที่ยืนยันได้ at time checked | Latest available quoted close was 2026-05-15 because the US market had not produced a later regular-session close at the time of this Asia/Bangkok check. |

## Caveats

- This is a simple FCF-to-firm DCF, not a full operating model by segment.
- Microsoft reports capex and finance lease commentary in a way that can create timing differences between capex spend and cash paid for property and equipment.
- The model uses diluted weighted average shares rather than ending basic shares outstanding, which slightly lowers per-share fair value.
- The model treats cash and short-term investments as excess cash and uses current plus long-term debt as debt. It does not subtract operating lease liabilities or other long-term obligations from equity value.
- The bull case may still understate long-term AI upside if Microsoft creates a large high-margin usage layer across productivity, developer tools, security, business applications, and Azure. The base case may overstate value if AI workloads permanently reduce cloud margins or require recurring replacement capex faster than expected.
- Market price can be rational if investors are underwriting much higher post-2026 FCF growth than this model allows. The memo's conclusion is that the current price is hard to justify with a mature-company terminal growth framework, not that the business quality is weak.

## Entity Update

Updated `wiki/entities/MSFT.md` with a dated valuation watch item and a report link to `[[MSFT DCF Valuation 2026-05-18]]`. The core thesis was not rewritten because this DCF mainly affects valuation discipline, not the official-source business-quality assessment.
