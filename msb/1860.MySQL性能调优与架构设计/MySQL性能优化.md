## 1.3.MySQL调优

### 1.3.1.MySQL调优金字塔

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/098cb1ed7e96428eaea382ab6b69848d.png)

很明显从图上可以看出，越往上走，难度越来越高，收益却是越来越小的。

对于**架构调优**，在系统设计时首先需要充分考虑业务的实际情况，是否可以把不适合数据库做的事情放到数据仓库、搜索引擎或者缓存中去做；然后考虑写的并发量有多大，是否需要采用分布式；最后考虑读的压力是否很大，是否需要读写分离。对于核心应用或者金融类的应用，需要额外考虑数据安全因素，数据是否不允许丢失。所以在进行优化时，首先需要关注和优化的应该是架构，如果架构不合理，即使是DBA能做的事情其实是也是比较有限的。

对于**MySQL调优**，需要确认业务表结构设计是否合理，SQL语句优化是否足够，该添加的索引是否都添加了，是否可以剔除多余的索引等等

比如**硬件和OS调优**，需要对硬件和OS有着非常深刻的了解，仅仅就磁盘一项来说，一般非DBA能想到的调整就是SSD盘比用机械硬盘更好。DBA级别考虑的至少包括了，使用什么样的磁盘阵列（RAID）级别、是否可以分散磁盘IO、是否使用裸设备存放数据，使用哪种文件系统（目前比较推荐的是XFS），操作系统的磁盘调度算法选择，是否需要调整操作系统文件管理方面比如atime属性等等。

所以本章我们重点关注MySQL方面的调优，特别是索引。SQL/索引调优要求对业务和数据流非常清楚。在阿里巴巴内部，有三分之二的DBA是业务DBA，从业务需求讨论到表结构审核、SQL语句审核、上线、索引更新、版本迭代升级，甚至哪些数据应该放到非关系型数据库中，哪些数据放到数据仓库、搜索引擎或者缓存中，都需要这些DBA跟踪和复审。他们甚至可以称为数据架构师（Data Architecher）。

### 1.3.2.查询性能优化

前面的章节我们知道如何设计最优的库表结构、如何建立最好的索引，这些对于高性能来说是必不可少的。但这些还不够—还需要合理的设计查询。如果查询写得很糟糕，即使库表结构再合理、索引再合适，也无法实现高性能。

#### 1.3.2.1.什么是慢查询

慢查询日志，顾名思义，就是查询花费大量时间的日志，是指mysql记录所有执行超过long_query_time参数设定的时间阈值的SQL语句的日志。该日志能为SQL语句的优化带来很好的帮助。默认情况下，慢查询日志是关闭的，要使用慢查询日志功能，首先要开启慢查询日志功能。如何开启，我们稍后再说。

##### **1.3.2.1.1慢查询基础-优化数据访问**

查询性能低下最基本的原因是访问的数据太多。大部分性能低下的查询都可以通过减少访问的数据量的方式进行优化。对于低效的查询，一般通过下面两个步骤来分析总是很有效:

1．确认应用程序是否在检索大量超过需要的数据。这通常意味着访问了太多的行，但有时候也可能是访问了太多的列。

2．确认MySQL服务器层是否在分析大量超过需要的数据行。

##### **1.3.2.1.2请求了不需要的数据？**

有些查询会请求超过实际需要的数据，然后这些多余的数据会被应用程序丢弃。这会给MySQL服务器带来额外的负担，并增加网络开销，另外也会消耗应用服务器的CPU和内存资源。比如:

**查询不需要的记录**

一个常见的错误是常常会误以为MySQL会只返回需要的数据，实际上MySQL却是先返回全部结果集再进行计算。我们经常会看到一些了解其他数据库系统的人会设计出这类应用程序。

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/c42215b7f5c442869027906f5aa80f4e.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/8915ae332c7b4dbea0fa3c591e902197.png)

以上SQL你认为MySQL会执行查询，并只返回他们需要的20条数据，然后停止查询。实际情况是MySQL会查询出全部的结果集，客户端的应用程序会接收全部的结果集数据，然后抛弃其中大部分数据。

**总是取出全部列**

每次看到SELECT*的时候都需要用怀疑的眼光审视，是不是真的需要返回全部的列？很可能不是必需的。取出全部列，会让优化器无法完成索引覆盖扫描这类优化,还会为服务器带来额外的I/O、内存和CPU的消耗。因此，一些DBA是严格禁止SELECT *的写法的，这样做有时候还能避免某些列被修改带来的问题。

尤其是使用二级索引，使用*的方式会导致回表，导致性能低下。

什么时候可以使用SELECT*如果应用程序使用了某种缓存机制，或者有其他考虑，获取超过需要的数据也可能有其好处，但不要忘记这样做的代价是什么。获取并缓存所有的列的查询，相比多个独立的只获取部分列的查询可能就更有好处。

**重复查询相同的数据**

不断地重复执行相同的查询，然后每次都返回完全相同的数据。比较好的方案是，当初次查询的时候将这个数据缓存起来，需要的时候从缓存中取出，这样性能显然会更好。

##### 1.3.2.1.3.是否在扫描额外的记录

在确定查询只返回需要的数据以后，接下来应该看看查询为了返回结果是否扫描了过多的数据。对于MySQL，最简单的衡量查询开销的三个指标如下:

**响应时间、扫描的行数、返回的行数**

没有哪个指标能够完美地衡量查询的开销，但它们大致反映了MySQL在内部执行查询时需要访问多少数据，并可以大概推算出查询运行的时间。这三个指标都会记录到MySQL的慢日志中，所以检查慢日志记录是找出扫描行数过多的查询的好办法。

**响应时间**

响应时间是两个部分之和:服务时间和排队时间。

服务时间是指数据库处理这个查询真正花了多长时间。

排队时间是指服务器因为等待某些资源而没有真正执行查询的时间—-可能是等I/O操作完成，也可能是等待行锁，等等。

**扫描的行数和返回的行数**

分析查询时，查看该查询扫描的行数是非常有帮助的。这在一定程度上能够说明该查询找到需要的数据的效率高不高。

理想情况下扫描的行数和返回的行数应该是相同的。但实际情况中这种“美事”并不多。例如在做一个关联查询时，服务器必须要扫描多行才能生成结果集中的一行。扫描的行数对返回的行数的比率通常很小，一般在1:1和10:1之间，不过有时候这个值也可能非常非常大。

**扫描的行数和访问类型**

在评估查询开销的时候，需要考虑一下从表中找到某一行数据的成本。MySQL有好几种访问方式可以查找并返回一行结果。有些访问方式可能需要扫描很多行才能返回一行结果，也有些访问方式可能无须扫描就能返回结果。

