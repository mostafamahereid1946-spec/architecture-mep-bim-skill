"""Build a 3D villa from a dxf_plan.py spec inside 3ds Max and render it (Arnold, sun & sky).

Run headless (Windows, licensed 3ds Max 2024+):
    set BS_SPEC=C:\\path\\plan.json
    set BS_OUT=C:\\path\\render.png
    "C:\\Program Files\\Autodesk\\3ds Max 2026\\3dsmaxbatch.exe" scripts\\max_massing.py

Optional env: BS_W/BS_H (pixels, default 1600x900), BS_HEIGHT (storey mm, 3300),
BS_RENDERER (art | arnold; Arnold watermarks batch renders without a batch licence),
BS_SECONDS (ART time budget, 120), BS_SAMPLES (Arnold AA, 4). Saves <out>.max next to the image.
Walls are split around openings exactly like the plan: sill + head pieces for
windows, lintel for doors, glass panes in window gaps.
"""
import json
import math
import os

from pymxs import runtime as rt

SPEC = json.load(open(os.environ["BS_SPEC"], encoding="utf-8"))
OUT = os.environ["BS_OUT"]
W, H = int(os.environ.get("BS_W", 1600)), int(os.environ.get("BS_H", 900))
STOREY = float(os.environ.get("BS_HEIGHT", 3300))
SILL, HEAD, DOOR_H, SLAB = 900.0, 2400.0, 2400.0, 300.0


def mat(name, rgb, rough, transparency=0.0):
    m = rt.PhysicalMaterial(name=name)
    m.base_color = rt.color(*rgb)
    m.roughness = rough
    if transparency:
        m.transparency = transparency
        m.trans_color = rt.color(220, 235, 240)
    return m


PLASTER = mat("Plaster_Warm", (232, 222, 204), 0.85)
STONE = mat("Stone_Base", (176, 160, 138), 0.7)
GLASS = mat("Glass_Clear", (40, 55, 60), 0.02, 0.9)
FRAME = mat("Frame_Bronze", (60, 50, 42), 0.35)
GROUND = mat("Ground_Paving", (150, 146, 138), 0.9)
WATER = mat("Water", (30, 105, 135), 0.03)
WOOD = mat("Wood_Teak", (122, 82, 50), 0.55)
MATS = {"plaster": PLASTER, "stone": STONE, "glass": GLASS, "frame": FRAME,
        "ground": GROUND, "water": WATER, "wood": WOOD}


def block(x, y, z, sx, sy, sz, angle, material, name):
    """Box centred on (x, y) in plan, base at z, length sx along `angle`."""
    b = rt.Box(width=sx, length=sy, height=sz, name=name)
    b.material = material
    rt.rotate(b, rt.EulerAngles(0, 0, angle))
    b.pos = rt.Point3(x, y, z)
    return b


def wall_pieces(i, w, openings):
    (x1, y1), (x2, y2) = w["from"], w["to"]
    length = math.hypot(x2 - x1, y2 - y1)
    ux, uy = (x2 - x1) / length, (y2 - y1) / length
    ang = math.degrees(math.atan2(uy, ux))
    t = w["thk"]
    at = lambda d: (x1 + ux * d, y1 + uy * d)

    def piece(a, b, z0, z1, m, tag):
        if b - a > 1 and z1 - z0 > 1:
            cx, cy = at((a + b) / 2)
            block(cx, cy, z0, b - a, t, z1 - z0, ang, m, f"W{i}_{tag}")

    cuts = sorted((o["at"], o["at"] + o["width"], o) for o in openings if o["wall"] == i)
    start = -t / 2
    for a, b, o in cuts:
        piece(start, a, 0, STOREY, PLASTER, "solid")
        if o["kind"] == "window":
            piece(a, b, 0, SILL, PLASTER, "sill")
            piece(a, b, HEAD, STOREY, PLASTER, "head")
            cx, cy = at((a + b) / 2)
            block(cx, cy, SILL, b - a, 20, HEAD - SILL, ang, GLASS, f"W{i}_glass")
            block(cx, cy, HEAD - 60, b - a, t + 20, 60, ang, FRAME, f"W{i}_frame")
        else:
            piece(a, b, DOOR_H, STOREY, PLASTER, "lintel")
        start = b
    piece(start, length + t / 2, 0, STOREY, PLASTER, "solid")


