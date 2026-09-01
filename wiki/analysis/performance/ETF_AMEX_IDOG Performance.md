---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:IDOG
input_ticker: IDOG
ticker: IDOG
exchange: NYSE Arca
fund: ALPS International Sector Dividend Dogs ETF
tracked_index: S-Network International Sector Dividend Dogs Index (IDOGX)
benchmark: S&P 500 Total Return
updated: 2026-09-01
performance_as_of: 2025-12-31 (calendar) / 2026-07-31 (rolling)
calendar_years_as_of: 2025-12-31 (official issuer table)
current_ytd_as_of: 2026-07-31
market_price_as_of: 2026-08-28 (secondary)
nav_as_of: 2026-08-25 (secondary)
fund_facts_as_of: 2026-07-31 (official performance) / 2026-06-30 (official factsheet)
source_batch: raw/imports/ETF_performance_sources_2026-09-01_run-6.md
return_basis: NAV total return; distributions reinvested; net of fund expenses
return_currency: USD
primary_region: International
tags:
  - analysis/etf-performance
  - ticker/IDOG
  - geography/International
  - geography/global-developed
---

# IDOG Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

IDOG เป็น passive/index-tracking international dividend ETF ที่ใช้ rules-based
`Dogs of the Dow` methodology เลือกหุ้น dividend yield สูงสุดราย sector และ
equal-weight. Official ALPS performance update รายงาน NAV YTD `16.08%`, 1-year
cumulative `34.75%`, 3-year annualized `27.34%` และ 10-year annualized `10.66%`
ณ 31 ก.ค. 2026. Complete official calendar rows 2016-2025 ให้ cumulative
`151.71%` / rounded-input CAGR `9.67%`, มีปีบวก/ลบ `7 / 3`; 2021-2025 ให้
`85.69%` / `13.18%` เทียบ S&P 500 TR `14.43%`.

## Performance check

- `entity_key: NYSE Arca:IDOG`
- Fund: ALPS International Sector Dividend Dogs ETF
- Inception: `2013-06-27`; listing exchange `NYSE Arca`; expense ratio `0.50%`
- Metric: `NAV Total Return` รวม distributions reinvested และ fund expenses
- Issuer benchmark: S-Network International Sector Dividend Dogs Index
- Common benchmark: `S&P 500 Total Return` (USD, dividends reinvested)
- 10-year NAV TR CAGR: `10.66%` as of `2026-07-31` (official ALPS annualized field); prior official factsheet reads `10.65%` as of `2026-06-30` and is kept date-separated
- Coverage/source note: annual NAV TR rows are official issuer rows captured 2026-07-02; current rolling fields use the newer official ALPS July 31, 2026 performance update. The existing filename contains legacy `AMEX`; the canonical entity/exchange is `NYSE Arca:IDOG`.

### Official rolling performance

| Period | IDOG NAV TR | IDOG market price TR | IDOGX Index NTR | As of |
|---|---:|---:|---:|---|
| 1 month | 6.14% | 6.12% | 6.20% | 2026-07-31 |
| YTD | 16.08% | 16.38% | 16.09% | 2026-07-31 |
| 1 year | 34.75% | 35.03% | 35.11% | 2026-07-31 |
| 3 years annualized | 27.34% | 27.17% | 27.69% | 2026-06-30 / 2026-07-31 source update |
| 5 years annualized | 13.05% | 13.11% | 13.43% | 2026-06-30 / 2026-07-31 source update |
| 10 years annualized | 10.66% | 10.60% | 11.06% | 2026-06-30 / 2026-07-31 source update |
| Since inception annualized | 8.41% | 8.44% | 8.82% | 2026-06-30 / 2026-07-31 source update |

The ALPS July performance update labels sub-one-year and one-year fields as
cumulative and longer fields as annualized. The June 30 official factsheet
separately reports NAV YTD `9.40%`, 1-year `27.38%`, 3-year `19.06%`, 5-year
`13.07%`, 10-year `10.65%` and since-inception `8.42%`; these earlier month-end
observations are not mixed with the July 31 update.

