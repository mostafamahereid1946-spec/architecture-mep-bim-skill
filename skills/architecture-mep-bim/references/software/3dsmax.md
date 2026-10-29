# 3ds Max: architectural visualization pipeline (V-Ray / Corona / Arnold) + scripting

Scope: turning CAD/SketchUp/Revit data into photoreal stills in 3ds Max 2023-2027; driving Max with MAXScript, pymxs, `3dsmaxbatch.exe`, and 3dsmax-mcp.
Principle: **an arch-viz image is 40% modeling scale/detail, 30% light & camera physics, 20% materials, 10% post.** Fix scale and camera first; render settings are the smallest lever.

## 0. Beginner/AI mistakes vs pro behaviour

| Beginner / AI does | Pro does |
|---|---|
| Starts modeling without checking Units | Sets System Unit Scale + Display Units before import or modeling; imports with matching units |
| Imports DWG with 5000 layers and renders it | Cleans in CAD first; imports; uses layers/groups; keeps CAD as a *locked ref* and models clean geometry above |
| Models walls as boxes, perfect 90 deg, zero edge bevel | Poly-modeled with real thickness, chamfered/bevelled edges (1-5 mm) so edges catch highlights |
| Uses 3ds Max Standard / Physical material without real-world size | Uses V-Ray/Corona/Arnold materials with **Real-world map size** and real dimensions (e.g. 600x600 mm tile) |
| Copies objects 100x | Instances / proxies (V-Ray Proxy, Corona Proxy), Forest Pack / RailClone for scatter/arrays |
| Dials Sun intensity & "multiplier" until bright | Uses physical camera (f-stop, shutter, ISO) with physically scaled Sun+Sky/HDRI, exposure from camera |
| White walls 255 RGB, black 0 | Albedo range ~0.04 (black) to ~0.85 (white); never pure white/black |
| Renders at 4K and waits 3 hours without a test | Test at 25-50% res, region renders, noise limit then final; denoise |
| Photoshop heavy-handed filters | Subtle: curves, colour balance, vignette, slight bloom/glare; render elements (Lightmix, Z-depth) used for control |
| Camera at 1.7 m with 24 mm wide lens and perspective distortion | Camera ~1.2-1.7 m for exteriors, 35-50 mm equiv, **vertical lines corrected** with Vertical Shift / 2-point |
| Same noise settings every time | Chooses noise limit / pass limit by purpose: preview vs final |

## 1. Project setup: units, gamma, folders

- **Customize > Units Setup**: *System Unit Setup* = Millimeters or Meters (match your CAD/SketchUp). Display Units = Metric (mm or m) or US Standard. **Do this before any geometry is created or imported.** Changing later does not rescale.
- File > Import: choose *Convert file units to* the system unit; for DWG: check *Rescale* with the same unit. For FBX: *Automatic* units.
- Project folder: `Max_Projects/<Client_Project>/scenes, sceneassets/images, export, renderoutput, backup`. Use `File > Set Project Folder`, maps referenced as relative paths. Save increments (`Ctrl+Alt+Shift+Space`) and Auto-backup on.
- Colour management: Gamma 2.2 & LUT enabled (default); assign *Bitmap Input Gamma* 2.2 for color maps, **1.0 / "Override" for data maps** (roughness, bump, normal, metalness, AO).
- Hardware: 32 GB RAM comfortable, 16 GB minimum (VizAcademy). Keep GPU drivers current (Chaos requires NVIDIA Studio/Game Ready mainstream).
- Scene hygiene: Scene Converter (V-Ray), Resource Collector to bundle assets, `Customize > Preferences > Files`: *Save viewport thumbnails* off for speed.

## 2. Data import: CAD, Revit, SketchUp, IFC

| Source | Route | Gotchas |
|---|---|---|
| DWG/DXF | Import (not link) for clean base, or **Link DWG** (File Link Manager) for live updates | Layers -> objects; many splines, 3D faces. Delete duplicates; weld (`Edit Poly Weld`) with 0.01 mm; collapse; use **Extrude/Shell on cleaned splines** |
| Revit | **Link Revit** (Revit link, `.rvt`): `File > Link Revit...` lets Max track changes | Ensure Revit 3D view has needed categories visible; combine by Material for fewer objects; keep unit consistency |
| SketchUp | `.skp` import or **Link SketchUp** (File Link Manager) | Components -> instances (good); faces may flip -> set Normal Unify; textures real size; remove 3D Warehouse junk first |
| IFC | Max can import IFC via Revit/Navisworks/Plant, or convert IFC -> FBX/glTF in Blender (BonsaiBIM) | IFC exports ~ all geometry as triangulated; many objects per storey; use layer/Name filters |
| FBX/OBJ/glTF | Import | FBX unit conversions; vertex colors; materials not carry; re-assign |
| Chaos Cosmos | Cosmos Browser (V-Ray) or Corona Asset Library | Scale check; proxy assets |

