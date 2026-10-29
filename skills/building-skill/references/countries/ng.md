# Nigeria — Drafting & Code Reference

Legend: **[Nn]** = value read this session from the source in §8. **⚠ verify** = drafter practice, memory, or an unofficial/secondary source. Nigeria is the thinnest of the sources I could reach: the **National Building Code text and the Lagos 2019 regulation schedules could not be opened** (the official Lagos PDF host refused the connection), so this file prefers *process and authority facts* to numbers. Where a number is given it is either read from a source or labelled ⚠.

Structure of control: **National Building Code (federal model, adopted state-by-state; its provisions apply "subject to adoption by the states")** [N1] → **state planning authority issues the development permit** → **state building-control agency inspects**. In Lagos these are **LASPPPA** (Lagos State Physical Planning Permit Authority) and **LASBCA** (Lagos State Building Control Agency) [N2]. Other states have their own ministry/agency (Abuja: FCDA / Development Control Department ⚠ verify).

## 1. Units, scales, sheets, title block, language

| Item | Practice |
|---|---|
| Units | Metric. Plans in **mm** (dimension strings) or **m** on site plans; levels in m (`+0.15`) ⚠ practice |
| Scales | Federal Housing Authority guidance: site plans **1:100–1:200** by scope; sections and elevations **1:50–1:100**; details **1:10–1:25**; the scale used must be marked on every sheet [N3] (an FHA document, not a state building authority) |
| Sheets | ISO A series (A1/A2/A3) ⚠ practice; permit sets are plotted and submitted in paper copies [N2, N3] |
| Title block | Project, client, location/plot no./layout, drawing title, scale, date, drawn/checked, revision, **ARCON registration no. and stamp**, architect's signature [N3]; structural sheets carry **COREN** stamp [N3]; survey sheets carry **SURCON** stamp [N2] |
| Language | English |
| Dates | DD/MM/YYYY ⚠ |
| Professionals | Architect: ARCON (regulator; NIA is the professional body); structural/civil engineer: COREN; surveyor: SURCON (SURCON also named in [N2]); builder: CORBON ⚠; planner: TOPREC ⚠ memory |

## 2. CAD layer/file naming practice + authority CAD/e-submission rules

- No mandatory layer or file naming standard found. Common AutoCAD/ArchiCAD practice with English layer names (WALL, DOOR, WINDOW, DIM, TEXT, GRID, FURN, ROOF) ⚠ practice. File names such as `ProjectName_Plan_GF_Rev1.dwg` ⚠ practice.
- **Lagos** permit package: five sets each of ARCON architectural drawings, COREN structural drawings and SURCON survey plan; application can be submitted online or at the LASPPPA zonal office [N2]. Federal Housing Authority asks ≥ **4 sets** signed by a registered architect, one ARCON stamp per copy, and COREN-stamped structurals with calculations [N3]. Exact e-submission file specifications (PDF size, DWG) not found ⚠ verify at the portal.
- Many state offices still want **stamped paper sets**; digital stamp acceptance varies ⚠ verify.

## 3. Drafting conventions

- Site plan shows survey beacons, plot dimensions, setbacks/building line, access road, drainage/gutters, soakaway, septic tank, boundary wall/gate, parking — and orientation/circulation analysis [N3] ⚠ practice.
- Plans typically show walls in 225 mm (9 in) or 150 mm (6 in) sandcrete blocks, dimensioned to 225 mm module, with doors/windows scheduled ⚠ practice (not code).
- Foundation, DPC level, floor slab, ring beam, roof structure (timber/steel trusses with long-span aluminium roofing sheets) are drawn on sections — these are the stages LASBCA inspects (see §6) [N2].
- Show septic tank + soakaway location, borehole where applicable, and generator house/space with clearances ⚠ practice.
- Fire: escape routes, extinguishers, hose reels on larger buildings per National Building Code fire part ⚠ verify; not read.

## 4. Governing codes & authorities (table)

| Instrument / body | Role | Notes |
|---|---|---|
| **National Building Code of Nigeria** (federal, 2006; an IEA entry lists it as 2008 — conflicting year, status "in force") | Minimum standards for design, construction, alteration, demolition, repair across Nigeria | Applies where adopted by states; ARCON says there is no coherent national enforcement framework or enabling law [N1, N4] ⚠ verify edition/year |
| Lagos State Physical Planning Permit and Building Control Regulations 2019 (revised LASPPPA regulation) | Permit process, setbacks, coverage, appeals | Passed by Lagos House of Assembly; LASBCA fee for inspection = 20 % of the planning permit's Building Plan Assessment fee; written notice to LASBCA before work starts [N5] |
| Lagos State Urban and Regional Planning and Development Law 2010 | Planning law | Referred to in research [N6] ⚠ verify |
| **LASPPPA** | Development permit | [N2] |
| **LASBCA** | Stage inspections; Certificate of Fitness for Habitation (CFH) | [N2] |
| Lagos domestication of NBC / Building Energy Efficiency Code (BEEC) | Lagos said it will not adopt NBC in full; will fold in energy efficiency | [N4] ⚠ verify status |
| **NEMSA** (Nigerian Electricity Management Services Agency) | Electrical safety, inspection, testing and certification of installations | Mandate now carried in the Electricity Act 2023 [N7]; NEMSA/SON MoU on enforcement [N7] |
| **SON** (Standards Organisation of Nigeria) | Product standards (cables, fittings) | Enforcement MoU with NEMSA [N7] |
| Nigerian wiring rules | Installation practice follows locally issued NEMSA rules and widely BS 7671 | Not confirmed in sources ⚠ verify (user mentioned "NEC / Nigerian Electricity rules") |
| ARCON / COREN / SURCON / NIA / NIOB | Registration and stamps | [N2, N3] |
| Environment (Lagos Ministry of Environment); Land Use Charge office; Lagos Development Levy | Clearances | EIA for larger/commercial projects [N2] |

