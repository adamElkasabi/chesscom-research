// Generic protobuf codec driven by chess.com's own FileDescriptorProtos.
// Wire output is byte-compatible with the decoder chess.com ships in
// shared.eager.BOGLllgUUR.chunk.js (`Mk(OH, bytes)`).
//
// Shape matches @bufbuild/protobuf (what chess.com uses):
//   message  -> { fieldLocalName: value, ... }
//   oneof    -> { oneofLocalName: { case, value } }
//   repeated -> array

import { DESCRIPTORS } from './descriptors.js';

/* ------------------------------------------------------------------ */
/* descriptor decoding                                                 */
/* ------------------------------------------------------------------ */

function readVarint(b, i) {
  let r = 0n, s = 0n;
  for (;;) {
    if (i >= b.length) throw new Error('varint overrun');
    const x = b[i++];
    r |= BigInt(x & 0x7f) << s;
    if ((x & 0x80) === 0) break;
    s += 7n;
    if (s > 70n) throw new Error('varint too long');
  }
  return [r, i];
}

function readBytes(b, i) {
  const [len, j] = readVarint(b, i);
  const n = Number(len);
  if (j + n > b.length) throw new Error('length overrun');
  return [b.subarray(j, j + n), j + n];
}

function walkFields(b) {
  const out = [];
  let i = 0;
  while (i < b.length) {
    const [key, j] = readVarint(b, i);
    i = j;
    const no = Number(key >> 3n), wt = Number(key & 7n);
    if (wt === 0) { const [v, k] = readVarint(b, i); out.push([no, wt, v]); i = k; }
    else if (wt === 1) { out.push([no, wt, b.subarray(i, i + 8)]); i += 8; }
    else if (wt === 2) { const [v, k] = readBytes(b, i); out.push([no, wt, v]); i = k; }
    else if (wt === 5) { out.push([no, wt, b.subarray(i, i + 4)]); i += 4; }
    else throw new Error('unsupported wire type ' + wt);
  }
  return out;
}

function parseFileDescriptor(raw) {
  const f = { name: '', package: '', dependency: [], messageType: [], enumType: [], syntax: 'proto2' };
  for (const [no, , v] of walkFields(raw)) {
    if (no === 1) f.name = str(v);
    else if (no === 2) f.package = str(v);
    else if (no === 3) f.dependency.push(str(v));
    else if (no === 4) f.messageType.push(parseMessage(v));
    else if (no === 5) f.enumType.push(parseEnum(v));
    else if (no === 12) f.syntax = str(v);
  }
  return f;
}
function parseMessage(raw) {
  const m = { name: '', field: [], nestedType: [], enumType: [], oneofDecl: [] };
  for (const [no, , v] of walkFields(raw)) {
    if (no === 1) m.name = str(v);
    else if (no === 2) m.field.push(parseField(v));
    else if (no === 3) m.nestedType.push(parseMessage(v));
    else if (no === 4) m.enumType.push(parseEnum(v));
    else if (no === 8) m.oneofDecl.push(parseOneof(v));
  }
  return m;
}

/** OneofDescriptorProto: 1 = name */
function parseOneof(raw) {
  const o = { name: '' };
  for (const [no, , v] of walkFields(raw)) {
    if (no === 1) { o.name = str(v); break; }
  }
  return o;
}
function parseField(raw) {
  const fl = {
    name: '', number: 0, label: 1, type: 1, typeName: '',
    oneofIndex: null, jsonName: '', proto3Optional: false,
  };
  for (const [no, , v] of walkFields(raw)) {
    if (no === 1) fl.name = str(v);
    else if (no === 3) fl.number = Number(v);
    else if (no === 4) fl.label = Number(v);
    else if (no === 5) fl.type = Number(v);
    else if (no === 6) fl.typeName = str(v);
    else if (no === 9) fl.oneofIndex = Number(v);
    else if (no === 10) fl.jsonName = str(v);
    else if (no === 17) fl.proto3Optional = v !== 0;
  }
  // proto3 `optional` creates a *synthetic* oneof named `_field`. Those are
  // plain fields with presence, never a {case,value} group.
  if (fl.proto3Optional) fl.oneofIndex = null;
  return fl;
}

