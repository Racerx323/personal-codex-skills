"""Synthetic local skill checks; no downloads, active profiles, or installations."""
import functools
import http.server
import json
import os
from pathlib import Path
import subprocess
import tempfile
import threading
import uuid


def main():
    records = []
    with tempfile.TemporaryDirectory(prefix="skill-audit-browser-") as directory:
        root = Path(directory)
        root.chmod(0o700)
        (root / "index.html").write_text('<title>Audit fixture</title><button onclick="document.querySelector(\'p\').textContent=\'Details ready\'">Details</button><p>Waiting</p>')
        class QuietHandler(http.server.SimpleHTTPRequestHandler):
            def log_message(self, *args):
                pass
        server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(QuietHandler, directory=directory))
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        names = ["audit-" + uuid.uuid4().hex[:10] for _ in range(2)]
        env = dict(os.environ)
        env["PLAYWRIGHT_CLI_OUTPUT_DIR"] = str(root / "output")
        def run(name, *args):
            command = ["playwright-cli", "-s=" + name, *args]
            result = subprocess.run(command, cwd=root, env=env, capture_output=True, text=True, timeout=45)
            records.append({"args": command, "exit": result.returncode, "stdout": result.stdout.replace(directory, "<private-task>"), "stderr": result.stderr.replace(directory, "<private-task>")})
            if result.returncode != 0 or "### Error" in result.stdout:
                raise RuntimeError(result.stderr or result.stdout)
            return result.stdout
        error = None
        try:
            url = "http://127.0.0.1:" + str(server.server_port)
            for name in names:
                run(name, "open", url)
            run(names[0], "run-code", "async page => { await page.getByRole('button', {name:'Details'}).click(); if (await page.locator('p').innerText() !== 'Details ready') throw new Error('assertion failed'); return 'click verified'; }")
            run(names[0], "eval", "() => localStorage.setItem('audit-synthetic', 'fixture-only')")
            state = root / "state.json"
            run(names[0], "state-save", str(state))
            state.chmod(0o600)
            run(names[1], "state-load", str(state))
            run(names[1], "goto", url)
            run(names[1], "run-code", "async page => { if(await page.evaluate(() => localStorage.getItem('audit-synthetic')) !== 'fixture-only') throw new Error('state roundtrip failed'); return 'state verified'; }")
            run(names[0], "close")
            run(names[1], "run-code", "async page => { if(await page.title() !== 'Audit fixture') throw new Error('wrong browser'); return 'second owned session survived targeted close'; }")
        except Exception as exc:
            error = str(exc).replace(directory, "<private-task>")
        finally:
            for name in names:
                try:
                    run(name, "close")
                except Exception:
                    pass
            server.shutdown()
            server.server_close()
        report = {"mode":"live loopback synthetic integration", "error":error,"records":records,"limitations":["No real authenticated profiles", "Attached-browser detach not exercised in this run", "Generated test runner and raster export not exercised"]}
    Path(__file__).with_name("browser-runtime.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"error":error,"commands":len(records)}))


if __name__ == "__main__":
    main()
