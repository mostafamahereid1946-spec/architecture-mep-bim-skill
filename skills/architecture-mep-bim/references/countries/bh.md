# Bahrain — Drafting & Code Reference

Legend: **✓** = read this session from the official English translation of Prime Minister's Decision No. 93 of 2023 (Legislation & Legal Opinion Commission docx, "published on the website Sep 2024") [S1]. **⚠ verify** = not confirmed. Zoning parameters change per zone code — first get the plot's zone code and map from Benyat/Planning & Development Authority.

**Regime in one line:** Building Regulation Law (Decree-Law 13/1977) + **Decision 93/2023 "Regulatory Requirements for Urbanization in various areas"** (Arabic: الاشتراطات التنظيمية للتعمير بمختلف المناطق) — in force the day after Gazette publication (Art. 5); replaced Decision 56/2022; applications under 2009/2022 rules accepted only if filed before **1 Dec 2023** (Art. 4) ✓ [S1]. Decision cites Decree-Laws 13/1977, 2/1994 (urban planning), 3/1994 (land division, exec. regulation Dec. 56/2009), 1/1996 (electricity & water) ✓. Issuing ministry: Ministry of Housing and Urban Planning (MOHUP); permits via **Benayat** portal, Ministry of Works / Municipalities Affairs [S2].

---
## 1. Units, scales, sheets, title block, language

| Item | Practice |
|---|---|
| Units | Metric. Dimensions in **mm or m** (office-specific); levels `+0.00` in m; areas m² |
| Datum | Site levels referenced to approved topographic survey / road (sidewalk) level — rules measure from **sidewalk level** (e.g. ground floor ≤ 1.50 m above sidewalk, Art. 5/12 ✓) |
| Language | **Bilingual Arabic + English** drawings common; Arabic governs official forms ⚠ practice |
| Scales | Site plan 1:200–1:500, floor plans/elevations/sections 1:100, details 1:20–1:5, sections thru stairs/majlis 1:50 ⚠ practice (Unified Guidebook not read) |
| Sheets | ISO A1/A0 plots, A3 booklets ⚠ |
| Title block | Project, owner (المالك), plot/block/road/area numbers (قطعة/ مجمع/ طريق), consultant licence (Bahrain Society of Engineers), drawing no., revision. Facades Committee approval stamp where needed ⚠ |
| Area schedule | Plot area, ground/typical floor area (check ≤ 60–70 % of plot), total built area vs building ratio % (Art. 3/10/17/23/30 ✓), basement, roof facilities, majlis, services |
| North / orientation | North arrow + road widths (important: 20 m road-reserve threshold drives setbacks) |

---
## 2. CAD layer/file naming practice (what local consultants use) + any authority CAD submission rules (DWG version, coordinate system)
- No official layer standard found. Local consultants typically use AIA/CAD-Layer-Guideline-style or in-house names: `A-WALL`, `A-DOOR`, `A-GLAZ`, `A-FLOR-STRS`, `A-ANNO-DIMS`, `A-ANNO-TEXT`, `S-COLS`, `E-LITE`, `M-HVAC`, `P-SANR` ⚠ practice, no source.
- Benayat is an online submission system for licensed engineering offices (apply, track permit, view zoning restrictions) ✓ [S2]. Required file formats (DWG vs PDF) and DWG version **not verified** ⚠ — export DWG 2013 + signed PDF, check Benayat checklist.
- Coordinate system: Bahrain uses its own state grid (Bahrain State Grid on Ain el Abd/WGS84 variants) ⚠ EPSG not verified; survey drawings come georeferenced from the Survey and Land Registration Bureau (SLRB) ⚠.

---
## 3. Drafting conventions (dims, text, symbols, bilingual rules)
- **Setbacks drawn as dimensions** from plot boundary to ground-floor wall and to upper-floor projections (1.20 m cantilever limit) — check Facades Committee wall rule (external wall height ≤ ground-floor height unless approved, Art. 5 ✓).
- Show **sidewalk level** datum, ground-floor level relative to sidewalk, basement ramp location/slope, entrance + parking (2 spaces/unit inside plot, Art. 7 ✓).
- Hatch/annotate areas excluded from building ratio: basement, facilities (housing facilities, majlis within % caps), lifts in setbacks (no side windows overlooking neighbours, Art. 8 ✓).
- Lines/text: monochrome plot, text ≥ 2.5 mm; Arabic RTL mirrored title block ⚠.
- Symbols: lift pit, fire escape arrows, civil-defence symbols per Civil Defence submission ⚠.
- Bilingual notes: dimensions & levels are language-neutral; room names Arabic/English (مجلس Majlis, غرفة نوم, مطبخ, دورة مياه, ملحق خادم) ⚠.