Link workflow tips (from V-Ray/Corona arch-viz courses): after linking, use File Link Manager's *Reload* instead of re-importing; never edit linked objects; apply materials via **Material ID/ Layer/ Revit family type** (use *Layer* or *Name* selection filters), so re-links retain materials; keep a master `.max` that XREFs the linked scene so lighting/cameras stay separate.

## 3. Modeling for arch-viz

- Prefer **Edit Poly** + modifiers (Shell, Chamfer, Symmetry, Bevel Profile) with non-destructive stack; avoid collapsing until final.
- **Walls**: start from a clean 2D spline; extrude; add thickness; create openings by *Cut* / *Connect* edges on the wall (preferred for clean UVs) or **ProBoolean** for complex; model window frames/jambs, reveals (20-50 mm), skirtings, plinth - details sell realism.
- **Floors**: separate objects per material; floor boards via spline + array/RailClone; slab thickness visible at edges.
- **Edges**: Chamfer 1-3 mm on all exposed edges (use *Chamfer* modifier with `Angle threshold` 30 deg, or V-Ray/Corona **Rounded Edges** bump shader to fake it).
- **Glass**: model real thickness and frames; don't leave single planes unless "thin" glass in material (V-Ray: refract + thin-walled; Corona: Thin refraction).
- **Furniture**: Chaos Cosmos / quality assets; check scale (sofa seat 45 cm, dining table 75 cm, door 2.1 m, counter 90 cm, stairs rise 17-18 cm).
- Use **Instances** (`Alt+copy`) for repeating items; do not convert an instance to editable poly (breaks link; VizAcademy warns about this).
- Name objects consistently (`WALL_Ext_N`, `WIN_01`) and put them in Layers (Scene Explorer). Use *Select by Layer/Name* scripts.
- Mapping: **Real-World Map Size** checked in UVW Map and Bitmap coordinates (`Use Real-World Scale`) so 1 tile = actual size; choose UVW Map `Box` with Real-World Map Size for walls; `Planar` for floors; `Unwrap UVW` only for hero assets.
- Keep poly count for background; vegetation as proxies.

## 4. Materials (PBR) in V-Ray / Corona / Arnold

| Property | V-Ray (VRayMtl) | Corona (Physical Mtl) | Arnold (aiStandardSurface) |
|---|---|---|---|
| Base colour | Diffuse | Base colour | Base color |
| Reflection strength | Reflect colour + IOR (use "Fresnel" on, IOR 1.5) | Specular (IOR 1.5) | Specular weight/IOR |
| Gloss | Reflection Glossiness (1 sharp, 0 matte) or **Roughness** mode | Roughness (0 sharp; 1 matte) | Specular roughness |
| Metal | Metalness 0..1 (map as grayscale) | Metalness | Metalness |
| Normal | VRayNormalMap (Normal), Bump amount 1.0 default | Normal map (Physical Mtl) | Normal map via aiNormalMap |
| Displacement | VRayDisplacement or Displacement slot | Displacement slot (World Units) | Displace |
| Opacity | Opacity map | Opacity | Opacity |
| Glass | Refract colour white, IOR 1.52 | Refraction (Thin for windows) | Transmission |

Rules:
- Albedo bounds: 30-240 sRGB for diffuse (most surfaces 60-200). Pure white/black breaks GI.
- Reflection IOR: 1.5 dielectrics; 1.0 = no reflection. Don't crank reflection colour on non-metals.
- Fresnel: ON; roughness mapped; bump small (0.2-1.0).
- Use **Chaos Cosmos** or **Corona Material Library** as starting point; always re-check scale in the Slate.
- Common glossy materials: wood 0.5-0.7 gloss; plaster 0.1-0.2; polished stone 0.9; fabric 0.1 (use sheen).
- Use **VRay Dirt / Rounded Edges / Corona AO**: subtle contact shadows. Apply Mix with maps (grime, scuffs) for realism.
- Use texture sets (`color`, `roughness`, `normal`, `AO`). Normal maps: OpenGL vs DirectX flip green channel.
- Glass material for windows: set *Affect shadows* on, *Affect alpha* on; avoid heavy refraction depth (limit 8).
- Tile floors: Use *Tile* maps with grout via Multi-Tile (VRay) or **Corona Tile map** + random colours via **MultiMap** (by ID).

