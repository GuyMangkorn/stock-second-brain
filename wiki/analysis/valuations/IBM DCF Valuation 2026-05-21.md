---
type: analysis
analysis_type: dcf-valuation
ticker: IBM
company: International Business Machines Corporation
date: 2026-05-21
currency: USD
source_files:
  - wiki/entities/IBM.md
  - raw/financials/IBM_fundamentals.md
  - raw/imports/IBM_latest_results_source.md
tags:
  - analysis/dcf
  - ticker/IBM
---

# IBM DCF Valuation - 2026-05-21
Entity: [[IBM]]

## Bottom Line

This DCF uses source-backed IBM-defined TTM free cash flow of USD 14.992B, latest available market close of USD 224.88 on 2026-05-20, cash / restricted cash / marketable securities of USD 11.828B, total debt of USD 66.4B, and Q1 2026 diluted shares of 952.1M.

Base-case fair value is approximately **USD 240.27 per diluted share**, or about **6.8% upside** versus USD 224.88. That is not enough margin of safety for a strong new-money add by itself, especially because the model uses total debt conservatively and IBM still needs to prove sustained Software-led FCF growth after Confluent.

The stock is more fairly described as **watchlist / hold-quality** than obviously cheap. Upside becomes more compelling if IBM keeps FCF near or above FY2026 guidance, reduces debt, and shows that Software + AI growth is recurring rather than mostly acquisition/cycle-driven.

## Source Map

| Source | URL / Path | Use |
|---|---|---|
| Entity page | `wiki/entities/IBM.md` | Business model, thesis, risks, catalysts, source gaps. |
| Normalized facts | `raw/financials/IBM_fundamentals.md` | Q1 2026 financials, FY2025 annual baseline, FCF, cash, debt, shares, guidance. |
| Latest results source note | `raw/imports/IBM_latest_results_source.md` | Source map and raw extraction. |
| IBM Q1 2026 Form 10-Q | https://www.sec.gov/Archives/edgar/data/51143/000005114326000038/ibm-20260331.htm | Q1 2026 statements, share count, cash flow reconciliation, FCF definition. |
| IBM Q1 2026 earnings release | https://newsroom.ibm.com/2026-04-22-IBM-RELEASES-FIRST-QUARTER-RESULTS | Q1 2026 segment results, cash/debt summary, guidance. |
| IBM 1Q26 prepared remarks | https://www.ibm.com/downloads/documents/us-en/15db805fff4249f1 | Management commentary and guidance details. |
| IBM FY2025 10-K / annual report extract | https://www.sec.gov/Archives/edgar/data/51143/000005114326000010/ibm-20251231_d2.htm | FY2025 FCF, cash, debt, and annual baseline. |
| Stooq IBM quote CSV | https://stooq.com/q/l/?s=ibm.us&f=sd2t2ohlcv&h&e=csv | Fresh market price checked 2026-05-21 Asia/Bangkok. |

## Input Table

All financial statement amounts are USD billions unless noted.

| Input | Value | Source / Calculation |
|---|---:|---|
| Fresh market price used | USD 224.88 | Stooq close on 2026-05-20; fetched 2026-05-21 Asia/Bangkok. |
| Market capitalization | USD 211.36B | USD 224.88 * 939.885M shares outstanding from IBM Q1 2026 Form 10-Q. |
| Shares outstanding | 939.885M | IBM Q1 2026 Form 10-Q cover page. |
| Diluted shares used for DCF | 952.1M | IBM Q1 2026 weighted-average diluted shares. |
| Cash + restricted cash + marketable securities | 11.828 | IBM Q1 2026 Form 10-Q line items. |
| Total debt | 66.400 | IBM Q1 2026 earnings release. |
| IBM Financing debt included in total debt | 12.800 | IBM Q1 2026 earnings release and prepared remarks. |
| Operational debt excluding IBM Financing debt | 53.600 | 66.400 - 12.800. |
| Net debt used in base DCF | 54.572 | 66.400 - 11.828. |
| FY2025 IBM-defined FCF | 14.734 | IBM FY2025 annual report extract. |
| Q1 2025 IBM-defined FCF | 1.962 | IBM Q1 2026 Form 10-Q FCF reconciliation. |
| Q1 2026 IBM-defined FCF | 2.220 | IBM Q1 2026 Form 10-Q FCF reconciliation. |
| TTM IBM-defined FCF | 14.992 | 14.734 - 1.962 + 2.220. |
| FY2026 FCF guidance | About 15.7 | FY2025 FCF 14.734 + management guidance for about USD 1B YoY increase. |
| FY2026 revenue guidance | More than 5% constant-currency growth | IBM Q1 2026 earnings release and prepared remarks. |
| FY2026 Software revenue guidance | 10%+ growth | IBM 1Q26 prepared remarks. |

## Base Case Assumptions

| Assumption | Bear | Base | Bull |
|---|---:|---:|---:|
| Starting FCF anchor | TTM FCF USD 14.992B | TTM FCF USD 14.992B | TTM FCF USD 14.992B |
| Year 1 FCF growth | 0% | 5.0% | 8.0% |
| Year 2 FCF growth | 2.0% | 5.5% | 7.5% |
| Year 3 FCF growth | 2.0% | 5.0% | 7.0% |
| Year 4 FCF growth | 2.0% | 4.5% | 6.0% |
| Year 5 FCF growth | 2.0% | 4.0% | 5.0% |
| WACC | 9.5% | 8.5% | 7.5% |
| Terminal growth | 2.0% | 2.5% | 3.0% |
| Debt treatment | Total debt | Total debt | Total debt |

