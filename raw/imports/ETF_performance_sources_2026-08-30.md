---
type: etf-performance-source-batch
workflow: check-etf-performance
batch_date: 2026-08-30
execution_profile: scheduled-inline
verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
pre_save_review: PASS
---

# ETF Performance Sources — 2026-08-30

## ESGD — iShares ESG Aware MSCI EAFE ETF

- `entity_key`: `NASDAQ:ESGD`; the official iShares product page identifies ESGD as an Equity ETF listed on NASDAQ, launched 2016-06-28, tracking the `MSCI EAFE Extended ESG Focus Index`.
- Official product/performance source: https://www.ishares.com/us/products/283778/ishares-esg-msci-eafe-etf-fund_2 — NAV `USD 106.92`, closing price `USD 107.04`, net assets `USD 12,263,795,121`, and 354 holdings as of 2026-08-24; NAV Total Return YTD `14.42%` as of 2026-08-21; expense ratio `0.20%`; 3-year standard deviation `12.86%`, equity beta `0.67`, 30-day SEC yield `2.40%`, and 12-month trailing yield `3.26%` as of 2026-07-31.
- Official standardized performance from the same source: 10-year NAV Total Return `154.00%` cumulative / `9.77%` average annual as of 2026-06-30; official 2021-2025 calendar NAV rows are `11.60%, -14.96%, 18.08%, 3.80%, 29.98%` and benchmark rows are `11.66%, -15.08%, 18.22%, 4.04%, 29.67%`.
- Official fact sheet: https://www.ishares.com/us/literature/fact-sheet/esgd-ishares-esg-aware-msci-eafe-etf-fund-fact-sheet-en-us.pdf — confirms NAV Total Return assumes reinvestment of dividends/capital gains and deducts fund expenses; distribution frequency is semi-annual; benchmark is the MSCI EAFE Extended ESG Focus Index (Net).
- Official classification source: https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-esg-msci-eafe-etf-8-31.pdf — the fund seeks to track an index of international developed-market stocks excluding the U.S. and Canada with positive ESG characteristics; eligible passive/index-tracking international equity ETF. The benchmark history is spliced: MSCI EAFE ESG Focus Index (Net) through 2018-05-31 and MSCI EAFE Extended ESG Focus Index (Net) from 2018-06-01.
- Common benchmark: cached `S&P 500 Total Return` convention for complete calendar years 2021-2025, USD, dividends reinvested, as of 2025-12-31; source references and rows are defined in the `check-etf-performance` skill.
- Calculations: 10-year normalized TR endpoint `100.00 → 254.00` from official cumulative `154.00%`; `(254.00 / 100.00)^(1 / 10.00) - 1 = 9.77%`. 2021-2025 NAV compound `51.20%`, rounded-input CAGR `8.62%`; S&P 500 TR compound `96.17%`, CAGR `14.43%`; relative wealth `(1.51195 / 1.96170) - 1 = -22.93%`.
- Evidence gaps: the official page does not expose a raw daily NAV Total Return series sufficient for maximum drawdown/recovery, so these remain `ไม่พบข้อมูลที่ยืนยันได้`; no market-price or secondary proxy is substituted into the NAV ranking.

## IRRRF / IWDA — iShares Core MSCI World UCITS ETF

- `entity_key`: `LSE:IWDA`; input card ticker `IRRRF` is an OTC alias for the official USD London Stock Exchange line `IWDA`, ISIN `IE00B4L5Y983`. The official iShares page identifies the fund as an accumulating Equity UCITS ETF launched 2009-09-25 and tracking the `MSCI World Index (Net)`.
- Official product/performance source: https://www.ishares.com/uk/individual/en/products/251882/ishares-msci-world-ucits-etf-acc — NAV `USD 148.01`, share-class net assets `USD 148,885,441,084`, and 1,278 holdings as of 2026-08-27/28; NAV Total Return YTD `13.67%` as of 2026-08-27; 3-year beta `0.999` as of 2026-08-27; TER `0.20%`; 3-year standard deviation `12.42%` as of 2026-07-31; physical optimized replication and accumulating income structure.
- Official factsheet: https://www.ishares.com/uk/professional/en/literature/fact-sheet/swda-ishares-core-msci-world-ucits-etf-fund-fact-sheet-en-gb.pdf?siteEntryPassthrough=true&switchLocale=y — official USD NAV Total Return and MSCI World Net calendar rows for 2016-2025, with performance as of 2025-12-31 and fund facts through 2026-07-06; annual NAV rows are `7.73%, 22.45%, -8.65%, 27.76%, 15.95%, 21.90%, -18.03%, 23.86%, 18.70%, 21.16%`.
- Classification: supported passive/index-tracking developed-market equity ETF; the official product page lists London Stock Exchange USD `IWDA` and GBP `SWDA` listings for the same share class. The input alias is not mixed with a separate market-price series.
- Common benchmark: cached `S&P 500 Total Return` convention for complete calendar years 2016-2025, USD, dividends reinvested, as of 2025-12-31. Cached rows are `11.96%, 21.83%, -4.38%, 31.49%, 18.40%, 28.71%, -18.11%, 26.29%, 25.02%, 17.88%`; original references are https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true, https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf, https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/, https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/, and the index definition page https://www.spglobal.com/spdji/en/indices/equity/sp-500/.
- Calculations from rounded official annual rows: 2016-2025 IWDA cumulative `217.74%`, normalized endpoint `100.00 → 317.74`, 10-year calendar CAGR `12.26%†`; 2021-2025 cumulative `77.99%`, rounded-input CAGR `5.94%`; S&P 500 cumulative `298.33%` / CAGR `14.82%` for 2016-2025 and `96.17%` / `14.43%` for 2021-2025. `†` marks a calculation from displayed rounded inputs, not an issuer rolling field.
- Scheduled-local pre-save checklist: PASS — identity/exchange, NAV Total Return definition, accumulating distribution treatment, complete-year markers, common benchmark basis/window, as-of dates, calculations, source links, and unresolved gaps reconciled. `verification_mode: scheduled-local`; `reviewer_dispatch: not-attempted-by-design`.
- Evidence gaps: official daily NAV Total Return history sufficient for maximum drawdown and recovery was not verified; no market-price or secondary proxy is substituted. The 2016-2025 CAGR is a calendar-window calculation from rounded official rows rather than a separately reported rolling 10-year issuer field.
