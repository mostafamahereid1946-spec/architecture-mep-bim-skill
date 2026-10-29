# SketchUp (Pro) + LayOut: professional modeling, documentation, scripting

Scope: architectural modeling in SketchUp 2023-2027, 2D documentation in LayOut, and driving both from Ruby / sketchup-mcp.
Rule of thumb: SketchUp is a *clean-surface* modeler. Output quality = model hygiene x scene/style discipline. LayOut only shows what the model already says.

## 0. Beginner/AI mistakes vs pro behaviour (read first)

| Beginner / AI does | Pro does |
|---|---|
| Draws everything loose in the root context (edges stick together, "everything is one blob") | Every building element is a Group or Component from the first stroke |
| Puts geometry on tags (layers) to organize it, or moves raw edges/faces to a non-Layer0 tag | Geometry stays on **Untagged**; the *Group/Component instance* gets the tag |
| Dozens of tags named "Layer1", "Tag 3" | Discipline-prefixed names: `A-WALL`, `A-DOOR`, `A-GLAZ`, `A-FLOR`, `S-COLS`, `F-FURN`, `X-2D-SYMB`, `X-DIMS` |
| Models in default template units, then scales to fit | Chooses template first (Architectural Millimeters / Meters / Feet-Inches), checks Model Info > Units |
| Types `3000` and lets the unit format swallow precision | Always writes units explicitly: `3000.mm`, `3.m`, `10'`, never bare floats in Ruby (inches!) |
| Copy/pasting 40 identical windows as groups | One Component definition, 40 instances (edit once, updates all; smaller file; LayOut fast) |
| Uses Group for repeated items, or Component for one-off walls | Group = unique one-off; Component = anything repeated (windows, doors, columns, furniture) |
| Moves a section plane after creating scenes | One section plane **per view** (see section 6); never reuse |
| Draws tiny edges (< 1 mm), leaves stray edges, flipped (blue) faces out | Clean geometry: no slivers, white face front out, run Solid Inspector2 / Fredo cleanup |
| Imports a 200 MB DWG straight in, leaves 3D faces and blocks everywhere | Cleans CAD first (purge, flatten, one layer per element type), imports at correct unit, one building layer at a time |
| Builds interior with thousands of poly from 3D Warehouse | Purges/limits 3D Warehouse; low-poly furniture, textures <= 1024 px, proxies where heavy |
| Exports to LayOut with Raster + shadows on + profiles | Hybrid/Vector viewports, shadows and heavy profiles off for plans; Raster only while drafting |
| Calls it done when it "looks right" | Runs a checklist: units, tags, scenes, purge, no stray geometry, classification, file name/version |

## 1. Template, units, precision

