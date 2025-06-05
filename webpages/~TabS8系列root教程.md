---
created: 2024-08-11T12:00:00
source: https://www.coolapk.com/feed/42938913?shareKey=NjYxY2Q4ZDhiMDNlNjZiNzhlNDg~
type: archive-web
modified: 2025-01-15T11:38:15
---

TabS8 系列 OneUi5.0 国行版刷入 TWRP 第三方 Recovery 与解锁 system 系统分区获取完全版 root 教程

⚠️警告：国行版解锁手机会导致失去官方保修，Knox 物理熔断不可逆，操作前请慎重！！ 放在开头：本教程适用于所有三星 OneUi5 国行设备，但文末的文件只适用于 tabs8 系列，请使用对应的文件刷机。 众嗦粥汁，OneUi5 国行刷第三方 TWRP 和 root 都会卡开机引导页面，激活失败显示：-45。为了解决这个问题所有了此教程。有两个方法，本教程着重介绍的是 TWRP 法。 一．TWRP 法： 1.前期准备： 1）退出三星与谷歌账号。 2）OEM 解锁：关于平板电脑>软件信息>编译编号连点七下，开启开发者选项，打开 OEM 解锁选项，解锁会清除所有数据。 2.进入下载模式： 数据线连接平板与电脑，长按强制关机侧键组合：音量减键＋关机键，关机状态下按住侧键：音量减键 + 音量加键进入下载模式。进入成功后 Odin 左上角会变蓝。 3.重装或更新系统：

如果无需重装或更新系统可以跳过此步骤，本机型固件下载地址为:[查看链接](https://samfw.com/firmware/SM-X800/CHN)，其他机型固件也可以此 samFW 网站上下载。PS：如果要降级需要注意固件包的基带版本号的倒数第五个数字，数字相同才能互刷，否则 odin 会显示刷机失败。例如：这里新版为 3，旧版本为 2 就会降级失败。如图所示：

![](http://image.coolapk.com/feed/2023/0202/05/3047752_f880a9ca_5987_3045_875@1589x233.png.m.jpg)

解压 Odin3\_v3.14.4.rar 并打开，解压下载好的固件压缩包，Odin 的 BL 槽位选择解压好的固件包 BL 开头文件，AP 槽位选择以 AP 开头文件，CP 槽位选择以 CP 开头文件（WiFi 版本没有的不用选），不同的是 CSC 槽位，要保留数据比如系统升级请选择以 HOME\_CSC 开头文件不会清除数据，否则选择 CSC 开头文件会清除数据。文件放入对应槽位后点击 Start，开始进行重装或更新系统。

![](http://image.coolapk.com/feed/2023/0202/05/3047752_86e9daa8_5987_3056_850@1310x951.png.m.jpg)

4.Odin 刷入 twrp 和 vb：

平板进入下载模式后，把 Odin 里的 options 选项取消勾选 Auto reboot（防止太快重启不利于下一步操作），TWRP 文件（以我自己的机型为例是 twrp-3.7.0\_12-1\_afaneh92-gts8p .tar）放入 ap 槽位，去 vb 验证文件 vbmeta\_disabled\_R.tar 放入 USEDATA 槽位，点 Strat 刷入，odin 上显示 pass 即为完成。

![](http://image.coolapk.com/feed/2023/0202/05/3047752_e73ecccd_5987_3063_48@1312x950.png.m.jpg)

5\. 进入恢复模式： 按侧键组合强制关机，再马上进入长按侧键组合进入恢复模式：音量加键＋关机键。刷入 TWRP 后开机必须进入恢复模式，否则直接进系统会掉 TWRP，导致需要重新进行 4 操作。 6.解锁 system 分区并清除 Data 数据： 进入 TWRP 后，点 Install 刷入 rw 文件 afaneh92\_lp\_rw\_tool\_v0.4.zip，等待完成后，返回主页选择 Wipe > Format Data 输入：yes ，抹除数据（第一次需要抹除全部数据，后续升级系统时你则只需要重刷一次此方法并跳过抹除数据，实现带数据升级）。完成后返回首页选择 Reboot >recovery，重启 TWRP。 7.TWRP 刷入文件： TWRP 内点 Install 刷入内核文件 waipio-gki\_kernel\_5.10.81-afaneh92-gd8d6af 75 19 72\_2022\_11\_08 .zip（缺少将无法正常开机）、激活免检验模块一 multidisabler\_A13\_OneUI5.zip、magisk 文件 22790980-delta.zip。

8.点击 Reboot system 重启系统，享受。

![](http://image.coolapk.com/feed/2023/0202/05/3047752_15dd2467_5987_307_70@2800x1752.jpeg.m.jpg)

二．修补 AP 法： 有人不喜欢 TWRP 刷自定义内核或觉得过于复杂，可以用使用 magisk 修补 ap 的旧方法。论坛里有很多此类教程，我这里就不多加赘述。完成所有操作后，在欢迎的引导引导界面点击辅助功>TalkBack>设置>盲文键盘>设置盲文键盘>; GBoard，利用超链接跳转到浏览器，输入下面网 址 下载 magiskAPP（zip 压缩包修改后缀为.apk 即可）和激活免检验模块二 samsung-activation-bypass-v2.zip（注意此模块与上面的刷 TWRP 教程里的激活免检验模块一不同），使用 magiskAPP 刷入模块并重启系统，即可正常激活完成 root。

本教程相关的刷机文件下载地址（请下载与自己机型适配的文件）：

[\[链接\]三星平板tbs8系列文件](https://wwmm.lanzoub.com/b047ny38f)

密码:2mme

如果本教程帮助了你，请不要吝惜你手中的![酷币](http://static.coolapk.com/emoticons/v9/c_coolb.png)![酷币](http://static.coolapk.com/emoticons/v9/c_coolb.png)(●’◡’●)。

[#OneUI5.0#](/t/OneUI5.0?type=12) [#三星GalaxyTabS8#](/t/三星GalaxyTabS8?type=12) [#三星GalaxyS22Ultra#](/t/三星GalaxyS22Ultra?type=12)
