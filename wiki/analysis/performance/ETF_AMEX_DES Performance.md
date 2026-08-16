---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:DES
ticker: DES
exchange: NYSE Arca
fund: WisdomTree U.S. SmallCap Dividend Fund
tracked_index: WisdomTree U.S. SmallCap Dividend Index
benchmark: S&P 500 Total Return
updated: 2026-08-17
performance_as_of: 2026-07-31
rolling_10y_as_of: 2026-07-31
current_ytd_as_of: 2026-07-31
price_nav_as_of: 2026-08-14
distribution_as_of: 2026-07-28
source_batch: raw/imports/ETF_performance_sources_2026-08-17.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/DES
  - geography/United-States
---

# DES Performance

> Navigation: [[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]

## Bottom line

DES ให้ cumulative NAV Total Return `106.62%` หรือ rounded-input CAGR `7.53%`
ใน complete calendar years 2016-2025 เทียบ S&P 500 TR ที่ `298.33%` / `14.82%`.
ช่วง 2021-2025 ให้ cumulative `44.59%` และ CAGR `7.65%`. ผลตอบแทนรายปีเป็นบวก
7 ปีและลบ 3 ปี; ปีที่ดีที่สุดคือ 2016 ที่ `31.06%` และแย่ที่สุดคือ 2018 ที่
`-12.74%`. Current YTD NAV TR ล่าสุดจาก issuer คือ `22.93%` ณ 31 ก.ค. 2026;
NAV ล่าสุดคือ `$41.676` ณ 14 ส.ค. 2026.

## Performance check

- `entity_key: NYSE Arca:DES`; fund: WisdomTree U.S. SmallCap Dividend Fund
- Inception: `2006-06-16`; exchange: `NYSE Arca`
- Expense ratio: `0.38%` gross/net ตาม issuer ณ 14 ส.ค. 2026
- Metric: `NAV Total Return` รวม dividends/distributions ที่ reinvested และ fund expenses; currency USD
- Tracked index: `WisdomTree U.S. SmallCap Dividend Index (WTSDI)`; กองทุนใช้ passive/indexing approach และ representative sampling
- Common benchmark: `S&P 500 Total Return` (USD, dividends reinvested; ใช้เป็น reference benchmark ไม่ใช่ issuer benchmark)
- Official rolling 10-year NAV TR: `8.04%` average annual return ณ 31 ก.ค. 2026; issuer ไม่เปิดเผย raw rolling endpoints ใน capture ที่ตรวจ
- Calendar-window calculation: 2016-01-01 ถึง 2025-12-31; Start TR index `100.00`, End TR index `206.62`, Years `10.00`; สูตร `(206.62 / 100.00)^(1 / 10.00) - 1 = 7.53%`. เป็น rounded-input approximation จาก annual rows ทางการ 10 แถว
- Coverage: annual NAV TR rows ครบ 2016-2025 โดยไม่มี proxy หรือ partial-year marker; current YTD เป็น month-end 31 ก.ค. 2026 และ quote เป็น 14 ส.ค. 2026

| ปี | ETF NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 31.06% | 11.96% |
| 2017 | 8.66% | 21.83% |
| 2018 | -12.74% | -4.38% |
| 2019 | 20.30% | 31.49% |
| 2020 | -4.41% | 18.40% |
| 2021 | 26.71% | 28.71% |
| 2022 | -10.94% | -18.11% |
| 2023 | 16.40% | 26.29% |
| 2024 | 9.79% | 25.02% |
| 2025 | 0.26% | 17.88% |

## Up years / Down years

- Up years / Down years: `7 / 3`
- Best: `2016`, `31.06%`
- Least positive: `2025`, `0.26%`
- Worst: `2018`, `-12.74%`
- Least bad down year: `2020`, `-4.41%`
- 2021-2025: DES cumulative `44.59%`, CAGR `7.65%`; S&P 500 cumulative `96.17%`, CAGR `14.43%`
- Current YTD: DES `22.93%` NAV TR ณ 31 ก.ค. 2026. Official S&P 500 TR current fieldที่ตรวจพบคือ `14.04%` ณ 10 ส.ค. 2026; วันอ้างอิงไม่ตรงกัน จึงไม่สรุปเป็น same-date spread

## Risk read-through

จาก annual NAV TR rows, sample standard deviation แบบคำนวณได้คือ `15.30%` ต่อปี
(ใช้ annual observations 2016-2025 ไม่ใช่ daily volatility). Year-end-observation
drawdown approximation อยู่ที่ประมาณ `-12.74%` ในปี 2018 และ cumulative year-end
กลับขึ้นเหนือจุดสูงสุดก่อนหน้าได้ภายในสิ้นปี 2019; นี่ไม่ใช่ daily maximum drawdown.

DES เป็น U.S. small-cap dividend factor ETF จึงมีความเสี่ยงจาก small-cap liquidity,
sector concentration, dividend cuts, rates และ equity drawdowns. ตัวเลข annual
return สะท้อน index construction และ tracking หลังหัก fund expenses ไม่ใช่หลักฐาน
ของ discretionary stock selection.

## Driver notes

- WTSDI เป็น fundamentally weighted dividend-paying U.S. small-cap index โดยคัดกลุ่ม small-cap หลังตัดบริษัทใหญ่สุด 300 แห่งออกตาม methodology ของ issuer
- 2018 เป็น down year ที่แย่ที่สุดในช่วงที่ตรวจ; 2020 เป็น down year ที่ขาดทุนน้อยที่สุด ขณะที่ 2021-2022 สะท้อน cycle sensitivity
- Product page แสดง latest four cash distributions รวม `$0.305` โดยรายการล่าสุด `$0.045` ex/pay 28/30 ก.ค. 2026; distribution yield ที่แสดงคือ `1.30%` ณ 14 ส.ค. 2026 ซึ่งไม่ใช่ NAV total return
- Current NAV/market price เป็นคนละ field: NAV `$41.676` และ market price `$41.730` ณ 14 ส.ค. 2026

## Sources

- [WisdomTree DES product page](https://www.wisdomtree.com/us/products/equity/des) — fund facts, NAV/price, official month-end YTD/rolling performance, and distributions
- [WisdomTree DES Q1-2026 presentation](https://www.wisdomtree.com/us/media/des-presentation) — official 2016-2025 calendar NAV rows, expense, and methodology
- [WisdomTree DES quarterly factsheet](https://www.wisdomtree.com/us/media/wisdomtree-factsheet-des-1008) — official exchange, inception, return definition, and index identity
- [SEC DES summary prospectus](https://www.sec.gov/Archives/edgar/data/1350487/000121465925011322/des73125497k.htm) — passive indexing, fees, listing, and return definitions
- [WisdomTree U.S. SmallCap Dividend Index](https://www.wisdomtree.com/us/indexes/wtsdi) — issuer benchmark methodology
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common benchmark definition
- [S&P 500 current return page](https://www.spglobal.com/spdji/en/additional-reports/all-returns/index.dot?parentIdentifier=f33eb5c2-5231-4c16-bc59-38407c3d2f2f&sourceIdentifier=home-page) — official current S&P 500 TR field `14.04%` displayed for 10 ส.ค. 2026
- [S&P 500 cached source 1](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [source 2](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), [source 3](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-2021/), [source 4](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/) — cached 2016-2025 USD gross S&P 500 TR rows
- Source batch: [[ETF_performance_sources_2026-08-17]]
