# Extended findings

[Master index](../chapters/00_MASTER_INDEX.md)

<a id="FND-30240"></a>
## FND-30240 — Implementation component cc-loader

Vue compiled component __name declaration. Name suggests cc loader; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
con-size-48":`cc-icon-size-48_a20950e`,"cc-icon-size-64":`cc-icon-size-64_a20950e`}}]])})),nK,Brt=r((()=>{Qa(),nK=Za(y({__name:`cc-loader`,props:{size:{},variant:{default:`blocks`}},setup(e){return(t,n)=>e.variant===`blocks`?(O(),p(`div`,{key:0,"aria-busy":`true`,"aria-live":`polite`,class:D([t.$style[`cc-loader-component`],t.$style[`cc-loader-${e.size}`]])},[(O(),p(s,null,ge(6,e=>m(`div`,{key:e,class:D([t.$style[`cc-loader-square`],t.$style[`cc-loader-square-${e}`]])},null,2)),64))],2)):(O(),p(`div`,{key:1,"aria-busy":`true`,"aria-live":`polite`,class:D([t.$style[`cc-loader-spinner`],t.$style[`cc-loader-${e.size}`],t.$style[`cc-loader-${e.variant}`]])},null,2))}}),[[`__cssModules`,{$style:{"cc-loader-component":`cc-loader-component_1e4c4f9`,"cc-loader-spinner":`cc-loader-spinner_1e4c4f9`,"cc-loader-spin":`cc-loader-spin_1e4c4f9`,"cc-loader-small":`cc-loader-small_1e4c4f9`,"cc-loader-medium":`cc-loader-medium_1e4c4f9`,"cc-loader-large":`cc-loader-large_1e4c4f9`,"cc-loader-spinner-green":`cc-loader-spinner-green_1e4c4f9`,"cc-loader-spinner-gray":`cc-loader-spinner-gray_1e4c4f9`,"cc-loader-spinner-chameleon":`cc-loader-spinner-chameleon_1e4c4f9`,"cc-loader-square":`cc-loader-square_1e4c4f9`,"cc-loader-s
```

<a id="FND-30241"></a>
## FND-30241 — Implementation component cc-button

Vue compiled component __name declaration. Name suggests cc button; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
rge`},"xx-large":{iconSize:32,imgSize:32,loaderSize:`large`}},Vrt=[`height`,`src`,`width`],Hrt=[`textContent`],iK=Za(y({__name:`cc-button`,props:{align:{default:`center`},customClasses:{},customImgSrc:{},disabled:{type:Boolean},fullWidth:{type:Boolean},href:{},icon:{},isOneLineText:{type:Boolean},label:{},loading:{type:Boolean},minWidth:{type:Boolean},routerLink:{},selectedBorder:{type:Boolean},size:{default:`medium`},type:{default:`button`},variant:{default:`secondary`}},emits:[`click`,`contextmenu`,`touchend`,`touchstart`],setup(e){let t=e,n=l(()=>t.routerLink?`router-link`:t.href?`a`:`button`),r=l(()=>{if(n.value===`button`)return t.disabled||t.loading?!0:void 0}),i=l(()=>rK[t.size].iconSize),a=l(()=>rK[t.size].loaderSize);return(t,o)=>(O(),d(ve(n.value),{class:D([t.$style[`cc-button-component`],t.$style[`cc-button-${e.variant}`],t.$style[`cc-button-${e.size}`],{[t.$style[`cc-button-full`]]:e.fullWidth,[t.$style[`cc-button-disabled`]]:e.disabled,[t.$style[`cc-button-loading`]]:e.loading,[t.$style[`cc-button-min-width`]]:e.minWidth,[t.$style[`cc-button-selected-border`]]:e.selectedBorder,[t.$style[`cc-button-align-start`]]:e.align===`start`}]),"data-align":e.align,"data-disabled":e.disabled?`true`:`
```

<a id="FND-30242"></a>
## FND-30242 — Implementation component cc-tooltip

Vue compiled component __name declaration. Name suggests cc tooltip; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
 Date(e),write:e=>e.toISOString()}},AK=`vueuse-storage`,jK=new Map,MK=1})),Fit,Iit,Lit=r((()=>{NK(),Ud(),Fit=200,Iit=y({__name:`cc-tooltip`,props:{allowMobile:{type:Boolean},anchor:{default:`center`},closeOnClick:{type:Boolean},delay:{default:200},forElement:{},forPreviousElement:{type:Boolean},position:{default:`top`},text:{},stickyVisible:{type:Boolean},triggerElement:{default:null}},setup(e){let t=e,n=wit(),r=Math.max(10,t.delay),i=xe(),a=xe(!1),o=xe(!1),s=ke(`popoverEl`),c,l,u;function d(){return typeof window>`u`||typeof window.matchMedia!=`function`?!0:window.matchMedia(`(hover: hover) and (pointer: fine)`)?.matches??!0}function g(){if(_(),c=t.forElement??(t.forPreviousElement?n.value?.previousElementSibling:n.value?.parentElement),l=t.triggerElement??c,t.stickyVisible){S();return}if(!d()){l?.addEventListener(`click`,b);return}t.closeOnClick&&l?.addEventListener(`click`,v),l?.addEventListener(`mouseenter`,y)}function _(){clearTimeout(u),l?.removeEventListener(`click`,v),l?.removeEventListener(`mouseleave`,v),l?.removeEventListener(`mouseenter`,y),l?.removeEventListener(`click`,b),document.removeEventListener(`click`,x)}se(()=>{!d()&&!t.allowMobile||ne(g)}),le(_);function v(){o.value=!1,clearTime
```

<a id="FND-30243"></a>
## FND-30243 — Implementation component cc-icon-button

Vue compiled component __name declaration. Name suggests cc icon button; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
FK=r((()=>{Lit(),Lit(),Kue(),He(),Rit={$style:el},PK=Ve(Iit,[[`__cssModules`,Rit]])})),zit,Bit=r((()=>{cK(),FK(),zit=y({__name:`cc-icon-button`,props:{customClasses:{},disabled:{type:Boolean},href:{},target:{},icon:{},iconSize:{default:20},size:{default:`small`},tooltip:{},variant:{default:`ghost`}},emits:[`click`,`contextmenu`,`touchend`,`touchstart`],setup(e){let t=e,n=l(()=>t.disabled||null),r=l(()=>typeof t.tooltip==`object`?t.tooltip:{text:t.tooltip,position:`top`,anchor:void 0,closeOnClick:void 0});return(t,i)=>(O(),d(ve(e.href?`a`:`button`),{"aria-label":r.value.text,class:D([`cc-icon-button-component`,`cc-icon-button-${e.size}`,`cc-icon-button-${e.variant}`,`cc-bg-${e.variant}`,{"cc-icon-button-disabled":n.value&&e.href},e.customClasses?.container]),disabled:n.value,href:e.href||null,target:e.target||null,type:e.href?null:`button`,onClick:i[0]||=e=>t.$emit(`click`,e),onContextmenu:i[1]||=e=>t.$emit(`contextmenu`,e),onTouchend:i[2]||=e=>t.$emit(`touchend`,e),onTouchstart:i[3]||=e=>t.$emit(`touchstart`,e)},{default:Me(()=>[e.tooltip?(O(),d(PK,{key:0,anchor:r.value.anchor,"close-on-click":r.value.closeOnClick,position:r.value.position,text:r.value.text},null,8,[`anchor`,`close-on-click`,`position
```

<a id="FND-30244"></a>
## FND-30244 — Implementation component report-ad-button

Vue compiled component __name declaration. Name suggests report ad button; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
sabled`,`href`,`target`,`type`]))}})})),IK,LK=r((()=>{Bit(),Bit(),IK=zit})),Vit,Hit=r((()=>{_E(),Frt(),oK(),LK(),Vit=y({__name:`report-ad-button`,props:{slotId:{},variant:{default:`default`}},setup(e){let t=e;function n(){Prt(t.slotId)}return(t,r)=>e.variant===`icon`?(O(),d(IK,{key:0,icon:{is:k(qy),variant:`glyph`},tooltip:{text:t.$trans(`Report Ad`),position:`bottom`},"icon-size":16,size:`small`,onClick:n},null,8,[`icon`,`tooltip`])):(O(),d(aK,{key:1,class:D([t.$style.report,`dark-mode`]),size:`x-small`,label:t.$trans(`Report Ad`),variant:`ghost`,onClick:n},null,8,[`class`,`label`]))}})})),Uit,Wit,Git=r((()=>{Hit(),Hit(),Oue(),He(),Uit={$style:ns},Wit=Ve(Vit,[[`__cssModules`,Uit]])})),Kit,qit=r((()=>{_E(),oK(),bg(),R(),window.chesscom=window.chesscom||{},window.chesscom.routes=window.chesscom.routes||{},Object.assign(window.chesscom.routes,{web_membership_no_ads:{tokens:[[`text`,`/no-ads`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_IR|fi_FI|fil_PH|fr_FR|gl_ES|he_IL|hi_IN|hr_HR|hu_HU|hy_AM|id_ID|is_IS|it
```

<a id="FND-30245"></a>
## FND-30245 — Implementation component ad-upgrade-link

Vue compiled component __name declaration. Name suggests ad upgrade link; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
chach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}}),Kit=y({__name:`ad-upgrade-link`,props:{referral:{},variant:{default:`default`}},setup(e){let t=e,n=L(`Remove Ads`),r=yg.generate(`web_membership_no_ads`,{c:t.referral??`no_ads`,utm_source:`chesscom`,utm_medium:`no_ads_button`});return(t,i)=>e.variant===`link`?(O(),d(aK,{key:0,variant:`ghost-link`,target:`_blank`,size:`medium`,class:D(t.$style[`link-height`]),label:k(n),href:k(r),icon:{is:k(Ky),variant:`glyph`}},null,8,[`class`,`label`,`href`,`icon`])):(O(),d(aK,{key:1,variant:`monetization`,target:`_blank`,size:`small`,"full-width":``,class:D(t.$style[`monetization-button`]),label:k(n),href:k(r),icon:{is:k(Ky),variant:`glyph`}},null,8,[`class`,`label`,`href`,`icon`]))}})})),Jit,Yit,Xit=r((()=>{qit(),qit(),Due(),He(),Jit={$style:es},Yit=Ve(Kit,[[`__cssModules`,Jit]])})),Zit,Qit=r((()=>{Ml(),tde(),Zit={[Pl.oneColumn]:[jl.leaderboardAtf,jl.leaderboardBtf],[Pl.twoColumn]:[jl.leaderboardAtf,jl.mediumRectangleAtf,jl.mediumRectangleBtf],[Pl.twoColumnAlt]:[jl.mediumRectangleAtf,jl.mediumRectangleBtf,jl.leaderboardBtf],[Pl.twoColumnProfile]:[jl.leaderboardAtf,jl.mediumRectangleAtf,jl.mediumRectangle
```

<a id="FND-30246"></a>
## FND-30246 — Implementation component user-chess-title

Vue compiled component __name declaration. Name suggests user chess title; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
tocomplete-fill-selected`},Mkt={FETCH_ROLES:`fetchRoles`}})),Nkt,Pkt,Fkt=r((()=>{q6(),FK(),Nkt=[`href`,`target`],Pkt=y({__name:`user-chess-title`,props:{openNewTab:{type:Boolean},title:{},tooltipPosition:{},url:{}},setup(e){let t=e,n=l(()=>K6[t.title]),r=l(()=>t.openNewTab?`_blank`:void 0);return(t,i)=>e.url?(O(),p(`a`,{key:0,class:D(t.$style.component),href:e.url,target:r.value},[g(PK,{position:e.tooltipPosition,text:n.value},null,8,[`position`,`text`]),h(` `+Se(e.title),1)],10,Nkt)):(O(),p(`span`,{key:1,class:D(t.$style.component)},[g(PK,{position:e.tooltipPosition,text:n.value},null,8,[`position`,`text`]),h(` `+Se(e.title),1)],2))}})})),Ikt,J6,Lkt=r((()=>{Fkt(),Fkt(),Bue(),He(),Ikt={$style:Zs},J6=Ve(Pkt,[[`__cssModules`,Ikt]])}));function Rkt(e,t){let n=t?Object.entries(t).map(([e,t])=>({check:wK(`(${e.startsWith(`min`)?`min-width`:`max-width`}: ${El[e]})`),value:t})):[];return l(()=>{let t=we(e);for(let{check:e,value:r}of n)e.value&&(t=r);return t})}var zkt=r((()=>{NK(),Que()})),Bkt,Vkt,Hkt=r((()=>{$m(),zkt(),sf(),Bkt=[`loading`,`src`,`srcset`,`alt`,`height`,`width`],Vkt=y({__name:`cc-avatar-pure`,props:{src:{},clickBehavior:{default:`none`},isLazyLoading:{type:Boolean},retinaSupport:{type:Boolean
```

<a id="FND-30247"></a>
## FND-30247 — Implementation component cc-avatar-pure

Vue compiled component __name declaration. Name suggests cc avatar pure; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
=r((()=>{NK(),Que()})),Bkt,Vkt,Hkt=r((()=>{$m(),zkt(),sf(),Bkt=[`loading`,`src`,`srcset`,`alt`,`height`,`width`],Vkt=y({__name:`cc-avatar-pure`,props:{src:{},clickBehavior:{default:`none`},isLazyLoading:{type:Boolean},retinaSupport:{type:Boolean,default:!0},responsiveSize:{},size:{default:40},status:{default:()=>({isOnline:!1,isPlaying:!1,isStreaming:!1})},username:{},userProfileUrl:{default:``}},setup(e){let{trans:t}=Zm(),n=e,r=[`openProfile`,`openProfileInNewTab`],i=me(!1),a=me(!1),o=l(()=>n.status?.isStreaming?`streaming`:n.status?.isPlaying?`playing`:n.status?.isOnline?`online`:``),s=Rkt(()=>n.size,n.responsiveSize),c=l(()=>n.username?t[`Avatar of %username%`](n.username):t.Avatar),u=l(()=>r.includes(n.clickBehavior)?`a`:`div`),f=l(()=>r.includes(n.clickBehavior)?n.userProfileUrl:null),p=l(()=>n.clickBehavior===`openProfileInNewTab`?`_blank`:null),g=l(()=>r.includes(n.clickBehavior)?n.username:null),_=l(()=>n.src&&n.retinaSupport&&!a.value?`${n.src} 1x, ${of(n.src)} 2x`:``),v=l(()=>i.value||!n.src?`/bundles/web/images/user-image.svg`:n.src);Ae(()=>n.src,()=>{i.value=!1,a.value=!1});function y(e){e.target.srcset?a.value=!0:i.value=!0}return(t,n)=>(O(),d(ve(u.value),{class:D([`cc-avatar-component`,`
```

<a id="FND-30248"></a>
## FND-30248 — Implementation component cc-avatar

Vue compiled component __name declaration. Name suggests cc avatar; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
3},8,[`class`,`href`,`title`,`target`]))}})})),Ukt,Wkt=r((()=>{Hkt(),Hkt(),Ukt=Vkt})),Gkt,Kkt=r((()=>{Wkt(),$m(),Gkt=y({__name:`cc-avatar`,props:{src:{},clickBehavior:{default:`none`},isLazyLoading:{type:Boolean,default:!0},retinaSupport:{type:Boolean,default:!0},responsiveSize:{},size:{default:40},status:{default:()=>({isOnline:!1,isPlaying:!1,isStreaming:!1})},url:{},username:{}},setup(e){let t=e,{routes:n}=Zm(),r=l(()=>t.url||n.webMemberView(t.username));return(t,n)=>(O(),d(Ukt,E(t.$attrs,{src:e.src,"click-behavior":e.clickBehavior,"retina-support":e.retinaSupport,"responsive-size":e.responsiveSize,size:e.size,status:e.status,"is-lazy-loading":e.isLazyLoading,username:e.username,"user-profile-url":r.value}),{default:Me(()=>[_e(t.$slots,`default`)]),_:3},16,[`src`,`click-behavior`,`retina-support`,`responsive-size`,`size`,`status`,`is-lazy-loading`,`username`,`user-profile-url`]))}})})),Y6,qkt=r((()=>{Kkt(),Kkt(),Y6=Gkt})),Jkt,Ykt,Xkt=r((()=>{sf(),Jkt=[`loading`,`alt`,`height`,`width`,`src`,`srcset`],Ykt=y({__name:`cc-image`,props:{alt:{},aspect:{default:`square`},retinaSupport:{type:Boolean,default:!0},isLazyLoading:{type:Boolean,default:!0},size:{default:40},src:{}},setup(e){let t=e,n=me(!1),r=me(
```

<a id="FND-30249"></a>
## FND-30249 — Implementation component cc-image

Vue compiled component __name declaration. Name suggests cc image; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
qkt=r((()=>{Kkt(),Kkt(),Y6=Gkt})),Jkt,Ykt,Xkt=r((()=>{sf(),Jkt=[`loading`,`alt`,`height`,`width`,`src`,`srcset`],Ykt=y({__name:`cc-image`,props:{alt:{},aspect:{default:`square`},retinaSupport:{type:Boolean,default:!0},isLazyLoading:{type:Boolean,default:!0},size:{default:40},src:{}},setup(e){let t=e,n=me(!1),r=me(!1),i=t.aspect===`16-9`?`/bundles/web/images/noavatar_content.png`:`/bundles/web/images/user-image.svg`,a=l(()=>t.src&&t.retinaSupport&&!r.value?`${t.src} 1x, ${of(t.src)} 2x`:``),o=l(()=>n.value||!t.src?i:t.src);function s(e){e.target.srcset?r.value=!0:n.value=!0}return(t,n)=>(O(),p(`div`,{class:D([`cc-image-component`,`cc-image-size-${e.size}`])},[m(`img`,{loading:e.isLazyLoading?`lazy`:void 0,alt:e.alt,class:D([`cc-image-image`,{"cc-image-wide":e.aspect===`16-9`}]),height:e.size,width:e.size,src:o.value,srcset:a.value,onError:s},null,42,Jkt)],2))}})})),Zkt,Qkt=r((()=>{Xkt(),Xkt(),Zkt=Ykt})),$kt,eAt,tAt,nAt,rAt=r((()=>{FK(),$kt=[`href`,`aria-label`],eAt=[`alt`,`width`,`height`,`src`],tAt=[`alt`,`width`,`height`,`src`],nAt=y({__name:`flair`,props:{alt:{},href:{},size:{default:`small`},src:{},tooltipPosition:{}},emits:[`click`],setup(e){let t={small:`16`,medium:`24`,large:`32`}[e.size];return
```

<a id="FND-30250"></a>
## FND-30250 — Implementation component flair

Vue compiled component __name declaration. Name suggests flair; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
rAt=r((()=>{FK(),$kt=[`href`,`aria-label`],eAt=[`alt`,`width`,`height`,`src`],tAt=[`alt`,`width`,`height`,`src`],nAt=y({__name:`flair`,props:{alt:{},href:{},size:{default:`small`},src:{},tooltipPosition:{}},emits:[`click`],setup(e){let t={small:`16`,medium:`24`,large:`32`}[e.size];return(n,r)=>(O(),p(s,null,[e.href?(O(),p(`a`,E({key:0},n.$attrs,{href:e.href,"aria-label":e.alt,onClick:r[0]||=e=>n.$emit(`click`,e)}),[m(`img`,{alt:e.alt,class:D([`flair-rpc-component`,`flair-rpc-${e.size}`]),width:k(t),height:k(t),src:e.src},null,10,eAt),r[2]||=h(),e.alt?(O(),d(PK,{key:0,"for-previous-element":``,position:e.tooltipPosition,text:e.alt},null,8,[`position`,`text`])):f(``,!0)],16,$kt)):(O(),p(`img`,E({key:1},n.$attrs,{alt:e.alt,class:[`flair-rpc-component`,`flair-rpc-${e.size}`],width:k(t),height:k(t),src:e.src,onClick:r[1]||=e=>n.$emit(`click`,e)}),null,16,tAt)),r[3]||=h(),e.alt?(O(),d(PK,{key:2,"close-on-click":``,"for-previous-element":``,position:e.tooltipPosition,text:e.alt},null,8,[`position`,`text`])):f(``,!0)],64))}})})),X6,iAt=r((()=>{rAt(),rAt(),X6=nAt}));function aAt(e){return!!(e?.id&&window.chesscom.features?.includes(`premium_badge_redesign`)&&W6.includes(e.id))}var oAt=r((()=>{q6()}));function 
```

<a id="FND-30251"></a>
## FND-30251 — Implementation component flair

Vue compiled component __name declaration. Name suggests flair; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
buser]:L(`Closed: Abuse`),[o_.voluntarilyClosed]:L(`Closed: Inactive`)}})),lAt,uAt=r((()=>{$G(),iAt(),Q6(),cAt(),lAt=y({__name:`flair`,props:{disableHref:{type:Boolean,default:!1},flair:{},membershipLevel:{default:jrt(`getMembershipLevel`)},size:{default:`small`},tooltipPosition:{}},emits:[`log-action`],setup(e){let t=e,n=l(()=>Z6(t.flair)),r=l(()=>sAt(t.flair,t.membershipLevel));return(t,i)=>n.value?(O(),d(X6,{key:0,alt:r.value,size:e.size,src:n.value,"tooltip-position":e.tooltipPosition,onClick:i[0]||=e=>t.$emit(`log-action`,{button:`flair`})},null,8,[`alt`,`size`,`src`,`tooltip-position`])):f(``,!0)}})})),e8,dAt=r((()=>{uAt(),uAt(),e8=lAt})),fAt,pAt=r((()=>{FK(),$m(),fAt=y({__name:`cc-country-flag`,props:{code:{},isClickable:{type:[Boolean,null],default:!0},name:{},showTooltip:{type:Boolean,default:!0},size:{default:`small`},tooltipPosition:{default:`top`},tooltipText:{}},setup(e){let t=e,{countryName:n,features:r,routes:i,trans:a}=Zm(),o=l(()=>c.value||h.value?`sanctioned`:t.code.toString().toLowerCase()),s=l(()=>t.code.toString().toUpperCase()),c=l(()=>[`FD`,`431`].includes(s.value)),u=l(()=>[`RU`,`116`].includes(s.value)),m=l(()=>[`BY`,`22`].includes(s.value)),h=l(()=>!!(r.includes(`sanction_rus
```

<a id="FND-30252"></a>
## FND-30252 — Implementation component cc-country-flag

Vue compiled component __name declaration. Name suggests cc country flag; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
`size`,`src`,`tooltip-position`])):f(``,!0)}})})),e8,dAt=r((()=>{uAt(),uAt(),e8=lAt})),fAt,pAt=r((()=>{FK(),$m(),fAt=y({__name:`cc-country-flag`,props:{code:{},isClickable:{type:[Boolean,null],default:!0},name:{},showTooltip:{type:Boolean,default:!0},size:{default:`small`},tooltipPosition:{default:`top`},tooltipText:{}},setup(e){let t=e,{countryName:n,features:r,routes:i,trans:a}=Zm(),o=l(()=>c.value||h.value?`sanctioned`:t.code.toString().toLowerCase()),s=l(()=>t.code.toString().toUpperCase()),c=l(()=>[`FD`,`431`].includes(s.value)),u=l(()=>[`RU`,`116`].includes(s.value)),m=l(()=>[`BY`,`22`].includes(s.value)),h=l(()=>!!(r.includes(`sanction_russia_flag`)&&u.value)||!!(r.includes(`sanction_belarus_flag`)&&m.value)),g=l(()=>{if(t.showTooltip)return c.value?a[`Due to the ongoing war and resulting international sanctions, Russian and Belarusian flags will not be shown for players in Verified events.`]:t.tooltipText===void 0?n(t.code)??t.name:t.tooltipText}),_=i.webArticleUkraine;return(t,n)=>h.value?(O(),d(ve(e.isClickable?`a`:`div`),{key:0,href:e.isClickable?k(_):null,target:e.isClickable?`_blank`:null,class:D([`cc-country-flag-component`,`country-${o.value}`,{[`cc-country-flag-${e.size}`]:e.size}])},{
```

<a id="FND-30253"></a>
## FND-30253 — Implementation component cc-user-badge-pure

Vue compiled component __name declaration. Name suggests cc user badge pure; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
 n?t?n===a_.staff||n===a_.moderator||r:!e&&r:!1}var SAt=r((()=>{s_()})),CAt,wAt=r((()=>{_E(),gM(),cK(),FK(),$m(),CAt=y({__name:`cc-user-badge-pure`,props:{badgeUrl:{},isClickable:{type:Boolean},membership:{},size:{},tooltipPosition:{}},setup(e){let{features:t,trans:n}=Zm(),r=e,i=l(()=>t.includes(`premium_badge_redesign`)),a=l(()=>{switch(r.size){case`medium`:return 16;case`large`:return 20;default:return 12}}),o=l(()=>{switch(r.size){case`medium`:return 20;case`large`:return 24;default:return 16}}),s=l(()=>{switch(r.membership){case a_.staff:return{type:`staff`,icon:kw,colorIcon:`pawn-staff`,tooltip:n[`Staff Member`],redirectTo:`about`};case a_.moderator:return{type:`moderator`,icon:uE,colorIcon:`pawn-mod`,tooltip:n.Moderator,redirectTo:`about`};case a_.gold:return{type:`gold`,icon:Wje,colorIcon:`commerce-gold`,tooltip:n[`Gold Member`],redirectTo:`membership`};case a_.platinum:return{type:`platinum`,icon:Kje,colorIcon:`commerce-platinum`,tooltip:n[`Platinum Member`],redirectTo:`membership`};case a_.diamond:return{type:`diamond`,icon:nw,colorIcon:`commerce-diamond`,tooltip:n[`Diamond Member`],redirectTo:`membership`};case a_.pro:return{type:`pro`,icon:pAe,colorIcon:`commerce-pro`,tooltip:n[`Pro Member`
```

<a id="FND-30254"></a>
## FND-30254 — Implementation component cc-user-badge

Vue compiled component __name declaration. Name suggests cc user badge; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
)=>{wAt(),wAt(),Jue(),He(),TAt={$style:fl},EAt=Ve(CAt,[[`__cssModules`,TAt]])})),OAt,kAt=r((()=>{gM(),DAt(),$m(),OAt=y({__name:`cc-user-badge`,props:{isClickable:{type:Boolean},membership:{},size:{},tooltipPosition:{}},setup(e){let t=e,{currentRoute:n,routes:r}=Zm(),i=l(()=>{switch(t.membership){case a_.staff:return{type:`staff`,redirectTo:`about`};case a_.moderator:return{type:`moderator`,redirectTo:`about`};case a_.gold:return{type:`gold`,redirectTo:`membership`};case a_.platinum:return{type:`platinum`,redirectTo:`membership`};case a_.diamond:return{type:`diamond`,redirectTo:`membership`};case a_.pro:return{type:`pro`,redirectTo:`membership`};default:return null}}),a=l(()=>i.value?.redirectTo===`membership`?r.webMembership({b:`badge-${i.value?.type}`,c:n()}):i.value?.redirectTo===`about`?r.webAbout:null);return(t,n)=>(O(),d(EAt,E(t.$attrs,{"is-clickable":e.isClickable,membership:e.membership,size:e.size,"tooltip-position":e.tooltipPosition,"badge-url":a.value}),null,16,[`is-clickable`,`membership`,`size`,`tooltip-position`,`badge-url`]))}})})),r8,AAt=r((()=>{kAt(),kAt(),r8=OAt})),jAt,MAt=r((()=>{jAt=y({__name:`cc-user-rating`,props:{rating:{},variant:{default:`default`},size:{default:``}},setup(e){r
```

<a id="FND-30255"></a>
## FND-30255 — Implementation component cc-user-rating

Vue compiled component __name declaration. Name suggests cc user rating; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
`membership`,`size`,`tooltip-position`,`badge-url`]))}})})),r8,AAt=r((()=>{kAt(),kAt(),r8=OAt})),jAt,MAt=r((()=>{jAt=y({__name:`cc-user-rating`,props:{rating:{},variant:{default:`default`},size:{default:``}},setup(e){return(t,n)=>(O(),p(`div`,{class:D([e.size===`large`?`cc-text-x-large`:`cc-text-medium`,t.$style[e.variant]])},`
    (`+Se(e.rating)+`)
  `,3))}})})),NAt,i8,PAt=r((()=>{MAt(),MAt(),Yue(),He(),NAt={$style:gl},i8=Ve(jAt,[[`__cssModules`,NAt]])})),FAt,IAt=r((()=>{q6(),FK(),FAt=y({__name:`cc-user-title-pure`,props:{isClickable:{type:Boolean},title:{},size:{default:``},tooltipPosition:{},titleUrl:{default:``}},setup(e){let t=e,n=l(()=>K6[t.title]),r=l(()=>t.size===`large`?`cc-text-x-large-bold`:t.size===`medium`?`cc-text-small-bold`:`cc-text-x-small-bold`);return(t,i)=>(O(),p(s,null,[(O(),d(ve(e.isClickable?`a`:`div`),{class:D([t.$style.component,r.value]),href:e.isClickable?e.titleUrl:null,target:e.isClickable?`_blank`:null},{default:Me(()=>[h(Se(e.title),1)]),_:1},8,[`class`,`href`,`target`])),i[0]||=h(),g(PK,{"close-on-click":``,"for-previous-element":``,text:n.value,position:e.tooltipPosition},null,8,[`text`,`position`])],64))}})})),LAt,RAt,zAt=r((()=>{IAt(),IAt(),Xue(),He(),LAt={$style:vl
```

<a id="FND-30256"></a>
## FND-30256 — Implementation component cc-user-title-pure

Vue compiled component __name declaration. Name suggests cc user title pure; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
At=r((()=>{MAt(),MAt(),Yue(),He(),NAt={$style:gl},i8=Ve(jAt,[[`__cssModules`,NAt]])})),FAt,IAt=r((()=>{q6(),FK(),FAt=y({__name:`cc-user-title-pure`,props:{isClickable:{type:Boolean},title:{},size:{default:``},tooltipPosition:{},titleUrl:{default:``}},setup(e){let t=e,n=l(()=>K6[t.title]),r=l(()=>t.size===`large`?`cc-text-x-large-bold`:t.size===`medium`?`cc-text-small-bold`:`cc-text-x-small-bold`);return(t,i)=>(O(),p(s,null,[(O(),d(ve(e.isClickable?`a`:`div`),{class:D([t.$style.component,r.value]),href:e.isClickable?e.titleUrl:null,target:e.isClickable?`_blank`:null},{default:Me(()=>[h(Se(e.title),1)]),_:1},8,[`class`,`href`,`target`])),i[0]||=h(),g(PK,{"close-on-click":``,"for-previous-element":``,text:n.value,position:e.tooltipPosition},null,8,[`text`,`position`])],64))}})})),LAt,RAt,zAt=r((()=>{IAt(),IAt(),Xue(),He(),LAt={$style:vl},RAt=Ve(FAt,[[`__cssModules`,LAt]])})),BAt,VAt=r((()=>{zAt(),$m(),BAt=y({__name:`cc-user-title`,props:{isClickable:{type:Boolean},title:{},size:{default:``},tooltipPosition:{}},setup(e){let{routes:t}=Zm(),n=t.webMemberTitledPlayers;return(t,r)=>(O(),d(RAt,{"is-clickable":e.isClickable,title:e.title,size:e.size,"tooltip-position":e.tooltipPosition,"title-url":k(n)},null,8,
```

<a id="FND-30257"></a>
## FND-30257 — Implementation component cc-user-title

Vue compiled component __name declaration. Name suggests cc user title; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
=r((()=>{IAt(),IAt(),Xue(),He(),LAt={$style:vl},RAt=Ve(FAt,[[`__cssModules`,LAt]])})),BAt,VAt=r((()=>{zAt(),$m(),BAt=y({__name:`cc-user-title`,props:{isClickable:{type:Boolean},title:{},size:{default:``},tooltipPosition:{}},setup(e){let{routes:t}=Zm(),n=t.webMemberTitledPlayers;return(t,r)=>(O(),d(RAt,{"is-clickable":e.isClickable,title:e.title,size:e.size,"tooltip-position":e.tooltipPosition,"title-url":k(n)},null,8,[`is-clickable`,`title`,`size`,`tooltip-position`,`title-url`]))}})})),a8,HAt=r((()=>{VAt(),VAt(),a8=BAt})),UAt,WAt=r((()=>{UAt=y({__name:`cc-user-username-pure`,props:{clickBehavior:{},customUrl:{},username:{},variant:{default:`boldest`},size:{default:``},userProfileUrl:{default:``}},emits:[`log-action`],setup(e){let t=[`openProfile`,`openProfileInNewTab`],n=e,r=l(()=>t.includes(n.clickBehavior)?`a`:`div`),i=l(()=>t.includes(n.clickBehavior)?n.userProfileUrl:null),a=l(()=>n.clickBehavior===`openProfileInNewTab`?`_blank`:null),o=l(()=>{let e={};return n.clickBehavior===`badgeAsLink`&&(e.role=`button`,e.tabindex=0),e});return(t,n)=>(O(),d(ve(r.value),E(o.value,{class:[`cc-text-medium-bold`,[t.$style.component,t.$style[e.variant],t.$style[e.size]]],href:i.value,target:a.value,onClick:n[0]||
```

<a id="FND-30258"></a>
## FND-30258 — Implementation component cc-user-username-pure

Vue compiled component __name declaration. Name suggests cc user username pure; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
ble`,`title`,`size`,`tooltip-position`,`title-url`]))}})})),a8,HAt=r((()=>{VAt(),VAt(),a8=BAt})),UAt,WAt=r((()=>{UAt=y({__name:`cc-user-username-pure`,props:{clickBehavior:{},customUrl:{},username:{},variant:{default:`boldest`},size:{default:``},userProfileUrl:{default:``}},emits:[`log-action`],setup(e){let t=[`openProfile`,`openProfileInNewTab`],n=e,r=l(()=>t.includes(n.clickBehavior)?`a`:`div`),i=l(()=>t.includes(n.clickBehavior)?n.userProfileUrl:null),a=l(()=>n.clickBehavior===`openProfileInNewTab`?`_blank`:null),o=l(()=>{let e={};return n.clickBehavior===`badgeAsLink`&&(e.role=`button`,e.tabindex=0),e});return(t,n)=>(O(),d(ve(r.value),E(o.value,{class:[`cc-text-medium-bold`,[t.$style.component,t.$style[e.variant],t.$style[e.size]]],href:i.value,target:a.value,onClick:n[0]||=e=>t.$emit(`log-action`,{button:`nameClick`})}),{default:Me(()=>[h(Se(e.username),1)]),_:1},16,[`class`,`href`,`target`]))}})})),GAt,KAt,qAt=r((()=>{WAt(),WAt(),Zue(),He(),GAt={$style:Tl},KAt=Ve(UAt,[[`__cssModules`,GAt]])})),JAt,YAt=r((()=>{qAt(),$m(),JAt=y({__name:`cc-user-username`,props:{clickBehavior:{},customUrl:{},username:{},variant:{default:`boldest`},size:{default:``}},emits:[`log-action`],setup(e){let t=e,{routes:n}=
```

<a id="FND-30259"></a>
## FND-30259 — Implementation component cc-user-username

Vue compiled component __name declaration. Name suggests cc user username; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
=r((()=>{WAt(),WAt(),Zue(),He(),GAt={$style:Tl},KAt=Ve(UAt,[[`__cssModules`,GAt]])})),JAt,YAt=r((()=>{qAt(),$m(),JAt=y({__name:`cc-user-username`,props:{clickBehavior:{},customUrl:{},username:{},variant:{default:`boldest`},size:{default:``}},emits:[`log-action`],setup(e){let t=e,{routes:n}=Zm(),r=l(()=>t.customUrl||n.webMemberView(t.username));return(t,n)=>(O(),d(KAt,E(t.$attrs,{"click-behavior":e.clickBehavior,"custom-url":e.customUrl,username:e.username,variant:e.variant,size:e.size,"user-profile-url":r.value,onLogAction:n[0]||=e=>t.$emit(`log-action`,e)}),null,16,[`click-behavior`,`custom-url`,`username`,`variant`,`size`,`user-profile-url`]))}})})),o8,XAt=r((()=>{YAt(),YAt(),o8=JAt})),ZAt,QAt=r((()=>{gM(),dAt(),n8(),$m(),bAt(),SAt(),AAt(),PAt(),HAt(),XAt(),ZAt=y({__name:`cc-user-block`,props:{country:{},customUrl:{},flair:{},hideStrategy:{default:`default`},membership:{default:a_.basic},rating:{},clickBehavior:{default:`openProfile`},showPremiumBadge:{type:Boolean,default:!0},size:{default:`small`},title:{},tooltipPosition:{},username:{default:``},variant:{default:`default`}},emits:[`log-action`],setup(e){let t=e,{features:n,shouldShowMembershipBadges:r}=Zm(),i=ke(`root`),a=l(()=>t.membership??a_.b
```

<a id="FND-30260"></a>
## FND-30260 — Implementation component cc-user-block

Vue compiled component __name declaration. Name suggests cc user block; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
)),o8,XAt=r((()=>{YAt(),YAt(),o8=JAt})),ZAt,QAt=r((()=>{gM(),dAt(),n8(),$m(),bAt(),SAt(),AAt(),PAt(),HAt(),XAt(),ZAt=y({__name:`cc-user-block`,props:{country:{},customUrl:{},flair:{},hideStrategy:{default:`default`},membership:{default:a_.basic},rating:{},clickBehavior:{default:`openProfile`},showPremiumBadge:{type:Boolean,default:!0},size:{default:`small`},title:{},tooltipPosition:{},username:{default:``},variant:{default:`default`}},emits:[`log-action`],setup(e){let t=e,{features:n,shouldShowMembershipBadges:r}=Zm(),i=ke(`root`),a=l(()=>t.membership??a_.basic);vAt({isEnabled:()=>n.includes(`premium_badge_redesign`),membership:()=>a.value,root:i,strategy:()=>t.hideStrategy});let o=l(()=>t.showPremiumBadge&&xAt({hasTitle:!!t.title,isPremiumBadgeRedesign:n.includes(`premium_badge_redesign`),membership:a.value,showMembershipBadges:r()}));return(t,r)=>(O(),p(`div`,{ref_key:`root`,ref:i,class:D([`cc-user-block-component`,`cc-user-block-${e.variant}`,`cc-user-block-${e.size}`,{"cc-user-block-premium-badge-redesign":k(n).includes(`premium_badge_redesign`)}])},[e.title?(O(),d(a8,{key:0,"is-clickable":e.clickBehavior!==`none`&&e.clickBehavior!==`badgeAsLink`,size:e.size,title:e.title,"tooltip-position":e.tool
```

<a id="FND-30261"></a>
## FND-30261 — Implementation component svg-color-icon

Vue compiled component __name declaration. Name suggests svg color icon; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
h(),_e(t.$slots,`default`)],2))}})})),$At,ejt=r((()=>{QAt(),QAt(),$At=ZAt})),tjt,njt=r((()=>{tjt=y({name:`SvgColorIcon`,__name:`svg-color-icon`,props:{icon:{}},setup(e){return(t,n)=>(O(),p(`span`,{class:D([t.$style.icon,t.$style[e.icon]])},null,2))}})})),rjt,ijt,ajt=r((()=>{njt(),njt(),eve(),He(),rjt={$style:$_e},ijt=Ve(tjt,[[`__cssModules`,rjt]])})),ojt,sjt,cjt,ljt=r((()=>{NK(),ojt=[`textContent`],sjt=[`textContent`],cjt=y({__name:`animated-text`,props:{animatedText:{default:`...`},interval:{default:300},text:{}},setup(e){let t=e,n=me(t.text),r=me(0);function i(){n.value=`${t.text}${t.animatedText.substring(0,r.value)}`,r.value++,r.value>t.animatedText.length&&(r.value=0)}return Ae(()=>t.text,e=>{n.value=e}),lit(i,t.interval),(t,r)=>(O(),p(`div`,{class:D(t.$style.component)},[m(`span`,{class:D(t.$style.hidden),textContent:Se(`${e.text}${e.animatedText}`)},null,10,ojt),r[0]||=h(),m(`span`,{class:D(t.$style.visible),textContent:Se(n.value)},null,10,sjt)],2))}})})),ujt,s8,djt=r((()=>{ljt(),ljt(),O_e(),He(),ujt={$style:D_e},s8=Ve(cjt,[[`__cssModules`,ujt]])})),fjt,pjt=r((()=>{fjt=y({__name:`user-username`,props:{theme:{},isClickable:{type:Boolean,default:!0},url:{},username:{},openNewTab:{type:Boolean}},
```

<a id="FND-30262"></a>
## FND-30262 — Implementation component animated-text

Vue compiled component __name declaration. Name suggests animated text; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
:$_e},ijt=Ve(tjt,[[`__cssModules`,rjt]])})),ojt,sjt,cjt,ljt=r((()=>{NK(),ojt=[`textContent`],sjt=[`textContent`],cjt=y({__name:`animated-text`,props:{animatedText:{default:`...`},interval:{default:300},text:{}},setup(e){let t=e,n=me(t.text),r=me(0);function i(){n.value=`${t.text}${t.animatedText.substring(0,r.value)}`,r.value++,r.value>t.animatedText.length&&(r.value=0)}return Ae(()=>t.text,e=>{n.value=e}),lit(i,t.interval),(t,r)=>(O(),p(`div`,{class:D(t.$style.component)},[m(`span`,{class:D(t.$style.hidden),textContent:Se(`${e.text}${e.animatedText}`)},null,10,ojt),r[0]||=h(),m(`span`,{class:D(t.$style.visible),textContent:Se(n.value)},null,10,sjt)],2))}})})),ujt,s8,djt=r((()=>{ljt(),ljt(),O_e(),He(),ujt={$style:D_e},s8=Ve(cjt,[[`__cssModules`,ujt]])})),fjt,pjt=r((()=>{fjt=y({__name:`user-username`,props:{theme:{},isClickable:{type:Boolean,default:!0},url:{},username:{},openNewTab:{type:Boolean}},emits:[`log-action`],setup(e,{emit:t}){let n=e,r=l(()=>n.openNewTab?`_blank`:null);return(t,n)=>(O(),d(ve(e.isClickable?`a`:`span`),{class:D([t.$style.component,t.$style[e.theme],{[t.$style.link]:e.isClickable}]),href:e.isClickable?e.url:null,target:r.value,onClick:n[0]||=e=>t.$emit(`log-action`,{button:`nam
```

<a id="FND-30263"></a>
## FND-30263 — Implementation component user-username

Vue compiled component __name declaration. Name suggests user username; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
,ujt,s8,djt=r((()=>{ljt(),ljt(),O_e(),He(),ujt={$style:D_e},s8=Ve(cjt,[[`__cssModules`,ujt]])})),fjt,pjt=r((()=>{fjt=y({__name:`user-username`,props:{theme:{},isClickable:{type:Boolean,default:!0},url:{},username:{},openNewTab:{type:Boolean}},emits:[`log-action`],setup(e,{emit:t}){let n=e,r=l(()=>n.openNewTab?`_blank`:null);return(t,n)=>(O(),d(ve(e.isClickable?`a`:`span`),{class:D([t.$style.component,t.$style[e.theme],{[t.$style.link]:e.isClickable}]),href:e.isClickable?e.url:null,target:r.value,onClick:n[0]||=e=>t.$emit(`log-action`,{button:`nameClick`}),textContent:Se(e.username)},null,8,[`class`,`href`,`target`,`textContent`]))}})})),mjt,c8,hjt=r((()=>{pjt(),pjt(),Vue(),He(),mjt={$style:dc},c8=Ve(fjt,[[`__cssModules`,mjt]])})),gjt,_jt,vjt=r((()=>{Lkt(),hjt(),n8(),bg(),window.chesscom=window.chesscom||{},window.chesscom.routes=window.chesscom.routes||{},Object.assign(window.chesscom.routes,{web_member_titled_players:{tokens:[[`text`,`/members/titled-players`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_ES|et_EE|eu_ES|fa_
```

<a id="FND-30264"></a>
## FND-30264 — Implementation component user-tagline-compact

Vue compiled component __name declaration. Name suggests user tagline compact; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}}),gjt=[`textContent`],_jt=y({__name:`user-tagline-compact`,props:{country:{},flair:{},isSidebar:{type:Boolean},isTheatre:{type:Boolean},membership:{},rating:{},title:{},tooltipPosition:{},username:{}},setup(e){let t=e,n=Te(),r=l(()=>({[n.sidebar]:!!t.isSidebar,[n.theatre]:!!t.isTheatre})),i=yg.generate(`web_member_titled_players`),a=l(()=>(t.flair||t.membership)&&t.isTheatre),o=l(()=>t.rating&&t.isSidebar),s=l(()=>t.isTheatre?`medium`:`small`);return(t,c)=>(O(),p(`div`,{class:D(r.value)},[m(`div`,{class:D(k(n).row)},[e.title&&e.isSidebar?(O(),d(J6,{key:0,"open-new-tab":``,class:D(k(n).title),url:k(i),title:e.title,"tooltip-position":e.tooltipPosition},null,8,[`class`,`url`,`title`,`tooltip-position`])):f(``,!0),c[0]||=h(),g(c8,{theme:`dark`,class:D(k(n).username),username:e.username},null,8,[`class`,`username`])],2),c[4]||=h(),m(`div`,{class:D(k(n).row)},[e.country?(O(),d(t8,{key:0,size:s.value,code:e.country.code,name:e.country.name,"tooltip-position":e.tooltipPosition},null,8,[`size`,`code`,`name`,`tooltip-position`])):f(``,!0),c[1]||=h(),a.value?(O(),d(k(e.flair),{key:1,flair:e.flair,"membership-level":e.memb
```

<a id="FND-30265"></a>
## FND-30265 — Implementation component clock

Vue compiled component __name declaration. Name suggests clock; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
jt,bjt,xjt=r((()=>{vjt(),vjt(),C_e(),He(),yjt={$style:S_e},bjt=Ve(_jt,[[`__cssModules`,yjt]])})),Sjt,Cjt=r((()=>{Sjt=y({__name:`clock`,props:{playerIndex:{},playerToMove:{},position:{},isTheatreMode:{type:Boolean},isShortSidebar:{type:Boolean},isVerticalSidebar:{type:Boolean},isHorizontalSidebar:{type:Boolean},lowTime:{type:Boolean}},setup(e){let t=e,n=Te(),r=l(()=>({[n.component]:!0,[n.theatre]:!!t.isTheatreMode,[n.sidebar]:!!(t.isShortSidebar||t.isVerticalSidebar||t.isHorizontalSidebar),[n[`short-sidebar`]]:!!t.isShortSidebar,[n[`vertical-sidebar`]]:!!t.isVerticalSidebar,[n[`horizontal-sidebar`]]:!!t.isHorizontalSidebar,[n[t.position]]:!0,[n.white]:t.playerIndex===0,[n.black]:t.playerIndex===1,"clock-player-turn":t.playerIndex===t.playerToMove,"clock-low-time":t.lowTime}));return(e,t)=>(O(),p(`div`,{class:D(r.value)},[_e(e.$slots,`default`)],2))}})})),wjt,Tjt,Ejt=r((()=>{Cjt(),Cjt(),gge(),He(),wjt={$style:hge},Tjt=Ve(Sjt,[[`__cssModules`,wjt]])}));function Djt(e,t){return O(),p(`svg`,kjt,[...t[0]||=[m(`path`,{d:`M5.48,9a.93.93,0,0,0-.3.71v.58a.94.94,0,0,0,.3.71,1,1,0,0,0,.71.3h4.58a1,1,0,0,0,.71-.3.94.94,0,0,0,.29-.71V9.7A.92.92,0,0,0,11.48,9a1,1,0,0,0-.71-.27H6.19A1,1,0,0,0,5.48,9Z`},null,-1),m(`pa
```

<a id="FND-30266"></a>
## FND-30266 — Implementation component clock-icon

Vue compiled component __name declaration. Name suggests clock icon; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
width:`20`,height:`20`,viewBox:`0 0 20 20`},Ajt=Ve(Ojt,[[`render`,Djt]])})),Mjt,Njt=r((()=>{_E(),jjt(),cK(),Vf(),Mjt=y({__name:`clock-icon`,props:{isPaused:{type:Boolean},rotation:{}},setup(e){let t=e,n=l(()=>Lf(t.rotation)?{transform:`rotate(${t.rotation}deg)`}:null);return(t,r)=>(O(),p(`div`,{class:D(t.$style.icon)},[e.isPaused?(O(),d(sK,{key:0,class:D([`pause`,t.$style.pauseIcon]),is:k(VC),variant:`glyph`,size:20},null,8,[`class`,`is`])):(O(),d(Ajt,{key:1,style:ie(n.value),class:D(t.$style.timer)},null,8,[`style`,`class`]))],2))}})})),Pjt,Fjt,Ijt=r((()=>{Njt(),Njt(),ege(),He(),Pjt={$style:$he},Fjt=Ve(Mjt,[[`__cssModules`,Pjt]])})),Ljt,Rjt,zjt=r((()=>{Ljt=[`textContent`],Rjt=y({__name:`clock-time`,props:{clock:{},isText:{type:Boolean}},setup(e){let t=e,n=Te(),r=l(()=>t.isText?n.text:n.monospace);return(t,n)=>(O(),p(`span`,{class:D(r.value),textContent:Se(e.clock),role:`timer`},null,10,Ljt))}})})),Bjt,Vjt,Hjt=r((()=>{zjt(),zjt(),ige(),He(),Bjt={$style:rge},Vjt=Ve(Rjt,[[`__cssModules`,Bjt]])}));function l8(){let e=XN();return/^[0-9]+$/.test(e.params.move)?parseInt(e.params.move,10)-1:null}var u8=r((()=>{ZN()}));function Ujt(){if(!wX())return l8()??-1;let e=NG(),t=SX().board?.selectedNode;for(t=e?.game
```

<a id="FND-30267"></a>
## FND-30267 — Implementation component clock-time

Vue compiled component __name declaration. Name suggests clock time; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
,Njt(),ege(),He(),Pjt={$style:$he},Fjt=Ve(Mjt,[[`__cssModules`,Pjt]])})),Ljt,Rjt,zjt=r((()=>{Ljt=[`textContent`],Rjt=y({__name:`clock-time`,props:{clock:{},isText:{type:Boolean}},setup(e){let t=e,n=Te(),r=l(()=>t.isText?n.text:n.monospace);return(t,n)=>(O(),p(`span`,{class:D(r.value),textContent:Se(e.clock),role:`timer`},null,10,Ljt))}})})),Bjt,Vjt,Hjt=r((()=>{zjt(),zjt(),ige(),He(),Bjt={$style:rge},Vjt=Ve(Rjt,[[`__cssModules`,Bjt]])}));function l8(){let e=XN();return/^[0-9]+$/.test(e.params.move)?parseInt(e.params.move,10)-1:null}var u8=r((()=>{ZN()}));function Ujt(){if(!wX())return l8()??-1;let e=NG(),t=SX().board?.selectedNode;for(t=e?.game.getSelectedNode()??null;t?.ids.line;)t=e.game.getNodeByIds(t.previous);return t?.ply??0}var Wjt=r((()=>{PG(),TX(),CX(),u8()}));function Gjt(e){return e?!e.id&&e.type?e.type:`${e.type}-${e.id}`:rm.Blank}var Kjt=r((()=>{im()}));function d8(e){return SX().snapshots[Gjt(e)]||null}var f8=r((()=>{CX(),Kjt()}));function qjt(e){let t=e??UG();if(!t)return!0;if(D6(t)){if(!wX())return l8()===null;let e=NG(),t=SX().board?.isAtEndOfLine;return t=e?.game.isAtEndOfLine(),!!t}return!d8(t)?.selectedNode}var Jjt=r((()=>{PG(),f8(),TX(),CX(),u8(),WG(),O6()})),p8,m8=r((()=>{z(),p8=d
```

<a id="FND-30268"></a>
## FND-30268 — Implementation component cc-popover-wrapper

Vue compiled component __name declaration. Name suggests cc popover wrapper; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
ineSize,i.inlineSize,o.inlineSize),...t===`stretch`?{blockSize:n.blockSize}:{}}}var MRt,NRt=r((()=>{Qa(),NK(),MRt=Za(y({__name:`cc-popover-wrapper`,props:T({align:{default:`start`},autoClose:{type:Boolean,default:!0},id:{},placement:{default:`bottom`}},{modelValue:{type:Boolean},modelModifiers:{}}),emits:[`update:modelValue`],setup(e){let t=typeof document<`u`,n=me(!1);se(()=>{n.value=`anchorName`in document.documentElement.style});let r=Oe(e,`modelValue`),i=e,a=me(r.value??!1),o=me(r.value??!1),s=ke(`wrapper`),c=ke(`anchor`),u=`--${i.id}-anchor`,d={start:`span-end`,end:`span-start`,center:`center`,stretch:`center`},h={start:`span-bottom`,end:`span-top`,center:`center`,stretch:`center`},g=l(()=>{let e=d[i.align];switch(i.placement){case`top`:return`start ${e}`;case`left`:return`${h[i.align]} left`;case`right`:return`${h[i.align]} right`;default:return`end ${e}`}}),_=l(()=>i.placement===`top`||i.placement===`bottom`),v=l(()=>i.align===`stretch`&&_.value?`anchor-size(inline)`:`auto`),y=l(()=>i.align===`stretch`&&!_.value?`anchor-size(block)`:`auto`),b={bottom:{exit:{side:`block-start`,value:`-.4rem`},enter:{side:`block-start`,value:`-1rem`}},top:{exit:{side:`block-end`,value:`-.4rem`},enter:{side:`block
```

<a id="FND-30269"></a>
## FND-30269 — Implementation component cc-popover-wrapper-legacy

Vue compiled component __name declaration. Name suggests cc popover wrapper legacy; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
r-wrapper-enter":`cc-popover-wrapper-enter_ec31346`}}]])})),PRt=r((()=>{Gce(),NRt()})),FRt,IRt=r((()=>{NK(),Ud(),FRt=y({__name:`cc-popover-wrapper-legacy`,props:T({id:{},placement:{default:`bottom`},autoClose:{type:Boolean,default:!0},align:{default:`start`}},{modelValue:{type:Boolean},modelModifiers:{}}),emits:[`update:modelValue`],setup(e){let t=`anchorName`in document.documentElement.style,n=Oe(e,`modelValue`),r=e,i=me(n.value??!1),a=me(n.value??!1),o=ke(`wrapper`),s=ke(`anchor`),c=`--${r.id}-anchor`,u={start:`span-end`,end:`span-start`,center:`center`,stretch:`center`},d=l(()=>{let e=u[r.align];switch(r.placement){case`top`:return`start ${e}`;case`left`:return`${e} start`;case`right`:return`${e} end`;default:return`end ${e}`}}),g=l(()=>r.placement===`top`||r.placement===`bottom`),_=l(()=>r.align===`stretch`&&g.value?`anchor-size(inline)`:`auto`),v={bottom:{exit:{side:`block-start`,value:`-0.4rem`},enter:{side:`block-start`,value:`-1rem`}},top:{exit:{side:`block-end`,value:`-.4rem`},enter:{side:`block-end`,value:`-1rem`}},right:{exit:{side:`inline-start`,value:`-0.4rem`},enter:{side:`inline-start`,value:`-1rem`}},left:{exit:{side:`inline-end`,value:`-.4rem`},enter:{side:`inline-end`,value:`-1rem`}}
```

<a id="FND-30270"></a>
## FND-30270 — Implementation component cc-popover-wrapper

Vue compiled component __name declaration. Name suggests cc popover wrapper; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
=>{IRt(),IRt(),Gue(),He(),LRt={$style:Hc},RRt=Ve(FRt,[[`__cssModules`,LRt]])})),BRt,VRt=r((()=>{PRt(),$m(),zRt(),BRt=y({__name:`cc-popover-wrapper`,props:T({id:{},placement:{default:`bottom`},autoClose:{type:Boolean,default:!0},align:{default:`start`}},{modelValue:{type:Boolean},modelModifiers:{}}),emits:[`update:modelValue`],setup(e){let t=Oe(e,`modelValue`),{features:n}=Zm(),r=n.includes(`design_system_component_migration_cc_popover_wrapper`);function i(e,t){e.firstElementChild?.setAttribute(`data-cy`,`anchor-${t}`),e.querySelector(`:scope > [popover]`)?.setAttribute(`data-cy`,`popover-${t}`)}let a={mounted:(e,{value:t})=>i(e,t),updated:(e,{value:t})=>i(e,t)};return(n,i)=>Ne((O(),d(ve(k(r)?k(MRt):RRt),{modelValue:t.value,"onUpdate:modelValue":i[0]||=e=>t.value=e,id:e.id,placement:e.placement,align:e.align,"auto-close":e.autoClose},{trigger:Me(()=>[_e(n.$slots,`trigger`)]),popover:Me(()=>[_e(n.$slots,`popover`)]),_:3},8,[`modelValue`,`id`,`placement`,`align`,`auto-close`])),[[a,e.id]])}})})),U5,HRt=r((()=>{VRt(),VRt(),U5=BRt})),URt,WRt,GRt,KRt=r((()=>{oK(),HRt(),URt=[`textContent`],WRt=[`textContent`],GRt=y({__name:`cc-confirmation-popover`,props:{id:{},secondaryButtonProps:{},primaryButtonProps:{},t
```

<a id="FND-30271"></a>
## FND-30271 — Implementation component cc-confirmation-popover

Vue compiled component __name declaration. Name suggests cc confirmation popover; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
,U5,HRt=r((()=>{VRt(),VRt(),U5=BRt})),URt,WRt,GRt,KRt=r((()=>{oK(),HRt(),URt=[`textContent`],WRt=[`textContent`],GRt=y({__name:`cc-confirmation-popover`,props:{id:{},secondaryButtonProps:{},primaryButtonProps:{},title:{},description:{},placement:{default:`top`}},emits:[`cancel`,`confirm`],setup(e,{expose:t,emit:n}){let r=n,i=me(!1);function a(){i.value=!1,r(`cancel`)}function o(){i.value=!1,r(`confirm`)}return t({show:()=>{i.value=!0},hide:()=>{i.value=!1}}),(t,n)=>(O(),d(U5,{id:e.id,align:`center`,placement:e.placement,"auto-close":!1,modelValue:i.value,"onUpdate:modelValue":n[0]||=e=>i.value=e},{trigger:Me(()=>[_e(t.$slots,`trigger`)]),popover:Me(()=>[m(`div`,{class:D([t.$style.popover,`cc-popover-lighter`])},[m(`div`,{class:D(t.$style.content)},[m(`p`,{class:D([`cc-color-text-boldest`,`cc-text-medium-bold`,t.$style.title]),textContent:Se(e.title)},null,10,URt),n[1]||=h(),e.description?(O(),p(`p`,{key:0,class:D([`cc-color-text-default`,`cc-paragraph-medium`,t.$style.description]),textContent:Se(e.description)},null,10,WRt)):f(``,!0)],2),n[3]||=h(),m(`div`,{class:D(t.$style.buttons)},[g(aK,E({size:`medium`,"full-width":``},e.secondaryButtonProps,{onClick:a}),null,16),n[2]||=h(),g(aK,E({"full-width":`
```

<a id="FND-30272"></a>
## FND-30272 — Implementation component popup

Vue compiled component __name declaration. Name suggests popup; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
},W5=Ve(GRt,[[`__cssModules`,qRt]])})),JRt,YRt,XRt,ZRt=r((()=>{_E(),cK(),JRt=[`textContent`],YRt=[`textContent`],XRt=y({__name:`popup`,props:{body:{},position:{default:`left`},title:{}},emits:[`close`],setup(e,{emit:t}){let n=t;return(t,r)=>(O(),p(`div`,{class:D([t.$style.component,t.$style[e.position]]),onClick:r[1]||=Fe(()=>{},[`stop`])},[g(sK,{is:k(fC),variant:`glyph`,class:D(t.$style.close),size:16,onClick:r[0]||=e=>n(`close`,e)},null,8,[`is`,`class`]),r[2]||=h(),m(`div`,{class:D(t.$style.arrow)},null,2),r[3]||=h(),e.title?(O(),p(`strong`,{key:0,textContent:Se(e.title)},null,8,JRt)):f(``,!0),r[4]||=h(),e.body?(O(),p(`p`,{key:1,textContent:Se(e.body)},null,8,YRt)):f(``,!0)],2))}})})),QRt,K5,$Rt=r((()=>{ZRt(),ZRt(),F_e(),He(),QRt={$style:P_e},K5=Ve(XRt,[[`__cssModules`,QRt]])})),ezt,tzt,nzt,rzt,izt,azt=r((()=>{_E(),G5(),cK(),$Rt(),ezt=[`data-tab`,`onClick`],tzt=[`textContent`],nzt=[`aria-label`],rzt=[`aria-label`,`onClick`],izt=y({__name:`tabs`,props:{selectedTab:{},tabs:{}},emits:[`close-tab`,`select-tab`,`close-daily-games-popup`],setup(e,{emit:t}){let n=Te(),r=e,i=t;function a(e){return{[n.tab]:!0,[n.active]:r.selectedTab===e.id}}function o(e,t){e.target.closest(`.${n.close}`)||i(`select-tab`,{ta
```

<a id="FND-30273"></a>
## FND-30273 — Implementation component tabs

Vue compiled component __name declaration. Name suggests tabs; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
),G5(),cK(),$Rt(),ezt=[`data-tab`,`onClick`],tzt=[`textContent`],nzt=[`aria-label`],rzt=[`aria-label`,`onClick`],izt=y({__name:`tabs`,props:{selectedTab:{},tabs:{}},emits:[`close-tab`,`select-tab`,`close-daily-games-popup`],setup(e,{emit:t}){let n=Te(),r=e,i=t;function a(e){return{[n.tab]:!0,[n.active]:r.selectedTab===e.id}}function o(e,t){e.target.closest(`.${n.close}`)||i(`select-tab`,{tab:t})}function c(e){i(`close-tab`,{tab:e})}function l(e){return!!(r.selectedTab===e.id&&e.closable)}return(t,r)=>(O(),p(`div`,{role:`tablist`,class:D(k(n).component)},[(O(!0),p(s,null,ge(e.tabs,e=>(O(),p(`div`,{key:e.id,"data-tab":e.id,role:`tab`,tabindex:`0`,class:D(a(e)),onClick:t=>o(t,e)},[e.icon?(O(),d(sK,{key:0,is:e.icon,class:D(k(n).icon)},null,8,[`is`,`class`])):f(``,!0),r[2]||=h(),m(`span`,{class:D(k(n).label),textContent:Se(e.label)},null,10,tzt),r[3]||=h(),l(e)&&e.confirmClose?.active?(O(),d(W5,{key:1,id:`tab-close-confirmation-${e.id}`,placement:`bottom`,"primary-button-props":{label:t.$trans(`Yes`),variant:`danger`},"secondary-button-props":{label:t.$trans(`No`)},title:e.confirmClose.content,onClick:r[0]||=Fe(()=>{},[`stop`]),onConfirm:t=>c(e)},{trigger:Me(()=>[m(`button`,{type:`button`,"aria-label":t.$t
```

<a id="FND-30274"></a>
## FND-30274 — Implementation component loader-three-bounce

Vue compiled component __name declaration. Name suggests loader three bounce; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
,dzt={},fzt=Za(dzt,[[`render`,lzt],[`__cssModules`,{$style:uzt}]])})),mzt=r((()=>{Kce(),pzt()})),hzt,gzt=r((()=>{hzt=y({__name:`loader-three-bounce`,props:{isCircle:{type:Boolean,default:!1},size:{default:80}},setup(e){let t=e,n=l(()=>{let e=`${t.size*.25}px`;return{width:e,height:e}});return(t,r)=>(O(),p(`div`,{class:D([t.$style.component,{[t.$style.circle]:e.isCircle}]),style:ie({width:`${e.size*.75+20}px`}),"data-test-element":`loader-three-bounce`},[m(`div`,{class:D([t.$style.dot,t.$style.bounce1]),style:ie(n.value)},null,6),r[0]||=h(),m(`div`,{class:D([t.$style.dot,t.$style.bounce2]),style:ie(n.value)},null,6),r[1]||=h(),m(`div`,{class:D(t.$style.dot),style:ie(n.value)},null,6)],6))}})})),_zt,q5,vzt=r((()=>{gzt(),gzt(),kue(),He(),_zt={$style:ls},q5=Ve(hzt,[[`__cssModules`,_zt]])})),yzt,bzt=r((()=>{_E(),NK(),vzt(),cK(),yzt=y({__name:`tab-async-content`,props:{showError:{type:Boolean,default:!1},showBar:{default:0}},setup(e){let t=e,n=me(!1);function r(){n.value=!0}let{start:i,stop:a}=uit(r,200,{immediate:!1});return Ae(()=>t.showError,e=>{e?a():i()},{immediate:!0}),(t,r)=>(O(),p(`div`,{class:D(t.$style.component),style:ie({paddingTop:`${e.showBar}px`})},[e.showBar?(O(),p(`div`,{key:0,style:ie({hei
```

<a id="FND-30275"></a>
## FND-30275 — Implementation component tab-async-content

Vue compiled component __name declaration. Name suggests tab async content; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
gzt(),gzt(),kue(),He(),_zt={$style:ls},q5=Ve(hzt,[[`__cssModules`,_zt]])})),yzt,bzt=r((()=>{_E(),NK(),vzt(),cK(),yzt=y({__name:`tab-async-content`,props:{showError:{type:Boolean,default:!1},showBar:{default:0}},setup(e){let t=e,n=me(!1);function r(){n.value=!0}let{start:i,stop:a}=uit(r,200,{immediate:!1});return Ae(()=>t.showError,e=>{e?a():i()},{immediate:!0}),(t,r)=>(O(),p(`div`,{class:D(t.$style.component),style:ie({paddingTop:`${e.showBar}px`})},[e.showBar?(O(),p(`div`,{key:0,style:ie({height:`${e.showBar}px`}),class:D(t.$style.bar)},null,6)):f(``,!0),r[0]||=h(),e.showError?(O(),d(sK,{key:1,is:k(qy),variant:`glyph`,class:D(t.$style.error),size:48},null,8,[`is`,`class`])):f(``,!0),r[1]||=h(),n.value?(O(),d(q5,{key:2})):f(``,!0)],6))}})})),xzt,J5,Szt=r((()=>{bzt(),bzt(),ave(),He(),xzt={$style:ive},J5=Ve(yzt,[[`__cssModules`,xzt]])}));function Czt(e){return v({delay:0,loader:e,errorComponent:wzt,loadingComponent:J5})}var wzt,Tzt=r((()=>{Szt(),wzt=y({extends:J5,props:{showError:{type:Boolean,default:!0}}})})),Ezt,Dzt,Ozt=r((()=>{_E(),cK(),FK(),Ezt=[`for`],Dzt=y({__name:`custom-game-field`,props:{name:{default:``},help:{default:``},label:{default:``},vertical:{type:Boolean,default:!1}},setup(e){let t=e
```

<a id="FND-30276"></a>
## FND-30276 — Implementation component custom-game-field

Vue compiled component __name declaration. Name suggests custom game field; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
zt=y({extends:J5,props:{showError:{type:Boolean,default:!0}}})})),Ezt,Dzt,Ozt=r((()=>{_E(),cK(),FK(),Ezt=[`for`],Dzt=y({__name:`custom-game-field`,props:{name:{default:``},help:{default:``},label:{default:``},vertical:{type:Boolean,default:!1}},setup(e){let t=e,n=Te(),r=l(()=>({[n.component]:!0,[n.vertical]:t.vertical}));return(i,a)=>(O(),p(`div`,{class:D(r.value)},[e.label?(O(),p(`label`,{key:0,class:D({[k(n).vertical]:t.vertical}),for:e.name},[h(Se(e.label)+` `,1),e.help?(O(),p(`span`,{key:0,class:D(k(n).icon)},[g(sK,{is:k(rke),variant:`glyph`,size:16},null,8,[`is`]),a[0]||=h(),g(PK,{text:e.help},null,8,[`text`])],2)):f(``,!0)],10,Ezt)):f(``,!0),a[1]||=h(),_e(i.$slots,`default`)],2))}})})),kzt,Y5,Azt=r((()=>{Ozt(),Ozt(),Aue(),He(),kzt={$style:ps},Y5=Ve(Dzt,[[`__cssModules`,kzt]])})),jzt,Mzt,Nzt,Pzt=r((()=>{Qa(),jzt=[`aria-label`,`checked`,`disabled`,`id`,`name`],Mzt=[`for`],Nzt=Za(y({__name:`cc-switch`,props:T({ariaLabel:{},disabled:{type:Boolean},id:{default:()=>De()},name:{},preventOptimisticUpdates:{type:Boolean},size:{default:`large`},variant:{default:`primary`}},{modelValue:{type:Boolean,default:!1},modelModifiers:{}}),emits:[`update:modelValue`],setup(e){let t=e,n=Oe(e,`modelValue`);function r
```

<a id="FND-30277"></a>
## FND-30277 — Implementation component cc-switch

Vue compiled component __name declaration. Name suggests cc switch; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
dules`,kzt]])})),jzt,Mzt,Nzt,Pzt=r((()=>{Qa(),jzt=[`aria-label`,`checked`,`disabled`,`id`,`name`],Mzt=[`for`],Nzt=Za(y({__name:`cc-switch`,props:T({ariaLabel:{},disabled:{type:Boolean},id:{default:()=>De()},name:{},preventOptimisticUpdates:{type:Boolean},size:{default:`large`},variant:{default:`primary`}},{modelValue:{type:Boolean,default:!1},modelModifiers:{}}),emits:[`update:modelValue`],setup(e){let t=e,n=Oe(e,`modelValue`);function r(e){let r=e.target,i=r.checked;t.preventOptimisticUpdates&&(r.checked=n.value),n.value=i}return(t,i)=>(O(),p(`div`,{class:D([t.$style[`cc-switch-component`],t.$style[`cc-switch-${e.variant}`],e.size?t.$style[`cc-switch-${e.size}`]:null])},[m(`input`,{type:`checkbox`,"aria-label":e.ariaLabel,checked:n.value,class:D(t.$style[`cc-switch-checkbox`]),disabled:e.disabled,id:e.id,name:e.name,onChange:r},null,42,jzt),m(`label`,{class:D(t.$style[`cc-switch-label`]),for:e.id},[m(`div`,{class:D(t.$style[`cc-switch-button`])},[e.variant===`secondary`?(O(),p(`svg`,{key:0,viewBox:`0 0 90 90`,xmlns:`http://www.w3.org/2000/svg`,class:D(t.$style[`cc-switch-glyph`])},[m(`path`,{d:`m55.6 45 16.9-16.9a2 2 0 0 0 0-3L65 17.6a2 2 0 0 0-3 0L45 34.4 28.1 17.5a2 2 0 0 0-3 0L17.6 25a2 2 0 0 0 0 
```

<a id="FND-30278"></a>
## FND-30278 — Implementation component cc-switch-legacy

Vue compiled component __name declaration. Name suggests cc switch legacy; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
s:`cc-switch-button`},zzt={key:0,xmlns:`http://www.w3.org/2000/svg`,class:`cc-switch-glyph`,viewBox:`0 0 90 90`},Bzt=y({__name:`cc-switch-legacy`,props:T({ariaLabel:{},disabled:{type:Boolean},id:{default:De},name:{},preventOptimisticUpdates:{type:Boolean},size:{default:`large`},variant:{default:`primary`}},{modelValue:{type:Boolean,default:!1},modelModifiers:{}}),emits:[`update:modelValue`],setup(e){let t=e,n=Oe(e,`modelValue`);function r(e){let r=e.target,i=r.checked;t.preventOptimisticUpdates&&(r.checked=n.value),n.value=i}return(t,i)=>(O(),p(`div`,{class:D([`cc-switch-component`,`cc-switch-${e.variant}`,{[`cc-switch-${e.size}`]:e.size}])},[m(`input`,{type:`checkbox`,class:`cc-switch-checkbox`,"aria-label":e.ariaLabel,checked:n.value,disabled:e.disabled,id:e.id,name:e.name,onChange:r},null,40,Izt),i[1]||=h(),m(`label`,{class:`cc-switch-label`,for:e.id},[m(`div`,Rzt,[e.variant===`secondary`?(O(),p(`svg`,zzt,[...i[0]||=[m(`path`,{class:`cc-switch-glyph-correct`,d:`m55.6 45 16.9-16.9a2 2 0 0 0 0-3L65 17.6a2 2 0 0 0-3 0L45 34.4 28.1 17.5a2
            2 0 0 0-3 0L17.6 25a2 2 0 0 0 0 3l16.8 17-16.9 16.9a2 2 0 0 0 0 3l7.5 7.5a2 2 0 0
            0 3 0l17-16.9 16.8 17a2 2 0 0 0 3 0l7.6-7.6a2 2 0 0 0 0-3z`}
```

<a id="FND-30279"></a>
## FND-30279 — Implementation component cc-switch

Vue compiled component __name declaration. Name suggests cc switch; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
!0)])],8,Lzt)],2))}})})),Hzt,Uzt=r((()=>{Vzt(),Vzt(),Hzt=Bzt})),Wzt,Gzt=r((()=>{Fzt(),$m(),Uzt(),Wzt=y({inheritAttrs:!1,__name:`cc-switch`,setup(e){let t=Zm({optional:!0})?.features.includes(`design_system_component_migration_cc_switch`)??!1;return(e,n)=>k(t)?(O(),d(k(Nzt),re(E({key:0},e.$attrs)),null,16)):(O(),d(Hzt,re(E({key:1},e.$attrs)),null,16))}})})),X5,Kzt=r((()=>{Gzt(),Gzt(),X5=Wzt})),qzt,Jzt=r((()=>{Azt(),Kzt(),qzt=y({__name:`rated-switch`,props:{isRated:{type:Boolean}},emits:[`set-rated`],setup(e,{emit:t}){let n=t;function r(){n(`set-rated`)}return(t,n)=>(O(),d(Y5,{name:`rated-switch`,label:t.$trans(`Rated`)},{default:Me(()=>[g(X5,{id:`rated-switch`,"model-value":e.isRated,"onUpdate:modelValue":r},null,8,[`model-value`])]),_:1},8,[`label`]))}})})),Yzt,Xzt=r((()=>{Jzt(),Jzt(),Yzt=qzt})),Zzt,Qzt=r((()=>{Zzt=y({name:`SelectorButtonDropdown`,__name:`selector-button-dropdown`,setup(e){return(e,t)=>(O(),p(`div`,{class:D(e.$style.component)},[_e(e.$slots,`default`)],2))}})})),$zt,Z5,eBt=r((()=>{Qzt(),Qzt(),Mue(),He(),$zt={$style:_s},Z5=Ve(Zzt,[[`__cssModules`,$zt]])})),tBt,nBt,rBt=r((()=>{_E(),cK(),FK(),tBt=[`textContent`],nBt=y({__name:`selector-button-option`,props:{icon:{},isSelected:{type:Boole
```

<a id="FND-30280"></a>
## FND-30280 — Implementation component rated-switch

Vue compiled component __name declaration. Name suggests rated switch; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
),d(Hzt,re(E({key:1},e.$attrs)),null,16))}})})),X5,Kzt=r((()=>{Gzt(),Gzt(),X5=Wzt})),qzt,Jzt=r((()=>{Azt(),Kzt(),qzt=y({__name:`rated-switch`,props:{isRated:{type:Boolean}},emits:[`set-rated`],setup(e,{emit:t}){let n=t;function r(){n(`set-rated`)}return(t,n)=>(O(),d(Y5,{name:`rated-switch`,label:t.$trans(`Rated`)},{default:Me(()=>[g(X5,{id:`rated-switch`,"model-value":e.isRated,"onUpdate:modelValue":r},null,8,[`model-value`])]),_:1},8,[`label`]))}})})),Yzt,Xzt=r((()=>{Jzt(),Jzt(),Yzt=qzt})),Zzt,Qzt=r((()=>{Zzt=y({name:`SelectorButtonDropdown`,__name:`selector-button-dropdown`,setup(e){return(e,t)=>(O(),p(`div`,{class:D(e.$style.component)},[_e(e.$slots,`default`)],2))}})})),$zt,Z5,eBt=r((()=>{Qzt(),Qzt(),Mue(),He(),$zt={$style:_s},Z5=Ve(Zzt,[[`__cssModules`,$zt]])})),tBt,nBt,rBt=r((()=>{_E(),cK(),FK(),tBt=[`textContent`],nBt=y({__name:`selector-button-option`,props:{icon:{},isSelected:{type:Boolean,default:!1},label:{},showPopoutIcon:{type:Boolean,default:!1},tooltip:{default:``}},emits:[`click`],setup(e){return(t,n)=>(O(),p(`button`,{class:D({[t.$style.button]:!0,[t.$style.selected]:e.isSelected}),onClick:n[0]||=e=>t.$emit(`click`,e)},[g(sK,{variant:`glyph`,class:D([t.$style.icon,`glyph-colored`]),is
```

<a id="FND-30281"></a>
## FND-30281 — Implementation component selector-button-dropdown

Vue compiled component __name declaration. Name suggests selector button dropdown; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
]),_:1},8,[`label`]))}})})),Yzt,Xzt=r((()=>{Jzt(),Jzt(),Yzt=qzt})),Zzt,Qzt=r((()=>{Zzt=y({name:`SelectorButtonDropdown`,__name:`selector-button-dropdown`,setup(e){return(e,t)=>(O(),p(`div`,{class:D(e.$style.component)},[_e(e.$slots,`default`)],2))}})})),$zt,Z5,eBt=r((()=>{Qzt(),Qzt(),Mue(),He(),$zt={$style:_s},Z5=Ve(Zzt,[[`__cssModules`,$zt]])})),tBt,nBt,rBt=r((()=>{_E(),cK(),FK(),tBt=[`textContent`],nBt=y({__name:`selector-button-option`,props:{icon:{},isSelected:{type:Boolean,default:!1},label:{},showPopoutIcon:{type:Boolean,default:!1},tooltip:{default:``}},emits:[`click`],setup(e){return(t,n)=>(O(),p(`button`,{class:D({[t.$style.button]:!0,[t.$style.selected]:e.isSelected}),onClick:n[0]||=e=>t.$emit(`click`,e)},[g(sK,{variant:`glyph`,class:D([t.$style.icon,`glyph-colored`]),is:e.icon},null,8,[`class`,`is`]),n[2]||=h(),m(`span`,{class:D(t.$style.label),textContent:Se(e.label)},null,10,tBt),n[3]||=h(),e.showPopoutIcon?(O(),d(sK,{key:0,variant:`glyph`,is:k(LDe),size:12,class:D(t.$style.popout)},null,8,[`is`,`class`])):f(``,!0),n[4]||=h(),e.tooltip?(O(),p(`span`,{key:1,class:D(t.$style.help)},[g(sK,{variant:`glyph`,is:k(Jy),size:16},null,8,[`is`]),n[1]||=h(),g(PK,{position:`left`,text:e.tooltip},null,
```

<a id="FND-30282"></a>
## FND-30282 — Implementation component selector-button-option

Vue compiled component __name declaration. Name suggests selector button option; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
He(),$zt={$style:_s},Z5=Ve(Zzt,[[`__cssModules`,$zt]])})),tBt,nBt,rBt=r((()=>{_E(),cK(),FK(),tBt=[`textContent`],nBt=y({__name:`selector-button-option`,props:{icon:{},isSelected:{type:Boolean,default:!1},label:{},showPopoutIcon:{type:Boolean,default:!1},tooltip:{default:``}},emits:[`click`],setup(e){return(t,n)=>(O(),p(`button`,{class:D({[t.$style.button]:!0,[t.$style.selected]:e.isSelected}),onClick:n[0]||=e=>t.$emit(`click`,e)},[g(sK,{variant:`glyph`,class:D([t.$style.icon,`glyph-colored`]),is:e.icon},null,8,[`class`,`is`]),n[2]||=h(),m(`span`,{class:D(t.$style.label),textContent:Se(e.label)},null,10,tBt),n[3]||=h(),e.showPopoutIcon?(O(),d(sK,{key:0,variant:`glyph`,is:k(LDe),size:12,class:D(t.$style.popout)},null,8,[`is`,`class`])):f(``,!0),n[4]||=h(),e.tooltip?(O(),p(`span`,{key:1,class:D(t.$style.help)},[g(sK,{variant:`glyph`,is:k(Jy),size:16},null,8,[`is`]),n[1]||=h(),g(PK,{position:`left`,text:e.tooltip},null,8,[`text`])],2)):f(``,!0)],2))}})})),iBt,Q5,aBt=r((()=>{rBt(),rBt(),Nue(),He(),iBt={$style:ws},Q5=Ve(nBt,[[`__cssModules`,iBt]])})),oBt,sBt=r((()=>{_E(),eBt(),aBt(),Z2(),qd(),bg(),R(),window.chesscom=window.chesscom||{},window.chesscom.routes=window.chesscom.routes||{},Object.assign(window.
```

<a id="FND-30283"></a>
## FND-30283 — Implementation component game-type-selector-options

Vue compiled component __name declaration. Name suggests game type selector options; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
chach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]}}),oBt=y({__name:`game-type-selector-options`,props:{gameTypeOptions:{},selectedGameType:{default:`chess`},showExtraOptions:{type:Boolean,default:!1},tooltip:{default:``}},emits:[`select-game-type`],setup(e,{emit:t}){let n=e,r=t,i=[...Kd()?[{key:`bughouse`,value:`bughouse`,icon:Yb,label:L(`Bughouse`),tooltip:L(`Team up with another player and you can drop the pieces that they capture.`),route:X2()}]:[],{key:`threecheck`,value:`threecheck`,icon:lx,label:L(`3 Check`),tooltip:L(`First to check the other king 3 times wins.`),route:yg.generate(`web_chess_variants`,{variant:`3-check`},!0)},{key:`crazyhouse`,value:`crazyhouse`,icon:tx,label:L(`Crazyhouse`),tooltip:L(`When you capture a piece, you can drop it on your turn!`),route:yg.generate(`web_chess_variants`,{variant:`crazyhouse`},!0)},{key:`kingofthehill`,value:`kingofthehill`,icon:ox,label:L(`King of the Hill`),tooltip:L(`First to get king to middle 4 squares wins.`),route:yg.generate(`web_chess_variants`,{variant:`king-of-the-hill`},!0)},{key:`fourPlayerChess`,value:`fourPlayerChess`,label:L(`4 Player Chess`),icon:ix,tooltip:L(`Play 2 on 2 or 
```

<a id="FND-30284"></a>
## FND-30284 — Implementation component cc-dropdown-button

Vue compiled component __name declaration. Name suggests cc dropdown button; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
0)]),_:1}))}})})),cBt,lBt=r((()=>{sBt(),sBt(),cBt=oBt})),uBt,dBt,fBt=r((()=>{_E(),cK(),Uue(),uBt=[`textContent`],dBt=y({__name:`cc-dropdown-button`,props:{customClasses:{},align:{default:`center`},disabled:{type:Boolean},selected:{type:Boolean},fullWidth:{type:Boolean},href:{},icon:{},label:{},direction:{default:`down`},size:{default:`medium`},variant:{default:`secondary`}},setup(e){let t=e,n=l(()=>Sc[t.size]?.iconSize),r=l(()=>Sc[t.size]?.chevronSize),i={down:tDe,up:gDe,right:uDe},a=l(()=>!!t.disabled),o=l(()=>!!t.selected);return(t,s)=>(O(),d(ve(e.href?`a`:`button`),{class:D([`cc-dropdown-button-component`,`cc-dropdown-button-${e.size}`,`cc-dropdown-button-${e.variant}`,`cc-bg-${e.variant}`,{"cc-dropdown-button-selected":o.value},{"cc-dropdown-button-full":e.fullWidth}]),disabled:a.value,href:e.href||null,type:e.href?null:`button`},{default:Me(()=>[m(`div`,{class:D([`cc-dropdown-button-label-wrapper`,{"cc-dropdown-button-align-center":e.align===`center`}])},[e.icon?(O(),d(sK,{key:0,class:D([`cc-dropdown-button-icon`,e.customClasses?.icon]),is:e.icon.is,name:e.icon.name,size:n.value,variant:e.icon.variant},null,8,[`class`,`is`,`name`,`size`,`variant`])):f(``,!0),s[0]||=h(),e.label?(O(),p(`span`,{key:
```

<a id="FND-30285"></a>
## FND-30285 — Implementation component game-type-selector

Vue compiled component __name declaration. Name suggests game type selector; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
_:1},8,[`class`,`disabled`,`href`,`type`]))}})})),$5,e7=r((()=>{fBt(),fBt(),$5=dBt})),pBt,mBt=r((()=>{lBt(),e7(),pBt=y({__name:`game-type-selector`,props:{dropdownClass:{default:``},gameTypeOptions:{},isOpen:{type:Boolean,default:!1},selectedGameType:{default:`chess`},showExtraOptions:{type:Boolean,default:!1}},emits:[`select-game-type`,`click-game-type`],setup(e,{emit:t}){let n=e,r=t,i=l(()=>n.gameTypeOptions.find(e=>e.key===n.selectedGameType)||n.gameTypeOptions.find(e=>e.key===`chess`)||n.gameTypeOptions[0]);function a(){r(`click-game-type`)}return(t,n)=>(O(),p(`div`,null,[g($5,{"full-width":``,size:`x-large`,"custom-classes":{icon:`glyph-colored`},icon:{is:i.value.icon,variant:`glyph`},label:i.value.label,direction:e.isOpen?`up`:`down`,onClick:a},null,8,[`icon`,`label`,`direction`]),n[1]||=h(),e.isOpen?(O(),d(cBt,{key:0,class:D(e.dropdownClass),"show-extra-options":e.showExtraOptions,"selected-game-type":i.value.key,"game-type-options":e.gameTypeOptions,onSelectGameType:n[0]||=e=>t.$emit(`select-game-type`,e)},null,8,[`class`,`show-extra-options`,`selected-game-type`,`game-type-options`])):f(``,!0)]))}})})),hBt,gBt=r((()=>{mBt(),mBt(),hBt=pBt})),_Bt,vBt,yBt,bBt=r((()=>{_E(),cK(),_Bt=[`textContent`
```

<a id="FND-30286"></a>
## FND-30286 — Implementation component recent-time-section

Vue compiled component __name declaration. Name suggests recent time section; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
hBt,gBt=r((()=>{mBt(),mBt(),hBt=pBt})),_Bt,vBt,yBt,bBt=r((()=>{_E(),cK(),_Bt=[`textContent`],vBt=[`textContent`],yBt=y({__name:`recent-time-section`,props:{headerVisible:{type:Boolean},isPinned:{type:Boolean},isFocusMode:{type:Boolean}},emits:[`select-pin`],setup(e){let t=e,n=Te(),r=l(()=>({[n.component]:!0,[n[`focus-mode`]]:t.isFocusMode}));return(t,i)=>(O(),p(`div`,{class:D(r.value)},[e.headerVisible?(O(),p(`div`,{key:0,class:D(k(n).header)},[g(sK,{is:k(nT),variant:`glyph`,class:D(k(n)[`clock-icon`]),size:16},null,8,[`is`,`class`]),i[2]||=h(),m(`span`,{class:D(k(n).label),textContent:Se(t.$trans(`Recent`))},null,10,_Bt),i[3]||=h(),m(`div`,{class:D(k(n).pin),onClick:i[0]||=e=>t.$emit(`select-pin`)},[g(sK,{is:k(bAe),variant:`glyph`,size:16},null,8,[`is`]),i[1]||=h(),m(`span`,{textContent:Se(e.isPinned?t.$trans(`Unpin`):t.$trans(`Pin`))},null,8,vBt)],2)],2)):f(``,!0),i[4]||=h(),_e(t.$slots,`default`)],2))}})})),xBt,SBt,CBt=r((()=>{bBt(),bBt(),Pue(),He(),xBt={$style:js},SBt=Ve(yBt,[[`__cssModules`,xBt]])})),wBt,TBt=r((()=>{oK(),PA(),wBt=y({__name:`time-selector-button`,props:{timeControl:{},selectedTime:{},highlightSelected:{type:Boolean,default:!0},isLoading:{type:Boolean,default:!1}},emits:[`click`],s
```

<a id="FND-30287"></a>
## FND-30287 — Implementation component time-selector-button

Vue compiled component __name declaration. Name suggests time selector button; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
t=r((()=>{bBt(),bBt(),Pue(),He(),xBt={$style:js},SBt=Ve(yBt,[[`__cssModules`,xBt]])})),wBt,TBt=r((()=>{oK(),PA(),wBt=y({__name:`time-selector-button`,props:{timeControl:{},selectedTime:{},highlightSelected:{type:Boolean,default:!0},isLoading:{type:Boolean,default:!1}},emits:[`click`],setup(e){let t=e,n=l(()=>t.isLoading?``:NA(t.timeControl));return(t,r)=>(O(),d(aK,{class:D(t.$style.button),"is-one-line-text":``,size:`medium`,variant:`secondary`,loading:e.isLoading,label:n.value,"selected-border":e.highlightSelected&&e.timeControl.key===e.selectedTime.key,onClick:r[0]||=e=>t.$emit(`click`,e)},null,8,[`class`,`loading`,`label`,`selected-border`]))}})})),EBt,t7,DBt=r((()=>{TBt(),TBt(),Fue(),He(),EBt={$style:Ns},t7=Ve(wBt,[[`__cssModules`,EBt]])}));function OBt(e,t){return O(),p(`div`,{class:D(e.$style.component)},[_e(e.$slots,`default`)],2)}var kBt,ABt,n7,jBt=r((()=>{Lue(),He(),kBt={},ABt={$style:Rs},n7=Ve(kBt,[[`render`,OBt],[`__cssModules`,ABt]])})),MBt,NBt=r((()=>{CBt(),DBt(),jBt(),MBt=y({__name:`recent-time-category`,props:{selectedTime:{},timeControls:{},isPinned:{type:Boolean},headerVisible:{type:Boolean},isFocusMode:{type:Boolean}},emits:[`select-time`,`select-pin`],setup(e,{emit:t}){let n=t;funct
```

<a id="FND-30288"></a>
## FND-30288 — Implementation component recent-time-category

Vue compiled component __name declaration. Name suggests recent time category; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
e(),kBt={},ABt={$style:Rs},n7=Ve(kBt,[[`render`,OBt],[`__cssModules`,ABt]])})),MBt,NBt=r((()=>{CBt(),DBt(),jBt(),MBt=y({__name:`recent-time-category`,props:{selectedTime:{},timeControls:{},isPinned:{type:Boolean},headerVisible:{type:Boolean},isFocusMode:{type:Boolean}},emits:[`select-time`,`select-pin`],setup(e,{emit:t}){let n=t;function r(e){n(`select-time`,{time:e})}return(t,n)=>(O(),d(SBt,{"header-visible":e.headerVisible,"is-pinned":e.isPinned,onSelectPin:n[0]||=e=>t.$emit(`select-pin`)},{default:Me(()=>[g(n7,null,{default:Me(()=>[(O(!0),p(s,null,ge(e.timeControls,(t,n)=>(O(),d(t7,{key:t.key||n,"time-control":t,"selected-time":e.selectedTime,"is-loading":t.timeType===`none`,onClick:e=>r(t)},null,8,[`time-control`,`selected-time`,`is-loading`,`onClick`]))),128))]),_:1})]),_:1},8,[`header-visible`,`is-pinned`]))}})})),r7,PBt=r((()=>{NBt(),NBt(),r7=MBt})),FBt,IBt=r((()=>{e7(),FBt=y({__name:`toggle-custom-game`,props:{isOpen:{type:Boolean},label:{}},emits:[`click`],setup(e){return(t,n)=>(O(),p(`div`,{class:D(t.$style.component)},[g($5,{size:`medium`,variant:`ghost`,label:e.label,direction:e.isOpen?`up`:`down`,onClick:n[0]||=e=>t.$emit(`click`,e)},null,8,[`label`,`direction`])],2))}})})),LBt,RBt,zBt=r(
```

<a id="FND-30289"></a>
## FND-30289 — Implementation component toggle-custom-game

Vue compiled component __name declaration. Name suggests toggle custom game; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
,_:1})]),_:1},8,[`header-visible`,`is-pinned`]))}})})),r7,PBt=r((()=>{NBt(),NBt(),r7=MBt})),FBt,IBt=r((()=>{e7(),FBt=y({__name:`toggle-custom-game`,props:{isOpen:{type:Boolean},label:{}},emits:[`click`],setup(e){return(t,n)=>(O(),p(`div`,{class:D(t.$style.component)},[g($5,{size:`medium`,variant:`ghost`,label:e.label,direction:e.isOpen?`up`:`down`,onClick:n[0]||=e=>t.$emit(`click`,e)},null,8,[`label`,`direction`])],2))}})})),LBt,RBt,zBt=r((()=>{IBt(),IBt(),jue(),He(),LBt={$style:hs},RBt=Ve(FBt,[[`__cssModules`,LBt]])})),BBt,VBt,HBt=r((()=>{_E(),cK(),FK(),BBt=[`textContent`],VBt=y({__name:`time-selector-section`,props:{icon:{},label:{},isFocusMode:{type:Boolean},tooltipText:{}},setup(e){return(t,n)=>(O(),p(`div`,{class:D({[t.$style.component]:!0,[t.$style[`focus-mode`]]:e.isFocusMode})},[m(`div`,{class:D(t.$style.header)},[g(sK,{variant:`glyph`,class:D([t.$style.icon,`glyph-colored`]),is:e.icon,size:16},null,8,[`class`,`is`]),n[1]||=h(),m(`span`,{class:D(t.$style.label),textContent:Se(e.label)},null,10,BBt),n[2]||=h(),e.tooltipText?(O(),p(`span`,{key:0,class:D(t.$style.info)},[g(sK,{variant:`glyph`,is:k(Jy),size:16},null,8,[`is`]),n[0]||=h(),g(PK,{text:e.tooltipText},null,8,[`text`])],2)):f(``,!0)],2),
```

<a id="FND-30290"></a>
## FND-30290 — Implementation component time-selector-section

Vue compiled component __name declaration. Name suggests time selector section; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
e(),LBt={$style:hs},RBt=Ve(FBt,[[`__cssModules`,LBt]])})),BBt,VBt,HBt=r((()=>{_E(),cK(),FK(),BBt=[`textContent`],VBt=y({__name:`time-selector-section`,props:{icon:{},label:{},isFocusMode:{type:Boolean},tooltipText:{}},setup(e){return(t,n)=>(O(),p(`div`,{class:D({[t.$style.component]:!0,[t.$style[`focus-mode`]]:e.isFocusMode})},[m(`div`,{class:D(t.$style.header)},[g(sK,{variant:`glyph`,class:D([t.$style.icon,`glyph-colored`]),is:e.icon,size:16},null,8,[`class`,`is`]),n[1]||=h(),m(`span`,{class:D(t.$style.label),textContent:Se(e.label)},null,10,BBt),n[2]||=h(),e.tooltipText?(O(),p(`span`,{key:0,class:D(t.$style.info)},[g(sK,{variant:`glyph`,is:k(Jy),size:16},null,8,[`is`]),n[0]||=h(),g(PK,{text:e.tooltipText},null,8,[`text`])],2)):f(``,!0)],2),n[3]||=h(),_e(t.$slots,`default`)],2))}})})),UBt,i7,WBt=r((()=>{HBt(),HBt(),Rue(),He(),UBt={$style:Gs},i7=Ve(VBt,[[`__cssModules`,UBt]])})),GBt,KBt=r((()=>{DBt(),jBt(),WBt(),GBt=y({__name:`time-selector-category`,props:{icon:{},isFocusMode:{type:Boolean,default:!1},label:{default:``},selectedTime:{},timeControls:{},tooltipText:{}},emits:[`select-time`],setup(e,{emit:t}){let n=t;function r(e){n(`select-time`,{time:e})}return(t,n)=>(O(),d(i7,{icon:e.icon,label:e.lab
```

<a id="FND-30291"></a>
## FND-30291 — Implementation component time-selector-category

Vue compiled component __name declaration. Name suggests time selector category; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
=>{HBt(),HBt(),Rue(),He(),UBt={$style:Gs},i7=Ve(VBt,[[`__cssModules`,UBt]])})),GBt,KBt=r((()=>{DBt(),jBt(),WBt(),GBt=y({__name:`time-selector-category`,props:{icon:{},isFocusMode:{type:Boolean,default:!1},label:{default:``},selectedTime:{},timeControls:{},tooltipText:{}},emits:[`select-time`],setup(e,{emit:t}){let n=t;function r(e){n(`select-time`,{time:e})}return(t,n)=>(O(),d(i7,{icon:e.icon,label:e.label,"is-focus-mode":e.isFocusMode,"tooltip-text":e.tooltipText},{default:Me(()=>[g(n7,null,{default:Me(()=>[(O(!0),p(s,null,ge(e.timeControls,t=>(O(),d(t7,{key:t.key,"time-control":t,"selected-time":e.selectedTime,onClick:e=>r(t)},null,8,[`time-control`,`selected-time`,`onClick`]))),128))]),_:1})]),_:1},8,[`icon`,`label`,`is-focus-mode`,`tooltip-text`]))}})})),a7,qBt=r((()=>{KBt(),KBt(),a7=GBt})),JBt,o7,YBt=r((()=>{Qa(),JBt=[`aria-label`,`type`,`value`],o7=Za(y({__name:`cc-input`,props:T({ariaLabel:{},autofocus:{type:Boolean},hasError:{type:Boolean},hasWarning:{type:Boolean},showSpinButtons:{type:Boolean},size:{default:`medium`},type:{default:`text`},variant:{default:`default`}},{modelValue:{default:``},modelModifiers:{}}),emits:T([`blur`,`change`,`enter`,`focus`,`keydown`,`keyup`,`paste`],[`update:mode
```

<a id="FND-30292"></a>
## FND-30292 — Implementation component cc-input

Vue compiled component __name declaration. Name suggests cc input; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
-text`]))}})})),a7,qBt=r((()=>{KBt(),KBt(),a7=GBt})),JBt,o7,YBt=r((()=>{Qa(),JBt=[`aria-label`,`type`,`value`],o7=Za(y({__name:`cc-input`,props:T({ariaLabel:{},autofocus:{type:Boolean},hasError:{type:Boolean},hasWarning:{type:Boolean},showSpinButtons:{type:Boolean},size:{default:`medium`},type:{default:`text`},variant:{default:`default`}},{modelValue:{default:``},modelModifiers:{}}),emits:T([`blur`,`change`,`enter`,`focus`,`keydown`,`keyup`,`paste`],[`update:modelValue`]),setup(e){let t=e,n=Oe(e,`modelValue`),r=ke(`inputEl`);se(()=>{t.autofocus&&requestAnimationFrame(()=>{r.value?.focus()})});function i(e){let r=e.target;if(t.type===`number`){n.value=r.value===``||Number.isNaN(r.valueAsNumber)?null:r.valueAsNumber;return}n.value=r.value}function a(e){t.type===`number`&&e.target.blur()}return(t,o)=>(O(),p(`input`,{ref_key:`inputEl`,ref:r,"aria-label":e.ariaLabel,class:D([t.$style[`cc-input-component`],t.$style[`cc-input-${e.size}`],{[t.$style[`cc-input-error`]]:e.hasError,[t.$style[`cc-input-warning`]]:e.hasWarning,[t.$style[`cc-input-ghost`]]:e.variant===`ghost`,[t.$style[`cc-input-spin-buttons`]]:e.showSpinButtons}]),type:e.type,value:n.value,onBlur:o[0]||=e=>t.$emit(`blur`,e),onChange:o[1]||=e=>t.$e
```

<a id="FND-30293"></a>
## FND-30293 — Implementation component cc-input

Vue compiled component __name declaration. Name suggests cc input; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
`}}]])})),XBt=r((()=>{Uce(),YBt()})),ZBt,QBt,$Bt=r((()=>{XBt(),$m(),ZBt=[`aria-label`,`type`,`readonly`,`value`],QBt=y({__name:`cc-input`,props:{ariaLabel:{},autofocus:{type:Boolean},hasError:{type:Boolean},hasWarning:{type:Boolean},modelValue:{default:``},readonly:{type:Boolean,default:!1},showSpinButtons:{type:Boolean},size:{default:`medium`},type:{default:`text`}},emits:[`blur`,`change`,`enter`,`focus`,`keydown`,`keyup`,`paste`,`update:modelValue`],setup(e,{emit:t}){let n=e,r=t,{features:i}=Zm(),a=i.includes(`design_system_component_migration_cc_input`),o=ke(`inputEl`);se(()=>{n.autofocus&&!a&&requestAnimationFrame(()=>{o.value?.focus()})});let s=e=>r(`keyup`,e),c=()=>void 0,l=e=>r(`update:modelValue`,e.target.value),u=e=>{n.type===`number`&&e.target.blur()};return(t,n)=>k(a)?(O(),d(k(o7),{key:0,"aria-label":e.ariaLabel,autofocus:e.autofocus,class:D([`cc-input-component`,`cc-input-published`,`cc-input-${e.size}`,{"cc-input-error":e.hasError,"cc-input-warning":e.hasWarning,"cc-input-spin-buttons":e.showSpinButtons}]),"has-error":e.hasError,"has-warning":e.hasWarning,"model-value":e.modelValue,readonly:e.readonly,"show-spin-buttons":e.showSpinButtons,size:e.size,type:e.type,onBlur:n[0]||=e=>t.$emit(`
```

<a id="FND-30294"></a>
## FND-30294 — Implementation component time-selector-custom

Vue compiled component __name declaration. Name suggests time selector custom; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
),onWheel:u},null,42,ZBt))}})})),s7,eVt=r((()=>{$Bt(),$Bt(),s7=QBt})),tVt,nVt=r((()=>{_E(),WBt(),oK(),eVt(),FK(),tVt=y({__name:`time-selector-custom`,props:{baseSeconds:{},baseTime:{},timeIncrement:{},isFocusMode:{type:Boolean}},emits:[`submit`,`input-base-seconds`,`input-base-time`,`input-time-increment`],setup(e,{emit:t}){let n=t;function r(e,t){switch(e){case`base-time`:n(`input-base-time`,{value:Math.floor(Number(t))});break;case`base-seconds`:n(`input-base-seconds`,{value:Math.floor(Number(t))});break;case`time-increment`:n(`input-time-increment`,{value:Math.round(Number(t)*10)/10});break;default:break}}function i(e){[`0`,`1`,`2`,`3`,`4`,`5`,`6`,`7`,`8`,`9`,`ArrowLeft`,`ArrowRight`,`Backspace`,`Clear`,`Delete`,`Tab`].includes(e.key)||e.preventDefault()}return(t,n)=>(O(),d(i7,{icon:k(xMe),"is-focus-mode":e.isFocusMode,label:t.$trans(`Custom`)},{default:Me(()=>[m(`form`,{class:D(t.$style.component),onSubmit:n[3]||=Fe(e=>t.$emit(`submit`),[`prevent`])},[g(s7,{type:`number`,"model-value":e.baseTime,placeholder:t.$trans(`min`),onKeydown:i,"onUpdate:modelValue":n[0]||=e=>r(`base-time`,e)},null,8,[`model-value`,`placeholder`]),n[4]||=h(),g(PK,{"for-previous-element":``,text:t.$trans(`Minutes`)},null,8,[
```

<a id="FND-30295"></a>
## FND-30295 — Implementation component time-selector-options

Vue compiled component __name declaration. Name suggests time selector options; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
t={$style:Is},iVt=Ve(tVt,[[`__cssModules`,rVt]])})),oVt,sVt=r((()=>{_E(),zBt(),PBt(),qBt(),aVt(),Zst(),Mf(),EA(),oVt=y({__name:`time-selector-options`,props:{isFocusMode:{type:Boolean,default:!1},isGuest:{type:Boolean,default:!1},isLoggedIn:{type:Boolean,default:!1},selectedTime:{},recentTimeControls:{},isRecentTimeControlsPinned:{type:Boolean,default:!1},timeOptionsOverride:{}},emits:[`select-time`,`click-recent-time-controls-pin`],setup(e,{emit:t}){let n=e,r=t,i=me(null),a=me(null),o=me(null),s=me(!1),c=[`60`,`60|1`,`120|1`,`180`,`180|2`,`300`,`600`,`600|5`,`900|10`,`1d`,`3d`,`7d`],u=[...Xst,...IJ],m=l(()=>{let e=n.timeOptionsOverride??c;return(s.value?u:e).map(jf)}),_=l(()=>!!(n.isLoggedIn&&!n.isGuest)),v=l(()=>!!(n.recentTimeControls&&n.recentTimeControls.length>2));function y(e){return m.value.filter(t=>OPe(t)===e)}function b(){s.value=!s.value}function x(){r(`click-recent-time-controls-pin`)}function S({value:e}){i.value=e}function C({value:e}){a.value=e}function w({value:e}){o.value=e}function ee(e){r(`select-time`,e)}function te(){let e=(a.value||0)*60+(i.value||0);if(e>=10){let t=jf({baseTime:e,timeIncrement:o.value||0,timeType:`live`});t.isCustom=!0,r(`select-time`,{time:t})}}return(t,n)=>(O
```

<a id="FND-30296"></a>
## FND-30296 — Implementation component play-button

Vue compiled component __name declaration. Name suggests play button; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
),_q()}));function fVt(e,t=2e3){return ait(e,t)}var pVt=r((()=>{NK()})),mVt,hVt=r((()=>{pVt(),oK(),G5(),FK(),R(),mVt=y({__name:`play-button`,props:{buttonClass:{},disabled:{type:Boolean,default:!1},disabledTooltip:{},fullWidth:{type:Boolean,default:!1},size:{},label:{default:L(`Play`)},variant:{default:`primary`},minutesUntilShutdown:{default:0},requireTournamentConfirmation:{type:Boolean,default:!1},requireShutdownConfirmation:{type:Boolean,default:!1},showConfirmationAboveButton:{type:Boolean,default:!1}},emits:[`click-play`],setup(e,{emit:t}){let n=e,r=t,i=ke(`confirmationPopover`),a=l(()=>n.requireShutdownConfirmation?lg(`{0} Server is restarting NOW. Any ongoing games are aborted when restarts happen. Are you sure you want to start game?|{1}Server is restarting in 1 minute. Any ongoing games are aborted when restarts happen. Are you sure you want to start game?|]1,Inf]Server is restarting in %minutes% minutes. Any ongoing games are aborted when restarts happen. Are you sure you want to start game?`,n.minutesUntilShutdown,{"%minutes%":n.minutesUntilShutdown}):n.requireTournamentConfirmation?L(`Seeking games outside of the tournament could interrupt ongoing tournament games. Are you sure?`):null),o
```

<a id="FND-30297"></a>
## FND-30297 — Implementation component live-stats

Vue compiled component __name declaration. Name suggests live stats; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
Vt(),gVt=mVt})),vVt,yVt,bVt,xVt,SVt=r((()=>{_E(),LK(),R(),vVt=[`aria-label`],yVt=[`innerHTML`],bVt=[`innerHTML`],xVt=y({__name:`live-stats`,props:{gamesCount:{},isLoggedIn:{type:Boolean},playersCount:{}},emits:[`click-console`,`click-stats`],setup(e){let t=e,n=l(()=>lg(`{0} <strong>0</strong> Playing|{1} <strong>1</strong> Playing|]1,Inf] <strong>%1$s%</strong> Playing`,t.playersCount,{"%1$s%":t.playersCount.toLocaleString()})),r=l(()=>lg(`{0} <strong>0</strong> Games Today|{1} <strong>1</strong> Game Today|]1,Inf] <strong>%1$s%</strong> Games Today`,t.gamesCount,{"%1$s%":t.gamesCount.toLocaleString()}));return(t,i)=>(O(),p(`div`,{class:D(t.$style.component)},[e.isLoggedIn?(O(),d(IK,{key:0,"aria-label":t.$trans(`Console`),class:D(t.$style.icon),icon:{is:k(AMe),variant:`glyph`},onClick:i[0]||=e=>t.$emit(`click-console`)},null,8,[`aria-label`,`class`,`icon`])):f(``,!0),i[3]||=h(),e.gamesCount&&e.playersCount?(O(),p(`button`,{key:1,type:`button`,"aria-label":t.$trans(`Watch games`),class:D(t.$style.text),onClick:i[1]||=e=>t.$emit(`click-stats`)},[m(`span`,{class:D(t.$style.stat),innerHTML:n.value},null,10,yVt),i[2]||=h(),m(`span`,{class:D(t.$style.stat),innerHTML:r.value},null,10,bVt)],10,vVt)):f(``,!0)]
```

<a id="FND-30298"></a>
## FND-30298 — Implementation component live-stats

Vue compiled component __name declaration. Name suggests live stats; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
Vf(),DVt(),l7(),HG()})),AVt,jVt=r((()=>{$G(),U3(),sut(),Zg(),TVt(),X3(),l6(),d6(),L6(),E6(),kVt(),l7(),um(),fm(),AVt=y({__name:`live-stats`,setup(e){let t=out({gamesCount(){return qg()&&window.chesscom.statsGames||0},playersCount(){return qg()&&window.chesscom.statsMembersOnline||0},isLoggedIn(){return MM()}});async function n(){if(!MM()||Qf()){H3();return}if(await u6(),c6()){Y3();return}OVt(c7().Console.key)}function r(){T6(dm.Games),I6(lm.Watch)}return(e,i)=>(O(),d(wVt,{"games-count":k(t).gamesCount,"is-logged-in":k(t).isLoggedIn,"players-count":k(t).playersCount,onClickConsole:n,onClickStats:r},null,8,[`games-count`,`is-logged-in`,`players-count`]))}})})),MVt,NVt=r((()=>{jVt(),jVt(),MVt=AVt})),u7,PVt=r((()=>{I(),_E(),z(),bN(),pf(),bg(),R(),op(),im(),window.chesscom=window.chesscom||{},window.chesscom.routes=window.chesscom.routes||{},Object.assign(window.chesscom.routes,{web_play_daily_team_match_challenge:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/daily-team/seek`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajedrez|fr|scacchi|sakk|schaken|szachy)?(\\.)?[^\\s]+`,_locale:`af_ZA|ar_AR|az_AZ|be_BY|bg_BG|bn_BD|bs_BA|ca|cs_CZ|da_DK|de_DE|el_GR|en_US|es_
```

<a id="FND-30299"></a>
## FND-30299 — Implementation component coach-settings-header

Vue compiled component __name declaration. Name suggests coach settings header; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0781
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
n L(`Turn on Play Sounds in your settings to hear Coach`)}var yUt=r((()=>{R()})),bUt,xUt=r((()=>{_E(),yUt(),LK(),bUt=y({__name:`coach-settings-header`,props:{audioToggle:{}},emits:[`close`,`toggleAudio`],setup(e){let t=vUt();return(n,r)=>(O(),p(`div`,{class:D(n.$style.component)},[e.audioToggle?(O(),d(IK,{key:0,size:`large`,"aria-label":n.$trans(`Toggle Coach Audio`),class:D(n.$style[`audio-toggle`]),disabled:e.audioToggle.isMutedByPlaySounds,icon:{is:e.audioToggle.isAudible?k(IC):k(NC),variant:`glyph`},"icon-size":16,tooltip:e.audioToggle.isMutedByPlaySounds?{text:k(t),position:`bottom`,anchor:`left`}:void 0,onClick:r[0]||=e=>n.$emit(`toggleAudio`)},null,8,[`aria-label`,`class`,`disabled`,`icon`,`tooltip`])):f(``,!0),r[2]||=h(),m(`h2`,{class:D([`cc-heading-x-small-bold`,n.$style.title])},[_e(n.$slots,`default`)],2),r[3]||=h(),g(IK,{size:`large`,"aria-label":n.$trans(`Close`),class:D(n.$style.close),icon:{is:k(fC),variant:`glyph`},"icon-size":16,onClick:r[1]||=e=>n.$emit(`close`)},null,8,[`aria-label`,`class`,`icon`])],2))}})})),SUt,CUt,wUt=r((()=>{xUt(),xUt(),bde(),He(),SUt={$style:yde},CUt=Ve(bUt,[[`__cssModules`,SUt]])})),TUt,EUt=r((()=>{NK(),wUt(),oK(),TUt=y({__name:`coach-settings-content`,props:
```
