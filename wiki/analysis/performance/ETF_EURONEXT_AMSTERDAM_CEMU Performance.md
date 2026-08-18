---
type: etf-performance
instrument_type: ETF
entity_key: Euronext Amsterdam:CEMU
input_ticker: XMTIF
ticker: CEMU
exchange: Euronext Amsterdam
fund: iShares Core MSCI EMU UCITS ETF EUR (Accumulating)
tracked_index: MSCI EMU Net Index (EUR)
benchmark: S&P 500 Total Return
management_mode: passive-index-tracking
updated: 2026-08-18
performance_as_of: 2025-12-31
rolling_10y_as_of: 2025-12-31
current_ytd_as_of: 2026-08-14
price_nav_as_of: 2026-08-17
fund_facts_as_of: 2026-08-14
source_batch: raw/imports/ETF_performance_sources_2026-08-18.md
return_basis: NAV total return; gross income reinvested where applicable
return_currency: EUR
tags:
  - analysis/etf-performance
  - ticker/CEMU
  - ticker/XMTIF
  - geography/Europe
---

# CEMU Performance

> Navigation: [[ETF Region Index]] → [[Europe ETF]] → [[ETF Performance Index]]

## Bottom line

`XMTIF` เป็น OTC input alias ของ official Euronext Amsterdam line
`Euronext Amsterdam:CEMU` สำหรับ iShares Core MSCI EMU UCITS ETF EUR
(Accumulating), ISIN `IE00B53QG562`. กองทุนเป็น passive, physically replicated,
accumulating UCITS equity ETF ที่ติดตาม `MSCI EMU Net Index (EUR)` และเปิดตัว
share class วันที่ 12 ม.ค. 2010. Official complete calendar rows 2016-2025 ให้
NAV TR cumulative `127.84%` / rounded-input CAGR `8.58%`; common 2021-2025 ให้
cumulative `75.96%` / CAGR `11.97%`, เทียบ tracked index ที่ `72.02%` / `11.46%`
จาก rounded rows. เทียบ S&P 500 TR common USD window ไม่ได้ใช้ เพราะ CEMU เป็น
EUR series; common reference ที่เก็บแยกคือ `96.17%` / `14.43%` ใน S&P 500 TR.
ล่าสุด official NAV TR YTD คือ `15.77%` ณ 14 ส.ค. 2026 และ NAV `€252.50` ณ
17 ส.ค. 2026.

## Performance check

- `entity_key: Euronext Amsterdam:CEMU`; `input_ticker: XMTIF`. Official iShares
  listings map the EUR accumulating share class to `CEMU` on Euronext Amsterdam;
  the OTC symbol is retained only as an input alias. The target share-class ISIN
  is `IE00B53QG562`.
- Classification: supported passive/index-tracking equity UCITS ETF; official
  materials describe physical replication, accumulating use of income, quarterly
  rebalancing and Ireland domicile. Share-class launch `2010-01-12`; ongoing
  charges `0.12%`.
- Tracked index: `MSCI EMU Net Index (EUR)`. The fund seeks to track developed
  EMU-country equity exposure; the issuer's benchmark rows and share-class NAV
  rows are both reported in EUR.
- Return basis: official NAV total return with gross income reinvested where
  applicable. The 2016-2025 table is a complete calendar-year window from the
  official factsheet; the `8.58%` 10-year CAGR is a rounded-input calendar CAGR,
  not an issuer-labeled rolling 10-year field.
- Official current snapshot: NAV `€252.50` as of 2026-08-17, NAV TR YTD
  `15.77%` as of 2026-08-14, fund net assets `€8.06B` as of 2026-08-17,
  share-class net assets `€6.40B`, and 220 holdings as of 2026-08-14.
- Official risk snapshot as of 2026-07-31: 3-year standard deviation `11.89%`
  and beta `1.004`. The issuer's 2026-08-14 snapshot shows P/E `19.36` and
  P/B `2.41`; sector weights include Financials `26.78%`, Industrials `20.26%`
  and Information Technology `15.93%`.
- Cash distribution: not applicable as a cash-income series for this
  accumulating share class; the official `Use of Income` field is
  `Accumulating`. No cash-distribution yield is inferred.

| Year | CEMU NAV TR (EUR) | MSCI EMU Net (EUR) |
|---|---:|---:|
| 2016 | 4.66% | 4.37% |
| 2017 | 12.75% | 12.49% |
| 2018 | -12.40% | -12.71% |
| 2019 | 26.22% | 25.47% |
| 2020 | -0.76% | -1.02% |
| 2021 | 22.73% | 22.16% |
| 2022 | -12.03% | -12.47% |
| 2023 | 19.29% | 18.78% |
| 2024 | 9.96% | 9.49% |
| 2025 | 24.25% | 23.70% |

The displayed-row arithmetic tracking difference is approximately `+8.91 pp`
cumulative / `+0.43 pp` CAGR over 2016-2025 and `+3.94 pp` cumulative /
`+0.51 pp` CAGR over 2021-2025. These are rounded-input comparisons, not
manager alpha; no active-management inference is made.

## Up years / Down years

- Complete 2016-2025 NAV TR up/down: `7 / 3`
- Best NAV TR year: 2025, `+24.25%`
- Worst NAV TR year: 2018, `-12.40%`
- Common 2021-2025 NAV TR cumulative/CAGR: `75.96%` / `11.97%`
- Common 2021-2025 tracked-index cumulative/CAGR: `72.02%` / `11.46%`
- Latest official NAV TR YTD: `+15.77%` ณ 14 ส.ค. 2026
- Common S&P 500 TR reference, kept on USD basis: `96.17%` / `14.43%` for
  2021-2025; it is not the tracked index of CEMU.

## Risk read-through

CEMU provides broad Eurozone equity exposure, but Financials, Industrials and
Information Technology are the largest sector exposures and country weights can
move with the EMU market. The accumulating structure retains income in NAV and
does not provide a cash-distribution yield. The official reviewed capture does
not disclose a daily NAV maximum drawdown or recovery date, and no price-only
proxy is substituted for that missing evidence. The rounded annual rows show
three down years in 2016-2025, including the `-12.40%` 2018 year.

## Sources

- [iShares Core MSCI EMU UCITS ETF product page](https://www.ishares.com/uk/individual/en/products/253729/ishares-core-msci-emu-ucits-etf) — official current EUR accumulating share-class NAV/YTD, assets, holdings, fee, risk snapshot and listings including Euronext Amsterdam CEMU
- [iShares CEMU/CEU1 factsheet](https://www.ishares.com/uk/individual/en/literature/fact-sheet/csemu-ishares-core-msci-emu-ucits-etf-fund-fact-sheet-en-gb.pdf?siteEntryPassthrough=true&switchLocale=y) — official 2016-2025 calendar rows, EUR benchmark rows, structure and trading lines
- [iShares EUR accumulating KIID](https://www.ishares.com/uk/individual/en/literature/kiid/ucits_kiid-ishares-core-msci-emu-ucits-etf-eur-acc-gb-ie00b53qg562-en.pdf?siteEntryPassthrough=true&switchLocale=y) — official passive/index objective and share-class risk/structure context
- [Stock Analysis XMTIF quote](https://stockanalysis.com/quote/otc/XMTIF/) — OTC alias identity cross-check only; not used as primary NAV performance evidence
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- Cached S&P 500 TR references: [2021](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/), [2022-2025](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/)
- ETF source batch: [[ETF_performance_sources_2026-08-18]] | [[ETF Performance Index]]
