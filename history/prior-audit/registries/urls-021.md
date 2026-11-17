# URL and reference inventory

[Master index](../00_MASTER_INDEX.md)

## URL-01001

`/daily-chess/seek`

- Type: page_or_route_candidate; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20132](../findings/url_references-011.md#FND-20132).

### SRC-0781 at character 13411

```text
s:[],schemes:[`https`]},web_daily_seek:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/daily-chess/seek`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-0781 at character 459506

```text
s:[],schemes:[`https`]},web_daily_seek:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/daily-chess/seek`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

## URL-01002

`/daily-team/seek`

- Type: page_or_route_candidate; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20133](../findings/url_references-011.md#FND-20133).

### SRC-0781 at character 14159

```text
]},web_play_daily_team_match_challenge:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/daily-team/seek`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-0781 at character 36436

```text
8n_web_play_daily_team_match_challenge:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/daily-team/seek`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

### SRC-0781 at character 460254

```text
]},web_play_daily_team_match_challenge:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/daily-team/seek`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-0781 at character 482531

```text
8n_web_play_daily_team_match_challenge:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/daily-team/seek`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

### SRC-0781 at character 2962669

```text
s,{web_play_daily_team_match_challenge:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/daily-team/seek`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-0781 at character 2963421

```text
8n_web_play_daily_team_match_challenge:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/daily-team/seek`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

## URL-01003

`/daily/match-seek/get`

- Type: page_or_route_candidate; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20134](../findings/url_references-011.md#FND-20134).

### SRC-0145 at character 181

```text
ct.assign(window.chesscom.routes,{web_club_callback_team_match_seek_view:{tokens:[[`text`,`/daily/match-seek/get`],[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/club`]],defaults:{host:`www.chess-d
```

### SRC-0145 at character 9560

```text
ct.assign(window.chesscom.routes,{web_club_callback_team_match_seek_view:{tokens:[[`text`,`/daily/match-seek/get`],[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/callback/club`]],defaults:{host:`www.chess-d
```

## URL-01004

`/decline-challenge`

- Type: page_or_route_candidate; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20135](../findings/url_references-011.md#FND-20135).

### SRC-0781 at character 103032

```text
],methods:[],schemes:[`https`]},web_game_seek_callback_decline_challenge:{tokens:[[`text`,`/decline-challenge`],[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/game_seek`]],defaults:{host:`www.ches
```

### SRC-0781 at character 2598329

```text
.assign(window.chesscom.routes,{web_game_seek_callback_decline_challenge:{tokens:[[`text`,`/decline-challenge`],[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/game_seek`]],defaults:{host:`www.ches
```

## URL-01005

`/decline-draw`

- Type: page_or_route_candidate; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20136](../findings/url_references-011.md#FND-20136).

### SRC-0781 at character 92426

```text
,!0]],methods:[`POST`],schemes:[`https`]},web_game_callback_decline_draw:{tokens:[[`text`,`/decline-draw`],[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/game`]],defaults:{host:`www.chess-dev
```

### SRC-0781 at character 2155913

```text
|{},Object.assign(window.chesscom.routes,{web_game_callback_decline_draw:{tokens:[[`text`,`/decline-draw`],[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/game`]],defaults:{host:`www.chess-dev
```

## URL-01006

`/delete-challenge`

- Type: page_or_route_candidate; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20137](../findings/url_references-011.md#FND-20137).

### SRC-0781 at character 119700

```text
]],methods:[],schemes:[`https`]},web_game_seek_callback_delete_challenge:{tokens:[[`text`,`/delete-challenge`],[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/game_seek`]],defaults:{host:`www.ches
```

### SRC-0781 at character 3224722

```text
t.assign(window.chesscom.routes,{web_game_seek_callback_delete_challenge:{tokens:[[`text`,`/delete-challenge`],[`variable`,`/`,`\\d+`,`id`,!0],[`text`,`/callback/game_seek`]],defaults:{host:`www.ches
```

## URL-01007

`/details`

- Type: page_or_route_candidate; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20138](../findings/url_references-011.md#FND-20138).

### SRC-1137 at character 77185

```text
ods:[`POST`],schemes:[`https`]},web_library_callback_update_lucg_details:{tokens:[[`text`,`/details`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/lucgs`]],defaults:{host:`
```

### SRC-1137 at character 1910772

```text
ods:[`POST`],schemes:[`https`]},web_library_callback_update_lucg_details:{tokens:[[`text`,`/details`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/lucgs`]],defaults:{host:`
```

### SRC-1165 at character 77185

```text
ods:[`POST`],schemes:[`https`]},web_library_callback_update_lucg_details:{tokens:[[`text`,`/details`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/lucgs`]],defaults:{host:`
```

### SRC-1165 at character 1910772

```text
ods:[`POST`],schemes:[`https`]},web_library_callback_update_lucg_details:{tokens:[[`text`,`/details`],[`variable`,`/`,`[^/]++`,`uuid`,!0],[`text`,`/callback/library/lucgs`]],defaults:{host:`
```

## URL-01008

`/dev`

- Type: page_or_route_candidate; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20139](../findings/url_references-011.md#FND-20139).

### SRC-0014 at character 49681

```text
dir("/tmp"),FS.mkdir("/home"),FS.mkdir("/home/web_user")},createDefaultDevices(){FS.mkdir("/dev"),FS.registerDevice(FS.makedev(1,3),{read:()=>0,write:(stream,buffer,offset,length,pos)=>l
```

### SRC-0014 at character 50197

```text
omBuffer),randomLeft=randomBuffer.byteLength),randomBuffer[--randomLeft]);FS.createDevice("/dev","random",randomByte),FS.createDevice("/dev","urandom",randomByte),FS.mkdir("/dev/shm"),FS
```

### SRC-0014 at character 50241

```text
),randomBuffer[--randomLeft]);FS.createDevice("/dev","random",randomByte),FS.createDevice("/dev","urandom",randomByte),FS.mkdir("/dev/shm"),FS.mkdir("/dev/shm/tmp")},createSpecialDirecto
```

### SRC-0014 at character 50929

```text
de}},{},"/proc/self/fd")},createStandardStreams(input,output,error){input?FS.createDevice("/dev","stdin",input):FS.symlink("/dev/tty","/dev/stdin"),output?FS.createDevice("/dev","stdout"
```

### SRC-0014 at character 51010

```text
teDevice("/dev","stdin",input):FS.symlink("/dev/tty","/dev/stdin"),output?FS.createDevice("/dev","stdout",null,output):FS.symlink("/dev/tty","/dev/stdout"),error?FS.createDevice("/dev","
```

### SRC-0014 at character 51098

```text
e("/dev","stdout",null,output):FS.symlink("/dev/tty","/dev/stdout"),error?FS.createDevice("/dev","stderr",null,error):FS.symlink("/dev/tty1","/dev/stderr");FS.open("/dev/stdin",0),FS.ope
```

### SRC-0031 at character 49681

```text
dir("/tmp"),FS.mkdir("/home"),FS.mkdir("/home/web_user")},createDefaultDevices(){FS.mkdir("/dev"),FS.registerDevice(FS.makedev(1,3),{read:()=>0,write:(stream,buffer,offset,length,pos)=>l
```

### SRC-0031 at character 50197

```text
omBuffer),randomLeft=randomBuffer.byteLength),randomBuffer[--randomLeft]);FS.createDevice("/dev","random",randomByte),FS.createDevice("/dev","urandom",randomByte),FS.mkdir("/dev/shm"),FS
```

### SRC-0031 at character 50241

```text
),randomBuffer[--randomLeft]);FS.createDevice("/dev","random",randomByte),FS.createDevice("/dev","urandom",randomByte),FS.mkdir("/dev/shm"),FS.mkdir("/dev/shm/tmp")},createSpecialDirecto
```

### SRC-0031 at character 50929

```text
de}},{},"/proc/self/fd")},createStandardStreams(input,output,error){input?FS.createDevice("/dev","stdin",input):FS.symlink("/dev/tty","/dev/stdin"),output?FS.createDevice("/dev","stdout"
```

### SRC-0031 at character 51010

```text
teDevice("/dev","stdin",input):FS.symlink("/dev/tty","/dev/stdin"),output?FS.createDevice("/dev","stdout",null,output):FS.symlink("/dev/tty","/dev/stdout"),error?FS.createDevice("/dev","
```

### SRC-0031 at character 51098

```text
e("/dev","stdout",null,output):FS.symlink("/dev/tty","/dev/stdout"),error?FS.createDevice("/dev","stderr",null,error):FS.symlink("/dev/tty1","/dev/stderr");FS.open("/dev/stdin",0),FS.ope
```

### SRC-0032 at character 49681

```text
dir("/tmp"),FS.mkdir("/home"),FS.mkdir("/home/web_user")},createDefaultDevices(){FS.mkdir("/dev"),FS.registerDevice(FS.makedev(1,3),{read:()=>0,write:(stream,buffer,offset,length,pos)=>l
```

### SRC-0032 at character 50197

```text
omBuffer),randomLeft=randomBuffer.byteLength),randomBuffer[--randomLeft]);FS.createDevice("/dev","random",randomByte),FS.createDevice("/dev","urandom",randomByte),FS.mkdir("/dev/shm"),FS
```

### SRC-0032 at character 50241

```text
),randomBuffer[--randomLeft]);FS.createDevice("/dev","random",randomByte),FS.createDevice("/dev","urandom",randomByte),FS.mkdir("/dev/shm"),FS.mkdir("/dev/shm/tmp")},createSpecialDirecto
```

### SRC-0032 at character 50929

```text
de}},{},"/proc/self/fd")},createStandardStreams(input,output,error){input?FS.createDevice("/dev","stdin",input):FS.symlink("/dev/tty","/dev/stdin"),output?FS.createDevice("/dev","stdout"
```

### SRC-0032 at character 51010

```text
teDevice("/dev","stdin",input):FS.symlink("/dev/tty","/dev/stdin"),output?FS.createDevice("/dev","stdout",null,output):FS.symlink("/dev/tty","/dev/stdout"),error?FS.createDevice("/dev","
```

### SRC-0032 at character 51098

```text
e("/dev","stdout",null,output):FS.symlink("/dev/tty","/dev/stdout"),error?FS.createDevice("/dev","stderr",null,error):FS.symlink("/dev/tty1","/dev/stderr");FS.open("/dev/stdin",0),FS.ope
```

### SRC-0072 at character 49681

```text
dir("/tmp"),FS.mkdir("/home"),FS.mkdir("/home/web_user")},createDefaultDevices(){FS.mkdir("/dev"),FS.registerDevice(FS.makedev(1,3),{read:()=>0,write:(stream,buffer,offset,length,pos)=>l
```

### SRC-0072 at character 50197

```text
omBuffer),randomLeft=randomBuffer.byteLength),randomBuffer[--randomLeft]);FS.createDevice("/dev","random",randomByte),FS.createDevice("/dev","urandom",randomByte),FS.mkdir("/dev/shm"),FS
```

### SRC-0072 at character 50241

```text
),randomBuffer[--randomLeft]);FS.createDevice("/dev","random",randomByte),FS.createDevice("/dev","urandom",randomByte),FS.mkdir("/dev/shm"),FS.mkdir("/dev/shm/tmp")},createSpecialDirecto
```

### SRC-0072 at character 50929

```text
de}},{},"/proc/self/fd")},createStandardStreams(input,output,error){input?FS.createDevice("/dev","stdin",input):FS.symlink("/dev/tty","/dev/stdin"),output?FS.createDevice("/dev","stdout"
```

### SRC-0072 at character 51010

```text
teDevice("/dev","stdin",input):FS.symlink("/dev/tty","/dev/stdin"),output?FS.createDevice("/dev","stdout",null,output):FS.symlink("/dev/tty","/dev/stdout"),error?FS.createDevice("/dev","
```

### SRC-0072 at character 51098

```text
e("/dev","stdout",null,output):FS.symlink("/dev/tty","/dev/stdout"),error?FS.createDevice("/dev","stderr",null,error):FS.symlink("/dev/tty1","/dev/stderr");FS.open("/dev/stdin",0),FS.ope
```

### SRC-0123 at character 49681

```text
dir("/tmp"),FS.mkdir("/home"),FS.mkdir("/home/web_user")},createDefaultDevices(){FS.mkdir("/dev"),FS.registerDevice(FS.makedev(1,3),{read:()=>0,write:(stream,buffer,offset,length,pos)=>l
```

### SRC-0123 at character 50197

```text
omBuffer),randomLeft=randomBuffer.byteLength),randomBuffer[--randomLeft]);FS.createDevice("/dev","random",randomByte),FS.createDevice("/dev","urandom",randomByte),FS.mkdir("/dev/shm"),FS
```

### SRC-0123 at character 50241

```text
),randomBuffer[--randomLeft]);FS.createDevice("/dev","random",randomByte),FS.createDevice("/dev","urandom",randomByte),FS.mkdir("/dev/shm"),FS.mkdir("/dev/shm/tmp")},createSpecialDirecto
```

### SRC-0123 at character 50929

```text
de}},{},"/proc/self/fd")},createStandardStreams(input,output,error){input?FS.createDevice("/dev","stdin",input):FS.symlink("/dev/tty","/dev/stdin"),output?FS.createDevice("/dev","stdout"
```

### SRC-0123 at character 51010

```text
teDevice("/dev","stdin",input):FS.symlink("/dev/tty","/dev/stdin"),output?FS.createDevice("/dev","stdout",null,output):FS.symlink("/dev/tty","/dev/stdout"),error?FS.createDevice("/dev","
```

### SRC-0123 at character 51098

```text
e("/dev","stdout",null,output):FS.symlink("/dev/tty","/dev/stdout"),error?FS.createDevice("/dev","stderr",null,error):FS.symlink("/dev/tty1","/dev/stderr");FS.open("/dev/stdin",0),FS.ope
```

### SRC-0781 at character 3081214

```text
>`}),Ke=Array(4096),ct(Be,`/`),ut(`/tmp`),ut(`/home`),ut(`/home/web_user`),(function(){ut(`/dev`),st(259,{read:()=>0,write:(e,t,n,r)=>r}),dt(`/dev/null`,259),A(1280,Le),A(1536,Re),dt(`/d
```

### SRC-1160 at character 49681

```text
dir("/tmp"),FS.mkdir("/home"),FS.mkdir("/home/web_user")},createDefaultDevices(){FS.mkdir("/dev"),FS.registerDevice(FS.makedev(1,3),{read:()=>0,write:(stream,buffer,offset,length,pos)=>l
```

### SRC-1160 at character 50197

```text
omBuffer),randomLeft=randomBuffer.byteLength),randomBuffer[--randomLeft]);FS.createDevice("/dev","random",randomByte),FS.createDevice("/dev","urandom",randomByte),FS.mkdir("/dev/shm"),FS
```

### SRC-1160 at character 50241

```text
),randomBuffer[--randomLeft]);FS.createDevice("/dev","random",randomByte),FS.createDevice("/dev","urandom",randomByte),FS.mkdir("/dev/shm"),FS.mkdir("/dev/shm/tmp")},createSpecialDirecto
```

### SRC-1160 at character 50929

```text
de}},{},"/proc/self/fd")},createStandardStreams(input,output,error){input?FS.createDevice("/dev","stdin",input):FS.symlink("/dev/tty","/dev/stdin"),output?FS.createDevice("/dev","stdout"
```

### SRC-1160 at character 51010

```text
teDevice("/dev","stdin",input):FS.symlink("/dev/tty","/dev/stdin"),output?FS.createDevice("/dev","stdout",null,output):FS.symlink("/dev/tty","/dev/stdout"),error?FS.createDevice("/dev","
```

### SRC-1160 at character 51098

```text
e("/dev","stdout",null,output):FS.symlink("/dev/tty","/dev/stdout"),error?FS.createDevice("/dev","stderr",null,error):FS.symlink("/dev/tty1","/dev/stderr");FS.open("/dev/stdin",0),FS.ope
```

## URL-01009

`/dev/`

- Type: page_or_route_candidate; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20140](../findings/url_references-011.md#FND-20140).

### SRC-0781 at character 3064119

```text
=1&&n!=2)throw new Je(28);e.position=e.m.ba(e,t,n),e.oc=[]}var gt;function _t(e,t,n){e=we(`/dev/`+e);var r=Ve(!!t,!!n);vt||=64;var i=vt++<<8|0;st(i,{open(e){e.seekable=!1},close(){n?.buff
```

## URL-01010

`/dev/null`

- Type: page_or_route_candidate; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20141](../findings/url_references-011.md#FND-20141).

### SRC-0014 at character 49807

```text
(1,3),{read:()=>0,write:(stream,buffer,offset,length,pos)=>length,llseek:()=>0}),FS.mkdev("/dev/null",FS.makedev(1,3)),TTY.register(FS.makedev(5,0),TTY.default_tty_ops),TTY.register(FS.makede
```

### SRC-0031 at character 49807

```text
(1,3),{read:()=>0,write:(stream,buffer,offset,length,pos)=>length,llseek:()=>0}),FS.mkdev("/dev/null",FS.makedev(1,3)),TTY.register(FS.makedev(5,0),TTY.default_tty_ops),TTY.register(FS.makede
```

### SRC-0032 at character 49807

```text
(1,3),{read:()=>0,write:(stream,buffer,offset,length,pos)=>length,llseek:()=>0}),FS.mkdev("/dev/null",FS.makedev(1,3)),TTY.register(FS.makedev(5,0),TTY.default_tty_ops),TTY.register(FS.makede
```

### SRC-0072 at character 49807

```text
(1,3),{read:()=>0,write:(stream,buffer,offset,length,pos)=>length,llseek:()=>0}),FS.mkdev("/dev/null",FS.makedev(1,3)),TTY.register(FS.makedev(5,0),TTY.default_tty_ops),TTY.register(FS.makede
```

### SRC-0123 at character 49807

```text
(1,3),{read:()=>0,write:(stream,buffer,offset,length,pos)=>length,llseek:()=>0}),FS.mkdev("/dev/null",FS.makedev(1,3)),TTY.register(FS.makedev(5,0),TTY.default_tty_ops),TTY.register(FS.makede
```

### SRC-0781 at character 3081265

```text
`),ut(`/home/web_user`),(function(){ut(`/dev`),st(259,{read:()=>0,write:(e,t,n,r)=>r}),dt(`/dev/null`,259),A(1280,Le),A(1536,Re),dt(`/dev/tty`,1280),dt(`/dev/tty1`,1536);var e=new Uint8Array(
```

### SRC-1160 at character 49807

```text
(1,3),{read:()=>0,write:(stream,buffer,offset,length,pos)=>length,llseek:()=>0}),FS.mkdev("/dev/null",FS.makedev(1,3)),TTY.register(FS.makedev(5,0),TTY.default_tty_ops),TTY.register(FS.makede
```

## URL-01011

`/dev/shm`

- Type: page_or_route_candidate; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20142](../findings/url_references-011.md#FND-20142).

### SRC-0014 at character 50279

```text
eDevice("/dev","random",randomByte),FS.createDevice("/dev","urandom",randomByte),FS.mkdir("/dev/shm"),FS.mkdir("/dev/shm/tmp")},createSpecialDirectories(){FS.mkdir("/proc");var proc_self=FS.
```

### SRC-0031 at character 50279

```text
eDevice("/dev","random",randomByte),FS.createDevice("/dev","urandom",randomByte),FS.mkdir("/dev/shm"),FS.mkdir("/dev/shm/tmp")},createSpecialDirectories(){FS.mkdir("/proc");var proc_self=FS.
```

### SRC-0032 at character 50279

```text
eDevice("/dev","random",randomByte),FS.createDevice("/dev","urandom",randomByte),FS.mkdir("/dev/shm"),FS.mkdir("/dev/shm/tmp")},createSpecialDirectories(){FS.mkdir("/proc");var proc_self=FS.
```

### SRC-0072 at character 50279

```text
eDevice("/dev","random",randomByte),FS.createDevice("/dev","urandom",randomByte),FS.mkdir("/dev/shm"),FS.mkdir("/dev/shm/tmp")},createSpecialDirectories(){FS.mkdir("/proc");var proc_self=FS.
```

### SRC-0123 at character 50279

```text
eDevice("/dev","random",randomByte),FS.createDevice("/dev","urandom",randomByte),FS.mkdir("/dev/shm"),FS.mkdir("/dev/shm/tmp")},createSpecialDirectories(){FS.mkdir("/proc");var proc_self=FS.
```

### SRC-0781 at character 3081453

```text
ay(1024),t=0,n=()=>(t===0&&(t=De(e).byteLength),e[--t]);_t(`random`,n),_t(`urandom`,n),ut(`/dev/shm`),ut(`/dev/shm/tmp`)})(),(function(){ut(`/proc`);var e=ut(`/proc/self`);ut(`/proc/self/fd`
```

### SRC-1160 at character 50279

```text
eDevice("/dev","random",randomByte),FS.createDevice("/dev","urandom",randomByte),FS.mkdir("/dev/shm"),FS.mkdir("/dev/shm/tmp")},createSpecialDirectories(){FS.mkdir("/proc");var proc_self=FS.
```

## URL-01012

`/dev/shm/tmp`

- Type: page_or_route_candidate; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20143](../findings/url_references-011.md#FND-20143).

### SRC-0014 at character 50300

```text
m",randomByte),FS.createDevice("/dev","urandom",randomByte),FS.mkdir("/dev/shm"),FS.mkdir("/dev/shm/tmp")},createSpecialDirectories(){FS.mkdir("/proc");var proc_self=FS.mkdir("/proc/self");FS.mk
```

### SRC-0031 at character 50300

```text
m",randomByte),FS.createDevice("/dev","urandom",randomByte),FS.mkdir("/dev/shm"),FS.mkdir("/dev/shm/tmp")},createSpecialDirectories(){FS.mkdir("/proc");var proc_self=FS.mkdir("/proc/self");FS.mk
```

### SRC-0032 at character 50300

```text
m",randomByte),FS.createDevice("/dev","urandom",randomByte),FS.mkdir("/dev/shm"),FS.mkdir("/dev/shm/tmp")},createSpecialDirectories(){FS.mkdir("/proc");var proc_self=FS.mkdir("/proc/self");FS.mk
```

### SRC-0072 at character 50300

```text
m",randomByte),FS.createDevice("/dev","urandom",randomByte),FS.mkdir("/dev/shm"),FS.mkdir("/dev/shm/tmp")},createSpecialDirectories(){FS.mkdir("/proc");var proc_self=FS.mkdir("/proc/self");FS.mk
```

### SRC-0123 at character 50300

```text
m",randomByte),FS.createDevice("/dev","urandom",randomByte),FS.mkdir("/dev/shm"),FS.mkdir("/dev/shm/tmp")},createSpecialDirectories(){FS.mkdir("/proc");var proc_self=FS.mkdir("/proc/self");FS.mk
```

### SRC-0781 at character 3081468

```text
()=>(t===0&&(t=De(e).byteLength),e[--t]);_t(`random`,n),_t(`urandom`,n),ut(`/dev/shm`),ut(`/dev/shm/tmp`)})(),(function(){ut(`/proc`);var e=ut(`/proc/self`);ut(`/proc/self/fd`),ct({U(){var t=N(e
```

### SRC-1160 at character 50300

```text
m",randomByte),FS.createDevice("/dev","urandom",randomByte),FS.mkdir("/dev/shm"),FS.mkdir("/dev/shm/tmp")},createSpecialDirectories(){FS.mkdir("/proc");var proc_self=FS.mkdir("/proc/self");FS.mk
```

## URL-01013

`/dev/stderr`

- Type: page_or_route_candidate; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20144](../findings/url_references-011.md#FND-20144).

### SRC-0014 at character 51149

```text
","/dev/stdout"),error?FS.createDevice("/dev","stderr",null,error):FS.symlink("/dev/tty1","/dev/stderr");FS.open("/dev/stdin",0),FS.open("/dev/stdout",1),FS.open("/dev/stderr",1)},staticInit(){
```

### SRC-0014 at character 51221

```text
mlink("/dev/tty1","/dev/stderr");FS.open("/dev/stdin",0),FS.open("/dev/stdout",1),FS.open("/dev/stderr",1)},staticInit(){FS.nameTable=new Array(4096),FS.mount(MEMFS,{},"/"),FS.createDefaultDire
```

### SRC-0031 at character 51149

```text
","/dev/stdout"),error?FS.createDevice("/dev","stderr",null,error):FS.symlink("/dev/tty1","/dev/stderr");FS.open("/dev/stdin",0),FS.open("/dev/stdout",1),FS.open("/dev/stderr",1)},staticInit(){
```

### SRC-0031 at character 51221

```text
mlink("/dev/tty1","/dev/stderr");FS.open("/dev/stdin",0),FS.open("/dev/stdout",1),FS.open("/dev/stderr",1)},staticInit(){FS.nameTable=new Array(4096),FS.mount(MEMFS,{},"/"),FS.createDefaultDire
```

### SRC-0032 at character 51149

```text
","/dev/stdout"),error?FS.createDevice("/dev","stderr",null,error):FS.symlink("/dev/tty1","/dev/stderr");FS.open("/dev/stdin",0),FS.open("/dev/stdout",1),FS.open("/dev/stderr",1)},staticInit(){
```

### SRC-0032 at character 51221

```text
mlink("/dev/tty1","/dev/stderr");FS.open("/dev/stdin",0),FS.open("/dev/stdout",1),FS.open("/dev/stderr",1)},staticInit(){FS.nameTable=new Array(4096),FS.mount(MEMFS,{},"/"),FS.createDefaultDire
```

### SRC-0072 at character 51149

```text
","/dev/stdout"),error?FS.createDevice("/dev","stderr",null,error):FS.symlink("/dev/tty1","/dev/stderr");FS.open("/dev/stdin",0),FS.open("/dev/stdout",1),FS.open("/dev/stderr",1)},staticInit(){
```

### SRC-0072 at character 51221

```text
mlink("/dev/tty1","/dev/stderr");FS.open("/dev/stdin",0),FS.open("/dev/stdout",1),FS.open("/dev/stderr",1)},staticInit(){FS.nameTable=new Array(4096),FS.mount(MEMFS,{},"/"),FS.createDefaultDire
```

### SRC-0123 at character 51149

```text
","/dev/stdout"),error?FS.createDevice("/dev","stderr",null,error):FS.symlink("/dev/tty1","/dev/stderr");FS.open("/dev/stdin",0),FS.open("/dev/stdout",1),FS.open("/dev/stderr",1)},staticInit(){
```

### SRC-0123 at character 51221

```text
mlink("/dev/tty1","/dev/stderr");FS.open("/dev/stdin",0),FS.open("/dev/stdout",1),FS.open("/dev/stderr",1)},staticInit(){FS.nameTable=new Array(4096),FS.mount(MEMFS,{},"/"),FS.createDefaultDire
```

### SRC-0781 at character 3111971

```text
r.stdout):ft(`/dev/tty`,`/dev/stdout`),r.stderr?_t(`stderr`,null,r.stderr):ft(`/dev/tty1`,`/dev/stderr`),mt(`/dev/stdin`,0),mt(`/dev/stdout`,1),mt(`/dev/stderr`,1)),qe=!1,xe(ae),i(r),r.onRuntim
```

### SRC-0781 at character 3112028

```text
r`,null,r.stderr):ft(`/dev/tty1`,`/dev/stderr`),mt(`/dev/stdin`,0),mt(`/dev/stdout`,1),mt(`/dev/stderr`,1)),qe=!1,xe(ae),i(r),r.onRuntimeInitialized&&r.onRuntimeInitialized(),r.postRun)for(type
```

### SRC-1160 at character 51149

```text
","/dev/stdout"),error?FS.createDevice("/dev","stderr",null,error):FS.symlink("/dev/tty1","/dev/stderr");FS.open("/dev/stdin",0),FS.open("/dev/stdout",1),FS.open("/dev/stderr",1)},staticInit(){
```

### SRC-1160 at character 51221

```text
mlink("/dev/tty1","/dev/stderr");FS.open("/dev/stdin",0),FS.open("/dev/stdout",1),FS.open("/dev/stderr",1)},staticInit(){FS.nameTable=new Array(4096),FS.mount(MEMFS,{},"/"),FS.createDefaultDire
```

## URL-01014

`/dev/stdin`

- Type: page_or_route_candidate; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20145](../findings/url_references-011.md#FND-20145).

### SRC-0014 at character 50973

```text
ams(input,output,error){input?FS.createDevice("/dev","stdin",input):FS.symlink("/dev/tty","/dev/stdin"),output?FS.createDevice("/dev","stdout",null,output):FS.symlink("/dev/tty","/dev/stdout")
```

### SRC-0014 at character 51172

```text
FS.createDevice("/dev","stderr",null,error):FS.symlink("/dev/tty1","/dev/stderr");FS.open("/dev/stdin",0),FS.open("/dev/stdout",1),FS.open("/dev/stderr",1)},staticInit(){FS.nameTable=new Array
```

### SRC-0031 at character 50973

```text
ams(input,output,error){input?FS.createDevice("/dev","stdin",input):FS.symlink("/dev/tty","/dev/stdin"),output?FS.createDevice("/dev","stdout",null,output):FS.symlink("/dev/tty","/dev/stdout")
```

### SRC-0031 at character 51172

```text
FS.createDevice("/dev","stderr",null,error):FS.symlink("/dev/tty1","/dev/stderr");FS.open("/dev/stdin",0),FS.open("/dev/stdout",1),FS.open("/dev/stderr",1)},staticInit(){FS.nameTable=new Array
```

### SRC-0032 at character 50973

```text
ams(input,output,error){input?FS.createDevice("/dev","stdin",input):FS.symlink("/dev/tty","/dev/stdin"),output?FS.createDevice("/dev","stdout",null,output):FS.symlink("/dev/tty","/dev/stdout")
```

### SRC-0032 at character 51172

```text
FS.createDevice("/dev","stderr",null,error):FS.symlink("/dev/tty1","/dev/stderr");FS.open("/dev/stdin",0),FS.open("/dev/stdout",1),FS.open("/dev/stderr",1)},staticInit(){FS.nameTable=new Array
```

### SRC-0072 at character 50973

```text
ams(input,output,error){input?FS.createDevice("/dev","stdin",input):FS.symlink("/dev/tty","/dev/stdin"),output?FS.createDevice("/dev","stdout",null,output):FS.symlink("/dev/tty","/dev/stdout")
```

### SRC-0072 at character 51172

```text
FS.createDevice("/dev","stderr",null,error):FS.symlink("/dev/tty1","/dev/stderr");FS.open("/dev/stdin",0),FS.open("/dev/stdout",1),FS.open("/dev/stderr",1)},staticInit(){FS.nameTable=new Array
```

### SRC-0123 at character 50973

```text
ams(input,output,error){input?FS.createDevice("/dev","stdin",input):FS.symlink("/dev/tty","/dev/stdin"),output?FS.createDevice("/dev","stdout",null,output):FS.symlink("/dev/tty","/dev/stdout")
```

### SRC-0123 at character 51172

```text
FS.createDevice("/dev","stderr",null,error):FS.symlink("/dev/tty1","/dev/stderr");FS.open("/dev/stdin",0),FS.open("/dev/stdout",1),FS.open("/dev/stderr",1)},staticInit(){FS.nameTable=new Array
```

### SRC-0781 at character 3111841

```text
din=r.stdin,r.stdout=r.stdout,r.stderr=r.stderr,r.stdin?_t(`stdin`,r.stdin):ft(`/dev/tty`,`/dev/stdin`),r.stdout?_t(`stdout`,null,r.stdout):ft(`/dev/tty`,`/dev/stdout`),r.stderr?_t(`stderr`,nu
```

### SRC-0781 at character 3111989

```text
/tty`,`/dev/stdout`),r.stderr?_t(`stderr`,null,r.stderr):ft(`/dev/tty1`,`/dev/stderr`),mt(`/dev/stdin`,0),mt(`/dev/stdout`,1),mt(`/dev/stderr`,1)),qe=!1,xe(ae),i(r),r.onRuntimeInitialized&&r.o
```

### SRC-1160 at character 50973

```text
ams(input,output,error){input?FS.createDevice("/dev","stdin",input):FS.symlink("/dev/tty","/dev/stdin"),output?FS.createDevice("/dev","stdout",null,output):FS.symlink("/dev/tty","/dev/stdout")
```

### SRC-1160 at character 51172

```text
FS.createDevice("/dev","stderr",null,error):FS.symlink("/dev/tty1","/dev/stderr");FS.open("/dev/stdin",0),FS.open("/dev/stdout",1),FS.open("/dev/stderr",1)},staticInit(){FS.nameTable=new Array
```

## URL-01015

`/dev/stdout`

- Type: page_or_route_candidate; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20146](../findings/url_references-011.md#FND-20146).

### SRC-0014 at character 51061

```text
","/dev/stdin"),output?FS.createDevice("/dev","stdout",null,output):FS.symlink("/dev/tty","/dev/stdout"),error?FS.createDevice("/dev","stderr",null,error):FS.symlink("/dev/tty1","/dev/stderr");
```

### SRC-0014 at character 51196

```text
stderr",null,error):FS.symlink("/dev/tty1","/dev/stderr");FS.open("/dev/stdin",0),FS.open("/dev/stdout",1),FS.open("/dev/stderr",1)},staticInit(){FS.nameTable=new Array(4096),FS.mount(MEMFS,{},
```

### SRC-0031 at character 51061

```text
","/dev/stdin"),output?FS.createDevice("/dev","stdout",null,output):FS.symlink("/dev/tty","/dev/stdout"),error?FS.createDevice("/dev","stderr",null,error):FS.symlink("/dev/tty1","/dev/stderr");
```

### SRC-0031 at character 51196

```text
stderr",null,error):FS.symlink("/dev/tty1","/dev/stderr");FS.open("/dev/stdin",0),FS.open("/dev/stdout",1),FS.open("/dev/stderr",1)},staticInit(){FS.nameTable=new Array(4096),FS.mount(MEMFS,{},
```

### SRC-0032 at character 51061

```text
","/dev/stdin"),output?FS.createDevice("/dev","stdout",null,output):FS.symlink("/dev/tty","/dev/stdout"),error?FS.createDevice("/dev","stderr",null,error):FS.symlink("/dev/tty1","/dev/stderr");
```

### SRC-0032 at character 51196

```text
stderr",null,error):FS.symlink("/dev/tty1","/dev/stderr");FS.open("/dev/stdin",0),FS.open("/dev/stdout",1),FS.open("/dev/stderr",1)},staticInit(){FS.nameTable=new Array(4096),FS.mount(MEMFS,{},
```

### SRC-0072 at character 51061

```text
","/dev/stdin"),output?FS.createDevice("/dev","stdout",null,output):FS.symlink("/dev/tty","/dev/stdout"),error?FS.createDevice("/dev","stderr",null,error):FS.symlink("/dev/tty1","/dev/stderr");
```

### SRC-0072 at character 51196

```text
stderr",null,error):FS.symlink("/dev/tty1","/dev/stderr");FS.open("/dev/stdin",0),FS.open("/dev/stdout",1),FS.open("/dev/stderr",1)},staticInit(){FS.nameTable=new Array(4096),FS.mount(MEMFS,{},
```

### SRC-0123 at character 51061

```text
","/dev/stdin"),output?FS.createDevice("/dev","stdout",null,output):FS.symlink("/dev/tty","/dev/stdout"),error?FS.createDevice("/dev","stderr",null,error):FS.symlink("/dev/tty1","/dev/stderr");
```

### SRC-0123 at character 51196

```text
stderr",null,error):FS.symlink("/dev/tty1","/dev/stderr");FS.open("/dev/stdin",0),FS.open("/dev/stdout",1),FS.open("/dev/stderr",1)},staticInit(){FS.nameTable=new Array(4096),FS.mount(MEMFS,{},
```

### SRC-0781 at character 3111905

```text
n`,r.stdin):ft(`/dev/tty`,`/dev/stdin`),r.stdout?_t(`stdout`,null,r.stdout):ft(`/dev/tty`,`/dev/stdout`),r.stderr?_t(`stderr`,null,r.stderr):ft(`/dev/tty1`,`/dev/stderr`),mt(`/dev/stdin`,0),mt(
```

### SRC-0781 at character 3112008

```text
),r.stderr?_t(`stderr`,null,r.stderr):ft(`/dev/tty1`,`/dev/stderr`),mt(`/dev/stdin`,0),mt(`/dev/stdout`,1),mt(`/dev/stderr`,1)),qe=!1,xe(ae),i(r),r.onRuntimeInitialized&&r.onRuntimeInitialized(
```

### SRC-1160 at character 51061

```text
","/dev/stdin"),output?FS.createDevice("/dev","stdout",null,output):FS.symlink("/dev/tty","/dev/stdout"),error?FS.createDevice("/dev","stderr",null,error):FS.symlink("/dev/tty1","/dev/stderr");
```

### SRC-1160 at character 51196

```text
stderr",null,error):FS.symlink("/dev/tty1","/dev/stderr");FS.open("/dev/stdin",0),FS.open("/dev/stdout",1),FS.open("/dev/stderr",1)},staticInit(){FS.nameTable=new Array(4096),FS.mount(MEMFS,{},
```

## URL-01016

`/dev/tty`

- Type: page_or_route_candidate; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20147](../findings/url_references-011.md#FND-20147).

### SRC-0014 at character 49946

```text
dev(5,0),TTY.default_tty_ops),TTY.register(FS.makedev(6,0),TTY.default_tty1_ops),FS.mkdev("/dev/tty",FS.makedev(5,0)),FS.mkdev("/dev/tty1",FS.makedev(6,0));var randomBuffer=new Uint8Array(10
```

### SRC-0014 at character 50962

```text
tandardStreams(input,output,error){input?FS.createDevice("/dev","stdin",input):FS.symlink("/dev/tty","/dev/stdin"),output?FS.createDevice("/dev","stdout",null,output):FS.symlink("/dev/tty","
```

### SRC-0014 at character 51050

```text
k("/dev/tty","/dev/stdin"),output?FS.createDevice("/dev","stdout",null,output):FS.symlink("/dev/tty","/dev/stdout"),error?FS.createDevice("/dev","stderr",null,error):FS.symlink("/dev/tty1","
```

### SRC-0031 at character 49946

```text
dev(5,0),TTY.default_tty_ops),TTY.register(FS.makedev(6,0),TTY.default_tty1_ops),FS.mkdev("/dev/tty",FS.makedev(5,0)),FS.mkdev("/dev/tty1",FS.makedev(6,0));var randomBuffer=new Uint8Array(10
```

### SRC-0031 at character 50962

```text
tandardStreams(input,output,error){input?FS.createDevice("/dev","stdin",input):FS.symlink("/dev/tty","/dev/stdin"),output?FS.createDevice("/dev","stdout",null,output):FS.symlink("/dev/tty","
```

### SRC-0031 at character 51050

```text
k("/dev/tty","/dev/stdin"),output?FS.createDevice("/dev","stdout",null,output):FS.symlink("/dev/tty","/dev/stdout"),error?FS.createDevice("/dev","stderr",null,error):FS.symlink("/dev/tty1","
```

### SRC-0032 at character 49946

```text
dev(5,0),TTY.default_tty_ops),TTY.register(FS.makedev(6,0),TTY.default_tty1_ops),FS.mkdev("/dev/tty",FS.makedev(5,0)),FS.mkdev("/dev/tty1",FS.makedev(6,0));var randomBuffer=new Uint8Array(10
```

### SRC-0032 at character 50962

```text
tandardStreams(input,output,error){input?FS.createDevice("/dev","stdin",input):FS.symlink("/dev/tty","/dev/stdin"),output?FS.createDevice("/dev","stdout",null,output):FS.symlink("/dev/tty","
```

### SRC-0032 at character 51050

```text
k("/dev/tty","/dev/stdin"),output?FS.createDevice("/dev","stdout",null,output):FS.symlink("/dev/tty","/dev/stdout"),error?FS.createDevice("/dev","stderr",null,error):FS.symlink("/dev/tty1","
```

### SRC-0072 at character 49946

```text
dev(5,0),TTY.default_tty_ops),TTY.register(FS.makedev(6,0),TTY.default_tty1_ops),FS.mkdev("/dev/tty",FS.makedev(5,0)),FS.mkdev("/dev/tty1",FS.makedev(6,0));var randomBuffer=new Uint8Array(10
```

### SRC-0072 at character 50962

```text
tandardStreams(input,output,error){input?FS.createDevice("/dev","stdin",input):FS.symlink("/dev/tty","/dev/stdin"),output?FS.createDevice("/dev","stdout",null,output):FS.symlink("/dev/tty","
```

### SRC-0072 at character 51050

```text
k("/dev/tty","/dev/stdin"),output?FS.createDevice("/dev","stdout",null,output):FS.symlink("/dev/tty","/dev/stdout"),error?FS.createDevice("/dev","stderr",null,error):FS.symlink("/dev/tty1","
```

### SRC-0123 at character 49946

```text
dev(5,0),TTY.default_tty_ops),TTY.register(FS.makedev(6,0),TTY.default_tty1_ops),FS.mkdev("/dev/tty",FS.makedev(5,0)),FS.mkdev("/dev/tty1",FS.makedev(6,0));var randomBuffer=new Uint8Array(10
```

### SRC-0123 at character 50962

```text
tandardStreams(input,output,error){input?FS.createDevice("/dev","stdin",input):FS.symlink("/dev/tty","/dev/stdin"),output?FS.createDevice("/dev","stdout",null,output):FS.symlink("/dev/tty","
```

### SRC-0123 at character 51050

```text
k("/dev/tty","/dev/stdin"),output?FS.createDevice("/dev","stdout",null,output):FS.symlink("/dev/tty","/dev/stdout"),error?FS.createDevice("/dev","stderr",null,error):FS.symlink("/dev/tty1","
```

### SRC-0781 at character 3081307

```text
ev`),st(259,{read:()=>0,write:(e,t,n,r)=>r}),dt(`/dev/null`,259),A(1280,Le),A(1536,Re),dt(`/dev/tty`,1280),dt(`/dev/tty1`,1536);var e=new Uint8Array(1024),t=0,n=()=>(t===0&&(t=De(e).byteLeng
```

### SRC-0781 at character 3111830

```text
(gt=!0,r.stdin=r.stdin,r.stdout=r.stdout,r.stderr=r.stderr,r.stdin?_t(`stdin`,r.stdin):ft(`/dev/tty`,`/dev/stdin`),r.stdout?_t(`stdout`,null,r.stdout):ft(`/dev/tty`,`/dev/stdout`),r.stderr?_
```

### SRC-0781 at character 3111894

```text
in?_t(`stdin`,r.stdin):ft(`/dev/tty`,`/dev/stdin`),r.stdout?_t(`stdout`,null,r.stdout):ft(`/dev/tty`,`/dev/stdout`),r.stderr?_t(`stderr`,null,r.stderr):ft(`/dev/tty1`,`/dev/stderr`),mt(`/dev
```

### SRC-1160 at character 49946

```text
dev(5,0),TTY.default_tty_ops),TTY.register(FS.makedev(6,0),TTY.default_tty1_ops),FS.mkdev("/dev/tty",FS.makedev(5,0)),FS.mkdev("/dev/tty1",FS.makedev(6,0));var randomBuffer=new Uint8Array(10
```

### SRC-1160 at character 50962

```text
tandardStreams(input,output,error){input?FS.createDevice("/dev","stdin",input):FS.symlink("/dev/tty","/dev/stdin"),output?FS.createDevice("/dev","stdout",null,output):FS.symlink("/dev/tty","
```

### SRC-1160 at character 51050

```text
k("/dev/tty","/dev/stdin"),output?FS.createDevice("/dev","stdout",null,output):FS.symlink("/dev/tty","/dev/stdout"),error?FS.createDevice("/dev","stderr",null,error):FS.symlink("/dev/tty1","
```

## URL-01017

`/dev/tty1`

- Type: page_or_route_candidate; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20148](../findings/url_references-011.md#FND-20148).

### SRC-0014 at character 49983

```text
ister(FS.makedev(6,0),TTY.default_tty1_ops),FS.mkdev("/dev/tty",FS.makedev(5,0)),FS.mkdev("/dev/tty1",FS.makedev(6,0));var randomBuffer=new Uint8Array(1024),randomLeft=0,randomByte=()=>(rando
```

### SRC-0014 at character 51137

```text
nk("/dev/tty","/dev/stdout"),error?FS.createDevice("/dev","stderr",null,error):FS.symlink("/dev/tty1","/dev/stderr");FS.open("/dev/stdin",0),FS.open("/dev/stdout",1),FS.open("/dev/stderr",1)}
```

### SRC-0031 at character 49983

```text
ister(FS.makedev(6,0),TTY.default_tty1_ops),FS.mkdev("/dev/tty",FS.makedev(5,0)),FS.mkdev("/dev/tty1",FS.makedev(6,0));var randomBuffer=new Uint8Array(1024),randomLeft=0,randomByte=()=>(rando
```

### SRC-0031 at character 51137

```text
nk("/dev/tty","/dev/stdout"),error?FS.createDevice("/dev","stderr",null,error):FS.symlink("/dev/tty1","/dev/stderr");FS.open("/dev/stdin",0),FS.open("/dev/stdout",1),FS.open("/dev/stderr",1)}
```

### SRC-0032 at character 49983

```text
ister(FS.makedev(6,0),TTY.default_tty1_ops),FS.mkdev("/dev/tty",FS.makedev(5,0)),FS.mkdev("/dev/tty1",FS.makedev(6,0));var randomBuffer=new Uint8Array(1024),randomLeft=0,randomByte=()=>(rando
```

### SRC-0032 at character 51137

```text
nk("/dev/tty","/dev/stdout"),error?FS.createDevice("/dev","stderr",null,error):FS.symlink("/dev/tty1","/dev/stderr");FS.open("/dev/stdin",0),FS.open("/dev/stdout",1),FS.open("/dev/stderr",1)}
```

### SRC-0072 at character 49983

```text
ister(FS.makedev(6,0),TTY.default_tty1_ops),FS.mkdev("/dev/tty",FS.makedev(5,0)),FS.mkdev("/dev/tty1",FS.makedev(6,0));var randomBuffer=new Uint8Array(1024),randomLeft=0,randomByte=()=>(rando
```

### SRC-0072 at character 51137

```text
nk("/dev/tty","/dev/stdout"),error?FS.createDevice("/dev","stderr",null,error):FS.symlink("/dev/tty1","/dev/stderr");FS.open("/dev/stdin",0),FS.open("/dev/stdout",1),FS.open("/dev/stderr",1)}
```

### SRC-0123 at character 49983

```text
ister(FS.makedev(6,0),TTY.default_tty1_ops),FS.mkdev("/dev/tty",FS.makedev(5,0)),FS.mkdev("/dev/tty1",FS.makedev(6,0));var randomBuffer=new Uint8Array(1024),randomLeft=0,randomByte=()=>(rando
```

### SRC-0123 at character 51137

```text
nk("/dev/tty","/dev/stdout"),error?FS.createDevice("/dev","stderr",null,error):FS.symlink("/dev/tty1","/dev/stderr");FS.open("/dev/stdin",0),FS.open("/dev/stdout",1),FS.open("/dev/stderr",1)}
```

### SRC-0781 at character 3081327

```text
=>0,write:(e,t,n,r)=>r}),dt(`/dev/null`,259),A(1280,Le),A(1536,Re),dt(`/dev/tty`,1280),dt(`/dev/tty1`,1536);var e=new Uint8Array(1024),t=0,n=()=>(t===0&&(t=De(e).byteLength),e[--t]);_t(`rando
```

### SRC-0781 at character 3111959

```text
tdout`,null,r.stdout):ft(`/dev/tty`,`/dev/stdout`),r.stderr?_t(`stderr`,null,r.stderr):ft(`/dev/tty1`,`/dev/stderr`),mt(`/dev/stdin`,0),mt(`/dev/stdout`,1),mt(`/dev/stderr`,1)),qe=!1,xe(ae),i
```

### SRC-1160 at character 49983

```text
ister(FS.makedev(6,0),TTY.default_tty1_ops),FS.mkdev("/dev/tty",FS.makedev(5,0)),FS.mkdev("/dev/tty1",FS.makedev(6,0));var randomBuffer=new Uint8Array(1024),randomLeft=0,randomByte=()=>(rando
```

### SRC-1160 at character 51137

```text
nk("/dev/tty","/dev/stdout"),error?FS.createDevice("/dev","stderr",null,error):FS.symlink("/dev/tty1","/dev/stderr");FS.open("/dev/stdin",0),FS.open("/dev/stdout",1),FS.open("/dev/stderr",1)}
```

## URL-01018

`/disconnect`

- Type: page_or_route_candidate; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20149](../findings/url_references-011.md#FND-20149).

### SRC-0171 at character 21867

```text
ut(this.onHandshakeTimeout,n)},disconnect(e=`none`){let t=d();t.disconnectReason=e,$.send(`/disconnect`,{channel:c.disconnect},!0),C.emit(y.ConnectionTerminated,{reason:e})},connect(e,t=!1){let
```

## URL-01019

`/event-a/~1`

- Type: page_or_route_candidate; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20150](../findings/url_references-011.md#FND-20150).

### SRC-0781 at character 260121

```text
u={admin:`/service/admin`,announce:`/service/announce`,arena:`/service/arena`,arenaEvents:`/event-a/~1`,chat:`/service/chat`,clubChat:`/chat`,connect:`/meta/connect`,disconnect:`/meta/disconnec
```

## URL-01020

`/event-t/~1`

- Type: page_or_route_candidate; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20151](../findings/url_references-011.md#FND-20151).

### SRC-0781 at character 260385

```text
bscribe`,teamMatch:`/service/teammatch`,tournament:`/service/tournament`,tournamentEvents:`/event-t/~1`,unsubscribe:`/meta/unsubscribe`,user:`/service/user`}})),Pu,Fu=r((()=>{Pu={Connect:`Conne
```

## URL-01021

`/events`

- Type: page_or_route_candidate; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20152](../findings/url_references-011.md#FND-20152).

### SRC-0183 at character 158

```text
hesscom.routes||{},Object.assign(window.chesscom.routes,{web_event_index:{tokens:[[`text`,`/events`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-0183 at character 847

```text
?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_event_index:{tokens:[[`text`,`/events`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

### SRC-0183 at character 7373

```text
hesscom.routes||{},Object.assign(window.chesscom.routes,{web_event_index:{tokens:[[`text`,`/events`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-0183 at character 8062

```text
?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_event_index:{tokens:[[`text`,`/events`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

### SRC-0187 at character 158

```text
hesscom.routes||{},Object.assign(window.chesscom.routes,{web_event_index:{tokens:[[`text`,`/events`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-0187 at character 847

```text
?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_event_index:{tokens:[[`text`,`/events`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

### SRC-0187 at character 10224

```text
hesscom.routes||{},Object.assign(window.chesscom.routes,{web_event_index:{tokens:[[`text`,`/events`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-0187 at character 10913

```text
?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_event_index:{tokens:[[`text`,`/events`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

## URL-01022

`/g`

- Type: page_or_route_candidate; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20153](../findings/url_references-011.md#FND-20153).

### SRC-0090 at character 110786

```text
eplace(/%2C/g,`,`).replace(/%2A/g,`*`).replace(/\(/g,`%28`).replace(/\)/g,`%29`).replace(/'/g,`%27`)},t.encodePathComponent=function(e){return t.customEncodeURIComponent(e).replace(/%3D
```

### SRC-0751 at character 110786

```text
eplace(/%2C/g,`,`).replace(/%2A/g,`*`).replace(/\(/g,`%28`).replace(/\)/g,`%29`).replace(/'/g,`%27`)},t.encodePathComponent=function(e){return t.customEncodeURIComponent(e).replace(/%3D
```

### SRC-0781 at character 421012

```text
eplace(/%2C/g,`,`).replace(/%2A/g,`*`).replace(/\(/g,`%28`).replace(/\)/g,`%29`).replace(/'/g,`%27`)},t.encodePathComponent=function(e){return t.customEncodeURIComponent(e).replace(/%3D
```

### SRC-1137 at character 410169

```text
eplace(/%2C/g,`,`).replace(/%2A/g,`*`).replace(/\(/g,`%28`).replace(/\)/g,`%29`).replace(/'/g,`%27`)},t.encodePathComponent=function(e){return t.customEncodeURIComponent(e).replace(/%3D
```

### SRC-1165 at character 410169

```text
eplace(/%2C/g,`,`).replace(/%2A/g,`*`).replace(/\(/g,`%28`).replace(/\)/g,`%29`).replace(/'/g,`%27`)},t.encodePathComponent=function(e){return t.customEncodeURIComponent(e).replace(/%3D
```

## URL-01023

`/game`

- Type: page_or_route_candidate; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20154](../findings/url_references-011.md#FND-20154).

### SRC-0781 at character 22094

```text
ds:[],schemes:[`https`]},web_game_uuid:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-0781 at character 45317

```text
,schemes:[`https`]},i18n_web_game_uuid:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

### SRC-0781 at character 468189

```text
ds:[],schemes:[`https`]},web_game_uuid:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-0781 at character 491412

```text
,schemes:[`https`]},i18n_web_game_uuid:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

### SRC-0781 at character 959562

```text
ds:[],schemes:[`https`]},web_game_uuid:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-0781 at character 961832

```text
,schemes:[`https`]},i18n_web_game_uuid:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

### SRC-1137 at character 122377

```text
ds:[],schemes:[`https`]},web_game_uuid:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-1137 at character 124647

```text
,schemes:[`https`]},i18n_web_game_uuid:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

### SRC-1137 at character 2968770

```text
ds:[],schemes:[`https`]},web_game_uuid:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-1137 at character 2971040

```text
,schemes:[`https`]},i18n_web_game_uuid:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

### SRC-1165 at character 122377

```text
ds:[],schemes:[`https`]},web_game_uuid:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-1165 at character 124647

```text
,schemes:[`https`]},i18n_web_game_uuid:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

### SRC-1165 at character 2968770

```text
ds:[],schemes:[`https`]},web_game_uuid:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-1165 at character 2971040

```text
,schemes:[`https`]},i18n_web_game_uuid:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

## URL-01024

`/game/*`

- Type: page_or_route_candidate; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20155](../findings/url_references-011.md#FND-20155).

### SRC-0781 at character 345040

```text
match/*`,`/play/online`,`/play/online/create-tournament/*`,`/game/live/*`,`/game/daily/*`,`/game/*`],assets:[]},Lye={name:Oye,version:kye,commit:Aye,scripts:jye,license:Mye,repository:Nye,p
```

## URL-01025

`/game/coach`

- Type: page_or_route_candidate; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20156](../findings/url_references-011.md#FND-20156).

### SRC-0781 at character 9076

```text
s:[],schemes:[`https`]},web_game_coach:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game/coach`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-0781 at character 31564

```text
schemes:[`https`]},i18n_web_game_coach:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game/coach`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

### SRC-0781 at character 455171

```text
s:[],schemes:[`https`]},web_game_coach:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game/coach`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-0781 at character 477659

```text
schemes:[`https`]},i18n_web_game_coach:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game/coach`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

## URL-01026

`/game/computer`

- Type: page_or_route_candidate; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20157](../findings/url_references-011.md#FND-20157).

### SRC-0781 at character 9800

```text
],schemes:[`https`]},web_game_computer:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game/computer`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-0781 at character 32374

```text
emes:[`https`]},i18n_web_game_computer:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game/computer`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

### SRC-0781 at character 455895

```text
],schemes:[`https`]},web_game_computer:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game/computer`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-0781 at character 478469

```text
emes:[`https`]},i18n_web_game_computer:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game/computer`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

## URL-01027

`/game/daily`

- Type: page_or_route_candidate; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20158](../findings/url_references-011.md#FND-20158).

### SRC-0185 at character 191

```text
window.chesscom.routes,{web_game_daily:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game/daily`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-0185 at character 917

```text
schemes:[`https`]},i18n_web_game_daily:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game/daily`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

### SRC-0185 at character 3168

```text
window.chesscom.routes,{web_game_daily:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game/daily`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-0185 at character 3894

```text
schemes:[`https`]},i18n_web_game_daily:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game/daily`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

### SRC-0781 at character 12690

```text
s:[],schemes:[`https`]},web_game_daily:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game/daily`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-0781 at character 35608

```text
schemes:[`https`]},i18n_web_game_daily:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game/daily`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

### SRC-0781 at character 458785

```text
s:[],schemes:[`https`]},web_game_daily:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game/daily`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-0781 at character 481703

```text
schemes:[`https`]},i18n_web_game_daily:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game/daily`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

## URL-01028

`/game/daily/*`

- Type: page_or_route_candidate; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20159](../findings/url_references-011.md#FND-20159).

### SRC-0781 at character 345024

```text
ament/*`,`/play/match/*`,`/play/online`,`/play/online/create-tournament/*`,`/game/live/*`,`/game/daily/*`,`/game/*`],assets:[]},Lye={name:Oye,version:kye,commit:Aye,scripts:jye,license:Mye,reposi
```

## URL-01029

`/game/live`

- Type: page_or_route_candidate; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20160](../findings/url_references-011.md#FND-20160).

### SRC-0781 at character 17780

```text
ds:[],schemes:[`https`]},web_game_live:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game/live`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-0781 at character 40487

```text
,schemes:[`https`]},i18n_web_game_live:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game/live`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

### SRC-0781 at character 463875

```text
ds:[],schemes:[`https`]},web_game_live:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game/live`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-0781 at character 486582

```text
,schemes:[`https`]},i18n_web_game_live:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game/live`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

### SRC-0781 at character 958843

```text
(window.chesscom.routes,{web_game_live:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game/live`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-0781 at character 961027

```text
,schemes:[`https`]},i18n_web_game_live:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game/live`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

### SRC-1137 at character 121658

```text
GET`],schemes:[`https`]},web_game_live:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game/live`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-1137 at character 123842

```text
,schemes:[`https`]},i18n_web_game_live:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game/live`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

### SRC-1137 at character 2968051

```text
(window.chesscom.routes,{web_game_live:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game/live`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-1137 at character 2970235

```text
,schemes:[`https`]},i18n_web_game_live:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game/live`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

### SRC-1165 at character 121658

```text
GET`],schemes:[`https`]},web_game_live:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game/live`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-1165 at character 123842

```text
,schemes:[`https`]},i18n_web_game_live:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game/live`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

### SRC-1165 at character 2968051

```text
(window.chesscom.routes,{web_game_live:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game/live`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-1165 at character 2970235

```text
,schemes:[`https`]},i18n_web_game_live:{tokens:[[`variable`,`/`,`[^/]++`,`id`,!0],[`text`,`/game/live`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

## URL-01030

`/game/live/*`

- Type: page_or_route_candidate; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20161](../findings/url_references-011.md#FND-20161).

### SRC-0781 at character 345009

```text
*`,`/play/tournament/*`,`/play/match/*`,`/play/online`,`/play/online/create-tournament/*`,`/game/live/*`,`/game/daily/*`,`/game/*`],assets:[]},Lye={name:Oye,version:kye,commit:Aye,scripts:jye,li
```

## URL-01031

`/games/archive`

- Type: page_or_route_candidate; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20162](../findings/url_references-011.md#FND-20162).

### SRC-0066 at character 11670

```text
mes:[`https`]},web_archive_index:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/games/archive`]],defaults:{username:null,host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|sch
```

### SRC-0066 at character 17295

```text
`https`]},i18n_web_archive_index:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/games/archive`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

### SRC-0066 at character 230564

```text
esscom.routes,{web_archive_index:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/games/archive`]],defaults:{username:null,host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|sch
```

### SRC-0066 at character 237573

```text
`https`]},i18n_web_archive_index:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/games/archive`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

### SRC-1151 at character 11670

```text
mes:[`https`]},web_archive_index:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/games/archive`]],defaults:{username:null,host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|sch
```

### SRC-1151 at character 17295

```text
`https`]},i18n_web_archive_index:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/games/archive`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

### SRC-1151 at character 230564

```text
esscom.routes,{web_archive_index:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/games/archive`]],defaults:{username:null,host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|sch
```

### SRC-1151 at character 237573

```text
`https`]},i18n_web_archive_index:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/games/archive`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

## URL-01032

`/games/search`

- Type: page_or_route_candidate; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20163](../findings/url_references-011.md#FND-20163).

### SRC-0066 at character 14467

```text
,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_master_games_search:{tokens:[[`text`,`/games/search`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-0066 at character 19052

```text
`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_master_games_search:{tokens:[[`text`,`/games/search`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

### SRC-0066 at character 233361

```text
,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_master_games_search:{tokens:[[`text`,`/games/search`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-0066 at character 239330

```text
`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_master_games_search:{tokens:[[`text`,`/games/search`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

### SRC-1136 at character 2789

```text
\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_master_games_search:{tokens:[[`text`,`/games/search`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-1136 at character 3497

```text
st`,!0]],methods:[`GET`],schemes:[`https`]},i18n_web_master_games_search:{tokens:[[`text`,`/games/search`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

### SRC-1136 at character 42169

```text
routes||{},Object.assign(window.chesscom.routes,{web_master_games_search:{tokens:[[`text`,`/games/search`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-1136 at character 42877

```text
st`,!0]],methods:[`GET`],schemes:[`https`]},i18n_web_master_games_search:{tokens:[[`text`,`/games/search`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

### SRC-1137 at character 18172

```text
,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_master_games_search:{tokens:[[`text`,`/games/search`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-1137 at character 24610

```text
`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_master_games_search:{tokens:[[`text`,`/games/search`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

### SRC-1137 at character 1147621

```text
,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_master_games_search:{tokens:[[`text`,`/games/search`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-1137 at character 1154746

```text
`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_master_games_search:{tokens:[[`text`,`/games/search`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

### SRC-1151 at character 14467

```text
,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_master_games_search:{tokens:[[`text`,`/games/search`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-1151 at character 19052

```text
`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_master_games_search:{tokens:[[`text`,`/games/search`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

### SRC-1151 at character 233361

```text
,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_master_games_search:{tokens:[[`text`,`/games/search`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-1151 at character 239330

```text
`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_master_games_search:{tokens:[[`text`,`/games/search`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

### SRC-1165 at character 18172

```text
,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_master_games_search:{tokens:[[`text`,`/games/search`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-1165 at character 24610

```text
`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_master_games_search:{tokens:[[`text`,`/games/search`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

### SRC-1165 at character 1147621

```text
,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_master_games_search:{tokens:[[`text`,`/games/search`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-1165 at character 1154746

```text
`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_master_games_search:{tokens:[[`text`,`/games/search`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

## URL-01033

`/gifs`

- Type: page_or_route_candidate; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20164](../findings/url_references-011.md#FND-20164).

### SRC-1137 at character 126243

```text
\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_content_gifs:{tokens:[[`text`,`/gifs`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-1137 at character 126931

```text
[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_content_gifs:{tokens:[[`text`,`/gifs`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

### SRC-1137 at character 3548722

```text
esscom.routes||{},Object.assign(window.chesscom.routes,{web_content_gifs:{tokens:[[`text`,`/gifs`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-1137 at character 3549410

```text
[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_content_gifs:{tokens:[[`text`,`/gifs`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

### SRC-1165 at character 126243

```text
\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_content_gifs:{tokens:[[`text`,`/gifs`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-1165 at character 126931

```text
[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_content_gifs:{tokens:[[`text`,`/gifs`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

### SRC-1165 at character 3548722

```text
esscom.routes||{},Object.assign(window.chesscom.routes,{web_content_gifs:{tokens:[[`text`,`/gifs`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-1165 at character 3549410

```text
[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},i18n_web_content_gifs:{tokens:[[`text`,`/gifs`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

## URL-01034

`/guest/update-skill-level`

- Type: page_or_route_candidate; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20165](../findings/url_references-011.md#FND-20165).

### SRC-1137 at character 96483

```text
`,`host`,!0]],methods:[],schemes:[`https`]},web_guest_update_skill_level:{tokens:[[`text`,`/guest/update-skill-level`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-1137 at character 2389981

```text
s||{},Object.assign(window.chesscom.routes,{web_guest_update_skill_level:{tokens:[[`text`,`/guest/update-skill-level`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-1165 at character 96483

```text
`,`host`,!0]],methods:[],schemes:[`https`]},web_guest_update_skill_level:{tokens:[[`text`,`/guest/update-skill-level`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-1165 at character 2389981

```text
s||{},Object.assign(window.chesscom.routes,{web_guest_update_skill_level:{tokens:[[`text`,`/guest/update-skill-level`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

## URL-01035

`/handshake`

- Type: page_or_route_candidate; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20166](../findings/url_references-011.md#FND-20166).

### SRC-0171 at character 21720

```text
handshaking=!0,e.isReusingSession=!1;let t=this.getHandshakeMessage(),n=H([t])+1e3;$.send(`/handshake`,t,!0),e.metaHandshakeTimeout=window.setTimeout(this.onHandshakeTimeout,n)},disconnect(e=`
```

## URL-01036

`/home`

- Type: page_or_route_candidate; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20167](../findings/url_references-011.md#FND-20167).

### SRC-0014 at character 49612

```text
errCode);FS.currentPath=lookup.path},createDefaultDirectories(){FS.mkdir("/tmp"),FS.mkdir("/home"),FS.mkdir("/home/web_user")},createDefaultDevices(){FS.mkdir("/dev"),FS.registerDevice(FS
```

### SRC-0031 at character 49612

```text
errCode);FS.currentPath=lookup.path},createDefaultDirectories(){FS.mkdir("/tmp"),FS.mkdir("/home"),FS.mkdir("/home/web_user")},createDefaultDevices(){FS.mkdir("/dev"),FS.registerDevice(FS
```

### SRC-0032 at character 49612

```text
errCode);FS.currentPath=lookup.path},createDefaultDirectories(){FS.mkdir("/tmp"),FS.mkdir("/home"),FS.mkdir("/home/web_user")},createDefaultDevices(){FS.mkdir("/dev"),FS.registerDevice(FS
```

### SRC-0072 at character 49612

```text
errCode);FS.currentPath=lookup.path},createDefaultDirectories(){FS.mkdir("/tmp"),FS.mkdir("/home"),FS.mkdir("/home/web_user")},createDefaultDevices(){FS.mkdir("/dev"),FS.registerDevice(FS
```

### SRC-0094 at character 6088

```text
(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_user_home:{tokens:[[`text`,`/home`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-0094 at character 22977

```text
(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_user_home:{tokens:[[`text`,`/home`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-0102 at character 6088

```text
(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_user_home:{tokens:[[`text`,`/home`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-0102 at character 22977

```text
(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_user_home:{tokens:[[`text`,`/home`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-0123 at character 49612

```text
errCode);FS.currentPath=lookup.path},createDefaultDirectories(){FS.mkdir("/tmp"),FS.mkdir("/home"),FS.mkdir("/home/web_user")},createDefaultDevices(){FS.mkdir("/dev"),FS.registerDevice(FS
```

### SRC-0144 at character 6088

```text
(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_user_home:{tokens:[[`text`,`/home`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-0144 at character 22891

```text
(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_user_home:{tokens:[[`text`,`/home`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-0781 at character 103804

```text
)?[^\\s]+`,`host`,!0]],methods:[`POST`],schemes:[`https`]},web_user_home:{tokens:[[`text`,`/home`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-0781 at character 2600176

```text
.chesscom.routes||{},Object.assign(window.chesscom.routes,{web_user_home:{tokens:[[`text`,`/home`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-0781 at character 3081169

```text
w Je(e),Ye[e].stack=`<generic error, no stack>`}),Ke=Array(4096),ct(Be,`/`),ut(`/tmp`),ut(`/home`),ut(`/home/web_user`),(function(){ut(`/dev`),st(259,{read:()=>0,write:(e,t,n,r)=>r}),dt(`
```

### SRC-1137 at character 137611

```text
(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_user_home:{tokens:[[`text`,`/home`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-1137 at character 3631149

```text
.chesscom.routes||{},Object.assign(window.chesscom.routes,{web_user_home:{tokens:[[`text`,`/home`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-1155 at character 6088

```text
(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_user_home:{tokens:[[`text`,`/home`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-1155 at character 22977

```text
(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_user_home:{tokens:[[`text`,`/home`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-1160 at character 49612

```text
errCode);FS.currentPath=lookup.path},createDefaultDirectories(){FS.mkdir("/tmp"),FS.mkdir("/home"),FS.mkdir("/home/web_user")},createDefaultDevices(){FS.mkdir("/dev"),FS.registerDevice(FS
```

### SRC-1165 at character 137611

```text
(?:\\.)?[^\\s]+`,`host`,!0]],methods:[],schemes:[`https`]},web_user_home:{tokens:[[`text`,`/home`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

### SRC-1165 at character 3631149

```text
.chesscom.routes||{},Object.assign(window.chesscom.routes,{web_user_home:{tokens:[[`text`,`/home`]],defaults:{host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|schach|ru|uk|ajed
```

## URL-01037

`/home/user`

- Type: page_or_route_candidate; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20168](../findings/url_references-011.md#FND-20168).

### SRC-0659 at character 49

```text
from pathlib import Path
import json,csv
p=Path('/home/user');d=p/'research/refinement'
t=json.loads((d/'target.json').read_text());b=json.loads((d/'r
```

## URL-01038

`/home/user/extension/engines/cee`

- Type: page_or_route_candidate; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20169](../findings/url_references-011.md#FND-20169).

### SRC-0074 at character 377

```text
t path from 'node:path';

const require = createRequire(import.meta.url);
const CEE_DIR = '/home/user/extension/engines/cee';

// ---- capture global postMessage (api responses) ----
const pending = [];   // {resol
```

### SRC-0075 at character 233

```text
rt path from 'node:path';
const require = createRequire(import.meta.url);
const CEE_DIR = '/home/user/extension/engines/cee';
const pending = [];
globalThis.postMessage = (msg) => {
  if (typeof msg === 'string') r
```

### SRC-0076 at character 232

```text
rt path from 'node:path';
const require = createRequire(import.meta.url);
const CEE_DIR = '/home/user/extension/engines/cee';
const pending = [];
globalThis.postMessage = (msg) => {
  if (typeof msg === 'string') r
```

### SRC-0077 at character 235

```text
rt path from 'node:path';
const require = createRequire(import.meta.url);
const CEE_DIR = '/home/user/extension/engines/cee';
const pending = [];
globalThis.postMessage = (msg) => {
  if (typeof msg === 'string') r
```

### SRC-0078 at character 226

```text
rt path from 'node:path';
const require = createRequire(import.meta.url);
const CEE_DIR = '/home/user/extension/engines/cee';
const pending = [];
const out=[];
const _log=console.log; console.log=(...a)=>{out.push(
```

### SRC-0079 at character 226

```text
rt path from 'node:path';
const require = createRequire(import.meta.url);
const CEE_DIR = '/home/user/extension/engines/cee';
const pending = [];
const out=[];
const _log=console.log; console.log=(...a)=>{out.push(
```

### SRC-0080 at character 226

```text
rt path from 'node:path';
const require = createRequire(import.meta.url);
const CEE_DIR = '/home/user/extension/engines/cee';
const pending = [];
const out=[];
const _log=console.log; console.log=(...a)=>{out.push(
```

### SRC-0081 at character 226

```text
rt path from 'node:path';
const require = createRequire(import.meta.url);
const CEE_DIR = '/home/user/extension/engines/cee';
const pending = [];
const out=[];
const _log=console.log; console.log=(...a)=>{out.push(
```

### SRC-0082 at character 226

```text
rt path from 'node:path';
const require = createRequire(import.meta.url);
const CEE_DIR = '/home/user/extension/engines/cee';
const pending = [];
const out=[];
const _log=console.log; console.log=(...a)=>{out.push(
```

### SRC-0083 at character 226

```text
rt path from 'node:path';
const require = createRequire(import.meta.url);
const CEE_DIR = '/home/user/extension/engines/cee';
const pending = [];
const out=[];
const _log=console.log; console.log=(...a)=>{out.push(
```

### SRC-0084 at character 226

```text
rt path from 'node:path';
const require = createRequire(import.meta.url);
const CEE_DIR = '/home/user/extension/engines/cee';
const pending = [];
const out=[];
const _log=console.log; console.log=(...a)=>{out.push(
```

### SRC-0085 at character 226

```text
rt path from 'node:path';
const require = createRequire(import.meta.url);
const CEE_DIR = '/home/user/extension/engines/cee';
const pending = [];
const out=[];
const _log=console.log; console.log=(...a)=>{out.push(
```

### SRC-0086 at character 932

```text
import fs from 'node:fs';
const require = createRequire(import.meta.url);
const CEE_DIR = '/home/user/extension/engines/cee';

const STRENGTH = Number(process.argv[2] || 1);
const VERSIONS = Number(process.argv[3] 
```

### SRC-0087 at character 952

```text
import fs from 'node:fs';
const require = createRequire(import.meta.url);
const CEE_DIR = '/home/user/extension/engines/cee';

const STRENGTH = Number(process.argv[2] || 1);
const OUT = process.argv[3] || `/tmp/pro
```

### SRC-0088 at character 952

```text
import fs from 'node:fs';
const require = createRequire(import.meta.url);
const CEE_DIR = '/home/user/extension/engines/cee';

const STRENGTH = Number(process.argv[2] || 1);
const OUT = process.argv[3] || `/tmp/pro
```

### SRC-0107 at character 952

```text
import fs from 'node:fs';
const require = createRequire(import.meta.url);
const CEE_DIR = '/home/user/extension/engines/cee';

const STRENGTH = Number(process.argv[2] || 1);
const OUT = process.argv[3] || `/tmp/pro
```

### SRC-0113 at character 952

```text
import fs from 'node:fs';
const require = createRequire(import.meta.url);
const CEE_DIR = '/home/user/extension/engines/cee';

const STRENGTH = Number(process.argv[2] || 1);
const OUT = process.argv[3] || `/tmp/pro
```

### SRC-0117 at character 952

```text
import fs from 'node:fs';
const require = createRequire(import.meta.url);
const CEE_DIR = '/home/user/extension/engines/cee';

const STRENGTH = Number(process.argv[2] || 1);
const OUT = process.argv[3] || `/tmp/pro
```

### SRC-0121 at character 952

```text
import fs from 'node:fs';
const require = createRequire(import.meta.url);
const CEE_DIR = '/home/user/extension/engines/cee';

const STRENGTH = Number(process.argv[2] || 1);
const OUT = process.argv[3] || `/tmp/pro
```

## URL-01039

`/home/user/extension/lib/protobuf.js`

- Type: asset; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20170](../findings/url_references-011.md#FND-20170).

### SRC-0074 at character 1839

```text

}

// ---- our protobuf codec ----
const { encodeMessage, decodeMessage } = await import('/home/user/extension/lib/protobuf.js');

const F = { ADD_EVALUATIONS:1, MOVE_CLASSIFICATION:25, NEW_GAME:26, RUN_SEARCH:29, SIM
```

### SRC-0075 at character 1390

```text
nding.shift(); reject(e); }
  });
}
const { encodeMessage, decodeMessage } = await import('/home/user/extension/lib/protobuf.js');
const F = { NEW_GAME:26, GAME_REVIEW:42, CHARM_INFERENCE:68, SET_GAME_RESULT:30, ADD_CH
```

### SRC-0076 at character 1228

```text
nding.shift(); reject(e); }
  });
}
const { encodeMessage, decodeMessage } = await import('/home/user/extension/lib/protobuf.js');
const F = { NEW_GAME:26, GAME_REVIEW:42, SET_GAME_RESULT:30, GET_GAME_RESULT:7, MAKE_MO
```

### SRC-0077 at character 1231

```text
nding.shift(); reject(e); }
  });
}
const { encodeMessage, decodeMessage } = await import('/home/user/extension/lib/protobuf.js');
const F = { NEW_GAME:26, GAME_REVIEW:42, RUN_SEARCH:29, SET_GAME_RESULT:30 };
async fun
```

### SRC-0078 at character 1952

```text
nding.shift(); reject(e); }
  });
}
const { encodeMessage, decodeMessage } = await import('/home/user/extension/lib/protobuf.js');
const F = { NEW_GAME:26, GAME_REVIEW:42, SET_GAME_RESULT:30, RUN_SEARCH:29 };
async fun
```

### SRC-0079 at character 1952

```text
nding.shift(); reject(e); }
  });
}
const { encodeMessage, decodeMessage } = await import('/home/user/extension/lib/protobuf.js');
const F = { NEW_GAME:26, GAME_REVIEW:42, SET_GAME_RESULT:30, RUN_SEARCH:29 };
async fun
```

### SRC-0080 at character 1952

```text
nding.shift(); reject(e); }
  });
}
const { encodeMessage, decodeMessage } = await import('/home/user/extension/lib/protobuf.js');
const F = { NEW_GAME:26, GAME_REVIEW:42, SET_GAME_RESULT:30, RUN_SEARCH:29 };
async fun
```

### SRC-0081 at character 1952

```text
nding.shift(); reject(e); }
  });
}
const { encodeMessage, decodeMessage } = await import('/home/user/extension/lib/protobuf.js');
const F = { NEW_GAME:26, GAME_REVIEW:42, SET_GAME_RESULT:30, RUN_SEARCH:29 };
async fun
```

### SRC-0082 at character 1952

```text
nding.shift(); reject(e); }
  });
}
const { encodeMessage, decodeMessage } = await import('/home/user/extension/lib/protobuf.js');
const F = { NEW_GAME:26, GAME_REVIEW:42, SET_GAME_RESULT:30, RUN_SEARCH:29 };
async fun
```

### SRC-0083 at character 1952

```text
nding.shift(); reject(e); }
  });
}
const { encodeMessage, decodeMessage } = await import('/home/user/extension/lib/protobuf.js');
const F = { NEW_GAME:26, GAME_REVIEW:42, SET_GAME_RESULT:30, RUN_SEARCH:29 };
async fun
```

### SRC-0084 at character 1952

```text
nding.shift(); reject(e); }
  });
}
const { encodeMessage, decodeMessage } = await import('/home/user/extension/lib/protobuf.js');
const F = { NEW_GAME:26, GAME_REVIEW:42, SET_GAME_RESULT:30, RUN_SEARCH:29 };
async fun
```

### SRC-0085 at character 1952

```text
nding.shift(); reject(e); }
  });
}
const { encodeMessage, decodeMessage } = await import('/home/user/extension/lib/protobuf.js');
const F = { NEW_GAME:26, GAME_REVIEW:42, SET_GAME_RESULT:30, RUN_SEARCH:29 };
async fun
```

### SRC-0086 at character 2547

```text
nding.shift(); reject(e); }
  });
}
const { encodeMessage, decodeMessage } = await import('/home/user/extension/lib/protobuf.js');
const F = { NEW_GAME: 26, GAME_REVIEW: 42, SET_GAME_RESULT: 30 };
async function featur
```

### SRC-0087 at character 2507

```text
nding.shift(); reject(e); }
  });
}
const { encodeMessage, decodeMessage } = await import('/home/user/extension/lib/protobuf.js');
const F = { NEW_GAME: 26, GAME_REVIEW: 42, SET_GAME_RESULT: 30 };
async function featur
```

### SRC-0088 at character 2507

```text
nding.shift(); reject(e); }
  });
}
const { encodeMessage, decodeMessage } = await import('/home/user/extension/lib/protobuf.js');
const F = { NEW_GAME: 26, GAME_REVIEW: 42, SET_GAME_RESULT: 30 };
async function featur
```

### SRC-0107 at character 2507

```text
nding.shift(); reject(e); }
  });
}
const { encodeMessage, decodeMessage } = await import('/home/user/extension/lib/protobuf.js');
const F = { NEW_GAME: 26, GAME_REVIEW: 42, SET_GAME_RESULT: 30 };
async function featur
```

### SRC-0113 at character 2532

```text
nding.shift(); reject(e); }
  });
}
const { encodeMessage, decodeMessage } = await import('/home/user/extension/lib/protobuf.js');
const F = { NEW_GAME: 26, GAME_REVIEW: 42, SET_GAME_RESULT: 30 };
async function featur
```

### SRC-0117 at character 2532

```text
nding.shift(); reject(e); }
  });
}
const { encodeMessage, decodeMessage } = await import('/home/user/extension/lib/protobuf.js');
const F = { NEW_GAME: 26, GAME_REVIEW: 42, SET_GAME_RESULT: 30 };
async function featur
```

### SRC-0121 at character 2532

```text
nding.shift(); reject(e); }
  });
}
const { encodeMessage, decodeMessage } = await import('/home/user/extension/lib/protobuf.js');
const F = { NEW_GAME: 26, GAME_REVIEW: 42, SET_GAME_RESULT: 30 };
async function featur
```

## URL-01040

`/home/user/research/doting-cee-baseline.json`

- Type: page_or_route_candidate; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20171](../findings/url_references-011.md#FND-20171).

### SRC-0107 at character 5221

```text
's');
  const g = gr.gameReview || {};
  const h = g.highlights || {};
  fs.writeFileSync('/home/user/research/doting-cee-baseline.json', JSON.stringify(g));
  console.log('accuracy:', JSON.stringify(h.accuracy));
  console.lo
```

## URL-01041

`/home/user/research/doting-preeval.json`

- Type: page_or_route_candidate; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20172](../findings/url_references-011.md#FND-20172).

### SRC-0113 at character 5702

```text
's');
  const g = gr.gameReview || {};
  const h = g.highlights || {};
  fs.writeFileSync('/home/user/research/doting-preeval.json', JSON.stringify(g));
  console.log('accuracy:', JSON.stringify(h.accuracy));
  console.lo
```

## URL-01042

`/home/user/research/doting-state12.json`

- Type: page_or_route_candidate; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20173](../findings/url_references-011.md#FND-20173).

### SRC-0117 at character 6526

```text
's');
  const g = gr.gameReview || {};
  const h = g.highlights || {};
  fs.writeFileSync('/home/user/research/doting-state12.json', JSON.stringify(g));
  console.log('accuracy:', JSON.stringify(h.accuracy));
  console.lo
```

## URL-01043

`/home/user/research/doting-v3.json`

- Type: page_or_route_candidate; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20174](../findings/url_references-011.md#FND-20174).

### SRC-0121 at character 5275

```text
's');
  const g = gr.gameReview || {};
  const h = g.highlights || {};
  fs.writeFileSync('/home/user/research/doting-v3.json', JSON.stringify(g));
  console.log('accuracy:', JSON.stringify(h.accuracy));
  console.lo
```

## URL-01044

`/home/user/research/fixtures/doting-prospect.pgn`

- Type: page_or_route_candidate; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20175](../findings/url_references-011.md#FND-20175).

### SRC-0107 at character 2973

```text
y { api('CEE_DisposeFeature', [handle]).catch(() => {}); }
}

const pgn = fs.readFileSync('/home/user/research/fixtures/doting-prospect.pgn', 'utf8');

// W4e-style settings: userColor + enableSkills + tricky flag; search proven-l
```

### SRC-0113 at character 2998

```text
y { api('CEE_DisposeFeature', [handle]).catch(() => {}); }
}

const pgn = fs.readFileSync('/home/user/research/fixtures/doting-prospect.pgn', 'utf8');

// W4e-style settings: userColor + enableSkills + tricky flag; search proven-l
```

### SRC-0117 at character 2998

```text
y { api('CEE_DisposeFeature', [handle]).catch(() => {}); }
}

const pgn = fs.readFileSync('/home/user/research/fixtures/doting-prospect.pgn', 'utf8');

// W4e-style settings: userColor + enableSkills + tricky flag; search proven-l
```

### SRC-0121 at character 2998

```text
y { api('CEE_DisposeFeature', [handle]).catch(() => {}); }
}

const pgn = fs.readFileSync('/home/user/research/fixtures/doting-prospect.pgn', 'utf8');

// W4e-style settings: userColor + enableSkills + tricky flag; search proven-l
```

## URL-01045

`/home/user/research/fixtures/example-game.pgn`

- Type: page_or_route_candidate; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20176](../findings/url_references-011.md#FND-20176).

### SRC-0086 at character 3013

```text
y { api('CEE_DisposeFeature', [handle]).catch(() => {}); }
}

const pgn = fs.readFileSync('/home/user/research/fixtures/example-game.pgn', 'utf8');

const settings = {
  locale: 'en_US',
  search: process.env.MODE === 'preset'

```

## URL-01046

`/home/user/research/fixtures/human-game.pgn`

- Type: page_or_route_candidate; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20177](../findings/url_references-011.md#FND-20177).

### SRC-0087 at character 2973

```text
y { api('CEE_DisposeFeature', [handle]).catch(() => {}); }
}

const pgn = fs.readFileSync('/home/user/research/fixtures/human-game.pgn', 'utf8');

// W4e-style settings: userColor + enableSkills + tricky flag; search proven-l
```

### SRC-0088 at character 3163

```text
', false, true);
await new Promise(r => setTimeout(r, 500));

const pgn = fs.readFileSync('/home/user/research/fixtures/human-game.pgn', 'utf8');

// W4e-style settings: userColor + enableSkills + tricky flag; search proven-l
```

## URL-01047

`/home/user/torch-refinement-findings.md`

- Type: page_or_route_candidate; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20178](../findings/url_references-011.md#FND-20178).

### SRC-0660 at character 6073

```text
on code, not part of a delivered update, and should not be installed.
`;
fs.writeFileSync('/home/user/torch-refinement-findings.md',doc);
console.log('Report written:',rows.length,'configurations;',holdout.length,'holdout
```

### SRC-1647 at character 6073

```text
on code, not part of a delivered update, and should not be installed.
`;
fs.writeFileSync('/home/user/torch-refinement-findings.md',doc);
console.log('Report written:',rows.length,'configurations;',holdout.length,'holdout
```

## URL-01048

`/home/web_user`

- Type: page_or_route_candidate; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20179](../findings/url_references-011.md#FND-20179).

### SRC-0014 at character 49630

```text
tPath=lookup.path},createDefaultDirectories(){FS.mkdir("/tmp"),FS.mkdir("/home"),FS.mkdir("/home/web_user")},createDefaultDevices(){FS.mkdir("/dev"),FS.registerDevice(FS.makedev(1,3),{read:()=>0,w
```

### SRC-0014 at character 65055

```text
!getEnvStrings.strings){var env={USER:"web_user",LOGNAME:"web_user",PATH:"/",PWD:"/",HOME:"/home/web_user",LANG:(globalThis.navigator?.language??"C").replace("-","_")+".UTF-8",_:thisProgram};for(v
```

### SRC-0031 at character 49630

```text
tPath=lookup.path},createDefaultDirectories(){FS.mkdir("/tmp"),FS.mkdir("/home"),FS.mkdir("/home/web_user")},createDefaultDevices(){FS.mkdir("/dev"),FS.registerDevice(FS.makedev(1,3),{read:()=>0,w
```

### SRC-0031 at character 65055

```text
!getEnvStrings.strings){var env={USER:"web_user",LOGNAME:"web_user",PATH:"/",PWD:"/",HOME:"/home/web_user",LANG:(globalThis.navigator?.language??"C").replace("-","_")+".UTF-8",_:thisProgram};for(v
```

### SRC-0032 at character 49630

```text
tPath=lookup.path},createDefaultDirectories(){FS.mkdir("/tmp"),FS.mkdir("/home"),FS.mkdir("/home/web_user")},createDefaultDevices(){FS.mkdir("/dev"),FS.registerDevice(FS.makedev(1,3),{read:()=>0,w
```

### SRC-0032 at character 65055

```text
!getEnvStrings.strings){var env={USER:"web_user",LOGNAME:"web_user",PATH:"/",PWD:"/",HOME:"/home/web_user",LANG:(globalThis.navigator?.language??"C").replace("-","_")+".UTF-8",_:thisProgram};for(v
```

### SRC-0036 at character 18381

```text
};function et(){if(!Je){var e,t={USER:"web_user",LOGNAME:"web_user",PATH:"/",PWD:"/",HOME:"/home/web_user",LANG:("object"==typeof navigator&&navigator.languages&&navigator.languages[0]||"C").repla
```

### SRC-0038 at character 8536

```text
};function _e(){if(!ve){var e,n={USER:"web_user",LOGNAME:"web_user",PATH:"/",PWD:"/",HOME:"/home/web_user",LANG:("object"==typeof navigator&&navigator.languages&&navigator.languages[0]||"C").repla
```

### SRC-0040 at character 5817

```text
={};function La(){if(!Ma){var a={USER:"web_user",LOGNAME:"web_user",PATH:"/",PWD:"/",HOME:"/home/web_user",LANG:("object"==typeof navigator&&navigator.languages&&navigator.languages[0]||"C").repla
```

### SRC-0072 at character 49630

```text
tPath=lookup.path},createDefaultDirectories(){FS.mkdir("/tmp"),FS.mkdir("/home"),FS.mkdir("/home/web_user")},createDefaultDevices(){FS.mkdir("/dev"),FS.registerDevice(FS.makedev(1,3),{read:()=>0,w
```

### SRC-0072 at character 65055

```text
!getEnvStrings.strings){var env={USER:"web_user",LOGNAME:"web_user",PATH:"/",PWD:"/",HOME:"/home/web_user",LANG:(globalThis.navigator?.language??"C").replace("-","_")+".UTF-8",_:thisProgram};for(v
```

### SRC-0123 at character 49630

```text
tPath=lookup.path},createDefaultDirectories(){FS.mkdir("/tmp"),FS.mkdir("/home"),FS.mkdir("/home/web_user")},createDefaultDevices(){FS.mkdir("/dev"),FS.registerDevice(FS.makedev(1,3),{read:()=>0,w
```

### SRC-0123 at character 65055

```text
!getEnvStrings.strings){var env={USER:"web_user",LOGNAME:"web_user",PATH:"/",PWD:"/",HOME:"/home/web_user",LANG:(globalThis.navigator?.language??"C").replace("-","_")+".UTF-8",_:thisProgram};for(v
```

### SRC-0781 at character 3076194

```text
,$n,er={},tr=()=>{if(!nr){var e={USER:`web_user`,LOGNAME:`web_user`,PATH:`/`,PWD:`/`,HOME:`/home/web_user`,LANG:(typeof navigator==`object`&&navigator.languages&&navigator.languages[0]||`C`).repla
```

### SRC-0781 at character 3081181

```text
].stack=`<generic error, no stack>`}),Ke=Array(4096),ct(Be,`/`),ut(`/tmp`),ut(`/home`),ut(`/home/web_user`),(function(){ut(`/dev`),st(259,{read:()=>0,write:(e,t,n,r)=>r}),dt(`/dev/null`,259),A(128
```

### SRC-1137 at character 3286102

```text
,nn,rn={},an=()=>{if(!on){var e={USER:`web_user`,LOGNAME:`web_user`,PATH:`/`,PWD:`/`,HOME:`/home/web_user`,LANG:(globalThis.navigator?.language??`C`).replace(`-`,`_`)+`.UTF-8`,_:d||`./this.program
```

### SRC-1138 at character 18381

```text
};function et(){if(!Je){var e,t={USER:"web_user",LOGNAME:"web_user",PATH:"/",PWD:"/",HOME:"/home/web_user",LANG:("object"==typeof navigator&&navigator.languages&&navigator.languages[0]||"C").repla
```

### SRC-1139 at character 8536

```text
};function _e(){if(!ve){var e,n={USER:"web_user",LOGNAME:"web_user",PATH:"/",PWD:"/",HOME:"/home/web_user",LANG:("object"==typeof navigator&&navigator.languages&&navigator.languages[0]||"C").repla
```

### SRC-1140 at character 17941

```text
};function Ze(){if(!Ke){var e,t={USER:"web_user",LOGNAME:"web_user",PATH:"/",PWD:"/",HOME:"/home/web_user",LANG:("object"==typeof navigator&&navigator.languages&&navigator.languages[0]||"C").repla
```

### SRC-1141 at character 56092

```text
"_")+".UTF-8";var env={"USER":"web_user","LOGNAME":"web_user","PATH":"/","PWD":"/","HOME":"/home/web_user","LANG":lang,"_":getExecutableName()};for(var x in ENV){env[x]=ENV[x]}var strings=[];for(v
```

### SRC-1144 at character 5817

```text
={};function La(){if(!Ma){var a={USER:"web_user",LOGNAME:"web_user",PATH:"/",PWD:"/",HOME:"/home/web_user",LANG:("object"==typeof navigator&&navigator.languages&&navigator.languages[0]||"C").repla
```

### SRC-1145 at character 5837

```text
={};function La(){if(!Ma){var a={USER:"web_user",LOGNAME:"web_user",PATH:"/",PWD:"/",HOME:"/home/web_user",LANG:("object"==typeof navigator&&navigator.languages&&navigator.languages[0]||"C").repla
```

### SRC-1146 at character 16446

```text
={};function Gb(){if(!Hb){var a={USER:"web_user",LOGNAME:"web_user",PATH:"/",PWD:"/",HOME:"/home/web_user",LANG:("object"===typeof navigator&&navigator.languages&&navigator.languages[0]||"C").repl
```

### SRC-1160 at character 49630

```text
tPath=lookup.path},createDefaultDirectories(){FS.mkdir("/tmp"),FS.mkdir("/home"),FS.mkdir("/home/web_user")},createDefaultDevices(){FS.mkdir("/dev"),FS.registerDevice(FS.makedev(1,3),{read:()=>0,w
```

### SRC-1160 at character 65055

```text
!getEnvStrings.strings){var env={USER:"web_user",LOGNAME:"web_user",PATH:"/",PWD:"/",HOME:"/home/web_user",LANG:(globalThis.navigator?.language??"C").replace("-","_")+".UTF-8",_:thisProgram};for(v
```

### SRC-1165 at character 3286102

```text
,nn,rn={},an=()=>{if(!on){var e={USER:`web_user`,LOGNAME:`web_user`,PATH:`/`,PWD:`/`,HOME:`/home/web_user`,LANG:(globalThis.navigator?.language??`C`).replace(`-`,`_`)+`.UTF-8`,_:d||`./this.program
```

### SRC-1166 at character 18381

```text
};function et(){if(!Je){var e,t={USER:"web_user",LOGNAME:"web_user",PATH:"/",PWD:"/",HOME:"/home/web_user",LANG:("object"==typeof navigator&&navigator.languages&&navigator.languages[0]||"C").repla
```

### SRC-1167 at character 8536

```text
};function _e(){if(!ve){var e,n={USER:"web_user",LOGNAME:"web_user",PATH:"/",PWD:"/",HOME:"/home/web_user",LANG:("object"==typeof navigator&&navigator.languages&&navigator.languages[0]||"C").repla
```

### SRC-1168 at character 17941

```text
};function Ze(){if(!Ke){var e,t={USER:"web_user",LOGNAME:"web_user",PATH:"/",PWD:"/",HOME:"/home/web_user",LANG:("object"==typeof navigator&&navigator.languages&&navigator.languages[0]||"C").repla
```

### SRC-1169 at character 56092

```text
"_")+".UTF-8";var env={"USER":"web_user","LOGNAME":"web_user","PATH":"/","PWD":"/","HOME":"/home/web_user","LANG":lang,"_":getExecutableName()};for(var x in ENV){env[x]=ENV[x]}var strings=[];for(v
```

### SRC-1171 at character 5817

```text
={};function La(){if(!Ma){var a={USER:"web_user",LOGNAME:"web_user",PATH:"/",PWD:"/",HOME:"/home/web_user",LANG:("object"==typeof navigator&&navigator.languages&&navigator.languages[0]||"C").repla
```

### SRC-1172 at character 5837

```text
={};function La(){if(!Ma){var a={USER:"web_user",LOGNAME:"web_user",PATH:"/",PWD:"/",HOME:"/home/web_user",LANG:("object"==typeof navigator&&navigator.languages&&navigator.languages[0]||"C").repla
```

### SRC-1173 at character 16446

```text
={};function Gb(){if(!Hb){var a={USER:"web_user",LOGNAME:"web_user",PATH:"/",PWD:"/",HOME:"/home/web_user",LANG:("object"===typeof navigator&&navigator.languages&&navigator.languages[0]||"C").repl
```

## URL-01049

`/insights`

- Type: page_or_route_candidate; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20180](../findings/url_references-011.md#FND-20180).

### SRC-0066 at character 6332

```text
,schemes:[`https`]},web_insights:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/insights`]],defaults:{username:null,host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|sch
```

### SRC-0066 at character 8690

```text
mes:[`https`]},i18n_web_insights:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/insights`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

### SRC-0066 at character 108558

```text
,schemes:[`https`]},web_insights:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/insights`]],defaults:{username:null,host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|sch
```

### SRC-0066 at character 110916

```text
mes:[`https`]},i18n_web_insights:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/insights`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

### SRC-1151 at character 6332

```text
,schemes:[`https`]},web_insights:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/insights`]],defaults:{username:null,host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|sch
```

### SRC-1151 at character 8690

```text
mes:[`https`]},i18n_web_insights:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/insights`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

### SRC-1151 at character 108558

```text
,schemes:[`https`]},web_insights:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/insights`]],defaults:{username:null,host:`www.chess-dev.com`},requirements:{host:`(?!admin)(www|sch
```

### SRC-1151 at character 110916

```text
mes:[`https`]},i18n_web_insights:{tokens:[[`variable`,`/`,`[^/]++`,`username`,!0],[`text`,`/insights`],[`variable`,`/`,`es|fr|de|pl|ru|sv|el|pt|it|zh|ja|ko|nl|hy|bg|hr|cs|da|fi|hu|lt|no|ro|sk
```

## URL-01050

`/int/`

- Type: page_or_route_candidate; form: relative_literal.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20181](../findings/url_references-011.md#FND-20181).

### SRC-0090 at character 36085

```text
 a}var et,tt,nt,rt,it=y((()=>{et=/[-[\]/{}()*+?.\\^$|]/g,tt=[`/callback`,`/admin`,`/pub/`,`/int/`],nt=null,rt=null}));function at(){return!!(window.chesscom.enableSentryHP&&window.context
```

### SRC-0751 at character 36085

```text
 a}var et,tt,nt,rt,it=y((()=>{et=/[-[\]/{}()*+?.\\^$|]/g,tt=[`/callback`,`/admin`,`/pub/`,`/int/`],nt=null,rt=null}));function at(){return!!(window.chesscom.enableSentryHP&&window.context
```

### SRC-0781 at character 317105

```text
var _he,Sf,Cf,wf,vhe=r((()=>{_he=/[-[\]/{}()*+?.\\^$|]/g,Sf=[`/callback`,`/admin`,`/pub/`,`/int/`],Cf=null,wf=null}));function yhe(){return!!(window.chesscom.enableSentryHP&&window.contex
```

### SRC-1137 at character 320909

```text
a}var ip,ap,op,sp,Mde=r((()=>{ip=/[-[\]/{}()*+?.\\^$|]/g,ap=[`/callback`,`/admin`,`/pub/`,`/int/`],op=null,sp=null}));function Nde(){return!!(window.chesscom.enableSentryHP&&window.contex
```

### SRC-1165 at character 320909

```text
a}var ip,ap,op,sp,Mde=r((()=>{ip=/[-[\]/{}()*+?.\\^$|]/g,ap=[`/callback`,`/admin`,`/pub/`,`/int/`],op=null,sp=null}));function Nde(){return!!(window.chesscom.enableSentryHP&&window.contex
```
