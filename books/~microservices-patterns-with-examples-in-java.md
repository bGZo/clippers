---
cover: https://img9.doubanio.com/view/subject/s/public/s34666774.jpg
author: 克里斯·理查森（Chris Richardson）
created: 2022-12-13
isbn: 9787111624127
lang: chinese
published: 20190501
rating: ⭐⭐⭐⭐
status: book/reading
tags: #microserver #java
type: book/dev
douban: https://book.douban.com/subject/33425123
weread: 
---

- [microservices-patterns/ftgo-application: Example code for the book Microservice patterns](https://github.com/microservices-patterns/ftgo-application);
## ![微服务架构设计模式 by 克里斯·理查森](../assets/book_微服务架构设计模式_克里斯·理查森_chris_richardson.pdf)
  - `([\u4e00-\u9fa5，。？；：”“、]) ([\u4e00-\u9fa5，。？；：”“、])`
    `$1$2`
    #regex
  - `(\w+) (\w+)`
## CONTENT
  - 写给中文版读者的话
    - 我想对本书的读者说：
      - 第一，要记住微服务不是解决所有问题的万能 “银弹”
        - ^^Silver bullet, 万金油^^, via: [Silver bullet - Wikipedia](https://en.wikipedia.org/wiki/Silver_bullet) & [银色子弹 - 维基百科，自由的百科全书](https://zh.wikipedia.org/wiki/%E9%8A%80%E8%89%B2%E5%AD%90%E5%BD%88)
      - 第二，编写整洁的代码和使用自动化测试至关重要，因为这是现代软件开发的基础
      - 第三，关注微服务的本质，即**服务的分解和定义，而不是技术**，如容器和其他工具
      - 第四，确保你的服务松耦合，并且可以独立开发、测试和部署，不要搞成分布式单体 (Distributed Monolith), 那将会是巨大的灾难。
      - 第五，也是最重要的，不能只是在技术上采用微服务架构。 拥抱DevOps的原则和实践，在组织结构上实现跨职能的自治团队，这必不可少。
      - 还必须记住：
        - 实现微服务架构并不是你的目标。你的目标是加速大型复杂应用程序的开发。
  - 译者序
  - 中文版序一
  - 中文版序二
  - 前言
    - > 我最喜欢的格言之一是：未来已经到来，只是还没有平均分布。
      > －－－威廉·吉布森，科幻小说作家
      >
    - 本书内容安排
      - 第1章描述了所谓"单体地狱"的症状，当单体应用程序超出其架构时会出现这种问题，这可以通过采用微服务架构来规避。这一章还概述了微服务架构模式语言，这也是本书大部分内容的主题。
      - 第2章解释了为什么软件架构很重要，描述了可用于将应用程序分解为服务集合的模式，并解释了如何克服在此过程中遇到的各种障碍。
      - 第3章 介绍了微服务架构中强大的==进程间通信的几种模式==，解释了为什么异步和基于消息的通信通常是最佳选择。
      - 第4章 介绍如何使用==Saga模式维护服务间的数据一致性==
        - Saga是通过传递异步消息的方式进行协调的一系列本地事务。
      - 第5章 介绍如何使用==领域驱动设计(DDD)的聚合和领域事件等模式==为服务设计业务逻辑
      - 第6章 以第5章为基础，解释了如何使用==事件溯源模式==开发业务逻辑，事件溯源模式是一种以事件为中心的设计思路，用来构建业务逻辑和持久化领域对象。
      - 第7章 介绍如何使用 API 组合模式或命令查询职责隔离(CQRS)模式，这两个模式用来实现查询分散在多个服务中的数据。
      - 第8章 介绍了处理来自各种外部客户端请求的外部API模式，例如移动应用程序、基于浏览器的JavaScript应用程序和第三方应用程序。
      - 第9章 是关于微服务自动化测试技术的两章中的第一章，介绍了重要的测试概念
        - 例如测试金字塔，描述了测试套件中每种测试类型的相对比例，还展示了如何编写构成测试金字塔基础的单元测试。
      - 第10章 以第9章为基础，描述了如何在测试金字塔中编写其他类型的测试，包括集成测试、消费者契约测试和组件测试等。
      - 第11章介绍了开发生产就绪服务的各个方面，包括安全性、外部化配置模式和服务可观测性模式。服务可观测性模式包括日志聚合、应用指标和分布式追踪。
      - 第12章 介绍了可用于部署服务的各种==部署模式==，包括虚拟机、容器和Serverless模式。还介绍了使用服务网格的好处，服务网格是在微服务架构中处理服务间通信的一个网络软件层。
      - 第13章介绍了如何通过采用==绞杀者(Strangler)模式==逐步将单体架构重构为微服务架构，绞杀者模式是指以服务形式实现新功能，从单体中提取模块将其转换为服务。
  - 引言
  - 第1章 逃离单体地狱
    - 1.1 迈向单体地狱的漫长旅程
      - 1.1.1 FTGO应用程序的架构
      - 1.1.2 单体架构的好处
      - 1.1.3 什么是单体地狱
    - 1.2 为什么本书与你有关
    - 1.3 你会在本书中学到什么
    - 1.4 拯救之道：微服务架构
      - 1.4.1 扩展立方体和服务
      - 1.4.2 微服务架构作为模块化的一种形式
      - 1.4.3 每个服务都拥有自己的数据库
      - 1.4.4 FTGO的微服务架构
      - 1.4.5 微服务架构与SOA的异同
    - 1.5 微服务架构的好处和弊端
      - 1.5.1 微服务架构的好处
      - 1.5.2 微服务架构的弊端
    - 1.6 微服务架构的模式语言
      - 1.6.1 微服务架构并不是“银弹”
      - 1.6.2 模式和模式语言
      - 1.6.3 微服务架构的模式语言概述
    - 1.7 微服务之上：流程和组织
      - 1.7.1 进行软件开发和交付的组织
      - 1.7.2 进行软件开发和交付的流程
      - 1.7.3 采用微服务架构时的人为因素
  - 第2章 服务的拆分策略
    - 2.1 微服务架构到底是什么
      - 传统上，架构的目标是可扩展性、可靠性和安全性。但是今天，该架构能够**快速安全地交付软件**，这一点非常重要
      - 2.1.1 软件架构是什么，为什么它如此重要
        - 2个专门讨论该主题的会议
          - [O&#39;Reilly的软件架构会议](https://conferences.oreilly.com/software-architecture)
          - [SATURN会议](https://resources.sei.cmu.edu/news-events/events/saturn)
        - 软件架构是什么
          -            > 计算机系统的软件架构是构建这个系统所需要的一组结构，包括软件元素、 它们之间的关系以及两者的属性。
            > — Len Bass 等著《Documenting Software Architectures: Views and Beyond》 From [卡耐基梅隆大学软件工程研究所](http://www.sei.cmu.edu)
            >
            - 但其实质是应用程序的架构是将 软件分解为元素 (element) 和这些元素之间的关系 (relation )
        - 分解**重要**
          - 它促进了**劳动和知识的分工**
            - 它使具有特定专业知识的人们 (或多个团队) 能就应用程序高效地协同工作
          - 它定义了**软件元素的交互方式**
        - 将软件分解成元素以及定义这些元素之间的关系，决定了软件的能力
        - 软件架构的 4+1 视图模型
          - ＋1是指场景
            - 它负责把视图串联在一起
            - 每个场景负责描述在一个视图中的多个架构元素如何协作, 以完成一个请求
              - 例如
                - 在逻辑视图中的场景，展现了类是如何协作的
                - 在进程视图中的场景，展现了进程是如何协作的。
          - More via ((63959db5-f30c-467a-970d-68960d208fae))
        - 架构**重要**
          - 帮助应用程序满足了第 2 类需求 -> **非功能性需求**
            - 也称之为**质量属性需求 / "能力"**
            - 非功能性需求决定一个应用程序在**运行时的质量 (可扩展性和可靠性)**;
              - 也决定了**开发阶段的质量 (可维护性, 可测试性, 可扩展性和可部署性)**
          - 第 1 类是功能性需求
            - 这些需求决定一个应用程序做什么
            - 通常都包含在用例（use case) / 用户故事 (user story) 中
            - 应用的架构其实跟这些功能性需求没什么关系
            - 功能性需求可以通过任意的架构来实现，甚至是非常糟糕的大泥球架构
      - 2.1.2 什么是架构的风格
        - 建筑风格的概念也适用软件
        - David Garlan和MaryShaw (An Introducti on to Software Architecture, January 1994 ) 这两位软件架构学科的先驱定义了如下[架构风格](https://www.cs.cmu.edu/afs/cs/project/able/ftp/intro_softarch/intro_softarch.pdf)
          - > 因此，架构风格根据结构组织模式定义了一系列此类系统。更具体地说，架构风格确定可以在该风格的实例中使用的组件和连接器的词汇表，以及关于如何组合它们的一组约束。
            >
        - 分层式架构风格
          - 分层架构将软件元素按 "层" 的方式组织
          - 每个层都有明确定义的职责
          - 分层架构还限制了层之间的依赖关系
            - 每一层只能依赖于紧邻其下方的层（如果严格分层）或其下面的任何层
          - 可以将分层架构应用于前面讨论的四个视图中的任何一个
          - 流行的三层架构 (MVC, Controller负责MV的通信) 是应用于**逻辑视图**的分层架构
            - 它将应用程序的类组织到以下层中
              - 表现层 (View)
                - 包含实现用户界面或外部API 的代码
              - 业务逻辑层 (Model)
                - 包含业务逻辑
              - 数据持久化层 (Model Object)
                - 实现与数据库交互的逻辑
                -                  >[!note]
                  > 明显的弊端
                  - 单个表现层
                    - 它无法展现应用程序可能不仅仅由 单个系统调用的事实
                  - 单一数据持久化层
                    - 它无法展现应用程序可能与多个数据库进行交互的事实
                  - 将业务逻辑层定义为依赖千数据持久化层
                    - 理论上，这样的依赖性会妨碍你在没有数据库的情况下测试业务逻辑
                  - **错误地表示了精心设计的应用程序中的依赖关系**
                    - 业务逻辑通常定义数据访问方法的接口或接口库
                    - 数据持久化层则定义了实现存储库接口的 DAO类
                      - 换句话说，依赖关系与分层架构所描述的相反
        - 六边形架构
          - ![image.png](../assets/book/Microservices-Patterns-With-Examples-in-Java/image_1670991548098_0.png)
          - 应用程序具有一个或多个入站适配器，而不是表示层
            - 它通过调用业务逻辑来处理来自外部的请求
          - 应用程序具有一个或多个出站适配器，而不是数据持久化层
            - 这些出站适配器由业务逻辑调用并调用外部应用程序
          - 此架构的一个关键特性和优点
            - **业务逻辑不依赖于适配器**
              - 相反，各种适配器都依赖业务逻辑
          - 业务逻辑具有一个或多个端口 (port）
            - 端口定义了一组操作，关于业务逻辑如何与外部交互
              - 例如，在Java中，端口通常是Java接口。
            - 有两种端口
              - 入站端口
                - 业务逻辑公开的API, 它使外部应用程序可以调用它
                - 入站端口的一个实例是服务接口，它定义服务的公共方法
              - 出站端口
                - 业务逻辑调用外部系统的方式
                - 出站端口的一个实例是存储库接口，它定义数据访问操作的集合
          - 业务逻辑的周围是适配器
            - 有两种类型的适配器
              - 入站适配器
                - 入站适配器通过调用入站端口来处理来自外部世界的请求
                - 入站适配器的一个实例是 SpringMVC Controller,
                  - 它实现一组 REST接口 (endpoint) 或一组Web页面
                - 另一个实例是订阅消息的消息代理客户端
                  - 多个入站适配器可以调用相同的入站端口
              - 出站适配器
                - 出站适配器实现出站端口，并通过调用外部应用程序或服务处理来自业务逻辑的请求
                - 2 个实例
                  - 实现访问数据库的操作的数据访问对象 ( DAO)类
                  - 调用远程服务的代理类。出站适配器也可以发布事件。
          - 好处
            - 将业务逻辑与适配器中包含**的表示层和数据访问层的逻辑分离开来**
              - 业务逻辑不依赖于表示层逻辑或数据访问层逻辑
              - 由于这种分离，**单独测试业务逻辑要容易得多**
            - 它更准确地反映了现代应用程序的架构
              - 可以通过多个适配器调用业务逻辑，每个适配器实现特定的API 或用户界面
              - 业务逻辑还可以调用多个适配器，每个适配器调用不同的外部系统。六边形架构是描述微服务架构中每个服务的架构的好方法
      - 2.1.3 微服务架构是一种架构风格
        - 微服务架构的实现视图由多个组件构成：一组可执行文件或 WAR文件
          - 单体模式: [Monolithic Architecture pattern](https://microservices.io/patterns/monolithic.html)
            - ![image.png](../assets/book/Microservices-Patterns-With-Examples-in-Java/image_1670993623992_0.png)
          - 微服务模式: [Microservice Architecture pattern](https://microservices.io/patterns/microservices.html)
            - ![image.png](../assets/book/Microservices-Patterns-With-Examples-in-Java/image_1670993647342_0.png)
              - Related
                - ![image.png](../assets/book/Microservices-Patterns-With-Examples-in-Java/image_1670993811612_0.png)
        - 微服务架构的组件是服务，连接器是使这些服务能够协作的通信协议
          - 每个服务都有自己的逻辑视图架构，通常也是六边形架构
        - FTGO 应用程序可能的微服务架构
          - ![image.png](../assets/book/Microservices-Patterns-With-Examples-in-Java/image_1670997157617_0.png)
          - 此架构中的服务对应于业务功能，例如订单管理和餐馆管理
        - 服务
          - 服务是一个单一的、可独立部署的软件组件，它实现了一些有用的功能。
            - ![image.png](../assets/book/Microservices-Patterns-With-Examples-in-Java/image_1670997366838_0.png)
              - 显示了服务的外部视图，在此示例中是 Order Service
              - 服务具有 API , 为其客户端提供对功能的访问
                - API 由命令、查询和事件组成
                - 命令如 createOrder() 执行操作并更新数据
                - 查询如 findOrderByid() 检索数据
              - 有两种类型的操作
                - 命令
                - 查询
              - 服务还发布由其客户端使用的事件，例如 OrderCreated
          - 服务的 API 封装了其内部实现。
            - 与单体架构不同，开发人员无法绕过服务的 API直接访问服务内部的方法或数据。因此，微服务架构强制实现了应用程序的模块化。
          - 微服务架构中的每项服务都有自己的架构，可能还有独特的技术栈。
            - 但是典型的服务往往都具有六边形架构
              - 其API 由与服务的业务逻辑交互的适配器实现
            - 操作适配器调用业务逻辑，事件适配器对外发布业务逻辑产生的事件。
        - 松耦合 Loose coupling
          - 服务之间的交互采用 API 完成，这样做就封装了服务的实现细节。
            - 这允许服务在不影响客户端的情况下，对实现方式做出修改。松耦合服务是改善开发效率、提升可维护性和可测试性的关键。小的、松耦合的服务更容易被理解、修改和测试。我们通过 API 来实现松耦合服务之间的协调调用，这样就避免了外界对服务的数据库的
          - 直接访问和调用
            - 服务自身的待久化数据就如同类的私有属性一样，是不对外的。保证数据的私有属性是实现松耦合的前提之一。这样做，就允许开发者修改服务的数据结构，而不用提前与其他服务的开发者互相协商。这样做在运行时也实现了更好的隔离。例如，一个服务的数据库加锁不会影响另外的服务。但是你稍后就会看到在服务间不共享数据库的弊端, 特别是处理数据一致性和跨服务查询都变得更为复杂
        - 共享类库的角色
        - 服务的大小并不重要
          - 目标不是一个 "微" 字, 更好的目标是
            - **将精心设计的服务定义为能够由小团队开发的服务，并且交付时间最短，与其他团队协作最少**
              - 理论上，团队可能只负责单一服务，因此服务绝不是微小的。相反，如果服务需要大型团队或需要很长时间进行测试，那么拆分团队或服务可能是有意义的。另外，如果你因为其他服务的变更而不断需要同步更新自己负责的服务，或者你所负责的服务正在触发其他服务的同步更新，那么这表明服务没有实现松耦合。你构建的甚至可能是一个分布式的单体。
          - 微服务架构把应用程序通过一些小的、松耦合的服务组织在一起。结果，这样的架构提升了开发阶段的效率，特别是可维护性、可测试性和可部署性，这也就让组织的软件开发速度更快。微服务架构也同时提升了应用程序的可扩展性，尽管这不是微服务的主要目标。为了使用微服务架构开发软件，你首先需要识别服务，并确定它们之间如何协作。现在我们来看看如何定义一个应用程序的微服务架构。
    - 2.2 为应用程序定义微服务架构
      - 三步式流程
        - ![image.png](../assets/book/Microservices-Patterns-With-Examples-in-Java/image_1670998184381_0.png)
        - 1.定义系统操作
          - 不是根据特定的进程间通信技术（如 REST 或消息）来描述这些请求，而是**使用更抽象的系统操作**这个概念
            - 系统操作 (system operation ) 是应用程序必须处理的请求的一种抽象描述。它既可以是更新数据的命令，也可以是检索数据的查询。每个命令的行为都是根据抽象领域模型定义的，抽象领域模型也是从需求中派生出来的。系统操作是描述服务之间协作方式的架构场景。
        - 2.定义服务
          - 有几种策略可供选择, 但策略的最终结果都是围绕业务概念而非技术概念分解和设计的服务
            - 定义与业务能力相对应的服务
              - 一种源于业务架构学派的策略
            - 围绕领域驱动设计的子域来分解和设计服务
              - > If we use _domain-driven design subdomains_(领域驱动设计的子域) to decompose and design services, the example would change to reflect the subdomains that are relevant to the domain of the e-commerce website.
                > For example, we might identify subdomains such as search, checkout, and delivery within the domain of the e-commerce website.
                > Then, we would design services that correspond to each of these subdomains, such as a search service for handling product searches, a checkout service for handling purchases, and a delivery service for handling product deliveries.
                > This approach would allow us to manage and use these services in a way that is aligned with the subdomains of the domain, and it could potentially improve the efficiency of the e-commerce website.
                > #chatGPT
                >
        - 3.定义服务 API 和协作方式
          - 将 1 中标识的每个系统操作分配给服务
            - 服务可以完全独立地实现操作
            - 需要与其他服务协作
              - 确定服务的协作方式
                - 另外一个服务来支持其他操作
                  - 进程间通信机制
          - 服务的分解有 4 个障碍需要克服
            - 1.网络延迟
              - 服务之间的网络往返太多，特定的分解将是不切实际的
                - ==优化下来的时间全砸到网络延时了, 追平甚至反超==
            - 2.服务之间的同步通信降低了可用性
              - 你可能需要使用第 3 章中描述的自包含服务的概念
            - 3.需要维护跨服务的数据一致性
              - 你需要使用第 4 章中讨论的 Saga
            - 4.所谓的上帝类 (GodClass)
              - 它广泛应用在整个应用程序中
                - 使用领域驱动设计中的概念来消除上帝类
                  - > This means defining clear boundaries for different parts of the system and the language used to describe them. This can help to prevent a single class from becoming overly large and unmanageable. Additionally, using the concept of aggregation and small, focused classes can also help to prevent the formation of a God class.
                    > #chatGPT
                    >
      - 2.2.1 识别系统操作
        - 两步式流程识别和定义系统操作
          - ![image.png](../assets/book/Microservices-Patterns-With-Examples-in-Java/image_1671018016495_0.png)
            - 这个流程的灵感来自CraigLannan的名著《ApplyingUML and Patterns》(Prentice Hall, 2004) 中介绍的[面向对象设计过程](http://www.craiglarman.com/wiki/index.php?title=Book_Applying_UML_and_Patterns)
          - 1.创建由关键类组成的**抽象领域模型**，这些关键类提供用于描述系统操作的词汇表
          - 2.确定系统操作，并根据领域模型描述每个系统操作的行为
        - 2.2.1.1 创建抽象领域模型
          id: 639996a4-5935-462f-9bf4-ce89250749fb
          - 通过与领域专家沟通后，分析用户故事和场景中频繁出现的名词
            - id: 6399b951-0ae3-4dbc-826e-4cd1210c9445
```shell
              # Place Order
              Given a consumer
                  And a restaurant
                  And a delivery address/time that can be served by that restaurant
                  And an order total that meets the restaurant''s order minimum
              When the consumer places an order for the restaurant
              Then consumer''s credit card is authorized
                  And an order is created in the PENDING ACCEPTANCE state
                  And the order is associated with the consumer
                  And the order is associated with the restaurant
              # Consumer, Order, Restaurant 和 CredtCard, 暗示了这些类都是需要的
```
            - id: 6399d7ae-6acc-4a32-bb44-be3cb996cfbf
```shell
              # Accept Order
              Given an order that is in the PENDING ACCEPTANCE state
                  and a courier that is available to deliver the order
              When a restaurant accepts an order with a promise to prepare by a particular
                  time
              Then the state of the order is changed to ACCEPTED
                  And the order''s promiseByTime is updated to the promised time
                  And the courier is assigned to deliver the order
```
            - ![image.png](../assets/book/Microservices-Patterns-With-Examples-in-Java/image_1671018988833_0.png)
        - 2.2.1.2 定义系统操作
          id: 639996a5-4b45-46b9-b60c-15648899453a
          - 有以下两种类型的系统操作
            - 命令型
              - 创建、更新或删除数据的系统操作
            - 查询型
              - 查询和读取数据的系统操作
          - 识别系统指令的切入点是分析用户故事和场景中的动词
            - 很多用户故事都会直接对应或映射为系统命令
            - 列出了一些关键的系统命令
              - ![image.png](../assets/book/Microservices-Patterns-With-Examples-in-Java/image_1671025463172_0.png)
                FTGO应用程序的重要系统命令
                - | :--------: | :--------------------: | :-----------------------: | :------------------------------------------------: |
                  |  Consumer  |      Create Order      |       createOrder()       |                    创建一个订单                    |
                  | Restaurant |      Accept Order      |       acceptOrder()       | 表示餐馆接受了订单,[:br]并承诺在规定的时间准备完毕 |
                  | Restaurant | Order Ready for Pickup | noteOrderReadyForPickup() |           表示订单已经准备完毕,可以送餐           |
                  |  Courier  |    Update Location    |   noteUpdatedLocation()   |                更新送餐员的当前位置                |
                  |  Courier  |   Delivery picked up   |  noteDeliveryPickedUp()  |                 表示送餐员已经取餐                 |
                  |  Courier  |   Delivery delivered   |  noteDeliveryDelivered()  |                 表示送餐员已经送餐                 |
          - 实现指令规范
            - 命令规范定义了命令对应的参数、返回值和领域模型类的行为。
            - 行为规范中包括前置条件（即当这个操作被调用时必须满足的条件）和后置条件（即这个操作被调用后必须满足的条件）
              - createOrder() 系统操作的规范
                - ![image.png](../assets/book/Microservices-Patterns-With-Examples-in-Java/image_1671025749343_0.png)
                  - 当系统操作被调用时，它会检查前置条件，执行操作来完成和满足后置条件
                  - 前置条件对应着Place Order 用户场景中的 givens
                    后置条件对应着场景中的Then
                    - ((6399b951-0ae3-4dbc-826e-4cd1210c9445))
              - acceptOrder () 的系统操作规范
                - ![image.png](../assets/book/Microservices-Patterns-With-Examples-in-Java/image_1671026200550_0.png)
                - ((6399d7ae-6acc-4a32-bb44-be3cb996cfbf))
          - 实现查询
            - 用户过程
```
                1.用户输人送餐地址和期望的送餐时间
                2.系统显示当前可用的餐馆
                3.用户选择餐馆；
                4.系统显示餐馆的菜单
                5.用户点餐并结账；
                6.系统创建订单。
```
```shell
                findAvailableRestaurants(deliveryAddress, deliveryTime)
                # 获取所有能够送餐到用户地址并满足送餐时间要求的餐馆。
                findRestaurantMenu(id)
                #返回餐馆信息和这家餐馆的菜单项。
```
                - 第1个包含了包含了地理位置等信息的复杂查询, 性能非常重要
                - ...
        - ((639996a4-5935-462f-9bf4-ce89250749fb)) & ((639996a5-4b45-46b9-b60c-15648899453a)) 回答了**应用"做什么"**
          - 有助于推动应用程序的架构设计
          - 每一个**系统操作的行为**都通过领域模型的方式来描述
          - 每一个重要的系统操作都对应着架构层面的一个重大**场景**，是架构中需要详细描述和特别考虑的地方
      - 2.2.2 根据业务能力进行服务拆分
        description: **创建微服务架构的策略之一**
        source: https://microservices.io/patterns/decomposition/decompose-by-business-capability.html
        - 业务能力
          - 一个来自于业务架构建模的术语
          - 指一些能够为公司（或组织）产生价值的商业活动
          - 特定业务的业务能力取决于这个业务的类型
            - 例如，保险公司业务能力通常包括承保、理赔管理、账务和合规等
            - 在线商店的业务能力包括：订单管理、库存管理和发货，等等
        - <`<Stop>`>
      - 2.2.3 根据子域进行服务拆分
      - 2.2.4 拆分的指导原则
      - 2.2.5 拆分单体应用为服务的难点
      - 2.2.6 定义服务API
  - 第3章 微服务架构中的进程间通信
    - 3.1 微服务架构中的进程间通信概述
      - 通信机制
        - 基于同步请求/响应的通信机制
          - 例如 HTTP REST 或gRPC
        - 异步的基于消息的通信机制
          - 比如 AMQP 或 STOMP
        - ....
      - 消息的格式
        - 具备可读性的格式
          - 比如基于文本的JSON 或 XML
        - 更加高效的、基于二进制的 Avro 或 Protocol Buffers 格式
        - ....
      - 3.1.1 交互方式
        - 有多种客户端与服务的交互方式, 它们可以分为2个维度
          -            1. **1 v 1** & **1 v n**
            - **1 v 1**: 每个客户端请求由一个服务实例来处理
            - **1 v n**: 每个客户端请求由多个服务实例来处理
              - 一对多的交互方式有以下几种类型
                - 发布 / 订阅方式 (publish/subscribe)
                  id: 639a859b-7b56-4a36-a5db-f8d4d8cead03
                  - 客户端发布通知消息，被零个或者多个感兴趣的服务订阅
                - 发布 / 异步响应方式 (publish/asynchronous)
                  id: 32f50700-a0b4-48b9-9cde-f847149926d4
                  - 客户端发布请求消息，然后等待从感兴趣的服务发回的响应
                - ((639a859b-7b56-4a36-a5db-f8d4d8cead03)) #vs ((32f50700-a0b4-48b9-9cde-f847149926d4))
                  -                    > in the publish/subscribe model, subscribers do not need to provide a callback address to the message broker. Instead, they simply subscribe to messages of a certain type and the message broker will notify them when a relevant message is received. In contrast, in the publish/asynchronous response model, subscribers must provide a callback address to the message broker, allowing the message broker to send messages directly to the subscriber's callback address when a relevant message is received. This allows subscribers to receive messages asynchronously, potentially improving the overall throughput of the system.
                    > #chatGPT
                    >
                    - Callback function
                      - > A callback function is a function that is passed as an argument to another function and is executed after some kind of event or action occurs. Callback functions are important because they allow for asynchronous programming, allowing a program to continue running without being blocked while waiting for some other action to complete. In this way, callback functions can help improve the performance and responsiveness of a program.
                        > While a callback function can often be replaced by a regular function, this may not always be the case. In some situations, the use of a callback function may be necessary in order to achieve the desired behavior or functionality. For example, if a program needs to perform some action after an event occurs, a callback function may be the only way to ensure that the action is executed at the right time. In general, the use of callback functions can help make a program more flexible and efficient.
                        >
          -            2. **同步** or **异步**
            ![image.png](../assets/book/Microservices-Patterns-With-Examples-in-Java/image_1671028103659_0.png)
            - 请求 / 响应
              - 一个客户端向服务端发起请求，等待响应
              - 客户端期望服务端很快就会发送响应
              - 在一个基于线程的应用中，等待过程可能造成线程阻塞
              - >[!warning]
                > 这样的方式会导致服务的紧耦合
            - 异步请求 / 响应
              - 客户端发送请求到服务端，服务端异步响应请求
              - 客户端在等待响应时不会阻塞线程，因为服务端的响应不会马上就返回
            - 单向通知
              - 客户端的请求发送到服务端，但是并不期望服务端做出任何响应
            - >[!note]
              > 交互方式并不会因为具体的进程间通信技术而发生改变
            - 一对多的交互方式有以下几种类型
      - 3.1.2 在微服务架构中定义API
      - 3.1.3 API的演化
        - 语义化版本控制
        - 进行次要并且向后兼容的改变
          - 向后兼容的更改
            - 对 API 的附加更改或功能增强
              - 添加可选属性
              - 向响应添加属性
              - 添加新操作
          - 正常运行的条件: 客户端和服务都遵守[健壮性原则](https://en.wikipedia.org/wiki/Robustness_principle)
            - 服务应该为缺少的请求属性提供默认值
            - 同样，客户端应忽略任何额外的响应属性
        - 进行主要并且不向后兼容的改变
          - HTTP REST
            -              1. 在 URL 中嵌入主要版本号
              - `/v1/...`
              - `/v2/...`
            -              2. HTTP 的内容协商机制, 并在 MIME 类型中包含版本号
              - 客户端将使用如下格式针对 1.x 版的服务 API 发起 Order 相关的请求
```
                  GET /orders/xyz HTTP/1.1
                  Accept:application/vnd.example.resource+json; version=1
```
              - 实现 API 的服务适配器将包含在旧版本和新版本之间进行转换的逻辑(API Gateway)
      - 3.1.4 消息的格式
        - 基于文本的消息格式
        - 二进制消息格式
          - 提供一个强类型定义的 IDL (接口描述文件), 用于定义消息的格式
            - [Protocol Buffers](https://developers.google.com/Protocol-buffers/docs/overview)
            - [Avro](https://avro.apache.org)
            - 区别
              - Protocol Buffers 使用 tagged fields (带标记的字段)，而 Avro 的消费者在解析消息之前需要知道它的格式
                - 因此，实行 API 的版本升级演进，Protocol Buffer 要优于 Avro
                - 有篇[博客文章](http://martin.kleppmann.com/2012/12/05/schema-evolution-in-avro-protocol-buffers-thrift.html)对 Thrift、 Protocol Bu ffers和 Avro 做了非常全面的比较
            -              >[!note]
              > 你不得不采用 API 优先的方法来进行服务设计
              - 编译器会自动根据这些格式生成序列化和反序列化的代码
    - 3.2 基于同步远程过程调用 (RPI) 模式的通信
      - [ ] #gtd/todo ![image.png](../assets/book/Microservices-Patterns-With-Examples-in-Java/image_1671096956858_0.png)  
        - 客户端中的业务逻辑调用**代理接口**
          - 接口由远程过程调用代理适配器类实现
        - 远程过程调用代理向服务发出请求
          - 该请求由远程过程调用服务器适配器类处理
        - 该类通过接口调用服务的业务逻辑。
          - 然后它将回复发送回远程过程调用代理，该代理将结果返回给客户端的业务逻辑
        - 客户端使用同步的远程过程调用协议（如 REST ) 来调用服务 [参阅](https://microservices.io/patterns/communication-style/messaging.html)
          RPI === Command Pattern ((63959dcc-1bd8-4fc7-b337-6123a2911057)) thx #chatGPT
          - Pattern: Messaging
```java
              public class OrderService {
                //...
                  public Order createOrder(long consumerId, long restaurantId,
                                           List<MenuItemIdAndQuantity> lineItems) {
                  Restaurant restaurant = restaurantRepository.findById(restaurantId)
                    .orElseThrow(() -> new RestaurantNotFoundException(restaurantId));
                  List<OrderLineItem> orderLineItems = makeOrderLineItems(lineItems, restaurant);
                  ResultWithDomainEvents<Order, OrderDomainEvent> orderAndEvents =
                    Order.createOrder(consumerId, restaurant, orderLineItems);
                  Order order = orderAndEvents.result;
                  orderRepository.save(order);
                  orderAggregateEventPublisher.publish(order, orderAndEvents.events);
                  OrderDetails orderDetails = new OrderDetails(consumerId, restaurantId, orderLineItems, order.getOrderTotal());
                  CreateOrderSagaState data = new CreateOrderSagaState(order.getId(), orderDetails);
                  createOrderSagaManager.create(data, Order.class, order.getId());
                  meterRegistry.ifPresent(mr -> mr.counter("placed_orders").increment());
                  return order;
                }
```
          - Pattern: Remote Procedure Invocation (RPI)
```Scala
              @Component
              class RegistrationServiceProxy @Autowired()(restTemplate: RestTemplate) extends RegistrationService {
                @Value("${user_registration_url}")
                var userRegistrationUrl: String = _
                @HystrixCommand(commandProperties=Array(new HystrixProperty(name="execution.isolation.thread.timeoutInMilliseconds", value="800")))
                override def registerUser(emailAddress: String, password: String): Either[RegistrationError, String] = {
                  try {
                    val response = restTemplate.postForEntity(userRegistrationUrl,
                      RegistrationBackendRequest(emailAddress, password),
                      classOf[RegistrationBackendResponse])
                    response.getStatusCode match {
                      case HttpStatus.OK =>
                        Right(response.getBody.id)
                    }
                  } catch {
                    case e: HttpClientErrorException if e.getStatusCode == HttpStatus.CONFLICT =>
                      Left(DuplicateRegistrationError)
                  }
                }
              }
```
      - 3.2.1 使用REST
        -          > REST 提供了一系列架构约束，当作为整体使用时，它强调组件交互的可扩展性、接口的通用性、组件的独立部署，以及那些能减少交互延迟的中间件，它强化了安全性，也能封装遗留系统。
          > —— http://www.ics.uci.edu/~fielding/pubs/dissertation/top.htm
          >
          - **资源**
            - 它通常表示单个业务对象，例如客户或产品，或业务对象的集合。 REST 使用 HTTP 动词来操作资源，使用 URL 引用这些资源。
            - 例如
              - GET 请求返回资源的表示形式，该资源通常采用XML 文档或JSON 对象的形式，但也可以使用其他格式（如二进制）
              - POST 请求创建新资源， PUT 请求更新资源。例如， Order Service 具有用千创建 Order 的 POST/ order 端点以及用于检索 Order 的 `GET/orders/{orderId}` 端点。
          - 很多开发者都表示他们基于 HTTP 的 API 是 RESTful 风格的。但是，如同 RoyFielding 在他的[博客](http://rog.gbiv.com/untangled/2008/rest-apis-must-be-hypertext-driven) 中所说，并非所有这些 API 都是 RESTful 风格的。为了更好地理解这个概念，我们来看一看 REST 成熟度模型
        - REST 成熟度模型
          - Leonard Richardson 为 REST 定义了一个[成熟度模型](https://martinfowler.com/articles/richardsonMaturityModel.html)
          - Level
            - ■ Level 0
              - 服务的客户端只是向服务端点发起 HTTP POST 请求，进行服务调用
              - 每个请求都指明了需要执行的操作、这个操作针对的目标（例如，业务对象）和必要的参数
            - ■ Level 1
              - 引入了**资源**的概念
              - 要执行对资源的操作，客户端需要发出指定要执行的操作和包含任何参数的 POST 请求
            - ■ Level 2
              - 使用 HTTP 动词来执行操作
                - 譬如 GET表示获取、POST 表示创建、 PUT 表示更新
              - 请求查询参数和主体（如果有的话）指定操作的参数。
                - 这让服务能够借助 Web 基础设施服务
                  - 例如通过CDN 来缓存 GET 请求
            - ■ Level 3
              - 基于 **HATEOAS( Hypertext As The Engine Of Application State)** 原则设计
                wikipedia: https://zh.wikipedia.org/wiki/HATEOAS
                - 基本思想是在由 GET 请求返回的资源信息中包含链接，这些链接能够执行该资源允许的操作
                  - 例如，客户端通过订单资源中包含的链接取消某一订单，或者发送 GET 请求去获取该订单，等等
                - server provides links to resources in its responses, allowing the client to discover and navigate the API without prior knowledge of the API's structure.
                  #chatGPT
```java
                    // The Book class represents a resource in the API
                    public class Book {
                      private String title;
                      private String author;
                      // Getters and setters for the title and author properties
                      // This method adds a link to the book resource
                      public void addLink(String rel, String href) {
                        // Code to add a link to the book resource
                      }
                    }
                    // The BookResource class provides an API for interacting with book resources
                    public class BookResource {
                      // This method returns a list of books
                      public List<Book> getBooks() {
                        List<Book> books = new ArrayList<>();
                        // Code to retrieve the books from a database
                        // Add a link to each book resource
                        for (Book book : books) {
                          book.addLink("self", "/books/" + book.getId());
                        }
                        return books;
                      }
                    }
```
                    - In this example, the  `BookResource`  class provides a  `getBooks`  method that returns a list of  `Book`  objects. Each  `Book`  object includes a link to its own resource, allowing the client to easily access the book's details by following the link. This allows the client to interact with the API without knowing the URLs of the individual book resources in advance.
                - HATEOAS 的优点
                  source: https://www.infoq.com/news/2009/04/hateoas-restful-api-advantages/
                  - 无须在客户端代码中写入硬链接的 URL
                  - 由于资源信息中包含可允许操作的链接，客户端无须猜测在资源的当前状态下执行何种操作
        - 定义 REST API
          - 使用接口定义语言 ( IDL ) 定义 API
            - 最流行的 REST IDL 是 [Open API 规范](http://www.openapis.org)
              - 它是从 Swagger 开源项目发展而来的
                - Swagger 项目是一组用于开发和记录 REST API 的工具
                  - 它包括从接口定义到生成客户端桩 ( stub , 存根）和服务器骨架的一整套工具
        - 在—个请求中获取多个资源的挑战
          - API 允许客户端在获取资源时检索相关资源。例如，客户可以使用 `GET/orders/order-id-1345?expand=consurner` 检索 Order 及其 Consumer
            - 请求中的查询参数用来指定要与 Order 一起返回的相关资源
            - 许多场景中都很有效, 但是
              - 实现它也可能很耗时
              - 对于更复杂的场景来说，它通常是不够的
          - 替代技术, 旨在支持高效的数据获取
            - [GraphQL](http://graphql.org) 和 [Neflix Falcor](http://netflix.github.io/falcor)
        - 把操作映射为 HTTP 动词的挑战
          - 每一种业务都有多种方法作为实现
          - 更新可能不是幕等的
            - 这却是使用 PUT 的要求
          - Solution 1
            - 定义用于更新资源的特定方面的子资源
              - OrderService 具有用于取消订单的 `POST/orders/{orderId}/cancel` 端点，以及用于修订订单的 `POST/orders/{orderId}/revise` 端点
          - Solution 2
            - 将动词指定为 URL 的查询参数
          - 可惜的是，这两种解决方案都不是特别符合 RESTful 的要求。
          - 映射操作到 HTTP 动词的这个问题导致了 REST 替代方案的日益普及, 见 ((639b0d75-e399-48dd-a4e6-0e2dc1f10b29))
        - REST 的好处和弊端
          - 好处
            - 1.简单 / 熟悉
            - 2.API 好测试
              - Postman (浏览器插件)
              - curl 之类的命令行
            - 3.直接支持请求 / 响应方式的通信
            - 4.HTTP 对防火墙友好
            - 5.不需要中间代理，简化系统架构
          - 弊端
            - 1.通信只支持 **请求/响应方式**
            - 2.可能导致可用性降低
              - 由于客户端和服务直接通信而没有代理来缓冲消息
                - 它们必须在 REST API 调用期间都保持在线
            - 3.客户端必须知道服务实例的位置 (URL)
              - 如 3.2.4 节所述，客户端必须使用所谓的服务发现机制来定位服务实例，这是现代应用程序中的一个重要问题。
            - 4.单个请求中获取多个资源具有挑战性
            - 5.有时很难将多个更新操作映射到 HTTP 动词
      - 3.2.2 使用[gRPC(Remote Procedure Call)](http://www.grpc.io)
        id: 639b0d75-e399-48dd-a4e6-0e2dc1f10b29
        description: 用于编写跨语言客户端和服务端的[框架](https://en.wikipedia.org/wiki/Remote_procedure_call)
        - 引用原因
          - REST **痛点**: 设计**支持多个更新操作**的 REST API
        - RPC是一种基于二进制消息的协议, 不得不采用 **API 优先**的方法来进行服务设计
          #google
          - > API-first design is a software design approach in which an application programming interface (API) is designed and developed first, before the actual implementation of the application. This approach is often used in the development of web-based applications, particularly those that will be consumed by other developers or businesses through an API.
            > An example of API-first design might be the development of a customer relationship management (CRM) system that is intended to be used by other businesses through an API. The developers of the CRM system would first design and document the API, outlining the various endpoints, input parameters, and output formats that would be available to consumers of the API. They would then implement the actual CRM system, ensuring that it is designed in a way that aligns with the API they have already designed. This approach allows the developers to focus on the functionality of the CRM system, while also ensuring that it can be easily consumed and integrated with other systems through the API.
            > #chatGPT
            >
        - gRPC API
          - 可以使用基于 Protocol Buffer 的 IDL 定义 gRPC API
            - 使用 Protocol Buffer 编译器生成客户端的桩 (stub/存根) 和服务端骨架 (skeleton)
              - 编译器可以为各种语言生成代码，包括Java、 c\# 、 Node.js和 GoLang
              - 客户端和服务端使用 HTTP/2 以 Protocol Buffer 格式交换二进制消息
          - gRPC API 由 一个或多个服务 和 请求/响应消息 定义组成
            - 服务定义类似于Java接口，是**强类型方法的集合**
              - 除了支持简单的请求/响应RPC之外， gRPC还支持流式 RPC
              - 服务器可以使用消息流回复客户端。客户端也可以向服务器发送消息流
          - gRPC 使用 Protocol Buffers 作为消息格式
            - Protocol Buffers是一种高效且紧凑的二进制格式
              - 它是一种标记格式
              - Protocol Buffers 消息的每个字段都有编号，并且有一个类型代码
                - 消息接收方可以提取所需的字段，并跳过它无法识别的字段
                - 因此，gRPC **使 API 能够在保持向后兼容的同时进行变更**
        - 好处
          - 设计**复杂更新**操作的 API 非常**简单**
          - **高效、紧凑的进程间通信机制**，尤其是在交换大量消息时
          - 支持在远程过程调用和消息传递过程中使用**双向流式消息**方式
          - 它实现了客户端和用各种语言编写的**服务端之间的互操作性**
        - 弊端
          - 与基于 REST/JSON 的 API机制相比，JavaScript 客户端使用基于 gRPC的 API 需要做更多的工作。
          - 旧式防火墙可能不支持 HTTP/2
```java
          // Define the service in a .proto file
          syntax = "proto3";
          service Greeter {
            rpc SayHello (HelloRequest) returns (HelloResponse);
          }
          message HelloRequest {
            string name = 1;
          }
          message HelloResponse {
            string message = 1;
          }
          // Generate the stubs using the Protocol Buffers compiler
          $ protoc -I . greeter.proto --java_out=. --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_cpp_plugin`
          // Implement the service
          import com.example.grpc.GreeterGrpc;
          import com.example.grpc.HelloRequest;
          import com.example.grpc.HelloResponse;
          import io.grpc.ManagedChannel;
          import io.grpc.ManagedChannelBuilder;
          import io.grpc.StatusRuntimeException;
          public class HelloWorldClient {
            public static void main(String[] args) {
              ManagedChannel channel = ManagedChannelBuilder.forAddress("localhost", 50051)
                  .usePlaintext()
                  .build();
              GreeterGrpc.GreeterBlockingStub stub = GreeterGrpc.newBlockingStub(channel);
              HelloRequest request = HelloRequest.newBuilder().setName("World").build();
              try {
                HelloResponse response = stub.sayHello(request);
                System.out.println(response.getMessage());
              } catch (StatusRuntimeException e) {
                System.out.println("RPC failed: " + e.getStatus());
              }
            }
          }
```
          This example shows a simple gRPC client that sends a request to a server to say hello. The server's response is then printed to the console. This example demonstrates how to mark:  a gRPC service, generate the necessary stubs and interfaces using the Protocol Buffers compiler, and implement a client that can communicate with the server using the gRPC API.
          #chatGPT
          --------
      - 3.2.3 使用断路器模式处理局部故障
        - 断路器模式
          description: "这是一个远程过程调用的代理，在连续失败次数超过指定阁值后的一段时间内，这个代理会立即拒绝其他调用"
          source: https://microservices.io/patterns/reliability/circuit-breaker.html
        - ![image.png](../assets/book/Microservices-Patterns-With-Examples-in-Java/image_1671261044236_0.png)
          description: 如果Order Service 出问题: OrderServiceProxy 将无限期地阻塞. 等待响应. 最后整个 API 网关就会崩掉.
          - 让远程过程调用代理 (如 OrderServiceProxy) 有正确处理无响应服务的能力
          - 需要决定如何从失败的远程服务中恢复
        - 开发可靠的远程过程调用代理
          - Netflix 描述的 [Fault Tolerance in a High Volume, Distributed System | by Netflix Technology Blog | Netflix TechBlog](https://netflixtechblog.com/fault-tolerance-in-a-high-volume-distributed-system-91ab4faae74a) 来保护自己, 包括
            - 网络超时
              - 等待针对请求的响应时，一定不要做成无限阻塞，而是要设定一个超时
                - 使用超时可以保证不会一直在无响应的请求上浪费资源
            - 限制客户端向服务器发出请求的数址
              - 把客户端能够向特定服务发起的请求设置一个上限
                - 如果请求达到了这样的上限，很有可能发起更多的请求也无济于事
                  - 这时就应该让请求立刻失败
            - 断路器模式
              - 监控客户端发出请求的成功和失败数量，如果失败的比例超过一定的阔值，就启动断路器，让后续的调用立刻失效
                - 如果大量的请求都以失败而告终，这说明被调服务不可用，这样即使发起更多的调用也是无济于事
                - 在经过一定的时间后，客户端应该继续尝试，如果调用成功，则解除断路器
          - [Netflix Hystrix](https://github.com/Netflix/Hystrix) in `Java`; [Polly库](https://github.com/Appv-Next/Polly) in `.NET`
        - 从服务失效故障中恢复
          - ![image.png](../assets/book/Microservices-Patterns-With-Examples-in-Java/image_1671261954020_0.png)
      - 3.2.4 使用服务发现
        - 必要性 -> 服务实例集会动态更改(故障和升级)
        - 什么是服务发现
          - 服务发现的关键组件是**服务注册表**
            - 服务注册表是包含服务实例网络位置信息的一个数据库
          - 服务实例启动和停止时，服务发现机制会更新服务注册表
            - 当客户端调用服务时，服务发现机制会查询服务注册表以获取可用服务实例的列表，并将请求路由到其中一个服务实例
          - 有 2 种主要实现方式
            - 服务及其客户直接与服务注册表交互。
            - 通过部署基础设施来处理服务发现 （12 章中详细讨论）
        - 应用层服务发现模式
          - ![image.png](../assets/book/Microservices-Patterns-With-Examples-in-Java/image_1671262994174_0.png)
          - 两种模式的组合
            - 自注册模式：服务实例向服务注册表注册自己
              source: https://microservices.io/patterns/self-registration.html
            - 客户端发现模式：客户端从服务注册表检索可用服务实例的列表，并在它们之间进行负载平衡
              source: https://microservices.io/patterns/client-side-discovery.html
          - 好处
            - 可以处理多平台部署的问题 （服务发现机制与具体的部署平台无关）
          - 弊端
            - 需要为你使用的每种编程语言（可能还有框架） 提供服务发现库
            - 开发者负责设置和管理服务注册表， 这 会分散一定的精力
        - 平台层服务发现模式
          - ![image.png](../assets/book/Microservices-Patterns-With-Examples-in-Java/image_1671262893616_0.png)
          - 两种模式的组合
            - 第三方注册模式: 服务实例由第三方自动注册到服务注册表
              source: https://microservices.io/patterns/3rd-party-registration.html
            - 服务端发现模式：客户端向路由器发出请求，路由器负责服务发现
              source: https://microservices.io/patterns/server-side-discovery.html
          - 好处
            - 服务发现的所有方面都完全由部署平台处理
          - 弊端
            - 仅限于支持使用该平台部署的服务
    - 3.3 基于异步消息模式的通信
      - 3.3.1 什么是消息传递
        - 关于消息
        - 关于消息通道
      - 3.3.2 使用消息机制实现交互方式
        - 实现请求 I 响应和异步请求/响应
        - 实现单向通知
        - 实现发布/订阅
        - 实现发布/异步响应
      - 3.3.3 为基于消息机制的服务API创建API规范
        - 记录异步操作
        - 记录事件发布
          id: 639d7be0-98ed-4f08-bb30-04660f771bb4
      - 3.3.4 使用消息代理
        - 无代理消息
        - 基于代理的消息
          - 好处
          - 弊端
      - 3.3.5 处理并发和消息顺序
      - 3.3.6 处理重复消息
        - 编写幕等消息处理器
        - 踉踪消息并丢弃重复消息
          id: 639d7c40-484d-4c81-8c1a-1aa68d7f17ea
      - 3.3.7 事务性消息
        - 使用数据库表作为消息队列
        - 通过轮询模式发布事件
        - 使用事务日志拖尾模式发布事件
      - 3.3.8 消息相关的类库和框架
    - 3.4 使用异步消息提高可用性
      - 3.4.1 同步消息会降低可用性
      - 3.4.2 消除同步交互
        - 使用异步交互模式
          id: 639d7cbc-4a72-4c32-a5fc-10415331456e
        - 复制数据
        - 先返回响应，再完成处理
  - 第4章 使用Saga管理事务
    - 4.1 微服务架构下的事务管理
      - 4.1.1 微服务架构对分布式事务的需求
      - 4.1.2 分布式事务的挑战
      - 4.1.3 使用Saga模式维护数据一致性
    - 4.2 Saga的协调模式
      - 4.2.1 协同式Saga
      - 4.2.2 编排式Saga
    - 4.3 解决隔离问题
      - 4.3.1 缺乏隔离导致的问题
      - 4.3.2 Saga模式下实现隔离的对策
    - 4.4 Order Service和Create Order Saga的设计
      - 4.4.1 OrderService类
      - 4.4.2 Create Order Saga的实现
      - 4.4.3 OrderCommandHandlers类
      - 4.4.4 OrderServiceConfiguration类
  - 第5章 微服务架构中的业务逻辑设计
    - 5.1 业务逻辑组织模式
      - 5.1.1 使用事务脚本模式设计业务逻辑
      - 5.1.2 使用领域模型模式设计业务逻辑
      - 5.1.3 关于领域驱动设计
    - 5.2 使用聚合模式设计领域模型
      - 5.2.1 模糊边界所带来的问题
      - 5.2.2 聚合拥有明确的边界
      - 5.2.3 聚合的规则
      - 5.2.4 聚合的颗粒度
      - 5.2.5 使用聚合设计业务逻辑
    - 5.3 发布领域事件
      - 5.3.1 为什么需要发布变更事件
      - 5.3.2 什么是领域事件
      - 5.3.3 事件增强
      - 5.3.4 识别领域事件
      - 5.3.5 生成和发布领域事件
      - 5.3.6 消费领域事件
    - 5.4 Kitchen Service的业务逻辑
    - 5.5 Order Service的业务逻辑
      - 5.5.1 Order聚合
      - 5.5.2  OrderService类
  - 第6章 使用事件溯源开发业务逻辑
    - 6.1 使用事件溯源开发业务逻辑概述
      - 6.1.1 传统持久化技术的问题
      - 6.1.2 什么是事件溯源
      - 6.1.3 使用乐观锁处理并发更新
      - 6.1.4 事件溯源和发布事件
      - 6.1.5 使用快照提升性能
      - 6.1.6 幂等方式的消息处理
      - 6.1.7 领域事件的演化
      - 6.1.8 事件溯源的好处
      - 6.1.9 事件溯源的弊端
    - 6.2 实现事件存储库
      - 6.2.1 Eventuate Local事件存储库的工作原理
      - 6.2.2 Eventuate的Java客户端框架
    - 6.3 同时使用Saga和事件溯源
      - 6.3.1 使用事件溯源实现协同式Saga
      - 6.3.2 创建编排式Saga
      - 6.3.3 实现基于事件溯源的Saga参与方
      - 6.3.4 实现基于事件溯源的Saga编排器
  - 第7章 在微服务架构中实现查询
    - 7.1 使用API组合模式进行查询
      - 7.1.1 findOrder()查询操作
      - 7.1.2 什么是API组合模式
      - 7.1.3 使用API组合模式实现findOrder()查询操作
      - 7.1.4 API组合模式的设计缺陷
      - 7.1.5 API组合模式的好处和弊端
    - 7.2 使用CQRS模式
      - 7.2.1 为什么要使用CQRS
      - 7.2.2 什么是CQRS
      - 7.2.3 CQRS的好处
      - 7.2.4 CQRS的弊端
    - 7.3 设计CQRS视图
      - 7.3.1 选择视图存储库
      - 7.3.2 设计数据访问模块
      - 7.3.3 添加和更新CQRS视图
    - 7.4 实现基于AWS DynamoDB的CQRS视图
      - 7.4.1 OrderHistoryEventHandlers模块
      - 7.4.2 DynamoDB中的数据建模和查询设计
      - 7.4.3 OrderHistoryDaoDynamoDb类
  - 第8章 外部API模式
    - 8.1 外部API的设计难题
      - 8.1.1 FTGO移动客户端API的设计难题
      - 8.1.2 其他类型客户端API的设计难题
    - 8.2 API Gateway模式
      - 8.2.1 什么是API Gateway模式
      - 8.2.2 API Gateway模式的好处和弊端
      - 8.2.3 以Netflix为例的API Gateway
      - 8.2.4 API Gateway的设计难题
    - 8.3 实现一个API Gateway
      - 8.3.1 使用现成的API Gateway产品或服务
      - 8.3.2 开发自己的API Gateway
      - 8.3.3 使用GraphQL实现API Gateway
  - **第9章** 微服务架构中的测试策略（上）
    - 9.1 微服务架构中的测试策略概述
      - 9.1.1 什么是测试
      - 9.1.2 微服务架构中的测试挑战
      - 9.1.3 部署流水线
    - 9.2 为服务编写单元测试
      - 9.2.1 为实体编写单元测试
      - 9.2.2 为值对象编写单元测试
      - 9.2.3 为Saga编写单元测试
      - 9.2.4 为领域服务编写单元测试
      - 9.2.5 为控制器编写单元测试
      - 9.2.6 为事件和消息处理程序编写单元测试
  - **第10章** 微服务架构中的测试策略（下）
    - 10.1 编写集成测试
      - 10.1.1 针对持久化层的集成测试
      - 10.1.2 针对基于REST的请求/响应式交互的集成测试
      - 10.1.3 针对发布/订阅式交互的集成测试
      - 10.1.4 针对异步请求/响应式交互的集成契约测试
    - 10.2 编写组件测试
      - 10.2.1 定义验收测试
      - 10.2.2 使用Gherkin编写验收测试
      - 10.2.3 设计组件测试
      - 10.2.4 为FTGO的Order Service编写组件测试
    - 10.3 端到端测试
      - 10.3.1 设计端到端测试
      - 10.3.2 编写端到端测试
      - 10.3.3 运行端到端测试
  - 第11章 开发面向生产环境的微服务应用
    - 11.1 开发安全的服务
      - 11.1.1 传统单体应用程序的安全性
      - 11.1.2 在微服务架构中实现安全性
    - 11.2 设计可配置的服务
      - 11.2.1 使用基于推送的外部化配置
      - 11.2.2 使用基于拉取的外部化配置
    - 11.3 设计可观测的服务
      - 11.3.1 使用健康检查API模式
      - 11.3.2 使用日志聚合模式
      - 11.3.3 使用分布式追踪模式
      - 11.3.4 使用应用程序指标模式
      - 11.3.5 使用异常追踪模式
      - 11.3.6 使用审计日志模式
    - 11.4 使用微服务基底模式开发服务
      - 11.4.1 使用微服务基底
      - 11.4.2 从微服务基底到服务网格
  - 第12章 部署微服务应用
    - 12.1 部署模式：编程语言特定的发布包格式
      - 12.1.1 使用编程语言特定的发布包格式进行部署的好处
      - 12.1.2 使用编程语言特定的发布包格式进行部署的弊端
    - 12.2 部署模式：将服务部署为虚拟机
      - 12.2.1 将服务部署为虚拟机的好处
      - 12.2.2 将服务部署为虚拟机的弊端
    - 12.3 部署模式：将服务部署为容器
      - 12.3.1 使用Docker部署服务
      - 12.3.2 将服务部署为容器的好处
      - 12.3.3 将服务部署为容器的弊端
    - 12.4 使用Kubernetes部署FTGO应用程序
      - 12.4.1 什么是Kubernetes
      - 12.4.2 在Kubernetes上部署Restaurant Service
      - 12.4.3 部署API Gateway
      - 12.4.4 零停机部署
      - 12.4.5 使用服务网格分隔部署与发布流程
    - 12.5 部署模式：Serverless部署
      - 12.5.1 使用AWS Lambda进行Serverless部署
      - 12.5.2 开发Lambda函数
      - 12.5.3 调用Lambda函数
      - 12.5.4 使用Lambda函数的好处
      - 12.5.5 使用Lambda函数的弊端
    - 12.6 使用AWS Lambda和AWS Gateway部署RESTful服务
      - 12.6.1 AWS Lambda版本的Restaurant Service
      - 12.6.2 把服务打包为ZIP文件
      - 12.6.3 使用Serverless框架部署Lambda函数
  - 第13章 微服务架构的重构策略
    - 13.1 重构到微服务需要考虑的问题
      - 13.1.1 为什么要重构单体应用
      - 13.1.2 绞杀单体应用
    - 13.2 将单体应用重构为微服务架构的若干策略
      - 13.2.1 将新功能实现为服务
      - 13.2.2 隔离表现层与后端
      - 13.2.3 提取业务能力到服务中
    - 13.3 设计服务与单体的协作方式
      - 13.3.1 设计集成胶水
      - 13.3.2 在服务和单体之间维持数据一致性
      - 13.3.3 处理身份验证和访问授权
    - 13.4 将新功能实现为服务：处理错误配送订单
      - 13.4.1 Delayed Delivery Service的设计
      - 13.4.2 为Delayed Delivery Service设计集成胶水
    - 13.5 从单体中提取送餐管理功能
      - 13.5.1 现有的送餐管理功能
      - 13.5.2 Delivery Service概览
      - 13.5.3 设计Delivery Service的领域模型
      - 13.5.4 Delivery Service集成胶水的设计
      - 13.5.5 修改FTGO单体使其能够与Delivery Service交互