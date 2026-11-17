# Extended findings

[Master index](../00_MASTER_INDEX.md)

<a id="FND-30120"></a>
## FND-30120 — Implementation component outgoing-challenges

Vue compiled component __name declaration. Name suggests outgoing challenges; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0201
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
je(),j(),tc(),dP(),wP(),zn(),An(),St(),wi(),am(),EP(),MP(),im(),Iu(),Jr(),Sa(),PP(),el(),IP(),bc(),pd(),or(),Hs(),LP=K({__name:`outgoing-challenges`,setup(e){fh(()=>{FP()&&jP(),bh(()=>!xl()&&!Ou().length,e=>{e&&i()},{immediate:!0})}),dh(()=>{zt(),Mm(Vf.FIRST_GAME),FP()&&TP()});let t=pu({contextUser(){return Xt()},currentUser(){return At()},outgoingChallenges(){return _m()},outgoingOpponentUuids(){return this.outgoingChallenges.map(e=>e.getTo()?.getUserUuid()).filter(e=>!!e)},showSpeechMessage(){return Pp(Vf.FIRST_GAME)},useSeekPanel(){return FP()&&this.outgoingChallenges.length===1},initialCoachMessage(){return this.showSpeechMessage?k(`Welcome to your first live game. Win, lose, or draw, every chess game is a chance to learn!`):null},seekCoachTip(){return NP()}});function n(e){let t=e.getTo()?.getUserUuid();return t?o.value[t]??null:null}function r({challenge:e}){if(Kp({challenge:e,interfaceName:`New Game Sidebar`,elementName:`Cancel Seek Button`}),e.isPlaceholderChallengeModel()){Be();return}at(e)}function i(){zt(),Fa(v.Default)}function a(){Ia()}let o=XN(z(()=>t.outgoingOpponentUuids),Xm.PlayOutgoingChallenge);return(e,s)=>Z(t).useSeekPanel?(J(),B(CP,{key:0,"can-cancel-pending-challenge":Z(t).showS
```

<a id="FND-30121"></a>
## FND-30121 — Implementation component sidebar

Vue compiled component __name declaration. Name suggests sidebar; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0201
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
Du(),Lm(),yr(),Et(),JP(),Ge(),Zc(),Un(),rn(),XP(),vt(),Kd(),$o(),Tu(),co(),Hm(),QP(),sc(),eF(),Ma(),E(),dt(),nF(),rF=K({__name:`sidebar`,setup(e){let t=Ad(),n=mh(!1);fh(()=>{$P()&&document.querySelector(`.sidebar-component`)?.scrollIntoView(!0),s()});let r=pu({selectedTab(){return ia()},defaultSidebarTab(){return we()},isLiveCompetitionRoute(){return Hd(Ut())},newGameView(){return au()},activeBoard(){return ps()},dailyChallenge(){return ue(T.DailyChallenge)},dailyGame(){return ue(T.DailyGame)},liveGame(){return ue(T.Game)},dailyTeamMatchChallenge(){return Qc()},votechessChallenge(){return Hf()},teamMatchChallenge(){return sp()},arenaChallenge(){return tu()},tournament(){return Cs()},arena(){return Gu()},teamMatch(){return ud()},tabs(){let e=[];return this.dailyChallenge&&e.push({id:T.DailyChallenge,icon:Ft,label:k(`Daily`),closable:!0}),this.dailyGame&&e.push({id:T.DailyGame,icon:this.dailyGame.type===`chess960`?Cu:Ft,label:k(`Daily`),closable:!0}),this.isLoading&&this.defaultSidebarTab===T.Game?e.push({id:T.Game,icon:xf,label:k(`Game`),closable:!1}):this.liveGame&&e.push({id:T.Game,icon:os(this.liveGame.getGameIcon()),label:tF(Pi(this.liveGame),this.liveGame.isOver()),closable:!Pi(this.liveGame)||thi
```

<a id="FND-30122"></a>
## FND-30122 — Implementation component application

Vue compiled component __name declaration. Name suggests application; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0201
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
`tabs`])]),_:1},8,[`content`]))}})})),aF,oF=t((()=>{iF(),iF(),aF=rF})),sF,cF=t((()=>{kA(),qM(),oF(),_e(),GN(),_(),sF=K({__name:`application`,setup(t){let n=WN(),r=z(()=>ju()),i=ih(()=>h(()=>e(()=>import(`./lazy-controllers.779ba150.Za0kuf1nZt.chunk.js`),`./lazy-controllers.779ba150.Za0kuf1nZt.chunk.js`).then(e=>(e.t(),e.n)),__vite__mapDeps([0]),import.meta.url)),a=ih(()=>h(()=>e(()=>import(`./focus-mode-sidebar.8eca441b.DTeFPYY3Gi.chunk.js`),`./focus-mode-sidebar.8eca441b.DTeFPYY3Gi.chunk.js`).then(e=>(e.n(),e.t)),__vite__mapDeps([0,59,53,60]),import.meta.url));return(e,t)=>(J(),H(Qm,null,[(J(),B(eh,{to:`#board-controls`},[G(OA)])),t[1]||=W(),(J(),B(eh,{to:`#board-layout-player-top`},[G(KM,{position:`top`})])),t[2]||=W(),(J(),B(eh,{to:`#board-layout-player-bottom`},[G(KM,{position:`bottom`})])),t[3]||=W(),(J(),B(eh,{to:`#board-layout-sidebar`},[r.value?(J(),B(Z(a),{key:0})):V(``,!0),t[0]||=W(),r.value?V(``,!0):(J(),B(aF,{key:1}))])),t[4]||=W(),Z(n)?(J(),B(Z(i),{key:0})):V(``,!0)],64))}})})),lF,uF=t((()=>{cF(),cF(),lF=sF}));function dF(){Mi(lF).mount(document.createElement(`div`)),oA({onAfterInitControllers(){US()||VS()}})}var fF=t((()=>{HS(),WS(),Ot(),sA(),uF()})),pF,mF,hF,gF,_F,vF,yF,bF,xF,SF=t((()=>
```

<a id="FND-30123"></a>
## FND-30123 — Implementation component board-layout-main

Vue compiled component __name declaration. Name suggests board layout main; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0201
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
ss:`board-layout-player board-layout-bottom`},bF={key:2,id:`board-layout-analysis`,class:`board-layout-analysis`},xF=K({__name:`board-layout-main`,props:{withAnalysis:{type:Boolean},withControls:{type:Boolean},withEvaluation:{type:Boolean},withPieces:{type:Boolean},withPlayers:{type:Boolean}},setup(e){return(t,n)=>(J(),H(`div`,pF,[e.withPlayers?(J(),H(`div`,mF,[Y(t.$slots,`playerTop`)])):V(``,!0),n[4]||=W(),U(`div`,hF,[e.withEvaluation?(J(),H(`div`,gF,[Y(t.$slots,`evaluation`)])):V(``,!0),n[1]||=W(),e.withPieces?(J(),H(`div`,_F,[Y(t.$slots,`pieces`)])):V(``,!0),n[2]||=W(),Y(t.$slots,`chessboard`),n[3]||=W(),e.withControls?(J(),H(`div`,vF,[Y(t.$slots,`controls`),n[0]||=W(),G(Il,{class:q([t.$style[`resize-icon`],`board-layout-icon`,`resize`]),is:Z(Nt),variant:`glyph`,size:20},null,8,[`class`,`is`])])):V(``,!0)]),n[5]||=W(),e.withPlayers?(J(),H(`div`,yF,[Y(t.$slots,`playerBottom`)])):V(``,!0),n[6]||=W(),e.withAnalysis?(J(),H(`div`,bF,[Y(t.$slots,`analysis`)])):V(``,!0)]))}})})),CF,wF,TF=t((()=>{SF(),SF(),Zg(),C(),CF={$style:Xg},wF=S(xF,[[`__cssModules`,CF]])})),EF,DF,OF=t((()=>{EF={id:`board-layout-sidebar`,class:`board-layout-sidebar`},DF=K({__name:`board-layout-sidebar`,props:{withGameList:{type:Boolea
```

<a id="FND-30124"></a>
## FND-30124 — Implementation component board-layout-sidebar

Vue compiled component __name declaration. Name suggests board layout sidebar; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0201
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
g},wF=S(xF,[[`__cssModules`,CF]])})),EF,DF,OF=t((()=>{EF={id:`board-layout-sidebar`,class:`board-layout-sidebar`},DF=K({__name:`board-layout-sidebar`,props:{withGameList:{type:Boolean}},setup(e){return(t,n)=>(J(),H(`div`,EF,[e.withGameList?Y(t.$slots,`gameList`,{},void 0,void 0,0):V(``,!0),n[0]||=W(),Y(t.$slots,`sidebar`)]))}})})),kF,AF=t((()=>{OF(),OF(),kF=DF}));function jF({options:e,fen:t,id:n=`single`}){let r=qe({options:{boardStyle:e.boardStyle,pieceStyle:e.pieceStyle,themeAssets:e.themeAssets,animationType:e.animationType,flipped:e.flipped,enabled:e.enabled,coordinates:e.coordinates,allowMarkings:e.allowMarkings,id:n},init:{fen:t??vd()}}),i=MF(r.boardId);return{id:r.attrs.id,class:[`board`,r.attrs.class].join(` `),html:`<style id="${r.styleTagId}">${i}</style>${r.html}`,style:NF(r.attrs.style)}}function MF(e){let t=`
    #${e}, .fade-in-overlay {
      background-image: var(--theme-board-style-image, var(--fallback-theme-board-style-image));
    }
    .coordinate-light {
      fill: var(--theme-board-style-coordinate-color-dark, var(--fallback-theme-board-style-coordinate-color-dark));
    }
    .coordinate-dark {
      fill: var(--theme-board-style-coordinate-color-light, var(--fallback-theme-b
```

<a id="FND-30125"></a>
## FND-30125 — Implementation component chessboard-placeholder

Vue compiled component __name declaration. Name suggests chessboard placeholder; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0201
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
dexOf(`:`);return[e.slice(0,t).trim(),e.slice(t+1).trim()]}))}var PF=t((()=>{Aa(),Kl()})),FF,IF=t((()=>{PF(),Kl(),FF=K({__name:`chessboard-placeholder`,props:{options:{},fen:{default:vd()},id:{}},setup(e){let t=e,n=z(()=>jF({options:t.options,fen:t.fen,id:t.id}));return(e,t)=>t[0]||(_h(-1,!0),(t[0]=U(`div`,{"data-chessboard-hydratable":``,class:q(n.value?.class),id:n.value?.id,style:uh(n.value?.style),innerHTML:n.value?.html},null,14,[`id`,`innerHTML`])).cacheIndex=0,_h(1),t[0])}})})),LF,RF=t((()=>{IF(),IF(),LF=FF})),zF,BF=t((()=>{Aa(),Vl(),of(),Gs(),RF(),ou(),si(),Ba(),Kl(),zF=K({__name:`chessboard`,props:{id:{},options:{},mode:{},fen:{default:vd()},variant:{},excludedPlugins:{},monitorUntrustedEvents:{type:Boolean,default:!1}},setup(e){let t=e,n=yh(`placeholder`);return fh(async()=>{let e=n.value.$el,r=t.fen??void 0,i=t.variant,a=r?i?{fen:r,variant:i}:{fen:r}:void 0,o={...Of(),...t.options,id:t.id,test:To()},s,c;a&&(s=jn({boardOptions:o,options:{}}),s.load(a),c=a),await wl(e,{id:t.id,fen:r,variant:i,mode:t.mode,options:t.options,excludedPlugins:t.excludedPlugins,monitorUntrustedEvents:t.monitorUntrustedEvents,emitEvents:!0,api:s,init:c}),Wd()}),dh(()=>{(n.value?.$el)?.dispatchEvent(new CustomEvent(W
```

<a id="FND-30126"></a>
## FND-30126 — Implementation component chessboard

Vue compiled component __name declaration. Name suggests chessboard; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0201
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
x=0,_h(1),t[0])}})})),LF,RF=t((()=>{IF(),IF(),LF=FF})),zF,BF=t((()=>{Aa(),Vl(),of(),Gs(),RF(),ou(),si(),Ba(),Kl(),zF=K({__name:`chessboard`,props:{id:{},options:{},mode:{},fen:{default:vd()},variant:{},excludedPlugins:{},monitorUntrustedEvents:{type:Boolean,default:!1}},setup(e){let t=e,n=yh(`placeholder`);return fh(async()=>{let e=n.value.$el,r=t.fen??void 0,i=t.variant,a=r?i?{fen:r,variant:i}:{fen:r}:void 0,o={...Of(),...t.options,id:t.id,test:To()},s,c;a&&(s=jn({boardOptions:o,options:{}}),s.load(a),c=a),await wl(e,{id:t.id,fen:r,variant:i,mode:t.mode,options:t.options,excludedPlugins:t.excludedPlugins,monitorUntrustedEvents:t.monitorUntrustedEvents,emitEvents:!0,api:s,init:c}),Wd()}),dh(()=>{(n.value?.$el)?.dispatchEvent(new CustomEvent(Wr.Events.BoardDetached)),hd(t.id)}),(t,r)=>(J(),B(LF,{ref_key:`placeholder`,ref:n,id:e.id,fen:e.fen,options:e.options},null,8,[`id`,`fen`,`options`]))}})})),VF,HF=t((()=>{BF(),BF(),VF=zF})),UF,WF=t((()=>{Ml(),HF(),ou(),Kl(),Mf(),yl(),gu(),FM(),hc(),$o(),UF=K({__name:`chessboard`,setup(e){let t=jd(),n=z(()=>{switch(ps()?.type){case Dm.VotechessChallenge:return{fen:Hf()?.getInitialPosition()??vd(),variant:void 0};case Dm.DailyTeamMatchChallenge:return{fen:Qc()?.getI
```

<a id="FND-30127"></a>
## FND-30127 — Implementation component chessboard

Vue compiled component __name declaration. Name suggests chessboard; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0201
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
ptions`]))}})})),VF,HF=t((()=>{BF(),BF(),VF=zF})),UF,WF=t((()=>{Ml(),HF(),ou(),Kl(),Mf(),yl(),gu(),FM(),hc(),$o(),UF=K({__name:`chessboard`,setup(e){let t=jd(),n=z(()=>{switch(ps()?.type){case Dm.VotechessChallenge:return{fen:Hf()?.getInitialPosition()??vd(),variant:void 0};case Dm.DailyTeamMatchChallenge:return{fen:Qc()?.getInitialPosition()??vd(),variant:void 0};default:{let e=PM();return{fen:e?.fen??vd(),variant:e?.variant}}}}),r=z(()=>Of());return(e,i)=>(J(),B(VF,{id:Z(t),fen:n.value.fen,variant:n.value.variant,options:r.value,"monitor-untrusted-events":Z(Rs)()},null,8,[`id`,`fen`,`variant`,`options`,`monitor-untrusted-events`]))}})})),GF,KF=t((()=>{WF(),WF(),GF=UF})),qF,JF=t((()=>{TF(),AF(),il(),sA(),kA(),qM(),oF(),KF(),up(),_e(),_(),qF=K({__name:`application`,async setup(t){let n,r,i=ih(()=>h(()=>e(()=>import(`./side-controls.ab81330e.CHC6_1EB_M.chunk.js`),`./side-controls.ab81330e.CHC6_1EB_M.chunk.js`).then(e=>(e.t(),e.n)),__vite__mapDeps([0,61]),import.meta.url)),a=ih(()=>h(()=>e(()=>import(`./lazy-controllers.779ba150.Za0kuf1nZt.chunk.js`),`./lazy-controllers.779ba150.Za0kuf1nZt.chunk.js`).then(e=>(e.t(),e.n)),__vite__mapDeps([0]),import.meta.url)),o=ih(()=>h(()=>e(()=>import(`./focus-mode-si
```

<a id="FND-30128"></a>
## FND-30128 — Implementation component application

Vue compiled component __name declaration. Name suggests application; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0201
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
ts`]))}})})),GF,KF=t((()=>{WF(),WF(),GF=UF})),qF,JF=t((()=>{TF(),AF(),il(),sA(),kA(),qM(),oF(),KF(),up(),_e(),_(),qF=K({__name:`application`,async setup(t){let n,r,i=ih(()=>h(()=>e(()=>import(`./side-controls.ab81330e.CHC6_1EB_M.chunk.js`),`./side-controls.ab81330e.CHC6_1EB_M.chunk.js`).then(e=>(e.t(),e.n)),__vite__mapDeps([0,61]),import.meta.url)),a=ih(()=>h(()=>e(()=>import(`./lazy-controllers.779ba150.Za0kuf1nZt.chunk.js`),`./lazy-controllers.779ba150.Za0kuf1nZt.chunk.js`).then(e=>(e.t(),e.n)),__vite__mapDeps([0]),import.meta.url)),o=ih(()=>h(()=>e(()=>import(`./focus-mode-sidebar.8eca441b.DTeFPYY3Gi.chunk.js`),`./focus-mode-sidebar.8eca441b.DTeFPYY3Gi.chunk.js`).then(e=>(e.n(),e.t)),__vite__mapDeps([0,59,53,60]),import.meta.url)),s=z(()=>ju()),c=Ad();return[n,r]=xh(()=>oA()),await n,r(),(e,t)=>(J(),H(Qm,null,[G(wF,{"with-players":``,"with-controls":``,"with-evaluation":``,"with-pieces":``},{playerTop:$(()=>[G(KM,{position:`top`})]),chessboard:$(()=>[G(GF)]),playerBottom:$(()=>[G(KM,{position:`bottom`})]),controls:$(()=>[G(OA)]),pieces:$(()=>[Z(Od)()?(J(),B(Z(i),{key:0})):V(``,!0)]),_:1}),t[5]||=W(),G(kF,null,{sidebar:$(()=>[s.value?(J(),B(Z(o),{key:0})):V(``,!0),t[4]||=W(),s.value?V(``,!0):(J(),B(
```

<a id="FND-30129"></a>
## FND-30129 — Implementation component arena-header

Vue compiled component __name declaration. Name suggests arena header; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0753
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
),ae(),W=[`textContent`],G=[`textContent`],K=[`textContent`],q=[`textContent`],J=[`textContent`],Y=[`textContent`],X=D({__name:`arena-header`,props:{arena:{},currentTime:{},canCancel:{type:Boolean,default:!1},canChallengeClubs:{type:Boolean,default:!1},canSchedule:{type:Boolean,default:!1},isShareModalVisible:{type:Boolean,default:!1}},emits:[`cancel-arena`,`click-challenge-clubs`,`close-share-modal`,`open-event-details`,`open-schedule-event`],setup(e){let n=e,c=i(),l=b(()=>{let e=``;return e+=n.arena.getVariantLabel(),e+=` - `,e+=f(`{0} 0 players|{1} 1 player|]1,Inf] %1$s% players`,n.arena.getPlayersCount(),{"%1$s%":n.arena.getPlayersCount()}),e+=` - `,e+=n.arena.getTimeLabel(),n.arena.isRcnArenaModel()&&(e+=` - `,e+=n.arena.isRated()?r(`Rated`):r(`Unrated`)),e}),u=b(()=>{if(!n.arena.isMultiClubArena()&&!n.arena.isClubArena())return``;let e=``,t=n.arena.getMaxPlayers(),r=n.arena.getMaxScoredPlayers();return t&&(e+=n.arena.isMultiClubArena()?f(`{0} Max Players Per Club 0|{1} Max Players Per Club 1|]1,Inf] Max Players Per Club %playersLimit%`,t,{"%playersLimit%":t}):f(`{0} Max players 0|{1} Max players 1|]1,Inf] Max players %1$s%`,t,{"%1$s%":t})),t&&r&&(e+=` - `),r&&(e+=f(`{0} Scorers 0|{1} Scorers 1|]
```

<a id="FND-30130"></a>
## FND-30130 — Implementation component play-bot-button

Vue compiled component __name declaration. Name suggests play bot button; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0754
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
ame_review_same_tab`)&&E(`web_game_review_same_tab_experiment`,`test`)}var H=e((()=>{ie()})),U,W=e((()=>{ge(),s(),U=Pe({__name:`play-bot-button`,props:{label:{}},emits:[`click`],setup(e){let t=c(`Play %botName%`,{"%botName%":e.label});return(e,n)=>(Fe(),Ne(h,{"full-width":``,"is-one-line-text":``,variant:`secondary`,size:`large`,label:Ie(t),onClick:n[0]||=t=>e.$emit(`click`)},null,8,[`label`]))}})})),G,Le=e((()=>{W(),W(),G=U})),K,Re=e((()=>{g(),K={name:`gameReviewClicked`,eventProperties:{},trackers:[{tracker:m.Service,name:`Game Review - Clicked`}]}}));async function ze(e){let t=M(),n=w.generate(`web_analysis_game_callback_user_allowed_view`,e),{data:r}=await de.get(n);t.createAnalysisPermission={allowed:r.allowed,quotaType:r.quotaType}}var Be=e((()=>{ve(),_(),Se(),window.chesscom=window.chesscom||{},window.chesscom.routes=window.chesscom.routes||{},Object.assign(window.chesscom.routes,{web_analysis_game_callback_user_allowed_view:{tokens:[[`text`,`/callback/analysis/user/allowed`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US
```

<a id="FND-30131"></a>
## FND-30131 — Implementation component confirm-move

Vue compiled component __name declaration. Name suggests confirm move; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0755
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
ove-icon`,P={component:O,buttons:k,animation:A,animated:j,animate:M,icon:N}})),I,L=e((()=>{d(),c(),u(),t(),m(),r(),I=C({__name:`confirm-move`,props:{currentMove:{}},emits:[`cancel-move`,`confirm-move`],setup(e,{emit:t}){let r=e,c=t,u=g(()=>!r.currentMove||r.currentMove.status===a.MoveMade);return(t,r)=>(T(),_(h,{onCancelMove:r[2]||=e=>t.$emit(`cancel-move`),class:w(t.$style.component)},{default:D(()=>[u.value?(T(),y(`div`,{key:0,class:w(t.$style.buttons)},[S(i,{size:`large`,"aria-label":t.$trans(`Cancel Move`),icon:{is:E(s),variant:`glyph`},onClick:r[0]||=e=>c(`cancel-move`)},null,8,[`aria-label`,`icon`]),r[3]||=x(),S(i,{size:`large`,variant:`primary`,"aria-label":t.$trans(`Submit Move`),icon:{is:E(o),variant:`glyph`},onClick:r[1]||=e=>c(`confirm-move`)},null,8,[`aria-label`,`icon`])],2)):e.currentMove?.status===E(a).SavingMove?(T(),_(l,{key:1})):e.currentMove?.status===E(a).MoveSaved?(T(),y(`div`,{key:2,class:w(t.$style.animation)},[b(`div`,{class:w(t.$style.animated)},[S(n,{class:w(t.$style.icon),is:E(o),variant:`glyph`,size:32},null,8,[`class`,`is`])],2)],2)):v(``,!0)]),_:1},8,[`class`]))}})})),R,z,B=e((()=>{L(),L(),F(),p(),R={$style:P},z=f(I,[[`__cssModules`,R]])}));export{B as n,z as t};
```

<a id="FND-30132"></a>
## FND-30132 — Implementation component chat-menu

Vue compiled component __name declaration. Name suggests chat menu; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0757
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
wn,Tn,Q,En=e((()=>{Ie(),Ee(),_(),Ze(),s(),Ve(),Re(),p(),Sn(),Cn=[`textContent`],wn=[`onClick`],Tn=[`textContent`],Q=rn({__name:`chat-menu`,props:{allowGameChatWith:{},friendRequestSent:{type:Boolean},isFriend:{type:Boolean},showDisableChat:{type:Boolean},showGameChatSettings:{type:Boolean}},emits:[`add-friend`,`cancel-friend-request`,`show-report-user`,`disable-chat`,`menu-toggle`,`update-allow-game-chat-with`],setup(e,{emit:t}){let n=Y(!1),r=Y(!1),a=Y(!1),s=e,c=t,u=cn(),d=B(()=>s.allowGameChatWith!==`nobody`),f=B(()=>d.value?y(`On`):y(`Off`)),p=B(()=>xn(j.edit.options).filter(e=>e.value!=null&&e.value!==`nobody`).map(e=>({value:e.value,label:typeof e.label==`function`?e.label():e.label})));Be(Ne(),()=>{n.value=!1,r.value=!1,a.value=!1});function m(){n.value||r.value?n.value=!1:(n.value=!0,c(`menu-toggle`)),r.value=!1}function h(){n.value=!1,r.value=!0}function g(){n.value=!0,r.value=!1}function _(){n.value=!1,c(`disable-chat`)}function v(e){return s.allowGameChatWith===e?ae:be}function x(e){c(`update-allow-game-chat-with`,{value:e})}return(t,a)=>(J(),U(`div`,{class:q(X(u).component)},[K(Pe,{size:`x-small`,icon:{is:X(ee),variant:`glyph`},onClick:m},null,8,[`icon`]),a[13]||=G(),n.value?(J(),U(`div`,{ke
```

<a id="FND-30133"></a>
## FND-30133 — Implementation component game-chat

Vue compiled component __name declaration. Name suggests game chat; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0757
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
t(),$n(),tr(),fe(),rr(),ue(),n(),ar(),sr(),lr(),Ce(),je(),me(),tn(),dr(),pr(),hr(),_r(),yr(),xr(),Cr(),Tr(),qe(),Er=rn({__name:`game-chat`,setup(e){let t=te();lt(`game-chat`);let n=Y(!1),r=Se({allowGameChatWith(){return Vt()},gameModel(){return oe()},gameView(){return P(this.gameModel)},isPlaying(){return!!this.gameView?.isPlaying()},isChatMenuVisible(){return this.isPlaying&&!this.gameModel?.isBughouse()},isGuest(){return m()},currentUser(){return Je(0)},opponent(){return this.gameView?.gameChatOpponent??null},shouldEscapeContent(){return!!this.gameModel?.isLiveGameModel()},inputPreventPaste(){return we().isChatInputRestricted()||!Ke()?.isPremium()},inputTimeLimit(){return this.inputPreventPaste&&!this.isPlaying?1e4:0},minHeight(){return this.isChatTabSelected?null:this.gameView?.selectedGameTab===h.Bughouse?this.isPlaying&&this.gameModel?.isOver()?110:200:this.gameModel?.isOver()?160:230},maxHeight(){return this.isChatTabSelected?null:this.gameModel?.isRealtimeGame()&&this.gameModel?.isOver()?160:null},height(){return this.isChatTabSelected?null:ir()},isResizable(){return!this.isChatTabSelected&&!!(this.gameModel?.isRealtimeGame()&&this.gameView?.selectedGameTab!==h.Bughouse&&this.minHeight!==this.m
```

<a id="FND-30134"></a>
## FND-30134 — Implementation component eco-opening

Vue compiled component __name declaration. Name suggests eco opening; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0761
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
rez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}}),M=[`textContent`],N=S({__name:`eco-opening`,props:{openingData:{},explorerGameSource:{default:`master`},explorerGameType:{default:`all`},isExplorerClickable:{type:Boolean,default:!0},isOpeningClickable:{type:Boolean,default:!0},isExplorerVisible:{type:Boolean,default:!0}},setup(e){let t=e,n=g(()=>t.openingData.variant===`chess`),r=g(()=>{if(!n.value||!t.isExplorerVisible||!t.isExplorerClickable||!t.openingData.link)return{};let e={color:t.openingData.flipped?`black`:`white`,gameSource:t.explorerGameSource,...t.explorerGameSource===`master`&&t.explorerGameType===`all`?{}:{gameType:t.explorerGameType},moveList:t.openingData.moveList.join(`+`),ne:1,ply:t.openingData.moveNumber+1};return{target:`_blank`,href:decodeURIComponent(h.generate(`web_analysis_board_editor_tab`,{tab:`explorer`,...e}))}}),a=g(()=>!n.value||!t.isOpeningClickable||!t.openingData.link?{}:{target:`_blank`,href:h.generate(`web_openings_view`,{cleanUrl:t.openingData.link})});return(t,s)=>(T(),y(`div`,{class:w(t.$style.component)},[b(`span`,{class:w(t.$style.name),textContent:E(e.openingData.name)},null,10,M),s[0]||=x(),n.value?(T(),_(c,C({key
```

<a id="FND-30135"></a>
## FND-30135 — Implementation component draw-button

Vue compiled component __name declaration. Name suggests draw button; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0763
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
ar}})),cr,lr,ur,dr=e((()=>{N(),p(),L(),i(),Ue(),O(),l(),te(),cr=[`aria-label`],lr=[`textContent`],ur=K({inheritAttrs:!1,__name:`draw-button`,props:{confirmDraw:{type:Boolean,default:!1},hasOutgoingDrawOffer:{type:Boolean},hasDeclinedOutgoingDrawOffer:{type:Boolean},isDrawEnabled:{type:Boolean},hideButtonLabel:{type:Boolean,default:!1},showLabelOnHover:{type:Boolean,default:!1},hasActiveDrawOffer:{type:Boolean,default:!1},drawOfferMoves:{default:null},iconSize:{default:20}},emits:[`offer-draw`],setup(e,{emit:t}){let n=Q(),r=e,i=t,a=Ht(`confirmationPopover`),s=Bt(!1),c=z(()=>({[n.component]:!0,[n.disabled]:!r.isDrawEnabled,[n.wide]:l.value,[n.highlight]:r.hasOutgoingDrawOffer&&r.showLabelOnHover})),l=z(()=>r.showLabelOnHover&&s.value),u=z(()=>!r.hideButtonLabel&&!!(r.showLabelOnHover&&s.value||!r.showLabelOnHover)),d=z(()=>r.hasOutgoingDrawOffer&&r.showLabelOnHover?g(`Draw Offered`):g(`Draw`)),f=z(()=>r.isDrawEnabled||r.hasOutgoingDrawOffer||r.hasActiveDrawOffer||r.hasDeclinedOutgoingDrawOffer?``:ie(r.drawOfferMoves)?r.drawOfferMoves===0?g(`Draw offers not allowed in this game`):g(`You can offer a draw after move %move%`,{"%move%":r.drawOfferMoves}):g(`You can offer a draw after move 20`)),p=v(_);functi
```

<a id="FND-30136"></a>
## FND-30136 — Implementation component resign-button

Vue compiled component __name declaration. Name suggests resign button; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0763
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
odules`,fr]])})),hr,gr,_r,vr=e((()=>{N(),p(),L(),i(),O(),l(),hr=[`aria-label`],gr=[`textContent`],_r=K({inheritAttrs:!1,__name:`resign-button`,props:{confirmResign:{type:Boolean},isAbortable:{type:Boolean},isResignEnabled:{type:Boolean},hideButtonLabel:{type:Boolean,default:!1},showLabelOnHover:{type:Boolean,default:!1},resignEnabledAfterMove:{default:10},iconSize:{default:20}},emits:[`resign-game`,`abort-game`],setup(e,{emit:t}){let n=Q(),r=e,i=t,a=Ht(`confirmationPopover`),s=Bt(!1);Ut(()=>r.isAbortable,(e,t)=>{t&&!e&&a.value?.hide()});let c=z(()=>({[n.component]:!0,[n.disabled]:d.value,[n.wide]:l.value})),l=z(()=>r.showLabelOnHover&&s.value),u=z(()=>!r.hideButtonLabel&&!!(r.showLabelOnHover&&s.value||!r.showLabelOnHover)),d=z(()=>!r.isAbortable&&!r.isResignEnabled),f=z(()=>r.isAbortable?g(`Abort`):g(`Resign`)),p=z(()=>g(`You can resign after move %moveNumber%`,{"%moveNumber%":r.resignEnabledAfterMove})),m=z(()=>r.isAbortable?g(`Are you sure you want to abort?`):g(`Are you sure you want to resign?`)),h=v(x);function _(){d.value||(r.confirmResign?a.value?.show():h())}function y(){}function b(){x()}function x(){r.isAbortable?i(`abort-game`):i(`resign-game`)}function ee(){s.value=!0}function S(){s.value
```

<a id="FND-30137"></a>
## FND-30137 — Implementation component game-review-buttons

Vue compiled component __name declaration. Name suggests game review buttons; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0763
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
br,xr=e((()=>{vr(),vr(),jn(),F(),yr={$style:An},br=P(_r,[[`__cssModules`,yr]])})),Sr,Cr=e((()=>{N(),M(),at(),lt(),Sr=K({__name:`game-review-buttons`,props:{computerPlayerName:{},gameReviewLabel:{},gameReviewUrl:{},isPlaying:{type:Boolean}},emits:[`click-play-bot`,`click-review`],setup(e){let t=st()?`_self`:`_blank`;return(n,r)=>(Y(),H(`div`,{class:J(n.$style.component)},[G(C,{"full-width":``,"is-one-line-text":``,size:`xx-large`,variant:`primary`,icon:{is:Z(oe),variant:`glyph`},label:e.gameReviewLabel,"aria-label":e.gameReviewLabel,href:e.gameReviewUrl,target:Z(t),onClick:r[0]||=e=>n.$emit(`click-review`,e)},null,8,[`icon`,`label`,`aria-label`,`href`,`target`]),r[2]||=W(),e.computerPlayerName&&!e.isPlaying?(Y(),B(ot,{key:0,class:J(n.$style[`play-bot`]),label:e.computerPlayerName,onClick:r[1]||=e=>n.$emit(`click-play-bot`)},null,8,[`class`,`label`])):V(``,!0)],2))}})})),wr,Tr,Er=e((()=>{Cr(),Cr(),dn(),F(),wr={$style:un},Tr=P(Sr,[[`__cssModules`,wr]])})),Dr,Or=e((()=>{T(),me(),Ke(),l(),A(),Er(),At(),E(),rt(),ct(),ft(),t(),pe(),Dr=K({__name:`game-review-buttons`,setup(e){let t=k({gameReviewLabel(){return g(`Game Review`)},computerPlayerName(){return this.gameView?.getComputerPlayerName()||``},gameModel()
```

<a id="FND-30138"></a>
## FND-30138 — Implementation component game-review-buttons

Vue compiled component __name declaration. Name suggests game review buttons; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0763
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
e:un},Tr=P(Sr,[[`__cssModules`,wr]])})),Dr,Or=e((()=>{T(),me(),Ke(),l(),A(),Er(),At(),E(),rt(),ct(),ft(),t(),pe(),Dr=K({__name:`game-review-buttons`,setup(e){let t=k({gameReviewLabel(){return g(`Game Review`)},computerPlayerName(){return this.gameView?.getComputerPlayerName()||``},gameModel(){return w()},gameView(){return I(this.gameModel)},isPlaying(){return!!this.gameView?.isPlaying()},gameReviewUrl(){return this.gameModel&&!u()?yt(this.gameModel,`review`):void 0}});function n(e){if(u()){d({slide:h.GUEST_MODAL_SLIDES.analysis});return}t.gameModel&&(Ge()||e.preventDefault(),it(t.gameModel,`sidebar`))}function r(){if(t.gameModel?.isDailyGameModel()){if(t.gameModel.isVsCoach)return Mt();if(t.gameModel.isVsComputer)return jt(t.gameModel,t.computerPlayerName)}}return(e,i)=>(Y(),B(Tr,{"computer-player-name":Z(t).computerPlayerName,"is-playing":Z(t).isPlaying,"game-review-label":Z(t).gameReviewLabel,"game-review-url":Z(t).gameReviewUrl,onClickPlayBot:r,onClickReview:n},null,8,[`computer-player-name`,`is-playing`,`game-review-label`,`game-review-url`]))}})})),kr,Ar=e((()=>{Or(),Or(),kr=Dr})),jr,Mr,Nr=e((()=>{N(),p(),M(),O(),l(),jr=[`textContent`],Mr=K({__name:`new-game-buttons`,props:{isBughouse:{type:Boole
```

<a id="FND-30139"></a>
## FND-30139 — Implementation component new-game-buttons

Vue compiled component __name declaration. Name suggests new game buttons; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0763
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
ame-review-url`]))}})})),kr,Ar=e((()=>{Or(),Or(),kr=Dr})),jr,Mr,Nr=e((()=>{N(),p(),M(),O(),l(),jr=[`textContent`],Mr=K({__name:`new-game-buttons`,props:{isBughouse:{type:Boolean},isCreatingChallenge:{type:Boolean},isFocusMode:{type:Boolean},isIncomingRematchActionPending:{type:Boolean},isNewArenaGameVisible:{type:Boolean},isNewGameDisabled:{type:Boolean},isNewGameVisible:{type:Boolean},isOver:{type:Boolean},isPlaying:{type:Boolean},isRematchDisabled:{type:Boolean},isRematchVisible:{type:Boolean},isSeekingNewGame:{type:Boolean},isVsComputer:{type:Boolean},isVsCoach:{type:Boolean},isWaitingArenaGame:{type:Boolean},newGameVariantLink:{},rematchAccepted:{type:Boolean},rematchRequested:{type:Boolean},rematchUsername:{},timeControlLabel:{}},emits:[`accept-rematch`,`cancel-new-arena-game`,`cancel-new-game`,`cancel-rematch`,`decline-rematch`,`new-arena-game`,`new-game`,`rematch`],setup(e,{emit:t}){let n=e,r=t,i=Q(),a=z(()=>{if(n.isFocusMode)return`large`;if(n.isNewArenaGameVisible)return`xx-large`}),o=z(()=>({[i.component]:!0,[i.bughouse]:n.isBughouse,[i[`with-rematch`]]:!!n.rematchUsername||n.rematchRequested,[i[`focus-mode`]]:n.isFocusMode})),s=z(()=>n.rematchRequested?g(`Rematch Requested...`):n.rematchUse
```

<a id="FND-30140"></a>
## FND-30140 — Implementation component new-game-buttons

Vue compiled component __name declaration. Name suggests new game buttons; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0763
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
,ne(),Ze(),Ve(),Re(),Pe(),re(),xt(),be(),Me(),ct(),ft(),ke(),He(),je(),It(),Qe(),Xe(),m(),nt(),ye(),xe(),t(),Ee(),Lr=K({__name:`new-game-buttons`,setup(e){let t=k({gameModel(){return w()},gameView(){return I(this.gameModel)},isBughouse(){return!!this.gameModel?.isBughouse()},isFocusMode(){return le()},isPlaying(){return!!this.gameView?.isPlaying()},isOver(){return!!this.gameView?.isOver()},isCreatingChallenge(){return De()},incomingRematch(){return x(this.gameModel)},isIncomingRematchActionPending(){return!!(this.incomingRematch&&Fe(String(this.incomingRematch.getChallengeId())))},outgoingRematch(){return Pt(this.gameModel)},isSeekingNewGame(){return this.isOver?Ft():!1},isWaitingArenaGame(){return!!(this.gameModel?.isRealtimeGame()&&this.gameModel.isArenaGame())&&(!!(this.gameModel?.isLiveGameModel()&&et(this.gameModel.getArenaId()))||!!(this.gameModel?.isRcnGameModel()&&$e(this.gameModel.getArenaId())))},isNewArenaGameVisible(){return!!(this.isOver&&this.gameModel?.isRealtimeGame()&&this.gameModel.isArenaGame()&&(r(this.gameModel.getArenaId())||c(this.gameModel.getArenaId()))?.isInProgress())},isNewGameVisible(){return!this.isNewArenaGameVisible&&!this.isTeamMatchInProgress&&!this.isTournamentInProg
```

<a id="FND-30141"></a>
## FND-30141 — Implementation component quick-analysis-loader

Vue compiled component __name declaration. Name suggests quick analysis loader; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0763
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
s-coach`,`is-vs-computer`,`new-game-variant-link`]))}})})),zr,Br=e((()=>{Rr(),Rr(),zr=Lr})),Vr,Hr=e((()=>{N(),i(),Vr=K({__name:`quick-analysis-loader`,props:{progress:{}},setup(e){let t=e,n=z(()=>({transform:`translate3d(${t.progress*100-100}%, 0, 0)`}));return(e,t)=>(Y(),H(`div`,{class:J(e.$style.component)},[U(`div`,{class:J(e.$style.fill),style:zt(n.value)},null,6),t[0]||=W(),U(`div`,{class:J(e.$style.loaderMessage)},[G(o,{is:Z(he),class:J(e.$style.icon),variant:`glyph`,size:32},null,8,[`is`,`class`]),W(` `+X(e.$trans(`Analyzing Game...`)),1)],2)],2))}})})),Ur,Wr,Gr=e((()=>{Hr(),Hr(),Ln(),F(),Ur={$style:In},Wr=P(Vr,[[`__cssModules`,Ur]])}));function Kr(e,t){return Y(),H(`div`,{class:J(e.$style.loading)},[U(`div`,{class:J(e.$style.circle)},null,2),t[0]||=W(),U(`div`,{class:J(e.$style.circle)},null,2),t[1]||=W(),U(`div`,{class:J(e.$style.circle)},null,2)],2)}var qr,Jr,Yr,Xr=e((()=>{Yt(),F(),qr={},Jr={$style:Jt},Yr=P(qr,[[`render`,Kr],[`__cssModules`,Jr]])})),Zr,Qr,$r,ei,ti,ni=e((()=>{s(),Xr(),Lt(),pt(),O(),at(),Ct(),Zr=[`href`,`aria-label`,`target`],Qr=[`innerHTML`],$r=[`textContent`],ei=[`textContent`],ti=K({__name:`quick-analysis-tally`,props:{progress:{},results:{},singleRow:{type:Boolean},gameRev
```

<a id="FND-30142"></a>
## FND-30142 — Implementation component quick-analysis-tally

Vue compiled component __name declaration. Name suggests quick analysis tally; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0763
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
,Lt(),pt(),O(),at(),Ct(),Zr=[`href`,`aria-label`,`target`],Qr=[`innerHTML`],$r=[`textContent`],ei=[`textContent`],ti=K({__name:`quick-analysis-tally`,props:{progress:{},results:{},singleRow:{type:Boolean},gameReviewUrl:{},isBrilliantVerificationPending:{type:Boolean}},emits:[`click-game-review`],setup(e){let t=e,n=z(()=>{let e=dt(t.results);return Et(t.isBrilliantVerificationPending?e.filter(e=>e.key!==Rt.Brilliant):e)}),r=Q(),i=st()?`_self`:`_blank`,a=z(()=>({[r.component]:!0,[r[`single-row`]]:t.singleRow}));return(t,o)=>e.progress<1?(Y(),B(Yr,{key:0,class:J(Z(r)[`pulse-loader`])},null,8,[`class`])):(Y(),H(`a`,{key:1,class:J(a.value),onClick:o[0]||=e=>t.$emit(`click-game-review`,e),href:e.gameReviewUrl,"aria-label":t.$trans(`Game Review`),target:Z(i),tabIndex:`0`},[(Y(!0),H(R,null,Vt(n.value,t=>(Y(),H(`div`,{key:t.key,class:J([Z(r).item,Z(r)[t.key.toLowerCase()]])},[t.tooltip?(Y(),B(j,{key:0,text:t.tooltip},null,8,[`text`])):V(``,!0),o[2]||=W(),U(`div`,{class:J(Z(r).row)},[U(`span`,{class:J(Z(r).icon),innerHTML:Z(ge)({path:t.icon,size:`16`})},null,10,Qr),o[1]||=W(),e.singleRow?V(``,!0):(Y(),H(`div`,{key:0,textContent:X(t.count),class:J(Z(r).count)},null,10,$r))],2),o[3]||=W(),U(`div`,{textContent:X(e
```

<a id="FND-30143"></a>
## FND-30143 — Implementation component quick-analysis

Vue compiled component __name declaration. Name suggests quick analysis; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0763
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
)})),ri,ii,ai=e((()=>{ni(),ni(),rr(),F(),ri={$style:nr},ii=P(ti,[[`__cssModules`,ri]])})),oi,si=e((()=>{Gr(),ai(),oi=K({__name:`quick-analysis`,props:{isFocusMode:{type:Boolean},progress:{},results:{},gameReviewUrl:{},isBrilliantVerificationPending:{type:Boolean}},emits:[`click-game-review`],setup(e){let t=e,n=Q(),r=z(()=>({[n.component]:!0,[n[`focus-mode`]]:t.isFocusMode}));return(t,i)=>(Y(),H(`div`,{class:J(r.value)},[e.results&&e.progress===1?(Y(),B(ii,{key:0,results:e.results,"game-review-url":e.gameReviewUrl,"is-brilliant-verification-pending":e.isBrilliantVerificationPending,class:J(Z(n).tally),progress:e.progress,"single-row":``,onClickGameReview:i[0]||=e=>t.$emit(`click-game-review`)},null,8,[`results`,`game-review-url`,`is-brilliant-verification-pending`,`class`,`progress`])):(Y(),B(Wr,{key:1,progress:e.progress},null,8,[`progress`]))],2))}})})),ci,li,ui=e((()=>{si(),si(),sr(),F(),ci={$style:or},li=P(oi,[[`__cssModules`,ci]])})),di,fi=e((()=>{T(),de(),me(),ht(),bt(),A(),ui(),E(),rt(),y(),St(),vt(),t(),di=K({__name:`quick-analysis`,setup(e){let t=k({gameModel(){return w()},gameView(){return I(this.gameModel)},isFocusMode(){return le()},quickAnalysisProgress(){return this.gameModel?mt(this.game
```

<a id="FND-30144"></a>
## FND-30144 — Implementation component quick-analysis

Vue compiled component __name declaration. Name suggests quick analysis; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0763
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
e:or},li=P(oi,[[`__cssModules`,ci]])})),di,fi=e((()=>{T(),de(),me(),ht(),bt(),A(),ui(),E(),rt(),y(),St(),vt(),t(),di=K({__name:`quick-analysis`,setup(e){let t=k({gameModel(){return w()},gameView(){return I(this.gameModel)},isFocusMode(){return le()},quickAnalysisProgress(){return this.gameModel?mt(this.gameModel.id):0},brilliantVerificationPending(){return this.gameModel?Ot(this.gameModel.id):!1},quickAnalysisResults(){return this.gameModel?Dt(this.gameModel):Tt},gameReviewUrl(){return this.gameModel&&!_()?yt(this.gameModel,`review`):void 0}});function n(){_()&&d({slide:h.GUEST_MODAL_SLIDES.analysis})}return(e,r)=>Z(t).gameView?(Y(),B(li,{key:0,"game-review-url":Z(t).gameReviewUrl,"is-focus-mode":Z(t).isFocusMode,"is-brilliant-verification-pending":Z(t).brilliantVerificationPending,progress:Z(t).quickAnalysisProgress,results:Z(t).quickAnalysisResults,onClickGameReview:n},null,8,[`game-review-url`,`is-focus-mode`,`is-brilliant-verification-pending`,`progress`,`results`])):V(``,!0)}})})),pi,mi=e((()=>{fi(),fi(),pi=di}));export{kr as a,br as c,zr as i,pr as l,pi as n,Ar as o,Br as r,xr as s,mi as t,mr as u};
```

<a id="FND-30145"></a>
## FND-30145 — Implementation component evaluation

Vue compiled component __name declaration. Name suggests evaluation; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0774
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
)||d(ln().engineName)?.name||``)}}})),da,fa,pa,ma=n((()=>{E(),ua(),ae(),st(),f(),da=[`board-id`],fa=[`innerHTML`],pa=V({__name:`evaluation`,props:{boardId:{},isPremiumUser:{type:Boolean}},setup(e){x(`wc-evaluation-lines`,la);let t=P(()=>m(`<a target="_blank" href="/membership?c=liveanalysis">Upgrade</a> to get computer engine moves`));return(n,r)=>e.isPremiumUser?(U(),L(`wc-evaluation-lines`,{key:0,class:H([n.$style.component,n.$style.lines]),"board-id":e.boardId},null,10,da)):(U(),L(`div`,{key:1,class:H([n.$style.component,n.$style.upgrade])},[B(ue,{is:K(Ut),variant:`glyph`,class:H(n.$style.icon),size:12},null,8,[`is`,`class`]),r[0]||=z(),R(`span`,{innerHTML:t.value},null,8,fa)],2))}})})),ha,ga,_a=n((()=>{ma(),ma(),ai(),A(),ha={$style:ii},ga=D(pa,[[`__cssModules`,ha]])})),va,ya,ba,xa=n((()=>{E(),ae(),va=[`href`],ya=[`innerHTML`],ba=V({__name:`game-competition-title`,props:{competition:{}},setup(e){return(t,n)=>(U(),L(`a`,{href:e.competition.url,class:H(t.$style.component)},[B(ue,{is:e.competition.icon,variant:`glyph`,class:H(t.$style.icon),"custom-size":24},null,8,[`is`,`class`]),n[0]||=z(),R(`span`,{class:H(t.$style.name),innerHTML:e.competition.name},null,10,ya),n[1]||=z(),B(ue,{is:K(Ve),variant:`g
```

<a id="FND-30146"></a>
## FND-30146 — Implementation component game-competition-title

Vue compiled component __name declaration. Name suggests game competition title; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0774
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
(),A(),ha={$style:ii},ga=D(pa,[[`__cssModules`,ha]])})),va,ya,ba,xa=n((()=>{E(),ae(),va=[`href`],ya=[`innerHTML`],ba=V({__name:`game-competition-title`,props:{competition:{}},setup(e){return(t,n)=>(U(),L(`a`,{href:e.competition.url,class:H(t.$style.component)},[B(ue,{is:e.competition.icon,variant:`glyph`,class:H(t.$style.icon),"custom-size":24},null,8,[`is`,`class`]),n[0]||=z(),R(`span`,{class:H(t.$style.name),innerHTML:e.competition.name},null,10,ya),n[1]||=z(),B(ue,{is:K(Ve),variant:`glyph`,class:H(t.$style.arrow),size:16},null,8,[`is`,`class`])],10,va))}})})),Sa,Ca,wa=n((()=>{xa(),xa(),Gi(),A(),Sa={$style:Wi},Ca=D(ba,[[`__cssModules`,Sa]])})),Ta,Ea,Da=n((()=>{gn(),Ta=[`id`],Ea=V({__name:`game-tab`,props:{tabs:{},selectedTab:{},scrollContainerId:{},isShortSidebar:{type:Boolean}},emits:[`select-tab`],setup(e,{emit:t}){let n=e,r=t,i=nr(`scrollContainer`),a=P(()=>!i.value||!n.isShortSidebar);function o({tab:e}){r(`select-tab`,{tab:e})}return(t,n)=>(U(),L(Yn,null,[G(t.$slots,`title`),n[0]||=z(),e.tabs.length>1&&e.selectedTab?(U(),F(hn,{key:0,tabs:e.tabs,"selected-tab":e.selectedTab,onSelectTab:o},null,8,[`tabs`,`selected-tab`])):I(``,!0),n[1]||=z(),G(t.$slots,`header`),n[2]||=z(),R(`div`,{ref_key:`scrol
```

<a id="FND-30147"></a>
## FND-30147 — Implementation component game-tab

Vue compiled component __name declaration. Name suggests game tab; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0774
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
Ca,wa=n((()=>{xa(),xa(),Gi(),A(),Sa={$style:Wi},Ca=D(ba,[[`__cssModules`,Sa]])})),Ta,Ea,Da=n((()=>{gn(),Ta=[`id`],Ea=V({__name:`game-tab`,props:{tabs:{},selectedTab:{},scrollContainerId:{},isShortSidebar:{type:Boolean}},emits:[`select-tab`],setup(e,{emit:t}){let n=e,r=t,i=nr(`scrollContainer`),a=P(()=>!i.value||!n.isShortSidebar);function o({tab:e}){r(`select-tab`,{tab:e})}return(t,n)=>(U(),L(Yn,null,[G(t.$slots,`title`),n[0]||=z(),e.tabs.length>1&&e.selectedTab?(U(),F(hn,{key:0,tabs:e.tabs,"selected-tab":e.selectedTab,onSelectTab:o},null,8,[`tabs`,`selected-tab`])):I(``,!0),n[1]||=z(),G(t.$slots,`header`),n[2]||=z(),R(`div`,{ref_key:`scrollContainer`,ref:i,id:e.scrollContainerId,class:H(t.$style.scrollable)},[G(t.$slots,`scrollable`)],10,Ta),n[3]||=z(),(U(),F(Xn,{disabled:a.value,to:i.value},[G(t.$slots,`scrollable-footer`)],8,[`disabled`,`to`])),n[4]||=z(),G(t.$slots,`footer`)],64))}})})),Oa,ka,Aa=n((()=>{Da(),Da(),$i(),A(),Oa={$style:Qi},ka=D(Ea,[[`__cssModules`,Oa]])})),ja,Ma=n((()=>{fe(),pe(),Ae(),tn(),k(),ja=class extends De{constructor(){super(),T(this,`updateMovelistHandler`,void 0),T(this,`moveList`,void 0),T(this,`events`,[nt.InstanceEvents.ModeChanged,nt.InstanceEvents.Create,`AnalysisStart
```

<a id="FND-30148"></a>
## FND-30148 — Implementation component mode-swap-move-list-wrapper

Vue compiled component __name declaration. Name suggests mode swap move list wrapper; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0774
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
t`}}})),Na,Pa,Fa=n((()=>{Ma(),tn(),st(),Na=[`scroll-container-id`,`board-id`,`display-result`,`timestamp-method`],Pa=V({__name:`mode-swap-move-list-wrapper`,props:{boardId:{},displayResult:{},scrollContainerId:{},isTimestampsVisible:{type:Boolean},timestampMethod:{}},setup(e){x(`wc-mode-swap-move-list`,ja),x(`wc-simple-move-list`,rn),x(`wc-move-list`,on);let t=e,n=tr(),r=P(()=>({[n.component]:!0,[n[`hide-timestamps`]]:!t.isTimestampsVisible}));return(t,n)=>(U(),L(`wc-mode-swap-move-list`,{class:H(r.value),"scroll-container-id":e.scrollContainerId,"board-id":e.boardId,"display-result":e.displayResult,"timestamp-method":e.timestampMethod},null,10,Na))}})})),Ia,La,Ra=n((()=>{Fa(),Fa(),ra(),A(),Ia={$style:na},La=D(Pa,[[`__cssModules`,Ia]])}));function za(){let t=$t();if(we()){sn();return}kt(()=>b(()=>e(()=>import(`./add-to-library-modal.7aa12abc.B0mYJrJMhL.chunk.js`),`./add-to-library-modal.7aa12abc.B0mYJrJMhL.chunk.js`).then(e=>(e.n(),e.t)),__vite__mapDeps([0,1,2,3,4,5,6,7,8]),import.meta.url)),t.isVisible=!0}var Ba=n((()=>{Qe(),cn(),en(),be(),y()})),Va,Ha=n((()=>{Jt(),vt(),Va=ie(`Ci5jaGVzc2NvbS9mYXZvcml0ZV9nYW1lcy92MS9mYXZvcml0ZV9nYW1lLnByb3RvEhpjaGVzc2NvbS5mYXZvcml0ZV9nYW1lcy52MSJkCgxGYXZvcml0ZUdhbWUSE
```

<a id="FND-30149"></a>
## FND-30149 — Implementation component favorite-game-toggle

Vue compiled component __name declaration. Name suggests favorite game toggle; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0774
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
ng:s,isLoading:c,hasIdentifier:n,toggle:te}}var po=n((()=>{Kt(),Ya(),Za(),so(),lo()})),mo,ho=n((()=>{E(),po(),O(),mo=V({__name:`favorite-game-toggle`,props:{gameId:{},gameUuid:{},isFavorite:{type:[Boolean,null],default:null},isVsComputer:{type:Boolean},isVsCoach:{type:Boolean}},emits:[`update:is-favorite`],setup(e,{emit:t}){let n=e,r=t,{isFavorite:i,isPending:a,isLoading:o,hasIdentifier:s,toggle:c}=fo(n);async function l(){let e=await c();r(`update:is-favorite`,e)}return(e,t)=>K(s)?(U(),F(w,{key:0,size:`small`,variant:`ghost`,class:H([e.$style.component,{[e.$style.favorite]:K(i),[e.$style.loading]:K(o)}]),disabled:K(a)||K(o),icon:{is:K(i)?K(xe):K(Ie),variant:`glyph`},"icon-size":20,tooltip:K(i)?e.$trans(`Remove from Favorites`):e.$trans(`Add to Favorites`),onClick:l},null,8,[`class`,`disabled`,`icon`,`tooltip`])):I(``,!0)}})})),go,_o,vo=n((()=>{ho(),ho(),Sr(),A(),go={$style:xr},_o=D(mo,[[`__cssModules`,go]])})),yo,bo=n((()=>{E(),C(),_(),yo=V({__name:`move-backward-button`,props:{isAtBeginningOfLine:{type:Boolean}},emits:[`click`],setup(e){return(t,n)=>(U(),F(h,{size:`large`,disabled:e.isAtBeginningOfLine,"aria-label":t.$trans(`Previous Move`),icon:{is:K(c),variant:`glyph`},onClick:n[0]||=e=>t.$emit(`c
```

<a id="FND-30150"></a>
## FND-30150 — Implementation component move-backward-button

Vue compiled component __name declaration. Name suggests move backward button; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0774
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
)),go,_o,vo=n((()=>{ho(),ho(),Sr(),A(),go={$style:xr},_o=D(mo,[[`__cssModules`,go]])})),yo,bo=n((()=>{E(),C(),_(),yo=V({__name:`move-backward-button`,props:{isAtBeginningOfLine:{type:Boolean}},emits:[`click`],setup(e){return(t,n)=>(U(),F(h,{size:`large`,disabled:e.isAtBeginningOfLine,"aria-label":t.$trans(`Previous Move`),icon:{is:K(c),variant:`glyph`},onClick:n[0]||=e=>t.$emit(`click`)},{default:q(()=>[B(S,{text:t.$trans(`Previous Move`)},null,8,[`text`])]),_:1},8,[`disabled`,`aria-label`,`icon`]))}})})),xo,So=n((()=>{bo(),bo(),xo=yo})),Co,wo=n((()=>{E(),C(),_(),Co=V({__name:`move-end-button`,props:{isAtEndOfLine:{type:Boolean}},emits:[`click`],setup(e){return(t,n)=>(U(),F(h,{size:`large`,disabled:e.isAtEndOfLine,"aria-label":t.$trans(`Last Move`),icon:{is:K(he),variant:`glyph`},onClick:n[0]||=e=>t.$emit(`click`)},{default:q(()=>[B(S,{text:t.$trans(`Last Move`)},null,8,[`text`])]),_:1},8,[`disabled`,`aria-label`,`icon`]))}})})),To,Eo=n((()=>{wo(),wo(),To=Co})),Do,Oo=n((()=>{E(),C(),_(),Do=V({__name:`move-forward-button`,props:{isAtEndOfLine:{type:Boolean}},emits:[`click`],setup(e){return(t,n)=>(U(),F(h,{size:`large`,disabled:e.isAtEndOfLine,"aria-label":t.$trans(`Next Move`),icon:{is:K(Ve),variant:`g
```

<a id="FND-30151"></a>
## FND-30151 — Implementation component move-end-button

Vue compiled component __name declaration. Name suggests move end button; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0774
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
t`])]),_:1},8,[`disabled`,`aria-label`,`icon`]))}})})),xo,So=n((()=>{bo(),bo(),xo=yo})),Co,wo=n((()=>{E(),C(),_(),Co=V({__name:`move-end-button`,props:{isAtEndOfLine:{type:Boolean}},emits:[`click`],setup(e){return(t,n)=>(U(),F(h,{size:`large`,disabled:e.isAtEndOfLine,"aria-label":t.$trans(`Last Move`),icon:{is:K(he),variant:`glyph`},onClick:n[0]||=e=>t.$emit(`click`)},{default:q(()=>[B(S,{text:t.$trans(`Last Move`)},null,8,[`text`])]),_:1},8,[`disabled`,`aria-label`,`icon`]))}})})),To,Eo=n((()=>{wo(),wo(),To=Co})),Do,Oo=n((()=>{E(),C(),_(),Do=V({__name:`move-forward-button`,props:{isAtEndOfLine:{type:Boolean}},emits:[`click`],setup(e){return(t,n)=>(U(),F(h,{size:`large`,disabled:e.isAtEndOfLine,"aria-label":t.$trans(`Next Move`),icon:{is:K(Ve),variant:`glyph`},onClick:n[0]||=e=>t.$emit(`click`)},{default:q(()=>[B(S,{text:t.$trans(`Next Move`)},null,8,[`text`])]),_:1},8,[`disabled`,`aria-label`,`icon`]))}})})),ko,Ao=n((()=>{Oo(),Oo(),ko=Do})),jo,Mo=n((()=>{E(),gt(),C(),_(),jo=V({__name:`move-replay-button`,props:{isAtEndOfLine:{type:Boolean}},emits:[`move-forward`,`go-to-start`],setup(e,{emit:t}){let n=e,r=t,i=Ye(s,500,{immediate:!1});Qn(()=>{i.stop()});let a=P(()=>i.isPending.value?Yt:We);function o()
```

<a id="FND-30152"></a>
## FND-30152 — Implementation component move-forward-button

Vue compiled component __name declaration. Name suggests move forward button; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0774
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
t`])]),_:1},8,[`disabled`,`aria-label`,`icon`]))}})})),To,Eo=n((()=>{wo(),wo(),To=Co})),Do,Oo=n((()=>{E(),C(),_(),Do=V({__name:`move-forward-button`,props:{isAtEndOfLine:{type:Boolean}},emits:[`click`],setup(e){return(t,n)=>(U(),F(h,{size:`large`,disabled:e.isAtEndOfLine,"aria-label":t.$trans(`Next Move`),icon:{is:K(Ve),variant:`glyph`},onClick:n[0]||=e=>t.$emit(`click`)},{default:q(()=>[B(S,{text:t.$trans(`Next Move`)},null,8,[`text`])]),_:1},8,[`disabled`,`aria-label`,`icon`]))}})})),ko,Ao=n((()=>{Oo(),Oo(),ko=Do})),jo,Mo=n((()=>{E(),gt(),C(),_(),jo=V({__name:`move-replay-button`,props:{isAtEndOfLine:{type:Boolean}},emits:[`move-forward`,`go-to-start`],setup(e,{emit:t}){let n=e,r=t,i=Ye(s,500,{immediate:!1});Qn(()=>{i.stop()});let a=P(()=>i.isPending.value?Yt:We);function o(){n.isAtEndOfLine&&r(`go-to-start`),i.isPending.value?i.stop():i.start()}function s(){i.stop(),n.isAtEndOfLine||(r(`move-forward`),i.start())}return(e,t)=>(U(),F(h,{size:`large`,"aria-label":e.$trans(`Play / Pause`),icon:{is:a.value,variant:`glyph`},onClick:o},{default:q(()=>[B(S,{text:e.$trans(`Play / Pause`)},null,8,[`text`])]),_:1},8,[`aria-label`,`icon`]))}})})),No,Po=n((()=>{Mo(),Mo(),No=jo})),Fo,Io=n((()=>{E(),C(),_(),Fo=V(
```

<a id="FND-30153"></a>
## FND-30153 — Implementation component move-replay-button

Vue compiled component __name declaration. Name suggests move replay button; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0774
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
),_:1},8,[`disabled`,`aria-label`,`icon`]))}})})),ko,Ao=n((()=>{Oo(),Oo(),ko=Do})),jo,Mo=n((()=>{E(),gt(),C(),_(),jo=V({__name:`move-replay-button`,props:{isAtEndOfLine:{type:Boolean}},emits:[`move-forward`,`go-to-start`],setup(e,{emit:t}){let n=e,r=t,i=Ye(s,500,{immediate:!1});Qn(()=>{i.stop()});let a=P(()=>i.isPending.value?Yt:We);function o(){n.isAtEndOfLine&&r(`go-to-start`),i.isPending.value?i.stop():i.start()}function s(){i.stop(),n.isAtEndOfLine||(r(`move-forward`),i.start())}return(e,t)=>(U(),F(h,{size:`large`,"aria-label":e.$trans(`Play / Pause`),icon:{is:a.value,variant:`glyph`},onClick:o},{default:q(()=>[B(S,{text:e.$trans(`Play / Pause`)},null,8,[`text`])]),_:1},8,[`aria-label`,`icon`]))}})})),No,Po=n((()=>{Mo(),Mo(),No=jo})),Fo,Io=n((()=>{E(),C(),_(),Fo=V({__name:`move-start-button`,props:{isAtBeginningOfLine:{type:Boolean}},emits:[`click`],setup(e){return(t,n)=>(U(),F(h,{size:`large`,disabled:e.isAtBeginningOfLine,"aria-label":t.$trans(`First Move`),icon:{is:K(ye),variant:`glyph`},onClick:n[0]||=e=>t.$emit(`click`)},{default:q(()=>[B(S,{text:t.$trans(`First Move`)},null,8,[`text`])]),_:1},8,[`disabled`,`aria-label`,`icon`]))}})})),Lo,Ro=n((()=>{Io(),Io(),Lo=Fo})),zo,Bo=n((()=>{gt(),rt(),
```

<a id="FND-30154"></a>
## FND-30154 — Implementation component move-start-button

Vue compiled component __name declaration. Name suggests move start button; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0774
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
ull,8,[`text`])]),_:1},8,[`aria-label`,`icon`]))}})})),No,Po=n((()=>{Mo(),Mo(),No=jo})),Fo,Io=n((()=>{E(),C(),_(),Fo=V({__name:`move-start-button`,props:{isAtBeginningOfLine:{type:Boolean}},emits:[`click`],setup(e){return(t,n)=>(U(),F(h,{size:`large`,disabled:e.isAtBeginningOfLine,"aria-label":t.$trans(`First Move`),icon:{is:K(ye),variant:`glyph`},onClick:n[0]||=e=>t.$emit(`click`)},{default:q(()=>[B(S,{text:t.$trans(`First Move`)},null,8,[`text`])]),_:1},8,[`disabled`,`aria-label`,`icon`]))}})})),Lo,Ro=n((()=>{Io(),Io(),Lo=Fo})),zo,Bo=n((()=>{gt(),rt(),wt(),zo=V({__name:`game-buttons-container`,props:{showButtons:{type:Boolean}},setup(e){let t=Be()||![`prod`,`staging`].includes(window.context.environment),n=nr(`root`),r=W(Be()),i=Oe();return t&&at(n,([e])=>{r.value=!e.isIntersecting},{rootMargin:`0px`,threshold:1}),(t,a)=>(U(),L(Yn,null,[e.showButtons?(U(),L(`div`,{key:0,class:H(t.$style.component),ref_key:`root`,ref:n},[G(t.$slots,`default`)],2)):I(``,!0),a[0]||=z(),K(i)&&r.value?(U(),F(Xn,{key:1,to:`body`},[R(`div`,{class:H(t.$style.mobile)},[G(t.$slots,`default`)],2)])):I(``,!0)],64))}})})),Vo,Ho,Uo=n((()=>{Bo(),Bo(),zi(),A(),Vo={$style:Ri},Ho=D(zo,[[`__cssModules`,Vo]])})),Wo,Go=n((()=>{E(),O(),W
```

<a id="FND-30155"></a>
## FND-30155 — Implementation component game-buttons-container

Vue compiled component __name declaration. Name suggests game buttons container; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0774
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
)]),_:1},8,[`disabled`,`aria-label`,`icon`]))}})})),Lo,Ro=n((()=>{Io(),Io(),Lo=Fo})),zo,Bo=n((()=>{gt(),rt(),wt(),zo=V({__name:`game-buttons-container`,props:{showButtons:{type:Boolean}},setup(e){let t=Be()||![`prod`,`staging`].includes(window.context.environment),n=nr(`root`),r=W(Be()),i=Oe();return t&&at(n,([e])=>{r.value=!e.isIntersecting},{rootMargin:`0px`,threshold:1}),(t,a)=>(U(),L(Yn,null,[e.showButtons?(U(),L(`div`,{key:0,class:H(t.$style.component),ref_key:`root`,ref:n},[G(t.$slots,`default`)],2)):I(``,!0),a[0]||=z(),K(i)&&r.value?(U(),F(Xn,{key:1,to:`body`},[R(`div`,{class:H(t.$style.mobile)},[G(t.$slots,`default`)],2)])):I(``,!0)],64))}})})),Vo,Ho,Uo=n((()=>{Bo(),Bo(),zi(),A(),Vo={$style:Ri},Ho=D(zo,[[`__cssModules`,Vo]])})),Wo,Go=n((()=>{E(),O(),Wo=V({__name:`add-to-library-icon`,emits:[`click`],setup(e){return(e,t)=>(U(),F(w,{"aria-label":e.$trans(`Add to Collection`),icon:{is:K(tt),variant:`glyph`},"icon-size":20,tooltip:e.$trans(`Add to Collection`),onClick:t[0]||=t=>e.$emit(`click`)},null,8,[`aria-label`,`icon`,`tooltip`]))}})})),Ko,qo=n((()=>{Go(),Go(),Ko=Wo})),Jo,Yo=n((()=>{E(),O(),Jo=V({__name:`analysis-icon`,props:{analysisUrl:{}},emits:[`click`],setup(e){return(t,n)=>(U(),F(w,{hre
```

<a id="FND-30156"></a>
## FND-30156 — Implementation component add-to-library-icon

Vue compiled component __name declaration. Name suggests add to library icon; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0774
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
}})})),Vo,Ho,Uo=n((()=>{Bo(),Bo(),zi(),A(),Vo={$style:Ri},Ho=D(zo,[[`__cssModules`,Vo]])})),Wo,Go=n((()=>{E(),O(),Wo=V({__name:`add-to-library-icon`,emits:[`click`],setup(e){return(e,t)=>(U(),F(w,{"aria-label":e.$trans(`Add to Collection`),icon:{is:K(tt),variant:`glyph`},"icon-size":20,tooltip:e.$trans(`Add to Collection`),onClick:t[0]||=t=>e.$emit(`click`)},null,8,[`aria-label`,`icon`,`tooltip`]))}})})),Ko,qo=n((()=>{Go(),Go(),Ko=Wo})),Jo,Yo=n((()=>{E(),O(),Jo=V({__name:`analysis-icon`,props:{analysisUrl:{}},emits:[`click`],setup(e){return(t,n)=>(U(),F(w,{href:e.analysisUrl,target:`_blank`,"aria-label":t.$trans(`Self Analysis`),icon:{is:K(Pt),variant:`glyph`},"icon-size":20,tooltip:t.$trans(`Self Analysis`),onClick:n[0]||=e=>t.$emit(`click`)},null,8,[`href`,`aria-label`,`icon`,`tooltip`]))}})})),Xo,Zo=n((()=>{Yo(),Yo(),Xo=Jo})),Qo,$o=n((()=>{E(),O(),Qo=V({__name:`classroom-icon`,props:{classroomUrl:{}},emits:[`click`],setup(e){return(t,n)=>(U(),F(w,{href:e.classroomUrl,target:`_blank`,"aria-label":t.$trans(`Classroom`),icon:{is:K(Mt),variant:`glyph`},"icon-size":20,tooltip:t.$trans(`Classroom`),onClick:n[0]||=e=>t.$emit(`click`,e)},null,8,[`href`,`aria-label`,`icon`,`tooltip`]))}})})),es,ts=n((()=>{$
```

<a id="FND-30157"></a>
## FND-30157 — Implementation component analysis-icon

Vue compiled component __name declaration. Name suggests analysis icon; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0774
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
t(`click`)},null,8,[`aria-label`,`icon`,`tooltip`]))}})})),Ko,qo=n((()=>{Go(),Go(),Ko=Wo})),Jo,Yo=n((()=>{E(),O(),Jo=V({__name:`analysis-icon`,props:{analysisUrl:{}},emits:[`click`],setup(e){return(t,n)=>(U(),F(w,{href:e.analysisUrl,target:`_blank`,"aria-label":t.$trans(`Self Analysis`),icon:{is:K(Pt),variant:`glyph`},"icon-size":20,tooltip:t.$trans(`Self Analysis`),onClick:n[0]||=e=>t.$emit(`click`)},null,8,[`href`,`aria-label`,`icon`,`tooltip`]))}})})),Xo,Zo=n((()=>{Yo(),Yo(),Xo=Jo})),Qo,$o=n((()=>{E(),O(),Qo=V({__name:`classroom-icon`,props:{classroomUrl:{}},emits:[`click`],setup(e){return(t,n)=>(U(),F(w,{href:e.classroomUrl,target:`_blank`,"aria-label":t.$trans(`Classroom`),icon:{is:K(Mt),variant:`glyph`},"icon-size":20,tooltip:t.$trans(`Classroom`),onClick:n[0]||=e=>t.$emit(`click`,e)},null,8,[`href`,`aria-label`,`icon`,`tooltip`]))}})})),es,ts=n((()=>{$o(),$o(),es=Qo})),ns,rs=n((()=>{E(),O(),ns=V({__name:`flip-board-icon`,emits:[`click`],setup(e){return(e,t)=>(U(),F(w,{"aria-label":e.$trans(`Flip Board`),icon:{is:K(dt),variant:`glyph`},"icon-size":20,tooltip:e.$trans(`Flip Board`),onClick:t[0]||=t=>e.$emit(`click`)},null,8,[`aria-label`,`icon`,`tooltip`]))}})})),is,as=n((()=>{rs(),rs(),is=ns})),
```

<a id="FND-30158"></a>
## FND-30158 — Implementation component classroom-icon

Vue compiled component __name declaration. Name suggests classroom icon; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0774
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
k`)},null,8,[`href`,`aria-label`,`icon`,`tooltip`]))}})})),Xo,Zo=n((()=>{Yo(),Yo(),Xo=Jo})),Qo,$o=n((()=>{E(),O(),Qo=V({__name:`classroom-icon`,props:{classroomUrl:{}},emits:[`click`],setup(e){return(t,n)=>(U(),F(w,{href:e.classroomUrl,target:`_blank`,"aria-label":t.$trans(`Classroom`),icon:{is:K(Mt),variant:`glyph`},"icon-size":20,tooltip:t.$trans(`Classroom`),onClick:n[0]||=e=>t.$emit(`click`,e)},null,8,[`href`,`aria-label`,`icon`,`tooltip`]))}})})),es,ts=n((()=>{$o(),$o(),es=Qo})),ns,rs=n((()=>{E(),O(),ns=V({__name:`flip-board-icon`,emits:[`click`],setup(e){return(e,t)=>(U(),F(w,{"aria-label":e.$trans(`Flip Board`),icon:{is:K(dt),variant:`glyph`},"icon-size":20,tooltip:e.$trans(`Flip Board`),onClick:t[0]||=t=>e.$emit(`click`)},null,8,[`aria-label`,`icon`,`tooltip`]))}})})),is,as=n((()=>{rs(),rs(),is=ns})),os,ss=n((()=>{E(),O(),os=V({__name:`reload-board-icon`,emits:[`click`],setup(e){return(e,t)=>(U(),F(w,{"aria-label":e.$trans(`Reload`),icon:{is:K(oe),variant:`glyph`},"icon-size":20,tooltip:e.$trans(`Reload`),onClick:t[0]||=t=>e.$emit(`click`)},null,8,[`aria-label`,`icon`,`tooltip`]))}})})),cs,ls=n((()=>{ss(),ss(),cs=os})),us,ds=n((()=>{E(),O(),us=V({__name:`share-icon`,emits:[`click`],setup(e){re
```

<a id="FND-30159"></a>
## FND-30159 — Implementation component flip-board-icon

Vue compiled component __name declaration. Name suggests flip board icon; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0774
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
,e)},null,8,[`href`,`aria-label`,`icon`,`tooltip`]))}})})),es,ts=n((()=>{$o(),$o(),es=Qo})),ns,rs=n((()=>{E(),O(),ns=V({__name:`flip-board-icon`,emits:[`click`],setup(e){return(e,t)=>(U(),F(w,{"aria-label":e.$trans(`Flip Board`),icon:{is:K(dt),variant:`glyph`},"icon-size":20,tooltip:e.$trans(`Flip Board`),onClick:t[0]||=t=>e.$emit(`click`)},null,8,[`aria-label`,`icon`,`tooltip`]))}})})),is,as=n((()=>{rs(),rs(),is=ns})),os,ss=n((()=>{E(),O(),os=V({__name:`reload-board-icon`,emits:[`click`],setup(e){return(e,t)=>(U(),F(w,{"aria-label":e.$trans(`Reload`),icon:{is:K(oe),variant:`glyph`},"icon-size":20,tooltip:e.$trans(`Reload`),onClick:t[0]||=t=>e.$emit(`click`)},null,8,[`aria-label`,`icon`,`tooltip`]))}})})),cs,ls=n((()=>{ss(),ss(),cs=os})),us,ds=n((()=>{E(),O(),us=V({__name:`share-icon`,emits:[`click`],setup(e){return(e,t)=>(U(),F(w,{"aria-label":e.$trans(`Share`),icon:{is:K(_e),variant:`glyph`},"icon-size":20,tooltip:e.$trans(`Share`),onClick:t[0]||=t=>e.$emit(`click`)},null,8,[`aria-label`,`icon`,`tooltip`]))}})})),fs,ps=n((()=>{ds(),ds(),fs=us})),ms,hs=n((()=>{ms=V({__name:`game-icons-container`,props:{isBughouse:{type:Boolean}},setup(e){let t=e,n=tr(),r=P(()=>({[n.component]:!0,[n.bughouse]:t.isBugh
```

<a id="FND-30160"></a>
## FND-30160 — Implementation component reload-board-icon

Vue compiled component __name declaration. Name suggests reload board icon; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0774
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
t(`click`)},null,8,[`aria-label`,`icon`,`tooltip`]))}})})),is,as=n((()=>{rs(),rs(),is=ns})),os,ss=n((()=>{E(),O(),os=V({__name:`reload-board-icon`,emits:[`click`],setup(e){return(e,t)=>(U(),F(w,{"aria-label":e.$trans(`Reload`),icon:{is:K(oe),variant:`glyph`},"icon-size":20,tooltip:e.$trans(`Reload`),onClick:t[0]||=t=>e.$emit(`click`)},null,8,[`aria-label`,`icon`,`tooltip`]))}})})),cs,ls=n((()=>{ss(),ss(),cs=os})),us,ds=n((()=>{E(),O(),us=V({__name:`share-icon`,emits:[`click`],setup(e){return(e,t)=>(U(),F(w,{"aria-label":e.$trans(`Share`),icon:{is:K(_e),variant:`glyph`},"icon-size":20,tooltip:e.$trans(`Share`),onClick:t[0]||=t=>e.$emit(`click`)},null,8,[`aria-label`,`icon`,`tooltip`]))}})})),fs,ps=n((()=>{ds(),ds(),fs=us})),ms,hs=n((()=>{ms=V({__name:`game-icons-container`,props:{isBughouse:{type:Boolean}},setup(e){let t=e,n=tr(),r=P(()=>({[n.component]:!0,[n.bughouse]:t.isBughouse}));return(e,t)=>(U(),L(`div`,{class:H(r.value)},[G(e.$slots,`left`),t[0]||=z(),R(`div`,{class:H(K(n).spacer)},null,2),t[1]||=z(),G(e.$slots,`right`)],2))}})})),gs,_s,vs=n((()=>{hs(),hs(),Xi(),A(),gs={$style:Yi},_s=D(ms,[[`__cssModules`,gs]])}));function ys(){let e=Et();e.game.observing?.isAnalyzing()?e.game.observing.restore
```

<a id="FND-30161"></a>
## FND-30161 — Implementation component share-icon

Vue compiled component __name declaration. Name suggests share icon; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0774
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
t(`click`)},null,8,[`aria-label`,`icon`,`tooltip`]))}})})),cs,ls=n((()=>{ss(),ss(),cs=os})),us,ds=n((()=>{E(),O(),us=V({__name:`share-icon`,emits:[`click`],setup(e){return(e,t)=>(U(),F(w,{"aria-label":e.$trans(`Share`),icon:{is:K(_e),variant:`glyph`},"icon-size":20,tooltip:e.$trans(`Share`),onClick:t[0]||=t=>e.$emit(`click`)},null,8,[`aria-label`,`icon`,`tooltip`]))}})})),fs,ps=n((()=>{ds(),ds(),fs=us})),ms,hs=n((()=>{ms=V({__name:`game-icons-container`,props:{isBughouse:{type:Boolean}},setup(e){let t=e,n=tr(),r=P(()=>({[n.component]:!0,[n.bughouse]:t.isBughouse}));return(e,t)=>(U(),L(`div`,{class:H(r.value)},[G(e.$slots,`left`),t[0]||=z(),R(`div`,{class:H(K(n).spacer)},null,2),t[1]||=z(),G(e.$slots,`right`)],2))}})})),gs,_s,vs=n((()=>{hs(),hs(),Xi(),A(),gs={$style:Yi},_s=D(ms,[[`__cssModules`,gs]])}));function ys(){let e=Et();e.game.observing?.isAnalyzing()?e.game.observing.restorePosition():e.game.selectLineEnd()}var bs=n((()=>{o()}));function xs(e){let t=e??ct();if(t&&Je(t)){if(!Nt()){let e=Xe();return e!==null&&e<=0}let e=re(),t=xt().board?.selectedNode;return t=e?.game.getSelectedNode(),t===null}return!1}var Ss=n((()=>{Ne(),Vt(),Rt(),de(),Ft(),Zt()})),Cs,ws=n((()=>{dn(),fn(),k(),Cs=class extends 
```

<a id="FND-30162"></a>
## FND-30162 — Implementation component game-icons-container

Vue compiled component __name declaration. Name suggests game icons container; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0774
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
=>e.$emit(`click`)},null,8,[`aria-label`,`icon`,`tooltip`]))}})})),fs,ps=n((()=>{ds(),ds(),fs=us})),ms,hs=n((()=>{ms=V({__name:`game-icons-container`,props:{isBughouse:{type:Boolean}},setup(e){let t=e,n=tr(),r=P(()=>({[n.component]:!0,[n.bughouse]:t.isBughouse}));return(e,t)=>(U(),L(`div`,{class:H(r.value)},[G(e.$slots,`left`),t[0]||=z(),R(`div`,{class:H(K(n).spacer)},null,2),t[1]||=z(),G(e.$slots,`right`)],2))}})})),gs,_s,vs=n((()=>{hs(),hs(),Xi(),A(),gs={$style:Yi},_s=D(ms,[[`__cssModules`,gs]])}));function ys(){let e=Et();e.game.observing?.isAnalyzing()?e.game.observing.restorePosition():e.game.selectLineEnd()}var bs=n((()=>{o()}));function xs(e){let t=e??ct();if(t&&Je(t)){if(!Nt()){let e=Xe();return e!==null&&e<=0}let e=re(),t=xt().board?.selectedNode;return t=e?.game.getSelectedNode(),t===null}return!1}var Ss=n((()=>{Ne(),Vt(),Rt(),de(),Ft(),Zt()})),Cs,ws=n((()=>{dn(),fn(),k(),Cs=class extends HTMLElement{constructor(){super(),T(this,`evaluationUpdatedHandler`,void 0),T(this,`evaluationDepth`,void 0),this.evaluationDepth=this.getDepth(),this.evaluationUpdatedHandler=this.evaluationUpdated.bind(this)}connectedCallback(){M.on(`evaluation.update`,this.evaluationUpdatedHandler),this.evaluationDepth=t
```

<a id="FND-30163"></a>
## FND-30163 — Implementation component switch-group

Vue compiled component __name declaration. Name suggests switch group; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0774
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
&&e!==0&&(this.innerHTML=`depth=${e}`,this.evaluationDepth=e)}}})),Ts,Es,Ds=n((()=>{It(),Ts=[`textContent`,`for`],Es=V({__name:`switch-group`,props:{name:{},label:{},modelValue:{type:Boolean},info:{},disabled:{type:Boolean}},emits:[`update:modelValue`],setup(e){return(t,n)=>(U(),L(`div`,{class:H(t.$style.component)},[B(ut,{size:`small`,variant:`secondary`,id:e.name,name:e.name,"model-value":e.modelValue,disabled:e.disabled,"onUpdate:modelValue":n[0]||=e=>t.$emit(`update:modelValue`,e)},null,8,[`id`,`name`,`model-value`,`disabled`]),n[1]||=z(),R(`label`,{textContent:er(e.label),class:H([t.$style.label,{[t.$style.disabled]:e.disabled}]),for:e.name},null,10,Ts)],2))}})})),Os,$,ks=n((()=>{Ds(),Ds(),cr(),A(),Os={$style:sr},$=D(Es,[[`__cssModules`,Os]])})),As,js=n((()=>{E(),ks(),O(),te(),As=V({__name:`switch-menu`,props:{name:{},label:{},value:{type:Boolean},disabled:{type:Boolean},hasMenu:{type:Boolean,default:!0}},emits:[`update:modelValue`],setup(e,{emit:t}){let n=e,r=t;rr(()=>n.value,()=>{!n.value&&i.value&&(i.value=!1)});let i=W(!1);function a(e){i.value=!1,r(`update:modelValue`,e)}return(t,n)=>(U(),L(`div`,{class:H(t.$style.component)},[B($,{label:e.label,"model-value":e.value,name:e.name,disabled:e.d
```

<a id="FND-30164"></a>
## FND-30164 — Implementation component switch-menu

Vue compiled component __name declaration. Name suggests switch menu; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0774
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
s,$,ks=n((()=>{Ds(),Ds(),cr(),A(),Os={$style:sr},$=D(Es,[[`__cssModules`,Os]])})),As,js=n((()=>{E(),ks(),O(),te(),As=V({__name:`switch-menu`,props:{name:{},label:{},value:{type:Boolean},disabled:{type:Boolean},hasMenu:{type:Boolean,default:!0}},emits:[`update:modelValue`],setup(e,{emit:t}){let n=e,r=t;rr(()=>n.value,()=>{!n.value&&i.value&&(i.value=!1)});let i=W(!1);function a(e){i.value=!1,r(`update:modelValue`,e)}return(t,n)=>(U(),L(`div`,{class:H(t.$style.component)},[B($,{label:e.label,"model-value":e.value,name:e.name,disabled:e.disabled,"onUpdate:modelValue":a},null,8,[`label`,`model-value`,`name`,`disabled`]),n[2]||=z(),e.hasMenu&&e.value?(U(),F(Ge,{key:0,modelValue:i.value,"onUpdate:modelValue":n[0]||=e=>i.value=e,id:`engine-settings-switch-menu`,placement:`bottom`,align:`start`},{trigger:q(()=>[B(w,{variant:`ghost`,"aria-label":t.$trans(`More options`),icon:{is:K(Se),variant:`glyph`},"icon-size":24,size:`small`},null,8,[`aria-label`,`icon`])]),popover:q(()=>[R(`div`,{class:H([`cc-popover`,t.$style.dropdown])},[G(t.$slots,`default`)],2)]),_:3},8,[`modelValue`])):I(``,!0)],2))}})})),Ms,Ns,Ps=n((()=>{js(),js(),gr(),A(),Ms={$style:hr},Ns=D(As,[[`__cssModules`,Ms]])}));function Fs(e,t){return U(),
```

<a id="FND-30165"></a>
## FND-30165 — Implementation component evaluation-settings

Vue compiled component __name declaration. Name suggests evaluation settings; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0774
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
Ls={$style:ur},Rs=D(Is,[[`render`,Fs],[`__cssModules`,Ls]])})),Bs,Vs=n((()=>{E(),ws(),ks(),Ps(),zs(),O(),_(),st(),Bs=V({__name:`evaluation-settings`,props:{disabledEvaluationTooltip:{},engineName:{},isEvaluationEnabled:{type:Boolean},isEvaluationBarEnabled:{type:Boolean},isEvaluationLinesEnabled:{type:Boolean},isEvaluationLinesAvailable:{type:Boolean},isEvaluationMenuVisible:{type:Boolean},shouldDisableEvaluationToggles:{type:Boolean}},emits:[`click-settings`,`toggle-bar`,`toggle-lines`,`toggle-evaluation`],setup(e){return x(`wc-evaluation-depth`,Cs),(t,n)=>(U(),L(`div`,{class:H(t.$style.component)},[R(`div`,{class:H(t.$style.switches)},[B(Ns,{name:`evaluationSettings`,label:t.$trans(`Analysis`),value:e.isEvaluationEnabled,disabled:e.shouldDisableEvaluationToggles,"has-menu":e.isEvaluationMenuVisible,"onUpdate:modelValue":n[2]||=e=>t.$emit(`toggle-evaluation`)},{default:q(()=>[B(Rs,null,{default:q(()=>[B($,{label:t.$trans(`Evaluation Bar`),"model-value":e.isEvaluationBarEnabled,name:`evaluationBar`,"onUpdate:modelValue":n[0]||=e=>t.$emit(`toggle-bar`)},null,8,[`label`,`model-value`])]),_:1}),n[4]||=z(),e.isEvaluationLinesAvailable?(U(),F(Rs,{key:0},{default:q(()=>[B($,{label:t.$trans(`Engine Lines`),"
```

<a id="FND-30166"></a>
## FND-30166 — Implementation component evaluation-settings

Vue compiled component __name declaration. Name suggests evaluation settings; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0774
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
),At()})),Ys,Xs=n((()=>{Dt(),Xt(),Ct(),ne(),s(),f(),ht(),Ws(),Ks(),Js(),Ln(),Mn(),Fn(),Ke(),l(),j(),et(),Lt(),r(),Ys=V({__name:`evaluation-settings`,setup(e){let t=pt({engineName(){return d(se(u))?.name},gameModel(){return Re()},gameView(){return qt(this.gameModel)},isEvaluationBarEnabled(){return He(this.gameView,v.EvaluationBar)},isEvaluationLinesEnabled(){return He(this.gameView,v.EvaluationLines)},isEvaluationEnabled(){return this.isEvaluationBarEnabled||this.isEvaluationLinesEnabled},isEvaluationLinesAvailable(){return Nn(this.gameModel)},isEvaluationMenuVisible(){return!jn()},shouldDisableEvaluationToggles(){return Ot(Bt)||Rn(this.gameModel)},disabledEvaluationTooltip(){return Ot(Bt)?m(`Chess engines are disabled by organizer while watching this game.`):m(`Chess engines are disabled while you are playing games.`)}});function n(){me(Ce.Analysis)}function r(){Gs(t.gameModel,!t.isEvaluationBarEnabled)}function i(){qs(t.gameModel,!t.isEvaluationLinesEnabled)}function a(){if(!t.shouldDisableEvaluationToggles){let e=!t.isEvaluationEnabled;Gs(t.gameModel,e),t.isEvaluationLinesAvailable&&qs(t.gameModel,e)}}return(e,o)=>(U(),F(Us,{"disabled-evaluation-tooltip":K(t).disabledEvaluationTooltip,"engine-name"
```

<a id="FND-30167"></a>
## FND-30167 — Implementation component chat-add-friend

Vue compiled component __name declaration. Name suggests chat add friend; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0776
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
,{immediate:!0}):ft(()=>A(e)),pt(()=>wn(e)))}var Dn=n((()=>{_(),Tn()})),On,kn,An=n((()=>{T(),f(),On=[`innerHTML`],kn=V({__name:`chat-add-friend`,props:{username:{},gameChatOpponent:{}},emits:[`add-friend`],setup(e){let t=e,n=P(()=>v(`%username% can only chat with friends.`,{"%username%":`<strong>${t.username}</strong>`}));return(t,r)=>(G(),L(`div`,{class:W(t.$style.component)},[R(`div`,{innerHTML:n.value},null,8,On),r[1]||=z(),e.gameChatOpponent.friendRequestSent?I(``,!0):(G(),L(`div`,{key:0,class:W(t.$style.buttons)},[B(x,{size:`small`,class:W(t.$style.button),label:t.$trans(`Add Friend`),onClick:r[0]||=e=>t.$emit(`add-friend`)},null,8,[`class`,`label`])],2))],2))}})})),jn,Mn,Nn=n((()=>{An(),An(),Ut(),j(),jn={$style:Ht},Mn=k(kn,[[`__cssModules`,jn]])})),Pn,Fn=n((()=>{O(),l(),Pn=V({__name:`chat-warn-shield`,props:{size:{default:`small`}},emits:[`reveal`],setup(e){let t=e,n=P(()=>t.size===`medium`?`cc-paragraph-medium`:`cc-text-small`),r=P(()=>t.size===`medium`?`cc-paragraph-medium-bold`:`cc-text-small-bold`);return(e,t)=>(G(),L(`span`,{class:W(e.$style.shield)},[B(d,{class:W(e.$style.icon),is:J(Te),variant:`glyph`,size:16},null,8,[`class`,`is`]),t[1]||=z(),R(`span`,{class:W([e.$style.text,n.value])},q
```

<a id="FND-30168"></a>
## FND-30168 — Implementation component chat-warn-shield

Vue compiled component __name declaration. Name suggests chat warn shield; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0776
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
}})})),jn,Mn,Nn=n((()=>{An(),An(),Ut(),j(),jn={$style:Ht},Mn=k(kn,[[`__cssModules`,jn]])})),Pn,Fn=n((()=>{O(),l(),Pn=V({__name:`chat-warn-shield`,props:{size:{default:`small`}},emits:[`reveal`],setup(e){let t=e,n=P(()=>t.size===`medium`?`cc-paragraph-medium`:`cc-text-small`),r=P(()=>t.size===`medium`?`cc-paragraph-medium-bold`:`cc-text-small-bold`);return(e,t)=>(G(),L(`span`,{class:W(e.$style.shield)},[B(d,{class:W(e.$style.icon),is:J(Te),variant:`glyph`,size:16},null,8,[`class`,`is`]),t[1]||=z(),R(`span`,{class:W([e.$style.text,n.value])},q(e.$trans(`This message is hidden because it may be offensive.`)),3),t[2]||=z(),R(`button`,{class:W([e.$style.reveal,r.value]),type:`button`,onClick:t[0]||=t=>e.$emit(`reveal`)},q(e.$trans(`Show message`)),3)],2))}})})),In,Ln,Rn=n((()=>{Fn(),Fn(),Ot(),j(),In={$style:Dt},Ln=k(Pn,[[`__cssModules`,In]])})),zn,Bn=n((()=>{He(),ke(),zn=class extends HTMLElement{constructor(...e){super(...e),D(this,`animation`,null),D(this,`onFirstFrameEvent`,this.onFirstFrame.bind(this)),D(this,`autoplay`,!1),D(this,`container`,document.createElement(`div`)),D(this,`height`,null),D(this,`loop`,!1),D(this,`speed`,null),D(this,`src`,``),D(this,`width`,null)}static get observedAttributes(){
```

<a id="FND-30169"></a>
## FND-30169 — Implementation component user-tagline-chat

Vue compiled component __name declaration. Name suggests user tagline chat; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0776
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
.onFirstFrameEvent),this.dispatchEvent(new Event(`animation-started`))}}})),Vn,Hn=n((()=>{u(),Ke(),Je(),ee(),ze(),Vn=V({__name:`user-tagline-chat`,props:{areFriends:{type:Boolean},flair:{},isSelf:{type:Boolean},membership:{},title:{},username:{},showMembershipBadges:{type:Boolean}},setup(e){let t=e,n=Y(),r=P(()=>t.isSelf?n.self:t.areFriends?n.friends:i.value?n.member:a.value?n.moderator:o.value?n.staff:null),i=P(()=>{let{basic:e,diamond:n,gold:r,platinum:i,pro:a}=w;return!![e,r,i,n,a].find(e=>e===t.membership)}),a=P(()=>t.membership===w.moderator),o=P(()=>t.membership===w.staff),s=!!window.chesscom.features?.includes(`premium_badge_redesign`),l=P(()=>t.membership??w.basic),u=P(()=>{if(t.title&&!s)return!1;if(o.value||a.value)return!0;let{diamond:e,gold:n,platinum:r,pro:i}=w,c=[n,r,e,i];return!!(t.showMembershipBadges&&c.find(e=>e===t.membership))}),d=P(()=>!!(t.showMembershipBadges&&t.flair?.id&&c.includes(t.flair.id)));return(t,i)=>(G(),L(`span`,{class:W(J(n).component)},[e.title?(G(),F(pe,{key:0,class:W(J(n).title),title:e.title},null,8,[`class`,`title`])):I(``,!0),i[0]||=z(),u.value?(G(),F(Ge,{key:1,class:W({[J(n)[`user-badge`]]:J(s)}),"is-clickable":!o.value&&!a.value,membership:l.value,size:`smal
```

<a id="FND-30170"></a>
## FND-30170 — Implementation component chat-message

Vue compiled component __name declaration. Name suggests chat message; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0776
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
,$n=n((()=>{O(),tt(),ot(),i(),Rn(),Bn(),Gn(),l(),we(),Ce(),We(),C(),qn(),Yn(),Xn=[`innerHTML`],Zn=[`textContent`],Qn=V({__name:`chat-message`,props:{currentUser:{},hideUsername:{type:Boolean},isBughouseEmoticonsVisible:{type:Boolean,default:!1},message:{},shouldEscapeContent:{type:Boolean},showMembershipBadges:{type:Boolean}},emits:[`remove-message`,`retry`],setup(e,{emit:t}){je(`wc-lottie-animation`,zn);let n=e,i=t,a=Y(),o=K(!1),s=P(()=>({[a.component]:!0,[a.pending]:n.message.pending})),c=P(()=>!n.message.sender||n.currentUser.username===n.message.sender.username),l=P(()=>c.value?n.currentUser:n.message.sender),u=P(()=>{let e=r(n.currentUser.membershipLevel),t=c.value?e:r(l.value.membershipLevel),i=e,a=!n.shouldEscapeContent&&!n.message.pending?n.message.content:De(n.message.content);return a=rt.emotify(a),a=et.emoticonify({text:a,userHasPremium:i,senderHasPremium:t,showEmoji:n.message.animate}),a=Kn(a),n.isBughouseEmoticonsVisible&&(a=Jn(a)),Ee(l.value.membershipLevel)&&(a=a.replace(/https?:\/\/chronograph\.io\/[^\s<]+/g,e=>`<a href="${e}" target="_blank">${e}</a>`)),a}),f=n.message.date?ye.full(new Date(n.message.date)):``;function p(){i(`retry`,{message:n.message})}function m(){i(`remove-message`
```

<a id="FND-30171"></a>
## FND-30171 — Implementation component chat-request

Vue compiled component __name declaration. Name suggests chat request; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0776
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
)=>{$n(),$n(),Zt(),j(),er={$style:Xt},tr=k(Qn,[[`__cssModules`,er]])})),rr,ir,ar=n((()=>{T(),f(),rr=[`innerHTML`],ir=V({__name:`chat-request`,props:{username:{}},emits:[`decline-chat-request`,`approve-chat-request`],setup(e){let t=e,n=P(()=>v(`%username% would like to chat...`,{"%username%":`<strong>${t.username}</strong>`}));return(e,t)=>(G(),L(`div`,{class:W(e.$style.component)},[R(`div`,{innerHTML:n.value},null,8,rr),t[3]||=z(),R(`div`,{class:W(e.$style.buttons)},[B(x,{size:`small`,class:W(e.$style.button),label:e.$trans(`Accept`),onClick:t[0]||=t=>e.$emit(`approve-chat-request`)},null,8,[`class`,`label`]),t[2]||=z(),B(x,{size:`small`,class:W(e.$style.button),label:e.$trans(`Decline`),onClick:t[1]||=t=>e.$emit(`decline-chat-request`)},null,8,[`class`,`label`])],2)],2))}})})),or,sr,cr=n((()=>{ar(),ar(),tn(),j(),or={$style:en},sr=k(ir,[[`__cssModules`,or]])})),lr,ur,dr=n((()=>{T(),f(),lr=[`innerHTML`],ur=V({__name:`chat-unblock`,props:{username:{}},emits:[`unblock`],setup(e){let t=e,n=P(()=>v(`You have blocked %username%.`,{"%username%":`<strong>${t.username}</strong>`}));return(e,t)=>(G(),L(`div`,{class:W(e.$style.component)},[R(`div`,{innerHTML:n.value},null,8,lr),t[1]||=z(),R(`div`,{class:W(e.$sty
```

<a id="FND-30172"></a>
## FND-30172 — Implementation component chat-unblock

Vue compiled component __name declaration. Name suggests chat unblock; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0776
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
)=>{ar(),ar(),tn(),j(),or={$style:en},sr=k(ir,[[`__cssModules`,or]])})),lr,ur,dr=n((()=>{T(),f(),lr=[`innerHTML`],ur=V({__name:`chat-unblock`,props:{username:{}},emits:[`unblock`],setup(e){let t=e,n=P(()=>v(`You have blocked %username%.`,{"%username%":`<strong>${t.username}</strong>`}));return(e,t)=>(G(),L(`div`,{class:W(e.$style.component)},[R(`div`,{innerHTML:n.value},null,8,lr),t[1]||=z(),R(`div`,{class:W(e.$style.buttons)},[B(x,{size:`small`,class:W(e.$style.button),label:e.$trans(`Unblock`),onClick:t[0]||=t=>e.$emit(`unblock`)},null,8,[`class`,`label`])],2)],2))}})})),fr,pr,mr=n((()=>{dr(),dr(),ln(),j(),fr={$style:cn},pr=k(ur,[[`__cssModules`,fr]])})),hr,gr,_r=n((()=>{p(),S(),Pe(),f(),re(),m(),hr=[`innerHTML`],gr=V({__name:`game-over-message`,props:{isPlaying:{type:Boolean},isPlayerRatingVisible:{type:Boolean},timeControl:{},isRated:{type:Boolean},ratingChange:{},newRating:{},whiteTagline:{},blackTagline:{},winnerTagline:{},gameType:{},gameEndReason:{},resultText:{},hasGrudgeScore:{type:Boolean}},setup(e){let t=e,n=P(()=>{let e=[`<strong>${v(`Game Over`)}</strong>`],n=M(t.timeControl),r=t.isRated?v(`%time% Rated`,{"%time%":n}):v(`%time% Unrated`,{"%time%":n}),i=t.resultText.replace(`%winner%`,t.w
```

<a id="FND-30173"></a>
## FND-30173 — Implementation component game-over-message

Vue compiled component __name declaration. Name suggests game over message; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0776
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
,j(),fr={$style:cn},pr=k(ur,[[`__cssModules`,fr]])})),hr,gr,_r=n((()=>{p(),S(),Pe(),f(),re(),m(),hr=[`innerHTML`],gr=V({__name:`game-over-message`,props:{isPlaying:{type:Boolean},isPlayerRatingVisible:{type:Boolean},timeControl:{},isRated:{type:Boolean},ratingChange:{},newRating:{},whiteTagline:{},blackTagline:{},winnerTagline:{},gameType:{},gameEndReason:{},resultText:{},hasGrudgeScore:{type:Boolean}},setup(e){let t=e,n=P(()=>{let e=[`<strong>${v(`Game Over`)}</strong>`],n=M(t.timeControl),r=t.isRated?v(`%time% Rated`,{"%time%":n}):v(`%time% Unrated`,{"%time%":n}),i=t.resultText.replace(`%winner%`,t.winnerTagline);if(e.push(v(`%result% (%rated%)`,{"%result%":i,"%rated%":r})),t.isPlaying&&t.isPlayerRatingVisible&&oe(t.ratingChange)&&t.newRating){let n=t.gameType===`chess`?o(t.timeControl):me(t.gameType);e.push(v(`Your new %1$s% rating is %2$s% (%3$s%).`,{"%1$s%":n,"%2$s%":`<strong>${t.newRating}</strong>`,"%3$s%":y(t.ratingChange)}))}if(t.hasGrudgeScore){let n=v(`%whiteUser% vs. %blackUser%`,{"%whiteUser%":t.whiteTagline,"%blackUser%":t.blackTagline});e.push(`${v(`Match Scores`)} ${n}`)}return e.join(`
`)});return(e,t)=>(G(),L(`div`,{class:W(e.$style.component),innerHTML:n.value},null,10,hr))}})})),vr
```

<a id="FND-30174"></a>
## FND-30174 — Implementation component game-rate-sport-message

Vue compiled component __name declaration. Name suggests game rate sport message; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0776
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}}),xr=[`innerHTML`],Sr=[`textContent`],Cr=[`textContent`],wr=V({__name:`game-rate-sport-message`,props:{isOpponentFriend:{type:Boolean},opponent:{},gameId:{},gameType:{},timeClass:{}},emits:[`add-friend`,`bad-sport`,`block-opponent`,`good-game`,`good-sport`,`report-user`],setup(e,{emit:t}){let n=e,r=t,i=P(()=>Ue(n.opponent.membershipLevel)),o=P(()=>qe.generate(`web_membership_gift`,{username:n.opponent.username})),s=P(()=>v(`Was %opponent% a good sport?`,{"%opponent%":Se({username:n.opponent.username,chessTitle:n.opponent.chessTitle})})),c=K(!1),l=K(!1),u=vt(`element`);function d(e){return{buttonClicked:e,timeClass:n.timeClass,gameType:n.gameType,recipientID:n.opponent.id,recipientIsFriend:n.isOpponentFriend,recipientUsername:n.opponent.username}}function f(){c.value=!0,U(y),r(`good-sport`,d(`goodSportYes`))}function p(){l.value=!0,U(y),r(`bad-sport`,d(`goodSportNo`))}let m=b(()=>r(`report-user`,n.opponent.username)),h=b(()=>r(`block-opponent`,n.gameId)),g=b(()=>r(`good-game`,d(`goodGame`))),_=b(()=>r(`add-friend`,n.opponent.id,n.opponent.uuid));function y(){u.value?.scrollIntoView(!0)}return(t,n)=>(G(),L(`div`,{ref_key:`element`,ref:u,class:W(t.
```

<a id="FND-30175"></a>
## FND-30175 — Implementation component game-start-message

Vue compiled component __name declaration. Name suggests game start message; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0776
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
Tr(),Tr(),bn(),j(),Er={$style:yn},Dr=k(wr,[[`__cssModules`,Er]])})),kr,Ar,jr=n((()=>{p(),S(),f(),kr=[`innerHTML`],Ar=V({__name:`game-start-message`,props:{isPlaying:{type:Boolean},isPlayerRatingVisible:{type:Boolean},timeControl:{},isRated:{type:Boolean},ratingChanges:{default:void 0},whiteTagline:{},blackTagline:{},showTitle:{type:Boolean,default:!0}},setup(e){let t=e,n=P(()=>{let e=[];t.showTitle&&(t.isPlaying?e.push(`<strong>${v(`New Game`)}</strong>`):e.push(`<strong>${v(`Observing Game`)}</strong>`));let n=M(t.timeControl);if(e.push(v(`%1$s% vs. %2$s% (%3$s%)`,{"%1$s%":t.whiteTagline,"%2$s%":t.blackTagline,"%3$s%":t.isRated?n:v(`%time% Unrated`,{"%time%":n})})),t.isPlaying&&t.isPlayerRatingVisible&&t.ratingChanges&&t.isRated){let[n=0,r=0,i=0]=t.ratingChanges;e.push(v(`win %win% / draw %draw% / lose %lose%`,{"%win%":y(n),"%draw%":y(r),"%lose%":y(i)}))}return e.join(`
`)});return(e,t)=>(G(),L(`div`,{class:W(e.$style.component),innerHTML:n.value},null,10,kr))}})})),Mr,Q,Nr=n((()=>{jr(),jr(),Cn(),j(),Mr={$style:Sn},Q=k(Ar,[[`__cssModules`,Mr]])})),Pr,Fr=n((()=>{C(),Nn(),nt(),nr(),cr(),mr(),$e(),br(),Or(),Nr(),ne(),Pr=V({__name:`chat-room`,props:{allowGameChatWith:{},chatMessages:{},currentUser:{},fri
```

<a id="FND-30176"></a>
## FND-30176 — Implementation component chat-room

Vue compiled component __name declaration. Name suggests chat room; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0776
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
={$style:Sn},Q=k(Ar,[[`__cssModules`,Mr]])})),Pr,Fr=n((()=>{C(),Nn(),nt(),nr(),cr(),mr(),$e(),br(),Or(),Nr(),ne(),Pr=V({__name:`chat-room`,props:{allowGameChatWith:{},chatMessages:{},currentUser:{},friendRequestReceived:{type:Boolean,default:!1},friendRequestSent:{type:Boolean,default:!1},inputMaxExtra:{},inputMaxLength:{},inputPreventPaste:{type:Boolean},inputTimeLimit:{},isBughouseEmoticonsVisible:{type:Boolean,default:!1},isBughouseSoundsEnabled:{type:Boolean,default:!1},isDisableChatVisible:{type:Boolean,default:!1},isEnabled:{type:Boolean},isFriend:{type:Boolean,default:!1},isGuest:{type:Boolean,default:!1},isInterlocutorBlocked:{type:Boolean,default:!1},isPlaying:{type:Boolean,default:!1},isReportUserVisible:{type:Boolean,default:!1},isRequestVisible:{type:Boolean,default:!1},listenScroll:{type:Boolean,default:!1},opponentUsername:{},reportSubmitted:{type:Boolean,default:!1},requestingUsername:{},shouldEscapeContent:{type:Boolean},showMembershipBadges:{type:Boolean}},emits:[`approve-chat-request`,`chat-input`,`click-user`,`decline-chat-request`,`emoticon-selected`,`remove-message`,`retry`,`scroll-top`,`toggle-bughouse-sounds`],setup(e,{emit:t}){let n=e,i=t,a=P(()=>{if(n.listenScroll)return{onScr
```

<a id="FND-30177"></a>
## FND-30177 — Implementation component draw-offer

Vue compiled component __name declaration. Name suggests draw offer; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0779
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
e-leave-to":`moves-tab-rating-info-fade-leave-to`,fadeLeaveTo:za}})),Ha,Ua,Wa=t((()=>{k(),it(),Ha=[`textContent`],Ua=W({__name:`draw-offer`,emits:[`ignore-draw-offer`,`accept-draw-offer`,`decline-draw-offer`],setup(e){return(e,t)=>t[0]||(Ur(-1,!0),(t[0]=V(`div`,{class:G(e.$style.component)},[V(`h3`,{class:G([e.$style.title,`cc-heading-x-small`]),textContent:J(e.$trans(`Accept Draw?`))},null,10,Ha),t[2]||=H(),V(`div`,{class:G(e.$style.buttons)},[U(v,{"leading-icon":``,"min-width":``,size:`large`,"aria-label":e.$trans(`Decline Draw`),icon:{is:Y(x),variant:`glyph`},onClick:t=>e.$emit(`decline-draw-offer`)},null,8,[`aria-label`,`icon`,`onClick`]),t[1]||=H(),U(v,{"min-width":``,size:`large`,variant:`primary`,"aria-label":e.$trans(`Accept Draw`),icon:{is:Y(_e),variant:`glyph`},onClick:t=>e.$emit(`accept-draw-offer`)},null,8,[`aria-label`,`icon`,`onClick`])],2),t[3]||=H(),U(v,{"leading-icon":``,size:`small`,icon:{is:Y(x),variant:`glyph`},label:e.$trans(`Disable Draw Offers for this game`),onClick:t=>e.$emit(`ignore-draw-offer`)},null,8,[`icon`,`label`,`onClick`])],2)).cacheIndex=0,Ur(1),t[0])}})})),Ga,Ka,qa=t((()=>{Wa(),Wa(),Vi(),M(),Ga={$style:Bi},Ka=A(Ua,[[`__cssModules`,Ga]])})),Ja,Ya=t((()=>{Ja=W({__name
```

<a id="FND-30178"></a>
## FND-30178 — Implementation component game-review-emphasis

Vue compiled component __name declaration. Name suggests game review emphasis; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0779
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
1),t[0])}})})),Ga,Ka,qa=t((()=>{Wa(),Wa(),Vi(),M(),Ga={$style:Bi},Ka=A(Ua,[[`__cssModules`,Ga]])})),Ja,Ya=t((()=>{Ja=W({__name:`game-review-emphasis`,props:{isEnabled:{type:Boolean},isPadded:{type:Boolean},isShortSidebar:{type:Boolean}},setup(e){return(t,n)=>e.isEnabled?(K(),B(`div`,{key:0,class:G({[t.$style.component]:!0,[t.$style.padded]:e.isPadded,[t.$style.short]:e.isShortSidebar})},[V(`div`,{class:G(t.$style.content)},[q(t.$slots,`default`)],2)],2)):q(t.$slots,`default`,{},void 0,void 0,1)}})})),Xa,Za,Qa=t((()=>{Ya(),Ya(),Ia(),M(),Xa={$style:Fa},Za=A(Ja,[[`__cssModules`,Xa]])})),$a,eo=t((()=>{D(),Nt(),$a=W({__name:`moves-tab-rating-info`,props:{gameModel:{},gameView:{},isPlayerRatingVisible:{type:Boolean}},setup(e){let t=e,n=E({realtimeGame(){return t.gameModel?.isRealtimeGame()?t.gameModel:null},isPlaying(){return!!t.gameView?.isPlaying()},isRated(){return!!this.realtimeGame?.isRated()},timeControl(){return this.realtimeGame?.getTimeControl()},whiteTagline(){return t.gameView?.getPlayerTagline({playerIndex:0,withScore:!0,withRating:t.isPlayerRatingVisible})??``},blackTagline(){return t.gameView?.getPlayerTagline({playerIndex:1,withScore:!0,withRating:t.isPlayerRatingVisible})??``},ratingChanges(
```

<a id="FND-30179"></a>
## FND-30179 — Implementation component moves-tab-rating-info

Vue compiled component __name declaration. Name suggests moves tab rating info; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0779
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
})})),Xa,Za,Qa=t((()=>{Ya(),Ya(),Ia(),M(),Xa={$style:Fa},Za=A(Ja,[[`__cssModules`,Xa]])})),$a,eo=t((()=>{D(),Nt(),$a=W({__name:`moves-tab-rating-info`,props:{gameModel:{},gameView:{},isPlayerRatingVisible:{type:Boolean}},setup(e){let t=e,n=E({realtimeGame(){return t.gameModel?.isRealtimeGame()?t.gameModel:null},isPlaying(){return!!t.gameView?.isPlaying()},isRated(){return!!this.realtimeGame?.isRated()},timeControl(){return this.realtimeGame?.getTimeControl()},whiteTagline(){return t.gameView?.getPlayerTagline({playerIndex:0,withScore:!0,withRating:t.isPlayerRatingVisible})??``},blackTagline(){return t.gameView?.getPlayerTagline({playerIndex:1,withScore:!0,withRating:t.isPlayerRatingVisible})??``},ratingChanges(){let e=this.realtimeGame;if(e)return e.isLiveGameModel()?e.getRatingChanges():e.getRatingChanges(t.gameView?.playingAs??-1)},isMounted(){let e=this.realtimeGame;return!e||e.isBughouse()||!e.isRated()||t.gameView?.getOpponent()?.isComputer?!1:t.isPlayerRatingVisible},isOver(){return!!t.gameView?.isOver()},isFaded(){let e=this.realtimeGame;return e?e.getMovesAmount()>=8:!1}});return(t,r)=>(K(),R(Lr,{"leave-active-class":t.$style[`fade-leave-active`],"leave-to-class":t.$style[`fade-leave-to`]},{de
```
