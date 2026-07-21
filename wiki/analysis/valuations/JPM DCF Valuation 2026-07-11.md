---
type: valuation
ticker: JPM
valuation_date: 2026-07-11
method: bank-specific P/TBV and P/BV scenario
stage_gate: calculation-ready
currency: USD
market_price: 336.47
source_files:
  - raw/financials/JPM_fundamentals.md
  - raw/imports/JPM_market_quote_2026-07-11.md
  - raw/imports/JPM_latest_results_source.md
entity: "[[JPM]]"
tags:
  - valuation/dcf
  - valuation/bank-specific
  - ticker/JPM
---

# JPM DCF Valuation - 2026-07-11

## Bottom Line

P11 ผ่าน stage gate ในรูปแบบ bank-specific valuation ไม่ใช่ simple FCF DCF. ที่ราคาปิด $336.47, JPM ซื้อขายที่ประมาณ 3.09x 1Q26 TBVPS และ 16.1x TTM diluted EPS. Scenario base ที่ 2.8x TBVPS ให้ fair value $304.84 ต่อหุ้น หรือ downside ราว 9.4%; bull case 3.3x ให้ $359.27 หรือ upside เพียง 6.8%. ผลลัพธ์จึงยังไม่ให้ margin of safety เพียงพอสำหรับ `ADD` แม้ franchise และ ROTCE มีคุณภาพสูง.

## Market Data Check

| Item | Value | Source |
|---|---:|---|
| Last regular-session close | $336.47 on 2026-07-10 | [[JPM_market_quote_2026-07-11]] |
| Period-end common shares | 2,679.5M | 1Q26 earnings supplement. |
| Implied market capitalization | $901.6B | Calculation: $336.47 × 2,679.5M shares. |

## Valuation Inputs

| Input | Value | Provenance |
|---|---:|---|
| 1Q26 TBVPS | $108.87 | 1Q26 earnings supplement. |
| 1Q26 book value per share | $128.38 | 1Q26 earnings supplement. |
| TTM diluted EPS | $20.89 | Calculation: FY2025 $20.02 - 1Q25 $5.07 + 1Q26 $5.94. |
| Current quarterly common dividend | $1.50 | 1Q26 earnings supplement; annualized $6.00 for cross-check only. |
| 1Q26 ROE / ROTCE | 19% / 23% | 1Q26 earnings supplement. |
| Standardized / Advanced CET1 | 14.3% / 14.1% | 1Q26 earnings supplement. |

## Method And Assumptions

Simple corporate FCF DCF is not suitable as the primary model for a bank because deposits, regulatory capital, and balance-sheet reinvestment are core operating inputs. This memo therefore uses a P/TBV scenario with P/BV and earnings cross-checks.

| Scenario | P/TBV multiple | Interpretation |
|---|---:|---|
| Bear | 2.3x | Credit-cycle or capital pressure reduces sustainable ROTCE and the premium multiple. |
| Base | 2.8x | High-quality diversified bank, but normalized returns and rate/credit uncertainty cap the premium. |
| Bull | 3.3x | 20%+ ROTCE remains durable, credit stays controlled, and capital returns remain flexible. |

Multiples are analyst assumptions, not management guidance. They are deliberately shown as a range because 2Q26 results are pending and JPM’s realized returns are market and credit dependent.

## Valuation Summary

| Scenario | Formula | Fair value / share | Upside / (downside) vs $336.47 |
|---|---|---:|---:|
| Bear | $108.87 × 2.3x | $250.40 | (25.6%) |
| Base | $108.87 × 2.8x | $304.84 | (9.4%) |
| Bull | $108.87 × 3.3x | $359.27 | 6.8% |

## Sensitivity

Illustrative fair value per share under alternative TBVPS and P/TBV inputs:

| P/TBV \ TBVPS | $100 | $108.87 | $120 |
|---:|---:|---:|---:|
| 2.3x | $230.00 | $250.40 | $276.00 |
| 2.8x | $280.00 | $304.84 | $336.00 |
| 3.3x | $330.00 | $359.27 | $396.00 |

## Sanity Checks

- Current P/TBV: 3.09x; current P/BV: 2.62x.
- Current price / TTM diluted EPS: 16.1x.
- Annualized current dividend yield: about 1.78%; the intended $1.65 3Q26 dividend is not used because it remained subject to Board approval in the source.
- The $50B repurchase authorization is flexibility, not a guaranteed cash outflow or valuation input.

## Valuation-Specific Blockers

- No 2Q26 financial results or updated guidance before the scheduled 2026-07-14 release.
- Simple FCF DCF not used because JPM is a bank; a residual-income model would require additional explicit capital, payout, and long-run return assumptions.
- Investor-specific required return, position size, cost basis, and tax constraints were not provided.

## Change Triggers

- Re-run after 2Q26 with TBVPS, CET1/RWA, NII, expense, NCOs, ROE/ROTCE, and capital returns.
- Upgrade valuation only if sustainable ROTCE and TBVPS growth support a multiple above the base case while credit costs remain controlled.
- Downgrade if credit losses accelerate, CET1 buffer narrows materially, or NII/expense guidance weakens.

## Sources

- [[JPM_latest_results_source]]
- [[JPM_fundamentals]]
- [[JPM_market_quote_2026-07-11]]
