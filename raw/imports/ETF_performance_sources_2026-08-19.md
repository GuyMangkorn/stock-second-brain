---
type: etf-performance-source-batch
date: 2026-08-19
workflow: check-etf-performance
execution_profile: scheduled-inline
verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS
---

# ETF Performance Source Batch — 2026-08-19

ชุดข้อมูลนี้เป็น evidence packet และ source ledger ของ workflow
`check-etf-performance` แบบ `scheduled-inline`. การตรวจ pre-save ทำใน
top-level context เดิมครบทุกข้อ และไม่มีการ dispatch worker, reviewer หรือ
`source_verifier`.

## VWCG — Vanguard FTSE Developed Europe UCITS ETF (EUR) Accumulating / VNGLF alias

### Identity and classification

- `entity_key: Euronext Amsterdam:VWCG`; input ticker `VNGLF`; canonical exchange `Euronext Amsterdam`; fund `Vanguard FTSE Developed Europe UCITS ETF (EUR) Accumulating`; ISIN `IE00BK5BQX27`; share-class inception `2019-07-23`; listing `2019-07-25`.
- `management_mode: passive-index`; tracked index `FTSE Developed Europe Index`; official EUR share class; physical acquisition with sampling where full replication is not practicable.
- `return_basis: NAV total return` with income reinvested, net of expenses, EUR; accumulation share class has no cash distribution schedule.
- Primary region: `Europe`; region page `[[Europe ETF]]` and canonical geography tag `geography/Europe`.

### Source map

| Source | URL/path | Use |
|---|---|---|
| Vanguard product page | https://www.vanguard.co.uk/professional/product/etf/equity/9681/vanguard-ftse-developed-europe-ucits-etf-eur-accumulating | official identity, canonical exchange/ticker mapping, inception, benchmark, current NAV, assets, holdings and exposures |
| Vanguard factsheet | https://fund-docs.vanguard.com/FTSE_Developed_Europe_UCITS_ETF_EUR_Accumulating_9681_EU_INT_UK_EN.pdf | official fee, performance summary, current YTD, rolling returns, tracking error and dated fund facts as of 2026-07-31 |
| Vanguard KID | https://fund-docs.vanguard.com/ie00bk5bqx27-en.pdf | official EUR calendar rows 2020-2025, index rows and accumulation disclosure; accurate 2026-02-17 |
| Cached S&P 500 Total Return convention | workflow cache and original URLs in `check-etf-performance/SKILL.md` | USD calendar rows 2020-2025, dividends reinvested, as of 2025-12-31; no new search because the window is within cached 2016-2025 |

### Raw observations

- Vanguard identifies the EUR accumulating share class as `VWCG` on NYSE Euronext - Amsterdam, with the same ISIN across listed currencies/exchanges; the input OTC label `VNGLF` is retained as an alias and not used as the displayed entity key.
- Official KID calendar NAV/index rows in EUR: 2020 `-2.6% / -2.7%`, 2021 `25.2% / 24.9%`, 2022 `-10.0% / -10.2%`, 2023 `16.5% / 16.2%`, 2024 `9.4% / 9.1%`, 2025 `19.9% / 19.5%`. The 2019 launch-year partial is not used because no verified partial return was retained.
- Official factsheet as of 2026-07-31: fund NAV TR YTD `12.06%`, 1Y `22.47%`, 3Y `14.60%`, 5Y `10.39%`, since inception `10.44%`; benchmark YTD `11.78%`, 1Y `22.12%`, 3Y `14.28%`, 5Y `10.05%`, since inception `10.14%`. The factsheet states NAV-to-NAV, gross income invested and net of fund expenses for the fund.
- Official product-page NAV snapshot: `€60.9809` at closure on 2026-08-17. Fund total assets are `€7.678B` and share-class assets `€2.902B` as of 2026-07-31; 513 stocks and country weights include UK `23.21%`, France `14.67%`, Switzerland `14.44%`, Germany `13.33%`, and Netherlands `8.14%`.
- Official OCF is `0.10%`; accumulation shares reinvest income and show no cash distribution frequency. Official annualized tracking error is `0.14%` for 1, 3 and 5 years as of 2026-07-31. Official daily NAV maximum drawdown and recovery date were not disclosed in the reviewed sources.
- Cached S&P 500 TR rows used for the common reference are USD: 2020 `18.40%`, 2021 `28.71%`, 2022 `-18.11%`, 2023 `26.29%`, 2024 `25.02%`, 2025 `17.88%`; the EUR/USD basis mismatch is explicitly preserved.

### Calculations and reconciliation

