---
type: etf-performance
instrument_type: ETF
entity_key: NASDAQ:VYMI
ticker: VYMI
exchange: Nasdaq
fund: Vanguard International High Dividend Yield ETF
tracked_index: FTSE All-World ex US High Dividend Yield Index
benchmark: S&P 500 Total Return
management_mode: passive-index-tracking
updated: 2026-08-29
performance_as_of: 2025-12-31
rolling_10y_as_of: 2026-07-31
current_ytd_as_of: 2026-08-26
price_nav_as_of: 2026-08-24
fund_facts_as_of: 2026-07-31
source_batch: raw/imports/ETF_performance_sources_2026-08-29.md
return_basis: NAV total return; income reinvested; net of expenses where source-defined
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/VYMI
  - geography/International
---

# VYMI ETF Performance

> [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

VYMI เป็น passive/index-tracking international high-dividend equity ETF ของ
Vanguard ที่จดทะเบียนบน Nasdaq และติดตาม FTSE All-World ex US High Dividend Yield
Index. Official Vanguard standardized data ณ 31 ก.ค. 2026 รายงาน NAV Total Return
แบบ annualized ที่ `34.56%` สำหรับ 1 ปี, `21.47%` สำหรับ 3 ปี, `14.05%` สำหรับ
5 ปี, `10.98%` สำหรับ 10 ปี และ `11.68%` ตั้งแต่จัดตั้ง. Current official YTD NAV
Total Return อยู่ที่ `+19.86%` ณ 26 ส.ค. 2026.

จาก complete calendar rows 2017-2025 VYMI ให้ cumulative return `132.81%` หรือ
rounded-input CAGR `9.84%`. Common window 2021-2025 ให้ cumulative `84.75%` หรือ
CAGR `13.06%`, ต่ำกว่า S&P 500 Total Return common reference ที่ `96.17%` ในช่วง
เดียวกัน. Secondary Schwab capture แสดง market price `US$105.17` ณ 24 ส.ค. 2026;
current official NAV คู่กันยัง `ไม่พบข้อมูลที่ยืนยันได้`.

## Performance check

- `entity_key: NASDAQ:VYMI`; Nasdaq listing; inception `2016-02-25`; CUSIP `921946794`.
- Metric: `NAV Total Return` รวมเงินปันผล/การกระจายที่ reinvested และหัก fund expenses ตามนิยามของ issuer; market-price return แยกต่างหาก.
- Classification: `passive-index-tracking`; Vanguard อธิบายกองว่าใช้ sampling strategy, remain fully invested และเน้น large-/mid-cap developed และ emerging markets นอกสหรัฐฯ ที่คาดว่าจะมี dividend yield สูงกว่าค่าเฉลี่ย.
- Issuer benchmark: `FTSE All-World ex US High Dividend Yield Index` (`GPVAN0TR`). Common reference คือ `S&P 500 Total Return` USD, dividends reinvested; ไม่ใช่ tracked index ของ VYMI และไม่ใช่ evidence ของ manager skill.
- Official standardized window: 1/3/5/10-year และ since-inception fields ใช้ as-of `2026-07-31`; current YTD field จาก Vanguard advisor page ใช้ as-of `2026-08-26`. Separate Vanguard fund-list capture แสดง YTD `18.37%` ณ `2026-08-11`; ไม่ผสมกับ later current YTD `19.86%`.
- `†` คือ official inception-year partial; complete-year ranking เริ่ม 2017. Annual rows เป็น official Vanguard returns ถึง 2025.

Annual rows มาจาก [Vanguard VYMI product performance](https://investor.vanguard.com/investment-products/etfs/profile/vymi); comparator ใช้ cached S&P 500 TR convention สำหรับ complete calendar years:

| Year | VYMI NAV TR | S&P 500 TR (USD; common ref.) |
|---|---:|---:|
| 2016† | 15.75% | 11.96% |
| 2017 | 22.37% | 21.83% |
| 2018 | -12.39% | -4.38% |
| 2019 | 18.31% | 31.49% |
| 2020 | -0.65% | 18.40% |
| 2021 | 15.00% | 28.71% |
| 2022 | -6.90% | -18.11% |
| 2023 | 16.88% | 26.29% |
| 2024 | 6.97% | 25.02% |
| 2025 | 38.02% | 17.88% |

### Calculations and current standardized return

- 2017-2025 annual rows: cumulative `132.81%`, rounded-input CAGR `9.84%`, population standard deviation `14.84%`, positive/negative years `6 / 3`.
- 2021-2025 annual rows: cumulative `84.75%`, rounded-input CAGR `13.06%`, population standard deviation `14.65%`, positive/negative years `4 / 1`.
- Cached S&P 500 TR common reference: 2017-2025 cumulative `255.78%` / CAGR `15.14%`; 2021-2025 cumulative `96.17%` / CAGR `14.43%`. This is a USD reference only, not VYMI's issuer benchmark.
- Latest official July 2026 standardized NAV TR: 1-year `34.56%`, 3-year annualised `21.47%`, 5-year `14.05%`, 10-year `10.98%`, and since inception `11.68%`; the separate fund-list YTD is `18.37%` as of 11 ส.ค. 2026. The later current advisor-page YTD is `19.86%` as of 26 ส.ค. 2026 and is the current field used in the bottom line.
- The issuer's rolling 10-year annualized field `10.98%` implies normalized growth `100.00 → 283.43`, or cumulative `183.43%`, via `100 × ((1 + 0.1098)^10 - 1)`. Raw endpoints are not disclosed; this is a shown calculation, not a sourced NAV endpoint.

**Up years / Down years**

- Best: 2025, **+38.02%**; least positive: 2024, **+6.97%**.
- Worst: 2018, **-12.39%**; least bad down year: 2022, **-6.90%**.
- Current 2026 YTD: **+19.86% NAV TR**, as of 26 ส.ค. 2026.

## Current fund snapshot

| Field | Value | As of |
|---|---:|---|
| NAV | ไม่พบข้อมูลที่ยืนยันได้ | current official capture did not expose a verified pair |
| Market price | US$105.17 (secondary Schwab) | 2026-08-24 |
| NAV Total Return YTD | 19.86% | 2026-08-26 |
| NAV Total Return, 1-year | 34.56% | 2026-07-31 |
| NAV Total Return, 3-year annualised | 21.47% | 2026-07-31 |
| NAV Total Return, 5-year annualised | 14.05% | 2026-07-31 |
| NAV Total Return, 10-year annualised | 10.98% | 2026-07-31 |
| NAV Total Return, since inception annualised | 11.68% | 2026-07-31 |
| ETF net assets | US$21.0B | 2026-07-31 |
| Fund total net assets | US$21.9B | 2026-07-31 |
| Holdings | 1,565 | 2026-06-30 |
| Net expense ratio | 0.07% | 2026-02-27 |
| Dividend yield | 3.69% | 2026-07-31 |
| Median bid/ask spread | 0.01% | 2026-08-26 |
| 3-year standard deviation | 11.27% | 2026-06-30 |

Official June portfolio characteristics include developed-market exposure `77.61%`,
emerging-market exposure `22.39%`, foreign holdings `99.34%`, median market cap
`US$65.0B`, P/E `14.1x`, P/B `1.7x`, ROE `13.0%`, earnings growth `9.9%`, and
turnover `8.8%`. These are fund/holdings metrics, not a forecast of future return.

The latest reviewed official factsheet country mix as of 30 มิ.ย. 2026 was Japan
`11.5%`, United Kingdom `11.0%`, Canada `9.2%`, Switzerland `7.6%`, Australia
`7.3%`, Taiwan `5.8%`, China `5.5%`, France `5.5%`, Spain `4.4%`, and Germany
`4.3%`. Top ten holdings were HSBC `1.8%`, Roche `1.7%`, Novartis `1.6%`, Royal
Bank of Canada `1.6%`, Nestle `1.5%`, Shell `1.2%`, Mitsubishi UFJ `1.2%`, BHP
`1.2%`, Toronto-Dominion Bank `1.1%`, and Banco Santander `1.1%`, or approximately
`13.8%` combined. Sector weights were Financials `43.7%`, Energy `8.3%`, Consumer
Staples `6.9%`, Consumer Discretionary `6.7%`, Health Care `6.6%`, Industrials
`6.2%`, Basic Materials `6.1%`, Utilities `5.6%`, Technology `5.1%`,
Telecommunications `3.6%`, and Real Estate `1.0%`.

Official Vanguard distribution data shows the latest two 2026 income payments of
`US$1.256900` payable 23 มิ.ย. and `US$0.708000` payable 24 มี.ค., totaling
`US$1.964900` per share; these are distributions, not NAV Total Return.

## Risk read-through

VYMI เป็น international value/high-dividend exposure ที่มี Financials ประมาณ
`43.7%` และ emerging-market exposure `22.39%` ใน official June snapshot. ความเสี่ยง
หลักจึงรวม FX, country/region, financials/energy/sector concentration, dividend
factor, emerging-market liquidity และ valuation-regime rotation. การถือหุ้น 1,565
ตัวช่วยลด single-name risk แต่ไม่ได้ลบ equity drawdown หรือ currency risk.

Secondary adjusted-price total-return series จาก [PortfoliosLab VYMI](https://portfolioslab.com/symbol/VYMI)
รายงาน maximum drawdown `-40.00%` เมื่อ 23 มี.ค. 2020 และ recovery ใน `202`
trading sessions. ตัวเลขนี้ไม่ใช่ official NAV series; official daily NAV history
ที่เพียงพอสำหรับการ reproduce fund-level drawdown/recovery ยัง
`ไม่พบข้อมูลที่ยืนยันได้`.

## Source reconciliation and follow-up

Prior official June factsheet reported NAV TR YTD `11.49%`, 1-year `27.47%`, and
10-year `10.82%` as of 30 มิ.ย. 2026. The later Vanguard fund-list capture reports
the July standardized 1/3/5/10-year and since-inception fields of `34.56%`,
`21.47%`, `14.05%`, `10.98%`, and `11.68%`; its separate YTD field is `18.37%` as
of 11 ส.ค. The later advisor-page current YTD is `19.86%` as of 26 ส.ค. These are
separate as-of windows and are not mixed into one return period.

The reviewed official current page did not expose a verified current NAV/market-price
pair, so the secondary Schwab price `US$105.17` as of 24 ส.ค. is shown without
inventing a premium/discount or current NAV. Current official benchmark YTD was not
exposed in the same capture.

Follow-up:

- Capture an official current NAV/closing-price pair and premium/discount when Vanguard exposes it in a stable page or factsheet.
- Locate an official daily NAV total-return series to replace the PortfoliosLab drawdown/recovery proxy.
- Keep future calendar-year rows and current benchmark fields separate from issuer rolling-return fields and current YTD snapshots.

## Sources

- [Vanguard advisor product page](https://advisors.vanguard.com/investments/products/vymi/vanguard-international-high-dividend-yield-etf) — current YTD, rolling-return summary, expense, yield, spread, assets and strategy facts.
- [Vanguard VYMI product page](https://investor.vanguard.com/investment-products/etfs/profile/vymi) — product identity and annual performance source.
- [Vanguard fund list](https://workplace.vanguard.com/fund-list/?filters=etf) — July standardized average annual returns and separately dated YTD field.
- [Vanguard VYMI factsheet](https://workplace.vanguard.com/assets/corp/fund_communications/pdf_publish/us-products/fact-sheet/F4430.pdf) — June 2026 performance/index cross-check, holdings, country/sector mix and risk fields.
- [Schwab VYMI report](https://www.schwab.wallst.com/schwab/Prospect/research/etfs/reports/reportRetrieve.asp?reportType=etfrc&symbol=VYMI) — secondary current price and rounded standardized cross-check.
- [PortfoliosLab VYMI](https://portfolioslab.com/symbol/VYMI) — secondary adjusted-price drawdown/recovery proxy.
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached workflow references — common USD Total Return rows, dividends reinvested, as of 2025-12-31.
- [[ETF_performance_sources_2026-08-29]] | [[ETF Performance Index]]
