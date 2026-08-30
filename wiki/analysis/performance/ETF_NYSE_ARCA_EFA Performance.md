---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:EFA
ticker: EFA
exchange: NYSE Arca
fund: iShares MSCI EAFE ETF
tracked_index: MSCI EAFE Index (Net)
benchmark: MSCI EAFE Index (Net)
management_mode: passive-index
implementation: representative-sampling
updated: 2026-08-30
performance_as_of: 2025-12-31 (official calendar) / 2026-06-30 (official standardized)
calendar_years_as_of: 2025-12-31
current_ytd_as_of: 2026-08-27
price_nav_as_of: 2026-08-28
fund_facts_as_of: 2026-08-28 / 2026-07-31
source_batch: raw/imports/ETF_performance_sources_2026-08-30.md
return_basis: NAV total return; dividends and distributions reinvested; net of expenses
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/EFA
  - geography/International
---

# EFA Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

EFA เป็น passive developed-markets ETF ที่ติดตาม MSCI EAFE Index (Net) สำหรับหุ้น
ขนาดใหญ่และกลางนอกสหรัฐฯ และแคนาดา. Official NAV Total Return ที่รวบรวมจาก
official iShares sources ให้ช่วง 2016-2025 สะสม `118.82%` หรือ rounded-input CAGR
`8.15%`; มีปีบวก/ลบ `8 / 2`. Official rolling 10-year NAV TR อยู่ที่ `9.68%`
เทียบ benchmark `9.65%` ณ 2026-06-30 และ current NAV TR YTD ล่าสุดที่ตรวจได้คือ
`14.29%` ณ 2026-08-27.

## Performance check

- `entity_key: NYSE Arca:EFA`; fund `iShares MSCI EAFE ETF`; inception `2001-08-14`; exchange `NYSE Arca`; asset class `equity`.
- Tracked index and strategy-aligned benchmark: `MSCI EAFE Index (Net)`, a free-float-adjusted market-capitalization-weighted index of large- and mid-cap developed-market equities outside the U.S. and Canada.
- Metric: `NAV Total Return` in USD, including reinvested dividends/distributions and net of expenses. Market-price returns are kept separate.
- Current official snapshot as of 2026-08-28: NAV `US$107.53`, closing price `US$107.72`, net assets `US$79.48B`, and premium/discount `0.18%`; official NAV TR YTD is `+14.29%` as of 2026-08-27.
- Current fund facts: expense ratio `0.32%` (`0.31%` management fee + `0.01%` other expenses), `673` holdings as of 2026-08-27, 3-year beta `0.66`, and 3-year standard deviation `12.79%` as of 2026-07-31.
- Official rolling performance as of 2026-06-30: NAV TR 1-year `20.11%`, 3-year `16.38%`, 5-year `9.11%`, 10-year `9.68%`; benchmark `20.23%`, `16.42%`, `9.04%`, `9.65%` respectively.
- 10-year calendar window: `2015-12-31` to `2025-12-31`; rounded-input NAV TR CAGR `8.15%`; official issuer rolling 10-year NAV TR is `9.68%` as of 2026-06-30. Calendar CAGR formula: `(End TR / Start TR)^(1 / Years) - 1`.
- Coverage/source note: official iShares summary prospectus provides EFA NAV rows for 2016-2020, while the current official product page provides EFA NAV and benchmark rows for 2021-2025. The reviewed official EFA table did not expose benchmark rows for 2016-2020, so those benchmark values are not backfilled or inferred.

