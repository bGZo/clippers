---
title: "如何看待手机内存 RAM 容量疯长甚至有隐隐超过电脑通用 8G 的趋势？"
created: 2021-04-05T12:39:34
modified: 2021-04-05T12:39:34
source: https://www.zhihu.com/question/301805084/answer/656016081
tags:
tags-link:
type: archive-web
---
1. 10g 12g 手机的溢价很高。

2. 安卓的很多 app 几乎没有竞品。只推 features 而优化不足。

3. arm 库没有 x86 库的设计经验好。

4. 手机的交互实时性要求高，推异步和全状态全资源在 ram 是常见操作。加上 android 和 ios 还会监视主线程，在桌面上有些同步操作在手机上都定义为高开销。

5. CPU 弱鸡，和第四点结合，只好空间换时间。

6. app 普偏不用原生 ui ，高分辨率图形多，图形处理一直是内存大户。