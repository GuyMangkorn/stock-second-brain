---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:VOO
ticker: VOO
exchange: NYSE Arca
fund: Vanguard S&P 500 ETF
tracked_index: S&P 500 Index
benchmark: S&P 500 Total Return
updated: 2026-07-13
performance_as_of: 2026-06-30
rolling_10y_as_of: 2026-06-30
current_ytd_as_of: 2026-07-09
price_nav_as_of: 2026-07-09
distribution_as_of: 2026-06-30
fund_facts_as_of: 2026-03-31
source_batch: raw/imports/ETF_performance_sources_2026-07-13.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/VOO
  - geography/United-States
---

# VOO Performance

## Bottom line

VOO ให้ cumulative `NAV Total Return` ประมาณ `296.90%` ใน complete calendar
years 2016-2025 หรือ CAGR `14.78%` จาก annual rows ทางการที่ปัดเศษแล้ว; เป็นบวก
8 ปีและลบ 2 ปี. ปีดีที่สุดคือ 2019 ที่ `+31.46%` และแย่ที่สุดคือ 2022 ที่
`-18.15%`. Current YTD คือ `+9.97%` ณ 9 ก.ค. 2026 เทียบ S&P 500 TR `+9.98%`
ในวันเดียวกัน.

## Performance check

- `entity_key: NYSE Arca:VOO`
- Inception: 7 ก.ย. 2010
- Metric: `NAV Total Return` แบบ pre-tax รวมเงินปันผลและ capital gains reinvested
  หลัง fund expenses
- Tracked index (issuer benchmark): `S&P 500 Index`
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference
  benchmark และเป็น total-return form ของ tracked index)
- Official rolling 10-year window: `2016-06-30` to `2026-06-30`
- 10-year NAV TR CAGR: `15.47%`; normalized Start TR value: `100.00`; End TR
  value: `421.27`; Years: `10.00`; official cumulative return `321.27%`
- Formula: `(End TR / Start TR)^(1 / Years) - 1`
- Annual coverage: official complete calendar years 2016-2025; ไม่มี `*` หรือ `†`.
  Calendar-window cumulative/CAGR เป็นค่าประมาณจาก annual rows ที่ปัดเศษสองตำแหน่ง;
  exclude `market-price return` จากตารางและ ranking.

- Annual NAV TR coverage: official 2016-2025 NAV TR
| ปี | VOO NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 11.93% | 11.96% |
| 2017 | 21.78% | 21.83% |
| 2018 | -4.42% | -4.38% |
| 2019 | 31.46% | 31.49% |
| 2020 | 18.35% | 18.40% |
| 2021 | 28.66% | 28.71% |
| 2022 | -18.15% | -18.11% |
| 2023 | 26.25% | 26.29% |
| 2024 | 24.98% | 25.02% |
| 2025 | 17.84% | 17.88% |

## Up years / Down years

- Up years / Down years: `8 / 2` ใน 2016-2025
- Best: 2019, `+31.46%`
- Least positive: 2016, `+11.93%`
- Worst: 2022, `-18.15%`
- Least bad down year: 2018, `-4.42%`
- 2021-2025 cumulative: VOO `95.81%`, CAGR `14.38%`; S&P 500 TR `96.17%`,
  CAGR `14.43%`
- Current YTD: VOO `+9.97%` NAV และ S&P 500 TR `+9.98%` ณ 9 ก.ค. 2026

## Risk read-through

**10-year NAV CAGR:** `15.47%` ณ 30 มิ.ย. 2026 ใกล้ issuer benchmark ที่
`15.51%`; ส่วนต่างสะท้อน fund expenses และ tracking difference ขนาดเล็ก.
VOO เป็น passive U.S. large-cap broad equity แบบ full replication จึงเหมาะเป็น
market-beta building block แต่ยังรับ equity drawdown เต็มรูปแบบ. 3-year standard
deviation คือ `12.06%` ณ 31 มี.ค. 2026 และ expense ratio `0.03%`. Issuer source
ที่จับไว้ไม่เปิดเผย maximum drawdown/recovery series จึงบันทึกเป็น
`ไม่พบข้อมูลที่ยืนยันได้`.

**Classification:** Structural = U.S. large-cap broad equity. Behavioral =
S&P 500 market beta, mega-cap sensitive, low tracking difference; ไม่ใช่
downside hedge.

## Sources

- [Vanguard VOO product page](https://investor.vanguard.com/investment-products/etfs/profile/voo) — current NAV/YTD, official annual and rolling returns, expense ratio, distributions, and fund identity
- [Vanguard VOO fact sheet](https://institutional.vanguard.com/assets/corp/fund_communications/pdf_publish/us-products/fact-sheet/F0968.pdf) — NYSE Arca, passive full-replication approach, return definition, risk, and fund facts as of 31 มี.ค. 2026
- [S&P DJI index returns](https://www.spglobal.com/spdji/en/additional-reports/all-returns/index.dot?additionalFilterCondition=&parentIdentifier=df8ec300-24ad-4c70-81d3-a3cece0200e2&sourceIdentifier=index-family-specialization) — S&P 500 TR current YTD as of 9 ก.ค. 2026
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — index definition and total-return series identity
- [[ETF_performance_sources_2026-07-13]] | [[ETF Performance Index]]
