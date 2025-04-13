---
title: "【Super Payload Dumper】现代化多线程Payload.bin解包工具"
aliases: "【Super Payload Dumper】现代化多线程Payload.bin解包工具"
created: 2025-04-09T22:53:31
modified: 2025-04-09T22:53:35
description: "Payload Dumper是什么这是一个由5ec1cff大佬开发的payload.bin多线程解包工具，其项目名称为payload dumper，详细介绍Super Payload Dumper是什么Payload Dumper使用Python编写，通过命令行进行使用，具有支持多线程、从URL解包等现代化的功能，然而并非人人都会部署Python环境，并非人人都能熟练使用命令行，因此我将其编..."
source: "https://optool.daxiaamu.com/super_payload_dumper"
tags:
tags-link:
type: "archive-web"
---

«

[大侠阿木](https://optool.daxiaamu.com/?author=1) 发布于 2024-6-2 05:12 阅读：14609

---

## Payload Dumper 是什么

这是一个由 5ec1cff 大佬开发的 payload.bin 多线程解包工具，其项目名称为 [payload dumper](https://github.com/5ec1cff/payload-dumper)，[详细介绍](https://www.daxiaamu.com/8277/)

## Super Payload Dumper 是什么

Payload Dumper 使用 Python 编写，通过命令行进行使用，具有支持多线程、从 URL 解包等现代化的功能，然而并非人人都会部署 Python 环境，并非人人都能熟练使用命令行，因此我将其编译为 exe 且为其编写了一个外部程序，让你在无需部署 Python、无需使用命令行敲一个命令的情况下，就可以使用它来解包 Payload.bin 文件，我把我这个项目叫做 Super Payload Dumper Py。如果想了解我具体完成的工作，可以到文章末尾查看。

## 直观但不全面的教程

视频教程：[https://www.bilibili.com/video/BV1ZD4y1z7rx/](https://www.bilibili.com/video/BV1ZD4y1z7rx/)

## 全面但不直观的教程

**解包全部分区**

将 rom 文件拖到 unpack.exe 图标上即可解包全部分区到 output 文件夹

**如果要解包单个分区呢？**

> 解包单个分区镜像，程序名就是要解包的分区名

例如：

1. 如果要解包 boot 分区，请将 unpack.exe 重命名为 boot.exe，然后将 rom 文件拖到 boot.exe 图标上。
2. 如果要解包 init\_boot 分区，请将 unpack.exe 重命名为 init\_boot.exe，然后将 rom 文件拖到 boot.exe 图标上。
3. 其他分区同理，你可以将 unpack.exe 复制多份并重命名为不同分区名字以备日常使用。

**如果要直接从 url 解包文件呢？**
双击打开 unpack.exe（或 boot.exe .etc），将全量包的 url 粘贴进去，回车，即可解包全部分区或 boot 分区

## 下载地址

[百度网盘](https://pan.baidu.com/s/1XswMYYzzfAwUvyZDlRGDPA?pwd=dxam#list/path=%2Fsharelink1478247800-193554613237343%2FPublic%2FTool%2FSuper_Payload_Dumper&parentPath=%2Fsharelink1478247800-193554613237343)
提取码：dxam

## Super Payload Dumper Py 中我做了哪些

1. 程序中的 Payload Dumper.exe 为基于原始项目直接打包，未进行改动
2. unpack.exe 由我开发
3. 显然使用 Payload Dumper.exe 解包一个文件需要 3 个参数：待解包文件、要解包的分区、解包到哪个目录，使用时需要命令行中运行并提供这三个参数，但是我通过 unpack.exe 简化了这个操作
- 通过拖动文件到 unpack.exe 的图标上，unpack.exe 可以获取第一个参数：待解包的文件
- 通过双击打开 unpack.exe 后输入 URL 或拖动文件到窗口里，unpack.exe 也可以获取第一个参数：待解包的文件
- 通过读取自身的文件名，unpack.exe 可以获取第二个参数：如果是 unpack.exe，则解包全部分区，否则，文件名是什么，就解包什么分区
- 通过默认设定，程序将解包后的文件放在同目录下的 output 文件夹中
4. 基于以上，用户不需要再手动输入和运行任何命令，只要你会使用鼠标和键盘，就用它解包文件了

## 捐赠

大侠阿木在其中的工作微不足道，如果这个工具对你有用，你可以给 Payload\_Dumper 原作者进行捐赠
[5ec1cff-正在创作 Android 开发](https://ifdian.net/a/5ec1cff)
