---
title: "我在-Windows-下不用-WSL-而使用-MinGW-+-scoop-的一些理由"
created: 2025-03-24T20:55:41
modified: 2025-03-24T20:56:49
source: "https://www.v2ex.com/t/923053"
tags:
tags-link:
type: "archive-web"
---

## Origin Content

主力机是笔记本, 因为 Windows 下 OEM 优化更好 + 个人习惯的问题还在使用 Windows 开发.

但 Windows 下 powershell / cmd 的 cli 体验真的是一言难尽... Linux 下的一套命令行工具就很好用.

目前我使用的方法是先安装 scoop 进行包管理, Windows 下 GUI 和 CLI 的包都可以使用 scoop 管理

然后使用 scoop 安装 git, 会自带 git bash (直接安装 msys2 也行), 就是精简的 MinGW

然后再从 Microsoft Store 装一个 Windows Terminal 并设置 MinGW 作为默认终端, 这样的话就可以在 Terminal 里使用常见的 Linux 命令行工具了, 如果缺什么工具大概率也可以使用 scoop install 安装.

我觉得这套设置对比 WSL 的优势是大部分应用都是移植到原生的 win32 应用, 能和主机共享一套环境. (比如我 IDE 里调用的 python, powershell 里的 python 和 MinGW 里的 python 都是同一个, 版本和包都是一致的.)

虽然 WSL1/2 对 Linux 的模拟更加完整, 但 WSL1 文件访问和其他系统调用性能差, WSL2 占用内存 + 访问 Windows 文件是网络文件系统, 兼容性不好且性能更差. 感觉不如直接使用直接移植到 windows 的这些命令行工具.

(当开发一些依赖 linux kernel 的 C/C++ 程序的时候我会使用 CLion 的 Remote SSH 用服务器开发.)

欢迎大家交流讨论自己的做法~

## Comment

> [!NOTE]
> 我用 WSL 不是为了那些命令，只是为了运行真正的 ELF 可执行文件，然后还要用 Linux 的 syscall 。不少原本只适配 Linux 的方案现在都可以轻松跑起来。
>
> 之前做一些项目特别依赖平台相关的特性，例如监视文件和文件属性变化。这种东西在 Mac 上都会有差异，监视文件变化的地方不一样。一些跨平台库虽然接口统一了，但行为还是有一些区别，导致不同的平台上代码可能会多执行或者少执行。
>
> 以前直接用 Linux 桌面来做开发，桌面谈不上好用，只能凑合用，小毛病挺多的。像投屏到会议平板之类的还全是问题，根本不能用。有了 WSL 之后，几乎同时满足办公协作和开发的需求。我也用过虚拟机和 vagrant 之类的东西搭环境，便利程度不及 WSL 。
>
> 用 msys2 那套的话，我曾经遇到过 sed 的行为不一样的问题，已经太久远了，细节忘了……

> [!NOTE]
> 我选择 MSYS2+zsh
