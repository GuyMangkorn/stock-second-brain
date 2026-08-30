---
type: etf-performance
instrument_type: ETF
entity_key: LSE:IWQU
input_ticker: ISQWF
ticker: IWQU
exchange: London Stock Exchange
fund: iShares Edge MSCI World Quality Factor UCITS ETF U.S. Dollar (Accumulating)
tracked_index: MSCI World Sector Neutral Quality Index (Net)
benchmark: S&P 500 Total Return
management_mode: passive-index
implementation: physical-optimized
updated: 2026-08-31
performance_as_of: 2025-12-31
calendar_years_as_of: 2025-12-31
current_ytd_as_of: 2026-08-21
price_nav_as_of: 2026-08-24
fund_facts_as_of: 2026-08-24
source_batch: raw/imports/ETF_performance_sources_2026-08-31.md
return_basis: NAV total return; gross income reinvested; net of ongoing charges
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/IWQU
  - ticker/ISQWF
  - geography/International
  - geography/global-developed
  - style/passive-index
---

# ISQWF / IWQU ETF Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

ISQWF เป็น OTC input alias ของ official USD listing `LSE:IWQU` สำหรับ iShares
Edge MSCI World Quality Factor UCITS ETF. กองทุนเป็น passive, physical-optimized,
accumulating global developed-market quality-factor ETF ที่ติดตาม `MSCI World
Sector Neutral Quality Index (Net)` และมี TER `0.25%`. จาก complete official
calendar NAV Total Return rows ช่วง 2016-2025 ผลตอบแทนสะสม `202.69%` หรือ
rounded-input CAGR `11.71%†`; มีปีบวก/ลบ `9 / 1`. Current official NAV TR YTD
คือ `+13.26%` ณ 21 ส.ค. 2026.

## Performance check

- `entity_key: LSE:IWQU`; input card ticker: `ISQWF` (OTC alias); official USD listing: London Stock Exchange `IWQU`
- ISIN: `IE00BP3QZ601`; share-class launch: 3 ต.ค. 2014; asset class: equity; domicile: Ireland
- Metric: `NAV Total Return` รวม gross income ที่ reinvested และหัก ongoing charges; currency USD. Market-price return ไม่ถูกรวมใน ranking
- Management mode: `passive-index`; implementation: physical optimized; use of income: accumulating; TER `0.25%`
- Tracked index / issuer benchmark: `MSCI World Sector Neutral Quality Index (Net)`; common benchmark: `S&P 500 Total Return` (USD, dividends reinvested)
- 10-year calendar window: `2015-12-31` ถึง `2025-12-31`, represented by ten complete official calendar returns from 2016-2025
- Normalized TR endpoints from rounded official rows: `100.00 → 302.69`; years `10.00`; formula `(End TR / Start TR)^(1 / Years) - 1`; CAGR `11.71%†`
- 2021-2025 IWQU compound `68.41%` / rounded-input CAGR `10.99%`; S&P 500 common-reference compound `96.17%` / CAGR `14.43%`
- Coverage note: official factsheet rows are displayed to two decimals; `†` marks the calendar CAGR calculated from those rounded inputs. No secondary proxy is used.

| Year | IWQU NAV TR | Issuer benchmark | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | 5.03% | 5.05% | 11.96% |
| 2017 | 23.09% | 23.21% | 21.83% |
| 2018 | -7.31% | -7.20% | -4.38% |
| 2019 | 30.53% | 30.65% | 31.49% |
| 2020 | 14.91% | 14.98% | 18.40% |
| 2021 | 23.20% | 23.42% | 28.71% |
| 2022 | -19.20% | -19.16% | -18.11% |
| 2023 | 25.72% | 25.83% | 26.29% |
| 2024 | 16.62% | 16.81% | 25.02% |
| 2025 | 15.39% | 15.49% | 17.88% |

**Up years / Down years**

- Complete 2016-2025 years: `9 / 1`; 2021-2025 years: `4 / 1`
- Best: 2019, `+30.53%`; least positive: 2016, `+5.03%`
- Worst: 2022, `-19.20%`; least bad down year: 2022, `-19.20%`
- Current official NAV TR YTD: `+13.26%` as of `2026-08-21`; current NAV `US$90.42` as of `2026-08-24`
- IWQU beat the issuer benchmark in none of the displayed 2016-2025 rounded rows; this is a return-only tracking observation, not an active-management claim.

## Risk read-through

The official iShares snapshot reports NAV `US$90.42`, net assets `US$6.203B`,
and 301 holdings as of 24/21 Aug 2026, plus P/E `27.16x` and P/B `7.07x` as of
21 Aug 2026. The issuer reports 3-year standard deviation `12.05%` as of
31 Jul 2026. Quality-factor concentration can make the fund sensitive to factor
rotation, valuation, selected countries/sectors, mega-cap technology, and
foreign currency. Accumulating income is reinvested rather than paid as cash;
there is no separate latest-four-cash-distribution series for this share class.

Official daily NAV Total Return history sufficient for maximum drawdown, recovery
duration, downside capture, or compatible risk-adjusted persistence was not
verified (`ไม่พบข้อมูลที่ยืนยันได้`); no market-price or secondary proxy is
substituted. TER `0.25%`, sampling/optimization, trading, securities lending,
and fair-value timing can create tracking difference versus the issuer index.

## Sources

- [iShares IWQU product and performance page](https://www.ishares.com/uk/professionals/en/products/270054/?siteEntryPassthrough=true&switchLocale=y) — official identity, LSE USD listing, NAV/YTD, benchmark, TER, structure, holdings and risk fields
- [iShares IWQU factsheet](https://www.blackrock.com/no/intermediaries/literature/fact-sheet/iwqu-ishares-edge-msci-world-quality-factor-ucits-etf-fund-fact-sheet-en-no.pdf) — official 2016-2025 NAV/index rows, return definition, launch date and fund facts
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached `check-etf-performance` references — common USD total-return benchmark for complete 2016-2025 calendar years
- [[ETF_performance_sources_2026-08-31]] | [[ETF Performance Index]]
