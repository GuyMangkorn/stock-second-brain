---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:EIRL
input_ticker: EIRL
ticker: EIRL
exchange: NYSE Arca
fund: iShares MSCI Ireland ETF
tracked_index: MSCI All Ireland Capped Index (Net)
benchmark: MSCI All Ireland Capped Index (Net)
management_mode: passive-index-tracking
updated: 2026-08-19
performance_as_of: 2025-12-31
rolling_10y_as_of: 2026-06-30
current_ytd_as_of: 2026-08-14
price_nav_as_of: 2026-08-17
fund_facts_as_of: 2026-08-17
source_batch: raw/imports/ETF_performance_sources_2026-08-19.md
return_basis: NAV total return; dividends and capital gains reinvested; net of expenses
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/EIRL
  - geography/Ireland
---

# EIRL ETF Performance

> [[ETF Region Index]] → [[Ireland ETF]] → [[ETF Performance Index]]

## Bottom line

`EIRL` คือ iShares MSCI Ireland ETF ที่จดทะเบียนบน `NYSE Arca` และเป็น
passive, single-country equity ETF ซึ่งติดตาม `MSCI All Ireland Capped Index
(Net)`. กองทุนเริ่ม 5 พ.ค. 2010, expense ratio `0.50%`, จ่าย distribution แบบ
semi-annual และมี 26 holdings ณ 14 ส.ค. 2026. Underlying exposure เป็นหุ้นที่มี
Ireland เป็นศูนย์กลาง แต่ geographic snapshot ยังมี UK และ US exposure จึงต้อง
อ่านร่วมกับ country, sector และ FX concentration.

จาก official 2016-2025 NAV Total Return rows ผลตอบแทนสะสมคือ `107.72%` หรือ
rounded-input calendar CAGR `7.58%`; ช่วง 2021-2025 สะสม `56.65%` หรือ CAGR
`9.39%`, positive/negative years `3/2`. Issuer rolling 10-year NAV TR คือ
`9.94%` ณ 30 มิ.ย. 2026 และ current official NAV TR YTD คือ `15.05%` ณ
14 ส.ค. 2026; NAV อยู่ที่ `USD 82.88` ณ 17 ส.ค. 2026. S&P 500 Total Return
ใช้เป็น common USD reference เท่านั้น ไม่ใช่ strategy-appropriate benchmark
ของกองทุนนี้.

## Performance check

- `entity_key: NYSE Arca:EIRL`; official fund name, ticker, exchange, CUSIP `46429B507` and inception `2010-05-05` are confirmed by iShares and the summary prospectus.
- Classification: `passive-index`; the fund seeks to track a free-float-adjusted, market-capitalization-weighted index of Irish equities subject to MSCI eligibility and capping rules.
- Metric: issuer `Total Return` / NAV return, with dividends and capital gains reinvested and fund expenses deducted; market-price return is not mixed into the NAV calculation.
- Current benchmark: `MSCI All Ireland Capped Index (Net)`. Historical index data before 2013-11-27 uses MSCI Ireland Investable Market 25/50 Index (Net); the 2016-2025 fund rows are after that transition.
- Official current snapshot: NAV `USD 82.88`, closing price `USD 83.01`, non-fair-value NAV `USD 83.11`, net assets `USD 78.73m`, and premium `0.16%`, all as of 17 ส.ค. 2026.
- Official rolling fields as of 30 มิ.ย. 2026: NAV 1-year `19.47%`, 3-year annualised `13.50%`, 5-year annualised `8.53%`, 10-year annualised `9.94%`, and since inception `9.86%`.

| Year | EIRL NAV TR (USD) | MSCI All Ireland Capped (Net) | S&P 500 TR (USD) |
|---|---:|---:|---:|
| 2016 | -6.96% | not disclosed | 11.96% |
| 2017 | 28.58% | not disclosed | 21.83% |
| 2018 | -20.99% | not disclosed | -4.38% |
| 2019 | 26.61% | not disclosed | 31.49% |
| 2020 | 10.80% | not disclosed | 18.40% |
| 2021 | 13.62% | 14.52% | 28.71% |
| 2022 | -18.63% | -18.19% | -18.11% |
| 2023 | 34.06% | 35.59% | 26.29% |
| 2024 | -1.74% | -0.76% | 25.02% |
| 2025 | 28.63% | 30.42% | 17.88% |

The official 2016-2024 NAV rows come from the iShares December 2025 summary
prospectus chart; the 2025 NAV and 2021-2025 benchmark rows come from the
current iShares performance table. The official 2021-2025 NAV rows compound to
`56.65%` / rounded-input CAGR `9.39%`; the benchmark rows compound to `64.42%`
/ `10.46%`. Annual fund-minus-benchmark observations are `-0.90`, `-0.44`,
`-1.53`, `-0.98` and `-1.79` percentage points for 2021-2025; these are
tracking/fee/fair-value context and are not called alpha.

