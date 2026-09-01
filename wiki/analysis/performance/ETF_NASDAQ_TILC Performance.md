---
type: etf-performance
instrument_type: ETF
entity_key: Nasdaq:TILC
input_ticker: TILC
ticker: TILC
exchange: Nasdaq
fund: Thrivent International Large Cap ETF
tracked_index: not applicable; active strategy
benchmark: MSCI EAFE Index (Net) (USD)
management_mode: active-equity-long-only
active_process: systematic-active
active_process_subtype: quantitative large-cap developed-international equity
management_benchmark: MSCI EAFE Index (Net) (USD)
track_record: established
track_record_maturity: established predecessor history; limited live ETF trading history
management_evidence: mixed
risk_evidence: mixed
risk_evidence_detail: issuer standard-deviation-beta-R2 fields; daily-NAV-drawdown-not-verified
updated: 2026-09-01
performance_as_of: 2025-12-31 (calendar) / 2026-07-31 (rolling)
calendar_years_as_of: 2025-12-31 (fund secondary; benchmark official)
current_ytd_as_of: 2026-07-31
market_price_as_of: not disclosed; trading halted
nav_as_of: not disclosed; trading halted
fund_facts_as_of: 2026-07-31
source_batch: raw/imports/ETF_performance_sources_2026-09-01_run-6.md
return_basis: NAV total return; dividends and capital gains reinvested; net of fund expenses
return_currency: USD
primary_region: International
tags:
  - analysis/etf-performance
  - ticker/TILC
  - geography/International
  - geography/global-developed
  - style/active-equity
---

# TILC Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

TILC เป็น `active-equity-long-only` ETF ของ Thrivent ที่เน้นหุ้น large-cap ใน
developed international markets และใช้กระบวนการที่ขับเคลื่อนโดย quantitative
techniques. Official issuer รายงาน NAV YTD `13.89%` และ 1-year `26.76%` ณ
31 ก.ค. 2026; current NAV และ market price เป็น `not disclosed` เพราะ issuer
ระบุว่าการซื้อขาย ETF ถูก halt. จาก complete calendar rows แบบ secondary ในช่วง
2018-2025 ผลตอบแทนสะสม `67.42%` / CAGR `6.65%`, มีปีบวก/ลบ `6 / 2`.

ETF มี live listing เพียง 15 มิ.ย. 2026 แต่ issuer ใช้ NAV ของ predecessor
mutual fund ก่อน listing จึงมีประวัติ strategy ยาวกว่าประวัติการซื้อขาย ETF จริง.

## Performance check

- `entity_key: Nasdaq:TILC`; inception `2017-11-14`; listing date `2026-06-15`; CUSIP `88588G604`.
- Metric: `NAV Total Return` รวมการ reinvest dividends และ capital gains และ net of fund expenses; market-price return เก็บแยก.
- Common benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference benchmark).
- Management mode: `active-equity-long-only`; `active_process: systematic-active`; subtype `quantitative large-cap developed-international equity`.
- Official strategy-aligned management benchmark: `MSCI EAFE Index (Net) (USD)` เพราะ issuer แสดง index นี้ใน performance table สำหรับ developed-economy stocks ใน Europe, Australasia และ Far East. AAII ระบุ MSCI ACWI Ex USA เป็นอีก benchmark แต่ไม่ใช้แทน official issuer comparator.
- Expense ratio: `0.52%` ณ 2026-07-31; holdings `327` ณ 2026-07-31.

### Official rolling performance

| Period | TILC NAV TR | TILC market price TR | MSCI EAFE Net | As of |
|---|---:|---:|---:|---|
| YTD | 13.89% | 14.20% | 11.59% | 2026-07-31 |
| 1 year | 26.76% | 27.11% | 24.33% | 2026-07-31 |
| 3 years annualized | 17.28% | 17.38% | 15.96% | 2026-07-31 |
| 5 years annualized | 9.60% | 9.66% | 9.31% | 2026-07-31 |
| Since inception annualized | 7.85% | 7.88% | not disclosed | 2026-07-31 |

Issuer notes that, before the ETF listing, predecessor NAVs represent both NAV
and market-price return history. The current page also presents a quarter-end
snapshot separately: YTD `12.34%` NAV / `13.30%` market price and 1-year
`22.19%` / `23.24%`, with MSCI EAFE `9.44%` / `20.23%`, as of 30 มิ.ย. 2026;
these observations are not merged with the month-end table above.

### Calendar-year performance

The fund rows marked `*` are secondary rounded dividend-reinvested NAV rows from
AAII; 2017 is a partial inception year and has no row. MSCI EAFE rows are the
official USD net-return factsheet; S&P rows reuse the cached USD total-return
convention as of 2025-12-31.

