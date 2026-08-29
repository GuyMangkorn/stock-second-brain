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

## GWX — State Street SPDR S&P International Small Cap ETF

- `entity_key`: `NYSE Arca:GWX`; official State Street page identifies GWX as a passively managed Equity ETF listed on NYSE Arca, launched 2007-04-20, tracking `S&P Developed Ex-U.S. Under USD2 Billion Index`, with semi-annual distributions and gross expense ratio `0.40%`.
- Official current fund data: https://www.ssga.com/us/en/individual/etfs/state-street-spdr-sp-international-small-cap-etf-gwx — NAV `USD 46.56`, shares outstanding `20.20M`, and assets under management `USD 940.44M` as of 2026-08-26; closing price `USD 46.71`, premium/discount `0.05%`, and bid/ask midpoint `USD 46.58` as of 2026-08-26.
- Official current characteristics: same State Street page reports 2,081 holdings, P/B `1.36`, P/E FY1 `14.21`, and weighted average market cap `USD 1,639.23M` as of 2026-08-26; 30-day SEC yield `1.87%`, fund distribution yield `2.57%`, and index dividend yield `2.41%` as of 2026-08-26. Sector weights as of 2026-08-25 are Industrials `22.35%`, Materials `15.62%`, Information Technology `13.94%`, Consumer Discretionary `10.87%`, and Financials `8.78%`.
- Official standardized performance from the same State Street page: as of 2026-07-31 NAV YTD `7.28%`, 1-year `19.13%`, 3-year `13.82%`, 5-year `5.15%`, 10-year `6.86%`, and since inception `4.49%`; benchmark YTD `5.91%` and 10-year `6.64%`. The issuer states returns assume reinvestment of dividends/capital gains and are shown net of fees.
- Official classification: State Street describes GWX as passively managed/index-sampling exposure to developed-market companies outside the United States with market capitalization under USD 2 billion; eligible passive international ex-U.S. small-cap equity ETF.
- Common benchmark: cached `S&P 500 Total Return` convention for complete calendar years 2021-2025, USD, dividends reinvested, as of 2025-12-31; current 2026 S&P comparison is not claimed.
- Calculations: 2021-2025 annual NAV rows and CAGR remain `not disclosed` because the reviewed official capture does not publish complete calendar-year NAV rows; no secondary annual proxy is saved due to prior conflict with official prospectus data.
- Evidence gaps: raw 10-year NAV TR endpoints, complete annual NAV rows, volatility/beta, and official daily NAV drawdown/recovery are `ไม่พบข้อมูลที่ยืนยันได้` in the reviewed official sources. The June 2026 standardized snapshot remains a separate dated observation and is not mixed with the July 2026 data.

## GXC — State Street SPDR S&P China ETF

- workflow: check-etf-performance; execution_profile: scheduled-inline; entity_key: NYSE Arca:GXC; issuer State Street Investment Management; NYSE Arca listing; inception 2007-03-20; passive/index-tracking equity ETF; tracked index S&P China BMI Index.
- Official product/performance source: https://www.ssga.com/us/en/intermediary/etfs/state-street-spdr-sp-china-etf-gxc — standardized NAV/market-value/index performance as of 2026-07-31: NAV YTD -6.10%, 1-year 1.02%, 3-year 6.94%, 5-year -2.14%, 10-year average annual 4.61%, since inception average annual 4.97%; issuer benchmark YTD -6.47%, 1-year 0.40%, 3-year 7.05%, 5-year -2.08%, 10-year 4.69%, since inception 5.13%.
- Current official fund and market data from the same source: NAV USD 91.05, closing price USD 91.00, bid/ask midpoint USD 90.89, premium/discount -0.18%, 30-day median bid/ask spread 0.22%, all as of 2026-08-26; AUM USD 473.46M and 5.20M shares as of 2026-08-26; fund/listing information as of 2026-08-27; gross expense ratio 0.59%.
- Current official characteristics as of 2026-08-26: 1,365 holdings, P/B 1.40, P/E FY1 11.18, weighted average market cap USD 111,664.81M, 30-day SEC yield 1.72%, distribution yield 2.19%, index dividend yield 2.33%; sector weights Consumer Discretionary 21.62%, Financials 18.26%, Communication Services 13.74%, Information Technology 12.56%, Industrials 9.29%, Materials 7.11%, Health Care 7.03%.
- Return basis and units: official NAV Total Return in USD, distributions/capital gains reinvested and fund expenses deducted; market-value return and S&P China BMI benchmark return kept separate. Common S&P 500 Total Return reference is cached for complete calendar years 2016-2025 only, USD, dividends reinvested, as of 2025-12-31.
- Annual/calendar candidate claims: GXC and S&P China BMI annual NAV/index rows for 2016-2025 are not readable or disclosed in the reviewed current capture; GXC 2016-2025 and 2021-2025 CAGR, up/down counts, best/worst year and exact spread are not disclosed. No third-party annual proxy is substituted. Cached S&P 500 rows retained: 2016 11.96%, 2017 21.83%, 2018 -4.38%, 2019 31.49%, 2020 18.40%, 2021 28.71%, 2022 -18.11%, 2023 26.29%, 2024 25.02%, 2025 17.88%.
- As-of reconciliation: the earlier June 2026 State Street observation was NAV YTD -10.99% as of 2026-06-30; the July 2026 standardized NAV YTD -6.10% is later and is used for the refreshed page. They are retained as separate dated observations, not arithmetically reconciled.
- Evidence gaps: raw 10-year NAV TR endpoints, cumulative return, complete calendar-year NAV/index rows, daily NAV series for volatility/max drawdown/recovery, and exact current daily NAV TR path are not verified in the reviewed official capture.
- Pre-save evidence packet: identity/exchange, return basis, benchmark, candidate claims, periods, units/currency, metric definitions, as-of dates, source URL, reconciliation note, unresolved gaps, and proposed file contents were checked locally. Proposed durable contents: refresh GXC performance page with latest July standardized returns and August fund facts; update the China ETF region snapshot; update ETF Performance Index coverage row/date; append this source-batch section; append one dated workflow bullet to log.md.
- Pre-save checklist: source identity verified; passive equity classification verified; NAV TR versus market-value and issuer-index bases separated; latest/as-of dates recorded per metric; no unsupported annual rows or cumulative value inferred; cached S&P convention applied only to 2016-2025; links and breadcrumb preserved; all durable numbers trace to the official State Street page or cached S&P references; result PASS.
- verification_mode: scheduled-local
- reviewer_dispatch: not-attempted-by-design

## FTDPF / FTEU — First Trust Eurozone AlphaDEX UCITS ETF

### Identity and classification

- `workflow: check-etf-performance`; `execution_profile: scheduled-inline`; input ticker `FTDPF` is an OTC alias for the First Trust Eurozone AlphaDEX UCITS ETF, while the official factsheet maps ISIN `IE00B8X9NY41` to the London Stock Exchange USD line `FTEU LN`. Durable ownership remains `entity_key: LSE:FTEU`, with `input_ticker: FTDPF` preserved.
- Official fund/share-class inception is `2014-10-21`; Ireland-domiciled UCITS; equity; accumulating; base currency EUR; ongoing charges `0.65%`; physical full replication; semi-annual rebalance; official tracking-index label `Nasdaq AlphaDEX Eurozone Index`.
- The official factsheet describes the fund as passively managed and index-tracking. The index ranks growth and value factors, selects the top 150 stocks, applies country/sector constraints, and reconstitutes semi-annually. This is an eligible passive, index-tracking equity ETF.
- Primary region is `Europe`; the existing `[[Europe ETF]]` page and `[[ETF Performance Index]]` row are the navigation owners.

### Source map

| Source | URL/path | Use |
|---|---|---|
| First Trust official factsheet, data as of 2026-07-31 | https://www.fundslibrary.co.uk/FundsLibrary.DataRetrieval//Documents.aspx?id=db97fa3f-452a-4e87-a092-5d78014ea6e7&type=packet_fund_class_doc_factsheet_private&user=fidelitydocumentreport | ISIN, official trading lines, inception, fee, UCITS/passive/physical structure, official Acc EUR performance and exposures |
| Fidelity document page | https://www.fidelity.co.uk/factsheet-data/factsheet/IE00B8X9NY41-first-trust-global-funds-icav/charges-and-key-documents | Discovery and confirmation that the provider factsheet posted 2026-08-18 is the 2026-07-31 factsheet |
| Morningstar FTEU report | https://lt.morningstar.com/1c6qh1t6k9/etfreport/default.aspx?1=1&ClientFund=0&CurrencyId=USD&Id=0P00018JZQ&SecurityToken=0P00018JZQ%5D22%5D0%5DETEXG%24XLON&tab=1 | Secondary USD annual rows as of 2026-07-31 and trailing fields as of 2026-08-27 |
| Central Bank of Ireland fund register | https://registers.centralbank.ie/%28X%281%29S%28uzbkfrrwrh3qjlqvxporqnfl%29%29/FundRegisterDataPage.aspx?fundReferenceNumber=C118215&register=28 | UCITS fund identity and regulatory status |
| Cached benchmark convention | workflow cache; original S&P references are listed on the performance page | S&P 500 Total Return common-reference rows for 2021-2025, USD, dividends reinvested |

### Candidate performance claims and raw observations

- Official First Trust factsheet as of `2026-07-31`: Acc EUR NAV total return YTD `14.55%`, 1-year `25.43%`, 3-year annualised `20.33%`, 5-year annualised `11.86%`, and since-inception annualised `10.61%`; corresponding index fields are `14.64%`, `25.63%`, `20.22%`, `11.91%`, and `10.95%`.
- The same official factsheet reports total fund AUM `€127.83 million`, outstanding shares `1,641,580`, and country exposure Germany `21.36%`, France `20.77%`, Italy `14.27%`, The Netherlands `9.26%`, Spain `9.15%`; sector exposure is Industrials `21.60%`, Financials `12.02%`, Materials `11.55%`, Energy `11.14%`, Utilities `9.40%`, and Consumer Discretionary `8.86%`, all as of `2026-07-31`.
- Official factsheet performance is in the EUR base/Acc EUR series and is net of fees with reinvested income. It uses the label `Nasdaq AlphaDEX Eurozone Index`; the previous 2026-08-18 batch used an NTR label for the return series. This naming difference is preserved as a source-language distinction and does not change the ISIN or share-class identity.
- Secondary Morningstar USD annual rows as of `2026-07-31` are 2021 `12.59%`, 2022 `-19.74%`, 2023 `16.65%`, 2024 `3.03%`, and 2025 `57.98%`; secondary trailing fields as of `2026-08-27` are YTD `14.06%`, 1-year `24.60%`, 3-year annualised `25.55%`, 5-year annualised `10.92%`, and 10-year annualised `10.63%`.
- Morningstar identifies its comparator as `Morningstar Developed Eurozone Target Market Exposure NR EUR`, not the official AlphaDEX strategy benchmark; no Morningstar benchmark gap is treated as manager alpha or issuer tracking evidence.
- A current FTEU USD-LSE price/NAV pair was not disclosed in the reviewed official or secondary capture. The U.S.-listed FEUZ price/NAV is a different security and is not substituted. Official daily NAV history sufficient for maximum drawdown/recovery is also `ไม่พบข้อมูลที่ยืนยันได้`.

### Calculations and reconciliation

- Secondary USD 2021-2025 cumulative return: `(1.1259 × 0.8026 × 1.1665 × 1.0303 × 1.5798) - 1 = 71.57%`; rounded-input CAGR `(1 + 0.7157)^(1/5) - 1 = 11.40%`; population standard deviation of the five annual returns `25.31%`; up/down years `4 / 1`.
- Cached S&P 500 Total Return common reference for 2021-2025 is cumulative `96.17%` / rounded-input CAGR `14.43%`; this is USD, dividends reinvested, and is not FTEU's strategy benchmark.
- The 10-year field `10.63%*` and YTD `14.06%*` are kept as secondary USD observations as of `2026-08-27`; official EUR observations are not currency-converted into the USD series. No cross-currency excess-return calculation is made.
- No official USD calendar-year table, current USD-LSE NAV/price pair, or daily NAV drawdown/recovery series was exposed. The prior annual table and current trailing metrics are retained with `*` secondary markers rather than upgraded to official issuer NAV claims.

### Pre-save evidence packet and proposed durable contents

- Evidence packet records ETF identity and exchange, OTC alias, ISIN, return bases, official and common benchmarks, all candidate annual/trailing/rolling claims, periods, units and currencies, metric definitions, as-of dates, source URLs, calculations, source-label reconciliation, unresolved gaps, and the complete planned contents.
- Proposed `wiki/analysis/performance/ETF_LSE_FTEU Performance.md`: refresh frontmatter/source batch, retain the 2021-2025 USD annual table and calculations, update official Acc EUR and secondary USD current fields, update exposure/risk notes, disclose no current USD-LSE price/NAV and no daily NAV drawdown series, and preserve the canonical breadcrumb and alias tags.
- Proposed `wiki/analysis/comparisons/Europe ETF.md`: update only the FTEU row and its explanatory note to secondary USD 10-year `10.63%*` and YTD `14.06%*` as of 2026-08-27.
- Proposed `wiki/analysis/performance/ETF Performance Index.md`: update only the FTEU row and explanatory note with the same dated secondary metrics and gap disclosure.
- Proposed `raw/imports/ETF_performance_sources_2026-08-29.md`: append this evidence packet, local checklist, and structured `trello_handoff`.
- Proposed `log.md`: append one `etf-performance` workflow bullet listing the FTEU performance page, Europe region/index updates, and the scheduled-local PASS; `log.md` remains outside the scoped commit because it already contains unrelated user changes.

### Local pre-save checklist

- PASS: official ISIN/share-class mapping, canonical `LSE:FTEU` exchange key, OTC alias, passive equity classification, tracked index, return bases, units/currencies, periods, metric definitions, and as-of dates are recorded.
- PASS: official EUR Acc performance and secondary USD FTEU performance are separated; no FEUZ U.S.-listed price/NAV is substituted; Morningstar's non-official comparator is not treated as the strategy benchmark; the current USD-LSE price/NAV and daily drawdown gaps are disclosed.
- PASS: calculations reproduce secondary USD 2021-2025 cumulative/CAGR and dispersion; the cached S&P 500 TR comparison is labeled common reference only; no cross-currency calculation or unsupported official USD calendar claim is made.
- PASS: complete proposed contents for performance, region, index, source batch, and log artifacts are specified; canonical breadcrumb, alias tags, region ownership, and source links are preserved; no unresolved High/Medium finding blocks the write and no WARNING requiring confirmation remains.
- verification_mode: scheduled-local
- reviewer_dispatch: not-attempted-by-design

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official July factsheet and current secondary USD evidence support the FTEU refresh; the scheduled-local checklist passed and currency, source-label, price/NAV, and drawdown gaps remain disclosed.

## DDLS — WisdomTree Dynamic International SmallCap Equity Fund

- `workflow: check-etf-performance`; `execution_profile: scheduled-inline`; `entity_key: Cboe BZX:DDLS`; issuer WisdomTree; current official product page lists stock exchange `Cboe`; Cboe/SEC listing evidence identifies principal listing exchange `Cboe BZX`; inception `2016-01-07`; asset class `Equity`; management mode `passive-index`; tracked index `WisdomTree Dynamic International SmallCap Equity Index` (`WTISDIHD`).
- Official current source: https://www.wisdomtree.com/us/products/equity/ddls — NAV `USD 46.476`, closing market price `USD 46.414`, premium/discount `-0.132%`, net assets `USD 434.55m`, and aggregate hedge ratio `80.76%`, all as of `2026-08-27`; current portfolio P/E `14.35`, P/B `1.45`, and underlying dividend yield `3.76%` as of `2026-08-27`; distribution yield `6.58%`, SEC 30-day yield `3.20%`, and net expense ratio `0.48%` as of `2026-08-27`.
- Official standardized performance from the same page: month-end `2026-07-31` NAV YTD `6.54%`, 1-year `16.16%`, 3-year annualized `16.40%`, 5-year `9.85%`, 10-year `9.61%`, and since-inception cumulative `169.91%`; underlying-index 10-year average annual return `10.04%`. The issuer defines total returns from daily 4:00pm NAV and keeps market-price returns separate.
- Official strategy/index sources: https://www.wisdomtree.com/investments/-/media/us-media-files/documents/resource-library/fund-fact-sheets/international-equity/wisdomtree-ddls-factsheet-2194.pdf and https://www.wisdomtree.com/us/indexes/WTISDIHD — developed ex-U.S./Canada small-cap dividend-paying equity exposure with a rules-based monthly currency hedge using momentum, value, and interest-rate signals. The use of currency derivatives is a hedge overlay; the fund remains an equity index-tracking product and is not treated as derivative-heavy, leveraged, inverse, or option-income.
- Exchange source: https://www.cboe.com/us/equities/listings/listed_products/symbols/DDLS/ and SEC listing evidence in the prior source batch confirm Cboe BZX context; the WisdomTree factsheet shortens this to `Cboe`, so both display conventions are preserved.
- Annual/calendar candidate claims retained from the prior reviewed official issuer capture: 2016 is `ไม่พบข้อมูลที่ยืนยันได้`; 2017-2024 official NAV rows are `25.02%, -16.59%, 24.74%, -1.78%, 16.11%, -9.79%, 15.16%, 9.84%`; 2025 `29.10%*` is a secondary dividend-reinvested NAV proxy because the current official page does not expose the calendar row. Cached S&P 500 Total Return rows for 2016-2025 are used only as the common reference, USD, dividends reinvested, as of 2025-12-31.
- Calculations: blended 2021-2025 DDLS compound `71.05%`, rounded-input CAGR `11.33%*`; cached S&P 500 2021-2025 compound `96.17%`, CAGR `14.43%`; DDLS trails the S&P common reference by `25.12 pp` cumulative and `3.09 pp` CAGR over the blended window. Disclosed 2017-2025 profile has `6 / 3` positive/negative years; best `2025 +29.10%*`; least positive `2024 +9.84%`; worst `2018 -16.59%`; least-bad down year `2020 -1.78%`. The official July rolling 10-year field is `9.61%`; raw ten-year endpoints/cumulative return are not disclosed.
- As-of reconciliation: the prior durable page used official quarter-end 10-year NAV average annual `10.18%` and YTD `4.48%` as of `2026-06-30`; the later official July month-end page reports `9.61%` and `6.54%` as of `2026-07-31`, while the latest NAV/price/hedge/exposure snapshot is `2026-08-27`. These are separate standardized and daily observations and are not arithmetically mixed.
- Evidence gaps: official current calendar rows for 2016 and 2025 are not exposed; the 2025 row remains secondary and marked `*`. Official daily NAV TR endpoints sufficient for reproducible maximum drawdown/recovery and volatility are `ไม่พบข้อมูลที่ยืนยันได้`; no unverified daily risk statistic is substituted.
- Pre-save evidence packet: identity/exchange, return basis, issuer/common benchmarks, passive equity classification, currency-hedge treatment, candidate annual/YTD/rolling claims, periods, units/currency, metric definitions, as-of dates, current NAV/price/valuation/hedge/exposure fields, calculations, prior-source reconciliation, gaps, and complete proposed contents for the DDLS performance page, International ETF snapshot, ETF Performance Index row, this source-batch section, and one log bullet were checked locally.
- Pre-save checklist: Cboe BZX identity resolved with source-display clarification; passive/index-tracking equity eligibility verified; NAV TR, market price, underlying-index, distribution and after-tax bases separated; July standardized returns kept separate from August daily quote and hedge fields; secondary 2025 proxy explicitly marked and excluded from official-only interpretation; cached S&P convention applied only to 2016-2025; gaps preserved; International breadcrumb and links resolve; local scheduled review verdict `PASS`.
- `verification_mode: scheduled-local`
- `reviewer_dispatch: not-attempted-by-design`

## DGRO — iShares Core Dividend Growth ETF

- `workflow: check-etf-performance`; `execution_profile: scheduled-inline`; `entity_key: NYSE Arca:DGRO`; issuer BlackRock/iShares; official listing exchange `NYSE Arca`; inception `2014-06-10`; asset class `Equity`; management mode `passive-index`; tracked index `Morningstar US Dividend Growth Index`.
- Official current source: https://www.ishares.com/us/products/264623/DGRO — current NAV `USD 79.27`, closing price `USD 79.28`, net assets `USD 43,595,761,451`, premium/discount `0.02%`, and `390` holdings as of `2026-08-27`; NAV Total Return YTD `15.25%` as of `2026-08-27`; expense ratio `0.08%`; quarterly distributions. The official objective is to track an index of U.S. stocks with a history of growing dividends.
- Official historical/performance source: https://www.ishares.com/ch/professionals/en/products/264623/ishares-core-dividend-growth-etf?switchLocale=Y — official calendar NAV Total Return rows displayed for 2016-2025 as `15.3%, 22.8%, -2.2%, 30.0%, 9.5%, 26.6%, -7.9%, 10.4%, 16.6%, 15.7%`; 2021-2025 U.S. page rows are more precise at `26.56%, -7.85%, 10.43%, 16.61%, 15.74%`. The same official capture reports the rolling 10-year NAV cumulative return `251.19%` / average annual `13.38%` for `2016-06-30` to `2026-06-30`; normalized endpoint `100.00 → 351.19` and elapsed years `10.00`.
- Official benchmark rows are Morningstar US Dividend Growth Index, not the S&P 500: 2021-2025 `26.69%, -7.75%, 10.45%, 16.66%, 15.87%`; 10-year average annual `13.46%` as of 2026-06-30. S&P 500 Total Return is retained only as the common reference benchmark.
- Official factsheet: https://www.ishares.com/us/literature/fact-sheet/dgro-ishares-core-dividend-growth-etf-fund-fact-sheet-en-us.pdf — return convention uses NAV with gross income/capital gains reinvested and fund expenses deducted; the product page provides the current fund and standardized performance fields.
- Common benchmark: cached `S&P 500 Total Return` convention for complete calendar years `2016-2025`, USD, dividends reinvested, as of `2025-12-31`; source references are https://www.spglobal.com/spdji/en/indices/equity/sp-500/ and the cached 2016-2019, 2018-2022, and 2022-2025 S&P market-attributes references defined in `check-etf-performance`. No current-year S&P comparison is claimed.
- Calculations: official rounded 2016-2025 rows compound to `242.63%`, rounded-input CAGR `13.11%`; the 2021-2025 precise rows compound to `73.82%`, rounded-input CAGR `11.69%`; cached S&P 500 rows compound to `298.33%` / `14.82%` for 2016-2025 and `96.17%` / `14.43%` for 2021-2025. DGRO trails S&P by `1.71 pp` of CAGR over 2016-2025 and `2.74 pp` over 2021-2025; cumulative 2021-2025 gap is `22.35 pp`. Complete-year up/down count is `8 / 2`; best `2019 +30.00%`; least positive `2020 +9.50%`; worst `2022 -7.85%`; least-bad down year `2018 -2.20%`.
- Official current characteristics: 3-year standard deviation `10.65%` and equity beta `0.68` as of `2026-07-31`; 30-day SEC yield `1.97%` and trailing 12-month yield `1.89%` as of `2026-07-31`; P/B `4.04` and P/E `24.68` as of `2026-08-27`. Secondary source https://portfolioslab.com/symbol/DGRO reports a maximum drawdown of `-35.10%` on `2020-03-23` and `161` trading sessions to recovery; this is kept as secondary price-and-distribution evidence, not official NAV drawdown.
- As-of reconciliation: the previous durable DGRO page used current YTD `10.22%` as of `2026-06-30` and a blended 2016-2020 secondary proxy. The latest official iShares page reports current NAV TR YTD `15.25%`, NAV `USD 79.27`, and closing price `USD 79.28` as of `2026-08-27`; these date-to-date/current fields remain separate from the June standardized rolling/calendar table. The 2016-2020 annual values are now official rounded issuer rows, so the secondary proxy is removed from the performance owner.
- Evidence gaps: official daily NAV Total Return endpoints sufficient to reproduce fund-level maximum drawdown/recovery are `ไม่พบข้อมูลที่ยืนยันได้`; the saved `-35.10%` / `161 sessions` observation remains secondary. No unsupported current-day benchmark or after-tax comparison is inferred.
- Pre-save evidence packet: identity/exchange, return basis, issuer benchmark, common benchmark, candidate performance claims, 10-year and calendar periods, units/currency, metric definitions, as-of dates, current NAV/YTD/holdings/expense/risk fields, calculations, as-of reconciliation, unresolved gaps, canonical `NYSE Arca:DGRO` filename migration, USA region row, entity delta, source-batch section, index changes, and one log bullet were checked locally. Proposed durable contents were `wiki/analysis/performance/ETF_NYSE_ARCA_DGRO Performance.md`, a legacy redirect at `wiki/analysis/performance/ETF_AMEX_DGRO Performance.md`, `wiki/analysis/comparisons/USA ETF.md`, `wiki/entities/ETF_AMEX_DGRO.md`, `wiki/analysis/performance/ETF Performance Index.md`, this source batch, and `log.md`.
- Pre-save checklist: passive/index-tracking equity eligibility verified; canonical exchange key and fund identity verified; NAV TR, market price, issuer-index TR, S&P reference, distribution and after-tax bases separated; official 2016-2025 rows and rolling 10-year window retained with their source/display precision; current August fields kept separate from June standardized data; cached S&P convention used only for 2016-2025; proxy removal and secondary drawdown label recorded; official daily-series gap preserved; canonical USA breadcrumb, region/index links, legacy redirect, and planned file contents checked; local scheduled review verdict `PASS`.
- `verification_mode: scheduled-local`
- `reviewer_dispatch: not-attempted-by-design`

## THD — iShares MSCI Thailand ETF

