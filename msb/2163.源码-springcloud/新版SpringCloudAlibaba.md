# 一、为什么有这课程

Spring Cloud Alibaba 新版本中Seata 1.5.2和Nacos 2.1.0 在性能和使用方面都有很大提升，这节课将从使用和源码的角度详细讲解这两个框架。

# 二、设计注册中心

## 1、分布式框架的注意点：三高架构

- 高可用

  高可用性（High Availability）通常来描述一个系统经过**专门**的设计，从而**减少停工时间**，而保持其服务的高度可用性(一直都能用)。

  解决方案：集群
- 高并发

  高并发（High Concurrency）是互联网分布式系统架构设计中必须考虑的因素之一，它通常是指，通过设计保证**系统能够同时并行处理很多请求**。 高并发相关常用的一些指标有**响应时间**（Response Time），**吞吐量**（Throughput），**每秒查询率**QPS（Query Per Second），**并发用户数**等。

  解决方案：

  - **垂直扩展**：**增强单机硬件性能**
  - **水平扩展**：
- 高性能

  高性能（High Performance）就是指**程序处理速度快，所占内存少，cpu占用率低**。

  解决方案：

  指程序处理速度快： 这里设计我们数据存储结构、访问机制、集群同步

## 2、注册中心的设计

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/370b76a9fa1a4d39ba69f2f9de637121.png)

- 服务注册
- 注册表结构设计
- 服务发现
- 服务订阅
- 服务推送
- 健康检查
- 集群同步：设计到数据同步，数据同步我们有哪些协议 raft 、distro、ZAB

# 三、Nacos作为注册中心源码分析

## 1、项目准备

* 客户端项目：msbshop-parent
  注意版本的对应

  ![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/bc779156c7674e4c8dd5a973623aba7d.png)
* 服务端项目：nacos-2.1.0

  下载对应的nacos，进行编译

  ```
  mvn clean install -DskipTests -Drat.skip=true -f pom.xml
  ```
* 启动源码服务时候指定参数

  ![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/b2c6ac0894cb46668f68675612a8531a.png)

## 2、服务启动入口

#### 2.1 整体流程图

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/42196557ce97408d8902b1d031dde65d.png)

#### 2.2 源码分析

通过学习Nacos1.4 我们知道了我们的注册对应的类是NacosNamingService，那我们Nacos2.1.0是不是也是一样的呢？

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/97a2094a1f5c40bfbfc507181d87a45c.png)

通过上图我们发现里面也有注册的信息，那我们打上断点看一下是否到这里，我们在对应注册方法打上断点，然后debug启动，如图 ：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/78625fabb4034444a857ec23608de01e.png)

我们发现服务启动后他确实通过这里，所以这里是注入的入口，那他是从哪里来这里的呢？

我们想nacos是和Springboot整合，那可能使用了SpringBoot的自动装配

我们查看我们引入的Jar包spring-cloud-starter-alibaba-nacos-discovery.jar 查看里面spring.factoris文件

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/0cd34efd3c21495fbfdf36684f8fa268.png)

我们可以查看自动装配类，在这里我们可以通过名称来推断那个关于注册自动配置类，NacosServiceRegistryAutoConfiguration应该和我们注册相关，我们进入看一下，导入以下类

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/dbe557c92ad044dcb37a450c4decaf7d.png)

我们可以通过上面debug端点看一下堆栈信息，看涉及到那个类

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/bde7371d0fbd4e9d89ba2dfdd2dd3705.png)

他的默认实现类是NacosAutoServiceRegistration

NacosAutoServiceRegistration 实现了ApplicationListener接口，监听事件WebServerInitializedEvent（spring核心方法refresh的完成后广播事件）

#### 2.3 总结

找入口的方式：自动装配类 spring.factories

事件驱动：NacosAutoServiceRegistration实现了applicationListener接口

## 3、实例注册

#### 3.1 整体流程图

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/ab4e3f1de593405ca7d5a623d411566a.png)

#### 3.2 客户端

##### 3.2.1 源码分析

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/a6f5987d51bf4f5b8e89d3d09c534eb1.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/35cdd40aaeec42bfb67f2c24b654b837.png)

我们的初始化代码如下：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/d3a9f62563e3418e85165639c28d366e.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/82ce6c987a9d44a280f218078a2070d5.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/a791f314888641dd94685a2c82f840c4.png)

上面是通过实例的参数ephemeral值来判断是否是grpcClientProxy还是httpClientProxy，我们在他的实例化的位置能判断ephemeral的值

我们根据堆栈信息去看找到instance实例化的位置

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/ee46e3af25c4458a9a5817541f753dbd.png)

具体实例创建

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/190b5d83863b4c14ad6282ece8a790ef.png)

分析NacosDiscoveryProperties![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/8d5c5f62e04f4f6fa7bd0d3ffb95c259.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/31e918a4877b4a7294d30ec2c31888d9.png)

由此我们知道这里使用grpc客户端端和服务端通信，同时我们能得出结论：我们

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/beb4a181466f47a8b2129b8d47cda547.png)

grpcClientProxy的调用

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/79f06e07b41b45df94a70d1ab0bf84df.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/07a40ee2edaa4476a50a976d38856c46.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/f25d21d3e6a6463591db41987e56d81f.png)

##### 3.2.2 源码总结

* 判断变量  1、 debug  2、 全文搜索 定位赋值位置
* 通过ephemeral的值判断是grpc通信，还是http通信，通过这我们能判断ap模式是用的grpc模式，cp模式是用http通信
* 判断服务端处理类的方式，我们可以根据请求参数，找对应服务端的处理类（由于开源框架都是规范的，一般都是根据请求参数来命名，所以可以采用这种方式）

