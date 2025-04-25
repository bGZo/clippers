---
title: SideStore-安装指南-如何在-iOSiPadOS-设备上侧载应用
created: 2025-04-18T21:17:31
modified: 2025-04-25T20:21:04
description: 借助SideStore实现脱离电脑连接的侧载应用安装体验，体验双微信、旧版应用复活的快感。
source: https://fylsen.com/posts/2024/05/sidestore-install-guide-ios-ipados-sideload-apps/
tags: 
tags-link: 
type: archive-web
---

## SideStore 安装指南：如何在 iOS/iPadOS 设备上侧载应用

这篇文章最后修改于 24 年 5 月 30 日 星期四，部分内容可能已经不适用，如有疑问可联系作者。

SideStore 是一款可在 iOS 和 iPadOS 设备上侧载应用的商店。侧载应用是指通过非官方渠道安装应用程序到设备上的过程，脱离苹果的官方应用商店 App Store 实现。SideStore 属于开发者模式和第三方应用商店的结合，使用虚假的开发者模式，不需要越狱。

要安装 SideStore，需要满足一些基本条件，包括运行 macOS 10.15 以上版本的 Mac 或者 Windows 10 以上版本、一个 Apple ID 账号和一台运行在 iOS 14、iPadOS 14 以上版本系统的 iPhone 或者 iPad 设备。在电脑中下载基础软件，包括 AltServer、SideStore.ipa 和 JitterbugPair。

安装步骤包括在电脑中下载并安装 AltServer，在移动设备中安装 SideStore，配对文件，并设置 WireGuard VPN。在 SideStore 中登录 Apple ID，可以通过 Refresh All 刷新应用的使用时长。SideStore 支持自部署的 Anisette 服务，可以通过设置 Anisette URL 来完成。

模型: @cf/meta/llama-4-scout-17b-16e-instruct

