# Jordan — Drafting & Code Reference

Legend: **✓** = read this session. Most Jordan values come from **secondary transcriptions** (a law-firm summary of the 2019 amendment to Amman Regulation 28/2018, and a third-party OCR of the old 1979 Amman Buildings & Planning Regulation) — treat them as **secondary ✓s**: confirm against the Official Gazette (الجريدة الرسمية) and the GAM/municipality zoning certificate before design. **⚠ verify** = not confirmed. Source keys [S#] in §8.

**Regime in one line:** national technical code = **Jordan National Building Code (JNBC, كودات البناء الوطني الأردني)** issued by the **Jordan National Building Council (المجلس الوطني للبناء)** under the Ministry of Public Works & Housing (MPWH) [S3]; zoning, setbacks, coverage = **municipal regulation** — Greater Amman Municipality (GAM, أمانة عمان الكبرى) "Amman Buildings & Zoning Regulation" (نظام الأبنية والتنظيم في مدينة عمان) No. 28 of 2018 as amended 2019 [S1]; outside Amman, Ministry of Local Administration / local councils use "Regulation of Buildings & Organisation outside municipalities" ⚠.

---
## 1. Units, scales, sheets, title block, language
| Item | Practice |
|---|---|
| Units | Metric. Dimensions in **m with 2 decimals** on site/setback plans, **cm or mm** on floor plans (office-specific) ⚠ |
| Datum | Levels referenced to road level / "منسوب الشارع" + `±0.00` = ground floor; plot levels from approved survey. Height measured **from ground slab level** per the zoning table ✓ [S1] |
| Language | **Arabic** official; bilingual Arabic/English common on consultant sheets. Arabic text RTL, dimension numerals Western ⚠ |
| Min scales (Amman permit, Art. 4 of 1979 reg ✓ secondary [S2]) | Site plan **1:200**; setback plan **1:200**; architectural plans/sections/elevations **1:100**; structural **1:100**; electrical/lighting **1:100**; plumbing **1:100**; roof drainage **1:200**; shelter, absorption pit, water-well details **1:50**; fence sections **1:20** — *scales stated as minimum* ✓ secondary; verify vs. current regulation ⚠ |
| Sheets | A1/A0 plots; A3 booklets ⚠ |
| Title block | Project (اسم المشروع), owner (المالك), plot no. (رقم القطعة), basin (الحوض), district (اسم الحي), village/zone, scale, date, engineer name + **Jordan Engineers Association (JEA, نقابة المهندسين) stamp & membership no.** — plans must be signed/stamped by JEA-registered engineer ⚠ |
| Area schedule | جدول مساحات: plot area, area per floor, built-up %, FAR, parking count, roof floor area (see §5.2) ✓ [S2 Art. 4(15)] |

---
## 2. CAD layer/file naming practice (what local consultants use) + any authority CAD submission rules (DWG version, coordinate system)
- No national layer standard identified. Jordanian consultants commonly use office-specific names, often bilingual in comments but ASCII in layer names: `WALL`, `DOOR`, `WINDOW`, `COLUMN`, `STAIR`, `DIM`, `TEXT`, `HATCH`, `FURN`, `SETBACK`, `PLOT_LINE`, `AXIS` ⚠ practice — no source.
- GAM accepts DWG + PDF in its online permit flow ⚠; DWG version not verified → export **DWG 2010–2018** + PDF with JEA stamp ⚠.
- Coordinate system: **Jordan Transverse Mercator (JTM)** (legacy Palestine Grid in older surveys) ⚠ exact EPSG not verified; Department of Lands & Survey (دائرة الأراضي والمساحة) supplies plot/basin sheets (حوض) ⚠.
- File naming: `PlotNo_Basin_Floor_Rev.dwg` ⚠ office convention.

---
## 3. Drafting conventions (dims, text, symbols, bilingual rules)
- **Dimensions:** setbacks to all four boundaries on the setback plan (front/side/rear) because zoning tables are expressed as front/side/rear ✓ [S1].
- Mandatory drawn items per old Art. 4 list ✓ secondary [S2]: shelter (ملجأ), absorption pit (حفرة امتصاصية) and water well (بئر مياه) details at 1:50, fence sections 1:20, roof drainage plan.
- Roof floor ("الطابق السطحي") shown separately: area ≤ 20 % of floor below and ≤ 100 m²; clear height ≤ 3.25 m; front setback ≥ 50 % of required (Art. 21 amending Art. 35, 2019) ✓ secondary [S1].
- Parking drawn with stall 5.25 × 2.50 m (2019 text) and ≥ 2.25 m clearance ✓ secondary [S1].
- Symbols: north arrow, level triangles, section marks, stair "up" arrow; text Arabic (e.g. غرفة نوم, صالون, مطبخ, حمام) with Latin duplicate ⚠.
- Hatching: new vs existing walls in additions (إضافة): partial plan for additions ≤ 60 m² once only (Art. 4(ب) ✓ secondary [S2]).


### Local terms for labels
- Plot (قطعة), basin (حوض), district (حي), setback (ارتداد), coverage (نسبة البناء/الإشغال), floor area ratio (نسبة المساحة الطابقية).
- Roof floor (طابق السطح), parking floor (طابق مواقف), basement (قبو/طابق تسوية), shelter (ملجأ), absorption pit (حفرة امتصاصية).
- Residential A/B/C/D (سكن أ/ب/ج/د), popular housing (إسكان شعبي), green housing (سكن أخضر), Civil Defence (الدفاع المدني).

---
## 4. Governing codes & authorities (table)
| Topic | Instrument | Authority |
|---|---|---|
| National technical code | **JNBC** parts (architectural, structural, loads/earthquake, electrical, mechanical, energy, fire, green) — exact part list ⚠ | Jordan National Building Council / MPWH [S3] |
| Seismic | JNBC earthquake loads + updated seismic map with **35 zones** (approved by National Building Council; Cabinet approval pending at Sept 2023 report) ✓ [S4] | Council / MPWH |
| Zoning | Amman Buildings & Zoning Reg. 28/2018 (am. 2019) ✓ [S1]; legacy 1979 reg (issued under Art. 67, Law 79/1966) ✓ [S2] | GAM; other municipalities |
| Practice licensing | Engineering profession law, JEA stamp | Jordan Engineers Association |
| Fire / life safety | Civil Defence Directorate (مديرية الدفاع المدني) approval + JNBC fire part ⚠ | Civil Defence |
| Electrical | JNBC electrical part ⚠; utilities: Jordan Electric Power Co. / EDCO / IDECO (distribution) ⚠; 230/400 V 50 Hz ⚠ | EMRC, distribution cos. |
| Water/sewer | Water Authority of Jordan / Miyahuna (Amman) ⚠ | |
| Energy efficiency | JNBC energy efficiency code ⚠ | |

---
## 5. Key numbers (residential setbacks/coverage/height, stairs, egress, doors, ceiling heights, min rooms, parking, fire basics, electrical basics, seismic zone/structural basics)

### 5.1 Amman residential zones — Reg. 28/2018 as amended 2019 (secondary ✓ [S1])
| Zone | Min plot m² | Min frontage | Setback front / side / rear | Max coverage | Max floors | Max height | Parking |
|---|---|---|---|---|---|---|---|
| Residential A (سكن أ) | 1000 | 25 m | 5 / 5 / 7 m | **39 %** | 4 | 16 m (from ground slab) | 1 per dwelling ≤ 250 m²; 2 for 250–500; 3 for ≥ 500 |
| Residential B (سكن ب) | 750 | 20 m | 4 / 4 / 6 m | **45 %** | 4 | 16 m | as A |
| Residential C (سكن ج) | 500 | 18 m | 4 / 3 / 4 m | **51 %** | 4 | 16 m | 1 |
| Residential D (سكن د) | 300 | 13 m | 3 / 2.5 / 2.5 m | **55 %** | 4 | 16 m | 1 |
| High-density residential | 1200 (subdivision projects) | 30 m | min 5 m linear (no split) | FAR ≤ 300 % | n/a | 28 m | as A/B; ≥ 10 % landscaped |
Articles: setbacks/coverage/floors = Art. 4 (replacing Art. 5); plot size = Art. 10 (am. Art. 21); parking = Art. 14 (am. Art. 26); stall dims = Art. 16 (am. Art. 30) ✓ secondary. *Old 1979 regulation had height 15 m for A–D (Art. 29) — superseded by 16 m?* ⚠ confirm with GAM.
Popular housing: front 2 / rear 2, no side (Art. 31, 1979 ✓ secondary [S2]) ⚠ current.

### 5.2 Other residential numbers (1979 regulation, third-party OCR ✓ secondary [S2]; may be superseded ⚠)
| Item | Value (article) |
|---|---|
| Clear height | bedrooms/offices **2.40 m**; kitchen & garage **2.25 m**; bath/WC **2.10 m**; other **2.50 m** (Art. 57) |
| Stair, dwellings | clear width ≥ **0.90 m**; enclosure ≥ 12 m² ⚠ (Art. 56هـ); 2nd stair when > 100 occupants or > 16 dwellings (Art. 58) |
| Riser / tread | riser ≤ **18 cm**; tread ≥ **26 cm**; 2R + T = 60–64 cm; ≤ 15 steps per flight; landing depth ≥ stair width; handrail ≥ 0.80 m (Art. 61) |
| Rooms | one-room dwelling room ≥ 16 m²; kitchen ≥ 6 m²; WC ≥ 1 m²; bath ≥ 1.5 m²; residential corridor ≥ 1.0 m (Art. 56, 59) |
| Light/vent | openings ≥ **5 %** of floor area; bedroom light well ≥ 10 m², side ≥ max(¼ height, 2.5 m); kitchen/WC well ≥ 7.5 m², width ≥ 2.5 m (Art. 53, 55) |
| Parking stall | ≥ 5.25 × 2.30 m (1979) — **2019 amendment: 5.25 × 2.50 m** ✓ [S1]; ramp ≤ 20 %, first 5 m ≤ 10 %, headroom 2.0 m; driveway 3.5 m (≤ 30 cars) (Art. 17–18) |
| Lift | required when building height > **14 m** and > 4 floors above main entrance (Art. 62) |
| Fences / walls | boundary fence ≤ 2.5 m; retaining wall ≤ 2.5 m (3.0 m in difficult terrain); roof parapet 1.0–1.5 m (Art. 15, 23) |
| Basement | full-plot basement exempt from setbacks/FAR if used for parking, shelter, storage, services (Art. 43); parking/basement floors excluded from floor & height count (Art. 44) |
| Projections | residential: architectural projections ≤ 0.75 m, balconies not beyond building line (Art. 11ب) |
| Tall buildings | require road ≥ 16 m; residential tall buildings need double side/rear setbacks (Art. 42) |
| Permit validity/timing | committee decides in 30 days; permit lapses if fees unpaid in 6 months or work not started within 1 year (Art. 5) |

### 5.3 Fire, electrical, structural basics ⚠
No verified numbers retrieved: egress widths/travel distances, fire ratings, sprinkler thresholds → JNBC fire part + Civil Defence ⚠. Electrical: 230/400 V 50 Hz ⚠. Seismic: 35 zones on JNBC map ✓ [S4]; PGA/zone factor per zone ⚠ not retrieved; Amman/Dead Sea Transform region = moderate-high ⚠. Concrete cover, minimum member sizes: JNBC structural (ACI 318 / BS-based) ⚠.

---
## 6. Permit drawing set
Five copies of application with: title deeds; site plan (≥ 1:200, by civil engineer/surveyor); setback plan; architectural plans/sections/elevations; structural plan; electrical & lighting; utility connection; plumbing; roof drainage; concrete calcs + soil bearing capacity; shelter, absorption pit, water well details; fence sections; schedule of areas; other items the committee asks. Soil test before design (Art. 6) ✓ secondary. Current GAM online system and fire/utility NOCs ⚠.

---
## 7. Common rejection reasons
1. Setbacks ignore zone (A: 5/5/7; D: 3/2.5/2.5) or coverage above 39–55 %.
2. Height > 16 m / > 4 floors (2019 table) or basement/parking floors wrongly counted.
3. Roof floor > 20 % of floor below, > 100 m², > 3.25 m high, or front setback < 50 % of required.
4. Parking short (A/B: up to 3 spaces by dwelling area), stall < 5.25 × 2.50 m, ramp > 20 %.
5. Room heights below 2.40 m (bed) / 2.25 m (kitchen) / 2.10 m (bath) per old rule ⚠.
6. Habitable room without opening onto balcony/court/well; openings < 5 % of floor.
7. Single stair where 2 required; stair under 0.90 m; riser > 18 cm.
8. No lift above 14 m/4 floors; no shelter/absorption pit drawn.
9. Plot below zone minimum area/frontage (Art. 10, 2019).
10. Missing JEA stamp/signatures; scale below minimum.


### Pre-submission checklist (Jordan / Amman — secondary sources, ⚠ confirm with GAM)
- [ ] Zone known (A / B / C / D / high-density) and plot area, frontage meet Art. 10 minimums.
- [ ] Setbacks and coverage per zone table (A 5/5/7, 39 %; B 4/4/6, 45 %; C 4/3/4, 51 %; D 3/2.5/2.5, 55 %).
- [ ] Max 4 floors, 16 m height measured from ground slab; roof floor <= 20 % / 100 m² / 3.25 m.
- [ ] Parking per dwelling by zone; stall 5.25 x 2.50 m; ramp <= 20 %.
- [ ] Clear heights checked against legacy values (2.40 / 2.25 / 2.10 m) and confirmed with GAM.
- [ ] Opening area >= 5 % of floor; light-well sizes; stair and riser/tread limits.
- [ ] Lift provided above 14 m / 4 floors.
- [ ] Shelter, absorption pit and water well details at 1:50; fence sections at 1:20.
- [ ] Seismic zone read from the 35-zone JNBC map; Civil Defence and utility approvals planned.
- [ ] JEA stamp and signatures on all sheets.

---
## 8. Sources
- [S1] Law-firm summary of the 2019 Amman amendment — https://jordan-lawyer.com/2019/07/01/2019-building-rules-in-amman-municipality/
- [S2] Amman Buildings & Planning Regulation (1979) transcription — https://jordanianlaw.com/الأنظمة/نظام-الابنية-والتنظيم-في-مدينة-عمان-صا/ (percent-encoded URL as returned by search)
- [S3] ICC summary of Jordan code regime — https://www.iccsafe.org/?p=229373 (listed in search; not fetched ⚠)
- [S4] Jordan News, seismic zones / National Building Council — https://www.jordannews.jo/Section-109/News/Jordan-approves-climate-codes-maps-35-earthquake-zones-30914
