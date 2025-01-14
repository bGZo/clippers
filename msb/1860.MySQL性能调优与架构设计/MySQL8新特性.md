## 1.7.	**MySQL8新特性**

对于 MySQL 5.7 版本，其将于 2023年 10月31日 停止支持。后续官方将不再进行后续的代码维护。

MySQL 8.0 全内存访问可以轻易跑到 200W QPS，I/O 极端高负载场景跑到 16W QPS，除此之外MySQL 8还新增了很多功能，那么我们来一起看一下。

### 1.7.1. 账户与安全

#### 1.7.1.1. 用户创建和授权

到了MySQL8中，用户创建与授权语句必须是分开执行，之前版本是可以一起执行。

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1653544165079/de3ffd4b519443439bdbd8c543c14a32.png)

**MySQL8的版本**

```
grant all privileges on *.* to 'lijin'@'%' identified by 'Lijin@2022';
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1653544165079/69ff061c543848569f28443f48fd3d2a.png)

```
create user 'lijin'@'%' identified by 'Lijin@2022';
grant all privileges on *.* to 'lijin'@'%'；
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1653544165079/377e9651c03148b09f1255b47c4f2e19.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1653544165079/b2a6e6d4d2f741838c8ca70c7da75693.png)

**MySQL5.7的版本**

```
grant all privileges on *.* to 'lijin'@'%' identified by 'Lijin@2022';
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1653544165079/cf816534a0734330acfc5d993b55310b.png)

#### 1.7.1.2. 认证插件更新

MySQL 8.0中默认的身份认证插件是caching_sha2_password，替代了之前的mysql_native_password。

```
show variables like 'default_authentication%';
```

**5.7版本**

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1653544165079/015cd62f5aa14b5887464c8562b5dd98.png)

**8版本**

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1653544165079/13929213dfb0439fa2373b969d19115d.png)

```
select user, host,plugin from mysql.user;
```

这个带来的问题就是如果客户端没有更新，就连接不上！！

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1653544165079/662464a5e80a4fcb8ad498c5adcc7b80.png)

当然可以通过在MySQL的服务端找到my.cnf的文件，把相关参数进行修改（不过要MySQL重启后才能生效）

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1653544165079/d8fc4c99b4d444ca8a2793f6f55cb6b8.png)

如果没办法重启服务，还有一种动态的方式：

```
alter user 'lijin'@'%' identified with mysql_native_password by 'Lijin@2022';
select host,user from mysql.user;
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1653544165079/4a96e29ae52f46d7815fc1af6fb2f151.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1653544165079/1abfde3fba0a4945b526d51ba098bb26.png)

使用老的Navicat for MySQL也能访问

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1653544165079/43c1bfc3251e4fa68354a57d9a15bd5e.png)

#### 1.7.1.3. 密码管理

MySQL 8.0开始允许限制重复使用以前的密码（修改密码时）。

并且还加入了密码的修改管理功能

```
show variables like 'password%';
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1653544165079/06b3320142bd41459b9ace0126211d88.png)

修改策略（全局级）

```
set persist password_history=3;        --修改密码不能和最近3次一致
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1653544165079/e85e65e80db64732b894b7a116401335.png)

修改策略（用户级）

```
alter user 'lijin'@'%' password history 3;
```

```
select user, host,Password_reuse_history from mysql.user;
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1653544165079/e7f298fd623a497b9b4af57d5afb0a2c.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1653544165079/6e3f3b85114d492faa8eadaea67038f4.png)使用重复密码修改用户密码(指定lijin用户)

```
alter user 'lijin'@'%' identified by 'Lijin@2022';
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1653544165079/e7d506e7e3e044238354b7a1db369012.png)如果我们把全局的参数改为0，则对于root用户可以反复的修改密码

