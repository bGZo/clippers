# 课程目标

1、了解Elastic-Job的基本特性

2、掌握Elastic-Job开发与配置方式（包括Java开发和Spring Boot开发），掌握任务类型和任务分片策略

3、了解Elastic-Job运维平台的使用

4、掌握Elastic-Job运行原理

# 内容定位

适合了解了Quartz的调度模型之后，想要知道如何基于ZK配置Quartz和如何实现任务分片的同学

# Quartz-Misfire

**什么情况下错过触发？错过触发怎么办？**

线程池只有5个线程，当有5个任务都在执行的时候，第六个任务即将触发，这个时候任务就不能得到执行。在quartz.properties有一个属性misfireThreshold，用来定义触发器超时的"临界值"，也就是超过了这个时间，就算错过触发了。

例如，如果misfireThreshold是60000（60秒），9点整应该执行的任务，9点零1分还没有可用线程执行它，就会超时（misfires）。

下面这些原因可能造成 misfired job:

1、 没有可用线程

2、 Trigger被暂停

3、 系统重启

4、 禁止并发执行的任务在到达触发时间时，上次执行还没有结束。

错过触发怎么办？Misfire策略设置

每一种Trigger都定义了自己的Misfire策略，不同的策略通过不同的方法来设置。

standalone工程 MisfireTest

```java
Trigger trigger = TriggerBuilder.newTrigger().withIdentity("trigger1", "group1").startNow()
.withSchedule(SimpleScheduleBuilder.simpleSchedule().
withMisfireHandlingInstructionNowWithExistingCount().
withIntervalInSeconds(1).
repeatForever()).build();
```

大体上来说有3种：

1、 忽略

2、 立即跑一次

3、 下次跑

详细内容参考：

https://www.cnblogs.com/daxin/p/3919927.html

https://www.cnblogs.com/skyLogin/p/6927629.html

```
怎么避免任务错过触发？ 
```

合理地设置线程池数量，以及任务触发间隔。

# **认识E** **-Job**

## **任务调度高级需求**

Quartz的不足：

1、 作业只能通过DB抢占随机负载，无法协调

2、 任务不能分片——单个任务数据太多了跑不完，消耗线程，负载不均

3、 作业日志可视化监控、统计

## **发展历史**

E-Job是怎么来的？

在当当的ddframe框架中，需要一个任务调度系统（作业系统）。

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1463/1657891874033/eb0623e09a6d4978bdce2ba3fe9cbe1d.png)

实现的话有两种思路，一个是修改开源产品，一种是基于开源产品搭建（封装），当当选择了后者，最开始这个调度系统叫做dd-job。它是一个无中心化的分布式调度框架。因为数据库缺少分布式协调功能（比如选主），替换为Zookeeper后，增加了弹性扩容和数据分片的功能。

Elastic-Job是ddframe中的dd-job作业模块分离出来的作业框架，基于Quartz和Curator开发，在2015年开源。

轻量级，无中心化解决方案。

为什么说是去中心化呢？因为没有统一的调度中心。集群的每个节点都是对等的，节点之间通过注册中心进行分布式协调。E-Job存在主节点的概念，但是主节点没有调度的功能，而是用于处理一些集中式任务，如分片，清理运行时信息等。

思考：如果ZK挂了怎么办？

每个任务有独立的线程池。

