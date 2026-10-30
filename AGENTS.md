# AGENTS.md — architecture-mep-bim (Codex, Cursor, any agent)

This repo is a skill for architecture, construction, BIM and MEP work: country-correct AutoCAD/DXF drawings, IFC for Revit/ArchiCAD, MEP layouts, renders and building-code checks.

Before any building, drawing, BIM, MEP or render task, read `skills/architecture-mep-bim/SKILL.md` and follow it: pin the jurisdiction, load only the references it points to, quote code numbers only from `references/countries/<iso2>.md`, and verify outputs before saying done.

For a whole project, work through these roles in order (each file in `agents/` is the role's brief):
1. `agents/aec-brief-planner.md` — brief, concept, plan spec JSON
2. `agents/aec-code-checker.md` — code + design audit; loop back to 1 until 0 FAIL
3. `agents/aec-drafter.md` — DXF/DWG sheets, AutoCAD verification
4. `agents/aec-mep-engineer.md` — HVAC, plumbing, electrical, fire
5. `agents/aec-bim-modeler.md` — IFC4 model
6. `agents/aec-visualizer.md` — renders
7. `agents/aec-qa-reviewer.md` — independent review, client dashboard

Scripts run with `uv` (it fetches Python and packages): see the command list in SKILL.md section 4.
