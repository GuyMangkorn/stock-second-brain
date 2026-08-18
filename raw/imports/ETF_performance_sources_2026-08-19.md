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

## VGRDF — Vanguard FTSE Developed Europe ex UK UCITS ETF (EUR) Accumulating

### Identity and classification

- entity_key: LSE:VERE; input ticker: VGRDF; official Vanguard USD London Stock Exchange line: VERE; ISIN: IE00BK5BQY34; share-class inception: 23 Jul 2019; listing: 25 Jul 2019.
- management_mode: passive-index; physical equity ETF tracking FTSE Developed Europe ex U.K. Index; accumulating share class; base currency EUR; primary region Europe; OTC input symbol retained as alias.
- return_basis: official NAV Total Return in EUR, net of fund expenses, with income and capital gains reinvested; complete calendar rows are secondary dividend-adjusted proxies marked *.
- supported type: passive index-tracking equity ETF.

### Source map

| Source | URL/path | Use |
|---|---|---|
| Vanguard product page | https://www.vanguard.co.uk/professional/product/etf/equity/9682/ftse-developed-europe-ex-uk-ucits-etf | official identity, exchange/alias mapping, benchmark, passive/physical structure, holdings, tracking error and NAV |
| Vanguard factsheet | https://fund-docs.vanguard.com/FTSE_Developed_Europe_ex_UK_UCITS_ETF_EUR_Accumulating_9682_EU_INT_UK_EN.pdf | official rolling NAV TR, OCF, inception/ISIN/currency and risk disclosures as of 31 Jul 2026 |
| PortfoliosLab VERE.DE | https://portfolioslab.com/symbol/VERE.DE | secondary dividend-adjusted 2021-2025 annual proxy, later YTD and drawdown/recovery |
| justETF VERE | https://www.justetf.com/nl-be/etf-profile.html?isin=IE00BK5BQY34 | secondary volatility and identity/exchange cross-check |
| Cached S&P 500 Total Return convention | workflow cache and original URLs in the check-etf-performance skill | USD calendar rows 2021-2025, dividends reinvested, as of 31 Dec 2025; reused within cached 2016-2025 window |

### Raw observations

- Official Vanguard factsheet as of 31 Jul 2026: fund NAV TR YTD 11.54%, 1Y 22.04%, 3Y annualized 14.04%, 5Y annualized 9.52%, since inception annualized 10.59%; fund 10-year field is not available because the share class launched in 2019.
- Official product page: OCF 0.10%; physical, accumulating; USD London Stock Exchange line VERE; EUR base currency; official NAV EUR 60.4211 at closure 27 Jul 2026; 417 holdings and 3Y/5Y tracking error 0.18% as of 30 Jun 2026.
- Official factsheet exposes rolling performance rather than complete calendar NAV rows. PortfoliosLab secondary dividend-adjusted annual proxy rows are 2021 24.57%, 2022 -12.43%, 2023 17.62%, 2024 6.80%, 2025 21.22%; later secondary YTD is 13.71% as of 15 Aug 2026.
- PortfoliosLab secondary max drawdown is -34.74% on 18 Mar 2020 with recovery in 225 trading sessions. JustETF reports 3-year volatility 12.83% and 5-year volatility 14.49% as of 30 Jun 2026. These are not official daily NAV fields.
- JustETF annual rows differ slightly from PortfoliosLab (for example 2022 -12.73% versus -12.43%), so its annual table is used only as a cross-check and not as the primary annual proxy.
- Cached S&P 500 TR rows used for the common reference are USD: 2021 28.71%, 2022 -18.11%, 2023 26.29%, 2024 25.02%, 2025 17.88%; reference window is complete calendar years 2016-2025, as of 31 Dec 2025, dividends reinvested.

### Calculations and reconciliation

- Cumulative = product of (1 + annual return) - 1. PortfoliosLab proxy 2021-2025 compounds to 66.11%*; rounded-input CAGR is 10.68%*; population standard deviation is 13.40%*; up/down years are 4/1; best is 2025 +21.22%*; least positive is 2024 +6.80%*; worst and least-bad down year are 2022 -12.43%*.
- Cached S&P 500 TR compounds to 96.17% / 14.43% over 2021-2025. It remains a USD common reference rather than the issuer benchmark; no cross-currency excess-return or alpha claim is calculated.
- Official rolling fields remain separate: 5Y annualized NAV TR is 9.52% and since-inception annualized NAV TR is 10.59% as of 31 Jul 2026. Neither is relabeled as the 2021-2025 calendar CAGR.
- History is under 10 years, so a 10-year NAV CAGR is not applicable. Official daily NAV drawdown/recovery is not disclosed; secondary drawdown/recovery is labeled accordingly.

### Planned durable paths and contents

- Create wiki/analysis/performance/ETF_LSE_VERE Performance.md with canonical LSE:VERE identity, VGRDF alias, EUR NAV/secondary annual table, rolling-versus-calendar distinction, current YTD/NAV dates, risk evidence, source links, geography/Europe tag and breadcrumb.
- Update wiki/analysis/comparisons/Europe ETF.md with the VERE row and source-date note.
- Update wiki/analysis/comparisons/ETF Region Index.md Europe count from 22 to 23.
- Update wiki/analysis/performance/ETF Performance Index.md with the VERE coverage row, 2021-2025 Common Window row and 2026-08-19 coverage bullet.
- Append one log.md workflow bullet; no entity hub, normalized financial table or raw/funds file is planned because this workflow owns the numeric performance page.

### Local pre-save checklist

