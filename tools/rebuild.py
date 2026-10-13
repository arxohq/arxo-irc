#!/usr/bin/env python3
"""Reproduce selected compiler snapshots from pinned source and native contexts."""
from pathlib import Path
import argparse,gzip,hashlib,json,subprocess,tempfile
root=Path(__file__).resolve().parent.parent
p=argparse.ArgumentParser();p.add_argument('--package',action='append',required=True);args=p.parse_args()
models=json.loads((root/'reports/current-models.json').read_text())['models']
for name in args.package:
 model=next(x for x in models if x['name']==name)
 with tempfile.TemporaryDirectory(prefix='irc-lowering-') as tmp:
  ctx=Path(tmp)/'imports.json';ctx.write_bytes(gzip.decompress((root/model['compileContext']).read_bytes()))
  process=subprocess.run(['law','engine','lower',str(root/model['owner']),'--imports',str(ctx),'--exact-release','law.core/0.2.11'],capture_output=True)
  if process.returncode:raise SystemExit(process.stderr.decode())
  assert hashlib.sha256(process.stdout).hexdigest()==model['sha256'],name+' lowering differs'
 print('PASS:',model['spec'],'native source lowering is byte reproducible')
