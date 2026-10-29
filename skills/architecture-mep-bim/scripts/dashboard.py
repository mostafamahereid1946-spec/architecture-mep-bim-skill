#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Project dashboard: ONE static HTML file that shows a project folder at a glance.

Usage:
    uv run -q scripts/dashboard.py <project-folder> [-o dashboard.html]

Open the result by double-click (no server, no network, inline CSS/JS, system fonts).
Images and downloads are referenced by RELATIVE path, so zip the folder and share it.

Auto-discovered from the folder (every piece is optional):
  spec JSON(s)            walls + country + rooms  -> header, key numbers, room schedule, notes
  mall.json               level list + mall parameters (GLA, travel distance, parking, ...)
  <level>.dxf             AREA SCHEDULE and CODE CHECK lines are read from the sheet's MTEXT
  <level>-audit.txt       plan_audit.py output -> PASS / WARN / FAIL lists
  <level>-report.txt      acad_verify.py key=value report (AUDIT_ERRORS ...)
  <level>-MEP.*           MEP overlay (dxf / pdf / png)
  *.ifc, ifc.txt          BIM model and its validation line
  render*.jpg, *.jpg      renders; *.png plan / MEP previews
  qa-review.md            output of aec-qa-reviewer
  *.zip                   file names inside are checked for dxf / dwg / ifc
No dependency: the DXF is read with a small stdlib group-code reader (ezdxf not needed).
"""
from __future__ import annotations

import argparse
import ast
import datetime as _dt
import html
import json
import os
import re
import sys
import zipfile
from pathlib import Path
from urllib.parse import quote

HERE = Path(__file__).resolve().parent
PROFILES = HERE / "profiles"

COUNTRY_NAMES = {
    "ae": "United Arab Emirates", "au": "Australia", "bh": "Bahrain", "br": "Brazil", "ca": "Canada",
    "cn": "China", "de": "Germany", "eg": "Egypt", "es": "Spain", "fr": "France", "in": "India",
    "it": "Italy", "jo": "Jordan", "jp": "Japan", "kw": "Kuwait", "ma": "Morocco", "mx": "Mexico",
    "my": "Malaysia", "ng": "Nigeria", "om": "Oman", "pk": "Pakistan", "qa": "Qatar",
    "sa": "Saudi Arabia", "sg": "Singapore", "tr": "Turkey", "uk": "United Kingdom",
    "us": "United States", "za": "South Africa",
}
STAGES = [
    ("brief", "Brief", "الموجز"), ("code", "Code check", "فحص الكود"), ("drawings", "Drawings", "المخططات"),
    ("mep", "MEP", "الكهروميكانيكا"), ("bim", "BIM", "نمذجة المعلومات"), ("render", "Render", "التصيير"),
    ("qa", "QA review", "مراجعة الجودة"),
]
AR = {
    "Project dashboard": "لوحة المشروع", "Pipeline": "مراحل العمل", "Key numbers": "الأرقام الرئيسية",
    "Gallery": "المعرض", "Renders": "التصيير", "Drawings": "المخططات", "Code check": "فحص الكود",
    "Design audit": "تدقيق التصميم", "Room schedule": "جدول الغرف", "Downloads": "التنزيلات",
    "Verification": "التحقق", "Notes & assumptions": "ملاحظات وافتراضات", "QA review": "مراجعة الجودة",
    "Plot area": "مساحة القطعة", "Footprint": "مساحة البناء", "Coverage": "نسبة البناء",
    "Levels": "الأدوار", "Rooms": "الغرف", "PASS": "ناجح", "FAIL": "راسب", "WARN": "تحذير",
}
BUILDING_TYPES = [
    (r"mall|shopping", "Shopping mall", "مجمع تسوق"), (r"villa", "Villa", "فيلا"),
    (r"apartment|residential block|flats?", "Apartments", "شقق سكنية"), (r"office|tower", "Office", "مكاتب"),
    (r"school", "School", "مدرسة"), (r"hospital|clinic", "Healthcare", "رعاية صحية"),
    (r"mosque", "Mosque", "مسجد"), (r"hotel", "Hotel", "فندق"), (r"warehouse|factory", "Industrial", "صناعي"),
]
LEVEL_LIKE = re.compile(r"^(gf|g|b\d|l\d+|f\d+|rf|ff|sf|bsmt|basement|roof|\d+f)$", re.I)
IMG_EXT = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg"}
DL_EXT = {".dwg", ".dxf", ".pdf", ".ifc", ".json", ".max", ".zip", ".rvt", ".skp", ".blend", ".obj",
          ".fbx", ".3ds", ".csv", ".xlsx", ".md", ".txt"}
FLAG_RE = re.compile(r"assum|verify|⚠|rule of thumb|\bRoT\b", re.I)
KEYNAME = {"ACADVER": "ACAD version", "AUDIT_ERRORS": "AUDIT errors", "ON_LAYER_0": "On layer 0"}
STATE_LABEL = {"ok": "Done", "warn": "Review", "fail": "Fail", "none": "Missing"}


# ----------------------------------------------------------------------------- helpers
def esc(s) -> str:
    return html.escape("" if s is None else str(s), quote=True)


def read_text(p: Path) -> str:
    try:
        return p.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def load_json(p: Path):
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None


def human(n: int) -> str:
    x = float(n)
    for u in ("B", "KB", "MB", "GB"):
        if x < 1024 or u == "GB":
            return f"{x:.0f} {u}" if u == "B" else f"{x:.1f} {u}"
        x /= 1024
    return f"{n} B"


def flag_emoji(cc: str) -> str:
    cc = {"uk": "gb"}.get(cc.lower(), cc.lower())
    if len(cc) != 2 or not cc.isalpha():
        return "🏳"
    return "".join(chr(0x1F1E6 + ord(c) - 97) for c in cc)


def profile_value(cc: str, key: str, default=None, _depth=0):
    """Resolve a key through the profile's `extends` chain."""
    if _depth > 5 or not cc:
        return default
    d = load_json(PROFILES / f"{cc.lower()}.json")
    if not isinstance(d, dict):
        return default
    if key in d:
        return d[key]
    if d.get("extends"):
        return profile_value(d["extends"], key, default, _depth + 1)
    return default


def is_spec_file(p: Path) -> bool:
    if p.suffix.lower() != ".json" or p.name.lower() == "mall.json":
        return False
    head = read_text(p)[:6000] if p.stat().st_size < 50_000_000 else ""
    return '"walls"' in head and '"country"' in head


def dir_has_project(d: Path, depth: int = 2) -> bool:
    try:
        for c in d.iterdir():
            if c.is_file() and (c.name.lower() == "mall.json" or is_spec_file(c)):
                return True
            if c.is_dir() and depth > 0 and not c.name.startswith(".") and dir_has_project(c, depth - 1):
                return True
    except OSError:
        pass
    return False


# ----------------------------------------------------------------------------- parsers
def dxf_mtexts(path: Path) -> list[str]:
    """All MTEXT strings of a DXF (group codes 3 + 1 reassembled). Stdlib only."""
    lines = read_text(path).splitlines()
    out, cur, in_mtext = [], [], False
    for i in range(0, len(lines) - 1, 2):
        code, val = lines[i].strip(), lines[i + 1]
        if code == "0":
            if in_mtext and cur:
                out.append("".join(cur))
            cur, in_mtext = [], val.strip() == "MTEXT"
        elif in_mtext and code in ("3", "1"):
            cur.append(val)
    if in_mtext and cur:
        out.append("".join(cur))
    return out


def clean_mtext(s: str) -> list[str]:
    s = re.sub(r"\{\\[^;]*;|\}", "", s)
    s = re.sub(r"\\U\+([0-9A-Fa-f]{4})", lambda m: chr(int(m.group(1), 16)), s)
    return [x.strip() for x in s.replace("\\P", "\n").splitlines()]


def num(s):
    try:
        return float(s.replace(",", ""))
    except (ValueError, AttributeError):
        return None


def area_m2(line: str):
    m = re.search(r":\s*([\d,]+(?:\.\d+)?)\s*(\S*)", line)
    if not m:
        return None
    v = num(m.group(1))
    if v is None:
        return None
    unit = m.group(2).lower()
    if unit in ("sf", "sq", "ft²", "ft2"):
        v /= 10.7639
    return v


CHECK_RE = re.compile(
    r"^(?P<name>.+?)\s+(?P<act>-?[\d.,]+)\s*(?P<au>%|mm|m)?\s*(?P<op><=|>=|<|>)\s*(?P<lim>-?[\d.,]+)\s*"
    r"(?P<lu>%|mm|m)?\s*:\s*(?P<st>PASS|FAIL)", re.I)


