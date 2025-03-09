---
doc_type: weread-highlights-reviews
bookId: "33114748"
reviewCount: 0
noteCount: 6
author:
  - Scott Meyers
  - 电子工业出版社
cover: https://cdn.weread.qq.com/weread/cover/99/YueWen_33114748/t7_YueWen_33114748.jpg
readingStatus: 未标记
progress: "-1"
totalReadDay: 1
readingTime: 0小时0分钟
readingDate: 2021-12-24
title: Effective STL中文版：50条有效使用STL的经验（双色）
published: 2013-05-01 00:00:00
description: 本书是Effective C++的第3卷，被评为“值得所有C++程序员阅读的C++书籍之一”。本书详细讲述了使用STL的50条指导原则，并提供了透彻的分析和深刻的实例，实用性极强，是C++程序员必备的基础书籍。C++的标准模板库(STL)是革命性的，要用好STL并不容易。本书作者Scott Meyers揭示了专家总结的一些关键规则，包括专家们总是采用的做法，以及专家们总是避免的做法。通过这些规则，STL程序员可以最大限度地使用STL。
isbn: 9787121201257
tags:
  - 计算机-计算机综合
type: weread-notes
weread: https://weread.qq.com/web/reader/72932ee071f94a7c72915cf

---


## 封面

## 版权信息

## 内容简介

## 译序

## 前言

## 致谢

## 引言

## 1 容器

### 第1条：慎重选择容器类型。

> [!NOTE] 
> multiset
> 
> 2021-12-24 09:58:14 ^33114748-9-638-646

> [!NOTE] 
> slist和rope
> 
> 2021-12-24 09:58:20 ^33114748-9-706-716

> [!NOTE] 
> 有时vector在运行时间和空间上都要优于标准关联容器
> 
> 2021-12-24 09:58:47 ^33114748-9-1109-1136

> [!NOTE] 
> 为什么bitset比vector<bool>要好
> 
> 2021-12-24 09:59:13 ^33114748-9-1297-1321

> [!NOTE] 
> 当需要频繁地在序列中间做插入和删除操作时，应使用list
> 
> 2021-12-24 10:01:32 ^33114748-9-1634-1662

> [!NOTE] 
> deque是应考虑的数据结构
> 
> 2021-12-24 10:01:38 ^33114748-9-1687-1701

### 第2条：不要试图编写独立于容器类型的代码。

### 第3条：确保容器中的对象拷贝正确而高效。

### 第4条：调用empty而不是检查size()是否为0。

### 第5条：区间成员函数优先于与之对应的单元素成员函数。

### 第6条：当心C++编译器最烦人的分析机制。

### 第7条：如果容器中包含了通过new操作创建的指针，切记在容器对象析构前将指针delete掉。

### 第8条：切勿创建包含auto_ptr的容器对象。

### 第9条：慎重选择删除元素的方法。

### 第10条：了解分配子（allocator）的约定和限制。

### 第11条：理解自定义分配子的合理用法。

### 第12条：切勿对STL容器的线程安全性有不切实际的依赖。

## 2 vector和string

### 第13条：vector和string优先于动态分配的数组。

### 第14条：使用reserve来避免不必要的重新分配。

### 第15条：注意string实现的多样性。

### 第16条：了解如何把vector和string数据传给旧的AP1。

### 第17条：使用“swap技巧”除去多余的容量。

### 第18条：避免使用vector<bool>。

## 3 关联容器

### 第19条：理解相等（equality）和等价（equivalence）的区别。

### 第20条：为包含指针的关联容器指定比较类型。

### 第21条：总是让比较函数在等值情况下返回false。

### 第22条：切勿直接修改set或multiset中的键。

### 第23条：考虑用排序的vector替代关联容器。

### 第24条：当效率至关重要时，请在map::operator[]与map::insert之间谨慎做出选择。

### 第25条：熟悉非标准的散列容器。

## 4 迭代器

### 第26条：iterator优先于const_iterator、reverse_iterator及const_reverse_iterator。

### 第27条：使用distance和advance将容器的const_iterator转换成iterator。

### 第28条：正确理解由reverse_iterator的base()成员函数所产生的iterator的用法。

### 第29条：对于逐个字符的输入请考虑使用istreambuf_iterator。

## 5 算法

### 第30条：确保目标区间足够大。

### 第31条：了解各种与排序有关的选择。

### 第32条：如果确实需要删除元素，则需要在remove这一类算法之后调用erase。

### 第33条：对包含指针的容器使用remove这一类算法时要特别小心。

### 第34条：了解哪些算法要求使用排序的区间作为参数。

### 第35条：通过mismatch或lexicographical_compare实现简单的忽略大小写的字符串比较。

### 第36条：理解copy_if算法的正确实现。

### 第37条：使用accumulate或者for_each进行区间统计。

## 6 函数子、函数子类、函数及其他

### 第38条：遵循按值传递的原则来设计函数子类。

### 第39条：确保判别式是“纯函数”。

### 第40条：若一个类是函数子，则应使它可配接。

### 第41条：理解ptr_fun、mem_fun和mem_fun_ref的来由。

### 第42条：确保less<T>与operator<具有相同的语义。

## 7 在程序中使用STL

### 第43条：算法调用优先于手写的循环。

### 第44条：容器的成员函数优先于同名的算法。

### 第45条：正确区分count、find、binary_search、lower_bound、upper_bound和equal_range。

### 第46条：考虑使用函数对象而不是函数作为STL算法的参数。

### 第47条：避免产生“直写型”（write-only）的代码。

### 第48条：总是包含（＃include）正确的头文件。

### 第49条：学会分析与STL相关的编译器诊断信息。

### 第50条：熟悉与STL相关的Web站点。

## 参考书目

## 附录A 地域性与忽略大小写的字符串比较

## 附录B 对Microsoft的STL平台的说明

## 文后

