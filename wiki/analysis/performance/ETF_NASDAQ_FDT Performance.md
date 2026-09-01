---
type: etf-performance
instrument_type: ETF
entity_key: NASDAQ:FDT
ticker: FDT
exchange: Nasdaq
fund: First Trust Developed Markets ex-US AlphaDEX Fund
tracked_index: Nasdaq AlphaDEX Developed Markets Ex-US Index
benchmark: MSCI World ex USA
updated: 2026-09-01
performance_as_of: 2026-07-31
annual_rows_as_of: 2026-03-31
current_ytd_as_of: 2026-07-31
source_batch: raw/imports/ETF_performance_sources_2026-09-01_run-5.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/FDT
  - geography/International
---

# FDT Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

FDT เป็น passive rules-based equity ETF ที่ใช้ Nasdaq AlphaDEX Developed Markets Ex-US Index เพื่อคัดหุ้น developed markets นอกสหรัฐ. Official calendar-year NAV TR 2016-2025 ให้ผลสะสม `126.34%` หรือ rounded-input CAGR `8.51%`; ช่วง 2021-2025 CAGR `10.77%`, ต่ำกว่า S&P 500 TR ที่ `14.43%` ต่อปี. Current official month-end performance ณ 2026-07-31 คือ NAV YTD `16.08%`, 1-year `35.50%`, 3-year annualised `23.02%`, 5-year `11.63%` และ 10-year `9.73%`; ตัวเลข 10-year นี้เป็น issuer-reported rolling return และไม่ใช่ CAGR ของ calendar rows ด้านล่าง.

## Performance check

- entity_key: NASDAQ:FDT
- Fund: First Trust Developed Markets ex-US AlphaDEX Fund
- Classification: passive index-tracking / strategic-beta equity ETF; no leverage, inverse, option-income, bond, commodity, currency, multi-asset or derivative-defined payoff was identified
- Inception: 2011-04-18; total expense ratio: 0.80% as of 2026-05-01; exchange: Nasdaq; holdings: 300
- Tracked index: Nasdaq AlphaDEX Developed Markets Ex-US Index; broad comparison in the official factsheet: MSCI World ex USA
- Return basis: NAV Total Return includes dividends and capital gains; market-price return is based on the official NBBO midpoint methodology and is kept separate
- Official current snapshot as of 2026-08-28: NAV USD 96.55, market price USD 96.23, assets USD 1,340,784,612, and 30-day SEC yield 1.68%
- Official current performance as of 2026-07-31: NAV YTD 16.08%, 1-year 35.50%, 3-year annualised 23.02%, 5-year annualised 11.63%, 10-year annualised 9.73%, and since inception annualised 6.77%
- 2016-2025: cumulative 126.34%; rounded-input CAGR 8.51%
- 2021-2025: cumulative 66.76%; rounded-input CAGR 10.77%
- Common benchmark: S&P 500 Total Return in USD with dividends reinvested; cached reference as of 2025-12-31 and used only as a broad reference

### Annual NAV TR

| Calendar year | FDT NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 3.55% | 11.96% |
| 2017 | 33.57% | 21.83% |
| 2018 | -19.52% | -4.38% |
| 2019 | 16.56% | 31.49% |
| 2020 | 4.61% | 18.40% |
| 2021 | 10.70% | 28.71% |
| 2022 | -18.57% | -18.11% |
| 2023 | 13.89% | 26.29% |
| 2024 | 7.02% | 25.02% |
| 2025 | 51.78% | 17.88% |

จาก rounded annual inputs, 2016-2025 FDT CAGR `8.51%` เทียบ S&P `14.82%` เป็น spread `-6.31` percentage points. ช่วง 2021-2025 FDT CAGR `10.77%` เทียบ S&P `14.43%` เป็น spread `-3.66` percentage points. The factsheet notes that the index history before 2015-10-13 reflects a prior index methodology; the table begins in 2016 but the caveat remains relevant to long-history interpretation.

## Up years / Down years

- Up years: 8; down years: 2
- Best year: 2025, +51.78%
- Least-positive year: 2024, +7.02%
- Worst year: 2018, -19.52%
- Least-bad down year: 2022, -18.57%

## Risk read-through

FDT มี factor/model risk, country/currency risk, developed ex-US equity risk, turnover/transaction-cost risk และ tracking risk. Calendar-row population standard deviation 2016-2025 อยู่ที่ประมาณ `20.31%`; official 3-year standard deviation ณ 2026-03-31 อยู่ที่ `16.00%`, beta `1.15`, Sharpe `1.06` และ correlation `0.93` เทียบ MSCI World ex USA. First Trust รายงานค่า `alpha` ใน factsheet แต่ไม่ควรตีความเป็น manager alpha เพราะ FDT เป็น index implementation และผลต่างขึ้นกับ factor exposure, benchmark, expenses และ window. Daily NAV history สำหรับ maximum drawdown และ recovery ไม่ได้ยืนยัน จึงบันทึกเป็น `not disclosed`.

## Sources

- [Official First Trust FDT summary](https://www.ftportfolios.com/Retail/etf/etfsummary.aspx?Ticker=fdt)
- [Official FDT factsheet](https://www.ftportfolios.com/Common/ContentFileLoader.aspx?ContentGUID=7fee07d6-8942-4b69-8923-e67e67e5df4d)
- [Official First Trust ETF performance list](https://www.ftportfolios.com/retail/etf/etflist.aspx?DisplayType=PerformanceNav&ViewAsList=1)
- Source batch: [[ETF_performance_sources_2026-09-01_run-5]]
