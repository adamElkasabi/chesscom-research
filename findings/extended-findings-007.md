# Extended findings

[Master index](../chapters/00_MASTER_INDEX.md)

<a id="FND-30360"></a>
## FND-30360 — Implementation component cc-user-title

Vue compiled component __name declaration. Name suggests cc user title; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1137
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
=r((()=>{GPt(),GPt(),Xle(),je(),KPt={$style:Ac},qPt=Ae(WPt,[[`__cssModules`,KPt]])})),YPt,XPt=r((()=>{JPt(),Sh(),YPt=_({__name:`cc-user-title`,props:{isClickable:{type:Boolean},title:{},size:{default:``},tooltipPosition:{}},setup(e){let{routes:t}=bh(),n=t.webMemberTitledPlayers;return(t,r)=>(k(),u(qPt,{"is-clickable":e.isClickable,title:e.title,size:e.size,"tooltip-position":e.tooltipPosition,"title-url":ve(n)},null,8,[`is-clickable`,`title`,`size`,`tooltip-position`,`title-url`]))}})})),k5,ZPt=r((()=>{XPt(),XPt(),k5=YPt})),QPt,$Pt=r((()=>{QPt=_({__name:`cc-user-username-pure`,props:{clickBehavior:{},customUrl:{},username:{},variant:{default:`boldest`},size:{default:``},userProfileUrl:{default:``}},emits:[`log-action`],setup(e){let t=[`openProfile`,`openProfileInNewTab`],n=e,r=c(()=>t.includes(n.clickBehavior)?`a`:`div`),i=c(()=>t.includes(n.clickBehavior)?n.userProfileUrl:null),a=c(()=>n.clickBehavior===`openProfileInNewTab`?`_blank`:null),o=c(()=>{let e={};return n.clickBehavior===`badgeAsLink`&&(e.role=`button`,e.tabindex=0),e});return(t,n)=>(k(),u(de(r.value),T(o.value,{class:[`cc-text-medium-bold`,[t.$style.component,t.$style[e.variant],t.$style[e.size]]],href:i.value,target:a.value,onClick:n[0]|
```

<a id="FND-30361"></a>
## FND-30361 — Implementation component cc-user-username-pure

Vue compiled component __name declaration. Name suggests cc user username pure; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1137
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
ble`,`title`,`size`,`tooltip-position`,`title-url`]))}})})),k5,ZPt=r((()=>{XPt(),XPt(),k5=YPt})),QPt,$Pt=r((()=>{QPt=_({__name:`cc-user-username-pure`,props:{clickBehavior:{},customUrl:{},username:{},variant:{default:`boldest`},size:{default:``},userProfileUrl:{default:``}},emits:[`log-action`],setup(e){let t=[`openProfile`,`openProfileInNewTab`],n=e,r=c(()=>t.includes(n.clickBehavior)?`a`:`div`),i=c(()=>t.includes(n.clickBehavior)?n.userProfileUrl:null),a=c(()=>n.clickBehavior===`openProfileInNewTab`?`_blank`:null),o=c(()=>{let e={};return n.clickBehavior===`badgeAsLink`&&(e.role=`button`,e.tabindex=0),e});return(t,n)=>(k(),u(de(r.value),T(o.value,{class:[`cc-text-medium-bold`,[t.$style.component,t.$style[e.variant],t.$style[e.size]]],href:i.value,target:a.value,onClick:n[0]||=e=>t.$emit(`log-action`,{button:`nameClick`})}),{default:Ce(()=>[m(he(e.username),1)]),_:1},16,[`class`,`href`,`target`]))}})})),eFt,tFt,nFt=r((()=>{$Pt(),$Pt(),Zle(),je(),eFt={$style:Lc},tFt=Ae(QPt,[[`__cssModules`,eFt]])})),rFt,iFt=r((()=>{nFt(),Sh(),rFt=_({__name:`cc-user-username`,props:{clickBehavior:{},customUrl:{},username:{},variant:{default:`boldest`},size:{default:``}},emits:[`log-action`],setup(e){let t=e,{routes:n}=
```

<a id="FND-30362"></a>
## FND-30362 — Implementation component cc-user-username

Vue compiled component __name declaration. Name suggests cc user username; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1137
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
=r((()=>{$Pt(),$Pt(),Zle(),je(),eFt={$style:Lc},tFt=Ae(QPt,[[`__cssModules`,eFt]])})),rFt,iFt=r((()=>{nFt(),Sh(),rFt=_({__name:`cc-user-username`,props:{clickBehavior:{},customUrl:{},username:{},variant:{default:`boldest`},size:{default:``}},emits:[`log-action`],setup(e){let t=e,{routes:n}=bh(),r=c(()=>t.customUrl||n.webMemberView(t.username));return(t,n)=>(k(),u(tFt,T(t.$attrs,{"click-behavior":e.clickBehavior,"custom-url":e.customUrl,username:e.username,variant:e.variant,size:e.size,"user-profile-url":r.value,onLogAction:n[0]||=e=>t.$emit(`log-action`,e)}),null,16,[`click-behavior`,`custom-url`,`username`,`variant`,`size`,`user-profile-url`]))}})})),A5,j5=r((()=>{iFt(),iFt(),A5=rFt})),aFt,oFt=r((()=>{GW(),T5(),SPt(),Sh(),kPt(),jPt(),zPt(),UPt(),ZPt(),j5(),aFt=_({__name:`cc-user-block`,props:{country:{},customUrl:{},flair:{},hideStrategy:{default:`default`},membership:{default:HW.basic},rating:{},clickBehavior:{default:`openProfile`},showPremiumBadge:{type:Boolean,default:!0},size:{default:`small`},title:{},tooltipPosition:{},username:{default:``},variant:{default:`default`}},emits:[`log-action`],setup(e){let t=e,{features:n,shouldShowMembershipBadges:r}=bh(),i=xe(`root`),a=c(()=>t.membership??HW.bas
```

<a id="FND-30363"></a>
## FND-30363 — Implementation component cc-user-block

Vue compiled component __name declaration. Name suggests cc user block; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1137
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
)})),A5,j5=r((()=>{iFt(),iFt(),A5=rFt})),aFt,oFt=r((()=>{GW(),T5(),SPt(),Sh(),kPt(),jPt(),zPt(),UPt(),ZPt(),j5(),aFt=_({__name:`cc-user-block`,props:{country:{},customUrl:{},flair:{},hideStrategy:{default:`default`},membership:{default:HW.basic},rating:{},clickBehavior:{default:`openProfile`},showPremiumBadge:{type:Boolean,default:!0},size:{default:`small`},title:{},tooltipPosition:{},username:{default:``},variant:{default:`default`}},emits:[`log-action`],setup(e){let t=e,{features:n,shouldShowMembershipBadges:r}=bh(),i=xe(`root`),a=c(()=>t.membership??HW.basic);DPt({isEnabled:()=>n.includes(`premium_badge_redesign`),membership:()=>a.value,root:i,strategy:()=>t.hideStrategy});let o=c(()=>t.showPremiumBadge&&APt({hasTitle:!!t.title,isPremiumBadgeRedesign:n.includes(`premium_badge_redesign`),membership:a.value,showMembershipBadges:r()}));return(t,r)=>(k(),f(`div`,{ref_key:`root`,ref:i,class:D([`cc-user-block-component`,`cc-user-block-${e.variant}`,`cc-user-block-${e.size}`,{"cc-user-block-premium-badge-redesign":ve(n).includes(`premium_badge_redesign`)}])},[e.title?(k(),u(k5,{key:0,"is-clickable":e.clickBehavior!==`none`&&e.clickBehavior!==`badgeAsLink`,size:e.size,title:e.title,"tooltip-position":e.too
```

<a id="FND-30364"></a>
## FND-30364 — Implementation component cc-user-block-with-popover

Vue compiled component __name declaration. Name suggests cc user block with popover; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1137
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
T`,`POST`],schemes:[`https`]}})})),wRt,TRt=r((()=>{GW(),T5(),CRt(),SPt(),Sh(),kPt(),jPt(),zPt(),UPt(),ZPt(),j5(),wRt=_({__name:`cc-user-block-with-popover`,props:{country:{},customUrl:{},flair:{},hideStrategy:{default:`default`},membership:{default:HW.basic},rating:{},ratingType:{},clickBehavior:{default:`openProfile`},hasUserPopover:{type:Boolean,default:!0},userPopoverLocation:{},showPremiumBadge:{type:Boolean,default:!0},size:{default:`small`},title:{},tooltipPosition:{},username:{default:``},variant:{default:`default`}},emits:[`log-action`],setup(e){let t=e,{features:n,currentRoute:r}=bh(),i=xe(`root`),a=c(()=>t.userPopoverLocation||r()),o=c(()=>t.membership??HW.basic);DPt({isEnabled:()=>n.includes(`premium_badge_redesign`),membership:()=>o.value,root:i,strategy:()=>t.hideStrategy});let s=se(!1);ne(()=>{s.value=window.chesscom?.settings?.[`gameplay.show_membership_badges`]!==!1});let l=c(()=>t.showPremiumBadge&&APt({hasTitle:!!t.title,isPremiumBadgeRedesign:n.includes(`premium_badge_redesign`),membership:o.value,showMembershipBadges:s.value}));function p(e){t.hasUserPopover&&window.chesscom.analysis?.gameType!==`coach`&&window.chesscom.analysis?.gameType!==`computer`&&SRt({user:{username:t.usernam
```

<a id="FND-30365"></a>
## FND-30365 — Implementation component player

Vue compiled component __name declaration. Name suggests player; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1137
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
ORt,kRt=r((()=>{iD(),WNt(),ePt(),S5(),sFt(),ERt(),Hd(),oM(),f7(),bm(),Sm(),vfe(),DRt=[`board-id`,`player-color`],ORt=_({__name:`player`,props:{boardId:{},color:{},gameType:{},position:{},player:{},time:{},timeClass:{},turn:{}},emits:[`click-user`],setup(e){let t=e,n=c(()=>({content:t.player.username,position:t.position===d7.Positions.Top?`bottom`:`top`})),r=c(()=>xm(t.player)),i=c(()=>t.gameType===aM.GameTypes.VsCoach||t.gameType===aM.GameTypes.VsComputer),a=c(()=>t.player.isCoach||t.player.isComputer),o=c(()=>!(i.value&&a.value)),s=c(()=>r.value?u7:M5),l=c(()=>i.value&&!a.value?null:ym(t.player)),g=c(()=>t.player.title),_=c(()=>t.time===void 0?void 0:Vd(t.time)),v=c(()=>t.turn===t.color),y=c(()=>t.color===G.ColorsAsNumbers.White?`light`:`dark`);return(t,i)=>(k(),f(`div`,{class:D([t.$style.component,t.$style[e.position]])},[h(b5,{size:40,class:D(t.$style.avatar),src:e.player.getAvatar(),username:e.player.name},null,8,[`class`,`src`,`username`]),i[1]||=m(),h(x5,{"for-previous-element":``,position:n.value.position,text:n.value.content},null,8,[`position`,`text`]),i[2]||=m(),p(`div`,{class:D(t.$style.tagline)},[(k(),u(de(s.value),{variant:`boldest`,"user-popover-location":`analysis`,"click-behavior":r.va
```

<a id="FND-30366"></a>
## FND-30366 — Implementation component player

Vue compiled component __name declaration. Name suggests player; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1137
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
>{iD(),pNt(),N8(),vp(),yNt(),MRt(),O3(),Oq(),LW(),PRt(),IRt(),O_t(),kW(),RRt(),f7(),tG(),zRt=_({name:`PlayerController`,__name:`player`,props:{position:{default:d7.Positions.Bottom}},setup(e){let t=e,n=c(()=>D3().isFlipped?t.position===d7.Positions.Bottom?G.ColorsAsNumbers.Black:G.ColorsAsNumbers.White:t.position===d7.Positions.Bottom?G.ColorsAsNumbers.White:G.ColorsAsNumbers.Black),r=c(()=>n.value===G.ColorsAsNumbers.White?eG.white:eG.black),i=c(()=>OW.turn),a=c(()=>{if(!LRt())return;if(Kkt(OW.headers.Termination)&&OW.isOver&&OW.ids.line===0&&D_t()!==n.value)return 0;if(qkt(OW.headers.Termination)&&OW.isOver&&OW.ids.line===0){let e=OW.nodes[OW.nodes.length-1];if(e&&e.color!==n.value)return 0}let e=FRt(),t=NRt();if(!t)return e;let r=t.color===n.value?t.ids.move:t.ids.move-1;if(r<0)return e;let i=OW.nodes[r];return i?i.time:e}),o=c(()=>vNt(_p(OW.headers.TimeControl||0))),s=c(()=>Dq().isInitialized),l=fNt(),f=c(()=>IW());return(t,c)=>s.value?(k(),u(jRt,{key:0,"board-id":ve(l),color:n.value,"game-type":f.value,player:r.value,position:e.position,time:a.value,"time-class":o.value,turn:i.value},null,8,[`board-id`,`color`,`game-type`,`player`,`position`,`time`,`time-class`,`turn`])):d(``,!0)}})})),p7,VRt=r((
```

<a id="FND-30367"></a>
## FND-30367 — Implementation component player-bottom

Vue compiled component __name declaration. Name suggests player bottom; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1137
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
])):d(``,!0)}})})),p7,VRt=r((()=>{BRt(),BRt(),p7=zRt})),HRt,URt=r((()=>{VRt(),f7(),HRt=_({name:`PlayerBottomController`,__name:`player-bottom`,props:{position:{default:d7.Positions.Bottom}},setup(e){return(t,n)=>(k(),u(p7,{position:e.position},null,8,[`position`]))}})})),WRt,GRt=r((()=>{URt(),URt(),WRt=HRt})),KRt,qRt=r((()=>{VRt(),f7(),KRt=_({name:`PlayerTopController`,__name:`player-top`,props:{position:{default:d7.Positions.Top}},setup(e){return(t,n)=>(k(),u(p7,{position:e.position},null,8,[`position`]))}})})),JRt,YRt=r((()=>{qRt(),qRt(),JRt=KRt}));function XRt(){let{state:e}=a8;return e.matches(`animatingSkillPoint`)&&!e.matches({animatingSkillPoint:{progressRow:`pending`}})||e.matches(`awaitingClaimResponse`)||e.matches(`resolvingBoardOverlay`)||e.matches(`showingFirstTimeCelebration`)||e.matches(`showingSkillMasteredCelebration`)||e.matches(`showingSkillsUnlockedCelebration`)||e.matches(`showingSkillDefinitionModal`)||e.matches(`showingSkillsCompletedCelebration`)}var ZRt=r((()=>{o8()})),m7=a(((e,t)=>{(function(n,r){typeof e==`object`&&typeof t==`object`?t.exports=r():typeof define==`function`&&define.amd?define([],r):typeof e==`object`?e.rive=r():n.rive=r()})(e,()=>(()=>{var e=[,((e,t,n)=>{n.r(t
```

<a id="FND-30368"></a>
## FND-30368 — Implementation component player-top

Vue compiled component __name declaration. Name suggests player top; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1137
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
`position`]))}})})),WRt,GRt=r((()=>{URt(),URt(),WRt=HRt})),KRt,qRt=r((()=>{VRt(),f7(),KRt=_({name:`PlayerTopController`,__name:`player-top`,props:{position:{default:d7.Positions.Top}},setup(e){return(t,n)=>(k(),u(p7,{position:e.position},null,8,[`position`]))}})})),JRt,YRt=r((()=>{qRt(),qRt(),JRt=KRt}));function XRt(){let{state:e}=a8;return e.matches(`animatingSkillPoint`)&&!e.matches({animatingSkillPoint:{progressRow:`pending`}})||e.matches(`awaitingClaimResponse`)||e.matches(`resolvingBoardOverlay`)||e.matches(`showingFirstTimeCelebration`)||e.matches(`showingSkillMasteredCelebration`)||e.matches(`showingSkillsUnlockedCelebration`)||e.matches(`showingSkillDefinitionModal`)||e.matches(`showingSkillsCompletedCelebration`)}var ZRt=r((()=>{o8()})),m7=a(((e,t)=>{(function(n,r){typeof e==`object`&&typeof t==`object`?t.exports=r():typeof define==`function`&&define.amd?define([],r):typeof e==`object`?e.rive=r():n.rive=r()})(e,()=>(()=>{var e=[,((e,t,n)=>{n.r(t),n.d(t,{Animation:()=>r.Animation});var r=n(2)}),((e,t,n)=>{n.r(t),n.d(t,{Animation:()=>r});var r=function(){function e(e,t,n,r){this.animation=e,this.artboard=t,this.playing=r,this.loopCount=0,this.scrubTo=null,this.instance=new n.LinearAnimationInst
```

<a id="FND-30369"></a>
## FND-30369 — Implementation component raw-rive-file

Vue compiled component __name declaration. Name suggests raw rive file; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1137
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
t t.arrayBuffer())}var h7,rzt=r((()=>{h7=tzt()})),g7,izt,azt,ozt=r((()=>{$Rt(),g7=m7(),izt=tzt(),rzt(),dd(),ph(),azt=_({__name:`raw-rive-file`,props:{src:{}},emits:[`load`,`error`],setup(e,{emit:t}){typeof window<`u`&&!window.Buffer&&(window.Buffer=izt.Buffer);let n=e,r=t,i=me(),a=e=>{let t;t=e instanceof Error?e:e.type===g7.EventType.LoadError?Error(e.data?.toString()??`RiveFile load error`):Error(`RiveFile load error`),window.chesscom.features.includes(`web_rive_error_reporting`)&&fh(t,{extra:{component:`raw-rive-file`,srcType:typeof n.src,srcLength:typeof n.src==`string`?n.src.length??-1:-1}}),r(`error`,t)},o=()=>{},s=se(o),c=Symbol(`non-string-src`),l=()=>{let{src:e}=n;return e?typeof e==`string`?e:c:null},u=async(e,t)=>{try{let n=await nzt(e);if(l()!==t)return;let c=new g7.RiveFile({buffer:ud(n)??void 0,onLoad:e=>{e.type!==g7.EventType.Load||!(e.data instanceof g7.RiveFile)||l()===t&&(i.value=e.data,r(`load`,e.data))},onLoadError:a});s.value=()=>{c.cleanup(),i.value=void 0},c.cleanup=o,await c.init()}catch(e){let t=e instanceof Error?e:Error(`raw-rive-file: load: Unknown error`);a(t)}},d=()=>{s.value(),s.value=o,i.value=void 0};return ne(()=>{let{src:e}=n;e&&u(e,l())}),Se(l,e=>{let{src:t}=n;t?u(t
```

<a id="FND-30370"></a>
## FND-30370 — Implementation component unsafe-rive-file

Vue compiled component __name declaration. Name suggests unsafe rive file; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1137
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
7=azt})),v7,y7,czt=r((()=>{v7=Symbol(`rive-file`),y7=Symbol(`rive-file-expected`)})),lzt,uzt=r((()=>{szt(),czt(),lzt=_({__name:`unsafe-rive-file`,props:{src:{}},emits:[`load`,`error`],setup(e,{emit:t}){let n=e,r=t,i=me();oe(v7,i),oe(y7,c(()=>!!n.src)),Se(()=>n.src,e=>{e||(i.value=void 0)});let a=e=>{i.value=e,r(`load`,e)},o=e=>{r(`error`,e)};return(t,n)=>(k(),u(_7,{src:e.src,onLoad:a,onError:o},{default:Ce(()=>[ue(t.$slots,`default`)]),_:3},8,[`src`]))}})})),dzt,fzt=r((()=>{uzt(),uzt(),dzt=lzt}));function pzt(e){let{emptyOption:t,multiple:n=!1,options:r,placeholderText:i,select:a,valueKey:o}=e;if(!a)return n?[]:``;let s=0;i&&(s+=1),t&&(s+=1);let c=(e,t)=>{let n=r[e];return n?n[o]:t};return n?[...a.selectedOptions].map(e=>{let t=[...a.options].indexOf(e)-s;return c(t,e.value)}):c(a.selectedIndex-s,a.value||``)}function mzt(e,t){return e===t||Number.isNaN(e)&&Number.isNaN(t)?!0:!!(e&&t&&typeof e==`object`&&typeof t==`object`&&Object.keys(e).length===Object.keys(t).length&&Object.entries(e).every(([e,n])=>mzt(n,t[e])))}var hzt,gzt,_zt,vzt,yzt,bzt=r((()=>{Ka(),hzt=[`disabled`,`multiple`],gzt=[`selected`],_zt=[`selected`],vzt=[`disabled`,`hidden`,`selected`,`value`],yzt=Ga(_({__name:`cc-select`,props:{disa
```

<a id="FND-30371"></a>
## FND-30371 — Implementation component cc-select

Vue compiled component __name declaration. Name suggests cc select; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1137
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
(),hzt=[`disabled`,`multiple`],gzt=[`selected`],_zt=[`selected`],vzt=[`disabled`,`hidden`,`selected`,`value`],yzt=Ga(_({__name:`cc-select`,props:{disabled:{type:Boolean,default:!1},emptyOption:{default:``},hasError:{type:Boolean,default:!1},labelKey:{default:`label`},modelValue:{},multiple:{type:Boolean,default:!1},options:{},placeholderText:{default:``},size:{default:`medium`},valueKey:{default:`value`}},emits:[`update:modelValue`],setup(e,{emit:t}){let n=e,r=t,i=xe(`selectElement`),a=c(()=>n.modelValue??``),o=c(()=>a.value===null||a.value===``);function l(e){return e[n.valueKey]}function u(e){return n.multiple?Array.isArray(a.value)?a.value.includes(l(e)):Object.values(a.value).includes(l(e)):mzt(l(e),a.value)}function p(){r(`update:modelValue`,pzt({emptyOption:n.emptyOption,multiple:n.multiple,options:n.options,placeholderText:n.placeholderText,select:i.value,valueKey:n.valueKey}))}return(t,n)=>(k(),f(`select`,{ref:`selectElement`,class:D([t.$style[`cc-select-component`],t.$style[`cc-select-${e.size}`],{[t.$style[`cc-select-error`]]:e.hasError}]),disabled:e.disabled,multiple:e.multiple,onChange:p},[e.placeholderText?(k(),f(`option`,{key:0,disabled:``,hidden:``,value:``,selected:o.value},he(e.placeh
```

<a id="FND-30372"></a>
## FND-30372 — Implementation component cc-select-legacy

Vue compiled component __name declaration. Name suggests cc select legacy; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1137
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
led`],Czt=[`selected`,`textContent`],wzt=[`selected`,`textContent`],Tzt=[`disabled`,`hidden`,`selected`,`value`],Ezt=_({__name:`cc-select-legacy`,props:{emptyOption:{default:``},hasError:{type:Boolean,default:!1},labelKey:{default:`label`},options:{},placeholderText:{default:``},size:{default:`medium`},modelValue:{default:``},valueKey:{default:`value`},multiple:{type:Boolean,default:!1},disabled:{type:Boolean,default:!1}},emits:[`update:modelValue`],setup(e,{emit:t}){let n=e,r=t,i=xe(`select-element`),{features:a}=bh(),o=a.includes(`cc_select_preserve_types`);function c(){r(`update:modelValue`,p())}function l(e){return e[n.valueKey]}function u(e){return n.multiple?Object.values(n.modelValue).includes(l(e)):Hf(l(e),n.modelValue)}function p(){if(o){let e=i.value;return Wle({select:e,options:n.options,valueKey:n.valueKey,placeholderText:n.placeholderText,emptyOption:n.emptyOption,multiple:n.multiple})}return n.multiple?Array.from(i.value?.selectedOptions??[]).map(e=>e.value):i.value?.value||``}return(t,n)=>(k(),f(`select`,{ref:`select-element`,class:D([`cc-select-component`,{[`cc-select-${e.size}`]:e.size,"cc-select-error":e.hasError}]),multiple:e.multiple,disabled:e.disabled,onChange:n[0]||=e=>c()},[e.p
```

<a id="FND-30373"></a>
## FND-30373 — Implementation component cc-select

Vue compiled component __name declaration. Name suggests cc select; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1137
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
)),128))],42,Szt))}})})),Ozt,kzt=r((()=>{Dzt(),Dzt(),Ozt=Ezt})),Azt,jzt=r((()=>{xzt(),Sh(),kzt(),Azt=_({inheritAttrs:!1,__name:`cc-select`,props:{multiple:{type:Boolean}},emits:[`update:modelValue`],setup(e,{emit:t}){let n=ye(),r=e,i=t,a=bh({optional:!0}),o=a?.features.includes(`design_system_component_migration_cc_select`)??!1,s=a?.features.includes(`cc_select_preserve_types`)??!1;function c(e){if(s){i(`update:modelValue`,e);return}let t=e=>e==null?``:String(e),n=r.multiple&&Array.isArray(e)?e.map(t):t(e);i(`update:modelValue`,n)}return(t,r)=>ve(o)?(k(),u(ve(yzt),T({key:0},ve(n),{multiple:e.multiple,"onUpdate:modelValue":c}),null,16,[`multiple`])):(k(),u(Ozt,T({key:1},ve(n),{multiple:e.multiple,"onUpdate:modelValue":r[0]||=e=>t.$emit(`update:modelValue`,e)}),null,16,[`multiple`]))}})})),Mzt,Nzt=r((()=>{jzt(),jzt(),Mzt=Azt})),Pzt,b7,Fzt=r((()=>{_5(),Ka(),Pzt=[`aria-label`],b7=Ga(_({__name:`cc-close-button`,props:{ariaLabel:{default:`Close`},size:{default:`large`},variant:{default:`subtle`}},emits:[`click`,`contextmenu`,`touchend`,`touchstart`],setup(e){let t=e,n=c(()=>t.size===`small`?12:16);return(t,r)=>(k(),f(`button`,{type:`button`,"aria-label":e.ariaLabel,class:D([t.$style[`cc-close-button-compone
```

<a id="FND-30374"></a>
## FND-30374 — Implementation component cc-close-button

Vue compiled component __name declaration. Name suggests cc close button; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1137
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
16,[`multiple`]))}})})),Mzt,Nzt=r((()=>{jzt(),jzt(),Mzt=Azt})),Pzt,b7,Fzt=r((()=>{_5(),Ka(),Pzt=[`aria-label`],b7=Ga(_({__name:`cc-close-button`,props:{ariaLabel:{default:`Close`},size:{default:`large`},variant:{default:`subtle`}},emits:[`click`,`contextmenu`,`touchend`,`touchstart`],setup(e){let t=e,n=c(()=>t.size===`small`?12:16);return(t,r)=>(k(),f(`button`,{type:`button`,"aria-label":e.ariaLabel,class:D([t.$style[`cc-close-button-component`],t.$style[`cc-close-button-${e.size}`],t.$style[`cc-close-button-${e.variant}`]]),onClick:r[0]||=e=>t.$emit(`click`,e),onContextmenu:r[1]||=e=>t.$emit(`contextmenu`,e),onTouchend:r[2]||=e=>t.$emit(`touchend`,e),onTouchstart:r[3]||=e=>t.$emit(`touchstart`,e)},[p(`div`,{class:D(t.$style[`cc-close-button-bg`])},null,2),h(g5,{name:`mark-cross`,variant:`glyph`,class:D(t.$style[`cc-close-button-icon`]),size:n.value},null,8,[`class`,`size`])],42,Pzt))}}),[[`__cssModules`,{$style:{"cc-close-button-component":`cc-close-button-component_5ce8bfe`,"cc-close-button-bg":`cc-close-button-bg_5ce8bfe`,"cc-close-button-icon":`cc-close-button-icon_5ce8bfe`,"cc-close-button-opaque":`cc-close-button-opaque_5ce8bfe`,"cc-close-button-default":`cc-close-button-default_5ce8bfe`,"cc-clo
```

<a id="FND-30375"></a>
## FND-30375 — Implementation component cc-close-button

Vue compiled component __name declaration. Name suggests cc close button; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1137
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
)})),Izt=r((()=>{qa(),Hoe(),Fzt()})),Lzt,Rzt,zzt=r((()=>{Izt(),oW(),y5(),Sh(),Lzt=[`aria-label`],Rzt=_({inheritAttrs:!1,__name:`cc-close-button`,props:{size:{default:`large`},variant:{default:`subtle`}},emits:[`click`,`contextmenu`,`touchend`,`touchstart`],setup(e){let t=bh({optional:!0}),n=t?.trans,r=t?.features.includes(`design_system_component_migration_cc_close_button`)??!1,i=e,a=c(()=>i.size===`small`?12:16);return(t,i)=>ve(r)?(k(),u(ve(b7),T({key:0,"aria-label":ve(n)?.Close,class:`cc-close-button-component`},t.$attrs,{size:e.size,variant:e.variant,onClick:i[0]||=e=>t.$emit(`click`,e),onContextmenu:i[1]||=e=>t.$emit(`contextmenu`,e),onTouchend:i[2]||=e=>t.$emit(`touchend`,e),onTouchstart:i[3]||=e=>t.$emit(`touchstart`,e)}),null,16,[`aria-label`,`size`,`variant`])):(k(),f(`button`,T({key:1,"aria-label":ve(n)?.Close??`Close`,class:[`cc-close-button-component`,`cc-close-button-${e.size}`,`cc-close-button-${e.variant}`,`cc-transition-color-hover`]},t.$attrs,{onClick:i[4]||=e=>t.$emit(`click`,e),onContextmenu:i[5]||=e=>t.$emit(`contextmenu`,e),onTouchend:i[6]||=e=>t.$emit(`touchend`,e),onTouchstart:i[7]||=e=>t.$emit(`touchstart`,e)}),[p(`div`,{class:D(t.$style.bg)},null,2),i[8]||=m(),h(v5,{class:`cc-c
```

<a id="FND-30376"></a>
## FND-30376 — Implementation component game-collection-thumbnail

Vue compiled component __name declaration. Name suggests game collection thumbnail; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1137
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
urn t>1?Ff(n,t):n}var Gzt=r((()=>{Zq(),Lf()})),Kzt,qzt,Jzt=r((()=>{Zq(),Gzt(),Kzt=[`height`,`width`,`alt`,`src`],qzt=_({__name:`game-collection-thumbnail`,props:{collection:{},size:{default:24}},setup(e){let t=e,n=c(()=>t.collection.customThumbnailUrl?t.collection.customThumbnailUrl:t.collection.thumbnail?Wzt(t.collection.thumbnail):Jq.PLACEHOLDER_IMG);return(t,r)=>(k(),f(`img`,{height:e.size,width:e.size,alt:e.collection.name,class:D(t.$style.component),src:n.value},null,10,Kzt))}})})),Yzt,Xzt,Zzt=r((()=>{Jzt(),Jzt(),Ple(),je(),Yzt={$style:bo},Xzt=Ae(qzt,[[`__cssModules`,Yzt]])})),Qzt,$zt=r((()=>{Qzt=_({__name:`loader-three-bounce`,props:{isCircle:{type:Boolean,default:!1},size:{default:80}},setup(e){let t=e,n=c(()=>{let e=`${t.size*.25}px`;return{width:e,height:e}});return(t,r)=>(k(),f(`div`,{class:D([t.$style.component,{[t.$style.circle]:e.isCircle}]),style:ee({width:`${e.size*.75+20}px`}),"data-test-element":`loader-three-bounce`},[p(`div`,{class:D([t.$style.dot,t.$style.bounce1]),style:ee(n.value)},null,6),r[0]||=m(),p(`div`,{class:D([t.$style.dot,t.$style.bounce2]),style:ee(n.value)},null,6),r[1]||=m(),p(`div`,{class:D(t.$style.dot),style:ee(n.value)},null,6)],6))}})})),eBt,tBt,nBt=r((()=>{$zt()
```

<a id="FND-30377"></a>
## FND-30377 — Implementation component loader-three-bounce

Vue compiled component __name declaration. Name suggests loader three bounce; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1137
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
Yzt,Xzt,Zzt=r((()=>{Jzt(),Jzt(),Ple(),je(),Yzt={$style:bo},Xzt=Ae(qzt,[[`__cssModules`,Yzt]])})),Qzt,$zt=r((()=>{Qzt=_({__name:`loader-three-bounce`,props:{isCircle:{type:Boolean,default:!1},size:{default:80}},setup(e){let t=e,n=c(()=>{let e=`${t.size*.25}px`;return{width:e,height:e}});return(t,r)=>(k(),f(`div`,{class:D([t.$style.component,{[t.$style.circle]:e.isCircle}]),style:ee({width:`${e.size*.75+20}px`}),"data-test-element":`loader-three-bounce`},[p(`div`,{class:D([t.$style.dot,t.$style.bounce1]),style:ee(n.value)},null,6),r[0]||=m(),p(`div`,{class:D([t.$style.dot,t.$style.bounce2]),style:ee(n.value)},null,6),r[1]||=m(),p(`div`,{class:D(t.$style.dot),style:ee(n.value)},null,6)],6))}})})),eBt,tBt,nBt=r((()=>{$zt(),$zt(),Ile(),je(),eBt={$style:hs},tBt=Ae(Qzt,[[`__cssModules`,eBt]])})),rBt,iBt=r((()=>{V(),rBt=Zg()}));function aBt(e){let t=oD();if(!t.activeMoveIds)return;let n=q4.getGameAPI(),{from:r,to:i}=df(e);if(t.hint===Yl.Arrow)return Y4();if(t.hint===Yl.Square)return a();return o();function a(){Y4(),t.hint=Yl.Arrow,n.markings.addOne({data:{color:Hl.arrow,opacity:.8,from:r,to:i},tags:[Ul],type:`arrow`})}function o(){t.hint=Yl.Square,n.markings.addOne({data:{color:Hl.square,opacity:.5,square:r},
```

<a id="FND-30378"></a>
## FND-30378 — Implementation component cc-loader

Vue compiled component __name declaration. Name suggests cc loader; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1137
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
anger`,e.Monetization=`monetization`,e.Primary=`primary`,e.Secondary=`secondary`,e}({})})),j7,bBt=r((()=>{Ka(),j7=Ga(_({__name:`cc-loader`,props:{size:{},variant:{default:`blocks`}},setup(e){return(t,n)=>e.variant===`blocks`?(k(),f(`div`,{key:0,"aria-busy":`true`,"aria-live":`polite`,class:D([t.$style[`cc-loader-component`],t.$style[`cc-loader-${e.size}`]])},[(k(),f(s,null,le(6,e=>p(`div`,{key:e,class:D([t.$style[`cc-loader-square`],t.$style[`cc-loader-square-${e}`]])},null,2)),64))],2)):(k(),f(`div`,{key:1,"aria-busy":`true`,"aria-live":`polite`,class:D([t.$style[`cc-loader-spinner`],t.$style[`cc-loader-${e.size}`],t.$style[`cc-loader-${e.variant}`]])},null,2))}}),[[`__cssModules`,{$style:{"cc-loader-component":`cc-loader-component_1e4c4f9`,"cc-loader-spinner":`cc-loader-spinner_1e4c4f9`,"cc-loader-spin":`cc-loader-spin_1e4c4f9`,"cc-loader-small":`cc-loader-small_1e4c4f9`,"cc-loader-medium":`cc-loader-medium_1e4c4f9`,"cc-loader-large":`cc-loader-large_1e4c4f9`,"cc-loader-spinner-green":`cc-loader-spinner-green_1e4c4f9`,"cc-loader-spinner-gray":`cc-loader-spinner-gray_1e4c4f9`,"cc-loader-spinner-chameleon":`cc-loader-spinner-chameleon_1e4c4f9`,"cc-loader-square":`cc-loader-square_1e4c4f9`,"cc-loader-s
```

<a id="FND-30379"></a>
## FND-30379 — Implementation component cc-button

Vue compiled component __name declaration. Name suggests cc button; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1137
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
rge`},"xx-large":{iconSize:32,imgSize:32,loaderSize:`large`}},xBt=[`height`,`src`,`width`],SBt=[`textContent`],N7=Ga(_({__name:`cc-button`,props:{align:{default:`center`},customClasses:{},customImgSrc:{},disabled:{type:Boolean},fullWidth:{type:Boolean},href:{},icon:{},isOneLineText:{type:Boolean},label:{},loading:{type:Boolean},minWidth:{type:Boolean},routerLink:{},selectedBorder:{type:Boolean},size:{default:`medium`},type:{default:`button`},variant:{default:`secondary`}},emits:[`click`,`contextmenu`,`touchend`,`touchstart`],setup(e){let t=e,n=c(()=>t.routerLink?`router-link`:t.href?`a`:`button`),r=c(()=>{if(n.value===`button`)return t.disabled||t.loading?!0:void 0}),i=c(()=>M7[t.size].iconSize),a=c(()=>M7[t.size].loaderSize);return(t,o)=>(k(),u(de(n.value),{class:D([t.$style[`cc-button-component`],t.$style[`cc-button-${e.variant}`],t.$style[`cc-button-${e.size}`],{[t.$style[`cc-button-full`]]:e.fullWidth,[t.$style[`cc-button-disabled`]]:e.disabled,[t.$style[`cc-button-loading`]]:e.loading,[t.$style[`cc-button-min-width`]]:e.minWidth,[t.$style[`cc-button-selected-border`]]:e.selectedBorder,[t.$style[`cc-button-align-start`]]:e.align===`start`}]),"data-align":e.align,"data-disabled":e.disabled?`true`:`
```

<a id="FND-30380"></a>
## FND-30380 — Implementation component cc-modal

Vue compiled component __name declaration. Name suggests cc modal; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1137
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
),Uoe(),Voe(),CBt()})),TBt,EBt=r((()=>{wBt(),TBt=N7})),P7,DBt=r((()=>{EBt(),EBt(),P7=TBt})),OBt,kBt=r((()=>{P$(),OBt=_({__name:`cc-modal`,props:{dismissable:{type:Boolean,default:!0},noCloseOnEscape:{type:Boolean,default:!1},modalWidth:{},isTransparent:{type:Boolean,default:!1},customClasses:{default:()=>({})},propagateKeys:{type:Boolean,default:!1}},emits:[`hide`],setup(e,{emit:t}){let n=e,r=()=>n.dismissable&&!n.noCloseOnEscape,i=t,a=xe(`dialogRef`),o=xe(`panelRef`);ne(()=>{a.value&&(a.value.showModal(),a.value.addEventListener(`cancel`,e=>{e.preventDefault()})),D$(window,`keydown`,e=>{e.key===`Escape`&&r()&&i(`hide`)})});function s(e){if(!n.dismissable)return;let t=o.value;t&&e.composedPath().includes(t)||i(`hide`)}function c(e){if(e.key===`Escape`){e.preventDefault(),e.stopPropagation(),e.type===`keydown`&&r()&&i(`hide`);return}n.propagateKeys||e.stopPropagation()}return(t,n)=>(k(),f(`dialog`,{ref_key:`dialogRef`,ref:a,class:D([t.$style.component,e.modalWidth&&t.$style[e.modalWidth],e.customClasses?.backdrop,{[t.$style[`bg-transparent`]]:e.isTransparent}]),onClick:s,onKeydown:c,onKeyup:c,onKeypress:c},[p(`div`,{ref_key:`panelRef`,ref:o,"data-ignore-close-board-modal":``,class:D([t.$style.dialog,e.
```

<a id="FND-30381"></a>
## FND-30381 — Implementation component cc-modal-close

Vue compiled component __name declaration. Name suggests cc modal close; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1137
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
F7,jBt=r((()=>{kBt(),kBt(),Hle(),je(),ABt={$style:$s},F7=Ae(OBt,[[`__cssModules`,ABt]])})),MBt,NBt=r((()=>{Vzt(),MBt=_({__name:`cc-modal-close`,props:{size:{default:`large`},variant:{default:`subtle`}},emits:[`close-modal`],setup(e){return(t,n)=>(k(),u(x7,{class:D(t.$style.component),size:e.size,variant:e.variant,onClick:n[0]||=e=>t.$emit(`close-modal`)},null,8,[`class`,`size`,`variant`]))}})})),PBt,I7,FBt=r((()=>{NBt(),NBt(),Ule(),je(),PBt={$style:tc},I7=Ae(MBt,[[`__cssModules`,PBt]])})),IBt,LBt,RBt,zBt=r((()=>{DBt(),jBt(),FBt(),IBt=[`textContent`],LBt=[`textContent`],RBt=_({__name:`cc-confirmation-modal`,props:{title:{},secondaryButtonProps:{},primaryButtonProps:{},description:{default:``},hideOnAction:{type:Boolean,default:!0},closeButtonVisible:{type:Boolean,default:!0},modalProps:{}},emits:[`show`,`hide`,`secondary-click`,`primary-click`],setup(e,{emit:t}){let n=e,r=t;ne(()=>{r(`show`)});function i(){r(`hide`)}function a(){n.hideOnAction&&r(`hide`),r(`secondary-click`)}function o(){n.hideOnAction&&r(`hide`),r(`primary-click`)}return(t,n)=>(k(),u(F7,T({"modal-width":`xs`},e.modalProps,{onHide:n[3]||=e=>i()}),{default:Ce(()=>[p(`div`,{class:D(t.$style.modal)},[e.closeButtonVisible?(k(),u(I7,{key:0,
```

<a id="FND-30382"></a>
## FND-30382 — Implementation component cc-confirmation-modal

Vue compiled component __name declaration. Name suggests cc confirmation modal; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1137
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
MBt,[[`__cssModules`,PBt]])})),IBt,LBt,RBt,zBt=r((()=>{DBt(),jBt(),FBt(),IBt=[`textContent`],LBt=[`textContent`],RBt=_({__name:`cc-confirmation-modal`,props:{title:{},secondaryButtonProps:{},primaryButtonProps:{},description:{default:``},hideOnAction:{type:Boolean,default:!0},closeButtonVisible:{type:Boolean,default:!0},modalProps:{}},emits:[`show`,`hide`,`secondary-click`,`primary-click`],setup(e,{emit:t}){let n=e,r=t;ne(()=>{r(`show`)});function i(){r(`hide`)}function a(){n.hideOnAction&&r(`hide`),r(`secondary-click`)}function o(){n.hideOnAction&&r(`hide`),r(`primary-click`)}return(t,n)=>(k(),u(F7,T({"modal-width":`xs`},e.modalProps,{onHide:n[3]||=e=>i()}),{default:Ce(()=>[p(`div`,{class:D(t.$style.modal)},[e.closeButtonVisible?(k(),u(I7,{key:0,onClick:n[0]||=e=>i()})):d(``,!0),n[6]||=m(),p(`div`,{class:D(t.$style.headings)},[e.title?(k(),f(`h2`,{key:0,class:D([`cc-heading-x-small`,`cc-text-wrap-pretty`,t.$style.title]),textContent:he(e.title)},null,10,IBt)):d(``,!0),n[4]||=m(),e.description?(k(),f(`div`,{key:1,class:D([`cc-text-large-bold`,t.$style.description]),textContent:he(e.description)},null,10,LBt)):d(``,!0)],2),n[7]||=m(),ue(t.$slots,`default`),n[8]||=m(),p(`div`,{class:D(t.$style.buttons)}
```

<a id="FND-30383"></a>
## FND-30383 — Implementation component cc-icon-button

Vue compiled component __name declaration. Name suggests cc icon button; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1137
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
t=r((()=>{zBt(),zBt(),Vle(),je(),BBt={$style:Bs},VBt=Ae(RBt,[[`__cssModules`,BBt]])})),UBt,WBt=r((()=>{y5(),S5(),UBt=_({__name:`cc-icon-button`,props:{customClasses:{},disabled:{type:Boolean},href:{},target:{},icon:{},iconSize:{default:20},size:{default:`small`},tooltip:{},variant:{default:`ghost`}},emits:[`click`,`contextmenu`,`touchend`,`touchstart`],setup(e){let t=e,n=c(()=>t.disabled||null),r=c(()=>typeof t.tooltip==`object`?t.tooltip:{text:t.tooltip,position:`top`,anchor:void 0,closeOnClick:void 0});return(t,i)=>(k(),u(de(e.href?`a`:`button`),{"aria-label":r.value.text,class:D([`cc-icon-button-component`,`cc-icon-button-${e.size}`,`cc-icon-button-${e.variant}`,`cc-bg-${e.variant}`,{"cc-icon-button-disabled":n.value&&e.href},e.customClasses?.container]),disabled:n.value,href:e.href||null,target:e.target||null,type:e.href?null:`button`,onClick:i[0]||=e=>t.$emit(`click`,e),onContextmenu:i[1]||=e=>t.$emit(`contextmenu`,e),onTouchend:i[2]||=e=>t.$emit(`touchend`,e),onTouchstart:i[3]||=e=>t.$emit(`touchstart`,e)},{default:Ce(()=>[e.tooltip?(k(),u(x5,{key:0,anchor:r.value.anchor,"close-on-click":r.value.closeOnClick,position:r.value.position,text:r.value.text},null,8,[`anchor`,`close-on-click`,`position
```

<a id="FND-30384"></a>
## FND-30384 — Implementation component cc-aside-item

Vue compiled component __name declaration. Name suggests cc aside item; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1137
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
get`,`type`]))}})})),GBt,KBt=r((()=>{WBt(),WBt(),GBt=UBt})),qBt,JBt,YBt=r((()=>{_5(),Ka(),qBt=[`textContent`],JBt=Ga(_({__name:`cc-aside-item`,props:{chevron:{},customClasses:{},href:{},icon:{},iconSize:{default:24},isClickable:{type:Boolean,default:!0},isDanger:{type:Boolean},isDisabled:{type:Boolean},isOneLineText:{type:Boolean},label:{},selected:{type:Boolean},selectedIcon:{type:Boolean,default:!1}},emits:[`click`],setup(e,{emit:t}){let n=e,r=t,i=c(()=>n.isClickable?n.href?`a`:`button`:`div`),a={up:`arrow-chevron-top`,right:`arrow-chevron-right`,down:`arrow-chevron-bottom`},o=c(()=>n.chevron?a[n.chevron]:void 0);function s(e){if(n.isDisabled){e.preventDefault();return}r(`click`,e)}return(t,n)=>(k(),u(de(i.value),{class:D([t.$style[`cc-aside-item-component`],{[t.$style[`cc-aside-item-selected`]]:e.selected,[t.$style[`cc-aside-item-danger`]]:e.isDanger}]),disabled:e.isClickable&&e.isDisabled?!0:void 0,href:e.isClickable&&e.href||void 0,type:e.isClickable&&!e.href?`button`:void 0,onClick:s},{default:Ce(()=>[e.icon?(k(),u(g5,{key:0,is:e.icon.is,class:D([t.$style[`cc-aside-item-icon`],e.customClasses?.icon]),name:e.icon.name,size:e.iconSize,variant:e.icon.variant},null,8,[`is`,`class`,`name`,`size`,`var
```

<a id="FND-30385"></a>
## FND-30385 — Implementation component cc-aside-item-legacy

Vue compiled component __name declaration. Name suggests cc aside item legacy; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1137
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
selected-icon_1d71ace`}}]])})),XBt=r((()=>{qa(),Boe(),YBt()})),ZBt,QBt,$Bt=r((()=>{oW(),y5(),ZBt=[`textContent`],QBt=_({__name:`cc-aside-item-legacy`,props:{chevron:{},customClasses:{},isDanger:{type:Boolean},iconSize:{default:24},icon:{},isDisabled:{type:Boolean},isOneLineText:{type:Boolean},href:{},isClickable:{type:Boolean,default:!0},label:{},selected:{type:Boolean},selectedIcon:{type:Boolean,default:!1}},emits:[`click`],setup(e,{emit:t}){let n=e,r={up:QJe,right:QU,down:RJe},i=t;function a(e){if(n.isDisabled){e.preventDefault();return}i(`click`,e)}return(t,n)=>(k(),u(de(e.isClickable?e.href?`a`:`button`:`div`),{class:D([`cc-aside-item-component`,{"cc-aside-item-selected":e.selected,"cc-aside-item-danger":e.isDanger,"cc-transition-bg-hover":e.isClickable}]),disabled:e.isClickable&&e.isDisabled||null,href:e.isClickable&&e.href||null,type:e.isClickable&&!e.href?`button`:null,onClick:a},{default:Ce(()=>[e.icon?(k(),u(v5,{key:0,class:D([`cc-aside-item-icon`,e.customClasses?.icon]),is:e.icon.is,name:e.icon.name,size:e.iconSize,variant:e.icon.variant},null,8,[`class`,`is`,`name`,`size`,`variant`])):d(``,!0),n[0]||=m(),p(`span`,{class:D([`cc-aside-item-label`,`cc-text-medium-bold`,e.customClasses?.label,{
```

<a id="FND-30386"></a>
## FND-30386 — Implementation component cc-aside-item

Vue compiled component __name declaration. Name suggests cc aside item; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1137
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
f`,`type`]))}})})),eVt,tVt=r((()=>{$Bt(),$Bt(),zle(),eVt=QBt})),nVt,rVt=r((()=>{XBt(),Sh(),tVt(),nVt=_({inheritAttrs:!1,__name:`cc-aside-item`,setup(e){let t=ye(),n=bh({optional:!0})?.features.includes(`design_system_component_migration_cc_aside_item`)??!1;return(e,r)=>ve(n)?(k(),u(ve(JBt),O(T({key:0},ve(t))),{default:Ce(()=>[ue(e.$slots,`default`)]),_:3},16)):(k(),u(eVt,O(T({key:1},ve(t))),{default:Ce(()=>[ue(e.$slots,`default`)]),_:3},16))}})})),iVt,aVt=r((()=>{rVt(),rVt(),iVt=nVt}));function oVt(e){cVt(),e&&lVt(uq.AddGamePreviewId)}function sVt(){cVt(),lVt(uq.Id)}function cVt(){let e=CU();Object.values(e.chessboards).forEach(e=>{e.game.plugins.remove(uVt)})}function lVt(e){let t=CU(),n=t.chessboards[e];!t.arrowKeysPlugin||!n||n.game.plugins.add(t.arrowKeysPlugin)}var uVt,dVt=r((()=>{iD(),wU(),dq(),uVt=x_.Plugin.Name}));function fVt(){let e=DU();WK.fen=e.game.getFEN(),WK.pgn=e.game.getPGN()}var pVt=r((()=>{OU(),GK()}));function mVt(){WK.setupBoardTab===HK.SetupPosition&&fVt(),d_t()}var hVt=r((()=>{UK(),pVt(),GK(),f_t()}));function gVt(e){Dq().activeChessboardId=e}var _Vt=r((()=>{Oq()}));function vVt(){eG.black=new ZW(G.ColorsAsNumbers.Black),eG.white=new ZW(G.ColorsAsNumbers.White)}var yVt=r((()=>{i
```

<a id="FND-30387"></a>
## FND-30387 — Implementation component shared-board-entry-state

Vue compiled component __name declaration. Name suggests shared board entry state; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1142
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
not contain a board yet.`)};default:return null}}var _e=t((()=>{te(),x(),ce(),p()})),W,G=t((()=>{x(),_e(),se(),k(),W=L({__name:`shared-board-entry-state`,props:{entryStatus:{},hasSharedBoard:{type:Boolean,default:!0},isActionPending:{type:Boolean,default:!1}},emits:[`primary-action`],setup(e,{emit:t}){let n=e,r=t,a=j(()=>ge(n.entryStatus??i.Idle,n.hasSharedBoard));return(t,n)=>a.value?(z(),P(`div`,{key:0,class:R(t.$style.component)},[F(A,{header:a.value.header,icon:a.value.icon,"icon-size":64,subheader:a.value.subheader},{default:V(()=>[a.value.button?(z(),M(ue,{key:0,disabled:e.isActionPending,label:a.value.button,loading:e.isActionPending,size:`medium`,variant:`secondary`,onClick:n[0]||=e=>r(`primary-action`)},null,8,[`disabled`,`label`,`loading`])):N(``,!0)]),_:1},8,[`header`,`icon`,`subheader`])],2)):N(``,!0)}})})),K,q,ve=t((()=>{G(),G(),he(),ne(),K={$style:U},q=s(W,[[`__cssModules`,K]])})),J,Y=t((()=>{(function(e){e.Controllers={Analysis:`Analysis`,Setup:`Setup`}})(J||={})})),X,ye=t((()=>{Y(),ae(),X={[J.Controllers.Analysis]:I({loader:()=>v(()=>e(()=>import(`./analysis.e3ec5995.CACK5xm3oi.chunk.js`),`./analysis.e3ec5995.CACK5xm3oi.chunk.js`).then(e=>(e.n(),e.t)),__vite__mapDeps([0,1,2,3,4,5,6,7,8
```

<a id="FND-30388"></a>
## FND-30388 — Implementation component tab-analysis

Vue compiled component __name declaration. Name suggests tab analysis; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1142
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
),oe(),ye(),Y(),O(),r(),Z=L({name:`AnalysisTabController`,components:{SidebarTabContent:T,SharedBoardEntryState:q,...X},__name:`tab-analysis`,setup(e){D(le.Events.Analysis);let t=B(!1);async function n(){if(!t.value){t.value=!0;try{u().entryStatus===i.Requesting&&await d()}catch(e){h(e instanceof Error?e:String(e)),re(f(`Unable to leave the Analysis Room`))}finally{g(),m(),t.value=!1}}}let r=j(()=>y.isLoaded?J.Controllers.Analysis:J.Controllers.Setup),a=j(()=>u().entryStatus),o=j(w);return(e,i)=>(z(),M(T,null,{default:V(()=>[o.value?(z(),M(q,{key:0,"entry-status":a.value,"is-action-pending":t.value,onPrimaryAction:n},null,8,[`entry-status`,`is-action-pending`])):(z(),M(me(r.value),{key:1}))]),_:1}))}})})),be=n({default:()=>$}),$,xe=t((()=>{Q(),Q(),$=Z}));export{be as n,xe as t};
```

<a id="FND-30389"></a>
## FND-30389 — Implementation component coach-settings-header

Vue compiled component __name declaration. Name suggests coach settings header; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1143
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
ORY:`move-promote-dark`,ADVANCED_STAT_TYPE_STRATEGY_CATEGORY:`piece-black-knight`}})),Hu,Uu=t((()=>{x(),Zt(),ai(),Hu=G({__name:`coach-settings-header`,props:{audioToggle:{}},emits:[`close`,`toggleAudio`],setup(e){let t=Lt();return(n,r)=>(q(),V(`div`,{class:K(n.$style.component)},[e.audioToggle?(q(),z(Rr,{key:0,size:`large`,"aria-label":n.$trans(`Toggle Coach Audio`),class:K(n.$style[`audio-toggle`]),disabled:e.audioToggle.isMutedByPlaySounds,icon:{is:e.audioToggle.isAudible?Z(Ie):Z($e),variant:`glyph`},"icon-size":16,tooltip:e.audioToggle.isMutedByPlaySounds?{text:Z(t),position:`bottom`,anchor:`left`}:void 0,onClick:r[0]||=e=>n.$emit(`toggleAudio`)},null,8,[`aria-label`,`class`,`disabled`,`icon`,`tooltip`])):B(``,!0),r[2]||=U(),H(`h2`,{class:K([`cc-heading-x-small-bold`,n.$style.title])},[Y(n.$slots,`default`)],2),r[3]||=U(),W(Rr,{size:`large`,"aria-label":n.$trans(`Close`),class:K(n.$style.close),icon:{is:Z(_e),variant:`glyph`},"icon-size":16,onClick:r[1]||=e=>n.$emit(`close`)},null,8,[`aria-label`,`class`,`icon`])],2))}})})),Wu,Gu,Ku=t((()=>{Uu(),Uu(),ps(),E(),Wu={$style:fs},Gu=w(Hu,[[`__cssModules`,Wu]])})),qu,Ju=t((()=>{Wn(),Ku(),Jn(),qu=G({__name:`coach-settings-content`,props:{audioToggle:{}},em
```

<a id="FND-30390"></a>
## FND-30390 — Implementation component coach-settings-content

Vue compiled component __name declaration. Name suggests coach settings content; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1143
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
Wu,Gu,Ku=t((()=>{Uu(),Uu(),ps(),E(),Wu={$style:fs},Gu=w(Hu,[[`__cssModules`,Wu]])})),qu,Ju=t((()=>{Wn(),Ku(),Jn(),qu=G({__name:`coach-settings-content`,props:{audioToggle:{}},emits:[`close`,`onChooseCoachClick`,`toggleAudio`],setup(e,{emit:t}){let n=t,r=J(!1),i=so(`scrollContainer`),{y:a}=Oi(i),o=R(()=>a.value>0);function s(){r.value=!0,n(`onChooseCoachClick`)}return(t,n)=>(q(),V(`div`,null,[W(Gu,{"audio-toggle":e.audioToggle,onClose:n[0]||=e=>t.$emit(`close`),onToggleAudio:n[1]||=e=>t.$emit(`toggleAudio`)},{default:$(()=>[U(X(t.$trans(`Choose Your Coach`)),1)]),_:1},8,[`audio-toggle`]),n[2]||=U(),Y(t.$slots,`coach-speech-tagline`),n[3]||=U(),H(`div`,{class:K([t.$style.wrapper,{[t.$style[`with-shadow`]]:o.value}])},[H(`div`,{class:K(t.$style.body),ref_key:`scrollContainer`,ref:i},[Y(t.$slots,`coach-selection-menu`)],2)],2),n[4]||=U(),H(`div`,{class:K(t.$style[`cta-button-container`])},[W(F,{class:K(t.$style[`cta-button`]),"full-width":``,size:`xx-large`,variant:`primary`,loading:r.value,label:t.$trans(`Choose Coach`),onClick:s},null,8,[`class`,`loading`,`label`])],2)]))}})})),Yu,Xu,Zu=t((()=>{Ju(),Ju(),ss(),E(),Yu={$style:os},Xu=w(qu,[[`__cssModules`,Yu]])})),Qu,$u=t((()=>{Zu(),Ur(),Qu=G({__name:`coac
```

<a id="FND-30391"></a>
## FND-30391 — Implementation component coach-settings-modal

Vue compiled component __name declaration. Name suggests coach settings modal; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1143
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
)})),Yu,Xu,Zu=t((()=>{Ju(),Ju(),ss(),E(),Yu={$style:os},Xu=w(qu,[[`__cssModules`,Yu]])})),Qu,$u=t((()=>{Zu(),Ur(),Qu=G({__name:`coach-settings-modal`,props:{audioToggle:{},selectedCoachId:{}},emits:[`close`,`onChooseCoachClick`,`toggleAudio`],setup(e,{emit:t}){let n=t;return(t,r)=>(q(),z(zn,{"modal-width":`sm`,onHide:r[3]||=e=>n(`close`)},{default:$(()=>[W(Xu,{"audio-toggle":e.audioToggle,onClose:r[0]||=e=>t.$emit(`close`),onOnChooseCoachClick:r[1]||=e=>t.$emit(`onChooseCoachClick`),onToggleAudio:r[2]||=e=>t.$emit(`toggleAudio`)},{"coach-speech-tagline":$(()=>[Y(t.$slots,`coach-speech-tagline`)]),"coach-selection-menu":$(()=>[Y(t.$slots,`coach-selection-menu`)]),_:3},8,[`audio-toggle`])]),_:3}))}})})),ed,td,nd=t((()=>{$u(),$u(),ys(),E(),ed={$style:vs},td=w(Qu,[[`__cssModules`,ed]])}));function rd(e={}){Ht.emit(Yt.CoachModalClose,{saved:e.saved===!0})}var id=t((()=>{ot(),It()}));async function ad(e,t){let n=k({preferPendingCoach:!0}),r=Be();if(!n||!r)return;let{textId:i,locale:a}=n;await t.loadAndSetCoach(e,{textAsset:{content:{case:`encryptedCompressedInBase64`,value:new TextEncoder().encode(r)},textId:i,locale:a}})}var od=t((()=>{Qt(),Ke()}));async function sd(){let e=k();if(!e)return;let{locale:t,te
```

<a id="FND-30392"></a>
## FND-30392 — Implementation component coach-selection-button

Vue compiled component __name declaration. Name suggests coach selection button; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1143
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
),Cd(),Ki(),Ne(),an(),se(),We(),Td(),Dd(),M()})),Ad,jd,Md,Nd=t((()=>{x(),rr(),Ad=[`alt`,`src`],jd=[`textContent`],Md=G({__name:`coach-selection-button`,props:{coach:{default:null},largeAvatars:{type:Boolean,default:!1},selected:{type:Boolean,default:!1},disabled:{type:Boolean,default:!1}},emits:[`click`],setup(e,{emit:t}){let n=e,r=t;function i(){n.disabled||r(`click`)}return(t,n)=>(q(),V(`div`,{class:K(t.$style.component)},[H(`button`,{type:`button`,class:K([t.$style.button,{[t.$style.large]:e.largeAvatars},{"cc-selected-border":e.selected},{[t.$style.none]:!e.coach}]),onClick:i},[e.coach?(q(),V(`img`,{key:0,height:`85`,width:`85`,alt:t.$trans(`coach`),class:K(t.$style.img),src:e.coach.imageUrl},null,10,Ad)):(q(),V(`div`,{key:1,class:K([t.$style.iconContainer,{[t.$style.iconContainerUnselected]:!e.selected}])},[W(p,{is:Z(_e),variant:`glyph`,size:40,class:K(t.$style.iconX)},null,8,[`is`,`class`])],2)),n[0]||=U(),e.coach?.i18nMeta?.languageIndicator?(q(),V(`div`,{key:2,class:K([t.$style.languageIndicator,`cc-text-x-small-bold`])},X(e.coach.i18nMeta.languageIndicator),3)):B(``,!0)],2),n[1]||=U(),H(`div`,{class:K([t.$style.label,{[t.$style.labelSelected]:e.selected}]),textContent:X(e.coach?.name??t.$tran
```

<a id="FND-30393"></a>
## FND-30393 — Implementation component coach-flat-selection-menu

Vue compiled component __name declaration. Name suggests coach flat selection menu; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1143
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
2))}})})),Pd,Fd,Id=t((()=>{Nd(),Nd(),ts(),E(),Pd={$style:es},Fd=w(Md,[[`__cssModules`,Pd]])})),Ld,Rd=t((()=>{Id(),Ld=G({__name:`coach-flat-selection-menu`,props:{coachesList:{},isLoading:{type:Boolean},selectedCoachId:{}},emits:[`set-coach`],setup(e){let t=e,n=J(null),r=e=>R(()=>!t.isLoading&&t.selectedCoachId===e);return ro(async()=>{await eo(),n.value&&Array.isArray(n.value)&&n.value[0].$el?.scrollIntoView({behavior:`smooth`,block:`center`,inline:`center`})}),(t,n)=>(q(),V(`div`,{class:K(t.$style.coaches)},[(q(!0),V(L,null,ao(e.coachesList,n=>(q(),z(Fd,{disabled:e.isLoading,key:n.id,ref_for:!0,ref:e.selectedCoachId===n.id?`selectedCoachEl`:void 0,selected:r(n.id).value,coach:n,onClick:e=>t.$emit(`set-coach`,{coachId:n.id})},null,8,[`disabled`,`selected`,`coach`,`onClick`]))),128))],2))}})})),zd,Bd,Vd=t((()=>{Rd(),Rd(),Ho(),E(),zd={$style:Vo},Bd=w(Ld,[[`__cssModules`,zd]])}));function Hd(){return o().state.status===Cr.Loading}var Ud=t((()=>{i(),ct()})),Wd,Gd=t((()=>{qi(),Vd(),Qt(),Ud(),Wd=G({__name:`coach-flat-selection-menu`,props:{coachesList:{}},emits:[`change`],setup(e,{emit:t}){let n=t,r=R(()=>Hd()),i=R(()=>k({preferPendingCoach:!0})?.id||null),a=async({coachId:e})=>{Wi(e)};return(t,o)=>(q(),z(B
```

<a id="FND-30394"></a>
## FND-30394 — Implementation component coach-flat-selection-menu

Vue compiled component __name declaration. Name suggests coach flat selection menu; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1143
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
);function Hd(){return o().state.status===Cr.Loading}var Ud=t((()=>{i(),ct()})),Wd,Gd=t((()=>{qi(),Vd(),Qt(),Ud(),Wd=G({__name:`coach-flat-selection-menu`,props:{coachesList:{}},emits:[`change`],setup(e,{emit:t}){let n=t,r=R(()=>Hd()),i=R(()=>k({preferPendingCoach:!0})?.id||null),a=async({coachId:e})=>{Wi(e)};return(t,o)=>(q(),z(Bd,{"coaches-list":e.coachesList,"is-loading":r.value,"selected-coach-id":i.value,onSetCoach:o[0]||=e=>n(`change`,a(e))},null,8,[`coaches-list`,`is-loading`,`selected-coach-id`]))}})})),Kd,qd=t((()=>{Gd(),Gd(),Kd=Wd}));function Jd(e,t){return q(),V(`div`,{class:K(e.$style[`speech-message`])},[Y(e.$slots,`coach-speech`)],2)}var Yd,Xd,Zd,Qd=t((()=>{Ss(),E(),Yd={},Xd={$style:xs},Zd=w(Yd,[[`render`,Jd],[`__cssModules`,Xd]])}));function $d(){return zt()&&!Fn().isGuest}var ef=t((()=>{mi(),Wt()})),tf,nf=t((()=>{Da(),va(),vf(),Qt(),ka(),ef(),Wa(),tf=G({__name:`coach-speech-single-message`,props:{animationKey:{},botAlign:{},coachSize:{},isCoachAvatarClickable:{type:Boolean,default:!0},isFullWidthMessage:{type:Boolean,default:!0},message:{},allowAnimationOverflowLeft:{type:Boolean},messageMaxWidth:{},preferPendingCoach:{type:Boolean,default:!1},shouldAutoResizeBotAvatar:{type:Boolean,de
```

<a id="FND-30395"></a>
## FND-30395 — Implementation component coach-speech-single-message

Vue compiled component __name declaration. Name suggests coach speech single message; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1143
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
tion $d(){return zt()&&!Fn().isGuest}var ef=t((()=>{mi(),Wt()})),tf,nf=t((()=>{Da(),va(),vf(),Qt(),ka(),ef(),Wa(),tf=G({__name:`coach-speech-single-message`,props:{animationKey:{},botAlign:{},coachSize:{},isCoachAvatarClickable:{type:Boolean,default:!0},isFullWidthMessage:{type:Boolean,default:!0},message:{},allowAnimationOverflowLeft:{type:Boolean},messageMaxWidth:{},preferPendingCoach:{type:Boolean,default:!1},shouldAutoResizeBotAvatar:{type:Boolean,default:xa.shouldAutoResizeBotAvatar},shouldShowBot:{type:Boolean,default:xa.shouldShowBot},shouldUseGameReviewHeight:{type:Boolean},showCoachNameTooltip:{type:Boolean,default:!0},speechBubbleMatchesCoachSize:{type:Boolean},startTypewriterAfterMount:{type:Boolean}},setup(e){let t=e,n=R(()=>k({preferPendingCoach:t.preferPendingCoach}));return(t,r)=>(q(),V(L,null,[W(Ra,{"allow-animation-overflow-left":e.allowAnimationOverflowLeft,"animation-key":e.animationKey,"bot-align":e.botAlign,"is-full-width-message":e.isFullWidthMessage,message:e.message,"message-max-width":e.messageMaxWidth,"bot-avatar":n.value?.imageUrl,"bot-name":n.value?.name,"bot-size":e.coachSize,"should-auto-resize-bot-avatar":e.shouldAutoResizeBotAvatar,"is-bot-avatar-clickable":Z($d)()&&e.i
```

<a id="FND-30396"></a>
## FND-30396 — Implementation component coach-speech-tagline

Vue compiled component __name declaration. Name suggests coach speech tagline; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1143
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
 cf(){return ci().pendingCoachMessage??``}var lf=t((()=>{kn()})),uf,df=t((()=>{Qd(),Ta(),af(),sf(),lf(),Qt(),ii(),uf=G({__name:`coach-speech-tagline`,props:{allowAnimationOverflowLeft:{type:Boolean},startTypewriterAfterMount:{type:Boolean}},setup(e){let t=R(()=>{let e=k({preferPendingCoach:!0});return e?.greetingRiveAnimationUrl||e?.riveAnimationUrl}),n=R(()=>cf()||(k({preferPendingCoach:!1})?.taglines?.[0]?.text??``)),{triggerCoachEmotion:r}=wa({event:{interface:`choose_your_coach`,preferPendingCoach:!0}});return Q(t,()=>r(`greeting`),{immediate:!0,flush:`post`}),(r,i)=>(q(),z(bn,{key:Z(of)()??t.value,src:t.value},{default:$(()=>[W(Zd,null,{"coach-speech":$(()=>[Z(k)()?(q(),z(rf,{key:0,"animation-key":n.value,"bot-align":`bottom`,"coach-size":96,"is-coach-avatar-clickable":!1,"allow-animation-overflow-left":e.allowAnimationOverflowLeft,message:n.value,"should-auto-resize-bot-avatar":!1,"start-typewriter-after-mount":e.startTypewriterAfterMount,"prefer-pending-coach":``},null,8,[`animation-key`,`allow-animation-overflow-left`,`message`,`start-typewriter-after-mount`])):B(``,!0)]),_:1})]),_:1},8,[`src`]))}})})),ff,pf=t((()=>{df(),df(),ff=uf})),mf,hf,gf=t((()=>{nd(),kd(),qd(),pf(),md(),Li(),mf={key:1},h
```

<a id="FND-30397"></a>
## FND-30397 — Implementation component coach-settings-modal

Vue compiled component __name declaration. Name suggests coach settings modal; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1143
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
_:1},8,[`src`]))}})})),ff,pf=t((()=>{df(),df(),ff=uf})),mf,hf,gf=t((()=>{nd(),kd(),qd(),pf(),md(),Li(),mf={key:1},hf=G({__name:`coach-settings-modal`,emits:[`change`],setup(e){let{audioToggle:t,coachesList:n,onChooseCoach:r,onClose:i,onToggleAudio:a}=Od();return(e,o)=>Z(_n)()?(q(),z(td,{key:0,"audio-toggle":Z(t),"selected-coach-id":Z(pd)(),onClose:Z(i),onOnChooseCoachClick:Z(r),onToggleAudio:Z(a)},{"coach-speech-tagline":$(()=>[W(ff,{"start-typewriter-after-mount":``})]),"coach-selection-menu":$(()=>[Z(n)?.length?(q(),z(Kd,{key:0,"coaches-list":Z(n),onChange:o[0]||=t=>e.$emit(`change`,t)},null,8,[`coaches-list`])):(q(),V(`div`,mf,X(e.$trans(`Loading coaches...`)),1))]),_:1},8,[`audio-toggle`,`selected-coach-id`,`onClose`,`onOnChooseCoachClick`,`onToggleAudio`])):B(``,!0)}})})),_f,vf=t((()=>{gf(),gf(),_f=hf})),yf,bf,xf,Sf,Cf,wf,Tf,Ef,Df,Of=t((()=>{Je(),x(),Jn(),rr(),Qi(),Ee(),Pr(),qe(),A(),na(),Ru(),window.chesscom=window.chesscom||{},window.chesscom.routes=window.chesscom.routes||{},Object.assign(window.chesscom.routes,{web_profile_view_stats:{tokens:[[`variable`,`/`,`bullet|blitz|rapid|chess|chess960|bughouse|threecheck|kingofthehill|openings|puzzles|tournaments|daily|daily960|live960|all-brilliant-m
```

<a id="FND-30398"></a>
## FND-30398 — Implementation component advanced-stats-report-card

Vue compiled component __name declaration. Name suggests advanced stats report card; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1143
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
ent`],xf=[`innerHTML`],Sf=[`textContent`],Cf=[`textContent`],wf=[`textContent`],Tf=[`innerHTML`],Ef=[`innerHTML`],Df=G({__name:`advanced-stats-report-card`,props:{isLoading:{type:Boolean},playerSide:{},report:{},timeControl:{}},emits:[`show-advanced-stats-upgrade-modal`],setup(e,{emit:t}){let n=ri(),r=!window.context.user?.isDiamond,i=t,a=e,o=de[Lu.MOVE_CLASSIFICATION_BRILLIANT].icon,s=[`Opening`,`Tactics`,`Strategy`,`Endgame`],c={Opening:()=>D(`Opening`),Tactics:()=>D(`Tactics`),Strategy:()=>D(`Strategy`),Endgame:()=>D(`Endgame`)};function l(e){return c[e]?.()??e}function u(e){if(e)return nt[e]?.icon??nt[Ue.Good].icon}function ee(e){return e?.length?e.filter(e=>typeof e==`object`&&!!e&&`category`in e&&`newRating`in e):[]}function d(e){return ee(e).map(e=>({label:e.category,classification:u(e.performance)??nt[Ue.Good].icon,new_rating:e.newRating,rating_change:e.ratingChange}))}function f(e){let t={};for(let n of ee(e))t[n.category]=u(n.performance);return t}let m=R(()=>{let e=a.report,t=d(e?.white?.categories),n=d(e?.black?.categories);return t.length&&n.length?[]:t.length&&a.playerSide===`white`?t:n.length&&a.playerSide===`black`?n:!a.isLoading||!a.playerSide?[]:s.map(e=>({label:e,classification:o,ne
```

<a id="FND-30399"></a>
## FND-30399 — Implementation component overview-avatar

Vue compiled component __name declaration. Name suggests overview avatar; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1143
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
f(),Of(),Js(),E(),kf={$style:qs},Af=w(Df,[[`__cssModules`,kf]])})),Mf,Nf,Pf=t((()=>{mn(),oe(),Mf=[`src`,`srcset`],Nf=G({__name:`overview-avatar`,props:{avatarUrl:{},isWinner:{type:Boolean}},setup(e){let t=e,n=Fi(`bundles/web/images/user-image.svg`),r=R(()=>t.avatarUrl?cr(t.avatarUrl):n);return(t,i)=>(q(),V(`div`,{class:K(t.$style.component)},[H(`img`,{class:K([t.$style.userAvatar,e.isWinner?t.$style.winner:``]),src:Z(n),srcset:r.value??``,width:`64`,height:`64`,alt:`avatar`},null,10,Mf)],2))}})})),Ff,If,Lf=t((()=>{Pf(),Pf(),Bc(),E(),Ff={$style:zc},If=w(Nf,[[`__cssModules`,Ff]])})),Rf,zf=t((()=>{Rf=function(e){return e.ClientSide=`?`,e.MissingValue=`-`,e}({})}));function Bf({digits:e=2,defaultVal:t=Rf.MissingValue,value:n}){return n?Ga({method:Math.floor,number:n}).toFixed(e)??t:t}var Vf=t((()=>{zf(),Ka()})),Hf,Uf,Wf,Gf=t((()=>{Ai(),Vf(),A(),Qs(),na(),Hf=[`innerHTML`],Uf=[`innerHTML`],Wf=G({__name:`report-card-legacy`,props:{isAnalysisRunning:{type:Boolean},reportCard:{}},setup(e){let t=e,n=R(()=>Ys(t.reportCard.white.data)),r=R(()=>Ys(t.reportCard.black.data)),i={gp0:{name:D(`Opening`),tooltip:D(`This is a grade for how well the player performed in the opening.`)},gp1:{name:D(`Middlegame`),tooltip:D(`
```

<a id="FND-30400"></a>
## FND-30400 — Implementation component report-card-legacy

Vue compiled component __name declaration. Name suggests report card legacy; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1143
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
e)??t:t}var Vf=t((()=>{zf(),Ka()})),Hf,Uf,Wf,Gf=t((()=>{Ai(),Vf(),A(),Qs(),na(),Hf=[`innerHTML`],Uf=[`innerHTML`],Wf=G({__name:`report-card-legacy`,props:{isAnalysisRunning:{type:Boolean},reportCard:{}},setup(e){let t=e,n=R(()=>Ys(t.reportCard.white.data)),r=R(()=>Ys(t.reportCard.black.data)),i={gp0:{name:D(`Opening`),tooltip:D(`This is a grade for how well the player performed in the opening.`)},gp1:{name:D(`Middlegame`),tooltip:D(`This is a grade for how well the player performed in the middlegame.`)},gp2:{name:D(`Endgame`),tooltip:D(`This is a grade for how well the player performed in the endgame.`)}};function a(e,t){let n={gp0:D(`Opening Accuracy: %rating%`,{"%rating%":Bf({digits:1,value:t})}),gp1:D(`Middlegame Accuracy: %rating%`,{"%rating%":Bf({digits:1,value:t})}),gp2:D(`Endgame Accuracy: %rating%`,{"%rating%":Bf({digits:1,value:t})})},r=D(`Accuracy: %rating%`,{"%rating%":Bf({digits:1,value:t})});return t>0?n[e]??r:D(`This phase of the game could not be graded due to a lack of relevant moves.`)}let o={0:400,1:500,2:600};function s(e){switch(e){case 0:return`brilliant`;case 1:return`good`;case 2:return`blunder`;default:return`brilliant`}}return(t,c)=>(q(),V(`section`,{class:K(t.$style.component
```

<a id="FND-30401"></a>
## FND-30401 — Implementation component review-rating

Vue compiled component __name declaration. Name suggests review rating; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1143
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
Gf(),Gf(),nl(),E(),Kf={$style:tl},qf=w(Wf,[[`__cssModules`,Kf]])})),Yf,Xf,Zf=t((()=>{Ai(),Vf(),Yf=[`textContent`],Xf=G({__name:`review-rating`,props:{color:{},isAnalysisRunning:{type:Boolean},rating:{},showDecimal:{type:Boolean},tooltip:{}},setup(e){let t=e,n=R(()=>Bf({digits:+!!t.showDecimal,defaultVal:t.rating===void 0&&!t.isAnalysisRunning?`—`:``,value:t.rating}));return(t,r)=>(q(),V(`div`,{class:K([t.$style.component,e.color===`white`?t.$style.white:t.$style.black,e.isAnalysisRunning?t.$style[`skeleton-${e.color}`]:``])},[e.tooltip?(q(),z(h,{key:0,text:e.tooltip},null,8,[`text`])):B(``,!0),r[0]||=U(),H(`span`,{textContent:X(n.value)},null,8,Yf)],2))}})})),Qf,$f,ep=t((()=>{Zf(),Zf(),dl(),E(),Qf={$style:ul},$f=w(Xf,[[`__cssModules`,Qf]])})),tp,np=t((()=>{Je(),tp={[T.Brilliant]:`brilliant`,[T.BestMove]:`best`,[T.Excellent]:`excellent`,[T.Good]:`good`,[T.Book]:`book`,[T.Inaccuracy]:`inaccuracy`,[T.Mistake]:`mistake`,[T.Blunder]:`blunder`,[T.Miss]:`miss`,[T.MissedWin]:`missedWin`,[T.GreatFind]:`greatFind`,[T.Tricky]:`tricky`}}));function rp(e,t){return e.map(e=>{let{className:n,icon:r,label:i}=de[e];return{className:e?`analysis-${n}`:void 0,data:{black:String(O.tallies.black[tp[e]]??0),white:String(O.t
```

<a id="FND-30402"></a>
## FND-30402 — Implementation component tallies

Vue compiled component __name declaration. Name suggests tallies; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1143
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
0]),import.meta.url);Dn(I(r,{isExpanded:n,result:Xt(t)}))}})),pp,mp=t((()=>{x(),ai(),ra(),up(),Bt(),fp(),Ut(),M(),pp=G({__name:`tallies`,props:{isAnalysisRunning:{type:Boolean},showExtraTallies:{type:Boolean},skillsPositionsLoaded:{type:Boolean},skillsCount:{},userColor:{}},emits:[`click-classification-row`,`update-show-extra-tallies`],setup(t,{emit:n}){let r={0:800,1:900,2:1e3,3:1100},i=$a(()=>j(()=>e(()=>import(`./skills-tally-row.7fc603bb.B6_ymQfGfh.chunk.js`),`./skills-tally-row.7fc603bb.B6_ymQfGfh.chunk.js`).then(e=>(e.t(),e.n)),__vite__mapDeps([0,1]),import.meta.url)),a=t,o=n,s=R(()=>a.isAnalysisRunning||!a.skillsPositionsLoaded||a.skillsCount>0),c=R(()=>op());function l(){let e=!a.showExtraTallies;window.chesscom.features.includes(`game_review_idl_event_tracking`)&&dp({isExpanded:e,result:S()}),o(`update-show-extra-tallies`,e)}return(e,n)=>(q(),V(`div`,null,[Z(en)()&&s.value?(q(),z(Z(i),{key:0,"is-analysis-running":t.isAnalysisRunning,"skills-positions-loaded":t.skillsPositionsLoaded,"skills-count":t.skillsCount,"user-color":t.userColor,onClickClassificationRow:n[0]||=t=>e.$emit(`click-classification-row`,t)},null,8,[`is-analysis-running`,`skills-positions-loaded`,`skills-count`,`user-color`]))
```

<a id="FND-30403"></a>
## FND-30403 — Implementation component game-overview

Vue compiled component __name declaration. Name suggests game overview; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1143
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
>{Ai(),yn(),le(),Pr(),ne(),jf(),Lf(),Jf(),ep(),_p(),Sp(),Cp=[`textContent`],wp=[`textContent`],Tp=[`textContent`],Ep=G({__name:`game-overview`,props:{avatars:{},accuracies:{},gameResult:{},isAnalysisRunning:{type:Boolean},isBasicAnalysis:{type:Boolean},playerSide:{},reportCard:{},players:{},showExtraTallies:{type:Boolean},skillsPositionsLoaded:{type:Boolean},skillsCount:{},timeControl:{},userColor:{}},emits:[`click-classification-row`,`update-show-extra-tallies`,`show-advanced-stats-upgrade-modal`],setup(e){let t=e,n=R(()=>({white:yp(t.reportCard?.white),black:yp(t.reportCard?.black)})),r=R(()=>({white:xp(t.reportCard?.white),black:xp(t.reportCard?.black)})),i=R(()=>ie()&&(!mr()||ri()));return(t,a)=>(q(),V(`div`,{class:K(t.$style.component)},[H(`div`,{class:K(t.$style.row)},[H(`span`,{class:K([`cc-paragraph-medium-bold`,t.$style[`row-title`]])},null,2),a[3]||=U(),H(`span`,{class:K([t.$style[`row-item`],t.$style.player]),textContent:X(e.players.white.getName())},null,10,Cp),a[4]||=U(),H(`span`,{class:K([t.$style[`row-item`],t.$style.player]),textContent:X(e.players.black.getName())},null,10,wp)],2),a[11]||=U(),H(`div`,{class:K(t.$style.row)},[H(`span`,{class:K([`cc-paragraph-medium-bold`,t.$style[`row-
```

<a id="FND-30404"></a>
## FND-30404 — Implementation component overview-view

Vue compiled component __name declaration. Name suggests overview view; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1143
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
,timeClass:At(t),result:Xt(n),gameReviewScreen:r}))}})),Np,Pp=t((()=>{a(),ki(),Jn(),Wa(),Ap(),La(),Xr(),Mp(),Ut(),Np=G({__name:`overview-view`,props:{avatars:{},accuracies:{},coachAvatar:{},coachName:{},coachSummary:{},depth:{},gameResult:{},gameSummary:{},forceLoadingState:{type:Boolean},isAnalysisRunning:{type:Boolean},isBasicAnalysis:{type:Boolean},playerSide:{},players:{},progress:{},reportCard:{},shouldShowCoach:{type:Boolean},showExtraTallies:{type:Boolean},showNewGameBtn:{type:Boolean},skillsPositionsLoaded:{type:Boolean},skillsCount:{},timeControl:{},timeControlLabel:{},timeControlIcon:{},userColor:{}},emits:[`start-review`,`start-new-game`,`choose-coach`,`click-classification-row`,`update-show-extra-tallies`,`show-advanced-stats-upgrade-modal`],setup(e,{emit:t}){let n=e,r=Va(),i=yt(),a=R(()=>i.value),o=R(()=>n.isAnalysisRunning||!!n.forceLoadingState),s=R(()=>o.value?void 0:`summary`),c=R(()=>`${n.coachSummary.label} - ${n.coachSummary.phrase}`),l=R(f),u=t,ee=C.Elements;function d(){window.chesscom.features.includes(`game_review_idl_event_tracking`)&&jp({timeClass:n.timeControl,result:S(),gameReviewScreen:Sn.OVERVIEW,gameType:n.timeControlIcon}),u(`start-new-game`)}function f(){return n.force
```

<a id="FND-30405"></a>
## FND-30405 — Implementation component loading-chart

Vue compiled component __name declaration. Name suggests loading chart; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1143
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
p=t((()=>{Pp(),Pp(),Yc(),E(),Fp={$style:Jc},Ip=w(Np,[[`__cssModules`,Fp]])})),Rp,zp,Bp=t((()=>{Rp=[`textContent`],zp=G({__name:`loading-chart`,props:{progress:{}},setup(e){let t=e,n=J(Math.round((t.progress||0)*100));return Q(()=>t.progress,()=>{n.value=Math.round((t.progress||0)*100)}),(t,r)=>(q(),V(`div`,{class:K([t.$style.component,{[t.$style.finished]:e.progress===1}])},[H(`div`,{class:K(t.$style.graph)},[H(`div`,{class:K(t.$style.grid)},[H(`div`,{class:K(t.$style.loadline),style:to({top:`28%`,height:`48%`,width:`${n.value}%`})},null,6),r[0]||=U(),H(`span`,{class:K(t.$style.percentage),textContent:X(`${n.value}%`)},null,10,Rp)],2)],2)],2))}})})),Vp,Hp,Up=t((()=>{Bp(),Bp(),Fc(),E(),Vp={$style:Pc},Hp=w(zp,[[`__cssModules`,Vp]])})),Wp,Gp=t((()=>{sa(),Up(),fa(),Wp=G({__name:`game-arc`,props:{currentPosition:{default:-1},options:{},progress:{default:0},blurChart:{type:Boolean,default:!1}},setup(e){let t=e,n=so(`chart`);Q(()=>t.currentPosition,r);function r(e){eo(()=>{n.value?.chart&&!t.blurChart&&ca({chart:n.value.chart,chartIndex:0,currentMoveNumber:e})})}return(t,r)=>(q(),V(`div`,{class:K(t.$style.component)},[H(`div`,{class:K(t.$style.chart)},[W(Qa,{appear:``,name:`review-game-arc-animate`},{default
```

<a id="FND-30406"></a>
## FND-30406 — Implementation component game-arc

Vue compiled component __name declaration. Name suggests game arc; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1143
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
Vp,Hp,Up=t((()=>{Bp(),Bp(),Fc(),E(),Vp={$style:Pc},Hp=w(zp,[[`__cssModules`,Vp]])})),Wp,Gp=t((()=>{sa(),Up(),fa(),Wp=G({__name:`game-arc`,props:{currentPosition:{default:-1},options:{},progress:{default:0},blurChart:{type:Boolean,default:!1}},setup(e){let t=e,n=so(`chart`);Q(()=>t.currentPosition,r);function r(e){eo(()=>{n.value?.chart&&!t.blurChart&&ca({chart:n.value.chart,chartIndex:0,currentMoveNumber:e})})}return(t,r)=>(q(),V(`div`,{class:K(t.$style.component)},[H(`div`,{class:K(t.$style.chart)},[W(Qa,{appear:``,name:`review-game-arc-animate`},{default:$(()=>[e.progress===1?(q(),z(oa,{key:0,ref_key:`chart`,ref:n,class:K([`dark-mode`,[t.$style.arc,{[t.$style.blur]:e.blurChart}]]),options:e.options},null,8,[`class`,`options`])):B(``,!0)]),_:1}),r[0]||=U(),e.progress<1?(q(),z(Hp,{key:0,class:K(t.$style.loader),progress:e.progress},null,8,[`class`,`progress`])):B(``,!0)],2)],2))}})})),Kp,qp,Jp=t((()=>{Gp(),Gp(),pc(),E(),Kp={$style:fc},qp=w(Wp,[[`__cssModules`,Kp]])}));function Yp(e,t){let n=de[e.classification],{score:r,mateIn:i}=e.playedMove,a=la(r,typeof i==`number`?5.75:4.75);return{className:`analysis-${n.className}-bg ${t.includes(e.moveNumber)?`key-move`:``}`,y:a}}var Xp=t((()=>{Ee(),ma()}));fun
```

<a id="FND-30407"></a>
## FND-30407 — Implementation component game-arc

Vue compiled component __name declaration. Name suggests game arc; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1143
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
 Qp=t((()=>{Xi(),re(),Ni(),Xp(),aa()})),$p,em=t((()=>{Jp(),Wr(),Jt(),Qp(),ui(),ua(),Kr(),$p=G({name:`GameArcController`,__name:`game-arc`,setup(e){let t=R(pa),n=R(()=>Zp({hideClassifications:!jn(),positions:Bn(),keyMoves:Hn()})),r=R(()=>O.progress);return(e,i)=>(q(),z(qp,{ref:`component`,"current-position":t.value,options:n.value,progress:r.value},null,8,[`current-position`,`options`,`progress`]))}})})),tm,nm=t((()=>{em(),em(),tm=$p})),rm,im=t((()=>{Je(),_(),it(),ze(),Fr(),rm=class extends Ge{constructor(){super(),ln(this,`updateMovelistHandler`,void 0),ln(this,`moveList`,void 0),ln(this,`events`,[be.InstanceEvents.ModeChanged,be.InstanceEvents.Create,`AnalysisStart`,`AnalysisEnd`]),ln(this,`reapplyDisplayResult`,()=>{let e=this.getAttribute(v.ObservedAttributes.DisplayResult);e&&this.getPluginMoveList()?.setResult?.(e)}),ln(this,`updateDisplayResult`,()=>{let e=this.getAttribute(v.ObservedAttributes.DisplayResult);e&&te(this.getPluginMoveList(),e,this.reapplyDisplayResult)}),this.updateMovelistHandler=e=>this.updateMoveList(e)}static get observedAttributes(){return[v.ObservedAttributes.BoardId,v.ObservedAttributes.DisplayResult,v.ObservedAttributes.IsActive,v.ObservedAttributes.MoveListId,v.ObservedA
```

<a id="FND-30408"></a>
## FND-30408 — Implementation component takeaways

Vue compiled component __name declaration. Name suggests takeaways; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1143
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
s`),ADVANCED_STAT_TYPE_STRATEGY_CATEGORY:()=>D(`Strategy`)}})),cm,lm,um=t((()=>{x(),rr(),Vu(),sm(),cm=[`onClick`],lm=G({__name:`takeaways`,props:{isTakeawayPaywalled:{type:Function},takeaways:{},selectedTakeaway:{}},emits:[`select-takeaway`,`show-advanced-stats-upgrade-modal`],setup(e){return(t,n)=>(q(),V(`div`,{class:K(t.$style.container)},[(q(!0),V(L,null,ao(e.takeaways,(r,i)=>(q(),V(`div`,{key:i,class:K([t.$style.item,e.selectedTakeaway===i?t.$style.selected:``]),onClick:e=>t.$emit(`select-takeaway`,i)},[H(`div`,{class:K(t.$style.type)},[W(p,{class:K(t.$style.icon),name:Z(zu)(r.category),variant:`color`},null,8,[`class`,`name`]),n[0]||=U(),H(`span`,{class:K(t.$style.label)},X(Z(am)(r.category)),3)],2),n[1]||=U(),e.isTakeawayPaywalled(i)?(q(),z(p,{key:0,variant:`glyph`,class:K([t.$style.icon,t.$style.lock]),is:Z(pn),onClick:co(e=>t.$emit(`show-advanced-stats-upgrade-modal`,i),[`stop`])},null,8,[`class`,`is`,`onClick`])):B(``,!0)],10,cm))),128))],2))}})})),dm,fm,pm=t((()=>{um(),um(),wl(),E(),dm={$style:Cl},fm=w(lm,[[`__cssModules`,dm]])})),mm,hm,gm,_m=t((()=>{ga(),Na(),rr(),Ca(),ja(),A(),Vu(),sm(),mm=[`textContent`],hm=[`textContent`],gm=G({__name:`takeaways-speech-bubble`,props:{botAlign:{},botAvata
```

<a id="FND-30409"></a>
## FND-30409 — Implementation component takeaways-speech-bubble

Vue compiled component __name declaration. Name suggests takeaways speech bubble; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1143
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
odules`,dm]])})),mm,hm,gm,_m=t((()=>{ga(),Na(),rr(),Ca(),ja(),A(),Vu(),sm(),mm=[`textContent`],hm=[`textContent`],gm=G({__name:`takeaways-speech-bubble`,props:{botAlign:{},botAvatar:{},botName:{},isPaywalled:{type:Boolean},speech:{},takeaway:{}},emits:[`choose-coach`],setup(e){let t={ADVANCED_STAT_TYPE_OPENING_CATEGORY:[D(`Trying to get off to a good start? Go Diamond for your Advanced Stats and learn what openings you win with the most.`),D(`Become a Diamond member and see how to improve your openings with Advanced Stats.`)],ADVANCED_STAT_TYPE_TACTICS_CATEGORY:[D(`Looking to unlock your potential? Become a Diamond member to find out which tactical patterns you should focus on.`),D(`Go Diamond and get Advanced Stats to see the tactics you're best at.`)],ADVANCED_STAT_TYPE_STRATEGY_CATEGORY:[D(`Become a Diamond member, dive into your Advanced Stats, and discover what types of chess positions you play best in.`),D(`Want more tips? Diamond members get Advanced Stats for a personalized look at how to improve their strategy.`)],ADVANCED_STAT_TYPE_ENDGAME_CATEGORY:[D(`Improve your game with Advanced Stats. Go Diamond for an in-depth look at what it takes to bring your endgame play to the next level.`),D(`Be
```

<a id="FND-30410"></a>
## FND-30410 — Implementation component move-by-move

Vue compiled component __name declaration. Name suggests move by move; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1143
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
),cn(),xe(),Mu(),wm(),d(),xn(),Xr(),Ii(),za(),Or(),ei(),tt(),Dt(),Ri(),Kn(),Zr(),Bt(),Me(),c(),Ae(),Di(),dt(),M(),Tm=G({__name:`move-by-move`,props:{coachAvatar:{},coachName:{},isBasicAnalysis:{type:Boolean},shouldShowCoach:{type:Boolean},showNewGameBtn:{type:Boolean},timeControlLabel:{},takeaways:{},selectedTakeaway:{}},emits:[`choose-coach`,`back-to-overview`,`new-game`,`select-takeaway`,`show-advanced-stats-upgrade-modal`],setup(t,{emit:n}){tn(`wc-mode-swap-move-list`,rm);let r=oo(),i=J(en()&&window.chesscom.features.includes(`web_game_review_skills_debug_ui`)),a=$a(()=>j(()=>e(()=>import(`./skills-debug-overlay.4c098d2e.DqKwcLMyu0.chunk.js`),`./skills-debug-overlay.4c098d2e.DqKwcLMyu0.chunk.js`).then(e=>(e.t(),e.n)),__vite__mapDeps([0,2]),import.meta.url)),o=so(`moveList`),s=so(`takeawaysRef`),c=R(()=>Qn.ids),l=R(()=>O.gameSummary),u=R(()=>`${Ua().label} - ${Ua().phrase}`),ee=R(()=>ue()?`summary`:void 0),d=R(()=>O.isBasicAnalysis),f=R(()=>rn().visibleModal===Ti.Types.UpgradeTrain),p=yt(),m=R(()=>p.value),te=R(()=>fi().filter(e=>!!e)),ne=R(()=>hn()),re=R(()=>({[r[`move-list-container`]]:!0,[r[`with-skills-row`]]:ne.value,[r[`hide-timestamps`]]:!wr.showTimeSpentOnMoveReview}));function h(){return/An
```

<a id="FND-30411"></a>
## FND-30411 — Implementation component tab-review

Vue compiled component __name declaration. Name suggests tab review; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-1143
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
),Lm(),Sr(),Ri(),r(),xt(),Nr(),Er(),ut(),Un(),Yr(),Me(),Nt(),Xa(),f(),qm(),Ym(),Zm(),$m(),Mp(),th(),dn(),Ut(),M(),nh=G({__name:`tab-review`,setup(t){let n=$a(()=>j(()=>e(()=>import(`./skills-progress-row.014a0e33.CHWE4eACMD.chunk.js`),`./skills-progress-row.014a0e33.CHWE4eACMD.chunk.js`).then(e=>(e.t(),e.n)),__vite__mapDeps([0,3,4]),import.meta.url)),r,i=R(()=>O.progress),a=J(Oa()),o=J(Am()),s=[In,Ds,Ts];l()&&s.push(li),Promise.resolve(Ji({settings:s})).then(()=>{a.value=Oa()});let c=_f,u=R(_a),ee=R(()=>k()),d=R(()=>!!(a.value&&Ea())),f=J(p());function p(){if(!o.value)return;if(br())return{baseTime:0,timeIncrement:0,timeType:`daily`};let e=Br();if(!e)return;let{baseTime:t,increment:n,timeType:r}=e;return{baseTime:t/1e3,timeIncrement:(n??0)/1e3,timeType:r}}Ya(sr.Events.Review),io(()=>{Yn()}),ro(()=>{let e=pi();if(e&&(gt(),Pm(),b.gameReviewPage=C.Pages.Overview),(i.value===0||e)&&(De({shouldSave:!0,userInitiated:!0,depth:di()&&document.referrer.includes(`/member/`)&&document.referrer.includes(`/stats/`)?18:void 0}),window.chesscom.features.includes(`game_review_idl_event_tracking`)&&window.chesscom.features.includes(`mbe_tracking_v2`))){let e;yi()&&(e=Km()),Xm({gameType:we(),result:S(),gameId:kt(),botCo
```

<a id="FND-30412"></a>
## FND-30412 — Stylesheet PUBLIC-006.css

531 CSS variable declarations,28media queries,1083selector records; font faces/families/exported breakpoints retained.

- Category: design_system
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3010
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Cascade order/themes matter; repeated variable names may have different scoped values. No claim the extracted selector inventory is a complete visual specification.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/design-system.json)

```text
{"variables": [{"name": "--linkBoxShadow", "value": "0 .5rem 0 0 #c7c6c5, 0 0 0 .1rem rgba(49, 46, 43, .06)", "offset": 1763}, {"name": "--linkHoverBackground", "value": "#f0f0f0", "offset": 1835}, {"name": "--linkBoxShadow", "value": "0 .5rem 0 0 rgba(0, 0, 0, .4)", "offset": 1964}], "export_blocks": [":export{blackWinning:#403d39;brandAndroid:#3DDB85;brandAppleDark:#000;brandAppleLight:#FFF;brandDiscord:#5865f2;brandFacebook:#1778f2;brandInstagram:#e93a56;brandLinkedin:#0A66C2;brandReddit:#ff4500;brandTiktokDark:#000;brandTiktokLight:#FFF;brandTwitch:#9146ff;brandTwitter:#1da1f2;brandTwitterDark:#000;brandTwitterLight:#FFF;brandVK:#5181b8;brandYoutube:#FF0000;darkShade25:rgba(0,0,0,.25);darkShade40:rgba(0,0,0,.4);medGrey:#777574}"]}
```

<a id="FND-30413"></a>
## FND-30413 — Stylesheet PUBLIC-007.css

662 CSS variable declarations,9media queries,1060selector records; font faces/families/exported breakpoints retained.

- Category: design_system
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3011
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Cascade order/themes matter; repeated variable names may have different scoped values. No claim the extracted selector inventory is a complete visual specification.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/design-system.json)

```text
{"variables": [{"name": "--color-aqua-25", "value": "#EAFFFA", "offset": 32409}, {"name": "--color-aqua-50", "value": "#DDFFF5", "offset": 32434}, {"name": "--color-aqua-75", "value": "#CCFFEC", "offset": 32459}], "export_blocks": [":export{max1024:63.999em;max1100:68.749em;max1200:74.999em;max1250:78.124em;max1400:87.499em;max330:20.624em;max400:24.999em;max480:29.999em;max550:34.374em;max640:39.999em;max700:43.749em;max768:47.999em;max960:59.999em;min1024:64em;min1100:68.75em;min1200:75em;min1250:78.125em;min1366:85.375em;min1400:87.5em;min1920:119.938em;min330:20.625em;min400:25em;min480:30em;min550:34.375em;min615:38.438em;min640:40em;min700:43.75em;min768:48em;min900:56.25em;min960:60em}"]}
```

<a id="FND-30414"></a>
## FND-30414 — Stylesheet PUBLIC-008.css

0 CSS variable declarations,2media queries,34selector records; font faces/families/exported breakpoints retained.

- Category: design_system
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3012
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Cascade order/themes matter; repeated variable names may have different scoped values. No claim the extracted selector inventory is a complete visual specification.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/design-system.json)

```text
{"variables": [], "export_blocks": [":export{max1024:63.999em;max1100:68.749em;max1200:74.999em;max1250:78.124em;max1400:87.499em;max330:20.624em;max400:24.999em;max480:29.999em;max550:34.374em;max640:39.999em;max700:43.749em;max768:47.999em;max960:59.999em;min1024:64em;min1100:68.75em;min1200:75em;min1250:78.125em;min1366:85.375em;min1400:87.5em;min1920:119.938em;min330:20.625em;min400:25em;min480:30em;min550:34.375em;min615:38.438em;min640:40em;min700:43.75em;min768:48em;min900:56.25em;min960:60em}"]}
```

<a id="FND-30415"></a>
## FND-30415 — Stylesheet PUBLIC-009.css

47 CSS variable declarations,13media queries,187selector records; font faces/families/exported breakpoints retained.

- Category: design_system
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3013
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Cascade order/themes matter; repeated variable names may have different scoped values. No claim the extracted selector inventory is a complete visual specification.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/design-system.json)

```text
{"variables": [{"name": "--navWidth", "value": "17rem", "offset": 565}, {"name": "--navWidth", "value": "5.6rem", "offset": 622}, {"name": "--navWidth", "value": "17rem", "offset": 709}], "export_blocks": [":export{navWidthCollapsed:5.6rem;navWidthDefault:17rem}"]}
```

<a id="FND-30416"></a>
## FND-30416 — module-001 complete structural inventory

32865067bytes; SHA256b1037807ca8917e083b37f62c3084bf77d5fa4e99ee125ec0ebff64fbd96ac28; 22922defined functions,154imported functions,152exports. All section offsets,types,limits,globals,elements,data and function body spans retained.

- Category: wasm_structure
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../wasm-analysis/modules/module-001/structure.json)

```text
Magic0061736d;version1;no custom sections.
```

<a id="FND-30417"></a>
## FND-30417 — module-001 function and call-graph analysis

97169direct caller/callee pairs;234030static direct-call sites;9438indirect-call sites. Exact direct call indices recovered from full WAT. Indirect dispatch targets not resolved; opcode frequencies are syntactic counts,not execution profiling.

- Category: wasm_functions
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/functions.json)

```text
See call-graph.jsonl.gz and opcode-statistics.json.
```

<a id="FND-30418"></a>
## FND-30418 — module-001 strings and data offsets

43416ASCII candidates,2747keyword-relevant candidates,540UTF16candidates. Strings linked to original file offsets and active data memory addresses when constant-resolvable. Random code/weight bytes can resemble text.

- Category: wasm_strings
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/strings.txt)

```text
All-ASCII candidates are separately gzipped; relevant output is not a semantic analysis of every string.
```

<a id="FND-30419"></a>
## FND-30419 — module-001 memory/host boundary

{"defined_memories": [{"flags": 1, "minimum": 6176, "shared": false, "memory64": false, "maximum": 32768}], "imported_memories": [], "tables": [{"element_type": "funcref", "limits": {"flags": 1, "minimum": 26300, "shared": false, "memory64": false, "maximum": 26300}}], "data_segments": 4270}

- Category: wasm_memory
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3014
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: FND-30416
- [Exact supporting artifact](../wasm-analysis/modules/module-001/structure.json)

```text
Memory limits use64KiBpages; shared flag is explicit.
```
