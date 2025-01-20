---
title: "谈谈-iOS-平台上的几款代理软件"
created: 2022-01-19T01:03:56
modified: 2025-01-19T02:57:24
pagse:
source: "https://blog.hly0928.com/post/talk-about-some-proxy-apps-on-ios/"
tags:
  - "todo"
tags-link:
type: "archive-web"
---

> 本文部分内容可能不适合无经验的小白阅读。
>
> 本文所述软件均不在 App Store 中国区提供。

自从去年 Quantumult X 上架以来，我就陆陆续续折腾了规则、策略组、JavaScript 脚本等功能，并相继入手了 Quantumult X、Surge、Loon 几款代理软件。加上先前一直在用的 Shadowrocket 和 Quantumult，我也算是把 iOS 平台上最热门的代理软件都使用了一遍。

本文就简单谈谈上述几款软件的上手体验，对比一下它们的区别。在开始之前，当然要先放一只可爱的 Clash 猫：

![](https://blog.hly0928.com/media/posts/talk-about-some-proxy-apps-on-ios/01.jpg)

#### 缝 合 怪

### Surge：最强大也是最贵

说到 iOS 平台的代理软件，绕不开的一款就是元老级别的 Surge。毫无疑问，Surge iOS 目前首年 $50 + 后续每年 $15 的价格肯定是虚高的。然而，Surge 优秀的稳定性、出色的软件设计、强大的高级功能~~和逼格~~，也在一定程度上支撑了其高昂的价格。下面就说说几个 Surge only 的 features：

#### iOS / macOS 双平台支持

![](https://blog.hly0928.com/media/posts/talk-about-some-proxy-apps-on-ios/02.png)

#### Surge Mac & Surge iOS

在所有代理软件中，Surge 是唯一提供了 iOS / macOS 双平台支持的一个。而且，两个平台在功能上相差无几（最大的区别应该是 macOS 多出了一个 [网关模式](https://medium.com/@Blankwonder/surge-mac-as-gateway-b0bd68464a4b)），也能使用同一份配置文件。另外，尽管本文讨论的是 iOS 平台，但对于 macOS 而言，Surge 也算是功能十分强大的代理软件了（相较于目前的 [ClashX](https://github.com/yichengchen/clashX/tree/master) 而言）。

#### 最强大的规则支持

从 Surge 自身来说，除了其他代理软件也支持的 `DOMAIN`, `DOMAIN-SUFFIX`, `DOMAIN-KEYWORD`, `IP-CIDR`, `USER-AGENT` 等规则类型，Surge 还支持 `URL-REGEX`, 逻辑匹配 (`AND`, `OR`, `NOT` 三种) 等规则<sup><a href="https://blog.hly0928.com/post/talk-about-some-proxy-apps-on-ios/#ref01">[1]</a></sup>，是 iOS 平台上对规则支持最强大的代理软件。

从规则集 (Ruleset) 引用来说，得益于 Surge 推出时间早、规则支持好、使用人数多，它拥有最丰富的在线规则集。[lhie1/Rules](https://github.com/lhie1/Rules/tree/master)、[神机规则](https://github.com/ConnersHua/Profiles/tree/master) 和许多其他热门规则仓库对 Surge 均有完整的支持，能在很大程度上方便自定义规则的编写。

#### 最完善的 JavaScript 脚本支持

Surge 在代理软件中最早提供了对 JavaScript 脚本的支持，同时也是目前做得最完善的一个。由于 Quantumult X 商店版放弃了对远程脚本的支持，而 Loon 现在仍不够成熟稳定，因此如果想要使用远程脚本，实现去广告、自动签到等高级功能，目前最好的选择仍是 Surge。

#### 一些其他的高级特性

除了上面所述的双平台支持、规则系统和 JS 脚本之外，Surge 还有一些~~你可能用不到的~~值得一提的高级特性：

##### 最近请求 / 抓包功能

![](https://blog.hly0928.com/media/posts/talk-about-some-proxy-apps-on-ios/03.png)

Surge 之前一直标榜自己是 **网络调试工具** ~~虽然我觉得这就是个笑话~~，因此它也有着还算好用的抓包功能。尽管 Quantumult X 等软件也可以抓取并保存请求，但 Surge 在界面和易用性上确实做得不错，能够简化我们对规则或脚本等功能的调试。

##### DNS over HTTPS

Surge iOS 在 4.3.0 版本后完善了对 DNS over HTTPS (DoH) 的支持<sup><a href="https://blog.hly0928.com/post/talk-about-some-proxy-apps-on-ios/#ref02">[2]</a></sup>。在目前的代理软件中，只有 Surge 提供了 DoH 支持。如果你已经在使用 Surge 了，那么不妨安装我写的 [Module](https://raw.githubusercontent.com/hly0928/Proxy-profiles/master/Surge/Module/DoH.sgmodule) 来体验阿里公共 DNS 的 DoH 服务，提高 DNS 查询的隐私性和安全性。

##### Module

Module（模块）是 Surge 最近加入的新功能。Module 是一系列设置的集合，可以用于覆盖当前配置的部分设定<sup><a href="https://blog.hly0928.com/post/talk-about-some-proxy-apps-on-ios/#ref03">[3]</a></sup>。对于小白用户来说，通过直接安装他人写好的 Module（比如 lhie1 的 [Module](https://github.com/lhie1/Rules/tree/master/Surge/Surge%203/Module)），可以方便地实现去除特定 app 广告等高级功能。而对于专业用户而言，Module 也为微调和开关部分设置提供了便利。[这里](https://github.com/hly0928/Proxy-profiles/tree/master/Surge/Module) 有我自用的几个 Modules，可以实现开关 WiFi Access、开关 DoH、开关对所有域名进行 MitM 等功能。

#### 小结

Surge 是我在 iOS 平台上 **使用频率最高的** 主力代理软件。~~才不是因为花了这么多钱呢！~~ 可以说，正如 Surge 最早设计并完善了现在重要的 **策略组** 特性一样，对于实验性的高级功能，Surge 一般是最早提出并支持的，这些功能也往往会被其他代理软件在后续更新中模仿借鉴。不过，如果你并不需要这些高级特性，那么 Surge 对你来说可能并没有什么吸引力 ~~（毕竟价格太高）~~。况且，Surge 还有一些其他的缺点：

- 不提供 SSR 协议支持
- 一次购买只能给三台设备使用
- 双平台购买成本超过 $100 ~~贵贵贵贵贵死了！~~

#### 推荐资源

- 官方 [Manual](https://manual.nssurge.com/)（英文）
- 官方 [支持社区](https://community.nssurge.com/)
- 开发者写的《[Surge 官方中文指引：理解 Surge 原理](https://manual.nssurge.com/book/understanding-surge/cn/)》
- 我自用的 [配置文件](https://github.com/hly0928/Proxy-profiles/blob/master/Surge/Surge.conf)
- [@Fndroid](https://github.com/Fndroid) 大佬的 [关于策略组的理解](https://github.com/Fndroid/jsbox_script/wiki/%E5%85%B3%E4%BA%8E%E7%AD%96%E7%95%A5%E7%BB%84%E7%9A%84%E7%90%86%E8%A7%A3)
- [@ZHUANGZHUANG](https://zhuangzhuang.cf/) 大佬的 [Surge 配置详解](https://zhuangzhuang.cf/2018-11-14/surge)（部分内容可能过时）
- [@ConnersHua](https://github.com/ConnersHua) 大佬的 [规则仓库](https://github.com/DivineEngine/Profiles/tree/master)

### Quantumult X：最值得推荐

说完 Surge，我们就来谈一谈现在最热门的代理软件：Quantumult X。作为 Quantumult 的船新升级版，Quantumult X 秉承了加量不加价的原则，在支持策略组、JS 脚本等高级功能的基础上，仍保持了 $8 的较低售价（在发售头两天 Quantumult 老用户甚至可以免费领取），实属良心。与其他代理软件相比，Quantumult X 最突出的优势有以下几点：

#### 也许是最好看的外观

![](https://blog.hly0928.com/media/posts/talk-about-some-proxy-apps-on-ios/04.png)

#### 颜控一本满足.png

对我个人而言，Quantumult X 的外观可能是目前所有代理软件中最合我胃口的一个。尤其是它对策略组的处理，兼顾了美观和实用性。

![](https://blog.hly0928.com/media/posts/talk-about-some-proxy-apps-on-ios/05.png)

#### Quantumult X 与 Surge 的策略组界面

Quantumult X 主页面的节点列表支持按配置文件中 `[server_remote]` 部分进行分组；顶部的策略组 + 可自定义图标的设计，不但大大方便了选择，在外观上也比 Surge 更胜一筹。而相比 Shadowrocket，Quantumult X 的设计更有现代感和科技感，~~当然配置也复杂得多。~~

#### 较全面的协议支持

Quantumult X 目前支持 SS, SSR, Vmess, HTTP(S), Trojan 协议。尽管在协议支持上不如 Shadowrocket 那么全面，但也绝对能满足 99% 机场的需要了。特别是如果你有机场仅支持 SSR 协议，那么 Quantumult X 就是一个不错的选择。

#### 功能与价格的最佳平衡

正如上文所说，Quantumult X 在支持许多高级功能的基础上，仍保持了 $8 的较低售价。在功能上，Quantumult X 拥有 Surge 大约 80% - 90% 的功能，所没有的功能（如逻辑规则、DoH）对普通用户而言也非必要；而前者的买断价格还不到后者的 1/6，且不需要后续每年再额外掏钱。

可以说，Quantumult X 凭借良心的售价和优秀的功能，实现了功能与价格之间的最佳平衡。

#### 不得不提的一些不足

尽管 Quantumult X 很好用，但还是有一些不得不提的问题：

##### 规则优先级与自己造轮子

以下内容引自 [神机规则](https://github.com/ConnersHua/Profiles/tree/master) 维护者 [@ConnersHua](https://github.com/ConnersHua)<sup><a href="https://blog.hly0928.com/post/talk-about-some-proxy-apps-on-ios/#ref04">[4]</a></sup>：

> 但是，Quantumult 的作者也有自己的执着造成一些体验问题：
>
> - JS 脚本远程砍了（这个放在第一点说其实是我基本不用脚本，而且这是盗版党造成的）
> - VMess URI 自己造标准（这就是很多人经常说的为什么扫一扫、订阅链接添加不上 v2 协议是不是不支持 balabala）
> - 规则类型优先级问题，在我看来这是很多余的设计，本来就是简单的前面规则覆盖后面规则的行为，非要搞类型优先级，那么就带来一些使用场景问题：
>
> （在订阅时 DOMAIN 会转换成 host，这个 host 也是 Quantumult 作者自己造的轮子，以下仍以 DOAMIN 表述）
>
> DOMAIN-KEYWORD 规则优先级带来的问题：
>
> 1. 本来 `DOMAIN-KEYWORD,adservice,REJECT` 就能解决的问题，如果有条代理或者直连规则为 xxx.com 而它有广告域名为 adservice.xxx.com 我还要专门写一条 `DOMAIN,adservice.xxx.com,REJECT`
> 2. 在自定义规则时，比如想对 Instagram 进行指定节点，那么你用 `DOMAIN-KEYWORD,instagram,ProxyA` 就存在优先级问题，因为其他人的规则中就可能存在 Instagram 的域名如 `DOMAIN-SUFFIX,instagram.com,PROXY` 和 `DOMAIN-SUFFIX,cdninstagram.com,PROXY`
>
> USER-AGENT 规则优先级带来的问题：
>
> 1. 对于不同应用使用统一域名时不能再简单的使用 User-Agent 规则进行分流，比如说 YouTube 和 YouTube Music，其主要传输内容域名均为 googlevideo.com ，这时候你是不能写两条 DOMAIN-SUFFIX 的，那么在 Surge 一类的工具上简单的做法就是加一条 YouTube Music 的 UA 如 `USER-AGENT,com.google.ios.youtubemusic*,PROXY` 和 `USER-AGENT,YouTubeMusic*,PROXY`，但是在 X 中 UA 类型规则优先级极低也就没法用
> 2. 有一些游戏应用是通过看广告解锁功能，解决方法也同上在广告规则前以 UA 规则指定直连来覆盖广告规则，但是同样是优先级问题造成没法用
>
> 如果说 DOMAIN-KEYWORD 规则的优先级问题解决方式是麻烦，那么 USER-AGENT 规则的优先级问题就是无解

如上所述，Quantumult X 没有完全采用 Surge 等软件规则按顺序匹配的设定，而是搞了一套莫名其妙的优先级系统，进而导致了规则维护中的种种问题。另外，在规则类型的写法上，Quantumult X 也没有采用 Surge 等软件的 `DOMAIN`，而是写成了 `host`（尽管写成 `DOMAIN` 也能用）、没有采用 `IP-CIDR6` 而是写成了 `ip6-cidr`，等等。这些地方在普通用户眼中可能无关紧要，但会给规则维护者带来一定的不便。同时，一些 URI 标准上的自己造轮子，也可能会给小白用户带来困扰。

##### 不支持远程 JS 脚本

**提示：** 此问题目前基本解决了，但是不排除作者以后再次改动的可能。

这一点在上面的引述中也提到了。目前，Quantumult X 只有 TestFlight (TF) 版支持远程 JS 脚本，商店版~~在 v1.0.3 后移除了相关支持~~ v1.0.10 又把远程脚本加回来了，~~但是每个脚本都要手动缓存还是很麻烦~~现在使用时长足够之后，脚本就能直接作为远程资源缓存了。~~如果你有 JS 脚本方面的需求，那么只能借助 WorkingCopy 等软件本地挂载脚本库<sup><a href="https://blog.hly0928.com/post/talk-about-some-proxy-apps-on-ios/#ref05">[5]</a></sup>，或是使用 Surge 或下文中的 Loon。~~

##### 上手难度较高

Quantumult X 中的细节和隐藏设计较多，上手难度可能是这几款软件中最高的。如果你不需要高级功能、只想简单使用，那么 Quantumult X 可能并不适合你。

#### 小结

Quantumult X 是我目前在 iOS 平台上 **最推荐** 的代理软件。如果你有一定高级功能的需求，又不想~~大出血~~买 Surge，那么 Quantumult X 无疑是你的最佳选择。

#### 推荐资源

- 官方 [示例配置](https://github.com/crossutility/Quantumult-X/blob/master/sample.conf)
- 我自用的 [配置文件](https://github.com/hly0928/Proxy-profiles/blob/master/QuantumultX/QuantumultX.conf)
- [Qure 图标组](https://github.com/Koolson/Qure)
- Shawn 大佬的 [Quantumult X 不完全教程](https://www.notion.so/Quantumult-X-1d32ddc6e61c4892ad2ec5ea47f00917)（非常详细全面，强烈推荐）

### Shadowrocket：性价比最高，真香

说完了上面两款功能复杂的软件，让我们谈谈简单一点的 Shadowrocket。自从上架以来，小火箭就以其 $3 的价格广受好评，成为了最适合新手入门使用的代理软件。其最大的优势有以下几点：

#### 性价比无敌

相比于 Surge 的「天价」和 Quantumult X 仍稍显昂贵的 $8，小火箭 3 刀的价格毫无疑问要亲民得多。作为性价比最高的代理软件，可以说，不管你最后是否将其当成主力使用，买一个小火箭都不会吃亏。

#### 最全面的协议支持

如果 Quantumult X 算「较全面的协议支持」，那么小火箭无疑是「最全面的协议支持」。除了支持常见的 SS, SSR, Vmess, HTTP(S), Socks5, Snell, Trojan 协议，小火箭还拥有最全面的混淆 / 加密支持，能够解析多种形式的 SS(R) 订阅，兼容 99.99% 的机场。另外，小火箭对新协议的兼容一般也会快于其他代理软件。

#### 上手简单

作为最适合新手使用的代理软件，小火箭的界面简单易懂，学习成本也极低：填入机场订阅、选择节点、随便导入一个远程规则（甚至不用）就能用了。相比于上面两款软件复杂的配置文件，小火箭傻瓜化的操作对需求不高的用户而言更友好。

#### 小结

Shadowrocket 是我在 iOS 上买的第一款代理软件。关于它，其实没有太多好说的。如果你对功能要求不高，那么买小火箭准没错。当然，相比其他软件，小火箭尽管价格便宜，但也有一些小问题：

- 耗电量和稳定性表现不如 Surge / Quantumult X
- 策略组、脚本等功能简陋，~~约等于没有~~
- MitM 不稳定，去广告能力有限
- 界面一般般，不过不难看

### Quantumult：停更了？

在 Quantumult X 上架之前，Quantumult 是经常拿来跟小火箭对比的存在。不过，在 X 推出之后，Quantumult 已经有七个多月没有更新了<sup><a href="https://blog.hly0928.com/post/talk-about-some-proxy-apps-on-ios/#ref06">[6]</a></sup>。

![](https://blog.hly0928.com/media/posts/talk-about-some-proxy-apps-on-ios/06.png)

#### Quantumult 主界面

在我第一次用上 Quantumult 的时候，最吸引我的就是其主界面世界地图的设计。Quantumult 会基于服务器 IP 大致判断其地理位置并显示在地图上，这比起当时普普通通的 Shadowrocket 来说，的确给人以耳目一新的感觉。不过，Quantumult 也有一些问题，比如策略组不能随时切换、SS 订阅没有组设定会弹出警告、UDP 转发不够完善等等。

长话短说，**鉴于 Quantumult 已经超过半年未更新，因此不推荐任何用户购买 Quantumult。** 如有需要，请选择上文的 Quantumult X。

### Loon：潜力无限

因为听说要涨价了，所以前天我花 $3 入手了 Loon ~~留着传家~~。从目前的状态来看，Loon 还处于开发初期，许多地方还不完善 ~~（像英文本地化都把 Dashboard 写成 Dsahboard 了草）~~。不过，从已有的功能来看，Loon 在一定程度上综合了 Surge 和 Quantumult X 的优点，发展潜力巨大。

![](https://blog.hly0928.com/media/posts/talk-about-some-proxy-apps-on-ios/07.png)

#### Loon 主界面

从外观上来说，Loon 主界面借鉴了 Surge 的设定，但改为了双栏显示，方便操作；从功能上来说，Loon 目前有下面一些优势：

- 支持 SS, SSR, Vmess 协议
- 支持导入 Surge Ruleset，方便编写规则
- 支持类 Surge 的策略组写法
- 支持类 Quantumult X 的订阅 Rewrite (`rewrite_remote`)
- 支持本地过滤节点，无需借助 API
- 支持远程脚本

如果 Loon 后续能保持更新维护，那么它很有可能成为 Quantumult X 的一大竞品。

#### 推荐资源

- Feng 大佬的 [Loon 不完全教程](https://www.notion.so/Loon-f0a98c39f5224c09b281c79837380431)

### 小结

目前看来，功能最强大的代理软件仍是 Surge；但普通用户使用 Quantumult X / 小火箭也足矣。另外，如果你有自定义配置文件的需求，不妨研究一下 [subconverter](https://github.com/tindy2013/subconverter/blob/master/README-cn.md) 和 [Surgio](https://surgio.royli.dev/)。在当前日益恶劣的互联网环境下，不仅要选择适合自己的代理软件，更要有稳定高速的线路、合理的规则、策略组与配置文件，才能获得无墙般的上网体验。

### 广告时间

推荐一个自用的机场（链接含 aff）：

- [Dler Cloud](https://dlercloud.com/auth/register?affid=51479)（墙洞）

---

#### ↩︎ 注

1. 参考 [Surge Manual - Proxy Rule](https://manual.nssurge.com/rule.html)
2. 参考 [Surge Tech Community - Surge iOS 4.3.0 以上版本关于 DNS-over-HTTPS 的修改和配置指引](https://community.nssurge.com/d/248-surge-ios-430-dns-over-https)
3. 参考 [Surge Tech Community - Module](https://community.nssurge.com/d/225-module)
4. 来源 [V2EX - Quantumult (X) 和 Shadowrocket 有何优劣？](https://www.v2ex.com/t/642077)
5. 参见 [本地/iCloud 文件夹挂载实现 Github 脚本库实时同步](https://www.notion.so/iCloud-Github-948f19e65e1a47b3b468451491a3f34b)
6. 参考 [App Store - Quantumult](https://apps.apple.com/us/app/quantumult/id1252015438)
