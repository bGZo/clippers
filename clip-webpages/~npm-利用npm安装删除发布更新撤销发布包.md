---
title: "【npm】利用npm安装/删除/发布/更新/撤销发布包"
aliases: "【npm】利用npm安装/删除/发布/更新/撤销发布包"
created: 2025-04-05T17:34:59
modified: 2025-04-05T17:34:59
description: "提纲：1.什么是npm? 2.利用npm安装包 3.利用npm删除包 4.利用npm 发布包 5.利用npm撤销发布的包6.npm发包后的更新 7.npm的版本控制标准——Semantic versioning"
source: "https://www.cnblogs.com/penghuwan/p/6973702.html"
tags:
tags-link:
type: "archive-web"
---
提纲：1.什么是npm? 2.利用npm安装包 3.利用npm删除包 4.利用npm 发布包 5.利用npm撤销发布的包6.npm发包后的更新 7.npm的版本控制标准——Semantic versioning

**目录**

- [什么是npm?](https://www.cnblogs.com/penghuwan/p/#_label0)
- [利用npm安装包](https://www.cnblogs.com/penghuwan/p/#_label1)
- [npm安装的方式——本地安装和全局安装](https://www.cnblogs.com/penghuwan/p/#_label1_0)
- [利用npm删除包](https://www.cnblogs.com/penghuwan/p/#_label2)
- [删除全局模块](https://www.cnblogs.com/penghuwan/p/#_label2_0)
- [删除本地模块](https://www.cnblogs.com/penghuwan/p/#_label2_1)
- [利用npm 发布包](https://www.cnblogs.com/penghuwan/p/#_label3)
- [第一次发布包：](https://www.cnblogs.com/penghuwan/p/#_label3_0)
- [非第一次发布包：](https://www.cnblogs.com/penghuwan/p/#_label3_1)
- [利用npm撤销发布包](https://www.cnblogs.com/penghuwan/p/#_label4)
- [npm更新发布后的包：](https://www.cnblogs.com/penghuwan/p/#_label5)

**正文**

 ![](https://img2018.cnblogs.com/blog/1060770/201908/1060770-20190825195301725-571534857.png)

## **什么是npm?**

npm是javascript的**包管理工具**，是**前端模块化**下的一个标志性产物

简单地地说，就是**通过npm下载模块，复用已有的代码，提高工作效率**

1.**从社区的角度**：把针对某一特定问题的模块发布到npm的服务器上，供社区里的其他人下载和使用，同时自己也可以在社区里寻找特定的模块的资源，解决问题

2.**从团队的角度**：有了npm这个包管理工具，复用团队既有的代码也变的更加地方便

## **利用npm安装包**

### **npm安装的方式——本地安装和全局安装**

**什么时候用本地／全局安装？**

1.当你试图安装命令行工具的时候，例如 grunt CLI的时候，使用全局安装

全局安装的方式：npm install -g 模块名称

2.当你试图通过npm install 某个模块，并通过require('XXX')的方式引入的时候，使用本地安装

本地安装的方式：npm install 模块名称

**你很可能遇到的问题**

在你试图本地安装的时候一般都会遇到permission deny的问题

例如我这里第一次尝试全局安装express，输入npm install -g express

![](https://images2015.cnblogs.com/blog/1060770/201706/1060770-20170609201942418-242164591.png)

【吐槽】而且让人无语的是在安装了许多依赖后才提醒你权限不够...

**解决方式：**

**1.** **sudo npm install -g XXX ，以管理员的身份安装**

评价：每次都要输入账号和密码，非常繁琐，且官方并不推荐（ You could also try using sudo, but this should be avoided）

**2.** **sudo chown -R 你的账号名 npm所在目录的路径 /{lib/node\_modules,bin,share}**

评价：官方推荐的做法，chown全称为change owner，即将npm目录的所有者指定为你的名字（授予权限），-R表示对指定目录下所有的子目录和文件也都采取同种操作。

**<1>**首先，通过 npm config get prefix获取npm所在目录的路径，例如像这样：

![](https://images2015.cnblogs.com/blog/1060770/201706/1060770-20170609202020403-1849902170.png)

**<2>**在命令行输入 sudo chown -R 你的账号名 npm所在目录的路径 /{lib/node\_modules,bin,share}，例如：

![](https://images2015.cnblogs.com/blog/1060770/201706/1060770-20170609202153637-337797609.png)

【注意】{lib/node\_modules,bin,share}中的大括号是要写上去的

再次全局安装express：输入npm install -g express

![](https://images2015.cnblogs.com/blog/1060770/201706/1060770-20170609202238168-910572638.png)

安装成功

**3.sudo chmod 777 npm所在目录（不推荐）**

评价：这是网上经常能够看到的解决方式，但，官方教程里没有对此有任何提及。chmod代表change mode更改读写模式，对该目录授予最高权限，任何人可读可写，这是很危险的

**本地安装的时候，将依赖包信息写入package.json中**

注意一个问题，在团队协作中，一个常见的情景是他人从github上clone你的项目，然后通过npm install安装必要的依赖，（刚从github上clone下来是没有node\_modules的，需要安装）那么**根据什么信息安装依赖呢？就是你的package.json中的dependencies和devDepencies**。所以，在本地安装的同时，**将依赖包的信息（要求的名称和版本）写入package.json中是很重要的！**

**npm install 模块**：安装好后不写入package.json中

**npm install 模块 --save** 安装好后写入package.json的dependencies中（生产环境依赖）

**npm install 模块 --save-dev** 安装好后写入package.json的devDepencies中（开发环境依赖）

示例：

我在项目下安装webpack：进入项目终端输入npm install

安装完毕后我的package.json

![](https://images2015.cnblogs.com/blog/1060770/201706/1060770-20170609202309231-32863709.png)

卸掉webpack再重装:输入npm install webpack --save后：

![](https://images2015.cnblogs.com/blog/1060770/201706/1060770-20170609202350653-1716772622.png)

卸掉webpack再重装:npm install webpack --save-dev后：

![](https://images2015.cnblogs.com/blog/1060770/201706/1060770-20170609202405137-2114842377.png)

## **利用npm删除包**

删除模块其实很简单：

### **删除全局模块**

npm uninstall -g <package>利用npm

### **删除本地模块**

npm uninstall 模块

删除本地模块时你应该思考的问题：**是否将在package.json上的相应依赖信息也消除？**

**npm uninstall 模块**：删除模块，但不删除模块留在package.json中的对应信息

**npm uninstall 模块 --save** 删除模块，同时删除模块留在package.json中dependencies下的对应信息

**npm uninstall 模块 --save-dev** 删除模块，同时删除模块留在package.json中devDependencies下的对应信息

## **利用npm 发布包**

发布包之前你首先要有一个npm的账号

### **第一次发布包：**

在终端输入npm adduser，提示输入账号，密码和邮箱，然后将提示创建成功

### **非第一次发布包：**

在终端输入npm login，然后输入你创建的账号和密码，和邮箱，登陆

【注意】npm adduser成功的时候默认你已经登陆了，所以不需要再接着npm login.

**例子：**

（因为我已经创建过账号了，所以直接登录）

1.进入项目目录下，然后再登陆：

![](https://images2015.cnblogs.com/blog/1060770/201706/1060770-20170609202446840-1610696376.png)

2.通过npm publish发包

![](https://images2015.cnblogs.com/blog/1060770/201706/1060770-20170609202514403-849332036.png)

包的名称和版本就是你项目里package.json里的name和version哦！

![](https://images2015.cnblogs.com/blog/1060770/201706/1060770-20170609202540872-285752890.png)

3然后你到npm的搜索里就可以找到被发布的APP啦！

![](https://images2015.cnblogs.com/blog/1060770/201706/1060770-20170609202554387-223704071.png)

**【注意点1】不能和已有的包的名字重名！**

例如我尝试把包名改成'react'显然已有的包：

![](https://images2015.cnblogs.com/blog/1060770/201706/1060770-20170609202622778-691361295.png)

然后发包的时候就会...

![](https://images2015.cnblogs.com/blog/1060770/201706/1060770-20170609202701200-1982551319.png)

(翻译：你没有发布react包的权限，请问你是以react所有者的身份登陆的吗？)

【提示】在发包前可以通过npm的搜索引擎查找是否已存在相同名称的包

**【注意点2】还有一点要注意的是npm对包名的限制：不能有大写字母/空格/下滑线!**

(其实在上面的例子中我原本打算写成penghuwanAPP的，报错。。。改成penghuwan\_app，又报错，最后不得不改成penghuwanapp。。。)

![](https://images2015.cnblogs.com/blog/1060770/201706/1060770-20170609202724981-936653704.png)

![](https://images2015.cnblogs.com/blog/1060770/201706/1060770-20170609202749747-1696746026.png)

**【注意点3】你的项目里有部分私密的代码不想发布到npm上？**

将它写入.gitignore 或.npmignore中，上传就会被忽略了

## **利用npm撤销发布包**

这里要说一点，取消发布包可能并不像你想象得那么容易，这种操作是受到诸多限制的，撤销发布的包被认为是一种不好的行为

**（试想一下你撤销了发布的包\[假设它已经在社区内有了一定程度的影响\]，这对那些已经深度使用并依赖你发布的包的团队是件多么崩溃的事情！）**

示例：

我现在将之前发布的包penghuwanapp撤销掉：输入npm unpublish 包名

![](https://images2015.cnblogs.com/blog/1060770/201706/1060770-20170609202809872-2061110882.png)

 【吐槽】注意看红框框住的字，你就知道npm官方撤销已发布的包对这种行为的态度了....

 【注意】如果报权限方面的错，加上--force

再去npm搜索已经搜不到了

![](https://images2015.cnblogs.com/blog/1060770/201706/1060770-20170609202853184-1883393075.png)

1根据规范，只有在发包的**24小时内才允许**撤销发布的包（ unpublish is only allowed with versions published in the last 24 hours）

2**即使**你撤销了发布的包，**发包的时候也不能再和被撤销的包的名称和版本重复了**（即不能名称相同，版本相同，因为这两者构成的唯一标识已经被“占用”了）

例如我在撤销包后尝试再发布同一名称+同一版本的包：

![](https://images2015.cnblogs.com/blog/1060770/201706/1060770-20170609202937153-1561244414.png)

报错，并建议我修改包的版本

**npm unpublish的推荐替代命令：npm deprecate <pkg>\[@<version>\] <message>**

使用这个命令，**并不会在社区里撤销你已有的包，但会在任何人尝试安装这个包的时候得到警告**

例如：npm deprecate penghuwanapp '这个包我已经不再维护了哟～'

## **npm更新发布后的包：**

事实上npm更新包和发布包的命令是一样的，都是npm publish,**不同之处在于，你需要修改包的版本**

所以步骤是：

1.修改包的版本（package.json里的version字段）

2.npm publish

关于修改版本的细节请看下面：

**七.npm的版本控制——Semantic versioning**

在我们的package.json里面有一个version字段。那么，怎么在项目不断构建的过程中调整版本呢？

**npm有一套自己的版本控制标准——Semantic versioning（语义化版本）**

**具体体现为：**

对于"version":"x.y.z"

**1.修复bug,小改动，增加z**

**2.增加了新特性，但仍能向后兼容，增加y**

**3.有很大的改动，无法向后兼容,增加x**

例如：我原本的项目是1.0.0版本的话

若是1中情况，变为1.0.1

若是2中情况，变为1.1.0

若是3中情况，变为2.0.0

**通过npm version <update\_type>自动改变版本**

**update\_type为patch, minor, or major其中之一，分别表示补丁，小改，大改**

例如我在shell去改动项目版本

![](https://images2015.cnblogs.com/blog/1060770/201706/1060770-20170609202952606-1996233874.png)

再来看看我的package.json，已经变成了v1.0.0

![](https://images2015.cnblogs.com/blog/1060770/201706/1060770-20170609203024153-897310699.png)

【完】

![](https://images2015.cnblogs.com/blog/1060770/201706/1060770-20170609204919106-712660263.png)