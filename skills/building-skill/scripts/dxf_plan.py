"""Generate a country-correct architectural floor plan DXF from a JSON spec.

Usage:
    uv run --with ezdxf scripts/dxf_plan.py spec.json [-o out.dxf]

Spec (lengths in mm, walls by centerline):
{
  "country": "qa",                       # loads scripts/profiles/<country>.json
  "project": {"title": "...", "title_ar": "...", "client": "...", "plot": "...",
              "drawing": "Ground Floor Plan", "drawing_ar": "...", "number": "A-101",
              "rev": "0", "date": "2026-10-29", "drawn": "building-skill"},
  "walls":    [{"from": [0, 0], "to": [12000, 0], "thk": 250}],
  "openings": [{"wall": 0, "at": 2000, "width": 1000, "kind": "door",
                "into": [3000, 3000], "hinge": "start", "tag": "D1"},
               {"wall": 0, "at": 6000, "width": 1500, "kind": "window", "tag": "W1"}],
  "rooms":    [{"name": "Majlis", "name_ar": "مجلس", "pt": [3000, 3000], "area": 24.5}],
  "grids":    {"x": [0, 4000, 8000, 12000], "y": [0, 5000, 10000]},
  "plot":     {"polygon": [[-6000, -5000], [14000, -5000], [14000, 25000], [-6000, 25000]],
               "front": "south"},          # optional: boundary, setback dims, coverage
  "notes":    ["ASSUMPTIONS: frontage on south side, zone R1 (unconfirmed)"],
  "rules":    {"source": "QA Decision 108/2026 Annex 7", "front": 5000, "side": 3000,
               "rear": 3000, "coverage_max": 60},   # optional: PASS/FAIL on the sheet
  "profile":  {"scale": 50, "scale_label": "1:50 @ A1"}   # optional per-drawing overrides
}
Walls are solid poche + outline, extended half a thickness at each end so
orthogonal corners close. Openings cut the wall and get symbol + tag.
"""
import argparse
import json
import math
import sys
from pathlib import Path

import ezdxf
from ezdxf.enums import TextEntityAlignment

HERE = Path(__file__).resolve().parent
MC = TextEntityAlignment.MIDDLE_CENTER


def load_profile(country):
    path = HERE / "profiles" / f"{country}.json"
    if not path.exists():
        have = ", ".join(sorted(p.stem for p in (HERE / "profiles").glob("*.json")))
        raise SystemExit(f"No profile {path.name}. Available: {have}")
    prof = json.loads(path.read_text(encoding="utf-8"))
    if "extends" in prof:   # shallow-merge dict sections over the parent profile
        base = load_profile(prof.pop("extends"))
        for k, v in prof.items():
            base[k] = {**base[k], **v} if isinstance(v, dict) and isinstance(base.get(k), dict) else v
        prof = base
    return prof


def setup_doc(prof):
    doc = ezdxf.new("R2018", setup=True)
    doc.header["$INSUNITS"] = prof["insunits"]
    doc.header["$MEASUREMENT"] = 0 if prof["insunits"] == 1 else 1
    doc.header["$LWDISPLAY"] = 1
    doc.header["$PSLTSCALE"] = 1
    doc.header["$LTSCALE"] = prof.get("ltscale", 1)
    for name, aci, lw, *lt in prof["layers"].values():
        if name not in doc.layers:
            layer = doc.layers.add(name, color=aci, lineweight=lw)
            if lt:
                layer.dxf.linetype = lt[0]
    t = prof["text"]
    doc.styles.add(t["style"], font=t["font"])
    d = prof["dim"]
    ds = doc.dimstyles.new(d["name"])
    for key, val in {
        "dimtxsty": t["style"], "dimscale": prof["scale"], "dimtxt": d["text_h"],
        "dimasz": d["arrow"], "dimtsz": d["arrow"] if d.get("ticks", True) else 0,
        "dimexo": d["ext_offset"], "dimexe": d["ext_extend"], "dimgap": d["gap"],
        "dimdec": d["decimals"], "dimlunit": d["lunit"], "dimlfac": d.get("lfac", 1.0),
        "dimtad": 1, "dimjust": 0, "dimzin": d.get("zin", 8), "dimtih": 0, "dimtoh": 0,
        "dimclrd": 256, "dimclre": 256, "dimclrt": 256,
    }.items():
        ds.dxf.set(key, val)
    return doc


