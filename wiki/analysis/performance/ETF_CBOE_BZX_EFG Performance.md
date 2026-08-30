---
type: etf-performance
instrument_type: ETF
entity_key: Cboe BZX:EFG
ticker: EFG
exchange: Cboe BZX
fund: iShares MSCI EAFE Growth ETF
tracked_index: MSCI EAFE Growth Index (Net)
benchmark: MSCI EAFE Growth Index (Net)
management_mode: passive-index
implementation: representative-sampling
updated: 2026-08-30
performance_as_of: 2025-12-31 (official calendar) / 2026-06-30 (official standardized)
calendar_years_as_of: 2025-12-31
current_ytd_as_of: 2026-08-27
price_nav_as_of: 2026-08-28
fund_facts_as_of: 2026-08-28 / 2026-08-27 / 2026-07-31
source_batch: raw/imports/ETF_performance_sources_2026-08-30.md
return_basis: NAV total return; dividends and distributions reinvested; net of expenses
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/EFG
  - geography/International
---

# EFG Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

EFG เป็น passive developed-markets growth ETF ที่ติดตาม MSCI EAFE Growth Index
(Net) สำหรับหุ้น large-/mid-cap นอกสหรัฐฯ และแคนาดา. Official NAV Total Return
จาก official iShares sources ให้ช่วง 2016-2025 สะสม `99.67%` หรือ rounded-input
CAGR `7.16%`; มีปีบวก/ลบ `7 / 3`. Official rolling 10-year NAV TR อยู่ที่
`8.43%` ณ 2026-06-30 และ current official NAV TR YTD ล่าสุดที่ตรวจได้คือ
`11.08%` ณ 2026-08-27.

## Performance check

- `entity_key: Cboe BZX:EFG`; fund `iShares MSCI EAFE Growth ETF`; inception `2005-08-01`; exchange `Cboe BZX`; asset class `equity`.
- Tracked index and strategy-aligned benchmark: `MSCI EAFE Growth Index (Net)`, a growth-style subset of the MSCI EAFE developed-markets index outside the U.S. and Canada, generally representing approximately 50% of the parent index's free-float-adjusted market capitalization.
- Metric: `NAV Total Return` in USD, including reinvested dividends/distributions and net of expenses. Market-price returns are kept separate.
- Current official snapshot as of 2026-08-28: NAV `US$124.68`, closing price `US$125.02`, net assets `US$17.06B`, premium/discount `0.27%`, and 136.8 million shares outstanding. Holdings were `358` as of 2026-08-27. Official NAV TR YTD is `+11.08%` as of 2026-08-27.
- Current fund facts: expense ratio `0.34%` (`0.34%` management fee + `0.00%` other expenses), semi-annual distributions, 30-day SEC yield `1.19%`, 12-month trailing yield `2.27%` as of 2026-07-31, 3-year beta `0.89`, and 3-year standard deviation `14.93%` as of 2026-07-31.
- Official rolling performance as of 2026-06-30: NAV TR 1-year `13.50%`, 3-year `11.32%`, 5-year `4.81%`, 10-year `8.43%`, and since inception `6.24%`; corresponding benchmark returns are `13.65%`, `11.45%`, `4.88%`, `8.61%`, and `6.44%`.
- 10-year calendar window: `2015-12-31` to `2025-12-31`; rounded-input NAV TR CAGR `7.16%`; official issuer rolling 10-year NAV TR is `8.43%` as of 2026-06-30. Calendar CAGR formula: `(End TR / Start TR)^(1 / Years) - 1`.
- Benchmark source gap: the reviewed official product table exposes benchmark calendar rows for 2021-2025, while the reviewed summary prospectus supplies fund rows for 2016-2020 but does not provide a readable matching annual benchmark series for those years. The 2016-2020 benchmark values are not backfilled or inferred.

