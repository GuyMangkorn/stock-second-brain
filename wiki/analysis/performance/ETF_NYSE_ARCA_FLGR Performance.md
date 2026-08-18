---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:FLGR
input_ticker: FLGR
ticker: FLGR
exchange: NYSE Arca
fund: Franklin FTSE Germany ETF
tracked_index: FTSE Germany Capped Index
benchmark: S&P 500 Total Return
updated: 2026-08-18
performance_as_of: 2025-12-31
rolling_10y_as_of: not-applicable-lt-10y
current_ytd_as_of: 2026-08-07
price_nav_as_of: 2026-08-07
fund_facts_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-08-18.md
return_basis: NAV total return; distributions reinvested; fund expenses reflected in NAV
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/FLGR
  - geography/Germany
---

# FLGR Performance

> Navigation: [[ETF Region Index]] → [[Germany ETF]] → [[ETF Performance Index]]

## Bottom line

`FLGR` คือ Franklin FTSE Germany ETF ที่จดทะเบียนบน NYSE Arca และเป็น
`passive-index` equity ETF ซึ่งติดตาม `FTSE Germany RIC Capped Index`.
Official complete-calendar NAV TR ปี 2018-2025 compound ได้ `63.92%` หรือ
rounded-input CAGR `6.37%`; ช่วง 2021-2025 ได้ `54.03%` หรือ `9.02%` ต่อปี.
มีปีบวก/ลบ `7/1`, best คือ 2025 `+36.70%`, worst คือ 2022 `-22.10%` และ
latest official NAV TR YTD คือ `+5.23%` ณ 7 ส.ค. 2026. Inception ปี 2017
ทำให้ยังไม่มี 10-year NAV CAGR ที่ใช้ได้.

## Performance check

- `entity_key: NYSE Arca:FLGR`; official fund name, ticker and exchange are confirmed by Franklin Templeton. Fund inception: 2 พ.ย. 2017.
- Classification: `passive-index` / indexed equity. กองทุนมุ่งติดตาม FTSE Germany RIC Capped Index ซึ่งเป็นดัชนีหุ้นเยอรมนี large- และ mid-capitalization; prospectus อนุญาต derivatives เพื่อ equitize cash, settlement หรือ tracking แต่ payoff หลักยังเป็น long German equity.
- Metric: issuer `NAV Return` รวม reinvested distributions และหัก fund expenses; market-price return แยกจาก NAV series.
- Issuer benchmark: `FTSE Germany Capped Index-NR`; `S&P 500 Total Return` เป็น common USD reference benchmark ไม่ใช่ tracked index.
- Expense ratio: `0.09%`; index reconstitution: semi-annual; distribution frequency: semi-annual.
- Official rolling fields ณ 30 มิ.ย. 2026: NAV 1-year `0.31%`, 3-year annualized `16.26%`, 5-year annualized `6.90%`, since inception annualized `5.69%`; 10-year เป็น `not applicable` เพราะกองทุนเริ่มในปี 2017.
- Latest official product-page snapshot ณ 7 ส.ค. 2026: NAV `$34.29`, NAV TR YTD `5.23%`; total net assets `$39.43m` ณ 9 ส.ค. 2026. Factsheet ณ 30 มิ.ย. 2026 ระบุ 69 holdings.
- Annual coverage: official complete calendar NAV rows คือ 2018-2025; 2017 เป็น inception-year partial และไม่รวมในการจัดอันดับ.

| Year | FLGR NAV TR (USD) | FTSE Germany Capped Index-NR (USD) | S&P 500 TR (USD) |
|---|---:|---:|---:|
| 2018 | -22.07% | -22.42% | -4.38% |
| 2019 | 21.67% | 21.34% | 31.49% |
| 2020 | 12.24% | 11.95% | 18.40% |
| 2021 | 5.29% | 5.10% | 28.71% |
| 2022 | -22.10% | -22.42% | -18.11% |
| 2023 | 24.12% | 23.68% | 26.29% |
| 2024 | 10.68% | 10.42% | 25.02% |
| 2025 | 36.70% | 36.38% | 17.88% |

Coverage/source note: annual FLGR and FTSE rows are official Franklin factsheet
rows as of 30 มิ.ย. 2026; 2017 partial is omitted. S&P 500 rows are the cached
USD total-return convention, dividends reinvested, as of 31 ธ.ค. 2025.

Official FLGR rows compound to `63.92%` / rounded-input CAGR `6.37%` for
2018-2025 and `54.03%` / `9.02%` for 2021-2025. The linked FTSE index rows
compound to `60.04%` / `6.05%` and `51.86%` / `8.72%`; the approximate
fund-minus-index differences of `+0.32 pp` and `+0.30 pp` are rounded-input
passive tracking observations, not alpha. Cached S&P 500 TR compounds to
`192.03%` / `14.33%` for 2018-2025 and `96.17%` / `14.43%` for 2021-2025;
FLGR trails that common reference by approximately `-7.96 pp` and `-5.41 pp`.

**Up years / Down years**

- Complete 2018-2025 NAV TR up/down: `7 / 1`
- Best NAV TR year: 2025, `+36.70%`
- Least positive year: 2021, `+5.29%`
- Worst NAV TR year: 2022, `-22.10%`
- Least bad down year: 2022, `-22.10%`
- Current official NAV TR YTD: `+5.23%` as of 7 ส.ค. 2026.

## Risk read-through

Franklin reports 3-year standard deviation of `16.66%` for FLGR versus
`16.59%` for the FTSE benchmark as of 30 มิ.ย. 2026. The factsheet listed 69
holdings; sector weights were Industrials `31.02%`, Financials `22.81%`, and
Information Technology `14.74%` at the same date. Germany/country, EUR/USD,
export-cycle, sector concentration and possible non-diversification risks are
material. Official daily NAV maximum drawdown and recovery date were not
disclosed in the reviewed sources, so `risk-adjusted evidence: not-verified`
for those fields. The `0.09%` fee and close index relationship support
efficient passive implementation but do not remove country or currency risk.

## Sources

- [Franklin Templeton FLGR product page](https://www.franklintempleton.com/investments/options/exchange-traded-funds/products/26360/SINGLCLASS/franklin-ftse-germany-etf/FLGR) — official identity, exchange, objective, current NAV/YTD, rolling returns, fee and risk snapshot
- [Franklin Templeton FLGR factsheet](https://www.franklintempleton.com/forms-literature/download/FLGR-FF) — official 2018-2025 NAV/index calendar rows, return definitions, risk statistics and fund facts as of June 30, 2026
- [Franklin Templeton passive ETF prospectus](https://www.franklintempleton.com/forms-literature/download/ETF5-P) — official objective, fees, passive strategy and permitted tracking/settlement derivatives
- [Franklin Templeton FLGR annual report](https://www.franklintempleton.com/tools-and-resources/literature/info/FLGR-ATSR) — official fiscal-year performance context
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- Cached S&P 500 TR references: [2016-2019](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [2018-2022](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), [2021](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/), and [2022-2025](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/)
- ETF source batch: [[ETF_performance_sources_2026-08-18]] | [[ETF Performance Index]]