def lay(prof, key):
    return prof["layers"][key][0]


def ar(prof, s):
    """AutoCAD shapes Arabic letters but lays words out left-to-right, so a
    phrase reads backwards. Reversing word order makes it read correctly."""
    if not s or not prof.get("ar_word_reverse", True):
        return s
    if not any("؀" <= ch <= "ۿ" for ch in s):
        return s
    return " ".join(reversed(s.split()))


def wall_frame(w):
    (x1, y1), (x2, y2) = w["from"], w["to"]
    length = math.hypot(x2 - x1, y2 - y1)
    u = ((x2 - x1) / length, (y2 - y1) / length)
    n = (-u[1], u[0])
    pt = lambda d, s: (x1 + u[0] * d + n[0] * s, y1 + u[1] * d + n[1] * s)
    return pt, n, length


def draw_walls(msp, prof, walls, openings):
    outline, poche = lay(prof, "wall"), lay(prof, "wall_hatch")
    for i, w in enumerate(walls):
        pt, _, length = wall_frame(w)
        h = w["thk"] / 2
        cuts = sorted((o["at"], o["at"] + o["width"]) for o in openings if o["wall"] == i)
        segs, start = [], -h
        for a, b in cuts:
            segs.append((start, a))
            start = b
        segs.append((start, length + h))
        for a, b in segs:
            if b - a <= 1:
                continue
            pts = [pt(a, -h), pt(b, -h), pt(b, h), pt(a, h)]
            msp.add_lwpolyline(pts, close=True, dxfattribs={"layer": outline})
            hatch = msp.add_hatch(color=256, dxfattribs={"layer": poche})
            hatch.paths.add_polyline_path(pts, is_closed=True)


def draw_openings(msp, prof, walls, openings, th):
    style = prof["text"]["style"]
    for o in openings:
        w = walls[o["wall"]]
        pt, n, _ = wall_frame(w)
        h = w["thk"] / 2
        a, b = o["at"], o["at"] + o["width"]
        if o["kind"] == "door":
            layer = lay(prof, "door")
            if "into" in o:   # swing toward a point inside the room the door serves
                base = pt(0, 0)
                dot = (o["into"][0] - base[0]) * n[0] + (o["into"][1] - base[1]) * n[1]
                side = 1 if dot > 0 else -1
            else:
                side = 1 if o.get("swing", "left") == "left" else -1
            hinge_d, free_d = (a, b) if o.get("hinge", "start") == "start" else (b, a)
            hinge = pt(hinge_d, side * h)
            leaf = (hinge[0] + n[0] * side * o["width"], hinge[1] + n[1] * side * o["width"])
            free = pt(free_d, side * h)
            msp.add_line(hinge, leaf, dxfattribs={"layer": layer})
            a1 = math.degrees(math.atan2(leaf[1] - hinge[1], leaf[0] - hinge[0]))
            a2 = math.degrees(math.atan2(free[1] - hinge[1], free[0] - hinge[0]))
            start, end = (a1, a2) if (a2 - a1) % 360 <= 180 else (a2, a1)
            msp.add_arc(hinge, o["width"], start, end, dxfattribs={"layer": layer})
            tag_pt = pt((a + b) / 2, -side * (h + th * 1.4))
        else:
            layer = lay(prof, "window")
            for s in (-h, -h / 4, h / 4, h):
                msp.add_line(pt(a, s), pt(b, s), dxfattribs={"layer": layer})
            tag_pt = pt((a + b) / 2, h + th * 1.4)
        for d in (a, b):  # jambs
            msp.add_line(pt(d, -h), pt(d, h), dxfattribs={"layer": lay(prof, "wall")})
        if o.get("tag"):
            msp.add_text(o["tag"], height=th, dxfattribs={"layer": lay(prof, "tag"), "style": style}
                         ).set_placement(tag_pt, align=MC)


