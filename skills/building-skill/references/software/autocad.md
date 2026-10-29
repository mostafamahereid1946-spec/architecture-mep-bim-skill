# AutoCAD (2D drafting) - professional practice and automation

Scope: AutoCAD vanilla / LT 2D drafting of architectural + general documentation, and how Claude drives it (AutoLISP, .NET, .scr, COM, ezdxf, MCP).
Rule of thumb: **geometry is drawn full size in model space; paper space only holds viewports, title block, and plot-scale annotation.** Almost every beginner/AI error is a violation of that sentence.

---
## 1. Setup before the first line (do it once in a .dwt, then never again)

| Item | Pro setting | Why / how |
|---|---|---|
| Units | Architectural metric: 1 drawing unit = 1 mm (buildings), 1 m (site/civil). Imperial: 1 unit = 1 in. `UNITS` + `INSUNITS` (blocks/xrefs scale on insert based on INSUNITS) | Mixed units are the #1 cause of "block is 1000x too big" |
| Precision | Length precision 0 (mm) or 0.00 (m); angle 0.00 | Display only, geometry keeps full precision |
| Template | Start from `acadiso.dwt` (metric) or `acad.dwt` (imperial) only to build own `.dwt`; save as `OFFICE-A1-MM.dwt` via `SAVEAS > AutoCAD Drawing Template`. `QNEW` uses default template (Options > Files > Template Settings) | Template carries layers, styles, layouts, title block, scale list |
| Limits/grid | Ignore LIMITS. Turn grid off. Use `ZOOM E` | Limits are obsolete in practice |
| Drafting aids | F8 ortho or polar 15/30/45/90, OSNAP: End, Mid, Int, Cen, Perp; F3 on; dynamic input off (many pros) | Never draw by eyeballing; wrong points are the main accuracy defect |
| Variables | `FILEDIA=1`, `CMDECHO=0` (scripts), `PICKFIRST=1`, `HPLAYER`/`CLAYER` set before hatching, `OSNAPCOORD=1`, `SAVETIME=10`, `LAYLOCKFADECTL=-50`, `PLINEGEN=1` | Reproducible behaviour for scripts |
| File format | Save as AutoCAD 2018 DWG (AC1032) for exchange; DXF only for non-Autodesk tools. Default DXF R12 loses everything | `SAVEAS` file type |

## 2. Layers, linetypes, lineweights

- **Naming standard** (pick one, never invent ad hoc): AIA/NCS `A-WALL`, `A-DOOR`, `A-GLAZ`, `A-FLOR-STRS`, `A-ANNO-DIMS`, `A-ANNO-TEXT`, `A-ANNO-NPLT` (non-plot), `A-GRID`; discipline letters `A`,`S`,`M`,`E`,`P`,`C`,`L`. ISO 13567 / BS 1192 (UK) or office standard: `Role_Element_Presentation`. Arabic/GCC projects usually follow client or consultant standard - ask for their layer standard file.
- Layer `0` and `Defpoints` stay empty: layer 0 is only for **block definitions** (so blocks inherit the insertion layer). `Defpoints` never plots - don't draw on it.
- Everything **ByLayer** (color, linetype, lineweight, transparency). Never override per entity. Check with `SETBYLAYER`, `LIST`.
- Use plot weights from a limited set (ISO: 0.13, 0.18, 0.25, 0.35, 0.50, 0.70, 1.00 mm): cut elements heavy (0.50-0.70), edges beyond cut medium (0.25-0.35), finishes/hatch/dims light (0.13-0.18), grids/center lines thin dash-dot.
- Linetypes: `CONTINUOUS`, `HIDDEN`, `CENTER`, `DASHDOT`, `PHANTOM`, `DASHED` (ISO versions in `acadiso.lin`: `ACAD_ISO02W100`...). Load with `-LINETYPE L CENTER acadiso.lin`.
- Layer states (`LAYERSTATE`/`LAS`) for views per sheet; `LAYMCH`, `LAYISO`, `LAYUNISO`, `LAYWALK`, `LAYFRZ`. Freeze > off for performance. Per-viewport freeze: `VPLAYER` or Layer Manager "VP Freeze".
- Filters: Layer Properties Manager > Group filters (e.g. "Walls"). Use Layer State to save/restore, don't hand-toggle across 60 layers.
- Don't leave 0 length lines, duplicate overlapping lines, or off-layer stragglers: `OVERKILL`, `PURGE` (all + nested), `AUDIT`, `-OVERKILL`.

