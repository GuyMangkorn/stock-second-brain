---
type: etf-performance
instrument_type: ETF
entity_key: Cboe BZX:GSID
input_ticker: GSID
ticker: GSID
exchange: Cboe BZX
fund: Goldman Sachs MarketBeta International Equity ETF
tracked_index: Solactive GBS Developed Markets ex North America Large & Mid Cap Index
benchmark: S&P 500 Total Return
updated: 2026-08-30
performance_as_of: 2026-07-31
rolling_5y_as_of: 2026-07-31
current_ytd_as_of: 2026-07-31
market_price_as_of: 2026-08-28
nav_as_of: not disclosed in reviewed official sources
fund_facts_as_of: 2026-07-31
source_batch: raw/imports/ETF_performance_sources_2026-08-30.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - geography/International
  - ticker/GSID
  - geography/developed-ex-North-America
  - style/market-beta
---

# GSID Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

GSID เป็น passive broad-market international ETF ที่ให้ official `NAV Total Return`
`+11.93%` YTD, `+25.48%` 1-year, `+16.08%` 3-year annualized, `+9.08%` 5-year
annualized และ `+13.88%` since inception ณ 31 ก.ค. 2026. ผลตอบแทน 2021-2024
ที่เปิดเผยเป็น complete calendar rows ให้ cumulative `+16.24%*` หรือ rounded-input
CAGR `+3.83%*`; ยังไม่คำนวณ 2021-2025 CAGR หรือ 10-year CAGR เพราะไม่พบปี 2025
ใน primary performance table และกองทุนเริ่ม 12 พ.ค. 2020.

## Performance check

- `entity_key: Cboe BZX:GSID`; inception: 12 พ.ค. 2020; expense ratio: `0.20%`
  หลัง fee waiver จาก gross `0.25%` อย่างน้อยถึง 29 ธ.ค. 2026
- Metric: `NAV Total Return` ใน USD รวมการ reinvest distributions และสะท้อน
  management fees/operating expenses ตาม Goldman Sachs
- Issuer benchmark: `Solactive GBS Developed Markets ex North America Large & Mid Cap Index`
- Benchmark: `S&P 500 Total Return` เป็น common USD reference เท่านั้น
- Management mode: `passive-index`
- Official 5-year NAV TR annualized: `9.08%` ณ 31 ก.ค. 2026; 10-year field:
  `ไม่พบข้อมูลที่ยืนยันได้` เพราะ fund inception ปี 2020
- Official current NAV TR comparison ณ 31 ก.ค. 2026:

| Period | GSID NAV TR | Solactive index | Return-only difference |
|---|---:|---:|---:|
| 1 month | 1.68% | 2.19% | -0.51 pp |
| YTD | 11.93% | 11.84% | +0.09 pp |
| 1 year | 25.48% | 24.78% | +0.70 pp |
| 3 years annualized | 16.08% | 16.08% | 0.00 pp |
| 5 years annualized | 9.08% | 9.28% | -0.20 pp |
| Since inception annualized | 13.88% | 13.95% | -0.07 pp |

ผลต่างข้างต้นเป็น return-only tracking observation ไม่ใช่ `alpha` หรือหลักฐาน
ของ manager skill; index return ไม่หัก fund expenses.

## Calendar performance

Official prospectus เปิดเผย complete calendar rows ถึงปี 2024 เท่านั้น:

| ปี | GSID NAV TR | S&P 500 TR |
|---|---:|---:|
| 2021 | 11.09% | 28.71% |
| 2022 | -14.53% | -18.11% |
| 2023 | 17.81% | 26.29% |
| 2024 | 3.92% | 25.02% |

- Available 2021-2024 window: GSID cumulative `16.24%*`, rounded-input CAGR
  `3.83%*`, 3 up years / 1 down year; S&P 500 TR cumulative `66.41%*` / CAGR
  `13.58%*`.
- 2025 calendar return และ 2021-2025 CAGR: `ไม่พบข้อมูลที่ยืนยันได้` ใน reviewed
  primary sources; ไม่เติมค่าจาก secondary proxy
- Best available year: 2023 `+17.81%`; worst: 2022 `-14.53%`

## Risk read-through

GSID ให้ exposure ประมาณ 85% ของ developed markets excluding North America ผ่าน
large-/mid-cap securities. Official factsheet ณ 31 ก.ค. 2026 ระบุ holdings `894`,
net assets `US$1,100.36M`, P/E `19.02x`, P/B `2.31x`, weighted average market cap
`US$122.57B`, และ quarterly distributions. Sector weights สูงสุดคือ Financials
`26.3%`, Industrials `18.9%`, Health Care `10.0%`, Information Technology `10.0%`
และ Consumer Discretionary `8.7%`; country weights สูงสุดคือ Japan `25.7%`, UK
`14.3%`, France `8.9%`, Germany `8.2%` และ Switzerland `8.4%`.

ความเสี่ยงหลักคือ foreign equity, country/Europe/Japan, FX, mid-cap liquidity,
industry concentration และ tracking error. Official daily NAV TR series สำหรับ
maximum drawdown, recovery duration, downside capture, standard deviation, beta
และ risk-adjusted persistence ยัง `ไม่พบข้อมูลที่ยืนยันได้`; ไม่ใช้ market-price
series แทน NAV TR. Secondary closing price คือ `US$77.84*` ณ 28 ส.ค. 2026 และใช้เป็น
เพียง price cross-check ไม่ใช่ performance metric.

## Sources

- [Goldman Sachs GSID factsheet](https://am.gs.com/public-assets/documents/47d091ff-3822-11f0-b258-073c8c60f146?view=true)
- [Goldman Sachs summary prospectus](https://am.gs.com/public-assets/documents/7d9e2f2c-2fa6-11ef-85a5-17cd01506bd9)
- [Cboe GSID listing](https://www.cboe.com/us/equities/listings/listed_products/symbols/GSID)
- [Secondary price cross-check](https://stockanalysis.com/etf/gsid/)
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) | [S&P DJI index returns](https://www.spglobal.com/spdji/en/additional-reports/all-returns/index.dot?additionalFilterCondition=&parentIdentifier=df8ec300-24ad-4c70-81d3-a3cece0200e2&sourceIdentifier=index-family-specialization)
- [[ETF_performance_sources_2026-08-30]] | [[ETF Performance Index]]
