import pathlib, json, hashlib, subprocess, pwd, os, re, tomllib
home=pathlib.Path('/home/aaron'); out=home/'code/personal-codex-skills/evals/audit-2026-09-29/inventory'
def clean(p): return str(p).replace(str(home),'$HOME')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
plugins=json.loads(subprocess.check_output(['codex','plugin','list','--json']))
for p in plugins['installed']:
 p.pop('source',None)
 if 'marketplaceSource' in p: p['marketplaceSource']={k:v for k,v in p['marketplaceSource'].items() if k in ('sourceType','source')}
(out/'plugins.json').write_text(json.dumps(plugins,indent=2)+'\n')
roots=[(home/'.agents/skills','personal'),(home/'.codex/skills','system-or-compatibility'),(home/'.codex/plugins/cache','plugin-cache'),(home/'code/personal-codex-skills/skills','maintained-source')]
for root in [pathlib.Path('/.agents/skills'),home/'.agents/skills',home/'code/.agents/skills',home/'code/personal-codex-skills/.agents/skills',pathlib.Path('/etc/codex/skills')]:
 if root.exists() and all(root!=r for r,s in roots): roots.append((root,'ancestor-or-admin'))
rows=[]
for root,scope in roots:
 for entry in sorted(root.rglob('SKILL.md')):
  text=entry.read_text(); name=re.search(r'^name:\s*[\'"]?([^\n\'"]+)',text,re.M)
  files=[]
  for f in sorted(entry.parent.rglob('*')):
   if f.is_file(): files.append({'path':str(f.relative_to(entry.parent)),'sha256':sha(f),'symlink':f.is_symlink(),'mode':oct(f.stat().st_mode&0o777)})
  meta=entry.parent/'agents/openai.yaml'
  row={'name':name.group(1) if name else entry.parent.name,'path':clean(entry),'scope':scope,'filesystem_owner':pwd.getpwuid(entry.stat().st_uid).pw_name,'sha256':sha(entry),'files':files,'policy_metadata':meta.read_text() if meta.exists() else None,'helpers':[f['path'] for f in files if f['path'].startswith(('scripts/','bin/'))],'references':[f['path'] for f in files if f['path'].startswith('references/')], 'provenance':'local maintained source and attribution' if scope in ('personal','maintained-source') else 'managed system bundle; upstream commit unknown' if scope=='system-or-compatibility' else 'cache path version; package presence alone does not prove enabled'}
  rows.append(row)
config=tomllib.loads((home/'.codex/config.toml').read_text())
safe={'skills_config':config.get('skills',{}).get('config',[]),'features_plugins':config.get('features',{}).get('plugins'),'plugin_entries':{k:{kk:vv for kk,vv in v.items() if kk in ('enabled',)} for k,v in config.get('plugins',{}).items() if isinstance(v,dict)}}
(out/'config-selection.json').write_text(json.dumps(safe,indent=2).replace(str(home),'$HOME')+'\n')
(out/'skills-filesystem.json').write_text(json.dumps(rows,indent=2)+'\n')
print(json.dumps({'skills':len(rows),'counts':{s:sum(r['scope']==s for r in rows) for _,s in roots},'plugin_count':len(plugins['installed']),'config_selection':safe},indent=2))
