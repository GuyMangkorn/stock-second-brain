---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:FNDA
input_ticker: FNDA
ticker: FNDA
exchange: NYSE Arca
fund: Schwab Fundamental U.S. Small Company ETF
tracked_index: RAFI Fundamental High Liquidity US Small Index
benchmark: S&P 500 Total Return
management_mode: passive-index-tracking
updated: 2026-08-29
annual_performance_as_of: 2025-12-31
performance_as_of: 2026-07-31
rolling_10y_as_of: 2026-07-31
current_ytd_as_of: 2026-07-31
nav_as_of: 2026-08-27
market_price_as_of: 2026-08-28
fund_facts_as_of: 2026-08-27
risk_as_of: 2026-07-31
source_batch: raw/imports/ETF_performance_sources_2026-08-29.md
return_basis: NAV total return; dividends and capital gains reinvested; net of expenses
return_currency: USD
primary_region: USA
tags:
  - analysis/etf-performance
  - ticker/FNDA
  - geography/United-States
---

# FNDA Performance

> Navigation: [[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]

## Bottom line

`FNDA` คือ Schwab Fundamental U.S. Small Company ETF แบบ passive/index-tracking
ที่ใช้ fundamental weighting กับหุ้น U.S. small-cap และติดตาม `RAFI Fundamental
High Liquidity US Small Index`. Official Schwab รายงาน NAV Total Return แบบ
rolling 10-year annualized `10.72%` และ current NAV TR YTD `18.41%` ณ
2026-07-31. Latest fund snapshot มี NAV `$37.61`, AUM `$9,238.33M` และ expense
ratio `0.25%` ณ 2026-08-27.

Complete calendar-year rows 2016-2025 เป็น secondary dividend-adjusted
total-return proxy*; proxy cumulative `159.56%` / rounded-input CAGR `10.01%*`
และ 2021-2025 CAGR `9.49%*`. ตัวเลข proxy ไม่ถูก relabel เป็น official NAV rows
และไม่ถูกใช้เป็นหลักฐานของ manager alpha.

## Performance check

- `entity_key: NYSE Arca:FNDA`; Schwab ระบุ fund เป็น `Schwab Fundamental U.S. Small Company ETF`, listed on NYSE Arca, inception `2013-08-15`, CUSIP `808524763`.
- Classification: `passive-index-tracking`; objective คือพยายามติดตาม total return ของบริษัท U.S. small-cap ที่จัดขนาดและน้ำหนักด้วย fundamental measures ก่อน fees and expenses.
- Metric: official Schwab `NAV Total Return` รวมการ reinvest distributions และ fund expenses; USD. Market-price return และ index return แยกเก็บจาก NAV.
- Tracked index: current issuer benchmark `RAFI Fundamental High Liquidity US Small Index`; common comparison benchmark คือ `S&P 500 Total Return` (USD, dividends reinvested) ไม่ใช่ issuer benchmark ของ FNDA.
- Schwab ระบุว่า benchmark เปลี่ยนจาก `Russell RAFI US Small Company Index` เป็น `RAFI Fundamental High Liquidity US Small Index` มีผล `2024-06-21`; `Fundamental U.S. Small Company Spliced Index` ใช้เป็น official long-history comparison.
- Official rolling 10-year NAV TR average annual `10.72%` as of `2026-07-31`; official current NAV TR YTD `18.41%` as of `2026-07-31`.
- Official current snapshot as of `2026-08-27` to `2026-08-28`: NAV `$37.61`, previous close `$37.62`, indicative bid/ask midpoint `$37.61`, premium/discount `0.03%`, 30-day median bid/ask spread `0.03%`, AUM `$9,238.33M`, shares `245.65M`, holdings `918`, and turnover `24.50%` as of 2026-07-31.
- Official characteristics as of `2026-07-31`: weighted average market cap `$8.98B`, P/E `18.78`, P/CF `9.63`, ROE `10.07%`, P/B `2.04`, 3-year beta versus benchmark `1.00`, and 3-year standard deviation `18.27%`.

### Official July 2026 standardized returns

| Return basis | 1M | 3M | YTD | 1Y | 3Y annualized | 5Y annualized | 10Y annualized | Since inception annualized |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| FNDA market price | -2.34% | 4.65% | 18.49% | 28.86% | 13.07% | 8.53% | 10.72% | 10.27% |
| FNDA NAV | -2.29% | 4.59% | 18.41% | 28.73% | 13.09% | 8.52% | 10.72% | 10.27% |
| RAFI Fundamental High Liquidity US Small Index | -2.27% | 4.65% | 18.59% | 29.03% | not disclosed | not disclosed | not disclosed | not disclosed |
| Russell RAFI US Small Company Index | -2.44% | 5.26% | 19.86% | 31.59% | 13.86% | 9.03% | 11.08% | not disclosed |
| Fundamental U.S. Small Company Spliced Index | -2.27% | 4.65% | 18.59% | 29.03% | 13.31% | 8.72% | 10.92% | not disclosed |
| Russell 2000 Index | -3.03% | 4.99% | 18.85% | 34.18% | 15.09% | 7.11% | 10.64% | not disclosed |

All official rows above are as of `2026-07-31`. Schwab defines periods under one
year as cumulative and periods of one year or longer as annualized. The
long-history spliced index is not the current issuer benchmark; the Russell
2000 row is a broad small-cap reference, not manager-skill evidence.

### Secondary annual total-return context

| Year | FNDA secondary total-return proxy* | S&P 500 TR (USD; common ref.) |
|---|---:|---:|
| 2016 | 23.54% | 11.96% |
| 2017 | 12.66% | 21.83% |
| 2018 | -12.10% | -4.38% |
| 2019 | 24.33% | 31.49% |
| 2020 | 8.46% | 18.40% |
| 2021 | 31.11% | 28.71% |
| 2022 | -14.82% | -18.11% |
| 2023 | 20.31% | 26.29% |
| 2024 | 8.99% | 25.02% |
| 2025 | 7.44% | 17.88% |

`*` Annual FNDA rows are ETFreplay dividend-adjusted total-return observations,
not issuer-published NAV rows. Annual S&P 500 rows reuse the cached USD Total
Return convention as of `2025-12-31`, with dividends reinvested.

## Window calculations and tracking context

- Secondary 2016-2025 proxy compounds to `159.56%*`; rounded-input CAGR is `(1 + 1.5956)^(1/10) - 1 = 10.01%*`; population standard deviation is `14.33%*`; up/down years are `8 / 2`, best is 2021 `+31.11%*`, least positive is 2025 `+7.44%*`, worst is 2022 `-14.82%*`, and least-bad down year is 2018 `-12.10%*`.
- Secondary 2021-2025 proxy compounds to `57.34%*`; rounded-input CAGR is `(1 + 0.5734)^(1/5) - 1 = 9.49%*`. Cached S&P 500 TR compounds to `96.17%` / CAGR `14.43%` over the same window. This is a common reference, not management-skill evidence.
- Official FNDA NAV minus the current RAFI index as of 2026-07-31 is 1M `-0.02 pp`, 3M `-0.06 pp`, YTD `-0.18 pp`, and 1Y `-0.30 pp`; longer current-index fields are not disclosed.
- Against the official long-history spliced index, NAV minus index is 1M `-0.02 pp`, 3M `-0.06 pp`, YTD `-0.18 pp`, 1Y `-0.30 pp`, 3Y `-0.22 pp`, 5Y `-0.20 pp`, and 10Y `-0.20 pp`. These are implementation/expense and index-construction observations, not alpha.
- Reconciliation: ETFreplay is the canonical secondary annual series. FinanceCharts is close but not identical (for example 2016 `23.49%` versus `23.54%` and 2019 `24.32%` versus `24.33%`); it is retained only as a cross-check. Its partial 2026 observation is not mixed with the official July YTD.

## Risk read-through

Current official top holdings as of `2026-08-27` are Lumentum Holdings `0.56%`,
Victoria's Secret `0.47%`, Compass `0.44%`, Delek US `0.37%`, Abercrombie & Fitch
Class A `0.36%`, Twilio Class A `0.34%`, MKS `0.34%`, Par Pacific Holdings `0.33%`,
Coherent `0.33%`, and ATI `0.32%`; the displayed top ten sum is `3.86%`. Asset
allocation is stocks `99.91%`, cash investments `0.09%`, and other `0.00%` as of
the same date.

Sector weights as of `2026-06-30` are Industrials `20.73%`, Financials `16.31%`,
Information Technology `14.26%`, Consumer Discretionary `12.57%`, Real Estate
`9.22%`, Health Care `7.39%`, Energy `4.93%`, Materials `4.85%`, Communication
Services `3.85%`, Consumer Staples `3.25%`, and Utilities `2.63%`.

FNDA มี small-cap, fundamental/value tilt, factor-regime, turnover, liquidity,
valuation และ sector risks. Official Schwab reports best three months `+32.40%`
สำหรับช่วง 2020-10-31 ถึง 2021-01-31 และ worst three months `-35.49%` สำหรับช่วง
2019-12-31 ถึง 2020-03-31. Official daily NAV history สำหรับคำนวณ maximum
drawdown และ recovery date ยังไม่พบข้อมูลที่ยืนยันได้.

## Sources

- [Official Schwab FNDA product page](https://www.schwabassetmanagement.com/products/fnda) — objective, current index, passive style, fee, NAV/AUM/holdings, characteristics, yields, current quote fields and official July return/risk tables.
- [Official Schwab FNDA fact-sheet page](https://www.schwabassetmanagement.com/resource/fnda-fact-sheet) — issuer document entry and fund facts.
- [SEC FNDA summary prospectus](https://www.sec.gov/Archives/edgar/data/1454889/000110465925063127/tm2513735-8_497k.htm) — passive objective, fees, benchmark-change context and risk disclosures.
- [ETFreplay FNDA annual total-return table](https://www.etfreplay.com/etf/fnda) — secondary dividend-adjusted annual rows and volatility cross-check.
- [FinanceCharts FNDA performance table](https://www.financecharts.com/etfs/FNDA/performance) — secondary cross-check; not mixed into canonical official fields.
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached workflow references — common USD Total Return rows, dividends reinvested, as of 2025-12-31.
- [[ETF_performance_sources_2026-08-29]] | [[ETF Performance Index]]
