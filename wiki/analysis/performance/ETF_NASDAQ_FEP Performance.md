---
type: etf-performance
instrument_type: ETF
entity_key: NASDAQ:FEP
ticker: FEP
exchange: Nasdaq
fund: First Trust Europe AlphaDEX Fund
tracked_index: Nasdaq AlphaDEX Europe Index
benchmark: S&P 500 Total Return
updated: 2026-08-18
performance_as_of: 2025-12-31
rolling_10y_as_of: 2026-07-31
current_ytd_as_of: 2026-07-31
price_nav_as_of: 2026-08-13
fund_facts_as_of: 2026-08-13
source_batch: raw/imports/ETF_performance_sources_2026-08-18.md
return_basis: NAV total return
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/FEP
  - geography/Europe
---

# FEP Performance

> Navigation: [[ETF Region Index]] → [[Europe ETF]] → [[ETF Performance Index]]

## Bottom line

FEP เป็น passive/index-tracking international equity ETF ที่ใช้กฎคัดเลือก
หุ้นแบบ AlphaDEX จาก Nasdaq Developed Markets Europe Index โดยผสม growth และ
value factors แล้วให้น้ำหนักตาม quintile ภายใต้ข้อจำกัด country/sector. ใน
complete calendar window 2016-2025 มี 8 ปีบวก / 2 ปีลบ; annual NAV Total
Return ที่คำนวณจาก official rounded rows ให้ cumulative `144.62%` และ CAGR
`9.36%`, เทียบ S&P 500 TR ที่ `298.33%` / `14.82%`. ปีดีที่สุดคือ 2025 ที่
`+55.13%` และแย่ที่สุดคือ 2022 ที่ `-22.87%`. Latest official NAV TR YTD
ที่ยืนยันได้คือ `+11.02%` ณ 31 ก.ค. 2026.

## Performance check

- `entity_key: NASDAQ:FEP`
- Classification: supported passive/index-tracking equity ETF; the prospectus
  says the fund uses an indexing approach and normally invests at least 90% of
  net assets in index securities.
- Inception: 18 เม.ย. 2011; exchange `Nasdaq`; total expense ratio `0.80%`
  (as of 1 พ.ค. 2026); number of holdings `200` ณ 13 ส.ค. 2026.
- Metric: `NAV Total Return` บนฐาน USD รวม distributions ตาม issuer
  methodology และหัก fund expenses; market-price return kept separate.
- Tracked index: `Nasdaq AlphaDEX Europe Index`. The index ranks growth factors
  (3-, 6-, 12-month price appreciation, sales/price and one-year sales growth)
  and value factors (book/price, cash-flow/price and return on assets), selects
  the top 200 stocks, and rebalances semi-annually.
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference
  benchmark ไม่ใช่ tracked index ของ FEP). The strategy-aligned comparison is
  the official Nasdaq AlphaDEX Europe Index.
- Official rolling 10-year NAV TR: average annual `10.57%` ณ 31 ก.ค. 2026;
  เป็น rolling issuer figure แยกจาก calendar-row CAGR.
- Current official NAV TR YTD: `11.02%`; 1-year `27.32%`; 3-year `21.97%`;
  5-year `10.06%`; 10-year `10.57%`; since inception `7.61%`, all as of
  31 ก.ค. 2026. The same-date tracked-index fields were `11.31%`, `27.45%`,
  `22.85%`, `10.84%`, and `11.31%` for the comparable periods.
- Latest quote snapshot: NAV `US$59.71`, closing market price `US$59.97`, and
  premium `+0.44%` ณ 13 ส.ค. 2026; quotes are not used in return calculations.
- Coverage/source note: the prospectus states that the underlying index changed
  on 13 ต.ค. 2015 from the Defined Europe Index to the Nasdaq AlphaDEX Europe
  Index. It describes the new index as substantially similar, so the long
  history is retained with this continuity caveat.

| Year | FEP NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 1.24% | 11.96% |
| 2017 | 35.67% | 21.83% |
| 2018 | -18.67% | -4.38% |
| 2019 | 24.38% | 31.49% |
| 2020 | 4.95% | 18.40% |
| 2021 | 16.53% | 28.71% |
| 2022 | -22.87% | -18.11% |
| 2023 | 16.01% | 26.29% |
| 2024 | 3.71% | 25.02% |
| 2025 | 55.13% | 17.88% |

## Up years / Down years

- Up years / Down years: `8 / 2` ใน 2016-2025
- Best: 2025, `+55.13%`
- Least positive: 2024, `+3.71%`
- Worst: 2022, `-22.87%`
- Least bad down year: 2018, `-18.67%`
- 2016-2025 cumulative/CAGR: FEP `144.62%` / `9.36%`; S&P 500 TR
  `298.33%` / `14.82%`
- 2021-2025 cumulative/CAGR: FEP `67.75%` / `10.90%`; S&P 500 TR
  `96.17%` / `14.43%`
- Current FEP NAV TR YTD: `+11.02%` ณ 31 ก.ค. 2026; the official
  strategy-aligned index was `+11.31%` on the same date. This is a tracking
  comparison, not a claim of manager skill.

## Risk read-through

จาก annual rows แบบ rounded-input ช่วง 2016-2025 ได้ annual-return volatility
แบบ population `22.36%`; official 3-year statistics ณ 31 ก.ค. 2026 รายงาน
standard deviation `14.98%`, beta `1.00`, Sharpe ratio `1.11`, และ correlation
`0.93`. Current exposure มี United Kingdom `20.08%`, Germany `13.52%`, France
`11.36%`; sectors คือ Industrials `21.63%`, Materials `13.85%`, Financials
`12.05%`, Consumer Discretionary `11.13%`, และ Energy `10.74%` ณ 12 ส.ค. 2026.
จึงมี country/sector/factor-selection/FX และ small-/mid-cap risks แม้จะมี
200 holdings.

Prospectus disclosed best quarter `+22.10%` ณ 31 ธ.ค. 2022 และ worst quarter
`-31.13%` ณ 31 มี.ค. 2020. Official daily NAV history ที่เพียงพอสำหรับ
maximum drawdown และ recovery ยังไม่ถูกเปิดเผย จึงไม่ใช้ market-price proxy
แทน NAV risk metric.

## Sources

- [First Trust FEP product page](https://www.ftportfolios.com/Retail/Etf/EtfSummary.aspx?Ticker=FEP) — identity, index methodology, fee, current NAV/price, holdings, exposures, rolling returns, YTD and risk statistics
- [First Trust Exchange-Traded AlphaDEX Fund II prospectus](https://www.ftportfolios.com/LoadContent/gradkqbz8r4y) — passive strategy, index-change disclosure, official 2016-2025 annual-return chart, average annual returns and risk disclosure
- [SEC N-CSR / FEP annual report evidence](https://www.sec.gov/Archives/edgar/data/1510337/000144554626001916/adex2_ncsr.htm) — 2025 official annual return and fund/index comparison
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- Cached S&P 500 TR references: [2016-2019](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [2018-2022](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), [2021](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/), [2022-2025](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/)
- ETF source batch: [[ETF_performance_sources_2026-08-18]] | [[ETF Performance Index]]
