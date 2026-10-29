# Australia — Drafting & Code Reference

Legend: **✓** = read this session on an ABCB/NCC page or standards-body listing (URL in §8). **⚠ verify** = memory/secondary (calculator & tool sites) or not opened. The NCC text on ncc.abcb.gov.au was only partly fetchable (Victorian variation page for Part D2 read; general D2/D3 pages returned 404 to the tool) — so most NCC dimensions below are **secondary** and flagged.

**Rule of thumb:** the **NCC** (National Construction Code) is adopted by each state/territory with **local variations** (Victoria, NSW, Qld, WA, SA, Tas, ACT, NT). Planning (setbacks, height, site cover, FSR) is **not** in the NCC — it is the local **council LEP/DCP, Planning Scheme, or Residential Design Codes (WA R-Codes)**. Never invent setbacks.

---
## 1. Units, scales, sheets, title block, language

| Item | Practice |
|---|---|
| Units | Metric; plan dimensions in **mm** (no unit), levels in **m** as RL (reduced level, m AHD) ✓ practice, AS 1100.101 |
| Datum | Australian Height Datum (AHD); MGA2020 / GDA2020 coordinates ⚠ |
| Language | English |
| Sheets | ISO A0/A1/A2/A3 (AS 1100.101 sheet sizes); A1 typical for permit set, A3 for DA sets ⚠ |
| Scales | Site 1:200 (1:100–1:500), plans/elevations/sections 1:100 (1:50 for small), details 1:20–1:5; scale bar on every sheet ⚠ |
| Title block | Project/address (lot, DP), client, drawing title/no./revision, date, scale, author with **registration number** (e.g. Architects Board / Building Practitioner) ⚠ |
| Area terms | GFA, **floor space ratio (FSR)**, site coverage, **private open space (POS)**, **deep soil / landscaped area** ⚠ |
| Drafting standard | **AS 1100.101-1992 (R2014)** Technical drawing — General principles; **AS 1100.301-2008** Architectural drawing; AS/NZS 1100.201 mechanical, 1100.501 structural ✓ catalogue |
| Projection | Third-angle ⚠ (AS 1100.101) verify |

## 2. CAD layer/file naming practice + authority CAD/e-submission rules

| Topic | Practice |
|---|---|
| Layer standard | No statutory national CAD layer standard. Industry uses **AS 1100.301** conventions, **NATSPEC BIM**/ISO 19650 naming, or `A-WALL` AIA style ⚠ |
| File naming | ISO 19650 style `[Project]-[Originator]-[Zone]-[Level]-[Type]-[Role]-[Number]` ⚠ |
| Submissions | PDF drawings via council **portals** (NSW Planning Portal, Victoria e-lodgement, Qld MyDAS/PD Online) ⚠ — DWG not usually required; some require **A3 PDF set + DWG for engineering/PCA** ⚠ |
| Digital signatures | Certifiers accept signed PDFs; **building surveyor/certifier** lodges |
| BIM | IFC acceptable but not mandatory; ⚠ council-specific |

## 3. Drafting conventions

- **Levels**: finished floor level (FFL) and natural/finished ground (NGL/FGL) as RL; ceiling height `CH 2400`.
- **Labels**: ALL CAPS room names; "BED 1", "MASTER", "ENS" (ensuite), "WIR", "LDY", "PWD" ✓ practice.
- **Dimensions** from structure face/centre per task; overall + opening dims; **set-out** notes for door swing.
- **Required symbols**: north point (true north), section tags `A-A`, elevations labelled N/E/S/W (compass elevations).
- **Hatches**: brick veneer, timber frame, concrete; wall legend with **fire-rating** (e.g. FRL 60/60/60) ✓ practice.
- **Bushfire BAL** (BAL-LOW/12.5/19/29/40/FZ) notes under AS 3959 ⚠, **wind class** (N1–N6, C1–C4 AS 4055) ⚠, **climate zone** (NCC 1–8), **NatHERS** ratings.
- **Notes**: "ALL WORK TO COMPLY WITH NCC 2022 VOLUME TWO", state variation list ⚠.

