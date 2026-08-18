---
type: etf-performance-source-batch
date: 2026-08-18
workflow: check-etf-performance
execution_profile: scheduled-inline
verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS
---

# ETF Performance Source Batch — 2026-08-18

ชุดข้อมูลนี้เป็น evidence packet และ source ledger ของ workflow `check-etf-performance` แบบ `scheduled-inline`. การตรวจ pre-save ทำใน top-level context เดิมครบทุกข้อ และไม่มีการ dispatch worker, reviewer หรือ `source_verifier`.

## AVDV — Avantis International Small Cap Value ETF

### Identity and classification

- `entity_key: NYSE Arca:AVDV`; ticker `AVDV`; canonical exchange `NYSE Arca`; inception `2019-09-24`.
- `management_mode: active-equity-long-only`; `active_process: fundamental-active`.
- `management_benchmark: MSCI World ex USA Small Cap Index (Net Dividends)`.
- `track_record: established`; `management_evidence: positive return-only`; `risk_evidence: not-verified`.
- The 2026-08-17 source batch recorded AVDV as unsupported under the older passive-only route. The current active long-only support path was applied using the card retry reason and current skill contract; the old record remains unchanged.

### Source map

| Source | URL/path | Use |
|---|---|---|
| Issuer product page | https://www.avantisinvestors.com/avantis-investments/avantis-international-small-cap-value-etf/ | current YTD NAV/market-price TR, fee, active strategy, NAV/price snapshot |
| Issuer factsheet | https://res.avantisinvestors.com/docs/avantis-international-small-cap-value-avdv-etf-fact-sheet.pdf | official rolling returns, benchmark, inception, exchange, AUM, team, risk |
| SEC summary prospectus | https://www.sec.gov/Archives/edgar/data/1710607/000171060725000402/acetftavdv497k.htm | canonical exchange, fee, strategy, active disclosure, turnover |
| Secondary total-return series | https://totalrealreturns.com/n/AVDV%2CAVUV%2CFIVA%2CAVNV%2CVXUS | annual proxy and observed drawdown window |
| Secondary performance cross-check | https://www.schwab.wallst.com/Prospect/Research/etfs/performance.asp?symbol=avdv | current price and rolling NAV/market-price cross-check |
| Cached benchmark convention | workflow cache | S&P 500 Total Return calendar rows 2016-2025 |

### Raw observations

- Official factsheet as of 2026-06-30: NAV TR `3Y 26.06%`, `5Y 13.81%`, `ITD 14.76%`; management benchmark `3Y 16.51%`, `5Y 6.03%`, `ITD 9.35%`.
- Official product page as of 2026-07-31: NAV TR YTD `13.11%`; market-price TR YTD `12.97%`.
- Official product page snapshot as of 2026-08-14: NAV `110.80`; market price `110.86`.
- Official fee `0.36%`; AUM `US$19.2B` as of 2026-06-30; quarterly distributions; latest SEC fiscal-year turnover `4%`.
- Secondary annual dividend-reinvested proxy: 2019 `+12.05%` partial, 2020 `+5.01%`, 2021 `+15.80%`, 2022 `-11.46%`, 2023 `+16.93%`, 2024 `+8.67%`, 2025 `+49.37%`.
- Secondary proxy observed drawdown window: `-14.17%` from 2025-03-19 to 2025-04-07; later `-5.35%` from 2026-05-26 peak as of 2026-07-09. Official daily NAV drawdown/recovery not verified.
- S&P 500 Total Return cached annual rows for 2016-2025 are USD total-return rows as of 2025-12-31. No current S&P YTD comparison was used because the available current dates did not match AVDV's official 2026-07-31 YTD date.

### Calculations and reconciliation

- Official 5Y management-benchmark Excess CAGR: `13.81% - 6.03% = +7.78 pp`; this is return-only evidence, not alpha.
- Complete 2020-2025 secondary proxy: `(1.0501 × 1.1580 × 0.8854 × 1.1693 × 1.0867 × 1.4937) - 1 = 104.35%`; rounded-input CAGR `104.35%` over six years = `12.65%`; population standard deviation `18.35%`.
- Complete 2021-2025 secondary proxy: cumulative `94.60%`, rounded-input CAGR `14.24%`; cached S&P 500 TR comparison cumulative `96.17%`, CAGR `14.43%`.
- 10-year CAGR is not applicable because inception is 2019-09-24.
- Annual calendar rows are secondary proxy rows because the SEC annual chart was image-based in the reviewed capture; official rolling returns remain the primary performance evidence.

### Local pre-save checklist

- PASS: ETF identity, exchange, active long-only classification, benchmark, return basis, periods, units, currencies, metric definitions, as-of dates, calculations, and source URLs are recorded.
- PASS: official/secondary evidence is separated; return-only evidence is not labeled alpha; risk and annual-row gaps are disclosed with correct ownership.
- PASS: proposed performance page, dated source batch, region row, performance-index row, and later run log entry are fully specified; canonical breadcrumb and `geography/International` tag are retained.
- PASS: no unresolved High/Medium finding blocks the write; no WARNING requiring confirmation remains.

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official active-equity evidence and the scheduled-local pre-save checklist passed; AVDV performance artifacts were written.

## EPOL — iShares MSCI Poland ETF

### Identity and classification

- `entity_key: NYSE Arca:EPOL`; ticker `EPOL`; canonical exchange `NYSE Arca`; inception `2010-05-25`.
- `management_mode: passive-index-tracking`; tracked index `MSCI Poland IMI 25/50 Index`; return basis `NAV total return` in USD.
- Primary region: `Poland`; region page `[[Poland ETF]]` was created because the exposure is single-country rather than multi-country Europe.

### Source map

| Source | URL/path | Use |
|---|---|---|
| Issuer current product page | https://www.ishares.com/us/products/239676/ishares-msci-poland-etf | current YTD, NAV/price, AUM, holdings, sector exposure, risk characteristics, fees |
| Issuer performance page | https://www.ishares.com/us/products/239676/ishares-msci-poland-capped-etf?fundSearch=true&qt=EPOL | official rolling/cumulative/calendar 2021-2025 and tracked-index returns |
| Issuer calendar-year page | https://www.ishares.com/ch/professionals/en/products/239676/ishares-msci-poland-capped-etf | official USD calendar rows 2016-2025 |
| Issuer summary prospectus | https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-poland-capped-etf-8-31.pdf | objective, ticker, exchange and fee disclosures |
| Cached benchmark convention | workflow cache | S&P 500 Total Return calendar rows 2016-2025 |

### Raw observations

- Current issuer page as of 2026-08-13: NAV TR YTD `26.40%`; current product snapshot as of 2026-08-14: NAV `44.43`, closing price `44.45`, net assets `US$859,799,003`, 32 holdings.
- Current issuer page: expense ratio `0.59%`, semi-annual distributions, exchange `NYSE Arca`, fund inception `2010-05-25`, tracked index `MSCI Poland IMI 25/50 Index`.
- Current portfolio snapshot as of 2026-08-14: Financials `44.17%`, Energy `13.43%`, Consumer Discretionary `13.20%`; P/E `16.13`, P/B `2.08`, equity beta `0.55`. Three-year standard deviation as of 2026-07-31 is `21.37%`.
- Official rolling NAV TR as of 2026-06-30: `1Y 25.00%`, `3Y 32.43%`, `5Y 16.54%`, `10Y 11.71%`, inception `6.12%`; tracked-index returns `25.90%`, `32.52%`, `16.91%`, `12.18%`, `6.70%`.
- Official calendar NAV/benchmark rows: 2016 `2.8% / 3.7%`, 2017 `52.7% / 53.8%`, 2018 `-14.3% / -14.0%`, 2019 `-5.6% / -4.6%`, 2020 `-8.2% / -8.3%`, 2021 `12.15% / 13.37%`, 2022 `-24.53% / -24.82%`, 2023 `50.13% / 52.23%`, 2024 `-2.58% / -2.04%`, 2025 `76.25% / 75.05%`.
- Same-date current tracked-index YTD and official daily NAV max drawdown/recovery were not disclosed in the reviewed current capture.

### Calculations and reconciliation

- Complete 2016-2025 EPOL using the rounded official annual rows: cumulative `154.36%`, rounded-input CAGR `9.79%`, up/down `5/5`, population annual-return standard deviation `32.01%`.
- Complete 2021-2025 EPOL: cumulative `118.18%`, rounded-input CAGR `16.89%`; tracked index cumulative `122.49%`, CAGR `17.34%`; arithmetic CAGR gap approximately `-0.46 pp`.
- Official rolling 5Y gap: `16.54% - 16.91% = -0.37 pp`; official rolling 10Y gap: `11.71% - 12.18% = -0.47 pp`.
- Best calendar year `2025 +76.25%`; worst `2022 -24.53%`; 10-year calendar CAGR uses rounded inputs and is separate from issuer rolling 10-year average annual `11.71%`.
- S&P 500 cached 2016-2025 cumulative `298.33%` / CAGR `14.82%`; same-window 2021-2025 cumulative `96.17%` / CAGR `14.43%`. No current S&P comparison was mixed with EPOL's 2026-08-13 YTD.

### Local pre-save checklist

- PASS: ETF identity, exchange, country region, tracked index, return basis, periods, units, currencies, metric definitions, as-of dates, calculations, and source URLs are recorded.
- PASS: official issuer calendar and rolling returns are separated; rolling 10-year average annual is not mislabeled as the 2016-2025 CAGR; same-date gaps are disclosed.
- PASS: proposed performance page, Poland region page, performance-index row, region-index row, and dated source-batch contents are specified; canonical breadcrumb and `geography/Poland` tag are present.
- PASS: no unresolved High/Medium finding blocks the write; no WARNING requiring confirmation remains.

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official passive-index evidence and the scheduled-local pre-save checklist passed; EPOL performance artifacts were written.

## EUFN — iShares MSCI Europe Financials ETF

### Identity and classification

- `entity_key: NASDAQ:EUFN`; ticker `EUFN`; canonical exchange `NASDAQ`; inception `2010-01-20`.
- `management_mode: passive-index-tracking`; tracked index `MSCI Europe Financials Index (Net)`; return basis `NAV total return` in USD.
- Primary region: `Europe`; region page `[[Europe ETF]]` was updated because the fund is diversified developed-Europe financials exposure.

### Source map

| Source | URL/path | Use |
|---|---|---|
| Issuer current product page | https://www.ishares.com/us/products/239645/ishares-msci-europe-financials-etf | current YTD, NAV/price, AUM, exposures, risk characteristics, fees |
| Issuer factsheet | https://www.ishares.com/us/literature/fact-sheet/eufn-ishares-msci-europe-financials-etf-fund-fact-sheet-en-us.pdf | official calendar 2021-2025, rolling returns, benchmark and risk characteristics |
| Issuer calendar-year page | https://www.ishares.com/ch/professionals/en/products/239645/ishares-msci-europe-financials-etf?switchLocale=Y | official USD calendar rows 2016-2025 |
| Issuer summary prospectus | https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-europe-financials-etf-7-31.pdf | strategy and worst-quarter disclosure |
| Cached benchmark convention | workflow cache | S&P 500 Total Return calendar rows 2016-2025 |

