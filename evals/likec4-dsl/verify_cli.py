"""Verify maintenance claims with an installed LikeC4 CLI and temporary fixtures."""
import argparse
import json
from pathlib import Path
import subprocess
import tempfile

BASE = '''specification {
 element service
 deploymentNode host
 relationship async
 relationship sync
}
model {
 a = service
 b = service
 c = service
 payment- = service
 a -[async]-> b "publishes"
 a -[sync]-> b "publishes"
 b -> c
}
'''
CASES = [
    ("trailing-hyphen", 'views { view all { include * } }', True),
    ("named-instance", 'deployment { machine = host { api = instanceOf a } }', True),
    ("root-instance-rejected", 'deployment { api = instanceOf a }', False),
    ("typed-extension", 'model { extend a -[async]-> b "publishes" { metadata { checked "yes" } } }', True),
    ("binary-bidirectional", 'views { view all { include a <-> b } }', True),
    ("either-direction", 'views { view all { include -> a -> } }', True),
    ("prefix-bidirectional-rejected", 'views { view all { include <-> b } }', False),
    ("return-steps", 'views { dynamic view flow {\n a -> b -> c\n b <- c\n a <- b\n} }', True),
    ("nested-parallel-rejected", 'views { dynamic view flow { parallel { parallel {\n a -> b\n b -> c\n} } } }', False),
]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    version = subprocess.run(["likec4", "--version"], check=True, capture_output=True, text=True).stdout.strip()
    results = []
    with tempfile.TemporaryDirectory(prefix="skill-likec4-eval-") as directory:
        root = Path(directory)
        for name, body, valid in CASES:
            project = root / name
            project.mkdir()
            (project / "model.c4").write_text(BASE)
            (project / "views.c4").write_text(body + "\n")
            run = subprocess.run([
                "likec4", "validate", "--json", "--no-layout",
                "--file", str(project / "model.c4"),
                "--file", str(project / "views.c4"), str(project),
            ], capture_output=True, text=True, timeout=30)
            data = json.loads(run.stdout)
            stats = data["stats"]
            passed = stats["filteredFiles"] == 2 and data["valid"] == valid and (run.returncode == 0) == valid
            results.append({"case": name, "expected_valid": valid, "passed": passed, "exit": run.returncode, "stats": stats})
        # A wrong relative filter can report success without checking any file.
        run = subprocess.run(["likec4", "validate", "--json", "--no-layout", "--file", "missing.c4", str(project)], cwd=root, capture_output=True, text=True, timeout=30)
        data = json.loads(run.stdout)
        results.append({"case": "empty-filter-detection", "passed": data["stats"]["filteredFiles"] == 0 and data["stats"]["totalErrors"] > 0, "exit": run.returncode, "stats": data["stats"]})
    report = {"version": version, "layout_tested": False, "results": results}
    text = json.dumps(report, indent=2) + "\n"
    if args.output:
        args.output.write_text(text)
    print(text, end="")
    return 0 if all(item["passed"] for item in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