在EXPLAIN语句中的type列反应了访问类型。访问类型有很多种，从全表扫描到索引扫描、范围扫描、唯一索引查询、常数引用等。这里列的这些，速度是从慢到快，扫描的行数也是从小到大。你不需要记住这些访问类型，但需要明白扫描表、扫描索引、范围访问和单值访问的概念。

如果查询没有办法找到合适的访问类型，那么解决的最好办法通常就是增加一个合适的索引，为什么索引对于查询优化如此重要了。索引让 MySQL以最高效、扫描行数最少的方式找到需要的记录。

一般 MySQL能够使用如下三种方式应用WHERE条件，从好到坏依次为:

1、在索引中使用WHERE条件来过滤不匹配的记录。这是在存储引擎层完成的。

select .... from where a>100 and a &#x3c;200

2、使用覆盖索引扫描来返回记录，直接从索引中过滤不需要的记录并返回命中的结果。这是在 MySQL服务器层完成的，但无须再回表查询记录。

3、从数据表中返回数据(存在回表)，然后过滤不满足条件的记录。这在 MySQL服务器层完成，MySQL需要先从数据表读出记录然后过滤。

好的索引可以让查询使用合适的访问类型，尽可能地只扫描需要的数据行。

**如果发现查询需要扫描大量的数据但只返回少数的行，那么通常可以尝试下面的技巧去优化它:**

1、使用索引覆盖扫描，把所有需要用的列都放到索引中，这样存储引擎无须回表获取对应行就可以返回结果了

2、改变库表结构。例如使用单独的汇总表。

3、重写这个复杂的查询，让MySQL优化器能够以更优化的方式执行这个查询。

### 1.3.3.慢查询

#### 1.3.3.1慢查询配置

我们已经知道慢查询日志可以帮助定位可能存在问题的SQL语句，从而进行SQL语句层面的优化。但是默认值为关闭的，需要我们手动开启。

```
show VARIABLES like 'slow_query_log';
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/f72a83180181494fa68d4f014375127b.png)

```
set GLOBAL slow_query_log=1;
```

开启1，关闭0

但是多慢算慢？MySQL中可以设定一个阈值，将运行时间超过该值的所有SQL语句都记录到慢查询日志中。long_query_time参数就是这个阈值。默认值为10，代表10秒。

```
show VARIABLES like '%long_query_time%';
```

当然也可以设置

```
set global long_query_time=0;
```

默认10秒，这里为了演示方便设置为0

同时对于运行的SQL语句没有使用索引，则MySQL数据库也可以将这条SQL语句记录到慢查询日志文件，控制参数是：

```
show VARIABLES like '%log_queries_not_using_indexes%';
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/19a8d15f0d724fae93946b5bd4f63cc3.png)

开启1，关闭0（默认）

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/67a74308e0524b459cb30cfa66bdba40.png)

```
show VARIABLES like '%slow_query_log_file%';
```

##### 小结

l  slow_query_log 启动停止慢查询日志

l  slow_query_log_file 指定慢查询日志得存储路径及文件（默认和数据文件放一起）

l  long_query_time 指定记录慢查询日志SQL执行时间得伐值（单位：秒，默认10秒）

l  log_queries_not_using_indexes  是否记录未使用索引的SQL

l  log_output 日志存放的地方可以是[TABLE][FILE][FILE,TABLE]

### 1.3.4.Explain执行计划

#### 1.3.4.1.什么是执行计划

有了慢查询语句后，就要对语句进行分析。一条查询语句在经过MySQL查询优化器的各种基于成本和规则的优化会后生成一个所谓的执行计划，这个执行计划展示了接下来具体执行查询的方式，比如多表连接的顺序是什么，对于每个表采用什么访问方法来具体执行查询等等。EXPLAIN语句来帮助我们查看某个查询语句的具体执行计划，我们需要搞懂EPLATNEXPLAIN的各个输出项都是干嘛使的，从而可以有针对性的提升我们查询语句的性能。

通过使用EXPLAIN关键字可以模拟优化器执行SQL查询语句，从而知道MySQL是如何处理你的SQL语句的。分析查询语句或是表结构的性能瓶颈，总的来说通过EXPLAIN我们可以：

l  表的读取顺序

l  数据读取操作的操作类型

l  哪些索引可以使用

l  哪些索引被实际使用

l  表之间的引用

l  每张表有多少行被优化器查询

#### 1.3.4.2.执行计划的语法

执行计划的语法其实非常简单： 在SQL查询的前面加上EXPLAIN关键字就行。比如：EXPLAIN select * from table1

重点的就是EXPLAIN后面你要分析的SQL语句

除了以SELECT开头的查询语句，其余的DELETE、INSERT、REPLACE以及UPOATE语句前边都可以加上EXPLAIN，用来查看这些语句的执行计划，不过我们这里对SELECT语句更感兴趣，所以后边只会以SELECT语句为例来描述EsxPLAIN语句的用法。

#### 1.3.4.3.执行计划详解

为了让大家先有一个感性的认识，我们把EXPLAIN语句输出的各个列的作用先大致罗列一下:

**explain
select * from order_exp;**

**id** **： ****在一个大的查询语句中每个SELECT****关键字都对应一个唯一的id**

**select_type** **： SELECT****关键字对应的那个查询的类型**

**table** **：表名**

**partitions** **：匹配的分区信息**

**type** **：针对单表的访问方法**

**possible_keys** **：可能用到的索引**

**key** **：实际上使用的索引**

**key_len** **：实际使用到的索引长度**

**ref** **：当使用索引列等值查询时，与索引列进行等值匹配的对象信息**

**rows** **：预估的需要读取的记录条数**

**filtered** **：某个表经过搜索条件过滤后剩余记录条数的百分比**

**Extra** **：—些额外的信息**

##### id

我们知道我们写的查询语句一般都以SELECT关键字开头，比较简单的查询语句里只有一个SELECT关键字，

稍微复杂一点的连接查询中也只有一个SELECT关键字，比如:

```sql
SELECT *FROM s1
INNER J0IN s2 ON s1.id = s2.id
WHERE s1.order_status = 0 ;
```

但是下边两种情况下在一条查询语句中会出现多个SELECT关键字:

1、查询中包含子查询的情况

比如下边这个查询语句中就包含2个SELECT关键字:

```
SELECT* FROM s1 WHERE id IN ( SELECT * FROM s2);
```

2、查询中包含UNION语句的情况

比如下边这个查询语句中也包含2个SELECT关键字:

