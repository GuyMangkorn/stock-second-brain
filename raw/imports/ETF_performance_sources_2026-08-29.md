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

## EWT — iShares MSCI Taiwan ETF

- `entity_key`: `NYSE Arca:EWT`; official BlackRock/iShares page identifies EWT as an Equity ETF listed on NYSE Arca, launched 2000-06-20, tracking `MSCI Taiwan 25/50 Index`.
- Official product/performance source: https://www.blackrock.com/us/individual/products/239686/ishares-msci-taiwan-etf — current NAV `USD 108.51` and closing price `USD 108.63` as of 2026-08-27; NAV Total Return YTD `70.74%` as of 2026-08-27; net assets `USD 11,772,851,445`; 79 holdings; expense ratio `0.59%`; 3-year standard deviation `24.80%` and beta `1.33` as of 2026-07-31; annual NAV rows 2021-2025; rolling 10-year NAV TR `552.21%` cumulative / `20.63%` average annual as of 2026-06-30.
- Official performance definition: issuer hypothetical-growth convention reinvests dividends and capital gains and deducts fund expenses; market-price rows are kept separate from NAV TR. The source reports 2021-2025 NAV rows `28.38%, -28.75%, 29.15%, 16.79%, 27.81%` and issuer benchmark rows `29.40%, -28.12%, 29.52%, 17.50%, 28.17%`.
- Official classification source: https://www.blackrock.com/us/individual/products/239686/ishares-msci-taiwan-etf — investment objective is to track an index of Taiwanese equities; eligible passive single-country equity ETF. Exchange-traded futures are described as incidental cash/receivables management.
- Common benchmark: cached `S&P 500 Total Return` convention for 2021-2025, USD, dividends reinvested, as of 2025-12-31; current 2026 S&P comparison is not claimed.
- Calculations: 10-year normalized TR endpoint `100.00 → 652.21` from issuer cumulative `552.21%`; `(652.21 / 100.00)^(1 / 10.00) - 1 = 20.63%`. 2021-2025 NAV compound `76.34%`, CAGR `12.01%`; S&P 500 TR compound `96.17%`, CAGR `14.43%`.
- Evidence gaps: raw per-share TR endpoints and a daily NAV series sufficient for official max drawdown/recovery are `ไม่พบข้อมูลที่ยืนยันได้`; current YTD is a date-to-date issuer observation, while the standardized performance table is as of 2026-06-30.

## FXI — iShares China Large-Cap ETF

- `entity_key`: `NYSE Arca:FXI`; official BlackRock/iShares pages identify FXI as an Equity ETF listed on NYSE Arca, launched 2004-10-05, tracking `FTSE China 50 Index (Net)`, with semi-annual distributions and expense ratio `0.73%`.
- Official current fund data: https://www.blackrock.com/us/individual/products/overview-v3-ishares-fund-data?portfolioId=239536&seoSlug=ishares-china-largecap-etf — NAV `USD 35.63`, closing price `USD 35.55`, net assets `USD 4,249,043,534`, 50 holdings, and premium/discount `-0.23%`, all as of 2026-08-26; NAV Total Return YTD `-6.68%` as of 2026-08-26.
- Official risk/portfolio snapshot: same BlackRock source reports sector weights as of 2026-08-26: Financials `35.32%`, Consumer Discretionary `26.13%`, Communication `15.33%`, Information Technology `5.93%`; 3-year standard deviation `22.02%` and beta `0.26` as of 2026-07-31; 30-day SEC yield `2.00%` and trailing 12-month yield `1.86%` as of 2026-07-31.
- Official standardized performance: BlackRock page https://www.blackrock.com/us/individual/products/239536/ishares-china-large-cap-etf reports 10-year NAV TR cumulative `18.94%` / average annual `1.75%` and benchmark cumulative `27.79%` / average annual `2.48%` as of 2026-06-30; annual NAV rows 2021-2025 are `-21.04%, -20.40%, -12.87%, 30.10%, 29.01%`, with benchmark rows `-19.99%, -19.54%, -12.92%, 31.98%, 29.11%`. The issuer convention reinvests dividends/capital gains and deducts fund expenses.
- Official classification: the investment objective is to track an index of large-cap Chinese equities listed on the Hong Kong Stock Exchange; eligible passive/index-tracking single-country equity ETF. Exchange-traded index futures are described as cash/receivables management and do not change the classification.
- Common benchmark: cached `S&P 500 Total Return` convention for complete calendar years 2021-2025, USD, dividends reinvested, as of 2025-12-31; current 2026 S&P comparison is not claimed.
- Calculations: 2021-2025 FXI NAV compound `-8.08%`, CAGR `-1.67%`; S&P 500 TR compound `96.17%`, CAGR `14.43%`. The issuer's 10-year cumulative `18.94%` normalizes to `100.00 → 118.94`; `(118.94 / 100.00)^(1 / 10.00) - 1 = 1.75%`.
- Source reconciliation note: the official BlackRock US current-data snapshot used above is dated 2026-08-26; BlackRock AE's regional page separately displayed NAV TR YTD `-6.85%` as of 2026-08-25. These are different site/as-of observations, so the later US snapshot is used and the difference is preserved rather than arithmetically reconciled.
- Evidence gaps: raw daily NAV TR endpoints and an official daily series sufficient to calculate max drawdown/recovery are `ไม่พบข้อมูลที่ยืนยันได้`; secondary drawdown history remains dated proxy evidence only.