def parse_dxf_sheet(path: Path) -> dict:
    """AREA SCHEDULE + CODE CHECK from the paper-space MTEXT that dxf_plan.py writes."""
    res = {"plot_m2": None, "foot_m2": None, "cov": None, "source": None, "rows": []}
    for raw in dxf_mtexts(path):
        if "AREA SCHEDULE" not in raw and "CODE CHECK" not in raw:
            continue
        in_check = False
        for line in clean_mtext(raw):
            if line.startswith("PLOT AREA"):
                res["plot_m2"] = area_m2(line)
            elif line.startswith("GROUND FLOOR FOOTPRINT"):
                res["foot_m2"] = area_m2(line)
            elif line.startswith("GROUND COVERAGE"):
                m = re.search(r":\s*([\d.]+)", line)
                res["cov"] = num(m.group(1)) if m else None
            elif line.startswith("CODE CHECK"):
                in_check = True
                m = re.match(r"CODE CHECK\s*\((.*)\)\s*$", line)
                res["source"] = m.group(1) if m else line[10:].strip()
            elif in_check and line:
                m = CHECK_RE.match(line)
                if m:
                    res["rows"].append(check_row(m))
    return res


def check_row(m) -> dict:
    name, au, lu = m["name"].strip(), m["au"] or "", m["lu"] or ""
    is_len = "setback" in name.lower() or au in ("mm", "m")

    def fmt(v, u):
        x = num(v)
        if x is None:
            return v
        if is_len and u != "m":
            return f"{x / 1000:.2f} m"
        return f"{x:g} {u}".strip()

    words = name.split()
    name = " ".join([words[0].capitalize()] + words[1:]) if words and words[0].isupper() else name
    return {"name": name, "actual": fmt(m["act"], au),
            "op": {"<=": "≤", ">=": "≥"}.get(m["op"], m["op"]), "limit": fmt(m["lim"], lu), "state": m["st"].upper()}


def compute_sheet(spec: dict) -> dict:
    """Fallback when no DXF exists: same arithmetic as dxf_plan.py (mm)."""
    res = {"plot_m2": None, "foot_m2": None, "cov": None, "source": None, "rows": []}
    walls = spec.get("walls") or []
    if not walls:
        return res
    xs = [c for w in walls for c in (w["from"][0], w["to"][0])]
    ys = [c for w in walls for c in (w["from"][1], w["to"][1])]
    half = max(w.get("thk", 0) for w in walls) / 2
    bx0, bx1, by0, by1 = min(xs) - half, max(xs) + half, min(ys) - half, max(ys) + half
    res["foot_m2"] = (bx1 - bx0) * (by1 - by0) / 1e6
    plot = (spec.get("plot") or {}).get("polygon")
    if plot:
        pts = [tuple(p) for p in plot]
        pa = abs(sum(x1 * y2 - x2 * y1 for (x1, y1), (x2, y2) in zip(pts, pts[1:] + pts[:1]))) / 2
        res["plot_m2"] = pa / 1e6
        res["cov"] = (bx1 - bx0) * (by1 - by0) / pa * 100
        rules = spec.get("rules") or {}
        if rules:
            res["source"] = rules.get("source", "source not given")
            px0, px1 = min(p[0] for p in pts), max(p[0] for p in pts)
            py0, py1 = min(p[1] for p in pts), max(p[1] for p in pts)
            gaps = {"south": by0 - py0, "north": py1 - by1, "west": bx0 - px0, "east": px1 - bx1}
            front = spec["plot"].get("front", "south")
            rear = {"south": "north", "north": "south", "east": "west", "west": "east"}[front]
            for side, gap in gaps.items():
                kind = "front" if side == front else "rear" if side == rear else "side"
                need = rules.get(kind)
                if need is not None:
                    res["rows"].append({"name": f"{side.capitalize()} {kind} setback", "actual": f"{gap / 1000:.2f} m",
                                        "op": "≥", "limit": f"{need / 1000:.2f} m",
                                        "state": "PASS" if gap >= need - 1e-6 else "FAIL"})
            if "coverage_max" in rules:
                res["rows"].append({"name": "Coverage", "actual": f"{res['cov']:.1f} %", "op": "≤",
                                    "limit": f"{rules['coverage_max']:g} %",
                                    "state": "PASS" if res["cov"] <= rules["coverage_max"] else "FAIL"})
    return res


def parse_audit(text: str) -> dict | None:
    items = []
    for line in text.splitlines():
        m = re.match(r"^(PASS|WARN|FAIL)\s+\[([^\]]+)\]\s*(.*)$", line.strip())
        if m:
            items.append({"state": m.group(1), "check": m.group(2), "msg": m.group(3)})
    if not items:
        return None
    count = {k: sum(1 for i in items if i["state"] == k) for k in ("PASS", "WARN", "FAIL")}
    return {"items": items, "count": count}


def parse_kv(text: str) -> dict:
    return {m.group(1): m.group(2) for m in re.finditer(r"^([A-Z_0-9]+)=(\S+)\s*$", text, re.M)}


def parse_ifc_txt(text: str) -> dict:
    out = {"counts": {}, "issues": None}
    m = re.search(r"\{.*?\}", text)
    if m:
        try:
            out["counts"] = ast.literal_eval(m.group(0))
        except (ValueError, SyntaxError):
            pass
    m = re.search(r"validation_issues=(\d+)", text)
    if m:
        out["issues"] = int(m.group(1))
    return out


def md_to_html(md: str) -> str:
    out, in_ul = [], False

    def inline(s):
        s = esc(s)
        s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
        return re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)

    for line in md.splitlines():
        m = re.match(r"^(#{1,4})\s+(.*)", line)
        b = re.match(r"^\s*(?:[-*]|\d+\.)\s+(.*)", line)
        if in_ul and not b:
            out.append("</ul>")
            in_ul = False
        if m:
            lvl = min(len(m.group(1)) + 2, 5)
            out.append(f"<h{lvl}>{inline(m.group(2))}</h{lvl}>")
        elif b:
            if not in_ul:
                out.append("<ul>")
                in_ul = True
            out.append(f"<li dir=\"auto\">{inline(b.group(1))}</li>")
        elif line.strip():
            out.append(f"<p dir=\"auto\">{inline(line)}</p>")
    if in_ul:
        out.append("</ul>")
    return "\n".join(out)


def qa_state(md: str) -> tuple[str, str]:
    sec, blockers, warns = None, 0, 0
    for line in md.splitlines():
        if re.match(r"^#{1,4}\s", line) or re.match(r"^\**(BLOCKERS|WARNINGS|NOT VERIFIED)\b", line.strip(), re.I):
            u = line.upper()
            sec = "B" if "BLOCKER" in u else "W" if "WARNING" in u else "O"
            continue
        b = re.match(r"^\s*(?:[-*]|\d+\.)\s+(.*)", line)
        if b and not re.match(r"^\W*(none|n/a|nil)\b", b.group(1), re.I):
            if sec == "B":
                blockers += 1
            elif sec == "W":
                warns += 1
    if blockers:
        return "fail", f"{blockers} blocker{'s' if blockers != 1 else ''}"
    if warns:
        return "warn", f"{warns} warning{'s' if warns != 1 else ''}"
    return "ok", "no blockers"


# ----------------------------------------------------------------------------- discovery
def classify_image(name: str) -> str:
    n = name.lower()
    ext = Path(n).suffix
    if "mep" in n:
        return "mep"
    if "render" in n or "perspective" in n or (ext in (".jpg", ".jpeg", ".webp") and "plan" not in n and "sheet" not in n):
        return "render"
    return "sheet" if "sheet" in n else "plan"


def level_order(stems: list[str]) -> list[str]:
    def key(s):
        m = re.match(r"^(b)(\d+)$", s, re.I)
        if m:
            return (0, -int(m.group(2)), s)
        if s.lower() in ("gf", "g", "ground"):
            return (1, 0, s)
        m = re.match(r"^l(\d+)$", s, re.I)
        if m:
            return (2, int(m.group(1)), s)
        return (3, 0, s.lower())
    return sorted(stems, key=key)


