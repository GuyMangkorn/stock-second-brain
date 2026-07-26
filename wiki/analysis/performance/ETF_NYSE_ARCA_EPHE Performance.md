---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:EPHE
ticker: EPHE
exchange: NYSE Arca
fund: iShares MSCI Philippines ETF
tracked_index: MSCI Philippines IMI 25/50 Index (USD) (Net)
benchmark: S&P 500 Total Return
updated: 2026-07-26
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-07-23
source_batch: raw/imports/ETF_performance_sources_2026-07-26.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/EPHE
  - geography/Philippines
---

# EPHE Performance

> Navigation: [[ETF Region Index]] → [[Philippines ETF]] → [[ETF Performance Index]]

## Bottom line

EPHE เป็น passive/index-tracking Philippines equity ETF ของ iShares ที่ติดตาม
`MSCI Philippines IMI 25/50 Index (USD) (Net)`. Official rolling 10-year NAV Total
Return (รวมการนำ distributions กลับไปลงทุนและ fund expenses) จาก 2026-06-30
ย้อนถึง 2016-06-30 มี cumulative return `-28.05%` และ CAGR `-3.24%` จากช่วงเวลา
จริง `10.00 elapsed years`. Current official NAV TR YTD ล่าสุดคือ `2.76%` ณ
2026-07-23. ตัวเลข 2021-2025 ที่เปิดเผยรวมกันเป็น cumulative `-15.95%` / CAGR
`-3.42%`; 2016-2020 annual NAV rows ไม่ได้เปิดเผยใน capture ที่ยืนยันได้.

## Performance check

- `entity_key`: `NYSE Arca:EPHE`
- Inception: `2010-09-28`
- Expense ratio: `0.59%`
- Metric: official NAV Total Return, including reinvested distributions and fund expenses
- Tracked index: `MSCI Philippines IMI 25/50 Index (USD) (Net)`
- Benchmark: S&P 500 Total Return, USD, dividends reinvested
- 10-year window: `2016-06-30` to `2026-06-30`; `10.00 elapsed years`
- Index-history caveat: iShares states that EPHE began tracking the current MSCI Philippines IMI 25/50 Index (Net) on `2020-12-01`; earlier history is not treated as perfectly like-for-like.
- Market-price return is not mixed with NAV Total Return.

### Rolling 10-year NAV TR

Raw NAV endpoints are `not disclosed` in the reviewed official capture. The
normalized endpoints below are a transparent representation of the issuer's
published cumulative return, not a proxy or a market-price series.

| Start date | End date | Actual years | Start TR value | End TR value | Cumulative NAV TR | CAGR |
|---|---|---:|---:|---:|---:|---:|
| 2016-06-30 | 2026-06-30 | 10.00 | 100.00 normalized | 71.95 derived | -28.05% official | -3.24% official |

- `71.95 = 100.00 × (1 - 28.05%)`.
- `CAGR = (71.95 / 100.00)^(1 / 10.00) - 1`; the displayed CAGR uses the issuer's rounded `-3.24%`.
- Official 5-year NAV TR: cumulative `-12.55%`, average annual `-2.65%`, through `2026-06-30`.
- Month-end NAV TR YTD: `0.06%` as of `2026-06-30`; latest current-page YTD: `2.76%` as of `2026-07-23`. These are separate as-of observations.

### Annual NAV TR vs S&P 500 TR

S&P 500 rows for complete calendar years 2016-2025 reuse the cached USD Total
Return convention recorded in the dated source batch. EPHE annual NAV rows for
2016-2020 are `not disclosed`; they are not reconstructed from a proxy.

| Year | EPHE NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | not disclosed | 11.96% |
| 2017 | not disclosed | 21.83% |
| 2018 | not disclosed | -4.38% |
| 2019 | not disclosed | 31.49% |
| 2020 | not disclosed | 18.40% |
| 2021 | -2.10% | 28.71% |
| 2022 | -14.37% | -18.11% |
| 2023 | -0.27% | 26.29% |
| 2024 | 1.08% | 25.02% |
| 2025 | -0.54% | 17.88% |
| 2026 YTD | 2.76% as of 2026-07-23 | not comparable; current-year S&P row not cached |

## Up years / Down years

- Disclosed 2021-2025 rows: up `1`, down `4`.
- Best disclosed year: `2024`, `1.08%`.
- Worst disclosed year: `2022`, `-14.37%`.
- Full 10-year best/worst ranking is not claimed because EPHE annual NAV rows for 2016-2020 are not disclosed.
- Available disclosed 2021-2025 period: cumulative `-15.95%`, CAGR `-3.42%`.

## Risk read-through

EPHE เป็นกอง single-country Philippines equity จึงมี country, FX, liquidity,
policy และ emerging-market risk สูงกว่ากอง broad developed-market. Official
exposure ณ 2026-07-17 กระจุกใน Industrials `41.02%`, Financials `20.03%`,
Utilities `11.80%` และ Real Estate `10.81%`; sector concentration นี้เป็น
ความเสี่ยงเพิ่มเติมจากตลาดประเทศเดียว. ผลตอบแทน rolling 10 ปีติดลบแม้กองมี
ประวัติยาวกว่า 10 ปี และไม่ควรใช้ current YTD ที่เป็น partial period แทน
ผลตอบแทน 10 ปี.

## Sources

- [Official iShares EPHE product/performance page](https://www.ishares.com/us/products/239675/ishares-msci-philippines-etf)
- [Official iShares EPHE data page](https://www.ishares.com/us/products/overview-v3-ishares-fund-data?portfolioId=239675&seoSlug=ishares-msci-philippines-etf)
- [Official EPHE factsheet](https://www.ishares.com/us/literature/fact-sheet/ephe-ishares-msci-philippines-etf-fund-fact-sheet-en-us.pdf)
- [Official EPHE prospectus material](https://www.ishares.com/uk/individual/en/literature/prospectus/p-ishares-trust-emerging-8-31-emea.pdf?siteEntryPassthrough=true&switchLocale=y)
- [Official EPHE annual shareholder report](https://www.blackrock.com/us/individual/literature/annual-report/ar-ephe-en.pdf)
 - [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/); complete-year rows use the cached convention documented in [[ETF_performance_sources_2026-07-24]].