/** Real (non-synthetic) oneof members of a message. */
function realOneofIndex(m, f) {
  if (f.oneofIndex === null || f.oneofIndex === undefined) return null;
  const oo = m.oneofDecl[f.oneofIndex];
  if (oo && oo.name && oo.name.startsWith('_')) return null;
  return f.oneofIndex;
}
function parseEnum(raw) {
  const e = { name: '', value: [] };
  for (const [no, , v] of walkFields(raw)) {
    if (no === 1) e.name = str(v);
    else if (no === 2) {
      const ev = { name: '', number: 0 };
      for (const [g, , w] of walkFields(v)) {
        if (g === 1) ev.name = str(w);
        else if (g === 2) ev.number = Number(w);
      }
      e.value.push(ev);
    }
  }
  return e;
}
function str(u8) { return new TextDecoder().decode(u8); }

/* ------------------------------------------------------------------ */
/* registry                                                            */
/* ------------------------------------------------------------------ */

const b64 = (s) => {
  const bin = atob(s);
  const out = new Uint8Array(bin.length);
  for (let i = 0; i < bin.length; i++) out[i] = bin.charCodeAt(i);
  return out;
};

let registry = null;
function getRegistry() {
  if (registry) return registry;
  const messages = new Map();   // '.pkg.Msg' -> descriptor
  const enums = new Map();      // '.pkg.Enum' -> descriptor
  const files = new Map();
  for (const key of Object.keys(DESCRIPTORS)) {
    let fd;
    try { fd = parseFileDescriptor(b64(DESCRIPTORS[key])); } catch { continue; }
    if (!fd.name) continue;
    files.set(fd.name, fd);
    const prefix = fd.package ? '.' + fd.package + '.' : '.';
    const walkMsg = (m, base) => {
      const full = base + m.name;
      messages.set(full, m);
      for (const e of m.enumType) enums.set(full + '.' + e.name, e);
      for (const n of m.nestedType) walkMsg(n, full + '.');
    };
    for (const m of fd.messageType) walkMsg(m, prefix);
    for (const e of fd.enumType) enums.set(prefix + e.name, e);
  }
  registry = { messages, enums, files };
  return registry;
}

export function messageDescriptor(fullName) {
  const r = getRegistry();
  const n = fullName.startsWith('.') ? fullName : '.' + fullName;
  const m = r.messages.get(n);
  if (!m) throw new Error('unknown message type: ' + fullName);
  return m;
}
export function enumDescriptor(fullName) {
  const r = getRegistry();
  const n = fullName.startsWith('.') ? fullName : '.' + fullName;
  return r.enums.get(n) || null;
}

/* ------------------------------------------------------------------ */
/* naming (matches @bufbuild/protobuf localName)                       */
/* ------------------------------------------------------------------ */

export function camel(name) {
  return name.replace(/_([a-z])/g, (_, c) => c.toUpperCase());
}

/* ------------------------------------------------------------------ */
/* wire types                                                          */
/* ------------------------------------------------------------------ */

const T_DOUBLE = 1, T_FLOAT = 2, T_INT64 = 3, T_UINT64 = 4, T_INT32 = 5,
      T_FIXED64 = 6, T_FIXED32 = 7, T_BOOL = 8, T_STRING = 9, T_GROUP = 10,
      T_MESSAGE = 11, T_BYTES = 12, T_UINT32 = 13, T_ENUM = 14,
      T_SFIXED32 = 15, T_SFIXED64 = 16, T_SINT32 = 17, T_SINT64 = 18;

