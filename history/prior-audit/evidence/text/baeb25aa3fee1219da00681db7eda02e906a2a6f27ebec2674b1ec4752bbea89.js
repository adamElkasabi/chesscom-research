// Minimal chess board: parse/build FEN, apply coordinate moves.
// Enough to walk a game and produce the FENs the GameReview payload needs.
// Move legality is never re-checked here — the moves come from a real game
// (or from the engine), so this only has to update state correctly.

export const START_FEN = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1';

const FILES = 'abcdefgh';
export const COLOR = { WHITE: 'w', BLACK: 'b' };
const TYPE_TO_LETTER = { pawn: 'p', knight: 'n', bishop: 'b', rook: 'r', queen: 'q', king: 'k' };
const LETTER_TO_TYPE = { p: 'pawn', n: 'knight', b: 'bishop', r: 'rook', q: 'queen', k: 'king' };

// chess.com Square enum: SQUARE_A1 = 1 ... SQUARE_H8 = 64
export function squareEnumToAlg(enumValue) {
  const i = Number(enumValue) - 1;
  if (!(i >= 0 && i < 64)) return null;
  return FILES[i % 8] + (Math.floor(i / 8) + 1);
}
export function algToSquareEnum(alg) {
  const f = FILES.indexOf(alg[0]);
  const r = Number(alg[1]) - 1;
  if (f < 0 || r < 0 || r > 7) return 0;
  return r * 8 + f + 1;
}

export class Board {
  constructor(fen = START_FEN) {
    this.load(fen);
  }

  load(fen) {
    const [placement, turn, castling, ep, half, full] = fen.trim().split(/\s+/);
    this.grid = new Array(64).fill(null);
    let idx = 56; // a8
    for (const ch of placement) {
      if (ch === '/') { idx -= 16; continue; }
      if (ch >= '1' && ch <= '8') { idx += Number(ch); continue; }
      const lower = ch.toLowerCase();
      this.grid[idx] = { color: ch === lower ? 'b' : 'w', type: LETTER_TO_TYPE[lower] };
      idx++;
    }
    this.turn = turn === 'b' ? 'b' : 'w';
    this.castling = new Set((castling && castling !== '-' ? castling : '').split('').filter(Boolean));
    this.ep = ep && ep !== '-' ? ep : null;
    this.halfmove = Number(half || 0);
    this.fullmove = Number(full || 1);
  }

  fen() {
    const rows = [];
    for (let r = 7; r >= 0; r--) {
      let row = '', empty = 0;
      for (let f = 0; f < 8; f++) {
        const p = this.grid[r * 8 + f];
        if (!p) { empty++; continue; }
        if (empty) { row += empty; empty = 0; }
        const letter = TYPE_TO_LETTER[p.type];
        row += p.color === 'w' ? letter.toUpperCase() : letter;
      }
      if (empty) row += empty;
      rows.push(row);
    }
    const castling = ['K', 'Q', 'k', 'q'].filter((c) => this.castling.has(c)).join('') || '-';
    return `${rows.join('/')} ${this.turn} ${castling} ${this.ep || '-'} ${this.halfmove} ${this.fullmove}`;
  }

  index(alg) {
    return FILES.indexOf(alg[0]) + (Number(alg[1]) - 1) * 8;
  }

  pieceAt(alg) { return this.grid[this.index(alg)]; }

