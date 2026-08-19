---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:EWU
input_ticker: EWU
ticker: EWU
exchange: NYSE Arca
fund: iShares MSCI United Kingdom ETF
tracked_index: MSCI United Kingdom Index (Net)
benchmark: S&P 500 Total Return
management_mode: passive-index
updated: 2026-08-19
performance_as_of: 2025-12-31
rolling_10y_as_of: 2026-06-30
current_ytd_as_of: 2026-08-17
price_nav_as_of: 2026-08-18
fund_facts_as_of: 2026-08-18
source_batch: raw/imports/ETF_performance_sources_2026-08-19.md
return_basis: NAV total return; distributions reinvested; fund expenses reflected in NAV
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/EWU
  - geography/United-Kingdom
---

# EWU Performance

> Navigation: [[ETF Region Index]] → [[United Kingdom ETF]] → [[ETF Performance Index]]

## Bottom line

`EWU` คือ iShares MSCI United Kingdom ETF ที่จดทะเบียนบน NYSE Arca และเป็น
`passive-index` equity ETF ซึ่งติดตาม `MSCI United Kingdom Index (Net)`. Official
rolling 10-year NAV TR CAGR อยู่ที่ `8.21%` ณ 30 มิ.ย. 2026; ส่วน annual rows
แบบครบปี 2016-2025 compound ได้ `101.02%` หรือ rounded-input CAGR `7.23%` และ
ช่วง 2021-2025 ได้ `81.59%` หรือ `12.67%` ต่อปี. Latest official NAV TR YTD
คือ `11.22%` ณ 17 ส.ค. 2026. Rolling field กับ calendar-derived CAGR เป็นคนละ
หน้าต่างเวลา จึงไม่ใช้แทนกัน.

## Performance check

- `entity_key: NYSE Arca:EWU`; official fund name, ticker, exchange and inception date `1996-03-12` are confirmed by iShares.
- Classification: `passive-index` / indexed equity. The fund uses representative sampling to track the MSCI United Kingdom Index, which measures UK large- and mid-cap equities; it does not seek to outperform the index.
- Metric: issuer NAV `Total Return` includes reinvested distributions and reflects fund expenses. Market-price return is kept separate from the NAV series.
- Issuer benchmark: `MSCI United Kingdom Index (Net)`; `S&P 500 Total Return` is a common USD reference benchmark, not the tracked index.
- Expense ratio: `0.50%`; distribution frequency: semi-annual; holdings: `67` as of 17 ส.ค. 2026.
- Official rolling fields as of 30 มิ.ย. 2026: NAV TR 1-year `19.23%`, 3-year annualised `16.76%`, 5-year annualised `11.31%`, 10-year annualised `8.21%`, and since inception annualised `5.99%`.
- Latest official issuer snapshot: NAV `$48.17` and total net assets `$3,781,711,907` as of 18 ส.ค. 2026; closing price `$48.16` as of 17 ส.ค. 2026; shares outstanding `78,500,000` as of 18 ส.ค. 2026; and 67 holdings as of 17 ส.ค. 2026. NAV TR YTD was `+11.22%` as of 17 ส.ค. 2026.
- Annual coverage: iShares' official 2016-2025 chart rows are used; 2016-2020 values are displayed by the professional product page rounded to 0.1 percentage point, while 2021-2025 values are available to two decimals from the U.S. product page/factsheet.

| Year | EWU NAV TR (USD) | MSCI United Kingdom Index (Net) (USD) | S&P 500 TR (USD) |
|---|---:|---:|---:|
| 2016 | -0.60% | -0.10% | 11.96% |
| 2017 | 21.70% | 22.30% | 21.83% |
| 2018 | -14.60% | -14.20% | -4.38% |
| 2019 | 20.40% | 21.00% | 31.49% |
| 2020 | -11.00% | -10.50% | 18.40% |
| 2021 | 17.89% | 18.50% | 28.71% |
| 2022 | -5.13% | -4.84% | -18.11% |
| 2023 | 13.03% | 14.09% | 26.29% |
| 2024 | 6.84% | 7.54% | 25.02% |
| 2025 | 34.45% | 35.11% | 17.88% |

