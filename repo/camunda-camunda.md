---
title: camunda/camunda
aliases: camunda
created: 2023-09-10T12:00:00
modified: 2025-06-07T16:06:46
description: provides a workflow and decision automation platform offering process orchestration capabilities to organizations of any size. 开源的商业流程引擎平台，基于 Java 开发，可以内嵌集成到 Java 应用、SpringBoot 应用中，也可以独立运行。Camunda 支持 BPMN 2.0，用于工作流和过程自动化；CMMN，用于案例管理；DMN，用于业务决策管理。
source: https://github.com/camunda/camunda
tags: workflow
tags-link: 
type: repo
wikipedia: https://en.wikipedia.org/wiki/Camunda
---

## Repo Meta

![](https://img.shields.io/github/stars/camunda/camunda?style=for-the-badge&label=stars) ![](https://img.shields.io/github/repo-size/camunda/camunda?style=for-the-badge&label=size) ![](https://img.shields.io/github/created-at/camunda/camunda?style=for-the-badge&label=since)

[![](https://github-readme-stats.vercel.app/api/pin/?username=camunda&repo=camunda&bg_color=00000000)](https://github.com/camunda/camunda)

## How
  - 工作流相关介绍
    - **BPM**(BusinessProcessManagement)，业务流程管理是一种管理原则，通常也可以代指 BPMS(BusinessProcessManagementSuite)，是一个实现整合不同系统和数据的流程管理软件套件.
    - **BPMN**(BusinessProcessModelandNotation) 是基于流程图的通用可视化标准。该流程图被设计用于创建业务流程操作的图形化模型。业务流程模型就是图形化对象的网状图，包括活动和用于定义这些活动执行顺序的 `流程设计器`。BPMN2.0 正式版本于 2011 年 1 月 3 日发布，常见的 `工作流引擎` 如：Activiti、Flowable、jBPM 都基于 BPMN 2.0 标准。
    - 然后来看看 BPM 的发展历程：
    - \![[image-20220830005000114.png]]
  - Camunda 介绍
    - 官网地址： https://camunda.com/
    - 中文站点： http://camunda-cn.shaochenfeng.com/
    - 下载： https://downloads.camunda.cloud/release/camunda-bpm/run/7.15/
    - 案例地址：[Congratulation! | docs.camunda.org](https://docs.camunda.org/get-started/quick-start/complete/)
    - 前期准备工作: JAVA1.8 以上的 JRE 或 JDK

## 1.Camunda Modeler
- Camunda Modeler 是 Camunda 官方提供的一个流程设计器，用于编辑流程图以及其他模型【表单】，也就是一个流程图的绘图工具。可以官方下载，也可以在提供给大家的资料中获取。获取后直接解压缩即可，注意：解压安装到非中文目录中!!!

\![[image-20220901105936567.png]]

启动的效果：

\![[image-20220901110007447.png]]

## 2.Camunda BPM
- 下载地址 https://camunda.com/download/

Camunda BPM 是 Camunda 官方提供的一个 `业务流程管理` 平台,用来管理，部署的流程定义、执行任务，策略等。下载安装一个 Camunda 平台，成功解压 Camunda 平台的发行版后，执行名为 start.bat（对于 Windows 用户）或 start.sh（对于 Unix 用户）的脚本。此脚本将启动应用程序服务器。

\![[image-20220901110225636.png]]

打开您的 Web 浏览器并导航到 http://localhost:8080/以访问欢迎页面，Camunda 的管理平台。

\![[image-20220718162641800.png]]

登录成功的主页：

\![[image-20220718162726028.png]]

## 3.入门案例
### 3.1 创建简单流程
- 我们先通过 Modeler 来绘制一个简单流程

1.) 创建流程：选择 BPMN diagram (Camunda Platform)

\![[image-20220901110718700.png]]

2.) 创建开始节点：并设定节点名称

\![[image-20220901110850675.png]]

3.) 创建服务节点：设置处理方式

\![[image-20220901110926577.png]]

\![[image-20220901111045576.png]]

我们切换节点的类型为 `service Task`

\![[image-20220901111125584.png]]

\![[image-20220901111141656.png]]

然后我们需要配置 `刷卡付款` 节点，服务类型有很多执行的方法，这次我们使用“external（外部）”任务模式。

\![[image-20220901111330988.png]]

具体配置内容为

\![[image-20220901111419588.png]]

4.) 添加结束节点

