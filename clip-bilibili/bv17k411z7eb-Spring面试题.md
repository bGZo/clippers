---
created: 2024-12-13T08:52:57
modified: 2025-01-19T02:57:07
---
author:: 马士兵

created: 2023-03-04

source:: https://www.bilibili.com/video/BV17K411Z7EB

type:: archives-web

- 原视频已经消失，此页终结
- [bjmashibing/InternetArchitect: 年薪百万互联网架构师课程文档及源码(公开部分)](https://github.com/bjmashibing/InternetArchitect)

## 心态调整
  - P1 互联网寒冬心态如何调整？
  - P2 如何找工作
  - P3 面试通不过怎么办？
  - P4 面进却待不住怎么办？
  - P5 如何找高薪工作
  - P6 简历编写的 4 不要原则
  - P7 简历编写的 4 要原则
  - P8 简历文件格式的选择
  - P9 个人情况模块的描述
  - P10 技术实力模块描述的原则
  - P11 技术描述模块的错误案例

## Spring 面试题
### P12 谈谈 Spring IOC 理解，原理与实现
    - 总：当前问题回答的是那些具体的点
      分：以1，2，3，4，5的方式分细节取描述相关的知识点，如果有哪些点不清楚，直接忽略过去
      - 突出一些技术名词（核心概念，接口，类，关键方法）
    - 避重就轻：没有重点
    - **1．谈谈Spring IOC的理解，原理与实现？**
      - (总)
        - 控制反转：理论思想，原来的对象是由使用者来进行控制，有了spring之后，可以把整个对象交给spring来帮我们进行管理
          - DI：依赖注入，把对应的属性的值注入到具体的对象中，＠Autowired，populateBean完成属性值的注入
        - 容器：存储对象，使用map结构来存储，在spring中一般存在三级缓存，singletonObjects 存放完整的bean对象.
          - 整个bean的生命周期，从创建到使用到销毁的过程全部都是由容器来管理（bean的生命周期）
      - (分)
        - 1、一般聊ioc容器的时候要涉及到容器的创建过程（beanFactory，DefaultListableBeanFactory），向bean工厂中设置一些参数
          （BeanPostProcessor，Aware接口的子类）等等属性
        - 2、加载解析bean对象，准备要创建的bean对象的定义对象beanDefinition，（xml或者注解的解析过程）
        - 3、beanFactoryPostProcessor的处理，此处是扩展点，PlaceHolderConfigurSupport，ConfigurationClassPostProcessor
        - 4、BeanPostProcessor的注册功能，方便后续对bean对象完成具体的扩展功能
        - 5、通过反射的方式讲BeanDefinition对象实例化成具体的bean对象，
        - 6、bean对象的初始化过程（填充属性，调用aware子类的方法，调用BeanPostProcessor前置处理方法，调用init-mehtod方法，调用
          BeanPostProcessor的后置处理方法）
        - 7、生成完整的bean对象，通过getBean方法可以直接获取
        - 8、销毁过程
    - **2．谈一下spring IOC的底层实现**
    - **3．描述一下bean的生命周期？**
    - **4．Spring是如何解决循环依赖的问题的？**
    - **5．Bean Factory与FactoryBean有什么区别？**
    - **6．Spring中用到的设计模式？**
    - **7．Spring的AOP的底层实现原理？**
    - **8．Spring的事务是如何回滚的？**
    - **9．谈一下spring事务传播？**

### P13 谈谈 Spring IOC 的底层实现
### [ ] #wait P14 描述一下 bean 的生命周期
    - ![2593013-20211208134354570-1643503307.png](../assets/2593013-20211208134354570-1643503307_1709646582222_0.png)
      #+BEGIN_CENTER
      [大厂高频面试题Spring Bean生命周期最详解 - Tom弹架构 - 博客园](https://www.cnblogs.com/gupaoedu-tom/p/15661075.html#1-spring%E7%94%9F%E5%91%BD%E5%91%A8%E6%9C%9F%E6%B5%81%E7%A8%8B%E5%9B%BE)
      #+END_CENTER
    - 注意学会拓展
      - 实例化bean
        logseq.order-list-type:: number
        - 反射的方式生成对象
          logseq.order-list-type:: number
      - 填充bean的属性
        logseq.order-list-type:: number
        - `populateBean()`
          logseq.order-list-type:: number
        - 循环依赖的问题 (三级缓存)
          logseq.order-list-type:: number
      - 调用aware接口相关的方法
        logseq.order-list-type:: number
        - `invokeAwareMethod`(完成BeanName,BeanFactory,BeanClassLoader对象的属性设置)
          logseq.order-list-type:: number
      - 调用 `BeanPostProcessor` 中的前置处理方法
        logseq.order-list-type:: number
        - 使用比较多的有(ApplicationContextPostProcessor,设置
          logseq.order-list-type:: number
          ApplicationContext,Environment,ResourceLoader,EmbeddValueResolverx)
      - 调用initmethod方法
        logseq.order-list-type:: number
        - invokelnitmethod(),判断是否实现了initializingBean接口
          logseq.order-list-type:: number
          - 如果有,调用afterPropertiesSet方法
            logseq.order-list-type:: number
          - 没有就不调用
            logseq.order-list-type:: number
      - 调用BeanPostProcessor的后置处理方法
        logseq.order-list-type:: number
        - spring的aop就是在此处实现的,AbstractAutoProxyCreator
        - 注册Destuction相关的回调接口:钩子函数
      - ==获取到完整的对象，可以通过 `getBean` 的方式来进行对象的获取==
        logseq.order-list-type:: number
      - 销毁流程
        logseq.order-list-type:: number
        - 判断是否实现了DispoableBean接口
          logseq.order-list-type:: number
        - 调用destroyMethod方法
          logseq.order-list-type:: number

### P15 Spring 是如何解决循环依赖的问题的
    - 什么是循环依赖？

```java
        public class A{
          @Autowired
          private B xxx;
        }
        public class B{
          @Autowired
          private A xxx;
        }
```

    - 重点
      - 三级缓存
        logseq.order-list-type:: number
      - 提前暴露对象
        logseq.order-list-type:: number
      - AOP
        logseq.order-list-type:: number
      - [[draws/2024-03-06-19-10-34.excalidraw]]
        logseq.order-list-type:: number
        - 这里的半成品，指的是完成了实例化，但是还没初始化完毕的对象；
          logseq.order-list-type:: number
    - 创建 A 对象 -> 实例化 A(`b=null`)
    - 从容器中查找B -> 找不到
    - logseq.order-list-type:: number

### P16 缓存的放置时间和删除时间
    - 三级缓存
      id:: 65e9dc09-1c4c-48a8-a2ff-f07e94caf388
      - `addSingletonFactory`
    - 二级缓存
      - 第一次从 ((65e9dc09-1c4c-48a8-a2ff-f07e94caf388)) 中确定对象是代理对象还是普通对象，同事删除三级缓存；
      - `getSingleton`
    - 一级缓存
      - 生成完整对象之后，删除二三级缓存；
      - `addSingleton`

### P17 Bean Factory 与 FactoryBean 有什么区别
    - 同
      - 创建 Bean 对象
    - 异
      - Bean Factory
        id:: 65ef0863-22f2-42ab-90e2-bc2b0def3c0c
        - 必须遵循严格的生命周期流程；
      - FactoryBean
        - 比 ((65ef0863-22f2-42ab-90e2-bc2b0def3c0c)) 更加简单；
        - 可以自定义对象创建，并且可以交给 Spring 容器管理；
        - 相关函数
          - `isSingleton`
            - 是否单例对象
          - `getObjectType`
            - 获得返回对象类型
          - `getObject`
            - 自定义创建对象的过程 （new、反射、动态代理）

### P18 Spring 中用到的设计模式
### P19 Spring 的 AOP 的底层实现原理
    - IOC => AOP 只是过程中的一个拓展
      - `BeanPostProcessor`
    - AOP 是 AOC 的扩展功能，现有的 IOC
  - 动态代理
  - P20 Spring 的事务是如何回滚的？
  - P21 谈一下 spring 事务传播？
- P22 【性能优化面试题】虚拟机栈
- P23 【性能优化面试题】pc 计数器
- P24 【性能优化面试题】本地方法栈
- P25 【性能优化面试题】方法区和堆
- P26 【性能优化面试题】java 执行引擎
- P27 【性能优化面试题】类加载器
- P28 【性能优化面试题】老年代和新生代的问题
- P29 【性能优化面试题】如何解决线上 Gc 频繁的问题
- P30 【性能优化面试题】简述内存溢出的原因，如何排查线上问题
- P31 【性能优化面试题】jvm 有哪些垃圾回收器，实际中如何选择
- P32 【性能优化面试题】介绍一下垃圾回收算法
- P33 【性能优化面试题】happens-before 规则
- P34 【性能优化面试题】阻塞队列的有界和无界
- P35 【性能优化面试题】jvm 监控系统是通过 Jmx 做的么
- P36 【ES 面试题】Elasticsearch 前言
- P37 【ES 面试题】倒排索引深入骨髓
- P38 【ES 面试题】Elasticsearch 的写入原理
- P39 【ES 面试题】读写性能调优一
- P40 【ES 面试题】读写性能调优二
- P41 【ES 面试题】ES 的节点类型
- P42 【ES 面试题】搜索引擎和 ES
- P43 【ES 面试题】面试技巧
- P44 【数据库面试题】redis 持久化 rdb 和 aof
- P45 【数据库面试题】redis 单线程为什么快，有哪些线程模型
- P46 【数据库面试题】redis 的过期键有哪些删除策略
- P47 【数据库面试题】redis 缓存如何回收
- P48 【数据库面试题】redis 事务是如何实现的
- P49 【数据库面试题】redis 主从复制的原理
- P50 【数据库面试题】击穿、穿透、雪崩、预热解决方案
- P51 【数据库面试题】Mysql 的隔离级别有哪些
- P52 【数据库面试题】mysql 复制的原理是什么
- P53 【数据库面试题】mysql 聚簇索引和非聚簇索引的区别
- P54 【数据库面试题】mysql 索引的基本原理
- P55 【数据库面试题】mysql 索引结构有哪些，各自的优劣是什么
- P56 【数据库面试题】mysql 锁的类型有哪些
- P57 【数据库面试题】mysql 为什么需要主从同步
- P58 【数据库面试题】mysql 执行计划怎么看
- P59 【数据库面试题】简述 mysql 中索引类型有哪些，以及对数据库的性能的影响
- P60 【数据库面试题】如何处理 mysql 的慢查询
- P61 【数据库面试题】什么是 mysql 的主从复制
- P62 【数据库面试题】索引的设计原则有哪些
- P63 【分布式面试题】分布式 ID 的生成方案有哪些？
- P64 【分布式面试题】雪花算法生成的 ID 由哪些部分组成？
- P65 【分布式面试题】分布式锁在项目中有哪些应用场景？
- P66 【分布式面试题】分布锁有哪些解决方案？
- P67 【分布式面试题】Redis 做分布式锁用什么命令？
- P68 【分布式面试题】Redis 做分布式锁死锁有哪些情况，如何解决？
- P69 【分布式面试题】Redis 如何做分布式锁？
- P70 【分布式面试题】基于 ZooKeeper 的分布式锁实现原理是什么
- P71 【分布式面试题】ZooKeeper 和 Reids 做分布式锁的区别？
- P72 【分布式面试题】MySQL 如何做分布式锁？
- P73 【分布式面试题】分布式架构下，Session 共享有什么方案
-
