# Qatar — Drafting & Code Reference

Legend: **✓** = read this session from an official text (Almeezan Gazette PDFs of Ministerial Decision 108/2026 incl. Annex 7 & 8 pages read visually; Civil Defence Technical Requirements Guide 2022; Kahramaa Wiring Code PDF; QNMP R1 zone doc) — URL in §8. **⚠ verify** = secondary/news source, drafter practice, or not found in an official text; confirm before issuing. Source tags [S1]… are listed in §8.

**Regime in one line:** Villa/palace planning + architectural limits = **Ministerial Decision No. 7 of 1989 as amended by Decision No. 108 of 2026** (Minister of Municipality; Council of Ministers approved 15/4/2026; Gazette Issue 11 of 2026; in force 26 Jun 2026 per Ministry of Justice record) [S1][S2][S3]. Where older documents (QNMP R1 zone sheet, pre-2026 guides, news before June 2026) differ, **Decision 108/2026 wins** — see §5.0 for superseded values.

---
## 1. Units, scales, sheets

| Item | Qatar practice |
|---|---|
| Unit system | Metric (SI). Plan dimensions in **mm, no unit symbol**; levels, site dims, setbacks in **m (2 decimals)**; areas **m² (م²)** ⚠ practice (no mandate text found) |
| Levels | Qatar uses a municipal datum (**"Qatar National Height Datum / QNHD"**); levels shown `+0.00 = FFL`, road/plot level from approved survey; Ashghal (أشغال) approves entry levels [S3 §3-2] ⚠ datum name |
| Horizontal datum | **QND95 / Qatar National Grid, EPSG:2932** — Transverse Mercator, central meridian 51.21666667°E, lat origin 24.45°N, scale 0.99999, FE 200 000 m, FN 300 000 m ✓ [S12] |
| Language | **Arabic (primary, legally controlling) + English** bilingual drawings and title blocks. Arabic text right-to-left; English left-aligned in a parallel column ⚠ practice |
| Date format | dd/mm/yyyy; Gregorian (Hijri optional) ⚠ |
| North arrow | Required on every plan; site plan oriented with north up; plot frontage/street named; **QND95 coordinates/grid ticks** on site/location plan ⚠ practice |
| Dimension chain | Overall + wall-to-wall room dims + opening dims + setbacks from plot boundaries to each facade (each setback dimensioned) — the AI permit checker reads setbacks, heights, areas, room dimensions from the drawings [S9] |
| Area schedule | Required on plans: plot area, ground/first/roof/basement/mezzanine areas, coverage %, FAR, annex/majlis areas — checked vs 60 % / 1.65 / 70 % roof limits (§5.1) |

### Typical scales (practice ⚠ — the Ministry's Building Permit Guidebook [S8] lists required drawings; scale rules not confirmed)
| Drawing | Scale |
|---|---|
| Location/key plan | 1:1000 – 1:5000 |
| Site plan (setbacks, entrances, levels) | 1:200 (1:100 small plots) |
| Floor plans (basement, G, 1st, roof, mezzanine) | 1:100 (1:50 for detail/unit) |
| Elevations (4 sides) / sections (≥2, through stair) | 1:100 |
| Wall sections / details | 1:20 – 1:5 |
| Boundary wall + gate elevations | 1:50 |
| Structural GA / foundation | 1:100 / 1:50 |
| MEP layouts (power, lighting, AC, plumbing, drainage, FF/FA) | 1:100 (single-line diagrams NTS) |

### Sheet sizes
ISO A-series (A0 841x1189, A1 594x841, A3 297x420 landscape) — A1 or A0 typical for permit sets; A3 for booklet/calcs ⚠ practice.

### Title block fields (bilingual, right = Arabic)
Project name (اسم المشروع) · Owner (المالك) · Plot no. (رقم القسيمة) · Zone no./Street no. (رقم المنطقة / الشارع) · Municipality (البلدية: الدوحة، الريان، الوكرة، الوكير، الخور والذخيرة، أم صلال، الشمال، الضعاين، الشحانية) · Consultant name + **registered consultant licence no.** (الاستشاري / رقم الترخيص) · Drawing title (عنوان اللوحة) · Drawing no. · Revision/date (التعديل / التاريخ) · Scale (المقياس) · Drawn/Checked (رسم/ مراجعة) · Engineer stamp + signature (ختم وتوقيع المهندس) · Building permit no. (رقم رخصة البناء) · "Preliminary / For approval / Issued for construction" ⚠ fields are practice; Ministry e-system captures plot/owner/consultant data.