```
SELECT * FROM s1
UNION SELECT * FROM s2 ;
```

查询语句中每出现一个SELECT关键字，MySQL就会为它分配一个唯一的id值。这个id值就是EXPLAIN语句的第一个列。

###### 单SELECT关键字

比如下边这个查询中只有一个SELECT关键字，所以EXPLAIN的结果中也就只有一条id列为1的记录∶

```
EXPLAIN SELECT * FROM s1 WHERE order_no = 'a';
```

###### 连接查询

对于连接查询来说，一个SELEOT关键字后边的FROM子句中可以跟随多个表，所以在连接查询的执行计划中，每个表都会对应一条记录，但是这些记录的id值都是相同的，比如:

```
EXPLAIN SELECT * FROM s1 WHERE order_no = 'a';
```

可以看到，上述连接查询中参与连接的s1和s2表分别对应一条记录，但是这两条记录对应的id值都是1。这里需要大家记住的是，在连接查询的执行计划中，每个表都会对应一条记录，这些记录的id列的值是相同的。

###### 包含子查询

对于包含子查询的查询语句来说，就可能涉及多个SELECT关键字，所以在包含子查询的查询语句的执行计划中，每个SELECT关键字都会对应一个唯一的id值，比如这样:

```
EXPLAIN
SELECT * FROM s1 WHERE id IN (SELECT id FROM s2) OR order_no = 'a';
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/93136f4766424e9e91a0b065908ad1c8.png)

但是这里大家需要特别注意，查询优化器可能对涉及子查询的查询语句进行重写，从而转换为连接查询。所以如果我们想知道查询优化器对某个包含子查询的语句是否进行了重写，直接查看执行计划就好了，比如说:

```
EXPLAIN
SELECT * FROM s1 WHERE id IN (SELECT id FROM s2 WHERE order_no = 'a');
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/6475b28cd68144b89566254b0891a210.png)

可以看到，虽然我们的查询语句是一个子查询，但是执行计划中s1和s2表对应的记录的id值全部是1，这就表明了查询优化器将子查询转换为了连接查询,

###### 包含UNION子句

对于包含UNION子句的查询语句来说，每个SELECT关键字对应一个id值也是没错的，不过还是有点儿特别的东西，比方说下边这个查询:

```
EXPLAIN
SELECT * FROM s1 UNION SELECT * FROM s2;
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/4907ca3c4cea47a0add9684f8081acc3.png)

这个语句的执行计划的第三条记录为什么这样？UNION
子句会把多个查询的结果集合并起来并对结果集中的记录进行去重，怎么去重呢? MySQL使用的是内部的临时表。正如上边的查询计划中所示，UNION 子句是为了把id为1的查询和id为2的查询的结果集合并起来并去重，所以在内部创建了一个名为&#x3c;union1，2>的临时表（就是执行计划第三条记录的table列的名称)，id为NULL表明这个临时表是为了合并两个查询的结果集而创建的。

跟UNION 对比起来，UNION
ALL就不需要为最终的结果集进行去重，它只是单纯的把多个查询的结果集中的记录合并成一个并返回给用户，所以也就不需要使用临时表。所以在包含UNION ALL子句的查询的执行计划中，就没有那个id为NULL的记录，如下所示:

```
EXPLAIN
SELECT * FROM s1 UNION ALL SELECT * FROM s2;
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/f58b6838d5c34edc8580e1309a96cd16.png)

##### table

不论我们的查询语句有多复杂，里边包含了多少个表，到最后也是需要对每个表进行单表访问的，MySQL规定EXPLAIN语句输出的每条记录都对应着某个单表的访问方法，该条记录的table列代表着该表的表名。

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/ad26adcd3f0b45d39ebc12b51de8c74b.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/e41c8c8a619c4781b0fd7293c556ed54.png)

可以看见，只涉及对s1表的单表查询，所以EXPLAIN输出中只有一条记录，其中的table列的值是s1，而连接查询的执行计划中有两条记录，这两条记录的table列分别是s1和s2.

##### partitions

和分区表有关，一般情况下我们的查询语句的执行计划的partitions列的值都是NULL。

##### type

我们前边说过执行计划的一条记录就代表着MySQL对某个表的执行查询时的访问方法/访问类型，其中的type列就表明了这个访问方法/访问类型是个什么东西，是较为重要的一个指标，结果值从最好到最坏依次是：

出现比较多的是system>const>eq_ref>ref>range>index>ALL

一般来说，得保证查询至少达到range级别，最好能达到ref。

###### system

当表中只有一条记录并且该表使用的存储引擎的统计数据是精确的，比如MyISAM、Memory，那么对该表的访问方法就是system。

```
explain select * from test_myisam;
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/0cd60414ae624c2aad6b7870d8702116.png)

当然，如果改成使用InnoDB存储引擎，试试看执行计划的type列的值是什么。

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/5f326bb8471841da9b8b750877c497b8.png)

###### const

就是当我们根据主键或者唯一二级索引列与常数进行等值匹配时，对单表的访问方法就是const。因为只匹配一行数据，所以很快。

例如将主键置于where列表中

```
EXPLAIN
SELECT * FROM s1 WHERE id = 716;
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/854f80afc83e4d53b368a29634dea02a.png)

B+树叶子节点中的记录是按照索引列排序的，对于的聚簇索引来说，它对应的B+树叶子节点中的记录就是按照id列排序的。B+树矮胖，所以这样根据主键值定位一条记录的速度很快。类似的，我们根据唯一二级索引列来定位一条记录的速度也很快的，比如下边这个查询：

```
SELECT * FROM
order_exp WHERE insert_time=’’ and order_status=’’ and expire_time=’’ ;
```

这个查询的执行分两步，第一步先从u_idx_day_status对应的B+树索引中根据索引列与常数的等值比较条件定位到一条二级索引记录，然后再根据该记录的id值到聚簇索引中获取到完整的用户记录。

MySQL把这种通过主键或者唯一二级索引列来定位一条记录的访问方法定义为：const，意思是常数级别的，代价是可以忽略不计的。

不过这种const访问方法只能在主键列或者唯一二级索引列和一个常数进行等值比较时才有效，如果主键或者唯一二级索引是由多个列构成的话，组成索引的每一个列都是与常数进行等值比较时，这个const访问方法才有效。

对于唯一二级索引来说，查询该列为NULL值的情况比较特殊，因为唯一二级索引列并不限制 NULL 值的数量，所以上述语句可能访问到多条记录，也就是说is null不可以使用const访问方法来执行。

###### eq_ref

