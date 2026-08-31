---
type: etf-performance
instrument_type: ETF
entity_key: Cboe BZX:IMFL
input_ticker: IMFL
ticker: IMFL
exchange: Cboe BZX
fund: Invesco International Developed Dynamic Multifactor ETF
tracked_index: FTSE Developed ex US Invesco Dynamic Multifactor Index
benchmark: S&P 500 Total Return
issuer_benchmark: FTSE Developed ex US Index
management_mode: passive-index
active_process: dynamic-multifactor-index
management_benchmark: not applicable
track_record: developing-short-live-history
management_evidence: not applicable
risk_evidence: issuer-fields
updated: 2026-09-01
performance_as_of: 2026-03-31
calendar_years_as_of: 2025-12-31
current_ytd_as_of: 2026-08-25
fund_facts_as_of: 2026-03-31
source_batch: raw/imports/ETF_performance_sources_2026-09-01_run-2.md
return_basis: USD NAV total return; market-price return separate
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/IMFL
  - geography/International
---

# IMFL Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

IMFL เป็น passive indexed multifactor ETF ของ Invesco สำหรับ developed markets
ex-US โดยใช้ดัชนี FTSE Developed ex US Invesco Dynamic Multifactor Index ที่
rebalance รายเดือน. Official factsheet ณ `2026-03-31` ให้ 1-year NAV TR
`31.64%` และ since-inception annualized `8.46%`; current YTD ที่มีล่าสุดเป็น
secondary proxy `20.09%*` ณ `2026-08-25` เพราะ official performance widget
อ่านเป็น text ไม่ได้.

## Performance check

- `entity_key`: `Cboe BZX:IMFL`
- Inception date: `2021-02-24`
- Expense ratio: `0.34%`
- Metric: USD NAV Total Return; market-price return is separate
- Current official NAV/YTD: `ไม่พบข้อมูลที่ยืนยันได้` in the captured official text; secondary YTD `20.09%*` as of `2026-08-25`
- Official factsheet returns as of `2026-03-31`: 1-year `31.64%`; 3-year annualized `14.31%`; 5-year `7.97%`; since inception `8.46%`
- Tracked index: `FTSE Developed ex US Invesco Dynamic Multifactor Index`; official comparison benchmark: `FTSE Developed ex US Index`
- Official rounded 2022-2025 rows imply cumulative `31.09%` and CAGR `7.00%`

| Year | IMFL NAV TR | S&P 500 TR (USD reference) |
|---|---:|---:|
| 2022 | -16.71% | -18.11% |
| 2023 | 24.96% | 26.29% |
| 2024 | -3.70% | 25.02% |
| 2025 | 30.79% | 17.88% |

2021 ไม่มี complete calendar-year row เพราะกองเริ่มต้นในเดือนกุมภาพันธ์. S&P
500 Total Return เป็น common USD reference ไม่ใช่ official comparison benchmark
ของ Invesco และไม่ใช่ tracked index.

## Up years / Down years

- Up years / Down years in the complete 2022-2025 window: `2 / 2`
- Best displayed year: 2025, `+30.79%`
- Worst displayed year: 2022, `-16.71%`
- Rounded-input 2022-2025 cumulative return / CAGR: `31.09% / 7.00%`
- Official since-inception annualized NAV return: `8.46%` as of `2026-03-31`

## Risk read-through

Monthly factor rebalancing can create turnover, style, sector, country, and
tracking differences versus a broad developed-market index. Official March
factsheet fields report `1,146` holdings, P/E `17.01`, P/B `2.37`, and ROE
`12.12%`. Equity, currency, liquidity, and market-trading risks remain. A
fresh daily-NAV maximum drawdown and recovery period is `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- [Invesco official IMFL product page](https://www.invesco.com/us/en/financial-products/etfs/invesco-international-developed-dynamic-multifactor-etf.html)
- [Invesco IMFL official factsheet](https://www.invesco.com/content/dam/invesco/us/en/product-documents/etf/fact-sheet/imfl-invesco-international-developed-dynamic-multifactor-etf-fact-sheet.pdf)
- [ETF Central IMFL data](https://www.etfcentral.com/fund/IMFL)
- [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- ETF source batch: [[ETF_performance_sources_2026-09-01_run-2]]

