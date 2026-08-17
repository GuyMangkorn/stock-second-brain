---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:DFAS
ticker: DFAS
exchange: NYSE Arca
fund: Dimensional U.S. Small Cap ETF
tracked_index: no specific index; actively managed
benchmark: S&P 500 Total Return
management_mode: active-equity-long-only
active_process: systematic-active
management_benchmark: Russell 2000 Index
track_record: established-with-predecessor-history
management_evidence: mixed-benchmark-relative
risk_evidence: not-verified
updated: 2026-08-17
performance_as_of: 2025-12-31
current_ytd_as_of: 2026-07-31
price_nav_as_of: 2026-08-14
source_batch: raw/imports/ETF_performance_sources_2026-08-17.md
return_basis: NAV total return
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/DFAS
  - geography/United-States
---

# DFAS Performance

> Navigation: [[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]

## Bottom line

DFAS เป็น active long-only U.S. small-cap ETF ของ Dimensional ที่ใช้
systematic-active process และไม่ได้มุ่ง replicate ดัชนีใดโดยเฉพาะ. Official SEC
summary prospectus ให้ complete calendar-year NAV Total Return ปี 2016-2025;
กองทุนมี cumulative return 154.28% และ rounded-input CAGR 9.78%. ใน common
2021-2025 window CAGR อยู่ที่ 9.42%. Current YTD 16.9% ณ 2026-07-31 เป็น
secondary NAV/market-price performance observation จาก Schwab ไม่ใช่ current
issuer table. หลักฐานเทียบ Russell 2000 เป็น mixed: -4.63 pp ใน 1-year,
+3.33 pp ใน 5-year และ +0.16 pp ใน 10-year ณ 2025-12-31; ตัวเลขเหล่านี้เป็น
benchmark-relative return evidence ไม่ใช่ alpha.

## Performance check

- entity_key: NYSE Arca:DFAS
- Inception: 1998-12-15; ETF listing: 2021-06-14; predecessor mutual-fund history is used before the June 2021 reorganization
- Listing venue: NYSE Arca, Inc.
- Expense ratio: 0.26% in the SEC summary prospectus dated 2026-02-28, comprising 0.25% management fee and 0.01% other expenses; a Dimensional Quick Guide search capture showed 0.27%, so the source-dated fee difference remains disclosed
- Metric: official NAV Total Return including reinvested dividends and other earnings; market-price return remains separate; currency USD
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark)
- management_mode: active-equity-long-only
- active_process: systematic-active; official SEC materials describe integrated research, portfolio design, portfolio management and trading with flexible implementation
- management_benchmark: Russell 2000 Index, the official additional index with a similar investment universe in the SEC performance table
- track_record: established-with-predecessor-history; the official performance discussion adopts predecessor-fund results before the 2021 reorganization
- management_evidence: mixed-benchmark-relative; official 1-year/5-year/10-year annualized differences versus Russell 2000 are -4.63 pp, +3.33 pp and +0.16 pp
- risk_evidence: not-verified; official daily NAV history sufficient for reproducible maximum drawdown and recovery was not captured
- Current secondary YTD: 16.9% as of 2026-07-31; Schwab reports identical market-price and NAV YTD values at one-decimal precision
- Current secondary quote snapshot: market price US$84.48 at close 2026-08-14; closing NAV US$83.78 and premium/discount +0.04% as of 2026-08-12

| Year / window | DFAS NAV TR | Management benchmark | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | 23.99% | not disclosed as annual row | 11.96% |
| 2017 | 11.87% | not disclosed as annual row | 21.83% |
| 2018 | -13.12% | not disclosed as annual row | -4.38% |
| 2019 | 21.89% | not disclosed as annual row | 31.49% |
| 2020 | 10.36% | not disclosed as annual row | 18.40% |
| 2021 | 29.70% | not disclosed as annual row | 28.71% |
| 2022 | -13.80% | not disclosed as annual row | -18.11% |
| 2023 | 17.53% | not disclosed as annual row | 26.29% |
| 2024 | 10.35% | not disclosed as annual row | 25.02% |
| 2025 | 8.18% | not disclosed as annual row | 17.88% |
| 2016-2025 cumulative | 154.28% | not calculated | 298.33% |
| 2016-2025 CAGR | 9.78% | not calculated | 14.82% |
| 2021-2025 CAGR | 9.42% | not calculated | 14.43% |

