#!/usr/bin/env python3
"""Small fixed passive public-source batch; no account/session or endpoint guessing."""
from pathlib import Path
import urllib.request,urllib.error,urllib.parse,json,re,hashlib,ssl,socket,time
from html.parser import HTMLParser
B=Path('/var/tmp/chess-forensic');OUT=B/'output/website-audit';E=OUT/'evidence/new-public';E.mkdir(parents=True,exist_ok=True)
def scrub(t):
 t=re.sub(r'(?i)(set-cookie:)[^\n]*',r'\1 [VALUE OMITTED]',t)
 t=re.sub(r'(?i)(["\']?(?:csrfToken|csrf_token|sitekey|apiKey|access_token)["\']?\s*[:=]\s*["\'])[^"\']+',r'\1[REDACTED]',t)
 t=re.sub(r'https://[a-f0-9]{16,64}@','https://[REDACTED_PUBLIC_KEY]@',t)
 t=re.sub(r'\beyJ[A-Za-z0-9_-]{12,}\.[A-Za-z0-9_-]{12,}\.[A-Za-z0-9_-]{8,}\b','[REDACTED_JWT]',t)
 return t
class Visible(HTMLParser):
 def __init__(self):super().__init__();self.s=0;self.out=[]
 def handle_starttag(self,t,a):
  if t in ['script','style']:self.s+=1
 def handle_endtag(self,t):
  if t in ['script','style']:self.s=max(0,self.s-1)
 def handle_data(self,t):
  if not self.s and t.strip():self.out.append(t.strip())
URLS=['https://cloud.google.com/blog/products/databases/online-chess-platform-upgrades-to-cloud-sql-enterprise-plus','https://www.mysql.com/customers/view/?id=1446','https://www.escapethecity.org/opportunity/11267-senior-backend-php-product-engineer-at-chesscom','https://www.chess.com/jobs','https://www.chess.com/']
# Fetch exactly stylesheets actually declared in saved HTML, not guessed asset paths.
saved=B/'input/research/analysis.html';txt=saved.read_text();styles=[]
for link in re.findall(r'<link\b[^>]*>',txt,re.S|re.I):
 if re.search(r'rel\s*=\s*["\']stylesheet',link,re.I):
  h=re.search(r'href\s*=\s*["\']([^"\']+)',link,re.I)
  if h:styles.append(urllib.parse.urljoin('https://www.chess.com',h[1]))
URLS+=list(dict.fromkeys(styles))[:4]
records=[]
for u in URLS:
 rid=f'PUBLIC-{len(records)+1:03d}';rec={'id':rid,'url':u,'request_method':'GET','request_headers':{'User-Agent':'Mozilla/5.0 (compatible; public documentation review)','Accept':'text/html,text/css;q=0.9,*/*;q=0.1'},'credentials':'none; no cookies supplied','batch':'new passive public-source verification; host clock not used as historical observation date'}
 try:
  req=urllib.request.Request(u,headers=rec['request_headers'])
  with urllib.request.urlopen(req,timeout=25) as response:
   raw=response.read(6000000);rec.update({'status':response.status,'final_url':response.url,'headers':{k:('[VALUE OMITTED]' if k.lower()=='set-cookie' else v) for k,v in response.headers.items()},'downloaded_bytes':len(raw),'original_sha256':hashlib.sha256(raw).hexdigest()})
  text=scrub(raw.decode('utf8',errors='replace'));suf='.css' if 'text/css' in rec['headers'].get('Content-Type','') or '.css' in u else '.html';dest=E/(rid+suf);dest.write_text(text);rec['evidence_file']=str(dest.relative_to(OUT));rec['copy_sha256']=hashlib.sha256(dest.read_bytes()).hexdigest()
  if suf=='.html':
   v=Visible();v.feed(text);(E/(rid+'.txt')).write_text('\n'.join(v.out));rec['visible_text']=str((E/(rid+'.txt')).relative_to(OUT))
 except urllib.error.HTTPError as ex:rec.update({'status':ex.code,'error':str(ex),'headers':{k:('[VALUE OMITTED]' if k.lower()=='set-cookie' else v) for k,v in ex.headers.items()}})
 except Exception as ex:rec['error']=repr(ex)
 records.append(rec);print(rid,rec.get('status'),u,flush=True)
(OUT/'audit-metadata').mkdir(exist_ok=True);(OUT/'audit-metadata/public-request-log.json').write_text(json.dumps(records,indent=2))
# One public TLS/DNS observation per relevant host; no port scan.
infra=[]
for host in ['www.chess.com','analysis.chess.com']:
 r={'host':host,'port':443,'scope':'new passive DNS/TLS connection; no application authentication'}
 try:
  r['addresses']=sorted(set(x[4][0] for x in socket.getaddrinfo(host,443,type=socket.SOCK_STREAM)))
  with socket.create_connection((host,443),timeout=10) as sock:
   with ssl.create_default_context().wrap_socket(sock,server_hostname=host) as ss:r.update({'tls_version':ss.version(),'cipher':ss.cipher(),'certificate':ss.getpeercert()})
 except Exception as ex:r['error']=repr(ex)
 infra.append(r)
(OUT/'audit-metadata/dns-tls-observations.json').write_text(json.dumps(infra,indent=2))