def collect(folder: Path, out_file: Path | None = None) -> dict:
    folder = folder.resolve()
    out_file = (out_file or folder / "dashboard.html").resolve()
    out_dir = out_file.parent
    if not folder.is_dir():
        sys.exit(f"not a folder: {folder}")

    # ---- files (depth <= 2, skipping sub-folders that are projects of their own)
    files: list[tuple[Path, int]] = []

    def walk(d: Path, depth: int):
        for c in sorted(d.iterdir(), key=lambda p: p.name.lower()):
            if c.name.startswith(".") or c.name.startswith("~"):
                continue
            if c.is_file():
                files.append((c, depth))
            elif depth < 2 and c.name.lower() not in ("node_modules", "__pycache__") and not dir_has_project(c):
                walk(c, depth + 1)
    walk(folder, 0)

    # ---- specs -> levels
    mall = None
    for p, d in files:
        if p.name.lower() == "mall.json" and d == 0:
            mall = load_json(p)
    spec_files = [p for p, d in files if d == 0 and is_spec_file(p)] or \
                 [p for p, d in files if d == 1 and is_spec_file(p)]
    specs = {}
    for p in spec_files:
        s = load_json(p)
        if isinstance(s, dict) and "walls" in s:
            specs[p.stem] = (p, s)
    order = []
    if isinstance(mall, dict) and isinstance(mall.get("files"), dict):
        order = [Path(v).stem for v in mall["files"].values() if Path(v).stem in specs]
    levels = order + level_order([k for k in specs if k not in order])
    stems = list(levels)

    first = specs[levels[0]][1] if levels else {}
    cc = str(first.get("country") or (mall or {}).get("country") or "").lower()
    project = first.get("project") or {}
    stem_scoped = len(stems) == 1 and not LEVEL_LIKE.match(stems[0]) and not mall

    def level_of(p: Path):
        n = p.name.lower()
        best = None
        for s in stems:
            sl = s.lower()
            if n.startswith(sl) and (len(n) == len(sl) or not n[len(sl)].isalnum()):
                if best is None or len(s) > len(best):
                    best = s
        return best

    mine = []
    for p, d in files:
        if p.suffix.lower() == ".html":
            continue
        lv = level_of(p)
        if lv is None and stem_scoped and d == 0 and not re.match(
                r"^(render[\w.\- ]*|qa-review\.md|ifc\.txt|mall\.json)$", p.name, re.I):
            continue
        mine.append((p, d, lv))

    def rel(p: Path) -> str:
        try:
            r = Path(os.path.relpath(p, out_dir))
        except ValueError:
            r = p
        return quote(str(r).replace("\\", "/"), safe="/")

    def by(lv, pred):
        return [p for p, _, l in mine if l == lv and pred(p)]

    # ---- per-level data
    lv_data = []
    for s in levels:
        sp_path, spec = specs[s]
        rooms = spec.get("rooms") or []
        dxfs = [p for p in by(s, lambda q: q.suffix.lower() == ".dxf") if "mep" not in q_name(p)]
        sheet = parse_dxf_sheet(dxfs[0]) if dxfs else None
        if not sheet or (sheet["plot_m2"] is None and sheet["foot_m2"] is None and not sheet["rows"]):
            sheet = compute_sheet(spec)
        audit_txt = by(s, lambda q: q.name.lower().endswith("-audit.txt") and "mep" not in q.name.lower())
        audit = parse_audit(read_text(audit_txt[0])) if audit_txt else None
        reports = {}
        for p in by(s, lambda q: q.name.lower().endswith("-report.txt")):
            reports["MEP" if "mep" in p.name.lower() else "Plan"] = parse_kv(read_text(p))
        pr = spec.get("project") or {}
        label = pr.get("drawing") or s
        tab = f"{s} · {label}" if label != s and len(s) <= 4 else label
        lv_data.append({
            "stem": s, "label": label, "tab": tab, "spec": spec, "sheet": sheet, "audit": audit,
            "reports": reports, "rooms": rooms, "title_ar": pr.get("drawing_ar"),
            "has": {
                "dxf": bool(dxfs), "dwg": bool(by(s, lambda q: q.suffix.lower() == ".dwg" and "mep" not in q.name.lower())),
                "pdf": bool(by(s, lambda q: q.suffix.lower() == ".pdf" and "mep" not in q.name.lower())),
                "mep_dxf": bool(by(s, lambda q: q.suffix.lower() == ".dxf" and "mep" in q.name.lower())),
                "mep_dwg": bool(by(s, lambda q: q.suffix.lower() == ".dwg" and "mep" in q.name.lower())),
                "mep_pdf": bool(by(s, lambda q: q.suffix.lower() == ".pdf" and "mep" in q.name.lower())),
                "ifc": bool(by(s, lambda q: q.suffix.lower() == ".ifc")),
            },
        })

    # ---- zips: look inside
    zip_names: list[str] = []
    zips = []
    for p, _, _ in mine:
        if p.suffix.lower() == ".zip":
            try:
                with zipfile.ZipFile(p) as z:
                    names = z.namelist()
                zip_names += names
                zips.append((p, names))
            except (zipfile.BadZipFile, OSError):
                pass
    zl = [n.lower() for n in zip_names]
    zip_has = {k: any(n.endswith(k) for n in zl) for k in (".dxf", ".dwg", ".ifc", ".pdf")}
    zip_mep = any("mep" in n and n.endswith((".dxf", ".dwg")) for n in zl)

    # ---- images
    images = []
    for p, d, lv in mine:
        if p.suffix.lower() in IMG_EXT:
            images.append({"path": p, "rel": rel(p), "kind": classify_image(p.name), "level": lv, "name": p.name})
    # ---- qa review
    qa_files = [p for p, _, _ in mine if p.name.lower() in ("qa-review.md", "qa_review.md")]
    qa_md = read_text(qa_files[0]) if qa_files else ""
    # ---- ifc
    ifc_files = [p for p, _, _ in mine if p.suffix.lower() == ".ifc"]
    ifc_txt = [p for p, _, _ in mine if p.name.lower() in ("ifc.txt",)]
    ifc_info = parse_ifc_txt(read_text(ifc_txt[0])) if ifc_txt else {"counts": {}, "issues": None}

    # ---- downloads
    downloads = []
    for p, _, lv in mine:
        ext = p.suffix.lower()
        if ext in DL_EXT:
            note = ""
            for zp, names in zips:
                if zp == p:
                    note = f"{len(names)} files: " + ", ".join(names[:6]) + (" …" if len(names) > 6 else "")
            downloads.append({"name": p.name, "rel": rel(p), "ext": ext[1:].upper(), "size": p.stat().st_size,
                              "level": lv, "note": note, "mep": "mep" in p.name.lower()})
    order_ext = {"DWG": 0, "DXF": 1, "PDF": 2, "IFC": 3, "JSON": 4, "MAX": 5, "ZIP": 6}
    downloads.sort(key=lambda d: (levels.index(d["level"]) if d["level"] in levels else 99, d["mep"],
                                  order_ext.get(d["ext"], 9), d["name"].lower()))

    # ---- totals
    g = lv_data[0] if lv_data else None
    sheet = g["sheet"] if g else {"plot_m2": None, "foot_m2": None, "cov": None, "source": None, "rows": []}
    rooms_total = sum(len(l["rooms"]) for l in lv_data)
    all_rows = []
    for l in lv_data:
        for r in l["sheet"]["rows"]:
            all_rows.append({**r, "level": l["stem"]})
    # rows repeated on several levels are shown once
    seen, code_rows = set(), []
    for r in all_rows:
        k = (r["name"].lower(), r["actual"], r["limit"], r["state"])
        if k not in seen:
            seen.add(k)
            code_rows.append(r)
    sources = [l["sheet"]["source"] for l in lv_data if l["sheet"]["source"]]
    code_source = sources[0] if sources else ((first.get("rules") or {}).get("source"))

    mall_rows = mall_param_rows(mall) if isinstance(mall, dict) else []

    bilingual = bool(profile_value(cc, "bilingual", False)) or any(
        r.get("name_ar") for l in lv_data for r in l["rooms"][:3])
    title = project.get("title") or (mall or {}).get("title") or folder.name
    btype, btype_ar = infer_type(title, mall, project)
    country_name = (mall or {}).get("profile_country") or profile_value(cc, "country") or COUNTRY_NAMES.get(cc, cc.upper())
    date = project.get("date") or ""

    D = {
        "folder": folder, "title": title, "title_ar": project.get("title_ar"), "cc": cc, "country": country_name,
        "flag": flag_emoji(cc) if cc else "", "type": btype, "type_ar": btype_ar, "date": date,
        "client": project.get("client"), "plot_no": project.get("plot"), "bilingual": bilingual,
        "levels": lv_data, "mall": mall if isinstance(mall, dict) else None, "mall_rows": mall_rows,
        "sheet": sheet, "rooms_total": rooms_total, "code_rows": code_rows, "code_source": code_source,
        "notes": (first.get("notes") or []), "images": images, "downloads": downloads, "ifc_info": ifc_info,
        "qa_md": qa_md, "qa_name": qa_files[0].name if qa_files else None, "zips": zips,
        "stem_scoped": stem_scoped,
    }
    D["pipeline"] = pipeline(D, zip_has, zip_mep, ifc_files)
    D["audit_total"] = {k: sum((l["audit"] or {"count": {}})["count"].get(k, 0) for l in lv_data)
                        for k in ("PASS", "WARN", "FAIL")}
    D["has_audit"] = any(l["audit"] for l in lv_data)
    return D


def q_name(p: Path) -> str:
    return p.name.lower()


