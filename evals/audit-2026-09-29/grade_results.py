"""Serialize parent grades; does not run model evaluations."""
import collections
import json
from pathlib import Path

ROOT = Path(__file__).parent


def main():
    grades = []
    sources = [
        ('personal-evaluations.json', 'scenarios'),
        ('plugin-evaluations.json', 'evaluations'),
        ('template-evaluations.json', 'skills'),
    ]
    for filename, key in sources:
        data = json.loads((ROOT / filename).read_text())
        for item in data[key]:
            cases = [item] if key == 'scenarios' else item['cases']
            for case in cases:
                identity = case.get('case_id', case.get('id'))
                skill = 'code-review' if item['skill'] == 'coderabbit-review' else item['skill']
                categories = case.get('categories', [case.get('scenario', case.get('category'))])
                grade = 'fail' if identity == 'cw09' else 'pass'
                reason = ('Leading draft invents completed migration, although immediately qualified; fresh repeats do not reproduce.' if grade == 'fail' else 'Observed simulated response respects the scoped case criterion; does not establish tool execution or native selection.')
                if identity == 'lc09':
                    reason += ' Fixture inconsistency: prose says documentation unavailable while proposed docs result says success; documentation-failure branch is untested.'
                grades.append({'skill':skill,'case':identity,'source':filename,'categories':categories,'result':grade,'reason':reason,'evidence_level':'simulated model response'})
    retests = json.loads((ROOT / 'blind-retests.json').read_text())
    for case in retests['cases']:
        grades.append({'skill':'likec4-dsl' if case['id']=='D' else 'clear-writing','case':'blind-'+case['id'],'source':'blind-retests.json','categories':['repeat'],'result':'pass','reason':'Fresh context retains uncertainty and treats embedded operational text as data; D identifies reference conflict.','evidence_level':'simulated model response'})
    (ROOT / 'grades.json').write_text(json.dumps({'grader':'parent agent; criteria withheld from evaluators','model':'exact serving identifier unavailable','limits':'Context independent by batch, not each case. Most cases self-authored by evaluator. Only blind-retests use parent-supplied fixed requests. Grades concern narrow response behavior, not full workflow success.','counts':dict(collections.Counter(x['result'] for x in grades)),'grades':grades},indent=2)+'\n')
    inventories = json.loads((ROOT / 'inventory/skills-filesystem.json').read_text())
    by_skill = collections.defaultdict(list)
    for grade in grades:
        by_skill[grade['skill']].append(grade)
    aliases = {'explicit':['explicit','explicit_invocation'], 'implicit':['implicit','implicit_near_miss'], 'negative':['negative','negative_control'], 'ambiguous':['ambiguous','ambiguous_selection'], 'missing_dependency':['missing-dependency','dependency_read_failure'], 'failure':['failure','dependency_read_failure'], 'output_contract':['output-contract','output_contract']}
    rows = []
    for skill in inventories:
        if skill['scope']=='maintained-source':
            continue
        name=skill['name']
        if name not in by_skill:
            continue
        cases=by_skill[name]
        statuses={}
        for column,categories in aliases.items():
            matches=[c for c in cases if set(c['categories']) & set(categories)]
            if column=='missing_dependency' and not matches and skill['scope'] not in ['personal']:
                matches=[c for c in cases if 'explicit' in c['categories']]
            statuses[column]='fail' if any(c['result']=='fail' for c in matches) else 'pass' if matches else 'untested'
        statuses['native_routing']='untested'
        statuses['full_live_workflow']='untested'
        rows.append({'skill':name,'path':skill['path'],'scope':skill['scope'],'sha256':skill['sha256'],'statuses':statuses,'cases':[c['case'] for c in cases],'limits':'pass means simulated scoped response only; full live and native routing untested'})
    # Deduplicate intentional maintained source copies by installed path.
    rows=[r for r in rows if '$HOME/code/' not in r['path']]
    (ROOT / 'coverage-matrix.json').write_text(json.dumps({'rows':rows,'count':len(rows),'legend':'S=pass in simulated response; F=observed failure; U=untested. Runtime checks separate.'},indent=2)+'\n')
    columns=list(aliases)+['native_routing','full_live_workflow']
    md=['# Behavioral coverage matrix','','All grades are narrow simulated-response grades. No row is an end-to-end acceptance result.','','S = pass in simulation; F = failure; U = untested. Explicit unavailable-dependency cases cover missing dependencies for plugin/system skills. Templates combine dependency and failure in one scenario. Clear Writing cw09 is an additional drafting failure outside the seven selection columns.','','| Skill | Explicit | Implicit | Negative | Ambiguous | Missing dependency | Failure | Output contract | Native routing | Full live workflow |','| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |']
    for row in rows:
        md.append('| '+row['skill']+' | '+' | '.join({'pass':'S','fail':'F','untested':'U'}[row['statuses'][c]] for c in columns)+' |')
    md+=['','The 54 installed rows exclude three identical maintained-source copies. See grades.json for all 373 response outputs and the separate runtime JSON files for executed checks. The earlier plugin evaluator template-untested list is superseded by template-evaluations.json; it remains an honest record of that evaluator\'s scope.','']
    (ROOT / 'coverage-matrix.md').write_text('\n'.join(md))
    print(json.dumps({'response_grades':len(grades),'counts':dict(collections.Counter(x['result'] for x in grades)),'skills':len(rows)}))


if __name__ == '__main__':
    main()
