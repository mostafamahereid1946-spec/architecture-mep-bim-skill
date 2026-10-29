# IFC / openBIM: model structure, data requirements, ifcopenshell, checking, exchange

Scope: IFC4 (ISO 16739-1:2018) and IFC4x3 (ISO 16739-1:2024) as the exchange format; IfcOpenShell (Python) to author/read/validate offline; IDS, BCF, ISO 19650 context; exporting from Revit / ArchiCAD / SketchUp / Blender (Bonsai).
All code below was executed against IfcOpenShell 0.9.0 (module-style API). `ifcopenshell.api.run("root.create_entity", f, ...)` is the legacy equivalent and still works.

## 0. Beginner/AI mistakes vs pro behaviour

| Beginner / AI does | Pro does |
|---|---|
| Treats IFC as a 3D mesh format | IFC is **semantic data with geometry**: class, type, properties, relationships. Meshes only = useless for QTO/clash/FM |
| Everything is `IfcBuildingElementProxy` | Uses the right class (`IfcWall`, `IfcSlab`, `IfcCovering` ...) + `PredefinedType` (e.g. `SOLIDWALL`, `FLOOR`) |
| Forgets spatial structure | `IfcProject > IfcSite > IfcBuilding > IfcBuildingStorey` via `IfcRelAggregates`; elements contained via `IfcRelContainedInSpatialStructure` |
| Puts walls in storeys but ignores elevation | Sets `IfcBuildingStorey.Elevation` and placements relative to the storey, so heights are consistent |
| Invents property names (`FireProtect`) | Uses standard `Pset_*Common` names; custom data goes in a company pset with prefix (`ACME_...`) |
| Draws a hole by deleting geometry from a wall mesh | Models `IfcOpeningElement` (IfcRelVoidsElement) + door/window filling (IfcRelFillsElement) |
| Duplicates type data per instance | Uses `IfcWallType` etc. with material layer set and type-level psets; instances inherit (`IfcRelDefinesByType`) |
| Mixes units | Declares SI project units (`assign_unit`), uses metres in geometry |
| No classification | Attaches Uniclass 2015 / OmniClass / Uniformat / CCI via `IfcClassificationReference` |
| Sends "model" without checking | Runs IFC schema validation + IDS checking + clash + viewer inspection before delivery |
| Sets random GUIDs or reuses | Lets API generate GlobalId (22-char compressed); keeps GUIDs stable across revisions |
| Ignores geo-reference | Sets `IfcMapConversion` + `IfcProjectedCRS` (IFC4) when GIS coordination matters |

## 1. Schema versions and what's in them

| Schema | Notes |
|---|---|
| IFC2x3 TC1 | Still widespread for legacy/Revit default; no `IfcMapConversion`, limited `IfcAlignment` |
| **IFC4** (ADD2 TC1) | Current practical standard for buildings: Reference View MVD, Design Transfer View MVD; `IfcWall.PredefinedType`, `IfcBuildingElementPart` |
| **IFC4x3 ADD2** | Infrastructure: `IfcRoad`, `IfcBridge`, `IfcRailway`, `IfcMarineFacility`, `IfcAlignment`, `IfcFacility`, `IfcFacilityPart`, `IfcLinearPlacement`; also extra building classes; ISO 16739-1:2024 |
| IFC5 / ifcx | In development (USD-like, JSON-style); not for production |

Choose IFC4 for buildings unless recipient demands 2x3; IFC4x3 for roads/rail/bridges/alignments or mixed. Check `f.schema`.

## 2. Spatial hierarchy and key entities

```
IfcProject  (units, contexts, map conversion)
 `-IfcSite
    `-IfcBuilding
       `-IfcBuildingStorey (Elevation, composition type ELEMENT)
          |- IfcWall / IfcSlab / IfcColumn / IfcBeam / IfcDoor / IfcWindow / IfcStair / IfcRoof / IfcCovering ...
          |- IfcSpace  (aggregated under storey)
          `- IfcFurnishingElement (IfcFurniture), IfcFlowTerminal, IfcSanitaryTerminal ...
```

