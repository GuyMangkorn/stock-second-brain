---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:SPDW
ticker: SPDW
exchange: NYSE Arca
updated: 2026-08-29
source_batch: raw/imports/ETF_performance_sources_2026-08-29.md
return_basis: NAV total return for official fields; secondary dividend-reinvested proxy for rows marked *
management_mode: passive-index
tags:
  - analysis/etf-performance
  - geography/International
  - ticker/SPDW
---

# SPDW Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

SPDW เป็น passive developed-markets ex-U.S. ETF ที่มี official rolling 10-year NAV
Total Return `9.88%` annualized ณ 2026-07-31 และ official NAV TR YTD `14.69%`
ณวันเดียวกัน. Complete annual rows ใน reviewed official capture ไม่อยู่ในรูปแบบ
ที่อ่านและตรวจสอบได้ จึงใช้ secondary dividend-reinvested total-return proxy*
สำหรับหน้าต่าง 2016-2025 และ 2021-2025 เท่านั้น: proxy CAGR อยู่ที่ `8.70%*` และ
`9.01%*` ตามลำดับ. ตัวเลข proxy ไม่ควรถูกอ่านเป็น official NAV TR หรือใช้สรุป
tracking quality โดยตรง.

## Performance check

- `entity_key: NYSE Arca:SPDW`
- Fund: `State Street SPDR Portfolio Developed World ex-US ETF`; inception: 20 เม.ย. 2007; asset class: developed international equity
- Metric: official fields เป็น `NAV Total Return` รวมเงินปันผลและ capital gains ที่ reinvested และหักค่าใช้จ่ายตาม issuer convention
- Management mode: `passive-index` / systematic equity beta; implementation ใช้ representative sampling
- Tracked index (issuer benchmark): `S&P Developed Ex-U.S. BMI Index`
- Common benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference ไม่ใช่ tracked index ของ SPDW)
- Official rolling 10-year NAV TR: `9.88%` annualized ณ `2026-07-31`; source ไม่แสดง raw endpoints หรือ cumulative value ของ rolling field
- Official current NAV TR YTD: `14.69%` ณ `2026-07-31`; periods ต่ำกว่าหนึ่งปีไม่ annualized
- Complete calendar window: `2016-2025` secondary proxy compound `130.20%*` / rounded-input CAGR `8.70%*`; S&P 500 cache compound `298.33%` / CAGR `14.82%`
- Common window: `2021-2025` secondary proxy compound `53.94%*` / rounded-input CAGR `9.01%*`; S&P 500 cache compound `96.17%` / CAGR `14.43%`
- Coverage note: annual table ด้านล่างเป็น secondary dividend-reinvested total-return proxy จาก FinanceCharts; official State Street/SEC annual chart ใน reviewed capture ไม่ readable เพียงพอสำหรับยืนยันแถว NAV รายปี จึงติด `*` ทุกค่า SPDW และไม่ผสม proxy เข้ากับ official NAV fields

| ปี | SPDW total-return proxy* | S&P 500 TR |
|---|---:|---:|
| 2016 | 3.00%* | 11.96% |
| 2017 | 25.81%* | 21.83% |
| 2018 | -14.22%* | -4.38% |
| 2019 | 22.41%* | 31.49% |
| 2020 | 9.90%* | 18.40% |
| 2021 | 11.45%* | 28.71% |
| 2022 | -15.98%* | -18.11% |
| 2023 | 17.82%* | 26.29% |
| 2024 | 3.55%* | 25.02% |
| 2025 | 34.75%* | 17.88% |

**Up years / Down years**

- Best proxy year: 2025, **+34.75%***
- Least positive proxy year: 2016, **+3.00%***
- Worst proxy year: 2022, **-15.98%***
- Least bad proxy down year: 2018, **-14.22%***
- Official current YTD: **+14.69% NAV**, as of **2026-07-31**
- SPDW proxy beat the S&P 500 common reference in 2017, 2022, and 2025 (`3 / 10` complete years); this arithmetic comparison is not a manager-skill claim

## Risk read-through

SPDW ให้ broad developed-market ex-U.S. exposure ผ่าน Canada, Europe และ Pacific
markets โดย official current snapshot ณ 2026-08-27 แสดง NAV `USD 51.97`, closing
price `USD 52.04`, AUM `USD 42.24bn`, holdings `2,433`, P/B `2.16x`, FY1 P/E
`14.28x`, fund distribution yield `2.92%`, และ 30-day SEC yield `2.09%`. Expense
ratio อยู่ที่ `0.03%`; distribution frequency เป็น semi-annual. SEC prospectus
ยืนยัน passive sampling, การถือหลักทรัพย์/DRs อย่างน้อย 80% ของสินทรัพย์ และ
foreign-market, currency, country, sector, liquidity และ index-tracking risks.

Official daily NAV Total Return series ที่เปิดเผยเพียงพอสำหรับคำนวณ maximum
drawdown และ recovery ยัง `ไม่พบข้อมูลที่ยืนยันได้`; จึงไม่แทนที่ด้วย
market-price หรือ secondary drawdown proxy. ความเสี่ยงเชิงพฤติกรรมหลักคือ
country/region concentration, FX และ global developed-equity drawdowns; ตัวเลข
annual proxy มี timing, fee และ NAV-vs-market-price differences ที่อาจทำให้
ต่างจาก official NAV return.

## Sources

- [State Street SPDW product page](https://www.ssga.com/us/en/intermediary/etfs/state-street-spdr-portfolio-developed-world-ex-us-etf) — identity, benchmark, current NAV/price, AUM, holdings, valuation metrics, current YTD and rolling performance
- [State Street SPDW factsheet](https://www.ssga.com/library-content/products/factsheets/etfs/us/factsheet-us-en-spdw.pdf) — official 2026-06-30 NAV total-return fields, expense ratio and fund characteristics
- [SEC SPDW summary prospectus](https://www.sec.gov/Archives/edgar/data/1168164/000119312526031210/d86341d497k.htm) — passive sampling, index objective, diversification, turnover and risks
- [FinanceCharts SPDW performance](https://www.financecharts.com/etfs/SPDW/performance) — secondary dividend-reinvested annual total-return proxy; not substituted for official NAV TR
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached source references in `check-etf-performance` — common USD total-return benchmark for 2016-2025
- [[ETF_performance_sources_2026-08-29]] | [[ETF Performance Index]]