- `Cumulative = ∏(1 + annual return) - 1`: VWCG 2020-2025 `67.71%`, rounded-input CAGR `9.00%`, population annual-return standard deviation `12.45%`, up/down `5/1`, best `2021 +25.20%`, least positive `2024 +9.40%`, worst/least-bad down year `2020 -2.60%`.
- VWCG 2021-2025 compounds to `72.19%` / rounded-input CAGR `11.48%`; the FTSE index compounds to `69.92%` / `11.19%`. Approximate fund-minus-index differences are `+0.30 pp` over 2021-2025 and `+0.26 pp` over 2020-2025; these are passive tracking observations, not alpha.
- Cached S&P 500 TR compounds to `132.26%` / `15.08%` over 2020-2025 and `96.17%` / `14.43%` over 2021-2025. No direct excess return is calculated because the ETF return is EUR and the common reference is USD.
- 10-year NAV TR CAGR is not applicable: the share class inception is 2019-07-23 and the official history is shorter than 10 years.

### Planned durable paths and contents

- Create `wiki/analysis/performance/ETF_EURONEXT_AMSTERDAM_VWCG Performance.md` with the canonical `Euronext Amsterdam:VWCG` identity, `input_ticker: VNGLF`, EUR NAV/index/S&P annual table, under-10-year rule, current YTD/NAV dates, tracking-risk evidence, source links, `geography/Europe` tag and breadcrumb.
- Update `wiki/analysis/comparisons/Europe ETF.md` with the VWCG row and current-date/under-10-year note.
- Update `wiki/analysis/comparisons/ETF Region Index.md` Europe count from `17` to `18` and preserve the existing navigation graph.
- Update `wiki/analysis/performance/ETF Performance Index.md` with the VWCG coverage row, 2021-2025 Common Window row and 2026-08-19 coverage bullet.
- Append one `log.md` workflow bullet; no entity hub or `raw/funds/` file is planned because this workflow owns the numeric performance page.

### Local pre-save checklist

- PASS: canonical ticker/exchange mapping, fund name, ISIN, inception/listing dates, passive eligibility, FTSE benchmark, OCF, accumulation/distribution treatment, NAV TR definition, EUR currency, annual rows, current YTD/NAV and all as-of dates are source-backed.
- PASS: official calendar rows are separated from rolling/current fields and from the cached S&P USD reference; no cross-currency excess return is claimed; passive tracking differences are not called alpha.
- PASS: the 2019 partial and daily NAV drawdown/recovery remain explicitly disclosed as gaps; best/worst and up/down counts use only the six complete official years.
- PASS: complete proposed performance page, source batch section, Europe row/count, performance-index row/Common Window/bullet and log bullet are specified; canonical breadcrumb, `geography/Europe` tag and planned wikilinks resolve.
- PASS: no unresolved High/Medium finding blocks the write and no WARNING requiring confirmation remains. Required scheduled audit lines are present: `verification_mode: scheduled-local` and `reviewer_dispatch: not-attempted-by-design`.

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official Vanguard identity, passive classification, EUR annual NAV/index rows, current YTD evidence and the scheduled-local pre-save checklist passed; VWCG artifacts were written with the VNGLF alias and currency separation disclosed.

## VEUR — Vanguard FTSE Developed Europe UCITS ETF (EUR) Distributing / VFDEF alias

### Identity and classification

- `entity_key: Euronext Amsterdam:VEUR`; input ticker `VFDEF`; canonical exchange `Euronext Amsterdam`; fund `Vanguard FTSE Developed Europe UCITS ETF (EUR) Distributing`; ISIN `IE00B945VV12`; share-class inception `2013-05-21`; listing `2013-05-22`.
- `management_mode: passive-index`; tracked index `FTSE Developed Europe Index`; official EUR share class; physical acquisition with sampling where full replication is not practicable.
- `return_basis: NAV total return` with income reinvested for performance measurement, net of expenses, EUR; the share class pays income out and distributes quarterly.
- Primary region: `Europe`; region page `[[Europe ETF]]` and canonical geography tag `geography/Europe`.

### Source map

| Source | URL/path | Use |
|---|---|---|
| Vanguard product page | https://www.vanguard.co.uk/professional/product/etf/equity/9520/vanguard-ftse-developed-europe-ucits-etf-eur-distributing | official identity, canonical exchange/ticker mapping, inception, benchmark, current NAV, distributions, holdings and exposures |
| Vanguard factsheet | https://fund-docs.vanguard.com/FTSE_Developed_Europe_UCITS_ETF_EUR_Distributing_9520_EU_INT_EN.pdf | official fee, performance summary, current YTD, rolling returns, tracking error and dated fund facts as of 2026-07-31 |
| Vanguard KID | https://fund-docs.vanguard.com/ie00b945vv12-en.pdf | official EUR calendar rows 2016-2025, index rows, ongoing charges and distributing-share disclosure; accurate 2026-02-17 |
| Cached S&P 500 Low Volatility historical comparison | https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true | cached S&P 500 TR rows for 2016-2019 |
| S&P U.S. Equities Market Attributes July 2023 | https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf | cached S&P 500 TR rows for 2018-2022 |
| S&P U.S. Equities Market Attributes December 2021 | https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/ | cached S&P 500 TR row for 2021 |
| S&P U.S. Equities Market Attributes December 2025 | https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/ | cached S&P 500 TR rows for 2022-2025 |
| S&P 500 index page | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | index definition and methodology context |

