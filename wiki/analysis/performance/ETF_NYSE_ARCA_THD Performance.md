---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:THD
ticker: THD
exchange: NYSE Arca
fund: iShares MSCI Thailand ETF
tracked_index: MSCI Thailand IMI 25/50 Index (Net)
benchmark: S&P 500 Total Return
updated: 2026-07-24
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-07-22
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/THD
  - geography/Thailand
---

# THD Performance

> Navigation: [[ETF Region Index]] → [[Thailand ETF]] → [[ETF Performance Index]]

## Bottom line

THD เป็น passive/index-tracking Thailand equity ETF ของ iShares ติดตาม `MSCI Thailand IMI 25/50 Index (Net)` และเริ่มกองทุนเมื่อ 2008-03-26. Official rolling 10-year NAV Total Return ครอบคลุม 2016-06-30 ถึง 2026-06-30 ครบ `10.00` ปี และรายงาน CAGR `3.35%` ต่อปี; เมื่อ normalize จาก 100.00 จะเท่ากับประมาณ 139.03 ที่ปลายช่วง. Raw NAV TR endpoints ไม่ได้เปิดเผย. Current official NAV TR YTD คือ `25.53%` ณ 2026-07-22.

## Performance check

- `entity_key`: `NYSE Arca:THD`
- Fund: iShares MSCI Thailand ETF; asset class `Equity`; expense ratio `0.59%`
- Inception: `2008-03-26`
- Metric: official NAV Total Return, รวม reinvested distributions และหัก fund expenses แล้ว
- Issuer benchmark: MSCI Thailand IMI 25/50 Index (Net); index methodology note ระบุว่า THD เริ่มติดตามดัชนีนี้เมื่อ `2013-02-12` และช่วงก่อนหน้านั้นใช้ MSCI Thailand Investable Market Index (Net)
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark, not issuer benchmark)

### Official 10-year NAV TR window

| Start date | End date | Actual years | Start TR value | End TR value | CAGR | Disclosure |
|---|---|---:|---:|---:|---:|---|
| 2016-06-30 | 2026-06-30 | 10.00 | 100.00 (normalized) | approx. 139.03 (calculated from official CAGR) | 3.35% | Raw start/end NAV TR values not disclosed by issuer |

สูตร normalized endpoint: `100.00 × (1 + 3.35%)^10.00 = 139.03`; ค่านี้เป็นการคำนวณจาก issuer-reported CAGR ไม่ใช่การสร้าง proxy และไม่ควรตีความเป็น raw NAV.

### Annual NAV Total Return

| Year | THD NAV TR | MSCI Thailand IMI 25/50 Index (Net) TR | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | not disclosed | not disclosed | 11.96% |
| 2017 | not disclosed | not disclosed | 21.83% |
| 2018 | not disclosed | not disclosed | -4.38% |
| 2019 | not disclosed | not disclosed | 31.49% |
| 2020 | not disclosed | not disclosed | 18.40% |
| 2021 | 1.66% | 1.89% | 28.71% |
| 2022 | 1.55% | 1.80% | -18.11% |
| 2023 | -12.18% | -12.20% | 26.29% |
| 2024 | -1.85% | -1.69% | 25.02% |
| 2025 | 0.87% | 1.00% | 17.88% |
| 2026 YTD | 25.53% | not disclosed | not comparable; current year not cached |

Rows `2016-2020` ของ THD และ issuer benchmark เป็น `not disclosed` ใน official factsheet ที่ตรวจทาน; ไม่เติมค่าจาก proxy. S&P 500 rows `2016-2025` reuse the cached USD Total Return convention as of `2025-12-31`; 2026 YTD ไม่ใช้แทน complete calendar year.

### Window calculations and ranking

- Common complete-calendar window `2021-2025`: THD NAV TR cumulative `-10.24%`, CAGR `-2.14%`; S&P 500 TR cumulative `96.17%`, CAGR `14.43%`; THD trails by approximately `16.56 pp` CAGR.
- Up years / down years in `2021-2025`: `2 / 3`.
- Best complete year: `2022`, `1.55%`; least positive: `2025`, `0.87%`.
- Worst complete year: `2023`, `-12.18%`; least bad down year: `2024`, `-1.85%`.
- Current NAV TR YTD: `25.53%` as of `2026-07-22`; this is a partial-year observation, not a calendar-year ranking.

## Risk read-through

THD เป็น single-country Thailand equity exposure. Official page reports `82` holdings and 3-year standard deviation `21.96%`; current P/E `17.92` and P/B `1.82` are as of `2026-07-22`. Index-change history on `2013-02-12` ทำให้การเทียบระยะยาวต้องแยก issuer benchmark ตาม methodology ที่รายงาน. Representative sampling และการอนุญาตให้ใช้ตราสารอนุพันธ์บางส่วนตาม prospectus อาจทำให้ NAV ต่างจากดัชนี; fund-level max drawdown และ recovery จาก daily NAV history ใน lean capture คือ `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- Official issuer product/performance page: https://www.ishares.com/us/products/239688/ishares-msci-thailand-capped-etf
- Official iShares factsheet (performance through 2026-06-30): https://www.ishares.com/us/literature/fact-sheet/thd-ishares-msci-thailand-etf-fund-fact-sheet-en-us.pdf
- Official summary prospectus: https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-thailand-capped-etf-8-31.pdf
- Official S&P 500 index page and cached USD Total Return convention: https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- ETF source batch: [[ETF_performance_sources_2026-07-24]]
- Navigation: [[Thailand ETF]] | [[ETF Region Index]] | [[ETF Performance Index]]
