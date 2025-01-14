# 一、分布式系统遇到的问题

## 1、服务雪崩效应

在分布式系统中,由于网络原因或自身的原因,服务一般无法保证 100% 可用。如果一个服务出现了问题，调用这个服务就会出现线程阻塞的情况，此时若有大量的请求涌入，就会出现多条线程阻塞等待，进而导致服务瘫痪。

由于服务与服务之间的依赖性，故障会传播，会对整个微服务系统造成灾难性的严重后果，这就是服务故障的 “雪崩效应” 。

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/a4185860072e4ebd9148cc8c4062bb1f.png)

雪崩发生的原因多种多样，最常见原因： 程序Bug，大流量请求，硬件故障，缓存击穿

- 程序Bug:  比说我们以前我们支付模块增加一个功能，我们监听一个Rocketmq消息然后进行业务的处理，至于什么业务处理我们就不说了，上线后就报警了，我们的支付成功的订单直线下降，这是什么原因，我们查看日志有很多消费消息的日志，一直在打，我们马上回滚，然后排查问题，我们发现线上的功能消费设置的是CONSUME_FROM_FIRST_OFFSET 这个是一个新的订阅组第一次启动从队列的最前位置开始消费，后续再启动接着上次消费的进度开始消费，而我们监听的消息是已经存在的，所以里面存在了很多的消息，为此消费端一直消费对应的消息，导致一直运行，从而影响了支付的功能。我们改为CONSUME_FROM_LAST_OFFSET【一个新的订阅组第一次启动从队列的最后位置开始消费后续再启动接着上次消费的进度开始消费】。
- 大流量请求：在秒杀和大促开始前,如果准备不充分,瞬间大量请求会造成服务提供者的不可用。
- 硬件故障：可能为硬件损坏造成的服务器主机宕机, 网络硬件故障造成的服务提供者的不可访问。
- 缓存击穿：一般发生在缓存应用重启, 缓存失效时高并发，所有缓存被清空时,以及短时间内大量缓存失效时。大量的缓存不命中, 使请求直击后端,造成服务提供者超负荷运行,引起服务不可用。

我们无法完全杜绝雪崩源头的发生，只有做好足够的容错，保证在一个服务发生问 题，不会影响到其它服务的正常运行。也就是＂[雪落而不雪崩]()＂。

# 二、常见容错方案

要防止雪崩的扩散，我们就要做好服务的容错，容错说白了就是保护自己不被猪队友拖垮的一些措施, 下面介绍常见的服务容错思路和组件

## 1、常见的容错思路

常见的容错思路有[隔离、超时、限流、熔断、降级]()这几种，下面分别介绍一下。

### 1.1 隔离

大的方向我们可以进行物理隔离，比如说我们可以把用户实例分为好几个组，一个组为4台为核心服务提供，另一组是2台为非核心的组提供服务，这样就进行了物理隔离，如果我们进入某个实例内我们想，比如我们的RPC调用我们调用的请求都会先进入一个队列里面然后再消费，那一个出了问题，也会影响其他的服务调用，那我们为每个服务的调用都会创建一个队列，这样进行了队列隔离，同时我们我在后面设置一个单独的线程池进行线程池隔离，但是如果我们后面访问的下游如果没有隔离会有什么问题，是不是还会出现问题，比如我们后面进行访问的时候都是一个数据库。

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/131e52c9729149738e39f726a57f8a43.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/18cdaad8dd5842e3b12f49e9a44e9e87.png)

### 1.1 超时

在上游服务调用下游服务的时候，上游服务设置一个最大响应时间，如果超过这个时间，下游未作出反应，上游服务就断开请求，释放掉线程。

### 1.2 限流

限制请求核心服务提供者的流量，使大流量拦截在核心服务之外，这样可以更好的保证核心服务提供者不出问题，对于一些出问题的服务可以限制流量访问。

- 计数器固定窗口算法
- 计数器滑动窗口算法
- 漏桶算法
- 令牌桶算法

### 1.3 熔断

在互联网系统中，当下游服务因访问压力过大而响应变慢或失败，上游服务为了保护系统整体的可用性，可以暂时切断对下游服务的调用。

> 这种牺牲局部，保全整体的措施就叫做熔断。

服务熔断一般有三种状态：

* [熔断关闭状态（Closed）]()

  服务没有故障时，熔断器所处的状态，对调用方的调用不做任何限制。
* [熔断开启状态（Open）]()

  后续对该服务接口的调用不再经过网络，直接执行本地的[fallback]()方法。
* [半熔断状态（Half-Open）]()

  尝试恢复服务调用，允许有限的流量调用该服务，并监控调用成功率。如果成功率达到预期，则说明服务已恢复，进入熔断关闭状态；如果成功率仍旧很低，则重新进入熔断关闭状态。

  【现实世界的断路器大家肯定都很了解，断路器实时监控电路的情况，如果发现电路电流异常，就会跳闸，从而防止电路被烧毁。

  软件世界的断路器可以这样理解：实时监测应用，如果发现在一定时间内失败次数/失败率达到一定阈值，就“跳闸”，断路器打开——此时，请求直接返回，而不去调用原本调用的逻辑。跳闸一段时间后（例如10秒），断路器会进入半开状态，这是一个瞬间态，此时允许一次请求调用该调的逻辑，如果成功，则断路器关闭，应用正常调用；如果调用依然不成功，断路器继续回到打开状态，过段时间再进入半开状态尝试——通过”跳闸“，应用可以保护自己，而且避免浪费资源；而通过半开的设计，可实现应用的“自我修复“。

  所以，同样的道理，当依赖的服务有大量超时时，在让新的请求去访问根本没有意义，只会无畏的消耗现有资源。比如我们设置了超时时间为1s,如果短时间内有大量请求在1s内都得不到响应，就意味着这个服务出现了异常，此时就没有必要再让其他的请求去访问这个依赖了，这个时候就应该使用断路器避免资源浪费。】

  ![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/5132d505b770482a9a2a406a9ac133ae.png)

### 1.4 降级

所谓降级就是我们调用的服务异常超时等原因不能正常返回的情况下，我们返回一个缺省的值。

【由于降级经常和熔断一起使用，所以就会有熔断降级的说法。】

## 2、常见的容错组件

* **Hystrix**

  Hystrix是由Netﬂix开源的一个延迟和容错库，用于隔离访问远程系统、服务或者第三方库，防止  级联失败，从而提升系统的可用性与容错性。
* **Resilience4J**

  Resilicence4J一款非常轻量、简单，并且文档非常清晰、丰富的熔断工具，这也是Hystrix官方推 荐的替代产品。不仅如此，Resilicence4j还原生支持Spring Boot 1.x/2.x，而且监控也支持和prometheus等多款主流产品进行整合。
* **Sentinel**

  Sentinel 是阿里巴巴开源的一款断路器实现，本身在阿里内部已经被大规模采用，非常稳定。

下面是三个组件在各方面的对比：

|                   | Sentinel                                                                                  | Hystrix                                           | resilience4j                                                        |
| ----------------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------------------------- |
| 隔离策略          | 信号量隔离（并发线程数限流）                                                              | 线程池隔离/信号量隔离                             | 信号量隔离                                                          |
| 熔断降级策略      | 基于慢调用比例、异常比例、异常数                                                          | 基于异常比例                                      | 基于异常比例、响应时间                                              |
| 实时统计实现      | 滑动窗口（LeapArray）                                                                     | 滑动窗口（基于 RxJava）                           | Ring Bit Buffer                                                     |
| 动态规则配置      | 支持近十种动态数据源                                                                      | 支持多种数据源                                    | 有限支持                                                            |
| 扩展性            | 多个扩展点                                                                                | 插件的形式                                        | 接口的形式                                                          |
| 基于注解的支持    | 支持                                                                                      | 支持                                              | 支持                                                                |
| 单机限流          | 基于 QPS，支持基于调用关系的限流                                                          | 有限的支持                                        | Rate Limiter                                                        |
| 集群流控          | 支持                                                                                      | 不支持                                            | 不支持                                                              |
| 流量整形          | 支持预热模式与匀速排队控制效果                                                            | 不支持                                            | 简单的 Rate Limiter 模式                                            |
| 系统自适应保护    | 支持                                                                                      | 不支持                                            | 不支持                                                              |
| 热点识别/防护     | 支持                                                                                      | 不支持                                            | 不支持                                                              |
| 多语言支持        | Java/Go/C++                                                                               | Java                                              | Java                                                                |
| Service Mesh 支持 | 支持 Envoy/Istio                                                                          | 不支持                                            | 不支持                                                              |
| 控制台            | &#x3c;font color="red">提供开箱即用的控制台，可配置规则、实时监控、机器发现等&#x3c;/font> | &#x3c;font color="red">简单的监控查看&#x3c;/font> | &#x3c;font color="red">不提供控制台，可对接其它监控系统&#x3c;/font> |

# 三、sentinel基本操作

## 1、 什么是Sentinel

Sentinel (分布式系统的流量防卫兵) 是阿里开源的一套用于**服务容错**的综合性解决方案。它以流量为切入点, 从**流量控制、熔断降级、系统负载保护**等多个维度来保护服务的稳定性。

**Sentinel 具有以下特征:**

