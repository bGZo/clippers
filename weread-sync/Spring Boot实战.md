---
doc_type: weread-highlights-reviews
bookId: "26211867"
reviewCount: 0
noteCount: 14
author:
  - 克雷格·沃斯
  - 人民邮电出版社
cover: https://cdn.weread.qq.com/weread/cover/43/YueWen_26211867/t7_YueWen_26211867.jpg
readingStatus: 读过
progress: 42%
totalReadDay: 4
readingTime: 0小时23分钟
readingDate: 2022-05-17
title: Spring Boot实战
published: 2016-09-05 00:00:00
description: Spring改变了企业级Java应用开发方式，让Java开发更简单、高效；Spring Boot作为Spring开发的黄金助手，则在这个基础上，让开发者的生活更上一个台阶！本书是Spring Boot的终极指南，以自动配置、起步依赖、命令行界面和Actuator这四个核心特性为基础，深入介绍Spring Boot的用法，让所有Java开发人员不费吹灰之力就构建出满足生产需求的服务，真正享受技术达人的乐趣！- 掌握自动配置和起步依赖，学会用很少的显示配置构建完整的Spring应用程序  - 了解如何为Spring Boot应用程序编写自动化集成测试  - 开发Spring Boot CLI应用程序  - 探秘Actuator的Web端点、远程shell和JMX MBean  - 自如部署各种Spring Boot应用程序。
isbn: 9787115433145
tags:
  - weread/计算机-编程设计
type: weread-notes
weread: https://weread.qq.com/web/reader/8f232240718ff61b8f23d5e

---


## 封面

## 版权信息

## 数字版权声明

## 作者简介

## 版权声明

## 译者序

## 序

## 前言

## 关于本书

## 致谢

## 第1章 入门

### 1.1 Spring风云再起

> [!NOTE] 
> ❑ 自动配置：针对很多Spring应用程序常见的应用功能，Spring Boot能自动提供相关配置。❑ 起步依赖：告诉Spring Boot需要什么功能，它就能引入需要的库。❑ 命令行界面：这是Spring Boot的可选特性，借此你只需写代码就能完成完整的应用程序，无需传统项目构建。❑ Actuator：让你能够深入运行中的Spring Boot应用程序，一探究竟。
> 
> 2022-07-27 11:25:52 ^26211867-12-3361-3720

> [!NOTE] 
> 这两个Bean配置方法都不复杂，也不是很长，但它们只是典型Spring应用程序配置的一小部分。除此之外，还有无数Spring应用程序有着完全相同的方法。所有需要用到嵌入式数据库和JdbcTemplate的应用程序都会用到那些方法。简而言之，这就是一个样板配置
> 
> 2022-07-27 11:27:07 ^26211867-12-4764-4893

> [!NOTE] 
> 你无需操心那些Bean的配置，Spring Boot会做好准备，随时都能将其注入到你的Bean里
> 
> 2022-07-27 11:27:44 ^26211867-12-5114-5162

### 1.2 Spring Boot入门

### 1.3 小结

## 第2章 开发第一个应用程序

### 2.1 运用Spring Boot

### 2.2 使用起步依赖

### 2.3 使用自动配置

### 2.4 小结

## 第3章 自定义配置

### 3.1 覆盖Spring Boot自动配置

> [!NOTE] 
> 你会希望修改Spring Security的一些配置，至少要有一个好看一些的登录页，还要有一个基于数据库或LDAP（Lightweight Directory Access Protocol）用户存储的身份验证服务
> 
> 2022-07-24 19:15:10 ^26211867-21-2053-2160

> [!NOTE] 
> 覆盖自动配置很简单，就当自动配置不存在，直接显式地写一段配置。这段显式配置的形式不限，Spring支持的XML和Groovy形式配置都可以。
> 
> 2022-07-24 19:20:12 ^26211867-21-2336-2406