在连接查询时，如果被驱动表是通过主键或者唯一二级索引列等值匹配的方式进行访问的〈如果该主键或者唯一二级索引是联合索引的话，所有的索引列都必须进行等值比较)，则对该被驱动表的访问方法就是eq_ref。

(***驱动表与被驱动表：*** *A**表和B**表join**连接查询，如果通过A**表的结果集作为循环基础数据，然后一条一条地通过该结果集中的数据作为过滤条件到B**表中查询数据，然后合并结果。那么我们称A**表为驱动表，B**表为被驱动表*)

比方说:

```
EXPLAIN
SELECT * FROM s1 INNER JOIN s2 ON s1.id = s2.id;
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/a33c7b8ce8e449d79866fc374baa7739.png)

从执行计划的结果中可以看出，MySQL打算将s2作为驱动表，s1作为被驱动表，重点关注s1的访问方法是eq_ref，表明在访问s1表的时候可以通过主键的等值匹配来进行访问。

###### ref

当通过普通的二级索引列与常量进行等值匹配时来查询某个表，那么对该表的访问方法就可能是ref。

本质上也是一种索引访问，它返回所有匹配某个单独值的行，然而，它可能会找到多个符合条件的行，所以他属于查找和扫描的混合体

```
EXPLAIN
SELECT * FROM s1 WHERE order_no = 'a';
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/adbe165526944750b5087866b270c858.png)

对于这个查询，我们当然可以选择全表扫描来逐一对比搜索条件是否满足要求，我们也可以先使用二级索引找到对应记录的id值，然后再回表到聚簇索引中查找完整的用户记录。

由于普通二级索引并不限制索引列值的唯一性，所以可能找到多条对应的记录，也就是说使用二级索引来执行查询的代价取决于等值匹配到的二级索引记录条数。如果匹配的记录较少，则回表的代价还是比较低的，所以MySQL可能选择使用索引而不是全表扫描的方式来执行查询。这种搜索条件为二级索引列与常数等值比较，采用二级索引来执行查询的访问方法称为：ref。

对于普通的二级索引来说，通过索引列进行等值比较后可能匹配到多条连续的记录，而不是像主键或者唯一二级索引那样最多只能匹配1条记录，所以这种ref访问方法比const要差些，但是在二级索引等值比较时匹配的记录数较少时的效率还是很高的（如果匹配的二级索引记录太多那么回表的成本就太大了）。

###### range

如果使用索引获取某些范围区间的记录，那么就可能使用到range访问方法，一般就是在你的where语句中出现了between、&#x3c;、>、in等的查询。

这种范围扫描索引扫描比全表扫描要好，因为它只需要开始于索引的某一点，而结束语另一点，不用扫描全部索引。

```
EXPLAIN
SELECT * FROM s1 WHERE order_no IN ('a', 'b', 'c');

EXPLAIN
SELECT * FROM s1 WHERE order_no > 'a' AND order_no < 'b';
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/e04fb43a98264bf5850510fdbe1db8d5.png)

这种利用索引进行范围匹配的访问方法称之为：range。

此处所说的使用索引进行范围匹配中的 `索引` 可以是聚簇索引，也可以是二级索引。

###### index

当我们可以使用索引覆盖，但需要扫描全部的索引记录时，该表的访问方法就是index。

```
EXPLAIN
SELECT insert_time FROM s1 WHERE expire_time = '2021-03-22 18:36:47';
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/a79786e8fe9147eb97696eaa28f1fada.png)

###### all

最熟悉的全表扫描，将遍历全表以找到匹配的行

```
EXPLAIN
SELECT * FROM s1;
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/315c3953f3a64e249435e19a5ce2089f.png)

##### possible_keys与key

在EXPLAIN 语句输出的执行计划中,possible_keys列表示在某个查询语句中，对某个表执行单表查询时可能用到的索引有哪些，key列表示实际用到的索引有哪些，如果为NULL，则没有使用索引。比方说下边这个查询:。

```
EXPLAIN SELECT order_note FROM s1 WHERE
insert_time = '2021-03-22 18:36:47';
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/d2f72f3156cd44369ed275e5991dcbb2.png)

上述执行计划的possible keys列的值表示该查询可能使用到u_idx_day_status,idx_insert_time两个索引，然后key列的值是u_idx_day_status，表示经过查询优化器计算使用不同索引的成本后，最后决定使用u_idx_day_status来执行查询比较划算。

##### key_len

key_len列表示当优化器决定使用某个索引执行查询时，该索引记录的最大长度，计算方式是这样的：

对于使用固定长度类型的索引列来说，它实际占用的存储空间的最大长度就是该固定值，对于指定字符集的变长类型的索引列来说，比如某个索引列的类型是VARCHAR(100)，使用的字符集是utf8，那么该列实际占用的最大存储空间就是100 x 3 = 300个字节。

如果该索引列可以存储NULL值，则key_len比不可以存储NULL值时多1个字节。

对于变长字段来说，都会有2个字节的空间来存储该变长列的实际长度。

⽐如下边这个查询：

```
EXPLAIN
SELECT * FROM s1 WHERE id = 718;
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/f898e5b7cfa54e3e9c63cd3b11a3920e.png)

由于id列的类型是bigint，并且不可以存储NULL值，所以在使用该列的索引时key_len大小就是8。

对于可变长度的索引列来说，比如下边这个查询:

```
EXPLAIN
SELECT * FROM s1 WHERE order_no = 'a';
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/74a8a80a304545c69e8fbaf4325908de.png)

由于order_no列的类型是VARCHAR(50)，所以该列实际最多占用的存储空间就是50*3字节，又因为该列是可变长度列，所以key_len需要加2，所以最后ken_len的值就是152。

MySQL在执行计划中输出key_len列主要是为了让我们区分某个使用联合索引的查询具体用了几个索引列(复合索引有最左前缀的特性，如果复合索引能全部使用上，则是复合索引字段的索引长度之和，这也可以用来判定复合索引是否部分使用，还是全部使用)，而不是为了准确的说明针对某个具体存储引擎存储变长字段的实际长度占用的空间到底是占用1个字节还是2个字节。

##### rows

如果查询优化器决定使用全表扫描的方式对某个表执行查询时，执行计划的rows列就代表预计需要扫描的行数，如果使用索引来执行查询时，执行计划的rows列就代表预计扫描的索引记录行数。比如下边两个个查询:

