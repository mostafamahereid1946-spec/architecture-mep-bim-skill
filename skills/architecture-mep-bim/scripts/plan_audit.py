"""Design-quality audit of a plan spec: rejects bad layouts before drawing/export.

Usage:
    uv run --with shapely --with networkx scripts/plan_audit.py spec.json [--country qa] [--json]

Reads the same JSON spec as dxf_plan.py (walls by centreline in mm, openings
{wall, at, width, kind door|window, into}, rooms {name, name_ar, pt, area}) and
prints PASS / WARN / FAIL lines. Exit code 1 if any FAIL, else 0 (2 = unreadable spec).

Checks
  rooms        wall centrelines -> polygons; every room pt inside exactly one polygon;
               unlabelled enclosed polygons; net area (wall thickness removed) vs spec area
  circulation  graph of rooms + OUTSIDE joined by doors; unreachable rooms; doors with the
               same room both sides or onto nothing; "into" point not in an adjacent room
  doors        door on a wall junction or < 100 mm from a perpendicular wall face;
               swing arc (radius = width) hitting a wall or another swing; opening past
               the wall end; overlapping openings
  dead-space   corridor/hall dead ends with one door and > 6 m2
  sizes        room area / width below the country minimum (table below)
  habitability habitable rooms without a window to OUTSIDE or a courtyard; WC/bath door
               straight into kitchen/dining/majlis
  privacy      (Gulf: qa ae sa kw om bh) majlis/guest zone linked to family/bedroom zone
               by more than one door

Minimum sizes: GENERIC values are rules of thumb (lower bound of the typical ranges in
references/disciplines/architecture.md section 3), NOT code. COUNTRY_MIN overrides only
the numbers that references/countries/<cc>.md states. Override per project with
"rules": {"min_room": {"bedroom": 9.0}, "min_width": {"bedroom": 2.7}}  (m2 / m,
keys = room type below or the exact room name).
"""
import argparse
import json
import math
import sys
from pathlib import Path

import networkx as nx
from shapely.geometry import LineString, Point, Polygon
from shapely.ops import polygonize, polylabel, unary_union

OUT = "OUTSIDE"
FRAME_MM = 100        # clear wall between a door jamb and a perpendicular wall face
PROBE_MM = 100        # sample distance beyond the wall face to find the room each side
AREA_TOL = 0.05       # spec area vs measured net area
GULF = {"qa", "ae", "sa", "kw", "om", "bh"}
DEAD_END_MIN_M2 = 6.0

# ---------------------------------------------------------------- room vocabulary
# Order matters: first matching type wins (wet rooms and maid rooms before bedroom, etc.).
TYPE_KW = {
    "wc": ["wc", "toilet", "powder", "lavatory", "دورة مياه", "دورة المياه", "مرحاض"],
    "bathroom": ["bath", "shower", "ensuite", "en-suite", "حمام"],
    "maid": ["maid", "driver", "guard", "خادمة", "سائق", "حارس"],
    "majlis": ["majlis", "مجلس"],
    "kitchen": ["kitchen", "مطبخ"],
    "dining": ["dining", "طعام", "سفرة"],
    "bedroom": ["bedroom", "bed room", "غرفة نوم", "غرفة النوم", "نوم"],
    "guest": ["guest", "ضيوف", "ضيف"],
    "living": ["living", "family", "lounge", "معيشة", "عائلة", "صالة"],
    "office": ["office", "study", "مكتب"],
    "laundry": ["laundry", "مغسلة", "غسيل"],
    "store": ["store", "storage", "مخزن"],
    "courtyard": ["courtyard", "حوش", "فناء"],
    "corridor": ["corridor", "passage", "lobby", "hall", "ممر", "طرقة"],
}
HABITABLE_KW = ["bedroom", "living", "majlis", "kitchen", "family", "guest", "office",
                "غرفة", "مجلس", "صالة"]
