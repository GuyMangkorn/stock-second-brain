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
