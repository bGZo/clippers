---
title: "Web-Fonts"
created: 2025-01-16T08:57:49
modified: 2025-01-16T09:29:07
source: "http://web.simmons.edu/~grabiner/comm244/weekfour/fonts.html"
tags:
  - "todo"
tags-link:
type: "archive-web"
---

[Back to Class Four page »](http://web.simmons.edu/~grabiner/comm244/class4.html)

In the labs we have over **2,500** fonts to choose from.

On the web, we have these:

Screen shot from: [http://dustinbrewer.com/fonts-on-the-web-and-a-list-of-web-safe-fonts/](http://dustinbrewer.com/fonts-on-the-web-and-a-list-of-web-safe-fonts/ "Fonts on the web and a list of web safe fonts | Dustin Brewer Web Design")

---

## Why So Few?

- ==Most people don't ever install fonts==
- ==Many people don't even know what a typeface is==

Most people rely on fonts that come with their operating system or software. There are three major categories of operating systems (listed in order of popularity):

- Windows
- OS X
- Linux (many varieties, but very low market share)

We can rely on the fonts from these operating systems being available.

Other common fonts are also installed with Microsoft Office. We can usually rely on these fonts as well.

---

## What happens if we ask for a font that the user doesn't have?

The font doesn't display.

A different font is used instead (usually chosen by the browser).

As graphic designers, we **always** want to have control of the font being rendered.

---

## Introducing Font Stacks

When specifying fonts for web pages, ==we use a system of "fallbacks", called a== **==font stack==**==.==

==The font stack allows us to:==

1. ==choose the font we want most==
2. ==choose the font we want if the first one isn't available==
3. ==choose any number of other fonts that we might want to fallback on==
4. ==choose a== **==last resort==** ==font==

This allows us to be sure that we have some control over what font is displayed in our website. Even if the user doesn't have our first choice font, they have some font that **we chose**.

---

### CSS Font-Family Property

The `font-family` property allows us to specify several fonts we might like to use.

`    ``` body { font-family: Helvetica, “Helvetica Neue”, Arial, sans-serif; } ```  `

The font stack breaks down like this:

- **1st Choice:** The first choice is Helvetica which is on all Macs, but not many Windows computers
- **2nd Choice:** The second choice is Helvetica Neue, which may be installed on Windows machines
- **3rd Choice:** Arial is the third choice and is installed on most machines
- **4th Choice:** If none of the previous fonts are available, a default sans serif font is used.

**Note: If a font is more than one word, you must surround it with quotation marks.**

---

### CSS Generic Font Families

==Generic Font Families are defined in the CSS Specification as a last resort method.== Here is the explanation from the [CSS Specification](http://www.w3.org/TR/CSS2/fonts.html#generic-font-families "Fonts") (Note: "user agent" means browser):

> ==Generic font families are a fallback mechanism, a means of preserving some of the style sheet author's intent in the worst case when none of the specified fonts can be selected. For optimum typographic control, particular named fonts should be used in style sheets.==
>
> ==All five generic font families are defined to exist in all CSS implementations (they need not necessarily map to five distinct actual fonts). User agents should provide reasonable default choices for the generic font families, which express the characteristics of each family as well as possible within the limits allowed by the underlying technology.==

Here are the descriptions of the five generic font families:

==serif==

==A serif font==

==sans-serif==

==A sans-serif font==

==cursive==

==A script or handwritten font==

==fantasy==

==A decorative font that doesn't fit in to the other categories.== *==Be careful using this one because the results are unpredictable==*

==monospace==

==A font that has equal spacing for all characters. This is mostly used for code examples.==

---

### Strategy for Choosing Font Stacks

When selecting your font stacks, you should choose several fonts that are the same type of font.

They should be listed in order of your preference and also by prevalence.

Your second-to-last font choice should be installed on most systems (see the [chart at the top of the page](#web-safe-list)).

The last choice is mostly just there to make sure the right classification of font shows up if all else fails. We hope to never get to this point, but just in case.

---

## Additional Reading

Here are some articles with more information on appropriately choosing your font stacks.

- [Fonts on the web and a list of web safe fonts](http://dustinbrewer.com/fonts-on-the-web-and-a-list-of-web-safe-fonts/ "Fonts on the web and a list of web safe fonts | Dustin Brewer Web Design")
- [Better CSS Font Stacks](http://unitinteractive.com/blog/2008/06/26/better-css-font-stacks/ "Better CSS Font Stacks | Unit Verse")
- [Increase Your Font Stacks With Font Matrix](http://24ways.org/2007/increase-your-font-stacks-with-font-matrix "24 ways: Increase Your Font Stacks With Font Matrix")
- [Best Fonts for the Web](http://www.kathymarks.com/archives/2006/11/best_fonts_for_the_web_1.html "Best Fonts for the Web | KathyMarks.com")

[Back to Class Four page »](http://web.simmons.edu/~grabiner/comm244/class4.html)