def infer_type(title, mall, project):
    if mall:
        return "Shopping mall", "مجمع تسوق"
    for k in ("type", "building_type", "use"):
        if project.get(k):
            return str(project[k]), None
    for pat, en, ar in BUILDING_TYPES:
        if re.search(pat, title or "", re.I):
            return en, ar
    return "Building", "مبنى"


def mall_param_rows(m: dict) -> list[dict]:
    """Rows for design parameters recorded by gen_mall.py (value, status, source)."""
    rows = []

    def add(name, value, state, source, warn=False):
        rows.append({"name": name, "value": value, "state": state, "source": source or "", "warn": bool(warn)})

    t = m.get("travel")
    if isinstance(t, dict):
        comp = t.get("computed") or []
        worst = max((c.get("max_m", 0) for c in comp), default=None)
        lim = t.get("limit_m")
        ok = t.get("ok", worst is not None and lim is not None and worst <= lim)
        add("Travel distance to exit", f"max {worst:g} m ≤ {lim:g} m" if worst is not None and lim is not None else "",
            "PASS" if ok else "FAIL", t.get("source"), t.get("warn"))
    p = m.get("parking")
    if isinstance(p, dict):
        add("Parking shown vs required", f"{p.get('shown')} of {p.get('required')} bays",
            "WARN" if p.get("shown", 0) < p.get("required", 0) else "PASS", p.get("source"), p.get("warn"))
    sw = m.get("stair_clear_width_mm")
    if isinstance(sw, dict):
        add("Stair clear width", f"{sw.get('value', 0) / 1000:.2f} m", "PASS", sw.get("source"), sw.get("warn"))
    h = m.get("gf_height_mm")
    if isinstance(h, dict):
        add("Ground-floor height", f"{h.get('value', 0) / 1000:.1f} m", "PASS", h.get("source"), h.get("warn"))
    sp = m.get("sprinkler")
    if isinstance(sp, dict):
        add("Sprinkler design", f"{sp.get('std')} · {sp.get('max_area')} m² / {sp.get('max_spacing', 0) / 1000:.1f} m",
            "PASS", sp.get("src"), False)
    return rows


def pipeline(D, zip_has, zip_mep, ifc_files) -> list[dict]:
    L = D["levels"]
    has = lambda k: any(l["has"][k] for l in L)
    imgs = D["images"]
    st = []

    # 1 brief
    if L:
        n = D["rooms_total"]
        assum = any("ASSUMPTION" in str(x).upper() for x in D["notes"])
        st.append(("brief", "ok", f"{n} rooms · {len(L)} level{'s' if len(L) != 1 else ''}" + (" · assumptions listed" if assum else "")))
    else:
        st.append(("brief", "none", "no spec JSON"))

    # 2 code
    rows = D["code_rows"]
    at = {k: sum((l["audit"] or {"count": {}})["count"].get(k, 0) for l in L) for k in ("PASS", "WARN", "FAIL")}
    nfail = sum(1 for r in rows if r["state"] == "FAIL") + at["FAIL"]
    nflag = (1 if FLAG_RE.search(D["code_source"] or "") else 0) + at["WARN"] + sum(1 for r in D["mall_rows"] if r["warn"])
    if not rows and not any(l["audit"] for l in L):
        st.append(("code", "none", "no code check or audit found"))
    else:
        s = "fail" if nfail else "warn" if nflag else "ok"
        bits = []
        if rows:
            bits.append(f"{sum(1 for r in rows if r['state'] == 'PASS')}/{len(rows)} code checks pass")
        if any(l["audit"] for l in L):
            bits.append(f"audit {at['PASS']} pass · {at['WARN']} warn · {at['FAIL']} fail")
        if s == "warn" and not at["WARN"]:
            bits.append("⚠ verify flags")
        st.append(("code", s, " · ".join(bits)))

    # 3 drawings
    dxf, dwg, pdf = has("dxf"), has("dwg"), has("pdf")
    kinds = [n for n, f in (("DXF", dxf), ("DWG", dwg), ("PDF", pdf)) if f]
    acad_err = [int(r.get("AUDIT_ERRORS", 0)) for l in L for k, r in l["reports"].items() if k == "Plan" and str(r.get("AUDIT_ERRORS", "")).isdigit()]
    if dxf and (pdf or dwg) and not any(acad_err):
        st.append(("drawings", "ok", " · ".join(kinds) + (" · AutoCAD AUDIT 0" if acad_err else "")))
    elif kinds:
        st.append(("drawings", "warn", " · ".join(kinds) + (" · AUDIT errors" if any(acad_err) else " · incomplete set")))
    elif any(zip_has[k] for k in (".dxf", ".dwg", ".pdf")):
        st.append(("drawings", "warn", "inside zip only"))
    elif any(i["kind"] in ("plan", "sheet") for i in imgs):
        st.append(("drawings", "warn", "preview image only"))
    else:
        st.append(("drawings", "none", "no DXF / PDF found"))

    # 4 mep
    mep_files = has("mep_dxf") or has("mep_dwg")
    mep_pdf = has("mep_pdf") or any(i["kind"] == "mep" for i in imgs)
    mrep = [r for l in L for k, r in l["reports"].items() if k == "MEP"]
    mep_err = any(r.get("AUDIT_ERRORS", "0") not in ("0", "") for r in mrep)
    if mep_files and mep_pdf and not mep_err:
        st.append(("mep", "ok", "MEP overlay · " + ("AutoCAD AUDIT 0" if mrep else "dxf + preview")))
    elif mep_files or mep_pdf or zip_mep:
        st.append(("mep", "warn", "MEP overlay " + ("in zip" if zip_mep and not mep_files else "partial")))
    else:
        st.append(("mep", "none", "no -MEP file found"))

    # 5 bim
    ii = D["ifc_info"]
    if ifc_files:
        size = human(sum(p.stat().st_size for p in ifc_files))
        if ii["issues"] is None:
            st.append(("bim", "warn", f"IFC {size} · not validated"))
        elif ii["issues"] == 0:
            n = sum(ii["counts"].values()) if ii["counts"] else 0
            st.append(("bim", "ok", f"IFC {size} · 0 validation issues" + (f" · {n} elements" if n else "")))
        else:
            st.append(("bim", "warn", f"IFC {size} · {ii['issues']} validation issues"))
    elif zip_has[".ifc"]:
        st.append(("bim", "warn", "IFC inside zip"))
    else:
        st.append(("bim", "none", "no IFC found"))

    # 6 render
    rn = [i for i in imgs if i["kind"] == "render"]
    st.append(("render", "ok", f"{len(rn)} image{'s' if len(rn) != 1 else ''}") if rn else ("render", "none", "no render image"))

    # 7 qa
    if D["qa_md"]:
        s, d = qa_state(D["qa_md"])
        st.append(("qa", s, d))
    else:
        st.append(("qa", "none", "no qa-review.md"))

    names = {k: (en, ar) for k, en, ar in STAGES}
    return [{"key": k, "en": names[k][0], "ar": names[k][1], "state": s, "detail": d} for k, s, d in st]