CORRIDOR_KW = ["corridor", "hall", "passage", "lobby", "ممر", "طرقة"]
COURTYARD_KW = ["courtyard", "حوش", "فناء"]
GUEST_ZONE_KW = ["majlis", "guest", "مجلس", "ضيف", "ضيوف"]
FAMILY_ZONE_KW = ["bedroom", "family", "living", "master", "غرفة نوم", "غرفة النوم", "نوم",
                  "عائلة", "معيشة"]

# ---------------------------------------------------------------- minimum sizes
# type -> (min area m2, min clear width m). None = no number.
GENERIC_SRC = "generic rule of thumb (lower bound of architecture.md section 3 typical range)"
GENERIC_MIN = {
    "bedroom": (9.0, 2.7), "guest": (9.0, 2.7), "maid": (7.0, 2.4), "living": (18.0, 3.6),
    "majlis": (25.0, 4.5), "dining": (12.0, 3.0), "kitchen": (9.0, 2.4),
    "bathroom": (3.5, 1.5), "wc": (1.5, 0.9), "laundry": (3.0, 1.5), "store": (2.0, 1.2),
    "office": (9.0, 2.7), "corridor": (None, 0.9),
}
# Only numbers that the country file states. None inside a tuple = keep the generic value.
# qa om bh eg: the country file gives no room-size number -> generic only.
COUNTRY_MIN = {
    "sa": ("references/countries/sa.md 5.4 (residential code 5-4-2; row mapping flagged in file)", {
        "majlis": (11.2, 2.8), "dining": (11.2, 2.8), "living": (11.2, 2.8),
        "bedroom": (6.5, 2.1), "guest": (6.5, 2.1), "kitchen": (5.0, 1.8),
        "bathroom": (2.8, 1.4), "wc": (1.5, 1.0), "maid": (6.5, 2.1), "corridor": (None, 0.9)}),
    "ae": ("references/countries/ae.md 5.2-5.3 (Dubai DBC Part B)", {
        "living": (10.5, 3.0), "bedroom": (10.5, 3.0), "guest": (10.5, 3.0),
        "maid": (4.5, 2.1), "kitchen": (5.4, 1.8), "corridor": (None, 1.0)}),
    "kw": ("references/countries/kw.md 5.3 (reported draft, verify)", {
        "bedroom": (10.0, 3.0), "guest": (10.0, 3.0), "kitchen": (7.5, 2.0),
        "bathroom": (4.0, 1.75), "wc": (1.5, 1.2), "corridor": (None, 1.2)}),
    "tr": ("references/countries/tr.md 5.3 (Imar Yonetmeligi Art. 29)", {
        "living": (12.0, 3.0), "bedroom": (9.0, 2.5), "guest": (9.0, 2.5),
        "kitchen": (3.3, 1.5), "bathroom": (3.0, 1.5), "wc": (1.2, 1.0), "corridor": (None, 1.2)}),
    "jo": ("references/countries/jo.md 5 (Art. 56, 59)", {
        "kitchen": (6.0, None), "wc": (1.0, None), "bathroom": (1.5, None),
        "corridor": (None, 1.0)}),
    "in": ("references/countries/in.md 5 (NBC 2016 Part 3, 'others' row; marked memory/verify)", {
        "bedroom": (7.5, 2.1), "guest": (7.5, 2.1), "living": (7.5, 2.1), "kitchen": (5.0, 1.8)}),
    "my": ("references/countries/my.md 5 (UBBL 42-43, 'other habitable rooms' row)", {
        "bedroom": (6.5, 2.0), "guest": (6.5, 2.0), "living": (6.5, 2.0),
        "kitchen": (4.5, 1.5), "bathroom": (1.5, 0.75)}),
    "za": ("references/countries/za.md 5 (habitable room 6 m2, no dimension < 2 m)", {
        "bedroom": (6.0, 2.0), "guest": (6.0, 2.0), "living": (6.0, 2.0),
        "majlis": (6.0, 2.0), "office": (6.0, 2.0)}),
    "mx": ("references/countries/mx.md 5 (NTC Table 2.1, additional bedrooms)", {
        "bedroom": (6.0, 2.2), "guest": (6.0, 2.2)}),
    "uk": ("references/countries/uk.md 5.4 (NDSS single bedroom)", {
        "bedroom": (7.5, 2.15), "guest": (7.5, 2.15)}),
    "us": ("references/countries/us.md (IRC R304: 70 sq ft, 7 ft; marked verify)", {
        "bedroom": (6.5, 2.13), "guest": (6.5, 2.13), "living": (6.5, 2.13), "office": (6.5, 2.13)}),
    "it": ("references/countries/it.md 5 (DM 5/7/1975 art. 2)", {
        "bedroom": (9.0, None), "guest": (9.0, None), "living": (14.0, None)}),
}


