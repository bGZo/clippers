---
title: midpoint/weread
aliases:
  - weread
created: 2025-04-12T10:46:08
modified: 2025-04-12T10:46:26
description: 微信读书之青龙篇
source: https://github.com/midpoint/weread
tags:
  - star
tags-link:
  - "[[bGZo-userscripts]]"
type: repo
---

## Repo Meta

![](https://img.shields.io/github/stars/midpoint/weread?style=for-the-badge&label=stars) ![](https://img.shields.io/github/repo-size/midpoint/weread?style=for-the-badge&label=size) ![](https://img.shields.io/github/created-at/midpoint/weread?style=for-the-badge&label=since)

[![](https://github-readme-stats.vercel.app/api/pin/?username=midpoint&repo=weread&bg_color=00000000)](https://github.com/midpoint/weread)

## Notes

1、先在青龙面板中拉取任务：

```
ql repo https://github.com/midpoint/weread.git "main" "" "" "main"  "py"
```

2、脚本逻辑还是比较简单的，运行 `main.py` 即可，依赖自行安装。大部分代码不需要改动。

先自行获取 heads 和 cookies 信息，更新 main.py 中的信息： 在微信阅读官网 [微信读书 (qq.com)](https://weread.qq.com/) 搜索【三体】点开阅读点击下一页进行抓包，抓到 `read` 接口 `https://weread.qq.com/web/book/read`，如果返回格式正常（如：

```json
{
  "succ": 1,
  "synckey": 564589834
}
```

右键复制为 Curl(Bash) 格式，然后到这里 [Convert curl commands to Python (curlconverter.com)](https://curlconverter.com/python/) 把网络请求相关信息转化为 Python 数据格式，只复制前面的 Header 与 Cookie 字段替换到 `main.py` 即可。对于 `renew`（`https://weread.qq.com/web/login/renewal`）自动更新 Cookie 的接口，可以沿用 `main.py` 中的大部分字段，或者自己抓取，需要一段时间才能抓到更新 cookie 的值（大于一小时）。
