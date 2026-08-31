---
type: etf-performance-source-batch
workflow: check-etf-performance
batch_date: 2026-09-01
execution_profile: scheduled-inline
run_id: 2026-09-01-queue-run-2
---

# ETF performance source batch — 2026-09-01 queue run 2

This is the run-scoped evidence packet for the ten oldest eligible queue
cards. The batch uses official issuer or regulatory material first, keeps NAV
total return separate from market-price return, and records secondary values
with `*`. The pre-existing 2026-09-01 FNDF recovery batch is deliberately not
reused because it was dirty before this queue claim.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design

## RODM — Hartford Multifactor Developed Markets (ex-US) ETF

### Identity and proposed durable outputs

- `input_ticker`: `RODM`; `entity_key`: `NYSE Arca:RODM`; `exchange`: NYSE Arca
- Primary region: International; exposure is developed markets ex-US
- `management_mode`: `passive-index`; issuer index: Hartford Risk-Optimized Multifactor Developed Markets (ex-US) Index; Bloomberg `LRODMX`
- Proposed outputs: `wiki/analysis/performance/ETF_NYSE_ARCA_RODM Performance.md` and this source batch

### Evidence and definitions

- Hartford’s official fund page identifies RODM, inception `2015-02-25`, total operating expense `0.29%`, NAV `$42.00`, and net assets `$1,650,684,642`, with the price and assets as of `2026-08-28`.
- The same official page reports NAV total return as of `2026-07-31`: YTD `14.01%`, 1-year `26.64%`, 3-year annualized `19.47%`, 5-year annualized `10.30%`, 10-year annualized `9.07%`, and since inception annualized `8.02%`. Market-price returns are retained separately in the page source context and are not mixed into the NAV series.
- The official 2025 summary prospectus supplies calendar-year NAV returns for `2016-2024`. AAII supplies a `2025` NAV return of `34.20%*` as of `2026-06-30`; it is a secondary proxy, not an official prospectus row.
- Return currency is USD. Total return means the issuer’s NAV performance convention; distributions and earnings are reflected according to the official performance presentation.
- The S&P 500 Total Return rows are the project’s cached USD common reference for complete calendar years `2016-2025`; they are not RODM’s management benchmark.

### Candidate claims, calculations, and gaps

| Year | RODM NAV TR | S&P 500 TR (USD reference) | Evidence |
|---|---:|---:|---|
| 2016 | 3.25% | 11.96% | Hartford summary prospectus |
| 2017 | 25.75% | 21.83% | Hartford summary prospectus |
| 2018 | -9.74% | -4.38% | Hartford summary prospectus |
| 2019 | 17.10% | 31.49% | Hartford summary prospectus |
| 2020 | -0.22% | 18.40% | Hartford summary prospectus |
| 2021 | 10.82% | 28.71% | Hartford summary prospectus |
| 2022 | -14.37% | -18.11% | Hartford summary prospectus |
| 2023 | 15.77% | 26.29% | Hartford summary prospectus |
| 2024 | 8.07% | 25.02% | Hartford summary prospectus |
| 2025 | 34.20%* | 17.88% | AAII secondary proxy |

Using `Π(1 + annual_return) - 1` on the ten displayed rounded rows gives a
`118.17%` cumulative return and `8.11%` rounded-input CAGR. Because 2025 is a
secondary proxy, both calculations are approximations and must not replace
Hartford’s official rolling 10-year NAV CAGR of `9.07%`. The displayed source
window has 7 up years and 3 down years; best is 2025 `34.20%*`, worst is 2022
`-14.37%`.

- Official risk fields to carry into the page: 5-year standard deviation `13.94%`, beta `0.87`, Sharpe `0.51`, information ratio `0.16`, and up/down capture `91.55% / 84.16%`, all as of `2026-07-31`.
- No verified daily NAV series was collected for a fresh maximum drawdown or recovery calculation; disclose `ไม่พบข้อมูลที่ยืนยันได้` for those fields.

### Sources

