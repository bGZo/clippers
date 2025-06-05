---
created: 2024-12-28T09:54:30
source: "https://iecho.cc/2019/01/09/PT-%E4%B8%8B%E8%BD%BD%E4%BB%8E%E5%85%A5%E9%97%A8%E5%88%B0%E5%85%BB%E8%80%81/"
type: "archive-web"
modified: 2025-01-15T11:38:15
---

This post is also available in English and alternative languages.

## 专题文章目录

- [PT 下载从入门到养老篇一：站点介绍及生存指南](https://iecho.cc/2019/01/09/PT-%E4%B8%8B%E8%BD%BD%E4%BB%8E%E5%85%A5%E9%97%A8%E5%88%B0%E5%85%BB%E8%80%81/)
- [PT 下载从入门到养老篇二：隐匿的地下通讯](https://iecho.cc/2019/06/01/beginners-guide-to-private-tracker-2/)
- [PT 下载从入门到养老篇三：NAS 存储服务器及硬盘选购](https://iecho.cc/2022/02/06/beginners-guide-to-private-tracker-3/)
- [PT 下载从入门到养老篇四：别买 QNAP - 聊聊威联通 NAS 的坑](https://iecho.cc/2022/10/28/do-not-buy-qnap/)
- [PT 下载从入门到养老篇五：基于 Plex Media Server 搭建家庭影音服务器](https://iecho.cc/2022/11/16/build-a-plex-media-server-as-home-media-center/)
- [PT 下载从入门到养老篇六：家庭网络那些事](https://iecho.cc/2023/04/18/best-practices-for-home-network/)

## 介绍

PT (Private Tracker) 是一种基于私有 BT Tracker 服务器的资源传播形式，经授权的用户使用受允许的客户端进行种子制作与下载。相较于传统 BT 和 emule，PT 站往往采取了==严格的邀请制度==以及免责制度来规避法律风险，同时要求用户客户端开启传输加密以绕过运营商的检测策略。当然，从实际上来说 PT 站的运营、使用仍然是违反了各国版权法的。

许多高清爱好者聚集在 PT 站，发布翻录的蓝光原盘、CD 资源以及录制的高清卫星电视讯号；得益于 Netflix、HBO、Apple TV 等高清流媒体在线视频平台的发展，近年也出现了一些 WEB-DL (Download from Web) 资源。

你可以从 PT 站下载到：

- Netflix/HBO/Apple TV/Paramount/Hulu/Disney+ 等海外流媒体平台的电视剧和电影
- 爱奇艺/腾讯视频/优酷等流媒体平台的电视剧和电影
- 包含特典和封面图片的蓝光动漫原盘
- 体育赛事和晚会庆典的卫星电视或 IPTV 录制
- 从 CD 抓取或 Spotify/Tidal/Qobuz 等音乐平台下载的无损音乐
- ~~日本动作片~~

目前国内使用的 PT 站源码==主要为==基于浙江大学 [xiazuojie](https://iecho.cc/2019/01/09/PT-%E4%B8%8B%E8%BD%BD%E4%BB%8E%E5%85%A5%E9%97%A8%E5%88%B0%E5%85%BB%E8%80%81/) 团队所开发的开源整站项目 [NexusPHP](https://sourceforge.net/projects/nexusphp/)，基于 PHP + MySQL + memcached。个别站点使用 Discuz! 进行二次开发。

日前，[@burpheart](https://github.com/burpheart/) 基于上游项目，开发了新版的 [NexuxPHP Safe](https://github.com/burpheart/NexusPHP_safe)。其修复了一些已知的安全漏洞，并加入了一些增强用户体验的小功能。

2022 年更新：[@burpheart](https://github.com/burpheart/) 似乎逐步淡出了项目维护。目前项目迁移至 [xiaomlove/nexusphp](https://github.com/xiaomlove/nexusphp)，由 [@xiaomlove](https://github.com/xiaomlove/) 为主的开发者继续维护。

U2 和某些教育网 PT 站（如 [北邮人](https://byr.pt/)）的研发能力是相当高的，基于原版 NexusPHP 做了很多功能和安全改进，对于新版本客户端也持欢迎态度。某些公网 PT 站属于 one-man 站点，Tracker 经常炸，技术 Bug 修老久，把网络问题甩锅 GFW 等等。==建议大家谨慎选择注册用户数小于 1 万或每周活跃用户数小于 1 千的 PT 站。==

## 考古

一些历史悠久的网帖：

- [SiLU.info 思路 - Google 网上论坛](https://groups.google.com/g/silu)
- [思想是需要一条道路的 (2008)](https://iecho.cc/2019/01/09/PT-%E4%B8%8B%E8%BD%BD%E4%BB%8E%E5%85%A5%E9%97%A8%E5%88%B0%E5%85%BB%E8%80%81/%E6%80%9D%E6%83%B3%E6%98%AF%E9%9C%80%E8%A6%81%E4%B8%80%E6%9D%A1%E9%81%93%E8%B7%AF%E7%9A%84.pdf) - [WebArchive](https://web.archive.org/web/20240410105019if_/https://groups.google.com/g/silu/c/Hxx39xzdIQw)
- [思路声明 (2008)](https://iecho.cc/2019/01/09/PT-%E4%B8%8B%E8%BD%BD%E4%BB%8E%E5%85%A5%E9%97%A8%E5%88%B0%E5%85%BB%E8%80%81/%E6%80%9D%E8%B7%AF%E5%A3%B0%E6%98%8E.pdf) - [WebArchive](https://web.archive.org/web/20240410105145if_/https://groups.google.com/g/silu/c/J4QfuHdTh0s)
- [拨乱反正：WENBO 出售 www.silu.info 域名的真相](https://web.archive.org/web/20080628163701if_/http://www.hd.club.tw/thread-8073-1-1.html)
- [再论国内的几大 PT 站 (2010)](https://iecho.cc/2019/01/09/PT-%E4%B8%8B%E8%BD%BD%E4%BB%8E%E5%85%A5%E9%97%A8%E5%88%B0%E5%85%BB%E8%80%81/%E5%86%8D%E8%AE%BA%E5%9B%BD%E5%86%85%E7%9A%84%E5%87%A0%E5%A4%A7PT%E7%AB%99.pdf)
- [关于各个 PT 站点 DNA 的个人理解](https://iecho.cc/2019/01/09/PT-%E4%B8%8B%E8%BD%BD%E4%BB%8E%E5%85%A5%E9%97%A8%E5%88%B0%E5%85%BB%E8%80%81/%E5%85%B3%E4%BA%8E%E5%90%84%E4%B8%AAPT%E7%AB%99%E7%82%B9DNA%E7%9A%84%E4%B8%AA%E4%BA%BA%E7%90%86%E8%A7%A3.pdf)
- [国内三大 PT 站分析 (2010)](https://iecho.cc/2019/01/09/PT-%E4%B8%8B%E8%BD%BD%E4%BB%8E%E5%85%A5%E9%97%A8%E5%88%B0%E5%85%BB%E8%80%81/%E5%9B%BD%E5%86%85%E4%B8%89%E5%A4%A7PT%E7%AB%99%E5%88%86%E6%9E%90.pdf)
- [国内高清 PT 格局初定，微妙平衡随时可能被破 (2011)](https://iecho.cc/2019/01/09/PT-%E4%B8%8B%E8%BD%BD%E4%BB%8E%E5%85%A5%E9%97%A8%E5%88%B0%E5%85%BB%E8%80%81/%E5%9B%BD%E5%86%85%E9%AB%98%E6%B8%85PT%E6%A0%BC%E5%B1%80%E5%88%9D%E5%AE%9A%EF%BC%8C%E5%BE%AE%E5%A6%99%E5%B9%B3%E8%A1%A1%E9%9A%8F%E6%97%B6%E5%8F%AF%E8%83%BD%E8%A2%AB%E7%A0%B4.pdf)
- [我买、卖 HDChina 账号的经历 (2011)](https://iecho.cc/2019/01/09/PT-%E4%B8%8B%E8%BD%BD%E4%BB%8E%E5%85%A5%E9%97%A8%E5%88%B0%E5%85%BB%E8%80%81/%E6%88%91%E4%B9%B0%E3%80%81%E5%8D%96hdchina%E8%B4%A6%E5%8F%B7%E7%9A%84%E7%BB%8F%E5%8E%86.pdf)
- [国内外 PT 站点评 (2012)](https://web.archive.org/web/20210404133244/https://www.douban.com/group/topic/27989385/)
- [PT 站点大全 (2012)](https://web.archive.org/web/20201121094012/https://www.douban.com/group/topic/32448115/)
- [思路网是怎么做起来的？(2013)](https://www.zhihu.com/question/20990894/answer/16824432)
- [马甲门论坛一位 PT 达人多年的经验之谈 (2015)](https://iecho.cc/2019/01/09/PT-%E4%B8%8B%E8%BD%BD%E4%BB%8E%E5%85%A5%E9%97%A8%E5%88%B0%E5%85%BB%E8%80%81/%E9%A9%AC%E7%94%B2%E9%97%A8%E8%AE%BA%E5%9D%9B%E4%B8%80%E4%BD%8DPT%E8%BE%BE%E4%BA%BA%E5%A4%9A%E5%B9%B4%E7%9A%84%E7%BB%8F%E9%AA%8C%E4%B9%8B%E8%B0%88.pdf)

## PT 站汇总

根据网络环境和用户群体，国内 PT 站可以划分为两个系别：**教育网 PT 站** 和 **公网 PT 站**。

### 教育网 PT 站点

以 [北邮人](http://bt.byr.cn/)（北京邮电大学）、[蒲公英](https://npupt.com/)（西北工业大学）、[极速之星](http://bitpt.cn/)（北京理工大学）和 [六维空间](http://bt.neu6.edu.cn/)（东北大学）为主。

高校校园网提供的 IPv4 网络一般是有计费及限速策略的，由校方向电信、联通、移动、鹏博士等运营商采购带宽并在出口实施自动分流。而为了推广 IPv6 业务，各高校所接入的中国教育网（CERNET）的 IPv6 网络一般是不计费且不限速的，因此组建一个依托于 IPv6 的免费资源分享网络有着很大意义。

一般来说，教育网 PT 站的原创影视资源较少，大部分为转载资源。Coursera、Udacity 等公开课资源（WEB-DL）、考研视频、电子书等内容较多，此外，北邮人等站点还提供一些诸如 Steam 游戏数据备份文件，这样学生就不用担心被几十个 G 的 Steam 游戏更新榨干网费了。

目前来看教育网 PT 站或多或少获得了学校网络中心的技术和政策支持，所以才能存留至今。==部分教育网 PT 站仅允许 IPv6 或仅归属于教育网单位的 IPv6 访问==，因此对于公众来说访问有些难度。可以通过 [Hurricane Electric](https://he.net/) 提供的 [IPv6 TunnelBroker 隧道](https://tunnelbroker.net/)，或者基于 [有 IPv6 网络的 VPS](https://www.vultr.com/?ref=9255123) 搭建代理来中转 tracker 的流量。

从分享率和发种规范来看，教育网 PT 站十分宽松，但保种率可能不如公网 PT 站高，资源也没那么丰富。但对于追热门电影和美剧的轻度用户来说还是足够了。==建议初次接触 PT 的用户先从教育网 PT 站（如 [北邮人](https://byr.pt/)、[蒲公英](https://npupt.com/)）养号==，之后通过官方邀请帖等渠道间接进入公网 PT 站。

[![](https://iecho.cc/2019/01/09/PT-%E4%B8%8B%E8%BD%BD%E4%BB%8E%E5%85%A5%E9%97%A8%E5%88%B0%E5%85%BB%E8%80%81/byr-user-level.png "北邮人用户等级制度")](https://iecho.cc/2019/01/09/PT-%E4%B8%8B%E8%BD%BD%E4%BB%8E%E5%85%A5%E9%97%A8%E5%88%B0%E5%85%BB%E8%80%81/byr-user-level.png)

### 公网 PT 站点

传说中国有五大公网 PT 站：HDS、TTG、HDC、CHD、HDR，也有三大 PT 站的说法，即 CHDbits、HDChina、TTG。经过 [2013 年 4 月 26 日世界版权日风波（“中国版权第一案”的思路网侵权案，又称==“426”事件==）](https://zh.wikipedia.org/wiki/%E6%80%9D%E8%B7%AF%E7%BD%91)，HDStar（思路网）管理组（站长”雪还是白的“等人）被捕入狱，剩下的站点也多多少少受到了一些影响，有些直接关闭了，有的则隐没了。

距离版权日风波已经过去了七八年，现在国内 PT 站又呈现出繁荣景象。一方面国内电视剧集的分级制度迟迟未推出，而 Netflix、HBO、Disney+、Apple TV+ 等境外流媒体业务的订阅费用也居高不下。另一方面，国内百兆、千兆家庭宽带已经覆盖到了三四线城市甚至是县城，养一个 PT 账号的成本已经相当低了。

以影视资源为主的有：

- HDChina.org (2008-2012)：自称“中国高清第一站“，是中国境内创立最早、用户规模最大的 PT 站之一。
- HDWing.com (2013-2014)：数据集成自 HDChina.org，于 2014 年关闭。
- [HDChina.org 瓷器（2015-2023）](https://hdchina.org/)：[创立于 2015 年](https://twitter.com/HDChinaOfficial)，==用户数据继承自原先的 HDWinG 和 HDStar。==最早使用 `hdchina.club` 域名，于 2017 年初重新启用 `hdchina.org` 域名。资源方面，官方制作组（HDCTV 和 HDChina）的 Netflix、HBO 剧集，原盘，录制的电视剧比较多。
- ==北京时间 2023 年 11 月 29 日始，HDChina 网站和 tracker 均无法访问，且 Telegram 机器人 [@hdchina\_group\_bot](https://t.me/@hdchina_group_bot) 也无响应。==
- 2024 年 2 月 9 日，HDChina Telegram 群管理员 @fork\_b 发布了一张文件列表截图：共 4 个 `.tar.gz` 格式文件，分别为 `2023-11-28-170{马赛克}`、 `2023-11-29{马赛克}`、 `2023-11-29{马赛克}` 和 `website.tar.gz`。 不难推测这是数据库以及 NexusPHP 和种子目录的备份。与此同时，管理员 @nilaoda\_cn 和 @duoluo1234 的 Telegram 账号状态仍然显示为“last seen a long time ago”。
- 2 月 26 日，`hdchina.org` 域名到期，并进入续约宽限期（Renewal Grace Period）。可见域名实控人失联。
- 2 月 28 日，管理员 @fork\_b 设置了禁言。
- 3 月，HDChina Telegram 群的 Owner @duoluo1234 账号因为长时间未登录而被 Telegram 自动删除，群组变为无主群。截止目前，两位管理员 @nilaoda\_cn 和 @duoluo1234 已经失联超过 4 个月，HDChina 网站和 tracker 仍然无法访问。
- 4 月 11 日，`hdchina.org` 域名被续费至 `2027-02-26`。
- 4 月 23 日，根据 [证书透明度](https://crt.sh/?q=hdchina.org) 计划，`hdchina.org` 域名的 SSL 证书被更新。
- [HDRoad.org / HDRoute.org（2009-）](http://hdroute.org/)：前身为 HDRoad 思路高清（思路 PT，隶属于 MySiLU），历史悠久。
- [CHDbits.co 彩虹岛](https://chdbits.co/)：近 10 年的老站点，影视资源很丰富。与 HDChina 有深仇大恨，至今 HDChina 群规仍然写着“禁止求 CHD 邀请”。
- [FRDS 朋友](https://pt.keepfrds.com/)：2012 年成立的老站。其制作组发布的 IMDb/豆瓣 Top 250 电影合集很不错。
- [Spring Sunday (SSD)](https://springsunday.net/)：2010 年创建的老站点，前身为 CMCT 触摸春天。
- [CCFBits.org 吹吹风](http://ccfbits.org/)：挺老的大站了，资源很丰富也很低调。
- [TCCF / TorrentCCF 他吹吹风](https://et8.org/)：2009 年创立的老站点。
- [M-Team.cc 馒头](https://www.m-team.cc/)：由台湾地区运营的以情色内容为主题的 PT 站，官方提供付费邀请码购买渠道。与大陆的 NAS、硬盘代理商（如广州华影影音科技有限公司）保持着紧密的合作关系，经常可以见到买硬盘或 NAS 送 M-Team 邀请的广告。
- [BTSchool.club 比特校园](https://pt.btschool.club/)：2019 年刚创建的新站点，门槛相对比较低。
- [HDTime.org 高清时间](https://hdtime.org/)：老站点，但是没什么名气。
- [52PT.site 我爱 PT](https://52pt.site/)：新站点。
- [HDSky 天空](https://hdsky.me/)：综合站点。2022 年年中，HDSky 突然修改了账号等级制度和保号政策，并上调 VIP 价格，吃相极为难看，因此不建议各位加入此网站。
- [TTG](https://totheglory.im/upload.php)：国内大站之一，2014 年末作为 TTG 出现。
- [JoyHD](https://joyhd.net/)：2013 年用 xbtit 建立的 PT 站，后来改用 NexusPHP。老实说我玩 PT 十几年了从没听说过这个站。
- [HDU 好多油](https://pt.upxin.net/): 2014 年 12 月 27 日创建的老站，距今也快 10 年了。知名度很低，资源一般，没什么原创种。
- [Ourbits 我堡](https://ourbits.club/)：算是国内大站了，创建于 2016 年末。直接访问域名会出现“工信部域名未备案”的提示，实际上仍然为具有合法 Cookies 的用户提供服务。[静默时期登录页面](https://ourbits.club/gohome.php)。
- [HDHome 家园](https://hdhome.org/)：2015 年左右成立的 PT 站，没啥特色。
- [PTHome 铂金家](http://www.pthome.net/)：2018 年左右成立的新站，没啥特色。PT 是 Platinum（铂金）的缩写，因此被称为“铂金家”。
- [HDCity 城市](https://hdcity.city/)：2009 年底成立的老站。
- [NicePT 老师站](https://www.nicept.net/)：又称为小馒头（相对于 M-Team 来说），2019 年建站。
- LeagueHD / LemonHD.org 柠檬：小站中发展的还算不错的，2019 年成立。==已于 2023 年 5 月 20 日永久关闭。==
- [Haidan 海胆之家](https://www.haidan.video/)：2020 年刚成立的小站。
- [Great Poster Wall (GPW) 海豹](https://greatposterwall.com/): 基于 Gazelle 开发的国内 PT 站，2021 年刚开，没啥特色。
- [PTerClub 猫站](https://pterclub.com/)：2018-19 年创立的新站点，早期入站门槛较低。其 PTer、PTerWeb 制作组的资源还不错。
- [HDFans 红豆饭](https://hdfans.org/)：2023 年 5 月创建的新站。站长是 [墨香梅林](https://tieba.baidu.com/home/main?un=%E5%A2%A8%E9%A6%99%E6%A2%85%E6%9E%97)，在贴吧较为活跃。以转载资源为主，没有特色。种子分为 free 和 50% off 两种，很好刷流和生存，适合新手和懒人。
- [UltraHD](https://ultrahd.net/): 2020 年年底由 xiaomlove 创建的以韩剧为主的 PT 站。
- [HDArea 高清视界](https://hdarea.club/)
- [HDPT 明教](https://hdpt.xtz/)：2022 年 8 月建立的综合站点，对小水管友好。
- [HD Dolby 高清杜比](https://www.hddolby.com/)：2019 年初创立的综合站，对新手友好。
- [HDVideo](https://hdvideo.one/)：2022 年中创立的综合站，没啥特色。
- [备胎 PT](https://beitai.pt/)
- [HD4Fans 兽站](https://pt.hd4fans.org/)：
- [Sbao 烧包](https://ptsbao.club/)

教育网 PT，部分 tracker 可能仅允许教育网或 IPv6 连接。入站门槛较低，可以凭借 edu 教育域名的邮箱进行注册，也可以通过校内用户发起邀请。对分享率和种子规范的限制比较宽松。

- [NanyangPT 南洋](https://nanyangpt.com/)：西安交通大学 PT 站
- [BYR 北邮人](https://byr.pt/)：北京邮电大学 PT 站，仅对 IPv6 开放
- [TJUPT 北洋园](https://www.tjupt.org/)：天津大学 PT 站
- [葡萄 PT](https://pt.sjtu.edu.cn/)：上海交通大学 PT 站
- [NPUPT 蒲公英](https://npupt.com/)：西北工业大学 PT 站
- [BITPT 极速之星](http://bitpt.cn/)：北京理工大学 PT 站
- [六维空间](http://bt.neu6.edu.cn/)：东北大学 PT 站
- [NexusHD](https://nexushd.org/)：浙江大学 PT 站，仅供校内用户访问
- [MTPT 麦田 PT](http://pt.nwsuaf6.edu.cn/): 西北农林科技大学 PT 站
- [西电睿思](https://rs.xidian.cc/)：西安电子科技大学 PT 站
- [HUDBT 蝴蝶](http://hudbt.hust.edu.cn/)：华中科技大学 PT 站

以动漫资源为主的有

- [U2 动漫花园 幼儿园](https://u2.dmhy.org/)：老牌动漫 PT 站。各种上古资源都能找到。
- [Skyey Snow 天雪动漫](https://www.skyey2.com/)：基于 Discuz! 构建的 PT 站点，相对来说新一些。
- [Azusa 梓喵](https://www.azusa.wiki/)：2022 年创立的二次元相关站点。
- [piggo 猪猪网](https://piggo.me/)：2022 年创立的新站，以动漫和 3D 原盘为主。

以音频资源为主的有

- [OpenCD 皇后 PT](https://open.cd/)：小体积种子比较多，基本靠攒魔力值来保号。欧美、华语和古典音乐资源都很丰富。邀请权限很少开放，网站活跃度较低。有 Hit & Run 限制。
- [DICMusic 海豚音乐](https://dicmusic.club/): 基于 Gazelle 开发的国内音乐 PT 站，前身是空耳 PT。
- [RedLeaves 红叶](https://leaves.red/)：2022 年 10 月成立的新站，以有声小说为主。
- [聆音 Club](https://pt.soulvoice.club/)

其他

- [杏坛 PT](https://xingtan.one/login.php)：成立于 2022 年 11 月，是一个主打学术资源的综合站点。之前名为杏林。

## PT 站质量

援引一份 [@Rhilip](https://blog.rhilip.info/) 的 [数据](https://blog.rhilip.info/archives/839/)，按官方种占比倒序排序。数据源日期为 2018/4/10，但仍具备一定参考价值。考虑到对于同一份资源，某些官方组会采用不同色彩配置和编码压制不同版本，如 HEVC/H.264 或 SDR/HDR 等，所以官方种占比值只起到参考作用。

==教育网 PT 以转载资源为主，一般在资源发布后的一天内就能在教育网 PT 站下载到来自公网 PT 站的热门电影和电视剧资源。在资源丰富度和种子活跃度（seeder 人数）上，公网 PT 站具备显著优势。==

| 站点 | 官方组标识 | 官方组发种数 | 统计种子总数 | 官方种占比 |
| --- | --- | --- | --- | --- |
| HDSky | HDSky, HDS, HDS3D, HDSTV, HDSWEB, HDSPad, HDSCD | 32502 | 60467 | 53.75% |
| CHDBits | CHDBits, CHD, CHDTV, CHDPAD , CHDWEB , CHDHKTV | 15419 | 30537 | 50.49% |
| HDChina | HDChina, HDCTV, iHD, HDWinG, HDWTV, OpenMV, HDC | 13562 | 29099 | 46.61% |
| HDHome | HDHome , HDH, HDHTV, HDHPad | 12672 | 31043 | 40.82% |
| HDTime | HDTime, HDT, Vtime, PADTime | 3524 | 12103 | 29.12% |
| CMCT | CMCT, CMCTA, CMCTV | 10609 | 41046 | 25.85% |
| HDCity | NoVA, NoPA, NoTA, NoXA | 2444 | 9750 | 25.07% |
| TCCF | BMDru | 4340 | 21251 | 20.42% |
| Ourbits | OurBits , OurTV, iLoveHD, iLoveTV | 5075 | 25432 | 19.96% |
| JoyHD | JoyHD | 1090 | 6726 | 16.21% |
| NYPT | NYHD, NYPAD, NYTV, NYPT | 1863 | 25655 | 7.26% |
| HDU | HDU | 1090 | 15852 | 6.88% |
| Hyperay | Hyper, PureTV, HyPad, Tron, geek, TronTV, Neon | 816 | 12148 | 6.72% |
| NWSUAF6 | MTTV | 2305 | 38978 | 5.91% |
| TTG | Wiki, TTG, DoA, NGB | 11066 | 196604 | 5.63% |
| Mteam | MTeam, MTeamPAD, MTeam3D, MTeamTV | 10002 | 204982 | 4.88% |
| SJTU | PuTao | 2005 | 62723 | 3.20% |
| BYR | BYRHD, BYRPAD, BYRTV | 2185 | 79643 | 2.74% |
| TJUPT | TJUPT | 593 | 40133 | 1.48% |
| NPU | npuer | 727 | 68434 | 1.06% |

## 用户规范

对于用户，无论是公网 PT 站还是教育网 PT 站，往往都有以下要求：

1. 上传、下载量：新手考核计划一般为一个月内 `>=50GB` 的上传下载量。部分教育网 PT 站可能没有新手考核要求。
2. 分享率（上传量/下载量）：PT 站的优质资源离不开各位用户的分享和做种。为了减少吸血鬼用户的影响，几乎所有 PT 站点都会要求用户的风险率超过一定值。除此之外，用户分享率与用户等级相关，如果风险率低于标准会自动回退到较低的用户等级。

[![](https://iecho.cc/2019/01/09/PT-%E4%B8%8B%E8%BD%BD%E4%BB%8E%E5%85%A5%E9%97%A8%E5%88%B0%E5%85%BB%E8%80%81/u2-user-level.png "U2 用户等级制度")](https://iecho.cc/2019/01/09/PT-%E4%B8%8B%E8%BD%BD%E4%BB%8E%E5%85%A5%E9%97%A8%E5%88%B0%E5%85%BB%E8%80%81/u2-user-level.png)

3. 魔力值（Bonus points，即积分，获得于用户赠送、活动奖励或做种）：魔力值可以用于兑换站内头衔、更改用户名、消除广告，甚至至博彩小游戏（例如赌球或 24 点，常见于世界杯期间）。
4. 最小做种时间：为了保障种子活跃度，一些 PT 站严格禁止下完就跑（称为 H&R, Hit and Run）的行为，要求用户至少持续做种一定时间）。摘录一段 OpenCD 的规则作为参考。

[![](https://iecho.cc/2019/01/09/PT-%E4%B8%8B%E8%BD%BD%E4%BB%8E%E5%85%A5%E9%97%A8%E5%88%B0%E5%85%BB%E8%80%81/opencd-down-rule.png "OpenCD 皇后 PT 站下载规范")](https://iecho.cc/2019/01/09/PT-%E4%B8%8B%E8%BD%BD%E4%BB%8E%E5%85%A5%E9%97%A8%E5%88%B0%E5%85%BB%E8%80%81/opencd-down-rule.png)

## 生存指南
### 考核期：快速满足新手考核标准

大部分站点都有邀请考核制度，需要在一个月时间内达成一定的==上传量、下载量、魔力值（做种获得的积分）和平均做种时间==。==部分站点考核不计算魔力值所兑换的上传量==，建议老老实实下载热门种子并做种。

邀请者通常可以消耗数倍的魔力值来兑换一个无需新手考核的邀请码。被邀请人也可以付费捐赠（几百元不等）来免除新手考核。

### 考核后：提高上传量和分享率

通过新手考核后，用户可以通过提高分享率和上传、下载量来提高自己的用户等级。有些站点会在升级时赠送一定的邀请码。通常在达到一个较高等级后，用户可以获得长时间不登录也不会被封号的特权。

- 对于一些以影视作品为主的公网 PT 站：尽可能的下载热门种子，这样能更快的获得上传量。可以使用 BT 客户端的 RSS 订阅功能，实现无人值守下载。如果手头宽裕，可以租用一个月的 Seedbox 来快速刷上传量。
- 对于以小种为主的 PT 站：如 OpenCD 以及大部分教育网站点，则需要通过下载大量小体积种子并长时间做种以换取魔力值，再使用魔力值兑换上传。

==想快速提高上传和下载量，最快的办法就是租用 Seedbox 或大盘鸡（大盘机，指代硬盘很大的服务器）。==Seedbox 即专用于跑 BT/PT 的服务器，一般位于海外（德国、罗马尼亚、荷兰）等地。

- 可以通过 SeedBox 例如 [FeralHosting](https://feralhosting.com/) 或 [Seedbox.io](https://seedbox.io/) 配合 RSS 订阅来实现无人值守下载。由于 Seedbox 带宽相对较大（普遍在 1-10Gbps 左右），盒子间互刷效果过于明显，部分 PT 站会有 seedbox 限制政策，例如限制上传、下载速度或者最大上传量。
- 也可以通过 [Hetzner](https://www.hetzner.com/)、[Kimsufi](https://www.kimsufi.com/en/)、[OVHCloud](https://www.ovhcloud.com/) 等云服务及托管商购买独立服务器（dedicated server，也称作独服、杜甫）。
- 也可以自己搭建黑群晖或直接使用群晖 Synology、威联通 QNAP 等成品 NAS 或使用 OpenMediaVault、VMWare ESXi、UNRaid 搭建私人的 HTPC 平台。

注意，==有些 PT 站对于 Seedbox、VPS 和独立服务器有严格的使用限制==，如图为 HDChina 的 Seedbox 规则。

[![](https://iecho.cc/2019/01/09/PT-%E4%B8%8B%E8%BD%BD%E4%BB%8E%E5%85%A5%E9%97%A8%E5%88%B0%E5%85%BB%E8%80%81/hdc-seedbox-rule.png "HDChina Seedbox 使用规范")](https://iecho.cc/2019/01/09/PT-%E4%B8%8B%E8%BD%BD%E4%BB%8E%E5%85%A5%E9%97%A8%E5%88%B0%E5%85%BB%E8%80%81/hdc-seedbox-rule.png)

此时混 PT 只为偶尔下几个资源，而不是那么注重参与了。你可以使用 RSS 订阅功能，订阅感兴趣的资源分类，配合 Plex 或 Infuse 等媒体中心软件，实现自动下载和元信息整理。无需再花精力在折腾 PT 上。

- 分享率：部分站点可以通过捐赠获得终身 VIP 头衔，从此不再需要担心分享率问题。
- 定期访问：==PT 站点会删除长期不访问的账号，请务必保持一定的活跃度，至少每半个月访问一次==。

## PT 下载客户端的选择

[![](https://iecho.cc/2019/01/09/PT-%E4%B8%8B%E8%BD%BD%E4%BB%8E%E5%85%A5%E9%97%A8%E5%88%B0%E5%85%BB%E8%80%81/u2-notice.png "U2 关于客户端版本的公告")](https://iecho.cc/2019/01/09/PT-%E4%B8%8B%E8%BD%BD%E4%BB%8E%E5%85%A5%E9%97%A8%E5%88%B0%E5%85%BB%E8%80%81/u2-notice.png)

不同网站对于 BT 客户端的兼容性不同。尤其是 BitTorrent v2 协议推出后，与旧版本的客户端均不兼容。因此部分 PT 站会拒绝较新版本的 BT 软件。此外，普通的 PT 下载器如 Free Download Manager (FDM)、迅雷、[Aria2c](https://aria2.github.io/) 以及 [qBittorrent-enhanced](https://github.com/c0re100/qBittorrent-Enhanced-Edition) 是被严格禁止的。

- 99.9% 的 seedbox 用户选择 Rtorrent/Rutorrent，因为有些 seedbox provider 只提供这些。
- 大部分 Windows 用户选择了 [µTorrent](https://www.utorrent.com/) (uTorrent)。但是 uTorrent 3.x/4.x 并不稳定，性能也不好，内置了浏览器、工具栏等奇怪的插件。另外一部分用户选择了 [qBittorrent](https://www.qbittorrent.org/)。
- 大部分群晖用户会选择 Synology Download Station；而由于糟糕的兼容性，大部分威联通用户会选择封装好的 [qBittorrent](https://www.qnapclub.eu/en/qpkg/358)。还有一部分人用 [Transmission](https://transmissionbt.com/)。这里更推荐使用 qBittorrent 的 [Docker 镜像](https://hub.docker.com/r/linuxserver/qbittorrent)，方便迁移数据和版本升级等。
- Linux 用户可能会选择 [libtorrent](https://www.libtorrent.org/) 或 [qBittorrent-nox](https://manpages.ubuntu.com/manpages/jammy/man1/qbittorrent-nox.1.html)。

## 注意事项

- 除非在特定板块，不要在某个 PT 站提到其他 PT 站点的名字。
有些网站管理员非常介意用户流失，或者与其他站点发生过不愉快的事情，因此会对触犯此条例的用户执行封禁。
- 尽可能地尊重发布者，不要在评论区发表不积极的意见。
尊重资源发布者是一种美德。触犯此条例可能会获得警告信或者永久封禁。
- 遇到技术问题应先使用搜索引擎检索，而不是当伸手党。
网站管理员一般非常反感小白用户的问题。
- 不要作弊
由于圈子很小，可能会遭受连锁封禁（被多个站点同时封禁）。你也可以理解为国内 PT 站点有着一个类似 John Wick 里的 High Table（高桌会）组织，会就行为恶劣的事件达成共识。
- 不要持有小号（马甲）
管理员一般会基于以下规则来判断马甲账号
1. 用户的登录、注册 IP
2. 用户客户端上报 Tracker 所使用的 IP
3. 用户名及邮箱的命名规律
4. 匿名举报
- 谨慎选择邀请人，不要随意向陌生人发送邀请。
部分站点对于违反某些规则的用户会采取连坐措施，封禁整个邀请链（树）。
- 不要在公共场合发送、索求邀请码，或者提到网站网址和名称。
这个“传统”已经持续近十年了，只不过是自我安慰。
