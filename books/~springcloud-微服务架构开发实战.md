---
aliases:
  - books/Spring Cloud 微服务架构开发实战
tags: 
author: 董超
publisher: 机械工业出版社
published: 20180700
isbn: 9787111604525
created: 2022-12-28
douban: https://book.douban.com/subject/30389992
weread: https://weread.qq.com/web/bookDetail/7d332ce0715dbcba7d3a09d
description: https://github.com/cd826/springcloud-demo
title: springcloud 微服务架构开发实战
---

- Content
  - 版权信息
  - 内容简介
  - 前言
  - 第1篇 微服务开发基础——Spring Boot框架及使用
    - 第1章 微服务架构开发
      - 1.1 单体架构应用的困境
      - 1.2 微服务架构
      - 1.3 微服务架构设计
      - 1.4 不应使用微服务架构的情形
    - 第2章 微服务基础——Spring Boot
      - 2.1 Spring与Spring Boot
        - Spring框架具有以下优点
          - Spring的**依赖反转功能**让我们可以开发出**方便进行测试的代码**
          - 提供了易用、灵活、强大的数据事务管理支持功能
          - Spring强大的开放基因，使得其可以和众多框架，如**JPA/Hibernate、JSF、Kafka、RabbitMQ、Thymeleaf**等整合，都可以轻易地整合到应用开发中
          - 提供了标准化的Web应用开发支持Spring MVC
        - Spring框架提供了如下功能和子系统：
          - Spring Data；
          - Spring MVC；
          - Spring Security；
          - Spring Session；
          - Spring Cloud；
        - Spring框架的高度灵活性和配置的多样性，使开发者在使用之初的学习难度曲线陡增，使用习惯之后又不得不面对在每个项目中几乎重复实现各项配置
          - 如DataSource、EntityManage、MessageSource、ViewResolver等
            - 一不小心还会出错，查找半天才知道是因为某个配置错误造成的
        - Spring Boot通过提供一系列名称以spring-boot-starter开头的启动器(Starters)帮助我们简化项目的依赖
          - 比如，当我们在项目中添加了spring-boot-starter-web时，Spring Boot就自动将相关依赖，如spring-mvc、jackson-json、tomcat等引入，从而将项目变成一个Web项目
          - [Spring Boot Reference Documentation](https://docs.spring.io/spring-boot/docs/current/reference/htmlsingle/#using.build-systems.starters) via: 全部启动器列表
            - >  For example, with the appropriate Eclipse or Spring Tools plugin installed, you can press ctrl-space in the POM editor and type “spring-boot-starter” for a complete list.
            - under the  `org.springframework.boot`  group:
              - *Spring Boot application starters*
              - *Spring Boot production starters*
              - *Spring Boot technical starters*
          - 在开发时我们常用的启动器有以下几个
            - spring-boot-starter-web, Web应用开发。
            - spring-boot-starter-logging，日志处理；
            - spring-boot-starter-jpa，数据存储管理；
            - spring-boot-starter-security，安全管理；
            - spring-boot-starter-actuator，应用监控；
            - spring-boot-srarter-data-redis, Redis数据库集成；
            - spring-boot-starter-amqp，消息中间件集成。
      - 2.2 快速启动Spring Boot
        - [cd826/springcloud-demo: Spring cloud demo projects](https://github.com/cd826/springcloud-demo)
        - [Spring Boot初始化工具](https://start.spring.io/)
```xml
            <? xml version="1.0" encoding="UTF-8"? >
            <project xmlns="http://maven.apache.org/POM/4.0.0"
                xmlns:xsi=http://www.w3.org/2001/XMLSchema-instance
                xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
            http://maven.apache.org/maven-v4_0_0.xsd">
                <modelVersion>4.0.0</modelVersion>
                <! -- 这里将项目的父项目设置为Spring Boot，所使用版本为1.5.2.RELEASE -->
                <parent>
                    <groupId>org.springframework.boot</groupId>
                    <artifactId>spring-boot-starter-parent</artifactId>
                    <version>1.5.2.RELEASE</version>
                </parent>
                <! -- 这里设置本项目的groupId、artifactId和版本等信息 -->
                <groupId>cd826dong.cloud</groupId>
                <artifactId>cd826dong-clouds-boot</artifactId>
                <version>0.0.1-SNAPSHOT</version>
                <packaging>jar</packaging>
            <name>SpringCloud Demo Projects -- Spring Boot</name>
            <properties>
                <! -- 定义项目所使用的编码为UTF-8 -->
                <project.build.sourceEncoding>UTF-8</project.build.source
                Encoding>
                <! -- 项目所用JDK 1.8，也可以使用低版本，但建议还是使用JDK 1.8以上版本-->
                <java.version>1.8</java.version>
                <maven.compiler.source>${java.version}</maven.compiler.source>
                <maven.compiler.target>${java.version}</maven.compiler.target>
                <! -- 项目所使用第三方包的版本，建议以后都采用这种方式，统一在一个地方声明
                版本号，这样对项目可以进行统一管理，方便以后升级 -->
                <guava.version>20.0</guava.version>
                <swagger.version>2.6.1</swagger.version>
            </properties>
            <dependencies>
                <! -- 项目所用Spring Boot starters:web -->
                <dependency>
                    <groupId>org.springframework.boot</groupId>
                    <artifactId>spring-boot-starter-web</artifactId>
                </dependency>
                <! -- Guava可以为我们提供缓存、集合等一些方便的工具类 -->
                <dependency>
                    <groupId>com.google.guava</groupId>
                    <artifactId>guava</artifactId>
                    <version>${guava.version}</version>
                </dependency>
                <! -- test -->
                <dependency>
                    <groupId>org.springframework.boot</groupId>
                    <artifactId>spring-boot-starter-test</artifactId>
                    <scope>test</scope>
                </dependency>
            </dependencies>
            <build>
                <plugins>
                    <! -- 该插件限定Maven打包时所使用的版本，避免出现版本不匹配问题 -->
                    <plugin>
                        <groupId>org.apache.maven.plugins</groupId>
                        <artifactId>maven-compiler-plugin</artifactId>
                        <version>3.5.1</version>
                        <configuration>
                            <source>1.8</source>
                            <target>1.8</target>
                        </configuration>
                    </plugin>
                    <! -- 该插件可以让Maven将工程直接打包成一个可以直接运行的JAR -->
                    <plugin>
                        <groupId>org.springframework.boot</groupId>
                        <artifactId>spring-boot-maven-plugin</artifactId>
                    </plugin>
                </plugins>
            </build>
          </project>
```
          - Spring Boot版本：这里采用1.5.2.RELEASE；
          - Spring Boot Starter：这里仅添加了Web，说明这是一个Web应用；
          - Guava：这是一个非常有用的工具库；
          - spring-boot-maven-plugin插件：该插件可以将项目打包成一个Fat Jar，然后直接通过java -jar的方式运行。至于什么是Fat Jar，后面会详细说明。说明：在后续章节中，Maven脚本文件不会像这里一样全部列出，仅会列出关键或需要修改的部分。
        - **编写应用引导类**
          - 对于Spring Boot应用来说，首先需要创建一个应用引导类
            - `main(String[] args)` 主函数
            - `@SpringBootApplication` 注解标识
          - 作用
            - 让Spring Boot框架启动并初始化应用
```java
            // @SpringBootApplication注解可以让Spring Boot框架通过该类启动整个应用
            @SpringBootApplication
            public class Application {
              public static void main(String[] args) throws Exception {
                // 调用SpringApplication启动一个Spring Boot应用
                SpringApplication.run(Application.class, args);
              }
            }
```
            - `@SpringBootApplication` 注解告诉Spring容器：**使用该类作为所有Bean源，通过该起始点构建应用的上下文**
            - `@SpringBootApplication` 注解继承自 `@EnableAutoConfiguration` 和 `@ComponentScan`，通过该注解使得项目在启动时Spring就会对该类所属目录下的所有子包进行扫描并根据Spring Boot的自动配置机制进行配置
            - 引导类如不在应用的根包中可能会造成部分配置或Bean无法被Spring扫描到，从而造成系统配置出错，导致启动失败
              - 如果项目中由于某些原因不能这么做的话，可以通过 `@ComponentScan` 注解进行修正，在 `@ComponentScan` 注解中可以配置需要扫描包的位置
```java
                package com.cd826dong.clouddemo.XXX.XX.application;
                import …
                @SpringBootApplication
                // 这里我们通过@ComponentScan注解，将配置自动扫描的起始位置设置为com.cd826dong
                @ComponentScan("com.cd826dong.＊＊")
                @EntityScan(basePackageClasses=User.class)
                public class Application {
                  public static void main(String[] args) throws Exception {
                    SpringApplication.run(Application.class, args);
                  }
                }
```
            - `Application` 类的`main()`方法调用了`SpringApplication.run()`，该方法会在项目启动时构建一个`Spring`容器，并返回一个`ApplicationContext`对象，也就是项目应用的上下文。
              - 对于`ApplicationContext`重要性，使用过Spring开发的读者都应该明白，但在这里因为不需要该对象做后续任何处理，所以没有列出来。
            - 对于引导类来说其是整个应用启动的初始点，因此，如果在应用启动时需要进行某些初始化处理，那么最好都在该类中完成。
        - **编写配置文件**
          - `properties`
          - `yml`
```properties
            # 应用启动后所监听的端口，可以不配置，默认就是8080端口
            server.port=8080
            # 配置日志输出级别，将Spring框架设置为INFO级别，
            # 而我们所编写的代码设置为DEBUG级别
            logging.level.org.springframework=INFO
            logging.level.com.cd826dong=DEBUG
```
        - **运行项目**
          - 对微服务来说，更多的时候是打包成一个部署单元
          - 在打包时就会使用之前我们在Maven脚本中所配置的`spring-boot-maven-plugin`插件，然后通过`mvn clean package`命令将项目打包成一个 `Fat Jar`
            - Fat Jar
              - 胖Jar
              - 不仅仅包含本项目中源码所编译生成的Java类文件，还会包含项目所依赖的第三方库及有关项目启动的相关信息
              - 文件中会包含以下3个内容
                - 项目代码
                  - 项目中所有源码经编译后会存放在 `BOOT-INF/classes` 下
                - 项目依赖包
                  - 存放在 `BOOT-INF/lib` 目录下
                - 应用启动相关文件
                  - `org/springframework/boot/loader` 下则包含了Spring Boot启动时所需要的类
```shell
            # 通过-jar直接启动
            $ java -jar cd826dong-clouds-boot-0.0.1-SNAPSHOT.jar
```
          - 在本示例项目中我们只构建了一个简单的Java类，并通过该类中的main()函数启动运行，并没有在打包之后将文件部署到任何Web容器中进行运行。那么示例项目为何就可以作为一个Web应用启动了呢？
            - `spring-boot-starter-web` 默认依赖了`spring-boot-starter-tomcat`，通过该依赖，Spring Boot在启动应用时就会启动一个内嵌的Tomcat容器，并在该容器中运行项目。
            - 如果不想使用Tomcat作为启动容器，而是使用Jetty，那么可以在pom.xml文件中排除对Tomcat的依赖，并增加`spring-boot-starter-jetty`即可。
      - 2.3 使用Spring Boot构建示例项目
        - 经典三层应用架构 (**整个应用架构上**)
          - 客户端层UI层
            - 主要用来与用户进行交互，显示数据并接收用户的输入，也常称为前端。一般对于一个应用通常会存在多种客户端，如Web、H5、App等。
          - 应用层
            - 系统核心价值部分
            - 其关注业务规则的制定和业务流程的实现，负责与UI层进行交互及数据存储的处理，我们常称为后端。
          - 存储层 / 持久层
            - 通常是一个数据库，主要用来保存我们的业务数据。
            - 当然这里数据存储指的不仅仅是关系型数据库，也包含非关系型数据库，如MongoDB、Redis或者文件存储系统，在我们存储附件、多媒体文件或图片时使用
          - 后端（应用层）的开发在架构搭建时往往也可以分为三层
            - 业务逻辑层
              - 该层主要承担两大职责
                - 定义业务领域对象 / 业务实体 (Domain)；
                - 业务逻辑的具体实现 (Service)。
            - 接口层（API层）
              - 该层用来对接UI层，为UI层提供数据集业务处理接口，一般将其称为Controller
              - 此外，现在的应用开发一般会对接多种用户端UI层，所以常常在这里使用REST方式提供API接口，供各个应用端使用，因此也可以称之为API层
            - 数据接口层（DAO）
              - 负责业务实体对象的数据处理，如增、删、改、查等，通常定义为Repository
              - 该层开发时往往会使用`O/R Mapping`技术，如Hibernate、JPA等。此外，数据接口层也包含对非关系型数据及文件或云存储的处理
          - ![image.png](../assets/book/Spring-Cloud-微服务架构开发实战/image_1672280754319_0.png)
        - 设计领域对象 (Domain)
          - 识别对象 + 对象间的交互关联
          - 开发核心 / 最难变更的部分
          - via: 《领域驱动设计：软件核心复杂性应对之道》[美] Eric Evans
```shell
            User
            Product
              ProductComment
```
            ![idea64_46.png](../assets/book_SpringCloud_微服务架构开发实战/idea64_46_1673420429327_0.png)
        - 数据管理
          - ORM / Object Relational Mapping #framework
            - Hibernate
              description: 辅助我们将业务对象通过映射的方式存储到数据库中，而不需要使用最原始的SQL语言
          - JPA / Java Persistence API / Java持久性规范
            description: 一个数据存储标准接口定义(By SUN)
            - 作用
              - 将业务与具体存储的数据库解耦，不需要为不同的数据库编写不同的处理方法，从而方便在多种数据库之间进行切换。
              - 当使用JPA时，对于简单的增、删、改、查等功能几乎不需要编写任何代码，只需继承JpaRepository接口即可
            - Spring Data JPA
              - 注释 Annotation
                - `@Entity`
                - `@Id`
                  - 注解数据库主键
                  - 通过 `@GeneratedValue` 告诉JPA自动生成主键的值，默认情况下会使用数据库自增方式。也可以通过下面的注解来指定主键的生成方式
                - `@Table`
                - `@Column`
            - `JpaRepository`继承自`PagingAndSortingRepository`，而`PagingAndSortingRepository`又继承了`CrudRepository`，从这些接口的命名上，我们可以推断所定义的`UserRepository`已经具备了分页数据查询和增、删、改、查等功能，事实也是如此
              - 对于该接口，我们也不需要在项目中进行实现，而是在项目启动时`Spring Data`会通过动态代码生成机制为我们创建该接口的具体实现类，并注册到Spring的应用上下文中，供我们在其他地方使用。此外，为方便查询处理，**Spring Data还提供了自然语义的数据访问处理机制**
                - 比如，我们可以在接口中定义一个名称为findTop10OrderByJoinDateDesc的方法，这时候Spring Data会自动实现查询最新加入的10个用户，并按照加入日期倒序排列。
                - 对于稍微复杂一些的查询，可能需要定义的方法比较长。比如findTop10ByUserSexAndCityAndAgeOrderByJoinDateDesc，用来查询某个城市中指定年龄段最新加入的前10名男性或女性用户。这种命名方法显然使用时非常不友好
                  - Spring Data还提供了`@Query`注解，可以直接在方法中声明该方法查询时所使用的查询语句，所声明的查询语句使用JPQL语言
        - 业务逻辑层 (Service)
          - Domian→REST API→业务逻辑层→数据存储层
          - DTO[^DTO] / Data **Transfer** Object / 数据传输对象
            description: 一般只有数据属性, 无业务逻辑, 一般用作前后端分离时的数据传输
        - **编写RESTful API**
          - Spring MVC针对Controller提供了两个注解
            - `@Controller`
              return: 将HTML部分的代码也一起返回给调用者
              - `@Controller + @ResponseBody` == `@RestController`
            - `@RestController`
              return: 所有使用 `@RequestMapping` 的方法返回响应体(response body)
              - `@RequestMapping`
                scope: 方法或类
                - 注解类上
                  - 类中所有注解的方法都会继承类中所声明的属性
                - 简化的注解
                  - @GetMapping
                    description: 处理Get请求
                  - @PostMapping
                    description: 处理Post请求
            - >[!note]
              > 注意返回值，最好的方式就是==对返回值进行统一包装==
              - 当方法的返回值是一个对象时，Spring MVC就会默认使用JSON序列化方法将对象序列化为一个JSON格式的字符串，并返回给请求者
              - 假如方法中的是返回基础数据类型 (boolean/int/...)
                - 无法进行序列化，从而造成错误
          - [ ] #gtd/todo [Swagger](https://swagger.io/)  
            description: 当系统启动后, 可以在浏览器中通过地址 `root/swagger/index.html` 访问到所生成的API文档
        - **数据库初始化**
          - Hibernate
            description: 根据实体类自动创建数据库
          - Spring JDBC #jdbc 
            description: 初始化 `DataSource`, 在启动系统时检测 `classpath` 根目录下是否有 `schema.sql` 和 `data.sql` 脚本文件，如果存在这两个脚本文件存在或者其中一个，将会尝试加载并执行该脚本，初始化产生异常，应用系统启动将会失败
            - `schema.sql` 创建数据库表
            - `data.sql` 初始化数据
              - 通过设置项目配置文件, 初始化脚本
                - `spring.datasource.schema`
                - `spring.datasource.data`
              - `spring.datasource.initialize` == `false`
                - Spring Boot在启动时将不执行数据库初始化处理
        - DTO [^DTO]
      - 2.4 Spring Boot特性
      - 2.5 关于敏捷开发
      - 2.6 关于RESTful API设计
  - 第2篇 Spring Cloud组件实战
    - 第3章 Spring Cloud简介
      - 3.1 微服务架构的核心关键点
        - ![](epub_22920378_12.jpeg)
          - 服务治理
          - 负载均衡
          - 统一入口
          - 容错
          - 统一配置
          - 监控
          - 部署
      - 3.2 Spring Cloud技术概览
        - **==Spring Cloud==**
          description: "在Netflix OSS等多家开源的基础上，使用Spring Boot风格将这些比较成熟的微服务框架组合起来，屏蔽掉了复杂的配置和实现原理，为快速构建微服务架构的应用提供了一套基础设施工具和开发支持。所提供的基础设施，如服务发现、客户端负载均衡、API网关、微服务容错、统一配置中心、消息总线及微服务调用监控等，都可以做到一键启动和部署，极大减轻了我们进入微服务世界的难度"
          - 基于Netflix实现服务治理、客户端负载均衡和声明式调用；
          - 服务网关；
          - 微服务容错管理；
          - 整合消息中间件提供消息驱动式开发；
          - 基于Spring Security提供微服务安全、单点登录功能；
          - 分布式、版本化的统一配置管理；
          - 微服务调用链及追踪管理
        - Spring Cloud 子项目
          - 分类 
            - 对现有成熟的第三方开源项目Spring Boot化，进行封装集成
              - 使得我们基于Spring的开发非常容易集成和使用
            - 新增一些微服务架构开发所需的基础设施
              - 如Spring Cloud Config提供了统一配置中心
              - Spring Cloud Stream则充当了与Kafka、RabbitMQ等消息中间件快速集成的桥梁
              - ![](epub_22920378_13.jpeg)
          - 1.Spring Cloud与Spring Boot
            - 每一个微服务就是一个独立的应用
              - 每一个独立的应用都需要一些基础设施和配置的要求 (Spring Boot)
                - 快速启动
                - 能够提供基于REST架构的服务接口等
            - Spring Boot默认提供JackJson序列化支持
              - 可以让服务接口输入、输出支持JSON
          - 2.Spring Cloud与服务治理(核心)
            - 2 个实现
              - Consul
                - More via: https://cloud.spring.io/spring-cloud-consul/
              - Eureka by Netflix
      - 3.3 Spring Cloud版Hello World示例
    - 第4章 服务治理与负载均衡
      - 4.1 什么是服务治理
      - 4.2 构建服务治理——Eureka
      - 4.3 使用客户端负载均衡——Ribbon
      - 4.4 使用Feign简化微服务调用
      - 4.5 深入Eureka
      - 4.6 深入Ribbon
      - 4.7 深入Feign
      - 4.8 微服务健康监控
      - 4.9 异构服务解决方案——Sidecar
    - 第5章 微服务容错保护——Hystrix
      - 5.1 什么是微服务容错保护
      - 5.2 快速启动Hystrix
      - 5.3 Hystrix容错机制分析
      - 5.4 服务隔离
      - 5.5 服务降级模式
      - 5.6 请求缓存
      - 5.7 请求合并
      - 5.8 Hystrix监控
    - 第6章 API服务网关——Zuul
      - 6.1 API服务网关
      - 6.2 Spring Cloud与Netflix Zuul
      - 6.3 启用Zuul路由服务
      - 6.4 路由配置规则
      - 6.5 Zuul路由其他设置
      - 6.6 Zuul容错与回退
      - 6.7 Zuul过滤器
      - 6.8 @EnableZuulServer与@EnableZuulProxy比较
    - 第7章 统一配置中心——Config
      - 7.1 Spring Cloud Config简介
      - 7.2 快速启动
      - 7.3 配置资源库
      - 7.4 配置的加密与解密
      - 7.5 配置服务器访问安全
      - 7.6 配置服务器的高可用
    - 第8章 分布式服务跟踪——Sleuth
      - 8.1 Spring Cloud Sleuth简介
      - 8.2 Sleuth与ELK整合
      - 8.3 整合Zipkin服务
      - 8.4 Sleuth抽样采集与采样率
    - 第9章 消息驱动——Stream
      - 9.1 什么是消息驱动开发
      - 9.2 Spring Cloud Stream简介
      - 9.3 Kafka使用指南
      - 9.4 使用消息对应用重构
      - 9.5 Spring Cloud Stream高级主题
      - 9.6 消息总线——Spring Cloud Bus
    - 第10章 微服务应用安全——Security
      - 10.1 Spring Boot的应用安全
      - 10.2 微服务安全
      - 10.3 基于OAuth 2.0的认证
      - 10.4 基于JWT的认证
  - 第3篇 微服务与Docker容器技术
    - 第11章 微服务与Docker
      - 11.1 Docker简介
      - 11.2 Docker的使用
      - 11.3 Docker与Spring Cloud微服务
      - 11.4 微服务与Jenkins
      - 11.5 微服务编排
- ---
## Reference
[^DTO]: DTO is a simple plain old Java object (POJO) that is used to transfer data between layers of an application, such as between the service and web layers.
    - Used to decouple(解耦) the presentation layer of an application from the service layer, which can improve the testability and maintainability of the code.
    - Be serialized and deserialized using JSON or XML
    - Benefit
      - they are typically simple and straightforward to use
      - help to keep the codebase clean
      - organized by separating the concerns of the different layers of the application.
    - 用来处理跨进程或网络传输数据聚合容器
  -