## 3. Linetype scale (the thing everyone gets wrong)

| Variable | Meaning | Recommended |
|---|---|---|
| `LTSCALE` | global multiplier for linetype patterns (pattern lengths are in drawing units) | Non-annotative mm drawing: = plot-scale denominator (1:50 -> 50) so a 12 mm paper dash stays 12 mm. Annotative workflow with `MSLTSCALE=1`: leave at `1`. Tune by plot preview |
| `MSLTSCALE` | 1 = model-space linetypes follow the annotation scale | `1` |
| `PSLTSCALE` | 1 = paper-space linetype scale independent of viewport zoom | `1` (so lines look identical on every sheet) |
| `CELTSCALE` | per-new-object multiplier | keep `1` |
| `PLINEGEN` | linetype pattern continuous along whole polyline | `1` |
- Symptom "dashed line plots solid": scale too small relative to geometry. "One huge dash": too large. Fix scale not the line. Run `REGEN`/`REGENALL` after changing.
- Test by plotting preview at the final scale, not by eye on screen.

## 4. Text, dimensions, scaling (annotative vs fixed)

**Choose one method per drawing and state it in the template:**
| Method | Text height | DIMSCALE | Pros | Cons |
|---|---|---|---|---|
| Non-annotative (classic) | `paper_height x plot_scale_denominator` (2.5 mm @ 1:100 = 250) | = scale denominator (100) | Simple, bulletproof in xrefs/scripts | One scale per drawing region; separate dimstyle per scale |
| Annotative | paper height (2.5) - AutoCAD multiplies by `ANNOSCALE` | `0` effect; dimstyle flagged annotative | Multi-scale details in one model, viewport scale drives size | Annotation scale lists multiply objects; xref of annotative fine, but scripted creation must set `ANNOSCALE` first |
(The freeCodeCamp university course tells students not to tick "Annotative" in a single-scale project and to use it only on larger multi-scale projects - follow that: do not enable annotative unless you will use several viewport scales.)

- Standard text heights on paper: notes 2.5 mm, titles 3.5-5, sheet title 7. Minimum plotted text 2.0 mm for legibility.
- **Text styles**: define `STANDARD-NOTES`, `TITLE`, `DIM`. Height `0` in the style (so `TEXT` asks / dimstyle sets it); width factor 1.
- **Arabic / RTL / non-Latin**: use **TrueType Unicode fonts** (Arial, Tahoma, Segoe UI, Simplified/Traditional Arabic, Cairo/Noto Naskh if installed on every machine). SHX/BigFont (`txt.shx`, `simplex.shx`) do **not** contain Arabic glyphs -> shows `????`. Use **MTEXT** (handles bidi/shaping); the single-line `TEXT` command is unreliable for mixed Arabic/Latin. Keep numbers/dimension text in Latin digits unless the client demands Eastern Arabic-Indic digits. Embed/ship the font (eTransmit includes fonts). Text style file name must be the TTF (`arial.ttf`).
- Annotation of mixed-language sheets: separate text styles per language (`TXT-EN`, `TXT-AR`) so one can be changed without the other; right-align Arabic MTEXT (justification `TR`, attachment; set paragraph direction in the MTEXT ribbon).
- **Dimstyle recipe (architectural metric)**: Units: decimal, precision 0, suppress trailing zeros; Arrows: `Architectural tick` (or closed filled 2.5), arrow size 2.0; Extension line: offset from origin 2 (paper), extend beyond 2; Text: height 2.5 (paper), above dim line, ISO alignment; Fit: "Use overall scale" = scale denominator for non-annotative. Create `DIM-100`, `DIM-50`, `DIM-20` (or one annotative). Dimension in **chains** with `DIMCONTINUE`/`DIMBASELINE`; keep 3 string levels: overall, grid-to-grid, openings. `DIMASSOC=2` (associative). **Never type over dimension text or explode dimensions.**
- Leaders: `MLEADER` with its own style (`MLEADERSTYLE`), annotative if text is. Use `QLEADER` only for legacy.
- Fields: `FIELD` for sheet number, date, filename, area (`Object` field on a polyline closed area -> room areas that update).
- Spelling: `SPELL`. Find/replace text: `FIND`. Text align: `TEXTALIGN`, `TEXTFIT`.

