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

## IRESF — iShares Core FTSE 100 UCITS ETF USD Hedged (Accumulating) / ISFD canonical line

### Identity and classification

- `workflow: check-etf-performance`; `entity_key: LSE:ISFD`; input ticker `IRESF`; canonical exchange `London Stock Exchange`; official fund `iShares Core FTSE 100 UCITS ETF USD Hedged (Accumulating)`; ISIN `IE00BYZ28W67`.
- The official iShares listing table maps the share class to `LSE:ISFD` in USD, listed 2017-10-23. MarketScreener independently identifies the OTC input `IRESF` with the same ISIN and USD-hedged accumulating name; IRESF is retained only as an input alias and is not the durable exchange key.
- `management_mode: passive-index`; iShares describes a physical, replicated UCITS equity ETF seeking to track the FTSE 100 Index. The share class accumulates income and uses derivatives for its USD currency hedge.
- Primary region: `United Kingdom`; region page `[[United Kingdom ETF]]`; canonical tag `geography/United-Kingdom`; breadcrumb `[[ETF Region Index]] → [[United Kingdom ETF]] → [[ETF Performance Index]]`.
- `return_basis: NAV total return` with gross income reinvested where applicable and expenses reflected in NAV; share-class return currency USD. The issuer benchmark rows are displayed in GBP, so benchmark arithmetic is kept separate from same-currency NAV analysis.

### Source map

| Source | URL/path | Use |
|---|---|---|
| iShares professional product page | https://www.ishares.com/uk/professionals/en/products/291401/?siteEntryPassthrough=true&switchLocale=y | official identity, canonical LSE listing, ISIN, objective, structure, fee, current USD NAV/YTD, assets, holdings, beta, standard deviation, valuation fields and sector exposures; current snapshot through `2026-08-13` / `2026-08-12` |
| iShares July 2026 factsheet | https://www.ishares.com/gls-download/literature/fact-sheet/isfd-ishares-core-ftse-100-ucits-etf-fund-fact-sheet-en-gb.pdf | official calendar NAV/benchmark rows, NAV return definition, share-class launch, TER, rolling performance, holdings and fund facts as of `2026-07-31` |
| MarketScreener IRESF page | https://www.marketscreener.com/quote/etf/ISHARES-CORE-FTSE-100-UCI-66468693/ | secondary OTC alias, USD currency and ISIN cross-check only; not primary NAV performance evidence |
| S&P 500 index page and cached convention | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ plus cached URLs in the skill | common USD S&P 500 Total Return rows for 2018-2025 and 2021-2025; dividends reinvested, reference as of `2025-12-31` |

### Raw observations

- The official product page identifies `ISFD`, USD Hedged (Accumulating), ISIN `IE00BYZ28W67`, LSE USD listing, inception `2017-10-19`, TER `0.20%`, physical/replicated structure, quarterly rebalance, 100 holdings, share-class net assets `USD 225,393,623`, fund net assets `GBP 16,670,824,973`, NAV `USD 10.45`, and NAV TR YTD `11.08%` as of `2026-08-12`.
- The same product-page capture reports 3-year beta `0.989` and standard deviation `9.46%` as of `2026-07-31`, P/B `2.40x` and P/E `18.04x` as of `2026-08-12`, and sector exposures as of `2026-08-12`: Financials `28.48%`, Industrials `14.14%`, Consumer Staples `13.27%`, Health Care `11.36%`, Energy `10.49%`, Materials `8.15%`, Consumer Discretionary `4.47%`, Utilities `4.41%`, Communication `1.95%`, Real Estate `1.19%`.
- The July 2026 factsheet reports calendar NAV TR rows for the share class: 2016 `-`, 2017 `-`, 2018 `-7.49%`, 2019 `19.10%`, 2020 `-11.28%`, 2021 `18.42%`, 2022 `5.69%`, 2023 `8.49%`, 2024 `9.66%`, 2025 `25.79%`. The corresponding FTSE 100 benchmark rows are 2016 `-`, 2017 `-`, 2018 `-14.11%`, 2019 `17.28%`, 2020 `-11.58%`, 2021 `18.40%`, 2022 `4.67%`, 2023 `7.90%`, 2024 `9.63%`, 2025 `25.78%`; the factsheet labels the share class performance as USD and benchmark performance as GBP.
- The same factsheet reports 1-month `3.63%`, 3-month `5.30%`, 6-month `8.00%`, YTD `11.18%`, 1-year `22.44%`, 3-year annualised `16.17%`, 5-year annualised `13.43%`, and since-inception annualised `8.80%`, all as of `2026-07-31`.
- The S&P 500 cached USD Total Return convention supplies 2018 `-4.38%`, 2019 `31.49%`, 2020 `18.40%`, 2021 `28.71%`, 2022 `-18.11%`, 2023 `26.29%`, 2024 `25.02%`, 2025 `17.88%`; the five-year subset is 2021 `28.71%`, 2022 `-18.11%`, 2023 `26.29%`, 2024 `25.02%`, 2025 `17.88%`.
- Official daily NAV observations sufficient to reproduce maximum drawdown and recovery date were not disclosed in the reviewed sources. The OTC quote is not used as a substitute for official NAV return.

### Calculations and reconciliation

- `Cumulative = ∏(1 + annual return) - 1`. Official ISFD rows compound to `83.090157%`, displayed as `83.09%`, and rounded-input CAGR is `7.853222%`, displayed as `7.85%`, for the eight complete calendar years 2018-2025. Population annual-return standard deviation is `12.071986%`, displayed as `12.07%`; up/down is `6/2`; best is 2025 `+25.79%`; worst is 2020 `-11.28%`; least-bad down year is 2018 `-7.49%`.
- Official ISFD rows for 2021-2025 compound to `87.302262%`, displayed as `87.30%`; rounded-input CAGR is `13.372730%`, displayed as `13.37%`; population annual-return standard deviation is `7.430098%`, displayed as `7.43%`; up/down is `5/0`; best is 2025 `+25.79%`; lowest positive year is 2022 `+5.69%`.
- FTSE 100 benchmark rows compound to `64.230360%` / rounded-input CAGR `6.397563%` for 2018-2025 and `84.389580%` / `13.017910%` for 2021-2025; benchmark standard deviation is `13.19%` for 2018-2025 and `7.73%` for 2021-2025. Because benchmark rows are GBP and share-class rows are USD hedged, the differences are not presented as alpha.
- Cached S&P 500 TR compounds to `192.028282%` / rounded-input CAGR `14.334715%` for 2018-2025 and `96.169618%` / `14.426430%` for 2021-2025. It remains a common USD reference, not the issuer benchmark or manager-skill evidence.

### Source conflict and quality choice

- The iShares product page and factsheet are the sources of truth for official share-class identity, canonical listing, passive structure, benchmark, fee, return definition, annual rows, rolling fields, current NAV/YTD and risk/fund facts. The product page's current YTD and July factsheet YTD are retained as separate dates, not treated as a conflict.
- MarketScreener is used only to cross-check the OTC alias-to-ISIN mapping; no OTC market-price or secondary performance series enters the NAV calculations.
- The official benchmark is FTSE 100 Index in GBP while the share-class NAV is USD hedged. Arithmetic fund-minus-benchmark observations are retained as tracking context only and are not called alpha.

### Planned durable paths and contents

- Create `wiki/analysis/performance/ETF_LSE_ISFD Performance.md` with canonical `LSE:ISFD`, input alias `IRESF`, USD hedged accumulating identity, official 2018-2025 annual NAV/benchmark/S&P rows, 83.09% / 7.85% available-window calculations, 87.30% / 13.37% common-window calculations, current/July YTD separation, risk fields, United Kingdom breadcrumb and `geography/United-Kingdom` tag.
- Update `wiki/analysis/comparisons/United Kingdom ETF.md` with the ISFD/IRESF row, `not applicable (<10y)` 10Y field, 13.37% common CAGR, 11.08% YTD, and USD-share-class/GBP-benchmark caveat.
- Update `wiki/analysis/comparisons/ETF Region Index.md` United Kingdom count from `4` to `5`; no new region file is needed.
- Update `wiki/analysis/performance/ETF Performance Index.md` with the ISFD/IRESF coverage row, the 2021-2025 Common Window row, and a `2026-08-19 Coverage Addition` bullet; do not add the under-10-year record to the strict 2016-2025 ranking.
- Append one `etf-performance` workflow bullet to `log.md`; no entity hub, normalized financial table, or `raw/funds/` file is planned.

### Local pre-save checklist

- PASS: canonical OTC-to-issuer mapping, official LSE USD line, ISIN, launch date, passive eligibility, physical replication, accumulation treatment, FTSE 100 benchmark, 0.20% fee, USD share-class return basis and all current/as-of dates are source-backed.
- PASS: official annual NAV/benchmark rows, rolling fields, current NAV/YTD, holdings, assets, beta, standard deviation and sector exposure are preserved with separate USD/GBP currency labels; S&P rows are labeled as a cached common USD reference.
- PASS: 2018-2025 and 2021-2025 calculations, up/down counts, best/worst years, standard deviations and S&P compounding recompute from the stated inputs; the eight-year CAGR is not relabeled as a 10-year issuer field.
- PASS: under-10-year history, USD hedge/GBP benchmark basis, OTC alias evidence and daily NAV drawdown/recovery gap are explicitly disclosed; no unsupported market-price return or alpha claim is introduced.
- PASS: complete proposed performance page, source batch section, United Kingdom row, region-index count, performance-index coverage/Common Window/bullet and log bullet are specified; canonical breadcrumb, `geography/United-Kingdom` tag and planned wikilinks resolve.
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
reason: Official iShares identity, IRESF-to-LSE:ISFD mapping, passive USD-hedged classification, official annual/current evidence, reconciled calculations and the scheduled-local pre-save checklist passed; under-10-year history, USD-share-class/GBP-benchmark basis and daily NAV gaps remain disclosed.

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

## EWK — iShares MSCI Belgium ETF

### Identity and classification

- `workflow: check-etf-performance`; `entity_key: NYSE Arca:EWK`; input ticker `EWK`; official fund `iShares MSCI Belgium ETF`; CUSIP `464286301`; fund inception `1996-03-12`; exchange `NYSE Arca`.
- `management_mode: passive-index`; the official objective is to track a broad-based index of Belgian equities. The current benchmark is `MSCI Belgium IMI 25/50 Index (Net)`, a free-float-adjusted, market-cap-weighted index of Belgian large-, mid- and small-cap equities subject to the 25/50 methodology.
- Primary region: `Belgium`; new region page `[[Belgium ETF]]`; canonical tag `geography/Belgium`; breadcrumb `[[ETF Region Index]] → [[Belgium ETF]] → [[ETF Performance Index]]`.
- `return_basis: NAV total return` with dividends and capital gains reinvested and expenses reflected in NAV; return currency USD. Market-price return is retained separately.

### Source map

| Source | URL/path | Use |
|---|---|---|
| iShares EWK product page | https://www.ishares.com/us/products/overview-v3-ishares-fund-data?portfolioId=239610&seoSlug=ishares-msci-belgium-capped-etf | official identity, NYSE Arca, benchmark, current NAV/YTD/price, assets, holdings, rolling returns, standard deviation, beta, valuation fields and sector exposures; current snapshot through `2026-08-11` / `2026-08-10` |
| iShares EWK June 2026 factsheet | https://www.ishares.com/us/literature/fact-sheet/ewk-ishares-msci-belgium-etf-fund-fact-sheet-en-us.pdf | official 2021-2025 NAV/market-price/benchmark rows, return definition, fee, launch, holdings, top holdings, sectors and benchmark-history note; as of `2026-06-30` |
| SEC EWK summary prospectus | https://www.sec.gov/Archives/edgar/data/930667/000119312525336632/d23588d497k.htm | official objective, NYSE Arca identity, index methodology and risk disclosures; December 2025 |
| S&P 500 index page and cached convention | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ plus cached URLs in the skill | common USD S&P 500 Total Return rows for 2021-2025; dividends reinvested, reference as of `2025-12-31` |

### Raw observations

- The official product page identifies EWK as an equity ETF on NYSE Arca tracking `MSCI Belgium IMI 25/50 Index (Net)`, with NAV `USD 26.75` as of `2026-08-11`, NAV TR YTD `12.61%` as of `2026-08-10`, closing price `USD 26.82`, net assets `USD 162,633,413`, 6,080,000 shares outstanding, semi-annual distributions and expense ratio `0.49%`.
- The same page reports fund inception `1996-03-12`, 38 holdings as of `2026-08-10`, 3-year standard deviation `14.38%` and beta `0.54` as of `2026-07-31`, P/B `1.79`, P/E `19.05`, and sector exposures as of `2026-08-10`: Health Care `25.98%`, Consumer Staples `25.25%`, Financials `16.78%`, Real Estate `9.53%`, Materials `7.57%`, Industrials `5.78%`, Utilities `2.58%`, Consumer Discretionary `1.87%`, Information Technology `1.48%`, Communication `1.40%`, Energy `1.25%`, and Cash/Derivatives `0.52%`.
- The June 2026 factsheet reports official NAV TR rows for 2021 `12.92%`, 2022 `-14.08%`, 2023 `7.46%`, 2024 `0.51%`, 2025 `34.96%`; market-price rows `12.87%`, `-13.93%`, `7.47%`, `0.17%`, `35.41%`; and MSCI Belgium IMI 25/50 benchmark rows `8.02%`, `-15.89%`, `7.71%`, `0.51%`, `35.30%`.
- The official product page's standardized performance table as of `2026-06-30` reports NAV 1-year `24.33%`, 3-year annualised `17.72%`, 5-year annualised `7.07%`, 10-year annualised `7.08%`, and since-inception `6.02%`; YTD `12.53%` is a June month-end field, while the later product-page date-to-date YTD `12.61%` is retained as the current snapshot.
- EWK began tracking the MSCI Belgium IMI 25/50 Index (Net) on `2012-11-09`; historical data before that date uses MSCI Belgium Investable Market Index (Net). The 2021-2025 annual table is post-transition.
- The factsheet's top-10 holdings total `69.05%` as of `2026-06-30`; Anheuser-Busch InBev `21.94%`, argenx `15.55%`, UCB `9.01%`, KBC Groep `4.65%`, Ageas `4.31%` and the remaining top holdings are retained as concentration context.
- Official daily NAV observations sufficient to reproduce maximum drawdown and recovery date were not disclosed in the reviewed sources. Systematic fair-value methodology is disclosed by iShares as a reason ETF total return may diverge from the benchmark.

