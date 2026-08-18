---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:FEZ
input_ticker: FEZ
ticker: FEZ
exchange: NYSE Arca
fund: State Street SPDR EURO STOXX 50 ETF
tracked_index: EURO STOXX 50 Index
benchmark: S&P 500 Total Return
updated: 2026-08-18
performance_as_of: 2025-12-31
rolling_10y_as_of: 2026-07-31
current_ytd_as_of: 2026-07-31
price_nav_as_of: 2026-08-17
fund_facts_as_of: 2026-08-18
source_batch: raw/imports/ETF_performance_sources_2026-08-18.md
return_basis: NAV total return where issuer-reported; secondary annual proxy is dividend-reinvested total return
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/FEZ
  - geography/Europe
---

# FEZ Performance

> Navigation: [[ETF Region Index]] → [[Europe ETF]] → [[ETF Performance Index]]

## Bottom line

`FEZ` คือ State Street SPDR EURO STOXX 50 ETF ที่จดทะเบียนบน NYSE Arca และเป็น
`passive-index` equity ETF. Official rolling `10-year NAV Total Return CAGR`
อยู่ที่ `10.92%` ณ 31 ก.ค. 2026 และ official NAV TR YTD อยู่ที่ `9.66%` ณ วันเดียวกัน.
Annual calendar rows 2016-2025 ที่ตรวจสอบได้เป็น secondary
dividend-reinvested total-return proxy จึงแยกจาก official NAV evidence และไม่ใช้
ใน strict common-window ranking.

## Performance check

- `entity_key: NYSE Arca:FEZ`; fund name, exchange and ticker are confirmed by State Street. Inception: 15 ต.ค. 2002.
- Classification: `passive-index`; the fund seeks to track the total-return performance of the `EURO STOXX 50 Index` before fees and expenses.
- Metric: issuer `NAV Total Return` รวมเงินปันผลและ capital gains ที่ reinvested และแสดง net of fund fees; annual table below is a secondary dividend-reinvested total-return proxy (`*`), not issuer NAV rows.
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference benchmark). Issuer benchmark remains `EURO STOXX 50 Index`.
- Expense ratio: `0.29%` gross; distribution frequency: quarterly; fund facts as of 18 ส.ค. 2026.
- 10-year window: issuer rolling field as of 31 ก.ค. 2026; raw endpoint values are `not disclosed` on the reviewed official page.
- 10-year NAV TR CAGR: `10.92%` (issuer-reported annualised field; no endpoint reconstruction).
- Coverage/source note: official issuer rolling/YTD fields are kept separate from the secondary annual proxy. S&P 500 rows reuse the cached USD convention as of 31 ธ.ค. 2025.

| Year | FEZ total-return proxy* (USD) | S&P 500 TR (USD) |
|---|---:|---:|
| 2016 | 0.67% | 11.96% |
| 2017 | 24.80% | 21.83% |
| 2018 | -15.86% | -4.38% |
| 2019 | 26.05% | 31.49% |
| 2020 | 4.84% | 18.40% |
| 2021 | 14.84% | 28.71% |
| 2022 | -14.27% | -18.11% |
| 2023 | 27.16% | 26.29% |
| 2024 | 3.58% | 25.02% |
| 2025 | 37.81% | 17.88% |

`*` Secondary rows include price appreciation plus reinvested dividends; they
are not relabelled as official NAV TR. The complete proxy window compounds to
`149.64%` / rounded-input CAGR `9.58%`; 2021-2025 compounds to `78.70%` /
`12.31%`. The cached S&P 500 2016-2025 cumulative return is `298.33%` /
`14.82%` CAGR from rounded annual inputs.

**Up years / Down years**

- Proxy up/down years: `8 / 2`
- Best: 2025, `+37.81%*`
- Least positive: 2016, `+0.67%*`
- Worst: 2018, `-15.86%*`
- Least bad down year: 2022, `-14.27%*`
- Current official NAV YTD: `+9.66%` as of 31 ก.ค. 2026; latest official NAV `71.95` and closing price `71.91` as of 17 ส.ค. 2026.

## Risk read-through

The official rolling 10-year NAV TR CAGR is `10.92%`; the annual proxy's
population standard deviation is `17.24%`, calculated from the ten rounded
secondary rows and not presented as official NAV risk evidence. The portfolio
had 50 holdings as of 14 ส.ค. 2026, with Financials `28.44%`, Industrials
`22.29%`, and Information Technology `15.07%`; country/sector concentration
and EUR/USD exposure remain relevant for a USD investor. Official daily NAV
maximum drawdown and recovery date were not disclosed in the reviewed capture,
so `risk-adjusted evidence: not-verified` for those fields. The fund's 0.29%
expense ratio and quarterly distributions also create tracking drag versus the
issuer index.

## Sources

- [State Street FEZ product page](https://www.ssga.com/us/en/intermediary/etfs/state-street-spdr-euro-stoxx-50-etf-fez) — official identity, exchange, current NAV/price, YTD, rolling returns, fee, holdings and fund facts
- [State Street FEZ factsheet, June 2026](https://www.ssga.com/library-content/products/factsheets/etfs/us/factsheet-us-en-fez.pdf) — official return definitions, fee, index objective and fund structure
- [State Street SPDR dividend distributions](https://www.ssga.com/us/en/intermediary/resources/documents/etf-dividend-distributions) — official distribution-source context
- [FEZ performance history](https://www.financecharts.com/etfs/FEZ/performance) — secondary dividend-reinvested annual proxy rows
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- Cached S&P 500 TR references: [2016-2019](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [2018-2022](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), [2021](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/), and [2022-2025](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/)
- ETF source batch: [[ETF_performance_sources_2026-08-18]] | [[ETF Performance Index]]
