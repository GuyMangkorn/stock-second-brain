---
type: etf-performance
instrument_type: ETF
entity_key: NASDAQ:VIGI
ticker: VIGI
exchange: Nasdaq
fund: Vanguard International Dividend Appreciation ETF
tracked_index: S&P Global Ex-U.S. Dividend Growers Index (USD) NTR
benchmark: S&P 500 Total Return
management_mode: passive-index-tracking
updated: 2026-08-29
performance_as_of: 2025-12-31
rolling_10y_as_of: 2026-07-31
current_ytd_as_of: 2026-08-26
price_nav_as_of: 2026-08-28
fund_facts_as_of: 2026-07-31
source_batch: raw/imports/ETF_performance_sources_2026-08-29.md
return_basis: NAV total return; income reinvested; net of expenses where source-defined
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/VIGI
  - geography/International
---

# VIGI ETF Performance

> [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

VIGI เป็น passive/index-tracking international equity ETF ของ Vanguard ที่จดทะเบียน
บน Nasdaq และติดตาม S&P Global Ex-U.S. Dividend Growers Index (USD) NTR. Official
Vanguard standardized data ณ 31 ก.ค. 2026 รายงาน NAV Total Return แบบ annualized
ที่ `15.69%` สำหรับ 1 ปี, `10.58%` สำหรับ 3 ปี, `5.32%` สำหรับ 5 ปี และ `8.01%`
สำหรับ 10 ปี; since inception อยู่ที่ `9.12%`. Current official YTD NAV Total Return
อยู่ที่ `+9.18%` ณ 26 ส.ค. 2026 และ market-price YTD อยู่ที่ `+9.01%` วันเดียวกัน.

จาก complete calendar rows 2017-2025 VIGI ให้ cumulative return `116.23%` หรือ
rounded-input CAGR `8.95%`, ต่ำกว่า S&P 500 Total Return common reference ที่
`255.78%` ในช่วงเดียวกัน. Current market price ที่ตรวจได้จาก secondary Schwab
capture คือ `US$98.55` ณ 28 ส.ค. 2026 แต่ current official NAV คู่กันยัง
`ไม่พบข้อมูลที่ยืนยันได้`.

## Performance check

- `entity_key: NASDAQ:VIGI`; Nasdaq listing; inception `2016-02-25`; CUSIP `921946810`.
- Metric: `NAV Total Return` รวมเงินปันผล/การกระจายที่ reinvested และหัก fund expenses ตามนิยามของ issuer; market-price return แยกต่างหาก.
- Classification: `passive-index-tracking`; Vanguard อธิบายกองเป็น fully invested, full-replication equity ETF ที่ลงทุนใน large-cap developed และ emerging markets นอกสหรัฐฯ.
- Issuer benchmark: `S&P Global Ex-U.S. Dividend Growers Index (USD) NTR`. Common reference คือ `S&P 500 Total Return` USD, dividends reinvested; ไม่ใช่ tracked index ของ VIGI และไม่ใช่ evidence ของ manager skill.
- Official standardized window: issuer table ใช้ as-of `2026-07-31`; current YTD field จาก Vanguard advisor page ใช้ as-of `2026-08-26`. Separate Vanguard fund-list capture แสดง YTD `9.80%` ณ `2026-08-11`; ไม่ผสมกับ later current YTD `9.18%`.
- `†` คือ official inception-year partial; complete-year ranking เริ่ม 2017. Annual rows เป็น official Vanguard returns ถึง 2025.

Annual rows มาจาก [Vanguard VIGI product performance](https://investor.vanguard.com/investment-products/etfs/profile/vigi); comparator ใช้ cached S&P 500 TR convention สำหรับ complete calendar years:

| Year | VIGI NAV TR | S&P 500 TR (USD; common ref.) |
|---|---:|---:|
| 2016† | 6.64% | — |
| 2017 | 27.80% | 21.83% |
| 2018 | -11.32% | -4.38% |
| 2019 | 27.04% | 31.49% |
| 2020 | 15.11% | 18.40% |
| 2021 | 12.42% | 28.71% |
| 2022 | -16.71% | -18.11% |
| 2023 | 16.16% | 26.29% |
| 2024 | 2.62% | 25.02% |
| 2025 | 16.89% | 17.88% |

### Calculations and current standardized return

- 2017-2025 annual rows: cumulative `116.23%`, rounded-input CAGR `8.95%`, population standard deviation `14.71%`, positive/negative years `7 / 2`.
- 2021-2025 annual rows: cumulative `30.47%`, rounded-input CAGR `5.46%`, population standard deviation `12.57%`, positive/negative years `4 / 1`.
- Cached S&P 500 TR common reference: 2017-2025 cumulative `255.78%` / CAGR `15.14%`; 2021-2025 cumulative `96.17%` / CAGR `14.43%`. This is a USD reference only, not VIGI's issuer benchmark.
- Latest official July 2026 standardized NAV TR: YTD `9.80%` in a separate 11 ส.ค. fund-list capture, 1-year `15.69%`, 3-year annualised `10.58%`, 5-year `5.32%`, 10-year `8.01%`, and since inception `9.12%`; the current later advisor-page YTD is `9.18%` as of 26 ส.ค. 2026 and is the current field used in the bottom line.
- The issuer's rolling 10-year annualized field `8.01%` implies normalized growth `100.00 → 216.09`, or cumulative `116.09%`, via `100 × ((1 + 0.0801)^10 - 1)`. Raw endpoints are not disclosed; this is a shown calculation, not a sourced NAV endpoint.

**Up years / Down years**

- Best: 2017, **+27.80%**; least positive: 2024, **+2.62%**.
- Worst: 2022, **-16.71%**; least bad down year: 2018, **-11.32%**.
- Current 2026 YTD: **+9.18% NAV TR** and **+9.01% market-price return**, both as of 26 ส.ค. 2026.

## Current fund snapshot

| Field | Value | As of |
|---|---:|---|
| NAV | ไม่พบข้อมูลที่ยืนยันได้ | current official capture did not expose a verified pair |
| Market price | US$98.55 (secondary Schwab) | 2026-08-28 |
| NAV Total Return YTD | 9.18% | 2026-08-26 |
| Market-price return YTD | 9.01% | 2026-08-26 |
| NAV Total Return, 1-year | 15.69% | 2026-07-31 |
| NAV Total Return, 3-year annualised | 10.58% | 2026-07-31 |
| NAV Total Return, 5-year annualised | 5.32% | 2026-07-31 |
| NAV Total Return, 10-year annualised | 8.01% | 2026-07-31 |
| NAV Total Return, since inception annualised | 9.12% | 2026-07-31 |
| ETF net assets | US$9.1B | 2026-07-31 |
| Fund total net assets | US$9.4B | 2026-07-31 |
| Holdings | 341 | 2026-07-31 |
| Net expense ratio | 0.07% | 2026-02-27 |
| Distribution yield | 2.13% | 2026-07-31 |
| Median bid/ask spread | 0.06% | 2026-08-25 |
| 3-year standard deviation | 12.05% | 2026-07-31 |

Current portfolio characteristics from the official Vanguard capture include P/E
`20.7x`, P/B `2.9x`, turnover `13.90%`, developed-market exposure `94.96%`,
emerging-market exposure `5.04%`, and foreign holdings `99.23%`. These are holdings
or fund-profile metrics, not a forecast of future return.

The latest reviewed official factsheet country mix as of 30 มิ.ย. 2026 was Japan
`30.6%`, Canada `23.7%`, Switzerland `14.6%`, United Kingdom `5.3%`, Germany
`5.0%`, India `3.2%`, France `3.2%`, Spain `2.9%`, Denmark `2.8%`, and Hong Kong
`1.7%`. Top ten holdings were RBC `4.9%`, Mitsubishi UFJ `4.3%`, Nestle `3.9%`,
TD `3.7%`, Novartis `3.6%`, Roche `3.5%`, Schneider `3.2%`, SAP `2.8%`, Iberdrola
`2.8%`, and Novo Nordisk `2.8%`, or approximately `35.4%` combined. Sector weights
were Financials `29.1%`, Industrials `16.3%`, Health Care `14.6%`, Technology
`11.4%`, Consumer Staples `8.6%`, Consumer Discretionary `5.9%`, Utilities `5.9%`,
Basic Materials `3.5%`, Energy `2.5%`, Real Estate `1.1%`, and Telecommunications
`1.0%`.

## Risk read-through

VIGI กระจายไป developed/emerging markets นอกสหรัฐฯ แต่ยังมี FX, country/region,
sector และ dividend-factor risk. การกระจาย 341 holdings ลด single-name risk แต่
ไม่ได้ลบความเสี่ยงจาก global equity valuation, foreign-market liquidity หรือ
currency translation. Standard deviation 3 ปีล่าสุดที่ `12.05%` เป็น issuer
snapshot และไม่ใช่ downside guarantee.

Secondary adjusted-price total-return proxy จาก [PortfoliosLab VIGI](https://portfolioslab.com/symbol/VIGI)
รายงาน maximum drawdown ประมาณ `-31.01%` ในช่วง COVID และใช้ `114` trading
sessions เพื่อฟื้นกลับจุดสูงสุดเดิม. ตัวเลขนี้ไม่ใช่ official NAV series; official
daily NAV history ที่เพียงพอสำหรับการ reproduce fund-level drawdown/recovery ยัง
`ไม่พบข้อมูลที่ยืนยันได้`.

## Source reconciliation and follow-up

Prior official June factsheet reported NAV TR YTD `3.70%`, 1-year `6.06%`, and
10-year `7.89%` as of 30 มิ.ย. 2026. Later Vanguard July standardized data raised
the corresponding 1-year/10-year fields to `15.69%`/`8.01%` as of 31 ก.ค., while
the later advisor-page current YTD is `9.18%` as of 26 ส.ค. These are separate
as-of windows and are not mixed into one return period.

The Vanguard fund-list capture separately labels YTD `9.80%` as of 11 ส.ค.; the
later 26 ส.ค. advisor-page observation is retained as the current YTD field. The
official current page did not expose a verified current NAV/market-price pair in
the reviewed capture, so the secondary Schwab market price `US$98.55` is shown
without inventing a premium/discount or current NAV.

Follow-up:

- Capture an official current NAV/closing-price pair and premium/discount when Vanguard exposes it in a stable page or factsheet.
- Locate an official daily NAV total-return series to replace the PortfoliosLab drawdown/recovery proxy.
- Keep future calendar-year rows and current benchmark fields separate from issuer rolling-return fields and current YTD snapshots.

## Sources

- [Vanguard advisor product page](https://advisors.vanguard.com/investments/products/vigi/vanguard-international-dividend-appreciation-etf) — current YTD, market-price YTD, expense, spread, holdings and current portfolio metrics.
- [Vanguard VIGI product page](https://investor.vanguard.com/investment-products/etfs/profile/vigi) — product identity and annual performance source.
- [Vanguard fund list](https://workplace.vanguard.com/fund-list/?filters=eqIndex%2C&viewType=monthEndReturnNAV) — July standardized average annual returns and separately dated YTD field.
- [Vanguard VIGI factsheet](https://fund-docs.vanguard.com/F4415.pdf) — June 2026 performance cross-check, benchmark, strategy, holdings, country/sector mix and risk fields.
- [Schwab VIGI report](https://www.schwab.wallst.com/schwab/Prospect/research/etfs/reports/reportRetrieve.asp?reportType=etfrc&symbol=VIGI) — secondary current market price and rounded standardized cross-check.
- [S&P Global Ex-U.S. Dividend Growers Index](https://www.spglobal.com/spdji/en/indices/dividends-factors/sp-global-ex-us-dividend-growers-index/) — issuer benchmark identity.
- [S&P Dividend Growers Index Series Methodology](https://www.spglobal.com/spdji/en/documents/methodologies/methodology-sp-dividend-growers-index-series.pdf) — index methodology context.
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached workflow references — common USD Total Return rows, dividends reinvested, as of 2025-12-31.
- [PortfoliosLab VIGI](https://portfolioslab.com/symbol/VIGI) — secondary adjusted-price drawdown/recovery proxy.
- [[ETF_performance_sources_2026-08-29]] | [[ETF Performance Index]]