### Calculations and reconciliation

- `Cumulative = ∏(1 + annual return) - 1`. Official EWK 2021-2025 NAV rows compound to `41.425042%`, displayed as `41.43%`; rounded-input CAGR is `7.177905%`, displayed as `7.18%`; population annual-return standard deviation is `16.089372%`, displayed as `16.09%`; up/down is `4/1`; best is 2025 `+34.96%`; worst is 2022 `-14.08%`; least-positive year is 2024 `+0.51%`.
- Official benchmark rows compound to `33.080646%` / rounded-input CAGR `5.882206%`; population annual-return standard deviation is `16.543411%`. Fund-minus-benchmark observations are `+4.90`, `+1.81`, `-0.25`, `0.00` and `-0.34` percentage points for 2021-2025; these are tracking/currency/fair-value context and are not called alpha.
- Cached S&P 500 TR compounds to `96.169618%` / rounded-input CAGR `14.426430%` for 2021-2025; it is a common USD reference, not EWK's strategy benchmark.
- The official rolling 10-year NAV TR `7.08%` as of `2026-06-30` is kept separate from the independently calculated 2021-2025 CAGR `7.18%`; the periods, endpoints and source fields differ.

### Source conflict and quality choice

- The iShares product page and June factsheet are the sources of truth for identity, classification, benchmark, annual NAV/market-price/benchmark rows, rolling fields, fee, holdings, sector and risk fields. Product-page YTD `12.61%` as of 2026-08-10 is kept separate from the June factsheet YTD `12.53%` and June standardized table; no conflict is manufactured.
- Market-price rows are displayed for reconciliation but excluded from NAV calculations. No secondary annual or price proxy is needed.
- The benchmark-history change on 2012-11-09 is recorded; 2021-2025 is treated as current-index history. The S&P 500 is labeled a common reference only.

### Planned durable paths and contents

- Create `wiki/analysis/performance/ETF_NYSE_ARCA_EWK Performance.md` with canonical `NYSE Arca:EWK`, official 2021-2025 NAV/market-price/benchmark/S&P rows, 41.43% / 7.18% calculations, official rolling 10-year 7.08%, current/June YTD separation, Belgium concentration and systematic fair-value notes, Belgium breadcrumb and `geography/Belgium` tag.
- Create `wiki/analysis/comparisons/Belgium ETF.md` as the new static region navigation page with the EWK row and links back to `[[ETF Region Index]]` and forward to `[[ETF Performance Index]]`.
- Update `wiki/analysis/comparisons/ETF Region Index.md` with Belgium count `1` and `[[Belgium ETF]]`; update `wiki/analysis/performance/ETF Performance Index.md` Browse by region with `[[Belgium ETF]]`.
- Update `wiki/analysis/performance/ETF Performance Index.md` with the EWK coverage row, 2021-2025 Common Window row and a `2026-08-19 Coverage Addition` bullet; no strict 2016-2025 annual ranking row is added because the reviewed official annual table does not expose 2016-2020 rows.
- Append one `etf-performance` workflow bullet to `log.md`; no entity hub, normalized financial table or `raw/funds/` file is planned.

### Local pre-save checklist

- PASS: official NYSE Arca identity, fund name, CUSIP, inception, passive-index classification, MSCI Belgium benchmark, fee, semi-annual distribution treatment, USD NAV return basis and all as-of dates are source-backed.
- PASS: official 2021-2025 NAV/market-price/benchmark rows, rolling 10-year field, current NAV/YTD, assets, holdings, valuation fields, beta, standard deviation, sectors and top holdings are preserved with separate dates; no 2016-2020 values are invented.
- PASS: 2021-2025 cumulative/CAGR, standard deviation, up/down count, best/worst year and S&P compounding recompute from the stated inputs; rolling 10-year is not relabeled as calendar CAGR.
- PASS: Belgium single-country/sector/top-holdings/liquidity risks, benchmark-history transition and systematic fair-value note are disclosed; daily NAV drawdown/recovery remains an explicit gap; no alpha claim is introduced.
- PASS: complete proposed performance page, new Belgium region page, region-index row, performance-index Browse/coverage/Common Window/bullet, source batch section and log bullet are specified; canonical breadcrumb, `geography/Belgium` tag and planned wikilinks resolve.
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
reason: Official iShares identity, passive Belgium classification, official 2021-2025 NAV/benchmark evidence, rolling 10-year/current fields, reconciled calculations and the scheduled-local pre-save checklist passed; benchmark-history, concentration, systematic fair-value and daily NAV gaps remain disclosed.

## HEDJ — WisdomTree Europe Hedged Equity Fund

### Identity and classification

- `workflow: check-etf-performance`; `entity_key: NYSE Arca:HEDJ`; input ticker `HEDJ`; official fund `WisdomTree Europe Hedged Equity Fund`; CUSIP `97717X701`; inception `2009-12-31`; official exchange `NYSE Arca`.
- `management_mode: passive-index`; SEC summary prospectus describes passive/indexing management with representative sampling. The fund seeks to track the `WisdomTree Europe Hedged Equity Index` before fees and expenses and does not attempt to outperform its index.
- The tracked index is a dividend-weighted European equity index with an exporter tilt and EUR/USD hedge. The current WisdomTree index page uses Bloomberg symbol `WTEHIP`; the fund product page and factsheet display related/legacy symbol `WTIDFTRH`. The index name is the canonical benchmark identity and the symbol discrepancy is preserved.
- `return_basis: NAV total return` with reinvested distributions and expenses reflected in NAV; return currency USD; market-price return and yields are kept separate. Primary region: `Europe`; canonical tag `geography/Europe`.

### Source map

| Source | URL/path | Use |
|---|---|---|
| WisdomTree HEDJ product page | https://www.wisdomtree.com/us/products/equity/hedj | official current identity, NYSE Arca context, NAV/price, rolling NAV/index returns, hedge ratio, assets, holdings, country and sector snapshots; current page through `2026-08-17`, month-end performance through `2026-07-31` |
| WisdomTree HEDJ factsheet | https://www.wisdomtree.com/-/media/us-media-files/documents/resource-library/fund-fact-sheets/international-equity/wisdomtree-factsheet-hedj-1056.pdf | official exchange, inception, fee, NAV/index rolling fields, 2025 year-end NAV/income observations, holdings and risks; all data as of `2026-06-30` |
| SEC HEDJ summary prospectus | https://www.sec.gov/Archives/edgar/data/1350487/000121465925011291/hedj73125497k.htm | official passive classification, objective, index rules, hedging risks, NYSE Arca listing and 2016-2024 annual-return chart; August 2025 |
| WisdomTree Europe Hedged Equity Index | https://www.wisdomtree.com/us/indexes/wtehip | current index identity, country/sector/valuation fields and current symbol `WTEHIP`; as of `2026-07-29` |
| WisdomTree rules-based methodology | https://www.wisdomtree.com/us/media/core-equity-index-methodology | official dividend-weighting, caps, index calculation and EUR hedge methodology; last updated July 2026 |
| AAII HEDJ performance page | https://www.aaii.com/etf/ticker/HEDJ | secondary dated annual NAV row used to reconcile calculated 2025; as of `2026-06-30` |
| Cached S&P 500 Total Return convention | check-etf-performance skill cache and original URLs | USD common reference for 2016-2025 and 2021-2025, dividends reinvested, reference as of `2025-12-31`; no new search |

### Raw observations

- WisdomTree official month-end performance as of `2026-07-31`: HEDJ NAV TR `1Y 18.71%`, `3Y 13.54%`, `5Y 10.97%`, `10Y 10.73%`, since inception `8.98%`; the underlying index is `19.27%`, `13.94%`, `11.30%`, `11.14%`, `9.41%` on the same rows. Current official NAV TR YTD is `9.15%` as of `2026-07-31`.
- Current WisdomTree product snapshot as of `2026-08-17`: NAV `USD 57.771`, closing market price `USD 57.870`, premium/discount `+0.17%`, total assets `$1,848,683.23k`, expense ratio `0.58%`, distribution yield `6.82%`, SEC 30-day yield `1.97%`, and aggregate hedge ratio `99.42%`. Yield fields are not NAV TR.
- The June 2026 factsheet identifies 130 holdings, ticker HEDJ, NYSE Arca, inception `12/31/2009`, net expense ratio `0.58%`, Bloomberg index symbol `WTIDFTRH`, and NAV/index rolling fields as of `2026-06-30`. It also reports year-end NAV observations and income: 2022 NAV `35.98`, 2023 `42.87`, 2024 `43.85`, 2025 `53.11`; annual income rows 2022 `0.99`, 2023 `1.42`, 2024 `1.43`, 2025 `0.87`.
- Official SEC 2025 summary-prospectus chart supplies complete calendar NAV TR rows for 2016-2024: `2016 9.30%`, `2017 13.56%`, `2018 -9.27%`, `2019 26.99%`, `2020 -2.90%`, `2021 23.57%`, `2022 -10.18%`, `2023 26.39%`, `2024 5.65%`. SEC states the chart assumes reinvestment of dividends/distributions.
- 2025 NAV TR is calculated from official year-end observations: `(53.11 + 0.87) / 43.85 - 1 = 23.3295%`, displayed as `23.33%‡`. AAII independently reports `23.3%` NAV total return for 2025 as of `2026-06-30`; it is a reconciliation check, not a substitute for the official product/factsheet source.
- Official current country weights as of `2026-08-17`: Germany `23.09%`, France `21.33%`, Spain `18.96%`, Netherlands `18.12%`, Italy `6.13%`, Finland `4.73%`, Belgium `4.46%`; sector weights include Industrials `23.11%`, Financials `16.71%`, Consumer Staples `12.42%`, Consumer Discretionary `11.93%`, Information Technology `11.76%`.
- Official daily NAV observations sufficient to reproduce maximum drawdown and recovery were not disclosed in the reviewed sources. Annual-return dispersion is used as descriptive evidence only; `risk-adjusted evidence: not-verified`.
- Cached S&P 500 TR rows are USD: 2016 `11.96%`, 2017 `21.83%`, 2018 `-4.38%`, 2019 `31.49%`, 2020 `18.40%`, 2021 `28.71%`, 2022 `-18.11%`, 2023 `26.29%`, 2024 `25.02%`, 2025 `17.88%`.

### Calculations and reconciliation

- `Cumulative = ∏(1 + annual return) - 1`: HEDJ 2016-2025 `153.817904%`, displayed `153.82%`; rounded-input calendar CAGR `9.762054%`, displayed `9.76%`; population annual-return standard deviation `13.755145%`, displayed `13.76%`; up/down `7/3`; best `2019 +26.99%`; least positive `2024 +5.65%`; worst `2022 -10.18%`; least-bad down year `2020 -2.90%`.
- HEDJ 2021-2025 compounds to `82.783523%`, displayed `82.78%`; rounded-input CAGR `12.820341%`, displayed `12.82%`; population annual-return standard deviation `14.044453%`, displayed `14.04%`; up/down `4/1`; best `2023 +26.39%`; worst `2022 -10.18%`.
- Cached S&P 500 TR compounds to `298.329111%` / rounded-input CAGR `14.821761%` over 2016-2025 and `96.169618%` / `14.426430%` over 2021-2025. It is a common USD reference, not the HEDJ management/tracked index, and no arithmetic alpha claim is made.
- The official rolling 10-year NAV TR `10.73%` as of `2026-07-31` is kept separate from the calendar-derived `9.76%`; endpoints, dates and source definitions differ.

### Source conflict and quality choice

- WisdomTree product page/factsheet and SEC prospectus are the sources of truth for HEDJ identity, exchange, passive method, objective, fees, index, current/rolling returns and risk. The SEC chart is used for 2016-2024 annual rows because the current product page exposes rolling fields but not a calendar table.
- The 2025 calculation uses official year-end NAV/income observations and is reconciled to AAII's rounded annual NAV row. It is marked `‡` and is not described as an issuer-published calendar row.
- `WTIDFTRH` versus `WTEHIP` is preserved as an issuer display-symbol discrepancy; the index name and hedge methodology remain consistent. No market-price return, distribution yield or S&P arithmetic difference is mixed into the NAV analysis.

### Planned durable paths and contents

- Create `wiki/analysis/performance/ETF_NYSE_ARCA_HEDJ Performance.md` with canonical `NYSE Arca:HEDJ`, official passive/index identity, USD NAV annual table for 2016-2025, calculated 2025 marker `‡`, rolling 10-year/YTD/current NAV fields, S&P common reference, hedge/country/sector risk, source links, `geography/Europe` tag and breadcrumb.
- Update `wiki/analysis/comparisons/Europe ETF.md` with the HEDJ row, `10.73%` issuer rolling field, `12.82%‡` calendar common-window CAGR, `9.15%` YTD and calculated-2025/index-symbol caveat.
- Update `wiki/analysis/comparisons/ETF Region Index.md` Europe count from `27` to `28`; no new region page is needed.
- Update `wiki/analysis/performance/ETF Performance Index.md` with HEDJ coverage row, marked `‡` Common Window row and 2026-08-19 coverage bullet; do not add HEDJ to the strict official 2016-2025 ranking because 2025 is calculated rather than an issuer calendar row.
- Append one `log.md` workflow bullet; no entity hub, normalized financial table or `raw/funds/` file is planned because this workflow owns the numeric performance page.

### Local pre-save checklist

