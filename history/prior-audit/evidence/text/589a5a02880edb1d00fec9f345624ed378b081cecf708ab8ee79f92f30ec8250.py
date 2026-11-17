from pathlib import Path
import json,csv
p=Path('/home/user');d=p/'research/refinement'
t=json.loads((d/'target.json').read_text());b=json.loads((d/'results/baseline.json').read_text());h=json.loads((d/'results/comparison-human.json').read_text());c=json.loads((d/'results/comparison-control.json').read_text())
labels={1:'Book',2:'Brilliant',3:'Great',4:'Best',5:'Excellent',6:'Good',7:'Inaccuracy',8:'Mistake',9:'Blunder',10:'Miss',11:'Forced',20:'Tricky'}
def pair(x,dec=False):return ' / '.join(f'{x[k]:.1f}' if dec else str(x[k]) for k in ['white','black'])
rows=[['Accuracy (%)',pair(t['accuracy'],True),pair(b['actual']['accuracy'],True),pair(h['actual']['accuracy'],True)],['Game Rating',pair(t['ratings']),pair(b['actual']['ratings']),pair(h['actual']['ratings'])]]
for i in [2,3,1,4,5,6,7,8,10,9]:
 rows.append([labels[i]]+[' / '.join(str(x['tallies'][col].get(str(i),0)) for col in ['white','black']) for x in [t,b['actual'],h['actual']]])
header=['Metric (White / Black)','Chess.com reference','Working extension v0.1.7','Local Torch human mode (experimental)']
def tab(head,rs):return '| '+' | '.join(head)+' |\n| '+' | '.join(['---']*len(head))+' |\n'+'\n'.join('| '+' | '.join(r)+' |' for r in rs)
sans='d4 d5 e4 dxe4 Be2 Nf6 Qd3 exd3 cxd3 Nc6 Bh5 Nxd4 Bd2 Nc2+ Kf1 Nxa1 Bc1 Qxd3+ Ke1 Nc2#'.split();mv=[]
for i,(bm,hm) in enumerate(zip(b['gameReview']['review']['playedMoves'],h['gameReview']['review']['playedMoves'])):
 mv.append([str(i//2+1)+('.' if i%2==0 else '...'),sans[i],labels.get(bm['playedMove'].get('moveClassification'),'Other'),labels.get(hm['playedMove'].get('moveClassification'),'Other')])
text='''# Reference-game comparison: Chess.com, extension, local Torch human mode

Game: [PUBLIC_PLAYER_HANDLE_REDACTED] (White) vs [PUBLIC_PLAYER_HANDLE_REDACTED] (Black), live game 186934806892, 20 plies, 0–1. This is the original reference, not the newer example link used for source inspection.

All paired values below are **White / Black**. Chess.com figures are the user's supplied reference, not newly fetched scores. Extension figures are the saved working v0.1.7 baseline. The human-mode column is a newly executed, research-only pipeline using native engine outputs.

'''+tab(header,rows)+'''

## What this experiment verifies
- Native GetGameReviewEvaluations feature79 with Fast strength and torchSearchMode.human was run at each of 21 game points (initial position plus 20 plies).
- All 21 calls completed with progress=1. The logs contain 20 human PV-tree searches (the terminal position needs no search), as well as auxiliary ordinary searches.
- Returned evaluations were added through the native AddEvaluations API, and native GameReview feature42 generated the accuracy, ratings and classifications above.
- No additional engine-search commands were recorded during that final review-generation step. No fetch attempts or warnings were recorded. Local WASM execution used its Node wrapper; this was not an installed Chrome integration test.
- Normalize/Hash tuning from the earlier sweep was NOT applied. The production extension was not modified.

## Important limits
This demonstrates a complete local experimental review built after human-mode evaluation, not parity with Chess.com's server-side Torch Human setup. Human-mode search logs use the internal default **rating 2100**; that has not been established as the server's configuration for this game. Underlying evaluation metadata remains engine11.

A matched research control (the same explicit per-position preload pipeline without human mode) returned accuracy '''+pair(c['actual']['accuracy'],True)+''' and ratings '''+pair(c['actual']['ratings'])+'''. It differs slightly from the direct production baseline. Therefore the human column versus production is a pipeline comparison, not a perfectly isolated one-setting benchmark. Relative to the matched control, human mode also moves both accuracy figures farther from the supplied reference.

**Conclusion:** This local human-mode configuration does not improve the reference match. Keep v0.1.7 unchanged.

## Move-by-move local classifications
The supplied Chess.com reference contains aggregate counts, not a classification for each individual move, so no per-move Chess.com labels are invented here.

'''+tab(['Move','Played','Working extension','Local human-mode experiment'],mv)+'''

## Raw evidence
- research/refinement/results/comparison-human.json
- research/refinement/results/comparison-control.json
- research/refinement/results/baseline.json
- research/refinement/comparison-trial.mjs
- research/refinement/configs/comparison-human.json
- research/refinement/target.json
'''
(p/'torch-human-comparison.md').write_text(text)
with (p/'torch-human-comparison.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(header);w.writerows(rows)
print(tab(header,rows));print('\n'+tab(['Move','Played','Extension','Human experiment'],mv))
