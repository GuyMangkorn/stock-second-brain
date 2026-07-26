---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:KURE
ticker: KURE
exchange: NYSE Arca
fund: KraneShares MSCI All China Health Care Index ETF
tracked_index: MSCI China All Shares Health Care 10/40 Index (USD)
benchmark: S&P 500 Total Return
updated: 2026-07-26
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/KURE
  - geography/China
---

# KURE Performance

> Navigation: [[ETF Region Index]] → [[China ETF]] → [[ETF Performance Index]]

## Bottom line

KURE เป็น passive/index-tracking equity ETF ที่ติดตาม `MSCI China All Shares
Health Care 10/40 Index (USD)` และลงทุนในบริษัท healthcare จีนที่จดทะเบียนใน
Mainland China, Hong Kong และสหรัฐฯ. กองทุนเริ่มเมื่อ `2018-01-31` จึงยังไม่มี
`10-year NAV TR` หรือ 10 complete calendar years.

KraneShares รายงาน official Fund NAV Total Return แบบ cumulative ตั้งแต่เริ่มกองทุน
ที่ `-23.43%` ถึง `2026-06-30` และรายงานแบบ annualized ที่ `-3.12%`. Current official
NAV TR YTD คือ `-8.80%` ถึง `2026-06-30`; NAV รายวันล่าสุดในหน้า issuer คือ
`US$17.53` ณ `2026-07-23`.

## Performance check

- entity_key: `NYSE Arca:KURE`
- Inception: `2018-01-31`
- Structure: passive/index-tracking equity ETF; the prospectus requires at least
  80% of net assets in instruments in the underlying index or similar instruments
- Tracked index: `MSCI China All Shares Health Care 10/40 Index (USD)`
- Metric: official Fund NAV Total Return; fund expenses are reflected in NAV and
  official total returns assume reinvestment of dividends and distributions
- Expense ratio: gross `0.79%`; net after waiver `0.65%` in the reviewed official
  materials
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference,
  not the ETF's tracked index)
- 10-year NAV TR: `unavailable`; the available window is `8.410678` years and
  does not contain 10 complete calendar years

### Available-period NAV TR

KraneShares reports the available since-inception return through `2026-06-30`.
Raw issuer NAV index endpoints are not disclosed, so the start and end values
below are normalized values derived from the official cumulative return.

| Window | Start date | End date | Start TR value | End TR value | Actual years | Cumulative NAV TR | CAGR |
|---|---|---|---:|---:|---:|---:|---:|
| Available since inception | 2018-01-31 | 2026-06-30 | 100.00 (normalized) | 76.57 (official cumulative, normalized) | 8.410678 | -23.43% (official) | -3.12% (official; derived -3.1243%) |

Calculation: `100 × (1 - 0.2343) = 76.57`; derived CAGR is
`(76.57 / 100)^(1 / 8.410678) - 1 = -3.1243%`, which rounds to the issuer's
reported `-3.12%`. This is available-period performance, not 10-year performance.

### Annual NAV TR and S&P 500 Total Return

The current official KraneShares performance page reports cumulative and
annualized windows but does not disclose exact calendar-year Fund NAV TR rows in
the reviewed text capture. The SEC summary prospectus contains a calendar-return
bar-chart image, but exact row values were not extracted or reconstructed. The
Fund column therefore remains `not disclosed`; no proxy or invented value is used.

| Year | KURE NAV TR | S&P 500 TR |
|---|---:|---:|
| 2018 | not disclosed (partial inception year) | -4.38% |
| 2019 | not disclosed | 31.49% |
| 2020 | not disclosed | 18.40% |
| 2021 | not disclosed | 28.71% |
| 2022 | not disclosed | -18.11% |
| 2023 | not disclosed | 26.29% |
| 2024 | not disclosed | 25.02% |
| 2025 | not disclosed | 17.88% |
| 2026 YTD | -8.80% as of 2026-06-30 | not comparable; current YTD not cached |

The cached S&P 500 USD Total Return rows for complete calendar years `2018-2025`
compound to `192.03%` / `14.33%` CAGR. This is a reference comparison rather
than an exact same-start/same-end comparison because KURE's official available
period starts on `2018-01-31` and ends on `2026-06-30`; the exact S&P 500 TR for
that same interval is `not disclosed` in the reviewed capture.

## Up years / Down years

- Up years / Down years: `not disclosed`; official calendar-year Fund NAV TR rows
  are not available in the reviewed issuer capture
- Best / worst year: `not disclosed`
- Official cumulative since inception: `-23.43%` through `2026-06-30`
- Official annualized since inception: `-3.12%` through `2026-06-30`
- Official rolling windows: 1Y `-3.15%`, 3Y `-2.80%`, and 5Y `-16.07%`, all as of
  `2026-06-30`

## Risk read-through

KURE เป็นกองทุน China healthcare แบบ sector-concentrated และ non-diversified ตาม
prospectus จึงมีความเสี่ยงจาก healthcare regulation, drug-development outcomes,
China/Hong Kong market structure, country and currency risk, liquidity, valuation
และความผันผวนของ biotechnology/pharmaceutical holdings. Daily NAV TR drawdown,
recovery dates และ exact calendar-year NAV rows: `ไม่พบข้อมูลที่ยืนยันได้` จาก
official capture นี้.

## Sources

- [Official KraneShares KURE product and performance page](https://kraneshares.com/etf/kure/) — identity, primary exchange, inception, index, expense ratio, NAV, performance windows, current YTD, distributions and as-of dates
- [Official KraneShares KURE factsheet](https://kraneshares.com/resources/factsheet/kure_factsheet.pdf) — passive/index strategy, exchange, ISIN, inception, index and fee cross-check
- [SEC official KURE summary prospectus](https://www.sec.gov/Archives/edgar/data/1547576/000182912625005533/kraneshares_497k.htm) — objective, 80% index policy, fee structure, risks, return basis and calendar-return chart availability
- [Official S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached source-batch convention — common USD total-return reference
- ETF source batch: [[ETF_performance_sources_2026-07-24]] | [[ETF Performance Index]]
