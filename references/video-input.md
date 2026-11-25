# Video input and timestamped transcription

When a user provides a class recording, do not choose visuals from the filename or title alone.

## Preferred route

1. Read metadata: duration, dimensions, frame rate, and audio presence.
2. For videos longer than 30 seconds, run the available video analysis tool with transcription, scene changes, silence, motion, and exposure as appropriate before extracting frames.
3. Extract a low-rate overview and drill into moments named by the transcript (`mira`, `como se ve`, a source quotation, a measurement, or a transition).
4. If the video analysis server is unavailable, run:

```bash
python scripts/transcribe_video.py input.mp4 --out .tmp/transcript --language Spanish
```

The helper requires local Whisper and produces timestamped `.json`, `.srt`, `.tsv`, `.vtt`, and `.txt` outputs. Install the fallback dependency only when needed:

```bash
python3 -m pip install --user openai-whisper
```

5. Inspect the transcript for proper names, Hebrew/Aramaic terms, source quotations, and uncertainty. Whisper's output is evidence for planning, not a verified source. Mark low-confidence or misrecognized terms and compare against the supplied text.

## The speech-to-scene contract

Every inserted visual needs a time range and a reason grounded in the spoken content. A visual plan must be auditable:

| Video time | Spoken claim | Visual | Status |
|---|---|---|---|
| 00:00–00:30 | exact or paraphrased transcript span | scene/asset id | verified / review |

If the speech cannot be understood, stop semantic editing and return a transcript-review task. Do not fill the gap with generic stock imagery. Keep the presenter or original footage only when it is the least misleading option.

For a recorded-class edit, also preserve the original video/audio and set the output duration to the source duration. The transcript is not a license to summarize later: visuals appear at the same timestamps as the claims they explain.

## Gemara Visual example

For a class explaining Berakhot 2a, the transcript may support: `night / stars`, `kohanim and terumah`, `mikveh and waiting until night`, and `Rabbi Eliezer / Sages / Rabban Gamliel`. It does not by itself verify the Hebrew quotation or a halakhic conclusion; those still require the project's source and teacher review.