### Raw observations

- Vanguard identifies the EUR Euronext Amsterdam exchange ticker as `VEUR`; the input OTC label `VFDEF` is retained as an alias and not used as the displayed entity key. The base currency is EUR and the official distributing share-class ISIN is `IE00B945VV12`.
- Official KID calendar NAV/index rows in EUR: 2016 `2.8% / 2.5%`, 2017 `10.7% / 10.5%`, 2018 `-10.5% / -10.7%`, 2019 `26.4% / 26.1%`, 2020 `-2.6% / -2.7%`, 2021 `25.2% / 24.9%`, 2022 `-10.0% / -10.2%`, 2023 `16.5% / 16.2%`, 2024 `9.4% / 9.1%`, 2025 `19.9% / 19.5%`. KID states that the rows include ongoing charges and reinvestment of income, are calculated in EUR, and the share class launched in 2013.
- Official factsheet as of 2026-07-31: fund NAV TR YTD `12.06%`, 1Y `22.47%`, 3Y `14.60%`, 5Y `10.39%`, 10Y `9.66%`, since inception `8.73%`; benchmark YTD `11.78%`, 1Y `22.12%`, 3Y `14.28%`, 5Y `10.05%`, 10Y `9.38%`, since inception `8.45%`. The factsheet states NAV-to-NAV, gross income invested, and fund performance net of expenses in EUR.
- Official product-page NAV snapshot: `€50.7466` at closure on 2026-08-17. Fund total assets are `€7.678B` and share-class assets `€4.776B` as of 2026-07-31; 513 stocks and country weights include UK `23.21%`, France `14.67%`, Switzerland `14.44%`, Germany `13.33%`, and Netherlands `8.14%`.
- Official OCF is `0.10%`; distribution schedule is quarterly. Latest four verified cash distributions are `€0.1609` ex 2025-09-18, `€0.1676` ex 2025-12-18, `€0.1815` ex 2026-03-19, and `€0.7814` ex 2026-06-18, summing to `€1.2914` per unit. The product page displays `Historical performance` `2.58%` as of 2026-07-31; the label is preserved without treating it as a forecast.
- Official annualized tracking error is `0.14%` for 1, 3 and 5 years as of 2026-07-31. The product page also shows a GBP market-price snapshot; it is not used as the EUR NAV return. Official daily NAV maximum drawdown and recovery date were not disclosed in the reviewed sources.
- Cached S&P 500 TR rows used for the common reference are USD: 2016 `11.96%`, 2017 `21.83%`, 2018 `-4.38%`, 2019 `31.49%`, 2020 `18.40%`, 2021 `28.71%`, 2022 `-18.11%`, 2023 `26.29%`, 2024 `25.02%`, 2025 `17.88%`; reference window is complete calendar years 2016-2025, implied endpoints 2015-12-31 to 2025-12-31, as of 2025-12-31, dividends reinvested, not price return or net total return.

### Calculations and reconciliation

- `Cumulative = ∏(1 + annual return) - 1`: VEUR 2016-2025 `115.91%`, rounded-input CAGR `8.00%`, population annual-return standard deviation `12.87%`, up/down `7/3`, best `2019 +26.40%`, least positive `2016 +2.80%`, worst `2018 -10.50%`, least-bad down year `2020 -2.60%`.
- VEUR 2021-2025 compounds to `72.19%` / rounded-input CAGR `11.48%`; the FTSE index compounds to `69.92%` / `11.19%`. Approximate fund-minus-index differences are `+0.30 pp` over 2021-2025 and `+0.26 pp` over 2016-2025; these are passive tracking observations, not alpha.
- Cached S&P 500 TR compounds to `298.33%` / `14.82%` over 2016-2025 and `96.17%` / `14.43%` over 2021-2025. No direct excess return is calculated because the ETF return is EUR and the common reference is USD.
- The issuer's rolling 10-year NAV TR field is `9.66%` as of 2026-07-31; it is kept separate from the complete-calendar 2016-2025 CAGR `8.00%`.

### Planned durable paths and contents

