# Render and QA checklist

## Automated

- Manifest schema and required fields pass.
- All scene intervals are valid and within known duration when supplied.
- Every source visual has a source record or is explicitly marked `editorial_visualization`.
- Every Hebrew/Aramaic scene has `text_direction: rtl` and a language label.
- Captions cover speech segments without overlaps or impossible timestamps.
- No scene is marked final while `review.blocking` is non-empty.

## Human review

- Watch once without pausing for narrative clarity.
- Watch source scenes paused: check exact text, direction, highlight, locator, and translation separation.
- Watch debate scenes: check that layout does not imply a winner.
- Watch diagrams: check object geometry, labels, measures, and the relationship being taught.
- Check PiP face visibility, captions, safe areas, audio intelligibility, and export frame rate.

## Export package

Include master video, captions, manifest, sources ledger, QA report, and a short README describing unresolved review items.
