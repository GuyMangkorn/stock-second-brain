---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:IDX
ticker: IDX
exchange: NYSE Arca
fund: VanEck Indonesia Index ETF
tracked_index: MVIS Indonesia Index (MVIDXTR)
benchmark: S&P 500 Total Return
updated: 2026-08-29
performance_as_of: 2026-07-31
current_ytd_as_of: 2026-08-14
price_nav_as_of: 2026-08-14
fund_facts_as_of: 2026-07-31
source_batch: raw/imports/ETF_performance_sources_2026-08-29.md
return_basis: NAV total return
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/IDX
  - geography/Indonesia
  - style/emerging-market
---

# IDX Performance

> Navigation: [[ETF Region Index]] → [[Indonesia ETF]] → [[ETF Performance Index]]

## Bottom line

`IDX` ในที่นี้คือ `VanEck Indonesia Index ETF` ที่จดทะเบียนบน `NYSE Arca` ไม่ใช่
ดัชนี IDX Composite ของตลาดหุ้นอินโดนีเซีย. Latest official daily snapshot อยู่ที่
NAV `$11.22`, NAV YTD `-32.77%` และ total net assets `$36.45M` ณ 14 ส.ค. 2026.
Latest standardized month-end table ณ 31 ก.ค. 2026 รายงาน rolling 1Y/3Y/5Y/10Y
NAV annualized ที่ `-26.74%` / `-13.43%` / `-6.74%` / `-5.02%`. ผลตอบแทนยัง
ติดลบหลายช่วงเวลา จึงยังไม่มีหลักฐานยืนยันการกลับตัวเป็นขาขึ้นแบบยั่งยืน.

## Performance check

- `entity_key: NYSE Arca:IDX`
- Fund: VanEck Indonesia Index ETF; inception `15 ม.ค. 2009`; passive,
  index-tracking equity ETF; gross/net expense ratio `0.86%` / `0.57%`
  (contractual net cap ถึงอย่างน้อย 1 พ.ค. 2027)
- Metric: `NAV Total Return` รวม distributions ที่ reinvested และหัก fund expenses
- Tracked index (issuer benchmark): `MVIS Indonesia Index (MVIDXTR)`
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference
  benchmark ไม่ใช่ tracked index ของ IDX)
- Latest official month-end performance ณ 2026-07-31: NAV `1M 10.72%`, `3M -15.62%`,
  `YTD -34.87%`, `1Y -26.74%`, `3Y -13.43%`, `5Y -6.74%`, `10Y -5.02%`, life `3.63%`;
  MVIS index `11.53%`, `-17.48%`, `-36.54%`, `-28.59%`, `-13.86%`, `-7.04%`,
  `-4.91%`, `4.00%` ตามลำดับ.
- Quarter-end cross-check ณ 2026-06-30: NAV 1Y/3Y/5Y/10Y `-30.93%` / `-15.82%` /
  `-8.96%` / `-5.49%`; issuer does not expose raw start/end TR endpoints.
- Latest official daily snapshot ณ 2026-08-14: NAV `$11.22`, current YTD NAV TR
  `-32.77%`, total net assets `$36.45M`; daily holdings `72` ณ 2026-08-13.
- Latest secondary market close located ณ 2026-08-27: market price `$11.59`; no
  same-date official closing NAV was exposed, so price and NAV are not reconciled.
- Annual coverage: `secondary total-return proxy*` ปี 2016-2025; official SEC
  prospectus แสดง annual chart เป็นภาพ แต่ไม่เปิดค่าตัวเลขในข้อความ

| ปี | IDX TR proxy* | S&P 500 TR |
|---|---:|---:|
| 2016 | 16.67% | 11.96% |
| 2017 | 19.25% | 21.83% |
| 2018 | -10.46% | -4.38% |
| 2019 | 6.13% | 31.49% |
| 2020 | -7.45% | 18.40% |
| 2021 | -2.60% | 28.71% |
| 2022 | -9.39% | -18.11% |
| 2023 | 1.97% | 26.29% |
| 2024 | -9.75% | 25.02% |
| 2025 | 13.83% | 17.88% |

