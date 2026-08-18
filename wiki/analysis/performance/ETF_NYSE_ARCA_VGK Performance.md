---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:VGK
input_ticker: VGK
ticker: VGK
exchange: NYSE Arca
fund: Vanguard FTSE Europe ETF
tracked_index: FTSE Developed Europe All Cap Index
benchmark: S&P 500 Total Return
management_mode: passive-index-tracking
updated: 2026-08-18
performance_as_of: 2025-12-31
rolling_10y_as_of: 2026-06-30
current_ytd_as_of: 2026-07-20
price_nav_as_of: 2026-06-12
fund_facts_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-08-18.md
return_basis: NAV total return; dividends and capital gains distributions reinvested; net of expenses
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/VGK
  - geography/Europe
---

# VGK Performance

> Navigation: [[ETF Region Index]] → [[Europe ETF]] → [[ETF Performance Index]]

## Bottom line

`VGK` คือ Vanguard FTSE Europe ETF ที่จดทะเบียนบน NYSE Arca และเป็น
`passive-index` broad developed-Europe equity ETF ซึ่งติดตาม `FTSE Developed
Europe All Cap Index` ด้วย full replication. Official complete-calendar NAV rows
ปี 2016-2025 compound ได้ `130.81%` หรือ rounded-input CAGR `8.72%`; ช่วงร่วม
2021-2025 ได้ `62.05%` หรือ `10.14%` ต่อปี. Vanguard rolling 10-year NAV
return คือ `10.06%` ณ 30 มิ.ย. 2026 และ latest official NAV TR YTD คือ `+7.06%`
ณ 20 ก.ค. 2026.

## Performance check

- `entity_key: NYSE Arca:VGK`; official fund name, ticker, CUSIP `922042874`, NYSE Arca listing, and inception `4 มี.ค. 2005` are confirmed by Vanguard.
- Classification: `passive-index` / full replication. Vanguard states that VGK seeks to track the FTSE Developed Europe All Cap Index, targets developed European common stocks, remains fully invested, and uses a passively managed full-replication approach.
- Metric: Vanguard `NAV total return` assumes reinvestment of dividends and capital-gains distributions and is net of expenses. `S&P 500 Total Return` is a common USD reference only, not VGK's tracked index.
- Tracked-index history: Vanguard's comparative benchmark is spliced — MSCI Europe through 26 มี.ค. 2013, FTSE Developed Europe through 30 ก.ย. 2015, and FTSE Developed Europe All Cap thereafter; benchmark returns are adjusted for withholding taxes.
- Expense ratio: `0.06%`; dividend schedule: quarterly. The official factsheet describes the index as covering large-, mid- and small-cap companies across developed Europe.
- Latest official performance: Vanguard Advisors reports NAV TR YTD `7.06%` as of 20 ก.ค. 2026. The Vanguard factsheet as of 30 มิ.ย. 2026 reports NAV `YTD 8.98%`, `1Y 17.71%`, `3Y 16.45%`, `5Y 9.27%`, `10Y 10.06%`, and since inception `6.38%`; the different YTD figures have different as-of dates.
- Official price snapshot as of 12 มิ.ย. 2026: NAV `$89.60` and market price `$89.62`. A secondary FinanceCharts snapshot shows adjusted close `$90.59` on 31 ก.ค. 2026; it is retained as a price-only cross-check and is not used in the NAV return calculations.
- Official fund facts as of 30 มิ.ย. 2026: ETF total net assets `$29.98B`, 1,230 stocks, P/E `18.0x`, P/B `2.4x`, ROE `13.8%`, and 3-year standard deviation `13.67%`.