### Raw observations

- Current issuer page as of 2026-08-14: NAV TR YTD `18.15%`; NAV `42.48`; closing price `42.57`; net assets `US$4,333,340,222`; exchange `NASDAQ`.
- Current issuer facts: expense ratio `0.49%`, semi-annual distributions, 84 holdings, tracked index `MSCI Europe Financials Index (Net)`.
- Current exposures as of 2026-08-14: Banks `59.06%`, Insurance `22.88%`, Financial Services `17.42%`; United Kingdom `23.79%`, Spain `12.38%`, Germany `12.11%`, Switzerland `11.31%`, Italy `10.92%`.
- Current risk characteristics: three-year standard deviation `15.75%` as of 2026-07-31, equity beta `0.61`, P/E `13.71`, P/B `1.78`.
- Official rolling NAV TR as of 2026-06-30: `1Y 28.45%`, `3Y 32.58%`, `5Y 20.44%`, `10Y 14.36%`, inception `7.03%`; tracked-index `28.99%`, `32.73%`, `20.44%`, `14.42%`, `7.14%`.
- Official calendar NAV/benchmark rows: 2016 `-3.1% / -3.0%`, 2017 `27.2% / 27.5%`, 2018 `-23.2% / -23.1%`, 2019 `20.1% / 20.1%`, 2020 `-8.2% / -8.0%`, 2021 `19.22% / 19.50%`, 2022 `-8.79% / -9.03%`, 2023 `26.18% / 25.78%`, 2024 `17.41% / 17.52%`, 2025 `65.23% / 65.97%`.
- The summary prospectus disclosed a worst quarter of `-34.69%` in Q1 2020; this is not a maximum-drawdown metric. Official daily NAV max drawdown/recovery was not captured.

### Calculations and reconciliation

- Complete 2016-2025 EUFN using rounded official annual rows: cumulative `177.80%`, rounded-input CAGR `10.76%`, up/down `6/4`, population annual-return standard deviation `23.89%`.
- Complete 2021-2025 EUFN: cumulative `166.18%`, rounded-input CAGR `21.63%`; S&P 500 TR cumulative `96.17%`, CAGR `14.43%`; arithmetic common-reference advantage about `+7.20 pp` CAGR.
- Official rolling 5Y tracking gap: `20.44% - 20.44% = 0.00 pp`; 10Y gap `14.36% - 14.42% = -0.06 pp`; 1Y gap `28.45% - 28.99% = -0.54 pp`.
- Best calendar year `2025 +65.23%`; worst `2018 -23.20%`; current YTD is kept separate from the 2026-06-30 rolling fields.
- S&P 500 cached 2016-2025 cumulative `298.33%` / CAGR `14.82%`. No current S&P comparison was mixed with EUFN's 2026-08-14 YTD.

### Local pre-save checklist

- PASS: ETF identity, exchange, Europe region, tracked index, return basis, periods, units, currencies, metric definitions, as-of dates, calculations, and source URLs are recorded.
- PASS: official calendar and rolling returns are separated; current YTD and same-date benchmark gaps are disclosed; sector concentration and worst-quarter evidence are not mislabeled as max drawdown.
- PASS: proposed performance page, Europe region row, performance-index row, and dated source-batch contents are specified; canonical breadcrumb and `geography/Europe` tag are present.
- PASS: no unresolved High/Medium finding blocks the write; no WARNING requiring confirmation remains.

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official passive-index evidence and the scheduled-local pre-save checklist passed; EUFN performance artifacts were written.

## EWO — iShares MSCI Austria ETF

### Identity and classification

- `entity_key: NYSE Arca:EWO`; ticker `EWO`; canonical exchange `NYSE Arca`; inception `1996-03-12`.
- `management_mode: passive-index-tracking`; tracked index `MSCI Austria IMI 25/50 Index (Net)`; return basis `NAV total return` in USD.
- Primary region: `Austria`; a new static `[[Austria ETF]]` navigation page was created for this single-country exposure.

### Source map

| Source | URL/path | Use |
|---|---|---|
| Issuer current product page | https://www.ishares.com/us/products/239609/ishares-msci-austria-etf | current YTD, NAV/price, AUM, exposures, risk characteristics, fees |
| Issuer factsheet | https://www.ishares.com/us/literature/fact-sheet/ewo-ishares-msci-austria-etf-fund-fact-sheet-en-us.pdf | official calendar 2021-2025, rolling returns, benchmark, index transition and risk |
| Issuer calendar-year page | https://www.ishares.com/ch/professionals/en/products/239609/ishares-msci-austria-capped-etf?switchLocale=Y | official USD calendar rows 2016-2025 |
| Issuer summary prospectus | https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-austria-capped-etf-8-31.pdf | strategy and risk disclosures |
| Cached benchmark convention | workflow cache | S&P 500 Total Return calendar rows 2016-2025 |

### Raw observations

- Current issuer page as of 2026-08-11: NAV TR YTD `25.85%`; NAV `43.88` as of 2026-08-12; closing price `43.72` as of 2026-08-11; net assets `US$204,053,447` as of 2026-08-12.
- Current issuer facts: expense ratio `0.49%`, semi-annual distributions, exchange `NYSE Arca`, fund inception `1996-03-12`, 21 holdings, tracked index `MSCI Austria IMI 25/50 Index (Net)`.
- Current exposures as of 2026-08-11: Financials `50.04%`, Industrials `14.23%`, Materials `11.00%`, Energy `9.44%`, Utilities `5.96%`.
- Current risk characteristics: three-year standard deviation `15.22%` as of 2026-07-31, equity beta `0.51`, P/E `14.76`, P/B `1.61`.
- Official rolling NAV TR as of 2026-06-30: `1Y 46.02%`, `3Y 34.15%`, `5Y 17.46%`, `10Y 15.59%`; tracked-index `47.39%`, `34.39%`, `17.41%`, `15.61%`.
- Official calendar NAV/benchmark rows: 2016 `7.1% / 7.4%`, 2017 `52.5% / 52.8%`, 2018 `-23.2% / -23.2%`, 2019 `17.7% / 17.9%`, 2020 `-3.2% / -3.5%`, 2021 `30.74% / 31.65%`, 2022 `-21.67% / -22.13%`, 2023 `19.88% / 19.30%`, 2024 `4.58% / 4.25%`, 2025 `72.85% / 74.54%`.
- Index-transition note: EWO began tracking MSCI Austria IMI 25/50 Index (Net) on 2013-02-12; earlier index data was for MSCI Austria Investable Market Index (Net).
- Official daily NAV max drawdown/recovery was not captured.

### Calculations and reconciliation

- Complete 2016-2025 EWO using rounded official annual rows: cumulative `217.16%`, rounded-input CAGR `12.23%`, up/down `7/3`, population annual-return standard deviation `28.87%`.
- Complete 2021-2025 EWO: cumulative `121.92%`, rounded-input CAGR `17.28%`; S&P 500 TR cumulative `96.17%`, CAGR `14.43%`; arithmetic common-reference advantage about `+2.85 pp` CAGR.
- Official rolling 5Y tracking gap: `17.46% - 17.41% = +0.05 pp`; 10Y gap `15.59% - 15.61% = -0.02 pp`; 1Y gap `46.02% - 47.39% = -1.37 pp`.
- Best calendar year `2025 +72.85%`; worst `2018 -23.20%`; current YTD is kept separate from the 2026-06-30 rolling fields.
- S&P 500 cached 2016-2025 cumulative `298.33%` / CAGR `14.82%`. No current S&P comparison was mixed with EWO's 2026-08-11 YTD.

### Local pre-save checklist

- PASS: ETF identity, exchange, Austria region, tracked index, index-transition caveat, return basis, periods, units, currencies, metric definitions, as-of dates, calculations, and source URLs are recorded.
- PASS: official calendar and rolling returns are separated; current YTD and same-date benchmark gaps are disclosed; historical index splice is not treated as a like-for-like uninterrupted benchmark.
- PASS: proposed performance page, Austria region page, performance-index rows, region-index row, and dated source-batch contents are specified; canonical breadcrumb and `geography/Austria` tag are present.
- PASS: no unresolved High/Medium finding blocks the write; no WARNING requiring confirmation remains.

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official passive-index evidence and the scheduled-local pre-save checklist passed; EWO performance artifacts were written.

## GREK — Global X MSCI Greece ETF

### Identity and classification

- `entity_key: NYSE Arca:GREK`; ticker `GREK`; canonical exchange `NYSE Arca`; inception `2011-12-07`.
- `management_mode: passive-index-tracking`; tracked index `MSCI All Greece Select 25/50 Index`; return basis `NAV total return` in USD.
- Primary region: `Greece`; a new static `[[Greece ETF]]` navigation page was created for this single-country exposure.
- The fund is non-diversified and the issuer describes an indexing strategy rather than an attempt to outperform the index.

### Source map

| Source | URL/path | Use |
|---|---|---|
| Issuer current product page | https://www.globalxetfs.com/funds/grek | objective, index, current product snapshot, rolling performance, portfolio, and risk fields |
| SEC summary prospectus | https://www.sec.gov/Archives/edgar/data/1432353/000143235326000191/a497kmscigreece.htm | exchange, fee, strategy, non-diversified status, standardized performance, and best/worst quarter |
| Secondary annual performance | https://www.aaii.com/etf/ticker/GREK?via=emailsignup-readmore | annual NAV total-return rows and rolling cross-check |
| Secondary performance cross-check | https://www.schwab.wallst.com/Prospect/Research/etfs/performance.asp?symbol=grek | current price and NAV/benchmark cross-check through 2026-07-31 |
| Cached benchmark convention | workflow cache | S&P 500 Total Return calendar rows 2016-2025 |

### Raw observations

