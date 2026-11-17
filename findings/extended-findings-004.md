# Extended findings

[Master index](../00_MASTER_INDEX.md)

<a id="FND-30180"></a>
## FND-30180 — Implementation component coach-nudge-game-review

Vue compiled component __name declaration. Name suggests coach nudge game review; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0779
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
},trackers:[{tracker:_.Service,name:`Coach Nudge Displayed`}]}})),po,mo,ho=t((()=>{k(),Je(),f(),po=[`aria-label`],mo=W({__name:`coach-nudge-game-review`,props:{isOnlyShowingGameReview:{type:Boolean},isShowingNewGameButtons:{type:Boolean},isQuickAnalysisVisible:{type:Boolean}},emits:[`close-button-click-nudge`,`nudge-displayed`,`accept-button-click-nudge`],setup(e,{emit:t}){let n=e,r=t,i=Hr(!1),a=Hr(!1),o=()=>{i.value=!1},s=()=>{i.value||r(`close-button-click-nudge`)},c=()=>{i.value&&r(`accept-button-click-nudge`)};Vr(()=>{De(()=>{a.value=!0,i.value=!0,r(`nudge-displayed`)},10)});let l=Wr(),u=L(()=>({[l[`game-review`]]:n.isOnlyShowingGameReview,[l[`game-review-button-padding`]]:!n.isQuickAnalysisVisible,[l[`content-animation`]]:a.value})),d=L(()=>({[l[`coach-nudge-height`]]:i.value})),f=L(()=>({[l[`new-game-buttons-visible`]]:n.isShowingNewGameButtons}));return(e,t)=>(K(),B(`div`,{class:G(Y(l).component)},[V(`div`,{class:G(Y(l).content)},[V(`div`,{class:G([Y(l)[`coach-nudge`],d.value]),onTransitionend:s},[V(`button`,{type:`button`,class:G(Y(l).close),"aria-label":e.$trans(`Close`),onClick:o},[U(ee,{is:Y(x),variant:`glyph`,size:20},null,8,[`is`])],10,po),t[0]||=H(),V(`div`,{class:G(Y(l)[`coach-section`]
```

<a id="FND-30181"></a>
## FND-30181 — Implementation component coach-nudge-game-review

Vue compiled component __name declaration. Name suggests coach nudge game review; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0779
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
}var Co=t((()=>{P()})),wo,To=t((()=>{be(),ce(),nt(),so(),lo(),fo(),D(),vo(),bo(),xo(),re(),Co(),P(),jr(),Mr(),r(),wo=W({__name:`coach-nudge-game-review`,setup(e){let t=E({coachSpeechPhrase(){return Pr(b())??Nr()??``},gameView(){return ke()},isOver(){return!!this.gameView?.isOver()},isPlaying(){return!!this.gameView?.isPlaying()},isGameReviewVisible(){return!!this.gameView?.hasComponent(T.GameReviewButton)},isGameReviewEmphasisVisible(){return!!(this.gameView&&So(this.gameView)&&this.gameView.isPlaying())},isQuickAnalysisVisible(){return!!this.gameView?.hasComponent(T.QuickAnalysis)},isGameReviewCoachNudgeVisible(){return!!this.gameView?.hasComponent(T.GameReviewNudge)},selectedCoach(){return mt()}});function n(){Z({accept:!0}),g(oo,{source:`play`,nudgeTo:`gameReview/analysis`,gameType:null,copy:t.coachSpeechPhrase??``})}function r(){t.gameView&&yo(t.gameView),g(co,{source:`play`,nudgeTo:`gameReview/analysis`,gameType:null,copy:t.coachSpeechPhrase??``})}Br(()=>{t.isGameReviewCoachNudgeVisible&&Z({accept:!1})});function i(){Z(),g(uo,{source:`play`,nudgeTo:`gameReview/analysis`,gameType:null,copy:t.coachSpeechPhrase??``})}return(e,a)=>Y(t).selectedCoach?(K(),R(_o,{key:0,"is-only-showing-game-review":!Y(t
```

<a id="FND-30182"></a>
## FND-30182 — Implementation component delete-game-button

Vue compiled component __name declaration. Name suggests delete game button; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0779
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
uttons`,`is-quick-analysis-visible`])):z(``,!0)}})})),Eo,Do=t((()=>{To(),To(),Eo=wo})),Oo,ko=t((()=>{k(),Et(),j(),Oo=W({__name:`delete-game-button`,emits:[`click`],setup(e,{emit:t}){let n=t;return(e,t)=>(K(),R(ze,{id:`delete-game-confirmation`,title:e.$trans(`Delete this game from your Game History?`),"primary-button-props":{label:e.$trans(`Delete`),variant:`danger`},"secondary-button-props":{label:e.$trans(`Cancel`)},onConfirm:t[0]||=e=>n(`click`)},{trigger:X(()=>[U(O,{icon:{is:Y(Be),variant:`glyph`},tooltip:{text:e.$trans(`Delete Game`),closeOnClick:!0}},null,8,[`icon`,`tooltip`])]),_:1},8,[`title`,`primary-button-props`,`secondary-button-props`]))}})})),Ao,jo=t((()=>{ko(),ko(),Ao=Oo})),Q,Mo,No,Po=t((()=>{Dt(),Q=[`textContent`],Mo=[`textContent`],No=W({__name:`draw-request`,setup(e){return(e,t)=>(K(),B(`div`,{class:G(e.$style.component)},[V(`div`,{class:G(e.$style.text)},[V(`span`,{class:G(e.$style.title),textContent:J(e.$trans(`Draw Offered`))},null,10,Q),t[0]||=H(),V(`span`,{class:G(e.$style.subtitle),textContent:J(e.$trans(`Waiting for opponent's response`))},null,10,Mo)],2),t[1]||=H(),U(Ot,{class:G(e.$style.image),size:`medium`,variant:`blocks`},null,8,[`class`])],2))}})})),Fo,Io,Lo=t((()=>{Po()
```

<a id="FND-30183"></a>
## FND-30183 — Implementation component draw-request

Vue compiled component __name declaration. Name suggests draw request; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0779
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
ton-props`]))}})})),Ao,jo=t((()=>{ko(),ko(),Ao=Oo})),Q,Mo,No,Po=t((()=>{Dt(),Q=[`textContent`],Mo=[`textContent`],No=W({__name:`draw-request`,setup(e){return(e,t)=>(K(),B(`div`,{class:G(e.$style.component)},[V(`div`,{class:G(e.$style.text)},[V(`span`,{class:G(e.$style.title),textContent:J(e.$trans(`Draw Offered`))},null,10,Q),t[0]||=H(),V(`span`,{class:G(e.$style.subtitle),textContent:J(e.$trans(`Waiting for opponent's response`))},null,10,Mo)],2),t[1]||=H(),U(Ot,{class:G(e.$style.image),size:`medium`,variant:`blocks`},null,8,[`class`])],2))}})})),Fo,Io,Lo=t((()=>{Po(),Po(),ea(),M(),Fo={$style:$i},Io=A(No,[[`__cssModules`,Fo]])}));function Ro(e,t){return K(),R(Lr,{"enter-active-class":e.$style[`enter-active`],"enter-from-class":e.$style.enter,"leave-active-class":e.$style[`leave-active`],"leave-to-class":e.$style[`leave-to`]},{default:X(()=>[q(e.$slots,`default`)]),_:3},8,[`enter-active-class`,`enter-from-class`,`leave-active-class`,`leave-to-class`])}var zo,Bo,Vo,Ho=t((()=>{qi(),M(),zo={},Bo={$style:Ki},Vo=A(zo,[[`render`,Ro],[`__cssModules`,Bo]])})),Uo,Wo=t((()=>{k(),j(),p(),Uo=W({__name:`grant-time-icon`,props:{disabled:{type:Boolean}},emits:[`click`],setup(e){let t=e,n=L(()=>t.disabled?h(`Can’t ad
```

<a id="FND-30184"></a>
## FND-30184 — Implementation component grant-time-icon

Vue compiled component __name declaration. Name suggests grant time icon; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0779
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
o=t((()=>{qi(),M(),zo={},Bo={$style:Ki},Vo=A(zo,[[`render`,Ro],[`__cssModules`,Bo]])})),Uo,Wo=t((()=>{k(),j(),p(),Uo=W({__name:`grant-time-icon`,props:{disabled:{type:Boolean}},emits:[`click`],setup(e){let t=e,n=L(()=>t.disabled?h(`Can’t add time above the starting time`):ft(`{0} Give %seconds% Seconds|{1} Give %seconds% Second|]1,Inf] Give %seconds% Seconds`,15,{"%seconds%":15}));return(t,r)=>(K(),R(O,{disabled:e.disabled,icon:{is:Y(Xe),variant:`glyph`},"icon-size":20,tooltip:n.value,onClick:r[0]||=e=>t.$emit(`click`)},null,8,[`disabled`,`icon`,`tooltip`]))}})})),Go,Ko=t((()=>{Wo(),Wo(),Go=Uo})),qo,Jo=t((()=>{k(),j(),qo=W({__name:`move-backward-icon`,emits:[`click`],setup(e){return(e,t)=>(K(),R(O,{"aria-label":e.$trans(`Previous Move`),icon:{is:Y(c),variant:`glyph`},"icon-size":20,tooltip:e.$trans(`Previous Move`),onClick:t[0]||=t=>e.$emit(`click`)},null,8,[`aria-label`,`icon`,`tooltip`]))}})})),Yo,Xo=t((()=>{Jo(),Jo(),Yo=qo})),Zo,Qo=t((()=>{k(),j(),Zo=W({__name:`move-end-icon`,emits:[`click`],setup(e){return(e,t)=>(K(),R(O,{"aria-label":e.$trans(`Last Move`),icon:{is:Y(ie),variant:`glyph`},"icon-size":20,tooltip:e.$trans(`Last Move`),onClick:t[0]||=t=>e.$emit(`click`)},null,8,[`aria-label`,`icon`,`t
```

<a id="FND-30185"></a>
## FND-30185 — Implementation component move-backward-icon

Vue compiled component __name declaration. Name suggests move backward icon; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0779
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
mit(`click`)},null,8,[`disabled`,`icon`,`tooltip`]))}})})),Go,Ko=t((()=>{Wo(),Wo(),Go=Uo})),qo,Jo=t((()=>{k(),j(),qo=W({__name:`move-backward-icon`,emits:[`click`],setup(e){return(e,t)=>(K(),R(O,{"aria-label":e.$trans(`Previous Move`),icon:{is:Y(c),variant:`glyph`},"icon-size":20,tooltip:e.$trans(`Previous Move`),onClick:t[0]||=t=>e.$emit(`click`)},null,8,[`aria-label`,`icon`,`tooltip`]))}})})),Yo,Xo=t((()=>{Jo(),Jo(),Yo=qo})),Zo,Qo=t((()=>{k(),j(),Zo=W({__name:`move-end-icon`,emits:[`click`],setup(e){return(e,t)=>(K(),R(O,{"aria-label":e.$trans(`Last Move`),icon:{is:Y(ie),variant:`glyph`},"icon-size":20,tooltip:e.$trans(`Last Move`),onClick:t[0]||=t=>e.$emit(`click`)},null,8,[`aria-label`,`icon`,`tooltip`]))}})})),$o,es=t((()=>{Qo(),Qo(),$o=Zo})),ts,ns=t((()=>{k(),j(),ts=W({__name:`move-forward-icon`,emits:[`click`],setup(e){return(e,t)=>(K(),R(O,{"aria-label":e.$trans(`Next Move`),icon:{is:Y(Se),variant:`glyph`},"icon-size":20,tooltip:e.$trans(`Next Move`),onClick:t[0]||=t=>e.$emit(`click`)},null,8,[`aria-label`,`icon`,`tooltip`]))}})})),rs,is=t((()=>{ns(),ns(),rs=ts})),as,os=t((()=>{k(),j(),as=W({__name:`move-start-icon`,emits:[`click`],setup(e){return(e,t)=>(K(),R(O,{"aria-label":e.$trans(`First M
```

<a id="FND-30186"></a>
## FND-30186 — Implementation component move-end-icon

Vue compiled component __name declaration. Name suggests move end icon; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0779
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
t(`click`)},null,8,[`aria-label`,`icon`,`tooltip`]))}})})),Yo,Xo=t((()=>{Jo(),Jo(),Yo=qo})),Zo,Qo=t((()=>{k(),j(),Zo=W({__name:`move-end-icon`,emits:[`click`],setup(e){return(e,t)=>(K(),R(O,{"aria-label":e.$trans(`Last Move`),icon:{is:Y(ie),variant:`glyph`},"icon-size":20,tooltip:e.$trans(`Last Move`),onClick:t[0]||=t=>e.$emit(`click`)},null,8,[`aria-label`,`icon`,`tooltip`]))}})})),$o,es=t((()=>{Qo(),Qo(),$o=Zo})),ts,ns=t((()=>{k(),j(),ts=W({__name:`move-forward-icon`,emits:[`click`],setup(e){return(e,t)=>(K(),R(O,{"aria-label":e.$trans(`Next Move`),icon:{is:Y(Se),variant:`glyph`},"icon-size":20,tooltip:e.$trans(`Next Move`),onClick:t[0]||=t=>e.$emit(`click`)},null,8,[`aria-label`,`icon`,`tooltip`]))}})})),rs,is=t((()=>{ns(),ns(),rs=ts})),as,os=t((()=>{k(),j(),as=W({__name:`move-start-icon`,emits:[`click`],setup(e){return(e,t)=>(K(),R(O,{"aria-label":e.$trans(`First Move`),icon:{is:Y(ae),variant:`glyph`},"icon-size":20,tooltip:e.$trans(`First Move`),onClick:t[0]||=t=>e.$emit(`click`)},null,8,[`aria-label`,`icon`,`tooltip`]))}})})),ss,cs=t((()=>{os(),os(),ss=as}));function ls(){let e=document.createElement(`form`);Object.assign(e,{action:N.generate(`web_classroom`,{},!0),method:`post`,target:`_blank`}
```

<a id="FND-30187"></a>
## FND-30187 — Implementation component move-forward-icon

Vue compiled component __name declaration. Name suggests move forward icon; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0779
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
t(`click`)},null,8,[`aria-label`,`icon`,`tooltip`]))}})})),$o,es=t((()=>{Qo(),Qo(),$o=Zo})),ts,ns=t((()=>{k(),j(),ts=W({__name:`move-forward-icon`,emits:[`click`],setup(e){return(e,t)=>(K(),R(O,{"aria-label":e.$trans(`Next Move`),icon:{is:Y(Se),variant:`glyph`},"icon-size":20,tooltip:e.$trans(`Next Move`),onClick:t[0]||=t=>e.$emit(`click`)},null,8,[`aria-label`,`icon`,`tooltip`]))}})})),rs,is=t((()=>{ns(),ns(),rs=ts})),as,os=t((()=>{k(),j(),as=W({__name:`move-start-icon`,emits:[`click`],setup(e){return(e,t)=>(K(),R(O,{"aria-label":e.$trans(`First Move`),icon:{is:Y(ae),variant:`glyph`},"icon-size":20,tooltip:e.$trans(`First Move`),onClick:t[0]||=t=>e.$emit(`click`)},null,8,[`aria-label`,`icon`,`tooltip`]))}})})),ss,cs=t((()=>{os(),os(),ss=as}));function ls(){let e=document.createElement(`form`);Object.assign(e,{action:N.generate(`web_classroom`,{},!0),method:`post`,target:`_blank`});let t=document.createElement(`input`);t.setAttribute(`name`,`createRoomFromPgn`),t.setAttribute(`value`,JSON.stringify({pgn:u().game.getPGN()})),e.append(t),document.body.appendChild(e),e.submit(),document.body.removeChild(e)}var us=t((()=>{w(),pe(),window.chesscom=window.chesscom||{},window.chesscom.routes=window.chesscom.
```

<a id="FND-30188"></a>
## FND-30188 — Implementation component move-start-icon

Vue compiled component __name declaration. Name suggests move start icon; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0779
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
t(`click`)},null,8,[`aria-label`,`icon`,`tooltip`]))}})})),rs,is=t((()=>{ns(),ns(),rs=ts})),as,os=t((()=>{k(),j(),as=W({__name:`move-start-icon`,emits:[`click`],setup(e){return(e,t)=>(K(),R(O,{"aria-label":e.$trans(`First Move`),icon:{is:Y(ae),variant:`glyph`},"icon-size":20,tooltip:e.$trans(`First Move`),onClick:t[0]||=t=>e.$emit(`click`)},null,8,[`aria-label`,`icon`,`tooltip`]))}})})),ss,cs=t((()=>{os(),os(),ss=as}));function ls(){let e=document.createElement(`form`);Object.assign(e,{action:N.generate(`web_classroom`,{},!0),method:`post`,target:`_blank`});let t=document.createElement(`input`);t.setAttribute(`name`,`createRoomFromPgn`),t.setAttribute(`value`,JSON.stringify({pgn:u().game.getPGN()})),e.append(t),document.body.appendChild(e),e.submit(),document.body.removeChild(e)}var us=t((()=>{w(),pe(),window.chesscom=window.chesscom||{},window.chesscom.routes=window.chesscom.routes||{},Object.assign(window.chesscom.routes,{web_classroom:{tokens:[[`text`,`/classroom`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu
```

<a id="FND-30189"></a>
## FND-30189 — Implementation component live-game-buttons

Vue compiled component __name declaration. Name suggests live game buttons; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0779
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}}),ys=W({__name:`live-game-buttons`,setup(e){let t=E({gameModel(){return b()},gameView(){return wt(this.gameModel)},isAtEndOfLine(){return Ct(this.gameView?.boardRef)},isAtBeginningOfLine(){return On(this.gameView?.boardRef)},confirmResign(){return Sr(this.gameModel)},isPlaying(){return!!this.gameView?.isPlaying()},isOver(){return!!this.gameView?.isOver()},hasOutgoingDrawOffer(){return!!this.gameView?.playerActions?.hasSentDrawOffer},hasActiveDrawOffer(){return!!this.gameView?.playerActions?.hasReceivedDrawOffer},hasDeclinedOutgoingDrawOffer(){return!!this.gameView?.playerActions?.hasOpponentDeclinedDrawOffer},isFocusMode(){return Ce()},isCompetitionGame(){return!!(this.gameModel?.isLiveGameModel()&&this.gameModel.isCompetitionGame())},showGrantTimeButton(){return!!this.gameView?.playerActions?.canGrantTime},isGrantTimeDisabled(){return!this.showGrantTimeButton||!this.gameModel||!this.gameView?!1:he(this.gameModel,{playerIndex:1-this.gameView.playingAs,currentTime:dt()})+15e3>te(this.gameModel)},isBughouse(){return!!this.gameModel?.isBughouse()},drawOfferMoves(){return this.gameView?.playerAc
```

<a id="FND-30190"></a>
## FND-30190 — Implementation component live-game-tab

Vue compiled component __name declaration. Name suggests live game tab; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0779
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
),Rt(),wn(),Qe(),Xn(),_t(),yt(),As(),Wt(),Ln(),Ee(),l(),Ar(),Co(),ot(),P(),Oe(),me(),Bn(),r(),pr(),Ms(),Ve(),Hn(),Ns=W({__name:`live-game-tab`,setup(e){let t=fe(),{width:n,height:r}=Re(),i=E({boardId(){return Tt()},scrollContainerId(){return`live-game-tab-scroll-container`},isPremiumUser(){return bt()?.isPremium()??!1},gameModel(){return b()},gameView(){return wt(this.gameModel)},displayResult(){return kr(this.gameModel)?`0-0`:void 0},isArchiveGame(){return!!this.gameModel?.isDailyGameModel()},liveArena(){return this.gameModel?.isLiveGameModel()&&this.gameModel.isArenaGame()?d(this.gameModel.getArenaId()):null},currentTime(){return gt()},tabs(){return this.gameModel?Sn(this.gameModel):[]},selectedTab(){return this.gameView?.selectedGameTab??m.Moves},isPartnerTabSelected(){return this.selectedTab===m.Bughouse},isMovesTabSelected(){return this.selectedTab===m.Moves},isPlayerRatingVisible(){return xt(this.gameModel)},isInfoTabSelected(){return this.selectedTab===m.Info},isOpeningsTabSelected(){return this.selectedTab===m.Openings},isChatTabSelected(){return this.selectedTab===m.Chat},isChatTabVisible(){return this.tabs.some(e=>e.id===m.Chat)},hasStreamingPlayers(){return this.gameModel?js(this.gameModel)
```

<a id="FND-30191"></a>
## FND-30191 — Implementation component leaderboard-ad

Vue compiled component __name declaration. Name suggests leaderboard ad; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0780
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
e.isUserGeneratedContent?.()&&bf(`page-content`)}var mE=t((()=>{tr(),Gc()})),hE,gE,_E=t((()=>{vo(),$c(),hE=[`id`],gE=K({__name:`leaderboard-ad`,props:{slotId:{},variant:{default:`leaderboard`}},setup(e){return(t,n)=>(J(),H(`div`,{class:q([t.$style.component,t.$style[e.variant],{[t.$style[`with-report-ad`]]:Z(Cn)()}])},[U(`div`,{class:q(t.$style.slot),id:e.slotId},null,10,hE),n[0]||=W(),Z(Cn)()?(J(),B(ip,{key:0,"slot-id":e.slotId},null,8,[`slot-id`])):V(``,!0)],2))}})})),vE,yE,bE=t((()=>{_E(),_E(),og(),I(),vE={$style:ag},yE=j(gE,[[`__cssModules`,vE]])})),xE,SE=t((()=>{Ed(),bE(),xE=K({__name:`leaderboard-atf-ad`,setup(e){return(e,t)=>(J(),B(yE,{"slot-id":Z(Xf).leaderboardAtf},null,8,[`slot-id`]))}})})),CE,wE=t((()=>{SE(),SE(),CE=xE})),TE,EE=t((()=>{Ed(),bE(),TE=K({__name:`leaderboard-btf-ad`,setup(e){return(e,t)=>(J(),B(yE,{"slot-id":Z(Xf).leaderboardBtf},null,8,[`slot-id`]))}})})),DE,OE=t((()=>{EE(),EE(),DE=TE})),kE,AE,jE=t((()=>{vo(),te(),$c(),kE=[`id`],AE=K({__name:`medium-rectangle-ad`,props:{slotId:{}},setup(e){return(t,n)=>(J(),H(`div`,{class:q([t.$style.component,{[t.$style[`with-report-ad`]]:Z(Cn)()}])},[U(`div`,{class:q(t.$style.slot),id:e.slotId},null,10,kE),n[0]||=W(),G(Ji),n[1]||=W(),Z(Cn)()
```

<a id="FND-30192"></a>
## FND-30192 — Implementation component leaderboard-atf-ad

Vue compiled component __name declaration. Name suggests leaderboard atf ad; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0780
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
)})),vE,yE,bE=t((()=>{_E(),_E(),og(),I(),vE={$style:ag},yE=j(gE,[[`__cssModules`,vE]])})),xE,SE=t((()=>{Ed(),bE(),xE=K({__name:`leaderboard-atf-ad`,setup(e){return(e,t)=>(J(),B(yE,{"slot-id":Z(Xf).leaderboardAtf},null,8,[`slot-id`]))}})})),CE,wE=t((()=>{SE(),SE(),CE=xE})),TE,EE=t((()=>{Ed(),bE(),TE=K({__name:`leaderboard-btf-ad`,setup(e){return(e,t)=>(J(),B(yE,{"slot-id":Z(Xf).leaderboardBtf},null,8,[`slot-id`]))}})})),DE,OE=t((()=>{EE(),EE(),DE=TE})),kE,AE,jE=t((()=>{vo(),te(),$c(),kE=[`id`],AE=K({__name:`medium-rectangle-ad`,props:{slotId:{}},setup(e){return(t,n)=>(J(),H(`div`,{class:q([t.$style.component,{[t.$style[`with-report-ad`]]:Z(Cn)()}])},[U(`div`,{class:q(t.$style.slot),id:e.slotId},null,10,kE),n[0]||=W(),G(Ji),n[1]||=W(),Z(Cn)()?(J(),B(ip,{key:0,"slot-id":e.slotId},null,8,[`slot-id`])):V(``,!0)],2))}})})),ME,NE,PE=t((()=>{jE(),jE(),Vg(),I(),ME={$style:Bg},NE=j(AE,[[`__cssModules`,ME]])})),FE,IE=t((()=>{Ed(),PE(),FE=K({__name:`medium-rectangle-atf-ad`,setup(e){return(e,t)=>(J(),B(NE,{"slot-id":Z(Xf).mediumRectangleAtf},null,8,[`slot-id`]))}})})),LE,RE=t((()=>{IE(),IE(),LE=FE})),zE,BE=t((()=>{Ed(),PE(),zE=K({__name:`medium-rectangle-btf-ad`,setup(e){return(e,t)=>(J(),B(NE,{"slot-id":Z(Xf).me
```

<a id="FND-30193"></a>
## FND-30193 — Implementation component leaderboard-btf-ad

Vue compiled component __name declaration. Name suggests leaderboard btf ad; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0780
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
lot-id":Z(Xf).leaderboardAtf},null,8,[`slot-id`]))}})})),CE,wE=t((()=>{SE(),SE(),CE=xE})),TE,EE=t((()=>{Ed(),bE(),TE=K({__name:`leaderboard-btf-ad`,setup(e){return(e,t)=>(J(),B(yE,{"slot-id":Z(Xf).leaderboardBtf},null,8,[`slot-id`]))}})})),DE,OE=t((()=>{EE(),EE(),DE=TE})),kE,AE,jE=t((()=>{vo(),te(),$c(),kE=[`id`],AE=K({__name:`medium-rectangle-ad`,props:{slotId:{}},setup(e){return(t,n)=>(J(),H(`div`,{class:q([t.$style.component,{[t.$style[`with-report-ad`]]:Z(Cn)()}])},[U(`div`,{class:q(t.$style.slot),id:e.slotId},null,10,kE),n[0]||=W(),G(Ji),n[1]||=W(),Z(Cn)()?(J(),B(ip,{key:0,"slot-id":e.slotId},null,8,[`slot-id`])):V(``,!0)],2))}})})),ME,NE,PE=t((()=>{jE(),jE(),Vg(),I(),ME={$style:Bg},NE=j(AE,[[`__cssModules`,ME]])})),FE,IE=t((()=>{Ed(),PE(),FE=K({__name:`medium-rectangle-atf-ad`,setup(e){return(e,t)=>(J(),B(NE,{"slot-id":Z(Xf).mediumRectangleAtf},null,8,[`slot-id`]))}})})),LE,RE=t((()=>{IE(),IE(),LE=FE})),zE,BE=t((()=>{Ed(),PE(),zE=K({__name:`medium-rectangle-btf-ad`,setup(e){return(e,t)=>(J(),B(NE,{"slot-id":Z(Xf).mediumRectangleBtf},null,8,[`slot-id`]))}})})),VE,HE=t((()=>{BE(),BE(),VE=zE}));function UE(e){tt(di.WithUnd,e)}var WE=t((()=>{ju(),Ct()}));function GE(e,t){Tf([t]),setTimeout(hf,10)}va
```

<a id="FND-30194"></a>
## FND-30194 — Implementation component medium-rectangle-ad

Vue compiled component __name declaration. Name suggests medium rectangle ad; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0780
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
erboardBtf},null,8,[`slot-id`]))}})})),DE,OE=t((()=>{EE(),EE(),DE=TE})),kE,AE,jE=t((()=>{vo(),te(),$c(),kE=[`id`],AE=K({__name:`medium-rectangle-ad`,props:{slotId:{}},setup(e){return(t,n)=>(J(),H(`div`,{class:q([t.$style.component,{[t.$style[`with-report-ad`]]:Z(Cn)()}])},[U(`div`,{class:q(t.$style.slot),id:e.slotId},null,10,kE),n[0]||=W(),G(Ji),n[1]||=W(),Z(Cn)()?(J(),B(ip,{key:0,"slot-id":e.slotId},null,8,[`slot-id`])):V(``,!0)],2))}})})),ME,NE,PE=t((()=>{jE(),jE(),Vg(),I(),ME={$style:Bg},NE=j(AE,[[`__cssModules`,ME]])})),FE,IE=t((()=>{Ed(),PE(),FE=K({__name:`medium-rectangle-atf-ad`,setup(e){return(e,t)=>(J(),B(NE,{"slot-id":Z(Xf).mediumRectangleAtf},null,8,[`slot-id`]))}})})),LE,RE=t((()=>{IE(),IE(),LE=FE})),zE,BE=t((()=>{Ed(),PE(),zE=K({__name:`medium-rectangle-btf-ad`,setup(e){return(e,t)=>(J(),B(NE,{"slot-id":Z(Xf).mediumRectangleBtf},null,8,[`slot-id`]))}})})),VE,HE=t((()=>{BE(),BE(),VE=zE}));function UE(e){tt(di.WithUnd,e)}var WE=t((()=>{ju(),Ct()}));function GE(e,t){Tf([t]),setTimeout(hf,10)}var KE=t((()=>{au(),dr()}));function qE(e,t){return e/t>=2?Xf.skyscraperWide:Xf.skyscraper}var JE=t((()=>{Ed()})),YE,XE,ZE=t((()=>{vo(),te(),$c(),YE=[`id`],XE=K({__name:`skyscraper-ad`,props:{id:{}},setu
```

<a id="FND-30195"></a>
## FND-30195 — Implementation component medium-rectangle-atf-ad

Vue compiled component __name declaration. Name suggests medium rectangle atf ad; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0780
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
)})),ME,NE,PE=t((()=>{jE(),jE(),Vg(),I(),ME={$style:Bg},NE=j(AE,[[`__cssModules`,ME]])})),FE,IE=t((()=>{Ed(),PE(),FE=K({__name:`medium-rectangle-atf-ad`,setup(e){return(e,t)=>(J(),B(NE,{"slot-id":Z(Xf).mediumRectangleAtf},null,8,[`slot-id`]))}})})),LE,RE=t((()=>{IE(),IE(),LE=FE})),zE,BE=t((()=>{Ed(),PE(),zE=K({__name:`medium-rectangle-btf-ad`,setup(e){return(e,t)=>(J(),B(NE,{"slot-id":Z(Xf).mediumRectangleBtf},null,8,[`slot-id`]))}})})),VE,HE=t((()=>{BE(),BE(),VE=zE}));function UE(e){tt(di.WithUnd,e)}var WE=t((()=>{ju(),Ct()}));function GE(e,t){Tf([t]),setTimeout(hf,10)}var KE=t((()=>{au(),dr()}));function qE(e,t){return e/t>=2?Xf.skyscraperWide:Xf.skyscraper}var JE=t((()=>{Ed()})),YE,XE,ZE=t((()=>{vo(),te(),$c(),YE=[`id`],XE=K({__name:`skyscraper-ad`,props:{id:{}},setup(e){return(t,n)=>(J(),H(`div`,{class:q([t.$style.component,{[t.$style[`with-report-ad`]]:Z(Cn)()}])},[U(`div`,{class:q(t.$style.slot),id:e.id},null,10,YE),n[0]||=W(),G(Ji),n[1]||=W(),Z(Cn)()?(J(),B(ip,{key:0,"slot-id":e.id},null,8,[`slot-id`])):V(``,!0)],2))}})})),QE,$E,eD=t((()=>{ZE(),ZE(),Kg(),I(),QE={$style:Gg},$E=j(XE,[[`__cssModules`,QE]])})),tD,nD=t((()=>{hl(),WE(),KE(),JE(),hs(),eD(),tD=K({__name:`skyscraper-ad`,setup(e){let t=l
```

<a id="FND-30196"></a>
## FND-30196 — Implementation component medium-rectangle-btf-ad

Vue compiled component __name declaration. Name suggests medium rectangle btf ad; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0780
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
id":Z(Xf).mediumRectangleAtf},null,8,[`slot-id`]))}})})),LE,RE=t((()=>{IE(),IE(),LE=FE})),zE,BE=t((()=>{Ed(),PE(),zE=K({__name:`medium-rectangle-btf-ad`,setup(e){return(e,t)=>(J(),B(NE,{"slot-id":Z(Xf).mediumRectangleBtf},null,8,[`slot-id`]))}})})),VE,HE=t((()=>{BE(),BE(),VE=zE}));function UE(e){tt(di.WithUnd,e)}var WE=t((()=>{ju(),Ct()}));function GE(e,t){Tf([t]),setTimeout(hf,10)}var KE=t((()=>{au(),dr()}));function qE(e,t){return e/t>=2?Xf.skyscraperWide:Xf.skyscraper}var JE=t((()=>{Ed()})),YE,XE,ZE=t((()=>{vo(),te(),$c(),YE=[`id`],XE=K({__name:`skyscraper-ad`,props:{id:{}},setup(e){return(t,n)=>(J(),H(`div`,{class:q([t.$style.component,{[t.$style[`with-report-ad`]]:Z(Cn)()}])},[U(`div`,{class:q(t.$style.slot),id:e.id},null,10,YE),n[0]||=W(),G(Ji),n[1]||=W(),Z(Cn)()?(J(),B(ip,{key:0,"slot-id":e.id},null,8,[`slot-id`])):V(``,!0)],2))}})})),QE,$E,eD=t((()=>{ZE(),ZE(),Kg(),I(),QE={$style:Gg},$E=j(XE,[[`__cssModules`,QE]])})),tD,nD=t((()=>{hl(),WE(),KE(),JE(),hs(),eD(),tD=K({__name:`skyscraper-ad`,setup(e){let t=lc(),n=z(()=>qE(t.width.value,t.height.value));return bh(()=>$i(),UE,{immediate:!0}),bh(()=>n.value,GE),(e,t)=>Z($i)()?(J(),B($E,{id:n.value,key:n.value},null,8,[`id`])):V(``,!0)}})})),rD,iD=t(
```

<a id="FND-30197"></a>
## FND-30197 — Implementation component skyscraper-ad

Vue compiled component __name declaration. Name suggests skyscraper ad; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0780
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
t){return e/t>=2?Xf.skyscraperWide:Xf.skyscraper}var JE=t((()=>{Ed()})),YE,XE,ZE=t((()=>{vo(),te(),$c(),YE=[`id`],XE=K({__name:`skyscraper-ad`,props:{id:{}},setup(e){return(t,n)=>(J(),H(`div`,{class:q([t.$style.component,{[t.$style[`with-report-ad`]]:Z(Cn)()}])},[U(`div`,{class:q(t.$style.slot),id:e.id},null,10,YE),n[0]||=W(),G(Ji),n[1]||=W(),Z(Cn)()?(J(),B(ip,{key:0,"slot-id":e.id},null,8,[`slot-id`])):V(``,!0)],2))}})})),QE,$E,eD=t((()=>{ZE(),ZE(),Kg(),I(),QE={$style:Gg},$E=j(XE,[[`__cssModules`,QE]])})),tD,nD=t((()=>{hl(),WE(),KE(),JE(),hs(),eD(),tD=K({__name:`skyscraper-ad`,setup(e){let t=lc(),n=z(()=>qE(t.width.value,t.height.value));return bh(()=>$i(),UE,{immediate:!0}),bh(()=>n.value,GE),(e,t)=>Z($i)()?(J(),B($E,{id:n.value,key:n.value},null,8,[`id`])):V(``,!0)}})})),rD,iD=t((()=>{nD(),nD(),rD=tD}));async function aD(){let e={skyscraper:`#sidebar-ad`,leaderboardAtf:`#leaderboard-atf-ad`,leaderboardBtf:`#leaderboard-btf-ad`,mediumRectangleAtf:`#medium-rectangle-atf-ad`,mediumRectangleBtf:`#medium-rectangle-btf-ad`},t={};document.querySelector(e.skyscraper)&&(t[e.skyscraper]=rD),document.querySelector(e.leaderboardAtf)&&(t[e.leaderboardAtf]=CE),document.querySelector(e.leaderboardBtf)&&(t[e.leade
```

<a id="FND-30198"></a>
## FND-30198 — Implementation component skyscraper-ad

Vue compiled component __name declaration. Name suggests skyscraper ad; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0780
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
>{ZE(),ZE(),Kg(),I(),QE={$style:Gg},$E=j(XE,[[`__cssModules`,QE]])})),tD,nD=t((()=>{hl(),WE(),KE(),JE(),hs(),eD(),tD=K({__name:`skyscraper-ad`,setup(e){let t=lc(),n=z(()=>qE(t.width.value,t.height.value));return bh(()=>$i(),UE,{immediate:!0}),bh(()=>n.value,GE),(e,t)=>Z($i)()?(J(),B($E,{id:n.value,key:n.value},null,8,[`id`])):V(``,!0)}})})),rD,iD=t((()=>{nD(),nD(),rD=tD}));async function aD(){let e={skyscraper:`#sidebar-ad`,leaderboardAtf:`#leaderboard-atf-ad`,leaderboardBtf:`#leaderboard-btf-ad`,mediumRectangleAtf:`#medium-rectangle-atf-ad`,mediumRectangleBtf:`#medium-rectangle-btf-ad`},t={};document.querySelector(e.skyscraper)&&(t[e.skyscraper]=rD),document.querySelector(e.leaderboardAtf)&&(t[e.leaderboardAtf]=CE),document.querySelector(e.leaderboardBtf)&&(t[e.leaderboardBtf]=DE),document.querySelector(e.mediumRectangleAtf)&&(t[e.mediumRectangleAtf]=LE),document.querySelector(e.mediumRectangleBtf)&&(t[e.mediumRectangleBtf]=VE),await Td(t)}var oD=t((()=>{wE(),OE(),RE(),HE(),iD(),m()}));function sD(){let e=Go();!p_()||e.adTimingMetricsRecorded||(e.adTimingMetricsRecorded=!0,un(`adsClientStart`,performance.now()),window.googletag=window.googletag||{cmd:[]},window.googletag.cmd.push(()=>{un(`adsTagLoade
```

<a id="FND-30199"></a>
## FND-30199 — Implementation component board-controls

Vue compiled component __name declaration. Name suggests board controls; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0780
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
s:tA,hooks:Object.assign({onBeforeInit(){xs()}},e)})}var iA=t((()=>{m(),xl(),aE(),nA()})),aA,oA=t((()=>{zd(),jf(),aA=K({__name:`board-controls`,props:{isBoardImagesPaletteVisible:{type:Boolean},isMenuIconVisible:{type:Boolean},isFocusModeSupported:{type:Boolean}},emits:[`click-board-images-palette`,`click-settings`,`click-focus`,`click-theatre`,`click-flip`,`click-menu`],setup(e){let t=window.chesscom.features.includes(`cc_ds_light_mode`);return(n,r)=>(J(),H(`div`,{class:q({"dark-mode":!Z(t)})},[G(Ad,{id:`board-controls-settings`,class:q(n.$style.button),tooltip:{text:n.$trans(`Settings`),position:`right`},size:`small`,icon:{variant:`glyph`,is:Z(El)},"icon-size":16,onClick:r[0]||=e=>n.$emit(`click-settings`)},null,8,[`class`,`tooltip`,`icon`]),r[6]||=W(),Y(n.$slots,`voice-move-icon`,{hoverClass:n.$style.hover}),r[7]||=W(),e.isFocusModeSupported?(J(),B(Ad,{key:0,id:`board-controls-focus`,class:q([n.$style.button,n.$style.hover]),tooltip:{text:n.$trans(`Focus Mode`),position:`right`},size:`small`,icon:{variant:`glyph`,is:Z(sp)},"icon-size":16,onClick:r[1]||=e=>n.$emit(`click-focus`)},null,8,[`class`,`tooltip`,`icon`])):V(``,!0),r[8]||=W(),e.isFocusModeSupported?(J(),B(Ad,{key:1,id:`board-controls-theatr
```

<a id="FND-30200"></a>
## FND-30200 — Implementation component voice-move-icon

Vue compiled component __name declaration. Name suggests voice move icon; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0780
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
t((()=>{oA(),oA(),Hv(),I(),sA={$style:Vv},cA=j(aA,[[`__cssModules`,sA]])})),uA,dA=t((()=>{zd(),jf(),d(),mp(),yc(),uA=K({__name:`voice-move-icon`,props:{hoverClass:{},voiceRecognizerStatus:{},voiceMicrophoneStatus:{}},emits:[`click`],setup(e){let t=e,n=Q(),r=z(()=>{switch(t.voiceRecognizerStatus){case F.Disabled:return h(`Click to enable voice move`);case F.Enabled:case F.Loading:return h(`Enabling voice move...`);default:break}switch(t.voiceMicrophoneStatus){case Zu.Pending:return h(`Waiting for microphone permission`);case Zu.Denied:return h(`Microphone permission denied`);default:return h(`Hold SPACE to speak your move`)}}),i=z(()=>{switch(t.voiceRecognizerStatus){case F.Disabled:return Mi;default:break}switch(t.voiceMicrophoneStatus){case Zu.Denied:return Pn;default:return Ir}}),a=z(()=>{switch(t.voiceMicrophoneStatus){case Zu.Denied:return n.error;default:break}switch(t.voiceRecognizerStatus){case F.Listening:case F.Starting:return n.listening;case F.Stopping:case F.Idle:return n.idle;case F.Error:return n.error;default:return``}}),o=z(()=>({[n.button]:!0,[a.value]:!0,[t.hoverClass]:t.voiceRecognizerStatus===F.Disabled}));return(e,t)=>(J(),B(Ad,{id:`board-controls-voice-move`,class:q(o.value),tool
```

<a id="FND-30201"></a>
## FND-30201 — Implementation component board-controls

Vue compiled component __name declaration. Name suggests board controls; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0780
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
=>{lm()})),CA,wA=t((()=>{lO(),cl(),_u(),lA(),mA(),Xc(),So(),Zm(),Mr(),gA(),vA(),Qa(),Oo(),Ld(),f(),bA(),SA(),ao(),CA=K({__name:`board-controls`,setup(e){let t=cA,n=Zr(),r=Nc({activeBoard(){return Us()},isBoardImagesPaletteVisible(){return!!this.activeBoard},isMenuIconVisible(){return _A()||ya()},isFocusModeSupported(){return n.value&&hA()},voiceMicrophoneStatus(){return xA()},voiceRecognizerStatus(){return Sn()}});function i({target:e}){cO(e)}function a(){if(!v()){zt();return}fn()}function o(){ce()}function s(){Dn()}function c(){Ie()}function ee(){Ie(!1)}function te(){yA()}return(e,ne)=>(J(),B(Z(t),{"is-board-images-palette-visible":Z(r).isBoardImagesPaletteVisible,"is-menu-icon-visible":Z(r).isMenuIconVisible,"is-focus-mode-supported":Z(r).isFocusModeSupported,onClickBoardImagesPalette:i,onClickSettings:a,onClickFocus:s,onClickTheatre:c,onClickFlip:o,onClickMenu:ee},rh({_:2},[Z(n)?{name:`voice-move-icon`,fn:$(({hoverClass:e})=>[G(pA,{"hover-class":e,"voice-microphone-status":Z(r).voiceMicrophoneStatus,"voice-recognizer-status":Z(r).voiceRecognizerStatus,onClick:te},null,8,[`hover-class`,`voice-microphone-status`,`voice-recognizer-status`])]),key:`0`}:void 0]),1032,[`is-board-images-palette-visible`,`
```

<a id="FND-30202"></a>
## FND-30202 — Implementation component captured-pieces-placeholder

Vue compiled component __name declaration. Name suggests captured pieces placeholder; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0780
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
t)=>Iv[e]-Iv[t]).map(r=>MA(r,t,e[r],n)).reduce((e,t)=>e.concat(t),[])})),FA,IA,LA=t((()=>{PA(),FA=[`textContent`],IA=K({__name:`captured-pieces-placeholder`,props:{material:{},color:{},verticalLayout:{type:Boolean}},setup(e){let t=Q(),n=e,r=z(()=>{if(!n.material)return[];let e=n.color===1?`white`:`black`,t=n.color===1?`b`:`w`;return NA(n.material[e]??{},t,!1)}),i=z(()=>{if(n.material?.imbalance){if(n.color===1&&n.material.imbalance>0)return`+${n.material.imbalance}`;if(n.color===2&&n.material.imbalance<0)return`+${Math.abs(n.material.imbalance)}`}});function a(e){return e.split(` `).map(e=>t[e])}return(t,n)=>(J(),H(`div`,{class:q([t.$style.capturedPieces,{[t.$style.vertical]:e.verticalLayout}])},[(J(!0),H(Qm,null,hh(r.value,(e,t)=>(J(),H(`span`,{key:t,class:q(a(e))},null,2))),128)),n[0]||=W(),i.value?(J(),H(`span`,{key:0,class:q([t.$style.cpiece,t.$style.score]),textContent:X(i.value)},null,10,FA)):V(``,!0)],2))}})})),RA,zA,BA=t((()=>{LA(),LA(),Z_(),I(),RA={$style:X_},zA=j(IA,[[`__cssModules`,RA]])})),VA,HA=t((()=>{Wt(),PA(),re(),ni(),Qt(),Pv(),If(),VA=class extends Br{static get observedAttributes(){return[Ii.ObservedAttributes.BoardId,Ii.ObservedAttributes.PlayerColor,Ii.ObservedAttributes.VerticalL
```

<a id="FND-30203"></a>
## FND-30203 — Implementation component arena-score

Vue compiled component __name declaration. Name suggests arena score; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0780
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
th.abs(this.capturedPieces.imbalance)}`),this.scoreElement.textContent=e}}})),UA,WA,GA=t((()=>{UA=[`textContent`],WA=K({__name:`arena-score`,props:{score:{},place:{}},setup(e){return(t,n)=>(J(),H(`div`,{class:q(t.$style.component)},[W(X(e.score)+` `,1),e.place?(J(),H(`span`,{key:0,class:q(t.$style.place),textContent:X(`#${e.place}`)},null,10,UA)):V(``,!0)],2))}})})),KA,qA,JA=t((()=>{GA(),GA(),Nb(),I(),KA={$style:Mb},qA=j(WA,[[`__cssModules`,KA]])})),YA,XA=t((()=>{Vf(),Ys(),d(),YA=K({__name:`connection`,props:{tooltipPosition:{},connection:{},isCurrentUser:{type:Boolean}},setup(e){let t=e,n=Q(),r=z(()=>t.isCurrentUser&&t.connection===Hd.Offline),i=z(()=>{switch(t.connection){case Hd.Excellent:return h(`Excellent Connection (very low lag)`);case Hd.Good:return h(`Good Connection (low lag)`);case Hd.Ok:return h(`OK Connection (some lag)`);case Hd.Poor:return h(`Poor Connection (high lag)`);case Hd.Offline:return h(`Member Offline`);default:return``}}),a=z(()=>({[n.component]:!0,[n[t.connection]]:!0,[n.reconnecting]:r.value}));return(t,n)=>(J(),H(`div`,{class:q(a.value)},[G(pu,{position:e.tooltipPosition,text:i.value},null,8,[`position`,`text`])],2))}})})),ZA,QA,$A=t((()=>{XA(),XA(),Ub(),I(),ZA={$style:Hb
```

<a id="FND-30204"></a>
## FND-30204 — Implementation component connection

Vue compiled component __name declaration. Name suggests connection; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0780
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
,KA,qA,JA=t((()=>{GA(),GA(),Nb(),I(),KA={$style:Mb},qA=j(WA,[[`__cssModules`,KA]])})),YA,XA=t((()=>{Vf(),Ys(),d(),YA=K({__name:`connection`,props:{tooltipPosition:{},connection:{},isCurrentUser:{type:Boolean}},setup(e){let t=e,n=Q(),r=z(()=>t.isCurrentUser&&t.connection===Hd.Offline),i=z(()=>{switch(t.connection){case Hd.Excellent:return h(`Excellent Connection (very low lag)`);case Hd.Good:return h(`Good Connection (low lag)`);case Hd.Ok:return h(`OK Connection (some lag)`);case Hd.Poor:return h(`Poor Connection (high lag)`);case Hd.Offline:return h(`Member Offline`);default:return``}}),a=z(()=>({[n.component]:!0,[n[t.connection]]:!0,[n.reconnecting]:r.value}));return(t,n)=>(J(),H(`div`,{class:q(a.value)},[G(pu,{position:e.tooltipPosition,text:i.value},null,8,[`position`,`text`])],2))}})})),ZA,QA,$A=t((()=>{XA(),XA(),Ub(),I(),ZA={$style:Hb},QA=j(YA,[[`__cssModules`,ZA]])})),ej,tj,nj=t((()=>{ej=[`textContent`],tj=K({__name:`grudge-score`,props:{score:{}},setup(e){return(t,n)=>(J(),H(`div`,{class:q(t.$style.component),textContent:X(e.score?.toFixed(1))},null,10,ej))}})})),rj,ij,aj=t((()=>{nj(),nj(),Kb(),I(),rj={$style:Gb},ij=j(tj,[[`__cssModules`,rj]])})),oj,sj,cj,lj,uj=t((()=>{Ys(),aa(),Ss(),d(),windo
```

<a id="FND-30205"></a>
## FND-30205 — Implementation component grudge-score

Vue compiled component __name declaration. Name suggests grudge score; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0780
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
A=t((()=>{XA(),XA(),Ub(),I(),ZA={$style:Hb},QA=j(YA,[[`__cssModules`,ZA]])})),ej,tj,nj=t((()=>{ej=[`textContent`],tj=K({__name:`grudge-score`,props:{score:{}},setup(e){return(t,n)=>(J(),H(`div`,{class:q(t.$style.component),textContent:X(e.score?.toFixed(1))},null,10,ej))}})})),rj,ij,aj=t((()=>{nj(),nj(),Kb(),I(),rj={$style:Gb},ij=j(tj,[[`__cssModules`,rj]])})),oj,sj,cj,lj,uj=t((()=>{Ys(),aa(),Ss(),d(),window.chesscom=window.chesscom||{},window.chesscom.routes=window.chesscom.routes||{},Object.assign(window.chesscom.routes,{web_league_division:{tokens:[[`variable`,`/`,`[\\w]{6,}`,`division`,!0],[`variable`,`/`,`\\w+`,`league`,!0],[`text`,`/leagues`]],defaults:{host:`www.chess-dev.com`},requirements:{league:`\\w+`,division:`[\\w]{6,}`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|
```

<a id="FND-30206"></a>
## FND-30206 — Implementation component league-badge

Vue compiled component __name declaration. Name suggests league badge; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0780
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
chy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}}),oj=[`href`],sj=[`alt`,`src`],cj=[`textContent`],lj=K({__name:`league-badge`,props:{leagueGameOver:{}},setup(e){let t=e,n=Q(),r=z(()=>`#${t.leagueGameOver.stats.ranking}`),i=z(()=>({[n.icon]:!0,[n.faded]:!t.leagueGameOver.isGameValid})),a=z(()=>!t.leagueGameOver.isGameValid||!t.leagueGameOver.division.league.code?Sr(`bundles/web/images/color-icons/cup.svg`):Sr(`bundles/web/images/leagues/badges/${t.leagueGameOver.division.league.code}.svg`)),o=z(()=>t.leagueGameOver.isGameValid?void 0:h(`This game does not qualify for League Points`)),s=z(()=>Dp.generate(`web_league_division`,{league:t.leagueGameOver.division.league.name.toLowerCase(),division:t.leagueGameOver.division.name.slice(1)}));return(t,c)=>(J(),H(`div`,{class:q(Z(n).component)},[U(`a`,{href:s.value,target:`_blank`},[U(`img`,{width:`14`,height:`14`,alt:o.value,src:a.value,class:q(i.value)},null,10,sj),c[0]||=W(),o.value?(J(),B(pu,{key:0,"for-previous-element":``,text:o.value},null,8,[`text`])):V(``,!0)],8,oj),c[1]||=W(),e.leagueGameOver.isGameValid?(J(),H(`span`,{key:0,textContent:X(r.value),class:q(Z(n).points)},null,10,cj)):V(``,!0)],2))}})})),dj,fj,pj=t((()=>{uj(),uj(),Qb(),I(
```

<a id="FND-30207"></a>
## FND-30207 — Implementation component league-score

Vue compiled component __name declaration. Name suggests league score; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0780
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
uj(),uj(),Qb(),I(),dj={$style:Zb},fj=j(lj,[[`__cssModules`,dj]])})),mj,hj,gj=t((()=>{_n(),pj(),mj=[`textContent`],hj=K({__name:`league-score`,props:{leagueGameOver:{}},setup(e){let t=e,n=Q(),r=z(()=>t.leagueGameOver.stats.rankingDelta),i=z(()=>vr(r.value)),a=z(()=>r.value>0?n.positive:n.negative),o=z(()=>t.leagueGameOver.isGameValid);return(t,s)=>(J(),H(`div`,{class:q(Z(n).component)},[G(fj,{"league-game-over":e.leagueGameOver},null,8,[`league-game-over`]),s[0]||=W(),o.value?(J(),B(th,{key:0,appear:``,"enter-active-class":Z(n).fade},{default:$(()=>[r.value?(J(),H(`span`,{key:0,textContent:X(i.value),class:q([Z(n).change,a.value])},null,10,mj)):V(``,!0)]),_:1},8,[`enter-active-class`])):V(``,!0)],2))}})})),_j,vj,yj=t((()=>{gj(),gj(),ax(),I(),_j={$style:ix},vj=j(hj,[[`__cssModules`,_j]])})),bj,xj,Sj=t((()=>{bj=[`textContent`],xj=K({__name:`animated-number`,props:{number:{},increment:{}},setup(e){let t=e,n=0,r=mh(t.number),i=e=>{ch(()=>{e.length&&(r.value+=e.shift()),e.length&&(n=window.setTimeout(i,40,e))})},a=()=>{let e=[],n=t.increment,r=Math.floor(n/10);for(let t=0;t<10;t++)n-=r,e.push(r);return n>0&&e.push(n),e};return fh(()=>{n=window.setTimeout(i,1e3,a())}),dh(()=>{n&&window.clearTimeout(n)}),bh((
```

<a id="FND-30208"></a>
## FND-30208 — Implementation component animated-number

Vue compiled component __name declaration. Name suggests animated number; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0780
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
j=t((()=>{gj(),gj(),ax(),I(),_j={$style:ix},vj=j(hj,[[`__cssModules`,_j]])})),bj,xj,Sj=t((()=>{bj=[`textContent`],xj=K({__name:`animated-number`,props:{number:{},increment:{}},setup(e){let t=e,n=0,r=mh(t.number),i=e=>{ch(()=>{e.length&&(r.value+=e.shift()),e.length&&(n=window.setTimeout(i,40,e))})},a=()=>{let e=[],n=t.increment,r=Math.floor(n/10);for(let t=0;t<10;t++)n-=r,e.push(r);return n>0&&e.push(n),e};return fh(()=>{n=window.setTimeout(i,1e3,a())}),dh(()=>{n&&window.clearTimeout(n)}),bh(()=>t.number,()=>{n&&window.clearTimeout(n),r.value=t.number+t.increment}),(e,t)=>(J(),H(`span`,{textContent:X(r.value)},null,8,bj))}})})),Cj,wj=t((()=>{Sj(),Sj(),Cj=xj})),Tj,Ej,Dj,Oj=t((()=>{_n(),wj(),co(),Tj=[`textContent`],Ej=[`textContent`],Dj=K({__name:`rating-score`,props:{timeControlIcon:{},rating:{},ratingChange:{}},setup(e){let t=e,n=Q(),r=z(()=>t.ratingChange===null?0:vr(t.ratingChange)),i=z(()=>t.ratingChange===null||t.ratingChange>0?n.positive:n.negative);return(t,a)=>(J(),H(`div`,{class:q(Z(n).component)},[G(No,{icon:e.timeControlIcon,class:q(Z(n).icon)},null,8,[`icon`,`class`]),a[1]||=W(),e.ratingChange===null?(J(),H(`span`,{key:0,textContent:X(e.rating),class:q(Z(n).rating)},null,10,Tj)):(J(),H(Qm,{
```

<a id="FND-30209"></a>
## FND-30209 — Implementation component rating-score

Vue compiled component __name declaration. Name suggests rating score; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0780
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
)}})})),Cj,wj=t((()=>{Sj(),Sj(),Cj=xj})),Tj,Ej,Dj,Oj=t((()=>{_n(),wj(),co(),Tj=[`textContent`],Ej=[`textContent`],Dj=K({__name:`rating-score`,props:{timeControlIcon:{},rating:{},ratingChange:{}},setup(e){let t=e,n=Q(),r=z(()=>t.ratingChange===null?0:vr(t.ratingChange)),i=z(()=>t.ratingChange===null||t.ratingChange>0?n.positive:n.negative);return(t,a)=>(J(),H(`div`,{class:q(Z(n).component)},[G(No,{icon:e.timeControlIcon,class:q(Z(n).icon)},null,8,[`icon`,`class`]),a[1]||=W(),e.ratingChange===null?(J(),H(`span`,{key:0,textContent:X(e.rating),class:q(Z(n).rating)},null,10,Tj)):(J(),H(Qm,{key:1},[G(Cj,{number:e.rating-e.ratingChange,increment:e.ratingChange,class:q(Z(n).rating)},null,8,[`number`,`increment`,`class`]),a[0]||=W(),G(th,{appear:``,"enter-active-class":Z(n).fade},{default:$(()=>[U(`span`,{textContent:X(r.value),class:q([Z(n).change,i.value])},null,10,Ej)]),_:1},8,[`enter-active-class`])],64))],2))}})})),kj,Aj,jj=t((()=>{Oj(),Oj(),Mx(),I(),kj={$style:jx},Aj=j(Dj,[[`__cssModules`,kj]])})),Mj,Nj=t((()=>{yj(),jj(),Mj=K({__name:`player-game-over`,props:{isCurrentUser:{type:Boolean},leagueGameOver:{},rating:{},ratingChange:{},timeControlIcon:{}},setup(e){return(t,n)=>(J(),H(`div`,{class:q(t.$style.c
```

<a id="FND-30210"></a>
## FND-30210 — Implementation component player-game-over

Vue compiled component __name declaration. Name suggests player game over; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0780
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
)})),kj,Aj,jj=t((()=>{Oj(),Oj(),Mx(),I(),kj={$style:jx},Aj=j(Dj,[[`__cssModules`,kj]])})),Mj,Nj=t((()=>{yj(),jj(),Mj=K({__name:`player-game-over`,props:{isCurrentUser:{type:Boolean},leagueGameOver:{},rating:{},ratingChange:{},timeControlIcon:{}},setup(e){return(t,n)=>(J(),H(`div`,{class:q(t.$style.component)},[G(Aj,{rating:e.rating,"time-control-icon":e.timeControlIcon,"rating-change":e.ratingChange},null,8,[`rating`,`time-control-icon`,`rating-change`]),n[0]||=W(),e.isCurrentUser&&e.leagueGameOver?(J(),B(vj,{key:0,"league-game-over":e.leagueGameOver},null,8,[`league-game-over`])):V(``,!0)],2))}})})),Pj,Fj,Ij=t((()=>{Nj(),Nj(),cx(),I(),Pj={$style:sx},Fj=j(Mj,[[`__cssModules`,Pj]])})),Lj,Rj,zj=t((()=>{d(),Tn(),Lj=[`textContent`],Rj=K({__name:`seeking-tagline`,props:{isTheatre:{type:Boolean},challenge:{}},setup(e){let t=e,n=Q(),r=z(()=>({[n.component]:!0,[n.theatre]:t.isTheatre})),i=z(()=>{let e=t.challenge.getMaxRating(),n=t.challenge.getMinRating();return!e&&!n?``:h(`Rating Range: %rating%`,{"%rating%":`${n||h(`Any`)}-${e||h(`Any`)}`})}),a=z(()=>t.challenge.getTo()?h(`Waiting for Opponent`):h(`Searching`));return(t,n)=>(J(),H(`div`,{class:q(r.value)},[G(bo,{class:q(t.$style.searching),text:a.value},nu
```

<a id="FND-30211"></a>
## FND-30211 — Implementation component seeking-tagline

Vue compiled component __name declaration. Name suggests seeking tagline; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0780
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
{Nj(),Nj(),cx(),I(),Pj={$style:sx},Fj=j(Mj,[[`__cssModules`,Pj]])})),Lj,Rj,zj=t((()=>{d(),Tn(),Lj=[`textContent`],Rj=K({__name:`seeking-tagline`,props:{isTheatre:{type:Boolean},challenge:{}},setup(e){let t=e,n=Q(),r=z(()=>({[n.component]:!0,[n.theatre]:t.isTheatre})),i=z(()=>{let e=t.challenge.getMaxRating(),n=t.challenge.getMinRating();return!e&&!n?``:h(`Rating Range: %rating%`,{"%rating%":`${n||h(`Any`)}-${e||h(`Any`)}`})}),a=z(()=>t.challenge.getTo()?h(`Waiting for Opponent`):h(`Searching`));return(t,n)=>(J(),H(`div`,{class:q(r.value)},[G(bo,{class:q(t.$style.searching),text:a.value},null,8,[`class`,`text`]),n[0]||=W(),e.challenge.getTo()?V(``,!0):(J(),H(`span`,{key:0,class:q(t.$style.rating),textContent:X(i.value)},null,10,Lj))],2))}})})),Bj,Vj,Hj=t((()=>{zj(),zj(),Rx(),I(),Bj={$style:Lx},Vj=j(Rj,[[`__cssModules`,Bj]])})),Uj,Wj=t((()=>{zd(),mt(),Ys(),d(),Pe(),Uj=K({__name:`timeout-avatar`,props:{timeoutNotification:{},isTheatre:{type:Boolean},isEnglishLocale:{type:Boolean}},setup(e){let t=e,n=Q(),r=z(()=>({[n.component]:!0,[n.theatre]:t.isTheatre})),i=z(()=>t.timeoutNotification?.type===Ym.Offline||t.timeoutNotification?.type===Ym.OpponentOffline),a=z(()=>{if(i.value&&!t.isEnglishLocale)return h(`
```

<a id="FND-30212"></a>
## FND-30212 — Implementation component timeout-avatar

Vue compiled component __name declaration. Name suggests timeout avatar; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0780
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
t((()=>{zj(),zj(),Rx(),I(),Bj={$style:Lx},Vj=j(Rj,[[`__cssModules`,Bj]])})),Uj,Wj=t((()=>{zd(),mt(),Ys(),d(),Pe(),Uj=K({__name:`timeout-avatar`,props:{timeoutNotification:{},isTheatre:{type:Boolean},isEnglishLocale:{type:Boolean}},setup(e){let t=e,n=Q(),r=z(()=>({[n.component]:!0,[n.theatre]:t.isTheatre})),i=z(()=>t.timeoutNotification?.type===Ym.Offline||t.timeoutNotification?.type===Ym.OpponentOffline),a=z(()=>{if(i.value&&!t.isEnglishLocale)return h(`Disconnected.`)});return(e,t)=>(J(),H(`div`,{class:q(r.value)},[G(pu,{text:a.value},null,8,[`text`]),t[0]||=W(),G(Pt,{is:i.value?Z(pr):Z(da),variant:`glyph`,size:20},null,8,[`is`])],2))}})})),Gj,Kj,qj=t((()=>{Wj(),Wj(),Hx(),I(),Gj={$style:Vx},Kj=j(Uj,[[`__cssModules`,Gj]])})),Jj,Yj=t((()=>{tp(),If(),Jj=class extends HTMLElement{constructor(...e){super(...e),Fd(this,`endTime`,1/0),Fd(this,`interval`,null),Fd(this,`timeLeft`,0)}connectedCallback(){this.initialize(),this.start()}initialize(){this.timeLeft=Number(this.getAttribute(`time-left`)),this.textContent=s(this.timeLeft)}start(){setTimeout(()=>{this.endTime=Date.now()+this.timeLeft,this.interval=setInterval(this.step.bind(this),100)},0)}step(){if(Date.now()>this.endTime){clearInterval(this.interval)
```

<a id="FND-30213"></a>
## FND-30213 — Implementation component timeout-text

Vue compiled component __name declaration. Name suggests timeout text; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0780
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
lback(){clearInterval(this.interval),this.interval=null}}})),Xj,Zj,Qj=t((()=>{Yj(),Hs(),d(),Pe(),Xj=[`innerHTML`],Zj=K({__name:`timeout-text`,props:{timeoutNotification:{},isTheatre:{type:Boolean},isEnglishLocale:{type:Boolean},position:{}},setup(e){iu(`wc-count-down`,Jj);let t=e,n=Q(),r=z(()=>({[n.component]:!0,[n.theatre]:t.isTheatre,[n[t.position]]:!0})),i=z(()=>{let{timestamp:e,timeLeft:n}=t.timeoutNotification;return n?Math.max(n-(Date.now()-e),0):0}),a=z(()=>{let e=t.timeoutNotification.type;return e===Ym.AutoAbortOpponentTurn?qn(`Waiting. Will auto-abort in %time%`,{"%time%":`<wc-count-down time-left="${i.value}"/>`}):e===Ym.AutoAbortMyTurn?qn(`Your move. Will auto-abort in %time%`,{"%time%":`<wc-count-down time-left="${i.value}"/>`}):e===Ym.AutoResignOpponentTurn?qn(`Auto-resign in %time%`,{"%time%":`<wc-count-down time-left="${i.value}"/>`}):e===Ym.AutoResignMyTurn?qn(`Your move. Will auto-resign in %time%`,{"%time%":`<wc-count-down time-left="${i.value}"/>`}):e===Ym.OpponentOffline?t.isEnglishLocale?qn(`Disconnected. Will auto-resign in %time%`,{"%time%":`<wc-count-down time-left="${i.value}"/>`}):qn(`Will auto-resign in %time%`,{"%time%":`<wc-count-down time-left="${i.value}"/>`}):e===Ym.Of
```

<a id="FND-30214"></a>
## FND-30214 — Implementation component player

Vue compiled component __name declaration. Name suggests player; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0780
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
`,`host`,!0]],methods:[],schemes:[`https`]}}),nM=[`textContent`],rM=[`board-id`,`vertical-layout`,`player-color`],iM=K({__name:`player`,props:{arenaPlace:{},boardId:{},clubAvatar:{default:``},clubName:{default:``},color:{},connection:{default:null},contentKey:{default:``},country:{},flair:{default:null},fullName:{default:``},isGameOverVisible:{type:Boolean},isCapturedPiecesVisible:{type:Boolean},isCapturedPiecesPlaceholderVisible:{type:Boolean},isCurrentUser:{type:Boolean},isFocusMode:{type:Boolean},isOnline:{type:Boolean,default:!1},isEnglishLocale:{type:Boolean},isSeekingTaglineVisible:{type:Boolean,default:!1},outgoingChallenge:{},isTheatreMode:{type:Boolean},leagueGameOver:{},material:{default:null},membership:{},position:{},rating:{default:0},ratingChange:{default:0},ratingRange:{},shouldAnimateContent:{type:Boolean,default:!1},timeControlIcon:{},ratingType:{},score:{},showFullName:{type:Boolean},squares:{},timeoutNotification:{},title:{default:``},userAvatar:{default:``},username:{},showMembershipBadges:{type:Boolean}},emits:[`click-user`],setup(e,{emit:t}){let n=Q(),r=e,i=t,a=mh({}),o=z(()=>!!(r.isTheatreMode||r.isFocusMode)),s=window.chesscom.features.includes(`cc_ds_light_mode`)?`boldest`:`wh
```

<a id="FND-30215"></a>
## FND-30215 — Implementation component clock-arrow

Vue compiled component __name declaration. Name suggests clock arrow; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0780
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
t`)],2))}})})),oM,sM,cM=t((()=>{aM(),aM(),Cx(),I(),oM={$style:Sx},sM=j(iM,[[`__cssModules`,oM]])})),lM,uM=t((()=>{lM=K({__name:`clock-arrow`,props:{playerIndex:{},position:{}},setup(e){let t=e,n=Q(),r=z(()=>({[n.arrow]:!0,[n[t.position]]:!0,[n.white]:t.playerIndex===0,[n.black]:t.playerIndex===1}));return(e,t)=>(J(),H(`div`,{class:q(r.value)},null,2))}})})),dM,fM,pM=t((()=>{uM(),uM(),ey(),I(),dM={$style:$v},fM=j(lM,[[`__cssModules`,dM]])})),mM,hM=t((()=>{fi(),mM=K({__name:`clock-bar`,props:{playerIndex:{},position:{},remainder:{}},setup(e){let t=e,n=Q(),r=z(()=>Ai(t.remainder)?`linear-gradient(
      to right,
      var(--remainder-color) 0%,
      var(--remainder-color) ${t.remainder}%,
      var(--expired-color) ${t.remainder}%
    )`:void 0),i=z(()=>({[n.bar]:!0,[n[t.position]]:!0,[n.white]:t.playerIndex===0,[n.black]:t.playerIndex===1}));return(e,t)=>(J(),H(`div`,{class:q(i.value),style:uh({background:r.value})},null,6))}})})),gM,_M,vM=t((()=>{hM(),hM(),sy(),I(),gM={$style:oy},_M=j(mM,[[`__cssModules`,gM]])}));function yM(){let e=or();return!!((e===M.Arena||e===M.TeamMatch||e===M.Tournament)&&ms())}var bM=t((()=>{Zi(),sd(),ff()}));function xM(){return yM()?ms()?.getTimeControl()??null:null}var SM=
```

<a id="FND-30216"></a>
## FND-30216 — Implementation component clock-bar

Vue compiled component __name declaration. Name suggests clock bar; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0780
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
2))}})})),dM,fM,pM=t((()=>{uM(),uM(),ey(),I(),dM={$style:$v},fM=j(lM,[[`__cssModules`,dM]])})),mM,hM=t((()=>{fi(),mM=K({__name:`clock-bar`,props:{playerIndex:{},position:{},remainder:{}},setup(e){let t=e,n=Q(),r=z(()=>Ai(t.remainder)?`linear-gradient(
      to right,
      var(--remainder-color) 0%,
      var(--remainder-color) ${t.remainder}%,
      var(--expired-color) ${t.remainder}%
    )`:void 0),i=z(()=>({[n.bar]:!0,[n[t.position]]:!0,[n.white]:t.playerIndex===0,[n.black]:t.playerIndex===1}));return(e,t)=>(J(),H(`div`,{class:q(i.value),style:uh({background:r.value})},null,6))}})})),gM,_M,vM=t((()=>{hM(),hM(),sy(),I(),gM={$style:oy},_M=j(mM,[[`__cssModules`,gM]])}));function yM(){let e=or();return!!((e===M.Arena||e===M.TeamMatch||e===M.Tournament)&&ms())}var bM=t((()=>{Zi(),sd(),ff()}));function xM(){return yM()?ms()?.getTimeControl()??null:null}var SM=t((()=>{Zi(),bM()}));function CM(){return wt(`gameplay.live.low_time_warning`)}var wM=t((()=>{nt()}));function TM(e,t){let n=Yp(e);n?.isPlaying()&&n.playingAs===t&&Dm(n)&&!n.hasComponent(tc.LowTimeWarning)&&CM()&&(ko(Jt.LowTime),_o(e,[tc.LowTimeWarning]))}var EM=t((()=>{io(),xn(),Ba(),mm(),Ap(),wM(),In()})),DM,OM=t((()=>{Ys(),Ic(),cl(),_u(),Kr(),pM
```

<a id="FND-30217"></a>
## FND-30217 — Implementation component player-clock

Vue compiled component __name declaration. Name suggests player clock; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0780
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
Ti(),cm(),zs(),bd(),SM(),bM(),Qf(),Ba(),EM(),Me(),Nu(),zr(),Fu(),Ap(),Mt(),pa(),Mr(),vA(),Wo(),nm(),Hm(),Ld(),c(),DM=K({__name:`player-clock`,props:{position:{},playerIndex:{}},setup(e){let t=Zr(),n=e,r=Nc({position(){return n.position},playerIndex(){return n.playerIndex},isTheatreMode(){return t.value&&(ya()||_A())},gameModel(){return Ki()},gameView(){return Yp(this.gameModel)},isClockRunning(){return Dm(this.gameView)&&t.value},isOnVacation(){return!!((this.gameModel?.isDailyGameModel()||this.gameModel?.isDailySeekModel())&&this.gameModel.isPlayerOnVacation(this.playerIndex)&&!this.gameModel.isOver())},clockTooltip(){return this.gameModel?.isDailyGameModel()?this.gameModel.getClockTooltip(this.playerIndex):``},timeControl(){if(this.gameModel)return this.gameModel.getTimeControl();let e=Us();if(e?.type===ua.DailySeek){let t=qc(e.id);if(t)return t.getTimeControl()}return xM()??rs()},isTextDisplay(){return this.timeControl.timeType!==`live`},initialClockTime(){return Er(this.timeControl)},isGameStarting(){return!!(this.gameModel?.isRealtimeGame()&&this.gameModel.isStarting())},chessboardSelectedPly(){return Qe()},selectedPly(){return this.isGameStarting?0:this.isClockRunning||this.gameView?.isOver()&&U
```

<a id="FND-30218"></a>
## FND-30218 — Implementation component player

Vue compiled component __name declaration. Name suggests player; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0780
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
np(),Jn(),Mo(),an(),zi(),ci(),Gr(),ye(),Wo(),BM(),qf(),oc(),Zf(),Xa(),Hm(),Ld(),Pa(),c(),Gf(),Gd(),Fc(),am(),hr(),VM=K({__name:`player`,props:{position:{}},setup(e){let t=Zr(),n=e,r=Nc({position(){return n.position},gameModel(){return Ki()},gameView(){return Yp(this.gameModel)},boardId(){return bm()},isFocusMode(){return ya()},isTheatreMode(){return _A()},isBoardFlipped(){return Rp(this.gameView)},isEnglishLocale(){return Xs()===`en_US`},color(){return this.position===`top`?this.isBoardFlipped?1:2:this.isBoardFlipped?2:1},playerIndex(){if(!this.gameModel&&yM()||Us()?.type===ua.CustomPosition)return this.position===`bottom`?0:1;switch(this.color){case 1:return 0;default:return 1}},player(){return this.gameModel?.isDailySeekModel()?this.gameModel.getPlayer(this.playerIndex):this.gameView?.getPlayer(this.playerIndex)??wm(this.playerIndex)},pclPlayerInfo(){return this.gameModel?.isLiveGameModel()&&this.gameModel.pcl?zM(this.player.username):null},displayRating(){return vp(this.gameModel)},rating(){if(!t.value)return null;let e=Kc(),n=e.name!==C.DailySeek&&ym.includes(e.name)&&!this.gameModel,r=this.gameView&&wc(this.gameView)&&!pl(),i=!this.gameModel&&Ec();if(!this.displayRating||n||r||i)return null;if(th
```

<a id="FND-30219"></a>
## FND-30219 — Implementation component sidebar

Vue compiled component __name declaration. Name suggests sidebar; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0780
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
imeout-notification.title.user-avatar.username`.split(`.`)))}})})),UM,WM=t((()=>{HM(),HM(),UM=VM})),GM,KM=t((()=>{GM=K({__name:`sidebar`,props:{content:{}},setup(e){let t=e,n=Q(),r=mh({});return bh(()=>t.content,(e,t)=>{e.transition||!t?.tab?r.value={enterActiveClass:n.fadeActive,leaveActiveClass:n.fadeActive,enterFromClass:n.fadeHiding,enterToClass:n.fadeShowing,leaveFromClass:n.fadeShowing,leaveToClass:n.fadeHiding,mode:`out-in`}:r.value={mode:`out-in`}},{immediate:!0}),(t,i)=>(J(),H(`div`,{class:q(Z(n).component)},[Y(t.$slots,`tabs`),i[0]||=W(),G(th,lh(ah(r.value)),{default:$(()=>[(J(),H(`div`,{key:e.content.key,class:q(Z(n).content)},[(J(),B(gh(e.content.component)))],2))]),_:1},16)],2))}})})),qM,JM,YM=t((()=>{KM(),KM(),FS(),I(),qM={$style:PS},JM=j(GM,[[`__cssModules`,qM]])})),XM,ZM=t((()=>{sf(),Wi(),XM=K({inheritAttrs:!1,__name:`cc-skeleton`,setup(e){let t=a({optional:!0})?.features.includes(`design_system_component_migration_cc_skeleton`)??!1;return(e,n)=>Z(t)?(J(),B(Z(tu),lh(sh({key:0},e.$attrs)),null,16)):(J(),H(`div`,sh({key:1},e.$attrs,{class:e.$style.skeleton}),null,16))}})})),QM,$M,eN=t((()=>{ZM(),ZM(),c_(),I(),QM={$style:s_},$M=j(XM,[[`__cssModules`,QM]])})),tN,nN=t((()=>{eN(),tN=K({__nam
```

<a id="FND-30220"></a>
## FND-30220 — Implementation component cc-skeleton

Vue compiled component __name declaration. Name suggests cc skeleton; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0780
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
(()=>{KM(),KM(),FS(),I(),qM={$style:PS},JM=j(GM,[[`__cssModules`,qM]])})),XM,ZM=t((()=>{sf(),Wi(),XM=K({inheritAttrs:!1,__name:`cc-skeleton`,setup(e){let t=a({optional:!0})?.features.includes(`design_system_component_migration_cc_skeleton`)??!1;return(e,n)=>Z(t)?(J(),B(Z(tu),lh(sh({key:0},e.$attrs)),null,16)):(J(),H(`div`,sh({key:1},e.$attrs,{class:e.$style.skeleton}),null,16))}})})),QM,$M,eN=t((()=>{ZM(),ZM(),c_(),I(),QM={$style:s_},$M=j(XM,[[`__cssModules`,QM]])})),tN,nN=t((()=>{eN(),tN=K({__name:`cc-skeleton-grid`,props:{rows:{default:1},columns:{default:1},items:{},rowHeight:{default:`1.4rem`},rowGap:{default:`0`},columnWidth:{default:`1fr`},columnGap:{default:`0`}},setup(e){vh(e=>({v4d30a8e6:e.rowGap,v0075b50f:e.columnGap,v0e547957:Z(n),v53a15299:Z(r)}));let t=e,n=Array(t.columns).fill(t.columnWidth).join(` `),r=Array(t.rows).fill(t.rowHeight).join(` `);return(t,n)=>(J(),H(`div`,{class:q(t.$style.wrapper)},[e.items&&e.items.length>0?(J(!0),H(Qm,{key:0},hh(e.items,(e,n)=>(J(),B($M,{key:n,style:uh(`grid-area: ${e}`),class:q(t.$style.item)},null,8,[`style`,`class`]))),128)):(J(!0),H(Qm,{key:1},hh(e.rows*e.columns,e=>(J(),B($M,{key:e,class:q(t.$style.item)},null,8,[`class`]))),128))],2))}})})),rN,iN,
```

<a id="FND-30221"></a>
## FND-30221 — Implementation component cc-skeleton-grid

Vue compiled component __name declaration. Name suggests cc skeleton grid; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0780
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
6))}})})),QM,$M,eN=t((()=>{ZM(),ZM(),c_(),I(),QM={$style:s_},$M=j(XM,[[`__cssModules`,QM]])})),tN,nN=t((()=>{eN(),tN=K({__name:`cc-skeleton-grid`,props:{rows:{default:1},columns:{default:1},items:{},rowHeight:{default:`1.4rem`},rowGap:{default:`0`},columnWidth:{default:`1fr`},columnGap:{default:`0`}},setup(e){vh(e=>({v4d30a8e6:e.rowGap,v0075b50f:e.columnGap,v0e547957:Z(n),v53a15299:Z(r)}));let t=e,n=Array(t.columns).fill(t.columnWidth).join(` `),r=Array(t.rows).fill(t.rowHeight).join(` `);return(t,n)=>(J(),H(`div`,{class:q(t.$style.wrapper)},[e.items&&e.items.length>0?(J(!0),H(Qm,{key:0},hh(e.items,(e,n)=>(J(),B($M,{key:n,style:uh(`grid-area: ${e}`),class:q(t.$style.item)},null,8,[`style`,`class`]))),128)):(J(!0),H(Qm,{key:1},hh(e.rows*e.columns,e=>(J(),B($M,{key:e,class:q(t.$style.item)},null,8,[`class`]))),128))],2))}})})),rN,iN,aN=t((()=>{nN(),nN(),i_(),I(),rN={$style:r_},iN=j(tN,[[`__cssModules`,rN]])})),oN,sN=t((()=>{aN(),oN=K({__name:`sidebar-skeleton`,setup(e){let t=[`1 / 1 / 2 / 2`,`1 / 2 / 2 / 3`,`1 / 3 / 2 / 4`,`1 / 4 / 2 / 5`,`1 / 5 / 2 / 6`,`2 / 1 / 3 / 5`,`2 / 5 / 3 / 6`,`3 / 1 / 4 / 6`,`4 / 1 / 5 / 6`,`5 / 1 / 6 / 6`,`6 / 1 / 7 / 6`,`7 / 1 / 8 / 6`,`8 / 1 / 9 / 6`];return(e,n)=>(J(),B(iN
```

<a id="FND-30222"></a>
## FND-30222 — Implementation component sidebar-skeleton

Vue compiled component __name declaration. Name suggests sidebar skeleton; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0780
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
2))}})})),rN,iN,aN=t((()=>{nN(),nN(),i_(),I(),rN={$style:r_},iN=j(tN,[[`__cssModules`,rN]])})),oN,sN=t((()=>{aN(),oN=K({__name:`sidebar-skeleton`,setup(e){let t=[`1 / 1 / 2 / 2`,`1 / 2 / 2 / 3`,`1 / 3 / 2 / 4`,`1 / 4 / 2 / 5`,`1 / 5 / 2 / 6`,`2 / 1 / 3 / 5`,`2 / 5 / 3 / 6`,`3 / 1 / 4 / 6`,`4 / 1 / 5 / 6`,`5 / 1 / 6 / 6`,`6 / 1 / 7 / 6`,`7 / 1 / 8 / 6`,`8 / 1 / 9 / 6`];return(e,n)=>(J(),B(iN,{rows:8,columns:5,items:t,"row-height":`4rem`,"row-gap":`.8rem`,"column-gap":`.8rem`,class:q(e.$style.component)},null,8,[`class`]))}})})),cN,lN,uN=t((()=>{sN(),sN(),Qx(),I(),cN={$style:Zx},lN=j(oN,[[`__cssModules`,cN]])})),dN,fN=t((()=>{Nf(),Uo(),_f(),je(),Xi(),cu(),Ic(),vu(),d(),dN=K({__name:`time-selector-next`,props:{dropdownClass:{default:``},gameTypeOptions:{},hasLoadedTimeControl:{type:Boolean,default:!0},isFocusMode:{type:Boolean,default:!1},isGuest:{type:Boolean,default:!1},isLoggedIn:{type:Boolean,default:!0},isOpen:{type:Boolean,default:!1},isRated:{type:Boolean},isRecentTimeControlsPinned:{type:Boolean,default:!1},recentTimeControls:{default:()=>[]},selectedGameType:{},selectedTime:{}},emits:[`click-recent-time-controls-pin`,`click-time`,`select-game-type`,`select-time`,`set-rated`],setup(e,{emit:t}){le
```

<a id="FND-30223"></a>
## FND-30223 — Implementation component time-selector-next

Vue compiled component __name declaration. Name suggests time selector next; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0780
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
(),I(),cN={$style:Zx},lN=j(oN,[[`__cssModules`,cN]])})),dN,fN=t((()=>{Nf(),Uo(),_f(),je(),Xi(),cu(),Ic(),vu(),d(),dN=K({__name:`time-selector-next`,props:{dropdownClass:{default:``},gameTypeOptions:{},hasLoadedTimeControl:{type:Boolean,default:!0},isFocusMode:{type:Boolean,default:!1},isGuest:{type:Boolean,default:!1},isLoggedIn:{type:Boolean,default:!0},isOpen:{type:Boolean,default:!1},isRated:{type:Boolean},isRecentTimeControlsPinned:{type:Boolean,default:!1},recentTimeControls:{default:()=>[]},selectedGameType:{},selectedTime:{}},emits:[`click-recent-time-controls-pin`,`click-time`,`select-game-type`,`select-time`,`set-rated`],setup(e,{emit:t}){let n=e,r=t;function i(e){a.value=!1,r(`select-game-type`,e)}let a=mh(!1),o=h(`(Unrated)`);function s(){a.value=!a.value}let c=z(()=>!n.hasLoadedTimeControl),ee=z(()=>{if(!n.hasLoadedTimeControl)return``;let e=_p(n.selectedTime);if(!n.isRated)return`${e} ${o}`;if(ne.value){let t=fe(n.selectedTime);e+=` (${t})`}return e}),te=z(()=>n.hasLoadedTimeControl?Od(`chess`,n.selectedTime):void 0),ne=z(()=>n.selectedGameType===`chess`);return(t,n)=>(J(),H(`div`,{class:q(t.$style.component)},[G(ps,{"full-width":``,size:`x-large`,"custom-classes":{icon:`glyph-colored`},d
```

<a id="FND-30224"></a>
## FND-30224 — Implementation component new-game

Vue compiled component __name declaration. Name suggests new game; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0780
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
((()=>{fN(),fN(),$g(),I(),pN={$style:Qg},mN=j(dN,[[`__cssModules`,pN]])})),gN,_N=t((()=>{hN(),Ru(),Wm(),Fi(),Jn(),gN=K({__name:`new-game`,props:{gameTypeOptions:{},hasLoadedTimeControl:{type:Boolean},isGuest:{type:Boolean},isLoggedIn:{type:Boolean},isRated:{type:Boolean},isRecentTimeControlsPinned:{type:Boolean},isTimeSelectorOpen:{type:Boolean},minutesUntilShutdown:{},recentTimeControls:{},requireShutdownConfirmation:{type:Boolean},requireTournamentConfirmation:{type:Boolean},selectedGameType:{},selectedTime:{},view:{}},emits:[`click-play`,`click-recent-time-controls-pin`,`custom-game-clicked`,`select-game-type`,`select-time`,`show-tournaments`,`show-view`,`set-rated`,`toggle-time-selector`],setup(e,{emit:t}){let n=fa(),r=t;function i(e){r(`select-game-type`,e)}function a(e){r(`select-time`,e)}function o(){r(`click-recent-time-controls-pin`)}function s(){r(`click-play`)}function c(){r(`show-view`,{view:N.PlayFriend})}return(t,r)=>(J(),H(Qm,null,[U(`div`,{class:q(t.$style.component)},[U(`div`,{class:q(t.$style.primary)},[G(mN,{"game-type-options":e.gameTypeOptions,"has-loaded-time-control":e.hasLoadedTimeControl,"is-guest":e.isGuest,"is-logged-in":e.isLoggedIn,"is-open":e.isTimeSelectorOpen,"is-rated"
```

<a id="FND-30225"></a>
## FND-30225 — Implementation component new-game

Vue compiled component __name declaration. Name suggests new game; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0780
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
,Sm(),Pm(),Jn(),qm(),Bp(),Xt(),an(),ae(),Fl(),ci(),Wo(),nm(),nl(),af(),Rc(),Rl(),Vc(),wo(),f(),td(),PN(),IN(),T(),LN=K({__name:`new-game`,setup(t){let n=Zr(),r=mh(!1);FN(()=>{if(v()){cn()||gr();let t=Xo({triggers:[()=>DN()],shouldLoad:kN,loader:()=>D(()=>e(()=>import(`./load-featured-tv-shows.3e8b4f68.BPG1IDZok3.chunk.js`),`./load-featured-tv-shows.3e8b4f68.BPG1IDZok3.chunk.js`).then(e=>(e.t(),e.n)),__vite__mapDeps([0]),import.meta.url)})();t.mount(),dh(()=>{t.unmount()})}});let i=Nc({gameTypeOptions(){return Ps()},isGuest(){return cn()},hasLoadedTimeControl(){return Je()},isFeaturedTvShowsVisible(){return n.value&&jN()},isLoggedIn(){return v()},isRated(){return op()},minutesUntilShutdown(){return Su()},newGameView(){return Hi()},recentTimeControls(){return $l()},recentTimeControlsPinned(){return n.value&&_d()},selectedGameType(){return Jr()},selectedTime(){return rs()},requireTournamentConfirmation(){let e=Gs();return!!(e&&(pt(e)||Cl(e)))},requireShutdownConfirmation(){return ml()},isIncomingChallengesVisible(){return!!(n.value&&Pi().length)},isAnnouncementVisible(){return n.value&&!!Lu()}});function a(){Pf(Qi()),yp({challenge:ma(),interfaceName:`New Game Sidebar`,elementName:`Game Seek Button`})}fun
```

<a id="FND-30226"></a>
## FND-30226 — Implementation component outgoing-challenge-row

Vue compiled component __name declaration. Name suggests outgoing challenge row; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0780
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
)=>{oo(),yo(),xf()})),UN,WN,GN,KN=t((()=>{zd(),sc(),mt(),Ys(),cu(),d(),Tn(),UN=[`textContent`],WN=[`textContent`],GN=K({__name:`outgoing-challenge-row`,props:{challenge:{},contextUser:{},currentUser:{}},emits:[`cancel-challenge`],setup(e,{emit:t}){let n=e,r=t,i=z(()=>n.contextUser?.isSameUser(n.challenge.getFrom())||n.currentUser.isSameUser(n.challenge.getFrom())),a=z(()=>n.challenge.getTo()?h(`Waiting for Opponent`):h(`Starting soon`));function o(){r(`cancel-challenge`,{challenge:n.challenge})}return(t,n)=>(J(),H(`div`,{class:q(t.$style.component)},[e.challenge.getTo()?(J(),B(Nm,{key:0,class:q(t.$style.avatar),src:e.challenge.getTo()?.getAvatar()||null,username:e.challenge.getTo()?.getUsername()},null,8,[`class`,`src`,`username`])):(J(),B(Pt,{key:1,class:`glyph-colored`,variant:`glyph`,is:Z(Od)(e.challenge.getGameType(),e.challenge.getTimeControl()),size:40},null,8,[`is`])),n[3]||=W(),U(`div`,{class:q(t.$style.column)},[U(`div`,null,[U(`span`,{class:q(t.$style.time),textContent:X(e.challenge.getTimeLabel())},null,10,UN),n[0]||=W(),e.challenge.isRatedChallenge()?V(``,!0):(J(),H(`span`,{key:0,class:q(t.$style.unrated),textContent:X(t.$trans(`(Unrated)`))},null,10,WN))]),n[1]||=W(),G(bo,{class:q(t.$styl
```

<a id="FND-30227"></a>
## FND-30227 — Implementation component outgoing-challenges

Vue compiled component __name declaration. Name suggests outgoing challenges; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0780
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
)})),XN,ZN,QN,$N=t((()=>{zd(),mt(),kr(),YN(),Tn(),XN=[`textContent`],ZN=[`textContent`],QN=K({name:`OutgoingChallenges`,__name:`outgoing-challenges`,props:{challenges:{},contextUser:{default:null},currentUser:{},presenceData:{},showSpeechMessage:{type:Boolean,default:!1}},emits:[`cancel-challenge`,`cancel-all-challenges`,`close-outgoing-challenges`],setup(e){let t=e,n=Q(),r=z(()=>t.challenges.length>1),i=z(()=>t.showSpeechMessage&&!r.value),a=z(()=>r.value?n.list:n.content),o=z(()=>r.value?JN:ga);function s(e){let n=e.getTo()?.getUserUuid();return n?t.presenceData[n]??null:null}return(t,c)=>(J(),H(`div`,{class:q(Z(n).component)},[U(`div`,{class:q(Z(n).header)},[G(bo,{text:t.$trans(`Searching`),class:q(Z(n).label)},null,8,[`text`,`class`]),c[4]||=W(),U(`button`,{class:q(Z(n).close),onClick:c[0]||=e=>t.$emit(`close-outgoing-challenges`)},[G(Pt,{is:Z(la),variant:`glyph`,class:q(Z(n).icon),size:16},null,8,[`is`,`class`]),c[3]||=W(),U(`span`,{class:q(Z(n).text),textContent:X(t.$trans(`New Game`))},null,10,XN)],2)],2),c[7]||=W(),U(`div`,{class:q(a.value)},[i.value?(J(),H(`div`,{key:0,class:q(Z(n).speech)},[Y(t.$slots,`speech`)],2)):V(``,!0),c[5]||=W(),r.value?(J(),H(`button`,{key:1,class:q(Z(n).cancel),text
```

<a id="FND-30228"></a>
## FND-30228 — Implementation component seek-panel-indicator

Vue compiled component __name declaration. Name suggests seek panel indicator; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0780
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
,[[`__cssModules`,eP]])})),rP,iP,aP,oP=t((()=>{sc(),Ru(),mt(),vn(),Ee(),d(),rP=[`textContent`],iP=[`textContent`],aP=K({__name:`seek-panel-indicator`,props:{avatarSrc:{},avatarUsername:{},headline:{},iconName:{},isCancelHidden:{type:Boolean},isUnrated:{type:Boolean},presenceData:{},showAvatar:{type:Boolean},showSearchDots:{type:Boolean},timeLabel:{}},emits:[`cancel`],setup(e){let t=e,n=Q(),r=h(`(Unrated)`),i=z(()=>({[n.cancel]:!0,[n.hidden]:t.isCancelHidden})),a=z(()=>t.presenceData?{isPlaying:t.presenceData.activity===po.Playing,isOnline:t.presenceData.status===zm.Online}:null);return(t,o)=>(J(),H(`div`,{class:q(Z(n).seek)},[e.showAvatar?(J(),B(Nm,{key:0,class:q(Z(n).avatar),size:48,src:e.avatarSrc,status:a.value||void 0,username:e.avatarUsername},null,8,[`class`,`src`,`status`,`username`])):(J(),B(Pt,{key:1,class:q(Z(n).icon),variant:`color`,name:e.iconName,size:48},null,8,[`class`,`name`])),o[3]||=W(),U(`div`,{class:q(Z(n).text)},[U(`p`,{class:q([`cc-heading-small-bold`,Z(n).headline])},[W(X(e.headline)+` `,1),e.showSearchDots?(J(),H(`span`,{key:0,class:q(Z(n).dots),"aria-hidden":`true`},null,2)):V(``,!0)],2),o[2]||=W(),U(`p`,{class:q([`cc-heading-xx-small`,Z(n).timeControl])},[U(`span`,{textConten
```

<a id="FND-30229"></a>
## FND-30229 — Implementation component seek-panel

Vue compiled component __name declaration. Name suggests seek panel; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0780
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
=>{oP(),oP(),wb(),I(),sP={$style:Cb},cP=j(aP,[[`__cssModules`,sP]])})),uP,dP,fP=t((()=>{Ru(),nf(),d(),lP(),uP=5e3,dP=K({__name:`seek-panel`,props:{canCancelPendingChallenge:{type:Boolean},challenge:{},coachTip:{},initialCoachMessage:{},presenceData:{}},emits:[`cancel-challenge`,`close-outgoing-challenges`],setup(e,{emit:t}){let n=e,r=t,i=!n.challenge.getTo(),a=mh(0),o;function s(){a.value++,a.value<3&&(o=window.setTimeout(s,uP))}fh(()=>{i&&(o=window.setTimeout(s,uP))}),dh(()=>{o!==void 0&&clearTimeout(o)});let c=z(()=>i?a.value>=1?h(`Still searching`):h(`Searching`):h(`Waiting for Opponent`)),ee=z(()=>!i||a.value<2?n.initialCoachMessage??n.coachTip:n.challenge.isDailyActiveSeekModel()?h(`You can leave this view. The game will start automatically.`):a.value===2?h(`Taking longer than expected to find a match...`):h(`For quicker pairings, try expanding or disabling your "Rating Range", or trying a more common time control.`)),te=z(()=>{let e=dl(n.challenge.getTimeControl(),n.challenge.getGameType());return e===`live960`||e===`chess960`?e:`time-${e}`}),ne=z(()=>n.challenge.getTo()),re=z(()=>ne.value?.getAvatar()||null),ie=z(()=>ne.value?.getUsername()),ae=z(()=>n.challenge.isPlaceholderChallengeModel()&&!
```

<a id="FND-30230"></a>
## FND-30230 — Implementation component outgoing-challenges

Vue compiled component __name declaration. Name suggests outgoing challenges; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0780
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
Ne(),d(),cl(),nP(),hP(),zn(),np(),It(),Si(),im(),_P(),CP(),Ft(),Jn(),zi(),Na(),TP(),cf(),DP(),uc(),Hc(),Fc(),Fs(),OP=K({__name:`outgoing-challenges`,setup(e){fh(()=>{EP()&&SP(),bh(()=>!yd()&&!ai().length,e=>{e&&i()},{immediate:!0})}),dh(()=>{$t(),Fm(Js.FIRST_GAME),EP()&&gP()});let t=Nc({contextUser(){return gp()},currentUser(){return Zc()},outgoingChallenges(){return Cm()},outgoingOpponentUuids(){return this.outgoingChallenges.map(e=>e.getTo()?.getUserUuid()).filter(e=>!!e)},showSpeechMessage(){return vl(Js.FIRST_GAME)},useSeekPanel(){return EP()&&this.outgoingChallenges.length===1},initialCoachMessage(){return this.showSpeechMessage?h(`Welcome to your first live game. Win, lose, or draw, every chess game is a chance to learn!`):null},seekCoachTip(){return wP()}});function n(e){let t=e.getTo()?.getUserUuid();return t?o.value[t]??null:null}function r({challenge:e}){if(Vp({challenge:e,interfaceName:`New Game Sidebar`,elementName:`Cancel Seek Button`}),e.isPlaceholderChallengeModel()){Xe();return}gt(e)}function i(){$t(),ht(N.Default)}function a(){Ja()}let o=VN(z(()=>t.outgoingOpponentUuids),Jm.PlayOutgoingChallenge);return(e,s)=>Z(t).useSeekPanel?(J(),B(mP,{key:0,"can-cancel-pending-challenge":Z(t).showS
```

<a id="FND-30231"></a>
## FND-30231 — Implementation component sidebar

Vue compiled component __name declaration. Name suggests sidebar; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0780
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
ii(),Lm(),yr(),Vt(),zP(),$e(),of(),Zf(),vf(),VP(),vi(),sd(),Ld(),ri(),Qo(),ff(),UP(),Gf(),GP(),wo(),f(),xt(),qP(),JP=K({__name:`sidebar`,setup(e){let t=Zr(),n=mh(!1);fh(()=>{WP()&&document.querySelector(`.sidebar-component`)?.scrollIntoView(!0),s()});let r=Nc({selectedTab(){return or()},defaultSidebarTab(){return Yn()},isLiveCompetitionRoute(){return jd(Kc())},newGameView(){return Hi()},activeBoard(){return Us()},dailyChallenge(){return Vr(M.DailyChallenge)},dailyGame(){return Vr(M.DailyGame)},liveGame(){return Vr(M.Game)},dailyTeamMatchChallenge(){return Bc()},votechessChallenge(){return Mf()},teamMatchChallenge(){return Wf()},arenaChallenge(){return eu()},tournament(){return ie()},arena(){return Cu()},teamMatch(){return zc()},tabs(){let e=[];return this.dailyChallenge&&e.push({id:M.DailyChallenge,icon:fl,label:h(`Daily`),closable:!0}),this.dailyGame&&e.push({id:M.DailyGame,icon:this.dailyGame.type===`chess960`?Cc:fl,label:h(`Daily`),closable:!0}),this.isLoading&&this.defaultSidebarTab===M.Game?e.push({id:M.Game,icon:om,label:h(`Game`),closable:!1}):this.liveGame&&e.push({id:M.Game,icon:Of(this.liveGame.getGameIcon()),label:KP(ee(this.liveGame),this.liveGame.isOver()),closable:!ee(this.liveGame)||thi
```

<a id="FND-30232"></a>
## FND-30232 — Implementation component application

Vue compiled component __name declaration. Name suggests application; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0780
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
`tabs`])]),_:1},8,[`content`]))}})})),XP,ZP=t((()=>{YP(),YP(),XP=JP})),QP,$P=t((()=>{EA(),WM(),ZP(),Mr(),IN(),T(),QP=K({__name:`application`,setup(t){let n=FN(),r=z(()=>ya()),i=ih(()=>D(()=>e(()=>import(`./lazy-controllers.779ba150.Dlu1JvaL7r.chunk.js`),`./lazy-controllers.779ba150.Dlu1JvaL7r.chunk.js`).then(e=>(e.t(),e.n)),__vite__mapDeps([0]),import.meta.url)),a=ih(()=>D(()=>e(()=>import(`./focus-mode-sidebar.8eca441b.B2duC7mXq5.chunk.js`),`./focus-mode-sidebar.8eca441b.B2duC7mXq5.chunk.js`).then(e=>(e.n(),e.t)),__vite__mapDeps([0,61,55,62]),import.meta.url));return(e,t)=>(J(),H(Qm,null,[(J(),B(eh,{to:`#board-controls`},[G(TA)])),t[1]||=W(),(J(),B(eh,{to:`#board-layout-player-top`},[G(UM,{position:`top`})])),t[2]||=W(),(J(),B(eh,{to:`#board-layout-player-bottom`},[G(UM,{position:`bottom`})])),t[3]||=W(),(J(),B(eh,{to:`#board-layout-sidebar`},[r.value?(J(),B(Z(a),{key:0})):V(``,!0),t[0]||=W(),r.value?V(``,!0):(J(),B(XP,{key:1}))])),t[4]||=W(),Z(n)?(J(),B(Z(i),{key:0})):V(``,!0)],64))}})})),eF,tF=t((()=>{$P(),$P(),eF=QP}));function nF(){Oc(eF).mount(document.createElement(`div`)),rA({onAfterInitControllers(){HS()||BS()}})}var rF=t((()=>{VS(),US(),al(),iA(),tF()})),iF,aF,oF,sF,cF,lF,uF,dF,fF,pF=t((()=>
```

<a id="FND-30233"></a>
## FND-30233 — Implementation component board-layout-main

Vue compiled component __name declaration. Name suggests board layout main; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0780
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
ss:`board-layout-player board-layout-bottom`},dF={key:2,id:`board-layout-analysis`,class:`board-layout-analysis`},fF=K({__name:`board-layout-main`,props:{withAnalysis:{type:Boolean},withControls:{type:Boolean},withEvaluation:{type:Boolean},withPieces:{type:Boolean},withPlayers:{type:Boolean}},setup(e){return(t,n)=>(J(),H(`div`,iF,[e.withPlayers?(J(),H(`div`,aF,[Y(t.$slots,`playerTop`)])):V(``,!0),n[4]||=W(),U(`div`,oF,[e.withEvaluation?(J(),H(`div`,sF,[Y(t.$slots,`evaluation`)])):V(``,!0),n[1]||=W(),e.withPieces?(J(),H(`div`,cF,[Y(t.$slots,`pieces`)])):V(``,!0),n[2]||=W(),Y(t.$slots,`chessboard`),n[3]||=W(),e.withControls?(J(),H(`div`,lF,[Y(t.$slots,`controls`),n[0]||=W(),G(Pt,{class:q([t.$style[`resize-icon`],`board-layout-icon`,`resize`]),is:Z(rl),variant:`glyph`,size:20},null,8,[`class`,`is`])])):V(``,!0)]),n[5]||=W(),e.withPlayers?(J(),H(`div`,uF,[Y(t.$slots,`playerBottom`)])):V(``,!0),n[6]||=W(),e.withAnalysis?(J(),H(`div`,dF,[Y(t.$slots,`analysis`)])):V(``,!0)]))}})})),mF,hF,gF=t((()=>{pF(),pF(),Xg(),I(),mF={$style:Yg},hF=j(fF,[[`__cssModules`,mF]])})),_F,vF,yF=t((()=>{_F={id:`board-layout-sidebar`,class:`board-layout-sidebar`},vF=K({__name:`board-layout-sidebar`,props:{withGameList:{type:Boolea
```

<a id="FND-30234"></a>
## FND-30234 — Implementation component board-layout-sidebar

Vue compiled component __name declaration. Name suggests board layout sidebar; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0780
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
g},hF=j(fF,[[`__cssModules`,mF]])})),_F,vF,yF=t((()=>{_F={id:`board-layout-sidebar`,class:`board-layout-sidebar`},vF=K({__name:`board-layout-sidebar`,props:{withGameList:{type:Boolean}},setup(e){return(t,n)=>(J(),H(`div`,_F,[e.withGameList?Y(t.$slots,`gameList`,{},void 0,void 0,0):V(``,!0),n[0]||=W(),Y(t.$slots,`sidebar`)]))}})})),bF,xF=t((()=>{yF(),yF(),bF=vF}));function SF({options:e,fen:t,id:n=`single`}){let r=xr({options:{boardStyle:e.boardStyle,pieceStyle:e.pieceStyle,themeAssets:e.themeAssets,animationType:e.animationType,flipped:e.flipped,enabled:e.enabled,coordinates:e.coordinates,allowMarkings:e.allowMarkings,id:n},init:{fen:t??sn()}}),i=CF(r.boardId);return{id:r.attrs.id,class:[`board`,r.attrs.class].join(` `),html:`<style id="${r.styleTagId}">${i}</style>${r.html}`,style:wF(r.attrs.style)}}function CF(e){let t=`
    #${e}, .fade-in-overlay {
      background-image: var(--theme-board-style-image, var(--fallback-theme-board-style-image));
    }
    .coordinate-light {
      fill: var(--theme-board-style-coordinate-color-dark, var(--fallback-theme-board-style-coordinate-color-dark));
    }
    .coordinate-dark {
      fill: var(--theme-board-style-coordinate-color-light, var(--fallback-theme-b
```

<a id="FND-30235"></a>
## FND-30235 — Implementation component chessboard-placeholder

Vue compiled component __name declaration. Name suggests chessboard placeholder; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0780
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
dexOf(`:`);return[e.slice(0,t).trim(),e.slice(t+1).trim()]}))}var TF=t((()=>{Wt(),sr()})),EF,DF=t((()=>{TF(),sr(),EF=K({__name:`chessboard-placeholder`,props:{options:{},fen:{default:sn()},id:{}},setup(e){let t=e,n=z(()=>SF({options:t.options,fen:t.fen,id:t.id}));return(e,t)=>t[0]||(_h(-1,!0),(t[0]=U(`div`,{"data-chessboard-hydratable":``,class:q(n.value?.class),id:n.value?.id,style:uh(n.value?.style),innerHTML:n.value?.html},null,14,[`id`,`innerHTML`])).cacheIndex=0,_h(1),t[0])}})})),OF,kF=t((()=>{DF(),DF(),OF=EF})),AF,jF=t((()=>{Wt(),Bl(),Kd(),Bs(),kF(),ru(),Qt(),ec(),sr(),AF=K({__name:`chessboard`,props:{id:{},options:{},mode:{},fen:{default:sn()},variant:{},excludedPlugins:{},monitorUntrustedEvents:{type:Boolean,default:!1}},setup(e){let t=e,n=yh(`placeholder`);return fh(async()=>{let e=n.value.$el,r=t.fen??void 0,i=t.variant,a=r?i?{fen:r,variant:i}:{fen:r}:void 0,o={...Cf(),...t.options,id:t.id,test:fm()},s,c;a&&(s=ur({boardOptions:o,options:{}}),s.load(a),c=a),await yl(e,{id:t.id,fen:r,variant:i,mode:t.mode,options:t.options,excludedPlugins:t.excludedPlugins,monitorUntrustedEvents:t.monitorUntrustedEvents,emitEvents:!0,api:s,init:c}),Nd()}),dh(()=>{(n.value?.$el)?.dispatchEvent(new CustomEvent(I
```

<a id="FND-30236"></a>
## FND-30236 — Implementation component chessboard

Vue compiled component __name declaration. Name suggests chessboard; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0780
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
x=0,_h(1),t[0])}})})),OF,kF=t((()=>{DF(),DF(),OF=EF})),AF,jF=t((()=>{Wt(),Bl(),Kd(),Bs(),kF(),ru(),Qt(),ec(),sr(),AF=K({__name:`chessboard`,props:{id:{},options:{},mode:{},fen:{default:sn()},variant:{},excludedPlugins:{},monitorUntrustedEvents:{type:Boolean,default:!1}},setup(e){let t=e,n=yh(`placeholder`);return fh(async()=>{let e=n.value.$el,r=t.fen??void 0,i=t.variant,a=r?i?{fen:r,variant:i}:{fen:r}:void 0,o={...Cf(),...t.options,id:t.id,test:fm()},s,c;a&&(s=ur({boardOptions:o,options:{}}),s.load(a),c=a),await yl(e,{id:t.id,fen:r,variant:i,mode:t.mode,options:t.options,excludedPlugins:t.excludedPlugins,monitorUntrustedEvents:t.monitorUntrustedEvents,emitEvents:!0,api:s,init:c}),Nd()}),dh(()=>{(n.value?.$el)?.dispatchEvent(new CustomEvent(Ii.Events.BoardDetached)),id(t.id)}),(t,r)=>(J(),B(OF,{ref_key:`placeholder`,ref:n,id:e.id,fen:e.fen,options:e.options},null,8,[`id`,`fen`,`options`]))}})})),MF,NF=t((()=>{jF(),jF(),MF=AF})),PF,FF=t((()=>{Yt(),NF(),ru(),sr(),Ac(),_l(),mu(),MM(),Hm(),Ld(),PF=K({__name:`chessboard`,setup(e){let t=up(),n=z(()=>{switch(Us()?.type){case ua.VotechessChallenge:return{fen:Mf()?.getInitialPosition()??sn(),variant:void 0};case ua.DailyTeamMatchChallenge:return{fen:Bc()?.getI
```

<a id="FND-30237"></a>
## FND-30237 — Implementation component chessboard

Vue compiled component __name declaration. Name suggests chessboard; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0780
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
ptions`]))}})})),MF,NF=t((()=>{jF(),jF(),MF=AF})),PF,FF=t((()=>{Yt(),NF(),ru(),sr(),Ac(),_l(),mu(),MM(),Hm(),Ld(),PF=K({__name:`chessboard`,setup(e){let t=up(),n=z(()=>{switch(Us()?.type){case ua.VotechessChallenge:return{fen:Mf()?.getInitialPosition()??sn(),variant:void 0};case ua.DailyTeamMatchChallenge:return{fen:Bc()?.getInitialPosition()??sn(),variant:void 0};default:{let e=jM();return{fen:e?.fen??sn(),variant:e?.variant}}}}),r=z(()=>Cf());return(e,i)=>(J(),B(MF,{id:Z(t),fen:n.value.fen,variant:n.value.variant,options:r.value,"monitor-untrusted-events":Z(Ln)()},null,8,[`id`,`fen`,`variant`,`options`,`monitor-untrusted-events`]))}})})),IF,LF=t((()=>{FF(),FF(),IF=PF})),RF,zF=t((()=>{gF(),xF(),_u(),iA(),EA(),WM(),ZP(),LF(),Kf(),Mr(),T(),RF=K({__name:`application`,async setup(t){let n,r,i=ih(()=>D(()=>e(()=>import(`./side-controls.ab81330e.BhfP95de_6.chunk.js`),`./side-controls.ab81330e.BhfP95de_6.chunk.js`).then(e=>(e.t(),e.n)),__vite__mapDeps([0,63]),import.meta.url)),a=ih(()=>D(()=>e(()=>import(`./lazy-controllers.779ba150.Dlu1JvaL7r.chunk.js`),`./lazy-controllers.779ba150.Dlu1JvaL7r.chunk.js`).then(e=>(e.t(),e.n)),__vite__mapDeps([0]),import.meta.url)),o=ih(()=>D(()=>e(()=>import(`./focus-mode-si
```

<a id="FND-30238"></a>
## FND-30238 — Implementation component application

Vue compiled component __name declaration. Name suggests application; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0780
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
ts`]))}})})),IF,LF=t((()=>{FF(),FF(),IF=PF})),RF,zF=t((()=>{gF(),xF(),_u(),iA(),EA(),WM(),ZP(),LF(),Kf(),Mr(),T(),RF=K({__name:`application`,async setup(t){let n,r,i=ih(()=>D(()=>e(()=>import(`./side-controls.ab81330e.BhfP95de_6.chunk.js`),`./side-controls.ab81330e.BhfP95de_6.chunk.js`).then(e=>(e.t(),e.n)),__vite__mapDeps([0,63]),import.meta.url)),a=ih(()=>D(()=>e(()=>import(`./lazy-controllers.779ba150.Dlu1JvaL7r.chunk.js`),`./lazy-controllers.779ba150.Dlu1JvaL7r.chunk.js`).then(e=>(e.t(),e.n)),__vite__mapDeps([0]),import.meta.url)),o=ih(()=>D(()=>e(()=>import(`./focus-mode-sidebar.8eca441b.B2duC7mXq5.chunk.js`),`./focus-mode-sidebar.8eca441b.B2duC7mXq5.chunk.js`).then(e=>(e.n(),e.t)),__vite__mapDeps([0,61,55,62]),import.meta.url)),s=z(()=>ya()),c=Zr();return[n,r]=xh(()=>rA()),await n,r(),(e,t)=>(J(),H(Qm,null,[G(hF,{"with-players":``,"with-controls":``,"with-evaluation":``,"with-pieces":``},{playerTop:$(()=>[G(UM,{position:`top`})]),chessboard:$(()=>[G(IF)]),playerBottom:$(()=>[G(UM,{position:`bottom`})]),controls:$(()=>[G(TA)]),pieces:$(()=>[Z(xd)()?(J(),B(Z(i),{key:0})):V(``,!0)]),_:1}),t[5]||=W(),G(bF,null,{sidebar:$(()=>[s.value?(J(),B(Z(o),{key:0})):V(``,!0),t[4]||=W(),s.value?V(``,!0):(J(),B(
```

<a id="FND-30239"></a>
## FND-30239 — Implementation component cc-icon

Vue compiled component __name declaration. Name suggests cc icon; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
`],Lrt=[`alt`,`aria-hidden`,`height`,`src`,`width`],Rrt=[`aria-hidden`,`aria-label`,`role`],zrt=[`data-glyph`],eK=Za(y({__name:`cc-icon`,props:{alt:{},color:{},customSize:{},host:{default:`https://assets-ds.chess.com`},is:{},name:{},size:{default:24},variant:{default:`glyph`}},setup(e){let t=e,n=l(()=>t.customSize?t.customSize:t.size),r=l(()=>t.customSize?`${t.customSize/10}rem`:void 0),i=l(()=>t.host.replace(/\/+$/,``)),a=l(()=>`${i.value}/color-icons/${t.name}.svg`),o=l(()=>`${i.value}/glyphs/${t.name}.svg`);return(t,i)=>e.is?(O(),p(`span`,{key:0,"aria-hidden":e.alt?void 0:`true`,"aria-label":e.alt?e.alt:void 0,class:D([t.$style[`cc-icon-glyph`],e.customSize?null:t.$style[`cc-icon-size-${e.size}`]]),role:e.alt?`img`:void 0,style:ie({color:e.color,"--cc-icon-size":r.value})},[(O(),d(ve(e.is),{height:n.value,width:n.value},null,8,[`height`,`width`]))],14,Irt)):e.variant===`color`?(O(),p(`img`,{key:1,"data-cy":`cc-icon`,alt:e.alt?e.alt:e.name,"aria-hidden":e.alt?void 0:`true`,class:D([t.$style[`cc-icon-img`],e.customSize?null:t.$style[`cc-icon-size-${e.size}`]]),height:n.value,src:a.value,style:ie({"--cc-icon-size":r.value}),width:n.value},null,14,Lrt)):(O(),p(`span`,{key:2,"aria-hidden":e.alt?void 0:`
```
