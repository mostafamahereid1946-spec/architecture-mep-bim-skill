# Revit (Architecture / Structure / MEP) - professional practice and automation

Revit is a **database of parametric elements**; drawings are views of it. The beginner/AI failure mode is drafting (detail lines, groups, model-in-view hacks) instead of modeling with the right categories, levels, types and parameters.

> **NOTE - Revit LT has NO API.** Revit LT cannot run add-ins (`.addin`), Dynamo, pyRevit, or `revit-mcp`. Any automation (C# API, pyRevit, Dynamo, MCP) requires **full Revit** (Architecture / Structure / MEP / AEC Collection). LT route for an automated pipeline: generate the model **offline** (e.g. IFC with IfcOpenShell, DWG/DXF with ezdxf) and have the user import/link it in LT (DWG link/import is supported; IFC support in LT varies by version - verify in the user's release before promising it). LT also lacks worksharing, MEP/Structure toolsets, and some analysis - confirm what the user's license includes before planning the workflow.

---
## 1. Project setup (before modeling)

| Item | Pro practice | Notes |
|---|---|---|
| Template | Start from a **company `.rte`** (not "Default"): levels/grids stubs, view templates, filters, text/dim types, line styles, object styles, phases, worksets, sheets index, title block, schedules | Built-in templates: Architectural/Construction/Structural/Mechanical/Electrical/Plumbing; never start a real job in an empty file |
| Units | Project Units: length mm (or m for site), area m2, volume m3, angle deg; rounding to 1 mm; "Suppress trailing 0's" | Revit stores feet internally - API values are feet |
| Project Information | Name, number, client, address, status; used in title blocks | Fill before sheets |
| Location / True North | Manage > Location; set Project North vs True North on a site view. Rotate True North, not the building | Wrong north breaks sun studies and Shared Coordinates |
| Coordinates | Acquire coordinates from a linked CAD/Revit survey (Manage > Coordinates); Project Base Point (project origin) at grid intersection near building; Survey Point at survey origin; publish when done | Do not move base/survey points casually; unclip first, and never "move" a pinned point |
| Linking | Link Revit/CAD/IFC (Insert > Link), **Origin to Origin** if models share origin, else Shared Coordinates; Positioning "By Shared Coordinates" for discipline models | Never Import CAD into a project file; **Link** and delete/purge if imported (bloats file) |
| Worksets | Create at start: `Shared Levels & Grids`, `Architecture - Walls`, `Architecture - Interior`, `Core&Shell`, `Links - Structure`, `Links - MEP`, `Site`, `Furniture`; disable "Editable" abuses; central file on server | Turn on worksharing early (Collaborate > Collaborate); Revit Server or BIM 360/ACC Docs |
| Phases | Existing / New Construction / Demolished as minimum; Phase Filters (Show New, Show Existing, Show Complete) in View templates | Required for renovation; set Phase Created/Demolished on elements |
| Design Options | Only for real alternatives; keep Main Model clean; don't leave options open | Options bloat and confuse schedules |
| Browser Organization | Views by Discipline > Type > Sheet; Sheets by Discipline + Sheet Number. Use shared parameters `Browser Group 1/2` (or "Discipline" + "View Type") | Make Project Browser readable by anyone |
| Naming standard | Views: `L01_FloorPlan_Arch`, `L01_RCP`, `SEC-A_Building`, `DET-01_Roof Eaves`; Sheets: `A-101`; Types: `EXT_Brick-Cavity-300` | Consistent = searchable |

## 2. Levels, grids, scope boxes - the skeleton

1. Add **Levels** in an elevation/section view. Name `L00_Ground FFL +0.00`, `L01_First +3.50`, plus `T.O. Parapet` as needed. Use datum names that appear in tags; set Story Above/Below. Keep structural levels (`TOS`, `SSL`) via level types `Structure`/`Finish`.
2. Add **Grids** in plan: orthogonal grid first; draw with `Pick Lines`/`Multi-segment` from CAD link; name `A,B,C` and `1,2,3`. Bubble visibility both ends; extents with 3D extents; **Pin** levels and grids after approval (Modify > Pin). Place on workset `Shared Levels & Grids`.
3. **Copy/Monitor** levels and grids from the architect when working MEP/Structure; coordination review shows moves.
4. **Scope Boxes** to crop multiple views identically and control grid extents; assign each view and grid.
5. Create **View templates** and **Level-based plans**: `Floor Plan` (Plan), `Ceiling Plan`, `Structural Plan`, `Area Plan` per level.
- Never place elements with "Level 1" defaults when you intended `L00`; rename levels before modeling (renaming prompts to rename views).
- Change level elevations only in sections/elevations; dependent elements move (check "Related to Level" constraints).

## 3. View templates, visibility, filters

- **View template** = scale, discipline, detail level, V/G overrides, view range, phase filter, underlay, graphic display options. One template per view type: `A-Floor Plan 1-100`, `A-Floor Plan 1-50`, `A-RCP 1-100`, `A-Section 1-50`, `S-Foundation Plan`, `M-HVAC Plan`, `Coordination 3D`. Assign by selecting views > Apply View Template; unlock "Include" parameters you want per-view.
- **Visibility/Graphics (VV/VG)**: control Model Categories, Annotation, Imported categories, Revit Links (By Host View / By Linked View / Custom) and Filters (rule-based overrides by parameter, e.g. `Fire Rating >= 120`).
- **View range** (plan): Cut plane 1200 mm above level for floor plans; ensure windows cut; top above ceiling; for RCP set cut plane under ceiling.
- **Detail level**: Coarse/Medium/Fine control which family linework displays; Fine shows layers of compound walls; Coarse hides.
- **Crop region** + **Annotation Crop**; **Hidden lines** off for production.
- **Halftone/Underlay** for the upper level. **Temporary Hide/Isolate** only for inspection; never leave on.
- **Line weights**: Manage > Additional Settings > Line Weights (per scale); Object Styles define category weights. Don't overwrite line weights per element (Linework tool) except for rare 2D cleanup.

## 4. Families (the single most important skill)

| Type | What | Use |
|---|---|---|
| **System families** | Built into Revit: walls, floors, roofs, ceilings, stairs (by component), railings, ducts, pipes, levels, grids, text/dim types. Duplicate types in project; cannot load from file (transfer Project Standards) | Naming with assemblies and layers; set materials; Function (Structure/Finish/Insulation/Membrane) |
| **Loadable families** (`.rfa`) | Doors, windows, furniture, equipment, fixtures, generic models, annotation symbols/tags, titleblocks, profiles | Created from a family template; can have type catalogs |
| **In-place families** | Modeled inside the project for one-off geometry | Use sparingly (file bloat, can't reuse, bad for schedules); never for repeated items |
| **Nested / Shared** | Family inside family; mark nested "Shared" to schedule/tag independently | Hardware sets in doors |

### 4.1 Family creation rules
- Start from the correct **family template** (Door, Window, Generic Model wall-based/floor-based, Casework, Mechanical Equipment, Plumbing Fixture, Lighting Fixture, Electrical Equipment; face-based/work plane-based/line-based). Category determines schedules, tags, OOTB behavior and **IFC mapping** - never use `Generic Model` for items that belong to doors/furniture/equipment.
- Build on **Reference Planes** (named; Strong Reference / Weak Reference / Not a Reference) -> add dimensions -> **label** dimensions as parameters -> **align + lock** geometry to planes. Test with **Flex** (change parameters in Family Types). Do not build with free-floating geometry or hard-coded values.
- **Parameters**: *Type vs Instance*: width/height usually Type for catalog sizes; offset/mark instance. *Family parameter* (inside the family only, cannot schedule/tag), *Shared parameter* (`.txt` SP file; schedulable/taggable, same GUID across projects - required for data like `Manufacturer`, `FireRating`), *Project parameter* (assigned to categories in the project). Naming: `Width`, `Height`, `Depth`, `FrameWidth`; no spaces/units in names.
- **Formulas**: `Height = Width * 2`, `if(Width > 900 mm, 2, 1)`; constrain with min/max via formulas. Units explicit (`mm`). Avoid circular references. Lookup tables (`.csv`) for large sets of sizes.
- **Type catalog** (`FamilyName.txt` beside the `.rfa`): first row headers `Name##length##millimeters` ... for each type set parameters; allows loading selected sizes only (keeps file small). Provides standard sizes for doors, ducts.
- **Visibility**: control 2D vs 3D with Visibility Settings (Plan/RCP Coarse/Medium/Fine); 2D symbolic lines for plan (door swing arcs) with 3D simplified; hide 3D in Plan if needed. Keep detail level proportion: Coarse = low poly, Fine = nested details.
- **Subcategories** for geometry (Glass, Frame, Panel) so Object Styles can control materials and linework; materials as **Type parameters** (parametric material) so they can be changed.
- **Keep light**: <1 MB for typical fixtures; no imported CAD in families (use Link into family and then delete); avoid lofts with large faces; no Detail Items 3D duplicates; purge unused; model only what the LOD requires.
- Family `Type Mark` blank at family level; assign in project; required unique per type for schedules (see duplicate Type Mark warning in courses).
- Always set `Part Type`, `Work Plane-Based`, `Always vertical`, `Room Calculation Point` (doors), `Cut with Voids When Loaded` (for casework), and 'Shared' for nested.
- **Naming**: `Manufacturer_Product_Type` / `AR_Door_Single_Flush_Wood` ; file name = family name; type names with size `0900x2100`. Prefix by discipline `AR_`, `ST_`, `ME_`, `EL_`, `PL_`.
- **MEP families**: add **MEP Connectors** (Duct/Pipe/Electrical) with flow/size parameters; connector directions and system type; connectors tied to parameters; set `Part Type`; rotate origin; add clearance geometry in a subcategory; set Electrical `Load Classification`, `Voltage`, `Number of Poles`.
- **Parametric array** for repeating elements (railings, louvers): count by formula; set `Fixed Number` vs `Maximum Spacing`.

### 4.2 Project-level family discipline
- Load only needed families; `Purge Unused` (Manage > Purge Unused) after cleaning; duplicate types by right-click "Duplicate"; keep one family with many types over many families.
- Walls/floors/roofs: **create types by assembly** (`EXT_BrickCavity_300`, `INT_Partition_100`), use **Compound Structure** layers with Function, materials (with Graphics Pattern: Surface = fill, Cut = hatch), wrapping at inserts/ends; set **Fire Rating**, **Assembly Code (Uniformat)**, **Keynote**, and **Type Mark**. Do not make 25 near-identical types.
- Doors/windows are hosted in walls; set `Mark` instance value (not manual number text) for schedules.

## 5. Modeling order (what goes first)

### Architecture
1. Link survey/CAD site, set shared coordinates -> 2. Levels -> 3. Grids -> 4. Structure link (columns/slabs) as reference -> 5. **Walls**: choose `Location Line` (Finish Face: Exterior for exterior), `Base Constraint` = level, `Top Constraint` = next level (not "Unconnected 3000"), `Room Bounding` on; draw closed loops; edit joins -> 6. **Floors** (sketch inside wall faces; type with layers; slope arrows if needed; `Room Bounding`) -> 7. Doors/Windows (host to walls; Mark; swing) -> 8. Curtain walls (grid lines, mullions, panels) -> 9. Stairs by component (runs, landings, max riser/tread: R 170-190 mm, T 250-300 mm; ensure headroom) -> 10. Railings (path + top rail/baluster) -> 11. Roofs (footprint/extrusion; slope; join to walls via Attach Top/Base) -> 12. Ceilings (RCP) -> 13. Rooms/Areas (after walls closed; Room Separation lines; name/number, finishes) -> 14. Furniture/Equipment -> 15. Annotations/Tags/Dimensions -> 16. Sheets/Schedules.

### Structure
Link architect -> copy/monitor levels & grids -> **Foundations** (isolated, wall, slab) -> **Columns** (Structural Column, `Moves with grids`, Material) -> **Beams** (`Beam`, `Beam System`, `Structural Framing` family; set Z-justification and Start/End levels) -> **Slabs** (Structural Floor, `Structural` checked) -> Braces -> **Rebar** (Structural Rebar; Cover Settings, Rebar Shape Browser, Rebar Set, Area/Path reinforcement) -> Connections -> **Analytical model** (`Structural Analysis`) for export to analysis software -> Schedules (Structural Framing, Foundation, Rebar) -> Detail views.
Keep Physical vs Analytical separate; set `Structural Material`, `Structural Usage` (Column/Beam/Brace), and `Enable Analytical Model`.

### MEP
Link arch & structure -> copy/monitor levels -> create **Spaces** (not Rooms) from architectural linked rooms or sketch -> place equipment (AHU, FCU, boiler, pump, panel) with **connectors** -> terminals (diffusers, sprinklers, light fixtures, outlets) -> **Systems** (Mechanical/Piping/Electrical): `Create Duct/Pipe System`, naming systems `SA-01`, `RA-01`, `CHW-S` ; **routing**: use `Generate Layout` for quick runs, then manual; apply **Routing Preferences** (segments, fittings, preferred junction type) -> **Size** (duct/pipe sizing tools by velocity/friction, Mechanical Settings) -> slopes for gravity pipes -> insulation -> **Check Duct/Pipe Systems** (Analyze) -> **Interference Check** vs architecture/structure (Collaborate > Interference Check) -> Panel Schedules & circuits (`Edit Circuit`, Load Classification, Voltage/Phase) -> Tags (`Tag by Category`) -> Schedules/Quantities -> Coordination in Navisworks.
Heating/cooling loads: Revit does not replace load software; Spaces export to gbXML.

## 6. Schedules and quantities

- **Schedule/Quantities** per category; fields from built-in + shared parameters; sort by `Type Mark`; group totals; filters (e.g. `Phase Created = New Construction`); **itemize every instance** off for summary; **Totals** for area/volume; **Calculated Value** (formulas) e.g. `Area * Cost`.
- **Material Takeoff** for layers (concrete m3, brick m2); requires material assigned and accurate layers.
- **Key schedules** for finishes (Room Finish Schedule keyed by `Finish Key`), **Multi-Category** schedule with shared parameters for generic lists.
- **Room/Area schedule** needs closed boundaries; check `Room Bounding`, `Computation Height`; unplaced/redundant rooms will pollute totals.
- Data discipline: edit values in the model/schedule field, never in exported Excel only; export (`Export Schedule to CSV` or Dynamo / `Export room data`) for reporting. Schedule on sheet as `Schedule Graphics` with split columns.
- Always verify quantity by a second method (spot-check manual area) and filter by phase/option so duplicates don't double count.

## 7. Sheets and title blocks

- **Titleblock family**: sheet size A1/A3 (`594x841`), frame at paper size, `Sheet Number`, `Sheet Name`, `Project Number`, `Drawn by`, `Checked by`, `Issue Date`, revision schedule; labels (shared parameters) bound to Project Info & sheet.
- **Sheet numbering**: `A-101` plans, `A-201` elevations/sections, `A-301` details, `S-101`, `M-101`, `E-101`, `P-101`. **Sheet list** schedule as index; Sheet Issues/Revisions (Revision Clouds + Revision Schedule).
- One view per sheet position, except legends and schedules (legends can repeat). Viewport types (`Title w/ Line`, `No Title`); viewport title shows view name/scale/number via parameters (`Title on Sheet`).
- **Callouts, sections, elevation tags** with detail numbers; "Reference Other View"; Section heads, tag families unified.
- **Crop/Scope**: crop views consistently; align views across sheets with the same scope box and **Guide Grid** on sheet (View > Guide Grid) so repeated plans line up.
- Printing: `Export > PDF` (2022+), settings for vector, raster quality; combine sheets; set "Hide Ref/Work Planes", "Hide Scope Boxes", "Hide Crop Boundaries". DWG export via Export Setups (layer mapping to AIA/ISO standard `exportlayers-*.txt`).
- **Sheet Collections** (2023+) for sheet sets; Revisions with `Issued` toggle.

## 8. Annotation

- Annotation scales automatically with view scale (text in paper size); define few Text Types (2.5 mm notes, 3.5 title; font **Arial/Tahoma**; Arabic needs a Unicode font; set background `Transparent`).
- **Dimensions**: Aligned/Linear tied to references, locked dims for constraints; **Equality** (`EQ`) dims; dimension types for plans, details. Spot Elevations/Coordinates/Slopes.
- **Tags**: Door/Window/Room/Material/Keynote tags using family type/parameters (`Mark`, `Type Mark`); do not type text over elements.
- **Keynotes**: Keynote file (`.txt` tab-delimited) from CSI/Uniclass; place keynotes as tags; keynote legend.
- **Detail components**, **Repeating details**, **Filled regions**, **Masking regions**, **Detail lines** only in views for detail drawing; **Drafting Views** for details not modeled; **Legends** for symbol lists. Do not mix detail drawn over a model that contradicts it.
- **Text Notes** only for general notes; for room names/areas use Room tags.

## 9. Model health / process

- **Warnings** (Manage > Inquiries > Review Warnings): keep < ~100; fix duplicates, overlapping walls, room not enclosed.
- `Audit` on open; `Compact` on save-as central; Sync with Central daily; Relinquish All; descriptive sync comments; never work in Central; use Local copies.
- Purge, remove unused views/families/imported CAD, `Manage Links` refresh, Compress.
- Remove groups unless truly repetitive; do not use model groups for whole floors (breaks per-instance parameters).
- Delete not-needed Design Options and unplaced rooms; remove "In-place Families" leftovers.
- **Interference checks** and `Model Checker`/Solibri/Navisworks; run **IDS** checks if specified.
- Export as `.rvt` correct version (backwards save not allowed); upgrade only with team agreement.

## 10. IFC export / interoperability

| Setting (Revit IFC exporter) | Recommendation |
|---|---|
| IFC version | **IFC4 Reference View** for new coordination (2022+); **IFC2x3 Coordination View 2.0** when the receiver only supports 2x3; IFC4 Design Transfer View for authoring hand-offs |
| File type | `.ifc` (or `.ifcZIP`) |
| Phase to export | Last phase (New Construction) |
| Space boundaries | None/1st level only if needed for energy |
| Split walls and columns by level | On for coordination; Off for authoring |
| Export base quantities | On (IfcQuantities for takeoff) |
| Include Revit property sets / IFC common property sets | On (Pset_WallCommon, Pset_DoorCommon with FireRating, IsExternal, LoadBearing) |
| Export schedules as property sets | On when you need schedule data |
| Level of detail | Medium (Low for large, High for fabrication) |
| Export 2D plan view elements | Off unless asked |
| Use active view when creating geometry | Off |
| Visible elements in view only | Off unless you set a dedicated "IFC Export" 3D view |
| Export bounding box | On/Off per receiver (bounding box = placeholder geometry) |
| Linked files | Off unless exporting links separately (export each model separately) |
| Coordinate base | **Shared Coordinates** (or Project Base Point if the project uses that; agree in BEP) |
| IFC class mapping | Verify **Export IFC Class as** per category/type (`IfcWall`, `IfcSlab`, `IfcDoor`); set `IfcExportAs` shared parameter on families that need override; Generic Models -> `IfcBuildingElementProxy` (avoid) |
| Shared parameters | Add `IfcExportAs`, `IfcExportType`, `IfcName`, `IfcDescription`, `IfcObjectType` to categories |
- Check the result in a viewer (BIMcollab Zoom, Solibri, xBIM, FZK Viewer) and with IfcOpenShell:
```python
import ifcopenshell
m = ifcopenshell.open("model.ifc")
print(m.schema, len(m.by_type("IfcWall")), "walls", len(m.by_type("IfcBuildingElementProxy")), "proxies")
for d in m.by_type("IfcDoor")[:5]: print(d.Name, d.GlobalId)
```
- DWG export: use Export Setups to map to AIA layers; set "Export rooms/spaces as polylines" if needed; units mm.
- Other: `COBie` export, `gbXML` for energy, `NWC` (Navisworks), `FBX/OBJ` for visualization, `CSV` schedules.

## 11. LOD / LOIN / information management

| Concept | Meaning | Practical use |
|---|---|---|
| LOD 100/200/300/350/400/500 (AIA/BIMForum) | Geometric/information maturity of elements (concept -> approximate -> precise -> with connections -> fabrication -> as-built) | Used per element per phase in the MPDT (Model Progression spec) |
| **LOIN** - Level of Information Need (ISO 7817-1 / EN 17412-1) | Defines needed **geometrical**, **alphanumerical** (properties), **documentation** information per purpose/actor/milestone; replaces LOD vocabulary in ISO 19650 environments | Put in BIM Execution Plan (BEP) / EIR: e.g. "Doors at Stage 4: geometry LOD 300 equivalent, properties `FireRating`, `Mark`, `Manufacturer`, documentation: data sheet" |
| LOG/LOI (UK) | Level of Geometry / Level of Information | Same idea |
- Do not model beyond the stage's need (heavy families, bolts in beams at concept stage). Do not leave key data blank (fire rating, material, classification code Uniclass/OmniClass/Uniformat, COBie `Type`, `Space`, `Component` info).
- **ISO 19650** file naming: `Project-Originator-Volume-Level-Type-Role-Number` e.g. `PRJ-ABC-ZZ-00-M3-A-0001.rvt`; Status codes (S0/S1/S2... WIP/Shared/Published/Archive); use CDE.
- Shared parameters and classification: assign `Assembly Code` and `Keynote`, `OmniClass Number` per type; template contains these.
- **Models** per discipline & volume split; link, don't merge; BEP states origin, units, naming, LOIN, clash tolerance, issue frequency.

---
## 12. Revit API, pyRevit, Dynamo, MCP

Requires **full Revit** (not LT). Internal units: **feet** - convert (`UnitUtils.ConvertToInternalUnits(5000, UnitTypeId.Millimeters)`). Revit 2024 and earlier: .NET Framework 4.8; **Revit 2025+: .NET 8**. `ElementId` is `long` from 2024 (`.Value`; `.IntegerValue` obsolete). All modifications inside a `Transaction`. Use `ExternalEvent`/`IExternalEventHandler` for any call from a non-Revit thread (MCP sockets, WPF modeless dialogs).

### 12.1 C# - external command skeleton + wall creation
```csharp
using Autodesk.Revit.Attributes; using Autodesk.Revit.DB; using Autodesk.Revit.UI; using System.Linq;
[Transaction(TransactionMode.Manual)]
public class MakeWall : IExternalCommand {
  public Result Execute(ExternalCommandData d, ref string msg, ElementSet els) {
    Document doc = d.Application.ActiveUIDocument.Document;
    Level lvl = new FilteredElementCollector(doc).OfClass(typeof(Level)).Cast<Level>().OrderBy(l => l.Elevation).First();
    double L = UnitUtils.ConvertToInternalUnits(5000, UnitTypeId.Millimeters);
    using (Transaction t = new Transaction(doc, "Create wall")) {
      t.Start();
      Wall.Create(doc, Line.CreateBound(XYZ.Zero, new XYZ(L, 0, 0)), lvl.Id, false);
      t.Commit();
    }
    return Result.Succeeded;
  }
}
```
Deploy: build DLL; create `MyAddin.addin` XML (`<Assembly>`, `<FullClassName>`, `<AddInId>` GUID) in `%AppData%\Autodesk\Revit\Addins\<year>\`. Debug with `Add-in Manager` or Visual Studio attach. Templates: Revit SDK, `Nice3point.Revit.Templates` (`dotnet new install Nice3point.Revit.Templates`).

### 12.2 Read data (filters, parameters)
```csharp
var doors = new FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Doors)
              .WhereElementIsNotElementType().Cast<FamilyInstance>();
foreach (var dr in doors) {
  string mark = dr.get_Parameter(BuiltInParameter.ALL_MODEL_MARK)?.AsString();
  double wFt  = dr.Symbol.get_Parameter(BuiltInParameter.DOOR_WIDTH)?.AsDouble() ?? 0;
  double wMm  = UnitUtils.ConvertFromInternalUnits(wFt, UnitTypeId.Millimeters);
}
```
Use `BuiltInParameter` (language independent) over `LookupParameter("Width")` (localized names, multiple matches). Prefer `OfClass`/`OfCategory`/quick filters before slow filters; `ElementParameterFilter` for rule-based.

### 12.3 IFC export through the API
```csharp
using (Transaction t = new Transaction(doc, "IFC")) {
  t.Start();
  var o = new IFCExportOptions { FileVersion = IFCVersion.IFC4, ExportBaseQuantities = true, WallAndColumnSplitting = true };
  doc.Export(@"C:\out", "model", o);
  t.RollBack();   // export may touch shared parameters; do not commit
}
```

### 12.4 pyRevit (IronPython or CPython script in a pyRevit tab)
Folder: `MyTab.tab/MyPanel.panel/Check.pushbutton/script.py` (+ optional `bundle.yaml`, `icon.png`). No compile step; edit & reload.
```python
from pyrevit import revit, DB, forms, script
doc = revit.doc
walls = (DB.FilteredElementCollector(doc).OfCategory(DB.BuiltInCategory.OST_Walls)
         .WhereElementIsNotElementType().ToElements())
bad = [w for w in walls if w.get_Parameter(DB.BuiltInParameter.WALL_USER_HEIGHT_PARAM).AsDouble() == 0]
with revit.Transaction("Flag walls"):
    for w in walls:
        p = w.LookupParameter("Comments")
        if p and not p.IsReadOnly: p.Set("checked")
forms.alert("{} walls, {} with zero height".format(len(walls), len(bad)))
```
Helpers: `revit.get_selection()`, `forms.SelectFromList`, `script.get_output()`; CLI `pyrevit run script.py model.rvt --revit=2025` runs headless against a model.

### 12.5 Dynamo (visual + Python node)
Use for placing families from Excel, renaming sheets, batch parameter set. CPython3 node:
```python
import clr; clr.AddReference('RevitAPI'); clr.AddReference('RevitServices')
from Autodesk.Revit.DB import *
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
doc = DocumentManager.Instance.CurrentDBDocument
TransactionManager.Instance.EnsureInTransaction(doc)
for e in UnwrapElement(IN[0]):
    e.LookupParameter("Comments").Set(IN[1])
TransactionManager.Instance.TransactionTaskDone()
OUT = len(IN[0])
```
Dynamo Player/Dynamo for Revit CLI can run graphs; keep graphs parameterized with inputs; test on a copy.

### 12.6 Revit MCP (revit-mcp)
- Architecture: Node MCP server (`revit-mcp`, Node 18+, `npm install && npm run build`, config `node build/index.js`) <-> **revit-mcp-plugin** (add-in inside Revit; SocketService -> CommandSet -> Revit API via ExternalEvent). Repo: github.com/mcp-servers-for-revit/revit-mcp (archived Feb 2026; development moved to a monorepo under the same GitHub org - check current repo).
- Tools: query `get_current_view_info`, `get_current_view_elements`, `get_available_family_types`, `get_selected_elements`, `get_material_quantities`, `ai_element_filter`, `analyze_model_statistics`; create `create_point_based_element`, `create_line_based_element`, `create_surface_based_element`, `create_grid`, `create_level`, `create_room`, `create_structural_framing_system`; modify `delete_element`, `operate_element`, `color_elements`; tag/export `tag_all_walls`, `tag_all_rooms`, `export_room_data`; storage `store_project_data`, `store_room_data`, `query_stored_data`; `send_code_to_revit` (arbitrary C# - success best on simple, well-specified code), `say_hello`.
- Practice: query types (`get_available_family_types`) before creating; coordinates are model units (check mm vs ft conversion in the tool); create levels/grids first; keep operations small; read back with queries; never send destructive code (`delete_element`) without confirmation; work on a detached/local copy of the model; LT cannot host this.
- Fallback when no live Revit: produce **IFC** with IfcOpenShell or **DWG/DXF** with ezdxf and tell the user to link it.

### 12.7 Choosing a route
| Task | Best tool |
|---|---|
| One-off bulk parameter update | pyRevit script or Dynamo |
| Repeatable product with UI | C# add-in (Nice3point templates) |
| Conversational model queries/edits | revit-mcp (Revit open) |
| Generate geometry without Revit | IfcOpenShell (IFC), ezdxf (DWG/DXF) |
| Headless server batch | Revit Design Automation API (APS) / `pyrevit run` |

## 13. Common mistakes (beginner/AI vs pro)

| Mistake | Consequence | Pro fix |
|---|---|---|
| Drawing with detail lines / lines instead of walls, floors | No schedules, no sections update | Model elements; detail lines only for 2D |
| Wall `Top Constraint` = Unconnected 3000 | Heights don't follow level changes | Constrain to levels; use offsets |
| Levels renamed/added after modeling | Views/tags mismatch | Set levels/grids first; pin |
| Grids not pinned / duplicated | Drift | Pin; copy/monitor |
| Importing CAD instead of linking | File bloat, unstable | Link; purge imports |
| Using Generic Model for everything | Wrong schedules/IFC | Correct category via template |
| Hard-coded dims in families, no reference planes | Families break when flexed | Reference planes + parameters + Flex |
| In-place families for repeated items | Bloat, no type control | Loadable family |
| Over-detailed families (CAD, 3D screws) | Slow file | Match LOIN; 2D symbolic for plan |
| Duplicate Type Mark / empty Mark | Schedule/tag errors | Unique Type Mark per type; Mark per instance |
| Too many wall types / names like "Wall 1" | Unmanageable | Assembly-based naming |
| Rooms not enclosed / room separation missing | Wrong areas | Room bounding, separators |
| Using Rooms in MEP | No loads | Use Spaces |
| Disconnected MEP elements / no system | Sizing fails | Connect, assign system, Check systems |
| Dimension/text typed values instead of parameters | Stale info | Tags & dims referencing elements |
| Same view placed on two sheets | Revit blocks | Duplicate with Detailing / Dependent view |
| Views without templates | Inconsistent graphics | View templates by type |
| Annotation scale in model, text sized wrong | Unreadable | Revit text is paper size; set Text Type 2.5 mm |
| Working in Central file, not syncing | Lost work | Local copy; sync often |
| Ignoring warnings | Corruption | Review warnings weekly |
| IFC export with defaults | Missing classes, proxies | Configure per section 10 |
| Moving Project Base Point to "fix" position | Coordinate chaos | Use Shared Coordinates; Acquire from link |
| Assuming Revit LT can run scripts/MCP | Pipeline fails | Full Revit only; LT = import offline outputs |
| API: forgetting Transaction / feet units / localized parameter names | Exceptions, wrong sizes | Section 12 rules |
| Claiming success because call returned | Hidden errors | Query back, count elements, export IFC/PDF and inspect |

## Sources
- Archgyan Academy, The Complete Revit Course for Architectural Design: https://www.youtube.com/watch?v=pQLrIcVxTy4 (levels/views/type mark/families workflow)
- freeCodeCamp AutoCAD course (scale/annotation contrast): https://www.youtube.com/watch?v=VtLXKU1PpRU
- Identified but captions not retrievable (rate-limited), reading list only: Balkan Architect https://www.youtube.com/watch?v=chom9hiewXI ; PTS CAD EXPERT Revit MEP https://www.youtube.com/watch?v=xCBYGG9kJFk ; PTS Revit Structure https://www.youtube.com/watch?v=tVcspo72rEY
- Revit API docs: https://www.revitapidocs.com/ and Autodesk Revit Developer Center https://aps.autodesk.com/developer/overview/revit ; Revit help https://help.autodesk.com/view/RVT/2025/ENU/
- revit-mcp: https://github.com/mcp-servers-for-revit/revit-mcp ; pyRevit https://github.com/pyrevitlabs/pyRevit ; Dynamo https://dynamobim.org ; IfcOpenShell https://ifcopenshell.org ; ISO 19650, ISO 7817-1, buildingSMART IFC docs.