| Year / window | EFA NAV TR | Tracked benchmark | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | 0.96% | not disclosed in reviewed EFA table | 11.96% |
| 2017 | 24.94% | not disclosed in reviewed EFA table | 21.83% |
| 2018 | -13.83% | not disclosed in reviewed EFA table | -4.38% |
| 2019 | 21.94% | not disclosed in reviewed EFA table | 31.49% |
| 2020 | 7.91% | not disclosed in reviewed EFA table | 18.40% |
| 2021 | 11.23% | 11.26% | 28.71% |
| 2022 | -14.27% | -14.45% | -18.11% |
| 2023 | 18.07% | 18.24% | 26.29% |
| 2024 | 3.43% | 3.82% | 25.02% |
| 2025 | 31.38% | 31.22% | 17.88% |
| 2016-2025 cumulative | 118.82% | not calculated | 298.33% |
| 2016-2025 CAGR | 8.15% | not calculated | 14.82% |
| 2021-2025 cumulative | 52.99% | 53.32% | 96.17% |
| 2021-2025 CAGR | 8.88% | 8.92% | 14.43% |

**Up years / Down years — complete 2016-2025 window**

- Up years / Down years: `8 / 2`.
- Best: 2025, `+31.38%`.
- Least positive: 2016, `+0.96%`.
- Worst: 2018, `-13.83%`.
- Least bad down year: 2018, `-13.83%`.
- Current official NAV TR YTD: `+14.29%` as of 2026-08-27; the reviewed S&P 500 source did not provide a synchronized current field, so no current cross-market comparison is inferred.

## Risk read-through

The official iShares snapshot reports 3-year beta `0.66` and standard deviation
`12.79%` as of 2026-07-31, with `673` holdings as of 2026-08-27. The largest
sector exposures were financials `26.03%`, industrials `19.09%`, information
technology `10.34%`, and health care `10.25%`; Japan was `23.35%` of geographic
exposure on the same August 27 snapshot. These are issuer snapshot fields, not
a substitute for a daily NAV series. Compatible official daily NAV history
sufficient to calculate maximum drawdown, recovery duration, downside capture,
or full tracking error was not verified. Main risks are developed-country,
foreign-currency, Japan/country, sector, large-/mid-cap, market, tracking-error,
systematic fair-value timing, securities-lending, and ETF premium/discount risks.

## Tracking / implementation read-through

- `management_mode`: `passive-index`; the fund uses indexing and does not seek to beat the MSCI EAFE Index.
- The official prospectus describes representative sampling, a general 80% investment policy in index components or substantially identical securities, and a goal of tracking the index before fees and expenses.
- Official 2021-2025 fund-minus-benchmark differences are `-0.03, +0.18, -0.17, -0.39, +0.16 pp`; EFA beat the tracked index in `2/5` calendar years. The rounded-input 2021-2025 relative wealth is `-0.21%` versus the benchmark.
- The official rolling 10-year NAV TR was `0.03 pp` above the benchmark as of 2026-06-30. Expense drag, transaction costs, cash, withholding taxes, portfolio sampling, and systematic fair-value timing can create tracking differences.
- S&P 500 TR is a common cross-ETF reference only and is not EFA's tracked index or evidence of active management. EFA beat that common reference in `3/10` complete calendar years, but this comparison is not strategy attribution.

## Sources

- [iShares EFA product page](https://www.ishares.com/us/products/239623/EFA) — official identity, exchange, inception, benchmark, current NAV/YTD, assets, holdings, price, premium/discount, rolling performance, 2021-2025 calendar rows, exposures, and fees.
- [iShares EFA summary prospectus](https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-eafe-etf-7-31.pdf) — official objective, 0.32% expenses, 4% turnover, representative-sampling/indexing strategy, 2016-2020 annual NAV rows, and risk disclosures.
- [iShares EFA fact sheet](https://www.ishares.com/us/literature/fact-sheet/efa-ishares-msci-eafe-etf-fund-fact-sheet-en-us.pdf) — official 2026-03-31 fund facts and 2021-2025 calendar performance context.
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached `check-etf-performance` references — common USD Total Return benchmark for complete 2016-2025 calendar years.
- [State Street SPY performance](https://www.ssga.com/us/en/individual/etfs/state-street-spdr-sp-500-etf-trust-spy) — official common-benchmark reference; no synchronized current YTD field is inferred here.
- [[ETF_performance_sources_2026-08-30]] | [[ETF Performance Index]]
