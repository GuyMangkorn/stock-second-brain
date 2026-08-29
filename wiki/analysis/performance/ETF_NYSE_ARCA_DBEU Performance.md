---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:DBEU
input_ticker: DBEU
ticker: DBEU
exchange: NYSE Arca
fund: Xtrackers MSCI Europe Hedged Equity ETF
tracked_index: MSCI Europe US Dollar Hedged Index
benchmark: S&P 500 Total Return
management_mode: passive-index-tracking
updated: 2026-08-29
annual_performance_as_of: 2025-12-31
performance_as_of: 2026-07-31
rolling_10y_as_of: 2026-06-30
current_ytd_as_of: 2026-07-31
nav_as_of: 2026-06-30
market_price_as_of: 2026-08-27
price_nav_as_of: not disclosed
fund_facts_as_of: 2026-06-30
risk_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-08-29.md
return_basis: NAV total return; secondary annual/YTD proxy where marked
return_currency: USD
primary_region: Europe
tags:
  - analysis/etf-performance
  - ticker/DBEU
  - geography/Europe
---

# DBEU Performance

> Navigation: [[ETF Region Index]] → [[Europe ETF]] → [[ETF Performance Index]]

## Bottom line

`DBEU` เป็น Xtrackers MSCI Europe Hedged Equity ETF, passive developed-Europe
large-/mid-cap equity ที่ hedge currency exposure เป็น USD. Official DWS Q2
factsheet รายงาน rolling `10-year NAV Total Return CAGR` `11.58%` ณ
30 มิ.ย. 2026. Latest secondary AAII capture reports NAV YTD `12.6%`, 1Y
`23.9%`, 3Y `15.8%`, 5Y `11.9%` และ trailing 10Y `11.2%` ณ 31 ก.ค. 2026;
จึงติด `*` และไม่ใช้แทน official DWS rolling field. Latest secondary market
price คือ `$54.80` ณ 27 ส.ค. 2026; current NAV ที่ตรงกัน `ไม่พบข้อมูลที่ยืนยันได้`.

## Performance check

- `entity_key: NYSE Arca:DBEU`; SEC/DWS identify the fund as `Xtrackers MSCI Europe Hedged Equity ETF`, NYSE ticker `DBEU`, CUSIP `233051853`, inception `2013-09-30`.
- Classification: `passive-index-tracking`; DWS describes an indexing approach with at least 80% in underlying-index component securities and representative sampling where appropriate.
- Metric: official `NAV Total Return` reflects distributions and fund expenses; market-price return is kept separate. Annual and latest YTD rows below are secondary rounded NAV-return observations marked `*` because the reviewed current DWS factsheet did not publish those calendar/YTD fields.
- Tracked index: `MSCI Europe US Dollar Hedged Index`; DWS describes one-month forward contracts that hedge the developed-Europe equity exposure to USD. Common reference is `S&P 500 Total Return` (USD, dividends reinvested), not DBEU's tracked index.
- Official DWS rolling 10-year window is `2016-06-30` to `2026-06-30`; official NAV TR CAGR `11.58%`, raw endpoints not disclosed.
- Official DWS fund facts as of `2026-06-30`: 410 holdings, net assets `US$758,183,774.79`, gross/net expense ratio `0.45%`, SEC 30-day yield `2.11%`, beta `0.73`, and index constituents `397` across 15 countries.
- Latest secondary current snapshot as of `2026-08-27`: market price `$54.80`, share-class assets about `$771M`, trailing yield `1.40%`, expense ratio `0.45%`; AAII's portfolio composition capture is as of `2026-07-30` with 424 securities, top ten `20.4%`, foreign issues `96.4%`, and cash `0.8%`.

### Official DWS Q2 2026 standardized returns

| Return basis | 3M | 1Y | 3Y annualized | 5Y annualized | 10Y annualized | Since inception annualized |
|---|---:|---:|---:|---:|---:|---:|
| NAV | 11.97% | 24.03% | 16.02% | 12.03% | 11.58% | 9.90% |
| Market price | 10.67% | 24.31% | 16.08% | 12.02% | 11.52% | 9.92% |
| MSCI Europe US Dollar Hedged Index | 11.87% | 24.16% | 16.25% | 12.18% | 11.82% | 10.15% |
| MSCI Europe parent index | 10.93% | 18.64% | 16.18% | 9.50% | 9.92% | 7.11% |

All official rows above are as of `2026-06-30`. Index returns are unmanaged,
gross of fees and assume dividend reinvestment; they are not called alpha.

### Secondary July 2026 cross-check

| Return basis | 1M | 3M | YTD | 1Y | 3Y annualized | 5Y annualized | 10Y annualized |
|---|---:|---:|---:|---:|---:|---:|---:|
| NAV proxy* | 1.0% | 7.7% | 12.6% | 23.9% | 15.8% | 11.9% | 11.2% |
| Closing-price proxy* | 0.6% | 7.1% | 13.0% | 24.1% | 15.7% | 11.9% | 11.2% |