- `workflow: check-etf-performance`; `execution_profile: scheduled-inline`; `entity_key: NYSE Arca:THD`; issuer BlackRock/iShares; NYSE Arca listing; inception `2008-03-26`; Equity ETF; passive/index-tracking; tracked index `MSCI Thailand IMI 25/50 Index (Net)`. The official prospectus states the fund seeks to track a broad-based Thai-equity index and normally invests at least 80% in index securities or economically equivalent DRs; permitted derivatives are incidental implementation/management tools and do not change eligibility.
- Official current source: https://www.ishares.com/us/products/239688/THD — NAV `USD 73.81`, closing price `USD 73.56`, net assets `USD 357,986,210`, 82 holdings, and premium/discount `-0.34%` as of `2026-08-20`; NAV Total Return YTD `26.46%` as of `2026-08-19`; expense ratio `0.59%`; 30-day SEC yield `2.65%` and trailing 12-month yield `3.49%` as of `2026-07-31`.
- Official standardized performance source: https://www.ishares.com/us/products/239688/ishares-msci-thailand-capped-etf — as of `2026-06-30`, rolling 10-year NAV Total Return cumulative `39.02%` / average annual `3.35%` for `2016-06-30` to `2026-06-30` (`10.00` elapsed years). The official display also gives the 2021-2025 NAV rows `1.66%, 1.55%, -12.18%, -1.85%, 0.87%` and issuer-index rows `1.89%, 1.80%, -12.20%, -1.69%, 1.00%`; NAV TR includes reinvested distributions and deducts fund expenses. Raw rolling endpoints and 2016-2020 annual rows are not disclosed in the reviewed capture.
- Official legal/classification source: https://www.ishares.com/us/literature/prospectus/p-ishares-inc-apac-8-31.pdf — THD section at the current prospectus identifies ticker `THD`, exchange `NYSE Arca`, broad-based Thai-equity index objective, representative sampling, and the incidental role of permitted derivatives.
- Common benchmark: cached `S&P 500 Total Return` convention for complete calendar years `2016-2025`, USD, dividends reinvested, as of `2025-12-31`; source references are the S&P official index page https://www.spglobal.com/spdji/en/indices/equity/sp-500/, the 2016-2019 historical comparison https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true, the 2018-2022 market attributes https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf, and the 2022-2025 market attributes https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/. No current-year S&P comparison is claimed.
- Calculations: issuer rolling normalized endpoint `100.00 → 139.02` from `39.02%` cumulative return; `(139.02 / 100.00)^(1 / 10.00) - 1 = 3.35%` (rounded). THD 2021-2025 compound `-10.24%`, rounded-input CAGR `-2.14%`; cached S&P 500 TR compound `96.17%`, CAGR `14.43%`; THD trails by approximately `16.56 pp` CAGR. Complete-year up/down count is `2 / 3`; best `2022 +1.55%`; least positive `2025 +0.87%`; worst `2023 -12.18%`; least-bad down year `2024 -1.85%`. Annual fund-minus-issuer-index tracking differences are `-0.23, -0.25, +0.02, -0.16, -0.13 pp` for 2021-2025.
- As-of reconciliation: the prior page used current YTD `25.53%` as of `2026-07-22`; the later official page reports `26.46%` as of `2026-08-19` and NAV/price as of `2026-08-20`. These are distinct date-to-date/current-field observations; the later observation is used without mixing it into the standardized June annual/rolling window.
- Evidence gaps: raw NAV TR start/end values, official 2016-2020 annual rows, and a daily NAV series sufficient to reproduce fund-level max drawdown/recovery remain `ไม่พบข้อมูลที่ยืนยันได้`. The official 3-year standard deviation is `21.96%` as of `2026-06-30`; the latest risk fields and yields have separate as-of dates recorded above.
- Pre-save evidence packet: proposed performance page `wiki/analysis/performance/ETF_NYSE_ARCA_THD Performance.md` refreshes the current dates/values, rolling 10-year cumulative/CAGR, annual rows, rankings, sources, and `Thailand` breadcrumb; proposed `wiki/analysis/comparisons/Thailand ETF.md` changes only its static YTD snapshot; proposed `wiki/analysis/performance/ETF Performance Index.md` changes only the THD coverage-row YTD; this source-batch section records all URLs, as-of dates, bases, calculations, gaps, and the exact log bullet; no new region page is required.
- Pre-save checklist: canonical exchange/ticker and fund identity verified; passive equity eligibility verified; NAV TR, issuer-index TR, market price, distributions, yield and price/NAV dates kept separate; rolling 10-year eligibility is `10.00` years and raw endpoint gap is explicit; cached S&P convention is used only for its stated 2016-2025 window; rankings exclude partial YTD; `geography/Thailand` tag and `[[ETF Region Index]] → [[Thailand ETF]] → [[ETF Performance Index]]` breadcrumb resolve; source links and planned paths checked; local scheduled review verdict `PASS`.
- `verification_mode: scheduled-local`
- `reviewer_dispatch: not-attempted-by-design`

## JPXN — iShares JPX-Nikkei 400 ETF

- `workflow: check-etf-performance`; `execution_profile: scheduled-inline`; `entity_key: NYSE Arca:JPXN`; issuer BlackRock/iShares; NYSE Arca listing; inception 2001-10-23; Equity ETF; passive/index-tracking; tracked index `JPX-Nikkei Index 400 (Net)`. This is an eligible passive equity ETF, not a leveraged, inverse, option-income, or derivative-heavy fund.
- Official product/performance source: https://www.ishares.com/us/products/239831/ishares-japan-largecap-etf — current NAV `USD 102.65`, closing price `USD 102.59`, net assets `USD 138,572,246`, shares outstanding `1,350,000`, premium/discount `-0.05%`, non-fair-value NAV `USD 102.70`, and 30-day median bid/ask spread `0.17%`, all as of 2026-08-27; current NAV Total Return YTD `19.53%` as of 2026-08-27; expense ratio `0.48%` and 389 holdings.
- Official standardized performance source: same iShares page and factsheet https://www.ishares.com/us/literature/fact-sheet/jpxn-ishares-japan-largecap-etf-fund-fact-sheet-en-us.pdf — standardized table as of 2026-06-30; NAV 10-year cumulative `142.85%` / average annual `9.28%`, 1-year `27.72%`, 3-year annualized `17.81%`, 5-year `9.30%`, and since inception `5.52%`; issuer benchmark 10-year cumulative `149.04%` / average annual `9.55%`, 1-year `26.99%`, 3-year `18.17%`, 5-year `9.46%`, and since inception `5.73%`. Current June standardized YTD is NAV `15.90%` and benchmark `14.79%`.
- Official calendar NAV rows 2021-2025 are `0.40%, -16.04%, 19.47%, 6.37%, 26.05%`; issuer benchmark rows are `0.49%, -15.37%, 20.00%, 7.80%, 25.16%`. Rows for 2016-2020 are `ไม่พบข้อมูลที่ยืนยันได้` in the reviewed compact issuer capture and were not reconstructed. Cached `S&P 500 Total Return` rows for 2021-2025 are `28.71%, -18.11%, 26.29%, 25.02%, 17.88%`, USD, dividends reinvested, as of 2025-12-31; the cached reference source is https://www.spglobal.com/spdji/en/indices/equity/sp-500/ and S&P 500 is not JPXN's strategy benchmark.
- Official current characteristics: sectors as of 2026-08-27 are Industrials `26.29%`, Information Technology `16.98%`, Financials `15.38%`, and Consumer Discretionary `13.48%`; P/B `1.97x` and P/E `18.66x` as of 2026-08-27; 3-year standard deviation `13.56%`, equity beta `0.67`, SEC yield `1.23%`, and trailing yield `2.75%` as of 2026-07-31.
- Distribution check: latest displayed payments are `US$0.642828` payable 2026-06-18 and `US$2.105441` payable 2025-12-19, totaling `US$2.748269` per share across the two latest payments; these are distributions, not NAV TR.
- Calculations: 2021-2025 JPXN NAV compound `35.03%`, rounded-input CAGR `6.19%`; issuer benchmark compound `37.69%`, rounded-input CAGR `6.61%`; cached S&P 500 TR compound `96.17%`, CAGR `14.43%`. Up/down NAV years are `4 / 1`; best is 2025 `+26.05%`; least positive is 2021 `+0.40%`; worst/least bad down year is 2022 `-16.04%`. Official rolling 10-year NAV TR is `142.85%` / `9.28%` for 2016-06-30 to 2026-06-30.
- Return basis: official NAV Total Return in USD includes reinvested dividends/capital gains and fund expenses; market-price, issuer-benchmark, after-tax, fair-value and distribution fields remain separate. No arithmetic excess return is labeled alpha.
- As-of reconciliation: the prior durable page reported NAV `USD 98.72` as of 2026-07-22 and NAV TR YTD `15.60%` as of 2026-07-21. Later official iShares observations are NAV `USD 102.65`, closing price `USD 102.59`, and NAV TR YTD `19.53%` as of 2026-08-27; these current date-to-date fields remain separate from the June month-end standardized table.
- Evidence gaps: official daily NAV TR series sufficient for a reproducible maximum-drawdown/recovery calculation remains `ไม่พบข้อมูลที่ยืนยันได้`; 2016-2020 calendar NAV rows and raw per-share NAV/TR endpoints are not disclosed in the reviewed capture. No ETF entity hub exists in `wiki/entities/` for JPXN, so the existing performance page remains the context owner.
- Pre-save evidence packet: identity/exchange, passive-equity classification, return basis, issuer/common benchmarks, candidate performance claims, periods, units/currency, metric definitions, as-of dates, source URLs, exposure and distribution data, calculations, current-field reconciliation, unresolved gaps, and complete proposed contents for the JPXN performance page, Japan ETF snapshot, ETF Performance Index refresh, source-batch section, and log bullet were checked locally.
- Pre-save checklist: passive/index-tracking equity eligibility verified; NAV TR versus market price/benchmark/after-tax/fair-value bases separated; standardized June and current August fields kept distinct; latest/as-of dates recorded per metric; cached S&P convention applied only to 2021-2025; no 2016-2020 values inferred; fee, exposure, distribution, gap, links, Japan breadcrumb and planned files checked; result `PASS`.
- verification_mode: scheduled-local
- reviewer_dispatch: not-attempted-by-design

## INCO — Columbia India Consumer ETF

- `workflow: check-etf-performance`; `execution_profile: scheduled-inline`; `entity_key: NYSE Arca:INCO`; issuer Columbia Threadneedle; NYSE Arca listing; inception 2011-08-10; eligible indexed/passive Equity ETF; tracked index `Indxx India Consumer Index`.
- Official product/performance source: https://www.columbiathreadneedleus.com/investment-products/exchange-traded-funds/columbia-india-consumer-etf/inco/details?cusip=19762B707 — detailed product table as of 2026-06-30 reports NAV Total Return YTD `-8.68%`, 1-year `-8.46%`, 3-year annualized `6.90%`, 5-year `6.82%`, 10-year `8.50%`, and since inception `9.33%`; current daily NAV `USD 60.84`, market price `USD 61.37`, premium `+0.87%`, and median bid/ask spread `0.18%` as of 2026-07-28; exchange, benchmark, inception, distribution schedule (annual), and indexed management style are also identified.
- Official current ETF-finder source: https://www.columbiathreadneedleus.com/investment-products/exchange-traded-funds — latest issuer row as of 2026-07-31 reports current NAV TR YTD `-4.67%`, 1-year `-1.96%`, 3-year `8.06%`, 5-year `7.83%`, 10-year `8.38%`, and since-inception `9.59%`; the 7/31 row is used for the latest current YTD/10-year fields, while the detailed June table remains a separate standardized snapshot.
- Official factsheet: https://www.columbiathreadneedleus.com/binaries/content/assets/cti/public/columbia_india_consumer_etf_fs.pdf — Q2/JUNE 30, 2026; fund objective is to correspond before fees and expenses to the Indxx India Consumer Index, a maximum 30-stock free-float-adjusted market-cap-weighted India consumer index; 30 holdings; gross expense ratio `0.76%`, net expense ratio `0.75%`; sector weights Consumer Discretionary `64.3%` and Consumer Staples `35.7%`; annual rows and index rows below.
- Official current portfolio observations from the product page: top holdings are as of 2026-07-28; portfolio characteristics as of 2026-06-30 report P/E `19.68x` and P/B `6.44x`. The reviewed detailed product/factsheet disclosure lists a net-fee waiver through 2026-07-31, while the later ETF-finder row shows `0.75% / 0.75%` expense fields and waiver expiration 2027-07-31; this official-source conflict is preserved rather than silently merged, and the detailed product/factsheet fee fields are used on the performance page.
- Official classification/risk wording in the product and factsheet sources states the fund is passively managed/index-tracking and concentrated in the India consumer sector; it is not a bond, commodity, currency, multi-asset, active, leveraged, inverse, option-income, or derivative-heavy ETF. Country, emerging-market, concentration, FX, small-/mid-cap, liquidity and tracking risks remain relevant.
- Official calendar-year NAV rows from the product/factsheet source, in 2021-2025 order, are `19.70%, -7.40%, 34.12%, 13.78%, 0.35%`; issuer Indxx benchmark rows are `22.76%, -6.28%, 40.74%, 17.70%, 2.45%`. The issuer table does not disclose 2016-2020 annual rows in the reviewed current capture. Cached `S&P 500 Total Return` common-reference rows for 2021-2025 are `28.71%, -18.11%, 26.29%, 25.02%, 17.88%`, USD, dividends reinvested, as of 2025-12-31; S&P 500 is not INCO's strategy benchmark.
- Calculations: INCO 2021-2025 NAV compound `69.74%`, rounded-input CAGR `11.16%`; Indxx benchmark compound `95.25%`, rounded-input CAGR `14.32%`; cached S&P 500 TR compound `96.17%`, CAGR `14.43%`; annual NAV population standard deviation `14.59%`. Up/down years `4 / 1`; best 2023 `+34.12%`; least positive 2025 `+0.35%`; worst/least bad down year 2022 `-7.40%`. Latest issuer 10-year average annual NAV TR `8.38%` implies a rounded-input normalized end value `223.61` from start `100.00` over ten years, but no raw endpoint or direct cumulative 10-year field is claimed.
- Return basis: official NAV Total Return includes reinvested dividends/capital gains and fund expenses; market-price, benchmark and common S&P reference returns remain separate. Returns over one year are annualized in the issuer table; no arithmetic excess return is labeled alpha.
- As-of reconciliation: the prior durable page recorded issuer 10-year average annual NAV TR `8.72%` and current YTD `-9.92%` as of 2026-05-31, with NAV `USD 59.45` as of 2026-06-23. The later detailed product table gives June YTD `-8.68%` and 10-year `8.50%` as of 2026-06-30; the later issuer ETF-finder row gives YTD `-4.67%` and 10-year `8.38%` as of 2026-07-31, while the latest displayed daily NAV/market price is `USD 60.84 / USD 61.37` as of 2026-07-28. These date-to-date and standardized fields are retained with their distinct as-of dates.
- Evidence gaps: raw daily NAV TR endpoints sufficient for reproducible maximum-drawdown/recovery are `ไม่พบข้อมูลที่ยืนยันได้`; no price-only proxy is substituted. Annual NAV rows for 2016-2020 are not disclosed in the reviewed current official capture. No ETF entity hub exists in `wiki/entities/` for INCO, so the existing performance page remains the context owner.
- Pre-save evidence packet: identity/exchange, return basis, issuer benchmark, common benchmark, candidate performance claims, periods, units/currency, metric definitions, as-of dates, calculations, source URLs, fee conflict, current-field reconciliation, unresolved gaps, and complete proposed contents for the INCO performance page, India ETF snapshot, ETF Performance Index row, source-batch section, and log bullet were checked locally.
- Pre-save checklist: indexed/passive equity eligibility verified; NAV TR versus market price/issuer benchmark/common reference separated; annual and rolling/date-to-date periods kept distinct; latest/as-of dates recorded per metric; fee conflict preserved; cached S&P convention applied only to 2021-2025; no 2016-2020 values inferred; gaps, links, India breadcrumb and planned files checked; result `PASS`.
- verification_mode: scheduled-local
- reviewer_dispatch: not-attempted-by-design

## IEUR — iShares Core MSCI Europe ETF

- `workflow: check-etf-performance`; `execution_profile: scheduled-inline`; `entity_key: NYSE Arca:IEUR`.
- Official product/performance source: https://www.ishares.com/us/products/264617/IEUR — Equity ETF listed on NYSE Arca, launched 2014-06-10, tracking `MSCI Europe IMI Index (Net)`; current NAV `USD 77.98`, closing price `USD 78.11`, net assets `USD 9,419,762,708`, shares outstanding `120,800,000`, and NAV Total Return YTD `12.23%`, all as of 2026-08-27. Expense ratio is `0.10%`, distribution frequency is semi-annual, and holdings are `1,009`.
- Official standardized performance source: same iShares page and factsheet https://www.ishares.com/us/literature/fact-sheet/ieur-ishares-core-msci-europe-etf-fund-fact-sheet-en-us.pdf — factsheet as of 2026-06-30; official 2021-2025 NAV rows `16.21%, -16.18%, 19.83%, 1.70%, 35.11%`, benchmark rows `16.13%, -16.71%, 19.52%, 1.49%, 35.08%`; rolling NAV TR fields are 1-year `17.19%`, 3-year `16.18%`, 5-year `9.07%`, 10-year `10.02%`, and since inception `6.54%`.
- Official classification source: same iShares product page and summary prospectus https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-core-msci-europe-etf-7-31.pdf — the fund tracks large-, mid- and small-cap developed-European equities with an indexing approach; eligible passive broad-Europe equity ETF. Current P/B is `2.48x` and P/E `19.14x` as of 2026-08-27; 3-year standard deviation `13.67%` and beta `0.66` are as of 2026-07-31. Country exposure as of 2026-08-27 is led by United Kingdom `22.89%`, France `14.14%`, Switzerland `13.88%`, Germany `13.42%`, and Netherlands `8.32%`.
- Return basis and common benchmark: official NAV Total Return includes reinvested dividends/capital gains and reflects fund expenses; market-price and issuer-index returns remain separate. Cached `S&P 500 Total Return` convention is used for complete 2021-2025 rows, USD, dividends reinvested, as of 2025-12-31; current 2026 S&P comparison is not claimed.
- Distribution observations from the official product page: `US$1.542483` payable 2026-06-18 and `US$0.849102` payable 2025-12-19; latest two verified cash payments total `US$2.391585` per share. These are distributions, not NAV TR.
- Calculations: 2021-2025 NAV compound `60.39%`, CAGR `9.91%`; issuer benchmark compound `58.49%`, CAGR `9.65%`; S&P 500 TR compound `96.17%`, CAGR `14.43%`. Up/down years are `4 / 1`; best is 2025 `+35.11%`, least positive is 2024 `+1.70%`, worst and least bad down year are 2022 `-16.18%`. The issuer rolling 10-year field remains `10.02%` as of 2026-06-30; no separate ten-year calendar CAGR is inferred.
- As-of reconciliation: the prior page snapshot reported NAV `USD 77.83`, closing price `USD 78.05`, and YTD `12.03%` as of 2026-08-17. The later official iShares observation is NAV `USD 77.98`, closing price `USD 78.11`, and YTD `12.23%` as of 2026-08-27 and is used for refreshed current fields. The date-to-date YTD is kept separate from the June month-end standardized table.
- Evidence gaps: raw daily NAV TR endpoints sufficient for a reproducible NAV max-drawdown/recovery series are `ไม่พบข้อมูลที่ยืนยันได้`; no price-only proxy is substituted. No ETF entity hub exists in `wiki/entities/` for IEUR, so the existing performance owner remains the context page.
- Pre-save local review: identity/exchange, passive equity eligibility, NAV/price/benchmark basis, as-of dates, annual markers, cached S&P window, calculations, source links, `Europe ETF` navigation, breadcrumb, and planned performance/source-batch/index/log changes were checked; no high-severity issue remained. Result: `PASS`.
- verification_mode: scheduled-local
- reviewer_dispatch: not-attempted-by-design

## HEZU — iShares Currency Hedged MSCI Eurozone ETF

- `workflow: check-etf-performance`; `execution_profile: scheduled-inline`; `entity_key: NYSE Arca:HEZU`.
- Official product/performance source: https://www.ishares.com/us/products/268708/HEZU — Equity ETF listed on NYSE Arca, launched 2014-07-09, tracking `MSCI EMU 100% Hedged to USD Index (Net)`; current NAV `USD 49.63`, closing price `USD 49.65`, net assets `USD 595,516,360`, shares outstanding `12,000,000`, and current NAV Total Return YTD `15.23%`, all as of 2026-08-27. The page reports expense ratio `1.12%`, net expense ratio `0.53%`, one holding, and semi-annual distributions.
- Official standardized performance source: same iShares page and factsheet https://www.ishares.com/us/literature/fact-sheet/hezu-ishares-currency-hedged-msci-eurozone-etf-fund-fact-sheet-en-us.pdf — factsheet as of 2026-06-30; official 2021-2025 NAV rows `23.25%, -9.34%, 22.89%, 10.82%, 25.86%`, benchmark rows `23.24%, -9.88%, 22.08%, 11.38%, 26.11%`; rolling NAV TR fields are 1-year `26.48%`, 3-year `18.64%`, 5-year `13.47%`, 10-year `12.88%`, and since inception `10.58%`.
- Official classification source: https://www.sec.gov/Archives/edgar/data/1100663/000119312525336755/d918823d497k.htm — the Fund uses an indexing approach, invests substantially in EZU, and uses monthly currency forwards to hedge euro exposure; it is an eligible passive equity ETF, not leverage or option-income exposure. The prospectus reports 13% portfolio turnover for the most recent fiscal year and BFA adviser/Orlando Montalvo continuity since 2014.
- Return basis and common benchmark: official NAV Total Return includes reinvested dividends/capital gains and reflects fund expenses; market-price and issuer-index returns remain separate. Cached `S&P 500 Total Return` convention is used for complete 2021-2025 rows, USD, dividends reinvested, as of 2025-12-31; current 2026 S&P comparison is not claimed.
- Current-risk and exposure observations from the official product page: 3-year standard deviation `11.39%` and beta `0.59` as of 2026-07-31; trailing yield `2.57%` as of 2026-07-31; P/E `19.11x` and P/B `2.38x` as of 2026-08-27. Sector exposure as of 2026-08-27 is led by Financials `27.38%`, Industrials `20.39%`, and Information Technology `15.44%`; country exposure is led by France `28.01%`, Germany `25.77%`, and the Netherlands `16.51%`.
- Calculations: 2021-2025 NAV compound `91.52%`, CAGR `13.88%`; issuer benchmark compound `90.45%`, CAGR `13.75%`; S&P 500 TR compound `96.17%`, CAGR `14.43%`. The displayed annual rows are rounded official observations. The issuer rolling 10-year field is retained as `12.88%` as of 2026-06-30; no 10-year calendar CAGR is reconstructed because 2016-2020 rows are not disclosed in the reviewed official capture. Up/down years are `4 / 1`; best is 2025 `+25.86%`, least positive is 2024 `+10.82%`, and worst is 2022 `-9.34%`.
- As-of reconciliation: the prior page snapshot reported NAV `USD 50.62` and YTD `17.53%` as of 2026-08-14; the later official iShares observation is NAV `USD 49.63` and YTD `15.23%` as of 2026-08-27 and is used for the refreshed current fields. These date-to-date observations are not arithmetically reconciled with the June month-end standardized table.
- Evidence gaps: raw daily NAV TR endpoints sufficient for a reproducible NAV max-drawdown/recovery series are `ไม่พบข้อมูลที่ยืนยันได้`; no price-only proxy is substituted. No ETF entity hub exists in `wiki/entities/` for HEZU, so the existing performance owner remains the context page.
- Pre-save local review: identity/exchange, passive equity eligibility, NAV/price/benchmark basis, all as-of dates, annual markers, cached S&P window, calculations, source links, `Europe ETF` navigation, breadcrumb, and planned performance/source-batch/index/log changes were checked; no high-severity issue remained. Result: `PASS`.
- verification_mode: scheduled-local
- reviewer_dispatch: not-attempted-by-design

## HEWJ — iShares Currency Hedged MSCI Japan ETF

- workflow: check-etf-performance; execution_profile: scheduled-inline; entity_key: NYSE Arca:HEWJ; issuer BlackRock/iShares; NYSE Arca listing; inception 2014-01-31; Equity ETF; tracked index MSCI Japan 100% Hedged to USD Index (Net).
- Official product/performance source: https://www.ishares.com/us/products/259624/ishares-currency-hedged-msci-japan-etf — current NAV USD 64.55, closing price USD 64.63, net assets USD 745,520,927, and 11.55M shares as of 2026-08-26; premium/discount 0.13% as of 2026-08-26; 30-day median bid/ask spread 0.16% as of 2026-08-25; current NAV Total Return YTD 23.35% as of 2026-08-25.
- Official current characteristics: gross expense ratio 1.02%, net expense ratio 0.49%; 30-day SEC yield 3.80%, 12-month trailing yield 3.72%, and unsubsidized SEC yield 3.27% as of 2026-07-31; 3-year standard deviation 11.98% and equity beta 0.43 as of 2026-07-31; P/B 2.04 and P/E 19.16 as of 2026-08-25; holdings field 1 as of 2026-08-25; sector weights as of 2026-08-25: Industrials 24.63%, Financials 18.66%, Information Technology 17.84%, Consumer Discretionary 15.30%, Communication 6.60%, Health Care 5.59%.
- Standardized performance as of 2026-06-30: NAV Total Return YTD 22.41%, 1-year 51.46%, 3-year annualized 28.13%, 5-year annualized 22.06%, 10-year annualized 17.27%, since inception annualized 14.11%; benchmark YTD 22.08%, 1-year 50.24%, 3-year annualized 28.67%, 5-year annualized 22.48%, 10-year annualized 17.88%, since inception annualized 14.37%; 10-year cumulative NAV TR 391.99% and benchmark cumulative 418.44%.
- Official calendar-year NAV Total Return rows 2021-2025: 12.79%, -3.91%, 36.20%, 24.87%, 30.08%; issuer benchmark rows 13.60%, -2.00%, 35.73%, 26.66%, 28.56%. From the official NAV rows, 2021-2025 cumulative/CAGR are 139.77% / 19.11%; up/down count 4 / 1; best 2023 +36.20%; worst 2022 -3.91%. The cached S&P 500 Total Return common reference for 2021-2025 is cumulative 96.17% / CAGR 14.43%, with rows 28.71%, -18.11%, 26.29%, 25.02%, 17.88%.
- Return basis and units: official NAV Total Return in USD, distributions reinvested and fund expenses reflected; iShares notes fee waivers/reimbursements may affect some periods. Market-price, benchmark and after-tax returns are kept separate from NAV TR. Currency hedge is part of the index strategy and does not change the equity ETF classification.
- As-of reconciliation: the earlier saved current date-to-date observation was NAV YTD 18.81% as of 2026-07-17; the later iShares observation is 23.35% as of 2026-08-25 and is used for the refreshed current-YTD field. The standardized month-end YTD 22.41% as of 2026-06-30 remains separate.
- Evidence gaps: daily NAV series sufficient for max drawdown/recovery is not verified; latest current date-to-date YTD and the standardized month-end performance table have different as-of dates and are not arithmetically reconciled. No unsupported calendar rows or current July standardized row is inferred from the date-to-date figure.
- Pre-save evidence packet: identity/exchange, return basis, benchmark, candidate performance claims, periods, units/currency, metric definitions, as-of dates, source URL, as-of reconciliation, unresolved gaps, and complete proposed contents were checked locally. Proposed durable contents: refresh HEWJ performance page with latest current NAV/YTD and current risk/sector facts while retaining official June rolling/calendar returns; update the Japan ETF snapshot/note; update ETF Performance Index coverage row/date; append this source-batch section; append one dated workflow bullet to log.md.
- Pre-save checklist: source identity verified; passive/index-tracking equity classification verified; NAV TR versus market price/benchmark/after-tax bases separated; gross/net fees recorded; latest/as-of dates recorded per metric; current YTD not mixed with month-end table; cached S&P convention applied only to 2021-2025; gaps and fee-waiver caveat preserved; links and breadcrumb preserved; result PASS.
- verification_mode: scheduled-local
- reviewer_dispatch: not-attempted-by-design

## IEV — iShares Europe ETF