function wireTypeOf(t) {
  switch (t) {
    case T_DOUBLE: case T_FIXED64: case T_SFIXED64: return 1;
    case T_STRING: case T_BYTES: case T_MESSAGE: case T_GROUP: return 2;
    case T_FLOAT: case T_FIXED32: case T_SFIXED32: return 5;
    default: return 0;
  }
}

/* ------------------------------------------------------------------ */
/* writer                                                              */
/* ------------------------------------------------------------------ */

class Writer {
  constructor() { this.chunks = []; this.len = 0; }
  push(u8) { this.chunks.push(u8); this.len += u8.length; }
  varint(v) {
    let n = typeof v === 'bigint' ? v : BigInt(v);
    if (n < 0n) n += 1n << 64n; // two's complement for int64/int32
    const bytes = [];
    for (;;) {
      const b = Number(n & 0x7fn);
      n >>= 7n;
      if (n === 0n) { bytes.push(b); break; }
      bytes.push(b | 0x80);
    }
    this.push(Uint8Array.from(bytes));
  }
  zigzag(v) {
    let n = BigInt(v);
    n = n < 0n ? (n << 1n) ^ -1n : (n << 1n);
    this.varint(n);
  }
  tag(no, wt) { this.varint((BigInt(no) << 3n) | BigInt(wt)); }
  bytes(u8) { this.varint(u8.length); this.push(u8); }
  float(x) { const b = new Uint8Array(4); new DataView(b.buffer).setFloat32(0, x, true); this.push(b); }
  double(x) { const b = new Uint8Array(8); new DataView(b.buffer).setFloat64(0, x, true); this.push(b); }
  fixed32(x) { const b = new Uint8Array(4); new DataView(b.buffer).setUint32(0, x >>> 0, true); this.push(b); }
  fixed64(x) { const b = new Uint8Array(8); new DataView(b.buffer).setBigUint64(0, BigInt(x) & 0xffffffffffffffffn, true); this.push(b); }
  sfixed32(x) { const b = new Uint8Array(4); new DataView(b.buffer).setInt32(0, x | 0, true); this.push(b); }
  sfixed64(x) { const b = new Uint8Array(8); new DataView(b.buffer).setBigInt64(0, BigInt(x), true); this.push(b); }
  finish() {
    const out = new Uint8Array(this.len);
    let o = 0;
    for (const c of this.chunks) { out.set(c, o); o += c.length; }
    return out;
  }
}

const te = new TextEncoder();

function writeScalar(w, type, v) {
  switch (type) {
    case T_DOUBLE: w.double(Number(v)); break;
    case T_FLOAT: w.float(Number(v)); break;
    case T_INT64: case T_INT32: w.varint(BigInt(v)); break;
    case T_UINT64: case T_UINT32: w.varint(BigInt(v)); break;
    case T_SINT64: case T_SINT32: w.zigzag(v); break;
    case T_FIXED64: w.fixed64(v); break;
    case T_SFIXED64: w.sfixed64(v); break;
    case T_FIXED32: w.fixed32(v); break;
    case T_SFIXED32: w.sfixed32(v); break;
    case T_BOOL: w.varint(v ? 1 : 0); break;
    case T_STRING: w.bytes(te.encode(String(v))); break;
    case T_BYTES: w.bytes(v instanceof Uint8Array ? v : new Uint8Array(v)); break;
    case T_ENUM: w.varint(BigInt(enumNumber(v, arguments[1]))); break;
    default: throw new Error('cannot write scalar type ' + type);
  }
}

function enumNumber(v, desc) {
  if (typeof v === 'number') return v;
  if (typeof v === 'string') {
    if (desc) { const e = desc.value.find((x) => x.name === v); if (e) return e.number; }
    const n = parseInt(v, 10);
    if (!Number.isNaN(n)) return n;
  }
  return 0;
}