- Official Global X product snapshot as of 2026-07-27: inception `2011-12-07`, expense ratio `0.56%`, net assets `US$289.29M`, NAV `US$77.44`, and market price `US$78.08`.
- Official trading snapshot as of 2026-07-24: NYSE Arca, 32 holdings, and 30-day median bid/ask spread `0.43%`.
- SEC summary prospectus: management fee `0.55%`, other expenses `0.01%`, total annual fund operating expenses `0.56%`; at least 80% of assets are invested in index constituents, ADRs/GDRs, or companies economically tied to Greece.
- Official rolling NAV TR as of 2026-06-30: `1Y 33.59%`, `3Y 31.38%`, `5Y 26.03%`, `10Y 17.01%`, since inception `5.71%`; tracked-index returns `34.54%`, `32.28%`, `26.83%`, `17.76%`, since inception `6.55%`.
- SEC standardized performance as of 2025-12-31: fund/index `1Y 75.12% / 76.40%`, `5Y 24.58% / 25.34%`, and `10Y 13.54% / 14.20%`; this is a separate as-of date from the issuer's 2026-06-30 rolling table.
- Portfolio and risk snapshot as of 2026-06-30: Financials `48.3%`, Industrials `19.0%`, Utilities `9.9%`, Consumer Discretionary `8.6%`, Energy `5.6%`, Communication `3.9%`, Materials `2.8%`, Real Estate `1.0%`, Staples `0.9%`; standard deviation `19.60%`.
- Official beta fields as of 2026-06-30: S&P 500 `1.08`, NASDAQ-100 `0.68`, MSCI EAFE `1.09`, MSCI EM `0.68`. SEC best/worst quarter: `+31.50%` in Q4 2020 / `-44.00%` in Q1 2020.
- Secondary annual NAV total-return rows as of 2026-06-30: 2016 `-1.2%`, 2017 `32.2%`, 2018 `-29.9%`, 2019 `49.3%`, 2020 `-13.3%`, 2021 `5.7%`, 2022 `3.0%`, 2023 `43.5%`, 2024 `9.7%`, 2025 `75.1%`.
- Secondary Schwab NAV performance as of 2026-07-31: current YTD `+22.0%`, 1Y `+34.6%`, 3Y `+31.5%`, 5Y `+27.6%`; secondary closing price `US$82.85` as of 2026-08-14. The issuer current capture did not expose a same-date numeric YTD field.
- Official numeric issuer calendar-year rows and daily NAV maximum drawdown/recovery were not available in the reviewed captures.

### Calculations and reconciliation

- Complete 2016-2025 secondary proxy: cumulative `255.67%`, rounded-input CAGR `13.53%`, up/down `7/3`, population annual-return standard deviation `31.93%`.
- Complete 2021-2025 secondary proxy: cumulative `200.09%`, rounded-input CAGR `24.58%`, up/down `5/0`; cached S&P 500 TR comparison cumulative `96.17%`, CAGR `14.43%`; arithmetic common-reference CAGR difference approximately `+10.15 pp`, not alpha.
- Official rolling 5Y tracking gap: `26.03% - 26.83% = -0.80 pp`; 10Y gap `17.01% - 17.76% = -0.75 pp`; 1Y gap `33.59% - 34.54% = -0.95 pp`.
- Best secondary calendar year `2025 +75.10%`; worst `2018 -29.90%`; current YTD is kept separate from the official 2026-06-30 rolling fields.
- S&P 500 cached 2016-2025 cumulative `298.33%` / CAGR `14.82%`. No current S&P comparison was mixed with GREK's secondary 2026-07-31 YTD.
- Annual rows are secondary proxy rows because the SEC annual chart was image-based in the reviewed capture; official rolling returns remain the primary performance evidence.

### Local pre-save checklist

- PASS: ETF identity, exchange, Greece region, tracked index, passive classification, return basis, periods, units, currencies, metric definitions, as-of dates, calculations, and source URLs are recorded.
- PASS: official issuer/SEC rolling and standardized returns are separated from secondary annual/YTD proxies; the arithmetic common-reference difference is not labeled alpha; risk and calendar-row gaps are disclosed.
- PASS: proposed performance page, Greece region page, performance-index row, common-window row, region-index row, and dated source-batch contents are fully specified; canonical breadcrumb and `geography/Greece` tag are present.
- PASS: no unresolved High/Medium finding blocks the write; no WARNING requiring confirmation remains.

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official passive-index evidence and the scheduled-local pre-save checklist passed; GREK performance artifacts were written.

## EWP — iShares MSCI Spain ETF

### Identity and classification

- `entity_key: NYSE Arca:EWP`; ticker `EWP`; canonical exchange `NYSE Arca`; inception `1996-03-12`.
- `management_mode: passive-index-tracking`; tracked index `MSCI Spain 25/50 Index (Net)`; return basis `NAV total return` in USD.
- Primary region: `Spain`; region page `[[Spain ETF]]` was created because the exposure is single-country rather than multi-country Europe.

### Source map

| Source | URL/path | Use |
|---|---|---|
| Issuer current product page | https://www.ishares.com/us/products/239683/ishares-msci-spain-capped-etf?qt=EWP | current YTD, NAV/price, AUM, exchange, index, fee and fund facts |
| Issuer fact sheet | https://www.ishares.com/us/literature/fact-sheet/ewp-ishares-msci-spain-etf-fund-fact-sheet-en-us.pdf | official 2021-2025 calendar NAV rows, rolling returns, benchmark, holdings and risk snapshot |
| Issuer summary prospectus | https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-spain-capped-etf-8-31.pdf | official 2016-2020 calendar rows, return definition, index history and quarter-risk disclosures |
| S&P 500 current cross-check | https://www.spglobal.com/spdji/en/additional-reports/all-returns/index.dot?parentIdentifier=df8ec300-24ad-4c70-81d3-a3dcce0200e2&sourceIdentifier=index-family-specialization | S&P 500 (TR) current YTD `14.54%` as of 2026-08-17; non-matched with EWP YTD |
| Cached benchmark convention | workflow cache and https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | S&P 500 Total Return calendar rows 2016-2025 |

### Raw observations

- Official iShares product page: NAV Total Return YTD `16.14%` as of `2026-07-30`; NAV `61.36` and closing price `61.48` as of `2026-07-31`; expense ratio `0.50%`; exchange `NYSE Arca`; benchmark `MSCI Spain 25/50 Index (Net)`; inception `1996-03-12`; distribution frequency semi-annual.
- Official iShares rolling table as of `2026-06-30`: NAV Total Return cumulative `232.40%` over 10 years and annualized `12.76%`; benchmark cumulative `243.69%` and annualized `13.13%`; 1-year NAV `38.56%`, 3-year `31.53%`, 5-year `19.70%`, inception `8.78%`.
- Official iShares fact sheet as of `2026-06-30`: 23 holdings; 3-year equity beta `0.49`; 3-year standard deviation `16.33%`; Financials `43.70%`, Utilities `24.16%`, Industrials `13.91%`; NAV calendar rows 2021 `0.10%`, 2022 `-5.34%`, 2023 `29.80%`, 2024 `6.30%`, 2025 `77.12%`.
- Official summary prospectus calendar chart: 2016 `-2.18%`, 2017 `26.97%`, 2018 `-15.07%`, 2019 `10.94%`, 2020 `-3.14%`; returns assume reinvestment of dividends and distributions.
- Official index history: EWP began tracking MSCI Spain 25/50 Index (Net) on `2013-02-12`; earlier historical index data is for MSCI Spain Index (Net).
- Official iShares distributions: `2026-06-15 $0.924231`, `2025-12-16 $0.740374`, `2025-06-16 $0.483756`, `2024-12-17 $0.818596`; latest four average cash distribution `US$0.741739` per semi-annual round. Latest four sum `US$2.966957`; issuer 12m trailing yield `2.81%` as of `2026-06-30`.
- S&P 500 current cross-check: official S&P 500 (TR) YTD `14.54%` as of `2026-08-17`; this is not combined with EWP's `2026-07-30` YTD in a same-date calculation.

### Calculations and reconciliation

- Complete official 2016-2025 EWP: `(0.9782 × 1.2697 × 0.8493 × 1.1094 × 0.9686 × 1.0010 × 0.9466 × 1.2980 × 1.0630 × 1.7712) - 1 = 162.48%`; rounded-input CAGR `10.13%`; population annual-return standard deviation `25.33%`; up/down `6/4`.
- Complete official 2021-2025 EWP: cumulative `131.57%`, rounded-input CAGR `18.29%`, up/down `4/1`. Cached S&P 500 TR cumulative `96.17%`, CAGR `14.43%` over the same 2021-2025 window.
- Official rolling 10-year endpoint normalization: start TR value `100.00`; end TR value `332.40` from official cumulative `232.40%`; elapsed years `10.00`; `(332.40 / 100.00)^(1/10.00) - 1 = 12.76%`.
- Best complete calendar year `2025 +77.12%`; least positive `2021 +0.10%`; worst `2018 -15.07%`; least bad down year `2016 -2.18%`.
- Official daily NAV maximum drawdown and recovery were not disclosed in the reviewed capture; no secondary proxy was substituted automatically.
- Cached S&P 500 TR annual rows for 2016-2025 are USD total-return rows as of 2025-12-31; cumulative `298.33%` and rounded-input CAGR `14.82%`.

### Local pre-save checklist

- PASS: ETF identity, canonical exchange, passive equity classification, tracked index, return basis, periods, units, currencies, distributions, as-of dates, and source URLs are recorded.
- PASS: rolling 10-year NAV TR is kept separate from the 2016-2025 calendar CAGR; annual rows are official and no proxy or partial-year marker is used; the index-history change is disclosed.
- PASS: current EWP YTD and current S&P 500 cross-check are visibly dated and not treated as a same-date spread; official daily drawdown/recovery remains an explicit gap.
- PASS: proposed EWP performance page, Spain region page, performance-index rows, region-index row, and source-batch contents are specified; canonical breadcrumb, `geography/Spain` tag, and graph links resolve.
- PASS: no unresolved High/Medium finding blocks the write; no WARNING requiring confirmation remains. `verification_mode: scheduled-local` and `reviewer_dispatch: not-attempted-by-design` are recorded in this batch header.

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official passive-index evidence and the scheduled-local pre-save checklist passed; EWP performance artifacts were written.

## IPOL — iShares MSCI Poland UCITS ETF USD (Acc)

### Identity and classification

- `entity_key: LSE:IPOL`; input ticker `IPLCF`; canonical exchange `London Stock Exchange`; official USD listing `IPOL`; ISIN `IE00B4M7GH52`; launch `2011-01-21`.
- `management_mode: passive-index-tracking`; tracked index `MSCI Emerging - Poland in Net USD`; return basis `NAV total return` in USD; use of income `accumulating`.
- Primary region: `Poland`; the region page `[[Poland ETF]]` now includes both EPOL and IPOL.

### Source map

