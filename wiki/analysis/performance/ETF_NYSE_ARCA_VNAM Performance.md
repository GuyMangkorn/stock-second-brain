---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:VNAM
ticker: VNAM
exchange: NYSE Arca
fund: Global X MSCI Vietnam ETF
tracked_index: MSCI Vietnam Select 25-50 Index
benchmark: S&P 500 Total Return
updated: 2026-07-26
performance_as_of: 2026-06-30
current_ytd_as_of: not disclosed
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/VNAM
  - geography/Vietnam
---

# VNAM Performance

> Navigation: [[ETF Region Index]] → [[Vietnam ETF]] → [[ETF Performance Index]]

## Bottom line

VNAM เป็น passive/index-tracking Vietnam equity ETF ที่ใช้ indexing approach เพื่อติดตาม `MSCI Vietnam Select 25-50 Index`. กองทุนเริ่มเมื่อ `2021-12-07` จึงมีประวัติประมาณ `4.561259` ปีถึง `2026-06-30` และ `10-year NAV TR unavailable`. Global X เปิดเผย official NAV total return แบบ annualized ตั้งแต่เริ่มกองทุน `0.34%` ณ `2026-06-30`; current NAV TR YTD ยัง `not disclosed` ในแหล่งที่ตรวจสอบได้.

## Performance check

- `entity_key: NYSE Arca:VNAM` (official SEC summary prospectus and Global X product page)
- Inception: `2021-12-07`; Global X launch material separately describes the NYSE Arca listing on `2021-12-09`.
- Metric: `NAV Total Return` รวม gross income ที่ reinvested where applicable และ fund expenses ตามนิยาม performance ของ issuer
- Tracked index (issuer benchmark): `MSCI Vietnam Select 25-50 Index`; index methodology/name change effective `2023-12-01` is noted in the 2026 summary prospectus.
- Expense ratio: `0.51%` total annual fund operating expenses.
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference benchmark; cached calendar rows shown below)
- 10-year NAV TR: `unavailable`; official inception is less than 10 years before the latest reviewed month-end.
- Available-period official observations (annualized, as of `2026-06-30`): 1Y `45.10%`; 3Y `15.86%`; since inception `0.34%`. Raw start/end NAV TR values are not disclosed, so no endpoint-derived cumulative return or independent CAGR is inferred.
- Actual elapsed since inception: `(2026-06-30 − 2021-12-07) / 365.25 = 4.561259` years. The issuer's `0.34%` is retained as its reported since-inception annualized NAV TR, not relabelled as a 10-year result.
- Coverage/source note: no complete calendar-year NAV TR rows were available in the reviewed official capture. S&P 500 rows reuse the cached USD Total Return convention as of `2025-12-31`; they are not a same-window rolling comparison to the 1Y/3Y/since-inception observations.

| Year | ETF NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | not applicable; before inception | 11.96% |
| 2017 | not applicable; before inception | 21.83% |
| 2018 | not applicable; before inception | -4.38% |
| 2019 | not applicable; before inception | 31.49% |
| 2020 | not applicable; before inception | 18.40% |
| 2021 | not disclosed; incomplete inception year | 28.71% |
| 2022 | not disclosed | -18.11% |
| 2023 | not disclosed | 26.29% |
| 2024 | not disclosed | 25.02% |
| 2025 | not disclosed | 17.88% |
| 2026 YTD | not disclosed | not comparable; current year not cached |

**Up years / Down years**

- Up years / Down years: not disclosed; complete annual NAV TR rows are unavailable.
- Best: not disclosed
- Least positive: not disclosed
- Worst: not disclosed
- Least bad down year: not disclosed
- Current YTD: `not disclosed` as of `2026-07-26`; the official Global X page's latest performance table is as of `2026-06-30` and does not include a YTD column.

## Risk read-through

The available-period signal is the issuer-reported since-inception NAV TR annualized `0.34%`, with no valid 10-year CAGR. VNAM is a non-diversified, single-country Vietnam equity ETF with `70` holdings; Global X reports sector exposure of real estate `32.1%` and financials `29.2%` as of `2026-06-30`, and the largest holding was `23.61%` as of `2026-07-17`. Official risk statistics show standard deviation `24.40%` as of `2026-06-30`. Country, frontier/emerging-market liquidity, FX, foreign-ownership, custody, political/regulatory, and sector-concentration risks are material. Market-price return is kept separate from NAV TR.

## Sources

- [Global X VNAM official product/performance page](https://www.globalxetfs.com/funds/vnam?download_full_holdings=true) — objective, index, inception, expense, official NAV TR observations, holdings, exposure, and as-of dates.
- [SEC 2026 Summary Prospectus](https://www.sec.gov/Archives/edgar/data/1432353/000143235326000195/a497kmscivietnam.htm) — `NYSE Arca:VNAM`, passive/indexing approach, expense ratio, index methodology, and risks.
- [Global X launch article](https://www.globalxetfs.com/articles/introducing-the-global-x-msci-vietnam-etf-vnam) — listing-date cross-check.
- [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — benchmark definition; annual rows reuse the cached convention.
- ETF source batch: [[ETF_performance_sources_2026-07-24]] | [[ETF Performance Index]]
