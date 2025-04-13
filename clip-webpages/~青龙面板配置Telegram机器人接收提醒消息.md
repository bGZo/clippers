---
title: "青龙面板配置Telegram机器人接收提醒消息 - 逍遥观世界"
aliases: "青龙面板配置Telegram机器人接收提醒消息 - 逍遥观世界"
created: 2025-04-12T10:45:31
modified: 2025-04-12T10:45:43
description: "青龙面板配置Telegram机器人接收提醒消息，上篇文章我们记录了青龙面板的搭建，还没有搭建青龙面板的朋友点击这里。这次我们来演示一下使用TG机器人来接受青龙面板的通知设置 逍遥观世界"
source: "https://www.xiaoyao01.com/qlmasztghprtx/"
tags:
tags-link:
type: "archive-web"
---

上篇文章我们记录了青龙面板的搭建，还没有搭建青龙面板的朋友 [点击这里](https://www.xiaoyao01.com/jddzjdjcqlmacj/)。这次我们来演示一下使用 TG 机器人来接收青龙面板的通知设置

## 新建 TG 机器人

在 Telegram 搜索【@BotFather】

[![](https://www.xiaoyao01.com/wp-content/uploads/2021/12/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20211212190710.png)](https://www.xiaoyao01.com/wp-content/uploads/2021/12/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20211212190710.png)

点击【开始】-- 输入【/newbot】

[![](https://www.xiaoyao01.com/wp-content/uploads/2021/12/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20211212190916.png)](https://www.xiaoyao01.com/wp-content/uploads/2021/12/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20211212190916.png)

给你的机器人起名字。名字自定义。[![](https://www.xiaoyao01.com/wp-content/uploads/2021/12/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20211212191135.png)](https://www.xiaoyao01.com/wp-content/uploads/2021/12/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20211212191135.png)

编辑个 tg 机器人的用户名自定义以 "\*\*\*\_bot" 结尾，便可获取到 token

[![](https://www.xiaoyao01.com/wp-content/uploads/2021/12/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20211212191612.png)](https://www.xiaoyao01.com/wp-content/uploads/2021/12/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20211212191612.png)

重新搜索【@getuseridbot】-- 点击【/start】便可获取到你的 ID

[![](https://www.xiaoyao01.com/wp-content/uploads/2021/12/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20211212191901.png)](https://www.xiaoyao01.com/wp-content/uploads/2021/12/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20211212191901.png)

## 对接青龙面板

打开你的青龙面板选择【系统设置】---【通知设置】

[![](https://www.xiaoyao01.com/wp-content/uploads/2021/12/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20211212192527.png)](https://www.xiaoyao01.com/wp-content/uploads/2021/12/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20211212192527.png)

在【通知方式】选择【Telegram 机器人】

[![](https://www.xiaoyao01.com/wp-content/uploads/2021/12/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20211212192613.png)](https://www.xiaoyao01.com/wp-content/uploads/2021/12/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20211212192613.png)

【telegramBotToken】就是我们刚才创建 TG 机器人时获取到的**token**

【telegramBotUserId】ID 就是我们在**@getuseridbot**获取到的**ID**

输入好**token**和**ID**后点击**保存**

[![](https://www.xiaoyao01.com/wp-content/uploads/2021/12/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20211212193054.png)](https://www.xiaoyao01.com/wp-content/uploads/2021/12/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20211212193054.png)

然后选择【配置文件】

在配置文件中找到**第 3 项 Telegram  对应位置输入 token 和 ID。要输入在“”内。**

[![](https://www.xiaoyao01.com/wp-content/uploads/2021/12/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20211212193403.png)](https://www.xiaoyao01.com/wp-content/uploads/2021/12/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20211212193403.png)

这样我们的 TG 机器人通知就设置好了。

你可以测试一下

先在 TG 搜索你的机器人，就是我们刚设置【\*\*\_bot】的用户名。

在【定时任务】中找到【京东资产变动通知】点击运行。如果设置正确那么选择 tg 机器人就会接受到通知了！

[![](https://www.xiaoyao01.com/wp-content/uploads/2021/12/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20211212194252.png)](https://www.xiaoyao01.com/wp-content/uploads/2021/12/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20211212194252.png)
