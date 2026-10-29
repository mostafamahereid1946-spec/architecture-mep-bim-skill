# Structural - Method Reference

Tags: **[RoT]** = rule of thumb for preliminary sizing only (never final design); **[CODE]** = take from country file / governing code (ACI 318, Eurocode 2/BS 8110, ECP 203, SBC 304 etc.); **⚠ verify** = unconfirmed. Final sizes come from analysis and design checks; RoT values are for layout/coordination and sanity checks of software output.

## 1. Workflow

| Step | Output |
|---|---|
| 1. Collect inputs | Arch plans/sections, geotechnical report (bearing capacity, water table, sulfates, soil class), loads (live, wind, seismic zone/site class), material grades, code |
| 2. Choose system | Section 2; confirm with architect (grid, ceiling heights, openings) |
| 3. Column grid + cores/shear walls | Grid aligned with walls; columns not in doors or room centres; shear walls in cores |
| 4. Preliminary sizing | Section 4 ratios |
| 5. Load take-down | Section 5 |
| 6. Analysis model | Frame/FE model (ETABS/SAFE/STAAD/SAP/Robot), gravity + lateral combos [CODE] |
| 7. Member design | Slabs, beams, columns, walls, footings, stairs |
| 8. Drawings + schedules | Section 8 |
| 9. Coordination | Section 9 |
| 10. Check | Section 10 |

## 2. Structural systems

| System | Typical span m | Typical use / height | Notes [RoT] |
|---|---|---|---|
| RC beam-column frame, one-way/two-way slab | 4-8 | Villas, apartments up to ~10-15 storeys with walls | Most common ME/Egypt; cheap formwork; deeper ceiling beams |
| RC flat plate / flat slab (drop panels) | 5-9 | Offices, parking, apartments | Min floor depth, punching shear governs; drop panel or column head |
| Ribbed / waffle slab | 8-12 | Long spans, parking | Rib 125-200 wide at 600-900 c/c; topping 50-100 |
| Post-tensioned slab | 8-12+ | Parking, offices | Thinner (L/35-40 ⚠), needs PT drawings/specialist |
| Shear wall / core + frame | - | Tall (> ~8 storeys) | Core carries lateral; walls 200-400 |
| Tube/outrigger | - | > ~40 storeys | Specialist |
| Load-bearing masonry | 3-5 | 1-3 storeys, low-rise | Walls 200-250, ring beams/lintels |
| Steel frame (composite deck) | 6-15 | Offices, industrial, atria | Beam depth L/20-L/25 ⚠; fire protection required |
| Precast / hollow-core | 6-12 | Parking, industrial, repetitive | Connection design key |
| Light-gauge steel / timber | 3-6 | Villas, low-rise (US/UK/Aus) | |
| Space frame / long-span roofs | 20-80+ | Halls, stadiums | Specialist |

Foundations: isolated pad, combined, strip, raft (mat), piles (bored/driven), pile caps; basement retaining walls; waterproofing.

## 3. Grid and layout rules [RoT]

- Residential grid 3.5-6.0 m; offices 7.5-9.0 m; parking 7.5-8.4 m bay (3 cars x 2.5-2.8) and 5.0-5.5 deep + aisle 6.0-7.0 (see civil); industrial 9-12 m.
- Economical span range RC slab+beam 5-8 m; flat slab 6-9 m; PT 8-12 m.
- Place columns at wall intersections and corners; avoid columns in the middle of door openings; align columns vertically (avoid transfer); keep similar spans (adjacent spans within ~1:1.25 ⚠) to avoid unbalanced moments.
- Cantilevers (balconies) ≤ 1.5-2.0 m for reinforced slab; edge beams for larger; balcony cantilever depth L/10.
- Shear walls/cores: symmetrical about the centre of mass where possible, keep centre of rigidity near mass centre; at least 2 non-parallel, non-concurrent walls/frames each direction.
- Expansion joint at 30-60 m length [RoT, depends on climate/code; hot climates 30-45 ⚠ verify]; seismic joints [CODE].
- Settlement/differential: separate adjacent buildings with different foundation levels with a joint.
- Roof water tanks and pools: show loads and position; place over columns/walls.
- Stairs and lift cores: lift pit depth 1.2-1.8 [per supplier], overrun 4.2-5.0 above top landing [per supplier], pit waterproofing.