| Relationship | IFC entity | API function |
|---|---|---|
| Decomposition (site in project) | `IfcRelAggregates` | `aggregate.assign_object` |
| Containment (wall in storey) | `IfcRelContainedInSpatialStructure` | `spatial.assign_container` |
| Type | `IfcRelDefinesByType` | `type.assign_type` |
| Properties | `IfcRelDefinesByProperties` | `pset.add_pset / edit_pset` |
| Material | `IfcRelAssociatesMaterial` | `material.assign_material` |
| Classification | `IfcRelAssociatesClassification` | `classification.add_reference` |
| Opening | `IfcRelVoidsElement` | `feature.add_feature` |
| Filling | `IfcRelFillsElement` | `feature.add_filling` |
| Space boundary | `IfcRelSpaceBoundary` | `boundary.*` |
| System | `IfcSystem` / `IfcRelAssignsToGroup` | `system.*`, `group.*` |

Building element classes (IFC4): `IfcWall` (+`IfcWallStandardCase` deprecated in 4x3), `IfcSlab` (FLOOR/ROOF/LANDING/BASESLAB), `IfcRoof`, `IfcCovering` (CEILING/FLOORING/CLADDING/INSULATION), `IfcColumn`, `IfcBeam`, `IfcMember`, `IfcPlate`, `IfcCurtainWall`, `IfcRailing`, `IfcStair` + `IfcStairFlight`, `IfcRamp`, `IfcDoor`, `IfcWindow`, `IfcFooting`, `IfcPile`, `IfcBuildingElementProxy` (last resort).
Types: every class has `...Type` with `PredefinedType`; set it (it drives IDS/QTO).

## 3. Property sets, quantities, classification

- **Pset_<Class>Common** are standard (buildingSMART Data Dictionary / IFC docs). Examples:

| Class | Pset | Common properties |
|---|---|---|
| IfcWall | `Pset_WallCommon` | `IsExternal`, `LoadBearing`, `FireRating`, `AcousticRating`, `ThermalTransmittance`, `Reference`, `Status` |
| IfcDoor | `Pset_DoorCommon` | `IsExternal`, `FireRating`, `SecurityRating`, `HandicapAccessible`, `FireExit`, `SelfClosing` |
| IfcWindow | `Pset_WindowCommon` | `IsExternal`, `GlazingAreaFraction`, `ThermalTransmittance` |
| IfcSlab | `Pset_SlabCommon` | `IsExternal`, `LoadBearing`, `FireRating`, `PitchAngle` |
| IfcSpace | `Pset_SpaceCommon` | `Category`, `OccupancyType`, `GrossPlannedArea`, `NetPlannedArea`, `IsExternal` |
| IfcBuilding | `Pset_BuildingCommon` | `NumberOfStoreys`, `YearOfConstruction`, `OccupancyType` |
| Any | `Pset_ManufacturerTypeInformation`, `Pset_Warranty`, `Pset_EnvironmentalImpactIndicators` | Product data |

- **Quantities**: `Qto_WallBaseQuantities` (Length, Height, Width, GrossVolume, NetVolume, GrossSideArea, NetSideArea), `Qto_SlabBaseQuantities` (Depth, GrossArea, NetArea, GrossVolume), `Qto_SpaceBaseQuantities` (NetFloorArea, GrossFloorArea, Height, GrossVolume), `Qto_DoorBaseQuantities` etc. Use `pset.add_qto / edit_qto`; compute from geometry (ifcopenshell.util.element + `ifcopenshell.geom`) or use `ifc5d`.
- **Custom data**: custom pset names must not start with `Pset_`; prefix with org (`ACME_RoomFinishes`). Property types: `IfcLabel`, `IfcText`, `IfcBoolean`, `IfcInteger`, `IfcReal`, `IfcLengthMeasure`, `IfcAreaMeasure`, `IfcPowerMeasure`...
- **Classification systems**: Uniclass 2015 (UK; `Ss_25_10_30` systems, `EF_25_10` elements, `Pr_` products), OmniClass (Table 21 Elements, Table 23 Products), Uniformat, MasterFormat, CCI (Denmark), CCS, NS 3451, Omniclass; store via `IfcClassification` + `IfcClassificationReference`. buildingSMART Data Dictionary (bSDD) provides mappings and property definitions.

```python
cl  = A.classification.add_classification(f, classification="Uniclass 2015")
A.classification.add_reference(f, products=[wall], identification="EF_25_10", name="Walls", classification=cl)
```

## 4. IfcOpenShell: install and orientation