#### 3.3 服务端

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/d0092239af1441f89574b368525acdb5.jpg)

##### 3.3.1源码分析

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/26a80427e44a401d80c55023bfe3c67c.png)

这里我们注意我们实际注册的应该是对应的实例，而不是服务，服务包括多个实例，具体上的实例才有对应的ip和port

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/e98a5da3c2c64154a139342bd4b90149.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/c0ebbff5ab9e4ac3a1e6678b1779be02.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/ed3840857d874a63bc4eb9464d68dfde.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/8aab301210e94cb4870039b154671817.png)

问题：这里一个服务对应一个实例，我们知道一个服务应该对应多个实例，为什么这里对应一个实例呢？ 他是怎样处理的？后面我们进行解答

对事件ClientRegisterServiceEvent的监听，我们可以通过全文搜索来看，哪里对应的处理的

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/f0fb4c744366447abfcc2f19d1109c26.png)下面进行事件监听进行处理：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/b7dc8941859c4c4580708a2b9fdb5861.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/b8aa6d23a3a34b93940b4f63d56a480d.png)

publisherIndexs就是注册表

##### 3.3.2 源码总结

1. 分清实例和服务的关系： 我们实际注册的是实例 ，一个服务包含多个实例
2. 这里注册实例会注册到我们Client中，Client有个Map,key：是service value是对应的一个实例，也就是一个Client对应一个服务的具体实例
3. 我们发送事件后来处理注册表，注册表结构是ConcurrentMap&#x3c;Service, Set&#x3c;String>> publisherIndexes
   里面key:是服务，value对应Client的clientId

## 4、注册表

### 4.1 注册表结构分析

下面是我们nacos2.1.0的注册表

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/b5d9aa23dd514bcbae9f2c8f083a8187.png)

这里是Nacos1.4x的注册表

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/ee2c55fd719f4d74be206947b834b7f0.png)

### 4.2 总结

通过Nacos1.4 和Nacos2.1 版本的注册表结构会发现，1.4 比较复杂，而2.1是比较简单，这样2.1的加锁的地方要少一些，所以2.1的注册表的结构性能要好，所以说我们可以总结一下,Nacoa2.1比Nacos1.4性能好的原因：

1. Nacos2.1 使用的是GRPC性能要好一些
2. Nacos2.1 表结构简单，所以加锁的地方要少一些，性能更好一些

## 5、服务发现

### 5.1 客户端

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/a2292a67de4245c98de2e9de9441bd0e.png)

#### 5.1.1 源码分析

我们需要从客户端找到服务发现的入口，我们注册的入口类是NacosNamingService，那我们服务发现入口应该也在这里：我们看一下有两个方法：getAllInstances和selectInstances

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/92f8bc84bc71459a8632fa81700cde50.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/82c9cf932a2c4de1901ce9d509267890.png)

那具体是那个方法，我们可以在每个方法里面打上断点，然后debug启动后，进行访问

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/661d1b8b2ef14dd38f0158ba3b96f5a3.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/106051abdf674438add0b5c30aab616a.png)

发送请求

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/e524241b700045d48d9aee66096490ed.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/5456027ed9314a87adbcfc64bb993fca.png)

从上图可以判断他是通过selectInstances来获取数据的

我们通过堆栈信息我们能发现，他的调用路径是通过ribbon最终调用selectInstances方法。

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/c6eb6a13445b47f588759524a24cf5a0.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/3aae38ce59f146b7b65a7e285fc987d3.png)

key1: 从缓存中获取数据

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/bf7db4b84d0a4751a8a54420fa0a15de.png)

这里注意，他是从缓存中获取数据，那他一定有定时任务处理这里的数据，否则他就会有脏数据的问题，带着这个问题我们继续学习。

key2：进行订阅

我们服务启动第一次一定是空的，所以我们进行订阅，当定于的clientProxy，具体是那个值呢？

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/db8290726a934d808fdee0ef7b149d93.png)

我们能确定clientProxy的具体实现类是NamingClientProxyDelegate，好我们看一下具体

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/a5c1ed84878c4072a814f73376e3a5ac.png)

key1:定时任务

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/be300ef20d7847e8ad6e6edf24d50948.png)

这里的UpdateTask一定是个Runable，所以我们看他的run方法

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/cdd3431d10f1466d8ce4c5154cc2e124.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/bd0414d7d463487e9ed5cd063d2e088a.png)

总结上图内容：从缓存获取，如果没有则发送请求获取，如果有则判断数据是否超时，在finally里面对应的内容是这个任务每6秒执行一次，如果失败就会扩大两倍时长，最大是一分钟

里面更新缓存中内容如下：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/751501f16d574f369c5764ddb207c126.png)

这里先写内存后写磁盘，那磁盘数据什么时候获取呢？

我们在ServiceInfoHolder构造方法中发现？

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/1327f355086741d6be3662bc87af818a.png)

那我们看一下服务发现对应代码

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/f8c042c29f6d42c1988f5633d21f251e.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/1c322b1b1e5743d986418ab9c57b6d7d.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/bc7b2cbb7728445ebb707db39a6b27b1.png)

#### 5.1.2 源码总结

- 服务启动时候读取磁盘中数据放到缓存
- 读取磁盘数据 如果没有则发送请求获取数据，然后写到缓存
- 读取磁盘数据，如果有则判断时间是否过期，过期则发送请求，写到缓存
- 读取数据是一个定时任务每6秒执行一次，如果失败就会延长，但最大时长是1分钟

### 5.2 服务端

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/508e673fc5c842ed9e78bdbd0a276714.jpg)

#### 5.2.1 源码分析

