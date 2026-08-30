---
type: etf-performance
instrument_type: ETF
entity_key: LSE:VHVE
input_ticker: VGDDF
ticker: VHVE
exchange: London Stock Exchange
fund: Vanguard FTSE Developed World UCITS ETF (USD) Accumulating
tracked_index: FTSE Developed Index
benchmark: S&P 500 Total Return
management_mode: passive-index-tracking
updated: 2026-08-30
performance_as_of: 2025-12-31
calendar_years_as_of: 2025-12-31
current_ytd_as_of: 2026-07-31
price_nav_as_of: 2026-08-28
fund_facts_as_of: 2026-07-31
source_batch: raw/imports/ETF_performance_sources_2026-08-30.md
return_basis: NAV total return; gross income reinvested; net of fund expenses
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/VHVE
  - ticker/VGDDF
  - geography/International
---

# VGDDF / VHVE ETF Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

VGDDF เป็น OTC input alias ของ official USD listing `LSE:VHVE` สำหรับ Vanguard
FTSE Developed World UCITS ETF (USD) Accumulating. กองทุนเป็น passive,
physical, accumulating developed-market large-/mid-cap equity ETF ที่ติดตาม
`FTSE Developed Index` และมี OCF `0.12%`.

จาก official complete calendar NAV Total Return rows ช่วง 2020-2025
(ตัด 2019 partial inception) ผลตอบแทนสะสมคือ `105.82%` หรือ rounded-input
CAGR `12.78%`; ช่วง 2021-2025 สะสม `77.11%` หรือ CAGR `12.11%`. ในช่วง
2021-2025 S&P 500 Total Return ซึ่งเป็น common USD reference ทำได้ `96.17%`
หรือ CAGR `14.43%`; terminal wealth ของ VHVE ต่ำกว่าประมาณ `9.72%` ใน window
เดียวกัน. Current official NAV TR YTD คือ `+11.45%` ณ 31 ก.ค. 2026 และ NAV
ล่าสุดที่อ่านได้คือ `US$154.1961` ณ 28 ส.ค. 2026.

## Performance check

- `entity_key: LSE:VHVE`; input card ticker: `VGDDF` (OTC alias); official USD listing: London Stock Exchange `VHVE`
- ISIN: `IE00BK5BQV03`; share-class inception: `24 ก.ย. 2019`; listing date: `26 ก.ย. 2019`
- Classification: supported passive/index-tracking equity UCITS ETF; Vanguard ระบุว่าใช้ physical acquisition และ representative sampling เพื่อ track index
- Metric: `NAV Total Return` บนฐาน USD; factsheet ระบุ NAV-to-NAV, gross income invested และตาราง fund เป็น `net of expenses`; accumulating income ไม่จ่าย distribution แยก
- Management mode: `passive-index-tracking`; investment method: `physical`; OCF: `0.12%`
- Tracked index (issuer benchmark): `FTSE Developed Index` ซึ่งครอบคลุม large- และ mid-cap stocks ใน developed markets
- Common benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference benchmark ไม่ใช่ tracked index ของ VHVE)
- 10-year NAV TR: `not applicable (<10y history)`; 2019 inception year เป็น partial และไม่ถูกนำมาคำนวณ
- Official current fields as of `2026-07-31`: NAV TR YTD `11.45%`, 1-year `22.23%`, 3-year `18.74%`, 5-year `11.47%`, since inception `14.27%`; benchmark YTD `11.40%`, 1-year `22.13%`, 3-year `18.62%`, 5-year `11.33%`, since inception `14.14%`
- Official tracking evidence as of `2026-07-31`: beta `1.00`, R² `1.00`, annualized tracking error `0.02%` for 1 year, `0.05%` for 3 years, and `0.04%` for 5 years
- Complete calendar window: `2020-2025` VHVE compound `105.82%` / rounded-input CAGR `12.78%`; FTSE Developed Index compound `104.36%` / CAGR `12.65%`; S&P 500 TR compound `132.26%` / CAGR `15.08%`
- Common comparison window: `2021-2025` VHVE compound `77.11%` / CAGR `12.11%`; S&P 500 TR compound `96.17%` / CAGR `14.43%`; relative terminal wealth `-9.72%`
- Current price/NAV: official NAV `US$154.1961` and market price `£114.26` as of `2026-08-28`; currencies are shown separately and the market-price series is not used in NAV-return calculations