- PASS: canonical mapping, fund identity, ISIN, inception/listing, passive equity eligibility, issuer benchmark, OCF, accumulating structure, NAV TR definition, EUR currency and separate as-of dates are source-backed.
- PASS: secondary proxy rows are marked *; official rolling fields remain separate; annual source conflict is disclosed; no cross-currency comparison or alpha label is used.
- PASS: no 10-year CAGR is asserted because inception is 2019; official daily NAV drawdown/recovery gap is disclosed; source links, Europe region and breadcrumb resolve.
- PASS: complete proposed contents of the performance page, source batch section, Europe row/count, performance-index row/Common Window/bullet and log bullet are specified.
- PASS: no unresolved High/Medium finding blocks the write and no WARNING requiring confirmation remains.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official Vanguard identity, passive classification, rolling EUR NAV evidence and the marked secondary 2021-2025 proxy passed the scheduled-local pre-save checklist; VGRDF was resolved to LSE:VERE and currency/source gaps were disclosed.

## GSEU — Goldman Sachs ActiveBeta Europe Equity ETF

### Identity and classification

- entity_key: NYSE Arca:GSEU; input ticker: GSEU; CUSIP: 381430305; inception: 2 Mar 2016; listing exchange: NYSE Arca.
- management_mode: passive-index; the official prospectus says the Fund is not actively managed and generally does not dispose of securities unless they are removed from the tracked index.
- tracked index and management benchmark: Goldman Sachs ActiveBeta Europe Equity Index. The index uses value, momentum, quality and low-volatility attributes, combines four factor indices equally and rebalances quarterly.
- return_basis: official NAV Total Return in USD, net of fund expenses, with distributions reinvested; primary region Europe.
- supported type: passive index-tracking equity ETF; established track record over ten years from inception.

### Source map

| Source | URL/path | Use |
|---|---|---|
| Goldman Sachs GSEU fact card | https://am.gs.com/public-assets/documents/570151a1-24d6-11ef-870d-25a687970406 | official identity, annual NAV rows, rolling NAV/index fields, expenses, holdings, distributions, benchmark and risk disclosures as of 31 Jul 2026 |
| Goldman Sachs summary prospectus | https://am.gs.com/public-assets/documents/f69ce232-24e2-11ef-ad18-ad734f1320f3 | official objective, not-actively-managed classification, index methodology and fee framework |
| PortfoliosLab GSEU | https://portfolioslab.com/symbol/GSEU | secondary dividend-adjusted drawdown/recovery and return cross-check |
| Cached S&P 500 Total Return convention | workflow cache and original URLs in the check-etf-performance skill | USD calendar rows 2021-2025, dividends reinvested, as of 31 Dec 2025; reused within cached 2016-2025 window |

### Raw observations

- Official fact card as of 31 Jul 2026: NAV Total Return YTD 9.78%, 1Y 22.13%, 3Y annualized 15.88%, 5Y annualized 8.85%, 10Y annualized 9.70%, since inception annualized 9.97%.
- The same official performance table reports Goldman Sachs ActiveBeta Europe Equity Index YTD 9.80%, 1Y 22.30%, 3Y annualized 15.98%, 5Y annualized 8.84%, 10Y annualized 9.75%, since inception annualized 10.01%.
- Official calendar NAV rows in USD: 2021 16.78%, 2022 -18.12%, 2023 20.86%, 2024 1.63%, 2025 36.41%. The official calendar table also shows the MSCI Europe net total-return reference rows, but MSCI Europe is not the fund’s management benchmark.
- Official OCF/total expense ratio is 0.25%; fund facts as of 31 Jul 2026 show 346 holdings and net assets of 120.87 million USD. Distribution frequency is quarterly.
- The official text capture does not expose an exact latest NAV price; current price/NAV and official daily NAV drawdown/recovery are unresolved gaps.
- PortfoliosLab secondary dividend-adjusted data reports maximum drawdown -35.71% on 18 Mar 2020 with recovery in 172 trading sessions and a 2022 drawdown of -33.98%.
- Cached S&P 500 TR rows used for the common reference are USD: 2021 28.71%, 2022 -18.11%, 2023 26.29%, 2024 25.02%, 2025 17.88%; reference window is complete calendar years 2016-2025, as of 31 Dec 2025, dividends reinvested.

### Calculations and reconciliation

- Cumulative = product of (1 + annual return) - 1. Official GSEU NAV 2021-2025 compounds to 60.21%; rounded-input CAGR is 9.89%; population standard deviation is 18.50%; up/down years are 4/1; best is 2025 +36.41%; least positive is 2024 +1.63%; worst and least-bad down year are 2022 -18.12%.
- Cached S&P 500 TR compounds to 96.17% / 14.43% over 2021-2025. It is a USD common reference rather than the strategy benchmark; no direct cross-strategy excess-return or manager-skill claim is made.
- Official management-benchmark tracking observations remain separate: NAV versus ActiveBeta Index is -0.02 percentage points YTD, -0.17 points over 1Y, -0.10 points annualized over 3Y, +0.01 points annualized over 5Y, -0.05 points annualized over 10Y and -0.04 points since inception, based on the official rounded fields.
- The official issuer 10-year field is 9.70% annualized as of 31 Jul 2026; it is kept separate from the 2021-2025 calendar CAGR 9.89%.

### Planned durable paths and contents

- Create wiki/analysis/performance/ETF_NYSE_ARCA_GSEU Performance.md with canonical NYSE Arca:GSEU identity, official USD NAV annual table, strategy-benchmark fields, S&P common reference, risk evidence, source links, geography/Europe tag and breadcrumb.
- Update wiki/analysis/comparisons/Europe ETF.md with the GSEU row and current-date/risk note.
- Update wiki/analysis/comparisons/ETF Region Index.md Europe count from 23 to 24.
- Update wiki/analysis/performance/ETF Performance Index.md with the GSEU coverage row, 2021-2025 Common Window row and 2026-08-19 coverage bullet.
- Append one log.md workflow bullet; no entity hub, normalized financial table or raw/funds file is planned because this workflow owns the numeric performance page.

### Local pre-save checklist

