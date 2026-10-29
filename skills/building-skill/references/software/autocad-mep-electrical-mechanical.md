# AutoCAD MEP, AutoCAD Electrical, AutoCAD Mechanical - professional practice

These are three **different products/toolsets on the AutoCAD engine**, each with its own project model, content database and report engine. Beginners (and AIs) treat them as "AutoCAD with symbols" and draw plain lines; the value is in the data (tags, connectors, systems, BOM). Always verify the exact command/ribbon name in the installed version (Autodesk renames items between releases); prefer UI-named workflows below over guessed command aliases.

| Product | Domain | Native model | Key data store | Typical output |
|---|---|---|---|---|
| AutoCAD MEP toolset (also Architecture toolset for backgrounds) | Building HVAC, plumbing, electrical power, fire | Project-based 3D "AEC objects" with connectors | Style Manager, Part Catalog (`.apc`/content DB), property sets | Plans, sections, schedule tables, MEP coordination DWG |
| AutoCAD Electrical toolset | Control/panel/schematic design | Project (`.wdp`) of schematic + panel DWGs | Catalog database (component part numbers), symbol library | Ladder diagrams, panel layouts, wire/BOM reports, PLC I/O |
| AutoCAD Mechanical toolset | Part/assembly 2D drafting | Mechanical Structure + Part References | Standards (AMOPTIONS), standard-parts content, layer standard (`AM_*`) | Detail/assembly drawings with BOM, balloons, GD&T |

If the installed AutoCAD is vanilla/LT, none of these libraries exist; fall back to plain-AutoCAD blocks + attributes + `DATAEXTRACTION` (see `autocad.md`). New work in building design is usually done in **Revit MEP** (see `revit.md`); use AutoCAD MEP when the client mandates DWG, for retrofit, or for 2D coordination.

---
# PART A - AutoCAD MEP