```bash
uv run --with ifcopenshell --with numpy python build.py            # no install needed
uv run --with ifcopenshell --with ifctester python check.py        # IDS checking (separate package: ifctester)
```
- Packages: `ifcopenshell` (core/api/util/geom/validate), `ifctester` (IDS), `ifcconvert` CLI (IFC -> OBJ/glTF/DAE/SVG), `ifcpatch` (recipes: merge, split, `Ifc2Sql`, convert schema), `ifcclash`, `ifcdiff`, `ifc5d`, `ifc4d`, `ifccsv`, `ifcopenshell.util.selector` (filter queries like `IfcWall, Pset_WallCommon.IsExternal=TRUE`).
- Module API: `import ifcopenshell.api.root` etc.; each module imported explicitly. `ifcopenshell.api.run("root.create_entity", ...)` (legacy).
- Coordinates in **metres** when `unit.assign_unit` default SI is used; passing mm to a metre model creates 1000x error.
- Reading: `f = ifcopenshell.open("x.ifc")`; `f.by_type("IfcWall")`, `f.by_guid(...)`, `e.is_a("IfcWall")`, `e.get_info()`, `ifcopenshell.util.element.get_psets(e)`, `get_type`, `get_container`, `get_material`, `ifcopenshell.util.placement.get_local_placement(e.ObjectPlacement)` (4x4 numpy).

## 5. Recipe: storey with 4 walls + door + slab + space, saved to IFC4 (tested)

Part 1: project, units, contexts, spatial tree.
```python
import numpy as np, ifcopenshell, ifcopenshell.util.element
import ifcopenshell.api.root, ifcopenshell.api.unit, ifcopenshell.api.context, ifcopenshell.api.project
import ifcopenshell.api.aggregate, ifcopenshell.api.spatial, ifcopenshell.api.geometry
import ifcopenshell.api.feature, ifcopenshell.api.pset, ifcopenshell.api.type
A = ifcopenshell.api
f = A.project.create_file(version="IFC4")
project = A.root.create_entity(f, ifc_class="IfcProject", name="Demo House")
A.unit.assign_unit(f)                                   # SI: metres
model = A.context.add_context(f, context_type="Model")
body = A.context.add_context(f, context_type="Model", context_identifier="Body",
                             target_view="MODEL_VIEW", parent=model)
site  = A.root.create_entity(f, ifc_class="IfcSite", name="Site")
bldg  = A.root.create_entity(f, ifc_class="IfcBuilding", name="Building A")
storey = A.root.create_entity(f, ifc_class="IfcBuildingStorey", name="Level 00"); storey.Elevation = 0.0
A.aggregate.assign_object(f, products=[site],   relating_object=project)
A.aggregate.assign_object(f, products=[bldg],   relating_object=site)
A.aggregate.assign_object(f, products=[storey], relating_object=bldg)
```
Part 2: placement helper, wall type, walls.
```python
def place(prod, x, y, rot=0.0, z=0.0):
    c, s = np.cos(rot), np.sin(rot)
    A.geometry.edit_object_placement(f, product=prod,
        matrix=np.array([[c,-s,0,x],[s,c,0,y],[0,0,1,z],[0,0,0,1]]))

wall_type = A.root.create_entity(f, ifc_class="IfcWallType", name="EW-200", predefined_type="SOLIDWALL")
def wall(p1, p2, name, h=3.0, t=0.2):
    w = A.root.create_entity(f, ifc_class="IfcWall", name=name)
    L = float(np.hypot(p2[0]-p1[0], p2[1]-p1[1]))
    rep = A.geometry.add_wall_representation(f, context=body, length=L, height=h, thickness=t)
    A.geometry.assign_representation(f, product=w, representation=rep)
    place(w, p1[0], p1[1], rot=float(np.arctan2(p2[1]-p1[1], p2[0]-p1[0])))
    A.spatial.assign_container(f, products=[w], relating_structure=storey)
    A.type.assign_type(f, related_objects=[w], relating_type=wall_type)
    return w
w1 = wall((0,0),(5,0),"W1"); wall((5,0),(5,4),"W2"); wall((5,4),(0,4),"W3"); wall((0,4),(0,0),"W4")
```
Part 3: door in opening, slab, space, psets, save.
```python
door = A.root.create_entity(f, ifc_class="IfcDoor", name="D1", predefined_type="DOOR")
door.OverallWidth, door.OverallHeight = 0.9, 2.1
opening = A.root.create_entity(f, ifc_class="IfcOpeningElement", name="D1-opening")
A.geometry.assign_representation(f, product=opening, representation=
    A.geometry.add_wall_representation(f, context=body, length=0.9, height=2.1, thickness=0.4))
place(opening, 2.0, -0.1); place(door, 2.0, -0.1)
A.feature.add_feature(f, feature=opening, element=w1)          # void in wall
A.feature.add_filling(f, opening=opening, element=door)        # door fills it
A.spatial.assign_container(f, products=[door], relating_structure=storey)

slab = A.root.create_entity(f, ifc_class="IfcSlab", name="Floor", predefined_type="FLOOR")
A.geometry.assign_representation(f, product=slab, representation=A.geometry.add_slab_representation(
    f, context=body, depth=0.2, polyline=[(0,0),(5,0),(5,4),(0,4)]))
place(slab, 0, 0, z=-0.2); A.spatial.assign_container(f, products=[slab], relating_structure=storey)

space = A.root.create_entity(f, ifc_class="IfcSpace", name="Room 01"); space.LongName = "Living"
A.aggregate.assign_object(f, products=[space], relating_object=storey)
ps = A.pset.add_pset(f, product=w1, name="Pset_WallCommon")
A.pset.edit_pset(f, pset=ps, properties={"IsExternal": True, "FireRating": "REI60", "LoadBearing": True})
f.write("house.ifc")
```
Result: 4 `IfcWall` (one with `IfcOpeningElement` + `IfcDoor`), `IfcSlab`, `IfcSpace`, all in `IfcBuildingStorey`; psets readable via `ifcopenshell.util.element.get_psets`.

