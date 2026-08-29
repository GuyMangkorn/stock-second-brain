---
type: etf-performance
instrument_type: ETF
entity_key: LSE:FTEU
input_ticker: FTDPF
ticker: FTEU
exchange: London Stock Exchange
fund: First Trust Eurozone AlphaDEX UCITS ETF
tracked_index: Nasdaq AlphaDEX Eurozone Index
benchmark: S&P 500 Total Return
updated: 2026-08-29
performance_as_of: 2025-12-31
rolling_10y_as_of: 2026-08-27
current_ytd_as_of: 2026-08-27
price_nav_as_of: not verified for the USD LSE line
fund_facts_as_of: 2026-07-31
source_batch: raw/imports/ETF_performance_sources_2026-08-29.md
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
equity ETF ที่ติดตาม `Nasdaq AlphaDEX Eurozone Index`. ชุด annual USD
total-return ที่ตรวจสอบได้จาก secondary source ครบ 2021-2025 ให้ cumulative
`71.57%*` และ CAGR `11.40%*`, เทียบ S&P 500 TR ที่ `96.17%` / `14.43%`; มี
4 ปีบวก / 1 ปีลบ. ปีดีที่สุดคือ 2025 ที่ `+57.98%*` และแย่ที่สุดคือ 2022 ที่
`-19.74%*`. Latest USD YTD secondary field คือ `+14.06%*` ณ 27 ส.ค. 2026.
Official factsheet reports the same ISIN's Acc EUR share-class YTD `14.55%`
and since-inception annualised `10.61%` ณ 31 ก.ค. 2026; those EUR figures are
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
  ณ 31 ก.ค. 2026; accumulating; base currency EUR.
- Metric: official factsheet's `Acc EUR` total return includes capital and income
  returns net of fees; the USD FTEU annual/current fields marked `*` are a
  secondary USD total-return series and are not presented as issuer NAV fields.
- Tracked index: `Nasdaq AlphaDEX Eurozone Index`; the methodology ranks
  growth and value factors, selects the top 150 stocks, weights by quintile with
  country/sector constraints, and reconstitutes semi-annually.
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference
  benchmark ไม่ใช่ tracked index ของ FTEU). The official strategy-aligned index
  remains the Nasdaq AlphaDEX Eurozone Index.
- Official Acc EUR performance as of 31 ก.ค. 2026: YTD `14.55%`, 1-year
  `25.43%`, 3-year annualised `20.33%`, 5-year annualised `11.86%`, and since
  inception annualised `10.61%`; corresponding index fields were `14.64%`,
  `25.63%`, `20.22%`, `11.91%`, and `10.95%`.
- Secondary FTEU USD trailing snapshot as of 27 ส.ค. 2026: YTD `14.06%*`,
  1-year `24.60%*`, 3-year annualised `25.55%*`, 5-year annualised `10.92%*`,
  and 10-year annualised `10.63%*`. The 10-year USD field is not an official
  issuer field and is retained with the `*` marker.
- A current FTEU USD-LSE price/NAV pair was not disclosed in the reviewed
  official or secondary capture; no FEUZ U.S.-listed price is substituted.

| Year | FTEU USD total return* | S&P 500 TR |
|---|---:|---:|
| 2021 | 12.59% | 28.71% |
| 2022 | -19.74% | -18.11% |
| 2023 | 16.65% | 26.29% |
| 2024 | 3.03% | 25.02% |
| 2025 | 57.98% | 17.88% |

`*` Secondary Morningstar USD fund-return series for the FTEU share class,
annual table as of 31 ก.ค. 2026 and trailing fields as of 27 ส.ค. 2026; issuer
official calendar rows for this USD line were not exposed in the reviewed
capture. Do not mix this table with the official EUR-base factsheet returns.

## Up years / Down years

- Secondary USD 2021-2025 up/down: `4 / 1`
- Best secondary USD year: 2025, `+57.98%*`
- Least positive secondary USD year: 2024, `+3.03%*`
- Worst secondary USD year: 2022, `-19.74%*`
- Least bad down year: 2022, the only down year in this five-year window
- 2021-2025 cumulative/CAGR: FTEU USD `71.57%*` / `11.40%*`; S&P 500 TR
  `96.17%` / `14.43%`
- Latest secondary USD YTD: `+14.06%*` ณ 27 ส.ค. 2026; official Acc EUR YTD
  `+14.55%` ณ 31 ก.ค. 2026 is a separate currency/as-of observation.

## Risk read-through

Official factsheet country exposure ณ 31 ก.ค. 2026 มี Germany `21.36%`, France
`20.77%`, Italy `14.27%`, The Netherlands `9.26%`, Spain `9.15%`; sector
exposure มี Industrials `21.60%`, Financials `12.02%`, Materials `11.55%`,
Energy `11.14%`, Utilities `9.40%`, Consumer Discretionary `8.86%`. Annual
return volatility ของ secondary USD rows 2021-2025 อยู่ที่ `25.31%*` แบบ
population; เป็นแค่ five-year return dispersion ไม่ใช่ official daily NAV
standard deviation.

กองทุนมี Eurozone country, sector, factor-selection และ EUR/USD currency risks.
Official daily NAV history ที่เพียงพอสำหรับ maximum drawdown และ recovery ยัง
ไม่ถูกเปิดเผย และไม่มีการใช้ price-only proxy แทน NAV. Main evidence limitation
คือ official factsheet exposes the Acc EUR share-class series, whereas the input
alias's USD annual/current fields are secondary; the USD-LSE price/NAV pair is
ยังไม่พบข้อมูลที่ยืนยันได้.

## Sources

- [First Trust Eurozone AlphaDEX UCITS ETF factsheet](https://www.fundslibrary.co.uk/FundsLibrary.DataRetrieval//Documents.aspx?id=db97fa3f-452a-4e87-a092-5d78014ea6e7&type=packet_fund_class_doc_factsheet_private&user=fidelitydocumentreport) — ISIN, official trading lines, inception, fee, UCITS/passive/physical structure, official Acc EUR performance and exposures as of 2026-07-31
- [Central Bank of Ireland fund register](https://registers.centralbank.ie/%28X%281%29S%28uzbkfrrwrh3qjlqvxporqnfl%29%29/FundRegisterDataPage.aspx?fundReferenceNumber=C118215&register=28) — UCITS fund identity and regulatory status
- [Morningstar FTEU report](https://lt.morningstar.com/1c6qh1t6k9/etfreport/default.aspx?1=1&ClientFund=0&CurrencyId=USD&Id=0P00018JZQ&SecurityToken=0P00018JZQ%5D22%5D0%5DETEXG%24XLON&tab=1) — secondary USD annual rows as of 2026-07-31 and trailing fields as of 2026-08-27
- [OTC FTDPF identity cross-check](https://www.eoddata.com/stockquote/OTCBB/FTDPF.htm) — input alias legal-name cross-check only; not used as primary NAV evidence
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- Cached S&P 500 TR references: [2021](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/), [2022-2025](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/)
- ETF source batch: [[ETF_performance_sources_2026-08-29]] | [[ETF Performance Index]]
