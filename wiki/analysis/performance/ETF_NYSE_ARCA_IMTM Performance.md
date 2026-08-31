---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:IMTM
input_ticker: IMTM
ticker: IMTM
exchange: NYSE Arca
fund: iShares MSCI Intl Momentum Factor ETF
tracked_index: MSCI World ex USA Momentum Index (Net)
benchmark: S&P 500 Total Return
issuer_benchmark: MSCI World ex USA Momentum Index (Net)
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
  - ticker/IMTM
  - geography/International
---

# IMTM Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

IMTM เป็น passive momentum-factor ETF สำหรับ developed markets ex-US โดย
ติดตาม MSCI World ex USA Momentum Index (Net). Official NAV TR ล่าสุดให้ YTD
`12.21%` ณ `2026-08-28`; official rolling 5-year annualized return อยู่ที่
`10.65%` ณ `2026-06-30`. Momentum มีความเสี่ยงจากการเปลี่ยนผู้นำตลาดและ
turnover/style reversal จึงควรอ่านควบคู่กับ factor exposure.

## Performance check

- `entity_key`: `NYSE Arca:IMTM`
- Inception date: `2015-01-13`
- Expense ratio: `0.30%`
- Current official NAV: `$53.18` as of `2026-08-28`; closing price `$53.32`; net assets `$4,254,713,180`; 302 holdings
- Metric: NAV Total Return in USD; market-price return is separate
- Official current YTD: `12.21%` as of `2026-08-28`
- Official rolling returns as of `2026-06-30`: 1-year `22.25%`; 3-year `21.07%`; 5-year `10.65%`; 10-year `10.71%`; since inception `9.51%`
- Issuer benchmark: `MSCI World ex USA Momentum Index (Net)`
- Official rounded 2021-2025 rows imply cumulative `52.32%` and CAGR `8.78%`

| Year | IMTM NAV TR | S&P 500 TR (USD reference) |
|---|---:|---:|
| 2021 | 6.53% | 28.71% |
| 2022 | -16.65% | -18.11% |
| 2023 | 13.68% | 26.29% |
| 2024 | 12.25% | 25.02% |
| 2025 | 34.43% | 17.88% |

S&P 500 Total Return เป็น common USD reference ไม่ใช่ IMTM’s issuer
benchmark. Annual rows มาจาก iShares June 2026 factsheet; rounded-row CAGR
ใช้เป็นการตรวจสอบช่วงปี ไม่แทนที่ rolling CAGR ที่มี endpoint ต่างกัน.

## Up years / Down years

- Up years / Down years in the complete 2021-2025 window: `4 / 1`
- Best displayed year: 2025, `+34.43%`
- Worst displayed year: 2022, `-16.65%`
- Rounded-input 2021-2025 cumulative return / CAGR: `52.32% / 8.78%`
- Official rolling 5-year NAV CAGR: `10.65%` as of `2026-06-30`

## Risk read-through

Momentum exposure can reverse abruptly and can produce country, sector, and
valuation concentration. Official June factsheet fields report beta `0.73`,
standard deviation `13.13%`, P/E `21.19`, and P/B `2.56`; the latest product
snapshot reports beta `0.74` and standard deviation `13.31%`. Equity, currency,
tracking, liquidity, and market-trading risks remain. A fresh daily-NAV maximum
drawdown and recovery period is `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- [iShares official IMTM product page](https://www.ishares.com/us/products/271538/ishares-msci-intl-momentum-factor-etf)
- [iShares IMTM official factsheet](https://www.ishares.com/us/literature/fact-sheet/imtm-ishares-msci-intl-momentum-factor-etf-fund-fact-sheet-en-us.pdf)
- [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- ETF source batch: [[ETF_performance_sources_2026-09-01_run-2]]

