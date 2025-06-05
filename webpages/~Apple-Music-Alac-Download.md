---
created: 2025-05-29T20:01:52
modified: 2025-05-29T20:01:58
description: "Apple Music Alac高解析度无损音乐下载教程(2025/1/16)文章最后编辑时间交流群 https://t.me/apple_music_alac原理来自github项目 https://github.com/alacleaker/apple-music-alac-downloader本文为Windows教程其他教程 https://applemusic.mintlify.app/1、安装配置MUMU模拟器#1下载MUMU模拟器安装包https://github.com/itouakirai/apple-music-jshook-script/releases/download/wsa/MuMuInstaller_3.1.13.0.exe#2 下载MUMU模拟器备份还原包https://github.com/itouakirai/apple-music-jshook-script/releases/download/wsa/amdl.mumudata#3 安装MUMU模拟器并运行MUMU多开器12，新建-->导入并新建-->选择还原包2、正式使用#1 运行模拟器中的Ap…"
source: "https://telegra.ph/Apple-Music-Alac%E9%AB%98%E8%A7%A3%E6%9E%90%E5%BA%A6%E6%97%A0%E6%8D%9F%E9%9F%B3%E4%B9%90%E4%B8%8B%E8%BD%BD%E6%95%99%E7%A8%8B-04-02-2"
tags:
tags-link:
type: "archive-web"
---

## Apple Music Alac Download

### Apple Music Alac 高解析度无损音乐下载教程

(2025/1/16) 文章最后编辑时间

交流群 [https://t.me/apple\_music\_alac](https://t.me/apple_music_alac)

原理来自 github 项目 [https://github.com/alacleaker/apple-music-alac-downloader](https://github.com/alacleaker/apple-music-alac-downloader)

本文为 Windows 教程

其他教程 [https://applemusic.mintlify.app/](https://applemusic.mintlify.app/)

#### 1、安装配置 MUMU 模拟器

*#1 下载 MUMU 模拟器安装包*

[https://github.com/itouakirai/apple-music-jshook-script/releases/download/wsa/MuMuInstaller\_3.1.13.0.exe](https://github.com/itouakirai/apple-music-jshook-script/releases/download/wsa/MuMuInstaller_3.1.13.0.exe)

#2 下载 MUMU 模拟器备份还原包

[https://github.com/itouakirai/apple-music-jshook-script/releases/download/wsa/amdl.mumudata](https://github.com/itouakirai/apple-music-jshook-script/releases/download/wsa/amdl.mumudata)

#3 安装 MUMU 模拟器并运行 MUMU 多开器 12，新建 -->导入并新建 -->选择还原包

#### 2、正式使用

#1 运行模拟器中的 AppleMusic 应用（需要确保已登录有订阅的账号并在后台持续运行）

#2 再运行 ZeroTermux 开始下载

> **使用下载命令**

1、只下载专辑中指定的几首歌，使用时输入要下载的曲目数字，多个时用空格隔开

go run main.go --select 专辑链接

2、下载整个专辑歌曲、播放列表、艺术家

go run main.go 专辑链接/播放列表链接/艺术家链接

播放列表下载示例

```
go run main.go https://music.apple.com/cn/playlist/hi-res-lossless-24-bit-192khz/pl.u-MDAWvpjt38370N
```

3、下载杜比全景声

go run main.go --atmos 杜比专辑链接

杜比下载示例

```
go run main.go --atmos https://music.apple.com/cn/album/1989-taylors-version-deluxe/1713845538
```

### 3、进阶操作

> **获取歌词及 aac-lc**

如果你要下载歌词和 aac-lc 则需要获取 media-user-token 并将其填入下载项目文件夹下 config.yaml 内对应的值

*#如何获取 media-user-token*

打开桌面端网页浏览器使用有订阅的账号**登录**[网页版Apple Music](https://music.apple.com/),在主页按下 F12 打开开发者工具，

依次点击 Application -> Storage -> Cookies -> [https://music.apple.com](https://music.apple.com/)

![](https://telegra.ph/file/4911920b7ddf941dd5f66.png)

图中选中的值就是 media-user-token

#填入配置文件中

zerotermux 中从右侧屏幕边缘向左滑动即可打开文件管理器，

依次点击 home -> amdl -> config.yaml 即可编辑，再替换第一个选项的值，保存

> 更新下载项目

双击 zerotermux 屏幕，运行对应快捷指令即可

每次更新都需要重新修改 config.yaml 内的值，确保文件下载到 mumu 的映射文件夹下

alac-save-folder: /sdcard/$MuMu12Shared/AM-DL

atmos-save-folder: /sdcard/$MuMu12Shared/AM-DL-Atmos