- **[丰富的应用场景]()**：Sentinel承接了阿里巴巴近 10 年的双十一大促流量的核心场景, 例如秒杀（即突发流量控制在系统容量可以承受的范围）、消息削峰填谷、集群流量控制、实时熔断下游不可用应用等。
- **[完备的实时监控]()**：Sentinel提供了实时的监控功能。通过控制台可以看到接入应用的单台机器秒级数据, 甚至 500 台以下规模的集群的汇总运行情况。
- **[广泛的开源生态]()**：Sentinel提供开箱即用的与其它开源框架/库的整合模块, 例如与 Spring Cloud、Dubbo、gRPC 的整合。只需要引入相应的依赖并进行简单的配置即可快速地接入Sentinel。
- **[完善的 SPI 扩展点]()**：Sentinel提供简单易用、完善的 SPI 扩展接口。您可以通过实现扩展接口来快速地定制逻辑。例如定制规则管理、适配动态数据源等。

**Sentinel 分为两个部分:**

- [核心库]()（Java 客户端）不依赖任何框架/库,能够运行于所有Java 运行时环境，同时对Dubbo/Spring Cloud 等框架也有较好的支持。
- [控制台]()（Dashboard）基于Spring Boot开发，打包后可以直接运行，不需要额外的Tomcat等应用容器。

## 2、基本概念

* **资源**

  > **资源就是Sentinel要保护的东西**
  >

  资源是 Sentinel 的关键概念。它可以是 Java 应用程序中的任何内容，例如，由应用程序提供的服务，或由应用程序调用的其它应用提供的服务，甚至可以是一段代码。
* **规则**

  > **规则就是用来定义如何进行保护资源的**
  >

  围绕资源的实时状态设定的规则，可以包括[流量控制规则]()、[熔断降级规则以及系统保护规则]()。所有规则可以动态实时调整

## 3、Sentinel 功能和设计理念

Sentinel的主要功能就是容错，主要体现为下面这三个：

#### 3.1 流量控制（上游）

流量控制在网络传输中是一个常用的概念，它用于调整网络包的数据。任意时间到来的请求往往是随机不可控的，而系统的处理能力是有限的。我们需要根据系统的处理能力对流量进行控制。

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/c249bb8826864797b955443c0e07940a.gif)

> Sentinel作为一个调配器，可以根据需要把随机的请求调整成合适的形状。

#### 3.2 熔断降级（下游）

当检测到调用链路中某个资源出现不稳定的表现，例如请求响应时间长或异常比例升高的时候，则对这个资源的调用进行限制，让请求快速失败（或者其他处理方式），避免影响到其它的资源而导致级联故障。

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/3ffc7cee1064431fa37c728ac3eb5283.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/31f8c2fe47104a8fab9da145e21bd7d1.png)

## 5、**Sentinel快速开始**

在官方文档中，定义的Sentinel进行资源保护的几个步骤：

1. 定义资源
2. 定义规则
3. 检验规则是否生效

### 5.1 抛出异常的方式定义资源

```java
Entry entry = null;
// 务必保证 finally 会被执行
try {
  // 资源名可使用任意有业务语义的字符串，注意数目不能太多（超过 1K），超出几千请作为参数传入而不要直接作为资源名
  // EntryType 代表流量类型（inbound/outbound），其中系统规则只对 IN 类型的埋点生效
  entry = SphU.entry("自定义资源名");
  // 被保护的业务逻辑
  // do something...
} catch (BlockException ex) {
  // 资源访问阻止，被限流或被降级
  // 进行相应的处理操作
} catch (Exception ex) {
  // 若需要配置降级规则，需要通过这种方式记录业务异常
  Tracer.traceEntry(ex, entry);
} finally {
  // 务必保证 exit，务必保证每个 entry 与 exit 配对
  if (entry != null) {
    entry.exit();
  }
}
```

### 5.2 api的实现

&#x3c;font color="red">msb-user项目中&#x3c;/font>

- 引入依赖

  ```pom
  <dependency>
       <groupId>com.alibaba.csp</groupId>
       <artifactId>sentinel-core</artifactId>
       <version>1.8.1</version>
  </dependency>
  ```
- 代码测试

```java
@Slf4j
@RestController
public class ApiController {

    private static final String RESOURCE_NAME = "API-RESOURCE";
    @RequestMapping("getInfo")
    public String getInfo(){
        Entry entry = null;
        // 务必保证 finally 会被执行
        try {
            // 资源名可使用任意有业务语义的字符串，注意数目不能太多（超过 1K），超出几千请作为参数传入而不要直接作为资源名
            // EntryType 代表流量类型（inbound/outbound），其中系统规则只对 IN 类型的埋点生效
            entry = SphU.entry(RESOURCE_NAME);
            // 被保护的业务逻辑
            String str = "业务逻辑正常处理";
            log.info("====="+str+"=====");
            return str;
        } catch (BlockException ex) {
            // 资源访问阻止，被限流或被降级
            // 进行相应的处理操作
            log.info("Block...!");
            return "业务被限流了！";
        } catch (Exception ex) {
            // 若需要配置降级规则，需要通过这种方式记录业务异常
            Tracer.traceEntry(ex, entry);
        } finally {
            // 务必保证 exit，务必保证每个 entry 与 exit 配对
            if (entry != null) {
                entry.exit();
            }
        }
        return null;
    }

    /**
     * 定义流控规则
     */
    @PostConstruct
    private static void initFlowRules(){
        List<FlowRule> rules = new ArrayList<>();
        FlowRule rule = new FlowRule();
        //设置受保护的资源
        rule.setResource(RESOURCE_NAME);
        // 设置流控规则 QPS
        rule.setGrade(RuleConstant.FLOW_GRADE_QPS);
        // 设置受保护的资源阈值
        rule.setCount(1);
        rules.add(rule);
        // 加载配置好的规则
        FlowRuleManager.loadRules(rules);
    }
}
```

缺点：

- 业务侵入性很强，需要在controller中写入非业务代码.
- 配置不灵活 若需要添加新的受保护资源 需要手动添加 init方法来添加流控规则

### 5.3 注解方式定义资源

**@SentinelResource注解实现**

在定义了资源点之后，我们可以通过Dashboard来设置限流和降级策略来对资源点进行保护。同时还能  通过@SentinelResource来指定出现异常时的处理策略。

@SentinelResource用于定义资源，并提供可选的异常处理和fallback 配置项。其主要参数如下:

| **属性**     | **作用**                                                                                                                                                                                                                                                                                                                                                       |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| value              | 资源名称                                                                                                                                                                                                                                                                                                                                                             |
| entryType          | entry类型，标记流量的方向，取值IN/OUT，默认是OUT                                                                                                                                                                                                                                                                                                                     |
| blockHandler       | 处理BlockException的函数名称,函数要求：&#x3c;br>1.必须是public&#x3c;br/>2.返回类型 参数与原方法一致&#x3c;br/>3.默认需和原方法在同一个类中。若希望使用其他类的函数，可配置blockHandlerClass，并指定blockHandlerClass里面的方法。                                                                                                                                      |
| blockHandlerClass  | 存放blockHandler的类,对应的处理函数必须static修饰。                                                                                                                                                                                                                                                                                                                  |
| fallback           | 用于在抛出异常的时候提供fallback处理逻辑。fallback函数可以针对所有类型的异常（除了 exceptionsToIgnore 里面排除掉的异常类型）进行处理。函数要求：&#x3c;br/>1.返回类型与原方法一致&#x3c;br/>2.参数类型需要和原方法相匹配&#x3c;br/>3.默认需和原方法在同一个类中。若希望使用其他类的函数，可配置fallbackClass ，并指定fallbackClass里面的方法。                          |
| fallbackClass      | 存放fallback的类。对应的处理函数必须static修饰。                                                                                                                                                                                                                                                                                                                     |
| defaultFallback    | 用于通用的 fallback 逻辑。默认fallback函数可以针对所有类型的异常进行处理。若同时配置了 fallback 和 defaultFallback，以fallback为准。函数要求：&#x3c;br/>1.返回类型与原方法一致&#x3c;br/>2.方法参数列表为空，或者有一个Throwable类型的参数。&#x3c;br/>3.默认需要和原方法在同一个类中。若希望使用其他类的函数，可配置fallbackClass ，并指定 fallbackClass 里面的方法。 |
| exceptionsToIgnore | 指定排除掉哪些异常。排除的异常不会计入异常统计，也不会进入fallback逻辑，而是原样抛出。                                                                                                                                                                                                                                                                               |
| exceptionsToTrace  | 需要trace的异常                                                                                                                                                                                                                                                                                                                                                      |

- 引入依赖

  ```pom
  <dependency>
      <groupId>com.alibaba.csp</groupId>
      <artifactId>sentinel-annotation-aspectj</artifactId>
      <version>1.8.1</version>
  </dependency>
  ```
- 切面支持

  ```java
  @Configuration
  public class SentinelAspectConfiguration {

      @Bean
      public SentinelResourceAspect sentinelResourceAspect() {
          return new SentinelResourceAspect();
      }
  }
  ```
- 代码编写

  &#x3c;font color="red">注意 这里面必须把以前的@PostConstruct导入的规则给注释掉，否则可能有冲突&#x3c;/font>

