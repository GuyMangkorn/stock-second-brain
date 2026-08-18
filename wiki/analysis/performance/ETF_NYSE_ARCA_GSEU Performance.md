---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:GSEU
input_ticker: GSEU
ticker: GSEU
exchange: NYSE Arca
fund: Goldman Sachs ActiveBeta Europe Equity ETF
tracked_index: Goldman Sachs ActiveBeta Europe Equity Index
benchmark: Goldman Sachs ActiveBeta Europe Equity Index
management_mode: passive-index-tracking
updated: 2026-08-19
performance_as_of: 2026-07-31
rolling_10y_as_of: 2026-07-31
current_ytd_as_of: 2026-07-31
source_batch: raw/imports/ETF_performance_sources_2026-08-19.md
return_basis: official NAV total return; distributions reinvested; net of fund expenses
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/GSEU
  - geography/Europe
---

# GSEU Performance

> Navigation: [[ETF Region Index]] → [[Europe ETF]] → [[ETF Performance Index]]

## Bottom line

GSEU เป็น Goldman Sachs ActiveBeta Europe Equity ETF ที่จดทะเบียนบน NYSE Arca
ตั้งแต่ 2 มี.ค. 2016 และเป็น passive index tracker ที่ติดตาม Goldman Sachs
ActiveBeta Europe Equity Index ซึ่งคัดเลือกหุ้นด้วย value, momentum, quality
และ low-volatility factors แล้ว rebalance รายไตรมาส. Official NAV Total Return
ปี 2021-2025 compound ได้ +60.21% หรือ 9.89% ต่อปี และ official YTD ล่าสุดคือ
+9.78% ณ 31 ก.ค. 2026. มี 4 ปีบวก / 1 ปีลบ; best 2025 +36.41% และ worst
2022 -18.12%.

## Performance check

- entity_key: NYSE Arca:GSEU; input ticker and canonical ticker are both GSEU; CUSIP 381430305; inception 2 Mar 2016; listing exchange NYSE Arca.
- Classification: passive-index-tracking strategic-beta equity ETF. The official prospectus says the Fund is not actively managed and generally does not dispose of a security unless it is removed from the Index.
- Index design: the Goldman Sachs ActiveBeta Europe Equity Index uses value, momentum, quality and low-volatility attributes, combines four factor indices equally and rebalances quarterly. The index provides developed-market Europe exposure.
- Metric: official NAV Total Return with all distributions reinvested; NAV total return assumes management fees and operating expenses. Return currency is USD.
- Ongoing expense ratio: 0.25%; fund factsheet as of 31 Jul 2026 shows 346 holdings and net assets of 120.87 million USD.
- Official rolling NAV fields as of 31 Jul 2026: YTD 9.78%, 1Y 22.13%, 3Y annualized 15.88%, 5Y annualized 8.85%, 10Y annualized 9.70%, since inception annualized 9.97%.
- Strategy-benchmark fields in the same official table: ActiveBeta Index YTD 9.80%, 1Y 22.30%, 3Y annualized 15.98%, 5Y annualized 8.84%, 10Y annualized 9.75%, since inception annualized 10.01%. These are benchmark-relative tracking observations, not manager-skill evidence.
- The reviewed official factsheet does not expose an exact latest NAV price in the text capture; current price/NAV and official daily NAV drawdown fields remain gaps.

| Year | GSEU NAV TR (USD) | S&P 500 TR (USD; common ref.) |
|---|---:|---:|
| 2021 | 16.78% | 28.71% |
| 2022 | -18.12% | -18.11% |
| 2023 | 20.86% | 26.29% |
| 2024 | 1.63% | 25.02% |
| 2025 | 36.41% | 17.88% |

**Up years / Down years**

- Official 2021-2025 up/down: 4 / 1
- Best: 2025, +36.41%
- Least positive: 2024, +1.63%
- Worst: 2022, -18.12%
- Least bad down year: 2022, the only down year
- Official 2021-2025 cumulative/CAGR: +60.21% / +9.89%
- Population standard deviation of the five official annual returns: 18.50%

The S&P 500 Total Return rows are a USD common reference, not the fund’s
strategy benchmark. No direct excess-return or manager-skill conclusion is
drawn from the side-by-side table. The strategy benchmark is the Goldman Sachs
ActiveBeta Europe Equity Index.

## Risk read-through

PortfoliosLab reports a dividend-adjusted full-history maximum drawdown of
-35.71% on 18 Mar 2020 with recovery in 172 trading sessions, and a secondary
2022 drawdown of -33.98%. These are secondary price/distribution observations,
not official daily NAV fields. The main structural risks are Europe country,
sector and factor concentration, foreign-market and currency exposure,
mid-/small-cap volatility, liquidity, index methodology and tracking risk.
The official factsheet notes that foreign investments may be more volatile and
less liquid than U.S. securities and that the fund may concentrate in Europe or
in industries represented heavily in the index.

## Sources

- [Goldman Sachs GSEU fact card](https://am.gs.com/public-assets/documents/570151a1-24d6-11ef-870d-25a687970406) — official identity, NAV/market-price and strategy-benchmark returns, expenses, holdings, index methodology and risk disclosures; facts as of 31 Jul 2026.
- [Goldman Sachs GSEU summary prospectus](https://am.gs.com/public-assets/documents/f69ce232-24e2-11ef-ad18-ad734f1320f3) — official objective, passive/not-actively-managed classification, benchmark and fee framework.
- [PortfoliosLab GSEU](https://portfolioslab.com/symbol/GSEU) — secondary dividend-adjusted performance and drawdown/recovery evidence.
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached workflow references — USD TR reference rows 2021-2025, dividends reinvested, as of 31 Dec 2025.
- [[ETF_performance_sources_2026-08-19]] | [[ETF Performance Index]]
