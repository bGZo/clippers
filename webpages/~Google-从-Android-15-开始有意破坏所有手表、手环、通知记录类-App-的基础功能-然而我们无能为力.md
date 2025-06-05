---
title: "Google-从-Android-15-开始有意破坏所有手表、手环、通知记录类-App-的基础功能-然而我们无能为力"
created: 2025-03-24T21:32:16
modified: 2025-03-24T21:32:21
source: "https://www.v2ex.com/t/1080973#reply14"
tags:
tags-link:
type: "archive-web"
---

我是通知滤盒的开发者，相信这个 App 在 V2EX 已经够有名了就不再给自己硬广了。

最近时不时收到用户反馈，通知滤盒里的部分通知内容变成了「已隐藏敏感通知内容」。 研究原来是 Android 15 开始 Google Protect 加了个所谓隐私防护措施，对可能含有 OTP 验证码的通知直接隐藏内容 [https://www.theverge.com/2024/5/15/24157547/android-15-will-hide-one-time-passwords-in-notifications](https://www.theverge.com/2024/5/15/24157547/android-15-will-hide-one-time-passwords-in-notifications)

这件事怎么看怎么透露一股草台班子的味道。

首先是实现方式：Google 采取的是硬编码替换字符串的实现，也即，第三方 App 收到的文本内容变成了「隐藏敏感通知内容」或 “Sensitive notification content hidden” 或其他语言。这给用户带来了极大的视觉误导，第一反应都以为是第三方服务隐藏的，而非系统所为。

同时，硬编码，而非增设某种 API 的方式，也极大地给开发者适配制造了麻烦，除了硬编码几十种语言的对应文案外，开发者没有正常的方法得知某条通知内容是否被隐藏。

然后，这直接颠覆性破坏了各类手环手表、通知历史、验证码提取类工具的使用场景。 [https://www.reddit.com/r/android\_beta/comments/1f9plr8/sensitive\_notification\_content\_hidden/?rdt=58980](https://www.reddit.com/r/android_beta/comments/1f9plr8/sensitive_notification_content_hidden/?rdt=58980) 这样的 breaking change ，在 Google 的 Android 15 behavior change 里压根没有提及。

最后，这个功能不仅产品逻辑草台班子，程序实现同样也很草台。根据实机数据反馈，高德、抖音、微博，甚至小米商城的营销、推送都被识别为了含验证码的敏感内容。

![](https://i.v2ex.co/5HN33Vq9.jpeg)

我只能说那个啥都没你 Google 敏感。