`*` ตาราง IDX เป็น secondary total-return proxy จาก FinanceCharts ไม่ใช่ annual
NAV TR ที่ issuer เปิดเผย จึงไม่ใช้แทน rolling NAV CAGR หรือจัดอันดับร่วมกับ
กองที่มี official annual NAV TR. Proxy 2016-2025 cumulative/CAGR คือ `13.13%`
และ `1.24%`; 2021-2025 cumulative/CAGR คือ `-7.55%` และ `-1.56%`. S&P 500
common benchmark ใช้ cached USD TR convention ณ 31 ธ.ค. 2025.

## Up years / Down years

- Up years / Down years: `5 / 5` ใน proxy window 2016-2025
- Best: 2017, `+19.25%*`
- Least positive: 2023, `+1.97%*`
- Worst: 2018, `-10.46%*`
- Least bad down year: 2022, `-9.39%*`
- Current YTD: `-32.77%` official NAV ณ 14 ส.ค. 2026; FinanceCharts secondary
  partial-year total-return capture อยู่ที่ `-29.25%` และ market close ณ 27 ส.ค.
  อยู่ที่ `$11.59`; ทั้งสองเป็นคนละ basis/as-of date และไม่ใช้ยืนยัน trend reversal.

## Risk read-through

Rolling 10-year NAV CAGR ติดลบและ 3Y/5Y ก็ยังติดลบ สะท้อนว่า cheap valuation
ยังไม่เพียงพอให้เกิด rerating. Official factsheet ณ 31 ก.ค. 2026 รายงาน P/E
`10.73x`, P/B `1.40x`, top 10 holdings `50.53%`, sector หลักคือ Financials
`26.4%`, Materials `23.2%`, Industrials `12.7%` และ Energy `12.4%`; country
exposure คือ Indonesia `77.63%` และ China `14.07%`. โครงสร้างนี้ทำให้ IDX ไวต่อ
ดอกเบี้ย, Rupiah, commodity cycle, bank earnings และ China risk มากกว่าตลาดโลก
แบบกระจาย. Official daily NAV TR series สำหรับคำนวณ maximum drawdown/recovery
date: `ไม่พบข้อมูลที่ยืนยันได้`. Total net assets ล่าสุดจาก official daily
snapshot คือ `$36.45M` ณ 14 ส.ค. 2026 จึงยังควรเผื่อ liquidity/bid-ask risk.

## Indonesia macro overlay and reversal scenarios (source snapshot 2026-07-19)

กรอบเวลา: 6-12 เดือน. Causal chain คือ growth และ employment ช่วยพยุง earnings
แต่ policy/FX/governance risk ยังขวาง multiple expansion. GDP Q1 2026 โต `5.61%`
และ unemployment `4.68%`; TFR `2.13` เป็น long-run demand tailwind. อย่างไรก็ดี
BI-Rate `5.75%` เทียบ headline inflation `3.34%` ให้ ex-post real policy-rate
ประมาณ `+2.41 percentage points` (คำนวณแบบหยาบ) ขณะที่ CPI corruption score
ของ Indonesia อยู่ที่ `34/100`; จึงยังไม่ใช่สภาพแวดล้อมที่เอื้อต่อการลด discount rate
อย่างชัดเจน. ค่าใช้จ่ายอาหารเฉลี่ยระดับประเทศราว `Rp804,430/คน/เดือน` และค่าใช้จ่าย
คนโสดใน Jakarta ราว `Rp8.44M/เดือน ไม่รวมค่าเช่า` เป็นข้อมูลประกอบที่ชี้ว่า
ฐานต้นทุนต่ำ แต่ purchasing power ในเมืองกับระดับประเทศแตกต่างกันมาก.

