import { Worker } from 'node:worker_threads';
import { fileURLToPath } from 'node:url';

export function ceeWorkerFactory(url) {
  const [loader, wasm] = String(url).split('#');
  const thread = new Worker(new URL('./cee-worker.cjs', import.meta.url), {
    workerData: { loader: fileURLToPath(loader), wasm: fileURLToPath(wasm) },
    execArgv: [],
  });
  const shim = {
    onmessage: null, onerror: null,
    postMessage(message) { thread.postMessage(message); },
    terminate() { return thread.terminate(); },
  };
  thread.on('message', data => shim.onmessage?.({ data }));
  thread.on('error', error => shim.onerror?.({ message: error.message }));
  return shim;
}