1. [Hartford official RODM fund page](https://www.hartfordfunds.com/funds/rodm.html)
2. [Hartford RODM 2025 summary prospectus](https://www.hartfordfunds.com/dam/en/docs/pub/funddocuments/regulatorydocument/summaryprospectus/SUM-RODM.pdf)
3. [AAII RODM fund data](https://www.aaii.com/fund/ticker/RODM)
4. [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/); cached project convention is USD total return through `2025-12-31`

### Scheduled-local pre-save review

- Identity, exchange, return basis, issuer benchmark, currency, units, source dates, annual rows, current snapshot, calculations, and unresolved drawdown gaps are recorded above.
- Proposed page contents: bottom line; performance check with identity/inception/expense/current NAV TR; 2016-2025 annual table; up/down years; risk read-through; source links; and the source-batch link.
- Local review result: `PASS`; no high or medium finding remains; no confirmation is required.

## IMFL — Invesco International Developed Dynamic Multifactor ETF

### Identity and proposed durable outputs

- `input_ticker`: `IMFL`; `entity_key`: `Cboe BZX:IMFL`; exchange: Cboe BZX
- Primary region: International; developed markets ex-US multifactor equity exposure
- `management_mode`: `passive-index`; tracked index: `FTSE Developed ex US Invesco Dynamic Multifactor Index`; official comparison benchmark: `FTSE Developed ex US Index`
- Proposed outputs: `wiki/analysis/performance/ETF_CBOE_BZX_IMFL Performance.md` and this source batch

### Evidence and definitions

- Invesco’s official product page identifies IMFL as an indexed equity ETF launched `2021-02-24`, using monthly rebalanced low-volatility, momentum, quality, size, and value factors. Management fee/expense ratio is `0.34%`; exchange is Cboe BZX.
- The official Invesco factsheet as of `2026-03-31` reports NAV total return YTD `6.43%`, 1-year `31.64%`, 3-year annualized `14.31%`, 5-year `7.97%`, and since inception annualized `8.46%`. Its benchmark fields are `FTSE Developed ex US Index`: `0.18%, 26.88%, 15.05%, 8.32%, 8.22%` for the same periods.
- The same official factsheet supplies complete NAV calendar rows for `2022-2025`: `-16.71%, 24.96%, -3.70%, 30.79%`. No complete 2021 row is claimed because inception was in February 2021.
- Official factsheet portfolio fields as of `2026-03-31` include `1,146` holdings, P/E `17.01`, P/B `2.37`, and ROE `12.12%`.
- The official product-page performance widget was not text-readable for the current date. ETF Central reports current YTD `20.09%*` as of `2026-08-25`; this is a secondary proxy and is not presented as official. Current official NAV/YTD is therefore `ไม่พบข้อมูลที่ยืนยันได้` in the captured official text.
- Return currency is USD. S&P 500 Total Return is only a cached USD common reference, not the official FTSE comparison benchmark.

### Candidate claims, calculations, and gaps

| Year | IMFL NAV TR | S&P 500 TR (USD reference) | Evidence |
|---|---:|---:|---|
| 2022 | -16.71% | -18.11% | Invesco factsheet |
| 2023 | 24.96% | 26.29% | Invesco factsheet |
| 2024 | -3.70% | 25.02% | Invesco factsheet |
| 2025 | 30.79% | 17.88% | Invesco factsheet |

Applying `Π(1 + annual_return) - 1` to the four official rounded rows gives
`31.09%` cumulative and `7.00%` rounded-input CAGR. The official rolling
since-inception annualized return is `8.46%` as of `2026-03-31`; the windows
and endpoints differ. The annual window has 2 up years and 2 down years; best
is 2025 `30.79%`, worst is 2022 `-16.71%`.

- Official 2025 NAV return `30.79%` exceeded the FTSE Developed ex US Index benchmark `34.22%` by `-3.43 pp`; 2023 IMFL `24.96%` exceeded benchmark `18.06%` by `+6.90 pp`. These are benchmark differences, not alpha.
- A fresh daily-NAV maximum drawdown and recovery calculation is `ไม่พบข้อมูลที่ยืนยันได้`.

### Sources

1. [Invesco official IMFL product page](https://www.invesco.com/us/en/financial-products/etfs/invesco-international-developed-dynamic-multifactor-etf.html)
2. [Invesco IMFL official factsheet](https://www.invesco.com/content/dam/invesco/us/en/product-documents/etf/fact-sheet/imfl-invesco-international-developed-dynamic-multifactor-etf-fact-sheet.pdf)
3. [ETF Central IMFL data](https://www.etfcentral.com/fund/IMFL)
4. [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/); cached project convention is USD total return through `2025-12-31`

### Scheduled-local pre-save review

- Identity, exchange, indexed factor process, tracked index, comparison benchmark, return basis, source dates, annual rows, current-YTD limitation, benchmark arithmetic, calculations, and unresolved drawdown gap are recorded above.
- Proposed page contents: bottom line; performance check; 2022-2025 annual table; up/down years; risk read-through; and source links.
- Local review result: `PASS`; no high or medium finding remains; no confirmation is required.

## IMTM — iShares MSCI Intl Momentum Factor ETF

### Identity and proposed durable outputs

- `input_ticker`: `IMTM`; `entity_key`: `NYSE Arca:IMTM`; exchange: NYSE Arca
- Primary region: International; developed markets ex-US momentum-factor exposure
- `management_mode`: `passive-index`; issuer benchmark: `MSCI World ex USA Momentum Index (Net)`
- Proposed outputs: `wiki/analysis/performance/ETF_NYSE_ARCA_IMTM Performance.md` and this source batch

### Evidence and definitions

- The official iShares product page identifies IMTM as an equity ETF launched `2015-01-13`, tracking `MSCI World ex USA Momentum Index (Net)`, with expense ratio `0.30%`, NAV `$53.18`, net assets `$4,254,713,180`, and `302` holdings as of `2026-08-28`.
- The official page reports NAV total-return YTD `12.21%` as of `2026-08-28`; closing price `$53.32` is kept separate.
- The official June 2026 factsheet supplies calendar NAV rows for `2021-2025`: `6.53%, -16.65%, 13.68%, 12.25%, 34.43%`, and rolling NAV annualized returns as of `2026-06-30`: 1-year `22.25%`, 3-year `21.07%`, 5-year `10.65%`, 10-year `10.71%`, and since inception `9.51%`.
- Official factsheet risk fields include beta `0.73`, standard deviation `13.13%`, P/E `21.19`, and P/B `2.56` as of `2026-06-30`; the current page reports beta `0.74` and standard deviation `13.31%` in the latest snapshot.
- Return currency is USD. S&P 500 Total Return is only a cached USD common reference, not IMTM’s issuer benchmark.

### Candidate claims, calculations, and gaps

| Year | IMTM NAV TR | S&P 500 TR (USD reference) | Evidence |
|---|---:|---:|---|
| 2021 | 6.53% | 28.71% | iShares factsheet |
| 2022 | -16.65% | -18.11% | iShares factsheet |
| 2023 | 13.68% | 26.29% | iShares factsheet |
| 2024 | 12.25% | 25.02% | iShares factsheet |
| 2025 | 34.43% | 17.88% | iShares factsheet |

Applying `Π(1 + annual_return) - 1` to the five official rounded rows gives
`52.32%` cumulative and `8.78%` rounded-input CAGR. The official rolling
5-year NAV CAGR is `10.65%` as of `2026-06-30`; the endpoint/window differs
from the calendar-row calculation. The annual window has 4 up years and 1 down
year; best is 2025 `34.43%`, worst is 2022 `-16.65%`.

- A fresh daily-NAV maximum drawdown and recovery calculation is `ไม่พบข้อมูลที่ยืนยันได้`.

### Sources

1. [iShares official IMTM product page](https://www.ishares.com/us/products/271538/ishares-msci-intl-momentum-factor-etf)
2. [iShares IMTM official factsheet](https://www.ishares.com/us/literature/fact-sheet/imtm-ishares-msci-intl-momentum-factor-etf-fund-fact-sheet-en-us.pdf)
3. [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/); cached project convention is USD total return through `2025-12-31`

### Scheduled-local pre-save review

- Identity, exchange, momentum-factor index, return basis, currency, source dates, annual rows, current snapshot, rolling comparison, risk fields, calculation, and unresolved drawdown gap are recorded above.
- Proposed page contents: bottom line; performance check; 2021-2025 annual table; up/down years; risk read-through; and source links.
- Local review result: `PASS`; no high or medium finding remains; no confirmation is required.

## IVLU — iShares MSCI Intl Value Factor ETF

### Identity and proposed durable outputs

- `input_ticker`: `IVLU`; `entity_key`: `NYSE Arca:IVLU`; exchange: NYSE Arca
- Primary region: International; developed markets ex-US value-factor exposure
- `management_mode`: `passive-index`; issuer benchmark: `MSCI World ex USA Enhanced Value Index (Net)`
- Proposed outputs: `wiki/analysis/performance/ETF_NYSE_ARCA_IVLU Performance.md` and this source batch

### Evidence and definitions

- The official iShares product page identifies IVLU as an equity ETF launched `2015-06-16`, tracking `MSCI World ex USA Enhanced Value Index (Net)`, with expense ratio `0.31%`, NAV `$44.08`, net assets `$4,584,495,178`, and `348` holdings as of `2026-08-28`.
- The official page reports NAV total-return YTD `17.91%` as of `2026-08-28`; market closing price was `$44.23` and is kept separate.
- The official June 2026 factsheet supplies calendar NAV rows for `2021-2025`: `15.32%, -5.80%, 19.99%, 6.75%, 46.24%`, and rolling NAV annualized returns as of `2026-06-30`: 1-year `32.00%`, 3-year `23.09%`, 5-year `14.77%`, 10-year `11.53%`, and since inception `8.47%`.
- Official factsheet risk fields include standard deviation `12.51%`, beta `0.50`, P/E `14.23`, and P/B `1.36` as of `2026-06-30`; current page standard deviation is `12.50%` and beta `0.49` in the latest snapshot.
- Return currency is USD. S&P 500 Total Return is only a cached USD common reference, not IVLU’s issuer benchmark.

### Candidate claims, calculations, and gaps

| Year | IVLU NAV TR | S&P 500 TR (USD reference) | Evidence |
|---|---:|---:|---|
| 2021 | 15.32% | 28.71% | iShares factsheet |
| 2022 | -5.80% | -18.11% | iShares factsheet |
| 2023 | 19.99% | 26.29% | iShares factsheet |
| 2024 | 6.75% | 25.02% | iShares factsheet |
| 2025 | 46.24% | 17.88% | iShares factsheet |

Applying `Π(1 + annual_return) - 1` to the five official rounded rows gives
`103.49%` cumulative and `15.27%` rounded-input CAGR. The official rolling
5-year CAGR is `14.77%` as of `2026-06-30`; the table and rolling endpoint are
different windows. The annual window has 4 up years and 1 down year; best is
2025 `46.24%`, worst is 2022 `-5.80%`.

- A fresh daily-NAV maximum drawdown and recovery calculation is `ไม่พบข้อมูลที่ยืนยันได้`.

### Sources

1. [iShares official IVLU product page](https://www.ishares.com/us/products/275382/IVLU)
2. [iShares IVLU official factsheet](https://www.ishares.com/us/literature/fact-sheet/ivlu-ishares-msci-intl-value-factor-etf-fund-fact-sheet-en-us.pdf)
3. [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/); cached project convention is USD total return through `2025-12-31`

### Scheduled-local pre-save review

- Identity, exchange, value-factor index, return basis, currency, source dates, annual rows, current snapshot, rolling comparison, risk fields, calculation, and unresolved drawdown gap are recorded above.
- Proposed page contents: bottom line; performance check; 2021-2025 annual table; up/down years; risk read-through; and source links.
- Local review result: `PASS`; no high or medium finding remains; no confirmation is required.

## QEFA — State Street SPDR MSCI EAFE StrategicFactors ETF

### Identity and proposed durable outputs

- `input_ticker`: `QEFA`; `entity_key`: `NYSE Arca:QEFA`; exchange: NYSE Arca
- Primary region: International; developed markets ex-US/Canada strategic-factor exposure
- `management_mode`: `passive-index`; issuer benchmark: `MSCI EAFE Factor Mix A-Series Index`
- Proposed outputs: `wiki/analysis/performance/ETF_NYSE_ARCA_QEFA Performance.md` and this source batch

### Evidence and definitions

- State Street’s official product page identifies QEFA, inception `2014-06-04`, base currency USD, expense ratio `0.30%`, NAV `$101.49`, and AUM `$1,075.78M`, with the latest price/assets snapshot as of `2026-08-27`. The strategy combines low-volatility, quality, and value factors.
- Official NAV total return as of `2026-07-31`: YTD `11.24%`, 1-year `23.04%`, 3-year annualized `14.90%`, 5-year annualized `8.58%`, 10-year annualized `8.92%`, and since inception annualized `7.07%`. Official benchmark fields are `11.20%, 23.16%, 14.94%, 8.63%, 8.97%, 7.13%` for the same periods.
- The official June 2026 factsheet confirms the index methodology, `0.30%` expense ratio, and `643` holdings as of `2026-06-30`. It does not provide the full calendar-year table in the captured extract.
- AAII provides rounded calendar NAV rows used only as secondary proxies: `2016-2025` equals `0.3%, 23.9%, -10.2%, 21.9%, 7.0%, 12.4%, -14.0%, 17.3%, 2.7%, 28.8%` as of `2026-07-31`.
- Return currency is USD. The S&P 500 Total Return rows are the project’s cached USD common reference, not QEFA’s issuer benchmark.

### Candidate claims, calculations, and gaps

| Year | QEFA NAV TR | S&P 500 TR (USD reference) | Evidence |
|---|---:|---:|---|
| 2016 | 0.3%* | 11.96% | AAII secondary proxy |
| 2017 | 23.9%* | 21.83% | AAII secondary proxy |
| 2018 | -10.2%* | -4.38% | AAII secondary proxy |
| 2019 | 21.9%* | 31.49% | AAII secondary proxy |
| 2020 | 7.0%* | 18.40% | AAII secondary proxy |
| 2021 | 12.4%* | 28.71% | AAII secondary proxy |
| 2022 | -14.0%* | -18.11% | AAII secondary proxy |
| 2023 | 17.3%* | 26.29% | AAII secondary proxy |
| 2024 | 2.7%* | 25.02% | AAII secondary proxy |
| 2025 | 28.8%* | 17.88% | AAII secondary proxy |

Applying `Π(1 + annual_return) - 1` to the ten secondary rounded rows gives
`118.32%` cumulative and `8.12%` rounded-input CAGR. The official rolling
10-year NAV CAGR is `8.92%` as of `2026-07-31`; the table is not a substitute
for that issuer field. The proxy window has 8 up years and 2 down years; best
is 2025 `28.8%*`, worst is 2022 `-14.0%*`.

- Benchmark-relative official rolling fields are close but mixed: QEFA trails the issuer benchmark by `-0.12 pp` over 1 year and `-0.04 pp` over 3 years, and leads by `+0.01 pp` over 10 years; rounding and different data dates matter.
- A fresh daily-NAV maximum drawdown and recovery calculation is `ไม่พบข้อมูลที่ยืนยันได้`.

### Sources

1. [State Street official QEFA product page](https://www.ssga.com/us/en/individual/etfs/state-street-spdr-msci-eafe-strategicfactors-etf-qefa)
2. [State Street QEFA factsheet](https://www.ssga.com/library-content/products/factsheets/etfs/us/factsheet-us-en-qefa.pdf)
3. [AAII QEFA data](https://www.aaii.com/etfs/summary?ticker=QEFA)
4. [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/); cached project convention is USD total return through `2025-12-31`

### Scheduled-local pre-save review

- Identity, exchange, return basis, issuer benchmark, factor methodology, currency, source dates, current official fields, secondary annual rows, calculations, and unresolved drawdown gap are recorded above.
- Proposed page contents: bottom line; performance check; 2016-2025 secondary annual table; up/down years; risk read-through; and source links.
- Local review result: `PASS`; no high or medium finding remains; no confirmation is required.

## VEXNF / VIDY — Vanguard FTSE Developed ex North America High Dividend Yield Index ETF

### Identity and proposed durable outputs

- `input_ticker`: `VEXNF` is an OTC alias; official Canadian listing used is `TSX:VIDY`
- Primary region: International; the underlying index excludes Canada and the United States
- `management_mode`: `passive-index`; issuer benchmark: `FTSE Developed ex North America High Dividend Yield Index`
- Proposed outputs: `wiki/analysis/performance/ETF_TSX_VIDY Performance.md` and this source batch

### Evidence and definitions

- Vanguard Canada’s official product page identifies VIDY as an equity ETF using passive full replication, with inception `2018-08-21`, management fee `0.28%`, and page-displayed RFG/MER `0.31%`. The official ETF Facts dated `2026-07-16` reports MER `0.32%`; this total-expense figure is used in the page while the page’s alternate display is retained as a note.
- The official page reports CAD NAV `$48.3366` and market price `$48.45` as of `2026-08-28`, with `629` stocks and standard deviation `9.23%` as of `2026-07-31`.
- The official ETF Facts supplies NAV total-return calendar rows for `2019-2025`: `12.3%, -2.9%, 14.0%, 1.6%, 15.1%, 16.1%, 34.5%`, plus since-inception value growth of `$1,000` to `$2,395` and annual compound return `11.89%` through `2026-05-31`.
- Official current YTD was not text-readable on the product page. Cboe Canada/ETF Market reports `19.37%*` as of `2026-08-21`; it is a secondary proxy. A separate secondary source showed `19.61%` as of July 31, so the page preserves the source limitation rather than presenting either as official.
- Return currency is CAD. The S&P 500 Total Return rows are USD-only common reference data and are not a currency-aligned benchmark for VIDY.

### Candidate claims, calculations, and gaps

| Year | VIDY NAV TR (CAD) | S&P 500 TR (USD reference) | Evidence |
|---|---:|---:|---|
| 2019 | 12.3% | 31.49% | Vanguard ETF Facts |
| 2020 | -2.9% | 18.40% | Vanguard ETF Facts |
| 2021 | 14.0% | 28.71% | Vanguard ETF Facts |
| 2022 | 1.6% | -18.11% | Vanguard ETF Facts |
| 2023 | 15.1% | 26.29% | Vanguard ETF Facts |
| 2024 | 16.1% | 25.02% | Vanguard ETF Facts |
| 2025 | 34.5% | 17.88% | Vanguard ETF Facts |

Applying `Π(1 + annual_return) - 1` to the seven official rounded CAD rows gives
`127.00%` cumulative and `12.42%` rounded-input CAGR. The official since-
inception ETF Facts figure is `11.89%` annual compound through `2026-05-31`;
the two calculations use different windows and should not be conflated. The
2019-2025 window has 6 up years and 1 down year; best is 2025 `34.5%`, worst is
2020 `-2.9%`.

- A fresh daily-NAV maximum drawdown and recovery calculation is `ไม่พบข้อมูลที่ยืนยันได้`.
- Underlying exposure, CAD return currency, and USD reference currency must remain explicit in any comparison.

### Sources

1. [Vanguard Canada official VIDY product page](https://www.vanguard.ca/fr/product/etf/equity/9742/vanguard-ftse-developed-ex-north-america-high-dividend-yield-index-etf)
2. [Vanguard VIDY official ETF Facts](https://fund-docs.vanguard.com/VIDY_FTSE_Developed_ex_North_America_High_Dividend_Yield_Index_ETF_ETF_9742_EN_FACTS.pdf)
3. [Cboe Canada / ETF Market VIDY data](https://etfmarket.cboe.com/canada/en/fund/VIDY)
4. [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/); cached project convention is USD total return through `2025-12-31`

### Scheduled-local pre-save review

- Alias mapping, official exchange, underlying geography, CAD return basis, fee-definition conflict, source dates, annual rows, current NAV, secondary YTD limitation, calculations, and unresolved drawdown gap are recorded above.
- Proposed page contents: alias mapping; bottom line; performance check; 2019-2025 annual table; up/down years; risk read-through; and source links.
- Local review result: `PASS`; no high or medium finding remains; no confirmation is required.

## WTTHF / WTCH — State Street SPDR MSCI World Technology UCITS ETF

### Identity and proposed durable outputs

- `input_ticker`: `WTTHF` is an OTC alias; official primary listing used is `Euronext Amsterdam:WTCH` (ISIN `IE00BYTRRD19`)
- Primary region: International; global developed-market information technology exposure
- `management_mode`: `passive-index`; issuer benchmark: `MSCI World Information Technology 35/20 Capped Index`
- Proposed outputs: `wiki/analysis/performance/ETF_EURONEXT_AMSTERDAM_WTCH Performance.md` and this source batch

### Evidence and definitions

- State Street’s official product page identifies the fund as accumulating, base currency USD, with fund inception `2016-04-29`, performance inception `2009-02-28` through a linked predecessor history, TER `0.30%`, NAV `$271.16` as of `2026-08-28`, AUM `$1,239.66M`, and `135` holdings as of `2026-08-27`.
- Official net NAV performance as of `2026-07-31`: YTD `16.31%`, 1-year `27.07%`, 3-year annualized `26.94%`, 5-year annualized `17.45%`, 10-year annualized `22.73%`, and since performance inception annualized `20.55%`; corresponding issuer-index returns are `16.55%, 27.49%, 27.17%, 17.64%, 22.95%, 20.82%`.
- Official calendar-year net NAV rows are `2016-2025`: `11.30%, 37.94%, -2.74%, 47.39%, 43.31%, 29.62%, -30.85%, 53.34%, 32.71%, 23.18%`. The 2016 row is marked `†` because State Street says the pre-May 2016 history is linked to a predecessor fund; it is not treated as a clean full live-ETF year.
- Return currency is USD for performance even though the primary Euronext listing is EUR; market-price/listing-currency returns remain separate.
- Official risk fields include 3-year standard deviation `21.61%` and tracking error `0.08%`, both as of `2026-07-31`.
- The S&P 500 Total Return rows are the project’s cached USD common reference, not the sector strategy’s issuer benchmark.

### Candidate claims, calculations, and gaps

| Year | WTCH NAV TR | S&P 500 TR (USD reference) | Evidence |
|---|---:|---:|---|
| 2016 | 11.30%† | 11.96% | State Street linked/predecessor history |
| 2017 | 37.94% | 21.83% | State Street official table |
| 2018 | -2.74% | -4.38% | State Street official table |
| 2019 | 47.39% | 31.49% | State Street official table |
| 2020 | 43.31% | 18.40% | State Street official table |
| 2021 | 29.62% | 28.71% | State Street official table |
| 2022 | -30.85% | -18.11% | State Street official table |
| 2023 | 53.34% | 26.29% | State Street official table |
| 2024 | 32.71% | 25.02% | State Street official table |
| 2025 | 23.18% | 17.88% | State Street official table |

Applying the formula to complete live/official rows `2017-2025` gives
`536.70%` cumulative and `22.84%` rounded-input CAGR. The current official
rolling 10-year CAGR is `22.73%`; the 2016 linked row is shown only for context
and is excluded from the complete-live calculation. The 2017-2025 window has 7
up years and 2 down years; best is 2023 `53.34%`, worst is 2022 `-30.85%`.

- A fresh daily-NAV maximum drawdown and recovery calculation is `ไม่พบข้อมูลที่ยืนยันได้`; the 2022 annual loss is not a substitute for max drawdown.

### Sources

1. [State Street official WTCH product page](https://www.ssga.com/uk/en_gb/institutional/etfs/state-street-spdr-msci-world-technology-ucits-etf-wtch-na)
2. [State Street WTCH factsheet](https://www.ssga.com/library-content/products/factsheets/etfs/emea/factsheet-emea-en_gb-wtch-na.pdf)
3. [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/); cached project convention is USD total return through `2025-12-31`

### Scheduled-local pre-save review

- OTC alias mapping, official primary listing, predecessor-history caveat, return basis, currency, benchmark, source dates, annual rows, current snapshot, risk fields, calculations, and unresolved drawdown gap are recorded above.
- Proposed page contents: alias/listing normalization; bottom line; performance check; 2016-2025 table; up/down years; risk read-through; and source links.
- Local review result: `PASS`; no high or medium finding remains; no confirmation is required.

## DIHP — Dimensional International High Profitability ETF

### Identity and proposed durable outputs

- `input_ticker`: `DIHP`; `entity_key`: `Cboe BZX:DIHP`; exchange: Cboe BZX
- Primary region: International; long-only non-US large-company profitability strategy
- `management_mode`: `active-equity-long-only`; `active_process`: systematic-factor; management benchmark: `MSCI World ex USA Index (net dividends)`
- Proposed outputs: `wiki/analysis/performance/ETF_CBOE_BZX_DIHP Performance.md` and this source batch

### Evidence and definitions

- The official SEC summary prospectus identifies DIHP as an actively managed, long-only ETF seeking long-term capital appreciation through high-profitability non-US companies; fund inception is `2022-03-23`. The prospectus benchmark is `MSCI World ex USA Index (net dividends)`.
- The SEC prospectus reports official NAV calendar returns of `18.93%` in 2023, `0.78%` in 2024, and `27.87%` in 2025. It reports 2025 1-year annualized NAV return `27.87%` versus benchmark `31.85%`, and since-inception annualized NAV return `8.90%` versus benchmark `10.92%` through `2025-12-31`.
- The official Dimensional fund table captured as of `2026-08-18` reports NAV `$35.25`, YTD `22.33%`, 1-year `13.67%`, since-inception annualized `10.12%`, and expense ratio `0.27%`.
- Return currency is USD. NAV total return is kept separate from market-price return. Because inception was in March 2022, no complete 2022 calendar-year row is claimed.
- The S&P 500 Total Return rows are the project’s cached USD common reference, not the strategy-aligned management benchmark.

### Candidate claims, calculations, and gaps

| Year | DIHP NAV TR | S&P 500 TR (USD reference) | Evidence |
|---|---:|---:|---|
| 2023 | 18.93% | 26.29% | SEC summary prospectus |
| 2024 | 0.78% | 25.02% | SEC summary prospectus |
| 2025 | 27.87% | 17.88% | SEC summary prospectus |

Applying `Π(1 + annual_return) - 1` to the three complete official rows gives
`53.26%` cumulative and `15.30%` rounded-input CAGR. All three complete rows are
positive; the lowest positive year is 2024 `0.78%` and the highest is 2025
`27.87%`. This short window must not be treated as a mature track record.

- Active evidence is mixed: 2025 underperformed the official management benchmark by `-3.98 pp`, and since inception through `2025-12-31` underperformed by `-2.02 pp`. This is arithmetic excess return, not alpha, and is insufficient to infer persistent manager skill.
- SEC risk fields to carry into the page: highest quarter `10.91%` (quarter ended `2023-12-31`) and lowest quarter `-8.16%` (quarter ended `2024-12-31`). A fresh daily-NAV maximum drawdown and recovery calculation is `ไม่พบข้อมูลที่ยืนยันได้`.

### Sources

1. [SEC DIHP summary prospectus](https://www.sec.gov/Archives/edgar/data/1816125/000181612526000046/R7.htm)
2. [Dimensional official DIHP product page](https://www.dimensional.com/us-en/funds/dihp/international-high-profitability-etf)
3. [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/); cached project convention is USD total return through `2025-12-31`

### Scheduled-local pre-save review

- Active classification, management benchmark, track-record maturity, return basis, currency, source dates, annual rows, current snapshot, benchmark-relative calculations, and risk gaps are recorded above.
- Proposed page contents: bottom line; performance check; 2023-2025 annual table; up/down years; risk read-through; active management read-through; and source links.
- Local review result: `PASS`; no high or medium finding remains; no confirmation is required.

## ISMVF / IWVL — iShares Edge MSCI World Value Factor UCITS ETF

### Identity and proposed durable outputs

- `input_ticker`: `ISMVF` is an OTC alias; official USD share class/listing used for the performance record is `LSE:IWVL`
- Primary region: International; developed-world value-factor exposure
- Proposed outputs: `wiki/analysis/performance/ETF_LSE_IWVL Performance.md` and this source batch

### Evidence and definitions

- The official iShares product page identifies the fund as equity, physical/replicated, accumulating, domiciled in Ireland, with share-class launch `2014-10-03`, benchmark `MSCI World Enhanced Value Index (Net)`, TER `0.25%`, NAV `$81.52`, and net assets `$7,208,692,355`, with the latest price/assets snapshot as of `2026-08-28`.
- The official product page reports NAV total return YTD `36.23%` as of `2026-08-28`. Its performance convention reinvests gross income where applicable; market-price performance is separate.
- The official July 2026 factsheet supplies calendar-year NAV/share-class returns for `2016-2025`: `8.14%, 22.16%, -13.90%, 19.13%, -3.93%, 20.03%, -9.96%, 19.41%, 5.25%, 39.63%`.
- Return currency is USD for the selected LSE listing. Official factsheet risk data include 3-year beta `0.998` and standard deviation `16.00%` as of `2026-07-31`, with `399` holdings in the current product snapshot.
- The S&P 500 Total Return rows are the project’s cached USD common reference for `2016-2025`, not the fund’s issuer benchmark.

### Candidate claims, calculations, and gaps

| Year | IWVL NAV TR | S&P 500 TR (USD reference) | Evidence |
|---|---:|---:|---|
| 2016 | 8.14% | 11.96% | iShares factsheet |
| 2017 | 22.16% | 21.83% | iShares factsheet |
| 2018 | -13.90% | -4.38% | iShares factsheet |
| 2019 | 19.13% | 31.49% | iShares factsheet |
| 2020 | -3.93% | 18.40% | iShares factsheet |
| 2021 | 20.03% | 28.71% | iShares factsheet |
| 2022 | -9.96% | -18.11% | iShares factsheet |
| 2023 | 19.41% | 26.29% | iShares factsheet |
| 2024 | 5.25% | 25.02% | iShares factsheet |
| 2025 | 39.63% | 17.88% | iShares factsheet |

Applying `Π(1 + annual_return) - 1` to the ten official rounded rows gives
`146.88%` cumulative and `9.46%` rounded-input CAGR. The official factsheet’s
rolling 10-year field is not needed for this complete annual-row calculation;
the page will retain the current official YTD and latest risk fields. The
window has 7 up years and 3 down years; best is 2025 `39.63%`, worst is 2018
`-13.90%`.

- A fresh maximum drawdown and recovery calculation from daily NAV data was not assembled; disclose `ไม่พบข้อมูลที่ยืนยันได้`.
- The OTC alias-to-LSE mapping is an identity normalization, not a return adjustment; listing currency and share-class details remain explicit.

### Sources

1. [iShares official IWVL product page](https://www.ishares.com/uk/professionals/en/products/270048/ishares-msci-world-value-factor-ucits-etf?shortLocale=en_GB)
2. [iShares IWVL July 2026 factsheet](https://www.ishares.com/uk/professional/en/literature/fact-sheet/iwvl-ishares-edge-msci-world-value-factor-ucits-etf-fund-fact-sheet-en-gb.pdf)
3. [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/); cached project convention is USD total return through `2025-12-31`

### Scheduled-local pre-save review

- Identity alias, official exchange/listing, return basis, benchmark, currency, units, source dates, annual rows, current snapshot, calculations, and unresolved drawdown gap are recorded above.
- Proposed page contents: alias mapping; bottom line; performance check; 2016-2025 annual table; up/down years; risk read-through; and source links.
- Local review result: `PASS`; no high or medium finding remains; no confirmation is required.