## 5. Lighting

### Sun + Sky (daylight exterior/interior)
- V-Ray: **VRaySun** + **VRaySky** (Environment slot; Max asks to add automatically), intensity multiplier 1.0, ozone/turbidity defaults 2.5-3.0. Place the sun so shadows fall at 30-45 deg for a pleasant look; use **Sun Position** (Light > Sunlight) for real orientation.
- Corona: **CoronaSun** + **CoronaSky** (or HDRI).
- Arnold: **Skydome light with Physical Sky** + **Distant light** (Sun) - or Arnold Sky shader.

### HDRI
- Use 8K+ HDRI for background/reflection; align rotation; set multiplier to match exposure; mix with sun if overcast.
- V-Ray: DomeLight with HDRI (rectangular), **Light Mix** for post control. Corona: Environment map HDRI + Corona Sun fine-tune.

### Interior lighting
- Use **portal lights** (V-Ray Light Plane with *Portal* option; Corona uses Interactive/Shadow-catcher/Interactive Portals) at windows.
- Use IES profiles for spot/downlights; real-lumen settings (2000 lm downlight). Temp 2700-3000 K interior; 5600 K daylight.
- Mesh lights for emissive strips; keep area lights proportional to geometry.
- Light mix (V-Ray) / Lightmix (Corona) lets you change colour, intensity of each source after render; requires **Progressive** image sampler.
- Avoid "fill" lights unless justified; use GI/bounce instead.

### Lighting settings checklist
| Step | V-Ray | Corona |
|---|---|---|
| GI | Brute Force + Light Cache (500-1000 subdivisions for preview) | Path Tracing + UHD Cache (default) |
| Bounces | Brute force depth 4-8 | max ray depth 25 |
| Clamp | none (use physical camera) | Highlight clamp 20-40 (if fireflies) |
| Noise limit | 0.01 for final (preview 0.05) | Noise level limit 3-5 (final), pass limit ~ 60-120 |
| Denoiser | Chaos denoiser (V-Ray) or NVIDIA OptiX (GPU) | Corona high-quality denoiser / Intel OIDN / NVIDIA OptiX |

## 6. Camera and exposure

Use the renderer's **physical camera** (VRayPhysicalCamera / Corona Camera modifier / Physical Camera in Max). Do not use Perspective view cameras with a default exposure.

| Setting | Exterior day | Interior day | Interior dusk | Notes |
|---|---|---|---|---|
| f-number | f/8-f/11 | f/5.6-f/8 | f/2.8-f/4 | Use tilt-shift/vertical shift instead of tilting up |
| Shutter | 1/125-1/250 | 1/30-1/60 | 1/8-1/15 | In V-Ray `shutter_speed` is 1/seconds |
| ISO | 100 | 200-400 | 800+ | Match exposure |
| White balance | Daylight 6500 K (or Custom ~5500-6500 K) | Neutral 6500 K | warm 4000 K | Avoid autocorrect hack |
| Focal length | 24-35 mm (wide arch) | 20-28 mm | | Use film width 36 mm (full frame) |
| Camera height | 1.2-1.7 m | 1.2-1.5 m | | Eye-level for exteriors (course tip) |
| Vertical shift | Use to keep verticals parallel | same | | Keeps camera level (no tilt) |
| Vignetting | 0.2-0.4 | | | Subtle |
| DOF | Off for interiors/ext, on for close-ups | | | Use sparingly |

Rules:
- Frame: rule of thirds; lead lines; show context; crop in 16:9 / 3:2 / 4:5 depending on use.
- Set **Safe Frame** (Shift+F) to see the render area.
- For exposures: start from "Sunny 16" for exteriors: f/16, 1/ISO, ISO 100 => 1/100 s (open aperture f/8 -> 1/400). Adjust with EV compensation, not light multipliers.
- Level horizon: camera pitch 0 deg; use Vertical Shift (Max Physical Camera `Shift`, V-Ray `vertical_shift`) to frame. Course tip: move camera target or use vertical shift instead of rotating the camera so lines stay vertical.
- Multiple cameras per project; save camera states; name cameras `CAM_Ext_01`.