- PASS: canonical ticker/exchange, fund identity, CUSIP, inception, passive eligibility, strategy benchmark, factor methodology, OCF, distribution treatment, NAV TR definition, USD currency and as-of date are source-backed.
- PASS: official annual NAV rows are separated from official rolling fields, the strategy benchmark is used for management evidence, S&P 500 is labeled only as a common reference, and no manager-skill label is assigned.
- PASS: 10-year issuer field is distinguished from 2021-2025 calendar CAGR; secondary drawdown/recovery is labeled; current price/NAV and official daily NAV gaps are disclosed.
- PASS: complete proposed contents of the performance page, source batch section, Europe row/count, performance-index row/Common Window/bullet and log bullet are specified.
- PASS: no unresolved High/Medium finding blocks the write and no WARNING requiring confirmation remains.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official Goldman Sachs identity, passive strategic-beta classification, USD NAV annual rows, strategy-benchmark rolling fields and the scheduled-local pre-save checklist passed; GSEU artifacts disclose S&P common-reference and price/NAV source gaps.

## ISACF — iShares MSCI ACWI UCITS ETF (USD) Accumulating

### Identity and classification

- entity_key: LSE:ISAC; input ticker: ISACF; official ticker: ISAC; exchange: London Stock Exchange USD line; ISIN: IE00B6R52259.
- Fund/share-class: iShares MSCI ACWI UCITS ETF (USD Accumulating); share-class launch 21 Oct 2011; accumulating USD share class; Ireland; UCITS.
- management_mode: passive-index-tracking; physical optimized replication; benchmark MSCI All Country World Index (Net).
- return_basis: official NAV Total Return in USD, net of expenses, with income/capital gains reinvested.
- supported type: passive index-tracking equity ETF; primary region International.
- input mapping: OTC ISACF is retained as alias and resolves to the official USD London line LSE:ISAC; LSE GBP line is SSAC and is not used.

### Source map

| Source | URL/path | Use |
|---|---|---|
| iShares product page | https://www.ishares.com/uk/individual/en/products/251850/ishares-msci-acwi-ucits-etf | official identity, listing table, ISIN, launch, current NAV/YTD, holdings, benchmark, beta, standard deviation and risk fields |
| iShares July 2026 factsheet | https://www.ishares.com/nl/particuliere-belegger/nl/literature/fact-sheet/ssac-ishares-msci-acwi-ucits-etf-fund-fact-sheet-en-nl.pdf?siteEntryPassthrough=true&switchLocale=y | official 2016-2025 annual NAV/benchmark rows, rolling NAV fields, TER, holdings and dated fund facts |
| iShares UK factsheet cross-check | https://www.ishares.com/uk/individual/en/literature/fact-sheet/ssac-ishares-msci-acwi-ucits-etf-fund-fact-sheet-en-gb.pdf?siteEntryPassthrough=true&switchLocale=y | official factsheet locale cross-check; same USD accumulating share-class identity and annual performance basis |
| Cached S&P 500 Total Return convention | workflow cache and original URLs in the check-etf-performance skill | USD calendar rows 2021-2025, dividends reinvested, as of 31 Dec 2025; reused inside cached 2016-2025 window |

### Raw observations

- Official listing table identifies the USD London Stock Exchange line as ISAC, listed 24 Oct 2011, with SEDOL B6R5225, Bloomberg ISAC LN and RIC ISACI.L. The OTC input ISACF is mapped by ISIN IE00B6R52259.
- Official product page current snapshot as of 17 Aug 2026: NAV USD 124.95, NAV Total Return YTD 15.06%, holdings 1,693, and the fund/share-class identity above.
- Official product-page risk/analytics fields as of 31 Jul 2026: 3-year beta 0.998 and 3-year standard deviation 12.61%.
- Official July factsheet says performance, portfolio and net-asset data are as of 31 Jul 2026 and other fund data are as of 06 Aug 2026. It reports TER 0.20%, 1,695 holdings, physical optimized replication, accumulating USD share class and MSCI ACWI Net benchmark.
- Official Share Class NAV Total Return annual rows in USD: 2016 7.82%, 2017 23.94%, 2018 -9.52%, 2019 26.37%, 2020 15.62%, 2021 18.71%, 2022 -18.19%, 2023 22.35%, 2024 17.35%, 2025 22.41%.
- Official MSCI ACWI Net benchmark annual rows in USD: 2016 7.86%, 2017 23.97%, 2018 -9.41%, 2019 26.60%, 2020 16.25%, 2021 18.54%, 2022 -18.36%, 2023 22.20%, 2024 17.49%, 2025 22.34%.
- Official July factsheet rolling fields: Share Class 1m 0.11%, 3m 4.46%, 6m 8.21%, YTD 11.42%, 1y 22.22%, 3y annualized 18.33%, 5y annualized 10.95%, since inception 11.17%; benchmark YTD 11.33%, 1y 22.11%, 3y 18.30%, 5y 10.85%, since inception 11.30%.
- Official product-page current YTD 15.06% is later than the July factsheet YTD 11.42%; this is an as-of date difference, not a contradictory performance claim. Current NAV/YTD and July rolling fields remain separately labeled.
- Official product-page risk disclosures cover global equity, country/sector concentration, emerging markets, currency, liquidity and counterparty risks. Official daily NAV maximum drawdown and recovery date were not disclosed in the reviewed sources.

### Calculations and reconciliation

- Cumulative = product of (1 + annual return) - 1. Official 2016-2025 Share Class rows compound to 201.535205%, displayed as 201.54%; rounded-input CAGR is 11.669302%, displayed as 11.67%†.
- Official 2021-2025 Share Class rows compound to 70.685907%, displayed as 70.69%; rounded-input CAGR is 11.285744%, displayed as 11.29%; population annual-return standard deviation is 15.486703%, displayed as 15.49%; positive/negative years are 4/1; best year is 2025 +22.41%; worst year is 2022 -18.19%.
- Official 2021-2025 benchmark rows compound to 69.984180%, displayed as 69.98%; rounded-input CAGR is 11.194089%, displayed as 11.19%.
- Fund-minus-benchmark annual differences for 2021-2025 are +0.17, +0.17, +0.15, -0.14 and +0.07 percentage points. These are tracking observations after fees/rounding and are not called alpha.
- Complete 2016-2025 rows support the calendar-derived 10-year display; no issuer rolling 10-year field is substituted for this calculation. The page marks the value with †.
- Cached S&P 500 Total Return rows are USD 2021 28.71%, 2022 -18.11%, 2023 26.29%, 2024 25.02%, 2025 17.88%; they compound to 96.17% / CAGR 14.43% and remain a common USD reference, not the fund's strategy benchmark.

