# Gemara Visual integration contract

This is the project-specific route for the `torah-video-editor` skill. The repository's `AGENTS.md`, `.cursor/rules/gemara-visual.mdc`, `docs/CREATIVE_BIBLE.md`, `docs/DESIGN_DECISIONS.md`, `docs/MANUAL_DEL_AGENTE.md`, `docs/ARCHITECTURE.md`, `docs/METODO_DE_ENSENANZA.md`, `docs/COMO_APRENDE_UNA_PERSONA.md`, `docs/QUE_DECIR.md`, `docs/VIDEOS.md`, and `docs/REFERENCIAS_VISUALES.md` outrank this file if there is any conflict.

## Read in order

1. Project entry instructions and permanent rules.
2. Manual, architecture, teaching method, learner/teacher reading guides, and improvements.
3. Creative Bible, design decisions, visual references, and the video guide.
4. Only then inspect the target daf's prepared explanation, storyboard, assets, and generated registry.

## Canonical design mapping

| Skill idea | Gemara Visual contract |
|---|---|
| Visual identity | `src/design/tokens.ts`, `docs/CREATIVE_BIBLE.md`; do not use this skill's standalone palette |
| Text/source | Sefaria-backed text, Hebrew/Aramaic source plus Spanish gloss; no invented quotation |
| Scene data | `StudyUnit` / `VisualSpec` / validated storyboard JSON; LLM writes data, not executable HTML |
| World continuity | Same actor id mutates across moments; `sampleAt(t)` is deterministic |
| Physics | Shared geometry/light calculations also draw the scene; never hand-draw a ray or shadow |
| Scale | Canonical person is 170 cm; measurements include an educational approximation disclaimer when needed |
| Motion | Sereno, purposeful, no bounce; use project timing/easing and `holdFor`, not hard-coded scene durations |
| Visual checks | TypeScript, Vitest, ESLint, scenes review, photos/contact sheet, panel/reader review as applicable |
| Video | Same app timeline and frame sampling; export must not become a second interpretation |

**No inventado:** si una fuente, sabio, medida, traducción o conclusión no está verificada en el material del proyecto, queda pendiente de revisión y no entra en una escena final.

## What the first visual must answer

Before designing any moment, write the obstacle in one sentence. The scene should show: situation → one meaningful change → result. If the image does not teach without the text below it, it is not ready. A life example is marked `ejemplo` and cannot add halakha. A logic moment is marked `logica` and cannot be presented as a source.

## Required review path

For a new daf, use the repository's canonical flow rather than a generic video editor:

```text
study/explanation → analyst review → learner/teacher read → data storyboard
→ strict scene review → photos/contact sheet → photo reviewer/panel
→ voice plan if requested → app preview → MP4/HyperFrames export
```

Useful commands are the ones defined by the project: `npm run hoja -- "<hoja>"`, `npm run escenas:revisar -- "<hoja>"`, `npm run fotos -- "<hoja>"`, `npm run fotos:revisar -- "<hoja>"`, `npm run panel -- "<hoja>"`, and `npm run video -- "<hoja>"`. Inspect outputs; do not edit generated registry files by hand.

## Style decisions that must survive export

- Warm editorial illustration with real depth and materials; no childish flat boxes.
- Hebrew source remains readable and RTL; Spanish glosa explains first-use terms.
- Paper boards sit over the world and retain the place/time behind them; no empty white dashboard cards.
- A machloket uses equal visual weight and no red/green correctness coding.
- The sun, rays, shadows, people, buildings, and measures remain physically consistent.
- A source line is compact and never covers the world it explains.