## 4. Governing codes & authorities

| Item | Code | Status |
|---|---|---|
| NCC 2022 | **Vol 1 (Class 2–9 buildings, BCA)**, **Vol 2 (Class 1 & 10, Housing Provisions)**, **Vol 3 (Plumbing)** — ABCB; states adopt with variations; **NCC 2025** now published and adopting by state/territory ⚠ verify transition dates | ✓ ncc.abcb.gov.au |
| Access | **AS 1428.1-2021** design for access and mobility (general requirements); AS 1428.2 (enhanced), DDA premises standards (Access to Premises Standard 2010) | ⚠ |
| Wiring | **AS/NZS 3000:2018** Wiring Rules (+ Amendments); AS/NZS 3008 cable selection | ⚠ |
| Structure | AS 1170 series (loads), AS 1170.4 earthquake, AS 3600 concrete, AS 4100 steel, AS 1684 timber framing | ⚠ |
| Fire | NCC Section C/D/E; AS 1670 (alarms), AS 2118 (sprinklers), AS 1851 maintenance, state fire authority (FRNSW, CFA/FRV, QFES) | ⚠ |
| Energy | NCC Section J (Vol 1) / Part 13 Housing Provisions; **NatHERS 7-star** from NCC 2022 | ⚠ |
| Bushfire | **AS 3959:2018** | ⚠ |
| Planning | LEP/DCP (NSW), Planning Scheme/ResCode (Vic), Planning Scheme/QDC MP (Qld), R-Codes (WA), Planning & Design Code (SA) | ⚠ |
| Certification | Private **Registered Certifier / Building Surveyor / PCA / Building Certifier** issues CC/BP | ⚠ |

## 5. Key numbers (mostly ⚠ secondary — verify against NCC 2022)

**Stairs (private & public):**

| Item | Value | Source |
|---|---|---|
| Riser | **115–190 mm** | NCC 2022 Housing Provisions Table 11.2.2a (secondary: calcforlife/ buildingtools) ⚠ |
| Going | **240–355 mm** (public/Vol 1 stairs 250–355 per tool) | same ⚠ |
| 2R+G quantity | 550–700 mm | same ⚠ |
| Riser/going consistency | adjacent ≤ 5 mm variation, whole flight ≤ 10 mm | NCC 2022 Vol 1 D3D14 ⚠ (ABCB search summary) |
| Barrier required | where a fall of **≥ 1 m** is possible | NCC 2022 Vol 1 D3D? ⚠ |
| Barrier height | **≥ 1 m** generally (Vol 1 D3D18(1)); stair-flight balustrade ≥ 865 mm above nosings (Vol 2) | nccb.gov.au FAQ ✓ (ABCB page: "current required minimum height of 1 m"); 865 ⚠ |
| Opening between balusters | **≤ 125 mm** (≤ 40 mm gap between barrier and balustrade where face-fixed rule applies) | ✓ NCC 2022 change notice; 125 ⚠ |
| Min doorway (Victoria D2D9) | unobstructed width **750 mm** in other cases (not sanitary/bathroom) | **VIC D2D9(4)** ✓ |

**Egress, ceilings, rooms, parking:**

