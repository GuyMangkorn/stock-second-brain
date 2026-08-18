---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:OPPE
ticker: OPPE
exchange: NYSE Arca
fund: WisdomTree European Opportunities Fund
tracked_index: WisdomTree European Opportunities Index
benchmark: S&P 500 Total Return
updated: 2026-08-18
performance_as_of: 2025-12-31
rolling_10y_as_of: 2026-07-31
current_ytd_as_of: 2026-07-31
price_nav_as_of: 2026-08-14
fund_facts_as_of: 2026-08-14
source_batch: raw/imports/ETF_performance_sources_2026-08-18.md
return_basis: NAV total return
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/OPPE
  - geography/Europe
---

# OPPE Performance

> Navigation: [[ETF Region Index]] → [[Europe ETF]] → [[ETF Performance Index]]

## Bottom line

OPPE เป็น passive/index-tracking Europe equity ETF ที่ติดตาม `WisdomTree
European Opportunities Index` และใช้ dynamic currency hedge. ใน complete
calendar window 2016-2025 มี 7 ปีบวก / 3 ปีลบ; annual NAV Total Return ที่
คำนวณจาก rounded official rows ให้ cumulative `186.21%` และ CAGR `11.09%`,
เทียบ S&P 500 TR ที่ `298.33%` / `14.82%`. ปีดีที่สุดคือ 2025 ที่ `+38.73%`
และแย่ที่สุดคือ 2018 ที่ `-13.41%`. Current official NAV TR YTD ล่าสุดที่
ยืนยันได้คือ `+17.72%` ณ 31 ก.ค. 2026. อย่างไรก็ดี ปี 2025 คร่อมการเปลี่ยน
objective/index วันที่ 2 มิ.ย. 2025 จึงไม่ใช่ clean current-strategy year.

## Performance check

- `entity_key: NYSE Arca:OPPE`
- Classification: supported passive/index-tracking equity ETF using passive
  indexing and representative sampling; exchange `NYSE Arca`
- Inception: 4 มี.ค. 2015; expense ratio `0.58%`; distribution yield `7.83%`
  ณ 14 ส.ค. 2026
- Metric: `NAV Total Return` บนฐาน USD รวม reinvested distributions และ fund
  expenses ตาม issuer methodology; total returns ใช้ daily 4:00pm NAV
- Tracked index (issuer benchmark): `WisdomTree European Opportunities Index`;
  historical performance uses the `WisdomTree Europe Hedged SmallCap Equity /
  WisdomTree European Opportunities Equity Spliced Index` across the
  2025-06-02 objective/index change
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference
  benchmark ไม่ใช่ tracked index ของ OPPE)
- Official rolling 10-year NAV TR: average annual `12.91%` ณ 31 ก.ค. 2026;
  เป็น rolling issuer figure แยกจาก calendar-row CAGR
- 10-year calendar window: `2016-01-01` to `2025-12-31`; rounded-input
  cumulative/CAGR `186.21%` / `11.09%`; Start TR value `100.00`, End TR value
  `286.21`, Years `10.00`
  - Formula: `(End TR / Start TR)^(1 / Years) - 1`
- Current official NAV TR YTD: `17.72%` ณ 31 ก.ค. 2026; official 1-year NAV TR
  `29.84%` and 5-year NAV TR `14.66%` ณ วันเดียวกัน
- Latest quote snapshot: NAV `US$60.308`, closing market price `US$60.504`,
  premium/discount `+0.324%` ณ 14 ส.ค. 2026; quotes are not used in return
  calculations
- Coverage/source note: 2016-2024 annual rows are the official prospectus
  annual-return chart; 2025 is the official 1-year NAV return ending
  31 ธ.ค. 2025. The 2016-2024 history reflects the former EUSC
  Europe Hedged SmallCap objective, while 2025 is a mixed transition year.

