import os,pathlib,tempfile,shutil,subprocess,json,select,time,hashlib
home=pathlib.Path('/home/aaron'); out=home/'code/personal-codex-skills/evals/audit-2026-09-29/inventory'
fixture=pathlib.Path(tempfile.mkdtemp(prefix='skill-audit-discovery-')); fixture.chmod(0o700)
codexhome=fixture/'codex'; codexhome.mkdir(); shutil.copytree(home/'.codex/skills',codexhome/'skills')
repo=fixture/'repo'; repo.mkdir(); subprocess.run(['git','init','-q',str(repo)],check=True)
copy=repo/'.agents/skills/plugin-creator'; copy.mkdir(parents=True); shutil.copy2(home/'.codex/skills/.system/plugin-creator/SKILL.md',copy/'SKILL.md')
def hashes(p): return {str(f.relative_to(p)):hashlib.sha256(f.read_bytes()).hexdigest() for f in p.rglob('*') if f.is_file()}
active_before=hashes(home/'.codex/skills'); before=hashes(codexhome/'skills')
env=dict(os.environ,CODEX_HOME=str(codexhome)); proc=subprocess.Popen(['codex','app-server','--listen','stdio://'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.DEVNULL,text=True,env=env,cwd=repo)
def req(obj): proc.stdin.write(json.dumps(obj)+'\n'); proc.stdin.flush()
def get(id):
 end=time.monotonic()+25
 while time.monotonic()<end:
  if select.select([proc.stdout],[],[],1)[0]:
   line=proc.stdout.readline()
   if not line: break
   obj=json.loads(line)
   if obj.get('id')==id:return obj
 return {'error':'timed out'}
req({'id':1,'method':'initialize','params':{'clientInfo':{'name':'skills-audit','version':'1.0'},'capabilities':{'experimentalApi':True}}}); init=get(1)
req({'method':'initialized','params':{}})
req({'id':2,'method':'skills/list','params':{'cwds':[str(repo),str(home/'code')],'forceReload':True}}); result=get(2)
proc.terminate()
try:proc.wait(timeout=5)
except subprocess.TimeoutExpired:proc.kill();proc.wait()
after=hashes(codexhome/'skills'); active_after=hashes(home/'.codex/skills')
safe={'cli_version':subprocess.check_output(['codex','--version'],text=True).strip(),'isolation':'Disposable CODEX_HOME with copied skill bundle only; no configuration, authentication, plugin installation state or model execution','initialize_error':init.get('error'),'result':result,'system_changes':{'removed':sorted(set(before)-set(after)),'added':sorted(set(after)-set(before)),'modified':[k for k in before.keys()&after.keys() if before[k]!=after[k]]},'active_system_unchanged':active_before==active_after}
# Restrict result to discovery metadata; no prompts/descriptions needed.
if 'result' in result:
 for item in result['result'].get('data',[]):
  item['skills']=[{k:v for k,v in s.items() if k in ('name','path','scope','enabled')} for s in item.get('skills',[])]
text=json.dumps(safe,indent=2).replace(str(fixture),'$DISPOSABLE').replace(str(home),'$HOME')
(out/'isolated-cli-discovery.json').write_text(text+'\n'); print(text)