  /** Apply a UCI move such as "e2e4", "e7e8q". Returns this. */
  apply(uci) {
    const from = uci.slice(0, 2), to = uci.slice(2, 4);
    const promo = uci[4] || null;
    const fi = this.index(from), ti = this.index(to);
    const moving = this.grid[fi];
    if (!moving) throw new Error(`no piece on ${from} for ${uci}`);
    const isPawn = moving.type === 'pawn';
    const isKing = moving.type === 'king';
    const capture = this.grid[ti] !== null;

    // en passant capture
    if (isPawn && !capture && this.ep && to === this.ep) {
      const capIdx = this.index(this.ep) + (moving.color === 'w' ? -8 : 8);
      this.grid[capIdx] = null;
    }

    // castling: king moves two files
    if (isKing && Math.abs(FILES.indexOf(to[0]) - FILES.indexOf(from[0])) === 2) {
      const rank = from[1];
      const kingSide = to[0] === 'g';
      const rookFrom = (kingSide ? 'h' : 'a') + rank;
      const rookTo = (kingSide ? 'f' : 'd') + rank;
      this.grid[this.index(rookTo)] = this.grid[this.index(rookFrom)];
      this.grid[this.index(rookFrom)] = null;
      this.castling.delete(moving.color === 'w' ? 'K' : 'k');
      this.castling.delete(moving.color === 'w' ? 'Q' : 'q');
    }

    this.grid[ti] = this.grid[fi];
    this.grid[fi] = null;
    if (promo) this.grid[ti] = { color: moving.color, type: LETTER_TO_TYPE[promo] };

    // castling rights bookkeeping
    if (isKing) {
      this.castling.delete('K'); this.castling.delete('Q');
      this.castling.delete('k'); this.castling.delete('q');
    }
    if (moving.type === 'rook') {
      if (from === 'a1') this.castling.delete('Q');
      if (from === 'h1') this.castling.delete('K');
      if (from === 'a8') this.castling.delete('q');
      if (from === 'h8') this.castling.delete('k');
    }
    if (to === 'a1') this.castling.delete('Q');
    if (to === 'h1') this.castling.delete('K');
    if (to === 'a8') this.castling.delete('q');
    if (to === 'h8') this.castling.delete('k');

    // en passant target
    this.ep = null;
    if (isPawn && Math.abs(Number(to[1]) - Number(from[1])) === 2) {
      this.ep = from[0] + (Number(from[1]) + (moving.color === 'w' ? 1 : -1));
    }

    this.halfmove = (isPawn || capture) ? 0 : this.halfmove + 1;
    if (this.turn === 'b') this.fullmove++;
    this.turn = this.turn === 'w' ? 'b' : 'w';
    return this;
  }

  clone() {
    const b = new Board(this.fen());
    return b;
  }

  /** Sum of material in pawns, from white's point of view. */
  materialBalance() {
    const VAL = { pawn: 1, knight: 3, bishop: 3, rook: 5, queen: 9, king: 0 };
    let m = 0;
    for (const p of this.grid) {
      if (!p) continue;
      m += (p.color === 'w' ? 1 : -1) * VAL[p.type];
    }
    return m;
  }
}

/** Walk a FEN + UCI move list, returning the FEN before every move and the final FEN. */
export function walk(startFen, uciMoves) {
  const board = new Board(startFen || START_FEN);
  const fens = [board.fen()];
  const uci = [];
  for (const m of uciMoves) {
    board.apply(m);
    uci.push(m);
    fens.push(board.fen());
  }
  return { fens, uci, finalFen: board.fen() };
}

/** Build FEN from a decoded chesscom.chess.v1.Position message. */
export function positionMessageToFen(pos) {
  if (!pos) return START_FEN;
  const grid = new Array(64).fill(null);
  const colorName = (c) => (Number(c) === 2 ? 'b' : 'w');
  const typeName = (t) => ({ 1: 'pawn', 2: 'knight', 3: 'bishop', 4: 'rook', 5: 'queen', 6: 'king' })[Number(t)] || null;
  for (const pl of pos.pieces || []) {
    const sq = squareEnumToAlg(pl.square);
    const type = typeName(pl.piece && pl.piece.type);
    if (!sq || !type) continue;
    const i = FILES.indexOf(sq[0]) + (Number(sq[1]) - 1) * 8;
    grid[i] = { color: colorName(pl.piece.color), type };
  }
  const turn = Number(pos.activeColor) === 2 ? 'b' : 'w';
  const rights = new Set();
  for (const cr of pos.castlingRights || []) {
    const fileIdx = Number(cr.rookFile) || 0;
    const file = FILES[fileIdx - 1];
    if (!file) continue;
    const white = Number(cr.color) !== 2;
    if (white) rights.add(file === 'h' ? 'K' : 'Q');
    else rights.add(file === 'h' ? 'k' : 'q');
  }
  let ep = null;
  if (pos.enPassantSquare) ep = squareEnumToAlg(pos.enPassantSquare);

  const rows = [];
  for (let r = 7; r >= 0; r--) {
    let row = '', empty = 0;
    for (let f = 0; f < 8; f++) {
      const p = grid[r * 8 + f];
      if (!p) { empty++; continue; }
      if (empty) { row += empty; empty = 0; }
      const letter = TYPE_TO_LETTER[p.type];
      row += p.color === 'w' ? letter.toUpperCase() : letter;
    }
    if (empty) row += empty;
    rows.push(row);
  }
  const castling = ['K', 'Q', 'k', 'q'].filter((c) => rights.has(c)).join('') || '-';
  return `${rows.join('/')} ${turn} ${castling} ${ep || '-'} ${Number(pos.halfmoveClock || 0)} ${Number(pos.fullmoveNumber || 1)}`;
}

