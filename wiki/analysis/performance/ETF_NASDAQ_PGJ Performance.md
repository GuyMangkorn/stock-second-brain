---
type: etf-performance
instrument_type: ETF
entity_key: NASDAQ:PGJ
ticker: PGJ
exchange: NASDAQ
fund: Invesco Golden Dragon China ETF
tracked_index: Nasdaq Golden Dragon China Index
benchmark: S&P 500 Total Return
updated: 2026-07-24
performance_as_of: 2025-12-31
current_ytd_as_of: not disclosed
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/PGJ
  - geography/China
---

# PGJ Performance

> Navigation: [[ETF Region Index]] → [[China ETF]] → [[ETF Performance Index]]

## Bottom line

PGJ เป็น passive/index-tracking China equity ETF ที่ติดตาม Nasdaq Golden Dragon China Index ซึ่งประกอบด้วยบริษัทที่จดทะเบียนในสหรัฐฯ และมีรายได้หลักจากจีน. Official rolling 10-year NAV Total Return CAGR คือ `0.35%` สำหรับ `2015-12-31` ถึง `2025-12-31` (`10.00` elapsed years); raw start/end TR values ไม่ได้เปิดเผย. Official calendar NAV TR rows `2016-2025` compound เป็น `3.50%` / CAGR `0.34%`. Current 2026 NAV TR YTD: `ไม่พบข้อมูลที่ยืนยันได้` ใน official capture ที่ตรวจ.

## Performance check

- entity_key: `NASDAQ:PGJ`
- Inception: `2004-12-09`
- Metric: NAV Total Return including reinvested distributions and fund expenses; Invesco reports NAV and market-price returns separately
- Tracked index: Nasdaq Golden Dragon China Index; U.S.-listed companies headquartered or incorporated in the People's Republic of China, rebalanced and reconstituted quarterly
- Official 10-year window: start date `2015-12-31`; end date `2025-12-31`; actual years `10.00`; start TR value `not disclosed`; end TR value `not disclosed`; official CAGR `0.35%`
- Implied cumulative return from the official CAGR is approximately `3.55%`; this is a shown calculation, not a substitute for undisclosed raw endpoints
- Official benchmark: FTSE China 50 Index (USD); benchmark rows are kept separate from the fund NAV TR metric
- Common reference benchmark: S&P 500 Total Return (USD, dividends reinvested; not the issuer benchmark)
- Current NAV TR YTD: `not disclosed`; the latest reviewed official standardized performance source is as of `2025-12-31`

| Year | PGJ NAV TR | Nasdaq Golden Dragon China Index TR | FTSE China 50 Index TR | S&P 500 TR |
|---|---:|---:|---:|---:|
| 2016 | -11.36% | -11.13% | 2.87% | 11.96% |
| 2017 | 59.97% | 60.51% | 35.99% | 21.83% |
| 2018 | -29.16% | -28.84% | -11.51% | -4.38% |
| 2019 | 31.91% | 32.42% | 14.89% | 31.49% |
| 2020 | 53.58% | 54.41% | 11.52% | 18.40% |
| 2021 | -42.76% | -42.60% | -19.82% | 28.71% |
| 2022 | -24.36% | -24.24% | -19.32% | -18.11% |
| 2023 | -2.45% | -2.72% | -12.66% | 26.29% |
| 2024 | 5.88% | 5.89% | 32.41% | 25.02% |
| 2025 | 13.73% | 13.25% | 29.51% | 17.88% |

Annual PGJ NAV/index/FTSE China 50 rows are from Invesco's official Q4 2025 report; S&P 500 rows reuse the cached USD Total Return convention for complete calendar years `2016-2025`.

## Window calculations

- Official rolling 10-year PGJ NAV TR: CAGR `0.35%`; implied cumulative from CAGR `3.55%` (raw cumulative and raw endpoints not disclosed)
- 2016-2025 PGJ NAV TR: cumulative `3.50%` / CAGR `0.34%`; S&P 500 TR: cumulative `298.33%` / CAGR `14.82%`; PGJ trails by approximately `14.48 pp` CAGR
- 2021-2025 PGJ NAV TR: cumulative `-49.14%` / CAGR `-12.65%`; S&P 500 TR: cumulative `96.17%` / CAGR `14.43%`; PGJ trails by approximately `27.08 pp` CAGR
- Up years / down years: `5 / 5`
- Best year: `2017`, `59.97%`; worst year: `2021`, `-42.76%`
- Current NAV TR YTD: `not disclosed`

## Risk read-through

PGJ มี 78 holdings ณ `2025-12-31`, expense ratio `0.70%` และเป็น non-diversified China/ADR-focused equity ETF. ความเสี่ยงหลักคือ China policy/geopolitical risk, ADR/VIE and U.S.-listing risk, country/sector concentration, emerging-market liquidity และ CNY/USD. Daily NAV history ที่ยืนยันได้สำหรับ max drawdown และ recovery: `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- Official Invesco PGJ product page: https://www.invesco.com/us/en/financial-products/etfs/invesco-golden-dragon-china-etf.html
- Official Invesco PGJ Q4 2025 report: https://www.invesco.com/us-rest/contentdetail?contentId=bc42fd05f0e21410VgnVCM100000c2f1bf0aRCRD&dnsName=us
- Official SEC PGJ filing cross-check: https://www.sec.gov/Archives/edgar/data/1209466/000120946625000313/edgar.htm
- Official S&P 500 index page: https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- ETF source batch: [[ETF_performance_sources_2026-07-24]] | [[ETF Performance Index]]
