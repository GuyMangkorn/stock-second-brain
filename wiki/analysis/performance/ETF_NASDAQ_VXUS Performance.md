---
type: etf-performance
instrument_type: ETF
entity_key: Nasdaq:VXUS
ticker: VXUS
exchange: Nasdaq
fund: Vanguard Total International Stock ETF
tracked_index: FTSE Global All Cap ex US Index
benchmark: S&P 500 Total Return
updated: 2026-07-18
performance_as_of: 2026-06-30
rolling_10y_as_of: 2026-06-30
current_ytd_as_of: 2026-07-13
price_nav_as_of: 2026-07-09
distribution_as_of: 2026-06-23
fund_facts_as_of: 2026-03-31
source_batch: raw/imports/ETF_performance_sources_2026-07-18.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/VXUS
  - geography/international-ex-US
---

# VXUS Performance

## Bottom line

VXUS ให้ cumulative `NAV Total Return` ประมาณ `127.03%` ใน complete calendar
years 2016-2025 หรือ CAGR `8.54%` จาก annual rows ทางการ; เป็นบวก 8 ปีและลบ
2 ปี. ปีดีที่สุดคือ 2025 ที่ `+32.23%` และแย่ที่สุดคือ 2022 ที่ `-15.99%`.
Current YTD ล่าสุดคือ `+11.55%` ณ 13 ก.ค. 2026.

## Performance check

- `entity_key: Nasdaq:VXUS`
- Inception: 26 ม.ค. 2011; expense ratio: `0.05%`
- Metric: `NAV Total Return` แบบ pre-tax รวม dividends และ capital gains
  reinvested หลัง fund expenses
- Tracked index (issuer benchmark): `FTSE Global All Cap ex US Index`
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference
  benchmark ไม่ใช่ issuer benchmark)
- Official rolling 10-year window: `2016-06-30` to `2026-06-30`
- 10-year NAV TR CAGR: `9.95%`; normalized Start TR value: `100.00`; End TR
  value: `258.55`; Years: `10.00`; official cumulative return `158.55%`
- Formula: `(End TR / Start TR)^(1 / Years) - 1`
- Annual coverage: official complete calendar years 2016-2025; ไม่มี `*` หรือ
  `†`. Calendar-window cumulative/CAGR เป็นค่าคำนวณจาก annual rows ที่ปัดเศษ;
  market-price return ถูกแยกออกจากตารางและ ranking.

| ปี | VXUS NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 4.72% | 11.96% |
| 2017 | 27.52% | 21.83% |
| 2018 | -14.42% | -4.38% |
| 2019 | 21.58% | 31.49% |
| 2020 | 11.32% | 18.40% |
| 2021 | 8.69% | 28.71% |
| 2022 | -15.99% | -18.11% |
| 2023 | 15.56% | 26.29% |
| 2024 | 5.20% | 25.02% |
| 2025 | 32.23% | 17.88% |

## Up years / Down years

- Up years / Down years: `8 / 2` ใน 2016-2025
- Best: 2025, `+32.23%`
- Least positive: 2016, `+4.72%`
- Worst: 2022, `-15.99%`
- Least bad down year: 2018, `-14.42%`
- 2021-2025 cumulative: VXUS `46.78%`, CAGR `7.98%`; S&P 500 TR `96.17%`,
  CAGR `14.43%`
- Current YTD: VXUS official NAV TR `+11.55%` ณ 13 ก.ค. 2026. Latest official
  market price/NAV pair ที่ยืนยันได้คือ USD `84.90` / `84.74` ณ 9 ก.ค. 2026.

## Risk read-through

**แนวโน้มตอนนี้:** medium-term ยังเป็นบวกจาก 2025 `+32.23%` ต่อด้วย 2026 YTD
`+11.55%`, แต่ short-term อยู่ในช่วงพักฐาน: secondary market-price data ณ
17 ก.ค. 2026 อยู่ที่ USD `83.37`, ลด `-3.15%` ในหนึ่งเดือนและต่ำกว่า 52-week
high `5.85%`. จึงอ่านเป็น `positive medium-term / correcting short-term`
มากกว่าขาขึ้นเร่งตัว.

Long-term ยังตาม S&P 500 ชัดเจน: 2016-2025 CAGR `8.54%` เทียบ `14.82%`.
3-year standard deviation คือ `12.60%` ณ 31 มี.ค. 2026; ความเสี่ยงหลักมาจาก
FX, non-U.S. growth, China/Europe/Japan และ sector mix ที่ financials มีน้ำหนัก
สูง. Expense ratio ต่ำ `0.05%`, แต่ issuer source ไม่เปิด official maximum
drawdown/recovery series จึงระบุ `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- [Vanguard VXUS product page](https://investor.vanguard.com/investment-products/etfs/profile/vxus) — official annual/rolling NAV returns, fund identity, price/NAV and distributions
- [Vanguard Advisors VXUS](https://advisors.vanguard.com/investments/products/vxus/vanguard-total-international-stock-etf) — current official NAV YTD as of 13 ก.ค. 2026
- [Vanguard VXUS fact sheet](https://institutional.vanguard.com/assets/corp/fund_communications/pdf_publish/us-products/fact-sheet/F3369.pdf) — Nasdaq listing, benchmark, fee, return definition, risk and holdings as of 31 มี.ค. 2026
- [Barchart VXUS performance](https://www.barchart.com/etfs-funds/quotes/VXUS/performance) — secondary short-term market-price trend as of 17 ก.ค. 2026
- [[ETF_performance_sources_2026-07-18]] | [[ETF Performance Index]]