从上文中我们可以分析出我们服务端处理类应该是ServiceQueryRequestHandler

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/6b618486762449cab366071dde77bc1b.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/d092f7a56b5e411a971b1a588c934e34.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/979eb1b16dc24940bbf46031905936af.png)

从上图可知getAllInstancesFromIndex是重点，它是获取我们对应的实例，来我们重点分析一下：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/c957c4ab1f934d4e96b73d4ce8f06534.png)

1、获取对应的clientId，这一定是在我们的注册表中获取的，注册表示个Map ,key:是服务名称，value:是对应client的set ，不理解的可以参考一下我们的注册表

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/4482a3bc7faf438187cd509208e41529.png)

2、获取对应实例这里我们详细看一下

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/03973e7b54f54753a17438e8da952f84.png)

这里可以和我们注册表中内容详细看一下

#### 5.2.2 源码总结

这里主要是从注册表中获取数据，所以理解这里需要看一下我们的注册表中，各个数据之间的关系

## 6、服务订阅

### 6.1 客户端源码

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/a2292a67de4245c98de2e9de9441bd0e.png)

源码可以参考我们服务发现对应的源码

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/644ccf6f847f487ba6485e24901825ae.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/c47d1abdf562412b98089fb5c0820163.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/bd059a88087e4da8a62c9d69115bae0c.png)

### 6.2 服务端源码

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/8322e18df1c74754baf9e4a7cf0d00ef.jpg)

#### 6.2.1源码分析

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/1419b31f593a4ccdaf842e239c1baf62.png)

key3: 查询服务列表的信息中，会调用serviceStorage.getData(service) 来获取服务的实例，这个和我们服务发现的服务端源码是一样的，这里就不在重复

key4:进行订阅

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/8e5330fb69d3492184f9d983aeabf760.png)

key2:把订阅者和服务进行关系绑定

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/48579359ac5446f9bf179cb5dc914aca.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/304d290e52e34c5ab4e623ec8e38848c.png)

这里和注册相同，每个客户端对应一个Map,Map里面key:是服务  value:就是这个服务对应的实例

key3:发送订阅事件， 我们全文搜索ClientSubscribeServiceEvent 查看处理事件位置

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/f063c749430148248dfe747fd53dea55.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/ff9cc37010024cc48992476dec170078.png)

更新订阅表

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/b9098a26573f4ee5bc4a2e2dd2816863.png)

#### 6.2.2 源码总结

我们的订阅很简单首先是获取对应订阅这个服务的实例，用于返回，然后进行订阅，订阅的信息是我们对应发起定于服务者和被订阅服务会以map形式放到我们的client，然后发送一个事件，这个时间就是更新我们的订阅注册表

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/6af0125c384845f4a0967cbe5988cb1b.png)

## 7、服务变更推送

这里注意我们推送有两种一种是服务变更推送，一种是订阅推送

服务变更推送：对于一个服务来说，订阅者有好多，我们在订阅表中能看到ConcurrentMap&#x3c;Service, Set&#x3c;String>> subscriberIndexes，能获所有订阅者，然后进行推送

订阅者推送：此时服务已经稳定，我这里增加一个msb-order，那对于msb-stock又增加一个订阅者，此时我们应该将msb-stock对应的实例推送给具体新增的实例

### 7.1 订阅推送

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/c7c88a6fd9ec45baad4a0ee73f3572cf.jpg)

#### 7.2.1服务端源码分析

客户端在订阅的时候发送事件更改注册表后，会再发送一个事件，这个事件就会获取对应的服务实例，然后通知订阅者获取对应的服务的实例，这里和上面我们直接订阅返回对应数据有点重复，这里我们可以注意一下，接下来我们看一下源码。

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/5020e9b325264373a3533ed5fd953609.png)

全文搜索ServiceSubscribedEvent查看处理事件的地方

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/ca0df48ab73f45d994dcb2721cd136b0.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/d5496d66597a47498e12daf83e4b4462.png)

我们进入addTask方法

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/2ed6461dd30d4a8faf868f1cc33cccc5.png)

我们想这里先从map中获取如果有则合并，没有则放进去，那我们想一定有个地方从这里来获取这个任务来处理；

我们看一下这个类的构造方法

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/78edd31ad42546c7aaa549d8b5b12ceb.png)

这里有个定时任务来处理我们看一下

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/927f00185e9a431da2584642231a710d.png)

我们进入处理任务

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/0a0c6e2b0d6744d4b30f61580f852b33.png)

这里的processor.process的处理方法

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/422725019753408c94e4c940189ce5e4.png)

我们分析一下上面到底是那个方法，1、我们可以通过debug 2、我们可以猜测，我们想我们处理的任务是PushDelayTask ，所以我们用它PushDelayTask来搜索一下

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/a92b8842e1c04e008619193763ec62c0.png)

所以处理类应该是PushDelayTaskProcessor

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/5d0f06944b7e4ed7a8c1997e972db0cd.png)

PushExecuteTask是实现Runable的线程，那重点应该是他的run方法

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/6daa30a8a3a94c78af3b4cf5a476f706.png)

进入对应的run方法

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/eb2663141a394a9a936db02242cd9381.png)

key1:获取订阅这个服务的客户端ID

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/5489002a56a042699a1c076ac842d2f6.png)

上面是判断是否是全部推送，如果我们有指定的ClientId就不全部推送，如果没有我们就全部推送，我们这是订阅推送，所以有要推送的客户端

key2:进行任务处理

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/77e823e83b31499bbaa9f580a2e2316e.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/7254cff9873a4771ace060bb5724a210.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/a72afdb86a434d0d91d0757aec2d372a.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/7027251733aa48f7b5888cb05f5f3ad7.png)