```
alter user 'root'@'localhost' identified by '789456';
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1653544165079/8eac02053e2f4e0e9686d997e2431c60.png)

password_reuse_interval   则是按照天数来限定（不允许重复的）

password_require_current    是否需要校验旧密码（off 不校验、 on校验）(针对非root用户)

```
set persist password_require_current=on;
```

### 1.7.2. 索引增强

#### 1.7.2.1. 隐藏索引

MySQL 8.0开始支持隐藏索引 (invisible index)，不可见索引.

隐藏索引不会被优化器使用，但仍然需要进行维护。
应用场景: 软删除、灰度发布。

软删除：就是我们在线上会经常删除和创建索引，如果是以前的版本，我们如果删除了索引，后面发现删错了，我又需要创建一个索引，这样做的话就非常影响性能。在MySQL8中我们可以这么操作，把一个索引变成隐藏索引（索引就不可用了，查询优化器也用不上），最后确定要进行删除这个索引我们才会进行删除索引操作。

灰度发布：也是类似的，我们想在线上进行一些测试，可以先创建一个隐藏索引，不会影响当前的生产环境，然后我们通过一些附加的测试，发现这个索引没问题，那么就直接把这个索引改成正式的索引，让线上环境生效。

**使用案例（灰度发布）：**

```
create table t1(i int,j int);  --创建一张t1表
create index i_idx on t1(i);  --创建一个正常索引
create index j_idx on t1(j) invisible;  --创建一个隐藏索引
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1653544165079/c73a1f8ec0714350aa7ba3cca4b510ef.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1653544165079/b0acbc1caa464f3082cc44f44838bee7.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1653544165079/04da87a0e2ed4fb2bf8e2393b67a30f1.png)

```
show index from t1\G         --查看索引信息
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1653544165079/11f5ca11849c4323be34c1f3713d9a2a.png)

使用查询优化器看下：

```
explain select * from t1 where i=1;
explain select * from t1 where j=1;
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1653544165079/168794969d3b42a2ad224643c6d1cfc7.png)

这里可以看到隐藏索引不会用上。

这里可以通过优化器的开关，打开一个设置，方便我们对隐藏索引进行设置。

```
select @@optimizer_switch\G;   --查看 各种参数
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1653544165079/0ab72a3fea784b3397319fadde1293b0.png)

红色的部分就是默认查询优化器对隐藏索引不可见，我们可以通过参数进行修改。确保我们可以用隐藏索引进行测试。

```
set session optimizer_switch="use_invisible_indexes=on';   --在会话级别设置查询优化器可以看到隐藏索引
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1653544165079/d4b7225269b64c728ed749f7b2f5d79b.png)

再使用查询优化器看下：

```
explain select * from t1 where j=1;
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1653544165079/dba6db5fe1e04e418fccd1f47718df9f.png)

把隐藏索引变成可见索引（正常索引）

```
alter table t1 alter index j_idx visible;   --变成可见
alter table t1 alter index j_idx invisible;   --变成不可见(隐藏索引)
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1653544165079/e4735a743ec14fcba847a9fac18b0798.png)

**最后一点，不能把主键设置成不可见的索引（隐藏索引）（MySQL做了限制）**

#### 1.7.2.2. 降序索引

MySQL 8.0开始真正支持降序索引 (descendingindex) 。只有InnoDB存储引擎支持降序索引，只支持BTREE降序索引。另外MySQL8.0不再对GROUP BY操作进行隐式排序。

在MySQL中创建一个t2表

```
create table t2(c1 int,c2 int,index idx1(c1 asc,c2 desc));

show create table t2\G

```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1653544165079/75d8a1f112174a0eae3bdcc329844c80.png)

如果是5.7中，则没有显示升序还是降序信息

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1653544165079/44eda4306a624a77ae6f4c9bf3811143.png)

我们插入一些数据，给大家演示下降序索引的使用

```
insert into t2(c1,c2) values(1,100),(2,200),(3,150),(4,50);
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1653544165079/6c688fd5a39342a08158c5cdecc8592b.png)

看下索引使用情况

```
explain select * from t2 order by c1,c2 desc;
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1653544165079/74a77cd932174740a18b3b6b28e19617.png)

我们在5.7对比一下

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1653544165079/9dfcf7f4f605455b851f3ae64c5b2fa5.png)

这里说明，这里需要一个额外的排序操作，才能把刚才的索引利用上。

我们把查询语句换一下

```
explain select * from t2 order by c1 desc,c2 ;
```

MySQL8中使用了

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1653544165079/00d9db6d7c71430a955e7107a0678461.png)

另外还有一点，就是group by语句在 8之后不再默认排序

```
select count(*),c2 from t2 group by c2;
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1653544165079/e51a002e1f034c15bad26b7781532518.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1653544165079/4bbbf1e99fa847479e232377e5d66a77.png)

在8要排序的话，就需要手动把排序语句加上

```
select count(*),c2 from t2 group by c2 order by c2;
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1653544165079/23c4a24d51db40e4aaae81792d4b8a40.png)

