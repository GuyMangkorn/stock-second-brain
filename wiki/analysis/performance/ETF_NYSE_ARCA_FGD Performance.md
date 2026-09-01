---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:FGD
input_ticker: FGD
ticker: FGD
exchange: NYSE Arca
fund: First Trust Dow Jones Global Select Dividend Index Fund
tracked_index: Dow Jones Global Select Dividend Index
benchmark: S&P 500 Total Return
issuer_benchmark: Dow Jones Global Select Dividend Index
management_mode: passive-index
active_process: not applicable
management_benchmark: not applicable
track_record: established
management_evidence: not applicable
risk_evidence: issuer-fields; daily-NAV-drawdown-not-verified
updated: 2026-09-01
performance_as_of: 2025-12-31 (calendar) / 2026-06-30 (rolling) / 2026-08-28 (price/NAV)
calendar_years_as_of: 2025-12-31 (official factsheet dated 2026-06-30)
rolling_10y_as_of: 2026-06-30
current_ytd_as_of: 2026-06-30
price_nav_as_of: 2026-08-28
fund_facts_as_of: 2026-07-31 (yield) / 2026-08-03 (holdings) / 2026-08-28 (price/NAV)
source_batch: raw/imports/ETF_performance_sources_2026-09-01_run-4.md
return_basis: NAV total return; distributions included; net of fund expenses
return_currency: USD
primary_region: International
tags:
  - analysis/etf-performance
  - ticker/FGD
  - geography/International
  - style/dividend
---

# FGD Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

FGD คือ First Trust Dow Jones Global Select Dividend Index Fund บน NYSE Arca
เป็น `passive-index` global developed-market equity ETF ที่ track `Dow Jones
Global Select Dividend Index` ซึ่งคัดหุ้น dividend-paying ผ่าน quality และ
liquidity screens แล้วเลือก 100 หุ้นโดยใช้ indicated dividend yield weighting.
Official closing NAV/market price อยู่ที่ `$35.61 / $35.63` ณ 28 ส.ค. 2026 และ
NAV YTD ที่มีคู่ benchmark แบบ synchronized ล่าสุดคือ `7.37%` ณ 30 มิ.ย. 2026.

จาก official NAV total-return rows ครบปี 2016-2025 FGD ให้ cumulative `143.22%`
และ rounded-input CAGR `9.30%`, เทียบกับ S&P 500 Total Return ที่ `298.33%`
และ `14.82%` CAGR. ช่วง 2021-2025 FGD ให้ cumulative `84.60%` และ CAGR
`13.04%`; ตัวเลขนี้เป็น passive implementation outcome ไม่ใช่หลักฐาน
manager skill.

## Performance check

- `entity_key: NYSE Arca:FGD`; inception `2007-11-21`; CUSIP `33734X200`; ISIN `US33734X2009`; asset class `Equity`.
- Fund objective คือให้ผลตอบแทนสอดคล้องโดยทั่วไปกับ price และ yield ของ `Dow Jones Global Select Dividend Index` ก่อนค่าธรรมเนียม; index rebalance/reconstitute รายปี และ fund ปกติลงทุนอย่างน้อย 90% ใน index securities.
- Index universe มาจาก developed-market country sub-indices ของ S&P Global Broad Market Index โดย exclude REITs; quality screens รวมการจ่ายปันผล 5 ปี, dividend-per-share ratio, dividend coverage, non-negative trailing EPS และ size/liquidity.
- Expense ratio `0.55%`; contractual expense cap `0.60%` อย่างน้อยถึง 31 ม.ค. 2027.
- Official price-history snapshot ณ 28 ส.ค. 2026: market price `$35.63`, NAV `$35.61`, midpoint `$35.61`, volume `118,105`, net assets `$1,646.8m`. Holdings `99` ณ 3 ส.ค. 2026.
- Official fund facts ณ 31 ก.ค. 2026: 30-day SEC yield `4.76%`, 12-month distribution rate `5.04%`, index yield `5.95%`. ณ 30 มิ.ย. 2026 P/E `11.12x`, P/B `1.17x`.

## Official rolling performance

Official First Trust rows are synchronized at 30 มิ.ย. 2026. The tracked-index
row is kept separate from broad developed-market references.

| Period | FGD NAV TR | FGD market price TR | Dow Jones Global Select Dividend Index | Dow Jones World Developed Markets Index | MSCI World Index | As of |
|---|---:|---:|---:|---:|---:|---|
| YTD | 7.37% | 7.70% | 7.58% | 11.71% | 9.69% | 2026-06-30 |
| 1 year | 22.81% | 22.88% | 23.35% | 24.07% | 21.34% | 2026-06-30 |
| 3 years annualized | 20.78% | 20.86% | 20.97% | 19.97% | 19.24% | 2026-06-30 |
| 5 years annualized | 10.60% | 10.58% | 10.70% | 11.56% | 11.47% | 2026-06-30 |
| 10 years annualized | 9.55% | 9.59% | 9.80% | 13.25% | 13.14% | 2026-06-30 |
| Since inception annualized | 5.77% | 5.78% | 5.92% | 8.64% | 8.33% | 2026-06-30 |