```java
@Slf4j
@RestController
public class SentinelResourceController {

    //http://localhost:8001/testAspect/12
    @GetMapping("/testAspect/{id}")
    @SentinelResource(value = "testAspect",
            fallback = "fallback",fallbackClass = CommonException.class,
            blockHandler = "handleException",blockHandlerClass = CommonException.class
    )
    public Result testAspect(@PathVariable("id") Integer id){
        if(Integer.compare(id,Integer.parseInt("0")) == -1){
            throw new IllegalArgumentException("参数异常");
        }
        log.info("处理业务信息");
        return Result.ok("测试注解方式限流正常");
    }


    @PostConstruct
    private static void initFlowRules(){
        List<FlowRule> rules = new ArrayList<>();
        FlowRule rule = new FlowRule();
        //设置受保护的资源
        rule.setResource("testAspect");
        // 设置流控规则 QPS
        rule.setGrade(RuleConstant.FLOW_GRADE_QPS);
        // 设置受保护的资源阈值
        rule.setCount(1);
        rules.add(rule);
        // 加载配置好的规则
        FlowRuleManager.loadRules(rules);
    }
}

```

```java
@Slf4j
public class CommonException {
    public static Result fallback(Integer id,Throwable e){
        log.error("出现业务异常");
        return Result.error(-1,"===业务异常==");
    }

    public static Result handleException(Integer id, BlockException e){
        log.error("触发限流机制");
        return Result.error(-2,"====触发限流机制==");
    }
}
```

这里的规则，需要我们自己编写，并且我们这里

### 5.4 整合springboot

1. 引入依赖

   ```pom
   <dependency>
       <groupId>com.alibaba.cloud</groupId>
       <artifactId>spring-cloud-starter-alibaba-sentinel</artifactId>
   </dependency>
   ```
2. 修改配置

   ```pom
   spring: 
   	cloud:
   		sentinel: 
   			transport:
                   port: 9999 #跟控制台交流的端口,随意指定一个未使用的端口即可
                   dashboard: localhost:8080 # 指定控制台服务的地址
   ```

### 5.5 引入控制台

Sentinel 提供一个轻量级的控制台, 它提供机器发现、单机资源实时监控以及规则管理等功能。

#### 第1步 下载jar包,解压到文件夹

https://github.com/alibaba/Sentinel/releases

#### 第2步 启动控制台

```sh
# 直接使用jar命令启动项目(控制台本身是一个SpringBoot项目)
java -Dserver.port=8080 -Dcsp.sentinel.dashboard.server=localhost:8080 -Dproject.name=sentinel-dashboard -jar sentinel-dashboard-1.8.1.jar
```

把dashboard自己也当成一个资源加入到了dashboard中来进行监控，如果不想把dashboard自己加入控制台监控可以使用简单启动指令如下:

```sh
java -Dserver.port=8080 -jar sentinel-dashboard-1.8.1.jar
```

#### 第4步: 访问控制台

> 用户可以通过如下参数进行配置：
>
> -Dsentinel.dashboard.auth.username=sentinel 用于指定控制台的登录用户名为 sentinel；
>
> -Dsentinel.dashboard.auth.password=123456 用于指定控制台的登录密码为 123456；如果省略这两个参数，默认用户和密码均为 sentinel；
>
> -Dserver.servlet.session.timeout=7200 用于指定 Spring Boot 服务端 session 的过期时间，如 7200 表示 7200 秒；60m 表示 60 分钟，默认为 30 分钟；
>
> 访问http://localhost:8080/#/login ,默认用户名密码： sentinel/sentinel

&#x3c;font color="red">Sentinel 会在客户端首次调用的时候进行初始化，开始向控制台发送心跳包，所以要确保客户端有访问量；&#x3c;/font>

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/1318a8765e954c21aff82f74577b0c52.png)

**补充：了解控制台的使用原理**

Sentinel的控制台其实就是一个SpringBoot编写的程序。我们需要将我们的微服务程序注册到控制台上, 即在微服务中指定控制台的地址, 并且还要开启一个跟控制台传递数据的端口,  控制台也可以通过此端口调用微服务中的监控程序获取微服务的各种信息。

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/b97b8f029fff4367bda6252da47f0bec.png)

## 6、Sentinel规则（dashboard）

### 6.1 流控规则

**流量控制**（flow control），其原理是监控应用流量的 QPS 或并发线程数等指标，当达到指定的阈值时对流量进行控制，以避免被瞬时的流量高峰冲垮，从而保障应用的高可用性。一条限流规则主要由下面几个因素组成，我们可以组合这些元素来实现不同的限流效果：

| Field           | 说明                                        | 默认值                      |
| --------------- | ------------------------------------------- | --------------------------- |
| resource        | 资源名，即限流规则的作用对象                |                             |
| count           | 限流阈值                                    |                             |
| grade           | 限流阈值类型（QPS 或并发线程数）            | QPS 模式                    |
| limitApp        | 流控针对的调用来源                          | default，代表不区分调用来源 |
| strategy        | 调用关系限流策略：直接、链路、关联          | 直接                        |
| controlBehavior | 流量控制效果（直接拒绝、Warm Up、匀速排队） | 直接拒绝                    |
| clusterMode     | 是否集群限流                                | 否                          |

> **流量控制**，其原理是监控应用流量的[QPS(每秒查询率)]() 或[并发线程数]()等指标，当达到指定的阈值时对流量进行控制，以避免被瞬时的流量高峰冲垮，从而保障应用的高可用性。

第1步: 点击【簇点链路】，我们就可以看到访问过的接口地址，然后点击对应的【流控】按钮，进入流控规则配置页面。新增流控规则界面如下:

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/0a8496f3bcd8424b9304131ed8bc5708.png)

* **资源名：**唯一名称，默认是请求路径，可自定义。
* **针对来源：**Sentinel可以针对调用者进行限流,填写【微服务名】,指定对哪个微服务进行限流 ,默认[default]()(不区分来源,全部限制)。
* **阈值类型/单机阈值：**

  * QPS（每秒请求数量）: 当调用该接口的QPS达到阈值的时候，进行限流。
  * 线程数：当调用该接口的线程数达到阈值的时候，进行限流。
* **是否集群：**暂不需要集群

> 接下来我们以QPS为例来研究限流规则的配置。

#### 6.1.1 简单配置

##### QPS

1. 代码

   ```java
   //com.msb.controller.SimpleController
   @RestController
   public class SimpleController {
       @GetMapping("/simple/qps")
       public String qps(){
           //模拟一次网络延时
           try {
               Thread.sleep(100);
           } catch (InterruptedException e) {
               e.printStackTrace();
           }
           return  "简单测试qps";
       }

   }
   ```
2. 流控规则

   ![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/c932e0da3bfb4dd290beb1ac2bfbfb3e.png)
3. 快速访问/simple/qps 接口，观察效果。

> 此时发现，当QPS > 1的时候，服务就不能正常响应，而是返回Blocked by Sentinel (ﬂow limiting)结果。

http://localhost:8001/simple/qps

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/5bf61a037d234c63b3a748eb1e494f22.png)

&#x3c;font color="red">**BlockException异常统一处理**&#x3c;/font>

springwebmvc接口资源限流入口在**HandlerInterceptor**的实现类**AbstractSentinelInterceptor**的preHandle方法中，对异常的处理是**BlockExceptionHandler**的实现类

> **sentinel 1.7.1 引入了sentinel-spring-webmvc-adapter.jar**

自定义BlockExceptionHandler 的实现类统一处理BlockException

```java
package com.msb.handle;

@Slf4j
@Component
public class CustomBlockExceptionHandler implements BlockExceptionHandler {
    @Override
    public void handle(HttpServletRequest request, HttpServletResponse response, BlockException e) throws Exception {
        log.info("BlockExceptionHandler BlockException================"+e.getRule());

        Result r = null;

        if (e instanceof FlowException) {
            r = Result.error(100,"接口限流了");

        } else if (e instanceof DegradeException) {
            r = Result.error(101,"服务降级了");

        } else if (e instanceof ParamFlowException) {
            r = Result.error(102,"热点参数限流了");

        } else if (e instanceof SystemBlockException) {
            r = Result.error(103,"触发系统保护规则了");

        } else if (e instanceof AuthorityException) {
            r = Result.error(104,"授权规则不通过");
        }

        //返回json数据
        response.setStatus(500);
        response.setCharacterEncoding("utf-8");
        response.setContentType(MediaType.APPLICATION_JSON_VALUE);
        new ObjectMapper().writeValue(response.getWriter(), r);

    }
}
```

##### 线程数

并发数控制用于保护业务线程池不被慢调用耗尽。例如，当应用所依赖的下游应用由于某种原因导致服务不稳定、响应延迟增加，对于调用者来说，意味着吞吐量下降和更多的线程数占用，极端情况下甚至导致线程池耗尽。

【为应对太多线程占用的情况，业内有使用隔离的方案，比如通过不同业务逻辑使用不同线程池来隔离业务自身之间的资源争抢（线程池隔离）。这种隔离方案虽然隔离性比较好，但是代价就是线程数目太多，线程上下文切换的 overhead 比较大，特别是对低延时的调用有比较大的影响。】

&#x3c;font color="red">Sentinel 并发控制不负责创建和管理线程池，而是简单统计当前请求上下文的线程数目（正在执行的调用数目），如果超出阈值，新的请求会被立即拒绝，效果类似于信号量隔离。并发数控制通常在调用端进行配置。&#x3c;/font>

1. 代码

   ```java
   //com.msb.controller.SimpleController#testThread
   @GetMapping("/simple/thread")
   public String testThread(){
       //模拟一次网络延时
       try {
           Thread.sleep(2*1000);
       } catch (InterruptedException e) {
           e.printStackTrace();
       }
       return  "简单测试线程";
   }
   ```
