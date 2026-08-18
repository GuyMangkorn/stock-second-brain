---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:EWK
input_ticker: EWK
ticker: EWK
exchange: NYSE Arca
fund: iShares MSCI Belgium ETF
tracked_index: MSCI Belgium IMI 25/50 Index (Net)
benchmark: MSCI Belgium IMI 25/50 Index (Net)
management_mode: passive-index-tracking
updated: 2026-08-19
performance_as_of: 2025-12-31
rolling_10y_as_of: 2026-06-30
current_ytd_as_of: 2026-08-10
price_nav_as_of: 2026-08-11
fund_facts_as_of: 2026-08-11
source_batch: raw/imports/ETF_performance_sources_2026-08-19.md
return_basis: NAV total return; dividends and capital gains reinvested; net of expenses
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/EWK
  - geography/Belgium
---

# EWK ETF Performance

> [[ETF Region Index]] → [[Belgium ETF]] → [[ETF Performance Index]]

## Bottom line

`EWK` คือ iShares MSCI Belgium ETF ที่จดทะเบียนบน `NYSE Arca` และเป็น
passive, single-country equity ETF ซึ่งติดตาม `MSCI Belgium IMI 25/50 Index
(Net)`. กองทุนเริ่ม 12 มี.ค. 1996, TER `0.49%`, จ่าย distribution แบบ
semi-annual และมี 38 holdings ณ 10 ส.ค. 2026. Underlying exposure เป็นหุ้น
เบลเยียม จึงจัด primary region เป็น `Belgium` แยกจาก broad `Europe`.

จาก official 2021-2025 NAV Total Return rows ผลตอบแทนสะสมคือ `41.43%` หรือ
rounded-input CAGR `7.18%`, positive/negative years `4/1`. Issuer rolling
10-year NAV TR annualized คือ `7.08%` ณ 30 มิ.ย. 2026 และ current official NAV
TR YTD คือ `12.61%` ณ 10 ส.ค. 2026; NAV อยู่ที่ `USD 26.75` ณ 11 ส.ค. 2026.
ไม่ใช้ 2016-2020 annual rows ที่ไม่ถูกเปิดเผยใน reviewed official capture มา
เติมย้อนหลัง.

## Performance check

- `entity_key: NYSE Arca:EWK`; official fund name, ticker and exchange are confirmed by iShares and the SEC summary prospectus.
- Classification: `passive-index`; the fund seeks to track a free-float-adjusted, market-cap-weighted index covering Belgian large-, mid- and small-cap equities, subject to the 25/50 concentration methodology.
- Metric: issuer `Total Return` / NAV return, with dividends and capital gains reinvested and fund expenses deducted; market-price return is shown separately and not mixed into the NAV calculation.
- Fund inception: 12 มี.ค. 1996; CUSIP `464286301`; TER `0.49%`; semi-annual distributions; current benchmark `MSCI Belgium IMI 25/50 Index (Net)`.
- Official current snapshot: NAV `USD 26.75`, closing price `USD 26.82`, net assets `USD 162.63m` as of 11 ส.ค. 2026; 38 holdings as of 10 ส.ค. 2026.
- Official rolling fields as of 30 มิ.ย. 2026: NAV 1-year `24.33%`, 3-year annualised `17.72%`, 5-year annualised `7.07%`, 10-year annualised `7.08%`, and since inception `6.02%`.
- Benchmark continuity: EWK began tracking MSCI Belgium IMI 25/50 Index (Net) on 9 พ.ย. 2012; prior historical index data uses MSCI Belgium Investable Market Index (Net). The 2021-2025 table is within the current benchmark period.

| Year | EWK NAV TR (USD) | Market Price TR (USD) | MSCI Belgium IMI 25/50 (Net) | S&P 500 TR (USD) |
|---|---:|---:|---:|---:|
| 2021 | 12.92% | 12.87% | 8.02% | 28.71% |
| 2022 | -14.08% | -13.93% | -15.89% | -18.11% |
| 2023 | 7.46% | 7.47% | 7.71% | 26.29% |
| 2024 | 0.51% | 0.17% | 0.51% | 25.02% |
| 2025 | 34.96% | 35.41% | 35.30% | 17.88% |

