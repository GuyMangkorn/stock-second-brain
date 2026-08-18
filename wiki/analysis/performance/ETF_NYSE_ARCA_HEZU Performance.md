---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:HEZU
input_ticker: HEZU
ticker: HEZU
exchange: NYSE Arca
fund: iShares Currency Hedged MSCI Eurozone ETF
tracked_index: MSCI EMU 100% Hedged to USD Index (Net)
benchmark: S&P 500 Total Return
updated: 2026-08-18
performance_as_of: 2025-12-31
rolling_10y_as_of: 2026-06-30
current_ytd_as_of: 2026-08-14
price_nav_as_of: 2026-08-14
fund_facts_as_of: 2026-08-14
source_batch: raw/imports/ETF_performance_sources_2026-08-18.md
return_basis: NAV total return; gross income reinvested; fund expenses reflected in NAV
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/HEZU
  - geography/Europe
---

# HEZU Performance

> Navigation: [[ETF Region Index]] → [[Europe ETF]] → [[ETF Performance Index]]

## Bottom line

`HEZU` คือ iShares Currency Hedged MSCI Eurozone ETF ที่จดทะเบียนบน NYSE Arca
และใช้ USD เป็น share-class currency. กองทุนเป็น `passive-index` equity ETF
ที่ลงทุนหลักผ่าน `EZU` และใช้ foreign-currency forwards เพื่อลด EUR/USD
exposure; derivatives เป็นส่วนของ currency hedge ไม่ใช่ leverage หรือ option-income
payoff. Official 2021-2025 NAV TR ให้ cumulative `91.52%` และ rounded-input
calendar CAGR `13.88%`; issuer rolling 10-year NAV TR อยู่ที่ `12.88%` ณ
30 มิ.ย. 2026. Common USD reference อย่าง S&P 500 TR ให้ `96.17%` / `14.43%`
ในช่วงเดียวกัน. Latest official NAV TR YTD คือ `17.53%` ณ 14 ส.ค. 2026.

## Performance check

- `entity_key: NYSE Arca:HEZU`; canonical fund name and exchange are confirmed by
  the issuer product page and SEC summary prospectus. Fund inception is 9 ก.ค.
  2014 and the asset class is equity.
- Classification: `passive-index`. The prospectus says the Fund seeks to track
  `MSCI EMU 100% Hedged to USD Index (Net)`, uses an indexing approach, invests
  substantially in `EZU`, and enters currency forwards to hedge euro exposure.
- Metric: issuer `NAV Total Return` with reinvested distributions and fund
  expenses reflected in NAV. Market-price return is kept separate.
- Official rolling annualised fields as of 30 มิ.ย. 2026: 1-year `26.48%`,
  3-year `18.64%`, 5-year `13.47%`, 10-year `12.88%`, and since inception
  `10.58%`.
- Current official snapshot as of 14 ส.ค. 2026: NAV `$50.62`, closing price
  `$50.68`, net assets `$589.68m`, and one underlying fund holding. Expense
  ratio is `1.12%`; contractual net expense ratio is `0.53%` after a `0.59%`
  fee waiver. Distribution frequency is semi-annual.

| Year | HEZU NAV TR (USD) | MSCI EMU 100% Hedged to USD NR (USD) | S&P 500 TR (USD) |
|---|---:|---:|---:|
| 2021 | 23.25% | 23.24% | 28.71% |
| 2022 | -9.34% | -9.88% | -18.11% |
| 2023 | 22.89% | 22.08% | 26.29% |
| 2024 | 10.82% | 11.38% | 25.02% |
| 2025 | 25.86% | 26.11% | 17.88% |

Official iShares calendar rows in the reviewed factsheet cover 2021-2025;
2016-2020 rows were not disclosed in that capture, so no ten-year calendar
CAGR is reconstructed. The `12.88%` ten-year figure above is the issuer's
rolling annualised NAV TR field, not the calendar-row CAGR. S&P 500 rows reuse
the cached USD Total Return convention as of 2025-12-31.

## Up years / Down years

- Complete 2021-2025 NAV TR up/down: `4 / 1`
- Best NAV TR year: 2025, `+25.86%`
- Least positive year: 2024, `+10.82%`
- Worst NAV TR year: 2022, `-9.34%`
- 2021-2025 HEZU NAV TR cumulative/CAGR: `91.52%` / `13.88%`.
- 2021-2025 issuer benchmark cumulative/CAGR: `90.45%` / `13.75%`; the
  rounded-input difference is approximately `+0.13 pp` CAGR and is a passive
  tracking comparison, not alpha.
- 2021-2025 S&P 500 TR cumulative/CAGR: `96.17%` / `14.43%` as a common USD
  reference. HEZU's rounded-input CAGR was approximately `0.55 pp` below it.
- Daily NAV maximum drawdown and recovery date were not disclosed in the
  reviewed official capture; no price-only proxy is substituted.

## Risk read-through

The latest issuer risk snapshot reports 3-year standard deviation `11.39%` and
beta `0.59` as of 31 ก.ค. 2026; P/E `19.36x` and P/B `2.41x` are as of 14 ส.ค.
2026, while trailing yield is `2.57%` as of 31 ก.ค. 2026. Look-through sector
exposure as of 14 ส.ค. 2026 was led by Financials `26.98%`, Industrials
`20.43%`, and Information Technology `16.06%`; country exposure was led by
France `28.01%`, Germany `25.34%`, and the Netherlands `16.97%`.

The hedge is designed to reduce, not eliminate, EUR/USD fluctuations. Forward
roll, basis mismatch, counterparty, derivative and residual currency risks can
therefore remain alongside Eurozone equity, country, sector and valuation risk.
The annual 2021-2025 return population standard deviation is `13.10%`, calculated
from the five rounded NAV rows; it is not substituted for the issuer's 3-year
standard deviation.

## Sources

- [iShares Currency Hedged MSCI Eurozone ETF product page](https://www.ishares.com/us/products/268708/HEZU) — official exchange, current NAV/YTD, net assets, fees, benchmark, rolling returns, risk and exposure snapshot
- [iShares HEZU factsheet, June 2026](https://www.ishares.com/us/literature/fact-sheet/hezu-ishares-currency-hedged-msci-eurozone-etf-fund-fact-sheet-en-us.pdf) — official 2021-2025 NAV/benchmark rows, rolling returns, fees, structure and risk fields
- [HEZU SEC summary prospectus](https://www.sec.gov/Archives/edgar/data/1100663/000119312525336755/d918823d497k.htm) — official passive objective, underlying fund, indexing approach and currency-forward hedge disclosures
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- Cached S&P 500 TR references: [2016-2019](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [2018-2022](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), [2021](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/), and [2022-2025](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/)
- ETF source batch: [[ETF_performance_sources_2026-08-18]] | [[ETF Performance Index]]