### Planned durable paths and contents

- Create wiki/analysis/performance/ETF_LSE_ISAC Performance.md with the canonical LSE:ISAC identity, ISACF alias, official USD annual table, MSCI ACWI Net benchmark rows, rolling/current date separation, risk evidence, source links, International breadcrumb and geography tag.
- Update wiki/analysis/comparisons/International ETF.md with the ISAC row, current product-page versus July factsheet date note and calendar-CAGR footnote.
- Update wiki/analysis/comparisons/ETF Region Index.md International count from 24 to 25.
- Update wiki/analysis/performance/ETF Performance Index.md with the ISAC coverage row, 2021-2025 Common Window row and 2026-08-19 coverage bullet.
- Append one log.md workflow bullet; no entity hub, normalized financial table or raw/funds file is planned because this workflow owns the numeric performance page.

### Local pre-save checklist

- PASS: canonical ticker/exchange mapping, fund identity, ISIN, launch/listing dates, passive eligibility, benchmark, replication method, TER, accumulation, NAV TR definition, USD currency, annual rows, rolling fields, current NAV/YTD and all as-of dates are source-backed.
- PASS: official product-page current YTD/NAV is separated from July factsheet performance and holdings; official benchmark rows are separated from the cached S&P common reference; no arithmetic alpha or manager-skill claim is made.
- PASS: complete official 2016-2025 rows support the calendar calculation; the rounded-input CAGR is marked †; 2021-2025 common-window calculations reconcile to the displayed annual rows; tracking differences are labeled as observations.
- PASS: global, country/sector, emerging-market, FX, liquidity and counterparty risks are disclosed; official daily NAV drawdown/recovery gap is disclosed; no secondary performance rows are required.
- PASS: complete proposed contents of the performance page, source batch section, International row/count, performance-index row/Common Window/bullet and log bullet are specified; planned links and breadcrumb resolve.
- PASS: no unresolved High/Medium finding blocks the write and no WARNING requiring confirmation remains.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official iShares identity and ISACF-to-LSE:ISAC mapping, passive classification, USD 2016-2025 NAV/benchmark rows, rolling/current fields and the scheduled-local pre-save checklist passed; July-versus-current as-of dates, tracking observations and global risk gaps are disclosed.

## IMSEF — iShares Core MSCI Europe UCITS ETF (EUR Distributing)

### Identity and classification

- entity_key: LSE:ISEU; input ticker: IMSEF; official ticker: ISEU; exchange: London Stock Exchange USD line; ISIN: IE00B1YZSC51.
- Fund/share-class: iShares Core MSCI Europe UCITS ETF (EUR Distributing); share-class launch 06 Jul 2007; EUR share class; Ireland; UCITS.
- management_mode: passive-index-tracking; physical optimized replication; benchmark MSCI Europe Index.
- return_basis: official NAV Total Return in EUR, net of expenses, with gross income reinvested where applicable; distributing share class pays quarterly income.
- supported type: passive index-tracking equity ETF; primary region Europe.
- input mapping: OTC IMSEF is retained as alias and resolves by ISIN to the same EUR share class whose official USD London Stock Exchange line is ISEU. The LSE GBP line IMEU and Euronext EUR line IMEU are separate trading lines for the same share-class identity.

### Source map

| Source | URL/path | Use |
|---|---|---|
| iShares product page | https://www.ishares.com/uk/individual/en/products/251860/ishares-msci-%20europe-ucits-etf-inc-fund | official identity, share class, benchmark, current NAV/YTD, holdings, risk fields and listing table |
| iShares July 2026 factsheet | https://www.ishares.com/uk/individual/en/literature/fact-sheet/imeu-ishares-core-msci-europe-ucits-etf-fund-fact-sheet-en-gb.pdf?siteEntryPassthrough=true&switchLocale=y | official EUR 2016-2025 annual NAV/benchmark rows, rolling performance, TER, holdings and dated fund facts |
| DTCC OTC notice | https://www.dtcc.com/-/media/Files/pdf/2016/5/16/OTC-094.pdf | OTC symbol IMSEF and iShares II plc MSCI Europe EUR UCITS ETF identity cross-check |
| Cached S&P 500 Total Return convention | workflow cache and original URLs in the check-etf-performance skill | separate USD common reference; not used for arithmetic comparison with EUR NAV returns |

### Raw observations

