---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:SPEU
input_ticker: SPEU
ticker: SPEU
exchange: NYSE Arca
fund: State Street SPDR Portfolio Europe ETF
tracked_index: STOXX Europe Total Market Index
benchmark: S&P 500 Total Return
management_mode: passive-index-tracking
updated: 2026-08-19
performance_as_of: 2025-12-31
current_ytd_as_of: 2026-06-30
price_nav_as_of: 2026-07-17
fund_facts_as_of: 2026-07-21
source_batch: raw/imports/ETF_performance_sources_2026-08-19.md
return_basis: NAV total return; dividends reinvested; net of expenses
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/SPEU
  - geography/Europe
---

# SPEU Performance

> Navigation: [[ETF Region Index]] → [[Europe ETF]] → [[ETF Performance Index]]

## Bottom line

`SPEU` คือ State Street SPDR Portfolio Europe ETF, canonical listing
`NYSE Arca:SPEU`. Official State Street capture ล่าสุดให้ NAV TR YTD `+7.29%`,
1Y `+17.82%`, 3Y `+16.35%`, 5Y `+9.12%` และ rolling 10Y `+9.76%` ณ 30 มิ.ย.
2026; current official NAV snapshot คือ `US$54.97` ณ 17 ก.ค. 2026. Issuer
ไม่แสดง complete annual calendar rows ใน capture ที่ตรวจ จึงใช้ secondary
dividend-reinvested total-return proxy ปี 2021-2025 แบบติด `*`: cumulative
`61.99%` หรือ rounded-input CAGR `10.13%`.

## Performance check

- `entity_key: NYSE Arca:SPEU`; State Street ระบุ exchange `NYSE Arca`, ticker `SPEU`, CUSIP `78463X103`, ISIN `US78463X1037`, inception `15 ต.ค. 2002`, base currency `USD` และ distribution frequency `Quarterly`.
- Classification: `passive-index-tracking`; fund ใช้ sampling และมุ่งติดตาม `STOXX Europe Total Market Index`, broad Western Europe across the market-cap spectrum.
- Metric: official `NAV Total Return` รวม dividends/capital gains ที่ reinvested และ net of fees; market-value return ถูกเก็บแยก. Annual rows ในตารางเป็น secondary total-return proxy `*` และไม่ควรเรียกว่า official NAV TR.
- Issuer benchmark: `STOXX Europe Total Market Index`; State Street ระบุ benchmark history ว่าใช้ linked `STOXX Europe 50 Index` ตั้งแต่ inception ถึง 22 ก.ย. 2019 และ `STOXX Europe Total Market Index` ตั้งแต่ 23 ก.ย. 2019. Common reference ในตารางคือ `S&P 500 Total Return` (USD, dividends reinvested).
- Expense ratio: `0.07%`; official NAV `US$54.97` และ AUM `US$714.59M` ณ 17 ก.ค. 2026; official 30-day SEC yield `2.43%` และ fund distribution yield `3.44%` ณ 17 ก.ค. 2026.
- Official NAV TR as of 30 มิ.ย. 2026: YTD `7.29%`, 1Y `17.82%`, 3Y `16.35%`, 5Y `9.12%`, 10Y `9.76%`, since inception `6.89%`; benchmark fields are `7.07% / 17.60% / 16.11% / 8.86% / 9.63% / 6.87%`.
- Current-YTD limitation: ไม่พบ official State Street YTD หลัง 30 มิ.ย. 2026 ใน capture ที่ตรวจ; later official NAV/fund facts as of 17-21 ก.ค. 2026 are retained separately and not relabeled as a later YTD.

| Year | SPEU total-return proxy* (USD; not official NAV) | S&P 500 TR (USD; common ref.) |
|---|---:|---:|
| 2021 | 16.20% | 28.71% |
| 2022 | -15.97% | -18.11% |
| 2023 | 19.84% | 26.29% |
| 2024 | 1.94% | 25.02% |
| 2025 | 35.80% | 17.88% |

Secondary SPEU proxy rows compound to `61.99%*` / rounded-input CAGR `10.13%*`
for 2021-2025. Cached S&P 500 TR compounds to `96.17%` / `14.43%` over the
same period. The comparison is a common USD reference only; no direct
manager-skill or alpha claim is made. The proxy is not used to override the
issuer's official rolling NAV TR fields.

**Up years / Down years**

- Secondary proxy 2021-2025 up/down: `4 / 1`
- Best proxy year: 2025, `+35.80%*`
- Least positive proxy year: 2024, `+1.94%*`
- Worst/least-bad down proxy year: 2022, `-15.97%*`
- Population standard deviation of the five proxy annual returns: `17.48%*`
- Latest official NAV TR YTD: `+7.29%` as of 30 มิ.ย. 2026

## Risk read-through

Official rolling NAV TR is `9.76%` annualized over 10 years as of 30 มิ.ย. 2026;
the `10.13%*` figure is a separate secondary calendar proxy. The fund held
1,684 positions ณ 17 ก.ค. 2026, with country exposure to the United Kingdom
`21.99%`, France `14.75%`, Switzerland `13.96%`, Germany `12.72%`, and the
Netherlands `8.30%`. Main risks are European country/sector/small-cap exposure,
non-USD underlying currency movements, index-history change, sampling/tracking
risk, equity volatility and market-price/NAV timing. Official daily NAV maximum
drawdown and recovery date ยัง `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- [State Street SPEU product page](https://www.ssga.com/us/en/individual/etfs/state-street-spdr-portfolio-europe-etf-speu) — official identity, listing, inception, benchmark-history change, NAV/AUM, current fund facts, distributions/yields and rolling NAV performance.
- [State Street SPEU factsheet](https://www.ssga.com/library-content/products/factsheets/etfs/us/factsheet-us-en-speu.pdf) — official NAV/benchmark performance, fee, holdings and country/sector facts as of 30 มิ.ย. 2026.
- [FinanceCharts SPEU total-return history](https://www.financecharts.com/stocks/SPEU/performance/total-return) — secondary dividend-reinvested total-return proxy for calendar rows 2021-2025; marked `*` and not treated as official NAV.
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached workflow references — common USD Total Return rows, dividends reinvested, as of 31 ธ.ค. 2025.
- [[ETF_performance_sources_2026-08-19]] | [[ETF Performance Index]]