2. 流控规则

   ![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/b8418a0dc1b9401d91c6dfc284717c90.png)
3. 快速访问/simple/thread接口，观察效果。

   ![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/f8c22b94476b44528ccd205180a83c2f.png)

#### 6.1.2 配置流控模式

点击上面设置流控规则的**【编辑】**按钮，然后在编辑页面点击**【高级选项】**，会看到有流控模式一栏。

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/39a3b4d8073a4bb48b65c5c15129dfff.png)

sentinel共有三种流控模式，分别是：

- [直接（默认）]()：指定来源对于该资源的访问达到限流条件时，开启限流。
- [关联]()：当与该资源设置了关联的资源达到限流条件（来源+阈值类型+单机阈值）时，开启限流 [适合做应用让步]
- [链路]()：当从某个上游资源接口访问过来的流量达到限流条件时，开启限流。

下面呢分别演示三种模式：

##### 直接流控模式

> 直接流控模式是最简单的模式，当指定的接口达到限流条件时开启限流。上面案例使用的就是直接流控模式。

##### 关联流控模式

当两个资源之间具有资源争抢或者依赖关系的时候，这两个资源便具有了关联。比如对数据库同一个字段的读操作和写操作存在争抢，读的速度过高会影响写得速度，写的速度过高会影响读的速度。如果放任读写操作争抢资源，则争抢本身带来的开销会降低整体的吞吐量。可使用关联限流来避免具有关联关系的资源之间过度的争抢，举例来说，`read_db` 和 `write_db` 这两个资源分别代表数据库读写，我们可以给 `read_db` 设置限流规则来达到写优先的目的：设置 `strategy` 为 `RuleConstant.STRATEGY_RELATE` 同时设置 `refResource` 为 `write_db`。这样当写库操作过于频繁时，读数据的请求会被限流。

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/41ec47e6ddba4da0aa57e7eecccc50e1.png)

1. 代码

   ```java
   @RestController
   public class FlowControllerModleContoller {

       @GetMapping("/flowModle/read")
       public String readRead(Integer orderId){
           return  "读资源";
       }
       @GetMapping("/flowModle/write")
       public String relation2(Integer orderId){
           return  "写资源";
       }
   }
   ```
2. 流控规则

   ![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/6618968b504d4633b044b9844a9d2f40.png)
3. jmeter测试

   ![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/d51271a9a9ed4f93ac1a0bc7969c6666.png)

   ![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/c18bcffe9c214d39aabc41904825cab8.png)
4. 查看监控图

   ![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/ad134f562df74f848793eed30b1e1986.png)

##### 链路流控模式

链路流控模式指的是，当从某个接口过来的资源达到限流条件时，开启限流。它的功能有点类似于针对 来源配置项，区别在于：**针对来源是针对上级[微服务]()，而链路流控是针对上级[接口]()，也就是说它的粒度更细**。

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/d70537facffd42e58196fa51036caef6.png)

1. 代码

   编写controller

   ```java
   //com.msb.controller.FlowControllerModleContoller
   @GetMapping("/linkModle/test1")
   public String test1(Integer userId){
       userService.getUser();
       return  "成功";
   }
   @GetMapping("/linkModle/test2")
   public String test2(Integer userId){
       userService.getUser();
       return  "成功";
   }
   ```

   编写service

   ```java
   @Service
   public class UserService {

       @SentinelResource(value = "getUser")
       public String getUser(){
           return "获取到用户信息";
       }
   }
   ```
2. 流控规则

   ![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/3ec1d77a8e3948e8bd236ed8516309a6.png)
3. 添加配置

   我们需要将web-context-unify参数设置为false，将其配置为false既可以根据不同的URL进行链路限流，如果不配置将不会生效

   ![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/8bff2353914d410090bdc79e05c62fd8.png)
4. jmeter测试

   ![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/7612167c008d4388b74f98a884e241a8.png)

   ![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/838c704911da45ba8aacff445a5969b8.png)
5. 访问/linkModle/test1

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/2ff866cf912d4844aad78ef3341e97dd.png)

#### 6.1.3 流控效果

当 QPS 超过某个阈值的时候，则采取措施进行流量控制。流量控制的效果包括以下几种：快速失败（直接拒绝）、Warm Up（预热）、匀速排队（排队等待）。对应 FlowRule 中的 controlBehavior 字段。

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/adeedf9e18c54b14a9f5d95dd1e1834f.png)

##### **快速失败（默认）**

&#x3c;font color = "red">当QPS超过任意规则的阈值后，新的请求就会被立即拒绝，拒绝方式为抛出FlowException&#x3c;/font>这种方式适用于对系统处理能力确切已知的情况下，比如通过压测确定了系统的准确水位时。

##### **Warm Up**

它从开始阈值到最大QPS阈值会有一个缓冲阶段，一开始的阈值是最大QPS阈值的1/3，然后慢慢增长，直到最大阈值。

即预热/冷启动方式。当系统长期处于低水位的情况下，当流量突然增加时，直接把系统拉升到高水位可能瞬间把系统压垮。通过"冷启动"，让通过的流量缓慢增加，在一定时间内逐渐增加到阈值上限，给冷系统一个预热的时间，避免冷系统被压垮。

&#x3c;font color="red">冷加载因子: codeFactor 默认是3，即请求 QPS 从 threshold / 3 开始，经预热时长逐渐升至设定的 QPS 阈值。  &#x3c;/font>

通常冷启动的过程系统允许通过的 QPS 曲线如下图所示：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/14941c0f96504c0dad099030d409f606.png)

> 场景主要用于启动需要额外开销的场景，例如建立数据库连接等。

1. 代码

```java
@RestController
public class FlowControlEffectController {

    @RequestMapping("/warmup")
    public String testWarmUp(){
        try {
            Thread.sleep(200);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        return "测试流控效果===热启动";
    }
}
```

2、流控规则

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/347216df49184b6f8baf95670bf943d5.png)

3、jmeter测试

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/f688c3f8605e40b8a52a8d3e7ea0aba1.png)

4、查看监控结果

查看你会发现首先会达到3 （阈值的1/3）然后等3秒后会达到阈值10

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/87ca2cd955d74f8182e83d1c6e244ab9.png)

##### **排队等待**

让请求以均匀的速度通过，单机阈值为每秒通过数量，其余的排队等待； 它还会让设置一个超时时间，当请求超过超时间时间还未处理，则会被丢弃。

该方式的作用如下图所示：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/3d8f03a8209a4094bc960d6819bd1f4a.png)

这种方式主要用于处理间隔性突发的流量，例如消息队列。想象一下这样的场景，在某一秒有大量的请求到来，而接下来的几秒则处于空闲状态，我们希望系统能够在接下来的空闲期间逐渐处理这些请求，而不是在第一秒直接拒绝多余的请求。

&#x3c;font color="red">注意：匀速排队模式暂时不支持 QPS > 1000 的场景。&#x3c;/font>【因为他的单位毫秒，所以最多是1秒通过一个，也就是1000qps】

1. 代码

   com.msb.controller.FlowControlEffectController#testRateLimiter

   ```java
   @RequestMapping("/rateLimiter")
   public String testRateLimiter(){
       try {
           Thread.sleep(200);
       } catch (InterruptedException e) {
           e.printStackTrace();
       }
       return "测试流控效果===匀速排队";
   }
   ```
2. 流控规则

   ![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/17986e150c4e4757b056ea9903ccef85.png)
3. jmeter测试

   ![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/7ffe9506ebab49a2a36bdfdabb4de141.png)
4. 查看监控图

   ![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/c7413f9359fe4ec8aae6590ef506043a.png)

### 6.2 降级规则

除了流量控制以外，对调用链路中不稳定的资源进行熔断降级也是保障高可用的重要措施之一。一个服务常常会调用别的模块，可能是另外的一个远程服务、数据库，或者第三方 API 等。例如，支付的时候，可能需要远程调用银联提供的 API；查询某个商品的价格，可能需要进行数据库查询。然而，这个被依赖服务的稳定性是不能保证的。如果依赖的服务出现了不稳定的情况，请求的响应时间变长，那么调用服务的方法的响应时间也会变长，线程会产生堆积，最终可能耗尽业务自身的线程池，服务本身也变得不可用。

熔断降级规则说明熔断降级规则（DegradeRule）包含下面几个重要的属性：

| Field              | 说明                                                                                                           | 默认值     |
| ------------------ | -------------------------------------------------------------------------------------------------------------- | ---------- |
| resource           | **资源名**，即规则的作用对象                                                                             |            |
| grade              | **熔断策略**，支持慢调用比例/异常比例/异常数策略                                                         | 慢调用比例 |
| count              | **最小请求数**，慢调用比例模式下为慢调用临界 RT（超出该值计为慢调用）；异常比例/异常数模式下为对应的阈值 |            |
| timeWindow         | **熔断时长**，单位为 s                                                                                   |            |
| minRequestAmount   | **最小请求数**，熔断触发的最小请求数，请求数小于该值时即使异常比率超出阈值也不会熔断（1.7.0 引入）       | 5          |
| statIntervalMs     | **统计时长，**（单位为 ms），如 60*1000 代表分钟级（1.8.0 引入）                                         | 1000 ms    |
| slowRatioThreshold | **比例阈值**，慢调用比例阈值，仅慢调用比例模式有效（1.8.0 引入）                                         |            |

