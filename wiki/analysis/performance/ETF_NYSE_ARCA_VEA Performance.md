---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:VEA
ticker: VEA
exchange: NYSE Arca
updated: 2026-08-29
source_batch: raw/imports/ETF_performance_sources_2026-08-29.md
return_basis: NAV total return
management_mode: passive-index
tags:
  - analysis/etf-performance
  - geography/International
  - ticker/VEA
---

# VEA Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

VEA ให้ผลตอบแทนเป็นบวก `8 / 10` complete calendar years ในช่วง 2016-2025 โดยปีดีที่สุดคือ 2025 ที่ `+35.15%` และแย่ที่สุดคือ 2022 ที่ `-15.35%`. Official rolling 10-year NAV Total Return อยู่ที่ `10.52%` annualized ณ 2026-06-30; raw endpoints ของ rolling field ไม่ได้เปิดเผย. ใน common window 2021-2025 VEA ให้ cumulative `54.83%` หรือ CAGR `9.14%` เทียบกับ S&P 500 Total Return ที่ `96.17%` หรือ `14.43%`; lagged `41.34 percentage points` แบบ cumulative.

## Performance check

- `entity_key: NYSE Arca:VEA`
- Fund: `Vanguard FTSE Developed Markets ETF`; inception: 20 ก.ค. 2007; asset class: `International/Global Stock`
- Metric: `NAV Total Return` รวมเงินปันผลและ capital gains ที่ reinvested และหัก fund expenses ตาม Vanguard convention
- Management mode: `passive-index`
- Tracked index (issuer benchmark): `FTSE Developed All Cap ex US Index`
- Common benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference ไม่ใช่ tracked index ของ VEA)
- Official rolling 10-year NAV TR: `10.52%` annualized ณ `2026-06-30`; source ไม่เปิดเผย raw TR endpoints หรือ cumulative value ของ rolling field
- Complete calendar window: `2016-2025` VEA compound `131.10%` / rounded-input CAGR `8.74%`; S&P 500 cache compound `298.33%` / CAGR `14.82%`
- Common window: `2021-2025` VEA compound `54.83%` / rounded-input CAGR `9.14%`; S&P 500 cache compound `96.17%` / CAGR `14.43%`
- Coverage note: annual rows 2016-2025 เป็น official Vanguard NAV total returns; benchmark splice ของ VEA เปลี่ยนตาม index history และ benchmark returns ถูกปรับ withholding taxes. ไม่มี secondary proxy ในตารางนี้.

| ปี | VEA TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 2.51% | 11.96% |
| 2017 | 26.44% | 21.83% |
| 2018 | -14.47% | -4.38% |
| 2019 | 22.08% | 31.49% |
| 2020 | 10.29% | 18.40% |
| 2021 | 11.49% | 28.71% |
| 2022 | -15.35% | -18.11% |
| 2023 | 17.77% | 26.29% |
| 2024 | 3.07% | 25.02% |
| 2025 | 35.15% | 17.88% |

**Up years / Down years**

- Best: 2025, **+35.15%**
- Least positive: 2016, **+2.51%**
- Worst: 2022, **-15.35%**
- Least bad down year: 2018, **-14.47%**
- Current YTD: **+18.46% NAV**, as of **2026-08-26**
- VEA beat the S&P 500 common reference in 2017, 2022, and 2025 (`3 / 10` complete years); this is not a manager-skill claim.

## Risk read-through

Annual NAV TR ของ VEA สะท้อน broad developed-market equity ที่มีช่วงบวกแรงใน 2025 แต่ยังมี downside ชัดเจนใน 2018 และ 2022. Official rolling 10-year NAV TR อยู่ที่ `10.52%` annualized ณ 2026-06-30. 3-year standard deviation อยู่ที่ `13.88%` ณ 2026-06-30; holdings `3,886`, ETF net assets `USD 230.3bn` ณ 2026-07-31, P/E `18.7x`, P/B `2.2x` ณ 2026-06-30, และ turnover `4.10%` ณ fiscal year-end. Expense ratio คือ `0.03%` ณ prospectus 2026-04-28 และ distribution schedule เป็น quarterly.

Official daily NAV Total Return series ที่เปิดเผยเพียงพอสำหรับคำนวณ maximum drawdown และ recovery ยัง `ไม่พบข้อมูลที่ยืนยันได้`; จึงไม่แทนที่ด้วย market-price หรือ secondary proxy. โครงสร้างคือ diversified large-, mid-, และ small-cap developed markets นอกสหรัฐฯ ครอบคลุม Canada, Europe และ Pacific; ความเสี่ยงหลักคือ foreign-market, country, currency, sector และ global-equity risk.

## Sources

- [Vanguard VEA product page](https://investor.vanguard.com/investment-products/etfs/profile/vea) — identity, inception, management style, current YTD and performance summary
- [Vanguard Advisors VEA page](https://advisors.vanguard.com/investments/products/vea/vanguard-ftse-developed-markets-etf) — latest YTD, holdings, net assets, expense ratio, turnover and fund characteristics
- [Vanguard VEA investment profile](https://workplace.vanguard.com/assets/corp/fund_communications/pdf_publish/us-products/investment-profiles/0936.pdf) — official 2016-2025 annual NAV rows, rolling performance, standard deviation and distributions
- [Vanguard VEA summary prospectus](https://www.vanguard.com/pub/Pdf/sp936.pdf) — NYSE Arca listing, objective, index methodology, fees and risks
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached source references in `check-etf-performance` — common USD total-return benchmark for 2016-2025
- [[ETF_performance_sources_2026-08-29]] | [[ETF Performance Index]]