## 4. Preliminary sizing [RoT]

L = span (m). Results in mm unless stated. Round up to formwork module (25 or 50).

### Slabs
| Type | Depth |
|---|---|
| One-way solid slab, simply supported | L/20-L/22 (ACI 318 min L/20) |
| One-way, one end continuous | L/24 (ACI), L/26 (EC2 end span at low steel) |
| One-way, both ends continuous | L/28 (ACI), L/30 (EC2 at low steel) |
| Two-way slab on beams (continuous) | L_short/30-L_short/36 (typically 120-200) |
| Flat plate | L/28-L/32 (150-300); min 125-150 ACI; punching check |
| Flat slab with drop panels | L/30-L/36; drop panel typically adds 25-50% of slab thickness ⚠ verify |
| Ribbed one-way | overall L/18-L/22 (ribs 150-250 depth + topping 50-100) |
| Waffle | L/20-L/25 |
| PT flat slab | L/40-L/45; PT beam L/20-L/25 ⚠ |
| Cantilever slab | L/7-L/10 |
| Minimum thickness | 120-150 (sound/fire/cover), 100 minimum [CODE] |

ACI 318 minimum thickness (fy 420 MPa, normal weight) - one-way slabs: simply supported L/20, one end continuous L/24, both ends L/28, cantilever L/10; beams L/16, L/18.5, L/21, L/8 ⚠ verify edition tables.
EC2 basic span/effective-depth ratios (Table 7.4N concept, before modification factors; for lightly stressed r = 0.5% / highly stressed r = 1.5%): simply supported 20/14, end span 26/18, interior span 30/20, flat slab 24/17, cantilever 8/6 ⚠ verify.

### Beams
| Item | Rule |
|---|---|
| Depth (total) | Simply supported L/10-L/12; continuous L/12-L/15; cantilever L/5-L/6 (RoT) |
| Width | 0.4-0.6 x depth; min 200-250 (300 in seismic/ heavy shear); equal to wall thickness (200/250) for hidden/aesthetic |
| Transfer beam | L/6-L/8 |
| Primary beam spacing in steel composite | 2.5-3.5 m secondary; deck 0.9-1.2 mm ⚠ |
| Hidden (band) beam | width 3-5 x slab depth; depth = slab + 50-100 |
- Check: deflection (L/250 total, L/350-500 after finishes [CODE]), shear, cracking, headroom, and web openings.

### Columns
- Ultimate load N (kN) = (number of floors) x (tributary area) x (ultimate floor load). Typical total ultimate floor load for RC residential/office 14-18 kN/m² per floor incl. self weight ⚠ verify; service ~ 10-12 kN/m² [RoT].
- Area A_c (mm²) ≈ N x 10³ / (0.3-0.4 f_ck) at 1-2% steel [RoT, concentric loading]; increase 20-40% if moments significant (edge/corner columns). Example: N = 3000 kN, f_ck = 30 MPa -> A_c ≈ 3,000,000 / (0.35x30) ≈ 285,700 mm² -> 550 x 550.
- Minimum 250-300 (200 for 1-2 storey), slender ratio l_0/h ≤ 15-25 (short column limit ≈ 12 braced [CODE]); circular dia 350-500.
- Longitudinal steel 1-4% (min 0.8-1% per code, max 4% outside lap, 6-8% at lap [CODE]); ties ø8-10 @ 150-300 [CODE].
- Column size reduction up the building: keep size, reduce steel; change at most every 5-8 storeys.
- Corner/edge columns carry fewer loads but moment: size ≥ internal column on lower floors.

### Walls
- Shear wall thickness: ≥ 200 (or H/20-H/25 floor height) and ≥ 250 for tall (> 20 storeys, [CODE]); lift core 200-300; basement retaining wall 250-400 (H/10-H/12).
- Plan length of shear walls ~ 1.0-1.5% of floor area in each direction for moderate seismic; ⚠ verify.

