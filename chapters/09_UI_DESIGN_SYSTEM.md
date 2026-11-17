# Design system and CSS architecture

[Master index](00_MASTER_INDEX.md)

Four actually referenced public stylesheets were fetched successfully:design-system-global,main-global,alerts-global and logged-out-navigation-global. They supply1,240CSSvariabledeclarations,633uniquevariablenames,52mediaqueries and full selector contexts. See the machine metrics rather than relying on this explanatory label if extraction is extended.

## Directly observed examples

- Main global CSS sets`html{font-size:62.5%}`;`body`uses1.4rem,line-height1.43,zero margin,and`var(--font-family-system)`. Rem units therefore derive from a10pxbase only when browser defaultfont-sizeis16px;user preferences can change it.
- `--color-green-400:#5D9948`;primary background references gray tokens rather than a globally fixed color. Repeated text/default variables have different scoped values.
- `--font-family-system:-apple-system,BlinkMacSystemFont,"Segoe UI",system-ui,Helvetica,Arial,sans-serif`;headingfamily`"Chess Sans",sans-serif`. Saved HTML preloadsChessSansBold/ExtraBold and chess glyph font files. Fontpreloadisnotproofeveryfacewasdownloaded.
- Navigation style exports collapsed5.6rem/default17remwidths and max/min break point values,includingmin768=48em,min1024=64em.
- cc-buttonstyles usegradients,color-mix,enabled/hoveredtokens,in set and external shadows;modal motion uses named durations/easing.
- CSSvariables,custom component classes,theme-scopedoverrides and exported breakpoints establish a custom design system. Genericframeworkidentityisnotestablished. Compiled`:export`blocksarecompatiblewithCSSModules/Sasspipelines,notproofthatallstyleswereauthoredinSass.

[Full variable values,cascade occurrences,selectors,mediaqueries,fonts and exports](../registries/design-system.json)