- PASS: canonical `NYSE Arca:HEDJ` identity, fund name, CUSIP, inception, passive eligibility, WisdomTree tracked index, NYSE Arca exchange, 0.58% fee, USD NAV TR definition, current NAV/YTD, rolling fields and all as-of dates are source-backed.
- PASS: official SEC 2016-2024 annual rows are separated from the calculated 2025 official-observation row and from cached S&P USD rows; market price, distribution yield and SEC yield are not mixed into NAV TR; `‡` caveat is visible.
- PASS: 2016-2025 and 2021-2025 cumulative/CAGR/dispersion/up-down/best-worst calculations recompute from the displayed inputs; issuer rolling 10-year field remains separate from calendar CAGR; no alpha or manager-skill claim is made.
- PASS: hedge ratio, country/sector/top-holding concentration, hedge-cost/forward/counterparty risks, index-symbol discrepancy and daily NAV drawdown/recovery gap are disclosed; risk-adjusted evidence remains `not-verified`.
- PASS: complete proposed performance page, source batch section, Europe row/count, performance-index coverage/Common Window/bullet and log bullet are specified; canonical breadcrumb, `geography/Europe` tag and all planned wikilinks resolve.
- PASS: no unresolved High/Medium finding blocks the write and no WARNING requiring confirmation remains. Required scheduled audit lines are present: `verification_mode: scheduled-local` and `reviewer_dispatch: not-attempted-by-design`.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official WisdomTree/SEC identity, passive classification, 2016-2024 NAV rows, calculated-and-reconciled 2025 return, official rolling/YTD fields, source reconciliation and the scheduled-local pre-save checklist passed; hedge, concentration, index-symbol and daily NAV gaps remain disclosed.

## EIRL — iShares MSCI Ireland ETF

### Identity and classification

- `workflow: check-etf-performance`; `entity_key: NYSE Arca:EIRL`; input ticker `EIRL`; official fund `iShares MSCI Ireland ETF`; CUSIP `46429B507`; fund inception `2010-05-05`; exchange `NYSE Arca`.
- `management_mode: passive-index`; iShares states that the fund seeks to track a broad-based index of Irish equities. The current underlying index is `MSCI All Ireland Capped Index (Net)`, free-float-adjusted and market-capitalization-weighted, subject to MSCI eligibility and capping rules.
- Primary region: `Ireland`; new region page `[[Ireland ETF]]`; canonical tag `geography/Ireland`; breadcrumb `[[ETF Region Index]] → [[Ireland ETF]] → [[ETF Performance Index]]`.
- `return_basis: NAV total return` with dividends and capital gains reinvested and expenses reflected in NAV; return currency USD. Market-price return is retained separately.

### Source map

| Source | URL/path | Use |
|---|---|---|
| iShares EIRL product page | https://www.ishares.com/us/products/239662/ishares-msci-ireland-capped-etf | official identity, exchange, benchmark, current NAV/YTD/price/assets, holdings, rolling returns, standard deviation, beta, valuation fields and sector/geography exposures; current snapshot through `2026-08-17` / `2026-08-14` |
| iShares EIRL June 2026 factsheet | https://www.ishares.com/us/literature/fact-sheet/eirl-ishares-msci-ireland-etf-fund-fact-sheet-en-us.pdf | official launch, fee, benchmark-history note, top holdings, sector/geography context and return definitions; as of `2026-06-30` |
| iShares EIRL December 2025 summary prospectus | https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-ireland-capped-etf-8-31.pdf | official objective, passive/index methodology, expense ratio, 2015-2024 calendar-year chart and risk disclosures |
| S&P 500 index page and cached convention | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ and cached URLs in `check-etf-performance/SKILL.md` | common USD S&P 500 Total Return reference for complete calendar years `2016-2025`; dividends reinvested, as of `2025-12-31` |

### Raw observations

- The official iShares product page identifies EIRL as an equity ETF on NYSE Arca tracking `MSCI All Ireland Capped Index (Net)`, with NAV `USD 82.88`, closing price `USD 83.01`, non-fair-value NAV `USD 83.11`, net assets `$78,733,413`, premium `0.16%`, and 950,000 shares outstanding as of `2026-08-17`. It reports NAV Total Return YTD `15.05%` as of `2026-08-14`, 30-day SEC yield `2.59%` and trailing 12-month yield `2.37%` as of `2026-07-31`, expense ratio `0.50%`, and semi-annual distributions.
- The same page reports 26 holdings as of `2026-08-14`, 3-year standard deviation `16.21%` and beta `0.77` as of `2026-07-31`, P/B `1.73` and P/E `17.50` as of `2026-08-14`, and rolling NAV returns as of `2026-06-30`: 1-year `19.47%`, 3-year annualised `13.50%`, 5-year `8.53%`, 10-year `9.94%` and since inception `9.86%`.
- Official exposure as of `2026-08-14`: Ireland `74.52%`, United Kingdom `12.80%`, United States `10.28%`, Bermuda `1.65%`, cash/derivatives `0.52%`, other `0.23%`; sectors include Financials `38.79%`, Consumer Staples `19.13%`, Industrials `14.62%`, Health Care `10.36%`, Consumer Discretionary `6.45%` and Energy `5.81%`.
- The June 2026 factsheet reports 25 holdings and top holdings including AIB Group `16.39%`, Bank of Ireland Group `14.65%`, Kerry Group `10.51%`, Icon `6.46%`, Ryanair `5.10%`, Glanbia `5.03%`, Kingspan `4.66%`, DCC `4.27%`, Grafton `3.56%` and Cairn Homes `3.52%`; top-ten concentration is `74.15%` as of `2026-06-30`.
- The December 2025 summary prospectus calendar chart reports EIRL NAV returns: 2015 `19.94%`, 2016 `-6.96%`, 2017 `28.58%`, 2018 `-20.99%`, 2019 `26.61%`, 2020 `10.80%`, 2021 `13.62%`, 2022 `-18.63%`, 2023 `34.06%`, and 2024 `-1.74%`. The current iShares performance table reports 2021 `13.62%`, 2022 `-18.63%`, 2023 `34.06%`, 2024 `-1.74%`, 2025 `28.63%` for NAV Total Return; market-price rows are kept separate.
- The current iShares performance table reports MSCI All Ireland Capped Index benchmark rows for 2021 `14.52%`, 2022 `-18.19%`, 2023 `35.59%`, 2024 `-0.76%`, and 2025 `30.42%`. It does not expose the 2016-2020 benchmark rows in the reviewed capture, so those fields remain `not disclosed`.
- iShares states that EIRL began tracking the MSCI All Ireland Capped Index on `2013-11-27`; historical index data before that date uses the MSCI Ireland Investable Market 25/50 Index. Official daily NAV observations sufficient to reproduce maximum drawdown and recovery were not disclosed in the reviewed sources.
- Cached S&P 500 TR rows for `2016-2025` are USD: `11.96%`, `21.83%`, `-4.38%`, `31.49%`, `18.40%`, `28.71%`, `-18.11%`, `26.29%`, `25.02%`, `17.88%`; dividends reinvested, reference as of `2025-12-31`.

### Calculations and reconciliation

- `Cumulative = ∏(1 + annual return) - 1`: official EIRL 2016-2025 NAV rows compound to `107.716167%`, displayed as `107.72%`; rounded-input calendar CAGR is `7.583837%`, displayed as `7.58%`; population annual-return standard deviation is `19.397720%`, displayed as `19.40%`; up/down is `6/4`; best is 2023 `+34.06%`; least positive is 2020 `+10.80%`; worst is 2018 `-20.99%`; least-bad down year is 2024 `-1.74%`.
- Official EIRL 2021-2025 NAV rows compound to `56.652506%`, displayed as `56.65%`; rounded-input CAGR is `9.392480%`, displayed as `9.39%`; population annual-return standard deviation for this five-year subset is `19.439715%`; up/down is `3/2`.
- Official benchmark rows for 2021-2025 compound to `64.416858%` / rounded-input CAGR `10.455989%`. Rounded fund-minus-benchmark observations are `-0.90`, `-0.44`, `-1.53`, `-0.98` and `-1.79` percentage points; these are tracking/fee/fair-value context and are not called alpha.
- Cached S&P 500 TR compounds to `298.329111%` / rounded-input CAGR `14.821761%` over 2016-2025 and `96.169618%` / `14.426430%` over 2021-2025. It is a common USD reference, not EIRL's strategy benchmark.
- The official rolling 10-year NAV TR `9.94%` as of `2026-06-30` is kept separate from the complete-calendar CAGR `7.58%`; dates, endpoints and source fields differ.

### Source conflict and quality choice

- iShares product page, factsheet and summary prospectus are the sources of truth for EIRL identity, passive method, benchmark, annual NAV rows, rolling fields, fee, holdings, exposure and risk fields. The product page exposes 2021-2025 benchmark rows but not 2016-2020 benchmark rows; the latter remain `not disclosed` rather than backfilled.
- The current product page's 2025 NAV row is used with the prospectus chart's 2016-2024 rows. Market-price rows, yield fields and current NAV are kept separate from the NAV Total Return calculation.
- The S&P 500 is labeled a common USD reference only. No arithmetic difference versus S&P or the tracked benchmark is described as alpha or manager skill.

### Planned durable paths and contents

- Create `wiki/analysis/performance/ETF_NYSE_ARCA_EIRL Performance.md` with canonical `NYSE Arca:EIRL`, official passive/index identity, USD NAV annual table for 2016-2025, 2021-2025 benchmark rows, S&P common reference, 107.72% / 7.58% and 56.65% / 9.39% calculations, rolling/YTD/current fields, Ireland concentration risks, sources and breadcrumb/tag.
- Create `wiki/analysis/comparisons/Ireland ETF.md` as the new static region navigation page with the EIRL row and links back to `[[ETF Region Index]]` and forward to `[[ETF Performance Index]]`.
- Update `wiki/analysis/comparisons/ETF Region Index.md` with Ireland count `1` and `[[Ireland ETF]]`; update `wiki/analysis/performance/ETF Performance Index.md` Browse by region, coverage row, Common Window row and `2026-08-19 Coverage Addition` bullet.
- Append one `log.md` workflow bullet; no entity hub, normalized financial table or `raw/funds/` file is planned because this workflow owns the numeric performance page.

### Local pre-save checklist

- PASS: canonical NYSE Arca identity, fund name, CUSIP, inception, passive-index classification, MSCI All Ireland Capped benchmark, fee, semi-annual distribution treatment, USD NAV return basis and all as-of dates are source-backed.
- PASS: official 2016-2024 prospectus rows, 2025/current-page NAV row, 2021-2025 benchmark rows, rolling fields, current NAV/YTD, assets, holdings, valuation fields, beta, standard deviation, sectors and top holdings are preserved with separate dates; unavailable 2016-2020 benchmark rows are explicitly `not disclosed`.
- PASS: 2016-2025 and 2021-2025 cumulative/CAGR, standard deviation, up/down count, best/worst year, benchmark reconciliation and S&P compounding recompute from the stated inputs; rolling 10-year is not relabeled as calendar CAGR.
- PASS: Ireland/country, financials, consumer-staples, top-holdings, FX, liquidity and systematic fair-value risks are disclosed; benchmark-history transition and daily NAV drawdown/recovery remain explicit gaps; no alpha claim is introduced.
- PASS: complete proposed performance page, new Ireland region page, region-index row, performance-index Browse/coverage/Common Window/bullet, source batch section and log bullet are specified; canonical breadcrumb, `geography/Ireland` tag and planned wikilinks resolve.
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
reason: Official iShares identity, passive Ireland classification, official 2016-2025 NAV evidence, official 2021-2025 benchmark rows, rolling/current fields, reconciled calculations and the scheduled-local pre-save checklist passed; benchmark-history, country/sector concentration, FX/liquidity and daily NAV gaps remain disclosed.

## FLSW — Franklin FTSE Switzerland ETF

### Workflow and identity

- `workflow: check-etf-performance`; caller: `trello-etf-processing`; mode: `lean`; `execution_profile: scheduled-inline`; input ticker `FLSW`.
- Canonical identity: `NYSE Arca:FLSW`; Franklin official fund name `Franklin FTSE Switzerland ETF`; inception `2018-02-06`; CUSIP `35473P694`; ISIN `US35473P6943`; exchange `NYSE Arca`.
- Management mode: `passive-index`; the fund seeks to track the `FTSE Switzerland RIC Capped Index` before fees and expenses. The index is a market-cap-weighted Swiss large-/mid-cap index with security caps. No active-management fields apply.
- Return basis: official USD `NAV Total Return`, distributions reinvested and fund expenses deducted. Market-price return, current NAV, portfolio multiples and yield fields are not mixed into NAV TR.

### Source map

| Source | URL/path | Use |
|---|---|---|
| Franklin FLSW product page | https://www.franklintempleton.com/investments/options/exchange-traded-funds/products/26352/SINGLCLASS/franklin-ftse-switzerland-etf/FLSW | official identity, exchange, benchmark, inception, expense ratio, rolling NAV returns, current NAV/YTD, assets, holdings, sectors and portfolio statistics; current fields through 2026-08-09, with NAV/YTD as of 2026-08-07 |
| Franklin FLSW factsheet | https://www.franklintempleton.com/forms-literature/download/FLSW-FF | official 2019-2025 calendar NAV/market-price/index rows, total-return definitions, 0.09% expense ratio and 3-year NAV standard deviation `15.88%` versus index `15.91%`; factsheet as of 2026-03-31 |
| Franklin FLSW summary prospectus | https://www.franklintempleton.com/forms-literature/download-preview/FLSW-PSUM | official objective, annual-return disclosure and passive/index context |
| S&P 500 Total Return cached convention | skill cache and original S&P DJI references | USD common reference for 2019-2025 and 2021-2025, dividends reinvested, reference as of 2025-12-31 |
| Slickcharts S&P 500 YTD | https://www.slickcharts.com/sp500/returns/ytd | secondary current S&P 500 total-return YTD cross-check `13.38%` as of 2026-08-07; kept separate from official Franklin YTD |

### Raw observations

