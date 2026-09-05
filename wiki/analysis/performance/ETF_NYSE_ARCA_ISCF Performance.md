---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:ISCF
ticker: ISCF
exchange: NYSE Arca
fund: iShares International Small-Cap Equity Factor ETF
tracked_index: STOXX International Small-Cap Equity Factor Index (USD) (Net)
benchmark: S&P 500 Total Return
updated: 2026-09-02
performance_as_of: 2025-12-31
calendar_years_as_of: 2025-12-31
rolling_10y_as_of: 2026-06-30
current_ytd_as_of: 2026-08-28
price_nav_as_of: 2026-08-28
fund_facts_as_of: 2026-08-28
source_batch: raw/imports/ETF_performance_sources_2026-09-02_run-3.md
return_basis: NAV total return
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/ISCF
  - geography/International
  - geography/international-ex-US
---

# ISCF Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

ISCF เป็น passive/index-tracking international small-cap multifactor ETF ที่ติดตาม
STOXX International Small-Cap Equity Factor Index (USD) (Net) และลงทุนใน developed
markets นอกสหรัฐฯ. Official complete calendar-year NAV Total Return 2016-2025 ให้
cumulative `127.24%` หรือ rounded-input CAGR `8.55%`; issuer rolling 10-year
average annual NAV TR คือ `9.69%` ณ 30 มิ.ย. 2026 ซึ่งเป็นคนละ metric. ช่วง
2021-2025 ให้ cumulative `50.01%` / CAGR `8.45%`, เทียบกับ S&P 500 TR
`96.17%` / `14.43%`. Current official NAV TR YTD ล่าสุดคือ `+12.99%` ณ 28 ส.ค.
2026.

## Performance check

- `entity_key: NYSE Arca:ISCF`; primary exchange: NYSE Arca
- Classification: supported passive/index-tracking international small-cap equity ETF
- Inception: 28 เม.ย. 2015; expense ratio `0.24%`
- Metric: `NAV Total Return` รวม reinvested dividends/capital gains และ fund expenses; currency USD
- Tracked index (current issuer benchmark): `STOXX International Small-Cap Equity Factor Index (USD) (Net)`
- Benchmark history note: ISCF began tracking STOXX on 1 มี.ค. 2023; historical index data before that date is for `MSCI World ex USA Small Cap Diversified Multiple-Factor Index (Net)`
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference benchmark ไม่ใช่ tracked index ของ ISCF)
- Official rolling 10-year NAV TR: average annual `9.69%` ณ 30 มิ.ย. 2026; raw rolling endpoints ไม่ได้เปิดเผย จึงแยกจาก calendar-window CAGR `8.55%`
- 2016-2025 calendar NAV TR: cumulative `127.24%`; rounded-input CAGR `8.55%`
- 2021-2025 calendar NAV TR: cumulative `50.01%`; rounded-input CAGR `8.45%`; S&P 500 cached cumulative `96.17%` / CAGR `14.43%`
- Current official fields: NAV `US$45.92` ณ 28 ส.ค. 2026, closing price `US$46.01` ณ 28 ส.ค. 2026, net assets `US$684.26m` ณ 28 ส.ค. 2026, holdings `1,161` ณ 28 ส.ค. 2026, และ NAV TR YTD `+12.99%` ณ 28 ส.ค. 2026
- Coverage/source note: official SEC summary prospectus supplies 2016-2024 annual NAV rows; official June 2026 factsheet supplies 2025 and current fund/benchmark fields; S&P annual rows use cached USD Total Return convention as of 31 ธ.ค. 2025

| Year | ISCF NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 0.01% | 11.96% |
| 2017 | 36.24% | 21.83% |
| 2018 | -18.18% | -4.38% |
| 2019 | 25.94% | 31.49% |
| 2020 | 7.89% | 18.40% |
| 2021 | 13.22% | 28.71% |
| 2022 | -15.06% | -18.11% |
| 2023 | 11.52% | 26.29% |
| 2024 | 4.33% | 25.02% |
| 2025 | 34.07% | 17.88% |

S&P 500 เป็น common reference benchmark ไม่ใช่ issuer benchmark ของ ISCF;
annual rows ใช้ cached USD Total Return convention และไม่ได้ผสมกับ market-price
return ของ ISCF.

## Up years / Down years

- Up years / Down years: `8 / 2` ใน complete calendar years 2016-2025
- Best: 2017, `+36.24%`
- Least positive: 2016, `+0.01%`
- Worst: 2018, `-18.18%`
- Least bad down year: 2022, `-15.06%`
- 2016-2025 cumulative/CAGR: ISCF `127.24%` / `8.55%`; S&P 500 TR `298.33%` / `14.82%`
- 2021-2025 cumulative/CAGR: ISCF `50.01%` / `8.45%`; S&P 500 TR `96.17%` / `14.43%`
- Current ISCF NAV TR YTD: `+12.99%` ณ 28 ส.ค. 2026; current S&P YTD ไม่ได้อ้างว่าเป็นวันเดียวกัน

## Risk read-through

ISCF มี international small-cap, factor-regime, country, currency และ liquidity
sensitivity. Official iShares fields รายงาน 3-year standard deviation `14.21%` ณ
31 ก.ค. 2026, beta `0.73` ณ 31 ก.ค. 2026 และ holdings `1,161` ณ 28 ส.ค. 2026.
Index splice ในปี 2023 ทำให้การอ่าน tracking behavior ต้องแยกช่วงก่อนและหลังการ
เปลี่ยน benchmark. Official daily NAV history ที่เพียงพอสำหรับคำนวณ maximum
drawdown และ recovery ยังไม่ถูกยืนยัน จึงไม่บันทึกตัวเลข proxy.

## Sources

- [iShares ISCF product page](https://www.ishares.com/us/products/272823/ishares-international-small-cap-equity-factor-etf) — identity, NYSE Arca listing, benchmark, inception, current NAV/price/YTD, holdings and risk fields
- [Official ISCF fact sheet](https://www.ishares.com/us/literature/fact-sheet/iscf-ishares-international-small-cap-equity-factor-etf-fund-fact-sheet-en-us.pdf) — 2021-2025 NAV/market-price/benchmark rows, return basis, current benchmark metadata and fund characteristics; as of 30 Jun 2026
- [ISCF summary prospectus](https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-edge-msci-multifactor-intl-small-cap-etf-7-31.pdf) — 2016-2024 annual rows, passive objective, fees, best/worst quarters and benchmark splice
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common benchmark definition
- Cached S&P 500 TR references: [2016-2019](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [2018-2022](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), [2021](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/), and [2022-2025](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/)
- ETF source batch: [[ETF_performance_sources_2026-09-02_run-3]] | [[ETF Performance Index]]
