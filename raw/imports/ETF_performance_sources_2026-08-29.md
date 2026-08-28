---
type: etf-performance-source-batch
workflow: check-etf-performance
batch_date: 2026-08-29
execution_profile: scheduled-inline
verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
pre_save_review: PASS
---

# ETF Performance Sources — 2026-08-29

## EWS — iShares MSCI Singapore ETF

- `entity_key`: `NYSE Arca:EWS`; issuer page identifies EWS as an Equity ETF listed on NYSE Arca, launched 1996-03-12, tracking `MSCI Singapore 25/50 Index`.
- Official product/performance source: https://www.blackrock.com/il/intermediaries/en/products/239678/ishares-msci-singapore-etf — current NAV `USD 34.12` as of 2026-08-26; NAV Total Return YTD `26.53%` as of 2026-08-25; net assets `USD 1,226,671,134` as of 2026-08-26; 17 holdings; expense ratio `0.50%`; 3-year standard deviation `12.34%` as of 2026-07-31; annual NAV and issuer-index rows for 2016-2025; rolling 10-year NAV TR `112.54%` cumulative / `7.83%` average annual as of 2026-06-30.
- Official factsheet: https://www.ishares.com/us/literature/fact-sheet/ews-ishares-msci-singapore-etf-fund-fact-sheet-en-us.pdf — factsheet as of 2026-06-30; precise 2021-2025 NAV TR rows `5.22%, -9.15%, 5.27%, 22.53%, 31.56%`; benchmark rows `5.65%, -8.76%, 6.10%, 23.15%, 32.17%`; NAV TR includes reinvested dividends/capital gains and deducts fund expenses.
- Official prospectus/source classification: https://www.ishares.com/us/literature/prospectus/p-ishares-inc-apac-8-31.pdf — EWS seeks to track an index of Singaporean equities; eligible passive single-country equity ETF. Exchange-traded futures are incidental cash/receivables management and do not change the classification.
- Common benchmark: cached `S&P 500 Total Return` convention for complete calendar years 2016-2025, USD, dividends reinvested, as of 2025-12-31; source references and rows are defined in the check-etf-performance skill. Current 2026 S&P comparison is not claimed.
- Calculations: issuer rolling 10-year normalized endpoint `100.00 → 212.54` from cumulative `112.54%`; `(212.54 / 100.00)^(1 / 10.00) - 1 = 7.83%`. 2021-2025 NAV compound `62.22%`, CAGR `10.16%`; issuer benchmark compound `67.32%`, CAGR `10.83%`; S&P 500 TR compound `96.17%`, CAGR `14.43%`. Rounded official 2016-2025 annual rows compound to `104.20%`, CAGR `7.40%`, retained as a separate rounded-input calculation.
- Evidence gaps: raw daily NAV TR endpoints and a daily NAV series for max drawdown/recovery are `ไม่พบข้อมูลที่ยืนยันได้`; early 2016-2020 issuer annual rows are displayed only to one decimal place. Latest detailed sector snapshot is as of 2026-08-12 (Financials 54.43%, Industrials 20.51%, Real Estate 7.91%, Consumer Discretionary 5.64%).