## 7. Render settings

| Item | V-Ray (CPU/GPU) | Corona | Arnold |
|---|---|---|---|
| Engine | V-Ray Production (CPU) / V-Ray GPU (RTX) | Corona | Arnold (MAXtoA) |
| Image sampler | Progressive (needed for Light Mix) | Progressive | Camera (AA) 3-5 samples |
| Output | 2400-4000 px width for stills; 4K for print | | |
| Format | EXR (32-bit float) master; PNG/JPEG for delivery | | |
| Gamma | 2.2 linear workflow | | |
| Denoiser | V-Ray Denoiser render element, or NVIDIA | Corona denoiser | OptiX / Noice denoiser |
| Render elements | Lighting, Reflection, Refraction, Self-Illum, ZDepth, Cryptomatte, LightMix, Denoiser | Beauty, LightMix, Cryptomatte, ZDepth | AOVs: diffuse, specular, N, depth, Cryptomatte |

Practical sequence:
1. Draft: 640x360, noise limit 0.05; check lighting/exposure.
2. Medium: 1280x720; test materials with **Region render**.
3. Final: 3000+ px, noise limit 0.01 (V-Ray), denoise on, save EXR + PNG.
4. Use **Interactive/IPR** only for lighting; final in production.
5. Render to a network location and **Backburner/Deadline** for many stills.
6. Save `.vrscene` for distributed/cloud; for Corona use Chaos Cloud.

## 8. Vegetation, scatter, arrays, assets

| Tool | Use | Tips |
|---|---|---|
| Forest Pack (iToo) | Grass, trees, gravel, decor | Distribute on area; use *camera clipping* and LOD to save RAM; Convert to proxies; separate low/high |
| RailClone | Fences, facades, stairs, curtain walls, flooring | Parametric rules + splines; edit style once |
| Chaos Cosmos | Libraries of assets | Browser inside V-Ray; assets as proxies |
| Chaos Scatter | Native V-Ray scatter | Quick vegetation |
| Corona Scatter | Scatter | Similar |
| MultiScatter | Scatter legacy | |
| V-Ray Proxy (.vrmesh) / Corona Proxy | Heavy meshes | Instance-friendly |
| Itoo Anima/ AXYZ | Animated people | |
| Skydome HDRI | Backgrounds | Add foreground trees for depth |

Add foreground/midground/background elements to create depth: foliage plates, cars, people for scale; consistent shadows. Course tip (Corona exterior): use composition layers - camera first, then lights, then assets (trees/cars), then tone mapping and post.

## 9. Post-production

- Use **VFB** (V-Ray Frame Buffer / Corona VFB) corrections as non-destructive layers: exposure, white balance, curves, color balance, LUT, bloom/glare, vignette, sharpen/denoise (for tidy output).
- **Light Mix**: after render, re-balance sun vs sky vs interior lights vs emissive meshes without re-rendering (course demo: blur sky light, desaturate wood, curves for contrast, reduce highlight burn, add filmic tone map).
- Photoshop: load EXR via Camera Raw filter; adjust exposure, highlights/shadows; add slight grain; sharpen. Use Cryptomatte/Material ID masks for selective edits. Add people/cars/sky only if consistent in light; match perspective & shadows.
- Add subtle lens effects: bloom/glare 0.1-0.3, chromatic aberration small, vignette 0.1-0.3; never overdo.
- Colour: tint the shadows slightly cool, highlights slightly warm.
- Deliver: sRGB JPEG 85-92% for web; TIFF 16-bit for print; name with project/view/version.

## 10. Scripting basics: MAXScript / pymxs

### Access
- MAXScript Listener (F11), Python in Max: `from pymxs import runtime as rt`.
- `rt.execute("...")` evaluates a MAXScript string; the safest bridge for obscure commands.
- Max 2026: **`3dsmaxbatch.exe`** (headless MAXScript/Python) - run `3dsmaxbatch.exe -help` for flags; typical: `3dsmaxbatch.exe -sceneFile "C:\proj\scene.max" "C:\scripts\task.py"` (or `.ms`). Good for batch renders, exports, QA.
- Always wrap in undo: `with undo on` (MAXScript) or `with pymxs.undo(True):`.