def extras():
    """Spec "massing": upper-floor blocks, pools, pergolas and mashrabiya/louvre fins.
    {"box": [x0, y0, x1, y1], "z": [z0, z1], "mat": "plaster|stone|glass|frame|water|wood",
     "kind": "fins", "spacing": 250}  -> fins run across the box's longer side."""
    for i, m in enumerate(SPEC.get("massing", [])):
        bx0, by0, bx1, by1 = m["box"]
        z0, z1 = m.get("z", [0, STOREY])
        material = MATS[m.get("mat", "plaster")]
        if m.get("kind") == "fins":
            step, along_x = m.get("spacing", 250), (bx1 - bx0) >= (by1 - by0)
            span = (bx1 - bx0) if along_x else (by1 - by0)
            for k in range(int(span // step) + 1):
                if along_x:
                    block(bx0 + k * step, (by0 + by1) / 2, z0, 60, by1 - by0, z1 - z0, 0, material, f"Fin{i}_{k}")
                else:
                    block((bx0 + bx1) / 2, by0 + k * step, z0, bx1 - bx0, 60, z1 - z0, 0, material, f"Fin{i}_{k}")
        else:
            block((bx0 + bx1) / 2, (by0 + by1) / 2, z0, bx1 - bx0, by1 - by0, z1 - z0, 0, material, f"Mass{i}")


def build():
    rt.resetMaxFile(rt.name("noPrompt"))
    rt.units.SystemType = rt.name("millimeters")
    walls, openings = SPEC["walls"], SPEC.get("openings", [])
    for i, w in enumerate(walls):
        wall_pieces(i, w, openings)
    xs = [c for w in walls for c in (w["from"][0], w["to"][0])]
    ys = [c for w in walls for c in (w["from"][1], w["to"][1])]
    x0, x1, y0, y1 = min(xs), max(xs), min(ys), max(ys)
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    ov = 900  # roof overhang for shade
    roofs = SPEC.get("roofs") or [[x0 - ov, y0 - ov, x1 + ov, y1 + ov]]   # leave courtyards open
    for i, (rx0, ry0, rx1, ry1) in enumerate(roofs):
        rcx, rcy = (rx0 + rx1) / 2, (ry0 + ry1) / 2
        block(rcx, rcy, STOREY, rx1 - rx0, ry1 - ry0, SLAB, 0, PLASTER, f"Roof_Slab{i}")
        block(rcx, rcy, STOREY + SLAB, rx1 - rx0, ry1 - ry0, 120, 0, PLASTER, f"Roof_Fascia{i}")
    extras()
    block(cx, cy, -150, x1 - x0 + 600, y1 - y0 + 600, 150, 0, STONE, "Plinth")
    g = rt.Plane(length=(y1 - y0) * 40, width=(x1 - x0) * 40, name="Ground")
    g.pos = rt.Point3(cx, cy, -155)
    g.material = GROUND
    return (x0, x1, y0, y1, cx, cy)


def light_and_camera(bounds):
    x0, x1, y0, y1, cx, cy = bounds
    sun = rt.SunPositioner()
    # real sun for the site: defaults to Doha, 21 March, 14:30 local
    env = os.environ.get
    for prop, val in (("north_direction_deg", 0.0), ("mode", 0),
                      ("latitude_deg", float(env("BS_LAT", 25.29))), ("longitude_deg", float(env("BS_LON", 51.53))),
                      ("time_zone", float(env("BS_TZ", 3))), ("dst", False),
                      ("year", 2026), ("month", int(env("BS_MONTH", 3))), ("day", 21),
                      ("hours", int(env("BS_HOUR", 14))), ("minutes", 30)):
        try:  # late-afternoon sun from the south-west
            setattr(sun, prop, val)
        except Exception as e:
            print(f"sun prop {prop} skipped: {e}")
    sky = rt.PhysicalSunSkyEnv()
    sky.sun_position_object = sun
    try:
        sky.haze = 0.15   # light Gulf haze; keeps the horizon from burning out
    except Exception as e:
        print(f"sky haze skipped: {e}")
    rt.environmentMap = sky
    rt.useEnvironmentMap = True
    span = max(x1 - x0, y1 - y0)
    cam = rt.Physical_Camera(name="Hero_Cam")
    cam.pos = rt.Point3(x0 - span * 0.55, y0 - span * 0.95, float(os.environ.get("BS_CAM_Z", 1700)))
    cam.target = rt.Targetobject(pos=rt.Point3(cx + span * 0.05, cy, STOREY * 0.45))
    for prop, val in (("focal_length_mm", 28.0), ("exposure_gain_type", 1), ("exposure_value", 15.0),
                      ("white_balance_type", 1), ("white_balance_kelvin", 6000.0),
                      ("auto_vertical_tilt_correction", True)):
        try:
            setattr(cam, prop, val)
        except Exception as e:
            print(f"camera prop {prop} skipped: {e}")
    try:
        rt.SceneExposureControl.exposureControl = rt.Physical_Camera_Exposure_Control()
    except Exception as e:
        print(f"exposure control skipped: {e}")
    return cam


def render(cam):
    # Arnold watermarks batch renders when its licence doesn't start in 3dsmaxbatch;
    # ART (Autodesk Raytracer) ships with Max, is physically based and unwatermarked.
    if os.environ.get("BS_RENDERER", "art") == "arnold":
        r = rt.Arnold()
        r.AA_samples = int(os.environ.get("BS_SAMPLES", 4))
    else:
        r = rt.ART_Renderer()
        for prop, val in (("enable_time", True), ("time_in_seconds", int(os.environ.get("BS_SECONDS", 120))),
                          ("enable_iterations", False), ("enable_noise_filter", True),
                          ("noise_filter_strength_percentage", 80.0)):
            try:
                setattr(r, prop, val)
            except Exception as e:
                print(f"ART prop {prop} skipped: {e}")
    rt.renderers.current = r
    rt.render(camera=cam, outputwidth=W, outputheight=H, outputfile=OUT, vfb=False)
    rt.saveMaxFile(os.path.splitext(OUT)[0] + ".max", quiet=True)
    print(f"BUILDING_SKILL_RENDER_DONE {OUT}")


render(light_and_camera(build()))