## 5. Model space vs paper space; viewports

- **Model**: 1:1 geometry, no title block, no scale text boxes, no frames. Place plan, sections, elevations, details **spaced apart** in model space (e.g., 10 m gaps) or in separate DWGs xref'd together.
- **Paper (Layouts)**: one layout per sheet. `PAGESETUP` (plotter, sheet size A1 = 841x594 mm, plot area Layout, scale 1:1, plot style table, lineweights on). Title block inserted at 0,0 at 1:1 (as a block with attributes).
- **Viewports**: `MVIEW`; set scale via `VPSCALE` or the viewport scale bar; **lock** it (`Display locked = Yes`) the moment it's set. Viewport frames on layer `A-ANNO-VPRT` with **plot = No** (don't use `Defpoints`). Non-rectangular via `MVIEW > Object/Polygonal`, clip with `VPCLIP`.
- Per-viewport layer control (`VPLAYER`/ VP Freeze), per-viewport visual style. Detail at larger scale: second viewport, different scale, same model.
- Scale list: `SCALELISTEDIT` -> reset to include 1:5,1:10,1:20,1:25,1:50,1:75,1:100,1:200,1:500 only; `-SCALELISTEDIT R Y` to reset.
- Never draw dimension/text in paper space except for sheet-specific notes (north arrow scale-less, general notes).
- Annotation pro tip: type `MSPACE` / `PSPACE` instead of double-clicking in scripts. `MVSETUP` is legacy.
- `TILEMODE`/`CTAB` for switching layouts in scripts.

## 6. Xrefs

| Rule | Detail |
|---|---|
| Use xrefs for: base plan reused in sections/elevations, site plan, grids, consultant backgrounds, title block library | Avoid copy/pasting between drawings |
| Attach type | **Attachment** for work you pass on; **Overlay** for backgrounds you don't want nested (no circular references) |
| Path | **Relative** path, same project folder structure; never absolute `C:\Users\...` (breaks when zipped). `XREF` palette > right-click > Change path type |
| Insertion | Insertion at 0,0,0, scale 1, rotation 0 (shared origin = coordination). Use `UNITS` match: `INSUNITS` mismatch causes scaling |
| Layer control | `VISRETAIN=1` keeps xref layer overrides; `XREFFADE` 50% for backgrounds; `XCLIP` to hide unneeded areas; layer names appear as `xrefname|A-WALL` |
| Bind | `XREF > Bind` with **Insert** (not Bind) so layers don't become `xref$0$A-WALL` |
| Lifecycle | `XREF > Reload`, `-XREF` in scripts, `Detach` stale ones; `RELOAD` before plotting, unload for performance |
| Hand-over | `ETRANSMIT` / `ARCHIVE` bundles DWG + xrefs + fonts + plot styles + images into ZIP with relative paths |
- `DWGUNDERLAY`, `PDFATTACH`, `IMAGEATTACH`: underlays for scanned survey/PDF plans; calibrate with `ALIGN`/`SCALE R` and name the file; lock the layer.
- `OPENDWG`/`INSERT` of DWG as block = copy not link; changes won't propagate.

## 7. Blocks, attributes, dynamic blocks

- **Create on layer 0, ByBlock/ByLayer** properties; insertion point at a meaningful snap (door hinge, column center); INSUNITS set; "Allow exploding" only when needed; description filled; units = Millimeters.
- Names: `A-DOOR-SINGLE-900`, `A-FURN-BED-DBL`, `E-SYM-SOCKET`. No spaces, no `Block1`.
- `BLOCK` (local) vs `WBLOCK` (to file, used for library). Insert via Tool Palettes/DesignCenter/`INSERT`. Library in a shared folder + **Tool Palette** for reuse; `BLOCKSPALETTE` in 2020+.
- **Attributes**: `ATTDEF` (Tag, Prompt, Default), `ATTSYNC` after redefining; `BATTMAN` to reorder/edit; `ATTEDIT` single. Extract to table/CSV: `DATAEXTRACTION` / `EATTEXT` (feed door/window/schedule tables). Title blocks use attributes + fields.
- **Dynamic blocks** (Block Editor `BEDIT`): parameters (Linear, Point, Rotation, Visibility, Flip, Lookup, Alignment, Base) + actions (Stretch, Move, Array, Scale, Rotate, Flip, Lookup). Use for doors (width stretch + swing flip), windows, furniture variants. Visibility states = one block for 6 sizes. Test with `BTESTBLOCK`. Add `Constraints` (geometric + dimensional) for parametric fit. Save sizes list via Block Properties Table.
- Don't: nest 6 levels, use annotative text inside blocks without checking, put hatches that need to scale.
- `BCOUNT` counts blocks (QTY takeoff); `COUNT` command (2022+) for quick quantity. `QSELECT` + `-PURGE` for cleanup.
- Replace a block everywhere: redefine via `INSERT` same name + `=`, or `BLOCK` redefine; `BLOCKREPLACE` (2024+).