![](file:///C:\Users\root\AppData\Local\Temp\ksohtml12492\wps2.jpg)![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1463/1657891874033/173e0f562bb240048c043f9b9d604468.png)

从官网开始

[http://elasticjob.io/docs/elastic-job-lite/00-overview/](http://elasticjob.io/docs/elastic-job-lite/00-overview/)

[https://github.com/elasticjob](https://github.com/elasticjob)

Elastic-Job最开始只有一个elastic-job-core的项目，在2.X版本以后主要分为Elastic-Job-Lite和Elastic-Job-Cloud两个子项目。其中，Elastic-Job-Lite定位为轻量级无中心化解决方案，使用jar包的形式提供分布式任务的协调服务。而Elastic-Job-Cloud使用Mesos + Docker的解决方案，额外提供资源治理、应用分发以及进程隔离等服务（跟Lite的区别只是部署方式不同，他们使用相同的API，只要开发一次）。

## **功能特性**

* 分布式调度协调：用ZK实现注册中心
* 错过执行作业重触发（Misfire）
* 支持并行调度（任务分片）
* 作业分片一致性，保证同一分片在分布式环境中仅一个执行实例
* 弹性扩容缩容：将任务拆分为n个任务项后，各个服务器分别执行各自分配到的任务项。一旦有新的服务器加入集群，或现有服务器下线，elastic-job将在保留本次任务执行不变的情况下，下次任务开始前触发任务重分片。
* 失效转移failover：弹性扩容缩容在下次作业运行前重分片，但本次作业执行的过程中，下线的服务器所分配的作业将不会重新被分配。失效转移功能可以在本次作业运行中用空闲服务器抓取孤儿作业分片执行。同样失效转移功能也会牺牲部分性能。
* 支持作业生命周期操作（Listener）
* 丰富的作业类型（Simple、DataFlow、Script）
* Spring整合以及命名空间提供
* 运维平台

## **项目架构**

应用在各自的节点执行任务，通过ZK注册中心协调。节点注册、节点选举、任务分片、监听都在E-Job的代码中完成。

![](file:///C:\Users\root\AppData\Local\Temp\ksohtml12492\wps3.jpg)![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1463/1657891874033/55469ff7787b4bfbb90a2738bd08b0fd.png)

# **Java开发**

以下关于 `ElasticJob`的介绍来自[官方文档](https://shardingsphere.apache.org/pdf/shardingsphere-elasticjob_docs_cn.pdf)：

ElasticJob是面向互联网生态和海量任务的分布式调度解决方案，由两个相互独立的子项目ElasticJob‐Lite和ElasticJob‐Cloud组成。它通过弹性调度、资源管控、以及作业治理的功能，打造一个适用于互联网场景的分布式调度解决方案，并通过开放的架构设计，提供多元化的作业生态。它的各个产品使用统一的作业API，开发者仅需一次开发，即可随意部署。ElasticJob已于2020年5月28日成为Apache ShardingSphere的子项目。

`ElasticJob`能够让开发工程师不再担心任务的线性吞吐量提升等非功能需求，使他们能够更加专注于面向业务编码设计；同时，它也能够解放运维工程师，使他们不必再担心任务的可用性和相关管理需求，只通过轻松的增加服务节点即可达到自动化运维的目的。

# 工程以及环境

工程：ejob-standalone

* `Java 8`及其以上版本。
* `Maven 3.5.0`及其以上版本。
* `ZooKeeper 3.6.0`及其以上版本。

## **pom依赖**

`ElasticJob‐Lite`会将作业注册到 `ZooKeeper`上，在定义的命名空间下，创建作业名称节点，用于区分不同作业，所以作业一旦创建则不能修改作业名称，如果修改作业名称将视为新的作业。

添加依赖（`3.0.1`是目前最新的 `Releases`版本）：

```powershell
<dependency>
<groupId>com.dangdang</groupId>
<artifactId>elastic-job-lite-core</artifactId>
<version>3.0.1</version>
</dependency>
```

## **任务类型**

注意：任何类型的作业，都是基于实现接口的不一样或者传入的参数不一样，没有其他区别

standalone工程

注册中心配置：

```java
private static CoordinatorRegistryCenter createRegistryCenter() {
        ZookeeperConfiguration zc = new ZookeeperConfiguration("192.168.xx.184:9000", "my-job");
        zc.setConnectionTimeoutMilliseconds(40000);
        zc.setMaxRetries(5);
        CoordinatorRegistryCenter regCenter = new ZookeeperRegistryCenter(zc);
        regCenter.init();
        return regCenter;
    }

```

ElasticJob的作业分类基于class和type两种类型。基于class的作业需要开发者自行通过实现接口的方式织入业务逻辑；基于type的作业则无需编码，只需要提供相应配置即可。基于class的作业接口的方法参数shardingContext包含作业配置、片和运行时信息。可通过getShardingTotalCount()、getShardingItem()等方法分别获取分片总数和运行在本作业服务器的分片序列号等。
`ElasticJob`目前提供 `Simple`、`Dataflow`这两种基于 `class`的作业类型，并提供 `Script`、`HTTP`这两种基于 `type`的作业类型，用户可通过实现 `SPI`接口自行扩展作业类型。

**SimpleJob**

SimpleJob: 简单实现，未经任何封装的类型。需实现SimpleJob接口。

ejob-standalone MySimpleJob.java

```java
public class MyElasticJob implements SimpleJob {
	public void execute(ShardingContext context) {
	System.out.println(String.format("Item: %s | Time: %s | Thread: %s ",
	context.getShardingItem(), new SimpleDateFormat("HH:mm:ss").format(new Date()),Thread.currentThread().getId()));
    }
}
```

```java

```

定义了作业，还需要对作业进行配置，比如作业的名称、分片数、cron时间表达式以及是否需要失效转移等，主要通过JobConfiguration类来完成这些配置，它提供了构建者风格的方法，比如下面的作业配置，作业名称为MySimpleJob、作业分片数为3，并且在每一分钟的第30秒执行任务，调用overwrite方法用来设置在作业启动时是否将本地配置覆盖到注册中心（默认不覆盖，所以本地修改了cron时间表达式会不起作用），如果需要覆盖（方法传入true），则每次启动时都将使用本地配置（即以本地的作业配置为主，不然本地修改作业配置不会起作用）。调用failover方法用于设置是否开启失效转移（仅适用于开启了 monitorExecution，默认开启 monitorExecution，但默认不开启失效转移），ElasticJob不会在本次执行过程中进行重新分片（给作业节点分配作业分片），而是等待下次调度之前才开启重新分片流程。当作业执行过程中服务器宕机，失效转移允许将该次未完成的任务在另一作业节点上补偿执行。

> 开启失效转移功能，ElasticJob会监控作业每一分片的执行状态，并将其写入注册中心，供其他节点感知。在一次运行耗时较长且间隔较长的作业场景，失效转移是提升作业运行实时性的有效手段；对于间隔较短的作业，会产生大量与注册中心的网络通信，对集群的性能产生影响。而且间隔较短的作业并未见得关注单次作业的实时性，可以通过下次作业执行的重分片使所有的分片正确执行，因此不建议短间隔作业开启失效转移。 另外需要注意的是，作业本身的幂等性，是保证失效转移正确性的前提.

```java
    private static JobConfiguration createJobConfiguration() {
        return JobConfiguration.newBuilder("MySimpleJob", 3)
                .cron("30 * * * * ?")
                .overwrite(true)
                .failover(true)
                .build();
    }

```

**DataFlowJob**

DataFlowJob：Dataflow类型用于处理数据流，必须实现fetchData()和processData()的方法，一个用来获取数据，一个用来处理获取到的数据。其他的是一样的，跟Simple没有区别

ejob-standalone MyDataFlowJob.java

```java
public class MyDataFlowJob implements DataflowJob<String> {
@Override
public List<String> fetchData(ShardingContext shardingContext) {
// 获取到了数据
return Arrays.asList("qingshan","jack","seven");
}

@Override
public void processData(ShardingContext shardingContext, List<String> data) {
data.forEach(x-> System.out.println("开始处理数据："+x));
}
}
```

**ScriptJob**

Script：Script类型作业意为脚本类型作业，支持shell，python，perl等所有类型脚本。D盘下新建1.bat，内容：

@echo ------【脚本任务】Sharding Context: %*

ejob-standalone script.ScriptJobTest

只要指定脚本的内容或者位置
