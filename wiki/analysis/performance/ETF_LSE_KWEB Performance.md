---
type: etf-performance
instrument_type: ETF
entity_key: LSE:KWEB
ticker: KWEB
input_ticker: KRANF
exchange: London Stock Exchange
fund: KraneShares CSI China Internet UCITS ETF USD
tracked_index: CSI Overseas China Internet Index (USD)
benchmark: S&P 500 Total Return
updated: 2026-07-26
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/KRANF
  - ticker/KWEB
  - geography/China
---

# KRANF / KWEB Performance

> Navigation: [[ETF Region Index]] → [[China ETF]] → [[ETF Performance Index]]

## Bottom line

Input `KRANF` is an OTC alias for the USD UCITS share class whose official
exchange-qualified listing is `LSE:KWEB` (`KWEB LN`, ISIN `IE00BFXR7892`). The
same share class is also listed on Euronext Amsterdam as `KWEB NA`. This is not
the US-listed KraneShares CSI China Internet ETF, which has a different ISIN;
the two products are kept separate.

The fund is a passive, physical, index-tracking China internet equity UCITS ETF
tracking the `CSI Overseas China Internet Index`. The USD share class launched
on `2018-11-21`, so `10-year NAV TR unavailable`. Official Fund NAV TR since
inception is `-26.60%` cumulative / `-3.98%` annualized through `2026-06-30`.
Current official NAV TR YTD is `-28.96%` as of `2026-06-30`; the latest daily
USD-share-class NAV shown by the issuer is `US$19.82` as of `2026-07-24`.

## Performance check

- entity_key: `LSE:KWEB`
- Input alias: `KRANF`; official USD share-class ticker: `KWEB LN`
- ISIN: `IE00BFXR7892`
- Share-class launch: `2018-11-21`; fund launch date in the KIID: `2018-11-20`
- Structure: passive, physical/replicated, accumulating China internet equity
  UCITS ETF; normal policy invests at least 80% in index securities or related
  depositary receipts
- Tracked index: `CSI Overseas China Internet Index (USD)`
- Metric: official Fund NAV performance; income is reinvested, and the issuer's
  growth-of-USD-10,000 methodology deducts fund expenses. The KIID performance
  chart includes tax, ongoing charges and portfolio transaction costs.
- Ongoing expense: `0.75%`
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference,
  not the fund's tracked index)
- 10-year NAV TR: `unavailable`; verified history is only `7.605749` years and
  has fewer than 10 complete calendar years

### Available-period NAV TR

Raw issuer NAV index endpoints are not disclosed. The end value below is a
normalized value derived from the official since-inception cumulative return.

| Window | Start date | End date | Start TR value | End TR value | Actual years | Cumulative NAV TR | CAGR |
|---|---|---|---:|---:|---:|---:|---:|
| Available since inception | 2018-11-21 | 2026-06-30 | 100.00 (normalized) | 73.40 (official cumulative, normalized) | 7.605749 | -26.60% (official) | -3.98% (official; derived -3.9844%) |

Calculation: `100 × (1 - 0.2660) = 73.40`; derived CAGR is
`(73.40 / 100)^(1 / 7.605749) - 1 = -3.9844%`, which rounds to the issuer's
reported `-3.98%`. This is available-period performance, not 10-year
performance.

### Annual NAV TR and S&P 500 Total Return

The current KIID provides annual USD share-class performance for complete
calendar years `2019-2025`; `2018` is a partial inception year and has no annual
row. The KIID also discloses a correction to the 2019 values; the corrected
values below are used.

| Year | KWEB NAV TR | CSI Overseas China Internet Index TR | S&P 500 TR |
|---|---:|---:|---:|
| 2018 | not disclosed (partial inception year) | not disclosed | -4.38% |
| 2019 | 28.20% | 29.20% | 31.49% |
| 2020 | 59.50% | 60.90% | 18.40% |
| 2021 | -49.20% | -49.00% | 28.71% |
| 2022 | -16.40% | -16.40% | -18.11% |
| 2023 | -9.90% | -10.00% | 26.29% |
| 2024 | 13.20% | 11.90% | 25.02% |
| 2025 | 23.80% | 23.30% | 17.88% |
| 2026 YTD | -28.96% as of 2026-06-30 | -29.41% as of 2026-06-30 | not comparable; current YTD not cached |

From the complete calendar rows `2019-2025`, KWEB compounds to `9.65%` and a
`1.32%` CAGR; the cached S&P 500 TR compounds to `205.41%` and a `17.29%` CAGR.
For the common `2021-2025` window, KWEB is `-46.38%` cumulative / `-11.72%`
CAGR versus S&P `96.17%` / `14.43%` CAGR. These calendar comparisons are kept
separate from the official since-inception window because the latter begins on
`2018-11-21`.

## Up years / Down years

- Up years / Down years: `4 / 3` over complete calendar years `2019-2025`
- Best: `2020`, `+59.50%`
- Least positive: `2024`, `+13.20%`
- Worst: `2021`, `-49.20%`
- Least bad down year: `2023`, `-9.90%`
- Official current YTD: `-28.96%` as of `2026-06-30`

## Risk read-through

กองทุนมี concentration ใน China internet และบริษัทเทคโนโลยี/consumer internet
ที่จดทะเบียนใน Hong Kong และสหรัฐฯ จึงมี China regulatory, geopolitical, ADR,
currency, emerging-market liquidity, valuation และ sector-concentration risk.
The fund is a UCITS ETF and the USD share class is accumulating; market-price
return remains separate from NAV TR. Daily NAV TR drawdown and recovery dates:
`ไม่พบข้อมูลที่ยืนยันได้` จาก official capture นี้.

## Sources

- [Official KraneShares Europe KWEB UCITS product and performance page](https://kraneshares.eu/etf/kwebln/) — identity, USD share class, listings, ISIN, inception, passive structure, index, expense, NAV TR windows, current NAV/YTD and as-of dates
- [Official current KWEB USD KIID](https://kraneshares.eu/resources/compliance/kiids/2026_02_20_kwebln_kiid_english_usd.pdf) — passive/index policy, income reinvestment, expenses, corrected 2019-2025 annual performance rows and launch dates
- [Official KraneShares 2025 annual financial report](https://kraneshares.eu/resources/compliance/2026_01_29_europe_annual.financials.and.other.information.pdf) — fiscal-year NAV performance cross-check and fund/index methodology
- [Official London Stock Exchange KWEB page](https://www.londonstockexchange.com/stock/KWEB/kraneshares-icav/company-page) — official exchange-qualified USD listing identity cross-check
- [OTC identity bridge for KRANF](https://stockanalysis.com/quote/otc/KRANF/) — secondary alias/name/inception cross-check only; not used as the performance metric
- [Official S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached source-batch convention — common USD total-return reference
- ETF source batch: [[ETF_performance_sources_2026-07-24]] | [[ETF Performance Index]]