## 8. Hatches, patterns, polylines

- Hatch only **closed** loops; `HPGAPTOL` for small gaps; associative on; `HPLAYER` set to hatch layer (`A-WALL-PATT`, `A-FLOR-PATT`). Pattern scale = tied to drawing scale; use annotative hatch only when multi-scale. Prefer `SOLID`/`ANSI31`/`AR-CONC` (metric: ISO patterns). `HATCHGEN` at 1: hatch origin consistent (`HPORIGIN`).
- Use closed **polylines** (`PLINE`, `PEDIT J`) for room outlines, walls, slabs (area queries via `AREA O`, `MEASUREGEOM`). Avoid 2D `MLINE` for walls (not editable at junctions); common pro method: wall centerlines/grid -> `OFFSET` both sides -> `FILLET 0` / `TRIM` junctions; or wall as closed `PLINE` + hatch.
- `BOUNDARY` creates closed polylines from areas, `REGION` for booleans, `OVERKILL` to merge colinear.
- Tolerances: gaps < 0.1 mm; `FILLET 0` instead of `EXPLODE` + trim.

## 9. Sheet Set Manager (SSM) + title block fields

- `SHEETSET` / `NEWSHEETSET`: create `.dst` from template; Subsets (`A-100 Plans`, `A-200 Elevations`...). Sheets are layout-linked; Properties: project name, number, client, issue date, sheet title, sheet number. Title block holds **fields** bound to Sheet Set properties and attributes, so renumbering updates automatically.
- Label block for viewports (title + scale) and Callout blocks (`Section`, `Elevation`, `Detail`) hyperlinked to sheet views, pulling `Sheet Number`/`View number`. Place with `Resource Drawings` palette.
- Sheet List Table (`SHEETLIST`) auto-generates the drawing index; update with `-SHEETSETLIST`.
- **Publish**: Right-click sheet set > Publish > DWF/PDF/Plotter; `PUBLISH` for batch; set Plot Stamp; "Publish in background" off for scripting (`BACKGROUNDPLOT=0`). `ARCHIVE` the set for handover; `ETRANSMIT` for single DWG. Revision cloud: `REVCLOUD`, revision table in title block via fields.
- Revision / issue: keep issued PDFs and a status code per sheet (P01 preliminary, C01 construction; ISO 19650 naming for filenames).

## 10. Plotting

| Topic | Pro practice |
|---|---|
| CTB vs STB | **CTB** (color-dependent): pen weights per ACI color - simplest, but forces color = weight; **STB** (named): weights assigned per plot style on layers - needed with true-color/layer-controlled weights. `PSTYLEPOLICY=1` (CTB for new) / `0` (STB). Do not mix inside one project; set `PSTYLEPOLICY` in template and attach table in `PAGESETUP` |
| Weights | Set `lineweight` by layer and plot style "Use object lineweight"; or CTB with pen table (screening 100%, color 7 black) |
| Plotter | `DWG To PDF.pc3` or `PublishToWeb PNG`; custom `Paper size` A1 (594x841) landscape no margin; `PLOTTRANSP=0` |
| Scale | 1:1 on the layout; 1:n only when plotting model tab. Check "Plot with lineweights", "Plot object lineweights", "Plot paper space last" |
| Output | Fit by *Layout*, plot area = Layout/Window/Extents (Layout for sheets), center the plot, offset 0 |
| PDF | `EXPORTPDF` with vector quality, merge layers (`PDFLAYERS`), embed TrueType (Arabic needs this), include bookmarks; `PDFSHX=1` for SHX searchable text |
| Verify | Open PDF, zoom 400% on thin lines/text, check fonts (no `?`), check weights, check ISO scale with scale bar. Add a graphic scale bar - never rely only on text "1:100" |
| Batch | `-PLOT` (script) or `PUBLISH` list `.dsd`; set `BACKGROUNDPLOT=0`, `FILEDIA=0` |