The cached S&P 500 Total Return rows compound to `298.33%` / rounded-input CAGR
`14.82%` for 2016-2025 and `96.17%` / `14.43%` for 2021-2025. It remains a
common USD reference, not EIRL's tracked index.

## Up years / Down years

- Complete 2016-2025 NAV TR up/down: `6 / 4`
- Best NAV TR year: 2023, `+34.06%`
- Least positive year: 2020, `+10.80%`
- Worst NAV TR year: 2018, `-20.99%`
- Least-bad down year: 2024, `-1.74%`
- 2016-2025 annual-return standard deviation, population: `19.40%`
- Current official NAV TR YTD: `+15.05%` as of 14 ส.ค. 2026.

## Current and rolling official fields

| Metric | Value | As of | Basis |
|---|---:|---|---|
| Current NAV TR YTD | 15.05% | 2026-08-14 | official product page |
| NAV | USD 82.88 | 2026-08-17 | official product page |
| Closing price | USD 83.01 | 2026-08-17 | official product page |
| Non-fair-value NAV | USD 83.11 | 2026-08-17 | official product page |
| Net assets | USD 78.73m | 2026-08-17 | official product page |
| 1-year NAV TR | 19.47% | 2026-06-30 | official product page |
| 3-year annualised NAV TR | 13.50% | 2026-06-30 | official product page |
| 5-year annualised NAV TR | 8.53% | 2026-06-30 | official product page |
| 10-year annualised NAV TR | 9.94% | 2026-06-30 | official product page |
| Since-inception annualised NAV TR | 9.86% | 2026-06-30 | official product page |
| 3-year standard deviation | 16.21% | 2026-07-31 | official product page |
| 3-year beta | 0.77 | 2026-07-31 | official product page |
| Holdings | 26 | 2026-08-14 | official product page |

## Risk read-through

EIRL เป็น single-country ETF ที่มี concentration สูงกว่ากอง broad Europe:
official exposure snapshot ณ 14 ส.ค. 2026 มี Ireland `74.52%`, UK `12.80%`,
US `10.28%`, Bermuda `1.65%`, cash/derivatives `0.52%` และ other `0.23%`.
Sector concentration อยู่ที่ Financials `38.79%`, Consumer Staples `19.13%`,
Industrials `14.62%` และ Health Care `10.36%`. Factsheet ณ 30 มิ.ย. 2026 ระบุ
top holdings เช่น AIB Group `16.39%`, Bank of Ireland `14.65%`, Kerry Group
`10.51%` และ Icon `6.46%`; top-three รวมประมาณ `41.55%`.

ความเสี่ยงหลักคือ Ireland/country concentration, financials and consumer-staples
concentration, USD-versus-local-currency FX, small-fund liquidity, bid-ask spread,
systematic fair-value pricing และ equity volatility. Official daily NAV
observations ที่เพียงพอสำหรับคำนวณ maximum drawdown และ recovery date ไม่ได้ถูก
เปิดเผยใน reviewed sources; `risk-adjusted evidence: not-verified` สำหรับ
drawdown/recovery fields.

## Sources

- [iShares EIRL product page](https://www.ishares.com/us/products/239662/ishares-msci-ireland-capped-etf) — official identity, NYSE Arca, benchmark, current NAV/YTD/price, assets, holdings, rolling performance, standard deviation, beta, valuation fields and exposures.
- [iShares EIRL June 2026 factsheet](https://www.ishares.com/us/literature/fact-sheet/eirl-ishares-msci-ireland-etf-fund-fact-sheet-en-us.pdf) — official launch, fee, benchmark-history note, holdings, sector/geography context and performance definitions.
- [iShares EIRL December 2025 summary prospectus](https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-ireland-capped-etf-8-31.pdf) — official objective, passive/index methodology, expense ratio, calendar-year chart and risk disclosures.
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached S&P 500 Total Return references — common USD reference rows for complete calendar years `2016-2025`.
- [[ETF_performance_sources_2026-08-19]] — source map, raw observations, calculations, reconciliation and scheduled-local verification record.

## Follow-up

- Refresh the current NAV/YTD snapshot and retain the December prospectus plus June factsheet as the historical annual/benchmark sources.
- Keep EIRL's Ireland single-country exposure separate from broad Europe pages; do not infer manager skill from the S&P comparison or arithmetic benchmark gap.
- Verify official daily NAV drawdown/recovery if iShares publishes a suitable dated series.