- Franklin official calendar NAV TR rows: 2019 `32.66%`, 2020 `14.15%`, 2021 `20.40%`, 2022 `-18.30%`, 2023 `16.71%`, 2024 `-1.41%`, 2025 `33.10%`.
- Franklin official tracked-index rows: 2019 `32.19%`, 2020 `13.30%`, 2021 `19.98%`, 2022 `-18.50%`, 2023 `16.27%`, 2024 `-1.83%`, 2025 `32.80%`.
- Cached S&P 500 TR rows for the same years: 2019 `31.49%`, 2020 `18.40%`, 2021 `28.71%`, 2022 `-18.11%`, 2023 `26.29%`, 2024 `25.02%`, 2025 `17.88%`; USD, dividends reinvested.
- Official rolling NAV TR as of 2026-06-30: 1Y `18.06%`, 3Y `13.53%`, 5Y `7.87%`, 10Y `not applicable`, since inception `10.12%`.
- Official current snapshot: NAV `$44.38` and NAV TR YTD `8.87%` as of 2026-08-07; total net assets `$84.32M` as of 2026-08-09; 50 holdings, P/E `26.69x`, P/B `4.50x` and sector allocation as of 2026-08-06; expense ratio `0.09%` as of 2026-08-01.
- Official sector allocation as of 2026-08-06: Health Care `38.85%`, Financials `18.10%`, Industrials `13.67%`, Consumer Staples `13.42%`, Materials `8.52%`; residual sectors and cash are retained on the issuer page.
- Official 3-year NAV standard deviation is `15.88%` versus benchmark `15.91%`, factsheet as of 2026-03-31. Official daily observations sufficient to reproduce NAV maximum drawdown and recovery were not disclosed in the reviewed sources.

### Calculations and reconciliation

- Formula: `cumulative = Π(1 + annual NAV TR) - 1`; `CAGR = (1 + cumulative)^(1 / years) - 1`.
- FLSW 2019-2025: cumulative `128.130548%`, rounded-input CAGR `12.504285%`, population annual-return standard deviation `17.079739%`, up/down `5/2`, best 2025 `33.10%`, least positive 2020 `14.15%`, worst 2022 `-18.30%`, least-bad down year 2024 `-1.41%`.
- FLSW 2021-2025: cumulative `50.649444%`, rounded-input CAGR `8.540922%`, up/down `3/2`.
- Tracked index 2019-2025: cumulative `121.993121%`, rounded-input CAGR `12.066827%`; 2021-2025 cumulative `48.221432%`, rounded-input CAGR `8.188774%`.
- Cached S&P 500 TR 2019-2025: cumulative `205.405022%`, rounded-input CAGR `17.291901%`; 2021-2025 cumulative `96.169618%`, rounded-input CAGR `14.426430%`.
- FLSW-minus-tracked-index annual differences are approximately `+0.47`, `+0.85`, `+0.42`, `+0.20`, `+0.44`, `+0.42`, and `+0.30` percentage points for 2019-2025; these are passive tracking observations, not alpha.

### Source conflict and quality choice

- Franklin product page and factsheet are the sources of truth for identity, passive classification, benchmark, fee, current fields, annual NAV rows and risk fields. The current product page has a newer YTD snapshot than the factsheet; the official product-page `8.87%` as of 2026-08-07 is used and the older factsheet YTD is not mixed into the result.
- The official Franklin annual table starts at the first complete post-inception year 2019; the partial 2018 inception year is omitted rather than inferred.
- The S&P annual comparison reuses the permitted cached 2016-2025 convention. Current YTD is outside the cache and is shown only as a clearly labelled same-date secondary cross-check; it is not used for the annual table or CAGR.
- Official daily NAV drawdown/recovery evidence was not available, so the performance page records `not found / not verified` rather than substituting price-only data.

### Planned durable paths and contents

- Create `wiki/analysis/performance/ETF_NYSE_ARCA_FLSW Performance.md` with canonical `NYSE Arca:FLSW`, official passive identity, USD NAV TR annual rows 2019-2025, the 2021-2025 Common Window row, current/rolling fields, source links, Swiss sector/FX/concentration risks, `geography/Switzerland` tag and breadcrumb `[[ETF Region Index]] → [[Switzerland ETF]] → [[ETF Performance Index]]`.
- Create `wiki/analysis/comparisons/Switzerland ETF.md` as the static region navigation page with one FLSW row, a link back to `[[ETF Region Index]]`, a link forward to `[[ETF Performance Index]]`, and no copied annual table.
- Update `wiki/analysis/comparisons/ETF Region Index.md` with Switzerland count `1` and `[[Switzerland ETF]]`; update the Browse by region links in `wiki/analysis/performance/ETF Performance Index.md`.
- Update `wiki/analysis/performance/ETF Performance Index.md` with the FLSW coverage row, official 2021-2025 Common Window row, and a 2026-08-19 coverage-addition bullet. FLSW is not added to the strict 2016-2025 ranking because its history begins in 2018 and the 2018 row is partial.
- Append one `etf-performance` workflow bullet to `log.md`; no entity hub, normalized financial table, or `raw/funds/` file is planned.

### Local pre-save checklist

- PASS: canonical exchange-qualified identity, fund name, ticker, inception, passive-index eligibility, tracked index, fee, distribution cadence, USD NAV TR basis and all as-of dates are source-backed.
- PASS: official 2019-2025 NAV/index rows, rolling fields, current NAV/YTD, assets, holdings, valuation fields, sectors and standard deviation are separated by source/as-of date; partial 2018 and unavailable daily NAV drawdown/recovery are explicit gaps.
- PASS: 2019-2025 and 2021-2025 cumulative/CAGR, annual dispersion, up/down count and best/worst subset recompute from the displayed inputs; no 10-year CAGR is claimed.
- PASS: tracked-index comparison is labelled passive tracking evidence, S&P annual rows use the cached USD convention, current S&P YTD is a separate secondary cross-check, and no arithmetic difference is called alpha.
- PASS: Switzerland is the sole primary exposure region; the new region page, canonical breadcrumb, `geography/Switzerland` tag, region-index row, performance-index links and source/log paths are planned and resolve.
- PASS: complete proposed performance page, region page, source batch section and log bullet were reviewed locally; no High/Medium finding remains and no confirmation-required WARNING remains.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official Franklin identity, passive classification, 2019-2025 NAV evidence, current/rolling fields, reconciled calculations and the scheduled-local pre-save checklist passed; Swiss concentration, CHF/USD and daily NAV drawdown/recovery gaps remain disclosed.

## HEDK — WisdomTree Europe Equity UCITS ETF - USD Hedged Acc / WEEUF alias

### Identity and classification

- `workflow: check-etf-performance`; `execution_profile: scheduled-inline`; `entity_key: LSE:HEDK`; `input_ticker: WEEUF`.
- Official WisdomTree identity is `WisdomTree Europe Equity UCITS ETF - USD Hedged Acc`, ISIN `IE00BYQCZP72`, with official USD London Stock Exchange listing `HEDK`; `WEEUF` is retained as the OTC input alias for traceability.
- `management_mode: passive-index`; physical full replication; accumulating; base/NAV currency USD; inception 2016-11-01; TER 0.58%.
- Tracked index: `WisdomTree Europe Hedged Equity UCITS Index`. Primary region: Europe. Return basis: USD NAV Total Return, net of fees, with income reinvested; no market-price proxy is mixed into the result.

### Source map

| Evidence | URL / path | Use and as-of |
|---|---|---|
| WisdomTree product page | https://www.wisdomtree.com/ie/products/equities/wisdomtree-europe-equity-ucits-etf---usd-hedged-acc | official identity, ISIN, LSE HEDK/HEDS listings, objective, index, structure, current NAV/AUM/TER; product snapshot 2026-08-11 |
| WisdomTree factsheet | https://dataspanapi.wisdomtree.com/pdr/documents/FACTSHEET/UCITS/EU/EN-GB/IE00BYQCZP72/ | official NAV TR, index rows, calendar returns, exposure and risk fields; document date 2026-07-31 |
| StockAnalysis WEEUF page | https://stockanalysis.com/quote/otc/WEEUF/ | secondary OTC alias/name cross-check only; not used for performance values |
| S&P 500 definition and cached workflow convention | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | USD total-return common reference, dividends reinvested; cached annual rows as of 2025-12-31 |

### Raw observations

- Official listing table maps the USD London line to `LSE:HEDK` and the GBp line to `LSE:HEDS`, both ISIN `IE00BYQCZP72`; the OTC `WEEUF` label is not treated as a separate fund.
- Official product snapshot: NAV `US$44.125`, fund AUM `US$116,181,561`, and TER `0.58%` as of 2026-08-11. Official factsheet performance fields as of 2026-07-31: NAV TR YTD `9.03%`, 1-year `18.57%`, 3-year annualised `13.19%`, and available-period annualised return since inception `10.85%`.
- Official HEDK NAV TR calendar rows: 2017 `13.74%`, 2018 `-9.14%`, 2019 `27.22%`, 2020 `-2.50%`, 2021 `23.68%`, 2022 `-10.04%`, 2023 `25.73%`, 2024 `5.66%`, 2025 `22.87%`.
- Official tracked-index rows for the same years: 2017 `13.99%`, 2018 `-9.06%`, 2019 `27.54%`, 2020 `-2.28%`, 2021 `24.23%`, 2022 `-9.98%`, 2023 `25.99%`, 2024 `5.75%`, 2025 `23.19%`.
- Official exposure snapshot as of 2026-07-31: Germany `22.83%`, France `21.45%`, Spain `19.56%`, Netherlands `17.62%`, Italy `5.51%`; leading sectors Industrials `20.91%`, Financials `17.21%`, Consumer Staples `13.82%`, Consumer Discretionary `12.60%`, and Information Technology `10.86%`.
- Cached S&P 500 TR rows for 2017-2025: `21.83%`, `-4.38%`, `31.49%`, `18.40%`, `28.71%`, `-18.11%`, `26.29%`, `25.02%`, and `17.88%`, respectively; USD, dividends reinvested.

### Calculations and reconciliation

- Formula: `cumulative = Π(1 + annual NAV TR) - 1`; `CAGR = (1 + cumulative)^(1 / years) - 1`; calculations use the displayed rounded annual inputs.
- HEDK 2017-2025: cumulative `132.803908%` → `132.80%`; rounded-input CAGR `9.844090%` → `9.84%`; up/down `6/3`; best 2019 `+27.22%`; worst 2022 `-10.04%`; population annual-return volatility `14.329313%` → `14.33%`.
- HEDK 2021-2025: cumulative `81.611901%` → `81.61%`; rounded-input CAGR `12.675336%` → `12.68%`.
- Cached S&P 500 TR 2017-2025: cumulative `255.778056%` → `255.78%`; CAGR `15.144216%` → `15.14%`. For 2021-2025: cumulative `96.169618%` → `96.17%`; CAGR `14.426431%` → `14.43%`.
- HEDK-minus-tracked-index annual gaps are approximately `-0.25`, `-0.08`, `-0.32`, `-0.22`, `-0.55`, `-0.06`, `-0.26`, `-0.09`, and `-0.32` percentage points for 2017-2025. These are passive tracking observations, not alpha.
- A 10-year NAV TR CAGR is not calculated: inception 2016-11-01 to latest verified performance 2026-07-31 is under ten elapsed years. The issuer `10.85%` field is retained as available-period since-inception annualised return, not relabelled as 10-year CAGR. Daily NAV observations sufficient for maximum drawdown/recovery were not disclosed.

### Source conflict and quality choice

- WisdomTree product page and factsheet are the sources of truth for identity, listing, classification, fees, return rows, current fields and exposures. StockAnalysis is used only to bridge the input alias `WEEUF` and is not used for performance arithmetic.
- The S&P 500 annual series reuses the permitted cached 2016-2025 convention because 2017-2025 is a subset of that window; no fresh S&P search was needed. No arithmetic HEDK-minus-S&P difference is labelled alpha.
- USD-hedging via monthly-rolled forwards, Eurozone country/sector concentration, TER drag and unavailable daily NAV drawdown/recovery are retained as explicit risk gaps; market-price history is not substituted for NAV risk evidence.

### Planned durable paths and contents

- Create `wiki/analysis/performance/ETF_LSE_HEDK Performance.md` with canonical `LSE:HEDK`, input alias `WEEUF`, USD NAV TR annual rows 2017-2025, 2021-2025 common-window metrics, current/available-period fields, sources and Europe breadcrumb/tag.
- Update `wiki/analysis/comparisons/Europe ETF.md` with one HEDK navigation row and a compact note; update `wiki/analysis/comparisons/ETF Region Index.md` Europe count from 28 to 29.
- Update `wiki/analysis/performance/ETF Performance Index.md` with HEDK coverage, 2021-2025 common-window row and 2026-08-19 coverage bullet; append one workflow bullet to `log.md`.
- No entity hub, normalized financial table or `raw/funds/` file is planned.

### Local pre-save checklist

- PASS: canonical exchange-qualified identity, alias bridge, ISIN, passive-index eligibility, tracked index, TER, accumulation, USD NAV TR basis and all as-of dates are source-backed.
- PASS: official 2017-2025 fund/index rows, current NAV/AUM/TER, YTD/1Y/3Y/inception fields, exposure weights and cached S&P rows are separated by source and date; no 10-year CAGR or market-price proxy is claimed.
- PASS: cumulative/CAGR, 2021-2025 window, up/down count, annual volatility, best/worst years and fund-minus-index tracking gaps recompute from displayed inputs; no arithmetic difference is called alpha.
- PASS: Europe is the sole primary exposure region; the canonical breadcrumb/tag, Europe row, region count, performance-index links, source batch section and log bullet are planned and resolve.
- PASS: complete proposed contents of every durable file were reviewed locally; no High/Medium finding remains and no confirmation-required WARNING remains.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official WisdomTree identity, passive classification, 2017-2025 NAV rows, current/available-period fields, reconciled calculations and scheduled-local pre-save checklist passed; under-10-year history, USD hedge/concentration and daily NAV drawdown/recovery gaps remain disclosed.