```
EXPLAIN
SELECT * FROM s1 WHERE order_no > 'z';

EXPLAIN
SELECT * FROM s1 WHERE order_no > 'a';
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/b3527b40c9494d17b4e608b3d8a21db6.png)

我们看到执行计划的rows列的值是分别是1和10573，这意味着查询优化器在经过分析使用idx_order_no进行查询的成本之后，觉得满足order_no> ' a '这个条件的记录只有1条，觉得满足order_no> ' a '这个条件的记录有10573条。

##### filtered

查询优化器预测有多少条记录满⾜其余的搜索条件，什么意思呢？看具体的语句：

```
EXPLAIN SELECT *
FROM s1 WHERE id > 5890 AND order_note = 'a';
```

从执行计划的key列中可以看出来，该查询使用 PRIMARY索引来执行查询，从rows列可以看出满足id > 5890的记录有5286条。执行计划的filtered列就代表查询优化器预测在这5286条记录中，有多少条记录满足其余的搜索条件，也就是order_note = 'a'这个条件的百分比。此处filtered列的值是10.0，说明查询优化器预测在5286条记录中有10.00%的记录满足order_note = 'a'这个条件。

对于单表查询来说，这个filtered列的值没什么意义，我们更关注在连接查询中驱动表对应的执行计划记录的filtered值，比方说下边这个查询:

```
EXPLAIN SELECT * FROM s1 INNER JOIN s2 ON s1.order_no = s2.order_no WHERE s1.order_note > '你好，李焕英';
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/6ba004e4db004b03b5632d9aa1a327c9.png)

从执行计划中可以看出来，查询优化器打算把s
1当作驱动表，s2当作被驱动表。我们可以看到驱动表s1表的执行计划的rows列为10573，filtered列为33.33 ，这意味着驱动表s1的扇出值就是10573 x 33.33 % = 3524.3，这说明还要对被驱动表执行大约3524次查询。

##### Extra

顾名思义，Extra列是用来说明一些额外信息的，我们可以通过这些额外信息来更准确的理解MySQL到底将如何执行给定的查询语句

### 1.3.5.查询优化器

一条SQL语句在MySQL执行的过程如下：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/b0dc955876354f09938142e60bc1f4ce.png)

1.如果是查询语句（select语句），首先会查询缓存是否已有相应结果，有则返回结果，无则进行下一步（如果不是查询语句，同样调到下一步）

2.解析查询，创建一个内部数据结构（解析树），这个解析树主要用来SQL语句的语义与语法解析；

3.优化：优化SQL语句，例如重写查询，决定表的读取顺序，以及选择需要的索引等。这一阶段用户是可以查询的，查询服务器优化器是如何进行优化的，便于用户重构查询和修改相关配置，达到最优化。这一阶段还涉及到存储引擎，优化器会询问存储引擎，比如某个操作的开销信息、是否对特定索引有查询优化等。

### 1.3.6.高性能的索引使用策略

#### 1.3.6.1.不在索引列上做任何操作

我们通常会看到一些查询不当地使用索引，或者使得MySQL无法使用已有的索引。如果查询中的列不是独立的，则 MySQL就不会使用索引。“独立的列”是指索引列不能是表达式的一部分，也不能是函数的参数。

例如，我们假设id上有主键索引，但是下面这个查询无法使用主键索引:

```
EXPLAIN SELECT * FROM order_exp WHERE id + 1 = 17;
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/4654e2c912994f258e99f87a7fbf722c.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/8b61405caded4ebb9cf0aa43e97db2ab.png)

凭肉眼很容易看出 WHERE中的表达式其实等价于id= 16，但是MySQL无法自动解析这个方程式。这完全是用户行为。我们应该养成简化WHERE条件的习惯，始终将索引列单独放在比较符号的一侧。

下面是另一个常见的错误:

在索引列上使用函数，也是无法利用索引的。

```
EXPLAIN SELECT * from order_exp WHERE YEAR(insert_time)=YEAR(DATE_SUB(NOW(),INTERVAL 1 YEAR));
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/40f54f165b8b45138d0adf947eb013b4.png)

```
EXPLAIN SELECT * from order_exp WHERE insert_time BETWEEN str_to_date('01/01/2021', '%m/%d/%Y') and str_to_date('12/31/2021', '%m/%d/%Y');
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/d8e9925bf3b445a3812aeca5ab3caa9c.png)

#### 1.3.6.2.尽量全值匹配

建立了联合索引列后，如果我们的搜索条件中的列和索引列一致的话，这种情况就称为全值匹配，比方说下边这个查找语句：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/2ef49edd0615433c8d878da02793f414.png)

```
 EXPLAIN select * from order_exp where insert_time='2021-03-22 18:34:55' and order_status=0 and expire_time='2021-03-22 18:35:14';
```

我们建立的u_idx_day_statusr索引包含的3个列在这个查询语句中都展现出来了，联合索引中的三个列都可能被用到。

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/d8ba5a3726cc4fc59bdd677cbfe314b7.png)

有的同学也许有个疑问，WHERE子句中的几个搜索条件的顺序对查询结果有啥影响么？也就是说如果我们调换 `insert_time`, `order_status`, `expire_time`这几个搜索列的顺序对查询的执行过程有影响么？比方说写成下边这样：

```
EXPLAIN select * from order_exp where  order_status=0 and insert_time='2021-03-22 18:34:55'  and expire_time='2021-03-22 18:35:14';
```

放心，MySQL没这么蠢，查询优化器会分析这些搜索条件并且按照可以使用的索引中列的顺序来决定先使用哪个搜索条件，后使用哪个搜索条件。

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/5341da5a2f8c4d548496e938571446fe.png)

所以，当建立了联合索引列后，能在where条件中使用索引的尽量使用。

#### 1.3.6.3.最佳左前缀法则

建立了联合索引列，如果搜索条件不够全值匹配怎么办？在我们的搜索语句中也可以不用包含全部联合索引中的列，但要遵守最左前缀法则。指的是查询从索引的最左前列开始并且不跳过索引中的列。

搜索条件中必须出现左边的列才可以使用到这个B+树索引

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/6470ee4f75b54fe9a3895a04a285445e.png)

```
EXPLAIN select * from order_exp where insert_time='2021-03-22 18:23:42' and order_status=1;
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/d6c0f39567d44f488b33673d7426fae1.png)

```
EXPLAIN select * from order_exp where insert_time='2021-03-22 18:23:42' ;
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/2cb52dc41f2d467485a6540a03fdad13.png)

搜索条件中没有出现左边的列不可以使用到这个B+树索引

```
EXPLAIN SELECT * FROM order_exp WHERE order_status=1;
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/2be581275fda43d9bde9e919ca08edea.png)

