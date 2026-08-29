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
management_mode: passive-index-tracking
updated: 2026-08-29
annual_performance_as_of: 2025-12-31
performance_as_of: 2026-07-31
rolling_10y_as_of: 2026-07-31
current_ytd_as_of: 2026-07-31
nav_as_of: 2026-08-27
market_price_as_of: 2026-08-27
fund_facts_as_of: 2026-08-28
risk_as_of: 2026-08-27
source_batch: raw/imports/ETF_performance_sources_2026-08-29.md
return_basis: NAV total return; dividends and capital gains reinvested; net of expenses
return_currency: USD
primary_region: Europe
tags:
  - analysis/etf-performance
  - ticker/FEZ
  - geography/Europe
---

# FEZ Performance

> Navigation: [[ETF Region Index]] → [[Europe ETF]] → [[ETF Performance Index]]

## Bottom line

`FEZ` คือ State Street SPDR EURO STOXX 50 ETF, passive Eurozone large-cap
equity ETF ที่ติดตาม `EURO STOXX 50 Index` และมี gross expense ratio `0.29%`.
Official State Street รายงาน NAV Total Return `10.92%` แบบ rolling 10-year
average annual และ `9.66%` current YTD ณ 2026-07-31. Latest official daily
snapshot รายงาน NAV `$71.14`, market midpoint/close `$71.34`,
premium/discount `0.27%` และ AUM `$4,503.11M` ณ 2026-08-27.

Complete calendar-year rows 2016-2025 เป็น secondary dividend-reinvested
total-return proxy*; proxy cumulative `149.39%` / rounded-input CAGR `9.57%*`
และ 2021-2025 CAGR `12.30%*` จึงไม่ถูก relabel เป็น official NAV rows และไม่ถูก
ใช้ใน strict Common Window ranking.

## Performance check

- `entity_key: NYSE Arca:FEZ`; State Street ระบุ fund เป็น `State Street SPDR EURO STOXX 50 ETF`, listed on NYSE Arca, inception `2002-10-15`, CUSIP `78463X202`, ISIN `US78463X2027`.
- Classification: `passive-index-tracking`; fund มุ่งให้ผลตอบแทนโดยทั่วไปสอดคล้องกับ `EURO STOXX 50 Index` และใช้ sampling/index-tracking mechanics; ไม่มี derivative-defined payoff.
- Metric: official `NAV Total Return` รวม dividends/capital gains ที่ reinvested และแสดง net of fund fees; market-price return และ index return ถูกเก็บแยก. Annual rows ด้านล่างเป็น secondary dividend-reinvested proxy `*` เพราะ official current page ไม่เปิดเผย complete calendar-year NAV rows.
- Tracked index: `EURO STOXX 50 Index`; index เป็น market-capitalization-weighted large-cap Eurozone reference. Common comparison benchmark คือ `S&P 500 Total Return` (USD, dividends reinvested) ไม่ใช่ issuer tracking benchmark.
- Official rolling 10-year NAV TR average annual `10.92%` as of `2026-07-31`; raw rolling endpoints และ exact elapsed years ไม่ได้เปิดเผย.
- Official current facts as of `2026-08-27` to `2026-08-28`: 50 holdings, AUM `$4,503.11M`, P/B `2.48`, P/E FY1 `16.08`, weighted average market cap `$197,779.33M`, estimated 3-5 year EPS growth `15.63%`, 30-day SEC yield `1.94%`, fund distribution yield `2.50%`, and index dividend yield `2.66%`.

### Official July 2026 standardized returns

| Return basis | 1M | QTD | YTD | 1Y | 3Y annualized | 5Y annualized | 10Y annualized | Since inception annualized |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| NAV | 1.20% | 1.20% | 9.66% | 22.94% | 16.94% | 11.50% | 10.92% | 7.83% |
| Market value | 1.56% | 1.56% | 10.27% | 23.82% | 17.17% | 11.53% | 10.96% | 7.84% |
| EURO STOXX 50 Index | 1.20% | 1.20% | 9.46% | 22.78% | 16.76% | 11.23% | 10.76% | 7.60% |

All official rows above are as of `2026-07-31`. State Street defines fund
returns as net of fees with reinvested distributions; index returns are
unmanaged and are not called alpha.

### Secondary annual total-return context

| Year | FEZ secondary total-return proxy* | S&P 500 TR (USD; common ref.) |
|---|---:|---:|
| 2016 | 0.64% | 11.96% |
| 2017 | 24.78% | 21.83% |
| 2018 | -15.85% | -4.38% |
| 2019 | 26.04% | 31.49% |
| 2020 | 4.85% | 18.40% |
| 2021 | 14.83% | 28.71% |
| 2022 | -14.30% | -18.11% |
| 2023 | 27.19% | 26.29% |
| 2024 | 3.55% | 25.02% |
| 2025 | 37.78% | 17.88% |

