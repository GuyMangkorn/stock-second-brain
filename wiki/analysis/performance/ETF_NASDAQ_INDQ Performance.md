---
type: etf-performance
instrument_type: ETF
entity_key: Nasdaq:INDQ
ticker: INDQ
exchange: Nasdaq
fund: Pacer ActiveAlpha India Quality ETF
tracked_index: ActiveAlpha India Quality Index
benchmark: MSCI India Index
updated: 2026-07-24
performance_as_of: 2026-03-31
current_ytd_as_of: not disclosed
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/INDQ
  - geography/India
---

# INDQ Performance

> Navigation: [[ETF Region Index]] → [[India ETF]] → [[ETF Performance Index]]

## Bottom line

INDQ เป็น passive, rules-based, index-tracking India equity ETF ที่ติดตาม
`ActiveAlpha India Quality Index` และใช้ quality, value และ momentum screens.
กองเริ่มมีผลดำเนินงานเมื่อ `2026-03-31` จึงยังไม่มี 10-year history และ
`10-year NAV TR unavailable`. Official Pacer performance table และ factsheet
ที่ตรวจสอบได้ยังแสดง NAV TR เป็น `N/A`; จึงยังไม่สามารถเปิดเผย available-period
NAV TR, CAGR หรือ current YTD ที่ยืนยันได้ และไม่สร้าง proxy.

## Performance check

- `entity_key`: `Nasdaq:INDQ`
- Inception: `2026-03-31`
- Expense ratio: `0.88%`
- Metric: NAV Total Return; Pacer states that NAV returns assume dividends and capital-gain distributions are reinvested.
- Tracked index: `ActiveAlpha India Quality Index`
- Issuer benchmark: `MSCI India Index`
- 10-year NAV TR: unavailable because inception is `2026-03-31`.
- Available-period NAV TR: `not disclosed` in the official Pacer page/factsheet reviewed; the table is explicitly `N/A`.
- Current YTD: `not disclosed`; the reviewed official performance snapshot is dated `2026-03-31` and does not provide a numeric YTD return.
- Market-price return is not substituted for NAV Total Return.

### Available-period coverage

| Start date | End date | Actual years | Start TR value | End TR value | Available-period NAV TR | CAGR |
|---|---|---:|---:|---:|---:|---:|
| 2026-03-31 | not disclosed | not calculable | not disclosed | not disclosed | not disclosed; official table shows N/A | not calculable |

`10-year NAV TR unavailable` is stated directly because the fund has less than
10 years of history. The official source does not disclose a numeric endpoint
for the short available period, so no return is inferred from the quoted NAV.

### Annual NAV TR vs S&P 500 TR

The table preserves the requested comparison structure. INDQ was not in
existence during 2016-2025, and the official 2026 NAV TR/YTD field is `N/A`;
therefore no ETF return is filled. S&P 500 rows for complete calendar years
reuse the cached USD Total Return convention recorded in the dated source batch.

| Year | INDQ NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | not applicable; before inception | 11.96% |
| 2017 | not applicable; before inception | 21.83% |
| 2018 | not applicable; before inception | -4.38% |
| 2019 | not applicable; before inception | 31.49% |
| 2020 | not applicable; before inception | 18.40% |
| 2021 | not applicable; before inception | 28.71% |
| 2022 | not applicable; before inception | -18.11% |
| 2023 | not applicable; before inception | 26.29% |
| 2024 | not applicable; before inception | 25.02% |
| 2025 | not applicable; before inception | 17.88% |
| 2026 YTD | not disclosed; official field N/A | not comparable; current-year S&P row not cached |

## Up years / Down years

- Up years / Down years: not disclosed.
- Best / worst year: not disclosed; no numeric annual NAV TR rows are available.
- Available-period cumulative return / CAGR: `not disclosed` / `not calculable`.
- 10-year NAV TR: unavailable because the fund's inception is `2026-03-31`.

## Risk read-through

INDQ มีความเสี่ยงจาก India single-country exposure, emerging-market FX,
factor concentration และ small-/mid-cap liquidity. Strategy เป็น rules-based
แต่ไม่ใช่ market-cap broad index: ActiveAlpha คัดเลือกประมาณ 20-30 บริษัทจาก
universe ของ Nifty 500 และ Nifty Microcap 250 ด้วย composite quality, value และ
momentum score และ rebalance/reconstitute รายไตรมาส. Because official NAV TR
ยังเป็น `N/A`, ยังประเมิน tracking, drawdown, recovery หรือ realized factor
behavior จากผลตอบแทนจริงไม่ได้.

## Sources

- [Official Pacer INDQ product/performance page](https://www.paceretfs.com/products/indq)
- [Official Pacer INDQ factsheet](https://www.paceretfs.com/media/indq.pdf)
- [Official Pacer INDQ documents](https://docs.paceretfs.com/indq)
- [SEC INDQ statement of additional information](https://www.sec.gov/Archives/edgar/data/1616668/000089418926007588/paceractivealphaindiaquali.htm)
- [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/); complete-year rows use the cached convention documented in [[ETF_performance_sources_2026-07-24]].