- `workflow: check-etf-performance`; `execution_profile: scheduled-inline`; `entity_key: NYSE Arca:IEV`; issuer BlackRock/iShares; NYSE Arca listing; inception 2000-07-25; Equity ETF; tracked index `S&P Europe 350 Index (Net)`.
- Official product/performance source: https://www.ishares.com/us/products/239736/IEV — current NAV `USD 75.45`, closing price `USD 75.58`, net assets `USD 1,693,897,422`, and `22.45M` shares as of 2026-08-27; current NAV Total Return YTD `12.71%` as of 2026-08-26; 360 holdings; expense ratio `0.60%`; semi-annual distributions.
- Official current characteristics: P/B `2.56`, P/E `19.35` as of 2026-08-27; 3-year standard deviation `13.38%` and equity beta `0.64` as of 2026-07-31; country exposure as of 2026-08-27 led by United Kingdom `23.15%`, France `14.96%`, Switzerland `14.32%`, Germany `13.72%`, and the Netherlands `8.36%`.
- Official standardized performance source: https://www.ishares.com/us/literature/fact-sheet/iev-ishares-europe-etf-fund-fact-sheet-en-us.pdf — factsheet as of 2026-06-30; official 2021-2025 NAV rows `16.34%, -14.16%, 19.82%, 1.71%, 35.02%`; issuer benchmark rows `16.62%, -14.75%, 20.20%, 2.10%, 35.78%`; issuer rolling 10-year NAV TR `9.87%`.
- Official classification/risk source: https://www.ishares.com/us/literature/prospectus/p-ishares-europe-etf-3-31.pdf — index-based European equity strategy and related investment risks; eligible passive, index-tracking equity ETF, not leverage or option-income exposure.
- Return basis and common benchmark: official NAV Total Return in USD with distributions reinvested and expenses reflected; market-price and issuer-index returns remain separate. Cached `S&P 500 Total Return` convention is used only for complete 2021-2025 rows, USD, dividends reinvested, as of 2025-12-31; current 2026 S&P comparison is not claimed.
- Distribution check: latest displayed income distributions are `US$1.280576` payable 2026-06-18 and `US$0.751330` payable 2025-12-19, totaling `US$2.031906` per share across the two latest payments; 30-day SEC yield `1.94%` and 12-month trailing yield `2.72%` as of 2026-07-31 are separate metrics from NAV TR.
- Calculations: 2021-2025 NAV compound `64.33%`, rounded-input CAGR `10.44%`; issuer benchmark compound `65.67%`, rounded-input CAGR `10.62%`; cached S&P 500 TR compound `96.17%`, CAGR `14.43%`. Up/down years are `4 / 1`; best NAV year is 2025 `+35.02%`; least positive is 2024 `+1.71%`; worst/least bad down year is 2022 `-14.16%`. The fund-minus-index difference is approximately `-0.18 pp`, a passive tracking observation, not alpha.
- As-of reconciliation: the prior saved page reported NAV `USD 75.37`, closing price `USD 75.42`, and YTD `11.94%` as of 2026-08-17. Later official iShares observations are NAV `USD 75.45`, closing price `USD 75.58` as of 2026-08-27 and NAV TR YTD `12.71%` as of 2026-08-26; these current date-to-date values remain separate from the June month-end standardized table.
- Evidence gaps: raw daily NAV TR series sufficient for a reproducible maximum-drawdown/recovery calculation are `ไม่พบข้อมูลที่ยืนยันได้`; no price-only proxy is substituted. No ETF entity hub exists in `wiki/entities/` for IEV, so the existing performance owner remains the context page.
- Pre-save evidence packet: identity/exchange, return basis, benchmark, candidate claims, periods, units/currency, metric definitions, as-of dates, source URLs, as-of reconciliation, unresolved gaps, and complete proposed contents for the IEV performance page, Europe ETF snapshot, ETF Performance Index row, source-batch section, and log bullet were checked locally.
- Pre-save checklist: passive/index-tracking equity eligibility verified; NAV TR versus market price/benchmark/after-tax bases separated; fee and distribution metrics kept distinct; latest/as-of dates recorded per metric; current YTD not mixed with June month-end table; cached S&P convention applied only to 2021-2025; gaps and benchmark caveat preserved; links and Europe breadcrumb preserved; result `PASS`.
- verification_mode: scheduled-local
- reviewer_dispatch: not-attempted-by-design

## IPAC — iShares Core MSCI Pacific ETF

- `workflow: check-etf-performance`; `execution_profile: scheduled-inline`; `entity_key: NYSE Arca:IPAC`; issuer BlackRock/iShares; NYSE Arca listing; inception 2014-06-10; Equity ETF; passive/index-tracking; tracked index `MSCI Pacific IMI Index (Net)`.
- Official product/performance source: https://www.ishares.com/us/products/264619/ishares-core-msci-pacific-etf — current NAV `USD 85.64`, closing price `USD 85.50`, net assets `USD 2,774,704,584`, shares outstanding `32,400,000`, premium/discount `-0.16%`, non-fair-value NAV `USD 85.62`, and 30-day median bid/ask spread `0.11%`, all as of 2026-08-27; current NAV Total Return YTD `18.43%` as of 2026-08-27; expense ratio `0.09%`; semi-annual distributions.
- Official standardized performance from the same product page and factsheet https://www.ishares.com/us/literature/fact-sheet/ipac-ishares-core-msci-pacific-etf-fund-fact-sheet-en-us.pdf — factsheet/table as of 2026-06-30; NAV 10-year cumulative `141.81%` / average annual `9.23%`, 1-year `24.52%`, 3-year annualized `16.66%`, 5-year `8.05%`, and since inception `7.36%`; benchmark 10-year cumulative `136.54%` / average annual `8.99%`, 1-year `23.78%`, 3-year `16.56%`, 5-year `7.84%`, and since inception `7.21%`.
- Official calendar NAV rows 2021-2025 are `3.03%, -13.31%, 14.33%, 5.56%, 25.62%`; issuer benchmark rows are `2.53%, -13.06%, 14.36%, 6.26%, 24.42%`. Rows for 2016-2020 are `ไม่พบข้อมูลที่ยืนยันได้` in the reviewed official capture and were not reconstructed. Cached `S&P 500 Total Return` common-reference rows for 2021-2025 are `28.71%, -18.11%, 26.29%, 25.02%, 17.88%`, USD, dividends reinvested, as of 2025-12-31; S&P 500 is not IPAC's strategy benchmark.
- Official current characteristics as of 2026-08-27: 1,369 holdings; P/B `1.93x`; P/E `19.27x`; country exposure Japan `69.30%`, Australia `19.64%`, Singapore `5.18%`, Hong Kong `4.87%`, Other `0.57%`, Cash and/or Derivatives `0.45%`; sector exposure Financials `23.56%`, Industrials `20.05%`, Information Technology `12.49%`, Consumer Discretionary `12.37%`, Materials `9.09%`, Health Care `5.03%`, Communication `4.83%`, Real Estate `4.65%`, Consumer Staples `4.17%`, Utilities `1.73%`, Energy `1.58%`, Cash and/or Derivatives `0.45%`. The issuer reports 3-year standard deviation `12.98%` and beta `0.69` as of 2026-07-31, and 30-day SEC yield `2.15%` / trailing yield `3.84%` as of 2026-07-31.
- Distribution check: latest displayed payments are `US$0.880642` payable 2026-06-18 and `US$2.316870` payable 2025-12-19, totaling `US$3.197512` per share across the two latest payments; these are distributions, not NAV TR.
- Calculations: 2021-2025 IPAC NAV compound `35.41%`, rounded-input CAGR `6.25%`; issuer benchmark compound `34.77%`, rounded-input CAGR `6.15%`; cached S&P 500 TR compound `96.17%`, CAGR `14.43%`. Up/down NAV years `4 / 1`; best 2025 `+25.62%`; worst 2022 `-13.31%`. Official rolling 10-year NAV TR remains `141.81%` / `9.23%` for 2016-06-30 to 2026-06-30.
- Return basis: official Total Return assumes reinvestment of dividends/capital gains and deducts fund expenses; market-price, benchmark, after-tax and fair-value fields remain separate. The issuer notes ETF total return may diverge from benchmark because of systematic fair value.
- As-of reconciliation: the prior durable page recorded current NAV TR YTD `13.75%` as of 2026-07-22 and 1,370 holdings with Japan `69.37%`, Australia `19.46%`, Singapore `5.17%`, Hong Kong `4.97%`, and 3-year standard deviation `13.01%` as of 2026-07-22. Later official iShares observations are NAV TR YTD `18.43%`, NAV `USD 85.64`, and closing price `USD 85.50` as of 2026-08-27, with current holdings/exposure refreshed to the same date; the June standardized rolling/calendar table remains separate.
- Evidence gaps: official daily NAV TR series sufficient for a reproducible maximum-drawdown/recovery calculation remains `ไม่พบข้อมูลที่ยืนยันได้`; 2016-2020 calendar NAV rows are not disclosed in the reviewed capture. No ETF entity hub exists in `wiki/entities/` for IPAC, so the existing performance page remains the context owner.
- Pre-save evidence packet: identity/exchange, passive-equity classification, return basis, issuer/common benchmarks, candidate performance claims, periods, units/currency, metric definitions, as-of dates, source URLs, exposure and distribution data, calculations, current-field reconciliation, unresolved gaps, and complete proposed contents for the IPAC performance page, Asia-Pacific ETF snapshot, ETF Performance Index refresh, source-batch section, and log bullet were checked locally.
- Pre-save checklist: passive/index-tracking equity eligibility verified; NAV TR versus market price/benchmark/after-tax/fair-value bases separated; standardized June and current August fields kept distinct; latest/as-of dates recorded per metric; cached S&P convention applied only to 2021-2025; no 2016-2020 values inferred; fee, exposure, distribution, gap, links, Asia-Pacific breadcrumb and planned files checked; result `PASS`.
- verification_mode: scheduled-local
- reviewer_dispatch: not-attempted-by-design

## KBA — KraneShares Bosera MSCI China A 50 Connect Index ETF

- `workflow: check-etf-performance`; `execution_profile: scheduled-inline`; `entity_key: NYSE Arca:KBA`; issuer KraneShares; canonical principal listing exchange `NYSE Arca` from the official summary prospectus and annual shareholder report, while the current product page displays `Primary Exchange NYSE`; inception 2014-03-04; Equity ETF; passive/index-tracking; tracked index `MSCI China A 50 Connect Index`.
- Official product/performance source: https://kraneshares.com/etf/kba/ — current fund facts as of 2026-08-27: NAV `USD 33.32`, closing price `USD 33.19`, net assets `USD 144,924,108`, shares outstanding `4,350,000`, premium/discount `-0.13%`, and 30-day median bid/ask spread `0.15%`; gross expense ratio `0.79%`, net expense ratio `0.56%`, annual distributions, and fee waiver shown as contractual through 2028-08-01. The page's latest standardized performance table is as of 2026-07-31.
- Official standardized performance source: same product page and factsheet https://kraneshares.com/resources/factsheet/kba_factsheet.pdf — July 2026 cumulative NAV rows are 1 month `-3.52%`, 3 months `-0.03%`, 6 months `7.00%`, YTD `7.45%`, and since inception `130.09%`; average annualized NAV rows are 1 year `33.34%`, 3 years `12.15%`, 5 years `1.28%`, 10 years `6.22%`, and since inception `6.94%`. Corresponding underlying-index rows are YTD `7.89%`, 10-year `6.50%`, and since inception `7.96%`. The separate June quarter-end table reports NAV YTD `11.37%`, 10-year `6.90%`, and underlying-index 10-year `7.16%`; these observations are retained with distinct as-of dates.
- Official calendar NAV rows from the summary prospectus are `2016 -19.37%`, `2017 28.64%`, `2018 -26.25%`, `2019 -26.49%`, `2020 -17.10%`, `2021 34.50%`, `2022 2.70%`, `2023 16.06%`, and `2024 42.39%`; 2025 is `not disclosed` in the reviewed official materials. Cached `S&P 500 Total Return` rows for 2016-2025 are used only as a common reference, USD, dividends reinvested, as of 2025-12-31; original reference source: https://www.spglobal.com/spdji/en/indices/equity/sp-500/.
- Official strategy and risk source: https://kraneshares.com/resources/compliance/2026_02_20_kba_summary.prospectus.pdf — the fund seeks to track a foreign equity index, normally invests at least 80% in index securities or similar instruments, and the MSCI China A 50 Connect Index selects 50 large- and mid-cap RMB-denominated A-shares accessible through Stock Connect. The current product page says the fee waiver lasts through 2028-08-01, while the linked August 2025 prospectus says 2026-08-01; the current product page is used for the latest fee snapshot and the conflict is preserved.
- Return basis: official Fund NAV total return includes reinvested dividends/distributions and fund expenses; closing-price, underlying-index, after-tax, and distribution metrics remain separate. The current product page discloses the custom blended index history: MSCI China A through 2014-10-23, MSCI China A International through 2017-12-26, MSCI China A Inclusion through 2019-05-29, MSCI China A through 2022-01-05, and MSCI China A 50 Connect thereafter.
- Distribution check: latest displayed payments are `US$0.483155` payable 2025-12-23 and `US$0.511692` payable 2024-12-18, totaling `US$0.994847` per share; these are distributions, not NAV TR.
- Calculations: complete disclosed 2016-2024 NAV rows compound to `6.41%`, rounded-input CAGR `0.69%` over nine years; 2021-2024 compound `128.27%`, CAGR `22.92%`; cached S&P 500 TR compound for 2016-2024 `237.91%`, CAGR `14.49%`, and for 2021-2024 `66.41%`, CAGR `13.58%`. Up/down years in 2016-2024 are `5 / 4`; best is 2024 `+42.39%`; worst is 2019 `-26.49%`. The latest rolling 10-year NAV CAGR is `6.22%` as of 2026-07-31; the normalized endpoint `182.84` and cumulative `82.84%` are calculated from that CAGR, not raw endpoints.
- As-of reconciliation: the prior durable page used June 2026 current fields, including NAV TR YTD `11.37%` as of 2026-06-30. The later official product page reports NAV `USD 33.32`, closing price `USD 33.19`, and NAV TR YTD `7.45%` in the July 2026 standardized table, with daily NAV/price as of 2026-08-27; these are not arithmetically reconciled across different as-of dates.
- Evidence gaps: 2025 calendar-year KBA NAV return is not disclosed in the reviewed official materials; daily NAV TR endpoints sufficient for reproducible fund-level maximum drawdown and recovery are `ไม่พบข้อมูลที่ยืนยันได้`. The product-page versus prospectus exchange and fee-waiver conflicts are retained; no unsupported 2025 or current date-to-date NAV TR is inferred.
- Pre-save evidence packet: identity/exchange, passive-equity classification, return basis, issuer/common benchmarks, candidate claims, periods, units/currency, metric definitions, as-of dates, source URLs, current-field reconciliation, methodology history, calculations, unresolved gaps, and complete proposed contents for the KBA performance page, China ETF snapshot, ETF Performance Index row/refresh, source-batch section, and log bullet were checked locally.
- Pre-save checklist: passive/index-tracking equity eligibility verified; NAV TR versus market price/underlying-index/after-tax/distribution bases separated; July standardized and June quarter-end fields kept distinct; latest/as-of dates recorded per metric; cached S&P convention applied only to the stated common windows; 2025 annual gap preserved; exchange/fee-waiver conflicts documented; links, China breadcrumb, and planned files checked; result `PASS`.
- verification_mode: scheduled-local
- reviewer_dispatch: not-attempted-by-design

## SPSM — State Street SPDR Portfolio S&P 600 Small Cap ETF

- `workflow: check-etf-performance`; `execution_profile: scheduled-inline`; `entity_key: NYSE Arca:SPSM`; issuer State Street SPDR; NYSE Arca listing; inception 2013-07-08; Equity ETF; passive/index-tracking; tracked index `S&P SmallCap 600 Index`; options unavailable on the current issuer page.
- Official product/performance source: https://www.ssga.com/us/en/intermediary/etfs/state-street-spdr-portfolio-sp-600-small-cap-etf-spsm — current NAV `USD 57.06`, bid/ask midpoint `USD 57.07`, closing price `USD 57.06`, premium/discount `+0.02%`, 30-day median bid/ask spread `0.02%`, and AUM `USD 17,080.79M`, all as of 2026-08-27; fund facts/listing information are as of 2026-08-28. Gross expense ratio is `0.03%`, distribution frequency quarterly, and holdings are `606` as of 2026-08-27.
- Official current characteristics as of 2026-08-27: P/B `2.04x`, forward P/E `15.12x`, estimated 3-5 year EPS growth `15.31%`, 30-day SEC yield `1.47%`, fund distribution yield `1.38%`; sector weights are Financials `19.02%`, Industrials `17.63%`, Consumer Discretionary `13.98%`, Information Technology `12.41%`, Health Care `10.97%`, Real Estate `6.54%`, and Energy `6.12%`.
- Official standardized performance from the same State Street page: as of 2026-07-31, NAV Total Return is 1-month/QTD `-1.90%`, YTD `21.54%`, 1-year `33.62%`, 3-year `13.24%`, 5-year `7.45%`, 10-year `10.75%`, and since inception `10.08%`; linked benchmark returns are YTD `21.55%`, 1-year `33.64%`, 3-year `13.26%`, 5-year `7.48%`, 10-year `10.79%`, and since inception `10.09%`. The June 2026 table remains a separate older standardized observation.
- Benchmark continuity: State Street links Russell 2000 from inception through 2017-11-16, SSGA Small Cap Index from 2017-11-16 through 2020-01-24, and S&P SmallCap 600 Index from 2020-01-24 onward. Index returns are unmanaged/gross of fund fees; fund NAV returns are net of fees with dividends and capital gains reinvested.
- Annual/calendar candidate claims: complete official SPSM calendar-year NAV rows for 2016-2025 are `not disclosed` in the reviewed current issuer capture; up/down counts, best/worst years, and a 2021-2025 CAGR are therefore not calculated. Cached `S&P 500 Total Return` rows for 2016-2025 are retained only as a common reference, USD, dividends reinvested, as of 2025-12-31; original reference sources are https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true, https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf, and https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/.
- Tracking observations: using the rounded July table, NAV trails the linked benchmark by `-0.01 pp` YTD, `-0.02 pp` for 1-year, `-0.02 pp` for 3-year, `-0.03 pp` for 5-year, `-0.04 pp` for 10-year, and `-0.01 pp` since inception; this is a passive tracking observation, not alpha.
- As-of reconciliation: the prior durable page used NAV `USD 58.20`, bid/ask midpoint `USD 58.22`, and premium/discount `+0.02%` as of 2026-08-13; later State Street observations are NAV `USD 57.06`, midpoint `USD 57.07`, closing price `USD 57.06`, and AUM `USD 17,080.79M` as of 2026-08-27. The July performance table remains the latest standardized NAV TR source and is not mixed with the later daily quote.
- Evidence gaps: official calendar-year NAV rows and raw 10-year NAV TR endpoints remain `ไม่พบข้อมูลที่ยืนยันได้`; daily NAV history sufficient for reproducible maximum drawdown/recovery and volatility is not available in the reviewed capture. No annual proxy is substituted.
- Pre-save evidence packet: identity/exchange, passive-equity classification, return basis, issuer/common benchmarks, candidate claims, periods, units/currency, metric definitions, as-of dates, source URLs, current-field reconciliation, benchmark continuity, exposure data, unresolved gaps, and complete proposed contents for the SPSM performance page, USA ETF snapshot, ETF Performance Index row/refresh, source-batch section, and log bullet were checked locally.
- Pre-save checklist: passive/index-tracking equity eligibility verified; NAV TR versus market price/benchmark/after-tax bases separated; July performance and August quote/characteristics dates kept distinct; latest/as-of dates recorded per metric; cached S&P convention applied only to 2016-2025 common-reference rows; annual/daily-series gaps preserved; links, USA breadcrumb, and planned files checked; result `PASS`.
- verification_mode: scheduled-local
- reviewer_dispatch: not-attempted-by-design

## DXMEF / XMED — Xtrackers MSCI Europe UCITS ETF 1C

### Identity and classification

- `workflow: check-etf-performance`; `execution_profile: scheduled-inline`; input ticker `DXMEF` is an OTC alias and the official DWS listing maps ISIN `LU0274209237` to the London Stock Exchange USD line `XMED LN` / `LSE:XMED`. Durable ownership remains `entity_key: LSE:XMED`, with `input_ticker: DXMEF` preserved.
- Official DWS factsheet as of `2026-07-31`: fund/share-class launch `2007-01-10`; Luxembourg domicile; share-class/fund currency USD; direct physical replication; capitalizing income; all-in fee `0.12% p.a.`; issuer benchmark `MSCI Total Return Net Europe Index`; 397 constituents; the fund invests in large- and mid-cap developed European companies representing approximately 85% of free-float market capitalisation.
- DWS describes the product as an index-tracking physical equity ETF. It is eligible for the passive, index-tracking equity workflow. Primary region is `Europe`; the existing `[[Europe ETF]]` page and `[[ETF Performance Index]]` row are the navigation owners.

### Source map

| Source | URL/path | Use |
|---|---|---|
| DWS official Xtrackers factsheet, data as of 2026-07-31 | https://etf.dws.com/download/asset/9851b59e-0dd9-4624-9a83-9f580e0a60a3 | ISIN, USD share class/fund currency, launch, LSE XMED mapping, fee, NAV, assets, replication, benchmark, constituents and risk disclosures |
| DWS official NAV portal | https://etf.dws.com/it-it/nav/?PageSize=327 | Current portal observation for ISIN `LU0274209237` dated 2026-08-27; portal displays NAV `120.68` without a currency column, so it is not merged into the USD return/price fields |
| Morningstar XMED performance report | https://lt.morningstar.com/1c6qh1t6k9/etfreport/default.aspx?1=1&ClientFund=0&CurrencyId=USD&Id=0P0000M2W8&SecurityToken=0P0000M2W8%5D22%5D0%5DETEXG%24XLON&tab=1 | Secondary USD annual rows as of 2026-07-31 and trailing fields as of 2026-08-26 |
| Morningstar XMED overview | https://lt.morningstar.com/1c6qh1t6k9/etfreport/default.aspx?1=1&ClientFund=0&CurrencyId=USD&Id=0P0000M2W8&SecurityToken=0P0000M2W8%5D22%5D0%5DETEXG%24XLON&tab=0 | Secondary USD NAV/closing-price snapshot, net assets and portfolio profile |
| DTCC OTC notice | https://www.dtcc.com/-/media/Files/pdf/2016/5/16/OTC-094.pdf | DXMEF OTC symbol/name cross-check |
| Cached benchmark convention | workflow cache; original S&P references are listed on the performance page | S&P 500 Total Return common-reference rows for 2021-2025, USD, dividends reinvested |

### Candidate performance claims and raw observations

- Official DWS factsheet as of `2026-07-31` reports NAV `US$140.30`, total fund assets `US$9.93 billion`, total shares outstanding `64.38 million`, and 397 index constituents. It links historical performance to an online page but does not expose numeric annual or current YTD rows in the reviewed factsheet.
- Secondary Morningstar USD annual rows as of `2026-07-31` are 2021 `16.58%`, 2022 `-14.85%`, 2023 `20.18%`, 2024 `2.02%`, 2025 `35.77%`, and partial 2026 `9.77%`; trailing fields as of `2026-08-26` are YTD `12.58%`, 1-year `21.70%`, 3-year annualised `19.36%`, 5-year annualised `10.05%`, and 10-year annualised `9.94%`.
- Morningstar's USD overview reports NAV/closing price `US$141.55` as of `2026-08-26`, net assets `US$9,772.12 million` as of `2026-07-31`, and total expense ratio `0.12%`. These are secondary current observations and are not merged with the official DWS July NAV `US$140.30`.
- Morningstar's comparator is `Morningstar Developed Europe Target Market Exposure NR EUR`; DWS's issuer benchmark remains `MSCI Total Return Net Europe Index`. The Morningstar comparator is not treated as manager-skill evidence or as a replacement issuer benchmark.
- Supplemental secondary portfolio profile as of `2026-07-31`: Eurozone `51.06%`, Europe ex Euro `24.36%`, United Kingdom `21.63%`; Financial Services `25.37%`, Industrials `19.52%`, and Healthcare `13.12%`. These are contextual only; no unsupported official DWS sector weights are inferred.
- Official daily NAV history sufficient for reproducible maximum drawdown/recovery is `ไม่พบข้อมูลที่ยืนยันได้`. Euro-labelled ETFdoc/Quantalys rows and conflicting Stuttgarter rows remain source conflicts and are excluded from the USD calculation.

### Calculations and reconciliation

- Secondary USD 2021-2025 cumulative return: `(1.1658 × 0.8515 × 1.2018 × 1.0202 × 1.3577) - 1 = 65.25%`; rounded-input CAGR `(1 + 0.6525)^(1/5) - 1 = 10.57%`; population standard deviation `17.17%`; up/down years `4 / 1`; best year 2025 `+35.77%`; worst year 2022 `-14.85%`.
- Cached S&P 500 Total Return common reference for 2021-2025 is cumulative `96.17%` / rounded-input CAGR `14.43%`; this is USD, dividends reinvested, and is not XMED's issuer benchmark.
- The secondary rolling 10-year field `9.94%*`, YTD `12.58%*`, and USD NAV/closing price `US$141.55` are each retained with their `2026-08-26` as-of date; the official DWS NAV/identity snapshot remains dated `2026-07-31`. No cross-currency calculation is made.
- The DWS NAV portal's `120.68` observation is retained as an unlabelled-currency current portal field and not used in the USD calculation. No official issuer annual NAV table, official current YTD field, or official daily drawdown/recovery series was exposed.

### Pre-save evidence packet and proposed durable contents

- Evidence packet records ETF identity and exchange, OTC alias, ISIN, return basis, issuer and common benchmarks, candidate annual/trailing/rolling/price/NAV claims, periods, units/currency, metric definitions, as-of dates, source URLs, calculations, source conflicts, unresolved gaps, and the complete planned contents.
- Proposed `wiki/analysis/performance/ETF_LSE_XMED Performance.md`: refresh frontmatter/source batch, retain the secondary USD 2021-2025 table and calculations, update Morningstar current USD trailing/NAV fields, retain official DWS July identity/NAV/facts, preserve source conflicts and daily drawdown gap, and keep the Europe breadcrumb and alias tags.
- Proposed `wiki/analysis/comparisons/Europe ETF.md`: update only the XMED row and explanatory note with secondary USD rolling 10-year `9.94%*`, 2021-2025 CAGR `10.57%*`, YTD `12.58%*`, and secondary USD NAV/closing price `US$141.55` as of 2026-08-26.
- Proposed `wiki/analysis/performance/ETF Performance Index.md`: update the XMED coverage row, explanatory note, and detailed performance-owner summary with the same dated secondary metrics and source-gap disclosure.
- Proposed `raw/imports/ETF_performance_sources_2026-08-29.md`: append this evidence packet, local checklist, and structured `trello_handoff`.
- Proposed `log.md`: append one `etf-performance` workflow bullet listing the XMED performance page, Europe/index updates, and scheduled-local PASS; `log.md` remains outside the scoped commit because it already contains unrelated user changes.

### Local pre-save checklist

- PASS: official DWS ISIN/listing mapping, canonical `LSE:XMED` exchange key, OTC alias, passive physical classification, issuer benchmark, fee, return basis, units/currency, periods, metric definitions, and as-of dates are recorded.
- PASS: official DWS July identity/NAV/facts are separated from secondary Morningstar USD annual/trailing/NAV fields; the DWS NAV portal's unlabelled-currency value is not merged; Euro-labelled and conflicting secondary series are excluded; no daily NAV drawdown/recovery claim is invented.
- PASS: secondary USD 2021-2025 cumulative/CAGR/dispersion calculations reproduce the saved table; cached S&P 500 TR is labeled common reference only; no unsupported official annual/current value or cross-currency calculation is made.
- PASS: complete proposed contents for performance, region, index, source batch, and log artifacts are specified; Europe breadcrumb, alias tags, region ownership, source conflicts, and links are preserved; no unresolved High/Medium finding blocks the write and no WARNING requiring confirmation remains.
- verification_mode: scheduled-local
- reviewer_dispatch: not-attempted-by-design

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official DWS identity and current secondary USD evidence support the XMED refresh; the scheduled-local checklist passed and currency, source-gap, and drawdown limitations remain disclosed.

## OPPJ — WisdomTree Japan Opportunities Fund

### Identity and classification

- `workflow: check-etf-performance`; `execution_profile: scheduled-inline`; `child_card_ari: ari:cloud:trello::card/workspace/6a78536437ed0b3b544c19e1/6a91772b924e9bf819ec2584`; `parent_ari: ari:cloud:trello::card/workspace/6a78536437ed0b3b544c19e1/6a91760cdaae83b3d4afdc13`; input ticker `OPPJ`; canonical `entity_key: NASDAQ:OPPJ`.
- WisdomTree's product page and prospectus identify OPPJ as the Nasdaq-listed WisdomTree Japan Opportunities Fund, inception `2013-06-28`, CUSIP `97717W521`, and a passive/index-tracking equity ETF. The prospectus describes representative sampling and an 80% policy for index constituents or substantially similar investments; it also identifies the fund as non-diversified.
- The fund seeks to track the `WisdomTree Japan Opportunities Index`. Before `2025-07-01`, it was the WisdomTree Japan Hedged SmallCap Equity Fund under ticker DXJS; the durable record therefore labels pre-change history and 2025 as a spliced strategy record. Primary region is `Japan`; ownership remains with `[[Japan ETF]]` and `[[ETF Performance Index]]`.

