---
cover: https://img3.doubanio.com/view/subject/s/public/s34360957.jpg
author: Craig Walls
created: 2023-01-11
isbn: 9787115598691
lang: chinese
published: 20221201
rating: ⭐⭐⭐⭐
status: book/reading
tags: #spring-framework #java
type: book/dev
douban: https://book.douban.com/subject/36142064
weread: https://weread.qq.com/web/bookDetail/c6d32700813ab77d1g0136f4
---

[habuma/spring-in-action-6-samples: Sample code from Spring in Action 6](https://github.com/habuma/spring-in-action-6-samples)

## 📄 Contents
  - 关于本书
    - 第1部分 涵盖了构建Spring应用的基础知识
      - 第1章介绍Spring、Spring Boot，以及如何初始化Spring项目。我们在这章中迈出构建Spring应用的第一步，在本书后续章节中，我们会对这个应用进行扩展。
      - 第2章讨论如何使用Spring MVC构建应用的Web层。我们会构建处理Web请求的控制器，并在浏览器中渲染信息的视图。
      - 第3章深入探讨Spring应用的后端，在这里数据会持久化到关系型数据库中。
      - 第4章会继续数据持久化的话题，学习如何将数据持久化到非关系型数据库Cassandra和MongoDB中。
      - 第5章介绍如何使用Spring Security认证用户并防止未认证的用户访问应用。
      - 第6章介绍如何使用Spring Boot的配置属性功能来配置Spring应用。我们还会在这章学习如何使用profile选择性地应用配置。
    - 第2部分 讨论了如何将Spring应用与其他应用进行集成。
      - 第7章延续第2章对Spring MVC的讨论，我们会学习如何在Spring中编写和消费REST API。
      - 第8章展示如何使用Spring Security和OAuth 2保护我们在第7章创建的API。
      - 第9章讨论如何使用异步通信技术让Spring应用发送和接收消息，这里会用到Java Message Service、RabbitMQ或Kafka。
      - 第10章讨论如何使用Spring Integration进行声明式地应用集成。
    - 第3部分 探讨了Spring对反应式编程提供的全新支持。
      - 第11章介绍Reactor项目，这是一个反应式编程库，支撑Spring 5的反应式特性。
      - 第12章重新探讨REST API开发，介绍全新的Web框架Spring WebFlex。该框架借用了很多Spring MVC的理念，为Web开发提供了新的反应式模型。
      - 第13章介绍如何使用Spring Data编写反应式数据持久化，我们会尝试读取和写入Cassandra与Mongo数据库。
      - 第14章介绍RSocket协议。这是一个新的通信协议，在创建API方面，它提供了HTTP协议的反应式替代方案。
    - 第4部分 介绍了如何做好应用投入生产环境前的准备工作，以及如何进行部署。
      - 第15章介绍Spring Boot Actuator。这是Spring Boot的一个扩展，它通过REST端点的形式暴露Spring应用内部的运行状况。
      - 第16章介绍如何使用Spring Boot Admin。它是构建在Actuator之上的一个对用户友好的基于浏览器的管理应用。
      - 第17章讨论如何将Spring bean暴露为JMX MBean，以及如何消费它们。
      - 最后，第18章介绍如何将Spring应用部署到各种生产环境中，包括Kubernetes。
  - 第1部分 Spring基础 -nested-3
    - Spring起步
      - 1.1 什么是Spring
        - 概念
          - 组件 (components, Bean)
          - 容器 (container, Spring application context / Spring应用上下文)
          - 依赖注入 (Dependency Injection, DI)
          - ![](../../soul/assets/book_Spring_in_Action/6.png)
            (商品服务需要依赖于库存服务，这样它才能提供商品的完整信息)
            (应用组件通过Spring的应用上下文来进行管理并实现互相注入)
        - 组件关联 -- XML -> Java
```xml
            <bean id = "inventoryService" class = "com.example.InventoryService" />
            <bean id = "productService" class = "com.example.ProductService" />
              <constructor-arg ref = "inventoryService" />
            </bean>
```
            ==
```java
            // NOTE: 告知Spring这是一个配置类，它会为Spring应用上下文提供bean
            @Configuration
            public class ServiceConfiguration {
              // NOTE: 方法所返回的对象会以bean的形式添加到Spring的应用上下文中
              // bean ID == method name by default
              @Bean
              public InventoryService inventoryService() {
                return new InventoryService();
              }
              @Bean
              public ProductService productService() {
                return new ProductService(inventoryService());
              }
            }
```
          - 自动配置起源
            - Component Scanning / 组件扫描
              description: 自动发现应用类路径下的组件，并将它们创建成Spring应用上下文中的bean
              id: 63bf6bef-9cb8-4fbc-96e2-c91f43d0d303
            - Autowiring / 自动装配
              description: 自动为组件注入它们所依赖的其他bean
              id: 63bf6bef-a710-4323-adf1-55dfc0d193e1
          - Spring Boot >>  ((63bf6bef-9cb8-4fbc-96e2-c91f43d0d303)) & ((63bf6bef-a710-4323-adf1-55dfc0d193e1))
            description: Spring框架的扩展，提供了很多生产效率方面的增强
            - Autoconfiguration / 自动配置
              description: 基于类路径中的条目、环境变量和其他因素合理猜测需要配置的组件，并将它们装配在一起
            - > 自动配置就像风一样，你可以看到它的效果，但是我找不到代码指给你说，“看！这就是自动配置的样例！”事情发生了，组件启用了，功能也提供了，但是不用编写任何的代码。没有代码就是自动装配的本质，也是它如此美妙的原因所在。
            - Spring XML配置是一种过时的方式, 本书会将Spring和Spring Boot当成一回事
      - 1.2 初始化Spring应用
        - Spring Initializr
          description: 基于浏览器的Web应用 / REST API, 能够生成一个Spring项目结构的骨架
          - 使用方式 
            - 通过地址为 https://start.spring.io/ 的Web应用；
            - 在命令行中使用curl命令；
            - 在命令行中使用Spring Boot命令行接口；
            - 在Spring Tool Suite中创建新项目；
            - 在IntelliJ IDEA中创建新项目；
            - 在NetBeans中创建新项目；
            - 在Apache NetBeans中创建新项目。
        - 使用 Spring Tool Suite 初始化Spring项目
          - > 尽管我可以教你手动创建项目目录结构和定义构建规范的各个步骤，但这无疑是浪费时间，我们最好将时间花在编写应用代码上
          - > 如果你不是Spring Tool Suite用户，那也没有关系，我们依然可以做朋友
        - 项目结构
          - ![](../../soul/assets/book_Spring_in_Action/11.png)
          - 应用的源码放到了`src/main/java`
          - 测试代码放到了`src/test/java`
          - 非Java的资源放到了`src/main/resources`
          - `mvnw` / `mvnw.cmd`
            description: Maven包装器(wrapper)脚本，即便没有Maven，也可以构建项目
          - `pom.xml`
            description: Maven 构建规范
          - `TacoCloudApplication.java`
            description: Spring Boot主类，启动该项目
          - `application.properties`
            description: 指定配置属性的 (第6章
          - `static`
            description: 为浏览器提供服务的静态内容 (图片/样式表/JavaScript等), 初始为空
          - `templates`
            description: 用来渲染内容到浏览器的模板文件; 初始是空; Thymeleaf
          - `TacoCloudApplicationTests.java`
            description: 测试类，确保Spring应用上下文成功加载
        - 构建规范
```xml
            <?xml version = "1.0" encoding = "UTF-8"?>
              <project     xmlns = "http://maven.apache.org/POM/4.0.0"
                        xmlns:xsi = "http://www.w3.org/2001/XMLSchema-instance"
                          xsi:schemaLocation = "http://maven.apache.org/POM/4.0.0
                    https://maven.apache.org/xsd/maven-4.0.0.xsd">
              <modelVersion>4.0.0</modelVersion>
              <parent>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-starter-parent</artifactId>
                <version>2.5.3</version>
                <!-- NOTE:
                    使用 Spring Boot 2.5.3,
                    依赖管理指定底层的核心Spring框架的版本为5.3.9
                -->
                <relativePath />
              </parent>
              <groupId>sia</groupId>
              <artifactId>taco-cloud</artifactId>
              <version>0.0.1-SNAPSHOT</version>
              <name>taco-cloud</name>
              <description>Taco Cloud Example</description>
              <properties>
                <java.version>11</java.version>
              </properties>
              <dependencies>
                <!-- Starter依赖-->
                <dependency>
                  <groupId>org.springframework.boot</groupId>
                  <artifactId>spring-boot-starter-thymeleaf</artifactId>
                </dependency>
                <dependency>
                 <groupId>org.springframework.boot</groupId>
                 <artifactId>spring-boot-starter-web</artifactId>
                </dependency>
                <dependency>
                  <!-- by default -->
                  <groupId>org.springframework.boot</groupId>
                  <artifactId>spring-boot-starter-test</artifactId>
                  <scope>test</scope>
                  <exclusions>
                    <exclusion>
                      <groupId>org.junit.vintage</groupId>
                      <artifactId>junit-vintage-engine</artifactId>
                    </exclusion>
                  </exclusions>
                </dependency>
                <dependency>
                  <groupId>org.springframework.boot</groupId>
                  <artifactId>spring-boot-devtools</artifactId>
                  <scope>runtime</scope>
                  <optional>true</optional>
                </dependency>
            </dependencies>
            <build>
              <plugins>
                <!-- Spring Boot插件 -->
                <plugin>　
                  <groupId>org.springframework.boot</groupId>
                  <artifactId>spring-boot-maven-plugin</artifactId>
                </plugin>
              </plugins>
            </build>
            <repositories>
              <repository>
                <id>spring-milestones</id>
                <name>Spring Milestones</name>
                <url>https://repo.spring.io/milestone</url>
              </repository>
              </repositories>
              <pluginRepositories>
                <pluginRepository>
                  <id>spring-milestones</id>
                  <name>Spring Milestones</name>
                  <url>https://repo.spring.io/milestone</url>
                </pluginRepository>
              </pluginRepositories>
            </project>
```
          - `<parent>`
            - 继承 父POM 中所涵盖到的库, 不需要指定版本
          - `<dependencies>`
            - Starter依赖 (它们本身并不包含库代码，而是传递性地拉取其他的库)
              - 减小构建文件大小且易于管理(不必为所需的每个依赖库都声明依赖)
                - 面向功能依赖导入依赖
                - Web应用只需添加web starter依赖，而不必添加一堆单独的库
              - 不必再担心库版本的问题 (Spring Boot version insteaded.)
          - `<plugin>` Spring Boot插件
            - 提供了一个Maven goal，允许使用Maven来运行应用
            - 确保依赖的所有库都会包含在可执行JAR文件中
              - 并且能够保证它们在运行时类路径下是可用的；
            - 在JAR中生成一个manifest文件，将引导类声明为可执行JAR的主类
              - TacoCloudApplication.java
        - 引导应用
```java
            package tacos;
            import org.springframework.boot.SpringApplication;
            import org.springframework.boot.autoconfigure.SpringBootApplication;
            @SpringBootApplication    // Spring Boot应用(POWERFUL!!!)
            public class TacoCloudApplication {
              public static void main(String[] args) {
                SpringApplication.run(TacoCloudApplication.class, args); //
                /** NOTE:  运行应用(样板代码)
                 * SpringApplication 中静态的 run() 方法，才真正执行应用的引导过程
                 * 传递 2 个参数 (配置类 + 命令行参数)
                     * 配置类不一定要和引导类相同，但这是最便利和最典型的做法???
                */
              }
            }
```
          - `@SpringBootApplication`
            id: 63bfd20c-314f-459c-a0bc-dfc7230de2df
            - `@SpringBootConfiguration`
              description: 声明为配置类; 实际上是 `@Configuration` 的特殊形式。
            - `@EnableAutoConfiguration`
              description: 自动配置 Spring Boot 认为我们会用到的组件
            - `@ComponentScan`
              description: 组件扫描, Spring 自动发现并将它们注册为Spring应用上下文中的组件, 通过 `@Component` / `@Controller` / `@Service`... 这样的注解声明其他类
        - 测试应用
          - 手动测试
```shell
              $ ./mvnw package
              ...
              $ java -jar target/taco-cloud-0.0.1-SNAPSHOT.jar
```
            - Spring Boot的Maven插件更加简单
```shell
                $ ./mvnw spring-boot:run
```
          - 自动测试 (一致 + 可重复)
```java
              package tacos;
              import org.junit.jupiter.api.Test;
              import org.springframework.boot.test.context.SpringBootTest;
              @SpringBootTest　　// Spring Boot测试
              public class TacoCloudApplicationTests {
                // 测试方法
                // 空的测试方法也会提示该注解完成了它的工作并成功加载Spring应用上下文
                @Test　　
                public void contextLoads() {
                }
              }
```
            - `@SpringBootTest`
              description: 告诉 JUnit 在启动测试的时候要添加上Spring Boot的功能
              - `ExtendWith(SpringExtension.class)`
                - 将Spring的测试功能添加到JUnit 5中
              - 与 ((63bfd20c-314f-459c-a0bc-dfc7230de2df)) 魅力相当
```shell
              # 执行
              $ ./mvnw test
```
      - 1.3 编写Spring应用
        - 1.3.1 处理Web请求
          - Spring MVC
            description: Spring自带的Web框架
            - Controller / 控制器(核心)
              description: 处理请求并以某种方式进行信息响应的类, 控制器填充可选的数据模型并将请求传递给一个视图，以便于生成返回给浏览器的HTML
```java
            @Controller
            /* NOTE: 控制器
                Spring会自动发现并创建一个HomeController实例作为Spring应用上下文中的bean*/
            public class HomeController {
              @GetMapping("/")                        // 处理对根路径“/ ”的请求
              public String home() {
                return "home";
                /** RETURN: String, 值将会解析为视图的逻辑名
                 * 逻辑名加上 `/templates/`前缀 和 `.html` 后缀, 得到
                 * `/templates/home.html`
                */
              }
            }
```
            - `@Controller`
              description: 目的是让组件扫描将这个类识别为一个组件
              - `@Component` / `@Service` / `@Repository`
                - 目的相同, 结果相同
                - `@Controller` 更能描述这个组件在应用中的角色
          - Thymeleaf位于类路径中，使得我们可以使用Thymeleaf来定义模板???
        - 1.3.2 定义视图
```html
            <!DOCTYPE html>
            <html xmlns = "http://www.w3.org/1999/xhtml"
                  xmlns:th = "http://www.thymeleaf.org">
              <head>
                <title>Taco Cloud</title>
              </head>
              <body>
                <h1>Welcome to...</h1>
                <img th:src = "@{/images/TacoCloud.png}"/>
                <!-- NOTE: 图片使用相对于上下文的 `/images/TacoCloud.png` 来引用, 结果
                `/src/main/resources/static/images/TacoCloud.png`
                -->
              </body>
            </html>
```
        - 1.3.3 测试控制器
          - 对 HTML 断言???
          - 测试
            - 针对根路径“/”发送一个HTTP GET请求并期望得到成功结果
            - 其中视图名称为home并且结果内容包含“Welcome to...”
```java
            @WebMvcTest(HomeController.class)　　// 针对HomeController的Web测试
            public class HomeControllerTest {
              @Autowired
              private MockMvc mockMvc;　　// 注入MockMvc, 能够让测试实现 mockup
              @Test
              public void testHomePage() throws Exception {
                mockMvc.perform(get("/"))　　          // 发起对“/”的GET请求
                  .andExpect(status().isOk())　       // 期望得到HTTP 200
                  .andExpect(view().name("home"))    // 期望得到home视图
                  .andExpect(content().string(　　  // 期望包含“Welcome to...”
                      containsString("Welcome to...")));
              }
            }
```
            - `@WebMvcTest` by Spring Boot
              description: 提供了Spring环境的支持, 让测试在Spring MVC应用的上下文中执行, 即将HomeController注册到Spring MVC中, 以便于发请求
              - ((63d268d6-2155-4425-93aa-21bf9186c87d))
              - ((63d2699d-04d0-41da-bc94-c357a4f43608))
              - See what package is imported auto via: ((63d27402-b74e-462a-92f7-8cb894ba8cae))
            - [wireframe，prototype，mockup到底有何不同？ | by MockingBot | Medium](https://medium.com/@mockingbot/wireframe-prototype-mockup%E5%88%B0%E5%BA%95%E6%9C%89%E4%BD%95%E4%B8%8D%E5%90%8C-85e9dddb67f8)
        - 1.3.4 构建和运行应用
```shell
            java -jar demo.jar
            java -jar demo.war
            # Maven
            mvn spring-boot:run
            # Gradle
            gradle bootRun
```
        - 1.3.5 了解Spring Boot DevTools
          - DevTools 
            description: 提供了一些便利的开发期工具和特性
            - 代码热更新, 自动重启；
              - 刚启用, 应用程序会加载到JVM中的 2 个独立的类加载器中 
                - 加载代码 / 属性文件 / 项目的 `src/main/` 下几乎所有内容
                  - (经常变化)
                - 加载依赖的库(不常变化)
              - 探测到变更时
                - 重新加载 1 的类加载器 + 重启Spring的应用上下文
                - 2 不变
                  - 减少应用启动的时间
                  - [不足] 无法反映依赖项的变化, 因为 2 不会变化
                    - 每当在构建规范中添加、变更或移除依赖的时候, 都要重新启动应用
            - 自动刷新 + 禁用模板缓存；
              description: 面向浏览器的资源(模板 / JS / CSS)
              - LiveReload服务器
            - (内置了H2控制台)
              - http://localhost:8080/h2-console, 就能看到应用所使用的数据
        - 1.3.6 回顾一下
          - Spring Boot 只关注满足应用需求的代码，无须考虑如何满足框架的需求
          - Spring / Spring Boot 可以视为感受不到框架的框架 (frameworkless framework)
          - Thymeleaf starter引入的依赖，包括：
            - Spring的MVC框架；
            - 嵌入式的Tomcat；
            - Thymeleaf和Thymeleaf布局方言。
          - 刚启动, SB探测并完成:
            - 在Spring应用上下文中配置bean以启用Spring MVC；
            - 在Spring应用上下文中配置嵌入式的Tomcat服务器；
            - 配置Thymeleaf视图解析器以便于使用Thymeleaf模板渲染Spring MVC视图
      - 1.4 俯瞰Spring风景线
        - 1.4.1 Spring核心框架
          - Spring Web -> Spring MVC
            - `@Controller` Web
            - `REST API` Web
          - 数据持久化 JdbcTemplate
          - Reactive 反应式风格编程 -> Spring WebFlux的新反应式Web框架
        - 1.4.2 Spring Boot 提供 
          - starter依赖
          - 自动配置
          - Actuator
            description: 洞察应用运行时的内部工作状况，包括指标、线程dump信息、应用的健康状况以及应用程序可用的环境属性；
          - 灵活的环境属性规范；
          - 在核心框架的测试辅助功能之上，提供了对测试的额外支持
          - 基于Groovy脚本的编程模型 / Spring Boot CLI
            description: 将整个应用程序编写为Groovy脚本的集合，并通过命令行运行它们
        - 1.4.3 Spring Data 
          - 将应用程序的数据存储库(repository)定义为简单的Java接口，在定义存储和检索数据的方法时使用一种特定的命名约定即可
          - 处理多种不同类型的数据库
            - 关系型数据库（通过JDBC或JPA实现）
            - 文档数据库(Mongo)
            - 图数据库(Neo4j)
        - 1.4.4 Spring Security (范围太大) 
          - 包括身份验证
          - 授权和API安全性
          - ...
        - 1.4.5 Spring Integration和Spring Batch
          - 应用集成
          - Spring Integration
            description: 实时集成问题，在实时集成中，数据在可用时马上就会得到处理
          - Spring Batch
            description: 批处理集成的问题，在此过程中，数据可以收集一段时间，直到某个触发器（可能是一个时间触发器）发出信号表明是时候处理批量数据了，才会得到处理
        - 1.4.6 Spring Cloud
          - 关于对Spring Cloud的完整介绍，我推荐阅读Thomas Vitale的Cloud Native Spring in Action（Manning，2020年）
        - 1.4.7 Spring Native
          - 关于对Spring Cloud的完整介绍，我推荐阅读Thomas Vitale的Cloud Native Spring in Action（Manning，2020年）
          - 关于Spring Native的更多信息，参见GitHub网站的spring-projects-experimental/spring- native代码库。
    - 开发Web应用 (硬编码, 把数据写在代码里)
      - 2.1 展现信息
        - ![](../../soul/assets/book_Spring_in_Action/14.png)
        - 2.1.1 构建领域类
          - 应用领域
            description: 它所要解决的主题范围，也就是会影响应用理解的理念和概念
          - ![](../../soul/assets/book_Spring_in_Action/15.png)
          - Lombok
            description: 它能够在编译期自动生成这些方法(getter / setter / equals() / hashCode() / toString()...)，这样一来，在运行期就能使用它们了
            - Lombok的魔力是在编译期发挥作用的，所以在运行期没有必要用到它们
            - Lombok注解 (如@Data), 并在编译期进行自动化的方法生成
            - 需要重申的是，IDE中安装Lombok插件, 因为IDE将无从得知Lombok提供了getter、setter和其他方法，并且会因为缺失这些方法而报错。
```java
            @Slf4j
            @Controller
            /* 规定DesignTacoController处理路径以`/design`开头的请求 */
            @RequestMapping("/design")
            @SessionAttributes("tacoOrder")
            public class DesignTacoController {
            @ModelAttribute
            public void addIngredientsToModel(Model model) {
                List<Ingredient> ingredients = Arrays.asList(
                  new Ingredient("FLTO", "Flour Tortilla", Type.WRAP),
                  new Ingredient("COTO", "Corn Tortilla", Type.WRAP),
                  new Ingredient("GRBF", "Ground Beef", Type.PROTEIN),
                  new Ingredient("CARN", "Carnitas", Type.PROTEIN),
                  new Ingredient("TMTO", "Diced Tomatoes", Type.VEGGIES),
                  new Ingredient("LETC", "Lettuce", Type.VEGGIES),
                  new Ingredient("CHED", "Cheddar", Type.CHEESE),
                  new Ingredient("JACK", "Monterrey Jack", Type.CHEESE),
                  new Ingredient("SLSA", "Salsa", Type.SAUCE),
                  new Ingredient("SRCR", "Sour Cream", Type.SAUCE)
                );
                Type[] types = Ingredient.Type.values();
                for (Type type : types) {
                  model.addAttribute(type.toString().toLowerCase(),
                  filterByType(ingredients, type));
              }
            }
            @ModelAttribute(name = "tacoOrder")
            public TacoOrder order() {
              return new TacoOrder();
            }
            @ModelAttribute(name = "taco")
            public Taco taco() {
              return new Taco();
            }
            /*     对类级别的`@RequestMapping`进行了细化
                当接收到对`/design`的HTTP GET请求时，
                Spring MVC将会调用showDesignForm()来处理请求
            */
            @GetMapping
            public String showDesignForm() {
              return "design";
            }
            private Iterable<Ingredient> filterByType(
                List<Ingredient> ingredients, Type type) {
              return ingredients
                        .stream()
                        .filter(x -> x.getType().equals(type))
                        .collect(Collectors.toList());
              }
            }
```
            - `@Slf4j` by Lombok
              description: 它会在这个类中自动生成一个SLF4J Logger（SLF4J即simple logging facade for Java,请访问slf4j网站以了解更多）静态属性
```java
                private static final org.slf4j.Logger log =
                    org.slf4j.LoggerFactory.getLogger(DesignTacoController.class);
```
            - `@RequestMapping`
              description: 用到类级别的时候，它能够**指定该控制器所处理的请求类型**
            - `@GetMapping`
              description: 请求映射注解中的一个
              - ![](../../soul/assets/book_Spring_in_Action/Chapter02_table_1.jpg)
            - `@ModelAttribute`
              description: 方法也会在请求处理的时候被调用，并将其放到模型中
          - 硬编码???
        - 2.1.2 创建控制器类
          - Spring 提供了多种定义视图的方式 
            - JavaServer Pages(JSP)
            - Thymeleaf
            - FreeMarker
            - Mustache
            - 基于Groovy的模板
          - Thymeleaf和其他的视图模板, 在Spring将请求转移到视图之前，它会把模型数据复制到request属性中，
            - 视图库在设计时是与特定的Web框架解耦，它们无法感知Spring的模型抽象，无法与控制器放到Model中的数据协同工作。但它们**可以与Servlet的request属性协作**
        - 2.1.3 设计视图
```html
            <p th:text = "${message}">placeholder message</p>
            <h3>Designate your wrap:</h3>
            <div th:each = "ingredient : ${wrap}">
              <input th:field = "*{ingredients}" type = "checkbox"
                     th:value = "${ingredient.id}"/>
              <span th:text = "${ingredient.name}">INGREDIENT</span><br/>
            </div>
            <!-------[RESULT]:
            <div>
              <input name = "ingredients" type = "checkbox" value = "FLTO" />
              <span>Flour Tortilla</span><br/>
            </div>
            -->
```
          - `th:text`
            description: Thymeleaf命名空间中的属性; 元素体会被替换为Servlet request中key为`message`的属性值
          - `${}`
            description: 操作符会告诉它要使用某个request属性中的值
          - `th:each`
            description: 迭代一个元素集合，为集合中的每个条目渲染HTML
          - `th:field`
            description: 用来绑定后台对象和表单数据
          - `th:value`
            description: 用对象对name值替换value属性
          - `@{}`
            description: 用来生成一个相对于上下文的路径
      - 2.2 处理表单提交
      - 2.3 校验表单输入
        - JavaBean Validation API / JavaBean校验API / JSR-303
          description: 不必在应用程序代码中显式编写声明逻辑
          - 在构建文件中添加 `Spring Validation starter`；
          - 在要被校验的类上声明校验规则；
            - Taco类
          - 在需要进行校验的控制器方法中声明要进行校验
            - DesignTacoController的processTaco()方法
            - OrderController的processOrder()方法；
          - 修改表单视图以展现校验错误
```xml
            <dependency>
              <groupId>org.springframework.boot</groupId>
              <artifactId>spring-boot-starter-validation</artifactId>
            </dependency>
            <!-- SB 2.3.0 开始，校验需要显式地将其添加到构建文件中 -->
```
        - 2.3.1 声明校验规则
```java
            @Data
            public class Taco {
              @NotNull
              @Size(min = 5, message = "Name must be at least 5 characters long")
              private String name;
              @NotNull
              @Size(min = 1, message = "You must choose at least 1 ingredient")
              private List<Ingredient> ingredients;
            }
```
            - `@NotNull` & `@Size`
              description: 确保name属性不能为空或null
              - `@NotBlank`
                description: 没有提交空白字段
          - 合法的信用卡号 -> Luhn算法
        - 2.3.2 在表单绑定的时候执行校验
```java
            @PostMapping
            public String processTaco(
              @Valid Taco taco, Errors errors,
              @ModelAttribute TacoOrder tacoOrder) {
              if (errors.hasErrors()) {
                return "design";
              }
              tacoOrder.addTaco(taco);
              log.info("Processing taco: {}", taco);
              return "redirect:/orders/current";
            }
```
            - 校验时机
              - 在它绑定完表单数据之后、调用processDesign()之前???
            - 如果存在校验错误，这个方法将不会处理Taco对象并返回“design”视图名，以使表单重新展现???
        - 2.3.3 展现校验错误
          - Thymeleaf & `fields` & `th:errors`
```html
              <label for = "ccNumber">Credit Card #: </label>
                <input type = "text" th:field = "*{ccNumber}"/>
                <span class = "validationError"
                    th:if = "${#fields.hasErrors('ccNumber')}"
                    th:errors = "*{ccNumber}">CC Num Error</span>
                    <!-- fields属性的hasErrors()方法会检查ccNumber域是否存在错误 -->
```
              - `th:if`
                description: 决定是否要显示该元素
      - 2.4 使用视图控制器
        - 只将请求转发到视图而不做其他事情的控制器
```java
            package tacos.web // 配置类替换了HomeController类
            @Configuration
            public class WebConfig implements WebMvcConfigurer {
              @Override
              public void addViewControllers(ViewControllerRegistry registry) {
                registry.addViewController("/").setViewName("home");
                /** NOTE: 视图控制器将会针对该路径执行GET请求
                 * 这个方法会返回ViewControllerRegistration对象
                 * 马上基于该对象调用setViewName()方法
                 * 用它指明当请求“/”的时候要转发到“home”视图上。
                */
              }
            }
```
          - `WebMvcConfigurer`
            description: 定义了多个方法来配置Spring MVC，尽管只是一个接口，却提供了所有方法的默认实现，只需要我们覆盖所需的方法
          - 所有的配置类都可以实现WebMvcConfigurer接口并覆盖addViewController方法, 即上述方法可以放到引导类中.
      - 2.5 选择视图模板库
        - ![](../../soul/assets/book_Spring_in_Action/Chapter02_table_2.jpg)
        - 只有在将应用构建为WAR文件并部署到的Servlet容器中时，才选择JSP
          - Java Servlet容器 (嵌入式的Tomcat和Jetty容器) 通常会在 `/WEB-INF` 目录下寻找JSP文件。如果将应用构建成一个可执行的JAR文件，就无法满足这种需求了
          - 如果想要构建可执行的JAR文件，那么必须选择Thymeleaf、FreeMarker或表中的其他方案
        - ![](../../soul/assets/book_Spring_in_Action/Chapter02_table_3.jpg)
    - 使用数据 [^CH03_DEBUG] [^CH03_TEST]
      - 使用JDBC读取和写入数据
        - `JdbcTemplate`
          description: 提供了一种方式, 开发人员在对关系型数据库执行SQL操作的时候，能够避免使用JDBC时常见的繁文缛节和样板式代码
          description: 即便有了JdbcTemplate，一些持久化任务仍然很有挑战性，尤其是在**持久化聚合中的嵌套领域对象时**
```java
            @Override
            public Optional<Ingredient> findById(String id) {
              Connection connection = null;
              PreparedStatement statement = null;
              ResultSet resultSet = null;
              try {
                connection = dataSource.getConnection();
                statement = connection.prepareStatement(
                    "select id, name, type from Ingredient where id = ?");
                statement.setString(1, id);
                resultSet = statement.executeQuery();
                Ingredient ingredient = null;
                if(resultSet.next()) {
                   ingredient = new Ingredient(
                       resultSet.getString("id"),
                       resultSet.getString("name"),
                       Ingredient.Type.valueOf(resultSet.getString("type")));
                }
                return Optional.of(ingredient);
              } catch (SQLException e) {
                // ??? What should be done here ???
              } finally {
                if (resultSet != null) {
                  try {
                    resultSet.close();
                  } catch (SQLException e) {}
                }
                if (statement != null) {
                  try {
                    statement.close();
                  } catch (SQLException e) {}
                }
                if (connection != null) {
                  try {
                    connection.close();
                  } catch (SQLException e) {}
                }
              }
              return Optional.empty();
            }
```
            - ==这里其实可以用 _疯狂Java讲义_ 里面提到的== ((63bf6c48-0fba-45ab-85a0-c2d712743600)) ==里异常自动关闭的写法== [^try-with-resource]
```java
              private JdbcTemplate jdbcTemplate;
              public Optional<Ingredient> findById(String id) {
                List<Ingredient> results = jdbcTemplate.query(
                    "select id, name, type from Ingredient where id = ?",
                    this:mapRowToIngredient,
                    id);
                return results.size() == 0 ?
                        Optional.empty() :
                        Optional.of(results.get(0));
              }
              private Ingredient mapRowToIngredient(ResultSet row, int rowNum)
                  throws SQLException {
                return new Ingredient(
                    row.getString("id"),
                    row.getString("name"),
                    Ingredient.Type.valueOf(row.getString("type")));
              }
```
        - 3.1.1 调整领域对象以适应持久化
          - Lombok在编译时生成访问器(accessor)方法
        - 3.1.2 使用JdbcTemplate
          - `@Repository`
            description: 构造型(stereotype)注解, 其他如`@Controller`和`@Component`
          - `@Autowired`
            description: (From Spring 2.5, annotations-driven *Dependency Injection*) Allows Spring to resolve and inject collaborating beans into our bean.
            - 当类只有一个构造器的时候
              - Spring会隐式地通过该构造器的参数应用依赖的自动装配
            - 如果有一个以上的构造器 / 明确声明自动装配
              - 在构造器上添加注解
```java
              @Autowired
              public JdbcIngredientRepository(JdbcTemplate jdbcTemplate) {
                this.jdbcTemplate = jdbcTemplate;
              }
```
            - Field injection vs Constructor injection
              - > Constructor injection is actually recommended over field injection.
                  + clearly identified.
                  + dependencies can be final, which helps with robustness and thread-safety
                  + you don't need reflection to set the dependencies.
                via: [dependency injection - Spring @Autowire on Properties vs Constructor - Stack Overflow](https://stackoverflow.com/questions/40620000/spring-autowire-on-properties-vs-constructor)
```java
                class MyComponent {
                  private final MyCollaborator collaborator;
                  @Inject
                  public MyComponent(MyCollaborator collaborator) {
                    Assert.notNull(collaborator, "MyCollaborator must not be null!");
                    this.collaborator = collaborator;
                  }
                  public void myBusinessMethod() {
                    collaborator.doSomething();
                  }
                }
```
              - Field injection:
```
                ++ less code to write
                -- unsafe code
                 - more complicated to test
```
                Constructor injection:
```
                ++ safe code
                 - more code to write (see the hint to Lombok)
                 + easy to test
```
                via: [Oliver Drotbohm - Why field injection is evil](https://odrotbohm.de/2013/11/why-field-injection-is-evil/)
          - `query()`
            description: 接受查询所使用的SQL及Spring RowMapper的一个实现（用来将结果集中的每行数据映射为一个对象）; 以最终参数(final argument)的形式接收查询中所需的任意参数
          - 必须先将数据写入数据库，才能读取它
            - Cases  #chatGPT
              description: keep in mind that a database is a persistent storage, so any changes made to the data must be saved/committed to the database before it can be read back.
              - When data is updated: If you want to read the updated data, you must first write the updated data to the database. This is because the database will not reflect the updated data until it is written.
              - When data is deleted: Before reading data that has been deleted, you must first delete it from the database. This is because the data is not available for reading after it has been deleted.
              - When a transaction is used: In some cases, you may be using a database transaction to perform multiple operations together. In this case, you must write the data to the database as part of the transaction before reading it, so that the data is consistent and meets the requirements of the transaction.
              - When using a caching mechanism: Some systems use a caching mechanism to improve performance when reading data. In these systems, data may be temporarily stored in cache, so it's necessary to write the data to the database first, so it will be available in cache for reading.
        - 3.1.3 定义模式和预加载数据
          - ![](../../soul/assets/book_Spring_in_Action/19.png)
            - Taco_Order和Taco被视为同一个聚合(aggregate)的成员
              - Taco无法在Taco_Order环境之外存在
              - Taco_Order是聚合根(aggregate root)
                - Ingredient对象则是其聚合的唯一成员
                  - 通过Ingredient_Ref建立与Taco的引用关系
            - >[!note]
              > 聚合和聚合根是领域驱动设计的核心概念，这种设计方式提倡软件代码的结构和语言要与业务领域匹配。在Taco Cloud领域对象中只使用了一点领域驱动设计(Domain-Driven Design, DDD)的思想，但是DDD的内容远不止聚合和聚合根。如果想要了解这项技术的更多内容，请阅读该主题的开创性著作——Eric Evans的《领域驱动设计》
            - `Spring Boot` 启动自动加载模式 (`schema.sql`) 和数据(`data.sql`)
              description: `src/main/resources`, 每次启动都会重新执行
              - > The data.sql file is executed **each time** the spring-boot application is fired up. This means that if you have insert statements, they may cause an `org.h2.jdbc.JdbcSQLException`-exception, because the **data is already present** in the database. I am using an embedded H2 database, but the problem stays the same.
                via: [Spring Boot - Loading Initial Data - Stack Overflow](https://stackoverflow.com/questions/38040572/spring-boot-loading-initial-data)
        - 3.1.4 插入数据
          - `Class GeneratedKeyHolder`
            description: The standard implementation of the [`KeyHolder`](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/jdbc/support/KeyHolder.html) interface, to be used for holding auto-generated keys (as potentially returned by JDBC insert statements). Create an instance of this class for each insert operation, and pass it to the corresponding [`JdbcTemplate`](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/jdbc/core/JdbcTemplate.html) or [`SqlUpdate`](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/jdbc/object/SqlUpdate.html) methods.
            source: https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/jdbc/support/GeneratedKeyHolder.html
          - `Class PreparedStatementCreatorFactory`
            description: Helper class that efficiently **creates multiple PreparedStatementCreator objects with different parameters based on an SQL statement and a single set of parameter declarations**.
            source: https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/jdbc/core/PreparedStatementCreatorFactory.html
          - `Interface PreparedStatementCreator`
            description: One of the two central callback interfaces used by the JdbcTemplate class. **This interface creates a PreparedStatement given a connection, provided by the JdbcTemplate class.** Implementations are responsible for providing SQL and any necessary parameters. Implementations do not need to concern themselves with SQLExceptions that may be thrown from operations they attempt. The JdbcTemplate class will catch and handle SQLExceptions appropriately. A PreparedStatementCreator should also implement the SqlProvider interface if it is able to provide the SQL it uses for PreparedStatement creation. This allows for better contextual information in case of exceptions.
      - 使用Spring Data JDBC
        - 添加依赖
```xml
            <dependency>
              <groupId>org.springframework.boot</groupId>
              <artifactId>spring-boot-starter-data-jdbc</artifactId>
            </dependency>
```
        - 定义存储库接口
        - 为领域类添加持久化的注解, Spring Data JDBC才能知道如何持久化它们
          - `@Table`
          - `@Id`
        - 使用CommandLineRunner预加载数据
          - 在应用启动的时候执行一定的逻辑的 2 个函数式接口
            - `Interface CommandLineRunner`
            - `Interface ApplicationRunner`
            - 执行时机
              - 应用上下文和所有bean装配完毕之后、所有其他功能执行之前
            - 函数式接口
              - 在一个返回lambda表达式的方法上使用@Bean注解???
```java
                @Bean
                public CommandLineRunner dataLoader(IngredientRepository repo) {
                  return args -> {
                    repo.save(new Ingredient("FLTO", "Flour Tortilla", Type.WRAP));
                    repo.save(new Ingredient("COTO", "Corn Tortilla", Type.WRAP));
                    repo.save(new Ingredient("GRBF", "Ground Beef", Type.PROTEIN));
                    repo.save(new Ingredient("CARN", "Carnitas", Type.PROTEIN));
                    repo.save(new Ingredient("TMTO", "Diced Tomatoes", Type.VEGGIES));
                    repo.save(new Ingredient("LETC", "Lettuce", Type.VEGGIES));
                    repo.save(new Ingredient("CHED", "Cheddar", Type.CHEESE));
                    repo.save(new Ingredient("JACK", "Monterrey Jack", Type.CHEESE));
                    repo.save(new Ingredient("SLSA", "Salsa", Type.SAUCE));
                    repo.save(new Ingredient("SRCR", "Sour Cream", Type.SAUCE));
                  };
                }
```
            - 区别 -> 传递给各自run()方法的参数
              - `CommandLineRunner` 接受一个String类型的可变长度参数，代表传递给命令行的原始参数
              - `ApplicationRunner` 接受一个ApplicationArguments参数，其提供了访问已解析命令行组件参数的方法
            - 好处
              - 它们使用存储库来创建要持久化的对象，而不是使用SQL脚本
                - 这种方式对关系型数据库和非关系型数据库同样有效
        -          ---
          - `Spring Data`(伞形项目) 子项目 
            description: Spring Data为各种项目提供基于存储库规范接口自动创建存储库的特性, 很少（甚至没有）持久化相关的逻辑，只需要编写一个或多个存储库接口
            - Spring Data JDBC：对关系型数据库进行JDBC持久化。
            - Spring Data JPA：对关系型数据库进行JPA持久化。
            - Spring Data MongoDB：持久化到Mongo文档数据库。
            - Spring Data Neo4j：持久化到Neo4j图数据库。
            - Spring Data Redis：持久化到Redis键-值存储。
            - Spring Data Cassandra：持久化到Cassandra列存储数据库。
      - 使用Spring Data JPA (Java Persistence API) 持久化数据
        - 添加Spring Data JPA到项目中
          - ==如果想要使用不同的JPA实现，那么至少需要将Hibernate依赖排除出去，并将所选择的JPA库包含进来（？）==
            - > The Java Persistence API (JPA) is a specification for accessing, persisting, and managing data between Java objects/classes and a relational database. Hibernate is a popular implementation of JPA, but there are other implementations available, such as EclipseLink and OpenJPA.
              When you include the Hibernate dependency in your project, you are effectively telling the application to use Hibernate as the JPA implementation. If you later decide that you want to use a different implementation, such as EclipseLink, you will need to exclude the Hibernate dependency from your project. This is because **the application will continue to use Hibernate as the JPA implementation, even if you include the new implementation**.
              The reason for this is that the JPA specification mark: s a set of interfaces that must be implemented by any JPA provider. When an application is using JPA, it communicates with the database through these interfaces, not directly with the JPA provider.
              When you include the Hibernate dependency, it provides an implementation of the JPA interfaces, and it will be used by the application. If you want to use a different JPA provider, you must remove the Hibernate dependency, so that the application will not use it and can find and use the new JPA provider that you have added instead.
              In summary, if you want to use a different JPA implementation, you need to exclude the Hibernate dependency because the application is looking for the JPA interfaces and Hibernate is an implementation of it, so it will use that as default. If you want to use another provider, you need to let the application know that you are using another provider. #chatGPT
```xml
              <dependency>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-starter-data-jpa</artifactId>
                <exclusions>
                  <exclusion>
                      <groupId>org.hibernate</groupId>
                      <artifactId>hibernate-core</artifactId>
                  </exclusion>
                </exclusions>
              </dependency>
              <dependency>
                <groupId>org.eclipse.persistence</groupId>
                <artifactId>org.eclipse.persistence.jpa</artifactId>
                <version>2.7.6</version>
              </dependency>
```
        - 将领域对象标注为实体
          - `@Entity` from by `javax.persistence`
            description: 将 class 声明为JPA实体, id属性需要使用@Id注解，以便于将其指定为数据库中唯一标识该实体的属性
            - >[!note]
              > 这个@Id注解来自javax.persistence包，不是Spring Data在org.springframework.data.annotation包中所提供的@Id注解
          - `@ManyToMany`
          - `@OneToMany`
          - ---
          - `lombok`
            - `@NoArgsConstructor`
              description: generate a constructor with no parameters. If this is not possible (because of final fields), a compiler error will result instead, unless @NoArgsConstructor(force = true) is used, then all final fields are initialized with 0 / false / null. For fields with constraints, such as @NonNull fields, no check is generated,so be aware that these constraints will generally not be fulfilled until those fields are properly initialized later. Certain java constructs, such as hibernate and the Service Provider Interface require a no-args constructor. This annotation is useful primarily in combination with either @Data or one of the other constructor generating annotations.
            - `@RequiredArgsConstructor`
              description: generates a constructor with 1 parameter for each field that requires special handling. All non-initialized `final` fields get a parameter, as well as any fields that are marked as `@NonNull` that aren't initialized where they are declared. For those fields marked with `@NonNull`, an explicit null check is also generated. The constructor will throw a `NullPointerException` if any of the parameters intended for the fields marked with `@NonNull` contain `null`. The order of the parameters match the order in which the fields appear in your class.
            - `@AllArgsConstructor`
              description: generates a constructor with 1 parameter for each field in your class. Fields marked with `@NonNull` result in null checks on those parameters.
            - > Each of these annotations allows an alternate form, where the generated constructor is always private, and an additional static factory method that wraps around the private constructor is generated. This mode is enabled by supplying the `staticName` value for the annotation, like so: `@RequiredArgsConstructor(staticName="of")`. Such a static factory method will infer generics, unlike a normal constructor. This means your API users get write `MapEntry.of("foo", 5)` instead of the much longer `new MapEntry<String, Integer>("foo", 5)`.
              via: [@NoArgsConstructor, @RequiredArgsConstructor, @AllArgsConstructor](https://projectlombok.org/features/constructor)
        - 声明JPA存储库
        - 3.3.4 自定义JPA存储库
          - 生成存储库实现时，Spring Data会检查存储库接口的所有方法，解析方法的名称，并基于被持久化的对象来试图推测方法的目的
            - Spring Data定义了一组小型的领域特定语言(Domain-Specific Language, DSL)，持久化的细节都是通过存储库方法的签名来描述的
          - 存储库的方法公式: $动词 + 主题(subject) (optional) + By + 断言$
            - `findByDeliveryZip()`
              - 动词是find
              - 断言是DeliveryZip
              - 主题并没有指定，暗含的主题是TacoOrder
```java
              List<TacoOrder> readOrdersByDeliveryZipAndPlacedAtBetween(
                    String deliveryZip, Date startDate, Date endDate);
```
              - ![](../../soul/assets/book_Spring_in_Action/20.png)
              - 尽管主题是可选的，但是这里要查找的就是TacoOrder。Spring Data会忽略主题中大部分的单词，所以你可以将方法命名为 `readPuppiesBy...`，而它依然会去查找TacoOrder实体，因为CrudRepository是使用TacoOrder类进行参数化的
              - 断言是方法签名中最为有意思的一部分
                - deliveryZip属性的值必须要等于方法第一个参数传入的值
                - 关键字Between表明placedAt属性的值必须要位于方法最后两个参数的值之间
              - 除了Equals和Between操作之外, 还有
                - IsAfter、After、IsGreaterThan、GreaterThan；
                - IsGreaterThanEqual、GreaterThanEqual；
                - IsBefore、Before、 IsLessThan、LessThan；
                - IsLessThanEqual、LessThanEqual；
                - IsBetween、Between ；
                - IsNull、Null；
                - IsNotNull、NotNull；
                - IsIn、In；
                - IsNotIn、NotIn；
                - IsStartingWith、StartingWith、StartsWith；
                - IsEndingWith、EndingWith、EndsWith；
                - IsContaining、Containing、Contains；
                - IsLike、Like；
                - IsNotLike、NotLike；
                - IsTrue、True；
                - IsFalse、False；
                - Is、Equals；
                - IsNot、Not；
                - IgnoringCase、IgnoresCase
                  - 替代方案: 在方法上添加AllIgnoringCase或AllIgnoresCase，这样它就会忽略所有String对比的大小写
```java
                    List<TacoOrder> findByDeliveryToAndDeliveryCityAllIgnoresCase(
                            String deliveryTo, String deliveryCity);
```
              - 在方法名称的结尾处添加`OrderBy`，使结果集根据某个列排序
            - 更加复杂. 需要自定义的情况: `@Query` + SQL
```java
                @Query("Order o where o.deliveryCity = 'Seattle'")
                List<TacoOrder> readOrdersDeliveredInSeattle();
```
              - 区别
                - 自定义方法都需要 `@Query`
                  - 与JPA不同，我们没有映射元数据帮助Spring Data JDBC根据方法名自动推断查询
                - `@Query` 中声明的必须全部是SQL查询，不允许使用JPA查询。
        - More Examples via
          - [Spring Data JPA Many To Many Relationship Mapping Example](https://attacomsian.com/blog/spring-data-jpa-many-to-many-mapping)
```java
              package com.attacomsian.jpa.many2many.domains;
              import javax.persistence.*;
              import java.io.Serializable;
              import java.util.Set;
              @Entity
              @Table(name = "students")
              public class Student implements Serializable {
                @Id
                @GeneratedValue(strategy = GenerationType.IDENTITY)
                private Long id;
                private String name;
                private int age;
                private String grade;
                @ManyToMany(fetch = FetchType.LAZY, cascade = CascadeType.PERSIST)
                @JoinTable(name = "students_courses",
                  joinColumns = {
                  @JoinColumn(name = "student_id", referencedColumnName = "id",
                                         nullable = false, updatable = false)},
                  inverseJoinColumns = {
                  @JoinColumn(name = "course_id", referencedColumnName = "id",
                                         nullable = false, updatable = false)})
                private Set<Course> courses = new HashSet<>();
                public Student() {
                }
                public Student(String name, int age, String grade) {
                  this.name = name;
                  this.age = age;
                  this.grade = grade;
                }
                // getters and setters, equals(), toString() .... (omitted for brevity)
              }
```
    - 使用非关系型数据 [^CH04_DEBUG]
      - 4.1 使用Cassandra存储库
        - Cassandra
          description: 分布式、高性能、始终可用、最终一致、列分区存储的NoSQL数据库
          tags: TODO
          source: https://en.wikipedia.org/wiki/Apache_Cassandra); [Welcome to Apache Cassandra’s documentation! | Apache Cassandra Documentation](https://cassandra.apache.org/doc/latest/
          - 简单来讲，Cassandra
          - 处理的是要写入表中的数据行
            - 数据会被分区到一对多的分布式节点上
            - 没有任何一个节点会持有所有的数据
            - 任何给定的数据行都会跨多个节点保存副本，从而消除了单点故障
          - 提供了用于将应用的领域模型映射为后端数据库结构的注解
        - 4.1.1 启用Spring Data Cassandra
          - 2 个独立的Spring Data Cassandra starter依赖
            - 用于反应式的数据持久化
            - 用于标准的、非反应式的持久化
```xml
              <dependency>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-starter-data-cassandra</artifactId>
              </dependency>
```
```shell
            docker run --name my-cassandra --network cassandra-net -p 9042:9042 -d cassandra:latest    
             docker run -it --network cassandra-net --rm cas
            sandra cqlsh my-cassandra
            # Wait connecting
            cqlsh> create keyspace tacocloud with replication = {'class':'SimpleStrategy', 'replication_factor':1} and durable_writes = true;
             # 创建一个名为tacocloud的键空间
             # 配置其为简单副本和持久性写入
             # with replication 确定副本处理的方式
              # 副本因子设置为1，可以让Cassandra为每行数据保留一个副本
              # 对于单个数据中心来说，SimpleStrategy副本策略可以满足需求，但是如果Cassandra集群跨多个数据中心，那就应该考虑使用NetworkTopologyStrategy策略
```
          - 键空间
            description: Cassandra节点中表的一个分组，大致类似于关系型数据库中表、视图和约束关系的分组
        - 4.1.2 理解Cassandra数据模型
          - Cassandra表可以有任意数量的列，但是并非所有的行都需要使用这些列。
          - Cassandra数据库会被分割到多个分区中。特定表的任意行都可能会由一个或多个分区进行管理，但是不太可能所有的分区包含所有的行。
          - Cassandra表有两种类型的键
            - 分区键(partition key)
            - 集群键(clustering key)
          - Cassandra会对每行数据的分区键进行哈希操作以确定该行由哪些分区来进行管理。集群键用来确定数据行在分区中的顺序（不一定是它们在查询结果中的顺序）。请参考Cassandra文档，以了解Cassandra数据模型的更多知识，包括分区、集群和它们对应的键。
          - Cassandra对读操作进行了高度的优化。因此，非常常见和推荐的方式是让表保持高度非规范化(denormalized)，并且在多个表中重复存储数据。（例如，客户信息可能会保存在专门的客户表中，同时也会重复存储在订单的表中，来记录该客户所创建的订单。）
        - 4.1.3 为Cassandra持久化映射领域类型
        - 4.1.4 编写Cassandra存储库
      - 4.2 编写MongoDB存储库
        - MongoDB
          description: MongoDB会将文档存储为BSON（即二进制JSON）格式，它的查询和检索方式与在其他的数据库中查询数据的方式类似
          tags: #NoSQL
          description: Cassandra是一个列存储的数据库，而MongoDB则被视为文档数据库
        - 4.2.1 启用Spring Data MongoDB
          - 反应式场景 (via: ch13)
          - \* 非反应式场景
        - 4.2.2 将领域类型映射为文档
          - `@Id` from Spring Data Commons
            description: 指定某个属性为文档的ID
          - `@Document`
            description: 将领域类型声明为要持久化到MongoDB的文档。
          - `@Field`
            description: 声明在持久化存储的文档中该属性的字段名称（我们还可以选择性地配置顺序）
          - `@Transient`
            description: 声明该属性是否要进行持久化
          - 如果选择使用String属性作为ID，我们会享受到Mongo在保存时自动为其赋值的好处（假设它的值为null）。通过选择使用String，我们会有一个数据库管理的ID分配策略，不需要关心如何手动设置该属性的值。
        - 4.2.3 编写MongoDB存储库接口
      - 小结
    - 第5章 保护Spring [^CH05_SPRING_SECURITY]
      - 5.1 启用Spring Security
```xml
          <dependency>
              <groupId>org.springframework.boot</groupId>
              <artifactId>spring-boot-starter-security</artifactId>
          </dependency>
          <!--
          Using generated security password: b7aace4e-ae7f-460c-b7cc-949fa646a2eb
          This generated password is for development use only. Your security configuration must be updated before running your application in production.
          -->
```
        - >[!tip]
          > 使用隐身模式，在手动测试安全性的时候，将浏览器设置为私有或隐身模式是非常有用的。这能够确保每次打开私有/隐身窗口时，都会有一个新的会话。这样，我们每次都需要重新登录应用。这能够确保在安全方面做的任何变更都生效，不会有任何旧的会话残留，妨碍我们看到变更的效果。
        - 自动配置提供了什么类型的安全性？
          - 所有的HTTP请求路径都需要认证；
          - 不需要特定的角色和权限；
          - 认证过程是通过弹出一个简单的登录页实现的；
          - 系统只有一个用户，用户名为user
        - **Tagret**
          - 提供应用自己的登录页，其设计要与我们的Web站点相符；
          - 提供多个用户，并提供一个注册页面，使得Taco Cloud的新用户能够注册；
          - 对不同的请求路径执行不同的安全规则，比如主页和注册页面根本不需要进行认证；
      - 5.2 配置Spring Security
        - `interface PasswordEncoder`：密码转码器接口
          - BCryptPasswordEncoder
            description: 使用bcrypt强哈希加密
          - NoOpPasswordEncoder （避免在生产环境中使用）
            description: 不使用任何转码
          - Pbkdf2PasswordEncoder
            description: 使用PBKDF2加密
          - SCryptPasswordEncoder
            description: 使用Scrypt哈希加密
          - StandardPasswordEncoder（避免在生产环境中使用）
            description: 使用SHA-256哈希加密（不安全）
          - >[!note]
            > 不管是哪种密码转码器，数据库中的密码永远不会被解码；
            与解码过程相反，用户在登录时输入的密码将会使用相同的算法转码，并与数据库中已编码的密码进行对比
          - 这种对比是在PasswordEncoder的matches()方法中进行的
            ![idea64_150.png](../../soul/assets/book_Spring_in_Action/idea64_150_1675662652793_0.png)
        - `interface UserDetailsService`：认证功能配置用户存储
          - ![idea64_151.png](../../soul/assets/book_Spring_in_Action/idea64_151_1675663429171_0.png)
          - Spring Security提供了多个内置的UserDetailsService实现
            - 内存用户存储；
            - JDBC用户存储；
            - LDAP用户存储；
        - 5.2.1 基于内存的用户详情服务
        - 5.2.2 自定义用户认证
          - 定义用户领域对象和持久化
          - 创建用户详情服务
            - UserDetailsService只定义了一个名为loadUserByUsername()的方法，这意味着它是一个**函数式接口**，能够以lambda表达式的方式来实现，从而避免提供一个完整的实现类
          - 注册用户
      - 5.3 保护Web请求
        - 项目需求
          - 用户在设计taco和提交订单之前，必须要经过认证；
          - 主页、登录页和注册页应该对未认证的用户开放；
        - `class HttpSecurity`：拦截请求以确保用户具备适当的权限
          - 功能
            - 要求在为某个请求提供服务之前，满足特定的安全条件；
            - 配置自定义的登录页；
            - 使用户能够退出应用；
            - 预防跨站请求伪造；
        - 5.3.1 保护请求
          - 声明请求路径的安全需求的方法 (自我限制，写死的)
            - ![](../../soul/assets/book_Spring_in_Action/Chapter05_table_1.jpg)
            - 除此之外，我们还可以使用access()方法，通过为其提供SpEL表达式来声明更丰富的安全规则。Spring Security扩展了SpEL，包含多个安全相关的值和函数
            - ![](../../soul/assets/book_Spring_in_Action/Chapter05_table_2.jpg)
            - 例如，假设（基于某些疯狂的原因）我们只想允许具备ROLE_USER权限的用户在星期二创建新taco（不妨叫“taco星期二”），就可以重写表达式，如下的代码展现了已修改版本的SecurityFilterChain方法：
```java
                @Bean
                public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
                  return http
                    .authorizeRequests()
                      .antMatchers("/design", "/orders")
                         .access("hasRole('USER') && " +
                          "T(java.util.Calendar).getInstance().get(" +
                          "T(java.util.Calendar).DAY_OF_WEEK) == " +
                          "T(java.util.Calendar).TUESDAY")
                      .antMatchers("/", "/**").access("permitAll")
                    .and()
                    .build();
                }
```
        - 5.3.2 创建自定义的登录页
          - What is the use of for attribute in label tag?
            - The for attribute **specifies which form element a label is bound to**.
          - What is the use of name attribute in label tag?
            - The name attribute specifies the name of an <input> element. The name attribute is used **to reference elements in a JavaScript, or to reference form data after a form is submitted**.
          - 默认情况下，Spring Security会在“/login”路径监听登录请求，用户名和密码输入域的名称分别应为username和password。但这都是可配置的，举例来说，如下的配置自定义了路径和输入域的名称：
```java
            .and()
              .formLogin()
                .loginPage("/login")
                .loginProcessingUrl("/authenticate")
                .usernameParameter("user")
                .passwordParameter("pwd")
```
          - 默认情况下，登录成功之后，用户将会被导航到Spring Security决定让他们登录时他们正在浏览的页面。用户如果直接访问登录页，登录成功之后将会被导航至根路径（例如，主页）。但是，我们可以通过指定默认的成功页来更改这种行为
```java
            .and()
              .formLogin()
                .loginPage("/login")
                .defaultSuccessUrl("/design")
```
        - 5.3.3 启用第三方认证
```xml
            <dependency>
              <groupId>org.springframework.boot</groupId>
              <artifactId>spring-boot-starter-oauth2-client</artifactId>
            </dependency>
```
          - OAuth2
            description: 授权规范，但它也可以用来通过第三方网站实现认证功能；
          - OpenID Connect
            description: 另一个基于OAuth2的安全规范，用于规范化第三方认证过程中发生的交互；
        - 5.3.4 防止 _跨站请求伪造(Cross-Site Request Forgery, CSRF)_
          - 为了防止这种类型的攻击发生
            - 应用可以在展现表单的时候生成一个CSRF令牌(token)，并将其放到隐藏域中临时存储起来，以便后续在服务器上使用；
            - 提交表单时，令牌会与其他的表单数据一起发送至服务器端
            - 请求会被服务器拦截，并与最初生成的令牌对比
              - 如果令牌匹配，请求将会允许处理；
              - 否则就可以断定表单是由恶意网站渲染的，因为恶意网站不知道服务器所生成的令牌
          - 在Thymeleaf模板中，我们可以按照如下的方式在隐藏域中渲染CSRF令牌：
```html
              <input type = "hidden" name = "_csrf" th:value = "${_csrf.token}"/>
```
            - 在Thymeleaf中，只需要确保<form>元素的某个属性带有Thymeleaf的属性前缀
              - 包括上下文路径渲染 `@`；
          - 禁用Spring Security对CSRF的支持
```xml
              .and()
                .csrf()
                  .disable()
```
      - 5.4 实现方法级别的安全
        - `@PreAuthorize`
          description: 注解会接受一个SpEL表达式，如果表达式的计算结果为false，这个方法将不会被调用；如果表达式的计算结果为true，方法就允许调用
          - 要使@PreAuthorize发挥作用，需要启用全局的方法安全功能。为了实现这一点，需要使用@EnableGlobalMethodSecurity注解标注安全配置类
        - 如果判定安全的条件依赖于方法调用的返回值，那么该如何保证方法不被调用呢？
          - 这又是一个“先有鸡还是先有蛋”的问题，我们可以先允许方法调用，并在表达式返回值为false时抛出一个AccessDeniedException，从而解决这个难题。
      - 5.5 了解用户是谁
        - 有多种方式确定用户是谁，常用的方式如下：
          - 将java.security.Principal对象注入控制器方法；
          - 将org.springframework.security.core.Authentication对象注入控制器方法；
          - 使用org.springframework.security.core.context.SecurityContextHolder获取安全上下文；
          - 注入@AuthenticationPrincipal注解标注的方法参数（@AuthenticationPrincipal来自Spring Security的org.springframework.security.core.annotation包）
    - 第6章 使用 ==配置属性==(configuration property) by Spring Boot
      description: 为应用组件设置属性值；Spring应用上下文中带有@ConfigurationProperties注解的bean的属性；
      - 6.1 细粒度地调整自动配置
        - 两种不同（但相关）的配置
          - bean装配
            description: 声明在Spring应用上下文中创建哪些应用组件（即bean）以及它们之间如何互相注入的配置；
          - 属性注入
            description: 设置Spring应用上下文中bean的值的配置；
        - 6.1.1 理解Spring的环境抽象
          - Spring的环境抽象抽取原始的属性，这样需要这些属性的bean就可以从Spring本身中获取了；
          - Spring环境会拉取多个属性源，包括
            - JVM系统属性；
            - 操作系统环境变量；
            - 命令行参数；
            - 应用属性配置文件；
          - 各个属性源的属性流经Spring的环境抽象进入Spring bean；
            - ![](../../soul/assets/book_Spring_in_Action/24.png)
        - 6.1.2 配置数据源
```yml
            spring:
              datasource:
                url: jdbc:mysql://localhost/tacocloud
                username: tacouser
                password: tacopassword
                driver-class-name: com.mysql.jdbc.Driver
```
            - Spring Boot在自动化配置DataSource bean时，将会使用该连接。
            - 如果在类路径中存在HikariCP连接池，DataSource将使用该连接池；
              - 否则，Spring Boot会在类路径下尝试查找并使用如下的连接池实现：
                - Tomcat JDBC连接池；
                - Apache Commons DBCP2；
              - Offical Refer: ((63e13a7c-6d40-4f76-b974-3c91d4868bb2))
              - HikariCP连接池
                description: spring boot 的默认数据库连接池；虽然功能不及Druid，但是对于监控也有一定的扩展性，简单，快速，稳定是其胜出的原因；[^HIKARI_CP]
```yml
            spring:
              datasource:
                schema:
                - order-schema.sql
                - ingredient-schema.sql
                - taco-schema.sql
                - user-schema.sql
                data:
                - ingredients.sql
```
            - JNDI（Java Naming and Directory Interface）
              description: 配置数据源并让Spring去那里进行查找并配置数据源；
            - 在这种情况下，可以使用spring.datasource.jndi-name搭建自己的数据源：
```yml
              spring:
                datasource:
                  jndi-name: java:/comp/env/jdbc/tacoCloudDS
```
        - 6.1.3 配置嵌入式服务器
```yml
            server:
              port: 0
```
            - 自动化集成测试时非常有用，保证并发运行的测试不会与硬编码的端口号冲突；
          - 底层服务器的配置并不仅仅局限于端口，对常见的一项设置就是
          - 让底层容器处理HTTPS请求
            - 首先要使用JDK的keytool命令行工具生成keystore：
```shell
              $ keytool -keystore mykeys.jks -genkey -alias tomcat -keyalg RSA
```
              - 当提示输入密码的时候，需要我们记住所输入的密码
            - 接下来，我们需要设置一些属性，以便在嵌入式服务器中启用HTTPS
```yml
              server:
                port: 8443
                ssl:
                  key-store: file:///path/to/mykeys.jks
                  key-store-password: letmein
                  key-password: letmein
```
              - 我们将server.port设置为8443，在开发阶段，这是HTTPS服务器的常用选择；
              - `server.ssl.key-store` 属性应该设置为我们所创建的keystore文件的路径
                - `file://URL` 会在文件系统中加载
                - `classpath:URL` 将它打包到一个应用JAR文件中
        - 6.1.4 配置日志
          - Spring Boot默认通过Logback配置日志，日志会以INFO级别写入控制台
          - 在类路径的根目录下（`src/main/resources`）创建一个logback.xml文件.
```xml
              <configuration>
                <appender name = "STDOUT" class = "ch.qos.logback.core.ConsoleAppender">
                  <encoder>
                    <pattern>
                      %d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n
                    </pattern>
                  </encoder>
                </appender>
                <logger name="root" level="INFO"/>
                <root level="INFO">
                  <appender-ref ref="STDOUT" />
                </root>
              </configuration>
```
```diff
              2021-07-29 17:24:24.187 INFO 52240 --- [nio-8080-exec-1]
              ➥com.example.demo.Hello                 Here's a log entry.
              2021-07-29 17:24:24.187 INFO 52240 --- [nio-8080-exec-1]
              ➥com.example.demo.Hello                 Here's another log entry.
              2021-07-29 17:24:24.187 INFO 52240 --- [nio-8080-exec-1]
              ➥com.example.demo.Hello                 And here's one more.
              --------------------------------------------------------------------------
              17:25:09.088 [http-nio-8080-exec-1] INFO com.example.demo.Hello -
                                                       Here's a log entry.
              17:25:09.088 [http-nio-8080-exec-1] INFO com.example.demo.Hello -
                                                       Here's another log entry.
              17:25:09.088 [http-nio-8080-exec-1] INFO com.example.demo.Hello -
                                                       And here's one more.
```
          - >[!note]
            > logback.xml文件中都可以声明哪些内容超出了本书的范围。可以参考Logback的文档来了解更多信息
          - 设置日志级别
            - 假设我们想要将root logging设置为WARN级别
              但是希望将Spring Security的日志级别设置为DEBUG
```YML
              logging:
                level:
                  root: WARN
                  org.springframework.security: DEBUG
```
          - 假设我们想要将日志条目写入“/var/logs/”中的TacoCloud.log文件
```YML
              logging:
                file:
                  path: /var/logs/
                  file: TacoCloud.log
                level:
                  root: WARN
                  org:
                    springframework:
                      security: DEBUG
```
          - 默认情况下，日志文件一旦达到10 MB就会轮换
        - 6.1.5 使用特定的属性值
          - 假设（不管基于什么原因）我们想要设置一个名为greeting.welcome的属性
            - 它的值来源于名为spring.application.name的另一个属性
```YML
              greeting:
                welcome: You are using ${spring.application.name}.
```
      - 6.2 创建自己的配置属性
        - 对于在生产环境中需要快速更改的情况，我们可以将taco.orders.pageSize设置为环境变量，以避免重新构建和重新部署应用
```shell
          $ export TACO_ORDERS_PAGESIZE = 10
```
        - 6.2.1 定义配置属性的持有者
        - 6.2.2 声明配置属性元数据
          - 配置属性的元数据完全是可选的，它并不会妨碍配置属性的运行。但是，元数据会为配置属性提供一个最小化的文档，这是非常有用的，在IDE中尤为如此。
          - 为了帮助那些使用我们所定义的配置属性的人（有可能就是我们自己），为这些属性创建一些元数据是非常好的做法，至少能消除IDE上那些烦人的黄色警告。
          - Spring Boot灵活的属性命名功能允许出现属性名出现不同的变种，比如taco.orders.page-size等价于taco.orders.pageSize，所以它对使用不会产生太大的影响
      - 6.3 使用profile进行配置
        - 在生产环境，我们可以按照如下的方式将数据库配置属性设置为环境变量：尽管这种方式可以运行，但是如果配置属性比较多，将它们声明为环境变量会非常麻烦。除此之外，我们没有好的方式来跟踪环境变量的变化，也无法在出现错误的时候进行回滚。
        - profile是一种条件化的配置，在运行时，根据哪些profile处于激活状态，可以使用或忽略不同的bean、配置类和配置属性。
        - 我们需要做的就是定义一个profile，其中包含适用于生产环境的属性。
        - ---
        - 6.3.1 定义特定profile的属性
          - 定义 2 种
            - 创建另外一个YAML或属性文件，其中只包含用于生产环境的属性。文件的名称要遵守如下的约定：application-{profile名}.yml或 application-{profile名}.properties。
            - 定义特定profile相关的属性的另外一种方式仅适用于YAML配置。它会将特定profile的属性和非profile的属性都放到application.yml中。它们之间使用3个短线进行分割，并且使用spring.profiles属性来命名profile。按照这种方式定义生产环境的属性，等价的application.yml如下所示：
        - 6.3.2 激活profile
```yml
            spring:
              profiles:
                active:
                - prod
```
```shell
            % export SPRING_PROFILES_ACTIVE = prod
```
```shell
            % java -jar taco-cloud.jar --spring.profiles.active = prod
```
          - 我们可以设置多个激活的profile：
```yml
              spring:
                profiles:
                  active:
                  - prod
                  - audit
                  - ha
```
```shell
              % export SPRING_PROFILES_ACTIVE = prod,audit,ha
```
        - 6.3.3 使用profile条件化地创建bean
```java
            @Bean
            @Profile("dev")
            @Profile({"dev", "qa"})
            @Profile("!prod")
            @Profile({"!prod", "!qa"})
            public CommandLineRunner dataLoader(IngredientRepository repo,
                  UserRepository userRepo, PasswordEncoder encoder) {
              ...
            }
```
      - 小结
        - 设置配置属性的 5 种方式
          - 命令行参数
          - 环境变量
          - JVM系统属性
          - 属性文件
          - YAML文件
  - 第2部分 Spring集成
    - 第7章 创建REST服务（扩展了第2章对Spring MVC的讨论，介绍了如何在Spring中编写REST API）
      - 将用户界面推到更接近客户端的地方，而让服务器暴露API，通过这种API，各种客户端都能与后端功能交互。
      - 7.1 编写RESTful控制器
        - 从服务器中检索数据
          - 对基于JavaScript的用户界面来说（比如使用像Angular或ReactJS这样的框架所编写的用户界面），一种常见的方式是让它们运行在与API相独立的主机或端口上（至少目前是这样的），Web浏览器会阻止客户端消费该API。我们可以在服务端响应中添加跨域资源共享(Cross- Origin Resource Sharing, CORS)头信息来突破这一限制
        - 发送数据到服务器端
        - 在服务器上更新数据
        - 删除服务器上的数据
      - 7.2 启用数据后端服务
        - 调整资源路径和关系名称
        - 分页和排序
      - 7.3 消费REST服务
        - GET资源
        - PUT资源
        - DELETE资源
        - POST资源
      - 小结
    - 第8章 保护REST
      - 8.1 OAuth 2简介
        - 方案
          - ==HTTP Basic 认证==来保护“/ingredients”的端点
            - 通过为处理器方法添加@PreAuthorize来实现
```java
                @PostMapping
                @PreAuthorize("#{hasRole('ADMIN')}")
                public Ingredient saveIngredient(@RequestBody Ingredient ingredient){
                  return repo.save(ingredient);
                }
                @DeleteMapping("/{id}")
                @PreAuthorize("#{hasRole('ADMIN')}")
                public void deleteIngredient(@PathVariable("id") String ingredientId){
                  repo.deleteById(ingredientId);
                }
```
            - 或者安全配置来保护：
```java
                @Override
                protected void configure(HttpSecurity http) throws Exception {
                  http.authorizeRequests()
                      .antMatchers(HttpMethod.POST,
                                   "/ingredients").hasRole("ADMIN")
                      .antMatchers(HttpMethod.DELETE,
                                   "/ingredients/**").hasRole("ADMIN")
                      ...
                }
```
            - **缺点**
              - 信息重复，客户端和 API 共享用户凭证信息；
              - 凭据丢失，不安全；
          - Token
            - 支持流程
              - ==授权码授权(authorization code grant)== \=> JWT
                - ![](../../soul/assets/book_Spring_in_Action/30.png)
              - 隐式授权(implicit grant)
                - 与授权码授权类似，隐式授权会将用户的浏览器重定向到授权服务器，以获取用户的许可。但是，重定向回来时，不是在请求中提供授权码，而是在请求中==隐式授予访问令牌==。
                - 尽管这种方式是为了在浏览器中运行的JavaScript客户端设计的，但是一般不推荐使用这种方式。更好的方式是使用授权码授权
              - 用户凭证（或密码）授权（user credentials (password) grant）
                - 这种流程不会进行重定向，甚至可能不涉及Web浏览器。客户端应用会获取用户的凭证，并将它们直接替换成访问令牌。
                - 这个流程似乎很适合那些非浏览器客户端，但是现代应用通常更倾向于要求用户在浏览器中访问一个Web站点，并进行授权码授权，从而避免直接处理用户的凭证
              - 客户端凭证授权(client credentials grant)
                - 这个流程与用户凭证授权类似，只不过不是交换用户的凭证以获取访问令牌，而是客户端交换自己的凭证以获取访问令牌。但是，所授予的令牌仅限于执行一些不以用户为中心的操作，并且不能以用户的身份行事。
        - >[!note]
          > 是否要使用“ROLE_”前缀（授权角色）
          - 显式情况：
            - 如果选择使用hasAuthority()来替代hasRole()，则需要传入“ROLE_ADMIN”，而不是“ADMIN”
      - 8.2 创建授权服务器
      - 8.3 使用资源服务器保护API
      - 8.4 开发客户端
      - 小结
    - 第9章 发送异步消息（接收Java Message Service(JMS)、RabbitMQ和Kafka的消息）
      description: 异步消息是一个应用程序向另一个应用程序间接发送消息的一种方式，这种间接性能够为通信的应用带来更松散的耦合和更大的可伸缩性。
      - 9.1 使用JMS (Java Message Service, Java消息服务)发送消息
        - 9.1.1 搭建JMS环境
        - 9.1.2 使用JmsTemplate发送消息
        - 9.1.3 接收JMS消息
      - 9.2 使用 RabbitMQ 和 AMQP (Advanced Message Queueing Protocol, AMQP)
        - 9.2.1 添加RabbitMQ到Spring中
        - 9.2.2 通过RabbitTemplate发送消息
        - 9.2.3 接收来自RabbitMQ的消息
      - 9.3 使用 Kafka by Apache的消息
        - 9.3.1 为Spring搭建支持Kafka消息的环境
        - 9.3.2 通过KafkaTemplate发送消息
        - 9.3.3 编写Kafka监听器
      - Apache ActiveMQ
```
          <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-activemq</artifactId>
          </dependency>
```
        - >[!note]
          > ActiveMQ代理不是分别设置代理的主机和端口，而是使用了一个名为spring.activemq.broker-url的属性来指定代理的地址。URL应该是“tcp://”协议的地址
          - 在本地开发运行时，都不需要配置这些属性。
        - >[!note]
          > 使用ActiveMQ时，则需要将spring.activemq.in-memory属性设置为false，防止Spring启动内存中运行的代理。内存中运行的代理看起来很有用，但是只有在同一个应用中发布和消费消息的情况下，才能使用它（这限制了它的用途）。
      - ActiveMQ Artemis
```
          <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-artemis</artifactId>
          </dependency>
```
```java
        // 发送原始的消息
        void send(MessageCreator messageCreator)
          throws JmsException;
        void send(Destination destination, MessageCreator messageCreator)
          throws JmsException;
        void send(String destinationName, MessageCreator messageCreator)
          throws JmsException;
        // 发送根据对象转换而成的消息
        void convertAndSend(Object message)
          throws JmsException;
        void convertAndSend(Destination destination, Object message)
          throws JmsException;
        void convertAndSend(String destinationName, Object message)
          throws JmsException;
        // 发送根据对象转换而成的消息，且带有后期处理的功能
        void convertAndSend(Object message, MessagePostProcessor
          postProcessor) throws JmsException;
        void convertAndSend(Destination destination, Object message,
          MessagePostProcessor postProcessor) throws JmsException;
        void convertAndSend(String destinationName, Object message,
          MessagePostProcessor postProcessor) throws JmsException;
```
        - 注意：
          - 3个send()方法都需要MessageCreator来生成Message对象；
          - 3个convertAndSend()方法会接受Object对象，并且会在幕后自动将Object转换为Message；
        - 3个convertAndSend()会自动将Object转换为Message，但同时还能接受一个MessagePostProcessor对象，用来在发送之前对Message进行自定义。
      - 这3种方法分类都分别包含3个重载方法，它们的区别在于指定JMS目的地（队列或主题）的方式：
        - 有1个方法不接受目的地参数，它会将消息发送至默认的目的地；
        - 有1个方法接受Destination对象，该对象指定了消息的目的地；
        - 有1个方法接受String，它通过名字的形式指定了消息的目的地。
      - RabbitMQ和AMQP
      - 交换机
        description: 负责将消息路由到一个或多个队列中，这个过程会基于交换机的类型、交换机与队列间的绑定，以及消息的路由键进行。
        - 具体类型：
          - Default
            - 这是代理创建的特殊交换机。它会将消息路由至名字与消息的路由键相同的队列。所有的队列都会自动绑定至Default类型的交换机。
          - Direct
            - 如果消息的路由键与队列的绑定键相同，消息会路由到该队列上。
          - Topic
            - 如果消息的路由键与队列的绑定键（可能会包含通配符）匹配，消息会路由到一个或多个这样的队列上。
          - Fanout
            - 不管路由键和绑定键是什么，消息都会路由到所有绑定队列上。
          - Headers
            - 与Topic类型类似，只不过要基于消息的头信息进行路由，而不是路由键。
          - Dead letter
            - 捕获所有无法投递（也就是它们无法匹配所有已定义的交换机和队列的绑定关系）的消息。
```
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-amqp</artifactId>
        </dependency>
```
        - 这样会为我们创建一个AMQP连接工厂、RabbitTemplate bean及其他支撑组件。
          - 要使用Spring发送和接收RabbitMQ代理的消息，只需要添加这项依赖。
        - >[!note]
          > 对于开发来说，我们可能会使用不需要认证的RabbitMQ代理，但是当应用程序投入生产环境时，它们无疑是非常有用的。
      - 小结
    - 第10章 Spring集成（实时处理数据、定义集成流，以及与外部系统（如电子邮件和文件系统）集成的功能）
      - 10.1 声明一个简单的集成流
      - 10.1.1 使用XML定义集成流
      - 10.1.2 使用Java配置集成流
      - 10.1.3 使用Spring Integration的DSL配置
      - 10.2 Spring Integration功能概览
      - 10.2.1 消息通道
      - 10.2.2 过滤器
      - 10.2.3 转换器
      - 10.2.4 路由器
      - 10.2.5 切分器
      - 10.2.6 服务激活器
      - 10.2.7 网关
      - 10.2.8 通道适配器
      - 10.2.9 端点模块
      - 10.3 创建电子邮件集成流
      - 小结
  - 第3部分 反应式Spring
    - 第11章 理解反应式编程
      - 11.1 反应式编程概览
      - 定义反应式流
      - 11.2 初识Reactor
      - 11.2.1 绘制反应式流图
      - 11.2.2 添加Reactor依赖
      - 11.3 使用常见的反应式操作
      - 11.3.1 创建反应式类型
      - 11.3.2 组合反应式类型
      - 11.3.3 转换和过滤反应式流
      - 11.3.4 在反应式类型上执行逻辑操作
      - 小结
    - 第12章 开发反应式API
      - 12.1 使用Spring WebFlux
      - 12.1.1 Spring WebFlux简介
      - 12.1.2 编写反应式控制器
      - 12.2 定义函数式请求处理器
      - 12.3 测试反应式控制器
      - 12.3.1 测试GET请求
      - 12.3.2 测试POST请求
      - 12.3.3 使用实时服务器进行测试
      - 12.4 反应式消费REST API
      - 12.4.1 获取资源
      - 12.4.2 发送资源
      - 12.4.3 删除资源
      - 12.4.4 处理错误
      - 12.4.5 交换请求
      - 12.5 保护反应式Web API
      - 12.5.1 配置反应式Web应用的安全性
      - 12.5.2 配置反应式的用户详情服务
      - 小结
    - 第13章 反应式持久化数据
      - 13.1 使用R2DBC
      - 13.1.1 为R2DBC定义领域实体
      - 13.1.2 定义反应式存储库
      - 13.1.3 测试R2DBC存储库
      - 13.1.4 定义OrderRepository的聚合根服务
      - 13.2 反应式地持久化MongoDB文档数据
      - 13.2.1 定义领域文档类型
      - 13.2.2 定义反应式MongoDB存储库
      - 13.2.3 测试反应式MongoDB存储库
      - 13.3 反应式地持久化Cassandra数据
      - 13.3.1 定义使用Cassandra持久化的领域类
      - 13.3.2 创建反应式Cassandra存储库
      - 13.3.3 测试反应式Cassandra存储库
      - 小结
    - 第14章 使用RSocket
      - 14.1 RSocket概览
      - 14.2 创建简单的RSocket服务器和客户端
      - 14.2.1 使用请求-响应通信模型
      - 14.2.2 处理请求-流的消息
      - 14.2.3 发送即发即忘的消息
      - 14.2.4 双向发送消息
      - 14.3 通过WebSocket传输RSocket
      - 小结
  - 第4部分 部署Spring
    - 第15章 使用Spring Boot Actuator
      - 15.1 Actuator概览
      - 15.1.1 配置Actuator的基础路径
      - 15.1.2 启用和禁用Actuator端点
      - 15.2 消费Actuator端点
      - 15.2.1 获取应用的基础信息
      - 15.2.2 查看配置细节
      - 15.2.3 查看应用的活动
      - 15.2.4 挖掘应用运行时的指标
      - 15.3 自定义Actuator
      - 15.3.1 为“/info”端点提供信息
      - 15.3.2 实现自定义的健康指示器
      - 15.3.3 注册自定义的指标
      - 15.3.4 创建自定义的端点
      - 15.4 确保Actuator的安全
      - 小结
    - 第16章 管理Spring
      - 16.1 使用Spring Boot Admin
      - 16.1.1 创建Admin服务器
      - 16.1.2 注册Admin客户端
      - 16.2 探索Admin服务器
      - 16.2.1 查看应用基本的健康状况和信息
      - 16.2.2 观察核心指标
      - 16.2.3 探查环境属性
      - 16.2.4 查看和设置日志级别
      - 16.3 保护Admin服务器
      - 16.3.1 为Admin服务器启用登录功能
      - 16.3.2 为Actuator启用认证
      - 小结
    - 第17章 使用JMX监控Spring
      - 17.1 使用Actuator MBean
      - 17.2 创建自己的MBean
      - 17.3 发送通知
      - 小结
    - 第18章 部署Spring
      - 18.1 权衡各种部署方案
      - 18.2 构建可执行JAR文件
      - 18.3 构建容器镜像
      - 18.3.1 部署至Kubernetes
      - 18.3.2 启用优雅关机功能
      - 18.3.3 处理应用程序的存活和就绪状态
      - 18.4 构建和部署WAR文件
      - 18.5 以终为始
      - 小结
## Comment
  - Fuck 异步社区, Download resource need account
  -    >[!note]
    > [Spring Boot 3.0 requires Java 17 as a minimum version.](https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-3.0-Release-Notes), so the version of java in `pom.xml` always stay java17. Uninstall IDEA is not work as well.
    - [Maven Repository: org.springframework.boot » spring-boot » 2.7.7](https://mvnrepository.com/artifact/org.springframework.boot/spring-boot/2.7.7)
  - [java - Plugin 'org.springframework.boot:spring-boot-maven-plugin:' not found - Stack Overflow](https://stackoverflow.com/questions/64639836/plugin-org-springframework-bootspring-boot-maven-plugin-not-found)
```xml
      <plugin>
          <groupId>org.springframework.boot</groupId>
          <artifactId>spring-boot-maven-plugin</artifactId>
          <version>${project.parent.version}</version>
      </plugin>
```
    - But Why???
## Implement
[^try-with-resource]: via: [Java使用Try with resources自动关闭资源 - BarryW - 博客园](https://www.cnblogs.com/barrywxx/p/9993005.html)
  -    [^CH02_DEBUG]: SB
    - [Fake Credit Card Generator | CreditCardValidator](https://www.creditcardvalidator.org/generator)
  -    [^CH03_DEBUG]: JPA
    - [x] #todo  JDBC JPA 中我无法理解 `TACO_ORDER_TACOS` 这张关联表是怎么创建起来的  
      - http url: http://localhost:8080/h2-console
      - jdbc url: `jdbc:h2:mem:tacocloud`
        - 默认密码为空
      - ![chrome_70.png](../../soul/assets/book_Spring_in_Action/chrome_70_1674024862725_0.png)
      - 事实是, 代码中只声明了三个实体, 然后在实体中有关联关系的 Field 中都设置了 `@OneToMany` 一类的注释, 然后我们看生成的表
        - `TACO_INGREDIENTS`
        - `TACO_ORDER`
        - `TACO_ORDER_TACOS`
        - 所以原项目的 `TACO_ORDER_Refs` 其实有点多余, 所以删掉了
    - [ ] #wait ch01 & ch02 alway `alter table Ingredient_Ref add foreign key (ingredient) references Ingredient(id); nested exception is org.h2.jdbc.JdbcSQLSyntaxErrorException: Constraint "PRIMARY KEY | UNIQUE (ID)" not found; SQL statement`  
      - [ ] #wait 说实话, 我实在搞不明白他怎么跑起来来的, 他 Github 仓库里面多了好几个类, 并且用到了后面讲的注释, 如`@AllArgsConstructor`  
```
        initialization - cancelling refresh attempt: org.springframework.beans.factory.UnsatisfiedDependencyException: Error creating bean with name 'jdbcIngredientRepository' mark: d in file [/mnt/c/Users/15517/Desktop/taco-cloud/target/classes/tacos/data/JdbcIngredientRepository.class]: Unsatisfied dependency expressed through constructor parameter 0; nested exception is org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'dataSourceScriptDatabaseInitializer' mark: d in class path resource [org/springframework/boot/autoconfigure/sql/init/DataSourceInitializationConfiguration.class]: Invocation of init method failed; nested exception is org.springframework.jdbc.datasource.init.ScriptStatementFailedException: Failed to execute SQL script statement #6 of URL [file:/mnt/c/Users/15517/Desktop/taco-cloud/target/classes/schema.sql]: alter table Ingredient_Ref add foreign key (ingredient) references Ingredient(id); nested exception is org.h2.jdbc.JdbcSQLSyntaxErrorException: Constraint "PRIMARY KEY | UNIQUE (ID)" not found; SQL statement:
        alter table Ingredient_Ref add foreign key (ingredient) references Ingredient(id) [90057-214]
```
    - [ ] #wait Auto complete static package import  
      - [java - IntelliJ Static Import Completion - Stack Overflow](https://stackoverflow.com/questions/4387134/intellij-static-import-completion)
      - [java - Eclipse Optimize Imports to Include Static Imports - Stack Overflow](https://stackoverflow.com/questions/288861/eclipse-optimize-imports-to-include-static-imports)
  -    [^CH03_TEST]: Test via: https://github.com/habuma/spring-in-action-6-samples/blob/main/ch03/tacos-sd-jpa
    - `@SpringBootTest(webEnvironment= SpringBootTest.WebEnvironment.RANDOM_PORT)`
      - ((63d244b1-8572-4263-8d21-197decff603c))
      - Refer the above, `@ExtendWith(SpringExtension.class)` is no need
    - `@ExtendWith` by Junit
      description: @ExtendWith is **a repeatable annotation that is used to register extensions for the annotated test class, test interface, test method, parameter, or field**. Annotated parameters are supported in test class constructors, in test methods, and in @BeforeAll , @AfterAll , @BeforeEach , and @AfterEach lifecycle methods. via: [ExtendWith (JUnit 5.8.0 API)](https://junit.org/junit5/docs/5.8.0/api/org.junit.jupiter.api/org/junit/jupiter/api/extension/ExtendWith.html)
    - `@MockBean`
      description: Spring Boot includes a @MockBean annotation that can be used to description:  a Mockito mock for a bean inside your ApplicationContext.
      - Mockito
        description: **一种Java Mock 框架，他主要就是用来做Mock 测试的**，它可以模拟任何Spring 管理的Bean、模拟方法的返回值、模拟抛出异常等等，同时也会记录调用这些模拟方法的参数、调用顺序，从而可以校验出这个Mock 对象是否有被正确的顺序调用，以及按照期望的参数被调用 via: [Mockito 简介- satire - 博客园](https://www.cnblogs.com/satire/p/14846492.html)
      - via: ((63d38953-fce4-471c-990e-98f98b614547))
    - `Class MediaType` -> Internet Media Types
      - Media type
        aliases: MIME type, Content type, 互联网媒体类型, MIME类型, 内容类型
        description: a two-part identifier for file formats and format contents transmitted on the Internet
        source: https://en.wikipedia.org/wiki/Media_type); Postel, J., [Media Type Registration Procedure](https://www.ietf.org/rfc/rfc1590.txt) , RFC 1590, November 1996
        - 一个MIME类型至少包括两个部分：一个*类型（type）*和一个*子类型（subtype）*
          它还可能包括一个或多个*可选参数（optional parameter）*
        - `type "/" [tree "."] subtype ["+" suffix]* [";" parameter]`
          - `type`
            - `application`
            - `audio`
            - `image`
            - `message`
            - `multipart`
            - `text`
            - `video`
            - Since November 1996
            - `font`
            - `example`
            - `model`
            - Since December 2020
          - `subtype`
            - typically consists of a **media format**, but it may or must also contain other content, such as **a tree prefix, producer, product or suffix**, according to the different rules in registration trees.
          - Types, subtypes, and parameter names are case-insensitive.
            Parameter values are usually case-sensitive
          - >[!example]
            > text/html; charset=UTF-8
            - `text` is the type
            - `html` is the subtype
            - `charset=UTF-8` is an optional parameter indicating the character encoding.
### More
              - `application/ld+json`
                - **JavaScript Object Notation for Linked Data**
                  via: [A Guide to JSON-LD for Beginners - Moz](https://moz.com/blog/json-ld-for-beginners)
              - `application/msword` (.doc)
              - `application/vnd.api+json`
              - `application/vnd.ms-excel` (.xls)
              - `application/vnd.ms-powerpoint` (.ppt)
              - `application/vnd.oasis.opendocument.text` (.odt)
              - `application/vnd.openxmlformats-officedocument.presentationml.presentation` (.pptx)
              - `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` (.xlsx)
              - `application/vnd.openxmlformats-officedocument.wordprocessingml.document` (.docx)
              - `application/zstd` (.zst)
              - When make a post request, encode the data that forms
                via: [html - What does enctype='multipart/form-data' mean? - Stack Overflow](https://stackoverflow.com/questions/4526273/what-does-enctype-multipart-form-data-mean)
                - HTML forms provide [three methods of encoding](https://www.w3.org/html/wg/spec/association-of-controls-and-forms.html#attr-fs-enctype).
                  - `application/x-www-form-urlencoded` (the default)
                    - be more efficient than 2
                  - `multipart/form-data`
                    - when your form includes any `<input type="file">` elements
                  - `text/plain` (Except for [debugging](http://www.w3.org/TR/html5/forms.html#text/plain-encoding-algorithm), Never use)
      - via: [MediaType (Java EE 6 )](https://docs.oracle.com/javaee/6/api/javax/ws/rs/core/MediaType.html) & [HTTP/1.1: Protocol Parameters](https://www.w3.org/Protocols/rfc2616/rfc2616-sec3.html#sec3.7)
    - `@DataJpaTest`
    - `@BeforeAll` 相当于构造函数吗?
  - 非关系数据库 [^CH04_DEBUG]
    - [x] #todo  WSL Docker 占用过高, `sudo dockerd` + `run docker` 容器之后占用达到了 5G, 再加上 Logseq, IDEA 和 Chrome 占用已经远超 16G 了. 所以 Cassandra 的实践暂时搁置吧  
      - 我发现是自己的上个项目（TTRSS）随着DOCKER启动也自启动了，随后内存占有就来到了1G上下的地步，使用命令停止部署即可
```shell
         $ sudo docker-compose -f ~/ttrss/docker-compose.yml stop
```
    - [x] #todo  [@EnableAutoConfiguration(exclude =...) on tests failed in Spring Boot 2.6.0 - Stack Overflow](https://stackoverflow.com/questions/70047380/enableautoconfigurationexclude-on-tests-failed-in-spring-boot-2-6-0)  
      - Since SB 2.6, Embeded mongodb needs the version must.
      - > To use embedded mongo, the spring.mongodb.embedded.version property must now be set. This helps to ensure that the MongoDB version that is used by the embedded support matches the MongoDB version that your application will use in production.
        via: [Spring Boot 2.6 Release Notes · spring-projects/spring-boot Wiki](https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-2.6-Release-Notes#embedded-mongo)
    - [ ] #wait I don't know why my entity field cannot be set `final`.  
      - It throws error `Cannot set property id because no setter`. Okey, the properties cannot changed when set final. But why they need to set when the page load?
      - How does they work?
  -    [^CH05_SPRING_SECURITY]: Spring 安全
    - 用这个工具检查了下 SQL 也没问题，后来金国几十分钟的排错，发现是 SB 大版本的问题
      via: [hibernate - Tests failing when upgrading to Spring Boot 2.7 - "CommandAcceptanceException: Error executing DDL" - Stack Overflow](https://stackoverflow.com/questions/72546596/tests-failing-when-upgrading-to-spring-boot-2-7-commandacceptanceexception-e)
      - [EverSQL | Automatic SQL Query Optimization for MySQL & PostgreSQL](https://www.eversql.com/)
    - 同时发现 #wsl 其实没有那么方便，因为我用 Windows 的环境运行了一下作者写的项目；然后停下来再运行我的，发现就访问不到了，最后还是用 WSL 的 IP 访问的；
      - 然后我发现 WSL 的IP 需要去 WSL 里面去找 😂；Windows 里面的 IP 是访问不到 Linux 的；
        - Emmmm🤔, 有点复杂
    - Kill port in windows via: https://stackoverflow.com/questions/56499928
```shell
        > netstat -ano | findstr *<port used>*
          TCP    0.0.0.0:*<port used>*  0.0.0.0:0              LISTENING       *<pid>*
          TCP    [:]:*<port used>*     [:]:0                 LISTENING       *<pid>*
        > taskkill /F /PID *<pid>*
        SUCCESS: The process with PID *<pid>* has been terminated.
```
    - Kill port in linux via: https://stackoverflow.com/questions/11583562
```shell
        fuser 8080/tcp
        fuser -k 8080/tcp
```
  - Spring Configuration Property
[^HIKARI_CP]: Via: [深入浅出HikariCP数据库连接池 - 掘金](https://juejin.cn/post/7039896653532233742)
    - @AuthenticationPrincipal
      description: Annotation that is used to resolve Authentication.getPrincipal() to a method argument.
      - 拿到当前会话的用户
        via: ((63e273ec-8e1b-445e-af31-f654ce5df0ca))
    - Error: `Spring Configuration Annotation Processor not configured`
      - via: [Configuration Metadata](https://docs.spring.io/spring-boot/docs/2.7.7/reference/html/configuration-metadata.html#appendix.configuration-metadata.annotation-processor)
    - Tips: `Re-run Spring Boot Configuration Annotation Processor to update generated metadata`
  - Spring Annotation
    - ((6454d3c0-bdea-4061-879d-813ab8b61927))
      - ((6454d495-c37d-467b-9d1c-d17e8d14ddf3))
      - ((6454d49b-6373-495c-95ec-ad764fca3ea5))
    - ((6454d4a5-e090-42a3-b441-e7d0523dcd5d))
    - [RequestMapping (Spring Framework 6.0.8 API)](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/web/bind/annotation/RequestMapping.html#produces())
      - consumes vs produces
        - [java - What is produce and consume in @Request Mapping - Stack Overflow](https://stackoverflow.com/questions/33591574/what-is-produce-and-consume-in-request-mapping)
        - 服务端生产(Produces)，客户端消费(Consume)，就是这么简单；
      - path == value vs params
        - 前者做路劲映射，后者做参数映射
  - Spring REST
    - ((6454d5ed-e408-4807-9042-28dd4fa6db8f))
      Spring Boot 默认禁用后缀匹配
  - Different package: `org.springframework.data.domain.Pageable;` & `java.awt.print.Pageable`;
## Reference
  - ~~How to download [Spring Framework 6.0.8 API](https://docs.spring.io/spring-framework/docs/current/javadoc-api/index.html) to PDF？~~
    - **Seem the official is not provide this option**
```
      [DIR] javadoc-api/            2023-04-13 08:28    -
      [DIR] kdoc-api/               2023-04-13 08:29    -
      [DIR] reference/              2023-04-13 08:29    -
```
      [Index of /spring-framework/docs/current](https://docs.spring.io/spring-framework/docs/current/)
    - And what's difference with Javadoc and reference?
      - Javadoc is more details than reference?
  - ![Spring Framework Document v6.0.8](../../soul/assets/doc_spring_framework_6.0.8.pdf)
  - ![Spring Boot Reference Document v3.0.2](../../soul/assets/doc_spring-boot-reference_1674720393793_0.pdf)
  - ![Spring Security Reference Document v3.0.8](../../soul/assets/doc_springsecurity_3.0.8.pdf)
-