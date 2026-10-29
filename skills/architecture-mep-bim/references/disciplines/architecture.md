# Architecture - Method Reference

Tags: **[RoT]** = rule of thumb (typical range, not a code value; confirm with brief/client/local code). **[CODE]** = number is jurisdiction-specific, take from the country file. **⚠ verify** = not independently confirmed. All dimensions mm unless stated. Imperial in brackets where useful.

## 1. Design sequence (always in this order)

| Step | Output | Notes |
|---|---|---|
| 1. Brief | Room list + areas + adjacency wishes + budget + storeys + parking + style | If missing, ask: plot size, occupants, storeys, orientation, special rooms |
| 2. Site/regulation check | Setbacks, coverage, FAR, height, parking ratio, fire access [CODE] | Compute buildable envelope first |
| 3. Zoning / bubble diagram | Public / semi-private / private / service zones, entrance, orientation | No dimensions yet; show adjacency lines (strong / weak / avoid) |
| 4. Block plan | Footprint inside envelope, structural grid proposal, core/stair/shaft positions | Agree grid with structural at this step |
| 5. Space plan | Rooms sized from the area schedule, walls placed on grid | Check against sections 3-4 below |
| 6. Circulation + egress | Corridors, stairs, lifts, exit distances [CODE] | Dead-end and travel limits [CODE] |
| 7. Vertical design | Floor-to-floor, ceiling heights, slab/beam/services zones, stair geometry | Coordinate with structural + MEP depth |
| 8. Envelope | Wall types, openings, shading, parapets, roof | Hot climate: minimise west glazing, add shading, insulation [CODE energy] |
| 9. Drawings + schedules | Section 10 set list | Dimension, tag, schedule, cross-reference |
| 10. Coordination + check | Section 11 checklist | Run before issue |

## 2. Zoning and adjacency

Adjacency matrix convention: **A** = must be adjacent, **N** = near, **S** = separated/buffered, **X** = avoid.

| Pair | Relation | Reason |
|---|---|---|
| Entrance - living/reception | A | Arrival sequence |
| Kitchen - dining | A | Service |
| Kitchen - utility/laundry/store | A | Plumbing shared wet wall |
| Kitchen - garage/service door | N | Grocery route |
| Bedrooms - bathrooms | A (en-suite for master) | Privacy, shared wet wall |
| Bedrooms - living/guest/entertaining | S | Noise |
| Guest/majlis - family area | S (separate entry, own WC) | Gulf privacy norm |
| Bathroom/kitchen/laundry | Stack vertically (same shaft/wall) | Cuts MEP risers, leak risk |
| Stair - entrance | N | Egress |
| Plant/electrical room - bedrooms | X | Noise, heat |
| Lift shaft - bedroom wall | X | Noise |
| Toilets - dining/kitchen door | X (no direct view) | Hygiene, privacy |
| Office meeting rooms - open plan | N | Acoustics: add lobby/sound lock |
| Server/comms room - wet areas | X | Water leak risk |

Zoning rules [RoT]:
- Orientation (northern hemisphere hot climate): living/bedrooms to N/NE views; service rooms (stairs, WC, store, kitchen) on W/SW as thermal buffer; keep glazing on W minimal. Reverse in southern hemisphere; cold climates favour south glazing.
- Cluster wet areas: back-to-back or one stack per 2-4 bathrooms.
- Entrance sequence: gate - drive - porch - lobby - zones; avoid seeing the toilet/bedrooms from the entrance.
- Mark north arrow on every plan.

## 3. Typical room sizes [RoT] (clear internal area; check client brief and [CODE] minimums)