---
## 2. CAD layer & file naming standard

**Authority position:** No national mandatory layer standard was found in official texts read [S8]. The Ministry's AI permit system extracts buildings, setbacks, heights, areas and room dims directly from the consultant drawings and compares them with the plot GIS record (linked to Ashghal and Kahramaa geodata) [S9] — so **clean closed polylines per space, one area per polygon, setback dims drawn from true plot boundary** matter more than a specific layer scheme. Consultants in Qatar commonly use **AIA CAD Layer Guidelines (A-, S-, M-, E-, P-, FP-)** or **BS 1192 / ISO 13567** ⚠. ADM-type BIM naming uses ISO 19650 [S-AE]; Qatar projects with Ashghal/Qatar Rail also use ISO 19650 CDE naming ⚠.

### Submission requirements to honour (⚠ confirm in Building Permit Guidebook [S8], 403 pp, 5 chapters)
- **DWG** (AutoCAD 2018 format or lower ⚠) + signed **PDF**; drawn in **true QND95 coordinates**, model space at 1:1 in **metres or mm declared in title** ⚠.
- Plot boundary from official plot survey (Survey & GIS) — do not move/rotate; site plan must match GIS plot polygon (the system flags discrepancies) [S9].
- Each floor plan on own layout/sheet; areas on closed polylines; no overlapping duplicate polylines.

### Naming
`<ProjectNo>-<Disc>-<Type>-<Level>-<Rev>.dwg` e.g. `QA2611-A-PL-GF-R00.dwg` (A architectural, S structural, M mech/HVAC, E elec, P plumbing, FP fire) ⚠ practice. Sheet no. `A-101` plans, `A-201` elevations, `A-301` sections, `A-501` details; `S-1xx`, `M-1xx`, `E-1xx`, `P-1xx`, `FP-1xx` ⚠.

### Example layers (AIA-style; ACI colour / lineweight mm) ⚠ practice
| Layer | Content | ACI | LW |
|---|---|---|---|
| A-WALL | Walls cut (blockwork/RC) | 7 white | 0.50 |
| A-WALL-PRHT | Parapet / partitions (thin) | 8 | 0.25 |
| A-DOOR | Doors + swings | 3 green | 0.25 |
| A-GLAZ | Windows/glazing | 5 blue | 0.25 |
| A-FLOR-STRS | Stairs | 6 magenta | 0.25 |
| A-AREA | Area polylines (closed) | 2 yellow | 0.13 |
| A-ANNO-DIMS | Dimensions | 1 red | 0.18 |
| A-ANNO-TEXT / A-ANNO-TEXT-AR | English / Arabic text | 7 | 0.18 |
| A-ANNO-SETB | Setback dims + plot offset lines | 4 cyan | 0.18 |
| A-SITE-BNDY | Plot boundary (do not edit) | 1 red | 0.70 |
| A-SITE-FENC | Boundary wall/fence | 30 | 0.35 |
| A-ELEV-LINE | Elevation outlines | 7 | 0.50 |
| S-COLS | Columns | 7 | 0.50 |
| S-BEAM | Beams (dashed) | 2 | 0.35 |
| S-FNDN | Footings/pile caps | 6 | 0.50 |
| S-SLAB | Slab edges, drops | 4 | 0.25 |
| M-HVAC-DUCT / M-HVAC-EQPM | Duct / split units, FCUs | 5 | 0.25 |
| E-LITE / E-POWR / E-DIST | Lighting / sockets / DB + cabling | 2 / 3 / 1 | 0.18 |
| P-SANR-PIPE / P-DOMW-PIPE | Drainage / water supply | 3 / 5 | 0.25 |
| FP-SPRK / FP-ALRM | Sprinkler / detection, call points | 1 / 6 | 0.25 |
| Defpoints / XREF-* | non-plotting / xrefs | — | — |

---
## 3. Drafting conventions

