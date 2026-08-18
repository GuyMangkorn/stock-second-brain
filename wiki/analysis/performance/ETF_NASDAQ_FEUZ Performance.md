---
type: etf-performance
instrument_type: ETF
entity_key: NASDAQ:FEUZ
ticker: FEUZ
exchange: Nasdaq
fund: First Trust Eurozone AlphaDEX ETF
tracked_index: Nasdaq AlphaDEX Eurozone Index
benchmark: S&P 500 Total Return
updated: 2026-08-18
performance_as_of: 2025-12-31
rolling_10y_as_of: 2026-07-31
current_ytd_as_of: 2026-07-31
price_nav_as_of: 2026-08-13
fund_facts_as_of: 2026-08-13
source_batch: raw/imports/ETF_performance_sources_2026-08-18.md
return_basis: NAV total return
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/FEUZ
  - geography/Europe
---

# FEUZ Performance

> Navigation: [[ETF Region Index]] → [[Europe ETF]] → [[ETF Performance Index]]

## Bottom line

FEUZ เป็น passive/index-tracking Eurozone equity ETF ที่ใช้ AlphaDEX คัดเลือก
หุ้นจาก Nasdaq Eurozone Index โดยจัดอันดับ growth/value factors เลือกหุ้น 150 ตัว
ให้น้ำหนักแบบ quintile และ rebalance ปีละสองครั้ง. ใน complete calendar window
2016-2025 มี 8 ปีบวก / 2 ปีลบ; annual NAV Total Return จาก official rounded rows
ให้ cumulative `144.62%` และ CAGR `9.36%`, เทียบ S&P 500 TR ที่ `298.33%` /
`14.82%`. ปีดีที่สุดคือ 2025 ที่ `+56.57%` และแย่ที่สุดคือ 2018 ที่ `-19.82%`.
Latest official NAV TR YTD ที่ยืนยันได้คือ `+12.30%` ณ 31 ก.ค. 2026.

## Performance check

- `entity_key: NASDAQ:FEUZ`
- Classification: supported passive/index-tracking equity ETF; the prospectus
  says the Fund normally invests at least 90% of net assets in the index and
  uses an indexing approach. FEUZ is the Nasdaq-listed U.S. ETF and is distinct
  from the UCITS USD London line `FTEU` tracked under the separate input alias
  `FTDPF`.
- Inception: 21 ต.ค. 2014; exchange `Nasdaq`; total expense ratio `0.80%`
  (as of 1 พ.ค. 2026); number of holdings `150` ณ 13 ส.ค. 2026.
- Metric: `NAV Total Return` บนฐาน USD รวม distributions ตาม issuer methodology
  และหัก fund expenses; market-price return kept separate.
- Tracked index: `Nasdaq AlphaDEX Eurozone Index`. The index begins with the
  Nasdaq Eurozone universe, removes duplicates and securities failing liquidity
  screens, ranks growth and value factors, selects the top 150 securities,
  weights them by quintile, applies country/industry constraints set at 15%
  above the base-index weights, and reconstitutes semi-annually.
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference
  benchmark ไม่ใช่ tracked index ของ FEUZ). Strategy-aligned comparisons use the
  official Nasdaq AlphaDEX Eurozone Index.
- Official rolling 10-year NAV TR: average annual `10.43%` ณ 31 ก.ค. 2026;
  เป็น rolling issuer figure แยกจาก calendar-row CAGR.
- Current official NAV TR as of 31 ก.ค. 2026: YTD `12.30%`, 1-year `26.53%`,
  3-year `21.31%`, 5-year `10.61%`, 10-year `10.43%`, and since inception
  `9.39%`. Same-date tracked-index fields were `12.30%`, `26.29%`, `21.94%`,
  `11.24%`, `11.05%`, and `10.00%` for the comparable periods.
- Latest quote snapshot as of 13 ส.ค. 2026: closing NAV `US$68.66`, closing
  market price `US$68.59`, bid/ask discount `0.07%`, net assets `US$133,878,209`,
  and 30-day median bid/ask spread `0.60%`; quotes are not used in return
  calculations.

| Year | FEUZ NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 5.49% | 11.96% |
| 2017 | 36.19% | 21.83% |
| 2018 | -19.82% | -4.38% |
| 2019 | 21.15% | 31.49% |
| 2020 | 4.69% | 18.40% |
| 2021 | 12.90% | 28.71% |
| 2022 | -19.65% | -18.11% |
| 2023 | 15.71% | 26.29% |
| 2024 | 1.88% | 25.02% |
| 2025 | 56.57% | 17.88% |

## Up years / Down years

- Up years / Down years: `8 / 2` ใน 2016-2025
- Best: 2025, `+56.57%`
- Least positive: 2024, `+1.88%`
- Worst: 2018, `-19.82%`
- Least bad down year: 2022, `-19.65%`
- 2016-2025 cumulative/CAGR: FEUZ `144.62%` / `9.36%`; S&P 500 TR
  `298.33%` / `14.82%`
- 2021-2025 cumulative/CAGR: FEUZ `67.44%` / `10.86%`; S&P 500 TR
  `96.17%` / `14.43%`
- Current FEUZ NAV TR YTD: `+12.30%` ณ 31 ก.ค. 2026; the official
  strategy-aligned index was also `+12.30%` on the same date. This is tracking
  comparison evidence, not a claim of manager skill.

## Risk read-through

จาก annual rows แบบ rounded-input ช่วง 2016-2025 ได้ annual-return volatility
แบบ population `22.09%`; official 3-year statistics ณ 31 ก.ค. 2026 รายงาน
standard deviation `15.31%`, beta `0.93`, Sharpe ratio `1.05`, และ correlation
`0.92`. Current country exposures ณ 13 ส.ค. 2026 คือ Germany `21.12%`, France
`20.60%`, Italy `14.44%`, The Netherlands `9.49%`, Spain `9.00%`; sectors คือ
Industrials `21.56%`, Financials `12.12%`, Materials `11.67%`, Energy `11.12%`,
Utilities `9.15%`, and Consumer Discretionary `8.77%`. จึงมี Eurozone
country/sector/factor/FX, mid-cap และ liquidity risks แม้จะมี 150 holdings.

Prospectus disclosed best quarter `+23.61%` ณ 31 ธ.ค. 2022 และ worst quarter
`-29.55%` ณ 31 มี.ค. 2020. Official daily NAV history ที่เพียงพอสำหรับ
maximum drawdown และ recovery ยังไม่ถูกเปิดเผย จึงไม่ใช้ market-price proxy
แทน NAV risk metric.

## Sources

- [First Trust FEUZ product page](https://www.ftportfolios.com/Retail/Etf/EtfSummary.aspx?Ticker=FEUZ) — identity, index methodology, fee, current NAV/price, holdings, exposures, rolling returns, YTD and risk statistics
- [First Trust Exchange-Traded AlphaDEX Fund II prospectus](https://www.ftportfolios.com/LoadContent/gradkqbz8r4y) — passive strategy, official 2016-2025 annual-return chart, average annual returns and risk disclosure
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- Cached S&P 500 TR references: [2016-2019](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [2018-2022](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), [2021](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/), [2022-2025](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/)
- ETF source batch: [[ETF_performance_sources_2026-08-18]] | [[ETF Performance Index]]