# ----------------------------------------------------------------------------- rendering
CSS = r"""
:root{
  --bg:#f5f4f0;--card:#fff;--ink:#1b1d22;--ink2:#545a66;--line:#e4e2db;--soft:#efede7;
  --accent:#3b5bdb;--accent-ink:#fff;--accent-soft:#e8ecfc;
  --ok:#2b7a4b;--ok-soft:#e3f2e8;--warn:#a86a0a;--warn-soft:#fbefd5;--fail:#b3261e;--fail-soft:#fbe4e1;--none:#8b909a;--none-soft:#ecebe6;
  --shadow:0 1px 2px rgba(20,22,30,.04),0 6px 24px rgba(20,22,30,.05);--r:14px;
  --sans:ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,"Helvetica Neue",Tahoma,Arial,sans-serif;
  --mono:ui-monospace,SFMono-Regular,Consolas,Menlo,monospace;
}
@media (prefers-color-scheme:dark){:root{
  --bg:#111215;--card:#1a1c21;--ink:#ecedf0;--ink2:#a0a6b2;--line:#2a2d34;--soft:#22252b;
  --accent:#8aa0ff;--accent-ink:#0d1020;--accent-soft:#222a4a;
  --ok:#62cf8f;--ok-soft:#173222;--warn:#f0b95a;--warn-soft:#38290e;--fail:#ff8a80;--fail-soft:#40191a;--none:#80858f;--none-soft:#24262c;
  --shadow:0 1px 2px rgba(0,0,0,.3),0 6px 24px rgba(0,0,0,.25)}}
*{box-sizing:border-box}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.55 var(--sans);overflow-x:hidden}
a{color:var(--accent);text-decoration:none}a:hover{text-decoration:underline}
img{max-width:100%;display:block}
.wrap{max-width:1160px;margin:0 auto;padding:0 clamp(16px,4vw,40px)}
.ar{font-family:var(--sans);color:var(--ink2);font-weight:400}
.lbl .ar,.eyebrow .ar{margin-left:.6em;font-size:.92em;letter-spacing:0}
.stat span .ar,.step .nm .ar{display:block;text-align:left}
.eyebrow{font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--accent);font-weight:600}
header.top{padding:clamp(28px,6vw,64px) 0 8px}
h1{font-size:clamp(28px,5vw,46px);line-height:1.1;margin:.3em 0 .15em;font-weight:650;letter-spacing:-.02em;overflow-wrap:anywhere}
.h1ar{font-size:clamp(20px,3vw,28px);color:var(--ink2);margin:0 0 .6em;text-align:left}
.meta{display:flex;flex-wrap:wrap;gap:8px 10px;margin:16px 0 0;padding:0;list-style:none}
.meta li{background:var(--card);border:1px solid var(--line);border-radius:999px;padding:5px 13px;font-size:13.5px;display:flex;gap:7px;align-items:center}
.flag{font-family:"Apple Color Emoji","Segoe UI Emoji","Noto Color Emoji",sans-serif;font-size:1.15em;line-height:1}
nav.sec{position:sticky;top:0;z-index:20;background:color-mix(in srgb,var(--bg) 88%,transparent);backdrop-filter:blur(10px);
  border-bottom:1px solid var(--line);margin-top:22px}
nav.sec .wrap{display:flex;gap:4px 18px;flex-wrap:wrap;padding-top:9px;padding-bottom:9px}
nav.sec a{font-size:13px;color:var(--ink2);padding:2px 0;border-bottom:2px solid transparent}
nav.sec a:hover{color:var(--ink);text-decoration:none;border-color:var(--accent)}
section{padding:clamp(28px,5vw,52px) 0 0;scroll-margin-top:50px}
h2{font-size:12.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--ink2);font-weight:650;margin:0 0 16px;display:flex;align-items:baseline;gap:.2em;flex-wrap:wrap}
h2 .ar{text-transform:none;letter-spacing:0;font-size:14px;margin-left:.7em}
h3{font-size:15px;margin:22px 0 8px;font-weight:650}
.card{background:var(--card);border:1px solid var(--line);border-radius:var(--r);box-shadow:var(--shadow)}
.pad{padding:clamp(14px,2.5vw,22px)}
/* pipeline */
.pipe{display:grid;grid-template-columns:repeat(7,1fr);gap:0;list-style:none;margin:0;padding:0;counter-reset:s}
.step{position:relative;padding:18px 14px 16px;border-inline-end:1px solid var(--line)}
.step:last-child{border-inline-end:0}
.step .n{font-size:11.5px;color:var(--ink2);letter-spacing:.08em}
.step .nm{font-weight:650;font-size:14.5px;margin:2px 0 8px;display:block}
.step .nm .ar{font-size:12px}
.step .d{font-size:12px;color:var(--ink2);margin-top:8px;line-height:1.4;overflow-wrap:anywhere}
.step::before{content:"";position:absolute;inset-inline:0;top:0;height:4px;background:var(--c)}
.s-ok{--c:var(--ok)}.s-warn{--c:var(--warn)}.s-fail{--c:var(--fail)}.s-none{--c:var(--line)}
.pill{display:inline-flex;align-items:center;gap:6px;font-size:11.5px;font-weight:650;border-radius:999px;padding:2px 10px;white-space:nowrap}
.pill::before{content:"";width:7px;height:7px;border-radius:50%;background:currentColor}
.p-ok,.PASS{color:var(--ok);background:var(--ok-soft)}.p-warn,.WARN{color:var(--warn);background:var(--warn-soft)}
.p-fail,.FAIL{color:var(--fail);background:var(--fail-soft)}.p-none{color:var(--none);background:var(--none-soft)}
/* stats */
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px}
.stat{padding:16px 18px}
.stat b{display:block;font-size:clamp(24px,3.4vw,32px);font-weight:600;letter-spacing:-.02em;line-height:1.15}
.stat b small{font-size:.5em;font-weight:500;color:var(--ink2);margin-inline-start:4px;letter-spacing:0}
.stat span{font-size:12.5px;color:var(--ink2)}
.stat span .ar{font-size:11.5px}
/* gallery */
.hero{display:block;position:relative;width:100%;padding:0;border:0;border-radius:var(--r);overflow:hidden;background:#222;cursor:zoom-in;box-shadow:var(--shadow)}
.hero img{width:100%;max-height:min(70vh,640px);object-fit:cover}
.cap{position:absolute;inset-inline:0;bottom:0;padding:26px 16px 12px;color:#fff;font-size:13px;text-align:start;background:linear-gradient(transparent,rgba(0,0,0,.6))}
.thumbs{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:10px;margin-top:10px}
.thumbs button{padding:0;border:1px solid var(--line);border-radius:10px;overflow:hidden;cursor:zoom-in;background:#222;aspect-ratio:16/10}
.thumbs img{width:100%;height:100%;object-fit:cover}
.sheets{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,420px),1fr));gap:16px}
.sheet{overflow:hidden}
.sheet button{display:block;width:100%;padding:0;border:0;background:#fff;cursor:zoom-in;border-bottom:1px solid var(--line)}
.sheet img{width:100%;height:auto;aspect-ratio:3/2;object-fit:contain;background:#fff}
.sheet figcaption{padding:11px 16px;font-size:13px;display:flex;justify-content:space-between;gap:10px;flex-wrap:wrap;color:var(--ink2)}
.sheet figcaption b{color:var(--ink);font-weight:600}
/* tabs */
.tablist{display:flex;gap:6px;flex-wrap:wrap;margin:0 0 14px}
.tablist button{font:inherit;font-size:13px;border:1px solid var(--line);background:var(--card);color:var(--ink2);padding:6px 14px;border-radius:999px;cursor:pointer}
.tablist button[aria-selected=true]{background:var(--accent);border-color:var(--accent);color:var(--accent-ink);font-weight:600}
.tabpanel[hidden]{display:none}
/* tables */
.tw{overflow-x:auto;-webkit-overflow-scrolling:touch}
table{border-collapse:collapse;width:100%;font-size:13.5px}
th{text-align:start;font-size:11.5px;letter-spacing:.08em;text-transform:uppercase;color:var(--ink2);font-weight:600;padding:10px 14px;border-bottom:1px solid var(--line);white-space:nowrap}
td{padding:10px 14px;border-bottom:1px solid var(--line);vertical-align:top}
tr:last-child td{border-bottom:0}
td.num,th.num{text-align:end;font-variant-numeric:tabular-nums;white-space:nowrap}
td.src{color:var(--ink2);font-size:12.5px;overflow-wrap:anywhere}
.prow{display:grid;grid-template-columns:minmax(150px,1.2fr) minmax(150px,1.3fr) 76px minmax(0,2.4fr);gap:4px 16px;align-items:start;padding:12px 18px;border-bottom:1px solid var(--line);font-size:13.5px}
.prow:last-child{border-bottom:0}.prow .v{font-variant-numeric:tabular-nums}.prow .src{color:var(--ink2);font-size:12.5px;overflow-wrap:anywhere}
.prow .pill{justify-self:start}
@media (max-width:760px){.prow{grid-template-columns:1fr auto}.prow .v{grid-column:1;grid-row:2}.prow .pill{grid-column:2;grid-row:1}.prow .src{grid-column:1/3}}
.warnmark{color:var(--warn);font-weight:700}
tfoot td{font-weight:600;border-top:1px solid var(--line);background:var(--soft)}
.filter{font:inherit;font-size:13.5px;border:1px solid var(--line);background:var(--card);color:var(--ink);border-radius:10px;padding:8px 12px;width:min(100%,280px);margin-bottom:12px}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:14px}
.chip{border-radius:10px;padding:6px 12px;font-size:13px;font-weight:600}
.dl td:first-child{overflow-wrap:anywhere}
.ext{font-family:var(--mono);font-size:11px;font-weight:700;padding:2px 7px;border-radius:6px;background:var(--accent-soft);color:var(--accent);margin-inline-end:8px}
.kv{display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:8px 18px;margin:0}
.kv div{display:flex;flex-direction:column}.kv dt{font-size:11.5px;color:var(--ink2);letter-spacing:.04em}.kv dd{margin:0;font-weight:600;font-variant-numeric:tabular-nums}
.two{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,340px),1fr));gap:16px}
ul.notes{margin:0;padding-inline-start:1.2em;color:var(--ink2);font-size:13.5px}ul.notes li{margin:5px 0}
.md h3,.md h4,.md h5{margin:18px 0 6px}.md code{font-family:var(--mono);font-size:.9em;background:var(--soft);padding:1px 5px;border-radius:5px}
footer{padding:48px 0 56px;color:var(--ink2);font-size:12.5px}
.empty{color:var(--ink2);font-size:13.5px;padding:6px 0}
/* lightbox */
#lb{position:fixed;inset:0;z-index:100;background:rgba(8,9,12,.94);display:none;flex-direction:column;touch-action:none}
#lb.on{display:flex}
#lb .bar{display:flex;align-items:center;gap:8px;padding:10px 14px;color:#e8e9ec;font-size:13px}
#lb .bar span{flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
#lb button{font:inherit;background:#2a2d35;color:#fff;border:0;border-radius:8px;min-width:36px;height:36px;cursor:pointer;font-size:16px}
#lb button:hover{background:#3b3f4a}
#lb .stage{flex:1;overflow:hidden;position:relative;cursor:grab}
#lb img{position:absolute;left:50%;top:50%;max-width:none;transform-origin:0 0;user-select:none;-webkit-user-drag:none;background:#fff}
@media (max-width:860px){
  .pipe{grid-template-columns:1fr}
  .step{display:grid;grid-template-columns:34px 1fr auto;gap:2px 10px;align-items:center;border-inline-end:0;border-bottom:1px solid var(--line);padding:12px 14px 12px 18px}
  .step:last-child{border-bottom:0}
  .step::before{inset-inline:auto;inset-block:0;inset-inline-start:0;width:4px;height:auto}
  .step .nm{margin:0}.step .nm .ar{display:inline;margin-left:.5em}
  .step .d{grid-column:2/4;margin-top:0}
  .step .pill{grid-column:3;grid-row:1}
  .step .n{grid-row:1}
}
@media (max-width:560px){th,td{padding:9px 9px}.thumbs{grid-template-columns:repeat(2,1fr)}nav.sec{position:static}}
@media print{nav.sec,#lb{display:none}body{background:#fff}}
"""

