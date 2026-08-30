---
type: etf-performance
instrument_type: ETF
entity_key: Cboe BZX:EFV
ticker: EFV
exchange: Cboe BZX
fund: iShares MSCI EAFE Value ETF
tracked_index: MSCI EAFE Value Index (Net)
benchmark: MSCI EAFE Value Index (Net)
management_mode: passive-index
implementation: representative-sampling
updated: 2026-08-30
performance_as_of: 2025-12-31 (official calendar) / 2026-06-30 (official standardized)
calendar_years_as_of: 2025-12-31
current_ytd_as_of: 2026-08-26
price_nav_as_of: 2026-08-27 / 2026-08-26
fund_facts_as_of: 2026-08-27 / 2026-07-31
source_batch: raw/imports/ETF_performance_sources_2026-08-30.md
return_basis: NAV total return; dividends and distributions reinvested; net of expenses
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/EFV
  - geography/International
---

# EFV Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

EFV เป็น passive value-tilt ETF ที่ติดตาม MSCI EAFE Value Index (Net) ซึ่งคัดหุ้น
developed markets นอกสหรัฐฯ และแคนาดาที่มี value characteristics. Official NAV
Total Return ที่รวบรวมจาก official iShares sources ให้ช่วง 2016-2025 สะสม
`128.17%` หรือ rounded-input CAGR `8.60%`; มีปีบวก/ลบ `7 / 3`. Official rolling
10-year NAV TR อยู่ที่ `10.39%` เทียบ benchmark `10.44%` ณ 2026-06-30 และ current
NAV TR YTD ล่าสุดที่ตรวจได้คือ `18.09%` ณ 2026-08-26.

## Performance check

- `entity_key: Cboe BZX:EFV`; fund `iShares MSCI EAFE Value ETF`; inception `2005-08-01`; exchange `Cboe BZX`; asset class `equity`.
- Tracked index and strategy-aligned benchmark: `MSCI EAFE Value Index (Net)`, a subset of the MSCI EAFE Index targeting approximately 50% of its free-float-adjusted market capitalization and emphasizing securities with value characteristics.
- Metric: `NAV Total Return` in USD, including reinvested dividends/distributions and net of expenses. Market-price returns are kept separate.
- Current official snapshot: NAV `US$81.65` and net assets `US$31.71B` as of 2026-08-27; closing price `US$82.23` and premium/discount `0.14%` as of 2026-08-26. Current official NAV TR YTD is `+18.09%` as of 2026-08-26.
- Current fund facts: expense ratio `0.31%` (`0.31%` management fee + `0.00%` other expenses), `404` holdings as of 2026-08-26, 30-day SEC yield `2.87%`, 12-month trailing yield `4.46%`, 3-year beta `0.43`, and 3-year standard deviation `12.09%` as of 2026-07-31.
- Official rolling performance as of 2026-06-30: NAV TR 1-year `26.64%`, 3-year `21.40%`, 5-year `13.19%`, 10-year `10.39%`; benchmark `26.95%`, `21.49%`, `13.14%`, `10.44%` respectively.
- 10-year calendar window: `2015-12-31` to `2025-12-31`; rounded-input NAV TR CAGR `8.60%`; official issuer rolling 10-year NAV TR is `10.39%` as of 2026-06-30. Calendar CAGR formula: `(End TR / Start TR)^(1 / Years) - 1`.
- Coverage/source note: the official iShares summary prospectus provides EFV NAV rows for 2016-2020, while the current official product page provides EFV NAV and benchmark rows for 2021-2025. The reviewed official EFV table did not expose benchmark rows for 2016-2020, so those benchmark values are not backfilled or inferred.

