# MEP Drafting and Shop Drawings - Practice Reference

Scope: HOW MEP drawings are produced, checked and issued in consultancy and contractor offices (Gulf / Egypt / UK-style projects). Design rules (load calcs, duct sizing, pipe sizing, code limits) live in `mep.md`; do not repeat them here. This file is about drawing production: sheet types, drafting sequence, layers, coordination drawings, schedules, rejection patterns, automation.

Labels used throughout:
- **[CAPTION]** = taken from a course transcript (see section 8; one URL per claim where possible).
- **[RoT]** = rule of thumb from common office practice; not a code. Use as a starting point only.
- **[CODE]** = governed by a standard or authority; read the local edition.
- **⚠ verify** = I could not confirm it from a source in this session; check before relying on it.

---

## 1. Drawing types and level of development

### 1.1 The chain of drawings (who makes what)

```
Concept / schematic -> Design drawings (consultant) -> Tender set
        -> Shop drawings (contractor) -> Coordination / composite drawings
        -> Builder's work (BW) drawings -> Approved-for-construction (IFC) set
        -> Site install -> As-built drawings -> O&M manual / handover
```

A Gulf-based instructor describes the same chain: design drawings are converted by the contractor's draftsman into shop drawings per service; if the consultant rejects them they are revised and resubmitted; once coordinated and approved they flow into builder's-work drawings and then to site labour [CAPTION: https://www.youtube.com/watch?v=08g_YIKlNQg]. That matches the usual submittal flow (submit -> review -> A/B/C/D code -> resubmit).

### 1.2 What each type must show

| Type | Author | Purpose | Geometry level | Must show |
|---|---|---|---|---|
| Schematic / concept | Consultant | Agree system logic | Diagrammatic | Flow diagrams, single-line duct/pipe sketches, riser logic, plant room positions |
| Design (tender) drawings | Consultant | Price and permit | Single-line or simple double-line, schematic routing | Equipment positions, main routes, sizes, legends, schedules, notes, design basis. Does not fix exact elevations |
| IFC (Issued for Construction) | Consultant | Release build | As design, revised for approved comments | Revision-controlled; final sizes; stamped |
| Shop drawings | Contractor | Prove the contractor will build it to design intent with real products | Double-line, to scale, real fittings, elevations | Exact routes, true sizes incl. insulation, levels (BOD/BOT/invert), supports, vendor equipment dimensions, tags, sections, sleeves |
| Coordination / composite drawing | Contractor (lead sub) or BIM coordinator | Show all services in one space, remove clashes | Same as shop drawings overlaid, or 3D model | All trades in layers, elevation callouts at congested points, ceiling height, sign-off blocks per trade |
| Builder's work (BW) drawings | Contractor MEP | Tell civil/structure contractor where to leave openings, plinths, trenches, chases | 2D with dimensions to gridlines | Opening size, level (bottom/centre), sleeve type, plinth size/height, trench size, fire rating of penetration |
| Fabrication / spool drawings | Fabricator | Shop manufacture | Part-level | Duct pieces with gauge, joint type, flange; pipe spools with weld/fit numbers |
| As-built | Contractor | Record what was actually installed | Same as shop drawings, updated | Deviations, final levels, valve/damper/access door positions, tested values, red-line markup merged |

Rule: **an as-built set is shop drawings updated after installation, not design drawings re-labelled** [RoT; also stated in most Gulf contract specs ⚠ verify per contract].

### 1.3 LOD / detail by deliverable [RoT, loosely mapped to BIM LOD 200-500]

| Stage | Ducts | Pipes | Electrical | Notes |
|---|---|---|---|---|
| Design (LOD ~200) | Single line or approx. double line with size tags | Single line with size tags | Symbols at approximate positions, tray routes in single line | Sizes are design sizes, not inclusive of insulation |
| Shop (LOD ~350) | Double line to true external size (incl. lining/insulation shown), fittings (elbows, tees, reducers) | Double line for large pipes, single for small; valves, fittings, supports | Trays/conduits to scale, DB and equipment real size, circuit/cable tags | Elevations on every run; sleeve/opening tags |
| Fabrication (LOD ~400) | Piece numbers, joint types, gauges | Spool numbers, cut lengths | Not usual | Normally by fabricator or CAM software |
| As-built (LOD ~500 for record) | As installed | As installed | As installed + circuit tracing | Includes serial numbers and test data attachments |

### 1.4 Standard sheet content (every shop drawing)
- Title block: project, drawing title, level/zone, scale, discipline code, drawing number, revision table, drawn/checked/approved initials, submittal number.
- Key plan with zone/area boundary and north arrow.
- Legend and abbreviations (own sheet at the front of the set, `*-000`).
- General notes (materials, insulation, test pressures, code references).
- Match-lines to adjacent zones with the sheet number of the continuation.
- Section/elevation callouts keyed to detail sheets.
- Approval stamp area for consultant (Approved / Approved as noted / Revise and resubmit / Rejected) [RoT; wording varies].

---

## 2. Per-system drafting workflow (step by step)

General start (all trades) [RoT, consistent with 08g_YIKlNQg]:
1. Get the latest architectural + structural backgrounds and **xref** them (attach, not insert). Course trainers recommend that a referenced civil/architectural plan be dimmed (a grey colour such as index 8) so services stand out [CAPTION: https://www.youtube.com/watch?v=08g_YIKlNQg].
2. Bind nothing; keep xref path relative; one xref per discipline background (arch plan, arch RCP, structure, other MEP trades).
3. Set units, drawing scale, annotation scale, layer set, text/dim styles from the office template.
4. Draw services, then tags, then schedules, then sections, then sheet layout (viewports / layouts).
5. Self-check against the check list in section 6 before sending to checker.

### 2.1 HVAC ducting

Single line (SLD) vs double line (DLD) [CAPTION: 08g_YIKlNQg]: SLD is a flow/routing sketch (centre-line, size label, arrows); DLD is the true-width drawing used for shop and coordination. The trainer insists that SLD and DLD are not just drafting steps but a design-check: friction, velocity and CFM are reviewed while the routes are set.

Step order that matches the course workflow and typical office practice:
1. **Xref reference plan and ceiling plan** (diffuser positions follow the RCP grid).
2. **Place air terminals first** (diffusers, grilles) on the ceiling layout; centre in tile grid where possible [RoT].
3. **Place equipment** (AHU, FCU, VAV box, fans) to scale from the approved vendor catalogue; show service/withdrawal clearance as a dashed box [RoT].
4. **Draw the SLD** as a polyline from equipment to terminals; use polylines (one object per run) so that offsetting for DLD is one step [CAPTION: 08g_YIKlNQg - trainer states polyline = single entity, easier to offset to double line].
5. **Convert to DLD**: offset the centre-line by half the duct width each side (e.g., width 600 -> offset 300 both sides). The same video shows the offset-from-centre-line method; for ducts that share a trunk, draw the main duct, then branch, then clean the T-joint by trim [CAPTION: 08g_YIKlNQg].
6. **Reducers**: draw as concentric or eccentric transitions. The trainer teaches using standard width steps (300, 450, 600, 900) when reducing after take-offs, and notes the reducer position follows the last branch/supply [CAPTION: 08g_YIKlNQg]. Common practice is length of taper ~ 3-5 times the width change (or per SMACNA limit of 20 deg slope) [RoT ⚠ verify against SMACNA edition].
7. **Elbows**: use radius elbows (inner radius 0.5-1.0 x width) or square elbows with turning vanes; draw the vanes as hatch/line series [RoT].
8. **Flexible duct** drawn as zig-zag/two lines + cross-hatch, max length 1.5-2 m in most Gulf specs [RoT ⚠ verify spec]; the course draws a flexible connection from the trunk to a ceiling diffuser as a pink box (plenum box) to show it connects to the plenum [CAPTION: 08g_YIKlNQg].
9. **Dampers and accessories** as blocks on their own layers: VCD (volume control), FD (fire damper), SD (smoke), FSD (combined), MD (motorised), NRD (non-return). Fire dampers go wherever a duct crosses a fire-rated wall/floor; the instructor explains that smoke is the greater life risk so fire/smoke dampers are compulsory at rated barriers and are counted as accessories in the BOQ [CAPTION: 08g_YIKlNQg]. Drawing symbols and SLD vs DLD representation differ and must both be in the legend.
10. **Insulation**: draw as an outer offset (course uses 12 mm external; some teach 25 mm) on a separate insulation layer with a different linetype (dashed) and colour; this makes clash checks use true size [CAPTION: 08g_YIKlNQg]. Check thickness against spec rather than trusting the drawing default [⚠ verify spec].
11. **Tag every duct run**: size as WxH (width first, depth second) e.g. `600x300`, plus CFM/airflow in L/s on branches; tag every terminal with type, size and flow (e.g., `SD-1 600x600 150 L/s`) [RoT].
12. **Elevations**: label each run with BOD (bottom of duct) or BOT (bottom of tray/pipe). Common callout style: `BOD +3.10 AFFL`/`BOD +2.85` (relative to finished floor level) and spot `T.O.D.` for top. Changes of level shown with a "rise/drop" tag and a section [RoT].
13. **Sections**: cut at congested places (corridors, plant, risers); draw slab, beam soffit, ceiling, duct, pipe, light, sprinkler to scale and dimension FFL, ceiling and BOD. The trainer discusses the section view as how to understand layering and height from FFL through false ceiling to structural slab [CAPTION: 08g_YIKlNQg].
14. **Schedules** tied to tags: diffuser/grille schedule, duct fittings list (for BOQ), equipment schedule (see section 5).
15. **Plant room layout and riser diagram** last, after routes are fixed.

Layer set for HVAC includes: supply duct, return duct, fresh air, exhaust, kitchen exhaust, transfer air, terminals, equipment, accessories (dampers etc.), insulation, flex duct, text, dims [CAPTION: 08g_YIKlNQg lists these as a layer start set].

### 2.2 Chilled water / hot water / refrigerant piping
1. Start from the plant flow diagram (CHWS/CHWR); draw risers in the shaft position from arch.
2. Draw horizontal mains in single line on first pass, size tags (DN or inches), flow direction arrows, supply above/return below (convention shown in 08g: red above, green below at crossings) [CAPTION: 08g_YIKlNQg].
3. Show valve set at each equipment: isolating valves, strainer, balancing valve, control valve, unions, PT points; draw typical detail for FCU/AHU connection once and refer by tag [RoT].
4. Slope and air vents: high-point air vent, low-point drain; show on riser diagram [RoT].
5. Expansion loops/anchors/guides on long runs; supports spacing table on notes sheet [RoT].
6. Insulation line drawn outside pipe, with type/thickness in note [CAPTION: 08g_YIKlNQg on pipe insulation].
7. Draw the elevation (schematic) at the end: ladder diagram of risers with valve symbols and sizes. The course closes with elevation/schematic after plans [CAPTION: 08g_YIKlNQg].
8. Condensate drains: show slope (min ~1:100) to nearest floor drain or trap [RoT ⚠ verify].
9. Refrigerant (VRF/split): draw separate layer, show liquid and suction line sizes, branch kits, max length/height note per manufacturer [RoT ⚠ verify per VRF maker].

### 2.3 Plumbing water supply (isometrics and risers)
1. Mark fixtures from arch (WC, WHB, shower, kitchen sink, floor drain, hose bib) with fixture tag.
2. Draw the cold-water branch from the riser or stub-up to each fixture; hot-water parallel with different layer/linetype.
3. Number every riser (`CWR-1`, `HWR-2`) and show the ID on plan.
4. **Riser diagram** (vertical, not to scale): level lines for each floor, branch take-offs with isolating valves, PRV stations at set heights, fixture units/flow if the consultant requires, pipe sizes changing floor by floor [RoT].
5. **Isometric** of toilet cores or kitchen: 30-degree axes; show every fitting, valve, offset, and pipe size; this is what plumbers install from [RoT].
6. Add the plumbing legend (gate, ball, check, PRV, water meter, BFP, air vent, drain cock).
7. Tanks and pump room: plan + section + schematic with valve order (isolation - strainer - pump - NRV - isolation), and labelled level switches/float valves [RoT].

### 2.4 Drainage and vent
1. Draw sanitary stacks at positions agreed with arch (shafts/bulkheads) and label stack ID (`SS-1`, `VP-1`).
2. Branch lines from fixtures to stack as double or single lines depending on scale; show cleanouts at changes of direction and at stack base.
3. **Slope**: label every horizontal run with slope (`1:60` or `2%` for small bore; `1:100` for 100 mm and larger are common values - **[RoT ⚠ verify against local plumbing code]**). Slope along the path creates a vertical drop: a 20 m run at 1:100 drops 200 mm, which must fit in the ceiling void.
4. **Invert levels**: external drains use invert level (IL) at each manhole and a cover level (CL); depth = CL - IL. Draw a longitudinal profile for each run with chainage, ground line, pipe, IL in, IL out, gradient [RoT; common civil practice].
5. **Manholes (MH) and inspection chambers (IC)**: number them, show on plan, and add a schedule (ID, cover level, invert in/out, depth, size, type) - section 5.
6. Venting: draw vent stacks with connection point at least 150 mm above the flood-rim of the highest fixture before offset [RoT ⚠ verify code], terminate above roof; show air admittance valves only if allowed.
7. Floor drains with trap seal depth and trap-primer lines if specified.
8. Show pump sumps (sewage ejector) with duty/standby, high-level alarm, and rising main.
9. Check no sanitary pipes cross electrical rooms, kitchens (food) or above ceilings in sensitive areas without the engineer's approval [RoT].

### 2.5 Fire fighting (sprinkler, hose reel, hydrants)
1. Start from the approved hazard classification and the head spacing limits from the design; do **not** change them in shop drawings [CODE: NFPA 13 / BS EN 12845].
2. Place sprinkler heads on the **ceiling grid**: centred in tiles, at least a minimum distance from walls/lights/diffusers, and not further than the max coverage per head [CODE]. Course demonstrators show a "barray"/array lisp or block to distribute sprinklers along the grid quickly: https://www.youtube.com/watch?v=0v8nICC0zng [identified, not caption-mined].
3. Draw branch lines in a straight run connecting heads, cross-mains feeding the branches, and the main riser; maintain slope for drain-down on dry systems [RoT ⚠ verify].
4. **Pipe sizing**: either a *pipe schedule* approach (size by number of heads on a line - only for allowed hazard classes) or *hydraulic calculation* (size by pressure/flow). Shop drawings carry hydraulic node numbers and the calc sheet cross-references them [CODE].
5. Show **zone control valve assemblies** (isolating valve, flow switch, test and drain), per floor/zone, and tamper switches.
6. **Fire hose cabinets (FHC)** and hose reels: position near exits/staircases, label cabinet type (e.g., combined hose reel + extinguisher + landing valve). Draw the wet-riser/dry-riser route and landing valves per floor.
7. **Fire pump room**: plan + section + P&ID; label jockey/duty/standby pumps, test header, flow-test line, and tank connections.
8. Coordinate with ceiling: heads in the reflected ceiling plan; dropping to pendent with flexible drops (length limit per manufacturer).
9. Add the **hanger/support** spacing note and seismic bracing if required ⚠ verify.
10. Add pipe size tags, riser IDs (`FR-1`), valve symbols, and the fire legend. Civil-defence (Gulf) or fire-authority approval drawings may require their own title block ⚠ verify per country.

### 2.6 Electrical (lighting, power, DB schedules, SLD, containment)
Workflow used in a power-distribution shop drawing video: place the DBs/SMDB from the design, draw cable tray runs (200, 300 mm sizes) with dynamic blocks for straight runs and fittings, align each run to the white route line from the design drawing, and adjust to site coordination [CAPTION: https://www.youtube.com/watch?v=7QytwDVTiyk]. Combined steps:

1. Xref arch RCP; place luminaires from the schedule on the ceiling grid (symmetrical, centred); then emergency luminaires and exit signs on separate layers/colours.
2. Circuit lighting: draw switch legs and home-run tags (`L1/DB-GF/3`) [RoT].
3. Power: sockets at heights, equipment feeders (AC, pumps, fans), isolators next to equipment.
4. **DB schedule**: one per DB, columns: way no., circuit ID, description, protection (MCB rating, RCD/RCBO), cable size, load (W/VA), phase, phase totals and imbalance. Schedule is drawn on E-002 style sheets and cross-checked to loads on plans [RoT].
5. **Single-line diagram (SLD)**: structure top-down: utility/transformer -> MDB -> SMDB -> DB, each showing breaker size, cable size/type, busbar rating, metering, SPD, ATS/generator, UPS. A freehand tutorial using polylines and quadrant/midpoint snaps shows the drafting approach: build one reusable breaker symbol, copy, then add text [CAPTION: https://www.youtube.com/watch?v=asPzWqRAgRg - 690k views, basic commands only].
6. **Cable routing**: show tray/ladder/trunking/conduit with size tags (width x height) and route elevations (BOT). Mark vertical drops, risers (shaft ID), and fire stopping.
7. Containment segregation: power vs ELV/data; show min separation lines (e.g., 300 mm for power-ELV is a common spec, ⚠ verify spec).
8. Earthing and lightning: separate sheet with earth bar, pits, ring route, air terminals, down conductors, test points.
9. Generator/transformer rooms: plan + section + cable trench.
10. Keep a **load reconciliation**: DB schedule total = SLD feeder size basis = transformer sizing (details in `mep.md` section 3).

### 2.7 ELV / low current (CCTV, data, fire alarm, access, PA)
1. Each system on its own layers and its own sheet; same base RCP/xref.
2. Device symbols with ID tag (e.g., `CAM-12`, `AP-03`, `SD-045`), outlet type, mounting height, and cable type reference.
3. Cable containment: shared tray with power segregation barrier, or dedicated ELV tray; label routes.
4. **CCTV**: camera positions with view cone (FOV), lens type, mounting height, PoE switch location, NVR location, cable route to IDF; some courses show layout steps: https://www.youtube.com/watch?v=wdZgF1_PI3E [identified, not mined].
5. **Data/structured cabling**: outlets per room, patch panel/rack elevation, riser diagram showing backbone (fibre/Cat6A) between MDF/IDFs, 90 m channel limit for horizontal copper [CODE: TIA/ISO].
6. **Fire alarm**: detector spacing by ceiling height and type, MCPs at exits, sounders reaching required dB at bed head, loop or zone schematic, panel schedule, cause and effect matrix. Shop drawing for fire alarm (device layout, loop wiring) shown at https://www.youtube.com/watch?v=d3U1HhsUlsU [identified, not mined].
7. Riser diagram for each ELV system, always at the end of the set.
8. Show device-to-panel loop addresses where the contractor submits them.

### 2.8 BMS / controls
1. Start from the control schematic of each plant item (AHU, chiller plant, pump set, FCU) with points list: AI, AO, DI, DO.
2. Plan sheet shows controller panel positions (DDC, field panels), sensor locations (duct, room, outside air), actuators, and the network cabling topology.
3. Provide **I/O summary schedule** by panel and a **network riser diagram** (BACnet/Modbus backbone).
4. Add sequence-of-operation notes (not drawings only), alarm list and graphics schedule ⚠ often submitted as separate documents.
5. Interfaces with fire alarm (damper release, AHU shutdown), lifts, power meters, and generators are marked with cross-reference notes.

---

## 3. Layers, linetypes and symbols

### 3.1 Naming convention
The Gulf course trainer teaches a **D-S-E-T** idea: Department - Service - Element - Tag, written as `M-HVAC-SAD` style names (M = mechanical, HVAC = service, SAD = supply air duct, optional tag), noting that SMACNA-style names exist but the principle is consistency [CAPTION: 08g_YIKlNQg]. Note: the trainer attributes the scheme to SMACNA; this is more commonly described as part of AIA/NCS (US National CAD Standard) - **⚠ verify attribution** before citing.

Alternative: AIA/NCS pattern `M-HVAC-DUCT` etc.; UK uses BS 1192 / ISO 19650 naming, e.g., `M-HVAC-SUPPLY`. Choose one, document it in the template, and enforce with a layer-standards check (CAD standards, LAYTRANS).

### 3.2 Starter layer table (25+ layers) [RoT; colours are conventional ACI indices, not mandated]

| Layer | Content | ACI colour | Lineweight (mm) | Linetype |
|---|---|---|---|---|
| `0-XREF-ARCH` | arch plan xref | 8 (grey) | 0.09 | Continuous |
| `0-XREF-STRUC` | structure xref | 9 | 0.09 | Continuous |
| `0-XREF-RCP` | arch ceiling xref | 8 | 0.09 | Continuous |
| `M-HVAC-SAD` | supply air duct | 5 (blue) | 0.35 | Continuous |
| `M-HVAC-RAD` | return air duct | 3 (green) | 0.35 | Continuous |
| `M-HVAC-FAD` | fresh air duct | 4 (cyan) | 0.35 | Continuous |
| `M-HVAC-EAD` | exhaust air duct | 30 (orange) | 0.35 | Continuous |
| `M-HVAC-KEX` | kitchen exhaust | 6 (magenta) | 0.35 | Continuous |
| `M-HVAC-TRF` | transfer air | 140 | 0.25 | Continuous |
| `M-HVAC-FLEX` | flex duct | 5 | 0.18 | Continuous (zigzag block) |
| `M-HVAC-SCD` | supply ceiling diffuser | 5 | 0.18 | Continuous |
| `M-HVAC-RCG` | return ceiling grille | 3 | 0.18 | Continuous |
| `M-HVAC-ACC` | dampers, vanes, access doors | 30 | 0.25 | Continuous |
| `M-HVAC-INSL` | insulation line | 6 | 0.13 | DASHED |
| `M-HVAC-EQPT` | AHU/FCU/fans | 1 (red) | 0.50 | Continuous |
| `M-HVAC-CHWS` | chilled water supply | 4 | 0.35 | Continuous |
| `M-HVAC-CHWR` | chilled water return | 140 | 0.35 | Continuous (or HIDDEN) |
| `M-HVAC-CNDS` | condensate drain | 34 | 0.25 | DASHED |
| `P-DCW` | domestic cold water | 4 | 0.25 | Continuous |
| `P-DHW` | domestic hot water | 1 | 0.25 | DASHDOT or CONTINUOUS red |
| `P-SANR` | sanitary/soil | 34 (brown) | 0.35 | Continuous |
| `P-VENT` | vent | 34 | 0.25 | DASHED |
| `P-STRM` | storm/rain | 94 | 0.35 | Continuous |
| `P-FIXT` | fixtures | 7 | 0.18 | Continuous |
| `FP-SPRK-PIPE` | sprinkler pipe | 1 (red) | 0.50 | Continuous |
| `FP-SPRK-HEAD` | sprinkler heads | 1 | 0.25 | Continuous |
| `FP-HOSE` | hose reel/ landing valve | 1 | 0.35 | Continuous |
| `E-LITE` | luminaires | 2 (yellow) | 0.18 | Continuous |
| `E-LITE-EMER` | emergency lights | 1 | 0.18 | Continuous |
| `E-POWR` | sockets/power | 2 | 0.18 | Continuous |
| `E-TRAY` | cable tray | 2 | 0.35 | Continuous |
| `E-COND` | conduit | 2 | 0.25 | DASHED |
| `E-DB` | DB/panel blocks | 1 | 0.50 | Continuous |
| `E-ELV-CCTV` | CCTV | 6 | 0.18 | Continuous |
| `E-ELV-DATA` | data/telephone | 5 | 0.18 | Continuous |
| `E-FALM` | fire alarm devices | 1 | 0.25 | Continuous |
| `X-ANNO-TEXT` | text | 7 | 0.18 | Continuous |
| `X-ANNO-DIM` | dimensions | 3 | 0.13 | Continuous |
| `X-ANNO-TAG` | tags | 7 | 0.18 | Continuous |
| `X-SECT` | section marks | 7 | 0.25 | Continuous |
| `X-VPORT` | viewport frames (no-plot) | 7 | - | Continuous, Plot off |
| `X-CLASH` | clash/cloud markers | 1 | 0.35 | Continuous |

Colours: ducts blue, drainage brown, fire red, electrical yellow, ELV magenta are common office habits but **not** mandatory [RoT]. Xrefs go to colour 8 so the services stand out [CAPTION: 08g_YIKlNQg].

### 3.3 Linetypes for services [RoT]
- CONTINUOUS: ducts, supply pipes, drains (soil), sprinkler pipe.
- DASHED: vents, condensate, insulation outline, conduits, hidden items below.
- DASHDOT / CENTER: centre-lines of future/option routes and equipment axes.
- HIDDEN: items above/below plane (e.g., pipes above ceiling in a RCP).
- Phantom: equipment clearance zones.
- Always set `LTSCALE` and `PSLTSCALE` consistently; mismatched scales make dashed layers look continuous and cause rejection comments about unclear systems.

### 3.4 Symbol legend minimum list
See `mep.md` section 5 for the full symbol list. Practical addition: the legend must show **both** SLD and DLD symbol versions for dampers and accessories [CAPTION: 08g_YIKlNQg]; include a "to be installed by others / existing" convention; and state which symbol standard is used (IEC 60617, ANSI/IEEE 315, NFPA 170).

---

## 4. Coordination (drawings and rules for the drafting side)

Design coordination rules and clearances are in `mep.md` section 6. Production-side practice:

### 4.1 Combined services drawing (CSD)
1. Each trade submits its shop drawing as an xref set with layers named per the BIM execution plan or CSD protocol.
2. The coordinator (usually the mechanical contractor or BIM team) stacks all trades, sets the **ceiling height** requirement from arch RCP, and marks conflicts with revision clouds.
3. Prepare **coordination sections** at all congested zones (corridors, shaft entry, plant room exits).
4. Each trade signs off the CSD (stamp/initial block per trade) before it is released as "approved for installation" [RoT].
5. Output: floor-by-floor CSD plans + composite sections + a clash log (ID, location, trades, resolution, owner, date).

### 4.2 Clash resolution priority (who moves)
Typical rule order in office practice [RoT; matches `mep.md` section 6 priority list]:
1. Structure and architectural fixed points.
2. Gravity drainage (cannot rise).
3. Large ducts and air-handling items (hard to reroute).
4. Sprinkler mains (hydraulic design fixed).
5. Chilled water and other pressure pipes (can offset).
6. Cable tray / busway.
7. Conduit, ELV, small pipes.
8. Flexible items last.

### 4.3 Drafting-level clearances [RoT; verify against spec]
- 50 mm minimum clear gap between insulated services (some specs 100 mm).
- 150 mm minimum above ceiling for hanger tolerance.
- Access zones in front of valves, dampers, FCUs: 450-600 mm [RoT ⚠ verify].
- Electrical panel front clearance 1 m, rear as per manufacturer [CODE ⚠ verify].
- Ceiling-void budget (typical office): ceiling tile 25 + light fitting 150 + duct 400 + insulation 50 + hanger gap 150 + structure beam 600 = 1375 mm (illustration) [RoT]. The point: draft this stack in a coordination section **before** finalising duct sizes.

### 4.4 Builder's work (BW) openings
1. For each service passing through a wall, slab or beam, put a **sleeve/opening tag** (`BW-M-001`) on the shop drawing.
2. Schedule: tag, system, size (W x H or dia), level (bottom or centre) relative to FFL, wall/slab type, fire rating, sleeve type, submitted date, structure approval status.
3. Openings through beams and slabs need the structural engineer's approval; show positions dimensioned to gridlines [RoT; link to `structural.md`].
4. Equipment plinths: size, height, anchor bolts, drainage trench for chillers/pumps; trenches for cables; wall chases.
5. The course trainer describes BW drawings as the stage after approved coordination, merged with civil and MEP, then issued to site workers in portions [CAPTION: 08g_YIKlNQg].

### 4.5 Reference tracking
- Always include a **revision cloud + triangle with letter** on changed items, revision table at sheet corner.
- Use a transmittal register; tie every sheet to a submittal number.

---

## 5. Schedules and BOQ extraction

### 5.1 Schedules each discipline produces
| Discipline | Schedules |
|---|---|
| HVAC | Equipment (AHU, FCU, VAV, fans, chillers, pumps), diffuser/grille, damper, duct accessories, insulation, valve, controls |
| Plumbing | Fixtures, pumps, tanks, valves, water heaters, MH/IC schedule, sleeves |
| Drainage | MH/IC (ID, CL, IL in, IL out, depth, type, size), pipe run schedule (from/to, dia, length, slope) |
| Fire | Sprinkler heads (type, K-factor, temp), valves, FHC schedule, pump data, hydraulic node table |
| Electrical | DB schedules, luminaire schedule, cable schedule, tray/containment schedule, load schedule, SLD data |
| ELV | Device schedule (ID, type, location), rack schedule, cable schedule |
| BW | Openings/sleeves, plinths, trenches |

### 5.2 Extraction methods [RoT]
1. **Block attribute extraction** (`EATTEXT` in AutoCAD): attach attributes (TAG, TYPE, SIZE, FLOW) to blocks; export to Excel; build the schedule table on the drawing. Works for diffusers, sprinklers, lights, devices.
2. **Data link / fields**: link table to Excel, update after revisions (`DATALINK`).
3. **Length of polylines**: use `LIST`, `DATAEXTRACTION`, or `LISP` to total pipe/duct lengths by layer; duct area = perimeter x length (so use polyline widths and sizes in attributes).
4. **Duct areas for insulation and fabrication**: perimeter (2 x (W+H)) x length; count fittings separately and add fitting factors per local practice ⚠ verify.
5. **Count blocks by layer** with `COUNT` or `QSELECT` for quick takeoffs.
6. **BIM**: Revit schedules (duct/pipe/fitting/accessory schedules) with filters by system; export CSV/XLSX [see section 7].
7. Reconcile quantities against the tender BOQ; report variations (above ±5% flagged to QS) [RoT].

### 5.3 Typical BOQ lines to ensure the drawing supports
Ductwork (m2 by size range, GI gauge), duct insulation (m2), fittings count, dampers (nr by type and size), diffusers (nr by size), pipes (m by dia and material), pipe insulation (m), valves (nr by type/size), supports (kg or nr), sleeves (nr), cable tray (m by width), cable (m by size), DBs (nr), luminaires (nr by type), heads (nr), FHC (nr), fire alarm devices (nr).

---

## 6. Common consultant rejection comments (Gulf / Egypt style)

Comments below are patterns seen across typical review stamps (Rejected / Revise & Resubmit). Treat as a pre-submission checklist [RoT; compiled from office practice and the shop-drawing workflow described in 08g_YIKlNQg; no single source lists them].

**General**
1. Drawing not coordinated with other services; clashes visible; provide combined services drawing.
2. Wrong or outdated architectural/structural background; not matching latest IFC.
3. Missing legend, abbreviations, scale bar, north arrow, revision table.
4. Drawings not to scale / viewport scales inconsistent.
5. Tags missing or inconsistent with schedules.
6. Approved material submittal not referenced / equipment model differs from approved.
7. Different symbol used than in the legend or the tender drawings.
8. Missing section/elevation at congested points; no levels (BOD/BOT) on runs.
9. Sleeve/opening locations not shown or not approved by structure.
10. Not matching specification (duct gauge, insulation thickness, pipe class).
11. Comments of the previous revision not addressed or not tracked in a comment-response sheet.

**HVAC**
12. Duct size/airflow differs from design without calculation.
13. Fire/smoke dampers missing at rated walls or not shown with access.
14. No access doors at dampers, fire dampers, coils, VAV.
15. Flexible duct too long or at inappropriate locations.
16. Diffusers not centred on the ceiling grid; mismatch with the RCP.
17. Missing insulation and vapor barrier detail; insulation not shown in clash.
18. Condensate drain slope or trap missing; drain routed to unapproved point.
19. Chilled-water valve set (strainer, balancing, isolation) missing at FCU/AHU.
20. Not enough clear height above corridor ceiling; provide section.

**Plumbing / drainage**
21. Slope not indicated or insufficient; pipe above ceiling shows no fall.
22. Cleanouts missing at stack base and changes of direction.
23. Vent pipe termination or connection not shown; venting system incomplete.
24. Invert levels or manhole schedule missing; levels discontinuous between runs.
25. Water supply riser diagram missing valves / PRV / meters.
26. Wet pipes above electrical rooms or elevator shafts.

**Fire**
27. Sprinkler spacing exceeds allowable; coverage areas not met; heads obstructed by ducts/lights/beams.
28. Hydraulic calc not submitted or not matching pipe sizes.
29. Zone valves/flow switches missing; drain points not shown.
30. Hose cabinets / extinguishers not per approved authority drawings (civil defence).

**Electrical / ELV**
31. DB schedule incomplete (ratings, cable size, spare ways, phase balance).
32. SLD does not match the plans (breaker/cable mismatch).
33. Containment sizing and fill not shown; segregation of power and ELV missing.
34. Luminaire type or lux level not per schedule; emergency/exit not shown.
35. Earthing/lightning not coordinated with structure (rebar, foundations).
36. Fire alarm: detector spacing, MCP positions, loop capacity or cause-and-effect not consistent with civil-defence comments.

**As-built**
37. Deviations not marked; valve/damper tags not updated; levels not recorded.
38. Test and commissioning certificates not attached.

---

## 7. Automation and tooling

### 7.1 AutoCAD / AutoCAD MEP
- **Use a template** with layers, linetypes, text/dim styles, plot styles (CTB/STB) and layouts; do not draw on a blank file.
- **Xref + layer-state manager**: save layer states per drawing type (HVAC-only, Combined) to switch quickly.
- **Dynamic blocks** for diffusers, dampers, cable tray runs/fittings (the power-distribution shop drawing video uses dynamic tray blocks to place and align runs rapidly) [CAPTION: https://www.youtube.com/watch?v=7QytwDVTiyk].
- **Block attributes** for tag/type/size so schedules extract directly.
- **Polylines and `OFFSET`** for ducts: course workflow uses polyline centre-line -> offset ½ width each side; check `FILLETRAD`/chamfer for elbows [CAPTION: 08g_YIKlNQg].
- **`MEASURE`/`DIVIDE`** to place diffusers or flex symbols at regular intervals (the course uses `MEASURE` with a named block) [CAPTION: 08g_YIKlNQg].
- **Lisp / scripts**: duct generator lisp (https://www.youtube.com/watch?v=oO_KjDFOwSA - Arabic, 87k views, identified not mined), sprinkler array/distribution lisp (https://www.youtube.com/watch?v=0v8nICC0zng, identified not mined). Common wins: auto-offset ducts, auto-tag sizes, lengths-by-layer totals, batch plot.
- **AutoCAD MEP**: use duct/pipe/cable-tray tools with "system definitions" and part catalogues; produce 3D, auto-section, schedules and tags; layers via layer key styles. Cautions: MEP objects need proxy-graphics handling when sent to non-MEP users (use `EXPORTTOAUTOCAD`/bind) [RoT ⚠ verify].
- **AutoCAD Electrical**: for control schematics (PLC, MCC) rather than building lighting/power plans; do not use for building-wide shop drawings [RoT].
- **PDF-to-DWG**: always rebuild; never trust traced old drawings.
- **Plot**: layout viewports locked, scale set, plot-style table applied, PDF publish via `PUBLISH` with a sheet set.

### 7.2 Revit MEP
- Model by system type, with views/filters per discipline and **view templates** for plan, RCP, section and 3D.
- Shop drawing set-up covers duct/pipe tagging and annotation: see https://www.youtube.com/watch?v=TtaawOpyRyE (HVAC shop drawing setup and tagging in Revit; identified, not mined).
- Use **worksets** per discipline; **linked models** for arch/structure; **shared coordinates** with the architect's file.
- Use **parameters** for BOD, system abbreviation, sleeve ID; schedules read them for BW and BOQ.
- Use **Interference Check** or **Navisworks** clash tests with a saved clash matrix (e.g., Duct vs Structure, Pipe vs Duct, Tray vs Pipe).
- Typical full courses: Revit MEP complete: https://www.youtube.com/watch?v=i3Wp3XGQE60 (10h; identified, not mined).

### 7.3 Dynamo / scripting [RoT]
- **Dynamo**: auto-number sleeves, copy parameters from linked arch rooms to spaces, place sleeves at duct-wall intersections, batch-export sheets to PDF/DWG, check missing tags.
- **Python / AutoLISP / .NET**: extract block attributes to CSV; validate layer names against the standard; check text height consistency.
- **Excel + CSV**: keep the master equipment list in Excel; drive schedules and tags from it (single source of truth).
- **Plugins / third-party**: CAD-Duct, Autodesk Fabrication CADmep/ESTmep for detailed duct/pipe and takeoff; use for fabrication-level shop drawings [RoT; mentioned by search results of an accredited course on CAD DUCT].

### 7.4 Quality control
- Run a CAD-standards checker (`STANDARDS`) and `PURGE`/`AUDIT` before issue.
- Run a clash report and attach to the submittal.
- Peer-check: a second person marks each system's lines with a highlighter on the printout (physical or PDF markup) and the drafter clears each markup [RoT].

---

## 8. Sources

Caption-mined (captions retrieved and searched for workflow statements):
- https://www.youtube.com/watch?v=08g_YIKlNQg - SM Techno MEP Training Services, "HVAC DRAFTING - COMPLETE" (7h08, ~64k views). Used for: shop-drawing flow, SLD/DLD, layer naming, xref colour, reducers, insulation, flex ducts, dampers, BW drawings, sections.
- https://www.youtube.com/watch?v=UF67vY5-7RU - MEP Engineering Tutorials, "HVAC system complete designing" (6h46, ~163k views). Mostly design/sizing; only used to confirm that sizing happens before drafting.
- https://www.youtube.com/watch?v=7QytwDVTiyk - AutoCAD & Revit Tools, "Electrical Plan for Power Distribution in AutoCAD / Power Cable Tray Distribution" (17 min, ~20k views). Used for: electrical power shop drawing from design drawing, dynamic cable-tray blocks.
- https://www.youtube.com/watch?v=asPzWqRAgRg - CAD CAM Tutorials, "AutoCAD Single Line Diagram Drawing Tutorial for Electrical Engineers" (35 min, ~690k views). Used for: SLD drafting mechanics.

Identified (title/metadata only; **not** caption-mined because YouTube returned HTTP 429 after the first pulls; treat statements citing them as pointers, not verified content):
- https://www.youtube.com/watch?v=62xH7IpWbJs - PTS CAD Expert, Complete AutoCAD MEP (hotel), 4h22.
- https://www.youtube.com/watch?v=i3Wp3XGQE60 - PTS CAD Expert, Complete Revit MEP, 10h14.
- https://www.youtube.com/watch?v=3NAXCTKOWWY and https://www.youtube.com/watch?v=g4EtnlyBx68 - Engosoft Global (Arabic), mechanical/HVAC shop drawing, ~3h48 each.
- https://www.youtube.com/watch?v=FAoxd9TuGrM - LEARN&EARN (Arabic), shop drawings, 58 min, ~224k views.
- https://www.youtube.com/watch?v=aDQmFpNrHXw and https://www.youtube.com/watch?v=EmVE3GVOli4 - Ibrahim Abd El Mohsen El Gohary (Arabic), duct drawing.
- https://www.youtube.com/watch?v=oO_KjDFOwSA - Droos MEP (Arabic), duct lisp.
- https://www.youtube.com/watch?v=EYEMGkhYe_c - MEPCADGURU, Drainage layout plan.
- https://www.youtube.com/watch?v=s5ztKI0wmd0 - Drawings Solution1, Fire fighting plan.
- https://www.youtube.com/watch?v=0v8nICC0zng - MEP WORK, Sprinkler distribution with lisp.
- https://www.youtube.com/watch?v=d3U1HhsUlsU - AutoCAD & Revit Tools, Fire alarm shop drawing.
- https://www.youtube.com/watch?v=zU1GgUEKgt0 - AutoCAD & Revit Tools, Lighting and DB schedules shop drawing.
- https://www.youtube.com/watch?v=wdZgF1_PI3E - CAD Coach Aman, CCTV layout.
- https://www.youtube.com/watch?v=TtaawOpyRyE - BIM Information Lab, HVAC shop drawing in Revit.
- https://www.youtube.com/watch?v=ERhQSpw1BWY and https://www.youtube.com/watch?v=QuMBAwgf218 - Arabic fire fighting tutorials.

Honest limitation: Arabic captions were not retrieved (auto-captions for the Arabic videos were unavailable or rate-limited), so Egyptian/Gulf-Arabic practice here comes from the English-language Gulf trainer plus general office knowledge. Items labelled [RoT] or ⚠ verify should be checked against the project specification, local authority requirements and current editions of SMACNA, NFPA, BS EN and local plumbing code before use.
