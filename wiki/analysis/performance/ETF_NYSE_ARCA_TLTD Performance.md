---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:TLTD
ticker: TLTD
input_ticker: TLTD
exchange: NYSE Arca
fund: Northern Trust Morningstar Developed Markets ex-US Factor Tilt ETF
tracked_index: Morningstar Developed Markets ex-US Factor Tilt Index
benchmark: S&P 500 Total Return
updated: 2026-09-01
performance_as_of: 2026-07-31
calendar_years_as_of: 2025-12-31
current_ytd_as_of: 2026-07-31
price_nav_as_of: 2026-08-28
fund_facts_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-09-01_run-6.md
return_basis: NAV total return
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/TLTD
  - geography/International
  - geography/global-developed
---

# TLTD Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

TLTD เป็น Northern Trust Morningstar Developed Markets ex-US Factor Tilt ETF
(ชื่อเดิม FlexShares) ที่จดทะเบียนบน NYSE Arca. กองทุนเป็น passive,
representative-sampling, factor-tilted international equity ETF ซึ่งเพิ่มน้ำหนัก
small-cap และ value เมื่อเทียบกับ developed ex-US parent index.

Official current NAV Total Return YTD คือ `+11.45%` ณ 31 ก.ค. 2026 และ official
10-year NAV annualized return คือ `9.71%` ณ วันเดียวกัน. จาก annual NAV rows
ที่เผยแพร่โดย secondary data cross-check สำหรับปีเต็ม 2016-2025, TLTD มี
cumulative return `131.19%` หรือ rounded-input CAGR `8.74%`; เทียบกับ S&P 500 TR
ที่ `298.33%` หรือ `14.82%` ต่อปี. ช่วง 2021-2025 TLTD ทำ CAGR `10.65%` เทียบกับ
S&P 500 ที่ `14.43%`.

## Performance check

- `entity_key: NYSE Arca:TLTD`; official exchange: NYSE Arca; fund formerly known as FlexShares Morningstar Developed Markets ex-US Factor Tilt Index Fund
- Classification: supported passive/index-tracking developed ex-US factor equity ETF
- CUSIP `33939L803`; inception: 25 ก.ย. 2012; net expense ratio `0.39%`; gross expense ratio `0.41%`; representative sampling; quarterly distributions
- Metric: `NAV Total Return` with dividends and capital gains reinvested at NAV; currency USD. Market-price return remains separate.
- Tracked index (issuer benchmark): `Morningstar Developed Markets ex-US Factor Tilt Index`
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference benchmark ไม่ใช่ tracked index ของกองทุน)
- Official current performance: NAV YTD `+11.45%`, 1-year `+27.05%`, 3-year annualized `+18.72%`, 5-year annualized `+10.65%`, 10-year annualized `+9.71%`, and since-inception `+8.38%`, all as of 31 ก.ค. 2026
- Latest official NAV: `US$105.33` and market price `US$104.51` as of 28 ส.ค. 2026; net assets `US$695.16m`
- 10-year calendar NAV TR: cumulative `131.19%`; rounded-input CAGR `8.74%` for 2016-2025. The official standardized 10-year window is a trailing July window and is not expected to equal the calendar-year calculation.
- 2021-2025 calendar NAV TR: cumulative `65.88%`; rounded-input CAGR `10.65%`
- Annual rows are marked secondary because the retrieved issuer page exposes the current NAV series and standardized periods but not a text calendar-year table; the secondary rows reconcile directionally with the official 2025 standardized and five-year fields.

| Year | TLTD NAV TR* | S&P 500 TR |
|---|---:|---:|
| 2016 | 5.40% | 11.96% |
| 2017 | 25.90% | 21.83% |
| 2018 | -17.20% | -4.38% |
| 2019 | 21.50% | 31.49% |
| 2020 | 4.40% | 18.40% |
| 2021 | 12.30% | 28.71% |
| 2022 | -13.70% | -18.11% |
| 2023 | 17.50% | 26.29% |
| 2024 | 5.10% | 25.02% |
| 2025 | 38.60% | 17.88% |

\* Annual TLTD rows are rounded secondary data; they are not substituted for the official standardized NAV return fields.

## Up years / Down years

- Up years / Down years: `8 / 2` across complete calendar years 2016-2025
- Best: 2025, `+38.60%`; least positive: 2020, `+4.40%`
- Worst: 2018, `-17.20%`; least-bad down year: 2022, `-13.70%`
- 2016-2025 rounded-input CAGR: `8.74%`; 2021-2025 rounded-input CAGR: `10.65%`
- Official current NAV TR YTD remains `+11.45%` as of 31 ก.ค. 2026; no same-date S&P 500 YTD comparison is asserted.

## Risk read-through

TLTD มี foreign-market, currency, liquidity, small-cap, value, concentration,
derivative และ tracking-error risks. Index methodology intentionally tilts toward
smaller and lower-valuation companies, soผลตอบแทนสามารถต่างจาก broad developed
ex-US market ได้มาก โดยเฉพาะช่วงที่ large-cap growth นำตลาด. Official factsheet
รายงาน 2,307 holdings และ weighted average beta `1.03` ณ 30 มิ.ย. 2026; Northern
Trust ระบุว่าใช้ representative sampling และมีการ rebalance/reconstitution ตาม
index. Annual-return population dispersion จากแถว rounded 2016-2025 อยู่ที่
`16.26%`; ค่านี้ไม่ใช่ official daily volatility. Daily NAV history สำหรับ
maximum drawdown และ recovery ยังไม่ถูกยืนยัน จึงเป็น `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- [Northern Trust official TLTD product page](https://etfs.ntam.northerntrust.com/us/en/individual/funds/tltd) — current NAV/market price, official YTD and trailing annualized returns, exchange, fee, methodology and risk disclosures; current observations through 28 ส.ค. 2026
- [Northern Trust official TLTD factsheet](https://www.flexshares.com/content/dam/ntflexshares/fund-documents/tltd/tltd-factsheet.pdf.coredownload.pdf) — inception, exchange, holdings, fees, beta, factor approach and June 2026 portfolio facts
- [SEC TLTD summary prospectus](https://www.sec.gov/Archives/edgar/data/1491978/000119312526352175/d272956d497k.htm) — legal identity, passive strategy, 2025 standardized returns, fee reimbursement and principal risks
- [AAII TLTD annual-return table](https://www.aaii.com/etf/ticker/TLTD) — secondary rounded annual NAV return rows used only for the calendar-year table and calculations
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common benchmark definition
- Cached S&P 500 TR references: [S&P DJI historical research](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [2023 U.S. Equities Market Attributes](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), [2021 S&P DJI market attributes](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/), and [2025 S&P DJI market attributes](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/); cached USD Total Return convention as of 31 ธ.ค. 2025
- ETF source batch: [[ETF_performance_sources_2026-09-01_run-6]] | [[ETF Performance Index]]

---
window: complete calendar years 2016-2025 plus current 2026 YTD
return_basis: NAV total return
verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
---
