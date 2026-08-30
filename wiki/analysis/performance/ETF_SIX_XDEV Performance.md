---
type: etf-performance
instrument_type: ETF
entity_key: SIX Swiss Exchange:XDEV
input_ticker: XDEVF
ticker: XDEV
exchange: SIX Swiss Exchange
fund: Xtrackers MSCI World Value UCITS ETF 1C
tracked_index: MSCI World Enhanced Value (USD) Index (TRN)
benchmark: MSCI World Enhanced Value (USD) Index (TRN)
management_mode: passive-index-tracking
updated: 2026-08-30
performance_as_of: 2025-12-31
current_ytd_as_of: 2026-08-27
market_price_as_of: 2026-08-27
nav_as_of: 2026-07-31
fund_facts_as_of: 2026-07-31
source_batch: raw/imports/ETF_performance_sources_2026-08-30.md
return_basis: official share-class total return; reinvested dividends; net of fund fees
return_currency: USD
tags:
  - analysis/etf-performance
  - geography/International
  - ticker/XDEV
  - ticker/XDEVF
  - geography/developed-markets
  - style/passive-index
  - theme/value
---

# XDEVF / XDEV ETF Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

XDEVF เป็น OTC input alias ของ official USD listing SIX Swiss Exchange:XDEV
สำหรับ Xtrackers MSCI World Value UCITS ETF 1C, ISIN IE00BL25JM42. กองทุนเป็น
passive, rules-based smart-beta, physically replicated และ accumulating โดยติดตาม
MSCI World Enhanced Value (USD) Index (TRN) และมี annual fee 0.25%.

Official DWS factsheet ณ 31 ก.ค. 2026 ระบุ share-class/fund currency เป็น USD,
NAV 82.83 ดอลลาร์, fund AUM 4.43 พันล้านดอลลาร์, shares outstanding 53.44
ล้านหุ้น และ index constituents 401. DWS ระบุว่า official USD line อยู่ที่ SIX
Swiss Exchange ภายใต้ XDEV SW; จึงใช้ SIX Swiss Exchange:XDEV เป็น canonical
entity แม้ Trello input จะเป็น OTC ticker XDEVF.

Official DWS past-performance document รายงาน complete calendar rows 2016-2025
โดย 2016 เป็น combined year ระหว่าง DB Equity Value Factor Index เดิมกับ MSCI
World Enhanced Value Index หลังเปลี่ยน objective วันที่ 3 พ.ย. 2016. จาก rounded
official rows กองทุนมี cumulative return 155.99% และ CAGR 9.86% ใน 2016-2025;
ช่วง 2021-2025 cumulative 89.98% และ CAGR 13.70%. Current YTD ที่อ่านได้จาก
secondary source คือ 36.97% ณ 27 ส.ค. 2026; ไม่แทน official current YTD.

## Performance check

- Identity: Xtrackers MSCI World Value UCITS ETF 1C; ISIN IE00BL25JM42; official USD listing SIX Swiss Exchange:XDEV; Trello input XDEVF เป็น OTC alias
- Classification: supported passive/index-tracking equity UCITS ETF; DWS ระบุ direct physical replication, capitalizing income และ rules-based smart-beta methodology
- Metric: official share-class total return หัก fund fees แล้วและรวม reinvested dividends; return currency คือ USD; market-price return แยกจาก NAV return
- Issuer benchmark: MSCI World Enhanced Value (USD) TR net; large- and mid-cap developed-market value strategy, reviewed semi-annually
- Fund facts as of 2026-07-31: NAV USD 82.83, AUM USD 4.43B, shares outstanding 53.44M, index constituents 401, annual fee 0.25%
- Secondary current fields as of 2026-08-27: YTD 36.97%*, 1-year 54.56%*, 3-year 29.46% annualized*, 5-year 17.39% annualized*, and 10-year 12.42% annualized*; secondary close price was USD 84.27*
- Official current NAV TR YTD was not readable in a directly comparable USD issuer performance field. The DWS Italian NAV page displayed 72.36 on 2026-08-27 without an explicit currency; it is not used for USD return calculation because the page is locale-formatted and the share-class currency is USD
- Risk-adjusted statistics, maximum drawdown, recovery duration, downside capture and daily-NAV persistence: ไม่พบข้อมูลที่ยืนยันได้จาก reviewed official sources

| Period | XDEV share-class TR (USD) | MSCI World Enhanced Value TR net (USD) | Return-only difference |
|---|---:|---:|---:|
| 1-year as of 2026-08-27 | 54.56%* | not disclosed in the secondary source | not applicable |
| 3-year annualized as of 2026-08-27 | 29.46%* | not disclosed in the secondary source | not applicable |
| 5-year annualized as of 2026-08-27 | 17.39%* | not disclosed in the secondary source | not applicable |
| 10-year annualized as of 2026-08-27 | 12.42%* | not disclosed in the secondary source | not applicable |
| 2026 YTD as of 2026-08-27 | 36.97%* | not disclosed in the secondary source | not applicable |

