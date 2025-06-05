---
created: 2024-08-03T12:00:00
source: https://linmi.cc/42154.html
type: archive-web
modified: 2025-01-15T11:38:18
---

上周做了一个有意思的玩具，用于录入我现有的实体书籍到 Notion 里面，方便我进行管理。

* 首先是有些书我会时不时的翻出来看，比如少楠赠予我的《悉达多》；

* 我还会把书籍进行出售，回回血，毕竟在外租房有些书有点重，这里也需要进行数据的记录。

* 实际使用中，我还会关联书籍到我的日记，关联后我直接在日记下面写想法，然后用同步块进行同步。

结合上面所说，这个玩具对于我这种实体数据比较多的人，还是减少了录入成本。借着之前我在社交媒体发的内容，要兑现诺言，所以本文就顺水推舟的出来啦～

如果你对这个工具感兴趣的话，这里我提供了两个版本：极客版本供喜欢折腾的同学使用，速通版本供对于折腾不感冒的同学使用。

? 如果你只想使用，请直接滑动到懒人包部分，直接下载对应的捷径与模板。

其实这个想法 Mayne 在早些年就做了，好像是没有放出来。至于我为什么会做，很大程度上因为我最近在学编程，想把自己学的东西付诸于实践。

言归正传，书籍扫码录入到 Notion，实际实现思路很简单：

1. 找到提供扫码能力的工具，快捷指令就支持扫码解析；

2. 把参数传给对应的 API，让 API 返回解析数值后的数据；

3. 把返回的解析数据导入到 Notion 中，实现导入。

![Untitled](https://vip1.loli.io/2022/03/27/6FHuts4U9W8SBRa.png)

所以关于上面流程实现，你需要准备以下东西：

1. 一个 Notion 账号；

2. 准备一台 iPhone，拥有捷径功能，用于扫码。Android 理论上也可以，但是需要有类似捷径的支持；

3. 准备一台服务器，用于中转解析，当然也可以尝试使用 Google 提供的 API；

4. 准备一台电脑，需要有一些编码工作；

那接下里就开始我们的操作，首先是获取到我们想要的数据。目前 ISBN 支持获取的免费 API 并不多，我找到的有 Google，但是大部分同学可能无法访问。

```

https://www.googleapis.com/books/v1/volumes?q=isbn:0771595158

```

另外还想看看书籍的豆瓣评分，那只能使用豆瓣的 API 来实现了，遗憾的是，豆瓣的 API 已经关停。

```

https://api.douban.com/v2/book/isbn/9787543632608

```

遗憾的是原接口已经不再提供，只能自己搭建，具体可以看这篇文档：[豆瓣 ISBN 查询 API 接口制作教程](https://cloud.tencent.com/developer/article/1460050)。

具体逻辑就是直接解析豆瓣网页，自定义生成 API，代码比较好理解，毕竟是世界上最好的编程语言来写的。

**创建 database**

创建一个 database 的页面，之后给属性分别命名好，我这里就直接使用了书籍名、作者、介绍、豆瓣评分等。具体大家可以参考这张图来进行定制。

![CleanShot 2022-03-27 at 19.02.52](https://vip1.loli.io/2022/03/27/nOvdMqj8LFUpoVA.png)

**创建机器人，获取 Token**

前往 <https://www.notion.so/my-integrations>，点击「New integration」创建一个机器人，输入名字、Logo，需要用到的空间、全选上支持的能力（读取、更新、写入内容）、基本上调整前面三个，后面默认就好。

![Untitled](https://vip2.loli.io/2022/03/27/7gyB23UGQ6JACez.png)

创建完成后，复制创建好的机器人 Token，我们后面需要用到。

![Untitled](https://vip1.loli.io/2022/03/27/2MLlaGrmFf9JRuZ.png)

再前往创建好的数据库邀请机器人。

![Untitled](https://vip1.loli.io/2022/03/27/fUDyQePTGlgxABh.png)

至此 Notion 配置部分就完成啦。

再接下来就是我们捷径的编辑流程，这里面建议大家拆步骤来做。

**扫码功能**

首先是确定扫码功能，在捷径中搜索「扫码」，这里可以解析条形码和二维码；

![Untitled](https://vip1.loli.io/2022/03/27/3Ijkq6PGRrD2SA5.png)

**链接解析**

接着搜索「获取 URL 内容」来解析链接，从 URL 内容中获取词典，也就是我们需要导入 Notion 的数据。

![Untitled](https://vip2.loli.io/2022/03/27/ja7JrwTGgQidO6F.png)

**写入 Notion**

再接着是写入数据到 Notion，也就是借助 Notion API 功能，这里具体 API 使用请参考：[Notion API 文档](https://developers.notion.com/reference/intro)。

首先去复制一下数据库的链接，速通版本做成了可配置，具体根据个人习惯自行配置。

```

https://www.notion.so/linmi/a8aec43384f447ed84390e8e42c2e089?v=...
  - |--------- Database ID --------|

```

我这里是直接拿到 JSON 去匹配数据，不然挨个加词典加数组真的让人头大，偶尔还会崩溃。粘贴你的 Token 和 database\_id。

![Untitled](https://vip2.loli.io/2022/03/27/6BfKqYOG3SPhosk.png)

JSON 数据格式代码放在下方了，请注意替换掉我标注的数据，不然运行会报错。

```

```

我们试着拿出一本书测试看看。嗯，我这边成功了。

![Untitled](https://vip2.loli.io/2022/03/27/RYdmiCufASjByTG.png)

考虑到部分同学没有时间或者相关知识背景来折腾这件事，我准备了一个相应简单的版本，只要点一点，复制粘贴就可以了。

复制模板：[图书扫描录入](https://www.notion.so/f7c827199f58479b9349c690eee2965f) ，接着复制 database 的链接 id。

```

https://www.notion.so/linmi/a8aec43384f447ed84390e8e42c2e089?v=...
  - |--------- Database ID --------|

```

创建机器人，具体参考极客版的「Notion 配置」环节，创建完成后，复制机器人的 Token，备用；

![Untitled](https://vip1.loli.io/2022/03/27/2MLlaGrmFf9JRuZ.png)

保存捷径到设备上，[捷径链接](https://www.icloud.com/shortcuts/c06b76465bb74ba3ba1f75d0e6a5459c)，接着点击编辑捷径，将 Token 、Database ID 填写到指定位置；

![Untitled](https://vip2.loli.io/2022/03/27/W2vO7Vts8wKNgFD.png)

添加机器人到刚刚创建好的模板上；

![Untitled](https://vip1.loli.io/2022/03/27/fUDyQePTGlgxABh.png)

启动捷径，安心开始使用吧。

有什么问题欢迎评论，如果是程序错误之类的，请录制屏幕或者详细描述你的操作步骤。对了，这个 API 是我自己服务器提供，后续可能会存在无法使用的情况，届时我会在本文同步更新快捷指令的链接。

还有的聊的话，就是功能的迭代，比如加上扫描去重。

**{{postData.favorites\_isset ? ' 已收藏 ' : ' 收藏 '}}**