### Units and scene (MAXScript)
```maxscript
units.SystemType  = #Millimeters      -- or #Meters; set BEFORE geometry (changes interpretation)
units.DisplayType = #Metric
units.MetricType  = #Millimeters
```
pymxs equivalent:
```python
from pymxs import runtime as rt
rt.units.SystemType  = rt.Name("Millimeters")
rt.units.DisplayType = rt.Name("Metric")
rt.units.MetricType  = rt.Name("Millimeters")
```

### Create wall box, assign material, instance
```python
import pymxs
from pymxs import runtime as rt
with pymxs.undo(True):
    w = rt.Box(length=5000, width=200, height=3000, name="WALL_N", pos=rt.Point3(0,0,0))
    m = rt.VRayMtl(name="Plaster_White")           # or rt.CoronaPhysicalMtl(), rt.ai_standard_surface()
    m.diffuse = rt.Color(210,210,205)
    m.reflection_glossiness = 0.15; m.reflection = rt.Color(40,40,40)   # introspect names with showProperties
    w.material = m
    inst = rt.instance(w); inst.pos = rt.Point3(6000,0,0)
```
Property names differ per renderer/version: use `showProperties $` (MAXScript) or `rt.showProperties(obj)` and `rt.showClass("VRay*")` to discover names. Do not guess.

### Camera + sun + sky
```python
cam = rt.VRayPhysicalCamera(name="CAM_Ext_01", pos=rt.Point3(8000,-8000,1500))
cam.target = rt.Targetobject(pos=rt.Point3(2500,0,1500))
cam.f_number = 8; cam.ISO = 100; cam.shutter_speed = 125     # 1/125; verify property names
cam.film_width = 36; cam.focal_length = 28                    # vertical shift: cam.vertical_shift
sun = rt.VRaySun(pos=rt.Point3(5000,5000,6000)); sun.target = rt.Targetobject(pos=rt.Point3(0,0,0))
rt.environmentMap = rt.VRaySky()                              # sky in environment slot
rt.useEnvironmentMap = True
```
Corona: `rt.CoronaSun()`, `rt.CoronaSky()`, camera via `rt.PhysicalCamera()` + `CoronaCameraMod` modifier.

### Real-world mapping / UVW
```maxscript
m = Uvwmap(); m.maptype = 4  -- box (index per docs)
m.realWorldMapSize = true
addModifier $WALL_N m
```
```python
b = rt.Bitmaptexture(filename=r"C:\tex\plaster_albedo.jpg"); b.coords.realWorldScale = True
rt.meditMaterials[1].diffuse_map = b       # property name depends on material class
```

### Renderer selection and render
```python
rt.renderers.current = rt.VRay()                 # or rt.Corona_Renderer(), rt.Arnold()
rt.rendOutputFilename = r"C:\out\ext_01.exr"
rt.rendSaveFile = True
rt.rendWidth, rt.rendHeight = 3000, 1688
rt.render(camera=cam, vfb=False)                 # blocking render
```
V-Ray class names have changed across versions (`V_Ray_6`, `VRay`, `V_Ray_GPU`). Check with `rt.showClass("V_Ray*")` and `rt.renderers.current.classID`. Arnold: `rt.showClass("*Arnold*")` and `rt.showClass("ai*")` for materials (`ai_standard_surface`), lights (`Arnold_Light`). **This host has Arnold (MAXtoA)**: use Arnold unless the task requires V-Ray/Corona; Arnold's Physical Sky + Distant light + Physical Camera cover most exteriors.

### Utility snippets
```maxscript
-- select by layer, hide, count
for o in objects where o.layer.name == "LANDSCAPE" do hide o
format "% objects, % cameras\n" objects.count cameras.count

-- rename all geometry with prefix
for o in geometry do o.name = "ARCH_" + o.name

-- batch convert to editable poly, skipping instanced objects (converting breaks instance links)
for o in selection do (
    local arr = #()
    InstanceMgr.GetInstances o &arr
    if arr.count <= 1 do convertToPoly o     -- count includes o itself
)

-- save increments
saveMaxFile (maxFilePath + "scene_v" + (timeStamp() as string) + ".max")
```

## 11. 3dsmax-mcp (github.com/cl0nazepamm/3dsmax-mcp)

