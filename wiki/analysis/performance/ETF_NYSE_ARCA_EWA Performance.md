---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:EWA
ticker: EWA
exchange: NYSE Arca
fund: iShares MSCI Australia ETF
tracked_index: MSCI Australia Index (Net)
benchmark: S&P 500 Total Return
updated: 2026-07-19
performance_as_of: 2026-07-16
rolling_10y_as_of: 2026-06-30
current_ytd_as_of: 2026-07-16
price_nav_as_of: 2026-07-17
source_batch: raw/imports/ETF_performance_sources_2026-07-19.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/EWA
  - geography/Australia
---

# EWA Performance

> Navigation: [[ETF Region Index]] → [[Australia ETF]] → [[ETF Performance Index]]

## Bottom line

EWA ให้ cumulative `NAV Total Return` ประมาณ `108.31%` ใน complete calendar years
2016-2025 หรือ CAGR `7.61%` จาก annual rows; เป็นบวก 8 ปีและลบ 2 ปี. ปีดีที่สุดคือ
2017 ที่ `+19.60%` และแย่ที่สุดคือ 2018 ที่ `-12.30%`. Current NAV YTD ล่าสุดคือ
`+10.44%` ณ 16 ก.ค. 2026; S&P 500 TR current YTD อยู่ที่ `+9.64%` ณ 17 ก.ค.
2026 แต่เป็นคนละวันจึงใช้เป็น directional reference เท่านั้น.

## Performance check

- `entity_key: NYSE Arca:EWA`
- Inception: 12 มี.ค. 1996
- Metric: `NAV Total Return` รวมเงินปันผล reinvested และ fund expenses
- Tracked index (issuer benchmark): `MSCI Australia Index (Net)`
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference
  benchmark ไม่ใช่ tracked index ของ EWA)
- Official rolling 10-year window: `2016-06-30` to `2026-06-30`
- 10-year NAV TR CAGR: `8.27%`; Start TR value: `100.00`; End TR value: `221.36`;
  Years: `10.00`
- Formula: `(End TR / Start TR)^(1 / Years) - 1`; official cumulative return ใน
  rolling window คือ `121.36%`
- Annual coverage: official complete calendar years 2016-2025. แถว 2016-2020
  เป็น official iShares endpoint ที่แสดงหนึ่งตำแหน่งทศนิยม; 2021-2025 ใช้ตัวเลข
  NAV แบบ exact จาก US product page/factsheet. Cumulative/CAGR 2016-2025 จึงเป็น
  calculation จาก annual rows ที่มีการปัดเศษบางแถว.
- S&P 500 cache 2016-2025: cumulative `298.33%`; CAGR `14.82%` จาก rounded
  annual inputs

| ปี | EWA NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 11.10% | 11.96% |
| 2017 | 19.60% | 21.83% |
| 2018 | -12.30% | -4.38% |
| 2019 | 22.40% | 31.49% |
| 2020 | 8.30% | 18.40% |
| 2021 | 9.09% | 28.71% |
| 2022 | -5.74% | -18.11% |
| 2023 | 13.98% | 26.29% |
| 2024 | 0.82% | 25.02% |
| 2025 | 14.12% | 17.88% |

## Up years / Down years

- Up years / Down years: `8 / 2` ใน 2016-2025
- Best: 2017, `+19.60%`
- Least positive: 2024, `+0.82%`
- Worst: 2018, `-12.30%`
- Least bad down year: 2022, `-5.74%`
- 2016-2025 cumulative/CAGR: EWA `108.31%` / `7.61%`; S&P 500 TR `298.33%` /
  `14.82%`
- 2021-2025 cumulative/CAGR: EWA `34.85%` / `6.16%`; S&P 500 TR `96.17%` /
  `14.43%`
- Current YTD: EWA NAV `+10.44%` ณ 16 ก.ค. 2026; S&P 500 TR `+9.64%` ณ 17 ก.ค.
  2026 จาก secondary current snapshot จึงไม่ใช่ same-date comparison

## Risk read-through

**10-year NAV CAGR:** `8.27%` ณ 30 มิ.ย. 2026. EWA เป็น single-country Australia
equity ETF ที่มี 3-year standard deviation `16.51%` และ equity beta `0.86` ณ
30 มิ.ย. 2026; sector exposure ล่าสุดกระจุกใน Financials `41.72%` และ Materials
`23.22%` ณ 17 ก.ค. 2026. Expense ratio คือ `0.50%`, holdings `47` และ distribution
frequency เป็น semi-annual; trailing yield `3.01%` ณ 30 มิ.ย. 2026.

Secondary dividend-reinvested proxy รายงาน maximum drawdown `-66.98%` จาก peak
31 ต.ค. 2007 ถึง trough 20 พ.ย. 2008; series กลับไปทำ high ใหม่ 15 เม.ย. 2026
หรือประมาณ `18.46` ปีจาก prior peak. ตัวเลข drawdown/recovery นี้ไม่ใช่ official
NAV TR series; raw daily NAV TR index levels ไม่เปิดเผยใน issuer capture.

**Classification:** Structural = Australia single-country broad equity. Behavioral =
financials/materials/commodity-sensitive, country/FX-sensitive และยังมี equity risk
เต็มรูปแบบ; ไม่ควรตีความเป็น crisis hedge.

## Sources

- [iShares EWA product page](https://www.ishares.com/us/products/239607/ishares-msci-australia-etf) — identity, NYSE Arca, inception, tracked index, current NAV/price, YTD, fees, holdings and risk snapshot
- [iShares EWA fact sheet](https://www.ishares.com/us/literature/fact-sheet/ewa-ishares-msci-australia-etf-fund-fact-sheet-en-us.pdf) — official NAV return definition and exact 2021-2025 calendar rows
- [iShares EWA international performance table](https://www.ishares.com/ch/professionals/en/products/239607/ishares-msci-australia-etf?siteEntryPassthrough=true&switchLocale=n) — official 2016-2025 calendar rows and rolling performance
- [Total Real Returns EWA](https://totalrealreturns.com/n/EWA) — secondary dividend-reinvested proxy for annual history and drawdown/recovery
- [Slickcharts S&P 500 YTD](https://www.slickcharts.com/sp500/returns/ytd) — secondary current S&P 500 TR YTD as of 17 ก.ค. 2026
- [Official S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common benchmark identity and methodology
- [[ETF_performance_sources_2026-07-19]] | [[ETF Performance Index]]