| Topic | Convention (⚠ practice unless marked ✓) |
|---|---|
| Text height on paper | 2.5 mm notes; 3.5 mm headings; 5–7 mm titles. Arabic font ≥ same height + 10 % (Arabic glyphs read smaller); Arabic styles: `Arial`/`Simplified Arabic` |
| Bilingual rule | Every room label, title and note in **Arabic + English**; Arabic first/right. Do not mix directions in one string; use two lines |
| Room tags | `Room name AR / EN`, area m² (2 dp), finish level; majlis = المجلس, living = صالة المعيشة, driver room = غرفة السائق, maid room = غرفة الخادمة, store = مخزن, laundry = مغسلة, kitchen = مطبخ (تحضيري prep kitchen / داخلي internal kitchen) [S3 §1] |
| Level markers | Triangle + `+0.80` etc.; label FFL, plot level, road level, basement slab; show Ashghal-approved entrance level where required [S3 §3-2] |
| Grid | Column grid bubbles Ø 8–10 mm; numbers (1,2,3) one way, letters (A,B,C) other; Arabic numerals Latin (0-9) on drawings (not Eastern Arabic) |
| Section/elevation tags | Circle with sheet no.; elevations named North/South/East/West (شمالية/جنوبية/شرقية/غربية) |
| Setback annotation | Dimension from plot boundary to each facade at each floor; label which rule applies (ground 5 m / upper 3 m / side 3 or 1.5 m) so the checker can read it [S2 §6] |
| Hatch | Blockwork 200 mm: diagonal single; RC: ANSI31 + dots / solid for cut columns; insulation: zig-zag; earth: ANSI37; sand/screed: dots; tiles: grid — hatch scale so lines ≥ 1.5 mm apart on paper |
| Sunscreen / privacy elements | Sandblasted/obscure glazing ≥ 1.8 m high shown as such where windows sit in reduced setbacks [S2 §6] |
| Hidden services | Pipes, AC units, tanks must be concealed behind architectural elements (not visible on street facades; AC openings/drains not on main/street facades) [S3 §3-3] |
| Legend/abbreviations | Kahramaa electrical symbols follow BS EN 60617 per Wiring Code symbol page ✓ [S7 §2] |
| Notes | Single-line diagram must carry the note that installations comply with latest Electricity & Water installation regulations ✓ [S7 §1.1.1] |

---
## 4. Governing codes & authorities

| Discipline | Code / document | Current edition (as found) | Enforced by |
|---|---|---|---|
| Villa/palace planning (plot size, coverage, FAR, floors, height, setbacks, fences) | Ministerial Decision 7/1989 amended by **Decision 108/2026**, **Annex 7** (planning conditions for villas & palaces) ✓ | In force 26 Jun 2026 [S1] | Ministry of Municipality (وزارة البلدية) + municipalities; Coordination Committee (اللجنة التنسيقية) for exceptions |
| Architectural conditions | Decision 108/2026 **Annex 8** (architectural conditions & technical specs for villas/palaces) ✓; Annex 1 definitions; Annex 2 room dimensions/light/vent (⚠ not read); Annex 6 thermal insulation (⚠ not read) | 2026 | MoM |
| Zoning/master plan | **Qatar National Master Plan (QNMP)** zone regs R1–R6 (pre-2026 baseline; Annex 7 governs villas) ✓ | QNMP zone sheet [S5] | MoM Planning |
| Building law | Law No. 4 of 1985 on building regulation (and amendments) ✓ [S1 preamble] | — | MoM |
| Permit system | Building Permit System (BPS, e-permit) + **"Requirements & Services Guidebook for the Building Permits System in Qatar" (1st ed. 2022, 403 pp/5 ch.)**; **Building Requirements Guide, 3rd ed. (2,399 pp / 52 ch.)** ✓ [S8] | 2022 / 3rd ed. | MoM Building Permits Complex Dept.; AI-assisted review launched Oct 2025 [S9] |
| Construction specs | **QCS (Qatar Construction Specifications)** — 2014 ed. was mandatory 5th ed.; **QCS 2024** exists (unofficial copies only seen) ⚠ [S10] | QCS 2014 / 2024 ⚠ verify which the tender requires | MoM (with Ashghal, QS—Qatar Standards) |
| Fire & life safety | **Civil Defence Technical Requirements Guide** (GDCD, Ministry of Interior), 2022; supersedes FSG_2015; adopts NFPA as principal reference; **guide prevails over NFPA on conflict** ✓ [S6] | 2022 | General Directorate of Civil Defence (الإدارة العامة للدفاع المدني — QCDD), QCD-registered consultants only ⚠ |
| Electrical (LV) | **KAHRAMAA Low Voltage Electricity Wiring Code** (CS-CSI-P1/C1, Issue 0, 16-10-2016; web title "2018") ✓; Electricity Planning Regs for Supply Issue 4 (2026); AMI Code 2016 | 2016/2018; Planning Regs 2026 [S7] | KAHRAMAA (كهرماء) |
| Water | **Water Installation Code 2016**; District Cooling Design & Water Mgmt Code 2016 ✓ [S7 list] | 2016 | KAHRAMAA |
| Energy efficiency | **Tarsheed Code 2026** (دليل ترشيد لكفاءة استهلاك الطاقة والمياه في المباني) ✓ listed [S7 list]; Annex 6 thermal insulation required for villa permits ✓ [S1] | 2026 | KAHRAMAA / MoM |
| Roads/utilities/drainage | Ashghal (الأشغال العامة) Qatar Highway Design Manual, Infrastructure Design Manuals, entry-level & access approvals ✓ [S3 §3-2] | ⚠ edition | Ashghal — Roads/Drainage |
| Sustainability | **GSAS** (GORD): mandatory for government projects and all projects in Lusail; **JADARA** ties extra FAR to GSAS D&B stars (1-star track via MoM) ✓ [S11]; Annex 7 §7 gives star-linked bonus (§5.1) | — | GORD / MoM |
| Survey/grid | QND95 / Qatar National Grid EPSG:2932 ✓ [S12] | — | MoM Survey / Qatar GIS |
| Structural | QCS structural sections + referenced BS/EN/ACI; seismic/wind per QCS ⚠ not extracted | ⚠ | MoM (structural review) |

