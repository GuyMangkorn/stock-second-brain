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

## IDX — VanEck Indonesia Index ETF

### Workflow identity and classification

- `workflow: check-etf-performance`; `execution_profile: scheduled-inline`; `child_card_ari: ari:cloud:trello::card/workspace/6a78536437ed0b3b544c19e1/6a917765261453c326d814a6`; `parent_ari: ari:cloud:trello::card/workspace/6a78536437ed0b3b544c19e1/6a91760cdaae83b3d4afdc13`; input ticker `IDX`; canonical `entity_key: NYSE Arca:IDX`.
- Card was claimed and directly reread as `In Progress` before research. Primary region is `Indonesia`; durable graph is `[[ETF Region Index]] → [[Indonesia ETF]] → [[ETF Performance Index]]`.
- VanEck identifies IDX as `VanEck Indonesia Index ETF`, listed on NYSE Arca, launched 2009-01-15, and tracking `MVIS Indonesia Index (MVIDXTR)`. It is a passive/index-tracking equity ETF and is classified as non-diversified; it is not the Indonesian IDX Composite index.

### Source map and raw observations

| Source | URL/path | Use and as-of date |
|---|---|---|
| VanEck official product page | https://www.vaneck.com/us/en/investments/indonesia-index-etf-idx?audience=retail&country=us | Identity, objective, current official NAV/YTD/net assets, fee cap, holdings and rolling/month-end performance; current snapshot through 2026-08-14 and standardized table through 2026-07-31 |
| VanEck official factsheet | https://www.vaneck.com/us/en/investments/indonesia-index-etf-idx-fact-sheet.pdf | Official July 2026 standardized NAV/market/index returns, valuation, top-10 concentration, country/sector weights, yield and fee details |
| SEC summary prospectus | https://www.sec.gov/Archives/edgar/data/1137360/000113736026000469/vaneckindonesiaindexetfidx.htm | Objective, 80% policy, passive/non-diversified classification, risk disclosures and calendar-year chart limitation |
| FinanceCharts IDX performance | https://www.financecharts.com/etfs/IDX/performance | Secondary total-return annual rows and partial-year/period cross-check; not used to replace official NAV fields |
| Investing.com IDX historical data | https://www.investing.com/etfs/marketvectors-indonesia-index-historical-data | Secondary market price through 2026-08-27 |
| Existing vault context | `wiki/analysis/performance/ETF_NYSE_ARCA_IDX Performance.md`, `wiki/analysis/comparisons/Indonesia ETF.md`, `wiki/analysis/performance/ETF Performance Index.md`, `raw/imports/ETF_performance_sources_2026-07-19.md` | Prior page structure, annual proxy rows, macro overlay and previously disclosed gaps; current performance fields are refreshed while the dated macro overlay is retained |
| S&P 500 Total Return convention | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Cached common USD total-return reference for complete calendar years 2016-2025, dividends reinvested, as of 2025-12-31 |

- Official VanEck daily snapshot as of 2026-08-14: NAV `$11.22`, YTD NAV return `-32.77%`, total net assets `$36.45M`; daily holdings `72` as of 2026-08-13.
- Official VanEck factsheet as of 2026-07-31: total net assets `$35.31M`, `71` holdings, P/E `10.73x`, P/B `1.40x`, 30-day SEC yield `3.58%`, exchange `NYSE Arca`, gross expense ratio `0.86%`, fee waiver `-0.29%`, and net expense ratio `0.57%`; contractual cap runs through 2027-05-01.
- Official month-end performance as of 2026-07-31: NAV TR `1M 10.72%`, `3M -15.62%`, `YTD -34.87%`, `1Y -26.74%`, `3Y -13.43%`, `5Y -6.74%`, `10Y -5.02%`, life `3.63%`; MVIS Indonesia Index `11.53%`, `-17.48%`, `-36.54%`, `-28.59%`, `-13.86%`, `-7.04%`, `-4.91%`, `4.00%` respectively.
- Official quarter-end cross-check as of 2026-06-30: NAV 1Y/3Y/5Y/10Y `-30.93%` / `-15.82%` / `-8.96%` / `-5.49%`; MVIS index `-32.88%` / `-16.34%` / `-9.36%` / `-5.42%`. Raw start/end NAV TR endpoints are not disclosed.
- Official July portfolio weights: Indonesia `77.63%`, China `14.07%`, Singapore `4.70%`, Thailand `1.99%`, Malaysia `0.92%`, United Kingdom `0.52%`, Germany `0.34%`, other/cash `-0.16%`; sector weights Financials `26.4%`, Materials `23.2%`, Industrials `12.7%`, Energy `12.4%`, Consumer Staples `9.6%`, Communication Services `8.4%`, Utilities `4.0%`, Health Care `1.6%`, Real Estate `1.4%`, Consumer Discretionary `0.7%`, other/cash `-0.2%`.
- Latest secondary market close located as of 2026-08-27 is `$11.59`; same-date official closing NAV was not exposed. FinanceCharts reports a partial 2026 total-return proxy of `-29.25%`; this is not substituted for the later official 2026-08-14 NAV YTD `-32.77%`.
- Secondary FinanceCharts annual total-return proxy rows are 2016 `16.67%`, 2017 `19.25%`, 2018 `-10.46%`, 2019 `6.13%`, 2020 `-7.45%`, 2021 `-2.60%`, 2022 `-9.39%`, 2023 `1.97%`, 2024 `-9.75%`, and 2025 `13.83%`. The SEC prospectus annual chart is image-based and does not expose numeric annual rows in text.
- Cached S&P 500 TR rows are 2016 `11.96%`, 2017 `21.83%`, 2018 `-4.38%`, 2019 `31.49%`, 2020 `18.40%`, 2021 `28.71%`, 2022 `-18.11%`, 2023 `26.29%`, 2024 `25.02%`, and 2025 `17.88%`.

### Calculations and reconciliation

- FinanceCharts secondary 2016-2025 rows compound to `13.1256%`, displayed as `13.13%*`; rounded-input CAGR is `(1 + 0.1313)^(1/10) - 1 = 1.24%*`; up/down years are `5 / 5`, best is 2017 `+19.25%*`, least positive is 2023 `+1.97%*`, worst is 2018 `-10.46%*`, and least-bad down year is 2022 `-9.39%*`.
- FinanceCharts secondary 2021-2025 rows compound to `-7.5490%`, displayed as `-7.55%*`; rounded-input CAGR is `(1 - 0.0755)^(1/5) - 1 = -1.56%*`; up/down years are `2 / 3`.
- Cached S&P 500 TR compounds to `96.1696%` / CAGR `14.43%` over 2021-2025 and `298.3291%` / CAGR `14.82%` over 2016-2025. The 2021-2025 arithmetic difference versus IDX secondary CAGR is `-16.0 pp`, not alpha.
- Official July 2026 NAV minus MVIS index differences are `-0.81 pp` for YTD, `+1.85 pp` for 1Y, `+0.43 pp` for 3Y, `+0.30 pp` for 5Y and `-0.11 pp` for 10Y. These are implementation, fee, tax, timing and index-construction observations, not alpha.
- The official current YTD `-32.77%` as of 2026-08-14, official month-end YTD `-34.87%` as of 2026-07-31, and secondary partial-year `-29.25%` are retained as separate observations because their dates and source/basis differ; no arithmetic reconciliation is inferred.

### Source-quality choice and unresolved gaps

- VanEck and SEC are the sources of truth for identity, passive classification, benchmark, fee, official NAV/market/index performance, holdings, valuation, country/sector exposure, yield and risk disclosures. FinanceCharts supplies only the marked annual proxy; Investing.com supplies only the later market-price cross-check.
- Official daily holdings and current snapshot are newer than the July factsheet and are not mixed with the July standardized performance/portfolio fields. Price, NAV and total-return data retain their own as-of dates.
- Official numeric calendar-year NAV rows, raw 10-year NAV endpoints, daily NAV TR index levels, maximum drawdown and recovery date are `ไม่พบข้อมูลที่ยืนยันได้`; the annual table remains marked `*`.
- The existing Indonesia macro overlay in the performance page is retained with its original 2026-07-19 source snapshot; it is not presented as newly refreshed macro research in this item.

### Pre-save evidence packet / proposed durable contents