## EWL — iShares MSCI Switzerland ETF

### Identity and classification

- `workflow: check-etf-performance`; `execution_profile: scheduled-inline`; `entity_key: NYSE_ARCA:EWL`; `input_ticker: EWL`.
- Official fund: `iShares MSCI Switzerland ETF`, CUSIP `464286749`, NYSE Arca, launch date `1996-03-12`; asset class equity; semi-annual distributions.
- `management_mode: passive-index`; the fund seeks to track `MSCI Switzerland 25/50 Index (Net)`, a free-float-adjusted, market-cap-weighted Swiss large-/mid-cap index with issuer capping methodology.
- Return basis: official USD NAV Total Return, net of fund expenses, with dividends/distributions reinvested. Market-price return is kept separate.
- Primary region: Switzerland. Expense ratio `0.50%`.

### Source map

| Evidence | URL / path | Use and as-of |
|---|---|---|
| iShares product page | https://www.ishares.com/us/products/239685/ishares-msci-switzerland-etf | official identity, NYSE Arca, benchmark, inception, current NAV/AUM, current YTD, rolling performance, sectors, holdings count, standard deviation and fees; page snapshot current fields through 2026-08-18 |
| iShares factsheet | https://www.ishares.com/us/literature/fact-sheet/ewl-ishares-msci-switzerland-etf-fund-fact-sheet-en-us.pdf | official 2021-2025 NAV/benchmark rows, 2025 return, rolling returns, top holdings, sector weights and risk fields; as of 2026-06-30 |
| iShares summary prospectus | https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-switzerland-capped-etf-8-31.pdf | official 2015-2024 calendar chart, index strategy, fees and principal risks; dated 2025-12-30 |
| S&P 500 definition and cached workflow convention | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | USD Total Return common reference; cached annual rows for 2016-2025, dividends reinvested, reference as of 2025-12-31 |

### Raw observations

- Official key facts: NAV `US$62.86`, net assets `US$2,388,778,706` and closing price `US$62.91` as of 2026-08-18; 40 holdings as of 2026-08-17; NAV TR YTD `7.02%` as of 2026-08-17; expense ratio `0.50%`.
- Official rolling performance as of 2026-06-30: NAV TR 1-year `16.53%`, 3-year `12.91%`, 5-year `7.39%`, 10-year `10.04%`, and since inception `7.68%`; benchmark rows are 1-year `17.41%`, 3-year `13.08%`, 5-year `7.51%`, and 10-year `10.19%`.
- Official EWL NAV TR calendar rows selected for the complete 2016-2025 window: 2016 `-3.04%`, 2017 `23.37%`, 2018 `-9.78%`, 2019 `32.27%`, 2020 `12.66%`, 2021 `19.27%`, 2022 `-18.57%`, 2023 `17.37%`, 2024 `-2.64%`, 2025 `32.54%`.
- Source provenance for annual rows: 2016-2024 are from the official summary-prospectus calendar-year chart; 2025 is from the official June 30, 2026 factsheet/product capture. The 2015 chart row `0.51%` is retained in source evidence but omitted from the 10-year calculation.
- Official tracked-index rows available for 2021-2025: 2021 `19.86%`, 2022 `-18.79%`, 2023 `17.32%`, 2024 `-2.10%`, 2025 `32.89%`.
- Official current risk/portfolio fields: 3-year standard deviation `15.30%` as of 2026-07-31; sector weights as of 2026-08-17 include Health Care `37.30%`, Financials `18.26%`, Industrials `13.15%`, Consumer Staples `13.13%`, Materials `7.26%`, Consumer Discretionary `6.19%`; factsheet top holdings as of 2026-06-30 include Roche `12.84%`, Novartis `12.67%`, Nestlé `11.64%`, ABB `6.34%`, and Richemont `5.04%`.
- Cached S&P 500 TR rows for 2016-2025: `11.96%`, `21.83%`, `-4.38%`, `31.49%`, `18.40%`, `28.71%`, `-18.11%`, `26.29%`, `25.02%`, and `17.88%`, respectively; USD, dividends reinvested.

### Calculations and reconciliation

- Formula: `cumulative = Π(1 + annual NAV TR) - 1`; `CAGR = (1 + cumulative)^(1 / years) - 1`; calculations use displayed rounded annual inputs.
- EWL 2016-2025: cumulative `136.557316%` → `136.56%`; rounded-input CAGR `8.991753%` → `8.99%`; up/down `6/4`; best 2025 `+32.54%`; worst 2022 `-18.57%`; population annual-return volatility `16.929858%` → `16.93%`.
- EWL 2021-2025: cumulative `47.095806%` → `47.10%`; rounded-input CAGR `8.023951%` → `8.02%`.
- Cached S&P 500 TR 2016-2025: cumulative `298.329111%` → `298.33%`; rounded-input CAGR `14.821761%` → `14.82%`. For 2021-2025: cumulative `96.169618%` → `96.17%`; CAGR `14.426430%` → `14.43%`.
- EWL-minus-tracked-index annual differences for 2021-2025 are `-0.59`, `+0.22`, `+0.05`, `-0.54`, and `-0.35` percentage points. These are passive tracking observations, not alpha.
- The issuer's rolling 10-year NAV TR `10.04%` is kept separate from the rounded-input 2016-2025 calendar CAGR `8.99%`; no arithmetic substitution is made. Current EWL YTD `7.02%` as of 2026-08-17 is not compared with the older benchmark YTD `6.15%` as of 2026-06-30.

### Source conflict and quality choice

- iShares product page, factsheet and summary prospectus are the sources of truth. The annual table combines official documents with clearly labelled period provenance: prospectus chart through 2024 and factsheet/product-page 2025 row; no values are inferred between them.
- The S&P annual comparison reuses the permitted cached 2016-2025 convention. No fresh S&P search is required for this complete cached window, and no arithmetic fund-minus-S&P difference is labelled alpha.
- The product page's current fields, factsheet risk snapshot and prospectus risk language have different as-of dates; they remain separated. Systematic fair-value, foreign-market timing, non-diversification, issuer/sector concentration and daily NAV drawdown/recovery gaps are disclosed.

### Planned durable paths and contents

- Create `wiki/analysis/performance/ETF_NYSE_ARCA_EWL Performance.md` with canonical `NYSE Arca:EWL`, USD NAV TR annual rows 2016-2025, 2021-2025 common-window metrics, issuer rolling fields, official benchmark rows, risk notes, sources and Switzerland breadcrumb/tag.
- Update `wiki/analysis/comparisons/Switzerland ETF.md` with the EWL navigation row/note and forward link; update `wiki/analysis/comparisons/ETF Region Index.md` Switzerland count from 1 to 2.
- Update `wiki/analysis/performance/ETF Performance Index.md` with the EWL coverage row, 2021-2025 common-window row and 2026-08-19 coverage bullet; append one workflow bullet to `log.md`.
- No entity hub, normalized financial table or `raw/funds/` file is planned.

### Local pre-save checklist

- PASS: canonical exchange-qualified identity, passive-index eligibility, tracked index, launch date, CUSIP, fees, USD NAV TR basis, semi-annual distribution cadence and current/rolling as-of dates are source-backed.
- PASS: 2016-2024 prospectus rows, 2025 factsheet row, 2021-2025 tracked-index rows, current NAV/YTD/AUM/holdings/sector/risk fields and cached S&P rows are separated by provenance and date.
- PASS: 2016-2025 and 2021-2025 cumulative/CAGR, up/down count, annual volatility, best/worst years and official fund-minus-index gaps recompute from displayed inputs; rolling 10-year `10.04%` remains an issuer field and no arithmetic difference is called alpha.
- PASS: Switzerland is the sole primary exposure region; the region page/count, canonical breadcrumb/tag, performance-index links, source batch section and log bullet are planned and resolve.
- PASS: complete proposed contents of every durable file were reviewed locally; no High/Medium finding remains and no confirmation-required WARNING remains.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official iShares identity, passive classification, 2016-2025 NAV evidence, current/rolling fields, benchmark reconciliation and scheduled-local pre-save checklist passed; Switzerland concentration, systematic fair-value and daily NAV drawdown/recovery gaps remain disclosed.

## PTEU — Pacer Trendpilot European Index ETF — unsupported ETF type

### Identity and type gate

- `workflow: check-etf-performance`; `execution_profile: scheduled-inline`; `entity_key: CBOE_BZX:PTEU`; `input_ticker: PTEU`.
- Official fund: `Pacer Trendpilot European Index ETF`, Cboe BZX-listed, CUSIP `69374H808`, ISIN `US69374H8088`, inception `2015-12-14`, total expenses `0.65%`.
- The fund is rules-based/passive in its mandate and seeks to track the Pacer Trendpilot European Index, but the tracked index is not equity-only: the official Pacer methodology can allocate 100% to the FTSE Eurozone Index, 50% to the FTSE Eurozone Index and 50% to 3-month U.S. Treasury bills, or 100% to 3-month U.S. Treasury bills.
- Type-gate result: `unsupported ETF type` because PTEU is a dynamic multi-asset/equity-and-T-bill allocation product, outside the supported passive index-tracking equity ETF scope. The official page's current `100% Equities` tracking field does not remove the documented T-bill states in the index methodology.

### Official source map

| Evidence | URL / path | Use and as-of |
|---|---|---|
| Pacer PTEU product page | https://www.paceretfs.com/products/pteu | official ticker, exchange, identity, inception, fee, current fund fields, strategy states, performance and holdings; page reviewed 2026-08-19, current performance capture through 2026-03-31 |
| Pacer PTEU factsheet | https://www.paceretfs.com/media/pteu.pdf | official objective, Pacer Trendpilot Index, FTSE Eurozone benchmark and T-bill strategy context; data as of 2026-03-31 |
| Pacer PTEU summary prospectus | https://docs.paceretfs.com/assets/pdfs/Pacer_PTEU_Summary.pdf | official passive/indexing language, index methodology and risks; prospectus dated 2025-08-31 |

### Scheduled-local review and write decision

- PASS: canonical identity, Cboe BZX listing, ticker, inception, official strategy documents and source URLs were directly reviewed inline.
- PASS: the unsupported-type classification is based on the index's explicit T-bill allocation states, not on a secondary performance label.
- PASS: no NAV performance page, annual equity-return table, S&P 500 comparison, region row, or ETF Performance Index row was written; no performance calculation was performed.
- PASS: the complete proposed source-batch section and blocked-card result metadata were reviewed locally; no High/Medium finding or confirmation-required WARNING remains.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

### trello_handoff

status: BLOCKED
scope: item
durable_write: not_completed
exhausted: true
confirmation: none
code: unsupported-etf-type
reason: Official Pacer methodology permits 100% equity, 50/50 equity-and-3-month-U.S.-T-bill, or 100% 3-month-U.S.-T-bill exposure, so PTEU is outside the supported equity-only ETF performance scope.

## FSZ — First Trust Switzerland AlphaDEX Fund

### Identity and classification

- `workflow: check-etf-performance`; `execution_profile: scheduled-inline`; `entity_key: NASDAQ:FSZ`; `input_ticker: FSZ`.
- Official fund: `First Trust Switzerland AlphaDEX Fund`, Nasdaq, CUSIP `33737J232`, ISIN `US33737J2327`, inception `2012-02-14`, total expense ratio `0.80%`.
- `management_mode: passive-index`; the Fund seeks to correspond generally to the price and yield of the equity `Nasdaq AlphaDEX Switzerland Index` before fees and expenses. The index is rules-based and rebalanced semi-annually.
- Primary region: Switzerland. Return basis: USD NAV Total Return, net of fund expenses, with distributions reinvested; market-price returns remain separate.

### Source map

| Evidence | URL / path | Use and as-of |
|---|---|---|
| First Trust FSZ fund page | https://www.ftportfolios.com/retail/etf/etfsummary.aspx?Ticker=FSZ | official identity, index objective, exchange, inception, current NAV/AUM/holdings/sectors, fees and month-end performance; current fields through 2026-08-03 and performance through 2026-06-30 |
| First Trust FSZ prospectus | https://www.ftportfolios.com/LoadContent/gradkqbz8r4y | official 2016-2025 calendar-year NAV rows, index transition, risks and annualized index comparison; periods ended 2025-12-31 |
| First Trust FSZ holdings | https://www.ftportfolios.com/Retail/etf/ETFholdings.aspx?Ticker=FSZ | official holdings and weights; as of 2026-07-31 |
| S&P 500 definition and cached workflow convention | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | USD Total Return common reference; cached annual rows for 2016-2025, dividends reinvested, reference as of 2025-12-31 |

### Raw observations

- Official FSZ NAV TR calendar rows for 2016-2025: 2016 `4.21%`, 2017 `31.26%`, 2018 `-15.11%`, 2019 `25.91%`, 2020 `14.50%`, 2021 `19.34%`, 2022 `-20.88%`, 2023 `22.07%`, 2024 `-1.25%`, 2025 `30.16%`.
- Official month-end performance as of 2026-06-30: FSZ NAV TR 3-month `4.35%`, YTD `3.46%`, 1-year `9.55%`, 3-year annualised `12.76%`, 5-year `6.78%`, 10-year `10.05%`, and since inception `9.46%`.
- Official Nasdaq AlphaDEX Switzerland Index comparison for the same date: 3-month `6.52%`, YTD `3.85%`, 1-year `11.05%`, 3-year annualised `13.50%`, 5-year `7.21%`, and 10-year `10.57%`.
- Official current snapshot as of 2026-08-03: NAV `US$82.02`, market price `US$82.01`, net assets `US$36.91m`, 40 holdings excluding cash, and 30-day median bid/ask spread `0.58%`; latest distribution `US$0.8084` as of 2026-08-05.
- Official exposure as of 2026-08-03: Industrials `30.02%`, Financials `19.72%`, Health Care `19.01%`, Consumer Discretionary `7.91%`, Consumer Staples `5.02%`; top holdings include Sulzer `4.75%`, Swiss Re `4.43%`, BKW `4.14%`, Flughafen Zurich `4.02%`, and Vontobel `3.93%`.
- Official 3-year standard deviation as of 2026-06-30: FSZ `14.51%`; Nasdaq Switzerland Index `15.94%`; MSCI Switzerland Index `16.00%`.
- Cached S&P 500 TR rows for 2016-2025: `11.96%`, `21.83%`, `-4.38%`, `31.49%`, `18.40%`, `28.71%`, `-18.11%`, `26.29%`, `25.02%`, and `17.88%`, respectively; USD, dividends reinvested.