---
## 5. Key numbers

### 5.0 Superseded / conflicting values (do NOT use for new submissions)
| Old (QNMP R1, pre-2026) [S5] | Now (Annex 7, 2026) [S2] |
|---|---|
| Villa height 13 m incl. parapet (G+1+P) | **16 m incl. parapet** (B+G+1+Roof) |
| Penthouse = 70 % of ground footprint | **70 % of ground or first floor, whichever larger** |
| Main-building side/rear 3 m (1.5 m for non-habitable/no windows) at all floors | Same 3/1.5 rule **but roof level may go to 0 m** under conditions (§5.1) |
| Boundary wall 2.6 m street / 3.5 m palace | **2.7–3.4 m villa; ≤5 m palace** |
| Basement side/rear setback 1.5 m | **1 m all sides** |

### 5.1 Villa planning — Decision 108/2026 Annex 7 ✓ (page images read) [S2]
| Parameter | Value |
|---|---|
| Min plot, detached villa — **R1** (all municipalities except Al Wakra/Wakair, Al Khor/Dhakhira) | **600 m²** |
| Attached villas R1 | **950 m²** (475 m²/villa), frontage ≥ 20 m |
| Two detached villas on one plot R1 | ≥ 1100 m², frontage ≥ 20 m |
| Back-to-back attached pair | ≥ 950 m², frontage ≥ 16 m, plot on two streets, ≥ 3 m setback one side |
| **R2** detached / attached | **400 m²** / 600 m² (300 m²/villa) ; two detached ≥ 800 m², frontage ≥ 20 m |
| R1A (Al Khor) / R1B (Khor-Dhakhira-Wakra-Wakair) / R2A (Wakra, Wakair) | 1000 m² villa / 500 m² villa / 400 m² detached, attached 600 m² |
| Palace min plot | **3000 m²** |
| Typical (نموذجية) zones & grant land | 1 villa or 2 villas (detached/attached) per plot, any size, per zone's other limits |
| **Coverage (max)** — villa & palace (all buildings incl. annexes) | **60 %** |
| Roof floor (طابق السطح) area | **70 %** of ground or first floor area (larger) of main building |
| **FAR (max)** — all buildings incl. annexes | **1.65** |
| Sustainability bonus (applies to coverage % **and** FAR) | 1★ +10 % · 2★ +14 % · 3★ +18 % · 4★+ +20 % |
| Floors — villa/palace | **Basement + Ground + First + Roof**; plus **one mezzanine** (between G–1 or 1–Roof), counts in FAR |
| Floors — annex | B+G+1 ; Majlis: B+G+mezzanine |
| **Max height — villa** | **16 m incl. parapet** |
| Majlis within villa | 7.5 m (mezz 50 %) with front 0 / side 0 setback; or 10 m (mezz 80 %) with front 3 m / side 1.5 m; utilisation ≤ 60 % of side length |
| Majlis within palace | 8.5 m (mezz 50 %) / 12 m (mezz 80 %) |
| Palace height (no dome/ornament) | 3000–10000 m²: 17 m · 10000–20000: 18 m · >20000: 22 m |
| Palace height (with ornament) | 20 m · 22.5 m · 25 m |
| Annex in villa — G only | 5.5 m high; allowed along boundary: front 60 %, side neighbour 100 %, rear neighbour 100 %, side/rear street 80 % |
| Annex in villa — G+1 | 7.5 m; side neighbour ground 100 % / first 50 %; rear 100 %; street side/rear → Coordination Committee |
| Annex in palace | 3000–10000 m²: G 5.5 m / G+1 7.5 m · 10000–20000: G 6.5 m · >20000: G 7.5 m |
| Annex/majlis ↔ villa gap | ≥ **1.5 m**; may be shaded by concrete roof if open on 2 sides & unconditioned (not in coverage/FAR); no projections/windows toward neighbour or street |
| **Setbacks — villa ground floor** | **Front 5 m**; side & rear **3 m with windows / 1.5 m without** |
| Villa first floor & roof | **Front 3 m**; side/rear 3 m with windows / 1.5 m without |
| Ground-floor window in 1.5 m setback | Allowed if sill ≤ boundary wall height (i.e. not above wall); stair window fixed, non-see-through |
| Upper-floor windows in 1.5 m setback | Allowed if window sill ≥ **1.8 m**, otherwise fixed opaque glass up to 1.8 m (kitchen-prep, halls, living, baths) |
| **Roof floor setbacks** | Front: 3 m for ≥ 50 % of roof facade length, 0 m for rest; front windows allowed (with/without setback). Side/rear: if villa is 3 m from boundary → 0 m allowed on neighbour side (sandblasted glass ≥1.8 m); if villa is 1.5 m → keep 1.5 m; no-habitable-window or service rooms (kitchen, bath, store) → 0 m; side street ≥ 12 m wide → 0 m |
| Ground-floor extension to 0 m (two neighbour sides only) | ≤ 80 % of adjoining side length; height ≤ 5.5 m; mechanical ventilation allowed; counts in coverage/FAR [S3 §1-2-1] |
| Basement setback | **1 m** from all sides |
| Palace setbacks (G) | 3000–10000 m²: front 5 m, side/rear 3 m (1.5 m no windows) · 10000–20000: front 8 m, side/rear 5 m · >20000: 13 m all |
| FAR exemptions | Service basement (store, tanks, electrical, services) ≤ 30 % of FAR as exempt; underground parking; balconies; M&E spaces on ground ≤ 30 % or inside building; courtyards, shades, open unconditioned areas |
| Coverage exemptions | Sills/architectural projections; roads, entrances, paths, parking (unless garage ≥ 1 m above ground); unwalled courts/paved areas < 1 m above ground |
| Boundary wall | Villa **2.7–3.4 m**; palace ≤ **5 m**; typical-zones 63–68: uniform **2.70 m** design [S2 §8] |
| Car gate height | Villa **5 m**; palace 7 m (9 m allowed where setback 2 m) [S2 §9] |