- Create `wiki/analysis/performance/ETF_EURONEXT_AMSTERDAM_VEUR Performance.md` with canonical `Euronext Amsterdam:VEUR` identity, `input_ticker: VFDEF`, EUR NAV/index/S&P annual table, rolling-versus-calendar 10-year distinction, current YTD/NAV/distribution dates, tracking-risk evidence, source links, `geography/Europe` tag and breadcrumb.
- Update `wiki/analysis/comparisons/Europe ETF.md` with the VEUR row and current-date/distribution note.
- Update `wiki/analysis/comparisons/ETF Region Index.md` Europe count from `18` to `19` and preserve the existing navigation graph.
- Update `wiki/analysis/performance/ETF Performance Index.md` with the VEUR coverage row, 2021-2025 Common Window row and 2026-08-19 coverage bullet.
- Append one `log.md` workflow bullet; no entity hub or `raw/funds/` file is planned because this workflow owns the numeric performance page.

### Local pre-save checklist

- PASS: canonical ticker/exchange mapping, fund name, ISIN, inception/listing dates, passive eligibility, FTSE benchmark, OCF, distributing/quarterly treatment, NAV TR definition, EUR currency, annual rows, rolling 10Y, current YTD/NAV/distributions and all as-of dates are source-backed.
- PASS: official calendar rows are separated from rolling/current fields and from the cached S&P USD reference; no cross-currency excess return is claimed; passive tracking differences are not called alpha.
- PASS: complete 2016-2025 annual history supports the 10-year calendar calculation; the issuer rolling 10-year field remains separately labeled; daily NAV drawdown/recovery remains explicitly disclosed as a gap.
- PASS: complete proposed performance page, source batch section, Europe row/count, performance-index row/Common Window/bullet and log bullet are specified; canonical breadcrumb, `geography/Europe` tag and planned wikilinks resolve.
- PASS: no unresolved High/Medium finding blocks the write and no WARNING requiring confirmation remains. Required scheduled audit lines are present: `verification_mode: scheduled-local` and `reviewer_dispatch: not-attempted-by-design`.

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official Vanguard identity, passive classification, EUR 2016-2025 NAV/index rows, rolling 10-year field, current YTD/distribution evidence and the scheduled-local pre-save checklist passed; VEUR artifacts were written with the VFDEF alias and currency separation disclosed.

## IEUR — iShares Core MSCI Europe ETF

### Identity and classification

- `entity_key: NYSE Arca:IEUR`; input ticker `IEUR`; canonical exchange `NYSE Arca`; fund `iShares Core MSCI Europe ETF`; CUSIP `46434V738`; inception `2014-06-10`.
- `management_mode: passive-index`; tracked index `MSCI Europe IMI Index (Net)`; U.S.-domiciled USD share class; equity ETF targeting large-, mid- and small-cap developed-European equities.
- `return_basis: NAV total return` with income and capital gains reinvested for performance measurement, net of expenses, USD; market-price return kept separate.
- Primary region: `Europe`; region page `[[Europe ETF]]` and canonical geography tag `geography/Europe`.

### Source map

| Source | URL/path | Use |
|---|---|---|
| iShares product page | https://www.ishares.com/us/products/264617/IEUR | official identity, NYSE Arca listing, current NAV/YTD, price/NAV, holdings, geography, distributions and performance tables; current page capture as of 2026-08-17 |
| iShares factsheet | https://www.ishares.com/us/literature/fact-sheet/ieur-ishares-core-msci-europe-etf-fund-fact-sheet-en-us.pdf | official 2021-2025 calendar rows, rolling annualized fields, fee, distributions and dated fund facts as of 2026-06-30 |
| iShares summary prospectus | https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-core-msci-europe-etf-7-31.pdf | official investment objective, risks and fee disclosures |
| Cached S&P 500 Total Return convention | original URLs and cache table recorded in the VEUR section above; same workflow cache is reused for the 2021-2025 subset | USD calendar rows 2021-2025, dividends reinvested, as of 2025-12-31; no new search because the window is within cached 2016-2025 |

### Raw observations

