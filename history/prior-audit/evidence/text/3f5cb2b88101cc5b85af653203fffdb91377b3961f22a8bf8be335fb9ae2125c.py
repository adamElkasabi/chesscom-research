import re, base64, os, json, sys

src = open('shared.eager.BOGLllgUUR.chunk.js', encoding='utf-8', errors='replace').read()

# J("base64...")  or  J(`base64...`)
pat = re.compile(r'(?<![A-Za-z0-9_$])J\((["\`])([A-Za-z0-9+/=]{120,})\1')
hits = pat.findall(src)
print('descriptor blobs found:', len(hits))

def read_varint(b, i):
    r = 0; s = 0
    while True:
        x = b[i]; i += 1
        r |= (x & 0x7f) << s
        if not (x & 0x80): return r, i
        s += 7

def parse(b):
    """generic protobuf -> list of (field, wiretype, value)"""
    out = []; i = 0; n = len(b)
    while i < n:
        key, i = read_varint(b, i)
        f, wt = key >> 3, key & 7
        if wt == 0:
            v, i = read_varint(b, i)
        elif wt == 1:
            v = b[i:i+8]; i += 8
        elif wt == 2:
            l, i = read_varint(b, i); v = b[i:i+l]; i += l
        elif wt == 5:
            v = b[i:i+4]; i += 4
        else:
            raise ValueError(f'wire {wt} at {i}')
        out.append((f, wt, v))
    return out

TYPE = {1:'double',2:'float',3:'int64',4:'uint64',5:'int32',6:'fixed64',7:'fixed32',
        8:'bool',9:'string',10:'group',11:'message',12:'bytes',13:'uint32',14:'enum',
        15:'sfixed32',16:'sfixed64',17:'sint32',18:'sint64'}
LABEL = {1:'optional',2:'required',3:'repeated'}

def parse_fd(b):
    d = {'name':'','package':'','dependency':[],'messageType':[],'enumType':[],'syntax':''}
    for f, wt, v in parse(b):
        if f == 1: d['name'] = v.decode()
        elif f == 2: d['package'] = v.decode()
        elif f == 3: d['dependency'].append(v.decode())
        elif f == 4: d['messageType'].append(parse_msg(v))
        elif f == 5: d['enumType'].append(parse_enum(v))
        elif f == 12: d['syntax'] = v.decode()
    return d

def parse_msg(b):
    m = {'name':'','field':[],'nestedType':[],'enumType':[],'oneofDecl':[]}
    for f, wt, v in parse(b):
        if f == 1: m['name'] = v.decode()
        elif f == 2: m['field'].append(parse_field(v))
        elif f == 3: m['nestedType'].append(parse_msg(v))
        elif f == 4: m['enumType'].append(parse_enum(v))
        elif f == 8: m['oneofDecl'].append(parse_oneof(v))
    return m

def parse_oneof(b):
    o = {'name':''}
    for f, wt, v in parse(b):
        if f == 1: o['name'] = v.decode()
    return o

def parse_field(b):
    fl = {'name':'','number':0,'label':1,'type':1,'typeName':'','oneofIndex':None,'jsonName':''}
    for f, wt, v in parse(b):
        if f == 1: fl['name'] = v.decode()
        elif f == 3: fl['number'] = v
        elif f == 4: fl['label'] = v
        elif f == 5: fl['type'] = v
        elif f == 6: fl['typeName'] = v.decode()
        elif f == 9: fl['oneofIndex'] = v
        elif f == 10: fl['jsonName'] = v.decode()
    return fl

def parse_enum(b):
    e = {'name':'','value':[]}
    for f, wt, v in parse(b):
        if f == 1: e['name'] = v.decode()
        elif f == 2:
            ev = {'name':'','number':0}
            for g, w2, v2 in parse(v):
                if g == 1: ev['name'] = v2.decode()
                elif g == 2: ev['number'] = v2
            e['value'].append(ev)
    return e

def render_field(fl, in_oneof):
    t = TYPE[fl['type']]
    if fl['type'] == 11:
        t = fl['typeName']
    elif fl['type'] == 14:
        t = fl['typeName']
    lab = LABEL[fl['label']]
    if in_oneof:
        return f'  {t} {fl["name"]} = {fl["number"]};'
    if lab == 'optional':
        return f'  optional {t} {fl["name"]} = {fl["number"]};'
    return f'  {lab} {t} {fl["name"]} = {fl["number"]};'

def render_msg(m, indent=0):
    pad = '  ' * indent
    out = [f'{pad}message {m["name"]} {{']
    # group fields by oneof
    oneofs = m['oneofDecl']
    assigned = set()
    for i, oo in enumerate(oneofs):
        out.append(f'{pad}  oneof {oo["name"]} {{')
        for fl in m['field']:
            if fl['oneofIndex'] == i:
                out.append(render_field(fl, True)); assigned.add(fl['number'])
        out.append(f'{pad}  }}')
    for fl in m['field']:
        if fl['number'] in assigned: continue
        out.append(render_field(fl, False))
    for e in m['enumType']:
        out.append(f'{pad}  enum {e["name"]} {{')
        for v in e['value']:
            out.append(f'{pad}    {v["name"]} = {v["number"]};')
        out.append(f'{pad}  }}')
    for n in m['nestedType']:
        out.extend(render_msg(n, indent+1))
    out.append(f'{pad}}}')
    return out

files = []
for q, b64 in hits:
    try:
        raw = base64.b64decode(b64)
        fd = parse_fd(raw)
        files.append(fd)
    except Exception as ex:
        print('skip', ex)

print('decoded files:', len(files))
by_name = {f['name']: f for f in files}
os.makedirs('proto', exist_ok=True)
for f in files:
    base = os.path.basename(f['name'])
    lines = [f'// package {f["package"]}', f'// syntax: {f["syntax"] or "proto2"}']
    if f['dependency']:
        lines += [f'import "{d}";' for d in f['dependency']]
    lines.append('')
    lines.append(f'package {f["package"]};')
    lines.append('')
    for e in f['enumType']:
        lines.append(f'enum {e["name"]} {{')
        for v in e['value']: lines.append(f'  {v["name"]} = {v["number"]};')
        lines.append('}')
        lines.append('')
    for m in f['messageType']:
        lines += render_msg(m); lines.append('')
    open(os.path.join('proto', base), 'w').write('\n'.join(lines))

json.dump([f['name'] for f in files], open('proto/index.json','w'), indent=1)
print('\n'.join(sorted(f['name'] for f in files)))
