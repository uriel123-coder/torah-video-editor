# Torah Video Editor

An installable Codex/Claude Code skill for editing Torah, Talmud, Gemara, Halakha, and Jewish education videos as clear visual lessons.

## What it does

- Plans scenes from a timestamped transcript instead of cutting by silence alone.
- Uses a restrained editorial system: presenter, source close-up, PiP, split-screen, diagrams, and synchronized emphasis.
- Includes original design manuals for identity, palette, typography, layouts, motion, storytelling, and source precision.
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
