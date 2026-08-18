---
type: etf-performance
instrument_type: ETF
entity_key: Nasdaq:DAX
input_ticker: DAX
ticker: DAX
exchange: Nasdaq
fund: Global X DAX Germany ETF
tracked_index: DAX Index
benchmark: S&P 500 Total Return
updated: 2026-08-18
performance_as_of: 2025-12-31
rolling_10y_as_of: 2026-06-30
current_ytd_as_of: 2026-05-31
price_nav_as_of: 2026-07-27
fund_facts_as_of: 2026-07-31
source_batch: raw/imports/ETF_performance_sources_2026-08-18.md
return_basis: official fund total return / NAV total return where issuer-reported
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/DAX
  - geography/Germany
---

# DAX Performance

> Navigation: [[ETF Region Index]] → [[Germany ETF]] → [[ETF Performance Index]]

## Bottom line

`DAX` คือ Global X DAX Germany ETF ที่จดทะเบียนบน Nasdaq และเป็น
`passive-index` equity ETF ซึ่งติดตาม `DAX Index` ก่อนค่าธรรมเนียม. Official
fund total return ปี 2016-2025 compound ได้ `130.68%` หรือ rounded-input CAGR
`8.72%`; ช่วง 2021-2025 ได้ `65.87%` หรือ `10.65%` ต่อปี. Official rolling
10-year NAV TR อยู่ที่ `9.57%` ณ 30 มิ.ย. 2026 และ official YTD อยู่ที่ `1.40%`
ณ 31 พ.ค. 2026. Annual rows เป็น official fund returns จาก summary prospectus
และไม่ควรสับสนกับ rolling field หรือ issuer benchmark rows.

## Performance check

- `entity_key: Nasdaq:DAX`; Global X DAX Germany ETF, ticker `DAX`, Nasdaq, inception 22 ต.ค. 2014.
- Classification: `passive-index`; กองทุนลงทุนอย่างน้อย 80% ในหลักทรัพย์ของ DAX Index หรือ ADRs/GDRs ที่เกี่ยวข้อง และใช้ replication โดยทั่วไป; prospectus ระบุว่าไม่ใช่ actively managed และเป็น non-diversified.
- Metric: ตาราง annual ด้านล่างเป็น official fund total return ของปีปฏิทิน ซึ่งรวมผลตอบแทนจากการลงทุน; official factsheet/product page แสดง rolling NAV TR แยกต่างหาก.
- Issuer benchmark: `DAX Index`; `S&P 500 Total Return` ใช้เป็น common USD reference เท่านั้น ไม่ใช่ tracked index ของกองทุน.
- Expense ratio: `0.20%`; distributions: semi-annual; portfolio turnover ล่าสุดใน summary prospectus `8.14%`.
- 10-year window: issuer rolling field as of 30 มิ.ย. 2026; raw endpoint values เป็น `not disclosed` ในเอกสารที่ตรวจสอบ.
- 10-year NAV TR CAGR: `9.57%` (issuer-reported annualised field; ไม่ reconstruct จาก annual rows).
- Issuer benchmark comparison, annualised ณ 30 มิ.ย. 2026: 1Y `1.24%` vs DAX Index `1.82%` (`-0.58 pp`); 3Y `16.77%` vs `17.50%` (`-0.73 pp`); 5Y `8.47%` vs `9.18%` (`-0.71 pp`); 10Y `9.57%` vs `10.27%` (`-0.70 pp`). นี่เป็น passive tracking/cost comparison ไม่ใช่ active alpha.

| Year | DAX Fund total return (official, USD) | S&P 500 TR (USD) |
|---|---:|---:|
| 2016 | 2.55% | 11.96% |
| 2017 | 26.83% | 21.83% |
| 2018 | -22.38% | -4.38% |
| 2019 | 22.47% | 31.49% |
| 2020 | 12.48% | 18.40% |
| 2021 | 7.09% | 28.71% |
| 2022 | -18.35% | -18.11% |
| 2023 | 23.59% | 26.29% |
| 2024 | 10.65% | 25.02% |
| 2025 | 38.72% | 17.88% |

Official DAX Fund rows compound to `130.68%` / rounded-input CAGR `8.72%` for
2016-2025 and `65.87%` / `10.65%` for 2021-2025. The cached S&P 500 TR rows
compound to `298.33%` / `14.82%` and `96.17%` / `14.43%`, respectively. DAX
underperformed this common reference by approximately `-6.10 pp` and
`-3.78 pp` of rounded-input CAGR; this is not an issuer-benchmark or alpha
claim. The 2016-2018 rows include predecessor history carried through the
24 ธ.ค. 2018 reorganization, as disclosed in the summary prospectus.

**Up years / Down years**

- Up/down years: `8 / 2`
- Best: 2025, `+38.72%`
- Least positive: 2016, `+2.55%`
- Worst: 2018, `-22.38%`
- Least bad down year: 2022, `-18.35%`
- Current official NAV TR YTD: `+1.40%` as of 31 พ.ค. 2026; latest official NAV `44.72` and market price `44.78` as of 27 ก.ค. 2026.

## Risk read-through

The issuer reports 3-year standard deviation of `16.10%` and beta of `1.03`
versus the S&P 500 as of 31 ก.ค. 2026. The portfolio had 41 holdings; sector
weights were Industrials `35.7%`, Financials `21.2%`, and Information
Technology `13.8%` as of the reviewed July snapshot. Germany/country,
EUR/USD, export-cycle, sector concentration and non-diversification risks are
therefore material. Official daily NAV maximum drawdown and recovery date were
not disclosed in the reviewed capture, so `risk-adjusted evidence: not-verified`
for those fields. The 0.20% expense ratio and passive tracking structure create
expected drag versus the DAX Index.

## Sources

- [Global X DAX product page](https://www.globalxetfs.com/funds/dax) — official identity, exchange, benchmark, holdings, current NAV/price, YTD, rolling returns, risk and exposure snapshot
- [Global X DAX factsheet](https://assets.globalxetfs.com/funds/documents/dax/Fact-Sheet_DAX.pdf) — official annualised and YTD performance table, fee, holdings and fund facts
- [Global X DAX summary prospectus](https://assets.globalxetfs.com/funds/documents/dax/prospectus-regulatory/Summary-Prospectus_DAX.pdf) — official objective, passive/80%/non-diversified disclosures and 2016-2025 annual total returns
- [SEC HTML summary prospectus](https://www.sec.gov/Archives/edgar/data/1432353/000143235326000193/a497kdaxgermany.htm) — filing copy of the official prospectus and performance chart
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- Cached S&P 500 TR references: [2016-2019](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [2018-2022](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), [2021](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/), and [2022-2025](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/)
- ETF source batch: [[ETF_performance_sources_2026-08-18]] | [[ETF Performance Index]]