- The evidence packet contains ETF identity and exchange, return basis (`NAV Total Return`), tracked and common benchmarks, candidate claims and periods, units/currency (`%`, USD), definitions, separate as-of dates, source URLs, calculations, reconciliation, source-quality choice, unresolved gaps and the complete planned write set.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/performance/ETF_NYSE_ARCA_IDX Performance.md`: refresh frontmatter, bottom line, official July performance table, official August-14 daily snapshot, August-27 secondary price cross-check, July valuation/portfolio fields, annual proxy calculations and source-quality/gap notes; preserve the existing macro overlay but label its 2026-07-19 source snapshot.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/comparisons/Indonesia ETF.md`: update the IDX row to official rolling `-5.02%`, secondary 2021-2025 CAGR `-1.56%*`, and official current YTD `-32.77%`; preserve the static region navigation and EIDO row.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/performance/ETF Performance Index.md`: update the IDX coverage row to official July rolling `-5.02%`, current official YTD `-32.77%` as of 2026-08-14, and explicitly retain the secondary annual-window marker and gap.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/raw/imports/ETF_performance_sources_2026-08-29.md`: append this IDX source batch with identity, sources, raw claims, calculations, reconciliation, conflicts, gaps, planned write set, local checklist, scheduled verification lines and structured handoff.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/log.md`: append one dated `etf-performance` bullet linking `[[ETF_NYSE_ARCA_IDX Performance]]`, `[[Indonesia ETF]]`, `[[ETF Performance Index]]` and `[[ETF_performance_sources_2026-08-29]]`, stating official rolling `-5.02%`, current official YTD `-32.77%`, secondary 2021-2025 CAGR `-1.56%*`, and preserved annual/daily-NAV gaps; keep outside the scoped commit because `log.md` already contains unrelated changes.
- No new ETF entity or region page is required; existing Indonesia navigation remains the canonical owner and no chart is created for this item.

### Local pre-save checklist

- PASS: official NYSE Arca identity, fund name, inception, passive/index-tracking equity eligibility, non-diversified classification, canonical key, tracked index, return basis, USD units and Indonesia region ownership are source-mapped.
- PASS: official July standardized NAV/market/index table, official August-14 NAV/YTD/net-assets snapshot, August-13 holdings, July valuation/country/sector/yield fields, secondary August-27 price, annual proxy rows, cached S&P rows and metric definitions retain separate sources and as-of dates; secondary fields remain marked `*`.
- PASS: annual/CAGR/up-down calculations, official fund-index differences, YTD date/basis reconciliation, source-quality choice, prior macro overlay provenance and annual/daily-NAV gaps reproduce the proposed values; no secondary result is relabeled official and no alpha claim is made.
- PASS: complete proposed contents for IDX performance, Indonesia region, index, source batch and log artifacts are specified; breadcrumbs/tags/source links are preserved; no unresolved High/Medium finding blocks the write and no WARNING requiring confirmation remains.
- `verification_mode: scheduled-local`
- `reviewer_dispatch: not-attempted-by-design`

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official VanEck July and August evidence support the IDX refresh; scheduled-local verification passed, annual proxy and YTD date conflicts are disclosed, and daily-NAV drawdown data remains unavailable.

## RWJ — Invesco S&P SmallCap 600 Revenue ETF

### Workflow identity and scope

- `workflow: check-etf-performance`; `execution_profile: scheduled-inline`; `child_card_ari: ari:cloud:trello::card/workspace/6a78536437ed0b3b544c19e1/6a917767243f5784f7eba0db`; `parent_ari: ari:cloud:trello::card/workspace/6a78536437ed0b3b544c19e1/6a91760cdaae83b3d4afdc13`; input ticker `RWJ`; canonical `entity_key: NYSE Arca:RWJ`.
- Card was claimed and directly reread as `In Progress` before research. Primary region is `USA`; the durable graph is `[[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]`.
- This refresh updates the existing RWJ performance owner, USA navigation snapshot, master performance index, this dated source batch and one log bullet. No ETF entity page or new region page is created.

### Source map and as-of dates

| Source | URL/path | Use and as-of date |
|---|---|---|
| Invesco official RWJ factsheet | https://www.invesco.com/content/dam/invesco/us/en/product-documents/etf/fact-sheet/rwj-invesco-s-p-smallcap-600-revenue-etf-fact-sheet.pdf | Official identity, passive methodology, NAV/market/index standardized returns, calendar-year rows, holdings, characteristics and yield; factsheet as of 2026-03-31 |
| Invesco official RWJ product page | https://www.invesco.com/us/en/financial-products/etfs/invesco-sp-smallcap-600-revenue-etf.html | Official product and strategy discovery; current dynamic quote/performance fields were not exposed in the text capture reviewed 2026-08-29 |
| SEC RWJ summary prospectus | https://www.sec.gov/Archives/edgar/data/1378872/000119312525325669/d54028d497k.htm | Official identity, NYSE Arca listing, objective, 90% policy, revenue-weighting/full-replication method, fee, risks, inception and issuer performance table; prospectus dated 2025-12-19 |
| TotalRealReturns RWJ comparison | https://totalrealreturns.com/n/RWJ%2CXMMO | Secondary dividend-reinvested total-return current/rolling fields, annual rows and drawdown proxy; data ending 2026-08-26 |
| Barchart RWJ performance | https://www.barchart.com/etfs-funds/quotes/RWJ/performance | Secondary market-price and price-only YTD cross-check; closing price `US$61.64` and price YTD `25.43%` as of 2026-08-28 |
| AAII RWJ profile | https://www.aaii.com/etf/ticker/RWJ?via=emailsignup-readmore | Secondary 2026-07-31 standardized NAV/price returns, share-class assets and yield cross-check |
| ETF Research Center RWJ profile | https://www.etfrc.com/RWJ | Secondary 2026-07-31 standardized returns, holdings/assets and portfolio profile cross-check |
| S&P 500 official index page and cached workflow references | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Common USD Total Return reference for complete calendar years 2016-2025; cached convention as of 2025-12-31, dividends reinvested |
| Existing vault context | `wiki/analysis/performance/ETF_NYSE_ARCA_RWJ Performance.md`, `wiki/analysis/comparisons/USA ETF.md`, `wiki/analysis/performance/ETF Performance Index.md`, prior dated source batch | Prior RWJ page, USA ownership, proxy calculations and disclosed gaps; official factsheet now supports replacing the annual proxy table |

### Identity and classification evidence

- Invesco identifies RWJ as `Invesco S&P SmallCap 600 Revenue ETF`, ticker `RWJ`, listed on NYSE Arca, with inception `2008-02-19` and total expense ratio `0.39%`.
- Classification is `passive-index-tracking`; the fund generally invests at least 90% of assets in the S&P SmallCap 600 Revenue-Weighted Index and uses full replication. The index weights positive-revenue S&P SmallCap 600 constituents by trailing-four-quarter revenue, subject to a 5% maximum constituent weight.
- Primary region is USA and canonical tag is `geography/United-States`. The issuer benchmark is the S&P SmallCap 600 Revenue-Weighted Index; S&P 500 TR remains a common large-cap reference only.

### Candidate performance claims and raw observations

- Official Invesco factsheet standardized returns as of `2026-03-31` are: RWJ NAV `YTD 3.92%`, `1Y 25.49%`, `3Y 11.93%`, `5Y 7.10%`, `10Y 12.06%`, and since inception `11.50%`; market-price returns are `3.96%`, `25.54%`, `11.95%`, `7.04%`, `12.07%`, and `11.50%`; the underlying index is `3.98%`, `25.89%`, `12.32%`, `7.45%`, `12.35%`, and `12.04%`.
- The same factsheet reports the S&P SmallCap 600 Index comparison at `3.51%` YTD, `20.50%` 1Y, `10.51%` 3Y annualized, `4.49%` 5Y annualized, `9.90%` 10Y annualized and `9.63%` since inception. This is a secondary official comparison, not the revenue-weighted tracking index.
- Official calendar-year NAV rows from the Invesco factsheet are: 2016 `30.52%`, 2017 `5.17%`, 2018 `-16.87%`, 2019 `20.25%`, 2020 `20.49%`, 2021 `52.93%`, 2022 `-11.03%`, 2023 `16.42%`, 2024 `11.55%`, and 2025 `7.81%`. Underlying-index rows are `31.36%`, `5.48%`, `-16.79%`, `20.45%`, `20.39%`, `53.30%`, `-10.72%`, `16.75%`, `11.88%`, and `8.22%` respectively.
- Official factsheet characteristics as of `2026-03-31` are `602` holdings, P/B `2.33`, P/E `13.31`, ROE `5.73%`, weighted market cap `US$3,451.26M`, 30-day SEC yield `1.29%`, and total expense ratio `0.39%`.
- Latest accessible secondary TotalRealReturns comparison data ending `2026-08-26` reports RWJ total return YTD `26.53%`, 1Y `30.62%`, 2Y `39.32%` (`18.03%` annualized), 3Y `68.22%` (`18.93%` annualized), 5Y `68.09%` (`10.94%` annualized), and 10Y `251.61%` (`13.40%` annualized). Its current drawdown proxy is `-2.44%` on 2026-08-26 from the 2026-08-04 peak; worst drawdown is `-55.97%` on 2009-03-09 from the 2008-09-19 peak.
- The same secondary source's annual rows are close but not identical to the official factsheet: 2016 `30.72%`, 2017 `5.09%`, 2018 `-16.95%`, 2019 `20.29%`, 2020 `20.83%`, 2021 `52.83%`, 2022 `-10.97%`, 2023 `16.22%`, 2024 `11.81%`, and 2025 `7.75%`; they are retained only as reconciliation evidence, not canonical rows.
- Barchart provides a later secondary market-price close of `US$61.64` as of `2026-08-28` and price-only YTD `25.43%`; it is not a total-return or NAV observation. AAII's 2026-07-31 cross-check reports NAV YTD `25.8%`, 1Y `39.9%`, 3Y `16.1%`, 5Y `10.8%`, 10Y `13.3%`, and share-class assets `US$2,065M`; ETFRC reports `593` holdings and approximately `US$2B` of assets on the same date.
- Cached S&P 500 TR rows are 2016 `11.96%`, 2017 `21.83%`, 2018 `-4.38%`, 2019 `31.49%`, 2020 `18.40%`, 2021 `28.71%`, 2022 `-18.11%`, 2023 `26.29%`, 2024 `25.02%`, and 2025 `17.88%`; USD, dividends reinvested, as of `2025-12-31`.

### Calculations and reconciliation

- Official displayed NAV rows compound to `214.9599%`, displayed as `214.96%`; rounded-input CAGR is `(1 + 2.149599)^(1/10) - 1 = 12.16%` over 2016-2025. The 2021-2025 compound is `90.4989%`, displayed as `90.50%`, with rounded-input CAGR `13.76%`.
- Official displayed index rows compound to `223.4590%` / CAGR `12.46%` over 2016-2025 and `93.4698%` / CAGR `14.11%` over 2021-2025. S&P 500 TR compounds to `298.3291%` / CAGR `14.82%` and `96.1696%` / CAGR `14.43%` over the same windows.
- Official RWJ-minus-index tracking differences from the 2026-03-31 factsheet are `-0.06 pp` YTD, `-0.40 pp` 1Y, `-0.39 pp` 3Y, `-0.35 pp` 5Y, `-0.29 pp` 10Y and `-0.54 pp` since inception. These are fee, implementation, tax, timing and index-construction observations, not alpha.
- Against the common S&P 500 reference, the official 2021-2025 CAGR difference is `13.76% - 14.43% = -0.67 pp`; the 2016-2025 difference is `12.16% - 14.82% = -2.66 pp`. S&P 500 TR is not RWJ's strategy benchmark.
- The sample standard deviation of the ten displayed official annual NAV returns is `19.93%`; this is an annual-row dispersion descriptor, not daily NAV volatility. Up/down years are `8 / 2`; best is 2021 `+52.93%`, worst is 2018 `-16.87%`.
- The prior direct TotalRealReturns snapshot was `28.61%` YTD through 2026-08-14; the later comparison capture is `26.53%` through 2026-08-26 and is used for the refreshed current secondary field. The Barchart `25.43%` figure is price-only through 2026-08-28, so no total-return/NAV reconciliation is inferred.

### Source-quality choice and unresolved gaps

- Invesco and SEC are the sources of truth for identity, passive classification, tracked index, official NAV/market/index performance, fee, methodology and risk disclosures. TotalRealReturns supplies only the marked current/rolling/drawdown proxy; Barchart, AAII and ETFRC supply later secondary cross-checks.
- The official factsheet now provides complete 2016-2025 calendar NAV rows, so the canonical annual table is upgraded from the former secondary proxy. Secondary annual rows remain recorded only to show the small source differences.
- Official current NAV and current official NAV YTD after the 2026-03-31 factsheet were not exposed in the reviewed Invesco text capture; current YTD and drawdown are therefore marked secondary. Official daily NAV history sufficient to independently reproduce maximum drawdown and recovery is `ไม่พบข้อมูลที่ยืนยันได้`.
- Point-in-time price, NAV, assets, holdings, yield, characteristics, rolling performance and annual performance retain separate as-of dates and are not mixed into one return series. RWJ is passive; no management-skill or alpha claim is made.

### Pre-save evidence packet / proposed durable contents

- Evidence packet includes ETF identity and exchange, return basis (`NAV Total Return`), tracked and common benchmarks, candidate claims and periods, units/currency (`%`, USD), metric definitions, separate as-of dates, source URLs/paths, calculations, reconciliation, source-quality choice, unresolved gaps and the complete planned write set.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/performance/ETF_NYSE_ARCA_RWJ Performance.md`: refresh frontmatter to 2026-08-29, use official Invesco 2026-03-31 rolling and 2016-2025 NAV rows, add official fund/index tracking differences, current secondary 2026-08-26 total-return/drawdown fields, 2026-08-28 price cross-check, risk/dispersion observations, and disclosed official-current/daily-NAV gaps; preserve the USA breadcrumb and canonical tag.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/comparisons/USA ETF.md`: update the RWJ navigation row to official rolling `12.06%`, official 2021-2025 NAV CAGR `13.76%`, and secondary current YTD `26.53%*`; preserve static navigation and add a concise source/as-of note.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/performance/ETF Performance Index.md`: update the RWJ coverage row and current refresh section to official rolling `12.06%`, official 2021-2025 CAGR `13.76%`, secondary current YTD `26.53%*`, and the annual/daily-NAV gap status; retain the separate official issuer `10.33%` field only as historical SEC context if useful.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/log.md`: append one dated `etf-performance` bullet linking `[[ETF_NYSE_ARCA_RWJ Performance]]`, `[[USA ETF]]`, `[[ETF Performance Index]]` and `[[ETF_performance_sources_2026-08-29]]`, stating official rolling `12.06%`, official 2021-2025 CAGR `13.76%`, secondary YTD `26.53%*`, and preserved current-official/daily-NAV gaps; keep the file outside the scoped commit because it already contains unrelated changes.
- No new ETF entity or region page is required; existing USA navigation remains the canonical owner and no chart is created for this item.

### Local pre-save checklist

- PASS: official NYSE Arca identity, fund name, inception, passive/index-tracking equity eligibility, canonical key, tracked index, return basis, USD units and USA region ownership are source-mapped.
- PASS: official 2026-03-31 rolling and calendar NAV/index rows, fee, holdings, characteristics, yield, secondary 2026-08-26 total-return/drawdown fields, 2026-08-28 price cross-check, cached S&P rows and each metric definition retain separate sources and as-of dates; secondary fields remain visibly marked `*`.
- PASS: official fund/index gaps, annual CAGRs, up/down counts, dispersion, common-benchmark comparison, prior/current secondary reconciliation and daily-NAV gap reproduce the proposed values; no secondary result is relabelled official and no alpha claim is made.
- PASS: complete proposed contents for RWJ performance, USA region, index, source batch and log artifacts are specified; breadcrumbs/tags/source links are preserved; no unresolved High/Medium finding blocks the write and no WARNING requiring confirmation remains.
verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official Invesco Q1 2026 factsheet and SEC evidence support the RWJ refresh; scheduled-local verification passed, current secondary fields and source-date differences are disclosed, and official current/daily-NAV gaps remain explicit.

## SCHA — Schwab U.S. Small-Cap ETF

### Workflow identity and scope

- `workflow: check-etf-performance`; `execution_profile: scheduled-inline`; `child_card_ari: ari:cloud:trello::card/workspace/6a78536437ed0b3b544c19e1/6a91776b47b6a2ddcf914270`; `parent_ari: ari:cloud:trello::card/workspace/6a78536437ed0b3b544c19e1/6a91760cdaae83b3d4afdc13`; input ticker `SCHA`; canonical `entity_key: NYSE Arca:SCHA`.
- Card was claimed and directly reread as `In Progress` before research. Primary region is `USA`; the durable graph is `[[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]`.
- This refresh updates the existing SCHA performance owner, USA navigation snapshot, master performance index, this dated source batch and one log bullet. No ETF entity page or new region page is created.

### Source map and as-of dates

| Source | URL/path | Use and as-of date |
|---|---|---|
| Schwab Asset Management official SCHA product page | https://www.schwabassetmanagement.com/products/scha | Official identity, passive classification, index, fee, current NAV/AUM/holdings/quote, yields, characteristics and July standardized NAV/market/index returns; current quote through 2026-08-26 and standardized table through 2026-07-31 |
| Schwab official ETF research performance page | https://www.schwab.wallst.com/Prospect/Research/mutualfunds/performance.asp?symbol=scha | Official daily fund-performance capture for current YTD and rolling returns through 2026-08-27; the captured table also shows Russell 2000 TR as a broad-based comparison, not SCHA’s issuer index |
| Schwab official ETF research portfolio page | https://www.schwab.wallst.com/Prospect/Research/etfs/portfolio.asp?symbol=scha | Official holdings/portfolio context and current quote; portfolio snapshot through 2026-07-31 and quote captures were separately dated |
| SEC SCHA summary prospectus | https://www.sec.gov/Archives/edgar/data/1454889/000110465925123320/tm2526338-13_497k.htm | Official objective, 90% policy, indexing strategy, small-cap risks and fund structure; prospectus dated 2025-12-22 |
| TotalRealReturns SCHA | https://totalrealreturns.com/n/SCHA | Secondary dividend-reinvested current/rolling returns, annual rows and drawdown proxy; data ending 2026-08-27 |
| S&P 500 official index page and cached workflow references | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Common USD Total Return reference for complete calendar years 2016-2025; cached convention as of 2025-12-31, dividends reinvested |
| Existing vault context | `wiki/analysis/performance/ETF_NYSE_ARCA_SCHA Performance.md`, `wiki/analysis/comparisons/USA ETF.md`, `wiki/analysis/performance/ETF Performance Index.md`, prior dated source batch | Prior SCHA page, USA ownership, secondary annual proxy and disclosed daily-NAV gap; current issuer fields are refreshed and annual proxy is retained |

### Identity and classification evidence

- Schwab identifies SCHA as `Schwab U.S. Small-Cap ETF`, ticker `SCHA`, listed on NYSE Arca, with inception `2009-11-03` and total expense ratio `0.030%` effective 2026-06-11.
- Classification is `passive-index-tracking`; the fund seeks to track the Dow Jones U.S. Small-Cap Total Stock Market Index before fees and expenses, normally investing at least 90% of assets in index securities and generally using replication with possible sampling.
- The issuer index covers companies ranked approximately 751-2,500 by full market capitalization and is float-adjusted market-cap weighted. Primary region is USA and canonical tag is `geography/United-States`.

### Candidate performance claims and raw observations

- Official Schwab ETF research daily fund-performance capture as of `2026-08-27` reports SCHA fund return YTD `22.36%`, 1-day `0.26%`, 1-month `2.27%`, 3-month `2.41%`, 1-year `29.05%`, 3-year annualized `18.86%`, 5-year annualized `7.95%`, and 10-year annualized `10.78%`. The capture's comparison row is Russell 2000 TR USD; it is not substituted for SCHA's Dow Jones issuer index.
- Official Schwab product-page standardized snapshot as of `2026-07-31` reports SCHA NAV YTD `18.27%`, 1-year `31.71%`, 3-year annualized `14.88%`, 5-year `7.25%`, 10-year `10.48%`, inception `12.31%`; market-price returns are `18.33%`, `31.88%`, `14.92%`, `7.26%`, `10.50%`, `12.32%`; Dow Jones index returns are `18.23%`, `31.65%`, `14.83%`, `7.19%`, `10.43%` for the comparable fields.
- Official current Schwab product-page fields as of `2026-08-26` are NAV `US$34.69`, previous close `US$34.71`, bid/ask midpoint `US$34.69`, total net assets `US$23,000,233,279.50`, and `1,710` holdings. The 30-day median bid/ask spread is `0.03%`; SEC yield is `1.02%` as of 2026-08-25 and TTM distribution yield is `1.07%` as of 2026-07-31.
- Official characteristics as of `2026-07-31` are weighted average market capitalization `US$13.61B`, P/E `19.05`, P/CF `11.21`, ROE `4.30%`, P/B `2.48`, 3-year beta `1.00`, 3-year standard deviation `19.78%`, and portfolio turnover `13.99%`.
- Official product-page risk fields report best three-month return `+33.21%` and worst three-month return `-31.61%`; these are not maximum-drawdown measures. Recent verified distributions are `US$0.1004` ex/pay 2026-06-24/2026-06-29 and `US$0.0384` ex/pay 2026-03-25/2026-03-30.
- Latest accessible secondary TotalRealReturns data ending `2026-08-27` reports total return YTD `22.60%`, 1Y `28.50%`, 2Y `40.79%` (`18.66%` annualized), 3Y `68.20%` (`18.93%` annualized), 5Y `43.22%` (`7.45%` annualized), and 10Y `178.94%` (`10.80%` annualized). Its current drawdown proxy is `-3.76%` on 2026-08-27 from the 2026-06-30 peak; worst drawdown is `-42.41%` on 2020-03-23 from the 2020-01-16 peak.
- Secondary annual total-return rows from the same source are 2016 `19.98%`, 2017 `14.94%`, 2018 `-11.76%`, 2019 `26.50%`, 2020 `19.34%`, 2021 `16.45%`, 2022 `-19.81%`, 2023 `18.46%`, 2024 `11.16%`, and 2025 `11.60%`; these are dividend-reinvested proxy observations, not issuer-published calendar NAV rows.
- Cached S&P 500 TR rows are 2016 `11.96%`, 2017 `21.83%`, 2018 `-4.38%`, 2019 `31.49%`, 2020 `18.40%`, 2021 `28.71%`, 2022 `-18.11%`, 2023 `26.29%`, 2024 `25.02%`, and 2025 `17.88%`; USD, dividends reinvested, as of `2025-12-31`.

### Calculations and reconciliation

- Secondary 2016-2025 rows compound to `152.0962%`, displayed as `152.10%*`; rounded-input CAGR is `(1 + 1.520962)^(1/10) - 1 = 9.69%*`. Secondary 2021-2025 rows compound to `37.2285%`, displayed as `37.23%*`; rounded-input CAGR is `6.53%*`.
- Cached S&P 500 TR compounds to `298.3291%` / CAGR `14.82%` over 2016-2025 and `96.1696%` / CAGR `14.43%` over 2021-2025. The secondary SCHA CAGR differences are `9.69% - 14.82% = -5.13 pp` and `6.53% - 14.43% = -7.90 pp`; these are common-reference comparisons, not alpha.
- Up/down years are `8 / 2`; best is 2019 `+26.50%*`, least positive is 2025 `+11.60%*`, worst is 2022 `-19.81%*`, and least-bad down year is 2018 `-11.76%*`.
- Official July product-page NAV-minus-Dow-Jones-index differences are `+0.04 pp` YTD, `+0.06 pp` 1Y, `+0.05 pp` 3Y, `+0.06 pp` 5Y and `+0.05 pp` 10Y. These small differences reflect fee, sampling, implementation, timing and index-construction effects; they are not alpha.
- Official daily Schwab YTD `22.36%` as of 2026-08-27, official July monthly NAV YTD `18.27%`, and secondary TotalRealReturns YTD `22.60%` as of 2026-08-27 are retained as separate observations because the source captures and return conventions differ. No synchronized S&P 500 current-year spread is inferred.

### Source-quality choice and unresolved gaps

- Schwab Asset Management and the SEC are the sources of truth for identity, passive classification, issuer index, official current NAV/quote, official rolling performance, fee, holdings, characteristics, yields, distributions and risk language. TotalRealReturns supplies only the marked annual/current/rolling/drawdown proxy.
- Official issuer text exposes current and rolling fields but not a complete 2016-2025 calendar NAV table in the reviewed capture; the annual table therefore remains secondary and visibly marked `*`.
- Official daily NAV history sufficient to independently reproduce maximum drawdown and recovery is `ไม่พบข้อมูลที่ยืนยันได้`; the TotalRealReturns drawdown values are not promoted to official NAV claims.
- Point-in-time NAV, price, AUM, holdings, yield, characteristics, standardized performance, daily performance and annual proxy retain separate as-of dates. SCHA is passive; no management-skill or alpha claim is made.

### Pre-save evidence packet / proposed durable contents

- Evidence packet includes ETF identity and exchange, return basis (`NAV Total Return`), issuer and common benchmarks, candidate claims and periods, units/currency (`%`, USD), metric definitions, separate as-of dates, source URLs/paths, calculations, reconciliation, source-quality choice, unresolved gaps and the complete planned write set.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/performance/ETF_NYSE_ARCA_SCHA Performance.md`: refresh frontmatter to 2026-08-29, add official current Schwab daily YTD/rolling fields and 2026-08-26 NAV/asset/holdings snapshot, preserve the separate July standardized issuer-index table, update secondary annual/current/drawdown proxy rows, retain distributions and risk fields, and disclose official daily-NAV gaps; preserve USA breadcrumb and tag.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/comparisons/USA ETF.md`: update the SCHA row to official rolling `10.78%`, secondary 2021-2025 CAGR `6.53%*`, and official daily current YTD `22.36%`; preserve static navigation and add a concise source/as-of note.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/performance/ETF Performance Index.md`: update the SCHA coverage row and dated refresh section to official rolling `10.78%`, secondary 2016-2025/2021-2025 values, official YTD `22.36%`, and the annual/daily-NAV gap status.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/log.md`: append one dated `etf-performance` bullet linking `[[ETF_NYSE_ARCA_SCHA Performance]]`, `[[USA ETF]]`, `[[ETF Performance Index]]` and `[[ETF_performance_sources_2026-08-29]]`, stating official rolling `10.78%`, official YTD `22.36%`, secondary 2021-2025 CAGR `6.53%*`, and preserved annual/daily-NAV gaps; keep the file outside the scoped commit because it already contains unrelated changes.
- No new ETF entity or region page is required; existing USA navigation remains the canonical owner and no chart is created for this item.

### Local pre-save checklist

- PASS: official NYSE Arca identity, fund name, inception, passive/index-tracking equity eligibility, canonical key, issuer index, return basis, USD units and USA region ownership are source-mapped.
- PASS: official 2026-08-27 daily return fields, July issuer-index standardized table, August-26 quote/NAV/AUM/holdings snapshot, characteristics/yields/distributions/risk fields, secondary annual/current/drawdown observations, cached S&P rows and all metric definitions retain separate sources and as-of dates; secondary fields remain marked `*`.
- PASS: annual/CAGR/up-down calculations, official fund-index differences, current-YTD source reconciliation, common-benchmark context and daily-NAV gap reproduce the proposed values; no secondary result is relabelled official and no alpha claim is made.
- PASS: complete proposed contents for SCHA performance, USA region, index, source batch and log artifacts are specified; breadcrumbs/tags/source links are preserved; no unresolved High/Medium finding blocks the write and no WARNING requiring confirmation remains.
verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official Schwab current/July evidence and SEC methodology support the SCHA refresh; scheduled-local verification passed, secondary annual/current drawdown fields and separate as-of conflicts are disclosed, and official daily-NAV gaps remain explicit.

## SLYG — State Street SPDR S&P 600 Small Cap Growth ETF

### Workflow identity and scope

- `workflow: check-etf-performance`; `execution_profile: scheduled-inline`; `child_card_ari: ari:cloud:trello::card/workspace/6a78536437ed0b3b544c19e1/6a91776e8cfa535e289bd503`; `parent_ari: ari:cloud:trello::card/workspace/6a78536437ed0b3b544c19e1/6a91760cdaae83b3d4afdc13`; input ticker `SLYG`; canonical `entity_key: NYSE Arca:SLYG`.
- Card was claimed and directly reread as `In Progress` before research. Primary region is USA; the durable graph is `[[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]`.
- This refresh updates the existing SLYG performance owner, USA navigation snapshot, master performance index, this dated source batch and one log bullet. No ETF entity or new region page is created.

### Source map and as-of dates

| Source | URL/path | Use and as-of date |
|---|---|---|
| State Street official SLYG product page | https://www.ssga.com/us/en/individual/etfs/state-street-spdr-sp-600-small-cap-growth-etf-slyg | Official identity, NYSE Arca listing, inception, benchmark, fee, current NAV/price/AUM/holdings/characteristics/yields and standardized performance; current snapshot through 2026-08-26/27 and standardized performance through 2026-07-31 |
| State Street official SLYG factsheet | https://www.ssga.com/library-content/products/factsheets/etfs/us/factsheet-us-en-slyg.pdf | Official passive/index approach, return-basis and risk context; reviewed factsheet is dated 2026-03-31 |
| Schwab official ETF performance page | https://www.schwab.wallst.com/Prospect/Research/etfs/performance.asp?symbol=slyg | Independent official-distributor display of SLYG NAV/market total returns and S&P 500 comparison; latest captured standardized table is 2026-07-31 |
| AAII SLYG profile | https://www.aaii.com/etf/ticker/SLYG | Secondary NAV annual and trailing-return cross-check; data as of 2026-07-31 |
| YTDReturn SLYG | https://www.ytdreturn.com/slyg/ | Secondary dividend-reinvested current YTD cross-check; data ending 2026-08-26 |
| S&P 500 official index page and cached workflow references | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Common USD Total Return reference for complete calendar years 2016-2025; cached convention as of 2025-12-31 |
| Existing vault context | `wiki/analysis/performance/ETF_NYSE_ARCA_SLYG Performance.md`, `wiki/analysis/comparisons/USA ETF.md`, `wiki/analysis/performance/ETF Performance Index.md`, prior dated source batch | Prior SLYG page, USA ownership, secondary annual proxy, calculations and disclosed gaps; current official July fields and August snapshot are refreshed |

### Identity and classification evidence

- State Street identifies SLYG as `State Street SPDR S&P 600 Small Cap Growth ETF`, ticker `SLYG`, listed on NYSE Arca, with inception `2000-09-25`, USD base currency, quarterly distributions and gross expense ratio `0.15%`.
- SLYG is a passive/index-tracking U.S. small-cap growth equity ETF. The tracked issuer benchmark is the `S&P SmallCap 600 Growth Index`, which selects growth characteristics using sales growth, earnings change to price and momentum and is float-adjusted market-cap weighted. The issuer page notes the linked benchmark history uses the Dow Jones U.S. Small-Cap Growth Total Stock Market Index through 2010-12-16 and S&P SmallCap 600 Growth Index from 2010-12-17.
- Primary region is USA and the canonical tag is `geography/United-States`. S&P 500 TR remains a common large-cap reference only, not SLYG's tracked index.

### Candidate performance claims and raw observations

- Official State Street standardized performance as of `2026-07-31`: NAV `-3.27%` 1M, `-3.27%` QTD, `22.77%` YTD, `30.23%` 1Y, `13.78%` 3Y annualized, `6.55%` 5Y, `10.97%` 10Y and `7.40%` since inception. Market-value returns are `-3.28%`, `-3.28%`, `22.78%`, `30.28%`, `13.77%`, `6.56%`, `10.98%` and `7.40%`; linked index returns are `-3.27%`, `-3.27%`, `22.89%`, `30.43%`, `13.94%`, `6.69%`, `11.13%` and `8.36%`.
- Official State Street current snapshot as of `2026-08-26` reports NAV `US$115.64`, market close `US$115.70`, bid/ask midpoint `US$115.66`, assets under management `US$5,088.35M`, and `351` fund holdings. Fund characteristics are P/B `3.11`, FY1 P/E `19.16`, weighted average market cap `US$5,090.10M` and estimated 3-5 year EPS growth `14.06%`; yields are SEC `0.75%` as of 2026-08-25 and fund distribution yield `0.66%`.
- The official State Street page does not expose complete 2016-2025 calendar NAV rows in the reviewed text capture. The existing secondary dividend-reinvested proxy remains: 2016 `22.16%`, 2017 `14.53%`, 2018 `-4.19%`, 2019 `20.98%`, 2020 `19.48%`, 2021 `22.42%`, 2022 `-21.26%`, 2023 `17.27%`, 2024 `9.38%`, 2025 `5.19%`.
- The latest secondary YTD cross-check reports SLYG total return `23.31%` with dividends reinvested through `2026-08-26`; it is not substituted for the latest official month-end NAV field because the windows and source basis differ. AAII independently rounds the July official/secondary calendar and trailing fields to 22.8% YTD and 11.0% 10-year annualized.
- Cached S&P 500 TR rows are 2016 `11.96%`, 2017 `21.83%`, 2018 `-4.38%`, 2019 `31.49%`, 2020 `18.40%`, 2021 `28.71%`, 2022 `-18.11%`, 2023 `26.29%`, 2024 `25.02%` and 2025 `17.88%`; USD, dividends reinvested, as of `2025-12-31`.

### Calculations and reconciliation

- The existing secondary SLYG rows compound to `152.01%` over 2016-2025; rounded-input CAGR is `(1 + 1.5201)^(1/10) - 1 = 9.68%*`. The 2021-2025 rows compound to `30.06%`, with rounded-input CAGR `5.40%*`.
- The cached S&P 500 TR compounds to `298.33%` / CAGR `14.82%` over 2016-2025 and `96.17%` / CAGR `14.43%` over 2021-2025. The arithmetic common-reference differences are `-5.14 pp` and `-9.03 pp`; these are not alpha and S&P 500 TR is not SLYG's strategy benchmark.
- Official State Street fund-minus-linked-index differences from the July table are `-0.12 pp` YTD, `-0.20 pp` 1Y, `-0.16 pp` 3Y, `-0.11 pp` 5Y, `-0.16 pp` 10Y and `-0.96 pp` since inception. These reflect fees, implementation, timing and index-linkage effects, not manager skill.
- Proxy up/down years are `8 / 2`; best proxy year is 2021 `+22.42%*`, worst is 2022 `-21.26%*`, and the ten-row sample standard deviation is retained from the prior source context as annual-row dispersion rather than official daily NAV volatility.

### Source-quality choice and unresolved gaps

- State Street and its official factsheet are the sources of truth for identity, passive classification, tracked index, fee, official standardized performance, current fund facts and risk framing. Schwab, AAII and YTDReturn are secondary cross-checks only; secondary calendar/current fields remain visibly marked `*`.
- The latest official standardized return window is July month-end, while the current quote/fund facts are August 26-27. The secondary `23.31%` YTD through August 26 is retained as a later total-return context field, not blended with the official July `22.77%` NAV YTD.
- Official daily NAV history sufficient to reproduce maximum drawdown and recovery is `ไม่พบข้อมูลที่ยืนยันได้`; no unsupported drawdown number is saved. Point-in-time NAV, price, AUM, holdings, yields, characteristics and performance retain separate as-of dates.
- SLYG is passive; no management-skill or alpha claim is made.

### Pre-save evidence packet / proposed durable contents

- Evidence packet includes ETF identity and exchange, return basis (`NAV Total Return`), issuer and common benchmarks, candidate performance claims and periods, units/currency (`%`, USD), definitions, separate as-of dates, source URLs/paths, calculations, reconciliation, source-quality choice, unresolved gaps and the complete planned write set.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/performance/ETF_NYSE_ARCA_SLYG Performance.md`: refresh frontmatter to 2026-08-29, use official July rolling/YTD table and August-26 current fund snapshot, retain secondary annual/current proxy fields, update tracking-gap and source/as-of notes, preserve USA breadcrumb and canonical tag.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/comparisons/USA ETF.md`: update SLYG to official rolling `10.97%`, secondary 2021-2025 CAGR `5.40%*`, official July YTD `22.77%`, and a concise July/August source-as-of note.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/performance/ETF Performance Index.md`: update the SLYG coverage row and dated refresh section to official rolling `10.97%`, secondary 2016-2025/2021-2025 values, official July YTD `22.77%`, and annual/daily-NAV gap status.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/log.md`: append one dated `etf-performance` bullet linking `[[ETF_NYSE_ARCA_SLYG Performance]]`, `[[USA ETF]]`, `[[ETF Performance Index]]` and `[[ETF_performance_sources_2026-08-29]]`, stating official rolling `10.97%`, official YTD `22.77%`, secondary 2021-2025 CAGR `5.40%*`, and preserved annual/daily-NAV gaps; keep outside the scoped commit because `log.md` already contains unrelated changes.
- No new ETF entity or region page is required; existing USA navigation remains the canonical owner and no chart is created for this item.

### Local pre-save checklist

- PASS: official NYSE Arca identity, fund name, inception, passive/index-tracking equity eligibility, canonical key, tracked index, return basis, USD units and USA region ownership are source-mapped.
- PASS: official July standardized NAV/market/index fields, August-26/27 NAV/price/AUM/holdings/characteristics/yields, secondary annual/current fields, cached S&P rows and metric definitions retain separate sources and as-of dates; secondary values remain marked `*`.
- PASS: annual/CAGR/up-down calculations, official fund-index differences, July-versus-August current-YTD reconciliation, common-benchmark context and daily-NAV gap reproduce the proposed values; no secondary result is relabelled official and no alpha claim is made.
- PASS: complete proposed contents for SLYG performance, USA region, index, source batch and log artifacts are specified; breadcrumbs/tags/source links are preserved; no unresolved High/Medium finding blocks the write and no WARNING requiring confirmation remains.
verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official State Street July performance and August fund-fact evidence support the SLYG refresh; scheduled-local verification passed, secondary annual/current fields and separate as-of windows are disclosed, and official daily-NAV drawdown data remains unavailable.

## SLYV — State Street SPDR S&P 600 Small Cap Value ETF

### Workflow identity and scope

- `workflow: check-etf-performance`; `execution_profile: scheduled-inline`; `child_card_ari: ari:cloud:trello::card/workspace/6a78536437ed0b3b544c19e1/6a91777155fda1b1f85c9d82`; `parent_ari: ari:cloud:trello::card/workspace/6a78536437ed0b3b544c19e1/6a91760cdaae83b3d4afdc13`; input ticker `SLYV`; canonical `entity_key: NYSE Arca:SLYV`.
- Card was claimed and directly reread as `In Progress` before research. Primary region is USA; the durable graph is `[[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]`.
- This refresh updates the existing SLYV performance owner, USA navigation snapshot, master performance index, this dated source batch and one log bullet. No ETF entity or new region page is created.

### Source map and as-of dates

| Source | URL/path | Use and as-of date |
|---|---|---|
| State Street official SLYV product page | https://www.ssga.com/us/en/individual/etfs/state-street-spdr-sp-600-small-cap-value-etf-slyv | Official identity, NYSE Arca listing, inception, benchmark, fee, current NAV/AUM/price/holdings/characteristics/yields, risk and standardized performance; current fund facts through 2026-08-27/28 and standardized performance through 2026-07-31 |
| State Street official SLYV factsheet | https://www.ssga.com/library-content/products/factsheets/etfs/us/factsheet-us-en-slyv.pdf | Official return basis, passive sampling approach, holdings/sector context and fund methodology; reviewed factsheet is dated 2026-03-31 |
| SEC-hosted SLYV summary prospectus | https://www.sec.gov/Archives/edgar/data/1064642/000119312524242957/R25.htm | Official passive strategy, value/small-cap risks and annual NAV rows through 2023 |
| ETFReplay SLYV history | https://www.etfreplay.com/etf/slyv | Secondary standardized total-return rows for 2024-2025 and prior source context |
| TotalRealReturns SLYV | https://totalrealreturns.com/n/SLYV | Secondary dividend-reinvested current YTD/rolling/drawdown corroboration; latest data ending 2026-08-27 |
| YTDReturn SLYV | https://www.ytdreturn.com/slyv/ | Secondary dividend-reinvested YTD cross-check through 2026-08-26 |
| S&P 500 official index page and cached workflow references | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Common USD Total Return reference for complete calendar years 2016-2025; cached convention as of 2025-12-31 |
| Existing vault context | `wiki/analysis/performance/ETF_NYSE_ARCA_SLYV Performance.md`, `wiki/analysis/comparisons/USA ETF.md`, `wiki/analysis/performance/ETF Performance Index.md`, prior dated source batch | Prior SLYV page, USA ownership, official 2016-2023 rows, secondary 2024-2025 rows, calculations and disclosed gaps; current official July/August fields are refreshed |

### Identity and classification evidence

- State Street identifies SLYV as `State Street SPDR S&P 600 Small Cap Value ETF`, ticker `SLYV`, listed on NYSE Arca, with inception `2000-09-25`, USD base currency, quarterly distributions and gross expense ratio `0.15%`.
- SLYV is a passive/index-tracking U.S. small-cap value equity ETF using representative sampling. The tracked issuer benchmark is the `S&P SmallCap 600 Value Index`, whose constituents exhibit value characteristics based on book value to price, earnings to price and sales to price. The issuer page links the predecessor Dow Jones U.S. Small-Cap Value Total Stock Market Index through 2010-12-16 and the S&P SmallCap 600 Value Index from 2010-12-17.
- Primary region is USA and the canonical tag is `geography/United-States`. S&P 500 TR remains a common large-cap reference only, not SLYV's tracked index.

### Candidate performance claims and raw observations

- Official State Street standardized performance as of `2026-07-31`: NAV `-0.56%` 1M, `-0.56%` QTD, `20.17%` YTD, `36.94%` 1Y, `12.35%` 3Y annualized, `7.98%` 5Y, `10.06%` 10Y and `10.77%` since inception. Market-value returns are `-0.59%`, `-0.59%`, `20.17%`, `36.98%`, `12.34%`, `7.99%`, `10.05%` and `10.78%`; linked index returns are `-0.55%`, `-0.55%`, `20.27%`, `37.16%`, `12.50%`, `8.14%`, `10.19%` and `10.47%`.
- Official State Street current snapshot as of `2026-08-27` reports NAV `US$110.06`, market close `US$110.07`, bid/ask midpoint `US$110.09`, AUM `US$5,046.52M` and `461` fund holdings. Fund characteristics are P/B `1.55`, FY1 P/E `12.67`, weighted average market cap `US$4,111.42M` and estimated 3-5 year EPS growth `16.28%`; yields are SEC `1.92%` and fund distribution yield `1.80%` as of 2026-08-26.
- The official SEC annual table exposes 2016-2023 NAV rows: 2016 `31.14%`, 2017 `11.45%`, 2018 `-12.69%`, 2019 `24.31%`, 2020 `2.60%`, 2021 `30.66%`, 2022 `-11.13%` and 2023 `14.71%`. Secondary standardized observations supply 2024 `7.28%*` and 2025 `6.52%*`; they remain marked `*` and are corroborated by TotalRealReturns.
- Latest secondary TotalRealReturns data ending `2026-08-27` reports total-return YTD `22.15%`, 1Y `27.42%`, since-inception cumulative `1,251.91%` / annualized `10.57%`, and current drawdown `-1.92%` from the 2026-08-14 total-return high. YTDReturn independently reports `22.10%` through 2026-08-26. These are secondary contexts and are not substituted for official July NAV YTD.
- Official current sector snapshot as of `2026-08-27`: Financials `21.66%`, Consumer Discretionary `15.63%`, Industrials `14.54%`, Information Technology `10.77%`, Energy `7.17%`, Real Estate `6.95%`, Health Care `6.78%`, Materials `5.75%`, Consumer Staples `4.63%`, Communication Services `3.91%` and Utilities `2.21%`.
- Cached S&P 500 TR rows are 2016 `11.96%`, 2017 `21.83%`, 2018 `-4.38%`, 2019 `31.49%`, 2020 `18.40%`, 2021 `28.71%`, 2022 `-18.11%`, 2023 `26.29%`, 2024 `25.02%` and 2025 `17.88%`; USD, dividends reinvested, as of `2025-12-31`.

### Calculations and reconciliation

- The displayed SLYV rows compound to `147.7318%` over 2016-2025, displayed as `147.73%`; rounded-input CAGR is `(1 + 1.477318)^(1/10) - 1 = 9.50%`. The 2021-2025 compound is `52.2121%`, displayed as `52.21%`, with rounded-input CAGR `8.77%`; both calculations include secondary 2024-2025 rows and therefore retain the source-quality caveat.
- Cached S&P 500 TR compounds to `298.33%` / CAGR `14.82%` over 2016-2025 and `96.17%` / CAGR `14.43%` over 2021-2025. The common-reference CAGR differences are `-5.32 pp` and `-5.66 pp`; these are not alpha and S&P 500 TR is not SLYV's strategy benchmark.
- Official State Street fund-minus-linked-index differences from the July table are `-0.10 pp` YTD, `-0.22 pp` 1Y, `-0.15 pp` 3Y, `-0.16 pp` 5Y, `-0.13 pp` 10Y and `+0.30 pp` since inception. These reflect fees, sampling, implementation, timing and benchmark-linkage effects, not manager skill.
- Up/down years are `8 / 2`; best row is 2016 `+31.14%`, worst is 2018 `-12.69%`. Official daily-NAV volatility is not disclosed in the reviewed source set; the annual rows are not converted into a daily risk statistic.

### Source-quality choice and unresolved gaps

- State Street, the official factsheet and SEC prospectus are the sources of truth for identity, passive classification, tracked index, fee, methodology, official standardized performance and risk framing. ETFReplay, TotalRealReturns and YTDReturn are secondary cross-checks only; 2024-2025 calendar rows and current secondary fields remain visibly marked `*`.
- The latest official standardized return window is July month-end, while current NAV/AUM/holdings/sector facts are August 27 and current secondary total return ends August 27. These windows are retained separately; no same-date official NAV YTD is inferred after July.
- Official daily NAV history sufficient to reproduce maximum drawdown and recovery is `ไม่พบข้อมูลที่ยืนยันได้`; the secondary current drawdown is retained only as labeled context and is not used in ranking calculations.
- Point-in-time NAV, price, AUM, holdings, yields, characteristics, sectors and performance retain separate as-of dates. SLYV is passive; no management-skill or alpha claim is made.

### Pre-save evidence packet / proposed durable contents

- Evidence packet includes ETF identity and exchange, return basis (`NAV Total Return`), issuer and common benchmarks, candidate performance claims and periods, units/currency (`%`, USD), definitions, separate as-of dates, source URLs/paths, calculations, reconciliation, source-quality choice, unresolved gaps and the complete planned write set.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/performance/ETF_NYSE_ARCA_SLYV Performance.md`: refresh frontmatter to 2026-08-29, use official July rolling/YTD table and August-27 current fund snapshot, preserve official 2016-2023 and secondary 2024-2025 annual rows, add current secondary YTD/drawdown context, update sector/risk and source/as-of notes, and preserve USA breadcrumb/tag.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/comparisons/USA ETF.md`: update SLYV to official rolling `10.06%`, official July YTD `20.17%`, secondary 2021-2025 CAGR `8.77%`, and a concise July/August source-as-of note.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/performance/ETF Performance Index.md`: update the SLYV coverage row and dated refresh section to official rolling `10.06%`, official July YTD `20.17%`, existing annual-window values, and the current secondary/daily-NAV gap status.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/log.md`: append one dated `etf-performance` bullet linking `[[ETF_NYSE_ARCA_SLYV Performance]]`, `[[USA ETF]]`, `[[ETF Performance Index]]` and `[[ETF_performance_sources_2026-08-29]]`, stating official rolling `10.06%`, official YTD `20.17%`, secondary 2021-2025 CAGR `8.77%`, current secondary YTD `22.15%*`, and preserved annual/daily-NAV gaps; keep outside the scoped commit because `log.md` already contains unrelated changes.
- No new ETF entity or region page is required; existing USA navigation remains the canonical owner and no chart is created for this item.

### Local pre-save checklist

- PASS: official NYSE Arca identity, fund name, inception, passive/index-tracking equity eligibility, canonical key, tracked index, return basis, USD units and USA region ownership are source-mapped.
- PASS: official July standardized NAV/market/index fields, August-27 NAV/AUM/price/holdings/sector/characteristics/yields, SEC/secondary annual rows, current secondary YTD/drawdown, cached S&P rows and metric definitions retain separate sources and as-of dates; secondary values remain marked `*` where applicable.
- PASS: annual/CAGR/up-down calculations, official fund-index differences, official-versus-secondary current-YTD reconciliation, common-benchmark context and daily-NAV gap reproduce the proposed values; no secondary result is relabelled official and no alpha claim is made.
- PASS: complete proposed contents for SLYV performance, USA region, index, source batch and log artifacts are specified; breadcrumbs/tags/source links are preserved; no unresolved High/Medium finding blocks the write and no WARNING requiring confirmation remains.
verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official State Street July performance and August-27 fund-fact evidence support the SLYV refresh; scheduled-local verification passed, official/secondary annual and current as-of differences are disclosed, and official daily-NAV drawdown data remains unavailable.

## VIOG — Vanguard S&P Small-Cap 600 Growth ETF

### Workflow identity and scope

- `workflow: check-etf-performance`; `execution_profile: scheduled-inline`; `child_card_ari: ari:cloud:trello::card/workspace/6a78536437ed0b3b544c19e1/6a917773d3aa1eb451e4e5dc`; `parent_ari: ari:cloud:trello::card/workspace/6a78536437ed0b3b544c19e1/6a91760cdaae83b3d4afdc13`; input ticker `VIOG`; canonical `entity_key: NYSE Arca:VIOG`.
- Card was claimed and directly reread as `In Progress` before research. Primary region is USA; the durable graph is `[[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]`.
- This refresh updates the existing VIOG performance owner, USA navigation snapshot, master performance index, this dated source batch and one log bullet. No ETF entity or new region page is created.

### Source map and as-of dates

| Source | URL/path | Use and as-of date |
|---|---|---|
| Vanguard advisor VIOG page | https://advisors.vanguard.com/investments/products/viog/vanguard-sp-small-cap-600-growth-etf | Official fund identity, tracked index, current NAV TR YTD and standardized performance table; current YTD `23.25%` as of 2026-08-26 and table through 2026-07-31 |
| Vanguard VIOG investor page | https://investor.vanguard.com/investment-products/etfs/profile/viog | Official product context and issuer identity; dynamic fields cross-checked during research |
| Vanguard ETF fund list | https://workplace.vanguard.com/fund-list/?filters=etf | Official distributor cross-check; a separate July YTD snippet displayed `25.41%`, which conflicts with the VIOG-specific advisor table and is retained as an unresolved source conflict |
| Vanguard VIOG fact sheet | https://workplace.vanguard.com/assets/corp/fund_communications/pdf_publish/us-products/fact-sheet/F3347.pdf | Official passive/full-replication approach, return basis, inception, expense ratio, exchange, holdings, standard deviation, turnover, sector snapshot and NAV/index performance; factsheet dated 2026-06-30 |
| Vanguard S&P ETF prospectus | https://fund-docs.vanguard.com/p3340.pdf | Official strategy/risk context and VIOG annual NAV total-return rows through 2024 |
| Schwab VIOG performance page | https://www.schwab.wallst.com/Prospect/Research/etfs/performance.asp?symbol=viog | Official distributor cross-check for price and July rolling/YTD fields; price `149.14` as of 2026-08-26 and rounded July performance fields |
| Yahoo Finance VIOG performance history | https://uk.finance.yahoo.com/quote/VIOG/performance/ | Secondary cross-check for the complete-year 2025 total-return row |
| ETFReplay VIOG return table | https://www.etfreplay.com/etf/viog | Secondary corroboration for the 2025 complete-year total-return row `5.40%` |
| S&P 500 official index page and cached workflow references | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Common USD Total Return reference for complete calendar years 2016-2025; cached convention as of 2025-12-31 |
| Existing vault context | `wiki/analysis/performance/ETF_NYSE_ARCA_VIOG Performance.md`, `wiki/analysis/comparisons/USA ETF.md`, `wiki/analysis/performance/ETF Performance Index.md`, prior dated source batch | Prior VIOG page, USA ownership, official 2016-2024 rows, secondary 2025 row, calculations and disclosed gaps; current official Vanguard fields are refreshed |

### Identity and classification evidence

- Vanguard identifies VIOG as `Vanguard S&P Small-Cap 600 Growth ETF`, ticker `VIOG`, listed on NYSE Arca, with inception `2010-09-07`, USD base currency, quarterly distributions and expense ratio `0.10%`.
- VIOG is a passive/index-tracking U.S. small-cap growth equity ETF using full replication. The tracked issuer benchmark is the `S&P SmallCap 600 Growth Index`; S&P 500 TR remains a common large-cap reference only, not VIOG's strategy benchmark.
- The official advisor page displayed an erroneous future inception metadata value, while the factsheet and prospectus corroborate `2010-09-07`; the corroborated date is used.
- Primary region is USA and the canonical tag is `geography/United-States`.

### Candidate performance claims and raw observations

- Official Vanguard advisor page current field as of `2026-08-26`: NAV total-return YTD `23.25%`. The same page's standardized table as of `2026-07-31` reports NAV `-3.28%` 1M, `22.82%` YTD, `30.32%` 1Y, `13.80%` 3Y annualized, `6.54%` 5Y, `10.98%` 10Y and `12.92%` since inception; its benchmark cells are blank in the reviewed capture.
- Official Vanguard factsheet as of `2026-06-30` reports NAV `23.62%` YTD, `26.98%` 1Y, `35.51%` 3Y, `16.96%` 5Y, `11.89%` 10Y and `13.23%` since inception. The linked-index fields are `23.66%`, `27.05%`, `35.62%`, `17.10%`, `12.05%` and `13.41%`, respectively; market-value fields are `23.45%`, `26.92%`, `35.27%`, `16.94%`, `7.22%`, `11.89%` and `13.22%`.
- Official fund facts include `348` holdings, median market cap `$5.0B`, P/E `22.6`, P/B `3.4`, earnings growth `14.0%`, turnover `47.6%` and standard deviation `19.41%` as of 2026-06-30; net assets were `$1,087M` at that date and approximately `$1.1B` on the July advisor snapshot. The advisor page also reports a `0.91%` dividend yield and `0.000%` 30-day bid/ask spread as of 2026-08-26.
- Schwab's official distributor page independently rounds July VIOG NAV/market YTD to `22.8%`/`22.7%`, 1Y `30.3%`, 3Y `13.8%`, 5Y `6.5%` and since inception `12.9%`; it reports a market close of `$149.14` as of 2026-08-26. These are cross-checks, not replacements for Vanguard's issuer fields.
- Official Vanguard annual NAV rows are available through 2024: 2016 `22.01%`, 2017 `14.58%`, 2018 `-4.18%`, 2019 `20.95%`, 2020 `19.48%`, 2021 `22.46%`, 2022 `-21.22%`, 2023 `16.95%` and 2024 `9.44%`. Secondary standardized total-return data supplies 2025 `5.40%*` to complete the comparison window.
- Cached S&P 500 TR rows are 2016 `11.96%`, 2017 `21.83%`, 2018 `-4.38%`, 2019 `31.49%`, 2020 `18.40%`, 2021 `28.71%`, 2022 `-18.11%`, 2023 `26.29%`, 2024 `25.02%` and 2025 `17.88%`; USD, dividends reinvested, as of `2025-12-31`.

### Calculations and reconciliation

- The displayed VIOG rows compound to `151.94%` over 2016-2025; rounded-input CAGR is `(1 + 1.5194)^(1/10) - 1 = 9.68%`. The 2021-2025 rows compound to `30.14%`, with rounded-input CAGR `5.41%`; both include the secondary 2025 row and retain that caveat.
- Cached S&P 500 TR compounds to `298.33%` / CAGR `14.82%` over 2016-2025 and `96.17%` / CAGR `14.43%` over 2021-2025. The common-reference CAGR differences are `-5.14 pp` and `-9.03 pp`; these are not alpha and S&P 500 TR is not VIOG's strategy benchmark.
- Official June factsheet fund-minus-linked-index differences are `-0.04 pp` YTD, `-0.07 pp` 1Y, `-0.11 pp` 3Y, `-0.14 pp` 5Y, `-0.16 pp` 10Y and `-0.18 pp` since inception. These reflect fees and implementation/timing effects, not manager skill.
- Up/down years are `8 / 2`; best row is 2021 `+22.46%`, worst is 2022 `-21.22%`. Official daily-NAV volatility, maximum drawdown and recovery dates are not disclosed in the reviewed source set.

### Source-quality choice and unresolved gaps

- Vanguard issuer materials and the prospectus are the sources of truth for identity, passive classification, tracked index, fee, official standardized performance and risk framing. Schwab, Yahoo Finance and ETFReplay are cross-checks only; the 2025 calendar row remains marked `*`.
- Current official YTD fields are dated 2026-08-26 (`23.25%`), 2026-07-31 (`22.82%`) and 2026-06-30 (`23.62%`); they are separate windows, and the latest dated VIOG-specific advisor field is used. The separate Vanguard workplace fund-list snippet showing July `25.41%` conflicts with the advisor table; it is not used without a resolved field mapping.
- The advisor page's future inception metadata is rejected in favor of the corroborated 2010-09-07 factsheet/prospectus date. Its July benchmark cells are blank, so June factsheet index fields are used for the available fund-index reconciliation.
- Official daily NAV history sufficient to reproduce maximum drawdown and recovery is `ไม่พบข้อมูลที่ยืนยันได้`; no numeric secondary drawdown proxy is saved. Point-in-time price, AUM, holdings, yield, risk and performance retain separate as-of dates.

### Pre-save evidence packet / proposed durable contents

- Evidence packet includes ETF identity and exchange, return basis (`NAV Total Return`), issuer and common benchmarks, candidate claims and periods, units/currency (`%`, USD), definitions, separate as-of dates, source URLs/paths, calculations, reconciliation, source-quality choice, unresolved gaps and the complete planned write set.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/performance/ETF_NYSE_ARCA_VIOG Performance.md`: refresh frontmatter to 2026-08-29, use the official current YTD and July standardized NAV fields, preserve official 2016-2024 plus secondary 2025 annual rows, add June fund/index reconciliation and current quote cross-check, update risk/source conflict notes and preserve the USA breadcrumb/tag.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/comparisons/USA ETF.md`: update VIOG to official rolling `10.98%`, rounded-input 2021-2025 CAGR `5.41%`, and current official YTD `23.25%`, with the separate July/current source-as-of note.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/performance/ETF Performance Index.md`: update the VIOG coverage row, annual summary linkage and 2026-08-29 refresh section to the latest official fields and disclosed source conflicts/gaps.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/log.md`: append one dated `etf-performance` bullet linking `[[ETF_NYSE_ARCA_VIOG Performance]]`, `[[USA ETF]]`, `[[ETF Performance Index]]` and `[[ETF_performance_sources_2026-08-29]]`, stating official rolling `10.98%`, current official YTD `23.25%`, rounded-input 2021-2025 CAGR `5.41%`, and preserved source/daily-NAV gaps; keep outside the scoped commit because `log.md` already contains unrelated changes.
- No new ETF entity or region page is required; existing USA navigation remains the canonical owner and no chart is created for this item.

### Local pre-save checklist

- PASS: official NYSE Arca identity, fund name, inception, passive/index-tracking equity eligibility, canonical key, tracked index, return basis, USD units and USA region ownership are source-mapped; the conflicting workplace inception/July fields are explicitly disclosed.
- PASS: official August-26 current YTD, July standardized NAV fields, June NAV/index reconciliation, fund facts, quote cross-check, annual rows, secondary 2025 row, cached S&P rows and metric definitions retain separate sources and as-of dates.
- PASS: annual/CAGR/up-down calculations, official fund-index differences, current-YTD reconciliation, common-benchmark context and daily-NAV gap reproduce the proposed values; no secondary result is relabelled official and no alpha claim is made.
- PASS: complete proposed contents for VIOG performance, USA region, index, source batch and log artifacts are specified; breadcrumbs/tags/source links are preserved; no unresolved High/Medium finding blocks the write and no WARNING requiring confirmation remains.
verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official Vanguard current and July performance plus June factsheet evidence support the VIOG refresh; scheduled-local verification passed, the workplace July-field conflict and separate as-of dates are disclosed, and official daily-NAV drawdown data remains unavailable.

## IPOL — iShares MSCI Poland UCITS ETF USD (Acc)

### Workflow identity and scope

- `workflow: check-etf-performance`; `execution_profile: scheduled-inline`; `child_card_ari: ari:cloud:trello::card/workspace/6a78536437ed0b3b544c19e1/6a9177759eb403580c64f8db`; `parent_ari: ari:cloud:trello::card/workspace/6a78536437ed0b3b544c19e1/6a91760cdaae83b3d4afdc13`; input ticker `IPOL`; canonical `entity_key: LSE:IPOL`; input/OTC alias `IPLCF` remains recorded on the owner page.
- Card was claimed and directly reread as `In Progress` before research. Primary region is Poland; the durable graph is `[[ETF Region Index]] → [[Poland ETF]] → [[ETF Performance Index]]`.
- This refresh updates the existing IPOL performance owner, Poland navigation snapshot, master performance index, this dated source batch and one log bullet. No ETF entity or new region page is created.

### Source map and as-of dates

| Source | URL/path | Use and as-of date |
|---|---|---|
| BlackRock/iShares current UK product page | https://www.blackrock.com/uk/individual/products/251875/ishares-msci-poland-ucits-etf_1 | Official current USD-share-class NAV, YTD NAV TR, rolling/cumulative table, fund facts, risks and listings; NAV as of 2026-08-27, YTD return as of 2026-08-26 and rolling table capture current to 2026-08-27 with selected return date not exposed |
| iShares July USD accumulating factsheet | https://www.ishares.com/uk/individual/en/literature/fact-sheet/spol-ishares-msci-poland-ucits-etf-fund-fact-sheet-en-gb.pdf | Official July 2026 calendar rows, fund/benchmark cumulative and annualized performance, holdings, fee, methodology and risk facts; performance/portfolio data as of 2026-07-31 and other data as of 2026-08-07 |
| iShares professional product page | https://www.ishares.com/uk/professionals/en/products/251875/ishares-msci-poland-ucits-etf?siteEntryPassthrough=true&switchLocale=y | Official listing map, benchmark, holdings and product-methodology cross-check |
| BlackRock Denmark current product page | https://www.blackrock.com/dk/individual/products/251875/ishares-msci-poland-ucits-etf | Official adjacent-locale cross-check for 26 Aug NAV/YTD and 25 Aug sector facts |
| Prior March factsheet snapshot | `raw/imports/ETF_performance_sources_2026-08-18.md` | Existing source batch records an earlier official March factsheet value for 2020 of `+1.91%`; the latest July factsheet/live page now show `-11.91%`, so the version conflict is retained and the latest July/current pair is used |
| S&P 500 official index page and cached workflow references | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Common USD Total Return reference for complete calendar years 2016-2025; cached convention as of 2025-12-31 |
| Existing vault context | `wiki/analysis/performance/ETF_LSE_IPOL Performance.md`, `wiki/analysis/comparisons/Poland ETF.md`, `wiki/analysis/performance/ETF Performance Index.md`, `raw/imports/ETF_performance_sources_2026-08-18.md` | Prior IPOL page, Poland ownership, annual conflict, 2021-2025 benchmark reconciliation and disclosed daily-NAV gap; current official fields are refreshed |

### Identity and classification evidence

- BlackRock/iShares identifies the fund as `iShares MSCI Poland UCITS ETF USD (Acc)`, ISIN `IE00B4M7GH52`, USD accumulating share class, launched `2011-01-21`, listed on London Stock Exchange as `IPOL` in USD (Bloomberg `IPOL LN`, RIC `IPLD.L`), with GBP `SPOL` as a separate LSE line.
- IPOL is a passive, physical, replicated Poland single-country equity UCITS ETF tracking `MSCI Emerging - Poland in Net USD`; TER is `0.74%`, domicile Ireland and rebalance frequency quarterly. S&P 500 TR is a common reference only, not the tracked benchmark.
- Primary region is Poland and the canonical tag is `geography/Poland`. The `IPLCF` OTC input alias is mapped to the official USD LSE line and is not treated as a separate fund.

### Candidate performance claims and raw observations

- Latest official current page snapshot reports NAV `US$41.43` as of `2026-08-27`, one-day NAV change `-US$1.07` / `-2.52%`, and NAV Total Return YTD `28.91%` as of `2026-08-26`. Net assets are `US$1,114,481,096` as of 2026-08-27; holdings are `16` as of 2026-08-26.
- Current official characteristics are P/B `2.13` and P/E `17.26` as of 2026-08-26, 3-year beta `0.993` and standard deviation `22.01%` as of 2026-07-31. The adjacent official Denmark page reports 25 Aug sector weights: Financials `46.28%`, Energy `16.71%`, Consumer Discretionary `12.42%`, Materials `9.67%`, Consumer Staples `5.72%`, Communication `2.98%`, Information Technology `2.42%`, Utilities `1.79%`, Industrials `1.71%` and Cash/Derivatives `0.31%`.
- The current official product-page rolling table reports fund NAV TR cumulative `164.99%` / annualized `10.24%` over 10 years versus tracked benchmark cumulative `169.59%` / annualized `10.43%`; the selected return date is not exposed in the HTML, so this is retained as an issuer-current capture rather than a reconstructed endpoint calculation.
- The latest official July factsheet reports cumulative NAV/benchmark performance as of 2026-07-31: 1M `10.12%`/`10.19%`, 3M `11.83%`/`11.53%`, 6M `12.94%`/`12.82%`, YTD `21.20%`/`21.13%`, 1Y `38.59%`/`38.12%`, 3Y annualized `30.08%`/`29.89%`, 5Y `15.80%`/`15.81%` and since inception `3.06%`/`3.14%`.
- The latest July factsheet and current live product page align on the complete annual fund rows: 2016 `0.02%`, 2017 `54.33%`, 2018 `-13.14%`, 2019 `-6.03%`, 2020 `-11.91%`, 2021 `8.16%`, 2022 `-27.36%`, 2023 `48.25%`, 2024 `-6.47%` and 2025 `74.88%`; benchmark rows are `0.13%`, `54.72%`, `-12.87%`, `-5.87%`, `-11.39%`, `8.46%`, `-27.24%`, `48.60%`, `-6.65%` and `74.61%`.
- Cached S&P 500 TR rows are 2016 `11.96%`, 2017 `21.83%`, 2018 `-4.38%`, 2019 `31.49%`, 2020 `18.40%`, 2021 `28.71%`, 2022 `-18.11%`, 2023 `26.29%`, 2024 `25.02%` and 2025 `17.88%`; USD, dividends reinvested, as of `2025-12-31`.

### Calculations and reconciliation

- Using the latest July/live annual rows, IPOL compounds to `111.4468%`, displayed as `111.45%`, over 2016-2025; rounded-input CAGR is `(1 + 1.114468)^(1/10) - 1 = 7.78%`. The 2021-2025 rows compound to `90.51%` with rounded-input CAGR `13.76%`; both are official latest July rows and no longer use the superseded March `+1.91%` 2020 observation.
- Cached S&P 500 TR compounds to `298.33%` / CAGR `14.82%` over 2016-2025 and `96.17%` / CAGR `14.43%` over 2021-2025. IPOL's common-reference CAGR differences are `-7.04 pp` and `-0.67 pp`; these are not alpha and S&P 500 TR is not IPOL's strategy benchmark.
- Latest issuer rolling fund-minus-index differences are `-4.60 pp` cumulative and `-0.19 pp` annualized over the 10-year table. The official 2021-2025 row comparison is `-0.64 pp` cumulative / approximately `-0.08 pp` CAGR; July factsheet YTD fund-minus-index is `+0.07 pp`, 1Y `+0.47 pp`, 3Y `+0.19 pp`, 5Y `-0.01 pp` and since inception `-0.08 pp`. These are tracking observations, not alpha.
- Latest annual rows give up/down years `6 / 4`; best is 2025 `+74.88%`, worst is 2022 `-27.36%`. Official daily NAV history sufficient to reproduce maximum drawdown and recovery is not disclosed.

### Source-quality choice and unresolved gaps

- BlackRock/iShares current page and the latest July 2026 factsheet are the sources of truth for the USD accumulating share class. The earlier March factsheet snapshot in the prior batch reported 2020 `+1.91%`, while the latest July factsheet and current live page report `-11.91%`; the latest aligned pair is used for the refreshed 2016-2025 calculation and the version conflict remains disclosed.
- Current NAV/YTD (`2026-08-27`/`2026-08-26`), July standardized performance (`2026-07-31`) and issuer rolling-table capture (selected date not exposed) are separate windows; no date is backfilled or harmonized.
- Official daily NAV history sufficient to reproduce maximum drawdown and recovery is `ไม่พบข้อมูลที่ยืนยันได้`; no secondary drawdown proxy is saved. Point-in-time NAV, AUM, holdings, characteristics, sector weights and performance retain separate as-of dates.
- The fund is passive; no management-skill or alpha claim is made. `IPLCF` is an input alias for the USD `LSE:IPOL` line, not a second performance series.

### Pre-save evidence packet / proposed durable contents

- Evidence packet includes ETF identity and exchange, alias mapping, return basis (`NAV Total Return`), issuer and common benchmarks, candidate claims and periods, units/currency (`%`, USD), definitions, separate as-of dates, source URLs/paths, calculations, reconciliation, source-quality choice, unresolved gaps and the complete planned write set.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/performance/ETF_LSE_IPOL Performance.md`: refresh frontmatter to 2026-08-29, update current NAV/YTD/AUM/holdings/characteristics, use latest July official annual and benchmark rows with 2016-2025 calculation, preserve alias/Poland breadcrumb/tags, and disclose the March-vs-July 2020 source-version conflict and daily-NAV gap.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/comparisons/Poland ETF.md`: update IPOL to official rolling `10.24%`, 2021-2025 CAGR `13.76%`, and current official NAV TR YTD `28.91%`, with separate current/July as-of notes.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/performance/ETF Performance Index.md`: update the IPOL coverage row and 2026-08-29 refresh section to the latest current fields, annual calculation, benchmark tracking observations and disclosed gaps.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/log.md`: append one dated `etf-performance` bullet linking `[[ETF_LSE_IPOL Performance]]`, `[[Poland ETF]]`, `[[ETF Performance Index]]` and `[[ETF_performance_sources_2026-08-29]]`, stating rolling `10.24%`, current official YTD `28.91%`, 2016-2025 CAGR `7.78%`, 2021-2025 CAGR `13.76%`, and the preserved source-version/daily-NAV gaps; keep outside the scoped commit because `log.md` already contains unrelated changes.
- No new ETF entity or region page is required; existing Poland navigation remains the canonical owner and no chart is created for this item.

### Local pre-save checklist

- PASS: official USD LSE identity, `IPLCF` alias mapping, fund name, inception, passive/physical/replicated eligibility, canonical key, tracked index, return basis, USD units and Poland region ownership are source-mapped.
- PASS: official current NAV/YTD/AUM/holdings/characteristics/sector fields, July standardized fund/index returns, current rolling table, latest annual rows, cached S&P rows and metric definitions retain separate sources and as-of dates.
- PASS: 2016-2025 and 2021-2025 calculations, fund/index reconciliation, common-benchmark context, March-vs-July 2020 source-version conflict and daily-NAV gap reproduce the proposed values; no unsupported return or alpha claim is made.
- PASS: complete proposed contents for IPOL performance, Poland region, index, source batch and log artifacts are specified; alias/breadcrumbs/tags/source links are preserved; no unresolved High/Medium finding blocks the write and no WARNING requiring confirmation remains.
verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official BlackRock/iShares current and July USD accumulating-share evidence support the IPOL refresh; scheduled-local verification passed, the March-versus-July 2020 source-version conflict and separate as-of windows are disclosed, and official daily-NAV drawdown data remains unavailable.

## VDJP — Vanguard FTSE Japan UCITS ETF (USD) Distributing

### Workflow identity and scope

- `workflow: check-etf-performance`; `execution_profile: scheduled-inline`; `child_card_ari: ari:cloud:trello::card/workspace/6a78536437ed0b3b544c19e1/6a9177774c4f9f6db18336ae`; `parent_ari: ari:cloud:trello::card/workspace/6a78536437ed0b3b544c19e1/6a91760cdaae83b3d4afdc13`; input ticker `VDJP`; canonical `entity_key: LSE:VDJP`; OTC/input alias `VNFGF` remains recorded on the owner page.
- Card was claimed and directly reread as `In Progress` before research. Primary region is Japan; the durable graph is `[[ETF Region Index]] → [[Japan ETF]] → [[ETF Performance Index]]`.
- This refresh updates the existing VDJP performance owner, Japan navigation snapshot, master performance index, this dated source batch and one log bullet. No ETF entity or new region page is created.

### Source map and as-of dates

| Source | URL/path | Use and as-of date |
|---|---|---|
| Vanguard official professional product page | https://www.vanguard.co.uk/professional/product/etf/equity/9504/ftse-japan-ucits-etf-usd-distributing | Official identity, USD LSE listing, current NAV/market price, current fund facts, classification, benchmark and tracking statistics; prices captured at 2026-08-28 close, 52-week fields may show 2026-08-29 page metadata |
| Vanguard FTSE Japan UCITS ETF USD Distributing factsheet | https://fund-docs.vanguard.com/FTSE_Japan_UCITS_ETF_USD_Distributing_9504_EU_INT_UK_EN.pdf | Official rolling 12-month NAV/benchmark returns, standardized rolling 10-year performance, portfolio characteristics, sectors, fee and share-class facts; performance and portfolio data as of 2026-07-31 |
| Vanguard ETF prospectus | https://fund-docs.vanguard.com/etf-prospectus-en.pdf | Official fund-structure and risk cross-check; current prospectus source retained from the existing page |
| S&P 500 official index page and cached workflow references | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Common USD Total Return reference for complete calendar years 2016-2025; cached convention as of 2025-12-31 |
| Existing vault context | `wiki/analysis/performance/ETF_LSE_VDJP Performance.md`, `wiki/analysis/comparisons/Japan ETF.md`, `wiki/analysis/performance/ETF Performance Index.md`, `raw/imports/ETF_performance_sources_2026-07-24.md` | Prior rolling June-May page, Japan ownership, alias mapping, benchmark context and disclosed daily-NAV gap; July 2026 official evidence supersedes the prior May 2026 snapshot |

### Identity and classification evidence

- Vanguard identifies the fund as `FTSE Japan UCITS ETF – (USD) Distributing` (fund/product code `9504`), with `VDJP` as the USD London Stock Exchange ticker; `VNFGF` is an OTC/input alias for this same fund, not a separate performance series. ISIN is `IE00B95PGT31`; Bloomberg `VDJP LN`; Reuters `VDJP.L`.
- The fund launched on `2013-05-21` and was listed on `2013-05-22`. It is an Irish UCITS, passive, physical equity ETF tracking the `FTSE Japan Index`, investing in large- and mid-cap Japanese equities with full replication where practicable and sampling where necessary. OCF is `0.10%`; distributions are quarterly.
- Primary region is Japan and the canonical tag is `geography/Japan`. The product page reports Japan allocation `100%`, share-class assets `US$3.18B`, total fund assets `US$4.99B`, and risk indicator `6` in the reviewed capture.

### Candidate performance claims and raw observations

- Latest official product-page price capture reports NAV `US$52.30` and market price `£38.65`, both at the 2026-08-28 close. Historical NAV fields show `US$52.3035` on 2026-08-28, `US$52.1557` on 2026-08-27 and `US$52.0387` on 2026-08-26. These are point-in-time prices, separate from standardized month-end total-return fields.
- The official July factsheet reports closing-NAV total return, net of fees with distributions reinvested, as of 2026-07-31: fund `0.87%` 1M, `5.05%` quarter, `16.27%` YTD, `31.22%` 1Y, `17.40%` 3Y annualized, `9.69%` 5Y annualized, `9.03%` 10Y annualized and `7.36%` since inception. The corresponding FTSE Japan Index fields are `0.87%`, `5.09%`, `16.32%`, `31.31%`, `17.50%`, `9.79%`, `9.17%` and `7.51%`.
- The same official factsheet supplies rolling 12-month fund/index NAV TR rows: 01 Aug 2016-31 Jul 2017 `14.62%`/`14.90%`; Aug 2017-Jul 2018 `8.90%`/`9.08%`; Aug 2018-Jul 2019 `-5.51%`/`-5.35%`; Aug 2019-Jul 2020 `0.99%`/`1.11%`; Aug 2020-Jul 2021 `25.47%`/`25.63%`; Aug 2021-Jul 2022 `-14.43%`/`-14.34%`; Aug 2022-Jul 2023 `14.71%`/`14.81%`; Aug 2023-Jul 2024 `15.44%`/`15.56%`; Aug 2024-Jul 2025 `6.81%`/`6.92%`; and Aug 2025-Jul 2026 `31.22%`/`31.31%`.
- Latest official July portfolio facts are `475` stocks, median market cap `US$43.4B`, P/E `16.6`, P/B `1.8`, ROE `10.2%`, earnings growth `16.8%`, turnover `-20.4%` from 2026-06-30, equity yield `1.9%`, and Japan allocation `100%`. Sector weights are Industrials `26.8%`, Financials `17.8%`, Consumer Discretionary `17.7%`, Technology `15.0%`, Health Care `5.1%`, Basic Materials `4.5%`, Consumer Staples `4.4%`, Telecommunications `4.0%`, Real Estate `2.7%`, Utilities `1.3%` and Energy `0.9%`.
- Official tracking statistics as of 2026-07-31 are beta `0.99`, R-squared `1.00`, and annualized tracking error `0.03%` 1Y, `0.47%` 3Y and `0.36%` 5Y. The factsheet's `1.73%` historic-performance field is not substituted for NAV total return.
- Cached S&P 500 TR rows are 2016 `11.96%`, 2017 `21.83%`, 2018 `-4.38%`, 2019 `31.49%`, 2020 `18.40%`, 2021 `28.71%`, 2022 `-18.11%`, 2023 `26.29%`, 2024 `25.02%` and 2025 `17.88%`; USD, dividends reinvested, as of `2025-12-31`. Calendar-year VDJP rows are not disclosed by the reviewed official July factsheet.

### Calculations and reconciliation

- The official rounded 10-year annualized NAV TR is `9.03%` for the rolling period 2016-08-01 through 2026-07-31, equivalent to `10.00` elapsed years. Because raw NAV endpoints are not disclosed, normalized cumulative return is derived from the displayed rounded CAGR: `100 × (1 + 0.0903)^10 - 100 = 137.35%`. The corresponding benchmark calculation from `9.17%` is `140.43%`; fund-minus-index is approximately `-3.09 pp` cumulative and `-0.14 pp` annualized. These normalized cumulative values are derived, not issuer-reported endpoints.
- Official rolling rows give up/down periods `8 / 2`; best is Aug 2025-Jul 2026 `+31.22%`, and worst is Aug 2021-Jul 2022 `-14.43%`. Calendar 2021-2025 CAGR is `not disclosed`; it is not calculated from these non-calendar rolling periods.
- The cached S&P 500 TR compounds to `298.33%` / CAGR `14.82%` over calendar 2016-2025. This is a common directional reference only and is not date-aligned with VDJP's rolling August-July periods; no alpha claim is made.
- Official rolling fund-minus-index differences are `-0.28 pp`, `-0.18 pp`, `-0.16 pp`, `-0.12 pp`, `-0.16 pp`, `-0.09 pp`, `-0.10 pp`, `-0.12 pp`, `-0.11 pp` and `-0.09 pp` across the ten rows. The July standardized fund-minus-index differences are `-0.04 pp` YTD, `-0.09 pp` 1Y, `-0.10 pp` 3Y, `-0.10 pp` 5Y, `-0.14 pp` 10Y and `-0.15 pp` since inception; these are tracking observations, not manager skill.

### Source-quality choice and unresolved gaps

- Vanguard's July 2026 factsheet and official product page are the sources of truth for the USD distributing share class, identity, rolling performance, current price and risk facts. The July factsheet supersedes the prior May 2026 snapshot; the new rolling periods are preserved as August-July periods and are not relabeled as calendar years.
- Current NAV/market prices are dated 2026-08-28, while standardized performance and fund facts are dated 2026-07-31. No current date-to-date YTD value after July is backfilled from the point-in-time price series; the latest verified standardized NAV TR YTD remains `16.27%` as of 2026-07-31.
- The product page's historic-performance/distribution field is not used as NAV total return. Official daily NAV history sufficient to reproduce maximum drawdown, recovery dates and a daily volatility series is `ไม่พบข้อมูลที่ยืนยันได้`; no secondary drawdown proxy is saved.
- Official holdings, sector, valuation, tracking-error, price and performance fields retain separate as-of dates. `VNFGF` is retained as an alias for `LSE:VDJP`; no duplicate OTC performance line is created.

### Pre-save evidence packet / proposed durable contents

- Evidence packet includes ETF identity and exchange, alias mapping, return basis (`NAV Total Return`), issuer benchmark (`FTSE Japan Index`), common S&P reference, candidate claims and rolling periods, units/currency (`%`, USD/GBP price), definitions, separate as-of dates, source URLs/paths, calculations, reconciliation, source-quality choice, unresolved gaps and the complete planned write set.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/performance/ETF_LSE_VDJP Performance.md`: refresh frontmatter to 2026-08-29, use official July rolling rows and 10-year NAV TR `9.03%`, derive normalized cumulative `137.35%` from the rounded CAGR with the formula disclosed, update current NAV/market prices, fund facts, tracking statistics and source-quality notes, preserve alias/breadcrumb/tags, and keep calendar 2021-2025 CAGR as not disclosed.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/comparisons/Japan ETF.md`: update VDJP to official rolling `9.03%`, calendar CAGR `not disclosed (rolling periods)`, and official standardized NAV TR YTD `16.27%`, with the current price and July performance as-of separation noted.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/performance/ETF Performance Index.md`: update the VDJP coverage row and 2026-08-29 refresh section to July rolling values, current NAV, benchmark tracking context and disclosed daily-NAV/calendar-window gaps.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/log.md`: append one dated `etf-performance` bullet linking `[[ETF_LSE_VDJP Performance]]`, `[[Japan ETF]]`, `[[ETF Performance Index]]` and `[[ETF_performance_sources_2026-08-29]]`, stating official rolling `9.03%`, derived normalized cumulative `137.35%`, official July YTD `16.27%`, and preserved rolling/calendar/daily-NAV gaps; keep outside the scoped commit because `log.md` already contains unrelated changes.
- No new ETF entity or region page is required; existing Japan navigation remains canonical and no chart is created for this item.

### Local pre-save checklist

- PASS: official LSE USD distributing identity, `VNFGF` alias mapping, fund name, inception/listing dates, passive/physical/index-tracking equity eligibility, canonical key, tracked index, return basis, currency and Japan region ownership are source-mapped.
- PASS: official current NAV/market price, July standardized NAV/index returns, rolling annual rows, fund facts, sector exposures, tracking statistics, fee, cached S&P rows and metric definitions retain separate sources and as-of dates.
- PASS: normalized cumulative calculations, fund-index reconciliation, up/down counts, best/worst rows, current-vs-standardized date separation, common-benchmark context and daily-NAV gap reproduce the proposed values; no secondary result is relabeled official and no alpha claim is made.
- PASS: complete proposed contents for VDJP performance, Japan region, index, source batch and log artifacts are specified; breadcrumb/alias/tags/source links are preserved; no unresolved High/Medium finding blocks the write and no WARNING requiring confirmation remains.
verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official Vanguard current and July factsheet evidence support the VDJP refresh; scheduled-local verification passed, rolling August-July periods and separate current-price/standardized-return dates are disclosed, calendar-year CAGR and official daily-NAV drawdown data remain unavailable, and the durable write set is complete.

## CUSS — iShares MSCI USA Small Cap CTB Enhanced ESG UCITS ETF USD (Acc)

### Workflow identity and scope

- `workflow: check-etf-performance`; `execution_profile: scheduled-inline`; `child_card_ari: ari:cloud:trello::card/workspace/6a78536437ed0b3b544c19e1/6a91777a1901f9ca3adfe7b1`; `parent_ari: ari:cloud:trello::card/workspace/6a78536437ed0b3b544c19e1/6a91760cdaae83b3d4afdc13`; input ticker `CUSS`; canonical `entity_key: LSE:CUSS`; OTC/input alias `CPLCF` remains recorded on the owner page.
- Card was claimed and directly reread as `In Progress` before research. Primary region is United States; the durable graph is `[[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]`.
- This refresh updates the existing CUSS performance owner, USA navigation snapshot, master performance index, this dated source batch and one log bullet. No ETF entity or new region page is created.

### Source map and as-of dates

| Source | URL/path | Use and as-of date |
|---|---|---|
| BlackRock/iShares current product page | https://www.blackrock.com/uk/individual/products/253480/ishares-msci-usa-small-cap-ctb-enhanced-esg-ucits-etf | Official current NAV/YTD, objective, benchmark-change disclosure, fund facts, characteristics and listing map; latest search capture shows NAV `US$708.60` as of 2026-08-27 and NAV TR YTD `20.54%` as of 2026-08-26; full page capture separately shows fund facts through 2026-08-24/31-Jul |
| iShares official professional product page | https://www.ishares.com/uk/professionals/en/products/253480/csuss | Official objective, benchmark change, risk language, fund facts, portfolio characteristics, USD LSE listing and literature links; page capture through 2026-07-31/07-Aug and current page fields through 2026-07-31 |
| iShares July USD factsheet | https://www.ishares.com/gls-download/literature/fact-sheet/csuss-ishares-msci-usa-small-cap-ctb-enhanced-esg-ucits-etf-fund-fact-sheet-en-gb.pdf | Official annual NAV/benchmark rows, July cumulative/annualized returns, holdings, fee, structure and risk facts; performance/portfolio data as of 2026-07-31 and all other data as of 2026-08-07 |
| London Stock Exchange CUSS page | https://www.londonstockexchange.com/stock/CUSS/ishares/company-page | USD LSE listing cross-check; page response did not expose a readable quote table in the reviewed capture |
| S&P 500 official index page and cached workflow references | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Common USD Total Return reference for complete calendar years 2016-2025; cached convention as of 2025-12-31 |
| Existing vault context | `wiki/analysis/performance/ETF_LSE_CUSS Performance.md`, `wiki/analysis/comparisons/USA ETF.md`, `wiki/analysis/performance/ETF Performance Index.md`, `raw/imports/ETF_performance_sources_2026-08-17.md` | Prior CUSS page, USA ownership, alias mapping, annual series and benchmark-change caveat; current official August/July evidence supersedes the prior July-29 snapshot |

### Identity and classification evidence

- BlackRock/iShares identifies the fund as `iShares MSCI USA Small Cap CTB Enhanced ESG UCITS ETF`, USD accumulating share class, ISIN `IE00B3VWM098`, launched `2009-07-01`, with `CUSS` as the USD London Stock Exchange ticker (Bloomberg `CUSS LN`, RIC `CUSS.L`, SEDOL `B53N420`). `CPLCF` is an OTC/input alias for this same fund and is not a separate performance series. The same fund family also has GBP `CUS1`; the listing map is preserved to avoid mixing exchange lines.
- CUSS is a passive, physical, optimised U.S. small-cap equity UCITS ETF tracking the `MSCI USA Small Cap ESG Enhanced Focus CTB Index`; TER is `0.43%`, income is accumulating, domicile Ireland, SFDR Article 8 and rebalance frequency quarterly.
- The fund changed name/objective and benchmark on `2022-06-01`: prior benchmark `MSCI USA Small Cap Index`, current benchmark `MSCI USA Small Cap ESG Enhanced Focus CTB Index`. The fund's calendar NAV history is continuous, but issuer benchmark comparisons across the full 2016-2025 window are not one continuous benchmark series.
- Primary region is United States and the canonical tag is `geography/United-States`.

### Candidate performance claims and raw observations

- Latest official current product-page search capture reports NAV `US$708.60` as of `2026-08-27`, one-day NAV change `-US$0.12` / `-0.02%`, and NAV Total Return YTD `20.54%` as of `2026-08-26`. The current page's full capture reports net assets `US$3,256,508,232`, `1,509` holdings and P/B `2.62` as of `2026-08-24`; P/E is `21.42` as of 2026-08-24, beta `1.000` and standard deviation `18.55%` as of 2026-07-31. These are separate current/fund-facts dates.
- The official July factsheet reports NAV total return, with gross income reinvested where applicable and on an NAV basis, as of `2026-07-31`: 1M `-4.34%`, 3M `4.31%`, 6M `10.72%`, YTD `16.40%`, 1Y `28.32%`, 3Y annualized `12.92%`, 5Y annualized `6.84%` and since inception annualized `12.61%`. The corresponding benchmark fields are `-4.34%`, `4.31%`, `10.75%`, `16.45%`, `28.51%`, `13.11%`, `6.99%` and `12.79%`.
- The latest official July factsheet supplies complete calendar-year NAV rows: 2016 `19.13%`, 2017 `16.49%`, 2018 `-10.49%`, 2019 `26.56%`, 2020 `18.15%`, 2021 `18.86%`, 2022 `-16.94%`, 2023 `15.63%`, 2024 `10.71%` and 2025 `9.60%`. Benchmark rows are `19.15%`, `16.75%`, `-10.40%`, `26.74%`, `18.32%`, `19.11%`, `-16.79%`, `15.53%`, `11.02%` and `9.77%`; the pre-2022 benchmark rows reflect the former MSCI USA Small Cap Index.
- The July factsheet reports `1,510` holdings, P/B `2.54x`, P/E `21.23x` and 3-year beta `1.00`; portfolio data and all other factsheet data are dated 2026-08-07 unless marked as performance/portfolio data at 2026-07-31. The full official page's current holdings snapshot is later but slightly different at `1,509`.
- Cached S&P 500 TR rows are 2016 `11.96%`, 2017 `21.83%`, 2018 `-4.38%`, 2019 `31.49%`, 2020 `18.40%`, 2021 `28.71%`, 2022 `-18.11%`, 2023 `26.29%`, 2024 `25.02%` and 2025 `17.88%`; USD, dividends reinvested, as of `2025-12-31`. S&P 500 TR is a common reference only, not CUSS's strategy benchmark.

### Calculations and reconciliation

- Using the official rounded fund rows, CUSS compounds to `157.2806%`, displayed as `157.28%`, over 2016-2025; rounded-input CAGR is `(1 + 1.572806)^(1/10) - 1 = 9.91%`. The 2021-2025 rows compound to `38.5146%`, displayed as `38.51%`, with rounded-input CAGR `6.73%`.
- The official rounded benchmark rows compound to `160.8160%` / CAGR `10.06%` over 2016-2025 and `39.5415%` / CAGR `6.89%` over 2021-2025. Fund-minus-index is approximately `-3.54 pp` cumulative / `-0.15 pp` annualized for 2016-2025 and `-1.03 pp` cumulative / `-0.16 pp` annualized for 2021-2025. Because of the 2022 benchmark change, these full-window benchmark comparisons are directional tracking context, not a single continuous strategy benchmark.
- Cached S&P 500 TR compounds to `298.33%` / CAGR `14.82%` over 2016-2025 and `96.17%` / CAGR `14.43%` over 2021-2025. These common-reference differences are not alpha and do not replace the issuer benchmark.
- Annual fund rows give up/down years `8 / 2`; best is 2019 `+26.56%`, worst is 2022 `-16.94%`, least positive is 2025 `+9.60%`, and least bad down year is 2018 `-10.49%`. Official daily NAV history sufficient to reproduce maximum drawdown and recovery is not disclosed in the reviewed source set.

### Source-quality choice and unresolved gaps

- BlackRock/iShares current and July USD factsheet materials are the sources of truth for identity, classification, current fields, annual NAV returns, benchmark rows and the 2022 methodology break. The latest current capture replaces the prior current YTD `14.97%` as of 2026-07-29 with `20.54%` as of 2026-08-26; the July standardized YTD `16.40%` remains separately labeled and is not harmonized with the later current field.
- The current page defaults visually to the GBP `CUS1` listing in some captures while its listing map identifies the USD `CUSS` line. The USD NAV/YTD fields, ISIN, USD share-class facts and LSE CUSS listing map are retained together; no GBP market-price series is mixed into NAV total return.
- Current NAV/YTD, current AUM/holdings/valuation, July standardized performance and July/August portfolio fields have separate as-of dates. Official daily NAV history sufficient to reproduce maximum drawdown and recovery is `ไม่พบข้อมูลที่ยืนยันได้`; no secondary drawdown proxy is saved.
- The 2022-06-01 benchmark/name change is disclosed wherever full-history benchmark context is used. No management-skill or alpha claim is made; return-only fund-minus-index arithmetic is labeled as tracking observation.

### Pre-save evidence packet / proposed durable contents

- Evidence packet includes ETF identity and exchange, alias mapping, return basis (`NAV Total Return`), issuer benchmark and benchmark-change date, common S&P reference, candidate claims and calendar periods, units/currency (`%`, USD), definitions, separate as-of dates, source URLs/paths, calculations, reconciliation, source-quality choice, unresolved gaps and the complete planned write set.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/performance/ETF_LSE_CUSS Performance.md`: refresh frontmatter to 2026-08-29, update current NAV/YTD/AUM/holdings/characteristics, preserve official 2016-2025 annual NAV and benchmark rows, update 2016-2025/2021-2025 calculations, retain the 2022 benchmark/name-change caveat, preserve alias/USA breadcrumb/tags and disclose the daily-NAV gap.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/comparisons/USA ETF.md`: update CUSS/CPLCF to official 2016-2025 CAGR `9.91%`, 2021-2025 CAGR `6.73%`, and latest current official NAV TR YTD `20.54%`, with July standardized YTD and current/fund-fact as-of dates separated.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/performance/ETF Performance Index.md`: update the CUSS coverage row, annual summary and 2026-08-29 refresh section to current official fields, annual calculations, benchmark-change caveat and disclosed daily-NAV gap.
- Proposed content for `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/log.md`: append one dated `etf-performance` bullet linking `[[ETF_LSE_CUSS Performance]]`, `[[USA ETF]]`, `[[ETF Performance Index]]` and `[[ETF_performance_sources_2026-08-29]]`, stating official 2016-2025 CAGR `9.91%`, 2021-2025 CAGR `6.73%`, current official YTD `20.54%`, and preserved benchmark-change/daily-NAV gaps; keep outside the scoped commit because `log.md` already contains unrelated changes.
- No new ETF entity or region page is required; existing USA navigation remains canonical and no chart is created for this item.

### Local pre-save checklist

- PASS: official USD LSE identity, `CPLCF` alias mapping, fund name, inception date, passive/physical/optimised/index-tracking equity eligibility, canonical key, tracked index, return basis, USD units and United States region ownership are source-mapped.
- PASS: official current NAV/YTD, current AUM/holdings/valuation, July standardized NAV/index returns, complete annual rows, benchmark-change date, fee, structure, risk facts, cached S&P rows and metric definitions retain separate sources and as-of dates.
- PASS: 2016-2025 and 2021-2025 calculations, fund/index reconciliation, common-benchmark context, up/down/best/worst rows, current-vs-standardized date separation and daily-NAV gap reproduce the proposed values; no secondary result is relabeled official and no alpha claim is made.
- PASS: complete proposed contents for CUSS performance, USA region, index, source batch and log artifacts are specified; alias/breadcrumbs/tags/source links are preserved; no unresolved High/Medium finding blocks the write and no WARNING requiring confirmation remains.
verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official BlackRock/iShares current and July USD-share-class evidence support the CUSS refresh; scheduled-local verification passed, the 2022 benchmark/name change and separate current/standardized as-of dates are disclosed, calendar returns reconcile, official daily-NAV drawdown data remains unavailable, and the durable write set is complete.

## NFTY — First Trust India NIFTY 50 Equal Weight ETF

### Workflow identity and scope

- `workflow: check-etf-performance`; `execution_profile: scheduled-inline`; child card ARI: `ari:cloud:trello::card/workspace/6a78536437ed0b3b544c19e1/6a91777d094c1678af65d776`; input ticker `NFTY`; canonical `entity_key: NASDAQ:NFTY`.
- The card was claimed and directly reread as `In Progress` before this check. Primary region is India; the durable graph is `[[ETF Region Index]] → [[India ETF]] → [[ETF Performance Index]]`.
- This refresh updates the existing NFTY performance owner, India navigation snapshot, ETF Performance Index coverage row, this source batch, and one log bullet. No ETF entity or new region page is required.

### Source map and classification

| Source | URL/path | Use and as-of date |
|---|---|---|
| First Trust official summary | https://www.ftportfolios.com/Retail/Etf/EtfSummary.aspx?Ticker=NFTY | Canonical identity, Nasdaq listing, inception `2012-02-14`, passive objective, index, expense ratio `0.80%` as of `2026-05-01`, current fund facts and standardized performance; page data includes performance through `2026-07-31` and current fields through `2026-08-28` |
| First Trust monthly performance report | https://www.ftportfolios.com/Common/ContentFileLoader.aspx?ContentGUID=b363655b-cc73-4f42-a7b1-4c1e00306c7c | Official NAV/market-price/index performance through `2026-07-31`; NAV TR YTD `-5.59%` and 3-year standard deviation `14.31%`; the PDF capture displays `7.99%` in its 10-year column, which conflicts with the current summary page's `7.62%` |
| First Trust factsheet | https://www.ftportfolios.com/Common/ContentFileLoader.aspx?ContentGUID=4ce8e98a-434e-452d-89fb-89f33f070e32 | Official historical calendar NAV rows `2016-2025` and passive/index facts in the reviewed capture; capture is dated `2026-03-31` |
| First Trust summary prospectus | https://www.ftportfolios.com/Common/ContentFileLoader.aspx?ContentGUID=9c00e478-c2d3-49d2-b8db-229055716c36 | Official indexing approach, 90% policy, risk and index-history caveat; dated `2026-05-01` |
| First Trust historical pricing | https://www.ftportfolios.com/Retail/Etf/EtfPriceHistory.aspx?Ticker=NFTY | Current point-in-time NAV `US$54.40`, market price `US$54.10`, and net assets `US$116,956,871`, all as of `2026-08-27` |
| First Trust holdings | https://www.ftportfolios.com/Retail/Etf/EtfHoldings.aspx?Ticker=NFTY | Current exposure and 50-holding confirmation as of `2026-08-28`; sector snapshot is separate from return dates |
| S&P 500 official index page and cached workflow references | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Common USD Total Return reference for complete calendar years `2016-2025`, dividends reinvested, as of `2025-12-31`; no current-year S&P comparison claimed |
| Existing vault context | `wiki/analysis/performance/ETF_NASDAQ_NFTY Performance.md`, `wiki/analysis/comparisons/India ETF.md`, `wiki/analysis/performance/ETF Performance Index.md` | Prior NFTY owner, India navigation, annual series and index-change caveat; current July/August evidence supersedes the prior June snapshot |

- First Trust describes NFTY as seeking results corresponding generally to the price and yield of the `NIFTY 50 Equal Weight Index`, normally investing at least 90% of net assets in index common stocks. This supports `passive-index` classification. The index contains 50 Indian securities, equal-weights constituents, rebalances quarterly and reconstitutes semi-annually.
- The underlying index changed from the NASDAQ AlphaDEX Taiwan Index to the NIFTY 50 Equal Weight Index on `2018-04-17`; the fund's pre-change history is retained as fund NAV history but is not a pure current-index backtest. The index inception is `2017-04-13`.

### Candidate performance claims and raw observations

- Latest official standardized month-end performance (`2026-07-31`) from the current First Trust summary page: NAV Total Return 3-month `2.27%`, YTD `-5.59%`, 1-year `-1.64%`, 3-year annualized `5.68%`, 5-year annualized `6.09%`, 10-year annualized `7.62%`, and since-inception annualized `6.35%`. Market-price return is kept separate (`-5.97%` YTD). The issuer states returns are total returns and the NAV series reflects fund expenses; distributions are included in NAV total return. The linked monthly-report PDF for the same as-of month displays `7.99%` in its 10-year column; this source conflict is retained, and `7.62%` is used because it is the later/current summary-page field.
- Current official point-in-time data (`2026-08-27`): NAV `US$54.40`, market price `US$54.10`, net assets `US$116,956,871`; current holdings page reports 50 holdings as of `2026-08-28`. These are not substituted for NAV TR observations.
- Current sector snapshot (`2026-08-27`) is Financials `21.98%`, Consumer Discretionary `17.04%`, Materials `12.19%`, Information Technology `10.60%`, Industrials `9.74%`, and Health Care `9.59%`, supporting the country/sector concentration risk read-through.
- The reviewed official historical calendar rows are: 2016 `10.31%`, 2017 `22.54%`, 2018 `-2.67%`, 2019 `0.88%`, 2020 `10.83%`, 2021 `26.22%`, 2022 `-4.45%`, 2023 `24.39%`, 2024 `5.30%`, and 2025 `5.84%`. Annual NIFTY 50 Equal Weight rows were not disclosed in the current capture.
- The May 2026 summary prospectus displays small version/rounding differences for 2023-2025 (`24.44%`, `5.27%`, `5.73%`) versus the reviewed factsheet series. The factsheet series is retained consistently in the owner page and calculations; the conflict is not silently reconciled.
- Cached S&P 500 Total Return rows for `2016-2025` are `11.96%`, `21.83%`, `-4.38%`, `31.49%`, `18.40%`, `28.71%`, `-18.11%`, `26.29%`, `25.02%`, and `17.88%`; USD, dividends reinvested, as of `2025-12-31`.

### Calculations and reconciliation

- Official rolling 10-year NAV TR is `7.62%` as of `2026-07-31`; raw per-share TR endpoints are not disclosed. A normalized display calculation is `100 × (1 + 0.0762)^10 - 100 = 108.42%`; this is derived from the displayed rounded CAGR and is not an issuer-reported cumulative endpoint. The 10-year window is shown as `2016-07-31` to `2026-07-31`, `10.00` years.
- The retained official calendar rows compound to `145.94%` cumulative / rounded-input CAGR `9.42%` for `2016-2025`; the five rows `2021-2025` compound to `67.19%` / CAGR `10.83%`. Cached S&P 500 TR compounds to `298.33%` / CAGR `14.82%` over `2016-2025` and `96.17%` / CAGR `14.43%` over `2021-2025`.
- Complete-year profile is `8` up / `2` down. Best year is `2021` at `26.22%`; least positive is `2019` at `0.88%`; worst is `2022` at `-4.45%`; least-bad down year is `2018` at `-2.67%`. The latest official month-end NAV TR YTD is `-5.59%` as of `2026-07-31`.
- First Trust reports 3-year standard deviation `14.31%` as of `2026-07-31`; official daily NAV observations sufficient to reproduce maximum drawdown and recovery are `ไม่พบข้อมูลที่ยืนยันได้`.

### Source-quality choice, gaps, and proposed durable contents

- The current First Trust summary page is the source of truth for the latest July standardized return fields and current fund identity. Its rolling 10-year field is `7.62%`; the monthly-report PDF's `7.99%` 10-year display is preserved as an explicit source conflict rather than mixed into the owner metric. The historical factsheet series is retained because it supplies the complete annual table; the prospectus version difference is disclosed rather than mixed into the calculations.
- Current NAV/market price and holdings dates (`2026-08-27`/`2026-08-28`) are kept separate from standardized NAV TR and risk dates (`2026-07-31`). No date-to-date YTD is backfilled from point-in-time NAV prices.
- Proposed `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/performance/ETF_NASDAQ_NFTY Performance.md`: refresh frontmatter/source batch, July rolling 10-year `7.62%`, July NAV TR YTD `-5.59%`, current NAV/market-price observations, official risk/sector facts, retained annual table, source conflict, index-change caveat, and India breadcrumb.
- Proposed `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/comparisons/India ETF.md`: update the NFTY row to `7.62%`, `10.83%`, `-5.59%` and add the dated July/August as-of note.
- Proposed `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/performance/ETF Performance Index.md`: update the NFTY coverage row and `2026-08-29 Performance Refresh` bullet to the same verified metrics and gaps.
- Proposed `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/raw/imports/ETF_performance_sources_2026-08-29.md`: append this complete source map, observations, calculations, reconciliation, local checklist, and handoff.
- Proposed `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/log.md`: append one dated `etf-performance` bullet linking NFTY performance, India navigation, ETF Performance Index, and this source batch; keep the existing unrelated working-tree change unstaged.

### Local pre-save checklist

- PASS: canonical `NASDAQ:NFTY` identity, Nasdaq exchange, fund name, inception, passive/index-tracking equity eligibility, tracked index, expense ratio, India region, and 2018 index-change caveat are source-mapped.
- PASS: NAV Total Return, market-price return, issuer-index rows, current NAV/price, holdings, sector facts, historical annual rows, currencies, units, and every as-of date are separated; distributions are included in the NAV TR convention; the summary-page `7.62%` versus monthly-PDF `7.99%` conflict is explicitly retained.
- PASS: 10-year eligibility, normalized rounded-CAGR calculation, 2016-2025 and 2021-2025 compounding, up/down/best/worst ranking, cached S&P 500 basis/window, and the summary/monthly-report plus factsheet/prospectus conflicts reconcile to the proposed page. No unsupported current YTD or daily drawdown value is inferred.
- PASS: complete proposed contents for performance, India region, ETF Performance Index, source batch, and log are specified; breadcrumb and links resolve; no critical/high finding remains and no WARNING requires confirmation.
- `verification_mode: scheduled-local`
- `reviewer_dispatch: not-attempted-by-design`

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official First Trust July performance and current fund evidence support the NFTY refresh; scheduled-local verification passed, the summary-versus-monthly-report 10-year conflict and separate as-of dates are disclosed, and the daily NAV drawdown/recovery gap remains explicit.

## CHIQ — Global X MSCI China Consumer Discretionary ETF

### Workflow identity and scope

- `workflow: check-etf-performance`; `execution_profile: scheduled-inline`; child card ARI: `ari:cloud:trello::card/workspace/6a78536437ed0b3b544c19e1/6a91777fac2e895ec1ef507e`; input ticker `CHIQ`; canonical `entity_key: NYSE Arca:CHIQ`.
- The card was claimed and directly reread as `In Progress` before research. Primary region is China; the durable graph is `[[ETF Region Index]] → [[China ETF]] → [[ETF Performance Index]]`.
- This refresh updates the existing CHIQ performance owner, China navigation snapshot, ETF Performance Index coverage row, this source batch, and one log bullet. No ETF entity or new region page is required.

### Source map and classification

| Source | URL | Use and as-of date |
|---|---|---|
| Global X official CHIQ product page | https://www.globalxetfs.com/funds/CHIQ | Canonical identity, NYSE Arca listing, objective, index, current NAV/market price/net assets/holdings, current characteristics and risk stats; current fields through `2026-08-27`, performance table through `2026-06-30` |
| Global X CHIQ factsheet | https://assets.globalxetfs.com/funds/documents/chiq/Fact-Sheet_CHIQ.pdf | Official NAV TR, market-price return, hybrid-index return, July YTD and rolling 10-year performance, 57 holdings, expense ratio, industry weights and return definitions; as of `2026-07-31` |
| Global X CHIQ summary prospectus | https://assets.globalxetfs.com/funds/documents/chiq/prospectus-regulatory/Summary-Prospectus_CHIQ.pdf | Official annual NAV TR rows `2016-2025`, formal objective/fee, replication/indexing approach, risk disclosures and index-history break; dated `2026-03-01`, annual rows through `2025-12-31` |
| Global X CHIQ annual shareholder report | https://assets.globalxetfs.com/funds/documents/chiq/prospectus-regulatory/Annual-Shareholder-Report.pdf | Passive/full-replication cross-check and fiscal-year performance; report period ended `2025-10-31`, not mixed into the calendar-year window |
| Global X index methodology summary | https://assets.globalxetfs.com/funds/documents/chiq/Index-Methodology-Summary.pdf | 10/50 construction, eligible China A/B/H, red-chip, P-chip and foreign listings, free-float weighting and quarterly rebalance; methodology document is historical and not used for current weights |
| Cached S&P 500 Total Return convention | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Common USD Total Return reference for complete calendar years `2016-2025`, dividends reinvested, as of `2025-12-31`; no current-year S&P comparison claimed |
| Existing vault context | `wiki/analysis/performance/ETF_NYSE_ARCA_CHIQ Performance.md`, `wiki/analysis/comparisons/China ETF.md`, `wiki/analysis/performance/ETF Performance Index.md` | Prior CHIQ owner and China navigation; July 2026 factsheet evidence supersedes the prior June/July-21 snapshot |

- Global X describes CHIQ as seeking to track the price and yield performance, before fees and expenses, of the `MSCI China Consumer Discretionary 10/50 Index`; the 2026 summary prospectus says the fund generally uses a replication strategy and is not actively managed. This supports `passive-index` classification.
- The fund's name, investment objective, investment strategy and underlying index changed effective `2018-12-06`; performance through `2018-12-05` reflects the predecessor Solactive China Consumer Total Return Index and later performance reflects the MSCI China Consumer Discretionary 10/50 Index. The break is disclosed rather than treated as one unchanged index history.

### Candidate performance claims and raw observations

- Latest official factsheet performance as of `2026-07-31`: NAV Total Return 1-month `17.80%`, YTD `-12.37%`, 1-year `-10.93%`, 3-year annualized `-2.25%`, 5-year annualized `-7.74%`, 10-year annualized `6.53%`, and since inception annualized `2.50%`. Market-price returns are kept separate: 1-month `18.41%`, YTD `-11.46%`, 1-year `-10.22%`, 3-year `-2.50%`, 5-year `-7.60%`, 10-year `6.57%`, since inception `2.53%`. Hybrid-index returns are separate: YTD `-12.11%` and 10-year `7.15%`.
- The current Global X product page as of `2026-08-27` reports NAV `US$17.57`, market price `US$17.40`, net assets `US$115.63m`, 57 holdings, expense ratio `0.65%`, median bid-ask spread `0.60%`, and 30-day SEC yield `0.98%`. These are point-in-time fund facts, not substitutions for the July NAV TR series.
- Current industry weights from the July factsheet are Consumer Discretionary Distribution & Retail `36.97%`, Automobiles & Components `28.66%`, Consumer Durables & Apparel `17.02%`, Consumer Services `16.69%`, Equity REITs `0.38%`, and Technology Hardware & Equipment `0.28%`. The product page reports standard deviation `32.00%` and beta `0.89` versus the S&P 500 as of `2026-07-31`.
- The official annual NAV TR rows from the March 2026 summary prospectus are: 2016 `-5.88%`, 2017 `65.28%`, 2018 `-27.72%`, 2019 `43.06%`, 2020 `93.43%`, 2021 `-27.23%`, 2022 `-22.07%`, 2023 `-10.92%`, 2024 `12.16%`, and 2025 `12.91%`.
- The annual shareholder report provides a separate fiscal-year cross-check: 1-year NAV return `14.55%` and index `15.26%` for the period ended `2025-10-31`; its 10-year NAV return `7.10%` is not mixed into the July 2026 rolling field.
- Cached S&P 500 Total Return rows for `2016-2025` are `11.96%`, `21.83%`, `-4.38%`, `31.49%`, `18.40%`, `28.71%`, `-18.11%`, `26.29%`, `25.02%`, and `17.88%`; USD, dividends reinvested, as of `2025-12-31`.

### Calculations and reconciliation

- The official rolling 10-year NAV TR CAGR is `6.53%` for `2016-07-31` to `2026-07-31`; raw NAV endpoints are not disclosed. A normalized display calculation is `100 × (1 + 0.0653)^10 - 100 = 88.24%`; this is derived from the rounded issuer CAGR and is not an issuer-reported cumulative endpoint.
- Official annual rows compound to normalized TR `100.00` → `199.05`, cumulative `99.05%`, and rounded-input CAGR `7.13%` for `2016-2025`. The `2021-2025` rows compound to approximately `-36.03%` cumulative / `-8.55%` CAGR; the prospectus reports `-8.54%` from unrounded underlying data, so the rounded-input calculation is retained and labeled.
- Cached S&P 500 TR compounds to `298.33%` cumulative / CAGR `14.82%` over `2016-2025` and `96.17%` / CAGR `14.43%` over `2021-2025`. CHIQ trails the S&P common reference by approximately `7.69 pp` CAGR over `2016-2025` and `22.98 pp` over `2021-2025`; this is reference context, not manager alpha.
- Complete-year profile is `5` up / `5` down. Best year is `2020` at `93.43%`; worst is `2021` at `-27.23%`; the latest official NAV TR YTD is `-12.37%` as of `2026-07-31`.
- The reviewed official sources do not expose a reproducible daily NAV series for maximum drawdown and recovery: `ไม่พบข้อมูลที่ยืนยันได้`.

### Source-quality choice, gaps, and proposed durable contents

- The July 2026 Global X factsheet is the source of truth for the latest standardized NAV TR, market-price and hybrid-index fields because it is the freshest official return table. The current product page supplies later point-in-time NAV, price, net assets and holdings, while its June performance table is not mixed into the July factsheet metrics.
- The summary prospectus is the source of truth for the complete 2016-2025 annual NAV series and formal index-history disclosure. The annual shareholder report is retained as a fiscal-year cross-check only; its dates and 10-year field differ from the July factsheet.
- Proposed `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/performance/ETF_NYSE_ARCA_CHIQ Performance.md`: refresh frontmatter/source batch, July rolling 10-year `6.53%`, July NAV TR YTD `-12.37%`, current NAV/market-price/net-assets observations, industry/risk facts, annual rows, index-change caveat, and China breadcrumb.
- Proposed `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/comparisons/China ETF.md`: add/update the current CHIQ row to `6.53%`, `-8.55%`, `-12.37%` and add the dated July/August as-of note; preserve the historical July-23 row.
- Proposed `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/performance/ETF Performance Index.md`: update the CHIQ coverage row and append the `2026-08-29 Performance Refresh` bullet with the same verified metrics and gaps.
- Proposed `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/raw/imports/ETF_performance_sources_2026-08-29.md`: append this complete source map, observations, calculations, reconciliation, local checklist and handoff.
- Proposed `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/log.md`: append one dated `etf-performance` bullet linking CHIQ performance, China navigation, ETF Performance Index and this source batch; keep the existing unrelated working-tree change unstaged.

### Local pre-save checklist

- PASS: canonical `NYSE Arca:CHIQ` identity, fund name, inception, passive/index-tracking equity eligibility, tracked index, expense ratio, China region and `2018-12-06` index/strategy break are source-mapped.
- PASS: NAV Total Return, market-price return, hybrid-index return, current NAV/price/net assets/holdings, industry/risk facts, annual rows, currencies, units and each as-of date are separated; distributions are included in the NAV TR convention.
- PASS: rolling 10-year eligibility, normalized rounded-CAGR calculation, 2016-2025 and 2021-2025 compounding, up/down/best/worst ranking, cached S&P 500 basis/window, July factsheet versus June product-page date distinction, and fiscal-year cross-check reconcile to the proposed page. No unsupported current-year benchmark or daily drawdown value is inferred.
- PASS: complete proposed contents for performance, China region, ETF Performance Index, source batch and log are specified; breadcrumbs/source links resolve; no critical/high finding remains and no WARNING requires confirmation.
- `verification_mode: scheduled-local`
- `reviewer_dispatch: not-attempted-by-design`

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official Global X July factsheet and current product-page evidence support the CHIQ refresh; scheduled-local verification passed, separate return and point-in-time dates are disclosed, the index-history break is preserved, and the daily NAV drawdown/recovery gap remains explicit.

## CQQQ — Invesco China Technology ETF

### Workflow identity and scope

- `workflow: check-etf-performance`; `execution_profile: scheduled-inline`; child card ARI: `ari:cloud:trello::card/workspace/6a78536437ed0b3b544c19e1/6a91778146e64ad3aa4c9cbf`; input ticker `CQQQ`; canonical `entity_key: NYSE Arca:CQQQ`.
- The card was claimed and directly reread as `In Progress` before research. Primary region is China; the durable graph is `[[ETF Region Index]] → [[China ETF]] → [[ETF Performance Index]]`.
- This recheck updates the existing CQQQ performance owner, China navigation note, ETF Performance Index refresh section, this source batch and one log bullet. No ETF entity or new region page is required.

### Source map and classification

| Source | URL | Use and as-of date |
|---|---|---|
| Invesco official CQQQ product page | https://www.invesco.com/us/en/financial-products/etfs/invesco-china-technology-etf.html | Canonical identity, NYSE Arca listing, current product discovery and strategy; current text capture did not expose numeric current NAV/YTD fields |
| Invesco Q4 2025 performance report | https://www.invesco.com/us-rest/contentdetail?contentId=84c2f428e1682610VgnVCM1000006e36b50aRCRD&dnsName=us | Official NAV/market-price/index standardized performance, annual rows, fund facts and holdings; as of `2025-12-31` |
| Invesco CQQQ factsheet | https://www.invesco.com/content/dam/invesco/us/en/product-documents/etf/fact-sheet/cqqq-invesco-china-technology-etf-fact-sheet.pdf | Official fund/index identity and risk/strategy context; reviewed PDF capture dated `2025-09-30`, retained as supporting rather than current-return evidence |
| SEC CQQQ summary prospectus | https://www.sec.gov/Archives/edgar/data/1378872/000119312525040714/d834062d497k.htm | Official predecessor/reorganization and index-history disclosures, at-least-90% policy, non-diversified and risk context |
| Cached S&P 500 Total Return convention | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Common USD Total Return reference for complete calendar years `2016-2025`, dividends reinvested, as of `2025-12-31`; no current-year comparison claimed |
| Existing vault context | `wiki/analysis/performance/ETF_NYSE_ARCA_CQQQ Performance.md`, `wiki/analysis/comparisons/China ETF.md`, `wiki/analysis/performance/ETF Performance Index.md` | Prior CQQQ annual series and strategy-history caveat; current recheck confirms no verified current NAV/YTD field to replace `not disclosed` |

- Invesco describes CQQQ as based on the `FTSE China Incl A 25% Technology Capped Index`; the fund invests at least 90% of total assets in index securities and related ADRs/GDRs. The official materials describe the shares as not actively managed, supporting `passive-index` classification.
- The SEC prospectus identifies CQQQ as successor to the Guggenheim China Technology ETF after the reorganization completed on `2018-05-18`. The current FTSE index methodology began on `2019-06-22`; earlier blended-index history reflects AlphaShares China Technology Index. These continuity breaks are disclosed.

### Candidate performance claims and raw observations

- Latest fully readable official standardized report as of `2025-12-31`: NAV TR YTD/1Y `33.65%`, 3-year annualized `7.27%`, 5-year annualized `-8.27%`, 10-year annualized `4.45%`, and since inception `5.69%`. Market-price values are `34.84%`, `34.84%`, `7.27%`, `-8.23%`, `4.47%`, and `5.67%`; underlying-index YTD `35.14%`, 1-year `35.14%`, 3-year `8.04%`, 5-year `-7.62%`. These are not current 2026 YTD values.
- The same official report provides fund facts as of `2025-12-31`: 157 holdings, management fee and total expense ratio `0.65%`, P/B `5.46`, P/E `21.99`, return on equity `12.77%`, and NYSE Arca listing. Current product-page text did not expose a newer numeric snapshot during this review.
- Official annual NAV TR rows are: 2016 `-0.07%`, 2017 `72.54%`, 2018 `-34.21%`, 2019 `32.46%`, 2020 `58.33%`, 2021 `-25.13%`, 2022 `-29.74%`, 2023 `-16.97%`, 2024 `11.24%`, and 2025 `33.65%`.
- Cached S&P 500 Total Return rows for `2016-2025` are `11.96%`, `21.83%`, `-4.38%`, `31.49%`, `18.40%`, `28.71%`, `-18.11%`, `26.29%`, `25.02%`, and `17.88%`; USD, dividends reinvested, as of `2025-12-31`.

### Calculations and reconciliation

- The official annual rows compound to normalized TR `100.00` → `154.48`, cumulative `54.48%`, and rounded-input CAGR `4.44%` for `2016-2025`; the official Q4 report displays `4.45%` from unrounded data. The row-derived `4.44%` is retained consistently in the owner page.
- The `2021-2025` rows compound to `-35.06%` cumulative / rounded-input CAGR `-8.27%`; the official Q4 report's 5-year annualized field also displays `-8.27%`.
- Cached S&P 500 TR compounds to `298.33%` cumulative / CAGR `14.82%` over `2016-2025` and `96.17%` / CAGR `14.43%` over `2021-2025`. CQQQ trails the common reference by approximately `10.38 pp` CAGR and `22.70 pp` CAGR, respectively; this is reference context, not manager alpha.
- Complete-year profile is `5` up / `5` down. Best year is `2017` at `72.54%`; least positive is `2024` at `11.24%`; worst is `2018` at `-34.21%`; least-bad down year is `2016` at `-0.07%`.
- Current NAV/YTD and reproducible official daily NAV history for drawdown/recovery are `ไม่พบข้อมูลที่ยืนยันได้` in the reviewed Invesco capture. The 2025-12-31 standardized field must not be presented as 2026 current YTD.

### Source-quality choice, gaps, and proposed durable contents

- The Q4 2025 Invesco report is the latest fully readable official standardized return table located in this review, so it supports the annual and historical metrics only. The current product-page text was freshly checked but did not expose a newer current NAV/YTD value; `not disclosed` is retained rather than backfilled from secondary price or return data.
- The annual NAV row-derived 10-year CAGR `4.44%` is used even though the Q4 report's rounded summary field is `4.45%`; this small difference is disclosed and the consistent row calculation is retained. The Q4 report's 5-year field agrees with the row-derived `-8.27%`.
- Proposed `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/performance/ETF_NYSE_ARCA_CQQQ Performance.md`: refresh timestamp/source batch, preserve official 2016-2025 annual/2021-2025 calculations, record current NAV/YTD as not disclosed, add Q4 source and strategy-history caveat, and preserve China breadcrumb.
- Proposed `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/comparisons/China ETF.md`: add a dated CQQQ recheck note while leaving the numeric snapshot unchanged and preserving the historical July-23 row.
- Proposed `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/performance/ETF Performance Index.md`: append the CQQQ status to the `2026-08-29 Performance Refresh` section while leaving current numeric row values unchanged.
- Proposed `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/raw/imports/ETF_performance_sources_2026-08-29.md`: append this complete source map, observations, calculations, reconciliation, local checklist and handoff.
- Proposed `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/log.md`: append one dated `etf-performance` bullet linking CQQQ performance, China navigation, ETF Performance Index and this source batch; keep the existing unrelated working-tree change unstaged.

### Local pre-save checklist

- PASS: canonical `NYSE Arca:CQQQ` identity, fund name, inception, passive/index-tracking equity eligibility, tracked index, expense ratio, China region, successor reorganization and `2019-06-22` methodology break are source-mapped.
- PASS: NAV Total Return, market-price return, underlying-index return, annual rows, Q4 fund facts, currencies, units and as-of dates are separated; the 2025-12-31 field is not relabeled as current 2026 YTD.
- PASS: 10-year calendar eligibility, normalized row calculation, 2021-2025 compounding, up/down/best/worst ranking, cached S&P 500 basis/window, 4.44-versus-4.45 rounding difference and current-data gap reconcile to the proposed page. No unsupported current NAV/YTD or daily drawdown value is inferred.
- PASS: complete proposed contents for performance, China navigation, ETF Performance Index, source batch and log are specified; breadcrumbs/source links resolve; no critical/high finding remains and no WARNING requires confirmation.
- `verification_mode: scheduled-local`
- `reviewer_dispatch: not-attempted-by-design`

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official Invesco historical performance and SEC strategy evidence support the CQQQ recheck; scheduled-local verification passed, current NAV/YTD remains explicitly undisclosed, rounding and continuity breaks are documented, and the daily NAV drawdown/recovery gap remains explicit.

## OPPE — WisdomTree European Opportunities Fund

### Workflow identity and scope

- `workflow: check-etf-performance`; `execution_profile: scheduled-inline`; child card ARI: `ari:cloud:trello::card/workspace/6a78536437ed0b3b544c19e1/6a9177830070452b908e1c0a`; input ticker `OPPE`; canonical `entity_key: NYSE Arca:OPPE`.
- The card was claimed and directly reread as `In Progress` before research. Primary region is Europe; the durable graph is `[[ETF Region Index]] → [[Europe ETF]] → [[ETF Performance Index]]`.
- This recheck updates the existing OPPE performance owner, Europe navigation note, ETF Performance Index refresh section, this source batch and one log bullet. No ETF entity or new region page is required.

### Source map and classification

| Source | URL | Use and as-of date |
|---|---|---|
| WisdomTree official OPPE product page | https://www.wisdomtree.com/us/products/equity/oppe | Canonical identity, NYSE Arca, current objective, fee, current NAV/price, July month-end NAV returns, portfolio characteristics, holdings, sectors and hedge ratio; point-in-time fields as of `2026-08-26/27` and return fields as of `2026-07-31` |
| WisdomTree OPPE quarterly factsheet | https://www.wisdomtree.com/us/media/international-equity/en-us-equity-oppe | Official exchange, inception, 90 holdings, 2026-06-30 rolling return table, return basis and historical index splice |
| WisdomTree Trust prospectus | https://regulated-documents.saytechnologies.com/prospectuses/e0ff850f-45f1-417b-8779-01e2206cb79d-97717X552.pdf | Passive management, representative sampling, official 2016-2024 annual-return chart and strategy-change disclosure |
| WisdomTree monthly performance report | https://www.wisdomtree.com/investments/-/media/us-media-files/documents/resource-library/fund-reports-schedules/performance/monthly-performance.pdf | Official 2026-06-30 rolling table and current report context |
| WisdomTree dividend yield report as of 2025-12-31 | https://www.wisdomtree.com/investments/-/media/us-media-files/documents/resource-library/fund-reports-schedules/dividend-yield/us-dividend-report-2025-12-31.pdf | Official 2025 NAV one-year return and 2021-2025/10-year cross-check |
| WisdomTree European Opportunities Index | https://www.wisdomtree.com/us/indexes/wteuop | Index design, shareholder-yield/value and geopolitical, technology and macro opportunity exposures; dynamic 0-100% currency hedge; base date `2025-04-30` |
| Secondary drawdown proxy | https://portfolioslab.com/symbol/OPPE | Dividend-adjusted daily market-price drawdown/recovery proxy only; not NAV evidence |
| Cached S&P 500 Total Return convention | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Common USD Total Return reference for complete calendar years `2016-2025`, dividends reinvested, as of `2025-12-31`; no current-year comparison claimed |
| Existing vault context | `wiki/analysis/performance/ETF_NYSE_ARCA_OPPE Performance.md`, `wiki/analysis/comparisons/Europe ETF.md`, `wiki/analysis/performance/ETF Performance Index.md` | Prior annual series, strategy-transition caveat and navigation graph; refreshed fields are reconciled against current official sources |

- `OPPE` is a supported passive/index-tracking equity ETF. The prospectus describes passive management and representative sampling; the product page says the fund seeks to track the price and yield performance, before fees and expenses, of the WisdomTree European Opportunities Index.
- The fund was formerly EUSC. WisdomTree states that the investment policy/index changed on `2025-06-02`; the current EUOP index was established with base value `200` on `2025-04-30` and uses a monthly dynamic hedge ratio between `0%` and `100%`.
- The historical source symbol remains `EUSC.NV` on the product page, but the canonical entity for this card is `NYSE Arca:OPPE`; this legacy symbol is not treated as a separate instrument.

### Candidate performance claims and raw observations

- Current WisdomTree product page fields labelled `2026-08-27`: net expense ratio `0.58%`, total assets `$296.60480M`, shares outstanding `4,950,000`, distribution yield `7.88%`, 30-day SEC yield `2.66%`, NAV `$59.920`, closing market price `$60.045`, premium/discount `0.208%`, and 30-day median bid/ask spread `0.18%`.
- The same page's portfolio characteristics as of `2026-08-27` are dividend yield `3.35%`, P/E `14.34`, estimated P/E `13.86`, P/B `1.94`, price/sales `0.98`, price/cash flow `8.38`, gross buyback yield `2.47%`, and net buyback yield `2.25%`. Holdings and sector data are labelled `2026-08-26`; the page shows 10 named holdings plus remaining portfolio, and sector weights Industrials `25.73%`, Financials `25.30%`, Materials `13.01%`, Consumer Discretionary `7.09%`, Information Technology `6.74%`, Energy `6.45%`, Utilities `5.46%`, Health Care `3.96%`, Consumer Staples `3.13%`, Real Estate `1.66%`, and Communication Services `1.47%`.
- Current page month-end return fields as of `2026-07-31`: NAV Total Return cumulative `1M 6.19%`, `3M 6.56%`, YTD `17.72%`, since inception `249.26%`; average annual NAV returns `1Y 29.84%`, `3Y 23.84%`, `5Y 14.66%`, `10Y 12.91%`, since inception `11.59%`. The corresponding index fields are `6.25%`, `6.64%`, `18.05%`, `255.60%`, and `30.79%`, `24.27%`, `14.91%`, `13.12%`, `11.75%`.
- The product page reports aggregate hedge ratio `98.12%` as of `2026-08-27`. WisdomTree explains that the fund uses derivatives for dynamic currency hedging; the hedge ratio is implemented after month-end close.
- Official factsheet as of `2026-06-30` reports 90 holdings and NAV returns `YTD 10.86%`, `1Y 23.70%`, `3Y 22.58%`, `5Y 14.02%`, `10Y 12.97%`, and since inception `11.09%`. These June fields are retained as a date-separated cross-check, not mixed with the newer July product-page return fields.
- Official annual NAV TR rows for `2016-2024` from the prospectus are `7.86%`, `22.32%`, `-13.41%`, `28.45%`, `-2.34%`, `22.65%`, `-11.18%`, `19.33%`, and `10.74%`. The official 2025 NAV one-year return ending `2025-12-31` is `38.73%` in the WisdomTree dividend-yield/monthly performance materials; it is a mixed transition year rather than a clean current-strategy year.
- The current official quarterly/product pages do not expose a reproducible daily NAV series sufficient to independently calculate maximum drawdown and recovery: `ไม่พบข้อมูลที่ยืนยันได้`. The freshly checked PortfoliosLab page is clearly labelled a dividend-adjusted daily market-price series; it reports maximum drawdown `39.28%` on `2020-03-18` and recovery `229` trading sessions, so it remains a marked secondary proxy only.

### Calculations and reconciliation

- The official rounded annual rows compound to normalized TR `100.00` → `286.21`, cumulative `186.21%`, and rounded-input CAGR `11.09%` over `2016-2025`; population annual-return standard deviation is `16.33%`; complete-year profile is `7` up / `3` down.
- The `2021-2025` rows compound to `99.71%` cumulative / rounded-input CAGR `14.84%`; the cached S&P 500 Total Return reference compounds to `96.17%` / CAGR `14.43%`. OPPE is ahead by approximately `0.41 pp` CAGR in this common reference window, but this is not manager alpha and the window includes the 2025 strategy transition.
- The cached S&P 500 Total Return reference compounds to `298.33%` / CAGR `14.82%` over `2016-2025`; OPPE trails that common reference by approximately `3.73 pp` CAGR. This is reference context, not tracked-index excess return or alpha.
- Best calendar year is `2025 +38.73%`; worst is `2018 -13.41%`; least-bad down year is `2020 -2.34%`; the 2025 result and the 2016-2024 rows must be read with the EUSC-to-OPPE continuity caveat.
- The issuer's rolling 10-year NAV TR `12.91%` as of `2026-07-31` is kept separate from the rounded-input 2016-2025 calendar CAGR `11.09%`; the June factsheet's `12.97%` is a prior month-end value and is not mixed into the current row.

### Source-quality choice, gaps, and proposed durable contents

- The current WisdomTree product page is the source of truth for current NAV, market price, premium/discount, yields, portfolio characteristics, current hedge ratio and July month-end performance. The June factsheet and monthly report are retained as date-separated official cross-checks.
- The prospectus annual chart is the source of truth for 2016-2024 annual NAV rows. The official 2025 one-year return ending 2025-12-31 is sourced separately from the WisdomTree report; the strategy/index transition is disclosed rather than treated as a seamless current-strategy history.
- The secondary PortfoliosLab drawdown/recovery data is retained only as a marked market-price proxy. No official daily NAV drawdown or recovery value is inferred, and no secondary YTD value replaces the official July NAV YTD.
- Proposed `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/performance/ETF_NYSE_ARCA_OPPE Performance.md`: refresh frontmatter/source batch, current NAV/price/fund facts through 2026-08-27, official July rolling/YTD fields, date-separated June cross-check, current sector/valuation/hedge facts, annual rows, calculation updates and transition/daily-NAV caveats.
- Proposed `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/comparisons/Europe ETF.md`: retain the OPPE row and add the current quote/yield/hedge recheck note while preserving the static Europe navigation summary.
- Proposed `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/performance/ETF Performance Index.md`: append OPPE to the `2026-08-29 Performance Refresh` section with the verified current metrics and disclosed gaps.
- Proposed `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/raw/imports/ETF_performance_sources_2026-08-29.md`: append this source map, observations, calculations, reconciliation, local checklist and handoff.
- Proposed `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/log.md`: append one dated `etf-performance` bullet linking OPPE performance, Europe navigation, ETF Performance Index and this source batch; preserve the existing unrelated working-tree change.

### Local pre-save checklist

- PASS: canonical `NYSE Arca:OPPE` identity, fund name, inception, passive/index-tracking equity eligibility, tracked index, exchange, fee, Europe region and EUSC-to-OPPE strategy/index transition are source-mapped.
- PASS: NAV Total Return, market-price return, underlying-index return, current NAV/price/yield/portfolio facts, hedge ratio, annual rows, currencies, units and every as-of date are separated; current July return fields are not mixed with June factsheet fields or secondary market-price proxy data.
- PASS: 10-year eligibility, normalized 2016-2025 and 2021-2025 calculations, up/down/best/worst ranking, cached S&P 500 basis/window, rolling-versus-calendar distinction, and 2025 transition caveat reconcile to the proposed page. No unsupported current benchmark YTD, NAV drawdown or recovery value is inferred.
- PASS: complete proposed contents for performance, Europe navigation, ETF Performance Index, source batch and log are specified; breadcrumbs/source links resolve; no critical/high finding remains and no WARNING requires confirmation.
- `verification_mode: scheduled-local`
- `reviewer_dispatch: not-attempted-by-design`

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official WisdomTree current product data and historical performance sources support the OPPE refresh; scheduled-local verification passed, separate as-of windows and the 2025 strategy transition are disclosed, and the daily NAV drawdown/recovery gap remains explicit.

## INDQ — Pacer ActiveAlpha India Quality ETF

### Workflow identity and scope

- `workflow: check-etf-performance`; `execution_profile: scheduled-inline`; child card ARI: `ari:cloud:trello::card/workspace/6a78536437ed0b3b544c19e1/6a9177857eb4d73991a4b62a`; input ticker `INDQ`; canonical `entity_key: Nasdaq:INDQ`.
- The card was claimed and directly reread as `In Progress` before research. Primary region is India; the durable graph is `[[ETF Region Index]] → [[India ETF]] → [[ETF Performance Index]]`.
- This recheck updates the existing INDQ performance owner, India navigation snapshot/note, ETF Performance Index refresh section, this source batch and one log bullet. No new ETF entity or region page is required.

### Source map and classification

| Source | URL | Use and as-of date |
|---|---|---|
| Official Pacer INDQ product/performance page | https://www.paceretfs.com/products/indq | Canonical identity, Nasdaq listing, fund/index, inception `2026-03-31`, passive rules-based strategy, expense ratio `0.88%`, and current/performance field availability; direct capture returned an access restriction, while the official indexed extract showed quote fields `as of --` and blank performance values |
| Official Pacer INDQ factsheet | https://www.paceretfs.com/media/indq.pdf | Fund/index identity, NAV Total Return convention, expense, inception, benchmark and performance table; data as of `2026-03-31`, with INDQ NAV, market-price and ActiveAlpha Index performance fields shown as `N/A` |
| Official Pacer INDQ documents | https://docs.paceretfs.com/indq | Official document hub and risk disclosure; reviewed during the current source pass |
| Official Pacer INDQ summary prospectus | https://regulated-documents.saytechnologies.com/prospectuses/7da4597a-2a8f-4dd7-836c-bce3400f9869-69374H196.pdf | Formal objective, fees, listing, ticker, index and short-history disclosure; dated `2025-12-22` in the official document record |
| Official Pacer INDQ launch release | https://www.paceretfs.com/media/Pacer_ETFs_INDQ_Launch_Press_Release.pdf | Strategy context: Indian quality/value/momentum selection from the Nifty 500 and Nifty Microcap 250 universe; launch announcement `2026-04-01` |
| SEC INDQ summary prospectus | https://www.sec.gov/Archives/edgar/data/1616668/000089418925017392/ck0001616668-20251222.htm | Objective, index methodology and portfolio-selection details; current prospectus dated `2025-12-22` |
| SEC INDQ statement of additional information | https://www.sec.gov/Archives/edgar/data/1616668/000089418926007588/paceractivealphaindiaquali.htm | Current identity/listing and confirmation that the fund seeks total-return performance before fees/expenses; amended `2026-03-05` |
| Official Nasdaq INDQ quote page | https://www.nasdaq.com/market-activity/etf/indq | Current exchange-side corroboration; reviewed result says `Data is currently not available` |
| Cached S&P 500 Total Return convention | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Common USD Total Return reference for complete calendar years `2016-2025`, dividends reinvested, as of `2025-12-31`; no INDQ comparison is calculated because the fund has no disclosed return rows |
| Existing vault context | `wiki/analysis/performance/ETF_NASDAQ_INDQ Performance.md`, `wiki/analysis/comparisons/India ETF.md`, `wiki/analysis/performance/ETF Performance Index.md` | Prior INDQ owner and India navigation; current recheck preserves the missing-return gap and updates the source batch/timestamps |

- Official Pacer and SEC materials classify INDQ as a passive, rules-based ETF seeking to track the total return performance before fees and expenses of the `ActiveAlpha India Quality Index`; NAV returns assume distributions are reinvested. This supports `passive-index` classification.
- The strategy starts from the Nifty 500 and Nifty Microcap 250 universe, applies eligibility/governance, value and risk-adjusted momentum filters, and narrows the portfolio to approximately 20-30 Indian companies. This is a factor-concentrated India equity exposure, not a broad market-cap index.
- The fund's official inception is `2026-03-31`, so 10-year NAV TR is not applicable. The official page/factsheet and Nasdaq capture do not expose a numeric current or available-period fund return.

### Candidate performance claims and raw observations

- Official factsheet data as of `2026-03-31` shows INDQ fund NAV return, market-price return and ActiveAlpha Index return fields as `N/A`; the factsheet states that returns for periods under one year are cumulative and that NAV/market returns assume dividends and capital gains are reinvested.
- The official Pacer product-page extract labels current quote fields `as of --` and its performance section `as of 03/31/2026` without numeric INDQ returns. The direct product-page capture returned an access restriction during this review; this is recorded as a source-access limitation, not filled with a secondary quote.
- Official Pacer search/document extracts identify ticker `INDQ`, Nasdaq listing, ISIN `US69374H1968`, CUSIP `69374H196`, inception `2026-03-31`, total expenses `0.88%`, tracked index `ActiveAlpha India Quality Index`, benchmark `MSCI India Index`, and intraday NAV symbol `INDQIV`.
- The official Nasdaq quote page reviewed for current corroboration reports `Data is currently not available`. Current NAV, current YTD, available-period NAV TR, holdings snapshot and realized risk statistics are therefore `not disclosed` in the reviewed official evidence.
- The factsheet includes a separate MSCI India benchmark section, but no benchmark value is substituted for INDQ's missing fund return. No market-price or secondary total-return proxy is used.

### Calculations and reconciliation

- `10-year NAV TR`: not applicable because inception is `2026-03-31`.
- Available-period NAV TR cannot be calculated: the official start/end return endpoints are not disclosed and the official performance fields are `N/A`. Therefore cumulative return, CAGR, up/down years, best/worst year, tracking difference, drawdown and recovery are all `not disclosed` or `not calculable`.
- Current YTD is `not disclosed`; no point-in-time NAV or market-price value is used to backfill it. No S&P 500 comparison is calculated for INDQ because there is no verified INDQ return row to compare against the cached USD reference.
- The only usable numeric inputs in this review are instrument metadata such as the `0.88%` expense ratio; no return arithmetic is performed. Units are percentages where applicable, currency is USD for the quoted share-class identifiers, and all dates remain source-specific.

### Source-quality choice, gaps, and proposed durable contents

- The official Pacer factsheet is the source of truth for the latest readable fund performance table, but its INDQ NAV/market/index fields are `N/A` as of `2026-03-31`. The official product-page extract and Nasdaq page independently leave current quote/performance data blank or unavailable.
- The official SEC filings are used for objective, listing, index and strategy details. A direct Pacer access restriction is disclosed rather than worked around with lower-priority secondary data. The MSCI India benchmark rows in the factsheet remain separate from INDQ fund performance.
- Proposed `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/performance/ETF_NASDAQ_INDQ Performance.md`: update frontmatter/source batch and recheck date, preserve inception/under-10-year status, record official N/A/blank current-return fields, add the source-access limitation, keep no-proxy policy, retain India breadcrumb and source links.
- Proposed `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/comparisons/India ETF.md`: add INDQ to the current performance snapshot and add a dated recheck note with the inception and not-disclosed return gap; preserve the historical coverage-addition row.
- Proposed `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/performance/ETF Performance Index.md`: append the INDQ status to the `2026-08-29 Performance Refresh` section while retaining the current coverage row's not-applicable/not-disclosed fields.
- Proposed `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/raw/imports/ETF_performance_sources_2026-08-29.md`: append this complete source map, observations, calculations, reconciliation, local checklist and handoff.
- Proposed `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/log.md`: append one dated `etf-performance` bullet linking INDQ performance, India navigation, ETF Performance Index and this source batch; preserve the existing unrelated working-tree change and keep `log.md` unstaged.

### Local pre-save checklist

- PASS: canonical `Nasdaq:INDQ` identity, fund name, inception, passive/index-tracking equity eligibility, tracked index, benchmark, expense ratio, India region and official listing are source-mapped.
- PASS: NAV Total Return, market-price return, index return and benchmark fields are kept separate; the factsheet's `N/A` and the product/Nasdaq blank/unavailable fields are not converted into zeroes or proxy returns; USD identifiers, percentage units and source-specific as-of dates are retained.
- PASS: 10-year ineligibility, missing available-period endpoints, no-CAGR/no-up-down conclusion, no-current-YTD conclusion, current-data access limitation and no-secondary-proxy choice reconcile to the proposed owner page and index/region notes.
- PASS: complete proposed contents for performance, India navigation, ETF Performance Index, source batch and log are specified; breadcrumbs/source links resolve; no critical/high finding remains and no WARNING requires confirmation.
verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official Pacer, SEC and Nasdaq evidence confirm INDQ identity and passive India factor exposure while official fund/index performance remains N/A or unavailable; scheduled-local verification passed, no return or proxy was inferred, and the under-10-year/current-data gaps are explicitly preserved.

## SMHC — VanEck China Semiconductor ETF

### Workflow identity and scope

- `workflow: check-etf-performance`; `execution_profile: scheduled-inline`; child card ARI: `ari:cloud:trello::card/workspace/6a78536437ed0b3b544c19e1/6a9177887f32ceaaadb7feb8`; input ticker `SMHC`; canonical `entity_key: Nasdaq:SMHC`.
- The card was claimed and directly reread as `In Progress` before research. Primary region is China; the durable graph is `[[ETF Region Index]] → [[China ETF]] → [[ETF Performance Index]]`.
- This recheck updates the existing SMHC performance owner, China navigation note, ETF Performance Index coverage row/refresh section, this source batch and one log bullet. No new ETF entity or region page is required.

### Source map and classification

| Source | URL | Use and as-of date |
|---|---|---|
| VanEck official SMHC product/performance page | https://www.vaneck.com/us/en/investments/china-semiconductor-etf-smhc/overview/ | Canonical identity, Nasdaq listing, current NAV, performance-since-inception summary, net assets, expense ratio, inception, holdings, currency exposure and detailed performance blocks; summary fields as of `2026-08-27`, holdings as of `2026-08-27`, currency exposure as of `2026-07-31` |
| VanEck SMHC fund profile | https://www.vaneck.com/us/en/investments/china-semiconductor-etf-smhc/smhc-chinas-race-to-the-future-fund-profile.pdf | Official fund/index identity, risk disclosure and return-convention notes; profile dated `2026-06` |
| VanEck SMHC launch release | https://www.vaneck.com/us/en/press-releases/vaneck-launches-smhc-offering-pure-play-access-to-chinas-semiconductor-build-out/ | Official strategy/launch context for China semiconductor exposure |
| VanEck SMHC Q&A | https://www.vaneck.com/us/en/blogs/thematic-investing/smhc-etf-question-answer/ | Official product and strategy context |
| SEC SMHC summary prospectus | https://www.sec.gov/Archives/edgar/data/1137360/000113736026000629/vaneckchinasemiconductoret.htm | Official identity, Nasdaq listing, objective, 0.65% fee, 80% policy, index construction, passive approach, Stock Connect and risk disclosures; dated `2026-06-22` |
| SEC SMHC statement of additional information | https://www.sec.gov/Archives/edgar/data/1137360/000113736026000630/veconsolsai485b062026.htm | Official current fund/ticker/exchange and administration details; dated `2026-06-22` |
| Cached S&P 500 Total Return convention | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Common USD Total Return reference for complete calendar years `2016-2025`, dividends reinvested, as of `2025-12-31`; no current-year comparison claimed |
| Existing vault context | `wiki/analysis/performance/ETF_NASDAQ_SMHC Performance.md`, `wiki/analysis/comparisons/China ETF.md`, `wiki/analysis/performance/ETF Performance Index.md` | Prior SMHC owner and China navigation; July gap snapshot is superseded by the current VanEck summary field and current holdings/asset facts |

- VanEck and SEC materials classify SMHC as a passive, index-tracking equity ETF seeking to track, before fees and expenses, the price and yield performance of the `MarketVector China Semiconductor 25 Index (MVSMHCTR)`. The index is rules-based, modified capitalization-weighted and float-adjusted; it selects 25 of the largest and most liquid eligible Chinese semiconductor companies. The fund normally invests at least 80% of total assets in benchmark securities and is non-diversified.
- Official inception is `2026-06-23`, so the fund is ineligible for a 10-year NAV TR series and for 2021-2025 calendar CAGR comparison. The current summary provides a less-than-one-year cumulative performance-since-inception field; no annualization is appropriate.

### Candidate performance claims and raw observations

- Current VanEck summary fields as of `2026-08-27`: NAV `US$47.82`, performance since inception `-18.83%`, and total net assets `US$26.30M`; total expense ratio is `0.65%` and inception is `2026-06-23`.
- Official current holdings page as of `2026-08-27` reports `27` holdings. Currency exposure as of `2026-07-31` is Chinese Renminbi `64.58%` and Other/Cash `35.42%`.
- The same page's detailed performance capture contains conflicting/unlabeled duplicate blocks: one block reports SMHC NAV 1-month `-33.52%` and life `-23.14%`, while another block reports life `15.61%`; the detailed YTD field is `--`. Because those blocks lack a single clear matching as-of label and conflict with the dated summary field, they are excluded from the owner metric and recorded as a source conflict.
- The underlying index is not substituted for the fund. The page shows an index 1-month field and separate index-life values, but these do not establish an ETF NAV Total Return series.
- Official SEC materials state that returns are subject to high volatility and tracking risk, the fund primarily invests directly in A-shares through Stock Connect, and the index may rebalance quarterly/reconstitute semi-annually. No reproducible official daily NAV series for maximum drawdown and recovery was identified.

### Calculations and reconciliation

- Available-period window is `2026-06-23` to `2026-08-27`: `65 days / 0.17796 years`, calculated from the source dates. The official summary's `-18.83%` is retained as a cumulative less-than-one-year fund figure; no CAGR or annualization is calculated.
- Start/end NAV TR endpoints are not disclosed, so normalized TR endpoints, tracking difference, up/down years, best/worst year, maximum drawdown and recovery are `not disclosed` or `not calculable`.
- `10-year NAV TR` and `2021-2025 CAGR` are not applicable because inception is `2026-06-23`; `2026 YTD` remains `not disclosed` because the official detailed YTD field is `--` and the dated summary field is since inception rather than calendar-year YTD.
- The cached S&P 500 reference remains separate and no excess-return comparison is calculated because SMHC has no comparable complete calendar-year return series. Currency is USD for the ETF quote/share class, returns are percentages, and the CNY/cash exposure is a separate portfolio snapshot.

### Source-quality choice, gaps, and proposed durable contents

- The dated VanEck summary field is used for the current available-period fund return and NAV/asset snapshot. The detailed duplicate performance blocks are retained as a conflict because their as-of labeling is unclear and their life-return values disagree; no attempt is made to reconcile them by inference.
- The SEC summary prospectus and SAI are the sources of truth for passive classification, fee, listing, index construction, 80% policy, non-diversified status and Stock Connect/risk context. The underlying index figures are not used as ETF returns.
- Proposed `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/performance/ETF_NASDAQ_SMHC Performance.md`: update frontmatter/source batch, current NAV/assets/performance-since-inception/holdings/currency facts, 65-day available-period window, no-YTD/no-10-year gaps, detailed-table conflict and current SEC risk disclosures.
- Proposed `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/comparisons/China ETF.md`: add the current SMHC NAV/assets/holdings/performance-since-inception note while leaving the 2026 YTD column not disclosed and preserving the historical coverage row.
- Proposed `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/performance/ETF Performance Index.md`: update the SMHC coverage row and append the current SMHC status to the `2026-08-29 Performance Refresh` section.
- Proposed `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/raw/imports/ETF_performance_sources_2026-08-29.md`: append this complete source map, observations, calculations, reconciliation, local checklist and handoff.
- Proposed `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/log.md`: append one dated `etf-performance` bullet linking SMHC performance, China navigation, ETF Performance Index and this source batch; preserve unrelated working-tree changes and keep `log.md` unstaged.

### Local pre-save checklist

- PASS: canonical `Nasdaq:SMHC` identity, fund name, Nasdaq listing, inception, passive/index-tracking equity eligibility, tracked index, fee, China region and current source dates are source-mapped.
- PASS: performance-since-inception summary, NAV, market-price/detail-table blocks, index return, holdings, currency exposure, fee, units/currency and all as-of dates are kept separate; duplicate performance conflict is disclosed and no underlying-index or secondary proxy is substituted.
- PASS: under-10-year eligibility, 65-day date calculation, no-annualization rule, no-current-YTD conclusion, no-calendar-CAGR conclusion, cached S&P separation and daily-NAV gap reconcile to the proposed page. No unsupported return is inferred.
- PASS: complete proposed contents for performance, China navigation, ETF Performance Index, source batch and log are specified; breadcrumbs/source links resolve; no critical/high finding remains and no WARNING requires confirmation.
verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official VanEck and SEC sources support the SMHC refresh with a dated available-period performance-since-inception field, current NAV/assets/holdings evidence and passive index classification; scheduled-local verification passed, detailed-table conflicts and no-YTD/no-10-year gaps are disclosed, and no underlying-index or secondary proxy was used.

## VEA — Vanguard FTSE Developed Markets ETF

### Workflow identity and scope

- `workflow: check-etf-performance`; `execution_profile: scheduled-inline`; child card ARI: `ari:cloud:trello::card/workspace/6a78536437ed0b3b544c19e1/6a924381bc27a88452a07e4b`; input ticker `VEA`; canonical `entity_key: NYSE Arca:VEA`.
- The card was claimed and directly reread as `In Progress` before research. Primary region is International; the durable graph is `[[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]`.
- This run creates the VEA performance owner and adds the corresponding International navigation, ETF Performance Index coverage/refresh entry, this source batch and one log bullet. No entity page was found or created.

### Source map and classification

| Source | URL | Use and as-of date |
|---|---|---|
| Official Vanguard VEA product page | https://investor.vanguard.com/investment-products/etfs/profile/vea | Identity, inception `2007-07-20`, index management, asset class, and product performance summary; page capture current to 2026-08-29 |
| Official Vanguard Advisors VEA page | https://advisors.vanguard.com/investments/products/vea/vanguard-ftse-developed-markets-etf | Current NAV TR YTD `18.46%` as of `2026-08-26`, expense ratio `0.03%` as of `2026-04-28`, holdings `3,886`, net assets `USD 230.3bn` as of `2026-07-31`, turnover `4.10%`, exchange and benchmark |
| Official Vanguard VEA investment profile | https://workplace.vanguard.com/assets/corp/fund_communications/pdf_publish/us-products/investment-profiles/0936.pdf | Official 2016-2025 annual NAV total returns, rolling 10-year `10.52%` annualized, 3-year standard deviation `13.88%`, benchmark splice, distributions and portfolio facts as of `2026-06-30` |
| Official Vanguard VEA summary prospectus | https://www.vanguard.com/pub/Pdf/sp936.pdf | NYSE Arca listing, objective, FTSE Developed All Cap ex US Index methodology, fees, passive replication and foreign-market risks; dated `2026-04-28` |
| Cached S&P 500 Total Return convention | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Common USD Total Return reference for complete calendar years `2016-2025`, dividends reinvested, as of `2025-12-31`; cache reused without a new benchmark search |
| Existing vault context | `index.md`, `wiki/analysis/comparisons/International ETF.md`, `wiki/analysis/performance/ETF Performance Index.md` | Routing and navigation context; no existing VEA performance or entity page was present |

- Vanguard and the SEC prospectus classify VEA as a passive, full-replication, index-tracking international equity ETF seeking to track the `FTSE Developed All Cap ex US Index`. The fund invests across large-, mid-, and small-cap companies in Canada, Europe and the Pacific region, so `management_mode: passive-index` and primary region `International` are supported.
- The official prospectus identifies the ETF shares as listed on `NYSE Arca`; the canonical displayed key is therefore `NYSE Arca:VEA`.
- Fund performance figures are NAV total returns, include reinvested dividends and capital-gains distributions, and are net of expenses. The issuer benchmark is kept separate from the common S&P 500 reference.

### Candidate performance claims and raw observations

- Official Vanguard annual NAV TR rows: 2016 `2.51%`, 2017 `26.44%`, 2018 `-14.47%`, 2019 `22.08%`, 2020 `10.29%`, 2021 `11.49%`, 2022 `-15.35%`, 2023 `17.77%`, 2024 `3.07%`, and 2025 `35.15%`.
- Official rolling 10-year NAV TR is `10.52%` annualized for the period ended `2026-06-30`. The source does not disclose raw start/end TR values or a cumulative value for this rolling field, so no normalized endpoint is inferred.
- Current official NAV TR YTD is `18.46%` as of `2026-08-26`. The same current source reports expense ratio `0.03%` as of `2026-04-28`; holdings `3,886` and ETF net assets `USD 230.3bn` as of `2026-07-31`.
- Official portfolio facts as of `2026-06-30` include P/E `18.7x`, P/B `2.2x`, turnover `4.1%`, and 3-year standard deviation `13.88%`. Distribution schedule is quarterly.
- The VEA benchmark is a historical splice: MSCI EAFE through `2013-05-28`, FTSE Developed ex North America through `2015-12-20`, FTSE Developed All Cap ex US Transition Index through `2016-05-31`, and FTSE Developed All Cap ex US thereafter. Benchmark returns are adjusted for withholding taxes.
- No official daily NAV total-return history sufficient to reproduce maximum drawdown and recovery was identified. No secondary market-price or dividend proxy is used.

### Calculations and reconciliation

- From the official annual rows, 2016-2025 compound return is `131.10%` and rounded-input CAGR is `8.74%` using `(Π(1 + annual TR))^(1/10) - 1`.
- For the common 2021-2025 window, VEA compound return is `54.83%` and CAGR is `9.14%`; the cached S&P 500 TR compound is `96.17%` and CAGR is `14.43%`. The cumulative gap is `41.34 percentage points` and CAGR gap is `5.29 pp`.
- VEA has `8` positive and `2` negative complete calendar years. Best is 2025 `+35.15%`; least positive is 2016 `+2.51%`; worst is 2022 `-15.35%`; least bad down year is 2018 `-14.47%`.
- VEA beat the S&P 500 common reference in 2017, 2022 and 2025 (`3 / 10` complete years). This arithmetic comparison is not a manager-skill claim.
- The 10-year issuer field is eligible as a complete rolling window but raw endpoints are not disclosed; the page therefore reports the issuer's `10.52%` annualized field without inventing a cumulative endpoint. Maximum drawdown and recovery remain `ไม่พบข้อมูลที่ยืนยันได้`.

### Source-quality choice, gaps, and proposed durable contents

- The Vanguard investment profile is the source of truth for the complete annual NAV rows, rolling 10-year field, standard deviation and distribution schedule. The Advisors page is used for the fresher current YTD and July fund snapshot. These are retained with separate as-of dates.
- The cached S&P 500 table is used only for its exact 2016-2025 USD total-return convention. It is not substituted for VEA's FTSE benchmark.
- Proposed `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/performance/ETF_NYSE_ARCA_VEA Performance.md`: complete VEA owner page with the required four sections, official annual table, rolling 10-year field, current YTD, calculations, risk gaps, sources, International breadcrumb and canonical geography tag.
- Proposed `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/comparisons/International ETF.md`: add the VEA row and dated refresh note; keep the region page as navigation-only.
- Proposed `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/wiki/analysis/performance/ETF Performance Index.md`: add VEA to the coverage table and `2026-08-29 Performance Refresh`.
- Proposed `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/raw/imports/ETF_performance_sources_2026-08-29.md`: append this source map, observations, calculations, local checklist and handoff.
- Proposed `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/log.md`: append one dated `etf-performance` bullet linking VEA performance, International navigation, ETF Performance Index and this source batch; preserve the existing unrelated working-tree change and keep `log.md` unstaged.

### Local pre-save checklist

- PASS: canonical `NYSE Arca:VEA` identity, fund name, inception, passive/index-tracking equity eligibility, FTSE benchmark, expense ratio, International region and official source dates are mapped.
- PASS: NAV Total Return, market-price return, price, benchmark splice, holdings, expense, standard deviation and distribution facts remain separate; current YTD uses the freshest official capture and no proxy is introduced.
- PASS: 10-year issuer field, annual-row CAGR, 2021-2025 comparison, best/worst ranking, S&P cache basis, 8/2 up/down count and daily-NAV drawdown gap reconcile to the proposed owner page and index/region notes.
- PASS: all planned links and breadcrumbs resolve; the performance page owns the numbers; the region page remains static; no critical/high finding remains and no WARNING requires confirmation.
verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official Vanguard and SEC sources confirm VEA as a passive NYSE Arca developed-markets ETF with complete 2016-2025 NAV rows, rolling 10-year and current-YTD evidence; scheduled-local verification passed and raw-endpoint and daily-drawdown gaps remain explicitly disclosed.
