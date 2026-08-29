---
type: etf-performance
instrument_type: ETF
entity_key: NASDAQ:NFTY
ticker: NFTY
exchange: NASDAQ
fund: First Trust India NIFTY 50 Equal Weight ETF
tracked_index: NIFTY 50 Equal Weight Index
benchmark: S&P 500 Total Return
updated: 2026-08-29
performance_as_of: 2026-07-31
current_ytd_as_of: 2026-07-31
source_batch: raw/imports/ETF_performance_sources_2026-08-29.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/NFTY
  - geography/India
---

# NFTY Performance

> Navigation: [[ETF Region Index]] → [[India ETF]] → [[ETF Performance Index]]

## Bottom line

NFTY เป็น passive/index-tracking India equity ETF ที่ติดตาม NIFTY 50 Equal Weight Index. Official rolling 10-year NAV Total Return CAGR ล่าสุดอยู่ที่ `7.62%` ณ `2026-07-31`; raw start/end TR values ไม่ได้เปิดเผย. Official calendar rows `2016-2025` compound เป็น `145.94%` / CAGR `9.42%`. Latest official month-end NAV TR YTD คือ `-5.59%` ณ `2026-07-31`.

## Performance check

- entity_key: `NASDAQ:NFTY`
- Inception: `2012-02-14`
- Metric: NAV Total Return including reinvested distributions and fund expenses
- Tracked index: NIFTY 50 Equal Weight Index; index inception `2017-04-13`
- Index history caveat: fund's underlying index changed from Nasdaq AlphaDEX Taiwan Index to NIFTY 50 Equal Weight Index on `2018-04-17`; earlier fund NAV history is not a pure current-index backtest
- Official 10-year window: latest month-end `2016-07-31` to `2026-07-31`; actual years `10.00`; start TR value `not disclosed`; end TR value `not disclosed`; official CAGR `7.62%`
- Implied cumulative return from the displayed official CAGR is approximately `108.42%`; this is a shown calculation, not a substitute for undisclosed raw endpoints
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark, not the issuer benchmark)

| Year | NFTY NAV TR | NIFTY 50 Equal Weight TR | NIFTY 50 TR | MSCI India TR | S&P 500 TR |
|---|---:|---:|---:|---:|---:|
| 2016 | 10.31% | not disclosed | 1.89% | -1.43% | 11.96% |
| 2017 | 22.54% | not disclosed | 37.95% | 38.75% | 21.83% |
| 2018 | -2.67% | not disclosed | -3.76% | -7.30% | -4.38% |
| 2019 | 0.88% | not disclosed | 11.88% | 7.58% | 31.49% |
| 2020 | 10.83% | not disclosed | 12.50% | 15.55% | 18.40% |
| 2021 | 26.22% | not disclosed | 23.48% | 26.23% | 28.71% |
| 2022 | -4.45% | not disclosed | -5.14% | -7.95% | -18.11% |
| 2023 | 24.39% | not disclosed | 20.82% | 20.81% | 26.29% |
| 2024 | 5.30% | not disclosed | 7.00% | 11.21% | 25.02% |
| 2025 | 5.84% | not disclosed | 6.57% | 2.62% | 17.88% |

Annual NFTY NAV TR rows are retained from the latest reviewed First Trust factsheet capture (historical calendar rows through `2025`); annual NIFTY 50 Equal Weight rows were not disclosed in the current official capture. A May 2026 summary prospectus shows small rounding/version differences for 2023-2025, so the factsheet series is kept consistently and the conflict is disclosed in the source batch. The current First Trust summary page reports July's rolling 10-year NAV TR as `7.62%`, while the linked monthly-report PDF displays `7.99%` in its 10-year column; the current summary page is used for the owner metric and the discrepancy is preserved rather than silently mixed. S&P 500 rows reuse the cached USD Total Return convention for complete calendar years `2016-2025`.

## Window calculations

- 2016-2025 NFTY NAV TR: cumulative `145.94%` / CAGR `9.42%`; S&P 500 TR: cumulative `298.33%` / CAGR `14.82%`
- 2021-2025 NFTY NAV TR: cumulative `67.19%` / CAGR `10.83%`; S&P 500 TR: cumulative `96.17%` / CAGR `14.43%`; NFTY trails by approximately `3.60 pp` CAGR
- Up years / down years: `8 / 2`
- Best year: `2021`, `26.22%`; worst year: `2022`, `-4.45%`
- Latest official month-end NAV TR YTD: `-5.59%` as of `2026-07-31`; current NAV `US$54.40` and market price `US$54.10` as of `2026-08-27` are separate point-in-time observations.

## Risk read-through

NFTY มี 50 holdings และมี exposure สูงต่อ India, financials, consumer discretionary, materials และ health care. First Trust รายงาน 3-year standard deviation `14.31%` ณ `2026-07-31`; ความเสี่ยงหลักคือ country concentration, emerging-market liquidity, INR/USD, sector concentration และความต่างระหว่าง NAV กับ market price. Daily NAV history ที่ยืนยันได้สำหรับ max drawdown และ recovery: `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- Official First Trust summary: https://www.ftportfolios.com/Retail/Etf/EtfSummary.aspx?Ticker=NFTY
- Official First Trust monthly performance report (as of 2026-07-31): https://www.ftportfolios.com/Common/ContentFileLoader.aspx?ContentGUID=b363655b-cc73-4f42-a7b1-4c1e00306c7c
- Official First Trust factsheet (historical calendar rows in reviewed capture): https://www.ftportfolios.com/Common/ContentFileLoader.aspx?ContentGUID=4ce8e98a-434e-452d-89fb-89f33f070e32
- Official First Trust summary prospectus (May 1, 2026): https://www.ftportfolios.com/Common/ContentFileLoader.aspx?ContentGUID=9c00e478-c2d3-49d2-b8db-229055716c36
- SEC annual-return XBRL record: https://www.sec.gov/Archives/edgar/data/1510337/000144554626003180/R11.htm
- SEC average-annual-return XBRL record: https://www.sec.gov/Archives/edgar/data/1510337/000144554626003180/R12.htm
- Official S&P 500 index page: https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- ETF source batch: [[ETF_performance_sources_2026-08-29]] | [[ETF Performance Index]]