The official 2021-2025 NAV rows compound to `41.43%` / rounded-input CAGR
`7.18%`; the benchmark rows compound to `33.08%` / `5.88%`. Rounded fund-minus-
benchmark observations are `+4.90`, `+1.81`, `-0.25`, `0.00` and `-0.34`
percentage points for 2021-2025. iShares warns that ETF total return may diverge
from the benchmark because of systematic fair value; these differences are not
called alpha.

The cached S&P 500 Total Return rows compound to `96.17%` / rounded-input CAGR
`14.43%` for 2021-2025. S&P 500 is a common USD reference only, not the
strategy-appropriate benchmark for a Belgium single-country ETF.

## Up years / Down years

- Complete 2021-2025 NAV TR up/down: `4 / 1`
- Best NAV TR year: 2025, `+34.96%`
- Least positive year: 2024, `+0.51%`
- Worst NAV TR year: 2022, `-14.08%`
- 2021-2025 annual-return standard deviation, population: `16.09%`
- Current official NAV TR YTD: `+12.61%` as of 10 ส.ค. 2026.

## Current and rolling official fields

| Metric | Value | As of | Basis |
|---|---:|---|---|
| Current NAV TR YTD | 12.61% | 2026-08-10 | official product page |
| NAV | USD 26.75 | 2026-08-11 | official product page |
| Closing price | USD 26.82 | 2026-08-11 | official product page |
| Net assets | USD 162.63m | 2026-08-11 | official product page |
| 1-year NAV TR | 24.33% | 2026-06-30 | official product page |
| 3-year annualised NAV TR | 17.72% | 2026-06-30 | official product page |
| 5-year annualised NAV TR | 7.07% | 2026-06-30 | official product page |
| 10-year annualised NAV TR | 7.08% | 2026-06-30 | official product page |
| Since-inception annualised NAV TR | 6.02% | 2026-06-30 | official product page |
| 3-year standard deviation | 14.38% | 2026-07-31 | official product page |
| 3-year beta | 0.54 | 2026-07-31 | official product page |
| Holdings | 38 | 2026-08-10 | official product page |

## Risk read-through

EWK เป็น single-country ETF ที่มี concentration สูงกว่ากอง broad Europe:
official exposure snapshot ณ 10 ส.ค. 2026 มี Health Care `25.98%`, Consumer
Staples `25.25%`, Financials `16.78%`, Real Estate `9.53%`, Materials `7.57%`
และ Industrials `5.78%`. Factsheet ณ 30 มิ.ย. 2026 ระบุ top-10 holdings รวม
`69.05%`; Anheuser-Busch InBev `21.94%`, argenx `15.55%` และ UCB `9.01%` เป็น
ตัวขับเคลื่อนสำคัญ. ความเสี่ยงหลักคือ Belgium/country concentration, sector
concentration, EUR/USD FX, small fund size, liquidity, systematic fair-value
pricing และ equity volatility. Official daily NAV maximum drawdown และ recovery
date ไม่ได้เปิดเผยใน reviewed sources; `risk-adjusted evidence: not-verified`
สำหรับสองฟิลด์นี้.

## Sources

- [iShares EWK product page](https://www.ishares.com/us/products/overview-v3-ishares-fund-data?portfolioId=239610&seoSlug=ishares-msci-belgium-capped-etf) — official identity, NYSE Arca, benchmark, current NAV/YTD/price, assets, holdings, rolling performance, risk fields and sector exposures.
- [iShares EWK June 2026 factsheet](https://www.ishares.com/us/literature/fact-sheet/ewk-ishares-msci-belgium-etf-fund-fact-sheet-en-us.pdf) — official 2021-2025 NAV/market-price/benchmark rows, return definitions, fee, launch, holdings, top holdings, sectors and benchmark-history note.
- [SEC EWK summary prospectus](https://www.sec.gov/Archives/edgar/data/930667/000119312525336632/d23588d497k.htm) — official NYSE Arca identity, objective, index methodology and risk disclosures.
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached S&P 500 Total Return references — common USD reference for the displayed 2021-2025 rows.
- [[ETF_performance_sources_2026-08-19]] — source map, raw observations, calculations, reconciliation and scheduled-local verification record.

## Follow-up

- Refresh the current NAV/YTD snapshot and retain the June factsheet as the historical annual/benchmark source.
- Keep EWK's Belgium single-country exposure separate from broad Europe pages and do not infer manager skill from benchmark arithmetic.
- Verify official daily NAV drawdown/recovery if iShares publishes a suitable dated series.