### Source map

| Source | URL/path | Use |
|---|---|---|
| WisdomTree OPPJ product page | https://www.wisdomtree.com/us/products/equity/oppj | Official identity, passive objective, current NAV/price, July standardized returns, assets, fee, portfolio characteristics, holdings, sectors, hedge ratio and distributions |
| WisdomTree OPPJ factsheet | https://www.wisdomtree.com/us/media/wisdomtree-factsheet-oppj | Official 2026-06-30 performance/benchmark cross-check, NASDAQ listing, 88 holdings, fee, fund size and strategy-change disclosure |
| SEC OPPJ summary prospectus | https://www.sec.gov/Archives/edgar/data/1350487/000121465925011309/oppj73125497k.htm | Passive management, 80% policy, index construction, dynamic JPY/USD hedge, non-diversified status and principal risks; official annual rows through 2024 |
| WisdomTree Japan Opportunities Index | https://www.wisdomtree.com/us/indexes/WTJOP | Current index design, 0-100% dynamic hedge description, 88 components, country/industry profile and definitions |
| Schwab OPPJ exchange-traded-funds report | https://www.schwab.wallst.com/Prospect/research/etfs/reports/reportRetrieve.asp?reportType=etfrc&symbol=OPPJ | Secondary 2025 annual row, current July standardized cross-check, current price and portfolio profile |
| PortfoliosLab OPPJ | https://portfolioslab.com/symbol/OPPJ | Secondary adjusted-market-price drawdown/recovery proxy retained with explicit non-NAV label |
| S&P 500 index page and cached workflow references | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Common USD Total Return reference rows for complete 2016-2025 and 2021-2025 windows; dividends reinvested |

### Candidate performance claims and raw observations

- Official WisdomTree month-end table as of `2026-07-31`: underlying-index YTD `24.86%`, NAV YTD `24.40%`, market-price YTD `22.02%`; NAV 1-year `56.11%`, 3-year annualised `31.08%`, 5-year annualised `24.91%`, 10-year annualised `17.00%`, and since-inception annualised `15.24%`. The issuer's underlying-index fields are before fund expenses; NAV total return is the durable return basis.
- Official current fund overview as of `2026-08-28`: NAV `US$57.915`, change `+0.20%`, premium/discount `-0.09%`, total assets `US$283.78305M`, shares outstanding `4,900,000`, distribution yield `2.35%`, SEC 30-day yield `1.77%`, and net expense ratio `0.58%`.
- Official trading/portfolio snapshot as of `2026-08-27`: closing market price `US$57.750`, 30-day average volume `37,662`, median bid/ask spread `0.49%`, P/E `14.17x`, estimated P/E `13.03x`, P/B `1.63x`, dividend yield `2.17%`, gross buyback yield `1.75%`, and net buyback yield `1.63%`.
- Official current hedge ratio is `97.24%` as of `2026-08-28`; WisdomTree states hedge ratios are implemented after the last business day of each month. Current country exposure is Japan `100.00%`; current holdings and sectors are as of `2026-08-27`.
- Current top holdings are Sumitomo `8.32%`, Mitsubishi `7.47%`, Marubeni `7.19%`, Mitsui `6.83%`, Itochu `5.90%`, Kioxia `4.12%`, Tokio Marine `3.92%`, Panasonic `2.52%`, Tokyo Electron `2.32%`, and Hanwa `2.09%`; the displayed top-ten weights sum to `50.68%`. Current sector weights are Industrials `48.27%`, Information Technology `13.99%`, Materials `11.31%`, Financials `11.12%`, Consumer Discretionary `7.55%`, Health Care `3.12%`, Consumer Staples `2.28%`, Communication Services `1.58%`, and Real Estate `0.78%`.
- Official June factsheet cross-check as of `2026-06-30` reports OPPJ NAV YTD `24.67%`, 10-year average annual NAV TR `17.89%`, 5-year `24.84%`, since-inception `15.37%`, and fund net assets `US$280.24M`. It reports the same strategy-change caveat and the spliced `WisdomTree Japan Hedged SmallCap Equity/WisdomTree Japan Opportunities` index.
- Official annual NAV rows through 2024 are `2016 6.88%`, `2017 29.46%`, `2018 -17.82%`, `2019 18.33%`, `2020 -4.64%`, `2021 11.98%`, `2022 6.84%`, `2023 36.69%`, and `2024 20.68%`; these are rounded rows from the SEC summary prospectus and largely reflect the predecessor DXJS objective. The 2025 row `36.20%*` remains a secondary standardized NAV total-return observation from Schwab, not an issuer calendar row.
- Official product/factsheet related index symbol is `WTJOPN`, while the current WisdomTree index page uses `WTJOP`; both labels are preserved as source-display identifiers for the same named Japan Opportunities Index and do not alter `NASDAQ:OPPJ` identity.
- Secondary adjusted-market-price evidence retains maximum drawdown `-39.30%` from 2018-01-09 to 2020-03-16 and recovery 2021-03-15; official daily NAV history sufficient to reproduce a fund-level drawdown/recovery is `ไม่พบข้อมูลที่ยืนยันได้`.

### Calculations and reconciliation

- 2016-2025 rounded annual-row calculation: `(1.0688 × 1.2946 × 0.8218 × 1.1833 × 0.9536 × 1.1198 × 1.0684 × 1.3669 × 1.2068 × 1.3620) - 1 = 244.89%`; rounded-input CAGR `(1 + 2.4489)^(1/10) - 1 = 13.18%`; population standard deviation `16.66%`; positive/negative years `8 / 2`.
- 2021-2025 rounded annual-row calculation: `(1.1198 × 1.0684 × 1.3669 × 1.2068 × 1.3620) - 1 = 68.80%`; rounded-input CAGR `(1 + 0.6880)^(1/5) - 1 = 21.87%`; population standard deviation `12.23%`; positive/negative years `5 / 0`.
- Cached S&P 500 Total Return common reference is cumulative `298.33%` / CAGR `14.82%` for 2016-2025 and cumulative `96.17%` / CAGR `14.43%` for 2021-2025; it is USD, dividends reinvested, and is not OPPJ's issuer benchmark or manager-skill evidence.
- July standardized tracking observations are NAV versus underlying index: YTD `24.40%` vs `24.86%` (`-0.46 pp`), 1-year `56.11%` vs `57.24%` (`-1.13 pp`), 3-year `31.08%` vs `31.76%` (`-0.68 pp`), 5-year `24.91%` vs `25.54%` (`-0.63 pp`), 10-year `17.00%` vs `17.66%` (`-0.66 pp`), and since inception `15.24%` vs `16.00%` (`-0.76 pp`). These are tracking/fee observations, not alpha.
- The July issuer rolling 10-year average annual NAV TR `17.00%` covers `2016-07-31` to `2026-07-31`. Because raw endpoints are not exposed, shown calculation `100 × (1 + 0.17)^10 = 480.68` is an implied growth endpoint and implied cumulative `380.68%`, not a sourced NAV/TR level.
- As-of reconciliation: prior June quarter-end values were NAV YTD `24.67%` and rolling 10-year `17.89%`; the later July month-end product table reports `24.40%` and `17.00%`. These standardized windows are kept separate from the August 27-28 quote, fund-facts and hedge snapshots. No cross-date arithmetic is performed.
- The prior index common-window row showed `168.80%*`; recomputation from the saved annual rows gives `68.80%*` cumulative return (growth factor `1.6880`), so the index row is corrected and the correction is disclosed here.

### Pre-save evidence packet and proposed durable contents

- Evidence packet records child card/parent ARIs, ETF identity and Nasdaq exchange, inception, passive classification, return basis, issuer/common benchmarks, strategy and index transition, all candidate annual/trailing/rolling/current claims, periods, units/currency, metric definitions, as-of dates, source URLs, calculations, source-label conflicts, current exposure, unresolved gaps and the complete planned file changes.
- Proposed `wiki/analysis/performance/ETF_NASDAQ_OPPJ Performance.md`: update frontmatter/source batch; refresh bottom line, current official July return fields, August NAV/price/fund-facts/hedge snapshot, annual table labels, rounded-input calculations, tracking observations, current exposure, risk read-through, strategy-transition reconciliation, source links and follow-up gaps; preserve the canonical Japan breadcrumb and secondary 2025/drawdown markers.
- Proposed `wiki/analysis/comparisons/Japan ETF.md`: replace the OPPJ snapshot row with fund name, official rolling 10-year `17.00%`, 2021-2025 `21.87%*`, and July YTD `24.40%`; append the dated OPPJ verified-refresh note and retain the Japan navigation contract.
- Proposed `wiki/analysis/performance/ETF Performance Index.md`: replace the OPPJ coverage row with July rolling/YTD fields and current risk labels; correct the Common Window cumulative field to `68.80%*`; update the OPPJ continuity note with July YTD and current hedge ratio; preserve the existing performance-owner wikilink.
- Proposed `raw/imports/ETF_performance_sources_2026-08-29.md`: append this OPPJ evidence packet, local pre-save checklist and structured `trello_handoff`.
- Proposed `log.md` exact bullet: ``- `etf-performance`: Refreshed [[ETF_NASDAQ_OPPJ Performance]] with official July rolling 10-year NAV TR `17.00%`, current NAV TR YTD `24.40%`, and current NAV `US$57.915` as of 2026-08-28; corrected the 2021-2025 cumulative calculation to `68.80%`, updated [[Japan ETF]], [[ETF Performance Index]], and [[ETF_performance_sources_2026-08-29]], and preserved the DXJS-to-OPPJ strategy-break caveat.`` `log.md` remains outside the scoped commit because it already contains unrelated user changes.
- No ETF entity hub or new region page is required; `NASDAQ:OPPJ` remains the canonical performance owner and the existing Japan region page remains the sole regional navigation owner.

### Local pre-save checklist

- PASS: Nasdaq identity, fund name, inception, passive/index-tracking equity eligibility, canonical key, tracked index, return basis, USD units, dynamic hedge policy, and current/predecessor strategy split are source-mapped.
- PASS: official July standardized NAV/index/market-price bases are separated; June quarter-end figures are retained only as a dated cross-check; August NAV, closing price, assets, yields, valuation fields, holdings, sectors and hedge ratio retain their individual as-of dates; no current value is backfilled.
- PASS: official 2016-2024 annual rows, secondary 2025 row, 2016-2025 and 2021-2025 calculations, cached S&P reference, passive tracking differences, and corrected `68.80%` Common Window cumulative return reproduce the planned page/index values; no arithmetic excess return is called alpha.
- PASS: strategy-change caveat, non-diversified/single-country/sector/hedge/derivatives risks, secondary drawdown proxy, official daily NAV gap, source-display symbol difference, source links, canonical breadcrumb, region ownership, and complete proposed file contents are disclosed; no unresolved High/Medium finding blocks the write and no WARNING requiring confirmation remains.
verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official WisdomTree July performance and August fund snapshots support the OPPJ refresh; scheduled-local verification passed, the DXJS strategy transition and secondary 2025/drawdown limitations remain disclosed, and the Common Window cumulative arithmetic was corrected to 68.80%.

## VIGI — Vanguard International Dividend Appreciation ETF

### Identity and classification

- `workflow: check-etf-performance`; `execution_profile: scheduled-inline`; `child_card_ari: ari:cloud:trello::card/workspace/6a78536437ed0b3b544c19e1/6a9177308f6ae33ff619e408`; `parent_ari: ari:cloud:trello::card/workspace/6a78536437ed0b3b544c19e1/6a91760cdaae83b3d4afdc13`; input ticker `VIGI`; canonical `entity_key: NASDAQ:VIGI`.
- Vanguard identifies VIGI as the Nasdaq-listed Vanguard International Dividend Appreciation ETF, inception `2016-02-25`, CUSIP `921946810`, and a passive/index-tracking equity ETF. The strategy is fully invested/full replication and targets large-cap developed and emerging markets outside the United States.
- Issuer benchmark is `S&P Global Ex-U.S. Dividend Growers Index (USD) NTR`. Primary region is `International`; ownership remains with `[[International ETF]]` and `[[ETF Performance Index]]`.

### Source map

| Source | URL/path | Use |
|---|---|---|
| Vanguard advisor product page | https://advisors.vanguard.com/investments/products/vigi/vanguard-international-dividend-appreciation-etf | Current NAV TR YTD, market-price YTD, expense ratio, distribution yield, spread, holdings, net assets and current portfolio metrics |
| Vanguard investor VIGI product page | https://investor.vanguard.com/investment-products/etfs/profile/vigi | Product identity and annual performance source |
| Vanguard fund list | https://workplace.vanguard.com/fund-list/?filters=eqIndex%2C&viewType=monthEndReturnNAV | Official standardized average annual returns as of 2026-07-31 and separately dated YTD field |
| Vanguard VIGI factsheet | https://fund-docs.vanguard.com/F4415.pdf | June 2026 performance cross-check, benchmark, strategy, holdings, country/sector mix and risk fields |
| Schwab VIGI report | https://www.schwab.wallst.com/schwab/Prospect/research/etfs/reports/reportRetrieve.asp?reportType=etfrc&symbol=VIGI | Secondary current market price and rounded standardized cross-check |
| S&P Global Ex-U.S. Dividend Growers Index | https://www.spglobal.com/spdji/en/indices/dividends-factors/sp-global-ex-us-dividend-growers-index/ | Issuer benchmark identity |
| S&P Dividend Growers Index Series Methodology | https://www.spglobal.com/spdji/en/documents/methodologies/methodology-sp-dividend-growers-index-series.pdf | Index methodology context |
| S&P 500 index page and cached workflow references | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Common USD Total Return reference rows for the stated complete calendar windows; dividends reinvested |
| PortfoliosLab VIGI | https://portfolioslab.com/symbol/VIGI | Secondary adjusted-price drawdown/recovery proxy |

### Candidate performance claims and raw observations

- Official Vanguard fund-list capture reports as of `2026-07-31`: NAV Total Return 1-year `15.69%`, 3-year annualised `10.58%`, 5-year annualised `5.32%`, 10-year annualised `8.01%`, and since-inception annualised `9.12%`. The same table separately labels YTD `9.80%` as of `2026-08-11`; it is retained as a dated separate observation.
- Later official Vanguard advisor-page capture reports current YTD NAV Total Return `9.18%` and market-price return `9.01%`, both as of `2026-08-26`; this later YTD field is the current durable value.
- Official current/near-current fund facts include net expense ratio `0.07%` as of `2026-02-27`, distribution yield `2.13%` as of `2026-07-31`, median bid/ask spread `0.06%` as of `2026-08-25`, holdings `341` as of `2026-07-31`, ETF net assets `US$9.1B`, fund total net assets `US$9.4B`, and 3-year standard deviation `12.05%` as of `2026-07-31`. Current portfolio metrics include P/E `20.7x`, P/B `2.9x`, turnover `13.90%`, developed-market exposure `94.96%`, emerging-market exposure `5.04%`, and foreign holdings `99.23%`.
- Official June factsheet as of `2026-06-30` reports NAV TR YTD `3.70%`, 1-year `6.06%`, 3-year `9.85%`, 5-year `4.65%`, 10-year `7.89%`, and since inception `8.80%`; it reports benchmark/index rows separately and is retained only as an older cross-check. June standard deviation is `11.93%`, holdings/benchmark constituents `342`, ETF net assets `US$8,725M`, and fund net assets `US$9,080M`.
- The June factsheet country weights are Japan `30.6%`, Canada `23.7%`, Switzerland `14.6%`, United Kingdom `5.3%`, Germany `5.0%`, India `3.2%`, France `3.2%`, Spain `2.9%`, Denmark `2.8%`, and Hong Kong `1.7%`. Top-ten holdings are RBC `4.9%`, Mitsubishi UFJ `4.3%`, Nestle `3.9%`, TD `3.7%`, Novartis `3.6%`, Roche `3.5%`, Schneider `3.2%`, SAP `2.8%`, Iberdrola `2.8%`, and Novo Nordisk `2.8%`, approximately `35.4%` combined. Sector weights are Financials `29.1%`, Industrials `16.3%`, Health Care `14.6%`, Technology `11.4%`, Consumer Staples `8.6%`, Consumer Discretionary `5.9%`, Utilities `5.9%`, Basic Materials `3.5%`, Energy `2.5%`, Real Estate `1.1%`, and Telecommunications `1.0%`.
- Secondary Schwab capture generated `2026-08-28` reports market price `US$98.55` as of `2026-08-28` and rounded July fields; it reports a different holdings profile of `370` as of `2026-08-18`. The secondary price is retained as market-price context only; no current official NAV or premium/discount is inferred.
- Official annual NAV rows are `2016 6.64%` (inception-year partial), `2017 27.80%`, `2018 -11.32%`, `2019 27.04%`, `2020 15.11%`, `2021 12.42%`, `2022 -16.71%`, `2023 16.16%`, `2024 2.62%`, and `2025 16.89%`. Cached S&P 500 TR rows used as a common USD reference are 2017-2025 `21.83%, -4.38%, 31.49%, 18.40%, 28.71%, -18.11%, 26.29%, 25.02%, 17.88%` and 2021-2025 `28.71%, -18.11%, 26.29%, 25.02%, 17.88%`; the cache is as of `2025-12-31`, dividends reinvested, and is not VIGI's strategy benchmark.
- Secondary adjusted-price evidence from PortfoliosLab reports maximum drawdown about `-31.01%` during the COVID period and `114` trading sessions to recover. Official daily NAV history sufficient for a reproducible fund-level drawdown/recovery remains `ไม่พบข้อมูลที่ยืนยันได้`.

### Calculations and reconciliation

- 2017-2025 rounded annual-row calculation: `(1.2780 × 0.8868 × 1.2704 × 1.1511 × 1.1242 × 0.8329 × 1.1616 × 1.0262 × 1.1689) - 1 = 116.23%`; rounded-input CAGR `(1 + 1.1623)^(1/9) - 1 = 8.95%`; population standard deviation `14.71%`; positive/negative years `7 / 2`.
- 2021-2025 rounded annual-row calculation: `(1.1242 × 0.8329 × 1.1616 × 1.0262 × 1.1689) - 1 = 30.47%`; rounded-input CAGR `(1 + 0.3047)^(1/5) - 1 = 5.46%`; population standard deviation `12.57%`; positive/negative years `4 / 1`.
- Cached S&P 500 TR common reference is cumulative `255.78%` / CAGR `15.14%` for 2017-2025 and cumulative `96.17%` / CAGR `14.43%` for 2021-2025. It is a USD reference only and no arithmetic excess return is called alpha.
- The issuer's rolling 10-year average annual NAV TR `8.01%` as of `2026-07-31` implies normalized growth `100.00 → 216.09`, or cumulative `116.09%`, via `100 × ((1 + 0.0801)^10 - 1)`. Raw endpoints are not disclosed, so the implied endpoint is not presented as a sourced NAV level.
- As-of reconciliation: June factsheet YTD/10-year were `3.70%`/`7.89%`; July standardized 1-year/10-year were `15.69%`/`8.01%`; current advisor-page YTD is `9.18%` as of 2026-08-26. The separate fund-list YTD `9.80%` is dated 2026-08-11. These fields are not mixed into one period.
- Current official benchmark YTD in the same as-of capture was not exposed. The current official NAV/market-price pair and official daily NAV drawdown series were also not exposed; these remain explicit gaps.

### Pre-save evidence packet and proposed durable contents

- Evidence packet records child/parent ARIs, Nasdaq identity, inception/CUSIP, passive classification, return basis, issuer/common benchmarks, candidate annual/rolling/current claims, periods, units/currency, metric definitions, as-of dates, source URLs, calculations, current exposure, secondary conflicts, unresolved gaps and the complete planned file changes.
- Proposed `wiki/analysis/performance/ETF_NASDAQ_VIGI Performance.md`: replace the stale July page with current frontmatter; preserve the official 2016† and 2017-2025 annual NAV table; add the official July 1/3/5/10-year and since-inception fields; use current official YTD NAV/market-price fields; add the rolling-10-year implied calculation, annual-window calculations, current fund snapshot, official June country/sector/top-ten context, international FX/country/sector/dividend-factor risks, secondary drawdown proxy, as-of reconciliation, source links and follow-up gaps; retain the canonical International breadcrumb and `geography/International` tag.
- Proposed `wiki/analysis/comparisons/International ETF.md`: update only the VIGI row to official rolling 10-year `8.01%`, 2021-2025 CAGR `5.46%`, and current official YTD `9.18%`; append a `2026-08-29 Verified Refresh` note distinguishing the issuer rolling field from the calendar-row CAGR and disclosing the current NAV-pair/drawdown gaps.
- Proposed `wiki/analysis/performance/ETF Performance Index.md`: update the VIGI coverage row to rolling 10-year `8.01%`, 2021-2025 `5.46%`, current YTD `9.18%`, best/worst `2025 +16.89% / 2022 -16.71%`, and the `12.05%` 3-year standard-deviation/daily-NAV-gap behavior label; append the dated VIGI note below the existing issuer-field footnotes. The Common Window row remains `30.47%` because its annual inputs did not change.
- Proposed `raw/imports/ETF_performance_sources_2026-08-29.md`: append this VIGI identity/source map, raw claims, calculations, reconciliation, complete proposed contents, local checklist, exact scheduled-inline verification lines, and structured `trello_handoff`.
- Proposed `log.md` exact bullet: ``- `etf-performance`: Refreshed [[ETF_NASDAQ_VIGI Performance]] with official July rolling 10-year NAV TR `8.01%`, current NAV TR YTD `9.18%` as of 2026-08-26, and 2017-2025 CAGR `8.95%`; updated [[International ETF]], [[ETF Performance Index]], and [[ETF_performance_sources_2026-08-29]], while preserving the current NAV-pair and official daily drawdown gaps.`` `log.md` remains outside the scoped commit because it already contains unrelated user changes.
- No ETF entity hub or new region page is required; `NASDAQ:VIGI` remains the canonical performance owner and the existing International region page remains the sole regional navigation owner.

### Local pre-save checklist

- PASS: official Nasdaq identity, fund name, inception, passive/full-replication equity eligibility, canonical key, tracked index, return basis, USD units, and International region ownership are source-mapped.
- PASS: official July standardized fields, the separate August 11 YTD table, later August 26 current YTD, secondary August 28 price, and June factsheet cross-check retain individual as-of dates; NAV, market price, benchmark, distribution and holdings metrics are not conflated.
- PASS: official annual rows, 2017-2025 and 2021-2025 calculations, rolling-10-year implied calculation, cached S&P common reference, secondary drawdown proxy and all unresolved current NAV/daily-series gaps reproduce the proposed page/index values; no unsupported benchmark-current or NAV endpoint is inferred.
- PASS: complete proposed contents for performance, International region, index, source batch and log artifacts are specified; canonical breadcrumb/tag, source links, secondary conflicts and follow-up gaps are preserved; no unresolved High/Medium finding blocks the write and no WARNING requiring confirmation remains.
verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official Vanguard July standardized fields and current August YTD support the VIGI refresh; scheduled-local verification passed and current NAV-pair, calendar/benchmark-current, and daily drawdown gaps remain disclosed.

## VYMI — Vanguard International High Dividend Yield ETF

### Identity and classification

- `workflow: check-etf-performance`; `execution_profile: scheduled-inline`; `child_card_ari: ari:cloud:trello::card/workspace/6a78536437ed0b3b544c19e1/6a9177346ed613956b8949e6`; `parent_ari: ari:cloud:trello::card/workspace/6a78536437ed0b3b544c19e1/6a91760cdaae83b3d4afdc13`; input ticker `VYMI`; canonical `entity_key: NASDAQ:VYMI`.
- Vanguard identifies VYMI as the Nasdaq-listed Vanguard International High Dividend Yield ETF, inception `2016-02-25`, CUSIP `921946794`, and a passive/index-tracking equity ETF. The fund uses a sampling strategy, remains fully invested, and targets large- and mid-cap developed and emerging markets outside the United States with above-average forecast dividend yields.
- Issuer benchmark is `FTSE All-World ex US High Dividend Yield Index` (`GPVAN0TR`). Primary region is `International`; ownership remains with `[[International ETF]]` and `[[ETF Performance Index]]`.

### Source map

| Source | URL/path | Use |
|---|---|---|
| Vanguard advisor product page | https://advisors.vanguard.com/investments/products/vymi/vanguard-international-high-dividend-yield-etf | Current official YTD, rolling return summary, expense, yield, spread, assets, strategy and portfolio facts |
| Vanguard investor VYMI product page | https://investor.vanguard.com/investment-products/etfs/profile/vymi | Product identity and annual performance source |
| Vanguard fund list | https://workplace.vanguard.com/fund-list/?filters=etf | Official standardized average annual returns as of 2026-07-31 and separately dated YTD field as of 2026-08-11 |
| Vanguard VYMI factsheet | https://workplace.vanguard.com/assets/corp/fund_communications/pdf_publish/us-products/fact-sheet/F4430.pdf | June 2026 performance/index cross-check, strategy, holdings, country/sector mix and risk fields |
| Schwab VYMI report | https://www.schwab.wallst.com/schwab/Prospect/research/etfs/reports/reportRetrieve.asp?reportType=etfrc&symbol=VYMI | Secondary current price and rounded standardized cross-check |
| PortfoliosLab VYMI | https://portfolioslab.com/symbol/VYMI | Secondary adjusted-price total-return drawdown/recovery proxy |
| S&P 500 index page and cached workflow references | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Common USD Total Return reference rows for the stated complete calendar windows; dividends reinvested |

### Candidate performance claims and raw observations

- Official Vanguard fund-list capture reports average annual NAV Total Return as of `2026-07-31`: 1-year `34.56%`, 3-year `21.47%`, 5-year `14.05%`, 10-year `10.98%`, and since inception `11.68%`. The same table separately labels YTD `18.37%` as of `2026-08-11`; it is retained as a dated separate observation.
- Later official Vanguard advisor-page capture reports current YTD NAV Total Return `19.86%` as of `2026-08-26`; this later YTD field is the current durable value. The page's earlier capture reported `18.22%` as of `2026-08-05`, which is retained only as an older observation.
- Official current/near-current fund facts include net expense ratio `0.07%` as of `2026-02-27`, dividend yield `3.69%` as of `2026-07-31`, median bid/ask spread `0.01%` as of `2026-08-26`, total net assets `US$21.9B`, and net assets for VYMI `US$21.0B`, all with the individual as-of dates exposed by Vanguard. Latest verified official holdings count is `1,565` as of `2026-06-30`.
- Official June factsheet as of `2026-06-30` reports NAV TR YTD `11.49%`, 1-year `27.47%`, 3-year `21.11%`, 5-year `12.72%`, 10-year `10.82%`, and since inception `11.22%`; corresponding market-price rows are `11.36%`, `27.47%`, `21.05%`, `12.69%`, `10.77%`, and `11.23%`. The FTSE index rows are `11.06%`, `27.59%`, `21.29%`, `12.87%`, `11.10%`, and `11.53%`. These are an older cross-check, not the current YTD field.
- Official June factsheet portfolio metrics include developed exposure `77.61%`, emerging exposure `22.39%`, foreign holdings `99.34%`, median market cap `US$65.0B`, P/E `14.1x`, P/B `1.7x`, ROE `13.0%`, earnings growth `9.9%`, turnover `8.8%`, and 3-year standard deviation `11.27%`. June ETF net assets were `US$19,502M` and fund total net assets `US$20,382M`.
- Official June country weights are Japan `11.5%`, United Kingdom `11.0%`, Canada `9.2%`, Switzerland `7.6%`, Australia `7.3%`, Taiwan `5.8%`, China `5.5%`, France `5.5%`, Spain `4.4%`, and Germany `4.3%`. Top ten holdings are HSBC `1.8%`, Roche `1.7%`, Novartis `1.6%`, Royal Bank of Canada `1.6%`, Nestle `1.5%`, Shell `1.2%`, Mitsubishi UFJ `1.2%`, BHP `1.2%`, Toronto-Dominion Bank `1.1%`, and Banco Santander `1.1%`, or `13.8%` combined. Sector weights are Financials `43.7%`, Energy `8.3%`, Consumer Staples `6.9%`, Consumer Discretionary `6.7%`, Health Care `6.6%`, Industrials `6.2%`, Basic Materials `6.1%`, Utilities `5.6%`, Technology `5.1%`, Telecommunications `3.6%`, and Real Estate `1.0%`.
- Official Vanguard distribution table shows the latest two 2026 income payments as `US$1.256900` payable `2026-06-23` and `US$0.708000` payable `2026-03-24`, totaling `US$1.964900` per share; these are distributions, not NAV Total Return.
- Secondary Schwab report generated `2026-08-25` reports price `US$105.17` as of `2026-08-24`, total assets `US$21.9B`, expense ratio `0.07%`, and rounded July NAV/market-price performance. It is used for price context only because the reviewed current official VYMI page did not expose a verified current NAV/market-price pair.
- Official annual NAV rows are `2016 15.75%` (inception-year partial), `2017 22.37%`, `2018 -12.39%`, `2019 18.31%`, `2020 -0.65%`, `2021 15.00%`, `2022 -6.90%`, `2023 16.88%`, `2024 6.97%`, and `2025 38.02%`. Cached S&P 500 TR rows used as a common USD reference are 2016 `11.96%`, 2017 `21.83%`, 2018 `-4.38%`, 2019 `31.49%`, 2020 `18.40%`, 2021 `28.71%`, 2022 `-18.11%`, 2023 `26.29%`, 2024 `25.02%`, and 2025 `17.88%`; the cache is as of `2025-12-31`, dividends reinvested, and is not VYMI's strategy benchmark.
- Secondary adjusted-price total-return evidence from PortfoliosLab reports maximum drawdown `-40.00%` on `2020-03-23` and recovery in `202` trading sessions, with the page updated `2026-08-28`. Official daily NAV history sufficient for a reproducible fund-level drawdown/recovery remains `ไม่พบข้อมูลที่ยืนยันได้`.