降级规则就是设置当满足什么条件的时候，对服务进行降级。Sentinel提供了三个衡量条件：平均响应时间、异常比例、异常数。

#### 6.2.1 慢调用比例

慢调用比例 (`SLOW_REQUEST_RATIO`)：选择以慢调用比例作为阈值，需要设置允许的慢调用 RT（即最大的响应时间），请求的响应时间大于该值则统计为慢调用。当单位统计时长（`statIntervalMs`）内请求数目大于设置的最小请求数目，并且慢调用的比例大于阈值，则接下来的熔断时长内请求会自动被熔断。经过熔断时长后熔断器会进入探测恢复状态（HALF-OPEN 状态），若接下来的一个请求响应时间小于设置的慢调用 RT 则结束熔断，若大于设置的慢调用 RT 则会再次被熔断。

1. 代码

   ```JAVA
   //com.msb.controller.DegradationRuleController#slowRequestRatio
   @RequestMapping("/slowRequestRatio")
   public String slowRequestRatio(){
       try {
           Thread.sleep(200);
       } catch (InterruptedException e) {
           e.printStackTrace();
       }
       return "熔断降级==慢调用比例";
   }
   ```
2. 流控规则

   ![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/1ca5e4de89394c5db178f688c7edda20.png)
3. jmeter测试

   ![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/8ea3e1fda7144f02801f72dc155df125.png)
4. 查看监控图

   查看效果发生流控，每两秒重试一次，我们可以通过查看jemter中查看结果树来判断， 会发现有个重试，每次重试间隔应该是两秒

   ![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/5096d871e836420dbd0541ed2e45c4c3.png)

#### 6.2.2 异常比例

当单位统计时长（`statIntervalMs`）内请求数目大于设置的最小请求数目，并且异常的比例大于阈值，则接下来的熔断时长内请求会自动被熔断。经过熔断时长后熔断器会进入探测恢复状态（HALF-OPEN 状态），若接下来的一个请求成功完成（没有错误）则结束熔断，否则会再次被熔断。异常比率的阈值范围是 `[0.0, 1.0]`，代表 0% - 100%。

1. 代码

   ```java
   //com.msb.controller.DegradationRuleController#errorRatio
   // 下面这个方式有待研究
   private AtomicInteger atomicInteger =new AtomicInteger(1);
   @RequestMapping("/errorRatio")
   public String errorRatio(){
       atomicInteger.getAndIncrement();
       log.info("现在的数值：{}",atomicInteger.get() );
       if (atomicInteger.get() % 2 == 0){
           //模拟异常和异常比率
           int i = 1/0;
       }
       return "熔断降级==异常比例";
   }

   ```
2. 流控规则

   ![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/85df50837f42461195e642159247638f.png)
3. jmeter测试

   ![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/9ef7e7b16c3f42bfbfae785693c5193c.png)
4. 查看监控图

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/a85363f51201434ba61c09171f9d7341.png)

#### 6.2.3 异常数

当单位统计时长内的异常数目超过阈值之后会自动进行熔断。经过熔断时长后熔断器会进入探测恢复状态（HALF-OPEN 状态），若接下来的一个请求成功完成（没有错误）则结束熔断，否则会再次被熔断。

&#x3c;font color= "red">注意:异常降级**仅针对业务异常**，对 Sentinel 限流降级本身的异常（`BlockException`）不生效。&#x3c;/font>

1. 代码

   ```java
   //com.msb.controller.DegradationRuleController#errorCount
   @RequestMapping("/errorCount")
   public String errorCount(){
       atomicInteger.getAndIncrement();
       if (atomicInteger.get() % 2 == 0){
           //模拟异常和异常比率
           int i = 1/0;
       }
       return "熔断降级==异常数量";
   }
   ```
2. 流控规则

   ![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/6fa78a9b7e4640709e2f30526b5bbfd8.png)
3. jmeter测试

   ![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/4e0fc13c19a84b57bf4145095313481e.png)
4. 查看监控图

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/26814effe18541bda3ac597c3328d790.png)

### 6.3 热点规则

> 热点参数流控规则是一种更细粒度的流控规则, 它允许将规则具体到参数上。

何为热点？热点即经常访问的数据。很多时候我们希望统计某个热点数据中访问频次最高的 Top K 数据，并对其访问进行限制。比如：

- 商品 ID 为参数，统计一段时间内最常购买的商品 ID 并进行限制
- 用户 ID 为参数，针对一段时间内频繁访问的用户 ID 进行限制

&#x3c;font color="red">热点参数限流会统计传入参数中的热点参数，并根据配置的限流阈值与模式，对包含热点参数的资源调用进行限流。热点参数限流可以看做是一种特殊的流量控制，仅对包含热点参数的资源调用生效。&#x3c;/font>

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/e18ac1a4ffa94c4ca0ab2d5d537f5b48.png)

1. 代码

   ```java
   //http://localhost:8001/hotspot/123
   @RestController
   public class HotSpotRuleController {

       @RequestMapping("/hotspot/{id}")
       @SentinelResource(value = "hotspot",
               blockHandlerClass = CommonException.class,
               blockHandler = "handleException",
               fallbackClass = CommonException.class,
               fallback = "fallback"
       )
       public Result info(@PathVariable("id") Integer id){
           return Result.ok("成功获取数据");
       }
   }
   ```

   注意：

   1. 热点规则需要使用@SentinelResource("resourceName")注解，否则不生效
   2. 参数必须是7种基本数据类型才会生效
2. 流控规则

   注意： 资源名必须是@SentinelResource(value="资源名")中 配置的资源名，热点规则依赖于注解

   ![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/49dc3490959441179b77ac87ffbed081.png)

   这里有个坑，经过上面的配置只是对接口的限流，如果具体到参数需要再热点规则中重新设置参数

   具体到参数值限流，配置参数值为1,限流阈值为2

   ![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/8b4bd5f708714428bf165978110a384b.png)
3. jmeter测试

   ![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/4037f2d6760343b8acea0350d955aed2.png)
4. 查看监控图

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/7f82b51c2d5943edba8ba12fb17a3606.png)

### 6.4 授权规则

很多时候，我们需要根据调用来源来判断该次请求是否允许放行，这时候可以使用 Sentinel 的来源访问控制的功能。来源访问控制根据资源的请求来源（origin）限制资源是否通过：

- 若配置白名单，则只有请求来源位于白名单内时才可通过；
- 若配置黑名单，则请求来源位于黑名单时不通过，其余的请求通过。

例如：活动和订单都会调用用户系统获取用户信息，我们可以将活动设置为黑名单

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/c76a1758ffb1464ba2fecb2a6871b4f8.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/9e5aa47a371b4cdcaaf0a7807941eae3.png)

上面的【资源名】和【授权类型】不难理解，但是【流控应用】怎么填写呢？

> 其实这个位置要填写的是来源标识，Sentinel提供了RequestOriginParser 接口来处理来源。
>
> 只要Sentinel保护的接口资源被访问，Sentinel就会调用RequestOriginParser 的实现类去解析访问来源。

第1步: 自定义来源处理规则

```java
//http://localhost:8001/grant
@RestController
public class GrantController {

    @RequestMapping("/grant")
    public Result grant(){
        return Result.ok("授权规则测试成功");
    }
}
```

```java
@Component
public class RequestOriginParserDefinition implements RequestOriginParser{
    @Override
    public String parseOrigin(HttpServletRequest request) { 
        String serviceName = request.getParameter("serviceName"); 
        return serviceName;
    }
}
```

第2步: 授权规则配置

这个配置的意思是只有serviceName=order不能访问(黑名单)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/885ab01ce7bd4b58b2d4378dd9d43adb.png)

第3步: 访问 http://localhost:8001/grant?serviceName=order观察结果

#### 6.4.1在feign中将参数设置进去

1. msb-order项目中光阴如引入feign的代码可以参看Feign的文档

   ```java
   public class FeignAuthRequestInterceptor  implements RequestInterceptor {
       private String serviceName;

       public FeignAuthRequestInterceptor(String serviceName) {
           this.serviceName = serviceName;
       }
       @Override
       public void apply(RequestTemplate template) {
           template.header("serviceName",serviceName);
       }
   }
   ```

   ```java
   @Configuration
   public class FeignConfig {
       @Value("${spring.application.name}")
       private String serviceName;

       /**
        * 自定义拦截器
        * @return
        */

       @Bean
       public FeignAuthRequestInterceptor feignAuthRequestInterceptor(){
           return new FeignAuthRequestInterceptor(serviceName);
       }
   }
   ```
2. 在msb-stock项目中增加配置

```
@Component
public class RequestOriginParserDefinition implements RequestOriginParser {
    @Override
    public String parseOrigin(HttpServletRequest request) {
        String serviceName = request.getHeader("serviceName");
        return serviceName;
    }
}
```

可以对异常进行包装

