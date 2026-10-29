# Kuwait — Drafting & Code Reference

Legend: **✓** = read this session, but note **no official Municipality text could be opened** (baladia.gov.kw returned an access-denied page). Private-housing numbers below come from **Al-Anba press reports (22 and 26 March 2024) of the Municipal Council's amended private/model housing regulation** and a Kuwait summary PDF — reported rules, not the gazette text; two outlets disagree on max height (18 m vs 20 m). Mark = **⚠ verify** against the Municipality's Ministerial Decision text before design. Source keys [S#] in §8.

**Regime in one line:** Building rules = **Ministerial Decision 206 of 2009 "regulating building works and annexed tables"** (تنظيم أعمال البناء والجداول الملحقة به), amended repeatedly — latest seen: **Decision 393 of 2025** (agricultural/other provisions) ✓ listing [S5]; private & model housing tables amended by Municipal Council in March 2024 and published in the Official Gazette (applied from ~June 2024) ✓ press [S1][S2]; **Decision 288 of 2024** is cited as governing building ratio/setbacks/attachments for private & model residences, with a May 2025 proposal (10 municipal councillors) to exempt up to **100 m² second-floor roof construction** on plots **≤ 365 m²** from the ratio ✓ press [S3] (status ⚠).

---
## 1. Units, scales, sheets, title block, language
| Item | Practice |
|---|---|
| Units | Metric. Plan dimensions **m (2 decimals)** or **cm** by office; areas **m² (م²)**; levels `+0.00` ⚠ practice |
| Levels | Datum = **adjacent road / sidewalk level**: rules cite "average sidewalk level" and the "more elevated internal street" for basement and boundary-wall heights ✓ [S2] |
| Language | **Arabic + English bilingual**; Arabic governs; RTL title block ⚠ practice |
| Scales | Site 1:200–1:500; plans/sections/elevations 1:100 (1:50 detail); fence/gate 1:50 ⚠ practice (Municipality checklist unreadable) |
| Sheets | A1/A0 (594×841 / 841×1189) for permit, A3 for calcs ⚠ |
| Title block | Project, owner (المالك), **Area (المنطقة) / Block (القطعة) / Plot (القسيمة) / Street (الشارع)**, transaction no. (رقم المعاملة), consultant stamp (Kuwait Society of Engineers), date, revision ⚠ practice |
| Area schedule | Plot area; area per floor; basement; building ratio % ; excluded areas listed separately (lift/stair, canopies, pergola); roof structures ✓ [S2] |
| Orientation | North arrow; service-street vs main-street clearly labelled (the rules differ per street type ✓ [S2]) |

---
## 2. CAD layer/file naming practice (what local consultants use) + any authority CAD submission rules (DWG version, coordinate system)
- No official layer standard found. Kuwait consultants use in-house/AIA-style English layers (`A-WALL`, `A-DOOR`, `A-GLAZ`, `A-ANNO-DIMS`, `S-COLS`, `E-POWR`, `M-HVAC`, `P-SANR`) and Arabic text styles (e.g. `Arial`/`Simplified Arabic`) ⚠ practice, no source.
- Municipality e-submission format (DWG version/PDF) ⚠ not verified → export DWG 2013 + signed PDF.
- Coordinate system: Kuwait Municipality survey sheets are georeferenced to the national grid (Kuwait UTM 39N / KOC Lambert variants) ⚠ EPSG not verified. Plot (قسيمة) boundary comes from the Municipality survey/“مخطط” — never redraw it.
- Layer for areas excluded from ratio is useful: `AREA-EXCL` etc. ⚠.

---
## 3. Drafting conventions (dims, text, symbols, bilingual rules)
- Dimension **setbacks from each boundary**; label plot frontages: main street, **service street (شارع الخدمة)**, other street. Ratio rules differ by side (boundary construction allowed on ground floor up to **70 %** of the frontage length, not on the service-street side, reported draft; **90 %** for the service-street boundary side per a later report — conflict ⚠) [S1][S2].
- Show roof structures (stair house, machine room, tank cover, pergola) with areas and the 4 m setback from parapet ✓ [S1 draft].
- Parapet heights drawn: 2 m main roof, 1 m on permitted second-floor roof structures, 0.5 m on ground-floor attached parts (reported) ✓ [S1].
- Text: Arabic room names (غرفة نوم، مطبخ، حمام، ديوانية، سرداب، بيت درج، غرفة آلات). Basement = **سرداب**.
- Symbols: lift shaft + lobby (excluded up to 7 m²/floor), canopies, pergola (بيرجولا), covered walkway (ممر مغطى) ✓ [S2].
- Hatch non-counted areas differently; add a calc table matching the Municipality exclusions.


### Local terms for labels
- Plot (قسيمة), block (قطعة), area (منطقة), service street (شارع الخدمة), basement (سرداب), stair house (بيت الدرج).
- Building ratio (نسبة البناء), setback (ارتداد), roof structures (منشآت السطح), pergola (بيرجولا), parapet (دروة/حاجز السطح).
- Private housing (السكن الخاص), model housing (السكن النموذجي), investment housing (السكن الاستثماري).
- Municipality (البلدية), Fire Service (الإطفاء), Electricity & Water (الكهرباء والماء).

---
## 4. Governing codes & authorities (table)
| Topic | Instrument | Authority |
|---|---|---|
| Building works, ratios, setbacks | Ministerial Decision **206/2009** + tables; amendments 288/2024 (private/model housing) and **393/2025** ✓ [S3][S5] | **Kuwait Municipality (بلدية الكويت)** under Ministry of State for Municipal Affairs |
| Housing allocation plots | Public Authority for Housing Welfare (PAHW) plot standards (e.g. min. 375 m² outside Kuwait City, per a market report; ⚠ weak source) | PAHW |
| Fire | **Kuwait Fire Protection Regulations 2014** (KFSD, ~229 pp.; classifications by use/hazard, permits, materials, fire-spread, basements, fire-rating schedules) ✓ title/summary only [S6]; Fire Law exempts **private housing** from KFSD requirements except smoke detectors/extinguishers advice (older report) ⚠ [S7] | **Kuwait Fire Service Directorate / Kuwait Fire Force (KFSD/KFF)** |
| Electrical & water | **MEW** wiring/installation regulations (Ministry of Electricity, Water & Renewable Energy) ⚠ ; supply **240/415 V, 50 Hz** ⚠ | MEW |
| Structural | Kuwait Municipality structural/geotech requirements; Kuwait is low-to-moderate seismicity — seismic design per UBC/IBC-based municipal guidance ⚠ | Municipality; Kuwait Institute for Scientific Research ⚠ |
| Energy | Kuwait Energy Conservation Code (MEW) ⚠ | MEW |

---
## 5. Key numbers (residential setbacks/coverage/height, stairs, egress, doors, ceiling heights, min rooms, parking, fire basics, electrical basics, seismic zone/structural basics)

### 5.1 Ratio, height, floors
| Item | Value |
|---|---|
| Building ratio | **210 %** of plot for plots **> 400 m²** (or 960 m² if greater, in the draft) ✓ press; 350–400 m²: 210 % + 120 m²; 250–350 m²: up to 800 m² built area, 3 floors ✓ draft [S2] |
| Floors | **max 3 incl. ground floor** ✓ [S1][S2] |
| Max height | **18 m** (main text) vs **20 m** (headline) — conflict ⚠ [S1][S2] |
| Min net floor height | **3.00 m** ✓ [S2] |
| Basement (سرداب) | **one only, full plot**; ≤ **1.80 m** above average sidewalk level; net height **2.75–5.00 m**; ground floor + basement one unit; not counted in ratio ✓ [S2] |
| Roof structures | ≤ 4 m high; stair-house ≤ **25 m²**; machine room ≤ 25 m² (within 100 m² roof allowance); tank-cover canopy ≤ 1.80 m; pergolas ≤ 20 m²; pergolas/canopies total ≤ **10 %** plot ✓ [S1] |
| Excluded from ratio | basement; lift shafts + stair/lift lobby ≤ **7 m²/floor**; stair-house roof ≤ 25 m²; covered open walkways ≤ **5 %** plot; entrance canopies ≤ 3 m wide ✓ [S2] |
| Second-floor roof structures | ≤ 100 m² and counted in ratio (proposal to exclude on ≤ 365 m² plots ⚠) [S3] |
| Lifts | one in main building; 2nd lift for plots ≥ 750 m² (smaller plots only for certified disability); max 2 per plot; food lift shaft ≤ 1.2 m wide not reaching roof ✓ [S1] |
| Boundary wall (perimeter) | ≤ **3.00 m** ✓ [S2] |

### 5.2 Setbacks (reported draft) ✓ [S2]
| Plot | Service street | Other sides (from 1st floor) | Corner sight line |
|---|---|---|---|
| < 750 m² | **2.0 m** | **1.5 m** | 1.5 m |
| ≥ 750 m² | **3.0 m** | **2.0 m** | 2.0 m |
Frontage ≤ 20 m on service street → 1.5 m to neighbours/other streets. Ground floor may be built to boundary (≤ 70 % of frontage, not on service-street side). Balcony or A/C duct projection on neighbour side ≤ **0.60 m** ✓ [S1]. Gate/door at a 90° plot corner ≥ **5 m** from adjacent plot edge ✓ [S2].

### 5.3 Rooms/units (reported draft ✓ [S2])
Bedroom ≥ **10 m²**, min width 3.0 m; kitchen ≥ **7.5 m²**, width 2.0 m; bathroom ≥ 4 m², width 1.75 m; toilet ≥ 1.5 m², width 1.2 m; internal corridor ≥ **1.20 m** clear. Unit rule: one unit per floor, except second floor may be split (two apartments).

### 5.4 Investment housing context (do not mix with private) ✓ [S4]
Building ratio **400 %** inside Kuwait City, **250 %** outside; height 200 m / 160 m; net apartment ≥ 50 m² (2022 draft; later report says 60 m² net, 12 m² bedroom ⚠).

### 5.5 Not found — ⚠ all
Stair width/riser/tread, door widths, parking ratios (a draft sec. 17: parking inside plot, parking floors excluded from ratio but counted in height/floors ✓ [S4]), egress distances, fire ratings, electrical sizing, seismic zone factor. Do not invent; extract from KFSD 2014 and Municipality schedules.

---
## 6. Permit drawing set
Municipality building licence: ownership/plot certificate (shahada), survey plan, architectural set (site, basement, ground, 1st, 2nd, roof, 4 elevations, ≥ 2 sections, fence/gate), area/ratio table, structural drawings + soil report, MEP (electrical load, plumbing, drainage), KFF approval where applicable (non-private-housing), MEW load approval. Exact list ⚠ not retrievable.

---
## 7. Common rejection reasons
1. Ratio calc includes/excludes wrong areas (lift/stair > 7 m², canopies > 3 m, walkways > 5 %).
2. Basement more than one level or not full-plot-unified with ground floor; > 1.80 m above sidewalk.
3. Height > 18 m (or 20 m per final text) / 4th floor.
4. Setbacks wrong for plot size (< 750 vs ≥ 750 m²).
5. Roof structures > 25 m² stair house, tall (> 4 m), or missing 4 m parapet setback.
6. Rooms below 10 m² bedroom / 7.5 m² kitchen; corridor < 1.20 m.
7. Boundary wall > 3 m.
8. Second lift on < 750 m² plot without disability certificate.
9. Balcony/A-C projection beyond 0.60 m on neighbour side.
10. Boundary construction beyond 70 % frontage or on service street.


### Pre-submission checklist (Kuwait private residence — numbers from §5, ⚠ confirm against gazette)
- [ ] Plot area band known (250–350 / 350–400 / > 400 m²) and ratio formula chosen accordingly.
- [ ] Floors <= 3 incl. ground; height <= 18 m (check 20 m reading with Municipality).
- [ ] Net floor height >= 3.00 m on every floor; basement net 2.75–5.00 m, <= 1.80 m above sidewalk.
- [ ] Setback table matches plot size (< 750 m²: 2.0 / 1.5 m; >= 750 m²: 3.0 / 2.0 m).
- [ ] Boundary construction <= 70 % of frontage, ground floor only, not on service street.
- [ ] Excluded areas separately tabulated: lift/stair lobby <= 7 m² per floor, stair house <= 25 m², walkway <= 5 % plot.
- [ ] Roof: structures <= 4 m high, 4 m from parapet on main/service streets, parapet 2 m / 1 m / 0.5 m.
- [ ] Rooms: bedroom >= 10 m² (3 m wide), kitchen >= 7.5 m² (2 m), bath >= 4 m², WC >= 1.5 m², corridor >= 1.20 m.
- [ ] Lifts: one main; second only on >= 750 m² plots or documented disability.
- [ ] Boundary wall <= 3.00 m; projections on neighbour side <= 0.60 m.

---
## 8. Sources
- [S1] Al-Anba, Council approves private housing ratios — https://www.alanba.com.kw/1230327 (26 Mar 2024)
- [S2] Al-Anba, 210 % ratio for plots > 400 m² (draft detail) — https://www.alanba.com.kw/1229983 (22 Mar 2024); summary PDF https://wikikuwait.com/wp-content/uploads/2024/03/%D9%84%D8%A7%D8%A6%D8%AD%D8%A9-%D8%A7%D9%84%D8%A8%D9%86%D8%A7%D8%A1-%D8%A7%D9%84%D8%AC%D8%AF%D9%8A%D8%AF%D8%A9-%D9%81%D9%8A-%D8%A7%D9%84%D8%B3%D9%83%D9%86-%D8%A7%D9%84%D8%AE%D8%A7%D8%B5-%D9%88%D8%A7%D9%84%D9%86%D9%85%D9%88%D8%B0%D8%AC%D9%8A-pdf.pdf
- [S3] Al-Jarida, Decision 288/2024 amendment proposal — https://www.aljarida.com/article/97913/amp (14 May 2025)
- [S4] Argaam/Al-Qabas draft regulation report (30 Jun 2022) — https://argaam.com/ar/article/articledetail/id/1571488
- [S5] Decision 393/2025 listing — https://lawskw.com (search result; not fetched ⚠)
- [S6] Kuwait Fire Protection Regulations 2014 (Scribd copy, unofficial, summary only) — https://www.scribd.com/document/428982882/KFSD-Code
- [S7] Kuwait Times / GDN on fire law and private housing — https://kuwaittimes.com/kuwait-fire-force-law-meets-goals-of-protecting-lives-and-properties