JS = r"""
(function(){
 // tabs
 document.querySelectorAll('[data-tabs]').forEach(function(g){
  var btns=g.querySelectorAll(':scope > .tablist > button'),panels=g.querySelectorAll(':scope > .tabpanel');
  btns.forEach(function(b){b.addEventListener('click',function(){
   btns.forEach(function(x){x.setAttribute('aria-selected',x===b)});
   panels.forEach(function(p){p.hidden=p.id!==b.dataset.tab});});});});
 // filters
 document.querySelectorAll('input[data-filter]').forEach(function(inp){
  inp.addEventListener('input',function(){var q=inp.value.toLowerCase(),t=document.getElementById(inp.dataset.filter);
   t.querySelectorAll('tbody tr').forEach(function(r){r.hidden=q&&r.textContent.toLowerCase().indexOf(q)<0});});});
 // lightbox
 var lb=document.getElementById('lb');if(!lb)return;
 var img=lb.querySelector('img'),cap=lb.querySelector('.bar span'),stage=lb.querySelector('.stage');
 var items=[].slice.call(document.querySelectorAll('[data-zoom]')),idx=0,sc=1,fit=1,ox=0,oy=0,nw=0,nh=0;
 function apply(){img.style.transform='translate('+ox+'px,'+oy+'px) scale('+sc+')'}
 function reset(){var W=stage.clientWidth,H=stage.clientHeight;nw=img.naturalWidth||W;nh=img.naturalHeight||H;
  fit=Math.min(W/nw,H/nh,1.0);sc=fit;ox=-(nw*sc)/2;oy=-(nh*sc)/2;img.style.left='50%';img.style.top='50%';apply()}
 function zoomAt(f,cx,cy){var W=stage.clientWidth/2,H=stage.clientHeight/2,ns=Math.max(fit*.5,Math.min(sc*f,fit*12));
  var px=cx-W,py=cy-H;ox=px-(px-ox)*(ns/sc);oy=py-(py-oy)*(ns/sc);sc=ns;apply()}
 function show(i){idx=(i+items.length)%items.length;var el=items[idx];cap.textContent=(idx+1)+' / '+items.length+'  ·  '+(el.dataset.cap||'');
  img.onload=reset;img.src=el.dataset.zoom;if(img.complete&&img.naturalWidth)reset();}
 function open(i){lb.classList.add('on');document.body.style.overflow='hidden';show(i)}
 function close(){lb.classList.remove('on');document.body.style.overflow='';img.removeAttribute('src')}
 items.forEach(function(el,i){el.addEventListener('click',function(){open(i)})});
 lb.querySelector('[data-a=close]').onclick=close;lb.querySelector('[data-a=prev]').onclick=function(){show(idx-1)};
 lb.querySelector('[data-a=next]').onclick=function(){show(idx+1)};
 lb.querySelector('[data-a=in]').onclick=function(){zoomAt(1.4,stage.clientWidth/2,stage.clientHeight/2)};
 lb.querySelector('[data-a=out]').onclick=function(){zoomAt(1/1.4,stage.clientWidth/2,stage.clientHeight/2)};
 lb.querySelector('[data-a=fit]').onclick=reset;
 stage.addEventListener('wheel',function(e){e.preventDefault();var r=stage.getBoundingClientRect();zoomAt(e.deltaY<0?1.15:1/1.15,e.clientX-r.left,e.clientY-r.top)},{passive:false});
 var drag=null,pts={},pd=0;
 stage.addEventListener('pointerdown',function(e){stage.setPointerCapture(e.pointerId);pts[e.pointerId]=[e.clientX,e.clientY];drag=[e.clientX,e.clientY,ox,oy];
  var k=Object.keys(pts);if(k.length==2)pd=Math.hypot(pts[k[0]][0]-pts[k[1]][0],pts[k[0]][1]-pts[k[1]][1])});
 stage.addEventListener('pointermove',function(e){if(!pts[e.pointerId])return;pts[e.pointerId]=[e.clientX,e.clientY];var k=Object.keys(pts);
  if(k.length==2){var d=Math.hypot(pts[k[0]][0]-pts[k[1]][0],pts[k[0]][1]-pts[k[1]][1]);if(pd){var r=stage.getBoundingClientRect();
   zoomAt(d/pd,(pts[k[0]][0]+pts[k[1]][0])/2-r.left,(pts[k[0]][1]+pts[k[1]][1])/2-r.top)}pd=d;return}
  if(drag){ox=drag[2]+e.clientX-drag[0];oy=drag[3]+e.clientY-drag[1];apply()}});
 function up(e){delete pts[e.pointerId];pd=0;drag=null}
 stage.addEventListener('pointerup',up);stage.addEventListener('pointercancel',up);
 stage.addEventListener('dblclick',function(){sc>fit*1.01?reset():zoomAt(2.5,stage.clientWidth/2,stage.clientHeight/2)});
 document.addEventListener('keydown',function(e){if(!lb.classList.contains('on'))return;
  if(e.key==='Escape')close();else if(e.key==='ArrowRight')show(idx+1);else if(e.key==='ArrowLeft')show(idx-1);
  else if(e.key==='+'||e.key==='=')zoomAt(1.4,stage.clientWidth/2,stage.clientHeight/2);else if(e.key==='-')zoomAt(1/1.4,stage.clientWidth/2,stage.clientHeight/2);else if(e.key==='0')reset()});
 window.addEventListener('resize',function(){if(lb.classList.contains('on'))reset()});
})();
"""

LIGHTBOX = ('<div id="lb" role="dialog" aria-modal="true" aria-label="Image viewer"><div class="bar"><span></span>'
            '<button data-a="out" title="Zoom out">−</button><button data-a="in" title="Zoom in">+</button>'
            '<button data-a="fit" title="Fit (0)">⤢</button><button data-a="prev" title="Previous">‹</button>'
            '<button data-a="next" title="Next">›</button><button data-a="close" title="Close (Esc)">✕</button></div>'
            '<div class="stage"><img alt=""></div></div>')


class Ctx:
    def __init__(self, D):
        self.bi = D["bilingual"]
        self._n = 0

    def L(self, en: str, ar: str | None = None) -> str:
        """Label: English, plus Arabic when the profile is bilingual."""
        ar = ar or AR.get(en)
        if self.bi and ar:
            return f'{esc(en)}<span class="ar" lang="ar" dir="rtl">{esc(ar)}</span>'
        return esc(en)

    def uid(self, p="t") -> str:
        self._n += 1
        return f"{p}{self._n}"


def pill(state: str, text: str | None = None) -> str:
    text = text or STATE_LABEL[state]
    return f'<span class="pill p-{state}">{esc(text)}</span>'


def st_pill(state: str) -> str:
    return f'<span class="pill {state}">{state}</span>'


