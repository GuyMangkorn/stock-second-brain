---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:DFIV
ticker: DFIV
exchange: NYSE Arca
fund: Dimensional International Value ETF
tracked_index: no specific index; actively managed
benchmark: S&P 500 Total Return
management_mode: active-equity-long-only
active_process: systematic-active
active_process_subtype: systematic developed ex-U.S. large-cap value tilt with flexible implementation
management_benchmark: MSCI World ex USA Value Index (net dividends)
track_record: established
management_evidence: positive
risk_evidence: not-verified
updated: 2026-08-30
performance_as_of: 2025-12-31 (official annual) / 2026-06-30 (official rolling)
calendar_years_as_of: 2025-12-31
current_ytd_as_of: 2026-07-31
price_nav_as_of: not used; current price/NAV pair not required for this performance check
fund_facts_as_of: 2026-06-30 / prospectus 2026-02-28
source_batch: raw/imports/ETF_performance_sources_2026-08-30.md
return_basis: NAV total return; dividends and other earnings reinvested; net of expenses
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/DFIV
  - geography/International
---

# DFIV Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

DFIV เป็น active long-only ETF ของ Dimensional ที่ใช้ `systematic-active` process
เพื่อเน้นหุ้น value ขนาดใหญ่ใน developed markets นอกสหรัฐฯ. Official
predecessor-linked NAV Total Return ช่วง 2016-2025 สะสม `166.30%` หรือ
rounded-input CAGR `10.29%`; มีปีบวก/ลบ `7 / 3`, ดีที่สุดปี 2025 `+45.17%`
และแย่ที่สุดปี 2018 `-17.32%`. Current YTD ที่ตรวจได้คือ `+16.70%*` ณ
2026-07-31 เทียบกับ S&P 500 Total Return `+10.14%` ในวันเดียวกัน โดย `*` คือ
secondary standardized NAV field.

## Performance check

- `entity_key: NYSE Arca:DFIV`; fund `Dimensional International Value ETF`; inception `1999-04-16`; ETF listing `2021-09-13`; listing venue `NYSE Arca, Inc.`
- Expense ratio `0.27%` (management fee `0.25%` + other expenses `0.02%`); official latest portfolio turnover `6%`.
- Metric: `NAV Total Return` รวม dividends และ other earnings ที่ reinvested และหัก fund expenses; currency USD. NAV/market-price history ก่อน listing ใช้ predecessor mutual fund ตาม official disclosure.
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference benchmark).
- `management_mode: active-equity-long-only`; `active_process: systematic-active`; portfolio design emphasizes lower relative price stocks, with flexible research, design, management, and trading functions.
- `management_benchmark: MSCI World ex USA Value Index (net dividends)`; official SEC performance table identifies it as the additional index with a similar investment universe. The broader MSCI World ex USA Index and S&P 500 remain reference alternatives, not the selected management comparator.
- 10-year window: `2015-12-31` to `2025-12-31`; 10-year NAV TR CAGR `10.29%`; `Start TR value: 100.00; End TR value: 266.30; Years: 10.00`. The SEC standardized 10-year annualized return is also `10.29%`.
- Formula: `(End TR / Start TR)^(1 / Years) - 1`; the endpoint is normalized from the displayed official annual rows, so the cumulative calculation is rounded-input.
- Coverage/source note: official complete calendar rows are predecessor-linked before the 2021 ETF listing and continue through 2025; the 2021 row is a complete annual return, not an inception-year partial. Current YTD is marked `*` because the reviewed official Dimensional capture did not expose a July 2026 YTD field.

| Year / window | DFIV NAV TR | Management benchmark | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | 8.20% | 7.39% | 11.96% |
| 2017 | 25.95% | 21.04% | 21.83% |
| 2018 | -17.32% | -15.06% | -4.38% |
| 2019 | 15.86% | 17.02% | 31.49% |
| 2020 | -1.58% | -3.22% | 18.40% |
| 2021 | 17.29% | 13.26% | 28.71% |
| 2022 | -3.62% | -5.64% | -18.11% |
| 2023 | 17.75% | 18.48% | 26.29% |
| 2024 | 7.26% | 6.65% | 25.02% |
| 2025 | 45.17% | 42.23% | 17.88% |
| 2016-2025 cumulative | 166.30% | 140.17% | 298.33% |
| 2016-2025 CAGR | 10.29% | 9.16% | 14.82% |
| 2021-2025 cumulative | 107.26% | 92.07% | 96.17% |
| 2021-2025 CAGR | 15.69% | 13.94% | 14.43% |

