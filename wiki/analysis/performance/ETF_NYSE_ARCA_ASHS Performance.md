---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:ASHS
ticker: ASHS
exchange: NYSE Arca
fund: Xtrackers Harvest CSI 500 China A-Shares Small Cap ETF
tracked_index: CSI 500 Index
benchmark: S&P 500 Total Return
updated: 2026-07-24
performance_as_of: 2026-03-31
current_ytd_as_of: 2026-03-31
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/ASHS
  - geography/China
---

# ASHS Performance

> Navigation: [[ETF Region Index]] → [[China ETF]] → [[ETF Performance Index]]

## Bottom line

ASHS เป็น passive/index-tracking China A-share small-cap equity ETF ที่ติดตาม CSI 500 Index. Official rolling 10-year NAV Total Return CAGR คือ `1.96%` สำหรับ `2016-03-31` ถึง `2026-03-31` (`10.00` elapsed years); raw start/end TR values และ raw cumulative return ไม่ได้เปิดเผย. Annual NAV TR rows `2016-2025` ไม่ได้เปิดเผยใน official capture จึงไม่คำนวณ CAGR จาก annual rows และไม่จัดอันดับ best/worst. Latest official NAV TR YTD คือ `3.36%` ณ `2026-03-31`; ค่า 2026-06-30 ไม่พบใน official source ที่ตรวจ.

## Performance check

- entity_key: `NYSE Arca:ASHS`
- Inception: `2014-05-20`
- Metric: NAV Total Return including reinvested distributions and fund expenses; DWS distinguishes ETF NAV returns from market-price returns, while index returns are gross of fees
- Tracked index: CSI 500 Index; 500 predominantly small-cap companies in the China A-share market listed on Shanghai and Shenzhen exchanges
- Official 10-year window: start date `2016-03-31`; end date `2026-03-31`; actual years `10.00`; start TR value `not disclosed`; end TR value `not disclosed`; official CAGR `1.96%`
- Implied cumulative return from the official CAGR is approximately `21.42%`; this is a shown calculation, not a substitute for undisclosed raw endpoints
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark, not the issuer benchmark)
- Current NAV TR YTD: `3.36%` as of `2026-03-31`; current `2026-06-30` NAV TR YTD: `not disclosed` in the reviewed official source capture

| Year | ASHS NAV TR | CSI 500 Index TR | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | not disclosed | not disclosed | 11.96% |
| 2017 | not disclosed | not disclosed | 21.83% |
| 2018 | not disclosed | not disclosed | -4.38% |
| 2019 | not disclosed | not disclosed | 31.49% |
| 2020 | not disclosed | not disclosed | 18.40% |
| 2021 | not disclosed | not disclosed | 28.71% |
| 2022 | not disclosed | not disclosed | -18.11% |
| 2023 | not disclosed | not disclosed | 26.29% |
| 2024 | not disclosed | not disclosed | 25.02% |
| 2025 | not disclosed | not disclosed | 17.88% |

DWS's Q1 2026 factsheet discloses standardized rolling periods but not readable annual NAV/index rows for `2016-2025`; the 2025 annual report provides a growth-of-$10,000 chart rather than a complete annual return table. No chart-derived proxy or third-party annual series is substituted. S&P 500 rows reuse the cached USD Total Return convention for complete calendar years `2016-2025`.

## Window calculations

- Official rolling 10-year ASHS NAV TR: CAGR `1.96%`; implied cumulative from CAGR `21.42%` (raw cumulative and raw endpoints not disclosed)
- 2016-2025 ASHS NAV TR and 2021-2025 ASHS NAV TR: `not disclosed`; no CAGR or spread is calculated from missing annual rows
- S&P 500 reference: 2016-2025 cumulative `298.33%` / CAGR `14.82%`; 2021-2025 cumulative `96.17%` / CAGR `14.43%`
- Up years / down years, best/worst calendar year and exact common-window spread: `not disclosed`
- Latest official NAV TR YTD: `3.36%` as of `2026-03-31`; 2026-06-30 value is `not disclosed`

## Risk read-through

ASHS ลงทุนโดยตรงใน China A-shares ผ่าน Stock Connect และ/หรือ QFI access, มี 497 holdings และ net assets ประมาณ `$38.3m` ณ `2026-03-31`; gross/net expense ratio `0.65%`. ความเสี่ยงหลักคือ China policy/geopolitical risk, A-share access/custody/tax, small-cap liquidity, sector concentration และ CNY/USD. Daily NAV history ที่ยืนยันได้สำหรับ max drawdown และ recovery: `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- Official Xtrackers ASHS Q1 2026 factsheet: https://etf.dws.com/download/asset/1bfed1b5-c933-4199-bdcc-30b0ed651740
- Official Xtrackers ASHS product finder: https://etf.dws.com/en-us/etf-products/
- Official Xtrackers ASHS summary prospectus (October 1, 2025): https://etf.dws.com/download/asset/7a928aa7-d2cc-490b-a3de-fb6144afc0cb
- Official Xtrackers ASHS annual shareholder report: https://etf.dws.com/download/asset/cd4f449d-b77e-49df-8486-46f48efe43cc
- SEC ASHS summary prospectus cross-check (October 1, 2024): https://www.sec.gov/Archives/edgar/data/1503123/000008805324000976/k100124ashs.htm
- Official S&P 500 index page: https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- ETF source batch: [[ETF_performance_sources_2026-07-24]] | [[ETF Performance Index]]
