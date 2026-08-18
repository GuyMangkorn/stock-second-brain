---
type: etf-performance
instrument_type: ETF
entity_key: Euronext Amsterdam:VEUR
input_ticker: VFDEF
ticker: VEUR
exchange: Euronext Amsterdam
fund: Vanguard FTSE Developed Europe UCITS ETF (EUR) Distributing
tracked_index: FTSE Developed Europe Index
benchmark: S&P 500 Total Return
management_mode: passive-index-tracking
updated: 2026-08-19
performance_as_of: 2025-12-31
current_ytd_as_of: 2026-07-31
price_nav_as_of: 2026-08-17
fund_facts_as_of: 2026-07-31
source_batch: raw/imports/ETF_performance_sources_2026-08-19.md
return_basis: NAV total return; dividends reinvested; net of expenses
return_currency: EUR
tags:
  - analysis/etf-performance
  - ticker/VEUR
  - geography/Europe
---

# VEUR Performance

> Navigation: [[ETF Region Index]] → [[Europe ETF]] → [[ETF Performance Index]]

## Bottom line

`VFDEF` เป็น OTC input alias ของ Vanguard FTSE Developed Europe UCITS ETF
(EUR) Distributing; canonical listing ที่ใช้ใน vault คือ `Euronext
Amsterdam:VEUR`. Official complete-calendar NAV rows ปี 2016-2025 compound ได้
`115.91%` หรือ rounded-input CAGR `8.00%`; ช่วงร่วม 2021-2025 ได้ `72.19%` หรือ
`11.48%` ต่อปี. ผลตอบแทนเป็นบวก/ลบ `7 / 3` ปี และ current official NAV TR YTD
คือ `+12.06%` ณ 31 ก.ค. 2026.

## Performance check

- `entity_key: Euronext Amsterdam:VEUR`; `input_ticker: VFDEF`; Vanguard ระบุ official EUR exchange ticker `VEUR` บน NYSE Euronext - Amsterdam, ISIN `IE00B945VV12`, share-class inception `21 พ.ค. 2013` และ listing date `22 พ.ค. 2013`.
- Classification: `passive-index` / physical indexing; กองทุนลงทุนในหุ้น large- และ mid-cap ของ developed Europe และใช้ sampling เมื่อ full replication ทำไม่ได้.
- Metric: `NAV Total Return` รวม dividends/capital gains ที่ reinvested และ fund expenses; คำนวณเป็น EUR. Share class นี้จ่าย income ออกและมี distribution frequency แบบ quarterly.
- Issuer benchmark: `FTSE Developed Europe Index`; benchmark ในตารางด้านล่างคือ `S&P 500 Total Return` (USD, dividends reinvested; common reference benchmark) จึงไม่ควรตีความเป็น direct excess return เทียบกับ EUR โดยไม่มี FX adjustment.
- Expense ratio: `0.10% Ongoing Charges Figure`; official current NAV `€50.7466` ณ 17 ส.ค. 2026; total assets `€7.678B` และ share-class assets `€4.776B` ณ 31 ก.ค. 2026.
- Current official NAV TR YTD: `+12.06%` ณ 31 ก.ค. 2026. Official 1Y/3Y/5Y/10Y annualised NAV TR ณ วันเดียวกันคือ `22.47% / 14.60% / 10.39% / 9.66%`.
- Distribution check: product page ระบุ quarterly และแสดง cash distributions ล่าสุด 4 งวดรวม `€1.2914` ต่อหน่วย (`€0.1609`, `€0.1676`, `€0.1815`, `€0.7814`); เงินจ่ายนี้แยกจาก NAV TR ซึ่ง reinvested income แล้ว. Product page ยังแสดง field `Historical performance` `2.58%` ณ 31 ก.ค. 2026 โดยคง label เดิมไว้ ไม่ตีความเพิ่มเป็น forward yield.
- Coverage/source note: KID ของ Vanguard ให้ complete calendar rows ปี 2016-2025 เป็น official EUR NAV/index returns. S&P 500 rows เป็น cached USD total-return convention ปี 2016-2025 ณ 31 ธ.ค. 2025.

| Year | VEUR NAV TR (EUR) | FTSE Developed Europe Index (EUR) | S&P 500 TR (USD; common ref.) |
|---|---:|---:|---:|
| 2016 | 2.80% | 2.50% | 11.96% |
| 2017 | 10.70% | 10.50% | 21.83% |
| 2018 | -10.50% | -10.70% | -4.38% |
| 2019 | 26.40% | 26.10% | 31.49% |
| 2020 | -2.60% | -2.70% | 18.40% |
| 2021 | 25.20% | 24.90% | 28.71% |
| 2022 | -10.00% | -10.20% | -18.11% |
| 2023 | 16.50% | 16.20% | 26.29% |
| 2024 | 9.40% | 9.10% | 25.02% |
| 2025 | 19.90% | 19.50% | 17.88% |

Official VEUR rows compound to `115.91%` / rounded-input CAGR `8.00%` for
2016-2025 and `72.19%` / `11.48%` for 2021-2025. The corresponding FTSE index
rows compound to `110.86%` / `7.75%` and `69.92%` / `11.19%`; the approximately
`+0.26 pp` and `+0.30 pp` fund-minus-index differences are passive tracking
observations, not alpha. Cached S&P 500 TR compounds to `298.33%` / `14.82%`
for 2016-2025 and `96.17%` / `14.43%` for 2021-2025, but its USD basis is not
directly comparable with this EUR share class without an FX-normalized series.

**Up years / Down years**

- Complete 2016-2025 NAV TR up/down: `7 / 3`
- Best NAV TR year: 2019, `+26.40%`
- Least positive year: 2016, `+2.80%`
- Worst NAV TR year: 2018, `-10.50%`
- Least bad down year: 2020, `-2.60%`
- Population standard deviation of the ten complete annual NAV returns: `12.87%`
- Current YTD: `+12.06%` as of 31 ก.ค. 2026

## Risk read-through

Official 2016-2025 NAV TR CAGR is `8.00%`, with annual-return dispersion
`12.87%`; official 1/3/5-year annualized tracking error is `0.14%` ณ 31 ก.ค.
2026. The fund held 513 stocks ณ วันเดียวกัน, with meaningful country exposure
to the United Kingdom `23.21%`, France `14.67%`, Switzerland `14.44%`, Germany
`13.33%`, and the Netherlands `8.14%`. Main risks are European country/sector
concentration, EUR-base versus non-EUR underlying currencies, foreign-market
and equity volatility, distribution timing, and index-tracking risk. Official
daily NAV maximum drawdown and recovery date ยัง `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- [Vanguard VEUR product page](https://www.vanguard.co.uk/professional/product/etf/equity/9520/vanguard-ftse-developed-europe-ucits-etf-eur-distributing) — official identity, listing, inception, benchmark, current NAV, distributions, holdings and dated portfolio facts.
- [Vanguard VEUR factsheet](https://fund-docs.vanguard.com/FTSE_Developed_Europe_UCITS_ETF_EUR_Distributing_9520_EU_INT_EN.pdf) — official performance summary, fee, assets, index, distribution and risk fields as of 31 ก.ค. 2026.
- [Vanguard VEUR KID](https://fund-docs.vanguard.com/ie00b945vv12-en.pdf) — official EUR calendar return chart for 2016-2025, ongoing charges and distributing-share disclosure; accurate 17 ก.พ. 2026.
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached workflow references — common USD Total Return rows, dividends reinvested, as of 31 ธ.ค. 2025.
- [[ETF_performance_sources_2026-08-19]] | [[ETF Performance Index]]
