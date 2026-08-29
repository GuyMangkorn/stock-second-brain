---
type: etf-performance
instrument_type: ETF
entity_key: TSX:XEF
input_ticker: IXSAF
ticker: XEF
exchange: Toronto Stock Exchange
fund: iShares Core MSCI EAFE IMI Index ETF
tracked_index: MSCI EAFE Investable Market Index (CAD)
benchmark: S&P 500 Total Return
management_mode: passive-index
implementation: index-replicating
updated: 2026-08-30
performance_as_of: 2026-07-31 (standardized) / 2026-08-26 (current YTD)
calendar_years_as_of: 2025-12-31
current_ytd_as_of: 2026-08-26
price_nav_as_of: 2026-08-27
fund_facts_as_of: 2026-08-27
source_batch: raw/imports/ETF_performance_sources_2026-08-30.md
return_basis: NAV total return; distributions reinvested; net of expenses
return_currency: CAD
tags:
  - analysis/etf-performance
  - ticker/IXSAF
  - ticker/XEF
  - geography/International
---

# IXSAF / XEF ETF Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

IXSAF เป็น OTC alias ของ official Canadian CAD share class `TSX:XEF` ของ iShares
Core MSCI EAFE IMI Index ETF, ISIN `CA46434T1057`; ไม่ใช้ข้อมูลของ USD class
`XEF.U` ปะปนกัน. กองทุนเป็น passive/index-replicating equity ETF ที่ติดตาม
`MSCI EAFE Investable Market Index (CAD)` และมี exposure แบบ all-cap ใน developed
markets นอกสหรัฐฯ และแคนาดา.

Official BlackRock product page รายงาน NAV Total Return YTD `16.10%` ณ
2026-08-26, NAV `CAD 52.46` และ price `CAD 52.59` ณ 2026-08-27. Standardized
issuer fields ณ 2026-07-31 รายงาน 10-year NAV TR average annual `9.95%`, 1-year
`25.51%`, 3-year `18.29%`, 5-year `11.29%` และ since inception `10.16%`.

Official calendar rows 2021-2025 ให้ NAV compound `61.12%` หรือ rounded-input
CAGR `10.01%`; management benchmark compound `61.31%` หรือ `10.04%`. S&P 500
Total Return common reference ให้ `96.17%` / `14.43%` ในช่วงเดียวกัน แต่เป็น USD
ขณะที่ XEF เป็น CAD จึงเป็น directional reference ที่ไม่ควรตีความเป็น
FX-adjusted relative performance.

## Fund and measurement

- Input card ticker: `IXSAF` OTC alias; official security: `TSX:XEF`, ISIN `CA46434T1057`; exchange `Toronto Stock Exchange`; class inception `2013-04-10`.
- Asset class: equity; official objective is long-term capital growth by replicating the MSCI EAFE Investable Market Index net of expenses.
- Management fee `0.20%`; MER `0.23%`; distribution frequency semi-annual. Net assets `CAD 23,819,021,597` and holdings `2,511` as of 2026-08-27.
- Primary metric: CAD NAV Total Return, with distributions reinvested and expenses deducted. Current official YTD is `+16.10%` as of 2026-08-26.
- 10-year NAV TR issuer average annual: `9.95%` as of 2026-07-31; raw rolling endpoints are not disclosed in the reviewed capture, so this remains an issuer-reported average annual field rather than an independently calculated CAGR.

## Annual performance

The official XEF product page exposes the 2021-2025 calendar rows in CAD. The S&P
500 column is the cached USD total-return common reference and is shown with an FX
warning; it is not the tracked index of XEF.

| Calendar year | XEF NAV TR (CAD) | MSCI EAFE IMI (CAD) | S&P 500 TR (USD reference) |
|---|---:|---:|---:|
| 2021 | 10.05% | 10.13% | 28.71% |
| 2022 | -9.27% | -9.39% | -18.11% |
| 2023 | 14.34% | 14.35% | 26.29% |
| 2024 | 12.58% | 12.94% | 25.02% |
| 2025 | 25.36% | 25.17% | 17.88% |

- XEF 2021-2025: cumulative `+61.12%`; rounded-input CAGR `10.01%`.
- MSCI EAFE IMI 2021-2025: cumulative `+61.31%`; rounded-input CAGR `10.04%`.
- S&P 500 TR 2021-2025: cumulative `+96.17%`; cached USD CAGR `14.43%`.
- Best XEF year: 2025, **+25.36%**. Worst XEF year: 2022, **-9.27%**. Up/down years: `4 / 1`.
- XEF was above the USD S&P reference in 2022 and 2025, but the currency mismatch makes the `2 / 5` arithmetic hit count non-attributable to fund implementation or manager skill.

Calculation from rounded official rows:
`1.1005 × 0.9073 × 1.1434 × 1.1258 × 1.2536 = 1.6112368`, so
`(1.6112368)^(1/5) - 1 = 10.01%`. The corresponding benchmark product is
`1.6131174`, or `10.04%` annualized. Against the cached S&P product `1.9616962`,
the relative-wealth difference is `-17.87%`, but this is not currency matched.

## Risk read-through

The fund provides broad developed ex-U.S./Canada exposure, but returns remain
sensitive to country, sector, foreign-currency, valuation, and smaller-company
liquidity effects. Official current snapshot reports P/E `19.11x`, P/B `2.24x`,
distribution yield `3.00%`, and 12-month trailing yield `2.29%` as of 2026-08-26/27.
Official standard deviation, beta, daily NAV maximum drawdown, and recovery series
were not verified in the reviewed sources, so they remain `ไม่พบข้อมูลที่ยืนยันได้`.

## Passive implementation read-through

- `management_mode`: `passive-index`
- `implementation`: `index-replicating`; the official objective is to replicate the MSCI EAFE Investable Market Index net of expenses.
- `tracked_index`: `MSCI EAFE Investable Market Index (CAD)`; this is the strategy-aligned benchmark, not the S&P 500 common reference.
- Tracking observation: 2021-2025 XEF compound `61.12%` versus official index `61.31%`; the small shortfall is consistent with fees and implementation effects, but no tracking-error statistic is inferred.
- `risk_evidence`: `not-verified` for daily NAV drawdown/recovery and risk-adjusted metrics.

## Sources

- [iShares XEF official product page](https://www.blackrock.com/ca/investors/en/products/251421/ishares-msci-eafe-imi-index-etf?switchLocale=Y) — official CAD class identity, objective, current NAV/YTD, 2021-2025 calendar rows, benchmark, assets, holdings, fees, and portfolio characteristics.
- [BlackRock Canada product list](https://www.blackrock.com/ca/investors/en/products/product-list?siteEntryPassthrough=true&switchLocale=Y) — standardized 10-year/1-year/3-year/5-year/inception NAV fields as of 2026-07-31.
- [XEF factsheet](https://www.blackrock.com/ca/individual/en/literature/fact-sheet/xef-ishares-core-msci-eafe-imi-index-etf-fund-fact-sheet-en-ca.pdf?siteEntryPassthrough=true&switchLocale=y) — official fund objective, fees, distribution structure, and fund facts.
- [Secondary IXSAF alias listing](https://www.zonebourse.com/cours/etf/ISHARES-CORE-MSCI-EAFE-IM-155279206/) — OTC alias and ISIN cross-check only; no performance values from this source are used.
- S&P 500 Total Return cached convention from the workflow — USD dividends-reinvested common reference for 2021-2025; not FX matched to XEF's CAD return.
- [[ETF_performance_sources_2026-08-30]] | [[ETF Performance Index]]