## GMF — State Street SPDR S&P Emerging Asia Pacific ETF

- `entity_key`: `NYSE Arca:GMF`; official State Street page identifies GMF as a passively managed Equity ETF listed on NYSE Arca, launched 2007-03-20, tracking `S&P Emerging Asia Pacific BMI Index`, with semi-annual distributions and gross expense ratio `0.49%`.
- Official current fund data: https://www.ssga.com/us/en/intermediary/etfs/state-street-spdr-sp-emerging-asia-pacific-etf-gmf — NAV `USD 158.03` and assets under management `USD 434.59M` as of 2026-08-27; fund information and listing data as of 2026-08-28; closing price `USD 157.38`, premium/discount `-0.35%`, 30-day median bid/ask spread `0.19%` as of 2026-08-27; 1,288 holdings, P/B `2.24`, and P/E FY1 `15.96` as of 2026-08-27; 30-day SEC yield `1.22%` as of 2026-08-26.
- Official standardized performance from the same State Street page: as of 2026-07-31 NAV YTD `9.44%`, 1-year `19.52%`, 3-year `15.31%`, 5-year `6.38%`, 10-year `9.17%`, and since inception `7.20%`; benchmark YTD `9.41%` and 10-year `9.23%`. The issuer states results assume reinvestment of dividends/capital gains and are shown net of fees.
- Prior official workbook cross-check retained from the 2026-06-30 window: daily NAV/distribution inputs produced cumulative `158.00%` and CAGR `9.94%`; this is a separate earlier as-of window, not substituted for the latest July standardized 10-year figure. The 2021-2025 annual rows are `-1.49%, -19.00%, 7.88%, 17.01%, 21.94%` and were calculated from the official NAV/distribution workbooks.
- Official classification: State Street describes GMF as passively managed/index-sampling and designed to track the benchmark; eligible passive emerging Asia-Pacific equity ETF.
- Common benchmark: cached `S&P 500 Total Return` convention for complete calendar years 2021-2025, USD, dividends reinvested, as of 2025-12-31; current 2026 S&P comparison is not claimed.
- Calculations: 2021-2025 GMF NAV compound `22.83%`, CAGR `4.20%`; S&P 500 TR compound `96.17%`, CAGR `14.43%`. Latest official July standardized 10-year cumulative is `not disclosed`, so no normalized endpoint is inferred for that window.
- Evidence gaps: current compact State Street output does not disclose latest July 10-year cumulative NAV TR or raw endpoints; latest detailed country/sector weights in the reviewed factsheet remain as of 2026-06-30, while current page provides current holdings/characteristics and top holdings.

## GSEU — Goldman Sachs ActiveBeta Europe Equity ETF

- `entity_key`: `NYSE Arca:GSEU`; official Goldman Sachs factsheet identifies GSEU as an Equity ETF listed on NYSE Arca, launched 2016-03-02, tracking the `Goldman Sachs ActiveBeta Europe Equity Index`, with quarterly distributions and total expense ratio `0.25%`.
- Official factsheet: https://am.gs.com/public-assets/documents/570151a1-24d6-11ef-870d-25a687970406 — as of 2026-07-31, NAV YTD `9.78%`, 1-year `22.13%`, 3-year annualized `15.88%`, 5-year annualized `8.85%`, 10-year annualized `9.70%`, and since-inception annualized `9.97%`; strategy benchmark YTD `9.80%`, 1-year `22.30%`, 3-year `15.98%`, 5-year `8.84%`, 10-year `9.75%`, and since-inception `10.01%`.
- The same official factsheet reports `346` holdings, net assets `USD 120.87M`, P/B `2.35`, P/E `18.52`, dividend yield `2.94%`, and 30-day SEC yield `2.30%`, all as of 2026-07-31. It reports calendar NAV Total Return rows for 2017-2025; the 2021-2025 rows are `16.78%, -18.12%, 20.86%, 1.63%, 36.41%`, with benchmark rows `16.30%, -15.06%, 19.89%, 1.78%, 35.41%`.
- Official classification: the prospectus and factsheet state that GSEU is not actively managed and seeks to track the ActiveBeta index; it is a passive strategic-beta Europe equity ETF. The index uses value, momentum, quality and low-volatility factors and rebalances quarterly.
- Common benchmark: cached `S&P 500 Total Return` convention for complete calendar years 2021-2025, USD, dividends reinvested, as of 2025-12-31; S&P is a common reference only, not GSEU's strategy benchmark.
- Calculations: GSEU 2021-2025 NAV compound `60.21%`, CAGR `9.89%`; population standard deviation of the five official annual NAV returns `18.50%`. Strategy-benchmark differences are `-0.02 pp` YTD, `-0.17 pp` 1-year, and `-0.05 pp` 10-year annualized based on the official July table.
- Evidence gaps: the reviewed official factsheet does not expose an exact latest NAV or market price in text; current price/NAV and official daily NAV drawdown/recovery remain `ไม่พบข้อมูลที่ยืนยันได้`. Latest verified official performance remains the 2026-07-31 month-end snapshot.
