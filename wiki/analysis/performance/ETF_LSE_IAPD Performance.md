---
type: etf-performance
instrument_type: ETF
entity_key: LSE:IAPD
ticker: IHSEF
exchange: LSE
fund: iShares Asia Pacific Dividend UCITS ETF
tracked_index: Dow Jones Asia/Pacific Select Dividend 50 Index (Net)
benchmark: S&P 500 Total Return
updated: 2026-07-24
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-07-21
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/IHSEF
  - geography/Asia-Pacific
---

# IHSEF Performance

> Navigation: [[ETF Region Index]] → [[Asia-Pacific ETF]] → [[ETF Performance Index]]

## Bottom line

IHSEF เป็น input OTC alias ของ iShares Asia Pacific Dividend UCITS ETF; issuer ระบุ canonical London Stock Exchange listing เป็น `IAPD` และกองทุนเป็น physical/replicated passive equity ETF ที่ track Dow Jones Asia/Pacific Select Dividend 50 Index (Net). Official iShares page ณ 2026-06-30 ยืนยัน rolling 10-year NAV Total Return CAGR `6.75%` สำหรับ 2016-06-30 ถึง 2026-06-30 หรือ `10.00` elapsed years. Raw NAV endpoints ไม่ได้เปิดเผย; normalized TR start `100.00` และ end ประมาณ `192.17` เป็นค่าคำนวณจาก CAGR ที่ issuer ปัดเศษ. Official calendar rows 2016-2025 มี NAV TR และ benchmark rows; current NAV TR YTD คือ `14.55%` ณ 2026-07-21.

## Performance check

- entity_key: LSE:IAPD
- Input alias: IHSEF; official issuer listing table confirms LSE:IAPD (GBP) and LSE:IDAP (USD) for the same ISIN `IE00B14X4T88`; this page keeps the existing canonical LSE:IAPD key and does not use a provider slug.
- Inception: 2006-06-02
- Metric: NAV Total Return with gross income reinvested where applicable; NAV performance is separate from market-price return
- Tracked index: Dow Jones Asia/Pacific Select Dividend 50 Index (Net)
- Structure: physical, replicated, passive/index-tracking equity ETF; distributing quarterly; TER `0.59%`
- 10-year NAV TR coverage: 2016-06-30 to 2026-06-30; actual years `10.00`
- 10-year NAV TR CAGR: `6.75%` (official issuer annualised return)
- Normalized NAV TR: start `100.00`; end `192.17` (calculated as `100 × (1 + 6.75%)^10`; raw endpoints not disclosed)
- Coverage/source note: official calendar rows are 2016-2025. iShares notes that the benchmark changed before 2020-06-22; benchmark rows remain separate from fund NAV TR. S&P 500 rows reuse the cached USD Total Return convention as of 2025-12-31.

| Year | IAPD NAV TR | Dow Jones Asia/Pacific Select Dividend 50 Index TR | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | 20.5% | 21.0% | 11.96% |
| 2017 | 16.6% | 16.8% | 21.83% |
| 2018 | -15.1% | -14.8% | -4.38% |
| 2019 | 14.4% | 14.9% | 31.49% |
| 2020 | -10.2% | -9.6% | 18.40% |
| 2021 | 4.0% | 4.4% | 28.71% |
| 2022 | -2.3% | -1.9% | -18.11% |
| 2023 | 13.8% | 14.3% | 26.29% |
| 2024 | 5.9% | 6.5% | 25.02% |
| 2025 | 29.7% | 30.4% | 17.88% |

## Up years / Down years

- Up years / Down years: `7 / 3` over complete calendar years 2016-2025
- Best complete calendar year: 2025, `29.7%`
- Least positive complete calendar year: 2021, `4.0%`
- Worst complete calendar year: 2018, `-15.1%`
- Least bad down year: 2022, `-2.3%`
- Calendar 2016-2025 rows compound to approximately `94.63%` / CAGR `6.89%` using the issuer's displayed one-decimal rows
- Common 2021-2025 rows compound to approximately `58.82%` / CAGR `9.69%`; S&P 500 common-window CAGR is `14.43%`, so IHSEF trails by approximately `4.74 pp`
- Current NAV TR YTD: `14.55%` as of 2026-07-21; NAV `US$31.26` as of 2026-07-21

## Risk read-through

IHSEF มี country, sector, currency และ dividend-factor concentration เพราะถือหุ้น Asia-Pacific จำนวน `50` ตัวและ rebalances annually. Official 3-year standard deviation คือ `14.36%` ณ 2026-06-30; trailing 12-month distribution yield คือ `4.14%` ณ 2026-07-16. Daily NAV history สำหรับ max drawdown และ recovery: `ไม่พบข้อมูลที่ยืนยันได้` ใน lean capture.

## Sources

- [Official iShares IAPD product and performance page](https://www.ishares.com/uk/professional/en/products/251567/iapd?siteEntryPassthrough=true&switchLocale=y)
- [Official iShares IAPD factsheet](https://www.ishares.com/uk/professional/en/literature/fact-sheet/iapd-ishares-asia-pacific-dividend-ucits-etf-fund-fact-sheet-en-gb.pdf?siteEntryPassthrough=true&switchLocale=y)
- [Official S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- ETF source batch: [[ETF_performance_sources_2026-07-24]] | [[ETF Performance Index]]
