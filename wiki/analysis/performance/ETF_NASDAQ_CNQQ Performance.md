---
type: etf-performance
instrument_type: ETF
entity_key: NASDAQ:CNQQ
ticker: CNQQ
exchange: NASDAQ
fund: Rayliant-ChinaAMC Transformative China Tech ETF
tracked_index: Solactive ChinaAMC Transformative China Tech Index
benchmark: S&P 500 Total Return
updated: 2026-07-24
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/CNQQ
  - geography/China
---

# CNQQ Performance

> Navigation: [[ETF Region Index]] → [[China ETF]] → [[ETF Performance Index]]

## Bottom line

CNQQ เป็น passive/index-tracking China technology equity ETF ที่ติดตาม
`Solactive ChinaAMC Transformative China Tech Index`. Official NAV Total Return
ตั้งแต่ inception `2025-09-24` ถึง `2026-06-30` อยู่ที่ cumulative `6.54%` หรือ
ประมาณ `0.764 elapsed years`; annualized CAGR ที่คำนวณจากช่วงสั้นนี้คือ
`8.65% derived`. จึงต้องระบุชัดว่า `10-year NAV TR unavailable`. Official
current NAV TR YTD ล่าสุดที่เปิดเผยคือ `14.95%` ณ `2026-06-30`.

## Performance check

- `entity_key`: `NASDAQ:CNQQ`
- Inception: `2025-09-24` จาก official product page, summary prospectus and annual report. The factsheet says `2025-09-25`; this one-day conflict is disclosed and the formal product/prospectus date is used.
- Expense ratio: `0.75%`
- Metric: official NAV return/Total Return; Rayliant separates NAV return from market-price return, and the annual report defines total return assuming reinvestment of dividends and distributions.
- Tracked index: `Solactive ChinaAMC Transformative China Tech Index`
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark)
- 10-year NAV TR: unavailable because inception is `2025-09-24`.
- Available-period window: `2025-09-24` to `2026-06-30`; `279 days / 0.764 elapsed years`.
- Market-price return is not mixed with NAV Total Return.

### Available-period NAV TR

Raw NAV endpoints are not disclosed as a time series. The normalized endpoints
below represent the issuer's published cumulative NAV return and are not a
market-price proxy.

| Start date | End date | Actual years | Start TR value | End TR value | Cumulative NAV TR | CAGR |
|---|---|---:|---:|---:|---:|---:|
| 2025-09-24 | 2026-06-30 | 0.764 | 100.00 normalized | 106.54 derived | 6.54% official | 8.65% derived |

- `106.54 = 100.00 × (1 + 6.54%)`.
- `CAGR = (106.54 / 100.00)^(1 / 0.763876) - 1 = 8.65%`; this annualization is a derived statistic over less than one year and is not a 10-year result.
- Current NAV TR YTD: `14.95%` as of `2026-06-30`.
- The factsheet's earlier Q1 2026 NAV since-inception figure was `-15.16%` as of `2026-03-31`; the later official product page observation is used for the current record and both as-of dates remain distinct.

### Annual NAV TR vs S&P 500 TR

CNQQ has no complete calendar year since inception in the reviewed official
capture. S&P 500 rows for 2016-2025 reuse the cached USD Total Return convention
recorded in the dated source batch; they are context only where CNQQ did not yet
exist or where the ETF annual row is not disclosed.

| Year | CNQQ NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | not applicable; before inception | 11.96% |
| 2017 | not applicable; before inception | 21.83% |
| 2018 | not applicable; before inception | -4.38% |
| 2019 | not applicable; before inception | 31.49% |
| 2020 | not applicable; before inception | 18.40% |
| 2021 | not applicable; before inception | 28.71% |
| 2022 | not applicable; before inception | -18.11% |
| 2023 | not applicable; before inception | 26.29% |
| 2024 | not applicable; before inception | 25.02% |
| 2025 | not disclosed; incomplete inception year | 17.88% |
| 2026 YTD | 14.95% as of 2026-06-30 | not comparable; current-year S&P row not cached |

## Up years / Down years

- Complete calendar-year up/down count: not disclosed; no complete calendar year has been reported since inception.
- Best / worst calendar year: not disclosed.
- Available-period cumulative return / annualized CAGR: `6.54% official` / `8.65% derived`.
- 10-year NAV TR: unavailable because the fund's inception is `2025-09-24`.

## Risk read-through

CNQQ มี China technology/innovation, policy, geopolitical, A-share/H-share,
sector, FX และ emerging-market risk สูง. Official strategy ลงทุนอย่างน้อย 80%
ใน securities ของ index หรือ participatory notes และอาจใช้ total return swaps
บน index; จึงมี counterparty/derivatives/valuation risk แม้ fund จะเป็น
index-tracking. Holdings ณ 2026-07-07 กระจุกใน Tencent, Zhongji Innolight,
Alibaba, CATL และ technology/consumer/industrials. ประวัติสั้นและผลตอบแทน
available-period ไม่ควรถูกตีความเป็น evidence ของ 10-year compounding.

## Sources

- [Official Rayliant CNQQ product/performance page](https://funds.rayliant.com/cnqq/)
- [Official Rayliant CNQQ factsheet](https://funds.rayliant.com/wp-content/uploads/FactSheets/Rayliant-CNQQ-ETF.pdf)
- [SEC CNQQ summary prospectus](https://www.sec.gov/Archives/edgar/data/2061770/000158064226000606/rayliantchinaetf497k.htm)
- [Official CNQQ prospectus](https://funds.rayliant.com/wp-content/uploads/ETF/CNQQ/Rayliant-CAMC-CNQQ-Prospectus.pdf)
- [Official CNQQ annual shareholder report](https://funds.rayliant.com/wp-content/uploads/ETF/CNQQ/Rayliant-CNQQ-Annual-Shareholder-Report.pdf)
- [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/); complete-year rows use the cached convention documented in [[ETF_performance_sources_2026-07-24]].