### 5.2 Architectural — Annex 8 ✓ [S3]
| Item | Value |
|---|---|
| Basement uses | Habitable (halls, living, kitchen) + service (parking, store, tanks, electrical) allowed; basement roof ≤ **1.5 m** above approved (Ashghal) plot level |
| Ground floor level (FFL) above plot level | ≤ **1.5 m** if basement; ≤ **0.80 m** if no basement |
| Mezzanine | net height ≥ **2.4 m**; ≤ **35 %** of floor below; counts in FAR; uses: internal hall, kitchen, bedrooms, store, bath, laundry |
| Roof floor | same uses as ground; services (tanks, M&E) allowed within roof coverage; **no tanks / M&E / telecom equipment above roof floor** unless within permitted roof coverage |
| Upper-floor extension past villa line (annex/majlis top) | keep 3 m front, 1.5 m side/rear, windows sill ≥ 1 m, no roof-door onto annex roof |
| Windows (upper floors, openable) | lowest openable edge ≥ **1.0 m** above floor |
| Balcony toward neighbour | Allowed-setback depends on size; opaque screen **≥ 1.8 m** on neighbour/street/lane sides ⚠ minimum setback figures not legible in text layer |
| Building min width | **8 m**; walls longer than 8 m need a visible break in façade |
| Main façade | Faces main entrance side; all street façades must be of good architectural standard; coloured finishes need municipality approval |
| Architectural projections | ≤ **60 cm** horizontal, ≤ **1 m** vertical; none beyond plot boundary |
| Walls/fence | Whole plot must be enclosed; no internal fence between annex & villa; may lower yard level if neighbour safety ensured |
| Pedestrian gate (driver room door) | ≤ **1.0 m** wide; only if driver room shown; must open onto internal court |
| Plot frontage > 30 m | extra pedestrian gates only via Coordination Committee |
| Car entrance | width **4–7 m**; pedestrian entrance ≤ **1.5 m**; car entrance ≥ **5 m** and pedestrian entrance ≥ **3.5 m** from sight-line corner; gate ≥ **1 m** from neighbour boundary (≥ 6 m from neighbour entrance on corner-opposite plots where possible); no entrances toward alley (سكة)/neighbour/government land; Ashghal Roads approval on level & location |
| Letterbox | ≤ 30 cm projection; 2 m high, ≤ 1 m wide; must not hide services |
| Pool | non-slip surround; **1.2 m** barrier; rescue ropes; depth sign; electrics per Kahramaa standards |
| Servant/driver room (example from design basis) | Fixed driver room needs inward-court opening; sizes per Annex 2 ⚠ (not read) [local design memo] |
| Service stair | Allowed for maids/maintenance, reaching all floors |