def tabs(cx: Ctx, panels: list[tuple[str, str]]) -> str:
    """panels: [(tab label, inner html)] -> tab group (no tab bar when only one)."""
    if len(panels) == 1:
        return panels[0][1]
    gid = cx.uid("g")
    bar = "".join(f'<button role="tab" data-tab="{gid}-{i}" aria-selected="{"true" if i == 0 else "false"}">{esc(lbl)}</button>'
                  for i, (lbl, _) in enumerate(panels))
    body = "".join(f'<div class="tabpanel" id="{gid}-{i}" role="tabpanel"{"" if i == 0 else " hidden"}>{h}</div>'
                   for i, (_, h) in enumerate(panels))
    return f'<div data-tabs><div class="tablist" role="tablist">{bar}</div>{body}</div>'


def fmt_m2(v):
    return None if v is None else f"{v:,.0f}" if v >= 1000 else f"{v:,.1f}"


def sec_pipeline(cx, D):
    li = []
    for i, s in enumerate(D["pipeline"], 1):
        ar = f'<span class="ar" lang="ar" dir="rtl">{esc(s["ar"])}</span>' if cx.bi else ""
        li.append(f'<li class="step s-{s["state"]}"><span class="n">{i:02d}</span>'
                  f'<span class="nm">{esc(s["en"])}{ar}</span>{pill(s["state"])}'
                  f'<div class="d">{esc(s["detail"])}</div></li>')
    return f'<section id="pipeline"><h2>{cx.L("Pipeline")}</h2><ol class="pipe card">{"".join(li)}</ol></section>'


def sec_numbers(cx, D):
    sh = D["sheet"]
    cards = []

    def stat(val, unit, en, ar=None):
        if val is None or val == "":
            return
        u = f"<small>{esc(unit)}</small>" if unit else ""
        cards.append(f'<div class="card stat"><b>{esc(val)}{u}</b><span>{cx.L(en, ar)}</span></div>')

    stat(fmt_m2(sh["plot_m2"]), "m²", "Plot area")
    stat(fmt_m2(sh["foot_m2"]), "m²", "Footprint")
    stat(f"{sh['cov']:.1f}" if sh["cov"] is not None else None, "%", "Coverage")
    stat(len(D["levels"]) or None, "", "Levels")
    stat(D["rooms_total"] or None, "", "Rooms")
    m = D["mall"] or {}
    if m:
        stat(f"{m['gla_m2']:,}" if m.get("gla_m2") else None, "m²", "Gross lettable area", "المساحة التأجيرية")
        sh_pl = m.get("shops_per_level")
        stat(" + ".join(str(x) for x in sh_pl) if sh_pl else None, "", "Shops per level", "المحلات لكل دور")
        trav = (m.get("travel") or {}).get("computed") or []
        if trav:
            stat(f"{max(c['max_m'] for c in trav):g}", "m", "Max travel to exit", "أقصى مسافة للخروج")
    if not cards:
        return ""
    return f'<section id="numbers"><h2>{cx.L("Key numbers")}</h2><div class="stats">{"".join(cards)}</div></section>'


def img_button(im, cap, cls=""):
    return (f'<button type="button" class="{cls}" data-zoom="{im["rel"]}" data-cap="{esc(cap)}" aria-label="Zoom: {esc(cap)}">'
            f'<img src="{im["rel"]}" alt="{esc(cap)}" loading="lazy"></button>')


def sec_gallery(cx, D):
    imgs = D["images"]
    if not imgs:
        return ""
    lvl_label = {l["stem"]: l["label"] for l in D["levels"]}
    out = []
    renders = [i for i in imgs if i["kind"] == "render"]
    if renders:
        r0 = renders[0]
        cap0 = f'Render · {r0["name"]}'
        hero = (f'<button type="button" class="hero" data-zoom="{r0["rel"]}" data-cap="{esc(cap0)}" aria-label="Zoom render">'
                f'<img src="{r0["rel"]}" alt="Render of {esc(D["title"])}"><span class="cap">{esc(D["title"])} · {esc(cap0)}</span></button>')
        th = "".join(img_button(i, f'Render · {i["name"]}') for i in renders[1:])
        out.append(f'<h3 class="lbl">{cx.L("Renders")}</h3>{hero}' + (f'<div class="thumbs">{th}</div>' if th else ""))
    drawn = [i for i in imgs if i["kind"] != "render"]
    if drawn:
        groups: dict[str, list] = {}
        for i in drawn:
            groups.setdefault(i["level"] or "", []).append(i)
        kind_name = {"plan": "Plan", "sheet": "Sheet", "mep": "MEP overlay"}
        kind_ord = {"plan": 0, "sheet": 1, "mep": 2}
        panels = []
        keys = [k for k in [l["stem"] for l in D["levels"]] if k in groups] + [k for k in groups if k not in lvl_label]
        for k in keys:
            figs = []
            for i in sorted(groups[k], key=lambda x: kind_ord.get(x["kind"], 9)):
                cap = f'{lvl_label.get(k, "Project")} · {kind_name[i["kind"]]}'
                pdf = ""
                figs.append(f'<figure class="card sheet" style="margin:0">{img_button(i, cap)}'
                            f'<figcaption><b>{esc(kind_name[i["kind"]])}</b><span>{esc(i["name"])}</span></figcaption></figure>')
            panels.append((lvl_label.get(k) or "Project", f'<div class="sheets">{"".join(figs)}</div>'))
        out.append(f'<h3 class="lbl" style="margin-top:30px">{cx.L("Drawings")}</h3>{tabs(cx, panels)}')
    return f'<section id="gallery"><h2>{cx.L("Gallery")}</h2>{"".join(out)}</section>'


def code_table(rows, imperial=False):
    body = []
    for r in rows:
        body.append(f'<tr><td>{esc(r["name"])}</td><td class="num">{esc(r["actual"])}</td>'
                    f'<td class="num">{esc(r["op"])} {esc(r["limit"])}</td><td>{st_pill(r["state"])}</td></tr>')
    return ('<div class="tw"><table><thead><tr><th>Check</th><th class="num">Design</th><th class="num">Limit</th>'
            f'<th>Result</th></tr></thead><tbody>{"".join(body)}</tbody></table></div>')


def sec_code(cx, D):
    rows, mrows = D["code_rows"], D["mall_rows"]
    if not rows and not mrows and not D["notes"]:
        return ""
    parts = []
    if rows:
        src = D["code_source"] or "source not given"
        flag = ' <span class="warnmark" title="Assumed or to be verified with the authority">⚠ verify</span>' if FLAG_RE.search(src) else ""
        n_pass = sum(1 for r in rows if r["state"] == "PASS")
        n_fail = len(rows) - n_pass
        chips = (f'<div class="chips"><span class="chip PASS">{n_pass} PASS</span>'
                 + (f'<span class="chip FAIL">{n_fail} FAIL</span>' if n_fail else "") + "</div>")
        parts.append(f'{chips}<div class="card">{code_table(rows)}'
                     f'<div class="pad" style="border-top:1px solid var(--line);font-size:12.5px;color:var(--ink2)">'
                     f'Source: <span dir="auto">{esc(src)}</span>{flag}</div></div>')
    if mrows:
        body = "".join(
            f'<div class="prow"><b>{esc(r["name"])}</b><span class="v">{esc(r["value"])}</span>{st_pill(r["state"])}'
            f'<span class="src">{esc(r["source"])}{" <span class=warnmark>⚠ verify</span>" if r["warn"] else ""}</span></div>'
            for r in mrows)
        parts.append(f'<h3>Design parameters</h3><div class="card plist">{body}</div>')
    if D["notes"]:
        li = "".join(f'<li dir="auto">{esc(n)}</li>' for n in D["notes"])
        parts.append(f'<h3 class="lbl">{cx.L("Notes & assumptions")}</h3><div class="card pad"><ul class="notes">{li}</ul></div>')
    return f'<section id="code"><h2>{cx.L("Code check")}</h2>{"".join(parts)}</section>'


def sec_audit(cx, D):
    if not D["has_audit"]:
        return ""
    panels = []
    for l in D["levels"]:
        a = l["audit"]
        if not a:
            continue
        c = a["count"]
        chips = "".join(f'<span class="chip {k}">{c[k]} {k}</span>' for k in ("PASS", "WARN", "FAIL") if c[k] or k == "PASS")
        items = sorted(a["items"], key=lambda i: {"FAIL": 0, "WARN": 1, "PASS": 2}[i["state"]])
        body = "".join(f'<tr><td>{st_pill(i["state"])}</td><td><b>{esc(i["check"])}</b></td><td dir="auto">{esc(i["msg"])}</td></tr>'
                       for i in items)
        panels.append((l["tab"], f'<div class="chips">{chips}</div><div class="card tw"><table><thead><tr><th>Result</th>'
                                 f'<th>Check</th><th>Finding</th></tr></thead><tbody>{body}</tbody></table></div>'))
    return f'<section id="audit"><h2>{cx.L("Design audit")}</h2>{tabs(cx, panels)}</section>'