| Item | Value | Status |
|---|---|---|
| Exit/ path to exit clear width | ≥ 1 m (2019 D1.6(b)(i) → D2 section in 2022) | ABCB seminar ⚠ |
| Class 2 (apartment) travel distance to exit | 6 m to a point of choice, 20 m to single exit, 40 m max alternate | memory ⚠ verify D2D5 |
| Dead end | 6 m (Class 2 ≤ 20 m via sole-occ unit) | ⚠ |
| Habitable room ceiling height | 2.4 m (Class 1); 2.1 m for bath/laundry/corridor ⚠ | NCC 2022 Vol 2 ⚠ |
| Min room sizes | none in NCC for floor area; local council/ State minimum rules (e.g. Victorian apartment Better Apartments Design Standards) | ⚠ |
| Light & ventilation | habitable rooms natural light ≥ 10% of floor area; ventilation 5% ⚠ | NCC 2022 Vol 2 Part 10 ⚠ |
| Smoke alarms | interconnected where multiple in Class 1 (AS 3786); hardwired in 240 V, in every sleeping area ⚠ | NCC 2022 ⚠ |
| Setbacks / site cover | **council-specific** (e.g. NSW low-density: front ~4.5–6 m, side 0.9 m ground; Vic ResCode: front 9 m or avg ⚠) — always read the local plan | ⚠ |
| Parking | council-specific (typically 2 spaces/house, 1/1.5 for apartments ⚠) | ⚠ |
| Wiring | 230 V single-phase / 400 V three-phase, 50 Hz; RCD 30 mA on circuits ≥ 1 per AS/NZS 3000 ⚠ | ⚠ |
| Seismic | AS 1170.4 hazard factor Z by site (0.03–0.22 ⚠), earthquake design category; importance level IL2 for houses ⚠ | ⚠ |
| Wind | AS 4055 N1–N6 / C1–C4; Qld cyclonic region C ⚠ | ⚠ |

## 6. Permit drawing set (DA → CC → Occupation)

1. **Development Application (DA)** with council: survey, site analysis, site plan, floor plans, elevations, sections, shadow diagrams, landscape plan, BASIX (NSW)/NatHERS cert, stormwater concept, statement of environmental effects ⚠
2. **Construction Certificate (CC) / Building Permit** with private **certifier**: structural (engineer's certified drawings), wet area details, fire/ BCA report, energy report, bushfire (BAL) report, plumbing/drainage layouts, specs ⚠
3. Mandatory inspections by certifier → **Occupation Certificate / Certificate of Occupancy / Certificate of Final Inspection** ⚠
4. Other approvals: water authority (Sydney Water Section 73 etc.), tree removal, heritage, bushfire authority ⚠

## 7. Common rejection reasons

- Setbacks / site cover / FSR / height breaches under LEP/DCP (not the NCC) — most DA refusals ⚠.
- Missing shadow diagrams, solar access, privacy screens, cut-and-fill/retaining details ⚠.
- Stair geometry outside riser/going range; no balustrade where fall ≥ 1 m ✓ (NCC).
- Fire separation: boundary distance & FRL on walls within 900 mm of boundary ⚠ (NCC Vol 2 Part 5.? / 9.x?).
- Bushfire BAL not assessed; wind class / soil class (AS 2870) missing from structural.
- Accessibility (AS 1428.1) paths, ramp grade 1:14, door clear 850 mm ⚠.
- No energy/BASIX/NatHERS certificate; wrong NCC edition cited.
- Drainage/stormwater (on-site detention) concept missing.

## 8. Sources

- NCC 2022 Vol 1 Victoria Part D2 variations (read): https://ncc.abcb.gov.au/editions/ncc-2022/adopted/volume-one/10-victoria/d2-provision-escape ✓
- ABCB FAQ stairways barriers handrails: https://www.nccb.gov.au/faq/stairways-barriers-and-handrails ✓ (summary)
- NCC 2022 change notice, face-mounted balustrades: https://www.nccb.gov.au/news/2022/ncc-2022-changes-face-mounted-balustrades ⚠
- NCC 2022 Vol 1 Part D3 (NSW variation page): https://cpd.nccb.gov.au/editions/ncc-2022/adopted/volume-one/5-new-south-wales/d3-construction-exits ⚠ not fetchable
- AS 1100.101 catalogue entry: https://infostore.saiglobal.com/en-us/Standards/AS-1100-101-1992-R2014--210494/ ✓
- AS 1100.301-2008 preview: https://www.saiglobal.com/PDFTemp/Previews/OSH/AS/AS1000/1100/1100.301-2008.pdf ✓
- Stair geometry summaries (secondary): https://calcforlife.com/en-au/stair-calculator/ , https://buildingtools.co/tool/access-stairs-private-handrails-balustrades ⚠
- ABCB seminar (exit widths): https://ncc.abcb.gov.au/resources/videos/2022-ncc-seminars-volume-one-access-and-egress-services-and-equipment ⚠
