---
type: etf-performance
instrument_type: ETF
entity_key: Cboe BZX:EZU
input_ticker: EZU
ticker: EZU
exchange: Cboe BZX
fund: iShares MSCI Eurozone ETF
tracked_index: MSCI EMU Index (Net)
benchmark: S&P 500 Total Return
updated: 2026-08-18
performance_as_of: 2025-12-31
rolling_10y_as_of: 2026-06-30
current_ytd_as_of: 2026-08-14
price_nav_as_of: 2026-08-14
fund_facts_as_of: 2026-08-14
source_batch: raw/imports/ETF_performance_sources_2026-08-18.md
return_basis: NAV total return; gross income reinvested; fund expenses reflected in NAV
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/EZU
  - geography/Europe
---

# EZU Performance

> Navigation: [[ETF Region Index]] → [[Europe ETF]] → [[ETF Performance Index]]

## Bottom line

`EZU` คือ iShares MSCI Eurozone ETF ที่จดทะเบียนบน Cboe BZX และเป็น USD
unhedged share class. กองทุนเป็น `passive-index` equity ETF ที่ติดตาม
`MSCI EMU Index (Net)` โดยลงทุนในหุ้น large- และ mid-cap ของประเทศ Eurozone
และไม่มี currency-hedge overlay แบบ `HEZU`. Official 2021-2025 NAV TR ให้
cumulative `65.48%` และ rounded-input calendar CAGR `10.60%`; issuer rolling
10-year NAV TR อยู่ที่ `10.91%` ณ 30 มิ.ย. 2026. Common USD reference อย่าง
S&P 500 TR ให้ `96.17%` / `14.43%` ในช่วงเดียวกัน. Latest official NAV TR
YTD คือ `14.20%` ณ 14 ส.ค. 2026.

## Performance check

- `entity_key: Cboe BZX:EZU`; canonical fund name and exchange are confirmed by
  the issuer product page and SEC summary prospectus. Fund inception is 25 ก.ค.
  2000 and the asset class is equity.
- Classification: `passive-index`. The prospectus says the Fund seeks to track
  `MSCI EMU Index (Net)`, uses an indexing approach and representative sampling,
  and generally invests at least 80% in index components or economically similar
  instruments. Limited derivatives may be used for tracking, not as the return
  objective.
- Metric: issuer `NAV Total Return` with reinvested distributions and fund
  expenses reflected in NAV. Market-price return is kept separate.
- Official rolling annualised fields as of 30 มิ.ย. 2026: 1-year `19.60%`,
  3-year `18.03%`, 5-year `10.24%`, 10-year `10.91%`, and since inception
  `4.73%`.
- Current official snapshot as of 14 ส.ค. 2026: NAV `$71.82`, closing price
  `$71.99`, net assets `$10.00bn`, and 220 holdings. Expense ratio is `0.50%`
  and distribution frequency is semi-annual.

| Year | EZU NAV TR (USD) | MSCI EMU Net (USD) | S&P 500 TR (USD) |
|---|---:|---:|---:|
| 2021 | 13.59% | 13.54% | 28.71% |
| 2022 | -17.28% | -17.86% | -18.11% |
| 2023 | 22.93% | 22.94% | 26.29% |
| 2024 | 2.58% | 2.64% | 25.02% |
| 2025 | 39.66% | 40.30% | 17.88% |

Official iShares calendar rows in the reviewed factsheet cover 2021-2025;
2016-2020 rows were not disclosed in that capture, so no ten-year calendar
CAGR is reconstructed. The `10.91%` ten-year figure above is the issuer's
rolling annualised NAV TR field, not the calendar-row CAGR. S&P 500 rows reuse
the cached USD Total Return convention as of 2025-12-31.

## Up years / Down years

- Complete 2021-2025 NAV TR up/down: `4 / 1`
- Best NAV TR year: 2025, `+39.66%`
- Least positive year: 2024, `+2.58%`
- Worst NAV TR year: 2022, `-17.28%`
- 2021-2025 EZU NAV TR cumulative/CAGR: `65.48%` / `10.60%`.
- 2021-2025 issuer benchmark cumulative/CAGR: `65.11%` / `10.55%`; the
  rounded-input difference is approximately `+0.04 pp` CAGR and is a passive
  tracking comparison, not alpha.
- 2021-2025 S&P 500 TR cumulative/CAGR: `96.17%` / `14.43%` as a common USD
  reference. EZU's rounded-input CAGR was approximately `3.35 pp` below it.
- Daily NAV maximum drawdown and recovery date were not disclosed in the
  reviewed official capture; no price-only proxy is substituted.

## Risk read-through

The latest issuer risk snapshot reports 3-year standard deviation `14.62%` and
beta `0.70` as of 31 ก.ค. 2026; P/E `19.36x` and P/B `2.41x` are as of 14 ส.ค.
2026, while trailing yield is `2.62%` as of 31 ก.ค. 2026. Look-through sector
exposure as of 14 ส.ค. 2026 was led by Financials `26.80%`, Industrials
`20.29%`, and Information Technology `15.95%`; country exposure was led by
France `27.83%`, Germany `25.17%`, and the Netherlands `16.85%`.

EZU leaves the USD investor exposed to EUR/USD movements, unlike HEZU's
currency-hedged structure. Eurozone equity, country, sector, valuation and
foreign-currency risk therefore remain direct return drivers. The annual
2021-2025 return population standard deviation is `19.15%`, calculated from the
five rounded NAV rows; it is not substituted for the issuer's 3-year standard
deviation.

## Sources

- [iShares MSCI Eurozone ETF product page](https://www.ishares.com/us/products/239644/EZU) — official exchange, current NAV/YTD, net assets, fees, benchmark, rolling returns, risk and exposure snapshot
- [iShares EZU factsheet, June 2026](https://www.ishares.com/us/literature/fact-sheet/ezu-ishares-msci-eurozone-etf-fund-fact-sheet-en-us.pdf) — official 2021-2025 NAV/benchmark rows, rolling returns, fees, structure and risk fields
- [EZU SEC summary prospectus](https://www.sec.gov/Archives/edgar/data/930667/000119312525336639/d31674d497k.htm) — official passive objective, index, representative sampling and tracking instruments
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- Cached S&P 500 TR references: [2016-2019](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [2018-2022](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), [2021](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/), and [2022-2025](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/)
- ETF source batch: [[ETF_performance_sources_2026-08-18]] | [[ETF Performance Index]]
