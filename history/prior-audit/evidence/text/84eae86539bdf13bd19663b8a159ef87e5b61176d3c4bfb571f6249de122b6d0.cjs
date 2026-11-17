// Node equivalent of the CEE script's browser Worker entry point.
const { parentPort, workerData } = require('node:worker_threads');
console.log = console.info = console.debug = console.warn = () => {};
// No API_LOG dump: logs can contain the entire PGN/player metadata.
console.error = () => {};
globalThis.postMessage = message => parentPort.postMessage(message);
const make = require(workerData.loader);
const engine = make(workerData.wasm);
engine.onmessage = message => parentPort.postMessage(message);
parentPort.on('message', message => {
  try {
    const result = engine.postMessage(message, false, true);
    if (result?.catch) result.catch(error => parentPort.postMessage({ error: String(error) }));
  } catch (error) { parentPort.postMessage({ error: String(error) }); }
});
