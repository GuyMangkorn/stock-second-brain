---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:BBIN
ticker: BBIN
exchange: NYSE Arca
fund: JPMorgan BetaBuilders International Equity ETF
tracked_index: Morningstar Developed Markets ex-North America Target Market Exposure Index (net total return)
benchmark: S&P 500 Total Return
updated: 2026-08-30
performance_as_of: 2025-12-31
rolling_10y_as_of: not applicable (<10y)
current_ytd_as_of: 2026-07-31
price_nav_as_of: not disclosed in reviewed official current capture
fund_facts_as_of: 2026-07-31
source_batch: raw/imports/ETF_performance_sources_2026-08-30.md
return_basis: NAV total return for official fields
return_currency: USD
management_mode: passive-index
tags:
  - analysis/etf-performance
  - ticker/BBIN
  - geography/International
---

# BBIN Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

BBIN เป็น passive/index-tracking ETF สำหรับ developed markets นอก North America
ที่ติดตาม Morningstar Developed Markets ex-North America Target Market Exposure
Index. ใน complete calendar window 2020-2025 มี 5 ปีบวก / 1 ปีลบ; official NAV
Total Return cumulative อยู่ที่ `67.92%` หรือ rounded-input CAGR `9.02%` เทียบ
S&P 500 TR common reference ที่ `132.26%` / `15.08%`. ปีดีที่สุดคือ 2025 ที่
`+32.05%` และปีติดลบเพียงปีเดียวคือ 2022 ที่ `-14.10%`. Current official NAV TR
YTD คือ `+11.47%` ณ 31 ก.ค. 2026.

## Performance check

- `entity_key: NYSE Arca:BBIN`
- Classification: supported passive/index-tracking equity ETF; JPMorgan uses an indexed approach and the prospectus describes passive management with replication/representative sampling.
- Inception / class launch: `2019-12-03`; 2019 เป็น partial inception year และไม่ถูกนำมาคำนวณ
- Expense ratio: `0.07%` gross และ net ณ factsheet 31 ก.ค. 2026
- Metric: `NAV Total Return` บนฐาน USD; JPMorgan ระบุว่า NAV ที่ใช้คำนวณ total return สะท้อน management fees และ operating expenses และ hypothetical growth reinvests dividends/capital gains
- Tracked index (issuer benchmark): `Morningstar Developed Markets ex-North America Target Market Exposure Index` (net total return)
- Common benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference benchmark ไม่ใช่ tracked index ของ BBIN)
- Official current YTD: NAV `+11.47%` ณ `2026-07-31`; tracked index `+11.22%`; market-price YTD `+11.42%`
- Official annual window: `2020-2025` NAV product `67.92%` cumulative / rounded-input CAGR `9.02%`; tracked index `66.53%` / `8.87%`; return-only tracking difference คือประมาณ `+0.15 pp` CAGR
- Common comparison window: `2021-2025` NAV product `54.59%` / CAGR `9.10%`; S&P 500 TR `96.17%` / CAGR `14.43%`; BBIN terminal wealth ต่ำกว่าประมาณ `21.20%` ใน window เดียวกัน
- Current price/NAV: ใน reviewed official current capture ไม่พบ price/NAV ที่ยืนยันได้ใหม่กว่าชุด performance; จึงไม่แทนที่ด้วย secondary quote

| Year | BBIN NAV TR | Morningstar index TR | S&P 500 TR |
|---|---:|---:|---:|
| 2020 | 8.62% | 8.23% | 18.40% |
| 2021 | 11.42% | 11.27% | 28.71% |
| 2022 | -14.10% | -14.31% | -18.11% |
| 2023 | 18.17% | 18.17% | 26.29% |
| 2024 | 3.51% | 3.76% | 25.02% |
| 2025 | 32.05% | 31.61% | 17.88% |

## Up years / Down years

- Up years / Down years: `5 / 1` ใน 2020-2025
- Best: 2025, `+32.05%`
- Least positive: 2024, `+3.51%`
- Worst / only down year: 2022, `-14.10%`
- 2020-2025 cumulative/CAGR: BBIN `67.92%` / `9.02%`; Morningstar index
  `66.53%` / `8.87%`; S&P 500 TR `132.26%` / `15.08%`
- 2021-2025 cumulative/CAGR: BBIN `54.59%` / `9.10%`; Morningstar index
  `53.86%` / `9.00%`; S&P 500 TR `96.17%` / `14.43%`
- BBIN beat the tracked index in `4 / 6` calendar years, tied in 2023 and lagged
  in 2024; this return-only tracking comparison is not a manager-skill claim
- Current BBIN NAV TR YTD: `+11.47%` ณ 31 ก.ค. 2026

## Risk read-through

ประวัติ BBIN ยังไม่ครบ 10 ปีจาก class launch `2019-12-03` จึงไม่มี 10-year NAV
CAGR ที่ใช้ได้. Official factsheet ณ 31 ก.ค. 2026 รายงาน annualized NAV TR
1-year `20.40%`, 3-year `16.52%`, 5-year `9.24%`, และ since launch `10.38%`;
current standardized fields แยกจาก calendar rows และ current YTD.

Portfolio snapshot เดียวกันรายงาน assets `US$6.60B`, holdings `636`, P/E
`15.99x`, P/B `2.29x`, 12-month rolling dividend yield `3.91%`; country exposure
นำโดย Japan `24.7%`, United Kingdom `14.2%`, Switzerland `9.4%`, France `8.6%`
และ Germany `8.5%`. Sector exposure นำโดย financials `26.8%`, industrials
`19.0%`, health care `10.2%` และ information technology `9.8%`.

ความเสี่ยงหลักคือ country/region, FX, financials/industrials concentration,
foreign-market trading calendar, sampling/tracking error, premium/discount,
และ liquidity. Prospectus อนุญาตให้ใช้ futures และ forward foreign-currency
contracts ได้ถึง `10%` ของ assets เพื่อช่วยให้ผลตอบแทนสอดคล้องกับ index แต่ไม่ใช่
กองทุน derivative-heavy. Official daily NAV history สำหรับ maximum drawdown,
recovery duration และ risk-adjusted persistence ยัง `ไม่พบข้อมูลที่ยืนยันได้`;
จึงไม่ใช้ secondary drawdown proxy.

## Sources

- [JPMorgan BBIN July 2026 factsheet](https://am.jpmorgan.com/content/dam/jpm-am-aem/americas/us/en/literature/fact-sheet/etfs/FS-BBIN.PDF) — indexed/passive objective, Morningstar benchmark, launch, expenses, official 2020-2025 calendar NAV/index rows, 2026 YTD, annualized fields, assets, holdings, country/sector and valuation snapshot as of 2026-07-31
- [JPMorgan BBIN product page](https://am.jpmorgan.com/us/en/asset-management/institutional/products/jpmorgan-betabuilders-international-equity-etf-etf-shares-46641q373) — official fund identity and product access point; reviewed page's dynamic current quote was not used when not readable
- [BBIN summary prospectus](https://www.sec.gov/Archives/edgar/data/1485894/000119312525036033/d766505d497k.htm) — objective, 80% index policy, passive/representative-sampling approach, derivative allowance and country/sector/FX/tracking risks
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- Cached S&P 500 TR references: [2016-2019](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [2018-2022](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), [2021](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/), [2022-2025](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/)
- ETF source batch: [[ETF_performance_sources_2026-08-30]] | [[International ETF]] | [[ETF Performance Index]]
