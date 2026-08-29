---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:EWX
input_ticker: EWX
ticker: EWX
exchange: NYSE Arca
fund: State Street SPDR S&P Emerging Markets Small Cap ETF
tracked_index: S&P Emerging Under USD2 Billion Index
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
primary_region: Emerging Markets
tags:
  - analysis/etf-performance
  - ticker/EWX
  - geography/Emerging-Markets
---

# EWX Performance

> Navigation: [[ETF Region Index]] → [[Emerging Markets ETF]] → [[ETF Performance Index]]

## Bottom line

`EWX` คือ State Street SPDR S&P Emerging Markets Small Cap ETF, passive
emerging-markets small-cap equity ETF ที่ติดตาม `S&P Emerging Under USD2
Billion Index` และมี gross expense ratio `0.65%`. Official State Street
รายงาน rolling 10-year NAV Total Return average annual `7.95%`, 1-year
`9.84%`, 3-year `9.82%`, 5-year `5.32%` และ current NAV TR YTD `3.91%` ณ
2026-07-31. Latest official daily snapshot รายงาน NAV `$73.96`, market price
`$74.02`, premium/discount `0.08%` และ AUM `$702.61M` ณ 2026-08-27.

Complete calendar-year rows 2016-2025 ยังเป็น secondary dividend-reinvested
total-return proxy*; proxy cumulative `128.55%` และ rounded-input CAGR
`8.62%*` จึงไม่ถูก relabel เป็น official NAV performance. Secondary EWX
partial-2026 observation `+10.72%` ณ 2026-08-21 ไม่ใช้แทน official July
month-end YTD เพราะคนละ period/as-of date.

## Performance check

- `entity_key: NYSE Arca:EWX`; State Street ระบุ fund เป็น `State Street SPDR S&P Emerging Markets Small Cap ETF`, listed on NYSE Arca, inception `2008-05-12`, CUSIP `78463X756`, ISIN `US78463X7562`.
- Classification: `passive-index-tracking`; fund ใช้ sampling strategy, ลงทุนอย่างน้อย 80% ใน securities/ADRs/GDRs ของ index และอาจใช้ futures เพื่อการติดตาม index หรือบริหาร cash flows; implementation นี้ไม่เปลี่ยน passive equity classification.
- Metric: official `NAV Total Return` รวม distributions ที่ reinvested และหัก fund expenses; market-price return และ issuer benchmark return ถูกเก็บแยก. Annual rows ในตารางเป็น secondary dividend-reinvested proxy `*` เพราะ official current page ไม่เปิดเผย complete calendar-year NAV rows.
- Tracked index: `S&P Emerging Under USD2 Billion Index`; common reference คือ `S&P 500 Total Return` (USD, dividends reinvested) ไม่ใช่ issuer tracking benchmark.
- Official rolling 10-year NAV TR average annual `7.95%` as of `2026-07-31`; raw rolling endpoints และ exact elapsed years ไม่ได้เปิดเผย.
- Official current fund facts as of `2026-08-27` to `2026-08-28`: 3,383 holdings, AUM `$702.61M`, P/B `1.70`, P/E FY1 `14.77`, weighted average market cap `$1,816.91M`, 30-day SEC yield `1.99%`, fund distribution `2.49%`, and index dividend `2.35%`.

### Official July 2026 standardized returns

| Return basis | 1M | QTD | YTD | 1Y | 3Y annualized | 5Y annualized | 10Y annualized | Since inception annualized |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| NAV | -8.69% | -8.69% | 3.91% | 9.84% | 9.82% | 5.32% | 7.95% | 4.18% |
| Market value | -9.58% | -9.58% | 3.07% | 10.33% | 9.58% | 5.14% | 7.87% | 4.14% |
| S&P Emerging Under USD2 Billion Index | -8.87% | -8.87% | 3.33% | 9.11% | 10.12% | 5.58% | 8.19% | 5.11% |

All official rows above are as of `2026-07-31`. State Street defines the fund
returns as net of fees with reinvested distributions; the index is unmanaged
and is not called alpha.

### Secondary annual total-return context

| Year | EWX secondary total-return proxy* | S&P 500 TR (USD; common ref.) |
|---|---:|---:|
| 2016 | 7.94% | 11.96% |
| 2017 | 34.10% | 21.83% |
| 2018 | -18.74% | -4.38% |
| 2019 | 15.59% | 31.49% |
| 2020 | 14.86% | 18.40% |
| 2021 | 18.16% | 28.71% |
| 2022 | -15.00% | -18.11% |
| 2023 | 18.15% | 26.29% |
| 2024 | 6.84% | 25.02% |
| 2025 | 15.44% | 17.88% |