S&P 500 rows reuse the cached USD Total Return convention for complete calendar
years 2016-2025, with dividends reinvested and as-of 2025-12-31. Russell 2000
is the strategy-aligned management comparator; the official SEC table provides
rolling annualized fields rather than a complete annual benchmark series.

| Synchronized rolling window ended 2025-12-31 | DFAS NAV TR | Russell 2000 Index | Difference |
|---|---:|---:|---:|
| 1-year annualized | 8.18% | 12.81% | -4.63 pp |
| 5-year annualized | 9.42% | 6.09% | +3.33 pp |
| 10-year annualized | 9.78% | 9.62% | +0.16 pp |

## Up years / Down years

- Up years / Down years: 8 / 2 ใน complete official 2016-2025 rows
- Best year: 2021, +29.70%
- Worst year: 2022, -13.80%
- Annual-return population standard deviation: 13.73% across the 10 rounded official annual observations
- 2016-2025 cumulative / CAGR: 154.28% / 9.78%; S&P 500 TR 298.33% / 14.82%
- 2021-2025 cumulative / CAGR: 56.86% / 9.42%; S&P 500 TR 96.17% / 14.43%
- Current date-to-date YTD: 16.9% as of 2026-07-31, secondary Schwab observation; no synchronized Russell 2000 YTD was captured
- Annual hit rate versus management benchmark: ไม่พบข้อมูลที่ยืนยันได้ because the reviewed official source does not disclose a comparable annual Russell 2000 row for each year

## Risk read-through

DFAS มี U.S. small-cap exposure และ official SEC prospectus ระบุ equity-market,
small-company, profitability, value, tax-management, market-trading,
premium/discount, derivatives, securities-lending, operational และ cyber
security risks. Portfolio turnover ใน fiscal year ล่าสุดที่รายงานคือ 6%.
Schwab's secondary snapshot reports 2,059 holdings and total assets of US$15.3B
as of 2026-08-12. Official daily NAV history for a reproducible maximum
drawdown and recovery was not verified; no numeric drawdown or recovery claim is
saved.

## Active management read-through

- management_mode: active-equity-long-only
- active_process: systematic-active
- management_benchmark: Russell 2000 Index
- track_record: established-with-predecessor-history
- management_evidence: mixed-benchmark-relative
- risk_evidence: not-verified
- The SEC identifies DFAS as actively managed and says it does not seek to replicate a specific index. The process combines research, portfolio design, management and trading with market-cap weighting plus possible emphasis on smaller size, lower relative price and higher profitability.
- Official rolling evidence is mixed: DFAS trailed Russell 2000 by 4.63 pp over one year, led by 3.33 pp over five years and led by 0.16 pp over ten years through 2025-12-31.
- The predecessor history makes the long record useful for strategy context, but ETF-share-class history and current expenses are not identical across the entire window. No alpha claim is made.

## Sources

- Official SEC summary prospectus: https://www.sec.gov/Archives/edgar/data/1816125/000181612526000081/c497k.htm
- Official Dimensional fund page: https://www.dimensional.com/us-en/funds/dfas/us-small-cap-etf
- Official Dimensional listing announcement: https://www.dimensional.com/us-en/newsroom/dimensional-lists-four-new-etfs-following-the-industrys-largest-mutual-fund-to-etf-conversion
- Official Dimensional ETF Quick Guide: https://my.dimensional.com/chmedia/282748/source/dimensional-etf-quick-guide.pdf
- Secondary current performance cross-check: https://www.schwab.wallst.com/Prospect/Research/etfs/performance.asp?symbol=dfas
- Secondary current fund snapshot: https://www.schwab.wallst.com/Prospect/Research/etfs/summary.asp?symbol=dfas
- Official S&P 500 index page: https://www.spglobal.com/spdji/en/indices/equity/sp-500/
