---
title: serif-sans-serif-monospace-cursive和fantasy
created: 2025-01-31T13:09:04
modified: 2025-01-31T13:09:04
description: PPT为什么不要用宋体？与CSS有什么关系？
source: https://www.ayqy.net/blog/serif%EF%BC%8Csans-serif%EF%BC%8Cmonospace%EF%BC%8Ccursive%E5%92%8Cfantasy/
tags: 
tags-link: 
type: archive-web
---
## 一.示例

[![generic-font-families](http://cdn.ayqy.net/data/home/qxu1001840309/htdocs/cms/wordpress/wp-content/uploads/2017/09/generic-font-families.png)](http://cdn.ayqy.net/data/home/qxu1001840309/htdocs/cms/wordpress/wp-content/uploads/2017/09/generic-font-families.png)

generic-font-families

P.S.更多英文字体示例见参考资料-[五种一般字体族英文示例](https://www.w3.org/Style/Examples/007/fonts.en.html)

P.S.更多中文字体示例见参考资料-[The Complete Beginner’s Guide to Chinese Fonts](https://webdesign.tutsplus.com/articles/the-complete-beginners-guide-to-chinese-fonts--cms-23444)

## 二.作用

> Generic font families are a fallback mechanism, a means of preserving some of the style sheet author’s intent in the worst case when none of the specified fonts can be selected.

（摘自[15.3.1 Generic font families](https://www.w3.org/TR/CSS2/fonts.html#generic-font-families)）

由于不是所有字体在所有终端设备上都可用（有几千种字体，而且大部分都不是免费的），CSS提供了一种*fallback机制*：先列出想要的字体，再列出作为替补的字体，最后以一般字体族结尾

在最坏的情况下（指定的所有字体都不可用时），能通过这种方式保留一些样式表编写者的意图

一般字体族共有5个：serif，sans-serif，monospace，cursive和fantasy，相对常用的是前3个（衬线，无衬线和等宽字体族）

## 三.特点

### serif 衬线字体族

特点：

- 具有修饰过的笔画，向外展开的或者尖细的末端，或者是带有实际衬线的末端
- 一笔一划末端（两头）都带点变化装饰，比如宋体笔画末端有毛笔字的感觉
- 文字末端有差异，在小字号下仍然容易辨认。但在大字号下笔画装饰部分可能会显得*模糊或带有锯齿*

示例：

- Times New Roman、MS Georgia
- 宋体、仿宋

衍生：

- petit-serif 小衬线字体族

末端变化不明显，可以当做无衬线
- slab-serif 雕版衬线字体族

末端变化非常明显

### sans-serif 无衬线字体族

sans-前缀是法语，发音为/san/，意为“无”

特点：

- 具有笔画清晰的末端–带有一点或者没有向外展开的，交错笔画，或者其它装饰
- 与“衬线字体”相比，如果字号比较小，看起来就会有些*难以分辨*，尤其段落阅读时容易串行

示例：

- MS Trebuchet、MS Arial、MS Verdana
- 黑体、幼圆、隶书、楷体

### cursive 手写字体族

特点：

- 像手写的一样

示例：

- Caflisch Script、Adobe Poetica
- 徐静蕾手写体、迷你简黄草、华文行草、少女体

### fantasy 梦幻字体族

特点：

- 艺术字，主要用于图片，页面上用的少

示例：

- WingDings、WingDings 2、WingDings 3、Symbol
- 萝卜体

### monospace 等宽字体族

特点：

- 每个字形都等宽，主要用于英文，中文方块字本来就等宽

示例：

- Courier、MS Courier New、Prestige
- 大多数中文字体

## 四.使用原则

常识：

- 一个页面上不要用3，4种甚至更多字体
- 如非必要，不要在句中改变字体
- sans-serif用于在线媒体，*serif用于打印设备*
- monospace用于打字机和代码
- *小字号场景不要用sans-serif*，衬线字体更容易辨认

最佳实践：

- sans-serif是页面首选，无衬线

因为在屏幕显示设备上，衬线会让文字变得难以辨认
- serif不适合在线阅读，但打印效果很好，适用于页面打印版

衬线字体在打印的场景更容易阅读，让人更容易清楚区分不同字母。打印机对分辨率的要求更精细（355ppi），高分辨率下细节显示得很清楚，而不会像屏幕显示一样出现模糊
- monospace用作代码示例

每个字符等宽，在页面上占据相同的空间，打字机就用这种字体
- 正文不要用fantasy和cursive

可以用在图片或者标题栏里

### 写在最后

*PPT不要用宋体*，不是瞎说的

### 参考资料

- [15.3.1 一般字体族](http://www.ayqy.net/doc/css2-1/fonts.html#generic-font-families)
- [CSS 中规定的五种一般字体家族（serif、sans-serif 等）](http://www.cftea.com/c/2009/02/1Y60JODHCZKWEC9I.asp)
- [CSS: fonts](https://www.w3.org/Style/Examples/007/fonts.en.html)：五种一般字体族英文示例
- [The Complete Beginner’s Guide to Chinese Fonts](https://webdesign.tutsplus.com/articles/the-complete-beginners-guide-to-chinese-fonts--cms-23444)：中文字体示例
- [MDN | font-family](https://developer.mozilla.org/en-US/docs/Web/CSS/font-family)
- [Five Font Families](https://openlab.citytech.cuny.edu/clarkeadv1227/type-history/five-font-families/)：英文字体字母A的演变
- [一起来发现Mac的内置字体库\[英文字体－完结\]～](https://www.douban.com/group/topic/55210544/)
- [Font Families – Serif, Sans-Serif, Monospace, Script, Fantasy](http://www.impressionwebstudio.com/en/news_articles/font_families.html) [Screen and Print Resolution](https://www.modernpostcard.com/knowledge/preparing-materials/resolution)