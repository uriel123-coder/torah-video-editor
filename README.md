# Torah Video Editor

An installable Codex/Claude Code skill for planning and exporting Torah, Talmud, Gemara, Halakha, and Jewish education videos as clear, source-faithful visual lessons. It includes a specific integration contract for Gemara Visual and a guarded HyperFrames export adapter.

## What it does

- Plans scenes from the source study and teaching obstacle instead of cutting by silence or decorating a talking head.
- Maps to Gemara Visual's VisualSpec, physical world, deterministic timeline, canonical design tokens, source rules, and photo/panel review.
- Includes standalone design manuals only as a fallback when a project has no visual bible.
- Defines a guarded HyperFrames adapter that exports approved scene data without reinterpreting the sugya.
- Treats Hebrew/Aramaic text, quotations, measurements, and halakhic claims as review-sensitive.
- Generates and validates an edit manifest that can drive a renderer or a human editor.

This system supports editing and explanation. It is not a posek, does not issue rulings, and does not verify a source merely because a citation looks plausible.

## Install

### Codex

Copy or symlink this folder into `~/.codex/skills/torah-video-editor/`, or install the ZIP through your normal skill workflow. The required entrypoint is `SKILL.md`.

### Claude Code

Copy the folder into the project's skills directory supported by your Claude Code setup. Keep `SKILL.md`, `references/`, and `scripts/` together. The same Markdown instructions are intentionally tool-agnostic.

## Quick start

```bash
python scripts/semantic_manifest.py init --out edit-manifest.json --title " שיעור על סוכה "
python scripts/semantic_manifest.py validate edit-manifest.json
python scripts/semantic_manifest.py report edit-manifest.json --out qa-report.md
```

Then add transcript beats, source records, assets, and scenes. Use `examples/` as the smallest complete examples.

For Gemara Visual, do not use the standalone manifest as the production schema. Read `references/gemara-visual-integration.md`, work inside the repository's existing commands and contracts, and use `references/hyperframes-export.md` only for an explicit export migration.

## Repository map

| Path | Purpose |
|---|---|
| `SKILL.md` | Installable agent instructions |
| `references/` | Design, editorial, pipeline, Hebrew, examples, QA |
| `scripts/semantic_manifest.py` | Deterministic manifest initializer, validator, and report generator |
| `examples/` | Sucah and Gemara-debate manifests |
| `tests/` | Invariant tests for the manifest tool and examples |

## License

MIT. See `LICENSE`.