| Scenario | เงื่อนไข | ผลต่อ IDX |
|---|---|---|
| Base | GDP ยังใกล้ 5%, BI คงดอกเบี้ยสูง, Rupiah/foreign flow ผันผวน | รีบาวด์เป็นช่วง ๆ ได้ แต่ยัง choppy; ยังไม่ยืนยัน trend reversal |
| Bull / Upside | เงินเฟ้อและ FX ผ่อนคลายจน BI pause/cut, bank credit/earnings ฟื้น, FDI และ governance/logistics reform เดินหน้า | financials และ domestic-demand shares นำการ rerating; โอกาสกลับตัวชัดขึ้น |
| Bear / Downside | FX อ่อนต่อ, inflation สูงกว่าขอบบน target, BI ต้องตึงตัว, commodity/China shock หรือ foreign outflow ต่อเนื่อง | ทำ low ใหม่ได้ แม้ valuation ดูถูก |

**Signposts:** BI-Rate จาก `5.75%` ต้องหยุดขึ้นหรือเริ่มลด, inflation ต้องไม่ทะลุ
ขอบบน target, Rupiah และ foreign flows ต้องหยุดทำจุดต่ำใหม่, bank credit/earnings
ต้องฟื้น และหุ้นใน Materials/Energy ต้องไม่ลากดัชนีลงต่อ.

**Falsifier:** หากเงินเฟ้อ/FX บังคับให้ BI ขึ้นดอกเบี้ยอีก พร้อม foreign outflow และ
earnings revisions ลงต่อ มุมมอง tactical rebound จะถูกยกเลิก. สรุปเชิงวิเคราะห์:
`มีโอกาสรีบาวด์ แต่ยังรอ confirmation`; ระยะยาวควรถือเป็น high-beta country/sector
bet ไม่ใช่ pure Indonesia macro proxy.

## Sources

- [VanEck IDX product page](https://www.vaneck.com/us/en/investments/indonesia-index-etf-idx?audience=retail&country=us) — current official NAV/YTD, fees, holdings and product-page performance through the reviewed 2026-08-14 capture
- [VanEck IDX fact sheet](https://www.vaneck.com/us/en/investments/indonesia-index-etf-idx-fact-sheet.pdf) — official July standardized returns, valuation, top-10 concentration, country/sector weights, yield and fee cap
- [SEC summary prospectus](https://www.sec.gov/Archives/edgar/data/1137360/000113736026000469/vaneckindonesiaindexetfidx.htm) — fund objective, calendar-year chart, passive/non-diversified classification and risk disclosures
- [FinanceCharts IDX performance](https://www.financecharts.com/etfs/IDX/performance) — secondary annual total-return proxy and current partial-year/period cross-check, clearly separated from official NAV TR
- [Investing.com IDX historical data](https://www.investing.com/etfs/marketvectors-indonesia-index-historical-data) — secondary 27 Aug 2026 market price cross-check
- [BPS Q1 2026 GDP, labor and demographics](https://www.bps.go.id/en/news/2026/05/06/910/ekonomi-indonesia-resilien-dan-tumbuh-solid--pada-triwulan-1-2026.html)
- [Bank Indonesia BI-Rate indicator](https://www.bi.go.id/en/statistik/indikator/bi-rate.aspx)
- [BPS June 2026 inflation](https://www.bps.go.id/en/pressrelease/2026/07/01/2590/inflasi-year-on-year--y-on-y--pada-juni-2026-sebesar-3-34-persen-.html)
- [Transparency International CPI 2025 Asia-Pacific](https://www.transparency.org/en/press/corruption-perceptions-index-2025-stalling-anti-corruption-progress-asia-pacific-public-anger-surges)
- [KPK SPI 2025 dashboard](https://spi.kpk.go.id/dashboard/hasil/)
- [BPS September 2025 consumption expenditure](https://www.bps.go.id/en/publication/2026/05/29/057b21b35bc236c5ede9d160/expenditure-for-consumption-of-indonesia-september-2025.html) and [Katadata BPS-based food-spending summary](https://databoks.katadata.co.id/produk-konsumen/statistik/6a18ecc8f1404/pengeluaran-warga-ri-untuk-rokok-melampaui-belanja-beras-pada-september-2025)
- [Numbeo Jakarta cost-of-living estimate](https://www.numbeo.com/cost-of-living/in/Jakarta) — crowd-sourced urban indicator, not a national official average
- [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — benchmark identity; annual rows reuse the cached 2016-2025 USD TR convention
