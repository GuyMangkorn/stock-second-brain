---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:RWJ
ticker: RWJ
exchange: NYSE Arca
fund: Invesco S&P SmallCap 600 Revenue ETF
tracked_index: S&P SmallCap 600 Revenue-Weighted Index
benchmark: S&P 500 Total Return
updated: 2026-08-29
performance_as_of: 2026-08-26
calendar_years_as_of: 2025-12-31
current_ytd_as_of: 2026-08-26
price_nav_as_of: 2026-08-28
source_batch: raw/imports/ETF_performance_sources_2026-08-29.md
return_basis: official NAV total return; secondary dividend-reinvested total-return proxy for current fields where official current NAV is not disclosed
tags:
  - analysis/etf-performance
  - ticker/RWJ
  - geography/United-States
---

# RWJ Performance

> Navigation: [[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]

## Bottom line

RWJ เป็น passive/index-tracking U.S. small-cap equity ETF ที่ติดตาม S&P SmallCap 600 Revenue-Weighted Index. Invesco ระบุว่ากองทุนลงทุนอย่างน้อย 90% ในองค์ประกอบของดัชนีและใช้ full replication โดยให้น้ำหนักตามรายได้. Factsheet official ล่าสุดที่อ่านได้ (2026-03-31) ให้ rolling 10-year NAV total return `12.06%` และมี calendar-year NAV rows ครบ 2016-2025; จึงใช้ official NAV เป็นตารางหลักแทน proxy เดิม. Current YTD ล่าสุดที่เข้าถึงได้เป็น secondary dividend-reinvested total-return `26.53%` ณ 2026-08-26 ขณะที่ official current NAV/YTD หลัง factsheet ยังไม่พบข้อมูลที่ยืนยันได้.

## Performance check

- entity_key: NYSE Arca:RWJ
- Inception: 2008-02-19
- Metric: total return with distributions reinvested; official Invesco rows are NAV-based and net of fund expenses, while current/drawdown fields marked `*` are secondary observations
- Tracked index (issuer benchmark): S&P SmallCap 600 Revenue-Weighted Index
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark only)
- Expense ratio: `0.39%` (official Invesco factsheet and SEC summary prospectus)
- Official standardized returns as of 2026-03-31:

| Window | RWJ NAV TR | RWJ market-price TR | Revenue-weighted index | S&P SmallCap 600 comparison |
|---|---:|---:|---:|---:|
| YTD | 3.92% | 3.96% | 3.98% | 3.51% |
| 1Y | 25.49% | 25.54% | 25.89% | 20.50% |
| 3Y annualized | 11.93% | 11.95% | 12.32% | 10.51% |
| 5Y annualized | 7.10% | 7.04% | 7.45% | 4.49% |
| 10Y annualized | 12.06% | 12.07% | 12.35% | 9.90% |
| Since inception annualized | 11.50% | 11.50% | 12.04% | 9.63% |

- Official 2016-2025 NAV total-return cumulative: `214.96%`; rounded-input CAGR: `12.16%`
- Official 2021-2025 NAV total-return cumulative: `90.50%`; rounded-input CAGR: `13.76%`
- Latest secondary current total-return proxy: `26.53%*` YTD and `30.62%*` 1Y as of 2026-08-26; this is later than the prior `28.61%*` snapshot as of 2026-08-14
- Latest secondary market-price cross-check: `US$61.64` close and price-only YTD `25.43%` as of 2026-08-28; no same-date official NAV was exposed

| Year | RWJ NAV TR† | Revenue index TR† | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | 30.52% | 31.36% | 11.96% |
| 2017 | 5.17% | 5.48% | 21.83% |
| 2018 | -16.87% | -16.79% | -4.38% |
| 2019 | 20.25% | 20.45% | 31.49% |
| 2020 | 20.49% | 20.39% | 18.40% |
| 2021 | 52.93% | 53.30% | 28.71% |
| 2022 | -11.03% | -10.72% | -18.11% |
| 2023 | 16.42% | 16.75% | 26.29% |
| 2024 | 11.55% | 11.88% | 25.02% |
| 2025 | 7.81% | 8.22% | 17.88% |

