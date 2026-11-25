#!/usr/bin/env python3
"""Small, dependency-free manifest tool for Torah Video Editor."""
import argparse, json, pathlib, sys

REQUIRED = ["schema_version", "project", "sources", "beats", "assets", "scenes", "qa"]
SCENE_REQUIRED = ["id", "in", "out", "beat_ids", "layout", "purpose", "text_direction", "visuals", "review"]

def base(title="Torah lesson"):
    return {"schema_version": "0.1", "project": {"title": title, "duration": None, "language": "es", "aspect_ratio": "16:9"}, "sources": [], "beats": [], "assets": [], "scenes": [], "qa": {"blocking": [], "reviewed_by": [], "status": "draft"}}

def load(path):
    with open(path, encoding="utf-8") as f: return json.load(f)

def validate(data):
    errors=[]
    for key in REQUIRED:
        if key not in data: errors.append(f"missing top-level field: {key}")
    if errors: return errors
    ids=set()
    for source in data["sources"]:
        if not source.get("id"): errors.append("source missing id")
        ids.add(source.get("id"))
    beat_ids={b.get("id") for b in data["beats"]}
    for i, scene in enumerate(data["scenes"]):
        for key in SCENE_REQUIRED:
            if key not in scene: errors.append(f"scene {i} missing field: {key}")
        if not all(isinstance(scene.get(k), (int,float)) for k in ("in","out")): errors.append(f"scene {i} times must be numbers")
        elif scene["out"] <= scene["in"]: errors.append(f"scene {i} out must be greater than in")
        if scene.get("text_direction") not in ("ltr","rtl","mixed"): errors.append(f"scene {i} invalid text_direction")
        missing=set(scene.get("beat_ids",[]))-beat_ids
        if missing: errors.append(f"scene {i} references missing beats: {sorted(missing)}")
        review=scene.get("review", {})
        if review.get("status") == "final" and review.get("blocking"): errors.append(f"scene {i} marked final with blocking review items")
        ids.add(scene.get("id"))
    scenes=sorted((s for s in data["scenes"] if isinstance(s.get("in"),(int,float)) and isinstance(s.get("out"),(int,float))), key=lambda s:s["in"])
    for a,b in zip(scenes, scenes[1:]):
        if a["out"] > b["in"]: errors.append(f"scene overlap: {a.get('id')} and {b.get('id')}")
    if data["qa"].get("status") == "final" and data["qa"].get("blocking"): errors.append("project marked final with blocking QA items")
    return errors

def report(data):
    errors=validate(data)
    lines=[f"# QA report: {data.get('project',{}).get('title','Untitled')}", "", f"Status: `{data.get('qa',{}).get('status','unknown')}`", f"Scenes: {len(data.get('scenes',[]))}", f"Sources: {len(data.get('sources',[]))}", "", "## Blocking items"]
    blocking=data.get("qa",{}).get("blocking",[])
    lines += [f"- {x}" for x in blocking] or ["- None recorded"]
    lines += ["", "## Validator"] + ([f"- ERROR: {x}" for x in errors] or ["- PASS: structural checks passed"])
    return "\n".join(lines)+"\n"

def main():
    p=argparse.ArgumentParser(); sub=p.add_subparsers(dest="command", required=True)
    i=sub.add_parser("init"); i.add_argument("--out", required=True); i.add_argument("--title", default="Torah lesson")
    v=sub.add_parser("validate"); v.add_argument("manifest")
    r=sub.add_parser("report"); r.add_argument("manifest"); r.add_argument("--out", required=True)
    a=p.parse_args()
    if a.command=="init":
        pathlib.Path(a.out).write_text(json.dumps(base(a.title), ensure_ascii=False, indent=2)+"\n", encoding="utf-8"); return 0
    data=load(a.manifest); errors=validate(data)
    if a.command=="validate":
        if errors:
            print("INVALID"); print("\n".join(f"- {x}" for x in errors)); return 1
        print("VALID"); return 0
    pathlib.Path(a.out).write_text(report(data), encoding="utf-8"); print(a.out); return 1 if errors else 0

if __name__ == "__main__": sys.exit(main())
