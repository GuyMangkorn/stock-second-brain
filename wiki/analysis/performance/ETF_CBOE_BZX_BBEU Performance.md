---
type: etf-performance
instrument_type: ETF
entity_key: Cboe BZX:BBEU
input_ticker: BBEU
ticker: BBEU
exchange: Cboe BZX
fund: JPMorgan BetaBuilders Europe ETF
tracked_index: Morningstar Developed Europe Target Market Exposure Index (net total return)
benchmark: S&P 500 Total Return
management_mode: passive-index-tracking
updated: 2026-08-18
performance_as_of: 2025-12-31
rolling_10y_as_of: not-applicable-lt-10y
current_ytd_as_of: 2026-07-31
price_nav_as_of: not-disclosed-official-capture
fund_facts_as_of: 2026-07-31
source_batch: raw/imports/ETF_performance_sources_2026-08-18.md
return_basis: NAV total return; distributions reinvested; fund expenses reflected in NAV
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/BBEU
  - geography/Europe
---

# BBEU Performance

> Navigation: [[ETF Region Index]] → [[Europe ETF]] → [[ETF Performance Index]]

## Bottom line

`BBEU` คือ JPMorgan BetaBuilders Europe ETF ที่จดทะเบียนบน Cboe BZX และเป็น
`passive-index` broad developed-Europe equity ETF ซึ่งติดตาม `Morningstar
Developed Europe Target Market Exposure Index (net total return)`. Official
complete calendar NAV rows ปี 2019-2025 compound ได้ `117.38%` หรือ
rounded-input CAGR `11.73%`; ช่วงร่วม 2021-2025 ได้ `65.74%` หรือ `10.63%`
ต่อปี. Latest official NAV TR YTD คือ `+10.47%` ณ 31 ก.ค. 2026. Inception ปี
2018 ทำให้ยังไม่มี 10-year NAV CAGR ที่ใช้ได้.

## Performance check

- `entity_key: Cboe BZX:BBEU`; official fund name, ticker, CUSIP `46641Q191`, and class launch `15 มิ.ย. 2018` are confirmed by JPMorgan and SEC filings. SEC identifies the listing exchange as Cboe BZX Exchange.
- Classification: `passive-index` / indexed equity. The fund seeks to closely correspond to the Morningstar Developed Europe Target Market Exposure Index, invests at least 80% of assets in index securities, and does not seek to outperform the index or take defensive positions.
- Metric: issuer `NAV Total Return` with distributions and capital gains reinvested; fund operating expenses are reflected in NAV performance. `S&P 500 Total Return` is a common USD reference only, not the tracked index.
- Expense ratio: gross and net annual expenses `0.09%`. The official factsheet describes a free-float adjusted market-capitalization-weighted index covering developed European countries.
- Official current performance as of 31 ก.ค. 2026: NAV TR `1M 2.13%`, `3M 5.16%`, `YTD 10.47%`, `1Y 24.41%`, and since-launch annualized `9.42%`. Official annualized fields as of 30 มิ.ย. 2026: `1Y 18.51%`, `3Y 16.59%`, `5Y 9.80%`, and since-launch `9.23%`.
- Official fund facts as of 31 ก.ค. 2026: fund assets `$9.36B`, 352 holdings, P/E `15.41x`, P/B `2.53x`, weighted average market cap `$148.34B`, and ROE `19.25%`. Current NAV and market price were not disclosed in the reviewed official capture.
- Annual coverage: official complete calendar NAV rows begin in 2019; 2018 is an inception-year partial period and is omitted from the calculated windows.

| Year | BBEU NAV TR (USD) | Morningstar Developed Europe Target Market Exposure Index (USD) | S&P 500 TR (USD) |
|---|---:|---:|---:|
| 2019 | 23.84% | 23.88% | 31.49% |
| 2020 | 5.91% | 5.82% | 18.40% |
| 2021 | 16.70% | 16.57% | 28.71% |
| 2022 | -14.71% | -15.23% | -18.11% |
| 2023 | 19.98% | 19.95% | 26.29% |
| 2024 | 2.25% | 2.16% | 25.02% |
| 2025 | 35.73% | 35.86% | 17.88% |

Coverage/source note: BBEU and Morningstar index rows are official JPMorgan
factsheet rows as of 31 ก.ค. 2026; the SEC summary prospectus separately reports
the 2025-ended 5-year fund return of `10.63%` and benchmark return of `10.47%`.
S&P 500 rows are the cached USD total-return convention, dividends reinvested,
as of 31 ธ.ค. 2025.

Official BBEU rows compound to `117.38%` / rounded-input CAGR `11.73%` for
2019-2025 and `65.74%` / `10.63%` for 2021-2025. The linked index rows compound
to `115.66%` / `11.60%` and `64.51%` / `10.47%`; approximate fund-minus-index
differences of `+0.13 pp` and `+0.16 pp` are rounded-input passive tracking
observations, not alpha. Cached S&P 500 TR compounds to `96.17%` / `14.43%`
for 2021-2025, so BBEU trails that common reference by approximately `-3.79 pp`
of CAGR; it is not the issuer benchmark.

**Up years / Down years**

- Complete 2019-2025 NAV TR up/down: `6 / 1`
- Best NAV TR year: 2025, `+35.73%`
- Least positive year: 2024, `+2.25%`
- Worst NAV TR year: 2022, `-14.71%`
- Least bad down year: 2022, `-14.71%`
- Population standard deviation of the seven complete annual NAV returns: `15.26%`; this is calendar-return dispersion, not an issuer daily-volatility field.

## Risk read-through

BBEU มี broad Europe แต่ยังมี country และ sector concentration: UK `22.1%`,
Switzerland `14.7%`, France `13.6%`, Germany `13.2%`, and Netherlands `9.7%`;
sector weights include Financials `26.3%`, Industrials `18.4%`, Health Care
`12.9%`, Consumer Staples `8.7%`, and Information Technology `8.3%` ณ 31 ก.ค.
2026. จึงมี European macro, EUR/GBP/CHF-USD FX, foreign-market, financials,
industrials, large-/mid-cap, passive-index, sampling และ tracking-cost risk.
Official daily NAV maximum drawdown และ recovery date ยัง `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- [JPMorgan BBEU July 2026 factsheet](https://am.jpmorgan.com/content/dam/jpm-am-aem/americas/us/en/literature/fact-sheet/etfs/FS-BBEU.PDF) — official identity, classification, annual rows, current YTD, rolling returns, assets, holdings, sectors, countries and portfolio metrics.
- [SEC BBEU summary prospectus](https://www.sec.gov/Archives/edgar/data/1485894/000119312526071726/d55674d497k.htm) — official objective, passive/indexing strategy, exchange, fees, risk disclosures and performance comparison through 31 Dec 2025.
- S&P 500 Total Return 2019-2025 and 2021-2025 cached convention from the workflow; USD dividends reinvested, as of 31 ธ.ค. 2025.
- [[ETF_performance_sources_2026-08-18]] | [[ETF Performance Index]]
