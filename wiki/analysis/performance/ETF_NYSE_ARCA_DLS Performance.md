---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:DLS
ticker: DLS
exchange: NYSE Arca
fund: WisdomTree International SmallCap Dividend Fund
tracked_index: WisdomTree International SmallCap Dividend Index
benchmark: S&P 500 Total Return
updated: 2026-08-16
performance_as_of: 2026-07-31
annual_rows_as_of: 2026-03-31
current_ytd_as_of: 2026-07-31
source_batch: raw/imports/ETF_performance_sources_2026-08-16.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/DLS
  - geography/International
---

# DLS Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

DLS ให้ผลตอบแทนบนฐาน NAV Total Return สะสม 46.75% หรือ rounded-input CAGR 7.97% ในช่วง 2021-2025 เทียบ S&P 500 Total Return ที่ 14.43% ต่อปีในช่วงเดียวกัน. ในช่วง annual rows 2016-2025 กองมี 7 ปีบวกและ 3 ปีลบ; ปีแย่สุดคือ 2018 ที่ -18.69%. ค่า issuer-reported 10-year average annual NAV TR คือ 7.69% ณ 2026-07-31 และ current NAV TR YTD คือ 8.54% ณ 2026-07-31. ค่า 7.69% ไม่ควรเรียกเป็น independently calculated CAGR เพราะ issuer ไม่เปิดเผย endpoints และ elapsed years.

## Performance check

- entity_key: NYSE Arca:DLS
- Fund: WisdomTree International SmallCap Dividend Fund
- Classification: passive index-tracking equity ETF
- Inception: 2006-06-16; net expense ratio: 0.58% as of 2026-08-14; factsheet gross expense ratio: 0.58% as of 2026-03-31
- Issuer benchmark: WisdomTree International SmallCap Dividend Index (WTISDI)
- NAV Total Return: daily 4:00 p.m. EST NAV, distributions reinvested, fund expenses reflected in NAV; USD
- Common benchmark: S&P 500 Total Return, USD, dividends reinvested; cached reference as of 2025-12-31
- Annual NAV TR source: official DLS presentation dated 2026-03-31; this is the sole supplied full annual-row source in this packet. The SEC prospectus independently corroborates the 2022 row at -17.36%; no conflict is established
- 2016-2025: cumulative 101.65%; rounded-input CAGR 7.27%
- 2021-2025: cumulative 46.75%; rounded-input CAGR 7.97%
- Current official performance from the [WisdomTree product page](https://www.wisdomtree.com/us/products/equity/dls), page/current quote as of 2026-08-14: NAV TR YTD 8.54%, 1-year average annual 18.29%, 10-year average annual 7.69%, all performance fields as of 2026-07-31
- Current NAV: 89.274 USD; market price: 88.940 USD; discount -0.375%; official product page current quote as of 2026-08-14
- Distribution yield: 6.43% as of 2026-08-14, from the official product page; issuer annualized-distribution measure, not total return

### Annual NAV TR

| Year | DLS NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 7.00% | 11.96% |
| 2017 | 30.95% | 21.83% |
| 2018 | -18.69% | -4.38% |
| 2019 | 22.11% | 31.49% |
| 2020 | -1.23% | 18.40% |
| 2021 | 11.66% | 28.71% |
| 2022 | -17.36% | -18.11% |
| 2023 | 15.40% | 26.29% |
| 2024 | 3.24% | 25.02% |
| 2025 | 33.49% | 17.88% |

2016-2025 DLS CAGR 7.27% vs S&P 500 TR CAGR 14.82%, a -7.55 percentage-point spread. 2021-2025 DLS CAGR 7.97% vs S&P 500 TR CAGR 14.43%, a -6.46 percentage-point spread. Calculations use rounded official annual inputs.

## Up years / Down years

- Up years: 7; down years: 3
- Best year: 2025, +33.49%
- Least-positive year: 2024, +3.24%
- Worst year: 2018, -18.69%
- Least-bad down year: 2020, -1.23%

## Risk read-through

ช่วง 2021-2025 ค่าเฉลี่ยของปีบวกคือ 15.95% และปีแย่สุดคือ -17.36%. The official [DLS presentation](https://www.wisdomtree.com/us/media/dls-presentation) reports risk metrics as of 2026-03-31: standard deviation since inception 17.67%, Sharpe ratio 0.24, down capture 95.51% และ beta 0.95. ความเสี่ยงหลักคือ small-cap liquidity/volatility, country and currency exposure, foreign withholding tax, dividend reduction, และ tracking/non-correlation risk; SEC prospectus ระบุ fund เป็น non-diversified. Official daily NAV history สำหรับคำนวณ maximum drawdown และ recovery ไม่ได้ยืนยัน จึงบันทึกเป็น not disclosed และไม่ใช้ secondary numeric proxy.

## Recent distributions

| Ex-date | Payable date | Total distribution (USD) |
|---|---|---:|
| 2026-06-25 | 2026-06-29 | 1.43500 |
| 2026-03-26 | 2026-03-30 | 0.16500 |
| 2025-12-26 | 2025-12-30 | 0.83275 |
| 2025-09-25 | 2025-09-29 | 0.59000 |

Distributions เป็น cash-flow ที่แยกจาก NAV TR ซึ่งคำนวณโดยสมมติ reinvestment.

## Sources

- [Official WisdomTree product page](https://www.wisdomtree.com/us/products/equity/dls)
- [Official DLS factsheet](https://www.wisdomtree.com/-/media/us-media-files/documents/resource-library/fund-fact-sheets/international-equity/wisdomtree-factsheet-dls-1050.ashx?la=en)
- [Official DLS presentation](https://www.wisdomtree.com/us/media/dls-presentation)
- [Official WTISDI methodology](https://www.wisdomtree.com/us/indexes/wtisdi)
- [SEC summary prospectus](https://www.sec.gov/Archives/edgar/data/1350487/000121465923010467/dls497k.htm)
- [S&P 500 index reference](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- Source batch: [[ETF_performance_sources_2026-08-16]]