จาก annual rows ที่แสดงข้างต้น EWU NAV TR compound ได้ `101.02%` / rounded-input
CAGR `7.23%` ในปี 2016-2025 และ `81.59%` / `12.67%` ในปี 2021-2025. Issuer
benchmark compound ได้ `112.24%` / `7.82%` และ `86.95%` / `13.33%` ตามลำดับ;
fund-minus-index อยู่ที่ประมาณ `-0.58 pp` และ `-0.66 pp` ซึ่งเป็น passive
tracking/cost observation ไม่ใช่ alpha. Cached S&P 500 TR compound ได้ `298.33%`
/ `14.82%` ในปี 2016-2025 และ `96.17%` / `14.43%` ในปี 2021-2025; EWU ต่ำกว่า
common USD reference ประมาณ `-7.59 pp` และ `-1.75 pp` ตามลำดับ.

Official issuer rolling 10-year field ณ 30 มิ.ย. 2026 รายงาน cumulative NAV TR
`120.07%` และ CAGR `8.21%`; ค่า `7.23%` ข้างต้นเป็น calendar-derived CAGR จาก
annual rows ที่มีการปัดเศษ จึงไม่ใช่การคัดลอก rolling field.

## Up years / Down years

- Complete 2016-2025 NAV TR up/down: `6 / 4`
- Best NAV TR year: 2025, `+34.45%`
- Least positive year: 2024, `+6.84%`
- Worst NAV TR year: 2018, `-14.60%`
- Least bad down year: 2016, `-0.60%`
- Average positive year: `+19.05%` from the six positive annual rows.
- Current official NAV TR YTD: `+11.22%` as of 17 ส.ค. 2026.

## Risk read-through

Current iShares characteristics report 3-year standard deviation `11.89%` and
equity beta `0.43` as of 31 ก.ค. 2026; P/E `17.99x` and P/B `2.40x` as of 17 ส.ค.
2026. Portfolio weights as of 17 ส.ค. 2026 were Financials `27.70%`, Industrials
`14.12%`, Consumer Staples `13.71%`, Health Care `12.11%`, Energy `11.23%`, and
Materials `8.22%`. UK/country, GBP/USD, sector,
large-cap and geopolitical/trade risks remain relevant. The fund's 0.50% expense
ratio and the approximately negative tracking differences are consistent with
passive implementation; they are not evidence of manager skill. Official daily
NAV maximum drawdown and recovery date were not disclosed in the reviewed sources;
risk-adjusted evidence is therefore `not-verified` for those fields.

## Sources

- [iShares EWU product page](https://www.ishares.com/us/products/239690/ishares-msci-united-kingdom-etf) — identity, current NAV/price, YTD, rolling returns, holdings, sectors, risk and distributions.
- [iShares EWU factsheet](https://www.ishares.com/us/literature/fact-sheet/ewu-ishares-msci-united-kingdom-etf-fund-fact-sheet-en-us.pdf) — official fund facts and 2021-2025 performance rows as of June 30, 2026.
- [iShares EWU summary prospectus](https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-united-kingdom-etf-8-31.pdf) — passive objective, sampling, benchmark and expense structure.
- [iShares UK professional EWU page](https://www.ishares.com/uk/professional/en/products/239690/ishares-msci-united-kingdom-etf?shortLocale=en_GB) — 2016-2020 annual chart rows displayed to 0.1 percentage point.
- Cached S&P 500 TR references: [S&P 500 low-volatility research PDF](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [U.S. equity market attributes July 2023](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), [December 2021](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/), and [current market attributes archive](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/).
- Source batch: [[ETF_performance_sources_2026-08-19]] | [[ETF Performance Index]]