def draw_rooms(msp, prof, rooms, th):
    for r in rooms:
        lines = [r["name"].upper()]
        if prof.get("bilingual") and r.get("name_ar"):
            lines.append(ar(prof, r["name_ar"]))
        if r.get("area"):
            lines.append(ar(prof, prof["area_fmt"].format(a=r["area"], ft2=r["area"] * 10.7639)))
        mt = msp.add_mtext("\\P".join(lines), dxfattribs={
            "layer": lay(prof, "room"), "style": prof["text"]["style"], "char_height": th * 1.2})
        mt.set_location(tuple(r["pt"]), attachment_point=5)


def grid_label(i, kind):
    return str(i + 1) if kind == "numbers" else chr(65 + i)


def draw_grids(msp, prof, grids, extent, th):
    layer, style = lay(prof, "grid"), prof["text"]["style"]
    (xmin, ymin), (xmax, ymax) = extent
    off = 34 * prof["scale"] * prof.get("paper_mm", 1)   # beyond both dim rows
    r = th * 2.2
    x_kind = prof.get("grid_x", "numbers")
    y_kind = "letters" if x_kind == "numbers" else "numbers"
    for axis, values, kind in (("x", grids.get("x", []), x_kind), ("y", grids.get("y", []), y_kind)):
        for i, v in enumerate(values):
            if axis == "x":
                p1, p2 = (v, ymin - off), (v, ymax + off)
                bubbles = [(v, ymin - off - r), (v, ymax + off + r)]
            else:
                p1, p2 = (xmin - off, v), (xmax + off, v)
                bubbles = [(xmin - off - r, v), (xmax + off + r, v)]
            msp.add_line(p1, p2, dxfattribs={"layer": layer})
            for c in bubbles:
                msp.add_circle(c, r, dxfattribs={"layer": layer})
                msp.add_text(grid_label(i, kind), height=th * 1.4,
                             dxfattribs={"layer": layer, "style": style}).set_placement(c, align=MC)


def ft_in(inches, step=0.25):
    """12'-6 1/4" style text; ezdxf's dim renderer ignores architectural DIMLUNIT."""
    total = round(inches / step) * step
    feet, rest = divmod(total, 12)
    whole = int(rest)
    frac = rest - whole
    frac_txt = ""
    if frac:
        num, den = int(round(frac / step)), int(round(1 / step))
        while num % 2 == 0 and den % 2 == 0:
            num, den = num // 2, den // 2
        frac_txt = f" {num}/{den}"
    return f"{int(feet)}'-{whole}{frac_txt}\""


def draw_dims(msp, prof, grids, extent):
    layer, ds = lay(prof, "dim"), prof["dim"]["name"]
    arch = prof["dim"]["lunit"] == 4
    txt = lambda a, b: ft_in(abs(b - a)) if arch else "<>"
    (xmin, ymin), (xmax, ymax) = extent
    step = 12 * prof["scale"] * prof.get("paper_mm", 1)   # clears opening tags
    xs = sorted(set(grids.get("x", [])) | {xmin, xmax})
    ys = sorted(set(grids.get("y", [])) | {ymin, ymax})
    for row, pairs in ((1, list(zip(xs, xs[1:]))), (2, [(xmin, xmax)])):
        for a, b in pairs:
            msp.add_linear_dim(base=(a, ymin - step * row), p1=(a, ymin), p2=(b, ymin), text=txt(a, b),
                               dimstyle=ds, dxfattribs={"layer": layer}).render()
    for row, pairs in ((1, list(zip(ys, ys[1:]))), (2, [(ymin, ymax)])):
        for a, b in pairs:
            msp.add_linear_dim(base=(xmin - step * row, a), p1=(xmin, a), p2=(xmin, b), angle=90,
                               text=txt(a, b), dimstyle=ds, dxfattribs={"layer": layer}).render()


