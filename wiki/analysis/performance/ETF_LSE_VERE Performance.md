---
type: etf-performance
instrument_type: ETF
entity_key: LSE:VERE
input_ticker: VGRDF
ticker: VERE
exchange: London Stock Exchange
fund: Vanguard FTSE Developed Europe ex UK UCITS ETF (EUR) Accumulating
tracked_index: FTSE Developed Europe ex U.K. Index
benchmark: S&P 500 Total Return
management_mode: passive-index-tracking
updated: 2026-08-19
performance_as_of: 2025-12-31
rolling_10y_as_of: 2026-07-31
current_ytd_as_of: 2026-07-31
price_nav_as_of: 2026-07-27
fund_facts_as_of: 2026-07-31
source_batch: raw/imports/ETF_performance_sources_2026-08-19.md
return_basis: NAV total return; secondary calendar rows marked *; dividends reinvested; net of expenses
return_currency: EUR
tags:
  - analysis/etf-performance
  - ticker/VERE
  - ticker/VGRDF
  - geography/Europe
---

# VERE Performance

> Navigation: [[ETF Region Index]] → [[Europe ETF]] → [[ETF Performance Index]]

## Bottom line

VGRDF เป็น OTC USD input alias ของ official London Stock Exchange USD listing
LSE:VERE สำหรับ Vanguard FTSE Developed Europe ex UK UCITS ETF (EUR)
Accumulating (ISIN IE00BK5BQY34). Fund เป็น passive physical index tracker และ
official NAV Total Return YTD ล่าสุดคือ +11.54% ณ 31 ก.ค. 2026. Secondary
dividend-adjusted calendar proxy ปี 2021-2025 compound ได้ +66.11%* หรือ
10.68%* ต่อปี เทียบกับ S&P 500 TR USD +96.17% / 14.43% แต่ไม่ทำ
cross-currency excess-return claim. มี 4 ปีบวก / 1 ปีลบ; best 2025 +21.22%*,
worst 2022 -12.43%*.

## Performance check

- entity_key: LSE:VERE; input_ticker: VGRDF; official Vanguard maps the USD London Stock Exchange line to ticker VERE; ISIN IE00BK5BQY34; share-class inception 23 Jul 2019; listing 25 Jul 2019.
- Classification: passive-index / physical replication; fund tracks FTSE Developed Europe ex U.K. Index, large- and mid-cap developed European stocks excluding the UK; accumulating share class reinvests dividends.
- Metric: NAV Total Return including reinvested dividends/capital gains and fund expenses, EUR. Official factsheet performance is NAV-to-NAV with gross income invested, net of expenses.
- Issuer benchmark: FTSE Developed Europe ex U.K. Index. The S&P 500 Total Return table is USD/dividends reinvested common reference, not a directly comparable EUR excess-return benchmark.
- OCF: 0.10%; official rolling NAV TR as of 31 Jul 2026: YTD 11.54%, 1Y 22.04%, 3Y 14.04%, 5Y 9.52%, since inception 10.59%. Issuer 10-year field is not applicable because the share class launched 23 Jul 2019.
- Official current NAV: EUR 60.4211 at closure 27 Jul 2026; current holdings 417 and 3Y/5Y tracking error 0.18% as of 30 Jun 2026. Daily NAV max drawdown/recovery is not disclosed by official source.
- Official Vanguard factsheet exposes rolling performance, not complete calendar-year NAV rows. PortfoliosLab dividend-adjusted 2021-2025 rows are marked * secondary proxies and are not issuer NAV rows.

| Year | VERE Total Return* (EUR) | S&P 500 TR (USD; common ref.) |
|---|---:|---:|
| 2021 | 24.57%* | 28.71% |
| 2022 | -12.43%* | -18.11% |
| 2023 | 17.62%* | 26.29% |
| 2024 | 6.80%* | 25.02% |
| 2025 | 21.22%* | 17.88% |

**Up years / Down years**

- Secondary proxy 2021-2025 up/down: 4 / 1
- Best: 2025, +21.22%*
- Least positive: 2024, +6.80%*
- Worst: 2022, -12.43%*
- Least bad down year: 2022, the only down year
- Secondary proxy cumulative/CAGR: +66.11%* / +10.68%*
- Current official YTD: +11.54% as of 31 Jul 2026; later secondary dividend-adjusted YTD +13.71%* as of 15 Aug 2026 is kept separate.

## Risk read-through

Official rolling 5-year NAV TR is 9.52% annualized as of 31 Jul 2026; secondary
calendar-proxy dispersion is 13.40%* population standard deviation. JustETF
reports 3-year annualized volatility 12.83% as of 30 Jun 2026, while
PortfoliosLab reports a full-history max drawdown of -34.74% on 18 Mar 2020 and
recovery in 225 trading sessions. These are secondary risk observations, not
official daily NAV fields. Main risks are Europe ex-UK country/sector
concentration, EUR-base versus underlying currencies, equity/foreign-market,
liquidity, counterparty and index-tracking risk. The main limitation is that
official complete calendar NAV rows were not exposed, so annual ranking is
secondary and marked *.

## Sources

- [Vanguard VERE product page](https://www.vanguard.co.uk/professional/product/etf/equity/9682/ftse-developed-europe-ex-uk-ucits-etf) — official identity, exchanges, benchmark, passive/physical structure, holdings, tracking error, NAV and as-of fields.
- [Vanguard VERE factsheet](https://fund-docs.vanguard.com/FTSE_Developed_Europe_ex_UK_UCITS_ETF_EUR_Accumulating_9682_EU_INT_UK_EN.pdf) — official EUR NAV TR rolling fields, fee, share-class, currency and risk disclosures as of 31 Jul 2026.
- [PortfoliosLab VERE.DE](https://portfolioslab.com/symbol/VERE.DE) — secondary dividend-adjusted annual/YTD proxy and drawdown/recovery.
- [justETF VERE](https://www.justetf.com/nl-be/etf-profile.html?isin=IE00BK5BQY34) — secondary volatility and identity/exchange cross-check.
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached workflow references — USD TR reference rows 2021-2025, dividends reinvested, as of 31 Dec 2025.
- [[ETF_performance_sources_2026-08-19]] | [[ETF Performance Index]]