### Foundations
- Allowable bearing: from geotech report - typical 100-300 kPa for medium sand/stiff clay (use geotech value, never RoT). Pad area A = (service column load + footing weight 5-10%) / q_a.
- Pad depth: 300-600 (min 300), governed by punching/one-way shear; start with thickness ~0.3-0.4 x cantilever projection beyond column face, then check.
- Rule: if sum of pad areas > 50% of building footprint, consider raft/strip.
- Raft thickness typically 0.4-1.2 m (~span/8-span/6 when heavily loaded) ⚠ verify; size by FE/punching, not by this. Raft edge extends 0.5-1.0 beyond outer columns.
- Piles: capacity from geotech; pile size 400-1000 dia typical; spacing ≥ 3 x dia; pile cap depth ~ 2-2.5 x dia ⚠.
- Minimum founding depth below ground 1.0-1.5 (below frost depth in cold climates; below fill/topsoil, usually ≥ 1.2 for ME).
- Plinth beams/tie beams between footings; ground slab 100-150 on 150 compacted base; basement slab thickness 300-500+.
- Hot climate/ME: use sulfate-resistant cement (SRC) / blended cement + bitumen coating for footings in saline soils [CODE]; ground water table → dewatering and waterproofing.

### Stairs
- Waist slab thickness L/20-L/25 (150-200 typical); landing slab per spans; support on core walls/beams.

## 5. Loads (typical values; always use [CODE])

| Load | RoT value |
|---|---|
| Reinforced concrete | 25 kN/m³ (150 lb/ft³) |
| Plain/ lean concrete | 23-24 |
| Steel | 77-78.5 |
| Hollow block 200 mm + 2x20 plaster | 2.3-3.0 kN/m² of wall (full height) ⚠ varies by block density |
| Hollow block 100 mm + plaster | 1.5-1.7 |
| Solid block wall 200 | 4.0-4.5 |
| Brick wall 250 (2 bricks) | ~4.5-5.0 |
| Screed 50 + tile 20 | 1.2-1.8 |
| False ceiling + services | 0.3-0.7 |
| Partition allowance (movable) | 1.0-1.5 (UK/EC1 allow 1.0 for ≤ 3 kN/m line; US 15 psf = 0.72) |
| Live load residential | 1.5-2.0 kPa (US 40 psf = 1.9) |
| Live load office | 2.5-3.0 kPa (US 50 psf =2.4; lobbies 100 psf=4.8) |
| Corridor/assembly | 3.0-5.0 kPa |
| Balcony | 2.5-4.0 kPa |
| Stair | 3.0-5.0 kPa |
| Roof (accessible/inaccessible) | 1.5 / 0.75 |
| Car parking (cars) | 2.5 kPa (US 40 psf) |
| Plant rooms | 7.5 or equipment |
| Water tank | 10 kN/m³ x depth (1 m = 10 kPa) |
| Soil (backfill) | 18-20 kN/m³ |

Combinations [CODE]: e.g., 1.4G + 1.6Q (BS 8110/ECP 203 old), 1.35G + 1.5Q (EC0), 1.2D + 1.6L (ACI/ASCE 7), plus wind/seismic combos.
Load path: slab -> secondary beams -> primary beams -> columns/walls -> foundations -> soil. Lateral: floor diaphragm -> shear walls/frames -> foundations. Show on a sketch for anyone confirming correctness.
Wind: from [CODE] basic wind speed, exposure, pressure coefficients; seismic: zone/site class, response spectrum, drift limits (H/400-H/500 typ. ⚠ verify), irregularity checks; hot climate: thermal effects, expansion joints.

## 6. Material and durability notes [RoT unless CODE]

