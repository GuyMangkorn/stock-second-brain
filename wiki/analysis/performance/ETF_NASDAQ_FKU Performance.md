---
type: etf-performance
instrument_type: ETF
entity_key: NASDAQ:FKU
ticker: FKU
exchange: Nasdaq
fund: First Trust United Kingdom AlphaDEX Fund
tracked_index: Nasdaq AlphaDEX United Kingdom Index
benchmark: S&P 500 Total Return
updated: 2026-08-18
performance_as_of: 2025-12-31
rolling_10y_as_of: 2026-07-31
current_ytd_as_of: 2026-07-31
price_nav_as_of: 2026-08-14
fund_facts_as_of: 2026-08-14
source_batch: raw/imports/ETF_performance_sources_2026-08-18.md
return_basis: NAV total return
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/FKU
  - geography/United-Kingdom
---

# FKU Performance

> Navigation: [[ETF Region Index]] → [[United Kingdom ETF]] → [[ETF Performance Index]]

## Bottom line

FKU เป็น passive/index-tracking equity ETF ที่ใช้กฎ AlphaDEX คัดหุ้นสหราชอาณาจักร
จาก growth และ value factors โดยเลือกหุ้น 75 ตัวและ rebalance ปีละสองครั้ง. ใน
complete calendar window 2016-2025 มี 6 ปีบวก / 4 ปีลบ; annual NAV Total
Return จาก official rounded rows ให้ cumulative `80.82%` และ CAGR `6.10%`, เทียบ
S&P 500 TR ที่ `298.33%` / `14.82%`. ปีดีที่สุดคือ 2025 ที่ `+37.60%` และแย่ที่สุด
คือ 2022 ที่ `-23.52%`. Latest official NAV TR YTD ที่ยืนยันได้คือ `+10.96%`
ณ 31 ก.ค. 2026.

## Performance check

- `entity_key: NASDAQ:FKU`
- Classification: supported passive/index-tracking equity ETF; the prospectus
  says the fund operates as an index fund, normally invests at least 90% of
  net assets in index securities, and is not actively managed.
- Inception: 14 ก.พ. 2012; exchange `Nasdaq`; total expense ratio `0.80%`
  (as of 1 พ.ค. 2026); number of holdings `76` ณ 14 ส.ค. 2026.
- Metric: `NAV Total Return` บนฐาน USD รวม distributions ตาม issuer methodology
  และหัก fund expenses; market-price return kept separate.
- Tracked index: `Nasdaq AlphaDEX United Kingdom Index`. The methodology ranks
  growth factors (3-, 6-, 12-month price appreciation, sales/price and one-year
  sales growth) and value factors (book/price, cash-flow/price and return on
  assets), selects the top 75 stocks, applies quintile weighting and sector
  constraints, and rebalances semi-annually.
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference
  benchmark ไม่ใช่ tracked index ของ FKU). The strategy-aligned comparison is
  the official Nasdaq AlphaDEX United Kingdom Index.
- Official rolling 10-year NAV TR: average annual `8.67%` ณ 31 ก.ค. 2026;
  เป็น rolling issuer figure แยกจาก calendar-row CAGR.
- Current official NAV TR as of 31 ก.ค. 2026: YTD `10.96%`, 1-year `25.50%`,
  3-year `20.53%`, 5-year `9.03%`, 10-year `8.67%`, and since inception
  `7.86%`. Same-date tracked-index fields were `12.12%`, `26.55%`, `21.94%`,
  `10.41%`, and `9.88%` for the comparable periods.
- Latest quote snapshot as of 14 ส.ค. 2026: NAV `US$56.53`, closing market price
  `US$56.69`, premium `+0.33%`, net assets `US$39,567,669`, and 30-day median
  bid/ask spread `0.57%`; quotes are not used in return calculations.
- Coverage/source note: the issuer notes that the underlying index changed on
  14 ก.ค. 2015 from the Defined United Kingdom Index to the Nasdaq AlphaDEX UK
  Index. The long history is retained with this continuity caveat and is not
  presented as a single uninterrupted current-index record.

| Year | FKU NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | -16.08% | 11.96% |
| 2017 | 25.53% | 21.83% |
| 2018 | -16.16% | -4.38% |
| 2019 | 32.36% | 31.49% |
| 2020 | -5.25% | 18.40% |
| 2021 | 19.10% | 28.71% |
| 2022 | -23.52% | -18.11% |
| 2023 | 20.59% | 26.29% |
| 2024 | 8.01% | 25.02% |
| 2025 | 37.60% | 17.88% |

## Up years / Down years

- Up years / Down years: `6 / 4` ใน 2016-2025
- Best: 2025, `+37.60%`
- Least positive: 2024, `+8.01%`
- Worst: 2022, `-23.52%`
- Least bad down year: 2020, `-5.25%`
- 2016-2025 cumulative/CAGR: FKU `80.82%` / `6.10%`; S&P 500 TR
  `298.33%` / `14.82%`
- 2021-2025 cumulative/CAGR: FKU `63.25%` / `10.30%`; S&P 500 TR
  `96.17%` / `14.43%`
- Current FKU NAV TR YTD: `+10.96%` ณ 31 ก.ค. 2026; the official
  strategy-aligned index was `+12.12%` on the same date. This is tracking
  comparison evidence, not a claim of manager skill.

## Risk read-through

จาก annual rows แบบ rounded-input ช่วง 2016-2025 ได้ annual-return volatility
แบบ population `20.95%`; official 3-year statistics ณ 31 ก.ค. 2026 รายงาน
standard deviation `15.80%`, beta `1.18`, Sharpe ratio `0.98`, และ correlation
`0.93`. Current exposures ณ 14 ส.ค. 2026 กระจายไปที่ Financials `25.33%`,
Industrials `15.49%`, Consumer Discretionary `15.26%`, Consumer Staples `11.55%`,
Materials `7.93%`, Information Technology `6.09%`, Energy `5.98%`, and Real
Estate `5.30%` among the largest sector weights. จึงมี country/sector/factor
selection/FX, small-/mid-cap และ liquidity risks แม้จะมี 76 holdings.

Prospectus disclosed best quarter `+23.45%` ณ 31 ธ.ค. 2022 และ worst quarter
`-40.79%` ณ 31 มี.ค. 2020. Official daily NAV history ที่เพียงพอสำหรับ
maximum drawdown และ recovery ยังไม่ถูกเปิดเผย จึงไม่ใช้ market-price proxy
แทน NAV risk metric.

## Sources

- [First Trust FKU product page](https://www.ftportfolios.com/Retail/Etf/EtfSummary.aspx?Ticker=FKU) — identity, index methodology, fee, current NAV/price, holdings, exposures, rolling returns, YTD and risk statistics
- [First Trust Exchange-Traded AlphaDEX Fund II prospectus](https://www.ftportfolios.com/LoadContent/gradkqbz8r4y) — passive strategy, index-change disclosure, official 2016-2025 annual-return chart, average annual returns and risk disclosure
- [SEC FKU summary prospectus](https://www.sec.gov/Archives/edgar/data/1510337/000144554626003320/fku_497k.htm) — official calendar-year returns and best/worst-quarter disclosure
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- Cached S&P 500 TR references: [2016-2019](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [2018-2022](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), [2021](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/), [2022-2025](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/)
- ETF source batch: [[ETF_performance_sources_2026-08-18]] | [[ETF Performance Index]]