### Calculations and reconciliation

- 2017-2025 rounded annual-row calculation: `(1.2237 × 0.8761 × 1.1831 × 0.9935 × 1.1500 × 0.9310 × 1.1688 × 1.0697 × 1.3802) - 1 = 132.81%`; rounded-input CAGR `(1 + 1.3281)^(1/9) - 1 = 9.84%`; population standard deviation `14.84%`; positive/negative years `6 / 3`.
- 2021-2025 rounded annual-row calculation: `(1.1500 × 0.9310 × 1.1688 × 1.0697 × 1.3802) - 1 = 84.75%`; rounded-input CAGR `(1 + 0.8475)^(1/5) - 1 = 13.06%`; population standard deviation `14.65%`; positive/negative years `4 / 1`.
- Cached S&P 500 TR common reference is cumulative `255.78%` / CAGR `15.14%` for 2017-2025 and cumulative `96.17%` / CAGR `14.43%` for 2021-2025. It is a USD reference only and no arithmetic excess return is called alpha.
- The issuer's rolling 10-year average annual NAV TR `10.98%` as of `2026-07-31` implies normalized growth `100.00 → 283.43`, or cumulative `183.43%`, via `100 × ((1 + 0.1098)^10 - 1)`. Raw endpoints are not disclosed, so the implied endpoint is not a sourced NAV level.
- June factsheet NAV/index tracking observations were YTD `11.49%` vs `11.06%`, 1-year `27.47%` vs `27.59%`, 3-year `21.11%` vs `21.29%`, 5-year `12.72%` vs `12.87%`, 10-year `10.82%` vs `11.10%`, and since inception `11.22%` vs `11.53%`; these are passive implementation/fee observations, not alpha.
- As-of reconciliation: June official NAV YTD/10-year were `11.49%`/`10.82%`; the separate fund-list YTD was `18.37%` as of `2026-08-11`; later official advisor-page YTD is `19.86%` as of `2026-08-26`; July standardized rolling fields are `34.56%`/`21.47%`/`14.05%`/`10.98%`/`11.68%`. These fields are kept separate and are not mixed into one period.
- Current official benchmark YTD in the same current capture was not exposed. The current official NAV/market-price pair and official daily NAV drawdown series were also not exposed; these remain explicit gaps.

### Pre-save evidence packet and proposed durable contents

- Evidence packet records child/parent ARIs, Nasdaq identity, inception/CUSIP, passive/sampling classification, return basis, issuer/common benchmarks, candidate annual/rolling/current claims, periods, units/currency, metric definitions, as-of dates, source URLs, calculations, current portfolio facts, distribution timing, secondary price/drawdown fields, unresolved gaps and the complete planned file changes.
- Proposed `wiki/analysis/performance/ETF_NASDAQ_VYMI Performance.md`: replace the stale July page with current frontmatter; retain the official 2016† and 2017-2025 annual NAV table; add July official rolling/annualized fields and current August YTD; add annual-window and rolling-10-year implied calculations, June index tracking cross-check, current fund snapshot, country/sector/top-ten context, distribution timing, international value/dividend/FX/emerging-market risks, secondary price and drawdown proxy, as-of reconciliation, source links and follow-up gaps; retain the canonical International breadcrumb and `geography/International` tag.
- Proposed `wiki/analysis/comparisons/International ETF.md`: update only the VYMI row to official rolling 10-year `10.98%`, 2021-2025 CAGR `13.06%`, and current official YTD `19.86%`; append the dated VYMI refresh note distinguishing the 8/11 and 8/26 YTD snapshots and disclosing current NAV-pair/daily-NAV gaps.
- Proposed `wiki/analysis/performance/ETF Performance Index.md`: update the VYMI row in the preliminary holdings-group table to `10.98%`, `13.06%`, worst `-6.90%`, average positive `19.22%`, and current YTD `19.86%`; append the dated VYMI note below the existing issuer-field footnotes. The Common Window values remain unchanged because annual rows did not change.
- Proposed `raw/imports/ETF_performance_sources_2026-08-29.md`: append this VYMI identity/source map, raw claims, calculations, reconciliation, complete proposed contents, local checklist, exact scheduled-inline verification lines, and structured `trello_handoff`.
- Proposed `log.md` exact bullet: ``- `etf-performance`: Refreshed [[ETF_NASDAQ_VYMI Performance]] with official July rolling 10-year NAV TR `10.98%`, current NAV TR YTD `19.86%` as of 2026-08-26, and 2021-2025 CAGR `13.06%`; updated [[International ETF]], [[ETF Performance Index]], and [[ETF_performance_sources_2026-08-29]], while preserving the current NAV-pair and official daily drawdown gaps.`` `log.md` remains outside the scoped commit because it already contains unrelated user changes.
- No ETF entity hub or new region page is required; `NASDAQ:VYMI` remains the canonical performance owner and the existing International region page remains the sole regional navigation owner.

### Local pre-save checklist

- PASS: official Nasdaq identity, fund name, inception, passive/sampling equity eligibility, canonical key, tracked index, return basis, USD units, and International region ownership are source-mapped.
- PASS: official June factsheet, July standardized fields, separate August 11 YTD, later August 26 current YTD, secondary August 24 price and secondary drawdown data retain individual as-of dates; NAV, market price, benchmark, distribution, holdings and risk metrics are not conflated.
- PASS: official annual rows, 2017-2025 and 2021-2025 calculations, rolling-10-year implied calculation, June index tracking observations, cached S&P common reference, secondary drawdown proxy and all unresolved current NAV/daily-series gaps reproduce the proposed page/index values; no unsupported benchmark-current or NAV endpoint is inferred.
- PASS: complete proposed contents for performance, International region, index, source batch and log artifacts are specified; canonical breadcrumb/tag, source links, secondary conflicts and follow-up gaps are preserved; no unresolved High/Medium finding blocks the write and no WARNING requiring confirmation remains.
verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official Vanguard July standardized fields and current August YTD support the VYMI refresh; scheduled-local verification passed and current NAV-pair, benchmark-current, and daily drawdown gaps remain disclosed.

## DIVI — Franklin International Core Dividend Tilt Index ETF

### Identity and classification

- `workflow: check-etf-performance`; `execution_profile: scheduled-inline`; `child_card_ari: ari:cloud:trello::card/workspace/6a78536437ed0b3b544c19e1/6a9177392785e124d26c3869`; `parent_ari: ari:cloud:trello::card/workspace/6a78536437ed0b3b544c19e1/6a91760cdaae83b3d4afdc13`; input ticker `DIVI`; canonical `entity_key: NYSE Arca:DIVI`.
- Franklin identifies DIVI as the Franklin International Core Dividend Tilt Index ETF, listed on NYSE Arca, with inception `2016-06-01`. The fund is an `Indexed` passive equity ETF tracking the `Morningstar Developed Markets ex-North America Dividend Enhanced Select Index-NR`; quarterly reconstitution and permitted implementation instruments do not change the passive equity classification.
- Primary region is `International`; the durable graph is `[[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]`, with the performance page retaining `geography/International` and the entity link `[[ETF_AMEX_DIVI]]`.

### Source map and as-of dates

| Source | URL/path | Use and as-of date |
|---|---|---|
| Franklin official product/performance page | https://www.franklintempleton.com/investments/options/exchange-traded-funds/products/21412/SINGLCLASS/franklin-international-core-dividend-tilt-index-etf/DIVI?role=fp | Identity, exchange, indexed classification, official NAV TR and rolling fields as of 2026-07-31, current NAV/YTD and fund facts as of 2026-08-21/23, exposure and yield fields |
| Franklin official DIVI factsheet | https://www.franklintempleton.com/forms-literature/download/DIVI-FF | Calendar NAV and issuer-index rows for 2017-2025; factsheet/holdings context as of 2026-06-30; return definition |
| PortfoliosLab DIVI | https://portfolioslab.com/symbol/DIVI | Secondary adjusted-price-plus-distributions max-drawdown/recovery proxy, accessed 2026-08-29; not official NAV evidence |
| S&P 500 official index page and cached workflow references | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Common USD Total Return reference for complete calendar years; cached convention as of 2025-12-31, dividends reinvested |
| Existing vault context | `raw/funds/ETF_AMEX_DIVI_fund_facts.md`; `raw/imports/ETF_AMEX_DIVI_fund_source_2026-07-12.md`; `wiki/entities/ETF_AMEX_DIVI.md` | Prior identity/strategy context only; fresh performance claims use the official web sources above |

### Candidate performance claims and raw observations

- Franklin official product page reports NAV Total Return average annual performance as of `2026-07-31`: 1-year `28.73%`, 3-year `17.52%`, 5-year `13.86%`, 10-year `11.13%`, and since inception `11.18%`. Corresponding issuer-index fields are `28.63%`, `17.38%`, `13.85%`, `11.35%`, and `11.42%`; market-price fields are `28.85%`, `17.39%`, `13.74%`, `11.06%`, and `11.16%`. The saved primary 10-year field is the official NAV value `11.13%`; raw rolling endpoints are not disclosed.
- The same official page reports current NAV `USD 44.55` and NAV Total Return YTD `16.62%` as of `2026-08-21`; total net assets are `USD 2.77B` as of `2026-08-23`; gross and net expense ratio are `0.09%` as of `2026-08-01`; 30-Day SEC Yield is `3.01%` as of `2026-07-31`; distribution rate at NAV is `2.98%` as of `2026-08-21`; distributions are quarterly.
- Official Franklin exposure fields as of `2026-08-20` are Europe `59.34%`, Asia `28.58%`, Australia/New Zealand `9.13%`, North America `1.79%`, and Middle East/Africa `1.24%`. Latest complete official holdings snapshot in the reviewed materials is `417` holdings as of `2026-06-30`.
- Official factsheet calendar NAV Total Return rows are: 2017 `12.82%`, 2018 `-6.18%`, 2019 `22.66%`, 2020 `1.55%`, 2021 `17.22%`, 2022 `-1.74%`, 2023 `19.23%`, 2024 `2.36%`, and 2025 `34.51%`. The corresponding Morningstar index rows are `13.21%`, `-5.75%`, `23.21%`, `1.86%`, `17.63%`, `-1.43%`, `18.96%`, `2.28%`, and `34.32%`. Inception-year 2016 is unavailable in the reviewed calendar table and is not ranked.
- Franklin's performance definition is NAV or market-price return with all distributions reinvested and fund expenses deducted. NAV Total Return, market-price return, issuer-index return, distribution rate, and SEC yield remain separate metrics with separate as-of dates.
- Cached S&P 500 Total Return common-reference rows for 2017-2025 are 2017 `21.83%`, 2018 `-4.38%`, 2019 `31.49%`, 2020 `18.40%`, 2021 `28.71%`, 2022 `-18.11%`, 2023 `26.29%`, 2024 `25.02%`, and 2025 `17.88%`; USD, dividends reinvested, as of `2025-12-31`. This is a common reference only, not DIVI's strategy benchmark.
- PortfoliosLab secondary adjusted-price total-return evidence reports maximum drawdown `-27.76%` on `2020-03-12` and recovery in `207` trading sessions. This is a price-plus-distributions proxy; official daily NAV history sufficient to independently reproduce fund-level max drawdown, recovery, or volatility is `ไม่พบข้อมูลที่ยืนยันได้`.

### Calculations and reconciliation

- `2021-2025` DIVI NAV compound is `(1.1722 × 0.9826 × 1.1923 × 1.0236 × 1.3451) - 1 = 89.08%`; rounded-input CAGR is `(1 + 0.8908)^(1/5) - 1 = 13.59%`.
- `2021-2025` cached S&P 500 TR compound is `96.17%` and CAGR `14.43%`. The arithmetic difference is approximately `-0.84 percentage points` of CAGR; it is not labelled alpha.
- `2017-2025` DIVI NAV compound is `149.29%`; rounded-input CAGR is `10.68%`; positive/negative calendar years are `7 / 2`; best year is 2025 `+34.51%`; least positive year is 2024 `+2.36%`; worst year is 2018 `-6.18%`; least-bad down year is 2022 `-1.74%`.
- `2017-2025` cached S&P 500 TR compound is `255.78%` and CAGR `15.14%`; this remains a cross-asset/common-reference comparison and does not replace the Morningstar issuer benchmark.
- The issuer-reported rolling 10-year NAV TR CAGR `11.13%` as of `2026-07-31` is recorded as reported. No cumulative endpoint is inferred because Franklin did not expose raw start/end total-return values. If a normalized illustration is needed, it is explicitly `100 × ((1 + 0.1113)^10 - 1) = 188.77%` implied growth, not a sourced NAV endpoint; the durable page does not present it as an observed cumulative return.
- Reconciliation: July official NAV rolling 10-year is `11.13%` while current YTD NAV TR is a separate `16.62%` observation as of `2026-08-21`; no period mixing is performed. Official index and market-price rolling fields are retained only as the issuer's same-window tracking context.

### Pre-save evidence packet / proposed durable contents

- Evidence packet contains ETF identity and exchange, return basis (`NAV Total Return`), issuer benchmark, common benchmark, all candidate claims and periods, units/currency (`%`, USD), metric definitions, individual as-of dates, source URLs/paths, calculations, secondary-risk qualification, unresolved gaps, and the complete planned write set.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/performance/ETF_AMEX_DIVI Performance.md`: current frontmatter with `entity_key: NYSE Arca:DIVI`, official 2026-07-31 performance date, current YTD/NAV/facts dates, NAV TR basis and International tag; canonical breadcrumb; Thai bottom line; official 10-year NAV TR `11.13%`; official annual NAV/index/S&P rows for 2017-2025; 2021-2025 and 2017-2025 calculations; current NAV/YTD, expense, yield, assets, geography and holdings context; secondary drawdown proxy; explicit official daily-NAV/raw-endpoint gaps; source links and follow-up navigation.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/comparisons/International ETF.md`: update only the DIVI row to official rolling 10-year `11.13%`, 2021-2025 CAGR `13.59%`, and current NAV TR YTD `16.62%`; append a dated refresh note preserving the raw rolling-endpoint and official daily NAV drawdown gaps and identifying `-27.76%`/`207` sessions as secondary proxy evidence.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/performance/ETF Performance Index.md`: update the DIVI coverage row to official rolling `11.13%`, 2021-2025 CAGR `13.59%`, current YTD `16.62%`, best/worst `2025 +34.51% / 2018 -6.18%`, and explicit secondary max-drawdown/official daily-NAV gap; preserve the common-window table and International navigation links.
- Proposed content for this source batch: this DIVI identity/source map, raw observations, calculations, reconciliation, evidence packet, local checklist, and exact structured `trello_handoff` below.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/log.md`: one workflow bullet linking `[[ETF_AMEX_DIVI Performance]]`, `[[International ETF]]`, `[[ETF Performance Index]]`, and `[[ETF_performance_sources_2026-08-29]]`, stating official rolling `11.13%`, current YTD `16.62%`, 2021-2025 CAGR `13.59%`, and preserved data gaps. The file remains outside the scoped commit because it already contained unrelated user changes.
- No new ETF entity or region page is required; existing `wiki/entities/ETF_AMEX_DIVI.md` and `wiki/analysis/comparisons/International ETF.md` remain the canonical owners.

### Local pre-save checklist

- PASS: official NYSE Arca identity, fund name, inception, passive/index-tracking equity eligibility, canonical key, tracked index, return basis, USD units, and International region ownership are source-mapped.
- PASS: official July rolling fields, official calendar rows, current August NAV/YTD/fund facts, secondary drawdown proxy and cached S&P rows retain individual sources and as-of dates; NAV, market price, benchmark, distribution and yield metrics are not conflated.
- PASS: official annual rows, 2021-2025 and 2017-2025 calculations, issuer-reported 10-year field, index tracking context, and secondary drawdown proxy reproduce the proposed page/index values; no raw endpoint, current benchmark, or official daily NAV value is inferred.
- PASS: complete proposed contents for performance, International region, index, source batch and log artifacts are specified; breadcrumb/tag/source links and secondary conflict language are preserved; no unresolved High/Medium finding blocks the write and no WARNING requiring confirmation remains.
verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official Franklin July performance fields and August current YTD support the DIVI refresh; scheduled-local verification passed and raw NAV endpoints/daily drawdown gaps remain disclosed.

## GSJY — Goldman Sachs ActiveBeta Japan Equity ETF

### Identity and classification

- `workflow: check-etf-performance`; `execution_profile: scheduled-inline`; `child_card_ari: ari:cloud:trello::card/workspace/6a78536437ed0b3b544c19e1/6a91773ff338b4c1e6bad08f`; `parent_ari: ari:cloud:trello::card/workspace/6a78536437ed0b3b544c19e1/6a91760cdaae83b3d4afdc13`; input ticker `GSJY`; canonical `entity_key: NYSE Arca:GSJY`.
- Goldman Sachs identifies GSJY as the Goldman Sachs ActiveBeta Japan Equity ETF, listed on NYSE Arca, with inception `2016-03-02` and CUSIP `381430404`. The fund is an index-tracking, rules-based smart-beta equity ETF tracking the `Goldman Sachs ActiveBeta Japan Equity Index`.
- The official summary prospectus states that the fund `is not actively managed`; the ActiveBeta methodology uses value, momentum, quality and low-volatility factors and is reconstituted/rebalanced quarterly. This remains eligible passive equity ETF performance work; the word ActiveBeta does not make it an active long-only fund.
- Primary region is `Japan`; the durable graph is `[[ETF Region Index]] → [[Japan ETF]] → [[ETF Performance Index]]`, with the performance page retaining `geography/Japan`.

### Source map and as-of dates

| Source | URL/path | Use and as-of date |
|---|---|---|
| Goldman Sachs official factsheet/performance PDF | https://am.gs.com/public-assets/documents/5747f795-24d6-11ef-870d-ed3a247c783e | July 2026 standardized NAV, market-price, ActiveBeta-index and MSCI Japan reference returns; fund facts, holdings, sector weights, yield and expense data as of 2026-07-31 |
| Goldman Sachs official fund page | https://am.gs.com/en-us/individual/funds/detail/PV102393/381430404/goldman-sachs-active-beta-japan-equity-etf | Fund identity, CUSIP, listing and issuer strategy/document discovery |
| Goldman Sachs official summary prospectus | https://am.gs.com/public-assets/documents/179d857b-24e3-11ef-ad18-377468fbef87?view=true | Objective, passive/not-actively-managed classification, index methodology and risks; December 2025 document |
| S&P 500 official index page and cached workflow references | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Common USD Total Return reference for complete calendar years; cached convention as of 2025-12-31, dividends reinvested |
| Existing vault context | `wiki/analysis/performance/ETF_NYSE_ARCA_GSJY Performance.md`; `wiki/analysis/comparisons/Japan ETF.md` | Prior rows and page structure; fresh July official fields replace stale June values |

### Candidate performance claims and raw observations

- Official Goldman Sachs factsheet reports NAV Total Return as of `2026-07-31`: 1-month `2.42%`, YTD `15.60%`, 1-year `31.15%`, 3-year annualized `17.33%`, 5-year annualized `9.83%`, 10-year annualized `9.01%`, and since inception annualized `9.50%`. The 10-year field covers `10.00` elapsed years from 2016-07-31 to 2026-07-31.
- Same-window market-price fields are `1.03%`, `14.27%`, `30.33%`, `16.95%`, `9.50%`, `9.20%`, and `9.41%`; they remain separate from NAV Total Return and are not used as the canonical return basis.
- Same-window issuer ActiveBeta Japan Index fields are `2.46%`, `15.65%`, `31.23%`, `17.37%`, `9.81%`, `8.90%`, and `9.38%`; MSCI Japan - USD (Net) reference fields are `1.03%`, `16.96%`, `32.28%`, `17.70%`, `9.99%`, `9.26%`, and `9.79%`. The ActiveBeta series is the issuer benchmark; MSCI Japan is a separate reference universe.
- Official calendar NAV rows are: 2017 `24.52%`, 2018 `-10.52%`, 2019 `18.28%`, 2020 `12.52%`, 2021 `0.60%`, 2022 `-15.60%`, 2023 `18.92%`, 2024 `9.09%`, and 2025 `25.07%`. Corresponding ActiveBeta Japan Index rows are `23.99%`, `-12.88%`, `19.61%`, `14.44%`, `1.71%`, `-16.65%`, `20.32%`, `8.28%`, and `24.60%`. 2016 is an inception-year partial and is not treated as a complete calendar row.
- Official fund facts as of `2026-07-31` include `155` holdings, net assets `USD 85.21M`, weighted average market cap `USD 83.95B`, P/E `17.70x`, P/B `1.86x`, ROE `12.00%`, dividend yield `2.00%`, 30-Day SEC Yield `1.42%`, total expense ratio `0.25%`, and quarterly distribution frequency.
- Official sector weights as of `2026-07-31` are Industrials `24.6%`, Financials `20.5%`, Information Technology `17.1%`, Consumer Discretionary `15.2%`, Health Care `4.7%`, Communication Services `4.5%`, Materials `4.1%`, Energy `3.2%`, Consumer Staples `3.2%`, Utilities `1.5%`, Real Estate `1.2%`, and Cash `0.2%`. Top holdings include Mitsubishi UFJ Financial Group `4.5%`, Advantest `3.6%`, Tokyo Electron `3.0%`, Toyota `3.0%`, Hitachi `2.8%`, and Sumitomo Mitsui Financial Group `2.6%`.
- Goldman Sachs' performance convention reflects reinvested distributions; NAV calculations assume management fees and operating expenses. Official daily NAV history sufficient to independently reproduce max drawdown, recovery, or volatility is `ไม่พบข้อมูลที่ยืนยันได้`.
- Cached S&P 500 Total Return common-reference rows for 2017-2025 are 2017 `21.83%`, 2018 `-4.38%`, 2019 `31.49%`, 2020 `18.40%`, 2021 `28.71%`, 2022 `-18.11%`, 2023 `26.29%`, 2024 `25.02%`, and 2025 `17.88%`; USD, dividends reinvested, as of `2025-12-31`. These rows are not GSJY's strategy benchmark.

### Calculations and reconciliation

- `2021-2025` GSJY NAV compound is `(1.0060 × 0.8440 × 1.1892 × 1.0909 × 1.2507) - 1 = 37.76%`; rounded-input CAGR is `(1 + 0.3776)^(1/5) - 1 = 6.62%`; positive / negative years are `3 / 2`.
- `2017-2025` GSJY NAV compound is `(1.2452 × 0.8948 × 1.1828 × 1.1252 × 1.0060 × 0.8440 × 1.1892 × 1.0909 × 1.2507) - 1 = 104.29%`; rounded-input CAGR is `8.26%`; positive / negative years are `6 / 3`.
- Best complete year is 2017 `+24.52%`; least positive is 2021 `+0.60%`; worst is 2022 `-15.60%`; least-bad down year is 2018 `-10.52%`.
- Cached S&P 500 TR common reference is cumulative `96.17%` / CAGR `14.43%` for 2021-2025 and `255.78%` / CAGR `15.14%` for 2017-2025. No arithmetic difference is called alpha.
- The issuer-reported rolling 10-year NAV TR CAGR `9.01%` implies normalized growth `100.00 → 236.95`, or `136.95%` cumulative implied growth, via `100 × ((1 + 0.0901)^10 - 1)`. Raw NAV endpoints are not disclosed, so this is not an observed cumulative return.
- Same-window tracking context: GSJY NAV is `-0.05 pp` below the ActiveBeta index YTD, `-0.08 pp` below over 1 year, and `+0.11 pp` above over 10 years. These differences are implementation/expense observations, not manager alpha.
- Reconciliation: the prior June snapshot was NAV YTD `12.86%` and rolling 10-year `9.29%`; the newer official July month-end snapshot is NAV YTD `15.60%` and rolling 10-year `9.01%`. The page uses the newer July fields and does not mix as-of dates.

### Pre-save evidence packet / proposed durable contents

- Evidence packet contains ETF identity and exchange, return basis (`NAV Total Return`), issuer/common benchmarks, classification, all candidate rolling/current/annual claims, periods, units/currency (`%`, USD), metric definitions, individual as-of dates, source URLs/paths, calculations, risk fields, unresolved gaps and complete planned file changes.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/performance/ETF_NYSE_ARCA_GSJY Performance.md`: replace the stale June page with updated July frontmatter; retain the canonical Japan breadcrumb and tag; add official July standardized NAV/market-price/index/MSCI table; retain official 2017-2025 annual NAV/index/S&P rows; update rolling 10-year `9.01%`, YTD `15.60%`, normalized implied calculation, 2021-2025 CAGR `6.62%`, best/worst years, current July fund facts, sector/top-holding context, passive/not-actively-managed risk language, source links and official daily-NAV gap.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/comparisons/Japan ETF.md`: update the primary GSJY row to `9.01% | 6.62% | 15.60%`; append a 2026-08-29 verified refresh note distinguishing the July month-end fields from the stale June snapshot and preserving raw-endpoint/daily-NAV gaps. The older 2026-07-23 coverage-addition row remains historical context.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/performance/ETF Performance Index.md`: update the GSJY coverage row to official rolling `9.01%`, 2021-2025 CAGR `6.62%`, YTD `15.60%`, best/worst `2017 +24.52% / 2022 -15.60%`, and explicit official daily NAV gap; append the dated GSJY refresh entry while leaving the unchanged Common Window annual row intact.
- Proposed content for this source batch: this GSJY identity/source map, raw observations, calculations, reconciliation, evidence packet, local checklist and exact structured `trello_handoff` below.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/log.md`: one workflow bullet linking `[[ETF_NYSE_ARCA_GSJY Performance]]`, `[[Japan ETF]]`, `[[ETF Performance Index]]`, and `[[ETF_performance_sources_2026-08-29]]`, stating official July rolling `9.01%`, YTD `15.60%`, and 2021-2025 CAGR `6.62%`; preserve the existing unrelated log modification outside the scoped commit.
- No new ETF entity or region page is required; the existing `Japan ETF` region page is the sole regional navigation owner.

