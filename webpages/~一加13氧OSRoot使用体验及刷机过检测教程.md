---
title: 一加-13-氧-OS-Root-使用体验-及-刷机过检测教程
created: 2025-03-24T20:37:39
modified: 2025-03-24T20:40:02
source: https://www.v2ex.com/t/1115757#reply43
tags: 
tags-link: 
type: archive-web
---

## 配置

一加 13 24G+1T pdd 国补 4500 入手

## 使用体验

- 买之前妹人和我说 OPPO 系推送这么拉啊...
- 好像可以刷入❀为推送，我没搞。
- QQ 必须锁定 + 后台行为无限制 才能即时收到通知，否则会延迟 5 分钟左右
- 微信 等有 Play Store 版本的优先使用，FCM 推送稳定，且无需锁后台

## Root 前须知

- 刷机有风险，Root 需谨慎。
- 不建议用一键包，本身 Root 就失去了很多安全性，用别人的脚本更危险。
- 目前 氧 OS 无法回锁，因为需要安装模块才能修复信号问题。但可以 OTA 更新并保留 Root 。

## Root 方案效果及问题

- MagiskAlpha + Zygisk Next + Shamiko + PlayIntegrityFix + Tricky Store + 隐藏应用列表
- 问题：微众无法使用指纹解锁，可以手势解锁。BOCHK 指纹失效，只能密码登录。
- 最终效果：除了上面提到的两位，其他国内外银行和币圈交易所类 App 都能正常运行。

## 氧 OS 刷机

刷机教程： [https://xdaforums.com/t/pjz110-1-3-coloros-to-oxygenos-stable-eu-glo-test-601-eu-glo-na-405-in-602.4707431/](https://xdaforums.com/t/pjz110-1-3-coloros-to-oxygenos-stable-eu-glo-test-601-eu-glo-na-405-in-602.4707431/)

个人整理的夸克盘： [https://pan.quark.cn/s/0c4f320786c8](https://pan.quark.cn/s/0c4f320786c8)

备注：

- 先安装 1 电脑驱动 内的三个驱动
- 解压 2 刷机包 后，进入里面的 Platform-Tools 文件夹，在空白位置 shift+ 右键菜单 - 在终端中打开（不要选 powershell ，路径不对，会更正的请无视）
- 准备过程结束
- 跟着英文教程刷机。其中，adb fastboot 等命令，要加 “.exe”，比如："adb devices" 要用 "adb.exe devices"
- 我已经在夸克盘准备好了 MagiskAlpha.apk 和补丁过的 init\_boot.img ，跟着教程做的时候，安装完 Magisk ，可以跳过自己打补丁这一步，使用命令进入 bootloader 刷入补丁好的 init\_boot.img 。

## 刷入 Magisk 模块和安装 app

.zip 的都是在 Magisk- 模块 内刷入，刷入完不需要立即重启，返回继续刷入。app 就正常安装。

- 00 安装 LocalSend 酷安 Clash Droid-ify 等
- 01 [ZygiskNext.zip](https://github.com/Dr-TSNG/ZygiskNext/releases)
- 02 LSPosed-v1.10.1-7115-zygisk-release.zip
- 03 fix-signal-oneplus13v2.zip
- 04 打开 Magisk ，右上角设置内点一下 Systemless hosts 。ksu 系需要刷 systemless-hosts-KernelSU-module.zip
- 05 systemless-fcm-hosts.zip
- 06 重启
- 07 zygisk-ThanoxPro.zip （安装 ThanoxPro 后在 app 设置最下面点补丁即可导出，不装 ThanoxPro 的跳过这一步。ThanoxPro 也可以用 LSP 模块运行，这里不启用）
- 08 PlayIntegrityFix\_v18.6.zip
- 09 Shamiko-v1.2.1-383-release.zip
- 10 使用 酷安 装 爱玩机工具箱，打开爱玩机，全勾选启动，添加附加模块 + 音量救砖 & 进入 - 导航 -Magisk 专区 - 启用 Shamiko 白名单
- 11 Tricky-Store-v1.2.1-158-51390a7-release.zip
- 12 zygisk-module-xfingerprint-pay-all-v5.2.0-release.zip
- 13 BCR-1.77-release.zip & BCR.apk
- 14 重启
- 15 用酷安装 MT 管理器，打开 爱玩机工具箱 - 导航 - 应用管理，找到 MT 管理器 点击唤醒 Root 权限 按钮。
- 16 使用 MT 管理器 运行 "trickystore [一键添加包名.sh](http://xn--4gqq6ixig9ah97fjf3c.sh/)"，执行前要点击 - 设置 - 使用 Root 权限运行√，进去后输入 n & 回车 & 回车 就结束了。

## LSP 模块

LSP 模块安装后需要手动启用，一般会自行选择好作用域，直接启用即可。 LSP 找不到的话，通过拨号调出，代码： `*#*#5776733#*#*`

- 17 安装 Fcmfix.apk ，模块作用域额外勾选 Google 框架 & play 商店 & play 服务。之后进入该 app ，等应用加载后，点击右上角 - 全选包含 fcm 的应用 即可。以后你安装完新 app 也需这里点一下全选。
- 18 LSP 内仓库搜索安装 Luckytool 。用来修改 coloros 的，氧 os 依旧有用。打开 爱玩机工具箱 - 导航 - 应用管理，找到该 app ，点击唤醒 Root 权限。
- 19 安装 HMA.apk （又叫 HideMyApplist 隐藏应用列表），用来过检测的。打开 爱玩机工具箱 - 导航 - 应用管理，找到该 app ，点击唤醒 Root 权限。
- 20 重启

## 配置 HMA （又叫 HideMyApplist 隐藏应用列表）

- 21 打开 HMA ，模板管理 - 创建黑名单模板，模板名称随意，应用不可见 - 编辑列表。要把不想被目标 app 检测到的都勾上，我截图了自己的供参考。
- 22 返回 HMA 主页 - 应用管理，以 HSBC HK 为例，搜索进入 - 启动隐藏 - 已启用模板 - 勾选上面配置过的黑名单 - 返回，最后杀掉重开 HSBC HK 即可

## 其他我常用的 app

- Adaway ashell-you shizuku SwiftBackup GKD
- 安装后打开 爱玩机工具箱 - 导航 - 应用管理，找到上面这些 app ，点击唤醒 Root 权限
