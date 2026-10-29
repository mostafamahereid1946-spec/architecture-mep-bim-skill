# South Africa — Drafting & Code Reference

Legend: **[Zn]** = value read this session from the source in §8. **⚠ verify** = drafter practice, memory, or a non-official/secondary source (SANS standards are paywalled; I did **not** obtain the standards' own text — municipal forms and guide sites were used). Numbers tied to a public guide site are labelled "guide" and should be checked against the edition your municipality enforces. The legal frame (from memory ⚠ verify): **National Building Regulations and Building Standards Act 103 of 1977** → **National Building Regulations (NBR)**, whose Part A is administrative and Parts B–XA are met by following the matching **SANS 10400** part ("deemed-to-satisfy"); the municipal building control officer (BCO) approves plans and the municipality sets zoning.

## 1. Units, scales, sheets, title block, language

| Item | Practice |
|---|---|
| Units | Metric (SI). Plans in **mm** (e.g. `3000`) on most house plans; levels in m with `+0.000` / `FFL 100.00` on site plans ⚠ practice |
| Scales | Site plan 1:200 (1:500 large sites); floor plans, elevations, sections 1:100 (1:50 for details); details 1:20, 1:10, 1:5 ⚠ practice. A SAHRA-hosted guide asks 1:100, 1:50 or 1:20, fully dimensioned, with north point and erf number on the site plan [Z4] ⚠ not municipal |
| Sheets | ISO A series; A1/A2/A3 typical; the same SAHRA guide says not smaller than A3 and not larger than A0 [Z4]. Municipal e-submission tolerates PDF at A-series size ⚠ verify per city |
| Title block | Project/erf no. (erf + township + street address), owner, professional's name + **SACAP registration** (architect/technologist) or ECSA (engineer), drawing title, scale, date, revision, drawing no. ⚠ practice [Z1: SACAP form is a required document] |
| Language | English (some municipalities also accept Afrikaans); terms: erf, building line, coverage, FAR, floor area ratio, bulk, stand, ground floor (GF), first floor (FF), plot |
| Date | YYYY-MM-DD or DD/MM/YYYY ⚠ |
| Required forms | **SANS 10400-A Form 1** (owner + professional declaration under Regulation A2), **Form 2** (appointment of a competent person for rational design/Regulation A19 areas — structural, fire, etc.), **Form 3** where applicable [Z1, Z2, Z3]. Recent forms are labelled SANS 10400-A:2022 Edition 4, older ones 2010 Edition 3 [Z3] |

## 2. CAD layer/file naming practice + authority CAD/e-submission rules

- No mandatory layer standard. Typical: AIA-style English layer names or firm standards (WALLS, DOORS, WINDOWS, DIMS, TEXT, HATCH, SANITARY, DRAINAGE, ELEC) ⚠ practice. Discipline prefixes A (architecture), S (structure), E, M, P, F (fire), XA (energy) ⚠.
- File name: `ErfNo_Suburb_Discipline_SheetNo_Rev.pdf`, e.g. `ERF1234_Sandton_ARCH_A101_P2.pdf` ⚠ practice.
- **City of Cape Town** only accepts building plans online via its **Development Application Management System (DAMS)**, requiring e-Services registration; its BDM Booklet 2 ("Building Plan Preparation and Submission") holds the drawing rules [Z5]. Older flash-drive submission is obsolete [Z5].
- **Johannesburg, Tshwane, eThekwini, Ekurhuleni** run their own portals or counters; Joburg's checklist per building type lists documents but not file rules [Z1] ⚠ verify. Always print-check scale by plotting a test PDF at 100 %.
- Digital signatures on Forms 1/2: municipalities differ; scanned wet-ink signatures common ⚠ verify.

## 3. Drafting conventions

- Floor plans show **room names with net floor areas**, ceiling heights (nominal), door/window references and a **Window & door schedule**; sections show floor-to-ceiling heights, foundations, DPC/DPM, roof pitch ⚠ practice.
- Site plan shows **building lines**, boundaries with dimensions, servitudes, adjoining erven, north point, existing/proposed coverage, drainage/sewer connection and stormwater direction ⚠ practice [Z1: zoning info + SG diagram required].
- **Drainage plan** (SANS 10400-P/ -Q) shows soil pipe, gradients, manholes, inspection eyes, municipal sewer connection point ⚠ verify.
- **Fire plan / Part T** for non-Category-1 buildings: escape routes, fire ratings, extinguishers, hose reels, compartmentation ⚠ [Z1: Fire plan is a checklist item for shop layouts and commercial].
- **Energy: Part XA** — fenestration/R-values or a rational design form; SANS 10400-XA:2021 Edition 2 is current per IEA/UJ copy; Joburg lists "Part XA rational design (if necessary)" as a document [Z1, Z6].
- Accessibility: Part S ramps, parking bays, accessible WC and signage for non-dwellings ⚠ verify.
- Heritage: buildings > 60 years old need heritage authority consent (PHRAG, SAHRA, Amafa in KZN) [Z1] [Z7].

## 4. Governing codes & authorities (table)

| Instrument | Governs | Notes |
|---|---|---|
| National Building Regulations and Building Standards Act 103 of 1977 + NBR | Legal basis; plan approval; BCO | ⚠ verify citation |
| **SANS 10400-A** General principles & requirements | Administrative, definitions, Forms 1–4 | 2022 Edition 4 forms in circulation [Z3] |
| **-B** Structural design; **-C** Dimensions; **-D** Public safety; **-F** Site operations; **-H** Foundations; **-J** Floors; **-K** Walls; **-L** Roofs; **-M** Stairways; **-N** Glazing; **-O** Lighting & ventilation; **-P** Drainage; **-Q** Non-water-borne sanitation; **-R** Stormwater; **-S** Facilities for persons with disabilities; **-T** Fire protection; **-U** Refuse disposal; **-V** Space heating; **-W** Fire installation; **-XA** Energy usage | Each NBR Part | Part list from memory ⚠ verify letters/titles; editions vary (e.g. -C Oct 2010, -O Jan 2011 per guide sources [Z8, Z9]) |
| **SANS 10142-1** Wiring of premises | Low-voltage installations; Certificate of Compliance (CoC) from a registered person | Not read ⚠ verify edition (3rd ed. 2020 from memory) |
| SANS 10160 series (loads), SANS 10100 (concrete), SANS 10162 (steel), SANS 10163 (timber), SANS 204 (energy, non-residential) | Structural/energy design | ⚠ verify editions |
| SANS 10252, 10254 (water, hot water), 10199/10400-XA (hot water solar) | Plumbing / water | ⚠ verify |
| Municipality: zoning scheme/land use scheme, building control, fire dept, roads | Setbacks, coverage, parking, approvals | Per municipality [Z1] |
| SACAP; ECSA; SAIA | Professional registration | [Z1] |
| MANTAG / Agrément SA | Alternative construction methods | Joburg lists "Agrément or MANTAG certificate (if necessary)" [Z1] |

## 5. Key numbers

### 5.1 Planning (municipal — no national value)
Building lines (street, side, rear), coverage %, floor area ratio, height, parking bays per dwelling are in the **land-use scheme of the municipality** (e.g. Johannesburg Land Use Scheme, Cape Town Municipal Planning By-law) ⚠ verify. Joburg requires a *building line relaxation letter* if the plan encroaches [Z1]. A Durban refusal notice flagged "hardened + roofed area over 40 % of the site needs a stormwater plan" — a local rule, not national [Z10].

### 5.2 Rooms and ceilings (SANS 10400-C, guide figures) [Z8]
| Item | Value |
|---|---|
| Habitable room | ≥ **6 m²** plan area, no linear dimension < **2 m** (kitchens, sculleries, laundries excepted) |
| Dwelling (permanent) | ≥ **30 m²**; "Category 1" ≥ 27 m² and ≤ 80 m² (single storey, no basement per Part T conditions) |
| Ceiling heights | Bedroom 2.4 m over ≥ 6 m² (clear ≥ 1.8 m beyond 0.75 m from edge); other habitable rooms in dwellings 2.4 m over ≥ 70 % of floor and 2.1 m over the rest; passages, entrance halls, bathrooms, WCs, laundries 2.1 m |
| Open mezzanine | ≤ 25 % of floor below, 2.1 m above and below |
| Plaster | ≥ 10 mm, no coat > 15 mm |
| Doors | No NBR width in the guide; ~700 mm clear is only practice ⚠ verify |

### 5.3 Light & ventilation (SANS 10400-O:2011 via guide) [Z9]
Natural ventilation opening ≥ **5 %** of room floor area (clause 4.3.1.1.2); toilets/bathrooms without openable window need mechanical ventilation (10 air changes per hour reported by commenter ⚠ weak source). Natural-light percentage ⚠ not confirmed; the 10 % figure often quoted is unverified. Glazing > 15 % of net floor area per storey triggers energy compliance (XA/SANS 204) per commenter ⚠ weak.

### 5.4 Stairs & balustrades (guide, attributed to SANS 10400 incl. -M, -D, -S, -T) [Z11]
| Item | Value |
|---|---|
| Riser | ≤ **200 mm**; accessible stairs ≤ 170 mm |
| Going | Comfort rule 2R + G ≈ 570–650 mm; tread ≥ 250 mm on accessible stairs; variation ≤ 6 mm |
| Stair width | Residential ≥ **750 mm** (900 mm better); escape stairs 1 000–1 800 mm by occupancy (Part T) |
| Landing | ≥ stair width and ≥ 900 mm |
| Balustrade | ≥ **1 000 mm** high; 100 mm sphere must not pass (balustrade), 450 mm sphere for railings; pool enclosure ≥ 1 200 mm; seated areas ≥ 850 mm |
| Headroom | 2.1 m measured from pitch line (secondary) ⚠ verify |
Handrail height ⚠ not found.

### 5.5 Fire (Part T) and egress
- Buildings over 3 storeys need ≥ 2 escape routes (Part T cl. 4.16, guide) ⚠ verify; hose reel per 500 m² per storey (guide) ⚠ verify. Occupancy class for houses: H4 (dwelling house) with population 2 per bedroom (Part A, guide) ⚠ verify. Category 1 building limits in 5.2.

### 5.6 Electrical
- Fixed installations need a **Certificate of Compliance** by a registered electrician under SANS 10142-1 (legal basis: Electrical Installation Regulations, OHS Act ⚠ memory). Socket spacing and minimum counts are not in the NBR — follow SANS 10142-1 ⚠ not read. Supply authority (Eskom or municipality) approves connection.

### 5.7 Structural / seismic
- Loads per SANS 10160 series; wind zones by region; seismic is low except mining-induced zones (Gauteng/Free State/North West) and Cape/Ceres area ⚠ verify SANS 10160-4. Rational design by a competent person on **Form 2** is required for Part B structure when beyond deemed-to-satisfy rules [Z1] ⚠ verify.

## 6. Permit drawing set

Johannesburg single-dwelling checklist (new/additions) [Z1]: registered title deed · power of attorney/company resolution if owner is entity · zoning information · Surveyor-General diagram · **SANS 10400 Form 1 and Form 2** · SACAP registered-professional form · building line relaxation letter + plan if applicable · site development plan approval if applicable · **Part XA** form where necessary · MANTAG/Agrément certificate for alternative construction · heritage approval if structure > 60 years. Add: site plan, floor plans, elevations (4), sections, drainage layout, window/door/room schedule, roof plan, structural/engineer's drawings and Form 2 for engineered elements, fire plan for non-dwellings ⚠ practice [Z1].

## 7. Common rejection reasons

- Missing/unsigned SANS Forms 1–2 or SACAP form [Z1] [Z3].
- Building line/coverage non-compliance without relaxation letter [Z1] ⚠ practice.
- No stormwater plan where roofed + hardened surface exceeds local threshold (Durban 40 %) [Z10].
- Heritage consent missing on structures older than 60 years [Z1] [Z10].
- Energy (XA) calculations/form absent [Z1].
- Dimensions failing Part C (room < 6 m², ceiling < 2.4 m) or ventilation < 5 % (Part O) [Z8, Z9].
- Drainage details incomplete (gradients, inspection points) ⚠ practice.
- Wrong or outdated form editions ⚠ practice [Z3].

## 8. Sources

- [Z1] City of Johannesburg building-plan submission checklists: `https://cpms.joburg.org.za/asset_uplds/docs/Checklists/Submission Categories - Checklists - revised.pdf` (PDF read this session).
- [Z2] SANS 10400-A Forms 1–4 (Joburg): `https://cpms.joburg.org.za/asset_uplds/docs/Application forms/sans10400-a-forms-1-to-4.pdf` (search description only).
- [Z3] Cape Town SANS10400-A Form 2: `https://resource.capetown.gov.za/documentcentre/Documents/Forms, notices, tariffs and lists/SANS10400-A 2016 FORM 2.pdf`; edition remark from search summary.
- [Z4] SAHRA-hosted plan guide (not a municipal document): `https://sahris.sahra.org.za/sites/default/files/orgdocs/2014/01/30/APP%201%20%286%29.pdf` (via search summary).
- [Z5] City of Cape Town building plan pages: `https://www.capetown.gov.za/City-Connect/Apply/Planning-building-and-development/Building-plan-applications/Apply-for-a-building-plan`; BDM Booklet 2 `https://resource.capetown.gov.za/documentcentre/Documents/Procedures, guidelines and regulations/BDM Booklet 2.pdf`
- [Z6] SANS 10400-XA overview: `https://www.iea.org/policies/8412-sans-10400-xa2021-national-building-regulations-energy-usage-in-buildings`
- [Z7] eThekwini refusal notice (heritage + stormwater): `https://sahris.sahra.org.za/sites/default/files/otherrefsdecisions/CE22030048%20RefusalDecision.pdf` (via search summary).
- [Z8] SANS 10400 guide, Dimensions/Part C: `https://www.sans10400.co.za/size-dimensions-room-height/`
- [Z9] Guide, Part O: `https://www.sans10400.co.za/lighting-and-ventilation/`
- [Z10] See Z7.
- [Z11] Stair/balustrade guide: `https://www.blueengineering.co.za/pages/Safe_staircases_and_balustrades_in_south_africa_and_the_regulations.html`
