---
type: etf-performance
instrument_type: ETF
entity_key: LSE:FTEU
input_ticker: FTDPF
ticker: FTEU
exchange: London Stock Exchange
fund: First Trust Eurozone AlphaDEX UCITS ETF
tracked_index: Nasdaq AlphaDEX Eurozone NTR Index
benchmark: S&P 500 Total Return
updated: 2026-08-18
performance_as_of: 2025-12-31
rolling_10y_as_of: 2026-07-27
current_ytd_as_of: 2026-07-30
price_nav_as_of: 2026-07-30
fund_facts_as_of: 2026-05-29
source_batch: raw/imports/ETF_performance_sources_2026-08-18.md
return_basis: NAV total return; secondary USD total-return fields marked *
return_currency: USD for FTEU secondary line; EUR for official Acc EUR factsheet
tags:
  - analysis/etf-performance
  - ticker/FTEU
  - ticker/FTDPF
  - geography/Europe
---

# FTEU Performance

> Navigation: [[ETF Region Index]] → [[Europe ETF]] → [[ETF Performance Index]]

## Bottom line

`FTDPF` เป็น OTC input alias ของ official USD London Stock Exchange line
`LSE:FTEU` สำหรับ First Trust Eurozone AlphaDEX UCITS ETF (ISIN
`IE00B8X9NY41`). กองทุนเป็น passive, physically replicated, accumulating UCITS
equity ETF ที่ติดตาม `Nasdaq AlphaDEX Eurozone NTR Index`. ชุด annual USD
total-return ที่ตรวจสอบได้จาก secondary source ครบ 2021-2025 ให้ cumulative
`71.57%*` และ CAGR `11.40%*`, เทียบ S&P 500 TR ที่ `96.17%` / `14.43%`; มี
4 ปีบวก / 1 ปีลบ. ปีดีที่สุดคือ 2025 ที่ `+57.98%*` และแย่ที่สุดคือ 2022 ที่
`-19.74%*`. Latest USD YTD secondary field คือ `+12.31%*` ณ 30 ก.ค. 2026.
Official factsheet reports the same ISIN's Acc EUR share-class YTD `13.39%`
and since-inception annualised `10.68%` ณ 29 พ.ค. 2026; those EUR figures are
kept separate from the USD alias series.

## Performance check

- `entity_key: LSE:FTEU`; `input_ticker: FTDPF`; the official factsheet maps the
  same ISIN to London Stock Exchange `USD FTEU LN`, while the input OTC symbol
  is retained only as an alias. The official factsheet does not list FTDPF as a
  primary exchange ticker.
- Classification: supported passive/index-tracking equity UCITS ETF; official
  factsheet says the fund is passively managed, physically fully replicated and
  rebalanced semi-annually.
- Inception: 21 ต.ค. 2014; Ireland-domiciled UCITS; ongoing charges `0.65%`
  ณ 29 พ.ค. 2026; accumulating; base currency EUR.
- Metric: official factsheet's `Acc EUR` total return includes capital and income
  returns net of fees; the USD FTEU annual/current fields marked `*` are a
  secondary USD total-return series and are not presented as issuer NAV fields.
- Tracked index: `Nasdaq AlphaDEX Eurozone NTR Index`; the methodology ranks
  growth and value factors, selects the top 150 stocks, weights by quintile with
  country/sector constraints, and reconstitutes semi-annually.
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference
  benchmark ไม่ใช่ tracked index ของ FTEU). The official strategy-aligned index
  remains the Nasdaq AlphaDEX Eurozone NTR Index.
- Official Acc EUR performance as of 29 พ.ค. 2026: YTD `13.39%`, 1-year
  `30.66%`, 3-year annualised `23.40%`, 5-year annualised `11.91%`, and since
  inception annualised `10.68%`; corresponding index fields were `13.44%`,
  `30.55%`, `23.25%`, `11.97%`, and `11.02%`.
- Secondary FTEU USD trailing snapshot as of 30 ก.ค. 2026: YTD `12.31%*`,
  1-year `20.85%*`, 3-year annualised `21.29%*`, 5-year annualised `10.98%*`,
  and 10-year annualised `10.75%*`. The 10-year USD field is not an official
  issuer field and is retained with the `*` marker.