```java
package com.msb.order.handle;
@Slf4j
@Component
public class CustomBlockExceptionHandler implements BlockExceptionHandler {
    @Override
    public void handle(HttpServletRequest request, HttpServletResponse response, BlockException e) throws Exception {
        log.info("BlockExceptionHandler BlockException================"+e.getRule());

        Result r = null;

        if (e instanceof FlowException) {
            r = Result.error(100,"接口限流了");

        } else if (e instanceof DegradeException) {
            r = Result.error(101,"服务降级了");

        } else if (e instanceof ParamFlowException) {
            r = Result.error(102,"热点参数限流了");

        } else if (e instanceof SystemBlockException) {
            r = Result.error(103,"触发系统保护规则了");

        } else if (e instanceof AuthorityException) {
            r = Result.error(104,"授权规则不通过");
        }
        //返回json数据
        response.setStatus(500);
        response.setCharacterEncoding("utf-8");
        response.setContentType(MediaType.APPLICATION_JSON_VALUE);
        new ObjectMapper().writeValue(response.getWriter(), r);

    }
}
```

### 6.5 系统规则

系统保护规则是从应用级别的入口流量进行控制，从单台机器的 load、CPU 使用率、平均 RT、入口 QPS 和并发线程数等几个维度监控应用指标，让系统尽可能跑在最大吞吐量的同时保证系统整体的稳定性。

系统保护规则是应用整体维度的，而不是资源维度的，并且**仅对入口流量生效**。入口流量指的是进入应用的流量（`EntryType.IN`），比如 Web 服务或 Dubbo 服务端接收的请求，都属于入口流量。

系统规则支持以下的模式：

- **Load 自适应**（仅对 Linux/Unix-like 机器生效）：系统的 load1 作为启发指标，进行自适应系统保护。当系统 load1 超过设定的启发值，且系统当前的并发线程数超过估算的系统容量时才会触发系统保护（BBR 阶段）。系统容量由系统的 `maxQps * minRt` 估算得出。设定参考值一般是 `CPU cores * 2.5`。
- **CPU usage**（1.5.0+ 版本）：当系统 CPU 使用率超过阈值即触发系统保护（取值范围 0.0-1.0），比较灵敏。
- **平均 RT**：当单台机器上所有入口流量的平均 RT 达到阈值即触发系统保护，单位是毫秒。
- **并发线程数**：当单台机器上所有入口流量的并发线程数达到阈值即触发系统保护。
- **入口 QPS**：当单台机器上所有入口流量的 QPS 达到阈值即触发系统保护。

这些不是很好测试，我们可以此时一下QPS

1. 代码

   ```java
   @RestController
   public class SystemRuleController {

       @RequestMapping("/systemRule")
       public Result systemRule(){
           return Result.ok("测试系统规则QPS");
       }
   }
   ```
2. 流控规则

   ![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/673c70045c154ceabae4313e73441500.png)
3. jmeter测试

   ![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/3a7cf926304642619d89a228c6a40bfd.png)
4. 查看监控图

   大于阈值之后进行限流

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/6bc2544f4c8c426f97dfd695f59bc6bf.png)

### 6.6 集群规则

https://github.com/alibaba/Sentinel/wiki/%E9%9B%86%E7%BE%A4%E6%B5%81%E6%8E%A7

为什么要使用集群流控呢？假设我们希望给某个用户限制调用某个 API 的总 QPS 为 50，但机器数可能很多（比如有 100 台）。这时候我们很自然地就想到，找一个 server 来专门来统计总的调用量，其它的实例都与这台 server 通信来判断是否可以调用。这就是最基础的集群流控的方式。

另外集群流控还可以解决流量不均匀导致总体限流效果不佳的问题。假设集群中有 10 台机器，我们给每台机器设置单机限流阈值为 10 QPS，理想情况下整个集群的限流阈值就为 100 QPS。不过实际情况下流量到每台机器可能会不均匀，会导致总量没有到的情况下某些机器就开始限流。因此仅靠单机维度去限制的话会无法精确地限制总体流量。而集群流控可以精确地控制整个集群的调用总量，结合单机限流兜底，可以更好地发挥流量控制的效果

部署方式

- 独立模式（Alone），即作为独立的 token server 进程启动，独立部署，隔离性好，但是需要额外的部署操作。独立模式适合作为 Global Rate Limiter 给集群提供流控服务。

  ![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/fc94c76cb99c4894830cf801ae84f489.png)
- 嵌入模式（Embedded），即作为内置的 token server 与服务在同一进程中启动。在此模式下，集群中各个实例都是对等的，token server 和 client 可以随时进行转变，因此无需单独部署，灵活性比较好。但是隔离性不佳，需要限制 token server 的总 QPS，防止影响应用本身。嵌入模式适合某个应用集群内部的流控。

  ![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/31bcbad172004c9baaeab683f74e6187.png)

## 4.8 Sentinel规则持久化

| 推送模式 | 说明                                                                                                                                                                                                          | 优点                         | 缺点                                                         |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- | ------------------------------------------------------------ |
| 原始模式 | API将规则推送至客户端并直接更新到内存中，扩展写数据源                                                                                                                                                         | 简单、无任何依赖             | 不保证一致性;规则保存在内存中，重启不建议用于生产环境        |
| PULL模式 | 客户端主动向某个规则管理中心定期轮询拉取规则，&#x3c;br />这个规则中心可以是 RDBMS.文件等                                                                                                                      | 简单、无任何依赖；规则持久化 | 不保证一致性；实时性不保证，拉取过于频繁，也可能会有性能问题 |
| PUSH模式 | 规则中心统一推送，客户端通过注册监听&#x3c;br />方式有更好的实时性和一致性保证。生产Nacos&#x3c;br />、Zookeeper等配置中心。这种方式有更好的实时性和一致性保证。&#x3c;br />生产环境下一般采用push模式的数据源。 | 规则持久化；一致性；快速     | 引入第三方依赖                                               |

### 4.8.1 原始模式

如果不做任何修改，Dashboard 的推送规则方式是通过 API 将规则推送至客户端并直接更新到内存中：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/6641247ea94d4b7fbfd85e66d47443ab.png)

### 4.8.2Pull模式

pull 模式的数据源（如本地文件、RDBMS 等）一般是可写入的。使用时需要在客户端注册数据源：将对应的读数据源注册至对应的 RuleManager，将写数据源注册至 transport 的 `WritableDataSourceRegistry` 中。以本地文件数据源为例：****

&#x3c;font color="red">本地文件数据源会定时轮询文件的变更，读取规则。&#x3c;/font>这样我们既可以在应用本地直接修改文件来更新规则，也可以通过 Sentinel 控制台推送规则。以本地文件数据源为例，推送过程如下图所示：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/a9fc56d256f24d5aa0f8e86c21cf9f16.png)

大家可以发现整个过程比较繁重，并且每次都需要更新本地文件，他的性能有一定的影响

### 4.8.3 Push模式

生产环境下一般更常用的是 push 模式的数据源。对于 push 模式的数据源,如远程配置中心（ZooKeeper, Nacos, Apollo等等），我们在sentinel Dashboard配置的规则会同步到Nacos中， Sentinel Dashboard也会从Nacos中获取规则，Nacos会讲规则推送给Sentinel客户端

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/de078d9cefce4bc68afca77a4edf8148.png)

1. 复制测试代码

   在sentinel-dashboard中的测试包中会有对阿波罗，nacos和zk的支持

   ![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/477077fb2510416ebc963a90039fc058.png)

   对nacos进行复制，copy到rule规则下

   ![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/7729aa2fc5a9476e8466df0519b3ca5a.png)

   我们会发现对应的类会报红，这是应为对应的sentinel包，没有引入进去

   ![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/c15cd106da94491c882d929f4bc55de2.png)

   我们进入对应的pom会发现里面有不对应的sentinel包，只是scope设置的是test，我们需要去掉范围就可以

   ![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/e3b9297919d6431bb81710a4b5d50c16.png)
2. 修改代码改造我们nacos注册地址

   改造对应的NacosConfig文件

   ![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/21d37844989f4015b3836493758b342d.png)
3. 更改注入的类

   ![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/b090ed1b34d04bbb9ac08570093d8591.png)

   ![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/73436d25c4fc4035815034178d8e23d4.png)

   ![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/7d5ca116a4f6442e913231b0e27f239b.png)

   这里就是相当于，他对规则的所有操作就是走我们nacos的操作。
4. 改造页面新增菜单

   app\scripts\directives\sidebar\sidebar.html

   ![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/12acb74b86984d00938c64bf59188211.png)
5. 启动dashboard

   如果启动后没有发现"流控规则 nacos" ，那我们可以使用无痕模式

   ![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/47d73d73226a49a2ae84ed5ffcbdddfb.png)

   此时我们增加一个流控规则

   ![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/3a314e6673304b1eb88f4fa8b98187c4.png)

   此时我们查看nacos就会发现里面已经同步了我们增加的流控规则，此时我们可以在nacos修改规则，也可以在sentinel修改规则

   ![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/cf70f309be5440109183ad36c076a707.png)
6. 更改客户端

   - 增加依赖

     ```pom
     dependency>
         <groupId>com.alibaba.csp</groupId>
         <artifactId>sentinel-datasource-nacos</artifactId>
     </dependency>
     ```
   - 添加配置

     ```yaml
     spring:
       cloud:
         sentinel:
           datasource:
             # 名称随意
             flow:
               nacos:
                 server-addr: localhost:8848
                 dataId: ${spring.application.name}-flow-rules
                 groupId: SENTINEL_GROUP
                 # 规则类型，取值见：
                 # org.springframework.cloud.alibaba.sentinel.datasource.RuleType
                 rule-type: flow
             degrade:
               nacos:
                 server-addr: localhost:8848
                 dataId: ${spring.application.name}-degrade-rules
                 groupId: SENTINEL_GROUP
                 rule-type: degrade
             system:
               nacos:
                 server-addr: localhost:8848
                 dataId: ${spring.application.name}-system-rules
                 groupId: SENTINEL_GROUP
                 rule-type: system
             authority:
               nacos:
                 server-addr: localhost:8848
                 dataId: ${spring.application.name}-authority-rules
                 groupId: SENTINEL_GROUP
                 rule-type: authority
             param-flow:
               nacos:
                 server-addr: localhost:8848
                 dataId: ${spring.application.name}-param-flow-rules
                 groupId: SENTINEL_GROUP
                 rule-type: param-flow
     ```

