# Extended findings

[Master index](../chapters/00_MASTER_INDEX.md)

<a id="FND-30060"></a>
## FND-30060 — Implementation component game-controls-secondary

Vue compiled component __name declaration. Name suggests game controls secondary; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0066
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
((()=>{_R(),_R(),aw(),x(),vR={$style:iw},yR=_(gR,[[`__cssModules`,vR]])})),xR,SR=n((()=>{Xn(),qd(),Zh(),hR(),bR(),xR=W({__name:`game-controls-secondary`,props:{controls:{}},emits:[`click`],setup(e,{emit:t}){let n=t,r=q(!1),i=q(fR().width),a=window.context?.locale===`en_US`,o=Gv(`container`),s=L(()=>!a&&i.value<350),c=new ResizeObserver(()=>{i.value=fR().width});Iv(()=>{o.value&&c.observe(o.value)}),Fv(()=>{c.disconnect()});function l(e){n(`click`,{value:e.value})}function u(e){r.value=!1,l(e)}function d(){r.value||=!0}function ee(){setTimeout(()=>{r.value=!1})}return(t,n)=>(K(),B(`div`,{class:G(t.$style.component),ref_key:`container`,ref:o},[s.value?(K(!0),B(kv,{key:0},zv(e.controls.left,(e,n)=>(K(),R(Pm,{key:n,icon:{is:e.icon,variant:`glyph`},loading:e.loading?.(),tooltip:e.tooltip(),"aria-label":e.tooltip(),disabled:!e.enabled(),class:G(t.$style.button),size:`small`,onClick:t=>l({value:e.event})},null,8,[`icon`,`loading`,`tooltip`,`aria-label`,`disabled`,`class`,`onClick`]))),128)):(K(!0),B(kv,{key:1},zv(e.controls.left,(e,n)=>(K(),R(Gp,{key:n,icon:{is:e.icon,variant:`glyph`},loading:e.loading?.(),tooltip:e.tooltip(),label:e.label?.(),"aria-label":e.tooltip(),disabled:!e.enabled(),class:G(t.$style.b
```

<a id="FND-30061"></a>
## FND-30061 — Implementation component game-controls

Vue compiled component __name declaration. Name suggests game controls; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0066
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}}),Az=W({__name:`game-controls`,props:{hideMainControls:{type:Boolean},hideSecondaryControls:{type:Boolean},overrides:{},secondaryControls:{}},setup(t){let n=Mv(()=>O(()=>e(()=>import(`./mobile-gr-footer.57f96aa7.o50jJkjMh9.chunk.js`),`./mobile-gr-footer.57f96aa7.o50jJkjMh9.chunk.js`).then(e=>(e.t(),e.n)),__vite__mapDeps([0,39]),import.meta.url)),r=Mv(()=>O(()=>e(()=>import(`./tertiary-controls-component.0e576136.CD--YXAYIf.chunk.js`),`./tertiary-controls-component.0e576136.CD--YXAYIf.chunk.js`).then(e=>(e.t(),e.n)),__vite__mapDeps([0,40]),import.meta.url)),i=Mv(()=>O(()=>e(()=>import(`./exploring-skills-menu.dff52af2.DqP_NWy7pd.chunk.js`),`./exploring-skills-menu.dff52af2.DqP_NWy7pd.chunk.js`).then(e=>(e.n(),e.t)),__vite__mapDeps([0,18,41,42,19,43]),import.meta.url)),a=t,o=q(),c=q(Og.selectedTab===P.Tabs.Review&&a.hideMainControls),l=q(a.hideSecondaryControls),u=L(()=>Og.selectedTab===P.Tabs.Review),d=L(()=>Mc()),ee=L(()=>le()),{isFavorite:te,hasFavoriteGame:ne,toggle:re}=dz(),ie=q(!1);qv(()=>oc.state.value,e=>{e!==`idle`&&(ie.value=!1)});let ae=L(()=>{let e=a.secondaryControls??bz();return{
```

<a id="FND-30062"></a>
## FND-30062 — Implementation component sidebar

Vue compiled component __name declaration. Name suggests sidebar; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0066
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
,Em(),ca(),aB(),j(),Qu(),Cv(),on(),mp(),rm(),Zs(),xd(),$o(),fl(),sB(),lB(),dc(),_g(),A(),uB=W({name:`SidebarController`,__name:`sidebar`,setup(t){let n=Mv(()=>O(()=>e(()=>import(`./skills-board-overlays-controller.016864b2.DUrV87IkA8.chunk.js`),`./skills-board-overlays-controller.016864b2.DUrV87IkA8.chunk.js`).then(e=>(e.t(),e.n)),__vite__mapDeps([0,46,47]),import.meta.url)),r=Mv(()=>O(()=>e(()=>import(`./skills-modals-controller.a1aed6b2.hy9_Z0iPT8.chunk.js`),`./skills-modals-controller.a1aed6b2.hy9_Z0iPT8.chunk.js`).then(e=>(e.t(),e.n)),__vite__mapDeps([0]),import.meta.url)),i=Mm(`analysis_openings_tab`,`Openings`),a=S(),o=q(f()),c=L(()=>rB[Og.selectedTab]),l=L(()=>c.value.key===P.Tabs.CollectionSettings),u=q(!1),d=L(()=>Z_()),ee=L(()=>k.isLoaded),te=L(()=>Xi().isInitialized),ne=L(()=>!0),re=L($_),ie=L(()=>Gs()?.riveAnimationUrl),ae=L(()=>!!d.value&&!pp()),oe=L(()=>c.value.key===P.Tabs.Review?m.gameReviewPage===g.Pages.MoveByMove:!!(d.value||c.value.key===P.Tabs.Analysis&&jm())),se=L(()=>Ve()),ce=L(()=>Mc()&&Og.selectedTab===P.Tabs.Review&&m.gameReviewPage===g.Pages.MoveByMove),{isFavorite:le,hasFavoriteGame:ue,toggle:de}=dz(),fe=L(()=>Og.selectedTab===P.Tabs.Review&&m.gameReviewPage===g.Pages.Overv
```

<a id="FND-30063"></a>
## FND-30063 — Implementation component report-ad-button

Vue compiled component __name declaration. Name suggests report ad button; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0066
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
=>n.unmount(),slotId:t});n.mount(`#report-ad-modal`)}var dV=n((()=>{so(),A()})),fV,pV=n((()=>{Xn(),dV(),qd(),Zh(),fV=W({__name:`report-ad-button`,props:{slotId:{},variant:{default:`default`}},setup(e){let t=e;function n(){uV(t.slotId)}return(t,r)=>e.variant===`icon`?(K(),R(Pm,{key:0,icon:{is:J(we),variant:`glyph`},tooltip:{text:t.$trans(`Report Ad`),position:`bottom`},"icon-size":16,size:`small`,onClick:n},null,8,[`icon`,`tooltip`])):(K(),R(Gp,{key:1,class:G([t.$style.report,`dark-mode`]),size:`x-small`,label:t.$trans(`Report Ad`),variant:`ghost`,onClick:n},null,8,[`class`,`label`]))}})})),mV,hV,gV=n((()=>{pV(),pV(),wb(),x(),mV={$style:Cb},hV=_(fV,[[`__cssModules`,mV]])})),_V,vV,yV=n((()=>{lV(),gV(),_V=[`id`],vV=W({__name:`leaderboard-ad`,props:{slotId:{},variant:{default:`leaderboard`}},setup(e){return(t,n)=>(K(),B(`div`,{class:G([t.$style.component,t.$style[e.variant],{[t.$style[`with-report-ad`]]:J(cV)()}])},[V(`div`,{class:G(t.$style.slot),id:e.slotId},null,10,_V),n[0]||=H(),J(cV)()?(K(),R(hV,{key:0,"slot-id":e.slotId},null,8,[`slot-id`])):z(``,!0)],2))}})})),bV,xV,SV=n((()=>{yV(),yV(),By(),x(),bV={$style:zy},xV=_(vV,[[`__cssModules`,bV]])})),CV,wV=n((()=>{Xx(),SV(),CV=W({__name:`leaderboard-atf-a
```

<a id="FND-30064"></a>
## FND-30064 — Implementation component leaderboard-ad

Vue compiled component __name declaration. Name suggests leaderboard ad; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0066
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
=n((()=>{pV(),pV(),wb(),x(),mV={$style:Cb},hV=_(fV,[[`__cssModules`,mV]])})),_V,vV,yV=n((()=>{lV(),gV(),_V=[`id`],vV=W({__name:`leaderboard-ad`,props:{slotId:{},variant:{default:`leaderboard`}},setup(e){return(t,n)=>(K(),B(`div`,{class:G([t.$style.component,t.$style[e.variant],{[t.$style[`with-report-ad`]]:J(cV)()}])},[V(`div`,{class:G(t.$style.slot),id:e.slotId},null,10,_V),n[0]||=H(),J(cV)()?(K(),R(hV,{key:0,"slot-id":e.slotId},null,8,[`slot-id`])):z(``,!0)],2))}})})),bV,xV,SV=n((()=>{yV(),yV(),By(),x(),bV={$style:zy},xV=_(vV,[[`__cssModules`,bV]])})),CV,wV=n((()=>{Xx(),SV(),CV=W({__name:`leaderboard-atf-ad`,setup(e){return(e,t)=>(K(),R(xV,{"slot-id":J(X).leaderboardAtf},null,8,[`slot-id`]))}})})),TV,EV=n((()=>{wV(),wV(),TV=CV})),DV,OV=n((()=>{Xx(),SV(),DV=W({__name:`leaderboard-btf-ad`,setup(e){return(e,t)=>(K(),R(xV,{"slot-id":J(X).leaderboardBtf},null,8,[`slot-id`]))}})})),kV,AV=n((()=>{OV(),OV(),kV=DV})),jV,MV=n((()=>{Xn(),qd(),Oi(),$s(),window.chesscom=window.chesscom||{},window.chesscom.routes=window.chesscom.routes||{},Object.assign(window.chesscom.routes,{web_membership_no_ads:{tokens:[[`text`,`/no-ads`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

<a id="FND-30065"></a>
## FND-30065 — Implementation component leaderboard-atf-ad

Vue compiled component __name declaration. Name suggests leaderboard atf ad; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0066
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
)})),bV,xV,SV=n((()=>{yV(),yV(),By(),x(),bV={$style:zy},xV=_(vV,[[`__cssModules`,bV]])})),CV,wV=n((()=>{Xx(),SV(),CV=W({__name:`leaderboard-atf-ad`,setup(e){return(e,t)=>(K(),R(xV,{"slot-id":J(X).leaderboardAtf},null,8,[`slot-id`]))}})})),TV,EV=n((()=>{wV(),wV(),TV=CV})),DV,OV=n((()=>{Xx(),SV(),DV=W({__name:`leaderboard-btf-ad`,setup(e){return(e,t)=>(K(),R(xV,{"slot-id":J(X).leaderboardBtf},null,8,[`slot-id`]))}})})),kV,AV=n((()=>{OV(),OV(),kV=DV})),jV,MV=n((()=>{Xn(),qd(),Oi(),$s(),window.chesscom=window.chesscom||{},window.chesscom.routes=window.chesscom.routes||{},Object.assign(window.chesscom.routes,{web_membership_no_ads:{tokens:[[`text`,`/no-ads`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacch
```

<a id="FND-30066"></a>
## FND-30066 — Implementation component leaderboard-btf-ad

Vue compiled component __name declaration. Name suggests leaderboard btf ad; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0066
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
slot-id":J(X).leaderboardAtf},null,8,[`slot-id`]))}})})),TV,EV=n((()=>{wV(),wV(),TV=CV})),DV,OV=n((()=>{Xx(),SV(),DV=W({__name:`leaderboard-btf-ad`,setup(e){return(e,t)=>(K(),R(xV,{"slot-id":J(X).leaderboardBtf},null,8,[`slot-id`]))}})})),kV,AV=n((()=>{OV(),OV(),kV=DV})),jV,MV=n((()=>{Xn(),qd(),Oi(),$s(),window.chesscom=window.chesscom||{},window.chesscom.routes=window.chesscom.routes||{},Object.assign(window.chesscom.routes,{web_membership_no_ads:{tokens:[[`text`,`/no-ads`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_membership_no_ads:{tokens:[[`text`,`/no-ads`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|z
```

<a id="FND-30067"></a>
## FND-30067 — Implementation component ad-upgrade-link

Vue compiled component __name declaration. Name suggests ad upgrade link; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0066
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}}),jV=W({__name:`ad-upgrade-link`,props:{referral:{},variant:{default:`default`}},setup(e){let t=e,n=C(`Remove Ads`),r=N.generate(`web_membership_no_ads`,{c:t.referral??`no_ads`,utm_source:`chesscom`,utm_medium:`no_ads_button`});return(t,i)=>e.variant===`link`?(K(),R(Gp,{key:0,variant:`ghost-link`,target:`_blank`,size:`medium`,class:G(t.$style[`link-height`]),label:J(n),href:J(r),icon:{is:J(rr),variant:`glyph`}},null,8,[`class`,`label`,`href`,`icon`])):(K(),R(Gp,{key:1,variant:`monetization`,target:`_blank`,size:`small`,"full-width":``,class:G(t.$style[`monetization-button`]),label:J(n),href:J(r),icon:{is:J(rr),variant:`glyph`}},null,8,[`class`,`label`,`href`,`icon`]))}})})),NV,PV,FV=n((()=>{MV(),MV(),ry(),x(),NV={$style:ny},PV=_(jV,[[`__cssModules`,NV]])})),IV,LV,RV=n((()=>{lV(),FV(),gV(),IV=[`id`],LV=W({__name:`medium-rectangle-ad`,props:{slotId:{}},setup(e){return(t,n)=>(K(),B(`div`,{class:G([t.$style.component,{[t.$style[`with-report-ad`]]:J(cV)()}])},[V(`div`,{class:G(t.$style.slot),id:e.slotId},null,10,IV),n[0]||=H(),U(PV),n[1]||=H(),J(cV)()?(K(),R(hV,{key:0,"slot-id":e.slotId},null,8,[
```

<a id="FND-30068"></a>
## FND-30068 — Implementation component medium-rectangle-ad

Vue compiled component __name declaration. Name suggests medium rectangle ad; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0066
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
)=>{MV(),MV(),ry(),x(),NV={$style:ny},PV=_(jV,[[`__cssModules`,NV]])})),IV,LV,RV=n((()=>{lV(),FV(),gV(),IV=[`id`],LV=W({__name:`medium-rectangle-ad`,props:{slotId:{}},setup(e){return(t,n)=>(K(),B(`div`,{class:G([t.$style.component,{[t.$style[`with-report-ad`]]:J(cV)()}])},[V(`div`,{class:G(t.$style.slot),id:e.slotId},null,10,IV),n[0]||=H(),U(PV),n[1]||=H(),J(cV)()?(K(),R(hV,{key:0,"slot-id":e.slotId},null,8,[`slot-id`])):z(``,!0)],2))}})})),zV,BV,VV=n((()=>{RV(),RV(),xb(),x(),zV={$style:bb},BV=_(LV,[[`__cssModules`,zV]])})),HV,UV=n((()=>{Xx(),VV(),HV=W({__name:`medium-rectangle-atf-ad`,setup(e){return(e,t)=>(K(),R(BV,{"slot-id":J(X).mediumRectangleAtf},null,8,[`slot-id`]))}})})),WV,GV=n((()=>{UV(),UV(),WV=HV})),KV,qV=n((()=>{Xx(),VV(),KV=W({__name:`medium-rectangle-btf-ad`,setup(e){return(e,t)=>(K(),R(BV,{"slot-id":J(X).mediumRectangleBtf},null,8,[`slot-id`]))}})})),JV,YV=n((()=>{qV(),qV(),JV=KV}));function XV(e){tp(Se.WithUnd,e)}var ZV=n((()=>{Lf(),Fi()})),QV,$V=n((()=>{Xx(),eS(),QV={[$x.oneColumn]:[X.leaderboardAtf,X.leaderboardBtf],[$x.twoColumn]:[X.leaderboardAtf,X.mediumRectangleAtf,X.mediumRectangleBtf],[$x.twoColumnAlt]:[X.mediumRectangleAtf,X.mediumRectangleBtf,X.leaderboardBtf],[$x.twoColumnP
```

<a id="FND-30069"></a>
## FND-30069 — Implementation component medium-rectangle-atf-ad

Vue compiled component __name declaration. Name suggests medium rectangle atf ad; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0066
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
)})),zV,BV,VV=n((()=>{RV(),RV(),xb(),x(),zV={$style:bb},BV=_(LV,[[`__cssModules`,zV]])})),HV,UV=n((()=>{Xx(),VV(),HV=W({__name:`medium-rectangle-atf-ad`,setup(e){return(e,t)=>(K(),R(BV,{"slot-id":J(X).mediumRectangleAtf},null,8,[`slot-id`]))}})})),WV,GV=n((()=>{UV(),UV(),WV=HV})),KV,qV=n((()=>{Xx(),VV(),KV=W({__name:`medium-rectangle-btf-ad`,setup(e){return(e,t)=>(K(),R(BV,{"slot-id":J(X).mediumRectangleBtf},null,8,[`slot-id`]))}})})),JV,YV=n((()=>{qV(),qV(),JV=KV}));function XV(e){tp(Se.WithUnd,e)}var ZV=n((()=>{Lf(),Fi()})),QV,$V=n((()=>{Xx(),eS(),QV={[$x.oneColumn]:[X.leaderboardAtf,X.leaderboardBtf],[$x.twoColumn]:[X.leaderboardAtf,X.mediumRectangleAtf,X.mediumRectangleBtf],[$x.twoColumnAlt]:[X.mediumRectangleAtf,X.mediumRectangleBtf,X.leaderboardBtf],[$x.twoColumnProfile]:[X.leaderboardAtf,X.mediumRectangleAtf,X.mediumRectangleBtf,X.superleaderboard1,X.superleaderboard2,X.superleaderboard3],[$x.chessboard]:[X.skyscraper,X.skyscraperWide,X.gameOver],[$x.chessboardAlt]:[X.skyscraper,X.skyscraperWide],[$x.variants]:[X.skyscraper,X.gameOver,X.gameOverVariantsFfa,X.gameOverVariantsTeams],[$x.events]:[X.leaderboardAtf,X.skyscraper,X.skyscraperWide,X.gameOver]}}));function eH(){let{chessboard:e,chessboa
```

<a id="FND-30070"></a>
## FND-30070 — Implementation component medium-rectangle-btf-ad

Vue compiled component __name declaration. Name suggests medium rectangle btf ad; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0066
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
-id":J(X).mediumRectangleAtf},null,8,[`slot-id`]))}})})),WV,GV=n((()=>{UV(),UV(),WV=HV})),KV,qV=n((()=>{Xx(),VV(),KV=W({__name:`medium-rectangle-btf-ad`,setup(e){return(e,t)=>(K(),R(BV,{"slot-id":J(X).mediumRectangleBtf},null,8,[`slot-id`]))}})})),JV,YV=n((()=>{qV(),qV(),JV=KV}));function XV(e){tp(Se.WithUnd,e)}var ZV=n((()=>{Lf(),Fi()})),QV,$V=n((()=>{Xx(),eS(),QV={[$x.oneColumn]:[X.leaderboardAtf,X.leaderboardBtf],[$x.twoColumn]:[X.leaderboardAtf,X.mediumRectangleAtf,X.mediumRectangleBtf],[$x.twoColumnAlt]:[X.mediumRectangleAtf,X.mediumRectangleBtf,X.leaderboardBtf],[$x.twoColumnProfile]:[X.leaderboardAtf,X.mediumRectangleAtf,X.mediumRectangleBtf,X.superleaderboard1,X.superleaderboard2,X.superleaderboard3],[$x.chessboard]:[X.skyscraper,X.skyscraperWide,X.gameOver],[$x.chessboardAlt]:[X.skyscraper,X.skyscraperWide],[$x.variants]:[X.skyscraper,X.gameOver,X.gameOverVariantsFfa,X.gameOverVariantsTeams],[$x.events]:[X.leaderboardAtf,X.skyscraper,X.skyscraperWide,X.gameOver]}}));function eH(){let{chessboard:e,chessboardAlt:t,twoColumn:n,twoColumnAlt:r,twoColumnProfile:i,oneColumn:a,variants:o,events:s}=QV;switch(eV.getAdsSection()){case Y.analysisChessboard:return rS(Y.analysis,t);case Y.features:return r
```

<a id="FND-30071"></a>
## FND-30071 — Implementation component skyscraper-ad

Vue compiled component __name declaration. Name suggests skyscraper ad; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0066
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
e,t){return e/t>=2?X.skyscraperWide:X.skyscraper}var sH=n((()=>{Xx()})),cH,lH,uH=n((()=>{lV(),FV(),gV(),cH=[`id`],lH=W({__name:`skyscraper-ad`,props:{id:{}},setup(e){return(t,n)=>(K(),B(`div`,{class:G([t.$style.component,{[t.$style[`with-report-ad`]]:J(cV)()}])},[V(`div`,{class:G(t.$style.slot),id:e.id},null,10,cH),n[0]||=H(),U(PV),n[1]||=H(),J(cV)()?(K(),R(hV,{key:0,"slot-id":e.id},null,8,[`slot-id`])):z(``,!0)],2))}})})),dH,fH,pH=n((()=>{uH(),uH(),kb(),x(),dH={$style:Ob},fH=_(lH,[[`__cssModules`,dH]])})),mH,hH=n((()=>{Td(),ZV(),aH(),sH(),rV(),pH(),mH=W({__name:`skyscraper-ad`,setup(e){let t=vo(),n=L(()=>oH(t.width.value,t.height.value));return qv(()=>nV(),XV,{immediate:!0}),qv(()=>n.value,iH),(e,t)=>J(nV)()?(K(),R(fH,{id:n.value,key:n.value},null,8,[`id`])):z(``,!0)}})})),gH,_H=n((()=>{hH(),hH(),gH=mH}));async function vH(){let e={skyscraper:`#sidebar-ad`,leaderboardAtf:`#leaderboard-atf-ad`,leaderboardBtf:`#leaderboard-btf-ad`,mediumRectangleAtf:`#medium-rectangle-atf-ad`,mediumRectangleBtf:`#medium-rectangle-btf-ad`},t={};document.querySelector(e.skyscraper)&&(t[e.skyscraper]=gH),document.querySelector(e.leaderboardAtf)&&(t[e.leaderboardAtf]=TV),document.querySelector(e.leaderboardBtf)&&(t[e.leade
```

<a id="FND-30072"></a>
## FND-30072 — Implementation component skyscraper-ad

Vue compiled component __name declaration. Name suggests skyscraper ad; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0066
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
>{uH(),uH(),kb(),x(),dH={$style:Ob},fH=_(lH,[[`__cssModules`,dH]])})),mH,hH=n((()=>{Td(),ZV(),aH(),sH(),rV(),pH(),mH=W({__name:`skyscraper-ad`,setup(e){let t=vo(),n=L(()=>oH(t.width.value,t.height.value));return qv(()=>nV(),XV,{immediate:!0}),qv(()=>n.value,iH),(e,t)=>J(nV)()?(K(),R(fH,{id:n.value,key:n.value},null,8,[`id`])):z(``,!0)}})})),gH,_H=n((()=>{hH(),hH(),gH=mH}));async function vH(){let e={skyscraper:`#sidebar-ad`,leaderboardAtf:`#leaderboard-atf-ad`,leaderboardBtf:`#leaderboard-btf-ad`,mediumRectangleAtf:`#medium-rectangle-atf-ad`,mediumRectangleBtf:`#medium-rectangle-btf-ad`},t={};document.querySelector(e.skyscraper)&&(t[e.skyscraper]=gH),document.querySelector(e.leaderboardAtf)&&(t[e.leaderboardAtf]=TV),document.querySelector(e.leaderboardBtf)&&(t[e.leaderboardBtf]=kV),document.querySelector(e.mediumRectangleAtf)&&(t[e.mediumRectangleAtf]=WV),document.querySelector(e.mediumRectangleBtf)&&(t[e.mediumRectangleBtf]=JV),await Rd(t)}var yH=n((()=>{EV(),AV(),GV(),YV(),_H(),l()}));function bH(e,t,n){window.chesscom.clientMetrics?.recordRuntimeMetricImpl?window.chesscom.clientMetrics.recordRuntimeMetricImpl(e,t,n):window.chesscom.clientMetrics?.enabled&&window.chesscom.clientMetrics.queue?.push({
```

<a id="FND-30073"></a>
## FND-30073 — Implementation component charts-tab

Vue compiled component __name declaration. Name suggests charts tab; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0089
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
seHTML:!0}}var dt=t((()=>{}));function ft(e){return e>3600}var pt=t((()=>{})),mt,ht,gt,_t=t((()=>{c(),ce(),Ve(),v(),mt={__name:`charts-tab`,props:{icon:{type:[Object,Function],required:!0},isActive:{type:Boolean,default:!1},isExpanded:{type:Boolean},label:{type:String,required:!0}},emits:[`click`],setup(e){return(t,n)=>(U(),R(`button`,{type:`button`,class:H([t.$style.component,{[t.$style.active]:e.isActive}]),onClick:n[0]||=e=>t.$emit(`click`,e)},[De(a,{is:e.icon,variant:`glyph`,class:H(t.$style.icon),size:20},null,8,[`is`,`class`]),n[1]||=B(),z(`span`,{class:H(t.$style.label)},Me(e.label),3),n[2]||=B(),e.isExpanded&&e.isActive?(U(),I(a,{key:0,is:Ne(ne),variant:`glyph`,class:H(t.$style[`collapse-icon`]),size:16},null,8,[`is`,`class`])):L(``,!0)],2))}},ht={$style:Be},gt=u(mt,[[`__cssModules`,ht]])})),vt,yt=t((()=>{xe(),_t(),vt=Oe({__name:`charts-view`,props:{analysisComplete:{type:Boolean},baseOptions:{},mainLineParentMoveNumber:{},tabs:{default:()=>[]}},emits:[`change-active-tab`],setup(e,{emit:t}){let n=e,r=t,i=Ae(),a=F(()=>n.tabs.find(e=>e.key===i.value)),o=Pe(`chartEl`),s=Ae(n.baseOptions),c=F(()=>!!i.value);W(()=>n.baseOptions,h,{deep:!0,immediate:!0}),W(()=>n.mainLineParentMoveNumber,p);function 
```

<a id="FND-30074"></a>
## FND-30074 — Implementation component charts-view

Vue compiled component __name declaration. Name suggests charts view; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0089
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
null,8,[`is`,`class`])):L(``,!0)],2))}},ht={$style:Be},gt=u(mt,[[`__cssModules`,ht]])})),vt,yt=t((()=>{xe(),_t(),vt=Oe({__name:`charts-view`,props:{analysisComplete:{type:Boolean},baseOptions:{},mainLineParentMoveNumber:{},tabs:{default:()=>[]}},emits:[`change-active-tab`],setup(e,{emit:t}){let n=e,r=t,i=Ae(),a=F(()=>n.tabs.find(e=>e.key===i.value)),o=Pe(`chartEl`),s=Ae(n.baseOptions),c=F(()=>!!i.value);W(()=>n.baseOptions,h,{deep:!0,immediate:!0}),W(()=>n.mainLineParentMoveNumber,p);function l(e){return i.value===e}function u(){return{...n.baseOptions,currentMoveNumber:n.mainLineParentMoveNumber}}function d(){a.value?.onLoad&&V(a.value.onLoad),p(n.mainLineParentMoveNumber)}function f(e){a.value?.onPositionChange(e)}function p(e){V(()=>{o?.value?.[0]?.chart&&a.value&&a.value?.onPositionChange({chart:o.value[0].chart,currentMoveNumber:e})})}function m(e){i.value=i.value===e?void 0:e,r(`change-active-tab`,i.value)}function h(){s.value=u(),V(()=>{o.value?.[0].update()})}return(t,n)=>(U(),R(`div`,{class:H([t.$style.component,{[t.$style.expanded]:c.value}])},[z(`div`,{class:H(t.$style[`data-parent`])},[c.value?(U(),R(`div`,{key:0,class:H(t.$style.data)},[a.value?(U(),I(be,{key:0,ref_key:`chartEl`,ref:o,cla
```

<a id="FND-30075"></a>
## FND-30075 — Implementation component charts

Vue compiled component __name declaration. Name suggests charts; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0089
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
tion yn(e){_n(e),ee(e)}var bn=t((()=>{vn(),ae()})),xn,Sn=t((()=>{St(),pe(),te(),T(),gn(),o(),_e(),Se(),bn(),me(),xn=Oe({__name:`charts`,setup(e){let t=F(()=>de.chartsEnabled&&fe()&&!S.isBasicAnalysis);ke(()=>{yn(t.value)}),W(()=>t.value,yn);let n=F(()=>({avgDiff:S.averageDifference,currentMoveNumber:-1,initialPly:0,moveTimes:S.time?.moves,phases:S.gamePhases,positions:re(),themes:S.themes.moves})),r=F(Te),i=F(()=>Object.values(hn).filter(e=>e?.shouldShow()));function a(e){D.emit(y.Events.ChangeActiveTab,{tab:e})}return(e,o)=>t.value?(U(),I(xt,{key:0,"base-options":n.value,"main-line-parent-move-number":r.value,tabs:i.value,onChangeActiveTab:a},null,8,[`base-options`,`main-line-parent-move-number`,`tabs`])):L(``,!0)}})})),Cn=n({default:()=>Tn}),wn,Tn,En=t((()=>{Sn(),Sn(),nt(),v(),wn={$style:tt},Tn=u(xn,[[`__cssModules`,wn]])}));export{En as n,Cn as t};
```

<a id="FND-30076"></a>
## FND-30076 — Implementation component cc-icon

Vue compiled component __name declaration. Name suggests cc icon; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0090, SRC-0751
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
role`],ko=[`alt`,`aria-hidden`,`height`,`src`,`width`],Ao=[`aria-hidden`,`aria-label`,`role`],jo=[`data-glyph`],Mo=x(u({__name:`cc-icon`,props:{alt:{},color:{},customSize:{},host:{default:`https://assets-ds.chess.com`},is:{},name:{},size:{default:24},variant:{default:`glyph`}},setup(e){let t=e,r=n(()=>t.customSize?t.customSize:t.size),a=n(()=>t.customSize?`${t.customSize/10}rem`:void 0),c=n(()=>t.host.replace(/\/+$/,``)),l=n(()=>`${c.value}/color-icons/${t.name}.svg`),u=n(()=>`${c.value}/glyphs/${t.name}.svg`);return(t,n)=>e.is?(p(),o(`span`,{key:0,"aria-hidden":e.alt?void 0:`true`,"aria-label":e.alt?e.alt:void 0,class:d([t.$style[`cc-icon-glyph`],e.customSize?null:t.$style[`cc-icon-size-${e.size}`]]),role:e.alt?`img`:void 0,style:f({color:e.color,"--cc-icon-size":a.value})},[(p(),i(te(e.is),{height:r.value,width:r.value},null,8,[`height`,`width`]))],14,Oo)):e.variant===`color`?(p(),o(`img`,{key:1,"data-cy":`cc-icon`,alt:e.alt?e.alt:e.name,"aria-hidden":e.alt?void 0:`true`,class:d([t.$style[`cc-icon-img`],e.customSize?null:t.$style[`cc-icon-size-${e.size}`]]),height:r.value,src:l.value,style:f({"--cc-icon-size":a.value}),width:r.value},null,14,ko)):(p(),o(`span`,{key:2,"aria-hidden":e.alt?void 0:`true
```

<a id="FND-30077"></a>
## FND-30077 — Implementation component cc-loader

Vue compiled component __name declaration. Name suggests cc loader; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0090, SRC-0751
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
-icon-size-48":`cc-icon-size-48_a20950e`,"cc-icon-size-64":`cc-icon-size-64_a20950e`}}]])})),Po,Fo=y((()=>{ve(),Po=x(u({__name:`cc-loader`,props:{size:{},variant:{default:`blocks`}},setup(e){return(n,r)=>e.variant===`blocks`?(p(),o(`div`,{key:0,"aria-busy":`true`,"aria-live":`polite`,class:d([n.$style[`cc-loader-component`],n.$style[`cc-loader-${e.size}`]])},[(p(),o(t,null,g(6,e=>s(`div`,{key:e,class:d([n.$style[`cc-loader-square`],n.$style[`cc-loader-square-${e}`]])},null,2)),64))],2)):(p(),o(`div`,{key:1,"aria-busy":`true`,"aria-live":`polite`,class:d([n.$style[`cc-loader-spinner`],n.$style[`cc-loader-${e.size}`],n.$style[`cc-loader-${e.variant}`]])},null,2))}}),[[`__cssModules`,{$style:{"cc-loader-component":`cc-loader-component_1e4c4f9`,"cc-loader-spinner":`cc-loader-spinner_1e4c4f9`,"cc-loader-spin":`cc-loader-spin_1e4c4f9`,"cc-loader-small":`cc-loader-small_1e4c4f9`,"cc-loader-medium":`cc-loader-medium_1e4c4f9`,"cc-loader-large":`cc-loader-large_1e4c4f9`,"cc-loader-spinner-green":`cc-loader-spinner-green_1e4c4f9`,"cc-loader-spinner-gray":`cc-loader-spinner-gray_1e4c4f9`,"cc-loader-spinner-chameleon":`cc-loader-spinner-chameleon_1e4c4f9`,"cc-loader-square":`cc-loader-square_1e4c4f9`,"cc-loader-sq
```

<a id="FND-30078"></a>
## FND-30078 — Implementation component cc-button

Vue compiled component __name declaration. Name suggests cc button; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0090, SRC-0751
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
`large`},"xx-large":{iconSize:32,imgSize:32,loaderSize:`large`}},Lo=[`height`,`src`,`width`],Ro=[`textContent`],zo=x(u({__name:`cc-button`,props:{align:{default:`center`},customClasses:{},customImgSrc:{},disabled:{type:Boolean},fullWidth:{type:Boolean},href:{},icon:{},isOneLineText:{type:Boolean},label:{},loading:{type:Boolean},minWidth:{type:Boolean},routerLink:{},selectedBorder:{type:Boolean},size:{default:`medium`},type:{default:`button`},variant:{default:`secondary`}},emits:[`click`,`contextmenu`,`touchend`,`touchstart`],setup(e){let t=e,r=n(()=>t.routerLink?`router-link`:t.href?`a`:`button`),s=n(()=>{if(r.value===`button`)return t.disabled||t.loading?!0:void 0}),c=n(()=>Io[t.size].iconSize),l=n(()=>Io[t.size].loaderSize);return(t,n)=>(p(),i(te(r.value),{class:d([t.$style[`cc-button-component`],t.$style[`cc-button-${e.variant}`],t.$style[`cc-button-${e.size}`],{[t.$style[`cc-button-full`]]:e.fullWidth,[t.$style[`cc-button-disabled`]]:e.disabled,[t.$style[`cc-button-loading`]]:e.loading,[t.$style[`cc-button-min-width`]]:e.minWidth,[t.$style[`cc-button-selected-border`]]:e.selectedBorder,[t.$style[`cc-button-align-start`]]:e.align===`start`}]),"data-align":e.align,"data-disabled":e.disabled?`true`:`
```

<a id="FND-30079"></a>
## FND-30079 — Implementation component bottom-banner

Vue compiled component __name declaration. Name suggests bottom banner; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0090, SRC-0751
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
),qo=Mo})),Yo,Xo=y((()=>{Jo(),Jo(),Yo=qo})),Zo,Qo,$o,es=y((()=>{Do(),Go(),Xo(),Zo=[`innerHTML`],Qo=[`aria-label`],$o=u({__name:`bottom-banner`,props:{hide:{type:Function},message:{},show:{type:Boolean},additionalButtonText:{},additionalButtonAction:{type:Function},icon:{},iconColor:{}},setup(e){return(t,n)=>e.show?(p(),o(`div`,{key:0,class:d(t.$style.component)},[s(`div`,{class:d(t.$style.wrapper)},[s(`div`,{class:d(t.$style.content)},[e.icon?(p(),i(Yo,{key:0,is:e.icon,variant:`glyph`,class:d([t.$style.icon,e.iconColor&&t.$style[e.iconColor]]),size:20},null,8,[`is`,`class`])):a(``,!0),n[1]||=c(),s(`span`,{class:d(t.$style.message),innerHTML:e.message},null,10,Zo)],2),n[2]||=c(),e.additionalButtonText?(p(),i(Wo,{key:0,variant:`primary`,class:d(t.$style.button),label:e.additionalButtonText,onClick:e.additionalButtonAction},null,8,[`class`,`label`,`onClick`])):a(``,!0)],2),n[3]||=c(),s(`button`,{"aria-label":t.$trans(`Close`),class:d(t.$style.close),onClick:n[0]||=(...t)=>e.hide&&e.hide(...t)},[l(Yo,{is:_(xo),variant:`glyph`,size:20},null,8,[`is`])],10,Qo)],2)):a(``,!0)}})})),ts,ns,rs=y((()=>{es(),es(),Zt(),_e(),ts={$style:Xt},ns=b($o,[[`__cssModules`,ts]])})),is,as,os,ss=y((()=>{$a(),Bi(),window.chessco
```

<a id="FND-30080"></a>
## FND-30080 — Implementation component adblocker-check

Vue compiled component __name declaration. Name suggests adblocker check; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0090, SRC-0751
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
ods:[],schemes:[`https`]}}),xs=window.context,Ss=()=>xs.user?.isPremium})),ws,Ts=y((()=>{Do(),rs(),hn(),ss(),Cs(),ws=u({__name:`adblocker-check`,setup(e){let t=Date.now()+10080*60*1e3,n=h(us()&&!Ss()),r=()=>{mn.set(`adblockerMessageExpiration`,t),n.value=!1};return(e,t)=>(p(),i(ns,{"icon-color":`blue`,hide:r,icon:_(wo),message:_(os),show:n.value},null,8,[`icon`,`message`,`show`]))}})})),Es,Ds=y((()=>{Ts(),Ts(),Es=ws}));function Os(){let e=Date.now(),t=document.querySelector(`body`),n=document.createElement(`div`);if(n.innerHTML=`&nbsp;`,n.className=`adsbox`,t.appendChild(n),n.offsetHeight===0){if(t.classList.add(`adblock`),mn.get(`adblockerMessageExpiration`)>e)return;ks.createInstance(`AdblockerCheck`)}n.parentNode.removeChild(n)}var ks,As,js;y((()=>{hn(),bo(),$a(),Ds(),ss(),window.chesscom=window.chesscom||{},window.chesscom.routes=window.chesscom.routes||{},Object.assign(window.chesscom.routes,{web_membership:{tokens:[[`text`,`/membership`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr
```

<a id="FND-30081"></a>
## FND-30081 — Implementation component leaderboard-ad

Vue compiled component __name declaration. Name suggests leaderboard ad; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0201
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
a.isUserGeneratedContent?.()&&kr(`page-content`)}var _E=t((()=>{ua(),Fo()})),vE,yE,bE=t((()=>{Eu(),ko(),vE=[`id`],yE=K({__name:`leaderboard-ad`,props:{slotId:{},variant:{default:`leaderboard`}},setup(e){return(t,n)=>(J(),H(`div`,{class:q([t.$style.component,t.$style[e.variant],{[t.$style[`with-report-ad`]]:Z(Gr)()}])},[U(`div`,{class:q(t.$style.slot),id:e.slotId},null,10,vE),n[0]||=W(),Z(Gr)()?(J(),B(Qt,{key:0,"slot-id":e.slotId},null,8,[`slot-id`])):V(``,!0)],2))}})})),xE,SE,CE=t((()=>{bE(),bE(),sg(),C(),xE={$style:og},SE=S(yE,[[`__cssModules`,xE]])})),wE,TE=t((()=>{hr(),CE(),wE=K({__name:`leaderboard-atf-ad`,setup(e){return(e,t)=>(J(),B(SE,{"slot-id":Z(sn).leaderboardAtf},null,8,[`slot-id`]))}})})),EE,DE=t((()=>{TE(),TE(),EE=wE})),OE,kE=t((()=>{hr(),CE(),OE=K({__name:`leaderboard-btf-ad`,setup(e){return(e,t)=>(J(),B(SE,{"slot-id":Z(sn).leaderboardBtf},null,8,[`slot-id`]))}})})),AE,jE=t((()=>{kE(),kE(),AE=OE})),ME,NE,PE=t((()=>{Eu(),Ua(),ko(),ME=[`id`],NE=K({__name:`medium-rectangle-ad`,props:{slotId:{}},setup(e){return(t,n)=>(J(),H(`div`,{class:q([t.$style.component,{[t.$style[`with-report-ad`]]:Z(Gr)()}])},[U(`div`,{class:q(t.$style.slot),id:e.slotId},null,10,ME),n[0]||=W(),G(hn),n[1]||=W(),Z(Gr)()
```

<a id="FND-30082"></a>
## FND-30082 — Implementation component leaderboard-atf-ad

Vue compiled component __name declaration. Name suggests leaderboard atf ad; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0201
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
)})),xE,SE,CE=t((()=>{bE(),bE(),sg(),C(),xE={$style:og},SE=S(yE,[[`__cssModules`,xE]])})),wE,TE=t((()=>{hr(),CE(),wE=K({__name:`leaderboard-atf-ad`,setup(e){return(e,t)=>(J(),B(SE,{"slot-id":Z(sn).leaderboardAtf},null,8,[`slot-id`]))}})})),EE,DE=t((()=>{TE(),TE(),EE=wE})),OE,kE=t((()=>{hr(),CE(),OE=K({__name:`leaderboard-btf-ad`,setup(e){return(e,t)=>(J(),B(SE,{"slot-id":Z(sn).leaderboardBtf},null,8,[`slot-id`]))}})})),AE,jE=t((()=>{kE(),kE(),AE=OE})),ME,NE,PE=t((()=>{Eu(),Ua(),ko(),ME=[`id`],NE=K({__name:`medium-rectangle-ad`,props:{slotId:{}},setup(e){return(t,n)=>(J(),H(`div`,{class:q([t.$style.component,{[t.$style[`with-report-ad`]]:Z(Gr)()}])},[U(`div`,{class:q(t.$style.slot),id:e.slotId},null,10,ME),n[0]||=W(),G(hn),n[1]||=W(),Z(Gr)()?(J(),B(Qt,{key:0,"slot-id":e.slotId},null,8,[`slot-id`])):V(``,!0)],2))}})})),FE,IE,LE=t((()=>{PE(),PE(),Hg(),C(),FE={$style:Vg},IE=S(NE,[[`__cssModules`,FE]])})),RE,zE=t((()=>{hr(),LE(),RE=K({__name:`medium-rectangle-atf-ad`,setup(e){return(e,t)=>(J(),B(IE,{"slot-id":Z(sn).mediumRectangleAtf},null,8,[`slot-id`]))}})})),BE,VE=t((()=>{zE(),zE(),BE=RE})),HE,UE=t((()=>{hr(),LE(),HE=K({__name:`medium-rectangle-btf-ad`,setup(e){return(e,t)=>(J(),B(IE,{"slot-id":Z(sn).me
```

<a id="FND-30083"></a>
## FND-30083 — Implementation component leaderboard-btf-ad

Vue compiled component __name declaration. Name suggests leaderboard btf ad; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0201
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
lot-id":Z(sn).leaderboardAtf},null,8,[`slot-id`]))}})})),EE,DE=t((()=>{TE(),TE(),EE=wE})),OE,kE=t((()=>{hr(),CE(),OE=K({__name:`leaderboard-btf-ad`,setup(e){return(e,t)=>(J(),B(SE,{"slot-id":Z(sn).leaderboardBtf},null,8,[`slot-id`]))}})})),AE,jE=t((()=>{kE(),kE(),AE=OE})),ME,NE,PE=t((()=>{Eu(),Ua(),ko(),ME=[`id`],NE=K({__name:`medium-rectangle-ad`,props:{slotId:{}},setup(e){return(t,n)=>(J(),H(`div`,{class:q([t.$style.component,{[t.$style[`with-report-ad`]]:Z(Gr)()}])},[U(`div`,{class:q(t.$style.slot),id:e.slotId},null,10,ME),n[0]||=W(),G(hn),n[1]||=W(),Z(Gr)()?(J(),B(Qt,{key:0,"slot-id":e.slotId},null,8,[`slot-id`])):V(``,!0)],2))}})})),FE,IE,LE=t((()=>{PE(),PE(),Hg(),C(),FE={$style:Vg},IE=S(NE,[[`__cssModules`,FE]])})),RE,zE=t((()=>{hr(),LE(),RE=K({__name:`medium-rectangle-atf-ad`,setup(e){return(e,t)=>(J(),B(IE,{"slot-id":Z(sn).mediumRectangleAtf},null,8,[`slot-id`]))}})})),BE,VE=t((()=>{zE(),zE(),BE=RE})),HE,UE=t((()=>{hr(),LE(),HE=K({__name:`medium-rectangle-btf-ad`,setup(e){return(e,t)=>(J(),B(IE,{"slot-id":Z(sn).mediumRectangleBtf},null,8,[`slot-id`]))}})})),WE,GE=t((()=>{UE(),UE(),WE=HE}));function KE(e){Vo(hs.WithUnd,e)}var qE=t((()=>{Ui(),rs()}));function JE(e,t){wf([t]),setTimeout(Cr,10)}va
```

<a id="FND-30084"></a>
## FND-30084 — Implementation component medium-rectangle-ad

Vue compiled component __name declaration. Name suggests medium rectangle ad; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0201
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
erboardBtf},null,8,[`slot-id`]))}})})),AE,jE=t((()=>{kE(),kE(),AE=OE})),ME,NE,PE=t((()=>{Eu(),Ua(),ko(),ME=[`id`],NE=K({__name:`medium-rectangle-ad`,props:{slotId:{}},setup(e){return(t,n)=>(J(),H(`div`,{class:q([t.$style.component,{[t.$style[`with-report-ad`]]:Z(Gr)()}])},[U(`div`,{class:q(t.$style.slot),id:e.slotId},null,10,ME),n[0]||=W(),G(hn),n[1]||=W(),Z(Gr)()?(J(),B(Qt,{key:0,"slot-id":e.slotId},null,8,[`slot-id`])):V(``,!0)],2))}})})),FE,IE,LE=t((()=>{PE(),PE(),Hg(),C(),FE={$style:Vg},IE=S(NE,[[`__cssModules`,FE]])})),RE,zE=t((()=>{hr(),LE(),RE=K({__name:`medium-rectangle-atf-ad`,setup(e){return(e,t)=>(J(),B(IE,{"slot-id":Z(sn).mediumRectangleAtf},null,8,[`slot-id`]))}})})),BE,VE=t((()=>{zE(),zE(),BE=RE})),HE,UE=t((()=>{hr(),LE(),HE=K({__name:`medium-rectangle-btf-ad`,setup(e){return(e,t)=>(J(),B(IE,{"slot-id":Z(sn).mediumRectangleBtf},null,8,[`slot-id`]))}})})),WE,GE=t((()=>{UE(),UE(),WE=HE}));function KE(e){Vo(hs.WithUnd,e)}var qE=t((()=>{Ui(),rs()}));function JE(e,t){wf([t]),setTimeout(Cr,10)}var YE=t((()=>{Qn(),Mn()}));function XE(e,t){return e/t>=2?sn.skyscraperWide:sn.skyscraper}var ZE=t((()=>{hr()})),QE,$E,eD=t((()=>{Eu(),Ua(),ko(),QE=[`id`],$E=K({__name:`skyscraper-ad`,props:{id:{}},setu
```

<a id="FND-30085"></a>
## FND-30085 — Implementation component medium-rectangle-atf-ad

Vue compiled component __name declaration. Name suggests medium rectangle atf ad; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0201
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
)})),FE,IE,LE=t((()=>{PE(),PE(),Hg(),C(),FE={$style:Vg},IE=S(NE,[[`__cssModules`,FE]])})),RE,zE=t((()=>{hr(),LE(),RE=K({__name:`medium-rectangle-atf-ad`,setup(e){return(e,t)=>(J(),B(IE,{"slot-id":Z(sn).mediumRectangleAtf},null,8,[`slot-id`]))}})})),BE,VE=t((()=>{zE(),zE(),BE=RE})),HE,UE=t((()=>{hr(),LE(),HE=K({__name:`medium-rectangle-btf-ad`,setup(e){return(e,t)=>(J(),B(IE,{"slot-id":Z(sn).mediumRectangleBtf},null,8,[`slot-id`]))}})})),WE,GE=t((()=>{UE(),UE(),WE=HE}));function KE(e){Vo(hs.WithUnd,e)}var qE=t((()=>{Ui(),rs()}));function JE(e,t){wf([t]),setTimeout(Cr,10)}var YE=t((()=>{Qn(),Mn()}));function XE(e,t){return e/t>=2?sn.skyscraperWide:sn.skyscraper}var ZE=t((()=>{hr()})),QE,$E,eD=t((()=>{Eu(),Ua(),ko(),QE=[`id`],$E=K({__name:`skyscraper-ad`,props:{id:{}},setup(e){return(t,n)=>(J(),H(`div`,{class:q([t.$style.component,{[t.$style[`with-report-ad`]]:Z(Gr)()}])},[U(`div`,{class:q(t.$style.slot),id:e.id},null,10,QE),n[0]||=W(),G(hn),n[1]||=W(),Z(Gr)()?(J(),B(Qt,{key:0,"slot-id":e.id},null,8,[`slot-id`])):V(``,!0)],2))}})})),tD,nD,rD=t((()=>{eD(),eD(),qg(),C(),tD={$style:Kg},nD=S($E,[[`__cssModules`,tD]])})),iD,aD=t((()=>{Vd(),qE(),YE(),ZE(),yo(),rD(),iD=K({__name:`skyscraper-ad`,setup(e){let t=j
```

<a id="FND-30086"></a>
## FND-30086 — Implementation component medium-rectangle-btf-ad

Vue compiled component __name declaration. Name suggests medium rectangle btf ad; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0201
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
id":Z(sn).mediumRectangleAtf},null,8,[`slot-id`]))}})})),BE,VE=t((()=>{zE(),zE(),BE=RE})),HE,UE=t((()=>{hr(),LE(),HE=K({__name:`medium-rectangle-btf-ad`,setup(e){return(e,t)=>(J(),B(IE,{"slot-id":Z(sn).mediumRectangleBtf},null,8,[`slot-id`]))}})})),WE,GE=t((()=>{UE(),UE(),WE=HE}));function KE(e){Vo(hs.WithUnd,e)}var qE=t((()=>{Ui(),rs()}));function JE(e,t){wf([t]),setTimeout(Cr,10)}var YE=t((()=>{Qn(),Mn()}));function XE(e,t){return e/t>=2?sn.skyscraperWide:sn.skyscraper}var ZE=t((()=>{hr()})),QE,$E,eD=t((()=>{Eu(),Ua(),ko(),QE=[`id`],$E=K({__name:`skyscraper-ad`,props:{id:{}},setup(e){return(t,n)=>(J(),H(`div`,{class:q([t.$style.component,{[t.$style[`with-report-ad`]]:Z(Gr)()}])},[U(`div`,{class:q(t.$style.slot),id:e.id},null,10,QE),n[0]||=W(),G(hn),n[1]||=W(),Z(Gr)()?(J(),B(Qt,{key:0,"slot-id":e.id},null,8,[`slot-id`])):V(``,!0)],2))}})})),tD,nD,rD=t((()=>{eD(),eD(),qg(),C(),tD={$style:Kg},nD=S($E,[[`__cssModules`,tD]])})),iD,aD=t((()=>{Vd(),qE(),YE(),ZE(),yo(),rD(),iD=K({__name:`skyscraper-ad`,setup(e){let t=jp(),n=z(()=>XE(t.width.value,t.height.value));return bh(()=>bn(),KE,{immediate:!0}),bh(()=>n.value,JE),(e,t)=>Z(bn)()?(J(),B(nD,{id:n.value,key:n.value},null,8,[`id`])):V(``,!0)}})})),oD,sD=t(
```

<a id="FND-30087"></a>
## FND-30087 — Implementation component skyscraper-ad

Vue compiled component __name declaration. Name suggests skyscraper ad; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0201
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
t){return e/t>=2?sn.skyscraperWide:sn.skyscraper}var ZE=t((()=>{hr()})),QE,$E,eD=t((()=>{Eu(),Ua(),ko(),QE=[`id`],$E=K({__name:`skyscraper-ad`,props:{id:{}},setup(e){return(t,n)=>(J(),H(`div`,{class:q([t.$style.component,{[t.$style[`with-report-ad`]]:Z(Gr)()}])},[U(`div`,{class:q(t.$style.slot),id:e.id},null,10,QE),n[0]||=W(),G(hn),n[1]||=W(),Z(Gr)()?(J(),B(Qt,{key:0,"slot-id":e.id},null,8,[`slot-id`])):V(``,!0)],2))}})})),tD,nD,rD=t((()=>{eD(),eD(),qg(),C(),tD={$style:Kg},nD=S($E,[[`__cssModules`,tD]])})),iD,aD=t((()=>{Vd(),qE(),YE(),ZE(),yo(),rD(),iD=K({__name:`skyscraper-ad`,setup(e){let t=jp(),n=z(()=>XE(t.width.value,t.height.value));return bh(()=>bn(),KE,{immediate:!0}),bh(()=>n.value,JE),(e,t)=>Z(bn)()?(J(),B(nD,{id:n.value,key:n.value},null,8,[`id`])):V(``,!0)}})})),oD,sD=t((()=>{aD(),aD(),oD=iD}));async function cD(){let e={skyscraper:`#sidebar-ad`,leaderboardAtf:`#leaderboard-atf-ad`,leaderboardBtf:`#leaderboard-btf-ad`,mediumRectangleAtf:`#medium-rectangle-atf-ad`,mediumRectangleBtf:`#medium-rectangle-btf-ad`},t={};document.querySelector(e.skyscraper)&&(t[e.skyscraper]=oD),document.querySelector(e.leaderboardAtf)&&(t[e.leaderboardAtf]=EE),document.querySelector(e.leaderboardBtf)&&(t[e.leade
```

<a id="FND-30088"></a>
## FND-30088 — Implementation component skyscraper-ad

Vue compiled component __name declaration. Name suggests skyscraper ad; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0201
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
>{eD(),eD(),qg(),C(),tD={$style:Kg},nD=S($E,[[`__cssModules`,tD]])})),iD,aD=t((()=>{Vd(),qE(),YE(),ZE(),yo(),rD(),iD=K({__name:`skyscraper-ad`,setup(e){let t=jp(),n=z(()=>XE(t.width.value,t.height.value));return bh(()=>bn(),KE,{immediate:!0}),bh(()=>n.value,JE),(e,t)=>Z(bn)()?(J(),B(nD,{id:n.value,key:n.value},null,8,[`id`])):V(``,!0)}})})),oD,sD=t((()=>{aD(),aD(),oD=iD}));async function cD(){let e={skyscraper:`#sidebar-ad`,leaderboardAtf:`#leaderboard-atf-ad`,leaderboardBtf:`#leaderboard-btf-ad`,mediumRectangleAtf:`#medium-rectangle-atf-ad`,mediumRectangleBtf:`#medium-rectangle-btf-ad`},t={};document.querySelector(e.skyscraper)&&(t[e.skyscraper]=oD),document.querySelector(e.leaderboardAtf)&&(t[e.leaderboardAtf]=EE),document.querySelector(e.leaderboardBtf)&&(t[e.leaderboardBtf]=AE),document.querySelector(e.mediumRectangleAtf)&&(t[e.mediumRectangleAtf]=BE),document.querySelector(e.mediumRectangleBtf)&&(t[e.mediumRectangleBtf]=WE),await Oa(t)}var lD=t((()=>{DE(),jE(),VE(),GE(),sD(),w()}));function uD(){let e=Ae();!m_()||e.adTimingMetricsRecorded||(e.adTimingMetricsRecorded=!0,Mt(`adsClientStart`,performance.now()),window.googletag=window.googletag||{cmd:[]},window.googletag.cmd.push(()=>{Mt(`adsTagLoade
```

<a id="FND-30089"></a>
## FND-30089 — Implementation component board-controls

Vue compiled component __name declaration. Name suggests board controls; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0201
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
s:iA,hooks:Object.assign({onBeforeInit(){be()}},e)})}var sA=t((()=>{w(),Rm(),cE(),aA()})),cA,lA=t((()=>{Ru(),Sf(),cA=K({__name:`board-controls`,props:{isBoardImagesPaletteVisible:{type:Boolean},isMenuIconVisible:{type:Boolean},isFocusModeSupported:{type:Boolean}},emits:[`click-board-images-palette`,`click-settings`,`click-focus`,`click-theatre`,`click-flip`,`click-menu`],setup(e){let t=window.chesscom.features.includes(`cc_ds_light_mode`);return(n,r)=>(J(),H(`div`,{class:q({"dark-mode":!Z(t)})},[G(cr,{id:`board-controls-settings`,class:q(n.$style.button),tooltip:{text:n.$trans(`Settings`),position:`right`},size:`small`,icon:{variant:`glyph`,is:Z(Um)},"icon-size":16,onClick:r[0]||=e=>n.$emit(`click-settings`)},null,8,[`class`,`tooltip`,`icon`]),r[6]||=W(),Y(n.$slots,`voice-move-icon`,{hoverClass:n.$style.hover}),r[7]||=W(),e.isFocusModeSupported?(J(),B(cr,{key:0,id:`board-controls-focus`,class:q([n.$style.button,n.$style.hover]),tooltip:{text:n.$trans(`Focus Mode`),position:`right`},size:`small`,icon:{variant:`glyph`,is:Z(ii)},"icon-size":16,onClick:r[1]||=e=>n.$emit(`click-focus`)},null,8,[`class`,`tooltip`,`icon`])):V(``,!0),r[8]||=W(),e.isFocusModeSupported?(J(),B(cr,{key:1,id:`board-controls-theatr
```

<a id="FND-30090"></a>
## FND-30090 — Implementation component voice-move-icon

Vue compiled component __name declaration. Name suggests voice move icon; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0201
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
t((()=>{lA(),lA(),Uv(),C(),uA={$style:Hv},dA=S(cA,[[`__cssModules`,uA]])})),pA,mA=t((()=>{Ru(),Sf(),j(),Rf(),gp(),pA=K({__name:`voice-move-icon`,props:{hoverClass:{},voiceRecognizerStatus:{},voiceMicrophoneStatus:{}},emits:[`click`],setup(e){let t=e,n=Q(),r=z(()=>{switch(t.voiceRecognizerStatus){case D.Disabled:return k(`Click to enable voice move`);case D.Enabled:case D.Loading:return k(`Enabling voice move...`);default:break}switch(t.voiceMicrophoneStatus){case Ld.Pending:return k(`Waiting for microphone permission`);case Ld.Denied:return k(`Microphone permission denied`);default:return k(`Hold SPACE to speak your move`)}}),i=z(()=>{switch(t.voiceRecognizerStatus){case D.Disabled:return Ff;default:break}switch(t.voiceMicrophoneStatus){case Ld.Denied:return Zs;default:return pp}}),a=z(()=>{switch(t.voiceMicrophoneStatus){case Ld.Denied:return n.error;default:break}switch(t.voiceRecognizerStatus){case D.Listening:case D.Starting:return n.listening;case D.Stopping:case D.Idle:return n.idle;case D.Error:return n.error;default:return``}}),o=z(()=>({[n.button]:!0,[a.value]:!0,[t.hoverClass]:t.voiceRecognizerStatus===D.Disabled}));return(e,t)=>(J(),B(cr,{id:`board-controls-voice-move`,class:q(o.value),tool
```

<a id="FND-30091"></a>
## FND-30091 — Implementation component board-controls

Vue compiled component __name declaration. Name suggests board controls; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0201
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
=>{wa()})),EA,DA=t((()=>{fO(),tc(),il(),fA(),_A(),Df(),Vi(),Zr(),_e(),yA(),xA(),Jp(),Er(),$o(),E(),CA(),TA(),_o(),EA=K({__name:`board-controls`,setup(e){let t=dA,n=Ad(),r=pu({activeBoard(){return ps()},isBoardImagesPaletteVisible(){return!!this.activeBoard},isMenuIconVisible(){return bA()||ju()},isFocusModeSupported(){return n.value&&vA()},voiceMicrophoneStatus(){return wA()},voiceRecognizerStatus(){return ke()}});function i({target:e}){dO(e)}function a(){if(!O()){Im();return}ca()}function o(){_r()}function s(){Ht()}function c(){di()}function ee(){di(!1)}function te(){SA()}return(e,ne)=>(J(),B(Z(t),{"is-board-images-palette-visible":Z(r).isBoardImagesPaletteVisible,"is-menu-icon-visible":Z(r).isMenuIconVisible,"is-focus-mode-supported":Z(r).isFocusModeSupported,onClickBoardImagesPalette:i,onClickSettings:a,onClickFocus:s,onClickTheatre:c,onClickFlip:o,onClickMenu:ee},rh({_:2},[Z(n)?{name:`voice-move-icon`,fn:$(({hoverClass:e})=>[G(gA,{"hover-class":e,"voice-microphone-status":Z(r).voiceMicrophoneStatus,"voice-recognizer-status":Z(r).voiceRecognizerStatus,onClick:te},null,8,[`hover-class`,`voice-microphone-status`,`voice-recognizer-status`])]),key:`0`}:void 0]),1032,[`is-board-images-palette-visible`,`
```

<a id="FND-30092"></a>
## FND-30092 — Implementation component captured-pieces-placeholder

Vue compiled component __name declaration. Name suggests captured pieces placeholder; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0201
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
t)=>Lv[e]-Lv[t]).map(r=>FA(r,t,e[r],n)).reduce((e,t)=>e.concat(t),[])})),RA,zA,BA=t((()=>{LA(),RA=[`textContent`],zA=K({__name:`captured-pieces-placeholder`,props:{material:{},color:{},verticalLayout:{type:Boolean}},setup(e){let t=Q(),n=e,r=z(()=>{if(!n.material)return[];let e=n.color===1?`white`:`black`,t=n.color===1?`b`:`w`;return IA(n.material[e]??{},t,!1)}),i=z(()=>{if(n.material?.imbalance){if(n.color===1&&n.material.imbalance>0)return`+${n.material.imbalance}`;if(n.color===2&&n.material.imbalance<0)return`+${Math.abs(n.material.imbalance)}`}});function a(e){return e.split(` `).map(e=>t[e])}return(t,n)=>(J(),H(`div`,{class:q([t.$style.capturedPieces,{[t.$style.vertical]:e.verticalLayout}])},[(J(!0),H(Qm,null,hh(r.value,(e,t)=>(J(),H(`span`,{key:t,class:q(a(e))},null,2))),128)),n[0]||=W(),i.value?(J(),H(`span`,{key:0,class:q([t.$style.cpiece,t.$style.score]),textContent:X(i.value)},null,10,RA)):V(``,!0)],2))}})})),VA,HA,UA=t((()=>{BA(),BA(),Q_(),C(),VA={$style:Z_},HA=S(zA,[[`__cssModules`,VA]])})),WA,GA=t((()=>{Aa(),LA(),Br(),wu(),si(),Fv(),re(),WA=class extends le{static get observedAttributes(){return[Wr.ObservedAttributes.BoardId,Wr.ObservedAttributes.PlayerColor,Wr.ObservedAttributes.VerticalL
```

<a id="FND-30093"></a>
## FND-30093 — Implementation component arena-score

Vue compiled component __name declaration. Name suggests arena score; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0201
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
th.abs(this.capturedPieces.imbalance)}`),this.scoreElement.textContent=e}}})),KA,qA,JA=t((()=>{KA=[`textContent`],qA=K({__name:`arena-score`,props:{score:{},place:{}},setup(e){return(t,n)=>(J(),H(`div`,{class:q(t.$style.component)},[W(X(e.score)+` `,1),e.place?(J(),H(`span`,{key:0,class:q(t.$style.place),textContent:X(`#${e.place}`)},null,10,KA)):V(``,!0)],2))}})})),YA,XA,ZA=t((()=>{JA(),JA(),Pb(),C(),YA={$style:Nb},XA=S(qA,[[`__cssModules`,YA]])})),QA,$A=t((()=>{mn(),ls(),j(),QA=K({__name:`connection`,props:{tooltipPosition:{},connection:{},isCurrentUser:{type:Boolean}},setup(e){let t=e,n=Q(),r=z(()=>t.isCurrentUser&&t.connection===uo.Offline),i=z(()=>{switch(t.connection){case uo.Excellent:return k(`Excellent Connection (very low lag)`);case uo.Good:return k(`Good Connection (low lag)`);case uo.Ok:return k(`OK Connection (some lag)`);case uo.Poor:return k(`Poor Connection (high lag)`);case uo.Offline:return k(`Member Offline`);default:return``}}),a=z(()=>({[n.component]:!0,[n[t.connection]]:!0,[n.reconnecting]:r.value}));return(t,n)=>(J(),H(`div`,{class:q(a.value)},[G(Xn,{position:e.tooltipPosition,text:i.value},null,8,[`position`,`text`])],2))}})})),ej,tj,nj=t((()=>{$A(),$A(),Wb(),C(),ej={$style:Ub
```

<a id="FND-30094"></a>
## FND-30094 — Implementation component connection

Vue compiled component __name declaration. Name suggests connection; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0201
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
,YA,XA,ZA=t((()=>{JA(),JA(),Pb(),C(),YA={$style:Nb},XA=S(qA,[[`__cssModules`,YA]])})),QA,$A=t((()=>{mn(),ls(),j(),QA=K({__name:`connection`,props:{tooltipPosition:{},connection:{},isCurrentUser:{type:Boolean}},setup(e){let t=e,n=Q(),r=z(()=>t.isCurrentUser&&t.connection===uo.Offline),i=z(()=>{switch(t.connection){case uo.Excellent:return k(`Excellent Connection (very low lag)`);case uo.Good:return k(`Good Connection (low lag)`);case uo.Ok:return k(`OK Connection (some lag)`);case uo.Poor:return k(`Poor Connection (high lag)`);case uo.Offline:return k(`Member Offline`);default:return``}}),a=z(()=>({[n.component]:!0,[n[t.connection]]:!0,[n.reconnecting]:r.value}));return(t,n)=>(J(),H(`div`,{class:q(a.value)},[G(Xn,{position:e.tooltipPosition,text:i.value},null,8,[`position`,`text`])],2))}})})),ej,tj,nj=t((()=>{$A(),$A(),Wb(),C(),ej={$style:Ub},tj=S(QA,[[`__cssModules`,ej]])})),rj,ij,aj=t((()=>{rj=[`textContent`],ij=K({__name:`grudge-score`,props:{score:{}},setup(e){return(t,n)=>(J(),H(`div`,{class:q(t.$style.component),textContent:X(e.score?.toFixed(1))},null,10,rj))}})})),oj,sj,cj=t((()=>{aj(),aj(),qb(),C(),oj={$style:Kb},sj=S(ij,[[`__cssModules`,oj]])})),lj,uj,dj,fj,pj=t((()=>{ls(),xm(),Se(),j(),windo
```

<a id="FND-30095"></a>
## FND-30095 — Implementation component grudge-score

Vue compiled component __name declaration. Name suggests grudge score; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0201
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
j=t((()=>{$A(),$A(),Wb(),C(),ej={$style:Ub},tj=S(QA,[[`__cssModules`,ej]])})),rj,ij,aj=t((()=>{rj=[`textContent`],ij=K({__name:`grudge-score`,props:{score:{}},setup(e){return(t,n)=>(J(),H(`div`,{class:q(t.$style.component),textContent:X(e.score?.toFixed(1))},null,10,rj))}})})),oj,sj,cj=t((()=>{aj(),aj(),qb(),C(),oj={$style:Kb},sj=S(ij,[[`__cssModules`,oj]])})),lj,uj,dj,fj,pj=t((()=>{ls(),xm(),Se(),j(),window.chesscom=window.chesscom||{},window.chesscom.routes=window.chesscom.routes||{},Object.assign(window.chesscom.routes,{web_league_division:{tokens:[[`variable`,`/`,`[\\w]{6,}`,`division`,!0],[`variable`,`/`,`\\w+`,`league`,!0],[`text`,`/leagues`]],defaults:{host:`www.chess-dev.com`},requirements:{league:`\\w+`,division:`[\\w]{6,}`,host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it_IT|ja_JP|ka_GE|ko_KR|lt_LT|lv_LV|nl_BE|ms_MY|nl_NL|no_NO|pl_PL|pt_BR|pt_PT|ro_RO|ru_RU|sk_SK|sl_SI|sq_AL|sr_RS|sv_SE|tk_TM|tr_TR|uk_UA|ur_PK|vi_VN|zh_CN|zh_HK|zh_TW`},hosttokens:[[`variable`,``,`(?!admin)(?:www|
```

<a id="FND-30096"></a>
## FND-30096 — Implementation component league-badge

Vue compiled component __name declaration. Name suggests league badge; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0201
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
chy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}}),lj=[`href`],uj=[`alt`,`src`],dj=[`textContent`],fj=K({__name:`league-badge`,props:{leagueGameOver:{}},setup(e){let t=e,n=Q(),r=z(()=>`#${t.leagueGameOver.stats.ranking}`),i=z(()=>({[n.icon]:!0,[n.faded]:!t.leagueGameOver.isGameValid})),a=z(()=>!t.leagueGameOver.isGameValid||!t.leagueGameOver.division.league.code?zp(`bundles/web/images/color-icons/cup.svg`):zp(`bundles/web/images/leagues/badges/${t.leagueGameOver.division.league.code}.svg`)),o=z(()=>t.leagueGameOver.isGameValid?void 0:k(`This game does not qualify for League Points`)),s=z(()=>ao.generate(`web_league_division`,{league:t.leagueGameOver.division.league.name.toLowerCase(),division:t.leagueGameOver.division.name.slice(1)}));return(t,c)=>(J(),H(`div`,{class:q(Z(n).component)},[U(`a`,{href:s.value,target:`_blank`},[U(`img`,{width:`14`,height:`14`,alt:o.value,src:a.value,class:q(i.value)},null,10,uj),c[0]||=W(),o.value?(J(),B(Xn,{key:0,"for-previous-element":``,text:o.value},null,8,[`text`])):V(``,!0)],8,lj),c[1]||=W(),e.leagueGameOver.isGameValid?(J(),H(`span`,{key:0,textContent:X(r.value),class:q(Z(n).points)},null,10,dj)):V(``,!0)],2))}})})),mj,hj,gj=t((()=>{pj(),pj(),$b(),C(
```

<a id="FND-30097"></a>
## FND-30097 — Implementation component league-score

Vue compiled component __name declaration. Name suggests league score; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0201
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
pj(),pj(),$b(),C(),mj={$style:Qb},hj=S(fj,[[`__cssModules`,mj]])})),_j,vj,yj=t((()=>{eo(),gj(),_j=[`textContent`],vj=K({__name:`league-score`,props:{leagueGameOver:{}},setup(e){let t=e,n=Q(),r=z(()=>t.leagueGameOver.stats.rankingDelta),i=z(()=>Ro(r.value)),a=z(()=>r.value>0?n.positive:n.negative),o=z(()=>t.leagueGameOver.isGameValid);return(t,s)=>(J(),H(`div`,{class:q(Z(n).component)},[G(hj,{"league-game-over":e.leagueGameOver},null,8,[`league-game-over`]),s[0]||=W(),o.value?(J(),B(th,{key:0,appear:``,"enter-active-class":Z(n).fade},{default:$(()=>[r.value?(J(),H(`span`,{key:0,textContent:X(i.value),class:q([Z(n).change,a.value])},null,10,_j)):V(``,!0)]),_:1},8,[`enter-active-class`])):V(``,!0)],2))}})})),bj,xj,Sj=t((()=>{yj(),yj(),ox(),C(),bj={$style:ax},xj=S(vj,[[`__cssModules`,bj]])})),Cj,wj,Tj=t((()=>{Cj=[`textContent`],wj=K({__name:`animated-number`,props:{number:{},increment:{}},setup(e){let t=e,n=0,r=mh(t.number),i=e=>{ch(()=>{e.length&&(r.value+=e.shift()),e.length&&(n=window.setTimeout(i,40,e))})},a=()=>{let e=[],n=t.increment,r=Math.floor(n/10);for(let t=0;t<10;t++)n-=r,e.push(r);return n>0&&e.push(n),e};return fh(()=>{n=window.setTimeout(i,1e3,a())}),dh(()=>{n&&window.clearTimeout(n)}),bh((
```

<a id="FND-30098"></a>
## FND-30098 — Implementation component animated-number

Vue compiled component __name declaration. Name suggests animated number; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0201
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
j=t((()=>{yj(),yj(),ox(),C(),bj={$style:ax},xj=S(vj,[[`__cssModules`,bj]])})),Cj,wj,Tj=t((()=>{Cj=[`textContent`],wj=K({__name:`animated-number`,props:{number:{},increment:{}},setup(e){let t=e,n=0,r=mh(t.number),i=e=>{ch(()=>{e.length&&(r.value+=e.shift()),e.length&&(n=window.setTimeout(i,40,e))})},a=()=>{let e=[],n=t.increment,r=Math.floor(n/10);for(let t=0;t<10;t++)n-=r,e.push(r);return n>0&&e.push(n),e};return fh(()=>{n=window.setTimeout(i,1e3,a())}),dh(()=>{n&&window.clearTimeout(n)}),bh(()=>t.number,()=>{n&&window.clearTimeout(n),r.value=t.number+t.increment}),(e,t)=>(J(),H(`span`,{textContent:X(r.value)},null,8,Cj))}})})),Ej,Dj=t((()=>{Tj(),Tj(),Ej=wj})),Oj,kj,Aj,jj=t((()=>{eo(),Dj(),So(),Oj=[`textContent`],kj=[`textContent`],Aj=K({__name:`rating-score`,props:{timeControlIcon:{},rating:{},ratingChange:{}},setup(e){let t=e,n=Q(),r=z(()=>t.ratingChange===null?0:Ro(t.ratingChange)),i=z(()=>t.ratingChange===null||t.ratingChange>0?n.positive:n.negative);return(t,a)=>(J(),H(`div`,{class:q(Z(n).component)},[G(wn,{icon:e.timeControlIcon,class:q(Z(n).icon)},null,8,[`icon`,`class`]),a[1]||=W(),e.ratingChange===null?(J(),H(`span`,{key:0,textContent:X(e.rating),class:q(Z(n).rating)},null,10,Oj)):(J(),H(Qm,{
```

<a id="FND-30099"></a>
## FND-30099 — Implementation component rating-score

Vue compiled component __name declaration. Name suggests rating score; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0201
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
)}})})),Ej,Dj=t((()=>{Tj(),Tj(),Ej=wj})),Oj,kj,Aj,jj=t((()=>{eo(),Dj(),So(),Oj=[`textContent`],kj=[`textContent`],Aj=K({__name:`rating-score`,props:{timeControlIcon:{},rating:{},ratingChange:{}},setup(e){let t=e,n=Q(),r=z(()=>t.ratingChange===null?0:Ro(t.ratingChange)),i=z(()=>t.ratingChange===null||t.ratingChange>0?n.positive:n.negative);return(t,a)=>(J(),H(`div`,{class:q(Z(n).component)},[G(wn,{icon:e.timeControlIcon,class:q(Z(n).icon)},null,8,[`icon`,`class`]),a[1]||=W(),e.ratingChange===null?(J(),H(`span`,{key:0,textContent:X(e.rating),class:q(Z(n).rating)},null,10,Oj)):(J(),H(Qm,{key:1},[G(Ej,{number:e.rating-e.ratingChange,increment:e.ratingChange,class:q(Z(n).rating)},null,8,[`number`,`increment`,`class`]),a[0]||=W(),G(th,{appear:``,"enter-active-class":Z(n).fade},{default:$(()=>[U(`span`,{textContent:X(r.value),class:q([Z(n).change,i.value])},null,10,kj)]),_:1},8,[`enter-active-class`])],64))],2))}})})),Mj,Nj,Pj=t((()=>{jj(),jj(),Nx(),C(),Mj={$style:Mx},Nj=S(Aj,[[`__cssModules`,Mj]])})),Fj,Ij=t((()=>{Sj(),Pj(),Fj=K({__name:`player-game-over`,props:{isCurrentUser:{type:Boolean},leagueGameOver:{},rating:{},ratingChange:{},timeControlIcon:{}},setup(e){return(t,n)=>(J(),H(`div`,{class:q(t.$style.c
```

<a id="FND-30100"></a>
## FND-30100 — Implementation component player-game-over

Vue compiled component __name declaration. Name suggests player game over; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0201
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
)})),Mj,Nj,Pj=t((()=>{jj(),jj(),Nx(),C(),Mj={$style:Mx},Nj=S(Aj,[[`__cssModules`,Mj]])})),Fj,Ij=t((()=>{Sj(),Pj(),Fj=K({__name:`player-game-over`,props:{isCurrentUser:{type:Boolean},leagueGameOver:{},rating:{},ratingChange:{},timeControlIcon:{}},setup(e){return(t,n)=>(J(),H(`div`,{class:q(t.$style.component)},[G(Nj,{rating:e.rating,"time-control-icon":e.timeControlIcon,"rating-change":e.ratingChange},null,8,[`rating`,`time-control-icon`,`rating-change`]),n[0]||=W(),e.isCurrentUser&&e.leagueGameOver?(J(),B(xj,{key:0,"league-game-over":e.leagueGameOver},null,8,[`league-game-over`])):V(``,!0)],2))}})})),Lj,Rj,zj=t((()=>{Ij(),Ij(),lx(),C(),Lj={$style:cx},Rj=S(Fj,[[`__cssModules`,Lj]])})),Bj,Vj,Hj=t((()=>{j(),Me(),Bj=[`textContent`],Vj=K({__name:`seeking-tagline`,props:{isTheatre:{type:Boolean},challenge:{}},setup(e){let t=e,n=Q(),r=z(()=>({[n.component]:!0,[n.theatre]:t.isTheatre})),i=z(()=>{let e=t.challenge.getMaxRating(),n=t.challenge.getMinRating();return!e&&!n?``:k(`Rating Range: %rating%`,{"%rating%":`${n||k(`Any`)}-${e||k(`Any`)}`})}),a=z(()=>t.challenge.getTo()?k(`Waiting for Opponent`):k(`Searching`));return(t,n)=>(J(),H(`div`,{class:q(r.value)},[G(Zm,{class:q(t.$style.searching),text:a.value},nu
```

<a id="FND-30101"></a>
## FND-30101 — Implementation component seeking-tagline

Vue compiled component __name declaration. Name suggests seeking tagline; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0201
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
{Ij(),Ij(),lx(),C(),Lj={$style:cx},Rj=S(Fj,[[`__cssModules`,Lj]])})),Bj,Vj,Hj=t((()=>{j(),Me(),Bj=[`textContent`],Vj=K({__name:`seeking-tagline`,props:{isTheatre:{type:Boolean},challenge:{}},setup(e){let t=e,n=Q(),r=z(()=>({[n.component]:!0,[n.theatre]:t.isTheatre})),i=z(()=>{let e=t.challenge.getMaxRating(),n=t.challenge.getMinRating();return!e&&!n?``:k(`Rating Range: %rating%`,{"%rating%":`${n||k(`Any`)}-${e||k(`Any`)}`})}),a=z(()=>t.challenge.getTo()?k(`Waiting for Opponent`):k(`Searching`));return(t,n)=>(J(),H(`div`,{class:q(r.value)},[G(Zm,{class:q(t.$style.searching),text:a.value},null,8,[`class`,`text`]),n[0]||=W(),e.challenge.getTo()?V(``,!0):(J(),H(`span`,{key:0,class:q(t.$style.rating),textContent:X(i.value)},null,10,Bj))],2))}})})),Uj,Wj,Gj=t((()=>{Hj(),Hj(),zx(),C(),Uj={$style:Rx},Wj=S(Vj,[[`__cssModules`,Uj]])})),Kj,qj=t((()=>{Ru(),Vs(),ls(),j(),pa(),Kj=K({__name:`timeout-avatar`,props:{timeoutNotification:{},isTheatre:{type:Boolean},isEnglishLocale:{type:Boolean}},setup(e){let t=e,n=Q(),r=z(()=>({[n.component]:!0,[n.theatre]:t.isTheatre})),i=z(()=>t.timeoutNotification?.type===Mr.Offline||t.timeoutNotification?.type===Mr.OpponentOffline),a=z(()=>{if(i.value&&!t.isEnglishLocale)return k(`
```

<a id="FND-30102"></a>
## FND-30102 — Implementation component timeout-avatar

Vue compiled component __name declaration. Name suggests timeout avatar; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0201
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
t((()=>{Hj(),Hj(),zx(),C(),Uj={$style:Rx},Wj=S(Vj,[[`__cssModules`,Uj]])})),Kj,qj=t((()=>{Ru(),Vs(),ls(),j(),pa(),Kj=K({__name:`timeout-avatar`,props:{timeoutNotification:{},isTheatre:{type:Boolean},isEnglishLocale:{type:Boolean}},setup(e){let t=e,n=Q(),r=z(()=>({[n.component]:!0,[n.theatre]:t.isTheatre})),i=z(()=>t.timeoutNotification?.type===Mr.Offline||t.timeoutNotification?.type===Mr.OpponentOffline),a=z(()=>{if(i.value&&!t.isEnglishLocale)return k(`Disconnected.`)});return(e,t)=>(J(),H(`div`,{class:q(r.value)},[G(Xn,{text:a.value},null,8,[`text`]),t[0]||=W(),G(Il,{is:i.value?Z(Zl):Z(ip),variant:`glyph`,size:20},null,8,[`is`])],2))}})})),Jj,Yj,Xj=t((()=>{qj(),qj(),Ux(),C(),Jj={$style:Hx},Yj=S(Kj,[[`__cssModules`,Jj]])})),Zj,Qj=t((()=>{_f(),re(),Zj=class extends HTMLElement{constructor(...e){super(...e),Fu(this,`endTime`,1/0),Fu(this,`interval`,null),Fu(this,`timeLeft`,0)}connectedCallback(){this.initialize(),this.start()}initialize(){this.timeLeft=Number(this.getAttribute(`time-left`)),this.textContent=Jt(this.timeLeft)}start(){setTimeout(()=>{this.endTime=Date.now()+this.timeLeft,this.interval=setInterval(this.step.bind(this),100)},0)}step(){if(Date.now()>this.endTime){clearInterval(this.interval
```

<a id="FND-30103"></a>
## FND-30103 — Implementation component timeout-text

Vue compiled component __name declaration. Name suggests timeout text; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0201
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
lback(){clearInterval(this.interval),this.interval=null}}})),$j,eM,tM=t((()=>{Qj(),hi(),j(),pa(),$j=[`innerHTML`],eM=K({__name:`timeout-text`,props:{timeoutNotification:{},isTheatre:{type:Boolean},isEnglishLocale:{type:Boolean},position:{}},setup(e){Ke(`wc-count-down`,Zj);let t=e,n=Q(),r=z(()=>({[n.component]:!0,[n.theatre]:t.isTheatre,[n[t.position]]:!0})),i=z(()=>{let{timestamp:e,timeLeft:n}=t.timeoutNotification;return n?Math.max(n-(Date.now()-e),0):0}),a=z(()=>{let e=t.timeoutNotification.type;return e===Mr.AutoAbortOpponentTurn?As(`Waiting. Will auto-abort in %time%`,{"%time%":`<wc-count-down time-left="${i.value}"/>`}):e===Mr.AutoAbortMyTurn?As(`Your move. Will auto-abort in %time%`,{"%time%":`<wc-count-down time-left="${i.value}"/>`}):e===Mr.AutoResignOpponentTurn?As(`Auto-resign in %time%`,{"%time%":`<wc-count-down time-left="${i.value}"/>`}):e===Mr.AutoResignMyTurn?As(`Your move. Will auto-resign in %time%`,{"%time%":`<wc-count-down time-left="${i.value}"/>`}):e===Mr.OpponentOffline?t.isEnglishLocale?As(`Disconnected. Will auto-resign in %time%`,{"%time%":`<wc-count-down time-left="${i.value}"/>`}):As(`Will auto-resign in %time%`,{"%time%":`<wc-count-down time-left="${i.value}"/>`}):e===Mr.Of
```

<a id="FND-30104"></a>
## FND-30104 — Implementation component player

Vue compiled component __name declaration. Name suggests player; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0201
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
`,`host`,!0]],methods:[],schemes:[`https`]}}),aM=[`textContent`],oM=[`board-id`,`vertical-layout`,`player-color`],sM=K({__name:`player`,props:{arenaPlace:{},boardId:{},clubAvatar:{default:``},clubName:{default:``},color:{},connection:{default:null},contentKey:{default:``},country:{},flair:{default:null},fullName:{default:``},isGameOverVisible:{type:Boolean},isCapturedPiecesVisible:{type:Boolean},isCapturedPiecesPlaceholderVisible:{type:Boolean},isCurrentUser:{type:Boolean},isFocusMode:{type:Boolean},isOnline:{type:Boolean,default:!1},isEnglishLocale:{type:Boolean},isSeekingTaglineVisible:{type:Boolean,default:!1},outgoingChallenge:{},isTheatreMode:{type:Boolean},leagueGameOver:{},material:{default:null},membership:{},position:{},rating:{default:0},ratingChange:{default:0},ratingRange:{},shouldAnimateContent:{type:Boolean,default:!1},timeControlIcon:{},ratingType:{},score:{},showFullName:{type:Boolean},squares:{},timeoutNotification:{},title:{default:``},userAvatar:{default:``},username:{},showMembershipBadges:{type:Boolean}},emits:[`click-user`],setup(e,{emit:t}){let n=Q(),r=e,i=t,a=mh({}),o=z(()=>!!(r.isTheatreMode||r.isFocusMode)),s=window.chesscom.features.includes(`cc_ds_light_mode`)?`boldest`:`wh
```

<a id="FND-30105"></a>
## FND-30105 — Implementation component clock-arrow

Vue compiled component __name declaration. Name suggests clock arrow; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0201
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
t`)],2))}})})),lM,uM,dM=t((()=>{cM(),cM(),wx(),C(),lM={$style:Cx},uM=S(sM,[[`__cssModules`,lM]])})),fM,pM=t((()=>{fM=K({__name:`clock-arrow`,props:{playerIndex:{},position:{}},setup(e){let t=e,n=Q(),r=z(()=>({[n.arrow]:!0,[n[t.position]]:!0,[n.white]:t.playerIndex===0,[n.black]:t.playerIndex===1}));return(e,t)=>(J(),H(`div`,{class:q(r.value)},null,2))}})})),mM,hM,gM=t((()=>{pM(),pM(),ty(),C(),mM={$style:ey},hM=S(fM,[[`__cssModules`,mM]])})),_M,vM=t((()=>{_s(),_M=K({__name:`clock-bar`,props:{playerIndex:{},position:{},remainder:{}},setup(e){let t=e,n=Q(),r=z(()=>jf(t.remainder)?`linear-gradient(
      to right,
      var(--remainder-color) 0%,
      var(--remainder-color) ${t.remainder}%,
      var(--expired-color) ${t.remainder}%
    )`:void 0),i=z(()=>({[n.bar]:!0,[n[t.position]]:!0,[n.white]:t.playerIndex===0,[n.black]:t.playerIndex===1}));return(e,t)=>(J(),H(`div`,{class:q(i.value),style:uh({background:r.value})},null,6))}})})),yM,bM,xM=t((()=>{vM(),vM(),cy(),C(),yM={$style:sy},bM=S(_M,[[`__cssModules`,yM]])}));function SM(){let e=ia();return!!((e===T.Arena||e===T.TeamMatch||e===T.Tournament)&&fs())}var CM=t((()=>{Zo(),Kd(),Hm()}));function wM(){return SM()?fs()?.getTimeControl()??null:null}var TM=
```

<a id="FND-30106"></a>
## FND-30106 — Implementation component clock-bar

Vue compiled component __name declaration. Name suggests clock bar; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0201
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
2))}})})),mM,hM,gM=t((()=>{pM(),pM(),ty(),C(),mM={$style:ey},hM=S(fM,[[`__cssModules`,mM]])})),_M,vM=t((()=>{_s(),_M=K({__name:`clock-bar`,props:{playerIndex:{},position:{},remainder:{}},setup(e){let t=e,n=Q(),r=z(()=>jf(t.remainder)?`linear-gradient(
      to right,
      var(--remainder-color) 0%,
      var(--remainder-color) ${t.remainder}%,
      var(--expired-color) ${t.remainder}%
    )`:void 0),i=z(()=>({[n.bar]:!0,[n[t.position]]:!0,[n.white]:t.playerIndex===0,[n.black]:t.playerIndex===1}));return(e,t)=>(J(),H(`div`,{class:q(i.value),style:uh({background:r.value})},null,6))}})})),yM,bM,xM=t((()=>{vM(),vM(),cy(),C(),yM={$style:sy},bM=S(_M,[[`__cssModules`,yM]])}));function SM(){let e=ia();return!!((e===T.Arena||e===T.TeamMatch||e===T.Tournament)&&fs())}var CM=t((()=>{Zo(),Kd(),Hm()}));function wM(){return SM()?fs()?.getTimeControl()??null:null}var TM=t((()=>{Zo(),CM()}));function EM(){return as(`gameplay.live.low_time_warning`)}var DM=t((()=>{Uo()}));function OM(e,t){let n=kl(e);n?.isPlaying()&&n.playingAs===t&&Wc(n)&&!n.hasComponent(fl.LowTimeWarning)&&EM()&&(vn(yi.LowTime),Jm(e,[fl.LowTimeWarning]))}var kM=t((()=>{go(),Oe(),Ns(),cf(),Tp(),DM(),Vu()})),AM,jM=t((()=>{ls(),jo(),tc(),il(),he(),gM
```

<a id="FND-30107"></a>
## FND-30107 — Implementation component player-clock

Vue compiled component __name declaration. Name suggests player clock; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0201
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
t(),Ca(),iu(),Sl(),TM(),CM(),vf(),Ns(),kM(),la(),fm(),ce(),et(),Tp(),nm(),In(),_e(),xA(),pr(),ba(),hc(),$o(),Yt(),AM=K({__name:`player-clock`,props:{position:{},playerIndex:{}},setup(e){let t=Ad(),n=e,r=pu({position(){return n.position},playerIndex(){return n.playerIndex},isTheatreMode(){return t.value&&(ju()||bA())},gameModel(){return Eo()},gameView(){return kl(this.gameModel)},isClockRunning(){return Wc(this.gameView)&&t.value},isOnVacation(){return!!((this.gameModel?.isDailyGameModel()||this.gameModel?.isDailySeekModel())&&this.gameModel.isPlayerOnVacation(this.playerIndex)&&!this.gameModel.isOver())},clockTooltip(){return this.gameModel?.isDailyGameModel()?this.gameModel.getClockTooltip(this.playerIndex):``},timeControl(){if(this.gameModel)return this.gameModel.getTimeControl();let e=ps();if(e?.type===Dm.DailySeek){let t=ar(e.id);if(t)return t.getTimeControl()}return wM()??an()},isTextDisplay(){return this.timeControl.timeType!==`live`},initialClockTime(){return It(this.timeControl)},isGameStarting(){return!!(this.gameModel?.isRealtimeGame()&&this.gameModel.isStarting())},chessboardSelectedPly(){return vm()},selectedPly(){return this.isGameStarting?0:this.isClockRunning||this.gameView?.isOver()&&z
```

<a id="FND-30108"></a>
## FND-30108 — Implementation component player

Vue compiled component __name declaration. Name suggests player; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0201
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
n(),Iu(),Cn(),Bl(),Jr(),Dd(),pe(),Ei(),pr(),UM(),Zp(),vp(),Un(),Ve(),hc(),$o(),Sc(),Yt(),sc(),_u(),or(),Nm(),yn(),WM=K({__name:`player`,props:{position:{}},setup(e){let t=Ad(),n=e,r=pu({position(){return n.position},gameModel(){return Eo()},gameView(){return kl(this.gameModel)},boardId(){return Om()},isFocusMode(){return ju()},isTheatreMode(){return bA()},isBoardFlipped(){return Nl(this.gameView)},isEnglishLocale(){return Uf()===`en_US`},color(){return this.position===`top`?this.isBoardFlipped?1:2:this.isBoardFlipped?2:1},playerIndex(){if(!this.gameModel&&SM()||ps()?.type===Dm.CustomPosition)return this.position===`bottom`?0:1;switch(this.color){case 1:return 0;default:return 1}},player(){return this.gameModel?.isDailySeekModel()?this.gameModel.getPlayer(this.playerIndex):this.gameView?.getPlayer(this.playerIndex)??Pm(this.playerIndex)},pclPlayerInfo(){return this.gameModel?.isLiveGameModel()&&this.gameModel.pcl?HM(this.player.username):null},displayRating(){return Ic(this.gameModel)},rating(){if(!t.value)return null;let e=Ut(),n=e.name!==u.DailySeek&&zd.includes(e.name)&&!this.gameModel,r=this.gameView&&rf(this.gameView)&&!kp(),i=!this.gameModel&&af();if(!this.displayRating||n||r||i)return null;if(th
```

<a id="FND-30109"></a>
## FND-30109 — Implementation component sidebar

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
imeout-notification.title.user-avatar.username`.split(`.`)))}})})),KM,qM=t((()=>{GM(),GM(),KM=WM})),JM,YM=t((()=>{JM=K({__name:`sidebar`,props:{content:{}},setup(e){let t=e,n=Q(),r=mh({});return bh(()=>t.content,(e,t)=>{e.transition||!t?.tab?r.value={enterActiveClass:n.fadeActive,leaveActiveClass:n.fadeActive,enterFromClass:n.fadeHiding,enterToClass:n.fadeShowing,leaveFromClass:n.fadeShowing,leaveToClass:n.fadeHiding,mode:`out-in`}:r.value={mode:`out-in`}},{immediate:!0}),(t,i)=>(J(),H(`div`,{class:q(Z(n).component)},[Y(t.$slots,`tabs`),i[0]||=W(),G(th,lh(ah(r.value)),{default:$(()=>[(J(),H(`div`,{key:e.content.key,class:q(Z(n).content)},[(J(),B(gh(e.content.component)))],2))]),_:1},16)],2))}})})),XM,ZM,QM=t((()=>{YM(),YM(),IS(),C(),XM={$style:FS},ZM=S(JM,[[`__cssModules`,XM]])}));function $M(e,t){return J(),H(`div`,{class:q(e.$style[`cc-skeleton-component`])},null,2)}var eN,tN,nN,rN=t((()=>{rt(),eN={"cc-skeleton-component":`cc-skeleton-component_360436c`,"cc-skeleton-shimmer":`cc-skeleton-shimmer_360436c`},tN={},nN=bt(tN,[[`render`,$M],[`__cssModules`,{$style:eN}]])})),iN=t((()=>{wh(),rN()})),aN,oN=t((()=>{iN(),um(),aN=K({inheritAttrs:!1,__name:`cc-skeleton`,setup(e){let t=_a({optional:!0})?.features
```

<a id="FND-30110"></a>
## FND-30110 — Implementation component cc-skeleton

Vue compiled component __name declaration. Name suggests cc skeleton; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0201
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
,[[`render`,$M],[`__cssModules`,{$style:eN}]])})),iN=t((()=>{wh(),rN()})),aN,oN=t((()=>{iN(),um(),aN=K({inheritAttrs:!1,__name:`cc-skeleton`,setup(e){let t=_a({optional:!0})?.features.includes(`design_system_component_migration_cc_skeleton`)??!1;return(e,n)=>Z(t)?(J(),B(Z(nN),lh(sh({key:0},e.$attrs)),null,16)):(J(),H(`div`,sh({key:1},e.$attrs,{class:e.$style.skeleton}),null,16))}})})),sN,cN,lN=t((()=>{oN(),oN(),l_(),C(),sN={$style:c_},cN=S(aN,[[`__cssModules`,sN]])})),uN,dN=t((()=>{lN(),uN=K({__name:`cc-skeleton-grid`,props:{rows:{default:1},columns:{default:1},items:{},rowHeight:{default:`1.4rem`},rowGap:{default:`0`},columnWidth:{default:`1fr`},columnGap:{default:`0`}},setup(e){vh(e=>({v4d30a8e6:e.rowGap,v0075b50f:e.columnGap,v0e547957:Z(n),v53a15299:Z(r)}));let t=e,n=Array(t.columns).fill(t.columnWidth).join(` `),r=Array(t.rows).fill(t.rowHeight).join(` `);return(t,n)=>(J(),H(`div`,{class:q(t.$style.wrapper)},[e.items&&e.items.length>0?(J(!0),H(Qm,{key:0},hh(e.items,(e,n)=>(J(),B(cN,{key:n,style:uh(`grid-area: ${e}`),class:q(t.$style.item)},null,8,[`style`,`class`]))),128)):(J(!0),H(Qm,{key:1},hh(e.rows*e.columns,e=>(J(),B(cN,{key:e,class:q(t.$style.item)},null,8,[`class`]))),128))],2))}})})),fN,pN
```

<a id="FND-30111"></a>
## FND-30111 — Implementation component cc-skeleton-grid

Vue compiled component __name declaration. Name suggests cc skeleton grid; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0201
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
6))}})})),sN,cN,lN=t((()=>{oN(),oN(),l_(),C(),sN={$style:c_},cN=S(aN,[[`__cssModules`,sN]])})),uN,dN=t((()=>{lN(),uN=K({__name:`cc-skeleton-grid`,props:{rows:{default:1},columns:{default:1},items:{},rowHeight:{default:`1.4rem`},rowGap:{default:`0`},columnWidth:{default:`1fr`},columnGap:{default:`0`}},setup(e){vh(e=>({v4d30a8e6:e.rowGap,v0075b50f:e.columnGap,v0e547957:Z(n),v53a15299:Z(r)}));let t=e,n=Array(t.columns).fill(t.columnWidth).join(` `),r=Array(t.rows).fill(t.rowHeight).join(` `);return(t,n)=>(J(),H(`div`,{class:q(t.$style.wrapper)},[e.items&&e.items.length>0?(J(!0),H(Qm,{key:0},hh(e.items,(e,n)=>(J(),B(cN,{key:n,style:uh(`grid-area: ${e}`),class:q(t.$style.item)},null,8,[`style`,`class`]))),128)):(J(!0),H(Qm,{key:1},hh(e.rows*e.columns,e=>(J(),B(cN,{key:e,class:q(t.$style.item)},null,8,[`class`]))),128))],2))}})})),fN,pN,mN=t((()=>{dN(),dN(),a_(),C(),fN={$style:i_},pN=S(uN,[[`__cssModules`,fN]])})),hN,gN=t((()=>{mN(),hN=K({__name:`sidebar-skeleton`,setup(e){let t=[`1 / 1 / 2 / 2`,`1 / 2 / 2 / 3`,`1 / 3 / 2 / 4`,`1 / 4 / 2 / 5`,`1 / 5 / 2 / 6`,`2 / 1 / 3 / 5`,`2 / 5 / 3 / 6`,`3 / 1 / 4 / 6`,`4 / 1 / 5 / 6`,`5 / 1 / 6 / 6`,`6 / 1 / 7 / 6`,`7 / 1 / 8 / 6`,`8 / 1 / 9 / 6`];return(e,n)=>(J(),B(pN
```

<a id="FND-30112"></a>
## FND-30112 — Implementation component sidebar-skeleton

Vue compiled component __name declaration. Name suggests sidebar skeleton; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0201
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
2))}})})),fN,pN,mN=t((()=>{dN(),dN(),a_(),C(),fN={$style:i_},pN=S(uN,[[`__cssModules`,fN]])})),hN,gN=t((()=>{mN(),hN=K({__name:`sidebar-skeleton`,setup(e){let t=[`1 / 1 / 2 / 2`,`1 / 2 / 2 / 3`,`1 / 3 / 2 / 4`,`1 / 4 / 2 / 5`,`1 / 5 / 2 / 6`,`2 / 1 / 3 / 5`,`2 / 5 / 3 / 6`,`3 / 1 / 4 / 6`,`4 / 1 / 5 / 6`,`5 / 1 / 6 / 6`,`6 / 1 / 7 / 6`,`7 / 1 / 8 / 6`,`8 / 1 / 9 / 6`];return(e,n)=>(J(),B(pN,{rows:8,columns:5,items:t,"row-height":`4rem`,"row-gap":`.8rem`,"column-gap":`.8rem`,class:q(e.$style.component)},null,8,[`class`]))}})})),_N,vN,yN=t((()=>{gN(),gN(),$x(),C(),_N={$style:Qx},vN=S(hN,[[`__cssModules`,_N]])})),bN,xN=t((()=>{bp(),Zn(),nn(),sa(),Xo(),Go(),jo(),Jl(),j(),bN=K({__name:`time-selector-next`,props:{dropdownClass:{default:``},gameTypeOptions:{},hasLoadedTimeControl:{type:Boolean,default:!0},isFocusMode:{type:Boolean,default:!1},isGuest:{type:Boolean,default:!1},isLoggedIn:{type:Boolean,default:!0},isOpen:{type:Boolean,default:!1},isRated:{type:Boolean},isRecentTimeControlsPinned:{type:Boolean,default:!1},recentTimeControls:{default:()=>[]},selectedGameType:{},selectedTime:{}},emits:[`click-recent-time-controls-pin`,`click-time`,`select-game-type`,`select-time`,`set-rated`],setup(e,{emit:t}){le
```

<a id="FND-30113"></a>
## FND-30113 — Implementation component time-selector-next

Vue compiled component __name declaration. Name suggests time selector next; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0201
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
(),C(),_N={$style:Qx},vN=S(hN,[[`__cssModules`,_N]])})),bN,xN=t((()=>{bp(),Zn(),nn(),sa(),Xo(),Go(),jo(),Jl(),j(),bN=K({__name:`time-selector-next`,props:{dropdownClass:{default:``},gameTypeOptions:{},hasLoadedTimeControl:{type:Boolean,default:!0},isFocusMode:{type:Boolean,default:!1},isGuest:{type:Boolean,default:!1},isLoggedIn:{type:Boolean,default:!0},isOpen:{type:Boolean,default:!1},isRated:{type:Boolean},isRecentTimeControlsPinned:{type:Boolean,default:!1},recentTimeControls:{default:()=>[]},selectedGameType:{},selectedTime:{}},emits:[`click-recent-time-controls-pin`,`click-time`,`select-game-type`,`select-time`,`set-rated`],setup(e,{emit:t}){let n=e,r=t;function i(e){a.value=!1,r(`select-game-type`,e)}let a=mh(!1),o=k(`(Unrated)`);function s(){a.value=!a.value}let c=z(()=>!n.hasLoadedTimeControl),ee=z(()=>{if(!n.hasLoadedTimeControl)return``;let e=Ka(n.selectedTime);if(!n.isRated)return`${e} ${o}`;if(ne.value){let t=xd(n.selectedTime);e+=` (${t})`}return e}),te=z(()=>n.hasLoadedTimeControl?qn(`chess`,n.selectedTime):void 0),ne=z(()=>n.selectedGameType===`chess`);return(t,n)=>(J(),H(`div`,{class:q(t.$style.component)},[G(ds,{"full-width":``,size:`x-large`,"custom-classes":{icon:`glyph-colored`},d
```

<a id="FND-30114"></a>
## FND-30114 — Implementation component new-game

Vue compiled component __name declaration. Name suggests new game; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0201
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
((()=>{xN(),xN(),e_(),C(),SN={$style:$g},CN=S(bN,[[`__cssModules`,SN]])})),TN,EN=t((()=>{wN(),jm(),Tr(),Hr(),Iu(),TN=K({__name:`new-game`,props:{gameTypeOptions:{},hasLoadedTimeControl:{type:Boolean},isGuest:{type:Boolean},isLoggedIn:{type:Boolean},isRated:{type:Boolean},isRecentTimeControlsPinned:{type:Boolean},isTimeSelectorOpen:{type:Boolean},minutesUntilShutdown:{},recentTimeControls:{},requireShutdownConfirmation:{type:Boolean},requireTournamentConfirmation:{type:Boolean},selectedGameType:{},selectedTime:{},view:{}},emits:[`click-play`,`click-recent-time-controls-pin`,`custom-game-clicked`,`select-game-type`,`select-time`,`show-tournaments`,`show-view`,`set-rated`,`toggle-time-selector`],setup(e,{emit:t}){let n=Fn(),r=t;function i(e){r(`select-game-type`,e)}function a(e){r(`select-time`,e)}function o(){r(`click-recent-time-controls-pin`)}function s(){r(`click-play`)}function c(){r(`show-view`,{view:v.PlayFriend})}return(t,r)=>(J(),H(Qm,null,[U(`div`,{class:q(t.$style.component)},[U(`div`,{class:q(t.$style.primary)},[G(CN,{"game-type-options":e.gameTypeOptions,"has-loaded-time-control":e.hasLoadedTimeControl,"is-guest":e.isGuest,"is-logged-in":e.isLoggedIn,"is-open":e.isTimeSelectorOpen,"is-rated"
```

<a id="FND-30115"></a>
## FND-30115 — Implementation component new-game

Vue compiled component __name declaration. Name suggests new game; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0201
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
,Am(),Bs(),Iu(),Or(),Fl(),ai(),Bl(),ws(),Td(),Dd(),pr(),ba(),Zi(),Xc(),ld(),Ed(),fd(),Ma(),E(),op(),UN(),GN(),_(),KN=K({__name:`new-game`,setup(t){let n=Ad(),r=mh(!1);WN(()=>{if(O()){mt()||Po();let t=Lp({triggers:[()=>IN()],shouldLoad:RN,loader:()=>h(()=>e(()=>import(`./load-featured-tv-shows.3e8b4f68.g5c5IkX5G5.chunk.js`),`./load-featured-tv-shows.3e8b4f68.g5c5IkX5G5.chunk.js`).then(e=>(e.t(),e.n)),__vite__mapDeps([0]),import.meta.url)})();t.mount(),dh(()=>{t.unmount()})}});let i=pu({gameTypeOptions(){return eu()},isGuest(){return mt()},hasLoadedTimeControl(){return hm()},isFeaturedTvShowsVisible(){return n.value&&BN()},isLoggedIn(){return O()},isRated(){return c()},minutesUntilShutdown(){return Wu()},newGameView(){return au()},recentTimeControls(){return pf()},recentTimeControlsPinned(){return n.value&&_l()},selectedGameType(){return mf()},selectedTime(){return an()},requireTournamentConfirmation(){let e=ys();return!!(e&&(Pa(e)||Ec(e)))},requireShutdownConfirmation(){return Ap()},isIncomingChallengesVisible(){return!!(n.value&&Vr().length)},isAnnouncementVisible(){return n.value&&!!nt()}});function a(){xp(Qo()),Lc({challenge:Ln(),interfaceName:`New Game Sidebar`,elementName:`Game Seek Button`})}func
```

<a id="FND-30116"></a>
## FND-30116 — Implementation component outgoing-challenge-row

Vue compiled component __name declaration. Name suggests outgoing challenge row; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0201
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
)=>{Za(),bo(),Tf()})),QN,$N,eP,tP=t((()=>{Ru(),Up(),Vs(),ls(),Go(),j(),Me(),QN=[`textContent`],$N=[`textContent`],eP=K({__name:`outgoing-challenge-row`,props:{challenge:{},contextUser:{},currentUser:{}},emits:[`cancel-challenge`],setup(e,{emit:t}){let n=e,r=t,i=z(()=>n.contextUser?.isSameUser(n.challenge.getFrom())||n.currentUser.isSameUser(n.challenge.getFrom())),a=z(()=>n.challenge.getTo()?k(`Waiting for Opponent`):k(`Starting soon`));function o(){r(`cancel-challenge`,{challenge:n.challenge})}return(t,n)=>(J(),H(`div`,{class:q(t.$style.component)},[e.challenge.getTo()?(J(),B(zs,{key:0,class:q(t.$style.avatar),src:e.challenge.getTo()?.getAvatar()||null,username:e.challenge.getTo()?.getUsername()},null,8,[`class`,`src`,`username`])):(J(),B(Il,{key:1,class:`glyph-colored`,variant:`glyph`,is:Z(qn)(e.challenge.getGameType(),e.challenge.getTimeControl()),size:40},null,8,[`is`])),n[3]||=W(),U(`div`,{class:q(t.$style.column)},[U(`div`,null,[U(`span`,{class:q(t.$style.time),textContent:X(e.challenge.getTimeLabel())},null,10,QN),n[0]||=W(),e.challenge.isRatedChallenge()?V(``,!0):(J(),H(`span`,{key:0,class:q(t.$style.unrated),textContent:X(t.$trans(`(Unrated)`))},null,10,$N))]),n[1]||=W(),G(Zm,{class:q(t.$styl
```

<a id="FND-30117"></a>
## FND-30117 — Implementation component outgoing-challenges

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
)})),aP,oP,sP,cP=t((()=>{Ru(),Vs(),Ar(),iP(),Me(),aP=[`textContent`],oP=[`textContent`],sP=K({name:`OutgoingChallenges`,__name:`outgoing-challenges`,props:{challenges:{},contextUser:{default:null},currentUser:{},presenceData:{},showSpeechMessage:{type:Boolean,default:!1}},emits:[`cancel-challenge`,`cancel-all-challenges`,`close-outgoing-challenges`],setup(e){let t=e,n=Q(),r=z(()=>t.challenges.length>1),i=z(()=>t.showSpeechMessage&&!r.value),a=z(()=>r.value?n.list:n.content),o=z(()=>r.value?rP:da);function s(e){let n=e.getTo()?.getUserUuid();return n?t.presenceData[n]??null:null}return(t,c)=>(J(),H(`div`,{class:q(Z(n).component)},[U(`div`,{class:q(Z(n).header)},[G(Zm,{text:t.$trans(`Searching`),class:q(Z(n).label)},null,8,[`text`,`class`]),c[4]||=W(),U(`button`,{class:q(Z(n).close),onClick:c[0]||=e=>t.$emit(`close-outgoing-challenges`)},[G(Il,{is:Z(Xf),variant:`glyph`,class:q(Z(n).icon),size:16},null,8,[`is`,`class`]),c[3]||=W(),U(`span`,{class:q(Z(n).text),textContent:X(t.$trans(`New Game`))},null,10,aP)],2)],2),c[7]||=W(),U(`div`,{class:q(a.value)},[i.value?(J(),H(`div`,{key:0,class:q(Z(n).speech)},[Y(t.$slots,`speech`)],2)):V(``,!0),c[5]||=W(),r.value?(J(),H(`button`,{key:1,class:q(Z(n).cancel),text
```

<a id="FND-30118"></a>
## FND-30118 — Implementation component seek-panel-indicator

Vue compiled component __name declaration. Name suggests seek panel indicator; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0201
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
,[[`__cssModules`,lP]])})),fP,pP,mP,hP=t((()=>{Up(),jm(),Vs(),Fe(),dm(),j(),fP=[`textContent`],pP=[`textContent`],mP=K({__name:`seek-panel-indicator`,props:{avatarSrc:{},avatarUsername:{},headline:{},iconName:{},isCancelHidden:{type:Boolean},isUnrated:{type:Boolean},presenceData:{},showAvatar:{type:Boolean},showSearchDots:{type:Boolean},timeLabel:{}},emits:[`cancel`],setup(e){let t=e,n=Q(),r=k(`(Unrated)`),i=z(()=>({[n.cancel]:!0,[n.hidden]:t.isCancelHidden})),a=z(()=>t.presenceData?{isPlaying:t.presenceData.activity===va.Playing,isOnline:t.presenceData.status===uc.Online}:null);return(t,o)=>(J(),H(`div`,{class:q(Z(n).seek)},[e.showAvatar?(J(),B(zs,{key:0,class:q(Z(n).avatar),size:48,src:e.avatarSrc,status:a.value||void 0,username:e.avatarUsername},null,8,[`class`,`src`,`status`,`username`])):(J(),B(Il,{key:1,class:q(Z(n).icon),variant:`color`,name:e.iconName,size:48},null,8,[`class`,`name`])),o[3]||=W(),U(`div`,{class:q(Z(n).text)},[U(`p`,{class:q([`cc-heading-small-bold`,Z(n).headline])},[W(X(e.headline)+` `,1),e.showSearchDots?(J(),H(`span`,{key:0,class:q(Z(n).dots),"aria-hidden":`true`},null,2)):V(``,!0)],2),o[2]||=W(),U(`p`,{class:q([`cc-heading-xx-small`,Z(n).timeControl])},[U(`span`,{textConten
```

<a id="FND-30119"></a>
## FND-30119 — Implementation component seek-panel

Vue compiled component __name declaration. Name suggests seek panel; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0201
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
=>{hP(),hP(),Tb(),C(),gP={$style:wb},_P=S(mP,[[`__cssModules`,gP]])})),yP,bP,xP=t((()=>{jm(),ur(),j(),vP(),yP=5e3,bP=K({__name:`seek-panel`,props:{canCancelPendingChallenge:{type:Boolean},challenge:{},coachTip:{},initialCoachMessage:{},presenceData:{}},emits:[`cancel-challenge`,`close-outgoing-challenges`],setup(e,{emit:t}){let n=e,r=t,i=!n.challenge.getTo(),a=mh(0),o;function s(){a.value++,a.value<3&&(o=window.setTimeout(s,yP))}fh(()=>{i&&(o=window.setTimeout(s,yP))}),dh(()=>{o!==void 0&&clearTimeout(o)});let c=z(()=>i?a.value>=1?k(`Still searching`):k(`Searching`):k(`Waiting for Opponent`)),ee=z(()=>!i||a.value<2?n.initialCoachMessage??n.coachTip:n.challenge.isDailyActiveSeekModel()?k(`You can leave this view. The game will start automatically.`):a.value===2?k(`Taking longer than expected to find a match...`):k(`For quicker pairings, try expanding or disabling your "Rating Range", or trying a more common time control.`)),te=z(()=>{let e=en(n.challenge.getTimeControl(),n.challenge.getGameType());return e===`live960`||e===`chess960`?e:`time-${e}`}),ne=z(()=>n.challenge.getTo()),l=z(()=>ne.value?.getAvatar()||null),re=z(()=>ne.value?.getUsername()),ie=z(()=>n.challenge.isPlaceholderChallengeModel()&&!n
```
