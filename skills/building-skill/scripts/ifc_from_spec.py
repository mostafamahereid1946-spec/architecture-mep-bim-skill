"""Build an IFC4 model from the same plan spec dxf_plan.py uses (Revit, Revit LT, ArchiCAD, Bonsai import it).

Usage:
    uv run --with ifcopenshell scripts/ifc_from_spec.py spec.json [-o out.ifc] [--height 3300]

Creates: IfcProject > IfcSite > IfcBuilding > IfcBuildingStorey with
  IfcWall per spec wall (typed by thickness, Pset_WallCommon.IsExternal for walls on the outline),
  IfcOpeningElement + IfcDoor / IfcWindow per opening (real voids),
  IfcSlab floor and roof over the building outline (spec "roofs" boxes if given),
  IfcSpace per room (LongName = name, Description = Arabic name).
Spec lengths are mm; the IFC is in metres. Validates the file before saving.
"""
import argparse
import json
import math
import sys
from pathlib import Path

import ifcopenshell
import ifcopenshell.api.aggregate
import ifcopenshell.api.context
import ifcopenshell.api.feature
import ifcopenshell.api.geometry
import ifcopenshell.api.project
import ifcopenshell.api.pset
import ifcopenshell.api.root
import ifcopenshell.api.spatial
import ifcopenshell.api.type
import ifcopenshell.api.unit
import ifcopenshell.validate
import numpy as np

A = ifcopenshell.api
SILL, WIN_H, DOOR_H, SLAB = 0.9, 1.5, 2.4, 0.3


def placement(f, prod, x, y, rot=0.0, z=0.0):
    c, s = math.cos(rot), math.sin(rot)
    A.geometry.edit_object_placement(f, product=prod, matrix=np.array(
        [[c, -s, 0, x], [s, c, 0, y], [0, 0, 1, z], [0, 0, 0, 1]], dtype=float))


