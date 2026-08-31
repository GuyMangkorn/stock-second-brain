---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:IVLU
input_ticker: IVLU
ticker: IVLU
exchange: NYSE Arca
fund: iShares MSCI Intl Value Factor ETF
tracked_index: MSCI World ex USA Enhanced Value Index (Net)
benchmark: S&P 500 Total Return
issuer_benchmark: MSCI World ex USA Enhanced Value Index (Net)
management_mode: passive-index
active_process: not applicable
management_benchmark: not applicable
track_record: established
management_evidence: not applicable
risk_evidence: issuer-fields
updated: 2026-09-01
performance_as_of: 2026-08-28
calendar_years_as_of: 2025-12-31
current_ytd_as_of: 2026-08-28
fund_facts_as_of: 2026-08-28
source_batch: raw/imports/ETF_performance_sources_2026-09-01_run-2.md
return_basis: NAV total return; market-price return separate
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/IVLU
  - geography/International
---

# IVLU Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

IVLU เป็น passive international value-factor ETF ที่ติดตาม MSCI World ex USA
Enhanced Value Index (Net). Official NAV TR ล่าสุดให้ YTD `17.91%` ณ
`2026-08-28`; official rolling 5-year annualized return อยู่ที่ `14.77%` ณ
`2026-06-30`. ปี 2025 ที่ `46.24%` ช่วยดันผลตอบแทนช่วงล่าสุด แต่ style factor
ยังมีโอกาส lag broad international market ได้.

## Performance check

- `entity_key`: `NYSE Arca:IVLU`
- Inception date: `2015-06-16`
- Expense ratio: `0.31%`
- Current official NAV: `$44.08` as of `2026-08-28`; closing price `$44.23`; net assets `$4,584,495,178`; 348 holdings
- Metric: NAV Total Return in USD; market-price return is separate
- Official current YTD: `17.91%` as of `2026-08-28`
- Official rolling returns as of `2026-06-30`: 1-year `32.00%`; 3-year `23.09%`; 5-year `14.77%`; 10-year `11.53%`; since inception `8.47%`
- Issuer benchmark: `MSCI World ex USA Enhanced Value Index (Net)`
- Official rounded 2021-2025 rows imply cumulative `103.49%` and CAGR `15.27%`

| Year | IVLU NAV TR | S&P 500 TR (USD reference) |
|---|---:|---:|
| 2021 | 15.32% | 28.71% |
| 2022 | -5.80% | -18.11% |
| 2023 | 19.99% | 26.29% |
| 2024 | 6.75% | 25.02% |
| 2025 | 46.24% | 17.88% |

S&P 500 Total Return เป็น common USD reference ไม่ใช่ IVLU’s issuer benchmark.
Annual rows มาจาก iShares June 2026 factsheet; rounded-row CAGR ใช้เพื่อ
ตรวจสอบช่วงปีเท่านั้น และไม่แทนที่ rolling CAGR ที่มี endpoint ต่างกัน.

## Up years / Down years

- Up years / Down years in the complete 2021-2025 window: `4 / 1`
- Best displayed year: 2025, `+46.24%`
- Worst displayed year: 2022, `-5.80%`
- Rounded-input 2021-2025 cumulative return / CAGR: `103.49% / 15.27%`
- Official rolling 5-year NAV CAGR: `14.77%` as of `2026-06-30`

## Risk read-through

The value tilt can create country, sector, and style concentration versus a
broad developed-market portfolio. Official June factsheet fields report
standard deviation `12.51%`, beta `0.50`, P/E `14.23`, and P/B `1.36`; the
latest product snapshot reports standard deviation `12.50%` and beta `0.49`.
Equity, currency, tracking, liquidity, and market-trading risks remain. A
fresh daily-NAV maximum drawdown and recovery period is `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- [iShares official IVLU product page](https://www.ishares.com/us/products/275382/IVLU)
- [iShares IVLU official factsheet](https://www.ishares.com/us/literature/fact-sheet/ivlu-ishares-msci-intl-value-factor-etf-fund-fact-sheet-en-us.pdf)
- [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- ETF source batch: [[ETF_performance_sources_2026-09-01_run-2]]

