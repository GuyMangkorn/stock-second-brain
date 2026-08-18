---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:FLGB
input_ticker: FLGB
ticker: FLGB
exchange: NYSE Arca
fund: Franklin FTSE United Kingdom ETF
tracked_index: FTSE UK Capped Index
benchmark: S&P 500 Total Return
updated: 2026-08-18
performance_as_of: 2025-12-31
rolling_10y_as_of: not-applicable-lt-10y
current_ytd_as_of: 2026-07-30
price_nav_as_of: 2026-07-30
fund_facts_as_of: 2026-07-30
source_batch: raw/imports/ETF_performance_sources_2026-08-18.md
return_basis: NAV total return; distributions reinvested; fund expenses reflected in NAV
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/FLGB
  - geography/United-Kingdom
---

# FLGB Performance

> Navigation: [[ETF Region Index]] → [[United Kingdom ETF]] → [[ETF Performance Index]]

## Bottom line

`FLGB` คือ Franklin FTSE United Kingdom ETF ที่จดทะเบียนบน NYSE Arca และเป็น
`passive-index` equity ETF ซึ่งติดตาม `FTSE UK Capped Index`. กองทุนเริ่มในปี
2017 จึงยังไม่มี 10-year NAV CAGR ที่ใช้ได้. Official complete calendar NAV TR
ปี 2018-2025 compound ได้ `74.10%` หรือ rounded-input CAGR `7.18%`; ช่วง
2021-2025 ได้ `82.62%` หรือ `12.80%` ต่อปี. Latest official NAV TR YTD คือ
`11.56%` ณ 30 ก.ค. 2026.

## Performance check

- `entity_key: NYSE Arca:FLGB`; official fund name, ticker and exchange are confirmed by Franklin Templeton. Fund inception: 2 พ.ย. 2017.
- Classification: `passive-index` / indexed equity. The objective is to track the FTSE UK RIC Capped Index, also referred to by the issuer as the FTSE UK Capped Index, covering UK large- and mid-capitalization stocks.
- Metric: issuer `NAV Return` includes reinvested distributions and deduction of fund expenses. Market-price return is kept separate from the NAV series.
- Issuer benchmark: `FTSE UK Capped Index`; `S&P 500 Total Return` is a common USD reference benchmark, not the tracked index.
- Expense ratio: `0.09%`; index reconstitution: semi-annual; distribution frequency: semi-annual.
- Official rolling fields as of 30 มิ.ย. 2026: NAV 1-year `18.81%`, 3-year `17.46%`, 5-year `11.51%`, since inception `8.04%`; 10-year is `not applicable` because the fund launched in 2017.
- Latest official issuer snapshot as of 30 ก.ค. 2026: NAV `$37.16`, total net assets `$895.52m`, and 96 holdings. The reviewed page did not expose a separate current market-price quote, so no current market price is inferred.
- Annual coverage: official complete calendar NAV rows are 2018-2025; 2017 is an inception-year partial period and is excluded from complete-year calculations.

| Year | FLGB NAV TR (USD) | FTSE UK Capped Index-NR (USD) | S&P 500 TR (USD) |
|---|---:|---:|---:|
| 2018 | -14.65% | -14.58% | -4.38% |
| 2019 | 22.57% | 22.80% | 31.49% |
| 2020 | -8.87% | -8.94% | 18.40% |
| 2021 | 17.15% | 17.25% | 28.71% |
| 2022 | -6.92% | -6.91% | -18.11% |
| 2023 | 15.37% | 15.49% | 26.29% |
| 2024 | 8.85% | 8.99% | 25.02% |
| 2025 | 33.36% | 33.54% | 17.88% |

Official FLGB NAV TR rows compound to `74.10%` / rounded-input CAGR `7.18%`
for 2018-2025 and `82.62%` / `12.80%` for 2021-2025. The linked issuer index
rows compound to `75.24%` / `7.26%` and `83.47%` / `12.90%`, respectively; the
rounded-input tracking differences are approximately `-0.09 pp` and `-0.10 pp`
and are not alpha. The cached S&P 500 TR rows compound to `192.03%` / `14.33%`
for 2018-2025 and `96.17%` / `14.43%` for 2021-2025. FLGB trails the common
five-year S&P reference by approximately `-1.63 pp` of rounded-input CAGR.

## Up years / Down years

- Complete 2018-2025 NAV TR up/down: `5 / 3`
- Best NAV TR year: 2025, `+33.36%`
- Least positive year: 2024, `+8.85%`
- Worst NAV TR year: 2018, `-14.65%`
- Least bad down year: 2022, `-6.92%`
- Current official NAV TR YTD: `+11.56%` as of 30 ก.ค. 2026.

## Risk read-through

Franklin reports 3-year standard deviation of `12.41%` for FLGB versus `12.43%`
for the benchmark as of 31 มี.ค. 2026. The current portfolio had 96 holdings as
of 30 ก.ค. 2026; sector weights as of 29 ก.ค. 2026 were Financials `26.96%`,
Consumer Staples `14.59%`, Industrials `14.25%`, Health Care `12.71%`, and
Energy `10.82%`. UK/country, GBP/USD, sector concentration, Brexit/trade and
large-cap/liquidity risks remain relevant. Official daily NAV maximum drawdown
and recovery date were not disclosed in the reviewed capture, so
`risk-adjusted evidence: not-verified` for those fields. The low 0.09% fee and
small NAV-to-index gaps support efficient passive tracking, but do not remove
country or currency risk.

## Sources

- [Franklin Templeton FLGB product page](https://www.franklintempleton.com/investments/options/exchange-traded-funds/products/26350/SINGLCLASS/franklin-ftse-united-kingdom-etf/FLGB) — official identity, exchange, objective, current NAV/YTD, rolling returns, fee, holdings, sectors and risk snapshot
- [Franklin Templeton FLGB factsheet](https://www.franklintempleton.com/forms-literature/download/FLGB-FF) — official 2018-2025 NAV/index calendar rows, return definitions, risk statistics and fund facts as of March 31, 2026
- [Franklin Templeton FLGB summary prospectus](https://www.franklintempleton.com/forms-literature/download-preview/FLGB-PSUM) — official objective, passive indexed structure, risks and benchmark definitions
- [Franklin Templeton FLGB annual shareholder report](https://www.franklintempleton.com/forms-literature/download-preview/FLGB-ATSR) — official fiscal-year performance comparison through March 31, 2026
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- Cached S&P 500 TR references: [2016-2019](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [2018-2022](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), [2021](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/), and [2022-2025](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/)
- ETF source batch: [[ETF_performance_sources_2026-08-18]] | [[ETF Performance Index]]