## A1. Project architecture (do not skip)
- Work inside a **Project** (Project Browser / Project Navigator): folders `Constructs` (building floors, MEP systems), `Elements` (typical rooms/stacks), `Views` (composed views: plans, sections), `Sheets` (layouts). Constructs are xref'd into Views; sheets reference Views. Opening random DWGs outside the project breaks cross-file references.
- **Levels & Divisions**: define Levels (floor elevations + floor-to-floor) in the project, assign Constructs to levels. Without levels, elevation data, section cuts and schedules are wrong.
- Architect background = xref (attached from architect's project or plain DWG with `INSUNITS` matching). Set a **common origin** and units (mm vs m) before drawing a single duct.
- Keep **one construct per system/discipline per level** (e.g. `L01-HVAC-SUPPLY`, `L01-PLUMB-DOMESTIC`) to allow independent display control and clash isolation.
- Drawing Setup: units (mm / m), scale, default layer standard (AIA/BS1192/ISO13567). Layer-key styles (Layer Key Styles in Style Manager) auto-assign layers by object type, e.g. `Duct-Supply -> M-HVAC-SUPPLY`. Do not hand-recolour duct layers; change the layer key.

## A2. Systems (the heart of AutoCAD MEP)
| System type | Typical definitions | What it controls |
|---|---|---|
| Duct systems | Supply Air, Return Air, Exhaust, Outside Air, Smoke Extract | Layer key, flow direction, sizing criteria, display colour, equipment connectivity |
| Pipe systems | Chilled Water Supply/Return, Hot Water, Domestic Cold/Hot, Sanitary Waste, Vent, Storm, Fire (Wet/Dry) | Slope for gravity systems, insulation, label styles |
| Electrical | Power, Lighting, Fire alarm, Low-voltage/data | Circuits, panel assignment, conduit/cable-tray |
- **Define systems before routing**: Style Manager > MEP Systems > Duct/Pipe System Definitions. Assign system to each run; *routing from an equipment connector inherits the system*.
- **Connectors**: parts expose connectors (supply/return/ducting/pipe/cable). Always connect parts to connectors (not just overlap visually); disconnected = no flow data, no sizing, no schedule quantity. Use *Add Duct/Pipe* from a connector grip or *Connect to* tools; verify by "Show Connections / System Analysis".
- **Slope (gravity)**: sanitary/drain pipes: typical 1:50 (2 %) for <=DN100, 1:100 for larger (check local plumbing code, e.g. BS EN 12056, IPC/UPC 1/4 in per ft); route from fixtures to stack with continuous fall and no reverse slope (set slope on pipe style, not by dragging endpoints).
- **Vent / trap rules**: vent stack required; maintain trap seal; cleanouts at changes of direction.

## A3. Parts, catalogs, content
- Parts are catalog-driven (size/shape/connection). Place with **Parts Catalog / Content Browser** items, not drawn lines. Typical sets: rectangular/round/oval duct, flex, plumbing pipe (copper, PPR, PVC, cast iron, steel), valves/fittings, VAV boxes, AHUs, FCUs, diffusers, fixtures, panels, conduits.
- Custom parts: create via **Content Builder**/MvPart tools; define MEP connectors with dimensions and flow; store in a *company* catalog, not in the install folder.
- **Routing preferences** (duct/pipe styles): set preferred fittings (elbow 90 mitered/radius, tee type, transition), min straight length, offsets. Poor preferences = ugly 45-degree spaghetti and wrong pressure drop.
- Sizing a part by typing width/height numbers is the beginner mistake - use sizing tools (Duct/Pipe Size) driven by criteria below, then update schedules.
- Insulation/lining: attach insulation spec to duct/pipe style so the clearance in clash checks includes it.

## A4. Sizing - rules of thumb (verify against project criteria/ASHRAE/CIBSE/local code)
| Item | Criteria | Notes |
|---|---|---|
| Low-velocity supply main | 5-8 m/s (1000-1600 fpm) | Offices ~6 m/s max for noise |
| Branch to terminal | 2.5-4 m/s | Near occupant: lower |
| Return/exhaust main | 4-7 m/s | |
| Friction (equal-friction method) | 0.8-1.0 Pa/m (~0.1 in.wg/100 ft) | Typical comfort HVAC |
| Pipe - chilled/hot water | 1.0-2.4 m/s; 100-400 Pa/m | Smaller pipe: lower velocity (noise, erosion) |
| Pipe - domestic cold | 0.9-2.4 m/s | Hot: ~1.5 m/s to avoid erosion |
| Condensate | 1:100 slope min | |
| Duct flow | CFM = (Q) / L/s = area x velocity; round equivalent diameter De = 1.3 (ab)^0.625/(a+b)^0.25 | Convert rectangular <-> round with this |
- Use MEP **Duct Sizing Calculator** / **Pipe Sizing Tools**: choose method (equal friction, velocity, static regain), set targets, apply to selected system, then re-check flow rates on terminals (Space load -> CFM). Heat loads come from HAP/Carrier/Revit/Excel; AutoCAD MEP does not compute them.

## A5. Spaces, schedules, tags
- Create **Spaces** (room objects with load/area/volume/occupancy) from architectural walls/boundaries; assign space type for ventilation rates.
- Schedule Tables: Schedule Table Styles (e.g. "Duct Takeoff", "Equipment Schedule", "Fixture Schedule") fed by **Property Set Definitions**. Property sets carry manual and automatic properties; if a property doesn't appear in a schedule, it isn't in the attached property set.
- Tags: Annotation tags attached to objects reference property sets; update by `Update Schedule`/ refresh; do not type over tag text.
- Export schedules to CSV/Excel; re-link to quantity takeoff. Use consistent unit display (mm/m, L/s) in styles.

## A6. Coordination and drawing production
- Coordinate with architect and structure via xref/link; **run clash**: use Navisworks (export NWC) or AutoCAD's `INTERFERE` for 3D solids; AutoCAD MEP has clash detection tools (Interference Detection) - run per level before issuing.
- **Display representations**: Plan (single-line), Plan High Detail (double line), Model (3D) - configured per View; use *Single-line* for coordination at 1:100, *double-line* at 1:50 and below.
- Mark up: section views generated from the 3D model using Building Section/Elevation Line objects; Sheets via Project Navigator -> Sheet Set Manager.
- Keep Z (elevation) correct: assign "Elevation" in the object property for each run (e.g. `+2850 mm AFF`); mixed elevation = false clash results.

---
# PART B - AutoCAD Electrical

## B1. Project model
- Create a **Project** with the Project Manager (`.wdp` plus `.wdt` tag-list data). All schematic and panel drawings must be **added to the project** and have the **same project settings** (Project Properties > Drawing Format) before inserting components. Opening a loose DWG and inserting symbols with the wrong standard is the classic failure.
- Per-project settings: **Standards**: *IEC* (IEC 60617, ladder with line references), *JIC* (US, NFPA 79 / JIC EMP, symbols styled ANSI), *IEC-60617*, *NFPA*, *JIS* (Japan), *GB* (China), *AS* (Australia) - set in Project Properties > Drawing Format > "Symbol Library / Standard". Do not mix IEC and JIC symbols; wire colours, contact numbering (13-14 vs numbered rungs) and pushbutton shapes differ.
- **Drawing Properties**: sheet number, section, ladder reference, description lines (title block attribute links). Title blocks use `WD_M`-type attribute blocks; map project descriptions with "Title Block Update".
- **Component tagging format** (Project > Properties > Components): default `%F%N` (family letter + sequential number, e.g. `K12`, `M3`) plus optional `%S` sheet and `%D` drawing (`%S%D` -> sheet-based `=A+B-K12` location/installation codes). Define once, apply project-wide. Wire tags: `L1`, `N`, `PE`, or sequential `%N` and reference-based `%X..` styles.
- Line reference numbers (IEC: `%S/%L`): ladder reference arrow and cross-referencing generate automatically from rung positions; changing ladder spacing later renumbers everything - **set ladder spacing/rung height first**.

## B2. Schematic drawing workflow
1. **Insert Ladder** (1-phase / 3-phase, rung spacing, rail width, rung count). Power rails labelled (L1/L2/L3, 24VDC, 0V). Fixed pitch required; never draw rungs manually.
2. **Insert Component** (Icon menu / Catalog): pick symbol (pushbutton, contactor coil, relay, overload, motor, PLC), assign **catalog part number** (manufacturer, catalog, assembly code) from the catalog DB so BOM auto-builds. Insert-on-wire to auto-break wires.
3. **Circuit Builder** (Motor starter, VFD, three-phase) inserts pre-wired circuits from Excel spreadsheet templates - use for repeated motor feeders.
4. **Wires**: `Wire` command snaps to connection points; use wire types/colors (layers `RED`, `BLU`, `WIRE-24VDC`...). Cross-wire links via **Signal Arrows** and **Source/Destination** markers (`Signal Arrows` = cross-sheet continuity). Never end a wire in empty space - dangling wires create phantom connections.
5. **Parent/child components**: coil is parent (`K12`), contacts are children; contacts inherit tag and show cross-references (e.g. `/12.4` or "Contact Map"). **Never type a tag**; always edit through the tag dialog so cross-references update.
6. **Wire numbering** (Project > Wire Numbers): methods - **Sequential** (continuous numbering across sheet), **Reference-based** (rung/line reference + position, e.g. `3-1`), **By tag/terminal** (`wire follows terminal name`). Apply after the circuit is final; use *Fixed* numbers for field changes. Leave "Same potential" ties so jumpers keep one number. Re-run per drawing, then "Update".
7. **Terminals**: use Terminal symbols with tag strips (`X1:1`...). Use **Terminal Strip Editor** to sort, jumper, add accessories; reports for terminal plan.
8. **PLC**: Insert **PLC (Parametric)** for generic rack modules or *PLC database* for vendor modules (Rockwell/Siemens/Mitsubishi); I/O points get addresses (`I:0/01` or `%I0.0`) and descriptions; **Spreadsheet to PLC I/O** import to auto-create the I/O drawing from an Excel I/O list; cross-reference between PLC channel and field device. Keep one I/O list as source of truth.
9. **Error check** (Project > Drawing Audit / Electrical Audit): duplicate tags, unconnected wires, missing catalog numbers, orphaned cross-references. Run before reports.
10. **Panel Layout**: from schematic list, `Insert Footprint` (Panel footprint library, to scale) from catalog; assign Panel/Enclosure; auto-link between schematic tag and footprint (same catalog number & tag). Mounting-plate cutouts, wire duct, DIN rail added from content library. Use real manufacturer dimensions (catalog DB), not guessed rectangles.

## B3. Reports (outputs the customer actually reads)
| Report | Use | Notes |
|---|---|---|
| Bill of Materials (BOM), Component, Missing BOM | Purchasing | Requires catalog part numbers; "Missing Catalog" shows gaps |
| Wire From/To | Panel builders | Run **after** numbering; includes length if panel layout used |
| Terminal Strip / Terminal Plan | Installers | Per strip, from jumpers/wire |
| PLC I/O Address and Descriptions, PLC Module Usage | Programmers | Spare channels flagged |
| Cable Summary / Connector Plug | Harness | Ensure cable tags |
| Schematic -> Panel Mismatch (Component Compare) | QA | |
| Export to Excel / Access | Hand-over | Template mapping in `Project > Reports` |
- Pro practice: run reports into the project folder `REPORTS/`, regenerate at each issue, never hand-edit the exported file (re-run overwrites); keep revision stamped title.

## B4. Symbol libraries - IEC vs JIC/NFPA (practical differences)
| Aspect | IEC / IEC 60617 | JIC / NFPA 79 / ANSI |
|---|---|---|
| Layout | Vertical or horizontal, columns with line references | Horizontal ladder, numbered rungs (1,2,3) |
| Contact numbering | 13-14 (NO), 21-22 (NC), A1/A2 coils, 95-96 OL | Wire numbers; contacts not pin-numbered |
| Wire colours | Standards like IEC 60204-1 (black power, blue neutral, green/yellow PE, red control AC, orange foreign voltage) | NFPA 79 (black power, red AC control, blue DC control, white neutral) |
| Terminals | `X1:1` / `=A+B-X1:1` full designation | `TB1-1` |
| Overload | Thermal relay with `95-96` aux | Heater element symbol |
| Pushbutton | Circle with mechanism lines | Circle (for NO), flat bar NC, mushroom |
| Motor | `M` circle with `3~` | `M` with `3PH` |
Use only one library per project; to migrate, use the toolset's symbol-swap/update utilities rather than manual redraw (check Help for the exact tool in your version). Custom symbols: create DWG block with `WD_M` attribute set via **Icon Menu Wizard / Symbol Builder** so they keep tag/attribute behaviour.

## B5. Electrical ordering of work
Standards/project -> ladder -> power circuits -> control -> PLC I/O -> terminals -> catalog numbers -> wire numbers -> audit -> panel layout -> reports -> title block revision -> plot set (`Plot Project`).

---
# PART C - AutoCAD Mechanical

## C1. Standards and drawing setup
- Choose **one drafting standard** at start (Options `AMOPTIONS` > Standards): **ISO** (international), **ANSI** (US, inch), **DIN** (Germany, ISO-compatible with DIN specifics), **JIS** (Japan), **GB** (China), plus **BSI**, **CSN**, **GOST** in the toolset. Standard drives: line types/weights per layer, dimension style, text height, hatch patterns, symbol standard, title block, fastener libraries and tolerance tables.
- Drafting standard also determines **projection method**: ISO/DIN/JIS/GB = **first-angle** projection; ANSI = **third-angle**. Mixing is a common review rejection. Put the projection symbol in the title block.
- Sheet formats: A0-A4 (ISO) / A-E (ANSI). Scale per view with the *Scale Representation/Scale Viewports* tools; text sizes remain correct via the standard.
- **Layers**: AutoCAD Mechanical manages a layer standard (`AM_0` visible, hidden, center, section, dimension... layers with defined colour/lineweight). Use *Layer Manager* and the "Layer Standard" tools; do not create ad hoc layers for contour/hidden/center lines, because hide management, hole charts, balloons and BOM rely on them.
- **Units**: millimetre for ISO/DIN/JIS/GB, inch for ANSI. Draw 1:1 in model space, scale in views/layout (same philosophy as plain AutoCAD).

## C2. Structure and part references (what makes BOM work)
- **Mechanical Structure** (browser): a hierarchy of Assemblies -> Sub-assemblies -> Components. Create components via *Create Component* from drawn geometry; define as *Part* or *Standard part* with Part Reference (`Part Ref`) tying geometry to BOM data. Geometry not part-referenced is invisible to BOM.
- **Part Reference**: add Part ID (drawing number), Description, Material, Qty, Weight; stored in drawing database; may be edited in *Structure Table*.
- **Assembly drawing process**: insert/xref each component DWG (or define parts in the same DWG) -> structure list -> BOM generated automatically; update by `Update BOM`.
- **Balloons / Part References**: Place balloons only after parts are referenced; balloon numbers link to BOM rows and renumber on BOM re-sort (*Renumber balloons*). Use item numbers sequential left-to-right/clockwise; leader never crossing; same style across sheets.
- **BOM**: `BOM` table style per standard (columns: Item, Qty, Part No., Description, Material, Mass, Remarks). Place on drawing, link to title block; export to CSV/Excel. Titles/sort/auto-update. **Hand-typed BOM rows** break integrity.

## C3. Dimensioning, tolerance, GD&T
- **Power Dimensioning** (`AMPOWERDIM`): single command creates linear/angular/radius/diameter/chain/baseline dimensions with automatic style and auto-placement, and edit via *Power Edit* (double-click). Handles tolerance (symmetric, deviation, limits, fits `H7/g6` ISO 286), arrows, text prefix/suffix, ordinate dimension. Prefer over raw `DIMLINEAR`; do not mix Power Dimension and associative standard dimension in the same view (inconsistent look).
- **Auto-dimensioning**: not always desirable; dimension for manufacturing/functions (datum features first, mating surfaces, then overall), avoid duplicate/chain closure; one dimension only once.
- **Tolerances**: general tolerance note ISO 2768-mK in title block; critical fits explicit (e.g. bearing seat `50 H7`, shaft `50 k6`). Provide surface finish via **Surface Texture** symbol (ISO 1302 / ASME Y14.36: Ra) and welding symbols (ISO 2553 / AWS A2.4).
- **GD&T**: Feature Control Frame (ASME Y14.5 or ISO 1101): symbol, tolerance value (diameter modifier), modifier (M/L), datum references `A|B|C` in order; **Datum Identifier**; **Datum Target**; basic dimension box. Datum features must be on actual surface features, not centrelines unless axis datums intended. Rule: no GD&T without datum reference frame for position/profile.
- **Hole charts / tables**: for plates with many holes use *Hole Chart* (tag holes `A1`, `B2`, table of X/Y/dia). **Revision table** and **Title block** via Drawing Properties attributes.

## C4. Standard parts, features, calculations
- **Content Manager / Standard Parts**: fasteners (ISO 4762, DIN 933/931, ASME B18), washers, nuts, pins, bearings, keys (DIN 6885), seals, O-rings, rivets; drop in with hide management (hidden lines resolved automatically), size from hole/thread. Use library rather than drawing screws.
- **Features**: chamfers, holes (through/blind/counterbore/countersink), threads (ISO metric `M10`, UNC), keyways, undercuts (DIN 509, DIN 76); thread representation by standard (thin line 3/4 circle in end view).
- **Shaft Generator** and calculations (springs, cams, gears via Machinery Handbook-like tools): use for shaft/bearing layouts; verify numbers independently - tools give drawing support, not certification.
- **Hide management**: automatic hidden-line removal between overlapping parts via *Hide Management* on layer pairs; reorder with *Move to Front/Back*; never erase hidden lines manually.
- **Views**: Orthographic via *Create View* (front/top/side) with base view then Projection; Sections via *Create section*; Details via *Detail view*; breakouts; auxiliary views; use section hatching with standard patterns (ISO 128: 45 degrees, different spacing/angle for adjacent parts).
- **Notes/BOM linking** to ERP: export XML/CSV with Part IDs consistent with PLM.

## C5. Mechanical drawing QA checklist
1. Correct standard (ISO/ANSI), projection symbol, units, scale, sheet size.
2. Views sufficient (min necessary), correct hidden/center lines, section hatching consistent.
3. Full dimensioning, no duplicates, no missing dimensions; tolerances/fits stated; GD&T datum frame complete.
4. Weld/surface texture/thread notes; material, heat treatment, finish notes.
5. Part references, balloons, BOM synced; revision table; title block complete (drawing no., rev, material, mass, scale, tolerance note, projection).
6. Run `AUDIT`, `PURGE`, check layers (`AM_*` only), plot to PDF at 1:1, review.

---
# Programmatic access (all three)
| Route | Reality |
|---|---|
| ezdxf | Can read/write DXF produced by MEP/Electrical/Mechanical, but **custom AEC/AM objects are proxy/ACAD_PROXY** - geometry only, data lost. Use for plain 2D schematics, not for tag-linked projects |
| AutoLISP / .NET | Electrical exposes an AutoLISP API (`ace_*` helper functions documented in its Help "AutoLISP API" section) for tagging, wire numbers, and project access; Mechanical ships `am*` LISP/ARX functions and its commands are `AM`-prefixed; MEP/Architecture objects have a .NET object model (`Autodesk.Aec.*` assemblies). Confirm names in the Autodesk developer docs for the exact installed version before coding against them. |
| Script (.scr) | Works for batch plot/purge/audit of project DWGs. Activate the project first in Electrical; in headless `accoreconsole` the toolset ARX modules are not loaded - use full AutoCAD with `/product` + toolset profile |
| Excel/CSV bridges | Electrical: **Spreadsheet to PLC I/O**, **Circuit Builder** Excel, BOM export; Mechanical: BOM export; MEP: schedule export. These are the safest automation points - generate the spreadsheet in Python (openpyxl), let the toolset build the drawings |
| MCP | Generic AutoCAD MCP servers (see `autocad.md`) draw primitives and P&ID symbols; they do **not** create MEP systems, Electrical tags or Mechanical part references. Use them only for plain-geometry fallback |

# Spreadsheet bridge (safest automation point for Electrical/MEP/Mechanical)
Generate the data in Python, let the toolset build or validate drawings. Example: PLC I/O list that the Electrical "Spreadsheet to PLC I/O" command can import (confirm required column headers in Help for your version; keep them in the first row).
```python
from openpyxl import Workbook
wb = Workbook(); ws = wb.active; ws.title = "PLC_IO"
ws.append(["RACK", "SLOT", "POINT", "ADDRESS", "DESC1", "DESC2", "TYPE"])
rows = [(0, 1, 0, "I:1/00", "START PB", "PUMP P101", "DI"),
        (0, 1, 1, "I:1/01", "STOP PB",  "PUMP P101", "DI"),
        (0, 2, 0, "O:2/00", "RUN LAMP", "PUMP P101", "DO")]
for r in rows: ws.append(r)
wb.save("plc_io.xlsx")
```
Validate before import: unique addresses, no spare channel overwritten, every field device has a tag; after import run the Electrical audit and the PLC I/O report and diff against the source sheet.

MEP equivalent: read a schedule export (CSV) with `csv.DictReader` and check airflow totals per system (sum of terminal L/s = AHU supply L/s within 5-10 %), duct velocity <= criteria, pipe slope >= minimum, no unconnected parts. Mechanical equivalent: parse BOM CSV and check Item numbers contiguous, every balloon item exists, mass > 0.

# Worked sequences (what a pro does, in order)
| Task | MEP | Electrical | Mechanical |
|---|---|---|---|
| 1 | New project, levels, units, layer standard | New project, set standard (IEC/JIC), tag format, wire-number style | Set standard (AMOPTIONS), units, sheet, projection |
| 2 | Xref architect plan, set origin, create spaces | Title block, ladder, rung spacing | Draw base views 1:1, assign layers by standard |
| 3 | Place equipment, connect connectors, define systems | Insert components with catalog numbers, parent/child | Create components, part references, standard parts |
| 4 | Route mains then branches, apply sizing, set elevations | Wire, signal arrows, terminals, PLC I/O | Power dimensioning, tolerances, GD&T, notes |
| 5 | Tags, schedules, clash check | Wire numbers, audit | BOM, balloons, title block, revision |
| 6 | Sections, sheets, plot | Panel layout, reports, plot project | Plot PDF, verify 1:1, release |

# Review questions an experienced reviewer asks
- MEP: is every run connected and assigned to the right system? Do schedule totals equal source loads? Is elevation set (AFF/AFFL stated)? Are clearances for insulation, access and service space shown? Are penetrations through fire-rated walls/floors flagged? Is flow direction shown on plans? Do gravity drains fall continuously?
- Electrical: any duplicate or missing tags? Any wires ending nowhere? Does every contact have a parent coil? Does every device have a part number and manufacturer? Is wire colour per standard? Are terminal numbers unique per strip? Are PLC addresses unique and spare capacity (~20 %) kept? Are fuse/overload ratings coordinated with conductor sizes (NEC/IEC 60364 tables)?
- Mechanical: is every feature fully dimensioned once? Are fits consistent (hole-basis H7 with shaft k6/g6)? Is material and finish stated? Can the part be manufactured and inspected (datum scheme, tolerance stack)? Does the BOM match balloons and the assembly?

# Common mistakes
| Mistake | Product | Fix |
|---|---|---|
| Drawing ducts/pipes as lines/polylines | MEP | Use parts + systems + connectors so sizing/schedules work |
| No levels/elevations set | MEP | Define project levels; set elevation per run before clash check |
| Disconnected parts | MEP | Connect to connectors; run system analysis |
| Hand-typed tags/schedule numbers | MEP/Electrical | Edit via property set/tag dialog; regenerate schedule |
| Wrong system on a run (supply drawn as return) | MEP | Check system assignment colour; change via *Change System* |
| Mixing IEC and JIC symbols | Electrical | One standard per project; set before first insert |
| Inserting symbols in DWG not in project | Electrical | Add DWG to project first; same drawing format |
| Typing component tags / editing text with `DDEDIT` | Electrical | Use Edit Component; keep cross-reference live |
| Numbering wires before design is frozen | Electrical | Finish circuit; then number; use fixed numbers for field edits |
| Skipping catalog part numbers | Electrical | Assign manufacturer/catalog at insert; BOM empty otherwise |
| Changing ladder rung spacing after drawing | Electrical | Settle spacing first; or re-run line reference update |
| Guessing panel component dimensions | Electrical | Use catalog footprint with real size |
| Wrong projection (first vs third angle) | Mechanical | Fix per standard; put symbol |
| Drawing hidden/center lines on ad hoc layers | Mechanical | Use `AM_*` layer standard; hide management |
| Not part-referencing components | Mechanical | Create components/Part refs; BOM follows |
| Raw `DIMLINEAR` mixed with power dims | Mechanical | Use Power Dimensioning consistently |
| Missing tolerance/datum frame | Mechanical | State general tolerance and datum reference frame |
| Hand-editing BOM/balloons | Mechanical | Update BOM; renumber balloons |
| Relying on auto-generated numbers without audit | all | Run Audit and report checks before issue |

## Sources
- AutoCAD Electrical / MEP / Mechanical context from video courses and official docs:
  - Skill Lync, AutoCAD Essentials for Mechanical Engineers (technical-drawing conventions, ISO/standards): https://www.youtube.com/watch?v=oqCio0IHsNE
  - freeCodeCamp, AutoCAD for Beginners (core engine, layers, dimstyles): https://www.youtube.com/watch?v=VtLXKU1PpRU
- Identified but captions could not be pulled (YouTube rate limit), used only as reading list: SourceCAD Electrical https://www.youtube.com/watch?v=7QQRG2sLbYk ; SM Techno Complete AutoCAD for MEP https://www.youtube.com/watch?v=r0HTg__mtcE ; SourceCAD AutoCAD for mechanical engineers https://www.youtube.com/watch?v=_6yX-5HC_hw
- Autodesk Help: AutoCAD Electrical https://help.autodesk.com/view/ACEL/2025/ENU/ ; AutoCAD Mechanical https://help.autodesk.com/view/ACDMECH/2025/ENU/ ; AutoCAD MEP https://help.autodesk.com/view/AMEP/2025/ENU/
- Engineering references for rules of thumb: ASHRAE Fundamentals, CIBSE Guide, IEC 60204-1, NFPA 79, ISO 128 / 1101 / 2768 / 286 (verify against project specifications).