### Local pre-save checklist

- PASS: official NYSE Arca identity, fund name, inception/CUSIP, passive/index-tracking equity eligibility, canonical key, tracked index, return basis, USD units and Japan region ownership are source-mapped.
- PASS: official July standardized NAV, market price, issuer index, MSCI reference, annual rows, fund facts and sector/holding snapshot retain individual metric definitions and as-of dates; no price/NAV or benchmark/current field is conflated.
- PASS: official annual rows, 2021-2025 and 2017-2025 calculations, rolling-10-year issuer field, normalized implied calculation, tracking differences, cached S&P reference and explicit daily-NAV gap reproduce the proposed page/index values; no raw endpoint or official drawdown is inferred.
- PASS: complete proposed contents for performance, Japan region, index, source batch and log artifacts are specified; canonical breadcrumb/tag/source links and passive smart-beta classification are preserved; no unresolved High/Medium finding blocks the write and no WARNING requiring confirmation remains.
verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official Goldman Sachs July standardized performance and fund facts support the GSJY refresh; scheduled-local verification passed and raw NAV endpoints/official daily drawdown gaps remain disclosed.

## SPEU — State Street SPDR Portfolio Europe ETF

### Identity and classification

- `workflow: check-etf-performance`; `execution_profile: scheduled-inline`; `child_card_ari: ari:cloud:trello::card/workspace/6a78536437ed0b3b544c19e1/6a917744ecbb2ebeae8cc910`; `parent_ari: ari:cloud:trello::card/workspace/6a78536437ed0b3b544c19e1/6a91760cdaae83b3d4afdc13`; input ticker `SPEU`; canonical `entity_key: NYSE Arca:SPEU`.
- State Street identifies SPEU as the State Street SPDR Portfolio Europe ETF, listed on NYSE Arca, with inception `2002-10-15`, CUSIP `78463X103`, ISIN `US78463X1037`, base currency USD, and quarterly distributions. It is a passive/index-tracking equity ETF that uses sampling to seek the `STOXX Europe Total Market Index` across Western Europe and market-cap segments.
- State Street's linked benchmark history uses STOXX Europe 50 from inception through `2019-09-22` and STOXX Europe Total Market Index from `2019-09-23` onward. This is preserved as a benchmark-history break, not silently treated as one unchanged series. Primary region is `Europe`; the durable graph is `[[ETF Region Index]] → [[Europe ETF]] → [[ETF Performance Index]]`.

### Source map and as-of dates

| Source | URL/path | Use and as-of date |
|---|---|---|
| State Street official product page | https://www.ssga.com/us/en/individual/etfs/state-street-spdr-portfolio-europe-etf-speu | Identity, listing, inception, benchmark-history change, official rolling performance, holdings/sector/country facts and current NAV/AUM captures |
| State Street official factsheet | https://www.ssga.com/library-content/products/factsheets/etfs/us/factsheet-us-en-speu.pdf | Official June 2026 NAV/benchmark table, fee, holdings, country/sector facts and return definitions; as of 2026-06-30 |
| FinanceCharts SPEU total-return history | https://www.financecharts.com/stocks/SPEU/performance/total-return | Secondary dividend-reinvested calendar proxy; direct page was captcha-gated during this run, so existing dated proxy rows are retained and marked `*` |
| Existing prior source batch | `raw/imports/ETF_performance_sources_2026-08-19.md` | Source path and prior evidence for the marked 2021-2025 secondary rows; no issuer calendar rows were available in that review |
| S&P 500 official index page and cached workflow references | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Common USD Total Return reference for complete calendar years; cached convention as of 2025-12-31, dividends reinvested |

### Candidate performance claims and raw observations

- State Street's latest official July standardized performance table reports NAV Total Return as of `2026-07-31`: 1-month `2.02%`, QTD `2.02%`, YTD `9.45%`, 1-year `22.02%`, 3-year annualized `15.87%`, 5-year annualized `9.09%`, 10-year annualized `9.65%`, and since inception `6.96%`.
- Same-window market-value fields are `2.20%`, `2.20%`, `9.90%`, `22.89%`, `16.01%`, `9.07%`, `9.69%`, and `6.97%`; linked benchmark fields are `2.02%`, `2.02%`, `9.23%`, `21.79%`, `15.63%`, `8.83%`, `9.52%`, and `6.93%`. All fund results assume reinvestment of dividends/capital gains and are net of fees; index returns are unmanaged.
- A later official product-page search capture reports NAV `US$57.41`, shares outstanding `13.00M`, and AUM `US$746.35M` as of `2026-08-26`. The full official page capture used for portfolio context separately reports NAV `US$54.97` and AUM `US$714.59M` as of `2026-07-17`; the later NAV/AUM is used for current context and the date discrepancy is disclosed rather than mixed.
- Official product/fund facts as of `2026-07-17` to `2026-07-21` include gross expense ratio `0.07%`, 30-Day SEC Yield `2.43%`, fund distribution yield `3.44%`, index dividend yield `2.93%`, holdings `1,684`, P/B `2.27x`, P/E FY1 `15.19x`, weighted average market cap `US$126,168.53M`, and 30-day median bid/ask spread `0.04%`. The product page reports the listing details and quarterly distribution frequency as of 2026-07-21.
- Official portfolio context as of `2026-07-17` reports top country weights United Kingdom `21.99%`, France `14.75%`, Switzerland `13.96%`, Germany `12.72%`, Netherlands `8.30%`, Sweden `6.06%`, Spain `5.76%`, and Italy `5.68%`; sector weights Financials `25.00%`, Industrials `19.24%`, Health Care `12.34%`, Information Technology `8.46%`, Consumer Staples `8.14%`, Consumer Discretionary `7.19%`, Materials `5.42%`, Energy `5.07%`, Utilities `4.73%`, Communication Services `2.93%`, and Real Estate `1.48%`.
- State Street's reviewed official capture did not publish complete calendar-year NAV rows. Retained FinanceCharts secondary dividend-reinvested proxy rows are 2021 `16.20%*`, 2022 `-15.97%*`, 2023 `19.84%*`, 2024 `1.94%*`, and 2025 `35.80%*`; the proxy is not issuer NAV evidence and direct page access was captcha-gated in this run.
- Cached S&P 500 Total Return common-reference rows for 2021-2025 are `28.71%`, `-18.11%`, `26.29%`, `25.02%`, and `17.88%`; USD, dividends reinvested, as of `2025-12-31`. This is a common reference only, not SPEU's strategy benchmark.
- Official daily NAV history sufficient to independently reproduce max drawdown, recovery, or volatility is `ไม่พบข้อมูลที่ยืนยันได้`.

### Calculations and reconciliation

- Secondary proxy 2021-2025 compounds to `61.99%*` and rounded-input CAGR `10.13%*`; positive/negative years are `4 / 1`; best proxy year is 2025 `+35.80%*`; least positive is 2024 `+1.94%*`; worst/least-bad down year is 2022 `-15.97%*`; population standard deviation is `17.48%*`.
- Cached S&P 500 TR compounds to `96.17%` / CAGR `14.43%` over 2021-2025. No direct fund-minus-index or manager-skill claim is made from the secondary proxy.
- Official rolling NAV TR `9.65%` as of 2026-07-31 is kept separate from the secondary calendar proxy `10.13%*`. Normalized growth from the official annualized field would be `100.00 → 251.24`, or `151.24%` implied cumulative growth via `100 × ((1 + 0.0965)^10 - 1)`; raw endpoints are not disclosed, so this is not an observed cumulative return.
- Official linked benchmark tracking differences for July are NAV minus index: YTD `+0.22 pp`, 1Y `+0.23 pp`, 3Y `+0.24 pp`, 5Y `+0.26 pp`, 10Y `+0.26 pp`, and since inception `+0.03 pp`; these are passive implementation observations, not alpha.
- Reconciliation: the prior June official fields were NAV YTD `7.29%` and rolling 10-year `9.76%`; the newer July official fields are NAV YTD `9.45%` and rolling 10-year `9.65%`. The page uses the newer July performance window, while current NAV/AUM and portfolio characteristics retain their own as-of dates.

### Pre-save evidence packet / proposed durable contents

- Evidence packet contains ETF identity and exchange, return basis (`NAV Total Return`, USD, dividends/capital gains reinvested, net of fees), issuer benchmark and linked-history break, common benchmark, candidate official/secondary claims, periods, units/currency, metric definitions, individual as-of dates, source URLs/paths, calculations, source-quality choice, unresolved gaps and complete planned file changes.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/performance/ETF_NYSE_ARCA_SPEU Performance.md`: replace the stale June page with July official rolling NAV/market-value/benchmark table; update official 10-year `9.65%`, YTD `9.45%`, current NAV/AUM, fee/yield/holdings/country/sector facts with their as-of dates; retain the 2021-2025 secondary proxy table marked `*`; correct the benchmark-history change to 2019-09-23; add tracking differences, source-quality/captcha note, current price/NAV gap and official daily-NAV drawdown gap; preserve Europe breadcrumb/tag.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/comparisons/Europe ETF.md`: update only the SPEU row to `9.65% | 10.13%* | 9.45%`; append a dated refresh note with the July official fields, later Aug-26 NAV/AUM, benchmark-history date, secondary annual proxy marker and daily-NAV gap.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/performance/ETF Performance Index.md`: update the SPEU coverage row to official rolling `9.65%`, secondary 2021-2025 CAGR `10.13%*`, YTD `9.45%`, and explicit current NAV-pair/daily-NAV gaps; correct linked benchmark change to 2019-09-23; update the dated refresh bullet. The Common Window row remains unchanged because its annual rows are secondary.
- Proposed content for this source batch: this SPEU identity/source map, raw observations, calculations, reconciliation, complete proposed contents, local checklist and exact structured `trello_handoff` below.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/log.md`: one workflow bullet linking `[[ETF_NYSE_ARCA_SPEU Performance]]`, `[[Europe ETF]]`, `[[ETF Performance Index]]`, and `[[ETF_performance_sources_2026-08-29]]`, stating official July rolling `9.65%`, YTD `9.45%`, retained secondary CAGR `10.13%*`, and corrected 2019-09-23 benchmark change; preserve unrelated prior log changes outside the scoped commit.
- No new ETF entity or region page is required; the existing Europe region page remains the sole regional navigation owner.

### Local pre-save checklist

- PASS: official NYSE Arca identity, identifiers, inception, passive/sampling equity eligibility, canonical key, STOXX benchmark, linked benchmark-history change, return basis, USD units and Europe region ownership are source-mapped.
- PASS: official July NAV/market-value/benchmark fields, current NAV/AUM capture, July portfolio facts, secondary annual proxy, cached S&P reference and each as-of date remain separate; the old-versus-new official captures are reconciled and disclosed.
- PASS: secondary annual rows are marked `*`, direct FinanceCharts captcha limitation is preserved, no secondary row overrides official rolling NAV fields, tracking differences are not called alpha, and no official daily NAV drawdown is inferred.
- PASS: complete proposed contents for performance, Europe region, index, source batch and log artifacts are specified; canonical breadcrumb/tag/source links and benchmark-history correction are preserved; no unresolved High/Medium finding blocks the write and no WARNING requiring confirmation remains.
verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official State Street July performance and current product data support the SPEU refresh; scheduled-local verification passed, secondary annual rows remain marked, and source/as-of and official daily NAV gaps are disclosed.

## KWEB — KraneShares CSI China Internet ETF

### Workflow identity and scope

- `workflow: check-etf-performance`; `execution_profile: scheduled-inline`; `child_card_ari: ari:cloud:trello::card/workspace/6a78536437ed0b3b544c19e1/6a917749032483b31141e900`; `parent_ari: ari:cloud:trello::card/workspace/6a78536437ed0b3b544c19e1/6a91760cdaae83b3d4afdc13`; input ticker `KWEB`; canonical `entity_key: NYSE Arca:KWEB`.
- Card was claimed and reread as `In Progress` before research. The card ticker resolves to the US-listed KraneShares CSI China Internet ETF. It is not the separate UCITS USD share class shown as `LSE:KWEB` / OTC alias `KRANF`.
- Primary region is `China`; the durable graph is `[[ETF Region Index]] → [[China ETF]] → [[ETF Performance Index]]`. Only `wiki/analysis/performance/ETF_NYSE_ARCA_KWEB Performance.md` is refreshed; `wiki/analysis/performance/ETF_LSE_KWEB Performance.md` is not changed.

### Source map and as-of dates

| Source | URL/path | Use and as-of date |
|---|---|---|
| KraneShares official US product page | https://kraneshares.com/etf/kweb/ | US identity, NYSE ticker, CUSIP/ISIN, inception, fee, index, NAV/market price, premium/discount, standardized performance, holdings and listed-location breakdown; performance as of 2026-07-31, fund facts/current pair as of 2026-08-28, spread as of 2026-08-27 |
| KraneShares official US factsheet | https://kraneshares.com/resources/factsheet/kweb_factsheet.pdf | Official fund-document and return-basis cross-reference; used with the current product page rather than to overwrite newer product-page fields |
| Total Real Returns KWEB | https://totalrealreturns.com/n/KWEB | Secondary dividend-reinvested market-price/adjusted-return proxy, annual rows, current YTD and drawdown; data ending 2026-08-28 |
| Stock Analysis KWEB history | https://stockanalysis.com/etf/kweb/history/ | Secondary market-price history cross-check; not used to replace official NAV TR |
| KraneShares official UCITS page | https://kraneshares.eu/etf/kwebln/ | Distinct UCITS identity: USD class `LSE:KWEB`, ISIN `IE00BFXR7892`, inception 2018-11-21, accumulating, expense 0.75%; used only for ticker/share-class disambiguation |
| S&P 500 official index page and cached workflow references | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Common USD Total Return reference for complete calendar years; cached convention as of 2025-12-31, dividends reinvested |
| Existing vault context | `wiki/analysis/performance/ETF_NYSE_ARCA_KWEB Performance.md`, `wiki/analysis/comparisons/China ETF.md`, `wiki/analysis/performance/ETF Performance Index.md` | Prior stale official June fields, page structure, region ownership, annual proxy rows and link graph |

### Identity and classification evidence

- KraneShares identifies the US fund as `KraneShares CSI China Internet ETF`, ticker `KWEB`, primary exchange `NYSE`, CUSIP `500767306`, ISIN `US5007673065`, inception `2013-07-31`, total annual fund operating expense `0.69%`, annual distributions, and underlying index `CSI Overseas China Internet Index`; these fund details are as of 2026-08-28.
- The fund is passive/index-tracking equity exposure. The official product page describes exposure to Chinese internet companies, e-commerce and technology themes; no active-management evidence is used.
- The vault canonical exchange-qualified key remains `NYSE Arca:KWEB` because the existing US performance owner and region/index links use the NYSE Arca convention. The issuer's wording that KWEB trades on the NYSE is retained in the performance page.

### Candidate performance claims and raw observations

- Official KraneShares cumulative NAV / closing-price / linked-index returns as of 2026-07-31 are: 1M `15.90% / 16.43% / 15.91%`; 3M `-0.14% / -0.97% / -0.27%`; 6M `-21.20% / -19.47% / -21.67%`; YTD `-17.66% / -16.33% / -18.18%`; since inception `44.81% / 46.20% / 45.05%`.
- Official annualized NAV / closing-price / linked-index returns as of month-end 2026-07-31 are: 1Y `-15.45% / -14.76% / -15.89%`; 3Y `-0.04% / -0.20% / -0.65%`; 5Y `-7.75% / -7.50% / -7.97%`; 10Y `0.22% / 0.29% / 0.20%`; since inception `2.89% / 2.96% / 2.90%`.
- Official daily/current fields as of 2026-08-28: NAV `US$26.30`, NAV daily change `+0.11%`, market price `US$26.32`, market-price daily change `+0.84%`, premium/discount `US$0.02`, net assets `US$5,193,762,658`, shares outstanding `197,500,000`, fee `0.69%`; 30-day median bid/ask spread `0.04%` as of 2026-08-27.
- Official holdings as of 2026-08-28: Tencent `10.23%`, Alibaba `8.58%`, PDD `8.38%`, Meituan `7.11%`, NetEase `6.20%`, Lenovo `4.99%`, KE Holdings `4.42%`, JD.com `3.85%`, Trip.com `3.68%`, and Baidu `3.34%`; top five sum calculation is `10.23 + 8.58 + 8.38 + 7.11 + 6.20 = 40.50%`.
- Official listed-location breakdown as of 2026-08-28 is Hong Kong `76.9%`, US ADRs with no secondary HK listing `12.2%`, and US ADRs with a secondary HK listing `10.8%`.
- Secondary Total Real Returns data ending 2026-08-28 reports total-return proxy YTD `-22.70%`, trailing one-year `-25.60%`, since 2013-08-01 cumulative `+28.82%` / annualized `+1.96%`, current drawdown `-69.56%` from the 2021-02-17 peak, and worst drawdown `-80.92%` to 2022-10-24. It cautions that its calculations are educational and may be incomplete; these are not official NAV drawdown fields.
- Secondary annual dividend-reinvested proxy rows retained from the existing verified source context are: 2016 `-8.54%`, 2017 `+69.73%`, 2018 `-33.80%`, 2019 `+29.92%`, 2020 `+58.23%`, 2021 `-49.01%`, 2022 `-17.24%`, 2023 `-9.06%`, 2024 `+12.01%`, 2025 `+23.55%`. They remain marked `*` and are not issuer-published NAV TR.
- Cached S&P 500 Total Return common-reference rows are 2016 `11.96%`, 2017 `21.83%`, 2018 `-4.38%`, 2019 `31.49%`, 2020 `18.40%`, 2021 `28.71%`, 2022 `-18.11%`, 2023 `26.29%`, 2024 `25.02%`, and 2025 `17.88%`; USD, dividends reinvested, as of 2025-12-31. The S&P series is not KWEB's strategy benchmark.

### Calculations and reconciliation

- Official tracking observations calculated as NAV minus linked index are YTD `-17.66 - (-18.18) = +0.52 pp`, 1Y `+0.44 pp`, 3Y `+0.61 pp`, 5Y `+0.22 pp`, 10Y `+0.02 pp`, and since inception `-0.01 pp`. These are implementation/expense observations and are not called alpha.
- Secondary 2016-2025 proxy compounds to `12.19%*` and rounded-input CAGR `1.16%*`; positive/negative years `5 / 5`; best `2017 +69.73%*`; worst `2021 -49.01%*`.
- Secondary 2021-2025 proxy compounds to `-46.89%*` and rounded-input CAGR `-11.89%*`; positive/negative years `2 / 3`. Cached S&P 500 TR compounds to `96.17%` / CAGR `14.43%` over the same window.
- Official rolling 10-year NAV TR `0.22%` annualized is a separate issuer field from the secondary 2021-2025 proxy CAGR `-11.89%*`; the fields have different windows, bases and source quality. Raw official NAV endpoints for the rolling field are not disclosed.
- Reconciliation: the prior page used official June quarter-end YTD `-28.96%` and rolling 10Y `-0.85%`; the current official July month-end fields are YTD `-17.66%` and rolling 10Y `0.22%`. Current NAV/price is a separate 2026-08-28 observation and is not mixed with July standardized returns.

### Source-quality choice and unresolved gaps

- Official KraneShares product-page performance is the canonical source for rolling NAV TR, current official YTD, NAV/price, fee and index tracking fields. Secondary annual rows are retained because a complete official 2016-2025 calendar NAV series was not exposed in the reviewed current page; every such row and derived CAGR is marked `*`.
- Secondary drawdown/current-YTD values are preserved as context only. Official daily NAV history sufficient to reproduce drawdown, recovery date and volatility is `ไม่พบข้อมูลที่ยืนยันได้`.
- No current material price/NAV dislocation is evidenced: the issuer reports a `US$0.02` premium/discount on 2026-08-28. This is not an inference about future performance.
- The distinct LSE/UCITS KWEB page reports a different ISIN, inception, fee, NAV and accumulating share class. It is deliberately excluded from the US page and from this card's result.

### Pre-save evidence packet / proposed durable contents

- Evidence packet includes ETF identity and exchange convention, US ISIN/CUSIP, passive equity classification, return basis (`NAV Total Return`, USD, distributions reinvested, net of expenses), issuer tracked index, S&P common reference, official and secondary candidate claims, periods, units/currency, metric definitions, as-of dates, calculations, source URLs/paths, source-quality choice, unresolved gaps and the full planned file set.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/performance/ETF_NYSE_ARCA_KWEB Performance.md`: replace the stale June/July-17 snapshot with official July standardized NAV/price/index tables; set rolling 10Y `0.22%`, YTD `-17.66%`, current NAV `US$26.30`, price `US$26.32`, premium/discount `US$0.02`, AUM `US$5.19B`, fee `0.69%`; retain marked secondary 2016-2025 rows and calculations; add current holdings/listed-location and secondary drawdown caveats; preserve the China breadcrumb/tag, source links and distinct LSE/UCITS disambiguation.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/comparisons/China ETF.md`: update only the US KWEB snapshot row to `0.22% | -11.89%* | -17.66%`; append a 2026-08-29 refresh note with July official performance, Aug-28 current pair/AUM, secondary annual-row caveat and US-versus-LSE share-class separation. Leave the separate `KRANF / KWEB` UCITS row unchanged.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/performance/ETF Performance Index.md`: update the US KWEB coverage row to official rolling `0.22%`, secondary 2021-2025 CAGR `-11.89%*`, YTD `-17.66%`, best/worst proxy years and drawdown/share-class caveats; append a dated KWEB reconciliation note; leave the Common Window annual proxy row unchanged because no calendar proxy values changed.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/log.md`: append one `etf-performance` workflow bullet linking `[[ETF_NYSE_ARCA_KWEB Performance]]`, `[[China ETF]]`, `[[ETF Performance Index]]` and `[[ETF_performance_sources_2026-08-29]]`, stating official rolling `0.22%`, YTD `-17.66%`, retained secondary CAGR `-11.89%*`, and the LSE share-class separation; preserve unrelated pre-existing log changes outside the scoped commit.
- This source batch section itself is part of the proposed durable write and records the complete evidence packet, checklist and structured handoff.

### Local pre-save checklist

- PASS: official US KWEB identity, NYSE/NYSE Arca canonical key, CUSIP/ISIN, inception, passive/index-tracking equity eligibility, tracked index, USD return basis, China region ownership and distinct LSE UCITS identity are source-mapped.
- PASS: official July NAV/price/index tables, official Aug-28 current NAV/price/AUM/holdings/location fields, secondary annual proxy, secondary drawdown, cached S&P reference and every as-of date remain separate; no current field is conflated with the July standardized window.
- PASS: annual rows and both CAGR calculations reproduce the proposed page/index values; official rolling NAV is not replaced by secondary proxy; tracking differences are labeled implementation observations rather than alpha; official daily NAV drawdown/recovery remains an explicit gap.
- PASS: complete proposed contents for US performance page, China region snapshot, master index, source batch and log are specified; canonical breadcrumb/tag/source links are preserved; LSE/UCITS KWEB is not overwritten; no unresolved High/Medium finding blocks the write and no WARNING requiring confirmation remains.
verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official KraneShares July standardized performance and Aug-28 US fund data support the KWEB refresh; scheduled-local verification passed, secondary calendar/drawdown data remain marked, and US/LSE share-class and official daily-NAV gaps are disclosed.

## DBEU — Xtrackers MSCI Europe Hedged Equity ETF

### Workflow identity and scope

- `workflow: check-etf-performance`; `execution_profile: scheduled-inline`; `child_card_ari: ari:cloud:trello::card/workspace/6a78536437ed0b3b544c19e1/6a91774fa415f5e69597f27e`; `parent_ari: ari:cloud:trello::card/workspace/6a78536437ed0b3b544c19e1/6a91760cdaae83b3d4afdc13`; input ticker `DBEU`; canonical `entity_key: NYSE Arca:DBEU`.
- Card was claimed and reread as `In Progress` before research. Primary region is `Europe`; the durable graph is `[[ETF Region Index]] → [[Europe ETF]] → [[ETF Performance Index]]`.
- This refresh does not create an entity page or normalized fund table. It updates the existing DBEU performance owner, Europe navigation snapshot, master performance index, source batch and one log bullet.

### Source map and as-of dates

| Source | URL/path | Use and as-of date |
|---|---|---|
| DWS official DBEU factsheet | https://etf.dws.com/download/asset/b2d0199b-0bfc-4ed0-866b-24f31967f463 | Official identity, passive objective, MSCI Europe USD-hedged benchmark, standardized NAV/market/index returns, fund facts, holdings, countries, sectors, yield and beta; Q2 factsheet as of 2026-06-30 |
| SEC DBEU summary prospectus | https://www.sec.gov/Archives/edgar/data/1503123/000008805325000878/k100125dbeu.htm | Official NYSE Arca identity, indexing method, 80% policy and principal risks; October 2025 |
| AAII DBEU performance page | https://www.aaii.com/etf/ticker/DBEU | Secondary rounded NAV/price trailing and annual rows, July YTD, current price/assets, portfolio and risk cross-check; data as of 2026-07-31 to 2026-08-27 where stated |
| DWS currency-hedged ETF overview | https://etf.dws.com/en-us/etf-knowledge/focus-topics-etf-investment-strategies/currency-hedged-etfs-mitigating-currency-risks-from-international-equities/ | Official currency-hedge structure and 0.45% expense cross-reference |
| S&P 500 official index page and cached workflow references | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Common USD Total Return reference for complete calendar years; cached convention as of 2025-12-31, dividends reinvested |
| Existing vault context | `wiki/analysis/performance/ETF_NYSE_ARCA_DBEU Performance.md`, `wiki/analysis/comparisons/Europe ETF.md`, `wiki/analysis/performance/ETF Performance Index.md`, `raw/imports/ETF_performance_sources_2026-08-19.md` | Prior official June fields, secondary annual rows, page structure, region ownership and unresolved source gaps |

### Identity and classification evidence

- DWS identifies DBEU as `Xtrackers MSCI Europe Hedged Equity ETF`, NYSE ticker `DBEU`, CUSIP `233051853`, inception `2013-09-30`, 410 holdings and net assets `US$758,183,774.79` as of 2026-06-30; gross and net expense ratio are `0.45%`.
- Classification is `passive-index-tracking`; the SEC prospectus describes a passive/indexing approach, with at least 80% of total assets in component securities of the underlying index and representative sampling permitted where direct acquisition is not practicable.
- Tracked index is `MSCI Europe US Dollar Hedged Index`; DWS describes one-month forward contracts that hedge the developed-Europe exposure to USD. The common comparison benchmark is S&P 500 Total Return and is not the fund's strategy benchmark.
- Primary region is Europe and canonical tag is `geography/Europe`.

### Candidate performance claims and raw observations