#### 1.7.2.3. 函数索引

之前我们知道，如果在查询中加入了函数，索引不生效，所以MySQL8引入了函数索引。

MySQL 8.0.13开始支持在索引中使用函数（表达式)的值。支持降序索引，支持JSON 数据的索引
函数索引基于虚拟列功能实现。

**使用函数索引（表达式）**

```
create table t3(c1 varchar(10),c2 varchar(10));
create index idx_c1 on t3(c1);   --普通索引
create index func_idx on t3( (UPPER(c2)) );   --一个大写的函数索引

```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1653544165079/47d2fd6adec142cf9dfde5c0cb677495.png)

```
show index from t3\G
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1653544165079/d8508066bd504ba0897c5a2d25b85bf5.png)

```
explain select * from t3 where upper(c1)='ABC' ;  
explain select * from t3 where upper(c2)='ABC' ;
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1653544165079/7bfb171eb5c3483ba2d8ec79399c8261.png)

**使用函数索引（JSON）**

```
create table t4(data json，index((CAST(data->>'$.name' as char(25)) )));
explain select * from t4 where CAST(data->>'$.name' as char(25)) = 'lijin ';
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1653544165079/45a6485744a9438da17953c4df4d83fd.png)

**函数索引基于虚拟列功能实现**

函数索引在MySQL中相当于新增了一个列，这个列会根据你的函数来进行计算结果，然后使用函数索引的时候就会用这个计算后的列作为索引。

### 1.7.3. 通用表表达式（CTE）

MySQL8.0开始支持通用表表达式(CTE）(common table expression)，即WITH子句。

**简单入门：**

以下SQL就是一个简单的CTE表达式，类似于递归调用，这段SQL中，首先执行select 1 然后得到查询结果后把这个值n送入 union all下面的 select n+1 from cte where n &#x3c;10,然后一直这样递归调用union all下面sql语句。

```
WITH recursive cte(n) as 
( select 1
  union ALL
  select n+1 from cte where n<10
)
select * from cte;
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1653544165079/7f73594320584b3ca192eec1fdee9389.png)

**案例介绍：**

一个staff表，里面有id，有name还有一个 m_id，这个是对应的上级id。数据如下：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1653544165079/faecda299a6e4117b9b60a9f41e09a9b.png)

如果我们想查询出每一个员工的上下级关系，可以使用以下方式

递归CTE：

```
with recursive staff_view(id,name,m_id) as
(select id ,name ,cast(id as char(200)) 
 from staff where m_id =0
 union ALL 
 select s2.id ,s2.name,concat(s1.m_id,'-',s2.id)
 from staff_view as s1 join  staff as s2
 on s1.id = s2.m_id
)
select * from staff_view order by id
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1653544165079/ca7f4cfa8b80461c919ab34a5931decb.png)

使用通用表表达式的好处就是上下级层级就算有4，5，6甚至更多层，都可以帮助我们遍历出来，而老的方式的写法SQL语句就要调整。

**总结：**

通用表表达式与派生表类似，就像语句级别的临时表或视图。CTE可以在查询中多次引用，可以引用其他CTE，可以递归。CTE支持SELECT/INSERT/UPDATE/DELETE等语句。

### 1.7.4. 窗口函数

MySQL 8.0支持窗口函数(Window Function)，也称分析函数。窗口函数与分组聚合函数类似，但是每一行数据都生成一个结果。聚合窗口函数: SUM /AVG / COUNT /MAX/MIN等等。

案例如下：sales表结构与数据如下：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1653544165079/55a0f2e91f0b4ff99d807c997899bd85.png)

普通的分组、聚合（以国家统计）

```
SELECT country,sum(sum)
FROM sales
GROUP BY country
order BY country;
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1653544165079/2f621f4802de415aa8e41152f0e96e67.png)

窗口函数（以国家汇总）

```
select year,country,product,sum,
	sum(sum) over (PARTITION by country) as country_sum
 from sales
order by country,year,product,sum;
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1653544165079/119d39d7e7b4425bb79873cf1e532d30.png)

窗口函数（计算平局值）

```
select year,country,product,sum,
			sum(sum) over (PARTITION by country) as country_sum,
			avg(sum) over (PARTITION by country) as country_avg
 from sales
