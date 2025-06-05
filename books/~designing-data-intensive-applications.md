---
aliases: Designing Data-Intensive Applications, books/设计数据密集型应用
tags: #database
author: Martin Kleppmann
translator: 赵军平, 李三平, 吕云松, 耿煜
publisher: O'Reilly
published:  20180901
isbn: 9787519821968
created: 2023-03-28
douban: https://book.douban.com/subject/26197294 ； https://book.douban.com/subject/30329536/
source: https://github.com/Vonng/ddia
---

## ![Designing Data-Intensive Applications](../assets/book_designing_data-Intensive_applications.pdf)
## Contents
  - [序言](http://ddia.vonng.com/#/preface)
    - > **在我们的社会中，技术是一种强大的力量。数据、软件、通信可以用于坏的方面：不公平的阶级固化，损害公民权利，保护既得利益集团。但也可以用于好的方面：让底层人民发出自己的声音，让每个人都拥有机会，避免灾难。本书献给所有将技术用于善途的人们。**
    - > 计算是一种流行文化，流行文化鄙视历史。 流行文化关乎个体身份和参与感，但与合作无关。流行文化活在当下，也与过去和未来无关。 我认为大部分（为了钱）编写代码的人就是这样的， 他们不知道自己的文化来自哪里。
      —— 阿兰・凯接受 Dobb 博士的杂志采访时（2012 年）
  - [第一部分：数据系统基础](http://ddia.vonng.com/#/part-i)
    - [第一章：可靠性、可伸缩性和可维护性](http://ddia.vonng.com/#/ch1)
    - [第二章：数据模型与查询语言](http://ddia.vonng.com/#/ch2)
      - [关系模型与文档模型](http://ddia.vonng.com/#/ch2?id=%e5%85%b3%e7%b3%bb%e6%a8%a1%e5%9e%8b%e4%b8%8e%e6%96%87%e6%a1%a3%e6%a8%a1%e5%9e%8b)
        - 关系数据库起源于商业数据处理，在 20 世纪 60 年代和 70 年代用大型计算机来执行。从今天的角度来看，那些用例显得很平常：典型的 **事务处理**（将销售或银行交易，航空公司预订，库存管理信息记录在库）和 **批处理**（客户发票，工资单，报告）。
        - [NoSQL 的诞生](http://ddia.vonng.com/#/ch2?id=nosql-%e7%9a%84%e8%af%9e%e7%94%9f)
        - [对象关系不匹配](http://ddia.vonng.com/#/ch2?id=%e5%af%b9%e8%b1%a1%e5%85%b3%e7%b3%bb%e4%b8%8d%e5%8c%b9%e9%85%8d)
        - [多对一和多对多的关系](http://ddia.vonng.com/#/ch2?id=%e5%a4%9a%e5%af%b9%e4%b8%80%e5%92%8c%e5%a4%9a%e5%af%b9%e5%a4%9a%e7%9a%84%e5%85%b3%e7%b3%bb)
        - [文档数据库是否在重蹈覆辙？](http://ddia.vonng.com/#/ch2?id=%e6%96%87%e6%a1%a3%e6%95%b0%e6%8d%ae%e5%ba%93%e6%98%af%e5%90%a6%e5%9c%a8%e9%87%8d%e8%b9%88%e8%a6%86%e8%be%99%ef%bc%9f)
        - [关系型数据库与文档数据库在今日的对比](http://ddia.vonng.com/#/ch2?id=%e5%85%b3%e7%b3%bb%e5%9e%8b%e6%95%b0%e6%8d%ae%e5%ba%93%e4%b8%8e%e6%96%87%e6%a1%a3%e6%95%b0%e6%8d%ae%e5%ba%93%e5%9c%a8%e4%bb%8a%e6%97%a5%e7%9a%84%e5%af%b9%e6%af%94)
      - [数据查询语言](http://ddia.vonng.com/#/ch2?id=%e6%95%b0%e6%8d%ae%e6%9f%a5%e8%af%a2%e8%af%ad%e8%a8%80)
        - [Web 上的声明式查询](http://ddia.vonng.com/#/ch2?id=web-%e4%b8%8a%e7%9a%84%e5%a3%b0%e6%98%8e%e5%bc%8f%e6%9f%a5%e8%af%a2)
        - [MapReduce查询](http://ddia.vonng.com/#/ch2?id=mapreduce%e6%9f%a5%e8%af%a2)
      - [图数据模型](http://ddia.vonng.com/#/ch2?id=%e5%9b%be%e6%95%b0%e6%8d%ae%e6%a8%a1%e5%9e%8b)
        - [属性图](http://ddia.vonng.com/#/ch2?id=%e5%b1%9e%e6%80%a7%e5%9b%be)
        - [Cypher 查询语言](http://ddia.vonng.com/#/ch2?id=cypher-%e6%9f%a5%e8%af%a2%e8%af%ad%e8%a8%80)
        - [SQL 中的图查询](http://ddia.vonng.com/#/ch2?id=sql-%e4%b8%ad%e7%9a%84%e5%9b%be%e6%9f%a5%e8%af%a2)
        - [三元组存储和 SPARQL](http://ddia.vonng.com/#/ch2?id=%e4%b8%89%e5%85%83%e7%bb%84%e5%ad%98%e5%82%a8%e5%92%8c-sparql)
        - [SPARQL 查询语言](http://ddia.vonng.com/#/ch2?id=sparql-%e6%9f%a5%e8%af%a2%e8%af%ad%e8%a8%80)
        - [基础：Datalog](http://ddia.vonng.com/#/ch2?id=%e5%9f%ba%e7%a1%80%ef%bc%9adatalog)
      - [本章小结](http://ddia.vonng.com/#/ch2?id=%e6%9c%ac%e7%ab%a0%e5%b0%8f%e7%bb%93)
      - [参考文献](http://ddia.vonng.com/#/ch2?id=%e5%8f%82%e8%80%83%e6%96%87%e7%8c%ae)
    - [第三章：存储与检索](http://ddia.vonng.com/#/ch3)
      - ![](http://ddia.vonng.com/img/ch3.png)
      - > 建立秩序，省却搜索
        —— 德国谚语
    - [第四章：编码与演化](http://ddia.vonng.com/#/ch4)
  - [第二部分：分布式数据](http://ddia.vonng.com/#/part-ii)
    - [第五章：复制](http://ddia.vonng.com/#/ch5)
    - [第六章：分区](http://ddia.vonng.com/#/ch6)
    - [第七章：事务](http://ddia.vonng.com/#/ch7)
    - [第八章：分布式系统的麻烦](http://ddia.vonng.com/#/ch8)
    - [第九章：一致性与共识](http://ddia.vonng.com/#/ch9)
  - [第三部分：衍生数据](http://ddia.vonng.com/#/part-iii)
    - [第十章：批处理](http://ddia.vonng.com/#/ch10)
    - [第十一章：流处理](http://ddia.vonng.com/#/ch11)
    - [第十二章：数据系统的未来](http://ddia.vonng.com/#/ch12)
  - [术语表](http://ddia.vonng.com/#/glossary)
  - [后记](http://ddia.vonng.com/#/colophon)
## Comment
-