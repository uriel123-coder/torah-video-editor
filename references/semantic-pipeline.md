# Semantic editing pipeline

## Stages

```text
media → transcript → normalized beats → source ledger → visual plan → asset ledger
      → timeline manifest → captions/render → frame/audio/RTL QA → deliverables
```

## Manifest contract

The repository examples define the machine-readable shape. Required top-level fields are `schema_version`, `project`, `sources`, `beats`, `assets`, `scenes`, and `qa`.

Each scene has `id`, `in`, `out`, `beat_ids`, `layout`, `purpose`, `text_direction`, `visuals`, and `review`. Time is seconds from media start. Scene intervals must be positive and non-overlapping unless a transition is explicitly represented.

## Transcription and planning

Keep raw transcript text separate from normalized text. Mark uncertain words with `confidence < 0.8` or an explicit note. Derive beats from meaning changes: a new source, example, position, measurement, or conclusion should be independently addressable.

## Rendering integration

The manifest is renderer-neutral. A Remotion, FFmpeg, Premiere, Resolve, or ChatCut adapter may consume it. Adapters must preserve scene IDs, source labels, caption timing, RTL metadata, and the QA report. The skill does not assume that a missing renderer means the edit is impossible: it can still deliver a reviewable manifest and asset brief.
