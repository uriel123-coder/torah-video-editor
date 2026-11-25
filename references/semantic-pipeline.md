# Semantic editing pipeline

## Gemara Visual mode

When the target repository is Gemara Visual, this generic manifest is only an interchange note. The production contract is its validated `StudyUnit`/`VisualSpec` and storyboard data. The agent must not generate HTML, SVG paths, physics, or a second timing system as a shortcut. The repository renderer owns those concerns.

## Stages

```text
media → transcript → normalized beats → source ledger → visual plan → asset ledger
      → timeline manifest → captions/render → frame/audio/RTL QA → deliverables
```

For Gemara Visual, replace the middle with:

```text
source study → learner/teacher explanation → VisualSpec → storyboard data
→ deterministic world/physics/layout → app frames → photo/panel review → export
```

## Manifest contract

The repository examples define the machine-readable shape. Required top-level fields are `schema_version`, `project`, `sources`, `beats`, `assets`, `scenes`, and `qa`. In `recorded_class` mode, also require source/output duration, preserved original audio, timestamped transcript metadata, and a segment-to-speech mapping.

Each scene has `id`, `in`, `out`, `beat_ids`, `layout`, `purpose`, `text_direction`, `visuals`, and `review`. Time is seconds from media start. Scene intervals must be positive and non-overlapping unless a transition is explicitly represented. In recorded-class mode, a visual scene also carries `source_time` and `spoken_claim`; neutral source-video holds are the only exception.

## Transcription and planning

Keep raw transcript text separate from normalized text. Mark uncertain words with `confidence < 0.8` or an explicit note. Derive beats from meaning changes: a new source, example, position, measurement, or conclusion should be independently addressable.

## Rendering integration

The manifest is renderer-neutral. In standalone work, an adapter may consume it. In Gemara Visual, the canonical renderer is the existing deterministic SVG/timeline system; HyperFrames is allowed only as a faithful export adapter after comparison. Any adapter must preserve scene IDs, source labels, caption timing, RTL metadata, physics-derived geometry, and the QA report. A missing adapter never authorizes inventing a new interpretation of the source.
