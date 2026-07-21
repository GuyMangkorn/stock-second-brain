---
type: valuation
ticker: LLY
valuation_date: 2026-07-11
method: corporate FCF DCF with scenario sensitivity
stage_gate: calculation-ready-high-sensitivity
currency: USD
market_price: 1188.58
source_files:
  - raw/financials/LLY_fundamentals.md
  - raw/imports/LLY_market_quote_2026-07-11.md
  - raw/imports/LLY_latest_results_source.md
entity: "[[LLY]]"
tags:
  - valuation/dcf
  - ticker/LLY
---

# LLY DCF Valuation - 2026-07-11

## Bottom Line

P11 ผ่าน stage gate แบบ `calculation-ready-high-sensitivity`: LLY มี source-backed FCF, cash, debt, diluted shares และ multi-year reinvestment history เพียงพอสำหรับ scenario DCF แต่ FCF กำลังโตจากฐานต่ำพร้อม capex/manufacturing ramp และไม่มี FY2026 FCF guide. Base fair value อยู่ประมาณ **USD 249/share** เทียบกับ close **USD 1,188.58**; bull case ที่ใช้ 35% → 30% → 25% → 15% → 10% FCF growth ยังอยู่ประมาณ **USD 385/share**. ผลลัพธ์จึงชี้ว่า current price สะท้อน execution และ terminal economics ที่ aggressive มาก และยังไม่มี margin of safety สำหรับ new capital.

## Market Data Check

| Item | Value | Source |
|---|---:|---|
| Last regular-session close | USD 1,188.58 on 2026-07-10 | [[LLY_market_quote_2026-07-11]]; S&P Global data via StockAnalysis |
| Official issuer visible close | USD 1,215.83 on 2026-07-08 | Lilly historic lookup / LSEG; cross-check only |
| Common shares outstanding | 941.741m | SEC Form 10-Q, as of 2026-04-17 |
| Market capitalization | approximately USD 1,119.3bn | Calculated: USD 1,188.58 × 941.741m |

## Valuation Inputs

| Input | Value | Provenance / treatment |
|---|---:|---|
| FY2025 FCF anchor | USD 8.972bn | Calculated from FY2025 OCF USD 16.813bn less capex spend USD 7.841bn |
| FY2024 / FY2023 FCF | USD 3.760bn / USD 0.792bn | Calculated from FY2025 Form 10-K cash-flow statements |
| Q1 2026 FCF | USD 3.007bn | Calculated from Q1 OCF USD 5.333bn less capex spend USD 2.326bn; not annualized |
| Cash used in EV-to-equity bridge | USD 5.282bn | Q1 2026 SEC Form 10-Q cash and cash equivalents |
| Debt | USD 43.370bn | Q1 current debt USD 4.000bn plus long-term debt USD 39.370bn |
| Net debt used | USD 38.088bn | Calculated: debt less cash; noncurrent investments excluded from cash bridge |
| Diluted shares used | 895m | Lilly FY2026 guidance assumption; distinct from 941.741m common shares outstanding |
| FY2026 revenue guidance | USD 82bn–85bn | Official Q1 release; used as growth context, not as a direct FCF forecast |
| FY2026 non-GAAP EPS guidance | USD 35.50–37.00 | Official Q1 release; cross-check only |

## Method And Assumptions

Simple corporate FCF DCF is usable because Lilly is profitable and has three annual FCF observations plus Q1 2026 cash flow. However, FCF is not yet mature: FY2025 capex was USD 7.841bn, Q1 2026 capex was USD 2.326bn, and management continues to expand manufacturing. I therefore use a transparent scenario model rather than a precise point target.

The FY2025 FCF anchor is an observed source-backed value. Forecast growth, WACC, and terminal growth are analyst assumptions, not company guidance.

| Scenario | FCF growth, Years 1–5 | WACC | Terminal growth | Interpretation |
|---|---|---:|---:|---|
| Bear | 10%, 8%, 6%, 4%, 3% | 10.0% | 2.0% | Price/rebate pressure, high reinvestment, and slower conversion of pipeline to cash |
| Base | 25%, 20%, 15%, 10%, 7% | 9.0% | 3.0% | Strong GLP-1 growth with gradual FCF normalization and continued investment |
| Bull | 35%, 30%, 25%, 15%, 10% | 8.5% | 3.0% | Foundayo/retatrutide expand the franchise and capacity converts with strong returns |

