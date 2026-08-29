---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:CQQQ
ticker: CQQQ
exchange: NYSE Arca
fund: Invesco China Technology ETF
tracked_index: FTSE China Incl A 25% Technology Capped Index
benchmark: S&P 500 Total Return
updated: 2026-08-29
performance_as_of: 2025-12-31
current_ytd_as_of: not disclosed
source_batch: raw/imports/ETF_performance_sources_2026-08-29.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/CQQQ
  - geography/China
---

# CQQQ Performance

> Navigation: [[ETF Region Index]] → [[China ETF]] → [[ETF Performance Index]]

## Bottom line

CQQQ เป็น passive/full-replication China technology equity ETF ของ Invesco
ที่ติดตาม FTSE China Incl A 25% Technology Capped Index. มี official NAV TR
ครบ 10 calendar years 2016-2025; rows ที่ยืนยันได้ compound เป็น `54.48%`
หรือ CAGR `4.44%` จาก normalized TR 100.00 เป็น 154.48 ใน 10.00 complete
calendar years. Common window 2021-2025 ติดลบ `35.06%` หรือ CAGR `-8.27%`
เทียบกับ S&P 500 TR `14.43%`. Current official NAV YTD: `ไม่พบข้อมูลที่ยืนยันได้`
in the reviewed Invesco capture; the latest fully readable official performance
report is as of `2025-12-31`.

ตัวเลข 10 ปีนี้เป็น calendar-year coverage ไม่ใช่ rolling date-to-date window
และต้องอ่านร่วมกับ strategy-history caveat: SEC prospectus ระบุว่า CQQQ เป็น
successor to Guggenheim China Technology ETF หลัง reorganization เมื่อ
2018-05-18 และ blended index เปลี่ยนเป็น FTSE methodology ปัจจุบันเมื่อ
2019-06-22. ดังนั้นนี่เป็น long historical record ไม่ใช่ผลของ current index
implementation แบบต่อเนื่องตลอดช่วง.

## Performance check

- entity_key: NYSE Arca:CQQQ
- Inception: 2009-12-08
- Metric: NAV Total Return including reinvested distributions and fund expenses
- Tracked index (issuer benchmark): FTSE China Incl A 25% Technology Capped Index
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark)
- 10-year window: complete calendar years 2016-2025
- 10-year NAV TR CAGR: 4.44%; start TR value 100.00 and end TR value 154.48 เป็น normalized levels calculated from the official annual rows; actual years 10.00 complete calendar years
- Formula: (154.48 / 100.00)^(1 / 10.00) - 1 = 4.44%
- Common-window calculation: official rows 2021-2025 compound to -35.06% and CAGR -8.27%; S&P 500 TR compounds to 96.17% and CAGR 14.43%
- Coverage/source note: annual rows are calendar-year NAV returns; current NAV/YTD
  was not disclosed in the verified current Invesco capture. The 2016-2025 history
  includes predecessor and index-methodology changes disclosed below.

| Year | CQQQ NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | -0.07% | 11.96% |
| 2017 | 72.54% | 21.83% |
| 2018 | -34.21% | -4.38% |
| 2019 | 32.46% | 31.49% |
| 2020 | 58.33% | 18.40% |
| 2021 | -25.13% | 28.71% |
| 2022 | -29.74% | -18.11% |
| 2023 | -16.97% | 26.29% |
| 2024 | 11.24% | 25.02% |
| 2025 | 33.65% | 17.88% |

S&P 500 เป็น common reference benchmark ไม่ใช่ issuer benchmark ของ CQQQ;
ตาราง S&P ใช้ cached USD Total Return convention ณ 2025-12-31.

## Up years / Down years

- Up years / Down years: 5 / 5
- Best: 2017, +72.54%
- Least positive: 2024, +11.24%
- Worst: 2018, -34.21%
- Least bad down year: 2016, -0.07%
- Current YTD: `ไม่พบข้อมูลที่ยืนยันได้` in the reviewed official capture

## Risk read-through

CQQQ มี China country, technology concentration, emerging-market, policy,
VIE, ADR/GDR และ currency risk. The latest readable official Invesco report
shows 157 holdings, P/B `5.46`, P/E `21.99` and return on equity `12.77%` as of
2025-12-31; the current product page did not expose a newer numeric holdings or
valuation snapshot in the reviewed capture. SEC prospectus ระบุว่ากองเป็น
non-diversified, ลงทุนอย่างน้อย 90% ใน index constituents/ADRs/GDRs และใช้
full replication; management fee/total annual operating expenses ที่ระบุใน
prospectus คือ `0.65%`. Daily NAV history สำหรับ max drawdown และ recovery:
`ไม่พบข้อมูลที่ยืนยันได้` ใน lean capture.

## Methodology and continuity gap

- SEC prospectus ระบุว่า CQQQ เป็น successor to the Guggenheim China Technology
  ETF หลัง reorganization ที่เสร็จสิ้น 2018-05-18; returns ก่อนวันนั้นเป็นของ
  predecessor fund.
- SEC prospectus ระบุว่า current FTSE China Incl A 25% Technology Capped Index
  เริ่มใช้ 2019-06-22; blended index ก่อนหน้านั้นสะท้อน AlphaShares China
  Technology Index. ดังนั้นไม่ควรตีความ CAGR นี้เป็นผลของ current index
  methodology แบบต่อเนื่องครบทั้งช่วง.

## Sources

- Official issuer product page:
  https://www.invesco.com/us/en/financial-products/etfs/invesco-china-technology-etf.html
- Official SEC summary prospectus (identity, index, fee, predecessor and methodology history):
  https://www.sec.gov/Archives/edgar/data/1378872/000119312525040714/d834062d497k.htm
- Official issuer factsheet URL:
  https://www.invesco.com/content/dam/invesco/us/en/product-documents/etf/fact-sheet/cqqq-invesco-china-technology-etf-fact-sheet.pdf
- Official Invesco Q4 2025 performance report:
  https://www.invesco.com/us-rest/contentdetail?contentId=84c2f428e1682610VgnVCM1000006e36b50aRCRD&dnsName=us
- Official S&P 500 index page:
  https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- ETF source batch: [[ETF_performance_sources_2026-08-29]] | [[ETF Performance Index]]
