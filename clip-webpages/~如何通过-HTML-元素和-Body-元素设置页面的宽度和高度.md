---
title: "如何通过 HTML 元素和 Body 元素设置页面的宽度和高度"
aliases: "如何通过 HTML 元素和 Body 元素设置页面的宽度和高度"
created: 2025-04-05T17:20:30
modified: 2025-04-05T17:20:30
description: "CSS 很困难，但也很宽容。这种宽容体现在我们可以随意地将样式扔到 CSS 中，而页面仍在加载，不会“崩溃”。 对于页面的宽度和高度，你知道在 HTML元素上设置什么吗？body 元素呢？ 你是否只是将样式应用于两个元素，然后就希望呈现最好的效果？ 如果你是这样做的，那么你并不孤单。 这些问题的答案并不直观。 过去我将样式应用到两个元素，而没有考虑确切地将哪个属性应用到哪个元素。🤦‍♂️ 像这样同时应用于 HTML 和 body 元素的 CSS 属性并不少见： html, body {      min-height: 100%; } 重要吗？ 是的，重要。 上面的样式定义产生了一个问题： 将两个元素的 min-height 设置为 100%，body 元素将不能像你期望的那样填充页面。如果你在开发工具中检查计算出的样式值，则 body 元素的高度为零。 同时，HTML 元素的高度等于浏览器中页面的可见部分。 从 Chrome Dev Tools 中查看以下屏幕截图： body 元素有一个默认的 8px 边距，高度值为"
source: "https://www.freecodecamp.org/chinese/news/html-page-width-height/"
tags:
tags-link:
type: "archive-web"
---
![如何通过 HTML 元素和 Body 元素设置页面的宽度和高度](https://chinese.freecodecamp.org/news/content/images/size/w2000/2021/06/william-warby-WahfNoqbYnM-unsplash--1-.jpeg)

CSS 很困难，但也很宽容。这种宽容体现在我们可以随意地将样式扔到 CSS 中，而页面仍在加载，不会“崩溃”。

对于页面的宽度和高度，你知道在 HTML元素上设置什么吗？body 元素呢？

你是否只是将样式应用于两个元素，然后就希望呈现最好的效果？

如果你是这样做的，那么你并不孤单。

这些问题的答案并不直观。

过去我将样式应用到两个元素，而没有考虑确切地将哪个属性应用到哪个元素。🤦‍♂️

像这样同时应用于 HTML 和 body 元素的 CSS 属性并不少见：

```
html, body {
     min-height: 100%;
}
```

## **重要吗？**

是的，重要。

上面的样式定义产生了一个问题：

将两个元素的 min-height 设置为 100%，body 元素将不能像你期望的那样填充页面。如果你在开发工具中检查计算出的样式值，则 body 元素的高度为零。

同时，HTML 元素的高度等于浏览器中页面的可见部分。

从 Chrome Dev Tools 中查看以下屏幕截图：

![empty_body](https://www.freecodecamp.org/news/content/images/2021/02/empty_body.png)

body 元素有一个默认的 8px 边距，高度值为 0

## 为什么会这样？

使用百分比作为大小值，需要元素参照一个父元素来作为该百分比的基础。

HTML 元素参照高度值等于可见视口高度的视口。然而，我们只在 HTML 元素上设置了一个 min-height ......而不是一个 height 属性值。

因此，在决定 100% 等于什么时，body 元素没有可参照的父元素高度值。

## 问题可能是隐藏的

如果你一开始使用足够的内容来填充页面的正文，你可能没有注意到这个问题。

并且更难以注意到的是，如果你在两个元素上或甚至仅在其中一个元素上设置背景颜色，则视口将充满该颜色。这给人的印象是 body 元素与视口一样高。

但是它仍然为零。

上图取自具有以下 CSS 的页面：

```
html, body {
    min-height: 100%;
}
body { background-color: dodgerblue; }
```

### 反向继承？

奇怪的是，如果你没有在 HTML 元素上设置单独的背景色，则 HTML 元素采用 body 元素的背景色。

## 那么什么是全响应页面的理想高度设置？

多年以来，答案如下：

```
html {
    height: 100%;
}
body {
    min-height: 100%;
}
```

这允许 HTML 元素引用父视口，并使其高度值等于视口值的 100%。

随着 HTML 元素接收高度值，分配给 body 元素的 min-height 值为其提供了一个与 HTML 元素匹配的初始高度。

如果内容超出可见页面，这也允许 body 显示得更高。

唯一的缺点是 HTML 元素不会超出可见视口的高度。然而，允许 body 元素超过 HTML 元素被认为是可以接受的。

## 如今的解决方案被简化了

```
body { min-height: 100vh; }
```

此示例使用 `vh`（视口高度）单位来允许主体根据视口的整个高度设置最小高度值。

与前面讨论的背景颜色一样，如果我们不为 HTML 元素设置高度值，那么将假定 HTML 的高度值与 body 元素的高度值相同。

因此，此解决方案避免了先前解决方案中存在的 HTML 元素溢出，并且这两个元素的高度都可以随着内容而变化！

过去使用 `vh` 单位确实会在一些移动浏览器出现问题，但现在 [Chrome 和 Safari 似乎与视口单位保持一致](https://developers.google.com/web/updates/2016/12/url-bar-resizing)。

## 页面高度可能激活水平滚动条

等等，什么？这不应该说“页面宽度”吗？

不是的。

在另一个奇怪的系列事件中，你的页面高度可能会激活浏览器中的水平滚动条。

当你的页面内容增长到高于视口高度时，右侧的垂直滚动条将被激活。

## 那么如何处理呢？

当任何元素——不仅仅是 HTML 或 body 元素——被设置为 100vw（视口宽度）单位时，就会出现这个问题。

视口单位不考虑垂直滚动条占用的大约 10 个像素。

因此，当垂直滚动条被激活时，还会产生一个水平滚动条。

## 如何将页面设置为全宽

也许不应该这么做。

不在 HTML 和 body 元素上设置宽度，将默认为屏幕的全尺寸。如果你确实设置了 auto 以外的宽度值，请考虑首先使用 CSS 样式重置。

请记住，默认情况下 body 元素的所有边都有 8px 的边距。

CSS 样式重置删除了这一点。否则，在移除边距之前将宽度设置为 100% 会导致 body 元素溢出。这是我使用的 CSS 重置：

```
* { 
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
```

## 如何根据你的喜好设置宽度

虽然可能并不总是需要设置宽度，但我通常会这样做。

这可能只是一种习惯。

如果你将 body 元素的宽度设置为 100%，将出现全屏宽度。这本质上等同于不设置宽度值并使用默认值。

如果要将 body 元素用作较小的容器，并让 HTML 元素填充页面，则可以在 body 上设置 max-width 值。

下面是一个例子：

```
html { background-color: #000; } 
body {
    min-height: 100vh;
    max-width: 400px;
    background-color: papayawhip; 
    margin: 0 auto;
}
```

## 总结

由于没有为 HTML 元素设置高度值，将 body 元素的高度和/或最小高度设置为 100%，会导致没有高度（在添加内容之前）。

但是，由于没有为 HTML 元素设置宽度值，将 body 元素的宽度设置为 100%，会导致全屏宽度。

这可能违反直觉且令人困惑。

对于响应式全屏高度，请将 body 元素 min-height 设置为 100vh。

设置页面宽度时，请在 100vw 上选择 100% 以避免意外的水平滚动条。

下面这个视频教程来自我的 YouTube 频道，演示 HTML 页面的 CSS 高度和宽度设置，该页面是全屏大小，并随着其包含的内容而变化：

![](https://www.youtube.com/watch?v=dpuKVjX6BJ8)

你是否有不同的方式来设置 CSS 宽度和高度？请告诉我你的方法！

原文：[HTML vs Body: How to Set Width and Height for Full Page Size](https://www.freecodecamp.org/news/html-page-width-height/)，作者：[Dave Gray](https://www.freecodecamp.org/news/author/dave/)

---

---

在 freeCodeCamp 免费学习编程。 freeCodeCamp 的开源课程已帮助 40,000 多人获得开发者工作。[开始学习](https://www.freecodecamp.org/chinese/learn/)