/** Material balance in pawns (white positive) for a FEN. */
export function materialOfFen(fen) {
  return new Board(fen).materialBalance();
}

/* --------------------------------------------------------------- SAN / PGN */

function pathClear(board, fi, ti, sr, sf) {
  let k = fi + 8 * sr + sf;
  let guard = 0;
  while (k !== ti) {
    if (k < 0 || k > 63 || board.grid[k] || ++guard > 12) return false;
    k += 8 * sr + sf;
  }
  return true;
}

function reachable(board, piece, fi, ti) {
  const fr = Math.floor(fi / 8), ff = fi % 8;
  const dr = Math.floor(ti / 8) - fr, df = (ti % 8) - ff;
  const ar = Math.abs(dr), af = Math.abs(df);
  const t = piece.type;
  if (t === 'pawn') {
    const dir = piece.color === 'w' ? 1 : -1;
    if (df === 0 && dr === dir && !board.grid[ti]) return true;
    if (df === 0 && dr === 2 * dir && fr === (piece.color === 'w' ? 1 : 6)
      && !board.grid[fi + 8 * dir] && !board.grid[ti]) return true;
    if (af === 1 && dr === dir) return true; // capture (or en passant)
    return false;
  }
  if (t === 'king') return ar <= 1 && af <= 1;
  if (t === 'knight') return (ar === 2 && af === 1) || (ar === 1 && af === 2);
  const sr = Math.sign(dr), sf = Math.sign(df);
  if (t === 'bishop') return ar === af && ar > 0 && pathClear(board, fi, ti, sr, sf);
  if (t === 'rook') return (dr === 0 || df === 0) && (ar + af > 0) && pathClear(board, fi, ti, sr, sf);
  if (t === 'queen') {
    const ok = ar === af ? ar > 0 : (dr === 0 || df === 0);
    return ok && (ar + af > 0) && pathClear(board, fi, ti, sr, sf);
  }
  return false;
}