\![[image-20220901111521063.png]]

5.) 配置流程参数

点击画布的空白处，右侧的面板会显示当前流程本身的参数,这里我们修改 id 为*payment-retrieval*，id 是区分流程的标识然后修改 Name 为“付款流程”最后确保 `Executable` 是勾选的，只有 `Executable` 被勾选，流程才能执行

\![[image-20220901111725855.png]]

### 3.2 外部任务
- 在上面设计的流程图，`刷卡付款` 节点的处理是外部任务，Camunda 可以使多种语言实现业务逻辑，我们以 Java 为例来介绍。

添加相关的依赖：

```xml
<dependencies>
<dependency>
<groupId>org.camunda.bpm</groupId>
<artifactId>camunda-external-task-client</artifactId>
<version>7.15.0</version>
</dependency>
<dependency>
<groupId>org.slf4j</groupId>
<artifactId>slf4j-simple</artifactId>
<version>1.6.1</version>
</dependency>
<dependency>
<groupId>javax.xml.bind</groupId>
<artifactId>jaxb-api</artifactId>
<version>2.3.1</version>
</dependency>
</dependencies>

```

编写处理的业务逻辑的代码

```java
import org.camunda.bpm.client.ExternalTaskClient;

import java.awt.*;
import java.net.URI;

public class Demo01 {
public static void main(String[] args) {
ExternalTaskClient client = ExternalTaskClient.create()
.baseUrl("http://localhost:8080/engine-rest")
.asyncResponseTimeout(10000) // 长轮询超时时间
.build();
// 订阅指定的外部任务
client.subscribe("charge-card")
.lockDuration(1000)
.handler(((externalTask, externalTaskService) -> {
    // 获取流程变量
    String item = (String) externalTask.getVariable("item");
    Long amount = (Long) externalTask.getVariable("amount");
    System.out.println("item--->"+item + "  amount-->" + amount);
    try {
        Desktop.getDesktop().browse(new URI("https://docs.camunda.org/get-started/quick-start/complete"));
    } catch (Exception e) {
        e.printStackTrace();
    }

    // 完成任务
    externalTaskService.complete(externalTask);
})).open();
}
}

```

运行该方法即可，当流程处理时会执行相关逻辑。

### 3.3 部署流程
- 接下来我们就可以来部署上面定义的流程了。使用 Camunda Modeler 部署流程，点击工具栏中的部署按钮可以将当前流程部署到流程引擎，点击部署按钮，输入 Deployment Name 为 “Payment” ，输入下方 REST Endpoint 为 http://localhost:8080/engine-rest ，然后点击右下角 Deploy 部署

部署操作：

\![[image-20220901102738775.png]]

部署的时候报错：原因是安装路径中有中文

\![[image-20220901101904825.png]]

部署成功：

\![[image-20220901102705446.png]]

然后在 BPM 中我们可以查看部署的流程：

\![[image-20220901112401741.png]]

### 3.4 启动流程
- 我们使用 Rest API 发起流程，所以需要一个接口测试工具（例如：Postman），或者也可以使用电脑自带的 curl

curl 执行如下命令

```curl
curl -H "Content-Type: application/json" -X POST -d '{"variables": {"amount": {"value":555,"type":"long"}, "item": {"value":"item-xyz"} } }' http://localhost:8080/engine-rest/process-definition/key/payment-retrieval/start

```

postman 方式处理

在 url 中输入：http://localhost:8080/engine-rest/process-definition/key/payment-retrieval/start 通过 `POST` 方式提交，提交的方式是 `JSON` 数据，具体内容为：

