---
type: etf-performance
instrument_type: ETF
entity_key: NASDAQ:CXSE
ticker: CXSE
exchange: NASDAQ
fund: WisdomTree China ex-State-Owned Enterprises Fund
tracked_index: WisdomTree China ex-State-Owned Enterprises Index (CHXSOE)
benchmark: S&P 500 Total Return
updated: 2026-07-24
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/CXSE
  - geography/China
---

# CXSE Performance

> Navigation: [[ETF Region Index]] → [[China ETF]] → [[ETF Performance Index]]

## Bottom line

CXSE เป็น passive/index-tracking China equity ETF ของ WisdomTree ที่ติดตาม
WisdomTree China ex-State-Owned Enterprises Index. Official issuer performance
ยืนยัน rolling 10-year NAV Total Return CAGR `6.85%` สำหรับ `2016-06-30` ถึง
`2026-06-30` หรือ `10.00` elapsed years; raw start/end TR values ไม่ได้เปิดเผย.
Official calendar NAV TR rows `2016-2025` compound เป็น `82.98%` / CAGR `6.23%`.
Current standardized NAV TR YTD คือ `-3.69%` ณ `2026-06-30`; YTD date-to-date
ถึง `2026-07-24` ไม่ได้เปิดเผยในแหล่ง official ที่ reviewed.

## Performance check

- entity_key: `NASDAQ:CXSE`
- Inception: `2012-09-19`
- Metric: NAV Total Return including reinvested distributions and fund expenses; WisdomTree states total returns use the daily 4:00pm NAV
- Passive/index-tracking gate: passed; the prospectus describes a passive indexing approach and representative sampling, with at least 80% of assets in index constituents or substantially identical securities
- Tracked index: WisdomTree China ex-State-Owned Enterprises Index; state-owned enterprises are defined as government ownership of more than 20%
- Expense ratio: `0.32%` as of `2026-07-22`
- Official 10-year window: start date `2016-06-30`; end date `2026-06-30`; actual years `10.00`; start TR value `not disclosed`; end TR value `not disclosed`; official CAGR `6.85%`
- Official calendar rows `2016-2025`: cumulative `82.98%` / CAGR `6.23%`; S&P 500 TR in the same window: cumulative `298.33%` / CAGR `14.82%`
- Common `2021-2025`: CXSE cumulative `-34.10%` / CAGR `-8.00%`; S&P 500 cumulative `96.17%` / CAGR `14.43%`; CXSE trails by approximately `22.43 pp` CAGR
- History caveat: the fund objective changed on `2015-07-01`; performance before that date reflects the former WisdomTree China Dividend ex-Financials Fund and its former index. The 2016-2025 table is post-change history.

| Year | CXSE NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | -1.20% | 11.96% |
| 2017 | 78.04% | 21.83% |
| 2018 | -27.95% | -4.38% |
| 2019 | 36.44% | 31.49% |
| 2020 | 60.58% | 18.40% |
| 2021 | -23.77% | 28.71% |
| 2022 | -28.89% | -18.11% |
| 2023 | -18.67% | 26.29% |
| 2024 | 9.59% | 25.02% |
| 2025 | 36.39% | 17.88% |

S&P 500 ใช้ cached USD Total Return convention สำหรับ complete calendar years
`2016-2025`; เป็น common reference benchmark ไม่ใช่ issuer benchmark ของ CXSE.
CXSE annual rows มาจาก official SEC prospectus charts for 2016-2024 และ
WisdomTree factsheet as of `2025-12-31` for 2025. ตัวเลขจาก chart เป็นค่าที่
issuer disclose และใช้ตามที่แสดงโดยไม่เติมค่าเอง.

## Window calculations

- Official rolling 10-year CXSE NAV TR: CAGR `6.85%`; raw cumulative and raw endpoints are not disclosed.
- 2016-2025 CXSE NAV TR: cumulative `82.98%` / CAGR `6.23%`; S&P 500 TR: cumulative `298.33%` / CAGR `14.82%`; CXSE trails by approximately `8.59 pp` CAGR.
- 2021-2025 CXSE NAV TR: cumulative `-34.10%` / CAGR `-8.00%`; S&P 500 TR: cumulative `96.17%` / CAGR `14.43%`; CXSE trails by approximately `22.43 pp` CAGR.
- Up years / down years in 2016-2025: `5 / 5`
- Best year: 2017, `78.04%`; worst year: 2022, `-28.89%`
- Current standardized NAV TR YTD: `-3.69%` as of `2026-06-30`; current date-to-date YTD as of `2026-07-24`: `ไม่พบข้อมูลที่ยืนยันได้`

## Risk read-through

CXSE มี China concentration `96.21%` และ Hong Kong `2.80%` ณ `2026-07-21`;
sector exposures หลักคือ Information Technology `26.79%`, Consumer
Discretionary `25.68%`, Communication Services `13.04%`, Industrials `11.47%`
และ Health Care `9.26%`. ความเสี่ยงหลักคือ single-country/emerging-market,
China A-shares ผ่าน Stock Connect, VIE, currency, regulation/geopolitics,
sector/issuer concentration และ NAV/market-price divergence. Daily NAV history
ที่ยืนยันได้เพียงพอสำหรับ max drawdown และ recovery: `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- Official WisdomTree CXSE product/performance page: https://www.wisdomtree.com/us/products/equity/cxse
- Official WisdomTree CXSE factsheet as of 2025-12-31: https://www.wisdomtree.com/nb-no/-/media/us-media-files/documents/resource-library/fund-fact-sheets/international-equity/wisdomtree-factsheet-cxse-1061.pdf
- SEC CXSE summary prospectus (August 1, 2024; 2016-2023 chart and strategy): https://www.sec.gov/Archives/edgar/data/1350487/000121465924013472/cxse73024497k.htm
- SEC CXSE summary prospectus (August 1, 2025; 2016-2024 chart): https://www.sec.gov/Archives/edgar/data/1350487/000121465925011285/cxse73125497k.htm
- Official WisdomTree China ex-State-Owned Enterprises Index page: https://www.wisdomtree.com/us/indexes/chxsoe
- Official S&P 500 index page: https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- ETF source batch: [[ETF_performance_sources_2026-07-24]] | [[ETF Performance Index]]