function writeValue(w, field, value, edesc) {
  const wt = wireTypeOf(field.type);
  if (field.label === 3) { // repeated
    if (!Array.isArray(value) || value.length === 0) return;
    const packedScalar = wt === 0 || field.type === T_ENUM;
    if (packedScalar && field.type !== T_STRING && field.type !== T_BYTES) {
      w.tag(field.number, 2);
      const inner = new Writer();
      for (const item of value) writeScalarType(inner, field.type, item, edesc);
      w.bytes(inner.finish());
    } else {
      for (const item of value) {
        w.tag(field.number, wt);
        writeSingular(w, field, item, edesc);
      }
    }
    return;
  }
  if (value === undefined || value === null) return;
  w.tag(field.number, wt);
  writeSingular(w, field, value, edesc);
}

function writeScalarType(w, type, v, edesc) {
  if (type === T_ENUM) { w.varint(BigInt(enumNumber(v, edesc))); return; }
  writeScalar(w, type, v);
}

function writeSingular(w, field, value, edesc) {
  if (field.type === T_MESSAGE || field.type === T_GROUP) {
    w.bytes(encodeMessage(field.typeName, value));
    return;
  }
  if (field.type === T_ENUM) { w.varint(BigInt(enumNumber(value, edesc))); return; }
  writeScalar(w, field.type, value);
}

export function encodeMessage(fullName, obj) {
  const m = messageDescriptor(fullName);
  const w = new Writer();
  const handled = new Set();

  for (let oi = 0; oi < m.oneofDecl.length; oi++) {
    const oo = m.oneofDecl[oi];
    if (oo.name && oo.name.startsWith('_')) continue; // synthetic (proto3 optional)
    const lc = camel(oo.name);
    const sel = obj && obj[lc];
    if (!sel || typeof sel !== 'object' || !('case' in sel)) continue;
    handled.add(lc);
    const field = m.field.find(
      (f) => realOneofIndex(m, f) === oi && (f.name === sel.case || camel(f.name) === sel.case)
    );
    if (!field || sel.value === undefined || sel.value === null) continue;
    const edesc = field.type === T_ENUM ? enumDescriptor(field.typeName) : null;
    w.tag(field.number, wireTypeOf(field.type));
    writeSingular(w, field, sel.value, edesc);
  }

  for (const f of m.field) {
    if (realOneofIndex(m, f) !== null) continue;
    const lc = camel(f.name);
    if (handled.has(lc)) continue;
    const v = obj ? obj[lc] : undefined;
    if (v === undefined || v === null) continue;
    const edesc = f.type === T_ENUM ? enumDescriptor(f.typeName) : null;
    writeValue(w, f, v, edesc);
  }
  return w.finish();
}

/* ------------------------------------------------------------------ */
/* reader                                                              */
/* ------------------------------------------------------------------ */

function readScalar(b, type, pos) {
  switch (type) {
    case T_DOUBLE: { const v = new DataView(b.buffer, b.byteOffset + pos, 8).getFloat64(0, true); return [v, pos + 8]; }
    case T_FLOAT: { const v = new DataView(b.buffer, b.byteOffset + pos, 4).getFloat32(0, true); return [v, pos + 4]; }
    case T_FIXED64: { const v = new DataView(b.buffer, b.byteOffset + pos, 8).getBigUint64(0, true); return [Number(v), pos + 8]; }
    case T_SFIXED64: { const v = new DataView(b.buffer, b.byteOffset + pos, 8).getBigInt64(0, true); return [Number(v), pos + 8]; }
    case T_FIXED32: { const v = new DataView(b.buffer, b.byteOffset + pos, 4).getUint32(0, true); return [v, pos + 4]; }
    case T_SFIXED32: { const v = new DataView(b.buffer, b.byteOffset + pos, 4).getInt32(0, true); return [v, pos + 4]; }
    case T_STRING: { const [u, p] = readBytes(b, pos); return [str(u), p]; }
    case T_BYTES: { const [u, p] = readBytes(b, pos); return [u.slice(), p]; }
    case T_BOOL: { const [v, p] = readVarint(b, pos); return [v !== 0n, p]; }
    case T_SINT32: case T_SINT64: {
      const [v, p] = readVarint(b, pos);
      const n = (v >> 1n) ^ (-(v & 1n));
      return [Number(n), p];
    }
    default: { const [v, p] = readVarint(b, pos); return [Number(v), p]; }
  }
}