- iShares identifies the fund as `IEUR` on NYSE Arca with CUSIP `46434V738`, inception `2014-06-10`, benchmark `MSCI Europe IMI Index (Net)`, and semi-annual distribution frequency. The fund is a passive equity ETF for developed European large-, mid- and small-cap stocks.
- Official factsheet calendar NAV/index rows in USD: 2021 `16.21% / 16.13%`, 2022 `-16.18% / -16.71%`, 2023 `19.83% / 19.52%`, 2024 `1.70% / 1.49%`, 2025 `35.11% / 35.08%`. The factsheet states the hypothetical growth series assumes reinvestment of dividends/capital gains and deducts fund expenses.
- Official factsheet as of 2026-06-30: NAV TR 1Y `17.19%`, 3Y `16.18%`, 5Y `9.07%`, 10Y `10.02%`, since inception `6.54%`; benchmark 1Y `17.42%`, 3Y `15.87%`, 5Y `8.74%`, 10Y `9.74%`, since inception `6.26%`. Expense ratio is `0.10%`, 3-year standard deviation is `13.69%` in the factsheet.
- Current official product page as of 2026-08-17: NAV `US$77.83`, closing price `US$78.05`, NAV TR YTD `12.03%`, net assets `US$9.402B`, and 1,009 holdings. Product-page 3-year standard deviation is `13.67%` as of 2026-07-31; geography includes UK `22.71%`, France `14.47%`, Switzerland `13.72%`, Germany `13.25%`, and Netherlands `8.76%` as of 2026-08-17.
- Official product-page distribution history: income `US$1.542483` with payable date 2026-06-18 and `US$0.849102` with payable date 2025-12-19; latest two verified payments sum to `US$2.391585` per unit. Product page also shows 30-day SEC yield `2.39%` and 12-month trailing yield `3.11%` as of 2026-07-31; these are not NAV TR.
- Cached S&P 500 TR rows used for the common reference are USD: 2021 `28.71%`, 2022 `-18.11%`, 2023 `26.29%`, 2024 `25.02%`, 2025 `17.88%`; reference window is complete calendar years 2016-2025, implied endpoints 2015-12-31 to 2025-12-31, as of 2025-12-31, dividends reinvested, not price return or net total return.
- Official daily NAV maximum drawdown and recovery date were not disclosed in the reviewed sources.

### Calculations and reconciliation

- `Cumulative = ∏(1 + annual return) - 1`: IEUR 2021-2025 `60.39%`, rounded-input CAGR `9.91%`, population annual-return standard deviation `17.38%`, up/down `4/1`, best `2025 +35.11%`, least positive `2024 +1.70%`, worst/least-bad down year `2022 -16.18%`.
- IEUR 2021-2025 compounds to `60.39%` / rounded-input CAGR `9.91%`; the MSCI index compounds to `58.49%` / `9.65%`. The approximate `+0.26 pp` fund-minus-index difference is a passive tracking observation, not alpha.
- Cached S&P 500 TR compounds to `96.17%` / `14.43%` over 2021-2025. It is the required common USD reference, not the issuer benchmark.
- The issuer's rolling 10-year NAV TR field is `10.02%` as of 2026-06-30; it is kept separate from the calendar-derived 2021-2025 CAGR `9.91%`.

### Planned durable paths and contents

- Create `wiki/analysis/performance/ETF_NYSE_ARCA_IEUR Performance.md` with canonical `NYSE Arca:IEUR` identity, USD NAV/index/S&P annual table, rolling-versus-calendar distinction, current YTD/NAV/price/distribution dates, risk evidence, source links, `geography/Europe` tag and breadcrumb.
- Update `wiki/analysis/comparisons/Europe ETF.md` with the IEUR row and current-date/distribution note.
- Update `wiki/analysis/comparisons/ETF Region Index.md` Europe count from `19` to `20` and preserve the existing navigation graph.
- Update `wiki/analysis/performance/ETF Performance Index.md` with the IEUR coverage row, 2021-2025 Common Window row and 2026-08-19 coverage bullet.
- Append one `log.md` workflow bullet; no entity hub or `raw/funds/` file is planned because this workflow owns the numeric performance page.

### Local pre-save checklist

- PASS: canonical ticker/exchange mapping, fund name, CUSIP, inception date, passive eligibility, MSCI benchmark, expense ratio, semi-annual distribution treatment, NAV TR definition, USD currency, annual rows, rolling 10Y, current YTD/NAV/price/distributions and all as-of dates are source-backed.
- PASS: official calendar rows are separated from rolling/current fields and from the cached S&P USD reference; market-price return, yields and NAV TR are not mixed; passive tracking differences are not called alpha.
- PASS: available complete annual history is correctly limited to 2021-2025; the issuer rolling 10-year field remains separately labeled; daily NAV drawdown/recovery remains explicitly disclosed as a gap.
- PASS: complete proposed performance page, source batch section, Europe row/count, performance-index row/Common Window/bullet and log bullet are specified; canonical breadcrumb, `geography/Europe` tag and planned wikilinks resolve.
- PASS: no unresolved High/Medium finding blocks the write and no WARNING requiring confirmation remains. Required scheduled audit lines are present: `verification_mode: scheduled-local` and `reviewer_dispatch: not-attempted-by-design`.

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official iShares identity, passive classification, USD 2021-2025 NAV/index rows, rolling 10-year field, current YTD/price/distribution evidence and the scheduled-local pre-save checklist passed; IEUR artifacts were written with the USD benchmark basis disclosed.

## SPEU — State Street SPDR Portfolio Europe ETF

### Identity and classification