The FEZ annual series is ETFreplay's secondary dividend-adjusted total-return
proxy, not issuer-published NAV rows. The S&P 500 column reuses the cached USD
Total Return convention as of `2025-12-31`.

## Window calculations and tracking context

- Secondary 2016-2025 proxy compounds to `149.39%*` / rounded-input CAGR `9.57%*`; up/down years are `8 / 2`; best is 2025 `+37.78%*`; least positive is 2016 `+0.64%*`; worst is 2018 `-15.85%*`; least-bad down year is 2022 `-14.30%*`.
- Secondary 2021-2025 proxy compounds to `78.58%*` / rounded-input CAGR `12.30%*`; cached S&P 500 TR compounds to `96.17%` / CAGR `14.43%` over the same window. This is a common reference, not manager-skill evidence.
- Official NAV minus linked-index observations as of 2026-07-31 are 1M/QTD `0.00 pp`, YTD `+0.20 pp`, 1Y `+0.16 pp`, 3Y `+0.18 pp`, 5Y `+0.27 pp`, 10Y `+0.16 pp`, and since inception `+0.23 pp`; these are passive implementation/expense observations, not alpha.
- Official rolling 10Y NAV TR `10.92%` remains separate from secondary 2016-2025 CAGR `9.57%*` and 2021-2025 CAGR `12.30%*`; the windows and source ownership differ.
- Reconciliation: the refreshed ETFreplay annual rows differ slightly from the prior FinanceCharts proxy (for example 2016 `0.64%` versus `0.67%` and 2025 `37.78%` versus `37.81%`). The fresh ETFreplay series is used consistently for the current annual proxy; FinanceCharts remains a secondary cross-check and its current YTD/rolling observations are not mixed with official State Street fields.

## Risk read-through

Latest official State Street holdings as of 2026-08-27 show a concentrated
large-cap portfolio. Top holdings are ASML Holding `8.84%`, Siemens `4.69%`,
SAP `4.28%`, Banco Santander `4.11%`, Schneider Electric `3.83%`, Allianz
`3.77%`, TotalEnergies `3.76%`, BBVA `3.10%`, Safran `2.82%`, and Iberdrola
`2.81%`; the displayed top ten sum is `42.01%`.

Current official sector weights as of 2026-08-27 are Financials `28.42%`,
Industrials `22.00%`, Information Technology `14.86%`, Consumer Discretionary
`9.32%`, Health Care `5.38%`, Consumer Staples `5.15%`, Energy `4.81%`,
Utilities `4.46%`, Materials `3.41%`, and Communication Services `2.19%`.
The official factsheet country snapshot as of 2026-06-30 was France `32.27%`,
Germany `28.88%`, Netherlands `14.98%`, Spain `11.36%`, Italy `8.38%`, Belgium
`2.85%`, and Finland `1.28%`; the latest product-page geographic section did
not expose a newer country breakdown.

FEZ มี Eurozone country, EUR/USD FX, large-cap concentration, sector,
valuation, equity-market, geopolitical และ liquidity risk. Secondary ETFreplay
reports annualized daily volatility `18.4%` as of 2026-08-21, while the
rounded annual proxy population standard deviation is `17.24%*`; ทั้งสองเป็น
secondary context ไม่ใช่ official daily NAV risk measure. Official daily NAV
history sufficient to reproduce maximum drawdown and recovery date ยังไม่พบ
ข้อมูลที่ยืนยันได้.

## Sources

- [State Street FEZ product/performance page](https://www.ssga.com/us/en/intermediary/etfs/state-street-spdr-euro-stoxx-50-etf-fez) — official identity, exchange, index, fee, current NAV/market price/AUM, holdings, sectors, characteristics, yields and July standardized performance.
- [Official FEZ factsheet](https://www.ssga.com/library-content/products/factsheets/etfs/us/factsheet-us-en-fez.pdf) — official return definition, June 2026 fund facts, holdings, sectors and country snapshot.
- [ETFreplay FEZ annual total-return table](https://www.etfreplay.com/etf/fez) — secondary dividend-adjusted annual rows and volatility cross-check.
- [FinanceCharts FEZ performance table](https://www.financecharts.com/etfs/FEZ/performance) — secondary cross-check; not mixed into the canonical official fields.
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached workflow references — common USD Total Return rows, dividends reinvested, as of 2025-12-31.
- [[ETF_performance_sources_2026-08-29]] | [[ETF Performance Index]]