- Annual NAV TR coverage: official 2016-2025 NAV TR

| ปี | ETF NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 3.97% | 11.96% |
| 2017 | 25.81% | 21.83% |
| 2018 | -13.09% | -4.38% |
| 2019 | 20.86% | 31.49% |
| 2020 | -1.34% | 18.40% |
| 2021 | 11.36% | 28.71% |
| 2022 | -4.23% | -18.11% |
| 2023 | 22.64% | 26.29% |
| 2024 | 1.53% | 25.02% |
| 2025 | 39.83% | 17.88% |

**Up years / Down years**

- Complete calendar years available: `10`
- Up/down: `7 / 3`
- Best: 2025, `+39.83%`
- Least positive: 2024, `+1.53%`
- Worst: 2018, `-13.09%`
- Least bad down year: 2020, `-1.34%`
- Current YTD: `+16.08%` NAV TR as of `2026-07-31` (official ALPS update).

Rounded-input calendar calculations: 2016-2025 IDOG cumulative `151.71%`,
CAGR `9.67%`, population standard deviation `15.45%`; 2021-2025 cumulative
`85.69%`, CAGR `13.18%`. The cached S&P 500 TR reference is `298.33%` / `14.82%`
for 2016-2025 and `96.17%` / `14.43%` for 2021-2025.

## Risk read-through

IDOG เป็น `passive-index` ไม่ใช่ active manager strategy; ผลตอบแทนจึงสะท้อน
index construction และ tracking หลังหัก fund expenses. กลยุทธ์มุ่ง developed
markets นอก Americas, เลือกห้า highest-yielding stocks ในสิบ GICS sectors และ
โดยทั่วไปมีประมาณ 50 holdings ที่ equal-weight. Official June 30 factsheet
แสดง sector allocations ใกล้เคียงกันราว 9.20%-10.61% และ top 10 holdings รวม
หลายประเทศ/อุตสาหกรรม; ความเสี่ยงหลักคือ dividend/value และ mean-reversion
regime, sector/country concentration, foreign currency/geopolitical risk,
tracking error, liquidity และ expense drag จาก TER `0.50%`. Standard deviation,
max drawdown และ recovery จาก daily NAV ยังเป็น `ไม่พบข้อมูลที่ยืนยันได้`.

Official ALPS page’s dynamic pricing fields were blank in the current text
capture. Secondary cross-check reports market price `US$44.30` ณ 28 ส.ค. 2026
และ closing NAV `US$44.79` ณ 25 ส.ค. 2026; dates and source quality are kept
separate and these values are not used to calculate NAV Total Return.

## Sources

- [ALPS official product page](https://www.alpsfunds.com/exchange-traded-funds/idog) — identity, NYSE Arca listing, passive objective, index methodology, current document library and risk disclosures.
- [ALPS official July 2026 performance update](https://www.alpsfunds.com/perspectives/etf-spotlights/idog-cyclical-strength-pays-international-dividends-20260806?hs_amp=true) — July 31, 2026 rolling NAV/market-price/index returns and July performance context.
- [ALPS official June 30, 2026 fact sheet](https://www.alpsfunds.com/hubfs/alps-docs/lit/fs/alps-international-sector-dividend-dogs-etf-idog-fs.pdf) — fees, fund details, June rolling returns, holdings/sector snapshot and passive classification.
- [ALPS summary prospectus](https://www.alpsfunds.com/hubfs/alps-docs/reg/sum-pro/alps-international-sector-dividend-dogs-etf-idog-sum-pro.pdf) — objective, rules-based index construction, fee and risk disclosures.
- [Secondary current price cross-check](https://www.financecharts.com/etfs/IDOG/summary/price) and [secondary NAV cross-check](https://www.schwab.wallst.com/Prospect/Research/etfs/summary.asp?symbol=IDOG) — dated price/NAV observations only; not used in NAV TR calculations.
- Benchmark convention and cached 2016-2025 rows: [[ETF_performance_sources_2026-09-01_run-6]] | [[ETF Performance Index]]