- Latest secondary USD quote snapshot: closing price `US$75.54` ณ 30 ก.ค.
  2026; it is not used in NAV return calculations.

| Year | FTEU USD total return* | S&P 500 TR |
|---|---:|---:|
| 2021 | 12.59% | 28.71% |
| 2022 | -19.74% | -18.11% |
| 2023 | 16.65% | 26.29% |
| 2024 | 3.03% | 25.02% |
| 2025 | 57.98% | 17.88% |

`*` Secondary Morningstar USD fund-return series for the FTEU share class;
issuer official calendar rows for this USD line were not exposed in the
reviewed capture. Do not mix this table with the official EUR-base factsheet
returns.

## Up years / Down years

- Secondary USD 2021-2025 up/down: `4 / 1`
- Best secondary USD year: 2025, `+57.98%*`
- Least positive secondary USD year: 2024, `+3.03%*`
- Worst secondary USD year: 2022, `-19.74%*`
- Least bad down year: 2022, the only down year in this five-year window
- 2021-2025 cumulative/CAGR: FTEU USD `71.57%*` / `11.40%*`; S&P 500 TR
  `96.17%` / `14.43%`
- Latest secondary USD YTD: `+12.31%*` ณ 30 ก.ค. 2026; official Acc EUR YTD
  `+13.39%` ณ 29 พ.ค. 2026 is a separate currency/as-of observation.

## Risk read-through

Official factsheet country exposure ณ 29 พ.ค. 2026 มี Germany `22.47%`, France
`20.14%`, Italy `14.54%`, The Netherlands `9.04%`, Spain `8.95%`; sector
exposure มี Industrials `22.44%`, Materials `12.25%`, Financials `10.65%`,
Energy `10.46%`, Consumer Discretionary `9.57%`, และ Utilities `9.29%`. Annual
return volatility ของ secondary USD rows 2021-2025 อยู่ที่ `25.31%*` แบบ
population; เป็นแค่ five-year return dispersion ไม่ใช่ official daily NAV
standard deviation.

กองทุนมี Eurozone country, sector, factor-selection และ EUR/USD currency risks.
Official daily NAV history ที่เพียงพอสำหรับ maximum drawdown และ recovery ยัง
ไม่ถูกเปิดเผย และไม่มีการใช้ price-only proxy แทน NAV. Main evidence limitation
คือ official factsheet exposes the Acc EUR share-class series, whereas the input
alias's USD annual/current fields are secondary.

## Sources

- [First Trust Eurozone AlphaDEX UCITS ETF factsheet](https://www.fundslibrary.co.uk/FundsLibrary.DataRetrieval/Documents.aspx/?id=db97fa3f-452a-4e87-a092-5d78014ea6e7&r=1&type=packet_fund_class_doc_factsheet_private&user=lmaloTxGN4q8hRUMT0fWlPBQqCmCX%2FhnFIbf7%2F7XByN2nwFrjrtLgpitSJYn96ru) — ISIN, official trading lines, inception, fee, UCITS/passive/physical structure, official Acc EUR performance and exposures as of 2026-05-29
- [Central Bank of Ireland fund register](https://registers.centralbank.ie/%28X%281%29S%28uzbkfrrwrh3qjlqvxporqnfl%29%29/FundRegisterDataPage.aspx?fundReferenceNumber=C118215&register=28) — UCITS fund identity and regulatory status
- [Morningstar FTEU report](https://lt.morningstar.com/1c6qh1t6k9/etfreport/default.aspx?1=1&ClientFund=0&CurrencyId=USD&Id=0P00018JZQ&SecurityToken=0P00018JZQ%5D22%5D0%5DETEXG%24XLON&tab=1) — secondary USD annual and trailing-return fields
- [OTC FTDPF identity cross-check](https://www.eoddata.com/stockquote/OTCBB/FTDPF.htm) — input alias legal-name cross-check only; not used as primary NAV evidence
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- Cached S&P 500 TR references: [2021](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/), [2022-2025](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/)
- ETF source batch: [[ETF_performance_sources_2026-08-18]] | [[ETF Performance Index]]
