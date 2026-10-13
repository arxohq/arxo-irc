import {readFileSync,writeFileSync,mkdirSync,renameSync,existsSync} from 'node:fs';
import {gunzipSync} from 'node:zlib';
import {createHash} from 'node:crypto';
import {execFileSync} from 'node:child_process';
import {dirname,resolve,join} from 'node:path';
import {fileURLToPath} from 'node:url';
const root=resolve(dirname(fileURLToPath(import.meta.url)),'..');
const hash=b=>createHash('sha256').update(b).digest('hex');
const pin=JSON.parse(readFileSync(join(root,'worlds/pin.json')));
const runtime=JSON.parse(readFileSync(join(root,'toolchain.lock.json')));
const version=JSON.parse(execFileSync('law',['version','--json'],{encoding:'utf8'}));
const target=runtime.targets[process.platform+'-'+process.arch];
if(!target||version.tool!==runtime.binaryVersion||version.binaryHash!=='sha256:'+target.binarySha256)throw Error('Install the tested CLI: npm install -g @arxo/cli@'+runtime.npmVersion);
const cache=join(root,'.runtime');mkdirSync(cache,{recursive:true});
for(const [name,p] of Object.entries(pin.worlds)){
 const world=join(cache,name+'.json');
 if(!existsSync(world)||hash(readFileSync(world))!==p.worldSha256){
  const archive=readFileSync(join(root,'worlds',name+'.json.gz'));
  if(hash(archive)!==p.gzipSha256||archive.length!==p.gzipBytes)throw Error('World archive integrity mismatch: '+name);
  const raw=gunzipSync(archive);
  if(hash(raw)!==p.worldSha256||raw.length!==p.worldBytes)throw Error('World integrity mismatch: '+name);
  writeFileSync(world+'.tmp',raw);renameSync(world+'.tmp',world);
 }
}
console.log('Verified IRC reader worlds. Run: law eval examples/eitc');