def draw_site(msp, prof, plot, bext, th):
    """Plot boundary + one setback dimension from each building face to the boundary."""
    pts = [tuple(p) for p in plot["polygon"]]
    msp.add_lwpolyline(pts, close=True, dxfattribs={"layer": lay(prof, "plot")})
    (bx0, by0), (bx1, by1) = bext
    px0, px1 = min(p[0] for p in pts), max(p[0] for p in pts)
    py0, py1 = min(p[1] for p in pts), max(p[1] for p in pts)
    ds, layer = prof["dim"]["name"], lay(prof, "dim")
    arch = prof["dim"]["lunit"] == 4
    label = lambda d: "SB " + (ft_in(d) if arch else "<>")
    my, mx = (by0 + by1) / 2, (bx0 + bx1) / 2
    for p1, p2, base, ang in (((px0, my), (bx0, my), (0, my + th * 3), 0),
                              ((bx1, my), (px1, my), (0, my + th * 3), 0),
                              ((mx, py0), (mx, by0), (mx + th * 3, 0), 90),
                              ((mx, by1), (mx, py1), (mx + th * 3, 0), 90)):
        d = abs(p2[0] - p1[0]) if ang == 0 else abs(p2[1] - p1[1])
        if d > 1:
            msp.add_linear_dim(base=base, p1=p1, p2=p2, angle=ang, text=label(d),
                               dimstyle=ds, dxfattribs={"layer": layer}).render()


def poly_area(pts):
    return abs(sum(x1 * y2 - x2 * y1 for (x1, y1), (x2, y2) in zip(pts, pts[1:] + pts[:1]))) / 2


def schedule_lines(prof, spec, bext):
    """Area schedule in m2 (and SF for imperial profiles): plot, footprint, coverage."""
    f = prof.get("mm_to_unit", 1)
    to_m2 = 1 / (1e6 * f * f)
    (bx0, by0), (bx1, by1) = bext
    foot = (bx1 - bx0) * (by1 - by0) * to_m2
    fmt = lambda a: prof["area_fmt"].replace("{ft2", "{b").format(a=a, b=a * 10.7639)
    lines = ["AREA SCHEDULE", f"GROUND FLOOR FOOTPRINT: {fmt(foot)}"]
    if spec.get("plot"):
        plot = poly_area([tuple(p) for p in spec["plot"]["polygon"]]) * to_m2
        lines[1:1] = [f"PLOT AREA: {fmt(plot)}"]
        lines.append(f"GROUND COVERAGE: {foot / plot * 100:.1f} %")
    return lines + check_lines(spec, bext, f)


def check_lines(spec, bext, f):
    """PASS/FAIL against limits the caller copied from the country file:
    "rules": {"source": "QA Decision 108/2026 Annex 7", "front": 5000, "side": 3000,
              "rear": 3000, "coverage_max": 60}   (mm, %)."""
    rules, plot = spec.get("rules"), spec.get("plot")
    if not rules or not plot:
        return []
    (bx0, by0), (bx1, by1) = bext
    pp = plot["polygon"]
    px0, px1 = min(p[0] for p in pp), max(p[0] for p in pp)
    py0, py1 = min(p[1] for p in pp), max(p[1] for p in pp)
    gaps = {"south": by0 - py0, "north": py1 - by1, "west": bx0 - px0, "east": px1 - bx1}
    front = plot.get("front", "south")
    rear = {"south": "north", "north": "south", "east": "west", "west": "east"}[front]
    out = ["", f"CODE CHECK ({rules.get('source', 'source not given')})"]
    for side, gap in gaps.items():
        kind = "front" if side == front else "rear" if side == rear else "side"
        need = rules.get(kind)
        if need is not None:
            need *= f
            out.append(f"{side.upper()} {kind} setback {gap / f:.0f} >= {need / f:.0f}: "
                       + ("PASS" if gap >= need - 1e-6 else "FAIL"))
    if "coverage_max" in rules:
        cov = (bx1 - bx0) * (by1 - by0) / poly_area([tuple(p) for p in pp]) * 100
        out.append(f"Coverage {cov:.1f} % <= {rules['coverage_max']} %: "
                   + ("PASS" if cov <= rules["coverage_max"] else "FAIL"))
    return out