### Calculations and reconciliation

- Formula: `cumulative = Π(1 + annual NAV TR) - 1`; `CAGR = (1 + cumulative)^(1 / years) - 1`; calculations use displayed rounded annual inputs.
- FSZ 2016-2025: cumulative `148.004717%` → `148.00%`; rounded-input CAGR `9.508037%` → `9.51%`; up/down `7/3`; best 2017 `+31.26%`; worst 2022 `-20.88%`; population annual-return volatility `17.602444%` → `17.60%`.
- FSZ 2021-2025: cumulative `48.148037%` → `48.15%`; rounded-input CAGR `8.178058%` → `8.18%`.
- Cached S&P 500 TR 2016-2025: cumulative `298.329111%` → `298.33%`; rounded-input CAGR `14.821761%` → `14.82%`. For 2021-2025: cumulative `96.169618%` → `96.17%`; CAGR `14.426430%` → `14.43%`.
- FSZ-minus-AlphaDEX index differences are approximately `-2.17 pp` for 3 months, `-0.39 pp` YTD, `-1.50 pp` 1-year, `-0.74 pp` 3-year annualised, `-0.43 pp` 5-year annualised and `-0.52 pp` 10-year annualised as of 2026-06-30. These are passive tracking observations, not alpha.
- The official index changed from Defined Switzerland Index to Nasdaq AlphaDEX Switzerland Index on 2015-07-14; the complete 2016-2025 table is post-change. No later official YTD than 2026-06-30 was present in the reviewed issuer capture.

### Source conflict and quality choice

- First Trust fund page and prospectus are the sources of truth for identity, passive classification, calendar rows, current/rolling fields, index comparison and fee. Secondary annual/YTD sources were not used.
- The S&P annual series reuses the permitted cached 2016-2025 convention; no fresh S&P search is needed. No arithmetic fund-minus-S&P difference is labelled alpha.
- Current NAV/holdings fields, issuer month-end performance, prospectus annual chart and risk snapshot have separate as-of dates; these are kept separate. Index-selection, rebalance, single-country, small/mid-cap, liquidity and daily NAV drawdown/recovery gaps remain disclosed.

### Planned durable paths and contents

- Create `wiki/analysis/performance/ETF_NASDAQ_FSZ Performance.md` with canonical `NASDAQ:FSZ`, USD NAV TR annual rows 2016-2025, 2021-2025 common-window metrics, issuer rolling/current fields, tracked-index comparison, risk notes, sources and Switzerland breadcrumb/tag.
- Update `wiki/analysis/comparisons/Switzerland ETF.md` with the FSZ navigation row/note; update `wiki/analysis/comparisons/ETF Region Index.md` Switzerland count from 2 to 3.
- Update `wiki/analysis/performance/ETF Performance Index.md` with the FSZ coverage row, 2021-2025 common-window row and 2026-08-19 coverage bullet; append one workflow bullet to `log.md`.
- No entity hub, normalized financial table or `raw/funds/` file is planned.

### Local pre-save checklist

- PASS: canonical exchange-qualified identity, ISIN/CUSIP, passive-index eligibility, tracked index, inception, fee, USD NAV TR basis, current/rolling fields and all as-of dates are source-backed.
- PASS: official 2016-2025 annual rows, 2021-2025 tracked-index fields, current NAV/AUM/holdings/sector/risk fields and cached S&P rows are separated by source and date; 2015 index transition is explicit.
- PASS: 2016-2025 and 2021-2025 cumulative/CAGR, up/down count, annual volatility, best/worst years and passive tracking gaps recompute from displayed inputs; no arithmetic difference is called alpha.
- PASS: Switzerland is the sole primary exposure region; region row/count, canonical breadcrumb/tag, performance-index links, source batch section and log bullet are planned and resolve.
- PASS: complete proposed contents of every durable file were reviewed locally; no High/Medium finding remains and no confirmation-required WARNING remains.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official First Trust identity, passive classification, 2016-2025 NAV rows, current/rolling fields, tracked-index reconciliation and scheduled-local pre-save checklist passed; AlphaDEX index transition, Swiss concentration and daily NAV drawdown/recovery gaps remain disclosed.

## EWQ — iShares MSCI France ETF

### Identity and classification

- `workflow: check-etf-performance`; `execution_profile: scheduled-inline`; `entity_key: NYSE_ARCA:EWQ`; `input_ticker: EWQ`.
- Official fund: `iShares MSCI France ETF`, listed on NYSE Arca, CUSIP `464286707`, inception `1996-03-12`, expense ratio `0.50%`, semi-annual distributions.
- `management_mode: passive-index`; tracked index `MSCI France Index (Net)`. The prospectus says the Fund uses an indexing approach and representative sampling to track large- and mid-cap French equities; it does not seek to beat the index.
- Primary region: `France`; return basis: USD NAV Total Return, net of fund expenses, with distributions reinvested; market-price returns remain separate.
- Type-gate result: supported passive equity ETF. The official product page and prospectus identify the fund as equity exposure rather than bond, commodity, currency, multi-asset, leveraged, inverse, covered-call, or derivative-heavy exposure.

### Source map

| Evidence | URL / path | Use and as-of |
|---|---|---|
| iShares EWQ product page | https://www.ishares.com/us/products/239648/ishares-msci-france-etf | official identity, NYSE Arca listing, tracked index, inception, current NAV, net assets, YTD, rolling returns, holdings, sectors, standard deviation and fees; current fields reviewed 2026-08-19, NAV/AUM 2026-08-18, holdings/sector 2026-08-17, risk fields 2026-07-31 |
| iShares EWQ factsheet | https://www.ishares.com/us/literature/fact-sheet/ewq-ishares-msci-france-etf-fund-fact-sheet-en-us.pdf | official 2021-2025 NAV and MSCI France Index rows, 2025 return, rolling fields, top holdings, sectors and fund characteristics; factsheet as of 2026-06-30 |
| iShares EWQ summary prospectus | https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-france-etf-8-31.pdf | official 2015-2024 calendar-year chart, passive/indexing method, tracked-index definition, fees and principal risks; prospectus dated 2025-12-30 |
| iShares EWQ annual shareholder report | https://www.ishares.com/us/literature/annual-report/ar-ewq-en.pdf | official reporting-period fund/index return context and portfolio concentration; period ended 2025-08-31 |
| S&P 500 definition and cached workflow convention | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ and the permitted `check-etf-performance` cache | USD Total Return common reference, dividends reinvested, annual rows 2016-2025 as of 2025-12-31; no new S&P search because the requested complete window is cached |

### Raw observations

- Official EWQ NAV TR calendar rows for 2016-2024 from the prospectus chart: 2016 `4.98%`, 2017 `28.84%`, 2018 `-12.69%`, 2019 `25.78%`, 2020 `3.89%`, 2021 `21.12%`, 2022 `-12.23%`, 2023 `21.69%`, and 2024 `-5.29%`.
- Official EWQ NAV TR 2025 factsheet row: `28.36%`; the same factsheet reports MSCI France Index (Net) `29.50%` for 2025 and official 2021-2025 rows of `20.59%`, `-12.67%`, `22.28%`, `-4.60%`, and `29.50%`.
- Official current snapshot: NAV `US$46.57`, net assets `US$335.28m`, and closing price `US$46.75` as of 2026-08-18; 55 holdings and sector exposures as of 2026-08-17; current NAV TR YTD `+7.03%` as of 2026-08-17; expense ratio `0.50%`.
- Official rolling performance as of 2026-06-30: fund 1Y `9.25%`, 3Y annualised `8.81%`, 5Y annualised `7.36%`, 10Y annualised `10.09%`, since inception `7.07%`; benchmark 1Y `10.45%`, 3Y `9.48%`, 5Y `7.52%`, 10Y `10.62%`.
- Official risk snapshot: 3-year standard deviation `14.45%` as of 2026-07-31; sector exposures as of 2026-08-17 include Industrials `32.88%`, Financials `14.00%`, Consumer Discretionary `10.87%`, Health Care `8.30%`, Consumer Staples `7.93%`, Energy `7.90%`, Materials `6.93%`, Utilities `3.41%`, Information Technology `3.20%`, Communication `2.77%`, Real Estate `1.33%`, and Cash/Derivatives `0.49%`.
- Official factsheet top ten as of 2026-06-30: Schneider Electric `8.31%`, TotalEnergies `7.12%`, LVMH `6.40%`, Safran `6.33%`, Airbus `6.14%`, Air Liquide `5.87%`, BNP Paribas `5.38%`, L'Oréal `4.90%`, Sanofi `4.35%`, and AXA `3.65%`; total `58.45%`.
- Cached S&P 500 TR rows for 2016-2025: `11.96%`, `21.83%`, `-4.38%`, `31.49%`, `18.40%`, `28.71%`, `-18.11%`, `26.29%`, `25.02%`, and `17.88%`, respectively; USD, dividends reinvested.

### Calculations and reconciliation

- Formula: `cumulative = Π(1 + annual NAV TR) - 1`; `CAGR = (1 + cumulative)^(1 / years) - 1`; calculations use displayed rounded annual inputs.
- EWQ 2016-2025: cumulative `142.688393%` → `142.69%`; rounded-input CAGR `9.270996%` → `9.27%`; up/down `7/3`; best 2017 `+28.84%`; worst 2018 `-12.69%`; population annual-return volatility `15.826242%` → `15.83%`.
- EWQ 2021-2025: cumulative `57.268736%` → `57.27%`; rounded-input CAGR `9.478409%` → `9.48%`.
- Cached S&P 500 TR 2016-2025: cumulative `298.329111%` → `298.33%`; rounded-input CAGR `14.821761%` → `14.82%`. For 2021-2025: cumulative `96.169618%` → `96.17%`; CAGR `14.426430%` → `14.43%`.
- EWQ-minus-MSCI-France Index annual differences for 2021-2025 are `+0.53`, `+0.44`, `-0.59`, `-0.69`, and `-1.14` percentage points. Rolling fund-minus-index observations are `-1.20 pp` for 1Y, `-0.67 pp` for 3Y annualised, `-0.16 pp` for 5Y annualised, and `-0.53 pp` for 10Y annualised as of 2026-06-30. These are passive tracking observations, not alpha.
- The issuer rolling 10-year NAV TR `10.09%` is kept separate from the rounded-input 2016-2025 calendar CAGR `9.27%`; no arithmetic substitution is made. Current EWQ YTD `7.03%` as of 2026-08-17 is not mixed with the older 2026-06-30 benchmark window.

### Source conflict and quality choice

- iShares product page, factsheet and summary prospectus are the sources of truth. The annual table combines the official prospectus chart through 2024 with the official factsheet 2025 row; no values are inferred between them.
- The annual shareholder report covers a fiscal reporting period ending 2025-08-31 and is used for context, not substituted for calendar-year 2025 NAV TR. The official factsheet row is used for the complete calendar-year table.
- The S&P annual comparison reuses the permitted cached 2016-2025 convention. No fresh S&P search is required for this complete cached window, and no arithmetic fund-minus-S&P difference is labelled alpha.
- Current NAV/AUM/holdings/sector fields, factsheet rolling performance, prospectus calendar chart and risk language have different as-of dates; they remain separated. France concentration, representative-sampling/systematic-fair-value timing, currency/foreign-market risk and the daily NAV drawdown/recovery gap are disclosed.

### Planned durable paths and contents

- Create `wiki/analysis/performance/ETF_NYSE_ARCA_EWQ Performance.md` with canonical `NYSE Arca:EWQ`, USD NAV TR annual rows 2016-2025, 2021-2025 common-window metrics, issuer rolling/current fields, official MSCI France Index comparison, risk notes, sources and France breadcrumb/tag.
- Create `wiki/analysis/comparisons/France ETF.md` as the static primary-region navigation page with the EWQ row, links to `[[ETF Region Index]]` and `[[ETF Performance Index]]`, and no copied annual table.
- Update `wiki/analysis/comparisons/ETF Region Index.md` with France count `1` and `[[France ETF]]`; update the Browse by region links in `wiki/analysis/performance/ETF Performance Index.md` with `[[France ETF]]`.
- Update `wiki/analysis/performance/ETF Performance Index.md` with the EWQ coverage row, 2021-2025 common-window row and the 2026-08-19 coverage bullet; append one workflow bullet to `log.md`.
- No entity hub, normalized financial table or `raw/funds/` file is planned.

### Local pre-save checklist

- PASS: canonical exchange-qualified identity, CUSIP, passive-index eligibility, tracked index, inception, fee, USD NAV TR basis, semi-annual distribution cadence and current/rolling as-of dates are source-backed.
- PASS: 2016-2024 prospectus rows, 2025 factsheet row, 2021-2025 tracked-index rows, current NAV/YTD/AUM/holdings/sector/risk fields and cached S&P rows are separated by provenance and date.
- PASS: 2016-2025 and 2021-2025 cumulative/CAGR, up/down count, annual volatility, best/worst years and official fund-minus-index gaps recompute from displayed inputs; rolling 10-year `10.09%` remains an issuer field and no arithmetic difference is called alpha.
- PASS: France is the sole primary exposure region; the new region page/count, canonical breadcrumb/tag, performance-index links, source batch section and log bullet are planned and resolve.
- PASS: complete proposed contents of every durable file were reviewed locally; no High/Medium finding remains and no confirmation-required WARNING remains.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official iShares identity, passive classification, 2016-2025 NAV evidence, current/rolling fields, MSCI France tracking reconciliation and scheduled-local pre-save checklist passed; France concentration, systematic fair-value timing and daily NAV drawdown/recovery gaps remain disclosed.

