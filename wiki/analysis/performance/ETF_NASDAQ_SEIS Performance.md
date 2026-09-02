---
type: etf-performance
instrument_type: ETF
entity_key: Nasdaq:SEIS
input_ticker: SEIS
ticker: SEIS
exchange: Nasdaq
fund: SEI Select Small Cap ETF
tracked_index: none; actively managed
benchmark: Russell 2000 Index (USD)
management_mode: active-equity-long-only
active_process: other-active
active_process_subtype: integrated quantitative and fundamental multi-manager U.S. small-cap selection
management_benchmark: Russell 2000 Index (USD)
track_record: insufficient
management_evidence: insufficient
risk_evidence: not-verified
updated: 2026-09-02
performance_as_of: 2026-07-31 (official current/YTD) / 2026-06-30 (official annualized)
calendar_years_as_of: 2025-12-31 (secondary one-year row)
current_ytd_as_of: 2026-07-31
price_nav_as_of: not disclosed in reviewed reliable official source
fund_facts_as_of: 2026-07-31
source_batch: raw/imports/ETF_performance_sources_2026-09-02_run-5.md
return_basis: NAV total return; net of fund expenses; distributions included per issuer total-return convention
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/SEIS
  - geography/United-States
  - style/active-multi-manager
---

# SEIS Performance