| Source | URL/path | Use |
|---|---|---|
| Issuer current product page | https://www.blackrock.com/uk/individual/products/251875/ishares-msci-poland-ucits-etf_1 | current NAV/YTD, rolling table, fund facts, risk and listings |
| Issuer USD accumulating factsheet | https://www.ishares.com/uk/professional/en/literature/fact-sheet/spol-ishares-msci-poland-ucits-etf-fund-fact-sheet-en-gb.pdf | official share-class annual rows and benchmark rows |
| Issuer professional product page | https://www.ishares.com/uk/professionals/en/products/251875/ishares-msci-poland-ucits-etf?shortLocale=en_GB&siteEntryPassthrough=true&switchLocale=y | listing map, holdings, exposures and risk fields |
| S&P 500 current cross-check | https://www.spglobal.com/spdji/en/additional-reports/all-returns/index.dot?parentIdentifier=df8ec300-24ad-4c70-81d3-a3dcce0200e2&sourceIdentifier=index-family-specialization | current reference cross-check only; date does not match IPOL YTD |
| Cached benchmark convention | workflow cache and https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | S&P 500 Total Return calendar rows 2016-2025 |

### Raw observations

- Current issuer page capture: NAV Total Return YTD `27.44%` as of `2026-08-14`; NAV `US$42.02` as of `2026-08-14`; net assets `US$1,126,150,918` and 16 holdings as of `2026-08-14`.
- Current issuer key facts: TER `0.74%`; accumulating; Ireland domicile; UCITS; physical and replicated; quarterly rebalance; benchmark `MSCI Emerging - Poland in Net USD`.
- Current risk snapshot: 3-year beta `0.993` and standard deviation `22.01%` as of `2026-07-31`; P/E `17.22` and P/B `2.11` as of `2026-08-14`.
- Professional page exposure as of `2026-08-06`: Financials `45.80%`, Energy `16.68%`, Consumer Discretionary `12.86%`, Materials `9.24%`, Consumer Staples `5.32%`, Communication `3.04%`, Information Technology `2.16%`, Utilities `1.83%`, Industrials `1.78%`, and Cash/Derivatives `1.29%`.
- Issuer current rolling table capture reports NAV Total Return annualised `10.24%` over 10 years and cumulative `164.99%`; benchmark `10.43%` annualised and `169.59%` cumulative. The selected date is not surfaced in the HTML, so it is retained as an issuer-current capture anchored to the page's `2026-08-14` snapshot rather than presented as an independently dated endpoint.
- Official March 2026 USD accumulating factsheet calendar rows: fund `0.02, 54.33, -13.14, -6.03, 1.91, 8.16, -27.36, 48.25, -6.47, 74.88`; benchmark `0.13, 54.72, -12.87, -5.87, 1.39, 8.46, -27.24, 48.60, -6.65, 74.61` for 2016-2025.
- The live product-page annual table reports fund `0.0, 54.3, -13.1, -6.0, -11.9, 8.2, -27.4, 48.2, -6.5, 74.9` and benchmark `0.1, 54.7, -12.9, -5.9, -11.4, 8.5, -27.2, 48.6, -6.7, 74.6`. The 2020 conflict (`+1.91%` vs `-11.9%`) is unresolved and preserved.
- The share class is accumulating; no cash-distribution series was used.
- S&P 500 current cross-check from the separate official report is `14.54%` YTD as of `2026-08-17`; it is not a same-date pair with IPOL's `2026-08-14` YTD.

### Calculations and reconciliation

- Factsheet complete common window 2021-2025: `(1.0816 × 0.7264 × 1.4825 × 0.9353 × 1.7488) - 1 = 90.51%`; rounded-input CAGR `13.76%`; up/down `3/2`.
- Factsheet tracked benchmark common window 2021-2025: cumulative `91.15%`; rounded-input CAGR `13.83%`; IPOL trails by approximately `-0.08 pp` CAGR. This is a tracking observation, not alpha.
- S&P 500 cached common-window cumulative `96.17%` / rounded-input CAGR `14.43%`; it is a common reference only.
- Factsheet annual rows across 2016-2025 produce up/down `6/4`, best `2025 +74.88%`, worst `2022 -27.36%`. Because the official live page conflicts with the factsheet in 2020, no cumulative or CAGR is saved for the 2016-2025 annual window.
- Official daily NAV maximum drawdown and recovery were not disclosed in the reviewed sources; no secondary proxy was substituted.

### Local pre-save checklist

- PASS: OTC alias, canonical USD LSE listing, ETF identity, passive classification, tracked index, return basis, periods, units, currencies, and as-of dates are recorded.
- PASS: official current/rolling fields are separated from factsheet annual rows; the 2020 source conflict is preserved; no unsupported 2016-2025 CAGR is calculated; S&P 500 is labeled common reference only.
- PASS: proposed IPOL performance page, Poland region row, performance-index row, common-window row, region-index count, and dated source-batch contents are fully specified; canonical breadcrumb and both ticker tags are present.
- PASS: no unresolved High/Medium finding blocks the write; no WARNING requiring confirmation remains. `verification_mode: scheduled-local` and `reviewer_dispatch: not-attempted-by-design` are recorded in this batch header.

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official passive-index evidence passed the scheduled-local checklist; the 2020 source conflict was disclosed and IPOL performance artifacts were written.

## EWI — iShares MSCI Italy ETF

### Identity and classification

- `entity_key: NYSE Arca:EWI`; ticker `EWI`; canonical exchange `NYSE Arca`; inception `1996-03-12`; CUSIP `46434G830`.
- `management_mode: passive-index-tracking`; tracked index `MSCI Italy 25/50 Index (Net)`; return basis `NAV total return` in USD; semi-annual distributions.
- Primary region: `Italy`; a new static region page `[[Italy ETF]]` was created and linked from both ETF indexes.

### Source map

| Source | URL/path | Use |
|---|---|---|
| Issuer current product page | https://www.ishares.com/us/products/239664/ishares-msci-italy-etf | current NAV/YTD, rolling returns, 2021-2025 annual rows, fund facts, exposures and distributions |
| Issuer summary prospectus | https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-italy-capped-etf-8-31.pdf | 2016-2020 annual NAV rows, return definition, index strategy, risks and best/worst quarter |
| S&P 500 current cross-check | https://www.spglobal.com/spdji/en/additional-reports/all-returns/index.dot?parentIdentifier=df8ec300-24ad-4c70-81d3-a3dcce0200e2&sourceIdentifier=index-family-specialization | current reference cross-check only; date does not match EWI YTD |
| Cached benchmark convention | workflow cache and https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | S&P 500 Total Return calendar rows 2016-2025 |

### Raw observations

- Official current page: NAV Total Return YTD `18.73%` and NAV `US$63.17` as of `2026-08-14`; closing price `US$63.27`, net assets `US$1,160,763,629`, 25 holdings, and 30-day median bid/ask spread `0.02%` as of `2026-08-14`.
- Fund facts: expense ratio `0.50%`; management fee `0.49%`; inception `1996-03-12`; benchmark `MSCI Italy 25/50 Index (Net)`; distribution frequency semi-annual.
- Official rolling table as of `2026-06-30`: NAV TR `1Y 27.21%`, `3Y 27.34%`, `5Y 17.16%`, `10Y 14.40%`, inception `6.44%`; benchmark `27.17%`, `27.34%`, `17.19%`, `14.48%`, with no inception benchmark value shown.
- Official current risk snapshot: Financials `54.88%`, Utilities `15.98%`, Consumer Discretionary `8.75%`, Industrials `7.81%`, Energy `6.84%`, Communication `2.41%`, Health Care `1.28%`, Consumer Staples `0.98%`, Materials `0.87%`, and Cash/Derivatives `0.21%` as of `2026-08-14`; 3-year standard deviation `15.16%`, beta `0.63`, P/E `15.84`, and P/B `2.14` across the issuer's stated dates.
- Official summary prospectus calendar NAV rows: 2016 `-9.40%`, 2017 `28.47%`, 2018 `-17.51%`, 2019 `27.19%`, 2020 `2.56%`, 2021 `13.80%`, 2022 `-14.19%`, 2023 `30.34%`, and 2024 `10.39%`. The current product page supplies 2025 `55.51%` and official benchmark rows for 2021-2025: `14.15%`, `-14.59%`, `30.66%`, `10.66%`, `56.28%`.
- Official current distributions: `2026-06-15 $1.173545`, `2025-12-16 $0.702133`, `2025-06-16 $0.821604`, and `2024-12-17 $0.559282`; latest four sum `US$3.256564`, average `US$0.814141`; issuer 12m trailing yield `3.05%` as of `2026-07-31`.
- Summary prospectus best/worst quarter: `+27.29%` in Q4 2022 / `-29.51%` in Q1 2020. Daily NAV maximum drawdown and recovery were not captured.
- S&P 500 current cross-check from the separate official report is `14.54%` YTD as of `2026-08-17`; it is not a same-date pair with EWI's `2026-08-14` YTD.

### Calculations and reconciliation

- Complete official fund 2016-2025: `(0.9060 × 1.2847 × 0.8249 × 1.2719 × 1.0256 × 1.1380 × 0.8581 × 1.3034 × 1.1039 × 1.5551) - 1 = 173.66%`; rounded-input CAGR `10.59%`; population annual-return standard deviation `21.99%`; up/down `7/3`.
- Complete official fund 2021-2025: cumulative `118.50%`, rounded-input CAGR `16.92%`, up/down `4/1`; cached S&P 500 TR cumulative `96.17%`, CAGR `14.43%` over the same window.
- Complete official tracked-index 2021-2025: cumulative `120.30%`, rounded-input CAGR `17.11%`; EWI trails by approximately `-0.19 pp` CAGR. This is tracking evidence, not alpha.
- Official rolling 10-year endpoint normalization: start TR value `100.00`; end TR value `383.84` from cumulative `283.84%`; annualised `(383.84 / 100.00)^(1/10) - 1 = 14.40%`, as reported by the issuer for the 2026-06-30 window.
- Best complete calendar year `2025 +55.51%`; worst `2018 -17.51%`; average positive year `24.04%`.
- Official daily NAV maximum drawdown and recovery were not disclosed; no secondary proxy was substituted automatically.

### Local pre-save checklist

- PASS: ETF identity, NYSE Arca exchange, passive classification, tracked index, return basis, periods, units, currencies, distributions, and as-of dates are recorded.
- PASS: 2016-2020 prospectus rows and 2021-2025 product-page rows are separated by source; official rolling and current fields are not mixed with annual windows; S&P 500 is labeled common reference only.
- PASS: proposed EWI performance page, new Italy region page, performance-index row, common-window row, region-index row, and dated source-batch contents are fully specified; canonical breadcrumb and `geography/Italy` tag are present.
- PASS: no unresolved High/Medium finding blocks the write; no WARNING requiring confirmation remains. `verification_mode: scheduled-local` and `reviewer_dispatch: not-attempted-by-design` are recorded in this batch header.

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official passive-index evidence and the scheduled-local pre-save checklist passed; EWI performance artifacts were written.

## FDD — First Trust STOXX European Select Dividend Index Fund

### Identity and classification