#### 7.2.2 客户端源码分析

服务端发送请求参数是ServerRequest，那我们怎样在客户端找到对应的处理方法呢？ 还是老办法，用ServerRequest在客户端进行搜索

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/fff1604f2b964bb2a6c8036169a1a5cf.png)

这个ServerRequestHandler是个接口，我们找他的实现类，如下

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/10e54c661a624f5f861578026944907b.png)

那具体的实现类，我们推理可以知道他一定是NamingPushRequestHandler

好我们来分析一下NamingPushRequestHandler

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/cf7e8ad210f6495eae2541d66443fe55.png)

#### 7.2.3 总结

我们新增服务订阅在更新完注册表会发布一个事件ServiceSubscribedEvent，NamingSubscriberServiceV2Impl.会监听事件，然后把订阅到的数据进行推送过去，这期间真正的工作任务是PushExecuteTask他是一个线程，同时注意这里是订阅，所以我们推送的时候，直接推送给新增订阅者就可以

### 7.2 服务变更推送

服务变更推送和订阅推送是一样的只是推送的对象不同，我们订阅推送是给新增订阅者进行推送，服务变更推送是给所有订阅这个服务的推送

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/9908719e64dc4765ade45de9200db571.jpg)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/9322b64b71044538b022f51200038f75.png)

## 8、心跳机制

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/42e51ba25c394259aff315ccffe78c33.jpg)

### 8.1 源码分析

我们进入ConnectionManager里面的start方法中，这个方法上有@PostConstruct，也就是构造方法执行完毕就执行这个方法

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/bced28ccc13b4f8c99a409cdad964f2d.png)

上图中我们可以知道它里面线程是每3秒执行一次：

由于里面方法比较多，这里我们可以看一些关键的点：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/619e5ca6937f404bbe1ae85428785500.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/c65bf5fad68a49599d5fd6b188ea37cc.png)![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/11b28027d4c547a18ee6fcaaf962f2a4.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/115580554f034e95a2881f1097d6eaa6.png)

key5:注销

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/07d6b7de0a744414ba9a893fb214d201.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/efafefd64c5c497285272ec968887ca0.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/f8fb000d21e640ea97bef9b9a9001059.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/e16d0576c28a464592842bf1322c5d71.png)

发布事件ClientDisconnectEvent

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/f6dd3f0242ef42ddab76e3258a3d0a6b.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/e1d1d0e4f4fd4a70848b208a7e28fe0f.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/8e76ae3ec3384ceb8c43760e8f70b97c.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/93b47f448108459b9d232ce116fea190.png)

### 8.2 总结

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/6a08c0144e2b44e0a395a78b9dd2d0b3.png)、

## 9、数据同步

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/b2e076ff364c448d8c3158b2d4769ed7.jpg)

### 9.1 源码分析

我们在实例注册的时候就应该进行集群同步

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/ec9325643c7546449198829484fb5297.png)

全文搜索ClientChangedEvent查看哪里处理

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/cea69f1c922d406cb722e18f73d9bbb6.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/a58d4e4856e24fb39a22f448b6a4d055.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/f9b18a0216f040fcba74a975d9d9dad8.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/13f2426ca52d4e128554d18123e9faee.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/6f33f8beec0947b289adc464f6314dd5.png)

我们进入addTask方法

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/9fd694498ea748ef834c1ea17986613e.png)

进入NacosDelayTaskExecuteEngine的构造方法里面，启动一个定时任务ProcessRunnable

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/8acbd4198f64437d97195e1892672549.png)

查看ProcessRunnable的run方法

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/2dcb876d7f8f426e8059e929738eb6c8.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/b45440a90db340daa59cd9839e81cd8a.png)

我们处理的任务是DistroDelayTask ，所以说我们查看具体方法如下

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/f43db064b4f24475aeafa837555d03d5.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/de4e110be3744e16b1de2a45d1d5ee93.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/7a9741167ddb4d989d0c294c0d35a4de.png)

DistroSyncChangeTask是具体的任务我看一下他的run方法

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/59de275cbc34425d96906faee2b9fbc8.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/329c48086b4d4897a2d415a58f3f3cef.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/e9717df0cf0b4094898af65b2ee4b4b6.png)

处理集群同步

从上图中我们知道集群同步的请求是DistroDataRequest， 那我可以在服务端全文搜索

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/04c8549da90b4fb888de356eb33487d9.png)

处理数据同步

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/1a13e83f8b3c429380e807d7b8b28ee9.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/14d1971e1d83457ea92c40f9809e60eb.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/0306ec408b8c4777a19684e855fdf079.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/4076f20e99ac44638378931d30c599b0.png)

新增实例

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/7f353e5b2a624b64b1453ef85ebc5cec.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/e22d42e3ba8e4ddbacfd0e80fb75240d.png)

### 9.2 总结

这里集群同步时候，我们采用的异步处理，这里和我们服务变更推送类似

## 10、GRPC源码分析

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/94e6b68fb2ac43f58c66d49868371094.png)

### 10.1、客户端源码分析

我们找到客户端注册的代码：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/6b30796225b1466793aca964257de9a2.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/d0bca279153742e492343a42b91ff152.png)

通过他初始化实例，我们知道他他真正的调用方法

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/8c696604aa0d47f6bdde3a3525b8eea0.png)

通过方法getExecuteClientProxy需要确定具体代理类 grpcClientProxy

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/149895442eb648d592db37b2424dd52d.png)

我们查找grpcClientProxy的初始化的地方。

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/9403d79e190846659e258c88a895a869.png)

那NamingGrpcClientProxy应该grpc的核心逻辑

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/aca98f4b5b8e4996ac8fe991a0a0c8f6.png)

