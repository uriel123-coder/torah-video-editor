#!/usr/bin/env python3
"""Transcribe a local video with timestamps when Whisper is available."""
import argparse, importlib.util, pathlib, subprocess, sys

def main():
    p=argparse.ArgumentParser(description="Create timestamped transcript files for a video")
    p.add_argument("video")
    p.add_argument("--out", required=True)
    p.add_argument("--model", default="small")
    p.add_argument("--language", default=None)
    args=p.parse_args()
    video=pathlib.Path(args.video)
    if not video.exists():
        print(f"ERROR: video not found: {video}", file=sys.stderr); return 2
    if importlib.util.find_spec("whisper") is None:
        print("ERROR: Whisper is not installed. Install with: python3 -m pip install --user openai-whisper", file=sys.stderr)
        return 3
    out=pathlib.Path(args.out); out.mkdir(parents=True, exist_ok=True)
    cmd=[sys.executable,"-m","whisper",str(video),"--model",args.model,"--task","transcribe","--output_dir",str(out),"--output_format","all","--word_timestamps","True","--fp16","False"]
    if args.language: cmd += ["--language",args.language]
    return subprocess.call(cmd)

if __name__ == "__main__": sys.exit(main())