```
EXPLAIN Select * from s1 where order_status=1 and expire_time='2021-03-22 18:35:14';
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/6904ca07e50942b9a89624601b7e76d5.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/8c5afbb6141042729c9cb6b62eae9be3.png)

那为什么搜索条件中必须出现左边的列才可以使用到这个B+树索引呢？比如下边的语句就用不到这个B+树索引么？

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/6d37e1eeeac044c8935919a484dc12f4.png)

因为B+树的数据页和记录先是按照insert_time列的值排序的，在insert_time列的值相同的情况下才使用order_status列进行排序，也就是说insert_time列的值不同的记录中order_status的值可能是无序的。而现在你跳过insert_time列直接根据order_status的值去查找，怎么可能呢？expire_time也是一样的道理，那如果我就想在只使用expire_time的值去通过B+树索引进行查找咋办呢？这好办，你再对expire_time列建一个B+树索引就行了。

但是需要特别注意的一点是，如果我们想使用联合索引中尽可能多的列，搜索条件中的各个列必须是联合索引中从最左边连续的列。比方说联合索引u_idx_day_status中列的定义顺序是 `insert_time`, `order_status`, `expire_time`，如果我们的搜索条件中只有insert_time和expire_time，而没有中间的order_status，

```
EXPLAIN select * from order_exp where insert_time='2021-03-22 18:23:42' and expire_time='2021-03-22 18:35:14';
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/71c66aeee5624538b15c1ac65bfb441c.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/b0c30125c76547549274176558ba4eac.png)

请注意key_len,只有5，说明只有insert_time用到了，其他的没有用到。

#### 1.3.6.4.范围条件放最后

这一点，也是针对联合索引来说的，前面我们反复强调过，所有记录都是按照索引列的值从小到大的顺序排好序的，而联合索引则是按创建索引时的顺序进行分组排序。

比如：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/c6343d4b9e404154a5d9542ab0991961.png)

```
EXPLAIN select * from order_exp_cut where insert_time>'2021-03-22 18:23:42' and insert_time<'2021-03-22 18:35:00';
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/288265c4c0ef489eb6fd23f908389ba4.png)

由于B+树中的数据页和记录是先按insert_time列排序的，所以我们上边的查询过程其实是这样的：

找到insert_time值为'2021-03-22 18:23:42' 的记录。

找到insert_timee值为'2021-03-22 18:35:00'的记录。

由于所有记录都是由链表连起来的，所以他们之间的记录都可以很容易的取出来，找到这些记录的主键值，再到聚簇索引中回表查找完整的记录。

但是如果对多个列同时进行范围查找的话，只有对索引最左边的那个列进行范围查找的时候才能用到B+树索引：

```
select * from order_exp_cut where insert_time>'2021-03-22 18:23:42' and insert_time<'2021-03-22 18:35:00' and order_status > -1;
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/b4ef55a0bbb043aa9fb6ea7aea4014d1.png)

上边这个查询可以分成两个部分：

通过条件insert_time>'2021-03-22 18:23:42' and insert_time&#x3c;'2021-03-22 18:35:00' 来对insert_time进行范围，查找的结果可能有多条insert_time值不同的记录，

对这些insert_time值不同的记录继续通过order_status>-1条件继续过滤。

这样子对于联合索引u_idx_day_status来说，只能用到insert_time列的部分，而用不到order_status列的部分（这里的key_len和之前的SQL的是一样长），因为只有insert_time值相同的情况下才能用order_status列的值进行排序，而这个查询中通过insert_time进行范围查找的记录中可能并不是按照order_status列进行排序的，所以在搜索条件中继续以order_status列进行查找时是用不到这个B+树索引的。

**所以对于一个联合索引来说，虽然对多个列都进行范围查找时只能用到最左边那个索引列，但是如果左边的列是精确查找，则右边的列可以进行范围查找：**

```
EXPLAIN select * from order_exp_cut
where insert_time='2021-03-22 18:34:55' and order_status=0 and expire_time>'2021-03-22
18:23:57' and expire_time<'2021-03-22 18:35:00' ;
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/591940f39f1b4b38aa5b32e55202bd60.png)

**而中间有范围查询会导致后面的列全部失效，无法充分利用这个联合索引：**

```
EXPLAIN select * from order_exp_cut
where insert_time='2021-03-22 18:23:42' and order_status>-1 and expire_time='2021-03-22
18:35:14';
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/5874bb991dc1459cabd34bfa0bc7299a.png)

#### 1.3.6.5.覆盖索引尽量用

覆盖索引是非常有用的工具，能够极大地提高性能，三星索引里最重要的那颗星就是宽索引星。考虑一下如果查询只需要扫描索引而无须回表，会带来多少好处:

索引条目通常远小于数据行大小，所以如果只需要读取索引，那 MySQL就会极大地减少数据访问量。这对缓存的负载非常重要，因为这种情况下响应时间大部分花费在数据拷贝上。覆盖索引对于I/O密集型的应用也有帮助，因为索引比数据更小,更容易全部放入内存中。

因为索引是按照列值顺序存储的，所以对于I/O密集型的范围查询会比随机从磁盘读取每一行数据的I/O要少得多。

由于InnoDB的聚簇索引，覆盖索引对InnoDB表特别有用。InnoDB的二级索引在叶子节点中保存了行的主键值，所以如果二级主键能够覆盖查询，则可以避免对主键索引的二次查询。

尽量使用覆盖索引(只访问索引的查询(索引列和查询列一致))，不是必要的情况下减少select*，除非是需要将表中的全部列检索后，进行缓存。

```
EXPLAIN  select * from
order_exp_cut where insert_time='2021-03-22 18:34:55' and order_status=0 and
expire_time='2021-03-22 18:35:04' ;
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/9dde17c64e9648cd8c41d8ed8e3b2b65.png)

使用具体名称取代*

```
EXPLAIN  select expire_time,id from
order_exp_cut where insert_time='2021-03-22 18:34:55' and order_status=0 and
expire_time='2021-03-22 18:35:04' ;
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/c50ef9c9280f4d8e94cf27cca596f9c1.png)

**解释一下Extra中的Using index**

当我们的查询列表以及搜索条件中只包含属于某个索引的列，也就是在可以**使用索引覆盖的情况**下，在Extra列将会提示该额外信息。以上的查询中只需要用到u_idx_day_status而不需要回表操作：

#### 1.3.6.6.不等于要慎用