### Local terms for labels
- Plot (قسيمة/قطعة), road reserve (حرم الطريق), setback (ارتداد), building ratio (نسبة البناء), building surface (مساحة البناء للدور).
- Housing facilities (ملحقات سكنية), external majlis (مجلس خارجي), mezzanine/tiered floor (دور مسيّر), basement (سرداب/قبو).
- Facades Committee (لجنة الواجهات), service entities (الجهات الخدمية), Benayat (بنايات).

---
## 4. Governing codes & authorities (table)

| Topic | Instrument / authority | Note |
|---|---|---|
| Building permit | **Benayat** portal; Ministry of Works, Municipalities Affairs and Urban Planning; Unified Guidebook of Building Permit Regulations [S2] ✓ | Guidebook not retrieved ⚠ |
| Zoning/ratios/setbacks/heights | **PM Decision 93/2023** [S1] ✓; maps by MOHUP minister decisions (Art. 2 ✓), e.g. Decisions 849 & 852 of 2026 apply it with zone codes RHB, IST [S3] ✓ | |
| Building law | Decree-Law 13/1977 (Building Regulation Law) + executive regulation ✓ (cited, text not read) | Light-shaft ("maneuvers") rules referenced in Art. 31 ✓ |
| Land division | Decree-Law 3/1994; Decision 56/2009 | Plot division checks, Art. 8/15 ✓ |
| Structural | Bahrain has no standalone seismic code found; practice follows BS/Eurocode/ACI, + Ministry requirements ⚠ | verify with MOW |
| Fire | General Directorate of Civil Defence (Ministry of Interior) approves fire design ⚠; Bahrain Fire Code Part ⚠ | not retrieved |
| Electricity/water | **EWA** (Electricity & Water Authority) under Decree-Law 1/1996 ✓ (cited) ; EWA wiring regulations ⚠ | |
| Facades | Facades Committee (لجنة الواجهات) ✓ (Art. 5) | approval to raise boundary wall |
| Utilities clearance | "Service entities" approval for basements/ramps ✓ (Art. 3) | |

---
## 5. Key numbers (residential setbacks/coverage/height, stairs, egress, doors, ceiling heights, min rooms, parking, fire basics, electrical basics, seismic zone/structural basics)

### 5.1 Residential zones — summary
| Zone (code) | Building ratio (FAR) | Max per-floor footprint | Floors / height | Front setback | Side / rear (ground) | Articles |
|---|---|---|---|---|---|---|
| Private Residential A (RA) villas only | **180 %** | **60 %** | 3 floors, **15 m** (16.50 m with basement) | **3 m** if road reserve < 20 m; **2 m** if ≥ 20 m | **2 m / 2 m** | 1–8 |
| Private Residential B (RB) villas + apartments | 180 % | 60 % | 3 fl / 15 m (16.50 m) | 3 m / 2 m (parking roof to front line with upper floors set back 1.80 m) | 2 m / 2 m | 9–15 |
| Private Residential Apartments (PAP) | 180 % | 60 % | 3 fl / 15 m (16.50 m) | 3 m / 2 m | 2 m / 2 m | 16–21 |
| Residential Villas (RV) villas only | **120 %** | 60 % | **2 floors, 12 m** (13.50 m with basement) | **5 m** if reserve < 20 m; **3 m** if ≥ 20 m | **2 m / 2 m** | 22–28 |
| Connected Housing A (RHA) villas | **210 %** | **70 %** | 3 fl / 15 m (16.50 m) | 3 m / 2 m | build on both side boundaries; rear 2 m | 29–32 |
| Connected/attached B (RHB) | not read ⚠ | ⚠ | ⚠ | ⚠ | ⚠ | 33+ (heading seen only) |

Common rules: upper-floor projections max **1.20 m** beyond ground floor on front; side projection 1 m only on secondary street; none otherwise. Basement (one level) may sit on boundary; not counted in ratio; ground floor ≤ **1.50 m** above sidewalk; 100 % of basement may be residential in villas (no street-direct access if residential). Corner plots: front setback from the entrance side street.

### 5.2 Extras not counted in ratio / extras counted
- Housing facilities (maids/driver) extra **15 %** of plot (RA, RV), ≤ **4 m** high, on rear/one side, depth ≤ 50 % of the other side; RB/PAP: extra **20 %**, ≤ 4 m (Art. 3(3), 10, 17, 23 ✓).
- Roof facilities at rear after mid-roof line: ≤ **30 %** of built roof area (30 m² if roof < 100 m²), ≤ 4 m (RB Art. 10 ✓).
- Outdoor majlis: ≤ **15 %** of plot, counted in ratio (RA Art. 3 ✓); facade length of majlis + parking entrances ≤ **50 %** of frontage; ≤ one floor, ≤ 4 m.
- Mezzanine in villa interiors ≤ **50 %** of floor area, counted in ratio (Art. 8, 15, 21, 28 ✓).
- Guard room/WC at front on plots **> 1000 m²** (Art. 8 ✓).
- Small plots (RA, Art. 8 ✓): < 300 m² or 12–15 m frontage → build on one side boundary; frontage < 12 m or < 200 m² → both sides, rear setback 1.50 m, front 3/2 m by road width.