function pushInto(obj, lc, v, oneofName, caseName, repeated) {
  if (oneofName) {
    obj[camel(oneofName)] = { case: caseName, value: v };
  } else if (repeated) {
    if (!Array.isArray(obj[lc])) obj[lc] = obj[lc] === undefined ? [] : [obj[lc]];
    obj[lc].push(v);
  } else {
    obj[lc] = v;
  }
}

export function decodeMessage(fullName, bytes) {
  const m = messageDescriptor(fullName);
  const b = bytes instanceof Uint8Array ? bytes : new Uint8Array(bytes);
  const obj = {};
  let i = 0;
  while (i < b.length) {
    const [key, j] = readVarint(b, i); i = j;
    const no = Number(key >> 3n), wt = Number(key & 7n);
    const f = m.field.find((x) => x.number === no);
    if (!f) { // skip unknown
      if (wt === 0) { [, i] = readVarint(b, i); }
      else if (wt === 1) i += 8;
      else if (wt === 2) { const [, p] = readBytes(b, i); i = p; }
      else if (wt === 5) i += 4;
      else throw new Error('bad wire type ' + wt);
      continue;
    }
    const lc = camel(f.name);
    const oi = realOneofIndex(m, f);
    const oo = oi === null ? null : m.oneofDecl[oi];
    const caseName = camel(f.name);
    const rep = f.label === 3;

    if (rep && f.type !== T_STRING && f.type !== T_BYTES && wt === 0) {
      const [v, p] = readVarint(b, i); i = p;
      pushInto(obj, lc, f.type === T_ENUM ? Number(v) : v, null, null, true);
      continue;
    }
    if (rep && wt === 2 && (wireTypeOf(f.type) === 0 || f.type === T_ENUM)) {
      const [buf, p] = readBytes(b, i); i = p;
      let q = 0;
      while (q < buf.length) {
        const [v, k] = readVarint(buf, q); q = k;
        pushInto(obj, lc, f.type === T_ENUM ? Number(v) : v, null, null, true);
      }
      continue;
    }
    if (f.type === T_MESSAGE || f.type === T_GROUP) {
      const [buf, p] = readBytes(b, i); i = p;
      pushInto(obj, lc, decodeMessage(f.typeName, buf), oo ? oo.name : null, caseName, rep);
      continue;
    }
    if (f.type === T_ENUM && wt === 0) {
      const [v, p] = readVarint(b, i); i = p;
      pushInto(obj, lc, Number(v), oo ? oo.name : null, caseName, rep);
      continue;
    }
    const [v, p] = readScalar(b, f.type, i); i = p;
    pushInto(obj, lc, v, oo ? oo.name : null, caseName, rep);
  }
  return obj;
}

/* helpers ------------------------------------------------------------ */

/**
 * One CEAC WebSocket message carries exactly one raw protobuf message
 * (`C3e` hands the ArrayBuffer straight to `fromBinary(GameReviewResponse)`),
 * so "framing" here is just a normalisation to a Uint8Array.
 */
export function frame(bytes) {
  return bytes instanceof Uint8Array ? bytes : new Uint8Array(bytes);
}

/** Split a concatenated byte stream into individual messages (identity). */
export function unframe(bytes) {
  return [frame(bytes)];
}

/** Encode + frame in one step. */
export function frameMessage(typeName, obj) {
  return frame(encodeMessage(typeName, obj));
}
export function gameReviewResponse(resultCase, value) {
  return encodeMessage('.chesscom.ceac.v2.GameReviewResponse', { result: { case: resultCase, value } });
}