order by country,year,product,sum;
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1653544165079/b1efa7b8456e43949f4b46aec9b12a70.png)

专用窗口函数：

* 序号函数：ROW_NUMBER()、RANK()、DENSE_RANK()
* 分布函数：PERCENT_RANK()、CUME_DIST()
* 前后函数：LAG()、LEAD()
* 头尾函数：FIRST_VALUE()、LAST_VALUE()
* 其它函数：NTH_VALUE()、NTILE()

![](https://img-blog.csdnimg.cn/img_convert/81e045c22f5b474b17ba33c0c2250c49.png)

**窗口函数（排名）**

用于计算分类排名的排名窗口函数，以及获取指定位置数据的取值窗口函数

```
SELECT
	YEAR,
	country,
	product,
	sum,
	row_number() over (ORDER BY sum) AS 'rank',
        rank() over (ORDER BY sum) AS 'rank_1'
FROM
	sales;
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1653544165079/5cca667ce4344608a49ea780d7a69ba3.png)

```
SELECT
	YEAR,
	country,
	product,
	sum,
	sum(sum) over (PARTITION by country order by sum rows unbounded preceding) as sum_1
FROM
	sales order by country,sum;
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1653544165079/24c5c7cd8cf44dee84e869ee5dfaadc3.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1653544165079/a96976f74acc4b3ab445bb22e6cdece7.png)

当然可以做的操作很多，具体见官网：

[https://dev.mysql.com/doc/refman/8.0/en/window-function-descriptions.html]()

### 1.7.5. 原子DDL操作

MySQL 8.0 开始支持原子 DDL 操作，其中与表相关的原子 DDL 只支持 InnoDB 存储引擎。一个原子 DDL 操作内容包括：更新数据字典，存储引擎层的操作，在 binlog 中记录 DDL 操作。支持与表相关的 DDL：数据库、表空间、表、索引的 CREATE、ALTER、DROP 以及 TRUNCATE TABLE。支持的其他 DDL ：存储程序、触发器、视图、UDF 的 CREATE、DROP 以及ALTER 语句。支持账户管理相关的 DDL：用户和角色的 CREATE、ALTER、DROP 以及适用的 RENAME，以及 GRANT 和 REVOKE 语句。

```
drop table t1,t2;   
```

上面这个语句，如果只有t1表，没有t2表。在MySQL5.7与8 的表现是不同的。

5.7会删除t1表。而在8中因为报错了，整个是一个原子操作，所以不会删除t1表。

### 1.7.6. JSON增强

具体看官网信息，英文好的直接看，英文不好的找个翻译工具即可看懂

[MySQL :: MySQL 8.0 Reference Manual :: 11.5 The JSON Data Type](https://dev.mysql.com/doc/refman/8.0/en/json.html)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1653544165079/1d64831a19c4488089e934b96119686e.png)

### 1.7.7. InnoDB其他改进功能

**自增列持久化**

MySQL 5.7 以及早期版本，InnoDB 自增列计数器（AUTO_INCREMENT）的值只存储在内存中。MySQL 8.0 每次变化时将自增计数器的最大值写入 redo log，同时在每次检查点将其写入引擎私有的系统表。解决了长期以来的自增字段值可能重复的 bug。

**死锁检查控制**

MySQL 8.0 （MySQL 5.7.15）增加了一个新的动态变量，用于控制系统是否执行 InnoDB 死锁检查。对于高并发的系统，禁用死锁检查可能带来性能的提高。

```
innodb_deadlock_detect
```

**锁定语句选项**

SELECT ... FOR SHARE 和 SELECT ... FOR UPDATE 中支持 NOWAIT、SKIP LOCKED 选项。对于 NOWAIT，如果请求的行被其他事务锁定时，语句立即返回。对于 SKIP LOCKED，从返回的结果集中移除被锁定的行。

**InnoDB 其他改进功能。**

* 支持部分快速 DDL，ALTER TABLE ALGORITHM=INSTANT;
* InnoDB 临时表使用共享的临时表空间 ibtmp1。
* 新增静态变量 innodb_dedicated_server，自动配置 InnoDB 内存参数：innodb_buffer_pool_size/innodb_log_file_size 等。
* 默认创建 2 个 UNDO 表空间，不再使用系统表空间。
* 支持 ALTER TABLESPACE ... RENAME TO 重命名通用表空间。