最近发现了可以在 iOS 中直接安装使用的侧载商店 [SideStore](https://sidestore.io/)，安装的应用可以使用 7 天（可通过刷新延长使用），具体介绍可以直接阅读官方文档（[SideStore Docs](https://docs.sidestore.io/docs/intro)）。

“侧载应用”（Sideloading）是指通过非官方渠道安装应用程序到设备上的过程，脱离苹果的官方应用商店 —— App Store 实现。侧载应用可以通过多种方式实现，包括但不限于：

1. **开发者模式**：iOS 设备可以通过 Xcode 来安装应用程序，开发者可以将未上架到 App Store 的应用程序安装到自己的设备上进行测试。
2. **企业签名**：一些企业会通过苹果的企业开发者计划（Apple Developer Enterprise Program）分发内部应用程序，这些应用程序并不需要通过 App Store 进行分发。
3. **第三方应用商店**：通过一些非官方的应用商店或者工具（例如 Cydia，对于越狱设备）来安装应用程序。
4. **TestFlight**：这是苹果官方提供的一种测试应用分发工具，开发者可以通过 TestFlight 邀请用户测试应用，但这并不完全算作侧载，因为它仍然是通过苹果的官方渠道进行控制和分发的。

本次尝试的 SideStore 应该是属于 1、3 结合的形式，使用了虚假的开发者模式，同时又不进行越狱。 ⠀ **侧载的优缺点：**

| 优点 | 缺点 |
| --- | --- |
| **灵活性**：能够安装未通过 App Store 审核的应用程序。   **测试**：开发者可以在个人设备上测试应用程序而无需上架到 App Store。   **内部应用分发**：企业可以将特定应用程序分发给内部员工使用。 | **安全风险**：侧载的应用程序没有经过苹果的安全审查，可能存在恶意代码或安全漏洞。   **稳定性**：未经过 App Store 审核的应用程序可能不稳定，容易崩溃。 |

欧盟通过《数字市场法》要求苹果等公司开放侧载应用，基本上可以确定侧载将会是逐步完善的一个 iOS、iPadOS 应用分发市场。

## 安装步骤
### 基础条件

- 运行 macOS 10.15 以上版本的 Mac 或者 Windows 10 以上版本
- 一个 Apple ID 账号
- 一台 运行在 iOS 14、 iPadOS 14 以上版本系统的 iPhone 或者 iPad 设备

### 一、 电脑中下载基础软件

**下载 AltServer**

[Mac 版 AltServer](https://cdn.altstore.io/file/altstore/altserver.zip) [https://cdn.altstore.io/file/altstore/altserver.zip](https://cdn.altstore.io/file/altstore/altserver.zip)

[Window 版 AltServer](https://cdn.altstore.io/file/altstore/altinstaller.zip) [https://cdn.altstore.io/file/altstore/altinstaller.zip](https://cdn.altstore.io/file/altstore/altinstaller.zip)

**下载 SideStore.ipa**

[SideStore](https://github.com/sidestore/sidestore/releases/latest/download/sidestore.ipa) [https://github.com/sidestore/sidestore/releases/latest/download/sidestore.ipa](https://github.com/sidestore/sidestore/releases/latest/download/sidestore.ipa)

**下载 JitterbugPair**

[Mac 版 jitterbugPair](https://github.com/osy/Jitterbug/releases/download/v1.3.1/jitterbugpair-macos.zip) [https://github.com/osy/Jitterbug/releases/download/v1.3.1/jitterbugpair-macos.zip](https://github.com/osy/Jitterbug/releases/download/v1.3.1/jitterbugpair-macos.zip)

[jitterbugpair-win64](https://github.com/osy/Jitterbug/releases/download/v1.3.1/jitterbugpair-win64.zip) [https://github.com/osy/Jitterbug/releases/download/v1.3.1/jitterbugpair-win64.zip](https://github.com/osy/Jitterbug/releases/download/v1.3.1/jitterbugpair-win64.zip)

### 二、移动设备中安装侧载商店 SideStore

1. 使用数据线连接 iPhone（iPad）与电脑，信任设备。
2. 解压之前下载的 AltServer，并直接运行，在状态栏中可以看到一个菱形的图标。

![AltServer](https://file.fylsen.com/images/2024/05/00d68b6feb7cc4c3b42d19630b32484fec146595bfa1e03927320fe6851b6fc9.jpg)

3. 键盘上按住 option 或 Shift 键后点击 AltServer 的图标，之后选择 `SideStore .ipa` ，并在本地目录中找到之前下载的 SideStore，按提示输入 Apple ID 等信息后等待移动设备上安装完成。
4. 在移动设备的 `设置 > 通用 > VPN与设备管理` 可以看到与之前输入的 Apple ID 相关的开发者 APP，完成信任确认操作。
5. iOS/iPadOS 16 以上系统还需要在 `设置 > 隐私与安全性 > 开发者模式` 中开启 `开发者模式`，并按照系统提示完成后续操作。

### 三、配对文件

1. 解压之前的下载好的 JitterbugPair。
2. 保持移动设备与电脑的数据线连接，解锁移动设备（需要已设置锁屏密码）到主屏幕。
3. 双击 `jitterbugpair 或 jitterbugpair.exe`，按提示操作并等待完成。

![JitterbugPair](https://file.fylsen.com/images/2024/05/b2d671402f2e42c36c360bec0d4640726b1bf5730cff11d53c3c5f9b3651d845.jpg)

4. 之后会得到类似 `00008101-001E78C10202001E.mobiledevicepairing` 这样的文件，Windows 在本目录下，Mac 在用户主目录下。

![配对文件](https://file.fylsen.com/images/2024/05/ebfba1d3cbf7b7f0113cc28f5caf6e3e0b9f9939e5c1b0379547d042ca689811.jpg)

5. 通过隔空投送或者微信将配对文件上传到移动设备中，并保存在 `文件` 中。
6. 点击手机中安装好的 `SideStore`，按提示选择上传的配对文件。

### 四、设置 WireGuard VPN

1. 移动端 App Store 中下载并安装 WireGuard。
2. 在 Safair 中下载配置文件 [WireGuard Config File](https://github.com/sidestore/sidestore/releases/download/0.1.1/sidestore.conf)
3. 在 WireGuard 中右上角 “+” 导入配置或压缩包，选择刚下载好的文件。

![WireGuard 配置](https://file.fylsen.com/images/2024/05/a2e789b45abe56b9c749c6495a40b0a3407553b86563bf0eaf1f63891a5bc59c.jpg)

### 五、SideStore 刷新应用

1. 在 SideStore 中登录之前使用的 Apple ID。
2. 在 “My Apps”中可以通过 Refresh All 刷新应用的使用时长，只要每七天执行一次就行。
3. 正常使用侧载的 App 时，不需要开启 WireGuard VPN，只在需要刷新或者安装新应用时开启。（⚠️ 要在连接 Wi-Fi 场景下进行）

### Anisette 自部署

如果对于安全性有要求，SideStore 支持自部署的 Anisette 服务，可以通过 `设置 - SideStore - Anisette URL` 设置。

![配置自部署Anisette](https://file.fylsen.com/images/2024/06/f55b1caad70c818e31489a949ae6a81e0f0de107dc60efb2284131ed6ca3f218.jpg)

可以通过 [Anisette-V3](https://github.com/Dadoum/anisette-v3-server) 的 Docker 方式完成部署。

shell

```
docker run -d --restart always --name anisette-v3 -p 6969:6969 --volume anisette-v3_data:/home/Alcoholic/.config/anisette-v3/lib/ dadoum/anisette-v3-server
```

## 体验

相较于官方的 App Store，虽然满足了一些特殊场景下的使用需求，但是缺点还是很明显的。

1. 安装 App 的速度有些不尽人意，很缓慢。
2. 需要记住刷新的时间不能超过 7 天，否则还要通过电脑重新来过。
3. IPA 的安全性还是需要斟酌再三。
4. 如果切换了 Anisette 服务就会出现了“验证”失效的问题，需要重新进行签名。

![验证失效](https://file.fylsen.com/images/2024/05/b8f9da906ccc0fdfe7eaa4f681720095075926a26d2a042c70c812d78d085758.jpg)

当然既然使用侧载，一定是存在一些优点。

1. 类似多个微信的使用需求是可以满足的，家庭、工作隔离开来应该是很多人的实际需求。
2. 直接在手机端就能完成 IPA 的安装，无需借助电脑，方便不少。
3. 从 App Store 中下架的应用，可以再次复活。

## 参考

- [SideStore](https://sidestore.io/)
- [Anisette-V3](https://github.com/Dadoum/anisette-v3-server)
- [Jitterbug](https://github.com/osy/Jitterbug)
- [WireGuard](https://www.wireguard.com/)
- [iPA Library(iPA 安全性自评)](https://ipalibrary.me/)

文章标题：SideStore 安装指南：如何在 iOS/iPadOS 设备上侧载应用

文章作者：Cedar

文章链接：https://fylsen.com/posts/2024/05/sidestore-install-guide-ios-ipados-sideload-apps\[复制\]

最后修改时间：

---

商业转载请联系站长获得授权，非商业转载请注明本文出处及文章链接，您可以自由地在任何媒体以任何形式复制和分发作品，也可以修改和创作，但是分发衍生作品时必须采用相同的许可协议。
本文遵循 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh) 许可协议。