class Report:
    def __init__(self):
        self.items = []

    def add(self, level, check, msg):
        self.items.append({"level": level, "check": check, "message": msg})

    def fail(self, check, msg):
        self.add("FAIL", check, msg)

    def warn(self, check, msg):
        self.add("WARN", check, msg)

    def close(self, check, start, pass_msg):
        """Emit a PASS line for `check` when nothing since `start` was WARN/FAIL."""
        if not any(i["check"] == check and i["level"] != "PASS" for i in self.items[start:]):
            self.add("PASS", check, pass_msg)

    def counts(self):
        return {lv: sum(1 for i in self.items if i["level"] == lv) for lv in ("PASS", "WARN", "FAIL")}


def has_kw(text, kws):
    return any(k in text for k in kws)


def room_text(r):
    return f"{r.get('name', '')} {r.get('name_ar', '')}".lower()


def room_type(r):
    t = room_text(r)
    for typ, kws in TYPE_KW.items():
        if has_kw(t, kws):
            return typ
    return None


def is_habitable(r):
    return has_kw(room_text(r), HABITABLE_KW)


def mm2m(x, y):
    return f"({x / 1000:.1f}, {y / 1000:.1f}) m"


class Wall:
    def __init__(self, i, w):
        self.i = i
        (x1, y1), (x2, y2) = w["from"], w["to"]
        self.p0 = (x1, y1)
        self.L = math.hypot(x2 - x1, y2 - y1)
        self.thk = float(w.get("thk", 200))
        self.h = self.thk / 2
        self.ok = self.L > 1
        if not self.ok:
            return
        self.u = ((x2 - x1) / self.L, (y2 - y1) / self.L)
        self.n = (-self.u[1], self.u[0])
        # same convention as dxf_plan.py: ends extended by half a thickness
        self.line = LineString([self.pt(-self.h, 0), self.pt(self.L + self.h, 0)])
        self.body = Polygon([self.pt(-self.h, -self.h), self.pt(self.L + self.h, -self.h),
                             self.pt(self.L + self.h, self.h), self.pt(-self.h, self.h)])

    def pt(self, d, s):
        return (self.p0[0] + self.u[0] * d + self.n[0] * s, self.p0[1] + self.u[1] * d + self.n[1] * s)

    def rect(self, a, b):
        return Polygon([self.pt(a, -self.h), self.pt(b, -self.h), self.pt(b, self.h), self.pt(a, self.h)])


class Opening:
    def __init__(self, k, o, walls):
        self.k, self.o = k, o
        self.kind = o.get("kind", "door")
        self.is_door = self.kind == "door"
        self.tag = o.get("tag") or f"{'D' if self.is_door else 'W'}#{k}"
        self.wi = o.get("wall")
        self.wall = walls[self.wi] if isinstance(self.wi, int) and 0 <= self.wi < len(walls) else None
        self.a = float(o.get("at", 0))
        self.width = float(o.get("width", 0))
        self.b = self.a + self.width
        self.sector = None
        self.side = None


