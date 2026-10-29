# Oman — Drafting & Code Reference

Legend: **✓** = read this session (secondary where noted). **⚠ verify** = not confirmed. Oman is in a **transition**: legacy municipal rules (Muscat Municipality Local Order 23/92 and per-governorate rules) coexist with the new MoHUP land-planning regulation and the ICC-based **Oman Building Code (OBC)**, whose enforcement is phased. Always check the plot's planning certificate (شهادة موقع / تخطيط) first. Source keys [S#] in §8.

**Regime in one line:** Ministry of Housing and Urban Planning (MoHUP, وزارة الإسكان والتخطيط العمراني) + Ministry of Interior / municipalities (Muscat Municipality, بلدية مسقط, other governorate municipalities) license buildings; fire clearance by Civil Defence (ROP → **PACDA**, Public Authority for Civil Defence and Ambulance); electricity by licensed utilities regulated by **APSR** (Authority for Public Services Regulation) ⚠ names/roles to confirm.

---
## 1. Units, scales, sheets, title block, language
| Item | Practice |
|---|---|
| Units | Metric. Dimensions **mm or m** by office; levels `+0.00` m; areas m² |
| Datum | Levels relative to adjacent road/plot level (survey benchmark from municipality) ⚠ |
| Language | **Arabic + English** bilingual; Arabic prevails on official forms ⚠ practice |
| Scales | Site 1:200–1:500, plans/elevations/sections 1:100, details 1:20–1:5, boundary wall/gate 1:50 ⚠ practice |
| Sheets | A1/A0 plots; A3 booklets ⚠ |
| Title block | Project, owner (المالك), plot no. (رقم القطعة), plan/block no. (المخطط), wilayat/governorate (الولاية/المحافظة), consultant (registered with Ministry/Oman Society of Engineers), drawing no., revision ⚠ practice |
| Area schedule | Plot area, ground coverage % per floor, total built area, parking count, setbacks table (see §5.2); roof facilities % (see §5.3) |
| Orientation | North arrow; street names/widths; adjacent plot numbers |

---
## 2. CAD layer/file naming practice (what local consultants use) + any authority CAD submission rules (DWG version, coordinate system)
- No national layer standard found. Common practice: English AIA-style layers (`A-WALL`, `A-DOOR`, `A-GLAZ`, `A-ANNO-TEXT`, `S-COLS`, `E-POWR`, `M-HVAC`, `P-SANR`) with Arabic text styles ⚠ practice, no source.
- Municipal e-submission (Muscat Municipality e-services, MoHUP platforms) DWG version / PDF format ⚠ not verified → export DWG 2013 + signed PDF.
- Coordinates: projected national CRS commonly **WGS84 / UTM zone 40N** around Muscat (zone 39N in the west, 40N central, 41N south-east) ⚠ unverified; ask municipality for survey DWG and keep the cadastral boundary untouched.
- File naming: `PlotNo_Wilayat_Floor_RevXX.dwg` ⚠ office convention.

---
## 3. Drafting conventions (dims, text, symbols, bilingual rules)
- Setbacks dimensioned to **each boundary**, with plot area on the drawing, because minimum setbacks depend on plot area band (§5.2) ✓ [S1].
- New buildings must **align with neighbouring buildings** (Art. 15, MoHUP 220/2023) ✓ [S1] — show neighbours' building lines on the site plan.
- Parking inside plot boundary shown with stall/aisle dims; parking shades outside plot need municipal permit ✓ [S3].
- Roof additions: drawn on rear/non-facade portion; area ratio table ✓ [S2].
- Arabic labels: غرفة نوم، مجلس، صالة، مطبخ، حمام، غرفة خادمة، سلم، سرداب (basement) ⚠ practice.
- Symbols per local practice; fire exit/extinguisher symbols per Civil Defence submission ⚠.
- Text: Arabic RTL aligned right in title block; Latin numerals ⚠.


### Local terms for labels
- Plot (قطعة أرض), plan/scheme (مخطط), wilayat (ولاية), governorate (محافظة), setback (ارتداد/ردود), building ratio (نسبة البناء).
- Majlis (مجلس), maid room (غرفة خادمة), car shade (مظلة سيارات), basement (سرداب), roof (سطح).
- Municipality (بلدية), Civil Defence (الدفاع المدني), Ministry of Housing and Urban Planning (وزارة الإسكان والتخطيط العمراني).

