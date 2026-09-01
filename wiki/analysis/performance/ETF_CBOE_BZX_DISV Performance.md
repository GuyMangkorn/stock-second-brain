---
type: etf-performance
instrument_type: ETF
entity_key: Cboe BZX:DISV
ticker: DISV
exchange: Cboe BZX
fund: Dimensional International Small Cap Value ETF
tracked_index: no specific index; actively managed
benchmark: S&P 500 Total Return
management_mode: active-equity-long-only
active_process: systematic-active
management_benchmark: MSCI World ex USA Small Value Index (net dividends)
track_record: provisional
management_evidence: positive return-only
risk_evidence: not-verified
updated: 2026-09-01
performance_as_of: 2025-12-31
current_ytd_as_of: 2026-07-31
price_nav_as_of: 2026-08-31
source_batch: raw/imports/ETF_performance_sources_2026-09-01_run-4.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/DISV
  - geography/International
---

# DISV Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

DISV เป็น active long-only international small-cap value ETF ของ Dimensional
ที่ใช้ systematic-active process และไม่มีเป้าหมาย replicate ดัชนีใดโดยเฉพาะ.
Official complete calendar rows ที่ยืนยันได้คือ 2023-2025: NAV Total Return
cumulative 86.70% และ rounded-input CAGR 23.14%; current NAV TR YTD ล่าสุดที่
พบจาก Schwab เป็น secondary observation 12.90% ณ 2026-07-31. Official issuer
since-inception annualized NAV TR อยู่ที่ 14.78% ณ 2025-12-31.

## Performance check

- entity_key: Cboe BZX:DISV
- Inception: 2022-03-23; listing date 2022-03-24
- Expense ratio: 0.42% total annual fund operating expenses (management fee 0.39% + other expenses 0.03%); Dimensional quick guide also reports gross 0.43% / net 0.42% as of 2025-12-31
- Metric: NAV Total Return รวม reinvested distributions และ fund expenses; market-price return remains separate
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark)
- management_mode: active-equity-long-only
- active_process: systematic-active; official SEC strategy combines research, portfolio design, portfolio management and trading, with flexible daily implementation
- management_benchmark: MSCI World ex USA Small Value Index (net dividends), selected because the official SEC performance table explicitly describes it as an additional index with a similar investment universe; MSCI World ex USA Index is broader and S&P 500 remains only the common reference benchmark
- track_record: provisional; official since-inception observation runs from 2022-03-23 to 2025-12-31, approximately 3.78 elapsed years
- management_evidence: positive return-only; official since-inception annualized NAV TR 14.78% versus management benchmark 10.38%, Excess CAGR +4.40 pp; compatible annual benchmark rows and hit rate were not disclosed
- risk_evidence: not-verified
- 10-year window: not applicable (<10 years of history)
- Coverage/source note: official calendar chart covers 2023-2025; the 2022 inception-year partial is not shown in the official annual bar chart and is excluded. Current 2026 YTD fields are secondary Schwab observations and are marked `*`.

| Year | DISV NAV TR | S&P 500 TR |
|---|---:|---:|
| 2023 | 19.60% | 26.29% |
| 2024 | 6.02% | 25.02% |
| 2025 | 47.24% | 17.88% |
| 2023-2025 cumulative | 86.70% | 86.12% |

S&P 500 เป็น common reference benchmark ไม่ใช่ management benchmark ของ DISV;
annual comparison นี้ใช้ cached USD Total Return convention ณ 2025-12-31.

## Up years / Down years

- Up years / Down years: 3 / 0 ใน complete official 2023-2025 rows
- Best: 2025, +47.24%
- Least positive: 2024, +6.02%
- Worst: ไม่พบ down year ใน complete official rows
- Least bad down year: ไม่พบข้อมูลที่ยืนยันได้
- 2023-2025 cumulative / CAGR: 86.70% / 23.14%; S&P 500 TR: 86.12% / 23.01%
- Official issuer 1-year NAV TR: 47.24% as of 2025-12-31; official since-inception annualized NAV TR: 14.78% as of 2025-12-31
- Current date-to-date YTD*: 12.90% NAV as of 2026-07-31 from secondary Schwab performance data; secondary closing price US$44.63 as of 2026-08-31

## Risk read-through

DISV มี international developed-markets small-cap/value exposure และ official
SEC prospectus ระบุ small-company, foreign securities/currencies, geographic,
value, profitability, market-trading และ international closed-market risks.
Population standard deviation ของ official 2023-2025 annual rows อยู่ที่ 17.15%
แต่มีเพียงสามปี จึงเป็นเพียง short-window descriptor. Official highest quarter
คือ +15.12% ใน Q2 2025 และ lowest quarter -7.54% ใน Q4 2024. Secondary Schwab
reports 3-year annualized NAV TR 22.40% as of 2026-07-31 and market price
US$44.63 as of 2026-08-31; official daily NAV history for a reproducible
maximum drawdown and recovery was not verified.

## Active management read-through

- management_mode: active-equity-long-only
- active_process: systematic-active
- management_benchmark: MSCI World ex USA Small Value Index (net dividends)
- track_record: provisional
- management_evidence: positive return-only
- risk_evidence: not-verified
- Official since-inception annualized NAV TR was 14.78% versus 10.38% for the selected management benchmark, or Excess CAGR +4.40 pp. This is return-only evidence because the SEC table does not disclose compatible annual benchmark rows or a complete-year hit rate.
- Dimensional names no individual portfolio manager in the reviewed summary-prospectus continuity block beyond the listed team; the strategy is described as an integrated research, portfolio-design, portfolio-management and trading process. The 2026-02-28 prospectus reports 8% portfolio turnover for the latest fiscal year.
- The official 1-year comparison at 2025-12-31 was DISV 47.24% versus MSCI World ex USA Small Value Index 38.55%; this is retained as a separate one-year observation and not converted into alpha.

## Sources

- Official SEC summary prospectus: https://www.sec.gov/Archives/edgar/data/1816125/000181612526000069/c497k.htm
- Official SEC prospectus: https://www.sec.gov/Archives/edgar/data/1816125/000181612526000046/c485bpos.htm
- Official Dimensional fund page: https://www.dimensional.com/us-en/funds/disv/international-small-cap-value
- Official Dimensional ETF lineup: https://www.dimensional.com/us-en/etfs
- Official Dimensional ETF Quick Guide: https://my.dimensional.com/chmedia/282748/source/dimensional-etf-quick-guide.pdf
- Official Cboe listing: https://www.cboe.com/us/equities/listings/listed_products/symbols/DISV
- Secondary current-performance cross-check: https://www.schwab.wallst.com/Prospect/Research/etfs/performance.asp?symbol=disv
- Official S&P 500 index page: https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- Current source batch: [[ETF_performance_sources_2026-09-01_run-4]]
