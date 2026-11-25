# Recorded-class mode

This mode is for a real teacher's uploaded class. It is not a replacement lecture and not a slideshow with a voice pasted underneath.

## Contract

```json
{
  "mode": "recorded_class",
  "source_media": "class.mp4",
  "source_duration": 319.135,
  "output_duration": 319.135,
  "audio": {"mode": "original", "preserve": true, "source": "class.mp4"},
  "transcript": {"path": "transcript.json", "language": "es", "timestamps": true},
  "segments": [
    {
      "id": "seg-01",
      "source_time": {"in": 0, "out": 20},
      "spoken_claim": "La clase presenta el Shemá de la noche",
      "visual_mode": "source-plus-graphic",
      "graphic_intent": "Mostrar la pregunta y la noche",
      "visual_ids": ["night-timeline"],
      "review": "needs_review"
    }
  ]
}
```

`source_duration` and `output_duration` are required and must match within 0.05 seconds. `audio.preserve` must be true unless the user explicitly requested a different audio edit. The original video stays in the composition even when a diagram/cutaway is on screen.

## Visual decision table

| What the teacher says | What may appear at that same time |
|---|---|
| Defines a question | The question, source anchor, or a simple physical situation |
| Names an object/person | Introduce that object/person before using it in a rule |
| Explains a change | Animate the same object id from before to after |
| Gives a measurement | Scale, person, endpoints, unit, and stated convention |
| Compares opinions | All named opinions together, equal weight, no winner coding |
| Quotes a source | Exact verified text with locator; otherwise use a labeled paraphrase |
| Gives an example | Mark `EJEMPLO`, keep it separate from the source, and use the same relationship |
| Summarizes | Show the already-established states; do not introduce a new picture |

## Berakhot 2a acceptance example

If the transcript says the three limits are Rabí Eliezer (first third), the Sabios (midnight), and Rabán Gamliel (dawn), the synchronized graphic must show one night timeline with all three limits and names while that explanation is spoken. It must not show only one photo, must not reorder the positions, and must not extend the video with a new conclusion card.

## Review questions

- Can a reviewer point from every graphic to the exact transcript span that caused it to appear?
- Is the teacher's original voice still intelligible and present?
- Does the graphic change when the spoken idea changes, rather than on arbitrary fixed intervals?
- Are all named cases/opinions visible together when the teacher compares them?
- Does the final frame end at the source video's end, not after it?