Notes on the recipe:
- `add_wall_representation(length, height, thickness)` creates an extruded rectangle along local X; placement rotates it. For arbitrary footprints use `add_slab_representation(polyline=...)` or `ifcopenshell.api.geometry.add_profile_representation` / `add_mesh_representation`.
- `IfcSpace` geometry (floor polygon extruded) is optional but needed for area QTO and room-based IDS; add `add_slab_representation` style polyline extrusion.
- Create one `IfcWallType` and assign many instances; add material layer set to type:
```python
import ifcopenshell.api.material
ms = A.material.add_material_set(f, name="EW-200", set_type="IfcMaterialLayerSet")
con = A.material.add_material(f, name="Concrete", category="concrete")
A.material.add_layer(f, layer_set=ms, material=con).LayerThickness = 0.2
A.material.assign_material(f, products=[wall_type], type="IfcMaterialLayerSet", material=ms)
```
- Representation types: `SweptSolid`, `Brep`, `Tessellation` (meshes), `Clipping`; keep one `Body` representation; `Axis` and `FootPrint` for drawings.
- Georeferencing: `A.georeference.add_georeferencing(f)` + `edit_georeferencing(f, projected_crs={"Name":"EPSG:27700"}, coordinate_operation={"Eastings":..., "Northings":..., "OrthogonalHeight":...})` (IFC4+).

## 6. Validation and checking

1. **Schema/syntax**: 
```python
import ifcopenshell.validate
log = ifcopenshell.validate.json_logger()
ifcopenshell.validate.validate(ifcopenshell.open("house.ifc"), log)
print(len(log.statements), [s["message"] for s in log.statements[:5]])   # 0 for the recipe
```
CLI alternative: `ifcopenshell.validate` module (`python -m ifcopenshell.validate file.ifc`) or buildingSMART's online validator / `bsi-ifc-validation` service.
2. **Geometry sanity**:
```python
import ifcopenshell.geom
s = ifcopenshell.geom.settings(); s.set("use-world-coords", True)
shape = ifcopenshell.geom.create_shape(s, f.by_type("IfcWall")[0])
print(len(shape.geometry.verts)//3, "vertices")    # empty/exception => bad representation
```
3. **IDS** (Information Delivery Specification, buildingSMART standard, XML `.ids`): machine-checkable data requirements.
```python
from ifctester import ids
spec_set = ids.Ids(title="Walls need fire rating")
spec = ids.Specification(name="Walls have FireRating", ifcVersion=["IFC4"], minOccurs=1)
spec.applicability.append(ids.Entity(name="IFCWALL"))
spec.requirements.append(ids.Property(propertySet="Pset_WallCommon", baseName="FireRating", cardinality="required"))
spec_set.specifications.append(spec); spec_set.to_xml("req.ids")

i = ids.open("req.ids"); i.validate(ifcopenshell.open("house.ifc"))
for s in i.specifications:
    print(s.name, s.status, "failed:", [e.Name for e in s.failed_entities])
```
(Recipe: W1 passes; W2-W4 fail because only W1 has the pset.) Report formats: `from ifctester import reporter; reporter.Json(i).report(); reporter.Html(i).to_file("report.html")`.
IDS facets: **Entity** (class + predefined type), **Attribute**, **Property** (pset + name + value/datatype), **Classification**, **Material**, **PartOf**. Cardinality: required / optional / prohibited. IDS = *what* information must be present; it does not check geometry or clashes.
4. **Rule/clash**: `ifcclash` (clash detection), Solibri, BIMcollab Zoom, Trimble Connect, usBIM; BCF to report.
5. **Viewers for eyeballing**: BIMvision, Bonsai (Blender), xBIM Xplorer, Dalux, Trimble Connect, FZKViewer.