## 4.9  RestTemplate整合Sentinel

1. 引入restTemplate

   ```java
   @EnableDiscoveryClient
   @SpringBootApplication
   @EnableFeignClients
   public class OrderApplication {

       @Bean
       @LoadBalanced
       @SentinelRestTemplate
       public RestTemplate restTemplate(){
           return new RestTemplate();
       }

       public static void main(String[] args) {
           SpringApplication.run(OrderApplication.class);
       }
   }

   ```

   ```java
   package com.msb.controller;

   import com.msb.util.Result;
   import org.springframework.beans.factory.annotation.Autowired;
   import org.springframework.web.bind.annotation.PathVariable;
   import org.springframework.web.bind.annotation.RequestMapping;
   import org.springframework.web.bind.annotation.RestController;
   import org.springframework.web.client.RestTemplate;

   @RestController
   public class RestTemplateController {
       @Autowired
       private RestTemplate restTemplate;

       @RequestMapping("/testRestTemplate/{userId}")
       public String getUser(@PathVariable Integer userId){
           String result = restTemplate.getForObject("http://msb-user:10001/user/" + userId, String.class);
           return result;
       }
   }
   ```
2. 流控规则

   ![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/b1fc89343d1940e5915c428821df0892.png)
3. 测试

   http://localhost:8001/testRestTemplate/222

   ![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/9655aa622efd42a1b5c5731c7fa45dc6.png)
4. 异常丑陋的更改

   重写这些方法

   ![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/a97482e23822429b942b0e1038c00ca6.png)

   ```java
   @EnableDiscoveryClient
   @SpringBootApplication
   @EnableFeignClients
   public class OrderApplication {

       @Bean
       @LoadBalanced
       @SentinelRestTemplate(blockHandler = "handleException",blockHandlerClass= GlobalException.class
       ,fallback = "fallback",fallbackClass = GlobalException.class)
       public RestTemplate restTemplate(){
           return new RestTemplate();
       }

       public static void main(String[] args) {
           SpringApplication.run(OrderApplication.class);
       }


   }
   ```

   ```java
   package com.msb.exception;

   import com.alibaba.cloud.sentinel.rest.SentinelClientHttpResponse;
   import com.alibaba.csp.sentinel.slots.block.BlockException;
   import com.fasterxml.jackson.core.JsonProcessingException;
   import com.fasterxml.jackson.databind.ObjectMapper;
   import org.springframework.http.HttpRequest;
   import com.msb.util.Result;
   import org.springframework.http.client.ClientHttpRequestExecution;

   public class GlobalException {

       public static SentinelClientHttpResponse handleException(HttpRequest request,
                                                                byte[] body, ClientHttpRequestExecution execution, BlockException ex) {
           Result r = Result.error(-1, "===被限流啦===");
           try {
               return new SentinelClientHttpResponse(new ObjectMapper().writeValueAsString(r));
           } catch (JsonProcessingException e) {
               e.printStackTrace();
           }
           return null;
       }

       public static SentinelClientHttpResponse fallback(HttpRequest request,
                                                         byte[] body, ClientHttpRequestExecution execution, BlockException ex) {
           Result r = Result.error(-2, "===被异常降级啦===");
           try {
               return new SentinelClientHttpResponse(new ObjectMapper().writeValueAsString(r));
           } catch (JsonProcessingException e) {
               e.printStackTrace();
           }
           return null;
       }
   }
   ```
5. 源码分析

   我们想我们ribbon是怎样restTemplate ，以前是不是通过类LoadBalancerInterceptor 来进行整合的，那我们的sentinel是不是也可是通过拦截器来进行整合的

   ```

   ```

   ![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/df59da91aa8a40e0a8a27ecdedfac5e1.png)

   在这里进行拦截的。

   ![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/dd784b3cccaa4037af229646ce4f5e79.png)

## 4.10 Feign整合Sentinel

1. 4.9 Feign整合Sentinel

   1. 引入sentinel的依赖

      ```java
      <!--sentinel客户端-->
      <dependency>
          <groupId>com.alibaba.cloud</groupId>
          <artifactId>spring-cloud-starter-alibaba-sentinel</artifactId>
      </dependency>
       <!-- openfeign 远程调用 -->
      <dependency>
          <groupId>org.springframework.cloud</groupId>
          <artifactId>spring-cloud-starter-openfeign</artifactId>
      </dependency>
      ```
   2. 在配置文件中开启Feign对Sentinel的支持

      ```pom
      feign:
      	sentinel: 
      		enabled: true
      ```
   3. 创建限流处理类

      ```java
      @Component
      public class FallbackOrderFeignServiceFactory implements FallbackFactory<UserFeignService> {
          @Override
          public UserFeignService create(Throwable throwable) {
              return new UserFeignService() {
                  @Override
                  public String getUserName(Integer userId) {
                      if (throwable instanceof FlowException) {
                          return Result.error(100,"接口限流了");
                      }

                      return Result.error(-1,"=======服务降级了========");
                  }
              };
          }
      }

      ```
   4. 为被容错的接口指定容错类

      ```java
      //value用于指定调用nacos下哪个微服务
      //fallbackFactory指定限流处理类
      @FeignClient(value = "msb-user",fallbackFactory = FallbackOrderFeignServiceFactory.class)
      public interface UserFeignService {
          @GetMapping("/user/{userId}")
          Result getUserName(@PathVariable Integer userId);
      }

      ```
   5. 修改controller

      ```java
      @RestController
      public class FeignOrderController {

          @Autowired
          private UserFeignService userFeignService;

          @RequestMapping("/getOrders/{userId}")
          public Result getOrders(@PathVariable("userId") Integer userId){
              Result resultUserInfo = userFeignService.getUserName(userId);
              /**
               * 处理其它业务
               */
              return resultUserInfo;
          }
      }
      ```
   6. 修改UserController

      ```java
      @RestController
      public class UserController {

          @GetMapping("/user/{userId}")
          public Result getUserName(@PathVariable Integer userId){
              return Result.ok("善缘老师");
          }
      }
      ```
   7. 修改流控规则

      ![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/d654b487b3cb4786b9b40e9dfe4045c6.png)
   8. 进行调用

      http://localhost:8001/getOrders/213
   9. 流控效果

      ![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/03f9f13d529e466cbb15326f04ab4591.png)

# 四、限流算法

### 1、计数器固定窗口算法

计数器固定窗口算法是最简单的限流算法，实现方式也比较简单。就是通过维护一个单位时间内的计数值，每当一个请求通过时，就将计数值加1，当计数值超过预先设定的阈值时，就拒绝单位时间内的其他请求。如果单位时间已经结束，则将计数器清零，开启下一轮的计数。

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/78d15964da2140318743f005bc60e468.png)

```java
package com.msb.sentinel;
import com.msb.sentinel.exception.BlockException;
import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.AtomicInteger;
public class CounterRateLimit implements RateLimit , Runnable {

    /**
     * 阈值
     */
    private Integer limitCount;

    /**
     * 当前通过请求数
     */
    private AtomicInteger passCount;

    /**
     * 统计时间间隔
     */
    private long period;
    private TimeUnit timeUnit;

    private ScheduledExecutorService scheduledExecutorService;


    public CounterRateLimit(Integer limitCount) {
        this(limitCount, 1000, TimeUnit.MILLISECONDS);
    }

    public CounterRateLimit(Integer limitCount, long period, TimeUnit timeUnit) {
        this.limitCount = limitCount;
        this.period = period;
        this.timeUnit = timeUnit;
        passCount = new AtomicInteger(0);
        this.startResetTask();
    }

    @Override
    public boolean canPass() throws BlockException {
        if (passCount.incrementAndGet() > limitCount) {
            throw new BlockException();
        }
        return true;
    }

    //启动一定定时任务线程，每过一个周期就将我们通过个数重置为0
    private void startResetTask() {
        scheduledExecutorService = Executors.newSingleThreadScheduledExecutor();
        scheduledExecutorService.scheduleAtFixedRate(this, 0, period, timeUnit);
    }

    @Override
    public void run() {
        passCount.set(0);
    }
}

```

但是这种实现会有一个问题，举个例子:

> 假设我们设定1秒内允许通过的请求阈值是99，如果有用户在时间窗口的最后几毫秒发送了99个请求，紧接着又在下一个时间窗口开始时发送了200个请求，那么这个用户其实在一秒内成功请求了198次，显然超过了阈值但并不会被限流。其实这就是临界值问题，那么临界值问题要怎么解决呢？

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/c0bb7b508bfc4514a7dcff7502cf9133.png)

### 2、计数器滑动窗口算法

