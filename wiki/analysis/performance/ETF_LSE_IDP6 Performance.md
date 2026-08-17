---
type: etf-performance
instrument_type: ETF
entity_key: LSE:IDP6
ticker: IDP6
input_alias: ISHOF
exchange: London Stock Exchange
fund: iShares S&P SmallCap 600 UCITS ETF USD (Dist)
tracked_index: S&P 600 Small Cap Index (NET)
benchmark: S&P 500 Total Return
updated: 2026-08-17
performance_as_of: 2026-07-30
calendar_years_as_of: 2025-12-31
current_ytd_as_of: 2026-07-30
price_nav_as_of: 2026-07-31
source_batch: raw/imports/ETF_performance_sources_2026-08-17.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/IDP6
  - ticker/ISHOF
  - geography/United-States
---

# IDP6 Performance

> Navigation: [[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]

## Bottom line

ISHOF เป็น OTC input alias ของกองทุนเดียวกับ official USD listing `LSE:IDP6` ของ iShares S&P SmallCap 600 UCITS ETF (ISIN `IE00B2QWCY14`). กองทุนเป็น passive physical/optimised U.S. small-cap equity ที่ติดตาม S&P 600 Small Cap Index (NET). Official iShares NAV Total Return 2016-2025 compound เป็น `141.31%` หรือ rounded-input CAGR `9.21%`; 2021-2025 CAGR เป็น `6.72%`. Current official NAV TR YTD คือ `21.36%` ณ 2026-07-30.

## Performance check

- entity_key: LSE:IDP6
- Input alias: ISHOF (OTC); canonical USD listing: `LSE:IDP6`; same fund ISIN `IE00B2QWCY14`
- Inception: 2008-05-09
- Metric: NAV Total Return with gross income reinvested where applicable, after ongoing charges
- Tracked index (issuer benchmark): S&P 600 Small Cap Index (NET)
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark)
- Total Expense Ratio: `0.30%`
- 2016-2025 calendar NAV TR: cumulative `141.31%`; rounded-input CAGR `9.21%`
- 2021-2025 calendar NAV TR: cumulative `38.40%`; rounded-input CAGR `6.72%`
- Current NAV TR YTD: `21.36%` as of 2026-07-30; latest NAV quote `US$117.48` as of 2026-07-31

| Year | IDP6 NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 25.93% | 11.96% |
| 2017 | 12.62% | 21.83% |
| 2018 | -8.95% | -4.38% |
| 2019 | 22.04% | 31.49% |
| 2020 | 10.64% | 18.40% |
| 2021 | 26.25% | 28.71% |
| 2022 | -16.72% | -18.11% |
| 2023 | 15.43% | 26.29% |
| 2024 | 8.04% | 25.02% |
| 2025 | 5.55% | 17.88% |

S&P 500 rows reuse the project’s cached USD total-return convention for complete calendar years 2016-2025; market-price return is not mixed.

## Up years / Down years

- Up years / Down years: `8 / 2` across complete calendar years 2016-2025
- Best: 2016, `25.93%`
- Least positive: 2025, `5.55%`
- Worst: 2022, `-16.72%`
- Least bad down year: 2018, `-8.95%`
- 2016-2025 rounded-input CAGR: `9.21%`; 2021-2025 rounded-input CAGR: `6.72%`
- Current NAV TR YTD: `21.36%` as of 2026-07-30; secondary S&P 500 current cross-check `10.14%` as of 2026-07-31 is one day later and is not used as a synchronized spread

## Risk read-through

IDP6 เป็น U.S. small-cap exposure ที่มี small-cap, cyclicality และ liquidity risk สูงกว่าหุ้น large-cap. Official iShares รายงาน 3-year standard deviation `19.40%` ณ 2026-06-30, 3-year beta `0.998`, holdings `657` ณ 2026-07-30 และ trailing distribution yield `1.01%` ณ 2026-07-28. Physical/optimised structure และ benchmark tracking เป็นข้อมูลโครงสร้าง ไม่ใช่หลักฐานของ future outperformance. Official daily NAV history สำหรับ maximum drawdown และ recovery ไม่ได้ถูกยืนยันใน capture นี้.

## Driver notes

- Confirmed structure: passive physical/optimised exposure to 600 U.S. small-cap companies through the S&P 600 Small Cap Index (NET); the fund distributes income semi-annually.
- Observed regime points: 2016 was the strongest complete year at `+25.93%`, while 2022 was the weakest at `-16.72%`. These are return observations, not causal event attribution.
- Alias resolution: ISHOF is preserved as the input alias, while durable ownership uses the official USD LSE line `IDP6` and ISIN `IE00B2QWCY14`; GBP `ISP6` is another listing of the same fund and is not used as the canonical currency line.

## Sources

- [iShares official IDP6/ISP6 product page](https://www.ishares.com/uk/individual/en/products/251920/ishares-s-p-smallcap-600-ucits-etf?siteEntryPassthrough=true) — official identity, USD/GBP listings, ISIN, index, NAV, YTD, expense ratio, risk fields and calendar NAV TR rows
- [iShares official factsheet](https://www.blackrock.com/uk/professional/en/literature/fact-sheet/isp6-ishares-s-p-smallcap-600-ucits-etf-fund-fact-sheet-en-gb.pdf) — official USD distributing share-class calendar performance and NAV-return definition
- [iShares USD distributing KIID](https://www.ishares.com/uk/professional/en/literature/kiid/ucits_kiid-ishares-sp-smallcap-600-ucits-etf-usd-dist-gb-ie00b2qwcy14-en.pdf) — passive objective, benchmark, NAV performance definition and risk context
- [Slickcharts S&P 500 YTD total return](https://www.slickcharts.com/sp500/returns/ytd) — secondary current benchmark cross-check through 2026-07-31
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common benchmark definition
- Cached S&P 500 TR references: [S&P DJI historical research](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [2023 U.S. Equities Market Attributes](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), and [2025 S&P DJI market attributes](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/); reference as-of 2025-12-31
- ETF source batch: [[ETF_performance_sources_2026-08-17]] | [[ETF Performance Index]]