| Item | Typical |
|---|---|
| Concrete grade | Foundations/columns C30-C40 (f_ck 30-40 MPa), slabs/beams C25-C35, blinding C15-C20; (f'c 3000-5000 psi) |
| Steel | Grade 500 (EU/UK B500B), Grade 60 (420 MPa) US, 400/ 360 (Egypt) ⚠ verify per country |
| Cover | Internal slab 20-25; beams/columns 25-40; external 40-50; against ground 50-75; ACI: 20 slabs, 40 beams/columns, 75 cast against earth (⚠ verify, check exposure & fire) |
| Lap length | 40-60 x bar dia tension (40d typ for good bond) - [CODE] exact |
| Min bar spacing | max(bar dia, 20-25 mm, 1.33 x agg size) |
| Slab reinforcement | min 0.12-0.2% of gross area each way (shrinkage/temp) [CODE] |
| Rebar sizes | Metric: 8,10,12,14,16,20,25,32,40; US: #3 (10 mm), #4 (13), #5 (16), #6 (19), #7 (22), #8 (25), #9 (29), #10 (32), #11 (36) |
| Rebar weight kg/m | 0.00617 x d² (d in mm): d10 = 0.617, 12 = 0.888, 16 = 1.58, 20 = 2.47, 25 = 3.85 |
| Concrete cube/cylinder | f_cu ≈ 1.2 x f_ck (cylinder) roughly: C30/37 -> 30 cyl / 37 cube |
| Fire resistance cover/size | Per [CODE] 1-4 hr tables |
| Construction joints | Max pour 15-20 m slab, keep sizes manageable; joint location at span L/3-L/4 ⚠ |

## 7. Reinforcement detailing notation

### 7.1 BS 8666 / UK-Euro style
Bar callout: `no. type dia - mark - spacing   location`, e.g. `12T16-05-200 B1` or `T12-02-150 T1` (type: R plain mild, T high yield, S stainless; dia mm; mark = bar mark number; spacing mm; location: B1 bottom layer 1 (outer), B2 bottom layer 2, T1 top layer 1, T2 top layer 2; EF each face, NF near face, FF far face).
- Link/stirrups: `T10-12-200` along beam; closer spacing near supports `T10-12-100 for 2d`.
- Slab: `T12-01-200 B1` bottom main, `T12-02-200 B2` bottom secondary, `T12-03-150 T1` top, etc. Sketch bar marks in plan with arrows and extent lines.
- Bar bending schedule (BBS) per BS 8666: Member | Bar mark | Type and size | No. of members | No. bars in each | Total no. | Length of each bar (mm) | Shape code | A | B | C | D | E/r.
- Shape codes (selected, ⚠ verify dimension letters): 00 straight; 11 single bend (L) - A, B; 12 - two bends ⚠; 13 - bends at both ends; 21 - U-shape with two bends - A, B, C; 41 - Z/crank ⚠; 51 - closed link with hooks ⚠; 99 - special shape (defined by sketch).
- Bend radii/hook dims by code (e.g., min bend dia 4d for ≤ 16 mm, 7d for > 16 mm; hooks 2-5d ⚠ verify BS 8666 Table 2); dims in schedule given as out-to-out except where otherwise stated.
- Bar sizes per BS 8666: 6, 8, 10, 12, 16, 20, 25, 32, 40, 50.

### 7.2 ACI 315 / US style (also ACI SP-66, CRSI Manual)
- Callout: `(4) #8 TOP`, `#4 @ 12" O.C.`, `#5 @ 6" E.W.` (each way), `T&B` (top and bottom), `EF` (each face), `CONT.` continuous.
- Bar marks/lists: Bar list columns: Mark | No. | Size | Length | Type (straight/bent) | Bend dims (A-J) per ACI 315 standard bar types. Standard hooks: 90°, 135° (stirrups, seismic), 180°.
- Development length Ld, splice class (A/B) per ACI 318 shown in notes. Stirrup: `#3 @ 8" O.C.` with `1 @ 2", 8 @ 4"` spacing groups.
- Show: bar quantity, size, spacing, extent, cover, splice location, termination hooks, section cuts. Bar sizes in inch-pound soft-metric: #10 to #57.

### 7.3 Drawing conventions common to both
- Bars shown as thick single lines (bar) or dots (cross section). Dashed for hidden or lower layers. Bar mark in circle optional.
- Section markers on plan with beam/column mark; reinforcement section drawn with stirrups, main bars, cover, clear spacing, size. Column section: ties and corner bars.
- Slab: show top steel as thick line with hook and extent length, bottom as thick line with spacing. Openings: trimmer bars.
- Show construction joints, expansion joints, kickers, starter bars, lap zones, anchorages.

## 8. Structural drawing set (S-series, per NCS: 100 plans, 200 elevations, 300 sections, 500 details, 600 schedules)

| Sheet | Content |
|---|---|
| S-001 | General notes: codes, design loads, soil bearing, materials, cover, laps, hooks, concrete grades, steel grades, tolerances, test requirements, formwork removal times, abbreviations |
| S-002 | Typical details: lap lengths, bar bends, slab openings, chair/support, anchorage, expansion joint |
| S-101 | Foundation layout: footing marks (F1, F2), sizes, levels, column marks, tie beams, grade beams, blinding, excavation level, soil replacement, gridlines |
| S-102 | Ground floor slab/plinth beams, retaining walls |
| S-201.. | Floor framing plans per level: slab thickness, drops/depressions, beam marks (B1, B2), column markers, openings, cantilevers, sleeves, stair/lift cut-outs, sunken areas |
| S-2xx | Slab reinforcement plans (bottom/top per direction) |
| S-3xx | Beam elevations/sections (longitudinal + cross), column schedule, shear wall elevations |
| S-401 | Column layout with sections at each level |
| S-5xx | Details: stairs, lift pit/core, retaining walls, water tank, parapet, balcony, ramps, trench, openings |
| S-6xx | Schedules: column schedule, beam schedule, slab schedule, footing schedule, wall schedule, BBS |
| S-7xx | Roof plan, steel connection details, precast |

**Column schedule columns:** Mark | Level range | Size b x h | Longitudinal bars | Ties (dia @ spacing, extents) | Concrete grade | Remarks (lap, offset). Format: C1 | GF-3F | 300x600 | 8T20 | T10@150 | C35.
**Beam schedule:** Mark | Size | Top bars (support/mid) | Bottom bars | Stirrups (support/mid) | Side bars | Remarks.
**Footing schedule:** Mark | Plan size LxB | Depth | Bottom bars each way | Top bars | Column dowels.
**Slab schedule:** Mark | Thickness | Bottom rebar x/y | Top rebar | Cover | Remarks.

## 9. Coordination with architecture and MEP

| Topic | Rule |
|---|---|
| Beam vs wall | Beam width = wall thickness for hidden beams; column/beam edges flush with wall line or recessed 25-50 |
| Beam depth vs ceiling | Check clear height under beam: ceiling at beam soffit + void; beams along corridors may reduce depth: services pass under |
| Slab depressions | Wet areas (bath/kitchen/balcony) 50-150 [RoT]; confirm on both arch + struct, add waterproofing |
| Slab openings | All shafts, stairs, lift, ducts. Openings ≤ 300 can be cut by trimmer bars; > 300 detail trimmers; large openings near columns avoided |
| Beam web openings | Pipes through beams: sleeves in middle third of span, opening dia ≤ 0.25-0.33 D ⚠ verify, top/bottom chord ≥ D/3, spacing ≥ 2 x opening dia; no openings near supports; use sleeves cast in, coordinate with structural |
| Penetrations in columns/shear walls | Avoid; if needed detail |
| Sleeves schedule | MEP provides sizes/levels before shop drawings; structural shows sleeves on slab drawings; keep > 150 from slab edge/ column |
| Inserts/ embedded conduits | Conduit dia ≤ 1/3 slab depth; spacing ≥ 3 x dia; run outside tension zones (top/bottom) |
| Equipment loads | Chillers, generators, cooling towers, tanks, lifts, pools: get weights, footprints, anchor points |
| Equipment bases | Plinth 100-150 high with vibration isolation; separate from slab for vibration where needed |
| Roof | Slopes/drainage by structural fill or screed (min 1:100), parapet height |
| Fire rating | Cover/size per fire rating; sprayed/boarded steel |
| Waterproofing | Basements, tanks, roofs: details with arch |
| Services zone | Ceiling void = beam depth + 100-300; avoid deep downstand beams crossing corridors with main ducts |
| Lift | Pit depth, overrun, machine room loads, rail brackets per supplier |
| Stairs | Arch stair geometry (R, G) drives structure; landing beams |

## 10. Pre-issue checklist
- Code, loads, materials, cover stated; soil bearing stated with geotech report ref.
- Column grid matches latest arch; column positions consistent in all floors; no clashes with doors/parking.
- All levels (top of footing, top of slab, depressions) tied to arch levels.
- Slab openings and sleeves reflect latest MEP; trimmer bars.
- Beam/column/footing marks unique and scheduled; schedules match plans.
- Rebar callouts consistent (BS 8666 or ACI); lap, anchorage, hooks, cover noted; BBS provided if required.
- Stair, lift core, water tank, retaining wall details present.
- Expansion/construction joints placed and detailed.
- Deflection/crack/punching/lateral drift checked in model; foundation settlement considered.
- Drawing numbers, revisions, scales, title block, sheet index consistent.
