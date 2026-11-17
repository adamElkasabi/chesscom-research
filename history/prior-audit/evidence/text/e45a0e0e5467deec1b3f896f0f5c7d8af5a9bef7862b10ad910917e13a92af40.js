// Chess.com's own client-side maths, transcribed from the shipped bundle
// (shared.eager.BOGLllgUUR.chunk.js).  These are the only analysis numbers the
// browser itself computes — everything else in a Game Review comes from the
// server.  See PREMIUM-ANALYSIS.md §7.2 and REVERSE-ENGINEERING.md §2.

/* --- evaluation bar / score helpers (RE §2) ------------------------- */

export const SCORE_CALC_COEFFICIENT = 45;
export const SCORE_CAP = 4;

export const clampScore = (e = 0) => (e === null ? e : Math.max(-4, Math.min(4, e)));
export const clamp01 = (x) => Math.max(0, Math.min(1, x));

/** score (pawns, white POV) -> 0..100 bar percentage */
export function scoreToPercent(score) {
  const t = clampScore(score ?? null);
  if (t === null) return 50;
  if (t > 0) return 50 + (t * SCORE_CALC_COEFFICIENT) / 4;
  if (t < 0) return 50 - (Math.abs(t) * SCORE_CALC_COEFFICIENT) / 4;
  return 50;
}

/** centipawns / mate -> pawns, white POV, same as the bundle's zU() */
const CP_PER_PAWN = 100;
const MATE_SCORE = 1000;
export function scoreToPawns(score) {
  if (!score) return 0;
  if (typeof score.mateInWhite === 'number' && score.mateInWhite !== 0) {
    return score.mateInWhite > 0 ? MATE_SCORE : -MATE_SCORE;
  }
  if (typeof score.mateInBlack === 'number' && score.mateInBlack !== 0) {
    return score.mateInBlack > 0 ? -MATE_SCORE : MATE_SCORE;
  }
  if (typeof score.scoreCentipawnsWhite === 'number') return score.scoreCentipawnsWhite / CP_PER_PAWN;
  return 0;
}

/* --- rating -> win/draw/loss model (PA §7.2) ------------------------ */

export function wdl(whiteElo, blackElo) {
  const e = whiteElo / 100, t = blackElo / 100;
  const w = clamp01(
    0.20773843 * Math.atan(2.49085889 * e - 2.47841945 * t) +
      0.02262979 * e - 0.02256839 * t + 0.52239679
  );
  const l = clamp01(
    -0.20720905 * Math.atan(2.49626837 * e - 2.48220286 * t) -
      0.02352551 * e + 0.02172627 * t + 0.49443923
  );
  const d = clamp01(
    Math.exp(0.037043456 * e + 0.178106427 * t - 8.069742932) +
      0.004823544 * Math.exp(-1.364136591 * (e - t) ** 2) -
      0.001625539
  );
  const s = w + l + d;
  return { w: w / s, b: l / s, d: d / s };
}

/* --- rating-scaled confidence bands (PA §7.2) ----------------------- */

const BANDS_WHITE = { Winning: 0.2, Better: 0.4, Equal: 0.5, Worse: 0.65, Losing: 0.8 };
const BANDS_BLACK = { Winning: 0.8, Better: 0.65, Equal: 0.5, Worse: 0.4, Losing: 0.2 };
const DEFAULT_RATING = 2000;

export function evalThreshold(probability, rating) {
  return Math.log(1 / probability - 1) / (0.004 * ((0.0685 * rating - 12) / 100)) / 100;
}

/** Classify an evaluation (pawns, white POV) into a band for `color`. */
export function evalBand(scorePawns, color, rating = DEFAULT_RATING) {
  const table = color === 'b' ? BANDS_BLACK : BANDS_WHITE;
  const r = Math.max(800, Math.min(3200, rating || DEFAULT_RATING));
  const bands = ['Winning', 'Better', 'Equal', 'Worse', 'Losing'];
  const values = bands.map((b) => evalThreshold(table[b], r));
  // `Winning` threshold is the most favourable; walk down the list.
  const signed = color === 'b' ? -scorePawns : scorePawns;
  if (signed >= values[0]) return 'Winning';
  if (signed >= values[1]) return 'Better';
  if (signed >= values[2]) return 'Equal';
  if (signed >= values[3]) return 'Worse';
  return 'Losing';
}

/** The 10 downgrade keys that have a sentence in the bundle. */
export const DOWNGRADES = [
  'WinningBetter', 'WinningEqual', 'WinningWorse', 'WinningLosing',
  'BetterEqual', 'BetterWorse', 'BetterLosing',
  'EqualWorse', 'EqualLosing', 'WorseLosing',
];

export function downgradeKey(playedBand, bestBand) {
  const key = `${playedBand}${bestBand}`;
  return DOWNGRADES.includes(key) ? key : null;
}
