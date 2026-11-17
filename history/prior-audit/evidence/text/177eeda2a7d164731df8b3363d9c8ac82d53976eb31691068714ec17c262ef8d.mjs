// Node stand-in for the browser `Worker`, so the extension's engine driver can
// be exercised outside Chrome.  Loads chess.com's loaders exactly the way the
// browser would (CJS/UMD entry, double factory) and relays UCI lines back.

import { createRequire } from 'node:module';
import { fileURLToPath } from 'node:url';
import path from 'node:path';
import fs from 'node:fs';

const require = createRequire(import.meta.url);

export class NodeWorkerShim {
  constructor(url) {
    const [loaderUrl, hash] = String(url).split('#');
    const loaderPath = fileURLToPath(loaderUrl);
    const dir = path.dirname(loaderPath);
    let wasmPath = hash ? decodeURIComponent(hash) : '';
    if (wasmPath.startsWith('file:')) wasmPath = fileURLToPath(wasmPath);
    this.onmessage = null;
    this.onerror = null;
    this._ready = false;
    this._queue = [];
    this._boot(loaderPath, dir, wasmPath)
      .then(() => {
        this._ready = true;
        for (const cmd of this._queue.splice(0)) this._send(cmd);
      })
      .catch((e) => {
        console.error('[worker-shim] boot failed:', e);
        if (this.onerror) this.onerror({ message: String(e) });
      });
  }

  async _boot(loaderPath, dir, wasmPath) {
    const base = path.basename(loaderPath);

    if (base.startsWith('torch')) {
      const INIT = require(loaderPath);
      const Torch = typeof INIT === 'function' ? INIT() : INIT;
      const parts = [];
      for (let i = 0; i < 6; i++) {
        const p = path.join(dir, `torch-2-single-part-${i}.wasm`);
        if (fs.existsSync(p)) parts.push(fs.readFileSync(p));
      }
      const cfg = {
        locateFile: (n) => (n.endsWith('.wasm') ? wasmPath || path.join(dir, n) : path.join(dir, n)),
        print: () => {},
        printErr: (e) => console.error('[torch]', e),
      };
      if (parts.length) cfg.wasmBinary = Buffer.concat(parts);
      const mod = await Torch(cfg);
      // Torch routes UCI output through Module.listener (the browser worker
      // branch points it at postMessage).
      mod.listener = (line) => this._emit(line);
      mod.addMessageListener?.((line) => this._emit(line));
      this._sendFn = (c) => mod.ccall('command', null, ['string'], [c], { async: /^go\b/.test(c) });
      this._mod = mod;
      return;
    }

    const outer = require(loaderPath);
    const make = typeof outer === 'function' ? outer() : outer;
    const mod = await make({
      locateFile: (n) => {
        if (n.endsWith('.wasm')) return wasmPath || path.join(dir, n);
        return path.join(dir, n);
      },
      print: () => {},
      printErr: (e) => console.error('[sf]', e),
    });
    mod.addMessageListener?.((line) => this._emit(line));
    this._sendFn = (c) => mod.onCustomMessage(c);
    this._mod = mod;
    // In Node the net must be pointed at explicitly; the browser build
    // resolves it next to the worker script the way chess.com's own page does.
    const nnue = path.join(dir, 'nn-5af11540bbfe.nnue');
    if (fs.existsSync(nnue)) mod.onCustomMessage(`setoption name EvalFile value ${nnue}`);
  }

  _emit(line) {
    if (this.onmessage) this.onmessage({ data: line });
  }

  _send(cmd) {
    let c = String(cmd);
    // The extension hands out file:// URLs in Node; the engine wants paths.
    const m = /^(setoption name \S+ value )(.+)$/.exec(c);
    if (m && m[2].startsWith('file:')) c = m[1] + fileURLToPath(m[2]);
    try { this._sendFn(c); } catch (e) { console.error('[worker-shim] send', e); }
  }

  postMessage(cmd) {
    if (this._ready) this._send(cmd);
    else this._queue.push(cmd);
  }

  terminate() {
    try { this._sendFn('quit'); } catch { /* ignore */ }
  }
}
