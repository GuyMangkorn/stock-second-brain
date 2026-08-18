---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:FLEU
input_ticker: FLEU
ticker: FLEU
exchange: NYSE Arca
fund: Franklin FTSE Eurozone ETF
tracked_index: Linked FTSE Developed Eurozone Index-NR
benchmark: S&P 500 Total Return
updated: 2026-08-18
performance_as_of: 2025-12-31
rolling_10y_as_of: not-applicable-lt-10y
current_ytd_as_of: 2026-07-23
price_nav_as_of: 2026-07-23
fund_facts_as_of: 2026-07-23
source_batch: raw/imports/ETF_performance_sources_2026-08-18.md
return_basis: NAV total return; distributions reinvested; fund expenses reflected in NAV
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/FLEU
  - geography/Europe
---

# FLEU Performance

> Navigation: [[ETF Region Index]] → [[Europe ETF]] → [[ETF Performance Index]]

## Bottom line

`FLEU` คือ Franklin FTSE Eurozone ETF ที่จดทะเบียนบน NYSE Arca และเป็น
`passive-index` equity ETF. Current objective คือการติดตาม `FTSE Developed
Eurozone Index` แต่ performance history ใช้ linked benchmark เพราะกองทุน
เปลี่ยน underlying index เมื่อ 1 ส.ค. 2023: ช่วงก่อนหน้าอ้างอิง FTSE Developed
Europe Capped Hedged Index และหลังจากนั้นอ้างอิง FTSE Developed Eurozone Index.
Official complete 2018-2025 NAV TR ให้ cumulative `126.40%` และ rounded-input
CAGR `10.75%`; common 2021-2025 ให้ `93.03%` / `14.06%`. Latest official
issuer NAV YTD ที่พบใน capture คือ `6.75%` ณ 23 ก.ค. 2026; ไม่พบตัวเลข official
ที่ใหม่กว่านี้ในรอบตรวจ.

## Performance check

- `entity_key: NYSE Arca:FLEU`; official fund name, ticker and exchange are
  confirmed by Franklin Templeton. Fund inception is 2 พ.ย. 2017 and asset
  class is equity.
- Classification: `passive-index` / indexed. The fund normally invests at least
  80% in the component securities of the underlying index or depositary receipts
  and may use replication or representative sampling.
- Current tracked index: `FTSE Developed Eurozone Index`; issuer performance
  table uses `Linked FTSE Developed Eurozone Index-NR`. Effective 1 ส.ค. 2023,
  the fund changed from the FTSE Developed Europe Capped Hedged Index to the
  FTSE Developed Eurozone Index; the linked benchmark joins the predecessor
  period to the current period.
- Metric: issuer `NAV Return` with distributions reinvested and fund expenses
  deducted. Market-price return is kept separate.
- Official rolling fields as of 30 มิ.ย. 2026: NAV 1-year `19.68%`, 3-year
  `17.80%`, 5-year `12.92%`, since inception `10.90%`; linked benchmark
  `19.45%`, `17.64%`, `12.73%`, and `10.75%`, respectively. No official 10-year
  field is applicable because the fund launched in 2017.
- Latest issuer snapshot in the reviewed product-page capture as of 23 ก.ค.
  2026: NAV `$34.93`, market price `$34.90`, net assets `$69.85m`, 260 holdings,
  and 30-day median bid/ask spread `0.48%`. Gross and net expense ratios are
  both `0.09%`; distribution frequency is semi-annual.
- The June 2026 factsheet showed NAV YTD `9.16%` as of 30 มิ.ย. 2026, while the
  later issuer product-page capture showed NAV YTD `6.75%` as of 23 ก.ค. 2026.
  These are different as-of dates, not a same-date conflict; the later product
  page value is used for the latest-YTD field.