### 5.3 Min rooms, ceilings, stairs, guards (Qatar official values not located in texts read)
| Item | Value |
|---|---|
| Habitable room min area/dim | **⚠ verify — Annex 2 of Decision 108/2026 (room dimensions, light, ventilation, light-wells)** |
| Ceiling height habitable | ⚠ verify (Annex 2); basement net height **2.8 m habitable / 2.4 m non-habitable** per QNMP R1 baseline ✓ [S5] — check Annex 8 supersession |
| Stairs (rise/going/width) & guard height | ⚠ verify — apartment egress per Civil Defence guide uses NFPA 101 §7.2.2 ✓ [S6]; villa stair rules in Annex 2 / QCS |
| Doors (escape path in dwelling units) | ≥ **710 mm** wide; bathrooms & rooms ≤ 6.5 m² ≥ **610 mm**; door nominal height ≥ **1980 mm** ✓ [S6 apartments] |
| Hallways in dwelling unit | width ≥ **915 mm**; clear height ≥ 2135 mm (2030 mm under projections) ✓ [S6] |
| Escape window (sleeping) | clear opening ≥ **0.53 m²**, width ≥ 510 mm, height ≥ 610 mm, sill ≤ **1120 mm** ✓ [S6] |

### 5.4 Egress & fire (Civil Defence guide 2022 — apartment chapter used as proxy; villas follow NFPA 101 one/two-family ⚠) ✓ [S6]
| Item | Value |
|---|---|
| Apartment height classes | Low-rise < 15 m habitable height; mid 15–<28 m; high ≥ 28 m |
| Dwelling > **185 m²** | two remote exit-access doors |
| Corridor serving > 50 persons | ≥ **1200 mm** clear |
| Travel inside unit to corridor door | ≤ **23 m** (≤ **38 m** if sprinklered) ⚠ parsed from table layout |
| Unit door → nearest exit | ≤ **30 m** unsprinklered / **61 m** sprinklered ⚠ |
| Other areas → exit | ≤ **61 m** / **76 m** sprinklered ⚠ |
| Common path | ≤ **11 m** (15 m protected ⚠); dead-end corridor ≤ **11 m** (15 m protected ⚠) |
| Single-exit apartment buildings | floor net area ≤ 500 m²; common path ≤ 11 m; stair enclosed 2 h if connecting ≥ 4 storeys |
| Exit stair enclosure | 1 h (sprinklered), 2 h connecting ≥ 4 stories; doors 1 h (1.5 h where 2 h wall) |
| Stair smoke control | vent at top for < 9 m; vents/pressurisation per height 9–15 m / > 15 m |
| Occupant load factor apartments | 18.6 m²/person |
| Basement stair single | serves one basement ≤ 500 m², depth ≤ 6 m |
| Fire drawings | Only **QCD-registered consultants** prepare fire safety drawings ⚠ [S6 search]; FF/FA drawings per NFPA 13/14/72 etc. |

### 5.5 Parking, plot
| Item | Value |
|---|---|
| Villa parking count | "per Car Parking Regulations / Ministry guidelines" — numeric ratio **⚠ verify** [S5] |
| Plot private open space (QNMP R1 baseline) | 15 % of site (≥ 25 m² ground/roof, min 5 m dim) ⚠ confirm still applicable |
| Compound villa (QNMP R1): min 3000 m², coverage 40 %, 5 m/3 m/3 m setbacks | ⚠ Annex 7 text not read for compounds |

