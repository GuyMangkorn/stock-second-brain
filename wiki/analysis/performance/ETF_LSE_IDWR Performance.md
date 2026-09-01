---
type: etf-performance
instrument_type: ETF
entity_key: LSE:IDWR
input_ticker: IIREF
ticker: IDWR
exchange: London Stock Exchange
fund: iShares MSCI World UCITS ETF USD (Dist)
tracked_index: MSCI World Index (Net)
benchmark: S&P 500 Total Return
management_mode: passive-index
implementation: physical-optimised
updated: 2026-09-01
performance_as_of: 2025-12-31 (calendar) / 2026-05-31 (factsheet rolling)
current_ytd_as_of: 2026-08-28
market_price_as_of: 2026-08-31 (secondary intraday)
nav_as_of: 2026-08-28
fund_facts_as_of: 2026-08-28
source_batch: raw/imports/ETF_performance_sources_2026-09-01_run-4.md
return_basis: NAV total return; gross income reinvested; net of fund expenses
return_currency: USD
primary_region: International
tags:
  - analysis/etf-performance
  - ticker/IIREF
  - ticker/IDWR
  - geography/International
  - geography/global-developed
  - style/passive-index
---

# IIREF / IDWR Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

`IIREF` เป็น OTC input alias ของ iShares MSCI World UCITS ETF USD (Dist) โดย
official iShares ระบุ ISIN `IE00B0M62Q58` และ USD listing บน London Stock
Exchange เป็น `IDWR`; หน้า issuer ใช้ `IWRD` เป็นชื่อกอง/GBP line และแสดง
`IDWR` แยกเป็น USD line. จึงใช้ `LSE:IDWR` เป็น canonical entity เพื่อให้
currency ของ listing ตรงกับ input alias ที่มีการ quote เป็น USD.

กองทุนเป็น passive, physical/optimised, distributing equity UCITS ETF ที่ติดตาม
`MSCI World Index (Net)` และมี total expense ratio `0.50%`. Official iShares
product page ระบุ NAV `US$106.25` และ NAV Total Return YTD `13.27%` ณ
28 ส.ค. 2026. Official calendar rows 2016-2025 ให้ cumulative `209.01%` และ
rounded-input CAGR `11.94%`; benchmark ให้ `215.32%` / `12.17%`. Common USD
reference คือ S&P 500 Total Return ที่ `298.33%` / `14.82%` ใน window เดียวกัน.

## Performance check

- `entity_key: LSE:IDWR`; `input_ticker: IIREF` (OTC alias); official USD listing: `London Stock Exchange:IDWR`; ISIN `IE00B0M62Q58`
- Fund launch/share-class launch: 28 ต.ค. 2005; issuer: iShares plc; domicile: Ireland; UCITS: yes
- Classification: `passive-index`; implementation `physical` with `optimised` methodology; no leverage, inverse, option-income or derivative-defined payoff identified
- Primary metric: issuer `NAV Total Return` in USD, with gross income reinvested where applicable and fund costs reflected in NAV; market-price return is not mixed
- Tracked index / strategy-aligned benchmark: `MSCI World Index (Net)`; common comparison below is S&P 500 Total Return in USD only
- Expense ratio: `0.50%`; income: distributing quarterly; current official NAV/YTD snapshot: `US$106.25` / `13.27%` as of 28 ส.ค. 2026
- Latest secondary IDWR market snapshot: `US$106.16` at 10:32 BST on 31 ส.ค. 2026; 28 ส.ค. closing price `US$106.79`. These are market-price observations, not NAV return inputs.

Official rolling snapshot from the May 2026 factsheet (as of 31 พ.ค. 2026):

| Period | IDWR NAV TR | MSCI World Net |
|---|---:|---:|
| YTD | 10.06% | 10.26% |
| 1 year | 20.03% | 20.41% |
| 3 years annualized | 17.84% | 18.14% |
| 5 years annualized | 10.93% | 11.19% |
| Since inception annualized | 8.83% | 9.04% |

The newer official product-page YTD field of `13.27%` as of 28 ส.ค. 2026 is kept
separate from the older factsheet snapshot. The calendar-row CAGR below is not
described as a rolling 10-year issuer field.

## Calendar performance

Official iShares calendar-year rows are NAV total returns in USD. S&P 500 rows
are the cached USD Total Return convention and are a common reference only, not
the tracked index of IDWR.

| Year | IDWR NAV TR (USD) | MSCI World Net (USD) | S&P 500 TR (USD reference) |
|---|---:|---:|---:|
| 2016 | 7.51% | 7.51% | 11.96% |
| 2017 | 22.26% | 22.40% | 21.83% |
| 2018 | -8.89% | -8.71% | -4.38% |
| 2019 | 27.35% | 27.67% | 31.49% |
| 2020 | 15.59% | 15.90% | 18.40% |
| 2021 | 21.49% | 21.82% | 28.71% |
| 2022 | -18.31% | -18.14% | -18.11% |
| 2023 | 23.55% | 23.79% | 26.29% |
| 2024 | 18.39% | 18.67% | 25.02% |
| 2025 | 20.75% | 21.09% | 17.88% |