| Year | FLEU NAV TR (USD) | Linked FTSE Developed Eurozone Index-NR (USD) | S&P 500 TR (USD) |
|---|---:|---:|---:|
| 2018 | -8.23% | -8.27% | -4.38% |
| 2019 | 27.22% | 27.14% | 31.49% |
| 2020 | 0.46% | 0.31% | 18.40% |
| 2021 | 23.43% | 23.27% | 28.71% |
| 2022 | -6.97% | -7.09% | -18.11% |
| 2023 | 15.90% | 15.68% | 26.29% |
| 2024 | 2.79% | 2.71% | 25.02% |
| 2025 | 41.11% | 40.80% | 17.88% |

The 2017 inception year is partial and not disclosed in the factsheet, so it is
excluded from complete-year ranking. The 2018-2025 table is an official linked
history, but it is not a pure current-strategy window because the benchmark and
fund objective changed on 1 ส.ค. 2023. S&P 500 rows reuse the cached USD Total
Return convention as of 2025-12-31.

## Up years / Down years

- Complete 2018-2025 NAV TR up/down: `6 / 2`
- Best NAV TR year: 2025, `+41.11%`
- Least positive year: 2020, `+0.46%`
- Worst NAV TR year: 2018, `-8.23%`
- Least bad down year: 2022, `-6.97%`
- Complete 2018-2025 NAV TR cumulative/CAGR: `126.40%` / `10.75%`; this is
  compounded from rounded official annual inputs and contains the linked-index
  transition caveat.
- Common 2021-2025 NAV TR cumulative/CAGR: `93.03%` / `14.06%`; linked
  benchmark is `91.60%` / `13.89%`, an approximate `+0.17 pp` CAGR tracking
  difference, not alpha.
- Common 2021-2025 S&P 500 TR cumulative/CAGR: `96.17%` / `14.43%` as a USD
  reference. FLEU's rounded-input CAGR was approximately `0.37 pp` below it.
- Latest official issuer NAV TR YTD in the reviewed capture: `+6.75%` as of
  23 ก.ค. 2026. A more recent official YTD value was not found.
- Daily NAV maximum drawdown and recovery date were not disclosed in the
  reviewed official capture; no price-only proxy is substituted.

## Risk read-through

The official June 2026 factsheet reports 3-year NAV-return standard deviation
`15.00%` versus `14.96%` for the linked benchmark. The latest product-page
portfolio snapshot as of 23 ก.ค. 2026 reports P/E `17.92x`, P/B `2.39x`, and
country weights led by France `27.40%`, Germany `24.27%`, Netherlands `15.86%`,
Spain `11.19%`, and Italy `10.06%`. June 2026 sector weights were led by
Financials `26.00%`, Industrials `20.00%`, and Information Technology `16.34%`.

FLEU is a small fund, so liquidity and bid/ask spread are material alongside
Eurozone equity, country, sector and EUR/USD risks. The index splice matters:
2018-2022 include the former hedged-Europe objective, while 2023-2025 include
the current Eurozone objective. The annual 2018-2025 return population standard
deviation is `16.63%`, calculated from the eight rounded NAV rows; it is not
substituted for the issuer's 3-year standard deviation.

## Sources

- [Franklin FTSE Eurozone ETF product page](https://www.franklintempleton.com/investments/options/exchange-traded-funds/products/26347/SINGLCLASS/franklin-ftse-eurozone-etf/FLEU) — official current objective, exchange, fees, NAV/YTD, assets, holdings, liquidity, portfolio and rolling performance
- [Franklin FLEU factsheet, June 2026](https://www.franklintempleton.com/forms-literature/download/FLEH-FF) — official 2018-2025 NAV/linked-benchmark rows, rolling returns, risk and index-transition note
- [Franklin FLEU prospectus supplement and summary prospectus](https://www.sec.gov/Archives/edgar/data/1655589/000174177324001255/c497.htm) — official passive strategy, 80% policy, derivative tracking role and 1 Aug 2023 benchmark transition
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- Cached S&P 500 TR references: [2016-2019](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [2018-2022](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), [2021](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/), and [2022-2025](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/)
- ETF source batch: [[ETF_performance_sources_2026-08-18]] | [[ETF Performance Index]]