- Official DWS Q2 standardized returns as of 2026-06-30 (NAV / market price / hedged index / parent MSCI Europe) are: 3M `11.97% / 10.67% / 11.87% / 10.93%`; 1Y `24.03% / 24.31% / 24.16% / 18.64%`; 3Y annualized `16.02% / 16.08% / 16.25% / 16.18%`; 5Y annualized `12.03% / 12.02% / 12.18% / 9.50%`; 10Y annualized `11.58% / 11.52% / 11.82% / 9.92%`; since inception annualized `9.90% / 9.92% / 10.15% / 7.11%`.
- Official DWS facts as of 2026-06-30 include SEC 30-day yield `2.11%`, beta `0.73`, 397 index constituents across 15 countries, and 410 fund holdings. Top countries: UK `20.08%`, Switzerland `14.86%`, France `14.29%`, Germany `13.10%`, Netherlands `10.57%`, Spain `5.97%`, Italy `4.88%`, Sweden `4.57%`, Denmark `2.54%`, cash `1.94%`.
- Official DWS sector weights as of 2026-06-30: Financials `23.71%`, Industrials `17.59%`, Health Care `12.46%`, Information Technology `9.84%`, Consumer Staples `8.29%`, Consumer Discretionary `6.42%`, Energy `5.30%`, Materials `5.11%`, Utilities `4.86%`, Communication Services `3.48%`, Real Estate `0.62%`, cash `1.94%`, other `0.37%`.
- Official DWS top holdings as of 2026-06-30 include ASML `5.25%`, HSBC `2.24%`, Roche `1.99%`, Novartis `1.97%`, AstraZeneca `1.94%`, Nestle `1.82%`, Siemens `1.64%`, Shell `1.50%`, Banco Santander `1.36%`, and Allianz `1.24%`.
- Latest secondary AAII trailing table as of 2026-07-31 reports NAV proxy 1M `1.0%`, 3M `7.7%`, YTD `12.6%`, 1Y `23.9%`, 3Y annualized `15.8%`, 5Y annualized `11.9%`, and 10Y annualized `11.2%`; price proxy is `0.6%`, `7.1%`, `13.0%`, `24.1%`, `15.7%`, `11.9%`, and `11.2%`, respectively.
- The same secondary source reports market price `$54.80` as of 2026-08-27, share-class assets about `$771M`, trailing yield `1.40%`, expense ratio `0.45%`, and a 2026-07-30 portfolio capture with 424 securities, top-ten weight `20.4%`, foreign issues `96.4%`, and cash `0.8%`.
- Secondary rounded annual NAV-return rows as of the 2026-07-31 table are unchanged: 2016 `8.10%`, 2017 `14.60%`, 2018 `-8.50%`, 2019 `26.80%`, 2020 `-0.50%`, 2021 `23.30%`, 2022 `-6.20%`, 2023 `17.00%`, 2024 `9.50%`, 2025 `22.50%`. These remain marked `*` because the current official DWS factsheet does not expose the calendar rows.
- Cached S&P 500 Total Return common-reference rows are 2016 `11.96%`, 2017 `21.83%`, 2018 `-4.38%`, 2019 `31.49%`, 2020 `18.40%`, 2021 `28.71%`, 2022 `-18.11%`, 2023 `26.29%`, 2024 `25.02%`, and 2025 `17.88%`; USD, dividends reinvested, as of 2025-12-31. These are not DBEU's hedged strategy benchmark.

### Calculations and reconciliation

- Official DWS NAV minus MSCI Europe USD Hedged Index observations as of 2026-06-30 are 3M `+0.10 pp`, 1Y `-0.13 pp`, 3Y `-0.23 pp`, 5Y `-0.15 pp`, 10Y `-0.24 pp`, and since inception `-0.25 pp`; these are passive implementation/expense/hedging observations, not alpha.
- Secondary 2016-2025 rows compound to `159.58%*` and rounded-input CAGR `10.01%*`; up/down years `7 / 3`; best `2019 +26.80%*`; worst `2018 -8.50%*`; population standard deviation `11.83%*`.
- Secondary 2021-2025 rows compound to `81.51%*` and rounded-input CAGR `12.66%*`; up/down years `4 / 1`. Cached S&P 500 TR compounds to `96.17%` / CAGR `14.43%` over the same window.
- Official rolling 10-year NAV TR `11.58%` is kept separate from secondary calendar CAGR `10.01%*` and secondary July trailing 10Y `11.2%*`; they have different source ownership and dates.
- Reconciliation: the prior durable page already used DWS official June rolling `11.58%`; this refresh adds later secondary July current/YTD fields (`12.6%*` YTD) and Aug-27 price while preserving the official June metric and facts. Current price/NAV pair remains unresolved because no same-date NAV was verified.

### Source-quality choice and unresolved gaps

- Official DWS is the source of truth for identity, passive USD-hedged index structure, official rolling NAV/benchmark performance, fee, holdings, country/sector weights, yield and beta. AAII is used only for later rounded July current/YTD/trailing and annual context.
- No official DWS July month-end factsheet or official calendar/YTD table was verified in this run; secondary rows are explicitly marked `*` and do not overwrite the official June rolling field.
- Official daily NAV history sufficient to reproduce maximum drawdown, recovery date and volatility is `ไม่พบข้อมูลที่ยืนยันได้`; AAII's secondary beta/standard deviation is retained only as a dated cross-check.
- Current market price `$54.80` has no verified same-date NAV, so premium/discount and a current NAV/price gap are `ไม่พบข้อมูลที่ยืนยันได้`.

### Pre-save evidence packet / proposed durable contents

- Evidence packet includes ETF identity/exchange, CUSIP/inception, passive eligibility, tracked hedged index, USD NAV-total-return basis, common S&P reference, official and secondary candidate claims, periods, units/currency, metric definitions, separate as-of dates, source URLs/paths, calculations, source-quality selection, unresolved gaps and the complete planned file set.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/performance/ETF_NYSE_ARCA_DBEU Performance.md`: replace the stale June-only narrative with official DWS Q2 table, secondary July cross-check, official rolling `11.58%`, secondary YTD `12.6%*`, retained 2016-2025 and 2021-2025 proxy calculations, current secondary price/assets, USD-hedge risk, dated country/sector facts and official calendar/YTD/NAV-pair/daily-NAV gaps; preserve Europe breadcrumb and tag.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/comparisons/Europe ETF.md`: update only the DBEU row to `11.58% issuer rolling 10Y | 12.66%* | 12.6%*`; append a refresh note distinguishing official June rolling/facts from secondary July current/YTD and Aug-27 price. No new region page is required.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/performance/ETF Performance Index.md`: update the DBEU coverage row to official rolling `11.58%`, secondary 2021-2025 CAGR `12.66%*`, secondary YTD `12.6%*`, best/worst proxy years and source/NAV gaps; append a current reconciliation note; leave the Common Window annual row unchanged.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/log.md`: append one `etf-performance` bullet linking `[[ETF_NYSE_ARCA_DBEU Performance]]`, `[[Europe ETF]]`, `[[ETF Performance Index]]` and `[[ETF_performance_sources_2026-08-29]]`, stating official rolling `11.58%`, secondary YTD `12.6%*`, retained secondary 2021-2025 CAGR `12.66%*`, and the official/secondary gap; preserve unrelated pre-existing log changes outside the scoped commit.
- This source batch section itself is part of the proposed durable write and records the full evidence packet, local checklist and structured handoff.

### Local pre-save checklist

- PASS: official DBEU identity, NYSE Arca key, CUSIP/inception, passive/indexing eligibility, 80% policy, MSCI Europe USD-hedged tracked index, USD NAV basis, Europe region ownership and all source dates are mapped.
- PASS: official June standardized table/facts, secondary July trailing/YTD/annual table, Aug-27 price/assets, cached S&P reference and each metric definition remain separate; secondary fields are visibly marked `*`.
- PASS: annual/CAGR/up-down calculations, official tracking differences, source-quality choice and prior-versus-current reconciliation reproduce the proposed values; no secondary result is relabeled official and no alpha claim is made.
- PASS: complete proposed contents for DBEU performance, Europe region, master index, source batch and log are specified; canonical links/tags are preserved; official calendar/YTD, current NAV pair and daily NAV gaps remain disclosed; no unresolved High/Medium finding blocks the write and no WARNING requiring confirmation remains.
verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official DWS June rolling performance/fund facts plus the latest secondary July/August observations support the DBEU refresh; scheduled-local verification passed, secondary fields remain marked, and official July/current NAV and daily-NAV gaps are disclosed.

## EWX — State Street SPDR S&P Emerging Markets Small Cap ETF

### Workflow identity and scope

- `workflow: check-etf-performance`; `execution_profile: scheduled-inline`; `child_card_ari: ari:cloud:trello::card/workspace/6a78536437ed0b3b544c19e1/6a91775396863dcefd1fe3ac`; `parent_ari: ari:cloud:trello::card/workspace/6a78536437ed0b3b544c19e1/6a91760cdaae83b3d4afdc13`; input ticker `EWX`; canonical `entity_key: NYSE Arca:EWX`.
- Card was claimed and directly reread as `In Progress` before research. Primary region is `Emerging Markets`; the durable graph is `[[ETF Region Index]] → [[Emerging Markets ETF]] → [[ETF Performance Index]]`.
- This refresh updates the existing EWX performance owner, Emerging Markets navigation snapshot, master performance index, this dated source batch and one log bullet. No ETF entity page or normalized fund table is created.

### Source map and as-of dates

| Source | URL/path | Use and as-of date |
|---|---|---|
| State Street official EWX product/performance page | https://www.ssga.com/us/en/intermediary/etfs/state-street-spdr-sp-emerging-markets-small-cap-etf-ewx | Official identity, exchange, passive/indexing classification, benchmark, current NAV/market price/AUM/holdings/sectors/characteristics/yields and standardized performance; current fields as of 2026-08-27 to 2026-08-28 and performance table as of 2026-07-31 |
| State Street official EWX factsheet | https://www.ssga.com/library-content/products/factsheets/etfs/us/factsheet-us-en-ewx.pdf | Official fund-document and standardized-return cross-reference; reviewed result dated 2026-07-31 |
| SEC EWX summary prospectus | https://www.sec.gov/Archives/edgar/data/1168164/000119312526031211/d87745d497k.htm | Official passive strategy, index construction, fees, risks and best/worst-quarter context |
| ETFreplay EWX | https://www.etfreplay.com/etf/ewx | Secondary dividend-adjusted calendar rows 2016-2025 and partial-2026 observation; page capture as of 2026-08-21 |
| FinanceCharts EWX | https://www.financecharts.com/etfs/EWX/performance | Secondary YTD/rolling and annual cross-check; current crawl observation retained only for conflict disclosure |
| S&P 500 official index page and cached workflow references | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Common USD Total Return reference for complete calendar years 2016-2025; cached convention as of 2025-12-31, dividends reinvested |
| Existing vault context | `wiki/analysis/performance/ETF_NYSE_ARCA_EWX Performance.md`, `wiki/analysis/comparisons/Emerging Markets ETF.md`, `wiki/analysis/performance/ETF Performance Index.md`, `raw/imports/ETF_performance_sources_2026-08-17.md` | Prior page structure, region ownership, annual proxy rows and earlier official fields; refreshed claims use the newer official capture above |

### Identity and classification evidence

- State Street identifies EWX as `State Street SPDR S&P Emerging Markets Small Cap ETF`, listed on NYSE Arca, ticker `EWX`, CUSIP `78463X756`, ISIN `US78463X7562`, inception `2008-05-12`, benchmark `S&P Emerging Under USD2 Billion Index`, base currency USD and semi-annual distributions.
- Classification is `passive-index-tracking`; the issuer describes sampling and at least 80% exposure to index securities/ADRs/GDRs. Incidental futures/cash-flow instruments do not change the passive equity classification.
- Primary region is Emerging Markets and canonical tag is `geography/Emerging-Markets`.

### Candidate performance claims and raw observations

- Official State Street standardized returns as of 2026-07-31 are NAV / market value / linked index: 1M `-8.69% / -9.58% / -8.87%`; QTD `-8.69% / -9.58% / -8.87%`; YTD `3.91% / 3.07% / 3.33%`; 1Y `9.84% / 10.33% / 9.11%`; 3Y annualized `9.82% / 9.58% / 10.12%`; 5Y annualized `5.32% / 5.14% / 5.58%`; 10Y annualized `7.95% / 7.87% / 8.19%`; since inception annualized `4.18% / 4.14% / 5.11%`.
- Official current State Street capture reports NAV `$73.96`, market price/close `$74.02`, premium/discount `0.08%`, median bid/ask spread `0.15%`, and volume `4,554` as of 2026-08-27. AUM is `$702.61M` as of 2026-08-27; gross expense ratio is `0.65%`.
- Official characteristics as of 2026-08-27 include 3,383 holdings, P/B `1.70`, P/E FY1 `14.77`, weighted average market cap `$1,816.91M`, 30-day SEC yield `1.99%`, fund distribution `2.49%`, and index dividend `2.35%`.
- Official sector weights as of 2026-08-27 are IT `26.67%`, Industrials `17.38%`, Materials `12.50%`, Consumer Discretionary `10.58%`, Financials `7.46%`, Health Care `7.10%`, Real Estate `5.77%`, Consumer Staples `5.45%`, Utilities `2.65%`, Communication Services `2.31%`, Energy `1.83%`, and Unassigned `0.29%`.
- Official top-ten holdings as of 2026-08-27 are LandMark Optoelectronics `0.76%`, Kinsus `0.72%`, Macronix `0.61%`, Katilim… `0.47%`, WinWay `0.44%`, Win Semiconductors `0.43%`, ITEQ `0.35%`, Syntec `0.31%`, A Data `0.31%`, and Innodisk `0.30%`; shown weights sum to `4.70%`.
- A prior official geographic snapshot as of 2026-08-14 listed Taiwan `31.79%`, India `18.50%`, and China `17.82%`. The latest accessible 2026-08-27 page did not expose a current geographic breakdown, so these older values are not presented as current.
- ETFreplay secondary annual total-return rows are 2016 `7.94%`, 2017 `34.10%`, 2018 `-18.74%`, 2019 `15.59%`, 2020 `14.86%`, 2021 `18.16%`, 2022 `-15.00%`, 2023 `18.15%`, 2024 `6.84%`, and 2025 `15.44%`; its partial-2026 observation is `+10.72%` as of 2026-08-21. These rows are dividend-adjusted secondary proxy evidence, not official NAV rows.
- FinanceCharts cross-check shows annual values within roughly `0.01–0.03 pp` of the ETFreplay rows, but current YTD `4.76%` and 10-year CAGR `8.18%` differ from ETFreplay and official State Street; these fields are retained only as a source conflict, not mixed into canonical performance.
- Cached S&P 500 Total Return common-reference rows for 2016-2025 are 2016 `11.96%`, 2017 `21.83%`, 2018 `-4.38%`, 2019 `31.49%`, 2020 `18.40%`, 2021 `28.71%`, 2022 `-18.11%`, 2023 `26.29%`, 2024 `25.02%`, and 2025 `17.88%`; USD, dividends reinvested, as of 2025-12-31. This is not EWX's strategy benchmark.
- Prospectus context reports best quarter `+25.82%` in Q2 2020 and worst quarter `-28.68%` in Q1 2020. Official daily NAV history sufficient to reproduce maximum drawdown, recovery and volatility is `ไม่พบข้อมูลที่ยืนยันได้`.

### Calculations and reconciliation

- Secondary 2016-2025 rows compound to `128.55%*`; rounded-input CAGR is `(1 + 1.2855)^(1/10) - 1 = 8.62%*`; up/down years are `8 / 2`, best is 2017 `+34.10%*`, and worst is 2018 `-18.74%*`.
- Secondary 2021-2025 rows compound to `46.36%*`; rounded-input CAGR is `(1 + 0.4636)^(1/5) - 1 = 7.92%*`. Cached S&P 500 TR compounds to `96.17%` / CAGR `14.43%` over the same window.
- Official NAV minus linked-index observations as of 2026-07-31 are 1M/QTD `+0.18 pp`, YTD `+0.58 pp`, 1Y `+0.73 pp`, 3Y `-0.30 pp`, 5Y `-0.26 pp`, 10Y `-0.24 pp`, and since inception `-0.93 pp`; these are implementation/expense observations, not alpha.
- Official rolling 10-year NAV TR `7.95%` is kept separate from the secondary 2016-2025 CAGR `8.62%*` and 2021-2025 CAGR `7.92%*`; official rolling, month-end YTD and secondary calendar rows have different windows and source ownership.
- Reconciliation: ETFreplay partial-2026 return `+10.72%` is through 2026-08-21, while official State Street YTD `+3.91%` is through 2026-07-31. FinanceCharts' `4.76%` YTD and `8.18%` 10-year secondary values are not used to overwrite either field.

### Source-quality choice and unresolved gaps

- State Street is the source of truth for identity, passive classification, tracked index, official NAV/market/index performance, fee, AUM, holdings, sector weights, characteristics and yields. ETFreplay is used only for the complete annual proxy and FinanceCharts only as a secondary conflict check.
- Official current geographic breakdown was not exposed in the latest accessible page capture; prior 2026-08-14 country values are retained with their date and are not asserted as current.
- Official daily NAV history sufficient to independently reproduce maximum drawdown, recovery date and volatility is `ไม่พบข้อมูลที่ยืนยันได้`; no secondary drawdown number is promoted to a NAV claim.
- The official current NAV/market pair and premium/discount are available as of 2026-08-27; they are point-in-time values and are not treated as total return.

### Pre-save evidence packet / proposed durable contents

- Evidence packet includes ETF identity and exchange, return basis (`NAV Total Return`), issuer benchmark, common benchmark, candidate claims and periods, units/currency (`%`, USD), metric definitions, separate as-of dates, source URLs/paths, calculations, source-quality selection, unresolved gaps and the complete planned write set.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/performance/ETF_NYSE_ARCA_EWX Performance.md`: replace stale Aug-14 fields with official July standardized NAV/market/index table, official rolling `7.95%`, official YTD `3.91%`, current Aug-27 NAV/market/AUM/holdings/sectors, retained secondary 2016-2025 and 2021-2025 proxy calculations, current country-data gap and official daily-NAV/drawdown gap; preserve the Emerging Markets breadcrumb and tag.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/comparisons/Emerging Markets ETF.md`: preserve the official 10Y/2021-2025/YTD snapshot row, update the page date and append current official EWX NAV/market/AUM/holdings context plus the current-country disclosure.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/performance/ETF Performance Index.md`: retain EWX's official/secondary headline metrics, add the current NAV/market snapshot to the coverage row and expand the EWX reconciliation note with the official country/daily-NAV gaps; do not change strict Common Window ranking membership.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/log.md`: append one `etf-performance` bullet linking `[[ETF_NYSE_ARCA_EWX Performance]]`, `[[Emerging Markets ETF]]`, `[[ETF Performance Index]]` and `[[ETF_performance_sources_2026-08-29]]`, stating official rolling `7.95%`, official YTD `3.91%`, retained secondary 2021-2025 CAGR `7.92%*`, and preserved source/daily-NAV gaps; keep the file outside the scoped commit because it already contains unrelated changes.
- No new ETF entity or region page is required; existing navigation remains the canonical owner.

### Local pre-save checklist

- PASS: official NYSE Arca identity, fund name, inception, passive/index-tracking equity eligibility, canonical key, tracked index, return basis, USD units, and Emerging Markets region ownership are source-mapped.
- PASS: official July standardized table, official August NAV/market/AUM/fund facts, secondary annual/partial-YTD observations, cached S&P rows and each metric definition retain separate sources and as-of dates; secondary fields remain visibly marked `*`.
- PASS: annual/CAGR/up-down calculations, official tracking differences, source-quality choice, current-country gap and prior-versus-current reconciliation reproduce the proposed values; no secondary result is relabeled official and no alpha claim is made.
- PASS: complete proposed contents for EWX performance, Emerging Markets region, index, source batch and log artifacts are specified; breadcrumbs/tags/source links are preserved; no unresolved High/Medium finding blocks the write and no WARNING requiring confirmation remains.
verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official State Street July standardized performance and August current fund data support the EWX refresh; scheduled-local verification passed, secondary annual/current conflicts remain marked, and current-country plus official daily-NAV gaps are disclosed.

## FEZ — State Street SPDR EURO STOXX 50 ETF

### Workflow identity and scope

- `workflow: check-etf-performance`; `execution_profile: scheduled-inline`; `child_card_ari: ari:cloud:trello::card/workspace/6a78536437ed0b3b544c19e1/6a917758a24a445865b49aa6`; `parent_ari: ari:cloud:trello::card/workspace/6a78536437ed0b3b544c19e1/6a91760cdaae83b3d4afdc13`; input ticker `FEZ`; canonical `entity_key: NYSE Arca:FEZ`.
- Card was claimed and directly reread as `In Progress` before research. Primary region is `Europe`; the durable graph is `[[ETF Region Index]] → [[Europe ETF]] → [[ETF Performance Index]]`.
- This refresh updates the existing FEZ performance owner, Europe navigation snapshot, master performance index, this dated source batch and one log bullet. No ETF entity page or normalized fund table is created.

### Source map and as-of dates

| Source | URL/path | Use and as-of date |
|---|---|---|
| State Street official FEZ product/performance page | https://www.ssga.com/us/en/intermediary/etfs/state-street-spdr-euro-stoxx-50-etf-fez | Official identity, exchange, passive/indexing classification, benchmark, current NAV/market price/AUM, holdings/sectors/characteristics/yields and standardized performance; current fields as of 2026-08-27 to 2026-08-28 and performance table as of 2026-07-31 |
| State Street official FEZ factsheet | https://www.ssga.com/library-content/products/factsheets/etfs/us/factsheet-us-en-fez.pdf | Official return definition, index objective, June 2026 fund facts, country/sector/holding snapshot and risk context; as of 2026-06-30 |
| State Street distribution page | https://www.ssga.com/us/en/intermediary/resources/documents/etf-dividend-distributions | Official distribution-source context; product page states quarterly distribution frequency |
| ETFreplay FEZ | https://www.etfreplay.com/etf/fez | Secondary dividend-adjusted calendar rows 2016-2025 and annual-return volatility cross-check; page capture as of 2026-08-21 |
| FinanceCharts FEZ | https://www.financecharts.com/etfs/FEZ/performance | Secondary current/annual cross-check; values are not mixed into canonical official fields |
| S&P 500 official index page and cached workflow references | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Common USD Total Return reference for complete calendar years 2016-2025; cached convention as of 2025-12-31, dividends reinvested |
| Existing vault context | `wiki/analysis/performance/ETF_NYSE_ARCA_FEZ Performance.md`, `wiki/analysis/comparisons/Europe ETF.md`, `wiki/analysis/performance/ETF Performance Index.md`, `raw/imports/ETF_performance_sources_2026-08-18.md` | Prior page structure, region ownership, older secondary rows and prior official snapshot; refreshed claims use the newer official/secondary captures above |

### Identity and classification evidence

- State Street identifies FEZ as `State Street SPDR EURO STOXX 50 ETF`, listed on NYSE Arca, ticker `FEZ`, CUSIP `78463X202`, ISIN `US78463X2027`, inception `2002-10-15`, benchmark `EURO STOXX 50 Index`, base currency USD and quarterly distributions.
- Classification is `passive-index-tracking`; the fund seeks to correspond generally to the total-return performance of the EURO STOXX 50 Index before fees and expenses. State Street describes sampling mechanics and related tracking-error risk; the payoff is not derivative-defined.
- Primary region is Europe and canonical tag is `geography/Europe`.

### Candidate performance claims and raw observations

- Official State Street standardized returns as of 2026-07-31 are NAV / market value / linked index: 1M `1.20% / 1.56% / 1.20%`; QTD `1.20% / 1.56% / 1.20%`; YTD `9.66% / 10.27% / 9.46%`; 1Y `22.94% / 23.82% / 22.78%`; 3Y annualized `16.94% / 17.17% / 16.76%`; 5Y annualized `11.50% / 11.53% / 11.23%`; 10Y annualized `10.92% / 10.96% / 10.76%`; since inception annualized `7.83% / 7.84% / 7.60%`.
- Official current State Street capture reports NAV `$71.14`, shares outstanding `63.30M`, AUM `$4,503.11M`, net cash amount `$8,865,134.99`, market midpoint/close `$71.34`, premium/discount `0.27%`, median bid/ask spread `0.01%`, and exchange volume `356,124` as of 2026-08-27. Gross expense ratio is `0.29%`.
- Official characteristics as of 2026-08-27 include 50 holdings, P/B `2.48`, P/E FY1 `16.08`, weighted average market cap `$197,779.33M`, estimated 3-5 year EPS growth `15.63%`, 30-day SEC yield `1.94%`, fund distribution yield `2.50%`, and index dividend yield `2.66%`.
- Official current fund top-ten holdings as of 2026-08-27 are ASML Holding `8.84%`, Siemens `4.69%`, SAP `4.28%`, Banco Santander `4.11%`, Schneider Electric `3.83%`, Allianz `3.77%`, TotalEnergies `3.76%`, BBVA `3.10%`, Safran `2.82%`, and Iberdrola `2.81%`; shown weights sum to `42.01%`.
- Official current fund sector weights as of 2026-08-27 are Financials `28.42%`, Industrials `22.00%`, Information Technology `14.86%`, Consumer Discretionary `9.32%`, Health Care `5.38%`, Consumer Staples `5.15%`, Energy `4.81%`, Utilities `4.46%`, Materials `3.41%`, and Communication Services `2.19%`.
- Official factsheet country weights as of 2026-06-30 are France `32.27%`, Germany `28.88%`, Netherlands `14.98%`, Spain `11.36%`, Italy `8.38%`, Belgium `2.85%`, and Finland `1.28%`; the latest product-page geographic section did not expose a newer country breakdown. The same factsheet's June sector snapshot is Financials `26.79%`, Industrials `22.09%`, IT `15.96%`, Consumer Discretionary `9.58%`, Consumer Staples `5.55%`, Health Care `5.32%`, Utilities `4.90%`, Energy `4.47%`, Materials `3.46%`, and Communication Services `1.88%`.
- ETFreplay secondary annual total-return rows are 2016 `0.64%`, 2017 `24.78%`, 2018 `-15.85%`, 2019 `26.04%`, 2020 `4.85%`, 2021 `14.83%`, 2022 `-14.30%`, 2023 `27.19%`, 2024 `3.55%`, and 2025 `37.78%`; these are dividend-adjusted proxy rows, not official NAV rows. ETFreplay also reports annualized daily volatility `18.4%` as of 2026-08-21.
- FinanceCharts is retained as a cross-check: its annual rows are close but not identical (for example 2016 `0.67%`, 2025 `37.81%`) and its current YTD/rolling values are source/date observations distinct from the official State Street July table; no FinanceCharts field overwrites the canonical data.
- Cached S&P 500 Total Return common-reference rows for 2016-2025 are 2016 `11.96%`, 2017 `21.83%`, 2018 `-4.38%`, 2019 `31.49%`, 2020 `18.40%`, 2021 `28.71%`, 2022 `-18.11%`, 2023 `26.29%`, 2024 `25.02%`, and 2025 `17.88%`; USD, dividends reinvested, as of 2025-12-31. This is not FEZ's strategy benchmark.
- Official daily NAV history sufficient to reproduce maximum drawdown and recovery is `ไม่พบข้อมูลที่ยืนยันได้`; no price-only drawdown proxy is substituted.

### Calculations and reconciliation

- Secondary 2016-2025 rows compound to `149.39%*`; rounded-input CAGR is `(1 + 1.4939)^(1/10) - 1 = 9.57%*`; population standard deviation is `17.24%*`; up/down years are `8 / 2`, best is 2025 `+37.78%*`, least positive is 2016 `+0.64%*`, worst is 2018 `-15.85%*`, and least-bad down year is 2022 `-14.30%*`.
- Secondary 2021-2025 rows compound to `78.58%*`; rounded-input CAGR is `(1 + 0.7858)^(1/5) - 1 = 12.30%*`. Cached S&P 500 TR compounds to `96.17%` / CAGR `14.43%` over the same window.
- Official NAV minus linked-index observations as of 2026-07-31 are 1M/QTD `0.00 pp`, YTD `+0.20 pp`, 1Y `+0.16 pp`, 3Y `+0.18 pp`, 5Y `+0.27 pp`, 10Y `+0.16 pp`, and since inception `+0.23 pp`; these are implementation/expense observations, not alpha.
- Official rolling 10-year NAV TR `10.92%` is kept separate from secondary 2016-2025 CAGR `9.57%*` and 2021-2025 CAGR `12.30%*`; official rolling and secondary calendar windows have different source ownership.
- Reconciliation: fresh ETFreplay annual rows replace the prior rounded FinanceCharts proxy for consistency. The small differences are disclosed rather than smoothed; official State Street rolling/YTD fields remain unchanged and current NAV/market fields are refreshed to 2026-08-27.