我们进入start方法：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/0ee522ee6a3443ff9b0391cd07dc8bfa.png)

上面方法分为两部分：

key1:是将处理的Handler放到对应的List<ServerRequestHandler> serverRequestHandlers  那后面一定是在客户端处理请求的时候，从哪这里面拿到对应的Handler进行处理

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/84eaa68eed2742e8bb1e2cc975003537.png)

key2: 启动这里 这里是关键，我们进来看一下：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/334ebda68a814706a3120ca78d762c19.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/5d1b8d2d678341048eaa9b1e5e7b74a0.png)

上图是简单描述：我们可以看一下第4、5、6、7步

key4:选择一个服务

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/e1be63a9a9194cfe834ac8a7556eef2b.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/7eefc90a0c7f42e7bf3dbe03e7c4e377.png)

key5:连接服务

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/6baf39ab23a348d596a74d1d2a2ea744.png)

key6: 发送事件到队列， 我们可以全文搜索哪里处理这个队列

线程池里面的一个线程正在处理，如

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/35424d4df43c435fbdaef72756128b01.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/71135fd687eb4d649f0ae35530a5c802.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/340903e3b32741329263e903e56d284f.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/b42b7b0e795e449b967d233cde27d183.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/4236b2c431a94bb69fcca0805a611a2e.png)

key7:

如果前面同步连接都失败的话，我们就进行异步连接

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/452d5387f0144fba93e1800922e86891.png)

我们全文搜索就会发现在上文中的第二个线程中会进行处理

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/5aa6fa69e04340f5abd35e62419301f2.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/8b7381f0084e4ed7a134c6c0e66ca5e8.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/f7f9543c9ca0427f857eb92815228c0c.png)

总结：在连接成功还是连接失败后都是异步进行处理，我们可以参考这种方式

### 10.2、服务端源码分析

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/e3af7e0873544b8a8f6a7865109fc943.png)

服务处理rpc的请求，那我们可以进行猜测一下服务端进行搜索RpcServer，如下

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/a44a1a47239441858c3c266ee9b2a8b5.png)

那BaseRpcServer应该是处理RPC的请求，我们看一下对应代码

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/13fe900e8f6647c681f7ebfa98845a2d.png)

通过名称我们应该知道他是启动server，那我们查看哪里调用他

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/ecd2d0abb2f84265b85602bb4ed5d4b5.png)

通过上图我们知道，他是构造方法之后我们进行服务启动

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/aaa3731c12f841508fc24a2a5ce5a216.png)

key1: 增加拦截器 ，这里主要获取一些远端Ip+port信息

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/4f525cb4d9f64bb6b940a58c4fb50838.png)

key2:  这里面重点是建立连接和处理请求

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/ee5b2a41eabb4f37a5f51d603c57aa2a.png)

key2.1 处理请求

我们想我们Springmvc处理请求的时候，我们是根据路径判断对应的controller，这里我们的请求应该是那个具体的handler呢？ 我们是根据type，这个type其实就是请求类型

如下图：获取对应type ,然后根据type获取对应的的RequestHandler

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/4a78359481fb451091d0af8d03df1d83.png)

我们进入getByRequestType

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/9f80113e5ba04c6e93c0fefae031fd2d.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/f3cb3967454d4b06b002c6daa695968f.png)从上图我们知道这里是将相应handler以map的形式进行存放，那这个key我们通过debug知道他对应的值，为请求参数的的名称

那什么时候进行初始化的：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/0b6dc0cba5b84fa8978102a37a3f1a9f.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/0f8fe3683e674e2ca594bf526d09b5f5.png)

那Handler对应泛型的第一参数类型名称是什么，那我们拿InstanceRequestHandler来举例：也就是InstanceRequest

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/a96da3e0de7e4f2797a1bddb2c4dc1a8.png)

总结：我们处理实例就是用的监听器来获取对应的所有实例，然后以map处理，所有请求从这map中拿取对应的对象。

# 四、Nacos作为配置中心源码分析

## 1、什么是Naocs配置中心

官方文档： [https://github.com/alibaba/spring-cloud-alibaba/wiki/Nacos-config](https://github.com/alibaba/spring-cloud-alibaba/wiki/Nacos-config)

Nacos 提供用于存储配置和其他元数据的 key/value 存储，为分布式系统中的外部化配置提供服务器端和客户端支持。使用 Spring Cloud Alibaba Nacos Config，您可以在 Nacos Server 集中管理你 Spring Cloud 应用的外部属性配置。

## 2、Nacos的使用

### 2.1 给Nacos2.1.0配置数据库

倒入数据

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/7b73603d4f4f4972bc8ebf1d2b69bae2.png)

修改内容

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/11fa6b963f3f4543bc43b1fe5b93c8f5.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/a2ce3b60bd1f451f87ae66e2691d329d.png)

### 2.2  版本推荐

https://github.com/alibaba/spring-cloud-alibaba/wiki/%E7%89%88%E6%9C%AC%E8%AF%B4%E6%98%8E

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/71b3c3f4b18a4b40b7d7ce8d44b72dec.png)

### 2.3 父工程指定版本

```
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>2.3.2.RELEASE</version>
</parent>
<properties>
    <maven.compiler.source>8</maven.compiler.source>
    <maven.compiler.target>8</maven.compiler.target>
    <spring-cloud-alibaba.version>2.2.9.RELEASE</spring-cloud-alibaba.version>
</properties>

<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>com.alibaba.cloud</groupId>
            <artifactId>spring-cloud-alibaba-dependencies</artifactId>
            <version>${spring-cloud-alibaba.version}</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
```

### 2.4 子工程引入依赖