/** Convert one SAN token to UCI for the side to move. Returns null on failure. */
export function sanToUci(board, san) {
  const turn = board.turn;
  let s = String(san).replace(/[+#!?]/g, '').replace(/e\.p\.$/, '');
  if (!s || /^(1-0|0-1|1\/2-1\/2|\*)$/.test(s)) return null;

  const rank = turn === 'w' ? '1' : '8';
  if (/^(O-O-O|0-0-0)$/.test(s)) return `e${rank}c${rank}`;
  if (/^(O-O|0-0)$/.test(s)) return `e${rank}g${rank}`;

  let promo = null;
  const pm = /=([NBRQnbrq])$/.exec(s);
  if (pm) { promo = pm[1].toLowerCase(); s = s.slice(0, -pm[0].length); }

  const dest = s.slice(-2);
  if (!/^[a-h][1-8]$/.test(dest)) return null;
  s = s.slice(0, -2).replace(/x/g, '');

  let type = 'pawn';
  const SAN_TYPE = { N: 'knight', B: 'bishop', R: 'rook', Q: 'queen', K: 'king' };
  if (SAN_TYPE[s[0]]) { type = SAN_TYPE[s[0]]; s = s.slice(1); }
  const dis = s;
  const wantFile = /[a-h]/.test(dis) ? dis.match(/[a-h]/)[0] : null;
  const wantRank = /[1-8]/.test(dis) ? dis.match(/[1-8]/)[0] : null;

  const ti = FILES.indexOf(dest[0]) + (Number(dest[1]) - 1) * 8;

  for (let fi = 0; fi < 64; fi++) {
    const p = board.grid[fi];
    if (!p || p.color !== turn || p.type !== type) continue;
    if (wantFile && FILES[fi % 8] !== wantFile) continue;
    if (wantRank && String(Math.floor(fi / 8) + 1) !== wantRank) continue;
    if (board.grid[ti] && board.grid[ti].color === turn) continue;
    if (!reachable(board, p, fi, ti)) continue;
    const uci = FILES[fi % 8] + String(Math.floor(fi / 8) + 1) + dest + (promo || '');
    const probe = board.clone();
    try { probe.apply(uci); } catch { continue; }
    if (isInCheck(probe, turn)) continue;
    return uci;
  }
  return null;
}

export function isInCheck(board, color) {
  let king = -1;
  for (let i = 0; i < 64; i++) {
    const p = board.grid[i];
    if (p && p.color === color && p.type === 'king') { king = i; break; }
  }
  if (king < 0) return false;
  const enemy = color === 'w' ? 'b' : 'w';
  const kr = Math.floor(king / 8), kf = king % 8;
  for (let i = 0; i < 64; i++) {
    const p = board.grid[i];
    if (!p || p.color !== enemy) continue;
    const r = Math.floor(i / 8), f = i % 8;
    const dr = kr - r, df = kf - f;
    const ad = Math.abs(dr), af = Math.abs(df);
    if (p.type === 'n' && ((ad === 2 && af === 1) || (ad === 1 && af === 2))) return true;
    if (p.type === 'k' && ad <= 1 && af <= 1) return true;
    if (p.type === 'p' && ad === 1 && af === 1 && dr === (enemy === 'w' ? 1 : -1)) return true;
    const slide =
      (p.type === 'b' && ad === af && ad > 0) ||
      (p.type === 'r' && (dr === 0 || df === 0) && (ad + af > 0)) ||
      (p.type === 'q' && (ad === af || dr === 0 || df === 0) && (ad + af > 0));
    if (!slide) continue;
    const sr = Math.sign(dr), sf = Math.sign(df);
    let k = i + 8 * sr + sf;
    let blocked = false;
    while (k !== king) {
      if (board.grid[k]) { blocked = true; break; }
      const kr2 = Math.floor(k / 8), kf2 = k % 8;
      if (sr && Math.sign(kr2 - r) !== sr) { blocked = true; break; }
      if (sf && Math.sign(kf2 - f) !== sf) { blocked = true; break; }
      k += 8 * sr + sf;
      if (k < 0 || k > 63) { blocked = true; break; }
    }
    if (!blocked && k === king) return true;
  }
  return false;
}

/** Convert the movetext of a PGN into UCI moves. */
export function pgnToUci(pgn, startFen = START_FEN) {
  const sep = pgn.indexOf('\n\n');
  const body = sep >= 0 ? pgn.slice(sep + 2) : pgn;
  const board = new Board(startFen);
  const uci = [];
  const tokens = body
    .replace(/\{[^}]*\}/g, ' ')
    .replace(/;[^\n]*/g, ' ')
    .split(/\s+/)
    .filter(Boolean);
  for (const raw of tokens) {
    let tok = raw.replace(/^\d+\.(\.\.)?/, '');
    if (!tok || /^(1-0|0-1|1\/2-1\/2|\*)$/.test(tok) || /^\$\d+$/.test(tok)) continue;
    const m = sanToUci(board, tok);
    if (!m) break;
    board.apply(m);
    uci.push(m);
  }
  return uci;
}