* Current rolling fields are secondary figures and are not mixed with the official
  DWS calendar rows below. They are retained for monitoring only.

## Calendar performance

Official DWS past-performance rows for the share class include reinvested
dividends and deduct fund costs. The benchmark row is unavailable for 2016
because that year combines the former DB Equity Value Factor Index and the
post-change MSCI World Enhanced Value Index.

| Year | XDEV share-class TR (USD) | MSCI World Enhanced Value TR net (USD) | S&P 500 TR (USD; common ref.) |
|---|---:|---:|---:|
| 2016 | 12.10% | not available; combined/splice year | 11.96% |
| 2017 | 22.30% | 22.20% | 21.83% |
| 2018 | -14.40% | -14.40% | -4.38% |
| 2019 | 19.60% | 19.60% | 31.49% |
| 2020 | -4.00% | -4.00% | 18.40% |
| 2021 | 20.10% | 20.00% | 28.71% |
| 2022 | -9.80% | -9.90% | -18.11% |
| 2023 | 19.50% | 19.30% | 26.29% |
| 2024 | 5.20% | 5.10% | 25.02% |
| 2025 | 39.50% | 39.40% | 17.88% |

Calculations from rounded official rows:

- 2016-2025: fund product 2.5598566, cumulative 155.99%, rounded-input CAGR 9.86%, 7 up years and 3 down years
- 2021-2025: fund product 1.8997979, cumulative 89.98%, rounded-input CAGR 13.70%, 4 up years and 1 down year
- 2017-2025 comparable benchmark window: fund CAGR 9.61% versus index CAGR 9.53%; the approximately 0.07 percentage-point difference is a return-only tracking observation, not alpha
- Best year: 2025 at 39.50%; worst year: 2018 at -14.40%
- Cached S&P 500 TR reference: 2016-2025 cumulative 298.33% / CAGR 14.82%; 2021-2025 cumulative 96.17% / CAGR 14.43%

S&P 500 Total Return เป็น common USD reference เท่านั้น ไม่ใช่
strategy-aligned benchmark ของ XDEV. The secondary rolling 10-year field
(12.42%*) is not substituted for the official annual-row CAGR.

## Risk read-through

XDEV concentrates on large- and mid-cap developed-market equities selected for
value characteristics. Official DWS top holdings ณ 31 ก.ค. 2026 ได้แก่ Micron
13.33%, Cisco Systems 3.32%, Verizon Communications 2.08%, Toyota Motor 1.64%,
AT&T 1.55%, Comcast 1.38%, Hewlett Packard Enterprise 1.34%, Qualcomm 1.31%,
General Motors 1.17% และ British American Tobacco 1.09%; top ten รวมประมาณ
28.21% จากน้ำหนักที่ประกาศแบบปัดเศษ.

ความเสี่ยงหลักคือ value-factor และ sector/country concentration, developed-market
equity drawdown, FX, tracking difference, liquidity และ premium/discount ระหว่าง
ราคา OTC หรือ exchange listing กับ NAV. DWS เตือนว่ากลยุทธ์แบบ rules-based อาจ
แตกต่างจากตลาดกว้างและทำให้ diversification ต่ำลง. Because the fund is
accumulating, income is reinvested rather than paid as a regular cash
distribution.

## Sources

- [DWS official July 2026 factsheet](https://etf.dws.com/download/asset/eb62907d-e0cd-4398-b392-b9154b1e94af) — identity, USD share class, SIX listing, inception, physical replication, fee, NAV, assets, index and holdings
- [DWS official past-performance document](https://etf.dws.com/Download/Past%20Performance/IE00BL25JM42/IE/EN) — official 2016-2025 share-class and benchmark rows, fee-deducted/reinvested-dividend basis and 2016 methodology splice
- [DWS official NAV page](https://etf.dws.com/it-it/nav/?PageSize=327) — current locale-formatted NAV display cross-check as of 2026-08-27; not used for USD return due no explicit currency
- [Liechtenstein Life fund page](https://liechtensteinlife.com/en-DE/markets/de/funds/IE00BL25JM42) — secondary current YTD, rolling returns and USD close-price fields as of 2026-08-27
- [StockAnalysis XDEVF profile](https://stockanalysis.com/quote/otc/XDEVF/) — secondary OTC ticker/name alias cross-check only
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common reference definition; calendar rows reused from the cached 2016-2025 convention
- [[ETF_performance_sources_2026-08-30]] | [[ETF Performance Index]]