## 11. Professional workflow: floor plan -> sections -> elevations -> sheets

1. **Brief & survey**: confirm units, coordinate origin, north, level datums (FFL +0.00), area programme, site constraints. Attach site/survey as xref/underlay; scale-check with a known dimension.
2. **Setup**: new drawing from office `.dwt`; save immediately; layers already there; set ANNOSCALE / DIMSTYLE; add project info.
3. **Grid first**: draw column/structural grid on `A-GRID` with `XLINE`/ `LINE` + circle bubble block with attribute (grid ID). Grid is the base of all dimensions.
4. **Plan per level (separate DWG per floor, or one file with level blocks)**: walls from grid (offset thickness), trim/clean junctions, openings (cut wall, insert door/window dynamic blocks at correct swing), stairs (riser count x riser, tread: 2R+T = 600-640 mm), columns, shafts, sanitary, furniture; rooms as closed polylines for area fields; hatch cut walls (poche) heavy, thin finishes.
5. **Stagger plans vertically** in model (or xref ground-floor as underlay so stairs/shafts align across levels); keep a common origin.
6. **Sections**: choose cut line on plan (`A-ANNO-SECT` with section symbol block and view direction). Draw the section **from the plan by projecting**: `XLINE` verticals from plan edges, heights from schedule (floor-to-floor, slab thickness, parapet) horizontal lines on same layers. Cut elements (walls, slabs) thick/hatched; elements beyond thinner. Add level markers (FFL, SSL, FFE blocks with attribute). Alternative when 3D model exists: `SECTIONPLANE` + `LIVESECTION`/`FLATSHOT` -> block, then clean up.
7. **Elevations**: project openings/heights from plan + section with `XLINE`/ ray; fill with materials (hatch) at light weight; ground line heavy; show levels, material tags, door/window marks.
8. **Details**: draw at 1:1 in model, place in separate area; scale in viewport 1:5/1:10; reuse blocks (insulation, DPC) from library.
9. **Annotation**: dimensions (overall -> grid -> openings), room names/numbers/areas (fields), door/window tags tied to `DATAEXTRACTION` schedule, notes (keynotes), north arrow, scale bar.
10. **Sheets**: build in SSM: title block -> viewport(s) -> lock scale -> layer state per viewport -> viewport titles -> revision cloud. Sheet numbering by discipline (A-101 plans, A-201 sections, A-301 elevations, A-501 details).
11. **QA checklist**: `PURGE` + `AUDIT` + `OVERKILL`; no entities on layer 0/Defpoints (except blocks); no ByColor overrides; no "0 length" objects; no text `?`; layer state per sheet; xrefs relative; `XREF` all found; plot-preview each sheet; PDF check.
12. **Issue**: `ETRANSMIT` DWG set + PDF; filename convention `PROJECT-ORIGINATOR-LEVEL-TYPE-ROLE-NUMBER-REV`.

## 12. Driving AutoCAD from code (Claude's options)

| Route | Needs AutoCAD? | Best for | Notes |
|---|---|---|---|
| **ezdxf** (Python, offline DXF/DWG-lite) | No | Generate/inspect DXF with layers, blocks, dims, MTEXT, layouts, viewports | `pip install ezdxf`; can't plot/render DWG natively (DWG needs ODA File Converter); `ezdxf.addons.drawing` renders PNG/PDF |
| **`.scr` script via `accoreconsole.exe`** | Yes (Core Console, no UI) | Batch plot/purge/convert/layer ops over many DWGs | no GUI commands (no dialogs, no palettes); use `-` command variants |
| **AutoLISP (`.lsp`)** | Yes (not Mac LT) | Fast custom commands, entmake, selection sets | LT 2024+ supports limited AutoLISP, no `vl*`/ActiveX/file IO |
| **.NET (`acdbmgd.dll`, `accoremgd.dll`, `acmgd.dll`)** | Yes (full AutoCAD) | Plug-ins, complex logic, Palette/UI | 2025+ targets .NET 8; 2024 and earlier .NET Framework 4.8 |
| **COM/ActiveX (pywin32)** | Yes, running | Python control of a live session | Windows only; deprecated-ish but works; retry on `RPC_E_CALL_REJECTED` |
| **MCP servers** | Either | Chat-driven drafting | See section 14 |

