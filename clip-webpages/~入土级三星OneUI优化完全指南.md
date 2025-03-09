---
created: 2024-08-10T12:00:00
source: https://radishzz.cc/posts/384776b2.html
tags: [[samsung]]
type: archive-web
modified: 2025-01-15T11:38:17
---

本文是一篇针对三星 OneUI 的超大型免 root 优化指南，旨在帮助大家「提升设备的续航与流畅度」，解决耗电过快、卡顿掉帧等问题。指南详细介绍了各种优化方法和相关原理。跟着这些方法，你的三星设备将会获得「超强的续航」和「丝滑的体验」，仿佛重获新生！

本指南以港版 OneUI 6.1 为背景，结合「大量前辈经验」和「个人玩机心得」重制而成。篇幅超长，全部看完需要 30 分钟左右。你可以先通过右侧的「目录」了解大致内容。如果你准备好了，那么我们就开始吧！

#### [](\#双清刷机篇) 双清刷机篇

![图片](/images/loading.svg)

想要对房子进行精装修，最好是从「干净的毛坯房」开始。同样地，想要对设备进行优化，最好是从「干净的系统」开始。一个「干净的系统」可以为设备打下良好的软件基础，不受应用卸载残留、系统升级冲突、设备缓存积累等问题影响。那么怎样才能实现「干净的系统」呢？有以下三种方式：

  > * **恢复出厂设置**：删除所有用户数据、应用程序、个性化设置等，将设备恢复到出厂状态。
  > * **双清**：执行两个清除操作，包括恢复出厂设置 `Wipe data/factory reset` 和清除系统缓存分区 `Wipe Cache Partition`。
  > * **刷机**：刷入完整系统固件（全量包），相当于彻底重装设备的操作系统。

**清理效果排名：刷机 > 双清 > 恢复出厂设置**。对于大多数人来说，恢复出厂设置就足够了。但对于能看到这篇文章的朋友，你们应该不会只局限于此。接下来我会介绍双清和刷机的「具体步骤」。新手可以尝试简单的双清，高手直接刷机就行了。操作前记得备份数据，防止重要数据丢失。

##### [](\#双清) 双清

![图片](/images/loading.svg)

  > 1. 退出三星账号与 Google 账号。
  > 2. 关机后按住「电源键」和「音量 + 键」，同时用数据线连接电脑，进入如上 `recovery` 界面。
  > 3. 选择 `Wipe data/factory reset` 清除数据/恢复出厂设置，再选择 `yes` 确定。
  > 4. 选择 `Wipe cache partition` 清除缓存分区 ，再选择 `yes` 确定。
  > 5. 选择 `Reboot system now` 重启系统即可。

##### [](\#刷机) 刷机

![图片](/images/loading.svg)