- `entity_key: NYSE Arca:SPEU`; input ticker `SPEU`; canonical exchange `NYSE Arca`; fund `State Street SPDR Portfolio Europe ETF`; CUSIP `78463X103`; ISIN `US78463X1037`; inception `2002-10-15`.
- `management_mode: passive-index`; tracked index `STOXX Europe Total Market Index`; official USD share class; State Street describes sampling and broad Western Europe exposure across the market-cap spectrum.
- `return_basis: official NAV total return` with dividends/capital gains reinvested, net of fees, USD; market-value return separate. The annual table uses a secondary total-return proxy because official annual calendar rows were not present in the reviewed State Street capture.
- Primary region: `Europe`; region page `[[Europe ETF]]` and canonical geography tag `geography/Europe`.

### Source map

| Source | URL/path | Use |
|---|---|---|
| State Street product page | https://www.ssga.com/us/en/individual/etfs/state-street-spdr-portfolio-europe-etf-speu | official identity, listing, inception, benchmark-history change, NAV/AUM, current facts, yields, holdings/geography and rolling performance |
| State Street factsheet | https://www.ssga.com/library-content/products/factsheets/etfs/us/factsheet-us-en-speu.pdf | official NAV/benchmark performance, fee, holdings, country/sector facts as of 2026-06-30 |
| State Street historical distributions page | https://www.ssga.com/us/en/individual/resources/documents/etf-dividend-distributions | official distribution-history route and frequency context; no SPEU row was exposed in the reviewed page capture |
| FinanceCharts SPEU total-return history | https://www.financecharts.com/stocks/SPEU/performance/total-return | secondary dividend-reinvested total-return proxy for calendar rows 2021-2025; not official NAV; marked `*` |
| Cached S&P 500 Total Return convention | original URLs and cache table recorded in the VEUR section above; same workflow cache is reused for the 2021-2025 subset | USD calendar rows 2021-2025, dividends reinvested, as of 2025-12-31; no new search because the window is within cached 2016-2025 |

### Raw observations

- State Street identifies `SPEU` on NYSE Arca with base currency USD, CUSIP `78463X103`, ISIN `US78463X1037`, inception `2002-10-15`, and quarterly distributions. The fund seeks to track the STOXX Europe Total Market Index using sampling.
- Official State Street performance as of 2026-06-30: NAV TR YTD `7.29%`, 1Y `17.82%`, 3Y `16.35%`, 5Y `9.12%`, 10Y `9.76%`, since inception `6.89%`; linked benchmark `7.07% / 17.60% / 16.11% / 8.86% / 9.63% / 6.87%`. All results assume reinvestment of dividends/capital gains and are net of fees for the fund.
- State Street benchmark-history note: benchmark returns reflect the STOXX Europe 50 Index from inception through 2023-09-22 and the STOXX Europe Total Market Index from 2023-09-23 onward. This is retained as a methodology break rather than silently treating the whole history as one unchanged index.
- Official product/fund facts as of 2026-07-17 to 2026-07-21: NAV `US$54.97`, AUM `US$714.59M`, gross expense ratio `0.07%`, holdings `1,684`, 30-day SEC yield `2.43%`, fund distribution yield `3.44%`, and country weights UK `21.99%`, France `14.75%`, Switzerland `13.96%`, Germany `12.72%`, Netherlands `8.30%`.
- Official State Street capture did not expose complete calendar-year NAV rows. FinanceCharts secondary total-return proxy rows used only for historical context are 2021 `16.20%*`, 2022 `-15.97%*`, 2023 `19.84%*`, 2024 `1.94%*`, 2025 `35.80%*`; the page describes total return as price appreciation plus reinvested dividends, not issuer NAV.
- Latest official YTD after 2026-06-30 was not disclosed in the reviewed State Street capture. The later official NAV snapshot is retained as a price/fund-facts observation, not relabeled as a later YTD. Official daily NAV maximum drawdown and recovery date were not disclosed.
- Cached S&P 500 TR rows used for the common reference are USD: 2021 `28.71%`, 2022 `-18.11%`, 2023 `26.29%`, 2024 `25.02%`, 2025 `17.88%`; reference window is complete calendar years 2016-2025, implied endpoints 2015-12-31 to 2025-12-31, as of 2025-12-31, dividends reinvested, not price return or net total return.

### Calculations and reconciliation

- `Cumulative = ∏(1 + annual return) - 1`: secondary SPEU proxy 2021-2025 `61.99%*`, rounded-input CAGR `10.13%*`, population annual-return standard deviation `17.48%*`, up/down `4/1`, best `2025 +35.80%*`, least positive `2024 +1.94%*`, worst/least-bad down year `2022 -15.97%*`.
- Cached S&P 500 TR compounds to `96.17%` / `14.43%` over 2021-2025. It is the common USD reference, not the issuer benchmark; no manager-skill or alpha claim is made.
- Official rolling NAV TR fields remain the source of truth: `9.76%` 10-year annualized as of 2026-06-30, separate from the secondary `10.13%*` calendar proxy. No fund-minus-index calculation is made from the secondary annual proxy.

