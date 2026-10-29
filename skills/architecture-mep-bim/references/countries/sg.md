# Singapore — Drafting & Code Reference

Legend: **✓** = read this session on an official agency page (SCDF, URA/BCA circular) — URL in §8. **⚠ verify** = from memory/secondary or page not readable (BCA's PDFs blocked/404 for the fetch tool this session). Singapore regulation is split by agency: **URA** (planning/use/GFA/height), **BCA** (structure, accessibility, building control, CORENET), **SCDF** (fire), plus NEA, PUB, LTA, NParks, EMA.

**Rule of thumb:** private landed housing (terrace/semi-D/bungalow, GCB) is governed by URA **Handbook on Development Control + Landed Housing Guidelines** by area type — never invent setbacks; check URA's *Master Plan 2019* zoning and the *Landed Housing Area* type for the plot ⚠.

---
## 1. Units, scales, sheets, title block, language

| Item | Practice |
|---|---|
| Units | Metric; plans in **mm**, site/levels in **m**; Singapore Height Datum (SHD, ~mean sea level) for RLs ⚠ |
| Coordinate system | SVY21 (EPSG:3414) ⚠ |
| Language | English only |
| Sheets | ISO A0–A3; A1 (594×841) and A3 booklets typical ⚠ |
| Scales | Site 1:200–1:500; plans/elevations/sections 1:100 (1:50); details 1:20–1:5 ⚠ |
| Title block | Project title/address (lot no., mukim/TS), QP name + PE/RA registration no., drawing no./rev, scale, date ✓ practice; QP = **Qualified Person** ⚠ |
| Area terms | **GFA** per URA definition (exclusions e.g. void, balcony, planter, ancillary areas ⚠ — Circular), **plot ratio** = GFA/site area ✓ concept |
| North | North point + SVY21 grid ⚠ |

## 2. CAD layer/file naming practice + authority CAD/e-submission rules

| Topic | Practice / rule |
|---|---|
| Submission platform | **CORENET X** (replaces CORENET 2 / e-Submission); issuing agencies BCA + URA; development control agencies include LTA, NEA, NParks, PUB, SCDF ✓ [URA dc26-08] |
| Timeline ✓ | mandatory for new projects **GFA ≥ 30,000 m² from 1 Oct 2025**; **GFA ≥ 5,000 m² from 1 Oct 2026**; ongoing ≥ 5,000 m² projects may continue on CORENET 2 until further notice; < 5,000 m² voluntary for now (circular dated 23 Jul 2026) |
| Process names ✓ | "Three-Gateway Process" and "Direct Submission Process" (gateway names Design/Piling/Construction/Completion ⚠ not stated in that circular) |
| Formats ⚠ | **IFC-SG** BIM for mandatory GFA ≥ 5,000 m² (URA Development Application page says < 5,000 m² may use 2D or lightweight BIM); smaller landed jobs still 2D PDF + DWG ⚠ verify |
| Code of Practice | **CORENET X Code of Practice (COP)**, latest Edition 3.1 (Dec 2025) — sets each gateway's requirements ✓ per circular citation |
| Layer naming | No mandatory scheme for 2D; follow **BIM-CAD standards / BCA "Guide to CAD layering"** or AIA/ISO 13567 (`A-WALL`, `A-DOOR`) ⚠ |
| File naming | `[ProjectCode]-[Discipline]-[Level]-[Seq]` ⚠ practice |
| Authority CAD rule | DWG not accepted as the submission record (PDF + IFC); BIM models must comply with COP IFC-SG schema ⚠ |

## 3. Drafting conventions

- **Dimensions** in mm; levels in m to 3 decimals (e.g. `+10.000 SHD`) ⚠.
- **Required symbols**: north point, section marks, door/window tags (`D1`, `W1`), room labels with use (BEDROOM, KITCHEN, YARD), fire-rated door ratings (e.g. "FRD 1/2 HR").
- **Fire notes**: exit travel arrows, FSC/fire compartment lines, dry riser inlet/hose reel positions, refuge areas ✓ practice; SCDF drawings are separate sheets (Fire Safety Plan).
- **Gross floor area plan** with coloured GFA vs non-GFA zones ✓ URA practice; calculation table.
- **Accessibility**: PWD (persons with disability) paths, accessible toilet, lift, ramp gradients shown per BCA Code on Accessibility ⚠.
- **Hatching** per BCA/ISO; roof drainage falls; slab thicknesses noted.
- **Housing-specific**: Rail setbacks/Buffer, "Hawker/ electrical sub-station" clearance ⚠.

## 4. Governing codes & authorities

| Item | Code / authority | Status |
|---|---|---|
| Building Control Act 1989 & Regs | **BCA**; QP appointed; permit stages (Plan approval → TOP → CSC) | ⚠ |
| BCA Approved Document | Acceptable Solutions for Building Control Regulations (structural eurocodes, safety, accessibility) | ⚠ not opened |
| Accessibility | **Code on Accessibility in the Built Environment 2019** (BCA); under review (public consultation planned end 2024 per press) | ⚠ |
| Planning | **URA** — Master Plan 2019, Development Control Handbook, Circulars, GFA definitions | ⚠/✓ |
| Fire | **SCDF Fire Code 2023** (Chapters 1–9 with commentary; amendments 1st & 2nd batches; Table 2.2A relaxed 1 Sep 2024) | ✓ |
| Electrical | **SS 638:2018** Code of practice for electrical installations; EMA licence/ Licensed Electrical Worker (LEW) | ⚠ |
| Ventilation | SS 553 Air-conditioning and mechanical ventilation | ⚠ |
| Structure | Eurocodes (SS EN 1991-1998) + Singapore NAs; wind/ seismic nominal (SS EN 1998 NA, low) | ⚠ |
| Water/drainage | PUB Code of Practice on Surface Water Drainage; SS 636 water services | ⚠ |
| Environmental | NEA; BCA Green Mark (GM:2021); Environmental sustainability measures (ESM) | ⚠ |

## 5. Key numbers

**Fire — SCDF Fire Code 2023, Purpose Group II (residential flats/maisonettes), Clause 9.2 ✓:**

| Item | Value | Clause |
|---|---|---|
| Exits per storey | ≥ 2 independent staircases/exits (default) | 9.2.1a(2) |
| Single staircase option | habitable height ≤ 24 m (travel distance applies; commentary: up to 4 storeys without smoke-stop lobby) | 9.2.1a(3) |
| Single staircase above 24 m | height ≤ 60 m, ≤ 4 units/storey, 15 m max from remote unit door to stair; ventilation openings ≥ 2 m wide × 1.2 m high; lobby/corridor ≥ 2 m wide | 9.2.1a(4) |
| Distance within unit to its entrance door | ≤ 20 m | 9.2.1a(5)(a) |
| Maisonette | max 2 storeys; upper floor area ≤ 60 m² unless separate exit | 9.2.1a(5)(b) |
| External corridor one-way / two-way | 20 m (24 m if combined in-unit+corridor ≤ 40 m) / 45 m | 9.2.1a(8) |
| Common internal corridor ventilation | openings ≥ 15% floor area, ≤ 9 m from any point; or cross-ventilated high-level ≥ 50% opposing wall area, ≤ 12 m from an opening | 9.2.1a(10)(b) |
| Air well for smoke-free approach | width ≥ 6 m, plan area ≥ 93 m² | 9.2.1a(7) |
| Fire resistance | unit separation 1 hr; unit entrance door ½ hr | 9.2.1b(1)(a) |
| Facade separation > 24 m | 1-hr spandrel ≥ 1.5 m high, or 1-hr projection ≥ 600 mm | 9.2.1b(3) |
| Super high-rise | refuge floor every ≤ 20 storeys; holding area 0.3 m²/person; ≥ 2 fire lifts; fire lift car ≥ 1.7×1.5 m | 9.2.2 |
| Table 2.2A (flats) | one-way TD 15 m non-sprinklered / 20 m sprinklered; two-way 30 / 40 m; dead end 15 / 20 m; min exit widths 1.0 m (door) and 1.2 m (some cases); maisonette internal stair ≥ 900 mm | Table 2.2A, relaxed 1 Sep 2024 ⚠ column mapping uncertain |
| PWD refuge corridor | clear width ≥ 1.2 m; refuge wheelchair space ≥ 900 mm × 1.4 m; ≥ 2 holding points/storey | 2.4.2(b)(1), 2.4.4(a) |

**Not verified (⚠) — read BCA/URA primary text before drawing:** minimum headroom (habitable ~2.4 m ⚠), stair riser/tread (≤ 175 / ≥ 275 residential? ⚠), parapet/guard 1.0 m (1.2 m above 4.5 m? ⚠), accessible door clear width 850 mm / ramp 1:12 / lift car 1.1×1.4 m or as updated ⚠ (press reports a lift car 1,200×1,400 mm and door 900 mm in current code — verify cl. 4.8), minimum room sizes (no statutory minimums except HDB/ URA unit size min for non-landed 35 m² ⚠), landed housing setbacks (typically front 7.5 m, rear 4 m… ⚠ varies by area type), site coverage (landed ~ 60–75% ⚠), height (2–3 storey landed ⚠), parking (landed 1 car/unit ⚠ LTA), electrical (230 V single-phase/400 V three-phase, 50 Hz, RCCB ≤ 30 mA, SS 638) ⚠, seismic (low; SS EN 1998 Part 1 NA light) ⚠.

## 6. Permit drawing set

1. **URA** Provisional/ Written Permission (WP) application: site plan, plans, elevations, sections, GFA plan, ESM calc, roof/boundary details ⚠
2. **BCA** Plan approval: architectural + structural + M&E, accessibility, building-control computations ⚠
3. **SCDF** fire plan approval: compartmentation, exits, dry riser, hose reel, sprinkler, fire alarm ✓ practice
4. Other agencies: LTA (parking/access), PUB (drainage/sewer), NEA (waste, ventilation), NParks (trees), SP Group (electrical)
5. Via CORENET X per §2; QP submissions; TOP (Temporary Occupation Permit) → CSC (Certificate of Statutory Completion) ⚠

## 7. Common rejection reasons

- GFA computed wrongly (balcony/planter/void/bay window/roof pitch exceeding limits).
- Plot ratio or height/storey exceeds Master Plan / landed housing guidelines for the plot.
- Setbacks (front/side/rear, party-wall type) mismatched with Landed Housing Area type.
- Fire: exit staircase count/travel distance vs Fire Code 2023, missing smoke-stop lobbies, wrong corridor ventilation openings.
- Accessibility path not continuous (PWD toilet, ramp, lift lobby).
- Drainage invert levels/platform levels (PUB) or road/footpath reserves ignored.
- Submitting through the wrong channel after CORENET X mandatory dates.

## 8. Sources

- SCDF Fire Code 2023 Clause 9.2 (residential): https://www.scdf.gov.sg/fire-safety-services-listing/fire-code-2023/table-of-content/chapter-9-additional-requirements-for-each-purpose-group/clause-9.2-purpose-group-ii-occupancy ✓
- SCDF Fire Code 2023 Related tables Chapter 2 (Table 2.2A): https://www.scdf.gov.sg/fire-safety-services-listing/fire-code-2023/table-of-content/chapter-2-means-of-escape/related-tables-and-diagrams-of-chapter-2 ✓ (column mapping partial)
- SCDF Fire Code Clause 2.4: https://www.scdf.gov.sg/firecode/table-of-content/chapter-2-means-of-escape/clause-2.4 ✓
- URA circular DC26-08 CORENET X timeline: https://www.ura.gov.sg/guidelines/circulars/dc26-08/ ✓
- URA circular DC25-07 mandatory 1 Oct 2025: https://www.ura.gov.sg/Corporate/Guidelines/Circulars/dc25-07 ⚠ (search result only)
- URA Development Application page: https://www.ura.gov.sg/Corporate/Guidelines/Development-Control/Planning-Permission/DAsub ⚠ (search result only)
- BCA Accessibility Code 2019 (not readable): https://www1.bca.gov.sg/docs/default-source/universaldesign/accessibilitycode2019.pdf ⚠
