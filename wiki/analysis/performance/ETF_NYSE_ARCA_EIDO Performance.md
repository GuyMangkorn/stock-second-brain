---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:EIDO
ticker: EIDO
exchange: NYSE Arca
fund: iShares MSCI Indonesia ETF
tracked_index: MSCI Indonesia IMI 25/50 Index (USD) (Net)
benchmark: S&P 500 Total Return
updated: 2026-07-26
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-07-23
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/EIDO
  - geography/Indonesia
---

# EIDO Performance

> Navigation: [[ETF Region Index]] → [[Indonesia ETF]] → [[ETF Performance Index]]

## Bottom line

EIDO เป็น passive/index-tracking Indonesia equity ETF ที่ใช้ representative sampling เพื่อติดตาม MSCI Indonesia IMI 25/50 Index. Official rolling 10-year NAV Total Return สำหรับ `2016-06-30` ถึง `2026-06-30` คือ cumulative `-40.80%` / CAGR `-5.11%` (`10.00` elapsed years). Annual NAV TR ครบ 10 calendar years `2016-2025` compound เป็น `11.70%` / CAGR `1.11%`. Current issuer NAV TR YTD ล่าสุดคือ `-31.36%` ณ `2026-07-23`; standardized month-end YTD คือ `-38.53%` ณ `2026-06-30`.

## Performance check

- entity_key: `NYSE Arca:EIDO`
- Inception: `2010-05-05`
- Metric: NAV Total Return including reinvested distributions and fund expenses
- Tracked index: `MSCI Indonesia IMI 25/50 Index (USD) (Net)`; before `2019-05-29`, historical index data reflects the MSCI Indonesia Investable Market Index (Net).
- Type gate: iShares identifies EIDO as an equity ETF; the prospectus says the fund uses an indexing approach, representative sampling, and generally invests at least 80% in index securities or substantially identical instruments.
- Expense ratio: `0.59%`.
- Official rolling 10-year window: start date `2016-06-30`; end date `2026-06-30`; actual years `10.00`; start TR value `100.00` normalized; end TR value `59.20` normalized from official cumulative `-40.80%`; official CAGR `-5.11%`.
- Official complete-calendar window: `2016-12-31` to `2025-12-31`; actual years `10.00`; normalized start/end TR `100.00 → 111.70` from official annual rows; CAGR `1.11%` calculated from those rows.
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark, not the issuer benchmark).

| Year | EIDO NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 16.83% | 11.96% |
| 2017 | 18.43% | 21.83% |
| 2018 | -10.58% | -4.38% |
| 2019 | 5.01% | 31.49% |
| 2020 | -8.09% | 18.40% |
| 2021 | 0.87% | 28.71% |
| 2022 | -0.43% | -18.11% |
| 2023 | 2.09% | 26.29% |
| 2024 | -11.41% | 25.02% |
| 2025 | 2.98% | 17.88% |

Official EIDO NAV rows for `2016-2024` come from the December 30, 2025 SEC summary prospectus calendar-year chart; the `2025` row comes from the June 30, 2026 iShares fact sheet. S&P 500 rows reuse the cached USD Total Return convention as of `2025-12-31`; 2026 is not included because the cached calendar-year series is incomplete.

## Window calculations

- EIDO official rolling `2016-06-30` to `2026-06-30`: cumulative `-40.80%`; normalized `100.00 → 59.20`; CAGR `-5.11%`.
- EIDO complete-calendar `2016-2025`: cumulative `11.70%`; CAGR `1.11%`; positive / negative years `6 / 4`; best year `2017 +18.43%`; worst year `2018 -10.58%`.
- EIDO common `2021-2025`: cumulative `-6.46%`; CAGR `-1.33%`; S&P 500 cumulative `96.17%`; CAGR `14.43%`; EIDO trails by approximately `15.75 pp` CAGR.
- S&P 500 reference `2016-2025`: cumulative `298.33%`; CAGR `14.82%`.
- Current NAV TR YTD: `-31.36%` as of `2026-07-23` from the current iShares product snapshot. The standardized June month-end table reports `-38.53%` as of `2026-06-30`; the two observations use different as-of dates and are retained separately.

## Risk read-through

EIDO เป็นกองทุน non-diversified ที่มี Indonesia single-country exposure; sector หลักคือ financials, materials, energy และ communication. ความเสี่ยงหลักคือ emerging-market liquidity, currency, political/regulatory and repatriation risk, country concentration, financials/materials concentration, and tracking error. Official 3-year standard deviation คือ `20.55%` ณ `2026-06-30`. Daily NAV history ที่ยืนยันได้สำหรับ max drawdown และ recovery: `ไม่พบข้อมูลที่ยืนยันได้` ใน lean capture.

## Sources

- [iShares official EIDO product and performance page](https://www.ishares.com/us/products/239661/ishares-msci-indonesia-etf) — current NAV/YTD, exchange, benchmark, inception, fees, rolling and calendar performance; current snapshot through `2026-07-24` / performance through `2026-06-30`.
- [iShares EIDO June 2026 fact sheet](https://www.ishares.com/us/literature/fact-sheet/eido-ishares-msci-indonesia-etf-fund-fact-sheet-en-us.pdf) — official 2021-2025 calendar NAV rows, 10-year NAV TR and current fund facts; as of `2026-06-30`.
- [iShares EIDO summary prospectus](https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-indonesia-etf-8-31.pdf) — NYSE Arca listing, indexing/representative sampling strategy, 80% policy, risks and 2016-2024 calendar NAV chart; dated `2025-12-30`.
- [Official S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common USD Total Return reference.
- ETF source batch: [[ETF_performance_sources_2026-07-24]] | [[ETF Performance Index]]