| Room | m² | ft² | Min clear width m |
|---|---|---|---|
| Master bedroom | 14-20 | 150-215 | 3.3-3.6 |
| Bedroom (standard) | 10-14 | 110-150 | 2.9-3.2 |
| Child/guest bedroom | 9-12 | 100-130 | 2.7-3.0 |
| Maid's / driver room | 7-9 | 75-100 | 2.4 |
| En-suite bathroom | 4.5-7 | 48-75 | 1.5-1.8 |
| Common bathroom | 3.5-5 | 38-55 | 1.5 |
| WC (powder room) | 1.5-2.5 | 16-27 | 0.9-1.0 |
| Living room | 18-35 | 190-375 | 3.6-4.5 |
| Majlis (Gulf, per gender) | 25-60 | 270-650 | 4.5-6 |
| Dining | 12-20 | 130-215 | 3.0-3.5 |
| Kitchen (family) | 9-16 | 95-170 | 2.4 (galley), 3.0 (U/island) |
| Dirty/prep kitchen | 5-8 | 55-85 | 2.0 |
| Laundry/utility | 3-6 | 32-65 | 1.5-1.8 |
| Store | 2-5 | 20-55 | 1.2 |
| Walk-in wardrobe | 4-8 | 43-85 | 1.8 |
| Entrance lobby | 4-9 | 43-97 | 1.8 |
| Car space (each, covered) | 12.5-15 | 135-160 | 2.5-3.0 x 5.0-5.5 |
| Single office (private) | 9-14 | 100-150 | 2.7 |
| Open-plan desk | 8-12 per person gross | 85-130 | - |
| Meeting room | 1.5-2.0 per seat | 16-22 | - |
| Pantry | 6-12 | 65-130 | - |

Fixture clearances [RoT]: WC centre 400-450 from side wall, 600 clear in front (min 500 tight); basin 550-650 wide, 700 clear front; shower tray min 800x800 (comfortable 900x900 to 900x1200); bath 1600-1800 x 700-800; kitchen work triangle legs 1.2-2.7 m, sum 4-7 m; counter depth 600, height 850-900; clear aisle between counters 1000-1200; bed 1.0-1.2 (single), 1.5-1.8 (double/king 1.8-2.0) wide + 700-900 access each side.

## 4. Circulation

| Element | Residential [RoT] | Office/commercial [RoT] | Note |
|---|---|---|---|
| Corridor clear width | 900-1200 | 1500-2400 | [CODE] min by occupant load |
| Entrance door clear | 900-1000 | 1000-1200 pair | Accessible: 800+ clear [CODE] |
| Internal door leaf | 800-900 | 900-1000 | Bath/WC 700-800 |
| Stair width | 900-1200 | 1200-1500+ | [CODE] by occupant load |
| Lift (passenger) | 8 persons ~1100x1400 car | 13-21 persons ~1400x1600 to 2000x1500 | Pit/overrun per supplier |
| Hospital bed lift | - | 1200x2300 car, 1300+ wide door | |
| Ramp (accessible) | 1:12 max common, 1:20 preferred | same | [CODE] |
| Turning circle wheelchair | 1500 dia | 1500-1800 | |

- Circulation share [RoT]: villa 10-15% of GFA; apartment unit 8-12%; office 15-20% (net-to-gross 80-85%); hotel 25-35%.
- Dead-end corridor, travel distance to exit, number of exits [CODE].
- Apartment blocks: single-loaded corridor (open side, lower efficiency, good light), double-loaded (efficient, typical corridor 1.5-2.0), point/tower core (units around core). Lift count by traffic calc - quick screen [RoT]: 1 lift per ~50-100 units residential, 1 per ~2500-4000 m² office net, at least 2 above 5-6 storeys incl. one service/fire lift [CODE] ⚠ verify.

## 5. Wall types and thicknesses

Nominal finished thickness = core + plaster/finish both faces. Plaster 12-20 each side typical (Gulf 20). Verify local block sizes; sizes vary by country.