WACC uses the Health Care reference range of 8%–10%. The base case is 9.0% because Lilly has market leadership and recurring medicine demand but also regulatory, pipeline, pricing, manufacturing, and financing risks. Terminal growth of 3.0% is the upper end of the mature developed-market compounder range and is intentionally favorable to Lilly.

## Base Projection And Calculation

| Fiscal year | FCF growth assumption | Projected FCF | PV of FCF at 9.0% |
|---|---:|---:|---:|
| Year 1 | 25% | 11.215 | 10.289 |
| Year 2 | 20% | 13.458 | 11.327 |
| Year 3 | 15% | 15.477 | 11.951 |
| Year 4 | 10% | 17.024 | 12.060 |
| Year 5 | 7% | 18.216 | 11.839 |
| Explicit forecast PV | — | — | 57.467 |
| Terminal value | 3.0% terminal growth | 312.709 | 203.240 PV |

Formulae: `FCF = OCF - capex spend`; `EV = PV(projected FCF) + PV(terminal value)`; `Equity value = EV + cash - debt`; `Fair value/share = equity value / diluted shares`; `Terminal value = Year 5 FCF × (1 + g) / (WACC - g)`.

## Valuation Summary

| Scenario | Enterprise value | Equity value | Fair value / share | Upside / (downside) vs USD 1,188.58 |
|---|---:|---:|---:|---:|
| Bear | 137.624 | 99.536 | 111.21 | (90.6%) |
| Base | 260.706 | 222.618 | 248.73 | (79.1%) |
| Bull | 382.933 | 344.845 | 385.30 | (67.6%) |

All dollar values in the valuation tables are USD billions except per-share values. The bridge does not separately add lease liabilities or noncurrent investments; this keeps the model traceable but may not be fully conservative or fully diluted.

## Sensitivity: Fair Value / Share

Base FCF growth path is held constant; only WACC and terminal growth vary.

| Terminal growth \ WACC | 8.5% | 9.0% | 9.5% |
|---:|---:|---:|---:|
| 2.0% | 234.97 | 214.41 | 196.59 |
| 2.5% | 253.80 | 230.25 | 210.08 |
| 3.0% | 276.06 | 248.73 | 225.63 |

Terminal value is approximately 78.0% of base enterprise value, within the normal mature-company range but high enough that the conclusion remains assumption-sensitive.

## Sanity Checks

- FY2025 price / diluted EPS is approximately 51.8x; price / FY2026 non-GAAP EPS guidance midpoint is approximately 32.8x.
- FY2025 FCF yield on calculated market cap is approximately 0.80%; EV / FY2025 FCF is approximately 129x using the DCF net-debt bridge.
- The DCF assumes sustained double-digit FCF growth for five years in the base case and still produces a value far below the market price. The gap is a valuation signal, not proof that the business will fail.
- Q2 2026 preliminary acquired IPR&D of approximately USD 2.8bn is an earnings headwind and should not be treated as recurring FCF in the DCF.

## Valuation-Specific Blockers

- FY2026 actual FCF and capex are not available, and there is no numeric FCF guide.
- FCF history is rapidly improving and may not represent a normalized steady state; future capacity spending could be higher or lower than modeled.
- Diluted shares used for guidance are approximately 895m while SEC common shares outstanding are 941.741m; a complete fully diluted reconciliation is not available.
- Product-level profitability, consensus estimates, and probability-adjusted pipeline cash flows are not disclosed.

## Change Triggers

- Re-run after 2026-08-05 Q2 results using actual revenue, price/volume mix, capex, OCF, FCF, and updated guidance.
- Upgrade only if FCF conversion improves materially without weakening product access/pricing and if the market price moves toward a defensible margin-of-safety range.
- Re-underwrite if Foundayo uptake, Medicare Bridge economics, retatrutide progress, Jaypirca EU approval, or Kisunla data materially changes the long-run cash-flow path.

## Sources

- [[LLY_latest_results_source]]
- [[LLY_fundamentals]]
- [[LLY_market_quote_2026-07-11]]
- [SEC LLY Q1 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/59478/000005947826000045/lly-20260331.htm)
- [Lilly Q1 2026 earnings release](https://investor.lilly.com/node/54176)
