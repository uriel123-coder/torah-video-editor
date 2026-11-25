import json, pathlib, subprocess, sys, unittest
ROOT=pathlib.Path(__file__).parents[1]
TOOL=ROOT/"scripts"/"semantic_manifest.py"

class ManifestTests(unittest.TestCase):
    def run_tool(self, *args):
        return subprocess.run([sys.executable, str(TOOL), *map(str,args)], capture_output=True, text=True)
    def test_examples_validate_structurally(self):
        for p in (ROOT/"examples").glob("*.json"):
            r=self.run_tool("validate", p)
            self.assertEqual(r.returncode, 0, r.stdout+r.stderr)
    def test_init_creates_valid_manifest(self):
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            out=pathlib.Path(d)/"new.json"
            self.assertEqual(self.run_tool("init", "--out", out, "--title", "Test").returncode, 0)
            self.assertEqual(self.run_tool("validate", out).returncode, 0)
    def test_overlap_is_rejected(self):
        data=json.loads((ROOT/"examples/edit-manifest.example.json").read_text())
        data["scenes"].append({"id":"bad","in":7,"out":10,"beat_ids":["b-01"],"layout":"presenter-full","purpose":"bad","text_direction":"ltr","visuals":[],"review":{"status":"draft","blocking":[]}})
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            p=pathlib.Path(d)/"bad.json"; p.write_text(json.dumps(data))
            self.assertNotEqual(self.run_tool("validate", p).returncode, 0)

    def test_project_integration_references_are_present(self):
        integration=(ROOT/"references/gemara-visual-integration.md").read_text()
        hyper=(ROOT/"references/hyperframes-export.md").read_text()
        for term in ("VisualSpec", "src/design/tokens.ts", "sampleAt(t)", "No inventado"):
            self.assertIn(term, integration)
        for term in ("npx hyperframes check --json", "same moment ids", "must not receive a prompt"):
            self.assertIn(term, hyper)

    def test_video_input_requires_timestamps_and_has_fallback(self):
        doc=(ROOT/"references/video-input.md").read_text()
        script=(ROOT/"scripts/transcribe_video.py").read_text()
        for term in ("timestamped", "speech-to-scene contract", "openai-whisper", "stop semantic editing"):
            self.assertIn(term, doc)
        for term in ("--word_timestamps", "video not found", "Whisper is not installed"):
            self.assertIn(term, script)

if __name__ == "__main__": unittest.main()
