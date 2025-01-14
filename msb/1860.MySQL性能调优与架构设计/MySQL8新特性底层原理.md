# MySQL8新特性底层原理

## 降序索引

### 什么是降序索引

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

到此为止，大家应该对升序索引和降序索引有了一个大概的了解，但并没有真正理解，因为大家并不知道升序索引与降序索引底层到底是如何实现的。

### 降序索引的底层实现

升序索引对应的B+树

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1656320896043/b595577948f94b2b84de3d79557eb9fc.png)

降序索引对应的B+树 

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1656320896043/d9b945594d154f63b167b3c6c150a99b.png)

如果没有降序索引，查询的时候要实现降序的数据展示，那么就需要把原来默认是升序排序的数据处理一遍（比如利用压栈和出栈操作），而降序索引的话就不需要，所以在优化一些SQL的时候更加高效。

还有一点，现在 **只有Innodb存储引擎支持降序索引** 。

## Doublewrite Buffer的改进

**MySQL5.7**![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1656320896043/d462b4c147bc41148f82bee5564c02b3.png)

**MySQL8.0**

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1656320896043/2b08d8cf75e64ceb909b03ce818cb287.png)

在MySQL 8.0.20 版本之前，doublewrite 存储区位于系统表空间，从 8.0.20 版本开始，doublewrite 有自己独立的表空间文件，这种变更，能够降低doublewrite的写入延迟，增加吞吐量，为设置doublewrite文件的存放位置提供了更高的灵活性。

因为系统表空间在存储中就是一个文件，那么doublewrite必然会受制于这个文件的读写效率（其他向这个文件的读写操作，比如统计、监控等数据操作）

**系统表空间(system tablespace)**

这个所谓的系统表空间可以对应文件系统上一个或多个实际的文件，默认情况下，InnoDB会在数据目录下创建一个名为ibdata1(在你的数据目录下找找看有木有)、大小为12M的文件，这个文件就是对应的系纳表空间在文件系统上的表示。

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/5983/1654000409075/6d3767c7708848ddb0b110e20df12388.png)

而单独的文件必然效率比放在系统表空间效率要高！！！

**新增的参数：**

**innodb_doublewrite_dir**

指定doublewrite文件存放的目录，如果没有指定该参数，那么与innodb数据目录一致(innodb_data_home_dir)，如果这个参数也没有指定，那么默认放在数据目录下面(datadir)。

**innodb_doublewrite_files**

指定doublewrite文件数量，默认情况下，每个buffer pool实例，对应2个doublewrite文件。

**innodb_doublewrite_pages**

一次批量写入的doublewrite页数量的最大值，默认值、最小值与innodb_write_io_threads参数值相同，最大值512。

**innodb_doublewrite_batch_size**

一次批量写入的页数量。默认值为0，取值范围0到256。

## redo log 无锁优化

[MySQL :: MySQL 8.0: New Lock free, scalable WAL design](https://dev.mysql.com/blog-archive/mysql-8-0-new-lock-free-scalable-wal-design/)
