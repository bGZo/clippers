---
title: "IT速成之JAVA速成班-五小时搞懂-Spring-Cloud"
cover: "http://i0.hdslb.com/bfs/archive/76644bb61423d9b489c1b1ccba233ae5e0a67618.jpg@189w_107h.webp"
author: "乐学教程"
created: 2025-01-14T22:27:55
modified: 2025-01-19T02:57:07
published: 2025-01-14T22:27:51
description: "IT速成之JAVA速成班 五小时搞懂 Spring Cloud共计14条视频，包括：开篇词：服务治理为何选择Spring Cloud (2)、第01讲：夯实基础-Spring Boot、第02讲：服务治理-Eureka (2)等，UP主更多精彩视频，请关注UP账号。"
source: "https://www.bilibili.com/video/BV13a411e7h5/?*p*=1"
tags:
  - "bilibili"
type: "video"
---

## Source

<iframe src='https://player.bilibili.com/player.html?isOutside=true&bvid=BV13a411e7h5&p=1&autoplay=false' style='height:40vh;width:100%' class='iframe-radius' allow='fullscreen'></iframe>
<center>via: <a href='https://www.bilibili.com/video/BV13a411e7h5?*p*=1' target='_blank' class='external-link'>https://www.bilibili.com/video/BV13a411e7h5?*p*=1</a></center>

## Notes

alias:: IT 速成之 JAVA 速成班 五小时搞懂 Spring Cloud

tags:: #spring-cloud

created: 2023-02-22

## [开篇词：服务治理为何选择Spring Cloud (2)](https://www.bilibili.com/video/BV13a411e7h5?*p*=1)
## [第01讲：夯实基础-Spring Boot_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV13a411e7h5/?p=2)
- Spring Boot Highlight
- 自动装配
- Starter 包简化 Maven 配置
- 内嵌容器
- 应用监控
- 创建方式
- 先创建一个 Maven 项目，然后手动往这个 Maven 项目中添加 Spring Boot 需要的依赖；
- 通过官方脚手架页面创建 Spring Boot 项目
- 读取配置文件的 3 种方式
- `Environment env;`
- `env.getProperty("spring.profiles.active")`
- `@Value("${server.port}")`
- `@ConfigurationProperties(prefix="spring")`（集中管理，集中注入一个类）
- 自定义 Starter 的
- 创建 Starter 项目
- 定义 Starter 需要的配置（Properties）
- 编写自动配置类
- **编写 spring.factories 文件加载自动配置类**
- 指定自动配置时需要扫描的类；
- 或者用 `@interface` 和 `@Import` 达到相同效果；
- 或者用 `ConditionalOnProperty(prefix="spring.user", value="enable", havingValue="true")` 来定义什么时候进行自动装配；
- 编写配置提示文件 spring-configuration-metadata.json（不是必须的）
- 使用项目中引入依赖，增加配置即可使用
- Spring Boot 监控
- 自己编写接口
- `Spring-boot-starter-actuator` 主动监控
- `localhost:8082/actuator/health`

```java
@Component
public class CustomHealthIndicator extends AbstractHealthIndicator {
  @Override
  protected void doHealthCheck(Health.Builder builder) throws Exception {
    builder.up().withDetail("fcustomInfo", "自定义信息");
}
```

- 服务的 4 种状态
- `UP`
- `DOWN`
- `UNKNOWN`
- `OUT_OF_SERVICE`

- ---