- Official iShares product page identifies the share class as iShares Core MSCI Europe UCITS ETF (EUR Distributing), ISIN IE00B1YZSC51, share-class launch 06 Jul 2007, share-class currency EUR, benchmark MSCI Europe Index, physical optimized methodology, TER 0.12%, quarterly distributions and 396 holdings as of 14 Aug 2026.
- Official listing table identifies London Stock Exchange ticker ISEU, currency USD, listing date 28 Nov 2016, SEDOL BD8BRX7, Bloomberg ISEU LN and RIC ISEU.L. The same table shows IMEU GBP and IMEU EUR listings for the share class.
- Official product page current snapshot: NAV EUR 41.11 as of 17 Aug 2026; NAV Total Return YTD 13.81% as of 14 Aug 2026; net assets of share class EUR 10.839B as of 17 Aug; shares outstanding 263.621M as of 17 Aug.
- Official product-page analytics as of 31 Jul 2026: 3-year standard deviation 10.59% and 3-year beta 1.002. The July factsheet also reports 3-year beta 1.00 and 396 holdings.
- Official July factsheet says performance, portfolio and net-asset information are as of 31 Jul 2026 and other data as of 07 Aug 2026. It reports TER 0.12%, physical optimized replication, EUR distributing share class and MSCI Europe Index benchmark.
- Official Share Class EUR NAV Total Return annual rows: 2016 2.65%, 2017 10.29%, 2018 -10.42%, 2019 26.42%, 2020 -3.14%, 2021 25.44%, 2022 -9.23%, 2023 16.13%, 2024 8.87%, 2025 19.67%.
- Official MSCI Europe EUR benchmark annual rows: 2016 2.58%, 2017 10.24%, 2018 -10.57%, 2019 26.05%, 2020 -3.32%, 2021 25.13%, 2022 -9.49%, 2023 15.83%, 2024 8.59%, 2025 19.39%.
- Official July factsheet rolling fields: Share Class 1m 0.97%, 3m 7.43%, 6m 8.67%, YTD 12.05%, 1y 22.36%, 3y annualized 14.28%, 5y annualized 10.40%, since inception 5.41%; benchmark YTD 11.82%, 1y 22.09%, 3y 14.00%, 5y 10.11%, since inception 5.29%.
- Official product-page risk text covers equity-market movements and counterparty risk; country, sector and currency exposure are inherent in the MSCI Europe equity portfolio. Official daily NAV maximum drawdown and recovery date were not disclosed in the reviewed sources.

### Calculations and reconciliation

- Cumulative = product of (1 + annual return) - 1. Official 2016-2025 Share Class rows compound to 113.935433%, displayed as 113.94%; rounded-input CAGR is 7.901696%, displayed as 7.90%†; population annual-return standard deviation is 12.791270%.
- Official 2021-2025 Share Class rows compound to 72.272645%, displayed as 72.27%; rounded-input CAGR is 11.491887%, displayed as 11.49%; population annual-return standard deviation is 11.973924%, displayed as 11.97%; positive/negative years are 4/1; best year is 2025 +19.67%; worst year is 2022 -9.23%.
- Official 2016-2025 benchmark rows compound to 109.604920%, displayed as 109.60%; rounded-input CAGR is 7.681265%, displayed as 7.68%.
- Official 2021-2025 benchmark rows compound to 70.073579%, displayed as 70.07%; rounded-input CAGR is 11.205782%, displayed as 11.21%.
- Fund-minus-benchmark annual differences for 2021-2025 are +0.31, +0.26, +0.30, +0.28 and +0.28 percentage points. These are passive tracking observations after fees/rounding and are not called alpha.
- Complete 2016-2025 rows support the calendar-derived 10-year display; no issuer rolling 10-year field is substituted for this calculation. The page marks the fund value with †.
- Cached S&P 500 Total Return rows remain a separate USD reference and are not compared with the EUR NAV rows because of currency and market-exposure mismatch.

### Planned durable paths and contents

- Create wiki/analysis/performance/ETF_LSE_ISEU Performance.md with the canonical LSE:ISEU identity, IMSEF alias, EUR NAV/benchmark annual table, USD listing-currency note, rolling/current date separation, risk evidence, source links, Europe breadcrumb and geography tag.
- Update wiki/analysis/comparisons/Europe ETF.md with the ISEU row, EUR-return/USD-listing note and calendar-CAGR footnote.
- Update wiki/analysis/comparisons/ETF Region Index.md Europe count from 24 to 25.
- Update wiki/analysis/performance/ETF Performance Index.md with the ISEU coverage row, 2021-2025 Common Window row and 2026-08-19 coverage bullet.
- Append one log.md workflow bullet; no entity hub, normalized financial table or raw/funds file is planned because this workflow owns the numeric performance page.

### Local pre-save checklist

- PASS: canonical ticker/exchange mapping, fund/share-class identity, ISIN, launch/listing dates, passive eligibility, benchmark, replication method, TER, distribution, EUR NAV TR definition, USD listing currency and all as-of dates are source-backed.
- PASS: official EUR annual rows and benchmark rows are separated from current product-page YTD/NAV; the USD LSE line is not treated as a USD return series; cached S&P is kept separate; no arithmetic alpha or manager-skill claim is made.
- PASS: complete official 2016-2025 rows support the calendar calculation; the rounded-input CAGR is marked †; 2021-2025 common-window calculations reconcile to displayed annual rows; tracking differences are labeled as observations.
- PASS: equity-market, country/sector, FX and counterparty risks are disclosed; official daily NAV drawdown/recovery gap is disclosed; no secondary performance rows are required.
- PASS: complete proposed contents of the performance page, source batch section, Europe row/count, performance-index row/Common Window/bullet and log bullet are specified; planned links and breadcrumb resolve.
- PASS: no unresolved High/Medium finding blocks the write and no WARNING requiring confirmation remains.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official iShares identity and IMSEF-to-LSE:ISEU mapping, passive classification, EUR 2016-2025 NAV/benchmark rows, rolling/current fields and the scheduled-local pre-save checklist passed; EUR-return/USD-listing basis, date gaps and daily NAV drawdown/recovery gap are disclosed.

## DXMEF — Xtrackers MSCI Europe UCITS ETF 1C / XMED

### Identity and classification

- `entity_key: LSE:XMED`; input ticker `DXMEF`; official ticker `XMED`; exchange `London Stock Exchange USD line`; ISIN `LU0274209237`; fund/share-class launch `2007-01-10`; domicile Luxembourg.
- DWS identifies the fund as Xtrackers MSCI Europe UCITS ETF 1C, with share-class and fund currency USD. The official listing table maps the USD London line to `XMED LN` / `XMED.L`; the GBX London line is `XMEU LN` and is not used for this input.
- DTCC's OTC notice cross-checks `DXMEF` to the legacy DB X-trackers/DB X-Trackers Europe fund name. The DWS ISIN and official listing table are the canonical identity evidence.
- `management_mode: passive-index-tracking`; direct physical replication; accumulating income treatment; all-in fee `0.12% p.a.`.
- Issuer benchmark: `MSCI Total Return Net Europe Index`, provider MSCI, USD base currency, 397 constituents, large-/mid-cap developed Europe and approximately 85% free-float coverage. Primary region: `Europe`; region page `[[Europe ETF]]`; canonical tag `geography/Europe`.
- Return basis: secondary USD total-return growth series with reinvestment where provider-defined, marked `*`; official DWS factsheet did not expose its annual numeric performance table in the reviewed capture.

