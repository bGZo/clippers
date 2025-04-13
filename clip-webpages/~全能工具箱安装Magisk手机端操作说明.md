---
title: 全能工具箱安装Magisk手机端操作说明
aliases:
  - 全能工具箱安装Magisk手机端操作说明
created: 2025-04-09T22:48:42
modified: 2025-04-09T22:48:54
description: 请注意 此页面是一加全能工具箱跳转过来的，如果你是主动打开本页面的，请忽略本篇文章内容只有当你通过工具箱完成了刷入Magisk的前序流程，自动跳转到本页面后，你才可以/也应该按本页面所述内容操作 刷面具后手机端操作流程如果你的手机型号不是【一加9R、一加8T】，请看1~3步，如果你的型号是一加9R、8T，请查看下面的【特殊机型操作流程】 手机上打开Magisk APP，提示你修复的话，你点击确...
source: https://optool.daxiaamu.com/magisk_installing
tags: 
tags-link:
  - "[[root]]"
type: archive-web
---

«

[大侠阿木](https://optool.daxiaamu.com/?author=1) 发布于 2024-3-28 05:45 阅读：103277

---

## 请注意

- 此页面是一加全能工具箱跳转过来的，如果你是主动打开本页面的，请忽略本篇文章内容
- 只有当你通过工具箱完成了刷入 Magisk 的前序流程，自动跳转到本页面后，你才可以/也应该按本页面所述内容操作

## 刷面具后手机端操作流程

如果你的手机型号不是【一加 9R、一加 8T】，请看 1~3 步，如果你的型号是一加 9R、8T，请查看下面的【特殊机型操作流程】

1. 手机上打开 Magisk APP，提示你修复的话，你点击确定即可

> 如果没有提示，则无需操作。如果看到提示不小心点了取消，则可以关闭 Magisk 进程并重新打开

[![](https://optool.daxiaamu.com/content/uploadfile/202403/thum-45ba1711578278.jpg)](https://optool.daxiaamu.com/content/uploadfile/202403/45ba1711578278.jpg)

2. 等手机重启后，至此，已经安装完 Magisk。通常你还需要安装 Shamiko 和 LSPosed，请继续往下看（如果不需要 Shamiko 和 LSPosed，就可以关闭本页面了）
3. 下载 [【一加全能盒子APP】](https://optool.daxiaamu.com/wiki_optool) 并安装到手机上
4. 打开全能盒子 APP，它会自动申请 ROOT 权限，请点允许。
5. 全能盒子功能菜单中找到“安装 Shamiko”并运行它，直至安装完成
6. 按照 [这个视频](https://www.bilibili.com/video/BV19w411t7YP/) 第 4 分 39 秒的内容开始操作，直到视频结束

> 视频先拍，本教程后出，本教程有效力覆盖视频教程，因此请忽略 4 分 39 秒之前的内容

7. 至此已经安装完 Magisk、Shamiko 以及 LSPosed，其中 shamiko 教程在这里：[https://www.daxiaamu.com/6465/](https://www.daxiaamu.com/6465/)

## 特殊机型刷面具后手机端操作流程

### 一加 8T、一加 9R 刷面具后手机端操作流程

> 因为 Magisk 的 bug，一加 9R 和 8T 无法使用高于 26.1 版本的面具（否则就会变砖）。即：一加 8T 和 9R 最高可用的面具版本是 26.1。
> 全能工具箱的菜单 3，在 8T 和 9R 的 ROOT 流程中，刷入的面具版本就是 26.1 的。
> 而在全能盒子 APP 10.1 及以前版本中，一直提供的是 26.1 版本的 Magisk，
> 旧版本的 Magisk 不兼容更高版本的 Shamiko，因此全能盒子提供的 Shamiko 是 0.7.3 版本的
> 是的，大家如果严格按照工具箱和全能盒子的流程来，你装的 Magisk 和 Shamiko 版本都是旧的
> 旧的 Magisk+ 旧的 Shamiko，意味着隐藏 ROOT 能力减弱，这极大地不方便大家使用
> 因此全能盒子 APP 不能再为了照顾 8T 和 9R 这两个旧机型，一直为大家提供旧版本的 Magisk 和 Shamiko 了
> 但是如果直接提供最新的 Magisk 和 Shamiko，大家按照原来的提示操作，又会导致一加 8T 或一加 9R 变砖，这是绝对不能发生的事情
> 于是在工具箱 ROOT 流程的结尾，引入了这个页面，为一加 8T 和 9R 提供单独的引导。现在你可以按下面的步骤操作

1. 手机上打开 Magisk APP，提示你修复的话，你点击确定即可
[![](https://optool.daxiaamu.com/content/uploadfile/202403/thum-45ba1711578278.jpg)](https://optool.daxiaamu.com/content/uploadfile/202403/45ba1711578278.jpg)
2. 重启手机后，打开 Magisk APP，进入设置，关闭【检查更新】，这一步是为了防止你将来忘记上面的提醒而不小心升级面具
[![](https://optool.daxiaamu.com/content/uploadfile/202403/thum-17b41711578352.jpg)](https://optool.daxiaamu.com/content/uploadfile/202403/17b41711578352.jpg)
3. 截止到这里，你已经安装好了 Magisk，通常你还需要安装 Shamiko 和 LSPosed，请继续往下看（如果不需要 Shamiko 和 LSPosed，就可以关闭本页面了）
4. 下载 [Shamiko 0.7.3](https://yun.daxiaamu.com/files/Magisk%E6%A8%A1%E5%9D%97/shamiko/)，以及 [LSPosed Zygisk版本](https://yun.daxiaamu.com/files/Magisk%E6%A8%A1%E5%9D%97/lsposed/) 到手机上
5. 打开 Magisk APP，点击底部第 4 个 tab，然后点击【从本地安装】功能，安装上面下载的两个模块，然后重启手机
[![](https://optool.daxiaamu.com/content/uploadfile/202403/thum-ef081711578471.jpg)](https://optool.daxiaamu.com/content/uploadfile/202403/ef081711578471.jpg)
6. 开机后下拉状态栏创建 LSPosed 快捷方式即可：1）如果桌面已经有 LSPosed 快捷方式，则下拉状态栏没有提示。2）如果下拉状态栏和桌面上都没有 LSPosed 快捷方式，你也可以拨号键盘输入 *#*#5776733#*#* 来手动进入 LSPosed，再进入其设置，如下图所示，手动创建快捷方式
[![](https://optool.daxiaamu.com/content/uploadfile/202403/thum-27a71711578653.jpg)](https://optool.daxiaamu.com/content/uploadfile/202403/27a71711578653.jpg)
7. 请你记住，不要升级 Magisk 到更高的版本，请让其保持低于等于 26.1 版本
8. 至此已经为你的一加 8T 或一加 9R 安装完 Magisk、Shamiko 以及 LSPosed，其中 shamiko 教程在这里：[https://www.daxiaamu.com/6465/](https://www.daxiaamu.com/6465/)

> 既然一加 9R 和一加 8T 和只能用旧的 Magisk+ 旧的 Shamiko（原因在上面说过），隐藏 ROOT 能力较弱，因此诚恳建议更换 [APatch](https://www.daxiaamu.com/8169/) 或 [KernelSU](https://www.daxiaamu.com/8236/)

## 如何在升级系统后保留 ROOT 权限（Magisk 仍然是安装状态）

1. [大侠阿木1分钟教你ColorOS 13、ColorOS 14如何保留Root升级系统版本](https://www.daxiaamu.com/7263/)
2. 如果你的系统是【单槽分区：A-only】的设备，比如【搭载 ColorOS 的一加 9R】，则无法升级保留 ROOT 权限，你只能升级系统后重新刷 Magisk。
3. 如果你是一加 ACE 2V，则无法升级保留 ROOT 权限，你只能升级系统后重新刷 Magisk。

## 其他资料

- [《ROOT后可以做什么》](https://optool.daxiaamu.com/ROOT%E5%90%8E%E5%8F%AF%E4%BB%A5%E5%81%9A%E4%BB%80%E4%B9%88)
- 加入 [【QQ频道：一加全能江湖】](https://optool.daxiaamu.com/join_group)，获取最新一加资讯、ROM 更新、和大家讨论刷机玩机技巧