AAII's July table is a secondary rounded capture as of `2026-07-31`; it is
used to refresh current/YTD context while the DWS official rolling field stays
the canonical 10-year metric.

### Secondary annual total-return context

| Year | DBEU NAV TR proxy* (USD) | S&P 500 TR (USD; common ref.) |
|---|---:|---:|
| 2016 | 8.10%* | 11.96% |
| 2017 | 14.60%* | 21.83% |
| 2018 | -8.50%* | -4.38% |
| 2019 | 26.80%* | 31.49% |
| 2020 | -0.50%* | 18.40% |
| 2021 | 23.30%* | 28.71% |
| 2022 | -6.20%* | -18.11% |
| 2023 | 17.00%* | 26.29% |
| 2024 | 9.50%* | 25.02% |
| 2025 | 22.50%* | 17.88% |

The DBEU annual series is a secondary rounded NAV-return capture, not
issuer-published calendar rows in the reviewed DWS factsheet. The S&P 500
column uses the cached USD total-return convention as of 2025-12-31.

## Window calculations and tracking context

- Secondary 2016-2025 proxy compounds to `159.58%*` / rounded-input CAGR `10.01%*`; up/down years are `7 / 3`; best is 2019 `+26.80%*`; worst is 2018 `-8.50%*`; population standard deviation is `11.83%*`.
- Secondary 2021-2025 proxy compounds to `81.51%*` / rounded-input CAGR `12.66%*`; up/down years are `4 / 1`. Cached S&P 500 TR compounds to `96.17%` / CAGR `14.43%` over the same window; this is a common reference, not manager-skill evidence.
- Official DWS NAV minus hedged-index tracking observations as of 2026-06-30 are 3M `+0.10 pp`, 1Y `-0.13 pp`, 3Y `-0.23 pp`, 5Y `-0.15 pp`, 10Y `-0.24 pp`, and since inception `-0.25 pp`; these are implementation/expense/hedging observations, not alpha.
- Official rolling 10Y NAV TR `11.58%` remains separate from the secondary 2016-2025 CAGR `10.01%*` and July secondary trailing 10Y `11.2%*`; windows and source quality differ.
- Reconciliation: the prior page's official June fields remain current for the rolling metric and official fund facts. The refreshed July AAII observation adds YTD `12.6%*` and the Aug-27 secondary price, without relabeling either as official DWS data.

## Risk read-through

Official DWS country weights as of 2026-06-30 were UK `20.08%`, Switzerland
`14.86%`, France `14.29%`, Germany `13.10%`, Netherlands `10.57%`, Spain
`5.97%`, Italy `4.88%`, Sweden `4.57%`, Denmark `2.54%`, and cash `1.94%`.
Largest sectors were Financials `23.71%`, Industrials `17.59%`, Health Care
`12.46%`, Information Technology `9.84%`, Consumer Staples `8.29%`, and
Consumer Discretionary `6.42%`. Top holdings included ASML `5.25%`, HSBC
`2.24%`, Roche `1.99%`, Novartis `1.97%`, and AstraZeneca `1.94%`.

USD hedging reduces direct non-USD currency exposure but creates forward,
basis, hedge-ratio and hedge-cost risk; the fund remains exposed to European
country, sector, equity-market and liquidity risk. DWS reports beta `0.73`
as of 2026-06-30, while AAII's secondary July risk capture reports 10.1%
standard deviation and beta `0.60`; these are different source/date metrics
and are not reconciled into one field. Daily NAV history sufficient to
reproduce maximum drawdown and recovery is `ไม่พบข้อมูลที่ยืนยันได้`.

Current secondary market price `$54.80` is not paired with a verified same-date
NAV, so premium/discount is `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- [DWS DBEU Q2 2026 factsheet](https://etf.dws.com/download/asset/b2d0199b-0bfc-4ed0-866b-24f31967f463) — official identity, passive/hedged objective, rolling NAV/benchmark returns, fee, holdings, countries, sectors and beta; as of 2026-06-30.
- [SEC DBEU summary prospectus](https://www.sec.gov/Archives/edgar/data/1503123/000008805325000878/k100125dbeu.htm) — official NYSE Arca identity, passive/indexing method, 80% policy and risk disclosures; October 2025.
- [AAII DBEU performance page](https://www.aaii.com/etf/ticker/DBEU) — secondary rounded July 2026 annual/YTD/rolling fields, current price/assets and portfolio/risk cross-check; data as of 2026-07-31 to 2026-08-27 where stated.
- [DWS currency-hedged ETFs](https://etf.dws.com/en-us/etf-knowledge/focus-topics-etf-investment-strategies/currency-hedged-etfs-mitigating-currency-risks-from-international-equities/) — official hedged-ETF structure and 0.45% fee cross-reference.
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached workflow references — common USD Total Return rows, dividends reinvested, as of 2025-12-31.
- [[ETF_performance_sources_2026-08-29]] | [[ETF Performance Index]]
