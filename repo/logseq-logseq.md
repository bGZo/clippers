---
title: logseq
aliases:
  - logseq
created: 2021-08-01T12:00:00
modified: 2025-06-07T15:53:20
description: http://trello.com/b/8txSM12G/roadmap
source: https://github.com/logseq/logseq
tags:
  - star
  - deprecated
tags-link: 
type: repo
changelog: https://docs.logseq.com
document: https://blog.logseq.com, https://hub.logseq.com
roadmap: https://trello.com/b/8txSM12G/roadmap
---

## Repo Meta

![](https://img.shields.io/github/stars/logseq/logseq?style=for-the-badge&label=stars) ![](https://img.shields.io/github/repo-size/logseq/logseq?style=for-the-badge&label=size) ![](https://img.shields.io/github/created-at/logseq/logseq?style=for-the-badge&label=since)

[![](https://github-readme-stats.vercel.app/api/pin/?username=logseq&repo=logseq&bg_color=00000000)](https://github.com/logseq/logseq)

## Why

Basically, it's better that encoding with txt and search in [[microsoft-vscode]]. I used it in the past but I was dropped in the category hell. When I finish a note last two months, and I have no idea where are they stored. The category I organized is terrible. And the LS gives us a vision we could organize. I like it.

- Journals in each day
- Using bi-directional links and graph to connect.
    - Although it's really slow.

I've learned a lot of things, not only how to note, how to remember, but also a few philosophy of organizing the whole [[knowledge]] system.

Anyway, considered [[open-source]], [[privacy]], [[censor]], high [[price]] subscriptions and bullshit user agreement. I choose this one. [^used_note_application]

## How
### How to rebuild when LS stuck?
#### windows

```shell
rm "$env:appdata\LS" -r
```

### How to replace TAB with two spaces

```edu
:export/bullet-indentation :two-spaces
```

Using sponge from https://joeyh.name/code/moreutils/

```shell
# via: https://discuss.logseq.com/t/specify-indentation-type-changing-the-default-font/2703/6
sudo apt install moreutils # sponge
find . -name '*.md' ! -type d -exec bash -c 'expand -t 2 "$0" | sponge "$0"' {} \;
```

### How publishing with GA?

```yml
on: [push]

permissions:
  contents: write
jobs:
  test:
    runs-on: ubuntu-latest
    name: Publish Logseq graph
    steps:
      - uses: actions/checkout@v3
        with:
          submodules: false

      - uses: logseq/publish-spa@main
        with:
          output-directory: www
          accent-color: grass

      # to make sure asset paths are correctly identified
      - name: Add a nojekyll file
        run: touch www/.nojekyll

      # Inject custom scripts
      - name: Inject Script 💬
        run: sed -i "s@</body>@$( cat logseq/inject.html | tr '\n' ' ' | sed 's@&@\\&@g' )</body>@"  www/index.html

      - name: Deploy 🚀
        uses: JamesIves/github-pages-deploy-action@v4
        with:
          folder: www
```

```html
<!-- 评论系统放置在主内容区域 -->
<script>
    var container = document.getElementById('main-content-container');
    container.style['flex-wrap'] = 'wrap';
    container.firstChild.style['flex-basis'] = '100%';
    var element = document.createElement('div');
    element.classList.add('giscus');
	container.appendChild(element);
</script>
<!-- 评论系统 -->
<script src="https://giscus.app/client.js"
        data-repo="bGZo/soul"
        data-repo-id="R_kgDOKbDA0w"
        data-category="Giscus"
        data-category-id="DIC_kwDOKbDA084Cfouf"
        data-mapping="title"
        data-strict="0"
        data-reactions-enabled="1"
        data-emit-metadata="0"
        data-input-position="bottom"
        data-theme="preferred_color_scheme"
        data-lang="zh-CN"
        data-loading="lazy"
        crossorigin="anonymous"
        async>
</script>
<!-- SPA 评论系统刷新问题 -->
<script>
    history.pushState = (f => function pushState() {
        var ret = f.apply(this, arguments);
        window.dispatchEvent(new Event('pushstate'));
        window.dispatchEvent(new Event('locationchange'));
        return ret;
    })(history.pushState);
    history.replaceState = (f => function replaceState() {
        var ret = f.apply(this, arguments);
        window.dispatchEvent(new Event('replacestate'));
        window.dispatchEvent(new Event('locationchange'));
        return ret;
    })(history.replaceState);
    window.addEventListener('popstate', () => {
        window.dispatchEvent(new Event('locationchange'))
    });
    window.addEventListener('locationchange', function() {
        const iframe = document.querySelector('iframe.giscus-frame');
        const title = decodeURIComponent(location.hash.split('/').slice(-1)[0]);
        console.debug("location change to:", title, iframe);
        if (!iframe || !title) return;
        iframe.contentWindow.postMessage({
            giscus: {
                setConfig: {
                    term: title
                }
            }
        }, 'https://giscus.app');
        console.debug("try refresh giscus:", title);
    }, false);
</script>
<!-- 评论系统主题随logseq变化 -->
<script>
    localStorage.setItem = (f => function setItem() {
        var ret = f.apply(this, arguments);
        if (arguments.length > 1 && arguments[0] == 'theme') {
            window.dispatchEvent(new Event('themechange'));
        }
        return ret;
    })(localStorage.setItem);

    window.addEventListener('themechange', () => {
        const logseqTheme = JSON.parse(window.localStorage.getItem('theme'));
        const lsq2gisThemeMap = {
            'dark': 'dark_dimmed',
            'white': 'light'
        };
        const giscusTheme = lsq2gisThemeMap[logseqTheme];
        const iframe = document.querySelector('iframe.giscus-frame');
        if (iframe && giscusTheme) {
            iframe.contentWindow.postMessage({
                giscus: {
                    setConfig: {
                        theme: giscusTheme
                    }
                }
            }, 'https://giscus.app');
            console.debug("try switch giscus theme:", giscusTheme);
        }
    });
</script>
```

Demo repo via: https://github.com/bGZo/notes/tree/logseq

Refer to https://logseq.abosen.top/#/page/logseq%20%E6%8E%A5%E5%85%A5%E8%AF%84%E8%AE%BA%E7%B3%BB%E7%BB%9F

## Changelog

Start begin Beta 0.6.5; [Changelog](https://docs.logseq.com/#/page/changelog); [docs/Changelog.md](https://github.com/logseq/docs/blob/master/pages/Changelog.md?plain=1)

- Apr 26st, 2023 Beta 0.9.4
    - Add `:remove-block-children?` query option for advanced queries [#9229](https://github.com/logseq/logseq/pull/9229)
- Apr 19st, 2023 Beta 0.9.3
    - Advanced queries have a new :group-by-page? option [#9133](https://github.com/logseq/logseq/pull/9133)
- Apr 13st, 2023 Beta 0.9.2
    - Support exporting to image [#9037](https://github.com/logseq/logseq/pull/9037)
    - Make publishing accessible to CLIs [#9033](https://github.com/logseq/logseq/pull/9033)
- Mar 29st, 2023 Beta 0.9.1
- Mar 28st, 2023 Beta 0.9.0
    - Refactored file system handling to fix filename issues on mobile platforms, requiring re-indexing of your working graph [#8792](https://github.com/logseq/logseq/pull/8792)
    - Added a simple [Query Builder](https://docs.logseq.com/#/page/Query%20Builder) [#8774](https://github.com/logseq/logseq/pull/8774)
    - Made [Whiteboards](https://docs.logseq.com/#/page/whiteboard) publicly available to all users [#8853](https://github.com/logseq/logseq/pull/8853)
    - Whiteboards
        - Paste and dnd behavior (also add a placeholder to shape labels) [#8753](https://github.com/logseq/logseq/pull/8753)
        - Publishing [#8899](https://github.com/logseq/logseq/pull/8899)
        - Refine UX [#8797](https://github.com/logseq/logseq/pull/8797)
    - Several copy-as/export enhancements [#8814](https://github.com/logseq/logseq/pull/8814)
    - Add better error messages for duplicate key in `config.edn` [#8488](https://github.com/logseq/logseq/pull/8488)
    - Add config option to handle default block refs expanding behavior [#8839](https://github.com/logseq/logseq/pull/8839). A new setting item `:ui/auto-expand-block-refs?` is added.
- Mar 1st, 2023 Beta 0.8.18
    - Support cues for Cloze cards [#8654](https://github.com/logseq/logseq/pull/8654) [Documentation](https://docs.logseq.com/#/page/cloze)
    - Add support for [block refs](https://docs.logseq.com/#/page/block%20reference) in properties to backlink to blocks [#8695](https://github.com/logseq/logseq/pull/8695)
    - Add command for copying a page url [#8538](https://github.com/logseq/logseq/pull/8538)
    - Shortcuts can be disabled with `false` now [#8618](https://github.com/logseq/logseq/pull/8618)
    - PDF viewer enhancements [#8616](https://github.com/logseq/logseq/pull/8616)
    - [Local HTTP Server](https://docs.logseq.com/#/page/local%20http%20server) now supports CORS for use from another web page or browser extension [#8651](https://github.com/logseq/logseq/pull/8651)
- Feb 10th, 2023 Beta 0.8.17
    - Adds support for `:query-page` as an input [#8449](https://github.com/logseq/logseq/pull/8449) - [Documentation](https://docs.logseq.com/#/page/advanced%20queries/block/query%20inputs)
    - Support dragging the PDF viewer head to move the window [#8305](https://github.com/logseq/logseq/pull/8305)
    - Add `{date}` template variable to quick-capture [#8560](https://github.com/logseq/logseq/pull/8560)
    - Add `:default-page` to `quick-capture-options` [#8529](https://github.com/logseq/logseq/pull/8529)
    - Add +/- syntax, (w)eek (m)onth (y)ear, and time support to query :inputs [#8387](https://github.com/logseq/logseq/pull/8387) - [Documentation](https://docs.logseq.com/#/page/advanced%20queries/block/query%20inputs)
- Jan 12th, 2023 Beta 0.8.16
    - PDF highlight drag & drop [#8103](https://github.com/logseq/logseq/pull/8103)
    - New query inputs for advanced query [#5674](https://github.com/logseq/logseq/pull/5674) [Document: Query Inputs](https://docs.logseq.com/#/page/advanced%20queries/block/query%20inputs)
    - Add a new option `:ui/show-full-blocks?` to show full blocks in references [#8124](https://github.com/logseq/logseq/pull/8124)
- Dec 29th, 2022 Beta 0.8.15
    - Use shortcut `mod+a` to select parent blocks up to the whole page [#7803](https://github.com/logseq/logseq/pull/7803)
    - Local Http server for API invoke [#7699](https://github.com/logseq/logseq/pull/7699)
- Dec 19th, 2022 Beta 0.8.13
    - LS Whiteboards now become a Beta Feature
    - Introduce a new config property `:logseq.query/nlp-date` . Default to `false` . Query without `logseq.query/nlp-date: true` would disable date normalization [#7708](https://github.com/logseq/logseq/pull/7708)
- Dec 2nd, 2022 Beta 0.8.12
    - Add `page` and `append` parameters to quickCapture URL, add corresponding config in `config.edn` [Documentation: LS Protocol](https://docs.logseq.com/#/page/LS%20Protocol)
- Nov 16th, 2022 Beta 0.8.11
    - [On-disk encryption is removed](https://discuss.logseq.com/t/deprecation-of-on-disk-encryption/12334) [#7221](https://github.com/logseq/logseq/pull/7221). You should follow the instructions to decrypt your graph files.
    - `logseq/pages-metadata.edn` is deprecated. Now it can be safely deleted.
- Nov 1st, 2022 Beta 0.8.10
    - Presentation bugs
- Oct 19th, 2022 Beta 0.8.9 **New Filename format**
    - Breaking Changes -- **Filename format**
        - `:legacy` and `:triple-lowbar`
    - **PDF enhancements**
        - Full-text search 🎉
        - Highlights list and colored label from the toolbar
    - A new theme-based highlighting system and a lot of enhancements to colors
- Sep 13th, 2022 Beta 0.8.6
    - Support for global config file, shared across all graphs [#6531](https://github.com/logseq/logseq/pull/6531) Global configuration
- Sep 1st, 2022 Beta 0.8.3
    - ==Config option to allow for longer, richer property values, new config option `:rich-property-values?` [#6336](https://github.com/logseq/logseq/pull/6336)==
    - Find in page on electron, use `CMD+F` or `Ctrl+F` to search term in current page [Documentation](https://docs.logseq.com/#/page/Find%20in%20page) [#6443](https://github.com/logseq/logseq/pull/6443)
- Aug 17th, 2022 Beta 0.8.1 **New Electron Version**
    - **NOTE**: This release updates Electron to version 19. If you encounter any errors, Clear Cache and re-add your graphs.
- Jul 20th, 2022 Beta 0.7.7
    - Auto-complete support for both block properties and their values [#5922](https://github.com/logseq/logseq/pull/5922)
- Jun 21st, 2022 Beta 0.7.5
    - Add request support, toolbar button pin/unpin to plugin API [#5712](https://github.com/logseq/logseq/pull/5712)
- Jun 9th, 2022 Beta 0.7.3
    - Support mod+e to copy block embed to current block
- May 31st, 2022 Beta 0.7.1
    - copy & Paste with rich-text formats, Use `Cmd+shift+v` or `Ctrl+shift+v` for copying/pasting without formatting [#5471](https://github.com/logseq/logseq/pull/5471)
- May 25th, 2022 Beta 0.7.0
    - Add `video` macro to embed various video URLs, deprecates old `youtube`, `vimeo` and `bilibili` macros [#5396](https://github.com/logseq/logseq/pull/5396)
- May 16th, 2022 Beta 0.6.9
    - lazy-loading for journals and queries, with loading skeleton
- May 10th, 2022 Beta 0.6.8
    - Support idiomatic shortcut `ctrl+n` for auto-complete navigation [#5202](https://github.com/logseq/logseq/pull/5202)
- Apr 29th, 2022 Beta 0.6.7
    - Parsing progress bar [#4980](https://github.com/logseq/logseq/pull/4980)
- Apr 18th, 2022 Beta 0.6.6
    - Open action for `logseq://` protocol, enabling cross-graph reference [#4881](https://github.com/logseq/logseq/pull/4881)
- Mar 8th, 2022 Beta 0.6.2
    - Add custom https proxy options for settings [#4373](https://github.com/logseq/logseq/pull/4373)
        - https://cn.logseq.com/t/topic/1847

## Core Design

LS is just a graph-driven note app,[^toc-is-hard-thing] which means linearity support is downside during several alternatives, like [obsidian](https://obsidian.md/).

LS is not perfect, a lot of bugs still existed on different versions[^bug-on-logseq]

The core of managing with LS is using templates and properties, which will be end on next release database version.

I mean, the table based on markdown is not the real excel table. It's impossible when you want to extends queries, then added some columns. The best product I know, is **notion**, even they could make a progress of project.

### Properties

> [!NOTE]
> Don't use alias as much as possible.

[^alias-should-more-power]

 A few properties hidden by default, like

- `collapsed`
- `template-including-parent`
- `query-properties: [:book-title :author :series]`
    - via: [Specify column order in query table view - Questions & Help - LS](https://discuss.logseq.com/t/specify-column-order-in-query-table-view/8877)
- `:table-view` can have one of the following values:
    - nil — default, show property button
    - true — table view, hide the button
    - false — regular view, hide the bbutton
    - more via: [(Partial Done) Hide query-table property heading - Feature Requests - LS](https://discuss.logseq.com/t/partial-done-hide-query-table-property-heading/4296/6)

### Configuration

Stored in config.edu file, which included a few option to choose, like code mirror.[^code-mirror]

### Tags == Linked pages

Basically, the page tagged is more special then linked pages. Then done. That's all. The sense I meet are the same thing.

LS change a lot, including the order shown by default, like hierarchy only could show one and they will not be the current page. It sucks a little. [^page-link-vs-tags]

Property Format

- Property will be parsed as delimiter in past and now it could be using \"\".
- via: [Quote string properties still get comma delimiter when a page reference exists · Issue #3747 · logseq/logseq](https://github.com/logseq/logseq/issues/3747)

### Hierarchies / HashTags | 层级 / 标签

这一功能只适用于进行快速搜索，一点也不适合把大段连续的知识打散的情况，因为如果一有要修改的想法，就要大刀阔斧地进行修改，VSCode 做起来还好，LS 做起来就是受苦，具体表现在：

- title + hierarchy **不会**出现在 Linked References 中
- alias + hierarchy **会**出现在 Linked References 中

So... 这只是一个重新分配名空间 (Namepace) 的问题

- 在 [Namespaces](https://mschmidtkorth.github.io/logseq-msk-docs/#/page/namespaces) 中是整理知识 (当然他的 说明/文档 非常简单...)
- 在 [Use Namespaces to Create a Dynamic Note Index in LS - YouTube](https://www.youtube.com/watch?v=fm45fG3A-Q4) 的更多的是 (层级) 搜索
    - 视频结尾说明一个更多的好处就是**在每次层级改变的时候, 只需要变更 Hashtag, 而不是将内容从一个文件搬运到另一个文件** (我是后者 hhh)

### Namespace #sugar

review hierarchy with

```
{{namespace logseq}}
```

### Filename specification

Basically, organize file structure & name is a difficult thing. Each time I change the page name and it would create the copied, so I have to delete it again. It's disappear in recent version.

Nouns is a awful suggestion, I lost many unlinked check...

use `___` or not

Which Version Change filename slash to `%2F`...: [Is it possible change the encoded slah %2F character in the file names of names spaces? - Questions & Help - LS](https://discuss.logseq.com/t/is-it-possible-change-the-encoded-slah-2f-character-in-the-file-names-of-names-spaces/8037/5)

### Presentation

like background-image: https://images.unsplash.com/photo-1498855926480-d98e83099315

- [The HTML presentation framework | reveal.js](https://revealjs.com/)
- But it only support show until **level 2**

### Plugin

Considered the page speed performance, please control the usage of plugins, because:

- The memory using by logseq is huge after start plugin
    - Debug memory usage on electron is difficult.
- Control the usage of graph.
    - **NOT ALL IN ONE**. Separate them to different pages.
    - Otherwise the whole graph would be huge

![](https://raw.githack.com/bGZo/assets/dev/2024/20241011235342.png)![](https://raw.githack.com/bGZo/assets/dev/2024/20241011235415.png)

### Embed Link

- `/embed Youtube video` with **timestamp**
- URL with \#t=XhYmZs \?t=XhYmZs
- Right click to select copy this position
- `@@` use html code!

### Dynamic Variable `<%  %>`

```
today => [[Today's journal page]]
yesterday => [[Yesterday's journal page]]
tomorrow => [[Tomorrow's journal page]]
time => Current time, e.g. 22:44
current page => [[Current page]]
Natural language date
    - Today, Tomorrow, Yesterday, Last Friday, etc
    - 17 August 2013 - 19 August 2013
    - This Friday from 13:00 - 16.00
    - 5 days ago
    - 2 weeks from now
    - Sat Aug 17 2013 18:40:39 GMT+0900 (JST)
    - 2014-11-30T08:15:30-05:30
Last Friday => [[Feb 12th, 2021]]
```

via: [Dynamic Variables](https://docs.logseq.com/#/page/Dynamic%20Variables) by [Templates injecting dynamic dates (and placeholders/arguments) - Feature Requests - LS](https://discuss.logseq.com/t/templates-injecting-dynamic-dates-and-placeholders-arguments/833)

### Export

Exported files by default is not included plugin setting. The better way is writing it in `custom.css`/`custom.js`/`config.edn`. I maintain a simple [Solarized](https://ethanschoonover.com/solarized/) [theme](https://gist.github.com/bGZo/b36c594b75499284d953bc2314d8e0b5)

### Publish

https://github.com/logseq/publish-spa

### Table

Tables are our first versioned component, accepting props to control the output. via: https://docs.logseq.com/#/page/tables

#### version 1

表格内换行 `[:br]`

#### New version demo

```
logseq.table.version: 2
logseq.table.hover: both
logseq.table.compact: true
logseq.table.headers: capitalize-first
logseq.table.borders: false
logseq.table.stripes: true
logseq.table.max-width: 10
logseq.color: pink
| notes | desc |
|-------| ------|
| logseq | privacy-first |
| obsdian | closed-source |
```

### Query
#### Multi tags

```clojure
{{query (and [[tag1]] [[tag2]] )}}
```

```clojure
#+BEGIN_QUERY
{:title "All todos with tag project"
 :query  [:find (pull ?b [*])
     :where
     [?b :block/path-refs [:block/name "2021w34"]]
     [?b :block/path-refs [:block/name "prm"]]
    ]}
#+END_QUERY
```

```clojure
#+BEGIN_QUERY
{:title [:h2 "✔ Doing"]
 :query [:find (pull ?b [*])
       :where
       (task ?b #{"DOING"})]
}
#+END_QUERY✔ Focus On
#+BEGIN_QUERY
{:title [:h2 "✔ To Do"]
 :query [:find (pull ?b [*])
       :where
       (task ?b #{"TODO"})]
}
#+END_QUERY✔ Focus On
{{query [[waiting-todo]] }}
#+BEGIN_QUERY
{:title [:h2 "Waiting ToDo"]
 :query  [:find (pull ?b [*])
     :where
     [?b :block/path-refs [:block/name "waiting-todo"]]
    ]}
#+END_QUERY
```

- [LS query with a custom view](https://www.loom.com/share/d007932e94db4b4981cca606bebdb54a)
- [LS queries example (using properties) and custom view](https://gist.github.com/tiensonqin/b319e19e6a1ef4659f24bb3b71d3d025)

#### ? the number of sub blocks

`{{query block (page <% current page %>)}}`

- [Queries](https://docs.logseq.com/#/page/queries)
- [Advanced Queries](https://docs.logseq.com/#/page/advanced%20queries)
- [The option to show block references on the graphview - Feature Requests - LS](https://discuss.logseq.com/t/the-option-to-show-block-references-on-the-graphview/3814/16)
- [logseq variable current-block - Google Search](https://www.google.com/search?q=logseq+variable+current-block)
- [Query for blocks with a specific parent on the current page - Questions & Help - LS](https://discuss.logseq.com/t/query-for-blocks-with-a-specific-parent-on-the-current-page/8284)

```
#+BEGIN_QUERY
{ :title "Current Members"
:query [:find (pull ?b [*])
  :in $ ?current-page
  :where
  [?b :block/page ?p]
  [?p :block/name ?current-page]
  [?b :block/parent ?parent]
  [?parent :block/content "Members"]]
:inputs [:current-page] }
#+END_QUERY
```

- [Advanced queries and the database documentation? - Questions & Help - LS](https://discuss.logseq.com/t/advanced-queries-and-the-database-documentation/1542/3)
    - Find all blocks referencing the page: `[LS]`, `_LS` or `tags`:` LS`.
    - `{{query [LS]}}`
    - Find all pages with page tags `tags`:` book` .
    - `{{query (page-tags book)}}`
    - Find all pages with both page tags `logseq` & `queries`.
    - `{{query (and (page-tags logseq) (page-tags queries))}}`
    - Find all pages with page tags `logseq` or `queries`
    - `{{query (page-tags logseq queries)}}`
    - Find all Todo blocks `doing` or `now`
    - `{{query (todo doing now)}}`
    - Find Todo blocks done in last 7 days.
    - `{{query (and (todo done) (between -7d today))}}`
    - Find all Todo/Doing Now/Later blocks in current page.
    - `{{query (and (todo todo doing now later) (page <% current page %>))}}`
    - Find all Todo/Doing Now/Later blocks where `tiensonqin` was tagged.
    - `{{query (and (todo todo doing now later) [tiensonqin]) }}`
- [Query for co-occurences in property - Look what I built - LS](https://discuss.logseq.com/t/query-for-co-occurences-in-property/5448/10)
- [Advanced Query: Blocks excluding certain tag - Questions & Help - LS](https://discuss.logseq.com/t/advanced-query-blocks-excluding-certain-tag/3173)

#### ? count of rows (show results-count in variable)

## [[custom/index|Custom Config]]

### Config.edn

```edn
; this config.edn refer those:
; https://github.com/logseq/logseq/blob/master/src/resources/templates/config.edn
; https://gist.github.com/tallguyjenks/6afc75e52a3d52d475b9df9dafdecfd2
; https://gist.github.com/tiensonqin/d871dcba33c4be460fabb3add0840276

{:meta/version 1

 :preferred-format "Markdown"

 :preferred-workflow :todo

 :hidden [ "/utils" ]

 :default-templates {
        :journals "daily"
        :pages "page" ;; wish one day could be supported.
 }

 :journal/page-title-format "yyyyMMdd"

 :journal/file-name-format "yyyyMMdd"

 :ui/enable-tooltip? true

 :ui/show-brackets? false

 :ui/show-full-blocks? true

 :ui/auto-expand-block-refs? true

 :feature/enable-block-timestamps? false

 :feature/enable-search-remove-accents? true

 :feature/enable-journals? true

 :feature/enable-whiteboards? true

 :feature/enable-flashcards? true

 :feature/disable-scheduled-and-deadline-query? true

 :scheduled/future-days 14

 :start-of-week 6

 ;; :custom-css-url "@import url('');"

 ;; :custom-js-url ""

 ;; :arweave/gateway "https://arweave.net"
 ;; via: https://www.reddit.com/r/logseq/comments/1apvfht/arweave_whats_that/

 :export/bullet-indentation :two-spaces

 :publishing/all-pages-public? true

 :default-home {
        :page "contents",
        :sidebar ["contents"]
 }

 :pages-directory "pages"

 :journals-directory "journals"

 :whiteboards-directory "whiteboards"

 :shortcuts {}

 :shortcut/doc-mode-enter-for-new-block? false

 :block/content-max-length 20000

 :ui/show-command-doc? true

 :ui/show-empty-bullets? false

 :query/views
 {:pprint
  (fn [r] [:pre.code (pprint r)])}

 :query/result-transforms
 {:sort-by-priority
  (fn [result] (sort-by (fn [h] (get h :block/priority "Z")) result))}

 :default-queries
 {:journals[
            ;; the "NOW" query asks the tasks which need to be finished "now",
            {:title "🔨 NOW"
             :query [:find (pull ?h [*])
                     ;:in $ ?start ?today
                     :where
                     [?h :block/marker ?marker]
                     [(contains? #{"NOW" "DOING"} ?marker)]
                     ;[?h :block/page ?p]
                     ;[?p :block/journal? true]
                     ;[?p :block/page? true]
                     ;[?p :block/journal-day ?d]
                     ;[(>= ?d ?start)]
                     ;[(<= ?d ?today)]
                    ]
             ;:inputs [:3650d :today]
             :result-transform (fn [result]
                                 (sort-by (fn [h]
                                            (get h :block/priority "Z")) result))
             :breadcrumbs-show? true
             :collapsed? true}

            ;; the "NEXT" query asks the future tasks.
            {:title "📅 NEXT"
             :query [:find (pull ?b [*])
                     ;:in $ ?start ?next
                     :where
                     [?h :block/marker ?marker]
                     [(contains? #{"NOW" "LATER" "TODO"} ?marker)]
                     [?h :block/page ?p]
                     [?p :block/journal? true]
                     [?p :block/journal-day ?d]
                     ;[(> ?d ?start)]
                     ;[(< ?d ?next)]
                     ]
             ;:inputs [:today :3650d-after]
             :breadcrumbs-show? true
             :collapsed? false}

            {:title "🗓️ Scheduled"
             :query [:find (pull ?b [*])
                     :in $ ?next
                     :where
                     (task ?b #{"NOW" "LATER" "TODO" "DOING" "WAIT" "WAITING"})
                     (not (property ?b :tags "Routine"))
                     (or-join [?b ?d]
                              [?b :block/scheduled ?d])
                     [(<= ?d ?next)]]
             :inputs [:today]
             :result-transform (fn [result]
                                 (sort-by (fn [h]
                                            (get h :block/scheduled)) result))
             :breadcrumbs-show? true
             :collapsed? true}

            {:title "🔥 OVERDUE"
             :query [:find (pull ?b [*])
                     ;:in $ ?start ?today
                     :where
                     (task ?b #{"NOW" "TODO"})
                     (not [?b :block/scheduled ?d])
                     (not [?b :block/deadline ?d])
                     ;(between ?b ?start ?today)
                     ]
             ;:inputs [:-3650d :today]
             :breadcrumbs-show? true
             :collapsed? true}
            ]}

 :commands[
           ;; without plugin dependencies, need to restart logseq
           ;; via: https://github.com/logseq/logseq/discussions/7976
           ["prefix/bilibili" "https://www.bilibili.com/video/"]
           ["prefix/youtube" "https://youtube.com/watch?v="]
           ["prefix/github" [[:editor/input "https://raw.githubusercontent.com//main/" {:backward-pos 6}]]]
           ["prefix/github/cdn" [[:editor/input "https://rawcdn.githack.com//main/" {:backward-pos 6}]]]
           ["iframe" [[:editor/input "{{iframe ,40vh,iframe-radius}}" {:backward-pos 21}]]]
           ["iframe/steam" [[:editor/input "{{iframe https://store.steampowered.com/widget/ ,200px}}" {:backward-pos 9}]]]
           ;; ["python code" [[:editor/input "```python\n\n```" {:backward-pos 4}]]]
           ;; ["cpp code" [[:editor/input "```cpp\n\n```" {:backward-pos 4}]]]
           ;; ["java code" [[:editor/input "```java\n\n```" {:backward-pos 4}]]]
           ;; ["shell code" [[:editor/input "```shell\n\n```" {:backward-pos 4}]]]
           ;; https://discuss.logseq.com/t/macros-and-commands-lets-share/9565
           ;; https://discuss.logseq.com/t/wish-add-the-code-block-by-using/12681
           ;; https://github.com/logseq/logseq/issues/9198

          ]

 :outliner/block-title-collapse-enabled? false ;; NOTE: the prefermance of logseq will be slowed down.

 :macros {
       ;; leecode <url> <height> [class(iframe-radius)]
       "leetcode" "<iframe src='https://leetcode.cn/problems/$1' class='$3' style='height:$2' allow='fullscreen'></iframe>
<center>via: <a href='https://leetcode.cn/problems/$1' target='_blank' class='external-link'>https://leetcode.cn/problems/$1</a></center>"

       "nav" "<img class='inline-left-tag' src='https://img.shields.io/website.svg?label=&cacheSeconds=7200&url=$1'/><a href='$1' target='_blank' class='external-link'>$1</a>"
       "nav-ri" "<a href='$1' target='_blank' class='external-link'>$1</a><img class='inline-right-tag' src='https://img.shields.io/website.svg?label=&cacheSeconds=7200&url=$1'/>"
       "navi" "<img class='inline-left-tag' src='https://img.shields.io/website.svg?label=&cacheSeconds=7200&url=$2'/><a href='$2' target='_blank' class='external-link'>$1</a>"
       "navi-ri" "<a href='$2' target='_blank' class='external-link'>$1</a><img class='inline-left-tag' src='https://img.shields.io/website.svg?label=&cacheSeconds=7200&url=$2'/>"

       "gh" "<a href='https://github.com/$1' target='_blank' class='external-link'>https://github.com/$1</a><img class='inline-right-tag' src='https://img.shields.io/github/stars/$1'/>"
       "tg" "https://t.me/$1 <a href='tg://resolve?domain=$1' target='_blank' class='external-link'>🚀</a>"
       "myanimelist" "https://myanimelist.net/anime/$1"
       "doufilm" "https://book.douban.com/subject/$1"
       "image/cover" "![]($1){:width 100}"
       "am" "<iframe allow='autoplay *; encrypted-media *;' frameborder='0' height='450' style='width:100%;max-width:660px;overflow:hidden;background:transparent;' sandbox='allow-forms allow-popups allow-same-origin allow-scripts allow-storage-access-by-user-activation allow-top-navigation-by-user-activation' src='https://embed.music.apple.com/cn/album/$1' ></iframe>
"

       ;; wish one day could support
       ;;"ghgist" "<script src='https://gist.github.com/bGZo/$1.js'></script>"

       }


 :ref/default-open-blocks-level 2

 :ref/linked-references-collapsed-threshold 10

 :graph/settings {:orphan-pages? true
 :builtin-pages? false
 :excluded-pages? false
 :journal? false}

 :graph/forcesettings {
        :link-dist       180
        :charge-strength -600
        :charge-range    600
 }

 :favorites ["inbox" "announcements" "issue" "dashboard" "musics" "writings" "hobbies" "omnivore" "2022 archive" "history/burden" "hecaitou" "networking" "postgresql修炼之道" "blogroll"]

;; :srs/learning-fraction 0.5

;; :srs/initial-interval 4

 :block-hidden-properties #{
                            :public 
                            ;:title 
                            ;:icon 
                            ;:created
                            }

 :property-pages/enabled? true

:property-pages/excludelist #{
                              :TODO
                              :DOING
                              :DONE
                              :WAITING
                              :icon
                              :also
                              :author
                              :bangumi
                              :cover
                              :created
                              :description
                              :difficulty
                              :douban
                              ;:duration
                              ;:exclude-from-graph-view
                              :isbn
                              :lang
                              :mark
                              :published
                              :published
                              :rating
                              :schema
                              :source
                              :status
                              ;:tags
                              :template
                              :template-including-parent
                              :title
                              :type
                              :weread
                              :wikipedia

                              :.ol
                              :.kanban
                              :.kanban-500
       }

:property/separated-by-commas #{
       ;:alias :tags :also
       }

:ignored-page-references-keywords #{
       ;:author :website
                                    :tags
                                    }
 
;; :logbook/settings
;; {:with-second-support? false ;limit logbook to minutes, seconds will be eliminated
;;  :enabled-in-all-blocks true ;display logbook in all blocks after timetracking
;;  :enabled-in-timestamped-blocks false ;don't display logbook at all
;; }

;; :mobile/photo
;; {:allow-editing? true
;;  :quality        80}

;; :mobile
;; {:gestures/disabled-in-block-with-tags ["kanban"]}

 :editor/extra-codemirror-options {
        :lineWrapping   false  ; when code is long, read really sucks 
        :lineNumbers    true
        :readOnly       false
        ;:theme "rdark"
 }

 :editor/logical-outdenting? true

 :editor/preferred-pasting-file? false

;; :quick-capture-templates
;; {:text "[[quick capture]] **{time}**: {text} from {url}"
;;  :media "[[quick capture]] **{time}**: {url}"}

;; :quick-capture-options
;; {:insert-today? false           ;; Default value: true
;;  :redirect-page? false          ;; Default value: false
;;  :default-page "quick capture"} ;; Default page: "quick capture"

;; File sync options
;; Ignore these files when syncing, regexp is supported.
;; :file-sync/ignore-files []

;; :dwim/settings
;; {:admonition&src?  true        ;; Default value: true
;;  :markup?          false       ;; Default value: false
;;  :block-ref?       true        ;; Default value: true
;;  :page-ref?        true        ;; Default value: true
;;  :properties?      true        ;; Default value: true
;;  :list?            false}      ;; Default value: false

 :file/name-format :triple-lowbar
 }
```

### Custom.css

```css
@import url('https://gistcdn.githack.com/bGZo/8df460ec380a5bd4385cb8225e894cf0/raw/8fc9f15b8f8b652119bfa15e92740d6cf9b6ae32/7.propsLayout.custom.css');
@import url('https://rawcdn.githack.com/yoyurec/logseq-awesome-content/main/src/modules/admonition/admonition.css');
@import url('https://rawcdn.githack.com/yoyurec/logseq-awesome-content/main/src/modules/quotes/quotes.css');
@import url('https://rawcdn.githack.com/yoyurec/logseq-awesome-content/main/src/modules/tasks/tasks.css');
@import url('https://rawcdn.githack.com/yoyurec/logseq-awesome-content/main/src/modules/code/code.css');
@import url("https://raw.githack.com/yoyurec/logseq-awesome-content/main/src/modules/columns/columns.css");
@import url("https://raw.githack.com/yoyurec/logseq-awesome-content/main/src/modules/todayQueries/todayQueries.css");
@import url("https://raw.githack.com/yoyurec/logseq-awesome-content/main/src/modules/breadcrumbs/breadcrumbs.css");

/**
 * feat: with right layout ability
 * via: https://discuss.logseq.com/t/align-text-images-etc-to-the-right-workaround/13375
 */
.ra{
  float: right;
}

/**
 * fix: hide the help button
 */
 .cp__sidebar-help-btn {
  display:none;
}

/**
 * fix: props margin too short.
 */
.block-properties > div > :is(div, span, a):first-child {
  width: calc(100% + 1.4rem);
}
.block-properties .page-property-value {
  margin-left: 2rem;
}
.block-properties > div > div {
  display: block !important;
}
.block-properties:not(.page-properties) > div > :is(div, span, a):first-child:after, .block-properties.page-properties > div > :is(div, span, a):first-child:after, .ls-block.ls-block.block-properties > div > :is(div, span, a):first-child:after {
  display: inline;
  margin: 0;
  float: right;
}


/**
 * feat: table wrap style by tag
 */
a.tag[data-ref*="config/table-wrap"] {
    display: none;
}
[data-refs-self*="config/table-wrap"] .whitespace-nowrap {
  white-space: wrap;
}


/**
 * style[required]: custom horizontal rule.
 */
hr {
  /* border-color: var(--); */
  margin: 1rem 0;
}


/**
 * style: custom color schame
 */
:root {
  --usuao: #91B493;
  --aoni: #516E41;
  --ls-tag-text-opacity: .7;
  --ls-highlight-color: var(--usuao);
  --ls-highlight-text-color: var(--aoni);
  --ls-link-text-color: var(--aoni);
}
.light-theme, html[data-theme="light"]{
  --ls-tag-background-hover: var(--color-level-1);
  --ls-page-blockquote-border-color: var(--ls-highlight-color);
  --ls-page-blockquote-bg-color: var(--color-level-3);
  --ls-page-mark-bg-color: var(--ls-highlight-color);
  --ls-page-properties-background-color: var(--color-level-3);
}

@media (prefers-color-scheme: light) {
  /**
   * fix: overwrite build-in css
   * link: http://unpkg.com/bgzo/img/texture.png
   */
  #app-container, #main-container {
    background-image: url(http://unpkg.com/bgzo/img/texture.png);
    background-repeat: repeat;
  }
}

@media (prefers-color-scheme: dark) {
  .dark-theme, html[data-theme="dark"]{
    --ls-tag-background-hover: var(--color-level-1);
    --ls-page-blockquote-border-color: var(--ls-highlight-color);
    --ls-page-blockquote-bg-color: var(--color-level-3);
    --ls-page-mark-bg-color: var(--ls-highlight-color);
    --ls-page-properties-background-color: var(--color-level-3);
  }
  img {
    filter: brightness(.80) contrast(1.1);
  }
  :selection {
    background:#d3d3d3;
    color:#555;
  }
  blockquote, .ls-block[data-refs-self*="\"quote\""]:not(.pre-block) {
    background-color: var(--lx-gray-05-alpha);
    border-left: 4px solid var(--ls-highlight-text-color);
  }
  .inline-wrap,
  .block-content,
  ol > li > p,
  .breadcrumb.block-parents > a,
  .cp__query-builder .cp__select .input-wrap input {
    color: var(--lx-gray-11);
  }
  .cp__query-builder .cp__select .input-wrap input {
    background: black;
  }
  .left-sidebar-inner .nav-content-item .header{
    background: var(--left-sidebar-bg-color);
  }

  /**
   * fix: overwrite build-in css
   * link: http://unpkg.com/bgzo/img/texture.png
   */
  #app-container,#main-container {
    background-image:
      linear-gradient(rgba(130, 130, 130, .05) 0.01em, transparent .05em),
      linear-gradient(90deg, rgba(130, 130, 130, .05) 0.01em, transparent .05em);
    background-size: 1em 1em;
    background-attachment: scroll;
    background-repeat: repeat;
  }

}
mark{
  color: #1e1e1e;
  code {
    background-color: var(--ls-highlight-color) !important;
  }
  a {
    color: black !important;
  }
}
.page-ref {
  color: var(--ls-highlight-text-color);
}


/**
 * style[required]: custom tag
 */
a.tag {
  display: inline;
  background: none;
  border: 1.5px dashed var(--ls-highlight-text-color, #045591);
  color: var(--ls-highlight-text-color);
}
a.tag:active, a.tag:focus, a.tag:hover {
  outline: none;
  text-decoration: none;
}


/**
 * style: hyber link style with underline
 */
.external-link {
  border: 0;
  text-decoration: underline;
  text-decoration-style: dashed;
  color: var(--ls-highlight-text-color);
}


/**
 * style: code mirror
 */
.CodeMirror {
  border-radius: var(--ls-border-radius-low);
}


/**
 * feat: task cancel text-decoration
.done {
  text-decoration: none !important;
  opacity: var(--ls-tag-text-opacity);
}
 */


.iframe-radius, .references-blocks-item {
  --tw-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06) !important;
  border-radius: 0.5rem !important;
  box-shadow: var(--tw-shadow) !important;
}

.raw_html {
  display: inline;
}
.inline-left-tag {
  display: inline;
  margin-right: .5em;
}
.inline-right-tag {
  display: inline;
  margin-left: .5em;
}

.macro {
    display: inline;
}
```

### Custom.js

```js
<script src="https://gist.github.com/defunkt/2059.js"></script>

const addCopyButtonToCodeBlock = (block) => {
  if (block.querySelector(".copy-code-button")) return;
  const copyButton = document.createElement("button");
  copyButton.className = "copy-code-button";
  copyButton.textContent = "Copy";
  copyButton.style.cssText = `
    position: absolute;
    bottom: 5px;
    right: 5px;
    z-index: 10;
    padding: 2px 5px;
    cursor: pointer;
    font-size: 70%;
  `;
  copyButton.addEventListener("click", () => {
    copyCodeContent(block);
  });
  block.style.position = "relative";
  block.appendChild(copyButton);
};
const copyCodeContent = (block) => {
  const codeMirror = block.querySelector(".CodeMirror");
  let content = "";
  if (codeMirror && codeMirror.CodeMirror) {
    content = codeMirror.CodeMirror.getValue();
  } else {
    const codeElement =
      block.querySelector("textarea") || block.querySelector("pre");
    if (codeElement) {
      content = codeElement.value || codeElement.textContent;
    } else {
      console.error("No code content found");
      return;
    }
  }
  navigator.clipboard
    .writeText(content)
    .then(() => {
      logseq.api.show_msg("Copied to clipboard");
    })
    .catch((err) => {
      console.error("Could not copy text: ", err);
      logseq.api.show_msg("Could not copy to clipboard");
    });
};
const observer = new MutationObserver((mutations) => {
  mutations.forEach((mutation) => {
    if (mutation.type === "childList") {
      mutation.addedNodes.forEach(function (node) {
        if (node.nodeType === Node.ELEMENT_NODE) {
          if (node.classList.contains("cp__fenced-code-block")) {
            addCopyButtonToCodeBlock(node);
          } else {
            const codeBlocks = node.querySelectorAll(".cp__fenced-code-block");
            codeBlocks.forEach(addCopyButtonToCodeBlock);
          }
        }
      });
    }
  });
});
observer.observe(document.body, { childList: true, subtree: true });
document
  .querySelectorAll(".cp__fenced-code-block")
  .forEach(addCopyButtonToCodeBlock);
```

### Plugins.edn

```edn
{:logseq-dictionary
 {:version "0.0.2",
  :repo "trashhalo/logseq-dictionary",
  :effect false,
  :theme false},
 :logseq-block-to-page
 {:version "v1.3.0",
  :repo "hyrijk/logseq-plugin-block-to-page",
  :effect false,
  :theme false},
 :logseq-mark-map
 {:version "v0.4.6", :repo "vipzhicheng/logseq-plugin-mark-map", :effect false, :theme false}
 :logseq-web-parser {:version "1.0.4", :repo "sawhney17/logseq-web-parser", :effect true, :theme false}
 :logseq-plugin-heading-level-shortcuts {:version "v0.0.6", :repo "vipzhicheng/logseq-plugin-heading-level-shortcuts", :effect false, :theme false}
 :logseq-copy-code-plugin {:version "v.1.2.0", :repo "vyleung/logseq-copy-code-plugin", :effect true, :theme false}
 :logseq-webpage-title {:version "v1.3.0", :repo "paulkinlan/logseq-webpage-title", :effect true, :theme false}
 :logseq-pdf-export-plugin {:version "2.2.8", :repo "sawhney17/logseq-pdf-export", :effect true, :theme false}
 :logseq13-full-house {:version "v4.1.0", :repo "stdword/logseq13-full-house-plugin", :effect true, :theme false}
 :logseq-agenda {:version "v3.13.1", :repo "haydenull/logseq-plugin-agenda", :effect true, :theme false}
 :logseq-omnivore {:version "v1.16.6", :repo "omnivore-app/logseq-omnivore", :effect false, :theme false}
 :logseq-imgur-upload {:version "v0.0.4", :repo "hserranome/logseq-imgur-upload", :effect false, :theme false}
 :logseq-focus-mode {:version "v1.0.4", :repo "sethfair/logseq-focus-mode", :effect false, :theme false}
 :logseq-journals-calendar {:version "v0.10.10", :repo "xyhp915/logseq-journals-calendar", :effect false, :theme false}
 :logseq-localassets-plugin {:version "1.6.5", :repo "hkgnp/logseq-localassets-plugin", :effect true, :theme false}
 :logseq-random-note {:version "1.1.2", :repo "tankcool/logseq-random-note", :effect false, :theme false}
 :logseq-anki-sync {:version "v4.6.1", :repo "debanjandhar12/logseq-anki-sync", :effect true, :theme false}
 :logseq-heatmap {:version "v2.4.3", :repo "pengx17/logseq-plugin-heatmap", :effect true, :theme false}
 :logseq-tidy-blocks-plugin {:version "v.1.2.1", :repo "vyleung/logseq-tidy-blocks-plugin", :effect true, :theme false}
 :logseq-browser {:version "v1.1.2", :repo "haydenull/logseq-plugin-browser", :effect false, :theme false}
 :template-gallery {:version "0.10", :repo "dangermccann/logseq-template-gallery", :effect true, :theme false}
 :logseq-movies {:version "1.0.1", :repo "darthorimar/logseq-movies-plugin", :effect true, :theme false}
 :logseq-ai-assistant {:version "v1.1.1", :repo "UNICKCHENG/logseq-ai-assistant", :effect false, :theme false}
 :logseq-local-telegram-bot {:version "v0.2.14", :repo "LelouchHe/logseq-local-telegram-bot", :effect false, :theme false}
 :logseq-calendars-plugin {:version "2.2.2", :repo "sawhney17/logseq-calendars-plugin", :effect true, :theme false}
 :logseq-open-in-external-app {:version "v1.0.0", :repo "haydenull/logseq-plugin-open-in-external-app", :effect false, :theme false}
 :logseq-excalidraw {:version "v1.5.1", :repo "haydenull/logseq-plugin-excalidraw", :effect true, :theme false}
 :logseq-chinese-tools {:version "v0.0.2", :repo "piobmx/logseq-chinese-tools", :effect false, :theme false}
 :logseq-reminder {:version "v0.9.1", :repo "sethyuan/logseq-plugin-reminder", :effect true, :theme false}
 :logseq-graph-analysis {:version "0.12.0", :repo "trashhalo/logseq-graph-analysis", :effect true, :theme false}
 :logseq-git {:version "v1.5.4", :repo "haydenull/logseq-plugin-git", :effect true, :theme false}
 :logseq-drawio-plugin {:version "v1.3.0", :repo "lee88688/logseq-drawio-plugin", :effect true, :theme false}
 :logseq-plugin-show-weekday-and-week-number {:version "v1.40.0", :repo "YU000jp/logseq-plugin-show-weekday-and-week-number", :effect true, :theme false}
 :logseq-code-formatter {:version "v1.1.0", :repo "PerfectPan/logseq-plugin-code-formatter", :effect false, :theme false}
 :logseq-plugin-github-get {:version "v1.0.2", :repo "mandpd/logseq-plugin-github-get", :effect false, :theme false}
 :logseq-bullet-threading {:version "v1.1.4", :repo "pengx17/logseq-plugin-bullet-threading", :effect false, :theme false}
 :logseq-link-unlinked {:version "v1.5.1", :repo "usoonees/logseq-plugin-link-unlink", :effect true, :theme false}
 :logseq-tags {:version "v0.1.2", :repo "gidongkwon/logseq-plugin-tags", :effect false, :theme false}
 :logseq-powertags-plugin {:version "1.0.5", :repo "hkgnp/logseq-powertags-plugin", :effect true, :theme false}
 :logseq-open-in-code {:version "v0.0.7", :repo "rebornix/logseq-open-in-code", :effect true, :theme false}
 :logseq-schrodinger {:version "1.3.1", :repo "sawhney17/logseq-schrodinger", :effect true, :theme false}
 :logseq-image-uploader {:version "v0.0.12", :repo "JJAYCHEN1e/logseq-plugin-image-uploader", :effect true, :theme false}
 :logseq-tocgen {:version "v2.13.0", :repo "sethyuan/logseq-plugin-tocgen", :effect true, :theme false}
 :logseq-luckysheet {:version "v0.9.3", :repo "sethyuan/logseq-plugin-luckysheet", :effect true, :theme false}
 :logseq-markdown-table {:version "v1.8.1", :repo "haydenull/logseq-plugin-markdown-table", :effect false, :theme false}
 :logseq-insert-movie-properties {:version "v1.7.1", :repo "b-yp/logseq-insert-movie-properties", :effect true, :theme false}
 :logseq-helium-plugin {:version "v.2.1.3", :repo "vyleung/logseq-helium-plugin", :effect true, :theme false}
 :logseq-rss-reader {:version "v1.1.0", :repo "b-yp/logseq-rss-reader", :effect true, :theme false}
 :logseq-plugin-leetcode {:version "v0.0.1", :repo "alucpro/logseq-plugin-leetcode", :effect true, :theme false}
 :logseq-tabs {:version "v1.19.4", :repo "pengx17/logseq-plugin-tabs", :effect true, :theme false}
 :logseq-emoji-picker-fork {:version "v0.0.6", :repo "walsvid/logseq-emoji-picker-fork", :effect false, :theme false}
 :logseq-tabbed-sidebar {:version "v0.13.4", :repo "sethyuan/logseq-plugin-tabbed-sidebar", :effect true, :theme false}
 :logseq-split-block {:version "v1.2.0", :repo "hyrijk/logseq-plugin-split-block", :effect false, :theme false}
 :logseq-wordcount-plugin {:version "v2.3.2", :repo "hkgnp/logseq-wordcount-plugin", :effect false, :theme false}
 :logseq-toc-plugin {:version "v2.0.1", :repo "benjypng/logseq-toc-plugin", :effect true, :theme false}
 :logseq-plugin-show-page-date {:version "v1.0.1", :repo "YU000jp/logseq-plugin-show-page-date", :effect true, :theme false}
 :logseq-banners-plugin {:version "v3.4.11", :repo "yoyurec/logseq-banners-plugin", :effect true, :theme false}
 :logseq-smartblocks {:version "3.51", :repo "sawhney17/logseq-smartblocks", :effect false, :theme false}
 :logseq-add-para-properties {:version "v1.2.1", :repo "georgeguimaraes/logseq-plugin-add-PARA-properties", :effect false, :theme false}
 :logseq-paste-more {:version "v1.5.9", :repo "usoonees/logseq-plugin-paste-more", :effect true, :theme false}
 :logseq-discourse-graphs {:version "v1.4.0", :repo "sawhney17/logseq-discourse-graphs", :effect true, :theme false}
 :logseq-inbox-telegram-plugin {:version "v0.1.5", :repo "shady2k/logseq-inbox-telegram-plugin", :effect false, :theme false}
 :logseq-awesome-links {:version "v1.15.16", :repo "yoyurec/logseq-awesome-links", :effect true, :theme false}}

```

## Waiting features

- [ ] hide duplicating **aliases** on graph
    - issue via: https://github.com/logseq/logseq/issues/4709
    - discuss via https://discuss.logseq.com/t/enhancement-of-aliases/14466/19
- [ ] outline **toc** for sidebar
    - discuss via https://discuss.logseq.com/t/outline-overview-for-sidebar/740/30
- [ ] **equb** view book
    - saving memory
    - discuss via https://discuss.logseq.com/t/support-epub-format-ebooks/2010/27
- [ ] disable **lazy load**
    - this make search and reach impossible in huge blocks
    - discuss via https://discuss.logseq.com/t/provide-option-to-disable-lazy-load/9784/14
- [ ] sort for **references**
    - discuss via: https://discuss.logseq.com/t/sort-linked-references/10391/6
- [ ] cross platform with **plugin**
    - discuss via https://discuss.logseq.com/t/plugin-support-for-ios-android-apps/10109/21
        - they said the most difficult is UI library during multi platform
- [ ] custom **icon** with image
    - discuss via https://discuss.logseq.com/t/image-asset-as-page-icon/3826/11
- [ ] different **environment** on different graph
    - https://discuss.logseq.com/t/different-plugins-for-each-graph/5846/4
- [ ] **fuzzy search** is not fuzzy
    - like search `windows memo` or `memo windows`, you will get different results
    - Not support fuzzy query, for example, I have a page name `widows-meme`, when you type `windows meme`, it's okey, but when you type `meme windows`, they would show nothing.
    - https://discuss.logseq.com/t/option-to-choose-between-fuzzy-search-and-precise-search/17528/1
- [ ] **export** with plugin feature on `custom.js`
    - https://discuss.logseq.com/t/export-published-document-with-plugin-installed-in-a-dockerized-container/22603
- [ ] open the deleted page recently directly
- [ ] Image asset as page icon
    - https://discuss.logseq.com/t/image-asset-as-page-icon/3826
- [ ] delete a unused file
    - Plugin I think, cause just find wiki for file name is enough.
    - via: [How to clean unlinked files in an effective way - Questions & Help - LS](https://discuss.logseq.com/t/how-to-clean-unlinked-files-in-an-effective-way/2125)
- [ ] Default template stored in `config.edu` is not supported for page, only for journal

## Alternatives via: [[publish-your-writing|How to publish your writing]]

---

- Considered Dep making the repo size increased, so clone main branch is enough.

```shell
    git clone --single-branch -b main git@github.com:bGZo/wiki-logseq.git
```

## Reference
  - https://discuss.logseq.com/c/look-what-i-built
  - https://github.com/mschmidtkorth/logseq-msk-docs
  - [求推荐：知识管理-电子书阅读管理 APP？ - V2EX](https://www.v2ex.com/t/826204)
  - [知识信息组织索引工具推荐 - V2EX](https://www.v2ex.com/t/222874)
  - [有什么比较好的用于摘抄网页的工具吗 - V2EX](https://www.v2ex.com/t/797881)
  - [[~笔记软件为何需要本地存储-Skywind-Inside]]

[^used_note_application]: (See ((6474b5b1-ad1a-47c3-bc2c-4343950295a9)))
[^toc-is-hard-thing]: via: https://discuss.logseq.com/t/outline-overview-for-sidebar/740/20, I choose use namespace instead of content side bar.
[^bug-on-logseq]: https://discuss.logseq.com/t/pasting-photos-increases-the-size-of-the-image-file-massively/9363
[^alias-should-more-power]: The working of alias on logseq is kind of weird, which should not appear on graph, because so much more properties, or connect. That would be mess without ability to hide. via: https://discuss.logseq.com/t/enhancement-of-aliases/14466, Towards non-native speakers in English, `alias` is a little bit interesting, more aliases makes graph more complex, which links every node duplicately. This is really funciton need to be enhanced.
[^code-mirror]: via:https://github.com/logseq/logseq/pull/3699, https://discuss.logseq.com/t/make-it-easy-to-configure-syntax-highlighting-theme/4617, https://github.com/codemirror/codemirror5
[^page-link-vs-tags]: [The difference between ((page links)), #tags, and properties: DocumentationLS](https://discuss.logseq.com/t/the-difference-between-page-links-tags-and-properties/8393), https://www.youtube.com/watch?v=FQg52aN19w8
