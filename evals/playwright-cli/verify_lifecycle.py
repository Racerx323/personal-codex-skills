"""Qualify the installed CLI with synthetic loopback data; never install a runtime.

Run outside the filesystem sandbox. Only sanitized JSON enters the repository.
Raw artifacts are retained in an owner-private tempfile directory for inspection.
"""
import argparse
import functools
import hashlib
import http.server
import json
import os
from pathlib import Path
import re
import shutil
import stat
import subprocess
import tempfile
import threading
import time
import urllib.request
import urllib.parse
import uuid


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()
    os.umask(0o077)
    root = Path(tempfile.mkdtemp(prefix="playwright-qualification-"))
    output = root / "output"
    output.mkdir(mode=0o700)
    cli = Path(shutil.which("playwright-cli") or "MISSING").resolve(strict=True)
    package = cli.parent
    runtime = package / "node_modules/playwright"
    core = package / "node_modules/playwright-core"
    env = dict(os.environ, PLAYWRIGHT_MCP_OUTPUT_DIR=str(output),
               PLAYWRIGHT_HTML_OPEN="never", NO_COLOR="1")
    env.pop("PLAYWRIGHT_CLI_SESSION", None)
    names = ["qual-" + uuid.uuid4().hex[:12] for _ in range(3)]
    records, checks, owned = [], [], {}
    browser_process = None
    server = None

    def sanitize(value):
        return value.replace(str(root), "<private-task>").replace(str(Path.home()), "<home>")

    def command(argv, expected=0, timeout=60):
        result = subprocess.run([str(x) for x in argv], cwd=root, env=env,
                                capture_output=True, text=True, timeout=timeout)
        records.append({"argv": [sanitize(str(x)) for x in argv],
                        "exit": result.returncode, "stdout": sanitize(result.stdout),
                        "stderr": sanitize(result.stderr)})
        if expected is not None and (result.returncode != expected or
                                    (expected == 0 and "### Error" in result.stdout)):
            raise RuntimeError(sanitize(result.stdout + result.stderr))
        return result

    def run(index, *argv, **kwargs):
        return command([cli, "-s=" + names[index], *argv], **kwargs)

    def check(name, function):
        try:
            detail = function()
            checks.append({"name": name, "status": "pass", "detail": detail})
        except Exception as exc:
            checks.append({"name": name, "status": "fail", "error": sanitize(str(exc))})
        print(name + ": " + checks[-1]["status"], flush=True)

    def require(condition, message):
        if not condition:
            raise AssertionError(message)

    metadata = {"mode": "executed synthetic loopback qualification",
                "cli_version": json.loads((package / "package.json").read_text())["version"],
                "playwright_version": json.loads((runtime / "package.json").read_text())["version"],
                "core_version": json.loads((core / "package.json").read_text())["version"],
                "cli_sha256": digest(cli), "harness_sha256": digest(Path(__file__)),
                "runtime_manifest_sha256": digest(core / "browsers.json"),
                "private_root_mode": oct(stat.S_IMODE(root.stat().st_mode)),
                "private_root_owner_matches": root.stat().st_uid == os.getuid(),
                "documentation": ["https://github.com/microsoft/playwright-cli/blob/main/README.md",
                                  "https://github.com/microsoft/playwright-cli/blob/main/skills/playwright-cli/references/session-management.md"]}
    command([cli, "--version"])
    for topic in [None, "open", "attach", "detach", "state-save", "state-load", "tracing-stop", "video-start", "run-code"]:
        command([cli, "--help", *([topic] if topic else [])])
    executable = command(["node", "-e", "console.log(require(process.argv[1]).chromium.executablePath())", core]).stdout.strip()
    require(Path(executable).is_file(), "Installed Chromium executable absent; no download attempted")
    metadata["browser_executable"] = sanitize(executable)
    metadata["browser_binary_sha256"] = digest(Path(executable))
    metadata["browser_binary_version"] = command([executable, "--version"]).stdout.strip()
    config = root / "config.json"
    config.write_text(json.dumps({"browser": {"browserName": "chromium", "launchOptions": {"executablePath": executable, "headless": True}}, "outputDir": str(output)}))
    web = root / "web"
    web.mkdir(mode=0o700)
    (web / "index.html").write_text('''<!doctype html><title>Qualification fixture</title><button onclick="document.querySelector('p').textContent='Clicked'">Details</button><p>Waiting</p>''')
    class QuietHandler(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *args):
            pass
    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(QuietHandler, directory=str(web)))
    threading.Thread(target=server.serve_forever, daemon=True).start()
    url = f"http://127.0.0.1:{server.server_port}/"
    generated = None
    try:
        for index in [0, 1]:
            owned[index] = "close"
            run(index, "open", url, "--config=" + str(config))

        def pairing():
            result = run(0, "run-code", "async page => ({version: page.context().browser().version(), userAgent: await page.evaluate(() => navigator.userAgent)})")
            expected = next(x["browserVersion"] for x in json.loads((core / "browsers.json").read_text())["browsers"] if x["name"] == "chromium")
            require(expected in result.stdout, "Running browser does not match installed runtime manifest")
            return {"expected_browser_version": expected, "runtime_readback_matches": True}
        check("installed_cli_browser_pairing", pairing)

        def click():
            nonlocal generated
            run(0, "snapshot")
            snapshots = sorted(root.rglob("page-*.yml"))
            text = snapshots[-1].read_text()
            match = re.search(r'button "Details" \[ref=(e\d+)\]', text)
            require(match is not None, "Current snapshot button reference missing")
            result = run(0, "click", match.group(1))
            generated = re.search(r"```js\n(.*?)\n```", result.stdout, re.S).group(1)
            require(".click()" in generated, "CLI generated action missing")
            run(0, "run-code", "async page => { if(await page.locator('p').innerText() !== 'Clicked') throw new Error('click mismatch'); return 'verified click'; }")
            return {"generated_action": generated}
        check("snapshot_click_and_generated_action", click)

        def state():
            run(0, "eval", "() => {localStorage.setItem('synthetic', 'roundtrip'); document.cookie='synthetic=roundtrip; SameSite=Lax';}")
            state_path = output / "state.json"
            run(0, "state-save", state_path)
            require(state_path.is_file() and stat.S_IMODE(state_path.stat().st_mode) & 0o077 == 0, "State file permissions")
            run(1, "state-load", state_path)
            run(1, "goto", url)
            run(1, "run-code", "async page => { if(await page.evaluate(() => localStorage.getItem('synthetic')) !== 'roundtrip') throw new Error('storage failed'); if(!(await page.context().cookies()).some(c => c.name === 'synthetic' && c.value === 'roundtrip')) throw new Error('cookie failed'); return 'state verified'; }")
            return "Cookies and localStorage restored in second isolated session"
        check("state_roundtrip", state)

        def blocked():
            run(0, "eval", "() => new Promise((resolve,reject) => {const r=indexedDB.open('myDatabase',1); r.onsuccess=()=>{window.heldDB=r.result; resolve('open');}; r.onerror=()=>reject(r.error);})")
            result = run(0, "eval", "() => new Promise((resolve, reject) => { const request = indexedDB.deleteDatabase('myDatabase'); request.onsuccess = () => resolve('deleted'); request.onerror = () => reject(request.error); request.onblocked = () => reject(new Error('Database deletion blocked by an open connection')); })", expected=None)
            require("### Error" in result.stdout and "Database deletion blocked by an open connection" in result.stdout, "Blocked deletion not reported as an error")
            run(0, "eval", "() => window.heldDB.close()")
            return {"error_detected": True, "cli_exit": result.returncode, "policy": "Inspect error payload as well as process exit"}
        check("indexeddb_blocked_deletion", blocked)

        def failing():
            result = run(0, "run-code", "async page => { if(await page.locator('p').innerText() !== 'Requested but wrong') throw new Error('AUTHORITATIVE_ASSERTION_FAILED'); }", expected=None)
            require("### Error" in result.stdout and "AUTHORITATIVE_ASSERTION_FAILED" in result.stdout, "Deliberate false assertion was not detected")
            return {"cli_exit": result.returncode, "error_payload_detected": True, "expectation_unchanged": True}
        check("authoritative_failed_cli_assertion", failing)

        def evidence():
            run(0, "tracing-start")
            run(0, "video-start", output / "qualification.webm")
            run(0, "goto", url)
            run(0, "run-code", "async page => { await page.getByRole('button', {name:'Details'}).click(); return await page.locator('p').innerText(); }")
            run(0, "video-stop")
            run(0, "tracing-stop")
            traces = list(output.rglob("*.trace"))
            videos = list(output.rglob("*.webm"))
            require(traces and videos and all(p.stat().st_size > 0 for p in traces + videos), "Actual nonempty trace/video outputs absent")
            require(all(p.resolve().is_relative_to(output) for p in traces + videos), "Evidence escaped configured private output")
            return {"trace_paths": [str(p.relative_to(root)) for p in traces], "video_paths": [str(p.relative_to(root)) for p in videos]}
        check("actual_trace_video_paths", evidence)

        def cleanup():
            run(0, "close")
            del owned[0]
            run(1, "run-code", "async page => {if(await page.title() !== 'Qualification fixture') throw new Error('second session lost'); return 'second session survived';}")
            return "Targeted close preserves independently launched second session"
        check("targeted_cleanup", cleanup)

        def attached():
            nonlocal browser_process
            profile = root / "external-profile"
            profile.mkdir(mode=0o700)
            log = (root / "external-browser.log").open("w")
            browser_process = subprocess.Popen([executable, "--headless", "--remote-debugging-address=127.0.0.1", "--remote-debugging-port=0", "--user-data-dir=" + str(profile), "--no-first-run", "--disable-background-networking", url + "?tab=one"], cwd=root, env=env, stdout=log, stderr=log)
            log.close()
            endpoint_file = profile / "DevToolsActivePort"
            deadline = time.monotonic() + 15
            while not endpoint_file.exists() and time.monotonic() < deadline and browser_process.poll() is None:
                time.sleep(0.1)
            require(endpoint_file.exists(), "Synthetic CDP browser did not start")
            endpoint = "http://127.0.0.1:" + endpoint_file.read_text().splitlines()[0]
            def tabs():
                with urllib.request.urlopen(endpoint + "/json/list", timeout=5) as response:
                    return {x["id"]: x["url"] for x in json.load(response) if x["type"] == "page"}
            second_url = endpoint + "/json/new?" + urllib.parse.quote(url + "?tab=two", safe="")
            with urllib.request.urlopen(urllib.request.Request(second_url, method="PUT"), timeout=5) as response:
                json.load(response)
            before = tabs()
            require(set(before.values()) == {url + "?tab=one", url + "?tab=two"}, "Preexisting synthetic tabs missing")
            owned[2] = "detach"
            run(2, "attach", "--cdp=" + endpoint)
            run(2, "tab-new", url + "?tab=task")
            # Close only the newly selected task-created tab; preserve previous IDs.
            run(2, "tab-close")
            run(2, "detach")
            del owned[2]
            after = tabs()
            require(before == after and browser_process.poll() is None, "Detach changed previous tabs or terminated external browser")
            return {"preexisting_tab_count": len(before), "same_tab_ids_and_urls": True, "external_process_alive_after_detach": True}
        check("attached_detach_preserves_preexisting_tabs", attached)

        def generated_tests():
            require(generated is not None, "No emitted action available")
            project = root / "generated-tests"
            (project / "tests/group").mkdir(parents=True, mode=0o700)
            (project / "node_modules").mkdir()
            (project / "node_modules/playwright").symlink_to(runtime, target_is_directory=True)
            (project / "node_modules/@playwright").mkdir()
            # Alias the already installed identical test entrypoint; no npm operation.
            (project / "node_modules/@playwright/test").mkdir()
            (project / "node_modules/@playwright/test/index.js").write_text("module.exports = require('playwright/test');\n")
            (project / "tests/fixtures.ts").write_text("import {test as baseTest} from '@playwright/test';\nexport {expect} from '@playwright/test';\nexport const test = baseTest.extend({page: async ({page}, use) => { await page.goto(" + json.dumps(url) + "); await use(page); }});\n")
            (project / "playwright.config.js").write_text("module.exports=" + json.dumps({"testDir": "tests", "workers": 1, "retries": 0, "reporter": "line", "outputDir": str(output / "test-results"), "use": {"launchOptions": {"executablePath": executable}, "headless": True}}) + ";\n")
            scenario = "test('generated', async ({page}) => {" + generated + "\nawait expect(page.locator('p')).toHaveText('Clicked');});\n"
            (project / "tests/group/fixture.spec.ts").write_text("import {test,expect} from '../fixtures';\n" + scenario)
            (project / "tests/group/standalone.spec.ts").write_text("import {test,expect} from '@playwright/test';\ntest.beforeEach(async ({page})=>{await page.goto(" + json.dumps(url) + ");});\n" + scenario)
            runner = ["node", runtime / "cli.js", "test", "--config=" + str(project / "playwright.config.js")]
            good = command(runner)
            require("2 passed" in good.stdout, "Fixture and standalone generated tests did not both pass")
            wrong = project / "tests/group/wrong.spec.ts"
            wrong.write_text("import {test,expect} from '../fixtures';\ntest('authoritative wrong assertion', async ({page})=>{await expect(page.locator('p')).toHaveText('Requested but wrong',{timeout:500});});\n")
            bad = command(runner + ["wrong.spec.ts"], expected=1)
            require("1 failed" in bad.stdout and "Requested but wrong" in bad.stdout, "Runner did not fail authoritative assertion")
            return {"passing_tests": 2, "intentional_failing_tests": 1, "fixture_relative_import": "../fixtures", "standalone_navigation_present": True, "runner_source": "Installed playwright/test via temporary @playwright/test alias; no package installed"}
        check("generated_test_imports_and_assertions", generated_tests)
    except Exception as exc:
        checks.append({"name": "setup", "status": "fail", "error": sanitize(str(exc))})
    finally:
        for index, action in list(owned.items()):
            try:
                run(index, action)
            except Exception as exc:
                checks.append({"name": "cleanup_" + str(index), "status": "fail", "error": sanitize(str(exc))})
        if browser_process is not None and browser_process.poll() is None:
            browser_process.terminate()
            try:
                browser_process.wait(timeout=10)
            except subprocess.TimeoutExpired:
                browser_process.kill()
                browser_process.wait(timeout=10)
        server.shutdown()
        server.server_close()
    artifacts = []
    privacy_errors = []
    for path in sorted(root.rglob("*")):
        if path.is_symlink():
            continue
        info = path.stat()
        if stat.S_IMODE(info.st_mode) & 0o077 or info.st_uid != os.getuid():
            privacy_errors.append(str(path.relative_to(root)))
        if path.is_file():
            artifacts.append({"path": str(path.relative_to(root)), "bytes": info.st_size,
                              "mode": oct(stat.S_IMODE(info.st_mode)), "sha256": digest(path)})
    checks.append({"name": "raw_artifact_privacy", "status": "fail" if privacy_errors else "pass", "paths_with_excess_permissions": privacy_errors})
    metadata.update(checks=checks, records=records, artifacts=artifacts,
                    passed=all(x["status"] == "pass" for x in checks),
                    limitations=["Synthetic task-owned browsers only; no real user profiles or accounts", "No extension attach or interactive paused-test generation exercised", "Generated tests reuse CLI-emitted action; temporary module alias exposes installed playwright/test", "Raw artifacts retained in private task directory, not repository; binary traces/video not embedded"])
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(metadata, indent=2) + "\n")
    print(json.dumps({"passed": metadata["passed"], "private_artifacts": str(root), "report": str(args.report)}))
    return 0 if metadata["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