Calculations from the rounded official rows:

- 2016-2025 IDWR product `3.0901022540`, cumulative `209.0102%`, rounded-input CAGR `11.9431%`, population standard deviation `14.3544%`.
- 2016-2025 MSCI World Net product `3.1531955215`, cumulative `215.3196%`, CAGR `12.1696%`; the approximately `-0.23 pp` CAGR difference is a return-only tracking observation, not alpha.
- 2021-2025 IDWR product `1.7528886858`, cumulative `75.2889%`, rounded-input CAGR `11.8796%`; MSCI World Net product `1.7738836057`, cumulative `77.3884%`, CAGR `12.1463%`.
- Cached S&P 500 TR: 2016-2025 product `3.9832911148`, cumulative `298.3291%`, CAGR `14.8218%`; 2021-2025 cumulative `96.1696%`, CAGR `14.4264%`.

## Up years / Down years

- Complete 2016-2025 NAV TR up/down: `8 / 2`
- Best NAV TR year: 2019, `+27.35%`
- Least positive year: 2016, `+7.51%`
- Worst NAV TR year: 2022, `-18.31%`
- Least bad down year: 2018, `-8.89%`
- 2021-2025 up/down: `4 / 1`; the 2022 drawdown was the only down year in that sub-window

## Risk read-through

Official iShares current snapshot as of 28 ส.ค. 2026 reports net assets
approximately `US$9.564bn`, `1,282` holdings, P/E `26.46x`, P/B `4.15x`, and
12-month trailing distribution yield `0.85%`. Official 3-year standard deviation
is `12.44%` and beta `1.000`, both as of 31 ก.ค. 2026. Information Technology
was `29.55%`, Financials `16.52%`, and Industrials `11.21%` of market value as of
28 ส.ค. 2026.

ความเสี่ยงหลักคือ global developed-market equity drawdown, U.S./mega-cap and
technology concentration, country/sector allocation, foreign-currency exposure
สำหรับผู้ลงทุนที่ไม่ได้ใช้ USD, premium/discount ของแต่ละ listing, tracking
difference, securities-lending/counterparty risk และภาษีจากการจ่าย distribution.
Optimised replication อาจทำให้ผลตอบแทนแตกต่างจาก index; quarterly distribution
ทำให้ market-price total return ของผู้ถือขึ้นกับการนำเงินปันผลกลับไปลงทุนด้วย.

Daily NAV history ที่ยืนยันได้สำหรับ maximum drawdown, recovery duration,
downside capture และ risk-adjusted persistence ยัง `ไม่พบข้อมูลที่ยืนยันได้`;
จึงไม่ใช้ OTC price history เป็น proxy ของ NAV risk.

## Passive implementation read-through

- `management_mode`: `passive-index`; ไม่มี management-skill evidence ที่ควรแยกจาก implementation outcome
- `tracked_index`: `MSCI World Index (Net)` เป็น benchmark ที่ตรงกับ objective ของ issuer
- 2016-2025 fund CAGR `11.94%` ต่ำกว่า index CAGR `12.17%` ราว `0.23 pp`; 2021-2025 fund CAGR `11.88%` ต่ำกว่า `12.15%` ราว `0.27 pp`
- ผลต่างเป็นเพียง tracking observation จาก fees, sampling, trading, securities lending และ valuation timing; ไม่เรียกว่า alpha

## Sources

- [iShares IWRD/IDWR official product page](https://www.ishares.com/uk/individual/en/products/251881/ishares-msci-world-ucits-etf) — official fund identity, ISIN, USD/GBP listings, NAV/YTD, fees, structure, benchmark, holdings and risk snapshot
- [iShares IWRD factsheet, May 2026](https://www.ishares.com/uk/individual/en/literature/fact-sheet/iwrd-ishares-msci-world-ucits-etf-fund-fact-sheet-en-gb.pdf?siteEntryPassthrough=true) — official 2016-2025 calendar rows, May 2026 rolling returns, return definition and trading information
- [iShares USD distributing KIID](https://www.ishares.com/uk/individual/en/literature/kiid/ucits_kiid-ishares-msci-world-ucits-etf-usd-dist-gb-ie00b0m62q58-en.pdf?siteEntryPassthrough=true&switchLocale=y) — passive objective, USD distributing class, benchmark and risk/charge description
- [OTC IIREF profile](https://stockanalysis.com/quote/otc/IIREF/history/) — secondary input-alias/name and USD-quote cross-check only; not primary NAV performance evidence
- [Secondary IDWR market data](https://markets.investorschronicle.markitdigital.com/data/etfs/tearsheet/historical?s=IDWR%3ALSE%3AUSD) — latest secondary market-price observation; not mixed into NAV returns
- [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and the cached source-batch convention — common USD Total Return reference
- [[ETF_performance_sources_2026-09-01_run-4]] | [[ETF Performance Index]]