> Navigation: [[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]

## Bottom line

SEIS คือ SEI Select Small Cap ETF ซึ่งเป็น active long-only U.S. small-cap ETF
ที่ผสาน quantitative model ของ SEI กับ model portfolios จาก sub-advisers แบบ
fundamental. Official fact sheet ณ 31 ก.ค. 2026 รายงาน NAV Total Return YTD
`15.79%` เทียบ Russell 2000 Index `18.85%`; ตัวเลข 1-year ณ 30 มิ.ย. 2026
คือ `31.44%` เทียบ benchmark `40.78%`. Return-only differences จึงเป็น
`-3.06 pp` และ `-9.34 pp` ตามลำดับ ไม่ใช่ alpha.

กองเริ่มดำเนินงาน 8 ต.ค. 2024 และเริ่มจดทะเบียนบน Nasdaq 10 ต.ค. 2024 จึงยังมี
track record ต่ำกว่า 3 ปี. Secondary standardized capture ให้ annual NAV TR
ปี 2025 `9.80%*`; เนื่องจากไม่มี annual benchmark row ที่ตรวจสอบได้ และมีเพียง
หนึ่ง complete calendar observation จึงยังไม่คำนวณ 2021-2025 CAGR, hit rate หรือ
ใช้ผลตอบแทนหนึ่งปีเป็นหลักฐานของ manager skill.

## Performance check

- `entity_key: Nasdaq:SEIS`; fund `SEI Select Small Cap ETF`; operations inception `2024-10-08`; Nasdaq listing `2024-10-10`
- Classification: `active-equity-long-only`; SEC ระบุว่ากองลงทุนอย่างน้อย 80% ใน equity securities ของ small companies ใน universe ของ Russell 2000 และใช้ integrated management approach ที่ผสาน quantitative-based active portfolio ของ SEI กับ model portfolios จาก sub-advisers
- Metric: `NAV Total Return` บนฐาน USD, net of expenses; market-price return แยกจาก NAV return และไม่ใช้แทนกัน
- Management benchmark: `Russell 2000 Index (USD)` ตาม official SEI fact sheet; S&P 500 TR เป็นเพียง common reference
- Official fund facts ณ 2026-07-31: net assets `US$575.55M`, holdings `372`, weighted average capitalization `US$6,065M`, P/B `2.40`, median forward P/E `14.37`, beta `0.95`, expense ratio `0.55%`
- Manager allocation ณ official fact sheet: SEI Investments Management Corporation `70%`, Easterly Investment Partners `20%`, Geneva Capital Management `10%`; key approaches include quantitative, deep-value and high-quality/low-volatility selection

| Period / year | SEIS NAV TR | Russell 2000 Index | S&P 500 TR |
|---|---:|---:|---:|
| 2025 | 9.80%* | not disclosed | 17.88% |
| 2026 YTD (2026-07-31) | 15.79% | 18.85% | not directly comparable |
| 1 year (2026-06-30) | 31.44% | 40.78% | not directly comparable |
| Since inception annualized (2026-06-30) | 18.35% | 21.99% | not directly comparable |

The 2025 annual row is a secondary NAV total-return observation and is marked
`*`; the official SEI fact sheet does not expose a complete calendar-year table
in the reviewed capture. The official benchmark rows above are available only
for the issuer's current rolling periods. S&P 500 TR calendar rows use the
cached USD total-return convention for 2016-2025; the current S&P reference is
`12.34%` YTD as of 2026-09-01 and is not directly compared because the dates
differ.

## Calendar performance

Only 2025 is a complete calendar observation in the reviewed data, and it is
secondary: NAV TR `+9.80%*`. Up/down-year count, best/worst year and
2021-2025 CAGR are therefore `not applicable` as a meaningful multi-year
window. The 2024 inception-year partial return is not backfilled into an annual
series.

## Risk read-through

SEIS is concentrated in U.S. small-cap equities and has model, sub-adviser,
value, momentum, quality and low-volatility exposures. The official fact sheet
reports 372 holdings, 0.95 beta and no disclosed 3-year standard deviation or
tracking error as of 2026-07-31. The prospectus highlights small/medium-cap,
quantitative-investing, market, liquidity, management, new-fund and
premium/discount risks.

Compatible official daily NAV history for maximum drawdown, recovery duration,
downside capture, tracking error or risk-adjusted persistence was not verified;
`risk_evidence` remains `not-verified`. The reviewed reliable official capture
does not provide a dated NAV/market-price pair, so no premium/discount
calculation is inferred.

## Active management read-through

- `management_mode`: `active-equity-long-only`
- `active_process`: `other-active`; SEI combines its quantitative active model with fundamental model portfolios from Easterly and Geneva under an integrated manager-of-managers approach
- `management_benchmark`: `Russell 2000 Index (USD)`; selected from the official fact sheet as the strategy-aligned U.S. small-cap comparator
- `track_record`: `insufficient`; operations began 2024-10-08, so the fund has less than three years of history
- `management_evidence`: `insufficient`; the available one-year and YTD comparisons are not enough under the track-record rule, and no compatible annual hit rate or longer Excess CAGR is available
- `risk_evidence`: `not-verified`; return-only differences are not called alpha and daily-NAV drawdown/recovery evidence remains unavailable

## Sources

- [SEI Select Small Cap official page](https://seietfs.filepoint.live/seis) — identity, Nasdaq listing, inception, current facts and performance access point
- [SEIS official fact sheet](https://seietfs.filepoint.live/assets/pdfs/SEIS_FactSheet.pdf) — strategy, manager allocation, official July 2026 NAV/benchmark returns, holdings, beta, expenses and portfolio characteristics
- [SEIS summary prospectus, SEC](https://www.sec.gov/Archives/edgar/data/1888997/000110465925073552/tm258862d15_497k.htm) — objective, fees, active strategy, small-cap mandate, managers and principal risks
- [Nasdaq SEIS listing notice](https://nasdaqtrader.com/TraderNews.aspx?id=ETP2024-93) — Nasdaq listing date and ticker confirmation
- [AAII SEIS performance](https://www.aaii.com/etf/ticker/SEIS) — secondary 2025 annual NAV row as of 2026-07-31
- [S&P Dow Jones Indices current all-returns table](https://www.spglobal.com/spdji/en/additional-reports/all-returns/index.dot?additionalFilterCondition=&parentIdentifier=df8ec300-24ad-4c70-81d3-a3cece0200e2&sourceIdentifier=index-family-specialization) — current S&P 500 Total Return reference as of 2026-09-01
- [[ETF_performance_sources_2026-09-02_run-5]] | [[ETF Performance Index]]