## TUR — iShares MSCI Turkey ETF

- `workflow: check-etf-performance`; `execution_profile: scheduled-inline`; `entity_key: NASDAQ:TUR`; `input_ticker: TUR`.
- Official fund: `iShares MSCI Turkey ETF`, NASDAQ, CUSIP `464286715`, inception `2008-03-26`, expense ratio `0.59%`, semi-annual distributions.
- `management_mode: passive-index`; the fund seeks to track the `MSCI Turkey IMI 25/50 Index (USD) (Net)`, a broad-based index of Turkish equities. The current index began on 2019-05-29; prior rows use the official spliced historical benchmark.
- Primary region: `Turkey`; return basis: USD `NAV Total Return`, with dividends/capital gains reinvested and fund expenses deducted; market-price return remains separate.

### Official source map

| Evidence | URL / path | Use and as-of |
|---|---|---|
| iShares TUR U.S. product page | https://www.ishares.com/us/products/239689/ishares-msci-turkey-etf | official identity, NASDAQ listing, benchmark, current NAV/price, YTD, rolling performance, holdings, sectors, distributions and fees; current page reviewed 2026-08-19, NAV/net assets 2026-08-18, price/holdings 2026-08-17, risk fields 2026-07-31 |
| iShares TUR fact sheet | https://www.ishares.com/us/literature/fact-sheet/tur-ishares-msci-turkey-etf-fund-fact-sheet-en-us.pdf | official 2021-2025 NAV/index rows, return definition, benchmark, fee and fund characteristics; factsheet as of 2026-06-30 |
| iShares TUR summary prospectus | https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-turkey-etf-8-31.pdf | official 2016-2020 calendar rows, passive objective, index splice, risks, and best/worst quarter; prospectus dated 2025-12-30 |
| iShares TUR international calendar page | https://www.ishares.com/ch/professionals/en/products/239689/ishares-msci-turkey-etf?switchLocale=Y | official USD fund/benchmark calendar cross-check for 2016-2025; page capture through 2026-07-30 |
| S&P 500 definition and cached workflow convention | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ and the permitted `check-etf-performance` cache | USD Total Return common reference, dividends reinvested, annual rows 2016-2025, reference as-of 2025-12-31 |
| Current S&P 500 YTD secondary snapshot | https://www.slickcharts.com/sp500/returns/ytd | secondary S&P 500 Total Return YTD `13.17%` as of 2026-08-18 |

### Raw observations

- Official product page current fields: NAV `US$39.58` and net assets `US$221.661M` as of 2026-08-18; closing price `US$39.43`, holdings `73`, and sector data as of 2026-08-17; official NAV TR YTD `16.38%` as of 2026-08-17. Product-page risk fields as of 2026-07-31 include 3-year standard deviation `25.11%`, equity beta `0.35`, 12m trailing yield `2.21%`, and 30-day SEC yield `1.44%`.
- Official fund NAV TR annual rows 2016-2020 from the summary-prospectus chart: 2016 `-8.28%`, 2017 `37.45%`, 2018 `-41.42%`, 2019 `13.94%`, 2020 `-0.74%`. Official fact-sheet rows for 2021-2025: `-27.51%`, `106.42%`, `-9.16%`, `13.70%`, `-2.91%`.
- Official benchmark rows: 2016-2020 international page rounded values `-8.2%`, `37.8%`, `-41.3%`, `14.5%`, `-0.7%`; 2021-2025 factsheet values `-27.68%`, `107.26%`, `-8.80%`, `14.82%`, `-2.57%`.
- Official rolling performance as of 2026-06-30: NAV TR 1Y `23.05%`, 3Y annualised `13.81%`, 5Y `16.21%`, 10Y `2.58%`, inception `1.08%`; benchmark 1Y `23.19%`, 3Y `14.47%`, 5Y `16.58%`, 10Y `2.86%`, inception `1.40%`. The same page reports 10-year cumulative NAV TR `28.97%` and YTD `14.54%` at that month-end.
- Official sector snapshot as of 2026-08-17: Industrials `27.62%`, Financials `16.56%`, Consumer Staples `13.18%`, Materials `11.70%`, Energy `9.05%`, Real Estate `6.49%`; holdings and allocations are subject to change.
- Official summary prospectus reports best quarter `+68.38%` in Q4 2022 and worst quarter `-29.37%` in Q1 2020. Daily NAV maximum drawdown and recovery date were not disclosed in the reviewed sources.
- Latest four official cash distributions: `US$0.479168` (record/ex 2026-06-15, payable 2026-06-18), `US$0.359292` (2025-12-16/2025-12-19), `US$0.466192` (2025-06-16/2025-06-20), and `US$0.146027` (2024-12-17/2024-12-20). Sum `US$1.450679`; average `US$0.362670` per round; approximate per-round yield `0.92%` against the verified closing price `US$39.43`.
- Cached S&P 500 TR rows for 2016-2025 are USD `11.96%`, `21.83%`, `-4.38%`, `31.49%`, `18.40%`, `28.71%`, `-18.11%`, `26.29%`, `25.02%`, and `17.88%`; current secondary YTD is `13.17%` as of 2026-08-18.

### Calculations and reconciliation

- Formula: `cumulative = Π(1 + annual NAV TR) - 1`; `CAGR = (1 + cumulative)^(1 / years) - 1`; calculations use the displayed official annual inputs.
- TUR 2016-2025: cumulative `25.328721%` → `25.33%`; rounded-input CAGR `2.283378%` → `2.28%`; up/down `4/6`; best 2022 `+106.42%`; least positive 2024 `+13.70%`; worst 2018 `-41.42%`; least-bad down year 2020 `-0.74%`; population annual-return standard deviation `38.832418%` → `38.83%`.
- TUR 2021-2025: cumulative `50.052061%` → `50.05%`; rounded-input CAGR `8.454704%` → `8.45%`. The tracked-index rows compound to `52.925178%` / `8.866886%`; the approximate passive tracking gap is `-0.41 pp` CAGR.
- Cached S&P 500 TR 2016-2025: cumulative `298.329111%` → `298.33%`; rounded-input CAGR `14.821761%` → `14.82%`. The 2021-2025 subset is `96.169618%` / `14.426430%` → `96.17%` / `14.43%`. These are common-reference comparisons, not alpha.
- Official rolling 10-year NAV TR is kept separate from the complete-calendar calculation: `28.97%` cumulative / `2.58%` issuer CAGR as of 2026-06-30 versus 2016-2025 rounded-input `25.33%` / `2.28%`.

### Source conflict and quality choice

- iShares U.S. product page, factsheet, summary prospectus and official international calendar page are the sources of truth. The current U.S. product page is used for the latest YTD/NAV/price; older locale snapshots are not substituted for current U.S. fields.
- 2016-2020 fund rows use the exact official prospectus chart; the international page's one-decimal rows provide a cross-check and are used for the displayed historical benchmark rows where the U.S. factsheet does not expose those years. 2021-2025 exact fund/index rows use the factsheet.
- The S&P annual series reuses the permitted cached 2016-2025 USD convention. Current S&P YTD is a separate secondary snapshot dated one day after TUR's latest NAV TR YTD; no cross-date arithmetic excess return is claimed.
- Turkey single-country/emerging-market, currency, sector concentration, systematic fair-value timing and daily NAV drawdown/recovery gaps remain disclosed.

### Planned durable paths and contents

- Create `wiki/analysis/performance/ETF_NASDAQ_TUR Performance.md` with canonical `NASDAQ:TUR`, USD NAV TR annual rows 2016-2025, official MSCI Turkey comparison, rolling 10-year field, current YTD/NAV/price/distribution dates, risk notes, sources, `geography/Turkey` tag and breadcrumb `[[ETF Region Index]] → [[Turkey ETF]] → [[ETF Performance Index]]`.
- Create `wiki/analysis/comparisons/Turkey ETF.md` as the static primary-region navigation page with the TUR row and links to `[[ETF Region Index]]` and `[[ETF Performance Index]]`; no annual table is duplicated there.
- Update `wiki/analysis/comparisons/ETF Region Index.md` with Turkey count `1` and `[[Turkey ETF]]`, add the Turkey link to the `ETF Performance Index` Browse by region list, add the TUR row and common-window row to `ETF Performance Index.md`, and append one `log.md` workflow bullet.
- No entity hub, normalized financial table or `raw/funds/` file is planned.

### Local pre-save checklist

- PASS: canonical exchange-qualified identity, passive equity eligibility, tracked index, inception, fee, USD NAV TR basis, semi-annual distributions, current/rolling fields and all as-of dates are source-backed.
- PASS: 2016-2020 exact prospectus rows, 2016-2020 benchmark cross-check, 2021-2025 factsheet rows, current NAV/YTD/price/holdings/sector/risk fields and cached/secondary S&P references are separated by provenance and date.
- PASS: calendar cumulative/CAGR, 2021-2025 CAGR, up/down count, annual volatility, best/worst years, distribution average and passive tracking gap recompute from displayed inputs; issuer rolling 10-year field remains separate and no arithmetic difference is called alpha.
- PASS: Turkey is the sole primary exposure region; region page/count, canonical breadcrumb/tag, performance-index links, source-batch section and log bullet are planned and resolve. Daily NAV drawdown/recovery is explicitly retained as a gap.
- PASS: complete proposed contents of every durable file were reviewed locally; no High/Medium finding remains and no confirmation-required WARNING remains.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official iShares identity, passive classification, 2016-2025 NAV/index evidence, rolling 10-year and current YTD fields, Turkey navigation and the scheduled-local pre-save checklist passed; country, currency, sector and daily NAV drawdown/recovery gaps remain disclosed.

## FESM — Fidelity Enhanced Small Cap Core ETF

- `workflow: check-etf-performance`; `execution_profile: scheduled-inline`; `entity_key: NYSE Arca:FESM`; `input_ticker: FESM`.
- Official fund identity: `Fidelity Enhanced Small Cap Core ETF` (formerly Fidelity Enhanced Small Cap ETF), listed on `NYSE Arca`; CUSIP `31609A206`; strategy/predecessor inception `2007-12-20`; ETF first listed `2023-11-20`; name change effective about `2026-05-11`.
- `management_mode: active-equity-long-only`; `active_process: systematic-quantitative`; `management_benchmark: Russell 2000`; `track_record: established-strategy-with-predecessor-history`.
- Return basis: USD `NAV Total Return`, including changes in share value and reinvested dividends/capital gains, after fund expenses; market-price return is retained separately. Rows through 2023-11-17 are predecessor mutual-fund history and are not relabelled as pure live ETF history.

### Official source map

| Evidence | URL / path | Use and as-of |
|---|---|---|
| Fidelity FESM factsheet | https://institutional.fidelity.com/app/proxy/content?literatureURL=%2F9911747.PDF | official strategy, active classification, Russell 2000 policy, 2016-2025 NAV/market/benchmark rows, rolling returns, fee, assets, holdings, turnover, beta, standard deviation and yield; factsheet as of 2026-06-30 |
| Fidelity FESM quote page | https://digital.fidelity.com/prgw/digital/research/quote/dashboard/summary?symbol=FESM | current identity, previous close, NAV, shares outstanding and exchange; page capture 2026-08-19, page does not expose an explicit quote timestamp |
| Fidelity portfolio holdings | https://research2.fidelity.com/fidelity/screeners/etf/etfholdings.asp?sortBy=Symbol&sortDir=desc&symbol=FESM&view=Holdings | official basket holdings and count; snapshot as of 2026-06-30 |
| Fidelity portfolio manager Q&A | https://institutional.fidelity.com/app/proxy/content?literatureURL=%2FRD_QAA_7545.PDF | active process, predecessor-history caveat, benchmark comparison and manager commentary; periods ending 2025-12-31 / quarter ending 2026-03-31 |
| SEC rename supplement | https://www.sec.gov/Archives/edgar/data/945908/000094590826000151/filing12065.htm | official name change to Fidelity Enhanced Small Cap Core ETF effective about 2026-05-11; filing dated 2026-04-29 |
| SEC prospectus | https://www.sec.gov/Archives/edgar/data/945908/000094590825000511/filing9117.htm | official objective, Russell 2000 policy and predecessor-inclusive performance context; filing dated 2025 |
| S&P 500 definition and cached workflow convention | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ and permitted `check-etf-performance` cache | USD Total Return common reference, dividends reinvested, annual rows 2016-2025, reference as-of 2025-12-31 |

### Candidate claims and raw observations

- Official factsheet fields as of 2026-06-30: expense ratio gross/net `0.28%/0.28%`; portfolio assets `$5,784.9M`; holdings `786`; turnover `41%`; 3-year beta `1.02`; 3-year standard deviation `20.52%`; 30-day SEC yield `0.52%`.
- Official NAV TR calendar rows 2016-2025: `22.84%`, `7.22%`, `-13.04%`, `23.65%`, `18.53%`, `20.54%`, `-18.28%`, `21.04%`, `16.48%`, `17.70%`.
- Official market-price calendar rows 2016-2025: `22.84%`, `7.22%`, `-13.04%`, `23.65%`, `18.53%`, `20.54%`, `-18.28%`, `21.40%`, `16.22%`, `17.88%`.
- Official Russell 2000 benchmark rows 2016-2025: `21.31%`, `14.65%`, `-11.01%`, `25.52%`, `19.96%`, `14.82%`, `-20.44%`, `16.93%`, `11.54%`, `12.81%`.
- Official rolling NAV TR as of 2026-06-30: 3-month `27.18%`, YTD `28.42%`, 1-year `52.23%`, 3-year annualized `24.57%`, 5-year annualized `11.69%`, 10-year annualized `13.28%`; market-price YTD `28.45%`; Russell 2000 YTD `22.57%`, 1-year `40.78%`, 3-year `18.60%`, 5-year `6.98%`, 10-year `11.62%`.
- Fidelity quote snapshot captured 2026-08-19: previous close `US$48.11`, NAV `US$48.095514`, shares outstanding `133,121,356`, primary exchange `NYSE Arca`. The page does not expose a dated current total-return YTD; latest official YTD remains 2026-06-30.
- Fidelity holdings page reports `789` basket holdings as of 2026-06-30; the factsheet reports `786` total holdings on the same date. The difference is retained as a source-definition conflict rather than reconciled by inference.
- Cached S&P 500 TR annual rows 2016-2025: `11.96%`, `21.83%`, `-4.38%`, `31.49%`, `18.40%`, `28.71%`, `-18.11%`, `26.29%`, `25.02%`, `17.88%`; USD, dividends reinvested.