```
 <dependencies>
        <dependency>
            <groupId>com.alibaba.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-nacos-config</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>

        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <optional>true</optional>
        </dependency>
        <!--  单元测试类 -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>

    </dependencies>
```

### 2.5 利用接口对配置进行操作

```

public class ConfigListenerTest {
    private static String serverAddr = "localhost";
    private static String dataId = "nacos-demo.yaml";
    private static String group = "DEFAULT_GROUP";
    private static ConfigService configService;

    @Test
    public void testListener() throws NacosException, InterruptedException {
        Properties properties = new Properties();
        properties.put(PropertyKeyConst.SERVER_ADDR, serverAddr);
        //获取配置服务
        configService = NacosFactory.createConfigService(properties);;
        //获取配置
        String content = configService.getConfig(dataId, group, 5000);
        System.out.println(content);
        //注册监听器
        CountDownLatch countDownLatch = new CountDownLatch(5);
        configService.addListener(dataId, group, new Listener() {
            @Override
            public Executor getExecutor() {
                return null;
            }

            @Override
            public void receiveConfigInfo(String configInfo) {
                System.out.println("配置发生变化:" + configInfo);
                countDownLatch.countDown();
            }

        });
        countDownLatch.await();
    }
    @Test
    public void publishConfig() throws NacosException {
        Properties properties = new Properties();
        properties.put(PropertyKeyConst.SERVER_ADDR, serverAddr);
        //获取配置服务
        configService = NacosFactory.createConfigService(properties);
        configService.publishConfig(dataId,group,"age: 30", ConfigType.PROPERTIES.getType());
    }


    @Test
    public void removeConfig() throws NacosException, InterruptedException {
        Properties properties = new Properties();
        properties.put(PropertyKeyConst.SERVER_ADDR, serverAddr);
        //获取配置服务
        configService = NacosFactory.createConfigService(properties);
        boolean isRemoveOk = configService.removeConfig(dataId, group);
        System.out.println(isRemoveOk);
    }

}

```

### 2.6 和Springboot整合

```
@RefreshScope
@RestController
public class NacosConfigController {

    @Value("${name}")
    private String name;

    @RequestMapping("/getName")
    public String getName(HttpServletRequest httpRequest){
        return name;
    }
}

```

### 2.7  里面放置定时任务

启动

```
@EnableScheduling
@SpringBootApplication
public class NacosConfigApplication {
    public static void main(String[] args)  {
         SpringApplication.run(NacosConfigApplication.class);
    }
}
```

增加定时任务

```
@RestController
public class NacosConfigController {

    @Value("${name}")
    private String name;

    @RequestMapping("/getName")
    public String getName(HttpServletRequest httpRequest){
        return name;
    }
    // 定时任务每5秒执行一次
    @Scheduled(cron = "*/2 * * * * ?")
    public void execute(){
        System.out.println("获取姓名：" + name);
    }


}

```

发现问题：如果我们更改配置，则对应的定时任务就失败

### 2.8 分析失败原因

#### 2.8.1 Schedule执行原理

当我们更改配置的时候，我们看日志会进行容器的刷新

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/6682a35bcb5c4f409ae2cfc2a6444a64.png)

此时容器中并没有对应的NacosConfigController对应的实例对象。所以我们的定时任务不会执行，我们可以调用一下我们controller对应的方法，然后容器中就有了NacosConfigController对应的实例，有了这个实例，我们的定时任务就会执行，因为这个定时任务是基于后置处理器进行执行的。

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/30e0e523f678442bb8bf63281164413a.png)

#### 2.8.2 @RefreshScope对象被清理的原因

那为什么刷新容器后NacosConfigController这Bean都没有了呢？

因为在我们更新配置后，我们的容器会将@RefreshScope标注的对象清掉，好我们来分析一下

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/7399d98a20544789b7dbe1e8ad0fd46b.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/60d2a066ac4e4d3dbe0e352b85b29d3a.png)

Scope对应的有一个接口

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/ca6c9d17045c4b3f8eed72ba75685322.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/d173b37729f041529b20ba43f2e7249f.png)

```

```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/d54c1c3c553a40248259705e0e4dbca7.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/e105bea3e0144e86be375f0a25a3c1cb.png)

真正实例创建 除了单例、多例、其他

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/5d23b5b790ae488aa1e3008370de304a.png)

我们分析这里从缓存中获取，

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/aa89bb4bb5a24baf89183da80019ca8b.png)

我们知道 单例获取是从单例对象池中，原型是重新构建Bean ,而我们Refresh是从BeanLifecycleWraperCache里面

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/c8f2dd7a356841ec94952fbbdf264858.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/bd00a539c5bb459b88743fecf3b14d71.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/be581d2c751d4d30b4bde88a840ec892.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/d4527f02753b4f009c7ff6de99877744.png)

也就是从缓存中获取对象，同时这里有个destroy

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/819053e658b746ba9ee430a0a304fe11.png)

总结一下：

1、@RefreshScope中有个@Scope里面值是Refresh,他创建对象是放到对应的缓存中，我们通过GenericScope#get方法从缓存中获取对应Bean对象

2、我们更新数据的时候，会发送一个RefreshEvent事件，容器会监听这个事件，然后将缓存中数据进行删除

3、而我们定时任务是在创建bean的后置处理器中执行的，此时bean都被清理了，所以定时任务也没有了

4、我们再次访问对应的NacosConfigController的时候，我们就会创建对应的对象放到缓存，此时定时任务也就执行了

解决问题方案：

我们缓存删除是监听RefreshEvent事件而处理的，我们现在也可以监听事件进行处理，监听事件，如果事件发生，它回调用对应监听器，然后就会实例化，这样定时任务也可以执行

