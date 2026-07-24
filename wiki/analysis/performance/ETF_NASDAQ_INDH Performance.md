---
type: etf-performance
instrument_type: ETF
entity_key: Nasdaq:INDH
ticker: INDH
exchange: Nasdaq
fund: WisdomTree India Hedged Equity Fund
tracked_index: WisdomTree India Hedged Equity Index
benchmark: S&P 500 Total Return
updated: 2026-07-24
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/INDH
  - geography/India
---

# INDH Performance

> Navigation: [[ETF Region Index]] → [[India ETF]] → [[ETF Performance Index]]

## Bottom line

INDH เป็น passive/index-tracking India equity ETF ที่ติดตาม
`WisdomTree India Hedged Equity Index` และ hedge ความผันผวน USD/INR. Official
available-period NAV Total Return ตั้งแต่ inception `2024-05-09` ถึง `2026-06-30`
มี cumulative `1.84%` และ average annual return/CAGR `0.85%` จากช่วงเวลา
`2.141 elapsed years`; `10-year NAV TR unavailable`. Official current NAV TR
YTD คือ `-9.04%` ณ `2026-06-30`.

## Performance check

- `entity_key`: `Nasdaq:INDH`
- Inception: `2024-05-09`
- Net expense ratio: `0.64%` as of `2026-07-17`
- Metric: official NAV Total Return; WisdomTree states total returns are calculated using daily 4:00pm NAV and are separate from market-price returns.
- Tracked index: `WisdomTree India Hedged Equity Index`
- Issuer comparison index: `MSCI India Index (Local)`; common comparison below is S&P 500 Total Return.
- 10-year NAV TR: unavailable because inception is `2024-05-09`.
- Available-period window: `2024-05-09` to `2026-06-30`; `782 days / 2.141 elapsed years`.
- Market-price return is not mixed with NAV Total Return.

### Available-period NAV TR

Raw NAV endpoints are not disclosed as a time series. The normalized endpoints
below represent the issuer's published cumulative NAV return and are not a
market-price proxy.

| Start date | End date | Actual years | Start TR value | End TR value | Cumulative NAV TR | CAGR |
|---|---|---:|---:|---:|---:|---:|
| 2024-05-09 | 2026-06-30 | 2.141 | 100.00 normalized | 101.84 derived | 1.84% official | 0.85% official |

- `101.84 = 100.00 × (1 + 1.84%)`.
- `CAGR = (101.84 / 100.00)^(1 / 2.141043) - 1 = 0.85%`; the displayed annualized return agrees with WisdomTree's official since-inception average annual return.
- Current NAV TR YTD: `-9.04%` as of `2026-06-30`.
- One-year NAV TR: `-7.52%` through `2026-06-30`; 3-, 5- and 10-year fields are `N/A` because the fund is too new.

### Annual NAV TR vs S&P 500 TR

WisdomTree's reviewed official performance table discloses rolling/month-end
and since-inception returns but no complete calendar-year NAV rows for INDH.
Rows before inception are not applicable; 2024 is an incomplete inception year
and 2025 is not disclosed. S&P 500 rows reuse the cached USD Total Return
convention recorded in the dated source batch.

| Year | INDH NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | not applicable; before inception | 11.96% |
| 2017 | not applicable; before inception | 21.83% |
| 2018 | not applicable; before inception | -4.38% |
| 2019 | not applicable; before inception | 31.49% |
| 2020 | not applicable; before inception | 18.40% |
| 2021 | not applicable; before inception | 28.71% |
| 2022 | not applicable; before inception | -18.11% |
| 2023 | not applicable; before inception | 26.29% |
| 2024 | not disclosed; incomplete inception year | 25.02% |
| 2025 | not disclosed | 17.88% |
| 2026 YTD | -9.04% as of 2026-06-30 | not comparable; current-year S&P row not cached |

## Up years / Down years

- Complete calendar-year up/down count: not disclosed; no complete annual NAV rows were published in the reviewed official capture.
- Best / worst calendar year: not disclosed.
- Available-period cumulative return / CAGR: `1.84% official` / `0.85% official`.
- 10-year NAV TR: unavailable because the fund's inception is `2024-05-09`.

## Risk read-through

INDH มี India single-country, emerging-market, equity, sector, valuation และ
FX/hedge-cost risk. WisdomTree ระบุ aggregate hedge ratio `100.25%` ณ
2026-07-17; hedge ลดความผันผวน USD/INR แต่ไม่ได้ลบความเสี่ยงจากหุ้นอินเดีย
หรือค่าใช้จ่าย/ความคลาดเคลื่อนของ hedge. Portfolio ณ 2026-07-17 กระจุกใน
Financials `24.58%`, Consumer Discretionary `13.37%`, Energy `11.59%` และ
Information Technology `9.62%`. ประวัติสั้นและไม่ควรใช้ current YTD แทน
ผลตอบแทน 10 ปี.

## Sources

- [Official WisdomTree INDH product/performance page](https://www.wisdomtree.com/us/products/equity/indh)
- [Official WisdomTree INDH factsheet](https://www.wisdomtree.com/investments/-/media/us-media-files/documents/resource-library/fund-fact-sheets/international-equity/wisdomtree-factsheet-indh.pdf)
- [SEC INDH summary prospectus](https://www.sec.gov/Archives/edgar/data/1350487/000121465925011298/indh73125497k.htm)
- [WisdomTree India Hedged Equity Index](https://www.wisdomtree.com/indexes/wtieqh)
- [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/); complete-year rows use the cached convention documented in [[ETF_performance_sources_2026-07-24]].
