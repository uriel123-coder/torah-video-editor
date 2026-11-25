# HyperFrames export adapter

HyperFrames is an export/runtime adapter, not the Gemara interpreter. Use it only after the Gemara Visual timeline and review are approved.

## The boundary

The source of truth remains the project's deterministic scene data and renderer. HyperFrames may render a faithful HTML representation of already-approved frames or a thin wrapper around exported scene images. It must not receive a prompt and invent the sugya, sources, physical relationships, timing, or halakhic meaning.

Do not silently replace the current Gemara Visual renderer with a generic HyperFrames composition. The repository currently documents its own SVG/timeline MP4 path and lists HyperFrames as a future export phase. If the owner requests a migration, treat it as an explicit architecture task with a comparison render and rollback path.

## Safe adapter workflow

1. Export a manifest of the approved moments: scene id, start/duration, sampled frame or approved SVG, source text, RTL metadata, and review state.
2. Build an editable HyperFrames project with `index.html`, `compositions/`, and `assets/`; use local assets and bundled fonts only.
3. Put one composition per approved scene. Every timed element has `class="clip"`, `data-start`, `data-duration`, stable ids, and a paused deterministic timeline.
4. Preserve the project aspect ratio (`1200×675` scene view or the requested output mapping), safe areas, font choices, source labels, and scene order.
5. Do not use `Date.now()`, unseeded randomness, timers, network fetches, CSS filters for media treatment, or media seeking/playback control.
6. Run `npx hyperframes check --json`, snapshot representative scenes, compare them against the Gemara Visual contact sheet, and record any pixel/semantic difference.
7. Render only after the comparison passes and the founder has approved the preview. The final report must say whether the MP4 came from the existing renderer or the HyperFrames adapter.

## HyperFrames-specific visual rules

- Use `Newsreader`/`Noto Serif Hebrew` and `Figtree`/`Noto Sans Hebrew` only when those fonts are bundled or declared via local `@font-face`.
- Keep source text and captions inside title-safe areas. Never reverse Hebrew manually.
- Use HyperFrames transitions to express an already-approved state change; do not create decorative transitions between unrelated screens.
- If footage is present, retain its audio contract and apply treatment through the prescribed media-treatment path, not arbitrary CSS filters.
- The HyperFrames desktop app is for preview/editing; it does not replace the project's learner, teacher, physics, or photo reviews.

## Acceptance criteria

The adapter is acceptable only if: the same moment ids exist in both timelines; four or more sampled frames match the approved project frames; source text and RTL are unchanged; scene duration and order match; `hyperframes check` is clean; and the project QA report has no blocking item.
