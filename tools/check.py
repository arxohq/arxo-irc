#!/usr/bin/env python3
"""Addressed delivery checks. No package suite or full corpus is run."""
from pathlib import Path
import argparse,hashlib,json,subprocess,sys,gzip,concurrent.futures
ROOT=Path(__file__).resolve().parent.parent
EXPECTED={'eitc':['6197.98'],'foreign-tax-limit':['22500'],'foreign-tax-credit':['22500'],'wash-sale-loss':['2000'],'wash-sale-basis':['7000'],'eitc-missing-agi':[],'eitc-conflict':[],'eitc-unpinned-year':[],'wash-sale-before-30':['2000'],'wash-sale-before-31':[],'wash-sale-after-30':['2000'],'wash-sale-after-31':[],'replacement-period-with-boundary':['2025-03-30'],'replacement-period-without-boundary':[]}
def sha(data):return hashlib.sha256(data).hexdigest()
def read(path):return json.loads((ROOT/path).read_text())
def check_example(row):
 name=row['name'];folder=ROOT/'examples'/name
 p=subprocess.run(['law','eval',str(folder)],capture_output=True,timeout=180)
 assert p.returncode==0,(name,p.stderr.decode(),p.stdout[:400]);doc=json.loads(p.stdout);saved=(folder/'result.json').read_bytes();assert p.stdout==saved,(name,'canonical replay differs')
 result=doc['results'][0];assert result['evaluationStatus']=='COMPUTED',name
 if name=='eligibility-conflict':assert result['truthStatus']=='BOTH',result
 else:assert [v['value'] for v in result['value']]==EXPECTED[name],result
 assert not any(x['code']=='NON_EXECUTABLE_RULE' for x in doc.get('issues',[])),(name,'skipped rule')
 if name=='eitc-unpinned-year':assert any(x['code']=='MISSING_PARAMETER_VALUE' for x in doc['issues'])
 graph={n['id']:n for n in doc['proofGraph']['nodes']};visited=set();anchors=set();selections=[]
 world=read('.runtime/'+row['world']+'.json');source_nodes={n['id']:n for n in world['nodes']}
 rule_anchors=set()
 def visit(key):
  if key in visited:return
  visited.add(key);node=graph[key];anchors.update(node.get('sourceAnchors',[]));selections.extend(node.get('attributes',{}).get('a3Selections',[]))
  rule=node.get('rule') or node.get('attributes',{}).get('rule')
  if rule in source_nodes:rule_anchors.update(source_nodes[rule].get('anchors',[]))
  for child in node.get('premises',[]):visit(child)
 visit(result['proof'])
 if name=='eitc':assert any('IRC_S32_A' in a for a in rule_anchors) and selections,(anchors,selections)
 if name.startswith('wash-sale-') and result.get('value'):assert any('IRC_S1091' in a for a in rule_anchors)
 if name=='replacement-period-without-boundary':assert not any(a['literal']['predicate'].endswith('#civil_calendar_boundary_before') for a in read('examples/'+name+'/case.json')['assertions'])
 return {'name':name,'canonicalSha256':sha(p.stdout),'resultHash':doc['resultHash'],'proofHash':doc['proofGraph']['proofHash'],'status':result['evaluationStatus'],'value':result.get('value'),'truthStatus':result.get('truthStatus'),'queryProofNodes':len(visited),'querySourceAnchors':sorted(anchors),'queryRuleAnchorsFromPinnedSnapshot':sorted(rule_anchors),'queryA3Selections':selections,'issueCodes':sorted({x['code'] for x in doc.get('issues',[])})}
def main():
 args=argparse.ArgumentParser();args.add_argument('--examples-only',action='store_true');args.add_argument('--report',type=Path);opts=args.parse_args()
 subprocess.run(['node',str(ROOT/'tools/prepare.mjs')],check=True)
 if not opts.examples_only:
  pin=read('source-pin.json')
  for item in [pin['historicalSourceArchive'],pin['compilerSeed']]:assert sha((ROOT/item['path']).read_bytes())==item['sha256'].removeprefix('sha256:')
  for model in read('reports/current-models.json')['models']:
   raw=(ROOT/model['path']).read_bytes();assert sha(raw)==model['sha256'];doc=json.loads(raw);assert doc['schemaVersion']=='law.core.ir/0.7' and doc['semanticVersion']=='0.2.11' and doc['package']['version']=='0.1.1'
   assert sha(gzip.decompress((ROOT/model['compileContext']).read_bytes()))==model['compileContextSha256']
  for w in read('worlds/pin.json')['worlds'].values():
   for p in w['packageInputs']:assert sha((ROOT/p['path']).read_bytes())==p['sha256']
 rows=read('examples/index.json')
 with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:checked=list(pool.map(check_example,rows))
 report={'scope':'addressed IRC reader delivery','runtime':read('toolchain.lock.json'),'examples':checked,'releaseVerified':False,'corpus':'not_checked'}
 if opts.report:opts.report.write_text(json.dumps(report,indent=2)+'\n')
 print('PASS: '+str(len(checked))+' canonical example replays; full corpus not_checked.')
if __name__=='__main__':main()
