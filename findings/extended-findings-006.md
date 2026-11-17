# Extended findings

[Master index](../chapters/00_MASTER_INDEX.md)

<a id="FND-30300"></a>
## FND-30300 — Implementation component coach-settings-content

Vue compiled component __name declaration. Name suggests coach settings content; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
=>{xUt(),xUt(),bde(),He(),SUt={$style:yde},CUt=Ve(bUt,[[`__cssModules`,SUt]])})),TUt,EUt=r((()=>{NK(),wUt(),oK(),TUt=y({__name:`coach-settings-content`,props:{audioToggle:{}},emits:[`close`,`onChooseCoachClick`,`toggleAudio`],setup(e,{emit:t}){let n=t,r=me(!1),i=ke(`scrollContainer`),{y:a}=Oit(i),o=l(()=>a.value>0);function s(){r.value=!0,n(`onChooseCoachClick`)}return(t,n)=>(O(),p(`div`,null,[g(CUt,{"audio-toggle":e.audioToggle,onClose:n[0]||=e=>t.$emit(`close`),onToggleAudio:n[1]||=e=>t.$emit(`toggleAudio`)},{default:Me(()=>[h(Se(t.$trans(`Choose Your Coach`)),1)]),_:1},8,[`audio-toggle`]),n[2]||=h(),_e(t.$slots,`coach-speech-tagline`),n[3]||=h(),m(`div`,{class:D([t.$style.wrapper,{[t.$style[`with-shadow`]]:o.value}])},[m(`div`,{class:D(t.$style.body),ref_key:`scrollContainer`,ref:i},[_e(t.$slots,`coach-selection-menu`)],2)],2),n[4]||=h(),m(`div`,{class:D(t.$style[`cta-button-container`])},[g(aK,{class:D(t.$style[`cta-button`]),"full-width":``,size:`xx-large`,variant:`primary`,loading:r.value,label:t.$trans(`Choose Coach`),onClick:s},null,8,[`class`,`loading`,`label`])],2)]))}})})),DUt,OUt,kUt=r((()=>{EUt(),EUt(),mde(),He(),DUt={$style:pde},OUt=Ve(TUt,[[`__cssModules`,DUt]])})),AUt,jUt=r((()=>{NK(),
```

<a id="FND-30301"></a>
## FND-30301 — Implementation component cc-modal

Vue compiled component __name declaration. Name suggests cc modal; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
t,kUt=r((()=>{EUt(),EUt(),mde(),He(),DUt={$style:pde},OUt=Ve(TUt,[[`__cssModules`,DUt]])})),AUt,jUt=r((()=>{NK(),AUt=y({__name:`cc-modal`,props:{dismissable:{type:Boolean,default:!0},noCloseOnEscape:{type:Boolean,default:!1},modalWidth:{},isTransparent:{type:Boolean,default:!1},customClasses:{default:()=>({})},propagateKeys:{type:Boolean,default:!1}},emits:[`hide`],setup(e,{emit:t}){let n=e,r=()=>n.dismissable&&!n.noCloseOnEscape,i=t,a=ke(`dialogRef`),o=ke(`panelRef`);se(()=>{a.value&&(a.value.showModal(),a.value.addEventListener(`cancel`,e=>{e.preventDefault()})),SK(window,`keydown`,e=>{e.key===`Escape`&&r()&&i(`hide`)})});function s(e){if(!n.dismissable)return;let t=o.value;t&&e.composedPath().includes(t)||i(`hide`)}function c(e){if(e.key===`Escape`){e.preventDefault(),e.stopPropagation(),e.type===`keydown`&&r()&&i(`hide`);return}n.propagateKeys||e.stopPropagation()}return(t,n)=>(O(),p(`dialog`,{ref_key:`dialogRef`,ref:a,class:D([t.$style.component,e.modalWidth&&t.$style[e.modalWidth],e.customClasses?.backdrop,{[t.$style[`bg-transparent`]]:e.isTransparent}]),onClick:s,onKeydown:c,onKeyup:c,onKeypress:c},[m(`div`,{ref_key:`panelRef`,ref:o,"data-ignore-close-board-modal":``,class:D([t.$style.dialog,e.
```

<a id="FND-30302"></a>
## FND-30302 — Implementation component coach-settings-modal

Vue compiled component __name declaration. Name suggests coach settings modal; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
=r((()=>{jUt(),jUt(),Wue(),He(),MUt={$style:Fc},R7=Ve(AUt,[[`__cssModules`,MUt]])})),PUt,FUt=r((()=>{kUt(),NUt(),PUt=y({__name:`coach-settings-modal`,props:{audioToggle:{},selectedCoachId:{}},emits:[`close`,`onChooseCoachClick`,`toggleAudio`],setup(e,{emit:t}){let n=t;return(t,r)=>(O(),d(R7,{"modal-width":`sm`,onHide:r[3]||=e=>n(`close`)},{default:Me(()=>[g(OUt,{"audio-toggle":e.audioToggle,onClose:r[0]||=e=>t.$emit(`close`),onOnChooseCoachClick:r[1]||=e=>t.$emit(`onChooseCoachClick`),onToggleAudio:r[2]||=e=>t.$emit(`toggleAudio`)},{"coach-speech-tagline":Me(()=>[_e(t.$slots,`coach-speech-tagline`)]),"coach-selection-menu":Me(()=>[_e(t.$slots,`coach-selection-menu`)]),_:3},8,[`audio-toggle`])]),_:3}))}})})),IUt,LUt,RUt=r((()=>{FUt(),FUt(),Ede(),He(),IUt={$style:Tde},LUt=Ve(PUt,[[`__cssModules`,IUt]])}));function zUt(e={}){P7.emit(Du.CoachModalClose,{saved:e.saved===!0})}var BUt=r((()=>{Ou(),F7()})),z7,VUt=r((()=>{z(),cq(),af(),Lm(),z7=Gg({name:`coachesService.coachesCategory`,global:!0,persist:`isolated`,async loader(){let t=await Im(()=>e(()=>import(`./coaches.dd1c6bed.BTqZvQUuOU.chunk.js`),`./coaches.dd1c6bed.BTqZvQUuOU.chunk.js`).then(e=>(e.n(),e.t)),[],import.meta.url),{bucketingId:n}=sq();return(
```

<a id="FND-30303"></a>
## FND-30303 — Implementation component coach-selection-button

Vue compiled component __name declaration. Name suggests coach selection button; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
e(),UUt(),RWt(),t9(),BWt(),HWt(),Lm()})),GWt,KWt,qWt,JWt=r((()=>{_E(),cK(),GWt=[`alt`,`src`],KWt=[`textContent`],qWt=y({__name:`coach-selection-button`,props:{coach:{default:null},largeAvatars:{type:Boolean,default:!1},selected:{type:Boolean,default:!1},disabled:{type:Boolean,default:!1}},emits:[`click`],setup(e,{emit:t}){let n=e,r=t;function i(){n.disabled||r(`click`)}return(t,n)=>(O(),p(`div`,{class:D(t.$style.component)},[m(`button`,{type:`button`,class:D([t.$style.button,{[t.$style.large]:e.largeAvatars},{"cc-selected-border":e.selected},{[t.$style.none]:!e.coach}]),onClick:i},[e.coach?(O(),p(`img`,{key:0,height:`85`,width:`85`,alt:t.$trans(`coach`),class:D(t.$style.img),src:e.coach.imageUrl},null,10,GWt)):(O(),p(`div`,{key:1,class:D([t.$style.iconContainer,{[t.$style.iconContainerUnselected]:!e.selected}])},[g(sK,{is:k(fC),variant:`glyph`,size:40,class:D(t.$style.iconX)},null,8,[`is`,`class`])],2)),n[0]||=h(),e.coach?.i18nMeta?.languageIndicator?(O(),p(`div`,{key:2,class:D([t.$style.languageIndicator,`cc-text-x-small-bold`])},Se(e.coach.i18nMeta.languageIndicator),3)):f(``,!0)],2),n[1]||=h(),m(`div`,{class:D([t.$style.label,{[t.$style.labelSelected]:e.selected}]),textContent:Se(e.coach?.name??t.$
```

<a id="FND-30304"></a>
## FND-30304 — Implementation component coach-flat-selection-menu

Vue compiled component __name declaration. Name suggests coach flat selection menu; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
,ZWt=r((()=>{JWt(),JWt(),cde(),He(),YWt={$style:sde},XWt=Ve(qWt,[[`__cssModules`,YWt]])})),QWt,$Wt=r((()=>{ZWt(),QWt=y({__name:`coach-flat-selection-menu`,props:{coachesList:{},isLoading:{type:Boolean},selectedCoachId:{}},emits:[`set-coach`],setup(e){let t=e,n=me(null),r=e=>l(()=>!t.isLoading&&t.selectedCoachId===e);return se(async()=>{await ne(),n.value&&Array.isArray(n.value)&&n.value[0].$el?.scrollIntoView({behavior:`smooth`,block:`center`,inline:`center`})}),(t,n)=>(O(),p(`div`,{class:D(t.$style.coaches)},[(O(!0),p(s,null,ge(e.coachesList,n=>(O(),d(XWt,{disabled:e.isLoading,key:n.id,ref_for:!0,ref:e.selectedCoachId===n.id?`selectedCoachEl`:void 0,selected:r(n.id).value,coach:n,onClick:e=>t.$emit(`set-coach`,{coachId:n.id})},null,8,[`disabled`,`selected`,`coach`,`onClick`]))),128))],2))}})})),eGt,tGt,nGt=r((()=>{$Wt(),$Wt(),rde(),He(),eGt={$style:_u},tGt=Ve(QWt,[[`__cssModules`,eGt]])}));function rGt(){return H7().state.status===Sd.Loading}var iGt=r((()=>{z(),U7()})),aGt,oGt=r((()=>{Z7(),nGt(),G7(),iGt(),aGt=y({__name:`coach-flat-selection-menu`,props:{coachesList:{}},emits:[`change`],setup(e,{emit:t}){let n=t,r=l(()=>rGt()),i=l(()=>W7({preferPendingCoach:!0})?.id||null),a=async({coachId:e})=>{X7(e
```

<a id="FND-30305"></a>
## FND-30305 — Implementation component coach-flat-selection-menu

Vue compiled component __name declaration. Name suggests coach flat selection menu; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
on rGt(){return H7().state.status===Sd.Loading}var iGt=r((()=>{z(),U7()})),aGt,oGt=r((()=>{Z7(),nGt(),G7(),iGt(),aGt=y({__name:`coach-flat-selection-menu`,props:{coachesList:{}},emits:[`change`],setup(e,{emit:t}){let n=t,r=l(()=>rGt()),i=l(()=>W7({preferPendingCoach:!0})?.id||null),a=async({coachId:e})=>{X7(e)};return(t,o)=>(O(),d(tGt,{"coaches-list":e.coachesList,"is-loading":r.value,"selected-coach-id":i.value,onSetCoach:o[0]||=e=>n(`change`,a(e))},null,8,[`coaches-list`,`is-loading`,`selected-coach-id`]))}})})),sGt,cGt=r((()=>{oGt(),oGt(),sGt=aGt}));function lGt(e,t){return O(),p(`div`,{class:D(e.$style[`speech-message`])},[_e(e.$slots,`coach-speech`)],2)}var uGt,dGt,fGt,pGt=r((()=>{kde(),He(),uGt={},dGt={$style:Ode},fGt=Ve(uGt,[[`render`,lGt],[`__cssModules`,dGt]])})),n9,mGt=r((()=>{n9=Symbol(`animatedCoach`)})),r9,hGt=r((()=>{NK(),r9=()=>{let e=Dit(Symbol(`rive-controls`));return oe(()=>{e.reset()}),{controls:e,binding:{setColor:(t,n)=>{e.emit(`binding`,[`color`,t,n])},setRgb:(t,n,r,i)=>{e.emit(`binding`,[`rgb`,t,n,r,i])},setRgba:(t,n,r,i,a)=>{e.emit(`binding`,[`rgba`,t,n,r,i,a])},setOpacity:(t,n)=>{e.emit(`binding`,[`opacity`,t,n])},setBoolean:(t,n)=>{e.emit(`binding`,[`boolean`,t,n])},setString
```

<a id="FND-30306"></a>
## FND-30306 — Implementation component raw-rive-file

Vue compiled component __name declaration. Name suggests raw rive file; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
ait t.arrayBuffer())}var o9,TGt=r((()=>{o9=g7()})),s9,EGt,DGt,OGt=r((()=>{a9(),s9=i9(),EGt=g7(),TGt(),nme(),Um(),DGt=y({__name:`raw-rive-file`,props:{src:{}},emits:[`load`,`error`],setup(e,{emit:t}){typeof window<`u`&&!window.Buffer&&(window.Buffer=EGt.Buffer);let n=e,r=t,i=xe(),a=e=>{let t;t=e instanceof Error?e:e.type===s9.EventType.LoadError?Error(e.data?.toString()??`RiveFile load error`):Error(`RiveFile load error`),window.chesscom.features.includes(`web_rive_error_reporting`)&&Hm(t,{extra:{component:`raw-rive-file`,srcType:typeof n.src,srcLength:typeof n.src==`string`?n.src.length??-1:-1}}),r(`error`,t)},o=()=>{},s=me(o),c=Symbol(`non-string-src`),l=()=>{let{src:e}=n;return e?typeof e==`string`?e:c:null},u=async(e,t)=>{try{let n=await wGt(e);if(l()!==t)return;let c=new s9.RiveFile({buffer:tme(n)??void 0,onLoad:e=>{e.type!==s9.EventType.Load||!(e.data instanceof s9.RiveFile)||l()===t&&(i.value=e.data,r(`load`,e.data))},onLoadError:a});s.value=()=>{c.cleanup(),i.value=void 0},c.cleanup=o,await c.init()}catch(e){let t=e instanceof Error?e:Error(`raw-rive-file: load: Unknown error`);a(t)}},d=()=>{s.value(),s.value=o,i.value=void 0};return se(()=>{let{src:e}=n;e&&u(e,l())}),Ae(l,e=>{let{src:t}=n;t?u(
```

<a id="FND-30307"></a>
## FND-30307 — Implementation component unsafe-rive-file

Vue compiled component __name declaration. Name suggests unsafe rive file; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
,c9=DGt})),l9,u9,d9=r((()=>{l9=Symbol(`rive-file`),u9=Symbol(`rive-file-expected`)})),AGt,jGt=r((()=>{kGt(),d9(),AGt=y({__name:`unsafe-rive-file`,props:{src:{}},emits:[`load`,`error`],setup(e,{emit:t}){let n=e,r=t,i=xe();de(l9,i),de(u9,l(()=>!!n.src)),Ae(()=>n.src,e=>{e||(i.value=void 0)});let a=e=>{i.value=e,r(`load`,e)},o=e=>{r(`error`,e)};return(t,n)=>(O(),d(c9,{src:e.src,onLoad:a,onError:o},{default:Me(()=>[_e(t.$slots,`default`)]),_:3},8,[`src`]))}})})),f9,MGt=r((()=>{jGt(),jGt(),f9=AGt})),NGt,PGt=r((()=>{pGt(),vGt(),oqt(),bGt(),SGt(),G7(),MGt(),NGt=y({__name:`coach-speech-tagline`,props:{allowAnimationOverflowLeft:{type:Boolean},startTypewriterAfterMount:{type:Boolean}},setup(e){let t=l(()=>{let e=W7({preferPendingCoach:!0});return e?.greetingRiveAnimationUrl||e?.riveAnimationUrl}),n=l(()=>xGt()||(W7({preferPendingCoach:!1})?.taglines?.[0]?.text??``)),{triggerCoachEmotion:r}=gGt({event:{interface:`choose_your_coach`,preferPendingCoach:!0}});return Ae(t,()=>r(`greeting`),{immediate:!0,flush:`post`}),(r,i)=>(O(),d(f9,{key:k(yGt)()??t.value,src:t.value},{default:Me(()=>[g(fGt,null,{"coach-speech":Me(()=>[k(W7)()?(O(),d(x9,{key:0,"animation-key":n.value,"bot-align":`bottom`,"coach-size":96,"is-coach
```

<a id="FND-30308"></a>
## FND-30308 — Implementation component coach-speech-tagline

Vue compiled component __name declaration. Name suggests coach speech tagline; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
,8,[`src`]))}})})),f9,MGt=r((()=>{jGt(),jGt(),f9=AGt})),NGt,PGt=r((()=>{pGt(),vGt(),oqt(),bGt(),SGt(),G7(),MGt(),NGt=y({__name:`coach-speech-tagline`,props:{allowAnimationOverflowLeft:{type:Boolean},startTypewriterAfterMount:{type:Boolean}},setup(e){let t=l(()=>{let e=W7({preferPendingCoach:!0});return e?.greetingRiveAnimationUrl||e?.riveAnimationUrl}),n=l(()=>xGt()||(W7({preferPendingCoach:!1})?.taglines?.[0]?.text??``)),{triggerCoachEmotion:r}=gGt({event:{interface:`choose_your_coach`,preferPendingCoach:!0}});return Ae(t,()=>r(`greeting`),{immediate:!0,flush:`post`}),(r,i)=>(O(),d(f9,{key:k(yGt)()??t.value,src:t.value},{default:Me(()=>[g(fGt,null,{"coach-speech":Me(()=>[k(W7)()?(O(),d(x9,{key:0,"animation-key":n.value,"bot-align":`bottom`,"coach-size":96,"is-coach-avatar-clickable":!1,"allow-animation-overflow-left":e.allowAnimationOverflowLeft,message:n.value,"should-auto-resize-bot-avatar":!1,"start-typewriter-after-mount":e.startTypewriterAfterMount,"prefer-pending-coach":``},null,8,[`animation-key`,`allow-animation-overflow-left`,`message`,`start-typewriter-after-mount`])):f(``,!0)]),_:1})]),_:1},8,[`src`]))}})})),FGt,IGt=r((()=>{PGt(),PGt(),FGt=NGt}));function LGt(){return B7().isCoachesModalOp
```

<a id="FND-30309"></a>
## FND-30309 — Implementation component coach-settings-modal

Vue compiled component __name declaration. Name suggests coach settings modal; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
().isCoachesModalOpen}var RGt=r((()=>{V7()})),zGt,BGt,VGt=r((()=>{RUt(),WWt(),cGt(),IGt(),$7(),RGt(),zGt={key:1},BGt=y({__name:`coach-settings-modal`,emits:[`change`],setup(e){let{audioToggle:t,coachesList:n,onChooseCoach:r,onClose:i,onToggleAudio:a}=UWt();return(e,o)=>k(LGt)()?(O(),d(LUt,{key:0,"audio-toggle":k(t),"selected-coach-id":k(Q7)(),onClose:k(i),onOnChooseCoachClick:k(r),onToggleAudio:k(a)},{"coach-speech-tagline":Me(()=>[g(FGt,{"start-typewriter-after-mount":``})]),"coach-selection-menu":Me(()=>[k(n)?.length?(O(),d(sGt,{key:0,"coaches-list":k(n),onChange:o[0]||=t=>e.$emit(`change`,t)},null,8,[`coaches-list`])):(O(),p(`div`,zGt,Se(e.$trans(`Loading coaches...`)),1))]),_:1},8,[`audio-toggle`,`selected-coach-id`,`onClose`,`onOnChooseCoachClick`,`onToggleAudio`])):f(``,!0)}})})),HGt,UGt=r((()=>{VGt(),VGt(),HGt=BGt}));function WGt(){let e=H7();return e.state.status!==Sd.Loaded||!!(e.state.data?.currentCoach||!MM())}var GGt=r((()=>{NM(),Cd(),U7()}));function KGt(){return y_()&&!__().isGuest}var qGt=r((()=>{v_(),b_()}));function p9(e){return/\s/.test(e)}function JGt(e,t){let n=Math.max(0,Math.min(e.length,t));if(!(n>0&&n<e.length&&!p9(e[n-1])&&!p9(e[n])))return{before:e.slice(0,n).join(``),wordVis
```

<a id="FND-30310"></a>
## FND-30310 — Implementation component typewriter-text

Vue compiled component __name declaration. Name suggests typewriter text; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
Kt,nKt,rKt,iKt,aKt=r((()=>{$Gt(),eKt=[`textContent`],tKt=[`textContent`],nKt=[`textContent`],rKt=[`textContent`],iKt=y({__name:`typewriter-text`,props:{chars:{},visibleCount:{}},setup(e){let t=e,n=l(()=>JGt(t.chars,t.visibleCount));return(e,t)=>(O(),p(`span`,{"aria-hidden":`true`,class:D(e.$style.tw)},[m(`span`,{textContent:Se(n.value.before)},null,8,eKt),m(`span`,{class:D(e.$style.word)},[m(`span`,{textContent:Se(n.value.wordVisible)},null,8,tKt),m(`span`,{class:D(e.$style.hidden),textContent:Se(n.value.wordHidden)},null,10,nKt)],2),m(`span`,{class:D(e.$style.hidden),textContent:Se(n.value.after)},null,10,rKt)],2))}})})),oKt,sKt,cKt=r((()=>{aKt(),aKt(),zue(),He(),oKt={$style:Ys},sKt=Ve(iKt,[[`__cssModules`,oKt]])})),lKt,uKt=r((()=>{lKt=y({__name:`animated-bot-speech`,props:{animationKey:{}},emits:[`speech-enter`],setup(e){let t=e,n=me(!0);function r(){n.value=!0}return Ae(()=>t.animationKey,(e,t)=>{n.value=!!(e&&!t)}),(e,t)=>(O(),d(c,{appear:``,"enter-active-class":e.$style[`enter-active`],"leave-active-class":e.$style[`leave-active`],"enter-from-class":e.$style[`enter-start`],"enter-to-class":e.$style[`enter-end`],"leave-from-class":e.$style[`leave-start`],"leave-to-class":e.$style[`leave-end`],onEn
```

<a id="FND-30311"></a>
## FND-30311 — Implementation component animated-bot-speech

Vue compiled component __name declaration. Name suggests animated bot speech; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
oKt,sKt,cKt=r((()=>{aKt(),aKt(),zue(),He(),oKt={$style:Ys},sKt=Ve(iKt,[[`__cssModules`,oKt]])})),lKt,uKt=r((()=>{lKt=y({__name:`animated-bot-speech`,props:{animationKey:{}},emits:[`speech-enter`],setup(e){let t=e,n=me(!0);function r(){n.value=!0}return Ae(()=>t.animationKey,(e,t)=>{n.value=!!(e&&!t)}),(e,t)=>(O(),d(c,{appear:``,"enter-active-class":e.$style[`enter-active`],"leave-active-class":e.$style[`leave-active`],"enter-from-class":e.$style[`enter-start`],"enter-to-class":e.$style[`enter-end`],"leave-from-class":e.$style[`leave-start`],"leave-to-class":e.$style[`leave-end`],onEnter:t[0]||=t=>e.$emit(`speech-enter`),onAfterLeave:r},{default:Me(()=>[n.value?_e(e.$slots,`default`,{},void 0,void 0,0):f(``,!0)]),_:3},8,[`enter-active-class`,`leave-active-class`,`enter-from-class`,`enter-to-class`,`leave-from-class`,`leave-to-class`]))}})})),dKt,fKt,pKt=r((()=>{uKt(),uKt(),tpe(),He(),dKt={$style:epe},fKt=Ve(lKt,[[`__cssModules`,dKt]])}));function m9(e){return e.clientWidth<2||e.clientHeight<2}function mKt(e){let t=e.prototype;if(t[h9])return;let n=t.draw;t.draw=function(e,t){let r=this.canvas;if(r instanceof HTMLCanvasElement&&m9(r)){this.stopRendering();return}if(this.activeArtboard===``){this.stopRen
```

<a id="FND-30312"></a>
## FND-30312 — Implementation component raw-rive-animation

Vue compiled component __name declaration. Name suggests raw rive animation; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
om.rive.tinyCanvasDrawGuard`)})),g9,_9,gKt,_Kt=r((()=>{a9(),g9=i9(),NK(),pc(),Zpe(),eme(),hKt(),ime(),lf(),_9=10,gKt=y({__name:`raw-rive-animation`,props:{fit:{default:`Contain`},alignment:{default:`CenterLeft`},layoutScaleFactor:{},riveFile:{},autoplay:{type:Boolean,default:!1},artboard:{},stateMachines:{default:`sm-main`},controls:{},initialBindings:{},height:{default:`100%`},width:{default:`100%`},respectReducedMotion:{type:Boolean,default:!1}},emits:[`statechange`,`loop`,`play`,`pause`,`load`,`advance`,`stop`],setup(e,{emit:t}){Ee(e=>({v75767f10:e.height,v17b65055:e.width})),mKt(g9.Rive);let n=e,r=t,i=kit(),a=l(()=>n.respectReducedMotion&&i.value===`reduce`);Ae(()=>[n.autoplay,n.stateMachines,n.riveFile],()=>pe()),Ae(()=>({fit:n.fit,alignment:n.alignment,layoutScaleFactor:n.layoutScaleFactor}),e=>ce(e));let o=ke(`canvas`),c=xe(null),u=me(!1),d=e=>{e.preventDefault(),pe()},m=xe(void 0),g=(e,t=_9)=>{if(!e)return;let n=c.value?.viewModelInstance;if(!n){if(t<=0){m.value=void 0;return}m.value=e,requestAnimationFrame(()=>{m.value===e&&g(e,t-1)});return}m.value=void 0,_(n,e)},_=(e,t)=>{let[n,r,...i]=t;switch(n){case`boolean`:{let t=e.boolean(r);if(!t)break;t.value=i[0];break}case`string`:{let t=e.string(
```

<a id="FND-30313"></a>
## FND-30313 — Implementation component unsafe-rive-animation

Vue compiled component __name declaration. Name suggests unsafe rive animation; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
=r((()=>{_Kt(),_Kt(),Ype(),He(),vKt={$style:Jpe},v9=Ve(gKt,[[`__cssModules`,vKt]])})),bKt,xKt=r((()=>{yKt(),d9(),bKt=y({__name:`unsafe-rive-animation`,props:{autoplay:{type:Boolean,default:!1},artboard:{},stateMachines:{default:`sm-main`},controls:{},height:{default:`100%`},width:{default:`100%`},fit:{default:`Contain`},alignment:{default:`CenterLeft`}},emits:[`statechange`,`loop`,`play`,`pause`,`load`,`advance`,`stop`],setup(e){let t=w(l9);ae(()=>{if(!t)throw Error("<unsafe-rive-animation> must be rendered inside an <unsafe-rive-file> ancestor that provides `riveFileKey`")});let n=l(()=>t?.value);return(t,r)=>(O(),d(v9,{"rive-file":n.value,autoplay:e.autoplay,artboard:e.artboard,"state-machines":e.stateMachines,controls:e.controls,height:e.height,width:e.width,fit:e.fit,alignment:e.alignment,onStatechange:r[0]||=e=>t.$emit(`statechange`,e),onLoop:r[1]||=e=>t.$emit(`loop`),onPlay:r[2]||=e=>t.$emit(`play`),onPause:r[3]||=e=>t.$emit(`pause`),onLoad:r[4]||=e=>t.$emit(`load`),onAdvance:r[5]||=e=>t.$emit(`advance`,e),onStop:r[6]||=e=>t.$emit(`stop`)},null,8,[`rive-file`,`autoplay`,`artboard`,`state-machines`,`controls`,`height`,`width`,`fit`,`alignment`]))}})})),y9,SKt=r((()=>{xKt(),xKt(),y9=bKt})),CKt,wKt
```

<a id="FND-30314"></a>
## FND-30314 — Implementation component animated-bot-avatar

Vue compiled component __name declaration. Name suggests animated bot avatar; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
),xKt(),y9=bKt})),CKt,wKt,TKt=r((()=>{mGt(),SKt(),CKt=[`data-emotion`,`data-viseme`,`data-lipsync`,`data-ready`],wKt=y({__name:`animated-bot-avatar`,props:{clickable:{type:Boolean,default:!1},allowAnimationOverflowLeft:{type:Boolean,default:!1}},emits:[`click`,`load`],setup(e,{emit:t}){let n=t,r=w(n9);if(!r)throw Error(`<animated-bot-avatar> must be rendered inside a useAnimatedCoach() scope`);let{rive:i,isReady:a,currentEmotion:o,currentViseme:s,currentLipsyncMode:c}=r;function l(){a.value=!0,n(`load`)}return oe(()=>{a.value=!1}),(t,n)=>(O(),p(`div`,{class:D([{[t.$style.clickable]:e.clickable,[t.$style.overflow]:e.allowAnimationOverflowLeft}]),"data-emotion":k(o),"data-viseme":k(s),"data-lipsync":k(c),"data-ready":k(a),onClick:n[0]||=n=>e.clickable&&t.$emit(`click`)},[m(`div`,{class:D([t.$style[`animation-container`],{[t.$style[`overflow-left`]]:e.allowAnimationOverflowLeft}])},[g(y9,{autoplay:!0,controls:k(i).controls,class:D(t.$style.animation),fit:`Contain`,alignment:e.allowAnimationOverflowLeft?`CenterRight`:`Center`,onLoad:l},null,8,[`controls`,`class`,`alignment`])],2)],10,CKt))}})})),EKt,DKt,OKt=r((()=>{TKt(),TKt(),qfe(),He(),EKt={$style:Kfe},DKt=Ve(wKt,[[`__cssModules`,EKt]])})),kKt,AKt=r((()
```

<a id="FND-30315"></a>
## FND-30315 — Implementation component bot-avatar-transition

Vue compiled component __name declaration. Name suggests bot avatar transition; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
Kt,DKt,OKt=r((()=>{TKt(),TKt(),qfe(),He(),EKt={$style:Kfe},DKt=Ve(wKt,[[`__cssModules`,EKt]])})),kKt,AKt=r((()=>{kKt=y({__name:`bot-avatar-transition`,props:{botAvatar:{},useTransition:{type:Boolean}},setup(e){let t=e,n=me(`fade-slide`);return Ae(()=>t.botAvatar,()=>{n.value=`fade-slide`}),(e,r)=>t.useTransition?(O(),d(c,{key:0,appear:``,name:n.value},{default:Me(()=>[_e(e.$slots,`default`)]),_:3},8,[`name`])):_e(e.$slots,`default`,{},void 0,void 0,1)}})})),jKt,MKt,NKt=r((()=>{AKt(),AKt(),rpe(),He(),jKt={$style:npe},MKt=Ve(kKt,[[`__cssModules`,jKt]])}));function PKt(e,t){return O(),p(`svg`,IKt,[...t[0]||=[m(`g`,{"clip-path":`url(#a)`},[m(`path`,{fill:`var(--color-bg-subtle)`,d:`M26.25 31.908v-.002c-.03-.144-.069-.337-.113-.573l-.038-.046-.054-.066c-.023-.189-.054-.398-.087-.626-.084-.581-.187-1.29-.247-2.13l.048.065c-.561-6.732.83-20.35 22.241-20.35 25.694 0 22.558 19.608 21.951 23.399a8.022 8.022 0 0 0-.08.56c-.12.75-.275 2.025-.45 3.616.65-.065 1.421.028 1.953.641.25.334.5.668.668 1.002.25.522.302 1.47.24 2.596 0 .456-.049.953-.127 1.46-.29 2.546-.918 5.425-1.144 6.463l-.054.25c-.084.417-.418 1.836-.919 2.254-.813.739-1.888.758-2.123.753l-.018.187v.002c-.318 3.41-.557 5.98-.613 6.32-.25 2.004-1.67 4
```

<a id="FND-30316"></a>
## FND-30316 — Implementation component bot-speech-avatar-and-wrapper

Vue compiled component __name declaration. Name suggests bot speech avatar and wrapper; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
FKt,[[`render`,PKt]])})),zKt,BKt,VKt=r((()=>{FK(),OKt(),NKt(),RKt(),d9(),kf(),zKt=[`alt`,`height`,`width`,`src`],BKt=y({__name:`bot-speech-avatar-and-wrapper`,props:{avatarOpacity:{},botAlign:{},botAvatar:{},botName:{},botSize:{},isBotAvatarClickable:{type:Boolean},allowAnimationOverflowLeft:{type:Boolean},shouldAutoResizeBotAvatar:{type:Boolean},shouldDockBotToBaseOfContainer:{type:Boolean},shouldHideOverflow:{type:Boolean},shouldShowBot:{type:Boolean},shouldStickBotToTop:{type:Boolean},shouldUseAvatarTransition:{type:Boolean},showBotNameTooltip:{type:Boolean,default:!0}},emits:[`choose-bot`],setup(e){let t=w(u9,void 0),n=l(()=>t?.value??!1),r=w(`forceStaticBotAvatar`,me(!1)),i=e,a=l(()=>i.botName?Ehe(i.botName):``),o=ke(`botContainer`);return de(`botContainer`,o),(t,s)=>(O(),p(`div`,{class:D(t.$style.component),style:ie({"--bot-size":e.botSize})},[m(`div`,{class:D([t.$style.avatarAndWrapper,t.$style[`bot-align-${e.botAlign}`],{[t.$style[`no-avatar`]]:!e.botAvatar,[t.$style[`avatar-auto-resize`]]:e.shouldAutoResizeBotAvatar,[t.$style[`hide-overflow`]]:e.shouldHideOverflow}])},[e.shouldShowBot?(O(),p(`div`,{key:0,ref_key:`botContainer`,ref:o,class:D([t.$style.bot,{[t.$style.docked]:e.shouldDockBotToBa
```

<a id="FND-30317"></a>
## FND-30317 — Implementation component bot-speech-content

Vue compiled component __name declaration. Name suggests bot speech content; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
(()=>{L7(),Eue(),kf(),GKt=[`width`,`height`,`viewBox`],KKt=[`d`],qKt=[`role`,`aria-live`,`aria-atomic`],b9=.0625,JKt=y({__name:`bot-speech-content`,props:{botAlign:{default:I7.botAlign},botSize:{},classificationKey:{default:I7.classificationKey},isFullWidthMessage:{type:Boolean,default:I7.isFullWidthMessage},isTyping:{type:Boolean},shouldAnimateTip:{type:Boolean,default:I7.shouldAnimateTip},shouldShowBot:{type:Boolean,default:I7.shouldShowBot},shouldShowTip:{type:Boolean,default:I7.shouldShowTip},shouldUseGameReviewHeight:{type:Boolean},shouldUseMinHeight:{type:Boolean,default:I7.shouldUseMinHeight},speechBubbleMatchesBotSize:{type:Boolean},tipObscured:{type:Boolean,default:I7.tipObscured},messageMaxWidth:{default:I7.messageMaxWidth}},setup(e){Ee(e=>({v044a38c5:c.value,v3e27f99c:d.value,v7934d3e8:u.value,v2659de4c:g.value}));let t=e,n=l(()=>t.botAlign===`above`),r={width:15,height:22,viewBox:`0 0 15 22`,path:`M0 14C8.4 14 12.8333 4.66667 15 0V22C15 22 3.5 22 0 14Z`},i={width:15,height:8,viewBox:`0 0 15 8`,path:`M0 0H15L8.7 7.4A1.6 1.6 0 0 1 6.3 7.4L0 0Z`},a=l(()=>n.value?i:r),o=l(()=>t.classificationKey?`${Dhe(t.classificationKey)}-animate`:``),s=l(()=>t.isFullWidthMessage?`100%`:t.messageMaxWidth?`${
```

<a id="FND-30318"></a>
## FND-30318 — Implementation component bot-speech-single-message

Vue compiled component __name declaration. Name suggests bot speech single message; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
ZKt=Ve(JKt,[[`__cssModules`,XKt]])})),$Kt,eqt,tqt=r((()=>{L7(),$Gt(),cKt(),pKt(),WKt(),QKt(),$Kt=[`textContent`],eqt=y({__name:`bot-speech-single-message`,props:{avatarOpacity:{},animationKey:{},botAlign:{default:I7.botAlign},botAvatar:{default:I7.botAvatar},botName:{default:I7.botName},botSize:{default:I7.botSize},classificationKey:{default:I7.classificationKey},allowAnimationOverflowLeft:{type:Boolean},isBotAvatarClickable:{type:Boolean,default:I7.isBotAvatarClickable()},shouldAutoResizeBotAvatar:{type:Boolean,default:I7.shouldAutoResizeBotAvatar},shouldShowBot:{type:Boolean,default:I7.shouldShowBot},shouldUseGameReviewHeight:{type:Boolean},speechBubbleMatchesBotSize:{type:Boolean},isFullWidthMessage:{type:Boolean,default:I7.isFullWidthMessage},message:{},messageMaxWidth:{default:I7.messageMaxWidth},showBotNameTooltip:{type:Boolean,default:!0},startTypewriterAfterMount:{type:Boolean}},emits:[`choose-bot`],setup(e){let t=e,{chars:n,visibleCount:r,isTyping:i,start:a}=YGt(()=>t.message==null?``:String(t.message),{autoStart:!t.startTypewriterAfterMount});function o(){t.startTypewriterAfterMount&&a()}Ae(()=>t.message,(e,n)=>{t.startTypewriterAfterMount&&e!==n&&n!=null&&a()});let s=l(()=>!!t.message||t.is
```

<a id="FND-30319"></a>
## FND-30319 — Implementation component coach-speech-single-message

Vue compiled component __name declaration. Name suggests coach speech single message; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
tooltip`]))}})})),nqt,rqt=r((()=>{tqt(),tqt(),nqt=eqt})),iqt,aqt=r((()=>{_Ut(),L7(),UGt(),G7(),GGt(),qGt(),rqt(),iqt=y({__name:`coach-speech-single-message`,props:{animationKey:{},botAlign:{},coachSize:{},isCoachAvatarClickable:{type:Boolean,default:!0},isFullWidthMessage:{type:Boolean,default:!0},message:{},allowAnimationOverflowLeft:{type:Boolean},messageMaxWidth:{},preferPendingCoach:{type:Boolean,default:!1},shouldAutoResizeBotAvatar:{type:Boolean,default:I7.shouldAutoResizeBotAvatar},shouldShowBot:{type:Boolean,default:I7.shouldShowBot},shouldUseGameReviewHeight:{type:Boolean},showCoachNameTooltip:{type:Boolean,default:!0},speechBubbleMatchesCoachSize:{type:Boolean},startTypewriterAfterMount:{type:Boolean}},setup(e){let t=e,n=l(()=>W7({preferPendingCoach:t.preferPendingCoach}));return(t,r)=>(O(),p(s,null,[g(nqt,{"allow-animation-overflow-left":e.allowAnimationOverflowLeft,"animation-key":e.animationKey,"bot-align":e.botAlign,"is-full-width-message":e.isFullWidthMessage,message:e.message,"message-max-width":e.messageMaxWidth,"bot-avatar":n.value?.imageUrl,"bot-name":n.value?.name,"bot-size":e.coachSize,"should-auto-resize-bot-avatar":e.shouldAutoResizeBotAvatar,"is-bot-avatar-clickable":k(KGt)()&&
```

<a id="FND-30320"></a>
## FND-30320 — Implementation component outgoing-challenge-box

Vue compiled component __name declaration. Name suggests outgoing challenge box; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
ntent`],xqt=[`textContent`],Sqt=[`textContent`],Cqt=[`textContent`],wqt={key:`tip-2`},Tqt=[`textContent`],E9=5e3,Eqt=y({__name:`outgoing-challenge-box`,props:{challenge:{},contextUser:{},currentUser:{},isFocusMode:{type:Boolean},presenceData:{},canCancelPendingChallenge:{type:Boolean}},emits:[`cancel-challenge`],setup(e,{emit:t}){let n=e,r=t,i=Te(),a=l(()=>({[i.component]:!0,[i[`focus-mode`]]:n.isFocusMode})),o=l(()=>n.challenge.isPlaceholderChallengeModel()),s=l(()=>o.value||n.contextUser?.isSameUser(n.challenge.getFrom())||n.currentUser.isSameUser(n.challenge.getFrom())),u=!n.challenge.getTo(),_=me(L(u?`Starting soon`:`Waiting for Opponent`)),v;u&&(v=window.setTimeout(b,E9));let y=me(0);function b(){y.value++,n.challenge.isDailyActiveSeekModel()&&(_.value=L(`You can leave this view. The game will start automatically.`)),y.value===1&&(_.value=L(`Still searching`)),y.value<3&&(v=window.setTimeout(b,E9))}le(()=>{v&&clearTimeout(v)});let x=l(()=>({[i.cancel]:!0,[i.hidden]:o.value&&!n.canCancelPendingChallenge}));function S(){r(`cancel-challenge`,{challenge:n.challenge})}let C=l(()=>n.presenceData?{isPlaying:n.presenceData.activity===pN.Playing,isOnline:n.presenceData.status===hN.Online}:null);return(t,n
```

<a id="FND-30321"></a>
## FND-30321 — Implementation component explorer-course-item

Vue compiled component __name declaration. Name suggests explorer course item; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1136
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
C(),rn(),gc=[`href`],_c=[`src`,`alt`],vc=[`textContent`],yc=[`textContent`],bc=[`textContent`],xc=[`textContent`],Sc=W({__name:`explorer-course-item`,props:{course:{}},emits:[`click-course`],setup(e){return(t,n)=>(K(),B(`a`,{class:G(t.$style.component),href:e.course.variationPreviewUrl,target:`_blank`,onClick:n[0]||=ri(n=>t.$emit(`click-course`,e.course),[`prevent`])},[V(`img`,{loading:`lazy`,crossorigin:`anonymous`,src:e.course.thumbnailUrl,alt:e.course.courseName,height:64,width:64,class:G(t.$style.thumbnail)},null,10,_c),n[5]||=H(),V(`div`,{class:G(t.$style.info)},[V(`div`,{textContent:Y(e.course.courseName),class:G([`cc-heading-xxx-small`,t.$style.title])},null,10,vc),n[3]||=H(),V(`div`,{textContent:Y(e.course.authorName),class:G([`cc-text-small-bold`,t.$style.author])},null,10,yc),n[4]||=H(),e.course.rating?(K(),B(`div`,{key:0,class:G(t.$style.review)},[V(`span`,{textContent:Y(e.course.rating.toFixed(1)),class:G([`cc-text-small-bold`,t.$style[`review-score`]])},null,10,bc),n[1]||=H(),U(p,{class:G(t.$style.star),is:X(me),size:16},null,8,[`class`,`is`]),n[2]||=H(),V(`span`,{textContent:Y(`(${e.course.numReviews})`),class:G([`cc-text-small`,t.$style[`review-count`]])},null,10,xc)],2)):z(``,!0)],2)],
```

<a id="FND-30322"></a>
## FND-30322 — Implementation component cc-skeleton-grid

Vue compiled component __name declaration. Name suggests cc skeleton grid; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1136
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
c))}})})),wc,Tc,Ec=t((()=>{Cc(),Cc(),vo(),D(),wc={$style:_o},Tc=T(Sc,[[`__cssModules`,wc]])})),Dc,Oc=t((()=>{gr(),Dc=W({__name:`cc-skeleton-grid`,props:{rows:{default:1},columns:{default:1},items:{},rowHeight:{default:`1.4rem`},rowGap:{default:`0`},columnWidth:{default:`1fr`},columnGap:{default:`0`}},setup(e){$r(e=>({v4d30a8e6:e.rowGap,v0075b50f:e.columnGap,v0e547957:X(n),v53a15299:X(r)}));let t=e,n=Array(t.columns).fill(t.columnWidth).join(` `),r=Array(t.rows).fill(t.rowHeight).join(` `);return(t,n)=>(K(),B(`div`,{class:G(t.$style.wrapper)},[e.items&&e.items.length>0?(K(!0),B(I,{key:0},J(e.items,(e,n)=>(K(),R(_r,{key:n,style:qr(`grid-area: ${e}`),class:G(t.$style.item)},null,8,[`style`,`class`]))),128)):(K(!0),B(I,{key:1},J(e.rows*e.columns,e=>(K(),R(_r,{key:e,class:G(t.$style.item)},null,8,[`class`]))),128))],2))}})})),kc,Ac,jc=t((()=>{Oc(),Oc(),Va(),D(),kc={$style:Ba},Ac=T(Dc,[[`__cssModules`,kc]])})),Mc,Nc,Pc=t((()=>{C(),Ec(),Gt(),Dr(),jc(),je(),window.chesscom=window.chesscom||{},window.chesscom.routes=window.chesscom.routes||{},Object.assign(window.chesscom.routes,{web_courses_shop:{tokens:[[`text`,`/courses/all`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|u
```

<a id="FND-30323"></a>
## FND-30323 — Implementation component explorer-courses

Vue compiled component __name declaration. Name suggests explorer courses; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1136
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
acchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}}),Mc=[`textContent`,`href`],Nc=W({__name:`explorer-courses`,props:{courses:{},isLoading:{type:Boolean},fen:{}},emits:[`click-course`,`view-courses`],setup(e,{emit:t}){let n=t,r=e,i=L(()=>sn.generate(`web_courses_shop`,{fen:r.fen,gameAspects:`openings`})),a=L(()=>sn.generate(`web_courses_shop`));function o(e){e.preventDefault(),window.open(a.value,`_blank`)}Z(()=>r.courses,()=>{s()},{immediate:!0});function s(){r.courses.length>0&&n(`view-courses`,r.courses)}return(t,n)=>(K(),B(`div`,{class:G(t.$style.component)},[e.isLoading&&e.courses.length===0?(K(),B(I,{key:0},J(5,e=>U(Ac,{key:e,rows:64,columns:17,"column-width":`1.6rem`,"row-height":`0.1rem`,items:[`1 / 1 / 65 / 5`,`1 / 6 / 17 / 18`,`21 / 6 / 37 / 14`,`41 / 6 / 57 / 10`]})),64)):z(``,!0),n[1]||=H(),(K(!0),B(I,null,J(e.courses,(e,r)=>(K(),R(Tc,{key:r,course:e,onClickCourse:n[0]||=e=>t.$emit(`click-course`,e)},null,8,[`course`]))),128)),n[2]||=H(),!e.isLoading&&e.courses.length===0?(K(),R(kr,{key:1,class:G(t.$style.empty),header:t.$trans(`No Courses in this position`),icon:{is:X(xn),variant:`glyph`},"icon-size":40},{default:Q(()=>[U(N,{size:`medium`,variant:`second
```

<a id="FND-30324"></a>
## FND-30324 — Implementation component explorer-move-list

Vue compiled component __name declaration. Name suggests explorer move list; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1136
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
yle:So},Ic=T(Nc,[[`__cssModules`,Fc]])})),Rc,zc=t((()=>{Me(),xr(),Rc=W({name:`ExplorerMoveList`,components:{MoveSan:br},__name:`explorer-move-list`,props:{playedMoves:{},startingMovePly:{},selectedMove:{}},emits:[`click-move`],setup(e,{emit:t}){let n=e,r=L(()=>n.startingMovePly===void 0?n.playedMoves[0]?.color??1:n.startingMovePly);function i(e,t){let n=Math.floor((e.moveNumber+r.value+1)/2);return e.color===E.ColorsAsNumbers.White?`${n}.`:t===0?`${n}...`:``}return(t,n)=>e.playedMoves.length?(K(),B(`h4`,{key:0,class:G(t.$style.moves)},[(K(!0),B(I,null,J(e.playedMoves,(n,r)=>(K(),R(br,{key:r,class:G(t.$style.move),color:n.color,highlighted:!!e.selectedMove&&e.selectedMove.ply===n.ply,san:n.san,"premove-text":i(n,r),onClick:e=>t.$emit(`click-move`,{ply:r})},null,8,[`class`,`color`,`highlighted`,`san`,`premove-text`,`onClick`]))),128))],2)):z(``,!0)}})})),Bc,Vc,Hc=t((()=>{zc(),zc(),Po(),D(),Bc={$style:No},Vc=T(Rc,[[`__cssModules`,Bc]])})),Uc,Wc=t((()=>{C(),rn(),Uc=W({name:`CaretIcon`,__name:`caret-icon`,props:{flip:{type:Boolean,default:!1},small:{type:Boolean,default:!1}},emits:[`click`],setup(e){let t=e,n=Qr(),r=L(()=>t.flip?gn:Jt),i=L(()=>t.small?12:16);return(e,t)=>(K(),R(p,{class:G(X(n).component),i
```

<a id="FND-30325"></a>
## FND-30325 — Implementation component caret-icon

Vue compiled component __name declaration. Name suggests caret icon; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1136
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
(()=>{zc(),zc(),Po(),D(),Bc={$style:No},Vc=T(Rc,[[`__cssModules`,Bc]])})),Uc,Wc=t((()=>{C(),rn(),Uc=W({name:`CaretIcon`,__name:`caret-icon`,props:{flip:{type:Boolean,default:!1},small:{type:Boolean,default:!1}},emits:[`click`],setup(e){let t=e,n=Qr(),r=L(()=>t.flip?gn:Jt),i=L(()=>t.small?12:16);return(e,t)=>(K(),R(p,{class:G(X(n).component),is:r.value,variant:`glyph`,size:i.value,onClick:t[0]||=t=>e.$emit(`click`,t)},null,8,[`class`,`is`,`size`]))}})})),Gc,Kc,qc=t((()=>{Wc(),Wc(),Ia(),D(),Gc={$style:Fa},Kc=T(Uc,[[`__cssModules`,Gc]])})),Jc,Yc,Xc,Zc,Qc,$c=t((()=>{qc(),cr(),rn(),Xn(),Jc=[`textContent`],Yc=[`textContent`],Xc=[`textContent`],Zc=[`textContent`],Qc=W({name:`GameItem`,__name:`game-item`,props:{blackName:{},blackRating:{default:null},blackTitle:{default:void 0},gameId:{},hasLost:{type:Boolean,default:!1},hasWon:{type:Boolean,default:!1},iconGlyph:{default:void 0},isExpanded:{type:Boolean,default:!1},isSelected:{type:Boolean},result:{},time:{},whiteName:{},whiteRating:{default:null},whiteTitle:{default:void 0},canSelectGame:{type:Boolean,default:!0}},emits:[`expand-game`,`select-game`],setup(e,{emit:t}){let n=e,r=t,i=Qr(),a=L(()=>({[i.component]:!0,[i.won]:n.hasWon,[i.lost]:n.hasLost}));functi
```

<a id="FND-30326"></a>
## FND-30326 — Implementation component game-item

Vue compiled component __name declaration. Name suggests game item; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1136
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
>{qc(),cr(),rn(),Xn(),Jc=[`textContent`],Yc=[`textContent`],Xc=[`textContent`],Zc=[`textContent`],Qc=W({name:`GameItem`,__name:`game-item`,props:{blackName:{},blackRating:{default:null},blackTitle:{default:void 0},gameId:{},hasLost:{type:Boolean,default:!1},hasWon:{type:Boolean,default:!1},iconGlyph:{default:void 0},isExpanded:{type:Boolean,default:!1},isSelected:{type:Boolean},result:{},time:{},whiteName:{},whiteRating:{default:null},whiteTitle:{default:void 0},canSelectGame:{type:Boolean,default:!0}},emits:[`expand-game`,`select-game`],setup(e,{emit:t}){let n=e,r=t,i=Qr(),a=L(()=>({[i.component]:!0,[i.won]:n.hasWon,[i.lost]:n.hasLost}));function o(){r(`select-game`,{gameId:n.gameId})}function s(e){e.target.id!==`toggle-game-${n.gameId}`&&r(`expand-game`,{gameId:n.gameId})}return(t,n)=>(K(),B(`div`,{class:G(a.value),onClick:s},[e.iconGlyph?(K(),R(p,{key:0,variant:`glyph`,is:e.iconGlyph,class:G([X(i)[`type-glyph`],`glyph-colored`]),size:20},null,8,[`is`,`class`])):z(``,!0),n[0]||=H(),U(dt,{"click-behavior":`none`,class:G(X(i).player),title:e.whiteTitle,username:e.whiteName},null,8,[`class`,`title`,`username`]),n[1]||=H(),V(`span`,{class:G(X(i).rating),textContent:Y(e.whiteRating?`(${e.whiteRating})`:`
```

<a id="FND-30327"></a>
## FND-30327 — Implementation component list-with-header

Vue compiled component __name declaration. Name suggests list with header; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1136
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
])})),rl,il,al,ol,sl=t((()=>{C(),cr(),rn(),ur(),rl=[`onClick`],il=[`id`],al=[`textContent`],ol=W({name:`ListWithHeader`,__name:`list-with-header`,props:{activeColumn:{default:void 0},currentSort:{default:void 0},emptyText:{default:void 0},headerColumns:{},isLoading:{type:Boolean},scrollAnchorId:{},scrollable:{type:Boolean,default:!0},showSelectAll:{type:Boolean,default:!0}},emits:[`select-all`,`sort-list`],setup(e,{emit:t}){let n=e,r=t,i=Qr(),a=L(()=>({[i.scroll]:!0,[i.scrollable]:n.scrollable}));function o(e){r(`select-all`,{isSelected:e})}function s(e){e&&r(`sort-list`,{column:e})}function c(e){return n.activeColumn?e===n.activeColumn?e===n.currentSort?gn:Jt:Be:Jt}return(t,n)=>(K(),B(`div`,{class:G(X(i).component)},[V(`div`,{class:G(X(i).header)},[(K(!0),B(I,null,J(e.headerColumns,(e,t)=>(K(),B(`div`,{key:t,class:G([X(i).column,e.className,{[X(i).sortable]:e.sort}]),onClick:t=>s(e.sort)},[H(Y(e.label)+` `,1),e.sort?(K(),R(p,{key:0,class:G(X(i).sort),is:c(e.sort),variant:`glyph`,size:12},null,8,[`class`,`is`])):z(``,!0)],10,rl))),128)),n[0]||=H(),e.showSelectAll?(K(),R(lr,{key:0,"aria-label":t.$trans(`Select All`),"model-value":!1,"onUpdate:modelValue":o},null,8,[`aria-label`])):z(``,!0)],2),n[2]||=H
```

<a id="FND-30328"></a>
## FND-30328 — Implementation component master-games

Vue compiled component __name declaration. Name suggests master games; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1136
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
l,fl=t((()=>{Hc(),nl(),ul(),A(),dl=W({name:`MasterGames`,components:{ExplorerMoveList:Vc,GameItem:tl,ListWithHeader:ll},__name:`master-games`,props:{boardId:{},gamePreviewMainLine:{default:()=>[]},gamePreviewSelectedMove:{default:null},currentSort:{},isLoadingMasterGames:{type:Boolean},masterGames:{},previewGameId:{},selectedMasterGames:{},scrollable:{type:Boolean,default:!0},canSelectGames:{type:Boolean,default:!0}},emits:[`click-move`,`expand-master-game`,`select-master-game`,`select-all-master-games`,`sort-master-games`],setup(e){let t=Qr(),n=e,r=L(()=>[{label:k(`Player`),className:t[`header-player`]},{label:k(`Rating`),className:t[`header-rating`]},{label:k(`Player`),className:t[`header-player`]},{label:k(`Rating`),className:t[`header-rating`]},{label:``,className:t[`header-expand`]},{label:k(`Result`),className:t[`header-result`]},{label:k(`Year`),className:t[`header-year`]}]),i=L(()=>n.masterGames.length?``:k(`No Master Games found.`));function a(e){return!!n.selectedMasterGames.find(t=>t.id===e)}return(t,n)=>(K(),R(ll,{"scroll-anchor-id":`master-scroll-anchor`,"is-loading":e.isLoadingMasterGames,"empty-text":i.value,"header-columns":r.value,"current-sort":e.currentSort,scrollable:e.scrollable,"
```

<a id="FND-30329"></a>
## FND-30329 — Implementation component archive-games

Vue compiled component __name declaration. Name suggests archive games; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1136
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
t((()=>{fl(),fl(),Bs(),D(),pl={$style:zs},ml=T(dl,[[`__cssModules`,pl]])})),gl,_l=t((()=>{Hc(),nl(),ul(),Ht(),A(),gl=W({__name:`archive-games`,props:{boardId:{},currentUsername:{},gamePreviewMainLine:{default:()=>[]},gamePreviewSelectedMove:{default:null},games:{},isLoading:{type:Boolean},isSearching:{type:Boolean},previewGameId:{default:null},selectedGames:{},selectedTimeControl:{default:``},username:{},scrollable:{type:Boolean,default:!0},canSelectGames:{type:Boolean,default:!0}},emits:[`click-move`,`select-game`,`expand-game`,`select-all-games`],setup(e){let t=e,n=Qr(),r=L(()=>t.games.length?``:t.isSearching?k(`No Games found.`):k(`You have not created any Games yet.`)),i=[{label:``,className:n[`header-type`]},{label:k(`Player`),className:n[`header-player`]},{label:k(`Rating`),className:n[`header-rating`]},{label:k(`Player`),className:n[`header-player`]},{label:k(`Rating`),className:n[`header-rating`]},{label:``,className:n[`header-expand`]},{label:k(`Result`),className:n[`header-result`]},{label:k(`Time`),className:n[`header-time`]}];function a(e){return t.selectedGames.some(t=>t.id===e)}return(t,n)=>(K(),R(ll,{"scroll-anchor-id":`archive-scroll-anchor`,"is-loading":e.isLoading,"empty-text":r.valu
```

<a id="FND-30330"></a>
## FND-30330 — Implementation component explorer-games

Vue compiled component __name declaration. Name suggests explorer games; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1136
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
__cssModules`,vl]])})),xl,Sl,Cl,wl=t((()=>{C(),hl(),yt(),bl(),Gt(),ur(),A(),xl=[`textContent`],Sl=[`textContent`],Cl=W({__name:`explorer-games`,props:{archiveSearch:{},boardId:{},currentUsername:{},gamePreviewMainLine:{},gamePreviewSelectedMove:{},games:{},isLoadingMasterGames:{type:Boolean},isLoading:{type:Boolean},isSearching:{type:Boolean},explorerSearch:{},masterGames:{},masterGamesCurrentSort:{},previewGameId:{},selectedGames:{},selectedMasterGames:{},selectedTimeControl:{},showImportMessage:{type:Boolean},showPremiumMessage:{type:Boolean},upgradeRoute:{},canSelectGames:{type:Boolean}},emits:[`click-move`,`expand-archive-game`,`expand-master-game`,`load-selected-games`,`select-all-games`,`select-all-master-games`,`select-game`,`select-master-game`,`sort-master-games`],setup(e){let t=e,n=L(()=>t.explorerSearch.source===F.Master),r=L(()=>{if(t.explorerSearch.source===F.Other&&!t.explorerSearch.username)return k(`Search for a %websiteName% user to see their games.`,{"%websiteName%":`Chess.com`});let e=t.archiveSearch?.fen?.split(` `)||[],n=Number(e[e.length-1]??1);return n>21||n===21&&e[1]===`b`?k(`Max Explorer depth reached.`):k(`There are no rated games in this position found in the database.`)});
```

<a id="FND-30331"></a>
## FND-30331 — Implementation component win-loss-draw

Vue compiled component __name declaration. Name suggests win loss draw; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1136
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
,Ao(),D(),Tl={$style:ko},El=T(Cl,[[`__cssModules`,Tl]])})),Ol,kl,Al=t((()=>{Ol=[`textContent`],kl=W({name:`WinLossDraw`,__name:`win-loss-draw`,props:{percentBlackWon:{},percentWhiteWon:{},percentDrawn:{}},setup(e){let t=e,n=L(()=>({white:t.percentWhiteWon,draw:t.percentDrawn,black:t.percentBlackWon}));return(e,t)=>(K(),B(`div`,{class:G(e.$style.component)},[(K(!0),B(I,null,J(Object.entries(n.value).filter(([e,t])=>t>0),([t,n])=>(K(),B(`div`,{key:t,class:G([e.$style.percentage,e.$style[`percentage-${t}`]]),style:qr({width:`${n}%`})},[V(`span`,{class:G([`cc-text-medium-bold`,e.$style[`percent-label`]]),textContent:Y(`${Math.round(n)}%`)},null,10,Ol)],6))),128))],2))}})})),jl,Ml,Nl=t((()=>{Al(),Al(),Na(),D(),jl={$style:Ma},Ml=T(kl,[[`__cssModules`,jl]])})),Pl,Fl,Il,Ll=t((()=>{xr(),Nl(),Cr(),je(),window.chesscom=window.chesscom||{},window.chesscom.routes=window.chesscom.routes||{},Object.assign(window.chesscom.routes,{web_master_games_search:{tokens:[[`text`,`/games/search`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE
```

<a id="FND-30332"></a>
## FND-30332 — Implementation component explorer-move-stats

Vue compiled component __name declaration. Name suggests explorer move stats; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1136
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
`https`]}}),Pl=[`textContent`],Fl=[`textContent`],Il=W({name:`ExplorerMoveStats`,components:{MoveSan:br,WinLossDraw:Ml},__name:`explorer-move-stats`,props:{move:{},playFrequencyLabel:{},startingMovePly:{},showMoveStatEvals:{type:Boolean,default:!0},isMasterGames:{type:Boolean,default:!1}},emits:[`click-move`],setup(e,{emit:t}){let n=e,r=t,i=L(()=>n.move.stats.blackWon),a=L(()=>n.move.stats.whiteWon),o=L(()=>n.move.stats.draw),s=L(()=>{if(n.move.ply<=0&&n.startingMovePly===1)return`1.`;let e=n.startingMovePly+n.move.ply;return e%2==0?`${e/2}.`:`${(e-1)/2}...`}),c=L(()=>!n.isMasterGames||!n.move.fen||n.move.stats.totalGames>1e4?null:sn.generate(`web_master_games_search`,{fen:n.move.fen})),l=L(()=>Sr(n.move.stats.totalGames));function u(){r(`click-move`,{move:n.move})}return(t,n)=>(K(),B(`div`,{class:G(t.$style.component)},[V(`button`,{type:`button`,class:G(t.$style.moveButton),onClick:u},[U(br,{class:G([`cc-text-medium-bold`,t.$style.move]),"premove-text":s.value,san:e.move.san},null,8,[`class`,`premove-text`,`san`])],2),n[0]||=H(),e.showMoveStatEvals?(K(),B(`div`,{key:0,class:G(t.$style[`eval-wrap`])},[e.move.stats.eval===void 0?z(``,!0):(K(),B(`span`,{key:0,class:G([`cc-monospace cc-text-medium-bold`,
```

<a id="FND-30333"></a>
## FND-30333 — Implementation component explorer-moves

Vue compiled component __name declaration. Name suggests explorer moves; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1136
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
,Vl,Hl,Ul,Wl=t((()=>{C(),Bl(),$s(),Nl(),Gt(),rn(),Cr(),Vl=[`textContent`],Hl=[`textContent`],Ul=W({name:`ExplorerMoves`,__name:`explorer-moves`,props:{suggestedMoves:{},showMoveStatEvals:{type:Boolean,default:!0},startingMovePly:{},isMasterGames:{type:Boolean,default:!1}},emits:[`click-move`],setup(e){let t=e,n=q(!1),r=L(()=>n.value?b:ce),i=L(()=>t.suggestedMoves.length>=5),a=L(()=>n.value?t.suggestedMoves:t.suggestedMoves.slice(0,5)),o=L(()=>t.suggestedMoves.reduce((e,t)=>e+t.stats.totalGames,0)),s=L(()=>t.suggestedMoves.length<2?!1:t.suggestedMoves.length>=5?n.value:!0),c=L(()=>Sr(o.value)),l=L(()=>o.value<=0?0:t.suggestedMoves.reduce((e,t)=>e+t.stats.totalGames*t.stats.whiteWon,0)/o.value),u=L(()=>o.value<=0?0:t.suggestedMoves.reduce((e,t)=>e+t.stats.totalGames*t.stats.draw,0)/o.value),d=L(()=>o.value<=0?0:t.suggestedMoves.reduce((e,t)=>e+t.stats.totalGames*t.stats.blackWon,0)/o.value);function f(){n.value=!n.value}function m(e){return Qs(e.stats.totalGames,o.value)}return(t,o)=>(K(),B(`div`,{class:G(t.$style.component)},[V(`div`,{class:G(t.$style.list)},[(K(!0),B(I,null,J(a.value,(n,r)=>(K(),R(zl,{key:r,move:n,"play-frequency-label":m(n),"show-move-stat-evals":e.showMoveStatEvals,"starting-move-pl
```

<a id="FND-30334"></a>
## FND-30334 — Implementation component explorer-moves-list-scrollable

Vue compiled component __name declaration. Name suggests explorer moves list scrollable; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1136
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
(Ul,[[`__cssModules`,Gl]])})),Jl,Yl,Xl,Zl,Ql=t((()=>{Me(),C(),xr(),Rn(),Jl=[`data-node-id`,`onClick`],Yl=1,Xl=.65,Zl=W({__name:`explorer-moves-list-scrollable`,props:{playedMoves:{},startingMovePly:{},selectedMoveIds:{}},emits:[`click-move`],setup(e){let t=e,n=Qr(),r=ni(`scrollContainer`),i=q(0),a=q(0),o=q(0),s=q(!1),c=L(()=>t.startingMovePly===void 0?t.playedMoves[0]?.color??1:t.startingMovePly),u=L(()=>Math.max(0,a.value-o.value)),d=L(()=>i.value>Yl),f=L(()=>i.value<u.value-Yl),p=L(()=>o.value<a.value&&i.value>Yl),m=L(()=>o.value<a.value&&i.value<u.value-Yl),h=L(()=>{if(p.value&&m.value)return n[`fade-both`];if(p.value)return n[`fade-left`];if(m.value)return n[`fade-right`]});function g(e){if(e?.ids)return`${e.ids.line}-${e.ids.move}`}function _(e,t){let n=Math.floor((e.moveNumber+c.value+1)/2);return e.color===E.ColorsAsNumbers.White?`${n}.`:t===0?`${n}...`:``}function v(e){return t.selectedMoveIds?t.selectedMoveIds.line===e.ids.line&&t.selectedMoveIds.move===e.ids.move:!1}function y(){let e=r.value;if(!e)return;i.value=e.scrollLeft,a.value=e.scrollWidth,o.value=e.clientWidth;let t=Math.max(0,e.scrollWidth-e.clientWidth);s.value=e.scrollLeft>=t-Yl}function b(){let e=r.value;if(!e||!d.value)return;l
```

<a id="FND-30335"></a>
## FND-30335 — Implementation component explorer-opening-header

Vue compiled component __name declaration. Name suggests explorer opening header; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1136
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
{Ql(),Ql(),ns(),D(),$l={$style:ts},eu=T(Zl,[[`__cssModules`,$l]])})),nu,ru,iu=t((()=>{C(),rn(),nu=[`textContent`],ru=W({__name:`explorer-opening-header`,props:{opening:{}},emits:[`reset-position`,`toggle-moves`],setup(e){let t=e,n=L(()=>{let{code:e,name:n}=t.opening;return e?`${e} ${n}`:n});return(e,t)=>(K(),B(`div`,{class:G(e.$style.component)},[U(p,{is:X(et),variant:`glyph`,class:G(e.$style.icon),size:20},null,8,[`is`,`class`]),t[0]||=H(),V(`span`,{class:G(e.$style.text),textContent:Y(n.value)},null,10,nu)],2))}})})),au,ou,su=t((()=>{iu(),iu(),ys(),D(),au={$style:vs},ou=T(ru,[[`__cssModules`,au]])})),cu,lu=t((()=>{Fr(),hn(),cu=W({name:`UsernameSearchInput`,__name:`username-search-input`,props:{leftIcon:{type:Boolean},showAvatar:{type:Boolean,default:!0},placeholder:{},userSearch:{},username:{},clearInput:{type:Boolean,default:!1},readonly:{type:Boolean,default:!1},size:{default:`small`}},emits:[`blur`,`clear-user`,`enter-user`,`query-change`,`search-username`,`select-user`],setup(e,{expose:t}){let n=e,r=ni(`autocomplete`),i=L(()=>Kt(n.userSearch.userSearchResults,[e=>+!e.are_friends]));function a(){r.value?.clearInput()}function o(e){r.value?.fillAutocomplete(e)}return t({clearAutocomplete:a,fillAut
```

<a id="FND-30336"></a>
## FND-30336 — Implementation component username-search-input

Vue compiled component __name declaration. Name suggests username search input; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1136
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
iu(),ys(),D(),au={$style:vs},ou=T(ru,[[`__cssModules`,au]])})),cu,lu=t((()=>{Fr(),hn(),cu=W({name:`UsernameSearchInput`,__name:`username-search-input`,props:{leftIcon:{type:Boolean},showAvatar:{type:Boolean,default:!0},placeholder:{},userSearch:{},username:{},clearInput:{type:Boolean,default:!1},readonly:{type:Boolean,default:!1},size:{default:`small`}},emits:[`blur`,`clear-user`,`enter-user`,`query-change`,`search-username`,`select-user`],setup(e,{expose:t}){let n=e,r=ni(`autocomplete`),i=L(()=>Kt(n.userSearch.userSearchResults,[e=>+!e.are_friends]));function a(){r.value?.clearInput()}function o(e){r.value?.fillAutocomplete(e)}return t({clearAutocomplete:a,fillAutocomplete:o}),(t,n)=>(K(),R(Pr,{ref_key:`autocomplete`,ref:r,"input-id":`username-search-input`,"input-name":`username-search-input`,"show-initial-options":``,"dont-clear-input":!e.clearInput,placeholder:e.placeholder,"is-searching":e.userSearch.isSearchingUser,"user-search-results":i.value,"search-exception-message":e.userSearch.userSearchMessage,class:G(t.$style.input),"left-icon":e.leftIcon,readonly:e.readonly,autofocus:!1,"initial-input-value":e.username,"current-input-value":e.username,"show-avatar":e.showAvatar,size:e.size,onBlur:n[0]|
```

<a id="FND-30337"></a>
## FND-30337 — Implementation component dropdown

Vue compiled component __name declaration. Name suggests dropdown; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1136
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
(),lu(),ba(),D(),uu={$style:ya},du=T(cu,[[`__cssModules`,uu]])})),pu,mu=t((()=>{C(),gt(),Er(),Ir(),rn(),vr(),ht(),pu=W({__name:`dropdown`,props:{disabled:{type:Boolean,default:!1},labelKey:{default:`label`},modelValue:{default:void 0},multiple:{type:Boolean,default:!1},options:{},placeholder:{default:``},preventEmptySelection:{type:Boolean,default:!1},valueKey:{default:`value`}},emits:[`update:modelValue`],setup(e,{emit:t}){let n=e,r=t,i=ei(),a=q(!1),o=ni(`menuRef`);Z(a,e=>{e&&Kr(()=>c())});let s=L(()=>{if(n.multiple){let e=Array.isArray(n.modelValue)?n.modelValue:[],t=n.options.filter(t=>e.some(e=>Tn(l(t),e)));return t.length===0?n.placeholder:t.map(e=>u(e)).join(`, `)}if(n.modelValue===void 0)return n.placeholder;let e=n.options.find(e=>Tn(l(e),n.modelValue));return e?u(e):n.placeholder});function c(){let e=o.value?.$el;if(!e)return;let t=e.querySelector(`[data-selected="true"]`);t&&t.scrollIntoView({block:`nearest`})}function l(e){return e[n.valueKey]}function u(e){return e[n.labelKey]}function d(e){return e.isClickable!==!1&&!e.disabled}function f(e){return n.multiple?(Array.isArray(n.modelValue)?n.modelValue:[]).some(t=>Tn(l(e),t)):Tn(l(e),n.modelValue)}function m(e){return f(e)?Ie:Ke}function h(
```

<a id="FND-30338"></a>
## FND-30338 — Implementation component date-range-selector

Vue compiled component __name declaration. Name suggests date range selector; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1136
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
){e?n(t):Nr.emit(dn.FILL_AUTOCOMPLETE,t)}var yu=t((()=>{Mr(),on()})),bu,xu,Su=t((()=>{Rr(),A(),bu=[`textContent`],xu=W({__name:`date-range-selector`,props:{startDate:{default:null},endDate:{default:null}},emits:[`update:startDate`,`update:endDate`],setup(e,{emit:t}){let n=q(!1),r=q(!1),i=new Date(2007,0,1),a=new Date,o=t;function s(e){return new Date(e.getFullYear(),e.getMonth(),1)}function c(e){return new Date(e.getFullYear(),e.getMonth()+1,0)}function l(e){o(`update:startDate`,e?s(e):null)}function u(e){o(`update:endDate`,e?c(e):null)}return(t,o)=>(K(),B(`div`,{class:G(t.$style[`date-range`])},[V(`span`,{textContent:Y(X(k)(`Date Range`)),class:G([`cc-text-medium-bold`,t.$style.label])},null,10,bu),o[5]||=H(),V(`div`,{class:G(t.$style[`date-inputs`])},[U(zr,{align:`bottom`,id:`search-form-start-month`,justify:`end`,type:`month-year`,"has-clear-button":n.value,class:G(t.$style[`date-input`]),"model-value":e.startDate,"placeholder-text":X(k)(`Start`),"start-date":X(i),"end-date":e.endDate||X(a),onMouseenter:o[0]||=e=>n.value=!0,onMouseleave:o[1]||=e=>n.value=!1,"onUpdate:modelValue":l},null,8,[`has-clear-button`,`class`,`model-value`,`placeholder-text`,`start-date`,`end-date`]),o[4]||=H(),U(zr,{align:`
```

<a id="FND-30339"></a>
## FND-30339 — Implementation component rating-range-selector

Vue compiled component __name declaration. Name suggests rating range selector; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1136
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
,Su(),oo(),D(),Cu={$style:ao},wu=T(xu,[[`__cssModules`,Cu]])})),Eu,Du,Ou=t((()=>{gu(),We(),A(),Eu=[`textContent`],Du=W({__name:`rating-range-selector`,props:{lowerRating:{},upperRating:{}},emits:[`update:lowerRating`,`update:upperRating`],setup(e,{emit:t}){let n=[0,200,400,600,800,1e3,1200,1400,1600,1800,2e3,2200,2400,2600,2800,3e3,tr],r=e,i=t,a=L(()=>n.slice(0,-1).map(e=>({label:e===0?k(`Min`):e.toString(),value:e}))),o=L(()=>n.filter(e=>e>r.lowerRating).map(e=>({label:e===4e3?k(`Max`):e.toString(),value:e})));function s(e){if(i(`update:lowerRating`,e),e>=r.upperRating){let t=n.indexOf(e),r=n[t+1];r!==void 0&&i(`update:upperRating`,r)}}function c(e){i(`update:upperRating`,e)}return(t,n)=>(K(),B(`div`,{class:G(t.$style.component)},[V(`span`,{textContent:Y(X(k)(`Rating Range`)),class:G([`cc-text-medium-bold`,t.$style.label])},null,10,Eu),n[1]||=H(),V(`div`,{class:G(t.$style.dropdowns)},[U($,{"model-value":e.lowerRating,options:a.value,"onUpdate:modelValue":s},null,8,[`model-value`,`options`]),n[0]||=H(),U($,{"model-value":e.upperRating,options:o.value,"onUpdate:modelValue":c},null,8,[`model-value`,`options`])],2)],2))}})})),ku,Au,ju=t((()=>{Ou(),Ou(),Zs(),D(),ku={$style:Xs},Au=T(Du,[[`__cssModules`,ku]
```

<a id="FND-30340"></a>
## FND-30340 — Implementation component explorer-search-form

Vue compiled component __name declaration. Name suggests explorer search form; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1136
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
t((()=>{Me(),C(),ie(),yt(),fu(),gu(),yu(),jr(),Gt(),Tu(),ju(),We(),Yn(),Ee(),A(),Mu=2e3,Nu=W({name:`ExplorerSearchForm`,__name:`explorer-search-form`,props:{openings:{},userSearch:{},playerSearch:{},explorerSearch:{},isLoggedIn:{type:Boolean,default:!0},archiveSearch:{}},emits:[`search-username`,`clear-user`,`clear-user-search-name`,`clear-player-search-name`,`search-explorer`],setup(e,{expose:t,emit:n}){let r=tr,i=e,a=n,o=q(),s=q(Ar()),c=q(0),l=q(i.explorerSearch.source),d=q(i.explorerSearch.username),f=q(``),p=q(``),m=q(``),h=q(E.ColorsAsWords.White),g=q(E.ColorsAsWords.White),_=q(E.ColorsAsWords.White),v=q(`all`),y=q(`all`),b=q(`all`),te=q(i.explorerSearch.allGamesTimeControls??[]),ne=q(i.explorerSearch.allGamesLowerRating??Mu),x=q(i.explorerSearch.allGamesUpperRating??r),S=q(null),re=q(null),ie=L(()=>[{label:k(`Master Games`),value:F.Master},...i.isLoggedIn?[{label:k(`My Games`),value:F.Own}]:[],{label:k(`Other players`),value:F.Other},{label:k(`All %websiteName% Games`,{"%websiteName%":`Chess.com`}),value:F.AllGames}]),ae=L(()=>[{label:k(`All Games`),value:`all`},...oe.value]),oe=L(()=>[{label:k(`Daily`),value:ut.Daily,icon:{is:Ne,variant:`glyph`},iconCustomClass:`cc-color-icon-daily`},{label:k(`
```

<a id="FND-30341"></a>
## FND-30341 — Implementation component explorer-search-modal

Vue compiled component __name declaration. Name suggests explorer search modal; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1136
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
Pu(),Ts(),D(),Fu={$style:ws},Iu=T(Nu,[[`__cssModules`,Fu]])})),Ru,zu,Bu=t((()=>{Lu(),On(),kt(),Ru=[`textContent`],zu=W({__name:`explorer-search-modal`,props:Gr({archiveSearch:{},userSearch:{},playerSearch:{},explorerSearch:{},openings:{},currentUsername:{}},{open:{type:Boolean,default:!1},openModifiers:{}}),emits:Gr([`clear-player-search-name`,`clear-user`,`clear-user-search-name`,`search-explorer`,`search-username`],[`update:open`]),setup(e,{emit:t}){let n=t,r=ti(e,`open`),i=q(0);Z(r,e=>{e&&(i.value+=1)});function a(){r.value=!1}function o(e){n(`search-explorer`,e),a()}return(t,s)=>r.value?(K(),R(Rt,{key:0,"modal-width":`md`,class:G(t.$style[`explorer-search-modal-container`]),"custom-classes":{dialog:t.$style[`explorer-search-modal-dialog`]},onHide:a},{default:Q(()=>[V(`div`,{class:G(t.$style[`explorer-search-modal`])},[V(`div`,{class:G(t.$style[`explorer-search-modal-header`])},[V(`h2`,{class:G(t.$style[`explorer-search-modal-title`]),textContent:Y(t.$trans(`Explore Games`))},null,10,Ru),s[4]||=H(),U(Kn,{onCloseModal:a})],2),s[5]||=H(),V(`div`,{class:G(t.$style[`explorer-search-modal-body`])},[(K(),R(Iu,{key:i.value,"archive-search":e.archiveSearch,"user-search":e.userSearch,"player-search":e.playe
```

<a id="FND-30342"></a>
## FND-30342 — Implementation component navigation

Vue compiled component __name declaration. Name suggests navigation; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1136
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
),Vu,Hu,Uu=t((()=>{Bu(),Bu(),Ns(),D(),Vu={$style:Ms},Hu=T(zu,[[`__cssModules`,Vu]])})),Wu,Gu=t((()=>{C(),x(),Gt(),Wu=W({__name:`navigation`,props:{isFirstPage:{type:Boolean},hasNextPage:{type:Boolean},scrollToAnchor:{}},emits:[`change-page`],setup(e,{emit:t}){let n=e,r=t;function i(e){document.getElementById(e||le.SCROLL_TOP_ANCHOR)?.scrollIntoView()}function a(e){r(`change-page`,{page:e}),i(n.scrollToAnchor)}return(t,n)=>(K(),B(`div`,{class:G(t.$style.component)},[U(N,{size:`x-small`,class:`cc-pagination-button cc-pagination-top`,"aria-label":t.$trans(`Back to Top`),icon:{is:X(b),variant:`glyph`},label:t.$trans(`Top`),onClick:n[0]||=t=>i(e.scrollToAnchor)},null,8,[`aria-label`,`icon`,`label`]),n[6]||=H(),V(`div`,{class:G(t.$style.buttons)},[U(N,{size:`x-small`,"aria-label":t.$trans(`First Page`),class:G([`cc-pagination-button`,t.$style.button,{"cc-pagination-disabled":e.isFirstPage}]),"custom-classes":{icon:`cc-pagination-icon`},disabled:e.isFirstPage,icon:{is:X(Ae),variant:`glyph`},onClick:n[1]||=e=>a(`first`)},null,8,[`aria-label`,`class`,`disabled`,`icon`]),n[4]||=H(),U(N,{size:`x-small`,"aria-label":t.$trans(`Previous Page`),class:G([`cc-pagination-button`,t.$style.button,{"cc-pagination-disabled
```

<a id="FND-30343"></a>
## FND-30343 — Implementation component add-games-button

Vue compiled component __name declaration. Name suggests add games button; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1136
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
})})),Ku,qu,Ju=t((()=>{Gu(),Gu(),Ks(),D(),Ku={$style:Gs},qu=T(Wu,[[`__cssModules`,Ku]])})),Yu,Xu=t((()=>{Gt(),A(),Yu=W({__name:`add-games-button`,props:{selectedGamesCount:{},loading:{type:Boolean}},emits:[`click`],setup(e){let t=e,n=L(()=>ot(`{0} Add 0 Games| {1} Add 1 Game|]1,Inf] Add %games% Games`,t.selectedGamesCount,{"%games%":t.selectedGamesCount}));return(t,r)=>e.selectedGamesCount>0?(K(),R(N,{key:0,size:`large`,variant:`primary`,loading:e.loading,class:G(t.$style.button),disabled:e.selectedGamesCount>100,label:n.value,onClick:r[0]||=e=>t.$emit(`click`,e)},null,8,[`loading`,`class`,`disabled`,`label`])):z(``,!0)}})})),Zu,Qu,$u=t((()=>{Xu(),Xu(),oi(),D(),Zu={$style:ai},Qu=T(Yu,[[`__cssModules`,Zu]])})),ed,td=t((()=>{Ju(),$u(),Br(),ed=W({__name:`add-games-footer`,props:{currentPage:{},scrollTo:{},selectedGamesCount:{},loading:{type:Boolean},totalPages:{},showNavigation:{type:Boolean},hasNextPage:{type:Boolean},isFirstPage:{type:Boolean}},emits:[`change-page`,`change-navigation-page`,`load-selected-games`],setup(e,{emit:t}){let n=t;function r(e){n(`change-page`,{page:e})}return(t,n)=>(K(),B(`div`,{class:G(t.$style.footer)},[e.showNavigation?(K(),R(qu,{key:0,"is-first-page":e.isFirstPage??!0,"has-
```

<a id="FND-30344"></a>
## FND-30344 — Implementation component add-games-footer

Vue compiled component __name declaration. Name suggests add games footer; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1136
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
Zu,Qu,$u=t((()=>{Xu(),Xu(),oi(),D(),Zu={$style:ai},Qu=T(Yu,[[`__cssModules`,Zu]])})),ed,td=t((()=>{Ju(),$u(),Br(),ed=W({__name:`add-games-footer`,props:{currentPage:{},scrollTo:{},selectedGamesCount:{},loading:{type:Boolean},totalPages:{},showNavigation:{type:Boolean},hasNextPage:{type:Boolean},isFirstPage:{type:Boolean}},emits:[`change-page`,`change-navigation-page`,`load-selected-games`],setup(e,{emit:t}){let n=t;function r(e){n(`change-page`,{page:e})}return(t,n)=>(K(),B(`div`,{class:G(t.$style.footer)},[e.showNavigation?(K(),R(qu,{key:0,"is-first-page":e.isFirstPage??!0,"has-next-page":e.hasNextPage??!1,"scroll-to-anchor":`explorer-scroll-anchor`,onChangePage:n[0]||=e=>t.$emit(`change-navigation-page`,e)},null,8,[`is-first-page`,`has-next-page`])):e.totalPages>1?(K(),R(Vr,{key:1,class:G(t.$style.pagination),"current-page":e.currentPage,"show-first-last-buttons":!1,"show-top-button":!0,"total-pages":e.totalPages,"scroll-to":e.scrollTo,onChangePage:r},null,8,[`class`,`current-page`,`total-pages`,`scroll-to`])):z(``,!0),n[2]||=H(),e.selectedGamesCount>0?(K(),R(Qu,{key:2,"selected-games-count":e.selectedGamesCount,loading:e.loading,onClick:n[1]||=e=>t.$emit(`load-selected-games`,e)},null,8,[`selected-
```

<a id="FND-30345"></a>
## FND-30345 — Implementation component board-explorer-tab

Vue compiled component __name declaration. Name suggests board explorer tab; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1136
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
),ad,od=t((()=>{C(),Lc(),Dl(),ql(),tu(),su(),Uu(),yt(),Vt(),Fe(),Hn(),id(),Gt(),Dr(),rn(),Zt(),fr(),pr(),A(),It(),ad=W({__name:`board-explorer-tab`,props:{archiveSearch:{},boardId:{},currentUsername:{},currentPage:{},gamePreviewMainLine:{},gamePreviewSelectedMove:{},games:{},isLoadingMasterGames:{type:Boolean},isLoading:{type:Boolean},isMoveListVisible:{type:Boolean},isSearching:{type:Boolean},explorerSearch:{},openings:{},opening:{},masterGames:{},masterGamesTotalPages:{},masterGamesCurrentPage:{},masterGamesCurrentSort:{},pagination:{},playedMoves:{},playerSearch:{},previewGameId:{},selectedGames:{},selectedMasterGames:{},selectedMoveIds:{},selectedMovePly:{},selectedTimeControl:{},showImportMessage:{type:Boolean},showMoveStatEvals:{type:Boolean},showPremiumMessage:{type:Boolean},startingMovePly:{},suggestedMoves:{},totalPages:{},upgradeRoute:{},userSearch:{},selectedExplorerTab:{},recommendedCourses:{},canSelectGames:{type:Boolean},showCourseRecommendationTab:{type:Boolean}},emits:[`change-page`,`change-master-games-page`,`clear-user`,`clear-user-search-name`,`clear-player-search-name`,`click-move`,`click-course`,`view-courses`,`expand-archive-game`,`expand-master-game`,`load-selected-games`,`load-
```

<a id="FND-30346"></a>
## FND-30346 — Implementation component load-from-explorer

Vue compiled component __name declaration. Name suggests load from explorer; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1136
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
,ve(),Et(),ln(),Fn(),ye(),He(),vt(),cf(),Le(),Yt(),uf(),hf(),Tr(),f(),zn(),Ce(),gf=W({name:`BoardExplorerTabController`,__name:`load-from-explorer`,setup(e){function t(e){if(e.source===F.Master&&e.username||e.source===F.Other&&e.username||e.source===F.Own)return e.color}let n=q(null),r=q(!0),a=q(`all`),s=q(null),c=q(!1),l=L(()=>bt()),u=L(()=>oe()),d=L(()=>mt()),f=L(()=>Pe().mainLine),p=L(()=>Pe().selectedNode),h=L(()=>re()),g=L(()=>Sd()),_=L(()=>it()),v=L(()=>ud()),y=L(()=>lt()),b=L(()=>In()),ee=L(()=>Od()),te=L(()=>ec()),x=L(()=>Xd()),ie=L(()=>!!Pt()),ae=L(()=>ie.value?Pt()?.username??``:``),se=L(()=>ef()),ce=L(()=>nf()),C=L(()=>Jd()),le=L(()=>Id()),ue=L(()=>Qd()),pe=L(()=>fd()),me=L(()=>Pd()),he=L(()=>Ed()),ge=L(()=>Rd()),_e=L(()=>bd()),ve=L(()=>vd()),T=L(()=>md()),ye=L(()=>gd()||void 0),be=L(()=>nc(i().game)),xe=L(()=>Ad()),Se=L(()=>sf()),Ce=L(()=>w()),Te=L(()=>Ce.value||Md()),E=L(()=>mn.upgradeMembership()),Ee=L(()=>Ln()),Oe=L(()=>wd());Yr(async()=>{wr(un.Events.Openings),Ft.isLoaded||af(),ff(),c.value=!0,await lf(),i().game.plugins.has(tn.Name)||(i().game.plugins.add(er({ecoPath:Vn(),http:Ye})),await i().game.eco.update()),Ae(),rt(void 0,t(_.value))}),Jr(()=>{let e=P();s.value!==null&&i().game.se
```

<a id="FND-30347"></a>
## FND-30347 — Implementation component ticker-icon

Vue compiled component __name declaration. Name suggests ticker icon; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1137
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
th:`20`,height:`20`,viewBox:`0 0 20 20`},CNt=Ae(xNt,[[`render`,bNt]])})),TNt,ENt=r((()=>{wNt(),TNt=_({name:`TickerIcon`,__name:`ticker-icon`,setup(e,{expose:t}){let n=se(0),r=c(()=>({transform:`rotate(${n.value}deg)`}));function i(){n.value+=90}return t({tick:i}),(e,t)=>(k(),u(CNt,{class:D(e.$style.component),style:ee(r.value)},null,8,[`class`,`style`]))}})})),DNt,ONt,kNt=r((()=>{ENt(),ENt(),Lle(),je(),DNt={$style:_s},ONt=Ae(TNt,[[`__cssModules`,DNt]])})),ANt,jNt,MNt,NNt,g5,_5=r((()=>{Ka(),ANt=[`aria-hidden`,`aria-label`,`role`],jNt=[`alt`,`aria-hidden`,`height`,`src`,`width`],MNt=[`aria-hidden`,`aria-label`,`role`],NNt=[`data-glyph`],g5=Ga(_({__name:`cc-icon`,props:{alt:{},color:{},customSize:{},host:{default:`https://assets-ds.chess.com`},is:{},name:{},size:{default:24},variant:{default:`glyph`}},setup(e){let t=e,n=c(()=>t.customSize?t.customSize:t.size),r=c(()=>t.customSize?`${t.customSize/10}rem`:void 0),i=c(()=>t.host.replace(/\/+$/,``)),a=c(()=>`${i.value}/color-icons/${t.name}.svg`),o=c(()=>`${i.value}/glyphs/${t.name}.svg`);return(t,i)=>e.is?(k(),f(`span`,{key:0,"aria-hidden":e.alt?void 0:`true`,"aria-label":e.alt?e.alt:void 0,class:D([t.$style[`cc-icon-glyph`],e.customSize?null:t.$style[`cc-i
```

<a id="FND-30348"></a>
## FND-30348 — Implementation component cc-icon

Vue compiled component __name declaration. Name suggests cc icon; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1137
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
`],jNt=[`alt`,`aria-hidden`,`height`,`src`,`width`],MNt=[`aria-hidden`,`aria-label`,`role`],NNt=[`data-glyph`],g5=Ga(_({__name:`cc-icon`,props:{alt:{},color:{},customSize:{},host:{default:`https://assets-ds.chess.com`},is:{},name:{},size:{default:24},variant:{default:`glyph`}},setup(e){let t=e,n=c(()=>t.customSize?t.customSize:t.size),r=c(()=>t.customSize?`${t.customSize/10}rem`:void 0),i=c(()=>t.host.replace(/\/+$/,``)),a=c(()=>`${i.value}/color-icons/${t.name}.svg`),o=c(()=>`${i.value}/glyphs/${t.name}.svg`);return(t,i)=>e.is?(k(),f(`span`,{key:0,"aria-hidden":e.alt?void 0:`true`,"aria-label":e.alt?e.alt:void 0,class:D([t.$style[`cc-icon-glyph`],e.customSize?null:t.$style[`cc-icon-size-${e.size}`]]),role:e.alt?`img`:void 0,style:ee({color:e.color,"--cc-icon-size":r.value})},[(k(),u(de(e.is),{height:n.value,width:n.value},null,8,[`height`,`width`]))],14,ANt)):e.variant===`color`?(k(),f(`img`,{key:1,"data-cy":`cc-icon`,alt:e.alt?e.alt:e.name,"aria-hidden":e.alt?void 0:`true`,class:D([t.$style[`cc-icon-img`],e.customSize?null:t.$style[`cc-icon-size-${e.size}`]]),height:n.value,src:a.value,style:ee({"--cc-icon-size":r.value}),width:n.value},null,14,jNt)):(k(),f(`span`,{key:2,"aria-hidden":e.alt?void 0:`
```

<a id="FND-30349"></a>
## FND-30349 — Implementation component move-time

Vue compiled component __name declaration. Name suggests move time; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1137
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
LIGHT:`light`,DARK:`dark`}})),zNt,BNt,VNt=r((()=>{oW(),kNt(),y5(),Hd(),RNt(),zNt=[`textContent`],BNt=_({name:`MoveTime`,__name:`move-time`,props:{clockIconTicks:{type:Boolean,default:!1},formatTime:{type:Boolean,default:!1},isMonospace:{type:Boolean,default:!1},isVacation:{type:Boolean,default:!1},showTimerIcon:{type:Boolean,default:!1},theme:{default:LNt.LIGHT},timeLeft:{default:`0:00:00`}},setup(e){let t=e,n=be(),r=xe(`tickerIcon`),i=c(()=>t.isVacation?Q$e:T0e),a=c(()=>{if(!t.formatTime)return t.timeLeft;let[e,n,r]=t.timeLeft.split(`:`),[i,a]=r.split(`.`);return Vd((Number(e)||0)*60*60*10+(Number(n)||0)*60*10+(Number(i)||0)*10+(Number(a)||0))}),o=c(()=>[n.time,n[t.theme],{[n.iconless]:!t.showTimerIcon,[n.inactive]:!t.showTimerIcon}]);return Se(()=>t.timeLeft,()=>{t.clockIconTicks&&r.value?.tick()}),(t,c)=>(k(),f(`div`,{class:D(o.value)},[e.showTimerIcon?(k(),f(s,{key:0},[e.clockIconTicks?(k(),u(ONt,{key:0,ref_key:`tickerIcon`,ref:r,class:D(ve(n).ticker)},null,8,[`class`])):(k(),u(v5,{key:1,is:i.value,class:D(ve(n).icon),size:24,variant:`glyph`},null,8,[`is`,`class`]))],64)):d(``,!0),c[0]||=m(),p(`div`,{class:D([ve(n).content,{[ve(n).monospace]:e.isMonospace}]),textContent:he(a.value)},null,10,zNt)],
```

<a id="FND-30350"></a>
## FND-30350 — Implementation component cc-avatar-pure

Vue compiled component __name declaration. Name suggests cc avatar pure; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1137
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
=r((()=>{P$(),Qle()})),qNt,JNt,YNt=r((()=>{Sh(),KNt(),Lf(),qNt=[`loading`,`src`,`srcset`,`alt`,`height`,`width`],JNt=_({__name:`cc-avatar-pure`,props:{src:{},clickBehavior:{default:`none`},isLazyLoading:{type:Boolean},retinaSupport:{type:Boolean,default:!0},responsiveSize:{},size:{default:40},status:{default:()=>({isOnline:!1,isPlaying:!1,isStreaming:!1})},username:{},userProfileUrl:{default:``}},setup(e){let{trans:t}=bh(),n=e,r=[`openProfile`,`openProfileInNewTab`],i=se(!1),a=se(!1),o=c(()=>n.status?.isStreaming?`streaming`:n.status?.isPlaying?`playing`:n.status?.isOnline?`online`:``),s=GNt(()=>n.size,n.responsiveSize),l=c(()=>n.username?t[`Avatar of %username%`](n.username):t.Avatar),d=c(()=>r.includes(n.clickBehavior)?`a`:`div`),f=c(()=>r.includes(n.clickBehavior)?n.userProfileUrl:null),h=c(()=>n.clickBehavior===`openProfileInNewTab`?`_blank`:null),g=c(()=>r.includes(n.clickBehavior)?n.username:null),_=c(()=>n.src&&n.retinaSupport&&!a.value?`${n.src} 1x, ${Ff(n.src)} 2x`:``),v=c(()=>i.value||!n.src?`/bundles/web/images/user-image.svg`:n.src);Se(()=>n.src,()=>{i.value=!1,a.value=!1});function y(e){e.target.srcset?a.value=!0:i.value=!0}return(t,n)=>(k(),u(de(d.value),{class:D([`cc-avatar-component`,`
```

<a id="FND-30351"></a>
## FND-30351 — Implementation component cc-avatar

Vue compiled component __name declaration. Name suggests cc avatar; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1137
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
3},8,[`class`,`href`,`title`,`target`]))}})})),XNt,ZNt=r((()=>{YNt(),YNt(),XNt=JNt})),QNt,$Nt=r((()=>{ZNt(),Sh(),QNt=_({__name:`cc-avatar`,props:{src:{},clickBehavior:{default:`none`},isLazyLoading:{type:Boolean,default:!0},retinaSupport:{type:Boolean,default:!0},responsiveSize:{},size:{default:40},status:{default:()=>({isOnline:!1,isPlaying:!1,isStreaming:!1})},url:{},username:{}},setup(e){let t=e,{routes:n}=bh(),r=c(()=>t.url||n.webMemberView(t.username));return(t,n)=>(k(),u(XNt,T(t.$attrs,{src:e.src,"click-behavior":e.clickBehavior,"retina-support":e.retinaSupport,"responsive-size":e.responsiveSize,size:e.size,status:e.status,"is-lazy-loading":e.isLazyLoading,username:e.username,"user-profile-url":r.value}),{default:Ce(()=>[ue(t.$slots,`default`)]),_:3},16,[`src`,`click-behavior`,`retina-support`,`responsive-size`,`size`,`status`,`is-lazy-loading`,`username`,`user-profile-url`]))}})})),b5,ePt=r((()=>{$Nt(),$Nt(),b5=QNt})),tPt,nPt,rPt=r((()=>{P$(),ef(),tPt=200,nPt=_({__name:`cc-tooltip`,props:{allowMobile:{type:Boolean},anchor:{default:`center`},closeOnClick:{type:Boolean},delay:{default:200},forElement:{},forPreviousElement:{type:Boolean},position:{default:`top`},text:{},stickyVisible:{type:Boolean
```

<a id="FND-30352"></a>
## FND-30352 — Implementation component cc-tooltip

Vue compiled component __name declaration. Name suggests cc tooltip; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1137
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
username`,`user-profile-url`]))}})})),b5,ePt=r((()=>{$Nt(),$Nt(),b5=QNt})),tPt,nPt,rPt=r((()=>{P$(),ef(),tPt=200,nPt=_({__name:`cc-tooltip`,props:{allowMobile:{type:Boolean},anchor:{default:`center`},closeOnClick:{type:Boolean},delay:{default:200},forElement:{},forPreviousElement:{type:Boolean},position:{default:`top`},text:{},stickyVisible:{type:Boolean},triggerElement:{default:null}},setup(e){let t=e,n=ymt(),r=Math.max(10,t.delay),i=me(),a=me(!1),o=me(!1),s=xe(`popoverEl`),c,l,u;function h(){return typeof window>`u`||typeof window.matchMedia!=`function`?!0:window.matchMedia(`(hover: hover) and (pointer: fine)`)?.matches??!0}function g(){if(_(),c=t.forElement??(t.forPreviousElement?n.value?.previousElementSibling:n.value?.parentElement),l=t.triggerElement??c,t.stickyVisible){S();return}if(!h()){l?.addEventListener(`click`,b);return}t.closeOnClick&&l?.addEventListener(`click`,v),l?.addEventListener(`mouseenter`,y)}function _(){clearTimeout(u),l?.removeEventListener(`click`,v),l?.removeEventListener(`mouseleave`,v),l?.removeEventListener(`mouseenter`,y),l?.removeEventListener(`click`,b),document.removeEventListener(`click`,x)}ne(()=>{!h()&&!t.allowMobile||E(g)}),ie(_);function v(){o.value=!1,clearTimeo
```

<a id="FND-30353"></a>
## FND-30353 — Implementation component flair

Vue compiled component __name declaration. Name suggests flair; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1137
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
lPt=r((()=>{S5(),aPt=[`href`,`aria-label`],oPt=[`alt`,`width`,`height`,`src`],sPt=[`alt`,`width`,`height`,`src`],cPt=_({__name:`flair`,props:{alt:{},href:{},size:{default:`small`},src:{},tooltipPosition:{}},emits:[`click`],setup(e){let t={small:`16`,medium:`24`,large:`32`}[e.size];return(n,r)=>(k(),f(s,null,[e.href?(k(),f(`a`,T({key:0},n.$attrs,{href:e.href,"aria-label":e.alt,onClick:r[0]||=e=>n.$emit(`click`,e)}),[p(`img`,{alt:e.alt,class:D([`flair-rpc-component`,`flair-rpc-${e.size}`]),width:ve(t),height:ve(t),src:e.src},null,10,oPt),r[2]||=m(),e.alt?(k(),u(x5,{key:0,"for-previous-element":``,position:e.tooltipPosition,text:e.alt},null,8,[`position`,`text`])):d(``,!0)],16,aPt)):(k(),f(`img`,T({key:1},n.$attrs,{alt:e.alt,class:[`flair-rpc-component`,`flair-rpc-${e.size}`],width:ve(t),height:ve(t),src:e.src,onClick:r[1]||=e=>n.$emit(`click`,e)}),null,16,sPt)),r[3]||=m(),e.alt?(k(),u(x5,{key:2,"close-on-click":``,"for-previous-element":``,position:e.tooltipPosition,text:e.alt},null,8,[`position`,`text`])):d(``,!0)],64))}})})),uPt,dPt=r((()=>{lPt(),lPt(),uPt=cPt}));function fPt(e){return!!(e?.id&&window.chesscom.features?.includes(`premium_badge_redesign`)&&r3e.includes(e.id))}var pPt=r((()=>{XW()}));fu
```

<a id="FND-30354"></a>
## FND-30354 — Implementation component flair

Vue compiled component __name declaration. Name suggests flair; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1137
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
user]:z(`Closed: Abuse`),[UW.voluntarilyClosed]:z(`Closed: Inactive`)}})),vPt,yPt=r((()=>{d4(),dPt(),hPt(),_Pt(),vPt=_({__name:`flair`,props:{disableHref:{type:Boolean,default:!1},flair:{},membershipLevel:{default:u4(`getMembershipLevel`)},size:{default:`small`},tooltipPosition:{}},emits:[`log-action`],setup(e){let t=e,n=c(()=>mPt(t.flair)),r=c(()=>gPt(t.flair,t.membershipLevel));return(t,i)=>n.value?(k(),u(uPt,{key:0,alt:r.value,size:e.size,src:n.value,"tooltip-position":e.tooltipPosition,onClick:i[0]||=e=>t.$emit(`log-action`,{button:`flair`})},null,8,[`alt`,`size`,`src`,`tooltip-position`])):d(``,!0)}})})),w5,T5=r((()=>{yPt(),yPt(),w5=vPt})),bPt,xPt=r((()=>{S5(),Sh(),bPt=_({__name:`cc-country-flag`,props:{code:{},isClickable:{type:[Boolean,null],default:!0},name:{},showTooltip:{type:Boolean,default:!0},size:{default:`small`},tooltipPosition:{default:`top`},tooltipText:{}},setup(e){let t=e,{countryName:n,features:r,routes:i,trans:a}=bh(),o=c(()=>l.value||h.value?`sanctioned`:t.code.toString().toLowerCase()),s=c(()=>t.code.toString().toUpperCase()),l=c(()=>[`FD`,`431`].includes(s.value)),p=c(()=>[`RU`,`116`].includes(s.value)),m=c(()=>[`BY`,`22`].includes(s.value)),h=c(()=>!!(r.includes(`sanction_rus
```

<a id="FND-30355"></a>
## FND-30355 — Implementation component cc-country-flag

Vue compiled component __name declaration. Name suggests cc country flag; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1137
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
,`size`,`src`,`tooltip-position`])):d(``,!0)}})})),w5,T5=r((()=>{yPt(),yPt(),w5=vPt})),bPt,xPt=r((()=>{S5(),Sh(),bPt=_({__name:`cc-country-flag`,props:{code:{},isClickable:{type:[Boolean,null],default:!0},name:{},showTooltip:{type:Boolean,default:!0},size:{default:`small`},tooltipPosition:{default:`top`},tooltipText:{}},setup(e){let t=e,{countryName:n,features:r,routes:i,trans:a}=bh(),o=c(()=>l.value||h.value?`sanctioned`:t.code.toString().toLowerCase()),s=c(()=>t.code.toString().toUpperCase()),l=c(()=>[`FD`,`431`].includes(s.value)),p=c(()=>[`RU`,`116`].includes(s.value)),m=c(()=>[`BY`,`22`].includes(s.value)),h=c(()=>!!(r.includes(`sanction_russia_flag`)&&p.value)||!!(r.includes(`sanction_belarus_flag`)&&m.value)),g=c(()=>{if(t.showTooltip)return l.value?a[`Due to the ongoing war and resulting international sanctions, Russian and Belarusian flags will not be shown for players in Verified events.`]:t.tooltipText===void 0?n(t.code)??t.name:t.tooltipText}),_=i.webArticleUkraine;return(t,n)=>h.value?(k(),u(de(e.isClickable?`a`:`div`),{key:0,href:e.isClickable?ve(_):null,target:e.isClickable?`_blank`:null,class:D([`cc-country-flag-component`,`country-${o.value}`,{[`cc-country-flag-${e.size}`]:e.size}])},
```

<a id="FND-30356"></a>
## FND-30356 — Implementation component cc-user-badge-pure

Vue compiled component __name declaration. Name suggests cc user badge pure; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1137
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
 n?t?n===HW.staff||n===HW.moderator||r:!e&&r:!1}var jPt=r((()=>{WW()})),MPt,NPt=r((()=>{oW(),GW(),y5(),S5(),Sh(),MPt=_({__name:`cc-user-badge-pure`,props:{badgeUrl:{},isClickable:{type:Boolean},membership:{},size:{},tooltipPosition:{}},setup(e){let{features:t,trans:n}=bh(),r=e,i=c(()=>t.includes(`premium_badge_redesign`)),a=c(()=>{switch(r.size){case`medium`:return 16;case`large`:return 20;default:return 12}}),o=c(()=>{switch(r.size){case`medium`:return 20;case`large`:return 24;default:return 16}}),s=c(()=>{switch(r.membership){case HW.staff:return{type:`staff`,icon:B1e,colorIcon:`pawn-staff`,tooltip:n[`Staff Member`],redirectTo:`about`};case HW.moderator:return{type:`moderator`,icon:R2e,colorIcon:`pawn-mod`,tooltip:n.Moderator,redirectTo:`about`};case HW.gold:return{type:`gold`,icon:h1e,colorIcon:`commerce-gold`,tooltip:n[`Gold Member`],redirectTo:`membership`};case HW.platinum:return{type:`platinum`,icon:v1e,colorIcon:`commerce-platinum`,tooltip:n[`Platinum Member`],redirectTo:`membership`};case HW.diamond:return{type:`diamond`,icon:f1e,colorIcon:`commerce-diamond`,tooltip:n[`Diamond Member`],redirectTo:`membership`};default:return null}});return(t,n)=>s.value?(k(),u(de(e.isClickable?`a`:`div`),{key
```

<a id="FND-30357"></a>
## FND-30357 — Implementation component cc-user-badge

Vue compiled component __name declaration. Name suggests cc user badge; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1137
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
)=>{NPt(),NPt(),Jle(),je(),PPt={$style:wc},FPt=Ae(MPt,[[`__cssModules`,PPt]])})),LPt,RPt=r((()=>{GW(),IPt(),Sh(),LPt=_({__name:`cc-user-badge`,props:{isClickable:{type:Boolean},membership:{},size:{},tooltipPosition:{}},setup(e){let t=e,{currentRoute:n,routes:r}=bh(),i=c(()=>{switch(t.membership){case HW.staff:return{type:`staff`,redirectTo:`about`};case HW.moderator:return{type:`moderator`,redirectTo:`about`};case HW.gold:return{type:`gold`,redirectTo:`membership`};case HW.platinum:return{type:`platinum`,redirectTo:`membership`};case HW.diamond:return{type:`diamond`,redirectTo:`membership`};default:return null}}),a=c(()=>i.value?.redirectTo===`membership`?r.webMembership({b:`badge-${i.value?.type}`,c:n()}):i.value?.redirectTo===`about`?r.webAbout:null);return(t,n)=>(k(),u(FPt,T(t.$attrs,{"is-clickable":e.isClickable,membership:e.membership,size:e.size,"tooltip-position":e.tooltipPosition,"badge-url":a.value}),null,16,[`is-clickable`,`membership`,`size`,`tooltip-position`,`badge-url`]))}})})),D5,zPt=r((()=>{RPt(),RPt(),D5=LPt})),BPt,VPt=r((()=>{BPt=_({__name:`cc-user-rating`,props:{rating:{},variant:{default:`default`},size:{default:``}},setup(e){return(t,n)=>(k(),f(`div`,{class:D([e.size===`large`?`cc
```

<a id="FND-30358"></a>
## FND-30358 — Implementation component cc-user-rating

Vue compiled component __name declaration. Name suggests cc user rating; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1137
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
`membership`,`size`,`tooltip-position`,`badge-url`]))}})})),D5,zPt=r((()=>{RPt(),RPt(),D5=LPt})),BPt,VPt=r((()=>{BPt=_({__name:`cc-user-rating`,props:{rating:{},variant:{default:`default`},size:{default:``}},setup(e){return(t,n)=>(k(),f(`div`,{class:D([e.size===`large`?`cc-text-x-large`:`cc-text-medium`,t.$style[e.variant]])},`
    (`+he(e.rating)+`)
  `,3))}})})),HPt,O5,UPt=r((()=>{VPt(),VPt(),Yle(),je(),HPt={$style:Oc},O5=Ae(BPt,[[`__cssModules`,HPt]])})),WPt,GPt=r((()=>{XW(),S5(),WPt=_({__name:`cc-user-title-pure`,props:{isClickable:{type:Boolean},title:{},size:{default:``},tooltipPosition:{},titleUrl:{default:``}},setup(e){let t=e,n=c(()=>YW[t.title]),r=c(()=>t.size===`large`?`cc-text-x-large-bold`:t.size===`medium`?`cc-text-small-bold`:`cc-text-x-small-bold`);return(t,i)=>(k(),f(s,null,[(k(),u(de(e.isClickable?`a`:`div`),{class:D([t.$style.component,r.value]),href:e.isClickable?e.titleUrl:null,target:e.isClickable?`_blank`:null},{default:Ce(()=>[m(he(e.title),1)]),_:1},8,[`class`,`href`,`target`])),i[0]||=m(),h(x5,{"close-on-click":``,"for-previous-element":``,text:n.value,position:e.tooltipPosition},null,8,[`text`,`position`])],64))}})})),KPt,qPt,JPt=r((()=>{GPt(),GPt(),Xle(),je(),KPt={$style:Ac
```

<a id="FND-30359"></a>
## FND-30359 — Implementation component cc-user-title-pure

Vue compiled component __name declaration. Name suggests cc user title pure; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1137
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
Pt=r((()=>{VPt(),VPt(),Yle(),je(),HPt={$style:Oc},O5=Ae(BPt,[[`__cssModules`,HPt]])})),WPt,GPt=r((()=>{XW(),S5(),WPt=_({__name:`cc-user-title-pure`,props:{isClickable:{type:Boolean},title:{},size:{default:``},tooltipPosition:{},titleUrl:{default:``}},setup(e){let t=e,n=c(()=>YW[t.title]),r=c(()=>t.size===`large`?`cc-text-x-large-bold`:t.size===`medium`?`cc-text-small-bold`:`cc-text-x-small-bold`);return(t,i)=>(k(),f(s,null,[(k(),u(de(e.isClickable?`a`:`div`),{class:D([t.$style.component,r.value]),href:e.isClickable?e.titleUrl:null,target:e.isClickable?`_blank`:null},{default:Ce(()=>[m(he(e.title),1)]),_:1},8,[`class`,`href`,`target`])),i[0]||=m(),h(x5,{"close-on-click":``,"for-previous-element":``,text:n.value,position:e.tooltipPosition},null,8,[`text`,`position`])],64))}})})),KPt,qPt,JPt=r((()=>{GPt(),GPt(),Xle(),je(),KPt={$style:Ac},qPt=Ae(WPt,[[`__cssModules`,KPt]])})),YPt,XPt=r((()=>{JPt(),Sh(),YPt=_({__name:`cc-user-title`,props:{isClickable:{type:Boolean},title:{},size:{default:``},tooltipPosition:{}},setup(e){let{routes:t}=bh(),n=t.webMemberTitledPlayers;return(t,r)=>(k(),u(qPt,{"is-clickable":e.isClickable,title:e.title,size:e.size,"tooltip-position":e.tooltipPosition,"title-url":ve(n)},null,8
```