### 5.6 Electrical — KAHRAMAA Wiring Code ✓ [S7]
| Item | Value |
|---|---|
| Declared supply | **240/415 V ±6 %, 3-phase 4-wire, solidly earthed neutral; fault level 31 MVA @ 415 V; 50 Hz** (±0.1 Hz normal; load shedding at 48.8 Hz) |
| Lighting final circuit | ≤ **1800 W per circuit** (1.5 mm²: 600/1200 W steps; 2.5 mm²: 1800 W); switch sizes 5/10/15 A; remote/outdoor lighting by timer + photocell via SWA cable |
| Kitchen sockets (dwelling) | ≥ **4 × 13 A** (8 if kitchen > 12 m²); own ring: 4 mm² L/N + 2.5 mm² CPC on **30 A MCB**; no other rooms on kitchen ring |
| Cooker | 45 A control unit on its own circuit, 6 mm² PVC + 6 mm² earth; connector unit at low level |
| Water heater | 20 A DP switch |
| Max demand / diversity | Section 12 of Wiring Code ⚠ values not extracted |
| Symbols | BS EN 60617 |
| Meter rooms | KAHRAMAA metering in separate lockable cabinet; CT metering (Class 1/0.5) on main switchboards where load dictates |
| Interface | Tarsheed Code 2026 for lighting/efficiency; Wiring Code **Appendix 03 lists applicable standards** (BS 7671, IEC) |

### 5.7 Plumbing, HVAC, structure
| Item | Value |
|---|---|
| Water | Kahramaa Water Installation Code 2016 — pipe/tank/meter rules ⚠ not extracted |
| HVAC / thermal | **Annex 6 insulation** is a permit condition ✓ [S1]; U-values/sizing per **Tarsheed 2026** ⚠ not extracted; district cooling code 2016 where Qatar Cool serves |
| Structural loads | QCS structural sections / ASCE 7 or BS EN 1991 as referenced — **⚠ verify design wind speed/seismic zone from QCS** |
| Climate for design | Kahramaa Wiring Code gives site conditions (RH 30–97 % at 27–44 °C, annual rain ~50 mm) ✓ [S7 §1.3] — design ambient temp **⚠ verify** |

---
## 6. Permit / approval drawing set (Building Permit System, e-permit via registered consultant)
Per the Guidebook [S8] the authority lists required docs "by building type" (403 pp). Typical villa set ⚠ — confirm in Guidebook:

| # | Sheet | Must show |
|---|---|---|
| 1 | Cover / index + area schedule | Plot, zone (R1/R2…), coverage %, FAR, floor areas, bonus stars claimed |
| 2 | Location & site plan | QND95 grid, plot polygon from survey, setbacks per floor, entrances (car ≤ 7 m / ped ≤ 1.5 m), levels, boundary wall, annex/majlis, driver-room gate, pool |
| 3 | Basement + GF + FF + roof + mezzanine plans | Room names AR/EN, areas, window locations vs setbacks, stairs, mezz ≤ 35 % |
| 4 | Elevations (4) | Height ≤ 16 m incl. parapet; wall ≤ 3.4 m; gate ≤ 5 m; AC/pipes concealed |
| 5 | Sections (≥2) | Floor-to-floor, ceiling, FFL ≤ 0.8/1.5 m above plot, basement ≤ 1.5 m above plot |
| 6 | Structural (foundations, columns, slabs, details) | Stamped by registered engineer |
| 7 | Electrical (single-line + layouts) | Kahramaa note per Wiring Code §1.1.1; load schedule |
| 8 | Plumbing/drainage/water + AC | Kahramaa water code; sewage to Ashghal network |
| 9 | Fire (if required) | QCD-registered consultant only |
| 10 | Thermal insulation compliance (Annex 6) & GSAS/JADARA docs if bonus | Required for permit ✓ [S1] |
| NOCs | Ashghal (roads/drainage), Kahramaa (electric/water), QCD, Ooredoo/Vodafone, Qatar Cool where applicable ⚠ |
The system validates in 3 steps (structure; consistency of drawings vs consultant input & GIS; violations) and returns a To-Do list; ≈70 % automated, ~120-minute issuance claimed [S9].