### Planned durable paths and contents

- Create `wiki/analysis/performance/ETF_NYSE_ARCA_SPEU Performance.md` with canonical `NYSE Arca:SPEU` identity, official rolling NAV/benchmark fields, secondary annual proxy table marked `*`, benchmark-history change, current NAV/YTD limitation, risk evidence, source links, `geography/Europe` tag and breadcrumb.
- Update `wiki/analysis/comparisons/Europe ETF.md` with the SPEU row and official-versus-secondary/as-of note.
- Update `wiki/analysis/comparisons/ETF Region Index.md` Europe count from `20` to `21` and preserve the existing navigation graph.
- Update `wiki/analysis/performance/ETF Performance Index.md` with the SPEU coverage row, 2021-2025 Common Window row and 2026-08-19 coverage bullet.
- Append one `log.md` workflow bullet; no entity hub or `raw/funds/` file is planned because this workflow owns the numeric performance page.

### Local pre-save checklist

- PASS: canonical ticker/exchange mapping, fund name, identifiers, inception date, passive eligibility, STOXX benchmark, documented index-history change, expense ratio, quarterly treatment, official NAV/benchmark definitions, USD currency, current NAV/fund facts and as-of dates are source-backed.
- PASS: secondary annual rows are explicitly marked `*` and never presented as official NAV; official rolling/YTD fields are kept separate; market-value return, distribution yield and NAV TR are not mixed.
- PASS: S&P cached rows are disclosed as a USD common reference; no direct fund-minus-index or alpha claim uses the secondary proxy; current-YTD limitation and daily NAV drawdown/recovery remain explicit gaps.
- PASS: complete proposed performance page, source batch section, Europe row/count, performance-index row/Common Window/bullet and log bullet are specified; canonical breadcrumb, `geography/Europe` tag and planned wikilinks resolve.
- PASS: no unresolved High/Medium finding blocks the write and no WARNING requiring confirmation remains. Required scheduled audit lines are present: `verification_mode: scheduled-local` and `reviewer_dispatch: not-attempted-by-design`.

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official State Street identity, passive classification, rolling NAV/benchmark evidence, disclosed benchmark-history change, marked secondary annual proxy and the scheduled-local pre-save checklist passed; SPEU artifacts were written with the issuer-YTD limitation and source-quality boundary disclosed.

## IEV — iShares Europe ETF

### Identity and classification

- `entity_key: NYSE Arca:IEV`; input ticker `IEV`; canonical exchange `NYSE Arca`; fund `iShares Europe ETF`; CUSIP `464287861`; inception `2000-07-25`.
- `management_mode: passive-index`; tracked index `S&P Europe 350 Index (Net)`; U.S.-domiciled USD share class; broad developed-European equity exposure.
- `return_basis: NAV total return` with income/capital gains reinvested for performance measurement, net of expenses, USD; market-price return kept separate.
- Primary region: `Europe`; region page `[[Europe ETF]]` and canonical geography tag `geography/Europe`.

### Source map

| Source | URL/path | Use |
|---|---|---|
| iShares product page | https://www.ishares.com/us/products/239736/IEV | official identity, NYSE Arca listing, current NAV/YTD, price/NAV, holdings, geography, distributions and performance tables; current page capture as of 2026-08-17 |
| iShares factsheet | https://www.ishares.com/us/literature/fact-sheet/iev-ishares-europe-etf-fund-fact-sheet-en-us.pdf | official 2021-2025 calendar rows, rolling annualized fields, fee, distributions and dated fund facts as of 2026-06-30 |
| iShares prospectus | https://www.ishares.com/us/literature/prospectus/p-ishares-europe-etf-3-31.pdf | official investment objective, fee and risk disclosures |
| Cached S&P 500 Total Return convention | original URLs and cache table recorded in the VEUR section above; same workflow cache is reused for the 2021-2025 subset | USD calendar rows 2021-2025, dividends reinvested, as of 2025-12-31; no new search because the window is within cached 2016-2025 |

### Raw observations