### Source map

| Source | URL/path | Use |
|---|---|---|
| DWS Xtrackers factsheet | https://etf.dws.com/download/asset/b67380f1-ceae-4018-9edf-9ddf65624841 | official July 2026 identity, USD share class, LSE XMED mapping, fee, NAV, assets, replication, benchmark, constituents and risk disclosures |
| DTCC OTC notice | https://www.dtcc.com/-/media/Files/pdf/2016/5/16/OTC-094.pdf | DXMEF OTC symbol/name cross-check |
| Morningstar XMED report | https://lt.morningstar.com/1c6qh1t6k9/etfreport/default.aspx?1=1&ClientFund=0&CurrencyId=USD&Id=0P0000M2W8&SecurityToken=0P0000M2W8%5D22%5D0%5DETEXG%24XLON&tab=0 | secondary USD growth rows for 2021-2025, rolling 10-year field, current YTD and dated NAV snapshot |
| ETFdoc analysis | https://www.etfdoc.it/en/d/Ana/DBX1ME/LU0274209237_xtrackers-msci-europe-ucits-etf-1c | secondary Euro-labelled annual/current rows for conflict review only |
| Stuttgarter fund page | https://fonds.stuttgarter.de/product/LU0274209237/ | secondary conflicting annual/current and risk cross-check; not used in USD calculation |
| Cached S&P 500 Total Return convention | check-etf-performance skill cache and original URLs | USD calendar rows 2021-2025, dividends reinvested, as of 2025-12-31; reused without a new search |

### Raw observations

- DWS factsheet as of 2026-07-31: ISIN `LU0274209237`; share-class currency USD; fund currency USD; launch 2007-01-10; domicile Luxembourg; direct physical replication; all-in fee `0.12%`; capitalizing income; NAV per share `US$140.30`; total fund assets `US$9.93B`; 64.38M shares outstanding; annual securities-lending return `0.0184%`.
- DWS official listing table: Borsa Italiana `XMEU IM` EUR, London USD line `XMED LN` / `XMED.L`, London GBX line `XMEU LN` / `XMEU.L`, SIX `XMEU SW` CHF and XETRA `XMEU GY` EUR. The requested OTC alias is therefore displayed as canonical `LSE:XMED`.
- DWS index key facts: `MSCI Total Return Net Europe Index`, Bloomberg `NDDUE15`, USD base currency, 397 constituents; large-/mid-cap developed European companies, approximately 85% free-float coverage and quarterly review.
- Morningstar USD Growth of 10,000 observations as of 2026-06-30: fund `2021 16.58%`, `2022 -14.85%`, `2023 20.18%`, `2024 2.02%`, `2025 35.77%`; Morningstar benchmark cross-check `16.56%`, `-15.23%`, `19.95%`, `2.16%`, `35.86%` is not used as the issuer benchmark series.
- Morningstar trailing fields as of 2026-07-21: YTD `7.85%`, 3-year annualized `15.41%`, 5-year annualized `9.82%`, 10-year annualized `9.86%`; NAV/closing price `US$135.61` on the same date. These are secondary observations.
- S&P 500 cached USD TR rows for the same complete calendar years: 2021 `28.71%`, 2022 `-18.11%`, 2023 `26.29%`, 2024 `25.02%`, 2025 `17.88%`; reference as-of 2025-12-31, dividends reinvested.

### Calculations and reconciliation

- `Cumulative = ∏(1 + annual return) - 1`: secondary XMED rows compound to `65.245652%`, displayed as `65.25%*`; rounded-input 2021-2025 CAGR is `10.567123%`, displayed as `10.57%*`.
- Population standard deviation of the five secondary annual returns is `17.166284%`, displayed as `17.17%*`; positive/negative years are `4/1`; best year is 2025 `+35.77%*`; worst year is 2022 `-14.85%*`; least positive year is 2024 `+2.02%*`.
- Cached S&P 500 TR compounds to `96.17%` / rounded-input CAGR `14.43%` over 2021-2025. It is a common USD reference only and not the XMED management benchmark.
- Official DWS benchmark annual rows and official issuer rolling/YTD performance values were not disclosed in the reviewed factsheet. Morningstar's `9.86%*` rolling field and `7.85%*` YTD are retained separately from the official DWS NAV snapshot `US$140.30` as of 2026-07-31.

### Source conflict and quality choice

- ETFdoc and Quantalys expose a Euro-labelled performance series with annual fund rows `2021 26.31%`, `2022 -8.33%`, `2023 14.41%`, `2024 8.51%`, `2025 20.05%`; these are not used because the DWS share class, fund currency, index base currency and canonical XMED line are USD.
- Stuttgarter reports a different annual sequence `2021 15.40%`, `2022 -14.70%`, `2023 20.18%`, `2024 1.72%`, `2025 36.44%`; the reviewed page does not provide a return-definition/as-of basis that reconciles it to DWS. It is kept as a conflict cross-check, not merged.
- Morningstar is the selected secondary source for the annual/current proxy because it explicitly identifies XMED, uses a USD report, provides dated USD trailing fields and a USD growth series. No cross-source spread or active-skill conclusion is calculated.

### Planned durable paths and contents