### 12.1 ezdxf: layered, unit-correct starter (runnable)
```python
import ezdxf
from ezdxf import units
doc = ezdxf.new("R2018", setup=True)      # loads std linetypes/text/dim styles
doc.units = units.MM                        # sets $INSUNITS
doc.header["$MEASUREMENT"] = 1              # metric
doc.header["$LTSCALE"] = 1
for name, aci, lw, lt in [("A-WALL", 7, 50, "Continuous"), ("A-GRID", 1, 13, "CENTER"),
                          ("A-ANNO-DIMS", 3, 18, "Continuous"), ("A-ANNO-TEXT", 7, 18, "Continuous")]:
    doc.layers.add(name, color=aci, lineweight=lw, linetype=lt)
doc.styles.add("ARABIC", font="arial.ttf")  # TrueType: Arabic-capable
msp = doc.modelspace()
msp.add_lwpolyline([(0,0),(6000,0),(6000,4000),(0,4000)], close=True, dxfattribs={"layer": "A-WALL"})
msp.add_mtext("غرفة المعيشة", dxfattribs={"layer": "A-ANNO-TEXT", "style": "ARABIC",
              "char_height": 250, "insert": (3000, 2000), "attachment_point": 5})
doc.saveas("plan.dxf")
```
(char_height 250 = 2.5 mm paper at 1:100.)

### 12.2 ezdxf: dimension with scale-aware style + sheet layout + viewport
```python
doc.dimstyles.new("ARCH_100", dxfattribs={"dimtxt": 2.5, "dimscale": 100, "dimasz": 2.0,
                                          "dimexe": 2, "dimexo": 2, "dimdec": 0, "dimtxsty": "Standard"})
msp.add_linear_dim(base=(0, -500), p1=(0, 0), p2=(6000, 0), dimstyle="ARCH_100",
                   dxfattribs={"layer": "A-ANNO-DIMS"}).render()
lay = doc.layouts.new("A1-101")
lay.page_setup(size=(841, 594), margins=(10, 10, 10, 10), units="mm")
lay.add_viewport(center=(420, 297), size=(800, 560), view_center_point=(3000, 2000), view_height=56000)
# view_height = viewport paper height (560) x scale denominator (100)
doc.saveas("plan_sheet.dxf")
```

### 12.3 Verification step (always run after generating)
```python
import ezdxf
from ezdxf import bbox
doc = ezdxf.readfile("plan_sheet.dxf")
auditor = doc.audit(); print("errors:", len(auditor.errors), "fixes:", len(auditor.fixes))
ext = bbox.extents(doc.modelspace()); print("extents:", ext.extmin, ext.extmax, "size:", ext.size)
print({l.dxf.name for l in doc.layers})
```
Render for visual check: `ezdxf.addons.drawing` with matplotlib backend -> `fig.savefig("preview.png", dpi=200)`. Look at the picture; do not trust success code alone.

### 12.4 AutoLISP (works in full AutoCAD and LT 2024+)
```lisp
(defun c:MKLAYERS ( / l)
  (foreach l '(("A-WALL" 7 "Continuous") ("A-DOOR" 2 "Continuous") ("A-ANNO-DIMS" 3 "Continuous"))
    (if (not (tblsearch "LAYER" (car l)))
      (entmake (list '(0 . "LAYER") '(100 . "AcDbSymbolTableRecord") '(100 . "AcDbLayerTableRecord")
                     (cons 2 (car l)) '(70 . 0) (cons 62 (cadr l)) (cons 6 (caddr l))))))
  (princ "\nLayers ready.") (princ))
```
Rules: wrap in `defun c:NAME` for command; always `(princ)` last; use `entmake` over `command` (no prompt dependence); `(setvar "CMDECHO" 0)` while calling `command`; use `command-s` in newer AutoCAD for stability; save/restore `OSMODE` (`(setq old (getvar "OSMODE")) (setvar "OSMODE" 0) ... (setvar "OSMODE" old)`); handle errors with `*error*`.

