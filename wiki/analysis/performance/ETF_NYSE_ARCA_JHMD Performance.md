---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:JHMD
ticker: JHMD
input_ticker: JHMD
exchange: NYSE Arca
fund: John Hancock Multifactor Developed International ETF
tracked_index: John Hancock Dimensional Developed International Index
benchmark: S&P 500 Total Return
updated: 2026-09-01
performance_as_of: 2026-03-31
calendar_years_as_of: 2025-12-31
current_ytd_as_of: 2026-07-31
fund_facts_as_of: 2026-03-31
source_batch: raw/imports/ETF_performance_sources_2026-09-01_run-6.md
return_basis: NAV total return
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/JHMD
  - geography/International
  - geography/global-developed
---

# JHMD Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

JHMD เป็น John Hancock Multifactor Developed International ETF ที่จดทะเบียนบน
NYSE Arca. กองทุนใช้ passive index approach เพื่อ track John Hancock Dimensional
Developed International Index และเน้น developed-market หุ้นนอก North America
ผ่าน size, value และ profitability factors.

Official factsheet ณ 31 มี.ค. 2026 รายงาน NAV YTD `+0.08%`, 1-year `+23.26%`,
3-year annualized `+14.40%`, 5-year annualized `+8.36%` และ since inception
annualized `+8.53%`; 10-year field ยังไม่มีเพราะ share class เริ่ม 15 ธ.ค. 2016.
Latest YTD ที่ยืนยันได้คือ secondary NAV observation `+11.6%` ณ 31 ก.ค. 2026.
จาก secondary annual NAV rows สำหรับปีเต็ม 2017-2025, JHMD มี cumulative
`115.54%` หรือ rounded-input CAGR `8.91%`; เทียบกับ S&P 500 TR `255.78%` หรือ
`15.14%` ต่อปี. ช่วง 2021-2025 JHMD ทำ CAGR `9.29%` เทียบกับ S&P 500 `14.43%`.

## Performance check

- `entity_key: NYSE Arca:JHMD`; input ticker: `JHMD`; listing exchange: NYSE Arca
- Classification: supported passive/index-tracking developed international multifactor equity ETF
- Inception: 15 ธ.ค. 2016; gross expense ratio `0.43%`; net expense ratio `0.39%` through 31 ส.ค. 2026; distributions are reinvested in total-return figures
- Metric: `NAV Total Return` in USD with reinvested distributions; market-price return remains separate
- Tracked index (issuer benchmark): `John Hancock Dimensional Developed International Index`
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference benchmark ไม่ใช่ tracked index ของกองทุน)
- Official standardized performance as of 31 มี.ค. 2026: NAV YTD `+0.08%`, 1-year `+23.26%`, 3-year annualized `+14.40%`, 5-year annualized `+8.36%`, since inception annualized `+8.53%`; 10-year `not available`
- Latest current YTD cross-check: secondary NAV `+11.6%` as of 31 ก.ค. 2026; no same-date official issuer NAV YTD field was established in this capture
- 2017-2025 calendar NAV TR: cumulative `115.54%`; rounded-input CAGR `8.91%`
- 2021-2025 calendar NAV TR: cumulative `55.92%`; rounded-input CAGR `9.29%`
- Annual rows are marked secondary because the retrieved issuer factsheet provides standardized periods but not a text calendar-year table; official and secondary return bases are kept separate.

| Year | JHMD NAV TR* | S&P 500 TR |
|---|---:|---:|
| 2017 | 25.20% | 21.83% |
| 2018 | -13.90% | -4.38% |
| 2019 | 20.30% | 31.49% |
| 2020 | 6.60% | 18.40% |
| 2021 | 11.70% | 28.71% |
| 2022 | -13.90% | -18.11% |
| 2023 | 19.10% | 26.29% |
| 2024 | 2.50% | 25.02% |
| 2025 | 32.80% | 17.88% |

\* Annual JHMD rows are rounded secondary data; they are not substituted for official standardized issuer fields.

## Up years / Down years

- Up years / Down years: `7 / 2` across complete calendar years 2017-2025
- Best: 2025, `+32.80%`; least positive: 2024, `+2.50%`
- Worst: 2018 and 2022, both `-13.90%`; least-bad down year: tie at `-13.90%`
- 2017-2025 rounded-input CAGR: `8.91%`; 2021-2025 rounded-input CAGR: `9.29%`
- Latest secondary NAV YTD is `+11.6%` as of 31 ก.ค. 2026; no synchronized S&P 500 YTD comparison is asserted.

## Risk read-through

JHMD มี factor exposure ต่อ smaller-cap, lower-relative-price และ higher-profitability
หุ้นใน developed markets จึงอาจต่างจาก cap-weighted MSCI EAFE และมี factor-cycle,
country, currency, equity-market, liquidity และ tracking-error risks. Official
factsheet ระบุ 1 fund manager structure and a net fee waiver through 31 ส.ค. 2026;
รายงานยังมี 10-year return ไม่ได้เพราะประวัติไม่ครบ. Secondary risk table รายงาน
beta `0.90` และ standard deviation `13.0%` ณ 31 ก.ค. 2026; values นี้ไม่ใช่
issuer-confirmed daily metrics. Annual-return population dispersion จาก rows
2017-2025 อยู่ที่ `15.47%`; daily NAV history สำหรับ maximum drawdown/recovery ยัง
ไม่ถูกยืนยัน จึงเป็น `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- [John Hancock official JHMD factsheet](https://www.jhinvestments.com/content/dam/jhi-investments/JHINV/public/ETFs/Documents/FactSheets/InvestorFactSheet/etf-multifactor-developed-international-investor-fact-sheet-jhi.pdf) — official objective, index, inception, fees, standardized NAV/market-price returns, strategy and risk disclosures; as of 31 มี.ค. 2026
- [SEC JHMD summary prospectus](https://www.sec.gov/Archives/edgar/data/1478482/000119312525191988/d911861d497k.htm) — official ticker/exchange, passive objective, index and risk disclosure
- [AAII JHMD annual-return table](https://www.aaii.com/etfs/summary?ticker=JHMD) — secondary 31 ก.ค. 2026 current-YTD, annual NAV rows and risk cross-check
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common benchmark definition
- Cached S&P 500 TR references: [S&P DJI historical research](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [2023 U.S. Equities Market Attributes](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), [2021 S&P DJI market attributes](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/), and [2025 S&P DJI market attributes](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/); cached USD Total Return convention as of 31 ธ.ค. 2025
- ETF source batch: [[ETF_performance_sources_2026-09-01_run-6]] | [[ETF Performance Index]]

---
window: complete calendar years 2017-2025 plus current 2026 YTD
return_basis: NAV total return
verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
---