- Windows-only; Max **2023-2027**; install via the `3dsmax-mcp` Setup `.exe` or source (`uv sync`, `uv run python install.py`); close Max and AI client first. Native bridge to Max.
- ~160 tools. Groups: scene (`query_scene`, `scene_qa`, `scene_patch`, `get_hierarchy`, `get_instances`, `get_dependencies`), objects (`create_object`, `delete_objects`, `transform_object`, `clone_objects`, `set_parent`, `add_modifier`, `set_modifier_property`), modeling (`create_mesh`, `mesh_edit`, `loft_mesh`, `boolean_operation`, `geometry_qa`), materials (`assign_material`, `create_material_from_textures`, `batch_replace_materials`, `smart_import`), render/view (`capture_viewport`, `render_scene`, `create_lights`, `lighting_capabilities`), scripting (`execute_maxscript`, `execute_python`), plus tyFlow, MCG, RailClone, Forest (WIP).
- `execute_python` is blocked in **safe mode**, and rolls back undo on failure. `execute_maxscript` respects safe mode; scripts that reset/open/quit keep the save prompt.
- Workflow pattern:
  1. `get_bridge_status` / `get_session_context` -> confirm units, renderer, version.
  2. `lighting_capabilities` -> which renderer lights exist.
  3. Build/transform in small tool calls; verify with `scene_qa` + `capture_viewport`.
  4. Use `render_scene` at low res first; then iterate.
  5. Use `execute_maxscript` / `execute_python` only when no dedicated tool covers it.
- Always check the renderer class and units before creating geometry: wrong unit = 1000x error.

## 12. Pipeline checklist (exterior example)

1. Units & project folder -> import CAD/SketchUp/Revit (linked) -> verify dimensions with `Tape`.
2. Clean & model: walls with thickness, glazing, roofs, ground plane; real-world UVs.
3. Camera: 1.2-1.7 m, 24-35 mm, vertical shift, composition; set render aspect.
4. Lighting: Sun + Sky/HDRI -> check exposure with physical camera.
5. Materials: Cosmos/library -> real scale; adjust albedo; add dirt/edge wear.
6. Entourage: trees (Forest/Cosmos proxies), people, cars, foreground plants.
7. Test render, noise check, fix fireflies (clamp, material issues).
8. Final render EXR + render elements + denoise.
9. Post: Light Mix, tone map, Photoshop touch-ups, export.
10. Archive: `.max` + assets (Resource Collector); keep a dated version.

## 13. Common errors and fixes

| Symptom | Cause | Fix |
|---|---|---|
| Everything huge/tiny after import | Unit mismatch | Reimport with right units; `Rescale World Units` utility only as last resort |
| Blown out / too dark render | Using 3ds Max exposure control and physical lights wrongly | Use physical camera; set exposure via ISO/shutter/f-stop |
| Fireflies | Small bright lights + glossy materials | Increase reflection roughness, avoid tiny emissive, clamp, more samples |
| Blotchy interior GI | Light cache too low / portals missing | Add portals; raise subdivisions; use brute force |
| Noise in glass | Refraction depth; thin glass | Use thin-walled, reduce IOR issues, denoise |
| Textures stretch | No UVs / box-map mismatch | Real-world UVW Map per surface |
| Slow viewport | Heavy mesh/vegetation | Proxies, display as box/point cloud |
| Crash on render | Out of RAM | Proxies, lower texture res, 64-bit bitmaps off; render per layer |
| Light Mix greyed out | Image sampler isn't Progressive | Switch to Progressive |
| Instances lost | Convert/Collapse | Keep instances; edit master |

## Sources

Course transcripts and docs consulted:
- Arch Viz Artist, "Exterior Architectural Visualization in V-Ray 6 & 3ds Max" - https://www.youtube.com/watch?v=ZoaNAjByW_U
- VizAcademy UK, "From Zero to Hero - Exterior modeling" - https://www.youtube.com/watch?v=h7CSgx2ByzI
- SWK Insights, "V-Ray 6 for 3ds Max Complete Course" - https://www.youtube.com/watch?v=yf-iIjFCebI
- Simple or Difficult, "Corona Render Exterior Tutorials for Beginners" - https://www.youtube.com/watch?v=Se8bJzuWEi8
- Autodesk 3ds Max MAXScript / Python API help - https://help.autodesk.com/view/3DSMAX/2026/ENU/
- Chaos V-Ray / Corona docs - https://docs.chaos.com/
- 3dsmax-mcp - https://github.com/cl0nazepamm/3dsmax-mcp