### 12.5 .NET (C#) command
```csharp
using Autodesk.AutoCAD.ApplicationServices; using Autodesk.AutoCAD.DatabaseServices;
using Autodesk.AutoCAD.Runtime; using Autodesk.AutoCAD.Colors;
public class Cmds {
  [CommandMethod("MKLAYER")]
  public void MkLayer() {
    var doc = Application.DocumentManager.MdiActiveDocument;
    using (doc.LockDocument())
    using (var tr = doc.TransactionManager.StartTransaction()) {
      var lt = (LayerTable)tr.GetObject(doc.Database.LayerTableId, OpenMode.ForRead);
      if (!lt.Has("A-WALL")) {
        lt.UpgradeOpen();
        var r = new LayerTableRecord { Name = "A-WALL", Color = Color.FromColorIndex(ColorMethod.ByAci, 7) };
        lt.Add(r); tr.AddNewlyCreatedDBObject(r, true);
      }
      tr.Commit();
    }
  }
}
```
Build as class library referencing `accoremgd.dll`, `acdbmgd.dll`, `acmgd.dll` (Copy Local = False); load with `NETLOAD`. Always use transactions; dispose; `LockDocument()` when called from palettes/modeless code.

### 12.6 Script (.scr) + headless batch
```
; setup.scr  - one token per Enter; blank line = Enter; no spaces inside names
FILEDIA 0
CMDECHO 0
-LAYER
M A-WALL
C 7 A-WALL
LW 0.5 A-WALL

-PURGE
A
*
N
ZOOM E
QSAVE
```
Run: `"C:\Program Files\Autodesk\AutoCAD 2025\accoreconsole.exe" /i "C:\work\plan.dwg" /s "C:\work\setup.scr" /l en-US`
Script rules: leading `_` for language-independent commands; `-` form to suppress dialogs; end every sub-prompt with a blank line; comments start `;`; a trailing space = Enter; script stops on error silently -> log with `/l` output and verify result.

### 12.7 COM (Python, live session)
```python
import win32com.client, pythoncom
from win32com.client import VARIANT
acad = win32com.client.Dispatch("AutoCAD.Application")
doc = acad.ActiveDocument
pt = lambda *c: VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, c)
line = doc.ModelSpace.AddLine(pt(0,0,0), pt(5000,0,0)); line.Layer = "A-WALL"
doc.SendCommand("_.ZOOM _E ")
```

## 13. Pro vs beginner/AI error table (common mistakes)

| Mistake | Consequence | Pro fix |
|---|---|---|
| Wrong/unknown units, mixed m/mm | Everything 1000x off, blocks scale wrong | Fix at template: `INSUNITS`, draw in mm; `SCALE R` against a known length |
| Everything on layer 0 / ByColor | Cannot control plot, no filtering | Layer standard + ByLayer; layer 0 only for block definitions |
| Drawing at paper scale (e.g. 1:100 geometry shrunk) | Dimensions/blocks nonsense, can't xref | Always full size; scale in viewport |
| Exploded dimensions, typed-over dim text | Values lie after edits | Use dimstyle overrides, `DIMASSOC=2` |
| Text height guessed per object | Inconsistent plot sizes | Styles with fixed paper heights; annotative or scale-multiplied |
| SHX font for Arabic | `????` text | TrueType + MTEXT |
| Annotative ticked on single-scale project | Dims grow/shrink strangely | Decide method up front |
| LTSCALE wrong / PSLTSCALE 0 | Solid lines, inconsistent dashes | MSLTSCALE=1, PSLTSCALE=1, LTSCALE per section 3 |
| Viewport scale unlocked | Scale changes on zoom | Lock; viewport on non-plot layer |
| Title block copied per sheet with typed text | Stale info | Attributes + fields + SSM |
| Absolute xref paths, `Bind` instead of Insert | Missing xrefs/`xref$0$` layers | Relative path, Insert bind, ETRANSMIT |
| Block drawn with colors/layers | Wrong colors when inserted | Layer 0 + ByBlock |
| Duplicates/overlaps from copy-paste | Heavy plotted lines, wrong quantity | `OVERKILL`, check `LIST` counts |
| Open polylines hatched | Hatch fails / leaks | Close, `HPGAPTOL`, `BOUNDARY` |
| Not plotting to check | PDF errors found by client | Plot preview, view at final scale |
| DXF R12 / old format default | Loses lineweights, Unicode, dims | R2018, `ezdxf.new("R2018")` |
| Trusting script success | Silent failure | Re-read drawing (ezdxf audit, `LIST`, render PNG) |
| No purge / audit before issue | Bloated, corrupt files | `-PURGE A * N`, `AUDIT Y`, `RECOVER` |
| Using `EXPLODE` on blocks/xrefs to "fix" | Loses data and structure | Edit block in `BEDIT`; XCLIP; layer overrides |
| Not setting sheet North/orientation | Wrong site orientation | North arrow block at project north; `UCS` for rotated plans, not rotated geometry |

