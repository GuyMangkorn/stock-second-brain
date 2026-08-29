---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:SPEU
input_ticker: SPEU
ticker: SPEU
exchange: NYSE Arca
fund: State Street SPDR Portfolio Europe ETF
tracked_index: STOXX Europe Total Market Index
benchmark: S&P 500 Total Return
management_mode: passive-index-tracking
updated: 2026-08-29
performance_as_of: 2026-07-31
current_ytd_as_of: 2026-07-31
current_nav_as_of: 2026-08-26
fund_facts_as_of: 2026-07-21
source_batch: raw/imports/ETF_performance_sources_2026-08-29.md
return_basis: NAV total return; dividends reinvested; net of expenses
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/SPEU
  - geography/Europe
---

# SPEU Performance

> Navigation: [[ETF Region Index]] → [[Europe ETF]] → [[ETF Performance Index]]

## Bottom line

`SPEU` คือ State Street SPDR Portfolio Europe ETF, canonical listing
`NYSE Arca:SPEU`. Latest official State Street July month-end capture reports
NAV TR YTD `+9.45%`, 1Y `+22.02%`, 3Y `+15.87%`, 5Y `+9.09%` และ rolling 10Y
`+9.65%` ณ 31 ก.ค. 2026. A later official product-page capture reports NAV
`US$57.41` and AUM `US$746.35M` ณ 26 ส.ค. 2026. Issuerไม่แสดง complete annual
calendar rows ใน reviewed official capture จึงคง secondary dividend-reinvested
total-return proxy ปี 2021-2025 แบบติด `*`: cumulative `61.99%*` หรือ
rounded-input CAGR `10.13%*`.

## Performance check

- `entity_key: NYSE Arca:SPEU`; State Street ระบุ exchange `NYSE Arca`, ticker `SPEU`, CUSIP `78463X103`, ISIN `US78463X1037`, inception `2002-10-15`, base currency `USD` และ distribution frequency `Quarterly`.
- Classification: `passive-index-tracking`; fund ใช้ sampling และมุ่งติดตาม `STOXX Europe Total Market Index`, broad Western Europe across the market-cap spectrum.
- Metric: official `NAV Total Return` รวม dividends/capital gains ที่ reinvested และ net of fees; market-value return ถูกเก็บแยก. Annual rows ในตารางเป็น secondary total-return proxy `*` และไม่ควรเรียกว่า official NAV TR.
- Issuer benchmark: `STOXX Europe Total Market Index`; State Street ระบุ linked benchmark ว่าใช้ `STOXX Europe 50 Index` ตั้งแต่ inception ถึง `2019-09-22` และ `STOXX Europe Total Market Index` ตั้งแต่ `2019-09-23`. Common reference ในตารางคือ `S&P 500 Total Return` (USD, dividends reinvested).
- Latest official current NAV/AUM capture: NAV `US$57.41`, shares outstanding `13.00M`, and AUM `US$746.35M` as of `2026-08-26`. The full product-page breakdown reviewed for holdings and yields is separately dated 2026-07-17: NAV `US$54.97`, AUM `US$714.59M`, 30-day SEC yield `2.43%`, fund distribution yield `3.44%`, and gross expense ratio `0.07%`.
- Official NAV TR as of `2026-07-31`: 1-month `2.02%`, QTD `2.02%`, YTD `9.45%`, 1Y `22.02%`, 3Y `15.87%`, 5Y `9.09%`, 10Y `9.65%`, since inception `6.96%`; linked benchmark fields are `2.02% / 2.02% / 9.23% / 21.79% / 15.63% / 8.83% / 9.52% / 6.93%`.
- The issuer's July product page is the fresh performance source. Its full HTML capture exposed older July-17 fund facts while the current search capture exposed the later Aug-26 NAV/AUM; both are preserved with their as-of dates rather than conflated.

### Official July 2026 standardized returns

| Return basis | 1M | QTD | YTD | 1Y | 3Y annualized | 5Y annualized | 10Y annualized | Since inception |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| NAV | 2.02% | 2.02% | 9.45% | 22.02% | 15.87% | 9.09% | 9.65% | 6.96% |
| Market value | 2.20% | 2.20% | 9.90% | 22.89% | 16.01% | 9.07% | 9.69% | 6.97% |
| STOXX Europe linked benchmark | 2.02% | 2.02% | 9.23% | 21.79% | 15.63% | 8.83% | 9.52% | 6.93% |

