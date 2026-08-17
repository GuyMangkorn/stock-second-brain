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