def build(spec, height):
    f = A.project.create_file(version="IFC4")
    proj = spec.get("project", {})
    project = A.root.create_entity(f, ifc_class="IfcProject", name=proj.get("title", "building-skill project"))
    A.unit.assign_unit(f)
    model = A.context.add_context(f, context_type="Model")
    body = A.context.add_context(f, context_type="Model", context_identifier="Body",
                                 target_view="MODEL_VIEW", parent=model)
    site = A.root.create_entity(f, ifc_class="IfcSite", name=proj.get("plot", "Site"))
    bldg = A.root.create_entity(f, ifc_class="IfcBuilding", name=proj.get("title", "Building"))
    storey = A.root.create_entity(f, ifc_class="IfcBuildingStorey", name="Ground Floor")
    storey.Elevation = 0.0
    A.aggregate.assign_object(f, products=[site], relating_object=project)
    A.aggregate.assign_object(f, products=[bldg], relating_object=site)
    A.aggregate.assign_object(f, products=[storey], relating_object=bldg)

    m = lambda v: v / 1000.0
    walls_spec = spec["walls"]
    xs = [c for w in walls_spec for c in (w["from"][0], w["to"][0])]
    ys = [c for w in walls_spec for c in (w["from"][1], w["to"][1])]
    x0, x1, y0, y1 = m(min(xs)), m(max(xs)), m(min(ys)), m(max(ys))
    on_outline = lambda w: all(
        abs(m(p[0]) - x0) < 1e-6 or abs(m(p[0]) - x1) < 1e-6 or abs(m(p[1]) - y0) < 1e-6
        or abs(m(p[1]) - y1) < 1e-6 for p in (w["from"], w["to"]))

    types, walls = {}, []
    for i, w in enumerate(walls_spec):
        (ax, ay), (bx, by), t = [m(v) for v in w["from"]], [m(v) for v in w["to"]], m(w["thk"])
        L = math.hypot(bx - ax, by - ay)
        ux, uy = (bx - ax) / L, (by - ay) / L
        nx, ny = -uy, ux
        name = f"WT-{int(w['thk'])}"
        if name not in types:
            types[name] = A.root.create_entity(f, ifc_class="IfcWallType", name=name, predefined_type="SOLIDWALL")
        wall = A.root.create_entity(f, ifc_class="IfcWall", name=f"W{i}")
        # extend by half thickness so corners meet, offset so the spec line is the centreline
        rep = A.geometry.add_wall_representation(f, context=body, length=L + t, height=height, thickness=t)
        A.geometry.assign_representation(f, product=wall, representation=rep)
        placement(f, wall, ax - ux * t / 2 - nx * t / 2, ay - uy * t / 2 - ny * t / 2, math.atan2(uy, ux))
        A.spatial.assign_container(f, products=[wall], relating_structure=storey)
        A.type.assign_type(f, related_objects=[wall], relating_type=types[name])
        ps = A.pset.add_pset(f, product=wall, name="Pset_WallCommon")
        A.pset.edit_pset(f, pset=ps, properties={"IsExternal": on_outline(w), "LoadBearing": t >= 0.2})
        walls.append((wall, (ax, ay), (ux, uy), (nx, ny), t))

    for o in spec.get("openings", []):
        wall, (ax, ay), (ux, uy), (nx, ny), t = walls[o["wall"]]
        w, at = m(o["width"]), m(o["at"])
        door = o["kind"] == "door"
        z, h = (0.0, DOOR_H) if door else (SILL, WIN_H)
        opening = A.root.create_entity(f, ifc_class="IfcOpeningElement", name=f"{o.get('tag', '')}-opening")
        A.geometry.assign_representation(f, product=opening, representation=A.geometry.add_wall_representation(
            f, context=body, length=w, height=h, thickness=t + 0.2))
        ox, oy = ax + ux * at - nx * (t / 2 + 0.1), ay + uy * at - ny * (t / 2 + 0.1)
        placement(f, opening, ox, oy, math.atan2(uy, ux), z)
        A.feature.add_feature(f, feature=opening, element=wall)
        fill = A.root.create_entity(f, ifc_class="IfcDoor" if door else "IfcWindow", name=o.get("tag", ""),
                                    predefined_type="DOOR" if door else "WINDOW")
        fill.OverallWidth, fill.OverallHeight = w, h
        placement(f, fill, ox, oy, math.atan2(uy, ux), z)
        A.feature.add_filling(f, opening=opening, element=fill)
        A.spatial.assign_container(f, products=[fill], relating_structure=storey)

    outline = [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]
    floor = A.root.create_entity(f, ifc_class="IfcSlab", name="Ground slab", predefined_type="FLOOR")
    A.geometry.assign_representation(f, product=floor, representation=A.geometry.add_slab_representation(
        f, context=body, depth=SLAB, polyline=outline))
    placement(f, floor, 0, 0, z=-SLAB)
    A.spatial.assign_container(f, products=[floor], relating_structure=storey)
    roofs = [[m(v) for v in r] for r in spec.get("roofs", [])] or [[x0, y0, x1, y1]]
    for i, (rx0, ry0, rx1, ry1) in enumerate(roofs):
        roof = A.root.create_entity(f, ifc_class="IfcSlab", name=f"Roof slab {i}", predefined_type="ROOF")
        A.geometry.assign_representation(f, product=roof, representation=A.geometry.add_slab_representation(
            f, context=body, depth=SLAB, polyline=[(rx0, ry0), (rx1, ry0), (rx1, ry1), (rx0, ry1)]))
        placement(f, roof, 0, 0, z=height)
        A.spatial.assign_container(f, products=[roof], relating_structure=storey)

    for i, r in enumerate(spec.get("rooms", [])):
        space = A.root.create_entity(f, ifc_class="IfcSpace", name=f"{i + 1:02d}")
        space.LongName = r["name"]
        if r.get("name_ar"):
            space.Description = r["name_ar"]
        placement(f, space, m(r["pt"][0]), m(r["pt"][1]))
        A.aggregate.assign_object(f, products=[space], relating_object=storey)
        if r.get("area"):
            ps = A.pset.add_pset(f, product=space, name="Pset_SpaceCommon")
            A.pset.edit_pset(f, pset=ps, properties={"Reference": r["name"]})
    return f


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("spec")
    ap.add_argument("-o", "--out")
    ap.add_argument("--height", type=float, default=3300, help="storey height mm")
    a = ap.parse_args()
    spec = json.loads(Path(a.spec).read_text(encoding="utf-8"))
    f = build(spec, a.height / 1000.0)
    log = ifcopenshell.validate.json_logger()
    ifcopenshell.validate.validate(f, log)
    out = Path(a.out or Path(a.spec).with_suffix(".ifc"))
    f.write(str(out))
    counts = {c: len(f.by_type(c)) for c in ("IfcWall", "IfcDoor", "IfcWindow", "IfcOpeningElement", "IfcSlab", "IfcSpace")}
    print(f"wrote {out}  {counts}  validation_issues={len(log.statements)}")
    for s in log.statements[:5]:
        print("  ", s)


if __name__ == "__main__":
    main()
