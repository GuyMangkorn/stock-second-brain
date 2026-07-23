---
type: etf-performance
instrument_type: ETF
entity_key: LSE:CEMA
ticker: CETFF
input_alias: CETFF
exchange: London Stock Exchange
fund: iShares MSCI EM Asia UCITS ETF USD (Acc)
tracked_index: MSCI EM Asia Index Net
benchmark: S&P 500 Total Return
updated: 2026-07-24
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/CETFF
  - ticker/CEMA
  - geography/Emerging-Markets
---

# CETFF Performance

> Navigation: [[ETF Region Index]] → [[Emerging Markets ETF]] → [[ETF Performance Index]]

## Bottom line

CETFF เป็น OTC alias ที่ resolve ได้เป็น iShares MSCI EM Asia UCITS ETF USD (Acc),
canonical `LSE:CEMA`, ISIN `IE00B5L8K969`. กองทุนเป็น passive, physical,
replicated, index-tracking equity ETF ที่ติดตาม MSCI EM Asia Index Net. Official
iShares performance page ให้ 10-year NAV Total Return cumulative `185.06%` และ
CAGR `11.04%` สำหรับ 2016-06-30 ถึง 2026-06-30 หรือ `10.00` elapsed years;
normalized TR คือ 100.00 เป็น 285.06. Current official NAV TR YTD ล่าสุดที่
ยืนยันได้คือ `28.17%` ณ 2026-06-30.

## Performance check

- input ticker: CETFF (OTC alias)
- entity_key: LSE:CEMA
- Inception: 2010-08-06
- Metric: NAV Total Return with gross income reinvested where applicable; iShares states performance is NAV-based and reflects fund expenses
- Tracked index (issuer benchmark): MSCI EM Asia Index Net
- Benchmark comparison: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark)
- 10-year NAV TR coverage: 2016-06-30 to 2026-06-30; actual years `10.00`
- 10-year NAV TR cumulative / CAGR: `185.06%` / `11.04%` (official iShares)
- Normalized NAV TR: start `100.00`; end `285.06` (official cumulative return; raw NAV endpoints are not disclosed)
- Calendar-row calculation: official 2016-2025 rows compound to `126.95%` / CAGR `8.54%`; official 2021-2025 rows compound to `19.44%` / CAGR `3.62%`
- Coverage/source note: rolling and current YTD figures are as of 2026-06-30; annual rows are official 2016-2025 observations. S&P 500 rows use the cached USD Total Return convention as of 2025-12-31.

| Year | CETFF / CEMA NAV TR | MSCI EM Asia Index Net TR | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | 5.48% | 6.14% | 11.96% |
| 2017 | 41.88% | 42.83% | 21.83% |
| 2018 | -15.99% | -15.45% | -4.38% |
| 2019 | 18.47% | 19.24% | 31.49% |
| 2020 | 27.57% | 28.38% | 18.40% |
| 2021 | -5.20% | -5.08% | 28.71% |
| 2022 | -21.00% | -21.11% | -18.11% |
| 2023 | 7.57% | 7.76% | 26.29% |
| 2024 | 11.98% | 11.96% | 25.02% |
| 2025 | 32.40% | 32.11% | 17.88% |

S&P 500 เป็น common reference benchmark ไม่ใช่ issuer benchmark ของ CEMA;
ตารางใช้ cached USD Total Return rows สำหรับ complete calendar years 2016-2025.

## Common-window comparison

- CEMA 2021-2025 NAV TR CAGR: `3.62%`
- S&P 500 2021-2025 TR CAGR: `14.43%`
- CEMA trails by approximately `10.81 pp` CAGR in the common calendar window.
- Up years / Down years in 2021-2025: `3 / 2`
- Best year: 2025, `32.40%`; worst year: 2022, `-21.00%`
- Latest standardized official NAV TR YTD: `28.17%` as of 2026-06-30

## Risk read-through

CEMA มี emerging-Asia exposure กระจุกใน technology, financials และประเทศอย่าง
Taiwan, South Korea, China และ India. Official iShares data ระบุ 549 holdings ณ
2026-07-20, total expense ratio `0.20%`, physical/replicated structure และ
3-year standard deviation `19.86%` ณ 2026-06-30. ความเสี่ยงหลักคือ country,
currency, policy/geopolitical, semiconductor/technology concentration และ
emerging-market volatility. Daily NAV history ที่ยืนยันได้เพียงพอสำหรับ
max drawdown และ recovery: `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- Official iShares product and performance page: https://www.ishares.com/uk/professional/en/products/253723/ishares-msci-em-asia-ucits-etf?siteEntryPassthrough=true&switchLocale=y
- Official iShares factsheet: https://www.ishares.com/uk/professional/en/literature/fact-sheet/csemas-ishares-msci-em-asia-ucits-etf-fund-fact-sheet-en-gb.pdf?siteEntryPassthrough=true&switchLocale=y
- OTC alias cross-check: https://stockanalysis.com/quote/otc/CETFF/
- Official S&P 500 index page: https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- ETF source batch: [[ETF_performance_sources_2026-07-24]] | [[ETF Performance Index]]