---
## 7. Common rejection reasons / mistakes
1. **Using QNMP R1 numbers** (13 m height, 2.6 m wall, 1.5 m basement setback) instead of Decision 108/2026 — see §5.0.
2. Setbacks not dimensioned per floor (ground 5 m front vs 3 m upper) so checker cannot confirm.
3. Window in 1.5 m setback with sill below 1.8 m / clear glass — must be obscure.
4. Coverage computed on footprint only: annexes, majlis, garages ≥ 1 m above ground count; roof floor must be ≤ 70 % of larger of G/1st.
5. FAR omitting mezzanine (counts) or basement habitable area (only service basement ≤ 30 % exempt).
6. Mezzanine > 35 % of floor below or net height < 2.4 m.
7. Roof tanks/equipment above roof floor; AC outlets/pipes visible on street façade.
8. Gate geometry: car entrance < 4 m or > 7 m; pedestrian > 1.5 m; no sight-triangle clearance; entrance onto alley.
9. Driver-room door on boundary not matched by a drawn driver room opening onto an internal court.
10. Plot polygon edited/shifted vs GIS — discrepancy flag.
11. Fire drawings by non-registered consultant; single-line diagram missing Kahramaa compliance note.
12. Ignoring Annex 6 thermal compliance (permit condition).

---
## 8. Sources
- [S1] Decision 108/2026 text (Almeezan): https://almeezan.qa/legislations/ministerial-decision/2026/108/municipality-minister ; local copies `D:\ai agents leaders all projects\qatar-architecture\research\` (details JSON, Akoma XML, design-basis memo 22-10-2026)
- [S2] Annex 7 planning conditions: https://files.almeezan.gov.qa/almeezan/8a1626f6-f6af-5fa7-a8f5-20ed14bec5f5.pdf
- [S3] Annex 8 architectural conditions: https://files.almeezan.gov.qa/almeezan/98099fe9-0e80-5dfb-9fc0-508c9817b255.pdf
- Annex 1 definitions: https://files.almeezan.gov.qa/almeezan/5b6b03f7-1441-5f04-876b-7b0fbb0c74b0.pdf ; Gazette copy: https://files.almeezan.gov.qa/almeezan/65d8a303-b758-57db-9ae3-d2bbce351521.pdf
- [S5] QNMP R1 zone regs: https://khazna.gisqatar.org.qa/portal/sharing/rest/content/items/ebfe7fff86034c7fabd2cbc9209610d7/data
- [S6] Civil Defence Technical Requirements Guide (2022): https://portal.moi.gov.qa/wps/wcm/connect/018e8b0f-4351-47d5-b2ff-f8ec090d2ddf/guide_english.pdf
- [S7] KAHRAMAA Wiring Code: https://km.qa/CustomerService/ServiceRegulations/ELECTRICTY%20WIRING%20CODE%202018.pdf ; regulations list: https://km.qa/CustomerService/Pages/ServicesRegulations.aspx
- [S8] Building Permits Guidebook (QNA 7 Aug 2022): https://www.qna.org.qa/en/News-Area/News/2022-08/07/0037-ministry-of-municipality-issues-requirements-and-services-guidebook-for-building-permits-system
- [S9] AI permit system (Peninsula, 26 Oct 2025): https://thepeninsulaqatar.com/article/26/10/2025/qatar-launches-ai-powered-building-permit-system
- [S10] QCS history: https://www.gulf-times.com/story/494340/New-construction-specifications-could-set-global-standards
- [S11] GSAS/GORD: https://www.gulf-times.com/article/689153/qatar/over-2400-projects-in-qatar-are-gsas-certified-gord-chairman ; JADARA https://jadara.gord.qa/wp-content/uploads/2025/10/jadara-program-brochure.pdf
- [S12] QND95 EPSG:2932: https://epsg.io/2932
- News on 2026 amendment (cross-check only): https://www.gulf-times.com/article/727204/qatar/updated-villa-and-mansion-requirements-offer-more-flexible-solutions-top-official ; https://www.gulf-times.com/article/727008/qatar/minister-of-municipality-issues-decision-updating-residential-villa-and-palace-regulations-in-response-to-qatari-families-needs-modern-construction-requirements
- [S-AE] ADM/ISO 19650 BIM note: https://globalbim.org/info-collection/abu-dhabi-municipality-adm-guidelines/

### Open items summary
⚠ Annex 2 (room sizes/ceiling/light/vent) and Annex 6 (insulation) not read; QCS edition; Qatar car-parking ratios; stair/guard dims; structural loads; CAD file-format rules; QNHD datum name; fire travel-distance table parsing; Ashghal manual edition; NOC list.
