---
title: "优化代码审查 · Issue #12 · Bylx666/key-lang"
aliases: "优化代码审查 · Issue #12 · Bylx666/key-lang"
created: 2025-03-31T22:18:12
modified: 2025-03-31T22:18:25
description: "很荣幸看到您没有经过rustfmt格式化，也没有经过rust官方的lint：clippy的代码，也很抱歉没有带上你所说的“脑子” 对于您的代码有没有通过cargo check我是存疑的，或许你的那一行allow已经很好地掩护了你的屎 我承认我是一个傻逼，你给我喂的屎我全部吃了，不仅如此，我还对你的代码不断f8 ，ctrl . 修复一个个warn 别被吹上天了，这个语言作为一个废物还是很不错的，起码它跑起来了不是吗？虽然对于其他人来说这只是你拉在github上的一坨屎，但..."
source: "https://github.com/Bylx666/key-lang/issues/12"
tags:
tags-link:
type: "archive-web"
---

### 很荣幸看到您没有经过 rustfmt 格式化，也没有经过 rust 官方的 lint：clippy 的代码，也很抱歉没有带上你所说的“脑子”

### 对于您的代码有没有通过 cargo check 我是存疑的，或许你的那一行 allow 已经很好地掩护了你的屎

### 我承认我是一个傻逼，你给我喂的屎我全部吃了，不仅如此，我还对你的代码不断 f8 ，ctrl . 修复一个个 warn

### 别被吹上天了，这个语言作为一个废物还是很不错的，起码它跑起来了不是吗？虽然对于其他人来说这只是你拉在 github 上的一坨屎，但是您仍然可以认为它就是最精致的语言呐

### 对了，给你看看我很可能不是 VSCode 的 VSCode 很可能删掉那行遮羞布的输出

[![image](https://private-user-images.githubusercontent.com/97959381/326263888-2a796d92-9f27-4da8-8bc5-bdf55909371c.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDM0MzA5MzIsIm5iZiI6MTc0MzQzMDYzMiwicGF0aCI6Ii85Nzk1OTM4MS8zMjYyNjM4ODgtMmE3OTZkOTItOWYyNy00ZGE4LThiYzUtYmRmNTU5MDkzNzFjLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTAzMzElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwMzMxVDE0MTcxMlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTMzYmM0ZGI3ZTY3ZDUyZDIwNjczNzhlZDkyYTM1NjFkNjZmN2JiNTYwYzFiYWRjYWNjMWNkZTUxMDkzMzNmODcmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.EEVO20yx4pup3sy9v_xGnRj4nhkoLnkk_kS2Nw7x4Go)](https://private-user-images.githubusercontent.com/97959381/326263888-2a796d92-9f27-4da8-8bc5-bdf55909371c.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDM0MzA5MzIsIm5iZiI6MTc0MzQzMDYzMiwicGF0aCI6Ii85Nzk1OTM4MS8zMjYyNjM4ODgtMmE3OTZkOTItOWYyNy00ZGE4LThiYzUtYmRmNTU5MDkzNzFjLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTAzMzElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwMzMxVDE0MTcxMlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTMzYmM0ZGI3ZTY3ZDUyZDIwNjczNzhlZDkyYTM1NjFkNjZmN2JiNTYwYzFiYWRjYWNjMWNkZTUxMDkzMzNmODcmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.EEVO20yx4pup3sy9v_xGnRj4nhkoLnkk_kS2Nw7x4Go)

你知道什么是 clippy 吗？[链接](https://github.com/rust-lang/rust-clippy) 挂给你，好好了解一下

### 同时您滥用 static mut 的设计模式也是非常优秀的，看到我的 pr 中使用的 addr\_of\_mut 了吗？在 rust2024，对 static mut 的&mu 将会触发一个编译错误，但是不使用 clippy 的您是不会在代码无法编译之前意识到这一点的

### 既然您已经使用了 nightly 工具链，可否恳请您花一点点时间使用 miri 看看你的代码有没有 ub 呢？看到\*mut 时我可是眼前一亮啊，仿佛正在观看一段精美的 C 代码！

### 有时间多看看书，不只是准备高考，同时也多学习一些你不知道的东西充实一下你自己，起码得让你意识到这个项目时一坨屎

### 另外，提升一下你令人窒息的英语水品吧
