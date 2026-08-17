---
type: etf-performance
instrument_type: ETF
entity_key: NASDAQ:SCZ
ticker: SCZ
exchange: NASDAQ
fund: iShares MSCI EAFE Small-Cap ETF
tracked_index: MSCI EAFE Small Cap Index (Net)
benchmark: S&P 500 Total Return
updated: 2026-08-17
performance_as_of: 2025-12-31
rolling_10y_as_of: 2026-06-30
current_ytd_as_of: 2026-08-13
price_nav_as_of: 2026-08-14
fund_facts_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-08-17.md
return_basis: NAV total return
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/SCZ
  - geography/International
  - geography/international-ex-US
---

# SCZ Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

SCZ เป็น passive/index-tracking international small-cap ETF ที่ติดตาม MSCI EAFE
Small Cap Index (Net). ใน complete calendar window 2016-2025 มี 8 ปีบวก / 2 ปีลบ;
จากตัวเลข NAV Total Return ที่แสดง คำนวณได้ cumulative `104.25%` หรือ rounded-input
CAGR `7.40%`, เทียบ S&P 500 TR `298.33%` / `14.82%`. ปีดีที่สุดคือ 2025 ที่
`+32.10%` และแย่ที่สุดคือ 2022 ที่ `-21.22%`; current official NAV TR YTD คือ
`+13.83%` ณ 13 ส.ค. 2026.

## Performance check

- `entity_key: NASDAQ:SCZ`
- Classification: supported passive/index-tracking equity ETF; iShares states that
  the fund seeks to track a small-cap developed-market index outside the U.S. and Canada.
- Inception: 10 ธ.ค. 2007; expense ratio `0.40%`
- Metric: `NAV Total Return` บนฐาน USD รวมเงินปันผลและ capital gains ที่ reinvested;
  fund expenses ถูกหักออกตาม factsheet
- Tracked index (issuer benchmark): `MSCI EAFE Small Cap Index (Net)`
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference
  benchmark ไม่ใช่ tracked index ของ SCZ)
- Official rolling 10-year NAV TR: issuer-reported average annual `8.60%` ณ 30 มิ.ย.
  2026; raw rolling endpoints ไม่ได้เปิดเผย จึงแยกจาก calendar-window CAGR `7.40%`
- Current NAV: `US$87.17` ณ 14 ส.ค. 2026; closing price `US$87.14` วันเดียวกัน
- Annual coverage: official complete calendar years 2016-2025; 2016-2020 ใช้
  iShares product table ที่แสดงหนึ่งตำแหน่งทศนิยม และ 2021-2025 ใช้ official
  June 2026 factsheet ที่แสดงสองตำแหน่ง; cumulative/CAGR เป็น rounded-input calculations

| Year | SCZ NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 2.40% | 11.96% |
| 2017 | 32.50% | 21.83% |
| 2018 | -17.80% | -4.38% |
| 2019 | 24.70% | 31.49% |
| 2020 | 12.10% | 18.40% |
| 2021 | 10.02% | 28.71% |
| 2022 | -21.22% | -18.11% |
| 2023 | 12.90% | 26.29% |
| 2024 | 1.35% | 25.02% |
| 2025 | 32.10% | 17.88% |

## Up years / Down years

- Up years / Down years: `8 / 2` ใน 2016-2025
- Best: 2025, `+32.10%`
- Least positive: 2024, `+1.35%`
- Worst: 2022, `-21.22%`
- Least bad down year: 2018, `-17.80%`
- 2016-2025 cumulative/CAGR: SCZ `104.25%` / `7.40%`; S&P 500 TR `298.33%` / `14.82%`
- 2021-2025 cumulative/CAGR: SCZ `31.01%` / `5.55%`; S&P 500 TR `96.17%` / `14.43%`
- Current SCZ NAV TR YTD: `+13.83%` ณ 13 ส.ค. 2026; current S&P field is not
  asserted as a same-date comparison

## Risk read-through

SCZ ให้ developed-market small-cap exposure นอกสหรัฐฯ และแคนาดา จึงมี small-cap,
country, currency และ liquidity sensitivity สูงกว่า developed-market broad equity.
Official iShares fields รายงาน 3-year standard deviation `14.97%` และ beta `0.78`
ณ 31 ก.ค. 2026; holdings `2,056` ณ 13 ส.ค. 2026. Rolling 10-year issuer average
annual NAV TR `8.60%` เป็นคนละ window กับ calendar CAGR `7.40%` และไม่มี raw endpoints
ให้คำนวณซ้ำ. Official daily NAV history ที่เพียงพอสำหรับ maximum drawdown และ
recovery ยังไม่ถูกยืนยัน จึงไม่บันทึกตัวเลข proxy.

## Sources

- [iShares SCZ product page](https://www.ishares.com/us/products/239627/) — identity, NASDAQ listing, inception, benchmark, current NAV/YTD, expense ratio and risk fields
- [iShares SCZ product performance table](https://www.ishares.com/ch/professionals/en/products/239627/ishares-msci-eafe-smallcap-etf?switchLocale=Y) — official 2016-2025 calendar return rows
- [Official SCZ fact sheet](https://www.ishares.com/us/literature/fact-sheet/scz-ishares-msci-eafe-small-cap-etf-fund-fact-sheet-en-us.pdf) — 2021-2025 NAV rows, return basis and fund characteristics as of 30 Jun 2026
- [SCZ summary prospectus](https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-eafe-small-cap-etf-7-31.pdf) — objective, fees and risk disclosures
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- Cached S&P 500 TR references: [2016-2019](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [2018-2022](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), [2021](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/), [2022-2025](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/)
- ETF source batch: [[ETF_performance_sources_2026-08-17]] | [[ETF Performance Index]]
