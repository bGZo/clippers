---
title: QianJianTech/LaTeXLive
aliases:
  - LaTeXLive
  - latex
created: 2024-12-08T21:26:22
modified: 2025-06-07T15:23:55
description: LateX公式编辑器-妈叔出品
source: https://github.com/QianJianTech/LaTeXLive
tags:
  - star
tags-link: 
type: repo
---

## Repo Meta

![](https://img.shields.io/github/stars/QianJianTech/LaTeXLive?style=for-the-badge&label=stars) ![](https://img.shields.io/github/repo-size/QianJianTech/LaTeXLive?style=for-the-badge&label=size) ![](https://img.shields.io/github/created-at/QianJianTech/LaTeXLive?style=for-the-badge&label=since)

[![](https://github-readme-stats.vercel.app/api/pin/?username=QianJianTech&repo=LaTeXLive&bg_color=00000000)](https://github.com/QianJianTech/LaTeXLive)

## Notes

# 使用文档 Documentation

### 目录 Contents

### 1 关于 LaTeX 公式编辑 Introduce

**LaTeX**（常被读作/ˈlɑːtɛk/或/ˈleɪtɛk/，正确读音:/ˈlɑːtɛx/音译：拉泰赫，写作 L A T E X ），是一种基于 TeX 的排版系统，由美国计算机科学家 [莱斯利·兰伯特](https://zh.wikipedia.org/wiki/%E8%8E%B1%E6%96%AF%E5%88%A9%C2%B7%E5%85%B0%E6%B3%A2%E7%89%B9) 在 20 世纪 80 年代初期开发。 **MathJax**是一个跨浏览器的 JavaScript 库，它使用 MathML、LaTeX 和 ASCIIMathML 标记在 Web 浏览器中显示数学符号。 本页面是基于 [MathJax](https://www.mathjax.org/) 实现的便捷 LaTeX 公式编辑器，支持导出 SVG 矢量图、高清 PNG 位图、MathML 代码以及 SVGCode，并且可根据需要自定义加载 TeX 扩展包，实现功能拓展。

#### 1.1 基本使用 Basic

在本页面输入框中输入的公式**不用**放在 `<math>` 与 `</math>`，或 `$` 与 `$` 之间，直接输入相关 LaTeX 代码即可。

在输出框您可以看到即时渲染出来效果，方便进行代码修改。

以下字符在 LaTeX 环境中是保留字符，它们具有特殊含义，只可以特定语法中起作用，所以并不能在输入框中直接输入它们（会报错或者不会渲染）

```
# % ^ & _ { } ~ \
```

如您因其他原因需要直接显示它们，请在其前面加入 `\` 反斜杠或其它转义符。

```
\# \% ^\wedge \& \_ \{ \} \sim \backslash
```

$$ 
# % ^\wedge & _ { } \sim \backslash 
$$ 

关于 LaTeX 代码部分请参考下一章节。

**注意：**本页面不支持文档编辑环境，因此不支持调用 `\begin{document}` 等相关命令，默认即为数学环境，可直接输入数学公式。

#### 1.2 关于渲染 Render

本页面采用 MathJax-tex-svg 显示数学符号，支持四种格式导出。

##### 1.2.1 导出 SVG

SVG 全称**S**calable **V**ector **G**raphics（可缩放矢量图形），是一种基于可扩展标记语言（XML），用于描述二维矢量图形的图形格式，标准由 W3C 制定，是一个开放标准。

我们可以简单理解为，SVG 是一种与图像分辨率无关的矢量格式的拓展名，因此 SVG 文件可以直接拖入**AI、PS**等绘图软件中进行相应编辑、修改，以满足任意尺寸需求。

##### 1.2.2 导出 PNG

PNG 全称**P**ortable **N**etwork **G**raphics（便携式网络图形），是一种无损压缩的**位图**图形格式。

因此 PNG 与图像分辨率有关，本页面导出的 PNG 分辨率为 4K 标准（3840x2160），也可以满足绝大部分的文档需求。

##### 1.2.3 导出 MathML

MathML 全称**Math**ematical **M**arkup **L**anguage（数学标记语言），是一种基于可扩展标记语言（XML）的标准，用来描述数学符号和公式。现已获得**HTML5**和大部分**办公软件**与**数学软件**的支持，例如 Microsoft Office、LibreOffice、Mathematica、Maple 等，这意味着，您只需将**MathML 代码**复制进 Microsoft Word 当中，便会自动转换成 Word 支持的 LaTeX 公式，并可进行相应后续编辑。

##### 1.2.4 导出 SVG Code（说不明白）

SVGCode 即是一个 SVG 文件的全部代码，此支持 HTML 环境。

### 2 数学公式编辑 Displaying a formula

#### 2.1 符号与字母 Symbol and Alphabet

##### 2.1.1 希腊字母 Greek alphabet

|序号|小写|LaTeX|读音|序号|大写|LaTeX|读音|
|:-:|:-:|:--|:--|:-:|:-:|:--|:--|
|1|α|\alpha|/ˈælfə/|31|Γ|\Gamma|/ˈɡæmə/|
|2|β|\beta|/ˈbiːtə/, US: /ˈbeɪtə/|32|Δ|\Delta|/ˈdɛltə/|
|3|γ|\gamma|/ˈɡæmə/|33|Θ|\Theta|/ˈθiːtə/|
|4|δ|\delta|/ˈdɛltə/|34|Λ|\Lambda|/ˈlæmdə/|
|5|ϵ|\epsilon|/ˈɛpsɪlɒn/|35|Ξ|\Xi|/zaɪ, ksaɪ/|
|6|ε|\varepsilon|/ˈɛpsɪlɒn/|36|Π|\Pi|/paɪ/|
|7|ζ|\zeta|/ˈzeɪtə/|37|Σ|\Sigma|/ˈsɪɡmə/|
|8|η|\eta|/ˈeɪtə/|38|Υ|\Upsilon|/ˈʌpsɪlɒn/|
|9|θ|\theta|/ˈθiːtə/|39|Φ|\Phi|/faɪ/|
|10|ϑ|\vartheta|/ˈθiːtə/|40|Ψ|\Psi|/psaɪ/|
|11|ι|\iota|/aɪˈoʊtə/|41|Ω|\Omega|/oʊˈmeɪɡə/|
|12|κ|\kappa|/ˈkæpə/|||||
|13|λ|\lambda|/ˈlæmdə/|||||
|14|μ|\mu|/mjuː/|||||
|15|ν|\nu|/njuː/|||||
|16|ξ|\xi|/zaɪ, ksaɪ/|||||
|17|o|o|/ˈɒmɪkrɒn/|||||
|18|π|\pi|/paɪ/|||||
|19|ϖ|\varpi|/paɪ/|||||
|20|ρ|\rho|/roʊ/|||||
|21|ϱ|\varrho|/roʊ/|||||
|22|σ|\sigma|/ˈsɪɡmə/|||||
|23|ς|\varsigma|/ˈsɪɡmə/|||||
|24|τ|\tau|/taʊ, tɔː/|||||
|25|υ|\upsilon|/ˈʌpsɪlɒn/|||||
|26|ϕ|\phi|/faɪ/|||||
|27|φ|\varphi|/faɪ/|||||
|28|χ|\chi|/kaɪ/|||||
|29|ψ|\psi|/psaɪ/|||||
|30|ω|\omega|/oʊˈmeɪɡə/|||||

**注意:** MathJax 支持的大写希腊字母有限，如需其他（如大写 Alpha），可使用**罗马体**转换，如 `\mathrm{A}` 表示大写 Alpha：$\mathrm{A}$。

##### 2.1.2 希伯来字母 Hebrew alphabet

|序号|图标|LaTeX|英文|
|:-:|:-:|:--|:--|
|1|ℵ|\aleph|aleph|
|2|ℶ|\beth|beth|
|3|ℷ|\gimel|gimel|
|4|ℸ|\daleth|daleth|

##### 2.1.3 二元运算符 Binary operations

|序号|图标|LaTeX|序号|图标|LaTeX|
|:-:|:-:|:--|:-:|:-:|:--|
|1|+|+|20|∙|\bullet|
|2|−|-|21|⊕|\oplus|
|3|×|\times|22|⊖|\ominus|
|4|÷|\div|23|⊙|\odot|
|5|±|\pm|24|⊘|\oslash|
|6|∓|\mp|25|⊗|\otimes|
|7|◃|\triangleleft|26|◯|\bigcirc|
|8|▹|\triangleright|27|⋄|\diamond|
|9|⋅|\cdot|28|⊎|\uplus|
|10|∖|\setminus|29|△|\bigtriangleup|
|11|⋆|\star|30|▽|\bigtriangledown|
|12|∗|\ast|31|⊲|\lhd|
|13|∪|\cup|32|⊳|\rhd|
|14|∩|\cap|33|⊴|\unlhd|
|15|⊔|\sqcup|34|⊵|\unrhd|
|16|⊓|\sqcap|35|⨿|\amalg|
|17|∨|\vee|36|≀|\wr|
|18|∧|\wedge|37|†|\dagger|
|19|∘|\circ|38|‡|\ddagger|

##### 2.1.4 二元关系符 Binary relations

|序号|图标|LaTeX|序号|图标|LaTeX|
|:-:|:-:|:--|:-:|:-:|:--|
|1|=|=|49|⪈|\gneq|
|2|≠|\ne|50|≧|\geqq|
|3|≠|\neq|51|≱|\ngeq|
|4|≡|\equiv|52|≱|\ngeqq|
|5|≢|\not\equiv|53|≩|\gneqq|
|6|≐|\doteq|54|≩|\gvertneqq|
|7|≑|\doteqdot|55|≶|\lessgtr|
|8|= def|\overset{\underset{\mathrm{def}}{}}{=}|56|⋚|\lesseqgtr|
|9|:=|:=|57|⪋|\lesseqqgtr|
|10|∼|\sim|58|≷|\gtrless|
|11|≁|\nsim|59|⋛|\gtreqless|
|12|∽|\backsim|60|⪌|\gtreqqless|
|13|∼|\thicksim|61|⩽|\leqslant|
|14|≃|\simeq|62|⪇|\nleqslant|
|15|⋍|\backsimeq|63|⪕|\eqslantless|
|16|≂|\eqsim|64|⩾|\geqslant|
|17|≅|\cong|65|⪈|\ngeqslant|
|18|≇|\ncong|66|⪖|\eqslantgtr|
|19|≈|\approx|67|≲|\lesssim|
|20|≈|\thickapprox|68|⋦|\lnsim|
|21|≊|\approxeq|69|⪅|\lessapprox|
|22|≍|\asymp|70|⪉|\lnapprox|
|23|∝|\propto|71|≳|\gtrsim|
|24|∝|\varpropto|72|⋧|\gnsim|
|25|<|<|73|⪆|\gtrapprox|
|26|≮|\nless|74|⪊|\gnapprox|
|27|≪|\ll|75|≺|\prec|
|28|≪̸|\not\ll|76|⊀|\nprec|
|29|⋘|\lll|77|⪯|\preceq|
|30|⋘̸|\not\lll|78|⋠|\npreceq|
|31|⋖|\lessdot|79|⪵|\precneqq|
|32|>|>|80|≻|\succ|
|33|≯|\ngtr|81|⊁|\nsucc|
|34|≫|\gg|82|⪰|\succeq|
|35|≫̸|\not\gg|83|⋡|\nsucceq|
|36|⋙|\ggg|84|⪶|\succneqq|
|37|⋙̸|\not\ggg|85|≼|\preccurlyeq|
|38|⋗|\gtrdot|86|⋞|\curlyeqprec|
|39|≤|\le|87|≽|\succcurlyeq|
|40|≤|\leq|88|⋟|\curlyeqsucc|
|41|⪇|\lneq|89|≾|\precsim|
|42|≦|\leqq|90|⋨|\precnsim|
|43|≰|\nleq|91|⪷|\precapprox|
|44|≰|\nleqq|92|⪹|\precnapprox|
|45|≨|\lneqq|93|≿|\succsim|
|46|≨|\lvertneqq|94|⋩|\succnsim|
|47|≥|\ge|95|⪸|\succapprox|
|48|≥|\geq|96|⪺|\succnapprox|

##### 2.1.5 几何符号 Geometric symbols

|序号|图标|LaTeX|序号|图标|LaTeX|
|:-:|:-:|:--|:-:|:-:|:--|
|1|∥|\parallel|14|◊|\lozenge|
|2|∦|\nparallel|15|⧫|\blacklozenge|
|3|∥|\shortparallel|16|★|\bigstar|
|4|∦|\nshortparallel|17|◯|\bigcirc|
|5|⊥|\perp|18|△|\triangle|
|6|∠|\angle|19|△|\bigtriangleup|
|7|∢|\sphericalangle|20|▽|\bigtriangledown|
|8|∡|\measuredangle|21|△|\vartriangle|
|9|45 ∘|45^\circ|22|▽|\triangledown|
|10|◻|\Box|23|▴|\blacktriangle|
|11|◼|\blacksquare|24|▾|\blacktriangledown|
|12|⋄|\diamond|25|◂|\blacktriangleleft|
|13|◊|\Diamond \lozenge|26|▸|\blacktriangleright|

##### 2.1.6 逻辑符号 Logic symbols

|序号|图标|LaTeX|序号|图标|LaTeX|
|:-:|:-:|:--|:-:|:-:|:--|
|1|∀|\forall|20|¬|\neg|
|2|∃|\exists|21|The following macros are not allowed: operatorname<br><br>  <br><br>$\not\operatorname{R}$|\not\operatorname{R}|
|3|∄|\nexists|22|⊥|\bot|
|4|∴|\therefore|23|⊤|\top|
|5|∵|\because|24|⊢|\vdash|
|6|&|\And|25|⊣|\dashv|
|7|∨|\lor|26|⊨|\vDash|
|8|∨|\vee|27|⊩|\Vdash|
|9|⋎|\curlyvee|28|⊨|\models|
|10|⋁|\bigvee|29|⊪|\Vvdash|
|11|∧|\land|30|⊬|\nvdash|
|12|∧|\wedge|31|⊮|\nVdash|
|13|⋏|\curlywedge|32|⊭|\nvDash|
|14|⋀|\bigwedge|33|⊯|\nVDash|
|15|q ¯|\bar{q}|34|⌜|\ulcorner|
|16|a b c ¯|\bar{abc}|35|⌝|\urcorner|
|17|q ―|\overline{q}|36|⌞|\llcorner|
|18|a b c ―|\overline{abc}|37|⌟|\lrcorner|
|19|¬|\lnot||||

##### 2.1.7 集合 Sets

|序号|图标|LaTeX|序号|图标|LaTeX|
|:-:|:-:|:--|:-:|:-:|:--|
|1||{}|23|⊏|\sqsubset|
|2|∅|\emptyset|24|⊃|\supset|
|3|∅|\varnothing|25|⋑|\Supset|
|4|∈|\in|26|⊐|\sqsupset|
|5|∉|\notin|27|⊆|\subseteq|
|6|∋|\ni|28|⊈|\nsubseteq|
|7|∩|\cap|29|⊊|\subsetneq|
|8|⋒|\Cap|30|⊊|\varsubsetneq|
|9|⊓|\sqcap|31|⊑|\sqsubseteq|
|10|⋂|\bigcap|32|⊇|\supseteq|
|11|∪|\cup|33|⊉|\nsupseteq|
|12|⋓|\Cup|34|⊋|\supsetneq|
|13|⊔|\sqcup|35|⊋|\varsupsetneq|
|14|⋃|\bigcup|36|⊒|\sqsupseteq|
|15|⨆|\bigsqcup|37|⫅|\subseteqq|
|16|⊎|\uplus|38|⊈|\nsubseteqq|
|17|⨄|\biguplus|39|⫋|\subsetneqq|
|18|∖|\setminus|40|⫋|\varsubsetneqq|
|19|∖|\smallsetminus|41|⫆|\supseteqq|
|20|×|\times|42|⊉|\nsupseteqq|
|21|⊂|\subset|43|⫌|\supsetneqq|
|22|⋐|\Subset|44|⫌|\varsupsetneqq|

##### 2.1.8 箭头 Arrows

|序号|图标|LaTeX|序号|图标|LaTeX|
|:-:|:-:|:--|:-:|:-:|:--|
|1|⇛|\Rrightarrow|36|⟼|\longmapsto|
|2|⇚|\Lleftarrow|37|⇀|\rightharpoonup|
|3|⇒|\Rightarrow|38|⇁|\rightharpoondown|
|4|⇏|\nRightarrow|39|↼|\leftharpoonup|
|5|⟹|\Longrightarrow|40|↽|\leftharpoondown|
|6|⟹|\implies|41|↿|\upharpoonleft|
|7|⇐|\Leftarrow|42|↾|\upharpoonright|
|8|⇍|\nLeftarrow|43|⇃|\downharpoonleft|
|9|⟸|\Longleftarrow|44|⇂|\downharpoonright|
|10|⇔|\Leftrightarrow|45|⇌|\rightleftharpoons|
|11|⇎|\nLeftrightarrow|46|⇋|\leftrightharpoons|
|12|⟺|\Longleftrightarrow|47|↶|\curvearrowleft|
|13|⟺|\iff|48|↺|\circlearrowleft|
|14|⇑|\Uparrow|49|↰|\Lsh|
|15|⇓|\Downarrow|50|⇈|\upuparrows|
|16|⇕|\Updownarrow|51|⇉|\rightrightarrows|
|17|→|\rightarrow|52|⇄|\rightleftarrows|
|18|→|\to|53|↣|\rightarrowtail|
|19|↛|\nrightarrow|54|↬|\looparrowright|
|20|⟶|\longrightarrow|55|↷|\curvearrowright|
|21|←|\leftarrow|56|↻|\circlearrowright|
|22|←|\gets|57|↱|\Rsh|
|23|↚|\nleftarrow|58|⇊|\downdownarrows|
|24|⟵|\longleftarrow|59|⇇|\leftleftarrows|
|25|↔|\leftrightarrow|60|⇆|\leftrightarrows|
|26|↮|\nleftrightarrow|61|↢|\leftarrowtail|
|27|⟷|\longleftrightarrow|62|↫|\looparrowleft|
|28|↑|\uparrow|63|↪|\hookrightarrow|
|29|↓|\downarrow|64|↩|\hookleftarrow|
|30|↕|\updownarrow|65|⊸|\multimap|
|31|↗|\nearrow|66|↭|\leftrightsquigarrow|
|32|↙|\swarrow|67|⇝|\rightsquigarrow|
|33|↖|\nwarrow|68|↠|\twoheadrightarrow|
|34|↘|\searrow|69|↞|\twoheadleftarrow|
|35|↦|\mapsto||||

##### 2.1.9 特殊 Special

|序号|图标|LaTeX|序号|图标|LaTeX|
|:-:|:-:|:--|:-:|:-:|:--|
|1|∞|\infty|33|♭|\flat|
|2|ℵ|\aleph|34|♮|\natural|
|3|∁|\complement|35|♯|\sharp|
|4|∍|\backepsilon|36|╱|\diagup|
|5|ð|\eth|37|╲|\diagdown|
|6|Ⅎ|\Finv|38|⋅|\centerdot|
|7|ℏ|\hbar|39|⋉|\ltimes|
|8|ℑ|\Im|40|⋊|\rtimes|
|9|ı|\imath|41|⋋|\leftthreetimes|
|10|ȷ|\jmath|42|⋌|\rightthreetimes|
|11|k|\Bbbk|43|≖|\eqcirc|
|12|ℓ|\ell|44|≗|\circeq|
|13|℧|\mho|45|≜|\triangleq|
|14|℘|\wp|46|≏|\bumpeq|
|15|ℜ|\Re|47|≎|\Bumpeq|
|16|Ⓢ|\circledS|48|≑|\doteqdot|
|17|⨿|\amalg|49|≓|\risingdotseq|
|18||%|50|≒|\fallingdotseq|
|19|†|\dagger|51|⊺|\intercal|
|20|‡|\ddagger|52|⊼|\barwedge|
|21|…|\ldots|53|⊻|\veebar|
|22|⋯|\cdots|54|⩞|\doublebarwedge|
|23|⌣|\smile|55|≬|\between|
|24|⌢|\frown|56|⋔|\pitchfork|
|25|≀|\wr|57|⊲|\vartriangleleft|
|26|◃|\triangleleft|58|⋪|\ntriangleleft|
|27|▹|\triangleright|59|⊳|\vartriangleright|
|28|♢|\diamondsuit|60|⋫|\ntriangleright|
|29|♡|\heartsuit|61|⊴|\trianglelefteq|
|30|♣|\clubsuit|62|⋬|\ntrianglelefteq|
|31|♠|\spadesuit|63|⊵|\trianglerighteq|
|32|⅁|\Game|64|⋭|\ntrianglerighteq|

#### 2.2 运算与函数 Operations & Functions

##### 2.2.1 分数 Fractions

|类型|样式|LaTeX|
|:--|:--|:--|
|分数  <br>Fractions|2 4 x = 0.5 x|\frac{2}{4}x=0.5x or {2 \over 4}x=0.5x|
|小型分数  <br>Small fractions (force \textstyle)|2 4 x = 0.5 x|\tfrac{2}{4}x = 0.5x|
|大型分数（不嵌套）  <br>Large (normal) fractions (force \displaystyle)|2 4 = 0.5 2 c + 2 d + 2 4 = a|\dfrac{2}{4} = 0.5 \qquad \dfrac{2}{c + \dfrac{2}{d + \dfrac{2}{4}}} = a|
|大型分数（嵌套）  <br>Large (nested) fractions|2 c + 2 d + 2 4 = a|\cfrac{2}{c + \cfrac{2}{d + \cfrac{2}{4}}} = a|
|约分线的使用  <br>Cancellations in fractions|[![cancel3](https://camo.githubusercontent.com/8848b96086f260f483316e60d03f05f1d20856c008fb6fdbfc0959aed4cbdbfe/68747470733a2f2f6f7572736974652d7265736f757273652e6f73732d636e2d71696e6764616f2e616c6979756e63732e636f6d2f666f726d756c612d696d616765732f726561646d652f63616e63656c332e706e67)](https://camo.githubusercontent.com/8848b96086f260f483316e60d03f05f1d20856c008fb6fdbfc0959aed4cbdbfe/68747470733a2f2f6f7572736974652d7265736f757273652e6f73732d636e2d71696e6764616f2e616c6979756e63732e636f6d2f666f726d756c612d696d616765732f726561646d652f63616e63656c332e706e67)|\cfrac{x}{1 + \cfrac{\cancel{y}}{\cancel{y}}} = \cfrac{x}{2}|

**注意：** 其中 `\cancel` 命令需要**cancel 扩展包**支持，**cancel 扩展包**是一款自定义宏包，如需使用请在公式页面右上角【设置】处勾选后使用。

##### 2.2.2 标准数值函数 Standard numerical functions

|样式|LaTeX|
|:--|:--|
|exp a ⁡ b = a b , exp ⁡ b = e b , 10 m|\exp_a b = a^b, \exp b = e^b, 10^m|
|ln ⁡ c , lg ⁡ d = log ⁡ e , log 10 ⁡ f|\ln c, \lg d = \log e, \log_{10} f|
|sin ⁡ a , cos ⁡ b , tan ⁡ c , cot ⁡ d , sec ⁡ e , csc ⁡ f|\sin a, \cos b, \tan c, \cot d, \sec e, \csc f|
|arcsin ⁡ a , arccos ⁡ b , arctan ⁡ c|\arcsin a, \arccos b, \arctan c|
|The following macros are not allowed: operatorname<br><br>  <br><br>$\operatorname{arccot} d, \operatorname{arcsec} e, \operatorname{arccsc} f$|\operatorname{arccot} d, \operatorname{arcsec} e, \operatorname{arccsc} f|
|sinh ⁡ a , cosh ⁡ b , tanh ⁡ c , coth ⁡ d|\sinh a, \cosh b, \tanh c, \coth d|
|The following macros are not allowed: operatorname<br><br>  <br><br>$\operatorname{sh}k, \operatorname{ch}l, \operatorname{th}m, \operatorname{coth}n$|\operatorname{sh}k, \operatorname{ch}l, \operatorname{th}m, \operatorname{coth}n|
|The following macros are not allowed: operatorname<br><br>  <br><br>$\operatorname{argsh}o, \operatorname{argch}p, \operatorname{argth}q$|\operatorname{argsh}o, \operatorname{argch}p, \operatorname{argth}q|
|The following macros are not allowed: operatorname<br><br>  <br><br>$\operatorname{sgn}r, \left\vert s \right\vert$|\operatorname{sgn}r, \left\vert s \right\vert|
|min ( x , y ) , max ( x , y )|\min(x,y), \max(x,y)|

**注意：**LaTeX 和 MathJax 支持的操作符有限，如有特殊操作符，可以使用 `\operatorname{}` 命令自定义，例如

```
\operatorname{mydefine}x
```

The following macros are not allowed: operatorname

$$
\operatorname{mydefine}x
$$

##### 2.2.3 根式 Radicals

|样式|LaTeX|
|:--|:--|
|√|\surd|
|π|\sqrt{\pi}|
|π n|\sqrt[n]{\pi}|
|x 3 + y 3 2 3|\sqrt[3]{\frac{x^3+y^3}{2}}|

##### 2.2.4 微分与导数 Differentials and derivatives

|样式|LaTeX|
|:--|:--|
|d t , d t , ∂ t , ∇ ψ|dt, \mathrm{d}t, \partial t, \nabla\psi|
|d y / d x , d y / d x , d y d x , d y d x , ∂ 2 ∂ x 1 ∂ x 2 y|dy/dx, \mathrm{d}y/\mathrm{d}x, \frac{dy}{dx}, \frac{\mathrm{d}y}{\mathrm{d}x}, \frac{\partial^2}{\partial x_1\partial x_2}y|
|′ , ‵ , f ′ , f ′ , f ″ , f ( 3 ) , y ˙ , y ¨|\prime, \backprime, f^\prime, f', f'', f^{(3)}, \dot y, \ddot y|

##### 2.2.5 同余与模算术 Modular arithmetic

|样式|LaTeX|
|:--|:--|
|s k ≡ 0 ( mod m )|s_k \equiv 0 \pmod{m}|
|a mod b|a \bmod b|
|The following macros are not allowed: operatorname<br><br>  <br><br>$\gcd(m, n), \operatorname{lcm}(m, n)$|\gcd(m, n), \operatorname{lcm}(m, n)|
|∣ , ∤ , ∣ , ∤|\mid, \nmid, \shortmid, \nshortmid|

##### 2.2.6 极限 Limits

|样式|LaTeX|
|:--|:--|
|lim n → ∞ x n|\lim_{n \to \infty}x_n|
|lim n → ∞ x n|\textstyle \lim_{n \to \infty}x_n|

##### 2.2.7 界限与投影 Bounds and Projections

|样式|LaTeX|
|:--|:--|
|min x , max y , inf s , sup t|\min x, \max y, \inf s, \sup t|
|lim u , lim inf v , lim sup w|\lim u, \liminf v, \limsup w|
|dim ⁡ p , deg ⁡ q , det m , ker ⁡ ϕ|\dim p, \deg q, \det m, \ker\phi|
|Pr j , hom ⁡ l , ‖ z ‖ , arg ⁡ z|\Pr j, \hom l, \lVert z \rVert, \arg z|

##### 2.2.8 积分 Integral

|样式|LaTeX|
|:--|:--|
|∫ 1 3 e 3 / x x 2 , d x|\int\limits_{1}^{3}\frac{e^3/x}{x^2}, dx|
|∫ 1 3 e 3 / x x 2 , d x|\int_{1}^{3}\frac{e^3/x}{x^2}, dx|
|∫ − N N e x d x|\textstyle \int\limits_{-N}^{N} e^x dx|
|∫ − N N e x d x|\textstyle \int_{-N}^{N} e^x dx|
|∬ D d x , d y|\iint\limits_D dx,dy|
|∭ E d x , d y , d z|\iiint\limits_E dx,dy,dz|
|⨌ F d x , d y , d z , d t|\iiiint\limits_F dx,dy,dz,dt|
|∫ ( x , y ) ∈ C x 3 , d x + 4 y 2 , d y|\int_{(x,y)\in C} x^3, dx + 4y^2, dy|
|∮ ( x , y ) ∈ C x 3 , d x + 4 y 2 , d y|\oint_{(x,y)\in C} x^3, dx + 4y^2, dy|

**注意：**积分符号可以使用 `\int_{}^{}` 命令调用，如需双重积分符号只需将 `int` 替换成 `iint` 即可，以此类推，最高支持四重。曲线积分可使用 `\oint` 命令调用，但曲面积分符号在 MathJax 环境中并不支持 `\oiint` 的用法，但仍可通过 `\unicode{}` 命令，即 Unicode 代码的方式进行调用（前提是您需要在设置中打开 Unicode 扩展），具体使用方法如下：

```
\unicode{8751}  \unicode{x222F}_C %曲面积分符号的Unicode码十进制为8751,十六进制为x222F(注意x标识符)
```

[![unicode2](https://camo.githubusercontent.com/68252c9e3f125e7b57fb493172c5071f83609837f657ac0ff6b05b878b4ff3c6/68747470733a2f2f6f7572736974652d7265736f757273652e6f73732d636e2d71696e6764616f2e616c6979756e63732e636f6d2f666f726d756c612d696d616765732f726561646d652f756e69636f6465322e706e67)](https://camo.githubusercontent.com/68252c9e3f125e7b57fb493172c5071f83609837f657ac0ff6b05b878b4ff3c6/68747470733a2f2f6f7572736974652d7265736f757273652e6f73732d636e2d71696e6764616f2e616c6979756e63732e636f6d2f666f726d756c612d696d616765732f726561646d652f756e69636f6465322e706e67)

```
\unicode{8752}  \unicode{x2230}_C %三维曲面积分符号的Unicode码十进制为8752,十六进制为x2230
```

[![unicode3](https://camo.githubusercontent.com/f1914e9ae320a47993b29dcbf5adee40c780400ddb1d6630eca55c8ea8bc6927/68747470733a2f2f6f7572736974652d7265736f757273652e6f73732d636e2d71696e6764616f2e616c6979756e63732e636f6d2f666f726d756c612d696d616765732f726561646d652f756e69636f6465332e706e67)](https://camo.githubusercontent.com/f1914e9ae320a47993b29dcbf5adee40c780400ddb1d6630eca55c8ea8bc6927/68747470733a2f2f6f7572736974652d7265736f757273652e6f73732d636e2d71696e6764616f2e616c6979756e63732e636f6d2f666f726d756c612d696d616765732f726561646d652f756e69636f6465332e706e67)

其他积分符号：

```
\unicode{8753} \unicode{x2231}_c
\unicode{8754} \unicode{x2232}_c
\unicode{8755} \unicode{x2233}_c
```

[![unicode4](https://camo.githubusercontent.com/8f7abd329c25908a102de097e13a02323a3267a6004451867571978fccbb4b64/68747470733a2f2f6f7572736974652d7265736f757273652e6f73732d636e2d71696e6764616f2e616c6979756e63732e636f6d2f666f726d756c612d696d616765732f726561646d652f756e69636f6465342e706e67)](https://camo.githubusercontent.com/8f7abd329c25908a102de097e13a02323a3267a6004451867571978fccbb4b64/68747470733a2f2f6f7572736974652d7265736f757273652e6f73732d636e2d71696e6764616f2e616c6979756e63732e636f6d2f666f726d756c612d696d616765732f726561646d652f756e69636f6465342e706e67)

##### 2.2.9 其他大型运算 Large operators

|类别|样式|LaTeX|
|:--|:--|:--|
|求和 Summation|∑ a b|\sum_{a}^{b}|
|求和 Summation|∑ a b|\textstyle \sum_{a}^{b}|
|连乘积 Product|∏ a b|\prod_{a}^{b}|
|连乘积 Product|∏ a b|\textstyle \prod_{a}^{b}|
|余积 Coproduct|∐ a b|\coprod_{a}^{b}|
|余积 Coproduct|∐ a b|\textstyle \coprod_{a}^{b}|
|并集 Union|⋃ a b|\bigcup_{a}^{b}|
|并集 Union|⋃ a b|\textstyle \bigcup_{a}^{b}|
|交集 Intersection|⋂ a b|\bigcap_{a}^{b}|
|交集 Intersection|⋂ a b|\textstyle \bigcap_{a}^{b}|
|析取 Disjunction|⋁ a b|\bigvee_{a}^{b}|
|析取 Disjunction|⋁ a b|\textstyle \bigvee_{a}^{b}|
|合取 Conjunction|⋀ a b|\bigwedge_{a}^{b}|
|合取 Conjunction|⋀ a b|\textstyle \bigwedge_{a}^{b}|

#### 2.3 上下标 Sub & Super

|类型|样式|代码|
|:--|:--|:--|
|上标 Superscript|a 2 , a x + 3|a^2, a^{x+3}|
|下标 Subscript|a 2|a_2|
|组合 Grouping|10 30 a 2 + 2|10^{30} a^{2+2}|
|a i , j b f ′|a_{i,j} b_{f'}||
|上下标混合 Combining sub & super without and with horizontal separation|x 2 3|x_2^3|
|x 2 3|{x_2}^3||
|上标的上标 Super super|10 10 8|10^{10^{8}}|
|混合标识 Preceding and/or additional sub & super|1 2 X 3 4 a b|\sideset{_1^2}{_3^4}X_a^b|
|1 2 ! Ω 3 4|{}_1^2!\Omega_3^4||
|顶标底标 Stacking|ω α|\overset{\alpha}{\omega}|
|ω α|\underset{\alpha}{\omega}||
|ω γ α|\overset{\alpha}{\underset{\gamma}{\omega}}||
|ω α|\stackrel{\alpha}{\omega}||
|导数 Derivatives|x ′ , y ″ , f ′ , f ″|x', y'', f', f''|
|x ′ , y ′ ′|x^\prime, y^{\prime\prime}||
|导数 Derivative dots|x ˙ , x ¨|\dot{x}, \ddot{x}|
|下划线、上划线与向量  <br>Underlines, overlines, vectors|a ^   b ¯   c →|\hat a \ \bar b \ \vec c|
|a b →   c d ←   d e f ^|\overrightarrow{a b} \ \overleftarrow{c d} \ \widehat{d e f}||
|g h i ―   j k l ―|\overline{g h i} \ \underline{j k l}||
|弧度 Arc (workaround)|A B ⌢|\overset{\frown} {AB}|
|箭头 Arrows|A ← n + μ − 1 B → T n ± i − 1 C|A \xleftarrow{n+\mu-1} B \xrightarrow[T]{n\pm i-1} C|
|大括号 Overbraces|1 + 2 + ⋯ + 100 ⏞ 5050|\overbrace{ 1+2+\cdots+100 }^{5050}|
|底部大括号 Underbraces|a + b + ⋯ + z ⏟ 26|\underbrace{ a+b+\cdots+z }_{26}|
|求和运算 Sum|∑ k = 1 N k 2|\sum_{k=1}^N k^2|
|文本模式下的求和运算 Sum (force \textstyle)|∑ k = 1 N k 2|\textstyle \sum_{k=1}^N k^2|
|分式中的求和运算 Sum in a fraction (default \textstyle)|∑ k = 1 N k 2 a|\frac{\sum_{k=1}^N k^2}{a}|
|分式中的求和运算 Sum in a fraction (force \displaystyle)|∑ k = 1 N k 2 a|\frac{\displaystyle \sum_{k=1}^N k^2}{a}|
|分式中的求和运算 Sum in a fraction (alternative limits style)|∑ k = 1 N k 2 a|\frac{\sum\limits^{^N}_{k=1} k^2}{a}|
|乘积运算 Product|∏ i = 1 N x i|\prod_{i=1}^N x_i|
|乘积运算 Product (force \textstyle)|∏ i = 1 N x i|\textstyle \prod_{i=1}^N x_i|
|副乘运算 Coproduct|∐ i = 1 N x i|\coprod_{i=1}^N x_i|
|副乘运算 Coproduct (force \textstyle)|∐ i = 1 N x i|\textstyle \coprod_{i=1}^N x_i|
|极限 Limit|lim n → ∞ x n|\lim_{n \to \infty}x_n|
|极限 Limit (force \textstyle)|lim n → ∞ x n|\textstyle \lim_{n \to \infty}x_n|
|积分 Integral|∫ 1 3 e 3 / x x 2 , d x|\int\limits_{1}^{3}\frac{e^3/x}{x^2}, dx|
|积分 Integral (alternative limits style)|∫ 1 3 e 3 / x x 2 , d x|\int_{1}^{3}\frac{e^3/x}{x^2}, dx|
|积分 Integral (force \textstyle)|∫ − N N e x d x|\textstyle \int\limits_{-N}^{N} e^x dx|
|积分 Integral (force \textstyle, alternative limits style)|∫ − N N e x d x|\textstyle \int_{-N}^{N} e^x dx|
|双重积分 Double integral|∬ D d x , d y|\iint\limits_D dx,dy|
|三重积分 Triple integral|∭ E d x , d y , d z|\iiint\limits_E dx,dy,dz|
|四重积分 Quadruple integral|⨌ F d x , d y , d z , d t|\iiiint\limits_F dx,dy,dz,dt|
|路径积分 Line or path integral|∫ ( x , y ) ∈ C x 3 , d x + 4 y 2 , d y|\int_{(x,y)\in C} x^3, dx + 4y^2, dy|
|环路积分 Closed line or path integral|∮ ( x , y ) ∈ C x 3 , d x + 4 y 2 , d y|\oint_{(x,y)\in C} x^3, dx + 4y^2, dy|
|交集 Intersections|⋂ i = 1 n E i|\bigcap_{i=1}^n E_i|
|并集 Unions|⋃ i = 1 n E i|\bigcup_{i=1}^n E_i|

#### 2.4 矩阵与多行列式 Matrices & Multilines

|类型|样式|LaTeX|
|:--|:--|:--|
|二项式系数  <br>Binomial coefficients|( n k )|\binom{n}{k}|
|小型二项式系数  <br>Small binomial coefficients (force \textstyle)|( n k )|\tbinom{n}{k}|
|大型二项式系数  <br>Large (normal) binomial coefficients (force \displaystyle)|( n k )|\dbinom{n}{k}|
|矩阵  <br>Matrices|$\begin{matrix} x & y \z & v\end{matrix}$|\begin{matrix}  <br>x & y \\  <br>z & v  <br>\end{matrix}|
|$\begin{vmatrix} x & y \ z & v \end{vmatrix}$|\begin{vmatrix}  <br>x & y \\  <br>z & v  <br>\end{vmatrix}||
|$\begin{Vmatrix} x & y \ z & v \end{Vmatrix} $|"\begin{Vmatrix}  <br>x & y \\  <br>z & v  <br>\end{Vmatrix}||
|$\begin{bmatrix} 0 & \cdots & 0 \ \vdots & \ddots & \vdots \ 0 & \cdots & 0 \end{bmatrix}$|\begin{bmatrix}  <br>0 & \cdots & 0 \\  <br>\vdots & \ddots & \vdots \\  <br>0 & \cdots & 0  <br>\end{bmatrix}||
|$\begin{Bmatrix} x & y \ z & v \end{Bmatrix}$|\begin{Bmatrix}  <br>x & y \\  <br>z & v  <br>\end{Bmatrix}||
|$\begin{pmatrix} x & y \ z & v \end{pmatrix}$|\begin{pmatrix}  <br>x & y \\  <br>z & v  <br>\end{pmatrix}||
|$\bigl( \begin{smallmatrix} a&b\ c&d \end{smallmatrix} \bigr)$|\bigl( \begin{smallmatrix}  <br>a&b\\  <br>c&d  <br>\end{smallmatrix} \bigr)||
|条件定义  <br>Case distinctions|$f(n) =\begin{cases} n/2, & \text{if }n\text{ is even} \ 3n+1, & \text{if }n\text{ is odd} \end{cases}$|f(n) =  <br>\begin{cases}  <br>n/2, & \text{if }n\text{ is even} \\  <br>3n+1, & \text{if }n\text{ is odd}  <br>\end{cases}|
|多行等式  <br>Multiline equations|$\begin{align} f(x) & = (a+b)^2 \ & = a^2+2ab+b^2 \ \end{align}$|\begin{align}  <br>f(x) & = (a+b)^2\\  <br>& = a^2+2ab+b^2 \\  <br>\end{align}|
|$\begin{alignat}{2} f(x) & = (a-b)^2 \ & = a^2-2ab+b^2 \ \end{alignat}$|\begin{alignat}{2}  <br>f(x) & = (a-b)^2 \\  <br>& = a^2-2ab+b^2 \\  <br>\end{alignat}||
|$\begin{array}{lcl} z & = & a \ f(x,y,z) & = & x + y + z \end{array}$|\begin{array}{lcl}  <br>z & = & a \\  <br>f(x,y,z) & = & x + y + z  <br>\end{array}||
|$\begin{array}{lcr} z & = & a \ f(x,y,z) & = & x + y + z \end{array}$|\begin{array}{lcr}  <br>z & = & a \\  <br>f(x,y,z) & = & x + y + z  <br>\end{array}||
|方程组  <br>Simultaneous equations|$\begin{cases} 3x + 5y + z \ 7x - 2y + 4z \ -6x + 3y + 2z \end{cases}$|\begin{cases}  <br>3x + 5y + z \\  <br>7x - 2y + 4z \\  <br>-6x + 3y + 2z  <br>\end{cases}|
|数组  <br>Arrays|$\begin{array}{|c|

#### 2.5 括号 Brackets

常用的括号符号例如 `( )[ ]{ }……` 这些也可以在输入环境中直接使用：

```
2(x+y)=z
```

2 ( x + y ) = z

但如果是在较大的表达式中这些符号就显得不合适了

```
( \frac{\pi}{2} )^n
```

( π 2 ) n

正确用法应配合 `\left` 和 `\right` 命令使用。

```
\left ( \frac{\pi}{2} \right )^n
```

( π 2 ) n

具体可参考下表。

|类型|样式|LaTeX|
|:--|:--|:--|
|圆括号、小括号  <br>Parentheses|( a b )|\left ( \frac{a}{b} \right )|
|方括号、中括号  <br>Brackets|[ a b ] [ a b ]|\left [ \frac{a}{b} \right ] \quad  <br>\left \lbrack \frac{a}{b} \right \rbrack|
|花括号、大括号  <br>Braces|Missing or unrecognized delimiter for \left<br><br>  <br><br>$\left { \frac{a}{b} \right } \quad \left \lbrace \frac{a}{b} \right \rbrace$|\left { \frac{a}{b} \right } \quad  <br>\left \lbrace \frac{a}{b} \right \rbrace|
|角括号  <br>Angle brackets|⟨ a b ⟩|\left \langle \frac{a}{b} \right \rangle|
|单竖线和双竖线  <br>Bars and double bars|$\left|\frac{a}{b} \right \vert \quad \left \Vert \frac{c}{d} \right \|$|
|取整函数与取顶函数  <br>Floor and ceiling functions:|⌊ a b ⌋ ⌈ c d ⌉|\left \lfloor \frac{a}{b} \right \rfloor \quad  <br>\left \lceil \frac{c}{d} \right \rceil|
|斜线与反斜线  <br>Slashes and backslashes|/ a b \|\left / \frac{a}{b} \right \backslash|
|上下箭头  <br>Up, down, and up-down arrows|↑ a b ↓ ⇑ a b ⇓ ↕ a b ⇕|\left \uparrow \frac{a}{b} \right \downarrow \quad  <br>\left \Uparrow \frac{a}{b} \right \Downarrow \quad  <br>\left \updownarrow \frac{a}{b} \right \Updownarrow|
|混合括号  <br>Delimiters can be mixed,as long as \left and \right match|$\left [ 0,1 \right ) \left \langle \psi \right|$|
|如果您不希望某一侧括号显示，可以使用\left. 和 \right.（带有英文句号）  <br>Use \left. and \right. if you do not want a delimiter to appear|Missing or unrecognized delimiter for \right<br><br>  <br><br>$\left . \frac{A}{B} \right } \to X$|\left . \frac{A}{B} \right } \to X|
|括号的大小  <br>Size of the delimiters (add "l" or "r" to indicate the side for proper spacing)|( ( ( ( ( … ] ] ] ] ]|( \bigl( \Bigl( \biggl( \Biggl( \dots \Biggr] \biggr] \Bigr] \bigr] ]|
|Missing close brace<br><br>  <br><br>${ \bigl{ \Bigl{ \biggl{ \Biggl{ \dots \Biggr\rangle \biggr\rangle \Bigr\rangle \bigr\rangle \rangle$|{ \bigl{ \Bigl{ \biggl{ \Biggl{ \dots  <br>\Biggr\rangle \biggr\rangle \Bigr\rangle \bigr\rangle \rangle||
|$\| \big\| \Big\| \bigg\| \Bigg\| \dots \Bigg|\bigg|\Big|
|⌊ ⌊ ⌊ ⌊ ⌊ … ⌉ ⌉ ⌉ ⌉ ⌉|\lfloor \bigl\lfloor \Bigl\lfloor \biggl\lfloor \Biggl\lfloor \dots  <br>\Biggr\rceil \biggr\rceil \Bigr\rceil \bigr\rceil \rceil||
|↑ ↑ ↑ ↑ ↑ ⋯ ⇓ ⇓ ⇓ ⇓ ⇓|\uparrow \big\uparrow \Big\uparrow \bigg\uparrow \Bigg\uparrow \dots  <br>\Bigg\Downarrow \bigg\Downarrow \Big\Downarrow \big\Downarrow \Downarrow||
|↕ ↕ ↕ ↕ ↕ ⋯ ⇕ ⇕ ⇕ ⇕ ⇕|\updownarrow \big\updownarrow \Big\updownarrow \bigg\updownarrow \Bigg\updownarrow \dots  <br>\Bigg\Updownarrow \bigg\Updownarrow \Big\Updownarrow \big\Updownarrow \Updownarrow||
|/ / / / / … \ \ \ \ ∖|/ \big/ \Big/ \bigg/ \Bigg/ \dots  <br>\Bigg\backslash \bigg\backslash \Big\backslash \big\backslash \backslash||

#### 2.6 空格与换行 Spacing & Line breaking

##### 2.6.1 空格 Spacing

MathJax 能够自动处理大多数空格间距的大小，但如果您需要自己控制，可参考下表。

序号 | 样式 | LaTeX | 中文说明英文说明 :----: | :----: | :---- | :---- | :---- 1 | a b | a \qquad b | 双空格 | double quad space 2 | a b | a \quad b | 单空格 | quad space 3 | a   b | a\ b | 字符空格 | text space 4 | a   b | a \text{ } b | 文本模式中的字符空格 | text space in text mode 5 | a ; b | a;b | 大空格 | large space 6 | a , b | a,b | 小空格 | small space 7 | a b | ab | 极小空格 (用于乘因子) | tiny space (use for multiplication of factors) 8 | a b | a b | 极小空格 (用于区分其它语法) | tiny space (syntax space ignored) 9 | ab | \mathit{ab} | 没有空格 (用于多字母变量) | no space (use for multi-letter variables) 10 | a ! b | a!b | 负空格 | small negative space

##### 2.6.2 换行 Line breaking

在 MathJax3.0 中取消了使用 `\\` 进行强制换行的功能，因此本页面也采取同样的逻辑，默认为单行公式环境。`\\` 强制换行命令只在支持多行编辑的数学环境中才起作用，如 `eqnarray` 环境、`align` 环境、`array` 环境、`matrix` 环境等等。如您需要显示多行公式，请在此类环境中输入公式，具体用法参见章节 [2.10](#2.10 LaTeX 环境 LaTeX environments)。

#### 2.7 颜色 Colors

##### 2.7.1 字体颜色 Font colors

在公式中可以使用 `\color{options}{math}` 来调用颜色命令，第一个参数为颜色，第二个参数为公式或文本内容。例如:

```
{\color{Blue}x^2}+{\color{Orange}2x}-{\color{LimeGreen}1}
```

$$ {\color{Blue}x^2}+{\color{Orange}2x}-{\color{LimeGreen}1} $$

```
x_{1,2}=\frac{{\color{Blue}-b}\pm\sqrt{\color{Red}b^2-4ac}}{\color{Green}2a }
```

x 1 , 2 = \color B l u e − b ± \color R e d b 2 − 4 a c \color G r e e n 2 a

**注意：** 使用 `\color` 命令时，请将需要设置颜色的部分用 `{ }` 整体扩住，以表明 `\color` 函数作用范围。

##### 2.7.2 背景颜色 Background color

在文本环境中可以使用 `\colorbox{options}{text}` 来调用背景颜色命令，第一个参数为颜色，第二个颜色为文本内容。例如：

```
\colorbox{yellow}{Thistext}
```

The following macros are not allowed: colorbox

$$
\colorbox{yellow}{text}
$$

**注意：** 若需要在数学环境中使用 `\colorbox{}{}`，请在第二个参数内加入 `$\displaystyle + 公式$`，例如：

```
\colorbox{yellow}{$\displaystyle \frac{a}{b}$}`
```

The following macros are not allowed: colorbox

$$
\colorbox{yellow}{$\displaystyle \frac{a}{b}$}
$$

或者您可以使用 **Bbox 扩展** 来替换 `\colorbox` 命令，详见下条 2.7.3。

##### 2.7.3 用 Bbox 扩展设置背景颜色 Setting background color with Bbox

Bbox 扩展是一款自定义宏包，如需使用请在公式页面右上角【设置】处勾选后使用。 具体用法如下：

###### 2.7.3.1 设置背景颜色 Setting Background color

在公式中可以使用 `\bbox[options]{math}` 来调用背景颜色命令，第一个参数为颜色或大小，需注意用 `[ ]` 包围，第二个参数为公式。例如:

```
\bbox[red]{x+y}
```

[![bbox1](https://camo.githubusercontent.com/a7a1e237ebf8f647815da1203274f6270b9a1c219700b17ad373d1e75fd00305/68747470733a2f2f6f7572736974652d7265736f757273652e6f73732d636e2d71696e6764616f2e616c6979756e63732e636f6d2f666f726d756c612d696d616765732f726561646d652f62626f78312e706e67)](https://camo.githubusercontent.com/a7a1e237ebf8f647815da1203274f6270b9a1c219700b17ad373d1e75fd00305/68747470733a2f2f6f7572736974652d7265736f757273652e6f73732d636e2d71696e6764616f2e616c6979756e63732e636f6d2f666f726d756c612d696d616765732f726561646d652f62626f78312e706e67)

###### 2.7.3.2 调整背景大小 Setting Background Size

默认情况下，背景大小为作用范围的最大边界，如需扩大背景，可在第一个参数中加入大小信息，例如：

```
\bbox[2pt]{x+y}  %设置透明背景，并增加2pt额外距离
```

[![bbox2](https://camo.githubusercontent.com/b7636de86337793fcf1d13f5b14de7db49b665aaccc2a4c1e6991a0f3809f111/68747470733a2f2f6f7572736974652d7265736f757273652e6f73732d636e2d71696e6764616f2e616c6979756e63732e636f6d2f666f726d756c612d696d616765732f726561646d652f62626f78322e706e67)](https://camo.githubusercontent.com/b7636de86337793fcf1d13f5b14de7db49b665aaccc2a4c1e6991a0f3809f111/68747470733a2f2f6f7572736974652d7265736f757273652e6f73732d636e2d71696e6764616f2e616c6979756e63732e636f6d2f666f726d756c612d696d616765732f726561646d652f62626f78322e706e67)

```
\bbox[red,5pt]{x+y}  %设置红色背景，并增加5pt额外距离
```

[![bbox3](https://camo.githubusercontent.com/cd3081fa22536059245b02ba097656facd330703b91e048f777d5fd46a06dc19/68747470733a2f2f6f7572736974652d7265736f757273652e6f73732d636e2d71696e6764616f2e616c6979756e63732e636f6d2f666f726d756c612d696d616765732f726561646d652f62626f78332e706e67)](https://camo.githubusercontent.com/cd3081fa22536059245b02ba097656facd330703b91e048f777d5fd46a06dc19/68747470733a2f2f6f7572736974652d7265736f757273652e6f73732d636e2d71696e6764616f2e616c6979756e63732e636f6d2f666f726d756c612d696d616765732f726561646d652f62626f78332e706e67)

##### 2.7.4 默认支持颜色 Colors supported

|支|持|颜|色|
|:--|:--|:--|:--|
|\color A p r i c o t A p r i c o t|\color E m e r a l d E m e r a l d|\color O l i v e G r e e n O l i v e G r e e n|\color R u b i n e R e d R u b i n e R e d|
|\color A q u a m a r i n e A q u a m a r i n e|\color F o r e s t G r e e n F o r e s t G r e e n|\color O r a n g e O r a n g e|\color S a l m o n S a l m o n|
|\color B i t t e r s w e e t B i t t e r s w e e t|\color F u c h s i a F u c h s i a|\color O r a n g e R e d O r a n g e R e d|\color S e a G r e e n S e a G r e e n|
|\color B l a c k B l a c k|\color G o l d e n r o d G o l d e n r o d|\color O r c h i d O r c h i d|\color S e p i a S e p i a|
|\color B l u e B l u e|\color G r a y G r a y|\color P e a c h P e a c h|\color S k y B l u e S k y B l u e|
|\color B l u e G r e e n B l u e G r e e n|\color G r e e n G r e e n|\color P e r i w i n k l e P e r i w i n k l e|\color S p r i n g G r e e n S p r i n g G r e e n|
|\color B l u e V i o l e t B l u e V i o l e t|\color G r e e n Y e l l o w G r e e n Y e l l o w|\color P i n e G r e e n P i n e G r e e n|\color T a n T a n|
|\color B r i c k R e d B r i c k R e d|\color J u n g l e G r e e n J u n g l e G r e e n|\color P l u m P l u m|\color T e a l B l u e T e a l B l u e|
|\color B r o w n B r o w n|\color L a v e n d e r L a v e n d e r|\color P r o c e s s B l u e P r o c e s s B l u e|\color T h i s t l e T h i s t l e|
|\color B u r n t O r a n g e B u r n t O r a n g e|\color L i m e G r e e n L i m e G r e e n|\color P u r p l e P u r p l e|\color T u r q u o i s e T u r q u o i s e|
|\color C a d e t B l u e C a d e t B l u e|\color M a g e n t a M a g e n t a|\color R a w S i e n n a R a w S i e n n a|\color V i o l e t V i o l e t|
|\color C a r n a t i o n P i n k C a r n a t i o n P i n k|\color M a h o g a n y M a h o g a n y|\color R e d R e d|\color V i o l e t R e d V i o l e t R e d|
|\color C e r u l e a n C e r u l e a n|\color M a r o o n M a r o o n|\color R e d O r a n g e R e d O r a n g e|\color W h i t e W h i t e|
|\color C o r n f l o w e r B l u e C o r n f l o w e r B l u e|\color M e l o n M e l o n|\color R e d V i o l e t R e d V i o l e t|\color W i l d S t r a w b e r r y W i l d S t r a w b e r r y|
|\color C y a n C y a n|\color M i d n i g h t B l u e M i d n i g h t B l u e|\color R h o d a m i n e R h o d a m i n e|\color Y e l l o w Y e l l o w|
|\color D a n d e l i o n D a n d e l i o n|\color M u l b e r r y M u l b e r r y|\color R o y a l B l u e R o y a l B l u e|\color Y e l l o w G r e e n Y e l l o w G r e e n|
|\color D a r k O r c h i d D a r k O r c h i d|\color N a v y B l u e N a v y B l u e|\color R o y a l P u r p l e R o y a l P u r p l e|\color Y e l l o w O r a n g e Y e l l o w O r a n g e|

##### 2.7.5 使用 RGB 颜色 Use RGB color

如需在 `\color` 命令中使用自选 RGB 颜色，可使用 `{\color[RGB]{0,0,0} }` 命令，例如：

```
{\color[RGB]{0,200,0} e^{i \pi} + 1 = 0} 
```

\color [ R G B ] 0 , 200 , 0 e i π + 1 = 0

##### 2.7.6 自定义颜色 Custom colors

可使用 `\definecolor` 命令进行自定义颜色，例如：

```
\definecolor{mygreen}{RGB}{0,200,0} {\color{mygreen}e^{i \pi} + 1 = 0 } 
```

The following macros are not allowed: definecolor

$$
\definecolor{mygreen}{RGB}{0,200,0} {\color{mygreen}e^{i \pi} + 1 = 0 }
$$

#### 2.8 字体字号 Fonts & Size

##### 2.8.1 字体 Fonts

如您需要替换公式内容的字体，可以点击工具栏下方的**【字体】**按钮进行相关操作。因有一些特定代码 Mathjax3.0 并没有相关支持，所以下表仅做参考。

|样式|LaTeX|
|:--|:--|
|希腊字母 Greek alphabet||
|A B Γ Δ E Z H Θ|\mathrm{A} \mathrm{B} \Gamma \Delta \mathrm{E} \mathrm{Z} \mathrm{H} \Theta|
|I K Λ M N Ξ O Π|\mathrm{I} \mathrm{K} \Lambda \mathrm{M} \mathrm{N} \Xi \mathrm{O} \Pi|
|R Σ T Υ Φ X Ψ Ω|\mathrm{R} \Sigma \mathrm{T} \Upsilon \Phi \mathrm{X} \Psi \Omega|
|α β γ δ ϵ ζ η θ|\alpha \beta \gamma \delta \epsilon \zeta \eta \theta|
|ι κ λ μ ν ξ ο π|\iota \kappa \lambda \mu \nu \xi \omicron \pi|
|ρ σ τ υ ϕ χ ψ ω|\rho \sigma \tau \upsilon \phi \chi \psi \omega|
|Γ Δ Θ Λ Ξ Π Σ Φ Υ Ω|\varGamma \varDelta \varTheta \varLambda \varXi \varPi \varSigma \varPhi \varUpsilon \varOmega|
|ε ϝ ϰ ϖ ϱ ς ϑ φ|\varepsilon \digamma \varkappa \varpi \varrho \varsigma \vartheta \varphi|
|希伯来字母 Hebrew symbols||
|ℵ ℶ ℷ ℸ|\aleph \beth \gimel \daleth|
|黑板报体 Blackboard bold/scripts||
|ABCDEFGHI|\mathbb{ABCDEFGHI}|
|JKLMNOPQR|\mathbb{JKLMNOPQR}|
|STUVWXYZ|\mathbb{STUVWXYZ}|
|粗体 Boldface||
|ABCDEFGHI|\mathbf{ABCDEFGHI}|
|JKLMNOPQR|\mathbf{JKLMNOPQR}|
|STUVWXYZ|\mathbf{STUVWXYZ}|
|abcdefghijklm|\mathbf{abcdefghijklm}|
|nopqrstuvwxyz|\mathbf{nopqrstuvwxyz}|
|0123456789|\mathbf{0123456789}|
|粗体希腊字母 Boldface (Greek)||
|$\boldsymbol{\mathrm{A} \mathrm{B} \Gamma \Delta \mathrm{E} \mathrm{Z} \mathrm{H} \Theta}$|\boldsymbol{\mathrm{A} \mathrm{B} \Gamma \Delta \mathrm{E} \mathrm{Z} \mathrm{H} \Theta}|
|\boldsymbol I K Λ M N Ξ O Π|\boldsymbol{\mathrm{I} \mathrm{K} \Lambda \mathrm{M} \mathrm{N} \Xi \mathrm{O} \Pi}|
|\boldsymbol R Σ T Υ Φ X Ψ Ω|\boldsymbol{\mathrm{R} \Sigma \mathrm{T} \Upsilon \Phi \mathrm{X} \Psi \Omega}|
|\boldsymbol α β γ δ ϵ ζ η θ|\boldsymbol{\alpha \beta \gamma \delta \epsilon \zeta \eta \theta}|
|\boldsymbol ι κ λ μ ν ξ ο π|\boldsymbol{\iota \kappa \lambda \mu \nu \xi \omicron \pi}|
|\boldsymbol ρ σ τ υ ϕ χ ψ ω|\boldsymbol{\rho \sigma \tau \upsilon \phi \chi \psi \omega}|
|\boldsymbol ε ϝ ϰ ϖ|\boldsymbol{\varepsilon\digamma\varkappa\varpi}|
|\boldsymbol ϱ ς ϑ φ|\boldsymbol{\varrho\varsigma\vartheta\varphi}|
|斜体 Italics (拉丁字母默认 default for Latin alphabet)||
|0123456789|\mathit{0123456789}|
|罗马体 Roman typeface|Roman typeface|
|ABCDEFGHI|\mathrm{ABCDEFGHI}|
|JKLMNOPQR|\mathrm{JKLMNOPQR}|
|STUVWXYZ|\mathrm{STUVWXYZ}|
|abcdefghijklm|\mathrm{abcdefghijklm}|
|nopqrstuvwxyz|\mathrm{nopqrstuvwxyz}|
|0123456789|\mathrm{0123456789}|
|无衬线体 Sans serif||
|ABCDEFGHI|\mathsf{ABCDEFGHI}|
|JKLMNOPQR|\mathsf{JKLMNOPQR}|
|STUVWXYZ|\mathsf{STUVWXYZ}|
|abcdefghijklm|\mathsf{abcdefghijklm}|
|nopqrstuvwxyz|\mathsf{nopqrstuvwxyz}|
|0123456789|\mathsf{0123456789}|
|手写体 Calligraphy/花体 script||
|ABCDEFGHI|\mathcal{ABCDEFGHI}|
|JKLMNOPQR|\mathcal{JKLMNOPQR}|
|STUVWXYZ|\mathcal{STUVWXYZ}|
|德文尖角体 Fraktur typeface||
|ABCDEFGHI|\mathfrak{ABCDEFGHI}|
|JKLMNOPQR|\mathfrak{JKLMNOPQR}|
|STUVWXYZ|\mathfrak{STUVWXYZ}|
|abcdefghijklm|\mathfrak{abcdefghijklm}|
|nopqrstuvwxyz|\mathfrak{nopqrstuvwxyz}|
|0123456789|\mathfrak{0123456789}|
|小型手写体 Small scriptstyle text||
|abcdefghijklm|{\scriptstyle\text{abcdefghijklm}}|

##### 2.8.2 字号 Size

|样式|LaTeX|
|:--|:--|
|a b c 巨 小 t i n y|{\tiny abc 巨小 tiny}|
|a b c 超 小 s c r i p t s i z e|{\scriptsize abc 超小 scriptsize}|
|a b c 小 s m a l l|{\small abc 小 small}|
|a b c 正 常 n o r m a l|{\normalsize abc 正常 normal}|
|a b c 大 l a r g e|{\large abc 大 large}|
|a b c 超 大 L a r g e|{\Large abc 超大 Large}|
|a b c 特 大 L A R G E|{\LARGE abc 特大 LARGE}|
|a b c 巨 大 h u g e|{\huge abc 巨大 huge}|
|a b c 巨 无 霸 H u g e|{\Huge abc 巨无霸 Huge}|

**注意：如您导出 SVG 格式**，理论上字体的整体大小并无用处，因为**SVG**为矢量图，所以大可不必担心图片不清晰的问题，即便是您选择下载**PNG 格式**的公式图片，图片整体尺寸也被默认设定为**4K**。所以此处的字号命令只为设置公式**相对大小**时使用，例如：

```
{\tiny x+y=z}x+y=z{\Huge x+y=z}
```

x + y = z x + y = z x + y = z

#### 2.9 方程式编号 Equation numbering

本页面可采用开启 AMS 宏包的方式获得方程自动编号，AMS 拓展包的具体开启方式请参考 2.11.4。

默认自动编号只在部分环境中起作用，如{equation}、{eqnarray}等，例如：

在 AMS 包开启状态下，会在公式后进行自动编号：

```
\begin{eqnarray}
E = mc^2 \\
e^{i\pi}+1=0 
\end{eqnarray}
```

$$ \begin{eqnarray} E = mc^2 \tag{1}\ e^{i\pi}+1=0 \tag{2} \end{eqnarray} $$ 如您在开启了 AMS 包状态下，全部公式均不希望出现编号，可使用{equation*}、或者{eqnarray*}环境，如：

```
\begin{eqnarray*}
E = mc^2 \\
e^{i\pi}+1=0 
\end{eqnarray*}
```

E = m c 2 e i π + 1 = 0

如您在开启了 AMS 包状态下，个别公式不希望出现编号，或者个别公式希望出现特有编号，可在公式后面使用 `\tag{}` 或者 `\notag` 命令，如：

```
\begin{eqnarray}
E = mc^2 \notag\\
e^{i\pi}+1=0 \tag{b}
\end{eqnarray}
```

E = m c 2 e i π + 1 = 0

#### 2.10 LaTeX 环境 LaTeX environments

环境通常是对代码段的整体描述，用于表达此段代码的角色，如，是矩阵？单行公式？多行公式？还是对齐公式等（本页面不支持文档环境），不同的环境起到的作用不同。以 `\begin{environments}` 开始，`\end{environments}` 结束。如最常用的矩阵命令，也是环境的一种，用法如下：

```
\begin{bmatrix}
1 & 0 \\
0 & 1
\end{bmatrix}
```

$$ \begin{bmatrix} 1 & 0 \ 0 & 1 \end{bmatrix} $$ 具体矩阵用法可参考章节 [2.4](#2.4 矩阵与多行列式 Matrices & Multilines)，下面给出几种其它常用环境的具体用法：

##### 2.10.1 equation 环境

\begin{equation}是单行公式环境，这意味着在此环境中只可以输入单行公式，同时 `\\` 等强制换行命令失效。如需对单行长公式进行强制换行，可使用 `\begin{split}` 环境进行嵌套，并用 `&` 字符表示对齐位置，如：

```
\begin{equation}
\begin{split}
 e ^ { x } = & 1 + \frac { x } { 1 ! } + \frac { x ^ { 2 } } { 2 ! } + \frac { x ^ { 3 } } { 3 ! } + \cdots \\
& - \infty < x < \infty  
\end{split}
\end{equation}
```

e x = 1 + x 1 ! + x 2 2 ! + x 3 3 ! + ⋯ − ∞ < x < ∞

##### 2.10.2 eqnarray 环境

\begin{eqnarray}是多行公式环境，环境内的所有公式默认右对齐，由 LaTeX 内核提供。

##### 2.10.3 align 环境

\begin{align}是多行公式环境，环境内的所有公式默认右对齐，由 amsmath 提供，排版较为灵活，如需表示多行公式推荐使用此环境。

```
\begin{align}
y = x \\
y = 3x^2 + 5x + 2 
\end{align}
```

$$ \begin{align} y = x \ y = 3x^2 + 5x + 2 \end{align} $$ 可使用 `&` 字符调整对齐位置。

```
\begin{align}
y & = x \\
y & = 3x^2 + 5x + 2 
\end{align}
```

y = x y = 3 x 2 + 5 x + 2

##### 2.10.4 array 环境

\begin{array}是数组环境，需手动输入对齐参数：

```
\begin{array}{|c|l|r|} 
a & b & S \\
\hline 
0 & 0 & 1 \\
0 & 1 & 1 \\
1 & 0 & 1 \\
1 & 1 & 0 \\
\end{array}
```

a b S 00 00 10 0 1 1 1 0 1 1 1 0

对齐参数使用 `c l r` 分别表示居中、居左和居右，如需竖线边框可直接在对齐参数区域输入 `|` 即可，如需横线边框可使用 `\hline` 命令。

更多环境使用可参考章节 [2.4](#2.4 矩阵与多行列式 Matrices & Multilines)。

#### 2.11 TeX 扩展包使用 TeX and LaTeX extensions

##### 2.11.1 physics 扩展包

physics 是一款便携出入物理符号、矩阵及方程的拓展包，使用前需要在设置中手动勾选。其具体用法可参考 [此文档](http://mirrors.ibiblio.org/CTAN/macros/latex/contrib/physics/physics.pdf)。

##### 2.11.2 mhchem 扩展包

mhchem 是一款便捷输入化学方程式的扩展包，使用前需要在设置中手动勾选。其具体用法如下：

###### 2.11.2.1 引用

基本命令为 `\ce{}`，可在 `{}` 中输入化学相关符号。

###### 2.11.2.2 化学式

在化学环境中，数字 `0123456789` 默认为下标，`+-` 默认为上标，如需强制上标可使用 `^` 符号，例如

```
\ce{H2O}  \ce{Sb2O3}  \ce{H+}  \ce{CrO4^2-}  \ce{[AgCl2]-}  \ce{Y^99+}  \ce{Y^{99+}}
```

[![ce1](https://camo.githubusercontent.com/207711578c49c2ea79da9e499c52fda24440f89707bc19fd5afa09aff65b828f/68747470733a2f2f6f7572736974652d7265736f757273652e6f73732d636e2d71696e6764616f2e616c6979756e63732e636f6d2f666f726d756c612d696d616765732f726561646d652f6365312e706e67)](https://camo.githubusercontent.com/207711578c49c2ea79da9e499c52fda24440f89707bc19fd5afa09aff65b828f/68747470733a2f2f6f7572736974652d7265736f757273652e6f73732d636e2d71696e6764616f2e616c6979756e63732e636f6d2f666f726d756c612d696d616765732f726561646d652f6365312e706e67)

###### 2.11.2.3 化学计量数

在化学环境中，计量数应与前面的大写字母使用**空格**分割，对于分数计量数，只需输入 `1/2` 即可显示 $\frac{1}{2}$ 的效果，如特殊情况需要显示 `1/2` 格式，请用 `( )` 扩起。

```
\ce{2H2O}  \ce{0.5 H2O}  \ce{1/2H2O}  \ce{(1/2)H2O}  \ce{$n$ H2O}
```

[![ce2](https://camo.githubusercontent.com/c92fdc1af0076e7f15ad54baad2ff88be0d735a3a56f982a9e7ea390412d5a33/68747470733a2f2f6f7572736974652d7265736f757273652e6f73732d636e2d71696e6764616f2e616c6979756e63732e636f6d2f666f726d756c612d696d616765732f726561646d652f6365322e706e67)](https://camo.githubusercontent.com/c92fdc1af0076e7f15ad54baad2ff88be0d735a3a56f982a9e7ea390412d5a33/68747470733a2f2f6f7572736974652d7265736f757273652e6f73732d636e2d71696e6764616f2e616c6979756e63732e636f6d2f666f726d756c612d696d616765732f726561646d652f6365322e706e67)

###### 2.11.2.4 同位素

```
\ce{^{227}_{90}Th+}  \ce{^227_90Th+}  \ce{^{0}_{-1}n^{-}}  \ce{^0_-1n-}
```

[![ce3](https://camo.githubusercontent.com/c9d4e43ab7200aeb55129721a1a90204afc59ba62ee1c8440252a53ac8cac10b/68747470733a2f2f6f7572736974652d7265736f757273652e6f73732d636e2d71696e6764616f2e616c6979756e63732e636f6d2f666f726d756c612d696d616765732f726561646d652f6365332e706e67)](https://camo.githubusercontent.com/c9d4e43ab7200aeb55129721a1a90204afc59ba62ee1c8440252a53ac8cac10b/68747470733a2f2f6f7572736974652d7265736f757273652e6f73732d636e2d71696e6764616f2e616c6979756e63732e636f6d2f666f726d756c612d696d616765732f726561646d652f6365332e706e67)

在一个复杂的化学式中，上标属于左侧元素还是右侧元素可能并不会明显的体现出来，但为了规范输入，建议使用 `{}` 分隔符作为区分：

```
\ce{H{}^3HO}  \ce{H^3HO}
```

[![ce4](https://camo.githubusercontent.com/8d080e14224aa2943fa164259d848e6f77cdc2859f6a4da834175e880b967044/68747470733a2f2f6f7572736974652d7265736f757273652e6f73732d636e2d71696e6764616f2e616c6979756e63732e636f6d2f666f726d756c612d696d616765732f726561646d652f6365342e706e67)](https://camo.githubusercontent.com/8d080e14224aa2943fa164259d848e6f77cdc2859f6a4da834175e880b967044/68747470733a2f2f6f7572736974652d7265736f757273652e6f73732d636e2d71696e6764616f2e616c6979756e63732e636f6d2f666f726d756c612d696d616765732f726561646d652f6365342e706e67)

###### 2.11.2.5 反应箭头

mhchem 提供了方便的反应箭头输入模式

```
\ce{A -> B}   \ce{A <- B}  \ce{A <-> B} 
```

[![ce5](https://camo.githubusercontent.com/f9565f1e0a8bee00a90a9b706de7a8abafeb746d653f3b4776a3083b1f036f61/68747470733a2f2f6f7572736974652d7265736f757273652e6f73732d636e2d71696e6764616f2e616c6979756e63732e636f6d2f666f726d756c612d696d616765732f726561646d652f6365352e706e67)](https://camo.githubusercontent.com/f9565f1e0a8bee00a90a9b706de7a8abafeb746d653f3b4776a3083b1f036f61/68747470733a2f2f6f7572736974652d7265736f757273652e6f73732d636e2d71696e6764616f2e616c6979756e63732e636f6d2f666f726d756c612d696d616765732f726561646d652f6365352e706e67)

```
\ce{A <--> B}  \ce{A <=> B}  \ce{A <=>> B}  \ce{A <<=> B}
```

[![ce6](https://camo.githubusercontent.com/a38f586805468640ecafdb8f5ca150956aed9d2d06ef5e37f7668da21baa012d/68747470733a2f2f6f7572736974652d7265736f757273652e6f73732d636e2d71696e6764616f2e616c6979756e63732e636f6d2f666f726d756c612d696d616765732f726561646d652f6365362e706e67)](https://camo.githubusercontent.com/a38f586805468640ecafdb8f5ca150956aed9d2d06ef5e37f7668da21baa012d/68747470733a2f2f6f7572736974652d7265736f757273652e6f73732d636e2d71696e6764616f2e616c6979756e63732e636f6d2f666f726d756c612d696d616765732f726561646d652f6365362e706e67)

箭头可以带有两个参数，即 `>[][]`，第一个 `[]` 表示上方参数，第二个 `[]` 表示下方参数

```
\ce{A ->[H2O] B}   \ce{A ->[{上方文字}]\[{下方文字}] B}
```

[![ce7](https://camo.githubusercontent.com/b096a1b97969644e5aa70cfdf747dc1073f1b2e0d15b2a5563bf099586279487/68747470733a2f2f6f7572736974652d7265736f757273652e6f73732d636e2d71696e6764616f2e616c6979756e63732e636f6d2f666f726d756c612d696d616765732f726561646d652f6365372e706e67)](https://camo.githubusercontent.com/b096a1b97969644e5aa70cfdf747dc1073f1b2e0d15b2a5563bf099586279487/68747470733a2f2f6f7572736974652d7265736f757273652e6f73732d636e2d71696e6764616f2e616c6979756e63732e636f6d2f666f726d756c612d696d616765732f726561646d652f6365372e706e67)

###### 2.11.2.6 气体和沉淀

在化学环境中可使用独立的 `^` 表示气体 $\uparrow$，使用独立的 `v`(小写字母 v) 表示沉淀 $\downarrow$

```
\ce{SO4^2- + Ba^2+ -> BaSO4 v}
```

[![ce8](https://camo.githubusercontent.com/83069b371254923bdfaded1619aa41aadb900844ddabe155dfd83698bb3fd23c/68747470733a2f2f6f7572736974652d7265736f757273652e6f73732d636e2d71696e6764616f2e616c6979756e63732e636f6d2f666f726d756c612d696d616765732f726561646d652f6365382e706e67)](https://camo.githubusercontent.com/83069b371254923bdfaded1619aa41aadb900844ddabe155dfd83698bb3fd23c/68747470733a2f2f6f7572736974652d7265736f757273652e6f73732d636e2d71696e6764616f2e616c6979756e63732e636f6d2f666f726d756c612d696d616765732f726561646d652f6365382e706e67)

```
\ce{A v B (v) -> B ^ B (^)}
```

[![ce9](https://camo.githubusercontent.com/c889d4c12e667912ee88ffad6ff93f6a45b5af6f0f10a70ba67ca16cac56631e/68747470733a2f2f6f7572736974652d7265736f757273652e6f73732d636e2d71696e6764616f2e616c6979756e63732e636f6d2f666f726d756c612d696d616765732f726561646d652f6365392e706e67)](https://camo.githubusercontent.com/c889d4c12e667912ee88ffad6ff93f6a45b5af6f0f10a70ba67ca16cac56631e/68747470733a2f2f6f7572736974652d7265736f757273652e6f73732d636e2d71696e6764616f2e616c6979756e63732e636f6d2f666f726d756c612d696d616765732f726561646d652f6365392e706e67)

###### 2.11.2.7 一些复杂的例子

```
\ce{Zn^2+  <=>[+ 2OH-]\[+ 2H+]  $\underset{\text{amphoteres Hydroxid}}{\ce{Zn(OH)2 v}}$  <=>[+ 2OH-]\[+ 2H+]  $\underset{\text{Hydroxozikat}}{\ce{[Zn(OH)4]^2-}}$}
```

[![ce10](https://camo.githubusercontent.com/a87e6234d8cfc15beb46744b442304080030fcfbf10edd6ec454291cd4af4f34/68747470733a2f2f6f7572736974652d7265736f757273652e6f73732d636e2d71696e6764616f2e616c6979756e63732e636f6d2f666f726d756c612d696d616765732f726561646d652f636531302e706e67)](https://camo.githubusercontent.com/a87e6234d8cfc15beb46744b442304080030fcfbf10edd6ec454291cd4af4f34/68747470733a2f2f6f7572736974652d7265736f757273652e6f73732d636e2d71696e6764616f2e616c6979756e63732e636f6d2f666f726d756c612d696d616765732f726561646d652f636531302e706e67)

```
\ce{$K = \frac{[\ce{Hg^2+}]\[\ce{Hg}]}{[\ce{Hg2^2+}]}$}
```

[![ce11](https://camo.githubusercontent.com/63594ecbcdf4736bb71a1bcc178a2a560ef2d2fbe885a598417f8cc1cb9a6407/68747470733a2f2f6f7572736974652d7265736f757273652e6f73732d636e2d71696e6764616f2e616c6979756e63732e636f6d2f666f726d756c612d696d616765732f726561646d652f636531312e706e67)](https://camo.githubusercontent.com/63594ecbcdf4736bb71a1bcc178a2a560ef2d2fbe885a598417f8cc1cb9a6407/68747470733a2f2f6f7572736974652d7265736f757273652e6f73732d636e2d71696e6764616f2e616c6979756e63732e636f6d2f666f726d756c612d696d616765732f726561646d652f636531312e706e67)

```
\ce{$K = \ce{\frac{[Hg^2+]\[Hg]}{[Hg2^2+]}}$}
```

[![ce12](https://camo.githubusercontent.com/cc4de6a81b83936ee794cd5991af7e7c0dd02a446a3ea6a4258ba52936f782a2/68747470733a2f2f6f7572736974652d7265736f757273652e6f73732d636e2d71696e6764616f2e616c6979756e63732e636f6d2f666f726d756c612d696d616765732f726561646d652f636531322e706e67)](https://camo.githubusercontent.com/cc4de6a81b83936ee794cd5991af7e7c0dd02a446a3ea6a4258ba52936f782a2/68747470733a2f2f6f7572736974652d7265736f757273652e6f73732d636e2d71696e6764616f2e616c6979756e63732e636f6d2f666f726d756c612d696d616765732f726561646d652f636531322e706e67)

```
\ce{Hg^2+ ->[I-]  $\underset{\mathrm{red}}{\ce{HgI2}}$  ->[I-]  $\underset{\mathrm{red}}{\ce{[Hg^{II}I4]^2-}}$}
```

[![ce13](https://camo.githubusercontent.com/442356df4c5e13332fc39db66246a8ea4e12ec7a3edbc8610a81172691eaed38/68747470733a2f2f6f7572736974652d7265736f757273652e6f73732d636e2d71696e6764616f2e616c6979756e63732e636f6d2f666f726d756c612d696d616765732f726561646d652f636531332e706e67)](https://camo.githubusercontent.com/442356df4c5e13332fc39db66246a8ea4e12ec7a3edbc8610a81172691eaed38/68747470733a2f2f6f7572736974652d7265736f757273652e6f73732d636e2d71696e6764616f2e616c6979756e63732e636f6d2f666f726d756c612d696d616765732f726561646d652f636531332e706e67)

##### 2.11.3 cancel 扩展包

cancel 扩展包为显示分数中**约分线**的 TeX 宏包，或显示其他划除效果，基本命令为 `\cancel{}`，例如：

```
\cfrac{x}{1 + \cfrac{\cancel{y}}{\cancel{y}}} = \cfrac{x}{2}
```

[![cancel1](https://camo.githubusercontent.com/22c3b7504d8f193e1aa831ef4f55d63c4dbb94775d003c425c5499b73dcafb06/68747470733a2f2f6f7572736974652d7265736f757273652e6f73732d636e2d71696e6764616f2e616c6979756e63732e636f6d2f666f726d756c612d696d616765732f726561646d652f63616e63656c312e706e67)](https://camo.githubusercontent.com/22c3b7504d8f193e1aa831ef4f55d63c4dbb94775d003c425c5499b73dcafb06/68747470733a2f2f6f7572736974652d7265736f757273652e6f73732d636e2d71696e6764616f2e616c6979756e63732e636f6d2f666f726d756c612d696d616765732f726561646d652f63616e63656c312e706e67)

```
\cancel{e^{i \pi} + 1 =0}
```

[![cancel2](https://camo.githubusercontent.com/5443e122128b9a959a88c5b82a634825e7cc406720ede0d5f0cef5c35e28813c/68747470733a2f2f6f7572736974652d7265736f757273652e6f73732d636e2d71696e6764616f2e616c6979756e63732e636f6d2f666f726d756c612d696d616765732f726561646d652f63616e63656c322e706e67)](https://camo.githubusercontent.com/5443e122128b9a959a88c5b82a634825e7cc406720ede0d5f0cef5c35e28813c/68747470733a2f2f6f7572736974652d7265736f757273652e6f73732d636e2d71696e6764616f2e616c6979756e63732e636f6d2f666f726d756c612d696d616765732f726561646d652f63616e63656c322e706e67)

##### 2.11.4 Ams 扩展包

本页面集成了大部分 ams 命令，即默认已打开。本拓展只为自动显示公式序号使用。

如，以下代码：

```
\begin{equation}
E = mc^2
\end{equation}
```

在 ams 包未开启状态下： $$ \begin{equation} E = mc^2 \end{equation} $$ 在 ams 包开启状态下： $$ \begin{equation} E = mc^2 \tag{1} \end{equation} $$ 具体自动编号用法请参考章节 [2.9](#2.9 方程式编号 Equation numbering)。

##### 2.11.5 AmsCd 扩展包

amsCd 扩展包是一款生成矩阵图的 TeX 宏包环境，基本环境命令为 `\begin{CD}` `\end{CD}`，基本用法如下：

`@<<<` 表示左箭头；

`@>>>` 表示右箭头；

`@AAA` 表示上箭头；

`@VVV` 表示下箭头；

`@=` 表示水平等号；

`@|` 表示数值等号；

`@.` 表示空箭头（占位）。

以 `@` 表示箭头开始，以 `<、>、A、V` 等表示箭头方向。如需在箭头上或下插入变量，直接在第一和第二，或第二和第三个箭头方向符号中插入即可，用法实例如下：

```
\begin{CD}
A @>a>> B\\
@VVbV @VVcV\\
C @>d>> D
\end{CD}
```

[![cd1](https://camo.githubusercontent.com/fc2c6e5850d86fa8e432a37971217235aeaf14f4bd839f647251f37a416e078d/68747470733a2f2f6f7572736974652d7265736f757273652e6f73732d636e2d71696e6764616f2e616c6979756e63732e636f6d2f666f726d756c612d696d616765732f726561646d652f6364312e706e67)](https://camo.githubusercontent.com/fc2c6e5850d86fa8e432a37971217235aeaf14f4bd839f647251f37a416e078d/68747470733a2f2f6f7572736974652d7265736f757273652e6f73732d636e2d71696e6764616f2e616c6979756e63732e636f6d2f666f726d756c612d696d616765732f726561646d652f6364312e706e67)

```
\begin{CD}
A @>a>b> B\\
@VlVrV @AlArA\\
C @<a<b< D
\end{CD}
```

[![cd2](https://camo.githubusercontent.com/226f6dca5396a43f74bde36e664c29d0b597d2c70e11ef004239d2f0b52b18c5/68747470733a2f2f6f7572736974652d7265736f757273652e6f73732d636e2d71696e6764616f2e616c6979756e63732e636f6d2f666f726d756c612d696d616765732f726561646d652f6364322e706e67)](https://camo.githubusercontent.com/226f6dca5396a43f74bde36e664c29d0b597d2c70e11ef004239d2f0b52b18c5/68747470733a2f2f6f7572736974652d7265736f757273652e6f73732d636e2d71696e6764616f2e616c6979756e63732e636f6d2f666f726d756c612d696d616765732f726561646d652f6364322e706e67)

##### 2.11.6 Unicode 扩展包

Unicode 扩展包一款显示 Unicode 字符的 TeX 宏包，基本命令为 `\unicode{}`，`{}` 中参数应输入指定字符的**十进制**或**十六进制**Unicode 代码，注意十六进制编码需在前面添加标识位 `x`，例如：

```
\unicode{8751} \unicode{x220f}
```

[![unicode1](https://camo.githubusercontent.com/f41c5f49999ffeb1722cbfc565b7736dd4051e405d341824041396e04c95299a/68747470733a2f2f6f7572736974652d7265736f757273652e6f73732d636e2d71696e6764616f2e616c6979756e63732e636f6d2f666f726d756c612d696d616765732f726561646d652f756e69636f6465312e706e67)](https://camo.githubusercontent.com/f41c5f49999ffeb1722cbfc565b7736dd4051e405d341824041396e04c95299a/68747470733a2f2f6f7572736974652d7265736f757273652e6f73732d636e2d71696e6764616f2e616c6979756e63732e636f6d2f666f726d756c612d696d616765732f726561646d652f756e69636f6465312e706e67)

##### 2.11.7 Bbox 扩展包

Bbox 扩展包一款用于设置公式背景颜色的 TeX 宏包，具体用法参见 [2.7.3](#2.7.3 用Bbox 扩展设置背景颜色 Setting background color with Bbox)

##### 2.11.8 NoErrors 扩展包

NoErrors 扩展包是一款阻止显示 TeX 错误消息的宏包，使用后将不会像是代码具体错误，而只会显示原始 TeX 代码。

##### 2.11.9 NewCommand 扩展包

Newcommand 扩展包提供了\def, \newcommand，\renewcommand，\let，\newenvironment 和 \renewenvironment 宏命令，用于在 TeX 中创建新的宏和环境。例如：

```
\def\RR{{\bf R}}  %将{\bf R}（加粗的R）定义为\RR
\RR               %调用\RR命令
```

[![new1](https://camo.githubusercontent.com/ae10c913531219885cef6475cfcf693111996628a10ec5d4bc61b3b2bb2487a7/68747470733a2f2f6f7572736974652d7265736f757273652e6f73732d636e2d71696e6764616f2e616c6979756e63732e636f6d2f666f726d756c612d696d616765732f726561646d652f6e6577312e706e67)](https://camo.githubusercontent.com/ae10c913531219885cef6475cfcf693111996628a10ec5d4bc61b3b2bb2487a7/68747470733a2f2f6f7572736974652d7265736f757273652e6f73732d636e2d71696e6764616f2e616c6979756e63732e636f6d2f666f726d756c612d696d616765732f726561646d652f6e6577312e706e67)

### 3 关于 About

如有任何问题可以点击页面下方的邮箱图标向我们反馈，感谢您的使用！

### 4 参考文献 Reference

[1. LaTeX公式编辑器](http://47.104.179.138/) [2. MathJax Documentation](https://docs.mathjax.org/en/latest/index.html) [3. Displaying a formula](https://en.wikipedia.org/wiki/Help:Displaying_a_formula) [4. mathjax/MathJax: Beautiful math in all browsers - GitHub](https://github.com/mathjax/MathJax) [5. mhchem for MathJax](https://mhchem.github.io/MathJax-mhchem/)

## More Refereneces

![[latex_1650278700583_0.pdf]] via: https://www.icl.utk.edu/~mgates3/docs/latex.pdf

- [LATEX：玩转数学公式 - 简书](https://www.jianshu.com/p/97ec8a3739f6)
- [Latex数学符号对应表 - 叮叮当当sunny - 博客园](https://www.cnblogs.com/dingdangsunny/p/12312966.html)
- [Online LaTeX Equation Editor - create, integrate, download](https://latex.codecogs.com)
