---
type: etf-performance
instrument_type: ETF
entity_key: Cboe BZX:BBSC
ticker: BBSC
exchange: Cboe BZX
fund: JPMorgan BetaBuilders U.S. Small Cap Equity ETF
tracked_index: Morningstar US Small Cap Target Market Exposure Extended Index
benchmark: S&P 500 Total Return
updated: 2026-08-17
performance_as_of: 2025-12-31
calendar_years_as_of: 2025-12-31
current_ytd_as_of: 2026-06-30
fund_facts_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-08-17.md
return_basis: NAV total return
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/BBSC
  - geography/United-States
---

# BBSC Performance

> Navigation: [[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]

## Bottom line

BBSC เป็น passive/index-tracking U.S. small-cap equity ETF ของ JPMorgan ที่ติดตาม
Morningstar US Small Cap Target Market Exposure Extended Index. กองทุนเริ่มเมื่อ
16 พ.ย. 2020 จึงยังมีประวัติไม่ครบ 10 ปี ณ 30 มิ.ย. 2026. Official complete
calendar-year NAV Total Return 2021-2025 ให้ cumulative `38.35%` หรือ
rounded-input CAGR `6.71%`, เทียบกับ S&P 500 TR `96.17%` / `14.43%`. Current
official NAV TR YTD ล่าสุดคือ `+23.96%` ณ 30 มิ.ย. 2026.

## Performance check

- `entity_key: Cboe BZX:BBSC`; current primary exchange: Cboe BZX Exchange. เอกสาร SEC ระบุการย้าย listing จาก NYSE Arca ไป Cboe BZX มีผล 16 เม.ย. 2026
- Classification: supported passive/index-tracking U.S. small-cap equity ETF
- Inception: 16 พ.ย. 2020; total expense ratio `0.09%`
- Metric: `NAV Total Return` รวม dividends/capital gains ที่ reinvested และ fund expenses; currency USD
- Tracked index (issuer benchmark): `Morningstar US Small Cap Target Market Exposure Extended Index`
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference benchmark ไม่ใช่ tracked index ของ BBSC)
- 10-year NAV TR: `not applicable (<10y history)`; 2020 เป็น inception-year partial period และไม่ถูกนำไปคำนวณ complete-year CAGR
- 2021-2025 calendar NAV TR: cumulative `38.35%`; rounded-input CAGR `6.71%`
- S&P 500 cached 2021-2025: cumulative `96.17%`; rounded-input CAGR `14.43%`
- Current official fields ณ 30 มิ.ย. 2026: NAV TR YTD `+23.96%`, market-price return `+24.13%`, และ issuer benchmark `+24.11%`; current S&P YTD ไม่ได้อ้างว่าเป็นวันเดียวกัน
- Coverage/source note: official JPMorgan factsheet ให้ rows 2021-2025 และ current fields ณ 30 มิ.ย. 2026; S&P annual rows ใช้ cached USD Total Return convention as of 31 ธ.ค. 2025

| Year | BBSC NAV TR | S&P 500 TR |
|---|---:|---:|
| 2021 | 15.55% | 28.71% |
| 2022 | -19.71% | -18.11% |
| 2023 | 20.03% | 26.29% |
| 2024 | 12.37% | 25.02% |
| 2025 | 10.56% | 17.88% |

S&P 500 เป็น common reference benchmark ไม่ใช่ issuer benchmark ของ BBSC;
annual rows ใช้ cached USD Total Return convention และไม่ได้ผสมกับ market-price
return ของ BBSC.

## Up years / Down years

- Up years / Down years: `4 / 1` ใน complete calendar years 2021-2025
- Best: 2021, `+15.55%`
- Least positive: 2025, `+10.56%`
- Worst and least bad down year: 2022, `-19.71%`
- 2021-2025 cumulative/CAGR: BBSC `38.35%` / `6.71%`; S&P 500 TR `96.17%` / `14.43%`
- Current BBSC NAV TR YTD: `+23.96%` ณ 30 มิ.ย. 2026; market-price return `+24.13%` และ issuer benchmark `+24.11%` เป็นคนละ metric ที่รายงานใน factsheet เดียวกัน

## Risk read-through

BBSC มี U.S. small-cap, cyclicality, valuation และ liquidity sensitivity. กองทุนใช้
representative sampling เพื่อ track ดัชนี และ expense ratio `0.09%` ถูกสะท้อนใน
NAV Total Return. Current NAV TR ต่ำกว่า issuer benchmark `0.15 pp` และ market-price
return สูงกว่า NAV TR `0.17 pp` ณ 30 มิ.ย. 2026; เป็น observed spread ไม่ใช่ causal
attribution. Official daily NAV history ที่เพียงพอสำหรับคำนวณ maximum drawdown และ
recovery ยังไม่ถูกยืนยัน จึงไม่บันทึกตัวเลข proxy.

## Sources

- [JPMorgan BBSC product page](https://am.jpmorgan.com/us/en/asset-management/adv/products/jpmorgan-betabuilders-us-small-cap-equity-etf-etf-shares-46641q290) — identity, objective, tracked index and product context
- [JPMorgan BBSC fact sheet](https://am.jpmorgan.com/content/dam/jpm-am-aem/americas/us/en/literature/fact-sheet/etfs/FS-BBSC.PDF) — official 2021-2025 NAV rows, current NAV/market-price/benchmark fields, fee, inception and return basis; as of 30 Jun 2026
- [SEC BBSC summary prospectus](https://www.sec.gov/Archives/edgar/data/1485894/000119312526071799/d46741d497k.htm) — objective, index strategy, fees and passive structure
- [SEC exchange-transfer supplement](https://www.sec.gov/Archives/edgar/data/1485894/000119312526128970/d123344d497k.htm) — NYSE Arca to Cboe BZX transfer effective 16 Apr 2026
- [SEC Cboe BZX Form 8-A](https://www.sec.gov/Archives/edgar/data/1485894/000119312526152486/d134932d8a12b.htm) — current Cboe BZX registration cross-check
- [JPMorgan exchange-transfer release](https://am.jpmorgan.com/us/en/asset-management/per/about-us/media/press-releases/jp-morgan-transfer-14-etfs-from-current-exchanges/) — official listing-transfer context
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common benchmark definition
- Cached S&P 500 TR references: [2018-2022](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), [2021](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/), and [2022-2025](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/)
- ETF source batch: [[ETF_performance_sources_2026-08-17]] | [[ETF Performance Index]]