class Audit:
    def __init__(self, spec, country, rep):
        self.spec, self.country, self.rep = spec, country, rep
        self.rules = spec.get("rules") or {}
        self.walls = [Wall(i, w) for i, w in enumerate(spec.get("walls", []))]
        good = [w for w in self.walls if w.ok]
        self.ops = [Opening(k, o, self.walls) for k, o in enumerate(spec.get("openings", []))]
        self.rooms = spec.get("rooms", [])
        self.labels = self._labels()
        self.noded = unary_union([w.line for w in good]) if good else None
        self.bodies = unary_union([w.body for w in good]) if good else None
        self.faces = []        # dicts: poly, net, label, rooms
        self.G = nx.MultiGraph()
        self.door_edges = []   # (op, A, B)

    # ---------------------------------------------------------- helpers
    def _labels(self):
        seen, out = {}, []
        for r in self.rooms:
            n = r.get("name", "room")
            seen[n] = seen.get(n, 0) + 1
            out.append(n if seen[n] == 1 else f"{n} #{seen[n]}")
        return out

    def node_at(self, p):
        for f in self.faces:
            if f["poly"].contains(p):
                return f["label"]
        return OUT

    def ambiguous(self, p):
        return self.noded is not None and p.distance(self.noded) < 1.0

    def sides(self, op):
        """[(A, B)] room labels at +n / -n side of the opening, sampled at 3 places."""
        w, res = op.wall, []
        for fr in (0.5, 0.25, 0.75):
            d = op.a + op.width * fr
            pa, pb = Point(w.pt(d, w.h + PROBE_MM)), Point(w.pt(d, -(w.h + PROBE_MM)))
            if self.ambiguous(pa) or self.ambiguous(pb):
                continue
            res.append((self.node_at(pa), self.node_at(pb)))
        return res

    def room_by_label(self, label):
        return self.rooms[self.labels.index(label)] if label in self.labels else None

    def is_courtyard(self, label):
        r = self.room_by_label(label)
        return bool(r) and has_kw(room_text(r), COURTYARD_KW)

    # ---------------------------------------------------------- 1. rooms
    def check_rooms(self):
        rep, start = self.rep, len(self.rep.items)
        for w in self.walls:
            if not w.ok:
                rep.fail("rooms", f"wall {w.i} has zero length")
        if self.noded is None:
            rep.fail("rooms", "spec has no usable walls")
            return
        for n, poly in enumerate(polygonize(self.noded)):
            net = poly.difference(self.bodies)
            self.faces.append({"poly": poly, "net": net, "label": None, "rooms": [], "n": n})
        for ri, r in enumerate(self.rooms):
            p = Point(r["pt"])
            hit = [f for f in self.faces if f["poly"].contains(p)]
            if not hit:
                rep.fail("rooms", f"Room '{r['name']}' pt {mm2m(*r['pt'])} is not inside any enclosed polygon "
                                  f"(walls do not close around it - check for gaps at wall ends)")
                continue
            hit[0]["rooms"].append(ri)
        for f in self.faces:
            if len(f["rooms"]) > 1:
                names = " and ".join(f"'{self.rooms[i]['name']}'" for i in f["rooms"])
                c = f["poly"].representative_point()
                rep.fail("rooms", f"Rooms {names} share one enclosed polygon around {mm2m(c.x, c.y)} "
                                  f"- no wall separates them")
            if f["rooms"]:
                f["label"] = self.labels[f["rooms"][0]]
            elif f["poly"].area / 1e6 > 0.05:
                c = f["poly"].representative_point()
                f["label"] = f"(unlabelled space @ {mm2m(c.x, c.y)})"
                rep.warn("rooms", f"Enclosed polygon of {f['poly'].area / 1e6:.1f} m2 at {mm2m(c.x, c.y)} "
                                  f"has no room label")
            else:
                f["label"] = "(sliver)"
        self.faces = [f for f in self.faces if f["label"] != "(sliver)"]
        for f in self.faces:
            if not f["rooms"]:
                continue
            r = self.rooms[f["rooms"][0]]
            net = f["net"].area / 1e6
            f["net_m2"] = net
            if r.get("area"):
                diff = (net - r["area"]) / r["area"]
                if abs(diff) > AREA_TOL:
                    rep.warn("rooms", f"Room '{r['name']}': spec area {r['area']:.1f} m2 but net polygon "
                                      f"(walls removed) is {net:.1f} m2 ({diff * 100:+.1f}%)")
        rep.close("rooms", start, f"{len(self.rooms)} rooms matched to {len(self.faces)} enclosed polygons; "
                                  f"net areas within {AREA_TOL * 100:.0f}% of spec")

    # ---------------------------------------------------------- 2. circulation
    def swing_side(self, op):
        w, o = op.wall, op.o
        if "into" in o:
            dot = (o["into"][0] - w.p0[0]) * w.n[0] + (o["into"][1] - w.p0[1]) * w.n[1]
            return 1 if dot > 0 else -1
        return 1 if o.get("swing", "left") == "left" else -1

    def check_circulation(self):
        rep, start = self.rep, len(self.rep.items)
        G = self.G
        G.add_node(OUT)
        for lab in self.labels:
            G.add_node(lab)
        for f in self.faces:
            if not f["rooms"]:
                G.add_node(f["label"])
        for op in self.ops:
            if not op.is_door:
                continue
            if op.wall is None or not op.wall.ok:
                rep.fail("circulation", f"{op.tag}: wall index {op.wi!r} does not exist")
                continue
            pairs = self.sides(op)
            if pairs:
                A, B = pairs[0]
            else:
                mid = op.a + op.width / 2
                A = self.node_at(Point(op.wall.pt(mid, op.wall.h + PROBE_MM)))
                B = self.node_at(Point(op.wall.pt(mid, -(op.wall.h + PROBE_MM))))
            op.side = self.swing_side(op)
            if A == B == OUT:
                rep.fail("circulation", f"{op.tag} on wall {op.wi}: opens onto nothing "
                                        f"(outside on both sides, no room is served)")
                continue
            if A == B:
                rep.fail("circulation", f"{op.tag} on wall {op.wi}: both sides are '{A}' "
                                        f"(door inside one room, it connects nothing)")
                continue
            for lab in (A, B):
                if lab.startswith("(unlabelled"):
                    rep.warn("circulation", f"{op.tag} on wall {op.wi} opens into {lab}")
            if "into" in op.o:
                ni = self.node_at(Point(op.o["into"]))
                swing_room = A if op.side > 0 else B
                if ni not in (A, B):
                    rep.fail("circulation", f"{op.tag} on wall {op.wi}: 'into' point {mm2m(*op.o['into'])} is in "
                                            f"'{ni}', not in a room adjacent to the door ('{A}' / '{B}')")
                elif ni != swing_room:
                    rep.fail("circulation", f"{op.tag} on wall {op.wi}: 'into' point is in '{ni}' but the swing "
                                            f"side of the wall is '{swing_room}'")
            G.add_edge(A, B, tag=op.tag)
            self.door_edges.append((op, A, B))
        comp = nx.node_connected_component(G, OUT)
        for lab in self.labels:
            if lab in comp:
                continue
            mine = nx.node_connected_component(G, lab) - {lab}
            doors = [d["tag"] for _, _, d in G.edges(lab, data=True)]
            why = (f"it has no door at all" if not doors else
                   f"its doors ({', '.join(doors)}) only lead to {sorted(mine)}")
            rep.fail("circulation", f"Room '{lab}' is unreachable from OUTSIDE: {why}")
        nd = sum(1 for o in self.ops if o.is_door)
        rep.close("circulation", start, f"{nd} doors; all {len(self.labels)} rooms reachable from OUTSIDE")

    # ---------------------------------------------------------- 3. door placement
    def junctions(self, w):
        out = []
        for v in self.walls:
            if v is w or not v.ok:
                continue
            inter = w.line.intersection(v.line)
            if inter.is_empty or inter.geom_type != "Point":
                continue
            sin = abs(w.u[0] * v.u[1] - w.u[1] * v.u[0])
            if sin < 1e-3:
                continue
            s = (inter.x - w.p0[0]) * w.u[0] + (inter.y - w.p0[1]) * w.u[1]
            out.append((v, s, v.thk / 2 / sin))
        return out

    def sector(self, op):
        w, side = op.wall, op.side
        a, b = op.a, op.b
        hinge_d, free_d = (a, b) if op.o.get("hinge", "start") == "start" else (b, a)
        hinge, free = w.pt(hinge_d, side * w.h), w.pt(free_d, side * w.h)
        leaf = (hinge[0] + w.n[0] * side * op.width, hinge[1] + w.n[1] * side * op.width)
        a0 = math.atan2(leaf[1] - hinge[1], leaf[0] - hinge[0])
        a1 = math.atan2(free[1] - hinge[1], free[0] - hinge[0])
        d = (a1 - a0 + math.pi) % (2 * math.pi) - math.pi
        pts = [hinge] + [(hinge[0] + op.width * math.cos(a0 + d * t / 16),
                          hinge[1] + op.width * math.sin(a0 + d * t / 16)) for t in range(17)]
        return Polygon(pts)

    def check_doors(self):
        rep, start = self.rep, len(self.rep.items)
        by_wall = {}
        for op in self.ops:
            if op.wall is None or not op.wall.ok:
                if not (op.is_door):
                    rep.fail("doors", f"{op.tag}: wall index {op.wi!r} does not exist")
                continue
            by_wall.setdefault(op.wi, []).append(op)
            w = op.wall
            if op.width <= 0:
                rep.fail("doors", f"{op.tag} on wall {op.wi}: width {op.width:.0f} mm is not positive")
                continue
            if op.a < 0 or op.b > w.L + 1e-6:
                rep.fail("doors", f"{op.tag} on wall {op.wi}: spans {op.a:.0f}..{op.b:.0f} mm but the wall is "
                                  f"only {w.L:.0f} mm long (opening extends past the wall)")
            for v, s, half in self.junctions(w):
                lo, hi = s - half, s + half
                if op.a < hi and op.b > lo:
                    msg = (f"{op.tag} on wall {op.wi}: overlaps the junction with wall {v.i} "
                           f"(that wall occupies {lo:.0f}..{hi:.0f} mm along this wall, opening "
                           f"{op.a:.0f}..{op.b:.0f}) at {mm2m(*w.pt(s, 0))}")
                    (rep.fail if op.is_door else rep.warn)("doors", msg if op.is_door else
                                                           msg.replace("overlaps the junction", "straddles the partition"))
                elif op.is_door:
                    gap = lo - op.b if op.b <= lo else op.a - hi
                    if gap < FRAME_MM:
                        rep.fail("doors", f"{op.tag} on wall {op.wi}: only {gap:.0f} mm from the face of wall {v.i} "
                                          f"at {mm2m(*w.pt(s, 0))} (need >= {FRAME_MM} mm for the frame)")
        for wi, lst in by_wall.items():
            lst = sorted(lst, key=lambda o: o.a)
            for x, y in zip(lst, lst[1:]):
                if y.a < x.b - 1e-6:
                    rep.fail("doors", f"{x.tag} and {y.tag} overlap on wall {wi} "
                                      f"({x.a:.0f}..{x.b:.0f} vs {y.a:.0f}..{y.b:.0f} mm)")
        # swings
        cut = {}
        for v in self.walls:
            if not v.ok:
                continue
            holes = [o.wall.rect(o.a, o.b) for o in self.ops if o.is_door and o.wall is v and o.width > 0]
            cut[v.i] = v.body.difference(unary_union(holes)) if holes else v.body
        doors = [o for o in self.ops if o.is_door and o.wall is not None and o.wall.ok and o.width > 0]
        for op in doors:
            if op.side is None:
                op.side = self.swing_side(op)
            op.sector = self.sector(op)
            core = op.sector.buffer(-5)
            for vi, geom in cut.items():
                if vi == op.wi:
                    continue
                x = core.intersection(geom)
                if x.area > 1e3:
                    c = x.centroid
                    rep.warn("doors", f"{op.tag} on wall {op.wi}: swing hits wall {vi} at {mm2m(c.x, c.y)}")
        for i, p in enumerate(doors):
            for q in doors[i + 1:]:
                x = p.sector.buffer(-5).intersection(q.sector.buffer(-5))
                if x.area > 1e4:
                    c = x.centroid
                    rep.warn("doors", f"{p.tag} (wall {p.wi}) swing overlaps {q.tag} (wall {q.wi}) swing "
                                      f"at {mm2m(c.x, c.y)}")
        rep.close("doors", start, f"{len(doors)} doors / {len(self.ops) - len(doors)} windows: placement, "
                                  f"swings and overlaps OK")

    # ---------------------------------------------------------- 4. dead space + sizes
    def min_for(self, r):
        typ = room_type(r)
        name = r.get("name", "").lower()
        ov_a = {k.lower(): v for k, v in (self.rules.get("min_room") or {}).items()}
        ov_w = {k.lower(): v for k, v in (self.rules.get("min_width") or {}).items()}
        a, w = (GENERIC_MIN.get(typ) or (None, None))
        sa = sw = GENERIC_SRC
        if self.country in COUNTRY_MIN:
            src, tab = COUNTRY_MIN[self.country]
            ca, cw = tab.get(typ, (None, None))
            if ca is not None:
                a, sa = ca, src
            if cw is not None:
                w, sw = cw, src
        for key in (typ, name):
            if key in ov_a:
                a, sa = ov_a[key], "spec rules.min_room"
            if key in ov_w:
                w, sw = ov_w[key], "spec rules.min_width"
        return typ, a, sa, w, sw

    @staticmethod
    def inscribed_width(geom):
        parts = list(geom.geoms) if geom.geom_type == "MultiPolygon" else [geom]
        best = 0.0
        for p in parts:
            if p.is_empty or p.area < 1:
                continue
            c = polylabel(p, tolerance=10)
            best = max(best, 2 * p.boundary.distance(c))
        return best / 1000

    def check_dead_space(self):
        rep, start = self.rep, len(self.rep.items)
        for ri, r in enumerate(self.rooms):
            lab = self.labels[ri]
            if room_type(r) != "corridor" or is_habitable(r) or not has_kw(room_text(r), CORRIDOR_KW):
                continue
            f = next((f for f in self.faces if ri in f["rooms"]), None)
            if f is None:
                continue
            doors = [d["tag"] for _, _, d in self.G.edges(lab, data=True)] if lab in self.G else []
            area = f["net_m2"]
            if len(doors) == 1 and area > DEAD_END_MIN_M2:
                rep.warn("dead-space", f"'{lab}' is a dead end: {area:.1f} m2 with a single door ({doors[0]}) "
                                       f"- circulation area that leads nowhere")
        rep.close("dead-space", start, "no dead-end corridor/hall over 6 m2")

    def check_sizes(self):
        rep, start = self.rep, len(self.rep.items)
        used = set()
        for ri, r in enumerate(self.rooms):
            f = next((f for f in self.faces if ri in f["rooms"]), None)
            if f is None:
                continue
            typ, a, sa, w, sw = self.min_for(r)
            if typ is None:
                continue
            lab = self.labels[ri]
            used.add(sa if a is not None else sw)
            if a is not None and f["net_m2"] < a - 1e-9:
                rep.warn("sizes", f"'{lab}' ({typ}) net area {f['net_m2']:.1f} m2 < minimum {a:g} m2 [{sa}]")
            if w is not None:
                width = self.inscribed_width(f["net"])
                if width < w - 1e-9:
                    rep.warn("sizes", f"'{lab}' ({typ}) min width {width:.2f} m < minimum {w:g} m [{sw}]")
        src = COUNTRY_MIN.get(self.country, (None,))[0]
        base = f"area/width minima: {src}; other types {GENERIC_SRC}" if src else \
            f"area/width minima: no room-size number in references/countries/{self.country or '??'}.md -> {GENERIC_SRC}"
        rep.close("sizes", start, base)

    # ---------------------------------------------------------- 5. habitability
    def check_habitability(self):
        rep, start = self.rep, len(self.rep.items)
        lit = set()
        for op in self.ops:
            if op.is_door or op.wall is None or not op.wall.ok or op.width <= 0:
                continue
            for A, B in self.sides(op):
                for x, y in ((A, B), (B, A)):
                    if y == OUT or self.is_courtyard(y):
                        lit.add(x)
        for ri, r in enumerate(self.rooms):
            lab = self.labels[ri]
            if is_habitable(r) and lab not in lit:
                rep.fail("habitability", f"Habitable room '{lab}' has no window to OUTSIDE or a courtyard")
        for op, A, B in self.door_edges:
            ra, rb = self.room_by_label(A), self.room_by_label(B)
            if not ra or not rb:
                continue
            for wet, other in ((ra, rb), (rb, ra)):
                if room_type(wet) in ("wc", "bathroom") and room_type(other) in ("kitchen", "dining", "majlis"):
                    rep.warn("habitability", f"{op.tag} on wall {op.wi}: '{wet['name']}' opens directly into "
                                             f"'{other['name']}' (add a lobby/vestibule)")
        rep.close("habitability", start, "every habitable room has a window to OUTSIDE/courtyard; "
                                         "no WC/bath door straight into kitchen/dining/majlis")

    # ---------------------------------------------------------- 6. privacy
    def check_privacy(self):
        rep, start = self.rep, len(self.rep.items)
        if self.country not in GULF:
            rep.add("PASS", "privacy", f"not applicable (country '{self.country}' is not a Gulf profile)")
            return
        guest, family = [], []
        for ri, r in enumerate(self.rooms):
            t = room_text(r)
            if has_kw(t, GUEST_ZONE_KW):
                guest.append(self.labels[ri])
            elif has_kw(t, FAMILY_ZONE_KW):
                family.append(self.labels[ri])
        if not guest or not family:
            rep.add("PASS", "privacy", "no separate majlis/guest and family/bedroom zones to compare")
            return
        D = nx.DiGraph()
        for _, A, B in self.door_edges:
            if OUT in (A, B):
                continue
            for u, v in ((A, B), (B, A)):
                c = D.get_edge_data(u, v, {}).get("capacity", 0)
                D.add_edge(u, v, capacity=c + 1)
        for g in guest:
            D.add_edge("_S", g)
        for f in family:
            D.add_edge(f, "_T")
        flow = nx.maximum_flow_value(D, "_S", "_T")
        if flow == 0:
            rep.add("PASS", "privacy", "majlis/guest zone has no indoor link to the family/bedroom zone")
        elif flow == 1:
            rep.add("PASS", "privacy", "majlis/guest zone reaches the family zone through a single controlled door")
        else:
            _, (S, T) = nx.minimum_cut(D, "_S", "_T")
            doors = sorted({t["tag"] for op, A, B in self.door_edges for t in [{"tag": op.tag}]
                            if (A in S and B in T) or (B in S and A in T)})
            rep.warn("privacy", f"majlis/guest rooms {guest} connect to family/bedroom rooms {family} by {flow} "
                                f"independent routes (doors {', '.join(doors)}); keep one controlled door")

    def run(self):
        self.check_rooms()
        self.check_circulation()
        self.check_doors()
        self.check_dead_space()
        self.check_sizes()
        self.check_habitability()
        self.check_privacy()


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("spec")
    ap.add_argument("--country", help="iso2 code; default: spec 'country'")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    args = ap.parse_args()
    try:
        spec = json.loads(Path(args.spec).read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        print(f"cannot read spec: {e}", file=sys.stderr)
        sys.exit(2)
    country = (args.country or spec.get("country") or "").lower()
    rep = Report()
    audit = Audit(spec, country, rep)
    audit.run()
    c = rep.counts()
    if args.json:
        print(json.dumps({"country": country, "summary": c, "findings": rep.items},
                         ensure_ascii=False, indent=1))
    else:
        print(f"plan_audit: {args.spec}  country={country or '?'}")
        for i in rep.items:
            print(f"{i['level']:<4} [{i['check']}] {i['message']}")
        print(f"SUMMARY: {c['PASS']} pass, {c['WARN']} warn, {c['FAIL']} fail")
    sys.exit(1 if c["FAIL"] else 0)


if __name__ == "__main__":
    main()
