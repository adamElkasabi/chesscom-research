#!/usr/bin/env python3
from pathlib import Path
import subprocess,ctypes,ctypes.util,resource,json,time,shutil
B=Path('/var/tmp/chess-forensic');OUT=B/'output/website-audit/wasm-analysis';script=Path('/home/user/forensic-mission-tools/runtime_probe.cjs')
# OS-enforced socket/connect denial, inherited by Node. No claim of a complete
# VM/container escape defense; V8 remains the WASM validation/execution boundary.
def restrict():
 resource.setrlimit(resource.RLIMIT_CPU,(25,30));resource.setrlimit(resource.RLIMIT_FSIZE,(20*1024*1024,20*1024*1024));resource.setrlimit(resource.RLIMIT_NOFILE,(64,64));resource.setrlimit(resource.RLIMIT_CORE,(0,0))
 lib=ctypes.CDLL(ctypes.util.find_library('seccomp'));lib.seccomp_init.argtypes=[ctypes.c_uint32];lib.seccomp_init.restype=ctypes.c_void_p;lib.seccomp_syscall_resolve_name.argtypes=[ctypes.c_char_p];lib.seccomp_rule_add.argtypes=[ctypes.c_void_p,ctypes.c_uint32,ctypes.c_int,ctypes.c_uint];lib.seccomp_load.argtypes=[ctypes.c_void_p]
 ctx=lib.seccomp_init(0x7fff0000)
 for syscall in [b'socket',b'connect',b'bind',b'listen',b'accept',b'accept4',b'socketpair']:
  number=lib.seccomp_syscall_resolve_name(syscall)
  if number>=0 and lib.seccomp_rule_add(ctx,0x00050001,number,0)!=0:raise RuntimeError('seccomp_rule_add failed')
 if lib.seccomp_load(ctx)!=0:raise RuntimeError('seccomp_load failed')
results=[]
for idx,path in enumerate(sorted((B/'input/extension/engines').rglob('*.wasm')),1):
 mid=f'module-{idx:03d}';dest=OUT/'modules'/mid;dest.mkdir(parents=True,exist_ok=True)
 if idx!=3:continue
 prior=dest/'runtime-observation.json'
 if prior.exists():shutil.copyfile(prior,dest/'runtime-observation.initial.json')
 args=['node','--experimental-permission','--allow-fs-read='+str(script),'--allow-fs-read='+str(path),'--max-old-space-size=256',str(script),str(path)]
 structure=dest/'structure.json';args.insert(2,'--allow-fs-read='+str(structure));args.append(str(structure))
 r={'module':mid,'command':args,'isolation':{'filesystem':'Node permission model: read-only allowlist of probe and binary, no write or child/worker grant','network':'Linux seccomp denies socket/connect/bind/listen/accept/socketpair; global fetch also throws','CPU_seconds':25,'wall_timeout_seconds':35,'JS_heap_MiB':256,'core_dumps':False},'scope':'NEW bounded structural instantiation; historical full native searches separately retained'}
 try:
  p=subprocess.run(args,capture_output=True,text=True,timeout=35,preexec_fn=restrict);r.update({'returncode':p.returncode,'stderr':p.stderr,'stdout':p.stdout})
  try:r['observation']=json.loads(p.stdout)
  except:pass
 except Exception as e:r['error']=repr(e)
 (dest/'runtime-observation.json').write_text(json.dumps(r,indent=2));results.append(r);print(mid,r.get('returncode'),r.get('error'),flush=True)
results=[json.loads(p.read_text()) for p in sorted((OUT/'modules').glob('*/runtime-observation.json'))]
(OUT/'runtime-summary.json').write_text(json.dumps(results,indent=2))