> [!NOTE] 
> 在Spring Security的场景下，这意味着写一个扩展了WebSecurityConfigurerAdapter的配置类。代码清单3-1中的SecurityConfig就是我们需要的东西
> 
> 2022-07-24 19:21:00 ^26211867-21-2460-2556

> [!NOTE] 
> Spring Security为身份认证提供了众多选项，后端可以是JDBC（Java Database Connectivity）、LDAP和内存用户存储。在这个应用程序中，我们会通过JPA用数据库来存储用户信息。第二个configure()方法设置了一个自定义的UserDetailsService，这个服务可以是任意实现了UserDetailsService的类，用于查找指定用户名的用户
> 
> 2022-07-24 19:24:40 ^26211867-21-3214-3410

> [!NOTE] 
> Spring Data JPA
> 
> 2022-07-24 19:25:12 ^26211867-21-3460-3475

### 3.2 通过属性文件外置配置

### 3.3 定制应用程序错误页面

### 3.4 小结

## 第4章 测试

### 4.1 集成测试自动配置

> [!NOTE] 
> Spring提供了额外的辅助功能，比如组件扫描、自动织入和声明性切面（缓存、事务和安全，等等）
> 
> 2022-06-03 18:06:41 ^26211867-26-696-743

> [!NOTE] 
> @RunWith的参数是SpringJUnit4ClassRunner.class，开启了Spring集成测试支持
> 
> 2022-06-03 18:08:09 ^26211867-26-1392-1449

> [!NOTE] 
> @ContextConfiguration指定了如何加载应用程序上下文。此处我们让它加载Address-BookConfiguration里配置的Spring应用程序上下文
> 
> 2022-06-03 18:08:19 ^26211867-26-1603-1689

> [!NOTE] 
> SpringApplication不仅加载应用程序上下文，还会开启日志、加载外部属性（application.properties或application.yml），以及其他Spring Boot特性
> 
> 2022-06-03 18:09:04 ^26211867-26-2069-2169

### 4.2 测试Web应用程序

> [!NOTE] 
> Spring MVC有一个优点：它的编程模型是围绕POJO展开的，在POJO上添加注解，声明如何处理Web请求
> 
> 2022-06-03 18:10:22 ^26211867-27-431-486

> [!NOTE] 
> ❑ Spring Mock MVC：能在一个近似真实的模拟Servlet容器里测试控制器，而不用实际启动应用服务器。❑ Web集成测试：在嵌入式Servlet容器（比如Tomcat或Jetty）里启动应用程序，在真正的应用服务器里执行测试。
> 
> 2022-06-03 18:11:22 ^26211867-27-1394-1544

### 4.3 测试运行中的应用程序

### 4.4 小结

## 第5章 Groovy与Spring Boot CLI

### 5.1 开发Spring Boot CLI应用程序

### 5.2 获取依赖

### 5.3 用CLI运行测试

### 5.4 创建可部署的产物

### 5.5 小结

## 第6章 在Spring Boot中使用Grails

### 6.1 使用GORM进行数据持久化

### 6.2 使用Groovy Server Pages定义视图

### 6.3 结合Spring Boot与Grails 3

### 6.4 小结

## 第7章 深入Actuator

### 7.1 揭秘Actuator的端点

### 7.2 连接Actuator的远程shell

### 7.3 通过JMX监控应用程序

### 7.4 定制Actuator

### 7.5 保护Actuator端点

### 7.6 小结

## 第8章 部署Spring Boot应用程序

### 8.1 衡量多种部署方式

### 8.2 部署到应用服务器

### 8.3 推上云端

### 8.4 小结

## 附录A Spring Boot开发者工具

### A.1 自动重启

### A.2 LiveReload

### A.3 远程开发

### A.4 默认的开发时属性

### A.5 全局配置开发者工具

## 附录B Spring Boot起步依赖

## 附录C 配置属性

## 附录D Spring Boot依赖

## 延展阅读

## 内容简介

## 看完了

