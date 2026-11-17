from pathlib import Path
import json,base64,hashlib
import os
D=Path(os.environ.get('EVIDENCE_DIR',Path(__file__).resolve().parent.parent/'evidence'))
def vi(b,p):
 n=0;s=0
 while 1:
  v=b[p];p+=1;n|=(v&127)<<s
  if v<128:return n,p
  s+=7

def fields(b):
 p=0;o=[]
 while p<len(b):
  k,p=vi(b,p);w=k&7
  if w==0:v,p=vi(b,p)
  elif w==2:n,p=vi(b,p);v=b[p:p+n];p+=n
  elif w in (1,5):n=8 if w==1 else 4;v=b[p:p+n];p+=n
  else:raise ValueError(w)
  o.append((k>>3,w,v))
 return o

def first(b,no,default=b''):return next((v for n,w,v in fields(b)if n==no),default)
summary=[];services=[]
for d in json.load(open(D/'current-descriptors.json')):
 b=base64.b64decode(d['base64']+'='*((-len(d['base64']))%4));name=first(b,1).decode();r={k:v for k,v in d.items()if k!='base64'};r.update(name=name,sha256=hashlib.sha256(b).hexdigest());summary.append(r)
 if any(t in name for t in ['/binary_interface','bot','charm','search','configurator']):
  p=D/'current-descriptors'/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b)
 for n,w,v in fields(b):
  if n!=6:continue
  srv={'file':name,'package':first(b,2).decode(),'name':first(v,1).decode(),'methods':[]}
  for n,w,m in fields(v):
   if n!=2:continue
   met={'name':first(m,1).decode(),'input':first(m,2).decode(),'output':first(m,3).decode(),'options':[]}
   for n,w,o in fields(first(m,4)):
    opt={'field':n,'wire':w,'value':o if w==0 else o.hex()}
    if w==2:
     try:opt['fields']=[{'field':x,'wire':y,'value':z if y==0 else z.hex()}for x,y,z in fields(o)]
     except:pass
    met['options'].append(opt)
   srv['methods'].append(met)
  services.append(srv)
(D/'descriptor-index.json').write_text(json.dumps(summary,indent=2));(D/'service-routing.json').write_text(json.dumps(services,indent=2))
for s in services:
 if any(x in s['name'].lower() for x in ['binary','engine','config']):
  print(s['file'],s['package'],s['name'])
  for m in s['methods']:
   if any(x in m['name'].lower()for x in ['bot','charm','artifact','search']):print(m)
