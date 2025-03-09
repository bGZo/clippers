---
created: 2024-08-17T12:00:00
source: https://www.coolapk.com/feed/53702265?shareKey=OGJlNWI1MjRiZDFkNjZiZTE5MjM~&shareUid=2988517&shareFrom=com.coolapk.market_14.3.0
type: archive-web
modified: 2025-01-15T11:38:15
---

这几天抓包才发现，自己原先安装的证书都不管用了，上网一查才知道系统升级成安卓 14 后，根证书路径从系统目录/system/etc/security/cacerts 变成/apex/com.android.conscrypt/cacerts 了，原系统目录证书依然存在。 以下是找到一些参考资料：

1、New ways to inject system CA certificates in Android 14：[查看链接](https://httptoolkit.com/blog/android-14-install-system-ca-certificate)

2、AdguardCert：[查看链接](https://github.com/AdguardTeam/adguardcert/blob/master/module/post-fs-data.sh)

3、wu 大微博：[查看链接](https://m.weibo.cn/status/Ni21tFiR9?jumpfrom=weibocom) 基本原理就是资料 3 微博中所说的，用 mount bind 命令覆盖 apex 目录。 而资料 1 和资料 2 给出的脚本更完善些，对于脚本中的使用 nsenter 命令那一段，貌似不用也可以。 我按照资料 2 中 AdguardCert 的 post-fs-data 脚本也写了一个，没有把证书模块和针对 Android14 特殊处理的脚本写到一起。大致逻辑为：Android13 及以下的设备依然按照之前刷证书模块的方式，把证书文件挂载到/system/etc/security/cacerts，而对于 Android14，每次开机额外执行一个脚本，负责把/system/etc/security/cacerts 的证书覆盖到/apex/com.android.conscrypt/cacerts。 HttpCanary 证书安装：

HttpCanary-v3.3.6 安装包：[查看链接](https://www.123pan.com/s/na6DVv-TBy53.html) 提取码：N0Bj

先安装 App，这个修改版的没有启动验证，因为原作者不维护了，正版用户也打不开原版了，只能用这个修改版的。 安装完成后，需要完成初始设置，并在设置中尝试导入根证书（会失败），这步主要是为了在/data/data/com.guoshi.httpcanary.premium/cache/目录生成证书，然后安装这个模块：

HttpCanaryRootCA：[查看链接](https://www.123pan.com/s/na6DVv-vBy53.html) 提取码：qTlS

模块内不含证书，而是拷贝/data/data/com.guoshi.httpcanary.premium/cache/目录下的证书至模块目录，另外完成一些其他设置，下次开机将自动挂载证书至/system。 Reqable 证书安装：

先安装 App 和辅助服务，可在 Play 商店下载，或到 Reqable 官网：[查看链接](https://reqable.com/zh-CN/) 下载。

安装完成后，需要完成初始设置，然后打开菜单 ->证书管理 ->导出根公钥证书 (.0)，此时会在/storage/emulated/0/Download/Reqable/生成所需的证书文件（文件名形如 12f056ab.0），值得一提的是，黄鸟的根证书的拥有者信息哈希值（subject\_hash\_old）都是相同的（87bc3517），Reqable 对不同设备以及清除数据、重新安装都会生成不同的证书，其 subject\_hash\_old 值也不一样，如果有人做的模块/脚本把证书文件名写死，那别人装了就会不生效。 确保已经正确导出证书后，安装这个模块：

ReqableRootCA：[查看链接](https://www.123pan.com/s/na6DVv-dBy53.html) 提取码：VIAr

模块内不含证书，而是拷贝/storage/emulated/0/Download/Reqable/目录下的证书至模块目录，下次开机将自动挂载证书至/system。 针对 Android14 的额外处理脚本：

CA-overlay-for-A14.sh：[查看链接](https://www.123pan.com/s/na6DVv-oBy53.html) 提取码：DBQg

下载上述脚本，需每次重启后手动执行一次（使用系统环境、root 权限执行），或者拷贝到/data/adb/service.d/目录下，并授予执行权限，每次开机将自动执行。

此脚本的每次执行日志保存在/data/local/tmp/CA\_mount.log 文件中。

![](http://image.coolapk.com/feed/2024/0218/19/3153203_dc0acbc2_4830_3259_690@1080x2400.jpeg.m.jpg)

其他注意事项：使用 windows 电脑编辑脚本后，换行符可能被更改，不能直接在手机上运行，可用 MT 管理器的文本编辑器打开，然后选择 右上角三个点 ->文件 ->换行符 ->Unix-like(LF)，然后保存。

![](http://image.coolapk.com/feed/2024/0218/19/3153203_d07ec28b_4830_3269_968@1080x2400.jpeg.m.jpg)
