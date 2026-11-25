# Torah, Hebrew, and Aramaic precision

This guide is an editorial safeguard, not a substitute for a qualified rabbi, teacher, translator, or source editor.

## Text handling

- Store original source text in `original_text` and the working translation in `translation`; never overwrite one with the other.
- Preserve niqqud when supplied. Do not add niqqud by guesswork.
- Use Unicode Hebrew text with explicit RTL metadata. Test mixed Hebrew/Latin strings, punctuation, numerals, and parentheses.
- Treat Talmudic Aramaic, Biblical Hebrew, Modern Hebrew, and transliteration as distinct language labels.
- For a displayed quote, capture the exact excerpt and a locator. A paraphrase must be visually labeled `Paráfrasis`.

## Claims and measurements

Record every legal or factual claim that drives a visual. For measurements, store the unit exactly as said, the source or teacher attribution, and a review state. Do not convert amot, tefachim, or other measures without an explicit convention.

## Review protocol

1. Compare transcript against the audio around the claim.
2. Compare displayed source against the supplied edition or trusted source record.
3. Ask a qualified reviewer when the edit could be read as a psak or when the source is disputed.
4. Keep the reviewer's note in the ledger; do not erase uncertainty after a visual decision.