- `entity_key: NYSE Arca:FDD`; ticker `FDD`; canonical exchange `NYSE Arca`; inception `2007-08-27`; CUSIP `33735T109`; ISIN `US33735T1097`.
- `management_mode: passive-index-tracking`; tracked index `STOXX Europe Select Dividend 30 Index`; return basis `NAV total return` in USD.
- Primary region: `Europe`; the existing static region page `[[Europe ETF]]` and existing FDD performance page were updated.

### Source map

| Source | URL/path | Use |
|---|---|---|
| Issuer product page | https://www.ftportfolios.com/retail/etf/etfsummary.aspx?Ticker=FDD | current NAV/price, fund facts, fee, holdings, exposures, distribution fields and methodology |
| Issuer performance list | https://www.ftportfolios.com/retail/etf/etflist.aspx?DisplayType=PerformanceNav&Type=Dividend | current standardized NAV performance as of 2026-07-31 |
| Issuer prospectus | https://www.ftportfolios.com/Funds/ETF/Prospectus/FAN | official annual NAV TR rows and return definitions |
| Cached benchmark convention | workflow cache and https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | S&P 500 Total Return calendar rows 2016-2025 |

### Raw observations

- Official First Trust performance list as of `2026-07-31`: NAV TR `3M 8.27%`, `YTD 18.51%`, `1Y 38.57%`, `3Y 26.57%`, `5Y 13.10%`, `10Y 10.86%`, and since inception `2.84%`.
- Official product page fund data as of `2026-07-23`: NAV `US$19.25`, market price `US$19.25`, total net assets `US$853,048,790`, and 30 holdings.
- Current issuer fee disclosure: expense ratio `0.56%` as of `2026-02-02`; expenses capped at `0.60%` through at least `2027-01-31`. The prior durable page's `0.58%` is retained as a source conflict; the current issuer disclosure is used.
- Product methodology: 30 European dividend-paying stocks selected from STOXX Europe 600 using positive five-year dividend-per-share growth, a dividend-to-EPS screen and yield/outperformance criteria; individual holdings are capped at 15%.
- Current exposure snapshots: country Netherlands `22.79%`, France `21.76%`, UK `20.21%`, Germany `9.34%`, Norway `4.21%`, South Africa `4.05%`, Jersey `3.93%`, Italy `3.58%`, Belgium `2.85%`, Poland `2.74%`; sectors Financials `57.23%`, Consumer Discretionary `15.31%`, Industrials `9.58%`, Energy `6.95%`, Real Estate `3.26%`, Materials `2.95%`, Utilities `2.74%`, Communication Services `1.98%` as of the issuer's 2026-06 snapshots.
- Distribution fields as of `2026-06-30`: 30-day SEC yield `4.33%`, 12-month distribution rate `5.45%`, and index yield `5.98%`.
- Official annual NAV TR rows for 2016-2025: `2.58%`, `19.04%`, `-8.83%`, `23.09%`, `-2.64%`, `15.07%`, `-15.67%`, `13.42%`, `0.60%`, `61.85%`. Cached S&P 500 TR rows for the same years are `11.96%`, `21.83%`, `-4.38%`, `31.49%`, `18.40%`, `28.71%`, `-18.11%`, `26.29%`, `25.02%`, `17.88%`.
- Official daily NAV maximum drawdown and recovery were not disclosed in the reviewed sources; no secondary proxy was substituted.

### Calculations and reconciliation

- Complete FDD 2016-2025 using the displayed annual rows: cumulative `139.09%`; rounded-input CAGR `9.11%`; population annual-return standard deviation `20.71%`; up/down `7/3`; best `2025 +61.85%`; worst `2022 -15.67%`.
- Complete FDD 2021-2025 using the displayed annual rows: cumulative `79.20%`; rounded-input CAGR `12.37%`; up/down `4/1`; average positive year `22.74%`.
- Cached S&P 500 TR common-window cumulative `96.17%` / rounded-input CAGR `14.43%`; FDD trails by approximately `-2.05 pp` CAGR. This is a common-reference comparison, not alpha.
- The issuer's current 10-year annualised figure `10.86%` and current YTD `18.51%` are kept separate from the rounded-input calendar-window calculations because their as-of date and return window differ.

### Local pre-save checklist

- PASS: ETF identity, exchange, passive classification, tracked index, return basis, periods, units, currencies, metric definitions, as-of dates, calculations, and source URLs are recorded.
- PASS: current issuer rolling/YTD fields are separated from annual rows; the older `0.58%` fee versus current `0.56%` fee is disclosed as a source conflict; common-reference comparison is not labeled alpha; daily drawdown/recovery gap is retained.
- PASS: proposed FDD performance page, Europe region row, performance-index row, existing-page delta, and dated source-batch contents are fully specified; canonical breadcrumb and `geography/Europe` tag are present.
- PASS: no unresolved High/Medium finding blocks the write; no WARNING requiring confirmation remains. `verification_mode: scheduled-local` and `reviewer_dispatch: not-attempted-by-design` are recorded in this batch header.

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official passive-index evidence and the scheduled-local pre-save checklist passed; FDD performance artifacts were refreshed.

## EUAD — Select STOXX Europe Aerospace & Defense ETF

### Identity and classification

- `entity_key: Cboe BZX:EUAD`; ticker `EUAD`; canonical exchange `Cboe BZX`; inception `2024-10-22`; CUSIP `84858T772`.
- `management_mode: passive-index-tracking`; tracked index `STOXX Europe Total Market Aerospace & Defense Index`; return basis `NAV total return` in USD.
- Primary region: `Europe`; the existing static region page `[[Europe ETF]]` was updated and a new EUAD performance page was created.

### Source map

| Source | URL/path | Use |
|---|---|---|
| Issuer fund page | https://www.select-funds.com/fund-info | official identity, exchange, inception, fee, NAV/market-price snapshot, assets, holdings count, strategy and risk disclosures |
| SEC summary prospectus | https://www.sec.gov/Archives/edgar/data/1484018/000148401824000217/r497e1024.htm | official Cboe BZX listing, passive strategy, fee breakdown, index construction, replication and risks |
| STOXX index page | https://stoxx.com/index/sxparo/ | tracked-index identity, USD net-return availability and index context |
| Secondary performance page | https://www.schwab.wallst.com/Prospect/Research/etfs/performance.asp?symbol=euad | issuer-display gap fill: NAV period returns through 2026-06-30 and worst 3-month observation |
| Secondary summary page | https://www.schwab.wallst.com/Prospect/Research/etfs/summary.asp?symbol=euad | latest NAV/market price, holdings conflict and distribution cross-check |
| S&P 500 official page | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | common benchmark definition; complete cached rows are not used for the short EUAD history |

### Raw observations

- Official issuer page snapshot as of `2026-07-29`: NAV `US$43.91`, market price `US$43.98`, net assets `US$1,166,571,261`, gross expense ratio `0.50%`, primary exchange `Cboe`, 23 holdings, 26,570,000 shares outstanding and 30-day median bid-ask `0.22%`.
- SEC prospectus: ticker `EUAD`; shares listed on Cboe BZX; management fee `0.05%`, other expenses `0.45%`, total annual fund operating expenses `0.50%`; the fund invests at least 80% of assets in index components and uses a passive approach with replication or representative sampling.
- SEC prospectus index description: the index covered 25 European aerospace-and-defense companies as of 2024-07-31, uses the STOXX Europe Total Market universe and is rebalanced/reconstituted daily based on relative market capitalization.
- Secondary Schwab snapshot as of `2026-06-30`: NAV TR YTD `+0.20%`, 1-month `-1.0%`, 3-month `+3.3%`, 6-month `+0.2%`, 1-year `-1.5%`, since-inception hypothetical US$10,000 growth to `US$17,230` (`+72.30%` cumulative) and since-inception annualised return `+36.80%`.
- Secondary Schwab snapshot reports worst 3-month return `-9.9%` for `2025-09-30` to `2025-12-31`; official daily NAV maximum drawdown and recovery were not disclosed.
- Latest secondary cross-check as of `2026-08-14`: closing NAV `US$47.99`, market price `US$47.89`, 33 holdings, and approximately 62.7% in a money-market position plus swap positions. This conflicts with the official 2026-07-29 snapshot of NAV `US$43.91`, 23 holdings and a portfolio displayed as securities; no combined holdings or return calculation is made.
- Secondary distribution cross-check: previous dividend `US$0.1688`, ex-date `2025-12-30`, pay date `2025-12-31`; trailing distribution yield `0.38%` on the current summary page. The issuer's current distribution series was not exposed in the reviewed static capture.
- No official issuer numeric current YTD, annual NAV rows, or complete 2021-2025 calendar window was exposed in the reviewed capture. Fund inception is under two years, so 10-year and 2021-2025 windows are not applicable.

### Calculations and reconciliation

- No 10-year NAV TR CAGR, 2016-2025 cumulative return, 2021-2025 CAGR, up/down count or calendar-year best/worst was calculated because the fund began on 2024-10-22 and the issuer did not disclose a complete annual NAV table.
- Secondary NAV YTD `+0.20%` and 1-year `-1.50%` are retained as period observations as of 2026-06-30; they are not relabelled as current August performance and are marked `†` in the performance page.
- Secondary since-inception cumulative growth is `US$17,230 / US$10,000 - 1 = 72.30%`; the source separately reports annualised since-inception return `36.80%`. No independently annualised CAGR is substituted because the exact endpoint convention is not exposed.
- S&P 500 cached 2016-2025 rows are not a comparable window for EUAD's short history; no same-date current S&P 500 comparison is claimed.

### Local pre-save checklist

- PASS: ETF identity, Cboe BZX exchange, passive classification, tracked index, return basis, limited-history window, units, currencies, metric definitions, as-of dates and source URLs are recorded.
- PASS: official issuer and SEC evidence establish eligibility; secondary NAV observations are separated and marked `†`; official current-YTD gap, official/secondary NAV-date conflict and holdings conflict are disclosed; no 10-year label is applied to a shorter history.
- PASS: proposed EUAD performance page, Europe region row, performance-index addition, region-index count, and dated source-batch contents are fully specified; canonical breadcrumb and `geography/Europe` tag are present.
- PASS: no unresolved High/Medium finding blocks the write; no WARNING requiring confirmation remains. `verification_mode: scheduled-local` and `reviewer_dispatch: not-attempted-by-design` are recorded in this batch header.

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official passive-index evidence established EUAD eligibility; the scheduled-local checklist passed and the limited-history/source-conflict gaps were disclosed.

## OPPE — WisdomTree European Opportunities Fund

### Identity and classification