```json
{
"variables": {
"amount": {
"value":555,
"type":"long"
},
"item": {
"value": "item-xyz"
}
}
}

```

\![[image-20220901112634925.png]]

然后我们点击发送，操作成功可以看到如下的返回信息

\![[image-20220901112709320.png]]

同时任务执行后我们在控制台可以看到相关的信息

\![[image-20220901112810150.png]]

- 案例扩展
- 上面的案例过于简单，我们添加不同的任务节点和网关来丰富下

## 1. 用户任务
### 1.1 添加节点
- 我们在上面的案例中添加一个 `用户任务` 来处理流程。

\![[image-20220903233945199.png]]

点击刚刚创建的 `批准付款` 节点，然后通过扳手设置节点的类型为 `用户任务`(User Task)

\![[image-20220903234050669.png]]

然后设置节点的审批人为 `demo`

\![[image-20220903234231682.png]]

### 1.2 配置表单
- 在 `用户节点` 处我们绑定表单数据。然后创建表单相关的字段，并添加对应的描述信息。

\![[image-20220904001026418.png]]

> amount 字段：
>
> ​ ID:amount
>
> ​ Type:long
>
> ​ Label: 金额
>
> Item 字段：
>
> ​ ID:item
>
> ​ Type:string
>
> ​ Label: 项目
>
> Approved 字段：
>
> ​ ID:approved
>
> ​ Type:boolean
>
> ​ Label: 是否同意

### 1.3 部署流程
- 流程定义好之后我们就可以部署流程了。直接在 `Camunda Modeler` 工具栏上的上传按钮将流程上传到流程引擎中。部署后在 `Camunda Web` 中查看部署的流程。

\![[image-20220904001636662.png]]

### 1.4 测试流程
- 打开任务列表（http://localhost:8080/camunda/app/tasklist/），使用 demo / demo 登录。点击右上角的 `Start process` ，在弹出的对话框中选择“付款流程”.

\![[image-20220904001816475.png]]

这时会弹出编辑流程变量的对话框，可以通过点击 Add a variable 按钮添加变量，这次我们先不添加，直接点击右下角 ` Start ` 启动流程。

\![[image-20220904001902564.png]]

这时，在任务列表应该就能看到刚创建的人工任务了，如果没有可以手动刷新一下

\![[image-20220904001953028.png]]

到这儿这个 `用户任务` 节点的人工审核就应该要处理了，我们在下一个案例中继续这个案例，我们加入排他网关来处理。

## 2.排他网关
- 我们将使用**排他网关**(*Exclusive Gateways*)，为流程添加分支，仅在金额足够大的时候进行人工审核.

### 2.1 添加网关节点
- 首先打开 `Camunda Modeler `，在左侧的工具架中找到网关（菱形），将它拖动到“付款请求”和“刷卡付款”之间，将“批准付款”向下移动再添加一个网关，调整流程，最后看起来类似这样：

\![[image-20220904004632887.png]]

