---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:EWH
ticker: EWH
exchange: NYSE Arca
fund: iShares MSCI Hong Kong ETF
tracked_index: MSCI Hong Kong 25-50 Index (USD) (Net)
benchmark: S&P 500 Total Return
updated: 2026-07-21
performance_as_of: 2026-07-17
rolling_10y_as_of: 2026-06-30
current_ytd_as_of: 2026-07-17
price_nav_as_of: 2026-07-20
source_batch: raw/imports/ETF_performance_sources_2026-07-21.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/EWH
  - geography/Hong-Kong
---

# EWH Performance

> Navigation: [[ETF Region Index]] → [[Hong Kong ETF]] → [[ETF Performance Index]]

## Bottom line

EWH ให้ official `NAV Total Return` ใน complete calendar years 2016-2025 cumulative `+51.86%` และ CAGR ประมาณ `4.27%` จาก annual rows ที่ 2016-2020 แสดงเพียงหนึ่งตำแหน่งทศนิยม; เป็นบวก 6 ปีและลบ 4 ปี. ปีดีที่สุดคือ 2017 ที่ `+35.60%` และแย่ที่สุดคือ 2023 ที่ `-14.04%`. Current NAV YTD คือ [`+5.44%` ณ 17 ก.ค. 2026](https://www.ishares.com/us/products/239657/ishares-msci-hong-kong-etf); S&P 500 TR อยู่ที่ [`+9.43%` ณ 20 ก.ค. 2026](https://www.slickcharts.com/sp500/returns/ytd) แต่เป็นคนละวัน.

## Performance check

- `entity_key: NYSE Arca:EWH`
- Inception: 12 มี.ค. 1996
- Metric: `NAV Total Return` รวมเงินปันผล reinvested และ fund expenses
- Tracked index (issuer benchmark): `MSCI Hong Kong 25-50 Index (USD) (Net)`
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference benchmark ไม่ใช่ tracked index ของ EWH)
- 10-year window: `2026-06-30` เทียบกับ `2016-06-30` ตาม issuer rolling-performance snapshot
- 10-year NAV TR CAGR: `4.20%`; Start TR value: `100.00`; End TR value: `150.95`; Years: `10.00` — normalized from issuer cumulative return `50.95%`; raw TR index endpoints ไม่ได้เปิดเผย
- Formula: `(End TR / Start TR)^(1 / Years) - 1`; `(150.95 / 100.00)^(1 / 10.00) - 1 = 4.20%`
- Annual coverage: official complete calendar years 2016-2025. แถว 2016-2020 เป็น official iShares display ที่ปัดเป็นหนึ่งตำแหน่งทศนิยม; 2021-2025 เป็น official NAV rows ที่แสดงสองตำแหน่ง. จึงคำนวณ 2016-2025 CAGR จาก published rounded inputs และไม่ใช้ proxy
- S&P 500 cache 2016-2025: cumulative `298.33%`; CAGR `14.82%` จาก rounded annual inputs; USD Total Return, dividends reinvested, cache as-of `2025-12-31`

| ปี | EWH NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 1.80% | 11.96% |
| 2017 | 35.60% | 21.83% |
| 2018 | -8.30% | -4.38% |
| 2019 | 9.70% | 31.49% |
| 2020 | 4.60% | 18.40% |
| 2021 | -3.43% | 28.71% |
| 2022 | -6.72% | -18.11% |
| 2023 | -14.04% | 26.29% |
| 2024 | 0.10% | 25.02% |
| 2025 | 34.89% | 17.88% |

## Up years / Down years

- Up years / Down years: `6 / 4` ใน 2016-2025
- Best: 2017, `+35.60%`
- Least positive: 2024, `+0.10%`
- Worst: 2023, `-14.04%`
- Least bad down year: 2021, `-3.43%`
- 2016-2025 cumulative/CAGR: EWH `+51.86%` / `4.27%` (approximate from rounded official annual rows); S&P 500 TR `+298.33%` / `14.82%`
- 2021-2025 cumulative/CAGR: EWH `+4.55%` / `0.89%`; S&P 500 TR `+96.17%` / `14.43%`
- Current YTD: EWH NAV `+5.44%` ณ 17 ก.ค. 2026; S&P 500 TR `+9.43%` ณ 20 ก.ค. 2026 จาก secondary snapshot จึงไม่ใช่ same-date comparison

## Risk read-through

**10-year NAV CAGR:** `4.20%` ณ 30 มิ.ย. 2026. EWH เป็น single-country Hong Kong equity ETF ที่มี 3-year standard deviation `19.08%` และ equity beta `0.45` ณ 30 มิ.ย. 2026; ล่าสุดมี `26` holdings ณ 17 ก.ค. 2026, expense ratio `0.50%`, distribution frequency semi-annual และ 12m trailing yield `4.95%` ณ 30 มิ.ย. 2026. Exposure กระจุกใน Insurance `20.99%`, Financial Services `16.75%`, Capital Goods `15.40%`, Real Estate Management & Development `14.01%` และ Utilities `11.88%` ณ 17 ก.ค. 2026.

Secondary dividend-reinvested proxy รายงาน maximum drawdown `-65.56%` จาก peak `1997-08` ถึง trough `1998-08` และ recovery/new high ใน `2006-03` หรือ `104` เดือน ณ 30 มิ.ย. 2026. Proxy นี้เป็น monthly USD series ที่สมมติ reinvested dividends และไม่หัก fees/taxes; ไม่ใช่ official NAV TR. Official daily NAV TR index levels จึงยังเป็น `ไม่พบข้อมูลที่ยืนยันได้` สำหรับการคำนวณ drawdown/recovery โดยตรง.

**Classification:** Structural = Hong Kong single-country equity. Behavioral = financials/real-estate/utilities concentration, country/FX/liquidity-sensitive และยังมี equity risk เต็มรูปแบบ.

## Sources

- [iShares EWH product page](https://www.ishares.com/us/products/239657/ishares-msci-hong-kong-etf) — identity, NYSE Arca, inception, tracked index, current NAV/price, YTD, fees, holdings, exposure, risk and distributions
- [iShares EWH fact sheet](https://www.ishares.com/us/literature/fact-sheet/ewh-ishares-msci-hong-kong-etf-fund-fact-sheet-en-us.pdf) — official NAV TR definition and 2021-2025 calendar rows
- [iShares EWH international performance table](https://www.ishares.com/uk/professional/en/products/239657/ishares-msci-hong-kong-etf?siteEntryPassthrough=true&switchLocale=y) — official complete calendar rows 2016-2025 and performance context
- [iShares EWH summary prospectus](https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-hong-kong-etf-8-31.pdf) — passive/index-tracking objective and risk disclosures
- [Lazy Portfolio ETF EWH](https://www.lazyportfolioetf.com/etf/ishares-msci-hong-kong-etf-ewh/) — secondary dividend-reinvested proxy for drawdown/recovery
- [Slickcharts S&P 500 YTD](https://www.slickcharts.com/sp500/returns/ytd) — secondary current S&P 500 TR YTD as of 20 ก.ค. 2026
- [Official S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common benchmark identity and methodology
- [[ETF_performance_sources_2026-07-21]] | [[ETF Performance Index]]