- `entity_key: NYSE Arca:OPPE`; ticker `OPPE`; canonical exchange `NYSE Arca`; inception `2015-03-04`; CUSIP `97717X552`.
- `management_mode: passive-index-tracking`; the prospectus describes passive management/indexing and representative sampling.
- Current tracked index: `WisdomTree European Opportunities Index`; historical performance uses the `WisdomTree Europe Hedged SmallCap Equity / WisdomTree European Opportunities Equity Spliced Index`.
- Primary region: `Europe`; the existing static region page `[[Europe ETF]]` was updated and a new OPPE performance page was created.
- The fund changed name from WisdomTree Europe Hedged SmallCap Equity Fund (EUSC) and changed its investment policy/index effective `2025-06-02`; the 2016-2024 history and part of 2025 therefore do not represent a continuous current-strategy record.

### Source map

| Source | URL/path | Use |
|---|---|---|
| WisdomTree product page | https://www.wisdomtree.com/us/products/equity/oppe | identity, current index objective, fee, NAV/price, rolling returns, YTD, sector/holdings and hedge ratio |
| WisdomTree OPPE quarterly factsheet | https://www.wisdomtree.com/us/media/international-equity/en-us-equity-oppe | exchange, inception, return basis, official performance table, historical index splice and risk disclosures |
| WisdomTree Trust prospectus | https://regulated-documents.saytechnologies.com/prospectuses/e0ff850f-45f1-417b-8779-01e2206cb79d-97717X552.pdf | passive strategy, representative sampling, official 2016-2024 annual-return chart and strategy-change disclosure |
| WisdomTree monthly performance report | https://www.wisdomtree.com/investments/-/media/us-media-files/documents/resource-library/fund-reports-schedules/performance/monthly-performance.pdf | official 2025 NAV return ending 2025-12-31 |
| WisdomTree European Opportunities Index | https://www.wisdomtree.com/us/indexes/wteuop | index design, shareholder-yield/value and dynamic currency-hedge methodology |
| Secondary drawdown proxy | https://portfolioslab.com/symbol/OPPE | dividend-adjusted daily market-price drawdown/recovery proxy only |
| Cached benchmark convention | workflow cache | S&P 500 Total Return calendar rows 2016-2025 in USD with dividends reinvested |

### Raw observations

- WisdomTree product page as of `2026-08-14`: net expense ratio `0.58%`, distribution yield `7.83%`, 30-day SEC yield `2.72%`, NAV `US$60.308`, closing market price `US$60.504`, premium/discount `+0.324%`, and aggregate hedge ratio `97.95%`.
- WisdomTree product page month-end performance as of `2026-07-31`: NAV TR YTD `17.72%`, 1-year `29.84%`, 3-year `23.84%`, 5-year `14.66%`, 10-year average annual `12.91%`, and since-inception average annual `11.59%`.
- Official product/factsheet identity: NYSE Arca listing, inception `2015-03-04`, current index symbol `NDDLE15`, and total-return calculation based on the daily 4:00pm NAV. The displayed NAV symbol remains `EUSC.NV` as a legacy source identifier after the ticker/name change; the canonical entity remains `NYSE Arca:OPPE`.
- Official index page: the current WisdomTree European Opportunities Index was established with base value `200` on `2025-04-30`; its hedge ratio ranges from `0%` to `100%` monthly and its construction combines total shareholder yield with geopolitical, technology and macro opportunity exposures.
- Official annual NAV TR rows used for 2016-2024 from the prospectus annual-return chart: 2016 `7.86%`, 2017 `22.32%`, 2018 `-13.41%`, 2019 `28.45%`, 2020 `-2.34%`, 2021 `22.65%`, 2022 `-11.18%`, 2023 `19.33%`, 2024 `10.74%`.
- Official 2025 NAV TR: `38.73%` for the one-year period ending `2025-12-31` in the WisdomTree monthly performance report; this row includes the June 2025 strategy/index transition.
- Secondary ETFreplay annual table differs from the official NAV chart in several years, including 2020 `-2.92%` and 2021 `23.51%`; it was excluded from the NAV annual table because its historical basis is not the selected official NAV source. PortfoliosLab rows are also treated as dividend-adjusted market-price history, not NAV TR.
- Secondary PortfoliosLab daily dividend-adjusted market-price proxy reports maximum drawdown `39.28%` on `2020-03-18` and recovery in `229` trading sessions. Official daily NAV maximum drawdown and recovery were not disclosed.
- Cached S&P 500 Total Return annual rows for 2016-2025 are USD total-return rows as of `2025-12-31`; cumulative `298.33%` and rounded-input CAGR `14.82%`.

### Calculations and reconciliation

- Complete OPPE 2016-2025 using the official rounded annual rows: cumulative `186.21%`; rounded-input CAGR `11.09%`; population annual-return standard deviation `16.33%`; up/down `7/3`; best `2025 +38.73%`; worst `2018 -13.41%`; least-bad down year `2020 -2.34%`.
- Complete OPPE 2021-2025: cumulative `99.71%`, rounded-input CAGR `14.84%`; cached S&P 500 TR cumulative `96.17%`, CAGR `14.43%`. The comparison is a common-reference comparison, not alpha.
- The issuer's rolling 10-year NAV TR average annual `12.91%` as of `2026-07-31` is kept separate from the rounded-input 2016-2025 calendar-row CAGR because the windows have different endpoints.
- The current YTD `17.72%` is as of `2026-07-31`; no same-date current S&P 500 YTD value was mixed into the table because the workflow cache only covers complete 2016-2025 calendar years.
- The secondary drawdown/recovery values are retained only as a marked market-price proxy; no NAV risk metric is inferred from them.

### Local pre-save checklist

- PASS: ETF identity, NYSE Arca exchange, passive classification, tracked index, historical splice, return basis, periods, units, currencies, metric definitions, as-of dates, calculations and source URLs are recorded.
- PASS: official annual NAV rows are separated from secondary ETFreplay/PortfoliosLab data; the source-quality choice and conflicting annual observations are disclosed; rolling 10-year and calendar-row CAGR are not mixed; current YTD and quotes have separate as-of dates.
- PASS: 2025 strategy/index transition and legacy EUSC source symbol are disclosed; current-strategy continuity is not overstated; market-price drawdown proxy is not labeled NAV evidence.
- PASS: proposed OPPE performance page, Europe region row, region-index count, performance-index rows, dated source-batch contents and one log bullet are fully specified; canonical breadcrumb and `geography/Europe` tag are present; all planned wikilinks resolve.
- PASS: no unresolved High/Medium finding blocks the write; no WARNING requiring confirmation remains. `verification_mode: scheduled-local` and `reviewer_dispatch: not-attempted-by-design` are recorded in this batch header.

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official passive-index evidence and the scheduled-local pre-save checklist passed; OPPE performance artifacts were written with the 2025 strategy-transition gap disclosed.

## FEP — First Trust Europe AlphaDEX Fund

### Identity and classification

- `entity_key: NASDAQ:FEP`; ticker `FEP`; canonical exchange `Nasdaq`; inception `2011-04-18`; CUSIP `33737J117`; ISIN `US33737J1170`.
- `management_mode: passive-index-tracking`; tracked index `Nasdaq AlphaDEX Europe Index`; return basis `NAV total return` in USD.
- The fund uses an indexing approach and normally invests at least 90% of net assets in index securities. The index is rules-based and selects from Nasdaq Developed Markets Europe using growth and value factors; this is not active long-only management.
- Primary region: `Europe`; the existing static region page `[[Europe ETF]]` was updated and a new FEP performance page was created.

### Source map

| Source | URL/path | Use |
|---|---|---|
| First Trust product page | https://www.ftportfolios.com/Retail/Etf/EtfSummary.aspx?Ticker=FEP | identity, index methodology, fee, current NAV/price, holdings, exposures, rolling returns, YTD and risk statistics |
| First Trust prospectus | https://www.ftportfolios.com/LoadContent/gradkqbz8r4y | passive strategy, index-change disclosure, official 2016-2025 annual-return chart, average annual returns and risk disclosure |
| SEC N-CSR / FEP annual report | https://www.sec.gov/Archives/edgar/data/1510337/000144554626001916/adex2_ncsr.htm | 2025 official annual return and fund/index comparison |
| Cached benchmark convention | workflow cache | S&P 500 Total Return calendar rows 2016-2025 in USD with dividends reinvested |

### Raw observations

- Official First Trust product page: FEP is a Nasdaq-listed international equity ETF with inception `2011-04-18`, total expense ratio `0.80%` as of `2026-05-01`, and `200` holdings excluding cash as of `2026-08-13`.
- Current snapshot as of `2026-08-13`: NAV `US$59.71`, closing market price `US$59.97`, premium `+0.44%`, net assets `US$534,405,825`; 30-day median bid/ask spread `0.40%` as of `2026-08-12`.
- Product page month-end performance as of `2026-07-31`: NAV TR `3M 2.58%`, `YTD 11.02%`, `1Y 27.32%`, `3Y 21.97%`, `5Y 10.06%`, `10Y 10.57%`, and since inception `7.61%`. Official Nasdaq AlphaDEX Europe Index rows were `2.79%`, `11.31%`, `27.45%`, `22.85%`, `10.84%`, and `11.31%` for the same periods.
- Current exposures as of `2026-08-12`: United Kingdom `20.08%`, Germany `13.52%`, France `11.36%`, Italy `8.09%`, Sweden `7.28%`; sectors Industrials `21.63%`, Materials `13.85%`, Financials `12.05%`, Consumer Discretionary `11.13%`, and Energy `10.74%`.
- Official 3-year statistics as of `2026-07-31`: standard deviation `14.98%`, beta `1.00`, Sharpe ratio `1.11`, and correlation `0.93`; daily NAV maximum drawdown and recovery are not disclosed in the reviewed issuer capture.
- Prospectus calendar-year NAV TR rows as of `2025-12-31`: 2016 `1.24%`, 2017 `35.67%`, 2018 `-18.67%`, 2019 `24.38%`, 2020 `4.95%`, 2021 `16.53%`, 2022 `-22.87%`, 2023 `16.01%`, 2024 `3.71%`, 2025 `55.13%`.
- Prospectus average annual return table for periods ended `2025-12-31`: FEP `1Y 55.13%`, `5Y 10.91%`, `10Y 9.36%`, since inception `7.16%`; Nasdaq AlphaDEX Europe Index `1Y 56.05%`, `5Y 11.68%`, `10Y 10.04%`.
- The prospectus states that the underlying index changed on `2015-10-13` from the Defined Europe Index to the Nasdaq AlphaDEX Europe Index and describes the new index as substantially similar. The performance history is therefore retained with an index-continuity caveat.
- The prospectus discloses best quarter `+22.10%` ended `2022-12-31` and worst quarter `-31.13%` ended `2020-03-31`; these are quarterly observations, not maximum drawdown/recovery.

### Calculations and reconciliation