```
@Slf4j
@RefreshScope
@RestController
public class NacosConfigController implements ApplicationListener<RefreshScopeRefreshedEvent> {

    @Value("${name}")
    private String name;

    @RequestMapping("/getName")
    public String getName(HttpServletRequest httpRequest){
        return name;
    }
    // 定时任务每5秒执行一次
    @Scheduled(cron = "*/2 * * * * ?")
    public void execute(){
        System.out.println("获取姓名：" + name);
    }


    @Override
    public void onApplicationEvent(RefreshScopeRefreshedEvent event) {
        log.info("监听刷新容器事件");
    }
}

```

## 3、源码分析

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/c0f4a18872d1495499c34f84c3a8f109.png)

### 3.1 服务启动加载bootstrap.propertis

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/fe82b99f7ff84d50bb76b17dbc752903.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/ef0054527c994102a82cba9f367320fb.png)

准备环境加载bootstrap.propertis，这里他会发送事件进行监听，我们可以直接进入	#load我们可以在load打上断点

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/a298fb0436234b7da9d37f500cad598f.png)

总结：我们可以根据堆栈信息来发现，它是在准备环境的时候发送一个事件，ConfigFileApplicationListener监听事件，最后调用PropertiesPropertySourceLoader 对资源进行加载

### 3.2 客户端拉取远程配置进行合并

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/ed0161730ff648d08cfd5529f2e4bbbf.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/1f1853e0884d49f7a165ab2c3462bae4.png)

这里最终会调用用到NacosPropertySourceLocator#  ，我们在locate上打上断点可以看一下堆栈信息

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/384d946df46647fab02089df6126ef08.png)

好，我们看一下locate方法

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/e864dc4b4a7c44919edd637a23dfd8b0.png)

记载配置文件后最终会用composite进行合并，那他们无论加载共享配置、扩展配置和当前应用配置最终会调到NacosPropertySourceLocator#loadNacosDatalfPresent

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/596fe539af5f4279b2b86d11a87ce9f4.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/a457e4f1ad0b4bbe884aa30036cbfcc8.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/9325e81bd43b4173a849082e7af6ca14.png)![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/c3f64f9672a94f6c85992665f13346f8.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/0dc5a76030444680a8f676deff2ee4a8.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/088bc1e5aebf457c97846120428b079e.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/5d2766cea280499f8a36b44bdf739f40.png)

重点我们看一下他的配置加载

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/bd4e2e0a1b3b46638d8f435446853514.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/36c124ab3bac48828c0a4229cffd44cf.png)

key1:从本地获取配置

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/db8b612e5a71414f98e7acceba4e458e.png)

key2:远程获取配置

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/51f79f57c5d84a549389ba0d8844ec72.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/2018a5c164794840b9b4cc18ebb1312f.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/b5a980095d5d49c5a6fa086c2249aab5.png)

总结：这里我们注意Spring的扩展点之一:在我们Bean构建之前加载一些数据，比如配置属性，我们就可以用这个扩展点，这里加载配置中心内容，这个内容用于后面bean对象创建。

例如：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/70f489aef9a445dd895ec8157ba28aa5.png)

进行配置

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/006d4cd787aa48ef9f7368c40843a33b.png)

### 3.3 服务端处理配置拉取

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/ebea61b6888746ceab2bbb1facd1a9f9.png)

客户端请求为ConfigQueryRequest，则从服务端进行搜索找到对应处理类

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/d1cc56dcffb74a7b833bb348f0155683.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/d300caea4cf2492893978b49d7462dc4.png)

下面对应的方法比较长，我们可以看一下关键的点

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/25104b534f6b4d5bb86f15e9a7683af3.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/58e57227695c496cb71813c48be66259.png)

总结：分析我们发送请求是从缓存文件中获取到的，这里带出两个问题，1、因为我们是从缓存中获取的，那我们直接修改数据库应该是不起作用的   2、缓存一定是从数据库中获取的，那什么时候设置进去的呢

### 3.4 服务启动进行数据库数据加载

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/e32f5ab8699d4971bc5c894bf5c4f120.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/3c244073b99247338fbdffa3a9d8b152.png)

服务端启动时就会依赖DumpService的init方法，从数据库中load 配置存储在本地磁盘上，并将一些重要的元信息例如MD5值缓存在内存中。服务端会根据心跳文件中保存的最后一次心跳时间，来判断到底是从数据库dump全量配置数据还是部分增量配置数据(如果机器上次心跳间隔是6h以内的话)。

全量dump当然先清空磁盘缓存，然后根据主键ID每次捞取一千条配置刷进磁盘和内存。增量dump就是捞取最近六小时的新增配置(包括更新的和删除的)，先按照这批数据刷新一遍内存和文件，再根据内存里所有的数据全量去比对一遍数据库，如果有改变的再同步一次，相比于全量dump的话会减少一定的数据库IO和磁盘I0次数。

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/6d2cf38914074da0b06a53a46b92ed51.png)

构建bean时候一定初始化@PostConstruct 对应的方法

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/81a0749651994f43b2b567fd822de674.png)

判断全量和增量获取数据

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/267471c63ffb425880cfb3f86d288279.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/cea77ebace75435b85750651a2eb064b.png)

全量拉取

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/0547847b4bcc4655998d5164169e9214.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/7a51073bb3534a70a0fd13917c8d2ddb.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/a68e062228e04aafa24f40dad128df6f.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/b4ba6f8c486c40ceb364e67af3a9a6b7.png)

总结：这里的md5值的我们学习，我们md5算法获取对应文件的值，如果这个值变化说明文件发生了变化，利用这中方式我们可以通过文件md5值来判断其他是否有变化

