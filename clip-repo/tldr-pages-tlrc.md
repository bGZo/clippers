---
title: tldr-pages/tlrc
aliases: tlrc
created: 2025-01-13T10:52:47
modified: 2025-01-13T11:02:04
description: Collaborative cheatsheets for console commands
source: https://github.com/tldr-pages/tlrc
tags:
  - star
  - document
  - cheatsheet
  - commandline
tags-link: 
type: repo
---
## Repo Meta

![](https://img.shields.io/github/stars/tldr-pages/tlrc?style=for-the-badge&label=stars) ![](https://img.shields.io/github/repo-size/tldr-pages/tlrc?style=for-the-badge&label=size) ![](https://img.shields.io/github/created-at/tldr-pages/tlrc?style=for-the-badge&label=since)

[![](https://github-readme-stats.vercel.app/api/pin/?username=tldr-pages&repo=tlrc&bg_color=00000000)](https://github.com/tldr-pages/tlrc)

## Notes


## Offline Client

### Command-line via: https://github.com/tldr-pages/tlrc

#### [MacOS](macos)

```shell
brew install tlrc

tldr --config-path

# Setting Language
vim /Users/bgzo/Library/Application\ Support/tlrc/config.toml
```

```toml
[cache]
dir = "~/Library/Caches/tlrc"
mirror = "https://github.com/tldr-pages/tldr/releases/latest/download"
auto_update = true
max_age = 336
languages = []

[output]
show_title = true
platform_title = false
show_hyphens = false
example_prefix = "- "
compact = false
raw_markdown = false

[indent]
title = 2
description = 2
bullet = 2
example = 4

[style.title]
color = "magenta"
background = "default"
bold = true
underline = false
italic = false
dim = false
strikethrough = false

[style.description]
color = "magenta"
background = "default"
bold = false
underline = false
italic = false
dim = false
strikethrough = false

[style.bullet]
color = "green"
background = "default"
bold = false
underline = false
italic = false
dim = false
strikethrough = false

[style.example]
color = "cyan"
background = "default"
bold = false
underline = false
italic = false
dim = false
strikethrough = false

[style.url]
color = "red"
background = "default"
bold = false
underline = false
italic = true
dim = false
strikethrough = false

[style.inline_code]
color = "yellow"
background = "default"
bold = false
underline = false
italic = true
dim = false
strikethrough = false

[style.placeholder]
color = "red"
background = "default"
bold = false
underline = false
italic = true
dim = false
strikethrough = false
```

### web via: https://tldr.inbrowser.app/