mysql 在使用不等于(!= 或者&#x3c;>)的时候无法使用索引会导致全表扫描

```
EXPLAIN  SELECT * FROM order_exp WHERE order_no <> 'DD00_6S';
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/d75a6e6d69f547caa3b8661b0a369973.png)

**解释一下Extra中的Using where**
当我们使用全表扫描来执行对某个表的查询，并且该语句的WHERE子句中有针对该表的搜索条件时，在Extra列中会提示上述额外信息。

#### 1.3.6.7.Null/Not 有影响

需要注意null/not null对索引的可能影响

**表order_exp的order_no为索引列，同时不允许为null，**

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/8ed4193b0c934d5dbbbc34f8dd581836.png)

```
explain SELECT * FROM order_exp WHERE order_no is null;
explain SELECT * FROM order_exp WHERE order_no is not null;
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/aa527c85faf945e6a81faaa7a0025409.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/ec817b8cf6e5488bb6e9382e503828f0.png)

可以看见，order_no is null的情况下，MySQL直接表示Impossible WHERE(查询语句的WHERE子句永远为FALSE时将会提示该额外信息)，对于 is not null直接走的全表扫描。

**表order_exp_cut的order_no为索引列，同时允许为null，**

```
explain SELECT * FROM order_exp_cut WHERE order_no is null;
explain SELECT * FROM order_exp_cut WHERE order_no is not null;
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/227c7a3ab927457d84739f1c3583ccdd.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/d954036891374b18a6ef0671d793cd86.png)

is null会走ref类型的索引访问，is not null;依然是全表扫描。所以总结起来：

is not null容易导致索引失效，is null则会区分被检索的列是否为null，如果是null则会走ref类型的索引访问，如果不为null，也是全表扫描。

**但是当联合索引上使用时覆盖索引时，情况会有一些不同(order_exp_cut表的order_no可为空)：**

```
explain SELECT order_status,expire_time FROM order_exp WHERE insert_time is null;
explain SELECT order_status,expire_time FROM order_exp WHERE insert_time is not null;
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/14d36c91cf0840a2b2be921b057e6f7a.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/42ebdd9dd8774f0d939440cde50512e1.png)

```
explain SELECT order_status,expire_time FROM order_exp_cut WHERE insert_time is null;
explain SELECT order_status,expire_time FROM order_exp_cut WHERE insert_time is not null;
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/d2fc5cb60d1c455e92b38dd4f1c87ebe.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/50565fb21ad145d89d0329c126aca8cf.png)

根据system>const>eq_ref>ref>range>index>ALL 的原则，看起来在联合索引中，is not null的表现会更好（如果列可为null的话），但是key_len的长度增加了1。所以总的来说，在设计表时列尽可能的不要声明为null。

#### 1.3.6.8.Like查询要当心

like以通配符开头('%abc...')，mysql索引失效会变成全表扫描的操作

```
explain SELECT * FROM order_exp WHERE order_no like '%_6S';
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/ac911fc11114479caa8ae55ac317bacf.png)

此时如果使用覆盖索引可以改善这个问题

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/0dd075168f3e48d69eca71710c72ed9e.png)

```
explain SELECT order_status,expire_time FROM order_exp_cut WHERE insert_time like '%18:35:09';
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/e494db4f81c846db89e74e6d23cdc646.png)

#### 1.3.6.9.字符类型加引号

字符串不加单引号索引失效

```
explain SELECT * FROM order_exp WHERE order_no = 6;
explain SELECT * FROM order_exp WHERE order_no = '6';
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/511255e7474c4502b15419058913d0cc.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/97f9ff147b5a4954aaf006f00b60660d.png)

MySQL的查询优化器，会自动的进行类型转换，比如上个语句里会尝试将order_no转换为数字后和6进行比较，自然造成索引失效。

#### 1.3.6.10.使用or关键字时要注意

```
explain SELECT * FROM order_exp WHERE order_no = 'DD00_6S' OR order_no = 'DD00_9S';
explain SELECT * FROM order_exp WHERE expire_time= '2021-03-22 18:35:09'  OR order_note = 'abc';
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/55f8e2400c4845e5b337c1a122ea4737.png)

表现是不一样的，第一个SQL的or是相同列，相当于产生两个扫描区间，可以使用上索引。

第二个SQL中or是不同列，并且order_note不是索引。所以只能全表扫描

当然如果两个条件都是索引列，情况会有变化：

```
explain  SELECT * FROM order_exp WHERE expire_time= '2021-03-22 18:35:09'  OR order_no = 'DD00_6S';
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/deabc3433e2440c5be499b296789d427.png)

这也给了我们提示，如果我们将 SQL改成union all

```
explain SELECT * FROM order_exp WHERE expire_time= '2021-03-22 18:35:09' 
					union all SELECT * FROM order_exp WHERE order_note = 'abc';
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/643d0629a531459594e318cc0ea6547b.png)

当然使用覆盖扫描也可以改善这个问题：

```
explain SELECT order_status,id FROM order_exp_cut WHERE insert_time='2021-03-22 18:34:55' or expire_time='2021-03-22 18:28:28';
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/aa9bc2fae8c54d4b86a3a38720cc42c2.png)

#### 1.3.6.11.使用索引扫描来做排序和分组

MySQL有两种方式可以生成有序的结果﹔通过排序操作﹔或者按索引顺序扫描施﹔如果EXPLAIN出来的type列的值为“index”，则说明MySQL使用了索引扫描来做排序。

扫描索引本身是很快的，因为只需要从一条索引记录移动到紧接着的下一条记录。但如果索引不能覆盖查询所需的全部列，那就不得不每扫描一条索引记录就都回表查询一次对应的行。这基本上都是随机I/O，因此按索引顺序读取数据的速度通常要比顺序地全表扫描慢，尤其是在IO密集型的工作负载时。

MySQL可以使用同一个索引既满足排序，又用于查找行。因此，如果可能，设计索引时应该尽可能地同时满足这两种任务，这样是最好的。

只有当索引的列顺序和ORDER BY子句的顺序完全一致，并且所有列的排序方向（倒序或正序）都一样时，MySQL才能够使用索引来对结果做排序。如果查询需要关联多张表，则只有当0RDER BY子句引用的字段全部为第一个表时，才能使用索引做排序。

#### 1.3.6.12.排序要当心

**ASC、DESC别混用**

对于使用联合索引进行排序的场景，我们要求各个排序列的排序顺序是一致的，也就是要么各个列都是ASC规则排序，要么都是DESC规则排序。

**排序列包含非同一个索引的列**

用来排序的多个列不是一个索引里的，这种情况也不能使用索引进行排序