- iShares identifies the fund as `IEV` on NYSE Arca with CUSIP `464287861`, inception `2000-07-25`, benchmark `S&P Europe 350 Index (Net)`, semi-annual distribution frequency, and equity asset class.
- Official factsheet calendar NAV/index rows in USD: 2021 `16.34% / 16.62%`, 2022 `-14.16% / -14.75%`, 2023 `19.82% / 20.20%`, 2024 `1.71% / 2.10%`, 2025 `35.02% / 35.78%`. The factsheet states the hypothetical growth series assumes reinvestment of dividends/capital gains and deducts fund expenses.
- Official factsheet as of 2026-06-30: NAV TR 1Y `18.26%`, 3Y `16.07%`, 5Y `9.64%`, 10Y `9.87%`, since inception `5.15%`; benchmark 1Y `19.03%`, 3Y `16.38%`, 5Y `9.75%`, 10Y `10.09%`; expense ratio `0.60%`, 3-year standard deviation `13.39%`.
- Current official product page as of 2026-08-17: NAV `US$75.37`, closing price `US$75.42`, NAV TR YTD `11.94%`, net assets `US$1.692B`, and 360 holdings. Product-page 3-year standard deviation is `13.38%` as of 2026-07-31; geography includes UK `22.90%`, France `15.31%`, Switzerland `14.14%`, Germany `13.55%`, and Netherlands `8.76%` as of 2026-08-17.
- Official product-page distribution history: income `US$1.280576` with payable date 2026-06-18 and `US$0.751330` with payable date 2025-12-19; latest two verified payments sum to `US$2.031906` per unit. Product page also shows 30-day SEC yield `1.94%` and 12-month trailing yield `2.72%` as of 2026-07-31; these are not NAV TR.
- Cached S&P 500 TR rows used for the common reference are USD: 2021 `28.71%`, 2022 `-18.11%`, 2023 `26.29%`, 2024 `25.02%`, 2025 `17.88%`; reference window is complete calendar years 2016-2025, implied endpoints 2015-12-31 to 2025-12-31, as of 2025-12-31, dividends reinvested, not price return or net total return.
- Official daily NAV maximum drawdown and recovery date were not disclosed in the reviewed sources.

### Calculations and reconciliation

- `Cumulative = ∏(1 + annual return) - 1`: IEV 2021-2025 `64.33%`, rounded-input CAGR `10.44%`, population annual-return standard deviation `16.73%`, up/down `4/1`, best `2025 +35.02%`, least positive `2024 +1.71%`, worst/least-bad down year `2022 -14.16%`.
- IEV 2021-2025 compounds to `64.33%` / rounded-input CAGR `10.44%`; the S&P Europe 350 rows compound to `65.67%` / `10.62%`. The approximate `-0.18 pp` fund-minus-index difference is a passive tracking observation, not alpha.
- Cached S&P 500 TR compounds to `96.17%` / `14.43%` over 2021-2025. It is the common USD reference, not the issuer benchmark.
- The issuer's rolling 10-year NAV TR field is `9.87%` as of 2026-06-30; it is kept separate from the calendar-derived 2021-2025 CAGR `10.44%`.

### Planned durable paths and contents

- Create `wiki/analysis/performance/ETF_NYSE_ARCA_IEV Performance.md` with canonical `NYSE Arca:IEV` identity, USD NAV/index/S&P annual table, rolling-versus-calendar distinction, current YTD/NAV/price/distribution dates, risk evidence, source links, `geography/Europe` tag and breadcrumb.
- Update `wiki/analysis/comparisons/Europe ETF.md` with the IEV row and current-date/distribution note.
- Update `wiki/analysis/comparisons/ETF Region Index.md` Europe count from `21` to `22` and preserve the existing navigation graph.
- Update `wiki/analysis/performance/ETF Performance Index.md` with the IEV coverage row, 2021-2025 Common Window row and 2026-08-19 coverage bullet.
- Append one `log.md` workflow bullet; no entity hub or `raw/funds/` file is planned because this workflow owns the numeric performance page.

### Local pre-save checklist

- PASS: canonical ticker/exchange mapping, fund name, CUSIP, inception date, passive eligibility, S&P Europe 350 benchmark, expense ratio, semi-annual distribution treatment, NAV TR definition, USD currency, annual rows, rolling 10Y, current YTD/NAV/price/distributions and all as-of dates are source-backed.
- PASS: official calendar rows are separated from rolling/current fields and from the cached S&P USD reference; market-price return, yields and NAV TR are not mixed; passive tracking differences are not called alpha.
- PASS: complete 2021-2025 history supports the calendar calculation; the issuer rolling 10-year field remains separately labeled; daily NAV drawdown/recovery remains explicitly disclosed as a gap.
- PASS: complete proposed performance page, source batch section, Europe row/count, performance-index row/Common Window/bullet and log bullet are specified; canonical breadcrumb, `geography/Europe` tag and planned wikilinks resolve.
- PASS: no unresolved High/Medium finding blocks the write and no WARNING requiring confirmation remains. Required scheduled audit lines are present: `verification_mode: scheduled-local` and `reviewer_dispatch: not-attempted-by-design`.

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official iShares identity, passive classification, USD 2021-2025 NAV/index rows, rolling 10-year field, current YTD/price/distribution evidence and the scheduled-local pre-save checklist passed; IEV artifacts were written with the USD benchmark basis disclosed.
