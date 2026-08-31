---
type: etf-performance
instrument_type: ETF
entity_key: Cboe BZX:DIHP
input_ticker: DIHP
ticker: DIHP
exchange: Cboe BZX
fund: Dimensional International High Profitability ETF
tracked_index: Active systematic high-profitability non-US equity process
benchmark: S&P 500 Total Return
issuer_benchmark: MSCI World ex USA Index (net dividends)
management_mode: active-equity-long-only
active_process: systematic-factor
management_benchmark: MSCI World ex USA Index (net dividends)
track_record: developing-short-live-history
management_evidence: mixed-short-track-record
risk_evidence: issuer-fields
updated: 2026-09-01
performance_as_of: 2026-08-18
calendar_years_as_of: 2025-12-31
current_ytd_as_of: 2026-08-18
fund_facts_as_of: 2026-08-18
source_batch: raw/imports/ETF_performance_sources_2026-09-01_run-2.md
return_basis: NAV total return; market-price return separate
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/DIHP
  - geography/International
---

# DIHP Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

DIHP เป็น active long-only ETF ของ Dimensional ที่ใช้ systematic profitability
process กับบริษัทขนาดใหญ่ในตลาดนอกสหรัฐฯ ไม่ใช่ index-replication fund. Official
fund table ล่าสุดที่ตรวจได้ให้ NAV `$35.25`, YTD `22.33%`, 1-year `13.67%` และ
since-inception annualized `10.12%` ณ `2026-08-18`. Track record ยังสั้น จึงควร
ให้น้ำหนักกับ benchmark-relative evidence มากกว่าการ extrapolate CAGR จากสามปี.

## Performance check

- `entity_key`: `Cboe BZX:DIHP`
- Fund inception: `2022-03-23`
- Expense ratio: `0.27%`
- Metric: NAV Total Return in USD; market-price return is separate
- Official current snapshot as of `2026-08-18`: NAV `$35.25`; YTD `22.33%`; 1-year `13.67%`; since-inception annualized `10.12%`
- Issuer/management benchmark: `MSCI World ex USA Index (net dividends)`
- Complete official annual rows 2023-2025 imply cumulative `53.26%` and rounded-input CAGR `15.30%`

| Year | DIHP NAV TR | S&P 500 TR (USD reference) |
|---|---:|---:|
| 2023 | 18.93% | 26.29% |
| 2024 | 0.78% | 25.02% |
| 2025 | 27.87% | 17.88% |

2022 ไม่มี complete calendar-year row เพราะกองเริ่มต้นในเดือนมีนาคม. S&P 500
Total Return เป็น common USD reference ไม่ใช่ management benchmark ของ DIHP.

## Up years / Down years

- Up years / Down years in the complete 2023-2025 window: `3 / 0`
- Best displayed year: 2025, `+27.87%`
- Least positive year: 2024, `+0.78%`
- Rounded-input 2023-2025 cumulative return / CAGR: `53.26% / 15.30%`
- 10-year live ETF CAGR: `ไม่พบข้อมูลที่ยืนยันได้` because the fund began in 2022

## Risk read-through

The strategy carries equity, non-US currency, country, liquidity, profitability-
factor, and active portfolio-construction risks. SEC data show the highest
quarterly return was `10.91%` for the quarter ended `2023-12-31`, while the
lowest was `-8.16%` for the quarter ended `2024-12-31`. A fresh daily-NAV
maximum drawdown and recovery period is `ไม่พบข้อมูลที่ยืนยันได้`.

## Active management read-through

`management_mode`: `active-equity-long-only`  
`active_process`: `systematic-factor`  
`management_benchmark`: `MSCI World ex USA Index (net dividends)`  
`track_record`: `developing-short-live-history`  
`management_evidence`: `mixed-short-track-record`  
`risk_evidence`: `issuer-fields`

- Official 2025 NAV return: DIHP `27.87%` versus management benchmark `31.85%`, arithmetic difference `-3.98 pp`.
- Official since-inception annualized return through `2025-12-31`: DIHP `8.90%` versus benchmark `10.92%`, arithmetic difference `-2.02 pp`.
- These are short-history benchmark-relative observations, not alpha and not evidence of persistent manager skill. The official process description supports a systematic profitability tilt, but future outperformance is not established.

## Sources

- [SEC DIHP summary prospectus](https://www.sec.gov/Archives/edgar/data/1816125/000181612526000046/R7.htm)
- [Dimensional official DIHP product page](https://www.dimensional.com/us-en/funds/dihp/international-high-profitability-etf)
- [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- ETF source batch: [[ETF_performance_sources_2026-09-01_run-2]]

