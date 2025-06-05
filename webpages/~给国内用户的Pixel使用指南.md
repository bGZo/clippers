---
created: 2024-08-05T12:00:00
source: https://www.coolapk.com/feed/57502239?shareKey=NWRiYTJkZWM3MDVhNjZiMGViNDA~
type: archive-web
modified: 2025-01-15T11:38:20
---

注：本文原作者为少数派用户“克莱德”，本文著作权归属于原始作者“克莱德”所有，经许可使用。

原作者文章传送门：[查看链接](https://sspai.com/post/78200) 一个比较残忍的现实是：因为近几年 Google 越来越喜欢将平台特性打包进 Google 服务进行分发，在没有 Google 服务或没有完整 Google 服务的 Android 设备上，想要体验照片选择器、快速分享等特性，感受完整、纯粹的 Android 体验，通过诸如亚马逊海外淘这样的渠道获取一台 Google Pixel 设备是为数不多的选择之一。 种草预警：

[查看链接](https://sspai.com/post/75272)（8000 字详解 Android 13 正式版的 9 个变化）

[查看链接](https://sspai.com/prime/story/inspecting-imported-used-pixel) （以 Pixel 为例谈二手 Android 水货验机）

[查看链接](https://sspai.com/post/75385)（银河系 Google Pixel 漫游指南）

[查看链接](https://sspai.com/post/65767)（你为什么选择 Google Pixel？） 但当你最终入手一台 Google Pixel，就还得面对另一个比较残忍的现实：即便你拥有基础的网络条件，Google 有意或无意（大多数时候是前者）间也屏蔽了很多大陆地区用户可以访问的功能，比如此前我们已经介绍过的、为 Pixel 5/6 等机型开启国内 5G 网络的方法。 考虑到「原汁原味的 Android」这件事的选择越来越少、慕名下单 Pixel 系列的新用户（相对）则越来越多，这篇文章中我们借近期 Pixel 8 系列免 root 解锁 VoLTE、5G 网络的新方案，分享一下 Google Pixel 系列机型的上手指南。 再聊解锁与 root 尽管都是为了感受最原汁原味的 Android，国内 Pixel 用户对使用体验的期望依然各有不同：看重 OTA 体验，希望尽可能减少玩机操作甚至 root 的影响，一般会选择仅解锁 Bootloader；喜欢完全掌控设备，享受 Magisk 模组带来的便利与实用性的朋友，解锁 Bootloader 之外则一定会选择 root。 无论你是哪种 Pixel 用户，我都建议在可能的情况下对 Bootloader 进行解锁。虽然理论上安全性会有所降低，但解锁状态的 Bootloader 另一方面也是各种翻车情况下进行恢复的急救通道（通过刷写工厂镜像）。 至于解锁流程就是老生常谈了，如果你对 Pixel 近几代机型不太熟悉，需要注意的地方是 Pixel 7 这样的新机型解锁 Bootloader 对应的命令是： fastboot flashing unlock 而非此前的 fastboot oem unlock。需要注意的是，解锁操作会清除当前设备上的所有内容（相当于进行一次恢复出厂设置），操作前请进行数据备份！ 解锁完成后我们就可以通过手动刷入镜像的方式来升级到最新版本系统了（自动 OTA 视设备已安装系统情况则可能需要多次）。 更新系统 下载最新的、适用于本机型的、完整的镜像文件。

这三个条件请注意检查，任何一个错了都会导致「翻车」。更重要的是，请保证访问页面时页面语言为英文。中文页面存在更新不及时的问题。（Google/Bing 搜索 Pixel 工厂映像）

![](http://image.coolapk.com/feed/2024/0715/18/23371073_f0038084_0432_6719_996@1004x565.jpg.m.jpg)

下载后解压，然后将手机重启至 bootloader 并连接电脑。在 Mac 上，刷机用到的脚本是 flash-all.sh，而在 Windows 上是 flash-all.bat。 如果你尚未配置手机，手机里没什么要保留的数据，那么直接运行脚本刷入即可，刷完手机会自动开机，开机后你可以跳转至下一小节「进行 root」继续操作。 如果你已经配置了手机，手机里有数据需要保留（比如每个月的安全更新发布了，你重新下载了最新版系统的完整工厂镜像），那么在获取并解压工厂镜像后，我们需要打开脚本文件进行编辑。 具体而言： 打开脚本后，你能在最后一行看到类似 fastboot -w update image-xxxxxx.zip 这样的语句 将这句更改为 fastboot --skip-reboot update image-xxxxxx.zip 其实就是将 -w 去掉了，替换成了 --skip-reboot，这样做的目的是避免刷机脚本清除用户数据，同时防止刷机完成后手机自动开机（开机前我们要先 root 啦）。 对了如果你选择了 --skip-reboot，刷机脚本跑完后手机应该会停留在 fastbootd 界面，注意识别菜单选项，用音量键选择重启到 bootloader 然后电源键确认，即可继续下面的操作。 获取 root 权限 接下来的部分为 root 教程，没有需求的用户请选择性跳过。

首先我们提取需要破解的镜像。将下载下来的完整镜像压缩包解压，得到下图所示文件列表：

![](http://image.coolapk.com/feed/2024/0715/18/23371073_9408b801_0432_6722_891@704x277.jpg.m.jpg)

然后打开如图所示红框中的压缩包，得到下图所示文件列表：

![](http://image.coolapk.com/feed/2024/0715/18/23371073_06e582c8_0432_6724_102@828x604.jpg.m.jpg)

从这里开始，流程根据机型的不同也会有所差异： 如果你购买的设备是 Pixel 6 系列之前的设备（包含 Pixel 6 系列），这里我们需要提取 boot.img 用于镜像破解 如果你购买的设备是 Pixel 7 系列之后的设备（包含 Pixel 7 系列），这里我们需要提取 init\_boot.img 用于镜像破解 我们将需要的镜像提取出来、放进手机，放到哪里不重要，待会儿能找到就行。接下来的 root 流程，则需要你根据自己的实际需求选择 root 方案：Magisk 兼容性强、模块生态成熟；Kernel SU 能够通过比较基础的设备完整性验证，无需繁琐操作即可从 Play 商店安装 Netflix、ChatGPT、Apple Music 等 app。 破解镜像

前往 Magisk 的 GitHub 页面（[查看链接](https://github.com/topjohnwu/Magisk/releases)），下载 Magisk，下载完成后用你喜欢的方式安装到手机上（adb install 或者传输后手动安装均可）。安装完成后开始破解镜像文件：

  - 打开 Magisk Manager，选择最上方的「安装 > 选择并修补一个文件」，然后找到刚刚扔进手机的镜像文件执行破解 破解成功后，Magisk 会在 Download 这个目录下生成一个破解好的镜像文件，找到它，然后把它扔回电脑

使用 Kernel SU 进行自动破解的流程类似。前往 Kernel SU 的项目页面（[查看链接](https://github.com/tiann/KernelSU/releases)）下载最新版管理器 (APK 文件）并安装，然后点击主界面右上角的安装图标并根据提示破解上面提取的镜像文件即可。

![](http://image.coolapk.com/feed/2024/0715/18/23371073_d7ae1e1d_0432_6732_509@1344x2992.jpg.m.jpg)

![](http://image.coolapk.com/feed/2024/0715/18/23371073_de9b197c_0432_6737_573@1344x2992.jpg.m.jpg)

接下来我们就可以进行 root 了： 手机重启至 bootloader 并连接至电脑 命令行执行 fastboot flash init\_boot 或 fastboot flash boot 加上你破解的镜像即可，比如 Pixel 8 系列破解的是 init\_boot 镜像，使用的是前者 完成后重启，完事\~ SafetyNet/隐藏 root 为了保证你的设备在 root 后也能正常下载、安装和更新 Netflix 等 app，这里建议在 root 完成并开机后先别干的，优先执行 SafetyNet 相关的环境配置工作——如果你使用的是 Kernel SU 方案，那这部分正常情况下则可以跳过。 SafetyNet 的介绍有兴趣可以读这个（文章里的方法已经过时了）：Android 玩机「神器」的矛盾与新生：Magisk Canary 更新详解

下载 PlayIntegrityFix（ [查看链接](https://github.com/chiteroman/PlayIntegrityFix/releases)）和 Shamiko （[查看链接](https://github.com/LSPosed/LSPosed.github.io/releases)）模块，然后传输至手机备用

打开 Magisk Manager，安装上面两个模块，然后重启（对了，这一步你可以把一些额外的模块也顺手装上再重启，减少重启次数） 重启后，打开 Magisk Manager，点击右上角的齿轮图标进入设置，勾选上 Zygisk 开关 然后点击「配置排除列表」，在排除列表右上角菜单里勾上「显示系统应用」，然后搜索下面这几个东西并勾选（中文系统下名称/英文系统下名称） Google Play 商店/Google Play Store Google 服务框架/Google Play Framework Google Play 服务/Google Play Services 其他检测 root 的应用，比如 Apple Music

注意，在笔者所使用的 Pixel 8 系列机型、最新版 PlayIntegrityFix 模块这一环境下，通过上述操作即可通过 MEET\_DEVICE\_INTEGRITY 认证；而如果你在执行上述操作后无法通过认证，不能正常搜索、下载和使用 Netflix 等应用，则需要手动寻找、替换新的设备指纹（fingerprints）来绕过检测。详细的说明和操作见 PIF FAQ（[查看链接](https://xdaforums.com/t/pif-faq.4653307/)）。

![](http://image.coolapk.com/feed/2024/0715/18/23371073_ddb58b49_0432_6741_658@1343x1788.jpg.m.jpg)

对了，既然提到了安装模块，这里推荐一个个人认为可以提升幸福感的模块：NotoSansCJK（[查看链接](https://github.com/simonsmh/notocjk/releases)），思源黑、动态字重、粗细分明，可以说是 Pixel 必备。 免 root 解锁网络功能 如果第一部分的内容与你无关，或者你已经被第一部分内容的篇幅吓到了，这一部分就是为你准备的。 在没有获取 root 的情况下，Pixel 6/7 系列可以解锁国内运营商 VoLTE 相关功能，Pixel 8 系列最近则有了进一步解锁 5G 网络的方法。

VoLTE 的基础性和重要性本文不再赘述了，对 Pixel 6/7 这两代设备而言，VoLTE 功能同时也是电信用户正常使用通话功能的前提。因此这里推荐没有 root 的用户选择近期由韩国开发者 [@kyujin-cho](/u/kyujin-cho) （[查看链接](https://github.com/kyujin-cho)）分享的免 root VoLTE 功能解锁方案。

  - 说起 Android 这边的「免 root 玩机」话题，Shizuku 这款工具自然是少不了的。所幸 undefined 此前已经分享过非常相近的介绍和配置方法，因此本教程的第一部分「Shizuku 配置」，请移步至下面这篇文章了解。

关联阅读：[查看链接](https://sspai.com/post/73294)

确保 Shizuku 服务已经正常运行之后，前往 Pixel IMS 的发行版页面（[查看链接](https://github.com/kyujin-cho/pixel-volte-patch/releases)）下载安装该工具的最新版本。安装完成后启动 Pixel IMS，此时你应该能够看到一个 Shizuku 接口调用的权限请求，点击「总是允许」：

![](http://image.coolapk.com/feed/2024/0715/18/23371073_c9af5e42_0432_6751_422@1440x3120.jpg.m.jpg)

图：kyujin-cho

随后进入 Pixel IMS 的主界面（希望开发者后续能适配个 Material 3 不知算不算过分），点击左下角的 ENABLE VOLTE 按钮进行激活。激活后，VoLTE Status 区域下的 VoLTE Enabled by Config 选项开关会自动变成启用状态。

![](http://image.coolapk.com/feed/2024/0715/18/23371073_a9bcd318_0432_6757_134@576x1280.jpg.m.jpg)

![](http://image.coolapk.com/feed/2024/0715/18/23371073_25b0e3c4_0432_6764_56@576x1280.jpg.m.jpg)

重启设备后你应该就能看见对应 SIM 设置中的 VoLTE 选项开关了。至此，电信用户已经可以在 Pixel 6/7 系列机型上拥有完整的 4G 网络体验。 针对 Pixel 8 系列的 5G 网络功能，近期 Google 在 Android 14 的 QPR3 Beta2 固件中「不小心」内置了一个为中国地区直接解锁 5G 网络的基带，对应的系统版本为 beta-ap21.240216.010（不是最新的 240305），基带版本为 beta-g5300i-240215-240223-b-11487724。

因此我们只需要下载上述系统镜像、提取对应的基带文件 radio-husky\_beta-g5300i-240215-240223-b-11487724.img，然后通过 fastboot flash radio 指令刷入并重启即可。

![](http://image.coolapk.com/feed/2024/0715/18/23371073_56408ec9_0436_3304_24@993x656.jpg.m.jpg)

由于该版本镜像现在已经被更新版本的替换掉了，这里直接提供适用于 Pixel 8 系列的基带文件下载（[查看链接](https://1drv.ms/u/s!AmLm2t9yvX8sgYE05TW53geU2JGrYA?e=rg2BzH)） root 后解锁网络功能 （转载者注：还是推荐上面的方法，第二个方法涉及修改系统文件。） 而如果你选择了 root 和 Magisk 这条路，root 权限则能在网络体验这件事情上为你带来更加完整的便利。本部分将基于此前的解锁流程简单介绍一下 Pixel 7 系列机型的 5G 网络、Vo5G 通话开启方法。 关联阅读：一日一技 | 为 Google Pixel 6 解锁国内 5G 网络支持 还是从 VoLTE 说起，你可以参考此前的教程使用 Magisk 模块来解锁 VoLTE，不过我在后续的使用和测试过程中发现，对 root 用户而言即便不用模块也能打开 VoLTE 的相关设置。具体流程如下： 前往 Google Play 商店下载 MiX 文件管理器 打开 MiX 文件管理器，然后导航至 /data/user\_de/0/com.android.phone/files 路径，过程中如果弹出 root 权限请求请选择授予 在上述路径中找到 carrierconfig-com.google.android.carrier-xxxxxxx-xxx.xml 文件并使用 MiX 文件管理器内置的代码编辑器打开 定位至编辑器末尾，在 </init-array> 和 </bundle> 中间，粘贴以下字段（\#后为注释记得去掉）： <boolean name="enhanced\_4g\_lte\_on\_by\_default\_bool" value="true" /> \#默认开启 LTE <boolean name="carrier\_volte\_available\_bool" value="true" /> \#开启 VoLTE 功能 <boolean name="vendor\_hide\_volte\_settng\_ui" value="false" /> \#显示 VoLTE 设置 <boolean name="hide\_lte\_plus\_data\_icon\_bool" value="false" /> \#隐藏 LTE+ 图标 <boolean name="vonr\_enabled\_bool" value="true" /> \#开启 Vo5G 功能 <boolean name="vonr\_setting\_visibility\_bool" value="true" /> \#显示 Vo5G 设置 <boolean name="show\_4g\_for\_lte\_data\_icon\_bool" value="true" /> \#将 LTE 网络标识显示为「4G」，可选 这里需要注意的是，如果你是 eSIM 双卡双待用户，在 com.android.phone/files 路径中也会看到不止一份配置文件。如果你难以分辨哪一个对应想要开启的运营商，可以在手机的「系统设置 > 关于手机」中的对应 SIM 卡状态中看到。 搞定 VoLTE 和相关设置可见性之后别急着重启，接下来我们还是像去年一样，通过网络信号大师这款应用来解锁 5G 网络。

具体配置流程还是参考去年的教程，唯一需要注意的是，Pixel 7 系列用户的配置流程与 Pixel 6 略有不同，需要在「NR MODE SETTING」里选择 SA 或者 NSA & SA（其实相对更简单了）。下方的 NR Band Combo 可随意（FR2 对应 mmWave 毫米波通讯功能，美版会有、国内没用）。

![](http://image.coolapk.com/feed/2024/0715/18/23371073_d1340aa6_0436_3314_252@1440x3120.jpg.m.jpg)

![](http://image.coolapk.com/feed/2024/0715/18/23371073_9eae463f_0436_332_411@1440x3624.jpg.m.jpg)

完成所有操作后重启手机，然后你应该就能在设置中看到 5G 网络、VoLTE、5G 通话以及 2G 网络开关等相关设定了。 让 5G 信号「更好」 注：本部分内容教程部分援引自酷安，原作者 xjw233，相关内容已获得作者授权。 通过上述任意手段为 Pixel 启用国内运营商 5G 网络后，你会发现手机的 5G 网络信号好像不怎么好。如果不是身处信号强度较好的市中心或基站附近，搭载 Tensor 芯片的 Pixel 设备（6\~8 三代）日常使用时的 5G 信号一般只有两格，一格甚至也都是常有的事。 是 Google 技不如人吗？当然不是。当我们谈论信号强度时，dBm（分贝毫瓦）是比「格子」更准确也更科学的计量方式，对移动设备而言，信号强度的数值一般为负，越接近 0 则信号越强，同时信号强度高于 -90dBm 时一般才被认为具备正常通话和访问数据网络的能力。

从用户的角度出发，数字肯定是不如信号格数直观的，因此在统一的计量单位下，手机厂商一般还会自行选择一套转换公式将信号强度对应到不同级别的信号格数中去，以下面这张广为流传的表格为例，华为、vivo、OPPO 一般会将 -90dBm 以上的强度为最强信号、-105\~-95dBm 往上为 3 格、-110dBm 左右往上为 2 格，以此类推。

![](http://image.coolapk.com/feed/2024/0715/18/23371073_c0575f04_0436_3328_147@798x394.jpg.m.jpg)

Pixel 信号不好，说到底还是不接地气或者说「不合国标」：打开 Pixel IMS，在 SIM 配置页面的「其他」板块找到专家模式，等待加载完成后搜索 5g\_nr\_ssrsrp\_thresholds\_int\_array：

![](http://image.coolapk.com/feed/2024/0715/18/23371073_67aae9ca_0436_333_360@1150x2560.jpg.m.jpg)

可以看到大部分国内厂商信号最强的挡位（-90dBm），在 Google 眼里只能获得 2 格信号……所以如果你想视觉上好受点、心理上也愉悦一点，不妨参考上面两张图在这里为不同的信号强度表示分配新的阈值。遇到无法输入字符或者输入字符后 Pixel IMS 闪退的情况，也可以在「SIM 配置」的「其他」设置部分点击「手动设置」，然后在弹出的「更新属性值」对话框中： 属性名填写 KEY\_5G\_NR\_SSRSRP\_THRESHOLDS\_INT\_ARRAY 类型填写 IntArray

数值选择自己喜欢的方案，用英文逗号隔开

![](http://image.coolapk.com/feed/2024/0715/18/23371073_6886ade1_0436_3339_246@720x1603.jpg.m.jpg)

修改完成后你就能拥有一台信号强度媲美国产手机的 Pixel 啦。

![](http://image.coolapk.com/feed/2024/0715/18/23371073_d6f1042d_0436_3343_397@1280x604.jpg.m.jpg)

小结 简而言之，如果你是没有 root 的用户，通过本文第二部分教程，简单几步便能在国内解锁电信网络和三大运营商的 VoLTE 功能；如果你是 root 用户，通过本文第三部分教程则可以拥有完整的 5G 网络体验。 最后感谢为 Pixel 玩机社区不断贡献、为大家带来便利的所有开发者。如果本文对你有所帮助，请考虑为相关 GitHub 页面加上星标或帮助教程原始作者进行传播分享。

（注：本文章为转载文章，原始作者为“少数派”平台用户“克莱德” ，经授权使用。亦感谢他授权我转载文章，原文链接：[查看链接](https://sspai.com/post/78200)）

[#Pixel8#](/t/Pixel8?type=12) [#Pixel8Pro#](/t/Pixel8Pro?type=12) [#GooglePixel7Pro#](/t/GooglePixel7Pro?type=12)
