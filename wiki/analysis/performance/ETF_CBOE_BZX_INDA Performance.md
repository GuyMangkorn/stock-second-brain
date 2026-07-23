---
type: etf-performance
instrument_type: ETF
entity_key: Cboe BZX:INDA
ticker: INDA
exchange: Cboe BZX
fund: iShares MSCI India ETF
tracked_index: MSCI India Index (Net)
benchmark: S&P 500 Total Return
updated: 2026-07-24
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-07-20
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/INDA
  - geography/India
---

# INDA Performance

> Navigation: [[ETF Region Index]] → [[India ETF]] → [[ETF Performance Index]]

## Bottom line

INDA เป็น iShares MSCI India ETF, canonical `Cboe BZX:INDA`, กองทุน passive,
index-tracking equity ETF ที่ติดตาม MSCI India Index (Net). Mandatory 10-year
audit ของ official iShares page ยืนยัน NAV Total Return cumulative `98.09%` และ
CAGR `7.07%` สำหรับ 2016-06-30 ถึง 2026-06-30 หรือ `10.00` elapsed years;
normalized TR คือ 100.00 เป็น 198.09. Current official NAV TR YTD คือ `-10.12%`
ณ 2026-07-20. Official calendar rows ที่เปิดเผยใน current capture มี 2021-2025;
annual rows 2016-2020 เป็น `not disclosed` และไม่มีการสร้าง proxy.

## Performance check

- entity_key: Cboe BZX:INDA
- Inception: 2012-02-02
- Metric: NAV Total Return including reinvested distributions and fund expenses; iShares' hypothetical-growth method reinvests dividends/capital gains and deducts fund expenses
- Tracked index (issuer benchmark): MSCI India Index (Net)
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark)
- 10-year NAV TR coverage: 2016-06-30 to 2026-06-30; actual years `10.00`
- 10-year NAV TR cumulative / CAGR: `98.09%` / `7.07%` (official iShares)
- Normalized NAV TR: start `100.00`; end `198.09` (official cumulative return; raw NAV endpoints are not disclosed)
- Available official calendar rows 2021-2025 compound to `45.55%` / CAGR `7.80%`; S&P 500 rows in the same window compound to `96.17%` / CAGR `14.43%`
- Coverage/source note: rolling 10-year summary is as of 2026-06-30; current YTD is as of 2026-07-20; 2016-2020 annual NAV rows are not disclosed in the reviewed official capture.

| Year | INDA NAV TR | MSCI India Index (Net) TR | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | not disclosed | not disclosed | 11.96% |
| 2017 | not disclosed | not disclosed | 21.83% |
| 2018 | not disclosed | not disclosed | -4.38% |
| 2019 | not disclosed | not disclosed | 31.49% |
| 2020 | not disclosed | not disclosed | 18.40% |
| 2021 | 22.41% | 26.23% | 28.71% |
| 2022 | -9.38% | -7.95% | -18.11% |
| 2023 | 17.49% | 20.81% | 26.29% |
| 2024 | 8.99% | 11.22% | 25.02% |
| 2025 | 2.47% | 2.62% | 17.88% |

S&P 500 เป็น common reference benchmark ไม่ใช่ issuer benchmark ของ INDA;
ตารางใช้ cached USD Total Return convention สำหรับ 2016-2025.

## Common-window comparison

- INDA 2021-2025 NAV TR CAGR: `7.80%`
- S&P 500 2021-2025 TR CAGR: `14.43%`
- INDA trails by approximately `6.63 pp` CAGR in the common calendar window.
- Up years / Down years in 2021-2025: `4 / 1`
- Best year: 2021, `22.41%`; worst year: 2022, `-9.38%`
- Current official NAV TR YTD: `-10.12%` as of 2026-07-20; latest NAV `US$48.65` as of 2026-07-20

## Risk read-through

INDA เป็น single-country India equity ETF; official data ณ 2026-07-20 มี 165
holdings, expense ratio `0.61%`, 3-year standard deviation `14.13%` และ 3-year
beta `0.43`. Sector exposureหลักคือ Financials `30.77%`, Consumer Discretionary
`12.04%`, Industrials `10.88%`, Materials `8.64%` และ Energy `8.37%`.
ความเสี่ยงหลักคือ India/country, valuation, currency, policy และ sector
concentration. Daily NAV history ที่ยืนยันได้เพียงพอสำหรับ max drawdown และ
recovery: `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- Official iShares product and performance page: https://www.ishares.com/us/products/239659/ishares-msci-india-etf
- Official iShares factsheet: https://www.ishares.com/us/literature/fact-sheet/inda-ishares-msci-india-etf-fund-fact-sheet-en-us.pdf
- Official S&P 500 index page: https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- ETF source batch: [[ETF_performance_sources_2026-07-24]] | [[ETF Performance Index]]
