---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:CGIE
input_ticker: CGIE
ticker: CGIE
exchange: NYSE Arca
fund: Capital Group International Equity ETF
tracked_index: not applicable; active strategy
benchmark: MSCI EAFE Index (Net) (USD)
management_mode: active-equity-long-only
active_process: fundamental-active multi-manager
active_process_subtype: fundamental growth-oriented developed ex-U.S. equity with multi-manager segments
management_benchmark: MSCI EAFE Index (Net) (USD)
track_record: provisional
management_evidence: negative return-only
risk_evidence: issuer-fields; daily-NAV-drawdown-not-verified
updated: 2026-09-01
performance_as_of: 2025-12-31 (calendar) / 2026-07-31 (rolling) / 2026-08-28 (daily YTD)
calendar_years_as_of: 2025-12-31
current_ytd_as_of: 2026-08-28
market_price_as_of: 2026-08-28
nav_as_of: 2026-08-28
fund_facts_as_of: 2026-08-27 (assets) / 2026-07-31 (portfolio)
source_batch: raw/imports/ETF_performance_sources_2026-09-01_run-4.md
return_basis: NAV total return; distributions reinvested; net of fund expenses
return_currency: USD
primary_region: International
tags:
  - analysis/etf-performance
  - ticker/CGIE
  - geography/International
  - geography/global-developed
  - style/active-equity
---

# CGIE Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

CGIE คือ Capital Group International Equity ETF บน NYSE Arca เป็น
`active-equity-long-only` ETF ที่ลงทุนหลักในหุ้นนอกสหรัฐฯ โดยใช้ fundamental
stock selection และ Capital System แบบหลาย portfolio managers. Official issuer
กำหนด `MSCI EAFE Index (Net) (USD)` เป็น management benchmark ที่เหมาะกับ
universe ของหุ้น developed markets นอกสหรัฐฯ และแคนาดา.

ข้อมูลล่าสุดจาก Capital Group แยกเป็นหลายวันที่: daily YTD NAV/market price
`10.17% / 10.14%` ณ 28 ส.ค. 2026; month-end YTD NAV/market price/index
`7.21% / 7.12% / 11.59%`, 1-year `17.06% / 17.00% / 24.33%` และ lifetime
`16.51% / 16.45% / 20.03%` ณ 31 ก.ค. 2026. Calendar-year evidence ที่ครบถ้วนมี
เพียง 2024-2025: NAV `1.09%` และ `28.00%` เทียบ index `3.82%` และ `31.22%`.
หลักฐานจึงยังเป็น `provisional` และผลเชิง benchmark เป็น `negative return-only`;
ไม่เรียกความแตกต่างนี้ว่า alpha.

## Performance check

- `entity_key: NYSE Arca:CGIE`; inception `2023-09-26`; CUSIP `14021M107`; exchange `NYSE Arca, Inc.`
- Official summary prospectus ระบุว่าเป็น active, nondiversified ETF ลงทุนหลักใน common stocks นอกสหรัฐฯ, อย่างน้อย 80% ใน equity securities และอย่างน้อย 80% นอกสหรัฐฯ; emerging markets ได้ไม่เกิน 10%.
- Process ใช้ multiple portfolio managers แบ่ง portfolio เป็น segments และพิจารณาบริษัทที่มี long-term growth/resilience, strong balance sheets และ dividend potential.
- Primary metric: USD NAV Total Return รวม reinvested dividends/capital gains และ net of fund expenses; market-price return เก็บแยกจาก NAV.
- Expense ratio `0.54%`; one-year turnover `43%`; assets `$2,491.5m` ณ 27 ส.ค. 2026; issuers `72` ณ 31 ก.ค. 2026.

## Official rolling performance

| Period | CGIE NAV TR | CGIE market price TR | MSCI EAFE Net | As of |
|---|---:|---:|---:|---|
| Daily YTD | 10.17% | 10.14% | ไม่พบข้อมูลที่ยืนยันได้ | 2026-08-28 |
| YTD | 7.21% | 7.12% | 11.59% | 2026-07-31 |
| 1 year | 17.06% | 17.00% | 24.33% | 2026-07-31 |
| Since inception annualized | 16.51% | 16.45% | 20.03% | 2026-07-31 |