- Start from a template; set once, save as `.skp` template. Model Info > Units: *Decimal*, *Millimeters* (EU/metric) or *Architectural* (US), **Precision 0 mm** (architecture) or 0.0 for details; enable *Length snapping* ~ 5-10 mm; *Angle snapping* 15 degrees.
- **Internal units are inches, always.** Ruby `10` means 10 inches. Use `Numeric` helpers: `3.m`, `25.mm`, `2.5.cm`, `4.feet`. (`3.m` is returned in inches as a Length.)
- Display never changes geometry; only `Model Info > Units` format changes how numbers appear.
- Geometry smaller than ~1 mm (0.001") can fail face creation. Model at 1:1 real size; to model tiny details, make them large in a separate group then scale component.
- Coordinate sanity: keep model near origin (< ~10 km away). Far-away geo-located models cause jitter and failed pushpull. Use *Model Info > Geo-location* for site, but keep local origin.
- Axes: Z up, Red = X, Green = Y. Align axes to the building grid (Tools > Axes) *before* modeling so inference locking works for rotated buildings.

```ruby
# Set units in Ruby (LengthUnit: 0 in, 1 ft, 2 mm, 3 cm, 4 m; LengthFormat: 0 decimal, 1 architectural)
m = Sketchup.active_model
u = m.options["UnitsOptions"]
u["LengthUnit"]   = 2   # mm
u["LengthFormat"] = 0
u["LengthPrecision"] = 0
u["SuppressUnitsDisplay"] = false
```

## 2. Inference, tools, and fast precise drawing

| Technique | Why |
|---|---|
| Arrow keys lock axes: Up = blue (Z), Right = red (X), Left = green (Y), Down = parallel/perpendicular | Precise direction without typing |
| Type value + Enter after starting a move/line/push-pull: `3000` or `3000mm` | Exact length; typing `3000,2000` in Rectangle gives both sides |
| `Tab` on a face while drawing a rectangle/offset locks the plane | Draw on walls/roofs in correct plane |
| Offset `F` with typed value for wall thickness | Wall from plan: offset outline by thickness, then pushpull |
| Double-click Push/Pull to repeat last distance; Ctrl-click toggles "create new face" | Fast repeated floors/storeys |
| Move with `Ctrl` = copy; after copying type `5x` (array) or `/5` (divide between) | Columns, stair treads, windows evenly spaced |
| Guides (tape measure, `Ctrl`-toggle guide mode) and *Edit > Delete Guides* | Layout grid, setbacks; delete guides before sharing |
| Follow-me along path with a profile | Cornices, skirting, gutters, slab edges (profile + path must be separate from the host first) |
| Scale tool with `Ctrl` (center) and `Shift` (uniform) | Never scale non-uniformly a component you need clean in LayOut dimensions |
| Select by context: triple-click = connected geometry; `Ctrl+A` in group selects only inside | Prevent "I deleted the wrong thing" |
| Always hide rest of model (View > Component Edit > Hide Rest of Model) while editing | Avoid inference snapping to hidden-behind geometry |

Typical wall workflow (from 2D plan): trace plan polylines -> Offset to thickness -> select face -> group it -> Push/Pull to wall height -> openings: draw rectangle on wall face at exact positions (type `900,2100`) -> pushpull through -> insert Door/Window **components** that cut the opening (use components with "Cut opening" enabled, `Always face camera` off).

## 3. Groups vs Components vs Tags (core organization)

| Item | Use for | Notes |
|---|---|---|
| **Group** | One-off: the unique building volume, a specific wall, site mass | `make_unique` is automatic-ish; groups do not share edits |
| **Component** | Anything used >= 2 times: doors, windows, columns, furniture, stair type | Edit once -> all instances update. Name the *definition* clearly (`DOOR_900x2100_Single`). Component axes = insertion point; set them intentionally |
| **Tags** (ex-Layers, renamed 2020.1) | Visibility switching **of groups/components** only | Do not put raw geometry on a tag; tags can be added to folders; Scenes remember tag visibility |
| **Outliner** | Structure view | Nest Groups: `Building > Level 01 > Walls > Wall_A`. Use it to spot orphaned loose geometry |
| **Layer0 / Untagged** | Raw edges and faces inside groups | Rule: raw geometry stays Untagged |

Practical hierarchy for a building:
```
Site (group)
  Terrain (group)
Building (group)
  L00 (group)  <- tag A-L00
    Walls (group), Slab (group), Openings (components), Furniture (components)
  L01 ...
  Roof (group)
```
Pro naming: `<Discipline>-<Element>[-<Level>]` for tags, `<TYPE>_<size>_<variant>` for components. Folder tags for levels (`LEVEL 00` containing `A-WALL-L00` etc.) so levels toggle in one click.

Why this matters downstream: tags map to LayOut visibility, to IFC classification, to export layer names in DWG, and to 3ds Max / Twinmotion object names.

## 4. Scenes (pages) and styles = the reusable view system

A scene stores: camera, hidden geometry, tags, axes, section planes, style, shadows (selectable via checkboxes in the Scenes panel).

| Scene type | Camera | Style | Tags | Section plane |
|---|---|---|---|---|
| Plan L00 | Parallel, Top view | "Plan - Line" (no profiles, sections fill off, light grey faces or white) | structure + walls + doors + 2D symbols | Horizontal, cut 1.2 m (US: 4') above floor |
| Elevation N/S/E/W | Parallel, standard front/side | "Elevation - Line+Shade" with soft shadows | exterior only | none (or a clip plane to cut away neighbors) |
| Section A-A | Parallel | Same as elevation but *section fill ON*, section line weight 2-3 | structure + insulation + finishes | one plane, vertical |
| 3D view | Perspective 35-50 deg FOV (or 28 mm equiv) | "Presentation" | everything | none |
| Detail | Parallel | Hidden-line, thicker section edge | detail group only | custom plane |
| Walkthrough/eye | Perspective, eye height 1.60 m | Realistic | all | none |

Rules:
- **Scenes carry the style**; keep a library of 4-6 named styles (Plan, Elevation, Section, Presentation, Sketch).
- When updating style across many scenes: select all scenes in Scenes panel > right-click > Update > check **only Style and Fog** (do not overwrite cameras/tags).
- Name scenes with sort-friendly codes: `01_PLAN_L00`, `02_PLAN_L01`, `10_ELV_N`, `20_SEC_AA`, `30_3D_EXT_01`.
- Turn off *Include in animation* for utility scenes.
- Shadows: plans OFF; elevations gentle (e.g. 10:00 or fixed sun, soft). Heavy shadows slow LayOut.
- Exporting a scene for LayOut doesn't re-save automatically: after changing a scene, **Update scene** (right-click) then save the .skp; LayOut flags the viewport "out of date".
- Profile/edge settings: turn off *Depth cue*, *Extension* for drawings; use *Profiles* 1-2 px, *Section lines* 2-3 px; disable *Section fill* in plans if you want hollow walls (or enable with dark fill for poche).

## 5. Section planes (the plan-making engine)

- **Golden rule (taught in Educk and TheSketchUpEssentials workflows): one section plane per view. Do not move a plane that other scenes depend on.** Create a new plane per plan/section/elevation and use tags/folders to name them (`SP_PLAN_L00`, `SP_SEC_AA`).
- Section plane active state is stored per scene; style option "Section cuts" must be consistent or the cut vanishes when the style changes.
- Group-level cuts: a section plane inside a group only cuts that group (use for isolating one wing).
- Section fill: Styles > Modeling > Section fill color. Section lines: width 2-3.
- Alternative for elevations without planes: "Position Camera" tool + parallel projection (no section cut, but fewer planes).
- Elevations of an interior wall: use a plane close to the wall and `Zoom extents` in that scene.

```ruby
m = Sketchup.active_model
# horizontal plane at 1.2 m cutting downward, activate it, and store in a scene
sp = m.entities.add_section_plane([0, 0, 1.2.m], [0, 0, -1])   # [point, normal]
sp.name = "SP_PLAN_L00"; sp.symbol = "L0"
sp.activate
pg = m.pages.add("01_PLAN_L00")
pg.use_camera = true; pg.use_section_planes = true; pg.use_style = true; pg.use_hidden_layers = true
```

## 6. Dynamic Components (DC) and attributes

- DC = Component + attributes in dictionary `"dynamic_attributes"` evaluated by the DC extension. Good for parametric windows, doors, shelving, stairs, fences.
- Key attributes: `lenx`, `leny`, `lenz` (size), `x`,`y`,`z` (position), `copies`, `material`, `_name`, formulas like `=lenx/2`, `=CHOOSE(variant,0.9,1.0)`. Options (dropdown) via `_<attr>_options`.
- Build principle: proportional resizing needs Scale tool (not Move) in the DC; set Scale/Behavior flags per axis (`Fixed` vs `Any`).
- Modern alternative: use well-built Components + Classifier/IFC attributes; DCs are brittle and not exported cleanly. Use DC only when you need on-site parametric tweaks.
- Edit attributes in Ruby:
```ruby
d = Sketchup.active_model.selection.first.definition
d.set_attribute("dynamic_attributes", "lenx", 0.9.m.to_f)  # attributes are numbers in inches unless units given
d.set_attribute("dynamic_attributes", "_lenx_formula", "=LargestX*1")  # not recomputed until redraw
$dc_observers && $dc_observers.get_latest_class.redraw_with_undo(Sketchup.active_model.selection.first) rescue nil
```
(Redraw call varies by DC version; verify in console `$dc_observers`.)

## 7. Import from CAD (2D DWG -> 3D) the clean way

1. **In AutoCAD first**: `PURGE`, `-OVERKILL`, `FLATTEN`, explode blocks/hatches you don't need; set layers: keep only wall/door/window/column/grid; delete text/dimensions; save `.dwg` ver <= 2018. Confirm units (`INSUNITS`, `UNITS`). A 2 MB plan is fine, a 100 MB is not.
2. In SketchUp: File > Import > AutoCAD (.dwg/.dxf) > Options: Units = the CAD unit, *Merge coplanar faces* ON, *Orient faces consistently* ON, *Preserve drawing origin* ON.
3. Imported CAD lands in a Group + creates a tag per CAD layer. Check Outliner; **rename tags**; purge unused ones.
4. Do not trace over the CAD in-place; **lock the CAD group** (Right-click > Lock) and model walls on a new group on a different tag (`A-WALL`), with the CAD tag hidden at the end.
5. Close gaps: wall outlines must be closed loops to create faces: use Draw line over gaps or *Fredo Tools > Joint Push Pull / Eneroth Face Creator*. Check "Unconnected edges" with Solid Inspector2.
6. Floors by level: move CAD copy to the level elevation (`move` with typed value `3000`).
7. Export back to CAD: `File > Export > 3D Model > DWG` (3D) or scene-based **2D Graphic > DWG** (flat from scene camera) with correct scale: set `Options > Full Scale (1:1)`, Units = mm/m. For true 2D plans, prefer LayOut -> DWG.

Model-first alternative: for a project that already has a BIM, import IFC (SketchUp 2022+: File > Import > IFC), explode nested groups only for the elements you need, then use tags to mirror IFC types.

## 8. LayOut: scaled, professional documentation

### Document setup
- Choose paper size and units (`Document Setup`: **Paper**: A1/A3/ARCH D; Units: *Decimal Millimeters*; **Grid**: off). Use a title-block template (`.layout` saved in `Templates`).
- Add **Layers** (ordered bottom -> top): `Model-viewports` (unshared), `Hatch/poche`, `Dimensions`, `Annotations`, `Title block` (shared across pages). Never put the viewport on a shared layer unless you want it repeated on every page (it turns red).
- Pages = sheets (A101 Plan L00, A201 Elevations, A301 Sections, A401 Details).

### Viewports
1. Insert > Insert SketchUp Model... pick .skp; choose the **Scene** in the panel (`SketchUp Model` inspector).
2. Set the **Scale** (e.g. `1:50` for plans, `1:20` details, `1:100` site); *Preserve scale on resize* checked; Standard Views must be **Parallel** (uncheck *Perspective*).
3. Render mode: **Vector** for line drawings (clean line weights), **Hybrid** when textures/shadows needed, **Raster** for fast drafting only (slow-fast but jagged lines).
4. Lock the viewport once positioned. Use *Right-click > Update Model Reference* if the .skp moved; use *Reference* tab > *Update All* after SketchUp edits.
5. Per-viewport Tags: choose which tags show *without* changing the SketchUp scene.
6. Styles: *SketchUp Model > Edit* temporarily edits the .skp in SketchUp (round-trips).

### Tips that fix common LayOut problems
| Problem | Fix |
|---|---|
| Slow, laggy LayOut | Simplify model, purge unused components/materials, texture <= 1024 px, turn off shadows/profiles in styles, Raster while working, SketchUp 2024+ "experimental graphics engine" (preferences) |
| Dimensions/annotations hidden | Layer order: model at bottom, dimensions/annotations above; check "Select entities on layer" |
| Out-of-date viewport warning | Update scene in SketchUp, save .skp, then `Update Reference` |
| Wrong scale after resize | Check *Preserve scale*, rescale via panel, not by dragging corners |
| Dashed lines break | Use Vector mode; use shorter dash patterns; line scale |
| Section poche invisible | Style > Modeling > *Section fill color* on; or hatch with LayOut patterns inside model-ref lines |

### Annotation conventions
- Dimensions: *Linear dimension* tool with **Auto-snap to model**; format: Decimal mm, precision 0, text 2.5 mm paper height; end point style: tick / slash.
- Text: 2.5 mm min for body, 3.5 mm for headings. Keep fonts to 1-2 families (ISOCPEUR or Arial).
- Hatches: LayOut Pattern fills for materials in section; walls with `Fill` solid black poche for cuts, `Hatch` for masonry.
- Symbols (north arrow, level mark) kept as scrapbook (`.layout` in `Scrapbooks`).
- Graphic scale bar: Dimension tool > Label > custom.
- **Copy styles** between entities with the Style tool (eyedropper) to unify line weights.
- Export PDF for plot sets: `File > Export > PDF` with *Quality: High* / vector retained; `.dwg` export for contractors (LayOut 2D -> DWG scale preserved).

### LayOut Ruby API (inside SketchUp Ruby console; create/update sheets programmatically)
```ruby
doc = Layout::Document.new
doc.units = Layout::Document::DECIMAL_MILLIMETERS
page = doc.pages.first
layer = doc.layers.first; layer.name = "Viewports"
bounds = Geom::Bounds2d.new(10, 10, 280, 190)             # mm on A3 landscape in doc units
vp = Layout::SketchUpModel.new("C:/proj/model.skp", bounds)
doc.add_entity(vp, layer, page)
vp.current_scene = 2          # scene index (1-based)
vp.perspective   = false
vp.scale         = 1/50.0     # drawing / model
vp.render_mode   = Layout::SketchUpModel::VECTOR_RENDER
doc.save("C:/proj/sheet.layout")
doc.export("C:/proj/sheet.pdf")
```
Verify constants/signatures in the LayOut Ruby API docs for your SketchUp version before relying on them.

## 9. SketchUp Ruby API essentials (drive the app programmatically)

Always wrap modifications in an operation: one undo step, faster, atomic.

```ruby
m = Sketchup.active_model; ents = m.active_entities
m.start_operation("Build wall", true)          # disable_ui = true => faster
begin
  g = ents.add_group; g.name = "Wall_A"
  pts = [[0,0,0],[4.m,0,0],[4.m,0.2.m,0],[0,0.2.m,0]]
  f = g.entities.add_face(pts)
  f.reverse! if f.normal.z < 0                  # ensure face points up before pushpull
  f.pushpull(3.m)                               # height
  g.layer = m.tags.add("A-WALL")                # tag on the group, not the faces
  m.commit_operation
rescue => e
  m.abort_operation; puts e.message
end
```

Key patterns:
```ruby
# Component definition used many times
d = m.definitions.add("WIN_1200x1200")
d.entities.add_face([0,0,0],[1.2.m,0,0],[1.2.m,0,1.2.m],[0,0,1.2.m]).pushpull(-0.1.m)  # sample volume
t = Geom::Transformation.new([2.m, 0, 0.9.m])
inst = ents.add_instance(d, t); inst.layer = m.tags["A-GLAZ"] || m.tags.add("A-GLAZ")

# Transform: rotate 90 deg around Z at origin
rot = Geom::Transformation.rotation(ORIGIN, Z_AXIS, 90.degrees)
inst.transform!(rot)

# Materials
mat = m.materials.add("Concrete"); mat.color = [200,200,200]; mat.alpha = 1.0
g.material = mat; # applies to group instance

# Camera / parallel plan view / scenes
view = m.active_view
cam = Sketchup::Camera.new([0,0,50.m],[0,0,0],[0,1,0], false)  # eye,target,up,perspective=false
view.camera = cam; view.zoom_extents
m.pages.add("01_PLAN") 

# Cleanup / hygiene
m.definitions.purge_unused; m.materials.purge_unused; m.layers.purge_unused rescue nil

# Query
ents.grep(Sketchup::Group).map(&:name)
m.selection.grep(Sketchup::ComponentInstance).map { |c| [c.definition.name, c.bounds.width.to_mm.round] }

# Export (graphics + 3D)
view.write_image("C:/out/view.png", 2400, 1600, true)           # width,height,antialias
m.export("C:/out/model.dwg", false)    # 3D CAD; also .obj .fbx .stl .kmz depending on version
```

Ruby gotchas:
- Units: `Length` objects in inches; `1.m` -> 39.37; `.to_mm` / `.to_m` to read back.
- Face winding: `add_face` may produce a face with back out; check `face.normal`.
- `pushpull` on a face with `Z` normal pointing down moves *negative*; use `reverse!`.
- Entities inside groups are in local coordinates; use `inst.transformation` to map.
- Not every `add_face` succeeds if points are non-coplanar or duplicates; wrap in `begin/rescue`.
- `Sketchup.active_model` can change if user opens another file; refetch per call.
- `m.tags` is the alias for `m.layers` (2020.1+); older versions use `layers`.
- Operations: never leave `start_operation` open; abort on failure, else undo stack corrupts.
- Run headless at startup: `SketchUp.exe -RubyStartup C:\scripts\build.rb` (confirmed on SketchUp 2027 per host notes); script must `UI.start_timer(1){...}` if the model is not ready at startup.

### Classification / IFC mapping in Ruby
```ruby
m = Sketchup.active_model
m.classifications.load_schema("IFC 4.skc") rescue nil   # ships in SketchUp's Classifications folder (check available names)
inst = m.selection.first
(inst.definition).add_classification("IFC 4", "IfcWall")          # schema name, type name
inst.definition.get_classification_value(["IFC 4","IfcWall","Name"]) rescue nil
```
Use Classifier panel (Window > Classifier) in UI; only classified entities export to IFC as typed objects. Everything else exports as `IfcBuildingElementProxy`.

## 10. sketchup-mcp (github.com/mhyrr/sketchup-mcp)

- Components: SketchUp extension (`.rbz`; Extensions > SketchupMCP > Start Server, listens on **TCP 9876**) + Python MCP server (`uvx sketchup-mcp`) configured in the client.
- Tools: `get_scene_info`, `get_selected_components`, `create_component`, `delete_component`, `transform_component`, `set_material`, `export_scene`, **`eval_ruby`**.
- Practice: use `eval_ruby` for anything non-trivial and send **small, atomic scripts** (complex commands may time out). Failures appear only in SketchUp's Ruby Console, so always return structured results from the script: `puts` JSON, or return a value.
- `eval_ruby` is arbitrary code execution: validate paths, never `File.delete`, `system`, or `exec` from model-derived strings.
- Pattern for reliable MCP automation:
  1. `get_scene_info` to see units/entities/tags.
  2. One `eval_ruby` per logical element (walls L00; slab; openings), each in `start_operation` and returning counts.
  3. Verify with `get_scene_info` or read-back (bounds, face counts).
  4. Save scene/view: `view.write_image` to a known path, then inspect.

```ruby
# eval_ruby template: returns JSON summary
require 'json'
m = Sketchup.active_model
m.start_operation("MCP: slab", true)
g = m.entities.add_group; g.name = "Slab_L00"
f = g.entities.add_face([0,0,0],[10.m,0,0],[10.m,6.m,0],[0,6.m,0])
f.reverse! if f.normal.z < 0
f.pushpull(0.2.m)
g.layer = m.tags.add("A-FLOR")
m.commit_operation
puts JSON.generate({group: g.name, bounds_mm: [g.bounds.width.to_mm, g.bounds.height.to_mm, g.bounds.depth.to_mm].map(&:round)})
```

## 11. Extensions worth knowing (and when)

| Extension | Use |
|---|---|
| Solid Inspector2 (TIG/ThomThom) | Find holes, stray edges, flipped faces; **run before export/IFC/rendering** |
| Eneroth Auto Weld, Eneroth Face Creator | Clean curves, force faces from edges |
| Fredo6 suite (Curviloft, JointPushPull, FredoScale, Round Corner) | Roofs, curved forms, chamfers |
| TIG tools (Rotate Array, Auto Weld) | Geometry ops |
| Profile Builder 3 | Parametric profiles for walls, rails, cornices (paid) |
| CleanUp3 (ThomThom) | Remove edge duplicates, merge coplanar faces, purge |
| Skatter / Skalp | Scatter vegetation; Skalp: live 2D section fills/hatches in SketchUp (paid) |
| Thea / V-Ray / Enscape / Twinmotion | Render engines (Chaos V-Ray for SketchUp is the pro choice; Enscape/Twinmotion for fast visualization) |
| Eneroth Component Swapper / Instance Manager | Swap component versions |
| Ruby Console+/ Ruby Code Editor | Dev workflow |
| Trimble Connect (built-in) | Cloud model, BCF issue exchange, IFC import/export workflow |
| TrueBend / Flowify | Shaping |
| Artisan (SubD), SketchUp Diffusion (AI) | Organic forms / AI concept images (concept only) |

Heuristic: pick extensions to fix a specific hygiene or speed issue; avoid adding Ruby plugins that change geometry silently in a scripted workflow.

## 12. Export: CAD, IFC, 3D, images

| Target | Method | Gotchas |
|---|---|---|
| DWG 3D | File > Export > 3D Model > DWG | Faces vs polyfaces vs meshes; choose *Polyface meshes*; tags become CAD layers (tag names matter!) |
| DWG 2D plan/section | File > Export > 2D Graphic > DWG/DXF (scene-based) or LayOut export | Only visible edges in view; set scale 1:1 and units; do **not** use perspective |
| IFC | Pro: File > Export > IFC Model; or Classifier + export | Only classified objects typed; set IFC 4 if recipient supports; group/component names become IfcName; check origin and story elevations (assign storeys via Classifier `IfcBuildingStorey`) |
| 3ds Max / Blender / V-Ray | `.skp` direct import (Max/V-Ray support Link SketchUp), or FBX / OBJ / glTF | Components -> instances; keep groups named; materials as `.skm`; reset normals; ensure real-world texture scale |
| Revit | Use IFC, or .skp via Link/Import in Revit as DirectShape (not BIM-intelligent) | Revit gets only "Generic Models" from SKP; IFC with Classifier is better |
| Images | `view.write_image` / File > Export > 2D Graphic > PNG | Anti-alias on; transparent for compositing; pixel size >= 3000 px width for sheets |
| Walkthrough | File > Export > Animation | Scenes with transition times; use Enscape/Twinmotion for quality |

IFC export checklist from SketchUp: units set, geometry solid/closed, each building element a **Group/Component classified** with IFC type, levels as `IfcBuildingStorey` in Classifier, site as `IfcSite`, materials named, remove 3D Warehouse stray components, then re-open IFC in a viewer (BIMvision, BonsaiBIM, Solibri) to verify.

## 13. Pre-delivery checklist

- [ ] Model Info > Units correct, template named by project; model at origin.
- [ ] All geometry in groups/components; no loose edges at root (`ents.grep(Sketchup::Edge).size == 0`).
- [ ] Tags in consistent naming; raw geometry Untagged; unused tags purged.
- [ ] Unique components duplicated only when intended (`make_unique` used); definitions purged.
- [ ] Scenes named, styles saved, section planes one-per-view, each scene updated.
- [ ] No flipped faces / holes (Solid Inspector2 clean); non-manifold flagged.
- [ ] 3D Warehouse imports cleaned; texture sizes optimized.
- [ ] LayOut viewports scaled, vector, locked; layers ordered; "out-of-date" warnings gone.
- [ ] Exports tested: open the DWG/IFC in a viewer and spot-check scale and layers.
- [ ] File saved with version: `PROJECT_MODEL_A_v03.skp`; `Save As` previous version to compress file.

## Sources

Course transcripts (captions) and docs consulted:
- TheSketchUpEssentials, "Creating PLANS IN LAYOUT from a SketchUp Model" - https://www.youtube.com/watch?v=Rx_vnOahk30
- Educk, "Top 5 Tips for Better Documentation in SketchUp Layout" - https://www.youtube.com/watch?v=hrqSbYDiS2I
- SketchUp Ruby API - https://ruby.sketchup.com/ ; LayOut Ruby API: https://ruby.sketchup.com/Layout.html
- sketchup-mcp - https://github.com/mhyrr/sketchup-mcp
- SketchUp Help (Scenes, Section Planes, Classifier) - https://help.sketchup.com/