### Calculations and reconciliation

- Formula: `cumulative = Π(1 + annual NAV TR) - 1`; `CAGR = (1 + cumulative)^(1 / years) - 1`; calculations use displayed rounded annual inputs.
- FESM 2016-2025: cumulative `174.393508%` → `174.39%`; rounded-input CAGR `10.620950%` → `10.62%`; up/down `8/2`; best 2019 `+23.65%`; least positive 2017 `+7.22%`; worst 2022 `-18.28%`; least-bad down year 2018 `-13.04%`; population annual-return standard deviation `14.383007%` → `14.38%`.
- FESM 2021-2025: cumulative `63.461803%` → `63.46%`; rounded-input CAGR `10.327368%` → `10.33%`. Russell 2000 compounds to `34.405334%` / `6.092162%` → `34.41%` / `6.09%`.
- Management-benchmark evidence: annual FESM-minus-Russell differences are positive in `6/10` years (2016, 2021, 2022, 2023, 2024 and 2025). Relative wealth is `15.889395%` → `15.89%`; rounded-input CAGR difference is approximately `+1.00 pp`. These are benchmark-relative observations, not alpha.
- Cached S&P 500 TR 2016-2025: cumulative `298.329111%` → `298.33%`; rounded-input CAGR `14.821761%` → `14.82%`; 2021-2025 cumulative `96.169618%` → `96.17%`; CAGR `14.426430%` → `14.43%`. This is a common reference, not FESM's management benchmark.

### Source conflict and quality choice

- Fidelity's June 2026 factsheet is the primary source for annual and rolling total-return fields, fees and risk fields. The quote page is used only for the current market snapshot because it does not provide a dated current YTD total return.
- FESM's 2016-2023 rows include the predecessor mutual fund. The current ETF structure has different expenses and market-price mechanics after conversion, so the long window is labelled strategy-plus-predecessor history.
- The same-date factsheet and holdings pages report `786` versus `789` holdings because they use different holdings definitions; both values are preserved with their source labels.
- Russell 2000 is the strategy-aligned management benchmark. S&P 500 TR is kept as a common reference only. No arithmetic return gap is labelled alpha.
- Official daily NAV history sufficient to calculate max drawdown and recovery date was not found; this gap remains disclosed.

### Planned durable paths and contents

- Update `wiki/analysis/performance/ETF_NYSE_ARCA_FESM Performance.md` with the current source batch, 2026-08-19 quote snapshot, official 2016-2025/rolling/YTD fields, active-management evidence, corrected `+15.89%` cumulative relative wealth, risk fields, sources and disclosed gaps.
- Update `wiki/analysis/comparisons/USA ETF.md` timestamp to 2026-08-19; the existing FESM row and performance link already resolve, so no duplicate region page or row is planned.
- Append one workflow bullet to `log.md`.
- `ETF Performance Index.md` and `ETF Region Index.md` already contain the FESM coverage/link and were not planned for content changes in this item.
- No entity hub, normalized financial table or `raw/funds/` file is planned.

### Local pre-save checklist

- PASS: canonical exchange-qualified identity, CUSIP, active equity eligibility, Russell 2000 management benchmark, predecessor/ETF dates, fee, USD NAV TR basis and current quote fields are source-backed.
- PASS: official annual NAV/market/benchmark rows, rolling fields, current quote, holdings, risk fields and cached S&P rows are separated by provenance and as-of date; current official YTD is explicitly limited to 2026-06-30.
- PASS: 2016-2025 and 2021-2025 cumulative/CAGR, up/down count, annual volatility, best/worst years, active hit rate and relative-wealth calculation recompute from displayed inputs; no arithmetic difference is called alpha.
- PASS: USA is the sole primary exposure region; the existing region navigation, canonical breadcrumb/tag, performance-index links, source-batch section and log bullet resolve. Predecessor-history, holdings-definition, current-YTD and daily NAV drawdown/recovery gaps remain disclosed.
- PASS: complete proposed contents of every durable file were reviewed locally; no High/Medium finding remains and no confirmation-required WARNING remains.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official Fidelity identity, active systematic classification, Russell 2000 benchmark, 2016-2025 NAV/benchmark evidence, rolling fields, current quote snapshot and the scheduled-local pre-save checklist passed; predecessor-history, holdings-definition, current-YTD and daily NAV drawdown/recovery gaps remain disclosed.

## BCYIF — iShares Core FTSE 100 UCITS ETF GBP (Distributing) / LSE:ISF

- `workflow: check-etf-performance`; `execution_profile: scheduled-inline`; `entity_key: LSE:ISF`; `input_ticker: BCYIF`.
- Input mapping: `BCYIF` is an OTC alias for the official GBP distributing share class identified by ISIN `IE0005042456`; the official London Stock Exchange line is `ISF` (`LSE:ISF`). The durable page keeps the alias in frontmatter and uses `LSE:ISF` as the exchange-qualified identity.
- Official fund: `iShares Core FTSE 100 UCITS ETF`, passive physical replicated equity UCITS ETF, Ireland domicile, share-class launch `2000-04-27`, benchmark `FTSE 100 Index`, quarterly distributions, TER `0.07%`.
- `management_mode: passive-index`; `return_basis: GBP share-class NAV Total Return`, with gross income reinvested where applicable and fund expenses reflected in NAV; S&P 500 Total Return is a separate USD common reference only.
- Primary region: `United Kingdom`; supported type: passive index-tracking equity ETF.

### Official source map

| Evidence | URL / path | Use and as-of |
|---|---|---|
| iShares ISF product page | https://www.ishares.com/uk/individual/en/products/251795/ishares-core-ftse-100-ucits-etf | official identity/ISIN/listing, current NAV/YTD, assets, holdings, sector, benchmark and risk fields; NAV/net assets 2026-08-18, NAV TR YTD/holdings/sectors 2026-08-17 |
| iShares ISF July factsheet | https://www.blackrock.com/uk/literature/fact-sheet/isf-ishares-core-ftse-100-ucits-etf-fund-fact-sheet-en-gb.pdf | official 2016-2025 NAV/benchmark rows, rolling performance, fee, structure, holdings and risk fields; performance and portfolio as of 2026-07-31, other data as of 2026-08-07 |
| iShares GBP distributing KIID | https://www.ishares.com/gls-download/literature/kiid/ucits_kiid-ishares-core-ftse-100-ucits-etf-gbp-dist-gb-ie0005042456-en.pdf | official passive objective, charge, GBP annual performance cross-check, benchmark and share-class disclosures; historical performance through 2025-12-31 |
| BCYIF OTC alias cross-check | https://stockanalysis.com/quote/otc/BCYIF/ | secondary OTC symbol/name cross-check; the official ISIN and LSE listing remain the source of truth |
| S&P 500 definition and cached workflow convention | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ and permitted `check-etf-performance` cache | USD Total Return common reference, dividends reinvested, annual rows 2016-2025, reference as-of 2025-12-31 |

### Candidate claims and raw observations

- Official GBP NAV TR calendar rows 2016-2025: `19.03%`, `11.94%`, `-8.83%`, `17.18%`, `-11.64%`, `18.31%`, `4.62%`, `7.80%`, `9.50%`, `25.66%`.
- Official FTSE 100 benchmark rows 2016-2025: `19.04%`, `11.91%`, `-8.77%`, `17.28%`, `-11.58%`, `18.40%`, `4.67%`, `7.90%`, `9.63%`, `25.78%`.
- The benchmark changed from a total-return series to a net-of-tax total-return series on 2019-07-17; historic benchmark performance was simulated to reflect that change.
- Official July factsheet rolling fields as of 2026-07-31: share-class 1-month `3.61%`, 3-month `5.38%`, 6-month/YTD `11.42%`, 1-year `22.68%`, 3-year annualized `16.11%`, 5-year annualized `13.02%`, since inception annualized `5.60%`; benchmark `3.62%`, `5.38%`, `11.47%`, `22.78%`, `16.23%`, `13.12%`, `5.88%`.
- Latest official product-page fields: NAV `GBP 10.48` and share-class net assets `GBP 16,350,956,822` as of 2026-08-18; NAV TR YTD `10.51%` as of 2026-08-17; 100 holdings and sector fields as of 2026-08-17; 3-year standard deviation `9.57%` and beta `1.000` as of 2026-07-31; trailing distribution yield `2.91%` as of 2026-08-17.
- Latest product-page sector snapshot: Financials `28.72%`, Industrials `14.15%`, Consumer Staples `13.21%`, Health Care `11.33%`, Energy `10.62%`, Materials `7.91%`, Utilities `4.40%`, Consumer Discretionary `4.39%`, Communication `1.97%`, Real Estate `1.19%`.
- Cached S&P 500 TR annual rows 2016-2025: USD `11.96%`, `21.83%`, `-4.38%`, `31.49%`, `18.40%`, `28.71%`, `-18.11%`, `26.29%`, `25.02%`, `17.88%`; no GBP/USD cross-currency performance gap is claimed.

### Calculations and reconciliation

- Formula: `cumulative = Π(1 + annual NAV TR) - 1`; `CAGR = (1 + cumulative)^(1 / years) - 1`; calculations use displayed official annual inputs.
- ISF 2016-2025: cumulative `130.923960%` → `130.92%`; rounded-input CAGR `8.729377%` → `8.73%`; up/down `8/2`; best 2025 `+25.66%`; least positive 2022 `+4.62%`; worst 2020 `-11.64%`; least-bad down year 2018 `-8.83%`; population annual-return standard deviation `11.418875%` → `11.42%`.
- ISF 2021-2025: cumulative `83.597222%` → `83.60%`; rounded-input CAGR `12.920611%` → `12.92%`. FTSE 100 compounds to `84.389580%` / `13.017911%` → `84.39%` / `13.02%`.
- Passive tracking evidence: 2016-2025 fund-versus-index relative wealth is `-0.629228%` → `-0.63%`; rounded-input CAGR gap is approximately `-0.07 pp`. For 2021-2025 the rounded-input CAGR gap is approximately `-0.10 pp`; rolling gaps from the July factsheet are approximately `-0.10 pp` (1Y), `-0.12 pp` (3Y annualized), `-0.10 pp` (5Y annualized) and `-0.28 pp` (since inception). These are tracking observations, not alpha.
- Cached S&P 500 TR 2016-2025: cumulative `298.329111%` → `298.33%`; rounded-input CAGR `14.821761%` → `14.82%`. It remains a USD common reference and is not used for direct same-currency ranking against GBP returns.

### Source conflict and quality choice

- The official iShares product page is the source of truth for the latest current fields: its current capture reports YTD `10.51%` as of 2026-08-17, while the July factsheet reports the earlier `11.42%` as of 2026-07-31. Both are preserved with their as-of dates; the newer product-page field is used in the durable current-YTD slot.
- Annual rows and rolling returns use the official July factsheet, cross-checked against the official KIID. No USD listing or OTC price is substituted for the GBP share-class NAV return.
- BCYIF-to-ISF mapping is retained as a secondary OTC alias cross-check; official ISIN/listing data determine the canonical `LSE:ISF` identity.
- UK/country, GBP share-class/FX, financials and energy concentration, quarterly distribution and daily NAV drawdown/recovery gaps remain disclosed.

### Planned durable paths and contents

- Refresh `wiki/analysis/performance/ETF_LSE_ISF Performance.md` with `LSE:ISF`, the `BCYIF` alias, latest product-page current fields, July rolling/annual fields, GBP basis, tracking reconciliation, sources and disclosed gaps.
- Update `wiki/analysis/comparisons/United Kingdom ETF.md` ISF row and explanatory note to current product-page YTD `10.51%` as of 2026-08-17, while retaining the July factsheet `11.42%` observation.
- Update `wiki/analysis/performance/ETF Performance Index.md` ISF current-YTD row/note/bullet; the existing UK region page, breadcrumbs and links already resolve, so no duplicate region page is planned.
- Append one workflow bullet to `log.md`.
- No entity hub, normalized financial table or `raw/funds/` file is planned.

### Local pre-save checklist

- PASS: canonical ISIN/listing identity, BCYIF alias mapping, passive equity eligibility, FTSE 100 benchmark, GBP share class, launch date, fee, distribution method and NAV TR basis are source-backed.
- PASS: official current product-page fields, July factsheet annual/rolling fields, KIID cross-check, benchmark-change caveat and cached USD S&P reference are separated by provenance and as-of date.
- PASS: 2016-2025 and 2021-2025 cumulative/CAGR, up/down count, annual volatility, best/worst years and passive tracking gaps recompute from displayed inputs; no arithmetic difference is called alpha.
- PASS: United Kingdom is the sole primary exposure region; existing region navigation, canonical breadcrumb/tag, performance-index links, source-batch section and log bullet resolve. Current-YTD source conflict and daily NAV drawdown/recovery gap remain disclosed.
- PASS: complete proposed contents of every durable file were reviewed locally; no High/Medium finding remains and no confirmation-required WARNING remains.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official iShares identity and BCYIF-to-LSE:ISF mapping, passive classification, GBP 2016-2025 NAV/benchmark evidence, rolling fields, latest current YTD/NAV fields and the scheduled-local pre-save checklist passed; current-YTD date reconciliation, GBP/FX, UK concentration and daily NAV drawdown/recovery gaps remain disclosed.