| Year / window | EFG NAV TR | Tracked benchmark | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | -3.34% | not disclosed in reviewed EFG table | 11.96% |
| 2017 | 28.50% | not disclosed in reviewed EFG table | 21.83% |
| 2018 | -13.02% | not disclosed in reviewed EFG table | -4.38% |
| 2019 | 27.60% | not disclosed in reviewed EFG table | 31.49% |
| 2020 | 17.98% | not disclosed in reviewed EFG table | 18.40% |
| 2021 | 10.95% | 11.25% | 28.71% |
| 2022 | -22.93% | -22.95% | -18.11% |
| 2023 | 17.24% | 17.58% | 26.29% |
| 2024 | 1.46% | 2.05% | 25.02% |
| 2025 | 20.70% | 20.76% | 17.88% |
| 2016-2025 cumulative | 99.67% | not calculated | 298.33% |
| 2016-2025 CAGR | 7.16% | not calculated | 14.82% |
| 2021-2025 cumulative | 22.77% | 24.21% | 96.17% |
| 2021-2025 CAGR | 4.19% | 4.43% | 14.43% |

**Up years / Down years — complete 2016-2025 window**

- Up years / Down years: `7 / 3`.
- Best: 2017, `+28.50%`.
- Least positive: 2024, `+1.46%`.
- Worst: 2022, `-22.93%`.
- Least bad down year: 2018, `-13.02%`.
- Annual-return population standard deviation: `16.51%`.
- Current official NAV TR YTD: `+11.08%` as of 2026-08-27; no synchronized current S&P 500 comparison is inferred.

## Risk read-through

The official iShares snapshot reports 3-year beta `0.89` and standard deviation
`14.93%` as of 2026-07-31, with `358` holdings as of 2026-08-27. Sector exposure
was led by industrials `28.97%`, information technology `18.26%`, health care
`12.93%`, and financials `12.10%`; Japan was `23.21%` of geographic exposure on
the same August 27 snapshot. These are issuer snapshot fields, not a substitute
for a daily NAV series. Compatible official daily NAV history sufficient to
calculate maximum drawdown, recovery duration, downside capture, or full tracking
error was not verified. Main risks are growth-style valuation, foreign currency,
developed-country, sector, large-/mid-cap, market, tracking-error, systematic
fair-value timing, securities-lending, and ETF premium/discount risks.

## Tracking / implementation read-through

- `management_mode`: `passive-index`; the fund uses representative sampling and does not seek to beat the MSCI EAFE Growth Index.
- The official prospectus describes a general 80% investment policy in index components or substantially identical securities, representative sampling, and a goal of tracking the index before fees and expenses.
- Official 2021-2025 fund-minus-benchmark differences are `-0.30, +0.02, -0.34, -0.59, -0.06 pp`; EFG beat the tracked index in `1/5` calendar years. The rounded-input 2021-2025 relative wealth is `-1.16%` versus the benchmark.
- The official rolling 10-year NAV TR was `0.18 pp` below the benchmark as of 2026-06-30. Expense drag, transaction costs, cash, withholding taxes, sampling, and systematic fair-value timing can create tracking differences.
- S&P 500 TR is a common cross-ETF reference only and is not EFG's tracked index. EFG beat that common reference in `2/10` complete calendar years, but this is not active-management evidence.

## Sources

- [iShares EFG product page](https://www.ishares.com/us/products/239622/ishares-msci-eafe-growth-etf) — official identity, Cboe BZX listing, inception, benchmark, current NAV/YTD, assets, holdings, price, premium/discount, rolling performance, 2021-2025 calendar rows, exposures, and fees.
- [iShares EFG summary prospectus](https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-eafe-growth-etf-7-31.pdf) — official objective, 0.34% expenses, 23% turnover, representative-sampling/indexing strategy, 2016-2020 annual NAV rows, and risk disclosures.
- [iShares EFG factsheet](https://www.ishares.com/us/literature/fact-sheet/efg-ishares-msci-eafe-growth-etf-fund-fact-sheet-en-us.pdf) — official 2026-06-30 fund facts, benchmark, holdings, and risk metrics.
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached `check-etf-performance` references — common USD Total Return benchmark for complete 2016-2025 calendar years.
- [[ETF_performance_sources_2026-08-30]] | [[ETF Performance Index]]
