---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:IDEV
ticker: IDEV
exchange: NYSE Arca
updated: 2026-08-29
source_batch: raw/imports/ETF_performance_sources_2026-08-29.md
return_basis: NAV total return for official fields; secondary dividend-reinvested proxy for rows marked *
management_mode: passive-index
tags:
  - analysis/etf-performance
  - geography/International
  - ticker/IDEV
---

# IDEV Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

IDEV เป็น passive broad developed-markets ex-U.S. ETF ที่เริ่มกองทุนเมื่อ
21 มี.ค. 2017. ดังนั้นยังไม่มี complete 10-year history และไม่ควรเติม 2016-2017
ที่ไม่มีข้อมูลเต็มปี. Official iShares
NAV TR YTD ล่าสุดที่ reviewed คือ `14.77%` ณ 2026-08-27 และ official complete
calendar rows ที่อ่านได้คือ 2021-2025: compound `55.79%` และ rounded-input CAGR
`9.27%`. เทียบกับ S&P 500 Total Return ช่วงเดียวกันที่ `96.17%` / `14.43%`;
ช่องว่าง cumulative `40.38 percentage points`.

## Performance check

- `entity_key: NYSE Arca:IDEV`
- Fund: `iShares Core MSCI International Developed Markets ETF`; inception: 21 มี.ค. 2017; asset class: equity
- Metric: official fields เป็น `NAV Total Return` รวมเงินปันผลและ capital gains ที่ reinvested และหักค่าใช้จ่ายตาม issuer convention
- Management mode: `passive-index`; กองทุนติดตามดัชนีด้วย systematic fair value และ sampling/portfolio implementation
- Tracked index (issuer benchmark): `MSCI World ex USA IMI Index (Net)`
- Common benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference ไม่ใช่ tracked index ของ IDEV)
- Official rolling 10-year NAV TR: `ไม่พบข้อมูลที่ยืนยันได้` เพราะ fund inception ยังไม่ครบ 10 ปี; official 5-year NAV TR annualized คือ `9.15%` ณ `2026-06-30`
- Official current NAV TR YTD: `14.77%` ณ `2026-08-27`; official NAV `USD 92.70` และ closing price `USD 92.89` ณ `2026-08-28`
- Complete available calendar window: `2021-2025` official NAV rows compound `55.79%` / rounded-input CAGR `9.27%`; S&P 500 cache compound `96.17%` / CAGR `14.43%`
- Coverage note: official rows 2021-2025 มาจาก iShares calendar-year table. Rows 2018-2020 ใน table เป็น secondary dividend-reinvested proxy* เพื่อแสดงบริบทเท่านั้น; 2016-2017 ไม่มี complete usable years เพราะ inception ปี 2017 เป็น partial year. ไม่คำนวณ 2018-2025 CAGR จาก mixed sources.

| ปี | IDEV NAV TR / proxy | S&P 500 TR |
|---|---:|---:|
| 2018 | -14.10%* | -4.38% |
| 2019 | 23.13%* | 31.49% |
| 2020 | 8.32%* | 18.40% |
| 2021 | 12.72% | 28.71% |
| 2022 | -14.94% | -18.11% |
| 2023 | 17.28% | 26.29% |
| 2024 | 4.49% | 25.02% |
| 2025 | 32.59% | 17.88% |

**Up years / Down years — official 2021-2025 window**

- Best official year: 2025, **+32.59%**
- Least positive official year: 2024, **+4.49%**
- Worst official year: 2022, **-14.94%**
- Least bad official down year: 2022, **-14.94%**
- Official current YTD: **+14.77% NAV**, as of **2026-08-27**
- IDEV official NAV beat the S&P 500 common reference in 2025 and underperformed in 2021-2024 (`1 / 5` official complete years); this arithmetic comparison is not a manager-skill claim

## Risk read-through

IDEV ให้ large-, mid- และ small-cap exposure ใน developed markets นอกสหรัฐฯ
ผ่านประเทศอย่าง Japan, United Kingdom, Canada, France, Switzerland และ Germany.
Official snapshot ณ 2026-08-28 แสดง net assets `USD 32.75bn`, holdings `2,312`
ณ 2026-08-27, P/E `19.44x`, P/B `2.32x` ณ 2026-08-27, 3-year standard deviation
`12.92%` ณ 2026-07-31, 30-day SEC yield `2.26%` และ 12-month trailing yield
`3.14%` ณ 2026-07-31. Expense ratio คือ `0.04%`, distribution frequency เป็น
semi-annual, และ fund เป็น passive.

BlackRock/iShares ระบุ systematic fair-value timing differences ที่ทำให้ total
return อาจต่างจาก benchmark ได้ รวมถึง foreign-market, currency, country,
liquidity, sector และ non-diversification risks. Official daily NAV Total Return
series ที่เปิดเผยเพียงพอสำหรับ maximum drawdown และ recovery ยัง `ไม่พบข้อมูลที่
ยืนยันได้`; จึงไม่แทนที่ด้วย market-price หรือ secondary drawdown proxy. Proxy
rows 2018-2020 ไม่ควรนำมาเทียบเป็น official NAV sequence กับ 2021-2025.

## Sources

- [iShares IDEV product page](https://www.ishares.com/us/products/286762/ishares-core-msci-international-developed-markets-etf) — identity, exchange, inception, benchmark, official 2021-2025 calendar rows, current NAV/YTD, assets, holdings, valuation, standard deviation and fees
- [iShares IDEV fact sheet](https://www.ishares.com/us/literature/fact-sheet/idev-ishares-core-msci-international-developed-markets-etf-fund-fact-sheet-en-us.pdf) — fund objective and performance-document context
- [SEC IDEV prospectus](https://www.sec.gov/Archives/edgar/data/1317146/000113322826007243/mmlsif-efp24450_497.htm) — objective, MSCI World ex USA Investable Market Index strategy and developed-country scope
- [FinanceCharts IDEV performance](https://www.financecharts.com/etfs/IDEV/performance) — secondary dividend-reinvested proxy for 2018-2020 only; not substituted for official 2021-2025 NAV TR
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached source references in `check-etf-performance` — common USD total-return benchmark for 2021-2025
- [[ETF_performance_sources_2026-08-29]] | [[ETF Performance Index]]
