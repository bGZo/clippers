---
title: "一加全能工具箱一键刷KernelSU-Next教程"
aliases: "一加全能工具箱一键刷KernelSU-Next教程"
created: 2025-04-09T22:52:57
modified: 2025-04-09T22:52:57
description: "KernelSU是什么 KernelSU是一种比Magisk更新的ROOT方式他有两种安装模式，一种是GKI、一种是LKM，本文所述方法基于LKMKernelsu官网本文所述的KernelSU-Next是KernelSU的一个分支，相比原项目，KernelSU-Next主要是支持非GKI，即更低的内核版本（4.4~），当然也有更多其他的特性。其项目地址：https://rifsxd.gith..."
source: "https://optool.daxiaamu.com/install_kernelsu-next"
tags:
tags-link:
type: "archive-web"
---
«

[大侠阿木](https://optool.daxiaamu.com/?author=1) 发布于 2025-1-12 05:45 阅读：7234

---

## KernelSU是什么

1. KernelSU是一种比Magisk更新的ROOT方式
2. 他有两种安装模式，一种是GKI、一种是LKM，本文所述方法基于LKM
3. [Kernelsu官网](https://kernelsu.org/)
4. 本文所述的KernelSU-Next是KernelSU的一个分支，相比原项目，KernelSU-Next主要是支持非GKI，即更低的内核版本（4.4~），当然也有更多其他的特性。其项目地址：[https://rifsxd.github.io/KernelSU-Next/](https://rifsxd.github.io/KernelSU-Next/)

## 如何刷入KernelSU-Next

1. 准备工作：请确认你已经完成以下准备工作
- 请确认你的手机已经解锁bootloader。如果没有解锁bootloader，请通过全能工具箱或其他方法进行解锁bootloader。
- 如果你其他ROOT（比如面具Magisk、KernelSU等），请先卸载或覆盖全量包。
- 手机能正常连接电脑，打开USB调试，手机上，与电脑的连接模式选传输文件（MTP）。
2. 下载[全能工具箱](https://optool.daxiaamu.com/wiki_pctool)到电脑上
3. 双击打开工具箱，输入P
4. 提示你选择ROOT方式，如果需要KernelSU-Next，那我们就输入6
5. 按提示拖入下载好的刷机包，并回车  
![](http://www.daxiaamu.com/wp-content/uploads/2024/03/Snipaste_2024-03-25_05-51-59-801x1024.png)
6. 等待工具箱完成后续操作并弹出一个网页，然后你按照网页上的引导继续操作即可（即：[这个页面](https://optool.daxiaamu.com/kernelsu-next_installing)）。

↓↓↓以下是关于Kernelsu的一些用法↓↓↓

## KernelSU-next如何隐藏ROOT权限

截止到这一步，无需任何额外设置和操作，就是做好隐藏环境的。你可以正常使用所有对ROOT权限敏感的软件

## 如何在升级系统时保留KernelSU而无需重新安装

> 不支持升级保留ROOT的情况：一加ACE 2V  
> 请检查确认手机当前所装模块适用于你升级后的系统版本，如果有模块不支持升级后的系统，请关掉或删除或卸载之  
> 请确保你收到的是【系统更新】而不是【软件更新】，最简单的判断方法就是，如果你收到的更新是若干个G大小的，则是系统更新。而一般几百M的都不是系统更新

1. 正常安装系统，只剩下最后一步（比如比如ColorOS 13和14系统最后一步是【立即安装】，ColorOS 14后期和ColorOS 15的最后一步是【立即重启】，不同的系统，按钮名字可能不一样），停下来不要操作了

> 如果点它就重启了，则表示这是【最后一步】，请不要操作这个【最后一步】

[![](https://optool.daxiaamu.com/content/uploadfile/202403/thum-62161711730360.jpg)](https://optool.daxiaamu.com/content/uploadfile/202403/62161711730360.jpg)

2. 切到KernelSU APP，点击顶部区域  
[![](https://optool.daxiaamu.com/content/uploadfile/202403/thum-a77a1711730395.jpg)](https://optool.daxiaamu.com/content/uploadfile/202403/a77a1711730395.jpg)
3. 点击如图所示选项

> 如果你看不到这个选项，说明当前机型和系统不支持这么做，你应该正常升级系统后重新刷KernelSU

[![](https://optool.daxiaamu.com/content/uploadfile/202403/thum-90c31711730496.jpg)](https://optool.daxiaamu.com/content/uploadfile/202403/90c31711730496.jpg)

4. 点确定，等它操作完成（注意，先不要点【重启】按钮）  
[![](https://optool.daxiaamu.com/content/uploadfile/202403/thum-c6821711730526.jpg)](https://optool.daxiaamu.com/content/uploadfile/202403/c6821711730526.jpg)

[![](https://optool.daxiaamu.com/content/uploadfile/202403/thum-72311711730550.jpg)](https://optool.daxiaamu.com/content/uploadfile/202403/72311711730550.jpg)

5. 如果你是ColorOS，请回到安装系统界面，去完成【最后一步】即可（比如ColorOS 13和14上面就是叫【立即安装】），等待重启开机即可。如果不是ColorOS，建议也这么操作。
6. 等待开机后，就完成了升级，且现在KernelSU仍然是安装状态。

## 其他资料

- [《ROOT后可以做什么》](https://optool.daxiaamu.com/whattodowithroot)
- 加入[【QQ频道：一加全能江湖】](https://optool.daxiaamu.com/join_group)，获取最新一加资讯、ROM更新、和大家讨论刷机玩机技巧
- 如果KernelSU-Next对你有用，可以给作者捐赠，但是也强烈建议给KernelSU作者进行捐赠，这是KernelSU-Next存在的基石。KernelSU捐赠连接：[https://vxposed.com/donate.html](https://vxposed.com/donate.html) 、 [https://www.patreon.com/weishu](https://www.patreon.com/weishu)