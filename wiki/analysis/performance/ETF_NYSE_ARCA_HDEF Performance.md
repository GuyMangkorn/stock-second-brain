---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:HDEF
ticker: HDEF
exchange: NYSE Arca
fund: Xtrackers MSCI EAFE High Dividend Yield Equity ETF
tracked_index: MSCI EAFE High Dividend Yield Index
benchmark: S&P 500 Total Return
updated: 2026-08-30
performance_as_of: 2025-12-31
rolling_10y_as_of: 2026-03-31
current_ytd_as_of: 2026-07-31
price_nav_as_of: not disclosed in reviewed official current capture
fund_facts_as_of: 2026-03-31
source_batch: raw/imports/ETF_performance_sources_2026-08-30.md
return_basis: NAV total return for official fields; secondary NAV-return series for rows marked *
return_currency: USD
management_mode: passive-index
tags:
  - analysis/etf-performance
  - ticker/HDEF
  - geography/International
---

# HDEF Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

HDEF เป็น passive high-dividend developed-markets ETF ที่ติดตาม MSCI EAFE High
Dividend Yield Index. ใน complete calendar window 2016-2025 มี 7 ปีบวก / 3 ปีลบ;
secondary NAV-return rows ให้ cumulative `119.89%*` หรือ rounded-input CAGR
`8.20%*`, เทียบ S&P 500 TR common reference `298.33%` / `14.82%`. ปีดีที่สุด
คือ 2025 ที่ `+33.00%*`; ปีที่แย่ที่สุดคือ 2018 ที่ `-13.30%*`. Current
secondary NAV-return YTD คือ `+12.20%*` ณ 31 ก.ค. 2026 ขณะที่ official index
YTD คือ `+13.05%` ในวันเดียวกัน.

## Performance check

- `entity_key: NYSE Arca:HDEF`
- Fund: `Xtrackers MSCI EAFE High Dividend Yield Equity ETF`; inception `2015-08-11`; listing `NYSE Arca`
- Identity note: ชื่อเก่าในบาง historical records คือ “Xtrackers MSCI EAFE High Dividend Yield Hedged Equity ETF”; DWS ระบุว่า effective `2018-02-13` fund เปลี่ยน underlying index จาก hedged เป็น unhedged MSCI EAFE High Dividend Yield Index
- Classification: supported passive/index-tracking equity ETF; DWS prospectus states full-replication indexing with representative sampling if needed
- Expense ratio: `0.09%` gross/net ตาม October 2025 summary prospectus
- Metric: `NAV Total Return` บนฐาน USD; official factsheet แยก NAV, market-price และ index returns และระบุว่า index returns เป็น gross of fees while fund return includes fund expenses
- Tracked index (issuer benchmark): `MSCI EAFE High Dividend Yield Index`
- Common benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference benchmark ไม่ใช่ tracked index ของ HDEF)
- Official rolling fields: NAV annualized `10-year 8.74%`, `5-year 11.05%`, `3-year 16.30%`, `1-year 23.43%`, since inception `7.36%`, all as of `2026-03-31`
- Current performance split: official DWS strategy factsheet reports index YTD `13.05%` and 1-year `20.96%` as of `2026-07-31`; secondary AAII reports HDEF NAV YTD `12.20%*` and 1-year `23.50%*` as of the same date
- Complete calendar window: `2016-2025` secondary NAV-return proxy compound `119.89%*` / rounded-input CAGR `8.20%*`; S&P 500 TR compound `298.33%` / CAGR `14.82%`
- Common window: `2021-2025` secondary NAV-return proxy compound `69.16%*` / rounded-input CAGR `11.09%*`; S&P 500 TR compound `96.17%` / CAGR `14.43%`; HDEF terminal wealth ต่ำกว่าประมาณ `13.77%` ใน window เดียวกัน
- Current official price/NAV: ใน reviewed official current capture ไม่พบ quote ที่ยืนยันได้ใหม่กว่าข้อมูล rolling/performance; จึงไม่แทนที่ด้วย secondary price

