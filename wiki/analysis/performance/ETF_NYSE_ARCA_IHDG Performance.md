---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:IHDG
ticker: IHDG
exchange: NYSE Arca
fund: WisdomTree International Hedged Quality Dividend Growth Fund
tracked_index: WisdomTree International Hedged Quality Dividend Growth Index
benchmark: S&P 500 Total Return
updated: 2026-09-01
performance_as_of: 2026-07-31
annual_rows_as_of: 2026-03-31
current_ytd_as_of: 2026-07-31
source_batch: raw/imports/ETF_performance_sources_2026-09-01_run-5.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/IHDG
  - geography/International
---

# IHDG Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

IHDG ให้ผลตอบแทนบนฐาน NAV Total Return สะสม 147.45% หรือ rounded-input CAGR 9.48% ในช่วง 2016-2025 เทียบ S&P 500 Total Return ที่ 14.82% ต่อปี. ในช่วง 2021-2025 IHDG สะสม 54.34% หรือ 9.07% ต่อปี เทียบ S&P ที่ 14.43% ต่อปี. จุดเด่นของกองคือการ hedge ค่าเงินเชิงระบบ ไม่ใช่การลด equity risk; current NAV TR YTD อยู่ที่ 9.84% ณ 2026-07-31 และ aggregate hedge ratio อยู่ที่ 98.65% ณ 2026-08-28.

## Performance check

- entity_key: NYSE Arca:IHDG
- Fund: WisdomTree International Hedged Quality Dividend Growth Fund
- Classification: passive index-tracking international equity ETF with systematic currency hedge
- Inception: 2014-05-07; net expense ratio: 0.58% as of 2026-08-31
- Issuer benchmark: WisdomTree International Hedged Quality Dividend Growth Index
- NAV Total Return: daily NAV return with distributions reinvested and fund expenses reflected; USD
- Common benchmark: S&P 500 Total Return, USD, dividends reinvested; cached reference as of 2025-12-31
- Current official product snapshot as of 2026-08-28: NAV $53.716, market price $53.540, premium/discount -0.329%, distribution yield 5.14%, 30-day SEC yield 1.89%, assets $2,191,614.64k, and aggregate hedge ratio 98.65%
- Official month-end performance as of 2026-07-31: index YTD 10.09%; NAV TR YTD 9.84%, 1-year 20.00%, 3-year 11.71%, 5-year 7.82%, 10-year average annual 10.34%, and since inception 9.69%
- The issuer's 10-year average annual figure is retained as reported and is not relabeled as an independently calculated CAGR because raw endpoints are not disclosed
- 2016-2025: cumulative 147.45%; rounded-input CAGR 9.48%
- 2021-2025: cumulative 54.34%; rounded-input CAGR 9.07%

### Annual NAV TR

| Year | IHDG NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 1.66% | 11.96% |
| 2017 | 21.47% | 21.83% |
| 2018 | -11.71% | -4.38% |
| 2019 | 32.74% | 31.49% |
| 2020 | 10.78% | 18.40% |
| 2021 | 19.72% | 28.71% |
| 2022 | -11.36% | -18.11% |
| 2023 | 19.55% | 26.29% |
| 2024 | 6.42% | 25.02% |
| 2025 | 14.32% | 17.88% |

2016-2025 IHDG CAGR 9.48% vs S&P 500 TR CAGR 14.82%, a -5.34 percentage-point spread. 2021-2025 IHDG CAGR 9.07% vs S&P 500 TR CAGR 14.43%, a -5.36 percentage-point spread. Calculations use rounded official annual inputs.

## Up years / Down years

- Up years: 8; down years: 2
- Best year: 2019, +32.74%
- Least-positive year: 2024, +6.42%
- Worst year: 2018, -11.71%
- Least-bad down year: 2022, -11.36%

## Risk read-through

The 2016-2025 population standard deviation computed from annual NAV returns is 13.65%, versus 14.92% for the cached S&P 500 annual series; this is an annual-path calculation, not an issuer daily-volatility statistic. การ hedge ค่าเงินช่วยแยกผลกระทบของ foreign-exchange movement ออกจาก equity return บางส่วน แต่ยังมี residual hedge, country, small/mid-cap, dividend, liquidity และ tracking risks. Aggregate hedge ratio ล่าสุดที่ยืนยันได้คือ 98.65% ณ 2026-08-28. Official daily NAV history สำหรับ maximum drawdown และ recovery duration ไม่ได้ยืนยัน จึงบันทึกเป็น not disclosed.

## Sources

- [Official WisdomTree product page](https://www.wisdomtree.com/us/products/equity/ihdg)
- [Official IHDG factsheet](https://www.wisdomtree.com/-/media/us-media-files/documents/resource-library/fund-fact-sheets/international-equity/wisdomtree-ihdg-1748.pdf)
- [Official IHDG presentation](https://www.wisdomtree.com/us/media/ihdg-presentation)
- [Official index page](https://www.wisdomtree.com/us/indexes/wtidhg)
- [S&P 500 index reference](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- Source batch: [[ETF_performance_sources_2026-09-01_run-5]]
