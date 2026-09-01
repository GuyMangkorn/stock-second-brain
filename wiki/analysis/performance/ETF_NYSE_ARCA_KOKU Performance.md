---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:KOKU
ticker: KOKU
exchange: NYSE Arca
fund: Xtrackers MSCI Kokusai Equity ETF
tracked_index: MSCI Kokusai Index (Net)
benchmark: MSCI Kokusai Index (Net)
updated: 2026-09-01
performance_as_of: 2026-08-29
annual_rows_as_of: 2026-03-31
current_ytd_as_of: 2026-08-29
source_batch: raw/imports/ETF_performance_sources_2026-09-01_run-6.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/KOKU
  - geography/International
---

# KOKU Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

KOKU เป็น passive developed-markets ex-Japan equity ETF ที่ติดตาม MSCI Kokusai Index. Verified NAV TR rows ครอบคลุม 2021-2024 จาก DWS และ 2025 เป็น secondary proxy `*`; ช่วง 2021-2025 ให้ผลสะสม `83.57%` หรือ rounded-input CAGR `12.92%`, ต่ำกว่า S&P 500 TR ที่ `17.41%` ต่อปี. Latest secondary YTD คือ `+13.09%` ณ 2026-08-29; 2020 เป็น inception-year partial และไม่ถูกจัดอันดับ.

## Performance check

- entity_key: NYSE Arca:KOKU
- Fund: Xtrackers MSCI Kokusai Equity ETF
- Classification: passive index-tracking equity ETF using full replication where practicable; no leverage, inverse, option-income, bond, commodity, currency, multi-asset or derivative-defined payoff was identified
- Inception: 2020-04-07; net expense ratio: 0.09% as of 2026-03-31; exchange: NYSE Arca
- Tracked index: MSCI Kokusai Index (Net), also known as MSCI World ex Japan, covering large- and mid-cap developed-market equities excluding Japan
- Return basis: NAV Total Return assumes dividends and distributions are reinvested; market-price return is kept separate
- Latest YTD cross-check: secondary dividend-reinvested total return `13.09%` as of 2026-08-29
- 2021-2025: cumulative `83.57%`; rounded-input CAGR `12.92%`; 2025 row is a marked secondary proxy
- Common benchmark: S&P 500 Total Return in USD with dividends reinvested; cached reference as of 2025-12-31 and used only as a broad reference

### Annual NAV TR

| Calendar year | KOKU NAV TR | S&P 500 TR |
|---|---:|---:|
| 2021 | 23.81% | 28.71% |
| 2022 | -17.96% | -18.11% |
| 2023 | 24.38% | 26.29% |
| 2024 | 19.64% | 25.02% |
| 2025* | 21.45% | 17.88% |

จาก rounded annual inputs, 2021-2025 KOKU CAGR `12.92%` เทียบ S&P `17.41%` เป็น spread `-4.49` percentage points. The DWS prospectus exposes official calendar rows through 2024; `2025*` is a secondary dividend-reinvested proxy and is not silently treated as an issuer row. ปี 2020 ถูกตัดออกเพราะเป็น inception-year partial.

## Up years / Down years

- Up years: 4; down years: 1
- Best year: 2023, +24.38%
- Least-positive year: 2024, +19.64%
- Worst year: 2022, -17.96%
- Least-bad down year: 2022, -17.96%

## Risk read-through

KOKU มี developed-market, country/currency, large-cap, concentration, liquidity และ index-tracking risk; fund ไม่ hedge foreign-currency exposure. Calendar-row population standard deviation 2021-2025 อยู่ที่ประมาณ `16.20%`; DWS factsheet รายงาน beta `1.04` ณ 2026-03-31 และ turnover rate `2%` ใน SEC summary prospectus. Daily NAV history สำหรับ maximum drawdown และ recovery ไม่ได้ยืนยัน จึงบันทึกเป็น `not disclosed`. The secondary 2025 row and current YTD are kept separate from DWS’s official 2021-2024 calendar rows.

## Sources

- [Official Xtrackers KOKU factsheet](https://etf.dws.com/en-us/AssetDownload/Index/94ec1d01-afbe-4684-8d4a-497c224fb2e5/KOKU-Fact-Sheet.pdf) — identity, index, inception, fees, official rolling returns and risk fields
- [Official KOKU prospectus](https://etf.dws.com/en-us/AssetDownload/Index/cfabbe07-bfc5-49c6-9de2-15429c72ad99/KOKU-1.pdf) — NYSE Arca listing, passive strategy and official 2021-2024 calendar rows
- [SEC KOKU summary prospectus](https://www.sec.gov/Archives/edgar/data/1503123/000008805325001122/k121925koku.htm) — objective, strategy, fees, turnover and management disclosures
- [Secondary KOKU total-return history](https://portfolioslab.com/symbol/KOKU) — current YTD and 2025 proxy, last updated 2026-08-29
- Source batch: [[ETF_performance_sources_2026-09-01_run-6]]