WACC basis: IBM sits economically between mature Information Technology, enterprise software, consulting, and infrastructure. The vault reference range for Information Technology is 8%-12%. Base WACC is 8.5% because IBM has recurring software/support cash flows and investment-grade liquidity, but leverage, acquisition integration, Consulting cyclicality, and IBM Financing complexity prevent a lower discount rate.

Terminal growth basis: 2.0%-3.0% matches the mature developed-market compounder range. The model does not use a terminal growth rate above 3.0% because IBM is already a large mature company and long-term growth should not assume indefinite AI re-acceleration.

## FCF Projection

Amounts are USD billions.

| Year | Bear FCF | Base FCF | Bull FCF |
|---:|---:|---:|---:|
| TTM anchor | 14.992 | 14.992 | 14.992 |
| Year 1 | 14.992 | 15.742 | 16.191 |
| Year 2 | 15.292 | 16.607 | 17.406 |
| Year 3 | 15.598 | 17.438 | 18.624 |
| Year 4 | 15.910 | 18.222 | 19.742 |
| Year 5 | 16.228 | 18.951 | 20.729 |

Base case rationale: management guidance for about USD 1B FY2026 FCF growth supports a Year 1 step-up near 5%, but debt load, acquisition integration, slower Consulting growth, and non-disclosed AI economics argue against assuming high-teens compounding.

## Valuation Summary

Amounts are USD billions except per-share data.

| Scenario | WACC | Terminal Growth | PV of Explicit FCF | PV of Terminal Value | Enterprise Value | Net Debt | Equity Value | Fair Value / Diluted Share | Upside / Downside vs USD 224.88 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Bear | 9.5% | 2.0% | 59.700 | 140.194 | 199.893 | 54.572 | 145.321 | 152.63 | -32.1% |
| Base | 8.5% | 2.5% | 68.020 | 215.310 | 283.330 | 54.572 | 228.758 | 240.27 | 6.8% |
| Bull | 7.5% | 3.0% | 74.336 | 330.486 | 404.822 | 54.572 | 350.250 | 367.87 | 63.6% |

## Sensitivity Matrix

Base projection fair value per diluted share, USD.

| WACC / Terminal Growth | 2.0% | 2.5% | 3.0% |
|---:|---:|---:|---:|
| 7.5% | 273.23 | 300.33 | 333.45 |
| 8.5% | 221.85 | 240.27 | 262.03 |
| 9.5% | 184.20 | 197.38 | 212.60 |

## Sanity Checks

| Check | Result | Read |
|---|---:|---|
| TTM FCF yield on market cap | 7.09% | Much less demanding than many AI/software names; supports watchlist interest. |
| Market EV / TTM FCF | 17.74x | Reasonable if IBM sustains FCF growth and Software mix improves; not cheap if growth fades. |
| FY2026 guided FCF yield | ~7.4% | Uses approximate USD 15.7B FY2026 FCF guidance and USD 211.36B market cap. |
| Total debt / TTM FCF | 4.43x | Leverage is material; debt reduction matters to equity upside. |
| Net debt / TTM FCF | 3.64x | Still meaningful even after cash/marketable securities. |
| Operational net debt / TTM FCF | 2.79x | Excluding IBM Financing debt makes leverage less severe, but this is an analytical adjustment, not the base DCF treatment. |
| Base DCF terminal value share of EV | 76.0% | High but below the 85%-90% warning threshold. |
| Bull DCF terminal value share of EV | 81.6% | Still below 85%, but increasingly sensitive to terminal assumptions. |

## What Would Change The Valuation

- Higher confidence in FY2026 FCF: progress toward USD 15.7B+ would support or raise base value.
- Debt reduction: lower total debt after Confluent would directly increase equity value and reduce WACC pressure.
- Clearer AI monetization: product-level AI revenue/margins or a fresh AI book-of-business figure would support higher growth assumptions.
- Consulting recovery: signings and GenAI backlog must convert into revenue growth, not only backlog penetration.
- Software durability: Red Hat/OpenShift/Data/Automation growth must remain strong after acquisition contributions normalize.
- Infrastructure normalization: if z17 cycle fades faster than expected, terminal growth and near-term FCF assumptions should be cut.

## Missing / Unverified Data

| Data item | Status | Valuation impact |
|---|---|---|
| Full FY2026 actual results | not disclosed | Uses Q1 2026 and FY2025 baseline instead. |
| Product-level AI revenue and AI margins | not disclosed | AI upside cannot be directly modeled. |
| Exact Q1 2026 generative AI book of business value | ไม่พบข้อมูลที่ยืนยันได้ | Cannot quantify Q1 AI pipeline expansion from official source set. |
| Segment-level FCF | not disclosed | Cannot test whether Software, Consulting, or Infrastructure is driving cash conversion. |
| Financing debt adjustment | judgment required | Base DCF uses total debt conservatively; excluding IBM Financing debt would raise fair value. |
| Investor-specific required return and position constraints | not provided | Prevents personalized sizing. |

## Entity Update

Updated `wiki/entities/IBM.md` with the valuation watch item and report link. Core action read is `HOLD / WATCHLIST`, not a high-conviction add, because base-case upside is modest and leverage/source gaps still matter.