def draw_sheet(doc, prof, project, extent, side_text=()):
    """Paper space: border, (bilingual) title block, scaled viewport, north arrow,
    and side_text (area schedule, notes) stacked above the north arrow."""
    sh = prof["sheet"]
    w, h, m = sh["w"], sh["h"], sh["margin"]
    psp = doc.layouts.new(sh["name"])
    psp.page_setup(size=(w, h), margins=(0, 0, 0, 0), units=sh["units"])
    main_vp = psp.main_viewport()
    if main_vp:   # AutoCAD AUDIT requires the overall paper-space viewport on layer 0
        main_vp.dxf.layer = "0"
    tb, style, th = lay(prof, "titleblock"), prof["text"]["style"], sh["tb_text"]
    psp.add_lwpolyline([(m, m), (w - m, m), (w - m, h - m), (m, h - m)], close=True,
                       dxfattribs={"layer": tb, "const_width": th * 0.15})
    bw, bh = sh["tb_w"], sh["tb_h"]
    x0, y0 = w - m - bw, m
    psp.add_lwpolyline([(x0, y0), (w - m, y0), (w - m, y0 + bh), (x0, y0 + bh)], close=True,
                       dxfattribs={"layer": tb})
    fields = prof["titleblock_fields"]
    rh = bh / len(fields)
    for i, (label, label_ar, key) in enumerate(fields):
        y = y0 + bh - (i + 1) * rh
        if i:
            psp.add_line((x0, y + rh), (w - m, y + rh), dxfattribs={"layer": tb})
        val = prof["scale_label"] if key == "scale" else project.get(key, "")
        psp.add_text(label, height=th * 0.6, dxfattribs={"layer": tb, "style": style}
                     ).set_placement((x0 + th * 0.5, y + rh - th * 0.4), align=TextEntityAlignment.TOP_LEFT)
        psp.add_text(str(val), height=th, dxfattribs={"layer": tb, "style": style}
                     ).set_placement((x0 + th * 0.5, y + th * 0.5), align=TextEntityAlignment.BOTTOM_LEFT)
        if prof.get("bilingual"):
            if label_ar:
                psp.add_mtext(ar(prof, label_ar), dxfattribs={"layer": tb, "style": style, "char_height": th * 0.6}
                              ).set_location((w - m - th * 0.5, y + rh - th * 0.4), attachment_point=3)
            if project.get(key + "_ar"):
                psp.add_mtext(ar(prof, project[key + "_ar"]), dxfattribs={"layer": tb, "style": style, "char_height": th}
                              ).set_location((w - m - th * 0.5, y + th * 0.5), attachment_point=9)
    (xmin, ymin), (xmax, ymax) = extent
    vw, vh = x0 - 3 * m, h - 4 * m
    model_per_paper = prof["scale"] * sh["model_per_paper"]   # model units per paper unit
    psp.add_viewport(center=(2 * m + vw / 2, h / 2), size=(vw, vh),
                     view_center_point=((xmin + xmax) / 2, (ymin + ymax) / 2),
                     view_height=vh * model_per_paper, dxfattribs={"layer": lay(prof, "viewport")})
    cx, cy, r = x0 + bw / 2, y0 + bh + th * 7, th * 3.5
    psp.add_circle((cx, cy), r, dxfattribs={"layer": tb})
    psp.add_lwpolyline([(cx, cy + r), (cx - r / 3, cy - r * 0.6), (cx, cy - r * 0.3),
                        (cx + r / 3, cy - r * 0.6)], close=True, dxfattribs={"layer": tb})
    psp.add_text("N", height=th * 1.4, dxfattribs={"layer": tb, "style": style}
                 ).set_placement((cx, cy + r * 1.5), align=MC)
    if side_text:
        mt = psp.add_mtext("\\P".join(side_text), dxfattribs={
            "layer": lay(prof, "notes"), "style": style, "char_height": th * 0.8, "width": bw})
        mt.set_location((x0, cy + r * 3), attachment_point=7)
    for name in [n for n in doc.layouts.names() if n not in ("Model", sh["name"])]:
        doc.layouts.delete(name)