| Year | HDEF NAV-return proxy* | S&P 500 TR |
|---|---:|---:|
| 2016 | 11.60%* | 11.96% |
| 2017 | 9.80%* | 21.83% |
| 2018 | -13.30%* | -4.38% |
| 2019 | 24.60%* | 31.49% |
| 2020 | -1.80%* | 18.40% |
| 2021 | 6.90%* | 28.71% |
| 2022 | -2.70%* | -18.11% |
| 2023 | 18.60%* | 26.29% |
| 2024 | 3.10%* | 25.02% |
| 2025 | 33.00%* | 17.88% |

## Up years / Down years

- Up years / Down years: `7 / 3` ใน 2016-2025
- Best proxy year: 2025, `+33.00%*`
- Least positive proxy year: 2024, `+3.10%*`
- Worst proxy year: 2018, `-13.30%*`
- Least bad down proxy year: 2020, `-1.80%*`
- 2016-2025 cumulative/CAGR: HDEF `119.89%*` / `8.20%*`; S&P 500 TR
  `298.33%` / `14.82%`
- 2021-2025 cumulative/CAGR: HDEF `69.16%*` / `11.09%*`; S&P 500 TR
  `96.17%` / `14.43%`
- Current HDEF NAV-return YTD: `+12.20%*` ณ 31 ก.ค. 2026; official index YTD
  ใน DWS strategy factsheet คือ `+13.05%`

## Risk read-through

Official DWS factsheet ณ 31 มี.ค. 2026 รายงาน fund net assets `US$2.269B`,
holdings `123`, SEC 30-day yield `2.76%`, beta `0.77` และ expense ratio `0.09%`.
Strategy factsheet ณ 31 ก.ค. 2026 แสดง index/factor snapshot ที่มี high-dividend
tilt; index sector weights นำโดย financials `28.27%`, consumer staples `19.40%`,
health care `16.54%` และ energy `11.45%`, ส่วน country weights นำโดย Switzerland
`19.97%`, United Kingdom `18.11%`, France `12.99%` และ Germany `9.36%`.

ความเสี่ยงหลักคือ dividend/value-factor concentration, financials/energy,
country concentration, FX, dividend sustainability, non-diversified exposure,
tracking difference และ premium/discount/liquidity. DWS ระบุว่า index excludes
REITs และคัดกรอง yield, quality, payout, dividend growth และ negative price
momentum เพื่อหลีกเลี่ยง yield traps; filter เหล่านี้ไม่ได้รับประกัน dividend
หรือ downside protection. Official daily NAV history สำหรับ maximum drawdown,
recovery duration และ risk-adjusted persistence ยัง `ไม่พบข้อมูลที่ยืนยันได้`;
annual rows และ current YTD ที่มาจาก AAII จึงติด `*` และไม่ถูกเรียกว่า alpha.

## Sources

- [Xtrackers HDEF August 2026 strategy factsheet](https://etf.dws.com/download/asset/0d8d8fa0-7dfe-430d-9037-4b44cbeebfcb) — current product/index identity, passive strategy context, July 31, 2026 index returns, index characteristics, country/sector weights and methodology context
- [Xtrackers HDEF Q1 2026 fact sheet](https://etf.dws.com/en-us/AssetDownload/Index/b76d8a50-13ed-4913-a175-1b62170c1e92/HDEF-fact-sheet.pdf) — official ETF NAV/market-price/index rolling returns, assets, holdings, yield, beta and expenses as of 2026-03-31
- [Xtrackers HDEF summary prospectus](https://www.dws.com/US/EN/resources/Xtrackers-MSCI-EAFE-High-Dividend-Yield-Equity-ETF/HDEF_summary-prospectus.pdf) — passive indexing, full replication/sampling, 0.09% expenses, dividend/country/financial-sector/ETF risks and the 2018 hedged-to-unhedged index change
- [AAII HDEF performance](https://www.aaii.com/etf/ticker/HDEF) — secondary NAV-return annual rows, current YTD and trailing risk fields as of 2026-07-31; marked `*` and not treated as issuer calendar data
- [MSCI EAFE High Dividend Yield Index](https://www.msci.com/indexes/index/136066/msci-eafe-high-dividend-yield-index) — index identity and current index context
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached source references in `check-etf-performance` — common USD total-return benchmark for 2016-2025
- ETF source batch: [[ETF_performance_sources_2026-08-30]] | [[International ETF]] | [[ETF Performance Index]]