Return-only spread versus the issuer benchmark is `-4.38 pp` for the synchronized
YTD row, `-7.27 pp` for 1 year, and `-3.52 pp` for since-inception annualized
performance. The later daily-YTD NAV and market-price fields are not merged with
the older benchmark row.

## Calendar-year performance

The 2023 launch year is partial and is excluded from complete-year rankings. The
official Q2 2026 factsheet reports the following USD total returns:

| Year | CGIE NAV TR | CGIE market price TR | MSCI EAFE Net | S&P 500 TR (USD reference) |
|---|---:|---:|---:|---:|
| 2024 | 1.09% | 0.72% | 3.82% | 25.02% |
| 2025 | 28.00% | 28.10% | 31.22% | 17.88% |

From the compatible NAV rows, fund product is `1.2939520000`, cumulative return
`29.3952%`, rounded-input CAGR `13.7520%`, and population standard deviation
`13.4550%`. The benchmark product is `1.3623260400`, cumulative `36.2326%`, and
CAGR `16.7187%`. The two-year CAGR gap is `-2.9667 pp`, cumulative relative
wealth is `-5.0189%`, and the complete-year hit rate is `0/2`.

## Up years / down years

- Complete calendar years available: `2`
- Up/down among complete years: `2 / 0`
- Best complete year: 2025, `+28.00%`
- Least positive complete year: 2024, `+1.09%`
- Worst down year: `ไม่พบข้อมูลที่ยืนยันได้` เพราะไม่มี complete down year
- 2023 is a partial inception year and is not ranked.

## Active-management evidence

- `management_mode`: `active-equity-long-only`
- `active_process_subtype`: fundamental growth-oriented developed ex-U.S. equity with multi-manager segments
- `management_benchmark`: MSCI EAFE Index (Net) (USD)
- `track_record_maturity`: provisional; inception 2023-09-26 and only two complete calendar years
- `management_evidence`: negative return-only; NAV lagged the management benchmark in both complete years (`-2.73 pp` in 2024 and `-3.22 pp` in 2025), as well as the synchronized YTD and 1-year rows
- `risk_evidence`: issuer fields show lower Morningstar standard deviation and beta than the index over the cited since-inception window, but daily-NAV maximum drawdown, recovery and risk-adjusted persistence were not verified.

Capital Group's official article cites Morningstar data for 2023-09-26 to
2026-03-31: CGIE standard deviation `12.4%` versus MSCI EAFE `13.4%`, and beta
`0.9` versus `1.0`. This is useful risk context, not evidence of persistent
manager skill. The sample remains too short for a durable management conclusion.

## Risk read-through

Official product data report NAV `$38.00`, market price `$37.97`, premium/discount
`-0.08%`, and 30-day median bid-ask spread `0.03%`, all as of 28 ส.ค. 2026. The
portfolio snapshot as of 31 ก.ค. 2026 is `96.8%` non-U.S. equities, `0.7%` U.S.
equities and `2.5%` cash/equivalents/other; P/B is `2.8x` versus index `2.2x` and
P/E `17.6x` versus `15.8x` as of 30 มิ.ย. 2026. Key risks are foreign-market and
currency exposure, developed/emerging-market political and liquidity risk,
growth-style and sector concentration, nondiversification, active manager/process
risk, and ETF premium/discount or spread risk. Daily-NAV maximum drawdown and
exact recovery duration remain `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- [Capital Group CGIE official product page](https://www.capitalgroup.com/individual/investments/exchange-traded-funds/details/cgie) — identity, exchange, current YTD/NAV/market price, assets, issuers, benchmark, portfolio, valuation and rolling returns.
- [Capital Group CGIE Q2 2026 fact sheet](https://www.capitalgroup.com/individual/pdf/shareholder/ETGEFSX-311-1039178.pdf) — official calendar-year chart, NAV/market-price/index rows, strategy, current characteristics and risk disclosures.
- [CGIE 2025 SEC summary prospectus](https://www.sec.gov/Archives/edgar/data/1969445/000005193125000866/cgie497k.htm) — active strategy, fees, 2024 return table, risks and management structure.
- [Capital Group CGIE risk perspective](https://www.capitalgroup.com/advisor/investments/equities/perspectives/5-things-to-know-about-CGIE.html) — official Morningstar standard-deviation and beta context.
- [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common USD Total Return reference convention.
- [[ETF_performance_sources_2026-09-01_run-4]] | [[ETF Performance Index]]