[视频教程推荐](https://www.bilibili.com/video/BV1WT411U7QL/?spm%5Fid%5Ffrom=333.999.0.0&vd%5Fsource=aa0fa65feef706e1da2fb8b025515559)

**工具准备**

**完整步骤**

  > 1. 退出三星账号与 Google 账号。
  > 2. 安装上述 USB 驱动与线刷工具，并解压固件（`BL`、`AP`、`CP`、`CSC`、`USERDATA`）
  > 3. 打开 Odin3，依次选择 `BL`、`AP`、`CP`、`CSC` 并导入对应文件。导入 `AP` 大概需要三分钟，耐心等待即可。
  > 4. 设备关机状态下，同时按住「音量 + 键」和「音量 - 键」，并用数据线连接电脑，亮屏后松开，再按一下「音量 + 键」，出现「下载图标」则代表已进入刷机模式。
  > 5. 查看左上角 `ID:COM` 方块，显示 `0:COM+数字` 则代表设备连接成功，点击 `Start` 开始刷机。
  > 6. 左上角显示 `PASS`，代表刷机完成，设备会自动重启。

如果显示 `FAIL` 失败怎么办？以下为个人经验，仅供参考。

  > 1. 拔掉数据线，长按「电源键」和「音量 - 键」7 秒，强制重启设备。
  > 2. 出现「更新设备软件时发生错误」的蓝色界面。不要慌，此界面也是刷机模式。
  > 3. 直接插入数据线，点击 `Start` 开始刷机。
  > 4. 查看 odin 左上角，进度条有变化则代表已进入正常刷机状态。
  > 5. 等待显示 `PASS` 即可。

#### [](\\#应用安装篇) 应用安装篇

![图片](/images/loading.svg)

新机到手，或者刚刷完系统后，不建议直接在「应用商店」安装应用，或者用「换机助手」恢复应用。因为这样安装的都是「官方最新版」。

官方最新版不好吗？不好。大部分国产应用都是越更新越臃肿，每次更新不是加一堆广告，就是塞各种没用的功能。所以现在，你甚至可以在支付宝里「刷短视频」，也可以在美团里「玩原神」。

另外，三星作为国内的 Others，没有任何一款国产应用会主动针对 OneUI 进行适配优化。即使是最新的旗舰机 S24 Ultra ，在运行某些应用时依然会卡顿掉帧，例如微博、B 站等。

##### [](\#版本选择) 版本选择

因此，想要设备变得流畅省电，第一步就是选择「其它版本的应用」进行安装，并且不轻易更新。这能有效避免「官方最新版」过度占用 CPU 资源，从而导致系统卡顿的问题。

**版本选择的优先级如下：**

**Play 版 > 定制版 > 第三方 > 破解版**

我在这里分享一些找安装包的网站。大多数应用都能在这里找到，全部找一遍可能需要花费一定时间，但当你建立起自己的「应用集」后，以后换机就会轻松多了。

##### [](\#下载途径) 下载途径
##### [](\#使用习惯) 使用习惯

补充一个冷知识。应用在「冷启动」时，设备的电流会瞬间飙升，是「热启动」的好几倍。就像以前的白炽灯，在开灯的瞬间，通过灯丝的电流会特别高。如果频繁地开关灯，灯丝甚至会烧断。

因此，在设备不卡顿的情况下，不要频繁地「清空后台」。后台的应用缓存是可以加快应用启动速度、降低设备耗电的。

#### [](\#系统设置篇) 系统设置篇

![图片](/images/loading.svg)

你可以跟着指示「逐步查找」对应功能，也可以在设置中使用「搜索」来跳转。如果你认为某些功能对你有用，你可以选择保持「设备默认选项」。由于系统版本的差异，有些功能的「名称/位置」会不太一样，请注意识别。

##### [](\#系统设置) 系统设置

1. **三星账户**

  >   * 安全与隐私 - 个性化服务 - 停止自定义所有设备（停止所有个性化）
  >   * 安全与隐私 - 获取新闻和特惠（关闭）
  >   * 三星云 - 所有选项（按需选择，可全部关闭）
  >   * 查找我的手机 - 允许找到此手机、发送最后的位置（按需选择，可关闭）- 右上角三个点 - 通知 - 新功能（关闭）

2. **连接**

  >   * Wi-Fi- 右上角三个点 - 智能 Wi-Fi- 显示网络质量信息（开启）- 其它功能（全部关闭）
  >   * NFC 与非接触式支付（按需选择，可关闭）
  >   * 超宽带 UWB（关闭）
  >   * 流量监控 - 流量节省（关闭）
  >   * 更多连接设置 - 附近设备扫描（关闭）
  >   * 更多连接设置 - 打印（关闭）- 默认打印服务（关闭）

关于 Wi-Fi 省电模式，虽然介绍说是可以降低电池使用量，但是也会降低数据吞吐量。设备只在周期性唤醒时进行数据收发，这可能会影响微信消息的「实时接收」。

1. **已连接的设备**

2. **通知**

  >   * 应用程序通知（关闭不需要的通知）
  >   * 高级设置 - 管理每个应用程序的通知类别（开启）

3. **显示**

  >   * 黑暗模式（按需选择，可开启）
  >   * 自动调节亮度（按需选择，可关闭）
  >   * 屏幕分辨率（按需选择，可选 QHD+）
  >   * 自动息屏（1 分钟）- 查看时保持屏幕开启（关闭）
  >   * 导航条 - 即圈即搜/圈定即搜（按需选择，可关闭）
  >   * 意外触摸保护（关闭）
  >   * 触摸灵敏度（关闭）

4. **电池**

  >   * 电池保护（按需选择）
  > _**省电模式↓**_
  >   * 将 CPU 速度限制为 70%（开启）
  >   * 其它选项（按需选择，可全部关闭）
  >   * 右上角三个点 - 自适应省电（关闭）
  > _**后台使用限制↓**_
  >   * 右上角三个点 - 自适应电池（关闭）
  >   * 让未使用的应用程序进入休眠（开启）
  >   * 本地电池政策（开启）
  >   * 先在「深度休眠」里添加所有应用，再到「休眠」里添加常用应用
  >   * 找不到「休眠/深度休眠」的，请跳转至步骤 25
  >   * 「从不自动休眠」留空，因为该功能与「电池不受限制」冲突，而后者效果更好

在电池设置中，我关闭了所有的「自适应」功能。因为「自适应」的后台管理机制不一定符合我的使用习惯，所以改成「由自己管理」，例如分配深度休眠等。如果你分配不好，可以不跟随设置。

1. **主屏幕**

  >   * 将媒体页面添加至主屏幕（按需选择，可关闭）
  >   * 向下滑动打开通知面板（开启）
  >   * 在主屏幕中搜索（按需选择，可关闭）

2. **锁定屏幕与熄屏提醒**

  >   * 延长解锁 - 贴身检测（关闭）
  >   * 息屏提醒（按需选择，可关闭）
  >   * 长按即可编辑（关闭）
  >   * 漫游时钟（按需选择，可关闭）
  > _**安全锁定设置↓**_
  >   * 在屏幕关闭时自动锁定（5 秒）
  >   * 用侧面按键立即锁定（开启）
  >   * 自动出厂重置、锁定网络与安全、显示锁定选项（关闭）

3. **安全与隐私**

  >   * 自动拦截程序（全部关闭）
  >   * 更多安全设置 - 安装未知应用程序（全部拒绝，再按需单独开启）
  >   * 更多安全设置 - 盖乐世系统应用程序更新（关闭）
  >   * 许可证管理器（逐个检查，关闭多余权限）
  >   * 其它隐私控制 - 访问剪贴板时提醒（开启）
  >   * 更多隐私设置 - 发送诊断数据、Android 个性化服务（关闭）- 广告（删除广告 ID）、使用情况和诊断信息（关闭）
  > _**应用程序安全性↓**_
  >   * 应用程序保护 - 右上角三个点 - 应用程序保护设置 - 每天自动扫描、安装应用程序时自动扫描、支付安全（全部关闭）- 信任的应用程序（添加所有应用）
  >   * Google Play Protect- 右上角设置 - 使用 Play 保护机制扫描应用、改进有害应用检测（关闭）
  > _**生物识别↓**_
  >   * 显示解锁过渡效果（按需选择，可关闭）
  >   * 指纹 - 删除所有已添加的指纹，把所有手指交替录入到同一枚指纹当中，录入时确保每次按压都覆盖完整，并且保持按压状态直到提示抬起手指。
  >   * 指纹 - 指纹始终开启（按需选择，可关闭）

4. **定位服务**

5. **安全与紧急状况**

  >   * 驾车时通知设为静音、紧急位置信息服务、无限紧急警报、地震警报、不明追踪器提醒（全部关闭）

6. **账户与备份**

7. **Google**

  >   * 广告 - 广告隐私权 - 所有选项（全部关闭）
  >   * 查找我的设备（关闭）

8. **高级功能**

  >   * 智能建议（关闭）
  >   * SPen- 更多 SPen 设置 -SPen 解锁、允许使用多个 SPen、保持 SPen 连接（关闭）
  >   * 单手模式（按需选择，可关闭）
  > _**动作与手势↓**_
  >   * 拿起时唤醒（按需选择，可关闭）
  >   * 双击可打开屏幕、双击可关闭屏幕（开启）
  >   * 手掌滑动截屏（关闭）

9. **智能管理器/设备维护**

  >   * 内存 - 已排除的应用程序 - 右上角加号（添加需要实时接收消息的的应用）
  >   * 内存 -Ram Plus（8G 开启，12G 关闭）
  >   * 性能配置（轻度）
  >   * 自动优化 - 自动重启（关闭）

关于 Ram Plus，其原理是把一部分存储空间当作额外的 Ram 来使用。这对低内存设备或重度使用场景（玩游戏等）是有好处的。但如果物理 Ram 足够大，系统足够流畅，再开启 Ram Plus 就不会有多少提升效果，相反还会因为频繁的数据交换而略微降低性能。

1. **应用程序**

  >   * 点击右侧居中位置的图标「排序」- 显示系统应用程序（打开）
  >   * 搜索「OneUI 主屏幕」并打开 - 电池（不受限制）
  >   * 搜索「系统 UI」并打开 - 电池（不受限制）
  >   * 右上角三个点 - 特殊访问（逐个检查，关闭多余权限）

2. **辅助功能**

  >   * 视觉增强 - 减少动画、减少透明度和模糊效果（关闭会影响动画效果，按需选择）

3. **软件更新**

4. **开发者选项**

  >   * _**开启方式：关于手机 - 软件信息 - 连续点击编译编号**_
  >   * 日志记录器缓冲区大小（关闭）
  >   * 系统跟踪 - 跟踪可调试的应用（关闭）
  >   * WLAN 扫描限制/调节（开启）
  >   * 暂停执行缓存的应用程序（保持设备默认设置，这等于开启）
  >   * 预见式返回动画（开启）

_**拓展阅读： [《开发者选项中的「暂停执行已缓存的应用」是墓碑模式吗？》](https://radishzz.cc/404page/)**_ _（文章待搬运，可以先在我的酷安主页查看）_

##### [](\#其它设置) 其它设置

1. **关闭应用自动更新**

  >   * _**打开 Play 商店 - 右上角头像 - 网络偏好设置**_
  >   * 自动更新应用（关闭）
  >   * 自动播放视频（关闭）
  > _**打开自带应用商店 - 左上角图标 - 右上角设置**_
  >   * 自动下载并更新应用程序（从不）
  >   * 获取新闻与特惠（关闭）
  >   * 个性化推荐（关闭）

2. **限制应用后台运行**

  >   * _**仅适用于「不需要」实时接收消息的应用**_
  >   * 回到系统桌面 - 长按应用 - 点击右上角⊙
  >   * 移动数据 - 允许后台流量使用（关闭）
  >   * 电池（受限制）
  >   * 打开设置 - 搜索「休眠」- 根据使用频率，分配应用至（休眠）或（深度休眠）

3. **保持应用后台运行**

  >   * _**仅适用于「需要」实时接收消息的应用**_
  >   * 回到系统桌面 - 长按应用 - 点击右上角⊙
  >   * 允许后台流量使用（保持默认开启）
  >   * 电池（不受限制）
  >   * 打开设置 - 搜索「内存」- 已排除的应用程序 - 右上角加号（选择并添加）

4. **应用通知最小化**

  >   * _**可在「保留应用通知」的同时，隐藏其显示在通知栏中的「图标」**_
  >   * 打开设置 - 搜索「管理每个应用程序的通知类别」（开启）
  >   * 打开通知面板 - 长按应用通知 - 设置 - 通知类别 - 点击「高亮选项」- 最小化通知（开启）

##### [](\#Good-Guardians-设置)Good Guardians 设置

以下应用都在三星官方插件「Good Guardians」中，这款应用可以在系统自带的应用商店中搜索下载。注意，这些应用都需要保持在后台运行，否则所有设置都会失效，可以参考上述步骤 22 来设置。

1. **Thermal Guardian（管理设备温度）**

  >   * 过热阈值（调到最低）
  >   * 更多设置（仅勾选过热时限制 CPU 提升）
  >   * 关于过热阈值，从左到右的档位分别是 37、38、39、40、41 度。有说调高好的，也有说调低好的。我这里建议调低，可以减少设备发热情况。

2. **Memory Guardian（管理设备内存）**

  >   * 已排除的应用 - 添加需要「实时接收消息」的应用
  >   * 底部选项「定制」- 选择「快速切换模式」

3. **Battery Guardian（管理设备续航）**

  >   * 应用程序省电（开启）- 点进去 - 右上角三个点 - 设置中找不到的「休眠/深度休眠」藏在这里
  >   * 就寝时省电（开启）
  >   * 设置睡眠时间（00:00-23:59）
  >   * 「幕布」功能可以关注一下

4. **App Booster（提高设备流畅度）**

#### [](\#Shizuku-应用篇)Shizuku 应用篇

![图片](/images/loading.svg)

作为本篇章的核心，首先要介绍的就是 Shizuku。它是一款 Android 应用，允许其他应用直接使用「系统 API 」，而无需 root 权限。以禁用 Google 框架为例，传统做法需要 root 设备来获取完整控制权，而 Shizuku 可以通过用户授权来「接管」系统 API，然后其它应用就可以通过 Shizuku 来使用系统 API ，从而实现「禁用系统应用」等高级功能。

Shizuku 下载安装后，需要通过「用户授权」才能正式接管系统 API。根据用户使用手册，一共有三种启动 Shizuku 的方式。通常我们采用「通过无线调试启动」，无需借助 root 或电脑，仅需满足「开发者选项已开启」和「设备已连接 Wi-Fi 」即可。

##### [](\#Shizuku-启用方式)Shizuku 启用方式

  > 1. 打开 Shizuku，点击「配对」
  > 2. 点击「开发者选项」 ，下滑找到「USB 调试」 并开启
  > 3. 找到「无线调试」 ，点击进入二级页面
  > 4. 打开无线调试开关，点击「使用配对码配对设备」
  > 5. 找到通知栏中的 Shizuku，「输入配对码」并发送
  > 6. 配对成功，返回 Shizuku 主页，点击「启动」
  > 7. 等待片刻，主页显示「Shizuku 正在运行」，即为启动成功
  > 8. 打开「已授权 0 个应用」，给予授权即可

注意，Shizuku 需要保持在后台运行，否则所有授权都会失效，可以参考「系统设置篇」的步骤 22 来设置。 成功启动 Shizuku 以后，就可以愉快地使用各种支持 Shizuku 的应用了。以下几款是我推荐的。

##### [](\#Sam-Helper)Sam Helper [下载地址](https://www.123pan.com/s/2xiAjv-CXzPh.html)

三星助手， 一款专门为三星设备开发的工具箱。它提供气密性测试、终端工具、修改系统设置等许多功能，并且整合了 Good Lock 和 Galaxy Labs 里的所有应用，帮助用户更方便地自定义系统。

使用 Sam Helper 需要安装一款插件 Sam Plugin，软件内会提供下载。如果遇到「插件无法安装」的问题，这是因为这款插件的 API 非常低，系统会限制低 API 应用的安装。你可以使用下方提到的 InstallerX 来解决。

除此以外，还可以通过 Sam Helper 来实现以下几个功能：

###### [](\#查询电池健康)**查询电池健康**

![图片](/images/loading.svg)

  > 1. 点击主页右上角的第二个图标，进入 Shizuku 终端
  > 2. 输入以下代码并执行
  > `dumpsys battery | grep -i msave`
  > 3. 查看输出结果
  > 4. 第二行：电池健康度 98%
  > 5. 第五行：电池循环次数 248.48 次
  > 6. 结果仅供参考

###### [](\#卡省电模式-120Hz-刷新率)**卡省电模式 + 120Hz 刷新率**

OneUI 在省电模式下，默认无法开启 120Hz。如果你想「同时拥有」 省电模式的省电效果，和 120Hz 的高刷体验，就需要用到以下方法（俗称卡省电）：

![图片](/images/loading.svg)

  > 1. 开启省电模式
  > 2. Sam Helper- 系统设置 - 屏幕刷新率（自适应）
  > 3. 打开电话，输入任意数字，例如 `0`
  > 4. 点击左侧按键，开启视频通话
  > 5. 3 秒后挂断即可

在以下情况下，卡省电会「失效」，需要重新设置：

* 进入设置中的「显示」选项

* 重启「设备」或「省电模式」

###### [](\#禁用系统更新)**禁用系统更新**

如果不想「升级系统」，或者想要关闭「更新手机」的通知提醒，可以通过 ADB 指令来实现。

![图片](/images/loading.svg)

  > 1. 进入 Shizuku 终端
  > 2. 输入「禁用指令」并执行即可，两条指令要分开执行
  > `pm disable-user com.wssyncmldm`
  > `pm disable-user com.sec.android.soagent`
  > 3. 如果想「恢复系统更新」，执行「解禁指令」即可
  > `pm enable com.wssyncmldm`
  > `pm enable com.sec.android.soagent`

##### [](\#Battery-Guru)Battery Guru [下载地址](https://liteapks.com/battery-guru.html)

![图片](/images/loading.svg)

电池专家，一款电池健康管理工具。它提供了实时电流检测、电池容量估算、应用耗电情况等多种功能，来帮助用户监控和管理电池的使用情况，从而延长电池寿命。

我们可以通过「放电波形图」来判断设备是否存在「耗电异常」的情况。还可以优化设备的 `Doze`（瞌睡）模式，或者开启「快速 Doze」来帮助设备在息屏后快速进入「深度 `Doze` 模式」，从而降低待机功耗。

###### [](\#优化-Doze-配置) 优化 Doze 配置

![图片](/images/loading.svg)

  > 1. 应用主页 - 右上角设置 - 权限管理 - 允许发布通知、修改系统设置（开启）
  > 2. 其余选项需要通过 ADB 指令才能开启
  > 3. 打开 Sam Helper 的 Shizuku 终端，「逐条」输入以下指令并执行
  > `pm grant com.paget96.batteryguru android.permission.BATTERY_STATS`
  > `pm grant com.paget96.batteryguru android.permission.PACKAGE_USAGE_STATS`
  > `pm grant com.paget96.batteryguru android.permission.WRITE_SECURE_SETTINGS`
  > `pm grant com.paget96.batteryguru android.permission.DUMP`
  > 4. 回到应用主页 - 底栏第四个选项 - 省电页面
  > 5. 配置 -Doze 优化、重新应用 Doze 参数、等待解锁（开启）

###### [](\#开启快速-Doze) 开启快速 Doze

注意，开启快速 Doze 要求先开启「省电模式」。不喜欢的话可以不设置，或者可以配合「卡省电」使用。

![图片](/images/loading.svg)

  > 1. 回到省电页面，如上图进行设置
  > 2. 仅在屏幕上开启、夜间模式、亮度调节（按需选择）
  > 3. 应用需要保持在后台运行，否则所有设置都会失效

##### [](\#App-Ops)App Ops [下载地址](https://appops.rikka.app/)

![图片](/images/loading.svg)

一款管理应用行为的工具。它通过修改系统 appops 的设置，来实现对应用的权限管理，并监控敏感权限的使用情况。相比于 Android 系统自带的权限管理，App Ops 提供了更多的管理选项。

例如，我们可以通过 App Ops 关闭某些流氓应用的运动传感器、读取剪贴板、读取日历、读取设备识别码等权限，从而防止「摇一摇广告的跳转」和「个人隐私的泄漏」。这在系统自带的权限管理中是做不到的。

##### [](\#Scene)Scene [下载地址](http://vtools.omarea.com/)

![图片](/images/loading.svg)

一款玩机工具箱，集合性能监测、充放电统计、应用管理、屏幕测试等许多功能，界面简洁易用。Scene 提供了三种工作模式，分别是基础模式、ADB 模式和 ROOT 模式。在 Shizuku 授予权限后，即可激活 ADB 模式并免费使用上述功能（ ROOT 模式需付费)。

###### [](\#dex2oat-编译)dex2oat 编译

Scene 中值得一提的是「强制 dex2oat 编译」功能。该功能的工作原理与上述提到的 App Booster 相同，但是 Scene 提供了更多的编译模式。使用 `everything` 模式编译以后，可以「最大程度」提升设备的流畅度。

_**详细原理请看 [《Galaxy App Booster 科普》](https://radishzz.cc/404page/)** （文章待搬运，可以先在我的酷安主页查看）_

##### [](\#InstallerX)InstallerX [下载地址](https://github.com/iamr0s/InstallerX)

![图片](/images/loading.svg)

安装器 X，一款干净的应用安装器。它支持降级安装应用、自动安装应用、更改安装样式等功能，并采用 Material Design 与 Monet 取色，界面简约美观。我们可以把 InstallerX 设为「默认安装器」，取代系统自带的「软件包安装程序」，从而解决广告推荐和应用检测的问题。

##### [](\#SD-Maid)SD Maid [下载地址](https://liteapks.com/sd-maid-2-se-system-cleaner.html)

![图片](/images/loading.svg)

SD 女仆，一款系统清理工具。它可以帮助用户清理不必要的文件、缓存、日志等来释放存储空间。授予「无障碍权限」后，它还能「自动清理」所有应用的缓存。这相当于你手动点进系统设置里，在每个应用的存储页面进行缓存清理。如果不是 Android 14 限制应用访问 data 文件夹，不然「清浊」也是一个非常棒的选择。

##### [](\#RootlessJamesDSP)RootlessJamesDSP [下载地址](https://play.google.com/store/apps/details?id=me.timschneeberger.rootlessjamesdsp&hl=zh&gl=US)

![图片](/images/loading.svg)

一款不需要 root 的音频处理工具。它提供了丰富的音频处理功能，如动态范围压扩器、动态低音提升、多模态均衡器、声场宽度等。Sound Assistant 跟它相比简直是小巫见大巫，就算跟 root 后的 ViPER4Android 相比，JamesDSP 也显得更加灵活和模块化，并且支持「导入配置」来调整参数。

我们可以借助它来对设备的音频进行「个性化调节」，从而优化外放或耳机的音频效果。它的缺点是需要常驻后台，且不支持 Spotify。

##### [](\#支持-Shizuku-的应用大全) 支持 Shizuku 的应用大全 [下载地址](https://github.com/ThePBone/awesome-shizuku)

几乎收录了所有支持 Shizuku 的玩机应用，各位可以尽情下载体验。

#### [](\#Lycan-禁用篇)Lycan 禁用篇

![图片](/images/loading.svg)

##### [](\#应用介绍) 应用介绍

Lycan 是一款专属于三星设备的应用，中文翻译为狼人，搭配狼头图标，~~我们不难看出作者是个狼人~~。它是 CCSWE App Manager 6.2.0 版本的「汉化翻版」应用，目前有且仅有一个版本，即 5.0.0 汉化版。这两款应用几乎完全一致，我找到了 [CCSWE App Manager 破解版](https://apkmb.com/ccswe-app-manager-samsung/) 的安装包（正版需付费），实测可以用与 Lycan 相同的激活方式进行安装激活（如上图其实是 CCSWE ），并且可以互相覆盖。

![图片](/images/loading.svg)

这两款应用的功能也完全一致。CCSWE App Manager 在 Google Play 上的应用介绍是「一款终极的软件包禁用程序和膨胀软件杀手」。软件包禁用程序，是指它可以「禁用应用」，比如 Google 框架、Google 服务等系统应用。你用不上又无法卸载的时候，就可以用 Lycan 来禁用它。

膨胀软件杀手呢？简单来说，就是指通过禁用应用的「四大基本组件」来强制管理那些「臃肿且流氓的应用」。这能极大的优化你的设备，尤其是面对一些国内公司出品的 App 时。很多人只把 Lycan 当作冰箱/小黑屋来使用（冻结系统自带应用），却忽视了这个功能，这可能是一种对 Lycan 的浪费。

###### [](\#Android-四大基本组件)Android 四大基本组件

![图片](/images/loading.svg)

由于安卓系统的开放性，有不少流氓应用会在系统内注册一堆 `Broadcast Receiver` 广播接收器和 `Service` 服务。这会导致应用被「无关行为」唤醒，或者切换至其它应用后，它也不进缓存，而是在后台「猛猛运行」，偷偷消耗着 CPU 性能与电量。

此时我们可以通过 Lycan 来解决这个问题。Lycan 可以管理「Android 四大基本组件」：`Service` 服务、`Broadcast Receiver` 广播接收器、`Activity` 活动 和 `Content Provider` 内容提供商。

* **Activity 活动**

`Activity` 是用户和应用程序交互的窗口。每一个 `Activity` 都相当于一个网页，用户可以在屏幕中进行特定操作。例如 QQ 邮箱会有一个专门的 `Activity` 用来查看邮件，也会有一个专门的 `Activity` 用来发送邮件。

* **Service 服务**

`Service` 能在后台完成「长时间运行的操作」，并且不提供用户界面。比如播放音乐的时候，即使用户切换到其它应用，音乐还是会在后台继续播放。

* **Broadcast Receiver 广播接收器**

`Broadcast Receiver` 用来「接收和响应」系统或应用程序发送的广播消息。App 可以使用它对外部事件（比如手机晃动、电话呼入、连接 Wi-Fi 等）进行接收，并根据规则唤醒对应的 `Activity` 或 `Service` 。

* **Content Provider 内容提供商**

`Content Provider` 用来保存和获取数据，并在所有应用之间实现「数据共享」。这是不同应用程序之间共享数据，且「不需要」申请存储权限的唯一方式。

\*_参考来源 [《MyAndroidTools 介绍 + Android 四大组件简析（非开发者向）》](https://bbs.letitfly.me/d/256)_

###### [](\#禁用组件的意义) 禁用组件的意义

* 禁用 `Activity`：禁用 `Activity` 会导致对应的页面无法正常显示。只有与核心功能无关或者不需要交互的 `Activity` 可以考虑禁用，例如广告、更新等页面。

* 禁用 `Service` ：`Service` 是程序能在后台活动的前提。因此禁用服务能让应用运行时少占 RAM，在后台时少唤醒 CPU。

* 禁用 `Broadcast Receiver` ：禁用不必要的 `Broadcast Receiver` ，可以避免在一些系统事件触发时，无关的应用被唤醒。

* 禁用 `Content Provider`：禁用 `Content Provider` 会导致应用程序之间无法共享数据，通常不需要禁用。

###### [](\#识别组件的方法) 识别组件的方法

禁用多余的组件可以极大地提高 App 运行时的「流畅度」，并减少 App 的「内存占用」。但是想要禁用组件，就得先认识组件。通过组件名称中的「关键词」，可以大概判断出组件的作用，然后再决定是否禁用。

**常见禁用关键词**

* 带 `push` 的都是推送通知服务，例如 `com.xiaomi.push`、`com.huawei.push` 等。

* 带 `gcm` 为谷歌推送通道，Play 版应用都会有 `google.gms` 服务。

* `sdk` 多为连接服务，比如使用 QQ、微信、微博登录等 `weibosdkbrower`。

* 有些 `sdk` 还可能是 `ads` 广告服务，例如 `igexin.sdk`、`qq.e.ads` 等。

* 带 `.ad` 或 `.ads` 的大多是广告服务。

* 非本应用厂商的服务大多都能禁用，例如 `bilibili` 里的 `alipay` 支付服务。

* 特殊广告名称：`umeng` 友盟、`igexin/getui` 个推、`kwad / kuaishou` 快手、`qq.e.ads` 腾讯、`socialbase / downloadlib / bytedance` 穿山甲、`douyin` 抖音

**常见英文名称识别**

* Auth：连接第三方

* Backup：备份

* Camera：相机

* Debug：调试

* Dialog：对话框

* Download：下载

* f：定位服务

* FloatWindow：悬浮窗

* Install：安装

* Media：音频

* Message：推送通知

* Notify：推送通知

* Notification：推送通知

* Pay：支付

* Share：分享

* Sync：同步

* TaobaoIntent：淘宝链接

* Update：更新

* Upload：上传

* Wallet：钱包

* Widget：桌面小部件

**辅助工具**

还可以搭配辅助工具 [Libchecker](https://play.google.com/store/apps/details?id=com.absinthe.libchecker&hl=en%5FUS) 来帮助我们识别组件。该应用可查看 App 的四大组件及原生库，并提供相应介绍。

![图片](/images/loading.svg)

##### [](\#如何禁用组件) 如何禁用组件

面对那么多的 App，如果真的一个组件一个组件地去识别，那无疑是愚公移山。因此我提供一个简单的禁用办法——**禁用 App 的所有「服务」和「广播接收器」**。非常简单，直接全部禁用，并且基本不影响 App 的正常使用。

国产 App 通常靠大量的 `Activity` 来运行，而不怎么依赖 `Service` 服务，因此「全部禁用」也没有关系。`Broadcast Receiver` 广播接收器，国产 App 大多利用它来实现监控、自启、推送，甚至是「链式唤醒」，因此也可以「全部禁用」。

这个方法适用于绝大多数「不需要实时接收消息」的国产 App，例如抖音、微博、贴吧等。以抖音为例。在正常情况下，抖音在退出前台后「仍在后台运行」，内存占用高达 1.7 G。

![图片](https://cdn.radishzz.cc/gh/radishzzz/jsDelivr-image/002-samsung-oneui-20.gif)

在「全部禁用」的情况下，抖音在退出前台后「立刻进入缓存」，缓存占用减少到 0.9 G。

![图片](https://cdn.radishzz.cc/gh/radishzzz/jsDelivr-image/002-samsung-oneui-21.gif)

通过禁用 App 的所有「服务」和「广播接收器」可以实现以下效果，堪比「墓碑模式」。

1. 应用退出后立刻进入缓存，不在后台驻留任何服务。

2. 应用的内存占用大大降低，不容易杀后台。

3. 应用不再自启，或被其它应用唤醒。

4. 系统也因此变得流畅省电。

不过凡事有利必有弊。部分应用在「全部禁用」后，会出现「白屏/闪退」等问题，可以根据这个 [《组件功能对照列表》](https://zhuanlan.zhihu.com/p/513280332?tdsourcetag=s%5Fpctim%5Faiomsg) 来「解禁对应组件」，或者直接「卸载重装」来让应用恢复正常。

##### [](\#如何禁用应用) 如何禁用应用

相比于禁用组件,「禁用应用」有更高的风险。很多人为了提升续航，会禁用一些「用不上」的系统程序。如果不小心把「核心」系统程序禁用了，设备就会卡开机无法进入系统，那就只能双清了。

因此「禁用应用」最好是参考别人的「禁用列表」，再根据自己的需求进行调整。毕竟每个人的需求不一样，例如有些人需要 Google 服务，有些人则不需要。这里我提供一个 [《安全禁用列表》](https://www.123pan.com/s/2xiAjv-AwzPh) ，参考自 [F-ckS-msung](https://github.com/rainbowflesh/F-ckS-msung/tree/main) 和 [OneUI-Debloat](https://github.com/pascua28/OneUI-Debloat) 。列表共计 100+ 禁用项，主要为 Samsung Services App、Link to Windows、Edge panels、Dex 等「非核心」系统程序，实测都可以安全禁用。

列表导入方式：主页 - 侧边栏 - 最爱 - 右上角三个点 - 恢复。禁用前务必「查看一遍」所有禁用项，「按需保留」应用程序，切勿无脑全部禁用。禁用有风险，小白需谨慎。以下是《禁用故障对照列表》。

禁用故障对照列表

  > Apps com.samsung.android.app.appsedge
  > 无法使用分屏多任务。
  > 启动器 com.sec.android.emergencylauncher
  > 无法使用省电模式。
  > 音质与音效 com.sec.android.app.soundalive
  > 无法开启全局杜比音效。
  > Samsung Core Services com.samsung.android.scs
  > 侧栏矩形截图，无法自动识别选择图片。联系人无法搜索，无法自选截图。
  > Samsung Multi Connectivity com.samsung.android.mcfserver
  > 无法使用多重连接，耳机无法随意切换。
  > Tethering com.google.android.networkstack.tethering
  > 打开软件点击无响应，设置 - 连接闪退。
  > Samsung Device Health Manager Service com.sec.android.sdhms
  > 打开三星设备健康闪退。
  > Settings Bixby com.samsung.android.app.settings.bixby
  > 无法使用三星云恢复备份。
  > Factory Test Provider com.samsung.android.app.providers.factory
  > 无法使用\*\#0\*\#。
  > SumeNNService com.samsung.android.sume.nn.servicePhoto Remaster Service com.samsung.android.photoremasterservice
  > 无法使用相册的重录。
  > DRParser Mode com.sec.android.app.parser
  > 无法使用相册重录，无法使用\*\#0\*\#。
  > Service Mode com.sec.android.app.servicemodeapp
  > 无法使用\*\#06\#。
  > Sec Media Storage com.samsung.android.providers.media
  > 无法截图，显示由于安全政策无法截取。
  > 网络管理器 com.google.android.networkstack
  > 无法使用移动网络。
  > VPN Dialogs com.android.vpndialogs
  > 无法使用 VPN。
  > 媒体 com.google.android.providers.media.module
  > 无法访问文件，内存里的文件。
  > Key Chain com.android.keychain
  > 无法打开安全与隐私 - 其他安全设置。
  > Sec Soter Service com.tencent.soter.soterserver
  > 微信无法使用，无法截图，无法录制视频。
  > 输入设备 com.android.inputdevices
  > 屏幕采样率下降，触控不跟手。
  > WLAN Test com.sec.android.app.wlantest
  > WiFi 无法重连。
  > 强制门户登陆 com.google.android.captiveportallogin
  > 无法登陆 Wi-Fi。
  > Global Post ProcMgr com.samsung.android.globalpostprocmgr
  > 拍照后相机打开预览图异常。
  > Tx Pwr Admin vendor.qti.data.txpwradmin
  > 快充失效。
  > 生物识别 com.samsung.android.biometrics.app.setting
  > 无法录入指纹。
  > 通话设置 com.samsung.android.app.telephonyui
  > 无法在状态栏切换 sim 卡和流量，设置里无法显示移动网络选项。
  > Ifaa Manager Application org.ifaa.aidl.manager
  > 无法使用支付宝指纹支付。
  > Sec Video Engine Service com.sec.sve
  > 语音通话无法唤起摄像头，从而导致卡省电 120 失败。
  > CMH Provider com.samsung.cmh
  > 相片重录完成保存时闪退。
  > Badge Provider com.sec.android.provider.badge
  > 短信无法显示小红点。
  > 三星键盘 com.samsung.android.honeyboard
  > 侧屏幕的剪切板无法使用。
  > Call BG Provider com.samsung.android.callbgprovider
  > 无通话背景。
  > Intent Resolver com.android.intentresolver
  > 分享闪退。
  > 三星文字转语音引擎 com.samsung.SMT
  > 手字笔输入无效。
  > 设置建议 com.android.settings.intelligence
  > 无法使用电池小组件。
  > Always On Display com.samsung.android.app.aodservice
  > 无法使用息屏提醒。
  > Container Service com.samsung.android.container
  > 蓝牙设置里，切换耳机降噪环境音功能消失。
  > Cell Broadcast Service com.google.android.cellbroadcastservice
  > 无法发送彩信，提示网络错误。
  > Sticker Center com.samsung.android.stickercenter
  > 相册编辑器闪退。
  > Handwriting Service com.samsung.android.sdk.handwriting
  > SPen 无法写字输入。
  > 三星文字转语音引擎 com.samsung.SMT
  > 无法使用语音转文字。
  > Factory Camera com.sec.factory.cameraFilter Provider com.samsung.android.provider.filterprovider
  > 相机滤镜的选择和添加异常。
  > Secure Element Application com.android.se
  > 钱包内公交卡余额相关异常。
  > App Linker com.sec.android.app.applinker
  > 角标失效。
  > TxPwrAdmin vendor.qti.data.txpwradmin
  > 快充失效。
  > Soter Sskds Service com.samsung.android.sskds
  > 微信无法开启指纹支付。
  > Spritewallipaper com.samsung.android.wallpaper.live
  > 桌面动态壁纸失效。
  > Samsung Editing Assets com.sec.android.app.ve.vebgm
  > 相册故事没声音。
  > 配套设备管理器 com.android.companiondevicemanager
  > 重新连接手表异常。
  > 壁纸服务 com.samsung.android.dynamicock
  > 锁屏状态下无法直接显示内容。
  > Android Shared Library com.google.android.ext.shared 智能建议 com.samsung.android.smartsuggestions
  > 无法自动识别并选定网址。
  > Bluetooth Pairing Request com.android.settings.bluetooth.BluetoothPairingRequest
  > 无法显示配对耳机弹窗。
  > Continuity Service com.samsung.android.mcfds
  > 无法使用多屏联动
  > 联系人存储 com.samsung.android.providers.contacts
  > 联系人功能异常。
  > 日历存储 com.android.providers.calendar
  > 无法创建新事件。
  > 密钥链 com.android.keychain
  > 无法打开安全与隐私 - 更多安全设置。
  > Shell com.android.shell
  > 无法打开 LSP。
  > 动态萌拍 com.samsung.android.aremoji
  > 通话背景失效。
  > Connectivity Overlay com.samsung.android.ConnectivilyOverlayConnectivity Ux Overlay com.samsung.android.ConnectivityUxOverlay
  > 无法连接 Spen。
  > Galaxy Editing Service ccm.samsung.android.globulpostprocmgr
  > 相机闪退。
  > 配置更新 com.samsung.android.cidmanagerDiagMon Agent com.sec.android.diagmonagentAdreno Graphics Drivers com.qualcomm.qti.gpudrivers.kalama.api33SumeNNService com.samsung.android.sume.nn.service
  > 耗电异常。

_列表来自酷安 @罗密欧与猪过夜_

##### [](\#安装教程) 安装教程

Lycan 是利用 Samsung Knox SDK 进行工作的，但是它无法直接获取 Knox 权限。Splashtop-Add-on-Samsung 和 Lycan 的包名一致，所以在系统看来，它们是同一款应用。所以先由 Splashtop-Add-on-Samsung 获取并激活 Knox 权限，再让 Lycan 来顶替它，从而「接管」已激活的 Knox 权限。整个过程就相当于「狸猫换太子」。

###### [](\#工具准备) 工具准备 [下载地址](https://www.123pan.com/s/2xiAjv-TStPh.html)

1. Lycan 安装包

2. Splashtop-Add-On-Samsung 安装包

3. Sam Helper

4. 炼妖壶

###### [](\#完整步骤) 完整步骤

  > * _**1\. 开放 Knox 权限**_
  > * 在「Sam Helper」中运行指令 `pm enable com.samsung.klmsagent`
  > * _**2\. 激活 Knox 权限**_
  > * 打开「炼妖壶」，建立「壶中界」
  > * 回到桌面，打开系统自带的「我的文件」
  > * 点击 Splashtop-Add-On-Samsung 安装包
  > * 打开方式选择 _**「工作」**_，不是选择「个人」
  > * 选择 _**「工作」**_ 中的「炼妖壶」安装
  > * 打开 Splashtop-Add-On-Samsung，按照提示激活 Knox 权限
  > * _**3\. 禁用 Konx 权限**_
  > * 在「Sam Helper」中运行指令 `pm disable-user com.samsung.klmsagent`
  > * _**4\. 接管 Knox 权限**_
  > * 找到桌面上的「炼妖壶设置」并打开
  > * 选择「彻底摧毁」，再选择「毁灭」
  > * 安装 Lycan，按照提示激活 Knox 权限

打开 Lycan 并授予权限，进入主页并显示所有应用，即为激活成功。_**如有异常情况，请看下方常见问题。**_

###### [](\#常见问题) 常见问题

  > * Lycan 显示 Error：Invalid package name \[ 204 / 301 \] ？
  > * 应用未安装：软件包似乎无效 ？
  > * 应用未安装：软件包与现有软件包存在冲突 ？
  > * 炼妖壶显示：INSTALL\_FAILED\_UPDATE\_INCOMPATIBLE ?

在设置中搜索「设备管理应用程序」，取消 Splashtop-Add-On-Samsung 或 Lycan 的授权并卸载。再运行指令 `pm uninstall com.splashtop.streamer.addon.knox`。最后按照教程从头再试一次。

1. 主页不显示所有应用？

重启设备即可。

2. OneUI 6.1 能安装吗？

可以，本教程适用于 OneUI 1.0 \~ 6.1。

3. 需要一直挂在后台吗？

不需要。

4. 可以加入深度休眠吗？

可以。

5. 怎么卸载？

侧边栏点击卸载，选择「不保留数据」。

6. 卸载后会怎么样？

所有的应用和组件都会解禁。

7. 会导致 Knox 熔断，或者影响系统安全吗？

不会，没有任何影响。

8. 更新系统前，要解禁所有应用吗？

可以不用。即使是大版本更新，实测也没有影响。

9. 炼妖壶不支持「Android 工作资料」特性？

改用「安全文件夹」进行安装。

##### [](\#使用方法) 使用方法

![图片](/images/loading.svg)

* **禁用应用**：主页 - 点击应用「图标」- 点击左下角 `Enable` 解禁或 `Disable` 禁用（右上角可全选）

* **禁用组件**：主页 - 点击应用「名称」- 选择四大基本组件 - 点击组件「图标」- 点击下方 `Enable` 解禁或 `Disable` 禁用（右上角可全选）

* **添加收藏**：主页 - 点击应用「图标」- 点击右下角的爱心 - 选择默认文件夹，或创建新文件夹

* **导入/导出应用禁用方案**：主页 - 侧边栏 - 最爱 - 右上角三个点 - 备份/恢复

* **导入/导出组件禁用方案**：主页 - 侧边栏 - 历史记录 - 右上角三个点 - 备份/恢复

![图片](/images/loading.svg)

##### [](\#救砖思路) 救砖思路

凡事都有意外。如果真的不小心禁错了系统程序，然后「设备变砖」了怎么办？我自己没遇到过，但可以分享一个救砖思路 ，仅供参考。如有错误，还请指正。

###### [](\#前提知识) 前提知识

* Lycan 是开机自启，它在设备开机时才会执行禁用。

* 卸载 Lycan 后，可以「取消」对所有软件的禁用。

通过这两点，可以想到一个救砖办法，就是在系统处于「关闭状态」时卸载 Lycan，**也就是在 recovery 界面通过 ADB 指令卸载 Lycan。**

###### [](\#操作步骤) 操作步骤

![图片](/images/loading.svg)

1. 关机后按住「电源键」和「音量 + 键」，同时用数据线连接电脑，进入 `recovery` 界面。

2. 下载安装 [「搞机工具箱」](https://jamcz.com/gjgjx/) 后打开。

3. 查看手机在 `recovery` 界面是否与「搞机工具箱」成功连接。

4. 未连接则选择 `Apply updata from ADB` ，再次尝试连接。

5. 连接成功后，在「软件管理」页输入 Lycan 的软件包名 `com.splashtop.streamer.addon.knox`

6. 点击「清除数据」「禁用」「卸载」。

7. 理论上即可成功进入系统。

#### [](\#Adhell3-广告拦截篇)Adhell3 广告拦截篇

![图片](/images/loading.svg)

Adhell3 也是一款专属于三星设备的应用，中文翻译为「广告地狱」，顾名思义其主打功能为「去广告」。它最初是由三星开发者 FiendFyre 开发，后因一些原因被迫下架。随后推出了 Adhell2，但在一段时间后也停止了服务。直到 2017 年 Adhell3 才出现。

它的工作原理是利用 Samsung Knox SDK 阻止「广告域」，因此它只适用于三星设备。它是 Samsung Knox SDK 的一个前端，会把你的规则设定（阻止的域、防火墙规则、白名单等）写入 Knox，因此它本身不需要在后台运行。

Adhell3 共有四大功能，分别是域规则、防火墙规则、应用管理器和组件管理器。除了拦截广告，Adhell3 还可以自定义「防火墙规则」来拦截特定应用程序的指定端口，限制应用的网络连接，以及禁用应用程序和应用组件等。

##### [](\#四大功能) 四大功能

* **域规则**：通过订阅「去广告 host 源」或者添加「本地 host 文件」，Adhell 能够拦截对应的「广告域」，从而达到去广告的效果，包括但不限于 App 内的开屏、信息流、弹窗广告等。

* **防火墙规则**：控制应用的移动数据 / Wi-Fi 联网。自定义防火墙规则。例如通过添加 com.android.chrome|\*|53 来阻止所有 IP 地址的端口为 53 上的 Chrome 应用程序的广告。

* **应用管理器**：禁用系统应用程序。

* **组件管理器** ：禁用 App 的权限与四大基本组件。

###### [](\#常见问题-1) 常见问题

1. 作用范围 ？

在整个系统范围内阻止广告。

2. 耗电异常 ？

Adhell 不会在后台运行，因此它本身不耗电。耗电异常的原因是，部分应用的广告被拦截后，在后台不断反复请求。

3. 与 Adguard 的区别 ？

Adguard 运行时会占用 VPN 通道，此时会无法开启 VPN。而 Adhell 并不占用，因此可以同时开启。

4. Adhell 和李跳跳有什么区别 ？

Adhell 是通过切断网络来「阻止广告加载」，李跳跳是在广告加载成功后「帮你点击跳过」。两者可以共存，起到互补作用。

5. 有 Adhell 还需要 Lycan 吗 ？

Adhell 没法批量禁用，只能一个个手动点击，非常不方便，而 Lycan 可以。因此更推荐使用 Lycan 来禁用。

6. 推荐 host 订阅源 ？

[Ad hosts](https://github.com/otobtc/ADhosts) 、[AdBlock DNS Filters](https://github.com/217heidai/adblockfilters)

7. 无法更新订阅源 ？

请开启 VPN 代理。

8. 弄完怎么还有广告 ？

本来就无法保证 100% 拦截广告。广告拦截效果是由你添加的 host 订阅源决定的，而 host 订阅源无法收集到网络中的「所有广告域名」，因此有些漏网之鱼是正常现象。

9. 规则越多越好？

规则越多，加载规则的时间越长，上网延迟也越高，甚至还有可能导致设备「无限重启」。因此适量即可。

###### [](\#注意事项) 注意事项

1. 不建议开启「防火墙规则」。开启后电信卡只能流量上网，无法「接打电话」和「收发短信」，其它运营商请自测。

2. Adhell 与 Clash 同时开启会导致「设备断网」，替代方案为 V2rayNG。

3. 开启「域规则」后，设备的热点会无网络，暂时无解。

4. 被拦截后容易「反复请求」的三个常见广告域，建议把这些域名「手动输入」到「作用域」页的「应用白名单」，否则会耗电异常。

`errlog.umeng.com` 错误日志

`dataflow.biliapi.com` 数据流

`loggw.alipay.com.cn` 日志网关

5. 不建议开启「应用」页的「应用白名单」，否则加载域规则的时间将「超级加倍」。比如正常情况下加载 50 w 规则可能需要 10 分钟，开启 1 个应用白名单后，加载时间会变成 20 分钟，开启 2 个就是 30 分钟，以此类推。

##### [](\#安装教程-1) 安装教程

Adhell3 和 Lycan 的工作原理一样，都是利用 Samsung Knox SDK 进行工作的。原理同上，整个过程就相当于「狸猫换太子」，不再赘述。

###### [](\#工具准备-1) 工具准备 [下载地址](https://www.123pan.com/s/2xiAjv-TStPh.html)

1. Adhell3 安装包

2. NotifyRDS-Add-On-Samsung 安装包

3. Sam Helper

4. 炼妖壶

###### [](\#完整步骤-1) 完整步骤

  > * _**1\. 开放 Knox 权限**_
  > * 在「Sam Helper」中运行指令：`pm enable com.samsung.klmsagent`
  > * _**2\. 激活 Knox 权限**_
  > * 打开「炼妖壶」，建立「壶中界」
  > * 打开「我的文件」，点击 NotifyRDS-Add-On-Samsung 安装包
  > * 打开方式选择 _**「工作」**_，不是选择「个人」
  > * 选择 _**「工作」**_ 中的「炼妖壶」并安装
  > * 打开 NotifyRDS-Add-On-Samsung，按照提示激活 Knox 权限
  > * _**3\. 禁用 Konx 权限**_
  > * 在「Sam Helper」中运行指令：`pm disable-user com.samsung.klmsagent`
  > * _**4\. 接管 Knox 权限**_
  > * 找到桌面上的「炼妖壶设置」并打开
  > * 选择「彻底摧毁」，再选择「毁灭」
  > * 安装 Adhell3，按照提示激活 Knox 权限

按提示授予权限后，进入主页即为激活成功。显示「激活证书」弹窗即为激活失败，从头再试一次。

##### [](\#替代方案) 替代方案

Adhell3 从 2017 年至今已经「年久失修」，在 OneUI 升级到 6.0 后又增加了不少 bug，本人已经不再使用。但是广告拦截的方式不止一种，除了鼎鼎大名的 AdGuard 以外，我再分享两个简单的替代方法。

###### [](\#DNS-广告拦截)DNS 广告拦截

设置中搜索「私密 DNS」，选择「私密 DNS 主机名」，输入 `adprodnsali.trli.club` 后保存即可。DNS 来自@[冷漠](https://blog.trli.cloudns.biz/article/000003/index.html) ，大佬更新很勤快，有问题可以向他反馈。

###### [](\#ACL4SSR-广告拦截规则)ACL4SSR 广告拦截规则

![图片](/images/loading.svg)

进入 [订阅转换页](https://acl4ssr-sub.github.io/) ，如图进行「订阅链接转换」。原理是在你的 VPN 订阅链接里添加 ACL4SSR 广告拦截规则，它仅在代理开启时生效。

#### [](\#总结) 总结

![图片](/images/loading.svg)

刚开始写这篇文章，只是想在 OneUI 6.1 更新之前，捋一遍新系统的设置流程，方便自己刷机后进行恢复。结果花了好几天，写完一看都 1w+ 字数了，毕业论文都没这么长。所以就整理成「优化指南」的形式，分享给各位网友作为参考。

那么关于整篇指南的主旨，想要「提升设备的续航与流畅度」，其实并不需要文中那么多花里胡哨的操作。如果你是以「玩机」为目的，那你确实可以跟着全部做一遍。但是对于大多数人来说「日用」才是关键，这些操作可能已经远远超纲了。

通常你只需要完成「应用安装篇」和「系统设置篇」就可以达到很不错的续航和流畅度了，不需要再折腾禁用什么的，这些收益已经不大了（类似 [边际效应](https://baike.baidu.com/item/%E8%BE%B9%E9%99%85%E6%95%88%E5%BA%94/555439) ）。

**最后给六个篇章的「流畅省电效果」排个名。**

**应用安装篇 > 系统设置篇 > 双清刷机篇 > shizuku 应用篇 ≈ Lycan 禁用篇 > Adhell3 广告拦截篇**

如果觉得本指南对你有一些帮助，欢迎赞助我一杯奶茶💰，我也可以为你解答相关问题。
