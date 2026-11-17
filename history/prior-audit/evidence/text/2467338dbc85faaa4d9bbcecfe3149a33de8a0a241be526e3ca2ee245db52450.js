// Thin UCI driver around chess.com's own engine loaders.
//
// Chess.com creates its workers as  new Worker(loader + '#' + engineUrl)
// (shared.eager.BOGLllgUUR.chunk.js, function u()).  The loaders read
// self.location.hash to locate the .wasm, and the stockfish build resolves
// its NNUE net relative to the worker script — so the packed files must sit
// next to the loader, which they do.

const RUNTIME = (typeof chrome !== 'undefined' && chrome.runtime) ? chrome.runtime : null;
export const asset = (p) => (RUNTIME ? RUNTIME.getURL(p) : new URL('../' + p, import.meta.url).href);

export const ENGINE_PRESETS = {
  'stockfish-nnue-16': {
    label: 'Stockfish 16.1 NNUE (chess.com)',
    loader: 'engines/stockfish/stockfish-nnue-16-single.js',
    wasm: 'engines/stockfish/stockfish-nnue-16-single.wasm',
    evalFile: 'engines/stockfish/nn-5af11540bbfe.nnue',
    init: ['setoption name Use NNUE value true', 'setoption name Threads value 1', 'setoption name Hash value 64'],
    enumValue: 10, // chesscom.engine.v1.Engine.ENGINE_SF16_1_NNUE
  },
  torch: {
    label: 'Torch 2 (chess.com)',
    loader: 'engines/torch/torch-2-single.js',
    wasm: 'engines/torch/torch-2-single.wasm',
    init: ['setoption name Threads value 1', 'setoption name Hash value 64'],
    enumValue: 11, // ENGINE_TORCH_3
  },
  'torch-lite': {
    label: 'Torch 2 Lite (chess.com)',
    loader: 'engines/torch-lite/torch-2-lite-single.js',
    wasm: 'engines/torch-lite/torch-2-lite-single.wasm',
    init: ['setoption name Threads value 1', 'setoption name Hash value 64'],
    enumValue: 11,
  },
};

export class UciEngine {
  constructor(presetKey = 'stockfish-nnue-16') {
    const p = ENGINE_PRESETS[presetKey];
    if (!p) throw new Error('unknown engine preset ' + presetKey);
    this.preset = p;
    this.key = presetKey;
    this.lines = [];
    this.bestmove = null;
    this._waiters = [];
    this.ready = this._boot();
  }

  async _boot() {
    const url = asset(this.preset.loader) + '#' + asset(this.preset.wasm);
    this.worker = new Worker(url);
    this.worker.onmessage = (ev) => this._onLine(String(ev.data));
    this.worker.onerror = (e) => {
      const err = new Error('engine worker error: ' + (e && e.message));
      this._fail(err);
    };
    await this.send('uci', 'uciok', 30000);
    // Exactly the option set chess.com's client sends (shared.eager iP catalog).
    for (const cmd of this.preset.init) this.worker.postMessage(cmd);
    await this.send('isready', 'readyok', 30000);
    this.worker.postMessage('ucinewgame');
    return true;
  }

  _onLine(line) {
    if (!line) return;
    for (const w of this._waiters) {
      if (line === w.expect) { w.resolve(line); w.done = true; }
    }
    this._waiters = this._waiters.filter((w) => !w.done);
    if (line.startsWith('info ')) {
      const m = /multipv (\d+)/.exec(line);
      const depth = /depth (\d+)/.exec(line);
      const scoreCp = /score cp (-?\d+)/.exec(line);
      const scoreMate = /score mate (-?\d+)/.exec(line);
      const pv = / pv (.+)$/.exec(line);
      const seldepth = /seldepth (\d+)/.exec(line);
      if (scoreCp || scoreMate) {
        const multipv = m ? Number(m[1]) : 1;
        const entry = {
          multipv,
          depth: depth ? Number(depth[1]) : 0,
          seldepth: seldepth ? Number(seldepth[1]) : 0,
          cp: scoreCp ? Number(scoreCp[1]) : null,
          mate: scoreMate ? Number(scoreMate[1]) : null,
          pv: pv ? pv[1].trim().split(/\s+/) : [],
        };
        const i = this.lines.findIndex((l) => l.multipv === multipv);
        if (i >= 0) this.lines[i] = entry; else this.lines.push(entry);
        this.lines.sort((a, b) => a.multipv - b.multipv);
      }
      return;
    }
    if (line.startsWith('bestmove ')) {
      this.bestmove = line.split(/\s+/)[1];
      for (const w of this._waiters) {
        if (w.expect === 'bestmove') { w.resolve(line); w.done = true; }
      }
      this._waiters = this._waiters.filter((w) => !w.done);
      if (this._onBest) this._onBest(this.bestmove);
    }
    for (const w of this._waiters) {
      if (w.match && w.match(line)) { w.resolve(line); w.done = true; }
    }
    this._waiters = this._waiters.filter((w) => !w.done);
  }

  _fail(err) {
    for (const w of this._waiters) { if (!w.done) { w.done = true; w.reject(err); } }
    this._waiters = [];
  }

  send(cmd, expect, timeout = 15000) {
    return new Promise((resolve, reject) => {
      const waiter = { expect, resolve, reject, done: false, match: null };
      if (expect) {
        this._waiters.push(waiter);
        setTimeout(() => {
          if (!waiter.done) {
            waiter.done = true;
            this._waiters = this._waiters.filter((w) => w !== waiter);
            reject(new Error(`timeout waiting for "${expect}" after "${cmd}"`));
          }
        }, timeout);
      }
      this.worker.postMessage(cmd);
      if (!expect) resolve(null);
    });
  }

  /**
   * Search a position.
   * @param {string} positionCmd  e.g. "position fen ... moves ..." or "position startpos moves ..."
   * @param {{depth:number, multipv?:number, movetime?:number}} opts
   * @returns {Promise<{lines:Array, bestmove:string}>}
   */
  async search(positionCmd, opts = {}) {
    const depth = opts.depth || 18;
    const multipv = Math.max(1, opts.multipv || 1);
    await this.ready;
    this.lines = [];
    this.bestmove = null;
    this.worker.postMessage(positionCmd);
    this.worker.postMessage(`setoption name MultiPV value ${multipv}`);
    const go = opts.movetime ? `go movetime ${opts.movetime}` : `go depth ${depth}`;
    const done = new Promise((resolve, reject) => {
      const t = setTimeout(() => reject(new Error('search timeout')), (opts.movetime || depth * 400) + 30000);
      this._onBest = () => { clearTimeout(t); this._onBest = null; resolve(); };
    });
    this.worker.postMessage(go);
    await done;
    return { lines: this.lines.slice(), bestmove: this.bestmove };
  }

  terminate() {
    try { this.worker.postMessage('quit'); } catch { /* ignore */ }
    setTimeout(() => { try { this.worker.terminate(); } catch { /* ignore */ } }, 300);
  }
}