### 5.3 Multiple units
Compound (RAC/RBC/RVC) needs planning approval + reclassification; RA/RB: plot ≥ **600 m²**, min side **32 m**, ≥ 300 m² per unit, internal passage ≥ **8 m**, parking 2 + **1.5 visitor**/unit if road < 20 m (Art. 6, 14 ✓); RV compound: ≥ 1000 m², ≥ 600 m² per unit, setbacks 3 m front / 4 m side & rear (Art. 27 ✓). Apartment size ≥ **100 m²** (RB, PAP: Art. 15, 21 ✓).

### 5.4 Parking
Villa/unit **2 spaces** on plot (Art. 7, 26 ✓); apartments 2 each; commercial/services **2 per 100 m²** (Art. 13, 20 ✓); not in ratio. Space dimensions / ramp slopes ⚠ not read.

### 5.5 Not found — do not invent (⚠ all)
Min ceiling height, stair width/riser, door widths, min room areas, fire egress distances, shaft sizes: governed by Building Regulation Law exec. regulation, Civil Defence requirements, Unified Guidebook — ⚠ not retrieved. Typical practice guess (not rules): ceiling 2.7–3.0 m ⚠. Electrical: 230/400 V 50 Hz ⚠. Seismic: low zone ⚠.

---
## 6. Permit drawing set
Via Benayat by licensed office ✓ [S2]: zoning/site check → architectural drawings (site, floors incl. basement & roof, elevations, sections, boundary wall/gate), area schedule vs Decision 93 caps, structural (calcs + soil report), MEP, Civil Defence + EWA/service-entity approvals ✓ (service entities required for basements/ramps), Facades Committee for wall height ⚠. Exact checklist from Unified Guidebook ⚠.

---
## 7. Common rejection reasons
1. Wrong zone (RA vs RV vs RHA) → using 180 % where 120 % (2 floors/12 m) applies.
2. Front setback uses 2 m with road reserve < 20 m (needs 3 m; RV needs 5 m).
3. Ground floor > 1.50 m above sidewalk with basement; height 15 m / 16.50 m exceeded.
4. Per-floor footprint > 60 % (RHA 70 %).
5. Upper projection > 1.20 m, or projections on side/rear where prohibited.
6. Parking < 2/unit or counted in ratio; visitor spaces missing in compounds.
7. Housing facilities > 15–20 % / > 4 m; majlis frontage > 50 %.
8. Basement with direct street access while residential; no service-entity approval for ramp.
9. Boundary wall higher than ground floor without Facades Committee approval.
10. Plot division below Decree-Law 3/1994 limits.


### Pre-submission checklist (Bahrain — Decision 93/2023)
- [ ] Zone code confirmed on Benayat (RA / RB / PAP / RV / RHA / RHB ...); applicable article range noted.
- [ ] Building ratio vs cap: 180 % (RA, RB, PAP), 120 % (RV), 210 % (RHA).
- [ ] Per-floor footprint <= 60 % (RHA 70 %).
- [ ] Floors / height: 3 / 15 m (RV 2 / 12 m); with basement 16.50 m (RV 13.50 m).
- [ ] Road reserve width recorded to pick front setback (3 m vs 2 m; RV 5 m vs 3 m).
- [ ] Side/rear 2 m on ground floor; upper-floor projection <= 1.20 m front only.
- [ ] Ground floor level <= 1.50 m above sidewalk when basement provided.
- [ ] Two parking spaces per unit inside plot, outside the ratio.
- [ ] Facilities (maid/driver) <= 15 % / 20 % and <= 4 m; majlis frontage <= 50 %.
- [ ] Services approval attached for basement/ramp; Facades Committee for wall height.

---
## 8. Sources
- [S1] Decision No. 93 of 2023 (English) — https://lloc.gov.bh/FullEn/RCAB9323.docx ; Arabic https://legalaffairs.gov.bh/Legislation/HTM/RCAB9323 ; PDF https://planning.bh/pdf/Rules%20and%20Regulations/Zoning%20and%20Construction%20Regulations/%D9%82%D8%B1%D8%A7%D8%B1%2093%20%D9%84%D8%B3%D9%86%D8%A9%202023.pdf
- [S2] ICC Bahrain note (Benayat, Unified Guidebook) — https://www.iccsafe.org/?p=241108 ; Benayat requirements https://benayat.app.gov.bh/RegulatoryRequirementsForConstructionAr.pdf (image-based, unread ⚠)
- [S3] MOHUP Decisions 849/852 of 2026 — https://lloc.gov.bh/Legislation/HTM/RHUP84926 , https://lloc.gov.bh/Legislation/HTM/RHUP85226
- [S4] PMO press note — https://www.pmo.gov.bh/en/article/hrh-the-crown-prince-and-prime-minister-issues-edict-93-of-2023