### 2.2 配置网关
- 接下来，我们选择“<1000”的连线，打开属性面板，选择“Condition Type”为“Expression”，这里我们使用 [JAVA统一表达式语言](https://docs.camunda.org/manual/latest/user-guide/process-engine/expression-language/) 编写条件，这里要做的是在金额小于 1000 时直接刷卡付款，则输入表达式 `${amount<1000}`

\![[image-20220904004725626.png]]

同样的，对另一条线也进行配置，表达式为 `${amount>=1000}`

\![[image-20220904004747234.png]]

然后 `是否批准` 的排他网关节点我们也需要处理下

\![[image-20220904004845594.png]]

\![[image-20220904004910392.png]]

### 2.3 部署流程
- 部署流程和上面的操作是一样的。

\![[image-20220904005023089.png]]

### 2.4 测试操作
- 打开任务列表（http://localhost:8080/camunda/app/tasklist/），使用 demo / demo 登录,点击右上角的 Start process ，在弹出的对话框中选择“付款流程”,上面例子中，我们直接点击 Start，但这次我们要增加几个变量来测试动态的流程。

\![[image-20220904005221732.png]]

试着更改 `amount` 的值，查看对流程执行顺序的影响

## 3.决策自动化
- 在上面的案例中我们在审批时是通过 `用户任务` 结合表单来做的审批，本案例我们来看看我们通过 `DMN` 为流程添加一个业务规则来处理

### 3.1 添加业务规则
- 打开 Camunda Modeler，点击 “批准付款”，在右面的扳手菜单中，将类型改为“**Business Rule Task** ”（业务规则任务）

\![[image-20220904113549016.png]]

下一步，将属性面板中的 `Implementation` 选择为 `DMN`，输入 Decision Ref 为 `approve-payment`，为了将决策的结果存入流程变量，我们还需要编辑结果变量 Result Variable 为 `approved`，结果类型 Map Decision Result 选择为 `singleEntry `，最后结果如下：

\![[image-20220904113700661.png]]

### 3.2 创建 DMN 表
- 点击 `File > New File > DMN Diagram` 创建一个新的 DMN,现在画布上已经存在一个决策元素了，选择它，然后在右侧属性面板中更改 `Id` 和 `Name`，这里的 Id 需要和流程中的 `Decision Ref` 属性一致，这次我们输入 Id 为 `approve-payment`

\![[image-20220904113803219.png]]

接下来，点击决策元素左上角的表格按钮，创建新的 DMN 表.

\![[image-20220904113905505.png]]

### 3.3 编辑 DMN 表
- 首先编辑输入参数，在本例中，为了简单，我们依据项目名进行判断，规则可以使用 `FEEL 表达式`、`JUEL` 或者 `Script` 书写，详情可以阅读 https://docs.camunda.org/manual/latest/user-guide/dmn-engine/expressions-and-scripts/
- 双击表格中的*Input*，编辑第一个输入参数
- \![[image-20220904114105012.png]]
- 下面，设置输入参数，双击*Output*编辑
- \![[image-20220904114133016.png]]
- 下面，我们点击左侧的蓝色加号，添加一些规则，最后类似这样：
- \![[image-20220904114210501.png]]

### 3.4 部署 DMN 表
- 点击底部的部署按钮，将 DMN 部署到流程引擎中

\![[image-20220904114317458.png]]

### 3.5 流程案例测试
- 现在打开 http://localhost:8080/camunda/app/cockpit/ ，使用 demo/demo 登录，可以看到决策定义增加了一个，点击进去可以看到刚才编辑的 DMN.

\![[image-20220904114413678.png]]

点击进去可以看到对应的决策信息

\![[image-20220904114452196.png]]

然后我们部署流程然后启动流程

\![[image-20220904114623954.png]]

该流程决策输出的 `approved` 为 true

\![[image-20220904114740904.png]]

更改下输入的参数

\![[image-20220904114822563.png]]

该决策中输出的 `approved` 为 false

\![[image-20220904114913062.png]]

- IDEA 引入流程设计器
- 在工作流引擎中流程设计器是一个非常重要的组件，而 `InterlliJ IDEA` 是 Java 程序员用到的最多的编程工具了。前面在基础篇的介绍中我们都在通过 Camunda 提供的流程设计器绘制好流程图，然后需要单独的拷贝到项目中，要是调整修改不是很方便，这时我们可以在 IDEA 中和流程设计器绑定起来。这样会更加的灵活。

## 1.下载 Camunda Model
- 第一步肯定是需要下载 `Camunda Model` 这个流程设计器，我们前面有介绍。就是之前解压好的目录了。

\![[image-20220907002253021.png]]

## 2.IDEA 中配置
- 我们先进入 `settings` 中然后找到 `tools`,继续找到 `External Tool`.

\![[image-20220907002432482.png]]

\![[image-20220907002649744.png]]

最终效果

\![[image-20220907002735603.png]]

## 3.编辑 bpmn 文件
- 找到您想打开的 bpmn 文件, 点击右键, 找到 External Tools 运行 camunda modler 即可进行文件编写.

\![[image-20220907002851738.png]]

搞定~

- SpringBoot 整合 Camunda

## 1.官方案例说明
- 接下来我们看看怎么在我们的实际项目中来使用 Camunda 了。方式有多种，首先我们可以参考官网提供的整合案例。

\![[image-20220907003810268.png]]

但是这里有个比较头疼的问题就是 Camunda 和 SpringBoot 版本的兼容性问题，虽然官方也给出了兼容版本的对照表。

\![[image-20220907003929928.png]]

但是如果不小心还是会出现各种问题，比如：

\![[image-20220907004050862.png]]

上面就是典型的版本不兼容的问题了。

## 2.官方 Demo
- 为了能让我们的案例快速搞定，我们可以通过 Camunda 官方提供的网站来创建我们的案例程序。地址：https://start.camunda.com/

\![[image-20220907004531764.png]]

生成代码后，解压后我们通过 idea 打开项目，项目结构

\![[image-20220907010229047.png]]

相关的 pom.xml 中的依赖

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">

<modelVersion>4.0.0</modelVersion>

<groupId>com.boge.workflow</groupId>
<artifactId>camunda-project-demo</artifactId>
<version>1.0.0-SNAPSHOT</version>

<properties>
<project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
<maven.compiler.source>8</maven.compiler.source>
<maven.compiler.target>8</maven.compiler.target>
</properties>

<dependencyManagement>
<dependencies>
<dependency>
<groupId>org.springframework.boot</groupId>
<artifactId>spring-boot-dependencies</artifactId>
<version>2.4.3</version>
<type>pom</type>
<scope>import</scope>
</dependency>

<dependency>
<groupId>org.camunda.bpm</groupId>
<artifactId>camunda-bom</artifactId>
<version>7.15.0</version>
<scope>import</scope>
<type>pom</type>
</dependency>
</dependencies>
</dependencyManagement>

<dependencies>
<dependency>
<groupId>org.camunda.bpm.springboot</groupId>
<artifactId>camunda-bpm-spring-boot-starter-rest</artifactId>
</dependency>

<dependency>
<groupId>org.camunda.bpm.springboot</groupId>
<artifactId>camunda-bpm-spring-boot-starter-webapp</artifactId>
</dependency>

<dependency>
<groupId>org.camunda.bpm</groupId>
<artifactId>camunda-engine-plugin-spin</artifactId>
</dependency>

<dependency>
<groupId>org.camunda.spin</groupId>
<artifactId>camunda-spin-dataformat-all</artifactId>
</dependency>

<dependency>
<groupId>org.springframework.boot</groupId>
<artifactId>spring-boot-starter-web</artifactId>
</dependency>

<dependency>
<groupId>com.h2database</groupId>
<artifactId>h2</artifactId>
</dependency>

<dependency>
<groupId>org.springframework.boot</groupId>
<artifactId>spring-boot-starter-jdbc</artifactId>
</dependency>

</dependencies>

<build>
<plugins>
<plugin>
<groupId>org.springframework.boot</groupId>
<artifactId>spring-boot-maven-plugin</artifactId>
<version>2.4.3</version>
</plugin>
</plugins>
</build>

</project>
```

属性文件的配置信息

```yaml
spring.datasource.url: jdbc:h2:file:./camunda-h2-database

camunda.bpm.admin-user:
id: demo
password: demo
```

然后通过启动类启动程序

\![[image-20220907010434493.png]]

访问服务：http://localhost:8080/

\![[image-20220907010523901.png]]

## 3.MySQL 数据库
- 上面的例子我们数据存储在了 H2 这个内存型数据库，我们可以切换到 `MySQL` 数据库。首先我们需要导入相关的 SQL 脚本。位置就在我们之前下载的 `Camunda Web` 服务中。

\![[image-20220907010729453.png]]

执行创建所有必需的表和默认索引的 SQL DDL 脚本。上面两个脚本都要执行。

\![[image-20220907011030798.png]]

生成的相关表结构比较多，因为本身就是基于 Activiti 演变而来，所以有 Activiti 基础的小伙伴会非常轻松了。简单介绍下相关表结构的作用。

* **ACT_RE** ：'RE' 表示 repository。 这个前缀的表包含了流程定义和流程静态资源 （图片，规则，等等）。
* **ACT_RU**：'RU' 表示 runtime。 这些运行时的表，包含流程实例，任务，变量，异步任务，等运行中的数据。 Flowable 只在流程实例执行过程中保存这些数据， 在流程结束时就会删除这些记录。 这样运行时表可以一直很小速度很快。
* **ACT_HI**：'HI' 表示 history。 这些表包含历史数据，比如历史流程实例， 变量，任务等等。
* **ACT_GE**： GE 表示 general。 通用数据， 用于不同场景下
* **ACT_ID:** ’ID’表示 identity(组织机构)。这些表包含标识的信息，如用户，用户组，等等。

具体的表结构的含义:

| **表分类**   | **表名**              | **解释**                                           |
| ------------ | --------------------- | -------------------------------------------------- |
| 一般数据     |                       |                                                    |
|              | [ACT_GE_BYTEARRAY]    | 通用的流程定义和流程资源                           |
|              | [ACT_GE_PROPERTY]     | 系统相关属性                                       |
| 流程历史记录 |                       |                                                    |
|              | [ACT_HI_ACTINST]      | 历史的流程实例                                     |
|              | [ACT_HI_ATTACHMENT]   | 历史的流程附件                                     |
|              | [ACT_HI_COMMENT]      | 历史的说明性信息                                   |
|              | [ACT_HI_DETAIL]       | 历史的流程运行中的细节信息                         |
|              | [ACT_HI_IDENTITYLINK] | 历史的流程运行过程中用户关系                       |
|              | [ACT_HI_PROCINST]     | 历史的流程实例                                     |
|              | [ACT_HI_TASKINST]     | 历史的任务实例                                     |
|              | [ACT_HI_VARINST]      | 历史的流程运行中的变量信息                         |
| 流程定义表   |                       |                                                    |
|              | [ACT_RE_DEPLOYMENT]   | 部署单元信息                                       |
|              | [ACT_RE_MODEL]        | 模型信息                                           |
|              | [ACT_RE_PROCDEF]      | 已部署的流程定义                                   |
| 运行实例表   |                       |                                                    |
|              | [ACT_RU_EVENT_SUBSCR] | 运行时事件                                         |
|              | [ACT_RU_EXECUTION]    | 运行时流程执行实例                                 |
|              | [ACT_RU_IDENTITYLINK] | 运行时用户关系信息，存储任务节点与参与者的相关信息 |
|              | [ACT_RU_JOB]          | 运行时作业                                         |
|              | [ACT_RU_TASK]         | 运行时任务                                         |
|              | [ACT_RU_VARIABLE]     | 运行时变量表                                       |
| 用户用户组表 |                       |                                                    |
|              | [ACT_ID_BYTEARRAY]    | 二进制数据表                                       |
|              | [ACT_ID_GROUP]        | 用户组信息表                                       |
|              | [ACT_ID_INFO]         | 用户信息详情表                                     |
|              | [ACT_ID_MEMBERSHIP]   | 人与组关系表                                       |
|              | [ACT_ID_PRIV]         | 权限表                                             |
|              | [ACT_ID_PRIV_MAPPING] | 用户或组权限关系表                                 |
|              | [ACT_ID_PROPERTY]     | 属性表                                             |
|              | [ACT_ID_TOKEN]        | 记录用户的 token 信息                                |
|              | [ACT_ID_USER]         | 用户表                                             |

然后我们在 SpringBoot 项目中导入 `MySql` 的依赖，然后修改对应的配置信息

```xml
<dependency>
<groupId>mysql</groupId>
<artifactId>mysql-connector-java</artifactId>
</dependency>
```

修改 `application.yaml`。添加数据源的相关信息。

```yaml
# spring.datasource.url: jdbc:h2:file:./camunda-h2-database

camunda.bpm.admin-user:
id: demo
password: demo
spring:
datasource:
driver-class-name: com.mysql.cj.jdbc.Driver
url: jdbc:mysql://127.0.0.1:3306/camunda1?serverTimezone=Asia/Shanghai
username: root
password: 123456
camunda:
bpm:
database:
type: mysql
schema-update: true
auto-deployment-enabled: false # 自动部署 resources 下的 bpmn文件
```

然后启动项目，发现数据库中有了相关记录，说明操作成功

\![[image-20220907011831014.png]]

- Camunda 专题讲解
- 用了整合的基础我们就可以来完成一个流程审批的案例了

## 1.部署流程

```java
@RestController
@RequestMapping("/flow")
public class FlowController {

@Autowired
private RepositoryService repositoryService;

@GetMapping("/deploy")
public String deplopy(){
Deployment deploy = repositoryService.createDeployment()
.name("部署的第一个流程") // 定义部署文件的名称
.addClasspathResource("process.bpmn") // 绑定需要部署的流程文件
.deploy();// 部署流程
return deploy.getId() + ":" + deploy.getName();
}
}
```

启动后访问接口即可

## 2.启动流程
- 启动流程我们通过单元测试来操作

```java
package com.boge.workflow;


import org.camunda.bpm.engine.RepositoryService;
import org.camunda.bpm.engine.RuntimeService;
import org.camunda.bpm.engine.TaskService;
import org.camunda.bpm.engine.runtime.ProcessInstance;
import org.camunda.bpm.engine.task.Task;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import java.util.List;

@SpringBootTest(classes = Application.class)
public class ApplicationTest {

@Autowired
private RepositoryService repositoryService;

@Autowired
private RuntimeService runtimeService;

@Autowired
private TaskService taskService;

/**
* 启动流程的案例
*/
@Test
public void startFlow(){
// 部署流程
ProcessInstance processInstance = runtimeService
.startProcessInstanceById("1a880f27-2e57-11ed-80d9-c03c59ad2248");
// 部署的流程实例的相关信息
System.out.println("processInstance.getId() = " + processInstance.getId());
System.out.println("processInstance.getProcessDefinitionId() = " + processInstance.getProcessDefinitionId());
}


}

```

## 3.查询待办
- 查询待办也就是查看当前需要审批的任务，通过 TaskService 来处理

```java
/**
* 查询任务
*    待办
*
*  流程定义ID:processDefinition : 我们部署流程的时候会，每一个流程都会产生一个流程定义ID
*  流程实例ID:processInstance ：我们启动流程实例的时候，会产生一个流程实例ID
*/
@Test
public void queryTask(){
List<Task> list = taskService.createTaskQuery()
//.processInstanceId("eff78817-2e58-11ed-aa3f-c03c59ad2248")
.taskAssignee("demo1")
.list();
if(list != null && list.size() > 0){
for (Task task : list) {
System.out.println("task.getId() = " + task.getId());
System.out.println("task.getAssignee() = " + task.getAssignee());
}
}
}
```

## 4.完成任务

```java
/**
* 完成任务
*/
@Test
public void completeTask(){
// 根据用户找到关联的Task
Task task = taskService.createTaskQuery()
//.processInstanceId("eff78817-2e58-11ed-aa3f-c03c59ad2248")
.taskAssignee("demo")
.singleResult();
if(task != null ){
taskService.complete(task.getId());
System.out.println("任务审批完成...");
}
}
```

## What
### [The Universal Process Orchestrator | Camunda](https://camunda.com/)
## References
- https://www.bilibili.com/video/BV1Ng411S7Ve