- Complete 2016-2025 FEP using the official displayed annual rows: `(1.0124 × 1.3567 × 0.8133 × 1.2438 × 1.0495 × 1.1653 × 0.7713 × 1.1601 × 1.0371 × 1.5513) - 1 = 144.62%`; rounded-input CAGR `9.36%`; population annual-return standard deviation `22.36%`; up/down `8/2`.
- Complete 2021-2025 FEP: cumulative `67.75%`, rounded-input CAGR `10.90%`; cached S&P 500 TR cumulative `96.17%`, CAGR `14.43%` over the same window.
- Cached S&P 500 TR common-window 2016-2025 is `298.33%` cumulative / `14.82%` rounded-input CAGR. It is a common reference comparison, not the tracked index.
- Official same-date 2026-07-31 YTD tracking comparison: FEP NAV TR `11.02%` versus Nasdaq AlphaDEX Europe Index `11.31%`; this is tracking evidence, not alpha or manager-skill evidence.
- The issuer's rolling 10-year average annual `10.57%` as of `2026-07-31` is kept separate from the rounded-input 2016-2025 calendar CAGR `9.36%`.

### Local pre-save checklist

- PASS: ETF identity, Nasdaq exchange, passive classification, tracked index, return basis, periods, units, currencies, metric definitions, as-of dates, calculations, and source URLs are recorded.
- PASS: official rolling/YTD fields are separated from calendar rows; the strategy-aligned index is separated from the S&P 500 common reference; tracking differences are not labeled alpha; the 2015 index change and daily NAV drawdown/recovery gap are disclosed.
- PASS: proposed FEP performance page, Europe region row, performance-index row, common-window row, and dated source-batch contents are fully specified; canonical breadcrumb and `geography/Europe` tag are present.
- PASS: no unresolved High/Medium finding blocks the write; no WARNING requiring confirmation remains. `verification_mode: scheduled-local` and `reviewer_dispatch: not-attempted-by-design` are recorded in this batch header.

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official passive-index evidence and the scheduled-local pre-save checklist passed; FEP performance artifacts were written with the 2015 index-continuity caveat disclosed.

## FTDPF / FTEU — First Trust Eurozone AlphaDEX UCITS ETF

### Identity and classification

- Input ticker `FTDPF` is an OTC alias for First Trust Global Funds Plc. The official First Trust factsheet maps ISIN `IE00B8X9NY41` to the USD London Stock Exchange line `FTEU LN`; durable ownership therefore uses `entity_key: LSE:FTEU` and preserves `FTDPF` as `input_ticker`.
- `fund: First Trust Eurozone AlphaDEX UCITS ETF`; official fund/share-class inception `2014-10-21`; Ireland-domiciled UCITS; base currency EUR; accumulating share class.
- `management_mode: passive-index-tracking`; tracked index `Nasdaq AlphaDEX Eurozone NTR Index`; physical full replication; semi-annual rebalance; ongoing charges `0.65%` as of `2026-05-29`.
- Primary region: `Europe`; the existing static region page `[[Europe ETF]]` was updated and a new canonical FTEU performance page was created.

### Source map

| Source | URL/path | Use |
|---|---|---|
| First Trust official factsheet | https://www.fundslibrary.co.uk/FundsLibrary.DataRetrieval/Documents.aspx/?id=db97fa3f-452a-4e87-a092-5d78014ea6e7&r=1&type=packet_fund_class_doc_factsheet_private&user=lmaloTxGN4q8hRUMT0fWlPBQqCmCX%2FhnFIbf7%2F7XByN2nwFrjrtLgpitSJYn96ru | ISIN, official trading lines, inception, fee, UCITS/passive/physical structure, official Acc EUR performance and exposures as of 2026-05-29 |
| Central Bank of Ireland fund register | https://registers.centralbank.ie/%28X%281%29S%28uzbkfrrwrh3qjlqvxporqnfl%29%29/FundRegisterDataPage.aspx?fundReferenceNumber=C118215&register=28 | UCITS fund identity and regulatory status |
| Morningstar FTEU report | https://lt.morningstar.com/1c6qh1t6k9/etfreport/default.aspx?1=1&ClientFund=0&CurrencyId=USD&Id=0P00018JZQ&SecurityToken=0P00018JZQ%5D22%5D0%5DETEXG%24XLON&tab=1 | secondary USD annual and trailing-return fields |
| OTC alias cross-check | https://www.eoddata.com/stockquote/OTCBB/FTDPF.htm | input alias legal-name cross-check only; not used as primary NAV evidence |
| Cached benchmark convention | workflow cache | S&P 500 Total Return rows for 2021-2025 in USD with dividends reinvested |

### Raw observations

- Official First Trust factsheet as of `2026-05-29`: ISIN `IE00B8X9NY41`, asset class equity, fund/share-class inception `2014-10-21`, ongoing charges `0.65%`, base currency EUR, income treatment accumulating, UCITS compliant, Ireland domicile, physical full replication, and tracking index `Nasdaq AlphaDEX Eurozone NTR Index`.
- Official trading lines for the same ISIN: London Stock Exchange GBP `FEUZ LN`, London Stock Exchange USD `FTEU LN`, Borsa Italiana EUR `FEUZ IM`, Xetra EUR `FTGE GY`, and Euronext Amsterdam EUR `FEUZ NA`. The input OTC symbol `FTDPF` is retained as an alias, not as the canonical exchange key.
- Official Acc EUR performance as of `2026-05-29`: YTD `13.39%`, 1-year `30.66%`, 3-year annualised `23.40%`, 5-year annualised `11.91%`, and since inception annualised `10.68%`; tracking-index fields were `13.44%`, `30.55%`, `23.25%`, `11.97%`, and `11.02%`.
- Official portfolio snapshot as of `2026-05-29`: country Germany `22.47%`, France `20.14%`, Italy `14.54%`, The Netherlands `9.04%`, Spain `8.95%`; sectors Industrials `22.44%`, Materials `12.25%`, Financials `10.65%`, Energy `10.46%`, Consumer Discretionary `9.57%`, and Utilities `9.29%`.
- Secondary Morningstar FTEU USD annual returns: 2021 `12.59%`, 2022 `-19.74%`, 2023 `16.65%`, 2024 `3.03%`, 2025 `57.98%`; USD trailing fields as of `2026-07-30`: YTD `12.31%`, 1-year `20.85%`, 3-year annualised `21.29%`, and 5-year annualised `10.98%`. A separate secondary 10-year annualised field is `10.75%` as of `2026-07-27`.
- Secondary USD closing-price snapshot: `US$75.54` as of `2026-07-30`; it is not used in NAV return calculations. Official daily NAV maximum drawdown and recovery were not disclosed.

### Calculations and reconciliation

- Secondary USD 2021-2025: `(1.1259 × 0.8026 × 1.1665 × 1.0303 × 1.5798) - 1 = 71.57%`; rounded-input CAGR `11.40%`; population annual-return standard deviation `25.31%`; up/down `4/1`.
- Cached S&P 500 TR 2021-2025 cumulative `96.17%` / rounded-input CAGR `14.43%`; this is a common reference comparison only and is not the issuer benchmark.
- The official Acc EUR factsheet series is kept separate from the secondary USD FTEU series; no currency conversion or cross-currency excess-return calculation is made.
- No official 2016-2025 calendar table for the FTEU USD line was exposed in the reviewed capture, so no official 10-year calendar CAGR, annual up/down ranking beyond the secondary 2021-2025 window, or official USD drawdown/recovery metric is claimed.

### Local pre-save checklist

- PASS: OTC alias, canonical USD LSE listing, ISIN/share-class identity, passive classification, tracked index, return basis, periods, units, currencies, and as-of dates are recorded.
- PASS: official EUR-base factsheet returns are separated from secondary USD alias returns; no cross-currency calculation is made; the lack of official USD calendar rows and daily NAV drawdown/recovery is disclosed; the S&P 500 is labeled common reference only.
- PASS: proposed FTEU performance page, Europe region row, performance-index row, common-window row, alias tags, canonical breadcrumb, and dated source-batch contents are fully specified.
- PASS: no unresolved High/Medium finding blocks the write; no WARNING requiring confirmation remains. `verification_mode: scheduled-local` and `reviewer_dispatch: not-attempted-by-design` are recorded in this batch header.

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official share-class/alias evidence established passive FTEU ownership; the scheduled-local checklist passed and official EUR versus secondary USD gaps were disclosed.

## FKU — First Trust United Kingdom AlphaDEX Fund

### Identity and classification

- `entity_key: NASDAQ:FKU`; ticker `FKU`; canonical exchange `Nasdaq`; inception `2012-02-14`; total expense ratio `0.80%` as of `2026-05-01`.
- `management_mode: passive-index-tracking`; tracked index `Nasdaq AlphaDEX United Kingdom Index`; return basis `NAV total return` in USD.
- The official prospectus describes FKU as an index fund that normally invests at least 90% of net assets in index securities and is not actively managed. The strategy-aligned benchmark is the Nasdaq AlphaDEX United Kingdom Index; S&P 500 Total Return is retained only as a common reference.
- Primary region: `United Kingdom`; new static region page `[[United Kingdom ETF]]` and canonical performance page `[[ETF_NASDAQ_FKU Performance]]` were created.

### Source map

| Source | URL/path | Use |
|---|---|---|
| First Trust FKU product page | https://www.ftportfolios.com/Retail/Etf/EtfSummary.aspx?Ticker=FKU | identity, index methodology, fee, current NAV/price, holdings, exposures, rolling returns, YTD and risk statistics |
| First Trust Exchange-Traded AlphaDEX Fund II prospectus | https://www.ftportfolios.com/LoadContent/gradkqbz8r4y | passive strategy, index-change disclosure, official 2016-2025 annual-return chart, average annual returns and risk disclosure |
| SEC FKU summary prospectus | https://www.sec.gov/Archives/edgar/data/1510337/000144554626003320/fku_497k.htm | official calendar-year returns and best/worst-quarter disclosure |
| Cached benchmark convention | workflow cache | S&P 500 Total Return calendar rows 2016-2025 in USD with dividends reinvested |

### Raw observations