## 14. MCP servers for AutoCAD
**puran-water/autocad-mcp** (github.com/puran-water/autocad-mcp)
- 8 tools: `drawing` (create/open/save/save_as_dxf/plot_pdf/purge/get_variables), `entity` (create_line/circle/polyline/rectangle/arc/ellipse/mtext/hatch; list/count/get; copy/move/rotate/scale/mirror/offset/array/fillet/chamfer/erase), `layer`, `block` (insert, attributes, define), `annotation` (text, dimension types, leader), `pid` (P&ID symbols), `view` (zoom, screenshot), `system` (status, execute_lisp).
- Backends via `AUTOCAD_MCP_BACKEND`: `auto` | `file_ipc` (live AutoCAD LT 2024+ on Windows, via `mcp_dispatch.lsp` loaded with `APPLOAD`; JSON IPC; default timeout 10 s) | `ezdxf` (headless, any OS; no offset/fillet/chamfer/undo/plot_pdf).
- Install: `uv sync`; Claude config command = venv python, args `["-m","autocad_mcp"]`. First call `system(operation="status")` to confirm backend.
- LT limits: no `vl*`/ActiveX, no file I/O, no selection sets. Use `execute_lisp` sparingly.

**U-C4N/Autocad-MCP** (github.com/U-C4N/Autocad-MCP; package `autocad-mcp-pro`)
- ~240+ tools; backends `com` (live AutoCAD on Windows, tested 2026) or `ezdxf` (headless; writing DWG needs ODA File Converter). `pip install autocad-mcp-pro` / `uvx autocad-mcp-pro`; extras `[com]`, `[pdf]`, `[office]`, `[full]`.
- Lifecycle tools: `drawing_new`, `drawing_preflight`, `drawing_plan`, `drawing_critique`, `drawing_refine`, `drawing_finalize`, `drawing_deliver`, `drawing_verify_requirements`; geometry `entity_create_line`, `dimension_linear`; `arch_plan_from_spec`, `arch_rooms_detect`; takeoffs `pipe_takeoff`, `cable_takeoff`; discovery `search_tools`, `describe_tool`, `cad_batch`.
- Set `ALLOWED_PATHS`; treat `system_run_command`/`system_run_lisp` as unsafe (denylist only). Self-reported benchmarks - verify output yourself.

**Practice with any MCP**: (1) `status/health` first; (2) create layers + styles before geometry; (3) work in mm; (4) batch calls (`cad_batch`) to reduce round trips; (5) screenshot/ preview after each major step; (6) save to a new filename before destructive edits; (7) never let the model guess coordinates - compute them from a grid/rooms table in code.

## Sources
- freeCodeCamp "AutoCAD for Beginners - Full University Course": https://www.youtube.com/watch?v=VtLXKU1PpRU (annotative/dimstyle/layer fundamentals)
- Skill Lync "AutoCAD Essentials for Mechanical Engineers" (technical drawing conventions): https://www.youtube.com/watch?v=oqCio0IHsNE
- Autodesk AutoCAD Help (system variables, plotting, sheet sets, accoreconsole, .NET API): https://help.autodesk.com/view/OARX/2025/ENU/
- ezdxf docs: https://ezdxf.readthedocs.io/
- https://github.com/puran-water/autocad-mcp and https://github.com/U-C4N/Autocad-MCP (READMEs, read 2026-10)