### Source-quality choice and unresolved gaps

- State Street is the source of truth for identity, passive classification, tracked index, official NAV/market/index performance, fee, AUM, holdings, sectors, characteristics, yields and current premium/discount. ETFreplay is used for the complete secondary annual proxy and FinanceCharts only as a cross-check.
- Official current country breakdown was not exposed in the latest product-page capture; June factsheet country weights are retained with their date and are not asserted as current.
- Official daily NAV history sufficient to independently reproduce maximum drawdown and recovery date is `ไม่พบข้อมูลที่ยืนยันได้`; ETFreplay's daily volatility is secondary context only.
- The current NAV/market pair is point-in-time data and is not treated as total return.

### Pre-save evidence packet / proposed durable contents

- Evidence packet includes ETF identity and exchange, return basis (`NAV Total Return`), issuer benchmark, common benchmark, candidate claims and periods, units/currency (`%`, USD), metric definitions, separate as-of dates, source URLs/paths, calculations, source-quality selection, unresolved gaps and the complete planned write set.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/performance/ETF_NYSE_ARCA_FEZ Performance.md`: replace the stale August-17 snapshot and old secondary proxy with the official July standardized NAV/market/index table, official rolling `10.92%`, official YTD `9.66%`, current Aug-27 NAV/market/AUM/holdings/sectors, fresh secondary annual proxy calculations, dated factsheet country weights, risk context and official daily-NAV/drawdown gap; preserve the Europe breadcrumb and tag.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/comparisons/Europe ETF.md`: update only the FEZ row to secondary 2021-2025 CAGR `12.30%*`, retain official `10.92%` and `9.66%`, and append current official NAV/market/premium/AUM context plus the country/daily-NAV gap.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/performance/ETF Performance Index.md`: update the FEZ coverage row and reconciliation note to `149.39%* / 9.57%*` for 2016-2025, `78.58%* / 12.30%*` for 2021-2025, best/worst proxy years, current NAV/market snapshot and strict-ranking exclusion; preserve historical dated coverage bullets.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/log.md`: append one `etf-performance` bullet linking `[[ETF_NYSE_ARCA_FEZ Performance]]`, `[[Europe ETF]]`, `[[ETF Performance Index]]` and `[[ETF_performance_sources_2026-08-29]]`, stating official rolling `10.92%`, official YTD `9.66%`, fresh secondary 2021-2025 CAGR `12.30%*`, and preserved country/daily-NAV gaps; keep the file outside the scoped commit because it already contains unrelated changes.
- No new ETF entity or region page is required; existing Europe navigation remains the canonical owner.

### Local pre-save checklist

- PASS: official NYSE Arca identity, fund name, inception, passive/index-tracking equity eligibility, canonical key, tracked index, return basis, USD units, and Europe region ownership are source-mapped.
- PASS: official July standardized table, official August NAV/market/AUM/fund facts, June factsheet country/sector context, fresh secondary annual rows/volatility, cached S&P rows and each metric definition retain separate sources and as-of dates; secondary fields remain visibly marked `*`.
- PASS: annual/CAGR/up-down/dispersion calculations, official tracking differences, source-quality choice, prior-proxy reconciliation and current-country/daily-NAV gaps reproduce the proposed values; no secondary result is relabeled official and no alpha claim is made.
- PASS: complete proposed contents for FEZ performance, Europe region, index, source batch and log artifacts are specified; breadcrumbs/tags/source links are preserved; no unresolved High/Medium finding blocks the write and no WARNING requiring confirmation remains.
verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official State Street July standardized performance and August current fund data support the FEZ refresh; scheduled-local verification passed, fresh secondary annual rows remain marked, and country/daily-NAV gaps are disclosed.

## FNDA — Schwab Fundamental U.S. Small Company ETF

### Workflow identity and scope

- `workflow: check-etf-performance`; `execution_profile: scheduled-inline`; `child_card_ari: ari:cloud:trello::card/workspace/6a78536437ed0b3b544c19e1/6a91775dba7092ffa28aee67`; `parent_ari: ari:cloud:trello::card/workspace/6a78536437ed0b3b544c19e1/6a91760cdaae83b3d4afdc13`; input ticker `FNDA`; canonical `entity_key: NYSE Arca:FNDA`.
- Card was claimed and directly reread as `In Progress` before research. Primary region is `USA`; the durable graph is `[[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]`.
- This refresh updates the existing FNDA performance owner, USA navigation snapshot, master performance index, this dated source batch and one log bullet. No ETF entity page or new region page is created.

### Source map and as-of dates

| Source | URL/path | Use and as-of date |
|---|---|---|
| Schwab Asset Management official FNDA product page | https://www.schwabassetmanagement.com/products/fnda | Official identity, exchange, passive classification, current index, fee, NAV/AUM/holdings, characteristics, yields, quote fields and July standardized performance/risk; fund/current fields as of 2026-08-27 to 2026-08-28 and performance table as of 2026-07-31 |
| Schwab official FNDA fact-sheet page | https://www.schwabassetmanagement.com/resource/fnda-fact-sheet | Issuer document entry, fund facts and methodology context; source document date is kept separate where shown |
| SEC FNDA summary prospectus | https://www.sec.gov/Archives/edgar/data/1454889/000110465925063127/tm2513735-8_497k.htm | Passive objective, fees, benchmark-change context and risk disclosures |
| ETFreplay FNDA | https://www.etfreplay.com/etf/fnda | Secondary dividend-adjusted calendar rows 2016-2025 and annualized daily-volatility cross-check; annual rows captured in the current run |
| FinanceCharts FNDA | https://www.financecharts.com/etfs/FNDA/performance | Secondary cross-check only; close but non-identical annual/current observations are not mixed into canonical official fields |
| S&P 500 official index page and cached workflow references | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Common USD Total Return reference for complete calendar years 2016-2025; cached convention as of 2025-12-31, dividends reinvested |
| Existing vault context | `wiki/analysis/performance/ETF_NYSE_ARCA_FNDA Performance.md`, `wiki/analysis/comparisons/USA ETF.md`, `wiki/analysis/performance/ETF Performance Index.md`, prior dated source batch | Prior page structure, USA ownership, older official snapshot and secondary rows; stale values are replaced only where refreshed evidence supports it |

### Identity and classification evidence

- Schwab identifies FNDA as `Schwab Fundamental U.S. Small Company ETF`, ticker `FNDA`, listed on NYSE Arca, CUSIP `808524763`, inception `2013-08-15`, and total expense ratio `0.250%`.
- Classification is `passive-index-tracking`; the fund seeks to track, before fees and expenses, the total return of an index measuring small U.S. companies using fundamental size and weighting measures. Schwab labels management style `Passive`.
- Current issuer benchmark is `RAFI Fundamental High Liquidity US Small Index`. Schwab notes the benchmark changed from `Russell RAFI US Small Company Index` effective `2024-06-21`; `Fundamental U.S. Small Company Spliced Index` is the official long-history comparison.
- Primary region is USA and canonical tag is `geography/United-States`.

### Candidate performance claims and raw observations

- Official Schwab standardized returns as of `2026-07-31` are: FNDA market price 1M `-2.34%`, 3M `4.65%`, YTD `18.49%`, 1Y `28.86%`, 3Y annualized `13.07%`, 5Y annualized `8.53%`, 10Y annualized `10.72%`, since-inception annualized `10.27%`; FNDA NAV 1M `-2.29%`, 3M `4.59%`, YTD `18.41%`, 1Y `28.73%`, 3Y `13.09%`, 5Y `8.52%`, 10Y `10.72%`, since inception `10.27%`.
- Official current-index rows as of `2026-07-31` are RAFI Fundamental High Liquidity US Small Index 1M `-2.27%`, 3M `4.65%`, YTD `18.59%`, 1Y `29.03%`; longer periods are not disclosed. The official long-history spliced index is 1M `-2.27%`, 3M `4.65%`, YTD `18.59%`, 1Y `29.03%`, 3Y `13.31%`, 5Y `8.72%`, 10Y `10.92%`; inception is not disclosed.
- Official comparative rows as of `2026-07-31` are Russell RAFI US Small Company Index 1M `-2.44%`, 3M `5.26%`, YTD `19.86%`, 1Y `31.59%`, 3Y `13.86%`, 5Y `9.03%`, 10Y `11.08%`; Russell 2000 Index 1M `-3.03%`, 3M `4.99%`, YTD `18.85%`, 1Y `34.18%`, 3Y `15.09%`, 5Y `7.11%`, 10Y `10.64%`.
- Official current Schwab fields as of `2026-08-27` to `2026-08-28` are NAV `$37.61`, previous close `$37.62`, indicative bid/ask midpoint `$37.61`, premium/discount `0.03%`, 30-day median bid/ask spread `0.03%`, total net assets `$9,238,333,945.91`, shares outstanding `245,650,000`, and holdings `918`. Portfolio turnover is `24.50%` as of `2026-07-31`.
- Official characteristics as of `2026-07-31` are weighted average market cap `$8.98B`, P/E `18.78`, P/CF `9.63`, ROE `10.07%`, P/B `2.04`, 3-year beta versus benchmark `1.00`, 3-year standard deviation `18.27%`, SEC 30-day yield `1.14%` as of 2026-08-27, and TTM distribution yield `1.12%` as of 2026-07-31.
- Current official top holdings as of `2026-08-27` are Lumentum Holdings `0.56%`, Victoria's Secret `0.47%`, Compass Class A `0.44%`, Delek US `0.37%`, Abercrombie & Fitch Class A `0.36%`, Twilio Class A `0.34%`, MKS `0.34%`, Par Pacific Holdings `0.33%`, Coherent `0.33%`, and ATI `0.32%`; the displayed top ten sum is `3.86%`.
- Official sector weights as of `2026-06-30` are Industrials `20.73%`, Financials `16.31%`, Information Technology `14.26%`, Consumer Discretionary `12.57%`, Real Estate `9.22%`, Health Care `7.39%`, Energy `4.93%`, Materials `4.85%`, Communication Services `3.85%`, Consumer Staples `3.25%`, and Utilities `2.63%`. Asset allocation as of 2026-08-27 is stocks `99.91%`, cash investments `0.09%`, other `0.00%`.
- Official risk table reports best three months `+32.40%` for 2020-10-31 to 2021-01-31 and worst three months `-35.49%` for 2019-12-31 to 2020-03-31. Official daily NAV history sufficient to reproduce maximum drawdown and recovery is `ไม่พบข้อมูลที่ยืนยันได้`.
- ETFreplay secondary annual total-return rows are 2016 `23.54%`, 2017 `12.66%`, 2018 `-12.10%`, 2019 `24.33%`, 2020 `8.46%`, 2021 `31.11%`, 2022 `-14.82%`, 2023 `20.31%`, 2024 `8.99%`, and 2025 `7.44%`; these are dividend-adjusted proxy rows, not issuer-published NAV rows. Its partial 2026 observation is not mixed with the official July YTD.
- FinanceCharts is retained only as a cross-check: its close annual observations include 2016 `23.49%`, 2017 `12.71%`, 2018 `-12.11%`, 2019 `24.32%`, 2020 `8.45%`, 2021 `31.13%`, 2022 `-14.82%`, 2023 `20.29%`, 2024 `8.99%`, and 2025 `7.44%`; no FinanceCharts current field overwrites the official Schwab table.
- Cached S&P 500 Total Return common-reference rows for 2016-2025 are 2016 `11.96%`, 2017 `21.83%`, 2018 `-4.38%`, 2019 `31.49%`, 2020 `18.40%`, 2021 `28.71%`, 2022 `-18.11%`, 2023 `26.29%`, 2024 `25.02%`, and 2025 `17.88%`; USD, dividends reinvested, as of `2025-12-31`. This is not FNDA's strategy benchmark.

### Calculations and reconciliation

- Secondary 2016-2025 rows compound to `159.56%*`; rounded-input CAGR is `(1 + 1.5956)^(1/10) - 1 = 10.01%*`; population standard deviation is `14.33%*`; up/down years are `8 / 2`, best is 2021 `+31.11%*`, least positive is 2025 `+7.44%*`, worst is 2022 `-14.82%*`, and least-bad down year is 2018 `-12.10%*`.
- Secondary 2021-2025 rows compound to `57.34%*`; rounded-input CAGR is `(1 + 0.5734)^(1/5) - 1 = 9.49%*`. Cached S&P 500 TR compounds to `96.17%` / CAGR `14.43%` over the same window.
- Official FNDA NAV minus the current RAFI index as of 2026-07-31 is 1M `-0.02 pp`, 3M `-0.06 pp`, YTD `-0.18 pp`, and 1Y `-0.30 pp`; longer current-index fields are not disclosed.
- Against the official long-history spliced index, NAV minus index is 1M `-0.02 pp`, 3M `-0.06 pp`, YTD `-0.18 pp`, 1Y `-0.30 pp`, 3Y `-0.22 pp`, 5Y `-0.20 pp`, and 10Y `-0.20 pp`. These are implementation/expense and index-construction observations, not alpha.
- Reconciliation choice: ETFreplay is the canonical secondary annual series because it supplied the complete current 2016-2025 row set. FinanceCharts differences are preserved as a cross-check. The official July NAV/YTD fields and secondary calendar rows are not merged into one source series.

### Source-quality choice and unresolved gaps

- Schwab is the source of truth for identity, passive classification, current benchmark, official NAV/market/index performance, fee, AUM, holdings, sectors, characteristics, yields, risk and quote fields. ETFreplay supplies only the marked secondary annual proxy; FinanceCharts is cross-check context.
- The current RAFI benchmark has limited long-horizon disclosure on the product page; the official spliced index and historical Russell RAFI row are retained with their distinct definitions and benchmark-change date.
- Complete issuer-published calendar-year NAV rows for 2016-2025 are `ไม่พบข้อมูลที่ยืนยันได้`; annual rows remain marked `*`. Official daily NAV history for independent max drawdown/recovery is also `ไม่พบข้อมูลที่ยืนยันได้`.
- Point-in-time NAV, market price, premium/discount, AUM, holdings, sectors, yield and risk fields retain their own as-of dates and are not treated as total-return data.

### Pre-save evidence packet / proposed durable contents

- Evidence packet includes ETF identity and exchange, return basis (`NAV Total Return`), current and historical issuer benchmarks, common benchmark, candidate claims and periods, units/currency (`%`, USD), metric definitions, separate as-of dates, source URLs/paths, calculations, reconciliation, source-quality choice, unresolved gaps and the complete planned write set.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/performance/ETF_NYSE_ARCA_FNDA Performance.md`: replace the stale June/July snapshot with official July standardized NAV/market/index returns, official rolling `10.72%`, official YTD `18.41%`, current Aug-27/28 NAV/quote/AUM/holdings/characteristics/yields, secondary annual proxy calculations, benchmark-change context, risk evidence and disclosed annual/daily-NAV gaps; preserve the USA breadcrumb and tag.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/comparisons/USA ETF.md`: update the FNDA navigation row to official rolling `10.72%`, secondary 2021-2025 CAGR `9.49%*`, official YTD `18.41%`, and add a current benchmark/as-of note without copying the full performance table.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/performance/ETF Performance Index.md`: update the FNDA coverage row and current coverage note to official rolling `10.72%` and YTD `18.41%` as of 2026-07-31; retain secondary 2016-2025 `159.56%* / 10.01%*`, 2021-2025 `9.49%*`, best/worst proxy years and strict source ownership.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/log.md`: append one `etf-performance` bullet linking `[[ETF_NYSE_ARCA_FNDA Performance]]`, `[[USA ETF]]`, `[[ETF Performance Index]]` and `[[ETF_performance_sources_2026-08-29]]`, stating official rolling `10.72%`, official YTD `18.41%`, retained secondary 2021-2025 CAGR `9.49%*`, and benchmark/calendar/daily-NAV gaps; keep the file outside the scoped commit because it already contains unrelated changes.
- No new ETF entity or region page is required; existing USA navigation remains the canonical owner and no chart is created for this item.

### Local pre-save checklist

- PASS: official NYSE Arca identity, fund name, inception, passive/index-tracking equity eligibility, canonical key, current issuer benchmark, historical benchmark splice, return basis, USD units and USA region ownership are source-mapped.
- PASS: official July standardized table, official August NAV/quote/AUM/fund facts, current holdings/sectors/characteristics/yields/risk fields, fresh secondary annual rows, cached S&P rows and each metric definition retain separate sources and as-of dates; secondary fields remain visibly marked `*`.
- PASS: annual/CAGR/up-down/dispersion calculations, official tracking differences, benchmark-change interpretation, source-quality choice, prior-snapshot reconciliation and annual/daily-NAV gaps reproduce the proposed values; no secondary result is relabeled official and no alpha claim is made.
- PASS: complete proposed contents for FNDA performance, USA region, index, source batch and log artifacts are specified; breadcrumbs/tags/source links are preserved; no unresolved High/Medium finding blocks the write and no WARNING requiring confirmation remains.
verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official Schwab July standardized performance and August current fund data support the FNDA refresh; scheduled-local verification passed, benchmark-change and secondary annual gaps remain disclosed, and official daily-NAV drawdown data is unavailable.

## GREK — Global X MSCI Greece ETF

### Workflow identity and classification

- `workflow: check-etf-performance`; `execution_profile: scheduled-inline`; `child_card_ari: ari:cloud:trello::card/workspace/6a78536437ed0b3b544c19e1/6a917762c8882cc31947fdb5`; `parent_ari: ari:cloud:trello::card/workspace/6a78536437ed0b3b544c19e1/6a91760cdaae83b3d4afdc13`; input ticker `GREK`; canonical `entity_key: NYSE Arca:GREK`.
- Card was claimed and directly reread as `In Progress` before research. Primary region is `Greece`; the durable graph is `[[ETF Region Index]] → [[Greece ETF]] → [[ETF Performance Index]]`.
- Global X identifies GREK as `Global X MSCI Greece ETF`, listed on NYSE Arca, launched 2011-12-07, and tracking the `MSCI All Greece Select 25/50 Index`. The fund is passive/index-tracking, non-diversified, and its prospectus requires at least 80% of assets to be economically tied to Greece or index instruments.

### Source map and raw observations

| Source | URL/path | Use and as-of date |
|---|---|---|
| Global X official product page | https://www.globalxetfs.com/funds/grek | Identity, objective, tracked index, current NAV/market/net assets, holdings, spread, yield, sector/risk fields and rolling performance; current fields through 2026-08-28 and standardized rolling fields as of 2026-06-30 |
| Global X official factsheet | https://assets.globalxetfs.com/funds/documents/grek/Fact-Sheet_GREK.pdf | July 2026 standardized NAV/market/index returns, holdings, AUM and fund facts as of 2026-07-31 |
| SEC summary prospectus | https://www.sec.gov/Archives/edgar/data/1432353/000143235326000191/a497kmscigreece.htm | Exchange, strategy, 80% policy, non-diversified status, fee and standardized performance/best-worst-quarter disclosures |
| AAII GREK performance page | https://www.aaii.com/etf/ticker/GREK?via=emailsignup-readmore | Secondary annual NAV total-return proxy rows from the prior reviewed capture; current capture returned 403 |
| ChartRow GREK returns | https://chartrow.com/quote/grek/returns | Conflicting secondary adjusted-close capture through 2026-08-12, used only for source reconciliation |
| S&P 500 Total Return convention | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Cached common USD total-return reference for complete calendar years 2016-2025, dividends reinvested, as of 2025-12-31 |

- Official Global X current snapshot: NAV `US$85.33`, market price `US$85.26`, net assets `US$343.51M` as of 2026-08-28; holdings `32` and 30-day median bid/ask spread `0.45%` as of 2026-08-27; 30-day SEC yield `2.22%` as of 2026-08-28 and semi-annual distributions.
- Official fee is total expense ratio `0.56%` (`0.55%` management fee plus `0.01%` other expenses). Return basis is USD NAV Total Return with distributions/capital gains reinvested and expenses deducted according to issuer convention.
- Official Global X product-page rolling table as of 2026-06-30: fund/index NAV TR `1Y 33.59% / 34.54%`, `3Y 31.38% / 32.28%`, `5Y 26.03% / 26.83%`, `10Y 17.01% / 17.76%`, and since inception `5.71% / 6.55%`.
- Official July factsheet as of 2026-07-31: NAV TR `1M 6.39%`, `YTD 21.99%`, `1Y 34.63%`, `3Y 31.55%`, `5Y 27.58%`, `10Y 16.88%`, and since inception `6.13%`; market-price counterparts are `6.24%`, `22.58%`, `36.34%`, `31.77%`, `27.82%`, `16.78%`, and `6.15%`; factsheet holdings `33` and AUM `US$313.64M` are separately dated.
- SEC standardized table as of 2025-12-31 reports fund/index `1Y 75.12% / 76.40%`, `5Y 24.58% / 25.34%`, and `10Y 13.54% / 14.20%`; index history splices FTSE/ATHEX Custom Capped before 2026-03-01 and MSCI All Greece Select 25/50 after that date.
- Official sector weights as of 2026-07-31 are Financials `49.0%`, Industrials `18.7%`, Utilities `9.1%`, Consumer Discretionary `8.2%`, Energy `6.5%`, Communication Services `4.0%`, Materials `2.8%`, Consumer Staples `0.9%`, and Real Estate `0.9%`. Official risk fields are standard deviation `19.60%`, beta versus S&P 500 `1.10`, Nasdaq-100 `0.69`, MSCI EAFE `1.11`, and MSCI EM `0.65`.
- SEC best quarter is `+31.50%` and worst quarter `-44.00%`; these are quarter observations, not maximum-drawdown measures. Official daily NAV history sufficient to calculate maximum drawdown and recovery remains `ไม่พบข้อมูลที่ยืนยันได้`.
- Secondary AAII annual proxy rows are 2016 `-1.20%`, 2017 `32.20%`, 2018 `-29.90%`, 2019 `49.30%`, 2020 `-13.30%`, 2021 `5.70%`, 2022 `3.00%`, 2023 `43.50%`, 2024 `9.70%`, and 2025 `75.10%`. These are not issuer-published calendar-year NAV rows.
- Cached S&P 500 TR rows are 2016 `11.96%`, 2017 `21.83%`, 2018 `-4.38%`, 2019 `31.49%`, 2020 `18.40%`, 2021 `28.71%`, 2022 `-18.11%`, 2023 `26.29%`, 2024 `25.02%`, and 2025 `17.88%`.

### Calculations and reconciliation

- AAII secondary 2016-2025 rows compound to `255.6659%`, displayed as `255.67%*`; rounded-input CAGR is `(1 + 2.5567)^(1/10) - 1 = 13.53%*`; up/down years are `7 / 3`, best is 2025 `+75.10%*`, and worst is 2018 `-29.90%*`.
- AAII secondary 2021-2025 rows compound to `200.0937%`, displayed as `200.09%*`; rounded-input CAGR is `(1 + 2.0009)^(1/5) - 1 = 24.58%*`; all five years are positive.
- Cached S&P 500 TR compounds to `96.1696%` / CAGR `14.43%` over 2021-2025 and `298.3291%` / CAGR `14.82%` over 2016-2025. The 2021-2025 arithmetic difference versus GREK secondary CAGR is `+10.15 pp`, not manager alpha.
- AAII rows were retained because their 2021-2025 compound/CAGR reconciles to the SEC standardized 5Y fund return `24.58%` and their 2016-2025 CAGR is close to the SEC standardized 10Y `13.54%` after rounding. ChartRow's adjusted-close rows differ and compound to approximately `158.89%` over 2021-2025, so they are not used in the canonical table.
- Official product-page rolling 10Y fund-index gap is `17.01% - 17.76% = -0.75 pp`; rolling 5Y gap is `26.03% - 26.83% = -0.80 pp`. These are tracking/implementation observations, not alpha.

### Source-quality choice and unresolved gaps

- Global X and SEC are the sources of truth for identity, passive classification, strategy, fee, official NAV/market/index performance, portfolio, risk and standardized returns. AAII supplies only the marked secondary annual proxy; ChartRow is retained solely as a conflicting cross-check.
- Current AAII access returned HTTP 403 during this run, so the previously reviewed AAII rows were not presented as newly retrieved data. Official numeric calendar-year NAV rows, raw daily NAV endpoints and daily NAV drawdown/recovery are `ไม่พบข้อมูลที่ยืนยันได้`.
- Point-in-time NAV, market price, net assets, holdings, sectors, yield and risk fields retain their own as-of dates and are not mixed into total-return calculations. July factsheet holdings/AUM are not treated as current August holdings/net assets.

### Pre-save evidence packet / proposed durable contents

- The evidence packet contains the ETF identity and exchange, return basis (`NAV Total Return`), tracked and common benchmarks, candidate claims and periods, units/currency (`%`, USD), definitions, separate as-of dates, source URLs, calculations, reconciliation, source-quality choice, unresolved gaps and the complete planned write set.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/performance/ETF_NYSE_ARCA_GREK Performance.md`: replace the stale August-18 page with the official Global X/SEC identity and rolling tables, official July YTD, current August NAV/market/net-assets/holdings/spread/yield, sector/risk observations, marked AAII annual proxy rows, S&P cache comparison, source conflict note, and disclosed daily-NAV gaps; preserve the Greece breadcrumb, canonical tag and source-batch link.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/comparisons/Greece ETF.md`: update the single GREK navigation row to official rolling `17.01%`, secondary 2021-2025 CAGR `24.58%*`, and official YTD `21.99%`; preserve static navigation and `*` marking for annual proxy data.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/performance/ETF Performance Index.md`: update the GREK coverage row and dated coverage note from secondary YTD `22.00%*` to official YTD `21.99%`, retaining official rolling `17.01%`, secondary calendar metrics, best/worst rows, Greece ownership and daily-NAV gap.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/raw/imports/ETF_performance_sources_2026-08-29.md`: append this GREK source batch with identity, sources, raw observations, calculations, reconciliation, conflicts, gaps, full planned write set, local checklist, scheduled verification lines and the structured handoff.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/log.md`: append one dated `etf-performance` bullet linking `[[ETF_NYSE_ARCA_GREK Performance]]`, `[[Greece ETF]]`, `[[ETF Performance Index]]` and `[[ETF_performance_sources_2026-08-29]]`, stating official rolling `17.01%`, official YTD `21.99%`, secondary 2021-2025 CAGR `24.58%*`, and preserved annual/daily-NAV gaps; keep outside the scoped commit because `log.md` already contains unrelated changes.
- No new ETF entity or region page is required; existing Greece navigation remains the canonical owner and no chart is created for this item.

### Local pre-save checklist

- PASS: official NYSE Arca identity, fund name, inception, passive/index-tracking equity eligibility, canonical key, tracked index, return basis, USD units and Greece region ownership are source-mapped.
- PASS: official June rolling table, July factsheet/YTD, August current NAV/market/net-assets/holdings/spread/yield, portfolio/risk fields, SEC standardized table, secondary annual proxy, cached S&P rows and each metric definition retain separate sources and as-of dates; secondary fields remain visibly marked `*`.
- PASS: annual/CAGR/up-down calculations, official fund-index gaps, splice interpretation, source-quality choice, AAII-versus-ChartRow conflict, prior-snapshot reconciliation and annual/daily-NAV gaps reproduce the proposed values; no secondary result is relabeled official and no alpha claim is made.
- PASS: complete proposed contents for GREK performance, Greece region, index, source batch and log artifacts are specified; breadcrumbs/tags/source links are preserved; no unresolved High/Medium finding blocks the write and no WARNING requiring confirmation remains.
- `verification_mode: scheduled-local`
- `reviewer_dispatch: not-attempted-by-design`

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official Global X July/August and SEC evidence support the GREK refresh; scheduled-local verification passed, secondary annual-source conflict and daily-NAV gaps remain disclosed.
