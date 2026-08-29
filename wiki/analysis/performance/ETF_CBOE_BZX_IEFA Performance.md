---
type: etf-performance
instrument_type: ETF
entity_key: Cboe BZX:IEFA
ticker: IEFA
exchange: Cboe BZX
updated: 2026-08-29
source_batch: raw/imports/ETF_performance_sources_2026-08-29.md
return_basis: NAV total return for official fields; secondary dividend-reinvested proxy for rows marked *
management_mode: passive-index
tags:
  - analysis/etf-performance
  - geography/International
  - ticker/IEFA
---

# IEFA Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

IEFA เป็น passive developed-markets ETF ที่ไม่รวมสหรัฐฯ และแคนาดา. Official
rolling 10-year NAV Total Return อยู่ที่ `9.78%` annualized ณ 2026-06-30 และ
official NAV TR YTD ล่าสุดที่ reviewed คือ `14.71%` ณ 2026-08-26. Official
calendar rows ที่เปิดเผยใน iShares capture คือ 2021-2025; คำนวณได้ compound
`51.46%` และ rounded-input CAGR `8.66%`. เทียบกับ S&P 500 Total Return ช่วงเดียวกัน
ที่ `96.17%` / `14.43%`; cumulative gap คือ `44.71 percentage points`.

## Performance check

- `entity_key: Cboe BZX:IEFA`
- Fund: `iShares Core MSCI EAFE ETF`; inception: 18 ต.ค. 2012; asset class: equity
- Metric: official fields เป็น `NAV Total Return` รวมเงินปันผลและ capital gains ที่ reinvested และหักค่าใช้จ่ายตาม issuer convention
- Management mode: `passive-index`; implementation ใช้ sampling และ systematic fair value
- Tracked index (issuer benchmark): `MSCI EAFE IMI Index (Net)`
- Common benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference ไม่ใช่ tracked index ของ IEFA)
- Official rolling 10-year NAV TR: `9.78%` annualized ณ `2026-06-30`; official 5-year NAV TR annualized `8.81%` ใน performance capture เดียวกัน
- Official current NAV TR YTD: `14.71%` ณ `2026-08-26`; NAV `USD 100.61` ณ `2026-08-27` และ closing price `USD 100.96` ณ `2026-08-26`
- Complete calendar window: `2016-2025` secondary dividend-reinvested proxy compound `122.96%*` / rounded-input CAGR `8.35%*`; official 2021-2025 rows compound `51.46%` / CAGR `8.66%`
- Common official window: `2021-2025` IEFA compound `51.46%` / CAGR `8.66%`; S&P 500 cache compound `96.17%` / CAGR `14.43%`
- Coverage note: table แสดง secondary proxy* เพื่อให้เห็น 2016-2025 ครบหน้าต่าง; official iShares calendar rows 2021-2025 ใช้คำนวณ common window แยกต่างหาก. Proxy ไม่ถูกเรียกว่า official NAV TR และไม่ใช้แทน tracked benchmark

| ปี | IEFA total-return proxy* | S&P 500 TR |
|---|---:|---:|
| 2016 | 1.58%* | 11.96% |
| 2017 | 26.57%* | 21.83% |
| 2018 | -14.14%* | -4.38% |
| 2019 | 22.64%* | 31.49% |
| 2020 | 8.18%* | 18.40% |
| 2021 | 11.64%* | 28.71% |
| 2022 | -15.24%* | -18.11% |
| 2023 | 17.95%* | 26.29% |
| 2024 | 3.27%* | 25.02% |
| 2025 | 32.08%* | 17.88% |

**Up years / Down years — official 2021-2025 window**

- Best official year: 2025, **+31.83%**
- Least positive official year: 2024, **+3.41%**
- Worst official year: 2022, **-15.13%**
- Least bad official down year: 2022, **-15.13%**
- Official current YTD: **+14.71% NAV**, as of **2026-08-26**
- IEFA official NAV beat the S&P 500 common reference in 2025 and underperformed in 2021-2024 (`1 / 5` official complete years); this arithmetic comparison is not a manager-skill claim

## Risk read-through

IEFA ให้ large-, mid- และ small-cap exposure ใน developed markets นอกสหรัฐฯ และ
แคนาดา. Official snapshot ณ 2026-08-27/26 แสดง net assets `USD 195.41bn`,
holdings `2,616`, P/E `19.09x`, P/B `2.25x`, 3-year standard deviation `12.99%`,
30-day SEC yield `2.30%`, trailing yield `3.31%`, premium/discount `0.16%`, และ
30-day median bid/ask spread `0.01%`. Expense ratio คือ `0.07%`, distribution
frequency เป็น semi-annual. Current listing ตาม iShares คือ `Cboe BZX` แม้
แหล่งข้อมูลเก่าบางแห่งอาจเรียก NYSE Arca.

BlackRock/iShares ระบุ systematic fair-value timing differences, foreign-market,
currency, country, liquidity และ non-diversification risks. Official daily NAV
Total Return series ที่เปิดเผยเพียงพอสำหรับ maximum drawdown และ recovery ยัง
`ไม่พบข้อมูลที่ยืนยันได้`; จึงไม่แทนที่ด้วย market-price หรือ secondary drawdown
proxy. Proxy annual rows ใช้เป็น historical context เท่านั้น.

## Sources

- [iShares IEFA product page](https://www.ishares.com/us/products/244049/ishares-core-msci-eafe-etf?fundSearch=true&qt=IEFA) — identity, current Cboe BZX listing, inception, benchmark, official 2021-2025 calendar rows, current NAV/YTD, assets, holdings, valuation, standard deviation and fees
- [iShares IEFA fact sheet](https://www.ishares.com/us/literature/fact-sheet/iefa-ishares-core-msci-eafe-etf-fund-fact-sheet-en-us.pdf) — fund objective and performance-document context
- [iShares IEFA documents](https://www.ishares.com/us/products/244049/ishares-core-msci-eafe-etf?fundSearch=true&qt=IEFA) — prospectus and regulatory-document access through the product page
- [FinanceCharts IEFA performance](https://www.financecharts.com/etfs/IEFA/performance) — secondary dividend-reinvested annual proxy for 2016-2025 context
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached source references in `check-etf-performance` — common USD total-return benchmark for 2016-2025 and 2021-2025
- [[ETF_performance_sources_2026-08-29]] | [[ETF Performance Index]]
