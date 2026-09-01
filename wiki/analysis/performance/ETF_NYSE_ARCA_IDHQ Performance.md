---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:IDHQ
ticker: IDHQ
input_ticker: IDHQ
exchange: NYSE Arca
fund: Invesco S&P International Developed Quality ETF
tracked_index: S&P Quality Developed ex-U.S. LargeMidCap Index
benchmark: S&P 500 Total Return
updated: 2026-09-01
performance_as_of: 2026-03-31
calendar_years_as_of: 2025-12-31
current_ytd_as_of: 2026-07-31
fund_facts_as_of: 2026-03-31
source_batch: raw/imports/ETF_performance_sources_2026-09-01_run-6.md
return_basis: NAV total return
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/IDHQ
  - geography/International
  - geography/global-developed
---

# IDHQ Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

IDHQ เป็น Invesco S&P International Developed Quality ETF ที่จดทะเบียนบน NYSE
Arca และเป็น passive/index-tracking international developed-market quality ETF.
กองทุนคัดหุ้นจาก S&P Developed ex-U.S. LargeMidCap Index ด้วย quality score ที่
อิง return on equity, accruals ratio และ financial leverage.

Official factsheet ณ 31 มี.ค. 2026 รายงาน 10-year NAV annualized return `8.57%`
และ fund inception annualized return `4.13%`; official YTD ณ วันเดียวกันคือ
`+0.84%`. Latest YTD ที่ยืนยันได้ ณ 31 ก.ค. 2026 คือ secondary NAV observation
`+26.0%`; จึงไม่ถูกนำเสนอเป็น issuer-current field. Official complete calendar
NAV rows 2016-2025 ให้ cumulative `122.28%` หรือ rounded-input CAGR `8.32%`,
เทียบกับ S&P 500 TR ที่ `298.33%` หรือ `14.82%` ต่อปี.

## Performance check

- `entity_key: NYSE Arca:IDHQ`; input ticker: `IDHQ`; listing exchange: NYSE Arca
- Classification: supported passive/index-tracking international developed-market quality equity ETF
- CUSIP `46138E214`; inception: 13 มิ.ย. 2007; management fee and total expense ratio `0.29%`; holdings `193` as of 31 มี.ค. 2026
- Metric: `NAV Total Return` in USD; the issuer index is net return and market-price return remains separate
- Tracked index (issuer benchmark): `S&P Quality Developed ex-U.S. LargeMidCap Index`
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference benchmark ไม่ใช่ tracked index ของกองทุน)
- Official standardized performance as of 31 มี.ค. 2026: NAV YTD `+0.84%`, 1-year `+20.52%`, 3-year annualized `+12.85%`, 5-year annualized `+6.68%`, 10-year annualized `+8.57%`, since inception annualized `+4.13%`
- Latest current YTD cross-check: secondary NAV `+26.0%` as of 31 ก.ค. 2026; official same-date issuer YTD was not established in this capture
- 10-year calendar NAV TR: cumulative `122.28%`; rounded-input CAGR `8.32%` for 2016-2025. This calendar calculation is distinct from the official trailing 10-year period ended 31 มี.ค. 2026.
- 2021-2025 calendar NAV TR: cumulative `36.54%`; rounded-input CAGR `6.43%`

| Year | IDHQ NAV TR | S&P Quality Developed ex-U.S. LargeMidCap Index TR | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | -1.96% | -1.24% | 11.96% |
| 2017 | 26.73% | 26.76% | 21.83% |
| 2018 | -12.74% | -12.63% | -4.38% |
| 2019 | 29.86% | 30.21% | 31.49% |
| 2020 | 15.63% | 15.65% | 18.40% |
| 2021 | 11.29% | 11.60% | 28.71% |
| 2022 | -20.20% | -20.07% | -18.11% |
| 2023 | 18.99% | 19.13% | 26.29% |
| 2024 | 1.90% | 2.07% | 25.02% |
| 2025 | 26.80% | 27.34% | 17.88% |

## Up years / Down years

- Up years / Down years: `7 / 3` across complete calendar years 2016-2025
- Best: 2019, `+29.86%`; least positive: 2024, `+1.90%`
- Worst: 2022, `-20.20%`; least-bad down year: 2016, `-1.96%`
- 2016-2025 rounded-input CAGR: `8.32%`; 2021-2025 rounded-input CAGR: `6.43%`
- Fund/index arithmetic tracking spread: `-0.25 pp` CAGR over 2016-2025 and `-0.25 pp` over 2021-2025; this is not alpha
- Latest secondary NAV YTD remains `+26.0%` as of 31 ก.ค. 2026; no same-date S&P 500 YTD comparison is asserted.

## Risk read-through

IDHQ มี quality-factor และ developed ex-U.S. concentration risk: ผลตอบแทนอาจ
ต่างจาก broad MSCI EAFE เพราะพอร์ตเลือกหุ้น quality สูงและมี country/sector tilts.
Official factsheet รายงาน 193 holdings, P/E `23.81`, P/B `9.02`, ROE `32.01%`
และ 30-day SEC yield `1.02%` ณ 31 มี.ค. 2026. ความเสี่ยงอื่นคือ equity-market,
currency, foreign-market, valuation, tracking error และ rebalance/reconstitution
ทุกครึ่งปี. Annual-return population dispersion จากแถว official 2016-2025 อยู่ที่
`16.45%`; ค่านี้ไม่ใช่ official daily volatility. Daily NAV history สำหรับ
maximum drawdown และ recovery ยังไม่ถูกยืนยัน จึงเป็น `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- [Invesco official IDHQ factsheet](https://www.invesco.com/content/dam/invesco/us/en/product-documents/etf/fact-sheet/idhq-invesco-s-p-international-developed-quality-etf-fact-sheet.pdf) — official identity, index, exchange, fees, holdings, current standardized performance and calendar NAV/index rows; as of 31 มี.ค. 2026
- [SEC IDHQ summary prospectus](https://www.sec.gov/Archives/edgar/data/1168164/000119312526031207/d72607d497k.htm) — official fund objective, quality methodology, index definitions, inception and risk disclosures
- [AAII IDHQ annual-return table](https://www.aaii.com/etf/ticker/IDHQ) — secondary 31 ก.ค. 2026 current-YTD cross-check and display of the official annual-return series
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common benchmark definition
- Cached S&P 500 TR references: [S&P DJI historical research](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [2023 U.S. Equities Market Attributes](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), [2021 S&P DJI market attributes](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/), and [2025 S&P DJI market attributes](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/); cached USD Total Return convention as of 31 ธ.ค. 2025
- ETF source batch: [[ETF_performance_sources_2026-09-01_run-6]] | [[ETF Performance Index]]

---
window: complete calendar years 2016-2025 plus current 2026 YTD
return_basis: NAV total return
verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
---