`†` Official Invesco factsheet observations as of 2026-03-31. S&P 500 rows reuse the project’s cached USD total-return convention for complete calendar years 2016-2025.

## Up years / Down years

- Up years / Down years: `8 / 2` across complete official calendar years 2016-2025
- Best: 2021, `52.93%†`
- Least positive: 2017, `5.17%†`
- Worst: 2018, `-16.87%†`
- Least bad down year: 2022, `-11.03%†`
- Official 2021-2025 rounded-input CAGR: `13.76%†`; common S&P 500 reference CAGR: `14.43%`; arithmetic difference: `-0.67 pp`, not alpha

## Risk read-through

RWJ เป็น small-cap revenue-weighted exposure จึงมี small-cap, cyclicality, liquidity และ sector-concentration risk. SEC prospectus ระบุ best quarter `+40.49%` ณ 2021-03-31 และ worst quarter `-37.74%` ณ 2020-03-31; ทั้งคู่เป็น quarter observations ไม่ใช่ maximum drawdown. Secondary total-return history reports maximum drawdown `-55.97%` ณ 2009-03-09 จาก peak 2008-09-19 และ current drawdown `-2.44%` ณ 2026-08-26 จาก peak 2026-08-04; recovery date ไม่ได้เปิดเผยใน source. Sample standard deviation ของ official annual rows ที่แสดงคือ `19.93%`; ไม่ใช่ daily NAV volatility.

## Driver notes

- Confirmed structure: passive full-replication exposure to the S&P SmallCap 600 Revenue-Weighted Index; revenue weighting can create factor and sector tilts relative to market-cap-weighted small-cap exposure.
- Official RWJ-minus-index gaps as of 2026-03-31 are `-0.06 pp` YTD, `-0.40 pp` 1Y, `-0.39 pp` 3Y, `-0.35 pp` 5Y, `-0.29 pp` 10Y and `-0.54 pp` since inception. These are implementation, fee, tax and timing observations, not alpha.
- Current secondary rolling context through 2026-08-26 is 2Y `39.32%*` (`18.03%*` annualized), 3Y `68.22%*` (`18.93%*` annualized), 5Y `68.09%*` (`10.94%*` annualized) and 10Y `251.61%*` (`13.40%*` annualized). These fields are not mixed with the official March factsheet windows.
- The official issuer benchmark is the revenue-weighted index; S&P 500 TR is retained only as a common large-cap reference and should not be read as RWJ’s tracking benchmark.

## Sources

- [Invesco RWJ factsheet](https://www.invesco.com/content/dam/invesco/us/en/product-documents/etf/fact-sheet/rwj-invesco-s-p-smallcap-600-revenue-etf-fact-sheet.pdf) — official standardized NAV/market/index returns, calendar rows, holdings, characteristics, yield and fee as of 2026-03-31
- [Invesco RWJ product page](https://www.invesco.com/us/en/financial-products/etfs/invesco-sp-smallcap-600-revenue-etf.html) — official product and strategy discovery
- [SEC RWJ summary prospectus](https://www.sec.gov/Archives/edgar/data/1378872/000119312525325669/d54028d497k.htm) — identity, objective, index method, passive treatment, fee, risks, inception and issuer average annual return through 2024-12-31
- [TotalRealReturns RWJ comparison](https://totalrealreturns.com/n/RWJ%2CXMMO) — secondary dividend-reinvested current/rolling returns, annual rows and drawdown proxy through 2026-08-26
- [Barchart RWJ performance](https://www.barchart.com/etfs-funds/quotes/RWJ/performance) — secondary market-price and price-only YTD cross-check through 2026-08-28
- [AAII RWJ profile](https://www.aaii.com/etf/ticker/RWJ?via=emailsignup-readmore) — secondary standardized performance and asset snapshot through 2026-07-31
- [ETF Research Center RWJ profile](https://www.etfrc.com/RWJ) — secondary holdings/assets and standardized performance cross-check through 2026-07-31
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common benchmark definition
- Cached S&P 500 TR references: [S&P DJI historical research](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [2023 U.S. Equities Market Attributes](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), and [2025 S&P DJI market attributes](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/); reference as-of 2025-12-31
- ETF source batch: [[ETF_performance_sources_2026-08-29]] | [[ETF Performance Index]]
