---
title: gandf/slick-rss
aliases:
  - slick-rss
created: 2025-03-29T23:43:05
modified: 2025-03-29T23:43:05
description: The news reader extension for Chromium
source: https://github.com/gandf/slick-rss
tags:
  - github/star
tags-link:
  - "[[pages/rss|rss]]"
type: repo
---
## Repo Meta

![](https://img.shields.io/github/stars/gandf/slick-rss?style=for-the-badge&label=stars) ![](https://img.shields.io/github/repo-size/gandf/slick-rss?style=for-the-badge&label=size) ![](https://img.shields.io/github/created-at/gandf/slick-rss?style=for-the-badge&label=since)

[![](https://github-readme-stats.vercel.app/api/pin/?username=gandf&repo=slick-rss&bg_color=00000000)](https://github.com/gandf/slick-rss)

## Notes


- [x] #gtd/todo with some userscripts due to some issues
- When address is begin with `//xxx.com`, the final address will be `chrome-extension://xxx.com`, while it should be `http`. I try some ways but I am novice in javascript.
- `//` only supported with server and extension actually run at local. `//` img cannot loaded and the http url is wrong as well.

```
foo://example.com:8042/over/there?name=ferret#nose
\_/   \______________/\_________/ \_________/ \__/
|           |            |            |        |
scheme     authority       path        query   fragment
```

via: [Is it valid to replace \<script src="http://...">?](https://stackoverflow.com/questions/550038/is-it-valid-to-replace-http-with-in-a-script-src-http)

- [ ] #gtd/todo I cannot replace target when all data has loaded. So I try to add a button to replace the RSS content, with [Content Security Policy - Chrome Developers](https://developer.chrome.com/docs/apps/contentSecurityPolicy/#relaxing-inline-script).
([cordova - The Content Security Policy 'default-src * data:;' was delivered via a  element outside the document's  - Stack Overflow](https://stackoverflow.com/questions/39657544/the-content-security-policy-default-src-data-was-delivered-via-a-meta-el))
- Cannot run inline javescript
- [How does inline JavaScript work with HTML ? - GeeksforGeeks](https://www.geeksforgeeks.org/how-does-inline-javascript-work-with-html/)
- Solution

```html
<button id="myButton">Click me</button>
<script src="script.js"></script>
```

```js
document.getElementById("myButton").addEventListener("click", myFunction);
function myFunction(){
console.log('asd');
}
```

- > In chrome apps, Content Security Policy does not allow inline javascript. So you have to put your javascript in a .js file and include it in your HTML.
Further reading: [https://developer.chrome.com/extensions/contentSecurityPolicy](https://developer.chrome.com/extensions/contentSecurityPolicy)
via: [javascript - Refused to execute inline event handler because it violates CSP. (SANDBOX) - Stack Overflow](https://stackoverflow.com/questions/36324333/refused-to-execute-inline-event-handler-because-it-violates-csp-sandbox)

- Extra
- [What are Bookmarklets? How to Use JavaScript to Make a Bookmarklet in Chromium and Firefox](https://www.freecodecamp.org/news/what-are-bookmarklets/)
- [ ] #gtd/todo [异步 JavaScript 简介 - 学习 Web 开发 | MDN](https://developer.mozilla.org/zh-CN/docs/Learn/JavaScript/Asynchronous/Introducing)
- JavaScript regex group replace?
[regex - Javascript replace with reference to matched group? - Stack Overflow](https://stackoverflow.com/questions/1234712/javascript-replace-with-reference-to-matched-group)

```js
/**
<div class="feedPreviewSummaryContent" style="max-height: 480px;">[img]https://img.imoutomoe.net/images/2022/12/06/35c17455f54a12950.jpg[/img]
[img]https://img.imoutomoe.net/images/2022/12/06/4c015ed6fd28b52d2.jpg[/img]
[img]https://img.imoutomoe.net/images/2022/12/06/52168fd40a039b8b4.jpg[/img]
[img]https://cdn.cloudflare.steamstatic.com/steam/apps/1924680/heade ..</div>
**/
```
