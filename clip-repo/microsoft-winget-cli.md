---
title: microsoft/winget-cli
aliases: winget-cli
created: 2025-04-04T11:00:05
modified: 2025-04-04T11:00:05
description: WinGet is the Windows Package Manager. This project includes a CLI (Command Line Interface), PowerShell modules, and a COM (Component Object Model) API (Application Programming Interface).
source: https://github.com/microsoft/winget-cli
tags:
  - star
tags-link: 
type: repo
---
## Repo Meta

![](https://img.shields.io/github/stars/microsoft/winget-cli?style=for-the-badge&label=stars) ![](https://img.shields.io/github/repo-size/microsoft/winget-cli?style=for-the-badge&label=size) ![](https://img.shields.io/github/created-at/microsoft/winget-cli?style=for-the-badge&label=since)

[![](https://github-readme-stats.vercel.app/api/pin/?username=microsoft&repo=winget-cli&bg_color=00000000)](https://github.com/microsoft/winget-cli)

## Notes

aliases: Windows package manager cli
tags: #Windows #tools, #scoop
source: https://github.com/microsoft/winget-cli
released-created: 2020-05-14
created: 2023-05-12
![](https://img.shields.io/github/stars/microsoft/winget-cli)

>[!warning]
  > winget cannot switch multi versions of app[^version]
## Consists
  - 仓库：[GitHub - microsoft/winget-pkgs: The Microsoft community Windows Package Manager manifest repository](https://github.com/microsoft/winget-pkgs)
  - 客户端：[GitHub - microsoft/winget-cli: Windows Package Manager CLI (aka winget)](https://github.com/microsoft/winget-cli)
    - [Releases · microsoft/winget-cli · GitHub](https://github.com/microsoft/winget-cli/releases)
## References
[^version]: 就算是允许多版本安装 Python，也都是安装在 `$LOCALAPPDATA\Programs\Python\PythonXX` 下，但是本身的环境变量没有办法方便的修改(via： [Can winget install an older version of Python? - Stack Overflow](https://stackoverflow.com/questions/70281103/can-winget-install-an-older-version-of-python))，所以相当鸡肋。只适用于
    - 微软已登录用户？
      - Github 安装的版本可以绕过这个限制吗？
    - 一些没有被墙的源（如 winget 源的 Google.PlatformTools，碍于无法使用代理，并且需要从 Google 官方那里拉取软件，所以基本已报错收尾）
      id: 645f8f88-c973-44da-8e08-41f71bd3e2d2
```
        An unexpected error occurred while executing the command:
        InternetOpenUrl() failed.
        0x80072efd : unknown error
        NativeCommandExitException: Program "winget.exe" ended with non-zero exit code: -2147012867.
```
    - 专门为 Windows 做了优化的（比如calibre、telegram等，这些特性可能便携版天然就做不到），也已说是便携版（scoop）用着不爽的。
-