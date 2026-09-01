---
type: etf-performance
instrument_type: ETF
entity_key: Cboe BZX:ICOW
ticker: ICOW
exchange: Cboe BZX
fund: Pacer Developed Markets International Cash Cows 100 ETF
tracked_index: Pacer Developed Markets International Cash Cows 100 Index
benchmark: MSCI World Index
updated: 2026-09-01
performance_as_of: 2026-07-31
annual_rows_as_of: 2025-08-31
current_ytd_as_of: 2026-07-31
source_batch: raw/imports/ETF_performance_sources_2026-09-01_run-5.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/ICOW
  - geography/International
---

# ICOW Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

ICOW เป็น passive developed-markets ex-US equity ETF ที่คัดหุ้น large/mid-cap จำนวน 100 บริษัทด้วย free-cash-flow yield และ weighting ที่อิง trailing FCF. ชุด calendar-year NAV TR ที่ยืนยันได้จาก SEC summary prospectus สำหรับ 2018-2024 ให้ผลสะสม `30.01%` หรือ rounded-input CAGR `3.82%`, ต่ำกว่า S&P 500 Total Return ที่ `13.84%` ต่อปีในช่วงเดียวกัน; ช่วง 2021-2024 CAGR อยู่ที่ `4.39%` เทียบ S&P `13.58%`. Current secondary cross-check ณ 2026-07-31 รายงาน NAV YTD `13.9%`; calendar-year 2025 และ 2026 ยังไม่ถูก backfill เพราะ official annual row ที่ยืนยันได้ไม่ครบ.

## Performance check

- entity_key: Cboe BZX:ICOW
- Fund: Pacer Developed Markets International Cash Cows 100 ETF
- Classification: passive index-tracking developed international equity ETF; no leverage, inverse, option-income, bond, commodity, currency, multi-asset or derivative-defined payoff was identified
- Inception: 2017-06-16; total expense ratio: 0.65%; exchange: Cboe BZX
- Tracked index: Pacer Developed Markets International Cash Cows 100 Index; current SEC summary prospectus identifies MSCI World Index as the broad benchmark after a benchmark change
- Return basis: NAV Total Return before/after fund expenses as stated by the relevant source; annual rows below are fund NAV rows, not index backtest data
- Current secondary cross-check as of 2026-07-31: NAV YTD 13.9%; the source also reports 1-year 32.2%, 3-year annualised 15.8%, and 5-year annualised 10.5%. These current fields are kept secondary because the accessible official Pacer annual factsheet is dated 2025-09-30
- Official SEC summary prospectus dated 2025-08-31 reports 2024 return before taxes -2.24%, 5-year annualised 5.06%, and since-inception annualised 5.46%; the same document reports index returns of -1.56%, 5.98%, and 6.40% for those periods
- 2018-2024: cumulative 30.01%; rounded-input CAGR 3.82%
- 2021-2024: cumulative 18.77%; rounded-input CAGR 4.39%
- Common benchmark: S&P 500 Total Return in USD with dividends reinvested; cached reference as of 2025-12-31 and used only as a broad reference

### Annual NAV TR

| Calendar year | ICOW NAV TR | S&P 500 TR |
|---|---:|---:|
| 2018 | -13.34% | -4.38% |
| 2019 | 17.23% | 31.49% |
| 2020 | 7.75% | 18.40% |
| 2021 | 10.62% | 28.71% |
| 2022 | -7.43% | -18.11% |
| 2023 | 18.64% | 26.29% |
| 2024 | -2.24% | 25.02% |

The official SEC bar chart states that these are fund NAV returns for calendar years ended December 31. A secondary total-return series retrieved during research reports different values for some overlapping years; it was not mixed into this table. The official SEC series is prioritized for historical annual rows, and 2025 is recorded as `not disclosed` in the official packet rather than filled from the conflicting secondary series. จาก rounded inputs, 2018-2024 ICOW CAGR `3.82%` เทียบ S&P `13.84%` เป็น spread `-10.02` percentage points; 2021-2024 spread คือ `-9.19` percentage points.

## Up years / Down years

- Up years: 4; down years: 3; 2025 and 2026 YTD are excluded because a complete official annual row was not established
- Best year: 2023, +18.64%
- Least-positive year: 2020, +7.75%
- Worst year: 2018, -13.34%
- Least-bad down year: 2024, -2.24%

## Risk read-through

ICOW มี value/FCF-yield, dividend, country, currency, sector และ non-U.S. equity risk; holdings อาจกระจุกตัวตาม index rebalance และ official SEC ระบุว่า index มี significant exposure ต่อ industrials ณ 2025-06-30. Rules-based screening ไม่ใช่ manager skill และผลต่างจาก index ต้องพิจารณา expense, turnover, transaction cost, local-market close และ fair-value/NAV timing. Official SEC ระบุ best quarter `+24.37%` ใน Q4 2020 และ worst quarter `-28.31%` ใน Q1 2020; นี่เป็น quarterly extremes ไม่ใช่ maximum drawdown. Daily NAV history สำหรับ maximum drawdown และ recovery ไม่ได้ยืนยัน จึงบันทึกเป็น `not disclosed` และไม่ใช้ secondary proxy.

## Sources

- [Official Pacer ICOW product resources](https://www.paceretfs.com/resources/product/icow)
- [Official ICOW factsheet](https://www.paceretfs.com/media/icow.pdf)
- [Official SEC summary prospectus, August 31 2025](https://www.sec.gov/Archives/edgar/data/1616668/000089418925006679/pacerdevelopedmarketsinter.htm)
- [Official Pacer/SEC prior summary with the earlier annual rows](https://www.sec.gov/Archives/edgar/data/1616668/000089418924005245/pacericowsummary.htm)
- [Official index methodology](https://www.indexdesigngroup.com/indexes/cash-cows-series/pacer-developed-markets-international-cash-cows-100-index/)
- [Secondary current performance cross-check](https://www.aaii.com/etf/ticker/ICOW)
- Source batch: [[ETF_performance_sources_2026-09-01_run-5]]