```
explain
SELECT * FROM order_exp order by
order_no,insert_time;
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/52bc3ba85bc1433cbed4510cba638556.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/645c2fa335824da292d3dcfcb32969e8.png)

#### 1.3.6.13.尽可能按主键顺序插入行

最好避免随机的（不连续且值的分布范围非常大）聚簇索引，特别是对于I/O密集型的应用。例如，从性能的角度考虑，使用UUID来作为聚簇索引则会很糟糕，它使得聚簇索引的插入变得完全随机，这是最坏的情况，使得数据没有任何聚集特性。

最简单的方法是使用AUTO_INCREMENT自增列。这样可以保证数据行是按顺序写入，对于根据主键做关联操作的性能也会更好。

注意到向UUID主键插入行不仅花费的时间更长，而且索引占用的空间也更大。这一方面是由于主键字段更长﹔另一方面毫无疑问是由于页分裂和碎片导致的。

因为主键的值是顺序的，所以InnoDB把每一条记录都存储在上一条记录的后面。当达到页的最大填充因子时(InnoDB默认的最大填充因子是页大小的15/16，留出部分空间用于以后修改)，下一条记录就会写入新的页中。一旦数据按照这种顺序的方式加载,主键页就会近似于被顺序的记录填满,这也正是所期望的结果。

如果新行的主键值不一定比之前插入的大，所以InnoDB无法简单地总是把新行插入到索引的最后，而是需要为新的行寻找合适的位置-—通常是已有数据的中间位置——并且分配空间。这会增加很多的额外工作，并导致数据分布不够优化。下面是总结的一些缺点:

写入的目标页可能已经刷到磁盘上并从缓存中移除，或者是还没有被加载到缓存中，InnoDB在插入之前不得不先找到并从磁盘读取目标页到内存中。这将导致大量的随机IO。

因为写入是乱序的，InnoDB不得不频繁地做页分裂操作，以便为新的行分配空间。页分裂会导致移动大量数据，一次插入最少需要修改三个页而不是一个页。

所以使用InnoDB时应该尽可能地按主键顺序插入数据，并且尽可能地使用单调增加的聚簇键的值来插入新行。

#### 1.3.6.14.优化Count查询

首先要注意，COUNT()是一个特殊的函数，有两种非常不同的作用:它可以统计某个列值的数量，也可以统计行数。

在统计列值时要求列值是非空的（不统计NULL)。

COUNT()的另一个作用是统计结果集的行数。常用的就是就是当我们使用COUNT(*)。实际上，它会忽略所有的列而直接统计所有的行数。

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/3264f862df374302bef83c9459ad0a7a.png)

```
select count(*) from test;
select count(c1) from test;
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/989e64fc120f45288787f480e1746dc1.png)![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/52fccea24657442db67c3d7b102de0fa.png)

通常来说，COUNT()都需要扫描大量的行（意味着要访问大量数据）才能获得精确的结果，因此是很难优化的。在MySQL层面能做的基本只有索引覆盖扫描了。如果这还不够,就需要考虑修改应用的架构，可以用估算值取代精确值，可以增加汇总表，或者增加类似Redis这样的外部缓存系统。

#### 1.3.6.15.优化limit分页

在系统中需要进行分页操作的时候，我们通常会使用LIMIT加上偏移量的办法实现，同时加上合适的ORDER BY子句。

一个非常常见又令人头疼的问题就是，在偏移量非常大的时候，例如可能是

```
select * from order_exp limit 10000,10;
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/358846c9b2db4bf79de4e2f200c5e46f.png)

这样的查询，这时MySQL需要查询10010条记录然后只返回最后10条，前面10 000条记录都将被抛弃，这样的代价非常高。

优化此类分页查询的一个最简单的办法是

会先查询翻页中需要的N条数据的主键值，然后根据主键值回表查询所需要的N条数据，在此过程中查询N条数据的主键id在索引中完成，所以效率会高一些。

```
EXPLAIN SELECT * FROM (select id from order_exp limit 10000,10) b,order_exp
					a where a.id = b.id;
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/b24ab67fa56e4da1b7fa151e0098c004.png)

从执行计划中可以看出，首先执行子查询中的order_exp表，根据主键做索引全表扫描，然后与a表通过id做主键关联查询，相比传统写法中的全表扫描效率会高一些。

从两种写法上能看出性能有一定的差距，虽然并不明显，但是随着数据量的增大，两者执行的效率便会体现出来。

上面的写法虽然可以达到一定程度的优化，但还是存在性能问题。最佳的方式是在业务上进行配合修改为以下语句：

```
EXPLAIN select * from order_exp where id > 67 order by id limit 10;
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/6efb18da3d19465e8538cb4e042d9e86.png)

采用这种写法，需要前端通过点击More来获得更多数据，而不是纯粹的翻页，因此，每次查询只需要使用上次查询出的数据中的id来获取接下来的数据即可，但这种写法需要业务配合。

#### 1.3.6.16.关于Null的特别说明

对于Null到底算什么，存在着分歧：

1、有的认为NULL值代表一个未确定的值，MySQL认为任何和NULL值做比较的表达式的值都为NULL，包括select
null=null和select null!=null;

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/11ebee5ff9db49b6bef2e80d2b2e46bd.png)![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/3e152ca5c31048a5afca4a7611bc5798.png)

所以每一个NULL值都是独一无二的。

2、有的认为其实NULL值在业务上就是代表没有，所有的NULL值和起来算一份；

3、有的认为这NULL完全没有意义，所以在统计数量时压根儿不能把它们算进来。

假设一个表中某个列c1的记录为(2,1000,null,null)，在第一种情况下，表中c1的记录数为4，第二种表中c1的记录数为3，第三种表中c1的记录数为2。

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1651212459071/09c50dcca1ab4f33b2247edb054905ae.png)

在对统计索引列不重复值的数量时如何对待NULL值，MySQL专门提供了一个innodb_stats_method的系统变量，

https://dev.mysql.com/doc/refman/5.7/en/innodb-parameters.html#sysvar_innodb_stats_method

**这个系统变量有三个候选值：**

nulls_equal：认为所有NULL值都是相等的。这个值也是innodb_stats_method的默认值。

如果某个索引列中NULL值特别多的话，这种统计方式会让优化器认为某个列中平均一个值重复次数特别多，所以倾向于不使用索引进行访问。

nulls_unequal：认为所有NULL值都是不相等的。

如果某个索引列中NULL值特别多的话，这种统计方式会让优化器认为某个列中平均一个值重复次数特别少，所以倾向于使用索引进行访问。

nulls_ignored：直接把NULL值忽略掉。

而且有迹象表明，在MySQL5.7.22以后的版本，对这个innodb_stats_method的修改不起作用，MySQL把这个值在代码里写死为nulls_equal。也就是说MySQL在进行索引列的数据统计行为又把null视为第二种情况（NULL值在业务上就是代表没有，所有的NULL值和起来算一份），看起来，MySQL中对Null值的处理也很分裂。所以总的来说，对于列的声明尽可能的不要允许为null。