| Year | VGK NAV TR (USD) | FTSE Developed Europe All Cap / spliced index (USD) | S&P 500 TR (USD) |
|---|---:|---:|---:|
| 2016 | -0.59% | -0.48% | 11.96% |
| 2017 | 27.06% | 26.83% | 21.83% |
| 2018 | -14.79% | -15.14% | -4.38% |
| 2019 | 24.26% | 24.58% | 31.49% |
| 2020 | 6.50% | 6.54% | 18.40% |
| 2021 | 16.35% | 16.35% | 28.71% |
| 2022 | -16.04% | -16.45% | -18.11% |
| 2023 | 20.03% | 20.10% | 26.29% |
| 2024 | 2.04% | 2.23% | 25.02% |
| 2025 | 35.44% | 35.79% | 17.88% |

Coverage/source note: VGK and spliced-index rows are official Vanguard annual
returns for periods ended 31 ธ.ค. 2025. The current rolling and risk fields are
from the Vanguard factsheet as of 30 มิ.ย. 2026; latest current YTD is from the
Vanguard Advisors product capture as of 20 ก.ค. 2026. S&P 500 rows are the cached
USD total-return convention, dividends reinvested, as of 31 ธ.ค. 2025.

Official VGK rows compound to `130.81%` / rounded-input CAGR `8.72%` for
2016-2025 and `62.05%` / `10.14%` for 2021-2025. The spliced benchmark rows
compound to `130.41%` / `8.71%` and `62.07%` / `10.14%`; fund-minus-index
differences of approximately `+0.02 pp` and `-0.00 pp` are passive tracking
observations, not alpha. Cached S&P 500 TR compounds to `298.33%` / `14.82%`
for 2016-2025 and `96.17%` / `14.43%` for 2021-2025, so VGK trails that common
reference by approximately `-6.10 pp` and `-4.29 pp` of CAGR.

The issuer rolling 10-year NAV return of `10.06%` as of 30 มิ.ย. 2026 is kept
separate from the `8.72%` calendar-derived 2016-2025 CAGR because the windows
and as-of dates differ.

**Up years / Down years**

- Complete 2016-2025 NAV TR up/down: `7 / 3`
- Best NAV TR year: 2025, `+35.44%`
- Least positive year: 2024, `+2.04%`
- Worst NAV TR year: 2022, `-16.04%`
- Least bad down year: 2016, `-0.59%`
- Population standard deviation of the ten complete annual NAV returns: `16.62%`; the issuer's separate 3-year monthly standard deviation is `13.67%`.

## Risk read-through

VGK กระจาย across developed Europe แต่ยังมี country และ sector concentration:
UK `22.5%`, Switzerland `14.3%`, France `14.2%`, Germany `12.9%`, Netherlands
`8.7%`; sector weights include Financials `24.2%`, Industrials `19.1%`, Health
Care `12.5%`, Technology `9.6%`, and Consumer Discretionary `8.0%` ณ 30 มิ.ย.
2026. จึงมี European macro, EUR/GBP/CHF-USD FX, foreign-market, country,
financials/industrials, large-/mid-/small-cap and passive-tracking risk. Official
daily NAV maximum drawdown และ recovery date ยัง `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- [Vanguard VGK product page](https://investor.vanguard.com/investment-products/etfs/profile/vgk) — official identity, listing, inception, price/NAV snapshot, annual NAV/index rows and return definitions.
- [Vanguard Advisors VGK page](https://advisors.vanguard.com/investments/products/vgk/vanguard-ftse-europe-etf) — latest official NAV TR YTD capture, expense ratio and current product fields.
- [Vanguard VGK factsheet](https://fund-docs.vanguard.com/F0963.pdf) — official rolling returns, fund facts, index methodology, risk, country and sector exposures as of 30 มิ.ย. 2026.
- [FinanceCharts VGK price history](https://www.financecharts.com/etfs/VGK/summary/price) — secondary adjusted-close cross-check for 31 ก.ค. 2026; not used as NAV return evidence.
- S&P 500 Total Return 2016-2025 cached convention from the workflow; USD dividends reinvested, as of 31 ธ.ค. 2025.
- [[ETF_performance_sources_2026-08-18]] | [[ETF Performance Index]]
