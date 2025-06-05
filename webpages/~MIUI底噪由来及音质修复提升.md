---
created: 2024-08-10T12:00:00
source: https://www.coolapk.com/feed/11091445?shareKey=MDY1MzFmYjAyMWRmNjZiNzhiYzk~
type: archive-web
modified: 2025-01-15T11:38:15
---

[#MIUI#](/t/MIUI?type=12) 首先，MIUI 祖传底噪来源是从什么时候来的呢？我还无法准确知道哪部小米手机的哪个 MIUI 版本开始的。

不过我也算是老早体验过增益和底噪的了，当时还用着第一部手机——红米 1s 移动 4G 版 (2014501)，清楚地记得某次 miui5 更新后，戴耳机听歌发现了明显增益，音量调到 4 级就过大，调到 3 级就太小，声音也很闷 (那时候用的耳机差没感受到底噪)。听歌只能靠米音提升一下听感，没深究

![](http://image.coolapk.com/feed/2019/0405/15/1220979_1554449448_0251@1080x2340.jpg.m.jpg)

底噪问题和解决方法的发现，是在我用小米 5 的时候，买了一个 170 左右的索尼耳机，晚上听歌发现明显底噪。受不了去网上论坛查底噪问题，发现这问题存在很久了。很快我就和当年红米 1s 的更新经历联想起来，猜测此为系统问题而非硬件。最终果然找到了问题根源及修复教程：[查看链接](http://www.miui.com/thread-10063200-1-1.html)

![](http://image.coolapk.com/feed/2019/0405/15/1220979_1554449859_0057@1080x2340.jpg.m.jpg)

理论教程适合所有 MIUI 系统，本质为 8 行代码缺失： 把 <ctl name="COMP1 Switch" value="0" /> <ctl name="COMP2 Switch"; value="0" /> <ctl name="HPHL Volume" value="11" /> <ctl name="HPHR Volume" value="11" /> 分别加到 <path name="headphones">和

<path name="headphones-44.1">里面去

![](http://image.coolapk.com/feed/2019/0405/15/1220979_1554449861_3499@1080x2340.jpg.m.jpg)

![](http://image.coolapk.com/feed/2019/0405/15/1220979_1554449863_6882@1080x2340.jpg.m.jpg)

重启手机就能发现耳机音量和底噪恢复正常水平

修复好后可能还想继续提升一下听感 (反正也解锁 root 了) 这时可以安装杜比音效或者蝰蛇音效，个人目前只体验过蝰蛇 HIFI [【VIPERFX 音效驱动 正式版 v2.5.0.5】](http://www.coolapk.com/apk/com.audlabs.viperfx)

安装也挺简单，普通的直接刷卡刷包，如果有 magisk 直接下载 zip 压缩包刷入。音效配置可以下载导入别人预置好的

![](http://image.coolapk.com/feed/2019/0405/15/1220979_1554449866_0204@1080x2340.jpg.m.jpg)

![](http://image.coolapk.com/feed/2019/0405/15/1220979_1554449868_2208@1080x2340.jpg.m.jpg)

![](http://image.coolapk.com/feed/2019/0405/15/1220979_1554449870_5682@1080x2340.jpg.m.jpg)

![](http://image.coolapk.com/feed/2019/0405/12/1220979_1554438462_2671@1080x2340.jpg.m.jpg)

最后![懒得理](http://static.coolapk.com/emoticons/v9/coolapk_emotion_107_landeli.png)，祖传底噪暂时消除，音效也提升了 可以的话也能买蓝牙耳机来 " 彻底消除 " 底噪，唯独游戏有延迟

至于小米官方到底修复不修复祖传底噪，会不会加入全局 dac。还只能持续观望。。。

![](http://image.coolapk.com/feed/2019/0405/15/1220979_1554449873_5507@3325x2494.jpg.m.jpg)