- Create `wiki/analysis/performance/ETF_LSE_XMED Performance.md` with canonical `LSE:XMED`, input alias `DXMEF`, official DWS identity/benchmark/fee/NAV/risk fields, secondary USD 2021-2025 annual table marked `*`, cached S&P reference, 65.25% / 10.57% secondary calculations, current YTD/rolling dates, source conflicts, Europe breadcrumb and `geography/Europe` tag.
- Update `wiki/analysis/comparisons/Europe ETF.md` with the XMED row, `9.86%*` secondary rolling field, `10.57%*` secondary 2021-2025 CAGR, `7.85%*` secondary YTD, and the DWS-versus-secondary source-gap note.
- Update `wiki/analysis/comparisons/ETF Region Index.md` Europe count from `25` to `26`; no new region page is needed.
- Update `wiki/analysis/performance/ETF Performance Index.md` with the XMED coverage row, a marked `*` 2021-2025 common-window row (not strict official ranking evidence), an explanatory source-gap note, and a `2026-08-19 Coverage Addition` bullet.
- Append this exact workflow bullet to `log.md`: `- etf-performance: Created [[ETF_LSE_XMED Performance]] for input alias DXMEF, updated [[Europe ETF]], [[ETF Region Index]], [[ETF Performance Index]], and [[ETF_performance_sources_2026-08-19]]. Scheduled-inline local pre-save returned PASS; DXMEF resolved to official USD London line LSE:XMED, with secondary USD 2021-2025 proxy cumulative 65.25%* / rounded-input CAGR 10.57%*, secondary rolling 10-year 9.86%* and YTD 7.85%* as of 2026-07-21, while DWS official identity/NAV/benchmark fields and conflicting currency sources are disclosed.`
- No entity hub, normalized financial table or `raw/funds/` file is planned because this workflow owns the numeric performance page.

### Local pre-save checklist

- PASS: canonical OTC-to-issuer mapping, official LSE USD line, ISIN, launch date, passive eligibility, physical replication, accumulation treatment, DWS benchmark, fee, USD currency, official NAV/assets, and all as-of dates are source-backed.
- PASS: official DWS identity/NAV/fund facts are separated from secondary Morningstar annual/current fields; the DWS benchmark has no invented annual rows; the S&P 500 cache is labeled as a common USD reference; no arithmetic alpha or manager-skill claim is made.
- PASS: secondary annual rows are marked `*`; the 65.25% cumulative result, 10.57% rounded-input CAGR, 17.17% population standard deviation, 4/1 up/down count and best/worst years reconcile to the displayed inputs.
- PASS: ETFdoc/Quantalys Euro-labelled rows and Stuttgarter conflicting rows are recorded as source conflicts and are not mixed into the USD calculation; official DWS NAV and secondary Morningstar NAV have separate dates.
- PASS: Europe primary-region assignment, canonical breadcrumb, `geography/Europe` tag, performance page, region row/count, performance-index row/common-window note, source batch section and exact log bullet are specified; every planned wikilink resolves.
- PASS: no unresolved High/Medium finding blocks the write and no WARNING requiring confirmation remains. The issuer annual/current performance gap is explicitly owned by the performance page and source batch.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official DWS identity, DXMEF-to-LSE:XMED mapping, passive USD share-class classification, secondary USD annual/current evidence, source reconciliation and the scheduled-local pre-save checklist passed; issuer performance gaps and conflicting Euro-labelled sources are explicitly disclosed.

## DBEU — Xtrackers MSCI Europe Hedged Equity ETF

### Identity and classification

- `entity_key: NYSE Arca:DBEU`; input ticker `DBEU`; official fund `Xtrackers MSCI Europe Hedged Equity ETF`; SEC filing identifies the listing as NYSE Arca; inception `2013-09-30`; CUSIP `233051853`.
- `management_mode: passive-index`; SEC summary prospectus describes a passive/indexing approach using full replication, with representative sampling permitted when direct acquisition is not practicable.
- Issuer benchmark: `MSCI Europe US Dollar Hedged Index`; the index hedges the developed-Europe equity exposure to USD with one-month currency forwards. Primary region: `Europe`; region page `[[Europe ETF]]`; canonical tag `geography/Europe`.
- `return_basis: NAV total return` in USD; the DWS factsheet reports ETF-at-NAV performance net of fund expenses and keeps market-price returns separate. The annual and YTD rows used below are secondary rounded NAV-return observations marked `*`.

### Source map

| Source | URL/path | Use |
|---|---|---|
| DWS DBEU Q2 2026 factsheet | https://etf.dws.com/download/asset/b2d0199b-0bfc-4ed0-866b-24f31967f463 | official fund identity, NYSE ticker, inception, hedged MSCI benchmark, rolling NAV/benchmark returns, fee, holdings, country/sector weights and beta; as of `2026-06-30` |
| SEC DBEU summary prospectus | https://www.sec.gov/Archives/edgar/data/1503123/000008805325000878/k100125dbeu.htm | official exchange identity, passive/indexing/full-replication method, expense ratio and risk disclosures; October 2025 |
| AAII DBEU performance page | https://www.aaii.com/etf/ticker/DBEU | secondary rounded annual NAV-total-return and YTD rows; as of `2026-06-30` |
| DWS 2026 NYSE dividend schedule | https://etf.dws.com/en-us/AssetDownload/Index/6b4403da-1256-4e11-8e8a-14254534db91/Dividend-Schedule.pdf/ | issuer distribution-schedule context; DBEU is listed under semi-annual distributions, but no amount is used in this performance run |
| S&P 500 index page and cached convention | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ and the cached URLs in `check-etf-performance/SKILL.md` | common USD S&P 500 Total Return reference for complete calendar years `2016-2025`; dividends reinvested, as of `2025-12-31` |

### Raw observations