---
## 4. Governing codes & authorities (table)
| Topic | Instrument | Authority |
|---|---|---|
| Land planning controls (no structure plan) | **MoHUP Ministerial Decision 220/2023** "Regulation of land-planning controls" (اللائحة التنظيمية لضوابط تخطيط الأراضي) with Annex 2 for residential plots ✓ [S1] — applies to areas without structure plans ✓ | MoHUP |
| Muscat building use | **Local Order 23/92** (some outlets cite "92/23" and Royal Decree 101/2020 for the governorates system) ⚠ numbering conflict ✓ [S3] | Muscat Municipality |
| Permits (older decision) | Ministerial decision (2017) of Minister of Regional Municipalities & Water Resources: permit validity, floor heights ✓ [S2] | Municipalities |
| Building code | **Oman Building Code** (ICC-developed; ICC–MoHUP contract Feb 2024, six codes, base 2021/2024 I-Codes; National Building Requirements and Standards Guide launched Oct 2025 at Urban October) ✓ [S4]; phased implementation; reports of full enforcement by 2030 ⚠ weak | MoHUP |
| Fire | Civil Defence clearance required before licence (Muscat Municipality does not inspect systems) ✓ [S5, ~2012 report] ; Civil Defence/PACDA fire code editions ⚠ | PACDA (ex ROP Civil Defence) |
| Electrical | Utility rules + Wiring regulations ⚠ ; supply **240/415 V, 50 Hz** ⚠ | Nama group distribution companies, regulator APSR ⚠ |
| Coast | Ministerial Decision 20/1990 coastal setbacks: **300 m** high cliffs, **150 m** sandy beaches/coves, **50 m** low-impact beaches ✓ secondary [S2] | MECA/municipalities |
| Seismic | Oman Building Code structural part (ASCE 7 / IBC-based); Oman zones: moderate near Musandam/north ⚠ | MoHUP |

---
## 5. Key numbers (residential setbacks/coverage/height, stairs, egress, doors, ceiling heights, min rooms, parking, fire basics, electrical basics, seismic zone/structural basics)

### 5.1 Structure of rules (what the code actually controls)
Plot coverage, setbacks, floors, heights and parking differ by **zone (residential R1…R4, commercial, mixed), governorate and structure plan** ⚠. Only the following were verified.

### 5.2 MoHUP Decision 220/2023, Annex 2 — residential plots (areas without structure plans) ✓ [S1]
| Plot area (m²) | Front setback min | Side/rear setback min | Ground coverage / parking |
|---|---|---|---|
| < 300 | by site & neighbours (openings/ventilation/access rules) | same | coverage **100 %**; parking inside plot |
| 300–400 | **3 m** | **1.5 m** | ⚠ not legible in source |
| 401–599 | **3 m** | **2 m** | ⚠ |
| 600–899 | **4 m** | **2 m** | ⚠ |
| 900–1,200 | **6 m** | **2 m** | ⚠ |
| > 1,200 | per Ministry general site plan / complex controls | same | ⚠ |
Art. 16 (outside the annex): plots **1,500–2,500 m²** coverage cap **60 %**; parking inside plot required for plots **≥ 750 m²** ✓ [S1]. Art. 15: align with neighbouring buildings; openings/ventilation per other competent authorities (no numbers).
Source text partly garbled — confirm table with the official gazette ⚠.

### 5.3 Heights / floors / roof (2017 ministerial decision, secondary ✓ [S2])
| Item | Value |
|---|---|
| Ground floor internal height, residential-commercial plots | **4.0 m min – 4.8 m max** |
| Upper floors used as offices/homes (same plots) | **2.8 m min – 3.4 m max** |
| Roof-level additional facilities, buildings ≤ 3 storeys | **50 %** of roof space (can be increased to 80 %), not on main facade |
| Major permit validity | **2 years**, renewable; minor permit **1 year** |
| Parking shade outside plot (2018 decision, press) | ≥ **4.5 m** street to outside wall; **2 m** wall to shade ✓ secondary [S3] ⚠ may be amended |
Muscat-specific: single-expatriate/bachelor accommodation not allowed in residential/mixed areas; families and bachelors not mixed in one building (Local Order 23/92) ✓ press [S3].

