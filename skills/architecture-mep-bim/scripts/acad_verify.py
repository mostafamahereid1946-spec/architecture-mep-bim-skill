"""Verify a DXF/DWG in real AutoCAD (headless Core Console): AUDIT, count, save DWG, plot PDF.

Usage:
    uv run scripts/acad_verify.py drawing.dxf [--layout A1-GF] [--paper "ISO full bleed A1 (841.00 x 594.00 MM)"]
          [--acad "C:/Program Files/Autodesk/AutoCAD 2026/accoreconsole.exe"]

Writes next to the input: <name>.dwg, <name>.pdf, <name>-report.txt (KEY=value lines,
including AUDIT_ERRORS and ON_LAYER_0, which ignores the paper-space viewport).
Needs a licensed AutoCAD install (full or toolset). AutoCAD LT has no Core Console.

Paper names for "DWG To PDF.pc3" (match the profile's sheet):
  "ISO full bleed A0 (841.00 x 1189.00 MM)"   "ISO full bleed A1 (841.00 x 594.00 MM)"
  "ISO full bleed A3 (420.00 x 297.00 MM)"    "ARCH full bleed D (36.00 x 24.00 Inches)" --paper-units I
"""
import argparse
import glob
import re
import subprocess
from pathlib import Path


def find_acad():
    hits = sorted(glob.glob(r"C:\Program Files\Autodesk\AutoCAD 20*\accoreconsole.exe"))
    if not hits:
        raise SystemExit("accoreconsole.exe not found; pass --acad")
    return hits[-1]


def lisp_path(p):
    return str(p).replace("\\", "/")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("drawing")
    ap.add_argument("--layout", default=None, help="layout to plot (default: first paper layout)")
    ap.add_argument("--paper", default="ISO full bleed A1 (841.00 x 594.00 MM)")
    ap.add_argument("--paper-units", default="M", choices=["M", "I"], help="M=mm, I=inches")
    ap.add_argument("--ctb", default="monochrome.ctb")
    ap.add_argument("--acad", default=None)
    a = ap.parse_args()
    src = Path(a.drawing).resolve()
    dwg, pdf = src.with_suffix(".dwg"), src.with_suffix(".pdf")
    report = src.with_name(src.stem + "-report.txt")
    for old in (dwg, pdf, report):   # SAVEAS/PLOT stall on overwrite prompts
        old.unlink(missing_ok=True)
    layout_expr = f'"{a.layout}"' if a.layout else "(car (layoutlist))"
    scr = src.with_suffix(".scr")
    scr.write_text("\n".join([
        '(setvar "FILEDIA" 0)', '(setvar "CMDECHO" 0)', '(setvar "BACKGROUNDPLOT" 0)',
        '(command "_.AUDIT" "_Y")',
        f'(setq rf (open "{lisp_path(report)}" "w"))',
        '(defun n (f) (if (setq s (ssget "_X" f)) (sslength s) 0))',
        '(write-line (strcat "ACADVER=" (getvar "ACADVER")) rf)',
        '(write-line (strcat "INSUNITS=" (itoa (getvar "INSUNITS"))) rf)',
        "(write-line (strcat \"ENTITIES=\" (itoa (n nil))) rf)",
        "(write-line (strcat \"ON_LAYER_0=\" (itoa (n '((8 . \"0\") (-4 . \"<NOT\") (0 . \"VIEWPORT\") (-4 . \"NOT>\"))))) rf)",
        "(write-line (strcat \"DIMENSIONS=\" (itoa (n '((0 . \"DIMENSION\"))))) rf)",
        "(write-line (strcat \"HATCHES=\" (itoa (n '((0 . \"HATCH\"))))) rf)",
        "(write-line (strcat \"TEXTS=\" (itoa (n '((0 . \"TEXT,MTEXT\"))))) rf)",
        '(setq lays nil) (setq l (tblnext "LAYER" T)) (while l (setq lays (cons (cdr (assoc 2 l)) lays)) (setq l (tblnext "LAYER")))',
        '(write-line (strcat "LAYERS=" (itoa (length lays))) rf)',
        f'(setq lo {layout_expr})',
        '(write-line (strcat "LAYOUT=" lo) rf)',
        '(close rf)',
        f'(command "_.SAVEAS" "2018" "{lisp_path(dwg)}")',
        '(command "_.LAYOUT" "_S" lo)',
        f'(command "_.-PLOT" "_Y" lo "DWG To PDF.pc3" "{a.paper}" "_{a.paper_units}" "_L" "_N" "_L" "1:1" "0,0"'
        f' "_Y" "{a.ctb}" "_Y" "_N" "_N" "_N" "{lisp_path(pdf)}" "_N" "_Y")',
        '(princ "\\nBUILDING_SKILL_VERIFY_DONE\\n")',
        "_.QUIT", "_Y", "",
    ]), encoding="utf-8")
    exe = a.acad or find_acad()
    res = subprocess.run([exe, "/i", str(src), "/s", str(scr), "/l", "en-US"],
                         capture_output=True, timeout=600, cwd=src.parent)
    log = res.stdout.decode("utf-16-le", errors="ignore").replace("\x00", "")
    ok = "BUILDING_SKILL_VERIFY_DONE" in log
    audit = re.search(r"Total errors found\s+(\d+)\s+fixed\s+(\d+)", log)
    if report.exists():
        with report.open("a") as f:
            f.write(f"AUDIT_ERRORS={audit.group(1) if audit else 'unknown'}\n")
    if not audit or audit.group(1) != "0" or not ok:
        src.with_name(src.stem + "-acad.log").write_text(log, encoding="utf-8")
    for junk in (scr, src.parent / "plot.log"):   # Core Console leaves these behind
        junk.unlink(missing_ok=True)
    print(report.read_text() if report.exists() else "NO REPORT")
    print(f"DWG={'yes' if dwg.exists() else 'no'}  PDF={'yes' if pdf.exists() else 'no'}  SCRIPT_DONE={ok}")
    if not ok:
        print(log[-2500:])


if __name__ == "__main__":
    main()
