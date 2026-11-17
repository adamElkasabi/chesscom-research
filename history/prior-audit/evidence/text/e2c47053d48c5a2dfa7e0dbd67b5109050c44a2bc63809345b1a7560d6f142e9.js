// Presentation-only duration estimator. Never used to calculate review scores.
// No fabricated first-run timing: only successful reviews on this device train it.
const MAX_SAMPLES = 40;
const valid = s => s && Number.isInteger(s.plies) && s.plies >= 1 &&
  typeof s.searchKey === 'string' && s.searchKey.length < 1000 &&
  Number.isFinite(s.durationMs) && s.durationMs > 0 && s.durationMs < 3600000;

export class ReviewProgressEstimator {
  constructor(samples = []) {
    this.samples = (Array.isArray(samples) ? samples : []).filter(valid).slice(-MAX_SAMPLES);
    this.active = null;
  }

  begin({ plies, searchKey }, now) {
    const matches = this.samples.filter(s => s.searchKey === searchKey)
      .map(s => ({ ...s, distance: Math.abs(Math.log((plies + 1) / (s.plies + 1))) }))
      .sort((a, b) => a.distance - b.distance).slice(0, 7);
    // Scale by number of positions; use the median to resist unusually slow runs.
    const predictions = matches.map(s => s.durationMs * (plies + 1) / (s.plies + 1)).sort((a,b) => a-b);
    const mid = Math.floor(predictions.length / 2);
    const expectedMs = predictions.length ? (predictions.length % 2 ? predictions[mid] :
      (predictions[mid - 1] + predictions[mid]) / 2) : null;
    this.active = { plies, searchKey, startedAt: now, expectedMs, sampleCount: matches.length };
    return { expectedMs, sampleCount: matches.length };
  }

  progress(now) {
    if (!this.active?.expectedMs) return null;
    const elapsed = Math.max(0, now - this.active.startedAt);
    // Reserve completion for the actual result. If late, hold at 95%, not 100%.
    return Math.min(0.95, 0.02 + 0.93 * elapsed / this.active.expectedMs);
  }

  complete(now) {
    if (!this.active) return null;
    const { plies, searchKey, startedAt } = this.active;
    const sample = { plies, searchKey, durationMs: now - startedAt };
    this.active = null;
    if (!valid(sample)) return null;
    this.samples.push(sample);
    this.samples = this.samples.slice(-MAX_SAMPLES);
    return sample;
  }

  cancel() { this.active = null; }
}