## 5. Key numbers

Few official numbers could be verified; **do not fill gaps with guesses — pull the number from the authority**.

### 5.1 Planning (Lagos regulation as summarised in an academic paper) [N6]
| Zone | Plot size | Max building footprint coverage | Dwellings / ha | Greenspace |
|---|---|---|---|---|
| Low density | 1 000 m² | 50 % | 30 | 20 % of plot |
| Medium density | 864 m² | 60 % | 90 | 10 % |
| High density | 648 m² | 70 % | 270 | 10 % |
- The paper cites "Lagos State Building Regulation 2010" and the LASPPPA 2019 PDF as source of the table; private-open-space : footprint ratio 50:50, 40:60, 30:70 for the three zones ⚠ verify against the official regulation, since a survey in the paper found developers non-compliant.
- **Setbacks (front/side/rear) depend on adjacent road width and land-use zone**; building line is strictly enforced; a news item says setbacks range 3 m to 9 m but that is general, not a residential rule [N2] [N8]. Obtain the setback schedule from LASPPPA before drawing (a pre-application consultation is offered) [N2]. No setback number is given here because none could be verified.
- PPTR (Physical Planning Technical Report) required for residential land ≥ 1 hectare, or residential schemes with > 8 family units (2019 Regs, section 4, subsection 15(a)) [N9].

### 5.2 Stairs, doors, ceilings, rooms, parking, fire, electrical, seismic
No verifiable Nigerian values were found for: stair riser/tread, door widths, ceiling height, minimum room areas, parking ratio, egress distances, receptacle counts, seismic parameters. Do **not** import Indian, Philippine or British figures. Nigerian mains supply is 230 V / 50 Hz ⚠ verify (memory). Seismic design is generally not governing in most of Nigeria (low seismicity) ⚠ verify; wind, flooding, and soil (lagoon/sand fill in Lagos) govern foundations ⚠ practice.

## 6. Permit drawing set (Lagos) [N2]

- Completed LASPPPA development-permit application form · certified **C of O** (certificate of occupancy) or title document · Lagos Development Levy payment evidence · **Land Use Charge clearance** · EIA from Ministry of Environment for larger/commercial schemes.
- **Five sets each**: ARCON architectural drawings (plans, elevations, sections, roof plan, site plan), COREN structural drawings with calculations, SURCON survey plan from the C of O.
- Process: optional pre-application consultation; submit online or at zonal office; pay fee and keep reference; technical review and site inspection; **21-day neighbour notice**; permit issued; keep permit and approved drawings on site. Statutory review 21 working days; practical timeline 4–8 weeks for simple houses [N2].
- **LASBCA stage inspections**: before foundation pour; DPC (before walls go higher); wall-plate level; roof structure (before sheeting); completion → **Certificate of Fitness for Habitation** needed for legal occupation/mortgage [N2]. Written notice to LASBCA before work starts [N5].
- Federal Housing Authority variant: ≥ 4 architectural sets signed by registered architect, one ARCON stamp per copy; structurals COREN stamped with calculation sheets [N3].

## 7. Common rejection reasons

- Drawings not carrying ARCON stamp/registration, or structural drawings without COREN stamp and calculations [N2, N3].
- Setbacks / building line encroached; canal, drain or road setbacks violated — LASBCA seals such buildings [N8].
- Coverage above the zone limit or insufficient open space [N6].
- Missing C of O, survey plan, levy or Land Use Charge clearance [N2].
- Starting work without building-control notice or skipping stage inspections [N2, N5].
- Above-threshold schemes without Physical Planning Technical Report [N9].
- Heritage/EIA issues on larger projects [N2].

## 8. Sources

- [N1] IEA policy entry, National Building Code (year 2008 shown, in force, subject to adoption by states): `https://www.iea.org/policies/8518-national-building-code`
- [N2] Ownkey guide to Lagos permits (secondary; drawn from LASPPPA/LASBCA process): `https://ownkey.com/ng/blog/building-permit-nigeria-guide`
- [N3] Federal Housing Authority, architectural plan requirements: `https://fha.gov.ng/architectural-plan`
- [N4] BusinessDay on Lagos domestication of the NBC: `https://businessday.ng/news/article/building-failure-lagos-experts-mull-domestication-of-natl-building-code/`; ARCON on legal backing: `https://www.thisdaylive.com/2022/08/23/arcon-tasks-national-assembly-on-legal-backing-for-building-code/`
- [N5] Guardian on the 2019 Lagos regulations (LASBCA notice, 20 % fee): `https://guardian.ng/?p=1107216`
- [N6] Acta Horticulturae et Regiotecturae 25 (2022) paper on Lagos footprint coverage: `https://reference-global.com/download/article/10.2478/ahr-2022-0008.pdf` (cites `https://epp.lagosstate.gov.ng/regulations/REVISED_LASPPPA_REGULATION_2019_1.pdf` — host unreachable from this session).
- [N7] NEMSA/Electricity Act 2023 and SON MoU coverage: `https://nannews.ng/son-nemsa-sign-mou-on-enforcement-of-standards`; `https://www.thisdaylive.com/2023/11/17/nemsa-moves-for-more-inspectorate-offices-to-enforce-standards-in-electricity-sector/`
- [N8] VON on setback enforcement: `https://von.gov.ng/?p=44823`
- [N9] SMC Insights on PPTR thresholds: `https://smcinsights.substack.com/p/physical-planning-reports-for-development`
