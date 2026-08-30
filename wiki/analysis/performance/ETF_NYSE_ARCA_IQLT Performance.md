---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:IQLT
ticker: IQLT
exchange: NYSE Arca
fund: iShares MSCI Intl Quality Factor ETF
tracked_index: MSCI World ex USA Sector Neutral Quality Index (Net)
benchmark: MSCI World ex USA Sector Neutral Quality Index (Net)
management_mode: passive-index
implementation: index-replicating
updated: 2026-08-30
performance_as_of: 2025-12-31 (official calendar) / 2026-06-30 (official standardized)
calendar_years_as_of: 2025-12-31
current_ytd_as_of: 2026-08-27
price_nav_as_of: 2026-08-28
fund_facts_as_of: 2026-08-28
source_batch: raw/imports/ETF_performance_sources_2026-08-30.md
return_basis: NAV total return; dividends and distributions reinvested; net of expenses
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/IQLT
  - geography/International
---

# IQLT Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

IQLT เป็น passive factor ETF ของ iShares ที่ติดตาม MSCI World ex USA Sector
Neutral Quality Index โดยคัดหุ้น developed markets นอกสหรัฐฯ ตาม return on
equity, earnings variability และ debt-to-equity. Official calendar NAV TR ช่วง
2016-2025 สะสม `132.33%` หรือ rounded-input CAGR `8.80%`; มีปีบวก/ลบ `8 / 2`.
Official rolling 10-year NAV TR คือ `9.99%` ณ 2026-06-30 และ current NAV TR YTD
ล่าสุดที่ตรวจได้คือ `16.01%` ณ 2026-08-27. ผลตอบแทนระยะยาวใกล้ benchmark แต่
ยังมี tracking drag เล็กน้อยตามค่าใช้จ่ายและ implementation.

## Performance check

- `entity_key: NYSE Arca:IQLT`; fund `iShares MSCI Intl Quality Factor ETF`; inception `2015-01-13`; exchange `NYSE Arca`; asset class `equity`.
- Tracked index and strategy-aligned benchmark: `MSCI World ex USA Sector Neutral Quality Index (Net)`. The index targets developed-market large- and mid-cap stocks outside the U.S. with relatively higher quality characteristics.
- Metric: `NAV Total Return` in USD, including reinvested dividends/distributions and net of expenses. Market-price returns are kept separate.
- Expense ratio `0.30%` and management fee `0.30%`; other expenses `0.00%` in the current prospectus. Fund net assets were `US$14.23B`, NAV `US$51.65`, closing price `US$51.67`, and premium/discount `0.05%` as of 2026-08-28.
- Official rolling performance as of 2026-06-30: NAV TR 1-year `17.49%`, 3-year `14.58%`, 5-year `8.00%`, 10-year `9.99%`; benchmark `17.77%`, `14.65%`, `8.01%`, `10.07%` respectively.
- 10-year calendar window: `2015-12-31` to `2025-12-31`; rounded-input NAV TR CAGR `8.80%`; official issuer rolling 10-year NAV TR `9.99%` as of 2026-06-30. Calendar CAGR formula: `(End TR / Start TR)^(1 / Years) - 1`.
- Coverage note: official calendar rows are available for every year from 2016 through 2025. The official web page notes that small variances can result from rounding and that systematic fair-value timing can cause fund/benchmark divergence.

| Year / window | IQLT NAV TR | Tracked benchmark | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | 0.60% | 0.70% | 11.96% |
| 2017 | 24.10% | 24.50% | 21.83% |
| 2018 | -10.90% | -11.00% | -4.38% |
| 2019 | 27.80% | 28.20% | 31.49% |
| 2020 | 13.10% | 13.20% | 18.40% |
| 2021 | 12.80% | 12.90% | 28.71% |
| 2022 | -15.10% | -15.30% | -18.11% |
| 2023 | 18.50% | 18.80% | 26.29% |
| 2024 | 1.70% | 2.10% | 25.02% |
| 2025 | 25.20% | 25.10% | 17.88% |
| 2016-2025 cumulative | 132.33% | 134.96% | 298.33% |
| 2016-2025 CAGR | 8.80% | 8.92% | 14.82% |
| 2021-2025 cumulative | 44.50% | 45.10% | 96.17% |
| 2021-2025 CAGR | 7.64% | 7.73% | 14.43% |

**Up years / Down years — complete 2016-2025 window**

- Up years / Down years: `8 / 2`.
- Best: 2017, `+24.10%`.
- Least positive: 2024, `+1.70%`.
- Worst: 2022, `-15.10%`.
- Least bad down year: 2018, `-10.90%`.
- Current official NAV TR YTD: `+16.01%` as of 2026-08-27; the latest reviewed current-period page did not provide a same-date S&P 500 TR field, so no unsynchronized current cross-market comparison is inferred.

## Risk read-through

The official iShares snapshot reports 3-year equity beta `0.68` and standard
deviation `13.07%` as of 2026-07-31, with `301` holdings and P/E `20.48` as of
2026-08-20. These are issuer snapshot fields, not a substitute for a daily NAV
series. Compatible official daily NAV history sufficient to calculate maximum
drawdown, recovery duration, downside capture, or full tracking error was not
verified. Main risks are quality-factor cyclicality, concentration in selected
countries/sectors, foreign currency and developed-market risk, mid-cap volatility,
index reconstitution, systematic fair-value timing, tracking error, securities
lending, and ETF premium/discount/liquidity.

## Tracking / implementation read-through

- `management_mode`: `passive-index`; the fund seeks to track the underlying MSCI quality index, not to exercise discretionary stock selection.
- Official calendar benchmark-relative differences are `-0.10, -0.40, +0.10, -0.40, -0.10, -0.10, +0.20, -0.30, -0.40, +0.10 pp` for 2016-2025. The fund beat the index in `3/10` calendar years, while official rolling 10-year NAV TR was `0.08 pp` below benchmark at 2026-06-30.
- The official index page attributes possible fund/benchmark divergence in part to systematic fair-value methodology; the expense ratio and trading/portfolio implementation also create tracking drag.
- S&P 500 TR is a common cross-ETF reference only and is not the tracked index or evidence of active management.

## Sources

- [iShares IQLT product page](https://www.ishares.com/us/products/271540/ishares-msci-international-developed-quality-factor-etf) — official identity, exchange, inception, benchmark, current NAV/YTD, assets, holdings, price, premium/discount, rolling performance, calendar rows, and fees.
- [iShares IQLT summary prospectus](https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-edge-msci-intl-quality-factor-etf-7-31.pdf) — official objective, quality-factor variables, 0.30% expenses, tracking methodology and risk disclosures.
- [IQLT SEC summary prospectus](https://www.sec.gov/Archives/edgar/data/1100663/000119312525302124/d43812d497k.htm) — official NYSE Arca identity, objective, fee table, turnover, index and risk framework.
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached `check-etf-performance` references — common USD Total Return benchmark for complete 2016-2025 calendar years.
- [State Street SPY performance](https://www.ssga.com/us/en/individual/etfs/state-street-spdr-sp-500-etf-trust-spy) — official common-benchmark reference for synchronized month-end comparisons.
- [[ETF_performance_sources_2026-08-30]] | [[ETF Performance Index]]
