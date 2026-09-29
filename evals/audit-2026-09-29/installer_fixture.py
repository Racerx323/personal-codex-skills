"""Offline installer substitution simulation in task-owned disposable storage."""
import contextlib
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import sys
import tempfile

sys.dont_write_bytecode = True
SCRIPT = Path('/home/aaron/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py')


def main():
    sys.path.insert(0, str(SCRIPT.parent))
    spec = importlib.util.spec_from_file_location('audited_installer', SCRIPT)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    original_copy = module._copy_skill
    original_temp = module.tempfile.gettempdir
    cases = []
    for repeat in range(2):
        with tempfile.TemporaryDirectory(prefix='installer-audit-') as directory:
            root = Path(directory)
            temp_parent = root / 'shared'
            temp_parent.mkdir()
            (temp_parent / 'codex').mkdir(mode=0o777)
            module.tempfile.gettempdir = lambda: str(temp_parent)
            def prepare(source, method, tmp_dir):
                repo = Path(tmp_dir) / 'repo'
                skill = repo / 'demo'
                skill.mkdir(parents=True)
                (skill / 'SKILL.md').write_text('---\nname: demo\ndescription: safe fixture\n---\nOriginal fixture\n')
                return str(repo)
            module._prepare_repo = prepare
            def substituted_copy(src, dest):
                child = Path(src).parents[1]
                child.rename(child.with_name(child.name + '-moved'))
                replacement = Path(src)
                replacement.mkdir(parents=True)
                (replacement / 'SKILL.md').write_text('---\nname: demo\ndescription: synthetic replacement\n---\nAUDIT_REPLACEMENT_MARKER\n')
                original_copy(src, dest)
            module._copy_skill = substituted_copy
            stream = io.StringIO()
            with contextlib.redirect_stdout(stream):
                rc = module.main(['--repo','synthetic/fixture','--path','demo','--dest',str(root / 'destination')])
            installed = (root / 'destination/demo/SKILL.md').read_text()
            cases.append({'repeat':repeat+1,'exit':rc,'replacement_installed':'AUDIT_REPLACEMENT_MARKER' in installed,'stdout':stream.getvalue().replace(directory,'<fixture>')})
            module.tempfile.gettempdir = original_temp
    report = {'helper_sha256':hashlib.sha256(SCRIPT.read_bytes()).hexdigest(),'mode':'actual installer main/validation/copy executed with mocked download and same-UID simulation of parent-owner replacement; no network, actual installation, second UID or live race','cases':cases,'prerequisite':'Local adversary can precreate and control the shared codex temp parent; child mode0700 does not protect its directory entry from its parent owner.'}
    Path(__file__).with_name('installer-fixture.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report))


if __name__ == '__main__':
    main()