- DWS official factsheet as of `2026-06-30`: NAV returns are `11.97%` for 3 months, `24.03%` for 1 year, `16.02%` annualized for 3 years, `12.03%` annualized for 5 years, `11.58%` annualized for 10 years and `9.90%` since inception. The same table reports the MSCI Europe US Dollar Hedged Index at `11.87%`, `24.16%`, `16.25%`, `12.18%`, `11.82%` and `10.15%`, respectively.
- DWS identifies the ETF as NYSE ticker `DBEU`, inception `2013-09-30`, 410 holdings, net assets `$758,183,774.79`, gross/net expense ratio `0.45%`, and beta `0.73`, all as of `2026-06-30`.
- DWS country weights as of `2026-06-30`: UK `20.08%`, Switzerland `14.86%`, France `14.29%`, Germany `13.10%`, Netherlands `10.57%`, Spain `5.97%`, Italy `4.88%`, Sweden `4.57%`, Denmark `2.54%`, plus cash `1.94%`. Sector weights include Financials `23.71%`, Industrials `17.59%`, Health Care `12.46%`, Information Technology `9.84%` and Consumer Staples `8.29%`.
- The AAII page labels the secondary annual NAV rows as: 2016 `8.1%`, 2017 `14.6%`, 2018 `-8.5%`, 2019 `26.8%`, 2020 `-0.5%`, 2021 `23.3%`, 2022 `-6.2%`, 2023 `17.0%`, 2024 `9.5%`, 2025 `22.5%`; its YTD row is `11.5%`, all as of `2026-06-30`. These values are rounded to one decimal in the source and are marked `*` rather than relabeled as official DWS calendar rows.
- The DWS factsheet provides no issuer-published 2016-2025 annual table or current YTD field in the reviewed capture. Daily NAV observations sufficient to reproduce maximum drawdown and recovery were also not disclosed.
- Cached S&P 500 TR rows for `2016-2025` are USD: `11.96%`, `21.83%`, `-4.38%`, `31.49%`, `18.40%`, `28.71%`, `-18.11%`, `26.29%`, `25.02%`, `17.88%`; dividends reinvested, reference as of `2025-12-31`.

### Calculations and reconciliation

- `Cumulative = ∏(1 + annual return) - 1`: secondary DBEU 2016-2025 rows compound to `159.582688%`, displayed as `159.58%*`; rounded-input CAGR is `10.008837%`, displayed as `10.01%*`; population annual-return standard deviation is `11.832092%`, displayed as `11.83%*`; up/down is `7/3`; best is 2019 `+26.80%*`; worst is 2018 `-8.50%*`; least-bad down year is 2020 `-0.50%*`.
- Secondary DBEU 2021-2025 rows compound to `81.510597%`, displayed as `81.51%*`; rounded-input CAGR is `12.662763%`, displayed as `12.66%*`; population annual-return standard deviation for this five-year subset is `10.890253%`.
- Cached S&P 500 TR compounds to `298.329111%` / rounded-input CAGR `14.821761%` over `2016-2025`, displayed as `298.33%` / `14.82%`; over `2021-2025` it compounds to `96.17%` / `14.43%`. It is a common USD reference, not DBEU's issuer benchmark, and no currency-mismatched excess-return claim is made.
- The official DWS rolling 10-year NAV TR field `11.58%` as of `2026-06-30` is kept separate from the secondary complete-calendar proxy CAGR `10.01%*`; the windows and evidence ownership differ.

### Source conflict and quality choice

- The DWS factsheet is the source of truth for identity, classification, issuer benchmark, rolling NAV performance, fee, holdings and risk fields. It does not expose the annual/YTD rows needed for the durable annual table.
- AAII is selected as the secondary source because it explicitly labels the observations as annual NAV total returns and provides a dated YTD NAV row. The values remain rounded and marked `*`; price-return and dividend-adjusted proxy pages were not substituted into the NAV table.
- No arithmetic annual difference versus S&P 500 is described as alpha. Currency-hedged DBEU NAV returns and the USD S&P reference are shown together only as a clearly labelled common reference comparison.

### Planned durable paths and contents

- Create `wiki/analysis/performance/ETF_NYSE_ARCA_DBEU Performance.md` with canonical `NYSE Arca:DBEU`, official rolling 10-year NAV TR `11.58%`, secondary rounded 2016-2025 NAV-return rows marked `*`, secondary YTD `11.50%*`, cached S&P USD rows, 159.58%* / 10.01%* and 81.51%* / 12.66%* calculations, risk/hedging caveats, Europe breadcrumb and `geography/Europe` tag.
- Update `wiki/analysis/comparisons/Europe ETF.md` with the DBEU row and the official-versus-secondary annual/YTD gap note.
- Update `wiki/analysis/comparisons/ETF Region Index.md` Europe count from `26` to `27`; no new region page is needed.
- Update `wiki/analysis/performance/ETF Performance Index.md` with the DBEU coverage row, a marked `*` 2021-2025 Common Window row, and a `2026-08-19 Coverage Addition` bullet.
- Append one `log.md` workflow bullet; no entity hub, normalized financial table or `raw/funds/` file is planned because this workflow owns the numeric performance page.

### Local pre-save checklist

- PASS: canonical `NYSE Arca:DBEU` identity, fund name, inception, passive eligibility, full-replication method, MSCI USD-hedged benchmark, 0.45% fee, USD return basis and all as-of dates are source-backed.
- PASS: official DWS rolling NAV/benchmark fields are kept separate from secondary annual/YTD NAV-return rows; market-price return and distributions are not mixed into the annual table; secondary rows are visibly marked `*`.
- PASS: 2016-2025 and 2021-2025 calculations, up/down counts, best/worst subset, S&P cached values and displayed percentages recompute from the stated inputs; the issuer rolling 10-year field is not relabeled as the calendar CAGR.
- PASS: official beta, holdings, country/sector exposure and USD hedge risks are disclosed; daily NAV drawdown/recovery and issuer calendar/YTD gaps are explicitly recorded as unresolved.
- PASS: complete proposed performance page, source batch section, Europe row/count, performance-index row/Common Window/bullet and log bullet are specified; canonical breadcrumb, `geography/Europe` tag and planned wikilinks resolve.
- PASS: no unresolved High/Medium finding blocks the write and no WARNING requiring confirmation remains.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official DWS identity, passive USD-hedged classification, rolling NAV evidence, secondary annual/YTD observations, reconciled calculations and the scheduled-local pre-save checklist passed; issuer calendar/YTD and daily NAV gaps remain disclosed.