def to_drawing_units(spec, f):
    """Spec is always mm; imperial profiles draw in inches (f = 1/25.4)."""
    if f == 1:
        return spec
    sc = lambda p: [p[0] * f, p[1] * f]
    for w in spec["walls"]:
        w["from"], w["to"], w["thk"] = sc(w["from"]), sc(w["to"]), w["thk"] * f
    for o in spec.get("openings", []):
        o["at"], o["width"] = o["at"] * f, o["width"] * f
        if "into" in o:
            o["into"] = sc(o["into"])
    for r in spec.get("rooms", []):
        r["pt"] = sc(r["pt"])
    if spec.get("plot"):
        spec["plot"]["polygon"] = [sc(p) for p in spec["plot"]["polygon"]]
    if spec.get("grids"):
        spec["grids"] = {k: [v * f for v in vs] for k, vs in spec["grids"].items()}
    return spec


def main():
    sys.stdout.reconfigure(encoding="utf-8")   # Arabic in --help on Windows consoles
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("spec")
    ap.add_argument("-o", "--out")
    args = ap.parse_args()
    spec = json.loads(Path(args.spec).read_text(encoding="utf-8"))
    prof = load_profile(spec["country"])
    for k, v in spec.get("profile", {}).items():   # per-drawing overrides, e.g. scale/sheet
        prof[k] = {**prof[k], **v} if isinstance(v, dict) and isinstance(prof.get(k), dict) else v
    spec = to_drawing_units(spec, prof.get("mm_to_unit", 1))
    doc = setup_doc(prof)
    msp = doc.modelspace()
    th = prof["dim"]["text_h"] * prof["scale"]
    walls, openings = spec["walls"], spec.get("openings", [])
    xs = [c for w in walls for c in (w["from"][0], w["to"][0])]
    ys = [c for w in walls for c in (w["from"][1], w["to"][1])]
    extent = ((min(xs), min(ys)), (max(xs), max(ys)))
    grids = spec.get("grids") or {"x": [extent[0][0], extent[1][0]], "y": [extent[0][1], extent[1][1]]}
    draw_walls(msp, prof, walls, openings)
    draw_openings(msp, prof, walls, openings, th)
    draw_rooms(msp, prof, spec.get("rooms", []), th)
    draw_grids(msp, prof, grids, extent, th)
    draw_dims(msp, prof, grids, extent)
    half = max(w["thk"] for w in walls) / 2
    bext = ((extent[0][0] - half, extent[0][1] - half), (extent[1][0] + half, extent[1][1] + half))
    view = extent
    if spec.get("plot"):
        draw_site(msp, prof, spec["plot"], bext, th)
        pp = spec["plot"]["polygon"]
        view = ((min(extent[0][0], *(p[0] for p in pp)), min(extent[0][1], *(p[1] for p in pp))),
                (max(extent[1][0], *(p[0] for p in pp)), max(extent[1][1], *(p[1] for p in pp))))
    side = schedule_lines(prof, spec, bext) + [""] + list(spec.get("notes", []))
    draw_sheet(doc, prof, spec.get("project", {}), view, side)
    out = Path(args.out or Path(args.spec).with_suffix(".dxf"))
    doc.saveas(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