### Secondary annual total-return context

| Year | SPEU total-return proxy* (USD; not official NAV) | S&P 500 TR (USD; common ref.) |
|---|---:|---:|
| 2021 | 16.20% | 28.71% |
| 2022 | -15.97% | -18.11% |
| 2023 | 19.84% | 26.29% |
| 2024 | 1.94% | 25.02% |
| 2025 | 35.80% | 17.88% |

FinanceCharts is a secondary dividend-reinvested total-return source; its direct page
was captcha-gated during this run, so the existing 2021-2025 proxy rows are retained
from the prior dated source batch and remain marked `*`. They do not override the
issuer's official rolling NAV fields.

## Window calculations and ranking

- Secondary proxy 2021-2025 compounds to `61.99%*` / rounded-input CAGR `10.13%*`; up/down years are `4 / 1`; best is 2025 `+35.80%*`; least positive is 2024 `+1.94%*`; worst/least-bad down year is 2022 `-15.97%*`; population standard deviation is `17.48%*`.
- Cached S&P 500 TR compounds to `96.17%` / CAGR `14.43%` over 2021-2025. It is a common USD reference only; no direct manager-skill or alpha claim is made.
- Official rolling NAV TR is `9.65%` annualized as of 2026-07-31 and remains separate from the secondary calendar proxy `10.13%*`.
- Official linked benchmark tracking differences for July are NAV minus index: YTD `+0.22 pp`, 1Y `+0.23 pp`, 3Y `+0.24 pp`, 5Y `+0.26 pp`, 10Y `+0.26 pp`, and since inception `+0.03 pp`; these are passive tracking observations, not alpha.
- Current official NAV: `US$57.41` as of 2026-08-26; current market-price/NAV pair for the same date is `ไม่พบข้อมูลที่ยืนยันได้`.

## Risk read-through

The official product breakdown as of 2026-07-17 reports `1,684` holdings, P/B `2.27x`,
P/E FY1 `15.19x`, weighted average market cap `US$126,168.53M`, 30-day SEC Yield
`2.43%`, fund distribution yield `3.44%`, and index dividend yield `2.93%`. Top country
weights are United Kingdom `21.99%`, France `14.75%`, Switzerland `13.96%`, Germany
`12.72%`, Netherlands `8.30%`, Sweden `6.06%`, Spain `5.76%`, and Italy `5.68%`.
Sector weights are Financials `25.00%`, Industrials `19.24%`, Health Care `12.34%`,
Information Technology `8.46%`, Consumer Staples `8.14%`, Consumer Discretionary
`7.19%`, Materials `5.42%`, Energy `5.07%`, Utilities `4.73%`, Communication Services
`2.93%`, and Real Estate `1.48%`.

Main risks are European country/sector/small-cap exposure, non-USD underlying currency
movements, linked benchmark-history change, sampling/tracking risk, equity volatility
and market-price/NAV timing. Official daily NAV maximum drawdown and recovery date
ยัง `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- [State Street SPEU product page](https://www.ssga.com/us/en/individual/etfs/state-street-spdr-portfolio-europe-etf-speu) — official identity, listing, inception, benchmark-history change, current NAV/AUM capture, fund facts, yields, holdings, sector weights and rolling NAV performance.
- [State Street SPEU factsheet](https://www.ssga.com/library-content/products/factsheets/etfs/us/factsheet-us-en-speu.pdf) — official NAV/benchmark performance, fee, holdings and country/sector facts as of 2026-06-30.
- [FinanceCharts SPEU total-return history](https://www.financecharts.com/stocks/SPEU/performance/total-return) — secondary dividend-reinvested total-return proxy for calendar rows 2021-2025; marked `*`, with direct page captcha limitation preserved.
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached workflow references — common USD Total Return rows, dividends reinvested, as of 2025-12-31.
- [[ETF_performance_sources_2026-08-29]] | [[ETF Performance Index]]
