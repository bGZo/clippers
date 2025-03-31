---
title: "如何拷贝软连接(symbol link)? - 问题求助 - 小众软件官方论坛"
aliases: "如何拷贝软连接(symbol link)? - 问题求助 - 小众软件官方论坛"
created: 2025-03-31T22:20:09
modified: 2025-03-31T22:20:09
description: "当我对软连接进行拷贝粘贴的时候, 它操作的对象是软连接的目标文件. 而我只想拷贝粘贴软连接本身, 请问在windows下, 有办法吗？"
source: "https://meta.appinn.net/t/topic/56698"
tags:
tags-link:
type: "archive-web"
---
xcopy可以，命令是XCOPY source \[destination\] /b  
fastcopy也可以，在设置里有相关选项  
如果你用其他专业的文件管理器，可能也有相关的设置（反正TotalCMD是没有），Double Commander是有的  
[![](https://doublecmd.github.io/doc/en/images/imgDC/copymove1.png)](https://doublecmd.github.io/doc/en/images/imgDC/copymove1.png)