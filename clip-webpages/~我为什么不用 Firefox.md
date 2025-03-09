---
created: 2024-10-12T12:00:00
source: {{nav-ri https://blog.skk.moe/post/why-not-use-firefox/}}
type: archive-web
modified: 2025-01-15T11:38:18
---

最近一直被「抛弃 Chrome 使用 Firefox」的言论包围着。然而我一直坚持使用 Chrome，因为 Firefox 并不像 Mozilla 所说的那样「生为民，不作恶」，也并没有鼓吹者说的那么优秀。

当然我也不是完全不使用 Firefox，至少测试浏览器兼容性还需要用到它，但它注定在未来一段时间里都不会成为我的主力浏览器。

本篇文章我将详细列出我认为 Firefox 不如 Chrome 之处，同时会驳斥一些 Firefox 鼓吹者的观点。

## 开发路线混乱
  - Chrome 的 UI/UX 都在遵循 Google 自己的设计语言，从传统界面到 Material Design。但是 Firefox 的 UI/UX 从传统界面到 Australis 界面再到现在的 Photon 界面，改成和 Chrome 相似的样子；然后仿佛就跟标签栏用直角还是圆角这件事情干上了，一会直角改圆角，一会圆角改直角。在 UI 这件事情上可以看出，Google 自己有清晰的设计语言，然而 Mozilla 内部的开发路线（至少早期）是相对混乱的。

## 扩展插件不友好
  - 经常听到有人说 Firefox 的扩展插件非常丰富、比 Chrome 应用市场的要多；在 Chrome 不断收紧第三方扩展插件的情况下，Firefox 更开放。是的，Chrome 不断限制扩展插件的自由是事实，但是又有多少人记得 Firefox 当年在扩展上走的弯路？Firefox 曾经花大力气做起自己的标准 Addon SDK 扩展接口。好不容易插件开发者都迁移完毕了，Mozilla 又看中了 Chrome 当时已然占据先机的插件市场，又把 Firefox 的扩展接口迁移到 WebExtension。Mozilla 对扩展插件的开发者很短的时间去重新迁移，而 Firefox 自己在整合 WebExtension 时也是困难重重；最后那些来不及迁移新接口的插件被 Mozilla 全部下架，老用户积累多年的扩展和主题就这么付诸东流。

## 网络中立性
  - Chrome 在 69 版本时爆出一个巨大的隐私危机，Chrome 在用户清除所有 cookie 时不会清除 `*.google.*` 下的 cookie，缺乏网络中立性。
  - Firefox 可能在清除 cookie 上对所有网站一视同仁，但是在对待不同地域的用户却并不是公平的。如果你身在中国（或者是使用中国 IP）访问 Mozilla 官网，最后都会强制跳转到北京谋智火狐的 `www.firefox.com.cn`，哪怕你使用代理服务不使用中国 IP 访问 Mozilla 原始官网甚至直接访问 Mozilla FTP 服务，但是 Mozilla 为简体中文编译打包的浏览器都是中国定制版，最明显的就是默认内置并使用 `i.firefoxchina.cn` 「中国特色导航主页」，尚不能确定（但已经被 Mozilla 承认存在）夹带了多少中国特供版的私货。
  - 如果你需要下载纯净的 Firefox，竟然需要下载繁体中文版，然后下载安装简体中文语言包，接着还需要修改 `about:config` 中的相关配置。至少，Google 只分发同一种 Chrome，没有针对地区的特供版；至少十年前，Google 还有毅力和魄力和中国政府说 Byebye。

## Firefox 的性能
  - Firefox 使用 Rust 编写的 Servo 内核，极大提升了 页面渲染和排版 的性能，同时避免了很多使用 C++ 编写（如 WebKit）的内核的安全漏洞，这是有目共睹的。但是因此就说 Rust 是新语言、Servo 安全漏洞一定更少的言论明显是荒唐和不负责任的。而且如今前端开发大多依赖三大框架 Angular/Vue/React，JavaScript 引擎的性能同样至关重要。或许 Firefox 在量子计划中用 Rust 重写了 JavaScript 的解析，但是 Google 有 V8——目前仍然是全球最快的 JavaScript 运行引擎，不接受任何反驳。而且在 Firefox 上对 WebFont 的渲染实质上是落后数年的 FOUT，对用户的体验并不友好。
  - 有人说 Chrome 占用内存比 Firefox 多很多，但是就我个人测试来看，打开完全相同的标签页、Firefox 不启用任何扩展而 Chrome 启用三个扩展以后，Firefox 的内存占用比 Chrome 还多。大家也可以自己试试，你会发现 Firefox 在内存管理上和 Chrome 相比并没有优势。

## Firefox 维护 CA 列表的隐患
  - 赛门铁克 CA 在诸多浏览器巨头响应之下，最终退出了历史的舞台。最早是由 Chrome 发起的对赛门铁克证书取消信任让大众怀疑浏览器是否有能力左右 CA，同时也有人怀疑微软是否会向政府妥协而 增加/删除 Windows 中的 受信任证书列表。同时，鼓吹者认为 Mozilla 是不盈利组织，所以不会受到任何威胁和强权的影响。但是，Firefox 自己维护的 CA 列表似乎提升了对 XP 的兼容性，却实际上比 Chrome 更容易做出取消信任一家 CA 的事情、而且 Mozilla 已经有向中国政府妥协的先例了、加上 Mozilla 还在试图不断扩张市场，你认为 Mozilla 是不会妥协的么？
  - Firefox 的 Dev Tools 看似有中文、看似对每一个条目都有通往 MDN 的链接，对开发者非常贴心，但是实际上却是非常简陋的。没有详细的瀑布图、HTML5Storage 难以调试、无法调试 Service Worker 也不能输出 Service Worker 相关日志、在模拟移动端显示上也没有 Chrome 做得好，Firefox 也没有 Chrome 的 Audit(Lighthouse) 这样的工具。
  - 经过几年混乱的开发和错误的营销推广方式，Mozilla 着眼于提升 Firefox 的市场占有率，为此 Firefox 为了与 Chrome 争抢市场份额，放弃忠实老用户，从 UI/UX 上全面抄袭、在扩展接口上模仿，为中国用户提供特供版等等。你真的认为 Mozilla 还是那个「生为民，不作恶」的非营利性组织么？
  - 请务必注意。本文接下来的内容和指控基于「一位**自称** Mozilla 核心开发者、高管」的言论。如果他**是真的 Mozilla 高层人物**，那么接下来看到的内容**会颠覆你对 Firefox 和 Mozilla 的认知**；如果他**和 Mozilla 八竿子打不着边**，那么大家**完全可以当个笑话来看**，无伤大雅。
  - 这里是这位「Mozilla 核心开发者」的声明。既然有他这句话在，我接下来的消息截图就不再进行打码处理。
  - 这张图是有关「Mozilla 核心开发者」对他自己是 Mozilla 一员的直接、间接的声明，接下来的指控都基于他是 Mozilla 核心开发者的**假设**。如果他**真的是 Mozilla 雇员**，则**下述基于假设的指控全部成立**。

## 代码审计不自由不公正
  - 由于这位 Mozilla 核心开发者和一位对 Firefox 色彩管理有异议的人之间的冲突，Mozilla 核心开发者便限制了所有 Bugzilla 上关于色彩管理方面的 issue 的讨论、甚至发出禁用 Mozilla 相关账号的威胁。
  - 你还相信 Firefox 的代码是开源和自由的、代码审计是公开公正的、你的 Firefox 账户是安全的么？

## 用户数据保管不善
  - 「由我在内四个人保管」「乱成一锅粥」
  - 可以看出 Mozilla 内部的危机应对机制匮乏，而且对于 Firefox Account 数据的保管极不妥善。你还会把你的书签和浏览历史一厢情愿地交给 Mozilla 保管么？

## 对 Web 开发者的态度
  - 「暂停冻结 MDN 的翻译」、「移除全部其它语种」，你还觉得这个非营利性组织的所作所为还靠谱么。如果这真的是 Mozilla 会议做出的决议，那么我就立刻弃用 MDN 去阅读 Google 的 Web Foundation，因为不敢想象是什么样的人在监管社区对 MDN 的贡献、以及 MDN 是否还可靠。
  - 当然你可以说这个人根本和 Mozilla 没有任何关系，就一假冒的。是的，如果他 **不是 Mozilla 雇员** 那还谢天谢地，不然 Firefox 就真的玩完了；然而如果不幸他 **真的是 Mozilla 雇员** 且 **他的身份和权力确有其事**，那我还是推荐大家立刻抛弃 Firefox 来用 Chrome 吧。商业化公司或许会不再遵守自己「不作恶」的承诺，但是在现有的体量之下至少还会有一些些顾忌、不敢肆意妄为。