### 3.5 加载数据发生变更，发送事件

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/5919423e085341b587fe85778e28560a.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/81fbd84468134f12b93956b57e2807ca.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/99952b33ee634fbb97f048dbc645224c.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/232b2fdc2dfa41259b98e1706703c0a1.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/05ad8d5c73c44ab3ab74ff0ac056088d.png)

如果队列写满则如下操作：但是我们上面是服务启动暂时没有新的服务进来，所以这里subscriber是空的也就无法调用

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/f7639306616a40fb87d782347579d84b.png)

如果正常情况下应该是放到队列里面，那就应该有取的地方,全文搜索对应的queue

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/93f4420dcd824d81a01100daf4239f39.png)

哪里调用到这里呢？

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/fd91d1d96536465c847733d578b54d20.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/cc743c7c05e54c6593375811e219a2ae.png)

从这里我们可以知道DefaultPublisher是一个线程，所有会调用run方法

**总结：我们应该学会发布监听事件**

### 3.6 监听配置变更

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/ed0e28dddd774c0783db95dda653fd2e.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/9b007bac8ca2450e9d6d5477267a67f7.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/e7e91a7be76b46328ebac131559c4152.png)

全文搜索ApplicationReadyEvent，查看NacosContextRefresher

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/6a269c1b889449c3a596cea17fb0fd3e.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/db9833f35ecb40aeb3e54dfb704c2a60.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/132881ed705c406587c47fec848345f1.png)

发送RefreshEvent事件后，就是对@RefreshScope标志的实例进行删除，这里可以参考**2.7分析失败原因**

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/633ef46fb65445699b19b0478da14977.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/9acdea99b10244ebbda51c4d6cbc3c38.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/aa115010d0cc48419efc50a49f89d5dc.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/ebb0d70e3ab24dbdb392d40f4f28dbe9.png)

key1:销毁对应实例

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/bd296f2d9cad4ca19d6698d734b705c4.png)

key2:发送事件RefreshScopeRefreshedEvent  这也是我们通过监听这个事件，来实例化对应的实例的

### 3.7 服务端端更改配置

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/b49d9b44ad72457e88702366d13959bc.png)

我们配置中心发布配置，一定是调用SpringMVC中的Controller方法 ，我们进行全文搜索，通过名称进行分析应该是ConfigController

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/f9ead1443b9b4189a9bf8897d27e39b1.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/3d521cce60724979b3e122b38486ee62.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/55480b65558248d79037cbfea686ef36.png)

key1: 更新数据库

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/0c2003665cea47b4807b301f33ed5fdf.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/c0f79a826b114888befc0ef1a23b7f47.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/7f173c61ce134b4c96ea8e8e9d624ff6.png)

key2:发布事件，进行客户端通知配置变更，以及集群同步

全文搜索ConfigDataChangeEvent

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/cbbd5720c6554311a039b206cb264f11.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/9e76d114e50740d2aefbf652e17ba2e9.png)

AsyncRpcTask是一个任务，并向里面传递了rpcQuene的一个任务队列，我看一下他是怎样处理的。

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/4c6aaa502c174bb39449347aeeca3656.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/ef386c937c564dc89cd158fba3f2e853.png)

key1:我们看一下数据持久化， key2中集群数据同步就是发送一个rpc请求

我们重点key1：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/e3db3dd2a08546569e73ce4643a5becc.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/dd192e1ae4fb45f9a67618e5842ecfee.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/efa6d0f3642e455d9f2d985fd651feba.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/7c02bf2caab9455bb0249d504ffbb9fa.png)

上面我们解释过这里是异步处理一定有个地方处理他

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/009a61444f3e416c8bc63408066bc586.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/b34d63225d9042ac83352fac0edbd6fd.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/2dd54e31a44645259831e072d42341ed.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/90341c4288594ca08c924b6c0fcd8e74.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/b18991dac31a4572aedede6a735f5801.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/278697157d784a51bce20c2b0bb77f22.png)

发布LocalDataChangeEvent事件

全文搜索对应的事件

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/5a813af521dc47ce9b9801bf7dae5ac5.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/a6d2c20949874ea5b2337bc1b27bc553.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/7d626593a9694bdfb6eb116439381dc5.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/37af0434d32a47acbbd33c5d9bec34cd.png)

查看任务RpcPushTask对应的方法：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/47f4465bbbf84bbd88fb15f2d4a6eb6d.png)

向客户端发送请求，进行配置变更的通知

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/957d734b158d4008944332dd5fc62ae5.png)

### 3.8 客户端处理事件

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/e80cc3cf9d8440e4b129c6d592e03471.png)

我们知道发送请求的是ConfigChangeNotifyRequest，好，我们到客户端全文搜索一下，找对应的处理

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/974e09f0abab4b08bed8878e84ea0ba4.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/38e47f7bfce74c92b9267503f5e8ae02.png)

我们全文搜索listenExecutebell找对应的处理位置

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/2e65061ac3f9409dab4c185d10ecab70.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/3759971f18b24608a69107972a5b00e2.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/fbffe24abbfb43f792d6e1256a963e7f.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/8cce027d73344ebe9c5cca36cb4d434e.png)

### 3.9 客户端定时拉取配置

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/a7ed759e80e649edbf3d4090ad1d332c.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/a329a5d93898476db7f5a3443b16f32a.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/db693761e2754bdcbde164bcbb02202f.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/7bface5ad4a74c8097554e6b8d8b8973.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/b2e3ffdcdb49402189a2ec30ee102cd0.png)

3.10 于Nacos1.x长轮询做对比

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1670652088093/6767a4fb44fe49c99b9d5ea4d339d3d0.png)
