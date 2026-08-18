---
type: etf-performance
instrument_type: ETF
entity_key: Euronext Amsterdam:VWCG
input_ticker: VNGLF
ticker: VWCG
exchange: Euronext Amsterdam
fund: Vanguard FTSE Developed Europe UCITS ETF (EUR) Accumulating
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
  - ticker/VWCG
  - geography/Europe
---

# VWCG Performance

> Navigation: [[ETF Region Index]] → [[Europe ETF]] → [[ETF Performance Index]]

## Bottom line

`VNGLF` เป็น OTC input alias ของ Vanguard FTSE Developed Europe UCITS ETF
(EUR) Accumulating; canonical listing ที่ใช้ใน vault คือ `Euronext
Amsterdam:VWCG`. Official complete-calendar NAV rows ปี 2020-2025 compound ได้
`67.71%` หรือ rounded-input CAGR `9.00%`; ช่วงร่วม 2021-2025 ได้ `72.19%` หรือ
`11.48%` ต่อปี. ผลตอบแทนเป็นบวก/ลบ `5 / 1` ปี และ current official NAV TR YTD
คือ `+12.06%` ณ 31 ก.ค. 2026.

## Performance check

- `entity_key: Euronext Amsterdam:VWCG`; `input_ticker: VNGLF`; Vanguard ระบุ official EUR exchange ticker `VWCG` บน NYSE Euronext - Amsterdam, ISIN `IE00BK5BQX27`, share-class inception `23 ก.ค. 2019` และ listing date `25 ก.ค. 2019`.
- Classification: `passive-index` / physical indexing; กองทุนลงทุนในหุ้น large- และ mid-cap ของ developed Europe และใช้ sampling เมื่อ full replication ทำไม่ได้.
- Metric: `NAV Total Return` รวม dividends/capital gains ที่ reinvested และ fund expenses; คำนวณเป็น EUR. Accumulation share class ไม่มี cash distribution schedule.
- Issuer benchmark: `FTSE Developed Europe Index`; benchmark ในตารางด้านล่างคือ `S&P 500 Total Return` (USD, dividends reinvested; common reference benchmark) จึงไม่ควรตีความเป็น direct excess return เทียบกับ EUR โดยไม่มี FX adjustment.
- Expense ratio: `0.10% Ongoing Charges Figure`; official current NAV `€60.9809` ณ 17 ส.ค. 2026; total assets `€7.678B` และ share-class assets `€2.902B` ณ 31 ก.ค. 2026.
- Current official NAV TR YTD: `+12.06%` ณ 31 ก.ค. 2026. Official 1Y/3Y/5Y annualised NAV TR ณ วันเดียวกันคือ `22.47% / 14.60% / 10.39%`; 10-year field ไม่ applicable เพราะ share class เริ่มในปี 2019.
- Coverage/source note: KID ของ Vanguard ให้ complete calendar rows ปี 2020-2025 เป็น official EUR NAV/index returns; 2019 partial ถูกตัดออกจาก ranking เพราะไม่มีตัวเลข partial ที่ยืนยันได้ในชุดที่ใช้. S&P 500 rows เป็น cached USD total-return convention ปี 2020-2025 ณ 31 ธ.ค. 2025.

| Year | VWCG NAV TR (EUR) | FTSE Developed Europe Index (EUR) | S&P 500 TR (USD; common ref.) |
|---|---:|---:|---:|
| 2020 | -2.60% | -2.70% | 18.40% |
| 2021 | 25.20% | 24.90% | 28.71% |
| 2022 | -10.00% | -10.20% | -18.11% |
| 2023 | 16.50% | 16.20% | 26.29% |
| 2024 | 9.40% | 9.10% | 25.02% |
| 2025 | 19.90% | 19.50% | 17.88% |

Official VWCG rows compound to `67.71%` / rounded-input CAGR `9.00%` for
2020-2025 and `72.19%` / `11.48%` for 2021-2025. The corresponding FTSE index
rows compound to `65.33%` / `8.74%` and `69.92%` / `11.19%`; the approximately
`+0.26 pp` and `+0.30 pp` fund-minus-index differences are passive tracking
observations, not alpha. Cached S&P 500 TR compounds to `132.26%` / `15.08%`
for 2020-2025 and `96.17%` / `14.43%` for 2021-2025, but its USD basis is not
directly comparable with this EUR share class without an FX-normalized series.

**Up years / Down years**

- Complete 2020-2025 NAV TR up/down: `5 / 1`
- Best NAV TR year: 2021, `+25.20%`
- Least positive year: 2024, `+9.40%`
- Worst NAV TR year: 2020, `-2.60%`
- Least bad down year: 2020, `-2.60%`
- Population standard deviation of the six complete annual NAV returns: `12.45%`
- Current YTD: `+12.06%` as of 31 ก.ค. 2026

## Risk read-through

Available-period 2020-2025 NAV TR CAGR is `9.00%`, with annual-return
dispersion `12.45%`; official 1/3/5-year annualized tracking error is `0.14%`
ณ 31 ก.ค. 2026. The fund held 513 stocks ณ วันเดียวกัน, with meaningful
country exposure to the United Kingdom `23.21%`, France `14.67%`, Switzerland
`14.44%`, Germany `13.33%`, and the Netherlands `8.14%`. Main risks are
European country/sector concentration, EUR-base versus non-EUR underlying
currencies, foreign-market and equity volatility, and index-tracking risk.
Official daily NAV maximum drawdown and recovery date ยัง `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- [Vanguard VWCG / VEUA product page](https://www.vanguard.co.uk/professional/product/etf/equity/9681/vanguard-ftse-developed-europe-ucits-etf-eur-accumulating) — official identity, listing, inception, benchmark, current NAV, holdings and dated portfolio facts.
- [Vanguard VWCG factsheet](https://fund-docs.vanguard.com/FTSE_Developed_Europe_UCITS_ETF_EUR_Accumulating_9681_EU_INT_UK_EN.pdf) — official performance summary, calendar/rolling definitions, fee, assets, index and risk fields as of 31 ก.ค. 2026.
- [Vanguard VWCG KID](https://fund-docs.vanguard.com/ie00bk5bqx27-en.pdf) — official EUR calendar return chart for 2020-2025 and accumulating-share disclosure; accurate 17 ก.พ. 2026.
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached workflow references — common USD Total Return rows, dividends reinvested, as of 31 ธ.ค. 2025.
- [[ETF_performance_sources_2026-08-19]] | [[ETF Performance Index]]