[算法演示](https://media.pearsoncmg.com/aw/ecs_kurose_compnetwork_7/cw/content/interactiveanimations/selective-repeat-protocol/index.html)

计数器滑动窗口法就是为了解决上述固定窗口计数存在的问题而诞生。前面说了固定窗口存在临界值问题，要解决这种临界值问题，显然只用一个窗口是解决不了问题的。假设我们仍然设定1秒内允许通过的请求是200个，但是在这里我们需要把1秒的时间分成多格，假设分成5格（格数越多，流量过渡越平滑），每格窗口的时间大小是200毫秒，每过200毫秒，就将窗口向前移动一格。为了便于理解，可以看下图

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/271f7b21287f4ccebbbb5503e1998bf9.png)

图中将窗口划为5份，每个小窗口中的数字表示在这个窗口中请求数，所以通过观察上图，可知在当前时间快（200毫秒）允许通过的请求数应该是70而不是200（只要超过70就会被限流），因为我们最终统计请求数时是需要把当前窗口的值进行累加，进而得到当前请求数来判断是不是需要进行限流。

那么滑动窗口限流法是完美的吗？

细心观察的我们应该能马上发现问题，*滑动窗口限流法其实就是计数器固定窗口算法的一个变种*。流量的过渡是否平滑依赖于我们设置的窗口格数也就是统计时间间隔，格数越多，统计越精确，但是具体要分多少格我们也说不上来呀...

```java
package com.msb.sentinel;

import com.msb.sentinel.exception.BlockException;
import lombok.Data;
import lombok.extern.slf4j.Slf4j;

import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;
@Slf4j
public class SlidingWindowRateLimit implements RateLimit, Runnable {

  
    /**
     * 阈值
     */
    private Integer limitCount;

    /**
     * 当前通过的请求数
     */
    private AtomicInteger passCount;

    /**
     * 窗口数
     */
    private Integer windowSize;

    /**
     * 每个窗口时间间隔大小
     */
    private long windowPeriod;
    private TimeUnit timeUnit;


    private Window[] windows;
    private volatile Integer windowIndex = 0;

    private Lock lock = new ReentrantLock();
    public SlidingWindowRateLimit(Integer limitCount) {
        // 默认统计qps, 窗口大小5
        this(limitCount, 5, 200, TimeUnit.MILLISECONDS);
    }

    /**
     * 统计总时间 = windowSize * windowPeriod
     */
    public SlidingWindowRateLimit(Integer limitCount, Integer windowSize, Integer windowPeriod, TimeUnit timeUnit) {
        this.limitCount = limitCount;
        this.windowSize = windowSize;
        this.windowPeriod = windowPeriod;
        this.timeUnit = timeUnit;
        this.passCount = new AtomicInteger(0);
        this.initWindows(windowSize);
        this.startResetTask();
    }

    @Override
    public boolean canPass() throws BlockException {
        lock.lock();
        if (passCount.get() > limitCount) {
            throw new BlockException();
        }
        windows[windowIndex].passCount.incrementAndGet();
        passCount.incrementAndGet();
        lock.unlock();
        return true;
    }

    private void initWindows(Integer windowSize) {
        windows = new Window[windowSize];
        for (int i = 0; i < windowSize; i++) {
            windows[i] = new Window();
        }
    }

    private ScheduledExecutorService scheduledExecutorService;
    private void startResetTask() {
        scheduledExecutorService = Executors.newSingleThreadScheduledExecutor();
        scheduledExecutorService.scheduleAtFixedRate(this, windowPeriod, windowPeriod, timeUnit);
    }

    @Override
    public void run() {
        // 获取当前窗口索引
        Integer curIndex = (windowIndex + 1) % windowSize;
        // 重置当前窗口索引通过数量，并获取上一次通过数量
        Integer count = windows[curIndex].passCount.getAndSet(0);
        windowIndex = curIndex;
        // 总通过数量 减去 当前窗口上次通过数量
        passCount.addAndGet(-count);
    }

    @Data
    class Window {
        private AtomicInteger passCount;
        public Window() {
            this.passCount = new AtomicInteger(0);
        }
    }
}
```

### 3、漏桶算法

上面所介绍的两种算法都不能非常平滑的过渡，下面就是漏桶算法登场了

什么是漏桶算法？

漏桶算法以一个常量限制了出口流量速率，因此漏桶算法可以平滑突发的流量。其中漏桶作为流量容器我们可以看做一个FIFO的队列，当入口流量速率大于出口流量速率时，因为流量容器是有限的，当超出流量容器大小时，超出的流量会被丢弃。

下图比较形象的说明了漏桶算法的原理，其中水龙头是入口流量，漏桶是流量容器，匀速流出的水是出口流量。

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/b7c04426a3fa4b7ebaf9ca3bd8cd68a9.png)

漏桶算法的特点

- 漏桶具有固定容量，出口流量速率是固定常量（流出请求）
- 入口流量可以以任意速率流入到漏桶中（流入请求）
- 如果入口流量超出了桶的容量，则流入流量会溢出（新请求被拒绝）

```java
package com.msb.sentinel;

import com.msb.sentinel.exception.BlockException;
import lombok.extern.slf4j.Slf4j;


import javax.swing.*;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Objects;
import java.util.concurrent.*;
import java.util.concurrent.locks.LockSupport;

public class LeakyBucketRateLimit implements RateLimit, Runnable {

    /**
     * 出口限制qps
     */
    private Integer limitSecond;
    /**
     * 漏桶队列
     */
    private BlockingQueue<Thread> leakyBucket;

    private ScheduledExecutorService scheduledExecutorService;

    public LeakyBucketRateLimit(Integer bucketSize, Integer limitSecond) {
        this.limitSecond = limitSecond;
        this.leakyBucket = new LinkedBlockingDeque<>(bucketSize);

        scheduledExecutorService = Executors.newSingleThreadScheduledExecutor();
        //1 秒=1000000000 纳秒
        // 计算出一个请求需要多少纳秒
        long interval = (1000 * 1000 * 1000) / limitSecond;
        scheduledExecutorService.scheduleAtFixedRate(this, 0, interval, TimeUnit.NANOSECONDS);
    }

    @Override
    public boolean canPass() throws BlockException {
        if (leakyBucket.remainingCapacity() == 0) {
            throw new BlockException();
        }
        //如果立即可行且不违反容量限制，则将指定的元素插入此双端队列表示的队列中（即此双端队列的尾部），
        // 并在成功时返回 true；如果当前没有空间可用，则返回 false。
        leakyBucket.offer(Thread.currentThread());
        //所有请求进来，只要有容量，就会停止到这里
        // 如果没有容量，就停止在上行代码
        LockSupport.park();
        return true;
    }

    @Override
    public void run() {
        // 以固定的速率去唤醒他，这样执行的速度就固定值
        Thread thread = leakyBucket.poll();
        if (Objects.nonNull(thread)) {
            LockSupport.unpark(thread);
        }
    }
}
```

*不过因为漏桶算法限制了流出速率是一个固定常量值，所以漏桶算法不支持出现突发流出流量。但是在实际情况下，流量往往是突发的。*

### 4、令牌桶算法

令牌桶算法是漏桶算法的改进版，可以支持突发流量。不过与漏桶算法不同的是，令牌桶算法的漏桶中存放的是令牌而不是流量。

那么令牌桶算法是怎么突发流量的呢？

最开始，令牌桶是空的，我们以恒定速率往令牌桶里加入令牌，令牌桶被装满时，多余的令牌会被丢弃。当请求到来时，会先尝试从令牌桶获取令牌（相当于从令牌桶移除一个令牌），获取成功则请求被放行，获取失败则阻塞活拒绝请求。

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/15647/1661428591016/0bd0d23c3d954720be0e6b55260fd0d1.png)

令牌桶算法的特点

- 最多可以存发b个令牌。如果令牌到达时令牌桶已经满了，那么这个令牌会被丢弃
- 每当一个请求过来时，就会尝试从桶里移除一个令牌，如果没有令牌的话，请求无法通过。

*令牌桶算法限制的是平均流量，因此其允许突发流量（只要令牌桶中有令牌，就不会被限流）*

```java
package com.msb.sentinel;

import com.msb.sentinel.exception.BlockException;
import org.apache.commons.lang3.StringUtils;

import java.util.concurrent.*;

public class TokenBucketRateLimit implements RateLimit, Runnable {

    /**
     * token 生成 速率 （每秒）
     */
    private Integer tokenLimitSecond;

    /**
     * 令牌桶队列
     */
    private BlockingQueue<String /* token */> tokenBucket;

    private static final String TOKEN = "__token__";

    private ScheduledExecutorService scheduledExecutorService;

    public TokenBucketRateLimit(Integer bucketSize, Integer tokenLimitSecond) {
        this.tokenLimitSecond = tokenLimitSecond;
        this.tokenBucket = new LinkedBlockingDeque<>(bucketSize);

        scheduledExecutorService = Executors.newSingleThreadScheduledExecutor();
        long interval = (1000 * 1000 * 1000) / tokenLimitSecond;
        scheduledExecutorService.scheduleAtFixedRate(this, 0, interval, TimeUnit.NANOSECONDS);
    }

    @Override
    public boolean canPass() throws BlockException {
        String token = tokenBucket.poll();
        if (StringUtils.isEmpty(token)) {
            throw new BlockException();
        }
        return true;
    }

    @Override
    public void run() {
        if (tokenBucket.remainingCapacity() == 0) {
            return;
        }
        tokenBucket.offer(TOKEN);
    }
}
```
