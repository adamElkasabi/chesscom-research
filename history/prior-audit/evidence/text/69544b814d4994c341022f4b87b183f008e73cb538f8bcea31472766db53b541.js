// Sequential binary-interface client for Chess.com's bundled CEE worker.
// The shipped protocol has no request IDs. Never overlap API calls: progress,
// API logs, and UCI text are notifications, not replies to the next call.
import { encodeMessage, decodeMessage } from './protobuf.js';

const NS = '.chesscom.explanation_engine.v1.';
function asset(path) {
  return globalThis.chrome?.runtime?.getURL
    ? chrome.runtime.getURL(path)
    : new URL('../' + path, import.meta.url).href;
}

export class CeeClient {
  constructor({ workerFactory = url => new Worker(url), onLog = () => {}, timeoutMs = 240000 } = {}) {
    this.onLog = onLog;
    this.timeoutMs = timeoutMs;
    this.tail = Promise.resolve();
    this.pending = null;
    this.closed = false;
    this.worker = workerFactory(asset('engines/cee/explanation-engine.js') + '#' + asset('engines/cee/explanation-engine.wasm'));
    this.worker.onmessage = event => this.receive(event.data);
    this.worker.onerror = event => this.fail(new Error('CEE worker: ' + (event.message || 'failed')));
    this.worker.onmessageerror = () => this.fail(new Error('CEE worker response could not be decoded'));
  }

  receive(message) {
    if (typeof message === 'string') {
      if (this.pending?.call === 'UCI' && message.trim() === 'readyok') this.settle(null, true);
      return; // Other UCI text, banners and API_LOG are notifications.
    }
    if (!message || typeof message !== 'object') return;
    if (message.error) {
      const error = new Error(String(message.error));
      if (this.pending) this.settle(error);
      else this.onLog(error.message);
      return;
    }
    const pending = this.pending;
    if (!pending) return;
    if (pending.call === 'CEE_Run') {
      if (message.proto != null) {
        pending.onUpdate?.(message.proto, !!message.is_final);
        if (message.is_final) this.settle(null, message.proto);
      }
      return;
    }
    if (Object.hasOwn(message, 'retval')) this.settle(null, message.retval);
    else if (message.call === pending.call + '_done') this.settle(null, message);
  }

  settle(error, value) {
    const pending = this.pending;
    if (!pending) return;
    this.pending = null;
    clearTimeout(pending.timer);
    if (error) pending.reject(error); else pending.resolve(value);
  }

  fail(error) {
    this.closed = true;
    this.failure = error;
    this.settle(error);
    this.worker?.terminate();
  }

  call(call, args = [], onUpdate) {
    const task = this.tail.then(() => {
      if (this.closed) throw this.failure || new Error('CEE client disposed');
      return new Promise((resolve, reject) => {
        const timer = setTimeout(() => this.fail(new Error(call + ' timed out')), this.timeoutMs);
        this.pending = { call, resolve, reject, timer, onUpdate };
        try {
          if (call === 'UCI') {
            this.worker.postMessage(args[0]);
            this.worker.postMessage('isready'); // ordered acknowledgment barrier
          } else this.worker.postMessage({ call, args });
        }
        catch (error) { this.fail(error); }
      });
    });
    this.tail = task.catch(() => {});
    return task;
  }

  // A UCI option is not an API call and has no retval. Serialize it with an
  // isready/readyok barrier so a late UCI line cannot steal a protobuf reply.
  command(command) {
    if (typeof command !== 'string' || /[\r\n]/.test(command)) throw new Error('Expected one UCI command');
    return this.call('UCI', [command]);
  }

  async feature(gamePoint, id, name, request = {}, onUpdate) {
    const type = name.startsWith('.') ? name : NS + name;
    const handle = await this.call('CEE_NewFeature', [gamePoint, id, encodeMessage(type, request)]);
    try {
      const bytes = await this.call('CEE_Run', [handle], onUpdate);
      return decodeMessage(type.replace(/Request$/, 'Response'), bytes);
    } finally {
      if (!this.closed) await this.call('CEE_DisposeFeature', [handle]);
    }
  }

  dispose() {
    this.fail(new Error('CEE client disposed'));
  }
}