- So spring boot considers DOWN more "severe" than OUT_OF_SERVICE. By default both map to HTTP 503 Service Unavailable for the /health endpoint. So really out of the box if you use either you will see the same behavior. None of the spring provided health indicators use OUT_OF_SERVICE. They just use DOWN.
  via: [OUT_OF_SERVICE VS DOWN health status (Spring Boot) - Stack Overflow](https://stackoverflow.com/questions/29924786/out-of-service-vs-down-health-status-spring-boot)
- 自定义端点

```java
  @Component
  @Endpoint(id ="springcloud")
  public class SpringCloudEndPoint{
    @ReadOperation
    public Map<String, Object> showData() {
      Map<String, Object> data = new HashMap<String,Object>();
      data.put("title", "springcloud");
      return data;
  }
```

- Spring Boot Admin
- 一个开源的 Web 项目，用于管理和监控 Spring Boot 应用程序的运行状态
- 作用
- 显示应用程序的监控状态
- 应用程序上下线监控
- 查看 JVM，线程信息
- 可视化的查看日志以及下载日志文件
- 动态切换日志级别
- HTTP 请求信息跟踪
- POM 依赖以及 `application.properties` 配置文件；
- 功能点
- 替换内置 Tomcat 容器
- 启动监听
- Filter 注册

## [第02讲：服务治理-Eureka (2)](https://www.bilibili.com/video/BV13a411e7h5?*p*=3)
- 注册中心
description:: 服务在启动的时候将自身的信息注册到注册中心，方便进行统一管理；
- 服务注册
description:: 客户端向注册中心提交信息；
- 服务发现
description:: 从注册中心获取对应服务的信息；服务发现是客户端向注册中心获取信息
- 其他动作
- 注册中心（集中存储管理服务信息）
- 服务提供者（API 需要给其他方调用）
- 服务消费者（需要调用其他方的 API）
- **注册**（告诉注册中心自身的信息）
- **拉取**（拉取对应服务的信息，发起调用）
- **心跳**（健康汇报，一定时间内无心跳注册中心会**剔除**服务信息）
- 解决了什么问题？
- 硬编码问题
- 接口地址： http://192.168.10.11:8081/blog/user/1
- 解决
- Nginx + Domain 可以解决故障问题
  - 需要手动维护可用节点列表
- IP 地址变了怎么办？节点增加减少了怎么办？
- 域名方式： http://cxytiandi.com/blog/user/1
- 服务数量成百上千，维护上千个域名？
- 注册中心获取服务信息，发起调用
- Eureka
- Netflix Eureka
decs:: 基于 REST 服务，提供服务发现功能
- Spring Cloud Eureka
description:: 是 Spring Cloud Netflix 微服务套件 的一部分，基于 Netflix Eureka 做 了二次封装，主要负责完成微服务架构中的服务治理功能；是一个基于 REST 的服务，并且提供了基于 Java 的客户端组件，能够非常方便的将服务注册到 Spring Cloud Eureka 中进行统一管理；
- ![chrome_308.png](../assets/chrome_308_1677053666121_0.png)
- Eureka 自我保护机制
description:: 自我保护机制是为了避免因网络分区故障导致服务不可用的问题
- ![chrome_309.png](../assets/chrome_309_1677054740861_0.png)
![chrome_310.png](../assets/chrome_310_1677054813358_0.png)
- 服务注册与服务发现相关动作
服务注册与服务发现解决的问题
服务治理 -Eureka

## [第03讲：客户端负载均衡-Ribbon (2)](https://www.bilibili.com/video/BV13a411e7h5?*p*=4)
- 负载均衡
- 随着用户量的增加，应用访问量也会随之增加，单台服务器已经不能满足高并发的业务需求
- **多台服务器组成集群**来应对高并发带来的业务的压力；
- **负均衡器**来对流量进行合理分配
- 目前主流的负载方案
- 一种是集中式负载均衡，在消费者和服务提供方中间使用独立的代理方式进行负载，有硬件的，比如 F5，也有软件的，如 Nginx
- 另一种则是客户端自己做负载均衡，根据自己的请求情况做负载，Ribbon 就是属于客户端自己做负载的框架
- 集中式负载均衡
- ![chrome_355.png](../assets/chrome_355_1679371658522_0.png)
- 客户端负载均衡
- ![chrome_356.png](../assets/chrome_356_1679371788888_0.png)
- Ribbon
- Ribbon
description:: by Netflix；有助于控制 HTTP 和 TCP 的客户端的行为
为 Ribbon 配置服务提供者地址后，Ribbon 就可基于某种负载均衡算法，自动地帮助服务消费者去请求
Ribbon 默认为我们提供了很多负载均衡算法，例如轮询、随机等
- 负载均衡策略
- 饥饿加载模式

## [第04讲：服务容错保护-Hytrix (2)](https://www.bilibili.com/video/BV13a411e7h5?*p*=5)
## [第05讲：声明式服务调用-Feign (2)](https://www.bilibili.com/video/BV13a411e7h5?*p*=6)
## [第06讲：API网关服务-Zuul (2)](https://www.bilibili.com/video/BV13a411e7h5?*p*=7)
## [第07讲：分布式配置中心-Apollo (2)](https://www.bilibili.com/video/BV13a411e7h5?*p*=8)
## [第08讲：分布式链路跟踪 (2)](https://www.bilibili.com/video/BV13a411e7h5?*p*=9)
## [第09讲：微服务安全认证 (2)](https://www.bilibili.com/video/BV13a411e7h5?*p*=10)
## [第10讲：灰度发布实战 (2)](https://www.bilibili.com/video/BV13a411e7h5?*p*=11)
## [第11讲：Spring Cloud常见问题及解决方案 (2)](https://www.bilibili.com/video/BV13a411e7h5?*p*=12)
## [第12讲：Spring Cloud综合案例 (2)](https://www.bilibili.com/video/BV13a411e7h5?*p*=13)
## [彩蛋：第二代微服务架构Spring Cloud Alibaba (2)](https://www.bilibili.com/video/BV13a411e7h5?*p*=14)
-
