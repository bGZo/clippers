---
doc_type: weread-highlights-reviews
bookId: "25462418"
reviewCount: 1
noteCount: 5
author:
  - 翟陆续 薛宾田
  - 电子工业出版社
cover: https://cdn.weread.qq.com/weread/cover/78/YueWen_25462418/t7_YueWen_25462418.jpg
readingStatus: 在读
progress: "-1"
totalReadDay: 3
readingTime: 0小时13分钟
readingDate: 2022-03-15
title: Java并发编程之美
published: 2018-10-01 00:00:00
description: Java并发编程无处不在，涉及的知识点多，要掌握并用好它并非易事。作者加多拥有在大型互联网公司阿里巴巴的丰富工作经验，遇到并解决了业务场景中很多实际的并发问题。本书是他对自己实践经验的总结与升华。为帮助读者解决学习中的各类痛点，作者将全书明确地分为基础篇、高级篇和实践篇，脉络清晰；全书以代码说话，辅以图表，让初学者能一步一步地深入堂奥，掌握并发编程的精髓。
isbn: 9787121349478
tags:
  - weread/计算机-编程设计
type: weread-notes
weread: https://weread.qq.com/web/reader/81c32b507184869281c2a23

---


## 封面

## 版权信息

## 内容简介

## 业界好评

> [!NOTE] 
> 依然没有模式、架构之类的宏大叙事
> 
> 2022-03-15 10:51:49 ^25462418-4-849-865

> [!NOTE] 
> JUC
> 
> 2022-03-15 10:53:13 ^25462418-4-1134-1137

## 前言

## 第一部分 Java并发编程基础篇

### 第1章 并发编程线程基础

#### 1.2 线程创建与运行

> [!NOTE] 
> Runnable接口的run方法
> 
> 2022-08-03 21:01:38 ^25462418-8-460-476

> [!NOTE] 
> 继承Thread类并重写run的方法
> 
> 2022-08-03 21:01:30 ^25462418-8-477-495

> [!NOTE] 
> FutureTask方式
> 
> 2022-08-03 21:01:41 ^25462418-8-498-510

#### 1.3 线程通知与等待

#### 1.4 等待线程执行终止的join方法

#### 1.5 让线程睡眠的sleep方法

#### 1.6 让出CPU执行权的yield方法

#### 1.7 线程中断

#### 1.8 理解线程上下文切换

#### 1.9 线程死锁

#### 1.10 守护线程与用户线程

#### 1.11 ThreadLocal

### 第2章 并发编程的其他基础知识

#### 2.2 为什么要进行多线程并发编程

#### 2.3 Java中的线程安全问题

#### 2.4 Java中共享变量的内存可见性问题

#### 2.5 Java中的synchronized关键字

#### 2.6 Java中的volatile关键字

#### 2.7 Java中的原子性操作

#### 2.8 Java中的CAS操作

#### 2.9 Unsafe类

#### 2.10 Java指令重排序

#### 2.11 伪共享

#### 2.12 锁的概述

#### 2.13 总结

## 第二部分 Java并发编程高级篇

### 第3章 Java并发包中ThreadLocalRandom类原理剖析

#### 3.1 Random类及其局限性

#### 3.2 ThreadLocalRandom

#### 3.3 源码分析

#### 3.4 总结

### 第4章 Java并发包中原子操作类原理剖析

#### 4.1 原子变量操作类

#### 4.2 JDK 8新增的原子操作类LongAdder

#### 4.3 LongAccumulator类原理探究

#### 4.4 总结

### 第5章 Java并发包中并发List源码剖析

#### 5.2 主要方法源码解析

#### 5.3 总结

### 第6章 Java并发包中锁原理剖析

#### 6.2 抽象同步队列AQS概述

#### 6.3 独占锁ReentrantLock的原理

#### 6.4 读写锁ReentrantReadWriteLock的原理

#### 6.5 JDK 8中新增的StampedLock锁探究

### 第7章 Java并发包中并发队列原理剖析

#### 7.1 ConcurrentLinkedQueue原理探究

#### 7.2 LinkedBlockingQueue原理探究

#### 7.3 ArrayBlockingQueue原理探究

#### 7.4 PriorityBlockingQueue原理探究

#### 7.5 DelayQueue原理探究

### 第8章 Java并发包中线程池ThreadPoolExecutor原理探究

#### 8.2 类图介绍

#### 8.3 源码分析

#### 8.4 总结

### 第9章 Java并发包中ScheduledThreadPoolExecutor原理探究

#### 9.2 类图介绍

#### 9.3 原理剖析

#### 9.4 总结

### 第10章 Java并发包中线程同步器原理剖析

#### 10.2 回环屏障CyclicBarrier原理探究

#### 10.3 信号量Semaphore原理探究

#### 10.4 总结

## 第三部分 Java并发编程实践篇

### 第11章 并发编程实践

#### 11.2 Tomcat的NioEndPoint中ConcurrentLinkedQueue的使用

#### 11.3 并发组件ConcurrentHashMap使用注意事项

#### 11.4 SimpleDateFormat是线程不安全的

#### 11.5 使用Timer时需要注意的事情

#### 11.6 对需要复用但是会被下游修改的参数要进行深复制

#### 11.7 创建线程和线程池时要指定与业务相关的名称

#### 11.8 使用线程池的情况下当程序结束时记得调用shutdown关闭线程池

#### 11.9 线程池使用FutureTask时需要注意的事情

#### 11.10 使用ThreadLocal不当可能会导致内存泄漏

#### 11.11 总结

## 后记

## 作者简介