**Up years / Down years — complete 2016-2025 window**

- Up years / Down years: `7 / 3`.
- Best: 2025, `+45.17%`.
- Least positive: 2024, `+7.26%`.
- Worst: 2018, `-17.32%`.
- Least bad down year: 2020, `-1.58%`.
- Current YTD: `+16.70%*` as of 2026-07-31; S&P 500 Total Return common reference `+10.14%` as of 2026-07-31.

## Risk read-through

Official annual-return population standard deviation is `16.41%` across
2016-2025. The official prospectus reports the highest quarter as `+21.49%`
(2020 Q4) and the lowest as `-31.49%` (2020 Q1). Official daily NAV history
sufficient to calculate maximum drawdown, recovery date/duration, downside
capture, or tracking error was not verified; risk evidence therefore remains
`not-verified`. Main risks are international country and currency exposure,
value-regime cyclicality, sector concentration, foreign-market trading, and
ETF premium/discount/liquidity. The 0.27% expense ratio and 6% turnover are
official fund-cost context, not a promise of future tracking results.

## Active management read-through

- `management_mode`: `active-equity-long-only`
- `active_process`: `systematic-active`
- `management_benchmark`: `MSCI World ex USA Value Index (net dividends)`; selected at hierarchy step 1 because the official SEC performance table identifies it as a similar-universe index. The broad MSCI World ex USA Index and S&P 500 were rejected as less strategy-aligned comparators.
- `track_record`: `established`; the ETF uses predecessor history from 1999, while the ETF listing began in 2021.
- `management_evidence`: `positive`; official 10-year annualized NAV TR `10.29%` exceeded the management benchmark `9.16%` by `+1.13 pp`, and the complete-year active return was positive in `7 / 10` years. The rounded-input cumulative relative wealth versus the management benchmark is `+10.88%`.
- `risk_evidence`: `not-verified`; annual volatility and quarterly extremes are available, but compatible daily NAV evidence for maximum drawdown/recovery and risk-adjusted management persistence was not captured.
- SEC-disclosed portfolio leadership includes Jed S. Fogdall (Portfolio Manager since 2021; predecessor since 2010), Joseph F. Hohn and Joel P. Schneider since 2022, and Brendan J. McAndrews since 2025. The evidence is attributed to the strategy/adviser process; it is not labeled alpha or proof of persistent manager skill.

## Sources

- [Dimensional International Value ETF factsheet](https://www.dimensional.com/chmedia/71946/source/download/international-value-etf.pdf) — official 2026-06-30 fund facts, benchmark, NAV/benchmark annual rows, rolling returns, and return definition.
- [DFIV summary prospectus, SEC](https://www.sec.gov/Archives/edgar/data/1816125/000181612526000082/c497k.htm) — official NYSE Arca identity, expenses, turnover, active strategy, predecessor history, 2016-2025 annual rows, 10-year comparator, quarterly extremes, and adviser/team disclosures.
- [Dimensional DFIV fund page](https://www.dimensional.com/us-en/funds/dfiv/international-value-etf) — official product access point.
- [Schwab DFIV performance](https://www.schwab.wallst.com/Prospect/Research/etfs/performance.asp?symbol=dfiv) — secondary standardized NAV YTD `+16.7%` as of 2026-07-31 and current market snapshot; marked `*` and not used to replace official annual NAV rows.
- [State Street SPY performance](https://www.ssga.com/us/en/individual/etfs/state-street-spdr-sp-500-etf-trust-spy) — official S&P 500 Index benchmark YTD `+10.14%` as of 2026-07-31.
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached `check-etf-performance` references — common USD Total Return benchmark for complete 2016-2025 calendar years.
- [[ETF_performance_sources_2026-08-30]] | [[ETF Performance Index]]
