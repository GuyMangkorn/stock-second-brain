---
type: etf-performance
instrument_type: ETF
entity_key: SIX Swiss Exchange:DFND
input_ticker: IVGAF
ticker: DFND
exchange: SIX Swiss Exchange
fund: iShares Global Aerospace & Defence UCITS ETF U.S. Dollar (Accumulating)
tracked_index: S&P Developed BMI Select Aerospace & Defense Capped Index
benchmark: S&P 500 Total Return
management_mode: passive-index
updated: 2026-09-02
performance_as_of: 2025-12-31
calendar_years_as_of: 2025-12-31
current_ytd_as_of: 2026-08-31
price_nav_as_of: 2026-08-31
fund_facts_as_of: 2026-08-31 / 2026-08-28
source_batch: raw/imports/ETF_performance_sources_2026-09-02_run-1.md
return_basis: NAV total return; gross income reinvested where applicable; net of expenses
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/IVGAF
  - ticker/DFND
  - geography/International
  - geography/global-developed
---

# IVGAF / DFND Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

IVGAF เป็น OTC input alias ของ official USD share class `SIX Swiss
Exchange:DFND` ของ iShares Global Aerospace & Defence UCITS ETF. กองทุนเป็น
passive, physical, accumulating sector equity ETF ที่ลงทุนใน developed-market
aerospace and defence companies. มี official complete calendar return ที่ยืนยัน
ได้เพียง 2025 ที่ `+54.55%`; จึงยังไม่มี 10-year หรือ multi-year CAGR และไม่ควร
จัดอันดับเป็นช่วงยาว. Current official NAV TR YTD ล่าสุดคือ `+7.13%` ณ
2026-08-31; NAV คือ `$9.73` ณ วันเดียวกัน.

## Performance check

- `entity_key: SIX Swiss Exchange:DFND`; input ticker `IVGAF` is a secondary OTC alias; official USD exchange listing is SIX Swiss Exchange `DFND` (listing date `2024-04-30`).
- Fund: `iShares Global Aerospace & Defence UCITS ETF U.S. Dollar (Accumulating)`; ISIN `IE000U9ODG19`; share-class/fund launch `2024-02-01`.
- Classification: `passive-index`; official iShares materials classify the product as `Equity`, `PASSIVE`, physical and replicated. The selected USD class is not leverage, inverse, option-income, bond, commodity, or multi-asset.
- Metric: `NAV Total Return` in USD with gross income reinvested where applicable and fund expenses reflected; market-price returns are separate.
- Tracked index: `S&P Developed BMI Select Aerospace & Defense Capped Index`; expense ratio `0.35%`; income treatment `Accumulating`.
- Current official snapshot: NAV `$9.73`, NAV TR YTD `+7.13%`, and net assets `$1.878B` as of 2026-08-31; holdings `77` as of 2026-08-28. The issuer also reports 99.83% industrials and 0.19% cash/derivatives as of 2026-08-31.
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference only). The only comparable complete calendar row is 2025, using the cached S&P 500 TR value `17.88%`.
- 10-year NAV TR CAGR: `not applicable`; the share class launched in 2024 and the official 2024 calendar cell is blank. No inception-year partial return is inferred or ranked.
- Coverage/source note: official July 2026 iShares factsheet provides the 2025 NAV row and benchmark row; the current product page provides the newer August 2026 NAV/YTD/fund-fact fields. The 2024 cell is not disclosed as a complete annual return.

| Year | DFND NAV TR | S&P 500 TR |
|---|---:|---:|
| 2025 | 54.55% | 17.88% |

**Up years / Down years**

- Up years / Down years: `1 / 0` across verified complete calendar years.
- Best: 2025, `+54.55%`.
- Least positive: 2025, `+54.55%`.
- Worst: `not applicable` — no verified complete down year.
- Least bad down year: `not applicable`.
- Current official NAV TR YTD: `+7.13%` as of 2026-08-31; no same-date S&P 500 TR comparison is asserted.

## Risk read-through

DFND มีข้อมูล annual return เพียงหนึ่ง complete year จึงยังไม่มี volatility,
maximum drawdown, recovery, downside capture หรือ compatible risk-adjusted
evidence ที่ยืนยันได้ (`ไม่พบข้อมูลที่ยืนยันได้`). ความเสี่ยงหลักคือ high
sector concentration ใน aerospace/defence, company/country concentration,
policy and procurement cycles, equity drawdown, FX ของหลักทรัพย์ต่างประเทศ,
liquidity และ counterparty risk จากธุรกรรมกองทุน. Current holdings `77` และ
industrials exposure `99.83%` สะท้อนความกระจุกตัว; TER `0.35%`.

## Sources

- [iShares DFND product page](https://www.ishares.com/uk/individual/en/products/334464/ishares-global-aerospace-defence-ucits-etf?siteEntryPassthrough=true&switchLocale=y) — official identity, USD share class, current NAV/YTD, benchmark, TER, structure, holdings, fund facts and exchange listings
- [iShares DFND July 2026 factsheet](https://www.ishares.com/uk/professional/en/literature/fact-sheet/dfnd-ishares-global-aerospace-defence-ucits-etf-fund-fact-sheet-en-gb.pdf?siteEntryPassthrough=true&switchLocale=y) — official 2025 calendar NAV/benchmark return, launch, USD accumulating treatment, and return definition
- [iShares DFND prospectus/KIID hub](https://www.ishares.com/uk/individual/en/products/334464/ishares-global-aerospace-defence-ucits-etf?siteEntryPassthrough=true&switchLocale=y) — official strategy and risk disclosures
- [Secondary OTC IVGAF profile](https://stockanalysis.com/quote/otc/IVGAF/) — alias and fund-name cross-check only; not used for NAV TR
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached `check-etf-performance` references — common USD Total Return benchmark for 2025
- Source batch: [[ETF_performance_sources_2026-09-02_run-1]] | [[ETF Performance Index]]