Checklist per delivery: valid schema; spatial tree; every product has container; no `IfcBuildingElementProxy` unless unavoidable; types present; psets complete per IDS; units SI; no empty geometry; GUIDs stable.

## 7. LOD / LOIN and information requirements

- **LOD (Level of Development, BIMForum US)** 100/200/300/350/400/500; focuses on geometry + generic info. **LOI**: level of information.
- **LOIN (Level of Information Need)** per ISO 7817-1:2024 / EN 17412-1: defines *purpose-driven* geometric information, alphanumeric information, documentation. Replace vague "LOD 300" with a LOIN table: *element x purpose x LOIN*.
- Example LOIN row: `IfcWall | Purpose: cost + energy + permit | Geometry: detailed, accurate within 10 mm, layers modeled | Info: FireRating, ThermalTransmittance, Classification Uniclass EF_25_10 | Documents: product data sheet`.
- **ISO 19650** (information management using BIM): 
  - Appointing party issues **OIR** (organizational), **PIR** (project), **AIR** (asset), and **EIR** (exchange information requirements) before tender.
  - Appointed party responds with **BEP** (BIM execution plan, pre-appointment + post-appointment), **TIDP** per task team, **MIDP** master.
  - Information container naming (ISO 19650-2 / UK NA): `Project-Originator-Volume/System-Level/Location-Type-Role-Number` e.g. `PRJ01-ACM-ZZ-00-M3-A-0001`, with status/revision metadata.
  - **CDE** (common data environment) states: *Work in Progress -> Shared -> Published -> Archive*; suitability codes S0..S6 (UK). IFC deliverables are typically exchanged at "Shared/Published".
  - Deliverables: federated model, IFC per discipline, COBie for asset handover (can derive from IFC), PIM (project) -> AIM (asset).
- **MVD (Model View Definition)**: subset of IFC for an exchange. IFC4 Reference View (read-only coordination) vs Design Transfer View (editable). Specify in EIR. IDS is the modern complement to MVD.

## 8. BCF (BIM Collaboration Format)

- Issue exchange format (zip of XML + snapshots): topics, viewpoints (camera + clipping + selected GUIDs), comments, assigned user, status. BCF 2.1 (XML/zip), 3.0 (IFC4-aligned), plus **BCF API** (REST) for server-based issue management.
- Anchor issues on **IfcGuid**; stable GUIDs matter. Use for clash resolution, design review.
- Tools: BIMcollab, Trimble Connect, Solibri, Bonsai (BCF panel), usBIM.platform, `bcf-client`/`bcf` Python libs.

## 9. Exporting IFC from authoring tools

| Tool | Route | Settings that matter |
|---|---|---|
| **Revit** | File > Export > IFC (open-source exporter, built-in) | IFC version: IFC4 Reference View (or 2x3 Coordination View 2.0 for legacy); export base quantities; export Revit properties as Psets; Space boundaries 1st level if energy; mapping table (Category -> IFC class) set; split walls/columns by level; coordinate base = Shared coordinates; "Export 2D elements" off |
| **ArchiCAD** | File > Save As IFC; use IFC Translator (Design Transfer, Coordination View, IFC4 RV) | Property mapping (IFC Manager); Type mapping; ensure "Convert Archicad properties to IFC property sets"; export by renovation filter and view; split by storey |
| **SketchUp (Pro)** | File > Export > IFC Model; classify objects first (Classifier with IFC 2x3 / IFC4) | Only classified groups/components typed; others -> `IfcBuildingElementProxy`; define `IfcBuildingStorey` elevations; solid, manifold geometry; clean tags; consistent names |
| **Blender + Bonsai (BlenderBIM)** | Native IFC authoring; File > Save as IFC; Bonsai reads/writes IFC directly | Create project -> storeys (Spatial) -> wall types with layer sets; assign types; run IDS from UI (Quality tab); Drawings, Schedules; Clash; QTO |
| **Vectorworks / Allplan / Tekla / FreeCAD** | Built-in IFC export | Choose reference view; map classes; verify with viewer |
| **Rhino/Grasshopper** | IFC exporter plugins (e.g. Bonsai from GH, `ifcopenshell` in Python) | Meshes -> proxy; use classification |
| **3ds Max** | Not an IFC authoring tool; import IFC via Revit/Navisworks -> FBX | Use IFC only as geometry source; link Revit when possible |