The EWX annual series is ETFreplay's secondary dividend-adjusted total-return
proxy, not issuer-published NAV rows. The S&P 500 column reuses the cached USD
Total Return convention as of `2025-12-31`.

## Window calculations and tracking context

- Secondary 2016-2025 proxy compounds to `128.55%*` / rounded-input CAGR `8.62%*`; up/down years are `8 / 2`; best is 2017 `+34.10%*`; worst is 2018 `-18.74%*`.
- Secondary 2021-2025 proxy compounds to `46.36%*` / rounded-input CAGR `7.92%*`; cached S&P 500 TR compounds to `96.17%` / CAGR `14.43%` over the same window. This is a common reference, not manager-skill evidence.
- Official NAV minus linked-index observations as of 2026-07-31 are 1M/QTD `+0.18 pp`, YTD `+0.58 pp`, 1Y `+0.73 pp`, 3Y `-0.30 pp`, 5Y `-0.26 pp`, 10Y `-0.24 pp`, and since inception `-0.93 pp`; these are passive implementation/expense observations, not alpha.
- Official rolling 10Y NAV TR `7.95%` remains separate from secondary 2016-2025 CAGR `8.62%*` and 2021-2025 CAGR `7.92%*`; the windows and source ownership differ.
- Reconciliation: ETFreplay reports partial-2026 total return `+10.72%` as of 2026-08-21, while State Street's official NAV TR YTD is `+3.91%` through 2026-07-31. FinanceCharts independently shows `4.76%` YTD and a `8.18%` secondary 10-year CAGR; these date/source differences are disclosed and not mixed into the canonical official fields.

## Risk read-through

Latest official State Street characteristics as of 2026-08-27 show 3,383
holdings and a low top-ten concentration: LandMark Optoelectronics `0.76%`,
Kinsus `0.72%`, Macronix `0.61%`, Katilim… `0.47%`, WinWay `0.44%`, Win
Semiconductors `0.43%`, ITEQ `0.35%`, Syntec `0.31%`, A Data `0.31%`, and
Innodisk `0.30%`; the displayed top ten sum is `4.70%`.

Sector weights as of 2026-08-27 were Information Technology `26.67%`,
Industrials `17.38%`, Materials `12.50%`, Consumer Discretionary `10.58%`,
Financials `7.46%`, Health Care `7.10%`, Real Estate `5.77%`, Consumer Staples
`5.45%`, Utilities `2.65%`, Communication Services `2.31%`, Energy `1.83%`,
and Unassigned `0.29%`. A prior official geographic snapshot as of 2026-08-14
listed Taiwan `31.79%`, India `18.50%`, and China `17.82%`; the latest
accessible 2026-08-27 page did not expose a current country breakdown, so no
newer country weights are asserted.

EWX มี emerging-market, small-cap, country, FX, technology, liquidity และ
geopolitical risk. Prospectus context records best quarter `+25.82%` in Q2
2020 and worst quarter `-28.68%` in Q1 2020. Official daily NAV history
sufficient to reproduce fund-level maximum drawdown, recovery date, or
volatility ยังไม่พบข้อมูลที่ยืนยันได้; จึงไม่สร้าง secondary NAV drawdown
number ขึ้นมา.

## Sources

- [State Street EWX product/performance page](https://www.ssga.com/us/en/intermediary/etfs/state-street-spdr-sp-emerging-markets-small-cap-etf-ewx) — official identity, exchange, index, passive strategy, current NAV/market price/AUM, holdings, sectors, characteristics, yields and July standardized performance.
- [Official EWX factsheet](https://www.ssga.com/library-content/products/factsheets/etfs/us/factsheet-us-en-ewx.pdf) — official fund-document and standardized-return cross-reference; dated 2026-07-31 in the reviewed source result.
- [SEC EWX summary prospectus](https://www.sec.gov/Archives/edgar/data/1168164/000119312526031211/d87745d497k.htm) — official passive strategy, index construction, fees, risks and best/worst-quarter context.
- [ETFreplay EWX annual total-return table](https://www.etfreplay.com/etf/ewx) — secondary dividend-adjusted annual rows and partial-2026 observation.
- [FinanceCharts EWX performance table](https://www.financecharts.com/etfs/EWX/performance) — secondary cross-check; not mixed into the official fields or canonical annual proxy.
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached workflow references — common USD Total Return rows, dividends reinvested, as of 2025-12-31.
- [[ETF_performance_sources_2026-08-29]] | [[ETF Performance Index]]