### 5.4 Not verified — ⚠ all (do not invent)
Residential floors/height per zone, FAR, min room areas, stair width/riser, door width, ceiling height for villas (common practice 2.8–3.0 m ⚠), fire egress distances/widths, fire ratings, sprinkler thresholds, electrical sizing, seismic Ss/S1 and design category. Source them from the OBC volumes and Civil Defence requirements once issued to your project's governorate.

---
## 6. Permit drawing set
Planning/site certificate; survey plan; ownership; architectural drawings (site, floors, roof, 4 elevations, ≥ 2 sections, boundary wall/gate); area/ratio schedule; structural drawings + calc + soil investigation report; MEP (electrical load, water, drainage); Civil Defence approval; utilities no-objection (electricity, water); consultant/contractor registrations. After approval: major permit 2 years / minor 1 year ✓ [S2]; completion certificate on inspection ⚠.

---
## 7. Common rejection reasons
1. Setbacks below Annex 2 band (e.g., 600–899 m² needs 4 m front, 2 m side/rear) or ignoring neighbours' alignment.
2. Ground coverage above zone cap (60 % example) or wrong plot band.
3. Roof addition on main facade or > 50–80 % of roof space.
4. Mixed-use floor heights outside 4.0–4.8 m (ground) / 2.8–3.4 m (upper).
5. Parking not inside plot for plots ≥ 750 m²; parking shade < 4.5 m from street wall.
6. Missing Civil Defence clearance.
7. Coastal plot ignoring 50/150/300 m setbacks.
8. Bachelor/worker accommodation in a family residential zone (Muscat).
9. Permit lapsed (2-year major / 1-year minor).
10. Drawing not matching survey boundary/area.


### Pre-submission checklist (Oman — verified items only)
- [ ] Obtain planning certificate: confirm whether the plot is inside a structure plan (Decision 220/2023 applies only where none exists).
- [ ] Plot area band identified; setbacks per Annex 2 (300–400: 3 / 1.5 m; 401–599: 3 / 2 m; 600–899: 4 / 2 m; 900–1,200: 6 / 2 m).
- [ ] Neighbour building lines drawn; new building aligned (Art. 15).
- [ ] Parking inside plot for plots >= 750 m²; shade structures outside plot flagged for municipal permit.
- [ ] Mixed-use plots: ground floor 4.0–4.8 m, upper floors 2.8–3.4 m internal height.
- [ ] Roof additions <= 50 % (max 80 %) of roof, not on main facade, buildings <= 3 storeys.
- [ ] Coastal plots: 50 / 150 / 300 m setbacks checked.
- [ ] Civil Defence clearance obtained before municipal licence.
- [ ] Permit duration recorded: major 2 years, minor 1 year.
- [ ] OBC/phase-in status confirmed with the governorate before citing code clauses.

---
## 8. Sources
- [S1] MoHUP Ministerial Decision 220/2023 — https://qanoon.om/p/2023/mhup20230220/ ; news https://www.omandaily.om (search result: «الإسكان» تصدر اللائحة التنظيمية لضوابط تخطيط الأراضي)
- [S2] Oman Observer, "New regulations for building permits" (21 Jan 2017) — https://www.omanobserver.om/article/89507/LATEST NEWS/new-regulations-for-building-permits ; coast decision 20/1990 https://leap.unep.org/en/countries/om/national-legislation/ministerial-decision-no-20-1990-regarding-rules-regulating-and
- [S3] Muscat rules press — https://www.lexis.ae/2025/08/08/oman-tightens-enforcement-of-building-permit-requirements/ ; https://www.omanobserver.om/article/1120842/oman/new-regulation-issued-on-car-shades ; https://gulfnews.com/world/gulf/oman/muscat-officially-bans-families-and-bachelors-from-living-in-the-same-building-1.500707989
- [S4] ICC–MoHUP: https://www.iccsafe.org/about/periodicals-and-newsroom/international-code-council-collaborates-with-the-ministry-of-housing-and-urban-planning-in-oman-to-develop-a-new-set-of-building-codes-for-the-sultanate/ ; https://technicalreviewmiddleeast.com/construction/icc-advances-building-safety-at-urban-october-2025 (search results, not fetched ⚠)
- [S5] Fire safety mandatory in Oman — https://meconstructionnews.com/3020/fire-safety-mandatory-in-oman
