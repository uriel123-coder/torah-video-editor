# Design system

## Identity

The visual voice is a quiet study table: warm paper, ink, slate, and one living accent. It should feel contemporary and respectful, never ornamental for its own sake. The source is treated as a primary object; the presenter remains a human guide.

## Palette

| Token | Hex | Use |
|---|---|---|
| `ink` | `#18232B` | text, presenter frame, dark background |
| `slate` | `#405463` | secondary labels and dividers |
| `paper` | `#F4F0E8` | source cards and light canvas |
| `sand` | `#D8C3A5` | measurement lines and neutral emphasis |
| `sage` | `#6F8460` | definitions, accepted framing, structure |
| `terracotta` | `#A96F58` | debate, tension, counter-case |
| `gold` | `#C79A45` | source marker and key phrase |
| `red-review` | `#B34E4E` | unresolved editorial review only; never a conclusion marker |

Use one accent per scene. Contrast must remain readable in both light and dark layouts.

## Typography

- Latin/UI: `Inter` or another neutral sans with tabular numerals.
- Hebrew/Aramaic: `Noto Sans Hebrew` for UI and `Noto Serif Hebrew` for source quotations. Use a tested local substitute if unavailable and record it in the manifest.
- Source title: 30–42 px at 1080p; source body: 42–58 px; presenter lower-third: 28–34 px; captions: 42–52 px.
- Never fake Hebrew by reversing characters. Set `dir="rtl"` or the renderer's RTL equivalent and align by meaning.

## Layouts

1. **Presenter full:** 100% frame. Use for opening, emotional nuance, and synthesis.
2. **Presenter + PiP:** explanatory visual 78–86% frame, presenter 18–24% frame with a 24 px safe margin. PiP may not cover Hebrew text or diagrams.
3. **Split case:** 50/50 for two conditions or named positions. Sage is the neutral case; terracotta is the contrasting case. Do not imply that color alone decides truth.
4. **Source desk:** paper canvas, source label, exact text, synchronized highlight, translation/summary in a separate band.
5. **Diagram board:** one object, one relationship, one annotation at a time. Build in layers rather than presenting a busy poster.

## Motion

- Default entrance: 220–320 ms ease-out; exit: 160–240 ms ease-in.
- Use a 6–10 px settle or paper-shift for editorial cards; no elastic bounce.
- Highlight source phrases by a tinted underline or translucent band, never by altering the quoted letters.
- Measurements draw from endpoint to endpoint, then label; do not animate an incorrect intermediate state.
- Debate transitions use a lateral handoff or a clean divider, not a winner-style slam.

## Storytelling beat

`question → source/problem → model/example → complication → comparison → takeaway`.

The visual must answer “why is this on screen now?” If it only decorates, keep the presenter full-frame.
