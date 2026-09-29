"""Check computed LikeC4 membership and optional real raster export, without installs."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile


def run(*args, cwd=None):
    result = subprocess.run(args, cwd=cwd, text=True, capture_output=True, timeout=120)
    return {"command": list(args), "exit": result.returncode,
            "stdout": result.stdout, "stderr": result.stderr}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--raster", action="store_true", help="Use existing LikeC4 browser only")
    args = parser.parse_args()
    os.umask(0o077)
    report = {"version": run("likec4", "--version"), "help": {
        name: run("likec4", *command, "--help") for name, command in
        [("validate", ["validate"]), ("json", ["export", "json"]),
         ("png", ["export", "png"])]}, "checks": []}
    with tempfile.TemporaryDirectory(prefix="likec4-qualification-") as directory:
        root = Path(directory)
        (root / "model.c4").write_text('''specification {
 element service
 relationship async
 relationship sync
 deploymentNode host
}
model {
 external = service
 g = service { a = service b = service { c = service } }
 x = service
 y = service
 x -[async]-> y "publishes"
 x -[sync]-> y "publishes"
 x -[async]-> y "other"
}
''')
        (root / "views.c4").write_text('''model {
 extend x -[async]-> y "publishes" { metadata { checked "yes" } }
}
deployment { machine = host { xx = instanceOf x yy = instanceOf y } }
views {
 view descendants { include g.** }
 view accumulated { include external include g.** }
 view linked { include x include y }
}
''')
        validation = run("likec4", "validate", "--json", "--no-layout",
                         "--file", str(root / "model.c4"), "--file", str(root / "views.c4"), str(root))
        report["validation"] = validation
        data = json.loads(validation["stdout"])
        report["checks"].append({"case": "absolute-files-total-errors", "passed":
            validation["exit"] == 0 and data["valid"] and data["stats"]["filteredFiles"] == 2
            and data["stats"]["totalErrors"] == 0})
        exported = root / "computed.json"
        report["export"] = run("likec4", "export", "json", "--skip-layout", "-o", str(exported), str(root))
        model = json.loads(exported.read_text())
        report["computed_model"] = model
        for view, expected in [("descendants", {"g.a", "g.b", "g.b.c"}),
                               ("accumulated", {"external", "g.a", "g.b", "g.b.c"}),
                               ("linked", {"x", "y"})]:
            actual = {node["id"] for node in model["views"][view]["nodes"]}
            edges = model["views"][view]["edges"]
            report["checks"].append({"case": view, "nodes": sorted(actual), "edge_count": len(edges),
                "passed": actual == expected and len(edges) == (1 if view == "linked" else 0)})
        edge = model["views"]["linked"]["edges"][0]
        report["checks"].append({"case": "computed-edge-membership", "passed":
            edge["source"] == "x" and edge["target"] == "y"
            and set(edge["relations"]) == set(model["relations"])})
        relations = list(model["relations"].values())
        selected = [r for r in relations if r.get("metadata", {}).get("checked") == "yes"]
        report["checks"].append({"case": "typed-title-exact-extension", "passed": len(relations) == 3
            and len(selected) == 1 and selected[0].get("kind") == "async" and selected[0].get("title") == "publishes"})
        instances = model["deployments"]["elements"]
        report["checks"].append({"case": "deployment-instances", "passed":
            instances["machine.xx"].get("element") == "x" and instances["machine.yy"].get("element") == "y"})
        report["raster"] = {"status": "not requested"}
        if args.raster:
            cli = str(Path(shutil.which("likec4")).resolve())
            probe = run("node", "-e", '''const r=require('module').createRequire(process.argv[1]);const p=r('playwright');console.log(JSON.stringify({version:r('playwright/package.json').version,executable:p.chromium.executablePath(),exists:require('fs').existsSync(p.chromium.executablePath())}));''', cli)
            browser = json.loads(probe["stdout"])
            report["raster"] = {"browser": browser, "status": "unavailable"}
            if browser["exists"]:
                output = root / "png"
                result = run("likec4", "export", "png", str(root), "-o", str(output), "-f", "descendants", "--max-attempts", "1")
                images = list(output.rglob("*.png")) if output.exists() else []
                passed = result["exit"] == 0 and bool(images) and all(p.read_bytes().startswith(b"\x89PNG\r\n\x1a\n") for p in images)
                for image in images:
                    shutil.copyfile(image, args.output.with_name("likec4-" + image.name))
                report["raster"] = {"browser": browser, "command": result, "status": "passed" if passed else "failed",
                    "images": [{"name": p.name, "bytes": p.stat().st_size, "sha256": hashlib.sha256(p.read_bytes()).hexdigest()} for p in images]}
                report["checks"].append({"case": "actual-png-export", "passed": passed})
        # Temporary source paths are evidence of isolation; no private user data is collected.
        args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"checks": report["checks"], "raster": report["raster"]["status"]}, indent=2))
    return 0 if all(check["passed"] for check in report["checks"]) else 1


if __name__ == "__main__":
    raise SystemExit(main())