| Year | VHVE NAV TR | FTSE Developed Index TR | S&P 500 TR |
|---|---:|---:|---:|
| 2020 | 16.21% | 16.11% | 18.40% |
| 2021 | 20.99% | 20.87% | 28.71% |
| 2022 | -18.05% | -18.15% | -18.11% |
| 2023 | 23.84% | 23.61% | 26.29% |
| 2024 | 17.86% | 17.73% | 25.02% |
| 2025 | 22.38% | 22.25% | 17.88% |

## Up years / Down years

- Complete 2020-2025 years: `5 / 1`; 2021-2025 years: `4 / 1`
- Best: 2023, `+23.84%`; least positive: 2020, `+16.21%`
- Worst / only down year: 2022, `-18.05%`
- VHVE beat the tracked FTSE Developed Index in all `6 / 6` complete calendar years in the displayed rounded series; this is a return-only tracking observation, not a manager-skill claim
- VHVE beat the S&P 500 common reference in `2 / 6` complete 2020-2025 years; this is not an active-management claim
- Current official NAV TR YTD: `+11.45%` ณ 31 ก.ค. 2026

## Risk read-through

VHVE เป็น broad developed-market equity exposure แต่มีน้ำหนักสหรัฐฯ สูงถึง
`68.52%` และ technology `33.3%` ณ 31 ก.ค. 2026. Portfolio snapshot เดียวกัน
รายงาน `1,974` stocks, share-class assets `US$6.59B`, total fund assets
`US$11.28B`, P/E `21.7x`, P/B `3.7x`, และ portfolio turnover `-12.2%` ณ
30 มิ.ย. 2026. ประเทศหลักถัดจากสหรัฐฯ คือ Japan `6.62%`, UK `3.69%`, Canada
`3.31%`, และ South Korea `2.68%`.

ความเสี่ยงหลักคือ global mega-cap และ U.S. concentration, technology/sector,
country, foreign-currency, developed-market, sampling/tracking-error และ
ETF premium/discount risk. Official tracking error อยู่ในระดับต่ำใน reviewed
window (`0.02%`/`0.05%`/`0.04%`) แต่ daily NAV Total Return series ที่ยืนยันได้
สำหรับ maximum drawdown, recovery duration, downside capture หรือ
risk-adjusted persistence ยัง `ไม่พบข้อมูลที่ยืนยันได้`; จึงไม่แทนที่ด้วย
market-price หรือ secondary proxy.

## Sources

- [Vanguard VHVG/VHVE/VGVF official product page](https://www.vanguard.co.uk/uk-fund-directory/product/etf/equity/9675/ftse-developed-world-ucits) — official identity, passive objective, FTSE Developed Index, ISIN, listings, current NAV/market price, assets, holdings, portfolio and tracking fields
- [Vanguard FTSE Developed World UCITS ETF USD Accumulating factsheet](https://fund-docs.vanguard.com/FTSE_Developed_World_UCITS_ETF_USD_Accumulating_9675_CB_INT_EN.pdf) — 31 July 2026 official NAV/index annual rows, rolling fields, return definition, OCF, structure and fund facts
- [MarketScreener VGDDF profile](https://www.marketscreener.com/quote/etf/VANGUARD-FTSE-DEVELOPED-W-134196015/) — secondary OTC alias/name and ISIN cross-check; not used as the NAV Total Return source
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- Cached S&P 500 TR references: [historical research](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [2023 U.S. Equities Market Attributes](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), [2021 market attributes](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/), and [2025 market attributes](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/); cached convention as of 31 ธ.ค. 2025
- [[ETF_performance_sources_2026-08-30]] | [[ETF Performance Index]]
