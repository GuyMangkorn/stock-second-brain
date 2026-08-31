---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:QEFA
input_ticker: QEFA
ticker: QEFA
exchange: NYSE Arca
fund: State Street SPDR MSCI EAFE StrategicFactors ETF
tracked_index: MSCI EAFE Factor Mix A-Series Index
benchmark: S&P 500 Total Return
issuer_benchmark: MSCI EAFE Factor Mix A-Series Index
management_mode: passive-index
active_process: strategic-factor
management_benchmark: not applicable
track_record: established
management_evidence: not applicable
risk_evidence: issuer-fields
updated: 2026-09-01
performance_as_of: 2026-07-31
calendar_years_as_of: 2025-12-31
current_ytd_as_of: 2026-07-31
fund_facts_as_of: 2026-08-27
source_batch: raw/imports/ETF_performance_sources_2026-09-01_run-2.md
return_basis: NAV total return; market-price return separate
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/QEFA
  - geography/International
---

# QEFA Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

QEFA เป็น passive strategic-factor ETF สำหรับ developed markets ex-US/Canada
ที่ผสม low-volatility, quality และ value. Official NAV TR ล่าสุดให้ YTD
`11.24%`, 1-year `23.04%` และ 10-year annualized `8.92%` ณ `2026-07-31`.
Calendar rows ด้านล่างเป็น secondary rounded proxies เพราะ official factsheet
ที่ตรวจได้ไม่แสดง annual table เต็มชุด.

## Performance check

- `entity_key`: `NYSE Arca:QEFA`
- Inception date: `2014-06-04`
- Expense ratio: `0.30%`
- Current official NAV: `$101.49` as of `2026-08-27`; AUM `$1,075.78M`
- Metric: NAV Total Return in USD; market-price return is separate
- Official current performance as of `2026-07-31`: YTD `11.24%`; 1-year `23.04%`; 3-year annualized `14.90%`; 5-year `8.58%`; 10-year `8.92%`; since inception `7.07%`
- Issuer benchmark: `MSCI EAFE Factor Mix A-Series Index`
- Secondary rounded 2016-2025 rows imply cumulative `118.32%` and CAGR `8.12%`; official rolling 10-year CAGR remains `8.92%`

| Year | QEFA NAV TR* | S&P 500 TR (USD reference) |
|---|---:|---:|
| 2016 | 0.3% | 11.96% |
| 2017 | 23.9% | 21.83% |
| 2018 | -10.2% | -4.38% |
| 2019 | 21.9% | 31.49% |
| 2020 | 7.0% | 18.40% |
| 2021 | 12.4% | 28.71% |
| 2022 | -14.0% | -18.11% |
| 2023 | 17.3% | 26.29% |
| 2024 | 2.7% | 25.02% |
| 2025 | 28.8% | 17.88% |

`*` Annual rows are rounded AAII secondary proxies as of `2026-07-31`; they
are not presented as issuer-reported annual figures. S&P 500 Total Return is a
common USD reference, not QEFA’s issuer benchmark.

## Up years / Down years

- Up years / Down years in the secondary 2016-2025 window: `8 / 2`
- Best displayed year: 2025, `+28.8%*`
- Worst displayed year: 2022, `-14.0%*`
- Rounded-input 2016-2025 cumulative return / CAGR: `118.32% / 8.12%` (proxy approximation)
- Official rolling 10-year NAV CAGR: `8.92%` as of `2026-07-31`

## Risk read-through

Factor mixing can lag a capitalization-weighted EAFE portfolio when value,
quality, or low-volatility leadership is out of favor. Official factsheet data
confirm `643` holdings as of `2026-06-30`; equity, country, currency, factor,
tracking, and market-trading risks remain. A fresh daily-NAV maximum drawdown
and recovery period is `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- [State Street official QEFA product page](https://www.ssga.com/us/en/individual/etfs/state-street-spdr-msci-eafe-strategicfactors-etf-qefa)
- [State Street QEFA factsheet](https://www.ssga.com/library-content/products/factsheets/etfs/us/factsheet-us-en-qefa.pdf)
- [AAII QEFA data](https://www.aaii.com/etfs/summary?ticker=QEFA)
- [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- ETF source batch: [[ETF_performance_sources_2026-09-01_run-2]]

