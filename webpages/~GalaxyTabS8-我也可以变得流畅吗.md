---
created: 2024-08-05T12:00:00
source: https://www.coolapk.com/feed/55898308?shareKey=NTZlMmRhYzg2NDk0NjZiMGVmZWU~
type: archive-web
modified: 2025-01-15T11:38:15
---

tags: #samsung

众嗦粥汁，平板上的 oneUI 功能丰富，可最最基础的系统流畅度却依旧开摆。恰巧遇上自家半导体犯病，这代平板的日用体验堪称灾难。（很难不联想到某 UI12.5![白眼](http://static.coolapk.com/emoticons/v9/coolapk_emotion_84_baiyan.png)） 面对这样一台用着旗舰芯片却难以确保日用流畅度的机器，必须重拳出击！👊🏻 本文将围绕系统服务、Kernel SU 模块、GPU 降压超频和 Femind 进行优化，所有文件打包放在文末

我们开始！！![哼唧](http://static.coolapk.com/emoticons/v9/coolapk_emotion_1011_hengji.png)

  - 🔴注：

① 文章内所有操作均基于 Kernel SU 进行，未刷入 Kernel SU 内核请参照官方指南和站内其他教程刷入

[\[链接\]安装 | KernelSU](https://kernelsu.org/zh%5FCN/guide/installation.html)

（Kernel SU 通用内核会使机器无法读取 SD 卡，权衡利弊自行考虑） ② 选择 Kernel SU 主要是因为解锁系统分区的模块需用 KSU 才能使用，且官方内核可能与 ZRAM 模块冲突。这边建议放弃 SD 卡换取强一大截的后台保活能力 ③ 该教程仅在 Tab S8 测试可用，其他机器酌情参考 ④ 刷机千万条，备份第一条。「数据无价⚠️谨慎操作」 🪄第一步，处理系统服务✨ 1\. 关闭设置项 🔴路径基于 oneUI 6.1，其他系统版本请自行查找并善用搜索 ① 设置 - 设备维护 - 内存 -RAM Plus ② 设置 - 安全与隐私 - 更多隐私设置 - 发送诊断数据、Android 个性化服务、使用情况和诊断信息 ③ 设置 - 安全与隐私 - 应用程序安全性 - 应用程序保护、Google Play Protect ④ 设置 - 主屏幕 - 将媒体页面添加至主屏幕 ⑤ 设置 - 主屏幕 - 在主屏幕中搜索 ⑥ 设置 - 主屏幕 - 锁定主屏幕布局（开启！！开启！！） ⑦ 设置 - 锁定屏幕 - 安全锁定设置 - 用侧键立即锁定、锁定网络和安全 ⑧ 设置 - 锁定屏幕 - 小组件 - 全部关闭 ⑨ 设置 - 高级功能 - 每日看板 ⑩ 设置 - 显示 - 自动息屏 - 查看时保持屏幕开启 ⑪ 设置 - 电池 - 后台使用设置 - 右上角三个点 - 自适应电池 建议把设置翻一遍底朝天，能不用的尽量不用，能关的尽量关 2\. 冻结系统应用

我用的 Thanox，活检解冻非常方便，同时管理自启，后台和划卡即停

![](http://image.coolapk.com/feed/2024/0515/18/1696628_9713e5eb_7394_4946_0@1369x6055.jpeg.m.jpg)

有点多，耐心一下\~

注：使用三星浏览器请不要禁用 Samsung Pass，否则白屏卡死 3\. 下载 SamHelper，在 Lock & Labs 找到 APP Booster，下载安装，每月运行一次 4\. 替换 oneUI 桌面。（注：oneUI 6.1 用户可略过） 复制 TouchWizHome\_2017.apk 文件至/system/priv-app/ 极大缓解手势进入最近任务掉帧 需刷入 overlayfs-release\_3.2.2.zip 模块使 system 目录可写

5\. KSU 刷入 HMSCore，安装 HMS Push，可以在没有后台的情况下接收推送。具体参见

[\[链接\]@bkmioa的图文...](https://www.coolapk.com/feed/37685586?shareKey=N2NhMzVjNmNjOGNmNjY0NDgwMTM~&shareUid=1696628&shareFrom=com.coolapk.market%5F14.1.1)

8G 内存寸土寸金，用在刀刃上 6\. 替换默认安装器为 InstallerX。打开 IntallerX- 设置 - 授权器 -Root 超级用户 - 锁定为默认安装器。安装速度比官方快且美观 🎉系统服务部分到此结束🎉 🪄第二步，安装 Kernel SU 模块并配置✨ 🔴这一步是最重要的，主要是干掉三星的温控并增强后台留存能力。将所有模块安装完毕，以下模块需要配置 ① 超强保后台 刷入前关闭 RAM Plus，否则开机过一会死机 复制 swap\_controller 文件夹至/data/adb/modules 复制 swap.conf 文件至/data/abd/swap\_controller 注：若使用官方内核可能引起一段时间后参数被更改的问题 ② A1- 内存管理 memory.json 至/data/adb/modules/Hc\_memory/config 复制名单列表.conf 至/storage/emulated/0/Android/HChai ③ Qualcomm Devices GPU/DDR Thermal Wall 修改/data/skai/thermal.conf 文件可再次提高 GPU 温度墙上限，我设置的 115℃，最高可跑 103℃ 🚫不建议改得太高 ④ Scene 附加模块 在 Scene 功能页 - 附加模块中修改 service.sh 文件添加以下代码，可解锁 CPU 温度墙至 110℃ sleep 1 echo 110000 > /sys/class/thermal/thermal\_zone29/trip\_point\_4\_temp echo 110000 > /sys/class/thermal/thermal\_zone30/trip\_point\_4\_temp echo 110000 > /sys/class/thermal/thermal\_zone31/trip\_point\_4\_temp echo 110000 > /sys/class/thermal/thermal\_zone32/trip\_point\_4\_temp echo 110000 > /sys/class/thermal/thermal\_zone33/trip\_point\_4\_temp echo 110000 > /sys/class/thermal/thermal\_zone34/trip\_point\_4\_temp echo 110000 > /sys/class/thermal/thermal\_zone35/trip\_point\_4\_temp echo 110000 > /sys/class/thermal/thermal\_zone36/trip\_point\_4\_temp echo 110000 > /sys/class/thermal/thermal\_zone37/trip\_point\_4\_temp sleep 1 chmod 0440 /sys/class/thermal/thermal\_zone29/trip\_point\_4\_temp chmod 0440 /sys/class/thermal/thermal\_zone30/trip\_point\_4\_temp chmod 0440 /sys/class/thermal/thermal\_zone31/trip\_point\_4\_temp chmod 0440 /sys/class/thermal/thermal\_zone32/trip\_point\_4\_temp chmod 0440 /sys/class/thermal/thermal\_zone33/trip\_point\_4\_temp chmod 0440 /sys/class/thermal/thermal\_zone34/trip\_point\_4\_temp chmod 0440 /sys/class/thermal/thermal\_zone35/trip\_point\_4\_temp chmod 0440 /sys/class/thermal/thermal\_zone36/trip\_point\_4\_temp chmod 0440 /sys/class/thermal/thermal\_zone37/trip\_point\_4\_temp

（我的附加模块不生效，各位有兴趣可以试试）

![](http://image.coolapk.com/feed/2024/0515/18/1696628_3fc4bf6b_7394_4953_220@2560x1600.jpeg.m.jpg)

有大佬整出来的话请浇浇（

🎉模块部分到此结束🎉 🪄第三步，GPU 降压超频✨ 自用 8 Gen 1 的 KonaBess 配置： konabess://H4sIAAAAAAAAAMXT3UrDMBQH8FcZ8XaFJG3XzI8hPkdB8nHaBbKua5wbjr276VQW9aTglReF8D9JzvkReiJ6bXtySw7S9nb77G3XOniyHZkTA16HSlg1A+zCaqe3m3nb77P+MDh4Bednp7q7kcYM4H2mwYXkYXZPj2x1FwrevkGc0jENd/TyxSoHIayRO2sSdv2KH+nYa4D2ctUq3jJO99Egp5opKq7ly9HPkeg1VnsfnVLf8o3t0Fgef8ZSmyxqIATXZdOYsX5GCSwisASBa1WwCics/13AIwFPCSpoFjkuKFMCiQuWfxRIwc20II8EeUrAFhQ0RQVFSlDhghIXyIk3gGlBEQmKhIBpmkuW+hESAo4LGC4QXxOOHzm/A24dlPhJBAAA 各 CPU 体质不同，若出现雪花屏可以适当降低 470 和 560 两档的频率

附上 [@CKXTAX](/u/CKXTAX) 大佬测出来的极限压榨图

![](http://image.coolapk.com/feed/2024/0515/18/1696628_db99b75a_7394_4956_35@1261x241.png.m.jpg)

🎉GPU 降压超频部分到此结束🎉 🪄第四步，Femind✨ 🔴Femind 模块中安装 busybox 模块，伪装温度和 oneUI 负优化拜拜。建议安装前仔细反复阅读说明 ① 伪装温度仅开启「移除 Linux 设备降温保护」中的处理器项，破掉 CPU 高于 95℃重启的温度墙。不要修改上面的电池、处理器，会锁 85℃墙 ② oneUI 负优化拜拜选择全部屏蔽，解除高温降频选择开机自启。系统的后台管理会被干掉，可用 Thanox 接管。游戏模式的息屏挂机存活 ③ 我自己用的 Femind 满血调度，感觉和没有调度的状态没什么区别，都是放开了跑。这边不建议使用 Scene 的调度，HP 锁 GPU 最低频率，吟惋兮充电时锁 CPU 频率 🎉Femind 部分到此结束🎉 🎉🎉🎉恭喜你已经解锁 Galaxy Tab S8 完全体，快跑个分庆祝一下吧\~🎉🎉🎉

写在最后![不开心](http://static.coolapk.com/emoticons/v9/coolapk_emotion_108_bukaixin.png)

所谓优化，我想让一切有序，化繁为简，顺理成章。所以如果有多个同类型的方案，我会一个个测试，确保不重复，不养蛊，不让 bug 之间互相掐架。上述方案是一星期高强度测试得出的结果，各位尽管放心抄![可爱](http://static.coolapk.com/emoticons/v9/coolapk_emotion_5_keai.png)

另，以上所有方法和经验并非个人摸索，而是站内大佬共同构筑和分享的结晶\[针不戳\]。文章着重参考：

[\[链接\]@ZEROAROMA的动态...](https://www.coolapk.com/feed/55110171?shareKey=NmU0NTBlY2YyMTE5NjY0NDdmY2E~&shareUid=1696628&shareFrom=com.coolapk.market%5F14.1.1)

[\[链接\]@TEACT的图文...](https://www.coolapk.com/feed/53079106?shareKey=OGNiMmJkZmU5YmM4NjY0NDdmZGM~&shareUid=1696628&shareFrom=com.coolapk.market%5F14.1.1)

[\[链接\]@香香的门徒的图文...](https://www.coolapk.com/feed/46524119)

[\[链接\]@来自M78星云的Man的图文...](https://www.coolapk.com/feed/45976076?shareKey=ODMxMTc1MzhlOWU2NjY0NDdmZmU~&shareUid=1696628&shareFrom=com.coolapk.market%5F14.1.1)

感谢大佬们为社区做出的贡献🧡🧡

欢迎评论区晒出你们的作业！![耶](http://static.coolapk.com/emoticons/v9/coolapk_emotion_35_ye.png)![耶](http://static.coolapk.com/emoticons/v9/coolapk_emotion_35_ye.png)

下载链接：[查看链接](https://www.123pan.com/s/RULQjv-JtFV3.html)

提取码:5Tq8

把硬币交出来![不开心](http://static.coolapk.com/emoticons/v9/coolapk_emotion_108_bukaixin.png)![不开心](http://static.coolapk.com/emoticons/v9/coolapk_emotion_108_bukaixin.png)
-
