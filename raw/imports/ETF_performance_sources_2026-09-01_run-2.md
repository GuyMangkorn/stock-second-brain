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