Rolling fund-minus-tracked-index spreads are `-0.21 pp` YTD, `-0.54 pp` for
1-year, `-0.19 pp` annualized for 3-year, `-0.10 pp` annualized for 5-year,
`-0.25 pp` annualized for 10-year and `-0.15 pp` annualized since inception.
These are implementation/tracking observations; arithmetic excess return is
not called alpha.

## Calendar-year performance

The official FGD factsheet provides the fund and broad reference-index rows
below, but does not provide a 2016-2025 calendar table for the tracked Dow Jones
Global Select Dividend Index. Therefore no annual tracked-index hit rate is
inferred.

| Year | FGD NAV TR | Dow Jones World Developed Markets Index | MSCI World Index | S&P 500 TR (USD reference) |
|---|---:|---:|---:|---:|
| 2016 | 11.80% | 8.11% | 7.51% | 11.96% |
| 2017 | 17.62% | 23.32% | 22.40% | 21.83% |
| 2018 | -12.40% | -9.20% | -8.71% | -4.38% |
| 2019 | 19.88% | 27.38% | 27.67% | 31.49% |
| 2020 | -4.59% | 16.42% | 15.90% | 18.40% |
| 2021 | 20.41% | 20.59% | 21.82% | 28.71% |
| 2022 | -6.98% | -18.25% | -18.14% | -18.11% |
| 2023 | 8.19% | 23.50% | 23.79% | 26.29% |
| 2024 | 5.63% | 17.50% | 18.67% | 25.02% |
| 2025 | 44.22% | 22.17% | 21.09% | 17.88% |

From the official FGD rows, 2016-2025 product is `2.4322404021`, cumulative
return `143.2240%`, rounded-input CAGR `9.2951%`, and population standard
deviation `15.6914%`. The cached S&P 500 reference product is `3.9832911148`,
cumulative `298.3291%`, and CAGR `14.8218%`; relative wealth of FGD versus S&P
is `-38.9389%`. MSCI World product is `3.1531955215`, cumulative `215.3196%`,
and CAGR `12.1696%`.

For 2021-2025, FGD product is `1.8460301227`, cumulative `84.6030%`, CAGR
`13.0441%`, and population standard deviation `17.3083%`; S&P reference CAGR is
`14.4264%`, and relative wealth is `-5.8962%`.

## Up years / down years

- Complete calendar years available: `10`.
- Up/down among complete years: `7 / 3`.
- Best complete year: 2025, `+44.22%`.
- Least positive complete year: 2024, `+5.63%`.
- Worst down year: 2018, `-12.40%`.
- Least bad down year: 2022, `-6.98%`.

## Risk read-through

FGD has global dividend and value-style exposure with meaningful financials
concentration. Official fields as of 30 มิ.ย. 2026 report standard deviation
`12.39%`, beta `0.68`, Sharpe ratio `1.23`, and correlation `0.69` versus MSCI
World. The issuer also displays an `Alpha 5.72` field; it is not used here as
manager-skill evidence because FGD is an index fund and the field's methodology
is not independently reconstructed.

As of 3 ส.ค. 2026, top sectors were Financials `36.83%`, Industrials `13.43%`,
Consumer Discretionary `10.45%`, Energy `9.24%`, and Communication Services
`8.19%`. Key risks include dividend cuts, financial-sector and country
concentration, foreign currency/market exposure, Asia and Europe risk, index
methodology changes, liquidity, and ETF premium/discount or bid-ask spread.
Daily NAV maximum drawdown and exact recovery duration remain
`ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- [First Trust FGD official fund summary](https://www.ftportfolios.com/Retail/etf/etfsummary.aspx?Ticker=FGD) — objective, index methodology, current fund facts, rolling performance, risk fields and portfolio data.
- [First Trust FGD official factsheet, 30 June 2026](https://www.ftportfolios.com/Common/ContentFileLoader.aspx?ContentGUID=978c0ace-c2ed-4b33-a779-bb829f1e4631) — official calendar-year rows, rolling returns, fund facts, index description and risk fields.
- [First Trust FGD official price history](https://www.ftportfolios.com/Retail/Etf/EtfPriceHistory.aspx?Ticker=FGD) — 28 Aug. 2026 market price, NAV, midpoint, volume and net assets.
- [First Trust FGD summary prospectus](https://www.ftportfolios.com/Funds/ETF/Prospectus/FAN) — index-fund strategy, expenses and principal risks.
- [First Trust Dow Jones Global Select Dividend Index components](https://www.ftportfolios.com/Retail/Index/IndexComponents.aspx?IndexID=84) — official index component/methodology reference.
- [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common USD Total Return reference convention.
- [[ETF_performance_sources_2026-09-01_run-4]] | [[ETF Performance Index]]