| Type | Core | Finished | Imperial | Typical use |
|---|---|---|---|---|
| Hollow concrete block (Gulf/ME) | 100 / 150 / 200 / 250 | +40 (20 plaster x2) | 4" / 6" / 8" / 10" CMU (actual 3-5/8", 5-5/8", 7-5/8") | 200 external, 100-150 internal |
| Solid block / dense CMU | 100-200 | +30-40 | same | Boundary wall, load-bearing |
| AAC (aerated) block | 100 / 150 / 200 / 250 | +20-30 (thin plaster) | - | Light weight, thermal ~0.1-0.15 W/mK ⚠ verify per maker |
| Clay brick, solid (UK 215x102.5x65) | 102.5 (half brick), 215 (one brick) | +30 | 4" / 8-3/4" | Facing, load-bearing |
| Cavity wall (UK) | 100 brick + 50-100 cavity/insulation + 100 block | 275-325 | ~11"-13" | External, thermal [CODE] |
| Brick veneer + stud (US) | 90 brick + 25 air gap + 140 stud (2x6) + 16 gyp | ~290 | 3-1/2" + 1" + 5-1/2" + 5/8" | External |
| Egyptian red brick | 120 / 250 | +30-40 | - | Typical loadbearing/infill (25 cm = 2 bricks) ⚠ verify |
| Drywall partition (light) | 70 stud + 2x12.5 board each side | ~120 | 2-1/2" stud + 5/8" gyp | Interior, 1 hr typical with 2 layers each side ⚠ verify rating by test |
| Drywall (wet/tall) | 92-150 stud + 2x12.5 each side | 140-200 | 3-5/8" - 6" stud | Shafts, tall rooms, acoustic (insulation fill) |
| Wood stud (US residential) | 2x4 (89) / 2x6 (140) | 100-110 / 150-160 incl. gyp | 3-1/2" / 5-1/2" | Interior / exterior |
| RC wall | 150-300 | +30 | 6"-12" | Core, basement, shear wall |
| Curtain wall (unitised/stick) | Mullion 50 wide x 100-250 deep | 100-250 depth | - | Glass facade; spans between slabs, anchored at slab edge |
| Glass partition | 10-12 tempered/laminated + frame | 50-100 | - | Offices |

- Partition heights: stop below slab for non-rated; fire/acoustic partitions run slab to slab [CODE].
- Lintels over openings: bearing 150-200 each side, depth 150-200 for openings up to ~1.5 m; beyond that coordinate with structural.
- Parapet height [RoT]: roof 300-1100; balcony/terrace guard 1000-1100 min [CODE]; guard openings < 100 sphere [CODE].
- Thermal/insulation, U-values [CODE]. Hot climate: external wall = block + XPS/PUR 25-50 + block or ETICS/ external insulation + render.
- Wall hatch conventions: concrete (diagonal + dots), block (cross-hatch or solid grey), brick (diagonal), insulation (squiggle), drywall (parallel lines or fill with stud symbols in detail).

## 6. Vertical dimensions [RoT]

| Item | Residential | Office | Retail/Public |
|---|---|---|---|
| Floor-to-floor | 3.0-3.4 (villa 3.2-3.5) | 3.6-4.2 | 4.5-6.0 |
| Finished ceiling height | 2.6-2.8 (min 2.4 [CODE]) | 2.7-3.0 | 3.0-4.0+ |
| Slab + beam depth | 0.2-0.5 | 0.3-0.8 | 0.4-0.8 |
| Floor finish build-up | 50-100 (screed+tile) | 50-150 (raised floor 100-300) | 50-100 |
| Services/false ceiling void | 200-500 | 500-800 | 600-1000 |
| Door height | 2100-2400 | 2100-2400 | 2100-2700 |
| Window sill | 900-1000 (bed/living), 1000-1100 kitchen over counter, 1500-1800 WC/bath high | 800-900 or full height | - |
| Window head | 2100-2400 (align with door head) | to ceiling | - |

Rule: floor-to-floor = clear ceiling + void + structure + finish. Typical office 3.9 = 2.7 clear + 0.7 services/ceiling + 0.35 slab/beam + 0.15 finish. Set slab edge/step levels: Bathroom/wet areas recessed 50-100 or raised threshold; balcony 20-50 below interior (Gulf: 50-150) ⚠ verify; internal level changes and threshold details drawn in section.

## 7. Stairs design method

Variables: R = riser, G = going (tread), N = number of risers, H = floor-to-floor height (finished to finished).

1. N = H / R_target (R_target 150-175 residential, 150-170 public); round N to whole number.
2. R = H / N (must be equal for all risers; first and last riser adjusted for finish thicknesses).
3. G from the Blondel formula **2R + G = 600-640** (630 comfortable) [RoT-classic]; check G within 250-300 residential, 280-300+ public.
4. Check [CODE] limits (typical: R ≤ 180-190 public / ≤ 196 US dwelling; G ≥ 250-280). Common reference: IBC (US) max riser 7 in (178 mm)/min tread 11 in (279 mm) general, 7-3/4 in (196)/10 in (254) one/two-family dwellings ⚠ verify edition; UK AD K private stair max R 220 / min G 220 with pitch ≤ 42° ⚠ verify.
5. Treads per flight = N - 1 per flight (landing counts as the top step). Flight run = (N_flight - 1) x G.
6. Headroom: min 2000-2200 clear measured vertically from pitch line [CODE]; check at landings and soffit of upper flight.
7. Width: [CODE] by occupancy; handrails both sides above ~1100 width; handrail height 900-1000 (US 865-965); guard 1000-1100 [CODE].
8. Landings: depth >= stair width; intermediate landing required after ~12-18 risers [RoT, CODE max vertical rise between landings e.g. US 3.66 m].
9. Nosing: 15-30 overhang; slip-resistant strip; contrast.
10. Stair types and footprint [RoT]: straight - length (N-1)xG; dog-leg (U) ~ 2 x flight + landing, width ~ 2x stair width + 100-200 gap; L-shape with quarter landing; winders only in villa private stairs [CODE]; spiral - secondary only [CODE].
11. Worked example: H = 3200, R target 165 -> N = 19.4 -> N = 19, R = 168.4; G = 630 - 2x168.4 = 293 -> use 290. Two flights 9 + 10 risers (dog-leg): flight 1 run 8x290 = 2320, flight 2 run 9x290 = 2610; landing 1200 -> core length ~ 2610 + 1200 + wall = ~4100.
12. Fire stairs: enclosed, rated door, no storage, pressurisation [CODE]; exit discharge to outside at ground.
13. Draw: plan with UP/DN arrow and cut line (break line at 1 m above floor), N risers numbered, section showing riser/tread/headroom, handrail detail.

Ramp: slope 1:12 to 1:20; run = rise x 12; max rise per run 750 with level landings 1200+ [CODE]. Car ramp: 1:8 - 1:6 ⚠ [CODE], with transitions; see civil-site.md.

## 8. Wet areas

- Floor fall to drain 1:100 - 1:50 (10-20 mm/m), inside shower 1:50; waterproofing membrane under screed turned up 150-300 at walls (full height in shower); test (flood test 24-48 h) before tiling.
- Slab recess/drop for wet areas 50-100 (Gulf/Egypt practice), shown on arch + structural drawings.
- Floor drain 100x100 grate in each bathroom/kitchen/laundry/balcony; WC drains ahead of shower in plan for 100 mm pipe, discharge to shaft.
- Plumbing shaft/duct 600x600 to 800x1000 typical per stack group; access panel; shaft continues through all floors with fire-stopping at slabs.
- Tile height: 2100-2400 wet wall; splashback 450-600 kitchen; skirting 80-100.
- Ventilation: openable window or mechanical extract (10-15 ACH [RoT], 25 L/s per fixture [RoT] ⚠ verify) - see mep.md.
- Show on plan: WC, basin, shower/bath, drains, hot water cylinder location, WC cistern type (concealed requires 120-150 wall frame).

## 9. Building-type specifics

### Villa / single-family
- Parts: porch/entry, majlis (Gulf, with separate WC and entrance), family living, dining, kitchen + dirty kitchen, laundry, store, bedrooms (master + en-suite + wardrobe), maid's room + WC, driver room, guard room, parking/carport, roof stair headroom/pergola, roof water tank location, external AC condensers on roof or service court.
- Stacking: GF public/service, FF bedrooms, roof utilities. Stair near entrance/central; 1 lift optional (provide shaft in 2-storey luxury villas).
- Plot ratios, setbacks, coverage, boundary wall height (1.8-2.4 [CODE]), gate widths (single 1.0, car 3.5-5.0, double 5-6), driveway 3.0-3.5 single.
- Show in plan: boundary, setback dimensions, gates, ramp/driveway slopes, landscaping zones, septic/manhole if no sewer, meter room location per utility.

### Apartment building
- Unit mix & areas [RoT]: studio 30-45, 1BR 55-80, 2BR 85-120, 3BR 120-170 m² (Gulf/ME).
- Depth of unit 8-12 m for natural light/cross vent; balconies 1.5-2.0 deep; AC condenser ledge/service balcony; service ducts shared.
- Core: stair x2 (separation [CODE]), lifts, riser shafts, refuse chute/room, fire lobby/smoke vent, electrical/ELV room per floor.
- Basement: parking (ramp, columns on 7.5-8.4 bay grid fitting 3 x 2.5-2.7 bays), plant, tanks; ventilation shafts; fire pump room.
- Typical structure grid 4-6 m in residential; align walls on columns; avoid transfer beams where possible.

### Office
- Floor plate: depth window-to-core 9-13.5 m for natural light [RoT]; planning grid 1.2-1.5 module (1.5 more common in ME); structural grid 7.5-9 m.
- Core: lifts, stairs x2, toilets (counts [CODE], ~1 WC/25 females, 1 per 40 males approx; ⚠ verify), pantry, riser room, electrical/IT closets, janitor.
- Toilet fixtures per [CODE]; accessible toilet per floor.
- Ceiling: grid 600x600 / 1200x600, light/AC/sprinkler/detector module layout (reflected ceiling plan).
- Raised floor optional 150-300 in IT-heavy areas; carpet tile; acoustic partitions.
- Net-to-gross 80-85%; area per person 8-12 m² NIA [RoT].
- Facade: curtain wall with spandrel + vision glass, solar shading, U-value/SHGC [CODE energy].

## 10. Architectural drawing set (A-series, based on US NCS sheet numbering; adapt to client/country)

| Sheet | Content | Typical scale |
|---|---|---|
| A-000 / G-series | Cover, drawing index, abbreviations, symbols, general notes, area statement, project data | n/a |
| A-001 | Site/location plan, key plan | 1:200-1:500 |
| A-100 series | Floor plans: basement, GF, typical, roof; furniture/layout plans; reflected ceiling plans (RCP); finishes plans; fire plans | 1:100 (1:50 small) |
| A-200 series | Elevations: all four + street elevation; material call-outs, levels | 1:100 (1:50) |
| A-300 series | Building sections (min 2: through stair and through wet areas) + wall sections | 1:100 / 1:50 |
| A-400 series | Enlarged plans: toilets, kitchens, stair cores, lift lobbies, typical rooms | 1:50, 1:20 |
| A-500 series | Details: wall sections, window/door heads/sills, thresholds, roof edges, parapet, expansion joints, stair details, balustrade, waterproofing | 1:20, 1:10, 1:5, 1:2, 1:1 |
| A-600 series | Schedules: door, window, finishes, ironmongery, sanitary | tabular |
| A-700 | Vertical circulation: stair sections, ramp, lift details | 1:50 |
| A-900 | 3D views, renders (optional) | n/a |

Scale imperial equivalents: 1:100 ~ 1/8"=1'-0"; 1:50 ~ 1/4"=1'-0"; 1:20 ~ 1/2"or 3/4"; 1:10 ~ 1-1/2"; 1:5 ~ 3".

### Plan content (each floor plan)
- Grid lines + bubbles, 3 dimension chains (overall, grid-to-grid, openings/walls), room names + numbers + areas, levels (FFL, SSL), door/window tags, stair UP/DN, section/elevation/detail markers, north arrow, finish tags, fire-rated wall marking, shaft hatching, slab edge/drop lines (dashed), equipment (AC, tanks), furniture (living, kitchen, bath fixtures), match lines.
- Plan cut at 1000-1500 above floor; show elements below as thin lines, above as dashed.
- Roof plan: slopes with arrow + %, drains, parapet, tank, stair headroom, AC units, skylight, access hatch, ridge/valley.

### Elevation content
- Finished ground level, FFL of each floor, parapet top, openings, materials/colour callouts, expansion/control joints, shading, signage, ladders, louvres, AC grilles, downpipes, gate/fence. Show grid lines at ends.

### Section content
- Cut line through stair, shaft, level change. Show levels (FFL, ceiling, roof, foundation top), floor-to-floor and ceiling heights, structure outline (slab/beam), floor build-up, ceiling void, wall types, parapet, roof layers, insulation, wall-to-slab connections, stair, lift shaft.

### Detail contents
- Wall section (foundation to parapet): plinth/DPC (150-300 above ground), ground floor slab, DPM, window head/sill, lintel, slab edge, waterproofing, parapet coping, roof build-up with slope screed (min 1:80-1:100 falls [RoT]), upstand 150-300, gutter.
- Window: frame fixing, sill slope, drip, sealant, flashing.
- Door: threshold, ironmongery, frame fixing, fire seal.
- Expansion joint: cover plate/gap width 20-50 [RoT], fire-rated sealant, waterproof.

## 11. Schedules

**Door schedule columns:** Mark | Location/room | Type (hinged/sliding/double/rolling) | Leaf width x height x thickness | Frame (material, finish) | Leaf material/finish | Fire rating (min) | Glazing | Hardware set (lock, closer, hinges, panic bar) | Swing/hand | Threshold | Remarks (accessible, acoustic). Clear opening = leaf - frame rebates (e.g., 900 leaf -> ~820-850 clear). Mark scheme: D1,D2 or by type + frame code.
**Window schedule:** Mark | Type (fixed/casement/sliding/tilt-turn/louvre) | Width x Height | Sill height | Frame material/colour | Glass type (single 6, double 6-12-6, low-E, laminated, tempered where < 800 AFFL or near doors) | Openable area % [CODE] | Screens/shutters | U-value/SHGC [CODE] | Remarks.
**Finish schedule:** Room no. | Name | Floor | Skirting | Walls (N/S/E/W) | Ceiling | Ceiling height | Remarks.
**Room data / area schedule:** each room area + total GFA, NFA, covered/uncovered areas, coverage %, FAR [CODE definitions vary].

## 12. Reflected ceiling plan (RCP)
- Ceiling type, heights, grid, bulkheads, light fittings (type tag), diffusers/grilles, sprinkler heads, smoke detectors, speakers, access panels, curtain boxes, exit signs. Layout of lights, AC, sprinklers, detectors must not clash: centre in tiles, keep >= 600 between detector and diffuser ⚠ verify, detectors >= 500 from walls/obstructions [CODE].

## 13. Accessibility (principles; numbers [CODE])
Step-free route from site boundary/parking to entrance; accessible toilet; door clear widths; maneuvering clearances (1500 turning circle, 900 clear beside door pull side); lifts to all floors; tactile paving; ramp rise limits; handrails 850-950 both sides; reception counter dual height; accessible parking near entrance.

## 14. Coordination with other disciplines
- With structure: columns/beam depths vs ceiling height; walls on beams; shaft sizes; slab drops in wet areas; stair/lift core walls; cantilevers; parapet details; expansion joints; roof loads (tanks, pools, planters) — provide loads/positions early.
- With MEP: shaft sizes and locations per floor stacked; plant room sizes; AC condenser space; ceiling heights vs duct depth; ceiling grid vs light/AC/sprinkler layout; access panels; riser fire-stopping; equipment louvre locations; transformer/gen set room access and ventilation; tank room location.
- With civil: levels (FFL vs road), driveway slope, drainage outfall, utility connection points, retaining walls, ramp geometry, setbacks.
- With fire: compartment lines, rated walls/doors, exit signage, stair pressurisation, firefighting lift, fire access, travel distance.

## 15. Pre-issue checklist
- Grid + dimensions closed (sum of chains = overall); doors/windows tagged and in schedules; room areas computed; levels consistent plan/section/elevation.
- Stairs: R equal, headroom OK, handrails; ramps slope labelled.
- Wet areas: falls, drains, drop slabs, waterproofing noted; stacked.
- Exits: number, widths, travel distance, dead-ends checked [CODE].
- Fire-rated walls/doors marked; shaft closures.
- North arrow, scale bar, title block, revision, drawing number, sheet index match.
- Elevations match plans (openings aligned, floor heights).
- Sections cut through stairs and key level changes.
- Materials and finish schedule consistent with details.
- Area statement vs setbacks/coverage/FAR/parking [CODE].
- Structure and MEP overlays checked for clashes (columns in rooms/doors, shafts, beams over openings).