| Year | OPPE NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 7.86% | 11.96% |
| 2017 | 22.32% | 21.83% |
| 2018 | -13.41% | -4.38% |
| 2019 | 28.45% | 31.49% |
| 2020 | -2.34% | 18.40% |
| 2021 | 22.65% | 28.71% |
| 2022 | -11.18% | -18.11% |
| 2023 | 19.33% | 26.29% |
| 2024 | 10.74% | 25.02% |
| 2025 | 38.73% | 17.88% |

## Up years / Down years

- Up years / Down years: `7 / 3` ใน 2016-2025
- Best: 2025, `+38.73%`
- Least positive: 2016, `+7.86%`
- Worst: 2018, `-13.41%`
- Least bad down year: 2020, `-2.34%`
- 2016-2025 cumulative/CAGR: OPPE `186.21%` / `11.09%`; S&P 500 TR
  `298.33%` / `14.82%`
- 2021-2025 cumulative/CAGR: OPPE `99.71%` / `14.84%`; S&P 500 TR
  `96.17%` / `14.43%`
- Current OPPE NAV TR YTD: `+17.72%` ณ 31 ก.ค. 2026

## Risk read-through

Official rolling 10-year NAV TR เฉลี่ยต่อปีอยู่ที่ `12.91%` ณ 31 ก.ค. 2026;
เมื่อใช้ annual rows แบบ rounded-input ช่วง 2016-2025 ได้ CAGR `11.09%` และ
annual-return volatility `16.33%`. OPPE มี exposure กระจุกใน Industrials
`25.94%`, Financials `25.62%` และ Materials `12.50%` ณ 14 ส.ค. 2026 และ
aggregate hedge ratio `97.95%`; จึงยังมี Europe country/sector, cyclical,
large-/mid-cap และ hedge-effect risks แม้จะลด EUR/USD exposure บางส่วน.

Official daily NAV history ที่เพียงพอสำหรับ maximum drawdown และ recovery ยัง
ไม่ถูกเปิดเผย. Secondary dividend-adjusted daily market-price proxy รายงาน
maximum drawdown `39.28%` เมื่อ 18 มี.ค. 2020 และ recovery `229` trading
sessions*; proxy นี้ไม่ใช่ NAV evidence และไม่ถูกใช้แทน NAV risk metric. The
main limitation is continuity: the 10-year rolling figure and most annual rows
contain the former EUSC strategy, while the current OPPE objective began in
June 2025.

## Sources

- [WisdomTree OPPE product page](https://www.wisdomtree.com/us/products/equity/oppe) — identity, index objective, fee, current NAV/price, rolling returns, YTD, holdings/sector and hedge ratio
- [WisdomTree OPPE quarterly factsheet](https://www.wisdomtree.com/us/media/international-equity/en-us-equity-oppe) — exchange, inception, return basis, official performance table, historical index splice and risks
- [WisdomTree Trust prospectus](https://regulated-documents.saytechnologies.com/prospectuses/e0ff850f-45f1-417b-8779-01e2206cb79d-97717X552.pdf) — passive strategy and official 2016-2024 annual-return chart
- [WisdomTree monthly performance report](https://www.wisdomtree.com/investments/-/media/us-media-files/documents/resource-library/fund-reports-schedules/performance/monthly-performance.pdf) — official 2025 NAV return ending 31 ธ.ค. 2025
- [WisdomTree European Opportunities Index](https://www.wisdomtree.com/us/indexes/wteuop) — index design, value/shareholder-yield and dynamic currency-hedge methodology
- [PortfoliosLab OPPE](https://portfolioslab.com/symbol/OPPE) — secondary dividend-adjusted market-price drawdown/recovery proxy only
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- Cached S&P 500 TR references: [2016-2019](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [2018-2022](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), [2021](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/), [2022-2025](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/)
- ETF source batch: [[ETF_performance_sources_2026-08-18]] | [[ETF Performance Index]]
