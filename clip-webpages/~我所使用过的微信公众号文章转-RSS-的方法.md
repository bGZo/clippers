---
title: "我所使用过的微信公众号文章转-RSS-的方法"
created: 2025-01-16T08:39:13
modified: 2025-01-16T09:29:07
source: "https://www.zmonster.me/2020/04/17/wechat-articles-rss-solution.html"
tags:
  
tags-link:
type: "archive-web"
---

2020-04-17

## 目录

- [背景](https://www.zmonster.me/2020/04/17/#org2291282)
- [Huginn 简介](https://www.zmonster.me/2020/04/17/#orgadb6262)
- [基于搜狗微信搜索的方案](https://www.zmonster.me/2020/04/17/#org5dc36cf)
- [(已失效)基于即刻/快知和 RSSHub 的方案](https://www.zmonster.me/2020/04/17/#org3f4ef78)
- [基于 EFB 和 Telegram 的方案](https://www.zmonster.me/2020/04/17/#org0ab99c4)
- [其他参考方案](https://www.zmonster.me/2020/04/17/#org7aff131)
- [后记](https://www.zmonster.me/2020/04/17/#org19ab5b2)

## 背景

作为一个 RSS 重度用户，在 [微广场关闭](https://zhuanlan.zhihu.com/p/26638306) 前，我一直使用微广场来把自己想看的微信公众号、知乎专栏转成 RSS。在微广场关闭后，不仅是我，很多人也意识到了，类似的公开服务最终都可能走向同样的结局。在那之后，我就开始探索自己的方案，尝试不依赖第三方服务来把微信公众号转成 RSS。比较幸运的是，当时我已经接触到了 [Huginn](https://github.com/huginn/huginn)，[使用它](https://www.zmonster.me/2016/10/22/pkm-information-collection.html#orgheadline7) 来获取一些学术论文资讯，而我加入的一个 Huginn 交流群里，早就有人在做相关的尝试了。基于交流群中朋友分享的方案，我也开始使用 Huginn 来为公众号输出 RSS，在这三年时间里，我前后使用过的方案有下面这些：

1. 基于 [搜狗微信搜索](https://weixin.sogou.com/) 的方案
2. 基于即刻/快知和 [RSSHub](https://github.com/DIYgod/RSSHub/) 的方案
3. 基于 [EFB](https://github.com/blueset/ehForwarderBot) 和 Telegram 的方案

我将在后文中按顺序讲一下这三种方案。

当然，除了这三种方案外，也有一些门槛相对低的方案，不想折腾的人可能会更感兴趣一些，所以我会在文末也介绍一下这些方法。

## Huginn 简介

由于几个方案主要都是使用 Huginn 来实现的，这里简单介绍一下 Huginn。

![huginn.png](https://www.zmonster.me/assets/img/huginn.png)

[Huginn](https://github.com/cantino/huginn) 是一个 Ruby 编写的自动化工具，在理念上类似 IFTTT 和天国的 Yahoo! Pipes，即进行事件的监听然后根据预先设定的规则自动化地进行后续操作。

Huginn 的 wiki 上列举了一些典型的使用场景，如:

1. Never Forget Your Umbrella Again: 下雨提醒
2. Adding RSS Feeds to Any Site: 为任意网站生成 RSS 输出
3. Follow stock prices: 监听股票价格

在 Huginn 中，主要有 event 和 agent 两个概念，agent 类似 IFTTT 里的 channel，event 则是 agent 的输出。在 Huginn 中可以将一个 agent 的输出作为另外一个 agent 的输入，由此产生复杂的自动化操作。

![huginn_diagram.png](https://www.zmonster.me/assets/img/huginn_diagram.png)

上图来自 [Huginn:烧录RSS的神器](https://web.archive.org/web/20170315013204/http://www.jianshu.com/p/4a47e452abc9) 一文，该文对 Huginn 的使用做了很详细的介绍。

和 IFTTT 不同的是，Huginn 需要自己部署，很多细节需要自己定制，因此在使用门槛上会高很多。想尝试一下的话，可以参考 [文档](https://github.com/huginn/huginn#heroku) 一键免费部署 Huginn 到 PaaS 平台 [Heroku](https://heroku.com/) 上，轻度使用的话足够了。

本文的目的并不是专门介绍 Huginn，如果读者想了解更多关于 Huginn 的内容，可以自行搜索、阅读文档和相关资料。

## 基于搜狗微信搜索的方案

[搜狗微信搜索](https://weixin.sogou.com/) 是一个开放的网站，同时又能获取指定公众号的最新文章，所以就成了早期的公众号文章转 RSS 的重要工具。

在搜狗微信搜索中，如果知道一个微信公众号的 ID，可以直接拼接出该公众号在搜狗微信搜索上的页面，以“经济学人”的公众号举例，其公众号 ID 是 *TheEconomistGroup* ，那么其对应的搜狗微信搜索页面就是 [https://weixin.sogou.com/weixin?query=TheEconomistGroup](https://weixin.sogou.com/weixin?query=TheEconomistGroup) ，访问这个页面，可以看到如下内容：

![sogou_wexin_search.png](https://www.zmonster.me/assets/img/sogou_wexin_search.png)

从最下方的“最近文章”处就可以解析出该公众号最新文章的标题和链接，因此基于搜狗微信搜索的方案，通过下面几个步骤来得到公众号的 RSS 输出：

1. 解析公众号的搜狗微信搜索页面，获取最新文章的标题和链接
2. 访问文章的链接，解析出文章的全文
3. 输入包含文章标题、文章链接、文章内容的 RSS

看起来是比较简单的，然而这个方案在实际中却遇到了一个比较大的问题，那就是搜狗的反爬机制。大概是出于保护内容、流量的缘故，搜狗微信搜索虽然能够比较方便地访问到微信公众号文章，但我们通过它获得的文章链接，都不是文章的原始链接：2017 年的时候这个链接是一个有时效性的临时链接，这个链接在不到一天的时间内就会失效而不可访问，所以早期的方案都会在链接没有失效的时候先解析出全文，这样在 RSS 阅读器里直接就能阅读；而现在，这个链接是一个重定向链接，在重定向后才会得到一个临时的文章链接。

我个人没有办法解决链接重定向的问题，所以认为这个方案现在已经无效了，如果有读者认为该问题可以被解决，那么可以参考 [Huginn教程：微信公众号 转换成 RSS](https://web.archive.org/web/20170719092304/http://www.jianshu.com/p/22167468300f) 一文去尝试一下。

## (已失效) 基于即刻/快知和 RSSHub 的方案

[即刻](https://baike.baidu.com/item/%25E5%258D%25B3%25E5%2588%25BB/18672117) 上线机器人功能后，用户就可以自定义微信公众号机器人来抓取任意公众号并生成一个主题了，而即刻的每个主题，又是存在公开 WEB 链接的，所以就可以用 Huginn 解析一个即刻的公众号主题页面，来获取一个公众号的文章列表更新了。而后来 RSSHub 又能直接输出一个即刻主题的 RSS，所以这个流程又能进一步简化一下，省略掉解析即刻主题页面这一步，直接从 RSSHub 输出的 RSS 中，进一步解析出公众号文章的原始链接并抓取全文了。

在即刻服务可用的时候，我就彻底抛弃了基于搜狗微信搜索的方案，因为基于即刻和 RSSHub 的方案一来可以获取文章的原始链接，二来在整体流程上比前者都更简单。

可惜的是，即刻也因为某些暂不了解的原因而停止服务了，不过依赖第三方服务服务会有这个下场我也是有心理准备的，后来就有了第三个方案。

在说第三个方案之前得说一下，现在有一个非常类似即刻的 APP 叫做 [快知](http://kzfeed.com/)，可以充当这个方案里即刻的替代品，唯一的差别是没有办法获得文章的原始链接，所以在 Huginn 中就少了一个文章直链获取的 Agent，见下图对比：

![huginn_scenarios_comparison.png](https://www.zmonster.me/assets/img/huginn_scenarios_comparison.png)

目前基于快知的这个方案是可用的，如果想使用这个方案，可以有两种办法：

1. 安装我的个人项目 [zs](https://github.com/Linusp/zs/) 然后执行下面的命令来生成一个 Huginn Scenario 文件，然后在 Huginn 中导入

```
zs-rss gen-scenario -t kz -n 晚点LatePost -i postlate --kz-topic-id k69QJvO82RKoA -o postlate.json
```

命令参数解释如下：

- "-t kz" 表示生成一个基于快知的 Huginn Scenario
- "-n 晚点 LatePost" 将这个 Scenario 命名为“晚点 LatePost”，同时也设置了最后输出的 RSS 的标题
- "-i postlate" 指定这个公众号的微信 ID，会用在最终的 RSS URL 中，比如这里指定的是 postlate，假设 Huginn 服务的域名是 [https://myhuginn.com](https://myhuginn.com/) 那么最终的 RSS URL 可能是 [https://myhuginn.com/users/1/web\_requests/395/wx-postlate.xml](https://myhuginn.com/users/1/web_requests/395/wx-postlate.xml) —— 这里如果不在乎可维护性的话，不用公众号的微信 ID 也可以，给一个自己喜欢的英文 id 即可
- "–kz-topic-id k69QJvO82RKoA" 这里指定“晚点 LatePost”这个公众号在快知中的主题 ID，可以通过快知搜索到公众号后，分享链接到浏览器获得，比如“晚点 LatePost”在快知中对应的主题链接是 [https://kz.sync163.com/web/topic/k69QJvO82RKoA](https://kz.sync163.com/web/topic/k69QJvO82RKoA) ，那么主题 ID 就是尾部那串符号 "k69QJvO82RKoA"
- "-o postlate.json" 指定输出文件名，随意
2. 直接下载我准备好的 Huginn Scenario 文件 [kz\_scenario\_template.json](https://raw.githubusercontent.com/Linusp/zs/master/zs/rss/kz_scenario_template.json) ，在 Huginn 中导入后再修改其中的设置

基于快知的方案目前可用，但我并不看好这个方案，按照经验，这种做信息抓取的服务，总是存在风险的。

## 基于 EFB 和 Telegram 的方案

由于我一直使用 Linux 系统，工作中需要使用微信进行沟通的时候非常不方便，后来了解到 [EFB](https://github.com/blueset/ehForwarderBot) 后就用它来把收到的微信消息转发到 Telegram，而 Telegram 是有 Linux 客户端的，这样我就能在 Linux 系统上查看微信消息了。

EFB 本质上是在服务器上登录网页微信，然后监听网页微信上的消息来做转发，只要不去搞什么自动回复机器人之类的，那么在使用 EFB 的过程中，所有通过 EFB 收到的消息就是微信上好友、关注的公众号主动发过来的消息，通过 EFB 发送的消息也都是以个人身份发出去的，总之是一个正常用户的正常行为，并不会有封号之类的风险。我使用 EFB 已经有两年了，除了偶尔需要重新登录一下，并没有遇到什么大问题。

使用 EFB 后可以在 Telegram 上收到我关注的公众号的更新消息，而 Telegram 的 API 丰富易用，完全可以写点代码把 Telegram 上收到的公众号文章更新收集起来再转成 RSS。于是在即刻停止服务后，我就开始摸索出了一套新的方案，大致流程是这样的：

1. 写一个脚本，利用 Telegram 的 API，定时获取更新的公众号文章，并保存下来
2. 在 Huginn 上新建一个 WebhookAgent，它会提供一个对应的 webhooks
3. 将保存下来的公众号文章发往到 WebhookAgent，然后通过后续的其他 Agent 进行全文解析和 RSS 输出

一个完整的 Scenario 是下面这个样子的：

![huginn_efb_scenario.png](https://www.zmonster.me/assets/img/huginn_efb_scenario.png)

这个方案的好处有：

1. 不依赖除 Telegram 外的任何第三方服务，因此也不用担心反爬、服务停止等各种问题
2. 能获得极低延时的 RSS 更新

不过相对的，这个方案的门槛也是最高的：

1. 需要自己部署 EFB 和 Huginn，其中 Huginn 虽然可以免费部署，但 EFB 却不行，所以至少需要一个 VPS
2. 需要熟悉 Telegram 的 API 并编写代码 —— 不过这块我已经做了，其他人有兴趣可以直接使用我的代码
3. 需要一个能登录网页微信的个人微信号，而 2017 年 9 月份之后注册的微信号已经无法登录网页微信

这个方案的总体过程是这样的：

1. 部署 EFB，可参考小众软件的文章：[EFB 简明安装教程：用 Telegram 收发微信](https://www.appinn.com/efb-tutorial-with-docker/)
2. 在 Telegram 上新建一个频道，比如“微信.公众号”
3. 与 EFB 机器人对话，将需要输出 RSS 的公众号链接到刚才建立的频道，如 "/link 晚点 LatePost"，这样该公众号的消息就会被 EFB 发送到这个频道了

![telegram_linked_channel.png](https://www.zmonster.me/assets/img/telegram_linked_channel.png)

4. 创建一个包含 WebhookAgent 的 Huginn Scenario，同样有两种方法

- 第一种方法是安装我的项目 [zs](https://github.com/Linusp/zs/)，然后执行下面的命令来生成 Scenario 文件

```
zs-rss gen-scenario -n 晚点LatePost -i postlate -o postlate.json
```

参数含义同之前生成基于快知的 Scenario 时一样

- 也可以直接下载我项目中提供的 Huginn Scenario 文件 [efb\_scenario\_template.json](https://raw.githubusercontent.com/Linusp/zs/master/zs/rss/efb_scenario_template.json) 然后在 Huginn 中导入

创建好 Huginn Scenario 后，点击进入“微信公众号 Webhooks”这个 Agent，获取 webhooks 链接，比如：[https://myhuginn.com/users/1/web\_requests/318/4SXo3X2T2X7HCDjv](https://myhuginn.com/users/1/web_requests/318/4SXo3X2T2X7HCDjv)

5. 在 VPS 或某台能 24 小时开机的机器上上新建定时任务

- 首先安装前面反复提到的我的个人项目 zs
- 然后创建本地数据库，用来存储收集到的微信公众号文章更新

这条命令会在 $HOME/.zs/data 目录下新建一个数据文件 rss.db

- 在 $HOME/.zs/config 目录下新建配置文件 rss.json，写入刚才获得的 webhooks 链接，如

```
{
    "huginn_webhooks": {
        "default": "https://myhuginn.com/users/1/web_requests/372/d742b76e",
        "晚点LatePost": "https://myhuginn.com/users/1/web_requests/372/4SXo3X2T2X7HCDjv"
    }
}
```

这个配置的意思是，公众号“晚点 LatePost”的更新发送到一个 webhooks，其他的发送到另外的 webhooks。如果每个公众号都要输出一个 RSS，那么就需要为每个公众号都设置一个 webhooks 链接；如果有多个公众号想要合并输出一个 RSS，那么可以不设置 webhooks 而使用 default 对应的 webhooks。

- 使用 [crontab](http://man7.org/linux/man-pages/man1/crontab.1.html) 新增两条定时任务

```
7,17,27,37,47,57 * * * * zs-rss fetch-wx-articles -n 微信.公众号 >> log.txt
*/10 * * * * zs-rss send-wx-articles >> log.txt
```

具体的时间频率可以自己调整。

其中第一条定时任务需要 Telegram 的授权认证，具体来说是需要在 $HOME/.zs/config/telegram.json 中有如下内容

```
{
    "api_id": "561071",
    "api_hash": "22691769c5decd501fd49d96ecff58e3",
    "session": "AUTHENTICATION SESSION CODE"
}
```

其中 "api\_id" 和 "api\_hash" 可以在 [https://my.telegram.org/](https://my.telegram.org/) 上获取，而 session 的值会在第一次运行时生成并自动写入到上面的配置文件里。

目前 zs 这个项目仅考虑了我自己的需求，所以设计未必很合理，如果有开发能力的话可以参考我的代码自行更改、增加功能。

## 其他参考方案

如果不想折腾，也有一定的经济来源，可以考虑一些付费服务，比如：

1. [今天看啥](http://www.jintiankansha.me/)：以前可以免费订阅若干个公众号的，现在必须付费了，价格见 [今天看啥-RSS订阅方法](http://www.jintiankansha.me/about/rss)
2. [WeRss](https://werss.app/)：免费试用三天，试用期间可订阅 8 个公众号，具体价格见 [WeRss 付费价格](https://werss.app/price/)

另外，[Kindle4rss](http://kindle4rss.com/) 上面有不少热门的微信公众号全文 RSS，我大致数了下差不多有 100 个，如下图所示：

![kindle4rss_feeds.png](https://www.zmonster.me/assets/img/kindle4rss_feeds.png)

Kindle4rss 的免费用户可以有 12 个订阅，付费价格也不贵，一年 36 人民币就可以订阅 300 个源，比前面两个便宜多了，而且这个服务存在很多年了，可以说一直很稳定，非常推荐。

此外 RSSHub 也有微信公众号支持，见 [文档](https://docs.rsshub.app/new-media.html#wei-xin)。在 RSSHub 里支持了六种方案，分别是：

1. 基于 [WeMP](https://wemp.app/) 的方案
2. 基于 [传送门](https://chuansongme.com/) 的方案
3. 基于北美生活引擎 [CareerEngine](https://careerengine.us/about) 的方案
4. 基于微信公众号数据分析平台 [二十次幂](https://www.ershicimi.com/) 的方案
5. 基于知识管理工具 [优读](https://uread.ai/) 的方案
6. 基于 EFB 和 Telegram 的方案

RSSHub 的前五个方案都是基于一些第三方信息抓取服务的，相对来说非常易用，但仍然存在第三方服务被关停的风险，最后那个方案和我的第三个方案类似，只不过把 Huginn 替换成了 RSSHub。

## 后记

也许有人会说微信就是个大毒瘤我就不看微信公众号，但确实有一些很好的作者只在微信公众号上写作，还有很多博客时代的知名写作者也迁移到了微信公众号上，原来的博客不再更新甚至不可访问了，加上微信生态的封闭，所以一个微信公众号文章的抓取和开放访问需求始终是存在的，也因此各种第三方抓取服务层出不穷。厌恶微信到完全不想碰微信产品包括微信公众号的人自然是有的，但既然大众的需求存在，我想也没什么好争辩的，每个人都有自己选择的自由。虽说如此，在看到一个好的公众号的时候，也不妨先去了解一下作者是否有同步更新的独立博客或知乎专栏，如果有的话还是更推荐去订阅其博客或知乎专栏等更开放的文章来源。
