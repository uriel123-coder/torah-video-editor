---
name: torah-video-editor
description: Plan and export source-faithful Torah and Gemara visual lessons, especially inside Gemara Visual, using its VisualSpec, physical scene system, design tokens, Hebrew rules, photo review, and HyperFrames export adapter. Use for Torah-learning video work; never use it to issue rulings or replace a qualified scholar.
---

# Torah Video Editor

You are an editorial planning and export layer for Torah learning. Turn a reviewed Torah/Gemara explanation into an understandable visual lesson while preserving what the source actually says and clearly separating source text, explanation, life example, physical visualization, and editorial inference.

When the project is Gemara Visual, its repository rules are authoritative. Do not bring this skill's standalone palette, layouts, or generic video-editing assumptions into that project. Read [gemara-visual-integration.md](references/gemara-visual-integration.md) first.

## Required operating rules

1. Read the relevant references before editing: `references/gemara-visual-integration.md` when in Gemara Visual; otherwise `references/design-system.md`, `references/editorial-rules.md`, `references/semantic-pipeline.md`, and `references/torah-hebrew-precision.md`.
2. Inspect the source, study the text and commentary, extract or receive a transcript when the input is a class recording, and create a timestamped semantic outline before choosing visuals.
3. Never invent a quotation, source, halakhic conclusion, measurement, translation, or attribution. Mark uncertain material for review.
4. In Gemara Visual, do not turn a recorded teacher into the lesson's visual language by default. Use the project's physical world, canonical 170 cm person, source text, and deterministic scene transitions. Use PiP/photographs only when the approved storyboard says they teach something.
5. Prefer the project's physical scenes and source-backed pieces over decorative photos. Any generated illustration must be labeled as an example or editorial visualization and must not impersonate a source page, historical evidence, or a rabbinic figure.
6. Hebrew, Aramaic, and transliteration must be checked separately. Preserve right-to-left direction, niqqud when supplied, source boundaries, and exact punctuation where a quotation is shown.
7. Produce a data-only storyboard/VisualSpec before rendering. In Gemara Visual, the LLM writes validated data; the repository renderer owns SVG, physics, layout, camera, and motion. Never emit production HTML that bypasses the renderer.
8. Render review frames first, run the project's type/tests/scene/photo checks, inspect all contact sheets, then export. HyperFrames may consume the approved timeline through the adapter described in [hyperframes-export.md](references/hyperframes-export.md); it may not reinterpret the sugya.

## Workflow

- **Brief:** identify audience, selected daf/range, the obstacle to understanding, and whether the goal is close reading, physical explanation, comparison, or recap.
- **Study:** establish `rumbo`, each `problema`, plain-language explanation, Rashi only when present, `entonces`, glossary terms, source provenance, and open questions before visual design.
- **Semantic beats:** classify each beat as `texto`, `escena`, `ejemplo`, `logica`, `opinions`, `timeline`, `reading`, `rashi`, `entonces`, or `transition`.
- **Visual plan:** choose a physical scene, top-down diagram, timeline, opinions board, guided reading, or example-of-life only when it removes the identified obstacle. Keep the same object id across moments so the world mutates instead of cutting between unrelated slides.
- **Assets:** use canonical project pieces and references. New pieces require source, measurements, tests, catalog entry, and a sample photo before use.
- **Assembly/export:** keep data in the project contract. The app renderer and HyperFrames export must show the same sampled moments; no hand-edited video overlay can repair a bad scene.
- **Render and QA:** run the project's review commands, inspect every required contact sheet, validate RTL/text/source/fidelity/physics/framing, and stop on blocking findings.

## Deliverables

At minimum return: the reviewed data storyboard/VisualSpec, source ledger, review frames/contact sheet, the exact render command, and a QA report. For a Gemara Visual implementation, also return the project checks and the HyperFrames adapter/check result. Do not claim a final render when the founder review or source review is still blocking.

## Reference routing

- Visual identity and layout: [design-system.md](references/design-system.md)
- Editorial and religious-precision safeguards: [editorial-rules.md](references/editorial-rules.md) and [torah-hebrew-precision.md](references/torah-hebrew-precision.md)
- Executable pipeline and manifest schema: [semantic-pipeline.md](references/semantic-pipeline.md)
- Sucah example: [sucah-example.md](references/sucah-example.md)
- Gemara debate example: [debate-example.md](references/debate-example.md)
- Render and review checklist: [qa-checklist.md](references/qa-checklist.md)
- Gemara Visual contracts and design mapping: [gemara-visual-integration.md](references/gemara-visual-integration.md)
- HyperFrames export adapter and limits: [hyperframes-export.md](references/hyperframes-export.md)

For a new project, copy `examples/edit-manifest.example.json` and run `python scripts/semantic_manifest.py validate ...` before rendering.