Native-IFC authoring idea (from Dion Moult's "Introduction to OpenBIM, Native IFC, and Open Source AEC"): author directly in IFC (Bonsai / IfcOpenShell) rather than export/translate; data stays in a single, schema-valid file and can be queried with scripts; drawings can be generated from the model as IFC annotation (grids, dimensions, tags are queryable), lighting/structural analysis models can ride in the same file.

## 10. Bonsai (Blender) workflow cues (from course "Modeling a full house in Bonsai BIM")

- Start: create project (units, MVD) -> add storeys/building -> define **types first** (wall type + material layer set; footing type with horizontal layers; slab type), then draw instances so each inherits type + material.
- Assign **materials to the type**, not instances (keeps edits global).
- Wall types: `Solid vertical layers` for walls; `horizontal layers` for slabs/footings; layer thicknesses in mm in the layer set editor.
- Use IFC classes + PredefinedType (e.g. geographic/feature element `cut base excavation`) rather than generic proxies.
- Use the Spatial tab to switch active container (storey) before drawing; drawings: plan/section/elevation from IFC with annotation, then export SVG/PDF.
- Properties: Psets tab; QTO tab for base quantities; Quality tab for IDS; BCF tab.

## 11. Python helpers (read & query)

```python
import ifcopenshell, ifcopenshell.util.element as E, ifcopenshell.util.selector as S
f = ifcopenshell.open("house.ifc")
for w in f.by_type("IfcWall"):
    print(w.GlobalId, w.Name, E.get_type(w).Name if E.get_type(w) else None,
          E.get_container(w).Name, E.get_psets(w).get("Pset_WallCommon", {}).get("FireRating"))
ext = S.filter_elements(f, "IfcWall, Pset_WallCommon.IsExternal=TRUE")      # selector query
```
```python
# Convert to glTF for Three.js/3ds Max pipelines (CLI)
# IfcConvert house.ifc house.glb      |  IfcConvert house.ifc house.obj
```
`ifcpatch` (separate pip package, not verified here) offers recipes such as merge, split, schema conversion, optimise; list them with its `--help` / docs before use.

## 12. Common mistakes (checklist)

| Mistake | Effect | Fix |
|---|---|---|
| Wrong schema chosen (2x3 vs 4) | Missing attributes / rejected by validator | Declare in EIR; pass `version="IFC4"` |
| Unit mismatch (mm in metre model) | 1000x scale errors | `assign_unit` + metres in geometry; or set mm unit explicitly |
| Elements not contained in storey | Invisible in tree/QTO | Always `spatial.assign_container` |
| Using `IfcWallStandardCase`/`IfcSlabStandardCase` | Deprecated in IFC4x3 | Use `IfcWall` / `IfcSlab` |
| Opening geometry in wall only | Door doesn't fill | Use `IfcOpeningElement` + `IfcRelFillsElement` |
| Duplicate GUIDs after copy | Merge conflicts / BCF broken | Re-create entities via API (new GUID) |
| Pset name invented, wrong data type | IDS fails | Use standard Pset names; correct measure types |
| Missing types / material | No take-off | Create types with layer sets |
| Over-detailed Brep (millions of triangles) | Huge file | Use extrusions/profiles; tessellate only when needed |
| Not validating | Bad delivery | Run validate + IDS + viewer |
| Revising without keeping GUIDs | Lost change history | Maintain GlobalId through revisions; use `ifcdiff` |

## Sources

Course transcripts and docs consulted:
- Dion Moult, "Introduction to OpenBIM, Native IFC, and Open Source AEC" - https://www.youtube.com/watch?v=h2Rv9iu7yDk
- BIMvoice, "modeling a full house in Bonsai BIM from scratch" - https://www.youtube.com/watch?v=JE4Y8sgS9Dk
- IfcOpenShell docs - https://docs.ifcopenshell.org/ ; API: https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/
- IfcTester (IDS) - https://docs.ifcopenshell.org/ifctester.html
- buildingSMART IFC4.3 docs - https://ifc43-docs.standards.buildingsmart.org/ ; IDS - https://technical.buildingsmart.org/projects/information-delivery-specification-ids/ ; BCF - https://technical.buildingsmart.org/standards/bcf/
- Bonsai docs - https://docs.bonsaibim.org/
