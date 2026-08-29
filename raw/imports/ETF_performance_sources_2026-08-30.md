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