| Year / window | EFV NAV TR | Tracked benchmark | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | 4.87% | not disclosed in reviewed EFV table | 11.96% |
| 2017 | 21.22% | not disclosed in reviewed EFV table | 21.83% |
| 2018 | -14.88% | not disclosed in reviewed EFV table | -4.38% |
| 2019 | 15.97% | not disclosed in reviewed EFV table | 31.49% |
| 2020 | -2.78% | not disclosed in reviewed EFV table | 18.40% |
| 2021 | 10.82% | 10.89% | 28.71% |
| 2022 | -5.38% | -5.58% | -18.11% |
| 2023 | 18.87% | 18.95% | 26.29% |
| 2024 | 5.40% | 5.68% | 25.02% |
| 2025 | 42.36% | 42.25% | 17.88% |
| 2016-2025 cumulative | 128.17% | not calculated | 298.33% |
| 2016-2025 CAGR | 8.60% | not calculated | 14.82% |
| 2021-2025 cumulative | 87.03% | 87.23% | 96.17% |
| 2021-2025 CAGR | 13.34% | 13.36% | 14.43% |

**Up years / Down years — complete 2016-2025 window**

- Up years / Down years: `7 / 3`.
- Best: 2025, `+42.36%`.
- Least positive: 2016, `+4.87%`.
- Worst: 2018, `-14.88%`.
- Least bad down year: 2020, `-2.78%`.
- Current official NAV TR YTD: `+18.09%` as of 2026-08-26; the reviewed S&P 500 source did not provide a synchronized current field, so no current cross-market comparison is inferred.

## Risk read-through

The official iShares snapshot reports 3-year beta `0.43` and standard deviation
`12.09%` as of 2026-07-31, with `404` holdings as of 2026-08-26. Financials were
`39.66%` of sector exposure and Japan was `23.33%` of geographic exposure on the
August 26 snapshot. These are issuer snapshot fields, not a substitute for a
daily NAV series. Compatible official daily NAV history sufficient to calculate
maximum drawdown, recovery duration, downside capture, or full tracking error was
not verified. Main risks are value-factor cyclicality, financial-sector and
country concentration, foreign currency and developed-market exposure, large-/
mid-cap risk, tracking error, systematic fair-value timing, securities lending,
and ETF premium/discount/liquidity.

## Tracking / implementation read-through

- `management_mode`: `passive-index`; the fund uses indexing and does not seek to beat the MSCI EAFE Value Index.
- The official prospectus describes representative sampling, a general 80% investment policy in index components or substantially identical securities, and a goal of tracking the index before fees and expenses.
- Official 2021-2025 fund-minus-benchmark differences are `-0.07, +0.20, -0.08, -0.28, +0.11 pp`; EFV beat the tracked index in `2/5` calendar years. The rounded-input 2021-2025 relative wealth is `-0.11%` versus the benchmark.
- The official rolling 10-year NAV TR was `0.05 pp` below the benchmark as of 2026-06-30. Expense drag, transaction costs, cash, withholding taxes, sampling, and systematic fair-value timing can create tracking differences.
- S&P 500 TR is a common cross-ETF reference only and is not EFV's tracked index or evidence of active management. EFV beat that common reference in `2/10` complete calendar years, but this comparison is not strategy attribution.

## Sources

- [iShares EFV product page](https://www.ishares.com/us/products/239628/ishares-msci-eafe-value-etf) — official identity, Cboe BZX listing, inception, benchmark, current NAV/YTD, assets, holdings, price, premium/discount, rolling performance, 2021-2025 calendar rows, exposures, and fees.
- [iShares EFV summary prospectus](https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-eafe-value-etf-7-31.pdf) — official objective, 0.31% expenses, 23% turnover, value-index scope, representative-sampling/indexing strategy, 2016-2020 annual NAV rows, and risk disclosures.
- [iShares EFV fact sheet](https://www.ishares.com/us/literature/fact-sheet/efv-ishares-msci-eafe-value-etf-fund-fact-sheet-en-us.pdf) — official 2026-06-30 fund facts and 2021-2025 calendar performance context.
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached `check-etf-performance` references — common USD Total Return benchmark for complete 2016-2025 calendar years.
- [State Street SPY performance](https://www.ssga.com/us/en/individual/etfs/state-street-spdr-sp-500-etf-trust-spy) — official common-benchmark reference; no synchronized current YTD field is inferred here.
- [[ETF_performance_sources_2026-08-30]] | [[ETF Performance Index]]