- Official First Trust product page: FKU is a Nasdaq-listed United Kingdom equity ETF with inception `2012-02-14`, total expense ratio `0.80%` as of `2026-05-01`, and `76` holdings as of `2026-08-14`.
- Current snapshot as of `2026-08-14`: NAV `US$56.53`, closing market price `US$56.69`, premium `+0.33%`, net assets `US$39,567,669`, and 30-day median bid/ask spread `0.57%`.
- Product page month-end performance as of `2026-07-31`: NAV TR `3M 6.09%`, `YTD 10.96%`, `1Y 25.50%`, `3Y 20.53%`, `5Y 9.03%`, `10Y 8.67%`, and since inception `7.86%`. Official Nasdaq AlphaDEX United Kingdom Index rows were `6.73%`, `12.12%`, `26.55%`, `21.94%`, `10.41%`, and `9.88%` for the comparable periods.
- Official 3-year statistics as of `2026-07-31`: standard deviation `15.80%`, beta `1.18`, Sharpe ratio `0.98`, and correlation `0.93`.
- Current sector exposures as of `2026-08-14`: Financials `25.33%`, Industrials `15.49%`, Consumer Discretionary `15.26%`, Consumer Staples `11.55%`, Materials `7.93%`, Information Technology `6.09%`, Energy `5.98%`, and Real Estate `5.30%` among the largest weights.
- Official calendar-year NAV TR rows as of `2025-12-31`: 2016 `-16.08%`, 2017 `25.53%`, 2018 `-16.16%`, 2019 `32.36%`, 2020 `-5.25%`, 2021 `19.10%`, 2022 `-23.52%`, 2023 `20.59%`, 2024 `8.01%`, 2025 `37.60%`.
- Prospectus average annual returns ended `2025-12-31`: FKU `1Y 37.60%`, `5Y 10.30%`, `10Y 6.10%`, since inception `7.40%`; Nasdaq AlphaDEX UK Index `1Y 39.19%`, `5Y 11.66%`, `10Y 7.30%`; Nasdaq UK Index `1Y 35.13%`, `5Y 12.12%`, `10Y 7.47%`; MSCI UK `1Y 35.11%`, `5Y 13.33%`, `10Y 7.83%`.
- The product page and prospectus state that the underlying index changed on `2015-07-14` from the Defined United Kingdom Index to the Nasdaq AlphaDEX United Kingdom Index. The annual history is retained with this continuity caveat.
- Prospectus best quarter was `+23.45%` ending `2022-12-31`; worst quarter was `-40.79%` ending `2020-03-31`. Official daily NAV maximum drawdown and recovery were not disclosed in the reviewed issuer capture.

### Calculations and reconciliation

- Complete 2016-2025 FKU using the official displayed annual rows: `(0.8392 × 1.2553 × 0.8384 × 1.3236 × 0.9475 × 1.1910 × 0.7648 × 1.2059 × 1.0801 × 1.3760) - 1 = 80.82%`; rounded-input CAGR `6.10%`; population annual-return standard deviation `20.95%`; up/down `6/4`; best `2025 +37.60%`; worst `2022 -23.52%`.
- Complete 2021-2025 FKU: cumulative `63.25%`, rounded-input CAGR `10.30%`; cached S&P 500 TR cumulative `96.17%`, CAGR `14.43%`. This is a common-reference comparison, not alpha.
- Cached S&P 500 TR common-window 2016-2025 is `298.33%` cumulative / `14.82%` rounded-input CAGR.
- Official same-date 2026-07-31 YTD tracking comparison: FKU NAV TR `10.96%` versus Nasdaq AlphaDEX United Kingdom Index `12.12%`; this is tracking evidence, not manager-skill evidence.
- The issuer's rolling 10-year average annual `8.67%` as of `2026-07-31` is kept separate from the rounded-input 2016-2025 calendar CAGR `6.10%`.

### Local pre-save checklist

- PASS: ETF identity, Nasdaq exchange, passive classification, tracked index, historical splice, return basis, periods, units, currencies, metric definitions, as-of dates, calculations and source URLs are recorded.
- PASS: official annual NAV rows are separated from the strategy-aligned index and S&P 500 common reference; tracking differences are not labeled alpha; rolling 10-year and calendar-row CAGR are not mixed; current YTD and quotes have separate as-of dates.
- PASS: the 2015 index change, 76-holding exposure snapshot, best/worst quarter and daily NAV drawdown/recovery gap are disclosed; no market-price proxy is labeled NAV evidence.
- PASS: proposed FKU performance page, new United Kingdom region page, region-index row, performance-index rows, dated source-batch contents and one log bullet are fully specified; canonical breadcrumb and `geography/United-Kingdom` tag are present; all planned wikilinks resolve.
- PASS: no unresolved High/Medium finding blocks the write; no WARNING requiring confirmation remains. `verification_mode: scheduled-local` and `reviewer_dispatch: not-attempted-by-design` are recorded in this batch header.

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official passive-index evidence and the scheduled-local checklist passed; FKU artifacts were written with the 2015 index continuity caveat disclosed.

## FEUZ — First Trust Eurozone AlphaDEX ETF

### Identity and classification

- `entity_key: NASDAQ:FEUZ`; ticker `FEUZ`; canonical exchange `Nasdaq`; ISIN `US33737J5056`; inception `2014-10-21`; total expense ratio `0.80%` as of `2026-05-01`.
- `management_mode: passive-index-tracking`; tracked index `Nasdaq AlphaDEX Eurozone Index`; return basis `NAV total return` in USD.
- The official prospectus says FEUZ normally invests at least 90% of net assets in the index and uses an indexing approach. FEUZ is the U.S.-listed Nasdaq ETF; it is not the same security as the UCITS USD London line `LSE:FTEU` used for input alias `FTDPF`.
- Primary region: `Europe`; the existing static region page `[[Europe ETF]]` was updated and a new canonical performance page `[[ETF_NASDAQ_FEUZ Performance]]` was created.

### Source map

| Source | URL/path | Use |
|---|---|---|
| First Trust FEUZ product page | https://www.ftportfolios.com/Retail/Etf/EtfSummary.aspx?Ticker=FEUZ | identity, index methodology, fee, current NAV/price, holdings, exposures, rolling returns, YTD and risk statistics |
| First Trust Exchange-Traded AlphaDEX Fund II prospectus | https://www.ftportfolios.com/LoadContent/gradkqbz8r4y | passive strategy, official 2016-2025 annual-return chart, average annual returns and risk disclosure |
| Cached benchmark convention | workflow cache | S&P 500 Total Return calendar rows 2016-2025 in USD with dividends reinvested |

### Raw observations

- Official First Trust product page: FEUZ is a Nasdaq-listed Eurozone equity ETF with ISIN `US33737J5056`, inception `2014-10-21`, total expense ratio `0.80%` as of `2026-05-01`, and `150` holdings as of `2026-08-13`.
- Current snapshot as of `2026-08-13`: closing NAV `US$68.66`, closing market price `US$68.59`, bid/ask discount `0.07%`, net assets `US$133,878,209`, and 30-day median bid/ask spread `0.60%`.
- Product page month-end performance as of `2026-07-31`: NAV TR `3M 2.50%`, `YTD 12.30%`, `1Y 26.53%`, `3Y 21.31%`, `5Y 10.61%`, `10Y 10.43%`, and since inception `9.39%`. Official Nasdaq AlphaDEX Eurozone Index rows were `2.48%`, `12.30%`, `26.29%`, `21.94%`, `11.24%`, `11.05%`, and `10.00%` for the comparable periods.
- Official 3-year statistics as of `2026-07-31`: standard deviation `15.31%`, beta `0.93`, Sharpe ratio `1.05`, and correlation `0.92`.
- Current country exposures as of `2026-08-13`: Germany `21.12%`, France `20.60%`, Italy `14.44%`, The Netherlands `9.49%`, Spain `9.00%`; sector exposures: Industrials `21.56%`, Financials `12.12%`, Materials `11.67%`, Energy `11.12%`, Utilities `9.15%`, and Consumer Discretionary `8.77%`.
- Official calendar-year NAV TR rows as of `2025-12-31`: 2016 `5.49%`, 2017 `36.19%`, 2018 `-19.82%`, 2019 `21.15%`, 2020 `4.69%`, 2021 `12.90%`, 2022 `-19.65%`, 2023 `15.71%`, 2024 `1.88%`, 2025 `56.57%`.
- Prospectus average annual returns ended `2025-12-31`: FEUZ `1Y 56.57%`, `5Y 10.86%`, `10Y 9.36%`, since inception `8.77%`; Nasdaq AlphaDEX Eurozone Index `1Y 57.52%`, `5Y 11.51%`, `10Y 9.94%`, since inception `9.41%`; Nasdaq Eurozone Index `1Y 41.74%`, `5Y 10.50%`, `10Y 8.93%`; MSCI EMU Index `1Y 40.30%`, `5Y 10.55%`, `10Y 9.00%`.
- Prospectus best quarter was `+23.61%` ending `2022-12-31`; worst quarter was `-29.55%` ending `2020-03-31`. Official daily NAV maximum drawdown and recovery were not disclosed in the reviewed issuer capture.

### Calculations and reconciliation

- Complete 2016-2025 FEUZ using the official displayed annual rows: `(1.0549 × 1.3619 × 0.8018 × 1.2115 × 1.0469 × 1.1290 × 0.8035 × 1.1571 × 1.0188 × 1.5657) - 1 = 144.62%`; rounded-input CAGR `9.36%`; population annual-return standard deviation `22.09%`; up/down `8/2`; best `2025 +56.57%`; worst `2018 -19.82%`.
- Complete 2021-2025 FEUZ: cumulative `67.44%`, rounded-input CAGR `10.86%`; cached S&P 500 TR cumulative `96.17%`, CAGR `14.43%`. This is a common-reference comparison, not alpha.
- Cached S&P 500 TR common-window 2016-2025 is `298.33%` cumulative / `14.82%` rounded-input CAGR.
- Official same-date 2026-07-31 YTD tracking comparison: FEUZ NAV TR `12.30%` versus Nasdaq AlphaDEX Eurozone Index `12.30%`; this is tracking evidence, not manager-skill evidence.
- The issuer's rolling 10-year average annual `10.43%` as of `2026-07-31` is kept separate from the rounded-input 2016-2025 calendar CAGR `9.36%`.

### Local pre-save checklist

- PASS: ETF identity, Nasdaq exchange, ISIN, passive classification, tracked index, return basis, periods, units, currencies, metric definitions, as-of dates, calculations and source URLs are recorded.
- PASS: official annual NAV rows are separated from the strategy-aligned index and S&P 500 common reference; tracking differences are not labeled alpha; rolling 10-year and calendar-row CAGR are not mixed; current YTD and quotes have separate as-of dates.
- PASS: FEUZ is explicitly separated from UCITS FTEU/FTDPF; 150-holding country/sector exposures, best/worst quarter and daily NAV drawdown/recovery gap are disclosed; no market-price proxy is labeled NAV evidence.
- PASS: proposed FEUZ performance page, Europe region row, region-index count, performance-index rows, dated source-batch contents and one log bullet are fully specified; canonical breadcrumb and `geography/Europe` tag are present; all planned wikilinks resolve.
- PASS: no unresolved High/Medium finding blocks the write; no WARNING requiring confirmation remains. `verification_mode: scheduled-local` and `reviewer_dispatch: not-attempted-by-design` are recorded in this batch header.

### trello_handoff

status: PASS
scope: item
durable_write: completed
exhausted: false
confirmation: none
code: durable-write-complete
reason: Official passive-index evidence and the scheduled-local checklist passed; FEUZ artifacts were written with the U.S.-listed versus UCITS FTEU identity distinction disclosed.