def sec_verification(cx, D):
    cards = []
    for l in D["levels"]:
        for kind, r in l["reports"].items():
            if not r:
                continue
            keys = ["AUDIT_ERRORS", "ON_LAYER_0", "ENTITIES", "LAYERS", "DIMENSIONS", "TEXTS", "HATCHES", "LAYOUT", "ACADVER"]
            dl = "".join(f'<div><dt>{esc(KEYNAME.get(k, k.replace("_", " ").title()))}</dt><dd>{esc(r[k])}</dd></div>' for k in keys if k in r)
            ok = r.get("AUDIT_ERRORS") == "0"
            bad = r.get("AUDIT_ERRORS", "0") != "0"
            cards.append(f'<div class="card pad"><div style="display:flex;justify-content:space-between;gap:10px;margin-bottom:12px;flex-wrap:wrap">'
                         f'<b>AutoCAD · {esc(l["stem"])} {esc(kind)}</b>{pill("ok" if ok else "fail" if bad else "none", "AUDIT 0 errors" if ok else "AUDIT errors" if bad else "n/a")}</div>'
                         f'<dl class="kv">{dl}</dl></div>')
    ii = D["ifc_info"]
    if ii["counts"] or ii["issues"] is not None:
        dl = "".join(f'<div><dt>{esc(k.replace("Ifc", ""))}</dt><dd>{esc(v)}</dd></div>' for k, v in ii["counts"].items())
        if ii["issues"] is not None:
            dl += f'<div><dt>Validation issues</dt><dd>{ii["issues"]}</dd></div>'
        cards.append(f'<div class="card pad"><div style="display:flex;justify-content:space-between;gap:10px;margin-bottom:12px;flex-wrap:wrap">'
                     f'<b>IFC model</b>{pill("ok" if ii["issues"] == 0 else "warn", "valid" if ii["issues"] == 0 else "check")}</div><dl class="kv">{dl}</dl></div>')
    if not cards:
        return ""
    return f'<section id="verify"><h2>{cx.L("Verification")}</h2><div class="two">{"".join(cards)}</div></section>'


def sec_rooms(cx, D):
    panels = []
    arabic = cx.bi or any(r.get("name_ar") for l in D["levels"] for r in l["rooms"])
    for l in D["levels"]:
        rooms = l["rooms"]
        if not rooms:
            continue
        tid = cx.uid("rt")
        rows = "".join(f'<tr><td dir="auto">{esc(r.get("name", ""))}</td>'
                       + (f'<td dir="auto" lang="ar">{esc(r.get("name_ar", ""))}</td>' if arabic else "")
                       + f'<td class="num">{r["area"]:,.1f}</td></tr>' if isinstance(r.get("area"), (int, float)) else
                       f'<tr><td dir="auto">{esc(r.get("name", ""))}</td>' + ('<td></td>' if arabic else "") + '<td class="num">–</td></tr>'
                       for r in rooms)
        total = sum(r["area"] for r in rooms if isinstance(r.get("area"), (int, float)))
        head = f'<th>Room</th>{"<th>Arabic name</th>" if arabic else ""}<th class="num">Area m²</th>'
        flt = f'<input class="filter" data-filter="{tid}" placeholder="Filter {len(rooms)} rooms…" aria-label="Filter rooms">' if len(rooms) > 12 else ""
        foot = f'<tfoot><tr><td>Total · {len(rooms)} rooms</td>{"<td></td>" if arabic else ""}<td class="num">{total:,.1f}</td></tr></tfoot>'
        panels.append((l["tab"], f'{flt}<div class="card tw"><table id="{tid}"><thead><tr>{head}</tr></thead><tbody>{rows}</tbody>{foot}</table></div>'))
    if not panels:
        return ""
    return f'<section id="rooms"><h2>{cx.L("Room schedule")}</h2>{tabs(cx, panels)}</section>'


def sec_qa(cx, D):
    if not D["qa_md"]:
        return ""
    return (f'<section id="qa"><h2>{cx.L("QA review")}</h2><div class="card pad md">{md_to_html(D["qa_md"])}</div></section>')


def sec_downloads(cx, D):
    if not D["downloads"]:
        return ""
    lvl_label = {l["stem"]: l["stem"] for l in D["levels"]}
    rows = []
    for d in D["downloads"]:
        note = f'<div style="font-size:12px;color:var(--ink2)">{esc(d["note"])}</div>' if d["note"] else ""
        rows.append(f'<tr><td><span class="ext">{esc(d["ext"])}</span><a href="{d["rel"]}" download>{esc(d["name"])}</a>{note}</td>'
                    f'<td>{esc(lvl_label.get(d["level"], "Project"))}{" · MEP" if d["mep"] else ""}</td><td class="num">{human(d["size"])}</td></tr>')
    tot = human(sum(d["size"] for d in D["downloads"]))
    return (f'<section id="downloads"><h2>{cx.L("Downloads")}</h2><div class="card tw"><table class="dl"><thead><tr><th>File</th><th>Level</th>'
            f'<th class="num">Size</th></tr></thead><tbody>{"".join(rows)}</tbody>'
            f'<tfoot><tr><td>{len(D["downloads"])} files</td><td></td><td class="num">{tot}</td></tr></tfoot></table></div></section>')


def render_page(D) -> str:
    cx = Ctx(D)
    lv = ", ".join(l["stem"] for l in D["levels"])
    meta = []
    if D["cc"]:
        meta.append(f'<li><span class="flag" aria-hidden="true">{D["flag"]}</span><span>{esc(D["country"])}</span></li>')
    meta.append(f'<li>{esc(D["type"])}' + (f'<span class="ar" lang="ar" dir="rtl">{esc(D["type_ar"])}</span>' if cx.bi and D["type_ar"] else "") + "</li>")
    if D["date"]:
        meta.append(f'<li>{esc(D["date"])}</li>')
    if D["client"]:
        meta.append(f'<li>Client: {esc(D["client"])}</li>')
    if D["plot_no"]:
        meta.append(f'<li dir="auto">{esc(D["plot_no"])}</li>')
    if len(D["levels"]) > 1 or (lv and LEVEL_LIKE.match(lv)):
        meta.append(f'<li>Levels: {esc(lv)}</li>')
    h1ar = f'<p class="h1ar" lang="ar" dir="rtl">{esc(D["title_ar"])}</p>' if D["title_ar"] else ""
    secs = [sec_pipeline(cx, D), sec_numbers(cx, D), sec_gallery(cx, D), sec_code(cx, D), sec_audit(cx, D),
            sec_verification(cx, D), sec_rooms(cx, D), sec_qa(cx, D), sec_downloads(cx, D)]
    navmap = [("pipeline", "Pipeline"), ("numbers", "Key numbers"), ("gallery", "Gallery"), ("code", "Code check"),
              ("audit", "Design audit"), ("verify", "Verification"), ("rooms", "Room schedule"), ("qa", "QA review"),
              ("downloads", "Downloads")]
    body = "".join(secs)
    nav = "".join(f'<a href="#{i}">{esc(n)}</a>' for i, n in navmap if f'id="{i}"' in body)
    today = _dt.date.today().isoformat()
    dirattr = ' dir="auto"'
    rtl = ' lang="en"'
    return (f'<!doctype html><html{rtl}><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<meta name="color-scheme" content="light dark"><title>{esc(D["title"])} — project dashboard</title>'
            f'<style>{CSS}</style></head><body>'
            f'<header class="top"><div class="wrap"><div class="eyebrow">{cx.L("Project dashboard")}</div>'
            f'<h1{dirattr}>{esc(D["title"])}</h1>{h1ar}<ul class="meta">{"".join(meta)}</ul></div>'
            f'<nav class="sec" aria-label="Sections"><div class="wrap">{nav}</div></nav></header>'
            f'<main class="wrap">{body}</main>'
            f'<footer class="wrap">Generated {today} by ArchMind <code>dashboard.py</code> from the project folder. '
            f'Sample / indicative output; verify against the authority before submission.</footer>'
            f'{LIGHTBOX}<script>{JS}</script></body></html>')


def build(folder: Path, out: Path | None = None) -> tuple[Path, dict]:
    folder = Path(folder)
    out = Path(out) if out else folder / "dashboard.html"
    D = collect(folder, out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render_page(D), encoding="utf-8")
    return out, D


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("folder", help="project folder (spec JSON, DXF, PDF, IFC, renders ...)")
    ap.add_argument("-o", "--out", help="output HTML (default <folder>/dashboard.html)")
    a = ap.parse_args()
    out, D = build(Path(a.folder), Path(a.out) if a.out else None)
    states = " ".join(f"{s['en']}={s['state']}" for s in D["pipeline"])
    print(f"wrote {out}  [{states}]")


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, OSError):
        pass
    main()
