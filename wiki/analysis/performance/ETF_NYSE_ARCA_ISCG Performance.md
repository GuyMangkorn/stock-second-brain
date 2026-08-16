---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:ISCG
ticker: ISCG
exchange: NYSE Arca
fund: iShares Morningstar Small-Cap Growth ETF
tracked_index: Morningstar US Small Cap Broad Growth Extended Index
benchmark: S&P 500 Total Return
updated: 2026-08-16
performance_as_of: 2025-12-31
rolling_10y_as_of: 2026-06-30
current_ytd_as_of: 2026-08-13
price_nav_as_of: 2026-08-14
fund_facts_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-08-16.md
return_basis: NAV total return
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/ISCG
  - geography/United-States
---

# ISCG Performance

> Navigation: [[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]

## Bottom line

ISCG เป็น passive/index-tracking U.S. small-cap growth ETF ที่ติดตาม Morningstar
US Small Cap Broad Growth Extended Index. ใน complete calendar window 2016-2025
มี 7 ปีบวก / 3 ปีลบ; cumulative NAV Total Return ที่คำนวณจาก annual rows คือ
`165.20%` หรือ CAGR `10.24%`, เทียบ S&P 500 TR `298.33%` / `14.82%`.
ปีดีที่สุดคือ 2020 ที่ `+43.28%` และแย่ที่สุดคือ 2022 ที่ `-26.65%`. Current
official NAV TR YTD คือ `+19.39%` ณ 13 ส.ค. 2026.

## Performance check

- `entity_key: NYSE Arca:ISCG`
- Classification: supported passive/index-tracking equity ETF using
  representative sampling
- Inception: 28 มิ.ย. 2004; expense ratio `0.06%`
- Metric: `NAV Total Return` บนฐาน USD รวม reinvested dividends และ capital
  gains; fund expenses สะท้อนอยู่ในผลตอบแทนตาม issuer disclosure
- Tracked index (issuer benchmark): `Morningstar US Small Cap Broad Growth
  Extended Index`
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference
  benchmark ไม่ใช่ tracked index ของ ISCG)
- Official rolling 10-year NAV TR: cumulative `211.14%` / annualized `12.02%`
  ณ 30 มิ.ย. 2026; raw rolling endpoints ไม่ได้เปิดเผย
- Current NAV: `US$66.33` และ closing price `US$66.36` ณ 14 ส.ค. 2026;
  premium/discount `0.05%` ณ วันเดียวกัน
- Annual coverage: official 2016-2024 NAV rows from the iShares summary
  prospectus and official 2025 NAV row from the current iShares product page /
  factsheet. Rows use the published precision of each official source.

| Year | ISCG NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 9.48% | 11.96% |
| 2017 | 23.48% | 21.83% |
| 2018 | -5.79% | -4.38% |
| 2019 | 27.41% | 31.49% |
| 2020 | 43.28% | 18.40% |
| 2021 | -1.32% | 28.71% |
| 2022 | -26.65% | -18.11% |
| 2023 | 22.84% | 26.29% |
| 2024 | 13.44% | 25.02% |
| 2025 | 13.09% | 17.88% |

## Up years / Down years

- Up years / Down years: `7 / 3` ใน 2016-2025
- Best: 2020, `+43.28%`
- Least positive: 2016, `+9.48%`
- Worst: 2022, `-26.65%`
- Least bad down year: 2021, `-1.32%`
- 2016-2025 cumulative/CAGR: ISCG `165.20%` / `10.24%`; S&P 500 TR
  `298.33%` / `14.82%`
- 2021-2025 cumulative/CAGR: ISCG `14.07%` / `2.67%`; S&P 500 TR
  `96.17%` / `14.43%`
- Current ISCG NAV TR YTD: `+19.39%` ณ 13 ส.ค. 2026

## Risk read-through

ISCG มี small-cap และ growth-style risk เต็มรูปแบบ โดย representative sampling
อาจทำให้ผลตอบแทนต่างจาก index ได้. Official product page แสดง holdings `929` ณ
13 ส.ค. 2026, three-year standard deviation `18.69%` และ beta `1.24` ณ 31 ก.ค.
2026. Sector exposure ล่าสุดกระจุกใน Industrials `24.37%`, Information
Technology `22.67%` และ Health Care `17.55%` ณ 13 ส.ค. 2026; จึงมี
cyclicality, valuation, liquidity และ sector-concentration sensitivity.

Official summary prospectus ระบุ best quarter `+32.85%` ในไตรมาสสิ้นสุด 30 มิ.ย.
2020 และ worst quarter `-21.51%` ในไตรมาสสิ้นสุด 31 มี.ค. 2020. Official daily
NAV history ที่เพียงพอสำหรับ maximum drawdown และ recovery ยังไม่ถูกยืนยัน จึง
ไม่ใช้ตัวเลข secondary proxy ในหน้านี้.

## Sources

- [Official iShares ISCG product page](https://www.ishares.com/us/products/239587/ishares-morningstar-smallcap-growth-etf) — identity, current NAV/price, YTD, holdings, risk fields and current calendar rows
- [Official ISCG fact sheet](https://www.ishares.com/us/literature/fact-sheet/iscg-ishares-morningstar-small-cap-growth-etf-fund-fact-sheet-en-us.pdf) — 2021-2025 calendar NAV rows, return basis, rolling annualized return and fund facts as of 30 Jun 2026
- [Official iShares ISCG summary prospectus](https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-morningstar-small-cap-growth-etf-4-30.pdf) — 2016-2024 calendar NAV rows, representative-sampling method and risk disclosures
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- Cached S&P 500 TR references: [2016-2019](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [2018-2022](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), [2021](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/), [2022-2025](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/)
- ETF source batch: [[ETF_performance_sources_2026-08-16]] | [[ETF Performance Index]]