| Year | TILC NAV TR* | MSCI EAFE Index (Net) | S&P 500 TR (USD reference) |
|---|---:|---:|---:|
| 2018 | -12.50%* | -13.79% | -4.38% |
| 2019 | 18.50%* | 22.01% | 31.49% |
| 2020 | 2.90%* | 7.82% | 18.40% |
| 2021 | 16.50%* | 11.26% | 28.71% |
| 2022 | -17.90%* | -14.45% | -18.11% |
| 2023 | 20.00%* | 18.24% | 26.29% |
| 2024 | 4.60%* | 3.82% | 25.02% |
| 2025 | 30.70%* | 31.22% | 17.88% |

Rounded-input calculations for 2018-2025: TILC cumulative `67.42%`, CAGR
`6.65%`, population standard deviation `15.69%`; MSCI EAFE cumulative `73.88%`
and CAGR `7.16%`; S&P 500 cumulative `192.03%` and CAGR `14.33%`. In the
common 2021-2025 window, TILC is `56.91%` cumulative / `9.43%` CAGR, MSCI EAFE
is `53.32%` / `8.92%`, and S&P 500 is `96.17%` / `14.43%`.

**Up years / Down years**

- Complete calendar years available: `8`
- Up/down: `6 / 2`
- Best: 2025, `+30.70%*`
- Least positive: 2024, `+4.60%*`
- Worst: 2022, `-17.90%*`
- Least bad down year: 2018, `-12.50%*`
- Current YTD: `+13.89%` NAV as of `2026-07-31` (official issuer); current trading status is halted.

## Active management read-through

- `management_mode: active-equity-long-only`
- `active_process: systematic-active`
- `active_process_subtype`: quantitative large-cap developed-international equity; issuer says the process is primarily driven by quantitative techniques.
- `management_benchmark: MSCI EAFE Index (Net) (USD)`
- `track_record: established`; comparable calendar history is available through the predecessor, but live ETF trading history remains limited since 2026-06-15.
- `management_evidence: mixed`: over 2018-2025, TILC beat MSCI EAFE in `4 / 8` years, but its arithmetic CAGR was `-0.51 pp` lower and cumulative relative wealth was `-3.72%`. Over 2021-2025, the arithmetic CAGR comparison was `+0.51 pp`, hit rate `3 / 5`, and cumulative relative wealth `+2.34%`. These are benchmark-return comparisons, not alpha or proof of manager skill.
- `risk_evidence: mixed`: issuer reports 3-year standard deviation `12.76%`, 5-year `15.90%`, beta `0.64` and R-squared `43%` as of 2026-07-31 versus S&P 500 fields; issuer cautions that S&P 500 may not represent this international strategy. Daily-NAV maximum drawdown, recovery and risk-adjusted persistence are not verified.

## Risk read-through

TILC has `0.52%` net annual fund operating expenses and 327 holdings. The
portfolio was `97.68%` developed international and `2.32%` United States as of
31 ก.ค. 2026; the largest country exposures were Japan `22.97%`, United Kingdom
`14.59%`, France `9.79%`, Switzerland `8.80%` and Germany `6.58%`. Sector
exposure was led by Financials `27.83%`, Industrials `19.52%` and Information
Technology `12.83%` as of 30 มิ.ย. 2026. Main risks are foreign-market and
currency exposure, country/sector concentration, quantitative model and active
implementation risk, higher expense drag than a plain index ETF, and ETF
liquidity or premium/discount risk. The issuer’s trading-halt notice means that
current price/NAV and daily drawdown cannot be refreshed in this run.

## Sources

- [Thrivent TILC official product page](https://fp.thriventfunds.com/etfs/international-large-cap-etf.html) — identity, listing, current official YTD/rolling returns, predecessor-history disclosure, holdings, portfolio, fees and risk fields.
- [TILC SEC prospectus](https://www.sec.gov/Archives/edgar/data/1896670/000119312526200277/d108541d497k.htm) — objective, Nasdaq listing and management fee disclosures.
- [MSCI EAFE Index USD net-return factsheet](https://www.msci.com/documents/10199/255599/msci-eafe-index-usd-net.pdf) — official 2018-2025 annual net returns and 2026-07-31 rolling benchmark returns.
- [AAII TILC evaluator](https://www.aaii.com/etf/ticker/TILC) — secondary rounded annual NAV rows and current cross-check; not used to override issuer current YTD.
- [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common USD total-return reference definition; annual values use the cached workflow convention.
- [[ETF_performance_sources_2026-09-01_run-6]] | [[ETF Performance Index]]
