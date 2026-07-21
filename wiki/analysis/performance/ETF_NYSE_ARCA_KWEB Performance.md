---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:KWEB
ticker: KWEB
exchange: NYSE Arca
fund: KraneShares CSI China Internet ETF
tracked_index: CSI Overseas China Internet Index
benchmark: S&P 500 Total Return
updated: 2026-07-18
annual_performance_as_of: 2025-12-31
performance_as_of: 2026-07-17
rolling_10y_as_of: 2026-06-30
current_ytd_as_of: 2026-06-30
nav_as_of: 2026-07-17
market_price_as_of: 2026-07-17
distribution_as_of: 2025-12-23
fund_facts_as_of: 2026-07-17
risk_as_of: 2026-07-17
source_batch: raw/imports/ETF_performance_sources_2026-07-18.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/KWEB
  - geography/China
  - theme/china-internet
---

# KWEB Performance

> Navigation: [[ETF Region Index]] → [[China ETF]] → [[ETF Performance Index]]

## Bottom line

KWEB ปิดที่ `$26.81` ณ 17 ก.ค. 2026 ลด `2.44%` ใน session ล่าสุด; market-price
total-return proxy ลด `21.26%` YTD ถึงวันเดียวกัน ขณะที่ official NAV TR ล่าสุดจาก
issuer ณ 30 มิ.ย. อยู่ที่ `-28.96%`. ใน complete calendar years 2016-2025,
secondary total-return proxy ให้ cumulative `12.19%` หรือ CAGR `1.16%`, บวก 5 ปี
ลบ 5 ปี; official rolling 10-year NAV TR CAGR อยู่ที่ `-0.85%`.

## Performance check

- `entity_key: NYSE Arca:KWEB` (ผู้ใช้ระบุ `AMEX-KWEB`; issuer/fund-data ระบุ
  NYSE/NYSE Arca จึงใช้ `NYSE Arca` เป็น exchange-qualified key)
- Inception: 31 ก.ค. 2013; expense ratio: `0.70%`
- Metric: official `NAV Total Return` รวม dividends/capital-gains distributions
  reinvested และ fund expenses
- Issuer benchmark: `CSI Overseas China Internet Index`
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference
  benchmark ไม่ใช่ tracked index ของ KWEB)
- Official rolling 10-year window: `2016-06-30` to `2026-06-30`
- 10-year NAV TR CAGR: `-0.85%` ตาม issuer; raw start/end NAV TR values ไม่เปิดเผย
- Coverage/source note: annual rows เป็น `secondary dividend-reinvested market-price
  total-return proxy*` เพื่อให้มี complete calendar-year history; ไม่ใช่ official
  NAV TR และไม่ใช้เป็น strict cross-ETF ranking. S&P 500 rows ใช้ cached USD TR
  convention ณ 31 ธ.ค. 2025.

| ปี | KWEB TR* | S&P 500 TR |
|---|---:|---:|
| 2016 | -8.54% | 11.96% |
| 2017 | 69.73% | 21.83% |
| 2018 | -33.80% | -4.38% |
| 2019 | 29.92% | 31.49% |
| 2020 | 58.23% | 18.40% |
| 2021 | -49.01% | 28.71% |
| 2022 | -17.24% | -18.11% |
| 2023 | -9.06% | 26.29% |
| 2024 | 12.01% | 25.02% |
| 2025 | 23.55% | 17.88% |

## Up years / Down years

- Up years / Down years: `5 / 5` ใน 2016-2025
- Best: 2017, `+69.73%`; least positive: 2024, `+12.01%`
- Worst: 2021, `-49.01%`; least bad down year: 2023, `-9.06%`
- 2016-2025 cumulative / CAGR: KWEB proxy* `12.19%` / `1.16%`; S&P 500 TR
  `298.33%` / `14.82%`
- 2021-2025 cumulative / CAGR: KWEB proxy* `-46.89%` / `-11.89%`; S&P 500 TR
  `96.17%` / `14.43%`
- Current YTD: official NAV TR `-28.96%` ณ 30 มิ.ย. 2026; latest market-price
  total-return proxy `-21.26%` ณ 17 ก.ค. 2026

## Risk read-through

Official rolling 10-year NAV CAGR `-0.85%` สะท้อนว่า long-term outcome ยังไม่ชดเชย
ความผันผวนของ China Internet exposure. Secondary total-return proxy ระบุ current
drawdown `-68.99%` จาก high วันที่ 17 ก.พ. 2021 และ worst drawdown `-80.92%` ถึง
24 ต.ค. 2022; official NAV drawdown/recovery series `ไม่พบข้อมูลที่ยืนยันได้`.
KWEB กระจุกใน Communication Services และ Consumer Discretionary รวม `79.83%`
ณ 30 มิ.ย. 2026 และ top five holdings รวม `40.65%` ณ 17 ก.ค. จึงไวต่อ valuation,
China consumer demand, policy และ FX/geopolitical risk. ล่าสุด market price `$26.81`
เทียบ NAV `$26.72` เป็น premium เพียง `0.34%`, จึงไม่มีหลักฐานว่า discount ของ ETF
เป็นสาเหตุหลักของการลง. Latest move สอดคล้องกับ global tech risk-off และ Hang Seng
Tech ที่ลดประมาณ `4%` มากกว่า fund-specific dislocation.

## Sources

- [KraneShares KWEB product page](https://kraneshares.com/etf/kweb/) — official fund facts, NAV/market price, rolling performance, holdings and premium/discount; as of 2026-07-17 where stated
- [KraneShares KWEB factsheet](https://kraneshares.com/resources/factsheet/kweb_factsheet.pdf) — official return basis, benchmark, expense ratio and 10-year NAV CAGR; as of 2026-06-30
- [Total Real Returns KWEB](https://totalrealreturns.com/n/KWEB) — secondary dividend-reinvested total-return history and drawdown proxy; ending 2026-07-17
- [Stock Analysis KWEB history](https://stockanalysis.com/etf/kweb/history/) — secondary market-price history; close 2026-07-17
- [[ETF_performance_sources_2026-07-18]] | [[ETF Performance Index]]
