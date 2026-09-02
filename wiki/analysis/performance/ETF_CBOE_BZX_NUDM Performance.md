---
type: etf-performance
instrument_type: ETF
entity_key: Cboe BZX:NUDM
input_ticker: NUDM
ticker: NUDM
exchange: Cboe BZX
fund: Nuveen ESG International Developed Markets Equity ETF
tracked_index: Nuveen ESG International Developed Markets Equity Index — USD Net Return
benchmark: S&P 500 Total Return
management_mode: passive-index
updated: 2026-09-02
performance_as_of: 2025-12-31 (official calendar rows)
calendar_years_as_of: 2025-12-31
current_ytd_as_of: 2026-06-30
price_nav_as_of: not disclosed in reviewed official sources
fund_facts_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-09-02_recheck.md
return_basis: NAV total return; distributions reinvested
return_currency: USD
primary_region: International
tags:
  - analysis/etf-performance
  - ticker/NUDM
  - geography/International
---

# NUDM Performance

> [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

NUDM เป็น Nuveen ESG International Developed Markets Equity ETF แบบ
passive/indexing ที่ลงทุนในหุ้น developed markets นอกสหรัฐฯ และแคนาดา โดยใช้ ESG,
controversial-business และ low-carbon screens. Official NAV Total Return สำหรับ
complete calendar years 2018-2025 สะสม `76.99%` และ rounded-input CAGR `7.40%`;
ช่วง 2021-2025 สะสม `50.64%` / CAGR `8.54%`. Current official NAV TR YTD ล่าสุดที่
ยืนยันได้คือ `+10.10%` ณ 2026-06-30.

## Performance check

- `entity_key: Cboe BZX:NUDM`; the issuer factsheet identifies the primary exchange as `Cboe` and ticker `NUDM`; the Cboe BZX venue is used for the exchange-qualified project key.
- Fund: `Nuveen ESG International Developed Markets Equity ETF`; inception `2017-06-06`; management mode `passive-index`; the fund seeks to track the `Nuveen ESG International Developed Markets Equity Index` before fees and expenses.
- Classification: supported passive equity ETF. The index uses a rules-based process for developed-market equities excluding the U.S. and Canada, with ESG, controversial-business involvement and low-carbon screens, and quarterly rebalancing.
- Metric: USD `NAV Total Return`, with distributions reinvested; market-price returns are kept separate. The 2017 launch year is partial and is not ranked or included in the complete-year calculations.
- Tracked index: `Nuveen ESG International Developed Markets Equity Index — USD Net Return`. Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference only, not the issuer benchmark). Cached S&P rows are as of 2025-12-31.
- Available complete-year window: eight annual rows from 2018 through 2025; normalized calculation `100.00 at 2017-12-31 → 176.99 at 2025-12-31`.
- NAV TR CAGR: `7.40%`, calculated from eight official complete calendar-year rows using `(End TR / Start TR)^(1 / Years) - 1`; this is a rounded-input calculation, not an issuer-reported endpoint CAGR.
- Current official snapshot: NAV TR YTD `+10.10%` as of 2026-06-30; expense ratio `0.27%`, SEC 30-day yield `2.33%`, distribution frequency annually, total net assets `US$698.26M`, `76` positions, forward P/E `17.39x`, and weighted average market cap `US$126.09B` as of 2026-06-30.
- Management continuity: the issuer states that Teachers Advisors, LLC merged into Nuveen Asset Management, LLC effective 2026-08-01, with no investment-strategy or portfolio-management change; Nuveen Asset Management became sub-adviser.
- Source wording note: the product-page and dated-factsheet presentations of adviser/sub-adviser roles differ after the 2026-08-01 merger; this page uses the dated factsheet statement above and does not infer a strategy change.

| Year / window | NUDM NAV TR | Nuveen ESG index — USD Net Return | S&P 500 TR |
|---|---:|---:|---:|
| 2018 | -14.63% | -14.47% | -4.38% |
| 2019 | 24.28% | 24.66% | 31.49% |
| 2020 | 10.74% | 11.14% | 18.40% |
| 2021 | 10.21% | 10.52% | 28.71% |
| 2022 | -15.08% | -14.94% | -18.11% |
| 2023 | 17.89% | 18.19% | 26.29% |
| 2024 | 5.55% | 5.80% | 25.02% |
| 2025 | 29.35% | 29.87% | 17.88% |
| 2018-2025 cumulative | 76.99% | 80.91% | 192.03% |
| 2018-2025 CAGR | 7.40% | 7.69% | 14.33% |
| 2021-2025 cumulative | 50.64% | 52.67% | 96.17% |
| 2021-2025 CAGR | 8.54% | 8.83% | 14.43% |
| 2026 YTD | 10.10% | 10.26% | not synchronized |

**Up years / Down years**

- Up years / Down years: `6 / 2` across complete 2018-2025 calendar years.
- Best: 2025, `+29.35%`.
- Least positive: 2024, `+5.55%`.
- Worst: 2022, `-15.08%`.
- Least bad down year: 2018, `-14.63%`.
- Current official NAV TR YTD: `+10.10%` as of 2026-06-30; no synchronized current S&P 500 YTD comparison is inferred.

## Risk read-through

NUDM มีความเสี่ยงจาก developed-market ex-U.S./Canada, currency, country/sector
concentration และการตัดหุ้นตาม ESG/controversial-business/low-carbon screens ซึ่ง
อาจทำให้พลาดหุ้นหรือโอกาสบางส่วนที่กองทุนทั่วไปถือได้. Population standard
deviation ที่คำนวณจาก annual NAV rows แบบปัดเศษคือ `15.33%` สำหรับ 2018-2025 และ
`14.73%` สำหรับ 2021-2025; ตัวเลขนี้ไม่ใช่ issuer daily-volatility field.
Maximum drawdown, recovery duration, downside capture และ risk-adjusted metrics
ที่ใช้ daily NAV ได้ยังเป็น `ไม่พบข้อมูลที่ยืนยันได้` จากหลักฐานที่ตรวจสอบ.
Expense ratio คือ `0.27%` และกองทุนจ่าย distribution annually.

## Sources

- [Nuveen official NUDM product page](https://www.nuveen.com/en-us/exchange-traded-funds/nudm-nuveen-esg-international-developed-markets-equity-etf) — fund identity, passive/indexing approach, strategy and index scope; accessed 2026-09-01
- [Nuveen official NUDM factsheet](https://documents.nuveen.com/Documents/Nuveen/Viewer.aspx?download=1&uniqueId=02852fbf-974a-433c-9b45-56a6a1289a83) — 2018-2025 NAV and index rows, 2026 YTD, return basis, fund facts and risk disclosures as of 2026-06-30
- [SEC NUDM summary prospectus](https://www.sec.gov/Archives/edgar/data/1635073/000119312526080207/d40382d497k.htm) — official prospectus, Cboe BZX listing, fund objective, risks and fee disclosure
- [MSCI index page](https://www.msci.com/indexes/index/713162/nuveen-esg-international-developed-markets-equity-index) — index identity and provider context
- [MSCI index factsheet](https://www.msci.com/documents/1296102/5161905/tiaa_esg_international_developed_markets_equity_index_usd_net.pdf/c086131e-2b0a-52de-ffec-ad056865129f) — USD net-return index context
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common benchmark definition
- Cached S&P 500 TR references: [2018-2022](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), [2021](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/), and [2022-2025](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/)
- ETF source batch: [[ETF_performance_sources_2026-09-02_recheck]]
